from pydantic import BaseModel
from autogen_core.models import UserMessage
from typing import List
import os
from dotenv import load_dotenv
import string
import json
import openai
import asyncio
from autogen_core import (
    RoutedAgent,
    MessageContext,
    DefaultTopicId,
    message_handler,
    Image,
    FunctionCall,
)
from autogen_core.tools import FunctionTool
from autogen_core.models import (
    ChatCompletionClient,
    LLMMessage,
    SystemMessage,
    AssistantMessage,
)
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

# 대화 히스토리를 저장할 전역 리스트
conversation_log = []

# 역할 이름 한국어 매핑
role_names_kr = {
    "Editor": "편집자",
    "Writer": "작가",
    "Illustrator": "일러스트레이터",
    "User": "사용자"
}

class GroupChatMessage(BaseModel):
    """그룹 채팅에서 사용되는 메시지"""
    body: UserMessage

class RequestToSpeak(BaseModel):
    """에이전트에게 발언 권한을 요청하는 메시지"""
    pass

class BaseGroupChatAgent(RoutedAgent):
    """
    LLM을 사용하는 기본 그룹 채팅 에이전트.
    
    이 클래스는:
    1. 그룹 채팅 메시지를 수신하고 대화 히스토리에 저장
    2. RequestToSpeak 메시지를 받으면 LLM을 호출하여 응답 생성
    3. 생성된 응답을 그룹 채팅 토픽에 발행
    """
    
    def __init__(
        self,
        description: str,
        group_chat_topic_type: str,
        model_client: ChatCompletionClient,
        system_message: str,
    ) -> None:
        super().__init__(description=description)
        self._group_chat_topic_type = group_chat_topic_type
        self._model_client = model_client
        self._system_message = SystemMessage(content=system_message)
        self._chat_history: List[LLMMessage] = []
        
    @message_handler
    async def handle_message(self, message: GroupChatMessage, ctx: MessageContext) -> None:
        """
        그룹 채팅 메시지를 수신하고 대화 히스토리에 추가.
        
        Args:
            message: 수신된 그룹 채팅 메시지
            ctx: 메시지 컨텍스트
        """
        # 대화 히스토리에 메시지 추가
        self._chat_history.extend([
            UserMessage(content=f"Transferred to {message.body.source}", source="system"),
            message.body,
        ])
        
    @message_handler
    async def handle_request_to_speak(self, message: RequestToSpeak, ctx: MessageContext) -> None:
        """
        발언 요청을 받고 LLM 응답 생성 후 그룹에 발행.
        
        Args:
            message: 발언 요청 메시지
            ctx: 메시지 컨텍스트
        """
        # 콘솔에 에이전트 이름 출력 (한국어로)
        agent_name_kr = role_names_kr.get(self.id.type, self.id.type)
        Console().print(Panel(f"[bold cyan]{agent_name_kr}[/bold cyan]", border_style="cyan"))
        
        # 시스템 메시지 추가
        self._chat_history.append(
            UserMessage(
                content=f"Transferred to {self.id.type}, adopt the persona immediately.",
                source="system"
            )
        )
        
        # 디버깅: 전송할 메시지 출력
        print("\n" + "="*80)
        print(f"[DEBUG] Sending to LLM for {self.id.type}")
        print("="*80)
        print(f"System Message: {self._system_message.content[:200]}...")
        print("\nChat History:")
        for idx, msg in enumerate(self._chat_history[-5:]):  # 최근 5개만
            content_preview = str(msg.content)[:100] if hasattr(msg, 'content') else str(msg)[:100]
            print(f"  {idx}: {type(msg).__name__} - {content_preview}...")
        print("="*80 + "\n")
        
        # LLM 호출하여 응답 생성 (content filter 오류 시 재시도)
        max_retries = 3
        completion = None
        
        for attempt in range(max_retries):
            try:
                completion = await self._model_client.create(
                    [self._system_message] + self._chat_history
                )
                break  # 성공하면 루프 탈출
                
            except openai.BadRequestError as e:
                # content_filter 오류 감지
                if hasattr(e, 'response') and 'content_filter' in str(e):
                    if attempt < max_retries - 1:
                        Console().print(f"[yellow]⚠️  Content filter 감지. 재시도 중... (시도 {attempt + 1}/{max_retries})[/yellow]")
                        # 히스토리 축약: 가장 오래된 대화 제거
                        if len(self._chat_history) > 3:
                            self._chat_history = self._chat_history[-3:]
                            Console().print("[yellow]   대화 히스토리를 축약했습니다.[/yellow]")
                        await asyncio.sleep(2)  # 2초 대기
                    else:
                        Console().print(f"[red]❌ {max_retries}회 재시도 후에도 content filter 오류가 계속 발생합니다.[/red]")
                        print("\n" + "!"*80)
                        print(f"[ERROR] Content Filter 오류 for {self.id.type}")
                        print("!"*80)
                        print(f"Error: {str(e)}")
                        print("!"*80 + "\n")
                        raise
                else:
                    raise
                    
            except Exception as e:
                print("\n" + "!"*80)
                print(f"[ERROR] LLM 호출 실패 for {self.id.type}")
                print("!"*80)
                print(f"Error Type: {type(e).__name__}")
                print(f"Error Message: {str(e)}")
                if hasattr(e, 'response'):
                    print(f"Response: {e.response}")
                print("\n전체 프롬프트:")
                print(f"System: {self._system_message.content}")
                print("\nHistory:")
                for idx, msg in enumerate(self._chat_history):
                    print(f"{idx}: {type(msg).__name__}")
                    print(f"   Source: {getattr(msg, 'source', 'N/A')}")
                    print(f"   Content: {str(msg.content)[:500]}")
                print("!"*80 + "\n")
                raise
        
        if completion is None:
            raise RuntimeError("Failed to get completion after all retries")
        
        assert isinstance(completion.content, str)
        
        # 응답을 히스토리에 추가
        self._chat_history.append(
            AssistantMessage(content=completion.content, source=self.id.type)
        )
        
        # 콘솔에 응답 출력
        Console().print(Markdown(completion.content))
        
        # 대화 로그에 추가 (한국어 이름으로)
        agent_name_kr = role_names_kr.get(self.id.type, self.id.type)
        conversation_log.append({
            'role': agent_name_kr,
            'content': completion.content
        })
        
        # 그룹 채팅 토픽에 메시지 발행
        await self.publish_message(
            GroupChatMessage(
                body=UserMessage(content=completion.content, source=self.id.type)
            ),
            topic_id=DefaultTopicId(type=self._group_chat_topic_type),
        )
        
class WriterAgent(BaseGroupChatAgent):
    """동화를 작성하는 작가 에이전트"""
    
    def __init__(
        self, 
        description: str, 
        group_chat_topic_type: str, 
        model_client: ChatCompletionClient
    ) -> None:
        super().__init__(
            description=description,
            group_chat_topic_type=group_chat_topic_type,
            model_client=model_client,
            system_message="""You are a professional children's storybook writer.
            Role: Create educational and positive content for children
            Target: Family-friendly stories for 5-7 year old children
            Theme: Positive values such as courage, friendship, adventure, and problem-solving
            Style: Vivid and imaginative expressions
            Length: Short story of about 2-3 paragraphs
            Safety: All content must be appropriate and positive for children""",
        )

class EditorAgent(BaseGroupChatAgent):
    """작품을 검토하고 피드백을 제공하는 편집자 에이전트"""
    
    def __init__(
        self, 
        description: str, 
        group_chat_topic_type: str, 
        model_client: ChatCompletionClient
    ) -> None:
        super().__init__(
            description=description,
            group_chat_topic_type=group_chat_topic_type,
            model_client=model_client,
            system_message="""You are a children's storybook editor.
            Role: Manage children's storybook production projects and quality review
            Check:
            - Is the content appropriate for children?
            - Does it convey positive and educational messages?
            - Is the story clear and easy to understand?
            - Are there no inappropriate or scary elements?
            Approval: Say 'APPROVED' when all requirements are met""",
        )

class IllustratorAgent(BaseGroupChatAgent):
    """Image Generation을 사용하여 실제 이미지를 생성하는 일러스트레이터 에이전트"""
    
    def __init__(
        self, 
        description: str, 
        group_chat_topic_type: str, 
        model_client: ChatCompletionClient,
        image_client: openai.AsyncOpenAI,  # AsyncAzureOpenAI 대신 AsyncOpenAI 사용
    ) -> None:
        super().__init__(
            description=description,
            group_chat_topic_type=group_chat_topic_type,
            model_client=model_client,
            system_message="""You are a children's storybook illustrator.
            Goal: Create cute and friendly illustrations that children love
            Style: Bright, warm, and safe visuals
            Features: Child-friendly subjects such as animals, robots, and nature
            Colors: Pastel tones, bright and cheerful colors
            Prohibited: Scary elements, violent content, inappropriate expressions
            Tool: Use generate_image function to create images
            Consistency: All images must maintain the same character and style""",
        )
        self._image_client = image_client
        self._image_counter = 0  # 이미지 순서 카운터
        # 이미지 생성 도구 정의
        self._image_gen_tool = FunctionTool(
            self._image_gen,
            name="generate_image",
            description="이미지를 생성하려면 이 도구를 호출하세요."
        )
    
    async def _image_gen(
        self,
        character_appearence: str,
        style_attributes: str,
        worn_and_carried: str,
        scenario: str
    ) -> str:
        """GPT-Image-1을 사용하여 이미지 생성 (429 오류 시 재시도)"""
        prompt = f"Digital painting of a {character_appearence} character with {style_attributes}. Wearing {worn_and_carried}, {scenario}."
        
        max_retries = 3
        retry_delay = 10  # 10초 대기
        
        for attempt in range(max_retries):
            try:
                # 이미지 생성 시작 알림
                if attempt == 0:
                    Console().print("[cyan]🎨 이미지 생성 중... (1024x1024)[/cyan]")
                else:
                    Console().print(f"[cyan]🎨 이미지 재생성 중... (시도 {attempt + 1}/{max_retries})[/cyan]")
                
                response = await self._image_client.images.generate(
                    prompt=prompt,
                    model=os.environ.get("AZURE_OPENAI_IMAGE_DEPLOYMENT"),
                    n=1,
                    size="1024x1024"
                )
                Console().print("[green]✓ 이미지 생성 완료![/green]")
                return response.data[0].b64_json  # type: ignore
            
            except openai.RateLimitError as e:
                if attempt < max_retries - 1:
                    Console().print(f"[yellow]Rate limit error (429). Waiting {retry_delay} seconds before retry... (Attempt {attempt + 1}/{max_retries})[/yellow]")
                    await asyncio.sleep(retry_delay)
                else:
                    Console().print(f"[red]Failed to generate image after {max_retries} attempts due to rate limit.[/red]")
                    raise
            
            except Exception as e:
                # 다른 예외의 경우 status code 확인
                if hasattr(e, 'status_code') and e.status_code == 429:
                    if attempt < max_retries - 1:
                        Console().print(f"[yellow]Rate limit error (429). Waiting {retry_delay} seconds before retry... (Attempt {attempt + 1}/{max_retries})[/yellow]")
                        await asyncio.sleep(retry_delay)
                    else:
                        Console().print(f"[red]Failed to generate image after {max_retries} attempts due to rate limit.[/red]")
                        raise
                else:
                    # 429가 아닌 다른 에러는 즉시 발생
                    raise
        
        # 모든 재시도 실패 시 (도달하지 않아야 함)
        raise RuntimeError("Failed to generate image after all retries")
    
    @message_handler
    async def handle_request_to_speak(self, message: RequestToSpeak, ctx: MessageContext) -> None:  # type: ignore
        """발언 요청을 받고 이미지 생성 후 그룹에 발행"""
        agent_name_kr = role_names_kr.get(self.id.type, self.id.type)
        Console().print(Panel(f"[bold cyan]{agent_name_kr}[/bold cyan]", border_style="cyan"))
        
        self._chat_history.append(
            UserMessage(
                content=f"Transferred to {self.id.type}, adopt the persona immediately.",
                source="system"
            )
        )
        
        # 디버깅: 전송할 메시지 출력
        print("\n" + "="*80)
        print(f"[DEBUG] Sending to LLM for {self.id.type} (with image tool)")
        print("="*80)
        print(f"System Message: {self._system_message.content[:200]}...")
        print("\nChat History:")
        for idx, msg in enumerate(self._chat_history[-5:]):  # 최근 5개만
            content_preview = str(msg.content)[:100] if hasattr(msg, 'content') else str(msg)[:100]
            print(f"  {idx}: {type(msg).__name__} - {content_preview}...")
        print(f"\nTool: {self._image_gen_tool.name}")
        print("="*80 + "\n")
        
        # 이미지 생성 도구를 반드시 사용하도록 설정 (content filter 오류 시 재시도)
        max_retries = 3
        completion = None
        
        for attempt in range(max_retries):
            try:
                completion = await self._model_client.create(
                    [self._system_message] + self._chat_history,
                    tools=[self._image_gen_tool],
                    extra_create_args={"tool_choice": "required"},
                    cancellation_token=ctx.cancellation_token,
                )
                break  # 성공하면 루프 탈출
                
            except openai.BadRequestError as e:
                # content_filter 오류 감지
                if hasattr(e, 'response') and 'content_filter' in str(e):
                    if attempt < max_retries - 1:
                        Console().print(f"[yellow]⚠️  Content filter 감지. 재시도 중... (시도 {attempt + 1}/{max_retries})[/yellow]")
                        # 히스토리 축약: 가장 오래된 대화 제거
                        if len(self._chat_history) > 3:
                            self._chat_history = self._chat_history[-3:]
                            Console().print("[yellow]   대화 히스토리를 축약했습니다.[/yellow]")
                        await asyncio.sleep(2)  # 2초 대기
                    else:
                        Console().print(f"[red]❌ {max_retries}회 재시도 후에도 content filter 오류가 계속 발생합니다.[/red]")
                        print("\n" + "!"*80)
                        print(f"[ERROR] Content Filter 오류 for {self.id.type}")
                        print("!"*80)
                        print(f"Error: {str(e)}")
                        print("!"*80 + "\n")
                        raise
                else:
                    raise
                    
            except Exception as e:
                print("\n" + "!"*80)
                print(f"[ERROR] LLM 호출 실패 for {self.id.type}")
                print("!"*80)
                print(f"Error Type: {type(e).__name__}")
                print(f"Error Message: {str(e)}")
                if hasattr(e, 'response'):
                    print(f"Response: {e.response}")
                print("\n전체 프롬프트:")
                print(f"System: {self._system_message.content}")
                print("\nHistory:")
                for idx, msg in enumerate(self._chat_history):
                    print(f"{idx}: {type(msg).__name__}")
                    print(f"   Source: {getattr(msg, 'source', 'N/A')}")
                    print(f"   Content: {str(msg.content)[:500]}")
                print("!"*80 + "\n")
                raise
        
        if completion is None:
            raise RuntimeError("Failed to get completion after all retries")
        
        assert isinstance(completion.content, list) and all(
            isinstance(item, FunctionCall) for item in completion.content
        )
        
        self._image_counter = 0
        
        images: List[str | Image] = []
        for tool_call in completion.content:
            arguments = json.loads(tool_call.arguments)
            Console().print(arguments)
            
            # 도구 실행하여 이미지 생성
            result = await self._image_gen_tool.run_json(arguments, ctx.cancellation_token)
            image = Image.from_base64(self._image_gen_tool.return_value_as_string(result))
            
            # 이미지 리사이즈 (표시용)
            # image = Image.from_pil(image.image.resize((256, 256)))
            
            # 이미지를 순서대로 파일로 저장
            self._image_counter += 1
            filename = f"generated_image_{self._image_counter:03d}.png"
            image.image.save(filename)
            Console().print(f"[green]Image saved to {filename}[/green]")
            
            images.append(image)
        
        # 대화 로그에 이미지 파일명 추가
        image_files = [f"generated_image_{i:03d}.png" for i in range(1, self._image_counter + 1)]
        agent_name_kr = role_names_kr.get(self.id.type, self.id.type)
        conversation_log.append({
            'role': agent_name_kr,
            'content': f"Generated {len(image_files)} illustration(s)",
            'images': image_files
        })
        
        await self.publish_message(
            GroupChatMessage(
                body=UserMessage(content=images, source=self.id.type)
            ),
            DefaultTopicId(type=self._group_chat_topic_type),
        )
class UserAgent(RoutedAgent):
    """사용자를 대표하는 에이전트"""
    
    def __init__(self, description: str, group_chat_topic_type: str) -> None:
        super().__init__(description=description)
        self._group_chat_topic_type = group_chat_topic_type
    
    @message_handler
    async def handle_message(self, message: GroupChatMessage, ctx: MessageContext) -> None:
        """그룹 채팅 메시지 수신 (프론트엔드로 전달할 위치)"""
        pass
    
    @message_handler
    async def handle_request_to_speak(self, message: RequestToSpeak, ctx: MessageContext) -> None:
        """사용자 입력을 받아 그룹에 전달"""
        user_input = input("Enter your message (type 'APPROVE' to conclude): ")
        agent_name_kr = role_names_kr.get(self.id.type, self.id.type)
        Console().print(Panel(f"[bold cyan]{agent_name_kr}[/bold cyan]\n\n{user_input}", border_style="cyan"))
        
        # 대화 로그에 추가 (한국어 이름으로)
        conversation_log.append({
            'role': agent_name_kr,
            'content': user_input
        })
        
        await self.publish_message(
            GroupChatMessage(
                body=UserMessage(content=user_input, source=self.id.type)
            ),
            DefaultTopicId(type=self._group_chat_topic_type),
        )

class GroupChatManager(RoutedAgent):
    """그룹 채팅을 관리하고 다음 발언자를 선택하는 매니저"""
    
    def __init__(
        self,
        participant_topic_types: List[str],
        model_client: ChatCompletionClient,
        participant_descriptions: List[str],
    ) -> None:
        super().__init__("Group chat manager")
        self._participant_topic_types = participant_topic_types
        self._model_client = model_client
        self._chat_history: List[UserMessage] = []
        self._participant_descriptions = participant_descriptions
        self._previous_participant_topic_type: str | None = None
        
    @message_handler
    async def handle_message(self, message: GroupChatMessage, ctx: MessageContext) -> None:
        """그룹 채팅 메시지를 수신하고 다음 발언자 선택"""
        assert isinstance(message.body, UserMessage)
        self._chat_history.append(message.body)
        
        # 사용자가 승인하면 종료
        if message.body.source == "User":
            assert isinstance(message.body.content, str)
            if "approve" in message.body.content.lower().strip(string.punctuation):
                return
        
        # 메시지 히스토리 포맷팅
        messages: List[str] = []
        for msg in self._chat_history:
            if isinstance(msg.content, str):
                messages.append(f"{msg.source}: {msg.content}")
        
        history = "\n".join(messages)
        
        # 역할 목록 포맷팅 (이전 발언자 제외)
        roles = "\n".join([
            f"{topic_type}: {description}".strip()
            for topic_type, description in zip(
                self._participant_topic_types, 
                self._participant_descriptions,
                strict=True
            )
            if topic_type != self._previous_participant_topic_type
        ])
        
        # 다음 발언자 선택 프롬프트
        selector_prompt = """You are in a role play game. The following roles are available:
{roles}

Read the following conversation. Then select the next role from {participants} to play.
Only return the role name.

{history}

Read the above conversation. Then select the next role from {participants} to play.
Only return the role name."""
        
        system_message = SystemMessage(
            content=selector_prompt.format(
                roles=roles,
                history=history,
                participants=str([
                    topic_type
                    for topic_type in self._participant_topic_types
                    if topic_type != self._previous_participant_topic_type
                ]),
            )
        )
        
        # 디버깅: 전송할 메시지 출력
        print("\n" + "="*80)
        print("[DEBUG] GroupChatManager selecting next speaker")
        print("="*80)
        print(f"System Message Preview: {system_message.content[:300]}...")
        print("="*80 + "\n")
        
        # LLM으로 다음 발언자 선택 (content filter 오류 시 재시도)
        max_retries = 3
        completion = None
        
        for attempt in range(max_retries):
            try:
                completion = await self._model_client.create(
                    [system_message], 
                    cancellation_token=ctx.cancellation_token
                )
                break  # 성공하면 루프 탈출
                
            except openai.BadRequestError as e:
                # content_filter 오류 감지
                if hasattr(e, 'response') and 'content_filter' in str(e):
                    if attempt < max_retries - 1:
                        Console().print(f"[yellow]⚠️  Content filter 감지. 재시도 중... (시도 {attempt + 1}/{max_retries})[/yellow]")
                        # 히스토리 축약: 가장 오래된 메시지 제거
                        if len(self._chat_history) > 5:
                            self._chat_history = self._chat_history[-5:]
                            Console().print("[yellow]   대화 히스토리를 축약했습니다.[/yellow]")
                            # 시스템 메시지 재생성
                            messages = []
                            for msg in self._chat_history:
                                if isinstance(msg.content, str):
                                    messages.append(f"{msg.source}: {msg.content}")
                            history = "\n".join(messages)
                            system_message = SystemMessage(
                                content=selector_prompt.format(
                                    roles=roles,
                                    history=history,
                                    participants=str([
                                        topic_type
                                        for topic_type in self._participant_topic_types
                                        if topic_type != self._previous_participant_topic_type
                                    ]),
                                )
                            )
                        await asyncio.sleep(2)  # 2초 대기
                    else:
                        Console().print(f"[red]❌ {max_retries}회 재시도 후에도 content filter 오류가 계속 발생합니다.[/red]")
                        print("\n" + "!"*80)
                        print("[ERROR] Content Filter 오류 - GroupChatManager")
                        print("!"*80)
                        print(f"Error: {str(e)}")
                        print("!"*80 + "\n")
                        raise
                else:
                    raise
                    
            except Exception as e:
                print("\n" + "!"*80)
                print("[ERROR] GroupChatManager LLM 호출 실패")
                print("!"*80)
                print(f"Error Type: {type(e).__name__}")
                print(f"Error Message: {str(e)}")
                print("\n전체 프롬프트:")
                print(system_message.content)
                print("!"*80 + "\n")
                raise
        
        if completion is None:
            raise RuntimeError("Failed to get completion after all retries")
        
        
        assert isinstance(completion.content, str)
        
        # 선택된 에이전트에게 발언 요청
        for topic_type in self._participant_topic_types:
            if topic_type.lower() in completion.content.lower():
                self._previous_participant_topic_type = topic_type
                await self.publish_message(
                    RequestToSpeak(), 
                    DefaultTopicId(type=topic_type)
                )
                return
        
        raise ValueError(f"Invalid role selected: {completion.content}")


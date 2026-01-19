import asyncio
import uuid
import openai
import os
from dotenv import load_dotenv
from autogen_core import SingleThreadedAgentRuntime, TypeSubscription, DefaultTopicId, TopicId
from autogen_ext.models.openai import OpenAIChatCompletionClient, AzureOpenAIChatCompletionClient
from group_chat_basics import (
    GroupChatMessage,
    WriterAgent,
    EditorAgent,
    IllustratorAgent,
    UserAgent,
    GroupChatManager,
)
from autogen_core.models import UserMessage
from pathlib import Path
import glob
import base64

# .env 파일에서 환경 변수 로드
load_dotenv()

# 대화 히스토리를 저장할 전역 변수
conversation_history = []

async def translate_to_korean(text: str, model_client) -> str:
    """영어 텍스트를 한국어로 번역"""
    try:
        from autogen_core.models import SystemMessage as TranslateSystemMessage, UserMessage as TranslateUserMessage
        messages = [
            TranslateSystemMessage(content="You are a professional translator. Translate the following English text to Korean. Maintain the tone and style of children's storybook. Only return the Korean translation without any additional comments."),
            TranslateUserMessage(content=text, source="user")
        ]
        response = await model_client.create(messages)
        return response.content if isinstance(response.content, str) else text
    except:
        return text

def generate_storybook_html(history, output_file="storybook.html", title=None):
    """대화 내용과 이미지를 동화책 형식의 HTML로 생성"""
    
    # 타이틀이 제공되지 않으면 작가의 콘텐츠에서 추출 시도
    if not title:
        import re
        for item in history:
            if item['role'] == '작가' and item['content']:
                # "Title:" 또는 "**Title:**" 패턴 찾기
                title_match = re.search(r'\*\*Title:\s*(.+?)\*\*|Title:\s*(.+?)(?:\n|$)', item['content'], re.IGNORECASE)
                if title_match:
                    title = title_match.group(1) or title_match.group(2)
                    title = title.strip()
                    break
                # 패턴이 없으면 첫 번째 줄을 타이틀로 사용
                first_line = item['content'].split('\n')[0].strip()
                if len(first_line) > 50:
                    first_line = first_line[:50] + '...'
                title = first_line
                break
        if not title:
            title = "AI가 만든 동화책"
    
    # 작가의 스토리 텍스트 추출
    story_parts = []
    for item in history:
        if item['role'] == '작가':
            story_parts.append(item['content'])
    
    story_text = '\n\n'.join(story_parts)
    
    # HTML 템플릿
    html_content = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>동화책 - 용감한 작은 로봇</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Nanum Gothic', 'Malgun Gothic', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            min-height: 100vh;
        }}
        
        .storybook {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 3em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }}
        
        .header p {{
            font-size: 1.2em;
            opacity: 0.9;
        }}
        
        .content {{
            padding: 40px;
        }}
        
        .story-section {{
            margin-bottom: 60px;
            background: white;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }}
        
        .story-text {{
            font-size: 1.3em;
            line-height: 1.8;
            color: #333;
            margin-bottom: 40px;
            text-align: justify;
            white-space: pre-line;
            background: #f8f9fa;
            padding: 30px;
            border-radius: 10px;
        }}
        
        .story-text p {{
            margin-bottom: 20px;
        }}
        
        .story-images {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin: 40px 0;
        }}
        
        .story-image {{
            text-align: center;
        }}
        
        .story-image img {{
            width: 100%;
            max-width: 500px;
            height: auto;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }}
        
        .conversation {{
            margin-top: 60px;
            padding-top: 40px;
            border-top: 3px solid #e0e0e0;
        }}
        
        .conversation h2 {{
            color: #667eea;
            margin-bottom: 30px;
            font-size: 2em;
        }}
        
        .message {{
            margin-bottom: 25px;
            padding: 20px;
            border-radius: 10px;
            background: #f8f9fa;
        }}
        
        .message.작가 {{
            background: #e3f2fd;
            border-left: 5px solid #2196f3;
        }}
        
        .message.편집자 {{
            background: #f3e5f5;
            border-left: 5px solid #9c27b0;
        }}
        
        .message.일러스트레이터 {{
            background: #fff3e0;
            border-left: 5px solid #ff9800;
        }}
        
        .message.사용자 {{
            background: #e8f5e9;
            border-left: 5px solid #4caf50;
        }}
        
        .message-header {{
            font-weight: bold;
            color: #333;
            margin-bottom: 10px;
            font-size: 1.1em;
        }}
        
        .message-content {{
            color: #555;
            line-height: 1.6;
            white-space: pre-line;
        }}
        
        .message-images {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }}
        
        .message-image {{
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }}
        
        .message-image img {{
            width: 100%;
            height: auto;
            display: block;
        }}
        
        .message-image-caption {{
            padding: 10px;
            text-align: center;
            background: white;
            font-size: 0.9em;
            color: #666;
        }}
        
        .footer {{
            text-align: center;
            padding: 30px;
            background: #f8f9fa;
            color: #666;
            font-size: 0.9em;
        }}
        
        @media print {{
            body {{
                background: white;
            }}
            
            .conversation {{
                display: none;
            }}
        }}
    </style>
</head>
<body>
    <div class="storybook">
        <div class="header">
            <h1>📚 {title}</h1>
            <p>AI가 만든 동화책</p>
        </div>
        
        <div class="content">
            <div class="story-section">
"""
    
    # 작가의 스토리를 문단별로 분할
    writer_paragraphs = []
    for item in history:
        if item['role'] == '작가':
            # 빈 줄로 문단 구분
            paragraphs = [p.strip() for p in item['content'].split('\n\n') if p.strip()]
            writer_paragraphs.extend(paragraphs)
    
    # 일러스트레이터의 모든 이미지 수집
    all_images = []
    for item in history:
        if item['role'] == '일러스트레이터' and 'images' in item and item['images']:
            all_images.extend(item['images'])
    
    # 문단과 이미지를 교차 배치
    total_paragraphs = len(writer_paragraphs)
    images_per_section = max(1, len(all_images) // max(1, total_paragraphs))
    
    image_index = 0
    for para_idx, paragraph in enumerate(writer_paragraphs):
        # 문단 추가
        html_content += f"""
                <div class="story-text">
{paragraph}
                </div>
"""
        
        # 문단 뒤에 이미지 추가 (마지막 문단이 아니면서 이미지가 남아있으면)
        if image_index < len(all_images):
            # 이 문단에 할당할 이미지 수 계산
            remaining_paragraphs = total_paragraphs - para_idx - 1
            remaining_images = len(all_images) - image_index
            
            if remaining_paragraphs == 0:
                # 마지막 문단: 남은 모든 이미지
                images_to_show = remaining_images
            else:
                # 남은 이미지를 남은 문단에 균등 분배
                images_to_show = min(images_per_section, remaining_images)
            
            if images_to_show > 0:
                html_content += """
                <div class="story-images">
"""
                for _ in range(images_to_show):
                    img_path = all_images[image_index]
                    abs_img_path = os.path.abspath(img_path)
                    html_content += f"""
                    <div class="story-image">
                        <img src="file://{abs_img_path}" alt="일러스트 {image_index + 1}">
                    </div>
"""
                    image_index += 1
                
                html_content += """
                </div>
"""
    
    html_content += """
            </div>
            
            <div class="conversation">
                <h2>💬 제작 과정</h2>
"""
    
    # 대화 내용 추가 (이미지 포함)
    for item in history:
        if item['content'].strip():
            html_content += f"""
                <div class="message {item['role']}">
                    <div class="message-header">{item['role']}</div>
                    <div class="message-content">{item['content']}</div>
"""
            # 이미지가 있으면 메시지 안에 삽입
            if 'images' in item and item['images']:
                html_content += """
                    <div class="message-images">
"""
                for idx, img_path in enumerate(item['images'], 1):
                    abs_img_path = os.path.abspath(img_path)
                    html_content += f"""
                        <div class="message-image">
                            <img src="file://{abs_img_path}" alt="일러스트 {idx}">
                            <div class="message-image-caption">일러스트 {idx}</div>
                        </div>
"""
                html_content += """
                    </div>
"""
            html_content += """
                </div>
"""
    
    html_content += """
            </div>
        </div>
        
        <div class="footer">
            <p>✨ AutoGen Group Chat으로 생성된 동화책 ✨</p>
        </div>
    </div>
</body>
</html>
"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    return output_file

async def main():
    # 런타임 생성
    runtime = SingleThreadedAgentRuntime()
    
    # 토픽 타입 정의 (영어로 유지 - OpenAI API 요구사항)
    editor_topic_type = "Editor"
    writer_topic_type = "Writer"
    illustrator_topic_type = "Illustrator"
    user_topic_type = "User"
    group_chat_topic_type = "group_chat"
    
    # 한국어 이름 매핑
    role_names_kr = {
        "Editor": "편집자",
        "Writer": "작가",
        "Illustrator": "일러스트레이터",
        "User": "사용자"
    }
    
    # 에이전트 설명
    editor_description = "Editor for planning and reviewing the content."
    writer_description = "Writer for creating any text content."
    user_description = "User for providing final approval."
    illustrator_description = "An illustrator for creating image descriptions."
    
    # OpenAI 모델 클라이언트 생성
    model_client = AzureOpenAIChatCompletionClient(
        model=os.environ.get("AZURE_OPENAI_DEPLOYMENT"),
        azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
        azure_deployment=os.environ.get("AZURE_OPENAI_DEPLOYMENT"),
        api_key=os.environ.get("AZURE_OPENAI_API_KEY"),
        api_version=os.environ.get("AZURE_OPENAI_API_VERSION"),
    )
    
    # OpenAI 이미지 클라이언트 생성 (DALL-E용)
    image_client = openai.AsyncAzureOpenAI(
        azure_deployment=os.environ.get("AZURE_OPENAI_IMAGE_DEPLOYMENT"),
        azure_endpoint=os.environ.get("AZURE_OPENAI_IMAGE_ENDPOINT"),
        api_key=os.environ.get("AZURE_OPENAI_API_GPT_IMAGE_KEY"),
        api_version=os.environ.get("AZURE_OPENAI_IMAGE_API_VERSION")
    )
    
    # Editor 에이전트 등록
    editor_agent_type = await EditorAgent.register(
        runtime,
        editor_topic_type,
        lambda: EditorAgent(
            description=editor_description,
            group_chat_topic_type=group_chat_topic_type,
            model_client=model_client,
        ),
    )
    await runtime.add_subscription(
        TypeSubscription(topic_type=editor_topic_type, agent_type=editor_agent_type.type)
    )
    await runtime.add_subscription(
        TypeSubscription(topic_type=group_chat_topic_type, agent_type=editor_agent_type.type)
    )
    
    # Writer 에이전트 등록
    writer_agent_type = await WriterAgent.register(
        runtime,
        writer_topic_type,
        lambda: WriterAgent(
            description=writer_description,
            group_chat_topic_type=group_chat_topic_type,
            model_client=model_client,
        ),
    )
    await runtime.add_subscription(
        TypeSubscription(topic_type=writer_topic_type, agent_type=writer_agent_type.type)
    )
    await runtime.add_subscription(
        TypeSubscription(topic_type=group_chat_topic_type, agent_type=writer_agent_type.type)
    )
    
    # Illustrator 에이전트 등록
    illustrator_agent_type = await IllustratorAgent.register(
        runtime,
        illustrator_topic_type,
        lambda: IllustratorAgent(
            description=illustrator_description,
            group_chat_topic_type=group_chat_topic_type,
            model_client=model_client,
            image_client=image_client,
        ),
    )
    await runtime.add_subscription(
        TypeSubscription(topic_type=illustrator_topic_type, agent_type=illustrator_agent_type.type)
    )
    await runtime.add_subscription(
        TypeSubscription(topic_type=group_chat_topic_type, agent_type=illustrator_agent_type.type)
    )
    
    # User 에이전트 등록
    user_agent_type = await UserAgent.register(
        runtime,
        user_topic_type,
        lambda: UserAgent(
            description=user_description, 
            group_chat_topic_type=group_chat_topic_type
        ),
    )
    await runtime.add_subscription(
        TypeSubscription(topic_type=user_topic_type, agent_type=user_agent_type.type)
    )
    await runtime.add_subscription(
        TypeSubscription(topic_type=group_chat_topic_type, agent_type=user_agent_type.type)
    )
    
    # GroupChatManager 등록
    group_chat_manager_type = await GroupChatManager.register(
        runtime,
        "group_chat_manager",
        lambda: GroupChatManager(
            participant_topic_types=[
                writer_topic_type, 
                illustrator_topic_type, 
                editor_topic_type, 
                user_topic_type
            ],
            model_client=model_client,
            participant_descriptions=[
                writer_description, 
                illustrator_description, 
                editor_description, 
                user_description
            ],
        ),
    )
    await runtime.add_subscription(
        TypeSubscription(topic_type=group_chat_topic_type, agent_type=group_chat_manager_type.type)
    )
    
    # 런타임 시작
    runtime.start()
    
    # 그룹 채팅 시작
    session_id = str(uuid.uuid4())
    initial_topic = "A story about a brave little robot helping friends"
    await runtime.publish_message(
        GroupChatMessage(
            body=UserMessage(
                content=f"""Children's Storybook Production Project:
Topic: {initial_topic}
Target: Educational and positive story for 5-7 year old children
Requirements:
1. Write a short and fun story of 3-5 paragraphs
2. Create bright and cute illustrations to match the story
3. Convey the values of courage and friendship to children""",
                source="User",
            )
        ),
        TopicId(type=group_chat_topic_type, source=session_id),
    )
    
    # 완료될 때까지 대기
    await runtime.stop_when_idle()
    
    print("\n✅ 그룹 채팅이 완료되었습니다!")
    
    # HTML 동화책 생성 (번역 적용)
    from group_chat_basics import conversation_log
    if conversation_log:
        print("📝 한국어로 번역 중...")
        translated_log = []
        for item in conversation_log:
            translated_content = await translate_to_korean(item['content'], model_client)
            translated_item = {
                'role': item['role'],
                'content': translated_content
            }
            if 'images' in item:
                translated_item['images'] = item['images']
            translated_log.append(translated_item)
        
        # 토픽을 한국어로 번역하여 타이틀로 사용
        translated_title = await translate_to_korean(initial_topic, model_client)
        
        html_file = generate_storybook_html(translated_log, title=translated_title)
        print(f"📖 동화책이 생성되었습니다: {html_file}")
        print(f"   브라우저에서 파일을 열어보세요!")
        
        # 자동으로 브라우저에서 열기
        import webbrowser
        webbrowser.open(f"file://{os.path.abspath(html_file)}")
    
    # 클린업
    await model_client.close()

if __name__ == "__main__":
    asyncio.run(main())
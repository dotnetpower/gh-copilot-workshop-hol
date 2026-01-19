"""DALL-E 이미지 생성 테스트"""
import asyncio
import os
from dotenv import load_dotenv
import openai
from PIL import Image
import base64
from io import BytesIO
import pytest

# .env 파일 로드
load_dotenv()

async def test_image_generation():
    """DALL-E를 사용하여 실제 이미지 생성 테스트"""
    
    print("=== DALL-E 이미지 생성 테스트 시작 ===\n")
    
    try:
        # 1. 환경 변수 확인
        print("1. 환경 변수 확인 중...")
        api_key = os.environ.get("AZURE_OPENAI_API_GPT_IMAGE_KEY")
        azure_endpoint = os.environ.get("AZURE_OPENAI_IMAGE_ENDPOINT")
        azure_deployment = os.environ.get("AZURE_OPENAI_IMAGE_DEPLOYMENT")
        api_version = os.environ.get("AZURE_OPENAI_IMAGE_API_VERSION")
        
        if not api_key:
            raise ValueError("AZURE_OPENAI_API_GPT_IMAGE_KEY 환경 변수가 설정되지 않았습니다.")
        if not azure_endpoint:
            raise ValueError("AZURE_OPENAI_IMAGE_ENDPOINT 환경 변수가 설정되지 않았습니다.")
        if not azure_deployment:
            raise ValueError("AZURE_OPENAI_IMAGE_DEPLOYMENT 환경 변수가 설정되지 않았습니다.")
        if not api_version:
            raise ValueError("AZURE_OPENAI_IMAGE_API_VERSION 환경 변수가 설정되지 않았습니다.")
            
        print(f"   ✅ API 키 확인됨 (길이: {len(api_key)} 자)")
        print(f"   ✅ 엔드포인트: {azure_endpoint}")
        print(f"   ✅ 배포 이름: {azure_deployment}")
        print(f"   ✅ API 버전: {api_version}\n")
        
        # 2. OpenAI 클라이언트 생성
        print("2. OpenAI 클라이언트 생성 중...")
        client = openai.AsyncAzureOpenAI(
            azure_deployment=azure_deployment,
            azure_endpoint=azure_endpoint,
            api_key=api_key,
            api_version=api_version
        )
        print("   ✅ 클라이언트 생성 완료\n")
        
        # 3. 이미지 생성 요청
        print("3. DALL-E 이미지 생성 요청 중...")
        print("   프롬프트: 'A cute robot in a digital painting style'")
        
        response = await client.images.generate(
            prompt="A cute robot in a digital painting style",
            model=azure_deployment,
            n=1,
            size="1024x1024"
        )
        print("   ✅ 이미지 생성 완료\n")
        
        # 4. Base64 디코딩
        print("4. Base64 이미지 디코딩 중...")
        image_data = base64.b64decode(response.data[0].b64_json)
        image = Image.open(BytesIO(image_data))
        print(f"   ✅ 이미지 디코딩 완료 (크기: {image.size})\n")
        
        # 5. 파일로 저장
        print("5. temp.png로 저장 중...")
        image.save("temp.png")
        print("   ✅ temp.png 저장 완료\n")
        
        print("=== ✅ 이미지 생성 테스트 성공! ===")
        print(f"생성된 파일: temp.png")
        return True
        
    except openai.AuthenticationError as e:
        print(f"\n❌ 인증 오류: {e}")
        print("   Azure OpenAI API 키나 엔드포인트를 확인해주세요.")
        return False
    except openai.NotFoundError as e:
        print(f"\n❌ 리소스를 찾을 수 없음: {e}")
        print("   DALL-E 배포 이름이 'dall-e-3'가 맞는지 확인해주세요.")
        print("   또는 Azure Portal에서 DALL-E 배포가 있는지 확인해주세요.")
        return False
    except Exception as e:
        print(f"\n❌ 테스트 실패: {type(e).__name__}")
        print(f"   에러 메시지: {str(e)}")
        import traceback
        print("\n전체 스택 트레이스:")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(test_image_generation())
    exit(0 if success else 1)

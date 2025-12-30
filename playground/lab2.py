import re

# 원본 함수
def validate_email(email: str) -> bool:
    regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    return bool(re.match(regex, email))

# Copilot Chat에 "이 함수의 테스트 코드를 작성해주세요"라고 요청

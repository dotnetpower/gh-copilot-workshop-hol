---
sidebar_position: 11
title: 실습 2 - Copilot Chat으로 코드 품질 개선
description: GitHub Copilot Chat을 활용한 코드 리뷰, 테스트 생성, 문서화 자동화 실습
---

# 실습 2: Copilot Chat을 이용하여 코드 품질 개선

:::tip 📝 학습 목표
- GitHub Copilot의 Ask, Edit, Agent 모드 활용법 학습
- 코드 리뷰 및 개선 방법 습득
- 테스트 코드 생성 및 문서화 자동화
:::

## 🛠️ 실습 내용

### 2.1 Copilot Chat 시작하기
```
// 채팅창에서 다음과 같이 질문할 수 있습니다:
"이 함수의 성능을 개선할 수 있는 방법이 있나요?"
"이 코드에 대한 단위 테스트를 작성해주세요"
"이 함수의 복잡도를 줄일 수 있나요?"
```

### 2.2 코드 품질 개선
- **코드 리팩토링**: 기존 코드의 구조 개선
- **성능 최적화**: 알고리즘 효율성 향상
- **가독성 향상**: 더 명확하고 이해하기 쉬운 코드로 변경

### 2.3 테스트 코드 생성
```python
import re

# 원본 함수
def validate_email(email: str) -> bool:
    regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    return bool(re.match(regex, email))

# Copilot Chat에 "이 함수의 테스트 코드를 작성해주세요"라고 요청
```

### 2.4 문서화 자동생성
- JSDoc, Python docstring 등 자동 생성
- README 파일 작성 도움
- API 문서 생성 지원

:::note ✅ 실습 과제
1. 기존 코드의 성능 개선안 요청하기
2. 단위 테스트 코드 자동 생성하기
3. 함수 문서화(JSDoc/docstring) 자동 생성하기
4. 코드 리뷰 의견 받기
:::

### 2.5 에이전트와 친해지기
에이전트와 상호작용을 통해 친해지면, 내 언어를 좀더 쉽게 이해합니다.
![Image text](/img/labs/agent_conv.png)

- 실제 에이전트는 현재 대화 세션 동안만 기억합니다. ;)
- 나의 표현 중에서 잘 작동하는 표현을 익히기 위해서 반복적으로 에이전트와 대화해서 친해지세요!

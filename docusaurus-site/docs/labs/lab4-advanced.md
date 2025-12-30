---
sidebar_position: 13
title: 실습 4 - Copilot 고급 기능
description: 고급 프롬프트 엔지니어링, 커스텀 Instructions, 보안 및 팀 협업 최적화 실습
---

# 실습 4: Copilot 고급 기능

:::tip 📝 학습 목표
- GitHub Copilot의 고급 기능 및 최적화 방법 학습
- 팀 협업을 위한 Copilot 활용 전략 수립
- 프로덕션 환경에서의 보안 및 품질 관리
:::

## 🛠️ 실습 내용

### 4.1 고급 프롬프트 엔지니어링
효과적인 프롬프트 작성을 통해 더 정확하고 유용한 결과를 얻습니다.

```python
"""
고급 프롬프트 예시:

컨텍스트: FastAPI 애플리케이션
요구사항: RESTful API 엔드포인트 작성
제약조건: Python 3.12+, JWT 인증, 에러 핸들링 포함, Type hints 사용
스타일: Clean Architecture 패턴 적용
"""

# 이러한 상세한 컨텍스트를 제공하면 더 정확한 코드를 생성합니다
```

### 4.2 커스텀 Instructions 설정
커스텀 지시파일 사용 [github.copilot.chat.codeGeneration.useInstructionFiles](vscode://settings/github.copilot.chat.codeGeneration.useInstructionFiles) 설정 후 `.github/copilot-instructions.md` 파일에 정의

```markdown
---
applyTo: "**"
---
# Project general coding standards

## Naming Conventions
- Use PascalCase for component names, interfaces, and type aliases
- Use camelCase for variables, functions, and methods
- Prefix private class members with underscore (_)
- Use ALL_CAPS for constants

## Error Handling
- Use try/catch blocks for async operations
- Implement proper error boundaries in React components
- Always log errors with contextual information

```

### 4.3 Copilot for Business/Enterprise 기능
- **코드 보안 스캔**: 취약점 자동 탐지 및 수정 제안
- **라이선스 준수**: 오픈소스 라이선스 충돌 방지
- **감사 로그**: 코드 생성 이력 추적
- **정책 관리**: 조직별 사용 정책 설정

### 4.4 성능 모니터링 및 최적화
```python
from dataclasses import dataclass

# Copilot 사용 통계 분석
@dataclass
class CopilotMetrics:
    acceptance_rate: float = 85.0    # 제안 수락률
    times_saved: int = 120           # 절약된 시간 (분)
    lines_generated: int = 2450      # 생성된 코드 라인 수
    errors_reduced: int = 23         # 줄어든 버그 수

metrics = CopilotMetrics()
```

### 4.5 팀 협업 최적화
- **공통 패턴 공유**: 팀의 코딩 패턴을 Copilot에 학습
- **코드 리뷰 통합**: Pull Request에서 Copilot 활용
- **지식 베이스 구축**: 프로젝트별 베스트 프랙티스 문서화

### 4.6 Git 커밋 메시지 자동 생성

GitHub Copilot은 변경된 코드를 분석하여 의미 있는 커밋 메시지를 자동으로 생성할 수 있습니다.

#### 4.6.1 기본 사용법
1. 소스 제어(Source Control) 패널 열기 (`Ctrl + Shift + G`)
2. 변경사항이 있는 상태에서 커밋 메시지 입력창의 **✨ 아이콘(Sparkle)** 클릭
3. Copilot이 자동으로 커밋 메시지 생성


#### 4.6.2 커밋 메시지 생성 설정
`.vscode/settings.json` 파일에서 커밋 메시지 생성을 커스터마이징할 수 있습니다:

```json
{
    // 한국어로 커밋 메시지 생성
    "github.copilot.chat.localeOverride": "ko",
    
    // 커밋 메시지 자동 생성 활성화
    "github.copilot.chat.generateCommitMessage.enabled": true,
    
    // 커밋 메시지 생성 규칙 커스터마이징
    "github.copilot.chat.commitMessageGeneration.instructions": [
        {
            "text": "한국어로 간략하게 생성해, feat: 같은 프리픽스는 넣지마"
        }
    ]
}
```

#### 4.6.3 커밋 메시지 커스터마이징 옵션

**기본 형식 (Conventional Commits 스타일):**
```json
{
    "github.copilot.chat.commitMessageGeneration.instructions": [
        {
            "text": "Use Conventional Commits format: <type>(<scope>): <description>"
        }
    ]
}
```

**팀 협업 스타일:**
```json
{
    "github.copilot.chat.commitMessageGeneration.instructions": [
        {
            "text": "커밋 메시지는 다음 규칙을 따라 작성: 1) 첫 줄은 50자 이내로 요약, 2) 변경 이유를 명확히 기술, 3) 이슈 번호가 있다면 #123 형식으로 포함"
        }
    ]
}
```

**한국어 상세 설명 스타일:**
```json
{
    "github.copilot.chat.commitMessageGeneration.instructions": [
        {
            "text": "한국어로 작성하며, 제목은 명령형으로 시작하고, 본문에는 '무엇을', '왜' 변경했는지 자세히 설명"
        }
    ]
}
```

#### 4.6.4 실습 예시

**변경 전 코드:**
```python
def calculate_total(items):
    return sum(item.price for item in items)
```

**변경 후 코드:**
```python
from typing import List
from dataclasses import dataclass

@dataclass
class Item:
    price: float
    quantity: int

def calculate_total(items: List[Item]) -> float:
    if not items:
        return 0.0
    return sum(item.price * item.quantity for item in items)
```

**자동 생성된 커밋 메시지 예시:**
```
계산 함수에 빈 배열 체크 및 수량 계산 로직 추가

- items가 비어있거나 null인 경우 0 반환하도록 가드 조건 추가
- 가격 계산 시 수량을 곱하도록 수정하여 정확한 총액 계산
```

:::tip 💡 커밋 메시지 생성 팁
- **변경사항을 논리적으로 그룹화**: 관련된 변경사항을 함께 스테이징하면 더 일관된 메시지를 생성합니다
- **커스텀 규칙 활용**: 팀의 커밋 메시지 컨벤션에 맞게 instructions를 설정하세요
- **리뷰 후 수정**: 자동 생성된 메시지를 검토하고 필요시 수정하세요
- **컨텍스트 제공**: 복잡한 변경의 경우, 관련 파일들을 함께 변경하면 더 정확한 메시지를 생성합니다
:::

### 4.7 CI/CD 파이프라인 통합
```yaml
# .github/workflows/copilot-security.yml
name: Copilot Security Scan
on: [push, pull_request]
jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: GitHub Copilot Security Scan
        uses: github/copilot-security-action@v1
```

:::note ✅ 실습 과제
1. 프로젝트별 커스텀 Instructions 설정하기
2. Copilot을 활용한 보안 코드 리뷰 수행하기
3. 팀 코딩 스타일 가이드 자동화하기
4. **Git 커밋 메시지 자동 생성 설정 및 활용하기**
   - `.vscode/settings.json`에 커밋 메시지 생성 규칙 추가
   - 여러 파일을 수정한 후 자동 생성된 커밋 메시지 확인
   - 팀 컨벤션에 맞게 instructions 커스터마이징
5. CI/CD 파이프라인에 Copilot 보안 스캔 통합하기
6. Copilot 사용 성과 측정 및 분석하기
:::

:::tip 🎯 고급 활용 팁
- **컨텍스트 최적화**: 관련 파일들을 함께 열어 더 나은 제안 받기
- **단계별 접근**: 복잡한 문제를 작은 단위로 나누어 해결하기
- **피드백 루프**: 생성된 코드를 검토하고 개선 사항 반영하기
- **보안 의식**: 생성된 코드의 보안 취약점 항상 검증하기
:::

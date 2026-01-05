---
sidebar_position: 11
title: 커스텀 설정
description: GitHub Copilot Instructions를 통한 프로젝트별 커스텀 설정 및 최적화 방법
---

# 사용자 정의 GitHub Copilot 구성

## 개요

프로젝트와 팀의 특성에 맞게 GitHub Copilot을 커스터마이징하여 생산성을 극대화하는 방법을 학습합니다.

참고: https://github.com/github/awesome-copilot/

## .github/copilot-instructions.md 설정

### 기본 구조

프로젝트 루트에 `.github/copilot-instructions.md` 파일을 생성하면 Copilot이 프로젝트 컨텍스트를 이해하고 더 적절한 제안을 제공합니다.

```markdown
---
description: 'MyProject 개발 지침'
applyTo: '**'
---

# MyProject Copilot 지침

## 프로젝트 개요
이 프로젝트는 Python + FastAPI 기반의 전자상거래 플랫폼입니다.

## 기술 스택
- Backend: Python 3.12, FastAPI, SQLAlchemy
- Database: PostgreSQL
- Testing: pytest, pytest-asyncio
- Frontend: React 18, Vite

## 코딩 규칙
1. 모든 API 엔드포인트는 async/await 사용
2. Pydantic 모델로 데이터 검증
3. 상태 관리는 Zustand 사용 (Frontend)
4. API 호출은 React Query 활용 (Frontend)

## 명명 규칙
- 모듈/클래스: PascalCase (예: ProductService.py)
- 함수: snake_case (예: format_price.py)
- 상수: UPPER_SNAKE_CASE (예: API_BASE_URL)
- CSS 클래스: kebab-case (예: product-card)

## 보안 요구사항
- 모든 API 엔드포인트는 JWT 인증 필수
- 사용자 입력은 반드시 검증
- XSS 방지를 위한 출력 이스케이프
- SQL 인젝션 방지를 위한 파라미터화된 쿼리

## 테스트 요구사항
- 모든 비즈니스 로직 함수는 단위 테스트 필수
- 컴포넌트는 렌더링 및 상호작용 테스트 작성
- 최소 80% 코드 커버리지 유지
```

### 언어별 지침

**Python 프로젝트 예시**
```markdown
---
description: 'Python API 개발 지침'
applyTo: '**/*.py'
---

# Python API 개발 지침

## 스타일 가이드
- PEP 8 준수
- Type hints 필수 사용
- Docstring은 Google 스타일

## 예시
```python
from typing import List, Optional

def calculate_total(
    items: List[dict], 
    tax_rate: float = 0.1
) -> float:
    """
    항목 리스트의 총액을 계산합니다.
    
    Args:
        items: 가격 정보가 포함된 항목 리스트
        tax_rate: 세율 (기본값 0.1)
    
    Returns:
        세금 포함 총액
        
    Raises:
        ValueError: items가 비어있는 경우
    """
    if not items:
        raise ValueError("항목 리스트가 비어있습니다")
    
    subtotal = sum(item["price"] for item in items)
    return subtotal * (1 + tax_rate)
```

## 프레임워크
- FastAPI 사용
- Pydantic으로 데이터 검증
- SQLAlchemy ORM
```

**.NET 프로젝트 예시**
```markdown
---
description: '.NET API 개발 지침'
applyTo: '**/*.cs'
---

# .NET API 개발 지침

## 스타일 가이드
- C# 12 이상 기능 활용
- Nullable reference types 활성화
- Async/await 패턴 사용

## 명명 규칙
- 인터페이스: IPascalCase
- 클래스: PascalCase
- 메서드: PascalCase
- private 필드: _camelCase

## 아키텍처
- Clean Architecture 패턴
- CQRS with MediatR
- Repository 패턴
- Dependency Injection

## 보안
- Input validation with FluentValidation
- JWT authentication
- Role-based authorization
```

## VS Code 설정

### settings.json 구성

```json
{
  "github.copilot.enable": {
    "*": true,
    "yaml": false,
    "plaintext": false
  },
  
  "github.copilot.advanced": {
    "authProvider": "github",
    "inlineSuggestCount": 3,
    "listCount": 10
  },
  
  "editor.inlineSuggest.enabled": true,
  "editor.quickSuggestions": {
    "comments": "on",
    "strings": "on",
    "other": "on"
  },
  
  // Copilot Chat 설정
  "github.copilot.chat.localeOverride": "ko",
  "github.copilot.chat.codeGeneration.instructions": [
    {
      "file": ".github/copilot-instructions.md"
    }
  ]
}
```

### 키보드 단축키 커스터마이징

```json
// keybindings.json
[
  {
    "key": "ctrl+shift+i",
    "command": "github.copilot.generate",
    "when": "editorTextFocus"
  },
  {
    "key": "ctrl+shift+/",
    "command": "workbench.action.chat.open",
    "when": "!inChat"
  },
  {
    "key": "alt+\\",
    "command": "editor.action.inlineSuggest.trigger",
    "when": "editorTextFocus && !editorHasSelection"
  }
]
```

## 프로젝트별 템플릿

### Python View 템플릿

`.github/templates/python-view.md`:
```markdown
# Python View 템플릿

모든 API View는 다음 구조를 따릅니다:

```python
from typing import Dict, Any
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class [ViewName]Request(BaseModel):
    """요청 데이터 모델"""
    # 필드 정의
    pass

class [ViewName]Response(BaseModel):
    """응답 데이터 모델"""
    # 필드 정의
    pass

@router.post("/[resource]")
async def [view_name](
    request_data: [ViewName]Request
) -> [ViewName]Response:
    """
    [엔드포인트 설명]
    
    Args:
        request_data: 요청 데이터
    
    Returns:
        응답 데이터
        
    Raises:
        HTTPException: 에러 발생 시
    """
    # 비즈니스 로직
    
    return [ViewName]Response()
```
```

### API Endpoint 템플릿

`.github/templates/api-endpoint.md`:
```markdown
# API Endpoint 템플릿

```python
from typing import Any, Dict
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field, validator

router = APIRouter()

class [Action]Request(BaseModel):
    """[요청 설명]"""
    field: str = Field(..., description="필드 설명")
    
    @validator('field')
    def validate_field(cls, v):
        if not v:
            raise ValueError('필드는 필수입니다')
        return v

class [Action]Response(BaseModel):
    """[응답 설명]"""
    success: bool
    data: Dict[str, Any]

@router.post(
    "/api/v1/[resource]",
    response_model=[Action]Response,
    status_code=status.HTTP_200_OK
)
async def [action]_endpoint(
    request: [Action]Request
) -> [Action]Response:
    """
    [엔드포인트 설명]
    
    - **access**: [Public/Private/Admin]
    """
    try:
        # 비즈니스 로직
        result = {}
        
        # 응답
        return [Action]Response(
            success=True,
            data=result
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
```
```

## 팀 스탠다드 적용

### .editorconfig

```ini
# .editorconfig
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true

[*.py]
indent_style = space
indent_size = 4
max_line_length = 88

[*.{yml,yaml,json}]
indent_style = space
indent_size = 2

[*.{md}]
trim_trailing_whitespace = false
```

### pyproject.toml (Black 및 Ruff 설정)

```toml
# pyproject.toml
[tool.black]
line-length = 88
target-version = ['py312']
include = '\.pyi?$'

[tool.ruff]
line-length = 88
target-version = "py312"
select = [
    "E",  # pycodestyle errors
    "W",  # pycodestyle warnings
    "F",  # pyflakes
    "I",  # isort
    "B",  # flake8-bugbear
    "C4",  # flake8-comprehensions
    "UP",  # pyupgrade
]
ignore = [
    "E501",  # line too long (handled by black)
]

[tool.ruff.per-file-ignores]
"__init__.py" = ["F401"]  # unused imports in __init__.py

[tool.pytest.ini_options]
pythonpath = ["src"]
testpaths = ["tests"]
```

## 고급 설정

### Workspace별 설정

```json
// .vscode/settings.json (프로젝트 전용)
{
  "github.copilot.chat.codeGeneration.instructions": [
    {
      "text": "이 프로젝트는 마이크로서비스 아키텍처를 사용합니다. 각 서비스는 독립적으로 배포 가능해야 합니다."
    },
    {
      "text": "모든 API는 FastAPI를 사용하고 OpenAPI 3.0 스펙을 자동으로 생성합니다."
    },
    {
      "text": "에러 처리는 HTTPException을 사용하고 적절한 status code를 반환합니다."
    },
    {
      "text": "모든 함수와 클래스에 Type hints를 필수로 사용하고 docstring을 작성합니다."
    }
  ],
  "python.formatting.provider": "black",
  "python.linting.enabled": true,
  "python.linting.ruffEnabled": true,
  "editor.formatOnSave": true
}
```

### 파일 타입별 설정

```json
{
  "github.copilot.chat.codeGeneration.instructions": [
    {
      "file": ".github/copilot-instructions.md"
    },
    {
      "file": ".github/copilot-python.md",
      "applyTo": "**/*.py"
    },
    {
      "file": ".github/copilot-tests.md",
      "applyTo": "**/test_*.py"
    }
  ]
}
```

## 실전 예제

### 프로젝트 초기 설정 체크리스트

```markdown
- [ ] .github/copilot-instructions.md 작성
- [ ] 기술 스택 명시
- [ ] 코딩 컨벤션 정의
- [ ] 보안 요구사항 문서화
- [ ] 테스트 정책 수립
- [ ] .editorconfig 설정
- [ ] Linter/Formatter 설정
- [ ] VS Code 워크스페이스 설정
- [ ] 팀원과 설정 공유
- [ ] README에 Copilot 가이드 링크 추가
```

## 다음 단계

다음 섹션에서는 GitHub Copilot Spaces를 활용한 고급 협업 방법을 학습합니다.

---

**참고 자료**
- [Copilot Instructions 가이드](https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot)
- [VS Code Copilot 설정](https://code.visualstudio.com/docs/copilot/copilot-settings)

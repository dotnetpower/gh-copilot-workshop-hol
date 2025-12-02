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
이 프로젝트는 React + TypeScript 기반의 전자상거래 플랫폼입니다.

## 기술 스택
- Frontend: React 18, TypeScript 5, Tailwind CSS
- Backend: Node.js, Express, PostgreSQL
- Testing: Jest, React Testing Library

## 코딩 규칙
1. 모든 컴포넌트는 함수형 컴포넌트로 작성
2. PropTypes 대신 TypeScript 인터페이스 사용
3. 상태 관리는 Zustand 사용
4. API 호출은 React Query 활용

## 명명 규칙
- 컴포넌트: PascalCase (예: ProductCard.tsx)
- 유틸 함수: camelCase (예: formatPrice.ts)
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

### React Component 템플릿

`.github/templates/react-component.md`:
```markdown
# React Component 템플릿

모든 React 컴포넌트는 다음 구조를 따릅니다:

```typescript
import React from 'react';

interface [ComponentName]Props {
  // Props 정의
}

/**
 * [컴포넌트 설명]
 * 
 * @param props - 컴포넌트 속성
 * @returns JSX.Element
 */
export const [ComponentName]: React.FC<[ComponentName]Props> = (props) => {
  // 상태 정의
  
  // 이벤트 핸들러
  
  // 부수 효과
  
  // 렌더링
  return (
    <div className="[component-name]">
      {/* 컴포넌트 내용 */}
    </div>
  );
};

export default [ComponentName];
```
```

### API Endpoint 템플릿

`.github/templates/api-endpoint.md`:
```markdown
# API Endpoint 템플릿

```typescript
import { Request, Response, NextFunction } from 'express';
import { body, validationResult } from 'express-validator';

/**
 * [엔드포인트 설명]
 * 
 * @route [METHOD] /api/v1/[resource]
 * @access [Public/Private/Admin]
 */

// 입력 검증
export const validate[Action] = [
  body('field').isString().notEmpty(),
  // 추가 검증 규칙
];

// 컨트롤러
export const [action]Controller = async (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  try {
    // 검증 결과 확인
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }
    
    // 비즈니스 로직
    
    // 응답
    res.status(200).json({
      success: true,
      data: result
    });
  } catch (error) {
    next(error);
  }
};
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

[*.{js,ts,jsx,tsx}]
indent_style = space
indent_size = 2

[*.{py}]
indent_style = space
indent_size = 4

[*.{md}]
trim_trailing_whitespace = false

[*.{yml,yaml}]
indent_style = space
indent_size = 2
```

### .prettierrc

```json
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 100,
  "tabWidth": 2,
  "arrowParens": "always"
}
```

### ESLint 설정

```javascript
// .eslintrc.js
module.exports = {
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended',
    'plugin:react/recommended',
    'prettier'
  ],
  rules: {
    // Copilot에게 준수시킬 규칙
    'no-console': 'warn',
    '@typescript-eslint/explicit-function-return-type': 'error',
    'react/prop-types': 'off', // TypeScript 사용 시
  }
};
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
      "text": "모든 API는 RESTful 원칙을 따르고 OpenAPI 3.0 스펙을 준수합니다."
    },
    {
      "text": "에러 처리는 RFC 7807 (Problem Details) 표준을 따릅니다."
    }
  ]
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
      "file": ".github/copilot-typescript.md",
      "applyTo": "**/*.{ts,tsx}"
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

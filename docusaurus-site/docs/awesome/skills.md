---
sidebar_position: 5
---

# Awesome Skills

전문화된 작업을 위한 AI 기능을 향상시키는 지침과 번들 리소스가 포함된 독립형 폴더입니다.

## 개요

Awesome Skills는 특정 작업이나 워크플로우를 위한 완전한 패키지입니다. 각 스킬은 지침, 예제 코드, 템플릿, 그리고 필요한 리소스를 포함하는 독립형 폴더로 구성됩니다.

## Skills vs Prompts vs Instructions

| 특징 | Skills | Prompts | Instructions |
|------|---------|---------|--------------|
| **범위** | 완전한 워크플로우 | 단일 작업 | 지속적인 가이드 |
| **구성** | 폴더 + 리소스 | 단일 파일 | 단일 파일 |
| **사용 방식** | 프로젝트 통합 | 명령어 실행 | 자동 적용 |
| **복잡도** | 높음 | 낮음 | 중간 |

## Skills 구조

일반적인 스킬 폴더 구조:

```
skill-name/
├── README.md              # 스킬 설명 및 사용법
├── instructions.md        # AI를 위한 지침
├── templates/             # 코드 템플릿
│   ├── component.tsx
│   ├── test.spec.ts
│   └── config.json
├── examples/              # 실제 사용 예제
│   └── sample-project/
└── resources/             # 추가 리소스
    ├── diagrams/
    └── docs/
```

## 사용 방법

### 1. 스킬 선택

필요한 작업에 맞는 스킬을 선택합니다:

- 웹 앱 테스팅
- API 개발
- 데이터베이스 마이그레이션
- CI/CD 파이프라인 설정
- 문서 생성

### 2. 스킬 설치

스킬을 프로젝트에 통합:

```bash
# MCP 서버를 통한 설치
copilot install skill webapp-testing

# 또는 수동 복사
cp -r skills/webapp-testing .copilot/skills/
```

### 3. 스킬 활성화

GitHub Copilot에서 스킬을 활성화:

```
@copilot use skill webapp-testing
```

### 4. 스킬 사용

활성화된 스킬을 사용하여 작업 수행:

```
@copilot generate test suite for user authentication
```

## 인기 있는 Skills

### 🌐 웹 앱 테스팅

- E2E 테스트 생성
- 단위 테스트 작성
- 통합 테스트 설정
- 테스트 데이터 관리

### 🔌 API 개발

- REST API 설계
- GraphQL 스키마 생성
- API 문서화
- 에러 핸들링 패턴

### 🗄️ 데이터베이스

- 마이그레이션 스크립트
- 쿼리 최적화
- 스키마 설계
- 시딩 데이터

### 🚀 DevOps

- CI/CD 파이프라인
- Docker 설정
- Kubernetes 배포
- 모니터링 구성

### 📱 모바일 개발

- React Native 컴포넌트
- 상태 관리
- 네비게이션 설정
- 푸시 알림

## 커스텀 스킬 만들기

자신만의 스킬을 만들 수 있습니다:

### 1. 폴더 구조 생성

```bash
mkdir -p .copilot/skills/my-skill/{templates,examples,resources}
```

### 2. README 작성

스킬의 목적과 사용법을 설명합니다.

### 3. 지침 작성

AI가 따라야 할 규칙과 패턴을 정의합니다.

### 4. 템플릿 제공

재사용 가능한 코드 템플릿을 추가합니다.

### 5. 예제 포함

실제 사용 사례를 보여주는 예제를 제공합니다.

## Skills 모범 사례

### ✅ 해야 할 것

- **명확한 문서**: 상세한 사용 설명서 제공
- **실용적인 예제**: 실제 시나리오 기반 예제 포함
- **유지보수**: 정기적으로 업데이트하고 개선
- **테스트**: 스킬이 예상대로 작동하는지 확인

### ❌ 하지 말아야 할 것

- **과도한 복잡성**: 너무 많은 기능을 하나의 스킬에 담지 말기
- **의존성 부족**: 필요한 도구나 라이브러리 명시
- **불명확한 지침**: 모호한 설명 피하기
- **버전 관리 무시**: 호환성 정보 제공

## 고급 기능

### 스킬 체이닝

여러 스킬을 조합하여 복잡한 워크플로우 구축:

```
@copilot chain webapp-testing api-development
```

### 스킬 커스터마이징

기존 스킬을 프로젝트에 맞게 수정:

```
@copilot customize skill webapp-testing
```

### 스킬 공유

팀이나 커뮤니티와 스킬 공유:

```
@copilot publish skill my-custom-skill
```

## 더 알아보기

전체 스킬 목록과 상세 문서는 [Awesome Skills 문서](https://github.com/github/awesome-copilot/blob/main/docs/README.skills.md)를 참조하세요.

## 기여하기

새로운 스킬을 추가하고 싶으신가요? [기여 가이드](https://github.com/github/awesome-copilot/blob/main/CONTRIBUTING.md)를 확인하세요.


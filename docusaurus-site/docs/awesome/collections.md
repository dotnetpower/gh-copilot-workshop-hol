---
sidebar_position: 6
---

# Awesome Collections

특정 테마와 워크플로우를 중심으로 구성된 관련 프롬프트, 지침, 채팅 모드의 큐레이션된 컬렉션입니다.

## 개요

Awesome Collections는 관련된 프롬프트, 지침, 에이전트를 함께 묶어 특정 작업이나 워크플로우를 위한 완전한 솔루션을 제공합니다. 각 컬렉션은 특정 테마나 기술 스택에 초점을 맞춥니다.

## Collections vs Skills

| 특징 | Collections | Skills |
|------|-------------|---------|
| **초점** | 테마별 그룹화 | 특정 작업 |
| **구성** | 여러 리소스 링크 | 독립형 폴더 |
| **사용성** | 선택적 사용 | 전체 패키지 |
| **유연성** | 높음 | 중간 |

## 주요 Collections

### 🤖 Awesome Copilot

메타 프롬프트 모음으로 GitHub Copilot 커스터마이제이션을 발견하고 생성하는 데 도움을 줍니다.

**포함 내용:**
- 6개 아이템
- 프롬프트 엔지니어링
- 에이전트 발견
- 커스터마이제이션 생성

**태그:** `github-copilot`, `discovery`, `meta`, `prompt-engineering`, `agents`

### 🤝 Partners

GitHub 파트너가 만든 커스텀 에이전트 모음입니다.

**포함 내용:**
- 20개 아이템
- 파트너 통합 에이전트
- 엔터프라이즈 도구

**태그:** `devops`, `security`, `database`, `cloud`, `infrastructure`, `observability`, `feature-flags`, `cicd`, `migration`, `performance`

## Collections 구조

컬렉션은 YAML 파일로 정의됩니다:

```yaml
---
name: Web Development
description: 웹 개발을 위한 완전한 도구 모음
tags: [web, frontend, backend, fullstack]
items:
  - type: prompt
    name: create-api
    path: prompts/create-api.prompt.md
  - type: instruction
    name: react-best-practices
    path: instructions/react.instructions.md
  - type: agent
    name: webpack-expert
    path: agents/webpack.agent.md
---
```

## 사용 방법

### 1. 컬렉션 탐색

사용 가능한 컬렉션을 탐색:

```
@copilot list collections
```

### 2. 컬렉션 설치

필요한 컬렉션을 설치:

```
@copilot install collection web-development
```

### 3. 컬렉션 활성화

컬렉션의 모든 항목을 활성화:

```
@copilot use collection web-development
```

### 4. 개별 항목 사용

컬렉션에서 특정 항목만 사용:

```
@copilot use collection web-development item create-api
```

## 인기 있는 Collections

### 🌐 웹 개발

**포함 내용:**
- React/Vue/Angular 프롬프트
- 프론트엔드 모범 사례
- API 개발 지침
- 풀스택 패턴

**사용 사례:**
- SPA 개발
- REST/GraphQL API
- 상태 관리
- 라우팅 및 네비게이션

### 🐍 Python 개발

**포함 내용:**
- PEP 8 지침
- FastAPI/Django 프롬프트
- 데이터 과학 도구
- 테스팅 프레임워크

**사용 사례:**
- 웹 API 개발
- 데이터 분석
- 머신러닝 파이프라인
- 자동화 스크립트

### ☁️ 클라우드 인프라

**포함 내용:**
- AWS/Azure/GCP 프롬프트
- IaC 지침 (Terraform, CloudFormation)
- Kubernetes 설정
- CI/CD 파이프라인

**사용 사례:**
- 클라우드 배포
- 인프라 자동화
- 컨테이너 오케스트레이션
- 모니터링 설정

### 🔒 보안

**포함 내용:**
- 보안 코딩 지침
- 취약점 스캔 프롬프트
- 인증/권한 부여 패턴
- OWASP 모범 사례

**사용 사례:**
- 보안 감사
- 코드 리뷰
- 취약점 수정
- 보안 테스트

### 🧪 테스팅

**포함 내용:**
- 단위 테스트 프롬프트
- E2E 테스트 지침
- TDD 패턴
- 테스트 커버리지 도구

**사용 사례:**
- 테스트 작성
- 리팩토링
- 품질 보증
- 회귀 테스트

## 커스텀 Collection 만들기

자신만의 컬렉션을 만들 수 있습니다:

### 1. YAML 파일 생성

```yaml
---
name: My Custom Collection
description: 내 팀을 위한 맞춤형 컬렉션
version: 1.0.0
author: Your Name
tags: [custom, team, internal]
items:
  - type: prompt
    name: team-standard-api
    path: prompts/team-api.prompt.md
    description: 우리 팀의 API 표준
  
  - type: instruction
    name: coding-standards
    path: instructions/team-standards.instructions.md
    description: 팀 코딩 표준
  
  - type: agent
    name: team-reviewer
    path: agents/reviewer.agent.md
    description: 코드 리뷰 에이전트
---
```

### 2. 메타데이터 추가

- **name**: 컬렉션 이름
- **description**: 간단한 설명
- **version**: 버전 번호
- **author**: 작성자
- **tags**: 검색 태그

### 3. 항목 정의

각 항목에 대해:
- **type**: prompt, instruction, agent, skill
- **name**: 항목 이름
- **path**: 파일 경로
- **description**: 항목 설명

### 4. 테스트 및 공유

컬렉션을 테스트하고 팀이나 커뮤니티와 공유합니다.

## Collection 모범 사례

### ✅ 해야 할 것

- **명확한 테마**: 관련 있는 항목만 포함
- **상세한 설명**: 각 항목의 목적 명시
- **버전 관리**: 변경 사항 추적
- **문서화**: 사용 예제 제공

### ❌ 하지 말아야 할 것

- **너무 많은 항목**: 집중도가 떨어짐
- **중복**: 유사한 기능의 항목 중복
- **불명확한 분류**: 테마가 맞지 않는 항목 포함
- **유지보수 부족**: 오래된 항목 방치

## 고급 사용법

### 컬렉션 필터링

특정 태그로 컬렉션 필터링:

```
@copilot list collections --tag=security
```

### 컬렉션 업데이트

컬렉션을 최신 버전으로 업데이트:

```
@copilot update collection web-development
```

### 컬렉션 커스터마이징

기존 컬렉션을 기반으로 커스터마이징:

```
@copilot fork collection web-development my-web-dev
```

### 컬렉션 공유

팀이나 조직과 공유:

```
@copilot share collection my-custom-collection --team
```

## 더 알아보기

전체 컬렉션 목록과 상세 문서는 [Awesome Collections 문서](https://github.com/github/awesome-copilot/blob/main/docs/README.collections.md)를 참조하세요.

## 기여하기

새로운 컬렉션을 추가하고 싶으신가요? [기여 가이드](https://github.com/github/awesome-copilot/blob/main/CONTRIBUTING.md)를 확인하세요.


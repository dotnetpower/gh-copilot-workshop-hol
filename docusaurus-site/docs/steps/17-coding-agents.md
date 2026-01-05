---
sidebar_position: 16
title: 코딩 에이전트
description: GitHub Copilot의 @workspace, @terminal 등 코딩 에이전트를 활용한 개발 작업 자동화
---

# 코딩 에이전트

## 개요

GitHub Copilot의 코딩 에이전트(@workspace, @terminal 등)를 활용하여 복잡한 개발 작업을 자동화하고 생산성을 극대화하는 방법을 학습합니다.

## 에이전트 종류

### @workspace - 워크스페이스 컨텍스트

**전체 프로젝트 이해**
```
@workspace 이 프로젝트의 아키텍처를 설명해줘
```

Copilot이 분석하는 내용:
- 프로젝트 구조 및 파일 조직
- 사용 중인 프레임워크 및 라이브러리
- 코딩 패턴 및 컨벤션
- 주요 컴포넌트 간 관계

**프로젝트 전반 검색**
```
@workspace 인증 관련 코드가 어디에 있어?

@workspace 데이터베이스 연결 설정을 어디서 하고 있어?

@workspace 에러 핸들링 패턴을 보여줘
```

**리팩토링 제안**
```
@workspace 중복 코드를 찾아서 리팩토링 방법을 제안해줘

@workspace 보안 취약점이 있는 코드를 찾아줘

@workspace 성능 개선이 필요한 부분을 찾아줘
```

### @terminal - 터미널 명령 에이전트

**복잡한 명령어 생성**
```
@terminal Git에서 마지막 3개 커밋을 하나로 합치는 명령어

@terminal Docker 컨테이너의 로그를 실시간으로 보면서 특정 문자열 필터링

@terminal 현재 디렉토리에서 7일 이상 된 .log 파일 모두 삭제
```

Copilot의 응답 예시:
```bash
# Git 커밋 합치기
git reset --soft HEAD~3
git commit -m "Combined commit message"

# Docker 로그 필터링
docker logs -f container_name 2>&1 | grep "ERROR"

# 오래된 로그 파일 삭제
find . -name "*.log" -type f -mtime +7 -delete
```

**스크립트 생성**
```
@terminal 매일 자정에 데이터베이스 백업하는 cron job 만들어줘

@terminal CI/CD 파이프라인 상태를 확인하는 bash 스크립트
```

### @vscode - VS Code 기능 활용

**설정 최적화**
```
@vscode Python 프로젝트를 위한 최적의 settings.json 설정

@vscode Python 개발을 위한 추천 확장 프로그램과 설정
```

**작업 자동화**
```
@vscode 코드 포맷팅과 린팅을 저장 시 자동으로 실행하도록 설정

@vscode 디버깅 설정을 프로젝트에 맞게 구성해줘
```

## 멀티 에이전트 워크플로우

### 시나리오 1: 새로운 기능 개발

**1단계: 프로젝트 분석**
```
@workspace 현재 프로젝트의 사용자 관리 시스템 구조를 설명해줘
```

**2단계: 구현 계획**
```
사용자 프로필 이미지 업로드 기능을 추가하려고 해.
기존 코드베이스와 일관되게 구현하려면 어떻게 해야 할까?
```

**3단계: 코드 생성**
```
위 계획에 따라 다음을 생성해줘:
1. API 엔드포인트 (FastAPI)
2. 프론트엔드 컴포넌트 (React)
3. 테스트 코드 (pytest)
4. 데이터 모델 (Pydantic)
```

**4단계: 배포 준비**
```
@terminal 이 기능을 프로덕션에 배포하기 위한 명령어 시퀀스

@workspace CI/CD 파이프라인에 이미지 처리 테스트를 추가해줘
```

### 시나리오 2: 버그 수정

**1단계: 버그 분석**
```
@workspace "사용자 로그인 후 대시보드가 표시되지 않음" 
이슈와 관련된 코드를 찾아줘
```

**2단계: 원인 파악**
```
찾은 코드를 분석해서 버그의 원인을 설명해줘.
관련된 모든 파일을 보여줘.
```

**3단계: 수정**
```
버그를 수정하고, 같은 문제가 다른 곳에도 있는지 확인해줘
```

**4단계: 테스트 추가**
```
이 버그가 재발하지 않도록 회귀 테스트를 작성해줘
```

## 고급 에이전트 활용

### 커스텀 에이전트 만들기

**프로젝트별 에이전트 설정**

`.github/copilot-agents/code-review.md`:
```markdown
# Code Review Agent

당신은 코드 리뷰 전문가입니다.

## 체크리스트
1. 보안: SQL 인젝션, XSS, CSRF 취약점 확인
2. 성능: N+1 쿼리, 메모리 누수 확인
3. 테스트: 테스트 커버리지 및 엣지 케이스
4. 문서화: 주석, README 업데이트
5. 컨벤션: 프로젝트 코딩 스타일 준수

## 리뷰 형식
각 항목에 대해:
- ✅ 통과
- ⚠️ 개선 필요
- ❌ 수정 필수

구체적인 코드 예시와 함께 제안 제공
```

**사용 예시**
```
@workspace /agent:code-review 
이 PR의 변경사항을 리뷰해줘
```

### 에이전트 체인

**복잡한 작업 자동화**

```yaml
# .github/copilot-workflows/feature-development.yml
workflow:
  name: "Full Feature Development"
  
  steps:
    - agent: "@workspace"
      task: "Analyze current architecture"
      
    - agent: "custom-architect"
      task: "Design feature implementation"
      input: "{{ previous.output }}"
      
    - agent: "code-generator"
      task: "Generate implementation code"
      input: "{{ previous.design }}"
      
    - agent: "test-generator"
      task: "Create comprehensive tests"
      input: "{{ previous.code }}"
      
    - agent: "@terminal"
      task: "Run tests and validation"
      
    - agent: "documentation"
      task: "Update documentation"
      input: "{{ all.outputs }}"
```

## 실전 예제

### 예제 1: API 엔드포인트 생성

**1. 요구사항 분석**
```
@workspace 현재 API 엔드포인트들의 패턴과 구조를 보여줘
```

**2. 구현**
```
위 패턴을 따라서 새로운 엔드포인트를 만들어줘:

기능: 사용자 활동 로그 조회
- GET /api/v1/users/:userId/activity
- 쿼리 파라미터: startDate, endDate, limit, offset
- 응답: 페이지네이션된 활동 로그
- 인증: JWT 필요
- 권한: 본인 또는 관리자만 조회 가능
```

**3. 테스트 생성**
```
위 엔드포인트의 테스트 코드를 작성해줘:
- 정상 케이스
- 권한 없음
- 잘못된 파라미터
- 페이지네이션
```

**4. 문서화**
```
OpenAPI 3.0 스펙 문서를 생성해줘
```

### 예제 2: 레거시 코드 현대화

**전체 프로세스 자동화**
```
@workspace 
1. src/legacy/ 디렉토리의 코드를 분석해줘
2. ES5 문법을 ES2020+로 변환하는 계획을 세워줘
3. 각 파일을 현대화하되, 기능은 동일하게 유지
4. 변경사항에 대한 테스트 추가
5. 마이그레이션 가이드 문서 생성
```

### 예제 3: 성능 최적화

```
@workspace 
이 애플리케이션의 성능 병목을 찾아서:

1. N+1 쿼리 문제 식별
2. 불필요한 re-render 찾기
3. 메모리 누수 가능성 확인
4. 번들 크기 최적화 제안

각 문제에 대해:
- 현재 코드
- 문제점 설명
- 개선된 코드
- 예상 성능 향상
```

## 에이전트 베스트 프랙티스

### Do's ✅

1. **구체적인 컨텍스트 제공**
```
❌ "에러 수정해줘"
✅ "@workspace 사용자 로그인 시 발생하는 401 에러를 
    인증 미들웨어와 관련해서 확인하고 수정해줘"
```

2. **단계별 접근**
```
# 큰 작업을 작은 단계로 분리
1. @workspace 현재 상태 분석
2. 문제 식별
3. 해결 방안 제안
4. 구현
5. 테스트
6. 문서화
```

3. **검증 요청**
```
위 코드의 보안 취약점과 성능 이슈를 확인해줘.
프로덕션 배포 전 체크리스트도 만들어줘.
```

### Don'ts ❌

1. **모호한 요청**
```
❌ "코드 개선해줘"
✅ "이 함수의 시간 복잡도를 O(n²)에서 O(n)으로 개선해줘"
```

2. **컨텍스트 무시**
```
❌ 프로젝트 구조를 무시한 코드 생성
✅ @workspace를 활용해 기존 패턴 따르기
```

3. **과도한 의존**
```
❌ 생성된 코드를 검증 없이 사용
✅ 생성된 코드를 이해하고 테스트 후 사용
```

## 생산성 측정

### 에이전트 활용 효과

**측정 지표**
```yaml
metrics:
  # 개발 속도
  - 기능 구현 시간: 50% 감소
  - 버그 수정 시간: 40% 감소
  - 코드 리뷰 시간: 30% 감소
  
  # 코드 품질
  - 테스트 커버리지: 65% → 85%
  - 코드 중복: 15% → 5%
  - 보안 취약점: 8개 → 2개
  
  # 개발자 만족도
  - 반복 작업 감소: 70%
  - 학습 곡선 개선: 60%
  - 전반적 만족도: 4.2/5.0 → 4.7/5.0
```

## 실습 과제

### 과제 1: 에이전트 워크플로우 만들기

새로운 REST API 리소스를 추가하는 완전 자동화된 워크플로우를 만들어보세요:

```
1. @workspace로 기존 API 패턴 분석
2. 새 리소스 설계
3. CRUD 엔드포인트 생성
4. 데이터 모델 정의
5. 테스트 코드 작성
6. API 문서 생성
7. @terminal로 마이그레이션 실행
```

### 과제 2: 코드 리뷰 에이전트

자동화된 코드 리뷰 에이전트를 만들어보세요:

```
보안, 성능, 테스트, 문서화 측면에서
PR의 변경사항을 분석하고
구체적인 개선 제안을 제공하는 에이전트
```

## 다음 단계

축하합니다! GitHub Copilot의 모든 주요 기능을 학습했습니다.

**추가 학습 자료:**
- [GitHub Copilot 블로그](https://github.blog/tag/github-copilot/)
- [Copilot 커뮤니티](https://github.com/community/community/discussions/categories/copilot)
- [Best Practices 가이드](https://docs.github.com/copilot/using-github-copilot/best-practices-for-using-github-copilot)

**다음 스텝:**
- 실제 프로젝트에 적용
- 팀원과 베스트 프랙티스 공유
- 조직 차원의 Copilot 전략 수립

---

**참고 자료**
- [GitHub Copilot Agents 문서](https://docs.github.com/copilot/using-github-copilot/using-chat-agents)
- [AI-Assisted Development Guide](https://github.blog/developer-skills/)

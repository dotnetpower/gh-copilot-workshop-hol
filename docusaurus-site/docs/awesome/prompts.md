---
sidebar_position: 3
---

# Awesome Prompts

코드, 문서 생성 및 특정 문제 해결을 위한 집중적이고 작업별 프롬프트 모음입니다.

## 개요

Awesome Prompts는 GitHub Copilot Chat에서 사용할 수 있는 사전 정의된 프롬프트 모음입니다. 이 프롬프트들은 일반적인 개발 작업을 위해 최적화되어 있으며, 일관성 있고 고품질의 결과를 제공합니다.

## 사용 방법

GitHub Copilot Chat에서 `/` 명령을 사용하여 프롬프트에 액세스합니다:

```
/awesome-copilot <prompt-name>
```

### 예제

```
/awesome-copilot create-readme
```

이 명령은 프로젝트를 위한 포괄적인 README 파일을 생성합니다.

## 프롬프트 카테고리

### 📝 문서화

- **create-readme**: 프로젝트 README 파일 생성
- **api-docs**: API 문서 생성
- **changelog**: 변경 로그 작성
- **contributing-guide**: 기여 가이드 작성

### 🏗️ 코드 생성

- **boilerplate**: 프로젝트 보일러플레이트 생성
- **api-endpoint**: REST API 엔드포인트 생성
- **database-schema**: 데이터베이스 스키마 설계
- **test-cases**: 테스트 케이스 생성

### 🔧 리팩토링

- **optimize-performance**: 성능 최적화 제안
- **improve-readability**: 코드 가독성 개선
- **security-review**: 보안 취약점 검토
- **extract-function**: 함수 추출 리팩토링

### 🐛 디버깅

- **analyze-error**: 에러 분석 및 해결 방법 제안
- **debug-performance**: 성능 문제 디버깅
- **memory-leak**: 메모리 누수 분석
- **race-condition**: 경쟁 조건 탐지

### 🧪 테스팅

- **unit-test**: 단위 테스트 생성
- **integration-test**: 통합 테스트 생성
- **e2e-test**: E2E 테스트 시나리오 작성
- **test-coverage**: 테스트 커버리지 분석

## 프롬프트 작성 모범 사례

1. **명확성**: 프롬프트는 명확하고 구체적이어야 합니다
2. **컨텍스트**: 충분한 컨텍스트를 제공하여 더 나은 결과를 얻으세요
3. **반복**: 결과가 만족스럽지 않으면 프롬프트를 조정하세요
4. **재사용성**: 자주 사용하는 프롬프트는 저장하여 재사용하세요

## 커스텀 프롬프트 만들기

자신만의 프롬프트를 만들 수도 있습니다:

1. `.prompt.md` 파일 생성
2. 프론트매터에 메타데이터 추가
3. 프롬프트 내용 작성
4. Awesome GitHub Copilot 리포지토리에 기여

## 더 알아보기

전체 프롬프트 목록과 상세 문서는 [Awesome Prompts 문서](https://github.com/github/awesome-copilot/blob/main/docs/README.prompts.md)를 참조하세요.

## 기여하기

새로운 프롬프트를 추가하고 싶으신가요? [기여 가이드](https://github.com/github/awesome-copilot/blob/main/CONTRIBUTING.md)를 확인하세요.


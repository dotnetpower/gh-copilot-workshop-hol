---
sidebar_position: 4
title: 제한사항과 주의사항
description: GitHub Copilot 사용 시 알아야 할 제한사항과 보안, 품질 관리 베스트 프랙티스
---

# 제한사항

## 주요 제한사항

### 1. 학습 데이터 기반

#### 📚 GitHub Copilot은 어떤 코드로 학습되었나?

GitHub Copilot은 처음부터 **OpenAI의 Codex 계열 모델**을 기반으로 만들어졌고, 이 모델들은 다음과 같은 데이터로 학습되었습니다:

* **공개적으로 접근 가능한 소스 코드**
  * GitHub의 **Public Repository**
  * 오픈소스 프로젝트
* 공개 문서, 기술 문서 등 자연어 텍스트
* 라이선스가 있거나 합법적으로 수집된 코드 데이터

:::info 중요한 점
* 개인(private) 저장소 코드는 기본적으로 학습에 사용되지 않습니다.
* Copilot이 사용자의 코드를 "실시간으로 학습"하는 구조는 아닙니다.
* 이미 학습된 모델을 기반으로 추론만 수행합니다.
:::

#### ⏰ 학습 데이터의 시점

**정확한 날짜 컷오프는 공개되어 있지 않습니다.** GitHub와 OpenAI는 학습 데이터의 정확한 수집 종료 날짜를 공개하지 않지만, 추정 가능한 범위는 있습니다:

**초기 GitHub Copilot (Codex 기반)**
* GitHub Copilot 최초 공개: **2021년 6월 29일**
* 당시 사용된 모델: **OpenAI Codex**
* 초기 Copilot은 대략 **2020년 ~ 2021년 초반까지의 공개 GitHub 코드**를 중심으로 학습
* Codex는 수천만 개의 GitHub 공개 리포지토리에서 수집한 코드 포함

**최근 GitHub Copilot (2023~2025)**

최근 Copilot은 단일 Codex가 아니라 여러 최신 모델을 사용합니다:
* GPT-4 / GPT-4o 계열
* Claude
* Gemini (일부 환경)

이 모델들의 특징:
* 공개 코드 + 라이선스 데이터 + 사람이 작성한 데이터로 학습
* 학습 데이터는 모델 출시 수개월 전까지의 데이터가 반영됨
* GPT-4o 계열: 대략 **2024년 상반기 이전 데이터까지 포함**

:::tip 한 줄 요약
GitHub Copilot은 공개 GitHub 리포지토리를 포함한 오픈소스 코드를 기반으로 학습되었으며, 초기 버전은 2020~2021년, 최신 Copilot은 대략 2024년 이전의 공개 코드까지 반영된 모델을 사용합니다.
:::

#### 실질적인 영향

- 최신 라이브러리나 프레임워크는 제한적 지원 => **이 부분을 완화하기 위해서 Context7 MCP 사용**
- 새로운 API나 기능에 대한 정보 부족 가능
- 최근에 출시된 기술은 제안의 정확도가 낮을 수 있음

### 2. 컨텍스트 제한
- 현재 파일과 몇 개의 관련 파일만 분석
- 전체 프로젝트 구조 이해 어려움
- 복잡한 비즈니스 로직 파악 제한

### 3. 코드 품질
- 항상 최적의 솔루션을 제공하지는 않음
- 보안 취약점이 포함될 수 있음
- 성능 최적화가 부족할 수 있음

## 주의사항

### ⚠️ 보안
```python
import os

# Copilot이 제안할 수 있는 안전하지 않은 코드
password = "hardcoded_password"  # ❌ 하드코딩된 비밀번호

# 대신 환경 변수 사용
password = os.getenv("PASSWORD")  # ✅
```

### ⚠️ 라이선스
- 제안된 코드의 라이선스 확인 필요
- 공개 저장소 코드가 포함될 수 있음
- 상업적 사용 시 주의

### ⚠️ 정확성
- 생성된 코드 검토 필수
- 단위 테스트 작성 권장
- 비즈니스 로직 검증 필요

## 베스트 프랙티스

### 1. 코드 리뷰
모든 Copilot 제안 코드는 반드시 리뷰하세요.

### 2. 테스트
```python
# Copilot 생성 함수
def calculate_total(items):
    return sum(item.price for item in items)

# 반드시 테스트 작성
def test_calculate_total():
    items = [Item(10), Item(20)]
    assert calculate_total(items) == 30
```

### 3. 보안 스캔
- 정기적인 보안 스캔 실행
- 민감 정보 하드코딩 확인
- 의존성 취약점 점검

## 올바른 사용 방법

✅ **DO**
- Copilot을 보조 도구로 활용
- 생성된 코드 검토 및 수정
- 팀 코딩 표준에 맞게 조정

❌ **DON'T**
- 맹목적으로 제안 수락
- 이해하지 못한 코드 사용
- 보안 검토 없이 배포

## 참고 자료

### 공식 문서 및 신뢰 가능한 출처

- [GitHub Copilot 공식 페이지](https://github.com/features/copilot)
- [GitHub Copilot 출시 발표 (2021-06-29)](https://github.blog/2021-06-29-introducing-github-copilot-ai-pair-programmer/)
- [GitHub Copilot Wikipedia](https://en.wikipedia.org/wiki/GitHub_Copilot)
- [OpenAI Codex 설명](https://openai.com/blog/openai-codex)
- [GitHub Copilot FAQ](https://github.com/features/copilot#faq)

### 추가 참고 사항

GitHub Copilot의 학습 데이터 및 프라이버시 정책에 대한 더 자세한 내용은 공식 문서를 참고하시기 바랍니다.

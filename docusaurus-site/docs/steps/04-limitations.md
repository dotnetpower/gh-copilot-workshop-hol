---
sidebar_position: 4
title: 제한사항과 주의사항
description: GitHub Copilot 사용 시 알아야 할 제한사항과 보안, 품질 관리 베스트 프랙티스
---

# 제한사항

## 주요 제한사항

### 1. 학습 데이터 기반
- 2021년까지의 공개 코드로 학습
- 최신 라이브러리나 프레임워크는 제한적 지원
- 새로운 API나 기능에 대한 정보 부족 가능

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
```javascript
// Copilot이 제안할 수 있는 안전하지 않은 코드
const password = "hardcoded_password"; // ❌ 하드코딩된 비밀번호

// 대신 환경 변수 사용
const password = process.env.PASSWORD; // ✅
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

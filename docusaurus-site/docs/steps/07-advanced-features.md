---
sidebar_position: 7
---

# 고급 기능

## 코드 리팩토링

기존 코드를 개선하고 최적화합니다.

### 방법
1. 코드 선택
2. Chat에서 "/refactor" 명령 사용
3. 제안 검토 및 적용

## 테스트 코드 생성

자동으로 단위 테스트를 생성합니다.

### 예제
```javascript
// Chat: "이 함수의 테스트 코드 작성해줘"
function multiply(a, b) {
    return a * b;
}
```

## 문서화

함수와 클래스에 대한 문서를 자동 생성합니다.

### JSDoc 생성
```javascript
/**
 * 두 숫자를 곱합니다
 * @param {number} a - 첫 번째 숫자
 * @param {number} b - 두 번째 숫자
 * @returns {number} 곱셈 결과
 */
```

## 실습

1. 기존 코드 리팩토링해보기
2. 테스트 코드 자동 생성
3. 문서 주석 추가하기

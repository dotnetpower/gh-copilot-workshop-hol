---
sidebar_position: 10
title: 실습 1 - Code Completion
description: GitHub Copilot의 기본 코드 자동완성 기능과 인라인 제안 활용 실습
---

# 실습 1: Code Completion

:::tip 📝 학습 목표
- GitHub Copilot의 기본 코드 자동완성 기능 익히기
- 인라인 제안(Inline Suggestions) 활용법 학습
- 키보드 단축키를 통한 효율적인 코딩 방법 습득
:::

## 🛠️ 실습 내용

### 1.1 기본 설정
- **활성화/비활성화**: `Ctrl + Shift + P` → "Copilot: Enable/Disable"
- **제안 툴바 활성화**
  
  ![Image text](/assets/copilot_toolbar.png)

### 1.2 주요 단축키
- `Tab`: 인라인 제안 수락
- `Esc`: 인라인 제안 거부
- `Alt + ]`: 다음 제안 표시
  
  ![Image text](/assets/suggestion_tip.png)
  
- `Alt + [`: 이전 제안 표시
- `Alt + \`: 인라인 제안 트리거
- `Ctrl + I`: 인라인 프롬프트 작성
  
  ![alt text](/assets/inline_prompt.png)

### 1.3 기본 코드 자동완성
```javascript
// 함수명과 주석만 작성하면 Copilot이 구현체를 제안합니다
function calculateTax(price, taxRate) {
  // 세금을 계산하는 함수
  
}
```

### 1.4 반복 패턴 학습
```python
# 몇 개의 예시를 작성하면 패턴을 학습하여 나머지를 자동완성합니다
def get_monday():
    return "Monday"

def get_tuesday():
    return "Tuesday"

# Copilot이 나머지 요일 함수들을 자동으로 제안합니다
```

### 1.5 주석 활용
```javascript
// 배열에서 최대값을 찾는 함수
function findMax(arr) {
  // Copilot이 구현체를 제안합니다
}
```

:::note ✅ 실습 과제
1. 간단한 계산기 함수 작성 (덧셈, 뺄셈, 곱셈, 나눗셈)
2. 배열 정렬 함수 구현
3. 문자열 처리 유틸리티 함수 작성
:::

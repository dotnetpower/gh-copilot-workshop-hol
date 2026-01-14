---
sidebar_position: 11
title: 실습 2 - Copilot Chat으로 코드 품질 개선
description: GitHub Copilot Chat을 활용한 코드 리뷰, 테스트 생성, 문서화 자동화 실습
---

# 실습 2: Copilot Chat을 이용하여 코드 품질 개선

:::tip 📝 학습 목표
- GitHub Copilot의 Ask, Edit, Agent 모드 활용법 학습
- 효과적인 코드 리뷰를 위한 프롬프트 작성 방법 습득
- 테스트 코드 자동 생성 및 문서화 자동화 실전 적용
- 코드 품질 개선을 위한 실질적인 워크플로우 경험
:::

## 🎯 실습 준비

이 실습에서는 실제 코드를 개선하는 과정을 체험합니다. 

**소요 시간**: 약 10분

**준비물**:
- GitHub Copilot이 활성화된 VS Code
- Python 또는 JavaScript/TypeScript 실행 환경

## 🛠️ 실습 내용

### 2.1 실습용 샘플 코드 준비

먼저 품질 개선이 필요한 샘플 코드를 작성하겠습니다.

`playground/user_service.py` 파일을 생성하고 다음 코드를 작성하세요:

```python
import re

def process_user_data(data):
    users = []
    for item in data:
        if item['age'] > 18 and item['email'] != '' and re.match(r'^[^\s@]+@[^\s@]+\.[^\s@]+$', item['email']):
            users.append({'name': item['name'], 'email': item['email'], 'age': item['age'], 'status': 'active'})
    return users

def calculate_discount(user_age, purchase_amount):
    if user_age < 18:
        return 0
    elif user_age >= 18 and user_age < 25:
        if purchase_amount > 100:
            return purchase_amount * 0.1
        else:
            return purchase_amount * 0.05
    elif user_age >= 25 and user_age < 60:
        if purchase_amount > 200:
            return purchase_amount * 0.15
        else:
            return purchase_amount * 0.1
    else:
        if purchase_amount > 150:
            return purchase_amount * 0.2
        else:
            return purchase_amount * 0.15
```

### 2.2 코드 리뷰 받기 (Ask 모드)

#### 실습 2-1: 전체 코드 리뷰 요청

1. `user_service.py` 파일을 열고 전체 코드를 선택합니다
2. Copilot Chat 창에서 다음 프롬프트를 입력하세요:

```
이 코드를 보안, 성능, 가독성 관점에서 리뷰해주세요. 
개선이 필요한 부분을 우선순위와 함께 알려주세요.
```

**예상 결과**: Copilot이 다음과 같은 개선점을 제안할 것입니다:
- 긴 함수를 작은 함수로 분리
- 매직 넘버를 상수로 정의
- 중첩된 if문 개선
- 타입 힌트 추가
- 에러 처리 추가

#### 실습 2-2: 특정 함수 개선 요청

`calculate_discount` 함수를 선택하고 다음 프롬프트를 시도하세요:

```
이 함수의 복잡도를 줄이고 가독성을 개선해주세요. 
딕셔너리나 데이터 구조를 활용하는 방법을 제안해주세요.
```

### 2.3 코드 개선하기 (Edit 모드)

#### 실습 2-3: 자동 리팩토링

1. `calculate_discount` 함수를 선택합니다
2. `Cmd/Ctrl + I`를 눌러 인라인 채팅을 활성화합니다
3. 다음 프롬프트를 입력하세요:

```
이 함수를 리팩토링해서:
1. 할인율을 설정 가능한 딕셔너리로 관리
2. 타입 힌트 추가
3. docstring 추가
4. 엣지 케이스 처리 추가
```

**기대 결과**:
```python
from typing import Dict, Tuple

# 할인율 설정: (최소 나이, 최대 나이, 최소 구매금액, 할인율)
DISCOUNT_RULES: list[Tuple[int, int, float, float]] = [
    (18, 25, 100, 0.10),
    (18, 25, 0, 0.05),
    (25, 60, 200, 0.15),
    (25, 60, 0, 0.10),
    (60, 200, 150, 0.20),
    (60, 200, 0, 0.15),
]

def calculate_discount(user_age: int, purchase_amount: float) -> float:
    """
    사용자 나이와 구매 금액에 따라 할인 금액을 계산합니다.
    
    Args:
        user_age: 사용자의 나이
        purchase_amount: 구매 금액
    
    Returns:
        할인 금액
    
    Raises:
        ValueError: user_age가 음수이거나 purchase_amount가 0 미만인 경우
    """
    if user_age < 0:
        raise ValueError("나이는 0 이상이어야 합니다")
    if purchase_amount < 0:
        raise ValueError("구매 금액은 0 이상이어야 합니다")
    
    if user_age < 18:
        return 0.0
    
    for min_age, max_age, min_amount, discount_rate in DISCOUNT_RULES:
        if min_age <= user_age < max_age and purchase_amount >= min_amount:
            return purchase_amount * discount_rate
    
    return 0.0
```

### 2.4 테스트 코드 생성

#### 실습 2-4: 단위 테스트 자동 생성

1. 개선된 `calculate_discount` 함수를 선택합니다
2. Copilot Chat에 다음 프롬프트를 입력하세요:

```
이 함수에 대한 pytest 테스트 코드를 작성해주세요.
다음을 포함해주세요:
- 정상 케이스 (각 나이대별)
- 경계값 테스트 (나이 17, 18, 25, 60 등)
- 예외 케이스 (음수 나이, 음수 금액)
- 파라미터화된 테스트 사용
```

**예상 생성 코드**:
```python
import pytest
from user_service import calculate_discount

class TestCalculateDiscount:
    @pytest.mark.parametrize("age,amount,expected", [
        # 미성년자
        (17, 100, 0.0),
        (10, 500, 0.0),
        
        # 18-25세
        (18, 50, 2.5),      # 5% 할인
        (18, 150, 15.0),    # 10% 할인
        (24, 100, 10.0),    # 10% 할인
        
        # 25-60세
        (25, 100, 10.0),    # 10% 할인
        (30, 250, 37.5),    # 15% 할인
        (59, 200, 30.0),    # 15% 할인
        
        # 60세 이상
        (60, 100, 15.0),    # 15% 할인
        (65, 200, 40.0),    # 20% 할인
        (80, 150, 30.0),    # 20% 할인
    ])
    def test_calculate_discount_valid_cases(self, age, amount, expected):
        """정상적인 할인 계산 테스트"""
        result = calculate_discount(age, amount)
        assert result == pytest.approx(expected, rel=1e-2)
    
    def test_calculate_discount_negative_age(self):
        """음수 나이 예외 테스트"""
        with pytest.raises(ValueError, match="나이는 0 이상"):
            calculate_discount(-1, 100)
    
    def test_calculate_discount_negative_amount(self):
        """음수 금액 예외 테스트"""
        with pytest.raises(ValueError, match="구매 금액은 0 이상"):
            calculate_discount(25, -10)
```

#### 실습 2-5: 테스트 실행

터미널에서 테스트를 실행하세요:

```bash
cd playground
pip install pytest
pytest test_user_service.py -v
```

### 2.5 문서화 자동 생성

#### 실습 2-6: README 문서 생성

1. `playground` 폴더를 선택합니다
2. Copilot Chat에 다음 프롬프트를 입력하세요:

```
이 user_service.py 모듈에 대한 README.md를 작성해주세요.
다음 항목을 포함해주세요:
- 모듈 설명
- 주요 함수 설명 및 사용 예제
- 설치 방법
- 테스트 실행 방법
- 할인 정책 테이블
```

#### 실습 2-7: 함수 docstring 개선

`process_user_data` 함수를 선택하고 다음 프롬프트를 입력하세요:

```
이 함수에 Google 스타일의 docstring을 추가하고,
타입 힌트도 함께 추가해주세요.
```

**예상 결과**:
```python
from typing import List, Dict, Any

def process_user_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    사용자 데이터를 검증하고 필터링합니다.
    
    성인(18세 이상)이면서 유효한 이메일을 가진 사용자만 필터링하여
    활성 상태로 표시합니다.
    
    Args:
        data (List[Dict[str, Any]]): 처리할 사용자 데이터 리스트.
            각 딕셔너리는 'name', 'email', 'age' 키를 포함해야 합니다.
    
    Returns:
        List[Dict[str, Any]]: 검증되고 필터링된 사용자 데이터 리스트.
            각 항목은 'name', 'email', 'age', 'status' 키를 포함합니다.
    
    Example:
        >>> data = [
        ...     {'name': 'Alice', 'email': 'alice@example.com', 'age': 25},
        ...     {'name': 'Bob', 'email': 'invalid-email', 'age': 30},
        ...     {'name': 'Charlie', 'email': 'charlie@example.com', 'age': 16}
        ... ]
        >>> process_user_data(data)
        [{'name': 'Alice', 'email': 'alice@example.com', 'age': 25, 'status': 'active'}]
    """
    users = []
    for item in data:
        if item['age'] > 18 and item['email'] != '' and re.match(r'^[^\s@]+@[^\s@]+\.[^\s@]+$', item['email']):
            users.append({'name': item['name'], 'email': item['email'], 'age': item['age'], 'status': 'active'})
    return users
```

### 2.6 고급 프롬프트 기법

#### 실습 2-8: 컨텍스트를 활용한 코드 리뷰

다음과 같이 구체적인 컨텍스트를 제공하는 프롬프트를 시도하세요:

```
이 코드는 하루 10만 건 이상의 요청을 처리하는 프로덕션 시스템에서 사용됩니다.
다음 관점에서 개선점을 제안해주세요:
1. 성능 최적화 (정규식 컴파일, 불필요한 연산 제거)
2. 보안 (입력 검증, SQL 인젝션 방지)
3. 에러 핸들링 (예외 상황 처리)
4. 메모리 효율성
```

#### 실습 2-9: 단계별 리팩토링 요청

```
이 process_user_data 함수를 다음 순서로 리팩토링해주세요:
1단계: 이메일 검증 로직을 별도 함수로 분리
2단계: 사용자 필터링 조건을 명확한 함수로 분리
3단계: 리스트 컴프리헨션으로 변경
각 단계마다 코드를 보여주고 설명해주세요.
```

### 2.7 에이전트 모드 활용

#### 실습 2-10: Agent를 이용한 전체 리팩토링

1. Copilot Chat 창에서 Agent 모드를 선택합니다
2. 다음 프롬프트를 입력하세요:

```
@workspace /new user_service.py 모듈을 완전히 리팩토링해서:
1. 각 함수를 별도 파일로 분리
2. 설정값을 config.py로 관리
3. 테스트 코드를 tests/ 디렉토리에 생성
4. README.md 작성
5. 타입 검사를 위한 mypy 설정 추가
엔터프라이즈급 코드 구조로 만들어주세요.
```

### 2.8 에이전트와 친해지기

에이전트와 상호작용을 통해 친해지면, 내 언어를 좀더 쉽게 이해합니다.

![Image text](/img/labs/agent_conv.png)

**팁**:
- 실제 에이전트는 현재 대화 세션 동안만 기억합니다
- 나의 표현 중에서 잘 작동하는 표현을 익히기 위해서 반복적으로 에이전트와 대화하세요
- 구체적인 요구사항을 제공할수록 더 정확한 결과를 얻습니다

## 📋 유용한 프롬프트 템플릿

### 코드 리뷰용 프롬프트

```
이 코드를 [보안/성능/가독성] 관점에서 리뷰해주세요.
OWASP Top 10과 SOLID 원칙을 고려해주세요.
```

```
프로덕션 환경에서 발생할 수 있는 잠재적 문제점을 찾아주세요.
각 문제에 대해 심각도(Critical/High/Medium/Low)를 표시해주세요.
```

### 테스트 생성용 프롬프트

```
이 함수에 대한 [pytest/unittest/jest] 테스트를 작성해주세요.
- 정상 케이스
- 경계값 테스트
- 예외 케이스
- Mock이 필요한 경우 포함
```

```
이 클래스의 테스트 커버리지를 90% 이상으로 만들기 위한
테스트 케이스를 제안해주세요.
```

### 문서화용 프롬프트

```
이 [함수/클래스/모듈]에 대한 [Google/NumPy/JSDoc] 스타일의
문서를 작성해주세요. 사용 예제도 포함해주세요.
```

```
이 API 엔드포인트에 대한 OpenAPI(Swagger) 문서를 생성해주세요.
요청/응답 예제와 에러 코드도 포함해주세요.
```

## ✅ 실습 체크리스트

완료한 항목에 체크하세요:

- [ ] 샘플 코드 작성 및 코드 리뷰 받기
- [ ] 함수 리팩토링하기 (Edit 모드)
- [ ] 테스트 코드 자동 생성하기
- [ ] 테스트 실행 및 통과 확인
- [ ] 함수 docstring 추가하기
- [ ] README 문서 생성하기
- [ ] 고급 프롬프트 기법 시도하기
- [ ] Agent 모드로 전체 프로젝트 구조 개선하기

## 🎓 학습 정리

이 실습에서 배운 내용:

1. **Ask 모드**: 코드에 대한 질문과 리뷰 요청
2. **Edit 모드**: 인라인으로 코드 직접 수정
3. **Agent 모드**: 복잡한 작업을 자동으로 수행
4. **효과적인 프롬프트 작성**: 구체적이고 맥락이 있는 요청
5. **실전 워크플로우**: 코드 작성 → 리뷰 → 테스트 → 문서화

## 🚀 다음 단계

- [실습 3: Edit과 Agent 모드 마스터하기](./lab3-edit-agents.md)
- [실습 4: 고급 기능 활용하기](./lab4-advanced.md)

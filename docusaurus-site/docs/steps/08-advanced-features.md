---
sidebar_position: 7
title: 고급 기능
description: Python 코드 리팩토링, pytest를 활용한 테스트 생성, 타입 힌트 추가, docstring 자동 생성 등 GitHub Copilot의 고급 기능을 실무에 활용하는 방법을 학습합니다. 코드 품질 향상, 보안 강화, 성능 최적화를 위한 Copilot 활용 패턴을 다룹니다.
---

# 고급 기능

GitHub Copilot의 고급 기능을 활용하면 단순한 코드 작성을 넘어 코드 품질 개선, 테스트 자동화, 문서화, 보안 강화 등 전문적인 개발 작업을 효율적으로 수행할 수 있습니다.

## 코드 리팩토링

기존 Python 코드를 클린 코드 원칙에 따라 개선하고 최적화합니다.

### 기본 리팩토링

**리팩토링 전 코드:**
```python
def calc(data):
    r = 0
    for i in data:
        if i > 0:
            r = r + i
    return r
```

**Copilot을 활용한 리팩토링:**
1. 리팩토링할 코드 선택
2. Chat에서 `/refactor 이 함수를 PEP 8 스타일로 개선하고 타입 힌트를 추가해줘` 입력
3. 제안된 코드 검토 및 적용

**리팩토링 후 코드:**
```python
from typing import List

def calculate_positive_sum(numbers: List[float]) -> float:
    """
    양수 값들의 합계를 계산합니다.
    
    Args:
        numbers: 계산할 숫자 리스트
        
    Returns:
        양수 값들의 합계
    """
    return sum(num for num in numbers if num > 0)
```

### 복잡한 함수 분리

**리팩토링 전 - 너무 많은 책임을 가진 함수:**
```python
def process_user_data(user_data):
    # 데이터 검증
    if not user_data.get('email'):
        raise ValueError("이메일 필수")
    if not user_data.get('name'):
        raise ValueError("이름 필수")
    
    # 데이터 정규화
    email = user_data['email'].lower().strip()
    name = user_data['name'].strip()
    
    # 데이터베이스 저장
    db.save({'email': email, 'name': name})
    
    # 이메일 발송
    send_email(email, "환영합니다")
    
    return True
```

**Chat 명령:**
```
/refactor 이 함수를 단일 책임 원칙에 따라 여러 함수로 분리하고, 
에러 처리를 개선해줘
```

**리팩토링 후 - 명확한 책임 분리:**
```python
from typing import Dict, Any
from dataclasses import dataclass

@dataclass
class UserData:
    email: str
    name: str

def validate_user_data(user_data: Dict[str, Any]) -> None:
    """사용자 데이터 유효성 검증"""
    if not user_data.get('email'):
        raise ValueError("이메일은 필수 항목입니다")
    if not user_data.get('name'):
        raise ValueError("이름은 필수 항목입니다")

def normalize_user_data(user_data: Dict[str, Any]) -> UserData:
    """사용자 데이터 정규화"""
    return UserData(
        email=user_data['email'].lower().strip(),
        name=user_data['name'].strip()
    )

def save_user(user: UserData) -> None:
    """사용자 정보를 데이터베이스에 저장"""
    db.save({'email': user.email, 'name': user.name})

def send_welcome_email(email: str) -> None:
    """환영 이메일 발송"""
    send_email(email, "환영합니다")

def process_user_data(user_data: Dict[str, Any]) -> bool:
    """
    사용자 데이터를 처리하는 메인 함수
    
    Args:
        user_data: 처리할 사용자 데이터
        
    Returns:
        처리 성공 여부
        
    Raises:
        ValueError: 데이터 유효성 검증 실패 시
    """
    validate_user_data(user_data)
    user = normalize_user_data(user_data)
    save_user(user)
    send_welcome_email(user.email)
    return True
```

### 성능 최적화 리팩토링

**Chat 명령:**
```
이 코드의 성능을 개선해줘. 특히 리스트 컴프리헨션과 
제너레이터를 활용해서 메모리 효율성을 높여줘
```

**최적화 전:**
```python
def process_large_dataset(data):
    filtered = []
    for item in data:
        if item['value'] > 100:
            filtered.append(item)
    
    results = []
    for item in filtered:
        results.append(transform(item))
    
    return results
```

**최적화 후:**
```python
from typing import Generator, Dict, Any

def process_large_dataset(data: list[Dict[str, Any]]) -> Generator[Any, None, None]:
    """
    대용량 데이터셋을 메모리 효율적으로 처리합니다.
    
    Args:
        data: 처리할 데이터 리스트
        
    Yields:
        변환된 데이터 아이템
    """
    return (
        transform(item) 
        for item in data 
        if item.get('value', 0) > 100
    )
```

## 테스트 코드 생성

pytest를 활용한 단위 테스트를 자동으로 생성합니다.

### 기본 테스트 생성

**원본 함수:**
```python
from typing import List

def calculate_average(numbers: List[float]) -> float:
    """숫자 리스트의 평균을 계산합니다."""
    if not numbers:
        raise ValueError("빈 리스트는 처리할 수 없습니다")
    return sum(numbers) / len(numbers)
```

**Chat 명령:**
```
이 함수에 대한 pytest 테스트 케이스를 작성해줘. 
정상 케이스, 경계 케이스, 예외 케이스를 모두 포함해줘
```

**생성된 테스트 코드:**
```python
import pytest
from decimal import Decimal

def test_calculate_average_with_positive_numbers():
    """정상적인 양수 리스트로 평균 계산"""
    # Arrange
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    
    # Act
    result = calculate_average(numbers)
    
    # Assert
    assert result == 3.0

def test_calculate_average_with_negative_numbers():
    """음수가 포함된 리스트로 평균 계산"""
    numbers = [-10.0, -5.0, 0.0, 5.0, 10.0]
    result = calculate_average(numbers)
    assert result == 0.0

def test_calculate_average_with_single_element():
    """단일 요소 리스트 처리"""
    numbers = [42.0]
    result = calculate_average(numbers)
    assert result == 42.0

def test_calculate_average_raises_error_for_empty_list():
    """빈 리스트로 호출 시 ValueError 발생 검증"""
    with pytest.raises(ValueError, match="빈 리스트는 처리할 수 없습니다"):
        calculate_average([])

def test_calculate_average_with_large_numbers():
    """큰 숫자 처리 테스트"""
    numbers = [1e10, 2e10, 3e10]
    result = calculate_average(numbers)
    assert result == 2e10

def test_calculate_average_precision():
    """소수점 정밀도 테스트"""
    numbers = [1.1, 2.2, 3.3]
    result = calculate_average(numbers)
    assert abs(result - 2.2) < 0.0001
```

### Mock을 활용한 외부 의존성 테스트

**원본 코드:**
```python
import requests
from typing import Dict, Any

def fetch_user_data(user_id: str) -> Dict[str, Any]:
    """외부 API에서 사용자 데이터를 가져옵니다."""
    response = requests.get(f"https://api.example.com/users/{user_id}")
    response.raise_for_status()
    return response.json()
```

**Chat 명령:**
```
이 함수를 테스트하는 코드를 작성해줘. 
pytest-mock을 사용해서 requests를 모킹하고, 
성공 케이스와 실패 케이스를 모두 테스트해줘
```

**생성된 테스트:**
```python
import pytest
from unittest.mock import Mock
import requests

def test_fetch_user_data_success(mocker):
    """API 호출 성공 시나리오"""
    # Arrange
    user_id = "user123"
    mock_response = Mock()
    mock_response.json.return_value = {
        "id": user_id,
        "name": "홍길동",
        "email": "hong@example.com"
    }
    mock_response.status_code = 200
    
    mock_get = mocker.patch('requests.get', return_value=mock_response)
    
    # Act
    result = fetch_user_data(user_id)
    
    # Assert
    assert result["id"] == user_id
    assert result["name"] == "홍길동"
    mock_get.assert_called_once_with(f"https://api.example.com/users/{user_id}")

def test_fetch_user_data_http_error(mocker):
    """API 호출 실패 시나리오"""
    # Arrange
    user_id = "user123"
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.HTTPError("404 Not Found")
    
    mocker.patch('requests.get', return_value=mock_response)
    
    # Act & Assert
    with pytest.raises(requests.HTTPError):
        fetch_user_data(user_id)

def test_fetch_user_data_network_error(mocker):
    """네트워크 오류 시나리오"""
    # Arrange
    mocker.patch('requests.get', side_effect=requests.ConnectionError())
    
    # Act & Assert
    with pytest.raises(requests.ConnectionError):
        fetch_user_data("user123")
```

### 파라미터화된 테스트

**Chat 명령:**
```
여러 입력값으로 테스트할 수 있도록 
pytest.mark.parametrize를 사용한 테스트를 작성해줘
```

```python
import pytest

@pytest.mark.parametrize("input_data,expected", [
    ([1, 2, 3], 2.0),
    ([10, 20, 30], 20.0),
    ([0, 0, 0], 0.0),
    ([-5, 0, 5], 0.0),
    ([100], 100.0),
])
def test_calculate_average_parametrized(input_data, expected):
    """여러 입력 데이터로 평균 계산 검증"""
    result = calculate_average(input_data)
    assert result == expected

@pytest.mark.parametrize("invalid_input", [
    [],
    None,
])
def test_calculate_average_invalid_input(invalid_input):
    """유효하지 않은 입력 처리 검증"""
    with pytest.raises((ValueError, TypeError)):
        calculate_average(invalid_input)
```

## 문서화

Python 함수와 클래스에 대한 docstring을 자동 생성합니다.

### Docstring 자동 생성

**원본 함수:**
```python
def process_order(order_id, user_id, items, discount=0.0):
    total = sum(item['price'] * item['quantity'] for item in items)
    discounted_total = total * (1 - discount)
    return {
        'order_id': order_id,
        'user_id': user_id,
        'total': discounted_total,
        'items': items
    }
```

**Chat 명령:**
```
이 함수에 Google 스타일의 docstring을 추가하고, 
타입 힌트도 함께 추가해줘
```

**문서화된 코드:**
```python
from typing import List, Dict, Any

def process_order(
    order_id: str, 
    user_id: str, 
    items: List[Dict[str, Any]], 
    discount: float = 0.0
) -> Dict[str, Any]:
    """
    주문을 처리하고 할인이 적용된 총액을 계산합니다.
    
    이 함수는 주문 항목들의 가격을 합산하고 할인율을 적용하여
    최종 주문 정보를 생성합니다.
    
    Args:
        order_id: 주문 고유 식별자
        user_id: 사용자 고유 식별자
        items: 주문 항목 리스트. 각 항목은 'price'와 'quantity' 키를 포함해야 함
        discount: 할인율 (0.0 ~ 1.0). 기본값은 0.0 (할인 없음)
    
    Returns:
        처리된 주문 정보를 담은 딕셔너리:
            - order_id: 주문 ID
            - user_id: 사용자 ID
            - total: 할인이 적용된 최종 금액
            - items: 주문 항목 리스트
    
    Raises:
        ValueError: discount가 0.0 미만이거나 1.0 초과인 경우
        KeyError: items의 요소에 'price' 또는 'quantity' 키가 없는 경우
    
    Examples:
        >>> items = [
        ...     {'name': '상품A', 'price': 10000, 'quantity': 2},
        ...     {'name': '상품B', 'price': 5000, 'quantity': 1}
        ... ]
        >>> result = process_order('ORD-001', 'USER-123', items, discount=0.1)
        >>> result['total']
        22500.0
    
    Note:
        할인율은 0.0(할인 없음)부터 1.0(100% 할인)까지의 값을 가질 수 있습니다.
    """
    if not 0.0 <= discount <= 1.0:
        raise ValueError("할인율은 0.0과 1.0 사이여야 합니다")
    
    total = sum(item['price'] * item['quantity'] for item in items)
    discounted_total = total * (1 - discount)
    
    return {
        'order_id': order_id,
        'user_id': user_id,
        'total': discounted_total,
        'items': items
    }
```

### 클래스 문서화

**Chat 명령:**
```
이 클래스에 상세한 docstring을 추가해줘. 
클래스 설명, 속성, 메서드 모두 문서화해줘
```

```python
from typing import Optional, List
from datetime import datetime

class OrderManager:
    """
    주문 관리를 담당하는 클래스입니다.
    
    이 클래스는 주문 생성, 조회, 업데이트, 취소 등의 
    주문 관련 모든 비즈니스 로직을 처리합니다.
    
    Attributes:
        db_connection: 데이터베이스 연결 객체
        logger: 로깅 객체
        cache: 주문 캐시 저장소
    
    Examples:
        >>> manager = OrderManager(db_connection)
        >>> order = manager.create_order('USER-123', items)
        >>> manager.get_order(order['order_id'])
    """
    
    def __init__(self, db_connection, logger=None):
        """
        OrderManager 인스턴스를 초기화합니다.
        
        Args:
            db_connection: 데이터베이스 연결 객체
            logger: 로깅 객체 (선택). 제공되지 않으면 기본 로거 사용
        """
        self.db_connection = db_connection
        self.logger = logger or self._setup_default_logger()
        self.cache = {}
    
    def create_order(
        self, 
        user_id: str, 
        items: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        새로운 주문을 생성합니다.
        
        Args:
            user_id: 주문을 생성하는 사용자 ID
            items: 주문할 상품 리스트
        
        Returns:
            생성된 주문 정보
        
        Raises:
            ValueError: 잘못된 사용자 ID 또는 빈 상품 리스트
            DatabaseError: 데이터베이스 저장 실패
        """
        pass
    
    def get_order(self, order_id: str) -> Optional[Dict[str, Any]]:
        """
        주문 ID로 주문 정보를 조회합니다.
        
        먼저 캐시를 확인하고, 캐시에 없으면 데이터베이스에서 조회합니다.
        
        Args:
            order_id: 조회할 주문 ID
        
        Returns:
            주문 정보. 존재하지 않으면 None
        """
        pass
```

## 타입 힌트 추가

**Chat 명령:**
```
이 Python 코드에 완전한 타입 힌트를 추가해줘. 
from __future__ import annotations도 사용해줘
```

**타입 힌트 추가 전:**
```python
def get_user_orders(user_id, status=None, limit=10):
    orders = fetch_orders(user_id)
    if status:
        orders = [o for o in orders if o['status'] == status]
    return orders[:limit]
```

**타입 힌트 추가 후:**
```python
from __future__ import annotations
from typing import Optional, List, Dict, Any, Literal

OrderStatus = Literal['pending', 'processing', 'completed', 'cancelled']

def get_user_orders(
    user_id: str,
    status: Optional[OrderStatus] = None,
    limit: int = 10
) -> List[Dict[str, Any]]:
    """
    사용자의 주문 목록을 조회합니다.
    
    Args:
        user_id: 사용자 ID
        status: 필터링할 주문 상태 (선택)
        limit: 반환할 최대 주문 수
    
    Returns:
        주문 정보 리스트
    """
    orders: List[Dict[str, Any]] = fetch_orders(user_id)
    
    if status:
        orders = [order for order in orders if order['status'] == status]
    
    return orders[:limit]
```

## 보안 취약점 수정

**Chat 명령:**
```
이 코드의 보안 취약점을 찾아서 수정해줘
```

**취약한 코드:**
```python
def execute_query(user_input):
    query = f"SELECT * FROM users WHERE name = '{user_input}'"
    return db.execute(query)
```

**수정된 코드:**
```python
from typing import List, Dict, Any

def execute_query(user_input: str) -> List[Dict[str, Any]]:
    """
    사용자 이름으로 사용자 정보를 조회합니다.
    
    Args:
        user_input: 검색할 사용자 이름
    
    Returns:
        조회된 사용자 정보 리스트
    
    Note:
        SQL 인젝션 방지를 위해 파라미터화된 쿼리를 사용합니다.
    """
    # 파라미터화된 쿼리 사용 (SQL 인젝션 방지)
    query = "SELECT * FROM users WHERE name = ?"
    return db.execute(query, (user_input,))
```

## 실습 과제

1. **코드 리팩토링 실습**
   - `playground/lab1.py` 파일의 복잡한 함수를 여러 개의 작은 함수로 분리해보세요
   - PEP 8 스타일 가이드를 준수하도록 코드를 개선하세요

2. **테스트 코드 생성 실습**
   - 작성한 함수에 대해 pytest 테스트 케이스를 생성하세요
   - 정상 케이스, 경계 케이스, 예외 케이스를 모두 포함하세요

3. **문서화 실습**
   - 모든 함수에 Google 스타일 docstring을 추가하세요
   - 타입 힌트를 완전하게 추가하세요

4. **보안 강화 실습**
   - 코드에서 보안 취약점을 찾아 수정하세요
   - 입력 검증 로직을 추가하세요

## 다음 단계

고급 기능 활용법을 익혔다면 이제 [실제 프로젝트 적용](./09-real-project.md)에서 실무에 적용하는 방법을 학습해보세요.

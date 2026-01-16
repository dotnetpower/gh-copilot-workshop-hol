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

## 📋 사전 준비 (Prerequisites)

실습을 시작하기 전에 다음 환경을 구성해야 합니다.

### 1. Python 환경 설정

Python 3.8 이상이 필요합니다. 다음 명령으로 설치 여부를 확인하세요:

```bash
python --version
# 또는
python3 --version
```

:::info 💡 Python 설치
Python이 설치되어 있지 않다면 [공식 웹사이트](https://www.python.org/downloads/)에서 다운로드하여 설치하세요.
- Windows: 설치 시 "Add Python to PATH" 옵션을 반드시 체크하세요
- macOS: Homebrew 사용 권장 (`brew install python3`)
- Linux: 패키지 관리자 사용 (`sudo apt install python3` 또는 `sudo yum install python3`)
:::

### 2. 가상환경 생성 (권장)

프로젝트별로 독립된 Python 환경을 사용하는 것이 좋습니다:

```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화
# Linux/macOS:
source venv/bin/activate

# Windows (Command Prompt):
venv\Scripts\activate

# Windows (PowerShell):
venv\Scripts\Activate.ps1
```

:::tip 가상환경 활성화 확인
가상환경이 활성화되면 터미널 프롬프트 앞에 `(venv)`가 표시됩니다.
:::

### 3. 필수 패키지 설치

실습에 필요한 Python 패키지들을 설치합니다:

```bash
pip install requests aiofiles pytest
```

:::note 패키지 설명
- **requests**: HTTP 요청을 위한 라이브러리 (API 호출 실습용)
- **aiofiles**: 비동기 파일 I/O 작업을 위한 라이브러리
- **pytest**: Python 테스트 프레임워크
:::

### 4. 작업 디렉토리 구성

실습을 진행할 디렉토리를 생성합니다:

```bash
# 프로젝트 루트에서
mkdir -p playground
cd playground
```

### 5. GitHub Copilot 활성화

VS Code에서 다음을 확인하세요:

1. **GitHub Copilot 확장 설치**
   - VS Code 확장 마켓플레이스에서 "GitHub Copilot" 검색 및 설치
   - 재시작 후 자동으로 활성화됨

2. **GitHub 계정 로그인**
   - VS Code 우측 하단의 계정 아이콘 클릭
   - "Sign in to use GitHub Copilot" 선택
   - GitHub 계정으로 로그인

3. **Copilot 상태 확인**
   - VS Code 우측 하단에 Copilot 아이콘 확인
   - 아이콘이 활성화(파란색)되어 있어야 함

:::warning ⚠️ Copilot 구독 필요
GitHub Copilot을 사용하려면 유료 구독 또는 무료 평가판이 필요합니다. [GitHub Copilot 구독 페이지](https://github.com/features/copilot)에서 신청하세요.
:::

### 6. 실습 환경 검증

모든 설정이 완료되었는지 확인합니다:

```bash
# Python 버전 확인
python --version

# 설치된 패키지 확인
pip list | grep -E "requests|aiofiles|pytest"

# 작업 디렉토리 확인
pwd  # playground 디렉토리에 있어야 함
```

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
```python
# 함수명과 주석만 작성하면 Copilot이 구현체를 제안합니다
def calculateTax(price, taxRate):
  # 세금을 계산하는 함수
  

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
```python
# 배열에서 최대값을 찾는 함수
def find_max(arr):
    # Copilot이 구현체를 제안합니다
    pass
```

### 1.6 데이터 클래스 정의
```python
from dataclasses import dataclass
from datetime import datetime
from typing import List

# 데이터 클래스 정의 후 서비스 클래스를 작성하면 자동완성 제안
@dataclass
class User:
    id: str
    name: str
    email: str
    created_at: datetime

class UserService:
    # Copilot이 CRUD 메서드들을 제안합니다
    pass
```

### 1.7 API 호출 패턴
```python
import requests

# REST API 호출 함수 - 주석과 함수명으로 구현체 유도
def fetch_user_data(user_id: str):
    """사용자 ID로 API에서 사용자 정보를 가져옵니다"""
    # Copilot이 requests를 사용한 GET 요청을 제안합니다
    

def create_user(name: str, email: str):
    """새 사용자를 생성하는 POST 요청"""
    # Copilot이 POST 요청 구현을 제안합니다
```

### 1.8 데이터 변환 및 처리
```python
from dataclasses import dataclass
from typing import List, Dict
from decimal import Decimal
from itertools import groupby

# Python을 사용한 데이터 처리
@dataclass
class Product:
    id: int
    name: str
    price: Decimal
    category: str

class ProductService:
    # 카테고리별로 제품을 그룹화하는 메서드
    def group_products_by_category(self, products: List[Product]) -> Dict[str, List[Product]]:
        # Copilot이 groupby를 사용한 그룹화 로직을 제안합니다
        pass
    
    # 가격 범위로 제품 필터링
    def filter_by_price_range(self, products: List[Product], min_price: Decimal, max_price: Decimal) -> List[Product]:
        # Copilot이 필터링 로직을 제안합니다
        pass
```

### 1.9 에러 처리 패턴
```python
import asyncio
from typing import Optional, Any

# 에러 처리가 포함된 비동기 함수
async def fetch_data_with_retry(url: str, max_retries: int = 3) -> Optional[Any]:
    """URL에서 데이터를 가져오고, 실패 시 재시도하는 함수"""
    # Copilot이 try-except와 재시도 로직을 제안합니다
    pass
```

### 1.10 테스트 코드 생성
```python
import pytest

# 함수 작성 후 테스트 함수명을 입력하면 자동으로 테스트 케이스 제안
def calculate_discount(price, discount_percent):
    """가격에 할인율을 적용한 최종 가격을 계산합니다"""
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("할인율은 0-100 사이여야 합니다")
    return price * (1 - discount_percent / 100)

# 테스트 함수 - Copilot이 다양한 테스트 케이스를 제안합니다
def test_calculate_discount():
    
```

### 1.11 환경 변수 및 설정 관리
```python
import os
from typing import Optional

# 설정 클래스 - 환경 변수를 안전하게 로드
class Config:
    """애플리케이션 설정을 관리하는 클래스"""
    # Copilot이 환경 변수 로드 패턴을 제안합니다
    
```

### 1.12 정규표현식 패턴
```python
import re

# 이메일 유효성 검증 함수
def is_valid_email(email: str) -> bool:
    """이메일 형식을 검증하는 정규표현식"""
    # Copilot이 적절한 regex 패턴을 제안합니다
    pass

# 전화번호 포맷팅 함수 (예: 01012345678 -> 010-1234-5678)
def format_phone_number(phone: str) -> str:
    """전화번호 포맷팅"""
    # Copilot이 포맷팅 로직을 제안합니다
    pass
```

### 1.13 클래스와 상속 패턴
```python
from abc import ABC, abstractmethod
from datetime import datetime

# 추상 클래스 정의
class PaymentMethod(ABC):
    """결제 수단 추상 클래스"""
    
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        """결제를 처리하는 추상 메서드"""
        pass

# Copilot이 구현 클래스들을 제안합니다
class CreditCardPayment(PaymentMethod):
    
```

### 1.14 파일 I/O 작업
```python
import json
import aiofiles
from typing import Any, Dict
from pathlib import Path

# JSON 파일 읽기/쓰기 유틸리티
async def read_json_file(file_path: Path) -> Dict[str, Any]:
    """JSON 파일을 읽어서 딕셔너리로 반환"""
    # Copilot이 에러 처리를 포함한 구현을 제안합니다
    pass

async def write_json_file(file_path: Path, data: Dict[str, Any]) -> None:
    """딕셔너리를 JSON 파일로 저장"""
    pass
```

:::tip 💡 Copilot 활용 팁
- **명확한 함수/변수명 사용**: 의도가 명확할수록 정확한 제안을 받을 수 있습니다
- **주석으로 컨텍스트 제공**: 복잡한 로직은 주석으로 설명하면 더 정확한 제안을 받습니다
- **타입 정의 활용**: Python의 타입 힌트를 사용하면 더 정확한 코드를 생성합니다
- **패턴 학습 활용**: 비슷한 코드 몇 개를 작성하면 패턴을 인식하여 나머지를 자동완성합니다
:::

:::note ✅ 실습 과제
1. 간단한 계산기 함수 작성 (덧셈, 뺄셈, 곱셈, 나눗셈)
2. 배열 정렬 함수 구현
3. 문자열 처리 유틸리티 함수 작성
4. REST API 호출 함수 작성 (GET, POST)
5. 에러 처리가 포함된 비동기 함수 구현
6. 간단한 클래스 계층 구조 설계 및 구현
7. 유효성 검증 함수 작성 (이메일, 전화번호 등)
8. 테스트 케이스 작성
:::

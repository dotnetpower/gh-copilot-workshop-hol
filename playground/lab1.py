# 실습 1: Code Completion

# 1.3 기본 코드 자동완성
# 함수명과 주석만 작성하면 Copilot이 구현체를 제안합니다
def calculateTax(price, taxRate):
    # 세금을 계산하는 함수
    pass


# 1.4 반복 패턴 학습
# 몇 개의 예시를 작성하면 패턴을 학습하여 나머지를 자동완성합니다
def get_monday():
    return "Monday"

def get_tuesday():
    return "Tuesday"

# Copilot이 나머지 요일 함수들을 자동으로 제안합니다


# 1.5 주석 활용
# 배열에서 최대값을 찾는 함수
def find_max(arr):
    # Copilot이 구현체를 제안합니다
    pass


# 1.6 데이터 클래스 정의
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


# 1.7 API 호출 패턴
import requests

# REST API 호출 함수 - 주석과 함수명으로 구현체 유도
def fetch_user_data(user_id: str):
    """사용자 ID로 API에서 사용자 정보를 가져옵니다"""
    # Copilot이 requests를 사용한 GET 요청을 제안합니다
    pass


def create_user(name: str, email: str):
    """새 사용자를 생성하는 POST 요청"""
    # Copilot이 POST 요청 구현을 제안합니다
    pass


# 1.8 데이터 변환 및 처리
from typing import Dict
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


# 1.9 에러 처리 패턴
import asyncio
from typing import Optional, Any

# 에러 처리가 포함된 비동기 함수
async def fetch_data_with_retry(url: str, max_retries: int = 3) -> Optional[Any]:
    """URL에서 데이터를 가져오고, 실패 시 재시도하는 함수"""
    # Copilot이 try-except와 재시도 로직을 제안합니다
    pass


# 1.10 테스트 코드 생성
import pytest

# 함수 작성 후 테스트 함수명을 입력하면 자동으로 테스트 케이스 제안
def calculate_discount(price, discount_percent):
    """가격에 할인율을 적용한 최종 가격을 계산합니다"""
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("할인율은 0-100 사이여야 합니다")
    return price * (1 - discount_percent / 100)

# 테스트 함수 - Copilot이 다양한 테스트 케이스를 제안합니다
def test_calculate_discount():
    pass


# 1.11 환경 변수 및 설정 관리
import os

# 설정 클래스 - 환경 변수를 안전하게 로드
class Config:
    """애플리케이션 설정을 관리하는 클래스"""
    # Copilot이 환경 변수 로드 패턴을 제안합니다
    pass


# 1.12 정규표현식 패턴
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


# 1.13 클래스와 상속 패턴
from abc import ABC, abstractmethod

# 추상 클래스 정의
class PaymentMethod(ABC):
    """결제 수단 추상 클래스"""
    
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        """결제를 처리하는 추상 메서드"""
        pass

# Copilot이 구현 클래스들을 제안합니다
class CreditCardPayment(PaymentMethod):
    pass


# 1.14 파일 I/O 작업
import json
import aiofiles
from pathlib import Path

# JSON 파일 읽기/쓰기 유틸리티
async def read_json_file(file_path: Path) -> Dict[str, Any]:
    """JSON 파일을 읽어서 딕셔너리로 반환"""
    # Copilot이 에러 처리를 포함한 구현을 제안합니다
    pass

async def write_json_file(file_path: Path, data: Dict[str, Any]) -> None:
    """딕셔너리를 JSON 파일로 저장"""
    pass

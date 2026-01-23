---
sidebar_position: 70
title: '[Hackathon] 항공편 지연 예측'
description: GitHub Copilot을 활용한 머신러닝 기반 항공편 지연 예측 해커톤
---

# 실습 7: 해커톤 - 항공편 지연 예측

:::tip 🎯 학습 목표
- GitHub Copilot을 활용한 실전 머신러닝 프로젝트 경험
- 데이터 분석부터 모델 배포까지 전체 파이프라인 구축
- Copilot을 페어 프로그래머로 활용하는 방법 습득
- 창의적 문제 해결과 빠른 프로토타이핑 능력 향상
:::

## 📋 해커톤 개요

### 🎯 프로젝트 목표

[미국 교통부(FAA)의 2013년 항공편 데이터](/assets/data/flights.csv)를 활용하여, **특정 요일과 도착 공항을 기준으로 항공편이 15분 이상 지연될 확률을 예측**하는 애플리케이션을 만듭니다.

### 🏆 해커톤 시나리오

**배경**: 
여러분은 항공사의 데이터 팀에 합류했습니다. 항공편 지연은 고객 불만의 주요 원인이며, 사전 예측을 통해 다음과 같은 가치를 제공할 수 있습니다:
- 승객에게 사전 알림으로 만족도 향상
- 대체 편 사전 준비
- 운영 효율성 증대

**목표**:
1. **데이터 분석**: 항공편 지연 패턴 파악
2. **모델 구축**: 요일과 공항별 지연 예측 모델 개발
3. **API 개발**: 예측 결과를 제공하는 REST API 구축
4. **UI 구축**: 사용자가 쉽게 활용할 수 있는 대시보드 제작

### ⏰ 해커톤 일정

| 시간 | 활동 | 목표 |
|------|------|------|
| 00:00 - 00:20 | 킥오프 & 환경 설정 | 프로젝트 이해 및 개발 환경 구축 |
| 00:20 - 01:30 | 데이터 탐색 & 모델링 | EDA, 모델 학습, 모델 저장 |
| 01:30 - 02:40 | Streamlit 앱 개발 | 대시보드 구축 및 모델 통합 |
| 02:40 - 03:00 | 발표 & 회고 | 결과 발표 및 학습 내용 공유 |

:::tip 💡 유연한 구조
이 해커톤은 **Streamlit 중심**으로 설계되었습니다. Streamlit만으로 모델을 직접 로드하고 예측할 수 있어 별도의 API 서버가 필요 없습니다. 하지만 백엔드를 분리하고 싶다면 Flask API를 추가로 구현할 수 있습니다.
:::

## 🛠 사전 준비 (Prerequisites)

### 1. 개발 환경 설정

#### uv 설치

[uv](https://github.com/astral-sh/uv)는 빠르고 현대적인 Python 패키지 및 프로젝트 관리자입니다.

```bash
# Linux/macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# 또는 pip로 설치
pip install uv
```

#### Python 버전 설정 및 가상환경 생성

```bash
# Python 3.11 설치 및 프로젝트 초기화
uv python install 3.11
uv init

# .venv 가상환경 생성 (Python 3.11 사용)
uv venv --python 3.11

# 가상환경 활성화
# Linux/macOS:
source .venv/bin/activate

# Windows:
.venv\Scripts\activate
```

:::info 💡 uv의 장점
- ⚡ **초고속**: pip보다 10-100배 빠른 패키지 설치
- 🔒 **자동 잠금**: pyproject.toml과 uv.lock으로 의존성 고정
- 🐍 **Python 버전 관리**: 여러 Python 버전 자동 설치 및 관리
- 📦 **단순함**: 하나의 도구로 모든 것 관리
:::

#### 필수 패키지 설치

프로젝트에 필요한 주요 패키지를 uv로 설치합니다:

```bash
# 기본 패키지 설치 (Streamlit 중심)
uv add pandas numpy scikit-learn matplotlib seaborn streamlit jupyter

# 선택사항: Flask API 구현 시
uv add flask flask-cors
```

또는 `pyproject.toml` 파일을 직접 작성할 수도 있습니다:

```toml
[project]
name = "flight-delay-prediction"
version = "0.1.0"
description = "Flight delay prediction hackathon"
requires-python = ">=3.11"
dependencies = [
    "pandas",
    "numpy",
    "scikit-learn",
    "matplotlib",
    "seaborn",
    "streamlit",
    "jupyter",
]

[project.optional-dependencies]
api = [
    "flask",
    "flask-cors",
]
```

그 후 설치:

```bash
# 기본 패키지 설치
uv sync

# Flask API 포함 설치
uv sync --extra api
```

:::info 💡 두 가지 접근 방식

**Option 1: Streamlit Only (권장)**
- Streamlit 앱에서 직접 모델 로드
- 빠른 프로토타이핑
- 단일 Python 프로세스

**Option 2: Flask API + Streamlit**
- 백엔드/프론트엔드 분리
- RESTful API 설계 경험
- 확장 가능한 구조

해커톤에서는 **Option 1**을 권장합니다!
:::

### 2. 데이터셋 이해

이 프로젝트는 **미국 교통부의 2013년 항공편 데이터**(flights.csv)를 사용합니다.

:::note 📊 데이터셋 스키마

| 컬럼명 | 설명 | 예시 |
|--------|------|------|
| Year | 연도 | 2013 |
| Month | 월 | 9 |
| DayofMonth | 일 | 16 |
| DayOfWeek | 요일 (1=월요일, 7=일요일) | 1 |
| Carrier | 항공사 코드 | DL, AS, WN |
| OriginAirportID | 출발 공항 ID | 15304 |
| OriginAirportName | 출발 공항명 | Tampa International |
| OriginCity | 출발 도시 | Tampa |
| OriginState | 출발 주 | FL |
| DestAirportID | 도착 공항 ID | 12478 |
| DestAirportName | 도착 공항명 | John F. Kennedy International |
| DestCity | 도착 도시 | New York |
| DestState | 도착 주 | NY |
| CRSDepTime | 예정 출발 시간 | 1539 |
| DepDelay | 출발 지연 시간(분) | 4 |
| DepDel15 | 15분 이상 출발 지연 여부 | 0 또는 1 |
| CRSArrTime | 예정 도착 시간 | 1824 |
| ArrDelay | 도착 지연 시간(분) | 13 |
| ArrDel15 | 15분 이상 도착 지연 여부 | 0 또는 1 |
| Cancelled | 취소 여부 | 0 또는 1 |

**목표 변수**: `ArrDel15` (15분 이상 도착 지연 여부)
:::

### 3. 프로젝트 구조

```bash
flight-delay-hackathon/
├── .venv/               # uv가 생성한 가상환경
├── data/
│   ├── flights.csv      # 원본 데이터
│   ├── airports.csv     # 공항 목록 (생성 예정)
│   └── model.pkl        # 저장된 모델 (생성 예정)
├── notebooks/
│   └── flight_analysis.ipynb  # 데이터 분석 및 모델링
├── app.py              # Streamlit 앱 (메인)
├── pyproject.toml      # uv 프로젝트 설정
├── uv.lock             # uv 의존성 잠금 파일
└── README.md

# 선택사항: Flask API 사용 시
├── server/
│   └── app.py          # Flask API
└── client/
    └── dashboard.py    # Streamlit UI
```

:::tip 💡 프로젝트 구조는 유연하게!
위 구조는 제안일 뿐입니다. **Streamlit만 사용한다면** 루트에 `app.py` 하나만 있어도 충분합니다. 여러분의 스타일에 맞게 자유롭게 구성하세요!
:::

## 📊 Phase 1: 데이터 탐색 및 모델링

### 1.1 Jupyter Notebook 생성 및 실행

#### VS Code에서 Notebook 실행 (권장)

VS Code에서 Jupyter Notebook을 직접 실행할 수 있습니다:

1. **Jupyter 확장 설치**
   - VS Code에서 `Ctrl+Shift+X` (또는 `Cmd+Shift+X`)
   - "Jupyter" 검색 후 설치 (Microsoft 제공)
   - "Python" 확장도 함께 설치

2. **Notebook 파일 생성**
   ```bash
   # 프로젝트에 notebooks 폴더 생성
   mkdir -p notebooks
   ```
   - VS Code에서 `notebooks/flight_analysis.ipynb` 파일 생성
   - 또는 Command Palette (`Ctrl+Shift+P`)에서 "Create: New Jupyter Notebook" 선택

3. **Kernel 선택**
   - Notebook 파일 열기
   - 우측 상단의 "Select Kernel" 클릭
   - ".venv (Python 3.11)" 선택
   - 또는 "Python Environments..." → `.venv/bin/python` 선택

4. **코드 실행**
   - 셀 선택 후 `Shift+Enter`: 실행 후 다음 셀로
   - `Ctrl+Enter`: 현재 셀만 실행
   - `Alt+Enter`: 실행 후 아래에 새 셀 추가

:::tip 💡 VS Code Notebook의 장점
- 별도의 브라우저 탭 불필요
- IntelliSense 및 자동완성 지원
- Git 통합 및 버전 관리 용이
- GitHub Copilot과 완벽한 통합
:::

#### 터미널에서 Jupyter Lab 실행 (선택사항)

브라우저에서 실행하고 싶다면:

```bash
# Jupyter Lab 실행
uv run jupyter lab

# 또는 Jupyter Notebook
uv run jupyter notebook
```

브라우저에서 `http://localhost:8888`로 자동 열립니다.

### 1.2 Notebook 시작하기

첫 번째 셀에 다음 코드를 입력하세요:

```python
# Flights Data Exploration Challenge
# 이 노트북에서는 FAA 항공편 데이터를 탐색하고 모델을 개발합니다.
# Using pandas for data manipulation
# Using scikit-learn for machine learning
# Model predicts flight delays based on day of week and destination airport

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 로드
# TODO: GitHub Copilot에게 "flights.csv 파일을 로드하고 기본 정보를 표시해줘" 요청
```

:::tip 🤖 Copilot 활용
주석에 "탐색적 데이터 분석", "show first 100 rows", "결측치 확인" 같은 구체적인 명령어를 사용하면 Copilot이 자동으로 코드를 생성합니다.
:::

### 1.3 데이터 정제 (Data Cleaning)

```python
# 결측치 확인
# TODO: Copilot에게 "모든 컬럼의 결측치를 확인해줘" 요청

# DepDel15가 null인 경우 0으로 채우기
# TODO: Copilot이 fillna() 함수를 제안할 것입니다
```

### 1.4 데이터 시각화

```python
# 공항별 지연 패턴 분석
# TODO: Copilot에게 "도착 공항별 지연 건수를 바 차트로 그려줘" 요청

# 요일별 지연 패턴
# TODO: "요일별 평균 지연 시간을 선 그래프로 그려줘"
```

### 1.5 모델 학습

**목표**: 요일(DayOfWeek)과 도착 공항(DestAirportID)을 기반으로 15분 이상 지연 확률 예측

```python
# Logistic Regression 모델 생성
# TODO: Copilot에게 "로지스틱 회귀 모델을 만들고 학습해줘" 요청

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# 특성과 타겟 변수 선택
X = df_flights[['DayOfWeek', 'DestAirportID']]
y = df_flights['ArrDel15']

# 데이터 분할
# TODO: Copilot이 train_test_split 사용을 제안할 것입니다

# 모델 학습
# TODO: Copilot이 model.fit() 코드를 생성할 것입니다

# 모델 평가
# TODO: accuracy_score, confusion_matrix 등 평가 지표
```

:::info 📊 모델 평가
Logistic Regression은 간단하면서도 효과적인 베이스라인 모델입니다. 시간이 허락하다면 Random Forest나 XGBoost 같은 모델도 시도해보세요!
:::

### 1.5 모델 저장 (pickle)

```python
# 모델을 pickle로 저장하여 나중에 API에서 사용
import pickle

# TODO: Copilot에게 "pickle로 모델을 파일에 저장해줘" 요청
# pickle.dump(model, open('data/model.pkl', 'wb'))
```

### 1.6 공항 목록 CSV 생성

```python
# 고유한 공항 ID와 이름 추출
# TODO: "OriginAirportID와 OriginAirportName의 고유값을 CSV로 저장해줘"
# df_flights[['OriginAirportID', 'OriginAirportName']].drop_duplicates().to_csv('data/airports.csv', index=False)
```

:::success ✅ Phase 1 체크포인트
- [ ] 데이터 로드 및 탐색 완료
- [ ] 결측치 처리 완료
- [ ] 모델 학습 및 평가 완료
- [ ] model.pkl 파일 생성
- [ ] airports.csv 파일 생성
:::

## 📈 Phase 2: Streamlit 대시보드 개발

### 2.1 대시보드 기본 구조

`app.py` (또는 `dashboard.py`) 파일을 생성합니다:

```python
# Streamlit dashboard for flight delay prediction
# Loads model directly from pickle file
# Shows prediction results with user-friendly interface

import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="항공편 지연 예측", page_icon="✈️")

# TODO: Copilot에게 "pickle 파일에서 모델을 로드해줘" 요청
# TODO: "airports.csv 파일을 로드해줘" 요청
```

:::tip 💡 Streamlit의 장점
Streamlit은 모델을 직접 로드하고 예측할 수 있어 별도의 API 서버가 필요 없습니다. 빠른 프로토타이핑에 최적화되어 있습니다!
:::

### 2.2 UI 레이아웃 구성

```python
st.title("✈️ 항공편 지연 예측 시스템")
st.write("요일과 도착 공항을 선택하면 15분 이상 지연될 확률을 알려드립니다.")

# 사이드바 또는 메인 영역에 입력 필드 구성
# TODO: Copilot에게 다음을 요청:
# "요일 선택 selectbox를 만들어줘 (월요일=1, 일요일=7)"
# "공항 선택 selectbox를 만들어줘 (airports 데이터프레임 사용)"
```

### 2.3 예측 로직 구현

```python
if st.button("예측하기", type="primary"):
    # TODO: "선택된 요일과 공항 ID로 모델 예측을 수행해줘"
    # TODO: "predict_proba()를 사용해서 확률을 계산해줘"
    # TODO: "결과를 st.metric()과 st.progress()로 표시해줘"
    pass
```

### 2.4 대시보드 실행

```bash
# uv로 Streamlit 실행
uv run streamlit run app.py

# 또는 파일명이 다른 경우
uv run streamlit run dashboard.py
```

브라우저에서 자동으로 열리지 않으면 `http://localhost:8501` 로 접속하세요.

:::success ✅ Phase 2 체크포인트
- [ ] Streamlit 앱 기본 구조 완료
- [ ] 모델과 데이터 로드 완료
- [ ] 사용자 입력 UI 구현
- [ ] 예측 로직 구현
- [ ] 결과 시각화 완료
:::

## 🎨 추가 기능 (선택사항)

### 데이터 시각화 추가

```python
# 요일별/공항별 지연 통계 차트
# TODO: "flights 데이터로 요일별 지연 비율을 막대 그래프로 그려줘"
# TODO: "상위 10개 공항의 지연 통계를 보여줘"
```

### 여러 항공편 비교

```python
# 여러 공항을 동시에 비교하는 기능
# TODO: "multiselect로 여러 공항을 선택할 수 있게 해줘"
```

## 🔧 선택사항: Flask API로 백엔드 분리

백엔드와 프론트엔드를 분리하고 싶다면 Flask API를 만들 수 있습니다.

### Flask API 구현

먼저 Flask 패키지를 추가합니다:

```bash
# Flask 관련 패키지 추가
uv add flask flask-cors
```

`server/app.py` 파일 생성:

```python
# Create a base Flask server
# Using Flask for API
# Load model from pickle file
# Model takes two parameters - day of week and airport id
# Returns prediction of flight delay probability

import pickle
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Streamlit에서 접근 가능하도록

# TODO: "pickle 파일에서 모델을 로드해줘"

@app.route('/predict', methods=['GET'])
def predict():
    # TODO: "day_of_week와 airport_id 파라미터를 받아서 예측해줘"
    pass

@app.route('/airports', methods=['GET'])
def airports():
    # TODO: "airports.csv를 읽어서 JSON으로 반환해줘"
    pass

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

### Flask 서버 실행

```bash
# Flask 서버 실행
cd server
uv run python app.py

# 또는 프로젝트 루트에서
uv run python server/app.py
```

```python
# Create a base Flask server
# Using Flask for API
# Load model from pickle file
# Model takes two parameters - day of week and airport id
# Returns prediction of flight delay probability

import pickle
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Streamlit에서 접근 가능하도록

# TODO: "pickle 파일에서 모델을 로드해줘"

@app.route('/predict', methods=['GET'])
def predict():
    # TODO: "day_of_week와 airport_id 파라미터를 받아서 예측해줘"
    pass

@app.route('/airports', methods=['GET'])
def airports():
    # TODO: "airports.csv를 읽어서 JSON으로 반환해줘"
    pass

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

### Streamlit에서 API 호출

```python
import requests

response = requests.get(f"http://localhost:5000/predict?day_of_week={day}&airport_id={airport_id}")
result = response.json()
```

:::info 📌 언제 Flask API를 사용할까?
- 여러 클라이언트(웹, 모바일)에서 접근할 때
- 모델 업데이트를 서버에서 독립적으로 할 때
- 부하 분산이 필요할 때
- RESTful API 설계 경험을 쌓고 싶을 때

그 외의 경우 Streamlit만으로 충분합니다!
:::

## 🏅 평가 기준

해커톤 프로젝트는 다음 기준으로 평가됩니다:

| 항목 | 배점 | 설명 |
|------|------|------|
| 모델 정확도 | 30% | 예측 정확도 및 신뢰도 |
| API 구현 | 25% | 안정성, 에러 처리, 문서화 |
| UI/UX | 20% | 사용성, 디자인, 직관성 |
| 코드 품질 | 15% | 가독성, 주석, 구조화 |
| 창의성 | 10% | 추가 기능, 독창적 아이디어 |

## 💡 GitHub Copilot 활용 꿀팁

### 🎯 상황별 Copilot 활용법

**1. 막힌 부분이 있을 때**
```python
# 방법 1: 구체적인 주석으로 요청
# "다음 작업을 수행하는 함수를 작성해줘:
# 1. API에서 데이터 가져오기
# 2. 에러 처리하기
# 3. 결과를 DataFrame으로 반환하기"

# 방법 2: Copilot Chat 사용
# Cmd/Ctrl + I 를 누르고 "이 코드가 왜 작동하지 않는지 설명해줘" 요청
```

**2. 에러가 발생했을 때**
```python
# 에러 메시지를 복사한 후 Copilot Chat에서:
# "/fix 이 에러를 해결해줘: [에러 메시지]"
```

**3. 코드를 개선하고 싶을 때**
```python
# 코드를 선택한 후:
# "/optimize 이 코드의 성능을 개선해줘"
# "/refactor 이 코드를 더 읽기 쉽게 리팩토링해줘"
```

### 🚀 프로젝트 가속화 팁

1. **파일 시작 시 컨텍스트 제공**
   ```python
   # Project: Flight Delay Prediction
   # Purpose: This API serves machine learning predictions
   # Framework: Flask
   # Model: Logistic Regression (saved as pickle)
   ```

2. **TODO 주석 활용**
   ```python
   # TODO: Load model from pickle file
   # TODO: Create /predict endpoint that accepts day_of_week and airport_id
   # TODO: Return JSON with delay probability
   ```

3. **예제 데이터 제공**
   ```python
   # Example request: GET /predict?day_of_week=1&airport_id=12892
   # Example response: {"certainty": 0.96, "delay": 0.04}
   ```

## 🎓 학습 포인트

### 기술적 성장

✅ **데이터 과학 파이프라인**
- EDA(Exploratory Data Analysis)부터 모델 배포까지 전체 프로세스 경험
- Pickle을 사용한 모델 직렬화
- CSV 데이터 처리 및 전처리

✅ **웹 개발**
- Flask로 RESTful API 구축
- CORS 설정 및 에러 처리
- Streamlit으로 빠른 프로토타이핑

✅ **협업 도구**
- Git을 통한 버전 관리
- 모듈화된 프로젝트 구조

### Copilot 마스터하기

✅ **효과적인 프롬프팅**
- 구체적이고 명확한 주석 작성
- 예시 포함하여 컨텍스트 제공
- 단계별로 나누어 요청

✅ **Chat 기능 활용**
- `/explain`: 코드 이해하기
- `/fix`: 에러 디버깅
- `/tests`: 테스트 케이스 생성
- `/doc`: 문서화 자동 생성

✅ **생산성 향상**
- 반복 작업 자동화
- 보일러플레이트 코드 생성
- 라이브러리 사용법 빠르게 학습

## 📚 참고 자료

### 데이터 과학
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [Scikit-learn Tutorial](https://scikit-learn.org/stable/tutorial/index.html)
- [Python Pickle Documentation](https://docs.python.org/3/library/pickle.html)

### 웹 개발
- [Flask Quickstart](https://flask.palletsprojects.com/quickstart/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [RESTful API Design](https://restfulapi.net/)

### GitHub Copilot
- [Copilot Best Practices](https://github.blog/developer-skills/github/how-to-use-github-copilot-in-the-command-line/)
- [Prompt Engineering Guide](https://github.blog/developer-skills/github/how-to-write-better-prompts-for-github-copilot/)

## 🚀 추가 도전 과제

해커톤을 완료했다면 다음 과제에 도전해보세요:

### Level 1: 기능 확장
- [ ] 여러 항공사 비교 기능
- [ ] 과거 데이터 시각화 차트
- [ ] 예측 신뢰도 표시

### Level 2: 성능 개선
- [ ] 다른 ML 모델 시도 (Random Forest, XGBoost)
- [ ] 하이퍼파라미터 튜닝
- [ ] 특성 추가 (시간대, 계절 등)

### Level 3: 프로덕션 준비
- [ ] Docker 컨테이너화
- [ ] 단위 테스트 작성
- [ ] API 문서화 (Swagger)
- [ ] 로깅 및 모니터링

## 💬 회고 및 공유

해커톤을 마무리하며 다음 질문에 답해보세요:

1. **GitHub Copilot을 사용하면서 가장 인상 깊었던 점은?**
2. **Copilot이 가장 도움이 되었던 순간은 언제인가요?**
3. **Copilot 없이 이 프로젝트를 완료했다면 얼마나 걸렸을까요?**
4. **다음 프로젝트에서 Copilot을 어떻게 활용하고 싶나요?**

:::success 🎉 축하합니다!
GitHub Copilot과 함께 완전한 머신러닝 애플리케이션을 만들었습니다! 

이 경험을 바탕으로:
- 실무 프로젝트에 Copilot 적용하기
- 팀원들과 Copilot 활용법 공유하기
- 더 복잡한 ML 프로젝트 도전하기

Copilot은 여러분의 최고의 페어 프로그래머입니다! 🚀
:::

---

**작성일**: 2026년 1월  
**난이도**: ⭐⭐⭐ (중급)  
**예상 소요 시간**: 4-5시간  
**참고 자료**: [GitHub - Flight Delay Hackathon](https://github.com/ps-copilot-sandbox/flight-delay-hackathon)

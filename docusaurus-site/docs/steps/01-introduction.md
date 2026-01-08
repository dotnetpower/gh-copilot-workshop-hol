---
sidebar_position: 1
title: GitHub Copilot 소개
description: AI 기반 코드 작성 도우미 GitHub Copilot의 주요 특징과 기반 기술 소개
---

# GitHub Copilot 소개 및 확장 설치

GitHub Copilot은 개발자들이 코드를 더 빠르게 작성할 수 있도록 도와주는 AI 기반 코드 완성 도구입니다.


## 💡 주요 특징

* **단순 코드 자동완성 이상의 역할**

  Copilot은 소프트웨어 개발 생명주기(SDLC) 전반에 걸쳐 도움을 제공합니다.

  * 코드 에디터 내 실시간 제안 및 채팅 지원
  * github.com 상의 코드 설명 및 문서 검색
  * 보안 취약점 탐지 및 안전한 코딩 가이드 제안

  :::info 관련 문서
  [Found Means Fixed (GitHub Blog)](https://github.blog/news-insights/product-news/found-means-fixed-introducing-code-scanning-autofix-powered-by-github-copilot-and-codeql/)
  :::

* **AI 기반 코드 제안**
  모든 제안은 AI가 실시간으로 생성하며, 특정 저장소에서 데이터를 재 활용 하지 않습니다.

* **다양한 언어 지원**
  Python, Java, C#, 심지어 Cobol 등 여러 언어를 지원합니다.


## ⚙️ 기반 기술

GitHub Copilot은 **OpenAI의 대규모 언어 모델(LLM)** 을 기반으로 작동합니다.

* LLM은 방대한 텍스트 데이터를 학습해 **언어 패턴과 문맥을 이해**하고
  **텍스트 생성, 번역, 질의응답** 등의 작업에 특화되어 있습니다.
* Copilot은 특히 **코드 관련 질의응답**에 집중된 모델입니다.



## 소개 영상

<div style={{position: 'relative', paddingBottom: '56.25%', height: 0, overflow: 'hidden'}}>
  <iframe 
    src="https://www.youtube.com/embed/n0NlxUyA7FI" 
    frameBorder="0" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowFullScreen
    style={{position: 'absolute', top: 0, left: 0, width: '100%', height: '100%'}}
  />
</div>

## 추가 리소스

대규모 언어 모델의 개념과 작동 원리를 쉽게 설명하는 영상
<div style={{position: 'relative', paddingBottom: '56.25%', height: 0, overflow: 'hidden'}}>
  <iframe 
    src="https://www.youtube.com/embed/HnvitMTkXro" 
    frameBorder="0" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowFullScreen
    style={{position: 'absolute', top: 0, left: 0, width: '100%', height: '100%'}}
  />
</div>



## 📦 VS Code에서 GitHub Copilot 설치하기

GitHub Copilot을 사용하려면 먼저 Visual Studio Code에 확장을 설치해야 합니다.

### 사전 요구사항

- [Visual Studio Code](https://code.visualstudio.com/) 설치
- GitHub 계정
- GitHub Copilot 구독 (개인, Business, 또는 Enterprise)
  - [GitHub Copilot 무료 체험](https://github.com/github-copilot/signup) 가능

### 설치 단계

#### 1. VS Code 확장 마켓플레이스 열기

VS Code에서 확장 마켓플레이스를 여는 방법:
- **단축키**: `Ctrl+Shift+X` (Windows/Linux) 또는 `Cmd+Shift+X` (Mac)
- 또는 왼쪽 사이드바의 확장 아이콘 (사각형 4개 모양) 클릭

#### 2. GitHub Copilot 확장 검색 및 설치

1. 검색창에 **"GitHub Copilot"** 입력
2. **GitHub Copilot** 확장 찾기 (게시자: GitHub)
3. **Install** 버튼 클릭

#### 3. GitHub Copilot Chat 확장 설치 (권장)

대화형 AI 지원을 위해 추가로 설치:

1. 검색창에 **"GitHub Copilot Chat"** 입력
2. **GitHub Copilot Chat** 확장 찾기 (게시자: GitHub)
3. **Install** 버튼 클릭

:::tip
GitHub Copilot Chat을 사용하면 코드 설명, 버그 수정, 테스트 생성 등을 대화형으로 요청할 수 있습니다.
:::

#### 4. GitHub 계정 인증

확장 설치 후:

1. VS Code 우측 하단에 GitHub Copilot 상태 표시줄이 나타남
2. 상태 표시줄 클릭 또는 명령 팔레트(`Ctrl+Shift+P` / `Cmd+Shift+P`)에서 **"GitHub Copilot: Sign In"** 실행
3. 브라우저가 열리면 GitHub 계정으로 로그인
4. VS Code에 권한 부여 승인

#### 5. 설치 확인

설치가 완료되면:

- VS Code 우측 하단에 GitHub Copilot 아이콘이 표시됨
- 아이콘 색상이 활성화 상태(파란색 또는 흰색)인지 확인
- 새 파일을 만들고 코드를 입력하면 자동 완성 제안이 나타남

:::info 상태 표시 의미
- ✅ **활성화됨**: Copilot이 정상 작동 중
- ⚠️ **비활성화됨**: 현재 파일 유형에서 비활성화됨
- ❌ **오류**: 인증 문제 또는 네트워크 오류
:::

### 빠른 설정 확인

1. 새 Python 또는 JavaScript 파일 생성
2. 주석으로 함수 설명 작성:
   ```python
   # 두 숫자를 더하는 함수
   ```
3. Enter 키를 누르면 Copilot이 함수 코드를 자동으로 제안합니다
4. `Tab` 키를 눌러 제안을 수락

### 추가 설정 (선택사항)

명령 팔레트(`Ctrl+Shift+P` / `Cmd+Shift+P`)에서 **"Preferences: Open Settings (UI)"** 를 열고 "copilot"을 검색하여:

- 자동 완성 활성화/비활성화
- 특정 언어에서만 활성화
- 제안 표시 지연 시간 조정
- 공개 코드 필터링 설정

:::warning 중요
회사나 조직에서 사용하는 경우, IT 정책을 확인하고 필요한 승인을 받으세요.
:::



---
sidebar_position: 1
title: GitHub Copilot 소개
description: AI 기반 코드 작성 도우미 GitHub Copilot의 주요 특징과 기반 기술 소개
---

# GitHub Copilot 소개

GitHub Copilot은 AI 기반의 코드 작성 도우미입니다. OpenAI Codex를 기반으로 하며, 자연어 주석이나 코드 컨텍스트를 이해하여 전체 함수나 코드 라인을 제안합니다.


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

:::note 모델 정보
2025년 10월 기준 GPT-5-(Codex) 모델을 사용할 수 있습니다.
:::



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

## 주요 기능

### 1. 코드 자동완성
- 실시간으로 코드 제안
- 여러 언어 지원

### 2. GitHub Copilot Chat
- 대화형 코드 작성
- 코드 설명 및 문서화

### 3. 코드 리팩토링
- 코드 개선 제안
- 베스트 프랙티스 적용

## 실습

1. VS Code에서 GitHub Copilot 확장 설치
2. GitHub 계정으로 로그인
3. 간단한 함수 작성해보기

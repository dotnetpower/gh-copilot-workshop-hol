# ⚙️ Github Copilot Workshop 한국어 버전

Github Copilot의 기능을 단계별로 학습할 수 있는 워크숍입니다.

[view on moaw.dev](https://moaw.dev/workshop/gh:dotnetpower/gh-copilot-workshop-hol/main/docs/?step=0)

[view on docusaurus](https://dotnetpower.github.io/gh-copilot-workshop-hol/)


# Agenda (Detailed TODO)

## 1. GitHub Copilot 기본 기능 마스터하기
- [x] GitHub Copilot 소개 및 설치 _(01-introduction.md)_
  - [x] VS Code에 GitHub Copilot 확장 설치하기
  - [x] 라이선스 활성화 및 인증 완료하기
- [x] 코드 자동 완성 기능 활용 _(03-basic-usage.md)_
  - [x] 단일 라인 코드 완성 실습 _(lab1-code-completion.md)_
  - [x] 멀티 라인 코드 블록 생성 실습
  - [x] 함수/메서드 자동 생성 실습
- [x] 주석 기반 코드 생성
  - [x] 자연어 주석으로 함수 구현하기
  - [x] TODO 주석을 실제 코드로 변환하기
- [x] Copilot Chat 활용법 _(05-copilot-modes.md)_
  - [x] 인라인 채팅으로 코드 설명 듣기 _(lab2-chat-quality.md)_
  - [x] 사이드바 채팅으로 문제 해결하기
  - [x] 슬래시 명령어(/explain, /fix, /tests) 사용하기

## 2. GitHub Copilot 엔지니어링 프랙티스
- [x] 효과적인 프롬프트 작성법 _(09-understanding-prompt.md)_
  - [x] 명확한 함수명과 변수명 사용하기
  - [x] 구체적인 주석으로 의도 전달하기
  - [x] 컨텍스트 제공을 위한 파일 구조 최적화
- [x] 코드 품질 유지하기 _(10-copilot-engineering-practices.md)_
  - [x] Copilot 제안 코드 리뷰 및 검증
  - [x] 보안 취약점 확인 및 수정
  - [x] 코딩 스타일 가이드 준수하기
- [x] 생산성 향상 팁
  - [x] 키보드 단축키 마스터하기
  - [x] 여러 제안 중 최적의 코드 선택하기
  - [x] 반복 작업 자동화하기

## 3. 사용자 정의 GitHub Copilot 구성
- [x] 개인 설정 커스터마이징 _(11-custom-configuration.md)_
  - [x] Copilot 제안 활성화/비활성화 설정
  - [x] 언어별 설정 구성하기
  - [x] 특정 파일 패턴 제외하기
- [x] 조직/팀 정책 설정
  - [x] Enterprise 설정 이해하기
  - [x] 코드 제안 필터링 규칙 설정
  - [x] 사용 현황 모니터링 및 분석
- [x] GitHub Copilot Extensions 활용
  - [x] 사용 가능한 확장 프로그램 탐색
  - [x] 맞춤형 확장 설치 및 구성

## 4. GitHub Copilot Spaces 실전 활용
- [x] **Vibe 코딩 실전** _(13-vibe-coding.md)_
  - [x] Spaces 환경 설정 및 시작하기
  - [x] 자연어로 프로젝트 구조 설계하기
  - [x] AI와 페어 프로그래밍하며 앱 개발하기
  - [x] 실시간 디버깅 및 문제 해결
- [x] **코드 리팩토링** _(14-code-refactoring-deep.md)_
  - [x] 레거시 코드 분석 및 이해하기
  - [x] Copilot으로 클린 코드 변환하기
  - [x] 디자인 패턴 적용 및 개선
  - [x] 성능 최적화 제안 받기
- [x] **CI/CD 자동화** _(15-cicd-automation.md)_
  - [x] GitHub Actions 워크플로우 생성
  - [x] 테스트 자동화 파이프라인 구축
  - [x] 배포 스크립트 자동 생성
  - [x] 모니터링 및 알림 설정

## 5. 코딩 에이전트와 고급 활용
- [x] GitHub Copilot Agent 이해하기 _(16-coding-agents.md, lab3-edit-agents.md)_
  - [x] Agent 모드 활성화 및 사용법
  - [x] 복잡한 작업 자동화하기
  - [x] Multi-step 작업 처리하기
- [x] 커스텀 에이전트 워크플로우 _(05-copilot-modes.md)_
  - [x] 반복 작업 패턴 정의하기
  - [x] 프로젝트별 에이전트 설정
  - [x] 팀 협업을 위한 에이전트 공유

## 6. 실전 프로젝트 실습
- [x] **10분만에 나만의 GitHub.io 블로그 만들기** _(lab5-docusaurus-blog.md)_
  - [x] Jekyll/Hugo/Docusaurus 템플릿 선택 및 커스터마이징
  - [x] Copilot으로 블로그 포스트 작성하기
  - [x] GitHub Pages 배포 자동화
  - [x] SEO 최적화 및 애널리틱스 연동
- [x] **미니 웹 애플리케이션 개발** _(08-real-project.md, lab4-advanced.md)_
  - [x] 프로젝트 요구사항 정의
  - [x] 프론트엔드 UI 자동 생성
  - [x] 백엔드 API 구현
  - [x] 데이터베이스 연동 및 테스트
  - [x] 프로덕션 배포
- [x] **오픈소스 기여하기** _(lab6-opensource-contribution.md)_
  - [x] 이슈 찾기 및 분석
  - [x] Copilot으로 패치 작성하기
  - [x] Pull Request 생성 및 코드 리뷰

## 7. 마무리 및 Best Practices
- [x] 학습 내용 복습 및 Q&A _(17-workshop-conclusion.md)_
- [x] 실무 적용 전략 수립
- [x] 지속적인 학습 리소스 안내
- [x] 커뮤니티 참여 및 네트워킹

---

## 📚 추가 작성된 문서
- [x] GitHub Copilot 개요 _(02-overview.md)_
- [x] Copilot의 한계점 _(04-limitations.md)_
- [x] GitHub Copilot의 영향 _(06-impact.md)_
- [x] 고급 기능 _(07-advanced-features.md)_
- [x] AI 모델 정보 _(ai-models.md)_
- [x] Copilot Spaces 소개 _(12-copilot-spaces.md)_


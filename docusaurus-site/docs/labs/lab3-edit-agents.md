---
sidebar_position: 12
title: 실습 3 - Copilot Edit & Agents 모드
description: 다중 파일 편집, 프로젝트 구조 개선, Agents Mode를 통한 전문화된 작업 실습
---

# 실습 3: Copilot Edit & Agents 모드

:::tip 📝 학습 목표
- GitHub Copilot Edits 기능 활용법 학습
- 다중 파일 편집 및 프로젝트 구조 개선
- Agents Mode를 통한 전문화된 작업 수행
:::

## 🛠️ 실습 내용

### 3.1 Copilot Edits 기능
- **다중 파일 동시 편집**: 여러 파일을 한 번에 수정
- **프로젝트 범위 리팩토링**: 전체 프로젝트 구조 개선
- **일관된 스타일 적용**: 코딩 컨벤션 자동 적용
  
  ![Image text](/assets/edit_mode.png)

```
// Copilot Edits 명령 예시:
"모든 JavaScript 파일에서 var를 const/let으로 변경해주세요"
"프로젝트 전체에서 함수명을 camelCase로 통일해주세요"
"모든 컴포넌c트에 PropTypes를 추가해주세요"
```

### 3.2 Agents Mode 활용
GitHub Copilot의 전문화된 에이전트들을 활용하여 특정 작업을 효율적으로 수행합니다.

#### @workspace Agent
```
@workspace 이 프로젝트의 전체 구조를 분석해주세요
@workspace 프로젝트에서 사용하지 않는 종속성을 찾아주세요
```

#### @vscode Agent
```
@vscode 이 프로젝트에 적합한 확장 프로그램을 추천해주세요
@vscode 디버깅 설정을 도와주세요
```

#### @terminal Agent
```
@terminal npm 패키지를 설치하고 프로젝트를 실행해주세요
@terminal 테스트를 실행하고 결과를 분석해주세요
```

:::info 그러나...
@workspace 와 같은 지정이 잘 안되는 경우가 있습니다. 이럴 때는 그냥 자연어로 요청해보세요! `터미널에 오류 참고 해서 코드 수정해` 와 같이요.
:::

### 3.3 고급 편집 기능
- **컨텍스트 인식 편집**: 프로젝트 전체 맥락을 고려한 수정
- **패턴 기반 변경**: 반복되는 패턴을 자동으로 감지하여 적용
- **의존성 관리**: 코드 변경 시 관련 파일들도 함께 업데이트

:::note ✅ 실습 과제
1. 전체 프로젝트에서 ES6+ 문법으로 업그레이드하기
2. @workspace 에이전트로 프로젝트 구조 분석하기
3. 여러 파일에 걸친 함수 리팩토링 수행하기
4. @terminal 에이전트로 자동화된 빌드/테스트 파이프라인 구성하기
:::

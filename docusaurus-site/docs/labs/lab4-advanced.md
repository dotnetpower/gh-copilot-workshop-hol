---
sidebar_position: 13
title: 실습 4 - Copilot 고급 기능
description: 고급 프롬프트 엔지니어링, 커스텀 Instructions, 보안 및 팀 협업 최적화 실습
---

# 실습 4: Copilot 고급 기능

:::tip 📝 학습 목표
- GitHub Copilot의 고급 기능 및 최적화 방법 학습
- 팀 협업을 위한 Copilot 활용 전략 수립
- 프로덕션 환경에서의 보안 및 품질 관리
:::

## 🛠️ 실습 내용

### 4.1 고급 프롬프트 엔지니어링
효과적인 프롬프트 작성을 통해 더 정확하고 유용한 결과를 얻습니다.

```python
"""
고급 프롬프트 예시:

컨텍스트: FastAPI 애플리케이션
요구사항: RESTful API 엔드포인트 작성
제약조건: Python 3.12+, JWT 인증, 에러 핸들링 포함, Type hints 사용
스타일: Clean Architecture 패턴 적용
"""

# 이러한 상세한 컨텍스트를 제공하면 더 정확한 코드를 생성합니다
```

### 4.2 커스텀 Instructions 설정
커스텀 지시파일 사용 [github.copilot.chat.codeGeneration.useInstructionFiles](vscode://settings/github.copilot.chat.codeGeneration.useInstructionFiles) 설정 후 `.github/copilot-instructions.md` 파일에 정의

```markdown
---
applyTo: "**"
---
# Project general coding standards

## Naming Conventions
- Use PascalCase for component names, interfaces, and type aliases
- Use camelCase for variables, functions, and methods
- Prefix private class members with underscore (_)
- Use ALL_CAPS for constants

## Error Handling
- Use try/catch blocks for async operations
- Implement proper error boundaries in React components
- Always log errors with contextual information

```

### 4.3 Copilot for Business/Enterprise 기능
- **코드 보안 스캔**: 취약점 자동 탐지 및 수정 제안
- **라이선스 준수**: 오픈소스 라이선스 충돌 방지
- **감사 로그**: 코드 생성 이력 추적
- **정책 관리**: 조직별 사용 정책 설정

### 4.4 성능 모니터링 및 최적화

GitHub Copilot의 사용 성과를 측정하고 최적화하는 방법을 알아봅니다.

#### 4.4.1 VS Code에서 Copilot 통계 확인하기

**방법 1: GitHub Copilot 상태 바 사용**
1. VS Code 하단 상태 바에서 GitHub Copilot 아이콘 클릭
2. "GitHub Copilot Status" 선택
3. 현재 세션의 통계 확인:
   - Completions accepted (수락된 제안 수)
   - Completions shown (표시된 제안 수)
   - Acceptance rate (수락률)

**방법 2: Copilot 설정에서 확인**
1. `Ctrl + Shift + P` → "GitHub Copilot: View Usage"
2. 일일/주간/월간 사용 통계 확인

**방법 3: GitHub.com에서 확인 (Enterprise/Business)**
1. GitHub.com → Settings → Copilot
2. "Usage" 탭에서 조직/팀 전체 통계 확인
3. API 활용 빈도, 수락률, 활성 사용자 수 등

#### 4.4.2 주요 모니터링 지표 (KPI)

| 지표 | 설명 | 목표 수치 |
|------|------|----------|
| **Acceptance Rate** | 제안 수락률 | 30% 이상 |
| **Completions per Day** | 일일 제안 수 | 50+ |
| **Time Saved** | 절약된 개발 시간 | 주당 2시간+ |
| **Lines Generated** | 생성된 코드 라인 수 | 일일 100+ |
| **Active Users** | 활성 사용자 비율 (팀) | 80% 이상 |

#### 4.4.3 메트릭 데이터 수집 방법

**개인 사용자 (수동 수집):**

1. **VS Code 출력 패널에서 확인**
   ```
   Ctrl + Shift + P → "Output: Focus on Output View" → "GitHub Copilot" 선택
   ```
   - 여기서 실시간 제안 수락/거부 로그 확인 가능

2. **Copilot 로그 파일 분석** (고급)
   ```bash
   # VS Code 로그 위치
   # macOS/Linux: ~/.vscode/extensions/github.copilot-*/dist/
   # Windows: %USERPROFILE%\.vscode\extensions\github.copilot-*\dist\
   
   # 텔레메트리 데이터는 GitHub에 전송되며 로컬에는 자세한 로그가 남지 않음
   ```

3. **개인 추적 시트 작성** (권장)
   - 하루 종료 시 상태 바의 수치를 기록
   - 스프레드시트나 Notion에 수동 입력
   - 주간/월간 트렌드 분석

**조직/팀 (GitHub Enterprise):**

1. **GitHub Copilot Metrics API 사용** (Enterprise Cloud/Server 전용)
   ```bash
   # GitHub REST API로 조직 메트릭 조회
   curl -H "Authorization: token YOUR_TOKEN" \
        -H "Accept: application/vnd.github+json" \
        https://api.github.com/orgs/YOUR_ORG/copilot/usage
   ```

2. **GitHub Copilot Dashboard 활용**
   - GitHub.com → Organization Settings → Copilot → Usage
   - 팀원별, 프로젝트별 사용 통계 확인
   - CSV/JSON 형식으로 다운로드 가능

3. **자동화된 데이터 수집 스크립트 예제**

```python
import requests
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Dict
import os

@dataclass
class TeamCopilotMetrics:
    """GitHub API에서 수집한 팀 메트릭"""
    date: str
    total_suggestions: int
    total_acceptances: int
    total_lines_suggested: int
    total_lines_accepted: int
    total_active_users: int
    
    @property
    def acceptance_rate(self) -> float:
        if self.total_suggestions == 0:
            return 0.0
        return (self.total_acceptances / self.total_suggestions) * 100

def fetch_copilot_metrics(org_name: str, token: str, days: int = 7) -> List[TeamCopilotMetrics]:
    """
    GitHub Copilot Metrics API를 통해 조직의 사용 데이터 수집
    
    필요 조건:
    - GitHub Enterprise Cloud/Server 계정
    - 'manage_billing:copilot' 권한이 있는 Personal Access Token
    - 조직 관리자 권한
    """
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    
    # 최근 N일간의 데이터 조회
    url = f"https://api.github.com/orgs/{org_name}/copilot/usage"
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        metrics = []
        for day_data in data:
            metrics.append(TeamCopilotMetrics(
                date=day_data['day'],
                total_suggestions=day_data['total_suggestions_count'],
                total_acceptances=day_data['total_acceptances_count'],
                total_lines_suggested=day_data['total_lines_suggested'],
                total_lines_accepted=day_data['total_lines_accepted'],
                total_active_users=day_data['total_active_users']
            ))
        
        return metrics
        
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print("⚠️  Copilot Metrics API는 GitHub Enterprise에서만 사용 가능합니다.")
        elif e.response.status_code == 403:
            print("⚠️  권한이 부족합니다. 조직 관리자 권한과 적절한 토큰이 필요합니다.")
        else:
            print(f"❌ API 오류: {e}")
        return []

# 사용 예시 (Enterprise 사용자만 가능)
if __name__ == "__main__":
    ORG_NAME = "your-org-name"
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # 환경 변수에서 토큰 로드
    
    if GITHUB_TOKEN:
        metrics = fetch_copilot_metrics(ORG_NAME, GITHUB_TOKEN, days=7)
        
        if metrics:
            print("\n📊 최근 7일 Copilot 사용 현황\n")
            for m in metrics:
                print(f"📅 {m.date}")
                print(f"   수락률: {m.acceptance_rate:.1f}%")
                print(f"   활성 사용자: {m.total_active_users}명")
                print(f"   생성 라인: {m.total_lines_accepted:,}줄")
                print()
    else:
        print("⚠️  GITHUB_TOKEN 환경 변수가 설정되지 않았습니다.")
```

**개인 사용자를 위한 간단한 추적 방법:**

```python
from dataclasses import dataclass
from datetime import datetime
import json
from pathlib import Path

@dataclass
class DailyMetrics:
    """수동으로 입력하는 일일 메트릭"""
    date: str
    acceptance_rate: float
    completions_accepted: int
    completions_shown: int
    notes: str = ""
    
    def save(self, filepath: str = "copilot_metrics.json"):
        """JSON 파일에 저장"""
        path = Path(filepath)
        
        # 기존 데이터 로드
        if path.exists():
            with open(path, 'r') as f:
                data = json.load(f)
        else:
            data = []
        
        # 새 데이터 추가
        data.append({
            'date': self.date,
            'acceptance_rate': self.acceptance_rate,
            'completions_accepted': self.completions_accepted,
            'completions_shown': self.completions_shown,
            'notes': self.notes
        })
        
        # 저장
        with open(path, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"✅ {self.date} 메트릭 저장 완료")

# 사용법: 하루 종료 시 VS Code 상태 바 확인 후 수동 입력
today = DailyMetrics(
    date=datetime.now().strftime('%Y-%m-%d'),
    acceptance_rate=45.5,  # VS Code 상태 바에서 확인
    completions_accepted=89,
    completions_shown=195,
    notes="FastAPI 프로젝트 작업, 제안 품질 좋음"
)
today.save()
```

:::warning ⚠️ 중요: 데이터 수집 제약사항
- **개인 사용자**: VS Code 상태 바에서 **현재 세션**만 확인 가능 (VS Code 재시작 시 초기화)
- **GitHub Copilot Individual**: API 접근 불가, 수동 기록만 가능
- **GitHub Copilot Business/Enterprise**: Metrics API와 대시보드 사용 가능
- GitHub는 텔레메트리 데이터를 수집하지만 개인 사용자에게 상세 로그를 제공하지 않음
:::

#### 4.4.4 최적화 팁

**수락률이 낮을 때 (< 30%):**
- 더 명확한 함수/변수명 사용
- 주석으로 의도를 명확히 표현
- 관련 파일들을 함께 열어 컨텍스트 제공
- 프로젝트 코딩 스타일 가이드 작성 (`.github/copilot-instructions.md`)

**제안이 적절하지 않을 때:**
- `Ctrl + Enter`로 여러 대안 확인
- 더 구체적인 주석 작성
- 타입 힌트 추가 (Python, TypeScript)

**팀 전체 생산성 향상:**
- 팀 공통 Instructions 설정
- 유용한 패턴을 Skills로 정의
- 정기적인 사용 현황 리뷰 (주간/월간)

### 4.5 팀 협업 최적화
- **공통 패턴 공유**: 팀의 코딩 패턴을 Copilot에 학습
- **코드 리뷰 통합**: Pull Request에서 Copilot 활용
- **지식 베이스 구축**: 프로젝트별 베스트 프랙티스 문서화

### 4.6 Copilot Skills 활용하기

GitHub Copilot Skills는 특정 작업을 위한 전문화된 지침을 제공하는 기능입니다. Skills를 통해 Copilot이 특정 도메인이나 작업에 최적화된 응답을 제공하도록 설정할 수 있습니다.

#### 4.6.1 Skills란?

Skills는 GitHub Copilot에게 특정 역할이나 전문 분야를 부여하는 구조화된 지침입니다.

| 구분 | Skills | Prompts | Instructions |
|------|--------|---------|--------------|
| **범위** | 완전한 워크플로우 | 단일 작업 | 지속적인 가이드 |
| **구성** | 단일 파일 (frontmatter 포함) | 단일 파일 | 단일 파일 |
| **사용 방식** | `@skill-name`으로 명시적 호출 | `/prompt-name`으로 실행 | 자동 적용 |
| **위치** | `.github/skills/` | `.github/prompts/` | `.github/copilot-instructions.md` |

#### 4.6.2 VS Code에서 Skills 활성화하기

**1단계: VS Code 설정 확인**

`settings.json`에서 다음 설정이 활성화되어 있는지 확인합니다:

```json
{
    // Skills 파일 사용 활성화
    "github.copilot.chat.codeGeneration.useInstructionFiles": true,
    
    // Chat에서 Skills 참조 허용
    "chat.promptFiles": true
}
```

**2단계: Skills 폴더 구조 생성**

프로젝트 루트에 `.github/skills/` 디렉토리를 생성합니다:

```bash
mkdir -p .github/skills
```

**3단계: Skill 파일 작성**

`.github/skills/` 폴더에 `skill-name.md` 형식으로 파일을 생성합니다.

#### 4.6.3 Skill 파일 구조

Skill 파일은 YAML frontmatter와 지침 본문으로 구성됩니다:

```markdown
---
name: skill-name
description: 스킬에 대한 간단한 설명
tools: ["read", "search", "edit"]
---

# 스킬 지침 내용

여기에 Copilot이 따라야 할 상세 지침을 작성합니다.

## 주요 책임
- 책임 1
- 책임 2

## 가이드라인
- 규칙 1
- 규칙 2
```

**Frontmatter 속성 설명:**
- `name`: 스킬 호출 시 사용할 이름
- `description`: 스킬의 목적과 기능 설명
- `tools`: 스킬이 사용할 수 있는 도구 목록 (read, search, edit 등)

#### 4.6.4 실습: 코드 정리 스킬 만들기

**cleanup-specialist.md 예제:**

```markdown
---
name: cleanup-specialist
description: 지저분한 코드를 정리하고 중복을 제거하며 유지보수성을 개선합니다
tools: ["read", "search", "edit"]
---

당신은 코드베이스를 더 깔끔하고 유지보수하기 쉽게 만드는 정리 전문가입니다.

## 정리 책임 사항

**코드 정리:**
- 사용하지 않는 변수, 함수, import 및 죽은 코드 제거
- 지나치게 복잡한 로직과 중첩 구조 단순화
- 일관된 포맷팅 및 네이밍 규칙 적용

**중복 제거:**
- 중복 코드를 찾아 재사용 가능한 함수로 통합
- 여러 파일에 걸친 반복 패턴을 식별하고 공통 유틸리티 추출

## 가이드라인
- 정리 전후에 항상 변경 사항 테스트
- 한 번에 하나의 개선 사항에 집중
- 기존 기능이 손상되지 않도록 주의
```

#### 4.6.5 Skill 사용 방법

**Chat에서 직접 호출:**
```
@cleanup-specialist 이 파일의 중복 코드를 제거해줘
```

**특정 파일 지정:**
```
@cleanup-specialist src/utils.py 파일을 정리해줘
```

**디렉토리 전체 대상:**
```
@cleanup-specialist src/ 디렉토리의 사용하지 않는 import를 정리해줘
```

#### 4.6.6 현재 워크스페이스에 적용된 Skills 예시

이 워크숍 프로젝트에는 다음과 같은 Skills가 설정되어 있습니다:

**📁 `.github/skills/cleanup-specialist.md`** (영어 버전)
```markdown
---
name: cleanup-specialist
description: Cleans up messy code, removes duplication, and improves maintainability
tools: ["read", "search", "edit"]
---

You are a cleanup specialist focused on making codebases cleaner...
```

**📁 `.github/skills/cleanup-specialist-kr.md`** (한국어 버전)
```markdown
---
name: cleanup-specialist-kr
description: 지저분한 코드를 정리하고 중복을 제거하며 유지보수성을 개선합니다
tools: ["read", "search", "edit"]
---

당신은 코드베이스를 더 깔끔하고 유지보수하기 쉽게 만드는 정리 전문가입니다...
```

**📁 `.github/copilot-instructions.md`에 정의된 스킬 사용 규칙:**
```markdown
### 5. 스킬 사용 규칙

**코드 정리 작업 시 필수:**
- 코드 정리, 리팩토링, 중복 제거 요청 시 `@cleanup-specialist` 또는 
  `@cleanup-specialist-kr` 스킬을 사용해야 함
- 사용하지 않는 import, 변수, 함수 제거 시 해당 스킬 적용
- 코드 품질 개선 및 유지보수성 향상 작업에 자동으로 스킬 적용

**스킬 사용 예시:**
사용자: "이 파일의 중복 코드를 제거해줘"
→ 자동으로 @cleanup-specialist-kr 스킬 적용
```

#### 4.6.7 유용한 Skills 아이디어

| 스킬 이름 | 용도 |
|----------|------|
| `api-developer` | REST/GraphQL API 개발 전문 |
| `test-writer` | 단위/통합 테스트 작성 전문 |
| `security-reviewer` | 보안 취약점 검토 전문 |
| `docs-writer` | 문서화 및 주석 작성 전문 |
| `performance-optimizer` | 성능 최적화 전문 |
| `accessibility-expert` | 접근성 개선 전문 |

:::tip 💡 Skills 활용 팁
- **명확한 범위 설정**: 하나의 스킬은 하나의 전문 분야에 집중하세요
- **구체적인 지침**: 모호한 표현보다 구체적인 규칙을 작성하세요
- **팀 공유**: 팀원들과 유용한 스킬을 공유하여 일관된 코드 품질을 유지하세요
- **점진적 개선**: 사용하면서 지침을 지속적으로 개선하세요
:::

### 4.7 Git 커밋 메시지 자동 생성

GitHub Copilot은 변경된 코드를 분석하여 의미 있는 커밋 메시지를 자동으로 생성할 수 있습니다.

#### 4.7.1 기본 사용법
1. 소스 제어(Source Control) 패널 열기 (`Ctrl + Shift + G`)
2. 변경사항이 있는 상태에서 커밋 메시지 입력창의 **✨ 아이콘(Sparkle)** 클릭
3. Copilot이 자동으로 커밋 메시지 생성


#### 4.7.2 커밋 메시지 생성 설정
`.vscode/settings.json` 파일에서 커밋 메시지 생성을 커스터마이징할 수 있습니다:

```json
{
    // 한국어로 커밋 메시지 생성
    "github.copilot.chat.localeOverride": "ko",
    
    // 커밋 메시지 자동 생성 활성화
    "github.copilot.chat.generateCommitMessage.enabled": true,
    
    // 커밋 메시지 생성 규칙 커스터마이징
    "github.copilot.chat.commitMessageGeneration.instructions": [
        {
            "text": "한국어로 간략하게 생성해, feat: 같은 프리픽스는 넣지마"
        }
    ]
}
```

#### 4.7.3 커밋 메시지 커스터마이징 옵션

**기본 형식 (Conventional Commits 스타일):**
```json
{
    "github.copilot.chat.commitMessageGeneration.instructions": [
        {
            "text": "Use Conventional Commits format: <type>(<scope>): <description>"
        }
    ]
}
```

**팀 협업 스타일:**
```json
{
    "github.copilot.chat.commitMessageGeneration.instructions": [
        {
            "text": "커밋 메시지는 다음 규칙을 따라 작성: 1) 첫 줄은 50자 이내로 요약, 2) 변경 이유를 명확히 기술, 3) 이슈 번호가 있다면 #123 형식으로 포함"
        }
    ]
}
```

**한국어 상세 설명 스타일:**
```json
{
    "github.copilot.chat.commitMessageGeneration.instructions": [
        {
            "text": "한국어로 작성하며, 제목은 명령형으로 시작하고, 본문에는 '무엇을', '왜' 변경했는지 자세히 설명"
        }
    ]
}
```

#### 4.7.4 실습 예시

**변경 전 코드:**
```python
def calculate_total(items):
    return sum(item.price for item in items)
```

**변경 후 코드:**
```python
from typing import List
from dataclasses import dataclass

@dataclass
class Item:
    price: float
    quantity: int

def calculate_total(items: List[Item]) -> float:
    if not items:
        return 0.0
    return sum(item.price * item.quantity for item in items)
```

**자동 생성된 커밋 메시지 예시:**
```
계산 함수에 빈 배열 체크 및 수량 계산 로직 추가

- items가 비어있거나 null인 경우 0 반환하도록 가드 조건 추가
- 가격 계산 시 수량을 곱하도록 수정하여 정확한 총액 계산
```

:::tip 💡 커밋 메시지 생성 팁
- **변경사항을 논리적으로 그룹화**: 관련된 변경사항을 함께 스테이징하면 더 일관된 메시지를 생성합니다
- **커스텀 규칙 활용**: 팀의 커밋 메시지 컨벤션에 맞게 instructions를 설정하세요
- **리뷰 후 수정**: 자동 생성된 메시지를 검토하고 필요시 수정하세요
- **컨텍스트 제공**: 복잡한 변경의 경우, 관련 파일들을 함께 변경하면 더 정확한 메시지를 생성합니다
:::

### 4.8 CI/CD 파이프라인 통합
```yaml
# .github/workflows/copilot-security.yml
name: Copilot Security Scan
on: [push, pull_request]
jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: GitHub Copilot Security Scan
        uses: github/copilot-security-action@v1
```

:::note ✅ 실습 과제
1. 프로젝트별 커스텀 Instructions 설정하기
2. Copilot을 활용한 보안 코드 리뷰 수행하기
3. 팀 코딩 스타일 가이드 자동화하기
4. **Copilot Skills 설정 및 활용하기**
   - `.github/skills/` 폴더에 커스텀 스킬 파일 생성
   - `@skill-name` 형식으로 스킬 호출하여 코드 정리 수행
   - 팀에 유용한 스킬 아이디어 브레인스토밍 및 구현
5. **Git 커밋 메시지 자동 생성 설정 및 활용하기**
   - `.vscode/settings.json`에 커밋 메시지 생성 규칙 추가
   - 여러 파일을 수정한 후 자동 생성된 커밋 메시지 확인
   - 팀 컨벤션에 맞게 instructions 커스터마이징
6. CI/CD 파이프라인에 Copilot 보안 스캔 통합하기
7. Copilot 사용 성과 측정 및 분석하기
:::

:::tip 🎯 고급 활용 팁
- **컨텍스트 최적화**: 관련 파일들을 함께 열어 더 나은 제안 받기
- **단계별 접근**: 복잡한 문제를 작은 단위로 나누어 해결하기
- **피드백 루프**: 생성된 코드를 검토하고 개선 사항 반영하기
- **보안 의식**: 생성된 코드의 보안 취약점 항상 검증하기
:::

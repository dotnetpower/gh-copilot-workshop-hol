---
sidebar_position: 14
title: 실습 5 - GitHub Copilot으로 Docusaurus 블로그 만들기
description: GitHub Copilot을 활용한 Docusaurus 블로그 구축 및 컴포넌트, 설정 파일 작성 실습
---

# 실습 5: GitHub Copilot으로 Docusaurus 블로그 만들기

:::tip 📝 학습 목표
- GitHub Copilot을 활용한 Docusaurus 블로그 구축
- 실제 프로젝트에서 Copilot Chat 및 코드 생성 활용
- 컴포넌트, 마크다운, 설정 파일 작성 자동화
:::

## 🎯 실습 개요

이 실습에서는 GitHub Copilot을 최대한 활용하여 Docusaurus 기반 블로그를 처음부터 만들어봅니다. Copilot Chat으로 구조를 설계하고, 인라인 제안으로 코드를 작성하며, 에이전트 기능으로 파일을 자동 생성합니다.

## 🛠️ 준비 사항

### 필수 도구
- Node.js 18.0 이상
- VS Code with GitHub Copilot 확장
- Git

### Github Repo 생성
<a href="https://github.com" target="_blank">https://github.com</a> 에 로그인하여 본인 계정의 repositories 에서 `New` 를 클릭 하여 새로운 리포지토리 생성
![alt text](/img/labs/github_repo.png)

Owner를 본인 계정 선택 후, Repository name 을 적절하게 넣고, add README 토클 후 `Create repository` 클릭
![alt text](/img/labs/create_repo.png)

생성된 repo 에서 로컬로 코드 복사 (선호하는 다른 방식도 OK)

![alt text](/img/labs/git_code_clone.png)

```bash
# 예시
git clone https://github.com/dotnetpower/gh-blog.git
cd gh-blog
code .
```


### 프로젝트 생성

먼저 Copilot Chat에 물어봅시다:

```
@workspace Docusaurus 블로그 프로젝트를 만들고 싶어요. 
어떤 명령어를 실행해야 하고, 어떤 구조로 시작하면 좋을까요?
```

![alt text](/img/labs/ask_blog_project.png)

Copilot이 제안한 명령어 실행:

```bash
npx create-docusaurus@latest my-blog classic --typescript
cd my-blog
```
:::warning 주의!
하위 폴더(my-blog)를 생성하므로 `현재 폴더에 생성하려면?` 이라는 프롬프트를 통해서 명령어 교정
:::

그럼에도 불구하고 생성 오류가 발생됨

![alt text](/img/labs/create_blog_error.png)

모드를 `Agent` 로 바꾸고 생성 요청 프롬프트 작성

![alt text](/img/labs/create_blog_agent.png)

`bash` 명령을 직접 실행하기위한 승인 요청, `Allow` 또는 셀렉트 박스 클릭하여 옵션 설정

![alt text](/img/labs/run_allow.png)

이후 추가 승인 관련 사항 follow-up 이후 프로젝트 생성이 완료되면 다음 버튼을 클릭하여 `npm start` 실행

![alt text](/img/labs/npm_start_cmd.png)

실행된 화면 예시

![alt text](/img/labs/docusaurus_main.png)


## Github Pages 로 배포
```prompt
github action 으로 배포할수 있게 구성해 주고 github.io 로 접속할수 있게 배포 후 링크 알려줘
```

node 버전 문제로 오류가 발생되어 agent 모드로 오류 수정 요청

![alt text](/img/labs/github_action_error.png)

만약 https://github.com/dotnetpower/gh-blog/actions Github Action 이 다시 오류가 난다면 오류 내용을 복사해서 Agent 에게 알려줍니다.

![alt text](/img/labs/github_action_error2.png)

다음처럼 오류 내용을 복사해서 vscode 의 github copilot agent 에게 붙여넣습니다.

![alt text](/img/labs/github_action_error2_vscode.png)

Actions 이 성공적으로 완료가 되면

![alt text](/img/labs/github_action_deployed.png)

https://dotnetpower.github.io/gh-blog/ 으로 접속이 가능

---

## 📝 단계별 실습

### 1단계: 블로그 설정 커스터마이징

#### 1.1 Copilot Chat으로 설정 파일 이해하기

`docusaurus.config.ts` 파일을 열고 Copilot Chat에 질문:

```
이 설정 파일의 각 섹션이 무엇을 하는지 설명해주고, 
개인 블로그를 위한 최적의 설정을 제안해주세요.
```

#### 1.2 설정 파일 수정

Copilot 인라인 제안을 사용하여 다음을 수정:

```typescript
// docusaurus.config.ts
import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: '내 기술 블로그',
  tagline: 'GitHub Copilot과 함께 성장하는 개발자',
  favicon: 'img/favicon.ico',

  // GitHub Pages 배포 설정 - Copilot에게 물어보세요!
  url: 'https://your-username.github.io',
  baseUrl: '/my-blog/',

  // GitHub 저장소 정보
  organizationName: 'your-username',
  projectName: 'my-blog',

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'ko',
    locales: ['ko', 'en'],
  },

  presets: [
    [
      'classic',
      {
        docs: false, // 블로그 전용으로 문서 비활성화
        blog: {
          routeBasePath: '/', // 블로그를 루트로
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          // Copilot 제안: 블로그 포스트당 표시할 개수
          blogSidebarCount: 'ALL',
          blogSidebarTitle: '모든 포스트',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    // Copilot이 제안하는 테마 설정
    navbar: {
      title: '개발 블로그',
      logo: {
        alt: 'My Blog Logo',
        src: 'img/logo.svg',
      },
      items: [
        {to: '/', label: '블로그', position: 'left'},
        {to: '/tags', label: '태그', position: 'left'},
        {
          href: 'https://github.com/your-username/my-blog',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      copyright: `Copyright © ${new Date().getFullYear()} My Blog. Built with Docusaurus and GitHub Copilot.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      // Copilot 제안: 지원할 프로그래밍 언어
      additionalLanguages: ['bash', 'json', 'yaml', 'typescript'],
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
```

**💡 Copilot 활용 팁:**
- 주석으로 "// GitHub Pages 설정 추가"라고 입력하면 자동으로 필요한 코드 제안
- 타입스크립트 타입 힌트가 자동으로 추가됨

---

### 2단계: 첫 블로그 포스트 작성

#### 2.1 Copilot Chat으로 포스트 구조 생성

Copilot Chat에서:

```
첫 블로그 포스트를 작성하려고 해요. 
"GitHub Copilot 활용기"라는 주제로 마크다운 템플릿을 만들어주세요.
frontmatter와 본문 구조를 포함해주세요.
```

#### 2.2 블로그 포스트 파일 생성

`blog/2025-12-02-getting-started-with-copilot.md` 파일 생성:

```markdown
---
slug: getting-started-with-copilot
title: GitHub Copilot으로 개발 생산성 10배 높이기
authors: 
  name: Your Name
  title: Software Engineer
  url: https://github.com/your-username
  image_url: https://github.com/your-username.png
tags: [github-copilot, ai, productivity, tutorial]
---

# GitHub Copilot으로 개발 생산성 10배 높이기

GitHub Copilot은 AI 기반 코드 자동완성 도구로, 개발자의 생산성을 극적으로 향상시킵니다.

<!-- truncate -->

## Copilot의 핵심 기능

### 1. 인라인 코드 제안

Copilot은 현재 컨텍스트를 이해하고 다음에 작성할 코드를 제안합니다.

```typescript
// 함수 시그니처만 작성하면 구현부를 자동 생성
function calculateTotalPrice(items: CartItem[], taxRate: number): number {
  // Copilot이 여기서 자동으로 구현 제안
  const subtotal = items.reduce((sum, item) => sum + item.price * item.quantity, 0);
  return subtotal * (1 + taxRate);
}
```

### 2. Copilot 모드

**Ask 모드**: 질문과 답변으로 빠른 확인  
**Edit 모드**: 검토 후 코드 변경 적용  
**Agent 모드**: 자율적으로 멀티스텝 작업 수행

### 3. 컨텍스트 활용

`@workspace`, `@terminal` 등의 참조로 프로젝트 전체를 이해하고 작업합니다.

## 실전 활용 사례

### 사례 1: API 엔드포인트 작성

```python
# Copilot에게 "FastAPI로 사용자 CRUD API 작성"이라고 요청
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str

users_db: List[User] = []

@app.post("/users/", response_model=User)
async def create_user(user: User):
    users_db.append(user)
    return user

@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    user = next((u for u in users_db if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
```

### 사례 2: 테스트 코드 자동 생성

함수를 선택하고 Copilot Chat에서:
```
이 함수에 대한 단위 테스트를 작성해주세요. 
edge case도 포함해주세요.
```

## 결론

GitHub Copilot은 단순한 자동완성을 넘어 개발 파트너가 되어줍니다. 이 블로그를 통해 더 많은 활용 팁을 공유하겠습니다!

## 다음 포스트 예고

- Copilot으로 React 컴포넌트 개발하기
- Copilot을 활용한 테스트 주도 개발(TDD)
- Copilot Enterprise의 고급 기능 탐구
```

**💡 Copilot 활용 포인트:**
- 포스트 제목을 입력하면 자동으로 slug 제안
- 태그를 몇 개 입력하면 관련 태그 자동 추천
- 코드 블록 언어를 지정하면 자동으로 문법 강조

---

### 3단계: 커스텀 React 컴포넌트 만들기

#### 3.1 저자 카드 컴포넌트

Copilot Chat에 요청:

```
블로그 포스트 하단에 표시할 저자 프로필 카드 컴포넌트를 
React + TypeScript로 만들어주세요. 
props는 name, bio, avatar, socialLinks를 받아야 합니다.
```

`src/components/AuthorCard.tsx` 생성:

```tsx
import React from 'react';
import styles from './AuthorCard.module.css';

interface SocialLink {
  platform: string;
  url: string;
  icon: string;
}

interface AuthorCardProps {
  name: string;
  bio: string;
  avatar: string;
  socialLinks?: SocialLink[];
}

export default function AuthorCard({ 
  name, 
  bio, 
  avatar, 
  socialLinks = [] 
}: AuthorCardProps): JSX.Element {
  return (
    <div className={styles.authorCard}>
      <img 
        src={avatar} 
        alt={`${name} profile`} 
        className={styles.avatar}
      />
      <div className={styles.info}>
        <h3 className={styles.name}>{name}</h3>
        <p className={styles.bio}>{bio}</p>
        {socialLinks.length > 0 && (
          <div className={styles.socialLinks}>
            {socialLinks.map((link) => (
              <a
                key={link.platform}
                href={link.url}
                target="_blank"
                rel="noopener noreferrer"
                className={styles.socialLink}
                aria-label={link.platform}
              >
                {link.icon}
              </a>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
```

#### 3.2 스타일 파일

Copilot에게 CSS 모듈 작성 요청:

`src/components/AuthorCard.module.css`:

```css
/* Copilot이 자동으로 생성한 스타일 */
.authorCard {
  display: flex;
  gap: 1.5rem;
  padding: 2rem;
  background: var(--ifm-card-background-color);
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  margin: 2rem 0;
}

.avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  object-fit: cover;
}

.info {
  flex: 1;
}

.name {
  margin: 0 0 0.5rem 0;
  font-size: 1.5rem;
  color: var(--ifm-heading-color);
}

.bio {
  margin: 0 0 1rem 0;
  color: var(--ifm-color-emphasis-700);
  line-height: 1.6;
}

.socialLinks {
  display: flex;
  gap: 1rem;
}

.socialLink {
  font-size: 1.5rem;
  color: var(--ifm-color-primary);
  transition: color 0.2s;
}

.socialLink:hover {
  color: var(--ifm-color-primary-dark);
}
```

---

### 4단계: 블로그 리스트 페이지 커스터마이징

#### 4.1 블로그 포스트 카드 개선

Copilot Chat 사용:

```
블로그 포스트 목록을 카드 형태로 보여주는 커스텀 컴포넌트를 만들어주세요.
- 썸네일 이미지 지원
- 읽기 시간 표시
- 태그 표시
- hover 효과
```

`src/components/BlogPostCard.tsx`:

```tsx
import React from 'react';
import Link from '@docusaurus/Link';
import styles from './BlogPostCard.module.css';

interface BlogPostCardProps {
  title: string;
  description: string;
  permalink: string;
  date: string;
  readingTime?: number;
  tags?: Array<{label: string; permalink: string}>;
  thumbnail?: string;
}

export default function BlogPostCard({
  title,
  description,
  permalink,
  date,
  readingTime,
  tags = [],
  thumbnail,
}: BlogPostCardProps): JSX.Element {
  return (
    <article className={styles.card}>
      {thumbnail && (
        <Link to={permalink} className={styles.thumbnailLink}>
          <img 
            src={thumbnail} 
            alt={title}
            className={styles.thumbnail}
            loading="lazy"
          />
        </Link>
      )}
      <div className={styles.content}>
        <div className={styles.meta}>
          <time dateTime={date} className={styles.date}>
            {new Date(date).toLocaleDateString('ko-KR', {
              year: 'numeric',
              month: 'long',
              day: 'numeric',
            })}
          </time>
          {readingTime && (
            <span className={styles.readingTime}>
              {Math.ceil(readingTime)}분 소요
            </span>
          )}
        </div>
        
        <Link to={permalink} className={styles.titleLink}>
          <h2 className={styles.title}>{title}</h2>
        </Link>
        
        <p className={styles.description}>{description}</p>
        
        {tags.length > 0 && (
          <div className={styles.tags}>
            {tags.map((tag) => (
              <Link
                key={tag.permalink}
                to={tag.permalink}
                className={styles.tag}
              >
                #{tag.label}
              </Link>
            ))}
          </div>
        )}
      </div>
    </article>
  );
}
```

**💡 Copilot이 자동으로 추가한 기능:**
- 접근성을 위한 `aria-label`
- 성능 최적화를 위한 `loading="lazy"`
- 타입 안전성을 위한 TypeScript 인터페이스

---

### 5단계: 다크 모드 테마 커스터마이징

#### 5.1 커스텀 CSS 변수

`src/css/custom.css` 파일에 Copilot 도움으로 추가:

```css
/**
 * Copilot에게: "다크 모드와 라이트 모드를 위한 
 * 커스텀 컬러 팔레트를 만들어주세요"
 */

:root {
  /* 브랜드 컬러 */
  --ifm-color-primary: #2e8555;
  --ifm-color-primary-dark: #29784c;
  --ifm-color-primary-darker: #277148;
  --ifm-color-primary-darkest: #205d3b;
  --ifm-color-primary-light: #33925d;
  --ifm-color-primary-lighter: #359962;
  --ifm-color-primary-lightest: #3cad6e;
  
  /* 코드 블록 */
  --ifm-code-font-size: 95%;
  --docusaurus-highlighted-code-line-bg: rgba(0, 0, 0, 0.1);
  
  /* 커스텀 변수 */
  --blog-card-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  --blog-card-hover-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
}

[data-theme='dark'] {
  --ifm-color-primary: #25c2a0;
  --ifm-color-primary-dark: #21af90;
  --ifm-color-primary-darker: #1fa588;
  --ifm-color-primary-darkest: #1a8870;
  --ifm-color-primary-light: #29d5b0;
  --ifm-color-primary-lighter: #32d8b4;
  --ifm-color-primary-lightest: #4fddbf;
  
  --docusaurus-highlighted-code-line-bg: rgba(0, 0, 0, 0.3);
  --blog-card-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
  --blog-card-hover-shadow: 0 8px 16px rgba(0, 0, 0, 0.4);
}

/* Copilot이 제안한 글로벌 스타일 개선 */
.markdown {
  --ifm-h1-font-size: 2.5rem;
  --ifm-h2-font-size: 2rem;
  --ifm-h3-font-size: 1.5rem;
}

.markdown > h2 {
  margin-top: 3rem;
  border-bottom: 2px solid var(--ifm-color-primary);
  padding-bottom: 0.5rem;
}

/* 코드 블록 개선 */
.theme-code-block {
  margin: 2rem 0;
  box-shadow: var(--blog-card-shadow);
}

/* 블로그 포스트 반응형 이미지 */
.markdown img {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
  box-shadow: var(--blog-card-shadow);
}
```

---

### 6단계: SEO 및 메타데이터 최적화

#### 6.1 Copilot으로 SEO 플러그인 추가

Copilot Chat에 질문:

```
Docusaurus에 SEO를 개선하기 위한 설정을 추가하고 싶어요.
sitemap, robots.txt, Open Graph 메타태그를 포함해주세요.
```

`docusaurus.config.ts`에 추가:

```typescript
const config: Config = {
  // ... 기존 설정

  plugins: [
    [
      '@docusaurus/plugin-sitemap',
      {
        changefreq: 'weekly',
        priority: 0.5,
        ignorePatterns: ['/tags/**'],
        filename: 'sitemap.xml',
      },
    ],
  ],

  themeConfig: {
    metadata: [
      {
        name: 'keywords',
        content: 'blog, development, github copilot, programming, tutorial',
      },
      {
        name: 'twitter:card',
        content: 'summary_large_image',
      },
    ],
    image: 'img/social-card.png', // Open Graph 이미지
    // ... 기존 themeConfig
  } satisfies Preset.ThemeConfig,
};
```

---

### 7단계: 검색 기능 추가

#### 7.1 Algolia DocSearch 설정

Copilot에게 요청:

```
Docusaurus에 Algolia DocSearch를 설정하는 방법을 알려주고,
필요한 설정 코드를 작성해주세요.
```

`docusaurus.config.ts`에 추가:

```typescript
themeConfig: {
  algolia: {
    appId: 'YOUR_APP_ID',
    apiKey: 'YOUR_SEARCH_API_KEY',
    indexName: 'YOUR_INDEX_NAME',
    contextualSearch: true,
    searchParameters: {},
    searchPagePath: 'search',
  },
  // ... 기존 설정
}
```

---

### 8단계: 배포 자동화

#### 8.1 GitHub Actions 워크플로우

Copilot Chat에 요청:

```
Docusaurus 블로그를 GitHub Pages에 자동 배포하는 
GitHub Actions 워크플로우를 작성해주세요.
```

`.github/workflows/deploy.yml`:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

permissions:
  contents: write

jobs:
  deploy:
    name: Deploy to GitHub Pages
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: 18
          cache: npm
      
      - name: Install dependencies
        run: npm ci
      
      - name: Build website
        run: npm run build
      
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        if: github.ref == 'refs/heads/main'
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./build
          user_name: github-actions[bot]
          user_email: github-actions[bot]@users.noreply.github.com
```

---

## 🎓 학습 내용 정리

### Copilot 활용 기법

1. **Chat 활용**
   - 프로젝트 구조 설계
   - 설정 파일 이해 및 최적화
   - 복잡한 컴포넌트 스캐폴딩

2. **인라인 제안**
   - TypeScript 타입 자동 완성
   - CSS 스타일링 자동 생성
   - 설정 값 자동 추천

3. **에이전트 기능**
   - `@workspace`로 프로젝트 전체 이해
   - `@terminal`로 명령어 실행
   - 파일 간 관계 파악

### 생산성 향상 포인트

- **시간 절약**: 컴포넌트 보일러플레이트 자동 생성
- **품질 향상**: 타입 안전성, 접근성, SEO 자동 적용
- **학습 효과**: 실시간 베스트 프랙티스 제안

---

## 🚀 도전 과제

### 초급
1. 추가 블로그 포스트 3개 작성 (Copilot 활용)
2. 카테고리별 태그 페이지 커스터마이징
3. 푸터에 소셜 미디어 링크 추가

### 중급
1. 댓글 시스템 통합 (Giscus 또는 Utterances)
2. 블로그 포스트 시리즈 기능 구현
3. RSS 피드 커스터마이징

### 고급
1. MDX를 활용한 인터랙티브 컴포넌트 추가
2. 블로그 통계 대시보드 페이지 구현
3. 다국어 지원 (i18n) 설정

---

## 📚 참고 자료

- [Docusaurus 공식 문서](https://docusaurus.io/)
- [GitHub Copilot 문서](https://docs.github.com/copilot)
- [React TypeScript 가이드](https://react-typescript-cheatsheet.netlify.app/)

---

## ✅ 체크리스트

완료한 항목을 체크하세요:

- [ ] Docusaurus 프로젝트 생성
- [ ] 설정 파일 커스터마이징
- [ ] 첫 블로그 포스트 작성
- [ ] 커스텀 React 컴포넌트 구현
- [ ] 테마 및 스타일 커스터마이징
- [ ] SEO 최적화 적용
- [ ] GitHub Pages 배포 설정
- [ ] 로컬에서 빌드 테스트 (`npm run build`)
- [ ] 배포 확인

:::success 축하합니다!
GitHub Copilot을 활용하여 완전한 기능을 갖춘 블로그를 만들었습니다. 이제 이 블로그로 여러분의 개발 여정을 기록해보세요!
:::

---

## 💡 다음 단계

- 정기적으로 블로그 포스트 작성
- 애널리틱스 도구 연동 (Google Analytics, Plausible)
- 뉴스레터 기능 추가
- 검색 엔진 최적화 모니터링

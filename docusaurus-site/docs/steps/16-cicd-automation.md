---
sidebar_position: 15
title: CI/CD 자동화
description: GitHub Copilot을 활용한 CI/CD 파이프라인 구축 및 자동화 방법
---

# CI/CD 자동화

## 개요

GitHub Copilot을 활용하여 CI/CD 파이프라인을 구축하고 자동화하는 방법을 학습합니다.

## GitHub Actions 워크플로우 생성

### 기본 CI 파이프라인

**Copilot Chat 활용**
```
"Node.js 프로젝트를 위한 GitHub Actions CI 워크플로우를 만들어줘.
 - 테스트 실행
 - 린팅 검사
 - 빌드
 - 코드 커버리지 리포트"
```

**생성된 워크플로우**
```yaml
# .github/workflows/ci.yml
name: CI Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    strategy:
      matrix:
        node-version: [18.x, 20.x]
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Setup Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run linter
        run: npm run lint
      
      - name: Run tests
        run: npm test -- --coverage
      
      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v3
        with:
          file: ./coverage/coverage-final.json
          fail_ci_if_error: true
  
  build:
    needs: test
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20.x'
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Build project
        run: npm run build
      
      - name: Upload build artifacts
        uses: actions/upload-artifact@v3
        with:
          name: build-files
          path: dist/
          retention-days: 7
```

### Python 프로젝트 CI/CD

```yaml
# .github/workflows/python-ci.yml
name: Python CI/CD

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    strategy:
      matrix:
        python-version: ['3.10', '3.11', '3.12']
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
          cache: 'pip'
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install -r requirements-dev.txt
      
      - name: Lint with Ruff
        run: |
          ruff check .
      
      - name: Type check with mypy
        run: |
          mypy src/
      
      - name: Test with pytest
        run: |
          pytest --cov=src --cov-report=xml --cov-report=term
      
      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          file: ./coverage.xml

  security:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Run Bandit security scan
        run: |
          pip install bandit
          bandit -r src/ -f json -o bandit-report.json
      
      - name: Run Safety check
        run: |
          pip install safety
          safety check --json
```

### .NET 프로젝트 CI/CD

**Copilot이 생성한 워크플로우**
```yaml
# .github/workflows/dotnet-ci.yml
name: .NET CI/CD

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

env:
  DOTNET_VERSION: '8.0.x'
  
jobs:
  build-and-test:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup .NET
        uses: actions/setup-dotnet@v3
        with:
          dotnet-version: ${{ env.DOTNET_VERSION }}
      
      - name: Restore dependencies
        run: dotnet restore
      
      - name: Build
        run: dotnet build --no-restore --configuration Release
      
      - name: Test
        run: |
          dotnet test --no-build --configuration Release \
            --logger "trx;LogFileName=test-results.trx" \
            --collect:"XPlat Code Coverage" \
            -- DataCollectionRunSettings.DataCollectors.DataCollector.Configuration.Format=opencover
      
      - name: Publish test results
        uses: dorny/test-reporter@v1
        if: always()
        with:
          name: .NET Tests
          path: '**/test-results.trx'
          reporter: dotnet-trx
      
      - name: Code Coverage Report
        uses: codecov/codecov-action@v3
        with:
          file: coverage.opencover.xml
  
  publish:
    needs: build-and-test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup .NET
        uses: actions/setup-dotnet@v3
        with:
          dotnet-version: ${{ env.DOTNET_VERSION }}
      
      - name: Publish
        run: dotnet publish -c Release -o ./publish
      
      - name: Upload artifacts
        uses: actions/upload-artifact@v3
        with:
          name: app-package
          path: ./publish
```

## Docker 이미지 빌드 & 배포

### Multi-stage Docker Build

```yaml
# .github/workflows/docker-build.yml
name: Build and Push Docker Image

on:
  push:
    branches: [ main ]
    tags: [ 'v*' ]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3
      
      - name: Log in to Container Registry
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=ref,event=branch
            type=ref,event=pr
            type=semver,pattern={{version}}
            type=semver,pattern={{major}}.{{minor}}
            type=sha,prefix={{branch}}-
      
      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
          platforms: linux/amd64,linux/arm64
      
      - name: Scan image for vulnerabilities
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:latest
          format: 'sarif'
          output: 'trivy-results.sarif'
      
      - name: Upload Trivy results to GitHub Security
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: 'trivy-results.sarif'
```

## 배포 자동화

### Azure App Service 배포

**Copilot 프롬프트**
```
"Azure App Service에 Node.js 앱을 배포하는 
 GitHub Actions 워크플로우를 만들어줘.
 - 프로덕션과 스테이징 환경 분리
 - Health check 포함
 - 롤백 가능하도록"
```

```yaml
# .github/workflows/deploy-azure.yml
name: Deploy to Azure App Service

on:
  push:
    branches: [ main ]
  workflow_dispatch:

env:
  AZURE_WEBAPP_NAME: my-app
  NODE_VERSION: '20.x'

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'
      
      - name: Install and build
        run: |
          npm ci
          npm run build --if-present
          npm run test --if-present
      
      - name: Upload artifact for deployment
        uses: actions/upload-artifact@v3
        with:
          name: node-app
          path: .
  
  deploy-staging:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: 'Staging'
      url: ${{ steps.deploy.outputs.webapp-url }}
    
    steps:
      - name: Download artifact
        uses: actions/download-artifact@v3
        with:
          name: node-app
      
      - name: Deploy to Azure Web App (Staging)
        id: deploy
        uses: azure/webapps-deploy@v2
        with:
          app-name: ${{ env.AZURE_WEBAPP_NAME }}
          slot-name: 'staging'
          publish-profile: ${{ secrets.AZURE_WEBAPP_PUBLISH_PROFILE_STAGING }}
          package: .
      
      - name: Health check
        run: |
          sleep 30
          response=$(curl -s -o /dev/null -w "%{http_code}" ${{ steps.deploy.outputs.webapp-url }}/health)
          if [ $response -ne 200 ]; then
            echo "Health check failed with status $response"
            exit 1
          fi
  
  deploy-production:
    needs: deploy-staging
    runs-on: ubuntu-latest
    environment:
      name: 'Production'
      url: ${{ steps.deploy.outputs.webapp-url }}
    
    steps:
      - name: Download artifact
        uses: actions/download-artifact@v3
        with:
          name: node-app
      
      - name: Deploy to Azure Web App (Production)
        id: deploy
        uses: azure/webapps-deploy@v2
        with:
          app-name: ${{ env.AZURE_WEBAPP_NAME }}
          publish-profile: ${{ secrets.AZURE_WEBAPP_PUBLISH_PROFILE }}
          package: .
      
      - name: Health check
        run: |
          sleep 30
          response=$(curl -s -o /dev/null -w "%{http_code}" ${{ steps.deploy.outputs.webapp-url }}/health)
          if [ $response -ne 200 ]; then
            echo "Production health check failed!"
            exit 1
          fi
      
      - name: Notify deployment
        uses: 8398a7/action-slack@v3
        if: always()
        with:
          status: ${{ job.status }}
          text: 'Production deployment completed!'
          webhook_url: ${{ secrets.SLACK_WEBHOOK }}
```

### Kubernetes 배포

```yaml
# .github/workflows/deploy-k8s.yml
name: Deploy to Kubernetes

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up kubectl
        uses: azure/setup-kubectl@v3
        with:
          version: 'v1.28.0'
      
      - name: Configure kubectl
        run: |
          echo "${{ secrets.KUBE_CONFIG }}" | base64 -d > kubeconfig
          echo "KUBECONFIG=$(pwd)/kubeconfig" >> $GITHUB_ENV
      
      - name: Deploy to Kubernetes
        run: |
          # 이미지 태그 업데이트
          sed -i "s|IMAGE_TAG|${GITHUB_SHA}|g" k8s/deployment.yaml
          
          # 배포 실행
          kubectl apply -f k8s/
          
          # 롤아웃 상태 확인
          kubectl rollout status deployment/my-app -n production
      
      - name: Verify deployment
        run: |
          kubectl get pods -n production
          kubectl get services -n production
```

## 보안 스캔 자동화

### 종합 보안 워크플로우

```yaml
# .github/workflows/security.yml
name: Security Scanning

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]
  schedule:
    # 매일 오전 2시에 실행
    - cron: '0 2 * * *'

jobs:
  sast:
    name: Static Application Security Testing
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Run Semgrep
        uses: returntocorp/semgrep-action@v1
        with:
          config: auto
      
      - name: CodeQL Analysis
        uses: github/codeql-action/init@v2
        with:
          languages: javascript, python, csharp
      
      - name: Autobuild
        uses: github/codeql-action/autobuild@v2
      
      - name: Perform CodeQL Analysis
        uses: github/codeql-action/analyze@v2
  
  dependency-scan:
    name: Dependency Vulnerability Scan
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Run Snyk
        uses: snyk/actions/node@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
        with:
          args: --severity-threshold=high
      
      - name: OWASP Dependency Check
        uses: dependency-check/Dependency-Check_Action@main
        with:
          project: 'My Project'
          path: '.'
          format: 'HTML'
  
  container-scan:
    name: Container Image Scan
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Build Docker image
        run: docker build -t myapp:test .
      
      - name: Scan with Trivy
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: 'myapp:test'
          format: 'sarif'
          output: 'trivy-results.sarif'
      
      - name: Upload Trivy results
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: 'trivy-results.sarif'
```

## 자동 릴리스 생성

### Semantic Release

```yaml
# .github/workflows/release.yml
name: Release

on:
  push:
    branches: [ main ]

jobs:
  release:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
          persist-credentials: false
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20.x'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Semantic Release
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          NPM_TOKEN: ${{ secrets.NPM_TOKEN }}
        run: npx semantic-release
```

```javascript
// release.config.js (Copilot이 생성)
module.exports = {
  branches: ['main'],
  plugins: [
    '@semantic-release/commit-analyzer',
    '@semantic-release/release-notes-generator',
    '@semantic-release/changelog',
    '@semantic-release/npm',
    '@semantic-release/github',
    [
      '@semantic-release/git',
      {
        assets: ['package.json', 'CHANGELOG.md'],
        message: 'chore(release): ${nextRelease.version} [skip ci]\n\n${nextRelease.notes}'
      }
    ]
  ]
};
```

## 성능 테스트 자동화

```yaml
# .github/workflows/performance.yml
name: Performance Testing

on:
  pull_request:
    branches: [ main ]

jobs:
  lighthouse:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20.x'
      
      - name: Install and build
        run: |
          npm ci
          npm run build
      
      - name: Run Lighthouse CI
        run: |
          npm install -g @lhci/cli
          lhci autorun
        env:
          LHCI_GITHUB_APP_TOKEN: ${{ secrets.LHCI_GITHUB_APP_TOKEN }}
  
  load-test:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Run k6 load test
        uses: grafana/k6-action@v0.3.0
        with:
          filename: tests/load-test.js
          cloud: true
          token: ${{ secrets.K6_CLOUD_TOKEN }}
```

## CI/CD 베스트 프랙티스

### 1. 빠른 피드백
```yaml
# 중요한 검사를 먼저 실행
jobs:
  quick-checks:
    runs-on: ubuntu-latest
    steps:
      - name: Lint
        run: npm run lint
      - name: Type check
        run: npm run type-check
  
  full-test:
    needs: quick-checks
    runs-on: ubuntu-latest
    steps:
      - name: Run all tests
        run: npm test
```

### 2. 캐싱 활용
```yaml
- name: Cache dependencies
  uses: actions/cache@v3
  with:
    path: ~/.npm
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-node-
```

### 3. 병렬 실행
```yaml
jobs:
  test:
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        node: [18, 20]
    runs-on: ${{ matrix.os }}
```

## 다음 단계

다음 섹션에서는 코딩 에이전트를 활용한 고급 자동화 기법을 학습합니다.

---

**참고 자료**
- [GitHub Actions 문서](https://docs.github.com/actions)
- [Azure DevOps 파이프라인](https://learn.microsoft.com/azure/devops/pipelines/)

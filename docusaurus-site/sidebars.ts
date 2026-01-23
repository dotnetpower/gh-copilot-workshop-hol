import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */
const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    'intro',
    {
      type: 'category',
      label: '🚀 GitHub Copilot 시작하기',
      items: [
        'steps/introduction',
        'steps/features',
        'steps/ai-models',
      ],
    },
    {
      type: 'category',
      label: '📚 기본 사용법',
      items: [
        'steps/basic-usage',
        'steps/limitations',
      ],
    },
    {
      type: 'category',
      label: '💡 Copilot 활용하기',
      items: [
        'steps/copilot-modes',
        'steps/impact',
      ],
    },
    {
      type: 'category',
      label: '🔧 고급 기능 및 실전',
      items: [
        'steps/advanced-features',
        'steps/real-project',
      ],
    },
    {
      type: 'category',
      label: '⚙️ 엔지니어링 프랙티스',
      items: [
        'steps/understanding-prompt',
        'steps/copilot-engineering-practices',
        'steps/custom-configuration',
        'steps/context-engineering',
      ],
    },
    {
      type: 'category',
      label: '🚀 Copilot Spaces & 협업',
      items: [
        'steps/copilot-spaces',
        'steps/vibe-coding',
      ],
    },
    {
      type: 'category',
      label: '🔄 리팩토링 & 자동화',
      items: [
        'steps/code-refactoring-deep',
        'steps/cicd-automation',
        'steps/coding-agents',
      ],
    },    
    {
      type: 'category',
      label: '🧪 실습',
      items: [
        'labs/lab1-code-completion',
        'labs/lab2-chat-quality',
        'labs/lab3-edit-agents',
        'labs/lab4-advanced',
        'labs/lab5-docusaurus-blog',
        'labs/lab6-autogen-group-chat',
        'labs/lab7-flight-delay-prediction',
      ],
    },
    {
      type: 'category',
      label: '🤖 Awesome GitHub Copilot',
      items: [
        'awesome/intro',
        'awesome/agents',
        'awesome/prompts',
        'awesome/instructions',
        'awesome/skills',
        'awesome/collections',
      ],
    },
    {
      type: 'doc',
      id: 'steps/workshop-conclusion',
      label: '🏁 워크숍 결론'
    },
  ],
};

export default sidebars;

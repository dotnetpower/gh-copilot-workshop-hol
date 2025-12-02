import type {ReactNode} from 'react';
import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

type FeatureItem = {
  title: string;
  Svg?: React.ComponentType<React.ComponentProps<'svg'>>;
  Img?: string;
  description: ReactNode;
  emoji?: string;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'AI 페어 프로그래밍',
    emoji: '🤖',
    description: (
      <>
        GitHub Copilot과 함께 코드를 작성하세요. 
        실시간 코드 제안으로 개발 속도를 2배 이상 향상시킬 수 있습니다.
      </>
    ),
  },
  {
    title: 'Ask, Edit, Agent 모드',
    emoji: '💬',
    description: (
      <>
        Ask로 빠른 질문, Edit로 정확한 수정, Agent로 자동화된 구현까지.
        상황에 맞는 모드를 선택하여 효율적으로 작업하세요.
      </>
    ),
  },
  {
    title: '생산성 극대화',
    emoji: '🚀',
    description: (
      <>
        반복 작업 자동화, 테스트 생성, 문서화까지.
        더 창의적인 작업에 집중할 수 있습니다.
      </>
    ),
  },
  {
    title: '프롬프트 엔지니어링',
    emoji: '🎯',
    description: (
      <>
        효과적인 프롬프트 작성으로 원하는 결과를 정확하게 얻으세요.
        Zero-shot, Few-shot, Chain-of-Thought 기법을 학습합니다.
      </>
    ),
  },
  {
    title: '실전 프로젝트',
    emoji: '🔧',
    description: (
      <>
        실제 프로젝트에서 Copilot을 활용하는 방법을 배웁니다.
        리팩토링, CI/CD, 협업까지 모든 것을 다룹니다.
      </>
    ),
  },
  {
    title: '체계적인 학습',
    emoji: '📚',
    description: (
      <>
        기초부터 고급까지 단계별로 학습합니다.
        실습을 통해 직접 경험하며 마스터하세요.
      </>
    ),
  },
];

function Feature({title, emoji, description}: FeatureItem) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center padding-top--md">
        <span className={styles.featureEmoji}>{emoji}</span>
      </div>
      <div className="text--center padding-horiz--md padding-bottom--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="text--center padding-bottom--xl">
          <Heading as="h2" className={styles.featuresTitle}>
            ✨ 워크샵 특징
          </Heading>
          <p className={styles.featuresSubtitle}>
            GitHub Copilot을 제대로 활용하는 방법을 배워보세요
          </p>
        </div>
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}

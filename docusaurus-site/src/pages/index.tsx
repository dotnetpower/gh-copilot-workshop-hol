import type {ReactNode} from 'react';
import {useState} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import useBaseUrl from '@docusaurus/useBaseUrl';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';
import Heading from '@theme/Heading';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  const videoUrl = useBaseUrl('/assets/20251229-120324-sora.webm');
  const [showPrompt, setShowPrompt] = useState(false);
  return (
    <header className={clsx('hero', styles.heroBanner)}>
      {/* <div className={styles.heroBackground}></div> */}
      <div className="container" style={{position: 'relative', zIndex: 1}}>
        <button 
          className={styles.promptButton}
          onClick={() => setShowPrompt(true)}
        >
          📝 Sora2 - Prompt
        </button>
        <video 
          className={styles.heroVideo}
          autoPlay 
          loop 
          muted 
          playsInline
        >
          <source src={videoUrl} type="video/webm" />
        </video>
        {showPrompt && (
          <div className={styles.promptOverlay} onClick={() => setShowPrompt(false)}>
            <div className={styles.promptModal} onClick={(e) => e.stopPropagation()}>
              <button 
                className={styles.closeButton}
                onClick={() => setShowPrompt(false)}
              >
                ✕
              </button>
              <h2>Sora2 - Prompt</h2>
              <div className={styles.promptContent}>
                <pre>
{`

## 1) 장면 전체 컨텍스트

* **배경**: 고대 석조 성채의 붕괴된 성벽과 잔해. 거친 회색 돌과 균열, 부서진 벽체가 전투의 긴박함을 강조.
* **시간/조명**: 맑은 낮, 차가운 자연광. 금속 표면에서 날카로운 하이라이트가 반사됨.
* **분위기**: 근접 전투의 순간 포착. 금속 충돌로 **불꽃과 파편**이 튀며, 공기 중에 긴장감과 폭발적인 에너지가 감돌음.
* **카메라 감각(권장)**: 로우 앵글에 가까운 중근접 샷, 빠른 셔터의 스틸 느낌. 슬로모션으로 불꽃이 튀는 순간을 강조해도 좋음.

---

## 2) 전사(인간)의 특징 — “노련한 중세 전사”

* **체형/자세**: 평균 이상 체격, 단단한 근육질. 몸을 낮추고 상대의 공격을 막아내는 **방어-반격 전환 동작**.
* **얼굴/머리**: 검은 머리카락이 얼굴을 부분적으로 가림. 표정은 집중과 결의가 섞인 냉정함.
* **장비**

  * **검**: 한손 장검. 날은 은회색, 사용 흔적이 있는 매트한 금속 질감. 몬스터의 공격을 받아내며 스파크가 발생.
  * **방패**: 둥근 방패. 중앙이 움푹 들어간 보스(Boss)가 있으며, 긁힘과 타격 자국이 다수.
  * **갑옷**: 가죽과 금속이 혼합된 중갑. 어깨에는 금속 견갑, 팔과 몸통에는 가죽 스트랩과 스터드 장식. 실전형, 과장되지 않은 현실적 디자인.
* **의상 디테일**: 어두운 색조(회색·갈색). 전투로 인한 먼지와 마모 표현.
* **무드**: 침착, 노련함, 생존을 위한 냉정한 판단.

---

## 3) 몬스터의 특징 — “사슴 머리의 수인 전사”

* **체형/자세**: 인간보다 훨씬 크고 육중한 체구. 상체를 비틀어 강력한 **내리찍기 공격**을 시도하는 순간.
* **머리/얼굴**

  * **사슴 머리**: 거대한 뿔이 좌우로 뻗어 있으며, 뿔에는 **붉은 천 리본**이 감겨 전투 중 휘날림.
  * **표정**: 포식자의 냉혹함. 눈빛은 차갑고 위협적.
  * **수염/털**: 얼굴과 목 주변에 거친 갈색 털.
* **장비**

  * **무기**: 두꺼운 장검 또는 중검. 타격 시 엄청난 힘이 느껴지는 묵직한 금속 질감.
  * **방어구**: 판금과 가죽 혼합. 인간 전사보다 더 장식적이며 상징적인 문양.
* **의상/상징**

  * **붉은 망토/깃발 요소**: 황금 문양이 새겨진 붉은 천이 어깨나 등 뒤에서 펄럭임. 전장의 지배자 같은 위엄.
  * **허리 장식**: 노란색 천 조각이 움직임에 따라 흔들림.
* **무드**: 압도적 힘, 야성, 고대의 수호자 혹은 침략자 같은 존재감.

---

## 4) 상호작용 디테일 (비디오화 포인트)

* **충돌 순간**: 검과 방패가 맞부딪히며 **불꽃 스파크**가 사방으로 튐.
* **물리감**: 몬스터의 공격은 무겁고 느리지만 파괴적, 전사의 방어는 빠르고 정교.
* **천/리본의 움직임**: 몬스터의 붉은 리본과 망토가 바람과 충격에 따라 크게 휘날림.
* **카메라 연출**:

  * 충돌 순간 슬로모션 → 스파크와 금속 마찰음 강조
  * 이후 미세한 카메라 흔들림으로 타격의 무게감 표현

---

## 5) 스타일 키워드 (AI 이해용)

* **Genre**: Dark Fantasy, Medieval Combat
* **Visual Style**: Realistic, cinematic, high-detail textures
* **Motion**: Slow-motion impact, cloth simulation, metal sparks
* **Tone**: Gritty, intense, epic duel

`}
                </pre>
              </div>
            </div>
          </div>
        )}
        <div className={styles.heroContent}>
          <span className={styles.heroEmoji}>🤖</span>
          <Heading as="h1" className="hero__title" style={{color: '#ffffff'}}>
            {siteConfig.title}
          </Heading>
          <p className={clsx('hero__subtitle', styles.heroSubtitle)}>
            {siteConfig.tagline}
          </p>
          <p className={styles.heroDescription}>
            AI 페어 프로그래밍의 새로운 시대, GitHub Copilot과 함께 시작하세요
          </p>
          <div className={styles.buttons}>
            <Link
              className="button button--primary button--lg"
              to="/docs/intro">
              워크샵 시작하기 🚀
            </Link>
            <Link
              className="button button--secondary button--lg margin-left--md"
              to="/docs/labs/lab1-code-completion">
              실습 바로가기 💻
            </Link>
          </div>
        </div>
      </div>
    </header>
  );
}

export default function Home(): ReactNode {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Hello from ${siteConfig.title}`}
      description="Description will go into a meta tag in <head />">
      <HomepageHeader />
      <main>
        <HomepageFeatures />
      </main>
    </Layout>
  );
}

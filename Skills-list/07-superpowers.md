# 07 superpowers — 일하는 순서 잡기

**쓰는 일:** 기획 ●  개발 ●  디자인 ○

부르는 법: 상황이 맞으면 자동. 직접 부르려면 `/superpowers:(이름)`

## 상황별
| 상황 | 기능 | 이렇게 말하기 |
|---|---|---|
| 아이디어가 막연할 때, 새 기능 기획 | brainstorming (아이디어 정리) | `/superpowers:brainstorming 회원 전용 리포트 기능` |
| 요구사항이 정해졌고 작업 순서가 필요할 때 | writing-plans (계획 쓰기) | `/superpowers:writing-plans` |
| 계획대로 직접 하나씩 실행 | executing-plans | `/superpowers:executing-plans` |
| 계획의 독립 작업들을 여러 도우미에게 나눠 실행 | subagent-driven-development | `/superpowers:subagent-driven-development` |
| 서로 상관없는 일 2개 이상을 동시에 | dispatching-parallel-agents | "이 세 가지 동시에 진행해줘" |
| 오류·이상한 동작 | systematic-debugging (원인부터 찾기) | `/superpowers:systematic-debugging 버튼 눌러도 반응 없음` |
| 기능 만들기 전 확인 장치(테스트) 먼저 | test-driven-development | `/superpowers:test-driven-development` |
| "다 됐다" 말하기 전 실제 확인 | verification-before-completion | 자동 |
| 작업이 끝나 점검 받고 싶을 때 | requesting-code-review | `/superpowers:requesting-code-review` |
| 점검 의견을 받았을 때 따질 건 따지기 | receiving-code-review | `/superpowers:receiving-code-review` |
| 원본을 건드리지 않는 별도 작업 공간 | using-git-worktrees | `/superpowers:using-git-worktrees` |
| 작업 마무리(합치기·정리 결정) | finishing-a-development-branch | `/superpowers:finishing-a-development-branch` |
| 나만의 스킬 만들기 | writing-skills | `/superpowers:writing-skills` |
| superpowers가 이상하게 굴 때 원인 보기 | diagnosing-superpowers | `/superpowers:diagnosing-superpowers` |

## 흐름 예 (웹 기능 하나 만들기)
brainstorming → writing-plans → (진행) → subagent-driven-development 또는 executing-plans → systematic-debugging(오류 시) → verification → requesting-code-review → finishing

## 주의
- 사용자 규칙이 먼저: 큰 일은 계획 보여주고 "진행" 뒤 실행, 커밋은 "cmt"일 때만
- brainstorming은 질문이 많아질 수 있음 → "질문은 최소로"라고 덧붙이면 됨

## 같이 쓰면 좋은 스킬
- [08 ponytail](08-ponytail.md), [09 karpathy](09-karpathy.md), [12 기본 명령](12-기본-명령.md)

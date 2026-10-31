# 02 impeccable — 화면 디자인 점검·다듬기

**쓰는 일:** 디자인 ●  개발 ●(화면 코드)  기획 ○(화면 구성 잡기)

부르는 법: `/impeccable (명령) (대상)` · 명령 없이 `/impeccable`만 치면 상황에 맞는 메뉴를 보여줌

## 명령어
| 명령 | 언제 | 예시 |
|---|---|---|
| `shape` | 만들기 전에 화면 구성부터 잡을 때 | `/impeccable shape 회원가입 화면` |
| `init` | 프로젝트 성격(누가·왜 쓰는지)을 처음 적어 둘 때 | `/impeccable init` |
| `document` | 지금 코드의 디자인 규칙을 문서(DESIGN.md)로 뽑을 때 | `/impeccable document` |
| `critique` | 디자인 평가를 점수로 받고 싶을 때 | `/impeccable critique 서비스소개 페이지` |
| `audit` | 접근성·속도·반응형 등 기술 점검 | `/impeccable audit index.html` |
| `polish` | 내보내기 직전 마지막 다듬기 | `/impeccable polish` |
| `bolder` | 밋밋하다 → 키우기 | `/impeccable bolder 첫 화면` |
| `quieter` | 너무 요란하다 → 줄이기 | `/impeccable quieter` |
| `distill` | 복잡하다 → 핵심만 남기기 | `/impeccable distill 설정 화면` |
| `layout` | 간격·정렬·위계 정리 | `/impeccable layout` |
| `typeset` | 글자 크기·굵기 체계 정리 | `/impeccable typeset` |
| `colorize` | 색이 너무 없을 때 포인트 색 넣기 | `/impeccable colorize` |
| `animate` | 의미 있는 움직임 넣기 | `/impeccable animate 버튼` |
| `delight` | 기억에 남는 작은 재미 | `/impeccable delight` |
| `clarify` | 버튼 문구·오류 문구 다듬기 | `/impeccable clarify 결제 화면` |
| `onboard` | 첫 사용 안내·빈 화면 디자인 | `/impeccable onboard` |
| `harden` | 오류·긴 글자·예외 상황 대비 | `/impeccable harden` |
| `adapt` | 모바일·태블릿 대응 | `/impeccable adapt` |
| `optimize` | 화면이 느릴 때 | `/impeccable optimize` |
| `extract` | 반복되는 부품을 디자인시스템으로 | `/impeccable extract` |
| `live` / `generate` | 브라우저에서 요소를 골라 여러 안 비교 | `/impeccable live` |
| `overdrive` | 평범함을 넘는 과감한 효과 | `/impeccable overdrive` |

## 이 프로젝트에서 써 본 예
- 1차 A안(다듬기), 2차 A2(bolder), 3차 ①안(위계 정리) — ①안이 사용자 수정본의 바탕이 됨

## 주의
- 기본은 웹 코드용. 피그마에서는 "진단·방향"으로 쓰고 실제 수정은 figma로
- 기존 정체성을 지키는 "다듬기"와 갈아엎는 "리디자인"을 구분함 → 원하는 쪽을 말하기

## 같이 쓰면 좋은 스킬
- [04 ui-ux-pro-max](04-ui-ux-pro-max.md)(쓰기 편함 규칙), [06 hallmark](06-hallmark.md)(AI 티 점검)

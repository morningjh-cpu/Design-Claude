# 08 ponytail — 코드를 최소한으로

**쓰는 일:** 개발 ●

부르는 법: 기본으로 자동 켜짐(단, **이 디자인 폴더에서는 꺼짐**). 켜기 `/ponytail`

## 명령어
| 명령 | 언제 |
|---|---|
| `/ponytail lite` | 시킨 대로 만들되, 더 작은 방법이 있으면 한 줄 알려줌 |
| `/ponytail` | 기본. 가장 작은 변경 + 빠뜨린 일·위험 알려줌 |
| `/ponytail ultra` | 만들기 전에 "정말 필요한가"부터 따짐 |
| `/ponytail-review` | 방금 고친 코드 점검(오류·보안·많이 쓸 때·빠진 테스트·지울 것) |
| `/ponytail-audit` | 프로젝트 전체 점검, 중요한 순 |
| `/ponytail-debt` | 미뤄 둔 곳(`shortcut:` 표시) 목록 |
| `/ponytail-gain` | 아낀 양 보기 |
| `/ponytail-help` | 안내 카드 |
| "stop ponytail" / `/ponytail off` | 끄기 |
| `/ponytail band` | 입력창 위 안내 줄 숨기기/보이기 |

## 언제 좋은가
- "간단히 하면 될 걸 복잡하게 만든다" 싶을 때
- 남이 짠 코드에 군더더기가 많은지 볼 때 → `/ponytail-audit`

## 주의
- 이 폴더 꺼짐 설정: `.claude/settings.json`의 `PONYTAIL_DEFAULT_MODE: off`

## 같이 쓰면 좋은 스킬
- [09 karpathy](09-karpathy.md)(비슷한 지침), [12 기본 명령](12-기본-명령.md)의 `/simplify`

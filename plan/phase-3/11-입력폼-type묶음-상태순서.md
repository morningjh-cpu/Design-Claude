# 11. 입력폼 부품 모습 — type 별 묶음 · 상태 순서 (2026-11-17)

파일 `jey6PXIFB19gl5et1XzIzi` · 페이지 `📘 부품 설명` · 구역 `4. 입력 / 입력`(16021:149).
사용자: "부품 설명 / home-search-bar 에 있는걸 수정해봤어. 부품 모습을 type 별로 그룹을 만들어서 보여주는게 좋겠어. 그리고 입력폼의 경우 상태 순서를 default, hover, focused, typing, typed, disabled, error 로 하는 것이 좋을 것 같은데"

## 사용자가 직접 고친 것 (본보기)
- home-search-bar(16021:162): 부품 모습 상자 안에 type 이름 틀(`home-search` · `snb-search`)을 만들고 그 안에 상태 순서대로 세로로 쌓음. 묶음 사이 40, 묶음 안 20. 이름표 글자 없음.
- service-search-bar(16021:845)도 이미 묶음 4개(`main` · `sub` · `main-show-chip` · `sub-show-chip`)로 나뉘어 있었음.

## 한 것
- input-base(16021:408): 같은 짜임으로 묶음 2개.
  - `text-field` 13개: default · focused · typing · typed · disabled · error · error-placeholder · drag · validation-default · validation-typing · validation-typed · validation-typed-done · validation-error
  - `pw-field` 9개: default · focused · typing · typing-open · typed · typed-open · disabled · error · validation-typed-done
- 3. 상태 표 줄 순서를 같은 순서로 맞춤: home-search-bar · input-base · service-search-bar 3장.
- 순서 규칙(뒤쪽은 AI 판단): 사용자가 정한 7개 순서가 먼저. `typing-open` 처럼 뒤에 말이 붙은 상태는 원래 상태 바로 뒤. `drag` 처럼 목록에 없는 것은 그 뒤. `validation-…` 은 맨 뒤에서 같은 순서.

## 안 한 것
- service-search-bar 의 부품 모습 순서는 손대지 않음. show-chip 두 묶음은 typed 가 맨 앞(typed · hover · focused · typing …)이라 규칙과 다름 — 사용자가 놓은 것일 수 있어 그대로 둠.
- 묶음 이름표(글자)는 안 붙임(사용자 본보기에 없음).
- `4. 입력 / 선택` 17장과 패턴 쪽 입력 문서는 그대로.

## show-chip 두 묶음 순서 맞춤 (2026-11-17)
사용자: "show-chip 두 묶음도 typed를 뒤로 보내 순서를 맞추는게 맞음, 이렇게 배치한 이유는 default 상태가, show-chip 이 없는 기본 상태와 같아서 였어."
- `main-show-chip`: typed · hover · focused · typing · typed-max → hover · focused · typing · typed · typed-max
- `sub-show-chip`: typed · hover · focused · typing → hover · focused · typing · typed
- `main` · `sub` 묶음은 이미 순서가 맞아 그대로.
- 알아둘 것(사용자 설명): show-chip 묶음에는 default 가 없음 — show-chip 이 없는 기본 상태와 같아서.

## 확인
- input-base 인스턴스 22개 그대로, 상자 밖에 남은 것 0.
- 눈으로 본 것: input-base 부품 모습 한 장.

# 18 간격 가까운 값으로 맞추기 · name 칸 정리 — 2026-11-03

## 사용자 말
- "2 간격 값은 가까운 값으로 맞춰. 3 개발쪽 신경쓰지말고 제안대로 진행. 4 비활성은 필요가 없어서 안만든거니까 자꾸 언급하지마."
  - 4 → 앞으로 비활성 없음을 남은 문제로 꺼내지 않음 (memory 에도 적음)

## name 칸 정리 (공통 컴포넌트 구역)
- 값이 하나뿐인 `name` 종류 칸을 90세트에서 지움 (종류 이름 "name=…, " 부분 빼기 → 화면 연결 그대로)
- 남은 5: arrow-folter-down (값 2개: arrow-folter-down/arrow-bar-to-up → 진짜 종류라 둠), icon·logo-wise·symbol-fnguide-logo·symbol-isms (종류 칸이 name 하나뿐인 낱개)
- 부품 설명에서 "name 칸 값이 …" · "비활성 상태 없음" 문구 지움 (9개)

## 간격 맞추기 (공통 컴포넌트 구역, 아이콘·로고 구역 제외 — 아이콘 모양 보호)
- 규칙: 0·2·4·6·8·10·12·14·16·20·24·32·40 중 가장 가까운 값, 같은 거리면 작은 쪽, 0이 되는 경우는 2
- 1,171곳 저장값 연결 (그중 값이 바뀐 곳 1,135)
  - 5→4 318 · 6.67→6 317 · 3→2 297 · 7→6 52 · 1→2 43 · 13.33→14 30 · 30→32 27 · 18→16 21 · 13→12 8 · 9→8 8 · 그 외 소수
- 안 바꿈: 음수 -1 (19곳, 겹치기용) · 40 넘는 값 44·98·140 (5곳)
- 화면 캡처로 segment-filter-fixable · box-date-select · btn-ot-tertiary · input-select 확인 — 깨짐 없음, 조금 촘촘해짐

## name 칸 되돌림 (사용자: "값이 하나뿐인 name 칸은 일부러 한거 … 클로드가 해당 컴포넌트를 식별하기 편하게 … 없앤거는 원래대로 복구하고 없는건 같은 규칙으로 네임을 넣어줘")
- 지웠던 90세트: 백업 파일(원본, 읽기만)의 같은 부품 값과 자리 그대로 되살림 (예: btn-fill-tertiary=btn-fill-secondary, btn-login=filter-reset, menu-ui-icon=gnb-icon, 아이콘은 icon/ 뺀 이름)
- 원래 없던 26세트에 name 추가: 값 = 세트 이름 마지막 부분, 맨 앞 자리 (input-base, checkbox, radio, switch, cell-data, tag-basic, dialog, tooltip, title …)
- 낱개 부품 9개(종류 칸 없음: text-label, tab-solid, unit-text 등)는 종류 칸을 만들려면 묶음으로 바꿔야 해서 안 함

## name 값이 여러 개인 세트 → 1개 (사용자 "네임 값은 많은 것은 1개만 남겨줘")
- menu/menu-right-content: 망가진 종류 3개(name=menu, Property 3~8)를 name=menu-right-content, type=analyst-search / -typing / -none 로 (anlyst 철자 고침) → 쓸데없는 칸 6개 없어짐
- keyword-list: name=keyword-list 하나로, 구분은 type=keyword-list / favorite-add-title 로 옮김
- searchbar-keyword-new: name=searchbar-keyword 하나로 (type 으로 이미 구분)
- arrow-folter-down: name=arrow-folter-down 하나로 (status 로 이미 구분)

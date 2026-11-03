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

## 모서리 연결 (점검 3차 뒤 사용자 "제안대로 진행해")
- 공통 컴포넌트 구역: 완전히 둥근 모양(모서리 ≥ 짧은 변의 절반, 값 > 24) → radius-full 167곳 (50 88 · 99 65 · 1000 8 · 81 6) — 모양 그대로
- 나머지는 가까운 값으로 맞춰 연결 46곳 (5→4 22 · 3→2 9 · 1→2 7 · 13→12 3 · 7→6 3 · 10.91→10 2), 같은 거리면 작은 쪽, 0 이 되면 2
- 아이콘·로고 구역은 완전히 둥근 것만 연결, 나머지 소수 값(1·3·9·4.79·0.44·14.4 등) 그대로 → 보이는 레이어 기준 남은 직접 모서리 26곳 모두 아이콘 안
- ic-gr: 이제 남은 곳 없음. icon/file 의 Icon 선은 사용자가 ic-ui(이 파일)로 연결해 둔 상태

## 낱개 부품 9개에 name 칸 (사용자 "낱개 부품 9개의 name칸 같은 이름으로 채워")
- 낱개 부품을 종류 1개짜리 묶음으로 바꾸고 종류 이름 = name=<부품 이름 마지막 부분>, 묶음 이름·위치·설명은 원래대로
- text-tooltip/best-analyst(name=best-analyst) · tag-best-analyst · text-label · dialog-header/dialog-body(name=dialog-body) · tab-solid · Icon/lock-report(name=lock-report) · wise-nodata · 🔽 · unit-text
- 확인: 부품 속성(tab-solid 의 Tab 3~6 켜고 끄기) 그대로, 화면에 놓인 부품 수 그대로 (안 맞으면 전부 되돌리게 해 둠)
- 공통 컴포넌트 구역 묶음 130개 모두 name 값 1개

## 간격 3 추가 (사용자 "간격 조정한 것에 수치 3을 넣어주도록해주고, 이전 피그마파일에서 간격이 3이었던 것들을 찾아서 적용해줘")
- 저장값 `spacing/space-3` = 3 새로 만듦 (쓰임: 간격, 개발 이름 var(--space-3))
- 공통 컴포넌트 구역에서 space-2 에 연결된 368곳을 백업 파일(읽기만)과 비교 → 백업에서 3이던 125곳(칸 213개)을 space-3 으로 다시 연결
  - 부품: segment-filter-fixable · segment-filter-size · switch · scroll-bar · tooltip · menu-ui-icon · menu/menu-left · menu/menu-right
  - 부품 속 겹친 부품 20곳은 원본을 따라 자동으로 3 이 됨
- 백업에서 원래 2·1·0 이던 곳은 그대로 2
- 백업에 없는 새 레이어 7개는 비교 못 함: checkbox hover 3개, switch xs hover 2개(14022:10003·10005 — 옆 switch xs 는 백업에서 위아래 3), dropdown-list-box 2개

## 백업과 높이 비교 (사용자 "이전 컴포넌트와 간격 조정된 컴포넌트에 height 값이 다른 컴포넌트가 얼마나 되는지 찾아봐") — 읽기만
- 공통 컴포넌트 구역 종류 679개 비교 (크기만 있는 아이콘·로고는 간격을 안 건드려서 뺌), 백업에 없는 새 종류 17개는 비교 못 함
- 높이 다름 16개 / 부품 8개 (백업 → 지금): dropdown-list-box 233→238·243→249 · cell-data 46→45·64→63 · tag-keywords sm 26→24 (4) · dialog 184→183·147→146 · message-area 85→87·172→174·114→116 · modal-header confirm 60→56 · footer-area default 94→110
- 너비 다름 12개 / 부품 5개: btn-uiform 145→141 · box-date-select 272→273 (5) · date-label 54→55 · input-select 230→228 (3) · check-list 63→65

## 높이 원래대로 (사용자 "message-area와 dialog를 제외하고 원래 수치로 변경해줘. height를 hug가 아닌 fix 값으로")
- 11개를 백업 높이로, 세로 크기 방식 내용 맞춤 → 고정: dropdown-list-box 3 (238→233·238→233·249→243) · cell-data 2 (45→46·63→64) · tag-keywords sm 4 (24→26) · modal-header confirm (56→60) · footer-area default (110→94)
- 가로 크기 방식은 그대로 둠 (tag-keywords 는 가로 내용 맞춤 유지)
- message-area 3 · dialog 2 는 그대로 (사용자)
- 너비 다른 12개는 찾기만 함 (위 표)

## 너비 원래대로 (사용자 "너비도 원래 수치로 고정해줘")
- 12개를 백업 너비로, 가로 크기 방식 내용 맞춤 → 고정: box-date-select 5 (273→272) · input-select 3 (228→230) · btn-uiform 2 (141→145) · date-label (55→54) · check-list 1 (65→63, 6786:5034)
- 세로 크기 방식은 그대로

## 간격 18 추가 (사용자 "간격에 18과 20이 없어서 생긴거면 간격에 추가해주고, 영향 받았던 너비 값은 간격 적용해서 원래 값과 동일하면 fix를 hug로")
- 20 은 이미 있음(space-20) → `spacing/space-18` = 18 만 새로 만듦
- 공통 컴포넌트 구역 space-16 연결 169곳 중 백업에서 18 이던 14곳(21칸) → space-18: btn-ot-primary · btn-uiform · input-select · modal-header(아래 여백) · footer-area(위아래)
- 너비 12개: 내용 맞춤으로 바꿔 원래 너비와 같은 10개는 내용 맞춤 — box-date-select 5 (272) · input-select 3 (230) · btn-uiform 2 (145)
- 고정 유지 2개 (간격 1·30 이 원인이라 내용 맞춤이면 달라짐): date-label 54 (내용맞춤이면 55) · check-list 63 (65)

## 높이 내용 맞춤 시도 (사용자 "높이도 원래 값과 같으면 hug로 바꿔줘")
- 11개 모두 내용 맞춤이면 원래와 달라서 고정 유지: dropdown-list-box 233·233·243 (내용맞춤 238·238·249) · cell-data 46·64 (45·63) · tag-keywords 26 ×4 (24) · modal-header 60 (56) · footer-area 94 (114)

## 높이 차이 원인 (백업 → 지금)
- dropdown-list-box 줄 사이 1→2 (+5) · cell-data 위 13→12 · tag-keywords sm 위아래 5→4 · modal-header confirm 위 36→32
- footer-area default: 안에 든 footer(home) 부품의 copyright 위 여백이 0→20 으로 덮어써져 있었음 (맞추기 작업 때문 아님)

## footer copyright 위 여백 0 (사용자 "footer copyright 위 여백 0으로 되돌려줘")
- footer-area type=default 안 copyright 위 여백 → 0 (space-0 연결). type=home 원본은 20 그대로
- 높이가 내용 맞춤으로 94 (원래와 같음) → 세로 내용 맞춤으로 바꿈

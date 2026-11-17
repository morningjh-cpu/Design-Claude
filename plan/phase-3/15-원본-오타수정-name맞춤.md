# 15. 원본 파일 — 오타 수정 · name 값 맞춤만 (2026-11-17)

파일 `HxECyUsoLnDxoSWSKophQn`(원본). 사용자: "디자인시스템 적용하려던 원본 파일인데, 아직 적용하지 말고 오타났던 부분과 name 일치하는 작업만 진행해줘."

13번 방안의 2단계 중 ㄴ(name 값 맞춤) · ㄷ(부품 이름 오타) · ㄹ(칸 이름 오타)만 함. 구조(6묶음) · 문서 · 합치기는 안 함.
부품 번호는 그대로라 화면 쪽 연결은 유지됨(화면 페이지를 하나씩 확인하지는 않음).

## 부품 이름 6개
- `menu/menu-leftt-content`(4263:17992) → `menu/menu-left-content`
- `txet-btn`(5306:11847) → `text-btn`
- `anlysis-info`(9841:124609) → `analysis-info`
- `icon/symbol-aothor-house`(4142:7851) → `icon/symbol-author-house`
- `arrow-folter-down`(6324:40663) → `arrow-filter-down`
- `Component`(7216:82201) → `symbol-box` — 오타는 아니지만 name 값을 맞추려면 이름이 필요해 테스트 때 사용자 결정대로 함

## 종류 칸 이름 7곳
- `stste` → `state`: text-btn · symbol-box
- `staet` → `state`: back-btn(6054:58711)
- `stete` → `state`: menu/menu-report-list(4514:13749)
- `stae` → `state`: event-chip(8672:8145)
- `namr` → `name`: chart-box(7035:36349)
- `stichy` → `sticky`: comp-search(14273:16061)

## name 값 맞춤 23묶음 (옛 값 → 새 값 = 부품 이름 마지막 토막)
- menu/menu-left-content: menu-leftt-content → menu-left-content (7)
- menu/ui-icon-favorite(14273:36035): menu/ui-icon-favorite → ui-icon-favorite (3) — 테스트 때 없던 것, 빗금 규칙대로
- symbol-box: symbol → symbol-box (2)
- condition-folding: filter-reset → condition-folding (8)
- searchbar-keyword-new: searchbar-keyword → searchbar-keyword-new (4)
- condition-item-all: condition-item → condition-item-all (2)
- service-tag(10. 부가정보 쪽, 9653:82901): IPO-tag → service-tag (7)
- analysis-info: sector-anaysis → analysis-info (2)
- btn-fill-tertiary: btn-fill-secondary → btn-fill-tertiary (15)
- btn-login: filter-reset → btn-login (2)
- dropdown-list(공통, 4957:849): select-list → dropdown-list (16)
- dropdown-list-box: select-list-box → dropdown-list-box (3)
- dropdown-ui-list: dropdown-list → dropdown-ui-list (20)
- segment-filter-fixable: segment-filter-new → segment-filter-fixable (20)
- segment-filter-size: segment-filter-new → segment-filter-size (20)
- ` menu-ui-icon`: gnb-icon → menu-ui-icon (3)
- footer-area: footer → footer-area (2)
- arrow-filter-down: arrow-folter-down → arrow-filter-down (4)
- icon: symbol-sector → icon (1)
- icon/spinner: ordering → spinner (3)
- icon/symbol-author-house: aothor-house → symbol-author-house (25)
- icon/symbol-etf: etf-symbol → symbol-etf (14)
- icon/symbol-stock: stock-symbol → symbol-stock (21)

## 확인
- name 칸이 있는 묶음 중 값이 부품 이름과 어긋난 곳 0. 종류 칸이 깨진 묶음 0 (묶음 219개 점검).
- 실행 전 버전 기록 이름 붙이기는 도구가 지원하지 않아 못 함 → 되돌리려면 피그마 버전 기록의 자동 저장분.

## 이름 2개 더 바꿈 (같은 날, 사용자: "차트버블, 드롭다운 리스트 정리만 해줘")
- 패턴 쪽 `bubble`(7729:7861) → `chart-bubble`
- 패턴 쪽 `dropdown-list`(4957:4005) → `search-dropdown-list`
- 이어서 사용자: "name칸에 넣어줘" → 두 묶음 종류 이름 맨 앞에 `name=묶음 이름` 넣음(chart-bubble 7종류 · search-dropdown-list 12종류). 종류 칸 깨짐 0. 같은 이름 묶음은 `service-tag` 1쌍만 남음. 아래 목록의 bubble · dropdown-list 는 이걸로 끝.

## 안 쓰는 부품 보관 (같은 날, 사용자: "옮겨줘")
- `dropdown-list-simple`(2012:2759, 4종류): 파일 전체에서 쓰는 곳 0(화면 쪽 · 부품 쪽 두 방법, 보관 페이지 포함) → `🗑 보관` 페이지로 옮김(x 14014, y 0).
- 원래 자리: `공통 컴포넌트 > 선택` 구역(14023:37692) x 2071, y 430.75 (크기 316×253). 그 자리는 비워 둠.
- 다른 파일에서 라이브러리로 쓰는지는 확인 못 함.

## td-first-text 의 horizontal 16종류 보관 (같은 날, 사용자: "horizontal 16종류 보관 페이지로 옮겨줘")
- `td-first-text`(8853:28542) 32종류 중 `type=horizontal` 16종류: 쓰는 곳 0(옮기기 직전 다시 확인) → `🗑 보관` 페이지에 새 묶음 `td-first-text (horizontal)`(14826:725, x 14530, y 0)으로 옮김. 종류 번호는 그대로.
- 남은 묶음: vertical 16종류. 묶음 틀 크기(696×248)는 그대로 두어 아래쪽(y 145~199 줄)이 비어 있음. `type` 칸은 값이 vertical 하나만 남음.
- 원래 좌표(묶음 틀 안, x·y): 되돌릴 때 새 묶음 안 좌표에 x+35, y+125 를 더하면 됨(새 묶음은 왼쪽 위 여백 20 으로 같은 배치를 유지).
- 참고: 이 묶음의 칸 이름은 사용자가 `horizontal-header` → `type`(vertical · horizontal)으로 바꿔 둔 상태였음. `cell-first` 도 `cell-tree` 로 바뀌어 있었음.

### 바로잡음 — 위 "쓰는 곳 0"은 틀렸음 (같은 날, selected 상태 조사하다 발견)
- 원인: 부품 쪽에서 쓰인 곳을 묻는 방법(getInstancesAsync)은 **다른 부품 안에 겹쳐 들어간 것을 화면에서 세지 못함**. 화면의 모든 인스턴스를 하나씩 확인하는 방법으로 다시 세니 다름.
- 다시 센 결과(보관 페이지 제외): td-first-text 전체 884곳. 그중 보관으로 옮긴 horizontal 묶음을 쓰는 곳 **64곳** — 5. 기업분석 46곳(스냅샷 6화면 각 6, 비즈니스 현황 3, 비즈니스 현황-리츠 7), 10. 부가정보 18곳(이벤트 일정 모달 7, IR 일정 모달 5, IPO 일정 6).
- 화면은 깨지지 않음(옮긴 종류의 번호가 그대로라 연결 유지). 다만 쓰이는 부품이 보관 페이지에 있는 상태.
- 보관 묶음(14826:725)의 종류 이름이 `=td-first-text, =default, …` 처럼 칸 이름이 빠져 보임 — 원인 확인 안 함.
- 그 사이 사용자가 원래 묶음을 고침: 지금 칸은 name · type(default · bold) · state(default · selected) · info · unit. 그래서 마음대로 되돌리지 않고 사용자에게 물음.
- `dropdown-list-simple` 은 겹친 것까지 세는 방법으로도 확인했으므로 0곳이 맞음.
- selected 상태를 쓰는 곳: 0곳(겹친 것 포함).
- 교훈: 쓰인 곳을 셀 때는 화면의 인스턴스를 하나씩 확인하는 방법을 쓴다.

### 되돌림 (같은 날, 사용자: "A 되돌려줘" → 구분 칸 이름은 `direction` 선택)
- horizontal 16종류를 원래 묶음 `td-first-text`(8853:28542)에 다시 넣음. 보관 페이지의 `td-first-text (horizontal)` 묶음은 비어서 없어짐. 종류 번호는 그대로(화면 64곳 연결 유지).
- 새 칸 `direction` 추가: 기존 16종류 = `vertical`, 되돌린 16종류 = `horizontal`. 지금 칸: name · type(default/bold) · state(default/selected) · info · unit · direction. 32종류, 이름 겹침 0, 칸 깨짐 0.
- 옛 값 → 새 값 짝(AI 추측, 화면 캡처로 확인: bold = 굵은 글자, selected = 보라색): accent=true → type=bold, hover → state=selected.
- 놓은 자리: 묶음 안 아래쪽(vertical 4줄 밑, 32 띄움). 묶음 높이 267 → 298, 너비 762 그대로.
- 묶음 틀이 오른쪽 `th-lines`(4321:16596)와 조금 겹침 — 되돌리기 전(762×267)에도 겹쳐 있던 것, 안 건드림.
- 주의: 다른 묶음의 종류를 appendChild 로 넣으면 그 순간 종류 이름이 틀어짐 → 넣은 뒤 번호 기준으로 이름을 다시 지정해야 함.

## 안 한 것 (요청 범위 밖)
- 같은 이름 묶음 3쌍 그대로: `service-tag` 2개(합치기 안 함), `bubble` 2개, `dropdown-list` 2개 — 테스트에서는 chart-bubble · search-dropdown-list 로 바꾸고 service-tag 는 type=ipo 로 합침.
- ` menu-ui-icon` 이름 앞 빈칸, `charge-type` 의 칸 이름 `Property 1`.
- name 칸이 없는 묶음에 name 칸 넣기.

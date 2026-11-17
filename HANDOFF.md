# HANDOFF — 이 파일은 clear 전에 항상 최신으로 덮어쓴다 (이 줄 포함)

기준: 2026-11-17 (마지막 작업: 회사 PC IMORNING02)

## 현재 상태
### 피그마 — 와이즈 컴포넌트 테스트 (파일 jey6PXIFB19gl5et1XzIzi, 디자인시스템 구조화 = phase-3)
- 방향(사용자 결정, 2026-11-13): 큰 틀은 KRDS(시작하기 / 디자인 스타일 / 컴포넌트 / 패턴), 부품 분류는 Ant Design 6묶음(일반 · 틀 · 탐색 · 입력 · 데이터 표시 · 피드백). 저장값·부품 이름은 안 바꿈 → plan/phase-3/01~03
- 2026-11-13 실행 끝: 패턴 139개를 6묶음 새 구역으로 전부 옮김(화면 번호 꼬리표 붙임, 옛 구역 14개는 보관 페이지), 공통 컴포넌트 132개는 기존 9묶음을 6묶음 구역 안에 넣음 → plan/phase-3/04
- 2026-11-13 새 페이지 `📍 시작하기`(16013:6)에 시작하기 안내 문서(16013:7)와 부품 설명 틀(16013:172, 빈 틀) 만듦 → plan/phase-3/05
- 2026-11-13 새 페이지 `📘 부품 설명`(16015:6)에 버튼 8개 설명 문서 만듦(사용 규칙 칸은 빈칸 — 사용자가 적을 것). 채우다 본 것: btn-fill-tertiary·btn-login 의 name 값이 부품 이름과 다름 등 → plan/phase-3/06
- 2026-11-13 name 값 고침(사용자 결정: name 값은 부품 이름과 같아야 함): btn-fill-tertiary 15종류, btn-login 2종류. 같은 어긋남이 다른 묶음 19곳에 더 있음(안 고침, 목록은 plan/phase-3/06)
- 2026-11-13 나머지도 맞춤: 15묶음 144종류. 남긴 4묶음 = txet-btn · anlysis-info(부품 이름 오타) · Component(임시 이름) · icon/symbol-aothor-house(둘 다 오타) → plan/phase-3/06
- 2026-11-13 오타 부품 이름 3개 고침(사용자 승인): txet-btn → text-btn, anlysis-info → analysis-info, icon/symbol-aothor-house → icon/symbol-author-house (name 값도 맞춤). 개발 쪽에 알려야 함
- 2026-11-13 `Component`(7216:82201) → `symbol-box` 로 이름·name 값 바꿈(사용자 선택). name 값 어긋난 묶음 0곳
- 2026-11-13 부품 설명 입력 3개 · 선택 17개 추가(같은 페이지, 구역 16021:149 · 16022:794). 지금 설명 문서 28장. 상태 뜻을 모르는 칸은 "—"로 둠 → plan/phase-3/07
- 2026-11-13 (사용자 퇴근, 자동 진행 승인) 부품 설명 나머지 전체 채움: 지금 구역 36개 · 문서 213장(공통 78 + 아이콘·로고 목록 1, 패턴 134. 작업용 표시 5개는 제외) → plan/phase-3/08
- 다음(사용자): 결과 확인 · 사용 규칙과 빈 상태 설명 적기 · 패턴 부품 용도 한 줄(135장 비어 있음) · 서체 바꾸기 플러그인 · 바뀐 부품 이름 4개 개발 쪽 전달 · 올리려면 "cmt"
- 2026-11-17 종류 칸 이름 오타 7곳 고침(stste·staet·stete·stae → state, namr → name, stichy → sticky), `menu/menu-leftt-content` → `menu/menu-left-content`. `service-tag` 2묶음을 1묶음으로 합침(부가정보 쪽 7종류 = `type=ipo`, 묶음 4012:2828 · 18종류) → plan/phase-3/09
- 2026-11-17 패턴 쪽 `bubble` → `chart-bubble`, `arrow-folter-down` → `arrow-filter-down` (사용자 결정) → plan/phase-3/09
- 2026-11-17 패턴 쪽 `dropdown-list` → `search-dropdown-list` (사용자 결정). 같은 이름 묶음 0쌍. chart-bubble · search-dropdown-list 에 name 칸도 넣음
- 2026-11-17 버튼 설명 문서 8장의 `부품 모습`을 격자로 다시 놓음(가로 = size, 세로 = state), 줄·칸 이름표도 붙임. 나머지 문서는 그대로 → plan/phase-3/10
- 2026-11-17 입력폼 규칙(사용자): 부품 모습은 type 별 묶음, 상태 순서는 default · hover · focused · typing · typed · disabled · error. 본보기 = 사용자가 고친 home-search-bar 문서. input-base 에 적용, 입력 3장의 상태 표 순서도 맞춤 → plan/phase-3/11
- 2026-11-17 service-search-bar 의 show-chip 두 묶음도 순서 맞춤(typed 를 뒤로). show-chip 묶음에 default 가 없는 건 기본 상태와 같아서(사용자 설명)
- 2026-11-17 선택 17장에도 적용(type 별 묶음 + 상태 순서 + 이름표). 넓은 4장(box-date-select · box-text-select · dropdown-ui-list · input-select)은 격자 대신 상태별 줄바꿈 나열 → plan/phase-3/12
- 2026-11-17 사용자: 테스트는 여기까지. 원본 파일 적용 방안 정리 → plan/phase-3/13 (추천 = 원본에서 단계별로 다시 실행: 0 준비·비교 → 1 구조 → 2 이름 정리 → 3 문서 → 4 마무리). 실행은 아직 안 함
- 멈춘 이유(사용자): 원본 파일에 부품이 계속 추가되는 중. 그래서 복사본을 원본으로 삼는 길은 뺌, 원본용 도구는 이름으로 찾게 짜야 함
- 2026-11-17 사용자 결정: 원본 작업 전까지 새 부품에는 정해진 규칙을 미리 씀 → plan/phase-3/14 (한 장 규칙)
- 이어서 할 때 붙여 넣을 문장: `디자인 일 하자. plan/phase-3/13 방안대로 디자인시스템을 원본 파일에 적용하려고 해. 원본 주소는 (링크), 이번엔 (0단계 비교만 / 1·3단계까지) 진행해줘.` — 새 부품 규칙이 헷갈릴 때는 `새 부품 규칙 보여줘`(plan/phase-3/14)
- 2026-11-17 **원본 파일(HxECyUsoLnDxoSWSKophQn)에 이름 정리만 먼저 함**(사용자: 적용은 아직, 오타·name 일치만): 부품 이름 6개 · 종류 칸 이름 7곳 · name 값 23묶음. 어긋난 곳 0. 구조·문서·합치기는 안 함 → plan/phase-3/15. 이어서 패턴 쪽 `bubble` → `chart-bubble`, `dropdown-list` → `search-dropdown-list` 도 바꾸고 name 칸도 넣음. 안 쓰는 `dropdown-list-simple`(쓰는 곳 0)은 보관 페이지로 옮김(원래 자리는 15번 파일). `td-first-text` 의 안 쓰는 horizontal 16종류도 보관 페이지에 `td-first-text (horizontal)` 묶음으로 옮김. **바로잡음: "안 쓰는"은 틀렸음 — 화면 64곳(5. 기업분석 46, 10. 부가정보 18)이 그 horizontal 을 쓰고 있음**(겹쳐 들어간 것을 못 센 탓, 화면은 안 깨짐). → 사용자 결정으로 원래 묶음에 되돌림: 새 칸 `direction`(vertical · horizontal) 추가, 지금 32종류(name · type · state · info · unit · direction), 보관 쪽 묶음은 없어짐 → plan/phase-3/15. 교훈: 쓰인 곳은 화면 인스턴스를 하나씩 확인해서 셀 것(getInstancesAsync 는 겹친 것을 놓침). 원본에 남은 것: 같은 이름 1쌍(service-tag), ` menu-ui-icon` 앞 빈칸, charge-type `Property 1`. 개발 쪽 전달 필요
- 다음(사용자가 정할 것): 원본 작업 시점 · 원본 파일 주소 · 이름 정리 시점 · AI 가 정한 규칙 5가지 그대로 쓸지
- (테스트 파일에 남은 것) 입력 3장(home-search-bar 등) 묶음에 이름표를 붙일지, 선택 17장·패턴 쪽에도 넓힐지. 격자 정렬을 다른 문서에도 할지. ` menu-ui-icon` 이름 앞 빈칸, `charge-type` 의 칸 이름 `Property 1` 도 그대로
- 개발 쪽에 알릴 것: 바뀐 부품 이름 8개(text-btn · analysis-info · icon/symbol-author-house · symbol-box · menu/menu-left-content · chart-bubble · arrow-filter-down · search-dropdown-list), 바뀐 칸 이름 7곳, service-tag 의 type=ipo. 꼬리표·문서 글자는 Noto Sans KR(서체 바꾸기 플러그인 필요)
- KRDS 파일: EnoDStsuDByOcdrMOUqwiI (읽기만)

### 저장소
- Design-Claude: 깃허브 morningjh-cpu/Design-Claude (공개 — 사용자 확인: 공개 문제없음). 이전 커밋 3adf3e7(2026-11-06 push, 간격 되돌림·개선안 10개·통합 조회 HTML). 2026-11-11 HANDOFF 고침 커밋·push(피그마 lg 버튼 높이 수정 기록)
- 홈 저장소: ~/.claude/skills = 깃허브 morningjh-cpu/my-claude-home (비공개). 스킬 + 공통설정 + 홈 파일 + 도구 + 저장소 목록. 상세는 그 저장소 `설치-안내.md`. 2026-11-02 10ef952(VS Code 글자 크기·확대 공통 적용) push 완료
- 홈 `~/my-projects` 에서 claude-study·Design-Claude·FnGudie-BI-Manager 를 오가며 작업 (VS Code: my-projects.code-workspace, 첫 폴더 = 🏠 홈)
- claude-study: 옛 vibe-codding-practice 를 이름 변경·비공개 전환, 클로드 공부 + 연습(vibe-coding/) 합침. 옛 폴더는 `~/my-projects/_trash/`
- 이 컴퓨터 git 기본 작성자 = morningjh-cpu. 공통설정 첫 적용 때 옛 `~/.claude/CLAUDE.md`·`settings.json` 은 `.백업-20261101-*` 로 남김
- 전역 규칙: "cmt"·"츳"·"커밋" → 커밋+push. 질문 선택지는 한글로(2026-11-01 추가, 고유명만 영어)
- VS Code 커밋 버튼 누르면 자동 올리기(`git.postCommitCommand: sync`) — 이 컴퓨터 VS Code 설정 + 홈 작업공간 파일 둘 다
- VS Code 글자 크기·확대(2026-11-02, 회사 PC): 글자 18, 확대 1단계(`window.zoomLevel: 1`), Ctrl +/- 하면 바로 저장(`window.zoomPerWindow: false`). 세 PC 공통 값은 홈 저장소 `공통설정/vscode-settings.json` → Claude 켤 때 `적용.sh` 가 VS Code 설정에 그 값만 끼워 넣음(공통 파일이 바뀔 때만, 평소 Ctrl +/- 로 바꾼 건 유지)
- 회사 PC: FnGudie-BI-Manager 에 안 올린 변경이 있어 2026-11-02 시작 때 최신으로 못 받음(그 저장소 일을 할 때 확인)

### 피그마 (파일 nRGwNoZ92JBOTFire7zK8P)
**15. 공지사항/고객지원 (10394:30337)**
- `디자인 변경 - 개선안` 구역(12540:5218) 완성 → plan/phase-1/02
- 관리자 글쓰기 12533:4810 을 기획안(12591:23369)대로 고침(한 줄 배치·유형 펼친 목록·작성일 시각·편집칸 안 가이드·파일 삭제 버튼·취소/등록하기) + 수정 화면 12597:4241 (바로 아래) → plan/phase-1/11. 파일 이름 말풍선은 안 넣기로 함(사용자 결정). 사용자 검토 대기

- 공지사항 - 목록(12533:4710) 스킬별 4안 + 조합 1안: 구역 아래 y=4100 한 줄 12688:819 · 12690:996 · 1273 · 1641 · 1917 → plan/phase-1/12. 사용자 검토 대기

**17. 서비스 소개 (7698:35779)**
- 기준 화면 12542:600 (기획안 수정 반영) → plan/phase-1/03
- 개선안 1차 A/B/C, 2차 A2/B2/C2/D, 3차 ①~⑤ → plan/phase-1/04~06 (1·2차 평: 별로)
- 사용자가 3차 ①안을 고친 화면 12568:2015 — 지금 이름 "서비스 소개- 수정버전-20261101"(전 "수정버전3"), PLUS 칸은 사용자가 새로 바꿈(12588:8982)
- Hallmark 리디자인 12577:3650 (x=6868, y=4074 — 원본 아래) → plan/phase-1/07
- 스킬별 4안 + 조합 1안 + 피그마 실제 움직임: 원본 오른쪽 한 줄(y=-277) 12585:3977 · 4145 · 4313 · 4481 · 4649 → plan/phase-1/09
- 움직임 없이 11안(단독 4 + 짝 6 + 네 스킬 1): 새 줄(y=9000) 12592:3977 ~ 12592:5727 → plan/phase-1/10
- 위 세 묶음 모두 사용자 검토 대기

### 피그마 — 와이즈리포트 디자인 AI 체크 버전 (파일 HxECyUsoLnDxoSWSKophQn)
- 2026-11-04 날짜 표기 되돌림: 두 자리 연도(26.11.04 / 26.11) → 네 자리(2026.11.04 / 2026.11) 전체 수정 완료
  - 원본 부품 4개(unit-text·service-tag·bullet-label-list-area/true·author-area) + 화면 9개 페이지 날짜만 있는 글자 518곳 → 글꼴 `Noto Sans`
  - 날짜+한글 섞인 글자 68곳(예: "2026.07.10 기준", "2026.08.21 환불") → 글자 전체 `Noto Sans KR`(사용자 결정)
  - 이유: Wanted Sans 가 이 PC에만 있어 피그마 자동 작업에서 못 불러옴 → 글꼴을 바꿔야 수정 가능
  - 줄바뀜 난 기업분석 차트 날짜 98곳은 글자 칸을 내용 크기에 맞춤으로 바꿔 한 줄로. unit-text 묶음 틀 너비 131→161
  - 일부러 안 고친 것: "20.07%"(퍼센트). 🗑 보관 페이지는 찾지 않음
  - 그 뒤 사용자가 직접 정리: 날짜 글꼴 전부 Wanted Sans 로 되돌림, 빗금 날짜(ETF 차트·chart/combo-sparse) 네 자리로, 결제내역 "2026. 08. 21" 띄어쓰기 정리
  - 다음 할 일: 표 머리칸(th-text) 월 표기 "2026.06" → "2026년 6월". 남은 91곳 모두 5.기업분석(재무제표-리즈 18, 리츠·선박 스냅샷 각 13, 비즈니스 현황 12, 멀티팩터 모달 10, 기업·스팩 스냅샷 각 8, 컨센서스-기업 7, 비즈니스 현황-리츠 1, 컨센서스-투자회사 1). 재무제표·재무비율·투자지표는 이미 바뀜. 누가 고칠지 미정(제가 고치면 Wanted Sans 못 불러와 글꼴 바꿔야 함)
  - 2026-11-04 재점검: 두 자리 연도 0곳, 잘림·줄바뀜 없음. 남은 1곳 = card-my-plan "*2026. 08.21에…"(결제 연간플랜 화면에도) 연도 뒤 빈칸 — 사용자 확인 대기
- 2026-11-11 큰 버튼(size lg) 높이 48 맞추기 (피그마 파일에서 직접 수정, 이 저장소엔 파일 변화 없음)
  - btn-fill-primary(부품 2255:1009) lg: 48 아닌 것 48개(12번 회원가입 계열 42, 14번 결제 3, 공통 컴포넌트 dialog-action(alert) 1, 17번 서비스 소개 2) → 높이 48. 14번의 3개는 높이 "내용에 맞춤"→"고정"으로 바뀜(내용 맞춤이면 19+여백28=47이라서)
  - btn-ot-primary(부품 2255:1002) lg: 6개(12번 90일 비밀번호 변경 5, 17번 1) → 높이 48. 가로 설정(꽉 채움 등)은 그대로
  - 부품 원본 lg 높이는 둘 다 이미 48. 처음 조사 때 62개였는데 중간에 누가 원본 쪽(card-payment-summary·card-my-plan·dialog-action confirm)을 먼저 고쳐 48개만 남아 있었음
  - 확인: btn-fill-primary lg 71개는 부모 상자 밖으로 나감·새로 겹침 0(숫자 점검). 화면 캡처는 너무 작아 1px 차이는 못 봄. btn-ot-primary 6개는 넘침 점검 안 함(사용자가 안 해도 된다고 함)
  - 되돌리기: 피그마 버전 기록
- 2026-11-11 "플랜 구독" 화면 디자인 개선안 (14번 페이지 `design` 구역 14508:56306, 원본 `디자인수정` 14508:56039 — 원본은 안 건드림)
  - 사용 스킬 4개: impeccable · taste-skill · ui-ux-pro-max · frontend-design (웹 코드용이라 피그마에선 방향·기준만 가져옴)
  - 1차 스킬별 2안씩 8안 → 사용자가 6개 지운 듯(내가 지운 것 아님): 남은 것 [impeccable-1] 정돈형, [frontend-design-2] 한 점 집중형
  - 2차 두 스킬 짝 6쌍×2안 = 12안: 원본 아래 3줄(y 2889·4033·5177). 이름 `[A×B-1/2] …`
  - 3차 네 스킬 모두 조합 2안: `[모두 조합-1] 보라 간행물·접근성형`, `[모두 조합-2] 무채색 장부·청록 요약 블록형` (y 6321 줄). 구역 높이 7700으로 늘림
  - 공통: 글꼴은 Wanted Sans 대신 Noto Sans KR 등으로 바뀜(고른 안은 글꼴 되돌려야 함), 문구·버튼 추가 없음, 결제하기 버튼 높이 48 유지, 카드 아래 여백 20 이상
  - 주의: 구역 안 좌표는 음수 → 위치 계산에서 최댓값 초기값은 -Infinity (0이면 틀어짐). 복사본(clone)은 페이지 맨 위로 생기니 만든 뒤 구역에 appendChild 하고 x·y 다시 지정
  - 다음: 사용자가 안 고르기(고른 안은 글꼴·간격 저장값 연결 정리 필요)

### 스킬
- 설치·설명서: 홈 저장소 ~/.claude/skills/Skills-list/ (설치한-스킬-목록, 00 상황별 찾기, 01~17) → plan/phase-1/08
- 플러그인 10개(figma, frontend-design, hallmark, superpowers, karpathy, humanize-korean, korean-skills, commit-commands, watch, motionsites-web-builder) + 개별 6개(docx, impeccable, taste-skill, ui-ux-pro-max, find-skills, design-system — 2026-11-03 회사 PC에서 추가, 디자인시스템 점검·설명서용 → Skills-list/18). 노트북·집 PC는 `npx skills add anthropics/knowledge-work-plugins@design-system -g -y -a claude-code` 또는 홈 저장소 받기로 생김
- MotionSites: 집 PC 설치 완료. 노트북·회사 PC는 켤 때 '안 깔린 플러그인' 알림이 뜨면 설치
- PC 자동 연동: Claude 켤 때 홈 저장소 `도구/시작.sh` 가 PC 종류 확인 → 설정 적용 → 일 저장소 최신 받기 → 회사 PC에서만 깃랩 연결 → 빠진 플러그인 알림
- watch: 집 PC 설치·점검 ready. 이번 세션 시작 때 "Python 3.10+ 필요" 경고가 떴음 → 확인 필요 → ~/.claude/skills/Skills-list/16-watch.md
- 스킬 설치 시 규칙: CLAUDE.md 참고 (목록·설명서·상황별 표·개인 스킬 저장소 함께 갱신)

## 다음 할 일
- **통합 조회 HTML (plan/phase-2/22·23)**: 피그마 `디자인-` 페이지의 `이걸로 HTML 만들어봐`(14294:77567)를 그대로 옮긴 판 `out/통합조회-v2/index.html`. 피그마에서 뽑은 조각 `parts/*.txt` + `template.html`(동작 스크립트) → `py -3 build.py`. 2026-11-06 바뀐 별(menu/ui-icon-action)·하트(menu/ui-icon-favorite) 아이콘 반영(`update_icons.py`, 기본·hover·선택 3상태). 버튼 동작은 직접 눌러 본 확인 아직 → 사용자 확인 대기. 화면이 또 바뀌면 같은 변환 스크립트로 해당 영역만 다시 뽑기(23번 파일에 방법)
  - 사용자가 정할 것: 첫 판 `out/통합조회`(선·아이콘 달라 안 씀)를 `_trash/` 로 옮길지
- 통합 조회 개선안 10개(스킬 4개 혼자·둘씩 짝)를 `디자인-` 페이지에 만듦 — 고를 안 정하기. 새 글자는 Noto Sans KR 이라 고른 안은 글꼴 바꿔야 함. 3안(ui-ux-pro-max)은 어두운 화면이 파일 dark 색 묶음 미완성으로 깨져 글자 대비 안으로 바꿈 (plan/phase-2/21)
- 간격 저장값 16개(spacing/space-*): 이제 쓰는 곳 없음(보관 페이지 3칸만). 지울지 남길지 사용자 결정 대기
- 스킬 추천 받음 → vercel web-design-guidelines 는 설치 안 하기로(사용자, 2026-11-06. 코드 검사용이라 피그마 단계엔 안 맞음)
- **간격 조정 되돌림(plan/phase-2/20, 2026-11-06)**: 사용자 요청으로 18번 간격 맞추기를 백업 값으로 원복 끝(부품 232칸 + 겹친 부품 539칸, 크기 방식도 백업대로). space-3·18·30 저장값은 남김. 간격 조정 뒤 만든 화면(ETF/ETN 페이지·디자인- 페이지 등) 목록은 20번 파일. 화면 크기 변화 없음. 그 화면 8개 이름 앞에 [간격조정후] 꼬리표 붙임. 그 뒤 간격 저장값 연결을 파일 전체(보관 제외)에서 풀고 같은 숫자로 넣음 — 저장값 16개는 남아 있지만 쓰는 곳 없음
- **SVG 로고 워터마크(plan/phase-1/13)**: 저작권 문제로 그만둠(2026-11-05). 점검 전용 도구 scripts/svg_watermark_check.py 만 남김. 결과물·전체 도구는 _trash/watermark/
- **로고 이미지 → 벡터(SVG) 변환 프로그램**: 새 저장소 ~/my-projects/logo-vectorizer 로 따로 진행(2026-11-05). 거기 HANDOFF 참고
- **디자인시스템 구축(plan/phase-2)**: 테스트 파일 HxECyUsoLnDxoSWSKophQn 에서. 1~5단계 끝(03~09) + 피그마 표시(10) + 입력·선택 분리(11, 종류별 페이지 9개) + 백업에서 빠진 색 저장값 5개 넣음(12, bg-card-pinned 는 백업처럼 iris-15 로 되돌림). 사용자가 종류별 페이지를 `📒 공통 컴포넌트 / 패턴` 페이지 구역으로 합침(정리 기록 페이지도 없어짐). 부품 안 연결 안 된 색 조사(13, 잘못 이해) → 다른 파일 저장값에 걸린 색 1,168곳 찾음(14, 전체 페이지 끊긴 색 385곳 연결 + 같은 이름 없는 221곳 빨강 표시. 숨김 레이어·파운데이션·보관 제외. 남은 끊긴 색 ic-gr 1, tx-ddl-add 2). 글자 스타일(15): Wanted Sans 로 바뀜 → 부품 원본 345개 연결, 자간 스타일 10개 추가, 부품 원본 522 + 화면 1,409 글자 스타일 연결 끝 (줄간격 다른 2,279·스타일 없는 673 은 그대로). 점검 3차: out/ds-inventory/디자인시스템-점검-3차.html (어림 81/100), 모서리 213곳 연결(full 167 + 맞춤 46), 남은 직접 모서리 26 은 아이콘 안. 끊긴 색 모두 해결(tx-ddl-add 2개 → base/sub/indigo-500). 보관 페이지는 모든 점검·표시·제안에서 제외(사용자). 낱개 부품 9개도 묶음으로 바꿔 name 칸 채움. 안 쓰는 색 168개 unused 폴더로(19, tx-ddl-add 2개 포함), 화면 페이지 아직. 직접 넣은 흰색 313곳 저장값 연결(16), 검정 불투명 64곳(어림) 연결, 10% 테두리 42곳 bd-light, 남은 직접 검정 9곳 보라 표시. 부품 설명(17): 공통 컴포넌트 구역 전부(129+기존1) 달았다가 용도 한 줄로 줄임, 패턴 구역은 패스(사용자). 6단계 점검 2차: out/ds-inventory/디자인시스템-점검-2차.html (어림 69/100). name 칸은 일부러 둔 것 → 되살림·없던 26세트 추가·여러 값 4세트 1개로, 간격 1,171곳 가까운 값으로 맞춤(18), 그 뒤 space-3 저장값 추가하고 백업에서 3이던 213칸 space-3 으로 되돌림, space-18 추가(21칸), 백업과 크기 다른 부품 너비·높이 원래대로(같으면 내용 맞춤, 아니면 고정), footer copyright 위 여백 0. 부품 설명은 용도 한 줄로 줄임. 사용자가 직접 checkbox·switch hover 추가, radio 작업 중(state=New value/New hover). 남은 것: tag-basic·btn-login·filter-reset 비활성 색, 검정·흰색 용도, 부품 설명, 글자 스타일(Wanted Sans로 바꾼 뒤 연결)
- 공지사항 목록 5안(plan/phase-1/12) 사용자 확인 → 고른 안 다듬기, 상세 화면에도 맞출지 정하기
- 새 글자를 넣는 작업은 Noto Sans로 하고, 끝나면 서체 바꾸기 플러그인 링크를 드리기(교훈 칸 참고)
- 공지사항 관리자 글쓰기·수정 화면(plan/phase-1/11) 사용자 확인 → 수정 반영
- 서비스 소개 11안(plan/phase-1/10)·움직임 5안(09)·Hallmark안(07) 사용자 확인 → 고를 안 정해서 다듬기
- 빈 그림 칸 2곳(서비스 소개 첫 화면·콘텐츠 구역): 실제 와이즈리포트 화면 캡처 받으면 채우기
- watch 경고 원인(2026-11-01 확인·조치, 집 PC): `python`이 윈도우 스토어 가짜 바로가기(WindowsApps)에 먼저 걸림 → 사용자 PATH에서 `%LOCALAPPDATA%\Python\bin` 을 WindowsApps 앞으로 옮김(원래 값 백업 `~/.claude/PATH-백업-20261101.txt`). Claude 다시 켠 뒤 경고 사라졌는지 확인, "setup needs attention" 뜨면 /watch 한 번 실행. 노트북·회사 PC도 같은 경고면 같은 조치
- 집 PC·노트북: Claude 켠 뒤 VS Code 글자 크기·확대가 회사 PC와 같게 들어갔는지 확인(VS Code 다시 켜야 보임)
- 회사 PC도 2026-11-02 시작 때 watch "setup needs attention" 경고 뜸 → 위 watch 조치와 같은지 확인
- 나머지 컴퓨터 2대: 홈 저장소 `설치-안내.md`의 "새 컴퓨터 시작하기" 1~6 (사용자가 할 일)
- VS Code 안에서 Claude 를 켰을 때 시작 폴더가 홈(my-projects)인지 확인 — 아니면 맞추기

## 남은 정리
- `.taste-skill/` 임시 폴더: 커밋 제외(.gitignore) 처리만 함, 폴더는 남아 있음

## 교훈
- Wanted Sans Variable 글꼴은 피그마 작업 도구에서 불러올 수 없음 → 글자 내용·정렬은 사용자가 손으로. 복제한 글자의 rescale(비율)·색·폭 변경은 됨 → 기준 화면을 복제해서 고치는 게 글꼴을 살리는 길
- 원인(2026-11-02 확인): 작업 도구는 피그마 서버에서 돌아 PC 설치 서체를 못 봄(구글 서체만). Pretendard도 같음. 해결: 작업은 Noto Sans로 하고, 끝나면 사용자가 플러그인 "Noto → Wanted Sans 서체 바꾸기"(id d67f5423-e882-45ed-ad25-9d285b84f705, FnGuide's Team)를 실행. 파일 링크 뒤에 `&try-tool-resource-content-id=<id>&try-tool-resource-type=gen_tool` 를 붙여 주면 바로 열림
- 공지사항 입력칸 부품의 '입력된 글자'도 없는 글꼴이라 못 바꿈 → 안내 글자 칸에 값을 넣고 색을 진하게
- 피그마 작업 스크립트는 중간에 오류가 나면 통째로 되돌아감 → 다시 돌려도 겹치지 않음. 다만 사용자가 기준 화면을 고치면 부품 번호가 바뀌니 작업 전에 다시 확인
- 맨 위 화면 틀 높이는 안쪽 container(고정 높이) 말고 푸터 아래끝 기준으로 맞춤. 세로 배치로 바꿀 때 "양끝 정렬"이면 간격이 0 → MIN으로
- resize()는 자동 크기를 고정으로 바꿈 → 뒤에 다시 AUTO/HUG. 가로 배치 틀은 세로 크기가 counterAxis 쪽
- 변수 색을 입힐 때 기본색을 실제 값으로 넣어야 화면 캡처에서 색이 안 틀어짐
- 피그마 움직임 기능은 이 파일에서 됨(키프레임). 다만 시간 기준이라 스크롤에 맞춰 나타나기는 못 함. 사용자는 움직임을 그만두기로 함(2026-11-01)
- 개선안은 "티는 나되 과하지 않게", 기획안에 없는 버튼·문구·가짜 예시 금지. 고정 조건이 많으면 짝·조합안끼리 비슷해짐 → 미리 알림
- Hallmark·taste-skill·impeccable 등은 웹 코드용 → 피그마에서는 점검 기준·방향 뽑기로만
- 피그마 화면 → HTML 은 손으로 그리면 선·아이콘이 달라져 비교가 안 됨(사용자 지적). 레이어를 그대로 옮기는 변환(자동 배치→flex, 선→안쪽 그림자, 아이콘→SVG 내보내기)으로 해야 함. 아이콘 틀의 자기 배경색은 SVG에 안 담길 수 있어 캡처로 확인
- 글꼴이 없어도 기존 글자의 색(fills)은 바꿀 수 있음. 내용·크기는 못 바꿈
- 화면 맨 위 틀에서 findAll 이 안쪽까지 못 찾는 때가 있음 → 안쪽 영역(부품) 번호로 직접 찾기
- 이 파일의 dark 색 묶음은 덜 만들어져 있음(흰 바탕 남음) → 어두운 화면 안 쓰기
- 결과물 확인은 크롬 headless 캡처(`--screenshot`)로 1920 너비 비교

# HANDOFF — 이 파일은 clear 전에 항상 최신으로 덮어쓴다 (이 줄 포함)

기준: 2026-11-02 (마지막 작업: 회사 PC IMORNING02)

## 현재 상태
### 저장소
- Design-Claude: 깃허브 morningjh-cpu/Design-Claude (공개 — 사용자 확인: 공개 문제없음). 마지막 커밋 1c0facc, 로컬과 같음(2026-11-02 시작 때 깨끗)
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

### 스킬
- 설치·설명서: 홈 저장소 ~/.claude/skills/Skills-list/ (설치한-스킬-목록, 00 상황별 찾기, 01~17) → plan/phase-1/08
- 플러그인 10개(figma, frontend-design, hallmark, superpowers, karpathy, humanize-korean, korean-skills, commit-commands, watch, motionsites-web-builder) + 개별 6개(docx, impeccable, taste-skill, ui-ux-pro-max, find-skills, design-system — 2026-11-03 회사 PC에서 추가, 디자인시스템 점검·설명서용 → Skills-list/18). 노트북·집 PC는 `npx skills add anthropics/knowledge-work-plugins@design-system -g -y -a claude-code` 또는 홈 저장소 받기로 생김
- MotionSites: 집 PC 설치 완료. 노트북·회사 PC는 켤 때 '안 깔린 플러그인' 알림이 뜨면 설치
- PC 자동 연동: Claude 켤 때 홈 저장소 `도구/시작.sh` 가 PC 종류 확인 → 설정 적용 → 일 저장소 최신 받기 → 회사 PC에서만 깃랩 연결 → 빠진 플러그인 알림
- watch: 집 PC 설치·점검 ready. 이번 세션 시작 때 "Python 3.10+ 필요" 경고가 떴음 → 확인 필요 → ~/.claude/skills/Skills-list/16-watch.md
- 스킬 설치 시 규칙: CLAUDE.md 참고 (목록·설명서·상황별 표·개인 스킬 저장소 함께 갱신)

## 다음 할 일
- **디자인시스템 구축(plan/phase-2)**: 테스트 파일 HxECyUsoLnDxoSWSKophQn 에서. 1~5단계 끝(03~09) + 피그마 표시(10) + 입력·선택 분리(11, 종류별 페이지 9개) + 백업에서 빠진 색 저장값 5개 넣음(12, bg-card-pinned 는 백업처럼 iris-15 로 되돌림). 사용자가 종류별 페이지를 `📒 공통 컴포넌트 / 패턴` 페이지 구역으로 합침(정리 기록 페이지도 없어짐). 부품 안 연결 안 된 색 조사(13, 잘못 이해) → 다른 파일 저장값에 걸린 색 1,168곳 찾음(14, 전체 페이지 끊긴 색 385곳 연결 + 같은 이름 없는 221곳 빨강 표시. 숨김 레이어·파운데이션·보관 제외. 남은 끊긴 색 ic-gr 1, tx-ddl-add 2). 글자 스타일(15): 사용자가 typo 18개를 Wanted Sans 로 바꾸면 줄간격까지 같은 522개만 연결. 직접 넣은 흰색 313곳 저장값 연결(16), 검정 불투명 64곳(어림) 연결, 10% 테두리 42곳 bd-light, 남은 직접 검정 9곳 보라 표시. 사용자가 직접 checkbox·switch hover 추가, radio 작업 중(state=New value/New hover). 남은 것: tag-basic·btn-login·filter-reset 비활성 색, 검정·흰색 용도, 부품 설명, 글자 스타일(Wanted Sans로 바꾼 뒤 연결)
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

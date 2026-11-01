# HANDOFF — 이 파일은 clear 전에 항상 최신으로 덮어쓴다 (이 줄 포함)

기준: 2026-11-01

## 현재 상태
### 저장소
- Design-Claude: 깃허브 morningjh-cpu/Design-Claude (공개 — 사용자 확인: 공개 문제없음) 에 push 완료, 로컬과 같음
- 홈 저장소: ~/.claude/skills = 깃허브 morningjh-cpu/my-claude-home (비공개, 2026-11-01 my-claude-skills 에서 이름 변경). 스킬 + 공통설정 + 홈 파일 + 도구 + 저장소 목록. 상세는 그 저장소 `설치-안내.md`
- 홈 `~/my-projects` 에서 claude-study·Design-Claude·FnGudie-BI-Manager 를 오가며 작업 (VS Code: my-projects.code-workspace, 첫 폴더 = 🏠 홈)
- claude-study: 옛 vibe-codding-practice 를 이름 변경·비공개 전환, 클로드 공부 + 연습(vibe-coding/) 합침. 옛 폴더는 `~/my-projects/_trash/`
- 2026-11-01 세 저장소(홈·claude-study·Design-Claude) 모두 push 완료. 이 컴퓨터 git 기본 작성자 = morningjh-cpu
- 공통설정 첫 적용 때 이 컴퓨터의 옛 `~/.claude/CLAUDE.md`·`settings.json` 은 `.백업-20261101-*` 로 남김

### 피그마 (파일 nRGwNoZ92JBOTFire7zK8P, 페이지 "17. 서비스 소개" 7698:35779)
- 15. 공지사항: `디자인 변경 - 개선안` 구역(12540:5218) 완성 → plan/phase-1/02
- 17. 서비스 소개 기준 화면 12542:600 (기획안 수정 반영) → plan/phase-1/03
- 개선안 1차 A/B/C, 2차 A2/B2/C2/D, 3차 ①~⑤ → plan/phase-1/04~06 (1·2차 평: 별로)
- 사용자가 3차 ①안을 고쳐 "서비스 소개- 수정버전3" 12568:2015 (x=6868)로 둠
- 그걸 Hallmark 기준으로 리디자인 → "서비스 소개- 수정버전3 (Hallmark)" 12577:3650 (x=8988), 사용자 검토 대기 → plan/phase-1/07

### 스킬
- 설치·설명서: Skills-list/ (설치한-스킬-목록, 00 상황별 찾기, 01~16) → plan/phase-1/08
- 플러그인 10개(figma, frontend-design, hallmark, superpowers, ponytail, karpathy, humanize-korean, korean-skills, commit-commands, watch) + 개별 5개(docx, impeccable, taste-skill, ui-ux-pro-max, find-skills)
- 이 폴더에서는 ponytail 자동 꺼짐(.claude/settings.json)
- 2026-11-01 watch(claude-video, 유튜브·영상 보고 요약) 설치 + FFmpeg·yt-dlp·Deno(winget). 점검 결과 ready. 자막 없는 영상용 받아쓰기는 설정 안 함 → Skills-list/16-watch.md
- 스킬 설치 시 규칙: CLAUDE.md 참고 (목록·설명서·상황별 표·개인 스킬 저장소 함께 갱신)

## 다음 할 일
- Hallmark 리디자인(12577:3650) 사용자 확인 → 수정 반영
- 빈 그림 칸 2곳(첫 화면·콘텐츠 구역): 실제 와이즈리포트 화면 캡처 받으면 채우기
- 나머지 컴퓨터 2대: 홈 저장소 `설치-안내.md`의 "새 컴퓨터 시작하기" 1~6 (watch 플러그인·영상 프로그램 3개 포함, 사용자가 할 일)
- watch 첫 사용: Claude 다시 켠 뒤 `/watch:watch (유튜브 주소)` 로 잘 되는지 확인
- VS Code 안에서 Claude 를 켰을 때 시작 폴더가 홈(my-projects)인지 확인 — 아니면 맞추기
- 이후: 지금까지 페이지로 디자인시스템 구축 (01-상황.md)

## 남은 정리
- `.taste-skill/` 임시 폴더: 커밋 제외(.gitignore) 처리만 함, 폴더는 남아 있음

## 교훈
- Wanted Sans Variable 글꼴은 피그마 작업 도구에서 불러올 수 없음 (설치·재시작 후에도 0개) → 글자 내용·정렬은 사용자가 손으로
- Wanted Sans 부품·글자를 통째로 복제하는 건 됨. 복제한 글자도 rescale(비율)·색·폭 변경은 됨 → 기준 화면을 복제해서 고치는 게 글꼴을 살리는 길
- 변수 색을 입힐 때 기본색을 실제 값으로 넣어야 화면 캡처에서 색이 안 틀어짐
- resize()는 자동 크기를 고정으로 바꿈 → 뒤에 다시 AUTO/HUG. 가로 배치 틀은 세로 크기가 counterAxis 쪽
- 개선안은 "티는 나되 과하지 않게", 기획안에 없는 버튼·문구·가짜 예시 금지
- Hallmark·taste-skill은 웹 코드용 → 피그마에서는 점검 기준·방향 뽑기로만

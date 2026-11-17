# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

이 폴더는 2026 와이즈리포트 리뉴얼 웹사이트의 피그마 디자인시스템 구축·신규 페이지 디자인 프로젝트다.
흐름별 상황은 plan/phase-N/01-상황.md 에 내 말을 받아써 둔다.
폴더 역할 — plan/: 계획·결정, phase 별로 나누고 파일은 01-부터 번호. data/: 받은 파일, 고치지 않는다. out/: 만든 결과물. scripts/: 네가 짠 도구.
흐름이 크게 바뀌면 plan/phase-N/ 을 새로 만든다(지금 phase-3). 새 일은 번호를 늘려 새 파일, 옛 파일은 지우지 않는다.
다른 폴더가 필요하면 영문 이름으로 만들고 이 파일에 역할을 한 줄 적는다.
스킬 목록 문서는 2026-11-01 홈 저장소 ~/.claude/skills/Skills-list/ 로 옮김(세 PC 공유). 스킬을 설치·삭제하면(내가 /plugin 으로 직접 한 것 포함) 바로 ~/.claude/skills/Skills-list/설치한-스킬-목록.md 를 고치고 기준일을 바꾼다. 같은 때 그 스킬의 번호 설명서(같은 틀)를 만들거나 정리하고, 00-상황별-찾기.md 표도 고친다. 또 홈 저장소(~/.claude/skills = github morningjh-cpu/my-claude-home, 비공개)의 설치-안내.md 와 스킬 폴더도 갱신하고, 올리기는 "cmt" 때 한다.
HANDOFF.md 에 현재 상태와 다음 할 일을 적어 두고, clear 하기 전에 항상 최신으로 덮어쓴다.
내 수준에 맞춰 전문용어 없이 말해라. 애매하면 먼저 물어라.

## 피그마 파일
- `HxECyUsoLnDxoSWSKophQn` — 와이즈리포트 디자인 AI 체크 버전 (디자인시스템·부품·전체 화면)
- `nRGwNoZ92JBOTFire7zK8P` — 서비스 소개(17번)·공지사항/고객지원(15번) 개선안 작업 파일
- `jey6PXIFB19gl5et1XzIzi` — 와이즈 컴포넌트 테스트 (phase-3 디자인시스템 구조화: KRDS 큰 틀 + Ant Design 6묶음 분류)

## 도구 (Windows 는 `py`)
- `py scripts/ds_inventory_report.py <원자료.txt> <결과.html>` — 부품 전수조사 원자료를 분류해 HTML 표로 (예: out/ds-inventory/)
- `py scripts/svg_watermark_check.py <파일.svg> ...` — SVG 안 숨은 표시 점검만, 파일은 안 고침
- `py out/통합조회-v2/build.py` — parts/ 조각 + template.html → index.html 하나로 합침
- `scripts/notice-list-variant.js` — 피그마 자동 작업(use_figma)용. 맨 위 `__KIND__`(1~5)·`__X__` 만 바꿔 실행

## 피그마 작업 주의
- Wanted Sans 는 이 PC에만 있어 피그마 자동 작업에서 못 불러온다 → 그 글꼴 글자를 고치려면 글꼴을 바꿔야 하니 먼저 묻는다.
- 복사본(clone)은 페이지 맨 위에 생긴다 → 만든 뒤 구역에 다시 넣고(appendChild) x·y 를 다시 지정.
- 구역 안 좌표는 음수일 수 있다 → 가장 큰 값 찾을 때 시작값은 -Infinity (0이면 틀어짐).
- `🗑 보관` 페이지는 모든 점검·표시·제안에서 뺀다.
- 부품 묶음의 `name` 종류 칸은 클로드가 부품을 알아보기 쉽게 일부러 둔 것이다. 지우거나 군더더기로 꼽지 마라. 묶음마다 값 하나, 새 묶음은 묶음 이름 마지막 토막을 종류 이름 맨 앞에. 값이 여럿이면 구분은 `type` 같은 다른 칸으로 → plan/phase-2/18
- tag-basic·btn-login·filter-reset 등의 비활성 상태는 필요 없어서 안 만든 것이다. 점검·보고·제안에서 "비활성 없음"을 꺼내지 마라(내가 상태를 물을 때만).
- "끊긴 색"(= "배리어블은 입력됐는데 연결 안 된 것") = 다른 파일 저장값에 걸린 색(`variable.remote === true`). 손으로 넣은 색이 아니다 — 그건 "직접 색"이라 부른다.
  - 지시 틀: `[어디] 끊긴 색 찾아줘 / 표시해줘 / 다시 연결해줘`. 부품 원본 먼저, 화면은 다음.
  - 숨긴 레이어(와 그 안)·`ㄴ 🎨 파운데이션`·`🗑 보관` 페이지는 건너뛴다.
  - 같은 이름 저장값이 이 파일에 없으면 빨갛게 표시하고 묻는다(마음대로 연결 금지). 다시 연결 뒤 색 값이 바뀐 곳은 모두 알린다 → plan/phase-2/14

## 피그마 → HTML
- 손으로 비슷하게 다시 그리지 말고 레이어 구조·선·여백·색을 그대로 옮기고, 아이콘은 피그마에서 SVG로 내보낸 것을 쓴다.
- 방식은 out/통합조회-v2 (parts 조각 + template + build.py) 를 다시 쓴다. 끝나면 크롬 화면 캡처로 피그마와 맞춰 본다 → plan/phase-2/23

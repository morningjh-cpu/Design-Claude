# 16 watch (claude-video) — 영상을 보고 요약·질문 답하기

**쓰는 일:** 기획 ● 디자인 ● 공부 (분야 무관)

부르는 법: `/watch:watch (유튜브 주소 또는 영상 파일)` · "이 영상 보고 요약해줘 (주소)" 라고 말해도 됨

## 상황별
| 상황 | 이렇게 말하기 |
|---|---|
| 유튜브 강의 내용 정리 | "이 영상 보고 핵심만 시간대별로 정리해줘 (주소)" |
| 영상 속 화면·디자인 참고 | "이 영상에서 화면이 나오는 장면을 시간과 함께 설명해줘" |
| 특정 내용 찾기 | "이 영상에서 ○○ 설명하는 부분이 몇 분쯤이야?" |
| 내 컴퓨터의 영상 파일 | "영상 파일 example.mp4 를 watch 로 보고 요약해줘" |

## 어떻게 동작하나
- 영상을 받아(유튜브는 yt-dlp) 일정 간격으로 장면 사진을 뽑고(FFmpeg), 자막·대본을 붙여 Claude에게 넘김
- 자막이 있으면 자막을 먼저 씀. 자막 없는 영상은 따로 받아쓰기 설정이 필요(지금은 안 해 둠)
- 자세히 볼수록(사진을 많이 뽑을수록) 대화 사용량이 커짐 — 기본값 "balanced"(보통)

## 필요한 프로그램 (컴퓨터마다 한 번)
- Windows: `winget install --id Gyan.FFmpeg --exact` · `winget install --id yt-dlp.yt-dlp --exact` · `winget install --id DenoLand.Deno --exact` + Python
- 설치 뒤 터미널·Claude 를 다시 켜야 프로그램을 찾음
- 유튜브가 자주 바뀌어 yt-dlp 는 최신이어야 함: 안 되면 `winget upgrade --id yt-dlp.yt-dlp --exact`

## 주의
- Claude Code(터미널·VS Code·데스크톱 앱의 Code)에서만 됨. 일반 Claude 채팅창·Cowork 에서는 안 됨
- 유튜브 영상 내려받기는 유튜브 이용약관·저작권과 관련됨 → 공부·참고용으로 혼자 보고, 받은 영상을 다시 공유하지 않기
- 회사 PC는 프로그램 설치·영상 내려받기가 보안 규정에 걸릴 수 있으니 먼저 확인
- 출처: github.com/bradautomates/claude-video (MIT, 별 약 1.9만, 2026-11-01 확인)

## 같이 쓰면 좋은 스킬
- [10 humanize-korean](10-humanize-korean.md) — 정리한 글을 자연스럽게
- [11 docx](11-docx.md) — 정리 내용을 워드로

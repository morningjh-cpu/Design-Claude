# 13 korean-skills — 한국어 글 다듬기 3종 (맞춤법·통일·AI 티)

**쓰는 일:** 기획 ●(기획서·공지·문서)  디자인 ○(화면 문구)  개발 ○(코드 속 한글 설명·안내문)

부르는 법: `/korean-skills:(이름)` + 글 붙여넣기 또는 파일 경로

## 명령어
| 명령 | 언제 | 예시 |
|---|---|---|
| `/korean-skills:grammar-checker` | 맞춤법·띄어쓰기·문법·문장부호 검사, 고친 이유 설명 | `/korean-skills:grammar-checker plan/phase-1/07-….md` |
| `/korean-skills:style-guide` | 문서 안·프로젝트 전체의 통일성 검사: 말투(존댓말/반말), 용어(사용자/유저), 숫자·날짜 형식, 목록·따옴표 | `/korean-skills:style-guide 서비스 소개 화면 문구 전체` |
| `/korean-skills:humanizer` | AI가 쓴 티(쉼표 과다, 번역투 "~에 대해/~을 통해/되어진다" 등 40가지)를 찾아 자연스럽게 | `/korean-skills:humanizer` + 글 |

## 언제 좋은가
- 화면 문구를 여러 사람이 써서 말투·용어가 섞였을 때 → style-guide
- 공지·약관·기획서를 내보내기 전 → grammar-checker
- 짧은 글의 AI 티를 빠르게 → humanizer

## humanize-korean(10번)과 차이
| | korean-skills humanizer | [10 humanize-korean](10-humanize-korean.md) |
|---|---|---|
| 규모 | 패턴 40가지, 한 번에 처리 | 패턴 85가지, 글 상태에 따라 1~3단계 |
| 좋은 때 | 짧은 문구·빠른 확인 | 긴 글·정밀 윤문 |

## 주의
- 글만 다루는 스킬(프로그램 실행·바깥 전송 없음, 설치 파일 확인함)
- 내용은 그대로 두고 표현만 고침

## 같이 쓰면 좋은 스킬
- [10 humanize-korean](10-humanize-korean.md), [11 docx](11-docx.md)

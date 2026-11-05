"""SVG 안에 워터마크·숨은 정보가 있는지 점검만 하는 도구 (파일은 고치지 않음).

워터마크 넣기·지우기는 저작권 문제로 그만둠(2026-11-05) → plan/phase-1/13.
옛 전체 기능 도구는 _trash/watermark/svg_watermark-전체기능.py

사용법 (Windows 는 py):
  py scripts/svg_watermark_check.py <파일.svg> [파일2.svg ...]

찾는 것: 주석·메모(metadata)·제목·설명·글자·그림·숨긴 요소·덧붙인 정보 칸(data-)·
         영문·숫자가 아닌 글자·자릿수가 유난히 긴 숫자(숫자에 숨긴 표시일 수 있음)
"의심" = 워터마크·저작권 표시일 수 있는 것, "참고" = 편집 프로그램·피그마가 남긴 흔적.
숫자 자체에 아주 정교하게 숨긴 표시는 못 찾을 수 있음.
"""
import re
import sys

EDITOR_WORDS = re.compile(r"generator|created with|illustrator|inkscape|sketch|figma|svg export|affinity|pixelmator", re.I)
RIGHTS_WORDS = re.compile(r"©|\(c\)|copyright|rights|owner|licen[cs]e|author|creator|watermark|저작|소유|무단|워터마크|권리", re.I)
HIDDEN = re.compile(r'(?:opacity|fill-opacity)\s*[:=]\s*"?0(?:\.0+)?(?![.\d])|display\s*[:=]\s*"?none|visibility\s*[:=]\s*"?hidden')


def short(s):
    s = " ".join(s.split())
    return s if len(s) <= 60 else s[:60] + "…"


def scan(svg):
    """돌려주는 값: (의심 목록, 참고 목록)"""
    sus, info = [], []
    for c in re.findall(r"<!--(.*?)-->", svg, re.S):
        if EDITOR_WORDS.search(c) and not RIGHTS_WORDS.search(c):
            info.append(f"편집 프로그램 주석: {short(c)}")
        else:
            sus.append(f"주석: {short(c)}")
    for tag in ("metadata", "title", "desc", "text", "tspan", "foreignObject"):
        for c in re.findall(rf"<{tag}\b[^>]*>(.*?)</{tag}>", svg, re.S):
            sus.append(f"<{tag}> 칸: {short(re.sub(r'<[^>]+>', ' ', c)) or '(비어 있음)'}")
    for m in re.findall(r"<image\b[^>]*>", svg):
        sus.append(f"그림 파일 들어 있음: {short(m)}")
    for m in re.findall(r'\s(data-[\w-]+="[^"]*")', svg):
        sus.append(f"덧붙인 정보 칸: {short(m)}")
    for m in re.findall(r"<[a-zA-Z][^>]*>", svg):
        if HIDDEN.search(m):
            sus.append(f"숨긴 요소: {short(m)}")
    odd = sorted(set(re.findall(r"[^\x09\x0a\x0d\x20-\x7e]", svg)))
    if odd:
        sus.append(f"영문·숫자가 아닌 글자 {len(odd)}종: {''.join(odd)[:20]}")
    nums = re.findall(r"\d+\.\d+", " ".join(re.findall(r'="([^"]*)"', svg)))
    long_nums = [n for n in nums if len(n.replace(".", "").lstrip("0")) > 6]
    if long_nums:
        sus.append(f"자릿수가 유난히 긴 숫자 {len(long_nums)}개 (숫자에 숨긴 표시일 수 있음, 예: {long_nums[0]})")
    for m in re.findall(r'\s((?:inkscape|sodipodi|adobe|i|x|illustrator|sketch|figma)[:-][\w-]*="[^"]*")', svg, re.I):
        info.append(f"편집 프로그램 흔적: {short(m)}")
    for m in re.findall(r'xmlns:(\w+)="([^"]*)"', svg):
        if m[0] != "xlink":
            info.append(f"편집 프로그램 이름표: {m[0]} = {short(m[1])}")
    for m in re.findall(r'id="((?:mask|clip|paint|filter)\d+_\w+)"', svg):
        info.append(f"피그마 내보내기 이름: {m}")
    return sus, info


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit()
    for path in sys.argv[1:]:
        sus, info = scan(open(path, encoding="utf-8").read())
        print(f"[{path}]")
        if not sus:
            print("  워터마크·숨은 정보: 없음")
        for s in sus:
            print(f"  의심: {s}")
        for s in info:
            print(f"  참고: {s}")

"""부품 전수 조사 원자료(raw-*.txt)를 읽어 분류하고 HTML 표로 만든다.
사용: py scripts/ds_inventory_report.py out/ds-inventory/raw-20261103.txt out/ds-inventory/부품-전수조사.html
"""
import sys, re, html, collections, json

PAGES = {0: "프로젝트 정보", 1: "디자인 가이드", 2: "파운데이션", 3: "------", 4: "공통 컴포넌트",
         5: "01 GNB/LNB", 6: "02 메인", 7: "03 리포트", 8: "03-α 스크리너", 9: "4 시장 시그널",
         10: "7 종목 발굴", 11: "5 기업분석", 12: "14 결제", 13: "10 부가정보", 14: "6 섹터분석",
         15: "9 ETF/ETN", 16: "11 내 관심", 17: "12 회원가입", 18: "마이페이지", 19: "17 서비스 소개",
         20: "15 공지사항", 21: "----"}
COMMON = 4
FILE_KEY = "HxECyUsoLnDxoSWSKophQn"

# 철자만 다른 것으로 보이는 이름 (사람 눈으로 고른 것)
TYPO = {"txet-btn": "txt-btn"}

# 분류 이름과 설명
CATS = [
    ("unused", "안 씀", "어디에도 안 쓰임 → 보관 후보"),
    ("inner", "부품 속에서만", "화면엔 없고 다른 부품 안에서만 쓰임 → 감싼 부품이 살아 있으면 유지"),
    ("move", "공통으로 옮길 것", "공통 페이지 밖에 있는데 화면 페이지 3곳 이상에서 쓰임"),
    ("local", "페이지 전용", "한 화면 페이지에서만 쓰임 → 그 페이지용 묶음으로 둘지 정하기"),
    ("keep", "공통 유지", "공통 페이지에 있고 쓰이고 있음"),
    ("guide", "가이드용", "디자인 가이드 페이지 설명용 → 디자인시스템과 따로"),
]


def norm(name):
    n = name.strip().lower()
    n = TYPO.get(n, n)
    n = n.split("/")[-1]
    n = re.sub(r"-new$", "", n)
    return re.sub(r"[^a-z0-9가-힣]", "", n)


def main(src, dst):
    rows = []
    for line in open(src, encoding="utf-8"):
        if line.startswith("#") or not line.strip():
            continue
        p = line.rstrip("\n").split("|")
        nid, name, page, kind, var, s, i, pgs, par = p
        pages = [int(x) for x in pgs.split(",") if x]
        rows.append(dict(id=nid, name=name.strip(), page=int(page), kind=kind, var=int(var),
                         s=int(s), i=int(i), pages=pages, par=par, dup=[]))

    groups = collections.defaultdict(list)
    for r in rows:
        if r["page"] != 1:
            groups[norm(r["name"])].append(r)
    for key, g in groups.items():
        for r in g:
            r["dup"] = [x for x in g if x is not r] if len(g) > 1 else []

    for r in rows:
        screen_pages = [x for x in r["pages"] if x not in (1, 2, 3, 4, 21)]
        if r["page"] == 1:
            r["cat"] = "guide"
        elif r["s"] == 0 and r["i"] == 0:
            r["cat"] = "unused"
        elif r["s"] == 0:
            r["cat"] = "inner"
        elif r["page"] != COMMON and len(screen_pages) >= 3:
            r["cat"] = "move"
        elif r["page"] != COMMON and len(set(r["pages"])) <= 1:
            r["cat"] = "local"
        elif r["page"] != COMMON:
            r["cat"] = "local"  # 화면 페이지 1~2곳
        else:
            r["cat"] = "keep"

    count = collections.Counter(r["cat"] for r in rows)
    dup_groups = {k: g for k, g in groups.items() if len(g) > 1}
    by_page = collections.Counter(r["page"] for r in rows)

    def link(r):
        return f"https://www.figma.com/design/{FILE_KEY}/?node-id={r['id'].replace(':', '-')}"

    def tr(r):
        dup = ", ".join(f"{html.escape(d['name'])}({PAGES[d['page']]})" for d in r["dup"])
        used_on = ", ".join(PAGES[x] for x in r["pages"]) or "-"
        kind = "세트" if r["kind"] == "S" else "낱개"
        return (f"<tr data-cat='{r['cat']}' data-dup='{1 if r['dup'] else 0}'>"
                f"<td><span class='chip c-{r['cat']}'>{dict((c[0], c[1]) for c in CATS)[r['cat']]}</span></td>"
                f"<td class='nm'><a href='{link(r)}' target='_blank'>{html.escape(r['name'])}</a></td>"
                f"<td>{PAGES[r['page']]}<div class='sub'>{html.escape(r['par'])}</div></td>"
                f"<td>{kind} · {r['var']}</td>"
                f"<td class='num'>{r['s']:,}</td><td class='num'>{r['i']:,}</td>"
                f"<td class='pg'>{used_on}</td>"
                f"<td class='dup'>{dup}</td></tr>")

    order = {c[0]: n for n, c in enumerate(CATS)}
    rows_sorted = sorted(rows, key=lambda r: (order[r["cat"]], r["page"], r["name"].lower()))

    cards = "".join(
        f"<button class='card' data-f='{c[0]}'><span class='chip c-{c[0]}'>{c[1]}</span>"
        f"<b>{count.get(c[0], 0)}</b><small>{c[2]}</small></button>" for c in CATS)
    page_list = "".join(f"<li>{PAGES[p]} <b>{n}</b></li>" for p, n in sorted(by_page.items()))
    dup_html = "".join(
        "<li>" + " / ".join(f"<a href='{link(r)}' target='_blank'>{html.escape(r['name'])}</a>"
                            f"<span class='sub'>({PAGES[r['page']]}, 화면 {r['s']}회)</span>" for r in g) + "</li>"
        for k, g in sorted(dup_groups.items()))

    doc = f"""<!doctype html><html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>부품 전수 조사</title>
<style>
:root{{--bg:#f6f7f9;--panel:#fff;--ink:#1b1f24;--mute:#6b7280;--line:#e5e7eb;--accent:#2f5bea;
--unused:#d14343;--inner:#b7791f;--move:#2f5bea;--local:#6b46c1;--keep:#2f855a;--guide:#718096}}
@media (prefers-color-scheme:dark){{:root:not([data-theme=light]){{--bg:#111418;--panel:#1a1e24;--ink:#e6e8eb;--mute:#9aa3ae;--line:#2a3039}}}}
:root[data-theme=dark]{{--bg:#111418;--panel:#1a1e24;--ink:#e6e8eb;--mute:#9aa3ae;--line:#2a3039}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:14px/1.5 "Pretendard","Noto Sans KR",system-ui,sans-serif}}
main{{max-width:1280px;margin:0 auto;padding:32px 16px 80px}}
h1{{font-size:24px;margin:0 0 4px}}h2{{font-size:17px;margin:36px 0 12px}}
.lead{{color:var(--mute);margin:0 0 24px}}
.cards{{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:10px}}
.card{{all:unset;cursor:pointer;background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:14px;display:flex;flex-direction:column;gap:4px}}
.card b{{font-size:26px}}.card small{{color:var(--mute);font-size:12px}}.card.on{{outline:2px solid var(--accent)}}
.chip{{display:inline-block;font-size:12px;font-weight:600;padding:1px 8px;border-radius:99px;color:#fff;width:max-content}}
.c-unused{{background:var(--unused)}}.c-inner{{background:var(--inner)}}.c-move{{background:var(--move)}}
.c-local{{background:var(--local)}}.c-keep{{background:var(--keep)}}.c-guide{{background:var(--guide)}}
.bar{{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:16px 0}}
.bar input{{padding:8px 10px;border:1px solid var(--line);border-radius:8px;background:var(--panel);color:var(--ink);min-width:220px}}
.bar label{{color:var(--mute)}}
.wrap{{overflow-x:auto;background:var(--panel);border:1px solid var(--line);border-radius:10px}}
table{{border-collapse:collapse;width:100%;min-width:980px}}
th,td{{text-align:left;padding:8px 10px;border-bottom:1px solid var(--line);vertical-align:top}}
th{{position:sticky;top:0;background:var(--panel);font-size:12px;color:var(--mute);font-weight:600}}
td.num{{text-align:right;font-variant-numeric:tabular-nums}}td.pg{{font-size:12px;color:var(--mute);max-width:260px}}
td.dup{{font-size:12px;color:var(--unused);max-width:220px}}.nm a{{color:var(--ink);font-weight:600;text-decoration:none}}.nm a:hover{{color:var(--accent)}}
.sub{{font-size:11px;color:var(--mute)}}
.cols{{display:grid;grid-template-columns:1fr 2fr;gap:16px}}@media(max-width:760px){{.cols{{grid-template-columns:1fr}}}}
.box{{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:14px 18px}}
.box ul{{margin:0;padding-left:18px}}.box li{{margin:4px 0}}.box a{{color:var(--accent)}}
.note{{font-size:13px;color:var(--mute)}}
</style></head><body><main>
<h1>부품 전수 조사</h1>
<p class="lead">와이즈리포트 디자인시스템 테스트 파일 · 2026-11-03 · 부품 {len(rows)}개 (세트 {sum(r['kind']=='S' for r in rows)} · 낱개 {sum(r['kind']=='C' for r in rows)}) · 이름을 누르면 피그마에서 열림</p>
<div class="cards">{cards}</div>
<p class="note">"화면" = 화면 디자인에 놓인 횟수, "부품 속" = 다른 부품 안에 들어간 횟수. 숫자는 이 파일 안에서만 센 것이고, 다른 파일이 이 부품을 쓰는지는 세지 않았어요.</p>

<h2>겹쳐 보이는 부품 ({len(dup_groups)}묶음)</h2>
<div class="box"><ul>{dup_html}</ul>
<p class="note">이름 끝부분이 같거나 철자만 다른 것을 묶었어요. 실제로 같은 모양인지는 2단계에서 화면으로 확인해요.</p></div>

<h2>전체 목록</h2>
<div class="bar"><input id="q" placeholder="이름으로 찾기"><label><input type="checkbox" id="d"> 겹치는 것만</label>
<button class="card" data-f="" style="padding:6px 12px">전체 보기</button></div>
<div class="wrap"><table><thead><tr><th>분류</th><th>이름</th><th>있는 곳</th><th>종류 · 수</th><th>화면</th><th>부품 속</th><th>화면에서 쓴 페이지</th><th>겹쳐 보이는 것</th></tr></thead>
<tbody>{''.join(tr(r) for r in rows_sorted)}</tbody></table></div>

<h2>참고</h2>
<div class="cols"><div class="box"><b>페이지별 부품 수</b><ul>{page_list}</ul></div>
<div class="box"><b>다른 파일에서 가져와 쓰는 부품</b>
<p class="note">이 파일 밖(다른 라이브러리)의 부품이 화면에 놓인 경우예요. 대표 예: legend 93회, icon/checkbox-check 64회, Button 16회, btn-ot-primary 11회, btn-fill-primary 9회, menu-ui-icon 44회, icon/rank 8회, icon/tag-delete 8회 등 약 190종.
공통 페이지에 같은 이름의 부품이 있는 경우(btn-ot-primary, btn-fill-primary, tag-basic, checkbox, radio 등)는 이 파일 부품으로 바꿔 끼워야 하나로 관리돼요.</p></div></div>
</main>
<script>
const rows=[...document.querySelectorAll('tbody tr')];let f='';
function apply(){{const q=document.getElementById('q').value.toLowerCase(),d=document.getElementById('d').checked;
rows.forEach(r=>{{const ok=(!f||r.dataset.cat===f)&&(!d||r.dataset.dup==='1')&&(!q||r.textContent.toLowerCase().includes(q));r.style.display=ok?'':'none';}});
document.querySelectorAll('.card[data-f]').forEach(c=>c.classList.toggle('on',c.dataset.f===f&&f!==''));}}
document.querySelectorAll('.card[data-f]').forEach(c=>c.onclick=()=>{{f=c.dataset.f;apply();}});
document.getElementById('q').oninput=apply;document.getElementById('d').onchange=apply;
</script></body></html>"""
    open(dst, "w", encoding="utf-8").write(doc)
    print(json.dumps({"total": len(rows), "cats": count, "dup_groups": len(dup_groups),
                      "dups": [[r["name"] + "@" + str(r["page"]) for r in g] for g in dup_groups.values()]},
                     ensure_ascii=False))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

# 2026-11-06 피그마에서 바뀐 즐겨찾기(menu/ui-icon-action)·관심(menu/ui-icon-favorite) 아이콘을 조각 파일에 반영
import os, re
here = os.path.dirname(os.path.abspath(__file__))
STAR = 'M8.00 12.27L3.67 14.5L4.50 9.79L1 6.46L5.83 5.77L8 1.5L10.16 5.77L15 6.46L11.49 9.79L12.32 14.5L8.00 12.27Z'
HEART = 'M13.49 3.06C13.17 2.72 12.80 2.45 12.38 2.27C11.97 2.09 11.52 2 11.07 2C10.62 2 10.18 2.09 9.76 2.27C9.35 2.45 8.97 2.72 8.65 3.06L7.99 3.75L7.34 3.06C6.69 2.38 5.82 2.00 4.92 2.00C4.01 2.00 3.14 2.38 2.50 3.06C1.86 3.73 1.5 4.66 1.5 5.62C1.5 6.58 1.86 7.50 2.50 8.18L3.16 8.87L7.99 14L12.83 8.87L13.49 8.18C13.81 7.84 14.06 7.44 14.23 7.00C14.41 6.56 14.5 6.09 14.5 5.62C14.5 5.14 14.41 4.67 14.23 4.23C14.06 3.79 13.81 3.39 13.49 3.06Z'
def sym(i, d, fill=None, stroke='#BBBDC4'):
    f = f' fill="{fill}"' if fill else ''
    return f'<symbol id="{i}" viewBox="0 0 16 16" fill="none"><path d="{d}"{f} stroke="{stroke}" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/></symbol>'
NEW = {
  'ls8':  sym('ls8', STAR),                              # 즐겨찾기 기본
  'ls8h': sym('ls8h', STAR, '#BBBDC4'),                  # 마우스 올림
  'ls8f': sym('ls8f', STAR, '#FFA000', '#FFA000'),       # 선택(active)
  'rs3':  sym('rs3', HEART),                             # 관심 기본
  'rs5':  sym('rs5', HEART, '#BBBDC4'),                  # 마우스 올림
  'rs6':  sym('rs6', HEART, '#FFA000', '#FFA000'),       # 선택(selected)
}
def patch(fn, ids):
    p = os.path.join(here, fn); t = open(p, encoding='utf-8').read()
    for i in ids:
        pat = re.compile(r'<symbol id="%s" .*?</symbol>' % re.escape(i), re.S)
        if pat.search(t): t = pat.sub(lambda m: NEW[i], t, count=1)
        else: t = t.replace('<!--@@ICONS-->', NEW[i] + '<!--@@ICONS-->') if '<!--@@ICONS-->' in t else t.rstrip('\n') + NEW[i] + '\n'
    open(p, 'w', encoding='utf-8').write(t); print(fn, 'ok')
patch('parts/3-left-footer.txt', ['ls8', 'ls8h'])
patch('parts/4-right.txt', ['rs3', 'rs5', 'rs6'])
patch('template.html', ['ls8f'])

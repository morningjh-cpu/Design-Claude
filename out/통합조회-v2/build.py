# 피그마 '이걸로 HTML 만들어봐'(14294:77567)에서 뽑은 조각(parts/*.txt)을 index.html 하나로 합친다.
# 조각은 피그마 레이어 구조·크기·여백·선·색을 그대로 옮긴 것이고, 아이콘은 피그마에서 SVG로 직접 내보낸 것이다.
import os, re
here = os.path.dirname(os.path.abspath(__file__))
def load(name):
    t = open(os.path.join(here, 'parts', name), encoding='utf-8').read()
    css = t.split('@@CSS\n')[1].split('\n@@HTML\n')[0]
    html = t.split('\n@@HTML\n')[1].split('\n@@DEFS\n')[0]
    defs = t.split('\n@@DEFS\n')[1].strip()
    return css, html, defs
nav = load('1-nav.txt'); con = load('2-contents.txt'); lf = load('3-left-footer.txt'); rt = load('4-right.txt')
left_html, footer_html = lf[1].split('@@FOOTER')

page = open(os.path.join(here, 'template.html'), encoding='utf-8').read()
out = (page.replace('/*@@CSS*/', '\n'.join([nav[0], con[0], lf[0], rt[0]]))
           .replace('<!--@@DEFS-->', nav[2] + con[2] + lf[2] + rt[2])
           .replace('<!--@@NAV-->', nav[1])
           .replace('<!--@@LEFT-->', left_html)
           .replace('<!--@@CONTENTS-->', con[1])
           .replace('<!--@@FOOTER-->', footer_html)
           .replace('<!--@@RIGHT-->', rt[1]))
open(os.path.join(here, 'index.html'), 'w', encoding='utf-8').write(out)
print('ok', len(out))

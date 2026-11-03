// 공지사항 - 목록(12533:4710) 을 복제해 스킬별 안으로 고치는 피그마 스크립트 (use_figma 용)
// 맨 위 KIND(1~5)·X 만 바꿔서 돌린다. 계획: plan/phase-1/12
const KIND = __KIND__;
const X = __X__;
const NAMES = { 1: '① impeccable', 2: '② taste-skill', 3: '③ ui-ux-pro-max', 4: '④ frontend-design', 5: '⑤ 조합' };

const page = await figma.getNodeByIdAsync('10394:30337');
await figma.setCurrentPageAsync(page);
const src = await figma.getNodeByIdAsync('12533:4710');
const f = src.clone();
page.appendChild(f);
f.x = X; f.y = 4100;
f.name = '공지사항 - 목록 · ' + NAMES[KIND];

const q = n => f.findOne(x => x.name === n);
const hex = h => ({ r: parseInt(h.slice(1, 3), 16) / 255, g: parseInt(h.slice(3, 5), 16) / 255, b: parseInt(h.slice(5, 7), 16) / 255 });
const solid = (h, o) => [o === undefined ? { type: 'SOLID', color: hex(h) } : { type: 'SOLID', color: hex(h), opacity: o }];
const log = [];

const mc = q('main-contents');
const list = q('cards-list');
const pinnedRow = q('pinned-row');
const pinned = pinnedRow.children.slice();
const rowFrames = ['row-1', 'row-2', 'row-3'].map(q);
const regular = rowFrames.flatMap(r => r.children.slice());
const line = list.findOne(x => x.type === 'LINE');
const tagText = tag => tag.findOne(n => n.type === 'TEXT');

function toolbar() {
  const search = q('service-search-bar');
  const bar = q('search-section');
  bar.insertChild(0, search);
  bar.primaryAxisAlignItems = 'SPACE_BETWEEN';
  bar.counterAxisAlignItems = 'CENTER';
  bar.counterAxisSizingMode = 'AUTO';
  return { search, bar, btn: q('btn-write (관리자 전용)') };
}
function bigTargets(search, btn) {
  search.resize(560, 44);
  try { btn.setProperties({ size: 'md' }); log.push('btn md'); } catch (e) { log.push('btn md 없음'); }
  if (btn.height < 44) { btn.resize(Math.max(btn.width, 96), 44); }
  const pag = q('pagination');
  pag.itemSpacing = 8;
  for (const p of pag.children) p.resize(40, 40);
}
function oneLineRows(cards, holder, style) {
  for (const card of cards) {
    const d = card.detachInstance();
    const date = d.findOne(n => n.name === 'date');
    const title = d.findOne(n => n.name === 'title');
    const tag = d.findOne(n => n.name === 'type-tag');
    const row = figma.createAutoLayout('HORIZONTAL', { name: 'notice-row', itemSpacing: 40 });
    row.counterAxisAlignItems = 'CENTER';
    row.paddingLeft = 24; row.paddingRight = 24;
    holder.appendChild(row);
    row.resize(1280, 64);
    row.layoutSizingHorizontal = 'FILL';
    row.layoutSizingVertical = 'FIXED';
    const dateBox = figma.createAutoLayout('HORIZONTAL', { name: 'date-col' });
    row.appendChild(dateBox);
    dateBox.appendChild(date);
    dateBox.resize(96, dateBox.height);
    dateBox.layoutSizingHorizontal = 'FIXED';
    dateBox.fills = [];
    row.appendChild(title);
    // 카드 안에서 세로로 늘어나던 설정을 끊고 18px 로 (글자 크기는 직접 못 바꿔서 비율로)
    title.rescale(0.9);
    title.layoutSizingVertical = 'FIXED';
    title.resize(title.width, Math.ceil(title.fontSize * 1.35));
    title.layoutSizingHorizontal = 'FILL';
    row.appendChild(tag);
    style(row);
    d.remove();
  }
}
function twoLineRows(cards, holder) {
  for (const card of cards) {
    const d = card.detachInstance();
    const date = d.findOne(n => n.name === 'date');
    const title = d.findOne(n => n.name === 'title');
    const tag = d.findOne(n => n.name === 'type-tag');
    const row = figma.createAutoLayout('HORIZONTAL', { name: 'notice-row', itemSpacing: 24 });
    row.counterAxisAlignItems = 'CENTER';
    row.paddingLeft = 24; row.paddingRight = 24; row.paddingTop = 20; row.paddingBottom = 20;
    holder.appendChild(row);
    row.layoutSizingHorizontal = 'FILL';
    const left = figma.createAutoLayout('VERTICAL', { name: 'text', itemSpacing: 8 });
    left.fills = [];
    row.appendChild(left);
    left.layoutSizingHorizontal = 'FILL';
    left.appendChild(title);
    title.layoutSizingVertical = 'FIXED';
    title.resize(title.width, Math.ceil(title.fontSize * 1.35));
    title.layoutSizingHorizontal = 'FILL';
    left.appendChild(date);
    row.appendChild(tag);
    row.fills = solid('#ffffff');
    row.strokes = solid('#ececf0');
    row.strokeTopWeight = 0; row.strokeLeftWeight = 0; row.strokeRightWeight = 0; row.strokeBottomWeight = 1;
    d.remove();
  }
}
function darkBand() {
  pinnedRow.fills = solid('#2b2570');
  pinnedRow.paddingLeft = pinnedRow.paddingRight = 36;
  pinnedRow.paddingTop = pinnedRow.paddingBottom = 32;
  pinnedRow.cornerRadius = 16;
  pinnedRow.itemSpacing = 24;
  pinnedRow.counterAxisSizingMode = 'AUTO';
  for (const c of pinned) {
    c.fills = []; c.strokes = [];
    c.paddingLeft = 0; c.paddingRight = 0; c.paddingTop = 0; c.paddingBottom = 0;
    c.layoutSizingHorizontal = 'FILL';
    c.findOne(n => n.name === 'title').fills = solid('#ffffff');
    c.findOne(n => n.name === 'date').fills = solid('#c9c5f2');
    c.findOne(n => n.name === 'summary').fills = solid('#dcdaf6');
    c.findOne(n => n.name === 'pin-label').fills = solid('#b7b0ff');
    const tag = c.findOne(n => n.name === 'type-tag');
    tag.fills = []; tag.strokes = solid('#ffffff', 0.4);
    tagText(tag).fills = solid('#ffffff');
  }
}

if (line) line.remove();

if (KIND === 1) {
  toolbar();
  for (const c of pinned) { c.strokes = []; c.fills = solid('#f4f3fd'); }
  const table = figma.createAutoLayout('VERTICAL', { name: 'notice-table', itemSpacing: 0 });
  table.fills = [];
  list.appendChild(table);
  table.layoutSizingHorizontal = 'FILL';
  table.strokes = solid('#17181c');
  table.strokeTopWeight = 1; table.strokeLeftWeight = 0; table.strokeRightWeight = 0; table.strokeBottomWeight = 0;
  oneLineRows(regular, table, row => {
    row.fills = [];
    row.strokes = solid('#ececf0');
    row.strokeTopWeight = 0; row.strokeLeftWeight = 0; row.strokeRightWeight = 0; row.strokeBottomWeight = 1;
  });
  list.itemSpacing = 40;
}
if (KIND === 2) {
  const search = q('service-search-bar');
  search.strokes = []; search.fills = solid('#f1f2f4');
  pinnedRow.fills = solid('#f1f0fc');
  pinnedRow.paddingLeft = pinnedRow.paddingRight = pinnedRow.paddingTop = pinnedRow.paddingBottom = 28;
  pinnedRow.cornerRadius = 8;
  pinnedRow.counterAxisSizingMode = 'AUTO';
  for (const c of pinned) {
    c.fills = []; c.strokes = []; c.paddingLeft = 0; c.paddingRight = 0;
    c.layoutSizingHorizontal = 'FILL';
    const tag = c.findOne(n => n.name === 'type-tag');
    tag.strokes = []; tag.fills = solid('#ffffff'); tagText(tag).fills = solid('#3b3494');
  }
  for (const c of regular) {
    c.fills = solid('#f5f6f8'); c.strokes = []; c.cornerRadius = 6;
    const tag = c.findOne(n => n.name === 'type-tag');
    tag.strokes = []; tag.fills = solid('#ecebfb'); tagText(tag).fills = solid('#3b3494');
  }
  for (const r of rowFrames) r.itemSpacing = 12;
  list.itemSpacing = 12;
  list.paddingTop = 0;
  // 띠와 일반 카드 사이만 넓게
  const spacer = figma.createFrame(); spacer.name = 'gap'; spacer.fills = []; spacer.resize(10, 20);
  list.insertChild(1, spacer);
}
if (KIND === 3) {
  const t = toolbar();
  bigTargets(t.search, t.btn);
  for (const c of pinned) c.fills = solid('#f4f3fd');
  const box = figma.createAutoLayout('VERTICAL', { name: 'notice-list', itemSpacing: 0 });
  box.fills = [];
  list.appendChild(box);
  box.layoutSizingHorizontal = 'FILL';
  box.strokes = solid('#d6d8db');
  box.strokeTopWeight = 1; box.strokeLeftWeight = 0; box.strokeRightWeight = 0; box.strokeBottomWeight = 0;
  twoLineRows(regular, box);
  list.itemSpacing = 32;
}
if (KIND === 4) {
  darkBand();
  for (const c of regular) {
    c.fills = []; c.cornerRadius = 0;
    c.strokes = solid('#17181c');
    c.strokeTopWeight = 2; c.strokeLeftWeight = 0; c.strokeRightWeight = 0; c.strokeBottomWeight = 0;
    c.paddingLeft = 0; c.paddingRight = 0; c.paddingTop = 20;
  }
  for (const r of rowFrames) r.itemSpacing = 32;
  list.itemSpacing = 40;
}
if (KIND === 5) {
  const t = toolbar();
  bigTargets(t.search, t.btn);
  t.search.strokes = []; t.search.fills = solid('#f1f2f4');
  darkBand();
  const table = figma.createAutoLayout('VERTICAL', { name: 'notice-table', itemSpacing: 6 });
  table.fills = [];
  list.appendChild(table);
  table.layoutSizingHorizontal = 'FILL';
  oneLineRows(regular, table, row => {
    row.fills = solid('#f6f6f9');
    row.cornerRadius = 8;
    const tag = row.findOne(n => n.name === 'type-tag');
    tag.strokes = []; tag.fills = solid('#ffffff');
  });
  list.itemSpacing = 32;
}

if (KIND === 1 || KIND === 3 || KIND === 5) for (const r of rowFrames) r.remove();

// 높이 맞추기: 안쪽부터 내용에 맞추고, 맨 위 틀은 푸터 아래끝 기준
for (const n of ['cards-list', 'content', 'contents', 'Frame 9920']) {
  const node = q(n);
  if (node && node.layoutMode !== 'NONE') { try { node.layoutSizingVertical = 'HUG'; } catch (e) { node.primaryAxisSizingMode = 'AUTO'; } }
}
try { mc.layoutSizingVertical = 'HUG'; } catch (e) { mc.primaryAxisSizingMode = 'AUTO'; }
const area = q('container-area');
area.resize(1920, mc.height + 44);
for (const m of area.children) if (m !== mc) { try { m.layoutSizingVertical = 'FILL'; } catch (e) { /* 그대로 */ } }
const container = q('container');
container.resize(1920, q('top-area').height + area.height);
f.resize(1920, container.height);

await f.screenshot({ scale: 0.4 });
return { frameId: f.id, name: f.name, height: Math.round(f.height), log };

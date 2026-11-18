"""2026-11-18 Frank 的价目表（钢丝轮页）更正规格：尺寸、单只重量、装箱数、箱规。不公布价格。
在 merge_sizes_20261116.py 之后运行；从原始站点重建时只运行一次。
- 改写 11 个产品的配置选项、configuration-data、规格表几行和 JSON-LD
- 每个产品页在规格表后加「尺寸、重量和包装」表；磨料刷页去掉旧目录型号表
- 全站文字更正：尼龙孔 24.5 mm、8 寸除草轮 24 股、扭平 4–8 寸、磨料尺寸、交期 10–30 天、M10×1.25 常规、定制插卡起订 3000/款
"""
from pathlib import Path
import html, json, re, sys

R = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
esc = lambda s: html.escape(str(s), quote=True)
INCH = {65: '2.5', 75: '3', 85: '3.5', 100: '4', 115: '4.5', 125: '5', 150: '6', 175: '7', 200: '8', 250: '10', 300: '12'}
ASK_EN, ASK_ES = 'Ask Frank.', 'Consulta a Frank.'


def inch(mm):
    return {'en': f'{INCH[mm]}" ({mm} mm)', 'es': f'{INCH[mm]}" ({mm} mm)'}


def mm(v):
    return {'en': f'{v} mm', 'es': f'{v} mm'}


def knots(i, n):
    return {'en': f'{i}" · {n} knots', 'es': f'{i}" · {n} haces'}


def bund(d, n):
    return {'en': f'{d} mm · {n} bundles', 'es': f'{d} mm · {n} haces'}


W = {
    'cu': ('Copper-coated steel', 'Acero cobrizado'),
    'c': ('Carbon steel', 'Acero al carbono'),
    'blk': ('Black steel wire', 'Alambre negro'),
    'cu_blk': ('Copper-coated or black steel', 'Acero cobrizado o alambre negro'),
    'ny': ('Nylon', 'Nailon'),
    'ab': ('Abrasive nylon filament', 'Filamento de nailon abrasivo'),
}
# (pid, [(form_en, form_es, wire, [(size, size_mm, weight_g, pcs, carton)])])
G = lambda f_en, f_es, w, rows: (f_en, f_es, w, rows)
D = {
    '10': [G('Crimped cup brush', 'Copa de alambre ondulado', 'cu', [
        (inch(65), 65, 110, 100, '40×32×32'), (inch(75), 75, 160, 100, '42×30×42'), (inch(100), 100, 260, 60, '42×32×42'),
        (inch(125), 125, 450, 45, '46×40.5×40.5'), (inch(150), 150, 620, 24, '42×30×44')])],
    '8': [G('Knotted cup brush', 'Copa de alambre trenzado', 'c', [
        (inch(65), 65, 160, 100, '40×32×32'), (inch(75), 75, 200, 100, '42×30×42'), (inch(100), 100, 330, 60, '42×32×42'),
        (inch(125), 125, 490, 45, '46×40.5×40.5'), (inch(150), 150, 670, 24, '42×30×44')])],
    '4': [G('Banded knot cup brush', 'Copa trenzada con anillo', 'c', [
        (inch(65), 65, 275, 60, '42×30×26'), (inch(75), 75, 400, 45, '42×32×32'), (inch(85), 85, 460, 45, '42×32×32'),
        (inch(100), 100, 660, 30, '46×40.5×40.5'), (inch(125), 125, 1000, 24, '44×30×40')])],
    '7': [G('Arbor-hole wheel', 'Carda de orificio', 'cu', [
        (inch(100), 100, 180, 100, '47×36×27'), (inch(125), 125, 300, 60, '42×34×28'), (inch(150), 150, 500, 40, '40×32.5×32.5'),
        (inch(175), 175, 750, 20, '37×37×19'), (inch(200), 200, 850, 20, '42×37.5×21.5'), (inch(250), 250, None, None, None),
        (inch(300), 300, None, None, None)]),
          G('Bench wheel with bushings', 'Carda de banco con bujes', 'cu', [
        (inch(100), 100, 180, 100, '47×36×27'), (inch(125), 125, 240, 60, '42×34×28'), (inch(150), 150, 410, 40, '40×32.5×32.5'),
        (inch(175), 175, 470, 20, '37×37×19'), (inch(200), 200, 600, 20, '42×37×21.5'), (inch(250), 250, None, None, None),
        (inch(300), 300, None, None, None)])],
    '9': [G('Stringer bead knot wheel', 'Carda trenzada angosta', 'c', [
        (inch(100), 100, 180, 100, '47×36×27'), (inch(115), 115, None, None, None), (inch(125), 125, 260, 60, '42×34×28'),
        (inch(150), 150, 415, 40, '40×32.5×32.5'), (inch(175), 175, 470, 20, '37×37×19'), (inch(200), 200, 720, 20, '42×37×21.5')])],
    '2': [G('Knotted bevel brush', 'Cepillo cónico trenzado', 'c', [
        (inch(100), 100, 200, 100, '54.5×42×22'), (inch(115), 115, 260, 65, '42×32×42'), (inch(125), 125, 230, 60, '42×38×42')]),
          G('Crimped bevel brush', 'Cepillo cónico ondulado', 'c', [
        (inch(100), 100, 160, 100, '54.5×42×22'), (inch(115), 115, 175, 65, '42×32×42'), (inch(125), 125, 210, 60, '42×38×42')])],
    '28': [G('Twisted wire trimmer head', 'Cabezal de alambre trenzado', 'c', [
        (knots(6, 24), None, 400, 30, '47×23×32'), (knots(6, 30), None, 490, 30, '47×23×32'), (knots(8, 24), None, 520, 20, '41×32×41'),
        (knots(8, 30), None, 780, 20, '41×32×41'), (knots(8, 36), None, 830, 20, '41×32×41')])],
    '29': [G('3/6 bundle trimmer head', 'Cabezal de 3/6 haces', 'blk', [
        (bund(150, 3), None, 105, 60, '47×36×32'), (bund(150, 6), None, 120, 60, '47×36×32'), (bund(180, 3), None, 120, 40, '42×38×42'),
        (bund(180, 6), None, 148, 40, '42×38×42'), (bund(200, 3), None, 125, 40, '42×38×42'), (bund(200, 6), None, 164, 40, '42×38×42'),
        (bund(230, 3), None, 135, 30, '53×24×47'), (bund(230, 6), None, 175, 30, '53×24×47')])],
    '31': [G('Nylon trimmer brush', 'Cepillo de nailon para desbrozadora', 'ny', [
        ({'en': '6" (150 mm)', 'es': '6" (150 mm)'}, None, 350, 30, '47×23×32'),
        ({'en': '8" (200 mm)', 'es': '8" (200 mm)'}, None, 590, 20, '41×32×41')])],
    '1': [G('Abrasive cup brush', 'Copa de filamento abrasivo', 'ab', [
        (inch(65), 65, 115, 100, '40×32×32'), (inch(75), 75, 155, 100, '42×30×42'), (inch(100), 100, 240, 60, '42×32×42'),
        (inch(125), 125, 480, 45, None)]),
          G('Abrasive arbor-hole wheel', 'Disco abrasivo de orificio', 'ab', [
        (inch(100), 100, 105, 100, None), (inch(125), 125, 120, 100, None), (inch(150), 150, None, 100, None)]),
          G('Shank-mounted abrasive wheel, 6 mm (1/4") hex shank', 'Disco abrasivo con vástago hexagonal de 6 mm (1/4")', 'ab', [
        (mm(50), 50, 30, 700, None), (mm(65), 65, 40, 500, None), (mm(75), 75, 62, 400, None), (mm(100), 100, 105, 300, '42×32×42')]),
          G('Shank-mounted abrasive cup, 6 mm (1/4") hex shank', 'Copa abrasiva con vástago hexagonal de 6 mm (1/4")', 'ab', [
        (mm(50), 50, 55, 400, None), (mm(65), 65, 68, 300, None), (mm(75), 75, 82, 250, None), (mm(100), 100, 150, 150, None)]),
          G('Abrasive end brush, 6 mm (1/4") hex shank', 'Cepillo de punta abrasivo, vástago hexagonal de 6 mm (1/4")', 'ab', [
        (mm(25), 25, 40, 500, None), (mm(30), 30, 53, 400, None)])],
    '5': [G('Shank-mounted wheel brush', 'Carda circular con vástago', 'cu_blk', [
        (mm(38), 38, 25, 120, '53×27×31'), (mm(50), 50, 35, 120, '53×27×31'), (mm(65), 65, 50, 120, '53×27×31'),
        (mm(75), 75, 70, 120, '53×27×31'), (mm(100), 100, 100, 80, '50×33×36')]),
          G('Shank-mounted cup brush', 'Carda copa con vástago', 'cu_blk', [
        (mm(38), 38, None, 120, '53×27×31'), (mm(50), 50, 65, 120, '53×27×31'), (mm(65), 65, 75, 80, '53×27×31'),
        (mm(75), 75, 85, 80, '53×27×31'), (mm(100), 100, None, 80, '50×33×36')]),
          G('End brush', 'Cepillo de punta', 'cu_blk', [
        (mm(10), 10, 16, 200, '53×27×31'), (mm(12), 12, 21, 200, '53×27×31'), (mm(16), 16, 26, 200, '53×27×31'),
        (mm(19), 19, 30, 200, '53×27×31'), (mm(25), 25, 40, 200, '53×27×31'), (mm(30), 30, 60, 200, '53×27×31')])],
}
L = {'size': ('Size', 'Medida'), 'wire': ('Wire', 'Alambre'), 'w': ('Approx. weight', 'Peso aprox.'),
     'pcs': ('Pieces / carton', 'Piezas por caja'), 'dia': ('Wire diameter', 'Calibre (diámetro del alambre)'), 'ctn': ('Carton (cm)', 'Caja (cm)'), 'form': ('Brush form', 'Forma'),
     'od': ('Outside diameter', 'Diámetro exterior'), 'bore': ('Bore / thread / shank', 'Barreno / rosca / vástago'),
     'rpm': ('Maximum safe RPM', 'RPM máximas seguras')}
I = {'en': 0, 'es': 1}


def val(v, lang, unit=''):
    if v is None: return ASK_EN if lang == 'en' else ASK_ES
    return f'{v}{unit}'


BORE = {'28': ('25.4 mm', '25.4 mm'), '31': ('25.4 mm', '25.4 mm'),
        '29': ('5.5 mm (battery trimmers) or 25.4 mm (petrol brush cutters)', '5.5 mm (batería) o 25.4 mm (gasolina)')}


def dia(pid, form_en, lang='en'):
    """Frank 2026-11-18: 曲丝都是 0.3 丝，扭丝 0.5 丝（3/6 股也是扭丝）；带杆看丝的种类；磨料丝 1.3 mm"""
    if pid == '1': return '1.3 mm'
    if pid == '5': return '0.3 mm'  # 带杆轮/碗/笔刷都是曲丝（看图）
    if pid in ('10', '7') or 'Crimped' in form_en: return '0.3 mm'
    if pid in ('8', '4', '9', '28', '29') or 'Knotted' in form_en: return '0.5 mm'
    return None


def configs_for(pid):
    out = []
    groups = D[pid]
    for f_en, f_es, w, rows in groups:
        for size, smm, g, pcs, ctn in rows:
            def lab(lang):
                f = f_en if lang == 'en' else f_es
                return size[lang] if len(groups) == 1 else f'{f} · {size[lang]}'
            r = [{'en': [L['form'][0], f_en], 'es': [L['form'][1], f_es]},
                 {'en': [L['od'][0] if smm or pid in ('31',) else L['size'][0], size['en']], 'es': [L['od'][1] if smm or pid in ('31',) else L['size'][1], size['es']]},
                 {'en': [L['wire'][0], W[w][0]], 'es': [L['wire'][1], W[w][1]]},
                 *([{'en': [L['dia'][0], dia(pid, f_en)], 'es': [L['dia'][1], dia(pid, f_en, 'es')]}] if dia(pid, f_en) else []),
                 {'en': [L['w'][0], val(g, 'en', ' g')], 'es': [L['w'][1], val(g, 'es', ' g')]},
                 {'en': [L['pcs'][0], val(pcs, 'en')], 'es': [L['pcs'][1], val(pcs, 'es')]},
                 {'en': [L['ctn'][0], val(ctn, 'en')], 'es': [L['ctn'][1], val(ctn, 'es')]},
                 {'en': [L['bore'][0], BORE.get(pid, (ASK_EN, ASK_ES))[0]], 'es': [L['bore'][1], BORE.get(pid, (ASK_EN, ASK_ES))[1]]},
                 {'en': [L['rpm'][0], ASK_EN], 'es': [L['rpm'][1], ASK_ES]}]
            e = {'en': lab('en'), 'es': lab('es'), 'rows': r}
            if smm: e['sizeMm'] = smm
            out.append(e)
    return out


def table_html(pid, lang):
    i = I[lang]
    h = ('Sizes, weight and packing', 'Medidas, peso y empaque')[i]
    note = ('Weight is approximate, per piece. Pieces per carton depend on the packaging you choose (blister card or colour box); '
            'Frank confirms them with your order. "Ask Frank" means the size is made but the packing data is confirmed per order.',
            'El peso es aproximado, por pieza. Las piezas por caja dependen del empaque que elijas (blíster con tarjeta o caja a color); '
            'Frank las confirma con tu pedido. "Consulta a Frank" indica que la medida se fabrica y el empaque se confirma en cada pedido.')[i]
    s = f'<section id="sizes-packing"><h2>{h}</h2><p class="fine">{esc(note)}</p>'
    for f_en, f_es, w, rows in D[pid]:
        f = (f_en, f_es)[i]
        d = dia(pid, f_en, lang); d = f' · {L["dia"][i]}: {d}' if d else ''
        s += f'<h3>{esc(f)}</h3><p class="fine">{L["wire"][i]}: {esc(W[w][i])}{esc(d)}</p>'
        s += f'<div aria-label="{esc(f)}" class="catalog-spec-scroll" role="region" tabindex="0"><table class="spec-table catalog-model-table"><thead><tr>'
        s += ''.join(f'<th scope="col">{L[k][i]}</th>' for k in ('size', 'w', 'pcs', 'ctn')) + '</tr></thead><tbody>'
        for size, smm, g, pcs, ctn in rows:
            s += (f'<tr><td>{esc(size[lang])}</td><td>{esc(val(g, lang, " g"))}</td><td>{esc(val(pcs, lang))}</td>'
                  f'<td>{esc(val(ctn, lang))}</td></tr>')
        s += '</tbody></table></div>'
    chart = ('/guides/wire-brush-size-and-packing-chart/', 'See all sizes in one packing chart (m³ per carton) →') if lang == 'en' else \
            ('/es/guias/tabla-de-medidas-y-empaque-de-cardas/', 'Ver todas las medidas en una sola tabla de empaque (m³ por caja) →')
    return s + f'<p><a href="{chart[0]}">{chart[1]}</a></p></section>'


# ---------------- 1. 全站文字更正（先做，避免与下面新写的值重复替换） ----------------
REPL = [
    ('22.5 mm', '25.4 mm'),
    ('The catalog runs from 80 to 320. Grit 80 is the most ordered.', 'Standard is grit 80 with 1.3 mm filament; 60 or 120 is made on request.'),
    ('El catálogo va de 80 a 320. El grano 80 es el más pedido.', 'El estándar es grano 80 con filamento de 1.3 mm; 60 o 120 se hacen sobre pedido.'),
    (', and 240 or 320 are used for finishing.', '.'), (', y 240 o 320 se usan para acabado.', '.'),
    ('The catalog covers grit 80 to 320.', 'Grit 60 and 120 are made on request.'),
    ('El catálogo cubre grano 80 a 320.', 'Los granos 60 y 120 se hacen sobre pedido.'),
    ('diferencia con la carda de alambre, grano 80 a 320,', 'diferencia con la carda, grano 80 (60/120 sobre pedido),'),
    ('grit 80 to 320', 'grit 80 (60/120 on request)'), ('grano 80 a 320', 'grano 80 (60/120 sobre pedido)'),
    ('80 to 320', '80 (60/120 on request)'), ('80 a 320', '80 (60/120 sobre pedido)'),
    ('0.5 mm; confirm for the selected model.', '0.5 mm (all knotted/twisted wire models)'),
    ('0.3 mm; confirm for the selected model.', '0.3 mm (all crimped wire models)'),
    ('0.5 mm; confirmar para el modelo elegido.', '0.5 mm (todos los modelos de alambre trenzado)'),
    ('0.3 mm; confirmar para el modelo elegido.', '0.3 mm (todos los modelos de alambre ondulado)'),
    ('Typical wire diameter', 'Wire diameter'), ('Diámetro típico del alambre', 'Calibre (diámetro del alambre)'),
    ('Diámetro del alambre', 'Calibre (diámetro del alambre)'),
    ('Medidas de carda: diámetro, rosca y orificio', 'Medidas de carda: diámetro, rosca y barreno'),
    ('Confirmación de orificio, rosca o vástago', 'Confirmación de barreno, rosca o vástago'),
    ('Indica diámetro exterior, orificio central, grano y respaldo para recibir un precio por volumen.',
     'Indica diámetro exterior, barreno, grano y respaldo para recibir un precio por volumen.'),
    ('orificio central', 'barreno (orificio central)'),
    ('Orificio de referencia: 25.4 mm', 'Barreno de referencia: 25.4 mm'),
    ('El orificio de referencia es de 25.4 mm', 'El barreno de referencia es de 25.4 mm'),
    ('la medida del orificio y la cantidad', 'la medida del barreno (orificio) y la cantidad'),
    ('30 or 36', '24, 30 or 36'), ('30 o 36', '24, 30 o 36'),
    ('4.5, 5, 6 or 7 in', '4, 4.5, 5, 6, 7 or 8 in'), ('4.5, 5, 6 and 7 in', '4, 4.5, 5, 6, 7 and 8 in'),
    ('4.5, 5, 6 o 7 pulgadas', '4, 4.5, 5, 6, 7 u 8 pulgadas'), ('4.5, 5, 6 y 7 pulgadas', '4, 4.5, 5, 6, 7 y 8 pulgadas'),
    ('(4.5 a 7 pulgadas)', '(4 a 8 pulgadas)'),
    ('Fine-bundle range: 4.5, 5, 6, 7 in', '4" (100 mm), 4.5" (115 mm), 5" (125 mm), 6" (150 mm), 7" (175 mm), 8" (200 mm)'),
    ('Gama de haces finos: 4.5, 5, 6, 7 pulgadas', '4" (100 mm), 4.5" (115 mm), 5" (125 mm), 6" (150 mm), 7" (175 mm), 8" (200 mm)'),
    ('Knotted end brushes run from 19 to 30 mm head diameter.', 'End brushes run from 10 to 30 mm head diameter.'),
    ('Las de punta trenzadas van de 19 a 30 mm de cabezal.', 'Las de punta van de 10 a 30 mm de cabezal.'),
    ('Catalog radial wheels', 'Radial wheels'), ('Circulares de catálogo', 'Circulares'), ('Los modelos circulares de catálogo', 'Los modelos circulares'),
    ('75 to 200 mm', '100 to 150 mm'), ('75 a 200 mm', '100 a 150 mm'), ('75–200 mm', '100–150 mm'),
    ('75 to 125 mm', '65 to 125 mm'), ('75 a 125 mm', '65 a 125 mm'), ('75–125 mm', '65–125 mm'),
    ('38 to 100 mm', '50 to 100 mm'), ('38 a 100 mm', '50 a 100 mm'), ('38–100 mm', '50–100 mm'),
    ('40 to 80 mm', '50 to 100 mm'), ('40 a 80 mm', '50 a 100 mm'), ('40–80 mm', '50–100 mm'),
    ('usually about 30 days for bulk orders, confirmed per order', '10 to 30 days for bulk orders, confirmed per order'),
    ('Bulk lead time is usually about 30 days, confirmed per order.', 'Bulk lead time is 10 to 30 days, confirmed per order.'),
    ('Production of a bulk order usually takes about 30 days and is confirmed for each order.', 'Production of a bulk order takes 10 to 30 days, confirmed for each order.'),
    ('suele ser de unos 30 días y se confirma en cada pedido', 'es de 10 a 30 días y se confirma en cada pedido'),
    ('M10 × 1.5 is our standard; M10 × 1.25 is made to order.', 'M10 × 1.5 is our standard; M10 × 1.25, M14 and 5/8"-11 are made to order.'),
    ('The threads we make most are <strong>M14</strong> (2.0 mm pitch) and <strong>M10</strong>.',
     'Our standard thread is <strong>M10 × 1.5</strong>; <strong>M14</strong> (2.0 mm pitch) and other threads are made to order.'),
    ('Las roscas que más fabricamos son <strong>M14</strong> (paso 2.0) y <strong>M10</strong>.',
     'Nuestra rosca estándar es <strong>M10 × 1.5</strong>; la <strong>M14</strong> (paso 2.0) y las demás roscas se hacen sobre pedido.'),
    ('The ones we make most are M14 and M10 (pitch 1.5 or 1.25; they are not interchangeable).',
     'Our standard is M10 × 1.5. M10 × 1.25 and M14 are made to order (M10 × 1.5 and M10 × 1.25 are not interchangeable).'),
    ('Las que más fabricamos son M14 y M10 (paso 1.5 o 1.25; no son intercambiables).',
     'La estándar es M10 × 1.5. La M10 × 1.25 y la M14 se hacen sobre pedido (M10 × 1.5 y M10 × 1.25 no son intercambiables).'),
    ('Small trial orders in standard packaging are accepted, without wholesale pricing.',
     'Custom-printed blister cards start at 3,000 pieces per model; below that we supply our standard card. Small trial orders in standard packaging are accepted, without wholesale pricing.'),
    ('Aceptamos pedidos pequeños de prueba con empaque estándar, sin precio de mayoreo.',
     'El blíster con tarjeta impresa con tu marca empieza en 3,000 piezas por modelo; por debajo enviamos nuestra tarjeta estándar. Aceptamos pedidos pequeños de prueba con empaque estándar, sin precio de mayoreo.'),
]
pages = [p for p in R.rglob('*.html') if 'scripts' not in p.parts]
hits = {o: 0 for o, _ in REPL}
SCRIPT = re.compile(r'(<script[^>]*type="application/(?:ld\+)?json"[^>]*>)(.*?)(</script>)', re.S)
jq = lambda s: json.dumps(s, ensure_ascii=False)[1:-1]


def rep_text(t):
    for o, n in REPL:
        for a, b in ((o, n), (esc(o), esc(n))) if esc(o) != o else ((o, n),):
            c = t.count(a)
            if c: hits[o] += c; t = t.replace(a, b)
    return t


def rep_json(t):
    for o, n in REPL:
        c = t.count(jq(o))
        if c: hits[o] += c; t = t.replace(jq(o), jq(n))
    return t


for p in pages:
    t = p.read_text(); parts = []; last = 0
    for m in SCRIPT.finditer(t):
        parts.append(rep_text(t[last:m.start()])); parts.append(m.group(1) + rep_json(m.group(2)) + m.group(3)); last = m.end()
    parts.append(rep_text(t[last:])); t2 = ''.join(parts)
    if t2 != t: p.write_text(t2)
for jf in ('products.json', 'product-specs.json', 'product-buying-questions.json', 'product-map.json'):
    f = R / jf
    if f.exists():
        t = f.read_text(); t2 = rep_json(t)
        if t2 != t: f.write_text(t2)
miss = [o for o, c in hits.items() if not c]
assert not miss, miss

# ---------------- 2. 配置、规格、产品页 ----------------
configs = json.loads((R / 'product-configurations.json').read_text())
specs = json.loads((R / 'product-specs.json').read_text())
mapping = json.loads((R / 'product-map.json').read_text())

# 规格行更新：(pid, 旧英文名, 新英文名, 新西文名, 新英文值, 新西文值)
SPEC = [
    ('1', 'Catalog outside diameters', 'Outside diameters', 'Diámetros exteriores',
     'Cup: 65, 75, 100, 125 mm; arbor-hole wheel: 100, 125, 150 mm; shank wheel: 50, 65, 75, 100 mm; shank cup: 50, 65, 75, 100 mm; end brush: 25, 30 mm.',
     'Copa: 65, 75, 100, 125 mm; disco de orificio: 100, 125, 150 mm; disco con vástago: 50, 65, 75, 100 mm; copa con vástago: 50, 65, 75, 100 mm; cepillo de punta: 25, 30 mm.'),
    ('1', 'Mounting', None, None,
     'Shank models: 6 mm (1/4") hex shank. Arbor-hole wheel bore and cup thread: ask Frank.',
     'Modelos con vástago: hexagonal de 6 mm (1/4"). Orificio del disco y rosca de la copa: consulta a Frank.'),
    ('1', 'Model and packing', 'Weight and packing', 'Peso y empaque',
     'Weight, pieces per carton and carton size by model are listed below. Packing changes are confirmed with the order.',
     'El peso, las piezas por caja y la medida de caja de cada modelo están abajo. Los cambios de empaque se confirman con el pedido.'),
    ('1', 'Catalog grit range', 'Grit and filament', 'Grano y filamento',
     'Standard: grit 80, 1.3 mm abrasive nylon filament. On request: grit 60 or 120, and softer or stiffer filament.',
     'Estándar: grano 80, filamento de nailon abrasivo de 1.3 mm. Sobre pedido: grano 60 o 120, y filamento más suave o más rígido.'),
    ('28', 'Series outside diameters', None, None, '6 in: 24 or 30 knots; 8 in: 24, 30 or 36 knots; 25.4 mm bore',
     '6 pulgadas: 24 o 30 haces; 8 pulgadas: 24, 30 o 36 haces; barreno de 25.4 mm'),
    ('29', 'Bundle count', None, None, '3 or 6 twisted bundles per head; 0.5 mm wire', '3 o 6 haces trenzados por cabezal; calibre 0.5 mm'),
    ('5', 'Brush shapes', None, None,
     'Wheel (38–100 mm), cup (38–100 mm) and end brush (10–30 mm); crimped copper-coated or black steel wire, 0.3 mm',
     'Circular (38–100 mm), copa (38–100 mm) y de punta (10–30 mm); alambre ondulado cobrizado o negro, calibre 0.3 mm'),
    ('30', 'Wire construction', None, None, 'Crimped wire, 0.3 mm', 'Alambre ondulado, calibre 0.3 mm'),
    ('2', 'Brush profile', None, None, 'Outward-angled bevel profile; knotted or crimped wire',
     'Perfil cónico hacia afuera; alambre trenzado u ondulado'),
    ('4', 'Series outside diameters', None, None,
     '2.5" (65 mm), 3" (75 mm), 3.5" (85 mm), 4" (100 mm), 5" (125 mm)', '2.5" (65 mm), 3" (75 mm), 3.5" (85 mm), 4" (100 mm), 5" (125 mm)'),
]
for pid, old, new_en, new_es, v_en, v_es in SPEC:
    row = next(r for r in specs[pid]['specifications'] if r['en'][0] == old)
    old_es, ov_en, ov_es = row['es'][0], row['en'][1], row['es'][1]
    row['en'] = [new_en or old, v_en]; row['es'] = [new_es or old_es, v_es]
    slug = mapping[pid]['slug']
    for lang, base, on, nn, ov, nv in (('en', R, old, new_en or old, ov_en, v_en), ('es', R / 'es', old_es, new_es or old_es, ov_es, v_es)):
        f = base / 'products' / slug / 'index.html'; t = f.read_text()
        t, n = re.subn(r'<tr><th scope="row">' + re.escape(esc(on)) + r'</th><td>[^<]*</td></tr>',
                       lambda m: f'<tr><th scope="row">{esc(nn)}</th><td>{esc(nv)}</td></tr>', t, count=1)
        assert n == 1, (f, on)
        t, n = re.subn(r'\{"@type": ?"PropertyValue", ?"name": ?' + re.escape(json.dumps(on, ensure_ascii=False)) + r', ?"value": ?"(?:[^"\\]|\\.)*"\}',
                       lambda m: json.dumps({'@type': 'PropertyValue', 'name': nn, 'value': nv}, ensure_ascii=False), t)
        f.write_text(t)

for pid in D:
    configs[pid] = configs_for(pid)
    slug = mapping[pid]['slug']
    for lang, base in (('en', R), ('es', R / 'es')):
        f = base / 'products' / slug / 'index.html'; t = f.read_text()
        opts = ''.join(f'<label class="configuration-card"><input name="configuration" type="radio" value="{i}"/><span>{esc(c[lang])}</span></label>'
                       for i, c in enumerate(configs[pid]))
        t, n = re.subn(r'(<fieldset class="configuration-options"><legend[^>]*>.*?</legend>).*?(<label class="configuration-card"><input name="configuration" type="radio" value="custom"/>)',
                       lambda m: m.group(1) + opts + m.group(2), t, count=1, flags=re.S)
        assert n == 1, f
        data = json.dumps(configs[pid], ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
        t, n = re.subn(r'(<script id="configuration-data" type="application/json">).*?(</script>)', lambda m: m.group(1) + data + m.group(2), t, count=1, flags=re.S)
        assert n == 1, f
        t = re.sub(r'<section id="catalog-models">.*?</section>', '', t, flags=re.S)
        t = re.sub(r'<a class="underlink" href="/images/catalog/[^"]*"[^>]*>[^<]*</a>', '', t)  # catálogo viejo, ya no coincide
        t = re.sub(r'<section id="sizes-packing">.*?</section>', '', t, flags=re.S)
        t, n = re.subn(r'(<section id="product-specifications".*?</section>)', lambda m: m.group(1) + table_html(pid, lang), t, count=1, flags=re.S)
        assert n == 1, f
        f.write_text(t)

(R / 'product-configurations.json').write_text(json.dumps(configs, ensure_ascii=False, indent=2))
for k, v in specs.items():
    for r in v.get('specifications', []):
        for lang in ('en', 'es'):
            r[lang] = [next((n for o, n in REPL if o == x), x) for x in r[lang]]
(R / 'product-specs.json').write_text(json.dumps(specs, ensure_ascii=False, indent=2))
print('price list applied:', {o: c for o, c in hits.items()})

# ---------------- 3. Organization: año de fundación y personal (Frank: fábrica de 24 años en 2026, ~50 trabajadores) ----------------
ORG = '"@type":"Organization","@id":"https://yekaifrank.com/#organization",'
n_org = 0
for p in pages:
    t = p.read_text()
    if ORG in t and '"foundingDate"' not in t:
        t = t.replace(ORG, ORG + '"foundingDate":"2002","numberOfEmployees":{"@type":"QuantitativeValue","value":50},', 1)
        p.write_text(t); n_org += 1
print('organization updated on', n_org, 'pages')


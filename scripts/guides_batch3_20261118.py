"""2026-11-18 — guía 3ª tanda: tabla de medidas, peso y empaque de todas las cardas (EN/ES).
Datos: lista de precios de Frank (hoja 钢丝轮), SIN precios. Volumen por caja y piezas por m³ calculados de la medida de caja.
Importado por scripts/seo_mx_20261116.py.
"""
from pathlib import Path
import html, json

_ROOT = Path(__file__).resolve().parent.parent
_SRC = (Path(__file__).resolve().parent / 'price_list_20261118.py').read_text()
_NS = {'__file__': str(Path(__file__).resolve().parent / 'price_list_20261118.py')}
exec(_SRC.split('# ---------------- 1.')[0].replace('R = Path(sys.argv[1]) if len(sys.argv) > 1 else', 'R ='), _NS)
D, W, dia, val = _NS['D'], _NS['W'], _NS['dia'], _NS['val']
esc = lambda s: html.escape(str(s), quote=True)
P = lambda s: f'<p>{s}</p>'
_MAP = json.loads((_ROOT / 'product-map.json').read_text())
_NAMES = {str(p['id']): p for p in json.loads((_ROOT / 'products.json').read_text())}
ORDER = ['8', '10', '4', '2', '9', '7', '5', '1', '28', '29', '31']

SLUG_EN, SLUG_ES = 'wire-brush-size-and-packing-chart', 'tabla-de-medidas-y-empaque-de-cardas'
PAIR3 = {SLUG_ES: SLUG_EN}
GUIDES_EN3 = [(SLUG_EN, 'Wire brush sizes, weights and carton packing chart')]
GUIDES_ES3 = [(SLUG_ES, 'Tabla de medidas, peso y empaque de cardas')]

T = {
    'en': dict(size='Size', dia='Wire', w='Weight / pc', pcs='Pcs / carton', ctn='Carton (cm)', cbm='m³ / carton',
               per='≈ pcs / m³', kg='≈ brush kg / carton', ask='Ask Frank', prod='/products/', see='See the product page →'),
    'es': dict(size='Medida', dia='Calibre', w='Peso / pza', pcs='Pzas / caja', ctn='Caja (cm)', cbm='m³ / caja',
               per='≈ pzas / m³', kg='≈ kg de cardas / caja', ask='Consulta a Frank', prod='/es/products/', see='Ver la página del producto →'),
}


def _cbm(ctn):
    if not ctn: return None
    a, b, c = (float(x) for x in ctn.split('×'))
    return a * b * c / 1_000_000


def _num(x, d=3):
    return f'{x:.{d}f}'.rstrip('0').rstrip('.')


def _tables(lang):
    t = T[lang]; i = 0 if lang == 'en' else 1
    out = []
    for pid in ORDER:
        name = _NAMES[pid][lang]; slug = _MAP[pid]['slug']
        out.append(f'<h2 id="p{pid}">{esc(name)}</h2>')
        for f_en, f_es, w, rows in D[pid]:
            f = f_en if lang == 'en' else f_es
            d = dia(pid, f_en, lang)
            out.append(f'<h3>{esc(f)}</h3><p class="fine">{esc(W[w][i])}{" · " + esc(t["dia"]) + " " + esc(d) if d else ""}</p>')
            h = ''.join(f'<th>{t[k]}</th>' for k in ('size', 'w', 'pcs', 'ctn', 'cbm', 'per', 'kg'))
            body = ''
            for size, smm, g, pcs, ctn in rows:
                cbm = _cbm(ctn)
                cells = [size[lang], f'{g} g' if g else t['ask'], pcs or t['ask'], ctn or t['ask'],
                         _num(cbm, 4) if cbm else '—',
                         f'{round(pcs / cbm / 10) * 10:,}' if (cbm and pcs) else '—',
                         _num(g * pcs / 1000, 1) if (g and pcs) else '—']
                body += '<tr>' + ''.join(f'<td>{esc(c)}</td>' for c in cells) + '</tr>'
            out.append(f'<div class="catalog-spec-scroll" role="region" tabindex="0" aria-label="{esc(f)}">'
                       f'<table class="guide-table"><thead><tr>{h}</tr></thead><tbody>{body}</tbody></table></div>')
        out.append(P(f'<a href="{t["prod"]}{slug}/">{t["see"]}</a>'))
    return out


_EN_INTRO = [
    P('This chart lists every size we have packing data for: weight per piece, pieces per export carton and carton size. '
      'We added two figures that importers usually work out by hand: the <strong>carton volume in m³</strong> and roughly '
      '<strong>how many pieces fit in one cubic metre</strong>. Prices are not published here; ask Frank for a quote.'),
    '<h2>How to use the chart</h2>',
    '<ul><li><strong>m³ per carton</strong> = length × width × height in cm ÷ 1,000,000.</li>'
    '<li><strong>Pieces per m³</strong> = pieces per carton ÷ m³ per carton, rounded. Use it to estimate how much of an LCL '
    'shipment or a container a mixed order fills.</li>'
    '<li><strong>Brush kg per carton</strong> = weight per piece × pieces. Add the carton and the inner packaging for gross weight.</li>'
    '<li>Counts are for our standard packing. Blister cards, double blisters and colour boxes change the count per carton; '
    'Frank confirms the final packing list with your order.</li></ul>',
    P('Wire diameter: all crimped-wire models use 0.3 mm wire and all knotted (twisted) models use 0.5 mm. '
      'Abrasive brushes use 1.3 mm abrasive nylon filament, grit 80 as standard.'),
]
_ES_INTRO = [
    P('Esta tabla reúne todas las medidas de las que tenemos datos de empaque: peso por pieza, piezas por caja de exportación '
      'y medida de la caja. Agregamos dos datos que el importador suele calcular a mano: el <strong>volumen de cada caja en m³</strong> '
      'y cuántas <strong>piezas caben aproximadamente en un metro cúbico</strong>. Aquí no publicamos precios; pide tu cotización a Frank.'),
    '<h2>Cómo usar la tabla</h2>',
    '<ul><li><strong>m³ por caja</strong> = largo × ancho × alto en cm ÷ 1,000,000.</li>'
    '<li><strong>Piezas por m³</strong> = piezas por caja ÷ m³ por caja, redondeado. Sirve para estimar cuánto ocupa un pedido '
    'mixto en un envío consolidado (LCL) o en un contenedor.</li>'
    '<li><strong>Kg de cardas por caja</strong> = peso por pieza × piezas. Para el peso bruto suma la caja y el empaque interior.</li>'
    '<li>Las cantidades son de nuestro empaque estándar. El blíster con tarjeta, el doble blíster y la caja a color cambian las piezas '
    'por caja; Frank confirma la lista de empaque final con tu pedido.</li></ul>',
    P('Calibre: todas las cardas de alambre ondulado usan alambre de 0.3 mm y todas las de alambre trenzado, de 0.5 mm. '
      'Los cepillos abrasivos usan filamento de nailon abrasivo de 1.3 mm, grano 80 como estándar.'),
]

CONTENT_EN3 = {SLUG_EN: dict(
    title='Wire Brush Size, Weight and Carton Packing Chart',
    h1='Wire brush sizes, weights and carton packing chart',
    desc='Weight per piece, pieces per carton, carton size and m³ for our wire cup brushes, wheels, bevel, shank and trimmer brushes. Plan LCL or container loads.',
    body=_EN_INTRO + _tables('en'))}
CONTENT_ES3 = {SLUG_ES: dict(
    title='Tabla de medidas, peso y empaque de cardas',
    h1='Tabla de medidas, peso y empaque de cardas',
    desc='Peso por pieza, piezas por caja, medida de caja y m³ de nuestras cardas copa, circulares, cónicas, con vástago y para desbrozadora.',
    body=_ES_INTRO + _tables('es'))}
FAQ3 = {
    SLUG_EN: [
        ('How many wire cup brushes fit in one cubic metre?', 'It depends on the size. For example, 3-inch (75 mm) crimped cups pack 100 per 42×30×42 cm carton, about 1,890 pieces per m³. See the chart for each size.'),
        ('Are these net or gross weights?', 'The weight is per brush and approximate. Add the carton and inner packaging for gross weight; Frank sends the packing list with your order.'),
        ('Does custom packaging change the carton count?', 'Yes. Blister cards, double blisters and colour boxes change pieces per carton. The chart shows our standard packing.')],
    SLUG_ES: [
        ('¿Cuántas cardas copa caben en un metro cúbico?', 'Depende de la medida. Por ejemplo, la copa ondulada de 3 pulgadas (75 mm) va 100 por caja de 42×30×42 cm, unas 1,890 piezas por m³. Revisa la tabla de cada medida.'),
        ('¿El peso es neto o bruto?', 'Es el peso aproximado de cada carda. Para el peso bruto suma la caja y el empaque interior; Frank envía la lista de empaque con tu pedido.'),
        ('¿El empaque personalizado cambia las piezas por caja?', 'Sí. El blíster con tarjeta, el doble blíster y la caja a color cambian las piezas por caja. La tabla muestra nuestro empaque estándar.')],
}

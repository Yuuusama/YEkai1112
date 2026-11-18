"""2026-11-16 — SEO en español para Latinoamérica (idempotente). Ejecutar al final, después de los demás scripts.

1. Títulos, H1 y descripciones de páginas /es/ con los términos que se buscan en Latinoamérica
   (carda, esmeril, pulidora, taladro). No cambia datos de producto ni JSON protegidos.
2. Crea /es/guias/ con 8 guías (5 de ellas en guides_es_20261116.py, con FAQ) de compra en español y enlaces internos hacia los productos.
3. Agrega enlaces internos: About desde los dos inicios, guías desde páginas /es/.
4. Regenera sitemap.xml (todas las páginas indexables).

Uso:  python3 scripts/seo_mx_20261116.py  (desde la raíz del sitio)
"""
from pathlib import Path
import html, json, re, sys
import xml.etree.ElementTree as ET

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
BASE = 'https://yekaifrank.com'
TODAY = '2026-11-16'
WA = 'https://wa.me/8619883954016?text='

# ---------------------------------------------------------------- 1. metadatos ES
# ruta: (title sin " | YEKAI", h1, description)
ES = {
 '': ('Cardas de alambre al mayoreo directo de fábrica',
      None,
      'Cardas de alambre para esmeril y pulidora, copas y cepillos para desbrozadora, directo de fábrica en China. Cotiza al mayoreo y con tu marca con Frank.'),
 'steel-wire-wheel-brush': ('Cardas de alambre para esmeril y pulidora al mayoreo',
      'Cardas de alambre: circulares, de copa, trenzadas y onduladas',
      'Compara cardas circulares, de copa y cónicas, de alambre trenzado u ondulado, por diámetro, ancho y rosca u orificio. Envía la medida y cotiza al mayoreo.'),
 'abrasive-filament-brush': ('Cepillos de nylon abrasivo para acabado de metal',
      'Cepillos de nylon (filamento) abrasivo para acabado',
      'Cepillos de nylon abrasivo circulares, de copa o con vástago. Compara diámetro y grano y pide a Frank el modelo adecuado para el acabado que buscas.'),
 'abrasive-flap-disc': ('Discos laminados (flap) para metal al mayoreo',
      'Discos laminados (flap) para desbaste y acabado de metal',
      'Cotiza discos laminados tipo flap para trabajar metal. Indica diámetro exterior, orificio central, grano y respaldo para recibir un precio por volumen.'),
 'wire-grass-trimmer-head': ('Cepillos de alambre para desbrozadora al mayoreo',
      None, None),
 'products/twisted-wire-wheels': ('Carda cónica de alambre trenzado | Mayoreo y OEM',
      'Carda cónica de alambre trenzado',
      'Carda cónica de alambre trenzado de 4, 4.5 o 5 pulgadas, con haces inclinados de acero al carbono. Alambre típico: 0.5 mm. Consulta a Frank sobre el montaje.'),
 'products/copper-coated-wire-wheels': ('Carda circular de alambre cobrizado | Mayoreo y OEM',
      'Carda circular de alambre cobrizado',
      'Carda circular de alambre de acero cobrizado para preparar metal. Alambre típico: 0.3 mm. Consulta a Frank sobre diámetro, ancho y montaje.'),
 'products/banded-twisted-cup-brushes': ('Carda copa trenzada con aro | Mayoreo y OEM',
      'Carda copa trenzada con aro',
      'Carda copa para pulidora, trenzada, con aro de retención y acero al carbono, de 2.5, 3, 3.5, 4 o 5 pulgadas. Consulta a Frank para confirmar la rosca.'),
 'products/crimped-wire-brush-wheels': ('Carda circular de alambre ondulado | Mayoreo y OEM',
      'Carda circular de alambre ondulado',
      'Carda circular de alambre ondulado con centro metálico, para esmeril. Envía diámetro y foto del montaje; Frank confirma alambre, orificio y adaptador.'),
 'products/crimped-wire-cup-brushes': ('Carda copa de alambre ondulado | Mayoreo y OEM',
      'Carda copa de alambre ondulado',
      'Carda copa de alambre ondulado para pulidora, de 2.5, 3, 4, 5 o 6 pulgadas, para superficies metálicas. Consulta a Frank sobre el material y la rosca.'),
 'products/red-knotted-wire-cup-brush': ('Carda copa de alambre trenzado roja | Mayoreo y OEM',
      'Carda copa de alambre trenzado',
      'Carda copa roja de alambre trenzado de acero al carbono para pulidora, de 2.5, 3, 4, 5 o 6 pulgadas. Consulta a Frank para confirmar diámetro y rosca.'),
 'products/shaft-mounted-wire-wheels': ('Cardas con vástago para taladro | Mayoreo y OEM',
      'Cardas con vástago para taladro',
      'Cardas con vástago para taladro: de punta, circulares y de copa. Consulta a Frank para confirmar forma, diámetro del cabezal y medida del vástago.'),
 'products/stringer-knotted-wheels': ('Carda trenzada angosta para soldadura | Mayoreo',
      'Carda trenzada angosta para soldadura',
      'Carda de trenzado angosto, de haces finos, para limpiar cordones de soldadura; 4.5, 5, 6 o 7 pulgadas. Consulta a Frank sobre ancho y orificio.'),
 'products/wide-crimped-wire-wheels': ('Carda circular ancha de alambre ondulado | Mayoreo',
      'Carda circular ancha de alambre ondulado',
      'Carda ancha de alambre ondulado para esmeril, de 4, 5, 6, 7, 8, 10 o 12 pulgadas. Alambre típico: 0.3 mm. Consulta a Frank sobre ancho y orificio.'),
 'products/plastic-handle-hand-brushes': ('Cepillos de alambre con mango de plástico | Mayoreo',
      'Cepillos de alambre con mango de plástico', None),
 'products/blister-card-brush-sets': ('Juegos de cardas en blíster para ferretería',
      'Juegos de cardas y cepillos en blíster',
      'Juegos de cardas y cepillos en blíster con tarjeta para ferretería. Indica modelos, piezas por tarjeta y diseño del empaque para cotizar con Frank.'),
 'products/abrasive-filament-brushes': ('Cepillos de nylon abrasivo | Mayoreo y OEM',
      'Cepillos de nylon abrasivo (filamento)', None),
 'products/abrasive-flap-discs': ('Discos laminados flap abrasivos | Mayoreo y OEM',
      'Discos laminados flap abrasivos', None),
}

GUIDES = [
 ('carda-trenzada-o-ondulada', '¿Carda trenzada u ondulada? Cuál elegir'),
 ('medidas-de-carda', 'Medidas de carda: diámetro, rosca y orificio'),
 ('importar-cardas-de-china', 'Cómo importar cardas desde China'),
]
from guides_es_20261116 import MORE_GUIDES, MORE_CONTENT, FAQ
from guides_en_20261117 import PAIR, GUIDES_EN, CONTENT_EN, FAQ_EN, EN, RENAME_EN
FAQ.update(FAQ_EN)
from guides_batch2_20261117 import PAIR2, GUIDES_EN2, GUIDES_ES2, CONTENT_EN2, CONTENT_ES2, FAQ2
PAIR.update(PAIR2); GUIDES_EN += GUIDES_EN2; CONTENT_EN.update(CONTENT_EN2); FAQ.update(FAQ2)
GUIDES += GUIDES_ES2
from guides_batch3_20261118 import PAIR3, GUIDES_EN3, GUIDES_ES3, CONTENT_EN3, CONTENT_ES3, FAQ3
PAIR.update(PAIR3); GUIDES_EN += GUIDES_EN3; CONTENT_EN.update(CONTENT_EN3); FAQ.update(FAQ3); GUIDES += GUIDES_ES3
GUIDES += MORE_GUIDES
GUIDE_LINKS_HTML = ' · '.join(f'<a href="/es/guias/{s}/">{html.escape(t)}</a>' for s, t in GUIDES)


def esc(s): return html.escape(s, quote=True)


def set_meta(text, key, value, kind):
    pat = re.compile(r'<meta content="[^"]*" ' + kind + r'="' + re.escape(key) + r'"/>')
    new = f'<meta content="{esc(value)}" {kind}="{key}"/>'
    return pat.sub(lambda m: new, text, count=1)


def edit_jsonld(text, fn):
    def rep(m):
        raw = m.group(2)
        try:
            data = json.loads(raw)
        except ValueError:
            return m.group(0)
        fn(data)
        sep = (', ', ': ') if '", "' in raw else (',', ':')
        return m.group(1) + json.dumps(data, ensure_ascii=False, separators=sep) + m.group(3)
    return re.sub(r'(<script type="application/ld\+json">)(.*?)(</script>)', rep, text, flags=re.S)


def apply_meta(table=None, prefix='es/'):
    table = ES if table is None else table
    changed = []
    for path, (title, h1, desc) in table.items():
        f = ROOT / prefix / path / 'index.html'
        text = f.read_text(); orig = text
        url = f'{BASE}/{prefix}{path + "/" if path else ""}'
        full = f'{title} | YEKAI'
        old_h1 = None
        text = re.sub(r'<title>.*?</title>', lambda m: f'<title>{esc(full)}</title>', text, count=1, flags=re.S)
        text = set_meta(text, 'og:title', full, 'property')
        if desc:
            text = set_meta(text, 'description', desc, 'name')
            text = set_meta(text, 'og:description', desc, 'property')
        if h1:
            m = re.search(r'(<h1[^>]*>)(.*?)(</h1>)', text, re.S)
            old_h1 = html.unescape(re.sub('<[^>]+>', '', m.group(2))).strip()
            text = text[:m.start()] + m.group(1) + esc(h1) + m.group(3) + text[m.end():]
            # migas visibles
            text = text.replace(f'<span aria-current="page">{esc(old_h1)}</span>', f'<span aria-current="page">{esc(h1)}</span>')
            # el mensaje prellenado de WhatsApp debe nombrar el producto igual que el H1
            if old_h1 != h1 and path.startswith('products/'):
                from urllib.parse import quote
                text = text.replace(quote(old_h1, safe=''), quote(h1, safe=''))

        def fix(data):
            nodes = data.get('@graph', [data]) if isinstance(data, dict) else []
            for n in nodes:
                t = n.get('@type')
                if t == 'WebPage':
                    n['name'] = full
                    if desc: n['description'] = desc
                if t == 'Product':
                    if h1: n['name'] = h1
                    if desc: n['description'] = desc
                if t == 'BreadcrumbList' and h1:
                    for it in n.get('itemListElement', []):
                        if it.get('item') == url: it['name'] = h1
        text = edit_jsonld(text, fix)
        if path == '':  # H1 del inicio con <br>
            text = text.replace('<h1>Cepillos de alambre<br/>directo de fábrica</h1>',
                                '<h1>Cardas y cepillos de alambre<br/>directo de fábrica</h1>')
        if text != orig:
            f.write_text(text); changed.append(f)
    # El nombre de la categoría en migas/menú de productos (texto de enlace) se actualiza en todas las páginas ES
    return changed


# ---------------------------------------------------------------- 2. guías
P = lambda s: f'<p>{s}</p>'
def link(path, label): return f'<a href="{path}">{label}</a>'

GUIDE_CONTENT = {
'carda-trenzada-o-ondulada': dict(
 title='Carda trenzada u ondulada: cuál elegir',
 h1='¿Carda trenzada u ondulada? Cómo elegir la correcta',
 desc='Diferencias entre carda de alambre trenzado y ondulado, y entre carda circular, de copa, cónica y con vástago. Guía para ferreterías y distribuidores.',
 body=[
  P('En México y buena parte de Latinoamérica se le dice <strong>carda</strong> (en otros países, <strong>grata</strong> o simplemente cepillo de alambre) al cepillo de alambre que se monta en el esmeril, la pulidora (esmeriladora o amoladora angular) o el taladro. Antes de pedir precio conviene definir dos cosas: el <strong>tipo de alambre</strong> (ondulado o trenzado) y la <strong>forma</strong> de la carda (circular, de copa, cónica o con vástago).'),
  '<h2>Carda de alambre ondulado</h2>',
  P('Los alambres van sueltos y ondulados, así que la carda trabaja de forma más flexible. Se usa para limpieza ligera y media: quitar óxido superficial, pintura suelta o suciedad, y dejar un acabado más parejo en superficies amplias.'),
  P('En nuestro catálogo: ' + link('/es/products/crimped-wire-cup-brushes/', 'carda copa ondulada') + ' (2.5 a 6 pulgadas), ' + link('/es/products/wide-crimped-wire-wheels/', 'carda circular ancha ondulada') + ' (4 a 12 pulgadas, alambre típico de 0.3 mm) y ' + link('/es/products/crimped-wire-brush-wheels/', 'carda circular ondulada con centro metálico') + '.'),
  '<h2>Carda de alambre trenzado</h2>',
  P('El alambre va torcido en haces, lo que hace la carda más rígida y agresiva. Se elige para limpieza pesada: óxido grueso, cascarilla, escoria y cordones de soldadura.'),
  P('En nuestro catálogo: ' + link('/es/products/red-knotted-wire-cup-brush/', 'carda copa trenzada roja') + ' (2.5 a 6 pulgadas), ' + link('/es/products/banded-twisted-cup-brushes/', 'carda copa trenzada con aro') + ' (2.5 a 5 pulgadas), ' + link('/es/products/twisted-wire-wheels/', 'carda cónica trenzada') + ' (4 a 5 pulgadas, alambre típico de 0.5 mm) y ' + link('/es/products/stringer-knotted-wheels/', 'carda trenzada angosta para soldadura') + ' (4.5 a 7 pulgadas).'),
  '<h2>Comparación rápida</h2>',
  '<table class="guide-table"><thead><tr><th></th><th>Ondulada</th><th>Trenzada</th></tr></thead><tbody>'
  '<tr><th>Acción</th><td>Flexible, más suave</td><td>Rígida, más agresiva</td></tr>'
  '<tr><th>Trabajo típico</th><td>Óxido ligero, pintura suelta, limpieza general</td><td>Óxido pesado, cascarilla, cordones de soldadura</td></tr>'
  '<tr><th>Acabado</th><td>Más parejo</td><td>Más marcado</td></tr></tbody></table>',
  '<h2>Circular, copa, cónica o con vástago</h2>',
  P('<strong>Carda circular:</strong> trabaja con el canto; las de centro con orificio se montan normalmente en esmeril de banco. <strong>Carda copa:</strong> trabaja con la cara y se enrosca en la pulidora; sirve para superficies planas grandes. <strong>Carda cónica:</strong> llega a esquinas y bordes en la pulidora. <strong>Carda con vástago:</strong> para taladro, en huecos y zonas pequeñas (' + link('/es/products/shaft-mounted-wire-wheels/', 'ver cardas con vástago') + ').'),
  '<h2>Seguridad</h2>',
  P('La velocidad máxima (RPM) marcada en la carda debe ser igual o mayor que la de la máquina. Usa siempre la guarda, lentes y guantes. Confirma con Frank las RPM del modelo que elijas.'),
  '<h2>¿No sabes cuál pedir?</h2>',
  P('Manda por WhatsApp una foto de la carda que ya vendes o de la pieza que hay que limpiar, y Frank te dice el modelo equivalente. También puedes ver todas en ' + link('/es/steel-wire-wheel-brush/', 'cardas de alambre') + '.'),
 ]),
'medidas-de-carda': dict(
 title='Medidas de carda: diámetro, rosca y orificio',
 h1='Medidas de carda: qué datos mandar para cotizar',
 desc='Cómo indicar el diámetro, la rosca de pulidora (M14, M10 o 5/8"-11), el orificio para esmeril y el vástago al pedir cardas de alambre al mayoreo.',
 body=[
  P('Una cotización rápida y sin errores depende de cuatro medidas: <strong>diámetro exterior</strong>, <strong>montaje</strong> (rosca, orificio o vástago), <strong>alambre</strong> y <strong>cantidad por medida</strong>. Esta guía explica cada una.'),
  '<h2>1. Diámetro exterior</h2>',
  P('En América normalmente se piden en pulgadas; en fábrica se trabaja también en milímetros. Equivalencias aproximadas:'),
  '<table class="guide-table"><thead><tr><th>Pulgadas</th><th>Milímetros aprox.</th></tr></thead><tbody>'
  + ''.join(f'<tr><td>{a}"</td><td>{b} mm</td></tr>' for a, b in [('3', 75), ('4', 100), ('4.5', 115), ('5', 125), ('6', 150), ('7', 175), ('8', 200), ('10', 250)])
  + '</tbody></table>',
  P('Cada producto muestra sus diámetros disponibles en su página. Si el que necesitas no aparece, pregunta.'),
  '<h2>2. Montaje</h2>',
  P('<strong>Carda copa o cónica para pulidora:</strong> va roscada. Las roscas que más fabricamos son <strong>M14</strong> (paso 2.0) y <strong>M10</strong>. Ojo con la M10: existe en paso <strong>1.5</strong> (gruesa) y <strong>1.25</strong> (fina), muchas pulidoras de 4 pulgadas usan la fina y una no entra en la otra. La rosca <strong>5/8"-11</strong> se hace sobre pedido. Revisa cuál usan las pulidoras que venden tus clientes y dínoslo en el pedido.'),
  P('<strong>Carda circular para esmeril de banco:</strong> lleva un orificio central. Indica el diámetro de la flecha del esmeril; si el orificio es mayor se usan bujes o adaptadores, que también se confirman al cotizar.'),
  P('<strong>Carda con vástago para taladro:</strong> indica el diámetro del vástago y el del cabezal. Ver ' + link('/es/products/shaft-mounted-wire-wheels/', 'cardas con vástago') + '.'),
  '<h2>3. Alambre</h2>',
  P('Indica si lo quieres <strong>ondulado o trenzado</strong> (ver ' + link('/es/guias/carda-trenzada-o-ondulada/', 'la diferencia') + '), el material (acero al carbono, cobrizado) y, si lo tienes, el calibre. Como referencia, en nuestras cardas onduladas el alambre típico es de 0.3 mm y en la cónica trenzada de 0.5 mm.'),
  '<h2>4. Velocidad (RPM)</h2>',
  P('La RPM máxima de la carda debe ser igual o mayor que la de la máquina. Frank confirma la RPM de cada modelo antes del pedido.'),
  '<h2>Lista para mandar por WhatsApp</h2>',
  '<ul><li>Foto o modelo de referencia de la carda</li><li>Diámetro exterior</li><li>Rosca, orificio o vástago</li><li>Alambre: ondulado o trenzado, material</li><li>Cantidad por cada medida</li><li>Empaque: granel, blíster con tarjeta o caja a color, con o sin tu marca</li><li>País y ciudad de destino</li></ul>',
 ]),
'importar-cardas-de-china': dict(
 title='Cómo importar cardas desde China: muestras y envío',
 h1='Cómo importar cardas de alambre directo de fábrica en China',
 desc='Pasos para comprar cardas directo de fábrica en China: muestras, pedido de prueba, empaque con tu marca, términos EXW/FOB/CIF y DDP según el país de destino.',
 body=[
  P('Si tienes ferretería, distribuidora o tu propia marca de herramienta, comprar cardas directo de fábrica te da mejor margen y control del empaque. Así trabajamos en YEKAI, fábrica de cepillos de alambre en Yongkang, Zhejiang.'),
  '<h2>1. Define tu surtido</h2>',
  P('Empieza por las medidas que más vendes: por ejemplo copas de 3" y 4" para pulidora y cardas circulares para esmeril. Separa la cantidad por medida y por tipo de alambre. La ' + link('/es/guias/medidas-de-carda/', 'guía de medidas') + ' te dice qué datos mandar.'),
  '<h2>2. Pide muestras</h2>',
  P('Antes del pedido al mayoreo enviamos muestras para que revises alambre, montaje y acabado. Las muestras viajan por avión; el pedido grande, por barco.'),
  '<h2>3. Elige el empaque</h2>',
  P('Puedes pedir caja de cartón sencilla, blíster con tarjeta o caja a color, con tu marca. La placa de impresión cuesta 300 RMB por diseño; se bonifica en pedidos de al menos 5,000 piezas en total que combinan de 2 a 4 modelos en una misma plancha. Más detalles en ' + link('/es/#oem', 'empaque OEM') + ' y ' + link('/es/products/blister-card-brush-sets/', 'juegos en blíster') + '.'),
  '<h2>4. Pedido de prueba</h2>',
  P('Aceptamos pedidos pequeños de prueba con empaque estándar. En esos pedidos no aplica el precio de mayoreo y el flete por pieza sale más alto, pero te sirven para probar el producto con tus clientes.'),
  '<h2>5. Envío e impuestos</h2>',
  P('Cotizamos en <strong>EXW, FOB o CIF</strong>. Si no quieres encargarte de la importación, también podemos cotizar <strong>DDP</strong> (puerta a puerta, con impuestos incluidos), por ejemplo a México; se confirma según el país, el producto, el volumen y la ciudad de destino.'),
  '<h2>6. Pago, plazo y control de calidad</h2>',
  P('El pago habitual es <strong>30% de anticipo y el saldo antes del embarque</strong>. El plazo de producción de un pedido al mayoreo suele ser de unos 30 días y se confirma en cada pedido. Revisamos las cardas en un equipo de balanceo y muestreamos cada lote antes de despachar.'),
  '<h2>7. Qué mandar para cotizar</h2>',
  '<ul><li>Productos y fotos de referencia</li><li>Medidas y montaje de cada modelo</li><li>Cantidad por modelo</li><li>Tipo de empaque y si lleva tu marca</li><li>Ciudad de entrega y término (EXW, FOB, CIF o DDP)</li></ul>',
  P('Con eso Frank prepara la cotización de fábrica. Puedes ver primero ' + link('/es/about/', 'cómo es la fábrica') + ' y ' + link('/es/#documents', 'los documentos') + '.'),
 ]),
}

GUIDE_CONTENT.update(MORE_CONTENT)
GUIDE_CONTENT.update(CONTENT_ES2)
GUIDE_CONTENT.update(CONTENT_ES3)


def faq_html(slug, head='Preguntas frecuentes'):
    qa = FAQ.get(slug, [])
    if not qa: return ''
    return f'<h2>{head}</h2>' + ''.join(f'<h3>{esc(q)}</h3><p>{esc(a)}</p>' for q, a in qa)


def faq_ld(slug):
    qa = FAQ.get(slug, [])
    if not qa: return []
    return [{'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in qa]}]


def page_shell(template, *, title, desc, url, main, breadcrumb, wa_text, ld_extra, alts, switch):
    t = template
    t = re.sub(r'<title>.*?</title>', f'<title>{esc(title)} | YEKAI</title>', t, count=1, flags=re.S)
    t = set_meta(t, 'description', desc, 'name')
    t = set_meta(t, 'og:title', f'{title} | YEKAI', 'property')
    t = set_meta(t, 'og:description', desc, 'property')
    t = set_meta(t, 'og:url', url, 'property')
    t = re.sub(r'<link href="[^"]*" rel="canonical"/>', f'<link href="{url}" rel="canonical"/>', t, count=1)
    t = re.sub(r'<link href="[^"]*" hreflang="[^"]*" rel="alternate"/>\s*', '', t)
    t = t.replace(f'<link href="{url}" rel="canonical"/>', f'<link href="{url}" rel="canonical"/>' + ''.join(f'<link href="{u}" hreflang="{k}" rel="alternate"/>' for k, u in alts.items()), 1)
    t = re.sub(r'\s*<script type="application/ld\+json">.*?</script>', '', t, flags=re.S)
    crumbs = [{'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': u} for i, (n, u) in enumerate(breadcrumb)]
    ld = [{'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': crumbs}] + ld_extra
    t = t.replace('</head>', '<link href="/guides.css" rel="stylesheet"/>\n</head>', 1)
    t = t.replace('</head>', ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld) + '\n</head>', 1)
    # language switch / EN link in header -> no EN version
    t = re.sub(r'<a href="[^"]*">(EN|ES)</a></nav></header>', lambda m: f'<a href="{switch}">{m.group(1)}</a></nav></header>', t, count=1)
    t = re.sub(r'<main class="detail-main">.*?</main>', lambda m: f'<main class="detail-main">{main}</main>', t, count=1, flags=re.S)
    t = re.sub(r'(<a class="btn wa-primary" href=")[^"]*(" id="sticky-quote")', lambda m: m.group(1) + WA + wa_text + m.group(2), t, count=1)
    return t


def nav_crumb(items):
    parts = [f'<a href="{u.replace(BASE, "")}">{esc(n)}</a>' for n, u in items[:-1]]
    parts.append(f'<span aria-current="page">{esc(items[-1][0])}</span>')
    return '<nav aria-label="Breadcrumb" class="breadcrumb">' + ' / '.join(parts) + '</nav>'


UNPAIR = {v: k for k, v in PAIR.items()}
LANGS = {
 'es': dict(prefix='es/', gdir='es/guias', template='es/steel-wire-wheel-brush/index.html', home='Inicio', idx='Guías de compra',
            eyebrow='GUÍA DE COMPRA · YEKAI', others='Otras guías', cta='Cotizar con Frank por WhatsApp ↗', inlang='es',
            wa='Hola%20Frank%2C%20vi%20la%20gu%C3%ADa%20de%20cardas%20y%20quisiera%20cotizar', faq='Preguntas frecuentes',
            idx_eyebrow='PARA FERRETERÍAS Y DISTRIBUIDORES', idx_h1='Guías para comprar cardas de alambre',
            idx_lead='Cómo elegir la carda para cada trabajo, qué medidas mandar, cómo pedir empaque con tu marca y cómo importar directo de fábrica.',
            idx_title='Guías para comprar cardas de alambre al mayoreo',
            idx_desc='Guías en español: qué carda usar para soldadura, óxido y pintura, cepillos para desbrozadora, nylon abrasivo, medidas, empaque con tu marca e importación.',
            home_h2='Guías para comprar cardas', all='Ver todas las guías →', read='Leer guía →', all_n='Ver las {n} guías →',
            home_lead='Respuestas cortas a lo que más preguntan ferreterías y distribuidores antes de pedir.', label='Guías de compra'),
 'en': dict(prefix='', gdir='guides', template='steel-wire-wheel-brush/index.html', home='Home', idx='Buyer guides',
            eyebrow='BUYER GUIDE · YEKAI', others='More guides', cta='Ask Frank for a quote on WhatsApp ↗', inlang='en',
            wa='Hello%20Frank%2C%20I%20read%20your%20wire%20brush%20guide%20and%20would%20like%20a%20quote', faq='Frequently asked questions',
            idx_eyebrow='FOR HARDWARE DISTRIBUTORS AND IMPORTERS', idx_h1='Wire brush buyer guides',
            idx_lead='How to choose the right wire brush for each job, which sizes to send, how to order private label packaging and how to import direct from the factory.',
            idx_title='Wire Brush Buyer Guides for Wholesale Orders',
            idx_desc='Guides for wire brush buyers: weld cleaning, rust and paint removal, weed brushes, abrasive nylon, sizes and threads, private label and importing.',
            home_h2='Wire brush buyer guides', all='See all guides →', read='Read guide →', all_n='See all {n} guides →',
            home_lead='Short answers to what importers and hardware distributors ask most before ordering.', label='Buyer guides'),
}


FEATURED = {
    'es': ['carda-trenzada-o-ondulada', 'medidas-de-carda', 'carda-copa-para-pulidora',
           'carda-para-esmeril-de-banco', 'cepillo-para-desbrozadora', 'importar-cardas-de-china'],
    'en': ['knotted-vs-crimped-wire-brush', 'wire-brush-sizes-and-threads', 'wire-cup-brush-for-angle-grinder',
           'wire-wheel-for-bench-grinder', 'wire-weed-brush-for-brush-cutter', 'import-wire-brushes-from-china'],
}


def guide_set(lang):
    return (GUIDES, GUIDE_CONTENT) if lang == 'es' else (GUIDES_EN, CONTENT_EN)


def guide_alts(lang, slug=None):
    """hreflang: cada guía tiene su par en el otro idioma"""
    if slug is None:
        en, es = f'{BASE}/guides/', f'{BASE}/es/guias/'
    else:
        if lang == 'en' and slug not in UNPAIR:  # guía sólo en inglés (p. ej. India)
            u = f'{BASE}/guides/{slug}/'
            return {'en': u, 'x-default': u}
        en_slug = slug if lang == 'en' else PAIR[slug]
        es_slug = slug if lang == 'es' else UNPAIR[slug]
        en, es = f'{BASE}/guides/{en_slug}/', f'{BASE}/es/guias/{es_slug}/'
    return {'en': en, 'es': es, 'x-default': en}


def build_guides(lang='es'):
    L = LANGS[lang]; guides, content = guide_set(lang)
    template = (ROOT / L['template']).read_text()
    template = re.sub(r'<!-- seo-mx guides:start -->.*?<!-- seo-mx guides:end -->', '', template, flags=re.S)
    cats = re.search(r'<nav[^>]*class="category-navigation"[^>]*>.*?</nav>', template, re.S).group(0)
    out = []
    gurl = f'{BASE}/{L["gdir"]}/'; gpath = f'/{L["gdir"]}/'
    home = (L['home'], f'{BASE}/{L["prefix"]}'); idx = (L['idx'], gurl)
    wa = L['wa']
    for slug, g in content.items():
        url = f'{gurl}{slug}/'
        crumbs = [home, idx, (g['h1'], url)]
        alts = guide_alts(lang, slug)
        others = ''.join(f'<li><a href="{gpath}{s}/">{esc(t)}</a></li>' for s, t in guides if s != slug)
        main = (cats + nav_crumb(crumbs)
                + f'<article class="yekai-buyer-guide guide-article"><span class="eyebrow">{L["eyebrow"]}</span><h1>{esc(g["h1"])}</h1>'
                + ''.join(g['body']) + faq_html(slug, L['faq'])
                + f'<h2>{L["others"]}</h2><ul>{others}</ul></article>'
                + f'<a class="btn wa-primary" href="{WA}{wa}" rel="noopener noreferrer" target="_blank">{L["cta"]}</a>')
        art = {'@context': 'https://schema.org', '@type': 'Article', 'headline': g['h1'], 'description': g['desc'],
               'inLanguage': L['inlang'], 'datePublished': TODAY, 'dateModified': TODAY, 'mainEntityOfPage': url,
               'image': f'{BASE}/images/yekai-factory.webp',
               'author': {'@type': 'Organization', 'name': 'YEKAI Abrasives', 'url': f'{BASE}/'},
               'publisher': {'@id': f'{BASE}/#organization'}}
        other = alts.get('es' if lang == 'en' else 'en', f'{BASE}/es/guias/').replace(BASE, '')
        page = page_shell(template, title=g['title'], desc=g['desc'], url=url, main=main, breadcrumb=crumbs, wa_text=wa,
                          ld_extra=[art] + faq_ld(slug), alts=alts, switch=other)
        f = ROOT / L['gdir'] / slug / 'index.html'; f.parent.mkdir(parents=True, exist_ok=True); f.write_text(page); out.append(f)
    cards = ''.join(f'<a class="range-card" href="{gpath}{s}/"><strong>{esc(content[s]["h1"])}</strong><span>{esc(content[s]["desc"])}</span></a>' for s, _ in guides)
    main = (cats + nav_crumb([home, idx]) + f'<span class="eyebrow">{L["idx_eyebrow"]}</span><h1>{L["idx_h1"]}</h1>'
            + f'<p class="lead">{L["idx_lead"]}</p><div class="range-grid">{cards}</div>')
    alts = guide_alts(lang)
    page = page_shell(template, title=L['idx_title'], desc=L['idx_desc'], url=gurl, main=main, breadcrumb=[home, idx], wa_text=wa,
                      ld_extra=[], alts=alts, switch=alts['es' if lang == 'en' else 'en'].replace(BASE, ''))
    f = ROOT / L['gdir'] / 'index.html'; f.write_text(page); out.append(f)
    return out


# ---------------------------------------------------------------- 3. enlaces internos
def add_block(text, marker, block, anchor, before=True):
    text = re.sub(rf'<!-- {marker}:start -->.*?<!-- {marker}:end -->', '', text, flags=re.S)
    wrapped = f'<!-- {marker}:start -->{block}<!-- {marker}:end -->'
    i = text.find(anchor)
    if i < 0: return text
    return text[:i] + wrapped + text[i:] if before else text[:i + len(anchor)] + wrapped + text[i + len(anchor):]

# guías más relevantes para cada producto (enlace contextual)
REL = {
 'stringer-knotted-wheels': ['carda-para-soldadura', 'carda-trenzada-o-ondulada', 'medidas-de-carda'],
 'red-knotted-wire-cup-brush': ['carda-para-soldadura', 'carda-para-quitar-oxido-y-pintura', 'medidas-de-carda'],
 'banded-twisted-cup-brushes': ['carda-para-soldadura', 'carda-trenzada-o-ondulada', 'medidas-de-carda'],
 'twisted-wire-wheels': ['carda-para-soldadura', 'carda-trenzada-o-ondulada', 'medidas-de-carda'],
 'crimped-wire-cup-brushes': ['carda-para-quitar-oxido-y-pintura', 'carda-trenzada-o-ondulada', 'medidas-de-carda'],
 'wide-crimped-wire-wheels': ['carda-para-quitar-oxido-y-pintura', 'carda-trenzada-o-ondulada', 'medidas-de-carda'],
 'crimped-wire-brush-wheels': ['carda-para-quitar-oxido-y-pintura', 'carda-trenzada-o-ondulada', 'medidas-de-carda'],
 'copper-coated-wire-wheels': ['carda-para-quitar-oxido-y-pintura', 'medidas-de-carda', 'cardas-con-tu-marca'],
 'shaft-mounted-wire-wheels': ['carda-para-quitar-oxido-y-pintura', 'carda-para-soldadura', 'medidas-de-carda'],
 'plastic-handle-hand-brushes': ['carda-para-quitar-oxido-y-pintura', 'cardas-con-tu-marca', 'importar-cardas-de-china'],
 'blister-card-brush-sets': ['cardas-con-tu-marca', 'importar-cardas-de-china', 'medidas-de-carda'],
 'abrasive-filament-brushes': ['cepillo-de-nylon-abrasivo', 'carda-para-quitar-oxido-y-pintura', 'cardas-con-tu-marca'],
 'abrasive-flap-discs': ['carda-para-quitar-oxido-y-pintura', 'cardas-con-tu-marca', 'importar-cardas-de-china'],
 '3-and-6-bundle-wire-trimmer-heads': ['cepillo-para-desbrozadora', 'cardas-con-tu-marca', 'importar-cardas-de-china'],
 'twisted-wire-grass-trimmer-heads': ['cepillo-para-desbrozadora', 'cardas-con-tu-marca', 'importar-cardas-de-china'],
 'nylon-grass-trimmer-brushes': ['cepillo-para-desbrozadora', 'cardas-con-tu-marca', 'importar-cardas-de-china'],
}


REL_FIRST = {
 'red-knotted-wire-cup-brush': 'carda-copa-para-pulidora', 'crimped-wire-cup-brushes': 'carda-copa-para-pulidora',
 'banded-twisted-cup-brushes': 'carda-copa-para-pulidora', 'wide-crimped-wire-wheels': 'carda-para-esmeril-de-banco',
 'crimped-wire-brush-wheels': 'carda-para-esmeril-de-banco', 'copper-coated-wire-wheels': 'carda-para-acero-inoxidable-y-aluminio',
 'shaft-mounted-wire-wheels': 'carda-para-taladro', 'abrasive-filament-brushes': 'cepillo-para-madera',
 'abrasive-flap-discs': 'carda-o-disco-flap', 'blister-card-brush-sets': 'surtido-de-cardas-para-ferreteria',
 'plastic-handle-hand-brushes': 'surtido-de-cardas-para-ferreteria', 'stringer-knotted-wheels': 'carda-para-esmeril-de-banco',
 'twisted-wire-wheels': 'seguridad-y-rpm-de-cardas',
}
for _k, _v in REL_FIRST.items():
    REL[_k] = ([_v] + [x for x in REL.get(_k, []) if x != _v])[:3]


def related_guides(product_slug, lang='es'):
    guides, _ = guide_set(lang); L = LANGS[lang]
    titles = dict(guides)
    slugs = REL.get(product_slug) or [s for s, _ in GUIDES[:3]]
    if lang == 'en': slugs = [PAIR[x] for x in slugs]
    return ' · '.join(f'<a href="/{L["gdir"]}/{x}/">{html.escape(titles[x])}</a>' for x in slugs)


def internal_links():
    changed = []
    # About desde los inicios
    for f, href, en, es, label in [(ROOT / 'index.html', '/about/', 'See the factory', 'Conoce la fábrica', 'See the factory'),
                                   (ROOT / 'es/index.html', '/es/about/', 'See the factory', 'Conoce la fábrica', 'Conoce la fábrica')]:
        t = f.read_text(); o = t
        anchor = re.search(r'<a class="underlink"[^>]*href="/(?:es/)?#contact">.*?</a>', t[t.find('id="about"'):], re.S)
        if anchor:
            block = f' <a class="underlink" data-en="{esc(en)} &lt;span&gt;→&lt;/span&gt;" data-es="{esc(es)} &lt;span&gt;→&lt;/span&gt;" href="{href}">{label} <span>→</span></a>'
            t = add_block(t, 'seo-mx about', block, anchor.group(0), before=False)
        if t != o: f.write_text(t); changed.append(f)
    for lang, L in LANGS.items():
        guides, content = guide_set(lang); gpath = f'/{L["gdir"]}/'
        # 2026-11-18: en el inicio sólo 6 guías destacadas en tarjetas; el resto en la página de guías
        feat = FEATURED[lang]; assert all(x in content for x in feat), feat
        lis = ''.join(f'<li><a class="guide-card" href="{gpath}{s}/"><strong>{esc(content[s]["h1"])}</strong>'
                      f'<span>{esc(content[s]["desc"])}</span><em>{L["read"]}</em></a></li>' for s in feat)
        # sección de guías en el inicio (antes de #contact)
        f = ROOT / L['prefix'] / 'index.html'; t = f.read_text(); o = t
        block = (f'<section class="section yekai-buyer-guide" id="{"guias" if lang == "es" else "guides"}"><h2>{L["home_h2"]}</h2>'
                 f'<p class="guide-cards-lead">{L["home_lead"]}</p><ul class="guide-cards">{lis}</ul>'
                 f'<p class="guide-cards-all"><a class="btn" href="{gpath}">{L["all_n"].format(n=len(guides))}</a></p></section>')
        m = re.search(r'<section[^>]*id="contact"', t)
        if m: t = add_block(t, 'seo-mx guides', block, m.group(0))
        t = add_block(t, 'seo-mx css', '<link href="/guides.css" rel="stylesheet"/>', '</head>')
        if t != o: f.write_text(t); changed.append(f)
        # páginas de detalle: categoría, productos y pie
        for f in sorted(ROOT.rglob('index.html')):
            rel = f.relative_to(ROOT).as_posix()
            if rel.startswith('reports/') or rel.startswith(('es/guias/', 'guides/')): continue
            if rel.startswith('es/') != (lang == 'es'): continue
            t = f.read_text(); o = t
            if 'content="noindex"' in t: continue
            if '<footer class="detail-footer">' in t:
                t = add_block(t, 'seo-mx footer', f' · <a href="{gpath}">{L["label"]}</a>', '</footer>')
            if '<section id="buyer-links">' in t:
                i = t.find('<section id="buyer-links">'); j = t.find('</section>', i)
                seg = t[i:j]
                seg = re.sub(r'<!-- seo-mx product guides:start -->.*?<!-- seo-mx product guides:end -->', '', seg, flags=re.S)
                seg += f'<!-- seo-mx product guides:start --><p>{L["label"]}: {related_guides(f.parent.name, lang)}</p><!-- seo-mx product guides:end -->'
                t = t[:i] + seg + t[j:]
            elif 'class="yekai-buyer-guide"' in t or f.parent.name == 'steel-wire-wheel-brush':
                blk = f'<section class="yekai-buyer-guide"><h2>{L["label"]}</h2><ul>{lis}</ul></section>'
                t = add_block(t, 'seo-mx guides', blk, '</main>')
                t = add_block(t, 'seo-mx css', '<link href="/guides.css" rel="stylesheet"/>', '</head>')
            if t != o: f.write_text(t); changed.append(f)
    return changed


# ---------------------------------------------------------------- 4. sitemap
def sitemap(changed):
    old = {}
    sm = ROOT / 'sitemap.xml'
    ns = 'http://www.sitemaps.org/schemas/sitemap/0.9'
    if sm.exists():
        for n in ET.parse(sm).getroot().findall('{%s}url' % ns):
            old[n.findtext('{%s}loc' % ns)] = n.findtext('{%s}lastmod' % ns)
    changed_urls = set()
    for f in changed:
        rel = f.relative_to(ROOT).as_posix().removesuffix('index.html')
        changed_urls.add(f'{BASE}/{rel}')
    urls = []
    for f in sorted(ROOT.rglob('index.html')):
        t = f.read_text()
        if re.search(r'<meta content="[^"]*noindex', t): continue
        m = re.search(r'<link href="([^"]+)" rel="canonical"/>', t)
        if m: urls.append(m.group(1))
    ET.register_namespace('', ns)
    root = ET.Element('{%s}urlset' % ns)
    for u in urls:
        n = ET.SubElement(root, '{%s}url' % ns)
        ET.SubElement(n, '{%s}loc' % ns).text = u
        ET.SubElement(n, '{%s}lastmod' % ns).text = TODAY if (u in changed_urls or u not in old) else (old.get(u) or TODAY)
    ET.indent(root)
    ET.ElementTree(root).write(sm, encoding='utf-8', xml_declaration=True)
    return urls


# ---------------------------------------------------------------- 5. textos neutrales (no sólo México)
NEUTRAL = [
 ('Para ferreterías, distribuidores e importadores en México: ', 'Para ferreterías, distribuidores e importadores: '),
 ('For hardware distributors, importers and industrial buyers supplying Mexico: ', 'For hardware distributors, importers and industrial buyers: '),
 ('para surtir tu negocio en México', 'para surtir tu negocio'),
 ('Envío a México (DDP disponible bajo cotización)', 'Exportación a todo el mundo · DDP a México bajo cotización'),
 ('para mi negocio en México.', 'para mi negocio.'),
 ('para%20mi%20negocio%20en%20M%C3%A9xico.', 'para%20mi%20negocio.'),
 # 2026-11-16: Frank confirmó que 3/6 haces de orificio chico es para batería y de orificio grande para gasolina
 ('The factory describes this range for handheld cordless trimmers. Confirm the particular machine and connection; do not assume universal fit or compatibility with petrol-powered equipment.',
  'Two bore sizes: 5.5 mm for battery (cordless) trimmers and 25.4 mm for petrol brush cutters. Send the machine model and bore size to confirm the fit; there is no universal fit.'),
 ('La fábrica describe esta gama para desbrozadoras inalámbricas de mano. Confirma máquina y conexión; no se presupone ajuste universal ni compatibilidad con equipos a gasolina.',
  'Hay dos orificios: 5.5 mm para desbrozadoras de batería (inalámbricas) y 25.4 mm para desbrozadoras a gasolina. Envía el modelo de la máquina y la medida del orificio para confirmar el montaje; no hay ajuste universal.'),
]


def neutral_copy():
    changed = []
    files = list(ROOT.rglob('index.html')) + [ROOT / 'product-specs.json', ROOT / 'scripts/seo-copy.json', ROOT / 'scripts/build-products.py', ROOT / 'scripts/refine_site_20261113.py']
    for f in files:
        if not f.exists(): continue
        t = f.read_text(); o = t
        for a, b in NEUTRAL: t = t.replace(a, b)
        if t != o:
            f.write_text(t)
            if f.name == 'index.html': changed.append(f)
    return changed


# ---------------------------------------------------------------- 6. "También se busca como" (sinónimos regionales)
AKA = {
 'red-knotted-wire-cup-brush': ('carda copa trenzada, cepillo de copa trenzado, grata copa trenzada, carda copa para pulidora o amoladora',
                                'knot wire cup brush, twist knot cup brush, wire cup brush for angle grinder'),
 'crimped-wire-cup-brushes': ('carda copa ondulada, cepillo de copa de alambre, grata copa, carda copa para pulidora o amoladora',
                              'crimped cup brush, wire cup brush for angle grinder, crimped wire cup wheel'),
 'banded-twisted-cup-brushes': ('carda copa trenzada con aro, carda copa con anillo, grata copa con anillo, cepillo copa trenzado reforzado',
                                'banded knot cup brush, twist knot cup brush with ring, wire cup brush for angle grinder'),
 'twisted-wire-wheels': ('carda cónica, cepillo cónico trenzado, grata cónica, carda biselada para pulidora',
                         'bevel wire brush, knotted bevel brush, twist knot bevel wheel'),
 'wide-crimped-wire-wheels': ('carda para esmeril, carda circular para esmeril de banco, grata circular, rueda de alambre, cepillo circular de alambre',
                              'bench grinder wire wheel, crimped wire wheel brush, wide face wire wheel'),
 'crimped-wire-brush-wheels': ('carda circular ondulada, carda para esmeril, grata circular, rueda de alambre ondulado',
                               'crimped wire wheel, bench grinder wire wheel, circular wire brush'),
 'copper-coated-wire-wheels': ('carda circular de alambre cobrizado, cepillo circular cobrizado, grata de alambre cobrizado',
                               'copper coated wire wheel, brass-color wire wheel brush'),
 'stringer-knotted-wheels': ('carda para soldadura, carda trenzada angosta, grata para cordón de soldadura, cepillo para limpiar soldadura',
                             'stringer bead wire wheel, weld cleaning wire wheel, narrow knot wheel'),
 'shaft-mounted-wire-wheels': ('carda con vástago, carda para taladro, cepillo de alambre para taladro, grata con espiga, carda de punta',
                               'shank mounted wire brush, wire brush for drill, end brush, mounted wire wheel'),
 'plastic-handle-hand-brushes': ('cepillo de alambre de mano, cepillo de alambre con mango, cepillo de acero manual',
                                 'hand wire brush, scratch brush, wire brush with plastic handle'),
 'blister-card-brush-sets': ('juego de cardas, kit de cepillos de alambre, cardas en blíster para ferretería',
                             'wire brush set, blister pack wire brushes, retail wire brush kit'),
 'abrasive-filament-brushes': ('cepillo de nylon abrasivo, carda de nylon, cepillo de filamento abrasivo, cepillo de nylon con carburo de silicio',
                               'abrasive nylon brush, nylon abrasive wheel, silicon carbide filament brush'),
 'abrasive-flap-discs': ('disco flap, disco laminado, disco de láminas, disco traslapado para pulidora o amoladora',
                         'flap disc, flap wheel for angle grinder, abrasive flap disc'),
 '3-and-6-bundle-wire-trimmer-heads': ('cepillo de alambre para desbrozadora, disco de alambre para desmalezadora o guadaña, cabezal de acero para desbrozadora',
                                       'wire trimmer head, brush cutter wire wheel, weed brush for trimmer'),
 'twisted-wire-grass-trimmer-heads': ('cepillo trenzado para desbrozadora, disco de alambre para desmalezadora o guadaña, cepillo quitamaleza',
                                      'twisted wire trimmer head, brush cutter weed brush, knot wire weed wheel'),
 'nylon-grass-trimmer-brushes': ('cepillo de nylon para desbrozadora, cepillo para desmalezadora o guadaña, cepillo quitamaleza de nylon',
                                 'nylon trimmer brush, brush cutter nylon weed brush'),
}


def also_known():
    changed = []
    for slug, (es, en) in AKA.items():
        for lang, base, lab, txt in (('es', ROOT / 'es', 'También se busca como', es), ('en', ROOT, 'Also known as', en)):
            f = base / 'products' / slug / 'index.html'
            t = f.read_text(); o = t
            m = re.search(r'<h1>[^<]*</h1>(<p>.*?</p>)', t, re.S)
            if not m: continue
            t = add_block(t, 'seo-mx aka', f'<p class="also-known"><strong>{lab}:</strong> {esc(txt)}.</p>', m.group(1), before=False)
            t = add_block(t, 'seo-mx css', '<link href="/guides.css" rel="stylesheet"/>', '</head>')
            if t != o: f.write_text(t); changed.append(f)
    return changed


# ---------------------------------------------------------------- 7. nombres de producto ES = H1 (tarjetas del inicio, enlaces, datos)
RENAME_ES = {
 'Cepillos de filamento abrasivo': 'Cepillos de nylon abrasivo (filamento)',
 'Discos de alambre trenzado': 'Carda cónica de alambre trenzado',
 'Discos de alambre cobrizado': 'Carda circular de alambre cobrizado',
 'Copas trenzadas con aro': 'Carda copa trenzada con aro',
 'Copas de alambre ondulado': 'Carda copa de alambre ondulado',
 'Cepillo de copa de alambre trenzado': 'Carda copa de alambre trenzado',
 'Discos de alambre con vástago': 'Cardas con vástago para taladro',
 'Cepillos manuales con mango plástico': 'Cepillos de alambre con mango de plástico',
 'Discos ondulados anchos': 'Carda circular ancha de alambre ondulado',
 'Discos de trenzado estrecho': 'Carda trenzada angosta para soldadura',
 'Discos de láminas abrasivas': 'Discos laminados flap abrasivos',
 'Cepillos circulares de alambre ondulado': 'Carda circular de alambre ondulado',
 'Juegos de cepillos en blíster': 'Juegos de cardas y cepillos en blíster',
 'Discos y copas de alambre': 'Cardas y copas de alambre',
}


def rename_products(table=None):
    from urllib.parse import quote
    changed = []
    pairs = sorted((RENAME_ES if table is None else table).items(), key=lambda kv: -len(kv[0]))
    files = list(ROOT.rglob('index.html')) + [ROOT / n for n in ('products.json', 'product-map.json', 'product-specs.json')]
    for f in files:
        if not f.exists() or 'reports' in f.parts: continue
        t = f.read_text(); o = t
        for a, b in pairs:
            t = t.replace(a, b).replace(esc(a), esc(b)).replace(quote(a, safe=''), quote(b, safe=''))
        if t != o:
            f.write_text(t)
            if f.name == 'index.html': changed.append(f)
    return changed


# ---------------------------------------------------------------- 8. "qué es / dónde comprar" en páginas de desbrozadora
# Search Console mostró búsquedas tipo "... qué es y dónde comprar" llegando a estas páginas.
G_TRIM = '/es/guias/cepillo-para-desbrozadora/'
PRODUCT_FAQ = {
 'twisted-wire-grass-trimmer-heads': {
  'es': [('¿Qué es un cabezal de alambre trenzado para desbrozadora?',
          'Es un cepillo de acero que se monta en la desbrozadora (desmalezadora o guadaña) en lugar del hilo o la cuchilla. Sirve para quitar maleza y musgo de juntas de adoquín, banquetas y pisos de concreto, sin herbicida. Los haces de alambre trenzado aguantan más que el hilo de nylon en superficies duras.'),
         ('¿Dónde comprar cabezales de alambre para desbrozadora al mayoreo?',
          'Directo de fábrica con YEKAI, en Yongkang, China. Cotizamos en EXW, FOB o CIF a cualquier país; para México también hay DDP (puerta a puerta con impuestos) bajo cotización. Envía por WhatsApp el modelo de tu máquina, el diámetro y la cantidad.')],
  'en': [('What is a twisted wire trimmer head?',
          'It is a steel wire brush that mounts on a brush cutter or grass trimmer in place of the line or blade. It removes weeds and moss from paving joints, kerbs and concrete floors without herbicide. Twisted wire knots last longer than nylon line on hard surfaces.'),
         ('Where can I buy wire trimmer heads wholesale?',
          'Direct from the YEKAI factory in Yongkang, China. We quote EXW, FOB or CIF to any country; DDP to Mexico is available on request. Send your machine model, diameter and quantity on WhatsApp.')]},
 '3-and-6-bundle-wire-trimmer-heads': {
  'es': [('¿Qué es un cabezal de alambre de 3 o 6 haces?',
          'Es un cabezal para desbrozadora con 3 o 6 haces de alambre de acero. Se usa para quitar maleza de juntas, orillas y pisos duros. El de orificio de 5.5 mm es para máquinas de batería y el de 25.4 mm para máquinas a gasolina.'),
         ('¿Dónde comprar cabezales de 3 y 6 haces al mayoreo?',
          'Directo de fábrica con YEKAI, en Yongkang, China. Cotizamos en EXW, FOB o CIF a cualquier país; para México también hay DDP bajo cotización. Envía por WhatsApp el modelo de tu máquina, la medida del orificio y la cantidad.')],
  'en': [('What is a 3 or 6 bundle wire trimmer head?',
          'It is a trimmer head with 3 or 6 steel wire bundles for clearing weeds from joints, edges and hard floors. The 5.5 mm bore fits battery trimmers and the 25.4 mm bore fits petrol brush cutters.'),
         ('Where can I buy 3 and 6 bundle trimmer heads wholesale?',
          'Direct from the YEKAI factory in Yongkang, China. We quote EXW, FOB or CIF to any country; DDP to Mexico is available on request. Send your machine model, bore size and quantity on WhatsApp.')]},
 'nylon-grass-trimmer-brushes': {
  'es': [('¿Qué es un cepillo de nylon para desbrozadora?',
          'Es un cepillo circular de filamento de nylon que se monta en la desbrozadora para quitar maleza y musgo. Se elige en lugar del alambre de acero cuando la superficie no debe rayarse.'),
         ('¿Dónde comprar cepillos de nylon para desbrozadora al mayoreo?',
          'Directo de fábrica con YEKAI, en Yongkang, China. Cotizamos en EXW, FOB o CIF a cualquier país; para México también hay DDP bajo cotización. Envía por WhatsApp el modelo de tu máquina, el diámetro y la cantidad.')],
  'en': [('What is a nylon trimmer brush?',
          'It is a circular nylon filament brush that mounts on a brush cutter to remove weeds and moss. It is chosen instead of steel wire when the surface must not be scratched.'),
         ('Where can I buy nylon trimmer brushes wholesale?',
          'Direct from the YEKAI factory in Yongkang, China. We quote EXW, FOB or CIF to any country; DDP to Mexico is available on request. Send your machine model, diameter and quantity on WhatsApp.')]},
}

from product_faq_20261117 import MORE_PRODUCT_FAQ, ABOUT, ABOUT_META
PRODUCT_FAQ.update(MORE_PRODUCT_FAQ)


def product_faq():
    changed = []
    for slug, langs in PRODUCT_FAQ.items():
        for lang, qa in langs.items():
            f = (ROOT / 'es' if lang == 'es' else ROOT) / 'products' / slug / 'index.html'
            t = f.read_text(); o = t
            head = 'Preguntas frecuentes' if lang == 'es' else 'Frequently asked questions'
            more = f'<p>{LANGS[lang]["label"]}: {related_guides(slug, lang)}</p>'
            sec = (f'<section class="yekai-buyer-guide" id="product-faq"><h2>{head}</h2>'
                   + ''.join(f'<h3>{esc(q)}</h3><p>{esc(a)}</p>' for q, a in qa) + more + '</section>')
            t = add_block(t, 'seo-mx product faq', sec, '<section id="buyer-links">')
            ld = {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
                {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in qa]}
            t = add_block(t, 'seo-mx product faq ld', f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>', '</head>')
            t = add_block(t, 'seo-mx css', '<link href="/guides.css" rel="stylesheet"/>', '</head>')
            if t != o: f.write_text(t); changed.append(f)
    return changed


# ---------------------------------------------------------------- 9. página About ampliada
def about_page():
    changed = []
    for lang, prefix in (('en', ''), ('es', 'es/')):
        f = ROOT / prefix / 'about/index.html'; t = f.read_text(); o = t
        t = add_block(t, 'seo-mx about body', ABOUT[lang], '<section class="order-terms">')
        t = add_block(t, 'seo-mx css', '<link href="/guides.css" rel="stylesheet"/>', '</head>')
        title, desc = ABOUT_META[lang]; full = f'{title} | YEKAI'
        t = re.sub(r'<title>.*?</title>', lambda m: f'<title>{esc(full)}</title>', t, count=1, flags=re.S)
        t = set_meta(t, 'og:title', full, 'property'); t = set_meta(t, 'description', desc, 'name'); t = set_meta(t, 'og:description', desc, 'property')

        def fix(data):
            for n in (data.get('@graph', [data]) if isinstance(data, dict) else []):
                if n.get('@type') == 'WebPage': n['name'] = full; n['description'] = desc
        t = edit_jsonld(t, fix)
        if t != o: f.write_text(t); changed.append(f)
    return changed


# ---------------------------------------------------------------- 10. carda de banco con bujes: fotos reales (2026-11-17)
BENCH = {
 'en': ('<section class="yekai-buyer-guide" id="bench-version"><h2>Bench grinder version with reducing bushings</h2>'
        '<p>This is the thicker bench wheel: a wider face with more wire than an arbor-hole wheel, and stepped bushings in the hub so one wheel fits several shaft sizes. It is used mostly on bench grinders and costs more than the arbor-hole type. Shown here in copper-coated crimped wire.</p><p><strong>Sizes:</strong> the same diameters as the arbor-hole wheel: 4, 5, 6, 7, 8, 10 and 12 in (100 to 300 mm). Send the shaft diameter of your grinder and Frank confirms the bushing set.</p>'
        '<div class="about-photos three"><img alt="Bench grinder crimped wire wheel with orange hub and reducing bushings" height="1254" loading="lazy" src="/images/bench-wheel-orange-top.webp" width="1254"/>'
        '<img alt="Side view of the wide-face bench wire wheel" height="1254" loading="lazy" src="/images/bench-wheel-orange-side.webp" width="1254"/>'
        '<img alt="Bench wire wheels in several diameters on a display wall" height="1180" loading="lazy" src="/images/bench-wheel-range.webp" width="1200"/></div>'
        '<p><a href="/guides/wire-wheel-for-bench-grinder/">How to choose a wire wheel for a bench grinder</a></p></section>'),
 'es': ('<section class="yekai-buyer-guide" id="bench-version"><h2>Versión para esmeril de banco con bujes reductores</h2>'
        '<p>Es la carda de banco gruesa: cara más ancha y más alambre que la carda con orificio, con bujes escalonados en el centro para que una misma pieza sirva en varias medidas de flecha. Se usa sobre todo en esmeril de banco y cuesta más que la de orificio. En la foto, en alambre ondulado cobrizado.</p><p><strong>Medidas:</strong> los mismos diámetros que la carda con orificio: 4, 5, 6, 7, 8, 10 y 12 pulgadas (100 a 300 mm). Envía el diámetro de la flecha de tu esmeril y Frank confirma el juego de bujes.</p>'
        '<div class="about-photos three"><img alt="Carda para esmeril de banco con centro naranja y bujes reductores" height="1254" loading="lazy" src="/images/bench-wheel-orange-top.webp" width="1254"/>'
        '<img alt="Vista lateral de la carda ancha para esmeril de banco" height="1254" loading="lazy" src="/images/bench-wheel-orange-side.webp" width="1254"/>'
        '<img alt="Cardas de banco en varios diámetros en un exhibidor" height="1180" loading="lazy" src="/images/bench-wheel-range.webp" width="1200"/></div>'
        '<p><a href="/es/guias/carda-para-esmeril-de-banco/">Cómo elegir una carda para esmeril de banco</a></p></section>'),
}


def bench_photos():
    changed = []
    for lang, prefix in (('en', ''), ('es', 'es/')):
        f = ROOT / prefix / 'products/wide-crimped-wire-wheels/index.html'; t = f.read_text(); o = t
        anchor = '<!-- seo-mx product faq:start -->' if '<!-- seo-mx product faq:start -->' in t else '<section id="buyer-links">'
        t = add_block(t, 'seo-mx bench', BENCH[lang], anchor)
        if t != o: f.write_text(t); changed.append(f)
    return changed


# ---------------------------------------------------------------- 11. botón del catálogo PDF (2026-11-18)
def catalog_pdf():
    changed = []
    for lang, prefix in (('en', ''), ('es', 'es/')):
        f = ROOT / prefix / 'index.html'; t = f.read_text(); o = t
        label = 'Download full catalog (PDF) ↓' if lang == 'en' else 'Descargar catálogo completo (PDF) ↓'
        note = 'PDF, 14 pages. Model numbers, sizes and maximum RPM.' if lang == 'en' else 'PDF de 14 páginas: modelos, medidas y RPM máximas.'
        new = (f'<div class="catalog-pdf-pending"><a class="btn secondary" data-en="Download full catalog (PDF) ↓" data-es="Descargar catálogo completo (PDF) ↓" '
               f'download="" href="/downloads/yekai-wire-brush-catalog.pdf">{label}</a><p>{note}</p></div>')
        t = re.sub(r'<div class="catalog-pdf-pending">.*?</div>', lambda m: new, t, count=1, flags=re.S)
        if t != o: f.write_text(t); changed.append(f)
    return changed


if __name__ == '__main__':
    c1 = apply_meta() + apply_meta(EN, '')
    c3 = internal_links() + neutral_copy() + also_known() + rename_products() + rename_products(RENAME_EN) + product_faq() + about_page() + bench_photos()  # catalog_pdf() desactivado 2026-11-18: el catálogo impreso está desactualizado
    c2 = build_guides('es') + build_guides('en')
    urls = sitemap(c1 + c2 + c3)
    print(f'metadatos: {len(c1)} páginas · guías: {len(c2)} páginas · enlaces: {len(c3)} páginas · sitemap: {len(urls)} URLs')

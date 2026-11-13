import html
import json
import re
from maintain_seo import set_meta


def build(root):
    copy = json.loads((root / 'scripts/seo-copy.json').read_text())
    mapping = json.loads((root / 'product-map.json').read_text())
    catalog = json.loads((root / 'products.json').read_text())
    names = {str(p['id']): p for p in catalog}
    escape = html.escape
    oem = [
        'Choose blister cards, color boxes or plain outer cartons. We waive the RMB 300 printing plate fee when an order of at least 5,000 pieces combines two to four models on one print layout. Otherwise the plate fee for custom printing is RMB 300. Smaller trial orders with standard packaging are quoted separately. Ask Frank for an EXW, FOB or CIF quote.',
        'Elige blíster con tarjeta, caja a color o caja de cartón sencilla. En pedidos de al menos 5,000 piezas que combinan de dos a cuatro modelos en una misma plancha, bonificamos el cargo de 300 RMB por la placa de impresión. En los demás pedidos con impresión personalizada se cobran 300 RMB por placa. Cotizamos por separado los pedidos pequeños de prueba con empaque estándar. Solicita precio EXW, FOB o CIF.'
    ]
    oem_heads = ['OEM Wire Brush Packaging for Wholesale Orders', 'Empaque de marca propia para pedidos al mayoreo']
    for i, lang in enumerate(('en', 'es')):
        base = root if not i else root / 'es'
        for slug, pair in copy['pages'].items():
            file = base / slug / 'index.html'
            t = file.read_text()
            title, heading, description = pair[i]
            title += ' | YEKAI'
            t = re.sub(r'<title>.*?</title>', '<title>'+escape(title)+'</title>', t, count=1, flags=re.S)
            t = set_meta(t, 'description', description)
            t = set_meta(t, 'og:title', title, 'property')
            t = set_meta(t, 'og:description', description, 'property')
            def localized(tag, items):
                return f'<{tag} data-en="{escape(items[0])}" data-es="{escape(items[1])}">{escape(items[i])}</{tag}>'
            h1 = '<h1>'+escape(heading)+'</h1>' if slug else localized('h1', [row[1] for row in pair])
            t = re.sub(r'<h1\b[^>]*>.*?</h1>', lambda m:h1, t, count=1, flags=re.S)
            if not slug:
                t = re.sub(r'(<section class="oem" id="oem">.*?</div>)<h2.*?</p>', lambda m:m[1]+localized('h2',oem_heads)+localized('p',oem), t, count=1, flags=re.S)
            else:
                t = re.sub(r'<p class="lead">.*?</p>', '<p class="lead">'+escape(description)+'</p>',t,count=1)
            def schema(match):
                data=json.loads(match[1])
                for node in data.get('@graph',[data]):
                    if node.get('@type')=='WebPage':
                        node.update(name=title,description=description)
                return '<script type="application/ld+json">'+json.dumps(data,ensure_ascii=False)+'</script>'
            t=re.sub(r'<script type="application/ld\+json">(.*?)</script>',schema,t,flags=re.S)
            file.write_text(t)
        for key, product in copy['products'].items():
            file = base / 'products' / mapping[key]['slug'] / 'index.html'
            t=file.read_text()
            t=re.sub(r'(<img\b[^>]*? alt=")[^"]*',lambda m:m[1]+escape(product['alt'][i]),t,count=1)
            t=re.sub(r'<section id="buyer-links">.*?</section>', '',t,flags=re.S)
            links=[f'<a href="../{mapping[str(n)]["slug"]}/index.html">{escape(names[str(n)][lang])}</a>' for n in product['related']]
            links.append('<a href="../../index.html#oem">'+oem_heads[i]+'</a>')
            heading=['Ordering and related brushes','Pedidos y productos relacionados'][i]
            note=['Ask Frank for the minimum order quantity for this model, or send your target quantity and OEM packaging requirements for a quote.','Consulta a Frank sobre la cantidad mínima de este modelo o envía la cantidad que necesitas y el empaque de tu marca para cotizar.'][i]
            block=f'<section id="buyer-links"><h2>{heading}</h2><p>{note}</p><p>'+ ' · '.join(links)+'</p></section>'
            file.write_text(t.replace('</main>',block+'</main>',1))

    from maintain_seo import build as maintain_seo
    maintain_seo(root)

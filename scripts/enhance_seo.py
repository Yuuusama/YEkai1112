"""Offline navigation/content enhancements, rebuilt from existing product data."""
import html,json,re,os
from urllib.parse import quote
from maintain_seo import attrs

def build(root):
    esc=html.escape
    products=json.loads((root/'products.json').read_text())
    mapping=json.loads((root/'product-map.json').read_text())
    groups=[('steel-wire-wheel-brush','Wire & cup brushes','Discos y copas de alambre'),('abrasive-filament-brush','Abrasive filament brushes','Cepillos de filamento abrasivo'),('wire-grass-trimmer-head','Trimmer heads','Cabezales para desbrozadora'),('abrasive-flap-disc','Flap discs','Discos laminados')]
    advice={
      'steel-wire-wheel-brush':[
       ('Specify a wire brush for your order',[('Choose the brush shape','Compare wheel, bevel, cup and shank-mounted profiles against the part you need to clean. Include a photo of the working area when asking Frank to match a model.'),('Confirm wire and mounting','State whether you need crimped or knotted wire, then provide the outside diameter, working width and exact bore, thread or shank size. Confirm the wire material and rated speed for the selected model.'),('Build a wholesale assortment','List quantities separately for each size and construction. A mixed product range for a hardware store needs a clear packing list, especially when the cups and wheels use different mounts.')]),
       ('Cómo especificar un cepillo para tu pedido',[('Elige la forma','Compara discos, cepillos cónicos, copas y modelos con vástago según la pieza que necesitas limpiar. Envía una foto de la zona de trabajo para que Frank identifique el modelo.'),('Confirma alambre y montaje','Indica si necesitas alambre ondulado o trenzado, diámetro exterior, ancho y medida exacta del orificio, rosca o vástago. Confirma el material y las RPM del modelo seleccionado.'),('Prepara un surtido al mayoreo','Separa las cantidades por medida y tipo de cepillo. Para surtir una ferretería conviene detallar el empaque de cada modelo, sobre todo si las copas y los discos tienen montajes distintos.')])],
      'abrasive-filament-brush':[
       ('Choose an abrasive filament brush',[('Describe the finish','Send the workpiece material, its current surface condition and the finish you want. Include a photo or sample reference so the grit can be discussed for your application.'),('Match the catalog model','Compare wheel, cup and mounted shapes, then identify the outside diameter and mounting dimensions. The catalog table lists individual models, not every possible combination of diameter and grit.'),('Confirm a sample before bulk supply','Ask Frank which sample configuration matches your process. Keep the agreed diameter, grit, mounting and packing details on the bulk order specification.')]),
       ('Elige un cepillo de filamento abrasivo',[('Describe el acabado','Indica el material de la pieza, su estado actual y el acabado que buscas. Una foto o muestra de referencia ayuda a definir el grano para tu trabajo.'),('Identifica el modelo del catálogo','Compara las formas circular, de copa y con vástago. Revisa diámetro y montaje. La tabla muestra modelos individuales, no todas las combinaciones posibles de diámetro y grano.'),('Confirma la muestra','Consulta a Frank qué configuración conviene probar. Conserva las medidas, el grano, el montaje y el empaque acordados en la especificación del pedido al mayoreo.')])],
      'wire-grass-trimmer-head':[
       ('Compare trimmer head configurations',[('Identify your machine','Provide the machine make and model, power source and a clear photo of its mounting. Diameter alone does not establish compatibility.'),('Specify the head','Compare twisted-wire, three- or six-bundle and nylon series. Record the outside diameter, bundle count where applicable, and mounting details separately.'),('Confirm suitability before ordering','Ask Frank to confirm the exact head specification. Follow the equipment manufacturer’s permitted attachments, guard requirements and speed limits before use.')]),
       ('Compara configuraciones para desbrozadora',[('Identifica tu máquina','Envía marca, modelo, tipo de alimentación y una foto clara del montaje. El diámetro por sí solo no confirma la compatibilidad.'),('Especifica el cabezal','Compara las series de alambre trenzado, de tres o seis haces y de nailon. Anota diámetro, número de haces cuando corresponda y medidas del montaje.'),('Confirma antes de comprar','Consulta a Frank la especificación del modelo. Antes de usarlo, verifica los accesorios permitidos, las protecciones y los límites de velocidad indicados por el fabricante de la máquina.')])],
      'abrasive-flap-disc':[
       ('Specify flap discs for wholesale supply',[('Define the workpiece','Tell Frank which material you work on and whether you need stock removal or a finishing step. Confirm the abrasive type rather than identifying it by color alone.'),('Provide the disc dimensions','Include outside diameter, bore, grit and backing requirements. Send a label or sample photo when matching an existing item in your range.'),('Agree on packing','List quantities by grit and diameter and specify standard or private-label packaging. Confirm the product specification and label information before production.')]),
       ('Especifica discos laminados al mayoreo',[('Define el trabajo','Indica el material de la pieza y si buscas desbaste o acabado. Confirma el tipo de abrasivo sin identificarlo únicamente por el color.'),('Comparte las medidas','Incluye diámetro exterior, orificio central, grano y requisitos del respaldo. Para igualar un producto de tu surtido, envía una foto de la etiqueta o de una muestra.'),('Acuerda el empaque','Separa cantidades por grano y diámetro e indica empaque estándar o de marca propia. Confirma la especificación y los datos de la etiqueta antes de producir.')])]
    }
    for li,lang in enumerate(('en','es')):
        base=root if lang=='en' else root/'es'
        def relative(file,target):return os.path.relpath(target,file.parent).replace(os.sep,'/')
        for file in base.rglob('index.html'):
            if lang=='en' and 'es' in file.relative_to(root).parts:continue
            t=file.read_text()
            if '<main' not in t:continue
            # Attribute order varies after HTML formatting. Only replace the
            # main category nav; preserve the separate brush-family-links nav.
            def remove_category_nav(match):
                attributes=attrs(match[1])
                is_category='category-navigation' in attributes.get('class','').split()
                return '' if is_category and attributes.get('id')!='brush-family-links' else match[0]
            t=re.sub(r'(<nav\b[^>]*>).*?</nav>',remove_category_nav,t,flags=re.S)
            links=[]
            for slug,en,es in groups:
                active=' aria-current="page"' if file==base/slug/'index.html' else ''
                links.append(f'<a href="{relative(file,base/slug/"index.html")}"{active}>{esc(es if li else en)}</a>')
            nav='<nav class="category-navigation" aria-label="'+('Categorías de productos' if li else 'Product categories')+'">'+''.join(links)+'</nav>'
            t=re.sub(r'(<main\b[^>]*>)',lambda m:m[1]+nav,t,count=1)
            # A genuine link works without JavaScript and exposes each language URL.
            if file==base/'index.html':
                other=root/'index.html' if li else root/'es/index.html'
                # The existing language link is intentionally preserved.
            for slug,_,_ in groups:
                if file!=base/slug/'index.html':continue
                t=re.sub(r'<section id="category-buying-guide">.*?</section>','',t,flags=re.S)
                title,rows=advice[slug][li]
                block='<section id="category-buying-guide"><h2>'+esc(title)+'</h2>'+''.join('<h3>'+esc(h)+'</h3><p>'+esc(p)+'</p>' for h,p in rows)+'</section>'
                t=t.replace('</main>',block+'</main>',1)
                for p in products:
                    pattern=r'(<a class="range-card" href="[^\"]*/'+re.escape(mapping[str(p['id'])]['slug'])+r'/index.html">.*?<p>).*?(</p>)'
                    t=re.sub(pattern,lambda m:m[1]+esc(p['descEs' if li else 'desc'])+m[2],t,flags=re.S)
            for p in products:
                if file!=base/'products'/mapping[str(p['id'])]['slug']/'index.html':continue
                slug='abrasive-filament-brush' if p['category']=='abrasive' else 'wire-grass-trimmer-head' if p['category']=='outdoor' else 'abrasive-flap-disc' if p['category']=='flap' else 'steel-wire-wheel-brush'
                # Packaging and manual brushes return to the full catalog instead of a wrong category.
                category=next(g[li+1] for g in groups if g[0]==slug)
                target=relative(file,base/slug/'index.html')
                if p['category'] in ('hand','packaging'):category='Todos los productos' if li else 'All products';target=relative(file,base/'index.html')+'#products'
                crumb=f'<nav class="breadcrumb" aria-label="'+('Ruta de navegación' if li else 'Breadcrumb')+f'"><a href="{relative(file,base/"index.html")}">'+('Inicio' if li else 'Home')+f'</a> / <a href="{target}">{esc(category)}</a> / <span aria-current="page">{esc(p[lang])}</span></nav>'
                t=re.sub(r'<(?:div|nav)\b[^>]*\bclass="breadcrumb"[^>]*>.*?</(?:div|nav)>',lambda m:crumb,t,count=1,flags=re.S)
            if li:
                for old,new in [('Skip to content','Ir al contenido'),('Main navigation','Navegación principal'),('Open navigation','Abrir menú'),('Search products','Buscar productos'),('Chat with Frank on WhatsApp','Habla con Frank por WhatsApp'),('WIRE BRUSHES / ABRASIVE FILAMENTS / FLAP DISCS','CEPILLOS DE ALAMBRE / FILAMENTOS ABRASIVOS / DISCOS LAMINADOS'),('01 / FINISHING','01 / ACABADO'),('02 / SURFACE PREPARATION','02 / PREPARACIÓN DE SUPERFICIES'),('03 / HEAVY-DUTY BRUSHING','03 / CEPILLADO INTENSIVO'),('YEKAI · INDUSTRIAL ABRASIVES','YEKAI · ABRASIVOS INDUSTRIALES')]:
                    t=t.replace(old,new)
            if file.parent.name in [g[0] for g in groups]:
                name=next(g[li+1] for g in groups if g[0]==file.parent.name)
                url='https://wa.me/8619883954016?text='+quote(('Hola Frank, quisiera cotizar: ' if li else 'Hello Frank, please quote: ')+name,safe='')
                t=re.sub(r'(<a\b[^>]*id="sticky-quote"[^>]*href=")[^"]*',lambda m:m[1]+url,t)
            css=relative(file,root/'seo-enhancements.css')
            if 'seo-enhancements.css' not in t:t=t.replace('</head>',f'<link rel="stylesheet" href="{css}"></head>')
            file.write_text(t)

    from maintain_seo import build as maintain_seo
    maintain_seo(root)

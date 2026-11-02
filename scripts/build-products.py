from pathlib import Path
import json,re,html,os,urllib.parse,xml.etree.ElementTree as ET
from PIL import Image
R=Path(__file__).resolve().parents[1]; BASE='https://yekaifrank.com'
def load(n):return json.loads((R/n).read_text())
def dump(o):return json.dumps(o,ensure_ascii=False,separators=(',',':'))
def esc(s):return html.escape(str(s),quote=True)
products=load('products.json'); specs=load('product-specs.json'); mapping=load('product-map.json')
for p in products:
 s=specs[str(p['id'])];p['desc']=s['description']['en'];p['descEs']=s['description']['es']
 for lang in ('en','es'):
  es=lang=='es'; prefix='es/' if es else ''; root='../../../' if es else '../../';slug=mapping[str(p['id'])]['slug'];path=R/prefix/'products'/slug/'index.html';t=path.read_text()
  name=p[lang]; desc=s['description'][lang];url=f'{BASE}/{prefix}products/{slug}/'
  title=name+(' | Mayoreo y OEM | YEKAI' if es else ' | Wholesale & OEM | YEKAI')
  meta=s.get('meta',{}).get(lang,desc+(' Cotiza con Frank por WhatsApp.' if es else ' Request a quote from Frank on WhatsApp.'))
  t=re.sub(r'<title>.*?</title>','<title>'+esc(title)+'</title>',t)
  for tag,val in [('name="description"',meta),('property="og:title"',title),('property="og:description"',meta),('property="og:image"',BASE+'/'+p['image'])]:
   t=re.sub(r'<meta '+tag+r' content="[^"]*">','<meta '+tag+' content="'+esc(val)+'">',t)
  # Replace intro only; preserve photo, nav, form, catalog and business rules.
  t=re.sub(r'(<h1>.*?</h1>)<p>.*?</p>',lambda m:m[1]+'<p>'+esc(desc)+'</p>',t,count=1)
  if es:t=t.replace('FACTORY DIRECT · OEM PACKAGING','DIRECTO DE FÁBRICA · EMPAQUE OEM')
  rows=list(s['specifications'])
  pending='Consulta a Frank.' if es else 'Ask Frank.'
  extra=[('Model / pack quantity','Modelo / piezas por empaque'),('Bore, thread or shank confirmation','Confirmación de orificio, rosca o vástago'),('Maximum safe RPM','RPM máximas seguras'),('Equipment compatibility','Compatibilidad con el equipo'),('Certification scope','Alcance de certificaciones')]
  if s.get('catalogModels'): extra=[]
  table=''.join('<tr><th scope="row">'+esc(r[lang][0])+'</th><td>'+esc(r[lang][1])+'</td></tr>' for r in rows)
  table+=''.join('<tr><th scope="row">'+esc(b if es else a)+'</th><td>'+pending+'</td></tr>' for a,b in extra)
  block='<section id="product-specifications"><h2>'+('Especificaciones y opciones de la serie' if es else 'Series specifications and options')+'</h2><h3>'+('Configuración del producto' if es else 'Product configuration')+'</h3><table class="spec-table">'+table+'</table><p class="fine">'+('Las medidas corresponden a la gama; la fotografía no representa todas las combinaciones. Confirma el modelo antes de ordenar.' if es else 'Sizes describe the range; the photograph does not represent every combination. Confirm the selected model before ordering.')+'</p></section>'
  if s.get('catalogModels'):
   note=('Valores transcritos del catálogo original, página impresa 08. Las RPM indicadas son valores del catálogo, consulta a Frank para confirmar las RPM seguras del modelo actual; no son una autorización de uso. Confirma etiqueta, montaje y máquina antes de operar.' if es else 'Transcribed from the original catalog, printed page 08. RPM figures are catalog values, ask Frank to confirm the safe speed for the current model; they are not operating approval. Confirm product labeling, mounting and machine before use.')
   tables='<section id="catalog-models"><h2>'+('Modelos y empaque del catálogo' if es else 'Catalog models and packing')+'</h2><p class="fine">'+esc(note)+'</p>'
   for group in s['catalogModels']:
    heads=['Modelo','Ø exterior (mm)','RPM del catálogo*','Piezas / empaque','Caja (cm)'] if es else ['Model','Outside Ø (mm)','Catalog RPM*','Pieces / pack','Carton (cm)']
    tables+='<h3>'+esc(group[lang])+'</h3>'
    if group['mounted']:tables+='<p>'+('Vástago: 6 mm en los modelos listados.' if es else 'Shank: 6 mm for the listed models.')+'</p>'
    tables+='<div class="catalog-spec-scroll" tabindex="0" role="region" aria-label="'+esc(group[lang])+'"><table class="spec-table catalog-model-table"><thead><tr>'+''.join('<th scope="col">'+esc(h)+'</th>' for h in heads)+'</tr></thead><tbody>'+''.join('<tr>'+''.join(('<th scope="row">' if i==0 else '<td>')+esc(v)+('</th>' if i==0 else '</td>') for i,v in enumerate(row))+'</tr>' for row in group['rows'])+'</tbody></table></div>'
   tables+='</section>'
  else: tables=''
  t=re.sub(r'<section id="catalog-models">.*?</section>','',t,flags=re.S)
  if 'id="product-specifications"' in t:
   t=re.sub(r'<section id="product-specifications">.*?</section>',lambda m:block+tables,t,count=1,flags=re.S)
  else:
   t=re.sub(r'<section><h2>[^<]*</h2><table class="spec-table">.*?</table></section>',lambda m:block+tables,t,count=1,flags=re.S)
  t=re.sub(r'<section id="buying-notes">.*?</section>','',t,flags=re.S)
  notes='<section id="buying-notes"><h2>'+('Selección y compras para distribuidores' if es else 'Selection and distributor purchasing')+'</h2><h3>'+('Qué confirmar antes de cotizar' if es else 'What to confirm before requesting a quote')+'</h3><p>'+esc(s['buyingNotes'][lang])+'</p><h3>'+('Pedidos de mayoreo y empaque OEM' if es else 'Wholesale orders and OEM packaging')+'</h3><p>'+('Para ferreterías, distribuidores e importadores en México: envía cantidades por modelo, ciudad o puerto de destino y requisitos de empaque. Cotizamos después de confirmar la configuración.' if es else 'For hardware distributors, importers and industrial buyers supplying Mexico: send quantities by model, destination city or port and packaging requirements. Quotations follow configuration confirmation.')+'</p></section>'
  t=t.replace('<section class="quote-panel">',notes+'<section class="quote-panel">')
  t=re.sub(r'<section id="related-products">.*?</section>','',t,flags=re.S)
  related=[q for q in products if q['id']!=p['id'] and q['category']==p['category']][:3]
  if not related:related=[q for q in products if q['id'] in [1,2,8] and q['id']!=p['id']][:3]
  links=' · '.join('<a href="../'+mapping[str(q['id'])]['slug']+'/">'+esc(q[lang])+'</a>' for q in related)
  t=t.replace('</main>','<section id="related-products"><h2>'+('Productos relacionados' if es else 'Related products')+'</h2><p>'+links+'</p><p><a href="'+root+prefix+'index.html#products">'+('Ver todos los productos' if es else 'Browse all products')+'</a></p></section></main>')
  t=t.replace('Documentation & exhibitions','Documentation & exhibitions').replace('Factory Supply','Suministro de fábrica' if es else 'Factory Supply')
  # Only verified, visible basic product attributes; no offers or ratings.
  graph={'@context':'https://schema.org','@graph':[{'@type':'WebPage','@id':url+'#webpage','url':url,'name':title,'description':meta,'inLanguage':'es-MX' if es else 'en','mainEntity':{'@id':url+'#product'}},{'@type':'Product','@id':url+'#product','name':name,'description':desc,'image':BASE+'/'+p['image'],'url':url,'brand':{'@type':'Brand','name':'YEKAI'},'additionalProperty':[{'@type':'PropertyValue','name':r[lang][0],'value':r[lang][1]} for r in rows]}]}
  t=re.sub(r'<script type="application/ld\+json">.*?</script>','<script type="application/ld+json">'+dump(graph)+'</script>',t,flags=re.S)
  # The product photo is the above-the-fold image.
  t=re.sub(r'(<div class="detail-product-image">.*?)(</div>)',lambda m:re.sub(r'alt="[^"]*"','alt="'+esc(name)+'"',m[1]).replace('loading="lazy"','loading="eager" fetchpriority="high"')+m[2],t,count=1,flags=re.S)
  path.write_text(t)
(R/'products.json').write_text(dump(products))
# Synchronize static/home fallback content and runtime data from one product source.
for lang in ('en','es'):
 path=R/('es/index.html' if lang=='es' else 'index.html');t=path.read_text()
 t=re.sub(r'(<script id="product-data" type="application/json">).*?(</script>)',lambda m:m[1]+dump(products)+m[2],t,flags=re.S)
 path.write_text(t)
# Regional language metadata and dimensions across the retained site.
for path in R.rglob('*.html'):
 t=path.read_text(); is_es=path.relative_to(R).parts[0]=='es'
 t=t.replace('hreflang="es"','hreflang="es-MX"')
 if is_es:
  t=t.replace('lang="es"','lang="es-MX"').replace('"inLanguage": "es"','"inLanguage": "es-MX"').replace('"inLanguage":"es"','"inLanguage":"es-MX"')
  t=t.replace('Factory Supply','Suministro de fábrica').replace('Wholesale &amp; OEM Factory','Mayoreo y OEM de fábrica').replace('Wholesale & OEM Factory','Mayoreo y OEM de fábrica')
 # Remove exact duplicate link tags and duplicate root attributes from previous package.
 seen=set()
 def unique(m):
  tag=m[0]
  if tag in seen:return ''
  seen.add(tag);return tag
 t=re.sub(r'<link\b[^>]*>',unique,t)
 t=re.sub(r'(data-root="[^"]*")\s+\1',r'\1',t)
 def image(m):
  tag=m[0];src=re.search(r'src="([^"]+)"',tag)
  if not src or src[1].startswith(('http','data:')):return tag
  img=(path.parent/urllib.parse.unquote(src[1].split('?')[0])).resolve()
  if img.is_file():
   try:
    w,h=Image.open(img).size
    if 'width=' not in tag:tag=tag[:-1]+f' width="{w}" height="{h}">'
   except Exception:pass
  if is_es:
   for p in products:
    if src[1].endswith(p['image']):tag=re.sub(r'alt="[^"]*"','alt="'+esc(p['es'])+'"',tag)
  if 'alt=' not in tag:tag=tag[:-1]+' alt="">'
  return tag
 t=re.sub(r'<img\b[^>]*>',image,t);path.write_text(t)
# Sitemap contains only canonical, indexable pages present in the package.
urls=[]
for path in sorted(R.rglob('index.html')):
 t=path.read_text()
 if re.search(r'<meta[^>]+content="[^"]*noindex',t,re.I):continue
 m=re.search(r'<link rel="canonical" href="([^"]+)"',t)
 if m:urls.append(m[1])
assert len(urls)==len(set(urls))
(R/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+esc(u)+'</loc></url>' for u in urls)+'</urlset>')
print(f'Updated {len(products)} products, 32 detail pages, {len(urls)} sitemap URLs.')

# Generated dimensions keep JS-rendered cards consistent with static HTML.
dimensions={p['image']:list(Image.open(R/p['image']).size) for p in products}
app=R/'app.js';js=app.read_text()
js=re.sub(r'const productImageSizes=.*?;\n','',js)
js='const productImageSizes='+dump(dimensions)+';\n'+js
js=js.replace('alt="${p[lang]}" loading="lazy">','alt="${p[lang]}" loading="lazy" width="${productImageSizes[p.image][0]}" height="${productImageSizes[p.image][1]}">')
app.write_text(js)

from build_configurations import build
build(R)

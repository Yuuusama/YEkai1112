"""Maintained bilingual display/path/conversion updates. Run after all generators."""
from pathlib import Path
from urllib.parse import urljoin,urlsplit,quote
import json,re
from bs4 import BeautifulSoup
BASE='https://yekaifrank.com'
def build(root):
 root=Path(root)
 def fragment(markup):return BeautifulSoup(markup,'html.parser')
 for f in root.rglob('*.html'):
  page='/'+f.relative_to(root).as_posix().removesuffix('index.html');es=page.startswith('/es/');s=BeautifulSoup(f.read_text(),'html.parser')
  indexed=bool(s.h1) and not s.select_one('meta[name="robots"][content*="noindex"]')
  home=page in ['/', '/es/'];label='Cotizar por WhatsApp' if es else 'Get a WhatsApp quote'
  def put(e,text):
   if e:
    e.clear();e.append(text)
    for a in ['data-en','data-es']:e.attrs.pop(a,None)
  def wa(name=''):
   msg=('Hola Frank, quisiera cotizar '+name+'. ¿Me compartes las opciones y condiciones de compra?' if es else 'Hello Frank, please quote '+name+'. Please share the options and order terms.') if name else ('Hola Frank, me interesan los cepillos YEKAI para mi negocio. Quisiera una cotización.' if es else 'Hello Frank, I am interested in YEKAI brushes for my business. Please send a quotation.')
   return 'https://wa.me/8619883954016?text='+quote(msg)
  def cta(name='',cls='btn'):
   a=s.new_tag('a',href=wa(name),attrs={'class':cls,'target':'_blank','rel':'noopener noreferrer'});a.string=('Cotizar este producto por WhatsApp' if es else 'Quote this product on WhatsApp') if name else label;return a
  if indexed:
   if not s.select_one('link[href="/site-refinements.css"]'):s.head.append(s.new_tag('link',rel='stylesheet',href='/site-refinements.css'))
   for x in s.select('link[hreflang="es-MX"]'):x['hreflang']='es'
   if home:
    s.body['data-root']='/'
    ann=s.select_one('.announcement')
    if ann:ann.decompose()
    put(s.select_one('.hero .eyebrow'), 'Fabricante en Yongkang, China' if es else 'Manufacturer in Yongkang, China')
    h=s.select_one('.hero h1');put(h,'');h.append(fragment('Cepillos de alambre<br/>directo de fábrica' if es else 'Wire brushes<br/>direct from the factory'))
    put(s.select_one('.hero-inner > p'),'Discos, copas y cepillos para distribuidores y ferreterías. Fabricamos en Yongkang y cotizamos según tu modelo, cantidad y destino.' if es else 'Wire wheels, cup brushes and brushes for distributors and hardware stores. Made in Yongkang; quotes based on your model, quantity and destination.')
    if not s.select_one('.hero-benefits'):
     ul=s.new_tag('ul',attrs={'class':'hero-benefits'})
     for text in (['Marca propia / OEM','Pedidos pequeños y muestras','Exportación a todo el mundo · DDP a México bajo cotización'] if es else ['Private label / OEM','Small orders and samples','Worldwide export shipping · DDP to Mexico on request']):
      li=s.new_tag('li');li.string=text;ul.append(li)
     s.select_one('.hero-inner > p').insert_after(ul)
    buttons=s.select_one('.hero-buttons');buttons.clear();buttons.append(cta())
    for dest,text in [('products','Descubre los productos' if es else 'Explore products'),('catalog','Ver el catálogo' if es else 'View the catalog')]:
     a=s.new_tag('a',href='#'+dest,attrs={'class':'hero-link'});a.string=text;buttons.append(a)
    navcta=s.select_one('.header-actions .btn')
    if navcta:navcta.replace_with(cta(cls='btn compact'))
    lang=s.select_one('#language')
    if lang:lang['aria-label']='Read in English' if es else 'Leer en español';lang.string='EN / ES';lang['href']='/' if es else '/es/'
    if not s.select_one('#oem .delivery-options'):
     p=s.new_tag('p',attrs={'class':'delivery-options'});p.string='DDP a México disponible bajo cotización. Muestras antes del pedido a granel' if es else 'DDP to Mexico available on request. Samples before bulk orders';s.select_one('.oem-copy').append(p)
    for id,txt in {'need':'Ej. disco trenzado de 100 mm','quantity':'Ej. 5,000 piezas','destination':'Ej. México'}.items():
     if es and s.select_one('#'+id):s.select_one('#'+id)['placeholder']=txt
    if not s.select_one('#catalog .catalog-pdf-pending'):
     box=fragment('<div class="catalog-pdf-pending"><button class="btn secondary" type="button" disabled>'+('Descargar catálogo completo (PDF)' if es else 'Download full catalog (PDF)')+'</button><p>'+('PDF pendiente de publicación. Puedes consultar las páginas del catálogo a continuación.' if es else 'PDF awaiting publication. Browse the catalog pages below.')+'</p></div>');s.select_one('#catalog .section-head').insert_after(box)
    for a in s.select('.document-card'):
     if a.select_one('.document-scope'):continue
     fn=a.get('href','');p=s.new_tag('p',attrs={'class':'document-scope'})
     if 'trimmer-design' in fn:txt=('Producto: cabezal para desbrozadora; consulta el diseño cubierto en la patente.' if es else 'Product: trimmer head; see the patent for the covered design.')
     elif 'wire-wheel-patent' in fn:txt=('Producto: disco de alambre trenzado; consulta el modelo cubierto en la patente.' if es else 'Product: twisted wire wheel; see the patent for the covered model.')
     else:txt=('Confirma con Frank qué productos y modelos están cubiertos por este documento.' if es else 'Confirm with Frank which products and models this document covers.')
     p.string=txt;a.append(p)
    if not s.select_one('#all-product-links'):
     sec=s.new_tag('section',id='all-product-links',attrs={'class':'section product-directory'});h2=s.new_tag('h2');h2.string='Todas las series de productos' if es else 'All product series';sec.append(h2);nav=s.new_tag('nav',attrs={'aria-label':'Todas las series' if es else 'All product series'})
     for p in json.loads((root/'products.json').read_text()):
      # Use existing generated pages and their visible H1; preserve catalog order.
      app=(root/'app.js').read_text();slugs=json.loads(re.search(r'const productSlugs=(.*?);',app)[1]);slug=slugs.get(str(p['id']))
      if slug:
       link=s.new_tag('a',href=('/es/' if es else '/')+'products/'+slug+'/');link.string=p['es' if es else 'en'];nav.append(link)
     sec.append(nav);s.select_one('#products').insert_after(sec)
   elif '/products/' in page:
    name=s.h1.get_text(' ',strip=True)
    for x in s.select('.product-direct-quote,.product-bottom-quote'):x.decompose()
    intro=s.select_one('.product-intro > div:last-child')
    if intro:intro.append(cta(name,'btn product-direct-quote'))
    s.main.append(cta(name,'btn product-bottom-quote'))
    sticky=s.select_one('#sticky-quote')
    if sticky:put(sticky,'Cotizar este producto por WhatsApp' if es else 'Quote this product on WhatsApp')
    for x in s.select('.detail-header nav a'):
     if x.get_text(strip=True) in ['EN','ES']:x['class']=['language']
  if indexed:
   for a in s.select('a[href*="wa.me"],a[data-wa],#product-inquiry button,.inquiry button'):
    a['class']=list(dict.fromkeys(a.get('class',[])+['wa-primary']))
   if home:
    s.select('.hero-benefits li')[-1].string='Exportación a todo el mundo · DDP a México bajo cotización' if es else 'Worldwide export shipping · DDP to Mexico on request'
    p=s.select_one('.delivery-options')
    if p:p.string='DDP a México disponible bajo cotización. Muestras antes del pedido a granel.' if es else 'DDP to Mexico available on request. Samples before bulk orders.'
    for p in s.select('#oem p'):
     if 'EXW / FOB / CIF' in p.get_text():
      sentence='DDP a México disponible bajo cotización.' if es else 'DDP to Mexico available on request.'
      if sentence not in p.get_text():p.append(' '+sentence)
      for key in ['data-en','data-es']:p.attrs.pop(key,None)
   switch=s.select_one('#language') if home else s.select_one('.detail-header .language-switch') or s.select_one('.detail-header a.language')
   if switch:
    wrapper=s.new_tag('span',attrs={'class':'language-switch','aria-label':'Idioma' if es else 'Language'})
    if home:wrapper['id']='language'
    en=page.replace('/es/','/',1) if es else page
    for code,dest,active in [('EN',en,not es),('ES','/es'+en,es)]:
     item=s.new_tag('span' if active else 'a',attrs={'class':'language-current' if active else 'language-option'})
     item.string=code
     if active:item['aria-current']='true'
     else:item['href']=dest
     wrapper.append(item)
    switch.replace_with(wrapper)
  # Root-relative local resources and internal links; canonical/schema URLs stay absolute.
  for e in s.find_all(True):
   for attr in ['src','href','poster']:
    val=e.get(attr)
    if not val or val.startswith(('data:','mailto:','tel:','javascript:')):continue
    if attr=='href' and e.name=='link' and ('canonical' in e.get('rel',[]) or e.get('hreflang')):continue
    u=urlsplit(urljoin(BASE+page,val))
    if u.netloc!='yekaifrank.com':continue
    path=u.path.removesuffix('index.html');e[attr]=path+('?' + u.query if u.query else '')+('#'+u.fragment if u.fragment else '')
  f.write_text(re.sub(r'(?i)(<!doctype html>)\s*',r'\1\n',str(s)))
 # Dynamic product / catalog resources share the root; product links retain language.
 app=root/'app.js';t=app.read_text();t=t.replace("const assetRoot=document.body.dataset.root||'';","const assetRoot='/';")
 t=t.replace('href="products/${productSlugs[p.id]}/index.html"','href="${lang===\'es\'?\'/es/\':\'/\'}products/${productSlugs[p.id]}/"')
 t=t.replace("$('#language').textContent=lang==='en'?'ES':'EN'","$('#language').textContent='EN / ES'")
 t=t.replace("$('#language').textContent='EN / ES';",'')
 app.write_text(t)
if __name__=='__main__':build(Path(__file__).resolve().parents[1])

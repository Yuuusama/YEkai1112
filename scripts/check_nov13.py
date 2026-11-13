"""Local HTTP and bilingual checks. No deployment or external requests."""
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlsplit, unquote, urljoin, parse_qs
import sys, json, re, subprocess, time, urllib.request, tempfile
R=Path(__file__).resolve().parents[1]
errors=[];paths=set(['/products.json','/sitemap.xml']);words=[];titles=[];descs=[]
pages=[]
for f in R.rglob('*.html'):
 s=BeautifulSoup(f.read_text(),'html.parser');page='/'+f.relative_to(R).as_posix().removesuffix('index.html')
 if 'file:///' in f.read_text():errors.append(page+': local file URL')
 for e in s.select('[href],[src],[poster]'):
  for attr in ('href','src','poster'):
   val=e.get(attr)
   if not val or val.startswith(('mailto:','tel:','data:','https://','http://','javascript:')):continue
   if not val.startswith('/'):errors.append(page+': non-root '+val)
   paths.add(urlsplit(urljoin(page,val)).path)
 if not s.h1 or s.select_one('meta[name="robots"][content*="noindex"]'):continue
 pages.append(page);paths.add(page);titles.append(s.title.get_text());descs.append(s.select_one('meta[name="description"]')['content'])
 if page.startswith('/es/'):
  for img in s.select('img'):
   if not img.get('alt'):errors.append(page+': missing Spanish alt')
 if '/products/' in page:
  for cls in ('.product-direct-quote','.product-bottom-quote'):
   a=s.select_one(cls)
   if not a or s.h1.get_text(' ',strip=True) not in parse_qs(urlsplit(a['href']).query).get('text',[''])[0]:errors.append(page+': missing named CTA '+cls)
  if not s.select_one('#buyer-links a[href*="/products/"]'):errors.append(page+': missing related product')
  if page.startswith('/es/'):
   m=s.main
   for x in m.select('nav,form,table,script,a,select'):x.decompose()
   count=len(re.findall(r'\b\w+\b',m.get_text(' ',strip=True)));words.append({'url':page,'body_words_excluding_navigation_forms_tables_links':count})
   if count<300:errors.append(page+': under 300 words')
if len(titles)!=len(set(titles)):errors.append('Duplicate titles')
if len(descs)!=len(set(descs)):errors.append('Duplicate descriptions')
data=json.loads((R/'products.json').read_text());app=(R/'app.js').read_text();slugs=json.loads(re.search(r'const productSlugs=(.*?);',app)[1])
assert "const assetRoot='/';" in app
for p in data:paths.add('/'+p['image'])
for n in range(4,16):paths.add('/images/catalog/'+str(n)+'.webp')
for lang in ('','es/'):
 s=BeautifulSoup((R/lang/'index.html').read_text(),'html.parser');links={a['href'] for a in s.select('#all-product-links a')}
 expected={'/'+lang+'products/'+slugs[str(p['id'])]+'/' for p in data}
 if links!=expected:errors.append(lang+': product directory mismatch')
http=[]
with tempfile.TemporaryFile() as log:
 proc=subprocess.Popen([sys.executable,'-m','http.server','8877','--bind','127.0.0.1','--directory',str(R)],stdout=log,stderr=log)
 try:
  for attempt in range(30):
   try:urllib.request.urlopen('http://127.0.0.1:8877/',timeout=2).close();break
   except Exception:
    if proc.poll() is not None:raise RuntimeError('Local HTTP server could not start')
    time.sleep(.1)
  for path in sorted(paths):
   try:
    with urllib.request.urlopen('http://127.0.0.1:8877'+path,timeout=5) as res:
     body=res.read();http.append({'path':path,'status':res.status,'bytes':len(body)})
     if res.status!=200 or not body:errors.append('HTTP failed '+path)
   except Exception as e:errors.append('HTTP '+path+': '+str(e))
 finally:proc.terminate();proc.wait()
result={'indexable_pages':len(pages),'unique_titles':len(set(titles)),'unique_descriptions':len(set(descs)),'spanish_product_body_counts':words,'local_http_server':'python -m http.server (127.0.0.1:8877)','http_resources_tested':len(http),'http_results':http,'errors':errors,'unverified':['Actual browser rendering on desktop/mobile','Real external WhatsApp opening','Live Netlify redirect responses','Search Console submission and indexing','Certificate product scope','Hero authenticity against original factory photo']}
print(json.dumps(result,ensure_ascii=False,indent=2));sys.exit(bool(errors))

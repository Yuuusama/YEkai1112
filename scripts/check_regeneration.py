"""Regression checks in a temporary copy; never edits the source or contacts hosting.
Requires the existing Pillow dependency and Node.js for the isolated quote test.
Usage: python scripts/check_regeneration.py
"""
from pathlib import Path
from tempfile import TemporaryDirectory
from collections import Counter
import shutil,subprocess,sys,json,hashlib,re
from maintain_seo import Tags,attrs,meta,canonical
ROOT=Path(__file__).resolve().parents[1]
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def snapshot(root):
 return {p.relative_to(root).as_posix():digest(p) for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts}
def run_validation(root):
 result=subprocess.run([sys.executable,str(root/'scripts/validate_seo.py')],capture_output=True,text=True,check=True)
 checks=json.loads(result.stdout)
 contacts=subprocess.run([sys.executable,str(root/'scripts/validate_contact_channels.py')],capture_output=True,text=True,check=True)
 checks['contacts']=json.loads(contacts.stdout)
 return checks
def quote_cases(root):
 cases=[]
 for f in sorted(root.glob('**/products/*/index.html')):
  t=f.read_text();m=re.search(r'<form\b(?=[^>]*\bid="product-inquiry")[^>]*>.*?</form>',t,re.S)
  if not m:continue
  fields={a['name']:a.get('value','') for k,a in Tags(m[0]).tags if k=='input' and a.get('name')}
  for select in re.finditer(r'<select\b[^>]*>.*?</select>',m[0],re.S):
   tags=Tags(select[0]).tags;name=tags[0][1]['name'];options=[a for k,a in tags if k=='option'];choice=next((a for a in options if 'selected' in a),options[0]);fields[name]=choice.get('value','')
  scripts=re.finditer(r'(<script\b[^>]*>)(.*?)(</script>)',t,re.S)
  choices=next(json.loads(s[2]) for s in scripts if attrs(s[1]).get('id')=='configuration-data')
  lang=next(a['lang'] for k,a in Tags(t).tags if k=='html')
  cases.append({'path':f.relative_to(root).as_posix(),'lang':lang,'product':attrs(m[0]).get('data-product'),'choices':choices,'fields':fields})
 return cases
def protected_files(root):
 names={'products.json','product-specs.json','product-configurations.json','size-reference-review.json','product-map.json','app.js','quote.js','_redirects'}
 names.update(f.relative_to(root).as_posix() for f in (root/'images').rglob('*') if f.is_file())
 names.update(f.relative_to(root).as_posix() for f in root.glob('**/products/*/index.html') if 'noindex' in meta(f.read_text(),'robots'))
 return names
def signature(root):
 out={}
 for f in root.rglob('index.html'):
  t=f.read_text();tags=Tags(t).tags
  if not canonical(t) or 'noindex' in meta(t,'robots'):continue
  switches=[(a.get('href'),a.get('hreflang')) for k,a in tags if k=='a' and ('language' in a.get('class','').split() or a.get('hreflang'))]
  imgs=[a.get('src') for k,a in tags if k=='img']
  family=re.search(r'<nav\b(?=[^>]*\bid="brush-family-links")[^>]*>.*?</nav>',t,re.S)
  family_links=[a.get('href') for k,a in Tags(family[0]).tags if k=='a'] if family else []
  out[f.relative_to(root).as_posix()]={'canonical':canonical(t),'switches':switches,'images':imgs,'family_links':family_links,'h1':re.search(r'<h1\b[^>]*>(.*?)</h1>',t,re.S)[1]}
 return out
if __name__=='__main__':
 original=snapshot(ROOT);keep=protected_files(ROOT);baseline=signature(ROOT);run_validation(ROOT)
 with TemporaryDirectory(prefix='yekai-regression-') as temp:
  copy=Path(temp)/'site';shutil.copytree(ROOT,copy,ignore=shutil.ignore_patterns('__pycache__'))
  for i in range(2):
   subprocess.run([sys.executable,str(copy/'scripts/build-products.py')],check=True,capture_output=True,text=True)
   checks=run_validation(copy);now=snapshot(copy)
   assert all(now[k]==original[k] for k in keep),'Protected files changed'
   assert signature(copy)==baseline,'URL, language, image, H1 or family links changed'
   if i==0:first=now
   else:assert now==first,'Second generation was not byte-for-byte stable'
  cases=Path(temp)/'quote-cases.json';cases.write_text(json.dumps(quote_cases(copy),ensure_ascii=False))
  quote=subprocess.run(['node',str(copy/'scripts/test_quote_logic.cjs'),str(cases)],check=True,capture_output=True,text=True)
  result={'build_runs':2,'second_run_changed_files':0,'protected_files_unchanged':len(keep),'canonical_language_images_h1_preserved':len(baseline),'indexable_pages':checks['indexable_pages'],'local_references':checks['local_html_css_references'],'static_errors':len(checks['errors']),'quote_simulation':json.loads(quote.stdout),'unverified':['Real browser layout and interactions','Live HTTP/Netlify routing','Google indexing and rich-result eligibility']}
  result['homepage_contacts']=checks['contacts']['homepage_contacts']
  result['contact_errors']=len(checks['contacts']['errors'])
 assert snapshot(ROOT)==original,'Source directory was changed'
 print(json.dumps(result,ensure_ascii=False,indent=2))

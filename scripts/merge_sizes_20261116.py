"""2026-11-16 合并重复尺寸：同一尺寸的英寸选项和毫米选项合并为一个，例如 3" (75 mm)。
影响产品 id 8、10、7、2（编织碗刷、波浪丝碗刷、宽面轮刷、斜角刷）。
直接修改 product-configurations.json、product-specs.json，以及这 4 个产品的中英西页面：
配置选项、configuration-data、规格表"系列外径"行；并删除单独的"毫米直径"区块。
不重新跑 build_configurations（旧生成器会改到其他页面）。脚本可重复执行，结果不变。
"""
from pathlib import Path
import html, json, re, sys

R = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
# mm -> 行业对应英寸
INCH = {65: '2.5', 75: '3', 90: '3.5', 100: '4', 115: '4.5', 125: '5', 150: '6', 175: '7', 200: '8', 250: '10', 300: '12'}
MM = {v: k for k, v in INCH.items()}
PIDS = ['8', '10', '7', '2']
# 3.5" no es medida regular en la copa trenzada (id 8); se fabrica bajo pedido
SUF = {'8': {'en': '; 3.5" (90 mm) on request', 'es': '; 3.5" (90 mm) bajo pedido'}}
DROP = {80, 85, 90, 110, 178}  # 2026-11-16 Frank: estas medidas no se fabrican
ASK = [('Wire material / diameter', 'Material / diámetro del alambre'), ('Bore / thread / shank', 'Orificio / rosca / vástago'),
       ('Maximum safe RPM', 'RPM máximas seguras'), ('Pieces / pack', 'Piezas / empaque')]

configs = json.loads((R / 'product-configurations.json').read_text())
specs = json.loads((R / 'product-specs.json').read_text())
mapping = json.loads((R / 'product-map.json').read_text())


def label(mm, lang):
    i = INCH.get(mm)
    if not i: return f'{mm} mm'
    return f'{i}" ({mm} mm)' if lang == 'en' else f'{i}" ({mm} mm)'


def mm_of(entry):
    m = re.search(r'(\d+) mm', entry['en'])
    if m: return int(m.group(1))
    m = re.match(r'([\d.]+) inch', entry['en'])
    return MM[m.group(1)] if m else None


summary = {}
for pid in PIDS:
    old = configs[pid]
    form = next((e for e in old if e.get('sizeSource')), None)
    if form is None:  # ya fusionado
        form_en, form_es = old[0]['rows'][0]['en'][1], old[0]['rows'][0]['es'][1]
    else:
        form_en, form_es = form['rows'][0]['en'][1], form['rows'][0]['es'][1]
    sizes = sorted({mm_of(e) for e in old} - DROP)
    assert None not in sizes, (pid, [e['en'] for e in old])
    new = []
    for mm in sizes:
        rows = [{'en': ['Brush form', form_en], 'es': ['Forma', form_es]},
                {'en': ['Outside diameter', label(mm, 'en')], 'es': ['Diámetro exterior', label(mm, 'es')]}]
        rows += [{'en': [a, 'Ask Frank.'], 'es': [b, 'Consulta a Frank.']} for a, b in ASK]
        new.append({'en': label(mm, 'en'), 'es': label(mm, 'es'), 'rows': rows, 'sizeMm': mm})
    configs[pid] = new
    series_en = ', '.join(label(mm, 'en') for mm in sizes)
    for r in specs[pid]['specifications']:
        if r['en'][0] == 'Series outside diameters':
            r['en'][1] = series_en + SUF.get(pid, {}).get('en', ''); r['es'][1] = series_en + SUF.get(pid, {}).get('es', '')
    summary[pid] = (len(old), len(new), series_en)

(R / 'product-configurations.json').write_text(json.dumps(configs, ensure_ascii=False, indent=2))
(R / 'product-specs.json').write_text(json.dumps(specs, ensure_ascii=False, indent=2))

esc = lambda s: html.escape(str(s), quote=True)
for pid in PIDS:
    slug = mapping[pid]['slug']; series = summary[pid][2]
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
        t = re.sub(r'<section id="available-diameters">.*?</section>', '', t, flags=re.S)
        th = 'Series outside diameters' if lang == 'en' else 'Diámetros exteriores de la serie'
        t, n = re.subn(r'(<tr><th scope="row">' + th + r'</th><td>)[^<]*(</td></tr>)', lambda m: m.group(1) + esc(series + SUF.get(pid, {}).get(lang, '')) + m.group(2), t, count=1)
        assert n == 1, f
        f.write_text(t)

# 2b) 宽面轮介绍/描述里的范围 4–10 → 4–12（全站，含产品数据文件）；以及 JSON-LD 里的系列外径要和选项一致
RANGE = [('4, 5, 6, 7, 8 or 10 in', '4, 5, 6, 7, 8, 10 or 12 in'),
         ('4, 5, 6, 7, 8 o 10 pulgadas', '4, 5, 6, 7, 8, 10 o 12 pulgadas')]
for f in list(R.rglob('*.html')) + [R / 'products.json', R / 'product-specs.json']:
    if 'reports' in f.parts or not f.exists(): continue
    t = f.read_text(); o = t
    for a, b in RANGE: t = t.replace(a, b)
    if t != o: f.write_text(t)
for pid in PIDS:
    slug = mapping[pid]['slug']; series = summary[pid][2]
    for lang, base in (('en', R), ('es', R / 'es')):
        f = base / 'products' / slug / 'index.html'; t = f.read_text()
        val = json.dumps(series + SUF.get(pid, {}).get(lang, ''), ensure_ascii=False)[1:-1]
        t = re.sub(r'("name":\s*"(?:Series outside diameters|Diámetros exteriores de la serie)",\s*"value":\s*")(?:[^"\\]|\\.)*(")',
                   lambda m: m.group(1) + val + m.group(2), t)
        f.write_text(t)

for pid, (a, b, s) in summary.items():
    print(f'id {pid}: {a} -> {b} opciones · {s}')

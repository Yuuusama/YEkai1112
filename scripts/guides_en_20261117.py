"""2026-11-17 — English buyer guides (8) + FAQ, mirroring the Spanish guides.
Imported by scripts/seo_mx_20261116.py. Uses only data already on the product pages
(sizes, wire, knot counts, grit range, packaging terms). No prices, lead times or RPM figures.
"""
P = lambda s: f'<p>{s}</p>'
def link(path, label): return f'<a href="{path}">{label}</a>'
PR = '/products/'
G = '/guides/'

# Spanish slug -> English slug (hreflang pairs)
PAIR = {
 'carda-trenzada-o-ondulada': 'knotted-vs-crimped-wire-brush',
 'medidas-de-carda': 'wire-brush-sizes-and-threads',
 'importar-cardas-de-china': 'import-wire-brushes-from-china',
 'carda-para-soldadura': 'wire-brush-for-weld-cleaning',
 'carda-para-quitar-oxido-y-pintura': 'wire-brush-for-rust-and-paint-removal',
 'cepillo-para-desbrozadora': 'wire-weed-brush-for-brush-cutter',
 'cepillo-de-nylon-abrasivo': 'abrasive-nylon-brush',
 'cardas-con-tu-marca': 'private-label-wire-brushes',
}

GUIDES_EN = [
 ('knotted-vs-crimped-wire-brush', 'Knotted vs crimped wire brush: which to choose'),
 ('wire-brush-sizes-and-threads', 'Wire brush sizes, threads and arbor holes'),
 ('import-wire-brushes-from-china', 'How to import wire brushes from China'),
 ('wire-brush-for-weld-cleaning', 'Wire brush for weld cleaning: which type'),
 ('wire-brush-for-rust-and-paint-removal', 'Wire brush for rust and paint removal'),
 ('wire-weed-brush-for-brush-cutter', 'Wire weed brush for brush cutters: how to choose'),
 ('abrasive-nylon-brush', 'Abrasive nylon brush: uses and grit'),
 ('private-label-wire-brushes', 'Private label wire brushes: OEM packaging'),
]

SAFETY = P('The maximum safe speed (RPM) marked on the brush must be equal to or higher than the speed of the machine. Always use the guard, eye protection and gloves. Ask Frank to confirm the RPM of the model you choose.')

CONTENT_EN = {
'knotted-vs-crimped-wire-brush': dict(
 title='Knotted vs Crimped Wire Brush: Which to Choose',
 h1='Knotted vs crimped wire brush: how to choose the right one',
 desc='The difference between knotted (twist knot) and crimped wire brushes, and between wheel, cup, bevel and shank-mounted shapes. A guide for distributors.',
 body=[
  P('A power wire brush is defined by two things: the <strong>wire style</strong> (crimped or knotted) and the <strong>shape</strong> (wheel, cup, bevel or shank-mounted). Settle both before asking for a price.'),
  '<h2>Crimped wire brushes</h2>',
  P('The wires are loose and wavy, so the brush is more flexible. Use it for light to medium cleaning: surface rust, loose paint and dirt, with a more even finish on wide areas.'),
  P('In our range: ' + link(PR + 'crimped-wire-cup-brushes/', 'crimped wire cup brushes') + ' (2.5 to 6 in), ' + link(PR + 'wide-crimped-wire-wheels/', 'wide-face crimped wire wheels') + ' (4 to 12 in, typical wire 0.3 mm) and ' + link(PR + 'crimped-wire-brush-wheels/', 'crimped wire brush wheels with a metal hub') + '.'),
  '<h2>Knotted (twist knot) wire brushes</h2>',
  P('The wire is twisted into knots, which makes the brush stiffer and more aggressive. Choose it for heavy work: thick rust, mill scale, slag and weld seams.'),
  P('In our range: ' + link(PR + 'red-knotted-wire-cup-brush/', 'knotted wire cup brush') + ' (2.5 to 6 in), ' + link(PR + 'banded-twisted-cup-brushes/', 'banded knot cup brush') + ' (2.5 to 5 in), ' + link(PR + 'twisted-wire-wheels/', 'knotted bevel brush') + ' (4 to 5 in, typical wire 0.5 mm) and ' + link(PR + 'stringer-knotted-wheels/', 'stringer bead wheel for welds') + ' (4.5 to 7 in).'),
  '<h2>Quick comparison</h2>',
  '<table class="guide-table"><thead><tr><th></th><th>Crimped</th><th>Knotted</th></tr></thead><tbody>'
  '<tr><th>Action</th><td>Flexible, gentler</td><td>Stiff, more aggressive</td></tr>'
  '<tr><th>Typical job</th><td>Light rust, loose paint, general cleaning</td><td>Heavy rust, scale, weld seams</td></tr>'
  '<tr><th>Finish</th><td>More even</td><td>More marked</td></tr></tbody></table>',
  '<h2>Wheel, cup, bevel or shank-mounted</h2>',
  P('<strong>Wheel brush:</strong> works on its edge; wheels with an arbor hole usually go on a bench grinder. <strong>Cup brush:</strong> works on its face and threads onto an angle grinder, for large flat surfaces. <strong>Bevel brush:</strong> reaches corners and edges on an angle grinder. <strong>Shank-mounted brush:</strong> for drills, in holes and small areas (' + link(PR + 'shaft-mounted-wire-wheels/', 'see shank-mounted brushes') + ').'),
  '<h2>Safety</h2>', SAFETY,
  '<h2>Not sure which one to order?</h2>',
  P('Send a photo on WhatsApp of the brush you already sell or the part to be cleaned, and Frank will tell you the matching model. You can also browse all ' + link('/steel-wire-wheel-brush/', 'steel wire wheel and cup brushes') + '.'),
 ]),

'wire-brush-sizes-and-threads': dict(
 title='Wire Brush Sizes, Threads and Arbor Holes',
 h1='Wire brush sizes: what to send for a quote',
 desc='How to specify diameter, angle grinder thread (M14, M10 or 5/8"-11), bench grinder arbor hole and shank when ordering wire brushes wholesale.',
 body=[
  P('A fast, error-free quote depends on four things: <strong>outside diameter</strong>, <strong>mount</strong> (thread, arbor hole or shank), <strong>wire</strong> and <strong>quantity per size</strong>.'),
  '<h2>1. Outside diameter</h2>',
  P('Some markets order in inches and others in millimetres. Approximate equivalents:'),
  '<table class="guide-table"><thead><tr><th>Inches</th><th>Millimetres (approx.)</th></tr></thead><tbody>'
  + ''.join(f'<tr><td>{a}"</td><td>{b} mm</td></tr>' for a, b in [('3', 75), ('4', 100), ('4.5', 115), ('5', 125), ('6', 150), ('7', 175), ('8', 200), ('10', 250), ('12', 300)])
  + '</tbody></table>',
  P('Each product page lists its available diameters. If the one you need is not shown, ask.'),
  '<h2>2. Mount</h2>',
  P('<strong>Cup and bevel brushes for angle grinders</strong> are threaded. The threads we make most are <strong>M14</strong> (2.0 mm pitch) and <strong>M10</strong>. Note that M10 exists in two pitches, <strong>1.5</strong> (coarse) and <strong>1.25</strong> (fine): many 4-inch grinders use the fine one, and the two do not fit each other. <strong>5/8"-11</strong> is made to order. Check which thread your customers\' grinders use and state it in the order.'),
  P('<strong>Wheel brushes for bench grinders</strong> have an arbor hole. Give the shaft diameter of the grinder; if the hole is larger, bushings or adapters are used and are confirmed with the quote.'),
  P('<strong>Shank-mounted brushes for drills:</strong> give the shank diameter and the head diameter. See ' + link(PR + 'shaft-mounted-wire-wheels/', 'shank-mounted wire brushes') + '.'),
  '<h2>3. Wire</h2>',
  P('State <strong>crimped or knotted</strong> (see ' + link(G + 'knotted-vs-crimped-wire-brush/', 'the difference') + '), the material (carbon steel, copper-coated) and the wire gauge if you have it. For reference, our crimped wheels typically use 0.3 mm wire and the knotted bevel brush 0.5 mm.'),
  '<h2>4. Speed (RPM)</h2>',
  P('The maximum RPM of the brush must be equal to or higher than the machine speed. Frank confirms the RPM of each model before the order.'),
  '<h2>Checklist to send on WhatsApp</h2>',
  '<ul><li>Photo or reference model of the brush</li><li>Outside diameter</li><li>Thread, arbor hole or shank</li><li>Wire: crimped or knotted, material</li><li>Quantity per size</li><li>Packaging: bulk, blister card or colour box, with or without your brand</li><li>Destination country and city</li></ul>',
 ]),

'import-wire-brushes-from-china': dict(
 title='How to Import Wire Brushes from China',
 h1='How to import wire brushes direct from a factory in China',
 desc='Steps to buy wire brushes direct from a Chinese factory: samples, trial order, private label packaging, EXW/FOB/CIF terms and DDP by destination.',
 body=[
  P('If you run a hardware store, a distribution business or your own tool brand, buying wire brushes direct from the factory gives you better margin and control over packaging. This is how we work at YEKAI, a wire brush factory in Yongkang, Zhejiang.'),
  '<h2>1. Define your range</h2>',
  P('Start with the sizes you sell most, for example 3" and 4" cup brushes for angle grinders and wheel brushes for bench grinders. Split the quantity by size and wire style. The ' + link(G + 'wire-brush-sizes-and-threads/', 'sizes guide') + ' lists what to send.'),
  '<h2>2. Ask for samples</h2>',
  P('Before a bulk order we send samples so you can check the wire, the mount and the finish. Samples travel by air; bulk orders by sea.'),
  '<h2>3. Choose the packaging</h2>',
  P('You can order a plain carton, a blister card or a colour box, with your brand. The printing plate costs RMB 300 per design; it is waived on orders of at least 5,000 pieces in total that combine 2 to 4 models on one plate. More in ' + link(G + 'private-label-wire-brushes/', 'private label packaging') + ' and ' + link(PR + 'blister-card-brush-sets/', 'blister card sets') + '.'),
  '<h2>4. Trial order</h2>',
  P('We accept small trial orders in standard packaging. Wholesale pricing does not apply to them and freight per piece is higher, but they let you test the product with your customers.'),
  '<h2>5. Shipping and duties</h2>',
  P('We quote <strong>EXW, FOB or CIF</strong>. If you prefer not to handle the import yourself, we can also quote <strong>DDP</strong> (door to door, duties included), for example to Mexico; it is confirmed by country, product, volume and destination city.'),
  '<h2>6. Payment, lead time and quality control</h2>',
  P('Standard payment is <strong>30% deposit and the balance before shipment</strong>. Production of a bulk order usually takes about 30 days and is confirmed for each order. We check brushes on a balancing tester and sample every batch before dispatch.'),
  '<h2>7. What to send for a quote</h2>',
  '<ul><li>Products and reference photos</li><li>Sizes and mount for each model</li><li>Quantity per model</li><li>Packaging type and whether it carries your brand</li><li>Delivery city and term (EXW, FOB, CIF or DDP)</li></ul>',
  P('With that, Frank prepares the factory quote. You can first see ' + link('/about/', 'the factory') + ' and ' + link('/#documents', 'the documents') + '.'),
 ]),

'wire-brush-for-weld-cleaning': dict(
 title='Wire Brush for Weld Cleaning: Which Type to Use',
 h1='Wire brush for weld cleaning: which type for each job',
 desc='Which wire brush to use for cleaning weld beads, slag and spatter: stringer bead wheel, knotted cup, bevel or end brush. For workshops and resellers.',
 body=[
  P('Weld cleaning is almost always done with a <strong>knotted (twist knot) wire brush</strong>: it is stiffer than a crimped brush and removes slag, spatter and scale without grinding the metal away. What changes from job to job is the <strong>shape</strong>.'),
  '<h2>Weld bead and root pass: stringer bead wheel</h2>',
  P('The ' + link(PR + 'stringer-knotted-wheels/', 'stringer bead knot wheel') + ' has narrow knots that follow the bead and enter tight bevels. Our series is carbon steel, typical wire 0.5 mm, in 4.5, 5, 6 and 7 in. To quote, give the working width and the arbor hole.'),
  '<h2>Plate and wide surfaces: knotted cup brush</h2>',
  P('To clean around the weld on sheet, plate or sections, a cup brush works on its face and covers more area: ' + link(PR + 'red-knotted-wire-cup-brush/', 'knotted wire cup brush') + ' or ' + link(PR + 'banded-twisted-cup-brushes/', 'banded knot cup brush') + ', which keeps the knots tighter.'),
  '<h2>Corners and fillet welds: bevel brush</h2>',
  P('The ' + link(PR + 'twisted-wire-wheels/', 'knotted bevel brush') + ' has angled knots and reaches fillets, corners and edges where a cup does not fit. Series in 4, 4.5 and 5 in, typical wire 0.5 mm.'),
  '<h2>Holes, pipe and small areas: end brush for drills</h2>',
  P('Where the angle grinder does not fit, use a ' + link(PR + 'shaft-mounted-wire-wheels/', 'shank-mounted brush') + '. Knotted end brushes run from 19 to 30 mm head diameter.'),
  '<h2>Hand touch-up</h2>',
  P('Between weld passes or for a quick touch-up, a ' + link(PR + 'plastic-handle-hand-brushes/', 'hand wire brush') + ' does the job.'),
  '<h2>Summary</h2>',
  '<table class="guide-table"><thead><tr><th>Job</th><th>Brush</th></tr></thead><tbody>'
  '<tr><td>Bead, root, bevel</td><td>Stringer bead wheel, 4.5 to 7 in</td></tr>'
  '<tr><td>Plate and surrounding surface</td><td>Knotted cup (with or without band)</td></tr>'
  '<tr><td>Fillet, corner, edge</td><td>Knotted bevel brush, 4 to 5 in</td></tr>'
  '<tr><td>Hole, inside of pipe</td><td>End brush with shank, for drills</td></tr></tbody></table>',
  '<h2>Safety</h2>', SAFETY,
 ]),

'wire-brush-for-rust-and-paint-removal': dict(
 title='Wire Brush for Rust and Paint Removal',
 h1='Wire brush for rust and paint removal: how to choose',
 desc='Which wire brush removes rust, paint and scale from metal: crimped or knotted, cup, wheel or drill brush, and when abrasive nylon is the better choice.',
 body=[
  P('A wire brush removes rust, old paint and dirt <strong>without eating into the metal</strong>, which is why it is used before painting or welding. The choice depends on how stubborn the coating is and on the shape of the part.'),
  '<h2>By how heavy the job is</h2>',
  '<table class="guide-table"><thead><tr><th>Situation</th><th>Wire style</th></tr></thead><tbody>'
  '<tr><td>Surface rust, loose paint, general cleaning</td><td>Crimped: more flexible, more even finish</td></tr>'
  '<tr><td>Thick rust, scale, firmly bonded paint</td><td>Knotted: stiffer and more aggressive</td></tr>'
  '<tr><td>Parts that must not be scratched, fine finish</td><td>Abrasive nylon instead of wire</td></tr></tbody></table>',
  P('The full difference is in ' + link(G + 'knotted-vs-crimped-wire-brush/', 'knotted vs crimped wire brush') + '.'),
  '<h2>By the shape of the part</h2>',
  P('<strong>Large flat surfaces</strong> (sheet, gates, structures): a cup brush on the angle grinder. Crimped: ' + link(PR + 'crimped-wire-cup-brushes/', 'crimped wire cup brush') + ', 2.5 to 6 in. Knotted: ' + link(PR + 'red-knotted-wire-cup-brush/', 'knotted wire cup brush') + '.'),
  P('<strong>Loose parts on a bench grinder</strong> (tools, fasteners, components): ' + link(PR + 'wide-crimped-wire-wheels/', 'wide-face crimped wire wheel') + ', 4 to 12 in, or ' + link(PR + 'copper-coated-wire-wheels/', 'copper-coated wire wheel') + '.'),
  P('<strong>Corners and edges</strong>: ' + link(PR + 'twisted-wire-wheels/', 'knotted bevel brush') + '.'),
  P('<strong>Holes, railings and small areas</strong>: ' + link(PR + 'shaft-mounted-wire-wheels/', 'shank-mounted wire brushes for drills') + ' (end, wheel and cup shapes).'),
  P('<strong>Hand touch-ups</strong>: ' + link(PR + 'plastic-handle-hand-brushes/', 'hand wire brush') + '.'),
  '<h2>When to use abrasive nylon or a flap disc</h2>',
  P('If the part must not be scratched, an ' + link(PR + 'abrasive-filament-brushes/', 'abrasive nylon brush') + ' removes rust, corrosion, paint and primer with less marking. If you also need to remove material or blend a weld, that is a job for a ' + link(PR + 'abrasive-flap-discs/', 'flap disc') + ', not a wire brush.'),
  '<h2>For resellers: what to stock first</h2>',
  P('Rust and paint jobs are covered by a few items: a crimped cup and a knotted cup for angle grinders, a wheel brush for bench grinders and a shank-mounted set for drills. They can be supplied ' + link(PR + 'blister-card-brush-sets/', 'on blister cards') + ' for peg displays.'),
  '<h2>Safety</h2>', SAFETY,
 ]),

'wire-weed-brush-for-brush-cutter': dict(
 title='Wire Weed Brush for Brush Cutters: How to Choose',
 h1='Wire weed brush for brush cutters and trimmers: types and how to choose',
 desc='Steel wire and nylon weed brushes for brush cutters and grass trimmers: clearing weeds from paving joints. Diameters, knot counts, bore sizes and fit.',
 body=[
  P('A weed brush (wire trimmer head) replaces the line or blade on a <strong>brush cutter or grass trimmer</strong> to <strong>remove weeds and moss from paving joints, kerbs, pavements and concrete floors</strong> without herbicide. There are three families in our catalog.'),
  '<h2>1. Twisted (knotted) wire weed brush</h2>',
  P('The most aggressive: knots of twisted carbon steel wire, 0.5 mm. The ' + link(PR + 'twisted-wire-grass-trimmer-heads/', 'twisted wire series') + ' is listed in 6 in with 24 or 30 knots and 8 in with 30 or 36 knots. More knots means a denser brush.'),
  '<h2>2. 3 or 6 bundle head</h2>',
  P('The ' + link(PR + '3-and-6-bundle-wire-trimmer-heads/', '3 and 6 bundle heads') + ' come in 150, 180, 200 and 230 mm. There are two versions by machine: <strong>5.5 mm bore for battery (cordless) trimmers</strong> and <strong>25.4 mm bore for petrol brush cutters</strong>.'),
  '<h2>3. Nylon weed brush</h2>',
  P('The ' + link(PR + 'nylon-grass-trimmer-brushes/', 'nylon trimmer brush') + ' uses rectangular nylon filament, in 6 and 8 in, with a 22.5 mm reference bore. Choose it when the surface is more delicate and should not be scratched by steel.'),
  '<h2>Comparison</h2>',
  '<table class="guide-table"><thead><tr><th>Type</th><th>Listed sizes</th><th>Best for</th></tr></thead><tbody>'
  '<tr><td>Twisted wire</td><td>6" (24 or 30 knots), 8" (30 or 36 knots)</td><td>Tough weeds on concrete and hard paving</td></tr>'
  '<tr><td>3 or 6 bundles</td><td>150, 180, 200, 230 mm</td><td>Battery (5.5 mm bore) or petrol (25.4 mm bore)</td></tr>'
  '<tr><td>Nylon</td><td>6" and 8", 22.5 mm bore</td><td>Surfaces that must not be scratched</td></tr></tbody></table>',
  '<h2>Fit is what causes most returns</h2>',
  P('There is no universal fit. Before ordering, send the <strong>make and model of the machine</strong>, the <strong>bore or shaft diameter</strong> and, if you can, a photo of the current head. Frank confirms the head, the adapter and the safe RPM for that model.'),
  '<h2>Safety</h2>',
  P('A steel brush throws stones and can shed wires: work with the guard fitted, a face shield, long trousers and closed footwear, and keep people away. On paving that scratches easily, test a hidden spot first or use nylon.'),
  '<h2>For distributors</h2>',
  P('This is a seasonal product for the growing season and for municipal and garden maintenance. It can be supplied under your brand in individual packaging; see ' + link(G + 'private-label-wire-brushes/', 'how private label packaging works') + ' or the ' + link('/wire-grass-trimmer-head/', 'wire trimmer head category') + '.'),
 ]),

'abrasive-nylon-brush': dict(
 title='Abrasive Nylon Brush: Uses, Grit and Shapes',
 h1='Abrasive nylon brush: what it is for and which grit to choose',
 desc='What an abrasive nylon (filament) brush is used for, how it differs from a wire brush, grit 80 to 320, and aluminium oxide vs silicon carbide.',
 body=[
  P('An <strong>abrasive nylon brush</strong> (abrasive filament brush) has nylon bristles with abrasive grain mixed through the whole filament. As it wears it exposes fresh grain, so the finish stays consistent.'),
  '<h2>What it is used for</h2>',
  P('Our catalog lists it for <strong>removing rust, corrosion, paint and primer and for surface cleaning</strong>. Compared with a wire brush it marks the part less and leaves no steel residue. It is also used on wood to clean and raise the grain; in that case confirm the grit with a sample.'),
  '<h2>Abrasive nylon or wire brush</h2>',
  '<table class="guide-table"><thead><tr><th></th><th>Abrasive nylon</th><th>Wire brush</th></tr></thead><tbody>'
  '<tr><th>Action</th><td>Gentler, more even</td><td>More aggressive</td></tr>'
  '<tr><th>Marking on the part</th><td>Less</td><td>More</td></tr>'
  '<tr><th>Typical job</th><td>Finishing, fine cleaning, delicate parts</td><td>Heavy rust, slag, welds</td></tr></tbody></table>',
  '<h2>Shapes and sizes in the catalog</h2>',
  '<ul><li><strong>Wheel:</strong> 75 to 200 mm</li><li><strong>Cup:</strong> 75 to 125 mm</li><li><strong>Shank-mounted wheel:</strong> 38 to 100 mm</li><li><strong>Shank-mounted cup:</strong> 40 to 80 mm</li></ul>',
  P('The listed shank-mounted models have a 6 mm shank, for drills. Arbor holes and threads on cups are confirmed with Frank. See all models in ' + link(PR + 'abrasive-filament-brushes/', 'abrasive nylon filament brushes') + '.'),
  '<h2>Which grit to choose</h2>',
  P('The catalog covers grit <strong>80 to 320</strong>. Lower number: more aggressive, faster removal. Higher number: finer finish. <strong>Grit 80 is the most ordered</strong> for general cleaning and for wood; 120 leaves a slightly finer finish, and 240 or 320 are used for finishing.'),
  '<h2>Aluminium oxide (AO) or silicon carbide (SiC)</h2>',
  P('The catalog offers both depending on the model. Note: <strong>brush colour alone does not identify the abrasive or the grit</strong>; always ask for it in writing for the model you choose.'),
  '<h2>What to send for a quote</h2>',
  '<ul><li>Part material (steel, aluminium, wood…) and the finish you want</li><li>Machine: angle grinder, drill, bench grinder</li><li>Shape and diameter</li><li>Grit and abrasive, if already defined</li><li>Quantity per model</li></ul>',
 ]),

'private-label-wire-brushes': dict(
 title='Private Label Wire Brushes: OEM Packaging',
 h1='Private label wire brushes: how OEM packaging works',
 desc='How to order wire brushes under your own brand: blister card, colour box, printing plate cost and the 5,000-piece order that waives it.',
 body=[
  P('If you run a hardware store, a distribution business or your own tool brand, you can order wire brushes <strong>with your logo and your packaging</strong> direct from the factory. This is how an order is put together at YEKAI.'),
  '<h2>Packaging types</h2>',
  '<ul><li><strong>Blister card</strong> (single or double blister): for peg displays</li><li><strong>Colour box</strong>: for shelves and single-piece retail</li><li><strong>Plain carton</strong>: for wholesale and industrial use</li></ul>',
  P('We also assemble ' + link(PR + 'blister-card-brush-sets/', 'wire brush sets on blister cards') + ': you define the models and the pieces per card.'),
  '<h2>Printing plate cost</h2>',
  P('Custom printing carries a charge of <strong>RMB 300 per plate</strong> (per design). The charge <strong>is waived</strong> on orders of at least <strong>5,000 pieces in total</strong> that combine 2 to 4 models on one printing plate.'),
  '<h2>Trial order</h2>',
  P('If you want to test the product first, we accept small orders in standard, non-customised packaging. Wholesale pricing does not apply to them and freight per piece is higher.'),
  '<h2>Step by step</h2>',
  '<ol><li>Choose models and sizes (' + link(G + 'wire-brush-sizes-and-threads/', 'what sizes to send') + ').</li><li>Ask for samples to check wire, mount and finish.</li><li>Send your artwork: vector logo, texts, barcode and any importer details the label must carry in your country.</li><li>You approve the design and the split by model before production.</li><li>Production and shipping on EXW, FOB or CIF; DDP quoted by country.</li></ol>',
  '<h2>What to send for a quote</h2>',
  '<ul><li>Models, sizes and quantity per model</li><li>Packaging type and pieces per pack</li><li>Whether you have a design or need one adapted</li><li>Destination country and city</li></ul>',
  P('More on shipping in ' + link(G + 'import-wire-brushes-from-china/', 'how to import wire brushes from China') + '. Photos of finished packaging in ' + link('/#oem', 'OEM packaging') + '.'),
 ]),
}

FAQ_EN = {
'knotted-vs-crimped-wire-brush': [
 ('Which is more aggressive, a knotted or a crimped wire brush?', 'Knotted. The twisted knots make it stiffer; a crimped brush is more flexible and leaves a more even finish.'),
 ('Which wire brush goes on an angle grinder?', 'Cup and bevel brushes, which are threaded. Wheel brushes with an arbor hole usually go on a bench grinder.'),
 ('Is a twist knot brush the same as a knotted brush?', 'Yes. Knotted, twist knot and twisted wire brush are names for the same construction.'),
],
'wire-brush-sizes-and-threads': [
 ('What thread does a wire cup brush for an angle grinder have?', 'The ones we make most are M14 and M10 (pitch 1.5 or 1.25; they are not interchangeable). 5/8"-11 is made to order. Confirm before ordering.'),
 ('How many millimetres is a 4.5 inch wire brush?', 'About 115 mm. Others: 4" = 100 mm, 5" = 125 mm, 6" = 150 mm, 7" = 175 mm.'),
 ('What do I need to send for a wholesale wire brush quote?', 'Outside diameter, mount (thread, arbor hole or shank), wire style, quantity per size, packaging and destination.'),
],
'import-wire-brushes-from-china': [
 ('Can I get samples before a bulk order?', 'Yes. Samples are sent by air so you can check wire, mount and finish before the wholesale order.'),
 ('What does DDP mean?', 'Door-to-door delivery with import duties included. It is quoted by country, product, volume and destination city.'),
 ('Do you accept small orders?', 'Yes, trial orders in standard packaging. Wholesale pricing does not apply and freight per piece is higher.'),
],
'wire-brush-for-weld-cleaning': [
 ('What wire brush is used to clean welds?', 'A knotted wire brush. A stringer bead wheel for the bead, a knotted cup for the surrounding surface and a bevel brush for corners.'),
 ('Can a crimped wire brush clean welds?', 'For light cleaning, yes, but for slag and spatter a knotted brush works better because it is stiffer.'),
 ('What sizes do stringer bead wheels come in?', 'In our series: 4.5, 5, 6 and 7 in, typical wire 0.5 mm carbon steel.'),
],
'wire-brush-for-rust-and-paint-removal': [
 ('What is the best wire brush for removing rust?', 'Light rust: crimped. Thick rust or scale: knotted. On flat surfaces use a cup brush on an angle grinder.'),
 ('Does a wire brush scratch metal?', 'It leaves marks, knotted more than crimped. If the part must not be scratched, use an abrasive nylon brush.'),
 ('Which wire brush do I use with a drill?', 'A shank-mounted brush: an end brush for holes, a wheel for edges or a cup for open surfaces.'),
],
'wire-weed-brush-for-brush-cutter': [
 ('What is a wire weed brush for a brush cutter used for?', 'For removing weeds and moss from paving joints, pavements and concrete floors, without herbicide.'),
 ('Does it fit any brush cutter?', 'There is no universal fit. On 3 and 6 bundle heads, the 5.5 mm bore is for battery trimmers and the 25.4 mm bore for petrol brush cutters. Confirm make, model and bore before ordering.'),
 ('Steel wire or nylon?', 'Twisted steel wire for tough weeds on hard surfaces; nylon when the surface must not be scratched.'),
],
'abrasive-nylon-brush': [
 ('What is an abrasive nylon brush used for?', 'For removing rust, corrosion, paint and primer and cleaning surfaces, with less marking than a wire brush.'),
 ('Which grit should I choose?', 'The catalog runs from 80 to 320. Grit 80 is the most ordered. Lower is more aggressive; higher gives a finer finish.'),
 ('Does the colour show the grit?', 'No. Colour alone does not identify the abrasive or the grit; confirm it for each model.'),
],
'private-label-wire-brushes': [
 ('How much does it cost to put my brand on the packaging?', 'RMB 300 per printing plate. It is waived on orders of at least 5,000 pieces in total with 2 to 4 models on one plate.'),
 ('Can I order fewer than 5,000 pieces?', 'Yes. With custom printing the plate is charged; trial orders in standard packaging are also possible.'),
 ('What packaging do you offer?', 'Blister card, double blister, colour box and plain carton.'),
],
}

# English titles / H1 / descriptions for existing pages: path -> (title without " | YEKAI", h1 or None, description or None)
EN = {
 '': ('Wire Brush Manufacturer in China | Wholesale & OEM', None,
      'Wire cup brushes, wire wheels and weed brushes direct from our Yongkang factory. Knotted and crimped styles, private label. Ask Frank for a quote.'),
 'steel-wire-wheel-brush': ('Wire Wheel and Cup Brushes for Grinders | Wholesale',
      'Wire wheel and cup brushes: knotted and crimped styles',
      'Compare wire cup brushes for angle grinders and wire wheels for bench grinders: knotted or crimped, by diameter, thread and arbor hole. Get a quote.'),
 'abrasive-filament-brush': ('Abrasive Nylon Filament Brushes | Wholesale & OEM',
      'Abrasive nylon filament brushes for surface finishing', None),
 'abrasive-flap-disc': ('Flap Discs for Angle Grinders | Wholesale Supplier', None, None),
 'wire-grass-trimmer-head': ('Wire Weed Brushes for Brush Cutters | Wholesale',
      'Wire weed brushes and trimmer heads for brush cutters',
      'Steel wire and nylon weed brushes for brush cutters and grass trimmers. Compare diameter, knot count and bore, and ask Frank to confirm machine fit.'),
 'products/twisted-wire-wheels': ('Knotted Bevel Wire Brush for Angle Grinders',
      'Knotted bevel wire brush',
      'Knotted bevel wire brush with angled carbon steel knots for angle grinders, 4, 4.5 or 5 in. Typical wire: 0.5 mm. Ask Frank to confirm wire and thread.'),
 'products/copper-coated-wire-wheels': ('Copper-Coated Wire Wheel Brush | Wholesale & OEM', None, None),
 'products/banded-twisted-cup-brushes': ('Banded Knot Wire Cup Brush for Angle Grinders',
      'Banded knot wire cup brush',
      'Banded knot wire cup brush for angle grinders, carbon steel twist knots, 2.5, 3, 3.5, 4 or 5 in. Ask Frank to confirm the spindle thread for your order.'),
 'products/crimped-wire-brush-wheels': ('Crimped Wire Wheel Brush with Metal Hub | Wholesale', None, None),
 'products/crimped-wire-cup-brushes': ('Crimped Wire Cup Brush for Angle Grinders', None,
      'Crimped wire cup brush for angle grinders and broad metal surfaces, 2.5, 3, 4, 5 or 6 in. Ask Frank to confirm wire material and thread for your size.'),
 'products/red-knotted-wire-cup-brush': ('Knotted Wire Cup Brush for Angle Grinders', None,
      'Knotted (twist knot) wire cup brush for angle grinders, carbon steel, 2.5, 3, 4, 5 or 6 in. Ask Frank to confirm cup diameter and spindle thread.'),
 'products/shaft-mounted-wire-wheels': ('Shank-Mounted Wire Brushes for Drills | Wholesale',
      'Shank-mounted wire brushes for drills',
      'Shank-mounted wire brushes for drills: end, wheel and cup shapes. Ask Frank to match head shape, head diameter and shank diameter to the item you stock.'),
 'products/stringer-knotted-wheels': ('Stringer Bead Wire Wheel for Weld Cleaning',
      'Stringer bead knot wire wheel',
      'Stringer bead knot wire wheel for weld cleaning, carbon steel, 4.5, 5, 6 or 7 in. Ask Frank to confirm working width and arbor hole.'),
 'products/wide-crimped-wire-wheels': ('Crimped Wire Wheel for Bench Grinders | Wholesale',
      'Wide-face crimped wire wheel for bench grinders',
      'Wide-face crimped wire wheel for bench grinders, 4, 5, 6, 7, 8, 10 or 12 in. Typical wire: 0.3 mm. Ask Frank to confirm face width and arbor hole.'),
 'products/plastic-handle-hand-brushes': ('Hand Wire Brushes with Plastic Handle | Wholesale',
      'Hand wire brushes with plastic handle', None),
 'products/blister-card-brush-sets': ('Wire Brush Sets on Blister Cards | Wholesale & OEM',
      'Wire brush sets on blister cards',
      'Wire brush sets on blister cards for hardware retail. Send brush models, pieces per card and packaging artwork, and ask Frank for a quote.'),
 'products/abrasive-filament-brushes': ('Abrasive Nylon Filament Brushes | Wheel, Cup, Shank',
      'Abrasive nylon filament brushes', None),
 'products/abrasive-flap-discs': ('Abrasive Flap Discs for Metal | Wholesale & OEM', None, None),
 'products/twisted-wire-grass-trimmer-heads': ('Twisted Wire Trimmer Heads for Brush Cutters', None,
      'Twisted wire trimmer heads (weed brushes) for brush cutters: 6 in with 24 or 30 knots; 8 in with 30 or 36. Ask Frank to confirm machine fit and mount.'),
 'products/3-and-6-bundle-wire-trimmer-heads': ('3 and 6 Bundle Wire Trimmer Heads | Wholesale', None,
      '3 and 6 bundle wire trimmer heads, 150, 180, 200 or 230 mm. 5.5 mm bore for battery trimmers, 25.4 mm bore for petrol brush cutters.'),
 'products/nylon-grass-trimmer-brushes': ('Nylon Weed Brushes for Grass Trimmers | Wholesale', None, None),
}

# English product names used on cards and links -> same wording as the new H1
RENAME_EN = {
 'Twisted wire wheels': 'Knotted bevel wire brush',
 'Banded twisted cup brushes': 'Banded knot wire cup brush',
 'Shaft-mounted wire wheels': 'Shank-mounted wire brushes for drills',
 'Stringer knotted wheels': 'Stringer bead knot wire wheel',
 'Wide crimped wire wheels': 'Wide-face crimped wire wheel for bench grinders',
 'Plastic-handle hand brushes': 'Hand wire brushes with plastic handle',
 'Blister-card brush sets': 'Wire brush sets on blister cards',
 'Abrasive filament brushes': 'Abrasive nylon filament brushes',
}

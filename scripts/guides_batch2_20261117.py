"""2026-11-17 — second batch of buyer guides: 9 EN/ES pairs + 1 English-only guide for India.
Facts confirmed by Frank on 2026-11-17: wire materials (carbon steel, copper-coated steel, stainless 201/304, brass),
balancing tester + batch sampling, M10 thread pitches (1.5 and 1.25), M14x2, India demand (cup brushes, abrasive
nylon, flat wheels; 3 and 4 inch), three flat wheel families (arbor-hole, bench with bushings, knotted).
Imported by scripts/seo_mx_20261116.py.
"""
P = lambda s: f'<p>{s}</p>'
def link(path, label): return f'<a href="{path}">{label}</a>'
E = '/products/'; S = '/es/products/'; GE = '/guides/'; GS = '/es/guias/'

PAIR2 = {
 'carda-copa-para-pulidora': 'wire-cup-brush-for-angle-grinder',
 'carda-para-esmeril-de-banco': 'wire-wheel-for-bench-grinder',
 'carda-para-taladro': 'wire-brush-for-drill',
 'cepillo-para-madera': 'wire-brush-for-wood',
 'carda-para-acero-inoxidable-y-aluminio': 'wire-brush-for-stainless-steel-and-aluminium',
 'carda-o-disco-flap': 'wire-brush-vs-flap-disc',
 'surtido-de-cardas-para-ferreteria': 'wire-brushes-for-hardware-stores',
 'calidad-de-cardas': 'wire-brush-quality-checklist',
 'seguridad-y-rpm-de-cardas': 'wire-brush-safety-and-rpm',
}
GUIDES_EN2 = [
 ('wire-cup-brush-for-angle-grinder', 'How to choose a wire cup brush for an angle grinder'),
 ('wire-wheel-for-bench-grinder', 'How to choose a wire wheel for a bench grinder'),
 ('wire-brush-for-drill', 'Wire brushes for drills: end, wheel and cup'),
 ('wire-brush-for-wood', 'Wire brushes for wood texturing and distressing'),
 ('wire-brush-for-stainless-steel-and-aluminium', 'Wire brushes for stainless steel and aluminium'),
 ('wire-brush-vs-flap-disc', 'Wire brush vs flap disc: which to use'),
 ('wire-brushes-for-hardware-stores', 'How to stock wire brushes for a hardware store'),
 ('wire-brush-quality-checklist', 'How to identify a good quality wire brush'),
 ('wire-brush-safety-and-rpm', 'Wire brush safety: RPM, wire loss and proper use'),
 ('wire-brushes-india-m10', 'Wire brushes for 4-inch angle grinders in India: M10 guide'),
]
GUIDES_ES2 = [
 ('carda-copa-para-pulidora', 'Cómo elegir carda copa para pulidora'),
 ('carda-para-esmeril-de-banco', 'Cómo elegir carda para esmeril de banco'),
 ('carda-para-taladro', 'Cardas para taladro: de punta, circular y copa'),
 ('cepillo-para-madera', 'Cepillos para texturizar y envejecer madera'),
 ('carda-para-acero-inoxidable-y-aluminio', 'Cardas para acero inoxidable y aluminio'),
 ('carda-o-disco-flap', '¿Carda o disco flap? Cuál usar'),
 ('surtido-de-cardas-para-ferreteria', 'Qué cardas surtir en una ferretería'),
 ('calidad-de-cardas', 'Cómo reconocer una carda de buena calidad'),
 ('seguridad-y-rpm-de-cardas', 'Seguridad con cardas: RPM y desprendimiento de alambre'),
]

SAFE_EN = P('The maximum RPM marked on the brush must be equal to or higher than the machine speed. Use the guard, eye protection and gloves, and ask Frank to confirm the RPM of the model you choose.')
SAFE_ES = P('Las RPM máximas marcadas en la carda deben ser iguales o mayores que las de la máquina. Usa guarda, lentes y guantes, y confirma con Frank las RPM del modelo que elijas.')
THREAD_EN = P('<strong>Check the thread pitch, not only the diameter.</strong> M14 spindles use a 2.0 mm pitch. M10 exists in two pitches: <strong>M10 × 1.5</strong> (coarse) and <strong>M10 × 1.25</strong> (fine), and many 4-inch grinders use the fine one. The two do not fit each other at all. 5/8"-11 is made to order.')
THREAD_ES = P('<strong>Revisa el paso de la rosca, no sólo el diámetro.</strong> La rosca M14 lleva paso de 2.0 mm. La M10 existe en dos pasos: <strong>M10 × 1.5</strong> (gruesa) y <strong>M10 × 1.25</strong> (fina), y muchas pulidoras de 4 pulgadas usan la fina. Una no entra en la otra. La 5/8"-11 se fabrica sobre pedido.')

CONTENT_EN2 = {
'wire-cup-brush-for-angle-grinder': dict(
 title='How to Choose a Wire Cup Brush for an Angle Grinder',
 h1='How to choose a wire cup brush for an angle grinder',
 desc='Choose a wire cup brush by grinder size, thread (M10 x 1.5, M10 x 1.25, M14) and wire style: crimped for light cleaning, knotted for heavy rust and welds.',
 body=[
  P('A wire cup brush works on its face, so it is the fastest way to clean large flat surfaces with an angle grinder. Three things decide the right one: <strong>cup diameter</strong>, <strong>thread</strong> and <strong>wire style</strong>.'),
  '<h2>1. Match the cup to the grinder</h2>',
  '<table class="guide-table"><thead><tr><th>Grinder size</th><th>Typical cup brush</th><th>Typical thread</th></tr></thead><tbody>'
  '<tr><td>100 mm (4")</td><td>65 to 75 mm (2.5" to 3")</td><td>M10</td></tr>'
  '<tr><td>115 to 125 mm (4.5" to 5")</td><td>75 to 100 mm (3" to 4")</td><td>M14</td></tr>'
  '<tr><td>180 to 230 mm (7" to 9")</td><td>125 to 150 mm (5" to 6")</td><td>M14</td></tr></tbody></table>',
  P('These are typical pairings, not a rule: the brush must clear the guard and its maximum RPM must cover the grinder speed.'),
  '<h2>2. Get the thread right</h2>', THREAD_EN,
  '<h2>3. Crimped or knotted</h2>',
  P('<strong>Crimped:</strong> flexible, for surface rust, loose paint and general cleaning: ' + link(E + 'crimped-wire-cup-brushes/', 'crimped wire cup brush') + ', 2.5 to 6 in. <strong>Knotted:</strong> stiff and aggressive, for thick rust, scale and welds: ' + link(E + 'red-knotted-wire-cup-brush/', 'knotted wire cup brush') + ', or the ' + link(E + 'banded-twisted-cup-brushes/', 'banded knot cup') + ' when you want the knots held tighter. More in ' + link(GE + 'knotted-vs-crimped-wire-brush/', 'knotted vs crimped') + '.'),
  '<h2>4. Wire material</h2>',
  P('Carbon steel is the standard for steel and iron. For stainless steel or aluminium use stainless wire; see ' + link(GE + 'wire-brush-for-stainless-steel-and-aluminium/', 'wire brushes for stainless steel and aluminium') + '.'),
  '<h2>Tips for use</h2>',
  '<ul><li>Use light pressure and let the wire tips do the work; pressing harder bends the wire and shortens brush life.</li><li>Run a new brush for about a minute inside the guard before the first job.</li><li>Keep the cup face flat or slightly tilted on the surface; do not dig in with the edge.</li><li>Replace the brush when the wire is worn short or it starts to vibrate.</li></ul>',
  '<h2>Safety</h2>', SAFE_EN,
 ]),
'wire-wheel-for-bench-grinder': dict(
 title='How to Choose a Wire Wheel for a Bench Grinder',
 h1='How to choose a wire wheel for a bench grinder',
 desc='Three types of flat wire wheel for bench grinders: arbor-hole crimped wheel, thick bench wheel with reducing bushings and knotted wheel. Sizes and fit.',
 body=[
  P('A bench grinder wire wheel works on its edge and cleans loose parts held against it: tools, fasteners, castings. There are three families, and they are not priced or built the same.'),
  '<h2>The three types</h2>',
  '<table class="guide-table"><thead><tr><th>Type</th><th>Build</th><th>Use</th></tr></thead><tbody>'
  '<tr><td>Arbor-hole crimped wheel</td><td>Thinner, plain metal hub</td><td>Economical general cleaning</td></tr>'
  '<tr><td>Bench wheel with reducing bushings</td><td>Thicker face, more wire, stepped bushings in the hub</td><td>Mostly bench grinders; costs more than the arbor-hole type</td></tr>'
  '<tr><td>Knotted wheel</td><td>Twisted knots, stiff</td><td>Heavy rust, scale, welds</td></tr></tbody></table>',
  P('The ' + link(E + 'wide-crimped-wire-wheels/', 'arbor-hole crimped wheel') + ' and the ' + link(E + 'wide-crimped-wire-wheels/#bench-version', 'bench version with bushings') + ' come in the same diameters, 4 to 12 in, with 0.3 mm typical wire. For knotted wheels see the ' + link(E + 'stringer-knotted-wheels/', 'stringer bead knot wheel') + ' (4.5 to 7 in).'),
  '<h2>Diameter</h2>',
  P('Use the wheel diameter the grinder is built for: a 6-inch grinder takes a 6-inch (150 mm) wheel, an 8-inch grinder an 8-inch (200 mm) wheel. Never fit a larger wheel than the guard allows.'),
  '<h2>Arbor hole and bushings</h2>',
  P('Give the shaft diameter of the grinder. Bench wheels with reducing bushings fit several shaft sizes with one wheel, which is why resellers like them: fewer references to stock. Confirm the bushing sizes with Frank for your market.'),
  '<h2>Wire</h2>',
  P('Crimped carbon steel or copper-coated steel for general work; stainless steel wire for stainless parts; brass wire for softer metals. Typical wire in our bench series is 0.3 mm.'),
  '<h2>Tips for use</h2>',
  '<ul><li>Use light pressure and let the wire tips do the work; pressing harder bends the wire and shortens brush life.</li><li>Run a new brush for about a minute inside the guard before the first job.</li><li>Hold the part below the centre line of the wheel and set the tool rest close to it. Turn the wheel around from time to time so the wire wears evenly.</li><li>Replace the brush when the wire is worn short or it starts to vibrate.</li></ul>',
  '<h2>Safety</h2>', SAFE_EN,
 ]),
'wire-brush-for-drill': dict(
 title='Wire Brushes for Drills: End, Wheel and Cup Brushes',
 h1='Wire brushes for drills: end brushes, wheel brushes and cup brushes',
 desc='Which shank-mounted wire brush to use in a drill: end brush for holes, wheel brush for edges, cup brush for flat areas. Shank, head size and wire style.',
 body=[
  P('A shank-mounted wire brush fits a drill chuck and reaches places an angle grinder cannot. The three shapes do different jobs.'),
  '<table class="guide-table"><thead><tr><th>Shape</th><th>Works on</th><th>Typical job</th></tr></thead><tbody>'
  '<tr><td>End brush</td><td>The tip</td><td>Holes, inside pipe, corners, weld roots</td></tr>'
  '<tr><td>Wheel brush</td><td>The edge</td><td>Edges, grooves, threads, narrow slots</td></tr>'
  '<tr><td>Cup brush</td><td>The face</td><td>Small flat areas, brackets, railings</td></tr></tbody></table>',
  P('All three are in our ' + link(E + 'shaft-mounted-wire-wheels/', 'shank-mounted wire brushes for drills') + '. Knotted end brushes run from 19 to 30 mm head diameter.'),
  '<h2>What to specify</h2>',
  '<ul><li><strong>Shank diameter:</strong> it must fit the chuck; state it in the order.</li><li><strong>Head diameter</strong> and shape.</li><li><strong>Wire style:</strong> crimped for general cleaning, knotted for heavy rust and welds.</li><li><strong>Wire material:</strong> carbon steel, copper-coated steel, stainless steel or brass.</li></ul>',
  '<h2>If the part must not be scratched</h2>',
  P('Use a shank-mounted ' + link(E + 'abrasive-filament-brushes/', 'abrasive nylon brush') + ' instead: the listed shank-mounted models have a 6 mm shank and come in grit 80 to 320.'),
  '<h2>For resellers</h2>',
  P('Drill brushes sell well as sets. We pack them ' + link(E + 'blister-card-brush-sets/', 'on blister cards') + ' with the models and pieces per card you choose.'),
  '<h2>Safety</h2>', SAFE_EN,
 ]),
'wire-brush-for-wood': dict(
 title='Wire Brushes for Wood Texturing and Distressing',
 h1='Wire brushes for wood texturing and distressing',
 desc='How to texture and distress wood with wire and abrasive nylon brushes: steel wire to open the grain, grit 80 nylon to clean and finish. For furniture.',
 body=[
  P('Brushing wood removes the soft early grain and leaves the hard grain standing, which gives the textured, aged look used in furniture, beams and flooring. It is usually done in two steps.'),
  '<h2>Step 1: open the grain with wire</h2>',
  P('A crimped steel wire brush cuts the soft grain quickly. Work <strong>along the grain</strong>, with light pressure, and test on an offcut first. Use a ' + link(E + 'crimped-wire-cup-brushes/', 'crimped wire cup brush') + ' on an angle grinder for boards, or a ' + link(E + 'wide-crimped-wire-wheels/', 'wide-face crimped wheel') + ' on a bench machine for small parts. Knotted brushes are usually too aggressive for wood.'),
  '<h2>Step 2: clean and finish with abrasive nylon</h2>',
  P('An ' + link(E + 'abrasive-filament-brushes/', 'abrasive nylon brush') + ' removes the fibres the wire leaves behind and smooths the surface without flattening the texture. <strong>Grit 80 is the most ordered</strong>; 120 gives a slightly finer finish. The catalog covers grit 80 to 320.'),
  '<h2>Which to choose</h2>',
  '<table class="guide-table"><thead><tr><th>Goal</th><th>Brush</th></tr></thead><tbody>'
  '<tr><td>Deep texture on softwood</td><td>Crimped steel wire, then nylon grit 80</td></tr>'
  '<tr><td>Light texture, hardwood</td><td>Abrasive nylon grit 80 only</td></tr>'
  '<tr><td>Cleaning before stain or oil</td><td>Abrasive nylon grit 120 or finer</td></tr></tbody></table>',
  '<h2>Shapes for furniture workshops</h2>',
  P('Abrasive nylon comes as wheel (75 to 200 mm), cup (75 to 125 mm) and shank-mounted models for drills. Colour alone does not identify the grit; confirm it for each model. More in ' + link(GE + 'abrasive-nylon-brush/', 'abrasive nylon brush: uses and grit') + '.'),
  '<h2>Ask for samples</h2>',
  P('Wood species react differently, so test before a bulk order. Tell Frank the wood, the machine and the look you want, and ask for sample brushes in two grits.'),
 ]),
'wire-brush-for-stainless-steel-and-aluminium': dict(
 title='Wire Brushes for Stainless Steel and Aluminium',
 h1='Wire brushes for stainless steel and aluminium: which wire to use',
 desc='Why carbon steel wire stains stainless steel, and which wire to use instead: stainless 304 or 201, brass, or abrasive nylon. Wire materials compared.',
 body=[
  P('The wire material matters as much as the shape. The wrong wire can leave rust marks on a part that should never rust.'),
  '<h2>Why not carbon steel on stainless</h2>',
  P('A carbon steel brush leaves tiny steel particles on the surface. On stainless steel or aluminium these particles rust and stain the part later, sometimes days after the job. The same happens with a stainless brush that was used on ordinary steel before: keep separate brushes.'),
  '<h2>Wire materials we make</h2>',
  '<table class="guide-table"><thead><tr><th>Wire</th><th>Use it for</th></tr></thead><tbody>'
  '<tr><td>Carbon steel</td><td>Steel and iron: rust, scale, paint, welds</td></tr>'
  '<tr><td>Copper-coated steel</td><td>Same uses as carbon steel; the coating protects the wire in storage. It is still steel, so not for stainless</td></tr>'
  '<tr><td>Stainless steel 304</td><td>Stainless steel and aluminium parts</td></tr>'
  '<tr><td>Stainless steel 201</td><td>A lower-cost stainless option; confirm suitability for your application</td></tr>'
  '<tr><td>Brass</td><td>Softer than steel: for softer metals and a gentler action</td></tr></tbody></table>',
  P('Copper-coated wire and brass wire look alike but are not the same product. State which one you need.'),
  '<h2>When to use abrasive nylon instead</h2>',
  P('For a fine, even finish on stainless or aluminium with no metal contact at all, use an ' + link(E + 'abrasive-filament-brushes/', 'abrasive nylon brush') + '.'),
  '<h2>How to order</h2>',
  P('Wire material is confirmed per model. Choose the shape first (' + link(E + 'red-knotted-wire-cup-brush/', 'cup') + ', ' + link(E + 'wide-crimped-wire-wheels/', 'wheel') + ', ' + link(E + 'shaft-mounted-wire-wheels/', 'shank-mounted') + '), then tell Frank the workpiece material and he will confirm the wire.'),
 ]),
'wire-brush-vs-flap-disc': dict(
 title='Wire Brush vs Flap Disc: Which One to Use',
 h1='Wire brush vs flap disc: which one should you use?',
 desc='A wire brush cleans without removing base metal; a flap disc grinds and blends. When to use each on rust, paint, welds and edges, and when to use both.',
 body=[
  P('Both go on an angle grinder and both are used on metal, but they do opposite jobs. A <strong>wire brush cleans</strong> what sits on the surface. A <strong>flap disc removes</strong> the surface itself.'),
  '<table class="guide-table"><thead><tr><th></th><th>Wire brush</th><th>Flap disc</th></tr></thead><tbody>'
  '<tr><th>Removes base metal</th><td>No</td><td>Yes</td></tr>'
  '<tr><th>Best for</th><td>Rust, scale, paint, slag, spatter</td><td>Grinding, blending welds, deburring, shaping</td></tr>'
  '<tr><th>Finish</th><td>Cleaned, original profile kept</td><td>Ground, smooth, dimension changed</td></tr>'
  '<tr><th>Uneven surfaces</th><td>Follows them</td><td>Flattens them</td></tr></tbody></table>',
  '<h2>Choose a wire brush when</h2>',
  P('You want to keep the part as it is and only clean it: before painting, between weld passes, on threads, castings or textured surfaces. See ' + link(E + 'red-knotted-wire-cup-brush/', 'knotted cup brushes') + ' and ' + link(E + 'crimped-wire-cup-brushes/', 'crimped cup brushes') + '.'),
  '<h2>Choose a flap disc when</h2>',
  P('You need to take material off: level a weld, remove a burr, round an edge or prepare a bevel. See ' + link(E + 'abrasive-flap-discs/', 'abrasive flap discs') + '; specify diameter, bore, grit and backing.'),
  '<h2>Often you need both</h2>',
  P('A common sequence on welded work is: wire brush to remove slag, flap disc to blend the weld, then a brush or ' + link(E + 'abrasive-filament-brushes/', 'abrasive nylon') + ' for the final clean before paint. For resellers, the two sell together.'),
 ]),
'wire-brushes-for-hardware-stores': dict(
 title='How to Stock Wire Brushes for a Hardware Store',
 h1='How to stock wire brushes for a hardware store',
 desc='A starter wire brush range for hardware stores and distributors: which cup brushes, wheels, drill sets and hand brushes to stock first, and packaging.',
 body=[
  P('You do not need every size to start. A small range covers most of what customers ask for; add sizes once you see what moves.'),
  '<h2>A starter range</h2>',
  '<table class="guide-table"><thead><tr><th>Item</th><th>Why</th></tr></thead><tbody>'
  '<tr><td>Crimped cup brush, 3" and 4"</td><td>General cleaning on angle grinders; the everyday seller</td></tr>'
  '<tr><td>Knotted cup brush, 3" and 4"</td><td>Heavy rust and welds</td></tr>'
  '<tr><td>Bench wheel, 6" and 8"</td><td>For bench grinders in workshops</td></tr>'
  '<tr><td>Shank-mounted set for drills</td><td>Low price point, sold as a set</td></tr>'
  '<tr><td>Hand wire brush</td><td>Impulse item at the counter</td></tr></tbody></table>',
  P('Products: ' + link(E + 'crimped-wire-cup-brushes/', 'crimped cups') + ', ' + link(E + 'red-knotted-wire-cup-brush/', 'knotted cups') + ', ' + link(E + 'wide-crimped-wire-wheels/', 'bench wheels') + ', ' + link(E + 'shaft-mounted-wire-wheels/', 'drill brushes') + ', ' + link(E + 'plastic-handle-hand-brushes/', 'hand brushes') + '.'),
  '<h2>Match the thread to your market</h2>',
  P('Cup brushes must fit the grinders sold locally. Check whether your market uses M10 (and which pitch, 1.5 or 1.25), M14 or 5/8"-11 before ordering. See ' + link(GE + 'wire-brush-sizes-and-threads/', 'sizes and threads') + '.'),
  '<h2>Packaging that sells</h2>',
  P('Blister cards hang on peg displays and protect the wire; colour boxes suit shelves. Both can carry your brand: the plate fee is RMB 300 per design and is waived at 5,000 pieces in total with 2 to 4 models on one plate. Details in ' + link(GE + 'private-label-wire-brushes/', 'private label packaging') + '.'),
  '<h2>Start with a trial order</h2>',
  P('We accept small trial orders in standard packaging, so you can test the range before committing to volume.'),
 ]),
'wire-brush-quality-checklist': dict(
 title='How to Identify a Good Quality Wire Brush',
 h1='How to identify a good quality wire brush',
 desc='A buyer checklist for wire brush quality: wire material, fill density, knot tightness, balance, wire retention and marking. What to check on samples.',
 body=[
  P('Two wire brushes can look the same in a photo and perform very differently. These are the points to check on a sample before a bulk order.'),
  '<h2>1. Wire material and diameter</h2>',
  P('Ask what the wire is: carbon steel, copper-coated steel, stainless 304 or 201, or brass. Measure the wire diameter on the sample and check that it matches the quote.'),
  '<h2>2. Fill density</h2>',
  P('More wire means longer life and a more even action. Compare the weight of samples of the same size: a much lighter brush has less wire.'),
  '<h2>3. Knots and trim</h2>',
  P('On knotted brushes the knots should be tight and even, with the same length all round. On crimped brushes the face should be even, with no long stray wires.'),
  '<h2>4. Balance</h2>',
  P('An unbalanced brush vibrates, wears the grinder and tires the operator. At YEKAI we check brushes on a balancing tester and sample every production batch.'),
  '<h2>5. Wire retention</h2>',
  P('Run the sample at working speed inside a guard. Every brush sheds a few wires at first; a good one stops shedding quickly.'),
  '<h2>6. Mount and marking</h2>',
  P('The thread or arbor hole must be clean and true, and the brush should be marked with its maximum RPM.'),
  '<h2>Ask the factory</h2>',
  '<ul><li>Samples from normal production, not specially made</li><li>The wire material and diameter in writing</li><li>The maximum RPM of each model</li><li>How batches are inspected</li></ul>',
  P('You can see the factory on the ' + link('/about/', 'about page') + ' and request samples from Frank on WhatsApp.'),
 ]),
'wire-brush-safety-and-rpm': dict(
 title='Wire Brush Safety: RPM, Wire Loss and Proper Use',
 h1='Wire brush safety: RPM, wire loss and proper use',
 desc='How to use a power wire brush safely: maximum RPM, guard and PPE, why wires break off, correct pressure and angle, and what to tell your customers.',
 body=[
  P('A power wire brush is safe when it is matched to the machine and used with light pressure. Most problems come from too much speed or too much force.'),
  '<h2>1. Never exceed the marked RPM</h2>',
  P('The maximum RPM on the brush must be equal to or higher than the no-load speed of the machine. A large brush on a small, fast grinder is the most common mistake.'),
  '<h2>2. Guard and protection</h2>',
  P('Keep the guard fitted. Wear safety glasses or a face shield, gloves and long sleeves: loose wires travel far. Keep other people away from the work area.'),
  '<h2>3. Run it in</h2>',
  P('Before first use, run a new brush at working speed for about a minute inside the guard, pointed away from people. Loose wires leave at this stage.'),
  '<h2>4. Why wires break off</h2>',
  '<ul><li><strong>Too much pressure:</strong> the wire bends and fatigues. Let the tips do the work.</li><li><strong>Wrong angle:</strong> a cup brush should work with its face, a wheel with its edge.</li><li><strong>Too much speed</strong> for the brush diameter.</li><li><strong>A worn or damaged brush:</strong> replace it.</li></ul>',
  '<h2>5. Mount it correctly</h2>',
  P('The thread must match the spindle exactly, including the pitch (M10 × 1.5 and M10 × 1.25 are different). On bench grinders use the right bushing and set the tool rest close to the wheel.'),
  '<h2>For resellers</h2>',
  P('Brushes that are balanced and marked with their RPM produce fewer complaints. See ' + link(GE + 'wire-brush-quality-checklist/', 'how to identify a good quality wire brush') + ', and ask Frank for the RPM of each model you order.'),
 ]),
'wire-brushes-india-m10': dict(
 title='Wire Brushes for 4-Inch Angle Grinders in India: M10',
 h1='Wire brushes for 4-inch angle grinders in India: M10 thread guide',
 desc='A guide for Indian importers and wholesalers: wire cup brushes for 100 mm (4 inch) grinders, M10 x 1.5 vs M10 x 1.25, popular sizes and factory terms.',
 body=[
  P('India is one of our largest export markets. Most of what we ship there is <strong>wire cup brushes</strong>, <strong>abrasive nylon brushes</strong> and <strong>flat wire wheels</strong>, mainly in <strong>3-inch (75 mm) and 4-inch (100 mm)</strong> sizes. This guide covers the points Indian importers ask about most.'),
  '<h2>M10 thread: check the pitch</h2>',
  P('The 100 mm (4-inch) angle grinder usually has an M10 spindle, but M10 comes in two pitches: <strong>M10 × 1.5</strong> (coarse) and <strong>M10 × 1.25</strong> (fine). A 1.5 nut will not go onto a 1.25 spindle at all. Before ordering, check the grinders your customers use and state the pitch in the order. M10 × 1.5 is our standard; M10 × 1.25 is made to order.'),
  '<h2>Cup brushes for 100 mm grinders</h2>',
  '<table class="guide-table"><thead><tr><th>Brush</th><th>Sizes</th><th>Use</th></tr></thead><tbody>'
  '<tr><td>' + link(E + 'crimped-wire-cup-brushes/', 'Crimped wire cup brush') + '</td><td>65, 75, 100 mm</td><td>General cleaning, paint, light rust</td></tr>'
  '<tr><td>' + link(E + 'red-knotted-wire-cup-brush/', 'Knotted wire cup brush') + '</td><td>65, 75, 100 mm</td><td>Heavy rust, scale, weld cleaning</td></tr></tbody></table>',
  P('Larger cups (125 and 150 mm) with M14 thread are available for 5-inch and 7-inch grinders.'),
  '<h2>Abrasive nylon brushes</h2>',
  P(link(E + 'abrasive-filament-brushes/', 'Abrasive nylon filament brushes') + ' come as wheel, cup and shank-mounted models in grit 80 to 320; grit 80 is the most ordered. They are used for finishing, wood and parts that must not be scratched.'),
  '<h2>Flat wire wheels</h2>',
  P('Three types: the economical arbor-hole crimped wheel, the thicker bench wheel with reducing bushings and the knotted wheel. See ' + link(GE + 'wire-wheel-for-bench-grinder/', 'how to choose a wire wheel for a bench grinder') + '.'),
  '<h2>Wire options</h2>',
  P('Carbon steel, copper-coated steel, stainless steel (304 or 201) and brass wire. See ' + link(GE + 'wire-brush-for-stainless-steel-and-aluminium/', 'which wire to use') + '.'),
  '<h2>Ordering from YEKAI</h2>',
  '<ul><li><strong>Terms:</strong> EXW, FOB or CIF to Indian ports.</li><li><strong>Payment:</strong> 30% deposit, balance before shipment.</li><li><strong>Lead time:</strong> usually about 30 days for bulk orders, confirmed per order.</li><li><strong>Packaging:</strong> plain carton, blister card or colour box, with your brand.</li><li><strong>Quality:</strong> balancing tester and sampling of every batch.</li></ul>',
  P('Send Frank the sizes, thread pitch, wire and quantity on WhatsApp for a factory quote.'),
 ]),
}

CONTENT_ES2 = {
'carda-copa-para-pulidora': dict(
 title='Cómo elegir carda copa para pulidora',
 h1='Cómo elegir una carda copa para pulidora (amoladora)',
 desc='Elige la carda copa por tamaño de pulidora, rosca (M10 x 1.5, M10 x 1.25, M14) y alambre: ondulado para limpieza ligera, trenzado para óxido y soldadura.',
 body=[
  P('La carda copa trabaja con la cara, por eso es la forma más rápida de limpiar superficies planas grandes con la pulidora (amoladora angular). Tres cosas definen cuál pedir: <strong>diámetro de la copa</strong>, <strong>rosca</strong> y <strong>tipo de alambre</strong>.'),
  '<h2>1. La copa según la pulidora</h2>',
  '<table class="guide-table"><thead><tr><th>Pulidora</th><th>Copa habitual</th><th>Rosca habitual</th></tr></thead><tbody>'
  '<tr><td>100 mm (4")</td><td>65 a 75 mm (2.5" a 3")</td><td>M10</td></tr>'
  '<tr><td>115 a 125 mm (4.5" a 5")</td><td>75 a 100 mm (3" a 4")</td><td>M14</td></tr>'
  '<tr><td>180 a 230 mm (7" a 9")</td><td>125 a 150 mm (5" a 6")</td><td>M14</td></tr></tbody></table>',
  P('Son combinaciones habituales, no una regla: la carda debe librar la guarda y sus RPM máximas deben cubrir las de la máquina.'),
  '<h2>2. La rosca correcta</h2>', THREAD_ES,
  '<h2>3. Ondulada o trenzada</h2>',
  P('<strong>Ondulada:</strong> flexible, para óxido superficial, pintura suelta y limpieza general: ' + link(S + 'crimped-wire-cup-brushes/', 'carda copa ondulada') + ', de 2.5 a 6 pulgadas. <strong>Trenzada:</strong> rígida y agresiva, para óxido grueso, cascarilla y soldadura: ' + link(S + 'red-knotted-wire-cup-brush/', 'carda copa trenzada') + ', o la ' + link(S + 'banded-twisted-cup-brushes/', 'copa trenzada con aro') + ' cuando quieres los haces más cerrados. Más en ' + link(GS + 'carda-trenzada-o-ondulada/', '¿trenzada u ondulada?') + '.'),
  '<h2>4. Material del alambre</h2>',
  P('El acero al carbono es el estándar para acero y hierro. Para acero inoxidable o aluminio usa alambre inoxidable; ver ' + link(GS + 'carda-para-acero-inoxidable-y-aluminio/', 'cardas para acero inoxidable y aluminio') + '.'),
  '<h2>Consejos de uso</h2>',
  '<ul><li>Usa poca presión y deja que trabajen las puntas del alambre; apretar más dobla el alambre y acorta la vida de la carda.</li><li>Haz girar la carda nueva un minuto aproximadamente dentro de la guarda antes del primer trabajo.</li><li>Apoya la cara de la copa plana o apenas inclinada sobre la superficie; no claves el canto.</li><li>Cambia la carda cuando el alambre esté corto o empiece a vibrar.</li></ul>',
  '<h2>Seguridad</h2>', SAFE_ES,
 ]),
'carda-para-esmeril-de-banco': dict(
 title='Cómo elegir carda para esmeril de banco',
 h1='Cómo elegir una carda para esmeril de banco',
 desc='Tres tipos de carda circular para esmeril de banco: ondulada con orificio, carda gruesa con bujes reductores y trenzada. Medidas y ajuste al eje.',
 body=[
  P('La carda para esmeril de banco trabaja con el canto y limpia piezas sueltas que se acercan a ella: herramienta, tornillería, fundición. Hay tres familias, y no se fabrican ni cuestan igual.'),
  '<h2>Los tres tipos</h2>',
  '<table class="guide-table"><thead><tr><th>Tipo</th><th>Construcción</th><th>Uso</th></tr></thead><tbody>'
  '<tr><td>Carda ondulada con orificio</td><td>Más delgada, centro metálico sencillo</td><td>Limpieza general económica</td></tr>'
  '<tr><td>Carda de banco con bujes reductores</td><td>Cara más gruesa, más alambre, bujes escalonados en el centro</td><td>Sobre todo en esmeril de banco; cuesta más que la de orificio</td></tr>'
  '<tr><td>Carda trenzada</td><td>Haces trenzados, rígida</td><td>Óxido pesado, cascarilla, soldadura</td></tr></tbody></table>',
  P('La ' + link(S + 'wide-crimped-wire-wheels/', 'carda ondulada con orificio') + ' y la ' + link(S + 'wide-crimped-wire-wheels/#bench-version', 'versión de banco con bujes') + ' vienen en los mismos diámetros, de 4 a 12 pulgadas, con alambre típico de 0.3 mm. Para trenzadas, ver la ' + link(S + 'stringer-knotted-wheels/', 'carda trenzada angosta') + ' (4.5 a 7 pulgadas).'),
  '<h2>Diámetro</h2>',
  P('Usa el diámetro para el que está hecho el esmeril: un esmeril de 6 pulgadas lleva carda de 6" (150 mm); uno de 8 pulgadas, de 8" (200 mm). Nunca montes una carda mayor de lo que permite la guarda.'),
  '<h2>Orificio y bujes</h2>',
  P('Indica el diámetro de la flecha del esmeril. Las cardas con bujes reductores sirven para varias medidas de flecha con una sola pieza; por eso convienen al distribuidor: menos referencias en inventario. Confirma con Frank las medidas de buje para tu mercado.'),
  '<h2>Alambre</h2>',
  P('Acero al carbono ondulado o acero cobrizado para trabajo general; acero inoxidable para piezas de inoxidable; latón para metales blandos. El alambre típico de nuestra serie de banco es de 0.3 mm.'),
  '<h2>Consejos de uso</h2>',
  '<ul><li>Usa poca presión y deja que trabajen las puntas del alambre; apretar más dobla el alambre y acorta la vida de la carda.</li><li>Haz girar la carda nueva un minuto aproximadamente dentro de la guarda antes del primer trabajo.</li><li>Acerca la pieza por debajo del centro de la carda y deja el apoyo cerca. Voltea la carda de vez en cuando para que el alambre se desgaste parejo.</li><li>Cambia la carda cuando el alambre esté corto o empiece a vibrar.</li></ul>',
  '<h2>Seguridad</h2>', SAFE_ES,
 ]),
'carda-para-taladro': dict(
 title='Cardas para taladro: de punta, circular y copa',
 h1='Cardas para taladro: de punta, circulares y de copa',
 desc='Qué carda con vástago usar en el taladro: de punta para huecos, circular para bordes y de copa para zonas planas. Vástago, cabezal y tipo de alambre.',
 body=[
  P('La carda con vástago se sujeta en el mandril del taladro y llega a donde la pulidora no entra. Las tres formas hacen trabajos distintos.'),
  '<table class="guide-table"><thead><tr><th>Forma</th><th>Trabaja con</th><th>Trabajo típico</th></tr></thead><tbody>'
  '<tr><td>De punta</td><td>La punta</td><td>Huecos, interior de tubo, esquinas, raíz de soldadura</td></tr>'
  '<tr><td>Circular</td><td>El canto</td><td>Bordes, ranuras, roscas</td></tr>'
  '<tr><td>De copa</td><td>La cara</td><td>Zonas planas pequeñas, herrería, barandales</td></tr></tbody></table>',
  P('Las tres están en nuestras ' + link(S + 'shaft-mounted-wire-wheels/', 'cardas con vástago para taladro') + '. Las de punta trenzadas van de 19 a 30 mm de cabezal.'),
  '<h2>Qué indicar</h2>',
  '<ul><li><strong>Diámetro del vástago:</strong> debe entrar en el mandril; indícalo en el pedido.</li><li><strong>Diámetro del cabezal</strong> y forma.</li><li><strong>Alambre:</strong> ondulado para limpieza general, trenzado para óxido pesado y soldadura.</li><li><strong>Material:</strong> acero al carbono, acero cobrizado, acero inoxidable o latón.</li></ul>',
  '<h2>Si la pieza no debe rayarse</h2>',
  P('Usa un ' + link(S + 'abrasive-filament-brushes/', 'cepillo de nylon abrasivo') + ' con vástago: los modelos listados son de vástago de 6 mm y vienen en grano 80 a 320.'),
  '<h2>Para distribuidores</h2>',
  P('Las cardas para taladro se venden bien en juego. Las empacamos ' + link(S + 'blister-card-brush-sets/', 'en blíster con tarjeta') + ' con los modelos y piezas por tarjeta que tú definas.'),
  '<h2>Seguridad</h2>', SAFE_ES,
 ]),
'cepillo-para-madera': dict(
 title='Cepillos para texturizar y envejecer madera',
 h1='Cepillos para texturizar y envejecer madera',
 desc='Cómo texturizar y envejecer madera con carda de alambre y cepillo de nylon abrasivo: alambre para abrir la veta y nylon grano 80 para limpiar y acabar.',
 body=[
  P('Cepillar la madera quita la veta blanda y deja la dura en relieve: el acabado rústico o envejecido que se usa en muebles, vigas y pisos. Normalmente se hace en dos pasos.'),
  '<h2>Paso 1: abrir la veta con alambre</h2>',
  P('Una carda de alambre ondulado corta rápido la veta blanda. Trabaja <strong>a favor de la veta</strong>, con poca presión, y prueba primero en un recorte. Usa una ' + link(S + 'crimped-wire-cup-brushes/', 'carda copa ondulada') + ' en la pulidora para tablas, o una ' + link(S + 'wide-crimped-wire-wheels/', 'carda circular ancha') + ' en máquina de banco para piezas chicas. Las trenzadas suelen ser demasiado agresivas para madera.'),
  '<h2>Paso 2: limpiar y acabar con nylon abrasivo</h2>',
  P('El ' + link(S + 'abrasive-filament-brushes/', 'cepillo de nylon abrasivo') + ' quita la fibra que deja el alambre y suaviza la superficie sin aplanar la textura. <strong>El grano 80 es el más pedido</strong>; el 120 deja un acabado un poco más fino. El catálogo cubre grano 80 a 320.'),
  '<h2>Cuál elegir</h2>',
  '<table class="guide-table"><thead><tr><th>Objetivo</th><th>Cepillo</th></tr></thead><tbody>'
  '<tr><td>Textura profunda en madera blanda</td><td>Alambre ondulado y después nylon grano 80</td></tr>'
  '<tr><td>Textura ligera, madera dura</td><td>Sólo nylon abrasivo grano 80</td></tr>'
  '<tr><td>Limpieza antes de tinte o aceite</td><td>Nylon abrasivo grano 120 o más fino</td></tr></tbody></table>',
  '<h2>Formas para talleres de muebles</h2>',
  P('El nylon abrasivo viene circular (75 a 200 mm), de copa (75 a 125 mm) y con vástago para taladro. El color no identifica por sí solo el grano; confírmalo para cada modelo. Más en ' + link(GS + 'cepillo-de-nylon-abrasivo/', 'cepillo de nylon abrasivo: usos y grano') + '.'),
  '<h2>Pide muestras</h2>',
  P('Cada madera responde distinto, así que conviene probar antes del pedido grande. Dile a Frank la madera, la máquina y el acabado que buscas, y pide muestras en dos granos.'),
 ]),
'carda-para-acero-inoxidable-y-aluminio': dict(
 title='Cardas para acero inoxidable y aluminio',
 h1='Cardas para acero inoxidable y aluminio: qué alambre usar',
 desc='Por qué el alambre de acero al carbono mancha el acero inoxidable y qué usar en su lugar: inoxidable 304 o 201, latón o nylon abrasivo. Comparación.',
 body=[
  P('El material del alambre importa tanto como la forma. El alambre equivocado puede dejar manchas de óxido en una pieza que nunca debería oxidarse.'),
  '<h2>Por qué no usar acero al carbono en inoxidable</h2>',
  P('Una carda de acero al carbono deja partículas de acero en la superficie. En acero inoxidable o aluminio esas partículas se oxidan y manchan la pieza después, a veces días más tarde. Pasa lo mismo con una carda inoxidable que ya se usó en acero común: usa cardas separadas.'),
  '<h2>Alambres que fabricamos</h2>',
  '<table class="guide-table"><thead><tr><th>Alambre</th><th>Para qué</th></tr></thead><tbody>'
  '<tr><td>Acero al carbono</td><td>Acero y hierro: óxido, cascarilla, pintura, soldadura</td></tr>'
  '<tr><td>Acero cobrizado</td><td>Mismos usos que el acero al carbono; el recubrimiento protege el alambre en almacén. Sigue siendo acero: no es para inoxidable</td></tr>'
  '<tr><td>Acero inoxidable 304</td><td>Piezas de acero inoxidable y aluminio</td></tr>'
  '<tr><td>Acero inoxidable 201</td><td>Opción inoxidable más económica; confirma si sirve para tu aplicación</td></tr>'
  '<tr><td>Latón</td><td>Más blando que el acero: para metales blandos y una acción más suave</td></tr></tbody></table>',
  P('El alambre cobrizado y el de latón se parecen, pero no son el mismo producto. Indica cuál necesitas.'),
  '<h2>Cuándo usar nylon abrasivo</h2>',
  P('Para un acabado fino y parejo en inoxidable o aluminio, sin contacto de metal, usa un ' + link(S + 'abrasive-filament-brushes/', 'cepillo de nylon abrasivo') + '.'),
  '<h2>Cómo pedir</h2>',
  P('El material del alambre se confirma por modelo. Elige primero la forma (' + link(S + 'red-knotted-wire-cup-brush/', 'copa') + ', ' + link(S + 'wide-crimped-wire-wheels/', 'circular') + ', ' + link(S + 'shaft-mounted-wire-wheels/', 'con vástago') + ') y dile a Frank el material de la pieza; él confirma el alambre.'),
 ]),
'carda-o-disco-flap': dict(
 title='¿Carda o disco flap? Cuál usar en cada trabajo',
 h1='¿Carda o disco flap? Cuál usar en cada trabajo',
 desc='La carda limpia sin quitar metal base; el disco flap desbasta y empareja. Cuándo usar cada uno en óxido, pintura, soldadura y bordes, y cuándo los dos.',
 body=[
  P('Los dos van en la pulidora y los dos se usan en metal, pero hacen trabajos opuestos. La <strong>carda limpia</strong> lo que está sobre la superficie. El <strong>disco flap quita</strong> la superficie misma.'),
  '<table class="guide-table"><thead><tr><th></th><th>Carda</th><th>Disco flap</th></tr></thead><tbody>'
  '<tr><th>Quita metal base</th><td>No</td><td>Sí</td></tr>'
  '<tr><th>Mejor para</th><td>Óxido, cascarilla, pintura, escoria, salpicaduras</td><td>Desbastar, emparejar soldadura, quitar rebaba, dar forma</td></tr>'
  '<tr><th>Acabado</th><td>Limpio, conserva el perfil original</td><td>Desbastado, liso, cambia la medida</td></tr>'
  '<tr><th>Superficies irregulares</th><td>Las sigue</td><td>Las aplana</td></tr></tbody></table>',
  '<h2>Usa carda cuando</h2>',
  P('Quieres conservar la pieza como está y sólo limpiarla: antes de pintar, entre pasadas de soldadura, en roscas, fundición o superficies con textura. Ver ' + link(S + 'red-knotted-wire-cup-brush/', 'cardas copa trenzadas') + ' y ' + link(S + 'crimped-wire-cup-brushes/', 'cardas copa onduladas') + '.'),
  '<h2>Usa disco flap cuando</h2>',
  P('Necesitas quitar material: emparejar una soldadura, quitar rebaba, redondear un filo o preparar un bisel. Ver ' + link(S + 'abrasive-flap-discs/', 'discos flap') + '; indica diámetro, orificio, grano y respaldo.'),
  '<h2>Muchas veces se usan los dos</h2>',
  P('Una secuencia común en herrería: carda para quitar la escoria, disco flap para emparejar la soldadura, y carda o ' + link(S + 'abrasive-filament-brushes/', 'nylon abrasivo') + ' para la limpieza final antes de pintar. Para la ferretería, los dos se venden juntos.'),
 ]),
'surtido-de-cardas-para-ferreteria': dict(
 title='Qué cardas surtir en una ferretería',
 h1='Qué cardas surtir primero en una ferretería',
 desc='Surtido inicial de cardas para ferreterías y distribuidores: qué copas, cardas circulares, juegos para taladro y cepillos de mano pedir, y cómo empacarlos.',
 body=[
  P('No hace falta tener todas las medidas para empezar. Un surtido corto cubre casi todo lo que pide el cliente; después agregas medidas según lo que se mueva.'),
  '<h2>Surtido inicial</h2>',
  '<table class="guide-table"><thead><tr><th>Producto</th><th>Por qué</th></tr></thead><tbody>'
  '<tr><td>Carda copa ondulada, 3" y 4"</td><td>Limpieza general con pulidora; la de venta diaria</td></tr>'
  '<tr><td>Carda copa trenzada, 3" y 4"</td><td>Óxido pesado y soldadura</td></tr>'
  '<tr><td>Carda para esmeril, 6" y 8"</td><td>Para esmeril de banco en talleres</td></tr>'
  '<tr><td>Juego de cardas con vástago para taladro</td><td>Precio bajo, se vende en juego</td></tr>'
  '<tr><td>Cepillo de alambre de mano</td><td>Venta de mostrador</td></tr></tbody></table>',
  P('Productos: ' + link(S + 'crimped-wire-cup-brushes/', 'copas onduladas') + ', ' + link(S + 'red-knotted-wire-cup-brush/', 'copas trenzadas') + ', ' + link(S + 'wide-crimped-wire-wheels/', 'cardas para esmeril') + ', ' + link(S + 'shaft-mounted-wire-wheels/', 'cardas para taladro') + ', ' + link(S + 'plastic-handle-hand-brushes/', 'cepillos de mano') + '.'),
  '<h2>La rosca según tu mercado</h2>',
  P('Las copas deben entrar en las pulidoras que se venden en tu zona. Revisa si tu mercado usa M10 (y con qué paso, 1.5 o 1.25), M14 o 5/8"-11 antes de pedir. Ver ' + link(GS + 'medidas-de-carda/', 'medidas y roscas') + '.'),
  '<h2>Empaque que vende</h2>',
  P('El blíster con tarjeta se cuelga en exhibidor y protege el alambre; la caja a color va en anaquel. Los dos pueden llevar tu marca: la placa cuesta 300 RMB por diseño y se bonifica con 5,000 piezas en total y de 2 a 4 modelos en una plancha. Detalles en ' + link(GS + 'cardas-con-tu-marca/', 'cardas con tu marca') + '.'),
  '<h2>Empieza con un pedido de prueba</h2>',
  P('Aceptamos pedidos pequeños de prueba con empaque estándar, para que pruebes el surtido antes de comprometerte con volumen.'),
 ]),
'calidad-de-cardas': dict(
 title='Cómo reconocer una carda de buena calidad',
 h1='Cómo reconocer una carda de buena calidad',
 desc='Lista para revisar la calidad de una carda: material del alambre, densidad, haces, balanceo, retención del alambre y marcado. Qué revisar en las muestras.',
 body=[
  P('Dos cardas pueden verse iguales en foto y rendir muy distinto. Estos son los puntos a revisar en la muestra antes de un pedido grande.'),
  '<h2>1. Material y calibre del alambre</h2>',
  P('Pregunta qué alambre es: acero al carbono, acero cobrizado, inoxidable 304 o 201, o latón. Mide el calibre en la muestra y revisa que coincida con la cotización.'),
  '<h2>2. Densidad</h2>',
  P('Más alambre significa más vida y una acción más pareja. Compara el peso de muestras de la misma medida: una carda mucho más ligera lleva menos alambre.'),
  '<h2>3. Haces y recorte</h2>',
  P('En las trenzadas, los haces deben estar apretados y parejos, del mismo largo en toda la vuelta. En las onduladas, la cara debe ser pareja, sin alambres largos sueltos.'),
  '<h2>4. Balanceo</h2>',
  P('Una carda desbalanceada vibra, desgasta la pulidora y cansa al operador. En YEKAI revisamos las cardas en un equipo de balanceo y muestreamos cada lote de producción.'),
  '<h2>5. Retención del alambre</h2>',
  P('Prueba la muestra a velocidad de trabajo dentro de una guarda. Toda carda suelta algunos alambres al inicio; una buena deja de soltarlos pronto.'),
  '<h2>6. Montaje y marcado</h2>',
  P('La rosca o el orificio deben estar limpios y centrados, y la carda debe traer marcadas sus RPM máximas.'),
  '<h2>Qué pedirle a la fábrica</h2>',
  '<ul><li>Muestras de producción normal, no hechas especialmente</li><li>Material y calibre del alambre por escrito</li><li>RPM máximas de cada modelo</li><li>Cómo se inspeccionan los lotes</li></ul>',
  P('Puedes conocer la fábrica en ' + link('/es/about/', 'sobre YEKAI') + ' y pedir muestras a Frank por WhatsApp.'),
 ]),
'seguridad-y-rpm-de-cardas': dict(
 title='Seguridad con cardas: RPM y alambre que se suelta',
 h1='Seguridad con cardas: RPM, desprendimiento de alambre y uso correcto',
 desc='Cómo usar una carda con seguridad: RPM máximas, guarda y protección, por qué se sueltan los alambres, presión y ángulo correctos, y qué decir al cliente.',
 body=[
  P('Una carda es segura cuando corresponde a la máquina y se usa con poca presión. Casi todos los problemas vienen de exceso de velocidad o de fuerza.'),
  '<h2>1. Nunca pases las RPM marcadas</h2>',
  P('Las RPM máximas de la carda deben ser iguales o mayores que la velocidad sin carga de la máquina. Una carda grande en una pulidora chica y rápida es el error más común.'),
  '<h2>2. Guarda y protección</h2>',
  P('Deja puesta la guarda. Usa lentes o careta, guantes y manga larga: los alambres sueltos llegan lejos. Mantén a otras personas fuera del área.'),
  '<h2>3. Asentar la carda</h2>',
  P('Antes del primer uso, haz girar la carda nueva a velocidad de trabajo durante un minuto aproximadamente, dentro de la guarda y sin apuntar a nadie. Ahí salen los alambres flojos.'),
  '<h2>4. Por qué se sueltan los alambres</h2>',
  '<ul><li><strong>Demasiada presión:</strong> el alambre se dobla y se fatiga. Deja que trabajen las puntas.</li><li><strong>Ángulo equivocado:</strong> la copa trabaja con la cara; la circular, con el canto.</li><li><strong>Demasiada velocidad</strong> para el diámetro de la carda.</li><li><strong>Carda gastada o dañada:</strong> cámbiala.</li></ul>',
  '<h2>5. Montaje correcto</h2>',
  P('La rosca debe coincidir exactamente con el eje, también en el paso (M10 × 1.5 y M10 × 1.25 son distintas). En esmeril de banco usa el buje correcto y acerca el apoyo a la carda.'),
  '<h2>Para distribuidores</h2>',
  P('Las cardas balanceadas y marcadas con sus RPM generan menos reclamos. Ver ' + link(GS + 'calidad-de-cardas/', 'cómo reconocer una carda de buena calidad') + ' y pide a Frank las RPM de cada modelo.'),
 ]),
}

FAQ2 = {
'wire-cup-brush-for-angle-grinder': [
 ('What size wire cup brush fits a 4-inch angle grinder?', 'Typically a 65 to 75 mm (2.5 to 3 in) cup with an M10 thread. Check the guard clearance and the thread pitch before ordering.'),
 ('Are M10 x 1.5 and M10 x 1.25 interchangeable?', 'No. They are different pitches and do not fit each other. State the pitch in the order.'),
 ('Crimped or knotted cup brush?', 'Crimped for light cleaning and loose paint; knotted for heavy rust, scale and welds.')],
'wire-wheel-for-bench-grinder': [
 ('What size wire wheel fits a 6-inch bench grinder?', 'A 6-inch (150 mm) wheel. Use the diameter the grinder and its guard are built for.'),
 ('What are reducing bushings on a wire wheel?', 'Stepped rings in the hub that let one wheel fit several shaft diameters.'),
 ('Why is a bench wheel more expensive than an arbor-hole wheel?', 'It has a thicker face, more wire and the bushing set, and it is built for bench grinder use.')],
'wire-brush-for-drill': [
 ('Can I use a wire brush in a drill?', 'Yes, with a shank-mounted brush that fits the chuck. Respect the maximum RPM of the brush.'),
 ('Which drill brush for holes?', 'An end brush: it works on its tip and reaches holes, pipe interiors and corners.'),
 ('What shank do drill wire brushes have?', 'It depends on the model; state the chuck size and Frank confirms the shank.')],
'wire-brush-for-wood': [
 ('What brush is used to texture wood?', 'A crimped steel wire brush to open the grain, followed by an abrasive nylon brush to clean and finish.'),
 ('What grit of nylon brush for wood?', 'Grit 80 is the most ordered; 120 gives a slightly finer finish.'),
 ('Should I brush with or against the grain?', 'Along the grain, with light pressure. Test on an offcut first.')],
'wire-brush-for-stainless-steel-and-aluminium': [
 ('Can I use a carbon steel wire brush on stainless steel?', 'No. It leaves steel particles that rust and stain the part. Use stainless steel wire.'),
 ('Is copper-coated wire the same as brass wire?', 'No. Copper-coated wire is steel with a coating; brass wire is solid brass and softer.'),
 ('Which wire for aluminium?', 'Stainless steel wire, or an abrasive nylon brush for a finer finish.')],
'wire-brush-vs-flap-disc': [
 ('Does a wire brush remove metal?', 'No. It removes rust, scale and paint and leaves the base metal. A flap disc removes metal.'),
 ('Which is better for removing rust?', 'A wire brush if you only need to clean; a flap disc if the surface must also be ground smooth.'),
 ('Can I blend a weld with a wire brush?', 'No. Use a flap disc to blend; use the wire brush to remove slag and spatter.')],
'wire-brushes-for-hardware-stores': [
 ('Which wire brushes sell most in a hardware store?', 'Crimped and knotted cup brushes in 3 and 4 inch, bench wheels in 6 and 8 inch, drill sets and hand brushes.'),
 ('Can I order with my own brand?', 'Yes: blister card or colour box. The RMB 300 plate fee is waived at 5,000 pieces in total with 2 to 4 models on one plate.'),
 ('Is there a minimum order?', 'Small trial orders in standard packaging are accepted, without wholesale pricing.')],
'wire-brush-quality-checklist': [
 ('How do I check wire brush quality?', 'Check the wire material and diameter, fill density, knot tightness, balance, wire retention and RPM marking on a sample.'),
 ('Why does a wire brush vibrate?', 'Usually because it is unbalanced. Balanced brushes run smoother and last longer.'),
 ('Is it normal for a new wire brush to lose wires?', 'A few at first, yes. A good brush stops shedding quickly; run it in inside the guard.')],
'wire-brush-safety-and-rpm': [
 ('What RPM should a wire brush run at?', 'Never above the maximum RPM marked on the brush. The machine speed must be equal or lower.'),
 ('Why do wires fly off a wire brush?', 'Too much pressure, the wrong angle, too much speed or a worn brush.'),
 ('What protection is needed?', 'The machine guard, safety glasses or a face shield, gloves and long sleeves.')],
'wire-brushes-india-m10': [
 ('What thread do 4-inch angle grinders use?', 'M10, in one of two pitches: M10 x 1.5 or M10 x 1.25. Check the spindle before ordering.'),
 ('Which wire brush sizes are most common in India?', 'In our shipments, 3-inch (75 mm) and 4-inch (100 mm).'),
 ('What are the payment terms?', '30% deposit and the balance before shipment. Bulk lead time is usually about 30 days, confirmed per order.')],
'carda-copa-para-pulidora': [
 ('¿Qué carda copa le queda a una pulidora de 4 pulgadas?', 'Normalmente una copa de 65 a 75 mm (2.5 a 3 pulgadas) con rosca M10. Revisa la guarda y el paso de la rosca antes de pedir.'),
 ('¿M10 x 1.5 y M10 x 1.25 son intercambiables?', 'No. Son pasos distintos y una no entra en la otra. Indica el paso en el pedido.'),
 ('¿Copa ondulada o trenzada?', 'Ondulada para limpieza ligera y pintura suelta; trenzada para óxido pesado, cascarilla y soldadura.')],
'carda-para-esmeril-de-banco': [
 ('¿Qué carda lleva un esmeril de 6 pulgadas?', 'Una carda de 6 pulgadas (150 mm). Usa el diámetro para el que están hechos el esmeril y su guarda.'),
 ('¿Qué son los bujes reductores?', 'Anillos escalonados en el centro que permiten usar una misma carda en varias medidas de flecha.'),
 ('¿Por qué cuesta más la carda de banco que la de orificio?', 'Lleva cara más gruesa, más alambre y el juego de bujes, y está hecha para esmeril de banco.')],
'carda-para-taladro': [
 ('¿Se puede usar una carda en el taladro?', 'Sí, con una carda con vástago que entre en el mandril. Respeta las RPM máximas de la carda.'),
 ('¿Qué carda de taladro sirve para huecos?', 'La de punta: trabaja con la punta y llega a huecos, interior de tubo y esquinas.'),
 ('¿Qué vástago traen las cardas para taladro?', 'Depende del modelo; indica la medida del mandril y Frank confirma el vástago.')],
'cepillo-para-madera': [
 ('¿Qué cepillo se usa para texturizar madera?', 'Una carda de alambre ondulado para abrir la veta y después un cepillo de nylon abrasivo para limpiar y acabar.'),
 ('¿Qué grano de nylon para madera?', 'El grano 80 es el más pedido; el 120 deja un acabado un poco más fino.'),
 ('¿Se cepilla a favor o en contra de la veta?', 'A favor de la veta, con poca presión. Prueba primero en un recorte.')],
'carda-para-acero-inoxidable-y-aluminio': [
 ('¿Puedo usar carda de acero al carbono en inoxidable?', 'No. Deja partículas de acero que se oxidan y manchan la pieza. Usa alambre de acero inoxidable.'),
 ('¿El alambre cobrizado es lo mismo que el de latón?', 'No. El cobrizado es acero con recubrimiento; el de latón es latón macizo y más blando.'),
 ('¿Qué alambre para aluminio?', 'Acero inoxidable, o un cepillo de nylon abrasivo para un acabado más fino.')],
'carda-o-disco-flap': [
 ('¿La carda quita metal?', 'No. Quita óxido, cascarilla y pintura y deja el metal base. El disco flap sí quita metal.'),
 ('¿Qué es mejor para quitar óxido?', 'La carda si sólo hay que limpiar; el disco flap si además hay que dejar la superficie lisa.'),
 ('¿Se puede emparejar una soldadura con carda?', 'No. Para emparejar usa disco flap; la carda quita escoria y salpicaduras.')],
'surtido-de-cardas-para-ferreteria': [
 ('¿Qué cardas se venden más en ferretería?', 'Copas onduladas y trenzadas de 3 y 4 pulgadas, cardas para esmeril de 6 y 8, juegos para taladro y cepillos de mano.'),
 ('¿Puedo pedirlas con mi marca?', 'Sí: blíster con tarjeta o caja a color. La placa de 300 RMB se bonifica con 5,000 piezas en total y de 2 a 4 modelos en una plancha.'),
 ('¿Hay pedido mínimo?', 'Aceptamos pedidos pequeños de prueba con empaque estándar, sin precio de mayoreo.')],
'calidad-de-cardas': [
 ('¿Cómo reviso la calidad de una carda?', 'Revisa en la muestra el material y calibre del alambre, la densidad, los haces, el balanceo, la retención del alambre y el marcado de RPM.'),
 ('¿Por qué vibra una carda?', 'Casi siempre porque está desbalanceada. Las cardas balanceadas giran más suave y duran más.'),
 ('¿Es normal que una carda nueva suelte alambres?', 'Algunos al principio, sí. Una buena deja de soltarlos pronto; asiéntala dentro de la guarda.')],
'seguridad-y-rpm-de-cardas': [
 ('¿A cuántas RPM debe girar una carda?', 'Nunca por encima de las RPM máximas marcadas. La velocidad de la máquina debe ser igual o menor.'),
 ('¿Por qué se sueltan los alambres?', 'Por demasiada presión, ángulo equivocado, exceso de velocidad o carda gastada.'),
 ('¿Qué protección se necesita?', 'La guarda de la máquina, lentes o careta, guantes y manga larga.')],
}

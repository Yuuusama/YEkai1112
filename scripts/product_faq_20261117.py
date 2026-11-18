"""2026-11-17 — "¿Qué es? / ¿Dónde comprar?" para las 13 páginas de producto restantes (ES + EN)
y contenido ampliado de la página About (datos dados por Frank el 2026-11-17).
Lo importa scripts/seo_mx_20261116.py.
"""
BUY_ES = 'Directo de fábrica con YEKAI, en Yongkang, China. Cotizamos en EXW, FOB o CIF a cualquier país; para México también hay DDP bajo cotización. Envía por WhatsApp {x} y la cantidad.'
BUY_EN = 'Direct from the YEKAI factory in Yongkang, China. We quote EXW, FOB or CIF to any country; DDP to Mexico is available on request. Send {x} and quantity on WhatsApp.'

# slug: (qué es ES, respuesta ES, dónde ES, datos ES, what EN, answer EN, where EN, data EN)
_D = {
 'red-knotted-wire-cup-brush': (
  '¿Qué es una carda copa de alambre trenzado?',
  'Es un cepillo en forma de copa con haces de alambre de acero trenzado que se enrosca en la pulidora (amoladora angular). Se usa para trabajo pesado: quitar óxido grueso, cascarilla, pintura y limpiar soldadura en superficies planas. Serie de 2.5 a 6 pulgadas.',
  '¿Dónde comprar cardas copa trenzadas al mayoreo?', 'el diámetro, la rosca',
  'What is a knotted wire cup brush?',
  'It is a cup-shaped brush with twisted knots of steel wire that threads onto an angle grinder. It is used for heavy work: removing thick rust, scale and paint and cleaning welds on flat surfaces. Series from 2.5 to 6 in.',
  'Where can I buy knotted wire cup brushes wholesale?', 'the diameter, thread'),
 'crimped-wire-cup-brushes': (
  '¿Qué es una carda copa de alambre ondulado?',
  'Es un cepillo en forma de copa con alambre de acero ondulado y suelto, para pulidora (amoladora angular). Es más flexible que la trenzada y se usa para limpieza ligera y media de superficies amplias: óxido superficial y pintura suelta. Serie de 2.5 a 6 pulgadas.',
  '¿Dónde comprar cardas copa onduladas al mayoreo?', 'el diámetro, la rosca',
  'What is a crimped wire cup brush?',
  'It is a cup-shaped brush with loose, wavy steel wire for angle grinders. It is more flexible than a knotted cup and is used for light to medium cleaning of broad surfaces: surface rust and loose paint. Series from 2.5 to 6 in.',
  'Where can I buy crimped wire cup brushes wholesale?', 'the diameter, thread'),
 'banded-twisted-cup-brushes': (
  '¿Qué es una carda copa trenzada con aro?',
  'Es una carda copa de alambre trenzado con un aro metálico que mantiene los haces más cerrados, para una acción más rígida y concentrada en la pulidora. Serie de 2.5, 3, 3.5, 4 y 5 pulgadas.',
  '¿Dónde comprar cardas copa con aro al mayoreo?', 'el diámetro, la rosca',
  'What is a banded knot wire cup brush?',
  'It is a knotted wire cup brush with a steel band that holds the knots tighter, for a stiffer, more concentrated action on an angle grinder. Series in 2.5, 3, 3.5, 4 and 5 in.',
  'Where can I buy banded knot cup brushes wholesale?', 'the diameter, thread'),
 'twisted-wire-wheels': (
  '¿Qué es una carda cónica de alambre trenzado?',
  'Es un cepillo para pulidora con los haces de alambre trenzado inclinados en forma de cono. Llega a esquinas, bordes y soldaduras en ángulo donde una copa no entra. Serie de 4, 4.5 y 5 pulgadas, alambre típico de 0.5 mm.',
  '¿Dónde comprar cardas cónicas al mayoreo?', 'el diámetro, la rosca',
  'What is a knotted bevel wire brush?',
  'It is an angle grinder brush with twisted wire knots set at an angle, like a cone. It reaches corners, edges and fillet welds where a cup brush does not fit. Series in 4, 4.5 and 5 in, typical wire 0.5 mm.',
  'Where can I buy knotted bevel brushes wholesale?', 'the diameter, thread'),
 'wide-crimped-wire-wheels': (
  '¿Qué es una carda circular para esmeril?',
  'Es una rueda de alambre ondulado de cara ancha con orificio central, que se monta en el esmeril de banco. Se usa para limpiar óxido, pintura y rebabas en piezas sueltas. Serie de 4 a 12 pulgadas, alambre típico de 0.3 mm.',
  '¿Dónde comprar cardas para esmeril al mayoreo?', 'el diámetro, el ancho, el orificio',
  'What is a crimped wire wheel for a bench grinder?',
  'It is a wide-face wheel of crimped steel wire with an arbor hole that mounts on a bench grinder. It is used to clean rust, paint and burrs from loose parts. Series from 4 to 12 in, typical wire 0.3 mm.',
  'Where can I buy bench grinder wire wheels wholesale?', 'the diameter, face width, arbor hole'),
 'crimped-wire-brush-wheels': (
  '¿Qué es una carda circular de alambre ondulado?',
  'Es una rueda de alambre de acero ondulado con centro metálico y orificio para montarla en el eje de la máquina. Trabaja con el canto y sirve para limpieza general de metal.',
  '¿Dónde comprar cardas circulares onduladas al mayoreo?', 'el diámetro, una foto del montaje',
  'What is a crimped wire brush wheel?',
  'It is a wheel of crimped steel wire with a metal hub and an arbor hole for mounting on the machine shaft. It works on its edge and is used for general metal cleaning.',
  'Where can I buy crimped wire brush wheels wholesale?', 'the diameter, a photo of the mount'),
 'copper-coated-wire-wheels': (
  '¿Qué es una carda circular de alambre cobrizado?',
  'Es una rueda de alambre de acero con recubrimiento de cobre, por eso su color dorado. Se usa para limpiar y preparar superficies metálicas. Alambre típico de 0.3 mm.',
  '¿Dónde comprar cardas de alambre cobrizado al mayoreo?', 'el diámetro, el ancho, el montaje',
  'What is a copper-coated wire wheel?',
  'It is a wheel of steel wire with a copper coating, which gives it its golden colour. It is used to clean and prepare metal surfaces. Typical wire 0.3 mm.',
  'Where can I buy copper-coated wire wheels wholesale?', 'the diameter, face width, mount'),
 'stringer-knotted-wheels': (
  '¿Qué es una carda trenzada angosta para soldadura?',
  'Es una rueda de haces trenzados finos y angostos, pensada para seguir el cordón de soldadura y entrar en biseles: quita escoria y salpicaduras. Serie de 4.5, 5, 6 y 7 pulgadas, alambre típico de 0.5 mm de acero al carbono.',
  '¿Dónde comprar cardas para soldadura al mayoreo?', 'el diámetro, el ancho de trabajo, el orificio',
  'What is a stringer bead wire wheel?',
  'It is a wheel with narrow, tightly twisted knots designed to follow a weld bead and enter bevels, removing slag and spatter. Series in 4.5, 5, 6 and 7 in, typical wire 0.5 mm carbon steel.',
  'Where can I buy stringer bead wheels wholesale?', 'the diameter, working width, arbor hole'),
 'shaft-mounted-wire-wheels': (
  '¿Qué es una carda con vástago para taladro?',
  'Es un cepillo de alambre con un vástago que se sujeta en el mandril del taladro. Hay de punta, circulares y de copa, para huecos, bordes y zonas pequeñas donde no entra la pulidora.',
  '¿Dónde comprar cardas para taladro al mayoreo?', 'la forma, el diámetro del cabezal, el vástago',
  'What is a shank-mounted wire brush?',
  'It is a wire brush with a shank that is held in a drill chuck. It comes as end, wheel and cup shapes, for holes, edges and small areas where an angle grinder does not fit.',
  'Where can I buy wire brushes for drills wholesale?', 'the shape, head diameter, shank'),
 'plastic-handle-hand-brushes': (
  '¿Qué es un cepillo de alambre de mano?',
  'Es un cepillo manual con cerdas de alambre y mango de plástico. Se usa para limpiar óxido, pintura suelta y soldadura a mano, sin máquina.',
  '¿Dónde comprar cepillos de alambre de mano al mayoreo?', 'el largo del cepillo, las hileras de alambre o una foto de referencia',
  'What is a hand wire brush?',
  'It is a manual brush with wire bristles and a plastic handle. It is used to clean rust, loose paint and welds by hand, without a machine.',
  'Where can I buy hand wire brushes wholesale?', 'the brush length, wire rows or a reference photo'),
 'blister-card-brush-sets': (
  '¿Qué es un juego de cardas en blíster?',
  'Es un surtido de cardas o cepillos de alambre empacado en blíster con tarjeta, listo para colgar en el exhibidor de la ferretería. Tú defines los modelos, las piezas por tarjeta y el diseño.',
  '¿Dónde comprar juegos de cardas en blíster al mayoreo?', 'los modelos, las piezas por tarjeta, tu diseño',
  'What is a wire brush set on a blister card?',
  'It is an assortment of wire brushes packed on a blister card, ready to hang on a hardware store display. You define the models, the pieces per card and the artwork.',
  'Where can I buy wire brush sets wholesale?', 'the models, pieces per card, your artwork'),
 'abrasive-filament-brushes': (
  '¿Qué es un cepillo de nylon abrasivo?',
  'Es un cepillo con cerdas de nylon que llevan grano abrasivo en todo el filamento. Quita óxido, corrosión, pintura e imprimación marcando menos la pieza que una carda de alambre. Hay circulares, de copa y con vástago, en grano 80 a 320.',
  '¿Dónde comprar cepillos de nylon abrasivo al mayoreo?', 'la forma, el diámetro, el grano',
  'What is an abrasive nylon filament brush?',
  'It is a brush with nylon bristles that carry abrasive grain through the whole filament. It removes rust, corrosion, paint and primer while marking the part less than a wire brush. Available as wheel, cup and shank-mounted shapes, grit 80 to 320.',
  'Where can I buy abrasive nylon brushes wholesale?', 'the shape, diameter, grit'),
 'abrasive-flap-discs': (
  '¿Qué es un disco flap (laminado)?',
  'Es un disco abrasivo formado por láminas de lija traslapadas sobre un respaldo, para pulidora (amoladora angular). Desbasta y da acabado al metal en una sola pasada.',
  '¿Dónde comprar discos flap al mayoreo?', 'el diámetro, el orificio, el grano, el respaldo',
  'What is a flap disc?',
  'It is an abrasive disc made of overlapping abrasive cloth flaps on a backing plate, for angle grinders. It grinds and finishes metal in one pass.',
  'Where can I buy flap discs wholesale?', 'the diameter, bore, grit, backing'),
}
MORE_PRODUCT_FAQ = {
 slug: {'es': [(q1, a1), (q2, BUY_ES.format(x=x1))], 'en': [(q3, a3), (q4, BUY_EN.format(x=x2))]}
 for slug, (q1, a1, q2, x1, q3, a3, q4, x2) in _D.items()
}

ABOUT = {
 'en': ('<h2>More than 20 years making wire brushes</h2>'
        '<p>YEKAI is a wire brush manufacturer in Yongkang, Zhejiang, China\'s hardware manufacturing hub. The factory has been making wire brushes for more than 20 years and today has around 50 workers.</p>'
        '<ul><li><strong>Main lines:</strong> wire cup brushes and wire wheels (knotted and crimped), shank-mounted brushes, wire weed brushes for brush cutters, abrasive nylon brushes and flap discs.</li>'
        '<li><strong>Private label:</strong> blister card, colour box or plain carton with your brand.</li>'
        '<li><strong>Terms:</strong> EXW, FOB or CIF; DDP to Mexico on request.</li></ul>'
        '<h2>Wire materials and quality control</h2>'
        '<p>We make brushes in carbon steel, copper-coated steel, stainless steel (304 and 201) and brass wire. Brushes are checked on a balancing tester and every production batch is sampled before shipment.</p>'
        '<h2>Certificates, test report and patents</h2><p>Open each document to see the products and models it covers.</p><div class="doc-mini-grid"><a class="doc-mini" href="/documents/ce-marked-document.pdf" rel="noopener" target="_blank"><img alt="CE-marked assessment document" height="800" loading="lazy" src="/images/evidence/ce-marked-document.webp" width="566"/><span>CE-marked assessment document</span></a><a class="doc-mini" href="/documents/rohs-document.pdf" rel="noopener" target="_blank"><img alt="RoHS assessment document" height="800" loading="lazy" src="/images/evidence/rohs-document.webp" width="566"/><span>RoHS assessment document</span></a><a class="doc-mini" href="/documents/ul-test-report.pdf" rel="noopener" target="_blank"><img alt="UL 62841-1 test report" height="800" loading="lazy" src="/images/evidence/ul-test-report.webp" width="566"/><span>UL 62841-1 test report</span></a><a class="doc-mini" href="/documents/wire-wheel-patent.pdf" rel="noopener" target="_blank"><img alt="Twisted wire wheel utility model patent" height="800" loading="lazy" src="/images/evidence/wire-wheel-patent.webp" width="566"/><span>Twisted wire wheel utility model patent</span></a><a class="doc-mini" href="/documents/trimmer-design-patent.pdf" rel="noopener" target="_blank"><img alt="Trimmer head design patent" height="800" loading="lazy" src="/images/evidence/trimmer-design-patent.webp" width="566"/><span>Trimmer head design patent</span></a></div>'
        '<h2>Export markets</h2>'
        '<p>We export every year. India is one of our largest markets, alongside Russia and Japan, and we also supply many trading companies, so YEKAI brushes reach buyers in most regions of the world. We are now developing Mexico and Latin America and welcome new distributors in every country.</p>'
        '<h2>Trade shows</h2>'
        '<p>You can meet us in person. Every year we exhibit at the China International Hardware Show in Shanghai and at the Yiwu fair, we have exhibited at the Canton Fair in the last two years, and each year we plan a show abroad, such as Indonesia.</p>'
        '<div class="about-photos"><img alt="YEKAI booth at a hardware trade show" height="1200" loading="lazy" src="/images/evidence/exhibition-booth.webp" width="1600"/><img alt="Buyers visiting the YEKAI booth" height="1600" loading="lazy" src="/images/evidence/exhibition-visitors.webp" width="1200"/></div>'
        '<p>Want to choose products first? See the <a href="/guides/">wire brush buyer guides</a> or the <a href="/#documents">factory documents and certificates</a>.</p>'),
 'es': ('<h2>Más de 20 años fabricando cepillos de alambre</h2>'
        '<p>YEKAI es un fabricante de cardas y cepillos de alambre en Yongkang, Zhejiang, la zona ferretera de China. La fábrica lleva más de 20 años produciendo cepillos de alambre y hoy cuenta con alrededor de 50 trabajadores.</p>'
        '<ul><li><strong>Líneas principales:</strong> cardas copa y circulares (trenzadas y onduladas), cardas con vástago, cepillos de alambre para desbrozadora, cepillos de nylon abrasivo y discos flap.</li>'
        '<li><strong>Marca propia:</strong> blíster con tarjeta, caja a color o caja sencilla con tu marca.</li>'
        '<li><strong>Condiciones:</strong> EXW, FOB o CIF; DDP a México bajo cotización.</li></ul>'
        '<h2>Materiales y control de calidad</h2>'
        '<p>Fabricamos cardas en alambre de acero al carbono, acero cobrizado, acero inoxidable (304 y 201) y latón. Las cardas se revisan en un equipo de balanceo y se muestrea cada lote de producción antes del embarque.</p>'
        '<h2>Certificados, informe de ensayo y patentes</h2><p>Abre cada documento para ver los productos y modelos que cubre.</p><div class="doc-mini-grid"><a class="doc-mini" href="/documents/ce-marked-document.pdf" rel="noopener" target="_blank"><img alt="Documento de evaluación con marcado CE" height="800" loading="lazy" src="/images/evidence/ce-marked-document.webp" width="566"/><span>Documento de evaluación con marcado CE</span></a><a class="doc-mini" href="/documents/rohs-document.pdf" rel="noopener" target="_blank"><img alt="Documento de evaluación RoHS" height="800" loading="lazy" src="/images/evidence/rohs-document.webp" width="566"/><span>Documento de evaluación RoHS</span></a><a class="doc-mini" href="/documents/ul-test-report.pdf" rel="noopener" target="_blank"><img alt="Informe de ensayo UL 62841-1" height="800" loading="lazy" src="/images/evidence/ul-test-report.webp" width="566"/><span>Informe de ensayo UL 62841-1</span></a><a class="doc-mini" href="/documents/wire-wheel-patent.pdf" rel="noopener" target="_blank"><img alt="Patente de modelo de utilidad del disco trenzado" height="800" loading="lazy" src="/images/evidence/wire-wheel-patent.webp" width="566"/><span>Patente de modelo de utilidad del disco trenzado</span></a><a class="doc-mini" href="/documents/trimmer-design-patent.pdf" rel="noopener" target="_blank"><img alt="Patente de diseño del cabezal para desbrozadora" height="800" loading="lazy" src="/images/evidence/trimmer-design-patent.webp" width="566"/><span>Patente de diseño del cabezal para desbrozadora</span></a></div>'
        '<h2>Mercados de exportación</h2>'
        '<p>Exportamos todos los años. India es uno de nuestros mercados más grandes, junto con Rusia y Japón, y también surtimos a muchas comercializadoras, por lo que los cepillos YEKAI llegan a compradores de casi todo el mundo. Ahora estamos desarrollando México y Latinoamérica y buscamos distribuidores en cada país.</p>'
        '<h2>Ferias</h2>'
        '<p>Puedes conocernos en persona. Cada año exponemos en la feria internacional de ferretería de Shanghái (China International Hardware Show) y en la feria de Yiwu; en los últimos dos años estuvimos en la Feria de Cantón, y cada año preparamos una feria en el extranjero, como Indonesia.</p>'
        '<div class="about-photos"><img alt="Stand de YEKAI en una feria de ferretería" height="1200" loading="lazy" src="/images/evidence/exhibition-booth.webp" width="1600"/><img alt="Compradores visitando el stand de YEKAI" height="1600" loading="lazy" src="/images/evidence/exhibition-visitors.webp" width="1200"/></div>'
        '<p>¿Prefieres elegir producto primero? Revisa las <a href="/es/guias/">guías de compra</a> o los <a href="/es/#documents">documentos y certificados de la fábrica</a>.</p>'),
}
ABOUT_META = {
 'en': ('Wire Brush Factory in Yongkang, China | About YEKAI',
        'YEKAI wire brush factory in Yongkang, China: 20+ years, about 50 workers, exporting to India, Russia, Japan and worldwide. See trade shows and order terms.'),
 'es': ('Fábrica de cardas en Yongkang, China | Sobre YEKAI',
        'Fábrica YEKAI en Yongkang, China: más de 20 años, unos 50 trabajadores, exporta a India, Rusia, Japón y más países. Conoce ferias y condiciones de pedido.'),
}

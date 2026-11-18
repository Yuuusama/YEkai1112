"""2026-11-16 — 5 guías nuevas en español + preguntas frecuentes (FAQ) para las 8 guías.
Lo importa scripts/seo_mx_20261116.py. Sólo usa datos que ya están en las páginas de producto
(medidas, alambre, haces, grano, condiciones de empaque); no agrega precios, plazos ni RPM.
"""
P = lambda s: f'<p>{s}</p>'
def link(path, label): return f'<a href="{path}">{label}</a>'
PR = '/es/products/'

MORE_GUIDES = [
 ('carda-para-soldadura', 'Carda para limpiar soldadura: cuál elegir'),
 ('carda-para-quitar-oxido-y-pintura', 'Carda para quitar óxido y pintura'),
 ('cepillo-para-desbrozadora', 'Cepillo de alambre para desbrozadora: cómo elegir'),
 ('cepillo-de-nylon-abrasivo', 'Cepillo de nylon abrasivo: usos y grano'),
 ('cardas-con-tu-marca', 'Cardas con tu marca: empaque OEM'),
]

MORE_CONTENT = {
'carda-para-soldadura': dict(
 title='Carda para limpiar soldadura: cuál elegir',
 h1='Carda para limpiar soldadura: qué tipo usar en cada trabajo',
 desc='Qué carda usar para limpiar cordones de soldadura, escoria y salpicaduras: trenzada angosta, copa, cónica o de punta. Guía para talleres y ferreterías.',
 body=[
  P('Para limpiar soldadura se usa casi siempre <strong>carda de alambre trenzado</strong>: es más rígida que la ondulada y quita escoria, salpicaduras y cascarilla sin tener que desbastar el metal. Lo que cambia de un trabajo a otro es la <strong>forma</strong> de la carda.'),
  '<h2>Cordón de soldadura y raíz: carda trenzada angosta</h2>',
  P('La ' + link(PR + 'stringer-knotted-wheels/', 'carda trenzada angosta para soldadura') + ' tiene haces finos que entran a lo largo del cordón y en biseles estrechos. En nuestra serie es de acero al carbono, con alambre típico de 0.5 mm y diámetros de 4.5, 5, 6 y 7 pulgadas. Para cotizar indica el ancho de trabajo y el orificio central.'),
  '<h2>Placas y superficies amplias: carda copa trenzada</h2>',
  P('Para limpiar alrededor de la soldadura en lámina, placa o perfiles, la carda copa trabaja con la cara y cubre más área: ' + link(PR + 'red-knotted-wire-cup-brush/', 'carda copa trenzada') + ' o ' + link(PR + 'banded-twisted-cup-brushes/', 'carda copa trenzada con aro') + ', que mantiene los haces más cerrados.'),
  '<h2>Esquinas y soldadura en ángulo: carda cónica</h2>',
  P('La ' + link(PR + 'twisted-wire-wheels/', 'carda cónica trenzada') + ' tiene los haces inclinados y llega a filetes, esquinas y bordes donde la copa no entra. Serie de 4, 4.5 y 5 pulgadas, alambre típico de 0.5 mm.'),
  '<h2>Huecos, tubo y zonas pequeñas: carda de punta para taladro</h2>',
  P('Donde no cabe la pulidora (amoladora), se usa una ' + link(PR + 'shaft-mounted-wire-wheels/', 'carda con vástago') + '. Las de punta trenzadas van de 19 a 30 mm de cabezal.'),
  '<h2>Retoque a mano</h2>',
  P('Entre pasadas de soldadura o para un retoque rápido sirve el ' + link(PR + 'plastic-handle-hand-brushes/', 'cepillo de alambre con mango') + '.'),
  '<h2>Resumen</h2>',
  '<table class="guide-table"><thead><tr><th>Trabajo</th><th>Carda</th></tr></thead><tbody>'
  '<tr><td>Cordón, raíz, bisel</td><td>Trenzada angosta, 4.5 a 7"</td></tr>'
  '<tr><td>Placa y superficie alrededor</td><td>Copa trenzada (con o sin aro)</td></tr>'
  '<tr><td>Filete, esquina, borde</td><td>Cónica trenzada, 4 a 5"</td></tr>'
  '<tr><td>Hueco, interior de tubo</td><td>De punta con vástago, para taladro</td></tr></tbody></table>',
  '<h2>Seguridad</h2>',
  P('La velocidad máxima (RPM) de la carda debe ser igual o mayor que la de la máquina. Usa guarda, lentes o careta y guantes: los alambres pueden desprenderse. Confirma con Frank las RPM del modelo que elijas.'),
 ]),

'carda-para-quitar-oxido-y-pintura': dict(
 title='Carda para quitar óxido y pintura: cuál usar',
 h1='Carda para quitar óxido y pintura: cómo elegir',
 desc='Qué carda usar para quitar óxido, pintura y sarro del metal: ondulada o trenzada, de copa, circular o para taladro, y cuándo conviene nylon abrasivo.',
 body=[
  P('La carda quita óxido, pintura vieja y suciedad <strong>sin comerse el metal</strong>, por eso se usa antes de pintar o soldar. La elección depende de qué tan pegado está lo que hay que quitar y de la forma de la pieza.'),
  '<h2>Según qué tan pesado es el trabajo</h2>',
  '<table class="guide-table"><thead><tr><th>Situación</th><th>Tipo de alambre</th></tr></thead><tbody>'
  '<tr><td>Óxido superficial, pintura suelta, limpieza general</td><td>Ondulado: más flexible, acabado más parejo</td></tr>'
  '<tr><td>Óxido grueso, sarro, cascarilla, pintura muy adherida</td><td>Trenzado: más rígido y agresivo</td></tr>'
  '<tr><td>Piezas que no deben rayarse, acabado fino</td><td>Nylon abrasivo en lugar de alambre</td></tr></tbody></table>',
  P('La diferencia completa está en ' + link('/es/guias/carda-trenzada-o-ondulada/', '¿carda trenzada u ondulada?') + '.'),
  '<h2>Según la forma de la pieza</h2>',
  P('<strong>Superficies planas y grandes</strong> (lámina, portones, estructuras): carda copa en la pulidora o amoladora. Ondulada: ' + link(PR + 'crimped-wire-cup-brushes/', 'carda copa ondulada') + ', de 2.5 a 6 pulgadas. Trenzada: ' + link(PR + 'red-knotted-wire-cup-brush/', 'carda copa trenzada') + '.'),
  P('<strong>Piezas sueltas en el esmeril de banco</strong> (herramienta, tornillería, partes): ' + link(PR + 'wide-crimped-wire-wheels/', 'carda circular ancha ondulada') + ', de 4 a 12 pulgadas, o ' + link(PR + 'copper-coated-wire-wheels/', 'carda circular de alambre cobrizado') + '.'),
  P('<strong>Esquinas y bordes</strong>: ' + link(PR + 'twisted-wire-wheels/', 'carda cónica trenzada') + '.'),
  P('<strong>Huecos, rejas y zonas pequeñas</strong>: ' + link(PR + 'shaft-mounted-wire-wheels/', 'cardas con vástago para taladro') + ' (de punta, circulares y de copa).'),
  P('<strong>Retoques a mano</strong>: ' + link(PR + 'plastic-handle-hand-brushes/', 'cepillo de alambre con mango') + '.'),
  '<h2>Cuándo usar nylon abrasivo o disco flap</h2>',
  P('Si la pieza no debe quedar rayada, el ' + link(PR + 'abrasive-filament-brushes/', 'cepillo de nylon abrasivo') + ' quita óxido, corrosión, pintura e imprimación con menos marca. Si además hay que rebajar material o emparejar una soldadura, eso ya es trabajo de ' + link(PR + 'abrasive-flap-discs/', 'disco flap (laminado)') + ', no de carda.'),
  '<h2>Para ferreterías: qué surtir primero</h2>',
  P('Los usos de óxido y pintura se cubren con pocas piezas: copa ondulada y copa trenzada para pulidora, una carda circular para esmeril y un juego con vástago para taladro. Se pueden entregar ' + link(PR + 'blister-card-brush-sets/', 'en blíster con tarjeta') + ' para colgar en exhibidor.'),
  '<h2>Seguridad</h2>',
  P('Revisa que las RPM máximas de la carda sean iguales o mayores que las de la máquina, y usa guarda, lentes y guantes. Confirma las RPM de cada modelo con Frank.'),
 ]),

'cepillo-para-desbrozadora': dict(
 title='Cepillo de alambre para desbrozadora: cómo elegir',
 h1='Cepillo de alambre para desbrozadora: tipos y cómo elegir',
 desc='Cepillos de alambre y de nylon para desbrozadora, desmalezadora o guadaña: quitar maleza de adoquines y banquetas. Diámetros, haces y montaje.',
 body=[
  P('El cepillo para <strong>desbrozadora</strong> (también llamada desmalezadora, guadaña, bordeadora u orilladora, según el país) sustituye al hilo o a la cuchilla para <strong>quitar maleza y musgo de juntas de adoquín, banquetas, guarniciones y pisos de concreto</strong>, sin herbicida. Hay tres familias en nuestro catálogo.'),
  '<h2>1. Cepillo de alambre trenzado</h2>',
  P('Es el más agresivo: haces de acero al carbono trenzado, alambre de 0.5 mm. La ' + link(PR + 'twisted-wire-grass-trimmer-heads/', 'serie trenzada') + ' se publica en 6 pulgadas con 24 o 30 haces y en 8 pulgadas con 30 o 36 haces. Más haces significa un cepillo más cerrado.'),
  '<h2>2. Cabezal de 3 o 6 haces</h2>',
  P('Los ' + link(PR + '3-and-6-bundle-wire-trimmer-heads/', 'cabezales de 3 y 6 haces') + ' vienen en 150, 180, 200 y 230 mm. Hay dos versiones según la máquina: <strong>orificio de 5.5 mm para desbrozadoras de batería</strong> (inalámbricas) y <strong>orificio de 25.4 mm para desbrozadoras a gasolina</strong>. Indica cuál usas.'),
  '<h2>3. Cepillo de nylon</h2>',
  P('El ' + link(PR + 'nylon-grass-trimmer-brushes/', 'cepillo de nylon para desbrozadora') + ' lleva filamento de nylon de sección rectangular, en 6 y 8 pulgadas, con orificio de referencia de 22.5 mm. Se elige cuando la superficie es más delicada y no conviene rayarla con acero.'),
  '<h2>Comparación</h2>',
  '<table class="guide-table"><thead><tr><th>Tipo</th><th>Medidas publicadas</th><th>Para qué</th></tr></thead><tbody>'
  '<tr><td>Alambre trenzado</td><td>6" (24 o 30 haces), 8" (30 o 36 haces)</td><td>Maleza dura en concreto y adoquín resistente</td></tr>'
  '<tr><td>3 o 6 haces</td><td>150, 180, 200, 230 mm</td><td>Batería (orificio 5.5 mm) o gasolina (orificio 25.4 mm)</td></tr>'
  '<tr><td>Nylon</td><td>6" y 8", orificio 22.5 mm</td><td>Superficies que no deben rayarse</td></tr></tbody></table>',
  '<h2>El montaje es lo que más devoluciones causa</h2>',
  P('No existe un ajuste universal. Antes de pedir, manda <strong>marca y modelo de la desbrozadora</strong>, el <strong>diámetro del orificio</strong> o del eje y, si puedes, una foto del cabezal actual. Frank confirma el cabezal, el adaptador y las RPM seguras para ese modelo.'),
  '<h2>Seguridad</h2>',
  P('El cepillo de acero lanza piedras y puede soltar alambres: se trabaja con la guarda puesta, careta, pantalón largo y calzado cerrado, y sin personas cerca. En adoquín o loseta que se raya fácil, prueba primero en una zona poco visible o usa nylon.'),
  '<h2>Para distribuidores</h2>',
  P('Es un producto de temporada de lluvias y de mantenimiento municipal y de jardinería. Se puede entregar con tu marca y en empaque individual; revisa ' + link('/es/guias/cardas-con-tu-marca/', 'cómo funciona el empaque OEM') + ' o ve la categoría de ' + link('/es/wire-grass-trimmer-head/', 'cepillos para desbrozadora') + '.'),
 ]),

'cepillo-de-nylon-abrasivo': dict(
 title='Cepillo de nylon abrasivo: usos, grano y formas',
 h1='Cepillo de nylon abrasivo: para qué sirve y qué grano elegir',
 desc='Para qué sirve el cepillo de nylon (filamento) abrasivo, diferencia con la carda de alambre, grano 80 a 320, óxido de aluminio o carburo de silicio.',
 body=[
  P('El <strong>cepillo de nylon abrasivo</strong> (también carda de nylon o cepillo de filamento abrasivo) tiene cerdas de nylon con grano abrasivo mezclado en todo el filamento. Conforme se gasta, va exponiendo grano nuevo, así que el acabado se mantiene parejo.'),
  '<h2>Para qué sirve</h2>',
  P('Nuestro catálogo lo indica para <strong>quitar óxido, corrosión, pintura e imprimación y limpiar superficies</strong>. Frente a la carda de alambre, marca menos la pieza y no deja restos de acero. También se usa en madera para limpiar y resaltar la veta; en ese caso conviene confirmar el grano con una muestra.'),
  '<h2>Nylon abrasivo o carda de alambre</h2>',
  '<table class="guide-table"><thead><tr><th></th><th>Nylon abrasivo</th><th>Carda de alambre</th></tr></thead><tbody>'
  '<tr><th>Acción</th><td>Más suave y pareja</td><td>Más agresiva</td></tr>'
  '<tr><th>Marca en la pieza</th><td>Menor</td><td>Mayor</td></tr>'
  '<tr><th>Trabajo típico</th><td>Acabado, limpieza fina, piezas delicadas</td><td>Óxido pesado, escoria, soldadura</td></tr></tbody></table>',
  '<h2>Formas y medidas del catálogo</h2>',
  '<ul><li><strong>Circular (disco):</strong> 75 a 200 mm</li><li><strong>Copa:</strong> 75 a 125 mm</li><li><strong>Circular con vástago:</strong> 38 a 100 mm</li><li><strong>Copa con vástago:</strong> 40 a 80 mm</li></ul>',
  P('Los modelos con vástago listados son de 6 mm, para taladro. Orificios y roscas de las copas se confirman con Frank. Ver todos los modelos en ' + link(PR + 'abrasive-filament-brushes/', 'cepillos de nylon abrasivo') + '.'),
  '<h2>Qué grano elegir</h2>',
  P('El catálogo cubre grano <strong>80 a 320</strong>. Número más bajo: más agresivo, quita más rápido. Número más alto: acabado más fino. El <strong>grano 80 es el más pedido</strong> para limpieza general y para madera; 120 deja un acabado un poco más fino, y 240 o 320 se usan para acabado.'),
  '<h2>Óxido de aluminio (AO) o carburo de silicio (SiC)</h2>',
  P('El catálogo ofrece las dos opciones según el modelo. Ojo: <strong>el color del cepillo no identifica por sí solo el abrasivo ni el grano</strong>; pide siempre el dato por escrito para el modelo que elijas.'),
  '<h2>Qué mandar para cotizar</h2>',
  '<ul><li>Material de la pieza (acero, aluminio, madera…) y acabado que buscas</li><li>Máquina: pulidora o amoladora, taladro, esmeril</li><li>Forma y diámetro</li><li>Grano y abrasivo, si ya lo tienes definido</li><li>Cantidad por modelo</li></ul>',
 ]),

'cardas-con-tu-marca': dict(
 title='Cardas con tu marca: empaque OEM y pedido mínimo',
 h1='Cardas con tu marca: cómo funciona el empaque OEM',
 desc='Cómo pedir cardas y cepillos de alambre con tu propia marca: blíster con tarjeta, caja a color, costo de placa de impresión y pedido de 5,000 piezas.',
 body=[
  P('Si tienes ferretería, distribuidora o marca propia de herramienta, puedes pedir las cardas <strong>con tu logotipo y tu empaque</strong> directo de fábrica. Así se arma el pedido en YEKAI.'),
  '<h2>Tipos de empaque</h2>',
  '<ul><li><strong>Blíster con tarjeta</strong> (sencillo o doble blíster): para colgar en exhibidor</li><li><strong>Caja a color</strong>: para anaquel y venta por pieza</li><li><strong>Caja de cartón sencilla</strong>: para mayoreo y uso industrial</li></ul>',
  P('También se arman ' + link(PR + 'blister-card-brush-sets/', 'juegos de cardas en blíster') + ': tú defines los modelos y las piezas por tarjeta.'),
  '<h2>Costo de la placa de impresión</h2>',
  P('La impresión personalizada tiene un cargo de <strong>300 RMB por placa</strong> (por diseño). Ese cargo <strong>se bonifica</strong> en pedidos de al menos <strong>5,000 piezas en total</strong> que combinan de 2 a 4 modelos en una misma plancha de impresión.'),
  '<h2>Pedido de prueba</h2>',
  P('Si primero quieres probar el producto, aceptamos pedidos pequeños con empaque estándar, sin personalizar. En esos pedidos no aplica el precio de mayoreo y el flete por pieza sale más alto.'),
  '<h2>Paso a paso</h2>',
  '<ol><li>Elige modelos y medidas (' + link('/es/guias/medidas-de-carda/', 'qué medidas mandar') + ').</li><li>Pide muestras para revisar alambre, montaje y acabado.</li><li>Manda tu arte: logotipo en vectores, textos, código de barras y datos del importador que deba llevar la etiqueta en tu país.</li><li>Confirmas el diseño y la distribución por modelo antes de producir.</li><li>Producción y envío en EXW, FOB o CIF; DDP bajo cotización según el país.</li></ol>',
  '<h2>Qué mandar para cotizar</h2>',
  '<ul><li>Modelos, medidas y cantidad por modelo</li><li>Tipo de empaque y piezas por empaque</li><li>Si ya tienes diseño o necesitas adaptar uno</li><li>País y ciudad de destino</li></ul>',
  P('Más detalle del envío en ' + link('/es/guias/importar-cardas-de-china/', 'cómo importar cardas desde China') + '. Fotos de empaques ya hechos en ' + link('/es/#oem', 'empaque OEM') + '.'),
 ]),
}

# Preguntas frecuentes: se muestran al final de cada guía y como FAQPage en JSON-LD
FAQ = {
'carda-trenzada-o-ondulada': [
 ('¿Qué carda es más agresiva, la trenzada o la ondulada?', 'La trenzada. El alambre torcido en haces la hace más rígida; la ondulada es más flexible y deja un acabado más parejo.'),
 ('¿Qué carda se usa en la pulidora o amoladora?', 'La carda copa y la cónica, que van roscadas. La carda circular con orificio se monta normalmente en esmeril de banco.'),
 ('¿Carda y grata son lo mismo?', 'Sí. Según el país se le dice carda, grata o cepillo de alambre; es el mismo producto.'),
],
'medidas-de-carda': [
 ('¿Qué rosca lleva una carda copa para pulidora?', 'Las que más fabricamos son M14 y M10 (paso 1.5 o 1.25; no son intercambiables). La 5/8"-11 se hace sobre pedido. Confírmala antes de pedir.'),
 ('¿Cuántos milímetros son 4.5 pulgadas?', 'Aproximadamente 115 mm. Otras equivalencias: 4" = 100 mm, 5" = 125 mm, 6" = 150 mm, 7" = 175 mm.'),
 ('¿Qué datos necesito para cotizar cardas al mayoreo?', 'Diámetro exterior, montaje (rosca, orificio o vástago), tipo de alambre, cantidad por medida, empaque y destino.'),
],
'importar-cardas-de-china': [
 ('¿Puedo pedir muestras antes de un pedido grande?', 'Sí. Las muestras se envían por avión para revisar alambre, montaje y acabado antes del pedido al mayoreo.'),
 ('¿Qué significa DDP?', 'Entrega puerta a puerta con impuestos de importación incluidos. Se cotiza según país, producto, volumen y ciudad de destino.'),
 ('¿Aceptan pedidos pequeños?', 'Sí, pedidos de prueba con empaque estándar. No aplica precio de mayoreo y el flete por pieza es más alto.'),
],
'carda-para-soldadura': [
 ('¿Qué carda se usa para limpiar soldadura?', 'Carda de alambre trenzado. Para el cordón, la trenzada angosta; para la superficie alrededor, la copa trenzada; para esquinas, la cónica.'),
 ('¿Sirve la carda ondulada para soldadura?', 'Para limpieza ligera sí, pero para escoria y salpicaduras rinde más la trenzada, que es más rígida.'),
 ('¿En qué medidas hay carda trenzada angosta?', 'En nuestra serie: 4.5, 5, 6 y 7 pulgadas, con alambre típico de 0.5 mm de acero al carbono.'),
],
'carda-para-quitar-oxido-y-pintura': [
 ('¿Qué carda es mejor para quitar óxido?', 'Óxido ligero: ondulada. Óxido grueso o sarro: trenzada. En superficies planas se usa la carda copa en la pulidora.'),
 ('¿La carda raya el metal?', 'Deja marca, más la trenzada que la ondulada. Si la pieza no debe rayarse conviene un cepillo de nylon abrasivo.'),
 ('¿Qué carda uso con el taladro?', 'Una carda con vástago: de punta para huecos, circular para bordes o de copa para superficies abiertas.'),
],
'cepillo-para-desbrozadora': [
 ('¿Para qué sirve el cepillo de alambre para desbrozadora?', 'Para quitar maleza y musgo de juntas de adoquín, banquetas y pisos de concreto, sin usar herbicida.'),
 ('¿Le queda a cualquier desbrozadora?', 'No hay ajuste universal. En los cabezales de 3 y 6 haces, el orificio de 5.5 mm es para máquinas de batería y el de 25.4 mm para gasolina. Confirma marca, modelo y orificio antes de pedir.'),
 ('¿Alambre o nylon?', 'Alambre trenzado para maleza dura en superficies resistentes; nylon cuando la superficie no debe rayarse.'),
],
'cepillo-de-nylon-abrasivo': [
 ('¿Para qué sirve el cepillo de nylon abrasivo?', 'Para quitar óxido, corrosión, pintura e imprimación y limpiar superficies, con menos marca que una carda de alambre.'),
 ('¿Qué grano de nylon abrasivo elegir?', 'El catálogo va de 80 a 320. El grano 80 es el más pedido. Número bajo, más agresivo; número alto, acabado más fino.'),
 ('¿El color indica el grano?', 'No. El color no identifica por sí solo el abrasivo ni el grano; hay que confirmarlo para cada modelo.'),
],
'cardas-con-tu-marca': [
 ('¿Cuánto cuesta poner mi marca en el empaque?', '300 RMB por placa de impresión. Se bonifica en pedidos de al menos 5,000 piezas en total con 2 a 4 modelos en una misma plancha.'),
 ('¿Puedo pedir menos de 5,000 piezas?', 'Sí. Con impresión personalizada se cobra la placa; también hay pedidos de prueba con empaque estándar.'),
 ('¿Qué empaques manejan?', 'Blíster con tarjeta, doble blíster, caja a color y caja de cartón sencilla.'),
],
}

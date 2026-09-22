# -*- coding: utf-8 -*-
"""
Dataset de playas de Asturias, organizado por concejo, de oeste a este.
Fuentes: milplayas.com, asturias.com, villadellanes.com, vivirasturias.com (investigación web, septiembre 2026).
dist_km = distancia aproximada en coche desde Gijon (Playa de San Lorenzo) al nucleo del concejo,
calculada con OSRM (router.project-osrm.org), ruta mas directa. Es una aproximación a nivel de concejo:
las playas de un mismo concejo comparten aprox. esa distancia (+/- unos pocos km según su posición exacta).
"""
import json

# (concejo, zona, dist_km, lat, lon_ref, [ (nombre, descripción, tags) ])
# tags posibles: arena-dorada, arena-blanca, arena-oscura, cantos, urbana, rural, dificil-acceso,
# accesible, nudista, perros, surf, buceo, monumento-natural, duna, acantilados, familias

concejos = [
    dict(nombre="Castropol", zona="oeste", dist_km=123.1, lat=43.5636, lon=-6.9636, mareas_slug="castropol", beaches=[
        ("Arnao", "Arena blanca y fina, aguas tranquilas, cerca de la zona recreativa de Arnao.", ["arena-blanca","accesible","familias"]),
        ("Figueras", "Escasa ocupación; da acceso a la playa de San Román en marea baja.", ["cantos","rural"]),
        ("San Román", "Solo accesible a través de Figueras con marea baja.", ["cantos","dificil-acceso","rural"]),
    ]),
    dict(nombre="Tapia de Casariego", zona="oeste", dist_km=120.1, lat=43.5709, lon=-6.9430, mareas_slug="tapia-de-casariego", beaches=[
        ("El Figo / El Figu", "Pequeña cala de piedras en entorno rocoso con acantilados, difícil acceso.", ["cantos","dificil-acceso"]),
        ("El Murallón", "Pequeña playa junto a Playa Grande, buenos servicios y alta ocupación.", ["urbana","accesible"]),
        ("La Grande / Anguileiro / Los Campos", "Extenso arenal con buenos servicios; sede de un campeonato de surf.", ["arena-dorada","surf","urbana","accesible"]),
        ("La Paloma / Esteiro", "Arena fina en entorno agreste.", ["arena-dorada","rural"]),
        ("La Reburdia", "Pequeña playa de arena fina entre acantilados, muy local.", ["arena-dorada","rural"]),
        ("Mexota / A Mixota", "Aguas cristalinas con un islote que la divide en dos.", ["arena-dorada","rural"]),
        ("Pantorgas / Santa Gadea / Ribeiria", "Recogida entre acantilados, arena fina dorada, islotes con especies protegidas; apta para pesca submarina y surf.", ["arena-dorada","surf","buceo","dificil-acceso"]),
        ("Peñarronda", "Amplio arenal con un peñasco central, muy popular entre surfistas.", ["arena-dorada","surf","accesible"]),
        ("Porcía (Tapia)", "Pequeña playa de buenos servicios en entorno atractivo, en el límite con El Franco.", ["arena-dorada","accesible"]),
        ("Represas", "Poco atractivo, entre acantilados y sin servicios.", ["cantos","dificil-acceso"]),
        ("Sarello / Sareyo", "Amplio arenal junto a Serantes, paisaje rural entre prados y arena dorada.", ["arena-dorada","rural"]),
        ("Serantes", "Playa rustica de gran anchura, arena fina dorada, tranquila.", ["arena-dorada","rural"]),
    ]),
    dict(nombre="El Franco", zona="oeste", dist_km=111.3, lat=43.5750, lon=-6.8100, mareas_slug="viavelez", beaches=[
        ("Cambaredo", "Playa rocosa, estrecha y alargada, alto valor ecológico, poco frecuentada.", ["cantos","dificil-acceso","rural"]),
        ("Castelo / Castello", "Cala de cantos de cuarcita y pizarra, gran interes geológico.", ["cantos","dificil-acceso"]),
        ("Monellos", "Pequeña cala rocosa al oeste de Viavélez, rodeada de acantilados bajos.", ["cantos","dificil-acceso"]),
        ("Porcía (El Franco)", "Forma triangular, alta ocupación en temporada, marismas y pequeñas dunas.", ["arena-dorada","duna","accesible"]),
        ("Pormenande", "Rocosa pero segura, unida al islote de El Rego por una barra natural, ruta de senderismo.", ["cantos","rural"]),
        ("Torbas (El Franco)", "Pequeña cala junto a Cabo Blanco, paisaje y aguas de gran calidad.", ["cantos","dificil-acceso"]),
    ]),
    dict(nombre="Coaña", zona="oeste", dist_km=107.8, lat=43.5636, lon=-6.7635, mareas_slug="ortiguera", beaches=[
        ("A Figueira", "Playa rocosa típica de la costa occidental, casi desaparece en pleamar.", ["cantos","dificil-acceso"]),
        ("Armazá", "Aislada y rocosa, con un mirador en lo alto de la Punta del Castello.", ["cantos","dificil-acceso"]),
        ("Arnelles", "Cerca del puerto de Ortiguera, con algunos servicios basicos.", ["cantos","accesible"]),
        ("El Barco", "Pequeña y aislada, difícil acceso, sin servicios.", ["cantos","dificil-acceso"]),
        ("Foxos / Ortiguera", "En la desembocadura del río Navia.", ["arena-dorada","rural"]),
        ("Torbas (Coana)", "Extensa playa de cantos y arena en entorno rural.", ["cantos","rural"]),
    ]),
    dict(nombre="Navia", zona="oeste", dist_km=102.5, lat=43.5443, lon=-6.7192, mareas_slug="navia", beaches=[
        ("Coedo", "Recondita cala pequeña de canto rodado y arena, cerca de Andés.", ["cantos","dificil-acceso"]),
        ("El Moro / Peñafurada", "Junto a la playa de Navia, arena oscura gruesa, ocupación media.", ["arena-oscura"]),
        ("Fabal", "Pequeña cala en forma de concha entre acantilados, oleaje fuerte.", ["cantos","dificil-acceso"]),
        ("Frejulfe / Frexulfe", "Extenso arenal con sistema dunar junto a Puerto de Vega, oleaje fuerte.", ["arena-oscura","duna","surf"]),
        ("La Losera", "Pequeña cala de canto y piedra al oeste de Puerto de Vega.", ["cantos","dificil-acceso"]),
        ("Navia", "Playa urbana en la desembocadura del río Navia, buenos servicios.", ["arena-dorada","urbana","accesible"]),
    ]),
    dict(nombre="Valdés", zona="oeste", dist_km=86.0, lat=43.5445, lon=-6.5339, mareas_slug="luarca", beaches=[
        ("Barayo / La Vega", "Playa virgen de 670 m dentro de la Reserva Natural Parcial de Barayo, estuario del río Barayo.", ["arena-dorada","monumento-natural","duna"]),
        ("Bozo", "Cala aislada de bolos junto a Cabo Busto, oleaje moderado.", ["cantos","dificil-acceso"]),
        ("Cadavedo / La Ribeirona", "Rural, forma de concha, alta ocupación en verano.", ["arena-dorada","rural"]),
        ("Campiecho", "Cala de bolos aislada, apenas visitada.", ["cantos","dificil-acceso"]),
        ("Carretón / Cabretón", "Aislada, acceso a pie difícil, bolos.", ["cantos","dificil-acceso"]),
        ("Castiel", "Cala rocosa encajonada entre acantilados, acceso muy difícil.", ["cantos","dificil-acceso"]),
        ("Choureu", "Cala rocosa entre la Punta de Santa Ana y la Punta La Osa.", ["cantos","dificil-acceso"]),
        ("Chousera", "Pequeña playa de bolos, oleaje fuerte, poco visitada.", ["cantos","dificil-acceso"]),
        ("Churín / Serón", "Acceso muy difícil, bolos, oleaje fuerte, apenas usada.", ["cantos","dificil-acceso"]),
        ("Cueva / La Arena", "Mas frecuentada por estar cerca de un nucleo de población.", ["arena-dorada"]),
        ("El Serrón", "Playa de cantos al norte de Cabo Busto, bajo un gran acantilado.", ["cantos","dificil-acceso"]),
        ("Fontanecha", "Pequeña, acceso por acantilado de 75 m, apenas usada salvo por pescadores.", ["cantos","dificil-acceso"]),
        ("La Escaladina", "Pequeña cala rocosa, oleaje fuerte, poco visitada.", ["cantos","dificil-acceso"]),
        ("La Herbosa", "Acceso difícil y oleaje fuerte, uso mínimo.", ["cantos","dificil-acceso"]),
        ("Las Arreas", "Al este del faro de Luarca, afectada por vertidos urbanos.", ["cantos","urbana"]),
        ("Los Molinos", "Aislada, abrupta, difícil acceso a pie, frecuentada por pescadores.", ["cantos","dificil-acceso"]),
        ("Los Molinos / Cutin", "Al este de Cabo Busto, difícil acceso, uso de pescadores.", ["cantos","dificil-acceso"]),
        ("Otur", "Playa de arena al oeste de Luarca, sistema dunar degradado, alta ocupación.", ["arena-dorada","duna","accesible"]),
        ("Perceberos / La Estaca", "Entorno protegido de gran valor paisajístico, acceso complicado.", ["cantos","dificil-acceso"]),
        ("Picón", "Pequeña y bonita cala de bolos, oleaje fuerte, poca visita.", ["cantos","dificil-acceso"]),
        ("Plumineru / Quintana", "Aislada y tranquila, bolos, oleaje fuerte, sin servicios.", ["cantos","dificil-acceso"]),
        ("Portizuelo", "Bello entorno rocoso y de acantilados, mas frecuentada que sus vecinas.", ["cantos"]),
        ("Primera y Segunda de Luarca", "Playa urbana de Luarca, gran actividad turística en verano, buenos servicios.", ["arena-dorada","urbana","accesible"]),
        ("Punxeo / El Ferreiro", "Dentro de espacio costero protegido, pocos visitantes, sin infraestructura.", ["cantos","dificil-acceso"]),
        ("Ribón", "Playa bonita, servicios minimos, baja ocupación, acantilados altos.", ["cantos"]),
        ("Sabugo", "Forma de concha, arena oscura, oleaje fuerte, acceso a pie desde la base del acantilado.", ["arena-oscura","dificil-acceso"]),
    ]),
    dict(nombre="Cudillero", zona="oeste", dist_km=55.4, lat=43.5644, lon=-6.1466, mareas_slug="cudillero", beaches=[
        ("Albuerne", "Cantos y arena, encajonada entre acantilados de mas de 50 m.", ["cantos","dificil-acceso"]),
        ("Calabon", "Difícil acceso, islotes y formaciones rocosas en su sector oeste.", ["cantos","dificil-acceso"]),
        ("El Aguaduz", "Calas y zonas rocosas con vegetación en el sector oeste.", ["cantos","dificil-acceso"]),
        ("El Castrillon", "Pequeña y tranquila entre dos puntas, sin servicios.", ["cantos","rural"]),
        ("El Castro / Caldeirina", "Cala de difícil acceso a través de un valle fluvial.", ["cantos","dificil-acceso"]),
        ("El Riego", "Pequeña cala rocosa con tres formaciones rocosas notables, sin servicios.", ["cantos","dificil-acceso"]),
        ("El Silencio / Gaviero / Gavieiru", "Posiblemente la playa mas bonita del occidente asturiano, virgen y con espectaculares islotes.", ["cantos","monumento-natural","dificil-acceso"]),
        ("Gradas", "Junto a acantilados imponentes al este de Cabo Vidio.", ["cantos","dificil-acceso"]),
        ("Gueirua / Gairúa", "Entorno muy fotogénico, baja ocupación, sin servicios.", ["arena-dorada","dificil-acceso"]),
        ("L'Airin", "Extenso arenal de canto rodado de colores, separada por el islote Farinon.", ["cantos"]),
        ("La Barquera", "Paisaje protegido, destaca por su riqueza pesquera.", ["cantos","rural"]),
        ("La Concha de Artedo", "Extensa y resguardada, aguas cristalinas, alta ocupación.", ["arena-dorada","accesible","familias"]),
        ("La Corvera", "Pequeña, entorno atractivo, baja ocupación, difícil acceso.", ["cantos","dificil-acceso"]),
        ("La Cueva", "De bolos, se accede por un sendero de mas de 80 m de acantilado.", ["cantos","dificil-acceso"]),
        ("Las Rubias", "Bonita y aislada, baja ocupación por su difícil acceso.", ["cantos","dificil-acceso"]),
        ("Los Botes", "Pequeña cala aislada, bolos, oleaje fuerte, sin servicios.", ["cantos","dificil-acceso"]),
        ("Oleiros", "Rodeada de pinares, oleaje fuerte pese a sus aguas limpias.", ["cantos","rural"]),
        ("Peña Doria", "Pequeña, malas condiciones de baño por oleaje y viento.", ["cantos","dificil-acceso"]),
        ("Portiella / Muriello", "Pequeña cala con zona marisquera.", ["cantos"]),
        ("Puerto Chico (Cudillero)", "Diminuta cala entre acantilados, baja ocupación, sin servicios.", ["cantos","dificil-acceso"]),
        ("Pumarín", "En la localidad de Santa Marina, zona oeste del concejo.", ["cantos","rural"]),
        ("Ribera del Molin", "Rural y tranquila, de bolos, oleaje fuerte.", ["cantos","rural"]),
        ("Río Cabo / Ballota (Cudillero)", "En la desembocadura de un río que marca el límite del concejo.", ["cantos","rural"]),
        ("Salencia", "Pequeña playa rural donde un arroyo llega al mar.", ["cantos","rural"]),
        ("San Pedro de Bocamar / San Pedro de la Ribera", "Ubicación aislada pero alta ocupación, buenos servicios.", ["arena-dorada","accesible"]),
        ("Sancidiello", "Junto a acantilados imponentes al este de Cabo Vidio.", ["cantos","dificil-acceso"]),
    ]),
    dict(nombre="Soto del Barco", zona="oeste", dist_km=45.0, lat=43.5766, lon=-6.0561, mareas_slug="san-juan-de-la-arena", beaches=[
        ("Los Quebrantos", "Extensa playa de arena oscura de 810 m unida al Playon de Bayas, con la desembocadura del Nalon; buenos servicios y apta para surf.", ["arena-oscura","surf","accesible","familias"]),
    ]),
    dict(nombre="Muros de Nalón", zona="oeste", dist_km=47.5, lat=43.5606, lon=-6.0961, mareas_slug="san-esteban", beaches=[
        ("Aguilar", "Amplia playa de arena, muy turística, buenos servicios y oferta gastronomica.", ["arena-dorada","urbana","accesible","familias"]),
        ("Campofrio", "Al pie de acantilados con vegetación, se extiende al oeste de Aguilar, comparte paseo y servicios.", ["arena-dorada","accesible"]),
        ("Cazonera", "Rocosa, de bolos, separada de La Atalaya por pequeños islotes, sin servicios.", ["cantos","dificil-acceso"]),
        ("El Focarón", "Pequeña cala rocosa, oleaje fuerte, poco frecuentada.", ["cantos","dificil-acceso"]),
        ("El Garruncho", "Pequeña cala de bolos y rocas al oeste del espigon del puerto.", ["cantos"]),
        ("La Atalaya", "Aislada, forma de concha, rocosa, separada por pequeñas islas, sin infraestructura.", ["cantos","dificil-acceso"]),
        ("La Guardada", "Pequeña de bolos, oleaje fuerte, poco concurrida.", ["cantos","dificil-acceso"]),
        ("Las Llanas", "Remota y tranquila, entre acantilados, se accede por una larga escalera.", ["cantos","dificil-acceso"]),
        ("Xan-Xún", "Pequeña playa aislada de grava, baja ocupación, sin infraestructura.", ["cantos","dificil-acceso"]),
        ("Xilo / Veneiro", "Pequeña, junto a Aguilar, se beneficia de sus servicios.", ["arena-dorada","accesible"]),
    ]),
    dict(nombre="Castrillón", zona="oeste", dist_km=35.1, lat=43.5827, lon=-5.9927, mareas_slug="salinas", beaches=[
        ("Arnao (Castrillon)", "Cala resguardada de arena y bolos, muy turística y con buenos servicios.", ["arena-dorada","accesible"]),
        ("Bahínas", "Semiurbana, arena oscura y bolos, oleaje moderado, cerca de Santa Maria del Mar.", ["arena-oscura","urbana"]),
        ("El Cordial / El Reguero", "Aislada, arena dorada, oleaje fuerte, solo accesible a pie desde Muinelles con marea baja.", ["arena-dorada","dificil-acceso"]),
        ("El Cuerno", "Pequeña, en forma de concha, grava y arena oscura.", ["arena-oscura","dificil-acceso"]),
        ("Munielles", "Compacta, cerca de Bayas, arena oscura, oleaje moderado.", ["arena-oscura"]),
        ("Playon de Bayas / El Sablon", "Extensa playa compartida con Soto del Barco, sistema dunar de gran valor ecológico, oleaje peligroso.", ["arena-dorada","duna","monumento-natural"]),
        ("Requexinos", "Arena oscura, oleaje fuerte, rodeada de colinas con vegetación.", ["arena-oscura"]),
        ("Salinas", "Gran playa muy popular con servicio completo, club náutico, alta afluencia.", ["arena-dorada","urbana","accesible","familias"]),
        ("San Juan de Nieva / El Espartal", "Protegida, con vegetación dunar, buenas instalaciones, alta ocupación.", ["arena-dorada","duna","accesible"]),
        ("Santa Maria del Mar", "Playa de ria en la desembocadura del río Ferrera, buenas instalaciones, alta ocupación.", ["arena-dorada","urbana","accesible"]),
    ]),
    dict(nombre="Gozón", zona="oeste", dist_km=20.1, lat=43.6103, lon=-5.7930, mareas_slug="luanco", beaches=[
        ("Aguilera", "Arena dorada gruesa, oleaje fuerte, poco visitada.", ["arena-dorada","dificil-acceso"]),
        ("Aramar", "Bolos y rocas en una cala resguardada por pequeñas islas.", ["cantos","dificil-acceso"]),
        ("Banugues", "En una ensenada con yacimientos paleoliticos, duchas y limpieza.", ["arena-dorada","accesible"]),
        ("Carriciega / Carniciega / De Barquera", "Arena dorada dentro del Paisaje Protegido de Cabo de Penas, oleaje fuerte, poca ocupación.", ["arena-dorada","monumento-natural","dificil-acceso"]),
        ("El Bigaral / Los Cristales", "Pequeña de arena blanca, poco frecuentada, sobre todo por pescadores.", ["arena-blanca","dificil-acceso"]),
        ("El Dique", "Pequeña de arena y grava, baja ocupación, sin servicios.", ["arena-oscura","dificil-acceso"]),
        ("Gargantera", "Con forma de concha y rocosa, difícil acceso, sin servicios.", ["cantos","dificil-acceso"]),
        ("La Ribera", "Arena dorada al fondo de la bahia de Luanco, junto al puerto.", ["arena-dorada","urbana"]),
        ("Llumeres", "Color rojizo por antiguas minas de hierro, frecuentada por pescadores.", ["arena-oscura","dificil-acceso"]),
        ("Luanco / Santa Marina", "Playa del pueblo pesquero y turístico de Luanco, infraestructura completa.", ["arena-dorada","urbana","accesible","familias"]),
        ("Moniello", "Pequeña cala de bolos cerca de Luanco, con duchas.", ["cantos"]),
        ("Samarincha / Samarinchón", "Semiurbana, de bolos, poco uso, sin infraestructura.", ["cantos"]),
        ("Samarinchina", "Pequeña cala de aguas tranquilas, baja ocupación, zona de fondeo.", ["cantos"]),
        ("San Pedro de Antromero", "Valor geológico, con huellas fosiles de dinosaurio.", ["cantos","dificil-acceso"]),
        ("Tenrero / Verdicio", "Arena dorada gruesa, sistema dunar ecológico, muy popular, yacimientos paleoliticos cerca.", ["arena-dorada","duna","accesible","familias"]),
        ("Viodo", "Cala en el Paisaje Protegido de Cabo de Penas, difícil acceso, sin infraestructura.", ["cantos","monumento-natural","dificil-acceso"]),
        ("Xago", "Extensa playa con notable complejo dunar, alta ocupación, oferta gastronomica modesta.", ["arena-dorada","duna","accesible","familias"]),
    ]),
    dict(nombre="Carreño", zona="oeste", dist_km=16.1, lat=43.5847, lon=-5.7742, mareas_slug="candas", beaches=[
        ("Candas / La Pregona", "Playa urbana con servicios completos, junto al puerto de Candas.", ["arena-dorada","urbana","accesible","familias"]),
        ("Carranques 1 y 2", "Calas de interes paisajístico con formaciones geológicas y vegetación.", ["cantos","dificil-acceso"]),
        ("Huelgues", "Arenosa, ocupación media, cerca de la urbanización de Perlora.", ["arena-dorada"]),
        ("La Palmera", "Arena fina en la turística Candas, con instalaciones completas y deportes nauticos.", ["arena-dorada","urbana","accesible"]),
        ("Rebolleres / Pineres", "De bolos, entorno algo degradado, sin servicios, poco visitada.", ["cantos","dificil-acceso"]),
        ("Taluxa", "Pequeña cala de arena y grava, difícil acceso, poco frecuentada salvo pescadores.", ["cantos","dificil-acceso"]),
        ("Tranqueru", "Rodeada de acantilados en zona de valor ecológico, sin servicios, frecuentada por pescadores.", ["cantos","dificil-acceso"]),
        ("Xivares 1 y 2", "Extensa playa de arena blanca en un entorno paisajístico atractivo.", ["arena-blanca","accesible"]),
    ]),
    dict(nombre="Gijón", zona="gijon", dist_km=0, lat=43.5378, lon=-5.6544, mareas_slug="gijon", beaches=[
        ("San Lorenzo", "La gran playa urbana de Gijon, en pleno centro, excelentes equipamientos: aseos, duchas, alquiler de sombrillas y hamacas, Club Náutico.", ["arena-dorada","urbana","accesible","familias"]),
        ("Poniente", "Playa artificial junto al puerto deportivo, arena dorada, mucha afluencia, zona de fondeo.", ["arena-dorada","urbana","accesible"]),
        ("El Arbeyal", "Gran afluencia desde su regeneración en 1995, aguas tranquilas y buenos servicios.", ["arena-dorada","urbana","accesible","familias"]),
        ("Cervigon / El Rinconin", "Junto a San Lorenzo, alta afluencia, bastantes equipamientos, admite perros.", ["arena-oscura","urbana","perros","accesible"]),
        ("Estano", "Pequeña playa semiurbana de arena y grava, servicios de nivel medio.", ["arena-dorada","urbana"]),
        ("Peñarrubia", "Muy estrecha, rodeada de altos acantilados, alta ocupación, playa nudista.", ["arena-dorada","nudista","dificil-acceso"]),
        ("Cagonera y Serín", "Cerca del Cabo de San Lorenzo, oleaje fuerte y poca afluencia.", ["cantos","dificil-acceso"]),
    ]),
    dict(nombre="Villaviciosa", zona="este", dist_km=29.1, lat=43.5333, lon=-5.3944, mareas_slug="villaviciosa", beaches=[
        ("Rodiles", "Gran arenal junto a la ria (Reserva Natural), pinares y eucaliptales, muy popular y con buenos servicios.", ["arena-dorada","monumento-natural","surf","accesible","familias"]),
        ("Tazones", "En el pintoresco pueblo pesquero de Tazones, buen nivel de equipamientos.", ["arena-dorada","urbana","accesible"]),
        ("España", "En la desembocadura del río España, rodeada de acantilados, oleaje fuerte y alta afluencia.", ["arena-dorada","dificil-acceso"]),
        ("La Ñora", "Pequeña cala de arena flanqueada por acantilados, nivel medio de servicios y alta ocupación.", ["arena-dorada","dificil-acceso"]),
        ("El Puntal", "En el interior de la ria de Villaviciosa (Reserva Natural), arena dorada y rocas, zona arbolada.", ["arena-dorada","monumento-natural"]),
        ("Merón", "Pequeña playa con forma de concha de arena y grava.", ["cantos"]),
        ("Misiego", "En la ria, aguas tranquilas y arena dorada, apenas tiene infraestructuras.", ["arena-dorada","dificil-acceso"]),
    ]),
    dict(nombre="Colunga", zona="este", dist_km=41.8, lat=43.5136, lon=-5.2667, mareas_slug="lastres", beaches=[
        ("La Isla", "Urbana, arena dorada, frente a un pequeño islote, paseo marítimo y buenos servicios.", ["arena-dorada","urbana","accesible","familias"]),
        ("La Griega", "Gran arenal dorado en la desembocadura del río Libardon, huellas de dinosaurio y charcas naturales con marea baja.", ["arena-dorada","accesible","familias"]),
        ("El Astillero / Playa de Lastres", "En el pueblo marinero de Lastres, nivel de servicios bajo pero mucho interes turístico.", ["cantos","urbana"]),
        ("Escanu", "Urbana, en pleno casco de Lastres, junto al puerto.", ["cantos","urbana"]),
        ("La Espasa (Colunga)", "En la desembocadura del río Espasa, límite con Caravia, arena dorada y buen nivel de servicios.", ["arena-dorada","accesible"]),
        ("Salmoriera / El Barrigon", "Pequeña, forma de concha, arena dorada, muy turística junto a La Isla.", ["arena-dorada","urbana"]),
    ]),
    dict(nombre="Caravia", zona="este", dist_km=54.6, lat=43.5028, lon=-5.1547, mareas_slug="caravia", beaches=[
        ("Arenal de Moris / Caravia", "Extensa playa en forma de concha, arena dorada, muy turística y con buen nivel de servicios.", ["arena-dorada","accesible","familias"]),
        ("Beciella / Barciella", "Aislada y tranquila, bolos y arena, sin servicios.", ["cantos","dificil-acceso"]),
        ("El Viso / Moracey", "Enclavada dentro de los extensos arenales de Caravia.", ["arena-dorada"]),
        ("La Espasa (Caravia)", "Comparte estuario con Colunga, buen nivel de servicios, accesible.", ["arena-dorada","accesible"]),
    ]),
    dict(nombre="Ribadesella", zona="este", dist_km=62.0, lat=43.4642, lon=-5.0575, mareas_slug="ribadesella", beaches=[
        ("Santa Marina", "Playa principal de Ribadesella, gran infraestructura turística y patrimonio cultural.", ["arena-dorada","urbana","accesible","familias"]),
        ("Vega / Berbes", "Extenso arenal con dunas, Monumento Natural, buena accesibilidad y servicio de rescate.", ["arena-dorada","monumento-natural","duna","accesible"]),
        ("La Atalaya", "Diminuta cala junto al puerto, fácil acceso a pie desde el casco urbano.", ["cantos","urbana"]),
        ("Arra", "Cala rocosa junto al límite con Llanes, zona de buceo adecuada.", ["cantos","buceo","dificil-acceso"]),
        ("Guadamia / Aguamia", "En la desembocadura, paisaje kárstico, oleaje y corrientes fuertes.", ["cantos","dificil-acceso"]),
    ]),
    dict(nombre="Llanes", zona="este", dist_km=88.8, lat=43.4203, lon=-4.7550, mareas_slug="llanes", beaches=[
        ("Torimbia", "Amplia y virgen, muy fotogénica, tradicionalmente nudista.", ["arena-dorada","nudista","dificil-acceso"]),
        ("Gulpiyuri", "Pequeña playa de interior, alimentada por galerías subterráneas a 100 m del mar, Monumento Natural.", ["arena-dorada","monumento-natural"]),
        ("San Antolín", "Extensa playa de arena blanca junto a un monasterio románico, ventosa y con oleaje fuerte.", ["arena-blanca","surf"]),
        ("Cuevas del Mar", "En la desembocadura de un río, con espectaculares cavidades kársticas.", ["cantos","accesible"]),
        ("Toranda / Niembro", "Gran arenal junto a la ria de Niembro, muy popular.", ["arena-dorada","accesible","familias"]),
        ("Andrin", "Entorno rocoso rodeado de acantilados, oleaje y corrientes fuertes.", ["arena-dorada","dificil-acceso"]),
        ("Ballota", "Bello entorno con un islote caracteristico frente a la playa (Castro Ballota).", ["arena-dorada"]),
        ("Barro", "Arena blanca, aguas claras, buenos servicios, conecta con Sorraos en marea baja.", ["arena-blanca","accesible","familias"]),
        ("Borizo / Borizu", "Arena blanca, muy turística, conecta con la Isla de Borizo en marea baja.", ["arena-blanca","accesible"]),
        ("Buelna / Arenillas", "Pequeña cala con formaciones kársticas (El Picón), ideal para familias, sin servicios.", ["cantos","familias"]),
        ("Cobijeru", "Cala semicircular al pie de un acantilado, aguas tranquilas por fisuras rocosas, Monumento Natural kárstico.", ["cantos","monumento-natural"]),
        ("Cue / Antilles / Canales", "Entorno rocoso, arena blanca fina, aguas tranquilas, conecta con un islote en marea baja.", ["arena-blanca","accesible"]),
        ("El Portiello de San Martín / La Capilla", "Pequeña cala resguardada entre grandes rocas, baja ocupación.", ["cantos","dificil-acceso"]),
        ("El Sablon", "Playa urbana de Llanes, alta ocupación, paseo marítimo y buenos servicios.", ["arena-dorada","urbana","accesible"]),
        ("Vidiago", "Playa dividida en dos tramos, entorno tranquilo.", ["arena-dorada"]),
        ("San Antonio", "Pequeña cala natural.", ["cantos","dificil-acceso"]),
        ("Toró", "Ideal para los mas pequeños.", ["arena-dorada","familias"]),
        ("El Canal", "Pequeña playa cerca de Villanueva de Pria, aguas tranquilas.", ["cantos","dificil-acceso"]),
        ("Palombina (Celorio)", "En Celorio, con creciente desarrollo turístico, arena dorada.", ["arena-dorada","urbana","accesible"]),
        ("Guadamia / Aguamia (Llanes)", "Paisaje kárstico, oleaje y corrientes fuertes.", ["cantos","dificil-acceso"]),
        ("La Acacia / Las Gaviotas / Jorconera", "Solo accesible en barco, aislada entre acantilados.", ["cantos","dificil-acceso"]),
        ("La Almenada", "En la desembocadura de un río, difícil acceso, sin servicios.", ["cantos","dificil-acceso"]),
        ("La Entrada", "Arena blanca, aguas tranquilas, poca afluencia, entorno de ria.", ["arena-blanca"]),
        ("La Huelga", "En la desembocadura de un río, alta ocupación cerca de Hontoria.", ["arena-dorada","accesible"]),
        ("La Tala / Naranxu", "Pequeña, rocosa y de grava, corrientes y oleaje fuertes, sin servicios.", ["cantos","dificil-acceso"]),
        ("La Tayada", "Pequeña, arena dorada, en paisaje protegido, desaparece en marea alta.", ["arena-dorada","monumento-natural"]),
        ("Las Camaras / Los Frailes", "Arena blanca, paseo marítimo, duchas y telefonos.", ["arena-blanca","accesible"]),
        ("Pendueles / Castiello", "Rodeada de acantilados, acceso por escaleras, arena oscura, unida a un islote por un tombolo.", ["arena-oscura","dificil-acceso"]),
        ("Pestaña / Portaquinos", "Pequeña cala, se accede caminando desde Torimbia, sin servicios.", ["cantos","dificil-acceso"]),
        ("Poo", "Cerca del pueblo de Poo, arena blanca, aguas tranquilas, alta ocupación, ideal para familias.", ["arena-blanca","accesible","familias"]),
        ("Portiellu de Cué", "Arena y rocas, aguas claras, ocupación media.", ["cantos"]),
        ("Puerto Chico / Puertu Chicu", "Arena y bolos, muy popular, paseo marítimo, servicios adecuados.", ["cantos","accesible"]),
        ("Cebías", "Playa de acceso rodado en el oriente del concejo.", ["arena-dorada"]),
        ("Troenzo", "Pequeña playa de acceso rodado.", ["cantos"]),
        ("Villanueva", "Playa de acceso rodado cerca de Villanueva de Pria.", ["arena-dorada"]),
        ("Xiglú", "Pequeña playa de acceso rodado.", ["cantos"]),
    ]),
    dict(nombre="Ribadedeva", zona="este", dist_km=110.6, lat=43.3921, lon=-4.5087, mareas_slug="la-franca", beaches=[
        ("La Franca", "Arena blanca fina en la desembocadura del río Cabra, oleaje fuerte, buen nivel de servicios, alta afluencia.", ["arena-blanca","accesible","familias"]),
        ("El Oso", "Rocosa, rodeada de altos acantilados, acceso difícil desde Pimiango o desde La Franca en marea baja.", ["cantos","dificil-acceso"]),
        ("Mendia / Regolguero", "Rocosa entre acantilados, oleaje fuerte, solo accesible en marea baja, sin servicios.", ["cantos","dificil-acceso"]),
    ]),
]

# ---------------------------------------------------------------------------
# Ruta fotográfica: puntos de interés (miradores, faros, pueblos marineros,
# fenómenos naturales) + una selección de las playas más fotogénicas del
# listado anterior. Fuentes: asturiasprestosa.com, asturias.com, blog.telecable.es
# (investigación web, septiembre 2026). tipo: mirador | faro | pueblo | playa | fenomeno-natural | monumento
# ---------------------------------------------------------------------------
_cj = {c["nombre"]: c for c in concejos}

def _poi(nombre, tipo, concejo, desc, mejor_luz):
    c = _cj[concejo]
    return dict(nombre=nombre, tipo=tipo, concejo=concejo, zona=c["zona"], dist_km=c["dist_km"], lat=c["lat"], lon=c["lon"], desc=desc, mejor_luz=mejor_luz)

ruta_foto = [
    _poi("Mirador de la Mirandiella", "mirador", "Castropol",
         "Junto a la iglesia de Santiago Apóstol, con vistas abiertas sobre la Ría del Eo y la costa gallega al otro lado.",
         "Media mañana, con la marea alta llenando la ría de agua."),
    _poi("Faro de Tapia", "faro", "Tapia de Casariego",
         "Pequeño faro de 1859 sobre la punta rocosa que separa las dos playas de Tapia, con vistas a la Playa de Anguileiro.",
         "Atardecer, cuando el sol bajo ilumina la torre y las playas de ambos lados."),
    _poi("Faro de San Agustín (Ortiguera)", "faro", "Coaña",
         "Faro de rayas blancas y azules muy reconocible, en un entorno agreste sobre acantilados.",
         "Días de cielo despejado a mediodía, por el contraste de color del faro."),
    _poi("Ermita de la Regalina", "mirador", "Valdés",
         "Pequeña ermita encaramada en un acantilado sobre el mar en Cadavedo, uno de los rincones más fotografiados de la costa occidental.",
         "Última hora de la tarde, luz rasante sobre el acantilado y el mar de fondo."),
    _poi("Faro de Luarca", "faro", "Valdés",
         "Construido en 1862 sobre la Punta Focicón, domina la villa de Luarca y su cementerio marinero.",
         "Atardecer, con el faro a contraluz sobre el puerto."),
    _poi("Pueblo de Cudillero", "pueblo", "Cudillero",
         "Casas de colores apiñadas en anfiteatro sobre una cala, uno de los pueblos marineros más fotografiados de Asturias.",
         "Media mañana desde el mirador de la iglesia, o al atardecer con luz cálida sobre las fachadas."),
    _poi("Faro de Cabo Vidio", "faro", "Cudillero",
         "A más de 100 m sobre el mar, uno de los acantilados más altos y espectaculares de la costa asturiana.",
         "Atardecer despejado, con el sol poniéndose sobre el océano hacia Galicia."),
    _poi("Faro de San Esteban de Pravia", "faro", "Muros de Nalón",
         "En la desembocadura del río Nalón, junto al puerto y las playas de Aguilar y San Esteban.",
         "Atardecer, con el faro recortado sobre la ría."),
    _poi("Faro de Cabo Peñas", "faro", "Gozón",
         "El faro más importante de Asturias, en el punto más septentrional del Principado, con museo marítimo y acantilados de gran altura.",
         "Amanecer o anochecer con niebla baja; también espectacular con mar de fondo en días de temporal."),
    _poi("Pueblo de Candás", "pueblo", "Carreño",
         "Villa marinera con puerto pesquero activo, paseo marítimo y el Cristo del Mar vigilando la bocana.",
         "Atardecer desde el paseo, con las barcas del puerto en primer plano."),
    _poi("Elogio del Horizonte", "monumento", "Gijón",
         "Escultura monumental de Eduardo Chillida en el Cerro de Santa Catalina, con vistas de 360° sobre la bahía y el mar Cantábrico.",
         "Amanecer, muy popular para fotografiar el sol saliendo a través de la escultura."),
    _poi("Pueblo de Tazones", "pueblo", "Villaviciosa",
         "Pueblo pesquero de casas de colores escalonadas sobre un pequeño puerto, en la bocana de la ría de Villaviciosa.",
         "Media tarde, con luz suave sobre las fachadas y los acantilados del entorno."),
    _poi("Mirador del Fitu", "mirador", "Colunga",
         "Balcón panorámico en la Sierra del Sueve a más de 600 m de altitud, con vistas simultáneas del mar Cantábrico y los Picos de Europa.",
         "Amanecer en días despejados de otoño o invierno, cuando el mar de nubes cubre los valles."),
    _poi("Pueblo de Lastres", "pueblo", "Colunga",
         "Villa marinera escalonada sobre un acantilado, con su faro y el puerto pesquero; escenario de la serie 'Doctor Mateo'.",
         "Desde el Mirador de San Roque, al atardecer con luz cálida sobre los tejados."),
    _poi("Faro de Ribadesella (Tereñes)", "faro", "Ribadesella",
         "Sobre un acantilado sobre la desembocadura del río Sella, con vistas a la playa de Santa Marina y el casco urbano.",
         "Atardecer, con el faro a contraluz sobre la ría del Sella."),
    _poi("Bufones de Pría", "fenomeno-natural", "Llanes",
         "Chimeneas naturales en el terreno kárstico que expulsan agua y aire con estruendo al romper las olas por debajo; el grupo más occidental de los bufones asturianos.",
         "Marea alta con oleaje fuerte, cuando los chorros de agua alcanzan más altura (mejor en otoño e invierno, con precaución)."),
    _poi("Faro de Llanes", "faro", "Llanes",
         "Pequeño faro de 1860 sobre el Paseo de San Pedro, junto al puerto y los famosos Cubos de la Memoria de Ibarrola.",
         "Atardecer, con el faro y los Cubos de la Memoria en el mismo encuadre."),
    _poi("Faro de San Emeterio (Pimiango)", "faro", "Ribadedeva",
         "En el extremo oriental de la costa asturiana, cerca de la Cueva del Pindal, con vistas hacia Cantabria.",
         "Atardecer despejado, punto elevado con horizonte marino amplio."),
    # playas más fotogénicas (ya presentes en el listado de playas, con nota de fotografía)
    _poi("Barayo / La Vega", "playa", "Valdés",
         "Playa virgen de 670 m dentro de la Reserva Natural Parcial de Barayo, con dunas, marisma y el estuario del río Barayo.",
         "Amanecer o marea baja, cuando queda al descubierto todo el estuario."),
    _poi("El Silencio / Gaviero / Gavieiru", "playa", "Cudillero",
         "Posiblemente la playa más fotogénica del occidente asturiano: virgen, con espectaculares islotes y acantilados.",
         "Marea baja para acceder a la arena y encuadrar los islotes; luz rasante de última hora de la tarde."),
    _poi("Playón de Bayas / El Sablón", "playa", "Castrillón",
         "Extensa playa con un sistema dunar de gran valor ecológico compartida con Soto del Barco.",
         "Amanecer, con la luz baja recorriendo las dunas."),
    _poi("Carriciega / Carniciega / De Barquera", "playa", "Gozón",
         "Cala de arena dorada dentro del Paisaje Protegido de Cabo de Peñas, poco frecuentada.",
         "Última hora de la tarde, con los acantilados del cabo como telón de fondo."),
    _poi("Rodiles", "playa", "Villaviciosa",
         "Gran arenal junto a la ría de Villaviciosa (Reserva Natural), con pinares y eucaliptales al fondo.",
         "Amanecer desde la desembocadura de la ría, con niebla frecuente en otoño."),
    _poi("Vega / Berbes", "playa", "Ribadesella",
         "Extenso arenal con dunas declarado Monumento Natural, con buena accesibilidad.",
         "Atardecer, con el sistema dunar iluminado de lado."),
    _poi("Torimbia", "playa", "Llanes",
         "Playa amplia y virgen, una de las más fotogénicas de Llanes, a la que solo se accede a pie.",
         "Media mañana, cuando el sol ilumina de frente la cala rodeada de acantilados."),
    _poi("Gulpiyuri", "playa", "Llanes",
         "Playa de interior alimentada por galerías subterráneas a 100 m del mar, Monumento Natural único en España.",
         "Cualquier hora con cielo despejado; el contraste del prado verde alrededor de la arena y el agua turquesa es lo llamativo."),
    _poi("Cobijeru", "playa", "Llanes",
         "Cala semicircular al pie de un acantilado, con aguas que entran por fisuras rocosas; Monumento Natural kárstico.",
         "Marea baja, cuando se puede bajar a la arena y ver el arco rocoso completo."),
]

print(f"Total puntos ruta fotográfica: {len(ruta_foto)}")

# aplanar
playas = []
for c in concejos:
    for (nombre, desc, tags) in c["beaches"]:
        playas.append(dict(
            nombre=nombre,
            concejo=c["nombre"],
            zona=c["zona"],
            dist_km=c["dist_km"],
            lat=c["lat"],
            lon=c["lon"],
            mareas_slug=c["mareas_slug"],
            desc=desc,
            tags=tags,
        ))

print(f"Total concejos: {len(concejos)}")
print(f"Total playas: {len(playas)}")

from extra_data import build_extra
restaurantes, sidrerias, ruta_foto_interior, lagares, sitios = build_extra(concejos)
print(f"Total restaurantes: {len(restaurantes)}")
print(f"Total sidrerías: {len(sidrerias)}")
print(f"Total rutas fotográficas de interior: {len(ruta_foto_interior)}")
print(f"Total lagares: {len(lagares)}")
print(f"Total sitios (Qué ver): {len(sitios)}")

data = dict(
    concejos=[dict(nombre=c["nombre"], zona=c["zona"], dist_km=c["dist_km"], lat=c["lat"], lon=c["lon"], mareas_slug=c["mareas_slug"], n=len(c["beaches"])) for c in concejos],
    playas=playas,
    ruta_foto=ruta_foto,
    ruta_foto_interior=ruta_foto_interior,
    restaurantes=restaurantes,
    sidrerias=sidrerias,
    lagares=lagares,
    sitios=sitios,
)

with open("playas.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)

with open("playas.min.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, separators=(",", ":"))

print("Escrito playas.json y playas.min.json")

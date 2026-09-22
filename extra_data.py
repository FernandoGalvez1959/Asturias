# -*- coding: utf-8 -*-
"""
Datos adicionales: restaurantes, sidrerías y ruta fotográfica de interior.
Investigados vía búsqueda web (Guía Michelín, Guía Repsol, D.O.P. Sidra de
Asturias, prensa local, guías de turismo/fotografía) en septiembre de 2026.
Este módulo se importa desde build_data.py, que ya define `concejos`.
"""
import json
import re

RESTAURANTES_RAW = json.loads(r'''
[
{"nombre":"Casa Marcial","concejo":"Parres (Arriondas)","distincion":["3 estrellas Michelín","3 soles Repsol"],"especialidades":"Alta cocina asturiana de vanguardia, producto de huerta propia, pescado de río","tique_medio":"165-220€ (menús degustación Fitu/Cachuchu)","desc":"El único tres estrellas Michelín de Asturias, dirigido por Nacho Manzano y su familia, referencia nacional de la cocina asturiana contemporánea."},
{"nombre":"El Corral del Indianu","concejo":"Parres (Arriondas)","distincion":["1 estrella Michelín","2 soles Repsol"],"especialidades":"Cocina moderna de producto asturiano: ostras del Eo, pitu de caleya, quesos","tique_medio":"95-130€ aprox (menú degustación)","desc":"Restaurante del chef José Antonio Campoviejo que busca la emoción a través del detalle partiendo de la despensa asturiana."},
{"nombre":"Auga","concejo":"Gijón","distincion":["1 estrella Michelín","2 soles Repsol"],"especialidades":"Cocina tradicional actualizada, pescado y marisco del Cantábrico","tique_medio":"70-100€ aprox","desc":"Situado en el puerto deportivo de Gijón, con terraza frente al mar y una carta que varía según el mercado, dirigido por el chef Gonzalo Pañeda."},
{"nombre":"Marcos","concejo":"Gijón","distincion":["1 estrella Michelín"],"especialidades":"Cocina moderna de autor, atún rojo, caza, setas silvestres","tique_medio":"120-160€ aprox (menús Río/Libertad)","desc":"Íntimo restaurante de solo 12 comensales con cocina a la vista, dirigido por el chef Marcos Mistry."},
{"nombre":"El Retiro","concejo":"Llanes (Pancar)","distincion":["1 estrella Michelín","2 soles Repsol"],"especialidades":"Cocina actual asturiana, bacalao, fusión asturiano-asiática","tique_medio":"110-150€ aprox (menú San Patricio)","desc":"Dirigido por Ricardo González Sotres, combina un bistró informal con una propuesta gastronómica de alta cocina en Pancar, Llanes."},
{"nombre":"Ferpel Gastronómico","concejo":"Coaña (Ortiguera)","distincion":["1 estrella Michelín","1 sol Repsol"],"especialidades":"Producto autóctono del occidente asturiano, pescado de la zona","tique_medio":"100-140€ aprox","desc":"Restaurante familiar en Ortiguera dirigido por el chef Elio Fernández, con vistas y compromiso con la tradición rural del occidente asturiano."},
{"nombre":"Real Balneario","concejo":"Castrillón (Salinas)","distincion":["1 estrella Michelín","2 soles Repsol"],"especialidades":"Cocina de mercado, pescado y marisco del Cantábrico, lubina al champagne","tique_medio":"90-130€ aprox","desc":"Situado en primera línea de playa en Salinas, con más de 50 años de historia y el chef Isaac Loya al frente."},
{"nombre":"Monte","concejo":"Lena (San Feliz)","distincion":["1 estrella Michelín","1 sol Repsol"],"especialidades":"Cocina de proximidad y de temporada, producto de la comarca de Lena","tique_medio":"100-140€ aprox","desc":"El chef Xune Andrade elabora una cocina moderna en la que el 90% de los productos proceden de un radio de 20 km."},
{"nombre":"Casa Gerardo","concejo":"Carreño (Prendes)","distincion":["1 estrella Michelín","3 soles Repsol"],"especialidades":"Fabada, arroz con leche, cocina asturiana renovada","tique_medio":"90-150€ aprox (menús 80-200€; carta 25-66€/plato)","desc":"Uno de los restaurantes más antiguos de España (140+ años), famoso por su fabada y su arroz con leche, dirigido por la familia Morán."},
{"nombre":"Ayalga","concejo":"Ribadesella","distincion":["1 estrella Michelín","2 soles Repsol"],"especialidades":"Cocina moderna, pescado de anzuelo, producto local","tique_medio":"110-150€ aprox","desc":"Restaurante del Hotel Villa Rosario, en un palacete de 1914 con vistas al Cantábrico, dirigido por el chef Israel Moreno."},
{"nombre":"Regueiro","concejo":"Navia (Tox)","distincion":["1 estrella Michelín","2 soles Repsol"],"especialidades":"Cocina fusión (india, mexicana, asiática) con producto asturiano","tique_medio":"85-120€ aprox (menús Corto/Diego/Hedonista)","desc":"En una aldea de 86 vecinos, el chef Diego Fernández sorprende con una fusión audaz de sabores internacionales y producto local."},
{"nombre":"Casa Fermín","concejo":"Oviedo","distincion":["2 soles Repsol"],"especialidades":"Cocina asturiana clásica y creativa, fabada","tique_medio":"35-60€ aprox","desc":"Clásico centenario de Oviedo que combina la artesanía tradicional con técnicas contemporáneas."},
{"nombre":"La Huertona","concejo":"Ribadesella","distincion":["2 soles Repsol"],"especialidades":"Pescado a la parrilla, producto de temporada, huerta propia","tique_medio":"60-80€ aprox","desc":"Restaurante de cocina de producto en Ribadesella, con huerta propia y especializado en pescado a la parrilla."},
{"nombre":"Alenda","concejo":"Villaviciosa","distincion":["1 sol Repsol"],"especialidades":"Cocina creativa de proximidad, ternera asturiana, sidra","tique_medio":"45-65€ aprox","desc":"Restaurante con huerta propia en plena comarca de la sidra, con menús degustación centrados en producto regional."},
{"nombre":"Blanco","concejo":"Cangas del Narcea","distincion":["1 sol Repsol"],"especialidades":"Cocina asturiana de cuchara reinterpretada, bonito en sidra, jabalí","tique_medio":"25-35€ aprox","desc":"Bar-restaurante que reinterpreta la cocina casera asturiana con producto local en pleno occidente."},
{"nombre":"Ca'Suso","concejo":"Oviedo","distincion":["1 sol Repsol"],"especialidades":"Cocina asturiana de autor, croquetas de queso, fabada","tique_medio":"40-55€ aprox","desc":"Restaurante familiar dirigido por los hermanos Iván y Vicente, famoso por sus croquetas y su cocina de raíz asturiana."},
{"nombre":"Casa Belarmino","concejo":"Gozón","distincion":["1 sol Repsol"],"especialidades":"Cocina asturiana casera, marisco del Cantábrico, pitu de caleya","tique_medio":"40-55€ aprox","desc":"Cerca del Cabo Peñas, reinterpreta con técnica los sabores clásicos asturianos y el recuerdo familiar."},
{"nombre":"Cocina Cabal","concejo":"Oviedo","distincion":["1 sol Repsol"],"especialidades":"Cocina de autor de mercado con influencia mediterránea","tique_medio":"40-55€ aprox","desc":"Dirigido por el chef Vicente Suárez Cabal, con paso por El Celler de Can Roca, apuesta por la solidez y el producto."},
{"nombre":"Del Arco","concejo":"Oviedo","distincion":["1 sol Repsol"],"especialidades":"Cocina asturiana contemporánea, guisos, taberna informal","tique_medio":"40-60€ aprox (menús degustación 75-90€)","desc":"Clásico contemporáneo en la Plaza de América de Oviedo, con taberna informal en planta baja y comedor gastronómico arriba."},
{"nombre":"El Asador de Abel-Casa Farpón","concejo":"Siero (Argüelles)","distincion":["1 sol Repsol"],"especialidades":"Carnes a la brasa, croquetas de jamón, cocina asturiana tradicional","tique_medio":"25-35€ aprox","desc":"A medio camino entre casa de comidas tradicional y asador contemporáneo, con parrilla de carbón como protagonista."},
{"nombre":"El Molín de Mingo","concejo":"Cangas de Onís (Peruyes)","distincion":["1 sol Repsol"],"especialidades":"Fabada, arroz con pitu, cocina casera asturiana","tique_medio":"40-55€ aprox","desc":"Instalado en un antiguo molino rehabilitado y rodeado de vegetación, dirigido por Dulce Martínez."},
{"nombre":"Éleonore","concejo":"Castrillón (Salinas)","distincion":["1 sol Repsol"],"especialidades":"Cocina de autor, langostino cántabro, venado","tique_medio":"65-90€ aprox","desc":"Restaurante boutique en el paseo de Salinas con vistas al Cantábrico, dirigido por la chef Cristina Arias."},
{"nombre":"Farragua","concejo":"Gijón","distincion":["1 sol Repsol"],"especialidades":"Cocina de autor, pilpiles de verduras, escabeches, casquería","tique_medio":"40-55€ aprox","desc":"Propuesta creativa del chef Ricardo Señorán en Gijón, con un menú especial dedicado a la casquería."},
{"nombre":"Güeyu-Mar","concejo":"Ribadesella","distincion":["1 sol Repsol"],"especialidades":"Pescado y marisco a la parrilla, cocina marinera ahumada","tique_medio":"45-70€ aprox (el pescado se cobra a peso)","desc":"Frente a la playa de Vega, referencia nacional en pescado a la parrilla dirigido por el chef Abel Álvarez."},
{"nombre":"Gunea","concejo":"Castrillón (Cruz de Illas)","distincion":["1 sol Repsol"],"especialidades":"Cocina asturiana de mercado con toques vascos","tique_medio":"40-55€ aprox","desc":"Restaurante rural donde el chef Pablo Montero moderniza recetas tradicionales asturianas con producto de temporada."},
{"nombre":"Los Llaureles","concejo":"Cabranes (Torazo)","distincion":["1 sol Repsol"],"especialidades":"Cocina de autor, verduras, ceviches, menú único degustación","tique_medio":"45-60€ aprox","desc":"Íntimo restaurante rural de solo ocho mesas en la comarca de la sidra, con un único menú degustación creativo."},
{"nombre":"Married Cocina","concejo":"Llanes (Hontoria)","distincion":["1 sol Repsol"],"especialidades":"Cocina de autor con técnica francesa y guisos asturianos","tique_medio":"45-65€ aprox (menús degustación 65-90€)","desc":"El chef César Casado fusiona la tradición del oriente asturiano con técnica francesa e inspiración en la nouvelle cuisine."},
{"nombre":"Mesón El Centro","concejo":"Navia (Puerto de Vega)","distincion":["1 sol Repsol"],"especialidades":"Pescado y marisco fresco de lonja, cocina tradicional marinera","tique_medio":"40-55€ aprox (menú degustación 48€)","desc":"En el pintoresco puerto pesquero de Puerto de Vega, especializado en pescado fresco de la lonja local."},
{"nombre":"Narbasu","concejo":"Piloña","distincion":["1 sol Repsol"],"especialidades":"Cocina asturiana de mercado, croquetas, arroz con pitu","tique_medio":"45-55€ aprox (menú degustación 50€)","desc":"Proyecto de los hermanos Manzano (Casa Marcial) en un palacete rural, homenaje al producto y la memoria asturiana."},
{"nombre":"Pedro Martino","concejo":"Oviedo (Caces)","distincion":["1 sol Repsol"],"especialidades":"Cocina de autor asturiana, potes reinterpretados","tique_medio":"40-55€ aprox","desc":"Con vistas al valle del Nalón, ofrece una interpretación particular de la asturianidad culinaria."},
{"nombre":"Quince Nudos","concejo":"Ribadesella","distincion":["1 sol Repsol"],"especialidades":"Arroces, marisco, cocina de ambiente marinero","tique_medio":"40-55€ aprox","desc":"Pequeño restaurante marinero del chef Bruno M. Lombán, conocido por sus arroces y producto fresco local."},
{"nombre":"Roble by Jairo Rodríguez","concejo":"Lena (Pola de Lena)","distincion":["1 sol Repsol"],"especialidades":"Cocina de autor de proximidad, pan y conservas propias","tique_medio":"45-65€ aprox (menú degustación 90€)","desc":"El chef Jairo Rodríguez cocina en solitario con producto de proximidad, pan y anchoas curadas en casa."},
{"nombre":"Yume","concejo":"Avilés","distincion":["1 sol Repsol"],"especialidades":"Cocina de autor con influencias asiáticas y producto asturiano","tique_medio":"30-65€ según menú","desc":"Situado en la Torre Niemeyer de Avilés, propuesta transgresora del chef Adrián San Julián."},
{"nombre":"El Pescador","concejo":"Cudillero","distincion":["Muy valorado en Google"],"especialidades":"Marisco, calderetas de pescado, paella marinera","tique_medio":"40-60€ aprox","desc":"Restaurante marinero en el puerto de Cudillero con barco de pesca propio, con 4,5/5 en Google y cerca de 2.000 reseñas."},
{"nombre":"El Barómetro","concejo":"Valdés (Luarca)","distincion":["Muy valorado en Google"],"especialidades":"Marisco y pescado fresco, cocina marinera","tique_medio":"35-50€ aprox","desc":"Clásico del puerto de Luarca, el restaurante mejor valorado de la villa por su pescado y marisco frescos."}
]
''')

REST_NUEVOS_RAW = json.loads(r'''
[
{"nombre":"Gloria","concejo":"Gijón","distincion":["Recomendado Michelín"],"especialidades":"Cocina asturiana actualizada, guisos y producto de temporada","tique_medio":"35-45€ aprox","desc":"Restaurante informal de los hermanos Nacho y Esther Manzano (Casa Marcial) en la Plaza Florencio Rodríguez. Figura en la Guía Michelín sin estrella."},
{"nombre":"Gloria","concejo":"Oviedo","distincion":["Recomendado Michelín"],"especialidades":"Cocina asturiana actualizada, guisos y producto de temporada","tique_medio":"35-45€ aprox","desc":"Segunda casa de la familia Manzano en Oviedo, mismo concepto desenfadado que el de Gijón. Recomendado por la Guía Michelín."},
{"nombre":"Abarike","concejo":"Gijón","distincion":["Recomendado Michelín"],"especialidades":"Pescados y mariscos del Cantábrico, menús degustación","tique_medio":"45-60€ aprox","desc":"Restaurante gastronómico liderado por la chef Lara Roguez, especializada en producto del mar. Presente en la Guía Michelín."},
{"nombre":"Sancho La Merced","concejo":"Gijón","distincion":["Recomendado Michelín"],"especialidades":"Cocina asturiana de mercado","tique_medio":"35-50€ aprox","desc":"Restaurante gijonés de cocina actual con base en producto local, incluido en la selección de la Guía Michelín."},
{"nombre":"Fūmu","concejo":"Gijón","distincion":["Recomendado Michelín"],"especialidades":"Fusión japonesa-asturiana, sushi con producto local","tique_medio":"30-45€ aprox","desc":"Propuesta de fusión nipona-asturiana en Gijón, recogida en la Guía Michelín."},
{"nombre":"La Tabla","concejo":"Gijón (Fano)","distincion":["Recomendado Michelín"],"especialidades":"Cocina asturiana tradicional, carnes a la brasa","tique_medio":"30-45€ aprox","desc":"Clásico de la parroquia gijonesa de Fano, abierto desde 1973, recomendado en la Guía Michelín."},
{"nombre":"El Recetario","concejo":"Gijón","distincion":["Recomendado Michelín"],"especialidades":"Cocina de mercado actualizada","tique_medio":"30-40€ aprox","desc":"Bib Gourmand de la Guía Michelín en Gijón: buena relación calidad-precio con cocina de temporada."},
{"nombre":"Le Bistró","concejo":"Llanes","distincion":["Recomendado Michelín"],"especialidades":"Cocina de bistró franco-asturiana","tique_medio":"30-45€ aprox","desc":"Bib Gourmand de la Guía Michelín en Llanes, con un formato de bistró de producto."},
{"nombre":"El Bálamu","concejo":"Llanes","distincion":["Recomendado Michelín"],"especialidades":"Pescado y marisco a la parrilla frente al mar","tique_medio":"40-60€ aprox","desc":"Chiringuito-restaurante de referencia junto a la playa de Toró, recomendado por la Guía Michelín."},
{"nombre":"Cabo Vidio","concejo":"Cudillero (Soto de Luiña)","distincion":["Recomendado Michelín","Recomendado Repsol"],"especialidades":"Pescados y mariscos, terraza con vistas","tique_medio":"40-60€ aprox","desc":"Restaurante con terraza sobre el cabo, parada gastronómica clásica de la Costa Verde, citado por Michelín y Repsol."},
{"nombre":"Casa Eutimio","concejo":"Colunga (Lastres)","distincion":["Recomendado Michelín"],"especialidades":"Merluza a la sidra, arroces y pescado de lonja","tique_medio":"35-50€ aprox","desc":"Clásico marinero del puerto de Lastres, recomendado en la Guía Michelín."},
{"nombre":"El Cenador del Azul","concejo":"Mieres","distincion":["Recomendado Michelín"],"especialidades":"Cocina de autor de temporada","tique_medio":"35-50€ aprox","desc":"Propuesta de cocina de autor en el centro de Mieres, incluida en la Guía Michelín."},
{"nombre":"El Pandora","concejo":"Avilés","distincion":["Recomendado Michelín"],"especialidades":"Cocina contemporánea de mercado","tique_medio":"35-50€ aprox","desc":"Restaurante de cocina actual en el casco histórico de Avilés, recomendado por Michelín."},
{"nombre":"Casa Chuchu","concejo":"Mieres (Turón)","distincion":["Recomendado Michelín"],"especialidades":"Sidrería y cocina de cuchara","tique_medio":"25-40€ aprox","desc":"Casa de comidas tradicional de la cuenca minera, en la parroquia de Turón, citada por la Guía Michelín."},
{"nombre":"Arraigo","concejo":"Llanera (Posada de Llanera)","distincion":["Recomendado Michelín"],"especialidades":"Cocina de raíz asturiana con toques actuales","tique_medio":"35-50€ aprox","desc":"Restaurante cercano al aeropuerto de Asturias con cocina de raíz reinterpretada, recomendado por Michelín."},
{"nombre":"El Planeta","concejo":"Gijón","distincion":["Recomendado Repsol"],"especialidades":"Sidrería, pescados (sardinas, bonito)","tique_medio":"30-40€ aprox","desc":"Sidrería histórica de Cimadevilla, especializada en pescado a la parrilla; cuenta con Solete de la Guía Repsol."},
{"nombre":"Casa Puyo","concejo":"Oviedo (Trubia)","distincion":["Recomendado Repsol"],"especialidades":"Cocina casera, platos de cuchara","tique_medio":"20-30€ aprox","desc":"Casa de comidas tradicional en la parroquia ovetense de Trubia, con Solete Repsol."},
{"nombre":"Parrilla La Veguca","concejo":"Llanes","distincion":["Recomendado Repsol"],"especialidades":"Carnes y pescados a la brasa","tique_medio":"25-40€ aprox","desc":"Parrilla llanisca reconocida con Solete Repsol por su producto a la brasa."},
{"nombre":"Meraki","concejo":"Oviedo","distincion":["Recomendado Repsol"],"especialidades":"Cocina mediterránea-asturiana de mercado","tique_medio":"25-35€ aprox","desc":"Restaurante informal en Oviedo con Solete Repsol, cocina de mercado en ambiente desenfadado."},
{"nombre":"La Reguerina","concejo":"Villaviciosa","distincion":["Recomendado Repsol"],"especialidades":"Sidrería, cocina casera con huerta propia","tique_medio":"25-40€ aprox","desc":"Sidrería en la comarca de la sidra con Solete Repsol y producto de huerta propia."},
{"nombre":"La Jamonería","concejo":"Oviedo","distincion":["Recomendado Repsol"],"especialidades":"Jamón ibérico y tapeo de producto selecto","tique_medio":"20-35€ aprox","desc":"Especialistas en jamón y tapeo de calidad en Oviedo, con Solete de la Guía Repsol."},
{"nombre":"Tierra de Agua","concejo":"Caso","distincion":["Recomendado Repsol"],"especialidades":"Cocina de montaña","tique_medio":"20-30€ aprox","desc":"Restaurante-terraza en el Parque Natural de Redes (Caso), con Solete Repsol."},
{"nombre":"Las Terrazas de Sardalla","concejo":"Ribadesella (Sardalla)","distincion":["Recomendado Repsol"],"especialidades":"Cocina tradicional asturiana con vistas","tique_medio":"25-35€ aprox","desc":"Terraza-restaurante con vistas al valle en Sardalla (Ribadesella), reconocida con Solete Repsol."},
{"nombre":"La Mar de Fondo","concejo":"Navia","distincion":["Recomendado Repsol"],"especialidades":"Pescados y mariscos frente a la ría","tique_medio":"25-35€ aprox","desc":"Terraza junto a la ría de Navia con Solete de la Guía Repsol."},
{"nombre":"Casa Benigna","concejo":"Ponga","distincion":["Recomendado Repsol"],"especialidades":"Fabada y cocina de puchero","tique_medio":"20-30€ aprox","desc":"Casa de comidas en el Parque Natural de Ponga, referencia de fabada con Solete Repsol."},
{"nombre":"Casa Xico","concejo":"Llanes","distincion":["Recomendado Repsol"],"especialidades":"Fabada y platos de cuchara","tique_medio":"20-30€ aprox","desc":"Sidrería-asador tradicional en Llanes, distinguida con Solete de la Guía Repsol."},
{"nombre":"Casa Pilar","concejo":"Llanes (Nueva)","distincion":["Recomendado Repsol"],"especialidades":"Fabada asturiana","tique_medio":"20-30€ aprox","desc":"Restaurante tradicional en Nueva de Llanes, célebre por su fabada; 1 Sol Repsol."},
{"nombre":"Casa Adela","concejo":"Langreo","distincion":["Recomendado Repsol"],"especialidades":"Cocina casera y fabada","tique_medio":"20-30€ aprox","desc":"Casa de comidas de la cuenca del Nalón con Solete de la Guía Repsol."},
{"nombre":"Casa Eladia","concejo":"Villaviciosa","distincion":["Recomendado Repsol"],"especialidades":"Cocina casera asturiana","tique_medio":"20-30€ aprox","desc":"Restaurante tradicional en la comarca de la sidra, con Solete Repsol."},
{"nombre":"Casa Ricardo","concejo":"Ponga (Sellaño)","distincion":["Recomendado Repsol"],"especialidades":"Fabada y platos típicos de montaña","tique_medio":"20-30€ aprox","desc":"Casa de comidas de montaña en Sellaño (Ponga), con Solete de la Guía Repsol."},
{"nombre":"La Nueva Allandesa","concejo":"Allande (Pola de Allande)","distincion":["Recomendado Repsol"],"especialidades":"Cocina tradicional del occidente asturiano","tique_medio":"20-30€ aprox","desc":"Restaurante de referencia en Pola de Allande, con Solete de la Guía Repsol."},
{"nombre":"El Torneiro","concejo":"Villayón","distincion":["Recomendado Repsol"],"especialidades":"Cocina tradicional del occidente asturiano","tique_medio":"20-30€ aprox","desc":"Restaurante rural en Villayón, reconocido con Solete Repsol."},
{"nombre":"Casa Poli","concejo":"Llanes (Vidiago)","distincion":["Recomendado Repsol"],"especialidades":"Marisco y pescado","tique_medio":"25-40€ aprox","desc":"Clásico de Vidiago (Llanes) con la distinción 'Solete con Solera' de la Guía Repsol."},
{"nombre":"Casa Marisa","concejo":"Ribadedeva (Colombres)","distincion":["Recomendado Repsol"],"especialidades":"Cocina asturiana de producto","tique_medio":"25-40€ aprox","desc":"Restaurante de referencia en el oriente asturiano, en Colombres, citado como parada gastronómica de la A-8."},
{"nombre":"Leypon","concejo":"Llanes","distincion":["Recomendado Repsol"],"especialidades":"Pescados y mariscos","tique_medio":"25-40€ aprox","desc":"Restaurante costero en Llanes especializado en producto del mar, incluido entre las paradas gastronómicas recomendadas por Repsol."},
{"nombre":"El Cafetín","concejo":"Colunga (Lastres)","distincion":["Recomendado Repsol"],"especialidades":"Cocina marinera con vistas al puerto","tique_medio":"25-40€ aprox","desc":"Restaurante con vistas al puerto de Lastres, recomendado por la Guía Repsol."},
{"nombre":"Casa Seín","concejo":"Ribadedeva (Bustio)","distincion":["Recomendado Repsol"],"especialidades":"Angulas y marisco","tique_medio":"30-50€ aprox","desc":"Especialistas en angulas y marisco en Bustio, junto a la ría del Deva; con Solete de la Guía Repsol."}
]
''')

SIDRERIAS_RAW = json.loads(r'''
[
{"nombre":"Sobiñagu","concejo":"Gijón","premiada":true,"premio":"Sidrería con más encanto, Gijón de Sidra 2025; Mejor Sidrería, Gijón de Sidra 2023","especialidad":"Cocina asturiana con producto de mar y su 'Bombón Sobiñagu'","desc":"Sidrería-restaurante de ambiente animado en Gijón, habitual entre las más premiadas del certamen Gijón de Sidra."},
{"nombre":"La Maniega","concejo":"Gijón","premiada":true,"premio":"Mejor Sidrería, Gijón de Sidra 2024; Mejor Equipo Sidrería-Llagar (con Sidra Trabanco), Gijón de Sidra 2025","especialidad":"Pescados, mariscos y cocina tradicional asturiana","desc":"Sidrería-restaurante gijonesa muy popular, elegida mejor sidrería en la 15ª edición de Gijón de Sidra."},
{"nombre":"Sidrería Champel","concejo":"Gijón","premiada":true,"premio":"Mejor Sidrería, Gijón de Sidra 2025","especialidad":"Cocina asturiana de mercado","desc":"Sidrería de barrio en Gijón, reconocida en la última edición del certamen Gijón de Sidra."},
{"nombre":"El Tendido","concejo":"Gijón","premiada":true,"premio":"Mejor Escanciadora, Gijón de Sidra 2024 (Jessica García); finalista Sidrería con más encanto 2025","especialidad":"Parrilla y pescado a la brasa","desc":"Sidrería-restaurante gijonesa conocida por su parrilla, premiada en el escanciado del certamen Gijón de Sidra."},
{"nombre":"La Tonada de la Guía","concejo":"Gijón","premiada":true,"premio":"Sidrería con más encanto, Gijón de Sidra 2024; finalista en 2025","especialidad":"Cocina asturiana con parrilla","desc":"Sidrería tradicional en Gijón distinguida por su ambiente en el certamen Gijón de Sidra."},
{"nombre":"Mesón Puente Romano","concejo":"Cangas de Onís","premiada":true,"premio":"Finalista Sidrería con más encanto, Gijón de Sidra 2025","especialidad":"Cocina asturiana de cuchara y parrilla","desc":"Sidrería-mesón junto al puente romano de Cangas de Onís, con reconocimiento en un certamen regional de sidra."},
{"nombre":"Peces de Madera","concejo":"Gijón","premiada":true,"premio":"Finalista Sidrería con más encanto, Gijón de Sidra 2025","especialidad":"Cocina asturiana de autor con producto de temporada","desc":"Sidrería-restaurante gijonesa de ambiente actual dentro de la tradición sidrera."},
{"nombre":"Tururú Sidrería","concejo":"Gijón","premiada":true,"premio":"Mejor Plato ('Crema de berza y su torrezno'), Gijón de Sidra 2024","especialidad":"Cocina tradicional de cuchara","desc":"Sidrería gijonesa centrada en platos de cuchara y cocina de siempre."},
{"nombre":"Restaurante Bar Cabaña Sidrería (Llagarín del Cabaña)","concejo":"Aller","premiada":true,"premio":"Mejor Equipo Sidrería-Llagar (con Sidra Frutos), Gijón de Sidra 2024","especialidad":"Cocina de montaña y carnes a la parrilla","desc":"Sidrería con llagar propio en Cabañaquinta, concejo de Aller, en la montaña central asturiana."},
{"nombre":"Sidrería Avenida","concejo":"Colunga","premiada":true,"premio":"Mejor Escanciador, Gijón de Sidra 2023 (Wilkin Aquiles)","especialidad":"Cocina asturiana tradicional","desc":"Sidrería de la Comarca de la Sidra ubicada en Colunga, con reconocimiento al escanciado."},
{"nombre":"El Chaflán","concejo":"Gijón","premiada":true,"premio":"Mejor Equipo Sidrería-Llagar y Premio a la Trayectoria (Lucinda Álvarez), Gijón de Sidra 2023","especialidad":"Pescados a la parrilla y carne a la piedra","desc":"Sidrería clásica gijonesa, muy popular por su parrilla y su larga trayectoria."},
{"nombre":"La Montera Picona de Ramón","concejo":"Gijón","premiada":true,"premio":"Sidrería con más encanto, Gijón de Sidra 2023; Mejor Equipo de Escanciadores, Campeonato de Asturias 2024","especialidad":"Cocina tradicional asturiana y pescado de rula","desc":"Sidrería gijonesa de gran tradición escanciadora, cantera habitual de campeones regionales."},
{"nombre":"Los Pomares","concejo":"Gijón","premiada":true,"premio":"1er premio Concurso Mejor Fabada del Mundo 2015; finalista Gijón de Sidra 2023","especialidad":"Fabada asturiana","desc":"Sidrería-restaurante gijonesa de gran tradición, célebre por su fabada premiada."},
{"nombre":"La Cabaña del Santu","concejo":"Gijón","premiada":true,"premio":"Finalista, Gijón de Sidra 2023","especialidad":"Cocina asturiana con pescados y mariscos","desc":"Sidrería de referencia en Gijón, con ambiente típico y buena reputación gastronómica."},
{"nombre":"La Casona de Jovellanos","concejo":"Gijón","premiada":true,"premio":"Premio a la Trayectoria / 'Cocinar con corazón' (María Luisa Acera), Gijón de Sidra 2024","especialidad":"Cocina asturiana en casona histórica","desc":"Sidrería histórica ubicada en un hotel-casona del centro de Gijón."},
{"nombre":"Bodegas Anchón","concejo":"Gijón","premiada":true,"premio":"Finalista Sub-25 y Top 10, Campeonato de Escanciadores de Asturias 2024 (Isabella Padrón)","especialidad":"Cocina casera asturiana","desc":"Sidrería de ambiente de bodega tradicional en Gijón, cantera de jóvenes escanciadores."},
{"nombre":"Sidrería Tierra Astur","concejo":"Oviedo","premiada":true,"premio":"Campeón Regional de Escanciadores 2024 y 2025 (Salvador Ondó); 2º Mejor Equipo, Campeonato de Asturias 2024","especialidad":"Embutidos, quesos y matanza asturiana","desc":"Gran sidrería-tienda de referencia en Oviedo, con llagar propio y una de las cadenas sidreras más conocidas de Asturias."},
{"nombre":"Sidrería El Portal","concejo":"Villaviciosa","premiada":true,"premio":"3er Mejor Equipo, Campeonato de Escanciadores de Asturias 2024","especialidad":"Cocina tradicional asturiana y pescado","desc":"Sidrería-restaurante en el centro de Villaviciosa, corazón de la Comarca de la Sidra."},
{"nombre":"Sidrería La Marina","concejo":"Gijón","premiada":false,"premio":"","especialidad":"Pescado fresco del Cantábrico","desc":"Chigre animado en el barrio de El Carmen de Gijón, de servicio rápido."},
{"nombre":"Sidrería El Cruce","concejo":"Gijón","premiada":false,"premio":"","especialidad":"Fabada asturiana y caza","desc":"Sidrería tradicional en Cabueñes (Gijón) con terrazas familiares y precios asequibles."},
{"nombre":"El Restallu","concejo":"Gijón","premiada":false,"premio":"","especialidad":"Arroz con bogavante y marisco","desc":"Sidrería-restaurante gijonesa muy popular, imprescindible reservar por su arroz con marisco."},
{"nombre":"Casa Trabanco","concejo":"Gijón","premiada":false,"premio":"","especialidad":"Carnes a la parrilla y bacalao a la sidra","desc":"Llagar con sidrería y producción propia en Lavandera (Gijón), ofrece visitas guiadas al proceso de elaboración."},
{"nombre":"Sidrería El Globo","concejo":"Gijón","premiada":false,"premio":"","especialidad":"Cocina asturiana de raciones abundantes","desc":"Sidrería céntrica de Gijón con ambiente clásico y sangría de sidra."},
{"nombre":"Restaurante Sidrería La Galana","concejo":"Gijón","premiada":false,"premio":"","especialidad":"Menú del día y cocina asturiana","desc":"Chigre tradicional en la Plaza Mayor de Gijón, con decoración de madera típica."},
{"nombre":"Sidrería Candasu","concejo":"Gijón","premiada":false,"premio":"","especialidad":"Marisco y pescado","desc":"Sidrería con varios ambientes en la zona de Nuevo Gijón."},
{"nombre":"Sidrería El Mallu","concejo":"Gijón","premiada":false,"premio":"","especialidad":"Cocina asturiana de raciones generosas","desc":"Sidrería gijonesa muy concurrida, conviene reservar con antelación."},
{"nombre":"Sidrería El Alleranu Casa Javi","concejo":"Gijón","premiada":false,"premio":"","especialidad":"Pescado y marisco a la parrilla","desc":"Sidrería gijonesa conocida por el trato cercano y el pescado a la parrilla."},
{"nombre":"Las Güelas Gascona","concejo":"Oviedo","premiada":false,"premio":"","especialidad":"Cocina asturiana tradicional","desc":"Sidrería situada en pleno bulevar de la sidra (calle Gascona) de Oviedo."},
{"nombre":"La Pumarada","concejo":"Oviedo","premiada":false,"premio":"","especialidad":"Marisquería y sidrería","desc":"Sidrería-marisquería de referencia en el centro de Oviedo."},
{"nombre":"Sidrería La Finca","concejo":"Oviedo","premiada":false,"premio":"","especialidad":"Cocina de producto de huerta y sidra","desc":"Sidrería-agrobar en Oviedo con enfoque en producto de proximidad."},
{"nombre":"Sidrería La Cabaña","concejo":"Oviedo","premiada":false,"premio":"","especialidad":"Cocina asturiana tradicional","desc":"Sidrería situada en la calle Gascona, el histórico bulevar de la sidra de Oviedo."},
{"nombre":"Sidrería Bedriñana","concejo":"Villaviciosa","premiada":false,"premio":"","especialidad":"Cocina de mar y tierra","desc":"Sidrería en la parroquia de Bedriñana, Villaviciosa, corazón de la comarca sidrera."},
{"nombre":"Sidrería La Tierrina","concejo":"Villaviciosa","premiada":false,"premio":"","especialidad":"Cocina tradicional asturiana","desc":"Sidrería familiar en el concejo de Villaviciosa."},
{"nombre":"Sidrería Restaurante Plaza","concejo":"Nava","premiada":false,"premio":"","especialidad":"Cocina asturiana tradicional","desc":"Sidrería en pleno centro de Nava, la 'capital de la sidra'."},
{"nombre":"Llagar Sidra Estrada","concejo":"Nava","premiada":false,"premio":"","especialidad":"Sidra natural de elaboración propia","desc":"Llagar con sidrería en Nava donde se degusta sidra de producción propia."},
{"nombre":"Sidrería El Chigre","concejo":"Avilés","premiada":false,"premio":"","especialidad":"Pinchos y tapas asturianas","desc":"Chigre tradicional en el centro de Avilés, de ambiente castizo."},
{"nombre":"Sidrería Tierra Astur Avilés","concejo":"Avilés","premiada":false,"premio":"","especialidad":"Embutidos, quesos y matanza asturiana","desc":"Sucursal avilesina de la conocida cadena de sidrerías Tierra Astur."},
{"nombre":"Casa Marisa","concejo":"Avilés","premiada":false,"premio":"","especialidad":"Cocina asturiana casera","desc":"Sidrería-restaurante familiar en el centro de Avilés."},
{"nombre":"La Taberna de Mario","concejo":"Avilés","premiada":false,"premio":"","especialidad":"Tapas y pinchos asturianos","desc":"Sidrería-taberna en la Plaza del Carbayo de Avilés."},
{"nombre":"Sidrería La Ovetense","concejo":"Cangas de Onís","premiada":false,"premio":"","especialidad":"Cocina asturiana de montaña","desc":"Sidrería tradicional en el centro de Cangas de Onís, puerta de los Picos de Europa."},
{"nombre":"Restaurante Sidrería La Guía","concejo":"Ribadesella","premiada":false,"premio":"","especialidad":"Pescado y marisco","desc":"Sidrería-restaurante en el casco urbano de Ribadesella con amplia terraza."},
{"nombre":"Sidrería Carroceu","concejo":"Ribadesella","premiada":false,"premio":"","especialidad":"Pescado del Cantábrico","desc":"Sidrería junto al muelle de Ribadesella, con vistas a la playa."},
{"nombre":"Sidrería El Puerto","concejo":"Ribadesella","premiada":false,"premio":"","especialidad":"Marisco y pescado","desc":"Sidrería renovada en la villa marinera de Ribadesella."},
{"nombre":"Sidrería El Antoju","concejo":"Llanes","premiada":false,"premio":"","especialidad":"Cocina asturiana tradicional","desc":"Sidrería muy valorada en el casco histórico de Llanes."},
{"nombre":"Sidrería La Casona de Llanes","concejo":"Llanes","premiada":false,"premio":"","especialidad":"Cocina tradicional asturiana","desc":"Sidrería en el corazón de Llanes, en un edificio de carácter tradicional."},
{"nombre":"Sidrería Narcea","concejo":"Cangas del Narcea","premiada":false,"premio":"","especialidad":"Cocina tradicional del occidente asturiano","desc":"Sidrería regentada por familia local en Cangas del Narcea, conocida por su hospitalidad."},
{"nombre":"Sidrería El Remo","concejo":"Cudillero","premiada":false,"premio":"","especialidad":"Pescado y marisco fresco","desc":"Sidrería con vistas al puerto pesquero de Cudillero."},
{"nombre":"Sidrería Feudo Real","concejo":"Grado","premiada":false,"premio":"","especialidad":"Cocina asturiana de mercado","desc":"Sidrería de ambiente rústico-moderno en Grado, occidente central de Asturias."},
{"nombre":"Sidrería Casa Ricardo","concejo":"Salas","premiada":false,"premio":"","especialidad":"Escalopines al cabrales y cocina de interior","desc":"Sidrería tradicional en la villa de Salas, occidente de Asturias."},
{"nombre":"Sidrería Antolín","concejo":"Navia","premiada":false,"premio":"","especialidad":"Pescado de rula y marisco","desc":"Sidrería costera en Navia especializada en pescado fresco."},
{"nombre":"Sidrería Casa Jano","concejo":"Vegadeo","premiada":false,"premio":"","especialidad":"Parrilla de carnes","desc":"Sidrería con amplia terraza en Vegadeo, extremo occidental de Asturias."},
{"nombre":"Sidrería Bar Brisas Candasinas","concejo":"Carreño","premiada":false,"premio":"","especialidad":"Pescado y marisco","desc":"Sidrería marinera en la villa de Candás, concejo de Carreño."},
{"nombre":"Sidrería El Gayo","concejo":"Gozón","premiada":false,"premio":"","especialidad":"Cocina marinera","desc":"Sidrería en Luanco, villa pesquera del concejo de Gozón."},
{"nombre":"Sidrería El Parque","concejo":"Siero","premiada":false,"premio":"","especialidad":"Cocina asturiana tradicional","desc":"Sidrería clásica en Pola de Siero, en el centro de Asturias."},
{"nombre":"Sidrería El Llagar","concejo":"Colunga","premiada":false,"premio":"","especialidad":"Cocina de mar y montaña","desc":"Sidrería en Colunga, entre la costa y la Comarca de la Sidra."}
]
''')

LAGARES_RAW = json.loads(r'''
[
{"nombre":"Sidra Trabanco","concejo":"Gijón (Lavandera)","premiada":true,"premio":"Mejor Sidra - Gijón de Sidra 2025 (Sidra Tradicional Amarilla)","especialidad":"Sidra natural tradicional","desc":"Uno de los llagares más conocidos de Asturias, con visitas guiadas, tienda y sidrería propia junto a las pumaradas."},
{"nombre":"Sidra Acebal","concejo":"Gijón (Cabueñes)","premiada":false,"premio":"","especialidad":"Sidra natural","desc":"Llagar tradicional en Cabueñes, parada habitual de la Ruta de la Sidra de Gijón, con venta directa al público."},
{"nombre":"Sidra Piñera","concejo":"Gijón (Deva)","premiada":false,"premio":"","especialidad":"Sidra natural","desc":"Llagar familiar en la carretera Caldones-Deva, con producción y venta directa en el propio recinto."},
{"nombre":"Sidra J.R.","concejo":"Gijón (Alto Infanzón)","premiada":false,"premio":"","especialidad":"Sidra natural","desc":"Pequeño llagar familiar gijonés con venta directa, menos conocido que los grandes llagares de la zona."},
{"nombre":"Sidra Menéndez","concejo":"Gijón (Fano)","premiada":true,"premio":"Manzana acogida a la D.O.P. Sidra de Asturias; pomaradas certificadas en cultivo ecológico","especialidad":"Sidra ecológica D.O.P.","desc":"Llagar con larga tradición familiar en Fano, elaborado en toneles de castaño, con tienda propia y venta directa."},
{"nombre":"Llagar Bernueces","concejo":"Gijón (Bernueces)","premiada":false,"premio":"","especialidad":"Sidra natural","desc":"Llagar tradicional gijonés, una de las seis paradas oficiales de la Ruta de la Sidra de Gijón."},
{"nombre":"Llagar de Sidra Cabueñes","concejo":"Gijón (Cabueñes)","premiada":false,"premio":"","especialidad":"Sidra natural","desc":"Llagar-sidrería en el barrio de Cabueñes con producción propia y venta directa."},
{"nombre":"Sidra Canal","concejo":"Gijón (Lavandera)","premiada":false,"premio":"","especialidad":"Sidra natural (elaborando desde 1955)","desc":"Llagar familiar gijonés con más de 65 años de tradición, sidrería propia y venta directa."},
{"nombre":"Sidra Fran","concejo":"Siero (Lugones)","premiada":false,"premio":"","especialidad":"Sidra natural","desc":"Llagar en Lugones con tienda y sidrería, punto de venta directa en el área metropolitana de Siero."},
{"nombre":"Llagar Quelo","concejo":"Siero (Tiñana)","premiada":false,"premio":"","especialidad":"Sidra natural","desc":"Llagar-restaurante en Tiñana con producción propia, venta directa y organización de eventos."},
{"nombre":"Sidra Fonciello","concejo":"Siero","premiada":false,"premio":"","especialidad":"Sidra natural, venta online","desc":"Llagar sierense con tienda física y online de sidra natural, además de visitas al lagar."},
{"nombre":"Sidra Alonso","concejo":"Langreo","premiada":false,"premio":"","especialidad":"Sidra natural","desc":"Llagar-sidrería en Langreo, uno de los pocos puntos de venta directa de sidra en la cuenca del Nalón."},
{"nombre":"Llagar Panizales","concejo":"Mieres","premiada":false,"premio":"","especialidad":"Sidra natural","desc":"Llagar en Mieres con venta y degustación, representando la producción sidrera de las cuencas mineras."},
{"nombre":"Sidra Herminio","concejo":"Oviedo (Colloto)","premiada":false,"premio":"","especialidad":"Sidra natural (fundada en 1943)","desc":"Histórico llagar familiar en Colloto con más de 80 años de tradición, llagar propio y venta directa."},
{"nombre":"Sidra Castañón","concejo":"Villaviciosa (Quintueles)","premiada":true,"premio":"Ganador del Concurso de Sidra Natural con su marca Val de Boides D.O.P.","especialidad":"Val de Boides D.O.P.","desc":"Llagar familiar desde 1938, referente de la D.O.P. Sidra de Asturias con numerosos premios en concursos de sidra natural."},
{"nombre":"Sidra Cortina","concejo":"Villaviciosa (Amandi)","premiada":false,"premio":"","especialidad":"Sidra natural y sidra de hielo","desc":"Llagar en Amandi, cuna histórica de la sidra asturiana, con gama que incluye sidra de hielo y venta directa."},
{"nombre":"Sidra El Gaitero","concejo":"Villaviciosa (La Espuncia)","premiada":true,"premio":"Trayectoria de reconocimientos desde 1890; marca sidrera asturiana más exportada internacionalmente","especialidad":"Sidra achampanada/espumosa","desc":"La sidrera más antigua y de mayor proyección internacional de Asturias, con museo, visitas guiadas y tienda."},
{"nombre":"Llagar Sidra Coro","concejo":"Villaviciosa","premiada":false,"premio":"","especialidad":"Sidra natural","desc":"Llagar villaviciosino con producción y venta directa, integrado en la ruta sidrera local."},
{"nombre":"Llagar Sidra Vigón","concejo":"Villaviciosa (Tornón)","premiada":false,"premio":"","especialidad":"Sidra natural","desc":"Llagar familiar en Tornón con tienda propia y venta directa al público."},
{"nombre":"Llagar Sidra Frutos","concejo":"Villaviciosa (Quintueles)","premiada":false,"premio":"","especialidad":"Sidra natural","desc":"Llagar en Quintueles con venta directa, uno de los puntos habituales de la fiesta sidrera de Villaviciosa."},
{"nombre":"Llagar Mayador (M. Busto)","concejo":"Villaviciosa","premiada":true,"premio":"Ganador de la cata popular en la Fiesta de la Sidra Natural de Villaviciosa","especialidad":"Sidra natural","desc":"Llagar villaviciosino reconocido en la cata popular de la fiesta local de la sidra."},
{"nombre":"Llagar Buznego","concejo":"Villaviciosa","premiada":false,"premio":"","especialidad":"Sidra natural","desc":"Llagar histórico, participante habitual de la Fiesta de la Sidra Natural de Villaviciosa."},
{"nombre":"Llagar El Gobernador","concejo":"Villaviciosa (Sopeña)","premiada":true,"premio":"Premio a la etiqueta más bonita, Fiesta de la Sidra de Villaviciosa","especialidad":"Sidra Sopeña","desc":"Llagar en Sopeña conocido por su marca 'Sopeña' y reconocido por el diseño de su etiqueta."},
{"nombre":"Llagar Sidra Muñiz","concejo":"Villaviciosa","premiada":false,"premio":"","especialidad":"Sidra natural","desc":"Llagar villaviciosino con venta directa y presencia habitual en la fiesta local de la sidra."},
{"nombre":"Sidra Viuda de Angelón (Pomar)","concejo":"Nava (Villa)","premiada":true,"premio":"Mejor Sidra de Asturias (varios años desde 1982); Sidra Más Prestosa - Gijón de Sidra 2025; Oro en Sagardo Forum 2025","especialidad":"Sidra de hielo, natural y achampanada","desc":"Uno de los llagares más laureados de Asturias, con décadas de premios en concursos regionales e internacionales."},
{"nombre":"Llagar Orizón","concejo":"Nava","premiada":false,"premio":"","especialidad":"Sidra natural","desc":"Llagar navetu con venta directa, integrado en la ruta sidrera de la Comarca de la Sidra."},
{"nombre":"Llagar Sidra Zapatero","concejo":"Nava","premiada":false,"premio":"","especialidad":"Sidra natural","desc":"Llagar familiar en Nava con producción y venta directa al público."},
{"nombre":"Sidra Viuda de Corsino","concejo":"Nava","premiada":true,"premio":"Mejor Sidra Local - Festival de la Sidra de Nava 2026","especialidad":"Sidra natural","desc":"Llagar histórico de Nava galardonado como mejor sidra local en el festival del concejo."},
{"nombre":"Llagar Foncueva","concejo":"Sariego","premiada":true,"premio":"Mencionado entre las mejores sidras de Asturias y del Festival de Nava (junto a Viuda de Corsino)","especialidad":"Sidra natural","desc":"Llagar sariegano reconocido entre las mejores sidras de la región en certámenes recientes."},
{"nombre":"Llagar Ismael Bastián","concejo":"Sariego","premiada":false,"premio":"","especialidad":"Sidra natural artesanal","desc":"Pequeño llagar familiar en Sariego, de producción limitada, con visitas y venta directa."},
{"nombre":"Sidra Crespo","concejo":"Colunga","premiada":false,"premio":"","especialidad":"Sidra natural","desc":"Llagar en Colunga con visitas guiadas organizadas junto al ayuntamiento y venta directa."},
{"nombre":"Llagar Finca Ecológica El Noceu","concejo":"Colunga (Santiago)","premiada":false,"premio":"","especialidad":"Sidra ecológica","desc":"Llagar ecológico en Santiago de Colunga, con producción respetuosa con el medio y venta directa."}
]
''')

SITIOS_RAW = json.loads(r'''
[
 {
  "nombre": "Casco histórico y Cubos de la Memoria",
  "concejo": "Llanes",
  "categoria": "patrimonio",
  "desc": "El paseo de San Pedro, sobre el acantilado junto al puerto, combina la muralla medieval con los coloristas Cubos de la Memoria pintados por Agustín Ibarrola. Es la postal más fotografiada de la villa y un paseo obligado junto al puerto pesquero."
 },
 {
  "nombre": "Basílica de Santa María del Conceyu",
  "concejo": "Llanes",
  "categoria": "monumento",
  "desc": "Iglesia gótica del siglo XIII-XIV situada en pleno casco urbano de Llanes, con un notable rosetón y portada esculpida. Es el principal monumento religioso de la villa y punto de referencia del centro histórico."
 },
 {
  "nombre": "Playa de Gulpiyuri",
  "concejo": "Llanes (Naves)",
  "categoria": "otro",
  "desc": "Monumento Natural único: una playa de arena situada a 100 metros del mar, en el interior de un prado, alimentada por el oleaje a través de galerías subterráneas kársticas. Uno de los fenómenos geológicos más curiosos de la costa asturiana."
 },
 {
  "nombre": "Cueva de Tito Bustillo",
  "concejo": "Ribadesella",
  "categoria": "cueva",
  "desc": "Cueva con arte rupestre paleolítico declarada Patrimonio de la Humanidad por la UNESCO, con pinturas de caballos y ciervos de gran calidad. Cuenta con centro de interpretación y visitas guiadas con aforo limitado, por lo que conviene reservar con antelación."
 },
 {
  "nombre": "Casco histórico y Barrio de Guía",
  "concejo": "Ribadesella",
  "categoria": "patrimonio",
  "desc": "La villa marinera se reparte a ambos lados de la ría del Sella: el paseo marítimo y casco antiguo en una orilla, y el tradicional Barrio de Guía, de pescadores, en la otra. Es además la salida del famoso Descenso Internacional del Sella."
 },
 {
  "nombre": "Cueva de El Pindal",
  "concejo": "Ribadedeva (Pimiango)",
  "categoria": "cueva",
  "desc": "Cueva prehistórica sobre los acantilados de Pimiango, con pinturas paleolíticas de bisontes, caballos y el célebre 'pez' rojo, integrada en el Patrimonio Mundial del arte rupestre paleolítico del Cantábrico. Las visitas guiadas incluyen un tramo con vistas al mar desde la propia boca de la cueva."
 },
 {
  "nombre": "Colombres y la Quinta Guadalupe",
  "concejo": "Ribadedeva (Colombres)",
  "categoria": "patrimonio",
  "desc": "Colombres es la capital de la 'ruta de los indianos', con vistosos palacetes construidos por emigrantes que hicieron fortuna en América. Destaca la Quinta Guadalupe, sede de la Fundación Archivo de Indianos, con su jardín y arquitectura de inspiración colonial."
 },
 {
  "nombre": "Puente Romano de Cangas de Onís",
  "concejo": "Cangas de Onís",
  "categoria": "monumento",
  "desc": "Símbolo de Asturias, este puente medieval (de origen bajomedieval pese a su nombre popular) cruza el río Sella con su característica réplica de la Cruz de la Victoria colgando del arco central. Es el lugar más fotografiado de la primera capital del Reino de Asturias."
 },
 {
  "nombre": "Santuario de Covadonga",
  "concejo": "Cangas de Onís (Covadonga)",
  "categoria": "monumento",
  "desc": "Lugar fundacional de la Reconquista: la Basílica neorrománica y la Santa Cueva, con la imagen de la Virgen y el sepulcro de Don Pelayo, atraen cada año a miles de peregrinos y visitantes. El entorno, con la cascada junto a la cueva, es de gran valor simbólico y paisajístico."
 },
 {
  "nombre": "Lagos de Covadonga (Enol y Ercina)",
  "concejo": "Cangas de Onís (Covadonga)",
  "categoria": "otro",
  "desc": "Dos lagos de origen glaciar en pleno macizo de los Picos de Europa, rodeados de prados de alta montaña donde pastan vacas y caballos en verano. El acceso en temporada alta está restringido a autobús lanzadera desde Cangas de Onís por la gran afluencia."
 },
 {
  "nombre": "Parque Nacional de los Picos de Europa",
  "concejo": "Cangas de Onís",
  "categoria": "parque-natural",
  "desc": "Primer Parque Nacional de España (1918), con imponentes macizos calizos, gargantas y cumbres de más de 2.600 m. Cangas de Onís es la puerta de entrada principal, con oficinas de información y acceso a numerosas rutas de senderismo."
 },
 {
  "nombre": "Cueva del Buxu",
  "concejo": "Onís (Cardes)",
  "categoria": "cueva",
  "desc": "Pequeña cueva con grabados y pinturas paleolíticas de caballos, ciervos y signos, parte también del conjunto de arte rupestre del Cantábrico reconocido por la UNESCO. Las visitas son en grupos muy reducidos, lo que la hace una experiencia íntima."
 },
 {
  "nombre": "La Cuevona de Cuevas del Agua",
  "concejo": "Onís (Cuevas)",
  "categoria": "otro",
  "desc": "Curiosa cueva natural de más de 300 metros por la que discurre tanto un río como una carretera asfaltada de un solo carril, algo insólito en España. Es una parada muy popular entre familias por lo peculiar de atravesarla en coche o a pie."
 },
 {
  "nombre": "Desfiladero de los Beyos",
  "concejo": "Amieva",
  "categoria": "otro",
  "desc": "Espectacular garganta excavada por el río Sella entre paredes calizas casi verticales, que se recorre por la carretera N-625 entre Amieva y Ponga. Varios miradores a lo largo del trayecto ofrecen vistas vertiginosas del cañón."
 },
 {
  "nombre": "Sames",
  "concejo": "Amieva",
  "categoria": "pueblo",
  "desc": "Capital del concejo de Amieva, es un pueblo tradicional de arquitectura de montaña rodeado de prados y bosques, con su iglesia parroquial como centro. Sirve de base habitual para excursiones a los Picos de Europa y al desfiladero de los Beyos."
 },
 {
  "nombre": "Parque Natural de Ponga",
  "concejo": "Ponga",
  "categoria": "parque-natural",
  "desc": "Reserva de la Biosfera con uno de los hayedos mejor conservados de Europa, además de tejos centenarios, roquedos calizos y una rica fauna (oso pardo, rebeco). Sus pueblos de pastores y sus rutas de senderismo lo convierten en un destino para amantes de la naturaleza poco masificado."
 },
 {
  "nombre": "San Juan de Beleño",
  "concejo": "Ponga",
  "categoria": "pueblo",
  "desc": "Capital administrativa de Ponga, con arquitectura tradicional de piedra y hórreos, enclavada en un valle rodeado de montañas. Es el punto de partida habitual para adentrarse en el Parque Natural de Ponga."
 },
 {
  "nombre": "Parque Natural de Redes",
  "concejo": "Caso",
  "categoria": "parque-natural",
  "desc": "Reserva de la Biosfera compartida con Sobrescobio, con el impresionante Bosque de Peloño (uno de los mejores hayedos de la Cordillera Cantábrica) y valles de gran valor ecológico. Es hábitat de oso pardo, urogallo y otras especies protegidas."
 },
 {
  "nombre": "Puerto y Campa de Tarna",
  "concejo": "Caso (Tarna)",
  "categoria": "mirador",
  "desc": "El pequeño pueblo de Tarna, junto al puerto de montaña que da paso a León, ofrece amplias vistas de prados de alta montaña y antiguas brañas de pastores. Fue sede de una histórica estación de esquí y conserva un fuerte carácter rural."
 },
 {
  "nombre": "Monumento Natural Ruta del Alba",
  "concejo": "Sobrescobio",
  "categoria": "otro",
  "desc": "Ruta que sigue el curso del río Alba entre bosques y pasarelas de madera junto a pozas de aguas cristalinas, dentro del Parque Natural de Redes. Es uno de los paseos fluviales más populares y accesibles de la comarca."
 },
 {
  "nombre": "Ecomuseo Molín de Xuacu",
  "concejo": "Sobrescobio (Rioseco)",
  "categoria": "museo",
  "desc": "Conjunto etnográfico junto al río Alba que recupera antiguos molinos hidráulicos y muestra oficios tradicionales de la zona, como la fabricación de mantas de lana (la 'llagüería'). Un buen complemento cultural a la visita del Parque Natural de Redes."
 },
 {
  "nombre": "Mirador del Fitu",
  "concejo": "Parres",
  "categoria": "mirador",
  "desc": "Situado en la Sierra del Sueve a más de 600 m de altitud, su curiosa plataforma circular ofrece vistas de 360 grados que abarcan la costa asturiana, la ría de Ribadesella y los picos nevados de Picos de Europa en días claros. Es uno de los miradores más famosos y fotografiados de Asturias."
 },
 {
  "nombre": "Arriondas",
  "concejo": "Parres",
  "categoria": "otro",
  "desc": "Villa fluvial a orillas del Sella, conocida internacionalmente por ser la salida del Descenso Internacional del Sella cada agosto, una de las fiestas más multitudinarias de Asturias. Su casco urbano y paseo junto al río son agradables para el paseo y la gastronomía."
 },
 {
  "nombre": "Espinaredo",
  "concejo": "Piloña",
  "categoria": "pueblo",
  "desc": "Conocido como el pueblo con más hórreos y paneras de Asturias en relación a su tamaño, conserva un urbanismo tradicional casi intacto junto a un molino de agua. Es una parada muy fotogénica para entender la arquitectura rural asturiana."
 },
 {
  "nombre": "Iglesia de Santa María de Villamayor",
  "concejo": "Piloña (Villamayor)",
  "categoria": "monumento",
  "desc": "Templo románico del siglo XIII con una portada esculpida de notable calidad, uno de los mejores ejemplos de arte románico rural de Asturias. Se encuentra en un entorno tranquilo típico de la campiña de Piloña."
 },
 {
  "nombre": "Bulnes y el Naranjo de Bulnes",
  "concejo": "Cabrales (Bulnes)",
  "categoria": "otro",
  "desc": "Pueblo enclavado en el corazón del Macizo Central de los Picos de Europa, accesible solo a pie o mediante un funicular subterráneo desde Poncebos (el único de este tipo en España). Es la base tradicional de los alpinistas que ascienden al Naranjo de Bulnes (Picu Urriellu), la torre caliza más icónica de la cordillera."
 },
 {
  "nombre": "Garganta del Cares (Ruta del Cares)",
  "concejo": "Cabrales (Poncebos)",
  "categoria": "otro",
  "desc": "Considerada una de las mejores rutas de senderismo de España, discurre tallada en la roca entre desfiladeros de más de 1.000 metros de desnivel, uniendo Poncebos con Caín. Un recorrido espectacular apto para cualquier persona con un mínimo de forma física."
 },
 {
  "nombre": "Cueva-exposición del Queso de Cabrales",
  "concejo": "Cabrales (Arenas de Cabrales)",
  "categoria": "museo",
  "desc": "Espacio museístico instalado en una auténtica cueva de maduración que explica el proceso de elaboración del famoso queso de Cabrales, con Denominación de Origen Protegida. Incluye degustación y es una parada muy recomendable para entender la cultura gastronómica de la zona."
 },
 {
  "nombre": "Alles",
  "concejo": "Peñamellera Alta",
  "categoria": "pueblo",
  "desc": "Capital del concejo, es un pueblo tranquilo de arquitectura tradicional montañesa rodeado de prados verdes al pie de los Picos de Europa. Buena base para rutas de senderismo menos concurridas que las de Cangas de Onís o Cabrales."
 },
 {
  "nombre": "Cueva de Coímbre",
  "concejo": "Peñamellera Alta",
  "categoria": "cueva",
  "desc": "Yacimiento con arte rupestre paleolítico, parte del conjunto de cuevas del Cantábrico reconocidas por su valor científico. Su entorno, en un paraje kárstico apenas transitado, resulta atractivo incluso para quien no pueda acceder al interior."
 },
 {
  "nombre": "Panes",
  "concejo": "Peñamellera Baja",
  "categoria": "pueblo",
  "desc": "Capital del concejo y puerta oriental de acceso a los Picos de Europa desde Cantabria, con un pequeño casco histórico junto al río Cares-Deva. Es un buen punto de paso y avituallamiento para quienes se adentran hacia Cabrales o Peñamellera Alta."
 },
 {
  "nombre": "Lastres",
  "concejo": "Colunga",
  "categoria": "pueblo",
  "desc": "Uno de los pueblos marineros más bonitos de Asturias (parte de la red 'Los Pueblos más Bonitos de España'), con sus calles empedradas en cuesta, el puerto pesquero y el faro asomado al Cantábrico. Ganó popularidad como escenario de la serie 'Doctor Mateo'."
 },
 {
  "nombre": "Museo del Jurásico de Asturias (MUJA)",
  "concejo": "Colunga",
  "categoria": "museo",
  "desc": "Museo con forma de huella de dinosaurio situado en un acantilado con vistas al mar, dedicado a la rica 'Costa de los Dinosaurios' asturiana, con réplicas a tamaño real e icnitas (huellas fósiles) originales. Muy recomendable para visitar en familia junto con un paseo por la costa cercana a Lastres."
 },
 {
  "nombre": "Sierra del Sueve y Hayedo de la Biescona",
  "concejo": "Caravia",
  "categoria": "otro",
  "desc": "Macizo montañoso que se alza muy cerca del mar, con el Hayedo de la Biescona como uno de los pocos bosques de hayas de Europa próximos a la costa. La ruta de la Forquita y Cerracín permite conocer su arquitectura tradicional y su fauna, incluidos los asturcones (caballos autóctonos) en semilibertad."
 },
 {
  "nombre": "Catedral de San Salvador y Cámara Santa",
  "concejo": "Oviedo",
  "categoria": "monumento",
  "desc": "Catedral gótica que alberga la Cámara Santa (Patrimonio de la Humanidad), con orfebrería prerrománica como la Cruz de los Ángeles y la Cruz de la Victoria, símbolo de Asturias. Su claustro y torre son de visita obligada en el corazón de la ciudad."
 },
 {
  "nombre": "Casco histórico de Oviedo",
  "concejo": "Oviedo",
  "categoria": "patrimonio",
  "desc": "Paseo por la Plaza de la Catedral, el Fontán, la calle Rosal y el Ayuntamiento, con esculturas urbanas (Woody Allen, La Regenta) y arquitectura señorial. Es uno de los cascos históricos mejor conservados del norte de España."
 },
 {
  "nombre": "Santa María del Naranco",
  "concejo": "Oviedo (Monte Naranco)",
  "categoria": "monumento",
  "desc": "Antiguo palacio real de Ramiro I del siglo IX, joya del Prerrománico Asturiano y Patrimonio de la Humanidad. Sus arcos peraltados y balcones con vistas a Oviedo lo convierten en el monumento prerrománico más fotografiado de Asturias."
 },
 {
  "nombre": "San Miguel de Lillo",
  "concejo": "Oviedo (Monte Naranco)",
  "categoria": "monumento",
  "desc": "Iglesia prerrománica del siglo IX situada junto a Santa María del Naranco, Patrimonio de la Humanidad, con relieves esculpidos únicos en sus jambas que representan escenas circenses romanas. Se visita en el mismo recorrido que el palacio de Naranco."
 },
 {
  "nombre": "Iglesia de San Julián de los Prados (Santullano)",
  "concejo": "Oviedo",
  "categoria": "monumento",
  "desc": "La iglesia prerrománica más grande conservada de Europa (siglo IX), Patrimonio de la Humanidad, célebre por sus pinturas murales de tradición pompeyana, únicas en su género. Un imprescindible menos conocido que los monumentos del Naranco."
 },
 {
  "nombre": "Fuente de Foncalada",
  "concejo": "Oviedo",
  "categoria": "patrimonio",
  "desc": "Única obra pública civil conservada del Prerrománico Asturiano (siglo IX), integrada en el casco histórico de Oviedo y también inscrita como Patrimonio de la Humanidad. Pequeña pero con gran valor simbólico como testimonio del urbanismo de la corte astur."
 },
 {
  "nombre": "Museo de Bellas Artes de Asturias",
  "concejo": "Oviedo",
  "categoria": "museo",
  "desc": "Una de las mejores pinacotecas de España, con obras de Goya, El Greco, Picasso y grandes pintores asturianos, instalada en varios palacios históricos del casco antiguo. Entrada gratuita y colección en constante ampliación."
 },
 {
  "nombre": "Museo Arqueológico de Asturias",
  "concejo": "Oviedo",
  "categoria": "museo",
  "desc": "Ubicado en el antiguo monasterio de San Vicente, repasa la prehistoria y la historia de Asturias desde el Paleolítico hasta la Edad Media, con piezas del arte rupestre y del reino astur. Complementa perfectamente la visita al Prerrománico."
 },
 {
  "nombre": "Cerro de Santa Catalina y Cimavilla",
  "concejo": "Gijón",
  "categoria": "mirador",
  "desc": "Barrio marinero más antiguo de Gijón, con calles estrechas, sidrerías y el mirador donde se alza el 'Elogio del Horizonte' de Chillida, símbolo de la ciudad frente al Cantábrico. Excelente panorámica de la playa de San Lorenzo y el puerto."
 },
 {
  "nombre": "Universidad Laboral de Gijón",
  "concejo": "Gijón",
  "categoria": "monumento",
  "desc": "Uno de los edificios más grandes de España, con una torre mirador de más de 100 m y un impresionante teatro y capilla. Hoy es Laboral Ciudad de la Cultura, con visitas guiadas a su arquitectura monumental de los años 50."
 },
 {
  "nombre": "Museo del Ferrocarril de Asturias",
  "concejo": "Gijón",
  "categoria": "museo",
  "desc": "Instalado en la antigua estación de Norte, reúne locomotoras históricas, vagones y material ferroviario que narran la industrialización de Asturias. Uno de los museos ferroviarios más completos de España."
 },
 {
  "nombre": "Museo del Pueblo de Asturias",
  "concejo": "Gijón",
  "categoria": "museo",
  "desc": "Conjunto etnográfico al aire libre con hórreos, una gaita gigante y la Gaita de Oro, dedicado a la cultura y las tradiciones asturianas. Incluye también el Muséu del Pueblu d'Asturies y el archivo fotográfico regional."
 },
 {
  "nombre": "Termas Romanas de Campo Valdés",
  "concejo": "Gijón",
  "categoria": "patrimonio",
  "desc": "Restos arqueológicos de unas termas públicas romanas del siglo I-II, visibles bajo la playa de San Lorenzo, junto a la iglesia de San Pedro. Testimonio del origen romano de Gijón (Gigia)."
 },
 {
  "nombre": "Palacio de Revillagigedo",
  "concejo": "Gijón",
  "categoria": "monumento",
  "desc": "Palacio barroco del siglo XVII en la plaza del Marqués, sede de exposiciones de arte contemporáneo, con una fachada emblemática frente al puerto deportivo de Gijón."
 },
 {
  "nombre": "Jardín Botánico Atlántico",
  "concejo": "Gijón",
  "categoria": "otro",
  "desc": "Amplio jardín botánico dedicado a la flora del norte de la Península y otras regiones atlánticas, con invernaderos, huertas tradicionales y bosques temáticos. Un espacio verde muy popular para familias."
 },
 {
  "nombre": "Casco histórico de Avilés",
  "concejo": "Avilés",
  "categoria": "patrimonio",
  "desc": "Considerado uno de los cascos históricos con más encanto de Asturias, con soportales medievales en la calle Galiana, la Plaza de España y palacios señoriales. Su recuperación urbana lo convirtió en referencia de revitalización histórica."
 },
 {
  "nombre": "Centro Niemeyer",
  "concejo": "Avilés",
  "categoria": "otro",
  "desc": "Complejo cultural diseñado por el arquitecto brasileño Oscar Niemeyer junto a la ría de Avilés, con auditorio, cúpula panorámica y torre mirador. Programa exposiciones, conciertos y actividades culturales todo el año."
 },
 {
  "nombre": "Iglesia de San Nicolás de Bari",
  "concejo": "Avilés",
  "categoria": "monumento",
  "desc": "Antiguo convento franciscano del siglo XIII en el corazón del casco histórico de Avilés, con un claustro gótico y capillas funerarias de linajes avilesinos. Uno de los edificios religiosos más notables de la villa."
 },
 {
  "nombre": "Palacio de Camposagrado",
  "concejo": "Avilés",
  "categoria": "monumento",
  "desc": "Palacio barroco del siglo XVIII con una fachada blasonada característica, hoy sede de instituciones culturales, situado en pleno casco antiguo avilesino junto a otros palacios señoriales."
 },
 {
  "nombre": "Iglesia y barrio de Sabugo",
  "concejo": "Avilés",
  "categoria": "patrimonio",
  "desc": "Antiguo barrio de pescadores de Avilés con la iglesia de Santo Tomás de Sabugo, escenario de la tradicional 'procesión de los Descalzos'. Conserva un ambiente popular distinto al del casco noble de la villa."
 },
 {
  "nombre": "Palacio de Meres",
  "concejo": "Siero (Meres)",
  "categoria": "patrimonio",
  "desc": "Finca histórica con palacio, llagar de sidra y un jardín de esculturas contemporáneas al aire libre, combinando patrimonio civil y arte moderno en un entorno rural. Ofrece visitas guiadas y cata de sidra."
 },
 {
  "nombre": "Iglesia de Santa María de Lugo de Llanera",
  "concejo": "Llanera (Lugo de Llanera)",
  "categoria": "monumento",
  "desc": "Templo románico bien conservado, uno de los pocos ejemplos de esta corriente arquitectónica en el concejo, situado en el núcleo histórico de Lugo de Llanera."
 },
 {
  "nombre": "Casco histórico de Noreña",
  "concejo": "Noreña",
  "categoria": "pueblo",
  "desc": "El municipio más pequeño de Asturias, con un centro compacto y animado, célebre por su gastronomía en torno al chosco (embutido con IGP) y su feria anual. Ideal para una parada corta y sidrería."
 },
 {
  "nombre": "Torre de Podes",
  "concejo": "Gozón (Podes)",
  "categoria": "monumento",
  "desc": "Torre defensiva medieval de los siglos XIV-XV, uno de los pocos vestigios de arquitectura militar del concejo, en el interior rural de Gozón alejado de la costa."
 },
 {
  "nombre": "Casco histórico y ría de Villaviciosa",
  "concejo": "Villaviciosa",
  "categoria": "patrimonio",
  "desc": "Capital de la comarca de la sidra, con la iglesia gótica de Santa María de la Oliva, casonas indianas y calles porticadas. Punto de partida ideal para conocer los llagares de la zona."
 },
 {
  "nombre": "Monasterio de San Salvador de Valdediós (El Conventín)",
  "concejo": "Villaviciosa (Valdediós)",
  "categoria": "monumento",
  "desc": "Iglesia prerrománica del siglo IX, Patrimonio de la Humanidad, integrada en un conjunto monástico posterior de estilo cisterciense. Conocida como 'Vallis Dei', combina en un mismo recinto dos etapas del arte asturiano."
 },
 {
  "nombre": "Ría de Villaviciosa (Reserva Natural Parcial)",
  "concejo": "Villaviciosa",
  "categoria": "parque-natural",
  "desc": "Estuario protegido de gran valor ecológico, refugio de aves migratorias y zona de marismas navegable en piragua o a pie por sus senderos. Uno de los espacios naturales más importantes de la costa central asturiana."
 },
 {
  "nombre": "Museo de la Sidra de Asturias",
  "concejo": "Nava",
  "categoria": "museo",
  "desc": "Museo interactivo dedicado a la cultura sidrera asturiana, con audiovisuales, cata guiada y el escanciado tradicional. Nava es la capital de la Fiesta de la Sidra Natural, declarada de Interés Turístico Nacional."
 },
 {
  "nombre": "Ecomuseo Minero Valle de Samuño",
  "concejo": "Langreo",
  "categoria": "museo",
  "desc": "Recorrido en tren minero histórico y visita guiada al interior de una mina de carbón, con antiguos mineros como guías. Una de las experiencias de turismo industrial más completas de las Cuencas."
 },
 {
  "nombre": "Casco histórico de Sama de Langreo",
  "concejo": "Langreo",
  "categoria": "patrimonio",
  "desc": "Núcleo urbano marcado por el pasado industrial y minero, con edificios modernistas, el Pozo Fondón y la iglesia de Santiago Apóstol, testimonio del auge industrial asturiano de finales del XIX."
 },
 {
  "nombre": "Pozo Santa Bárbara",
  "concejo": "Mieres",
  "categoria": "patrimonio",
  "desc": "Castillete minero emblemático visible desde la autovía, símbolo del pasado hullero de Mieres y de la identidad de las Cuencas Mineras asturianas."
 },
 {
  "nombre": "Santa Cristina de Lena",
  "concejo": "Lena",
  "categoria": "monumento",
  "desc": "Iglesia prerrománica del siglo IX construida sobre una plataforma rocosa junto a la vía del tren, Patrimonio de la Humanidad. Su iconostasio de piedra es único en el arte prerrománico europeo."
 },
 {
  "nombre": "Puerto de Pajares / Valgrande-Pajares",
  "concejo": "Lena",
  "categoria": "mirador",
  "desc": "Puerto de montaña histórico frontera con León, con panorámicas espectaculares de la Cordillera Cantábrica y estación de esquí en invierno. Punto de referencia histórico del Camino de Santiago y las vías de comunicación asturianas."
 },
 {
  "nombre": "Cueva Huerta",
  "concejo": "Aller",
  "categoria": "cueva",
  "desc": "Uno de los sistemas kársticos más largos de Asturias, con visitas guiadas a sus galerías, formaciones de estalactitas y un río subterráneo. Atractivo natural y espeleológico poco masificado."
 },
 {
  "nombre": "Museo de la Minería y de la Industria (MUMI)",
  "concejo": "San Martín del Rey Aurelio (El Entrego)",
  "categoria": "museo",
  "desc": "Museo de referencia sobre la minería del carbón en España, con una réplica de galería subterránea y maquinaria original. Pieza clave para entender la historia industrial de las Cuencas Mineras."
 },
 {
  "nombre": "Pozo Sotón",
  "concejo": "San Martín del Rey Aurelio (Sotrondio)",
  "categoria": "patrimonio",
  "desc": "Antigua mina en funcionamiento hasta hace pocos años, hoy ofrece la visita minera más auténtica de Asturias: bajada real en jaula hasta las galerías con exmineros como guías."
 },
 {
  "nombre": "Senda del Oso y Casa del Oso",
  "concejo": "Proaza",
  "categoria": "otro",
  "desc": "Vía verde sobre una antigua vía minera que recorre los valles de Proaza, Teverga y Quirós, con la Casa del Oso donde viven en semilibertad ejemplares de oso pardo cantábrico. Ruta ideal en bici o a pie apta para toda la familia."
 },
 {
  "nombre": "Desfiladero de las Xanas",
  "concejo": "Teverga",
  "categoria": "parque-natural",
  "desc": "Espectacular garganta fluvial excavada por el arroyo de las Xanas, con senderos entre paredes de roca caliza y pequeñas cascadas. Una de las rutas de naturaleza más populares del centro de Asturias."
 },
 {
  "nombre": "Parque de la Prehistoria de Asturias",
  "concejo": "Teverga",
  "categoria": "museo",
  "desc": "Único parque temático de Europa dedicado íntegramente al arte rupestre paleolítico, con réplicas exactas de Altamira, Tito Bustillo y otras cuevas Patrimonio de la Humanidad. Complemento perfecto de una visita a la Senda del Oso."
 },
 {
  "nombre": "Iglesia prerrománica de San Adriano de Tuñón",
  "concejo": "Santo Adriano (Tuñón)",
  "categoria": "monumento",
  "desc": "Templo de época asturiana (siglo IX) de estilo mozárabe-prerrománico, situado en un entorno rural tranquilo junto al río Trubia, en la entrada de la Senda del Oso. Menos visitado que los grandes monumentos de Oviedo pero de gran valor histórico."
 },
 {
  "nombre": "Taramundi (pueblo)",
  "concejo": "Taramundi",
  "categoria": "pueblo",
  "desc": "Pueblo pionero del turismo rural en España, con arquitectura tradicional en piedra y pizarra encajada en un valle verde de Los Oscos. Su casco es punto de partida de la famosa Ruta del Agua y sigue siendo cuna de la artesanía cuchillera asturiana."
 },
 {
  "nombre": "Ruta del Agua (molinos y batanes)",
  "concejo": "Taramundi",
  "categoria": "patrimonio",
  "desc": "Sendero circular corto que enlaza mazos, batanes, un molino harinero y una serrería, todos movidos por la fuerza del agua y restaurados como museo etnográfico al aire libre. Es la mejor forma de entender la vida tradicional de Los Oscos y muy asequible para toda la familia."
 },
 {
  "nombre": "Museo Etnográfico de Grandas de Salime \"Pepe el Ferreiro\"",
  "concejo": "Grandas de Salime",
  "categoria": "museo",
  "desc": "Uno de los museos etnográficos más completos de España, reunido por el 'coleccionista' Pepe el Ferreiro en un antiguo colegio, con miles de piezas sobre oficios, agricultura y vida rural asturiana. Incluye una capilla de arte contemporáneo pintada por artistas invitados, algo insólito en un museo rural."
 },
 {
  "nombre": "Castro de Chao Samartín",
  "concejo": "Grandas de Salime (Villaseca)",
  "categoria": "patrimonio",
  "desc": "Poblado fortificado astur-romano de gran importancia arqueológica, con restos de viviendas, un edificio termal y objetos que muestran el paso de la cultura castreña a la romanización. Cuenta con un museo anexo que exhibe más de 350 piezas halladas en las excavaciones."
 },
 {
  "nombre": "Parque Natural de Somiedo",
  "concejo": "Somiedo",
  "categoria": "parque-natural",
  "desc": "Reserva de la Biosfera con el sistema lacustre glaciar más importante de la Cordillera Cantábrica (Lagos de Saliencia, Lago del Valle) y una de las poblaciones más estables de oso pardo cantábrico. Sus valles combinan naturaleza salvaje con un paisaje ganadero tradicional único."
 },
 {
  "nombre": "Brañas de teitos de La Pornacal",
  "concejo": "Somiedo",
  "categoria": "patrimonio",
  "desc": "El mayor conjunto de brañas (asentamientos ganaderos de altura) con cabañas de teito -cubierta vegetal de escoba- de toda Asturias, declarado Monumento Natural. Es una imagen vivísima de la trashumancia vaqueira que aún se practica en el parque."
 },
 {
  "nombre": "Cudillero (pueblo)",
  "concejo": "Cudillero",
  "categoria": "pueblo",
  "desc": "Villa marinera construida en anfiteatro sobre un puerto natural, con casas de colores escalonadas y calles empinadas que bajan hasta la lonja. Su mirador de El Pico y el barrio pescador son de los rincones más fotografiados de Asturias."
 },
 {
  "nombre": "Conjunto monumental de Salas (Torre, Palacio y Colegiata)",
  "concejo": "Salas",
  "categoria": "monumento",
  "desc": "Villa del Camino Primitivo con cuatro Monumentos Nacionales en su casco: la Torre de la Villa (s. XIV), el Palacio de Valdés-Salas unido a ella por un arco, la Colegiata de Santa María la Mayor con el sepulcro renacentista de Fernando de Valdés y la iglesia prerrománica de San Martín. Muy recomendable combinarla con la cercana cascada de Nonaya."
 },
 {
  "nombre": "Monasterio de San Juan Bautista de Corias",
  "concejo": "Cangas del Narcea (Corias)",
  "categoria": "monumento",
  "desc": "Uno de los monasterios benedictinos más grandes de España, con una imponente fachada barroca sobre el río Narcea; hoy alberga un Parador y bodega. Su iglesia y claustros pueden visitarse y ofrecen una de las estampas monumentales más notables del occidente asturiano."
 },
 {
  "nombre": "Hayedo de Monasterio de Hermo",
  "concejo": "Cangas del Narcea (Monasterio de Hermo)",
  "categoria": "parque-natural",
  "desc": "Uno de los hayedos mejor conservados y más extensos de la península ibérica, dentro del Parque Natural de las Fuentes del Narcea, Degaña e Ibias. Espectacular en otoño por el color del follaje y hábitat de fauna protegida como el urogallo."
 },
 {
  "nombre": "Parque Natural de Muniellos",
  "concejo": "Ibias",
  "categoria": "parque-natural",
  "desc": "Reserva Natural Integral y Reserva de la Biosfera que protege el robledal mejor conservado de España y uno de los más extensos de Europa, refugio de oso pardo y urogallo. El acceso está muy restringido (máximo 20 visitantes al día con reserva previa), lo que lo convierte en una experiencia de naturaleza casi virgen."
 },
 {
  "nombre": "Parque Natural de las Fuentes del Narcea, Degaña e Ibias",
  "concejo": "Degaña",
  "categoria": "parque-natural",
  "desc": "Extenso espacio protegido de montaña que da nombre al concejo, con bosques atlánticos, la Reserva Regional de Caza de Degaña y paisajes de alta montaña poco transitados. Es la puerta de entrada menos conocida a este gran macizo forestal del suroccidente asturiano."
 },
 {
  "nombre": "Castro de Coaña",
  "concejo": "Coaña",
  "categoria": "patrimonio",
  "desc": "Uno de los poblados fortificados prerromanos mejor conservados de España, habitado entre los siglos IV a.C. y I d.C., con viviendas circulares, calles empedradas y un recinto termal de uso ritual. Un centro de interpretación explica la cultura castreña y la posterior explotación romana del oro cercano."
 },
 {
  "nombre": "Cueva de la Peña (Candamo)",
  "concejo": "Candamo (San Román)",
  "categoria": "cueva",
  "desc": "Cueva con arte rupestre paleolítico declarada Patrimonio Mundial por la UNESCO, la cavidad con pinturas del Paleolítico más occidental de Europa. Las visitas son guiadas y muy limitadas (grupos reducidos con reserva obligatoria), con un centro de interpretación en el Palacio Valdés-Bazán."
 },
 {
  "nombre": "Luarca",
  "concejo": "Valdés (Luarca)",
  "categoria": "pueblo",
  "desc": "La 'villa blanca de la costa verde', con su puerto pesquero repartido a ambos lados de la ría, calles empinadas y el singular cementerio en lo alto del cabo con vistas al mar. Su casco histórico de casas de indianos y su faro completan un paseo obligado."
 },
 {
  "nombre": "Ferrería de Mazonovo",
  "concejo": "Santa Eulalia de Oscos (Mazonovo)",
  "categoria": "patrimonio",
  "desc": "Una de las ferrerías hidráulicas más antiguas conservadas de Asturias (principios del s. XVIII), donde se forjaba hierro con la fuerza del agua del río. Forma parte del paisaje fluvial de Los Oscos, con zonas de baño cercanas en el Agüeira."
 },
 {
  "nombre": "Monasterio de Santa María de Villanueva de Oscos",
  "concejo": "Villanueva de Oscos",
  "categoria": "monumento",
  "desc": "Monasterio cisterciense del siglo XII, restaurado, que da nombre al concejo y conserva elementos románicos y barrocos. Su entorno rural y el cercano ecomuseo del pan completan una visita centrada en la vida monástica y agrícola de la comarca."
 },
 {
  "nombre": "Palacio de Mon",
  "concejo": "San Martín de Oscos",
  "categoria": "monumento",
  "desc": "Palacio barroco de los siglos XVII-XVIII con una fachada blasonada muy vistosa, uno de los edificios civiles más notables de Los Oscos. Representa el poder de los antiguos linajes ferreiros de la comarca."
 },
 {
  "nombre": "Castro de Pendia",
  "concejo": "Boal (Pendia)",
  "categoria": "patrimonio",
  "desc": "Poblado castreño considerado seña de identidad de Boal y de todo el Parque Histórico del Navia, con restos de murallas y viviendas sobre un cordal con vistas al valle. Se puede combinar con el Centro de Interpretación del Hierro de Rozadas, dedicado a ferreiros y claveros."
 },
 {
  "nombre": "Aldea de Argul",
  "concejo": "Pesoz (Argul)",
  "categoria": "pueblo",
  "desc": "Pequeña aldea medieval construida literalmente sobre y entre grandes rocas, con casas de piedra conectadas por túneles y pasos elevados. Es uno de los pueblos con trazado más singular y sorprendente del occidente asturiano."
 },
 {
  "nombre": "Santesteba",
  "concejo": "Illano (Santesteba)",
  "categoria": "pueblo",
  "desc": "Pueblo de casas de pizarra y madera del siglo XIX, aferrado a las rocas sobre el río Navia, en uno de los concejos más despoblados y silvestres de Asturias. Su aislamiento ha conservado un paisaje rural casi intacto."
 },
 {
  "nombre": "Cascadas de Oneta",
  "concejo": "Villayón (Oneta)",
  "categoria": "otro",
  "desc": "Conjunto de tres saltos de agua escalonados en un entorno boscoso, accesibles por una ruta corta y muy popular en primavera y tras las lluvias. Uno de los rincones naturales más visitados del concejo de Villayón."
 },
 {
  "nombre": "Monasterio de Santa María la Real de Obona",
  "concejo": "Tineo (Obona)",
  "categoria": "monumento",
  "desc": "Antiguo monasterio benedictino en un paraje boscoso apartado, con una iglesia de origen medieval y fachada barroca; en sus documentos aparece la primera referencia escrita a la sidra asturiana. Un lugar tranquilo y con mucha carga histórica dentro del extenso concejo de Tineo."
 },
 {
  "nombre": "Tapia de Casariego (pueblo)",
  "concejo": "Tapia de Casariego",
  "categoria": "pueblo",
  "desc": "Villa marinera con un puerto pintoresco entre acantilados, casco histórico de casas de indianos y ambiente surfero por sus olas de calidad. Su paseo marítimo y la iglesia parroquial completan un recorrido corto pero muy agradable."
 },
 {
  "nombre": "Castropol (mirador de la ría del Eo)",
  "concejo": "Castropol",
  "categoria": "pueblo",
  "desc": "Villa señorial asomada a la ría del Eo, con casas blasonadas, soportales y un paseo con vistas privilegiadas a Galicia al otro lado del agua. Su conjunto histórico-artístico es uno de los mejor conservados del extremo occidental asturiano."
 },
 {
  "nombre": "Puente de los Santos y ría del Eo",
  "concejo": "Vegadeo",
  "categoria": "otro",
  "desc": "Vegadeo es la puerta de entrada a Asturias desde Galicia por la ría del Eo, con un puente histórico y un entorno natural protegido como Reserva de la Biosfera transfronteriza. Su mercado y su casco comercial reflejan el papel de capital de comarca del municipio."
 },
 {
  "nombre": "Minas de oro romanas de El Valle-Boinás y Aula del Oro",
  "concejo": "Belmonte de Miranda",
  "categoria": "patrimonio",
  "desc": "Restos de una de las mayores explotaciones auríferas de época romana en Asturias, con galerías y canales que se pueden visitar junto a un centro de interpretación (Aula del Oro) sobre la técnica de la ruina montium. Un testimonio poco conocido de la ingeniería minera romana."
 },
 {
  "nombre": "Pola de Allande",
  "concejo": "Allande (Pola de Allande)",
  "categoria": "pueblo",
  "desc": "Capital de un concejo montañoso atravesado por el Camino Primitivo de Santiago, con casonas indianas, un pequeño casco histórico y el exigente puerto del Palo como telón de fondo. Punto de partida habitual para etapas de peregrinación hacia Galicia."
 },
 {
  "nombre": "Iglesia prerrománica de Santianes de Pravia",
  "concejo": "Pravia (Santianes)",
  "categoria": "monumento",
  "desc": "Templo del siglo VIII vinculado al rey Silo, cuando Pravia fue durante un breve periodo capital del Reino de Asturias; es uno de los edificios prerrománicos más antiguos que se conservan. El casco histórico de Pravia, con soportales y plaza porticada, completa la visita."
 },
 {
  "nombre": "Miudes",
  "concejo": "El Franco (Miudes)",
  "categoria": "pueblo",
  "desc": "Pequeño pueblo marinero de casas blancas y tejados de pizarra colgado sobre los acantilados, muy fotogénico y con encanto tradicional. Representa bien la arquitectura costera del concejo de El Franco."
 },
 {
  "nombre": "San Tirso de Abres",
  "concejo": "San Tirso de Abres",
  "categoria": "pueblo",
  "desc": "Villa fronteriza con Galicia en la confluencia de los ríos Eo y Agüeira, etapa del Camino Primitivo interior y con la iglesia de San Juan Bautista como principal hito religioso. Su entorno fluvial es tranquilo y muy verde."
 },
 {
  "nombre": "Navia (pueblo y ría)",
  "concejo": "Navia",
  "categoria": "pueblo",
  "desc": "Villa marinera en la desembocadura del río Navia, con un paseo fluvial, playa urbana y un casco con arquitectura indiana de los emigrantes que hicieron fortuna en América. Buen punto de partida para explorar el Parque Histórico del Navia y sus castros."
 },
 {
  "nombre": "Casco histórico de Grado (Iglesia de Santa María y palacios)",
  "concejo": "Grado",
  "categoria": "monumento",
  "desc": "Villa mercado del valle del Nalón con soportales, palacios señoriales y la iglesia de Santa María, dentro de una de las rutas del románico asturiano. Su mercado semanal es uno de los más animados y tradicionales de la región."
 },
 {
  "nombre": "Castillo de San Martín",
  "concejo": "Soto del Barco",
  "categoria": "monumento",
  "desc": "Restos de una fortaleza medieval sobre un promontorio que domina la ría del Nalón, con un mirador desde el que se ve todo el estuario hasta la desembocadura. Un rincón histórico poco masificado en la comarca del Bajo Nalón."
 },
 {
  "nombre": "Muros de Nalón (pueblo indiano)",
  "concejo": "Muros de Nalón",
  "categoria": "pueblo",
  "desc": "Pequeña villa de la comarca de las Cinco Villas del Bajo Nalón, con arquitectura de indianos, chalés modernistas y un ambiente veraniego tranquilo. Su paseo marítimo y su entorno pesquero completan bien una ruta por el litoral occidental."
 }
]
''')

RUTA_FOTO_INTERIOR_RAW = json.loads(r'''
[
{"nombre":"Lagos de Covadonga (Enol y Ercina)","concejo":"Cangas de Onís","tipo":"lago","desc":"Dos lagos glaciares a más de 1000 m de altitud rodeados de picos calizos; reflejos del Macizo Occidental y ganado pastando en los Picos de Europa.","mejor_luz":"Amanecer, antes de la afluencia de tráfico y con niebla frecuente en las mañanas de otoño","dist_km_aprox":95},
{"nombre":"Mirador de la Reina","concejo":"Cangas de Onís","tipo":"mirador","desc":"Balcón sobre el desfiladero de Los Beyos y los valles hacia Covadonga, con vistas escalonadas de las montañas calizas.","mejor_luz":"Atardecer, luz rasante dorada sobre las crestas","dist_km_aprox":92},
{"nombre":"Mirador del Rey","concejo":"Cangas de Onís","tipo":"mirador","desc":"Vista panorámica de la Basílica de Covadonga y del valle hacia el santuario, enmarcada por paredones rocosos.","mejor_luz":"Mañana, luz suave sobre la fachada de la basílica","dist_km_aprox":85},
{"nombre":"Puente Romano de Cangas de Onís","concejo":"Cangas de Onís","tipo":"otro","desc":"Puente medieval (atribuido erróneamente a época romana) sobre el río Sella con la Cruz de la Victoria colgando en el arco central.","mejor_luz":"Última hora de la tarde, reflejos del puente en el agua","dist_km_aprox":75},
{"nombre":"Mirador del Pozo de la Oración (Camarmeña)","concejo":"Cabrales","tipo":"mirador","desc":"Uno de los mejores puntos para fotografiar el Naranjo de Bulnes (Picu Urriellu) recortado sobre el pueblo de Bulnes.","mejor_luz":"Atardecer, cuando el pico se tiñe de rojo (alpenglow)","dist_km_aprox":108},
{"nombre":"Bulnes","concejo":"Cabrales","tipo":"pueblo","desc":"Aldea de piedra sin acceso rodado, encajonada bajo el Naranjo de Bulnes, accesible a pie o en funicular desde Poncebos.","mejor_luz":"Mañana temprano, con niebla en el fondo del valle","dist_km_aprox":112},
{"nombre":"Poncebos y desfiladero del Cares","concejo":"Cabrales","tipo":"desfiladero","desc":"Inicio de la Ruta del Cares, garganta vertical excavada por el río entre paredes calizas de cientos de metros.","mejor_luz":"Mañana, cuando el sol entra directamente al cañón","dist_km_aprox":100},
{"nombre":"Desfiladero de los Beyos","concejo":"Amieva / Ponga","tipo":"desfiladero","desc":"Cañón de unos 20 km excavado por el río Sella, con carretera y vía de tren sinuosas entre paredes rocosas casi verticales.","mejor_luz":"Media mañana, cuando la luz alcanza el fondo del desfiladero","dist_km_aprox":88},
{"nombre":"Alto del Cabanón","concejo":"Ponga","tipo":"mirador","desc":"Vista espectacular de las cumbres de los macizos Occidental y Central de Picos de Europa desde un puerto de montaña remoto.","mejor_luz":"Atardecer, con los picos iluminados y el valle en sombra","dist_km_aprox":105},
{"nombre":"El Fito","concejo":"Parres","tipo":"mirador","desc":"Mirador circular considerado uno de los mejores de la península: panorámica de 360º con la costa, la ría de Ribadesella y los Picos de Europa al fondo.","mejor_luz":"Mañana despejada, mejor visibilidad hacia la costa y las cumbres","dist_km_aprox":55},
{"nombre":"San Juan de Beleño","concejo":"Ponga","tipo":"pueblo","desc":"Capital del valle de Ponga, punto de partida hacia el Pico Pierzu y el Bosque de Peloño, con arquitectura tradicional de montaña.","mejor_luz":"Otoño, cuando el hayedo circundante cambia de color","dist_km_aprox":95},
{"nombre":"Casielles","concejo":"Ponga","tipo":"mirador","desc":"Pequeño pueblo encaramado sobre una carretera de 21 curvas cerradas, con vistas dramáticas del valle de Ponga.","mejor_luz":"Atardecer, luz lateral que resalta las curvas de la carretera","dist_km_aprox":98},
{"nombre":"Lagos de Saliencia","concejo":"Somiedo","tipo":"lago","desc":"Conjunto de lagos glaciares de alta montaña (Calabazosa, La Cueva, Cerveriz, Almagrera) en un circo rodeado de picos pizarrosos.","mejor_luz":"Amanecer, aguas en calma antes de que se levante el viento","dist_km_aprox":112},
{"nombre":"Lago del Valle (Valle del Lago)","concejo":"Somiedo","tipo":"lago","desc":"El mayor lago glaciar de Asturias, con un mirador natural que domina el valle y la braña con teitos al fondo.","mejor_luz":"Atardecer, con niebla frecuente en otoño sobre la superficie del lago","dist_km_aprox":118},
{"nombre":"Braña de La Pornacal","concejo":"Somiedo","tipo":"otro","desc":"La mayor braña de teitos (cabañas de techo vegetal) de Asturias, uno de los conjuntos etnográficos de montaña mejor conservados.","mejor_luz":"Amanecer con niebla baja, muy característica del valle en otoño","dist_km_aprox":95},
{"nombre":"Desfiladero de las Xanas","concejo":"Proaza / Teverga","tipo":"desfiladero","desc":"Conocido como 'el pequeño Cares', un cañón estrecho tallado por el arroyo Cabria con pasarelas colgadas sobre el agua.","mejor_luz":"Mediodía, cuando la luz vertical entra hasta el fondo del cañón estrecho","dist_km_aprox":50},
{"nombre":"Bandujo","concejo":"Proaza","tipo":"pueblo","desc":"Pueblo medieval de piedra con torre defensiva e iglesia románica, encaramado sobre el valle del Trubia.","mejor_luz":"Atardecer, luz cálida sobre la piedra dorada de las fachadas","dist_km_aprox":52},
{"nombre":"Senda del Oso (valle del Trubia)","concejo":"Teverga / Proaza","tipo":"otro","desc":"Antiguo trazado de vía verde junto al río Trubia entre túneles y desfiladeros, con recinto de osos pardos en semilibertad.","mejor_luz":"Mañana, luz filtrada entre el bosque de ribera","dist_km_aprox":45},
{"nombre":"Puente colgante de Cangas del Narcea","concejo":"Cangas del Narcea","tipo":"otro","desc":"Pasarela colgante sobre el río Narcea que conecta dos barrios de la villa, con vistas de la Colegiata de Santa María Magdalena.","mejor_luz":"Atardecer, con la villa iluminada de luz dorada","dist_km_aprox":108},
{"nombre":"Monasterio de Corias","concejo":"Cangas del Narcea","tipo":"otro","desc":"Gran monasterio benedictino (el 'Escorial asturiano') sobre una colina dominando el valle del Narcea.","mejor_luz":"Atardecer, luz rasante sobre la fachada monumental","dist_km_aprox":110},
{"nombre":"Cascada del Xiblu","concejo":"Cangas del Narcea","tipo":"cascada","desc":"Espectacular salto de agua de unos 80 metros en el entorno de Rengos, poco conocido y rodeado de bosque atlántico.","mejor_luz":"Tras lluvias, luz difusa de día nublado para evitar contrastes fuertes en el agua","dist_km_aprox":135},
{"nombre":"Bosque de Muniellos","concejo":"Ibias","tipo":"otro","desc":"Uno de los robledales mejor conservados de Europa, Reserva de la Biosfera, con acceso limitado y luz filtrada entre robles centenarios.","mejor_luz":"Otoño, colores del follaje con luz filtrada de media mañana","dist_km_aprox":150},
{"nombre":"Embalse de la Florida (valle de Degaña)","concejo":"Degaña","tipo":"lago","desc":"Embalse de montaña rodeado de bosques y picos del Parque Natural de las Fuentes del Narcea, Degaña e Ibias.","mejor_luz":"Amanecer con niebla sobre el agua, frecuente en otoño","dist_km_aprox":150},
{"nombre":"Mirador de A Paicega sobre el Embalse de Grandas de Salime","concejo":"Grandas de Salime","tipo":"mirador","desc":"Vistas del gran embalse serpenteante entre montañas del occidente asturiano, con la presa al fondo.","mejor_luz":"Atardecer, cuando la luz baja resalta los meandros del embalse","dist_km_aprox":150},
{"nombre":"Lago Ubales","concejo":"Caso","tipo":"lago","desc":"Pequeño lago de montaña cerca del puerto de Tarna, con reflejos de las cumbres del Parque Natural de Redes.","mejor_luz":"Amanecer, aguas en calma antes del viento del mediodía","dist_km_aprox":78},
{"nombre":"Tabayón del Mongallu","concejo":"Caso","tipo":"cascada","desc":"Cascada de más de 60 metros de caída libre, accesible en ruta de senderismo desde Tarna, una de las más altas de Asturias.","mejor_luz":"Día nublado tras lluvias, para captar bien el caudal sin contrastes","dist_km_aprox":80},
{"nombre":"Embalse de Rioseco / Tanes","concejo":"Caso / Sobrescobio","tipo":"lago","desc":"Embalse alargado entre montañas del Parque Natural de Redes, con miradores desde Campiellos y Llaíñes.","mejor_luz":"Atardecer, luz dorada reflejada en el agua desde el mirador de Campiellos","dist_km_aprox":65},
{"nombre":"Brañagallones","concejo":"Caso","tipo":"otro","desc":"Vega de alta montaña considerada una de las más bellas de Asturias, con prados verdes rodeados de picos del Parque de Redes.","mejor_luz":"Amanecer de verano, niebla baja disipándose sobre el prado","dist_km_aprox":85}
]
''')

# Distancias aproximadas en coche desde Gijón (km) para concejos que no
# forman parte de la lista de "concejos" de playas.
DIST_EXTRA = {
    "Oviedo": 28, "Avilés": 25, "Siero": 20, "Cabranes": 35, "Piloña": 45,
    "Parres": 55, "Cangas de Onís": 75, "Cangas del Narcea": 110, "Lena": 55,
    "Aller": 65, "Nava": 38, "Grado": 45, "Salas": 65, "Vegadeo": 130,
    "Llanera": 28, "Mieres": 48, "Langreo": 32, "Sariego": 42,
    "Caso": 78, "Ponga": 85, "Allande": 95, "Villayón": 90,
    # concejos adicionales para la pestaña "Qué ver"
    "Amieva": 85, "Belmonte de Miranda": 65, "Boal": 110, "Cabrales": 105,
    "Candamo": 45, "Degaña": 150, "Grandas de Salime": 150, "Ibias": 150,
    "Illano": 120, "Noreña": 22, "Onís": 80, "Peñamellera Alta": 105,
    "Peñamellera Baja": 100, "Pesoz": 135, "Pravia": 45, "Proaza": 50,
    "San Martín de Oscos": 140, "San Martín del Rey Aurelio": 35,
    "San Tirso de Abres": 135, "Santa Eulalia de Oscos": 140,
    "Santo Adriano": 48, "Sobrescobio": 72, "Somiedo": 112,
    "Taramundi": 140, "Teverga": 52, "Tineo": 85, "Villanueva de Oscos": 135,
}


def _parse_concejo(raw):
    m = re.match(r'^(.*?)\s*\((.*)\)\s*$', raw.strip())
    if m:
        return m.group(1).strip(), m.group(2).strip()
    return raw.strip(), None


def build_extra(concejos):
    dist_lookup = {c["nombre"]: c["dist_km"] for c in concejos}
    dist_lookup.update(DIST_EXTRA)

    restaurantes = []
    vistos = set()
    for r in RESTAURANTES_RAW + REST_NUEVOS_RAW:
        concejo_base, localidad = _parse_concejo(r["concejo"])
        clave = (r["nombre"].strip().lower(), concejo_base.strip().lower())
        if clave in vistos:
            continue
        vistos.add(clave)
        restaurantes.append(dict(
            nombre=r["nombre"], concejo=concejo_base, localidad=localidad,
            distincion=r["distincion"], especialidades=r["especialidades"],
            tique_medio=r["tique_medio"], desc=r["desc"],
            dist_km=dist_lookup[concejo_base],
        ))

    sidrerias = []
    for s in SIDRERIAS_RAW:
        concejo_base, localidad = _parse_concejo(s["concejo"])
        sidrerias.append(dict(
            nombre=s["nombre"], concejo=concejo_base, localidad=localidad,
            premiada=s["premiada"], premio=s["premio"],
            especialidad=s["especialidad"], desc=s["desc"],
            dist_km=dist_lookup[concejo_base],
        ))

    lagares = []
    for l in LAGARES_RAW:
        concejo_base, localidad = _parse_concejo(l["concejo"])
        lagares.append(dict(
            nombre=l["nombre"], concejo=concejo_base, localidad=localidad,
            premiada=l["premiada"], premio=l["premio"],
            especialidad=l["especialidad"], desc=l["desc"],
            dist_km=dist_lookup[concejo_base],
        ))

    ruta_foto_interior = []
    for p in RUTA_FOTO_INTERIOR_RAW:
        ruta_foto_interior.append(dict(
            nombre=p["nombre"], concejo=p["concejo"], tipo=p["tipo"],
            desc=p["desc"], mejor_luz=p["mejor_luz"],
            dist_km=p["dist_km_aprox"],
        ))

    sitios = []
    for s in SITIOS_RAW:
        concejo_base, localidad = _parse_concejo(s["concejo"])
        sitios.append(dict(
            nombre=s["nombre"], concejo=concejo_base, localidad=localidad,
            categoria=s["categoria"], desc=s["desc"],
            dist_km=dist_lookup[concejo_base],
        ))

    return restaurantes, sidrerias, ruta_foto_interior, lagares, sitios

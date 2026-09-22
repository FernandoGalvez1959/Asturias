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

    return restaurantes, sidrerias, ruta_foto_interior, lagares

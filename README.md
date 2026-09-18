# Asturias

App web de una sola página con las 199 playas del Principado de Asturias, pensada para uso personal y para empaquetar como app Android (por ejemplo con AppsGeyser).

## Contenido del repositorio

```
index.html         → La app completa, lista para usar (ábrela directamente en el navegador
                      o publícala con GitHub Pages)
icons/              → Iconos de la app (512px y 1024px)
src/
  template.html     → Plantilla fuente de la app (HTML + CSS + JS), sin los datos incrustados
  build_data.py      → Script Python que genera datos.json / datos.min.json a partir de
                      los datos de playas y rutas fotográficas
  datos.json          → Datos de playas, concejos y ruta fotográfica (formato legible)
  datos.min.json      → Mismos datos, minificados (los que se incrustan en index.html)
```

## Cómo funciona

- `index.html` es completamente autocontenido: no depende de ningún servidor ni de conexión a internet salvo para los enlaces externos (Google Maps, Windy, tablademareas.com).
- Los datos están incrustados dentro de `index.html` en un bloque `<script type="application/json">`. Si quieres modificarlos, edita `src/build_data.py` (o `src/datos.json` directamente) y vuelve a generar `index.html` insertando el JSON minificado en la plantilla `src/template.html`.
- Favoritos, notas y fotos propias se guardan en el propio dispositivo (localStorage), no se suben a ningún sitio.

## Publicar con GitHub Pages

1. Sube este repositorio a GitHub.
2. En **Settings → Pages**, selecciona la rama principal y la carpeta raíz (`/`).
3. GitHub Pages servirá `index.html` automáticamente como la página principal.

## Empaquetar como app Android

`index.html` puede usarse directamente como la URL/archivo fuente en AppsGeyser u otro empaquetador de WebView para generar un `.apk`.

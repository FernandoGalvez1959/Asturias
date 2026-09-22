# Asturias

App web de una sola página con guía personal de Asturias: 199 playas del Principado, rutas fotográficas (costa e interior), restaurantes y sidrerías. Pensada para uso personal, instalable como app (PWA) desde el navegador, y también empaquetable como app Android (por ejemplo con AppsGeyser).

## Contenido del repositorio

```
index.html          → La app completa, lista para usar
manifest.json        → Manifiesto PWA (nombre, iconos, modo standalone)
sw.js                 → Service worker mínimo, necesario para que se pueda "instalar"
icons/                → Iconos de la app (192px, 512px y 1024px)
src/
  template.html       → Plantilla fuente de la app (HTML + CSS + JS), sin los datos incrustados
  build_data.py        → Script Python que genera datos.json / datos.min.json (playas)
  extra_data.py        → Datos de restaurantes, sidrerías y ruta fotográfica de interior
  datos.json            → Datos completos en formato legible
  datos.min.json        → Mismos datos, minificados (los que se incrustan en index.html)
```

## Publicar con GitHub Pages (necesario para poder "instalarla")

1. Sube este repositorio a GitHub, manteniendo `index.html`, `manifest.json`, `sw.js` e `icons/` en la raíz.
2. En **Settings → Pages**, selecciona la rama principal y la carpeta raíz (`/`).
3. GitHub Pages servirá `index.html` automáticamente. Anota la URL que te da (algo como `https://tuusuario.github.io/turepo/`).

## Instalar la app en el móvil (no solo un acceso directo)

Un archivo HTML suelto, o abierto directamente sin pasar por GitHub Pages, solo permite crear un acceso directo. Para que el móvil ofrezca **"Instalar app"** de verdad (icono propio, pantalla completa sin barra del navegador), la página tiene que servirse por **https** — por eso hace falta GitHub Pages (o cualquier otro hosting):

- **Android (Chrome)**: abre la URL de GitHub Pages → menú (⋮) → "Instalar aplicación" o "Añadir a pantalla de inicio".
- **iPhone (Safari)**: abre la URL → botón compartir (□↑) → "Añadir a pantalla de inicio".

## Cómo funciona

- `index.html` es autocontenido: los datos de playas, rutas, restaurantes y sidrerías están incrustados en un bloque `<script type="application/json">`. Para modificarlos, edita `src/build_data.py` / `src/extra_data.py` (o los JSON directamente) y vuelve a generar `index.html` insertando el JSON minificado en `src/template.html`.
- Favoritos, notas y fotos propias se guardan en el propio dispositivo (localStorage), no se suben a ningún sitio.

## Empaquetar como app Android (alternativa a la instalación PWA)

`index.html` puede usarse directamente como la URL/archivo fuente en AppsGeyser u otro empaquetador de WebView para generar un `.apk`.

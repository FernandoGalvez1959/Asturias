# -*- coding: utf-8 -*-
"""
Genera app.html (sin envolver, para publicar como Claude Artifact) y
asturias.html (HTML autocontenido con envoltorio PWA completo: doctype,
head con manifest/meta/iconos, y registro del service worker) a partir de
template.html + playas.min.json.
"""
import json

with open("template.html", "r", encoding="utf-8") as f:
    template = f.read()

with open("playas.min.json", "r", encoding="utf-8") as f:
    data_json = f.read()

assert "</script" not in data_json, "El JSON de datos contiene '</script', hay que escaparlo"
assert "__DATA_JSON__" in template, "No se encontró el marcador __DATA_JSON__ en template.html"

body = template.replace("__DATA_JSON__", data_json)

# ---- app.html: version sin envolver, para el Artifact (que añade su propio esqueleto) ----
with open("app.html", "w", encoding="utf-8") as f:
    f.write(body)

# ---- asturias.html: version envuelta y autocontenida (descarga directa / GitHub Pages) ----
HEAD_PREFIX = '''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<link rel="manifest" href="manifest.json">
<meta name="theme-color" content="#0e6e73">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Asturias">
<link rel="apple-touch-icon" href="icons/icono-asturias-512.png">
'''

SW_SUFFIX = '''

<script>if('serviceWorker' in navigator){window.addEventListener('load',function(){navigator.serviceWorker.register('sw.js').catch(function(){});});}</script>
</body>
</html>
'''

standalone = HEAD_PREFIX + body + SW_SUFFIX
with open("asturias.html", "w", encoding="utf-8") as f:
    f.write(standalone)

print(f"app.html: {len(body)} caracteres")
print(f"asturias.html: {len(standalone)} caracteres")

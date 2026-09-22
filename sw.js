// Service worker mínimo: permite que el navegador ofrezca "Instalar app" (PWA)
// y sirve un caché básico para que la app cargue más rápido en visitas repetidas.
//
// IMPORTANTE: cada vez que se publique una versión nueva de la app (o se
// corrija algo como el manifest.json o los iconos), hay que subir el número
// de CACHE (v2, v3, ...). Si no, los móviles que ya visitaron la app se
// quedan sirviendo para siempre la copia vieja guardada en caché, aunque el
// archivo en el servidor ya esté arreglado.
const CACHE = 'asturias-v2';

self.addEventListener('install', (event) => {
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((names) => Promise.all(names.filter((n) => n !== CACHE).map((n) => caches.delete(n))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;
  event.respondWith(
    caches.match(event.request).then((cached) => {
      const network = fetch(event.request)
        .then((resp) => {
          // Solo se guarda en caché si la respuesta es válida (evita dejar
          // grabado para siempre un 404 u otro error).
          if (resp && resp.ok) {
            const copy = resp.clone();
            caches.open(CACHE).then((c) => c.put(event.request, copy)).catch(() => {});
          }
          return resp;
        })
        .catch(() => cached);
      return cached || network;
    })
  );
});

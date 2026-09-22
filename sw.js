// Service worker mínimo: permite que el navegador ofrezca "Instalar app" (PWA)
// y sirve un caché básico para que la app cargue más rápido en visitas repetidas.
const CACHE = 'asturias-v1';

self.addEventListener('install', (event) => {
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(self.clients.claim());
});

self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;
  event.respondWith(
    caches.match(event.request).then((cached) => {
      const network = fetch(event.request)
        .then((resp) => {
          const copy = resp.clone();
          caches.open(CACHE).then((c) => c.put(event.request, copy)).catch(() => {});
          return resp;
        })
        .catch(() => cached);
      return cached || network;
    })
  );
});

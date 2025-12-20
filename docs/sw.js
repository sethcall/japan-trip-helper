const CACHE_NAME = 'japan-trip-v1';
const URLS_TO_CACHE = [
  './',
  'index.html',
  'itinerary.html',
  'suggestions.html',
  'tips.html',
  'words.html',
  'phrases.html',
  'install.html',
  'css/style.css',
  'js/main.js',
  'js/japanese-data.js',
  'js/learn-japanese.js',
  'js/sw-register.js',
  'manifest.json',
  'assets/cards/keio-plaza-hotel.png'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('Opened cache');
        return cache.addAll(URLS_TO_CACHE);
      })
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        // Cache hit - return response
        if (response) {
          return response;
        }
        return fetch(event.request).then(
          response => {
            // Check if we received a valid response
            // Allow caching of basic (same-origin) and opaque (no-cors) resources if needed, 
            // but usually we just want to cache our own assets.
            // For this trip app, caching everything we touch is good.
            if(!response || response.status !== 200 || response.type !== 'basic') {
              return response;
            }

            const responseToCache = response.clone();

            caches.open(CACHE_NAME)
              .then(cache => {
                cache.put(event.request, responseToCache);
              });

            return response;
          }
        );
      })
  );
});

self.addEventListener('activate', event => {
  const cacheWhitelist = [CACHE_NAME];
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheWhitelist.indexOf(cacheName) === -1) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});

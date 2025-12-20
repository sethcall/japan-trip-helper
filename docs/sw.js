const CACHE_NAME = 'japan-trip-v9';
const URLS_TO_CACHE = [
  './',
  'index.html',
  'itinerary.html',
  'suggestions.html',
  'sunday-schedule.html',
  'subway-tips.html',
  'tips.html',
  'words.html',
  'phrases.html',
  'install.html',
  'currency.html',
  'css/style.css',
  'js/main.js',
  'js/currency.js',
  'js/japanese-data.js',
  'js/learn-japanese.js',
  'js/sw-register.js',
  'js/modal.js',
  'manifest.json',
  'assets/infographics/app-icon.jpg',
  'assets/infographics/phrases-graphic.jpeg',
  'assets/infographics/example_gmaps.png',
  'prince-park.html',
  'assets/photos/le-pain-quotidien-1.jpg',
  'assets/sub_map_eng.pdf'
];

self.addEventListener('install', event => {
  // Force this SW to activate immediately
  self.skipWaiting();
  
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('Opened cache v8');
        return cache.addAll(URLS_TO_CACHE);
      })
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    fetch(event.request)
      .then(response => {
        // Network hit - return and update cache
        if (!response || response.status !== 200 || response.type !== 'basic') {
          return response;
        }

        const responseToCache = response.clone();
        caches.open(CACHE_NAME)
          .then(cache => {
            cache.put(event.request, responseToCache);
          });

        return response;
      })
      .catch(() => {
        // Network failed - return cache
        return caches.match(event.request);
      })
  );
});

self.addEventListener('activate', event => {
  // Take control of all pages immediately
  event.waitUntil(self.clients.claim());

  const cacheWhitelist = [CACHE_NAME];
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheWhitelist.indexOf(cacheName) === -1) {
            console.log('Deleting old cache:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});
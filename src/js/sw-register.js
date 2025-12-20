if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    // --------------------------------------------------------
    // DEV MODE: DISABLE SERVICE WORKER ON LOCALHOST
    // --------------------------------------------------------
    if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
      console.log('Localhost detected: Unregistering Service Workers for development.');
      navigator.serviceWorker.getRegistrations().then(function(registrations) {
        for(let registration of registrations) {
          registration.unregister();
        }
      });
      return; // EXIT: Do not register SW
    }
    // --------------------------------------------------------

    let swPath = 'sw.js';
    // Check if we are in a subdirectory that needs to go up a level
    const path = window.location.pathname;
    if (path.includes('/cards/') || path.includes('/instructions/')) {
        swPath = '../sw.js';
    }
    
    navigator.serviceWorker.register(swPath).then(registration => {
      console.log('ServiceWorker registration successful with scope: ', registration.scope);
    }, err => {
      console.log('ServiceWorker registration failed: ', err);
    });
  });
}
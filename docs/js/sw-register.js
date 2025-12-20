if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    let swPath = 'sw.js';
    // Check if we are in a subdirectory that needs to go up a level
    // This covers cards/ and instructions/ if they exist and are one level deep
    const path = window.location.pathname;
    if (path.includes('/cards/') || path.includes('/instructions/')) {
        swPath = '../sw.js';
    }
    
    // Adjust for local file system or different hosting structures if needed
    // But for standard static serving, this relative pathing should work.

    navigator.serviceWorker.register(swPath).then(registration => {
      console.log('ServiceWorker registration successful with scope: ', registration.scope);
    }, err => {
      console.log('ServiceWorker registration failed: ', err);
    });
  });
}

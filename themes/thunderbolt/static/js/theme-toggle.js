/* Theme toggle: switches between thunderbolt (default) and old-book.
   localStorage key: 'theme'
   Values: 'thunderbolt' | 'old-book'

   FOUC prevention: data-theme is set in <head> before render.
   This script handles the button interaction only.
*/
(function () {
  var btn = document.getElementById('theme-toggle');
  if (!btn) return;

  var html = document.documentElement;

  function applyTheme(theme) {
    html.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
    if (theme === 'old-book') {
      btn.textContent = '⚡';
      btn.title = 'Switch to Thunderbolt & Lightfoot';
    } else {
      btn.textContent = '📖';
      btn.title = 'Switch to Old Book';
    }
  }

  var current = localStorage.getItem('theme') || 'thunderbolt';
  applyTheme(current);

  btn.addEventListener('click', function () {
    var next = html.getAttribute('data-theme') === 'old-book' ? 'thunderbolt' : 'old-book';
    applyTheme(next);
  });
}());

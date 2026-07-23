/* Fora Digital — mockup behaviour.
   Signature motion is the mask-curtain entrance (see style.css .reveal).
   This file only decides WHEN a curtain opens; the animation itself is CSS.
   Deliberately no fade-up and no count-up (flagged defaults). */

(function () {
  'use strict';

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var items = Array.prototype.slice.call(document.querySelectorAll('.reveal'));

  function openAll() {
    items.forEach(function (el) { el.classList.add('in'); });
  }

  // Reduced motion: nothing to animate — CSS already hides the curtain panel.
  if (reduce || !('IntersectionObserver' in window)) {
    openAll();
    return;
  }

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('in');
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -5% 0px' });

  items.forEach(function (el) { io.observe(el); });

  // Safety net: a curtain must never stay shut. If anything goes wrong with the
  // observer (or an element never intersects), open everything after 2s so content
  // is guaranteed visible.
  window.setTimeout(openAll, 2000);
})();

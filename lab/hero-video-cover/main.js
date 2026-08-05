/* Hero-video-cover — lazy hydrate.
   The clip ships with preload="none" and its URL parked on data-src, so a
   visitor who never reaches the hero never pays for it. On intersect we copy
   data-src onto the source, call load(), and play. Every failure path leaves
   the poster in place, which is a finished-looking hero on its own. */
(function () {
  'use strict';

  try {
    var reduce = window.matchMedia &&
                 window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    var vids = [].slice.call(document.querySelectorAll('video[data-lazy]'));

    function hydrate(v) {
      if (v.dataset.loaded) return;
      var s = v.querySelector('source[data-src]');
      if (s) s.src = s.dataset.src;
      v.dataset.loaded = '1';
      v.load();
      var p = v.play();
      if (p && p.catch) p.catch(function () { /* autoplay blocked: poster stays */ });
    }

    if (reduce) {
      // Never fetch the clip at all — CSS is already showing the poster.
      vids.forEach(function (v) { v.dataset.loaded = 'skipped'; });
    } else if (!('IntersectionObserver' in window)) {
      vids.forEach(hydrate);                       // old browser: just load it
    } else {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (!e.isIntersecting) return;
          hydrate(e.target);
          io.unobserve(e.target);
        });
      }, { rootMargin: '200px' });
      vids.forEach(function (v) { io.observe(v); });
    }

    if (window.motionOK) window.motionOK();
  } catch (err) {
    if (window.motionOff) window.motionOff();
  }
})();

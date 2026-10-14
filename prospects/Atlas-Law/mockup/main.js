if (window.motionOK) window.motionOK();

(function () {
  'use strict';

  // Header: hairline shadow once the page scrolls (state, not a set-piece)
  var header = document.querySelector('.site-header');
  if (header) {
    var onScroll = function () { header.classList.toggle('is-scrolled', window.scrollY > 8); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  // Mobile menu: open/close, Escape, close on link tap
  var btn = document.querySelector('.menu-btn');
  var panel = document.getElementById('menu');
  if (btn && panel) {
    var setOpen = function (open) {
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      btn.setAttribute('aria-label', open ? 'Close menu' : 'Menu');
      panel.hidden = !open;
    };
    btn.addEventListener('click', function () {
      setOpen(btn.getAttribute('aria-expanded') !== 'true');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && btn.getAttribute('aria-expanded') === 'true') { setOpen(false); btn.focus(); }
    });
    panel.addEventListener('click', function (e) { if (e.target.closest('a')) setOpen(false); });
    window.matchMedia('(min-width: 820px)').addEventListener('change', function (m) { if (m.matches) setOpen(false); });
  }

  // Entrance: clip-wipe, once, on the elements the sheet names.
  // A fully clipped element never reports as intersecting, so the observer watches
  // unclipped targets: the media <figure> (its <img> is clipped) and each tile group.
  var media = Array.prototype.slice.call(document.querySelectorAll('.wipe-media'));
  var groups = [];
  document.querySelectorAll('.wipe-tile').forEach(function (el) {
    if (groups.indexOf(el.parentElement) === -1) groups.push(el.parentElement);
  });
  var reveal = function (target) {
    if (target.classList.contains('wipe-media')) { target.classList.add('in'); return; }
    target.querySelectorAll(':scope > .wipe-tile').forEach(function (el) { el.classList.add('in'); });
  };
  var targets = media.concat(groups);
  if (!targets.length) return;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce || !('IntersectionObserver' in window)) { targets.forEach(reveal); return; }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) { reveal(entry.target); io.unobserve(entry.target); }
    });
  }, { threshold: 0.12 });
  targets.forEach(function (el) { io.observe(el); });
})();

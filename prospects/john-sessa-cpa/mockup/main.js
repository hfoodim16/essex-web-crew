/* John Sessa Jr, CPA — "Balanced Books"
   Restraint is the flex: reveal-on-scroll + mobile menu only.
   No cursor replacement, no tilt, no parallax. All motion reduced-motion gated. */
(function () {
  'use strict';

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- Mobile menu ---- */
  var burger = document.getElementById('hamburger');
  var menu = document.getElementById('mobileMenu');
  if (burger && menu) {
    burger.addEventListener('click', function () {
      var open = menu.classList.toggle('open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    });
    // Close on link click
    menu.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        menu.classList.remove('open');
        burger.setAttribute('aria-expanded', 'false');
        burger.setAttribute('aria-label', 'Open menu');
      });
    });
    // Close on Escape
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menu.classList.contains('open')) {
        menu.classList.remove('open');
        burger.setAttribute('aria-expanded', 'false');
        burger.setAttribute('aria-label', 'Open menu');
        burger.focus();
      }
    });
  }

  /* ---- Reveal on scroll ---- */
  var reveals = document.querySelectorAll('.reveal');
  if (reduce || !('IntersectionObserver' in window)) {
    reveals.forEach(function (el) { el.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('in');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
    reveals.forEach(function (el) { io.observe(el); });
  }

  /* ---- Contact form (demo - no real submit) ----------------------------- */
  var msgForm = document.querySelector('.form-ph');
  if (msgForm) {
    msgForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var note = msgForm.querySelector('.form-result');
      if (note) {
        note.textContent = 'Thanks \u2014 this is a demo form. On the live site this reaches John directly. For now, please call (973) 748-5710.';
        note.hidden = false;
      }
    });
  }

})();

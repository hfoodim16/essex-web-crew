/* ============================================================================
   Law Office of Anthony DiSalvo, Esq. — "Porta Aperta"

   Signature motion, per website-plan.md §11:
     entrance  : scale-settle (opacity 0 + scale .97 -> settled), 650ms, 80ms stagger
     hover     : zoom-crop (CSS only)
     set-piece : none, deliberately
     ambient   : one slow doorway-light drift inside the hero arch
   GSAP tier 0 — no library, no vendor folder.

   Rule 0: this file only ADDS the resting class. Every hidden state lives behind
   html.js in style.css, so a missing or broken script leaves the page complete.
   ========================================================================== */

(function () {
  'use strict';

  // "Motion is live, stand down" — cancels the dead-man's timer in <head>.
  if (window.motionOK) window.motionOK();

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ------------------------------------------------ entrance: scale-settle */

  var reveals = document.querySelectorAll('.reveal');

  if (reduced || !('IntersectionObserver' in window)) {
    for (var i = 0; i < reveals.length; i++) reveals[i].classList.add('in');
  } else {
    var io = new IntersectionObserver(function (entries, obs) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add('in');
        obs.unobserve(e.target);           // fire once
      });
    }, { threshold: 0.12, rootMargin: '0px 0px 30% 0px' });   // settle before it's read, no pop-in

    for (var j = 0; j < reveals.length; j++) io.observe(reveals[j]);

    // Anything already in view on load settles immediately.
    requestAnimationFrame(function () {
      for (var k = 0; k < reveals.length; k++) {
        var r = reveals[k].getBoundingClientRect();
        if (r.top < window.innerHeight && r.bottom > 0) reveals[k].classList.add('in');
      }
    });
  }

  /* ------------------------------------------------ ambient: doorway light */

  var glow = document.querySelector('.arch-glow');
  if (glow && !reduced && 'IntersectionObserver' in window) {
    var gio = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        glow.classList.toggle('run', e.isIntersecting);   // pause offscreen
      });
    }, { threshold: 0 });
    gio.observe(glow);
  }

  /* ------------------------------------------------ mobile navigation */

  var burger = document.getElementById('burger');
  var nav = document.getElementById('nav');

  if (burger && nav) {
    var setOpen = function (open) {
      nav.classList.toggle('open', open);
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    };

    burger.addEventListener('click', function () {
      setOpen(burger.getAttribute('aria-expanded') !== 'true');
    });

    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) setOpen(false);
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && burger.getAttribute('aria-expanded') === 'true') {
        setOpen(false);
        burger.focus();
      }
    });
  }

  /* ------------------------------------------------ contact form (demo only)
     Static mockup: no network call. The submit shows an inline confirmation so
     the button is never a dead click and never a disabled grey box. */

  var form = document.getElementById('contact-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var out = document.getElementById('form-result');
      if (!out) return;
      out.textContent = 'Thanks — this is a demo form. On the live site it reaches ' +
        'Anthony directly. For now, please call (973) 233-4778.';
      out.hidden = false;
      out.focus({ preventScroll: true });
    });
  }

})();

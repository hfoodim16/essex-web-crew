/* Gee-Kay Landscaping — "Property Line"
   Motion signature: entrance = slide-alternate · hover = rule-trace edge-lift
   (pure CSS) · set-piece = hero-exit · tempo 620ms cubic-bezier(.2,.75,.25,1).
   Nothing here is required to READ the page — every hidden state is gated on
   the `js` class this file confirms. GSAP tier 0: no library. */
(function () {
  'use strict';

  // "Motion is live, stand down" — cancels the head script's un-hide timer.
  if (window.motionOK) window.motionOK();

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ------------------------------------------------------------ nav ----- */
  var burger = document.querySelector('.burger');
  var nav = document.getElementById('primary-nav');
  if (burger && nav) {
    burger.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) {
        nav.classList.remove('is-open');
        burger.setAttribute('aria-expanded', 'false');
        burger.setAttribute('aria-label', 'Open menu');
      }
    });
  }

  /* ------------------------------------------- entrance: slide-alternate - */
  if (!reduced && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('in');
        io.unobserve(entry.target);
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -6% 0px' });

    document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });
  } else {
    document.querySelectorAll('.reveal').forEach(function (el) { el.classList.add('in'); });
  }

  /* ------------------------------- set-piece: hero-exit + compact header - */
  var head = document.querySelector('.masthead');
  var hero = document.querySelector('.hero');
  var ticking = false;

  function onScroll() {
    var y = window.scrollY || window.pageYOffset;
    if (head) head.classList.toggle('is-compact', y > 12);
    if (hero && !reduced) {
      hero.classList.toggle('is-exiting', y > hero.offsetHeight * 0.55);
    }
    ticking = false;
  }
  window.addEventListener('scroll', function () {
    if (ticking) return;
    ticking = true;
    window.requestAnimationFrame(onScroll);
  }, { passive: true });
  onScroll();

  /* ------------------------------------------- estimate form (demo only) - */
  // No third-party service is wired up. The submit shows an inline confirmation
  // so the control is never a dead click or a disabled button.
  var form = document.getElementById('estimate-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var ok = document.getElementById('form-ok');
      if (ok) {
        ok.hidden = false;
        ok.setAttribute('tabindex', '-1');
        ok.focus();
      }
    });
  }
})();

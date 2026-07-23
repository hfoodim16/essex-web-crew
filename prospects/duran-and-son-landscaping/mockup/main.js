/* ============================================================================
   Duran & Son Landscaping — SPA interactions
   Motion is gated behind prefers-reduced-motion; cursor/magnetic effects also
   disabled on coarse pointers (touch).
   ============================================================================ */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var coarsePointer = window.matchMedia('(pointer: coarse)').matches;

  /* ---------------------------------------------------------------- Footer year */
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  /* ---------------------------------------------------------------- SPA routing */
  var pages = Array.prototype.slice.call(document.querySelectorAll('.page'));
  var navLinks = Array.prototype.slice.call(document.querySelectorAll('.nav-link'));

  function setActivePage(pageId, scrollTarget, fromHash) {
    var target = document.getElementById(pageId);
    if (!target) return;

    pages.forEach(function (p) { p.classList.toggle('active', p === target); });

    // Keep the URL hash in sync for deep-linking / shareable pages
    if (!fromHash) {
      var newHash = '#' + (scrollTarget ? scrollTarget : pageId);
      if (window.history && window.history.replaceState) {
        window.history.replaceState(null, '', newHash);
      }
    }

    navLinks.forEach(function (link) {
      link.classList.toggle('active', link.getAttribute('data-page') === pageId && !link.hasAttribute('data-scroll'));
    });

    // Re-arm reveals inside the newly shown page
    armReveals(target);

    closeMobileNav();

    if (scrollTarget) {
      // Defer so the page is displayed before we measure/scroll
      requestAnimationFrame(function () {
        var el = document.getElementById(scrollTarget);
        if (el) el.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth', block: 'start' });
      });
    } else {
      window.scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' });
    }
  }

  // Delegate all data-page clicks (nav, footer, cards, buttons)
  document.addEventListener('click', function (e) {
    var trigger = e.target.closest('[data-page]');
    if (!trigger) return;
    // Allow the wordmark anchor default? No — intercept for SPA behavior.
    e.preventDefault();
    var pageId = trigger.getAttribute('data-page');
    var scrollTarget = trigger.getAttribute('data-scroll');
    setActivePage(pageId, scrollTarget);
  });

  // In-page scroll buttons that don't switch pages (e.g. "See our services")
  document.addEventListener('click', function (e) {
    var trigger = e.target.closest('[data-scroll]');
    if (!trigger || trigger.hasAttribute('data-page')) return;
    e.preventDefault();
    var el = document.getElementById(trigger.getAttribute('data-scroll'));
    if (el) el.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth', block: 'start' });
  });

  /* ---------------------------------------------------------------- Deep-link routing */
  var contactSectionIds = { contact: 'page-home', services: 'page-home', about: 'page-home' };

  function routeFromHash(fromHash) {
    var raw = (window.location.hash || '').replace('#', '');
    if (!raw) return false;
    if (document.getElementById(raw) && /^page-/.test(raw)) {
      setActivePage(raw, null, fromHash);
      return true;
    }
    if (contactSectionIds[raw]) {
      setActivePage(contactSectionIds[raw], raw, fromHash);
      return true;
    }
    return false;
  }
  routeFromHash(true);
  window.addEventListener('hashchange', function () { routeFromHash(true); });

  /* ---------------------------------------------------------------- Mobile nav */
  var navToggle = document.getElementById('nav-toggle');
  var navLinksEl = document.getElementById('nav-links');

  function closeMobileNav() {
    if (!navLinksEl) return;
    navLinksEl.classList.remove('open');
    if (navToggle) navToggle.setAttribute('aria-expanded', 'false');
  }

  if (navToggle && navLinksEl) {
    navToggle.addEventListener('click', function () {
      var open = navLinksEl.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  /* ---------------------------------------------------------------- Header shadow on scroll */
  var header = document.querySelector('.site-header');
  function onScroll() {
    if (header) header.classList.toggle('scrolled', window.scrollY > 10);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ---------------------------------------------------------------- Reveal on scroll */
  var revealObserver = null;
  if (!reduceMotion && 'IntersectionObserver' in window) {
    revealObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          var el = entry.target;
          // Stagger siblings within a grid
          var delay = parseInt(el.getAttribute('data-stagger') || '0', 10);
          el.style.transitionDelay = delay + 'ms';
          el.classList.add('in');
          revealObserver.unobserve(el);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
  }

  function armReveals(scope) {
    var root = scope || document;
    var items = Array.prototype.slice.call(root.querySelectorAll('.reveal, .pop'));

    // Assign stagger within card grids / trust rows
    var groups = Array.prototype.slice.call(root.querySelectorAll('.card-grid, .trust-row'));
    groups.forEach(function (group) {
      var kids = Array.prototype.slice.call(group.children);
      kids.forEach(function (kid, i) {
        if (kid.classList.contains('reveal') || kid.classList.contains('pop')) {
          kid.setAttribute('data-stagger', String(i * 70));
        }
      });
    });

    items.forEach(function (el) {
      if (el.classList.contains('in')) return;
      if (reduceMotion || !revealObserver) { el.classList.add('in'); return; }
      revealObserver.observe(el);
    });
  }
  armReveals(document);

  /* ---------------------------------------------------------------- Custom cursor */
  if (!coarsePointer && !reduceMotion) {
    var dot = document.querySelector('.cursor-dot');
    var ring = document.querySelector('.cursor-ring');
    var label = ring ? ring.querySelector('.cursor-label') : null;

    if (dot && ring) {
      var mouseX = window.innerWidth / 2, mouseY = window.innerHeight / 2;
      var ringX = mouseX, ringY = mouseY;

      window.addEventListener('mousemove', function (e) {
        mouseX = e.clientX; mouseY = e.clientY;
        dot.style.left = mouseX + 'px';
        dot.style.top = mouseY + 'px';
        document.body.classList.add('cursor-active');
      });

      window.addEventListener('mouseleave', function () {
        document.body.classList.remove('cursor-active');
      });

      (function loop() {
        ringX += (mouseX - ringX) * 0.18;
        ringY += (mouseY - ringY) * 0.18;
        ring.style.left = ringX + 'px';
        ring.style.top = ringY + 'px';
        requestAnimationFrame(loop);
      })();

      // Contextual hover state + labels
      var hoverSel = 'a, button, .svc-card, [data-cursor]';
      document.addEventListener('mouseover', function (e) {
        var t = e.target.closest(hoverSel);
        if (!t) return;
        ring.classList.add('is-hovering');
        if (label) label.textContent = t.getAttribute('data-cursor') || '';
      });
      document.addEventListener('mouseout', function (e) {
        var t = e.target.closest(hoverSel);
        if (!t) return;
        var to = e.relatedTarget && e.relatedTarget.closest ? e.relatedTarget.closest(hoverSel) : null;
        if (to) return;
        ring.classList.remove('is-hovering');
        if (label) label.textContent = '';
      });
    }
  }

  /* ---------------------------------------------------------------- Magnetic buttons */
  if (!coarsePointer && !reduceMotion) {
    var magnets = Array.prototype.slice.call(document.querySelectorAll('[data-magnetic]'));
    magnets.forEach(function (btn) {
      var strength = 0.28;
      btn.addEventListener('mousemove', function (e) {
        var r = btn.getBoundingClientRect();
        var x = e.clientX - (r.left + r.width / 2);
        var y = e.clientY - (r.top + r.height / 2);
        btn.style.transform = 'translate(' + (x * strength) + 'px,' + (y * strength) + 'px)';
      });
      btn.addEventListener('mouseleave', function () {
        btn.style.transform = '';
      });
    });
  }


  /* ---- Contact form (demo — no real submit) ----------------------------- */
  var inqForm = document.querySelector('.contact-form-card');
  if (inqForm) {
    inqForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var note = inqForm.querySelector('.form-result');
      if (note) {
        note.textContent = 'Thanks — this is a demo form. On the live site this reaches Duran & Son directly. For now, please call (862) 252-7030.';
        note.hidden = false;
      }
    });
  }

})();

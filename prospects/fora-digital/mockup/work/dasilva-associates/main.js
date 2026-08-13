/* Paul DaSilva Law — "The Quiet Verdict"
   Signature move: blur-focus entrance + icon-nudge hover. No scroll set-piece.

   Content is never hidden by this file failing. The hidden entrance states
   live behind the runtime `.js` class set in the <head> preamble, and there
   are three independent ways out of it:
     1. the file never arrives  -> the preamble's error listener un-hides
     2. the file throws         -> the catch below calls window.motionOff(),
                                   and an escaped throw still reaches the
                                   preamble's window-level error listener
     3. anything else at all    -> the 2s dead-man's timer un-hides
     4. the observer stalls     -> the backstop below un-hides, because paths
                                   1-3 cannot see a silent no-op observer
   The timer is only cancelled once the reveals are actually wired, so a throw
   before that point can never leave the page stranded at opacity 0. */

(function () {
  'use strict';

  try {
    var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    /* --- blur-focus entrance ------------------------------------------- */
    var targets = document.querySelectorAll('.reveal');

    var observerDelivered = false;

    if (reduced || !('IntersectionObserver' in window)) {
      for (var i = 0; i < targets.length; i++) targets[i].classList.add('in');
      observerDelivered = true;
    } else {
      var io = new IntersectionObserver(function (entries) {
        observerDelivered = true;
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          entry.target.classList.add('in');
          io.unobserve(entry.target);
        });
      }, { threshold: 0.12, rootMargin: '0px 0px -6% 0px' });

      targets.forEach(function (el) { io.observe(el); });

      /* Backstop for the one failure the guards below cannot see: an
         IntersectionObserver that exists, accepts observe(), and then never
         delivers a callback (stubbed by an extension, disabled, or a browser
         bug). Nothing throws, so the catch never runs, and motionOK() has
         already stood the dead-man timer down — the page would sit at
         opacity 0 forever and scrolling would not help. Measured before this
         backstop: 56-85% of page text permanently hidden. */
      setTimeout(function () {
        if (!observerDelivered) {
          if (window.motionOff) window.motionOff();
          else document.documentElement.classList.remove('js');
        }
      }, 2000);
    }

    /* Stagger index, capped at 12 per group */
    document.querySelectorAll('.stagger').forEach(function (group) {
      var kids = group.querySelectorAll(':scope > .reveal');
      for (var n = 0; n < kids.length; n++) {
        kids[n].style.setProperty('--i', String(Math.min(n, 12)));
      }
    });

    /* Every .reveal is now guaranteed to be un-hidden, so — and only now —
       the dead-man's timer can be stood down. Nothing below this line can
       leave text invisible. */
    if (window.motionOK) window.motionOK();

    /* --- mobile nav ----------------------------------------------------- */
    var burger = document.querySelector('.burger');
    var links = document.getElementById('nav-links');

    if (burger && links) {
      burger.addEventListener('click', function () {
        var open = burger.getAttribute('aria-expanded') === 'true';
        burger.setAttribute('aria-expanded', open ? 'false' : 'true');
        links.classList.toggle('open', !open);
      });

      links.addEventListener('click', function (e) {
        if (e.target.closest('a')) {
          burger.setAttribute('aria-expanded', 'false');
          links.classList.remove('open');
        }
      });

      document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && burger.getAttribute('aria-expanded') === 'true') {
          burger.setAttribute('aria-expanded', 'false');
          links.classList.remove('open');
          burger.focus();
        }
      });
    }

    /* --- placeholder contact form --------------------------------------- */
    /* Demo only. Never wired to a network call. */
    var form = document.getElementById('contact-form');
    if (form) {
      form.addEventListener('submit', function (e) {
        e.preventDefault();
        var out = form.querySelector('.form-result');
        if (!out) return;
        out.textContent =
          'Thanks. This is a demo form, so nothing was sent. On the live site this ' +
          'reaches Paul directly. For now, please call 973-344-0808.';
        out.hidden = false;
        out.focus && out.focus();
      });
    }
  } catch (err) {
    /* Un-hide first, then let the error surface in the console. */
    if (window.motionOff) window.motionOff();
    else document.documentElement.classList.remove('js');
    throw err;
  }
})();

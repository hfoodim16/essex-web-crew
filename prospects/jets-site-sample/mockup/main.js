/* New York Jets — Gameday Broadcast
   Signature move: skew-slide entrances, in-frame hovers, one scroll set-piece
   (the 1969 numerals, done in CSS with animation-timeline: view()).

   Rule 0: this file never hides anything. The `js` class armed by the boot
   script in index.html is the only thing that applies an entrance pre-state,
   and a dead-man's timer strips it if this file fails to load. Cancelling that
   timer is the first thing we do, and only because we are here to finish the
   job. */

(function () {
  'use strict';

  var docEl = document.documentElement;
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

  /* --- 0. We're alive: stand down the failsafe. ------------------------- */
  if (window.__jetsFailsafe) {
    window.clearTimeout(window.__jetsFailsafe);
    window.__jetsFailsafe = null;
  }

  /* --- 1. Entrances: skew-slide, revealed on intersection. -------------- */
  var risers = Array.prototype.slice.call(document.querySelectorAll('.rise'));

  function revealAll() {
    risers.forEach(function (el) { el.classList.add('in'); });
  }

  if (reduceMotion.matches || !('IntersectionObserver' in window)) {
    revealAll();
  } else {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('in');
        observer.unobserve(entry.target);
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });

    risers.forEach(function (el) { observer.observe(el); });

    /* If the preference flips mid-session, finish the page immediately. */
    var onPrefChange = function () { if (reduceMotion.matches) revealAll(); };
    if (typeof reduceMotion.addEventListener === 'function') {
      reduceMotion.addEventListener('change', onPrefChange);
    } else if (typeof reduceMotion.addListener === 'function') {
      reduceMotion.addListener(onPrefChange);
    }
  }

  /* --- 2. Mobile menu. -------------------------------------------------- */
  var hamburger = document.getElementById('hamburger');
  var nav = document.getElementById('nav');

  function setMenu(open) {
    if (!hamburger || !nav) return;
    hamburger.setAttribute('aria-expanded', open ? 'true' : 'false');
    hamburger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    nav.classList.toggle('open', open);
  }

  if (hamburger && nav) {
    hamburger.addEventListener('click', function () {
      setMenu(hamburger.getAttribute('aria-expanded') !== 'true');
    });

    nav.addEventListener('click', function (event) {
      if (event.target.closest('a')) setMenu(false);
    });

    document.addEventListener('keydown', function (event) {
      if (event.key !== 'Escape') return;
      if (hamburger.getAttribute('aria-expanded') !== 'true') return;
      setMenu(false);
      hamburger.focus();
    });
  }

  /* --- 3. Placeholder links answer the click. --------------------------- */
  /* Every ticket, privacy and terms link points at a PLACEHOLDER_ token,
     because the client hasn't supplied the real destinations yet. A dead
     click is a defect, so the click gets an inline, spoken answer instead. */
  var note = document.getElementById('demo-note');
  var noteTimer = null;

  var NOTE_TEXT = {
    PLACEHOLDER_TICKET_URL:
      'This is a demo link. On the live site it goes straight to the club’s ticket page. For now, ticket questions go through the ticket team.',
    PLACEHOLDER_PRIVACY_URL:
      'This is a demo link. The privacy policy goes here once the club supplies it.',
    PLACEHOLDER_TERMS_URL:
      'This is a demo link. The terms go here once the club supplies them.'
  };

  document.addEventListener('click', function (event) {
    var link = event.target.closest('a[href^="PLACEHOLDER_"]');
    if (!link || !note) return;

    event.preventDefault();

    note.textContent = NOTE_TEXT[link.getAttribute('href')] ||
      'This is a demo link. The real destination comes from the club.';
    note.hidden = false;

    if (noteTimer) window.clearTimeout(noteTimer);
    noteTimer = window.setTimeout(function () { note.hidden = true; }, 6000);
  });

  /* --- 4. Keep the sticky header out of the way of anchor targets. ------ */
  /* scroll-padding-top handles this in CSS; this only closes the menu so the
     panel isn't left open over the section the visitor just jumped to. */
  window.addEventListener('hashchange', function () { setMenu(false); });

  /* Mark the document as booted, for QA. */
  docEl.setAttribute('data-booted', 'true');
})();

/* Fora Digital — mockup behaviour.
   Signature motion is the mask-curtain entrance (see style.css .reveal).
   This file only decides WHEN a curtain opens; the animation itself is CSS.
   Deliberately no fade-up and no count-up (flagged defaults). */

(function () {
  'use strict';

  // Mark that JS is alive BEFORE anything else. The mask-curtain panels are scoped to
  // .js in style.css, so if this file never loads (or throws), the page renders as plain
  // content instead of a wall of opaque cobalt rectangles.
  document.documentElement.classList.add('js');

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


/* Interactive cobalt "compass field" — a grid of short line segments in the hero that
   rotate to point at the pointer; segments near it grow longer and brighter, so a soft
   spotlight of activity follows the mouse. When the pointer is idle or absent (touch), a
   slow auto-orbit keeps the field breathing. Reduced motion → one calm static frame.

   Perf discipline (learned the EMBERS way): NO shadowBlur, capped segment count, a single
   IntersectionObserver pause when the hero scrolls away, DPR capped at 2. Plain strokes are
   cheap; per-frame shadows are what kill the renderer. */
(function () {
  'use strict';

  var canvas = document.getElementById('hero-field');
  if (!canvas) return;
  var hero = canvas.closest('.hero');
  var ctx = canvas.getContext('2d');
  if (!ctx || !hero) return;

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var coarse = window.matchMedia('(pointer: coarse)').matches;

  // brand cobalt from CSS, with a safe fallback
  var cobalt = (getComputedStyle(document.documentElement)
    .getPropertyValue('--cobalt') || '#2447C2').trim() || '#2447C2';

  var GAP = 30;          // cell spacing in CSS px
  var MAX_CELLS = 1400;  // hard cap (backstop, not a target)
  var RADIUS = 300;      // cursor influence radius in CSS px
  var LEN_MIN = 7, LEN_MAX = 24;

  var W = 0, H = 0, dpr = 1;
  var cells = [];        // {x, y, ramp}  ramp = left→right 0..1
  // pointer state (CSS px, hero-relative). Start at right-center so the very first frame —
  // and any headless screenshot — already shows the spotlight on the empty right side.
  var px = 0, py = 0, tx = 0, ty = 0;
  var lastMove = -99999, usingPointer = false;

  function build() {
    var rect = hero.getBoundingClientRect();
    W = rect.width; H = rect.height;
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    canvas.width = Math.round(W * dpr);
    canvas.height = Math.round(H * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

    // fit the grid with even margins
    var cols = Math.max(2, Math.floor(W / GAP));
    var rows = Math.max(2, Math.floor(H / GAP));
    while (cols * rows > MAX_CELLS) { if (cols >= rows) cols--; else rows--; }
    var ox = (W - (cols - 1) * GAP) / 2;
    var oy = (H - (rows - 1) * GAP) / 2;
    cells = [];
    for (var r = 0; r < rows; r++) {
      for (var c = 0; c < cols; c++) {
        var x = ox + c * GAP;
        cells.push({ x: x, y: oy + r * GAP, ramp: W ? x / W : 0.5 });
      }
    }
    // keep the resting/idle spotlight on the right if the pointer hasn't taken over
    if (!usingPointer) { tx = px = W * 0.72; ty = py = H * 0.44; }
  }

  function draw(now) {
    // idle / touch: drive a virtual pointer on a slow orbit so the field stays alive
    if (!usingPointer || (now - lastMove) > 1600 || coarse) {
      var t = now * 0.00042;
      tx = W * (0.6 + 0.26 * Math.cos(t));
      ty = H * (0.45 + 0.28 * Math.sin(t * 1.23));
    }
    // ease the drawn point toward the target
    px += (tx - px) * 0.08;
    py += (ty - py) * 0.08;

    ctx.clearRect(0, 0, W, H);
    ctx.strokeStyle = cobalt;
    ctx.lineWidth = 1.15;
    ctx.lineCap = 'round';

    for (var i = 0; i < cells.length; i++) {
      var cell = cells[i];
      var dx = px - cell.x, dy = py - cell.y;
      var dist = Math.sqrt(dx * dx + dy * dy);
      var ang = Math.atan2(dy, dx);
      var prox = dist < RADIUS ? (1 - dist / RADIUS) : 0;
      prox *= prox; // ease — tightens the spotlight

      // length: base + cursor spotlight.  alpha: faint on the left (behind the headline),
      // livelier on the right, with a bright bloom right at the cursor.
      var len = LEN_MIN + (LEN_MAX - LEN_MIN) * prox;
      var alpha = (0.07 + 0.28 * cell.ramp) + 0.6 * prox;
      if (alpha > 0.8) alpha = 0.8;

      var half = len / 2, ca = Math.cos(ang) * half, sa = Math.sin(ang) * half;
      ctx.globalAlpha = alpha;
      ctx.beginPath();
      ctx.moveTo(cell.x - ca, cell.y - sa);
      ctx.lineTo(cell.x + ca, cell.y + sa);
      ctx.stroke();
    }
    ctx.globalAlpha = 1;
  }

  // ---- static frame, no rAF loop ----
  // Triggered by reduced-motion, OR by a `?still` capture flag. The flag exists because a
  // continuous rAF loop starves headless Chrome's virtual-time clock, which freezes the
  // reveal-curtain transitions mid-open in screenshots. `?still` paints one representative
  // field frame (spotlight resting on the right) and skips the loop, so QA captures render
  // the real look with the curtains fully open. The live site (no flag) runs the animation.
  var still = /(?:^|[?&])still(?:=|&|$)/.test(window.location.search);
  if (reduce || still) {
    build();
    usingPointer = false;
    tx = px = W * 0.72; ty = py = H * 0.44;
    draw(0);
    return;
  }

  var rafId = 0, running = false;
  function loop(now) { draw(now); rafId = window.requestAnimationFrame(loop); }
  function start() { if (!running) { running = true; rafId = window.requestAnimationFrame(loop); } }
  function stop() { if (running) { running = false; window.cancelAnimationFrame(rafId); } }

  window.addEventListener('pointermove', function (e) {
    var rect = hero.getBoundingClientRect();
    // only treat it as "the user is driving" while the pointer is over the hero
    if (e.clientX < rect.left || e.clientX > rect.right ||
        e.clientY < rect.top || e.clientY > rect.bottom) return;
    usingPointer = true;
    lastMove = (window.performance && performance.now) ? performance.now() : Date.now();
    tx = e.clientX - rect.left;
    ty = e.clientY - rect.top;
  }, { passive: true });

  var resizeTimer = 0;
  window.addEventListener('resize', function () {
    window.clearTimeout(resizeTimer);
    resizeTimer = window.setTimeout(build, 150);
  });

  // pause the loop whenever the hero is off-screen (perf)
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (entries) {
      if (entries[0].isIntersecting) start(); else stop();
    }, { threshold: 0 }).observe(hero);
  } else {
    start();
  }

  build();
  draw(0);   // paint one frame synchronously so the field is visible immediately,
  start();   // even before the first rAF tick (and in throttled/headless capture contexts)
})();

/* New York Jets — "Lights On" hero film.
   One 25-second continuous shot (601 frames, 24fps) scrubbed by scroll on a
   canvas. Same contract as main.js: nothing on this page depends on this file
   to be readable. With scripting dead, reduced motion on, or any capability
   missing, the hero stays a static poster with its copy in normal flow — this
   file only upgrades it.

   Engine notes (why it doesn't jank):
   - Pre-extracted JPEGs on a canvas; never <video currentTime> (seek stutter).
   - createImageBitmap sliding window around the playhead so every draw is a
     GPU blit, never a synchronous JPEG decode on the main thread.
   - Lerped playhead (current += (target - current) * .14) for smooth motion.
   - DPR capped at 1 — the source is 854px wide; more device pixels only
     upscale harder. */

(function () {
  'use strict';

  var FRAME_COUNT = 601;
  var FRAME_DIR = 'frames/';
  var LERP = 0.14;
  var MAX_CROP = 0.22;          /* cover until the crop eats >22%, then contain */
  var AHEAD = 36, BEHIND = 12;  /* decoded-bitmap window, biased down-scroll    */
  var EVICT_AHEAD = 48, EVICT_BEHIND = 24;
  var PUMP = 12;                /* image fetches in flight                      */

  var docEl = document.documentElement;
  var film = document.querySelector('.film');
  var stage = document.querySelector('.film-stage');
  var canvas = document.querySelector('.film-canvas');
  var poster = document.querySelector('.film-poster');
  var fade = document.querySelector('.film-fade');
  var beats = [];

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  var jumpParam = new URLSearchParams(location.search).get('jump');

  function frameSrc(i) {
    var n = String(i + 1);
    while (n.length < 4) n = '0' + n;
    return FRAME_DIR + 'f_' + n + '.jpg';
  }

  /* Static path: everything already reads. Just report ready. */
  function standDown() {
    if (jumpParam !== null) window.scrollTo(0, +jumpParam || 0);
    window.__ready = true;
  }

  if (!film || !canvas || !canvas.getContext ||
      typeof createImageBitmap !== 'function' || reduceMotion.matches) {
    standDown();
    return;
  }

  docEl.classList.add('film-on');

  var ctx = canvas.getContext('2d');
  var images = new Array(FRAME_COUNT);   /* HTMLImageElement once fetched   */
  var loaded = new Array(FRAME_COUNT);   /* true once decodable             */
  var bitmaps = new Map();               /* index -> ImageBitmap            */
  var decoding = new Set();
  var bmpCenter = -999;

  var current = 0, target = 0, displayed = -1, progress = 0;
  var firstDraw = false;

  /* ---- beats: copy overlays driven by film progress ---------------------- */
  Array.prototype.forEach.call(film.querySelectorAll('.beat'), function (el) {
    beats.push({
      el: el,
      in: parseFloat(el.getAttribute('data-in')),
      peak: parseFloat(el.getAttribute('data-peak')),
      out: parseFloat(el.getAttribute('data-out'))
    });
  });

  function beatAlpha(b, p) {
    if (p < b.in || p > b.out) return 0;
    if (p < b.peak) return (p - b.in) / Math.max(1e-4, b.peak - b.in);
    if (b.out > 1.5) return 1;                    /* finale never fades */
    return 1 - (p - b.peak) / Math.max(1e-4, b.out - b.peak);
  }

  /* ---- canvas sizing (DPR capped at 1) ----------------------------------- */
  function resize() {
    var r = stage.getBoundingClientRect();
    canvas.width = Math.round(r.width);
    canvas.height = Math.round(r.height);
    displayed = -1;                                /* force repaint */
  }

  /* ---- fit: cover with a crop budget, contain past it -------------------- */
  function drawBitmap(bm) {
    var cw = canvas.width, ch = canvas.height;
    var sCover = Math.max(cw / bm.width, ch / bm.height);
    var crop = 1 - Math.min(cw / (bm.width * sCover), ch / (bm.height * sCover));
    var s = crop > MAX_CROP ? Math.min(cw / bm.width, ch / bm.height) : sCover;
    var w = bm.width * s, h = bm.height * s;
    ctx.fillStyle = '#0A1F14';
    ctx.fillRect(0, 0, cw, ch);
    ctx.drawImage(bm, (cw - w) / 2, (ch - h) / 2, w, h);
  }

  function nearestFrame(i) {
    if (bitmaps.has(i)) return bitmaps.get(i);
    for (var d = 1; d < FRAME_COUNT; d++) {
      if (bitmaps.has(i - d)) return bitmaps.get(i - d);
      if (bitmaps.has(i + d)) return bitmaps.get(i + d);
    }
    return null;
  }

  function drawFrame(i, force) {
    if (i === displayed && !force) return;
    var bm = bitmaps.get(i);
    if (!bm) {
      bm = nearestFrame(i);
      if (!bm) {
        var img = images[i];                       /* last resort: sync decode */
        if (img && loaded[i]) { drawBitmap(img); displayed = i; markDrawn(); }
        return;
      }
    }
    drawBitmap(bm);
    displayed = i;
    markDrawn();
  }

  function markDrawn() {
    if (firstDraw) return;
    firstDraw = true;
    poster.classList.add('film-poster-off');
  }

  /* ---- decoded-bitmap sliding window ------------------------------------- */
  function ensureBitmaps(center) {
    if (Math.abs(center - bmpCenter) < 3 && bitmaps.size) return;
    bmpCenter = center;
    var lo = Math.max(0, center - BEHIND);
    var hi = Math.min(FRAME_COUNT - 1, center + AHEAD);
    var started = 0;
    for (var i = lo; i <= hi; i++) {
      if (bitmaps.has(i) || decoding.has(i) || !loaded[i]) continue;
      if (++started > 10) { bmpCenter = -999; break; }  /* spread the wave over ticks */
      decoding.add(i);
      (function (idx) {
        createImageBitmap(images[idx]).then(function (b) {
          decoding.delete(idx);
          if (idx < bmpCenter - EVICT_BEHIND || idx > bmpCenter + EVICT_AHEAD) { b.close(); return; }
          bitmaps.set(idx, b);
          if (idx === Math.round(current)) drawFrame(idx, true);
        }).catch(function () { decoding.delete(idx); });
      })(i);
    }
    bitmaps.forEach(function (b, k) {
      if (k < center - EVICT_BEHIND || k > center + EVICT_AHEAD) {
        b.close();
        bitmaps.delete(k);
      }
    });
  }

  /* ---- frame pump: prioritised, concurrency-capped ------------------------ */
  var queue = [];
  for (var q = 0; q < FRAME_COUNT; q++) queue.push(q);
  /* Opening run first — the poster hides boot, but frame 0 should win. */
  queue.sort(function (a, b) { return a - b; });
  var inFlight = 0, cursor = 0;

  function pump() {
    while (inFlight < PUMP && cursor < queue.length) {
      (function (idx) {
        inFlight++;
        var img = new Image();
        img.decoding = 'async';
        img.onload = function () {
          loaded[idx] = true;
          inFlight--;
          if (idx <= 2 && !firstDraw) { ensureBitmaps(0); }
          pump();
        };
        img.onerror = function () { inFlight--; pump(); };
        img.src = frameSrc(idx);
        images[idx] = img;
      })(queue[cursor++]);
    }
  }
  pump();

  /* ---- scroll → progress -------------------------------------------------- */
  function readProgress() {
    var r = film.getBoundingClientRect();
    var travel = r.height - window.innerHeight;
    if (travel <= 0) return 0;
    return Math.max(0, Math.min(1, -r.top / travel));
  }

  /* ---- main tick ---------------------------------------------------------- */
  var jankMax = 0, jankLast = performance.now(), debug = jumpParam === null &&
      new URLSearchParams(location.search).has('debug');

  function tick() {
    var now = performance.now();
    if (debug) {
      jankMax = Math.max(jankMax, now - jankLast);
      if (now % 2000 < 17) { console.log('rAF max ' + jankMax.toFixed(1) + 'ms'); jankMax = 0; }
      jankLast = now;
    }

    progress = readProgress();
    target = progress * (FRAME_COUNT - 1);
    /* A hard flick can put the target far outside the decoded window; chasing
       it frame-by-frame forces synchronous decodes (visible hitch). Snap to
       the window's edge and let the lerp finish the approach. */
    if (Math.abs(target - current) > AHEAD - 6) {
      current = target - Math.sign(target - current) * (AHEAD - 6);
      bmpCenter = -999;                     /* re-aim the window immediately */
    }
    current += (target - current) * LERP;
    if (Math.abs(target - current) < 0.4) current = target;

    var idx = Math.round(current);
    ensureBitmaps(idx);
    drawFrame(idx);

    for (var i = 0; i < beats.length; i++) {
      var a = beatAlpha(beats[i], progress);
      var el = beats[i].el;
      el.style.opacity = a.toFixed(3);
      el.style.transform = 'translateY(' + ((1 - a) * 18).toFixed(1) + 'px)';
      el.style.pointerEvents = a > 0.5 ? 'auto' : 'none';
    }

    if (fade) fade.style.opacity = Math.max(0, Math.min(1, (progress - 0.92) / 0.08)).toFixed(3);

    requestAnimationFrame(tick);
  }

  /* ---- boot ---------------------------------------------------------------- */
  resize();
  window.addEventListener('resize', resize);

  if (jumpParam !== null) {
    history.scrollRestoration = 'manual';
    docEl.style.scrollBehavior = 'auto';
  }

  var readyPoll = window.setInterval(function () {
    /* Ready = frame 0 drawable and the opening window decoded. */
    if (!loaded[0]) return;
    window.clearInterval(readyPoll);
    ensureBitmaps(Math.round(current));
    if (jumpParam !== null) {
      window.scrollTo(0, +jumpParam || 0);
      progress = readProgress();
      current = target = progress * (FRAME_COUNT - 1);
      ensureBitmaps(Math.round(current));
      /* Give the window one beat to decode the jumped-to frames. */
      window.setTimeout(function () {
        drawFrame(Math.round(current), true);
        window.__ready = true;
      }, 900);
    } else {
      window.__ready = true;
    }
  }, 120);

  requestAnimationFrame(tick);
})();

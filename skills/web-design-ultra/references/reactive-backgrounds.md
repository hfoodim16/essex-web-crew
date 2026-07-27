# Reactive backgrounds — fields that move and respond

**Purpose:** the background register of a technology site — a hero that *reacts*. Pointer-tracked line fields, constellation networks, flow ribbons, perspective grids. This is the third file in the background trio:

| File | Layer |
|---|---|
| `backgrounds.md` | **static depth** — gradients, grain, orbs, dot grids |
| `atmosphere.md` | **weather and light** — fog, god rays, motes; ambient, ignores the user |
| **this file** | **reactive and generative** — responds to pointer, scroll, or time |

**Budget: ONE reactive field per site, hero only, and it costs you your scroll set-piece.** It counts against the ≤4 animated systems ceiling shared with the other two files. A constellation field *and* a pinned horizontal strip *and* drifting fog is a page that fights itself.

**Occupational fit matters.** This register reads as tech, SaaS, security, fintech, data, agency, studio. Putting a particle network behind a landscaper or a family law firm is the convention error `color-conventions.md` exists to prevent — name the industry norm and make the honor-or-break call on purpose.

**No WebGL, no three.js.** Everything here is CSS or 2D canvas. `backgrounds.md`'s cost warning stands: a 150 KB 3D dependency for a background is almost never the trade, and this file exists so you don't need one.

---

## Tier 0 — CSS only (no canvas, no rAF)

Reach here first. These cover most of what people mean by "a moving tech background," at roughly zero cost.

### Pointer spotlight
One listener, no loop, no canvas. A gradient follows the cursor.
```css
.spot{position:relative;background:#0b0f1a;--mx:50%;--my:40%}
.spot::before{content:"";position:absolute;inset:0;pointer-events:none;
  background:radial-gradient(520px circle at var(--mx) var(--my),
    hsla(212,90%,60%,.20), transparent 70%);
  transition:opacity .4s}
@media (prefers-reduced-motion: reduce){.spot::before{--mx:70%;--my:35%}}
```
```js
var s=document.querySelector('.spot');
if (matchMedia('(pointer:fine)').matches && matchMedia('(prefers-reduced-motion:no-preference)').matches){
  s.addEventListener('pointermove',function(e){
    var r=s.getBoundingClientRect();
    s.style.setProperty('--mx',(e.clientX-r.left)+'px');
    s.style.setProperty('--my',(e.clientY-r.top)+'px');
  },{passive:true});
}
```
Pairs with any grid below — the spotlight reveals the grid it sits over.

### Animated gradient angle (`@property`)
Real angle interpolation, which plain custom properties can't do.
```css
@property --ang{syntax:'<angle>';initial-value:0deg;inherits:false}
.sweep{background:conic-gradient(from var(--ang),#0b0f1a,#12233f,#0b0f1a);
  animation:spin 22s linear infinite}
@keyframes spin{to{--ang:360deg}}
@media (prefers-reduced-motion: reduce){.sweep{animation:none}}
```

### Grid with a travelling mask
A dot or line grid that only exists where the light is.
```css
.grid{background-image:linear-gradient(hsla(210,60%,70%,.10) 1px,transparent 1px),
  linear-gradient(90deg,hsla(210,60%,70%,.10) 1px,transparent 1px);
  background-size:44px 44px;
  mask-image:radial-gradient(420px circle at var(--mx,50%) var(--my,40%),#000 20%,transparent 75%)}
```
Perspective variant: wrap in `perspective:600px` and `transform:rotateX(62deg)` for the receding-floor look, with a fade mask at the horizon.

### Scroll-linked hue / grid drift
```css
@supports (animation-timeline: scroll()){
  .grid{animation:shift linear;animation-timeline:scroll()}
  @keyframes shift{to{background-position:0 220px,220px 0}}
}
```
Zero JS, and unsupported browsers simply get the static grid.

---

## Tier 1 — Canvas fields

### The harness (write this once, reuse for every field)

Generalized from the shipped `fora-digital` hero field, which is where the perf rules below were learned the hard way. **Every recipe after this is just a `draw` body** — they all inherit DPR capping, count capping, off-screen pausing, debounced resize, the reduced-motion static frame, the `?still` capture flag, and one synchronous first paint.

```js
/* createField(canvas, draw, opts) — hardened 2D field harness.
   draw(ctx, w, h, t, p) where t = ms, p = {x, y, live} in CSS px, host-relative. */
function createField(canvas, draw, opts) {
  opts = opts || {};
  var host = canvas.parentElement, ctx = canvas.getContext('2d');
  if (!ctx || !host) return;

  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var coarse = matchMedia('(pointer: coarse)').matches;
  var still  = /[?&]still\b/.test(location.search);

  var w = 0, h = 0, dpr = 1;
  var p = { x: 0, y: 0, live: false }, tx = 0, ty = 0, lastMove = -1e9;

  function build() {
    var r = host.getBoundingClientRect();
    w = r.width; h = r.height;
    dpr = Math.min(window.devicePixelRatio || 1, 2);      // cap at 2 — 3x costs 2.25x the fill
    canvas.width = Math.round(w * dpr);
    canvas.height = Math.round(h * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    if (!p.live) { tx = p.x = w * .72; ty = p.y = h * .44; }  // resting spotlight, off the headline
    if (opts.onResize) opts.onResize(w, h);
  }

  function frame(now) {
    if (!p.live || coarse || (now - lastMove) > 1600) {    // idle: slow auto-orbit keeps it alive
      tx = w * (.6 + .26 * Math.cos(now * .00042));
      ty = h * (.45 + .28 * Math.sin(now * .00052));
    }
    p.x += (tx - p.x) * .08;                               // ease toward target
    p.y += (ty - p.y) * .08;
    draw(ctx, w, h, now, p);
  }

  // Static frame: reduced motion, or a ?still capture. One representative frame, no loop.
  if (reduce || still) { build(); frame(0); return; }

  var id = 0, running = false;
  function loop(now) { frame(now); id = requestAnimationFrame(loop); }
  function start() { if (!running) { running = true; id = requestAnimationFrame(loop); } }
  function stop()  { if (running) { running = false; cancelAnimationFrame(id); } }

  addEventListener('pointermove', function (e) {
    var r = host.getBoundingClientRect();
    if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) return;
    p.live = true; lastMove = performance.now();
    tx = e.clientX - r.left; ty = e.clientY - r.top;
  }, { passive: true });

  var rt = 0;
  addEventListener('resize', function () { clearTimeout(rt); rt = setTimeout(build, 150); });

  build();
  frame(0);   // paint one frame synchronously — throttled panes and headless capture see it

  // Let the observer own start/stop. Do NOT also call start() here: the observer's first
  // callback is async, so an unconditional start leaves every off-screen field running
  // until it arrives — and on a page with several fields they all run at once.
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (es) {
      for (var i = 0; i < es.length; i++) es[i].isIntersecting ? start() : stop();
    }, { threshold: 0 }).observe(host);
  } else {
    start();                                               // no IO: nothing else can drive it
  }
}
```

Markup — note the explicit `width:100%;height:100%`, which is `critique.md` field note 11:
```html
<section class="hero"><canvas id="field" aria-hidden="true"></canvas> … </section>
```
```css
.hero{position:relative;isolation:isolate}
.hero > canvas{position:absolute;inset:0;width:100%;height:100%;z-index:0;pointer-events:none}
.hero > *:not(canvas){position:relative;z-index:1}
```

### Perf rules (non-negotiable — these are what kill renderers)

1. **Never per-frame `shadowBlur`.** It is the single most expensive thing you can do in a loop and it pegs the renderer. Get glow from overlapping low-alpha strokes instead.
2. **Cap the element count** with a hard backstop, not a hopeful density. Reduce the grid until it fits the cap.
3. **DPR ≤ 2.** A 3× buffer is 2.25× the fill rate for no visible gain.
4. **One `clearRect` per frame**, one `beginPath` per stroke batch where possible. Batch by colour, not per element.
5. **Halve density and radius below 780px**, or skip the field entirely and ship the static gradient — phones are where this hurts.
6. **A renderer timeout while scrolling is a performance finding**, not a tooling annoyance (`critique.md` note 5). Fix the page.
7. Fields are decorative: `aria-hidden="true"`, below content, never the sole carrier of meaning. Their absence must change nothing.

---

## The fields

### Vector / compass field
Short segments that rotate to point at the cursor; the nearest grow longer and brighter, so a soft spotlight of activity follows the pointer. Reads as instrumentation, navigation, precision. *(The shipped `fora-digital` implementation.)*
```js
var GAP = 30, R = 300, LMIN = 7, LMAX = 24, cells = [];
createField(cv, function (ctx, w, h, t, p) {
  ctx.clearRect(0, 0, w, h);
  ctx.strokeStyle = accent; ctx.lineWidth = 1.15; ctx.lineCap = 'round';
  for (var i = 0; i < cells.length; i++) {
    var c = cells[i], dx = p.x - c.x, dy = p.y - c.y;
    var d = Math.sqrt(dx * dx + dy * dy), a = Math.atan2(dy, dx);
    var prox = d < R ? (1 - d / R) : 0; prox *= prox;          // squared ease tightens the spotlight
    var len = LMIN + (LMAX - LMIN) * prox, half = len / 2;
    ctx.globalAlpha = Math.min(.8, (.07 + .28 * c.ramp) + .6 * prox);
    ctx.beginPath();
    ctx.moveTo(c.x - Math.cos(a) * half, c.y - Math.sin(a) * half);
    ctx.lineTo(c.x + Math.cos(a) * half, c.y + Math.sin(a) * half);
    ctx.stroke();
  }
  ctx.globalAlpha = 1;
}, { onResize: function (w, h) {
  var cols = Math.max(2, Math.floor(w / GAP)), rows = Math.max(2, Math.floor(h / GAP));
  while (cols * rows > 1400) { cols >= rows ? cols-- : rows--; }   // hard cap
  var ox = (w - (cols - 1) * GAP) / 2, oy = (h - (rows - 1) * GAP) / 2;
  cells = [];
  for (var r = 0; r < rows; r++) for (var c = 0; c < cols; c++)
    cells.push({ x: ox + c * GAP, y: oy + r * GAP, ramp: w ? (ox + c * GAP) / w : .5 });
}});
```
The `ramp` term fades the left side so a headline sits over quiet field and the busy area stays on the empty right. Always build in a quiet zone for the copy.

### Constellation network
Drifting nodes, lines drawn between near neighbours, the cursor pulling them. The canonical SaaS hero — which is both its strength and its risk: it is *the* recognisable choice, so treat it as the safe option, not the bold one.
```js
var N = [], LINK = 132;
createField(cv, function (ctx, w, h, t, p) {
  ctx.clearRect(0, 0, w, h);
  for (var i = 0; i < N.length; i++) {                      // integrate + wrap
    var n = N[i]; n.x += n.vx; n.y += n.vy;
    if (n.x < 0) n.x += w; if (n.x > w) n.x -= w;
    if (n.y < 0) n.y += h; if (n.y > h) n.y -= h;
  }
  ctx.strokeStyle = accent; ctx.lineWidth = 1;
  for (i = 0; i < N.length; i++) for (var j = i + 1; j < N.length; j++) {
    var a = N[i], b = N[j], dx = a.x - b.x, dy = a.y - b.y, d2 = dx * dx + dy * dy;
    if (d2 > LINK * LINK) continue;
    ctx.globalAlpha = (1 - Math.sqrt(d2) / LINK) * .38;
    ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke();
  }
  ctx.globalAlpha = .85; ctx.fillStyle = accent;            // nodes, brighter near the cursor
  for (i = 0; i < N.length; i++) {
    var n2 = N[i], pd = Math.hypot(p.x - n2.x, p.y - n2.y);
    var rr = pd < 180 ? 2.4 : 1.5;
    ctx.beginPath(); ctx.arc(n2.x, n2.y, rr, 0, 6.284); ctx.fill();
  }
  ctx.globalAlpha = 1;
}, { onResize: function (w, h) {
  var count = Math.min(90, Math.round(w * h / 16000));      // hard cap — the N² loop is the cost
  N = []; for (var i = 0; i < count; i++) N.push({
    x: Math.random() * w, y: Math.random() * h,
    vx: (Math.random() - .5) * .28, vy: (Math.random() - .5) * .28 });
}});
```
**The neighbour loop is O(n²).** 90 nodes is ~4,000 pair tests per frame and fine; 300 nodes is 45,000 and will stutter. The cap is the whole recipe.

### Flow-field ribbons
Particles advected through a smooth pseudo-noise field, leaving trails. Organic, generative, data-ish — the most "designed" of the set.
```js
var P = [];
createField(cv, function (ctx, w, h, t, p) {
  ctx.fillStyle = 'rgba(11,15,26,.06)';                     // low-alpha veil = trails, no clearRect
  ctx.fillRect(0, 0, w, h);
  ctx.strokeStyle = accent; ctx.globalAlpha = .5; ctx.lineWidth = 1;
  var k = t * .00008;
  for (var i = 0; i < P.length; i++) {
    var q = P[i];
    // cheap smooth field — sum of sines beats a real noise lib and needs no dependency
    var ang = Math.sin(q.x * .0042 + k) + Math.cos(q.y * .0038 - k) + Math.sin((q.x + q.y) * .0016);
    ang *= 1.7;
    var nx = q.x + Math.cos(ang) * 1.5, ny = q.y + Math.sin(ang) * 1.5;
    ctx.beginPath(); ctx.moveTo(q.x, q.y); ctx.lineTo(nx, ny); ctx.stroke();
    q.x = nx; q.y = ny; q.life--;
    if (q.life < 0 || q.x < 0 || q.x > w || q.y < 0 || q.y > h) {
      q.x = Math.random() * w; q.y = Math.random() * h; q.life = 120 + Math.random() * 220;
    }
  }
  ctx.globalAlpha = 1;
}, { onResize: function (w, h) {
  P = []; var n = Math.min(420, Math.round(w * h / 3400));
  for (var i = 0; i < n; i++) P.push({ x: Math.random() * w, y: Math.random() * h, life: Math.random() * 300 });
}});
```
The trail veil means the canvas is never cleared — so the **static frame will look empty**. Give it a `?still`/reduced-motion path that runs ~120 warm-up iterations before the single draw, or the capture is a blank rectangle.

### Perspective grid
A receding floor grid scrolling toward the viewer. Retro-futurist, infrastructure, telemetry.
```js
createField(cv, function (ctx, w, h, t) {
  ctx.clearRect(0, 0, w, h);
  var hz = h * .42, off = (t * .04) % 60;
  ctx.strokeStyle = accent; ctx.lineWidth = 1;
  for (var i = 0; i < 26; i++) {                            // horizontals, accelerating toward the eye
    var f = i / 26, y = hz + Math.pow(f, 2.2) * (h - hz) + off * Math.pow(f, 1.6);
    if (y > h) continue;
    ctx.globalAlpha = .06 + .22 * f;
    ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(w, y); ctx.stroke();
  }
  for (i = -14; i <= 14; i++) {                             // verticals converging on the vanishing point
    ctx.globalAlpha = .14;
    ctx.beginPath(); ctx.moveTo(w / 2 + i * (w / 9), h); ctx.lineTo(w / 2 + i * 6, hz); ctx.stroke();
  }
  ctx.globalAlpha = 1;
});
```
Mask the horizon with a gradient overlay or the convergence looks like a bug.

### Data stream
Columns of falling ticks or glyphs. Terminal, security, logs. Use sparingly — it is one step from a screensaver.
```js
var cols = [];
createField(cv, function (ctx, w, h) {
  ctx.fillStyle = 'rgba(11,15,26,.10)'; ctx.fillRect(0, 0, w, h);
  ctx.fillStyle = accent;
  for (var i = 0; i < cols.length; i++) {
    var c = cols[i];
    ctx.globalAlpha = .12 + .5 * Math.random();
    ctx.fillRect(c.x, c.y, 2, 12);
    c.y += c.v;
    if (c.y > h) { c.y = -40 - Math.random() * 200; c.v = .8 + Math.random() * 2.4; }
  }
  ctx.globalAlpha = 1;
}, { onResize: function (w, h) {
  cols = []; for (var x = 8; x < w; x += 26)
    cols.push({ x: x, y: Math.random() * h, v: .8 + Math.random() * 2.4 });
}});
```

### Starfield depth parallax
Three depth layers at different speeds. Space, scale, ambition. Cheapest field here.
```js
var S = [];
createField(cv, function (ctx, w, h, t) {
  ctx.clearRect(0, 0, w, h); ctx.fillStyle = '#fff';
  for (var i = 0; i < S.length; i++) {
    var s = S[i];
    s.x -= s.z * .22; if (s.x < 0) s.x += w;
    ctx.globalAlpha = .18 + s.z * .26;
    ctx.fillRect(s.x, s.y, s.z, s.z);
  }
  ctx.globalAlpha = 1;
}, { onResize: function (w, h) {
  S = []; var n = Math.min(260, Math.round(w * h / 5200));
  for (var i = 0; i < n; i++) S.push({ x: Math.random() * w, y: Math.random() * h, z: 1 + Math.floor(Math.random() * 3) });
}});
```
Link `s.x` to scroll instead of time for a scroll-driven variant — and then it costs no idle frames at all.

### Aurora mesh
Large soft colour blobs drawn as canvas radial gradients. Do this **instead of** the CSS `filter: blur()` + `mix-blend-mode` stack when you need it animated — `atmosphere.md` documents that combination as the #1 compositor trap, and a canvas gradient has none of that cost.
```js
var BLOBS = [{h:212,r:.55},{h:268,r:.45},{h:186,r:.5}];
createField(cv, function (ctx, w, h, t) {
  ctx.clearRect(0, 0, w, h);
  for (var i = 0; i < BLOBS.length; i++) {
    var b = BLOBS[i], k = t * .00007 + i * 2.1;
    var x = w * (.5 + .3 * Math.cos(k * (1 + i * .3)));
    var y = h * (.5 + .3 * Math.sin(k * (1.2 - i * .2)));
    var rad = Math.max(w, h) * b.r;
    var g = ctx.createRadialGradient(x, y, 0, x, y, rad);
    g.addColorStop(0, 'hsla(' + b.h + ',85%,58%,.30)');
    g.addColorStop(1, 'hsla(' + b.h + ',85%,58%,0)');
    ctx.fillStyle = g; ctx.fillRect(0, 0, w, h);
  }
});
```
Three blobs max — each is a full-viewport fill.

### Circuit traces (SVG, no canvas, no loop)
Monoline paths that light along their length. Craft-adjacent tech: hardware, manufacturing, infrastructure.
```js
gsap.fromTo('.trace path',
  { drawSVG: '0% 0%' },
  { drawSVG: '0% 100%', duration: 2.2, ease: 'power1.inOut', stagger: { each: .18, repeat: -1, repeatDelay: 1.4 } });
```
Needs `DrawSVGPlugin` from `gsap.md`; the dash-offset recipe in `motion.md` is the zero-dependency version. This is the only field with no rAF loop of its own, which makes it the cheapest way to look technical.

---

## Pairing guide

| Direction / industry | Field | Tier |
|---|---|---|
| SaaS, developer tools | constellation network *or* pointer spotlight + grid | 1 / 0 |
| Security, infrastructure | data stream, perspective grid | 1 |
| Fintech, data, analytics | vector field, flow ribbons | 1 |
| Agency, studio, portfolio | vector field, aurora mesh | 1 |
| Hardware, manufacturing | circuit traces | SVG |
| Space, science, ambition | starfield parallax | 1 |
| Premium / editorial | pointer spotlight only — restraint IS the flex | 0 |
| Local trade, legal, medical | **none.** Wrong register. Use `backgrounds.md` + `atmosphere.md`. | — |

## Pre-ship checklist

- [ ] Exactly **one** field, hero only, and the scroll set-piece was given up for it.
- [ ] `aria-hidden="true"`, below content, page fully readable with the canvas deleted.
- [ ] Canvas has explicit `width:100%;height:100%` (field note 11) and `pointer-events:none`.
- [ ] Element count capped; DPR capped at 2; **no `shadowBlur` anywhere in the loop**.
- [ ] IntersectionObserver actually stops the loop off-screen — verify, don't assume.
- [ ] One synchronous frame painted at init (field note 12), and `?still` renders a *representative* frame — for trail-based fields, warm up before drawing or you ship a blank rectangle.
- [ ] Reduced motion paints one calm static frame, never blank, never mid-loop.
- [ ] Headline sits over a deliberately quiet zone of the field; body text hits **WCAG AA against the field's brightest frame**, not its average.
- [ ] Density halved or the field dropped below 780px; page still scrolls smoothly (field note 5).
- [ ] The field name is logged to `design-memory.md`'s background-system column.

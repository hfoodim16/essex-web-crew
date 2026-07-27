# GSAP — the JS motion tier (scrub, pin, timelines, split text, SVG)

**Purpose:** the moves CSS can't do. `motion.md` is the vocabulary and the default; this file is what you reach for when a signature move needs scroll-linked scrubbing, pinning, staged sequencing, real text splitting, or SVG draw/morph. GSAP is **free for commercial use including every plugin** (GreenSock Standard License, since Webflow's acquisition) and ships **UMD globals** — a plain `<script>` tag, no build step, works from `file://`.

**Budget: one loadout tier per project, and it must earn its bytes.** If the direction's signature move is a clip-wipe entrance and an underline-draw hover, that's pure CSS — don't ship 114 KB to do it. Same cost-discipline as `backgrounds.md`'s three.js clause.

## When to reach for it

| Reach for GSAP | Stay in CSS (`motion.md`) |
|---|---|
| Scroll-**scrubbed** motion (progress-linked, reversible) | Trigger-once entrance reveals |
| **Pinned** sections, horizontal panels, sticky stacks | Hover personalities, pressed states |
| Staged **timelines** (hero choreography, 4+ beats in sequence) | Single-property transitions |
| **Split text** by line with masking, re-splitting on font load | Word stagger you can hand-wrap with `--i` |
| SVG **draw-in** / **morph**, FLIP layout transitions | Marquees, floats, slow orbits |

Two or fewer rows on the left → keep it CSS-only. `animation-timeline: view()` (in `motion.md`) is still the right zero-JS answer for a *single* scrub; GSAP earns its place when you need scrub **plus** pin, or scrub that must work identically everywhere.

## Loadout tiers

Copy only what the tier needs from `assets/gsap/` into the deliverable's `vendor/`:

```bash
cp ~/.claude/skills/web-design-ultra/assets/gsap/{gsap,ScrollTrigger}.min.js mockup/vendor/
```

| Tier | Files | Raw | Zipped | Buys you |
|---|---|---|---|---|
| **1 — Core** | `gsap.min.js` | 71 KB | 27 KB | timelines, easing, `matchMedia()`, `quickTo` |
| **2 — Scroll** (default) | + `ScrollTrigger.min.js` | 114 KB | 45 KB | batch reveal, scrub, pin, horizontal |
| **3 — Type** | + `SplitText.min.js` | 122 KB | 49 KB | masked line/word/char reveals |
| **à la carte** | `Flip` 24 KB · `MorphSVGPlugin` 20 KB · `DrawSVGPlugin` 4 KB | — | — | only for a named set-piece |

Zipped figures are measured, and deflate is what gzip uses too — so they're also roughly what a static host serves over the wire. One hero image's worth. On a pitch mockup this can push the package past the 200 KB email-attach threshold; that's the manual-attach path, not a blocker.

```html
<!-- before </body>, before main.js -->
<script src="vendor/gsap.min.js"></script>
<script src="vendor/ScrollTrigger.min.js"></script>
<script src="main.js"></script>
```
```js
if (window.gsap) gsap.registerPlugin(ScrollTrigger);
```

**ScrollSmoother is deliberately not vendored.** Momentum-smoothed scrolling hijacks the user's scroll, fights trackpad and screen-reader expectations, and is the single most common accessibility complaint about agency sites. If a direction truly demands it, treat it like three.js: justify it, gate it, ship a fallback.

## Rules (non-negotiable)

1. **Fail visible — the deliverable ships as a zip somebody else unpacks.** Content is visible in CSS; JS *hides then reveals*. A vendored script that 404s must leave a readable page, never blank boxes.
   - Prefer **`gsap.from()`**, which animates *from* a state *to* whatever the CSS already says — the no-JS state is the finished state, for free.
   - Set the pre-state with `gsap.set()` in the same synchronous block, immediately after the library loads, so there's no flash.
   - Never author `opacity: 0` on content in the stylesheet. That is the exact `fora-digital` item-8 failure: hidden-by-default content plus one missing script equals an empty homepage.
   ```js
   if (!window.gsap) return;              // no library → CSS state stands, page reads fine
   if (window.motionOK) window.motionOK(); // cancel motion.md's dead-man's switch
   gsap.set('.reveal', { opacity: 0, y: 24 });
   ```
   Pair this with the `<head>` boot preamble in `motion.md` — it's the half that covers a 404'd `vendor/` file, and its timer **must** be cancelled here or it will un-hide the page mid-session and quietly kill every below-the-fold reveal.
2. **Every gate goes through `gsap.matchMedia()`** — reduced-motion, `pointer:coarse`, and breakpoints in one API that auto-reverts its tweens when a condition flips. This is easier than hand-rolled `matchMedia` guards, so there's no excuse for an ungated effect.
   ```js
   const mm = gsap.matchMedia();
   mm.add({
     ok:      '(prefers-reduced-motion: no-preference)',
     fine:    '(pointer: fine)',
     desktop: '(min-width: 900px)'
   }, (self) => {
     const { ok, fine, desktop } = self.conditions;
     if (!ok) return;                     // reduced motion → nothing runs, gsap.set stays reverted
     /* tweens here; matchMedia reverts them automatically */
   });
   ```
   Under reduced motion, also make sure the pre-state never applied — put the `gsap.set()` *inside* the `ok` branch, or call `gsap.set('.reveal', {clearProps:'all'})`.
3. **`ScrollTrigger.batch()` for anything repeated.** One trigger for a list, not one per card. Free stagger, far fewer scroll listeners.
4. **Clean up.** `ScrollTrigger.getAll().forEach(t => t.kill())` before re-init; `ScrollTrigger.refresh()` after images load or fonts swap (a mis-measured pin is the #1 ScrollTrigger bug).
5. **Capture discipline.** A running scrub keeps a rAF loop alive, which breaks headless virtual-time screenshots — see `critique.md` field note 10 and reuse the `?still` flag (it should follow the same code path as reduced motion). **The `?still` branch must also drop the `.js` class**, not just `clearProps` the GSAP-set values — otherwise the CSS hidden states survive and the capture shows an empty page below the fold:
   ```js
   if (!c.ok || still) {
     document.documentElement.classList.remove('js');
     gsap.set('.reveal, .pin-head', { clearProps: 'all' });
     return;
   }
   ``` Field note 5 still governs: if the browser pane chokes while scrolling, the page is too expensive — that's a performance finding, not a tooling annoyance.
6. **Composition with `atmosphere.md`.** That file owns the ambient layer and its `mix-blend-mode` + `blur` perf trap. Don't scrub a blended, blurred layer — you'll re-composite the whole viewport every frame. Atmosphere drifts on its own clock; GSAP moves the elements.
7. **`immediateRender: false` on every scrubbed tween that touches an element an entrance already animates.** A `gsap.to()` records its start values the moment it's created. If an entrance `gsap.from()` has that element at `opacity: 0` at the time, the scrub adopts 0 as its start and *pins the element invisible at scroll 0* — copy silently gone, no error, only visible if you scroll back to the top. Any hero with both an entrance and a hero-exit hits this.
   ```js
   gsap.to('.hero h1, .hero p', {
     yPercent: -18, opacity: .25, ease: 'none',
     immediateRender: false,                    // ← without this the hero is blank at rest
     scrollTrigger: { trigger: '.hero', start: 'center center', end: 'bottom 20%', scrub: .6 }
   });
   ```
8. **Still one set-piece per site** (`motion.md`'s cap). GSAP makes pinning cheap to write, which is exactly why the cap matters more, not less.

## The standard `main.js` spine

Start every GSAP build from this. It is the whole contract — fail-visible, gated, capture-safe, cleaned up — in one block. Add recipes inside the `matchMedia` callback; change nothing above it.

```js
(function () {
  'use strict';
  if (!window.gsap) return;                       // 1. no library -> CSS state stands, page reads fine
  if (window.motionOK) window.motionOK();         // 2. cancel motion.md's dead-man's switch
  gsap.registerPlugin(ScrollTrigger);             // 3. only the plugins this tier actually loads

  var still = /[?&]still\b/.test(location.search); // 4. capture flag (critique.md notes 10/13/14)
  var mm = gsap.matchMedia();

  mm.add({
    ok:   '(prefers-reduced-motion: no-preference)',
    fine: '(pointer: fine)',
    wide: '(min-width: 861px)'
  }, function (self) {
    var c = self.conditions;

    // 5. reduced motion OR capture: drop the CSS hidden states, settle everything, run nothing.
    //    Removing .js is required — clearProps alone leaves the stylesheet's hidden rules matching.
    if (!c.ok || still) {
      document.documentElement.classList.remove('js');
      gsap.set('.reveal', { clearProps: 'all' });
      return;
    }

    // 6. entrances — one batch per family, never one trigger per element
    gsap.set('.reveal', { opacity: 0, y: 26 });
    ScrollTrigger.batch('.reveal', {
      start: 'top 88%', once: true,
      onEnter: function (b) {
        gsap.to(b, { opacity: 1, y: 0, duration: .8, ease: 'power3.out', stagger: .08, overwrite: true });
      }
    });

    // 7. desktop-only set-pieces go behind c.wide; hover personalities behind c.fine

    return function () {                          // 8. matchMedia reverts its own tweens; kill triggers
      ScrollTrigger.getAll().forEach(function (t) { t.kill(); });
    };
  });

  // 9. late layout shifts move every trigger — refresh after fonts and images settle
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { ScrollTrigger.refresh(); });
  window.addEventListener('load', function () { ScrollTrigger.refresh(); });
})();
```

Pair it with the `<head>` boot preamble in `motion.md` — the two halves are one mechanism.

## Recipes

### Batch reveal — the workhorse
Replaces the hand-rolled IntersectionObserver in every existing `main.js`. Same `.reveal` class, same contract.
```js
gsap.set('.reveal', { opacity: 0, y: 26 });
ScrollTrigger.batch('.reveal', {
  start: 'top 88%',
  once: true,
  onEnter: b => gsap.to(b, { opacity: 1, y: 0, duration: .8, ease: 'power3.out', stagger: .08, overwrite: true })
});
```
Swap the `set`/`to` pair for any entrance family in `motion.md` — `clipPath`, `scale`, `rotate`, `filter` — and the family name is what gets logged to design-memory.

### Scrub parallax
Progress-linked, reversible, no rAF of your own.
```js
gsap.to('.hero-bg', {
  yPercent: 18, ease: 'none',
  scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: true }
});
```
`scrub: true` locks to scroll position; `scrub: 0.6` adds catch-up smoothing (prettier, but keeps the ticker running — see rule 5).

### Pinned section
```js
ScrollTrigger.create({
  trigger: '.chapter', start: 'top top', end: '+=120%', pin: true, pinSpacing: true,
  animation: gsap.timeline().from('.chapter h2', { yPercent: 40, opacity: 0 })
                            .from('.chapter .fig', { scale: .92, opacity: 0 }, '<.2'),
  scrub: 1
});
```

### Horizontal panel strip
The set-piece `motion.md` flags as "high effort" — this is the whole thing.
```js
const panels = gsap.utils.toArray('.hstrip .panel');
gsap.to(panels, {
  xPercent: -100 * (panels.length - 1), ease: 'none',
  scrollTrigger: {
    trigger: '.hstrip', pin: true, scrub: 1,
    end: () => '+=' + document.querySelector('.hstrip').offsetWidth
  }
});
```
Keyboard/touch reachability is on you: every panel needs focusable content that scrolls into view, and the whole strip should collapse to a normal vertical stack under `(max-width: 780px)` via `matchMedia`.

### Staged hero timeline
Four beats in deliberate sequence — the thing a pile of CSS delays can't keep in sync.
```js
gsap.timeline({ defaults: { ease: 'power3.out', duration: .9 } })
  .from('.hero-mark',  { scale: .8, opacity: 0, duration: .6 })
  .from('.hero h1',    { yPercent: 40, opacity: 0 }, '-=.3')
  .from('.hero p',     { y: 20, opacity: 0 }, '-=.55')
  .from('.hero .cta',  { y: 16, opacity: 0, stagger: .08 }, '-=.5');
```
All `.from()` — no JS means the hero simply renders finished.

### Masked line reveal (SplitText)
```js
SplitText.create('.hero h1', {
  type: 'lines', mask: 'lines', autoSplit: true,
  onSplit: self => gsap.from(self.lines, { yPercent: 110, stagger: .09, duration: 1, ease: 'power4.out' })
});
```
`mask: 'lines'` builds the `overflow:hidden` wrappers for you; `autoSplit` re-splits after a webfont swaps, which is the bug that makes hand-rolled splitting look broken on slow connections. SplitText keeps the original text accessible to screen readers. Chars only for short display words.

### SVG draw-in
```js
gsap.from('.underline path', {
  drawSVG: '0%', duration: 1.1, ease: 'power2.inOut',
  scrollTrigger: { trigger: '.underline', start: 'top 85%', once: true }
});
```
Upgrade of `motion.md`'s `stroke-dasharray` recipe — handles multi-segment paths and any direction without `pathLength` gymnastics.

### FLIP layout transition
Filtering a gallery or reordering a grid, animated instead of snapping.
```js
const state = Flip.getState('.card');
grid.classList.toggle('filtered');            // any DOM/class mutation
Flip.from(state, { duration: .6, ease: 'power2.inOut', stagger: .03, absolute: true, onEnter: e => gsap.from(e, {opacity: 0, scale: .9}), onLeave: e => gsap.to(e, {opacity: 0, scale: .9}) });
```

### Morph mark
```js
gsap.to('#mark-a', { morphSVG: '#mark-b', duration: .8, ease: 'power2.inOut', repeat: -1, yoyo: true, repeatDelay: 2 });
```
Brand-mark garnish only. Both paths need comparable point counts or the tween gets mushy.

### Magnetic / cursor follow
`quickTo` is a pre-baked setter — far cheaper than a new tween per `pointermove`.
```js
const xTo = gsap.quickTo(btn, 'x', { duration: .4, ease: 'power3' });
const yTo = gsap.quickTo(btn, 'y', { duration: .4, ease: 'power3' });
btn.addEventListener('pointermove', e => {
  const r = btn.getBoundingClientRect();
  xTo((e.clientX - r.left - r.width / 2) * .3);
  yTo((e.clientY - r.top - r.height / 2) * .3);
});
btn.addEventListener('pointerleave', () => { xTo(0); yTo(0); });
```
Inside the `fine` branch of `matchMedia` — never on touch.

## Pairing guide

| Direction mood | Loadout | Signature move |
|---|---|---|
| Editorial / archival | 3 | masked line reveal + underline-draw hover |
| Premium / restrained | 1 | staged hero timeline + pressed states, nothing scroll-linked |
| Cinematic / immersive | 2 | pinned chapter with scrub + scrim wipe |
| Industrial / technical | 2 + DrawSVG | schematic draw-in + scrub parallax |
| Gallery / portfolio | 2 + Flip | FLIP filter transition + zoom-crop hover |
| Kinetic / bold | 2 | horizontal panel strip + magnetic CTAs |
| Warm local trade | — | stay in CSS; `motion.md` covers it. Bytes belong in the photos. |

## Pre-ship checklist

- [ ] `vendor/` contains only the tier's files, and `index.html` loads them locally — no CDN.
- [ ] Rename `vendor/gsap.min.js` and reload: the page is still fully readable. **This is the gate.**
- [ ] Every tween lives inside a `gsap.matchMedia()` condition; reduced motion leaves a good static frame with no half-applied pre-state.
- [ ] `ScrollTrigger.batch` used for lists; pins `refresh()` after images/fonts settle.
- [ ] Only one scroll set-piece on the site.
- [ ] Every scrubbed tween that shares an element with an entrance carries `immediateRender: false` — scroll to the very top and confirm the hero copy is actually there.
- [ ] Deliverable screenshots taken with the `?still` flag (`critique.md` notes 10/13/14); no renderer timeout while scrolling.
- [ ] If the page looks frozen in the browser pane, you checked `document.visibilityState` before believing it (note 13).
- [ ] The entrance family + hover personality are named in the direction brief and logged to `design-memory.md`, and neither matches the last 3 projects.

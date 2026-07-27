# Motion — element animations (entrances, reveals, hovers, staggers)

Scope: **element choreography** — how content enters, reacts, and moves. Ambient light/air effects (fog, god rays, shimmer) live in `atmosphere.md`; this file is what the *elements themselves* do.

**Two tiers.** Everything here is plain CSS + a few lines of vanilla JS unless it's marked **`[GSAP]`** — those need the vendored GSAP loadout in `gsap.md`. Default to CSS; reach for the JS tier when the signature move needs scroll-scrubbing, pinning, staged sequencing, real text splitting, or SVG draw/morph. A one-page trade site that ships tier 0 and nails a clip-wipe is not doing it wrong.

## The signature-move system (the anti-same-y rule)

Every AI-built site ships the same trio: **fade-up reveals + staggered text delay + number count-up**. Those are now *flagged defaults* — allowed only as deliberate, justified picks, never all together, and banned when a recent project logged them.

Per build, choose:
1. **ONE entrance family** (below) — applied consistently to all reveals on the site
2. **ONE hover personality** — one micro-interaction language across buttons/cards/links
3. **At most ONE scroll-driven set-piece** — a single memorable moment, not a theme park
4. **ONE tempo** — a single ease + a single stagger value, reused everywhere (below)

Consistency *inside* a site; variety *across* sites. The choice is named in the direction brief (axis 5), logged to design-memory at Stage 8, and banned for the next 3 projects at Stage 4.

## Tempo (pick once, reuse everywhere)

Mixed easing across a page is the loudest amateur tell — it reads as several people animating separately. Commit to one ease and one stagger.

**Durations.** micro/hover 150–250ms · entrance 500–900ms · set-piece 1.0–1.6s · SVG draw 1.2–2.0s.

**Ease, with the character it carries:**

| Ease | Reads as |
|---|---|
| `cubic-bezier(.2,.7,.2,1)` / `power2.out` | neutral, safe default |
| `cubic-bezier(.16,1,.3,1)` / `power4.out` | expensive, slow-settling, editorial |
| `cubic-bezier(.77,0,.18,1)` | decisive, mechanical (wipes and curtains) |
| `cubic-bezier(.34,1.4,.44,1)` / `back.out(1.5)` | playful, springy |
| `ease-in-out` sine | calm, breathing, wellness |
| `steps(n)` | split-flap, terminal, retro |

Never `linear` except marquees and scrubs. **Never the bare `ease` keyword** — the browser default is instantly recognizable.

**Stagger.** 20ms characters · 60ms editorial lines · 70–90ms cards and rows. Cap the *total* stagger span at ~0.7s, so a 10-card grid uses 70ms, not 200ms.

## Entrance families (pick one)

All: trigger once via IntersectionObserver adding `.in` (threshold ~.12, unobserve after), transform/opacity only, gated behind `prefers-reduced-motion`.

**Every hidden state below must be scoped to `html.js` — that's rule 0.** A one-line inline script in `<head>` opts the page in; with JS off or broken, none of these rules ever match and the page renders finished. Wrap the whole block once:

```html
<!-- in <head>, before the stylesheet -->
<script>var d=document.documentElement,t;d.className+=' js';
function undo(){clearTimeout(t);d.classList.remove('js')}
addEventListener('error',function(e){if(e.target&&e.target.tagName==='SCRIPT')undo()},true);
t=setTimeout(undo,2000);window.motionOK=function(){clearTimeout(t)};</script>
```
```js
// first line of main.js, after the library guard — "motion is live, stand down"
if (window.motionOK) window.motionOK();
```
```css
@media (prefers-reduced-motion: no-preference) {
  .js .reveal    { /* the hidden state — clip-path / opacity / transform */ }
  .js .reveal.in { /* the resting state */ }
}
```
Three failure modes, three nets: a **404'd script** trips the capture-phase `error` listener (measured at 16ms, before `DOMContentLoaded` — no visible blank); a script that **loads but throws** before reaching `motionOK()` trips the 2s timer; a **healthy** page cancels the timer and keeps its hidden states. The cancel is not optional — without it the timer un-hides everything mid-session and every below-the-fold reveal silently stops animating.

The snippets below show the `.reveal` / `.reveal.in` pair only; the `.js` prefix and the media wrapper are assumed.

**Fade-up — ⚠ FLAGGED DEFAULT.** `opacity:0; translateY(26px)` → none. Fine, but it's what every AI site does. Use only with justification; never alongside count-up.

**Clip-wipe.** Content revealed by an expanding clip rectangle — crisp, editorial.
```css
.reveal{clip-path:inset(0 100% 0 0);transition:clip-path .8s cubic-bezier(.77,0,.18,1)}
.reveal.in{clip-path:inset(0 0 0 0)}
/* image curtain variant: wrap img; animate inset(0 0 100% 0) → 0 for a top-down unveil */
```

**Mask-curtain.** A solid panel (brand color) slides off the element.
```css
.reveal{position:relative}
.reveal::after{content:"";position:absolute;inset:0;background:var(--accent);transform:scaleX(1);transform-origin:right;transition:transform .7s cubic-bezier(.77,0,.18,1)}
.reveal.in::after{transform:scaleX(0)}
```

**Blur-focus.** Sharpens into place — dreamy/premium. (Filter = costlier; small/medium elements only, never full-bleed.)
```css
.reveal{opacity:0;filter:blur(12px);transition:opacity .7s,filter .9s}
.reveal.in{opacity:1;filter:blur(0)}
```

**Scale-settle.** Grows from 96–98% with a soft overshoot — confident, product-y.
```css
.reveal{opacity:0;transform:scale(.97);transition:opacity .6s,transform .8s cubic-bezier(.34,1.4,.44,1)}
.reveal.in{opacity:1;transform:scale(1)}
```

**Slide-alternate.** Rows enter from alternating sides — rhythmic, editorial.
```css
.reveal{opacity:0;transform:translateX(-40px);transition:.8s cubic-bezier(.2,.7,.2,1)}
.reveal:nth-child(even){transform:translateX(40px)}
.reveal.in{opacity:1;transform:none}
```

**Tilt-settle.** Enters slightly rotated, levels out — playful/crafted.
```css
.reveal{opacity:0;transform:rotate(-2.5deg) translateY(18px);transition:.7s cubic-bezier(.34,1.3,.44,1)}
.reveal.in{opacity:1;transform:none}
```

**Stagger cascade.** Any family + per-item delay via a CSS index — cards, nav items, letters. Cap ~12 items.
```html
<li style="--i:0">…</li><li style="--i:1">…</li>
```
```css
.list .reveal{transition-delay:calc(var(--i) * 70ms)}
```

**Line-draw.** SVG strokes (underlines, dividers, borders) draw themselves in.
```css
.draw path{stroke-dasharray:1;stroke-dashoffset:1}
.draw.in path{stroke-dashoffset:0;transition:stroke-dashoffset 1.1s cubic-bezier(.65,0,.35,1)}
/* set pathLength="1" on the <path> so dasharray/offset are unit-free */
```
[GSAP] upgrade: `DrawSVGPlugin` handles multi-segment paths and any draw direction without the `pathLength` trick — see `gsap.md`.

**Skew-slide.** Enters translated on X with a skew that unwinds to zero — reads as velocity. Automotive, industrial, sport.
```css
.reveal{opacity:0;transform:translateX(-56px) skewX(-7deg);transition:.6s cubic-bezier(.16,1,.3,1)}
.reveal.in{opacity:1;transform:none}
```

**Split-line mask `[GSAP]`.** Each line of a headline rises from behind its own clipped edge. The editorial classic, and the one hand-wrapping can't do reliably — `SplitText` re-splits after a webfont swaps, which is why hand-rolled versions look broken on slow connections.
```js
SplitText.create('.hero h1', { type:'lines', mask:'lines', autoSplit:true,
  onSplit: s => gsap.from(s.lines, {yPercent:110, stagger:.06, duration:1, ease:'power4.out'}) });
```

**Character cascade `[GSAP]`.** Individual glyphs rise/rotate in on a 20ms stagger, optionally `from:'random'`. Kinetic, young, typographic. Display words only (≤ 12 chars) — never body copy, and never on a phone number.

**Word-tumble `[GSAP]`.** Words flip up on `rotationX:-90` over a `perspective` parent — a departures board resolving. Mechanical and playful at once.
```js
SplitText.create('.hero h1', { type:'words', onSplit: s =>
  gsap.from(s.words, {rotationX:-90, opacity:0, transformOrigin:'50% 0', stagger:.05, ease:'back.out(1.4)'}) });
```

**Iris-open `[GSAP]`.** A circular clip expands from a focal point in the hero image. Cinematic, dark-luxury. **Hero only, once per site** — it's a curtain-up, and you only raise the curtain once.
```js
gsap.from('.hero-img', { clipPath:'circle(0% at 62% 40%)', duration:1.4, ease:'power3.inOut' });
```

**Scrub-reveal `[GSAP]`.** The entrance is bound to scroll *progress* rather than a threshold — the element assembles as you scroll and disassembles as you scroll back. Reversible, tactile, and immediately different from every trigger-once site. One section, not the whole page.

## Text moves

- **Split-text stagger (no library):** wrap words in `<span style="--i:n">`, apply any entrance family + `transition-delay:calc(var(--i)*60ms)`. Letters only for short display words (≤12 chars).
- **Highlighter sweep:** `background:linear-gradient(var(--accent),var(--accent)) no-repeat 0 88%/0% 3px` → `.in{background-size:100% 3px}` (underline) or `/0% 45%` → `100% 45%` (marker highlight).
- **Line-by-line mask:** each line in an `overflow:hidden` wrapper; inner span `translateY(110%)` → 0, staggered per line.
- **Typewriter:** niche (terminal/retro directions only). `width` steps + `steps()` easing on a monospace span.
- **Count-up — ⚠ FLAGGED DEFAULT.** Only when the stats genuinely matter to the pitch. Vary it: different easing (fast-then-brake reads best), formats (`400+`, `4.9★`, `$2.1M`), and never more than one row of them. rAF version: ease with `1-Math.pow(1-t,3)`, duration ≤1.2s, fire once via IO.

## Image reveals

- **Clip expand:** `clip-path:inset(12% 12% 12% 12% round 8px)` → `inset(0 round 0)` on enter.
- **Ken Burns settle:** wrapper `overflow:hidden`; img `scale(1.08)` → `scale(1)` over 1.4s on enter (or slow continuous 18s drift for heroes — then it's ambient, keep subtle).
- **Scrim wipe-away:** the plate's gradient scrim `opacity:1 → .6` + image `scale(1.04)→1` on enter — the photo "develops."
- **Color-in:** `filter:grayscale(1)` (or a duotone via blend-mode layer) → full color on enter/hover. Filter cost: contained elements only.

## Scroll-driven (max ONE set-piece per site)

- **Subtle parallax:** background layer translates at ~0.85× scroll speed. Tiny rAF: `el.style.transform = translateY(scrollY * -0.15px)` on the hero only; skip under reduced-motion and `pointer:coarse`.
- **Scroll-scrub (modern CSS, zero JS):**
```css
@supports (animation-timeline: view()) {
  .scrub{animation:grow linear both;animation-timeline:view();animation-range:entry 0% cover 40%}
  @keyframes grow{from{transform:scale(.92);opacity:.4}to{transform:none;opacity:1}}
}
/* no support → element simply renders static. Perfect fallback. */
```
- **Sticky progress:** `position:sticky` section + a progress bar `scaleX` driven by `animation-timeline: scroll()` (same @supports pattern).
- **Horizontal strip:** sticky viewport + inner track translating X on scroll. Hand-rolled this is high effort; `[GSAP]` ScrollTrigger makes it ~8 lines (`gsap.md`). Either way content must stay reachable by keyboard, and the strip collapses to a vertical stack under ~780px.

The rest are `[GSAP]` — recipes in `gsap.md`:

- **Pinned statement:** a section holds still while its headline swaps or a step index advances. Desktop only; must reserve its space.
- **Sticky stacking cards:** process/step cards pin and stack with graded scale + offset. Watch cumulative pin spacing.
- **Hero exit:** as the hero leaves, its content lifts and fades while the header toggles to its compact/solid state. Pairs with any entrance family and costs almost nothing.
- **Theme transition:** scroll position toggles `data-theme` on `<html>` and the whole token block crossfades. The most "art-directed" trick here per byte spent.
- **Marquee velocity:** the `backgrounds.md` marquee, but its speed reacts to scroll velocity. Doubles as a section divider.

## Hover personalities (pick one language)

Guard hover-dependent meaning behind `@media (hover:hover) and (pointer:fine)`.

- **Underline draw:** `background-size 0%→100%` left-to-right on links (pairs with highlighter sweep).
- **Fill sweep:** button pseudo-element `scaleX(0)→1` from origin left behind the label; label color swaps.
- **Magnetic pull:** button translates toward cursor (max ~8px, lerp in rAF), springs back on leave. Premium/playful directions.
- **Lift + tilt:** card `translateY(-6px) rotate3d(…, ≤4°)` + shadow deepen. Never more than 4°.
- **Zoom-crop:** image scales 1.06 inside overflow-hidden frame; caption slides up 4px.
- **Icon nudge:** arrow `translateX(5px)`, external-link icon 45° hop — 150–250ms.
- **Weight-shift:** a variable font's `wght` (and/or `wdth`) axis animates on hover — 400 → 700, or normal → condensed. Pure CSS, needs a variable font, and it's the most distinctive option on this list because almost nobody does it. `a{font-variation-settings:'wght' 400;transition:font-variation-settings .25s}` → `:hover{'wght' 680}`.
- **Rule-trace edge-lift:** card lifts on a directional shadow while a hairline travels its perimeter (two scaling pseudo-elements, or DrawSVG). Craft/heritage register.
- **Crossfade-zoom:** card image cross-dissolves to a second frame while slowly scaling — the natural home for before/after galleries. Use `[GSAP]` Flip if the swap changes layout.
- **Cursor-follow label:** a lerped custom cursor that morphs into a labeled pill ("View" / "Call" / "Before → After") over specific targets. High impact, high cost: needs a genuine touch fallback and must never be the only affordance. (The base custom-cursor recipe lives in `backgrounds.md`; this is the labeled version.)
- **Glyph-scramble `[GSAP]`:** characters shuffle through random glyphs and resolve. Techy — one element per page, never body copy.
- **Pressed state:** `:active{transform:scale(.97)}` everywhere clickable — cheap, always right.

**Never put a hover cue on a non-interactive element.** A plate that lifts but doesn't click is a misleading affordance and fails the click test.

## Continuous element motion (use sparingly, 1–2 per page)

- **Marquee:** infinite band — duplicate track content, `translateX(0→-50%)` linear loop 20–40s; pause on hover; `prefers-reduced-motion` stops it. (backgrounds.md's divider mention points here.)
- **Floating chips/badges:** absolutely-positioned pills with slow `translateY` sine floats (10–16s, offset phases) — the Alder-hero pattern.
- **Slow orbit/rotation:** a decorative ring/asterisk rotating 360° over 30s+ — brand-mark garnish, not content.

## Rules (mirror the critique gate)

0. **Fail visible — content is never hidden by JavaScript.** The deliverable ships as a zip somebody else unpacks and drags onto a host; a script that 404s or throws must still leave a readable page. No content selector may carry `opacity:0`, a covering pseudo-element, a hiding `clip-path`, or an off-screen transform **in the stylesheet** unless a `@media (prefers-reduced-motion: no-preference)` wrapper or a runtime `.js` class guards it. Apply hidden states at runtime; prefer `gsap.from()`, which animates *from* a pre-state *to* whatever the CSS already says. **Verification is a step, not a vibe: rename the script, reload, read every word.** (This is a logged HIGH-severity failure, not a hypothetical — a mockup once rendered as solid accent-colored rectangles with JS off.)
1. Animate **transform/opacity only** (filter/clip-path = flagged costlier; contained elements, never full-viewport).
2. Every effect inside `@media (prefers-reduced-motion: reduce)` kill switch — reveals render visible, loops stop.
3. IO reveals fire **once** (unobserve); stagger caps ≤12; delays ≤ 90ms per step.
4. Hover moves guarded by `(hover:hover) and (pointer:fine)`; scroll set-pieces skipped on `pointer:coarse` where they'd fight touch scrolling.
5. The renderer-timeout smell test applies (see critique.md field notes): if the browser pane chokes scrolling, the motion is too expensive — fix the page.
6. **No default trio.** Fade-up everywhere + text delay + count-up = automatic critique-gate flag.
7. **No entrance may delay the phone number or primary CTA** becoming visible and tappable. Hero motion is done inside ~1.2s; nothing but ambient is still moving at 3s.
8. **Never hijack scroll** — no smooth-scroll libraries, no scroll-jacked full-page sections, no `scroll-behavior:smooth` on the root (it also swallows the programmatic scrolls the critique pass needs).
9. **Combined budget with `atmosphere.md`: ≤ 4 animated systems on a page** (1 entrance + 1 hover + 1 set-piece + ≤ 2 ambient, and if you take two ambient effects you drop the set-piece). Never scrub or parallax a layer that is both blurred and blend-moded — that's atmosphere.md's documented compositor trap.
10. **Choosing a tier.** `[GSAP]` moves need the vendored loadout in `gsap.md`; if the signature is a CSS entrance plus a CSS hover, ship no library at all. Bytes belong in the photographs.

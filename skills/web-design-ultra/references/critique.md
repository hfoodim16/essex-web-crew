# Critique gate — score with your own eyes

Purpose: quality is inconsistent when nobody checks the built result. This stage forces you to *look* at the site (screenshots) and score it before claiming done. No score, no ship.

## How to run

1. Open the site in the browser pane. For a dev-server project, `preview_start` by name. For a **static double-click mockup** (no build step — the crew's `mockup/index.html + style.css + main.js`), start a tiny server and point the pane at it: `cd <mockup dir> && (python3 -m http.server <port> &)` then `navigate` to `http://localhost:<port>/`. (`file://` often blocks fonts/fetch — always serve over http.)
2. Screenshot at **desktop (1280+)**, **mobile (375px)** via `resize_window`, and **dark mode** if the design supports it.
3. Check `read_console_messages` / `preview_logs` for errors and `read_page` for broken structure.
4. Score each dimension 1–10 by looking at the screenshots. Write the scores down in your response.

### Field notes: browser-pane quirks (hard-won — don't re-debug these)

**1. Black frames on programmatic scroll → capture at scroll 0.** The pane reliably screenshots only at scroll position 0; mid-page programmatic scroll returns black frames. To shoot a lower section, `javascript_exec` to `display:none` the sections above it, `scrollTo(0,0)`, then screenshot. Force reveal-animated elements visible first:
```js
document.querySelectorAll('.reveal').forEach(e=>e.classList.add('in'));
document.getElementById('hdr').style.position='static';   // un-fix sticky headers
['.hero','.trust','.svc'].forEach(s=>{const el=document.querySelector(s); if(el) el.style.display='none';});
window.scrollTo(0,0);
```

**2. A washed-out / dim frame is usually a capture artifact — re-shoot before "fixing" it.** A section can come back looking grey and low-contrast even though it renders fine. **Verify with computed styles before changing any CSS:**
```js
const h=document.querySelector('h2'); const cs=getComputedStyle(h);
JSON.stringify({opacity:cs.opacity, color:cs.color, bg:getComputedStyle(document.body).backgroundColor})
```
If the computed color/opacity are correct, just screenshot again — the second frame is normally clean. Do not "fix" a contrast problem that does not exist.

**2b. …but computed styles can go stale too — the screenshot is the tiebreaker.** The reverse also happens: after adding a class (e.g. an IO reveal's `.in`), `getComputedStyle` may keep reporting the *pre-animation* values while the page has actually rendered the final state — the tab throttles style recalc. Symptom: the class is provably on the element and the rule provably parsed (check `document.styleSheets[0].cssRules`), yet computed values don't move. **Screenshot before concluding an animation is broken.** Rule of thumb: computed styles diagnose *color/contrast*; screenshots diagnose *motion/final state*. When the two disagree, believe the pixels.

**3. Swapped an image file? Cache-bust it.** The pane caches aggressively, so replacing `hero.webp` on disk keeps showing the old one. Bust the URL:
```js
const p=[...document.querySelectorAll('.plate')].find(el=>el.style.backgroundImage.includes('masonry'));
p.style.backgroundImage=`url('public/masonry.webp?v=${Math.floor(performance.now())}')`;
```
(Also re-`navigate` for `<img src>` swaps.) If a "replaced" image looks unchanged, suspect cache before suspecting the file.

**4. Scroll via JS, not the `computer` action, on heavy pages.** `computer` scroll can hang and time out. Use `javascript_tool` and disable smooth scrolling first — CSS `scroll-behavior:smooth` swallows programmatic jumps (`scrollTo` silently lands at 0):
```js
document.documentElement.style.scrollBehavior='auto';
document.documentElement.scrollTop = 1000;
```
Also declare `var` not `const` in these one-liners — the pane reuses one JS context, so a repeated `const p` throws "already declared."

**5. A renderer timeout is a PERFORMANCE finding, not just a tooling annoyance.** If scrolling/screenshotting hangs, the page is too expensive — suspect per-frame `shadowBlur`, uncapped particle counts, or a `requestAnimationFrame` loop that never pauses off-screen. Fix the page (cap particles, drop per-particle shadows, pause via `IntersectionObserver`), then re-score Motion polish. Don't just work around the capture.

**6. A fix round needs the same capture discipline as a build round — shoot the section you touched.** Re-review passes tend to ship hero-only frames, because the hero is what captures at scroll 0 without effort. That is exactly how a regression survives: a hero frame cannot show a defect two screens down. **Any round that edits a section must deliver a capture of that section**, using the hide-sections technique in note 1. (Learned on `fora-digital`: a round-1 fix set `h3{display:inline}`, which collapsed the portfolio honesty badge onto the project title — `gapBadgeToTitle` went from `+16px` to `-37px`. Both delivered screenshots were of the hero. It cost a whole extra round.)

**7. `100svh` heroes defeat tall-window full-page captures.** Sizing a headless window to the document height just makes a `min-height:100svh` hero that tall, and everything below is pushed off-frame. For a one-frame capture of a lower section, render a throwaway copy of the page with `.hero{min-height:0!important}` and the reveal curtains forced open, shoot it, then delete the copy. Keep it *beside* the real page so relative asset paths still resolve.

**8. Media-query-only rules need the media query emulated, or you'll measure a false failure.** Tap targets guarded by `@media (pointer:coarse)` measure under 44px in the pane, which is `pointer:fine` — the rule never matches. Prove the rule instead: inject the same declarations into a `<style>`, re-measure, then remove it. Same trap for `prefers-reduced-motion` (use headless Chrome's `--force-prefers-reduced-motion`) and no-JS (`--disable-javascript`).

**9. Verify a selector matches what you think before filing a finding.** `document.querySelector('.founder-card p')` returns the *first* `p` — which may be a tiny caption, not the body copy you meant to measure. A "12.8px bio" finding evaporated on re-check. Enumerate all matches and print their text before concluding anything from a measurement.

**10. A continuous `requestAnimationFrame` loop starves headless Chrome's `--virtual-time-budget`.** If the page has an always-on canvas/rAF animation (a particle field, a shader, a marquee driven by JS), virtual-time screenshots come out with OTHER animations frozen mid-transition — e.g. reveal curtains stuck as solid blocks — at ANY budget (tested to 9s). Real Chrome (the browser pane) renders it fine; it is purely a virtual-time-vs-rAF conflict. Fix: add a `?still` capture flag the animation checks — it paints ONE static frame and skips the loop (reuse the reduced-motion code path), so virtual-time captures render the real look with everything else settled. Take deliverable screenshots with the flag; ship the live animation without it. (Learned on `fora-digital`'s interactive hero field.)

**11. A `<canvas>`'s default size beats `inset:0`.** `<canvas>` carries presentational `width`/`height` attributes (300×150). With `position:absolute; left:0; right:0` the width *hint* wins over the over-constrained inset, so the box silently stays 300px wide. Always give a full-bleed canvas an explicit `width:100%;height:100%`. Symptom: `getBoundingClientRect().width === 300` on an element you expected to fill its parent.

**12. Neither the automation pane nor headless-virtual-time cleanly shows a live rAF canvas — draw one synchronous frame at init.** The browser pane throttles rAF when it isn't the focused surface (canvas reads back blank); headless virtual-time has note 10's problem. Call `draw()` once synchronously right after building the canvas (before starting the loop) so a representative frame always exists regardless of the capture environment; the loop then animates on top in real browsers.

**13. A GSAP page looks completely DEAD in a backgrounded pane tab — that is the tab, not the build.** Note 12 covers canvas; this is worse, because GSAP drives *everything* off rAF. When the pane tab isn't the focused surface, rAF is throttled to zero and the ticker never advances, so every tween sits frozen at its pre-animation state: reveals at `opacity:0`, a hero that never resolves, a page that looks like a fail-visible bug. CSS transitions keep rendering when backgrounded, so nothing before the GSAP tier ever behaved this way — expect to be fooled once.

**Diagnose before you "fix" it.** All three of these confirm the environment, not the page:
```js
document.visibilityState        // "hidden"
gsap.ticker.frame               // stuck at 1
ScrollTrigger.getAll().length   // healthy — triggers built fine, nothing is driving them
```
**Then seek the timeline to see the real end state:**
```js
gsap.globalTimeline.time(6); gsap.ticker.tick();   // then screenshot
```
Note the trap inside the trap: spinning `gsap.ticker.tick()` in a synchronous loop advances almost nothing, because the ticker reads the wall clock and the wall clock barely moves. You must **seek** the timeline; ticking alone does nothing. (Measured on a live build: rAF fired **0 times in 300ms**.)

**14. An infinite GSAP tween re-triggers note 10.** A `repeat: -1` marquee or a numeric `scrub` keeps the ticker permanently busy, so headless `--virtual-time-budget` never settles and captures come out mid-transition at *any* budget. Prefer `scrub: true` over `scrub: 0.6` when a capture matters, and take deliverable screenshots with `?still`.

**Pitch-mockup deliverable:** when the output is a client pitch package, the desktop **and** 375px mobile screenshots are a **required artifact**, saved to the prospect's `screenshots/` folder — not just a verification step. A mockup with no mobile screenshot **fails the gate automatically** (you cannot prove the mobile layout was designed, not shrunk).

## The 10 dimensions

| # | Dimension | What a 9–10 looks like |
|---|-----------|------------------------|
| 1 | **Boldness / distinctiveness** | Memorable, unmistakably not a template. Would place on a gallery. |
| 2 | Visual hierarchy | Eye lands where intended; clear primary/secondary/tertiary. |
| 3 | Typography craft | Distinctive faces, strong size/weight contrast, tight rhythm. Not the generic four. |
| 4 | Color & contrast | Confident palette, WCAG AA body text, accents used with intent. |
| 5 | Spacing rhythm | Consistent scale, generous where it counts, nothing cramped or arbitrary. |
| 6 | Background / depth | Layered — mesh/texture/imagery, not a flat rectangle. |
| 7 | Imagery quality | Style-matched, high-quality, WebP-optimized. No stock-photo feel. |
| 8 | Responsiveness | Mobile is designed, not just shrunk. No overflow, tap targets ≥44px. |
| 9 | Motion polish | Purposeful, smooth, reduced-motion respected — **and it has a signature move you could name from the screenshots alone**. One ease, one stagger, at most one set-piece. Deduct hard for the default trio (fade-up everywhere + staggered text delay + number count-up) used without justification, or motion matching the last 3 design-memory entries. See `motion.md` and `gsap.md`. |
| 10 | Cohesion | Every choice feels from one art director. Nothing off-brand. |

## The gate

Ship only when **all** hold:
- No dimension scored below **7**.
- **Boldness ≥ 8.**
- No console errors, no horizontal overflow at 375px.
- **The JS-off test passes.** Rename the motion script (`main.js`, and `vendor/gsap.min.js` if present), reload, screenshot. Every word must still be readable and every CTA tappable. Content hidden by default and revealed only by JS **caps dimension 9 at 3 and fails outright** — the deliverable ships as a zip somebody else unpacks, so one missing script is a blank homepage. This is written law, not a judgment call: it has already happened once.
- For a **redesign**: the **bold test** passes (below).

## The bold test (redesigns)

Put the before and after screenshots side by side. If a stranger glancing for one second couldn't tell they're different designs, it **fails outright** — this is a subtle pass, and subtle passes get rejected. Fix by changing something structural (layout archetype, type system, color story, or background system), not by nudging spacing. Additive change beats timid change.

## Fix loop

On any failure: name the specific low-scoring dimensions, fix those (edit source), re-screenshot, re-score. Max **3 loops**. If still failing after 3, stop and report honestly: the scores, what's weak, and what you'd change next — do not claim success.

## On pass — two steps, both required

**(a) Log the design choices.** Append one row with: project name, date (`2026-07-21` format), font pairing, palette family, layout archetype, background system, **signature motion** (entrance family + hover personality + tier). Write it to the **same log Stage 4 read** — the project-local `design-memory.md` if the project has one, else the skill's global `data/design-memory.md`. This powers the anti-repetition check for the next project, so skipping it silently breaks divergence for every future build.

**(b) Publish it to Claude Design.** Invoke the **`design-push`** skill on the site directory. The finished site lands at claude.ai/design as a browsable card-per-section design system — one card per block, every page, the tokens as foundations, and the full assembled page as a template — which is where the site gets reviewed and precisely edited before it goes live.

Both steps are on-pass duties of Stage 8, not optional follow-ups. In crew mode the critic owns (a) and **hands (b) to the lead**, because the DesignSync authorization lives in the lead session, not in a subagent — name it in the sign-off message so it doesn't get dropped.

Two things about (b) worth knowing before you run it:
- **A re-push updates the same project in place**, so after a revision round you run it again rather than creating a second project.
- **Claude Design compiles a project's card index exactly once**, the first time it's opened in a browser. A path added after that is invisible forever, so if the bundle's shape changed (new foundations, new templates, newly-discovered pages) the site needs a **fresh** project, not a re-push. `design-push` explains how to tell.

## Rules
- Actually look at the screenshots — don't score from memory of the code.
- Report the scores in your final message; evidence before assertion.
- A passing rubric with a failed bold test is still a fail.

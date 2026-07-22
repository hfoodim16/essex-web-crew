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
| 9 | Motion polish | Purposeful, smooth, reduced-motion respected. |
| 10 | Cohesion | Every choice feels from one art director. Nothing off-brand. |

## The gate

Ship only when **all** hold:
- No dimension scored below **7**.
- **Boldness ≥ 8.**
- No console errors, no horizontal overflow at 375px.
- For a **redesign**: the **bold test** passes (below).

## The bold test (redesigns)

Put the before and after screenshots side by side. If a stranger glancing for one second couldn't tell they're different designs, it **fails outright** — this is a subtle pass, and subtle passes get rejected. Fix by changing something structural (layout archetype, type system, color story, or background system), not by nudging spacing. Additive change beats timid change.

## Fix loop

On any failure: name the specific low-scoring dimensions, fix those (edit source), re-screenshot, re-score. Max **3 loops**. If still failing after 3, stop and report honestly: the scores, what's weak, and what you'd change next — do not claim success.

## On pass

Append to `data/design-memory.md` a row with: project name, date (`2026-07-21` format), font pairing, palette family, layout archetype, background system. This powers the anti-repetition check for the next project.

## Rules
- Actually look at the screenshots — don't score from memory of the code.
- Report the scores in your final message; evidence before assertion.
- A passing rubric with a failed bold test is still a fail.

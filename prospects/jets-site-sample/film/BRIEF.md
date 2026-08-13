# BRIEF — jets-lights-on scroll-film (survives compaction; read me first)

Project: hero scroll-film for the NY Jets sample site.
Site: `/Users/harryfoodim/Projects/essex-web-crew/prospects/jets-site-sample/mockup/` (index.html, style.css, main.js — "Gameday Broadcast" direction: #0A1F14 night, #14472F pine, #1F7A4D turf, #F4F7F3 chalk, Big Shoulders/Chivo, real logo at `mockup/assets/ny-jets-logo.svg`).
Film build dir: `/Users/harryfoodim/Projects/essex-web-crew/prospects/jets-site-sample/film/`
Skill: `/Users/harryfoodim/Downloads/Super website skill v2/scroll-film-studio/` (SKILL.md + references/playbook.md are law).

## Concept (approved by Harry): "LIGHTS ON"
One vector: slow forward push at knee height along the chalk 50-yard-line paint, toward the painted midfield emblem. 5 clips × 5s = 25s. Floodlight banks slam on one by one — dark → quarter → half → full broadcast light → chalk-paint macro resolve into the page's #0A1F14 ground. NO crowds, NO generated logos (real SVG overlays at resolve in HTML).

## Engine + budget (approved — REVISED 2026-08-08)
- PIVOT: user's key is model-scoped (401 on nano-banana-2/NB1 image models). User directed: **use Seedance 2.5** (`bytedance/seedance-2-5`).
- Seedance 2.5 supports duration up to 30s → **single 25s continuous take, no chaining, no keyframes** (user approved "Straight 25s single take"). ~700 cr at 480p (28 cr/s no-video rate), zero retry buffer — user accepted.
- `generate_audio` DEFAULTS TRUE on 2.5 — always send false (3× cost trap).
- Driver: `film/single-take.py` (resumable; task id persisted; browser UA on every request incl. CDN download). Output: `film/build/master-raw.mp4`.
- Kie WAF: EVERY request (API + CDN download) needs a browser User-Agent.
- storyboard.json + seedance-chain.py kept on disk for reference; NOT the active path.

## Gates for the single take
- No junctions exist. Still run continuity-gate.sh over extracted frames (stride 8) to catch mid-take teleports before building.
- Grade transformation: frame 0 vs final frame must read as same journey (dark stadium → chalk paint macro).

## After film passes gates
- assemble.sh → master.mp4 → extract ALL ~601 frames at native fps, 1024px wide `-q:v 6`. Never decimate frames.
- Trim static head frames, set FRAME_COUNT to trimmed count (finishing.md §1).
- Build canvas scrub hero into existing mockup/index.html per references/engine.md (ImageBitmap sliding window ±18/±28, lerp 0.14, DPR cap 1.5, adaptive header, sampled seam color → handoff to #0A1F14, prefers-reduced-motion fallback = static first frame).
- Real ny-jets-logo.svg overlay fades in at film resolve — the generated "emblem" is abstract paint, never a logo stand-in.
- Verify: scripts/verify.js (needs `npm install` in skill scripts dir once), jank p95/max <50ms, copy-gate.js exit 0. Never foreground a server (nohup + curl + pkill).

## State log — COMPLETE 2026-08-08
- [x] Concept approved (A — LIGHTS ON); pivoted to Seedance 2.5 single 25s take (user-approved, 700 cr, receipt 742→42)
- [x] vector-check PASS (storyboard kept for record; single-take prompt derived from it)
- [x] master-raw.mp4: 854×480, 24fps, 601 frames, 25.04s (film/build/)
- [x] continuity-gate PASS (median SSIM 0.951, stride 8)
- [x] head check: no trim needed → FRAME_COUNT = 601 (mockup/frames/f_0001..f_0601.jpg, 11MB)
- [x] hero built: mockup/film.js + .film section in index.html + CSS. 560vh driver (420vh mobile), ImageBitmap window (36 ahead/12 behind, 10 decodes/tick), snap-on-flick, DPR 1, MAX_CROP .22 letterbox, beats at 0/.41/.69/finale, film-fade → #0A1F14. Fail-visible static fallback + reduced-motion respected.
- [x] verify.js jank PASS ×2 (avg 16.7ms, p95 ~18, max 32ms, 0 over 50)
- [x] copy-gate: 1 pre-existing intentional hit (players img-placeholder tiles — voice-spec-mandated, NOT film copy). Film copy clean.
- [x] Screenshots: dark hero beat / first-bank "56 years" / full-blaze "Serving the fans" / finale real-logo — all legible.
- Note: mobile letterboxes the 16:9 film (no credits left for a 9:16 pass — 42 cr remain).
- [x] 2026-08-08 sharpness pass: Harry flagged blur. Root cause = 854px source (ffmpeg default extraction) upscaled ~1.7x by the browser to fill desktop viewport. FREE fix, no credits: re-extracted from cached master-raw.mp4 with `-vf "scale=1280:-2:flags=lanczos,unsharp=5:5:0.8:5:5:0.0" -q:v 4` → mockup/frames/ (23MB, was 11MB). Poster + width/height attrs updated to 1280×720. Re-verified: jank PASS ×1 (max 43.7ms, still <50 target), screenshots confirm visibly sharper grass/paint/lines.

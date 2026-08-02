# Video Generation — two registers

Hero background video, looping product reels, animated OG/social clips. Stills plus the free motion tiers stay the default path — video must earn its way in via the register system below, and a clip-free build is never a deduction.

**All generation runs through the `/generate` skill** (`~/.claude/skills/generate/`), not a direct SDK call. Invoke it with the Skill tool and let it own model choice, provider routing, keys, polling, and logging. It routes Veo 3.1 through Kie AI at roughly a quarter of Google's direct price, and carries Kling 3.0 and Sora 2 for shots Veo can't cover. Read its `models/video-*.md` recipe before every run — that file, not this one, is the authority on request shape and current pricing.

## The two registers

Every generated clip is one of two kinds. They have different gates, different prompt styles, different budgets, and different failure modes. Declare the register in the plan; the critic judges against the declared register.

### FILMED ACTION — documentary proof

Photorealistic footage of real work happening. Its job is **proof**: this business does this physical thing, well.

**Gate — the frame-2 test:** what does frame 2 show that frame 1 cannot? Nothing → ship the still. Real motion that proves or sells → passes. The five legitimate needs:
1. **Physical motion IS the product.** Water feature, fireplace, machine running, food sizzling. A still of a fountain is a dead fountain.
2. **Process proof.** A 10-second timelapse of a crew transforming a yard beats five before/after photos.
3. **Product demo.** SaaS UI, tool in use. (Screen-recording beats AI generation here — Veo cannot render screens or text.)
4. **Atmosphere CSS can't fake.** Real volumetric motion when the brief demands the real thing.
5. **Emotional register.** Venue, travel, ambience — feeling sold, not specs.

**Style:** `imagery.md` photorealism kit applies in full — proud-contractor register, believable-not-glossy, the two-way realism test.
**For:** trades, restaurants, venues, any business whose work is physically visible.
**Never for:** businesses whose product lives on a screen — every filmed attempt becomes a workaround that avoids showing the actual work (see case log).

### DESIGNED LOOP — a motion-design object

Abstract or stylized rendered animation — soft-body forms, liquid glass, slow viscous morphs, flowing gradients — in the site's exact palette. Its job is **register, not proof**: it sets brand temperature the way type and color do. Reference exemplar: Esteban Diácono's portfolio register (slow translucent 3D forms, gallery restraint).

**Gate (frame-2 does NOT apply — it deliberately shows no work):**
- **(a) Occupational fit.** Studio / tech / SaaS / premium / creative brands ONLY — the same register table as `reactive-backgrounds.md`. A designed loop behind a local trade, legal, or medical site is the convention error `color-conventions.md` exists to prevent. Hard no.
- **(b) The moment needs rendered richness no free tier can fake** — subsurface scattering, viscous 3D morph, liquid-glass refraction. If a CSS gradient, atmosphere layer, or canvas field sells the same feeling, use that instead.
- **(c) Budget slot.** It occupies the scroll-set-piece slot in `motion.md`'s ≤4-animated-systems ceiling and is **mutually exclusive with a reactive canvas field** — a page gets one or the other, never both.

**Style — INVERTS the photorealism kit.** Lead the prompt with "Abstract 3D rendered motion-design loop. Not live action, not filmed, not photographic — a clean CGI render." `imagery.md`'s mandatory negative list (`no illustration, no 3D render, no CGI`) applies to the FILMED register only; here the render IS the point. The plan's `:root` palette tokens are mandatory in the prompt (name the hexes' colors in words). Keep the background a flat/gradient field — it's what makes the loop seam stable and the file small.

**Still banned in BOTH registers:** text/lettering of any kind, fabricated staff for a real business, real-brand likeness without rights.

## The decision ladder (cost-ascending — stop at the first rung that serves the brief)

1. `backgrounds.md` static depth — free
2. `atmosphere.md` ambient light/air — free
3. `reactive-backgrounds.md` canvas field — free, tech register, interactive
4. **Designed loop** — paid (≤$2.50), non-interactive but cinematically rich
5. **Filmed action** — paid (≤$1), the only register that proves real work

**ONE clip per site TOTAL, either register, never both.** Most sites ship with zero — rungs 1–3 carry almost every build.

## Authorization

**Solo / interactive builds: opt-in only** — propose register + concept, state clip count × duration × rate, get an explicit yes. Standard tier beyond the caps below, 4K, or >6s always requires this gate in every mode.

**Crew tier (Essex Web Crew): video is NEVER pre-approved.** Images are (2 per mockup); video is the deliberate exception. The **planner** may mark at most ONE `VIDEO` slot with its register and justification — but a marked slot is a **request, not an authorization**. The **lead** takes it to Harry; the **builder** generates only once Harry has said yes to that specific clip; the **critic** hard-fails any clip that ran without one. An unanswered request is a reason to ship the poster still and report, never a reason to assume yes.

Ceilings on what will be considered (these bound the ask — they do not license a run):
- **Filmed action: ≤$1/build** — one clip, ≤8s.
- **Designed loop: ≤$2.50/build** — one clip, ≤8s.
- Because the Kie route runs ~4× cheaper than Google direct, an approved clip can afford **1080p and the full 8s** inside those ceilings. Spend the room on quality.
- **No retries.** One approval buys one run. If the clip is unusable, exhaust the free `ffmpeg` fixes (crossfade loop, boomerang, reframe); still unusable → report and ship the poster still. A regeneration is a fresh ask.
- A second clip, 4K, a non-default model (Kling/Sora), or anything projected above these ceilings → a fresh ask, same route.

## Models — `/generate` picks, you brief

Veo 3.1 (`veo3_fast`) is the default and covers nearly every website clip. `/generate` carries two alternatives worth knowing about:

| Model | Reach for it when | Watch out |
|-------|-------------------|-----------|
| **Veo 3.1** | default — best prompt adherence, start/end-frame control | durations are **4, 6 or 8 seconds only** |
| **Kling 3.0** | a shot needs **12s+ continuous** motion, or multi-shot character consistency | motion strength can undershoot a subtle prompt — verify |
| **Sora 2** | hard physics realism: water, cloth, crowds | priciest, strict content filter |

Because Kie runs ~4× cheaper than Google direct, the crew caps below now buy real quality — **1080p and the full 8s are affordable inside them**. Prefer spending the headroom on resolution and duration over spending it on retries.

## Image-to-video — the preferred path for filmed action

Veo takes 1–3 reference images (`imageUrls`), which makes **image-to-video the default technique for the filmed register**: generate the still first with Nano Banana 2 (see `imagery.md`), then animate it. It's cheaper than text-to-video, holds the art direction the stills already set, and gives far better control over the opening frame — which doubles as your `poster`.

`/generate` requires reference images as **public URLs**; local files get uploaded first via its Kie base64 endpoint. Let the skill handle that — don't hand-roll it.

**Sourcing reference frames from `Inspiration/`:** the crew's `~/Projects/essex-web-crew/Inspiration/` folder holds reference photography and site mockups. Those images may seed an image-to-video shot, but **the output must be a transformation, not an animated copy** — see `inspiration.md` for the transformation rule and why it exists. A clip that is recognizably someone else's photograph with motion added is a fail.

## Hard-won facts

**Universal — these bit us and will bite again:**
- **Text negation does not work.** Veo stamped garbled pseudo-words ("HEDITE", "MEBLITE") on a sketched wireframe despite explicit "no lettering" in the prompt. **Compose text out instead:** no letterable surface — paper sheet, notebook, screen, signage, vehicle, decal, apparel print — legibly in frame at all. The fix is the shot design, not the wording.
- **Negatives go in the prompt text**, each item individually negated (`no text, no letters, no signage, …`), never a bare comma keyword list — a bare list reads as things to include.
- **"Locked-off camera" is not reliably honored** in filmed scenes (a canopy shot drifted from helmet-POV to third-person across 6s). Check first vs last frame before shipping a `loop`; designed loops on flat fields hold composition far better.
- **Always state duration explicitly.** Leaving it to a default produced an 8s clip when 6 was planned, billing ~33% over.
- **A `success` status is not proof of motion.** Pull two frames seconds apart and confirm the motion actually happened before delivering — `/generate` requires this too.
- **File-size physics:** organic filmed scene ≈ 11.7MB/6s; flat-field designed loop ≈ 1MB/6s. Only designed loops ship near the <5MB hero budget without heavy `ffmpeg` work.
- **Free post-processing beats a paid re-run.** A seam jump, bad loop, or wrong crop is usually fixable with a local `ffmpeg` pass (crossfade loop, boomerang, reframe) at zero cost. Always try that before spending a retry.

**Google-direct-SDK only — do NOT apply these to the `/generate` route:** the `negative_prompt` parameter 400s, and `resolution='1080p'` 400s at 6s duration. Via Kie both are non-issues: `resolution` accepts `720p`/`1080p`/`4k`, and negatives are prompt-text either way. These are recorded only so nobody re-derives them if they ever call Google directly.

## Running it

Invoke the `/generate` skill with the Skill tool. Give it: the register, the prompt, aspect ratio, duration (4/6/8), resolution, and any reference image paths. It handles model choice, provider routing, keys, polling, download, and the sidecar log.

`/generate` saves output **flat into its own iCloud generations folder**. For a crew build, **copy the file into the prospect's `mockup/assets/`** and reference that local path from the HTML — never link the iCloud path or an expiring result URL.

## Prompt discipline

**Both registers:** name the camera behavior (locked-off static / slow push), the subject, the light, the mood. Describe continuous loopable motion — no hard start or end, nothing enters or exits frame. Inline the negatives as `no X, no Y` prose. Compose lettering out of the shot. No identifiable faces, no fabricated staff, no real-brand likeness.

**Filmed action additionally:** the `imagery.md` photorealism kit — "shot like real on-the-job footage", honest level framing, natural light, believable-not-glossy, the proud-contractor bar. Frame the work at a distance/angle where no signage, truck lettering, plates, decals, or house numbers can appear.

**Designed loop additionally:** open with the CGI declaration ("Abstract 3D rendered motion-design loop. Not live action, not photographic — a clean CGI render"). Name the palette colors from the plan's `:root` tokens in words ("deep cobalt blue interior, warm cream-linen field, one burnt-clay accent"). One form, slow hypnotic morph, flat or gradient background, soft studio light, gallery restraint. The motion should read as designed, not simulated.

## Shipping the clip

- `<video autoplay muted loop playsinline poster="…">` — the `poster` still is mandatory (a Stage 6 image, or the clip's own first frame exported via `ffmpeg -ss 0 -frames:v 1` on a $0-imagery build).
- `prefers-reduced-motion: reduce` → show the poster still, don't autoplay.
- Target <5MB (ideally <2MB) — compress with `ffmpeg` (`media-processing` skill) if over; filmed clips almost always are.
- Check the loop seam: extract first and last frames, compare. Visible jump → crossfade in-page or re-roll.
- Any nonessential loop pauses when offscreen (`IntersectionObserver`) — same rule as every other animated system.

## Case log (2026-08-01, Fora Digital + Happy Trees tests — the canonical examples)

1. **Linen wall, drifting light** (Lite) — REJECTED: palette-matched wallpaper, showed nothing about the business.
2. **Hands sketching wireframe** (Lite) — REJECTED: Veo stamped "HEDITE"/"MEBLITE" on the paper despite explicit negation. Lesson: compose text out.
3. **Hands arranging color blocks** (Lite) — text-free but read as a craft project, not a business; Lite looked mushy. Lesson: workaround shots that avoid the real product satisfy nobody.
4. **Arborist at canopy height** (Standard) — GOOD: real work, real proof, chartreuse rope on palette, no letterable surface at height. Flaws: camera drifted (loop seam), 11.7MB.
5. **Cobalt soft-body morph on linen** (Standard) — BEST: stable composition, 997KB, palette-exact, no text possible by construction. The designed-loop register's proof of concept.

Root lesson: register choice is the decision that matters. Filmed action when the work is physically visible; designed loop when the product lives on a screen or the goal is brand temperature; nothing at all when rungs 1–3 of the ladder already serve.

## Reference

- [Gemini API video generation docs](https://ai.google.dev/gemini-api/docs/video)

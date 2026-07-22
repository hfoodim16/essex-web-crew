# Imagery — AI-generated visuals via Gemini

Purpose: real, style-matched imagery is how a site stops looking like a stock template. Generate hero visuals, textures, and OG images with the existing `ai-multimodal` (Gemini) skill, matched to the chosen direction's style. **Never ship the generic stock-photo look.**

## How to generate

Command (from `ai-multimodal`; uses its own venv — run verbatim). **One prompt = one image per call**; loop the command for a set. The `--model gemini-3-pro-image` flag is **mandatory** — without it the script silently calls the text model and returns no image. (`gemini-3-pro-image` = "Nano Banana Pro", Google's high-realism image model; it supersedes the older `gemini-2.5-flash-image` for this skill.)
```bash
~/.claude/skills/ai-multimodal/.venv/bin/python \
  ~/.claude/skills/ai-multimodal/scripts/gemini_batch_process.py \
  --task generate \
  --prompt "<prompt formula below>" \
  --output <project>/public/hero.png \
  --model gemini-3-pro-image \
  --aspect-ratio 16:9 \
  --image-size 2K
```
`--aspect-ratio` accepts **only** `1:1 | 16:9 | 9:16 | 4:3 | 3:4`. `--image-size` accepts `1K | 2K | 4K` (default 1K if omitted). **Choose both per the slot — see "Fit the slot" below.**

It occasionally returns a transient `503 UNAVAILABLE` ("high demand") — that is NOT a `limit: 0` billing error; just retry (up to ~3×). A failed 503 produces no image and no charge.

## Fit the slot (choose aspect + resolution per image)

Every generated image must be sized for **where it actually renders** — realism AND correct fit. Decide two things before generating:

**Aspect ratio — by role:**
| Slot | Aspect |
|------|--------|
| Full-bleed / background hero, full-width band | `16:9` |
| Contained portrait hero, arch/framed image | `3:4` |
| Gallery / work / service plates | `4:3` |
| Tall mobile-first feature, phone mockup | `9:16` |
| OG / social share image | `16:9` |
| Avatar, icon-ish detail, square card | `1:1` |

**Resolution — by displayed width (the deciding rule):**
- **2K (~$0.13)** → the image renders **full-bleed or ≥ ~1400px wide** on desktop: background heroes, full-width photo bands, anything the eye sees edge-to-edge. At 16:9, 2K ≈ 2752×1536 — sharp on large retina displays.
- **1K (~$0.04, default)** → **contained** slots: cards, work/gallery plates, arch-framed or split-hero images, sidebars, OG images (1K ≈ 1376×768 at 16:9 — plenty for a 1200×630 OG). Most slots are 1K.
- **4K (~$0.24)** → almost never; only a print or deep-zoom deliverable.

**Then always downscale to the real display size** during WebP optimization (`media_optimizer.py`) — target ~1.5–2× the CSS pixel width for retina, no more. Generate big for a big slot, but never ship a 2752px file into a 640px card. Never upscale a 1K image to fake 2K — regenerate at 2K instead.

### The API key
The key lives in `~/.claude/skills/ai-multimodal/.env` (`GEMINI_API_KEY=…`); an exported shell var wins over it. The Bash tool does **not** source `~/.zshrc`, so the `.env` file is what makes it work in this harness. If the key is missing, copy it from `~/.zshrc` into that `.env`.

### Billing gate — read before assuming failure
Gemini **image generation is a paid feature**. On a free-tier Google project the image model returns `429 RESOURCE_EXHAUSTED` with **`limit: 0`** (not a per-minute rate limit — a zero entitlement). When you see `limit: 0` for `generate_content_free_tier_requests`, **do not retry** — the account needs billing enabled at aistudio.google.com / Google Cloud. Text calls still work free, so a working text call + `limit: 0` on image = billing not enabled, *not* a bad key. Report this to the user; you cannot enable billing for them.

### When generation is unavailable (no key, or `limit: 0`)
Fall back to a strong CSS/SVG treatment from `backgrounds.md`, plus **elegant labeled image slots** (a framed plate with an italic `"— photo"` caption and the intended subject/location) so the layout reads as intentional, not broken. Say explicitly in your report that imagery is the fallback and name what unlocks it. Never ship a bland grey placeholder box.

## Cost discipline (hard rules — real money)

Every generated image costs **real money**. Nano Banana Pro (`gemini-3-pro-image`) is priced by resolution: **~$0.04/image at the default 1024×1024 (1K)** — which is what the script emits — rising to ~$0.13 at 2K and ~$0.24 at 4K. The script requests 1K by default (no resolution flag exposed), so budget at **~$0.04/image**. Generate the fewest the design genuinely needs. The budget depends on the context:

- **Skill tests / demos: exactly ONE image. No exceptions.** Pick the highest-impact slot (usually the hero); static CSS/background treatments for the rest.
- **Crew pitch mockups (Essex Web Crew): hard cap of 2, pre-approved — no need to ask.** The planner marks exactly which slots are `GENERATE` (hero + 1 priority slot), each with its aspect + resolution tier; **every other image slot stays a labeled `<!-- AI-IMAGE: … -->` placeholder** — this is expected, most slots ship as placeholders for the client to fill with real job photos. Cost depends on tier: **~$0.08/prospect** if both are 1K, up to **~$0.27** if both are 2K (typical: one 2K hero + one 1K ≈ $0.17). Do not exceed 2 without the lead asking Harry.
- **Other real builds: announce the count and per-tier cost (`1K ≈ $0.04, 2K ≈ $0.13 each`) and get the user's OK** before generating a set.
- **The client's real logo doesn't count** against any cap — always download and use it locally (never hotlink), never regenerate a real brand's logo.
- **Never regenerate an asset more than once** without asking — the realism QA below allows a single retry, then stop.
- Never generate speculative spares or variations. **Reuse first:** check the project's `public/` or `mockup/assets/` for existing generated images before generating anything.

## Photorealism prompt kit (default for all imagery)

The goal is **believable as a real photograph of this business** — which is NOT the same as beautiful. A flawless magazine shot on a local contractor's site reads as fake instantly; **perfect staging is itself the #1 AI tell.**

### Step 0 — pick the register (before anything else) — ONE register per site

**PROUD CONTRACTOR — the DEFAULT for local businesses, trades, and any real client site.**
The two-way test: *would the business proudly put THIS on their own website — AND would a visitor believe they took it themselves?* It fails both ways: a stock-ad-perfect shot reads fake; a shabby snapshot undercuts the work. Three dials, set independently:

- **The work: always flawless.** The finished job IS the advertisement — crisp pavers, razor mowing stripes, clean bed edges, spotless install. **Never show mess attributable to the business** (clippings left in the street, scattered tools after a "finished" job, half-done edges) — real crews clean up before they shoot. In-progress mess is allowed only in a slot explicitly labeled before/during.
- **The setting: aspirational.** An attractive, well-kept property the client would want to own — handsome colonial/craftsman, good curb appeal, healthy neighborhood. Real-world context cues are good (`mailbox, driveway, a work truck at the curb, glimpse of the street`) but nothing ugly, run-down, or shabby. Clients buy the *after* picture of their own life.
- **The photography: casual-but-flattering, believable.** `taken with a phone, good consumer-camera quality`, honest straight-on or gently angled framing, **level horizon**, natural pleasant light: `bright clear day` · `soft morning sun` · `warm late-afternoon light`. NOT a shoot (banned: editorial, cinematic, magazine, staged, showroom, moody, luxury styling) and NOT a bad snapshot (no crooked framing, no lens-flare wash, no dreary grey gloom, no shallow-DOF/85mm/medium-format language). **Always append the UI-chrome negatives when using phone language:** `no phone UI, no on-screen icons, no status bar, no timestamp overlay, no screen chrome` — the model otherwise renders a literal phone-screen screenshot.

**NO fabricated branding — hard rule (both registers).** The model cannot render a specific real name and WILL invent a fake or garbled one (a truck lettered "GreenWorks," a sign with gibberish) — on a real business's site that is misleading and can even show a *competitor's* name. So: **generated images must contain no readable business name, logo, or signage.** Keep vehicles and signs **unbranded, angled away, or out of frame** — or leave them out entirely ("nothing at all" beats a fake name). Append to negatives whenever a vehicle/sign could appear: `no branding, no lettering on vehicles, no signage, no logos, plain unmarked truck`. If a branded truck or sign is genuinely wanted, generate it **plain** and composite the client's *real* name/logo in the build — never let the model write the brand. (This is the imagery arm of the content-honesty rule: real businesses get real names or none.)

**EDITORIAL — opt-in only.** The pro-shoot language (below) is allowed ONLY when the brand would plausibly commission a photographer (luxury spa, upscale restaurant, premium product brand) AND the direction brief explicitly calls for it. Always state which register you used and why.

**Cohesion rule: one register per site, chosen in the direction brief, applied to EVERY image slot including the hero.** Never mix registers in one build — a casual photo sitting in an editorial gallery (or vice versa) reads as inconsistent and kills trust faster than either register alone.

**Distinct property per project photo.** When a site shows multiple job/project photos (a work gallery), each must depict a visibly DIFFERENT property — vary the architecture (red-brick colonial · gray craftsman · white farmhouse · stone Tudor · cape · stucco), the siding color, the landscaping, and the street. The model defaults to the *same* handsome brick colonial every prompt; identical-looking houses across "different projects in different towns" is an instant AI tell. Give each GENERATE slot its own explicit, different property description. (Same register/light — different house.)

### The prompt shape

`A photograph of [subject], [register camera language], [composition per register], [light per register], [palette tint matching the direction], [realism anchors], [negatives]`

The rules that make it read as real:
1. **Say "photograph," never "image/visual/render."** Lead the prompt with it.
2. **Camera language per register.** Authentic: smartphone/handheld levers above. Editorial (opt-in): `shot on 35mm film` (documentary warmth) · `85mm f/1.8, shallow depth of field` (subject isolation) · `24mm wide-angle` (spaces/architecture) · `medium-format editorial photography` (premium stillness).
3. **One believable light source, per register.** Authentic: ordinary weather from the levers. Editorial: `low golden-hour sun from the west, long soft shadows` / `single window light from the left`. Never "beautiful lighting."
4. **Realism anchors — the casual-photo feel is what reads as real:** texture-level (`subtle grain, natural imperfections, uneven textures`) plus the proud-contractor photography dial (phone-camera look, natural light, level honest framing). This applies to the *photo*, never to the work or setting — those stay flawless and attractive. An over-produced magazine look is the #1 AI tell.
5. **Full negative list, always appended:** `no illustration, no 3D render, no CGI, no painting, no oversaturation, no plastic or waxy textures, no perfect symmetry, no text, no watermark, no logo, no people` (drop `no people` only when people are wanted).

### Realism QA (after every generation)
View the result at full size and hunt the AI tells:
- **Rendering tells:** warped straight lines (fences, pavers, window frames), melted or duplicated details, impossible geometry, texture that repeats unnaturally, over-uniform grass/foliage.
- **The "too perfect" tell:** magazine staging, showroom cleanliness, ideal light everywhere, everything styled — if a stranger would say "that's a stock photo / an ad," it FAILS even if technically flawless. Regenerate once toward the proud-contractor register (casual phone framing, natural light).
- **The "too shabby" tell:** unattractive/run-down setting, mess that implies sloppy work (clippings in the street, tools strewn about a finished job), dreary flat-grey light, crooked framing — believable but NOT something the business would proudly post. Also a FAIL. Regenerate once toward a more attractive property, cleaned-up site, and pleasant light while keeping the casual, non-editorial feel.
- **The target is between them:** flawless work + attractive setting + casual, flattering, believable photography. Both tells above are misses on the same two-way test.

If it fails: **one** regeneration with a tightened prompt targeting the specific flaw — then stop and tell the user rather than burn more paid calls.

## Style → prompt starting points (photographic vocabulary)

| Direction style | Register | Imagery approach |
|-----------------|----------|------------------|
| **Trades / landscaping / home services** | **proud contractor (default)** | phone photo, natural pleasant light (bright clear day / warm afternoon), **flawless finished work at an attractive home** (crisp stripes, clean edges, spotless install), site cleaned up, level flattering framing — no clippings/tools left out, no shabby house, **any truck/sign unbranded or out of frame** (real name composited in the build) |
| **Local dental / medical / salon** | **proud contractor (default)** | phone photo of the real space looking its best — tidy, warm daylight, welcoming, a touch lived-in but not messy; not showroom-styled, not a stock ad |
| Brutalist / kinetic | editorial (opt-in) | 35mm black & white photograph, harsh direct flash, heavy grain, raw documentary |
| Luxury / premium | editorial (opt-in) | medium-format editorial photograph, moody single-source light, deep shadows, muted rich tones |
| SaaS / techy | editorial (opt-in) | macro photograph of real glass/metal/light refraction, studio strobe, shallow DOF (real materials, not 3D abstractions) |
| Maximalist / vibrant | editorial (opt-in) | saturated editorial photograph, bold real-world color blocking, direct flash fashion-photo energy |
| Editorial | editorial (opt-in) | cinematic wide photograph, one anchored light source, negative space for the headline |

**Editorial-register rows are opt-in** — only for brands where a commissioned shoot is believable. When in doubt for a real local business, use the proud-contractor register. Exception: non-photo art (abstract 3D, illustration) only when the direction explicitly calls for it — realism is the default.

## Asset types & sizes

| Asset | Aspect (supported only) | Notes |
|-------|-------------------------|-------|
| Hero | 16:9 | Leave dead space where the headline sits |
| Section texture | 1:1 | Low-contrast so text stays readable over it |
| Card / feature art | 4:3 or 1:1 | Consistent lighting across the set |
| OG / social | generate 16:9, then crop to 1200×630 | Crop/resize with `media_optimizer.py` or Pillow; add the brand mark in the build, not the gen |

Always put a scrim (a dark-to-transparent gradient overlay) between a photo and any text on top — generated images vary in brightness and will break contrast otherwise. Re-check WCAG AA in the critique gate.

## Post-processing (always)

Convert to WebP and size correctly with ai-multimodal's optimizer:
```bash
~/.claude/skills/ai-multimodal/.venv/bin/python \
  ~/.claude/skills/ai-multimodal/scripts/media_optimizer.py \
  --input <project>/public/hero.png \
  --output <project>/public/hero.webp \
  --quality 85
```
Then reference the `.webp` in markup with width/height set and `loading="lazy"` on below-fold images.

## Rules
- Every generated image must match the direction's palette and mood — a mismatched image reads worse than none.
- Generate a small consistent *set* (hero + 2–3 supporting) with shared lighting/treatment, not one-offs.
- Never leave raw multi-MB PNGs in the build; WebP + correct dimensions is mandatory.

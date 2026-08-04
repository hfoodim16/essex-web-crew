# Media policy — image & video fine print

> Extracted from CLAUDE.md (token diet, 2026-08-03): read ON DEMAND by the role that
> needs it, instead of by every teammate at spawn. CLAUDE.md keeps the binding summary;
> where the two ever disagree, CLAUDE.md wins.

## Image policy (hard rule)

**Tiered: 2 real AI images per mockup, placeholders beyond.**

- **Builders generate up to 2 AI images per mockup — HARD CAP.** Use the **`/generate`
  skill** on **`nano-banana-2`** (Google Gemini 3.1 Flash Image, via Kie AI) — say the
  model explicitly, because `/generate`'s default `-lite` is a draft tier and is not
  acceptable for a client-facing image. Priced by resolution: **~$0.04 at 1K, ~$0.06 at
  2K.** Per-prospect ≈ $0.08 (both 1K) to $0.12 (both 2K); typical one-2K-hero-plus-one-1K
  ≈ $0.10. Pre-approved by Harry at the 2-image cap; NEVER exceed 2 without the lead
  asking Harry first.
- **Priority order: the hero first**, then the one next most visible slot — the
  Planner marks these two as `GENERATE` in the plan's image list.
- **The Planner sizes each GENERATE slot** (see the plan-spec below): aspect ratio +
  resolution tier + where it renders. Rule of thumb: **full-bleed / background hero → `2K`;
  contained cards, plates, split-hero, OG → `1K`** (see the "Fit the slot" section of
  `imagery.md`). The Builder passes `aspect_ratio` and `resolution` accordingly.
- **Quality bar — "proud contractor" register is the DEFAULT for trades.** Follow the
  photorealism kit in `~/.claude/skills/web-design-ultra/references/imagery.md`. The bar is
  the **best photo on the business's Google Business profile**: **flawless finished work**
  (crisp stripes, clean edges, spotless install — nothing sloppy, no clippings/tools left
  out) at an **attractive property** (good curb appeal, nice home), shot **casually but
  flatteringly** in pleasant natural light. Two-way test: *would they proudly post it, AND
  would a visitor believe they took it?* **Both fail modes are rejects** — "too perfect /
  stock-ad" (reads fake) AND "too shabby / mediocre" (believable but not worth showing).
  **One register across the whole mockup** (hero + all slots), set by the Planner — never
  mix. Editorial (pro-shoot look) is opt-in with the Planner's justification.
  **No fabricated branding:** generated images must show no readable business name/logo —
  the model invents fake or competitor names (a truck lettered with the wrong brand). Keep
  vehicles/signs unbranded, angled, or out of frame; composite the prospect's REAL name/logo
  in the build if a branded truck or sign is wanted. Optimize to
  WebP, **downscaling to the real display width** (never ship a 2K file into a small slot),
  store in `prospects/<slug>/mockup/assets/`, reference locally (never hotlink).
- **Every slot beyond the 2 stays a labeled AI-IMAGE placeholder** (this is the norm — most image slots ship as marked placeholders for the client to fill with real job photos)**:**

```html
<!-- AI-IMAGE: wide drone shot of a finished bluestone paver patio at golden hour -->
<div class="img-placeholder" role="img" aria-label="Finished bluestone paver patio">
  <span>AI-IMAGE — paver patio, golden hour</span>
</div>
```

Style `.img-placeholder` as a labeled block in the art direction's colors so the
mockup still reads well. Harry generates the remaining images from these prompts before
anything goes to a client (PLAYBOOK Part 3 Reference A). Still banned always: stock
photos, Unsplash/Google image URLs, hotlinked or copyrighted images.


## Video policy (hard rule)

**Default is zero video.** Stills plus the free CSS/GSAP motion tiers carry almost every
mockup, and a clip-free build is never a deduction. **Unlike images, video is NEVER
pre-approved** — the Planner may *request* a clip, but Harry approves each one
individually before the Builder spends anything. Full framework:
`~/.claude/skills/web-design-ultra/references/video.md`.

All generation — images and video alike — runs through the **`/generate` skill**
(`~/.claude/skills/generate/`): Nano Banana 2 for images, Veo 3.1 (`veo3_fast`, Kie AI)
for video. It owns model choice, provider routing, keys, polling and logging; no agent
touches an API key.

**Work the cost-ascending ladder first, stop at the first rung that serves the brief:**
static depth (`backgrounds.md`) → ambient atmosphere (`atmosphere.md`) → reactive canvas
field (`reactive-backgrounds.md`) — all free — then paid video. If a free rung sells the
same feeling, take it.

**Two registers, and a site gets ONE clip TOTAL — either register, never both.**

- **`filmed-action`** — documentary proof. Gate: **the frame-2 test.** What does frame 2
  show that frame 1 cannot? Nothing → ship the still. Real motion that proves or sells
  (water feature, fire, a process/timelapse proof, venue ambience) → justified. For
  businesses whose work is **physically visible**. Photorealism kit applies in full.
  **Ceiling: ≤$1**, ≤8s.
- **`designed-loop`** — an abstract rendered motion object in the site's exact palette; its
  job is **brand register, not proof**, so frame-2 does not apply. Gate: **occupational fit
  — studio / tech / SaaS / premium / creative ONLY** (behind a trade, legal, or medical
  prospect it's the convention error `color-conventions.md` prevents — hard no), the moment
  needs rendered richness no free tier can fake, and it **consumes the scroll-set-piece
  slot** (mutually exclusive with a reactive field). **INVERTS the photorealism kit** — the
  CGI look is the point. **Ceiling: ≤$2.50**, ≤8s.

"It looks premium" and "the hero feels static" are not justifications in either register.

Those dollar figures are **ceilings on what Harry will consider, not budgets the crew may
spend.** Because Kie runs ~4× cheaper than Google direct, an approved clip can afford
1080p and the full 8s inside them — spend the room on quality, never on retries.

- **The Planner marks 0 or 1 `VIDEO` slot** with its **register**, justification, budget,
  duration, aspect, source (text-to-video or an image-to-video seed frame), and poster
  still. **Marking it is a REQUEST.** Unmarked means the Builder ships no clip.
- **The lead takes the request to Harry.** No answer is not a yes — the poster still ships
  alone and the plan is not defective for it.
- **The Builder generates only after Harry approves that specific clip**, to the declared
  register, and never switches it. **No retries** — one approval buys one run; exhaust the
  free `ffmpeg` fixes, then report. A second clip, 4K, >8s, a non-default model
  (Kling/Sora), or any regeneration is a fresh ask.
- **Shipping is part of the rule:** `<video autoplay muted loop playsinline poster="…">`,
  a `prefers-reduced-motion` branch showing the poster still, <~5MB, and a checked loop
  seam. Same content bans in both registers — no readable branding (compose lettering out
  of the shot; negating it does not work), no invented people for a real business.
- **The Critic judges against the declared register** and fails any clip that is
  unauthorized, unjustified, over cap, fallback-less, register-mismatched, or wrong for the
  occupation. The realism test applies to filmed clips only.

**The ONE exception — the client's own logo.** If the business's existing site (or
Facebook / Google Business profile) shows a logo, the mockup must use **that exact
logo** — it's their brand, and the whole pitch is "your site, done right." The Analyst
records the logo's direct image URL in the dossier; the Builder downloads the actual
file into `prospects/<slug>/mockup/assets/` and places it in the header/nav (top-left,
where a logo belongs) with proper alt text (`alt="<Business Name> logo"`). Serve it as a
**local file — never hotlink it**, never redraw or "improve" it, and never substitute a
styled text wordmark when a real logo exists. Only if no logo exists anywhere is a
tasteful text wordmark in the display font the right call.


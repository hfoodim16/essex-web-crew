# Media policy — image & video fine print

> Extracted from CLAUDE.md (token diet, 2026-08-03): read ON DEMAND by the role that
> needs it, instead of by every teammate at spawn. CLAUDE.md keeps the binding summary;
> where the two ever disagree, CLAUDE.md wins.

## Image policy (hard rule)

**There is no image count cap. The site budget is the only limit.**

- **Builders generate as many AI images as the design genuinely needs, priced to fit the
  site's all-in budget** ($1.00 with no video, $1.50 with an approved one — see "The site
  budget" below). Use the **`/generate` skill** on **`nano-banana-2`** (Google Gemini 3.1
  Flash Image, via Kie AI) — say the model explicitly, because `/generate`'s default
  `-lite` is a draft tier and is not acceptable for a client-facing image. Priced by
  resolution: **~$0.04 at 1K, ~$0.06 at 2K.** At those rates $1.00 buys roughly **16 images
  at 2K, or 25 at 1K** — the budget is not the binding constraint on a still-only site, and
  it never was. **Count the projected total before generating and keep it inside the
  budget**; the lead asks Harry before anything that would break it.
- **The constraint that actually binds is design judgment, not money.** Generate the images
  the page needs to look finished and specific — hero, section plates, service cards,
  gallery, OG. Do not pad a page with generated filler to spend the budget, and do not
  starve a page that genuinely needs six images because two used to be the rule.
- **Priority order: the hero first**, then by visibility — the Planner marks every
  generated slot `GENERATE` in the plan's image list, in that order, with a running cost
  total.
- **Placeholders are still right for client-photo slots — for content reasons, not cost.**
  Slots that should carry the business's own real work (job galleries, before/after,
  team, the actual trucks) stay labeled `AI-IMAGE` placeholders for the client to fill.
  That call is about honesty and what the client will want to swap, and it survives the
  cap's removal untouched.
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
- **Client-photo slots stay labeled AI-IMAGE placeholders** — the slots whose real answer
  is the business's own job photography, which the client fills after the pitch**:**

```html
<!-- AI-IMAGE: wide drone shot of a finished bluestone paver patio at golden hour -->
<div class="img-placeholder" role="img" aria-label="Finished bluestone paver patio">
  <span>AI-IMAGE — paver patio, golden hour</span>
</div>
```

Style `.img-placeholder` as a labeled block in the art direction's colors so the
mockup still reads well. If one of those slots turns out to need a generated image rather
than one of the client's own photos, Harry can fill it from its prompt before the site
goes to the client (PLAYBOOK Part 3 Reference A) — through `/generate`, and only while the
site's all-in budget still holds. Still banned always: stock
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
- **`designed-loop`** — an abstract rendered motion object in the site's exact palette; its
  job is **brand register, not proof**, so frame-2 does not apply. Gate: **occupational fit
  — studio / tech / SaaS / premium / creative ONLY** (behind a trade, legal, or medical
  prospect it's the convention error `color-conventions.md` prevents — hard no), the moment
  needs rendered richness no free tier can fake, and it **consumes the scroll-set-piece
  slot** (mutually exclusive with a reactive field). **INVERTS the photorealism kit** — the
  CGI look is the point. ≤8s.

"It looks premium" and "the hero feels static" are not justifications in either register.

## The site budget (hard rule — everything included)

**One number per site, and it covers ALL paid generation for that site — images, video,
every retry, every tier.**

| The site ships | All-in budget |
|---|---|
| **no video** | **$1.00** |
| **a video** (either register) | **$1.50** |

This replaced the old per-register ceilings (filmed ≤$1, designed ≤$2.50) on 2026-08-04.
There is no separate image budget and no separate video budget — there is one site number,
and images spend against it first.

What that means in practice:

**The budget ends at sign-off.** It governs the build, and the Critic's spend ledger
closes when the Critic signs off. Anything generated afterwards — during the client phase,
when Harry is filling placeholder slots or acting on client feedback — is his own
deliberate spend, priced per ask (~$0.04 at 1K, ~$0.06 at 2K) and not charged against a
closed ledger. Everything else still binds there: `/generate` only, the plan's register,
no readable branding, no stock. There is no doc-enforced ceiling on the client phase
because by then a real client is paying for the site.

- **No-video build.** $1.00 buys ~16 images at 2K or ~25 at 1K. There is no count cap —
  generate what the design needs and keep the running total inside the dollar. In practice
  a strong mockup lands well under it.
- **Video build.** Images plus the clip must both fit in $1.50, and the clip is by far the
  expensive half. Budget the clip first, then spend what is left on stills — a handful of
  images (~$0.20–0.30) still leaves over $1.10 for the clip. Price the actual run before asking: if the model, resolution and
  duration you want project over the remaining headroom, the ask is over budget and the
  answer is a cheaper shape (720p instead of 1080p, 6s instead of 8s) or no clip.
- **A designed loop can no longer assume $2.50.** Whatever it costs has to land inside
  $1.50 all-in, same as a filmed clip. Register choice does not buy extra money.
- **No retries, and now it bites harder.** A failed clip has already spent the site's
  budget. Exhaust the free `ffmpeg` fixes (boomerang, crossfade, reframe — see the
  hero-video-cover recipe in `video.md`), then ship the poster still and report. A
  regeneration is a fresh ask against a budget that is already gone.
- **A free rung costs $0 and always fits.** Static depth, atmosphere, a canvas field, a
  free-licence stock clip boomeranged locally — none of these touch the budget. Most sites
  should still ship for well under $0.20.

**The budget is a ceiling, not an authorization.** $1.50 does not mean a site may have a
video; it means that IF Harry approves one, the site's total paid media may not exceed
$1.50. Video is still never pre-approved.

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


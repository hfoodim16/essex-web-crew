---
name: generate
description: Generate images and videos via AI model APIs. Triggers on /generate, generate image, generate video, create image, thumbnail, animate.
---

# /generate

## Models

| Task | Default model | Recipe |
|---|---|---|
| Image (drafts) | `nano-banana-2-lite` (Kie AI) | models/image-model.md |
| Image (shipping) | `nano-banana-2` (Kie AI) | models/image-nano-banana-2.md |
| Image (heavy type) | `fal-ai/gpt-image-2` (fal.ai) | models/image-model-pro.md |
| Video (default) | Veo 3.1 (`veo3_fast`, Kie AI) | models/video-veo-3-1.md |

Draft on lite; run **`nano-banana-2`** for anything a real customer will see. Reach for
GPT Image 2 only when the shot needs typography both Banana tiers struggle with.

Read the recipe file before every generation.

## Video model picker

Default to **Veo 3.1** (`veo3_fast` tier) for every video job unless the shot's needs
point somewhere else. Say which model ran and why in the same message as the cost
quote — even when it's the default.

| Model | Recipe | Pick it for | Watch out |
|---|---|---|---|
| Veo 3.1 | models/video-veo-3-1.md | **default.** Best prompt adherence, native audio, dialogue/lip sync, start-and-end-frame control | 4, 6 or 8 seconds only |
| Kling 3.0 | models/video-kling-3.md | 12s+ continuous takes, multi-shot sequences, character consistency, cheapest per-second drafts | motion strength can undershoot a subtle prompt — verify before delivering |
| Sora 2 | models/video-sora-2.md | hard physics, photoreal stunts, water/cloth/crowds, short-form realism | priciest; strict content filter |

Rules:

- Run Veo 3.1 `veo3_fast` by default. Only reach for Kling or Sora when the shot has
  a concrete need Veo can't cover — 12s+ continuous motion, multi-shot/character
  consistency work, or hard physics realism.
- If a shot needs more than 8 seconds continuous, Veo is out — that's Kling's lane.
  Say so instead of silently trimming my duration or silently switching models.
- Never swap the model I named. If I asked for a specific model, run that model —
  flag a better default, but wait for my go.
- **Verify motion before delivering.** Don't just report success — pull two frames
  a few seconds apart and confirm real motion happened, not a near-static clip. A job
  reporting `success` is not proof the shot did what the prompt asked.
- These three are the current roster, not the ceiling. Kie AI and fal.ai both carry
  Seedance, Wan, Hailuo/MiniMax and Runway too. If a shot suits one of those better,
  or a newer model has landed, check https://kie.ai/market and https://fal.ai/models,
  say what you found, and write a new `models/video-*.md` recipe before running it.
- **Free post-processing beats a paid re-run.** A seam-jump, loop, or crop issue is
  often fixable with a local, no-cost `ffmpeg` pass (crossfade loop, boomerang loop,
  reframe) before spending on a regenerate. Offer the free fix first.

## Provider routing

1. Default to the LOWEST COST provider that runs the model well
   (check Kie AI, fal.ai, WaveSpeed AI).
2. If the cheapest route lacks the model, fails auth, or errors,
   fall back to the next provider.
3. Never hide a provider swap. Say which route ran and why.

## Keys

Read from this file, regardless of the current working directory:

```
/Users/harryfoodim/Library/Mobile Documents/com~apple~CloudDocs/Claude Projects/Generate/.env
```

Never paste a key into code or into a message.

| Provider | Variable |
|---|---|
| Kie AI | `KIE_API_KEY` |
| fal.ai | `FAL_KEY` |
| WaveSpeed AI | `WAVESPEED_API_KEY` |

## Output

- Save every file FLAT into my generations folder:
  `/Users/harryfoodim/Library/Mobile Documents/com~apple~CloudDocs/Claude Projects/Generate/generations`
- No subfolders. Reference images live in `generations/refs/`
- Naming: `{project}_{description}_{timestamp}.{ext}` — timestamp is Unix seconds.

## Rules

- Quote the cost and wait for my explicit go before any paid
  video run. One approval = one run.
  - **Standing-authorization exception — images only.** Where I have already set a
    written, capped image budget for an automated workflow, that cap IS the approval
    for runs inside it: quote the cost, run it, report what it cost. The Essex Web
    Crew is the live case — 2 images per mockup, pre-approved (see its `CLAUDE.md`
    Image policy). **Video is never covered by a standing cap**, there or anywhere:
    every paid video run needs my explicit go for that specific clip. A run above a
    documented image cap falls back to the normal gate too — stop and ask.
- Draft on the cheap image model first. Only rerun on a quality
  model when I pick a favourite.
  - Automated workflows with a standing cap skip the draft step and go straight
    to the shipping model when their plan already specifies the shot.
- Never describe a logo or face in text. Pass the real image
  file as a reference. If it's missing, stop and ask me for it.
- Run multiple generations one at a time to avoid rate limits.
- After every save, write the sidecar log (see Logging).

## Reference images

Both Kie AI and fal.ai take reference images as **public URLs**, not local files.
A file in `generations/refs/` must be uploaded first.

Kie AI base64 upload (files auto-delete after 3 days). Real host is
`kieai.redpandaai.co`, NOT `api.kie.ai` — the docs page says `api.kie.ai` but that 404s:

```
POST https://kieai.redpandaai.co/api/file-base64-upload
Authorization: Bearer $KIE_API_KEY
Content-Type: application/json

{
  "base64Data": "data:image/png;base64,<...>",
  "uploadPath": "images/refs",
  "fileName": "logo.png"
}
```

Public URL comes back at `data.downloadUrl` (a `tempfile.redpandaai.co` link). Pass
that into `image_urls`.

Use `curl`, not Python `urllib` — this host's Cloudflare blocks urllib's default
user-agent with a 403 (`error code: 1010`). curl works fine.

## Downloading results

Result URLs expire in hours. Download immediately after the task reports success,
then save into the generations folder, then write the log.

## Logging

After every save, write a sidecar JSON next to the media: same basename, `.json`
extension. `hero_thumbnail_1774912000.jpg` gets `hero_thumbnail_1774912000.json`.

```json
{
  "model": "nano-banana-2-lite",
  "provider": "Kie AI",
  "prompt": "the full text prompt that was sent to the API",
  "refs": ["refs/logo.png", "refs/headshot.jpg"],
  "params": { "aspect_ratio": "16:9" },
  "cost_usd": 0.034,
  "created": "2026-08-01T09:41:00Z"
}
```

`created` is UTC ISO-8601. `refs` are paths relative to the generations folder.

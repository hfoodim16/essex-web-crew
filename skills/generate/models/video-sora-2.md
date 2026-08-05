# Sora 2 (OpenAI)

Strongest physics simulation and photoreal motion, with synced dialogue. Reach for it
on short-form realism: real-world stunts, water, cloth, crowds, anything where wrong
physics kills the shot. Most expensive per second of the roster.

| Field | Value |
|---|---|
| Model IDs | `sora-2-text-to-video` · `sora-2-image-to-video` · `sora-2-pro-text-to-video` · `sora-2-pro-image-to-video` · `sora-2-characters` |
| Provider | Kie AI (cheapest verified route) · fal.ai fallback (`fal-ai/sora-2/...`, roughly $0.30/s at 720p, $0.50/s at 1080p) |
| Method | Async (submit, then poll) — same `jobs/createTask` shape as Kling |
| Type | Video |
| API key | `.env` -> `KIE_API_KEY` |
| Docs | https://docs.kie.ai/market/sora2/ |
| Cost | highest of the three video models. Confirm live before quoting. |

**Verify the exact model ID on https://kie.ai/market before the first run of a session.**
The `pro` and `characters` variants are confirmed; plain text-to-video slug is inferred
from the family pattern. If `createTask` returns an unknown-model error, that is why —
read the market page, do not guess a second time.

**Paid video gate.** Quote model variant, duration, resolution and expected dollars, then
wait for an explicit go. One approval = one run. Confirm real cost afterwards from
`data.creditsConsumed`.

## Endpoint

```
POST https://api.kie.ai/api/v1/jobs/createTask
Authorization: Bearer $KIE_API_KEY
Content-Type: application/json
```

## Request format

```json
{
  "model": "sora-2-text-to-video",
  "input": {
    "prompt": "what happens in the shot, including spoken lines",
    "image_urls": [],
    "aspect_ratio": "16:9"
  }
}
```

- `prompt` — the shot. Sora rewards physical description: weight, speed, material,
  contact. Dialogue in quotes.
- `image_urls` — required for the `image-to-video` variants, public URLs only. Upload
  from `generations/refs/` first (see SKILL.md > Reference images).
- Pick the variant by job rather than passing a mode flag: `-text-to-video` vs
  `-image-to-video`, and `-pro-` for the higher-quality tier.
- `sora-2-characters` keeps a defined character consistent across shots. Use it instead
  of describing a face in text.
- Duration and resolution options are variant-specific — read the market page for the
  chosen variant rather than assuming Kling's `"3"`–`"15"` range.

## Response handling

Identical to Kling. Create-task returns `data.taskId`. Poll:

```
GET https://api.kie.ai/api/v1/jobs/recordInfo?taskId=<taskId>
Authorization: Bearer $KIE_API_KEY
```

Poll every 10 to 15 seconds. `data.state` is `waiting`, `queuing`, `generating`,
`success` or `fail`.

On `success`, `data.resultJson` is a **JSON-encoded string** — parse it, then read
`resultUrls[0]`.

On `fail`, report `data.failCode` and `data.failMsg`. A failed run may still have burned
credits — say so.

Download immediately, save flat into the generations folder, then write the sidecar log.

## Notes

- Priciest model here. Never use it for a first draft — draft on Kling, escalate to
  Sora only when I pick a favourite and the shot actually needs the physics.
- Result URLs expire within hours. Download before doing anything else.
- Never resubmit after a dead poll loop — reuse the same `taskId`.
- Sora rejects some real-person and likeness prompts upstream. If it fails on content
  grounds, report that plainly instead of retrying with softened wording.
- One video at a time. Never fan out parallel video jobs.

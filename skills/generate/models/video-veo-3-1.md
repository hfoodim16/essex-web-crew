# Veo 3.1 (Google)

**Default video model for every job unless the shot calls for something else** — see
the picker in SKILL.md. Best-in-class prompt adherence and native audio, so it also
covers dialogue, lip sync, scored soundtrack, and start-and-end-frame control.
Three tiers: `veo3` (quality), `veo3_fast`, `veo3_lite`. Default to `veo3_fast`.

| Field | Value |
|---|---|
| Model IDs | `veo3` (quality) · `veo3_fast` · `veo3_lite` |
| Provider | Kie AI (cheapest verified route — roughly 25% of Google's direct price) |
| Method | Async (submit, then poll) |
| Type | Video |
| API key | `.env` -> `KIE_API_KEY` |
| Docs | https://docs.kie.ai/veo3-api/generate-veo-3-video |
| Cost | tier and resolution dependent; 4K runs about 2x the fast rate. Confirm live before quoting. |

**Veo uses its own endpoints, NOT `jobs/createTask`.** Do not copy the Kling call shape.

**Paid video gate.** Quote model tier, duration, resolution and expected dollars, then
wait for an explicit go. One approval = one run.

## Endpoint

```
POST https://api.kie.ai/api/v1/veo/generate
Authorization: Bearer $KIE_API_KEY
Content-Type: application/json
```

## Request format

```json
{
  "prompt": "what happens in the shot, including spoken lines",
  "model": "veo3_fast",
  "generationType": "TEXT_2_VIDEO",
  "aspect_ratio": "16:9",
  "resolution": "720p",
  "duration": 8,
  "imageUrls": []
}
```

- `prompt` — required. Veo rewards detail: camera, lens, lighting, motion, audio.
  Put dialogue in quotes inside the prompt.
- `model` — `veo3` `veo3_fast` `veo3_lite`. Default `veo3_fast`. Escalate to `veo3`
  only when I pick a favourite draft.
- `generationType` —
  - `TEXT_2_VIDEO` — prompt only.
  - `FIRST_AND_LAST_FRAMES_2_VIDEO` — 1 to 2 images, start frame and optional end frame.
  - `REFERENCE_2_VIDEO` — material/reference driven. **Fast and lite models only.**
- `aspect_ratio` — `16:9` `9:16` `Auto`.
- `resolution` — `720p` `1080p` `4k`. `720p` unless I ask otherwise; 4K roughly doubles cost.
- `duration` — number, `4` `6` or `8` seconds only. Shorter than Kling — if I need
  12s+, that is a Kling job or two Veo shots.
- `imageUrls` — 1 to 3 public URLs, count depends on mode. Upload from `generations/refs/`
  first (see SKILL.md > Reference images).

Audio is native and on by default — no `sound` flag like Kling.

## Response handling

Create-task reply returns a task id, e.g. `veo_task_abcdef123456`.

Poll:

```
GET https://api.kie.ai/api/v1/veo/record-info?taskId=<taskId>
Authorization: Bearer $KIE_API_KEY
```

Poll every 10 to 15 seconds. `data.successFlag`:

| Value | Meaning |
|---|---|
| `0` | generating |
| `1` | success |
| `2` | failed |
| `3` | created, but upstream generation failed |

On `1`, the video URL is at `data.response.resultUrls[0]`. If the clip was extended,
prefer `data.response.fullResultUrls[0]`. Unlike Kling these are real arrays — no
JSON-string parsing step.

On `2` or `3`, report `data.errorCode` and `msg`. A failed run may still have burned
credits — say so.

Download immediately, save flat into the generations folder, then write the sidecar log.

## Notes

- Result URLs expire within hours. Download before doing anything else.
- Never resubmit after a dead poll loop — that double-bills. Reuse the same `taskId`.
- `REFERENCE_2_VIDEO` on `veo3` quality is rejected. Use fast or lite for that mode.
- One video at a time. Never fan out parallel video jobs.

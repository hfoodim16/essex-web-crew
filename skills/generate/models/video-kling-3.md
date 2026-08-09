# Kling 3.0

General video, cheapest per second of the roster. Best for longer takes, multi-shot
sequences, and consistent characters across shots. Text-to-video or image-to-video,
3 to 15 seconds, optional native audio.

Not the default by reflex — run the picker in SKILL.md first. Veo 3.1 wins on dialogue
and audio sync; Sora 2 wins on physics and realism.

| Field | Value |
|---|---|
| Model ID | `kling-3.0/video` |
| Provider | Kie AI |
| Method | Async (submit, then poll) |
| Type | Video |
| API key | `.env` -> `KIE_API_KEY` |
| Docs | https://docs.kie.ai/market/kling/kling-3-0 |
| Cost | roughly $0.08 to $0.17 per second depending on mode and audio |

**Paid video gate.** Quote model, duration, mode and expected dollars, then wait for an
explicit go. One approval = one run. Confirm the real cost afterwards from
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
  "model": "kling-3.0/video",
  "input": {
    "prompt": "what happens in the shot",
    "image_urls": ["https://public-url-of-start-frame.png"],
    "duration": "5",
    "aspect_ratio": "16:9",
    "mode": "std",
    "sound": false,
    "multi_shots": false
  }
}
```

- `prompt` — the shot description.
- `image_urls` — optional. Supply a start frame for image-to-video. Public URLs only.
- `duration` — string, `"3"` through `"15"`. Cost scales directly with this. Default to
  the shortest that works.
- `aspect_ratio` — `16:9` `9:16` `1:1`.
- `mode` — `std` (720p) `pro` (1080p) `4K`. `std` unless I ask otherwise.
- `sound` — boolean, native audio. Adds cost.
- `multi_shots` — boolean, multi-shot storytelling.
- `multi_prompt` — array of `{"prompt": "...", "duration": 1-12}` for per-shot control.
- `kling_elements` — array of `{"name", "description", "element_input_urls": [...]}` for
  consistent characters or objects across shots.
- `callBackUrl` — optional. Skip it; we poll instead.

## Response handling

Create-task reply:

```json
{ "code": "200", "msg": "success", "data": { "taskId": "task_kling-3.0_1765187774173" } }
```

Poll:

```
GET https://api.kie.ai/api/v1/jobs/recordInfo?taskId=<taskId>
Authorization: Bearer $KIE_API_KEY
```

Poll every 10 to 15 seconds — video is slow, be patient. `data.state` is one of
`waiting`, `queuing`, `generating`, `success`, `fail`.

On `success`, `data.resultJson` is a **JSON-encoded string** — parse it, then read
`resultUrls[0]`:

```json
"resultJson": "{\"resultUrls\":[\"https://.../generated.mp4\"]}"
```

On `fail`, read `data.failCode` and `data.failMsg` and report both. A failed run may
still have burned credits — say so.

Download the URL immediately, save flat into the generations folder, then write the
sidecar log.

## Notes

- Result URLs expire within hours. Download before doing anything else.
- Never poll a video job with a short timeout and then resubmit — that double-bills.
  If a poll loop dies, reuse the same `taskId`.
- Reference/start-frame images must be public URLs. Upload from `generations/refs/`
  first (see SKILL.md > Reference images).
- `pro` and `4K` modes and `sound: true` all raise the per-second price. Re-quote before
  switching any of them on.
- One video at a time. Never fan out parallel video jobs.

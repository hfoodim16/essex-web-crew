# Nano Banana 2 Lite

Cheap, fast everyday images. Strong with reference images. Default for all drafts.
Weak at readable text inside the image — use the pro recipe for signs, posters, UI.

| Field | Value |
|---|---|
| Model ID | `nano-banana-2-lite` (Google `gemini-3.1-flash-lite-image`) |
| Provider | Kie AI |
| Method | Async (submit, then poll) |
| Type | Image |
| API key | `.env` -> `KIE_API_KEY` |
| Docs | https://docs.kie.ai/market/google/nano-banana-2-lite |
| Cost | about $0.034 per 1K image |

## Endpoint

```
POST https://api.kie.ai/api/v1/jobs/createTask
Authorization: Bearer $KIE_API_KEY
Content-Type: application/json
```

## Request format

```json
{
  "model": "nano-banana-2-lite",
  "input": {
    "prompt": "your prompt, max 20000 chars",
    "aspect_ratio": "16:9",
    "image_urls": ["https://public-url-of-reference.png"]
  }
}
```

- `prompt` — required, max 20000 chars.
- `aspect_ratio` — one of `1:1 1:4 1:8 2:3 3:2 3:4 4:1 4:3 4:5 5:4 8:1 9:16 16:9 21:9 auto`. Default `auto`.
- `image_urls` — optional, max 10 public URLs. Local files must be uploaded first (see SKILL.md > Reference images).
- `callBackUrl` — optional. Skip it; we poll instead.

## Response handling

Create-task reply:

```json
{ "code": 200, "msg": "success", "data": { "taskId": "task_nanobanana_1765180586443" } }
```

Poll:

```
GET https://api.kie.ai/api/v1/jobs/recordInfo?taskId=<taskId>
Authorization: Bearer $KIE_API_KEY
```

Poll every 5 to 10 seconds. `data.state` is one of `waiting`, `queuing`,
`generating`, `success`, `fail`.

On `success`, `data.resultJson` is a **JSON-encoded string** — parse it, then read
`resultUrls[0]`:

```json
"resultJson": "{\"resultUrls\":[\"https://.../generated.png\"]}"
```

On `fail`, read `data.failCode` and `data.failMsg` and report both.

Download the URL immediately, save flat into the generations folder, then write the
sidecar log.

## Notes

- Result URLs expire within hours. Download before doing anything else.
- Uploaded reference files on Kie are deleted after 3 days. Re-upload from
  `generations/refs/` each session rather than reusing an old URL.
- `data.creditsConsumed` in the poll reply is the real cost. Use it in the sidecar log.
- If the API returns "model not found", the id has moved — check the docs page above
  and update this file. That is the only maintenance this recipe needs.

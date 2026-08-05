# Nano Banana 2 (full)

Client-facing images: heroes, portfolio plates, anything a real customer will see.
Same family as the lite recipe but with the quality and text rendering lite lacks —
readable text inside the image, stronger subject consistency across a set, up to 4K.

Use lite for drafts and throwaways. Use **this** for any image that ships. Use
`image-model-pro.md` (GPT Image 2) only when the shot needs heavy typographic work
lite and full both struggle with.

| Field | Value |
|---|---|
| Model ID | `nano-banana-2` (Google `gemini-3.1-flash-image`) |
| Provider | Kie AI |
| Method | Async (submit, then poll) |
| Type | Image |
| API key | `.env` -> `KIE_API_KEY` |
| Docs | https://docs.kie.ai/market/google/nano-banana-2 |
| Cost | about $0.04 per 1K, $0.06 per 2K, $0.09 per 4K (output-only pricing) |

## Endpoint

```
POST https://api.kie.ai/api/v1/jobs/createTask
Authorization: Bearer $KIE_API_KEY
Content-Type: application/json
```

## Request format

```json
{
  "model": "nano-banana-2",
  "input": {
    "prompt": "your prompt, max 20000 chars",
    "aspect_ratio": "16:9",
    "resolution": "2K",
    "image_urls": ["https://public-url-of-reference.png"]
  }
}
```

- `prompt` — required, max 20000 chars.
- `aspect_ratio` — one of `1:1 1:4 1:8 2:3 3:2 3:4 4:1 4:3 4:5 5:4 8:1 9:16 16:9 21:9 auto`. Default `auto`.
- `resolution` — `1K` `2K` `4K`. Pick it from where the image renders: `2K` for
  full-bleed and background heroes, `1K` for contained cards, plates and OG images.
  Cost scales with it — never default to 4K.
- `image_urls` — optional, max 10 public URLs. Local files must be uploaded first
  (see SKILL.md > Reference images).
- `callBackUrl` — optional. Skip it; we poll instead.

## Response handling

Identical to the lite recipe. Create-task returns `data.taskId`; poll
`GET https://api.kie.ai/api/v1/jobs/recordInfo?taskId=<taskId>` every 5 to 10 seconds
until `data.state` is `success` or `fail`. On success, `data.resultJson` is a
**JSON-encoded string** — parse it and read `resultUrls[0]`. On fail, report
`data.failCode` and `data.failMsg`.

Download the URL immediately, save flat into the generations folder, then write the
sidecar log.

## Notes

- Result URLs expire within hours. Download before doing anything else.
- Uploaded reference files on Kie are deleted after 3 days. Re-upload from
  `generations/refs/` each session rather than reusing an old URL.
- `data.creditsConsumed` is in **Kie credits, not dollars** — a 1K image came back as
  `8.0`. Log the credit figure and the dollar estimate separately; don't write credits
  into the sidecar's `cost_usd`.
- **Verified live 2026-08-02:** model id `nano-banana-2` accepted, `state: success` in
  ~24s, `resolution: "1K"` at `aspect_ratio: "16:9"` returned **1376×768 JPEG**. Results
  are served from `tempfile.aiquickdraw.com` (a different host from the upload endpoint).
  Photorealism is strong — fine surface texture, believable wear, natural light.
- Text rendering is genuinely better than lite, but still not a typesetting tool —
  for a site, real text belongs in HTML over the image, never baked into it.
- If the API returns "model not found", the id has moved — check the docs page above
  and update this file. That is the only maintenance this recipe needs.

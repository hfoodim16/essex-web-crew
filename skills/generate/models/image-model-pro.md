# GPT Image 2

Hero images and anything with readable text: signs, posters, menus, packaging, UI
mockups. Slower and pricier than the lite model. Only run after I pick a draft.

| Field | Value |
|---|---|
| Model ID | `fal-ai/gpt-image-2` (edit variant: `fal-ai/gpt-image-2/edit`) |
| Provider | fal.ai |
| Method | Sync via `fal.run`, or async via `queue.fal.run` |
| Type | Image |
| API key | `.env` -> `FAL_KEY` |
| Docs | https://fal.ai/models/fal-ai/gpt-image-2/api |
| Cost | about $0.05 per image at medium quality |

The guide lists this as `openai/gpt-image-2`. On fal the real endpoint id is
`fal-ai/gpt-image-2`. Use the `fal-ai/` form.

## Endpoint

Sync — one call, blocks until done. Use this for single images:

```
POST https://fal.run/fal-ai/gpt-image-2
Authorization: Key $FAL_KEY
Content-Type: application/json
```

Async — submit and poll. Use for batches or if sync times out:

```
POST https://queue.fal.run/fal-ai/gpt-image-2
GET  https://queue.fal.run/fal-ai/gpt-image-2/requests/{request_id}/status
GET  https://queue.fal.run/fal-ai/gpt-image-2/requests/{request_id}
```

## Request format

```json
{
  "prompt": "your prompt, min 2 chars, max 32000",
  "image_size": "landscape_16_9",
  "num_images": 1,
  "quality": "high",
  "output_format": "png"
}
```

- `prompt` — required.
- `image_size` — preset `square_hd` `square` `portrait_4_3` `portrait_16_9`
  `landscape_4_3` `landscape_16_9` `auto`, or explicit `{"width": W, "height": H}`.
  Explicit sizes: both dimensions multiples of 16, max edge 3840, aspect ratio <= 3:1,
  total pixels between 655,360 and 8,294,400. Default `landscape_4_3`.
- `num_images` — 1 to 4. Default 1. Each image bills separately.
- `quality` — `auto` `low` `medium` `high`. Default `high`. Use `medium` unless I ask
  for the top tier; `high` costs more.
- `output_format` — `jpeg` `png` `webp`. Default `png`.
- `sync_mode` — leave `false`. `true` returns a data URI instead of a URL.

### Edit variant

`POST https://fal.run/fal-ai/gpt-image-2/edit` — same fields plus:

- `image_urls` — **required**, array of public image URLs to edit from.
- `mask_url` — optional, marks the region to change.
- `image_size` defaults to `auto` here.

Required for edit: `prompt` and `image_urls`.

## Response handling

```json
{
  "images": [
    {
      "url": "https://v3b.fal.media/files/b/.../image.png",
      "width": 1024,
      "height": 1024,
      "content_type": "image/png",
      "file_name": "image.png"
    }
  ]
}
```

Read `images[0].url`. For async, poll the status URL until
`status` is `COMPLETED` (values: `IN_QUEUE`, `IN_PROGRESS`, `COMPLETED`), then GET the
result URL for the same body.

Download immediately, save flat into the generations folder, then write the sidecar log.

## Notes

- Auth header is the word `Key`, not `Bearer`. `Authorization: Key $FAL_KEY`.
- fal takes reference images as public URLs only. Upload local files from
  `generations/refs/` first (see SKILL.md > Reference images).
- Model is marked alpha by fal — the schema can change. If a field is rejected, refetch
  `https://fal.ai/api/openapi/queue/openapi.json?endpoint_id=fal-ai/gpt-image-2` and
  update this file.
- `num_images: 4` is four billed images, not four cheap variants. Ask before using it.

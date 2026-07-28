# Color conventions — occupational / industry palettes

Purpose: every industry carries a **conventional color language** people read subconsciously — blue for a dentist, navy for a law firm, red for a burger joint. The skill's job is not to blindly follow it *or* blindly break it, but to **know the convention, decide deliberately, and tell the user which choice was made and why.** Diverging silently is the mistake — a warm dentist can be great, but the user should know it broke the blue norm on purpose.

Exact palettes live in the engine: `python3 ~/.claude/skills/ui-ux-pro-max/scripts/search.py "<industry>" --domain color` (colors.csv is keyed by `Product Type` with hex + a psychology note). This file is the *map and the decision*, not a hex dump.

## Occupational color map (convention + why)

| Sector | Conventional palette | Psychology |
|--------|---------------------|------------|
| Healthcare / dental / medical | blue, teal, cyan + white; health-green | trust, cleanliness, calm, sterility, competence |
| Mental health / therapy | muted blue, sage, lavender, warm neutral | calm, safety, non-clinical warmth |
| Finance / banking / insurance | navy, deep blue, green, gold | stability, security, growth (green = money) |
| Legal / law / accounting | navy, burgundy, deep green, gold | authority, tradition, trust, gravitas |
| Food / restaurant / delivery | red, orange, warm yellow; green (fresh/organic) | appetite, energy, urgency; freshness |
| Beauty / spa / cosmetics | blush, nude, sage, cream, soft gold | calm luxury, self-care, softness |
| Eco / sustainability / agriculture / solar | green, earth browns, sky blue | nature, growth, responsibility |
| Luxury / premium / jewelry | black, gold, deep jewel tones, monochrome | exclusivity, craft, restraint |
| Tech / SaaS / fintech | trust blue (default); or vibrant gradient | reliability; or challenger-energy when broken |
| Childcare / education / kids | bright primaries, playful multicolor, warm | safety, energy, approachability |
| Fitness / gym / sports | red, orange, black, electric accents | energy, power, intensity |
| Real estate / property | navy, teal, gold, warm neutrals | trust + aspiration |
| Nonprofit / charity | blue/teal/green + one warm accent | hope, credibility, humanity |
| Home services / trades | strong primary + safety orange/red, or earthy | reliability, visibility, groundedness |

(Not exhaustive — for any sector, query `--domain color` for the engine's exact recommendation and its `Notes` rationale.)

## The honor-vs-break decision

For the brief's industry, name the convention, then choose:

**Honor the convention when:**
- The audience is risk-averse and the site's core job is **trust / recognition** — healthcare, finance, legal, insurance, childcare. People need to feel safe instantly; an unexpected palette can read as "off."
- The client is established or traditional, or the brief leads with safety, credibility, or compliance.
- The category is *not* saturated locally — looking normal-but-better beats looking different.

**Break the convention when:**
- The category is visually **saturated and samey**, and differentiation is the competitive edge. (Tend broke dental-blue for warm cream/serif and it's exactly why they stand out.)
- It's a premium or challenger repositioning, or the audience is young/design-savvy.
- The brand wants to feel like the exception, not the default.

**Always, whichever you pick:**
1. State the convention and its psychology in your report.
2. Say whether the direction **honors** or **breaks** it, and why that serves *this* brief.
3. If breaking, **keep at least one trust cue** from the category (clean whitespace, a calm secondary, legible medical-grade contrast) so you don't forfeit the category's baseline expectation. A broken convention should feel intentional, not ignorant.

## The premium-consumer trap (a convention nobody chose)

There is one palette that isn't an industry convention at all — it's an *AI* convention, and it shows up unbidden on every premium-consumer brief (cookware, wellness, artisan goods, heritage craft, DTC home, small-batch anything). It is **warm beige/cream ground + brass/clay/oxblood/ochre accent + espresso near-black text**. Reached for by default, it makes every premium brand look like the same brand.

Concretely, as *defaults*:

| Role | Overused values |
|---|---|
| Backgrounds | `#f5f1ea` `#f7f5f1` `#fbf8f1` `#efeae0` `#ece6db` `#faf7f1` `#e8dfcb` (warm paper / cream / chalk / bone) |
| Accents | `#b08947` `#b6553a` `#9a2436` `#9c6e2a` `#bc7c3a` `#7d5621` (brass / clay / oxblood / ochre) |
| Text | `#1a1714` `#1a1814` `#1b1814` (espresso / warm near-black) |

**Rotate instead.** Seven families that read as expensive without the beige reflex:

- **Cold luxury** — silver-grey, chrome, smoke
- **Forest** — deep green, bone, amber accent
- **Black and tan** — true off-black against warm tan, sharp contrast, no beige
- **Cobalt + cream** — one saturated blue against a single neutral, no brass
- **Terracotta + slate** — warm rust against cool grey
- **Olive + brick + paper** — muted olive with a brick-red accent
- **Monochrome + one pop** — off-white, off-black, one bright accent (electric blue, emerald, hot pink)

**The rotation rule:** check `design-memory.md` (Stage 4). If the last premium-consumer build used a family, this one uses a different one — the same mechanism that already bans repeat font pairings and layout archetypes.

**This is a ban on the *default*, not on the colours.** Earth tones are correct for a landscaper, warm stone for a heritage mason, cream for an actual bakery — the occupational map above outranks this section every time, and a brand brief that names these colours settles it. What's banned is arriving here because the brief said "premium" and no other decision got made. Say which it was.

## How it feeds the pipeline
- **Stage 2** captures the conventional palette + psychology (query the bare industry term).
- **Stage 5** makes the call explicit: at least one of the three directions **honors/adapts** the convention; each direction's brief states honor-or-break. The user chooses knowing the trade-off.
- **Stage 7** builds it: this file decides *which* palette, `references/color-craft.md` decides *how* — colour roles, OKLCH ramps, contrast verification, and deriving secondary text from the surface hue instead of reaching for generic grey.

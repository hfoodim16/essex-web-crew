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

## How it feeds the pipeline
- **Stage 2** captures the conventional palette + psychology (query the bare industry term).
- **Stage 5** makes the call explicit: at least one of the three directions **honors/adapts** the convention; each direction's brief states honor-or-break. The user chooses knowing the trade-off.

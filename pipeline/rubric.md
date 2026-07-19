# Candidate Scoring Rubric

The Analyst scores every candidate 0–100 using these weighted dimensions. Higher =
better prospect. All candidates must first pass the hard qualification rules in
CLAUDE.md (weak/no site + established + reachable) — the rubric ranks the ones that pass.

| # | Dimension | Weight | What earns points |
|---|-----------|--------|-------------------|
| 1 | **Website gap severity** | 30 | No site at all, or a badly broken/dated/non-responsive one. The more dramatic the before→after, the higher. A "meh but functional" site scores low here. |
| 2 | **Established-ness** | 25 | Years in business, review history, "since 20XX", strong local footprint. Signals they have budget and staying power. |
| 3 | **Static-site fit** | 20 | Their business genuinely needs only a low-maintenance brochure site (no e-commerce, no weekly-changing content, no booking engine). Perfect fit = full points. |
| 4 | **Service breadth → showcase potential** | 15 | Multiple service lines (landscaping + masonry + hardscaping) give us a richer, more impressive multi-page mockup and a bigger sale. Single-service still scores, just lower. |
| 5 | **Contactability** | 10 | Named owner + direct phone/email = full. Only a generic contact form = partial. |

**Bonus (up to +10):** strong public reviews / ratings (4.0★+ with a real volume) —
shows they invest in reputation and are likelier to pay for a better web presence.

## Scoring output

Append a `## Scoring — <date>` section to `pipeline/candidates.md`:

```
| # | Business | Gap/30 | Est/25 | Fit/20 | Breadth/15 | Contact/10 | Bonus | Total | Rank |
|---|----------|--------|--------|--------|------------|------------|-------|-------|------|
```

Then the **top 3 by total** become the finalists (ties broken toward the most dramatic
website gap on an established business).

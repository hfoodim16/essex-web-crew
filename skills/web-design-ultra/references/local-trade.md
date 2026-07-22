# Local service-business conversion patterns

For local trades — landscapers, dentists, plumbers, roofers, contractors, HVAC, cleaners. These businesses win on **trust + ease of contact**, not on being clever. The design can (and should) still be bold and distinctive per the rest of the skill — but it must nail these conversion mechanics, because a beautiful site that a 55-year-old homeowner can't figure out how to call is a failure.

The visitor is usually: on a phone, in a hurry, comparing 2–3 local options, and deciding on "do I trust these people in my home." Design for that person.

## The non-negotiable conversion elements

1. **Tap-to-call, everywhere.** The phone number is a real `tel:` link, visible in the header on mobile (a call button, not buried). Repeat the CTA at the top, mid-page, and footer. Half of local-service traffic converts by phone.
2. **One primary action, stated plainly.** "Get a free estimate" / "Book a visit" / "Call now" — not clever wordplay. The CTA says exactly what happens next.
3. **Service-area block with real town names.** List the towns/neighborhoods served ("Serving Caldwell, Cedar Grove, West Orange & Montclair"). This is both a trust signal ("they work near me") and local SEO — search engines read the town names.
4. **Trust strip near the top.** Years in business, # of jobs/homes served, license #, insured/bonded, real star rating. **License and insurance line is huge** for trades — "Licensed & insured · NJ HIC #13VH…". (Real numbers only — see honesty rule; use a labeled placeholder if you don't have them.)
5. **Before/after or real project gallery.** The single most persuasive element for trades — proof of the actual work. Design a proper gallery (grid or before/after slider), with images marked `GENERATE` or left as labeled photo slots for the client's real job photos.
6. **Reviews with attributed, real sources.** A review strip — but each quote labeled with a real source ("★★★★★ via Google") and a real first name + town. Never fabricate; placeholder if absent.
7. **Estimate form ≤ 4 fields.** Name, phone, ZIP/town, one "what do you need" line. Every extra field drops completion. Phone > email for this audience. Make it work or leave an honest "form submits to …" note.
8. **Consistent NAP in the footer.** Name, Address, Phone — identical to their Google Business Profile (consistency is a local-SEO ranking factor). Add hours and a map embed slot.

## Section order that works (adapt, don't copy)

Hero (headline + service + tap-to-call) → trust strip (years / license / rating) → services → before/after work → service-area + towns → reviews → estimate CTA → footer (NAP + hours + map).

## Built to be found — local SEO structure (ship this in every real-business mockup)

Most small-trade sites have none of this, which is exactly why they're invisible in "landscaper near me" results. It is free to include and it is a genuinely true pitch line: *"Google can't read your current site as a business — this one is built so it can."*

### 1. `LocalBusiness` JSON-LD — paste in `<head>`

Use the **most specific schema.org type** that fits, falling back as needed:
`LandscapingBusiness` · `Plumber` · `RoofingContractor` · `HVACBusiness` · `Electrician` · `HousePainter` · `Dentist` · `GeneralContractor` → fallback `HomeAndConstructionBusiness` → fallback `LocalBusiness`.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LandscapingBusiness",
  "name": "PLACEHOLDER_BUSINESS_NAME",
  "url": "https://PLACEHOLDER_DOMAIN",
  "telephone": "PLACEHOLDER_PHONE",
  "image": "https://PLACEHOLDER_DOMAIN/assets/hero.webp",
  "priceRange": "$$",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "PLACEHOLDER_STREET",
    "addressLocality": "PLACEHOLDER_TOWN",
    "addressRegion": "NJ",
    "postalCode": "PLACEHOLDER_ZIP",
    "addressCountry": "US"
  },
  "geo": { "@type": "GeoCoordinates", "latitude": "PLACEHOLDER_LAT", "longitude": "PLACEHOLDER_LNG" },
  "areaServed": [
    { "@type": "City", "name": "PLACEHOLDER_TOWN_1" },
    { "@type": "City", "name": "PLACEHOLDER_TOWN_2" },
    { "@type": "City", "name": "PLACEHOLDER_TOWN_3" }
  ],
  "openingHoursSpecification": [{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
    "opens": "PLACEHOLDER_OPEN",
    "closes": "PLACEHOLDER_CLOSE"
  }],
  "sameAs": ["PLACEHOLDER_GOOGLE_PROFILE_OR_FACEBOOK_URL"]
}
</script>
```

**Honesty rule applies fully.** Every value comes from the analyst's dossier (the client's real Google Business Profile / site). **Never invent a phone number, address, license, coordinates, or hours.** If a value isn't known, leave the `PLACEHOLDER_…` token in place — a visible placeholder is correct and expected; fabricated NAP data is a hard fail. Drop `geo` and `sameAs` entirely rather than guessing them.

### 2. Meta essentials checklist

- `<title>` = `<Service> in <Town>, <ST> | <Business>` — e.g. "Landscaping in Montclair, NJ | Cecere Brothers".
- Meta description names the service **and 2–3 real towns**.
- OG + Twitter title/description/image (the hero image), so a shared link looks legit.
- `<link rel="canonical">`, a real favicon (inline SVG is fine), `<html lang="en">`.
- One `<h1>` per page containing the service + primary town.

### 3. NAP consistency (the ranking factor people miss)

The Name / Address / Phone shown in the visible footer must match the JSON-LD **and** the client's Google Business Profile **character for character** ("St." vs "Street" matters). Same phone format everywhere, and it's a real `tel:` link.

## What kills these sites (avoid)

- A gorgeous hero with **no visible phone number**.
- Stock smiling-people photos instead of the real crew/work (reads as fake — trades buyers are skeptical).
- A contact form as the *only* path to reach them.
- Generic "we're the best / quality you can trust" copy with zero specifics (no towns, no license, no numbers).
- Fabricated reviews or an invented "since 1985." Real content only.

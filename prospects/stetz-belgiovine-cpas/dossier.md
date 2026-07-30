# Dossier — Stetz, Belgiovine, Manwarren & Wallis, P.C.

**Slug:** `stetz-belgiovine-cpas`
**Prospecting run:** 2026-07-29 · **Rank 3 of 12 · score 91/100**
**Researched by:** Analyst, with load-bearing facts verified against primary sources.

---

## Business summary

A **four-partner CPA firm in Verona**, Essex County, serving small-to-medium businesses and
individuals. The firm's own two accounts of its history differ and both are theirs:

- Its **website** says it "has been operating in its present form since **1993**."
- Its **Patch listing** says "The Firm has been in business since **1983**, and in 2011 purchased
  the building located at 155 Pompton Avenue."

These reconcile as **founded 1983, reorganized into the named partnership in 1993** — but only the
client can confirm which they want on the site. Either way this is a **43-year-old firm that owns
its own building.**

**Partners (verbatim from their contacts page):** Larry W. Stetz, CPA · Alex Belgiovine, CPA ·
Robert Manwarren, CPA · Chris Wallis, CPA — each with a direct extension.

Six described service lines: management advisory, forensic accounting, tax preparation and
compliance, litigation support, estate and retirement planning, and accounting/auditing/review/
compilation. They are members of the **NJ Society of CPAs** and the **AICPA**, and have
**successfully completed Peer Review**. They name **20 industries** they work in — a genuinely
valuable, specific asset buried on a sub-page.

They run **live, modern client infrastructure**: a **SmartVault** secure file portal and a
**CPACharge** payment page. This firm is not technophobic. Their website is just abandoned.

**Currently active.** No evidence of merger, acquisition, rename, death or departure. The only
change found is that **"Wallis" was added to the firm name** at some point and the website was never
fully updated to match.

---

## Contact — how Harry reaches them

| | |
|---|---|
| **Contact partner** | **Robert Manwarren, CPA** — direct: (973) 433-1100 **ext. 140** |
| Other partners | Larry W. Stetz **ext. 130** · Alex Belgiovine **ext. 110** · Chris Wallis **ext. 260** |
| **Phone** | **(973) 433-1100** |
| Fax | (973) 433-1111 |
| Address | **155 Pompton Ave, Suite 204, Verona, NJ 07044** — the firm owns this building |
| **Email** | **No email published in plaintext.** See below — recoverable in ~30 seconds. |
| Website | sbcpas.com (live, responsive, badly dated) |

**Harry should CALL, and he can reach a specific partner directly.** The four extensions are real
and public — that is unusually good access for a first approach. **Ext. 140 (Robert Manwarren)** is
the contact partner the scouting identified.

⚠️ **The Montclair address in the scouting notes is a FORMER office.** 45 Park St, Montclair is
pre-2011. The firm's own Patch listing states: *"Prior to moving to Verona the Firm was located in
Montclair, NJ."* I confirmed by direct fetch that the live contact page lists **only Verona, no
Montclair anywhere.** Per the currency rule this is **current fact with history noted**, not a
discrepancy. **There is no second office.** Do not mention Montclair as a location on a call.

**On the email — a 30-second job for Harry or the lead.** The site holds **four real partner email
addresses**, but they are XOR-encrypted by **Obfuscapery v1.10 (© 2011)** and only decode after
JavaScript runs *and* the visitor moves a mouse. Until then the page renders the literal text
**"Loading Email..."** — which I confirmed myself. The research subagent's sandbox blocked the two
POST requests needed to decode them headlessly.

> **To get the emails:** open `https://www.sbcpas.com/contact_us.html?id=19128` in a real browser
> and move the mouse. The four partner addresses resolve into live `mailto:` links.

**This is also a pitch point, not just an inconvenience:** because the email only appears after a
mouse move, **a visitor on a phone may never see an email address on their website at all.** That
is a live conversion bug on a professional-services site.

**Hours: published nowhere.** Not on the site, "Not provided" on Patch, "Unknown" on dotax.
`[placeholder]` — must be asked.

---

## The website gap — the pitch

**Two corrections to the scouting row first, because getting these wrong would cost Harry the call:**

1. **The site IS mobile-responsive.** It has `<meta name="viewport" content="width=device-width,
   initial-scale=1">` (I verified this myself) and ships Bootstrap 3 with a working hamburger menu.
   **Do not tell a CPA his site isn't mobile-friendly — he will check, and he'll be right.**
2. **The Montclair office closed in 2011.** See above.

**The real defects are worse than responsiveness, and they are all concrete and screenshot-able:**

- **They have no logo.** The header references `/images/logo.gif` as the logo — I downloaded it:
  **43 bytes, `GIF image data, version 89a, 1 x 1`.** It is a **1×1 transparent spacer pixel**, the
  CCH template's empty placeholder, never filled in. The visible header is the firm name in the
  template's default font.
- **The header image is a stock photo of New York City.** `/images/header.jpg`, 1900×450 — a
  night shot of the Lower Manhattan skyline with the Brooklyn Bridge, from CCH's "Arrival/blue"
  template. **A photo of Manhattan at the top of a New Jersey firm's website.**
- **No tagline, no headline, no hero.** The `<div class="container slogan">` exists in the markup
  and is **empty**.
- **The homepage has no phone number, no address, and no service list.** Its only firm-written words
  are three paragraphs of CCH boilerplate beginning *"Welcome and thank you for visiting our
  Website."*
- **The footer has no NAP and no copyright.** The element with `id="copyright"` contains exactly one
  thing: **"Designed by CCH Site Builder."** Its three columns are empty whitespace.
- **A published estate-tax rate that expired in 2001.** Their Estate Planning copy reads *"With
  Estate Tax rates reaching as high as 55%…"* — the 55% top federal rate expired in 2001 and has
  been **40% since 2013**. **Materially misleading tax information, live on a CPA firm's site.**
  This is the single strongest thing Harry can point to, because it is a professional-credibility
  problem rather than a design opinion.
- **Their copy was written around 2003.** The Firm Profile says *"Over the course of a decade…"* —
  written when the firm was ~10 years old — and has two grammatical errors in its first two
  sentences (*"it's Principals"*, and the page **calls the firm "Stetz, Belgiovine and Manwarren,
  P.C." with no Wallis** while the header says otherwise). **The site contradicts itself on its own
  name.**
- **The site hasn't been regenerated since 2024-02-17** — every asset carries the cache-buster
  `d=1708180317768` and `sitemap.xml` shows that `lastmod` on all 9 URLs.
- **Zero local SEO.** No JSON-LD, no `LocalBusiness` schema, no canonical, no Open Graph, no Twitter
  card. The `<title>` names **no service and no town**. The meta description is truncated mid-word
  at `"Our dedica"`.
- **Four typos in their own metadata:** "Certified Public **Accountanta**", "**Compliation**",
  "**Entrepenuer**", "**Finacial Statemets**".
- **Two dead federal links:** an IRS form hosted on **FedWorld** (shut down 2011) and an I-9 on
  **ins.usdoj.gov** (the INS ceased to exist in 2003). Plus "Emloyment" misspelled in the label.
- **Their only contact form is a 1990s popup** — `window.open(..., width=550, height=760,
  resizable=no)`. Popup blockers eat it and **it is unusable on a phone.**
- **The partner list is hidden behind an unstyled form button**, absent from the nav and from
  sitemap.xml — **uncrawlable.** The firm's entire team presence is invisible to Google.
- **Ancient dependencies:** jQuery **1.11.1** (May 2014), Bootstrap 3 (EOL 2019), an **IE6-era
  proprietary PNG hack** (`behavior:url("images/pngbehavior.htc")`), an IE8 conditional stylesheet,
  and a non-standard `<!DOCTYPE html SYSTEM "about:legacy-compat">`.
- **Three of eight pages are pure vendor content** — a CCH tax-news feed, ~250 CCH calculators, and
  IRS form libraries. The firm neither writes nor owns any of it. Several calculators are visibly
  stale: one computes self-employment tax **"for tax year 2019"**, another is a **1040EZ** calculator
  (form abolished after 2017).
- **No hours, no team photos, no bios, no imagery of the firm, no Google Business Profile found.**

**The irony worth naming on the call:** the newsletter feed on their site reads current to 2026,
because CCH pushes it automatically. Everything the *firm itself* wrote is frozen in 2003. The site
looks maintained and isn't.

---

## Logo

**Logo: No logo found.**

Verified three ways. (1) `https://www.sbcpas.com/images/logo.gif` — downloaded 2026-07-29:
**43 bytes, 1×1 transparent GIF.** Not a logo; the CCH template's unfilled placeholder. (2) The
visible header is a plain text wordmark: `<span class="title">Stetz,  Belgiovine, Manwarren and
Wallis, P.C. </span>` in the template default font (note the double space, as published). (3) **No
Facebook page and no LinkedIn company page exist** — only unclaimed personal profiles for Gary Stetz
and Larry Stetz, neither carrying a firm logo. A Crunchbase stub exists with no logo.

**This is the CLAUDE.md "no logo exists anywhere" case → a tasteful text wordmark in the display
face is the correct call**, and for a firm with a four-surname name that is a real typographic
opportunity rather than a consolation prize.

---

## Tagline

**They have none.** No tagline, no headline, no positioning statement anywhere on the site — the
slogan container is empty in the markup. The closest thing is **"Certified Public Accountants"**
under the firm name on the contact page.

**This is a genuine gap, not a capture failure, and it is a selling point:** the rebuild gets to
give them a headline they have never had. It also means the voice must come **entirely from their
questionnaire answers** — their existing copy is 2003 boilerplate and is a facts source only.

---

## Real reviews

### **No usable reviews found.**

Exactly one public review exists anywhere, and it fails our attribution rule twice over.

**Clutch.co — 5.0/5, 1 review**, titled "Tax Preparation & Financial Consulting for IT Company",
dated Mar 10 2020. Verbatim quotes: *"Their team's personable and knowledgeable."* · *"It's easy to
talk with them."* · *"They've been good to us, giving us referrals to other small businesses, which
has been good."*

**Two reasons it cannot ship:**
1. **The reviewer has no first name** — they are displayed only as **"CFO, Bit by Bit"**, a job
   title. Our rule requires a verbatim quote plus a reviewer first name. **Do not invent one.**
2. **Bit by Bit is not arm's length** — it is listed as a client **on the firm's own Links page**
   ("Bit by Bit Computer Consutants → bitxbit.com", under "Client Sites"). A reciprocal-link
   partner's review is weak social proof even if genuine.

**Every other platform: zero.** CPAdirectory "Based on 0 Client Reviews" · Experience.com 0 for both
Larry and Gary Stetz · Patch none · dotax none · **no BBB listing found** · **no Google Business
Profile found in any search.** Yelp is Cloudflare-blocked to free tools — a listing exists as "STETZ
BELGIOVINE & MANWARREN" and a snippet says "Updated July 2026", but no rating or count was
retrievable. `[placeholder — needs a browser check]`

**→ The mockup ships with NO testimonial section**, or a clearly-labeled `[Real review goes here —
none captured yet]` block. Never fabricated praise.

**And this is itself one of the best pitch angles:** *a 43-year-old firm with four partners has one
review on the internet, from 2020, anonymous.* They have three decades of happy clients and have
never once asked for a quote. Harry should put "any client willing to give a testimonial?" in the
questionnaire.

---

## Services (grouped)

Full descriptions with all "Our Services Include" bullets are in `site-content.md`. Their own
grouping is incoherent — three headings for six services, with four filed under **"Miscellaneous"**
— so **parity here means carrying the facts, not the structure.** Re-group it.

**Consulting**
- **Management Advisory Services (MAS)** — business plan editing, software recommendations,
  operational review, accounting-system analysis, strategic planning, information-system
  definition, merger assistance, insolvency services, valuation, financing preparation,
  merger/acquisition analysis, bookkeeper substitution, controllership activities.

**Accounting & Assurance**
- **Accounting, Auditing, Review & Compilation** — from Certified Audits for companies down to
  write-ups for "Mom and Pop" businesses; custom accounting-system design.
- **Forensic Accounting** — financial-record analysis for dispute resolution, fraud and theft
  investigation, damage measurement.

**Tax**
- **Tax Preparation and Compliance** — returns for any entity type, federal and state;
  representation before all taxing authorities; estate and gift tax returns; transaction tax
  strategy (dispositions, reorganizations, M&A, real estate).

**Planning**
- **Estate and Retirement Planning** — asset preservation, asset allocation, estate-tax reduction,
  retirement income analysis, coordination with the client's attorney.
  ⚠️ **Drop or replace the "55%" estate-tax figure** — expired 2001.

**Litigation**
- **Litigation Support** — financial data interpretation, damage-claim calculation, trial
  depositions and exhibits, expert opinion and expert-witness appearances, settlement and mediation
  assistance, business valuation.

**The 20 industries they name** — a ready-made industries grid, and the most valuable content on the
site: Automobile · Collectibles · Communications · Contractors · Distributors · Entertainment · Fast
Food Franchises · Health Care · Importers · Law Practices · Licensing · Manufacturing · Music · Not
For Profits · Professional Practices · Real Estate Developers · Restaurants · Retail · Trucking ·
Wholesale.

⚠️ **Services their own Patch listing names that the website never mentions:** **bookkeeping**,
**quarterly reports**, **financial statements**, **business valuations**. Not a contradiction — the
website is **missing services the firm actually sells.** Both lists must feed the questionnaire.

---

## Recommended page map — 6 pages

The richest content of the three finalists, and the only one where the page count is driven by
material that already exists.

| Page | Why |
|---|---|
| **1. Home** | Hero + the tagline they've never had; the service lines as cards; a trust strip (since 1983 · 4 partners · NJSCPA + AICPA · Peer Review completed); the industries strip; **real NAP and a tap-to-call**, none of which the current homepage has. |
| **2. Services** | All six lines, **re-grouped coherently** (no "Miscellaneous"), each with its full description and "Our Services Include" bullets. Their descriptions are long and substantive — parity says carry the facts. |
| **3. Industries We Serve** | The 20-industry list as its own page. It is their sharpest differentiator, it maps directly to search intent ("Verona CPA for contractors"), and it is currently buried in the last paragraph of a sub-page. |
| **4. Our Partners** | Four partners, their credentials, **their direct extensions**, and bios + headshots we request. Fixes the worst structural flaw on the current site — a team page hidden behind a form button and invisible to Google. |
| **5. Client Portal & Payments** | **Load-bearing.** SmartVault secure file transfer + CPACharge "Pay Your Bill" + the IRS refund-status link. These are live, modern, and used by real clients — they must survive the rebuild, presented properly instead of buried in a "Links" page beside two dead federal URLs. |
| **6. About & Contact** | Founding history (1983/1993 as the client prefers), NJSCPA/AICPA membership, Peer Review, the Verona office they own, hours, NAP, `LocalBusiness` JSON-LD, and a real ≤4-field contact form replacing the 550px popup. |

**Deliberately dropped** (for the Planner's content map): the CCH tax-news feed, the ~250 CCH
calculators, the IRS form/publication widgets, the QuickBooks link, and the "Links" page's dead
federal URLs. **All vendor content the firm neither owns nor writes**, some of it visibly stale. The
three load-bearing links (SmartVault, CPACharge, IRS refund status) move to page 5.

---

## Service area

**They publish none.** No service-area page, no town list, no county named anywhere on the site.
`[placeholder]`

Available material: the Verona office (155 Pompton Ave), the **Montclair history 1983–2011**, and
their own claim that *"we are able to service clients throughout the nation."* Essex County towns
are the obvious build, and **naming Montclair as a service area is worth asking about** — they were
there ~18 years and Essex County clients still search it. **A client decision, not ours.**

---

## Reputation notes

- **43 years in business** by the firm's own Patch statement (1983); 33 in its "present form" (1993).
- **They own their building** — bought 155 Pompton Ave in 2011. A strong stability signal.
- **Four partners**, all CPAs, all with direct extensions. Clutch lists 2–9 employees.
- **NJSCPA and AICPA members; Peer Review successfully completed** — real credentials, currently
  buried in the fourth paragraph of the Firm Profile.
- **Live SmartVault and CPACharge integrations** — they invest in client-facing technology.
- **Reputation footprint is almost nonexistent:** one anonymous review from 2020, no Google Business
  Profile found, no BBB listing found. Not a negative-reputation problem — an **absence** problem.

---

## Competitor references (for the Planner)

**A. Klatzkin & Company LLP — `klatzkin.com`** (Hamilton, NJ + Newtown, PA) — **the closest
structural analogue: a multi-decade NJ firm, partner-heavy, ~30 people, 90+ years.** Full-bleed
photo hero under a heavy **brand-navy overlay wash** (`rgba(21,69,118,.65)`), single centered
headline ("Our Top Priority is Your Bottom Line"), one CTA. Below it a **hairline-lattice service
grid** — 33.3% cells separated by `2px solid #fff`, reading as one divided panel rather than
floating cards. Then industries, a 4-partner leadership spotlight, an insights feed. A
**single-family weight-contrast type system** (Avenir Next Rounded Demi + Regular, self-hosted, no
Google Fonts at all). Two brand colors over a gray ramp: `#154576` navy + `#f05c32` orange.
**Four patterns worth taking:** (1) **benefit-phrased service labels instead of noun labels** —
"Accurate Financial Reporting for Targeted Decision Making" rather than "Accounting" — directly
transplantable to a firm whose cards currently say *"Miscellaneous"*; (2) the **brand-color overlay
wash**, which makes even mediocre client-supplied photography look art-directed and guarantees AA
contrast — **highly relevant, since this prospect has no photography at all**; (3) the hairline
lattice, nearly free to build; (4) **a contact form at the bottom of every service page.**
**Caveats — take the structure, not the technique:** fixed breakpoints, no `clamp()`, no CSS Grid,
**no phone number in the header**, and its homepage service cells look clickable but aren't — an
affordance flaw our own QA gate fails builds for.

**B. Lutz and Carr CPAs LLP — `lutzandcarr.com`** (New York) — 70+ years, 28 people, niched into
not-for-profits and entertainment. Full-bleed photographic hero with a **dual-entry CTA pair**
(Audit / Tax, equal weight) over the image; headline "Beyond the Numbers." Then a **client-logo
credibility band** (Lincoln Center Theater, Jazz at Lincoln Center, Apollo Theater), a rotating
"Featured Partner" spotlight, testimonials. A true display/body pairing: **Lora + Poppins**,
hierarchy from weight contrast. **A page per topic** — 2 service + 6 industry pages on SEO-shaped
slugs, each a ~180–200 word linear narrative under named subheads with sub-services woven into prose
rather than bulleted. Palette: `#3217fa` electric blue + `#ffd800` yellow + `#e83c00` orange over
neutrals — **an electric-blue/yellow CPA site is the least generic decision in this reference set.**
**Three patterns worth taking:** (1) a **"Key Contacts" block ending every service page** — two
named partners with headshot and bio link, turning an abstract service into a person you can ask
for (**perfect for a four-partner firm with four public extensions**); (2) a **client-logo proof
band instead of adjectives** — which is what this prospect's 20-industry list can become; (3) the
**dual-CTA hero that segments at the door** (Business / Individual would fit here).

---

## Art-direction hints (for the Planner — not decisions)

- **This is the one finalist where the design has to carry everything**, because there is no logo, no
  tagline, no photography, no reviews, and no faces. Type, color, layout and structure are the whole
  product. Both competitor references solve exactly this problem — Klatzkin with a color wash over
  weak photography, Lutz and Carr with an unexpected palette and a real type pairing.
- **The four-surname name is the brand.** "Stetz, Belgiovine, Manwarren & Wallis" is long,
  distinctive, and rhythmic — a wordmark opportunity, not a problem to shrink. Fix the double space.
- **Avoid the CPA defaults hard:** navy-and-gray corporate, a skyline photo, stock handshakes,
  calculators, columns, "trusted advisors since 19XX". Their current site is the *platonic* version
  of that, so anything in that register reads as a lateral move. Lutz and Carr's electric blue is
  the useful provocation here.
- **Do not put a skyline on this site.** Their current header is a stock photo of Manhattan on a New
  Jersey firm's website — replacing it with a nicer skyline would repeat the original sin. Verona /
  Essex County or nothing.
- Register: **substantive and current** — the opposite of the frozen-in-2003 feeling. Their real
  assets are longevity, four named partners with direct lines, 20 industries, and Peer Review.
- Check `design-memory.md` first: the previous run's #1 finalist was also a CPA (`john-sessa-cpa`).
  **This site must not look like a sibling of that one** — different font pairing, palette family
  and layout archetype, per the anti-repetition rule.

---

## Needed image placeholders

Two `GENERATE` slots. This prospect has **zero usable imagery** — no logo, no headshots, no office
photos — so the generated images and the CSS craft carry the visual load.

| Slot | Note |
|---|---|
| **1. Hero — `GENERATE`, 2K** | Full-bleed, and **not a skyline.** Suggest a warm, credible professional-office or Essex County main-street register — or, following Klatzkin, an abstract/architectural image under a brand-color wash so the type dominates. **No readable signage, no legible text, no invented branding.** |
| **2. Second `GENERATE`, 1K** | Planner's call — likely the Industries page or the Partners page header. **Same register as the hero**, per the one-register rule. |
| 3. Partner headshots ×4 | **`[placeholder]` — must come from the client.** Never generate faces for real people. **The highest-value questionnaire ask**, since the current site's worst structural flaw is that its four partners are invisible. |
| 4. Office exterior | AI-IMAGE placeholder, **or better — ask for a real photo of 155 Pompton Ave.** They own the building; that is a genuine trust asset. |
| 5. Industries page | AI-IMAGE placeholder, or an icon set instead — 20 industries suit icons better than photography. |

---

## Gaps to close in the questionnaire

- **Is Gary Stetz still a partner?** — the most important question. See the contradictions below.
- **1983 or 1993** — which founding year do they want published?
- **Business hours** — published absolutely nowhere.
- **Do they offer bookkeeping, quarterly reports, financial statements and business valuations?**
  Their Patch listing says yes; their website never mentions them.
- **Is Anne Murphy Mountjoy a staff member?** (listed at their suite; unconfirmed)
- **Should Montclair be named as a service area?** (18 years there; clients still search it)
- **Any client willing to give a quotable testimonial?** They have one anonymous review from 2020.
- **Include "Suite 204"?** The site omits it; every directory has it.
- **Partner credentials beyond CPA** — MST? MBA? (Gary Stetz's Prabook entry says MBA.)
- **The four partner email addresses** — decode them in a browser (see Contact).
- **Confirm NJ licensure** — `newjersey.mylicense.com/verification` is an interactive form that
  cannot be fetched. `[placeholder]` — do not publish a license number unverified.
- **The "55%" estate-tax figure must be corrected or dropped**, not carried.

---

## Contradictions found (recorded, not resolved)

1. **Founding year:** **1993** ("operating in its present form since 1993" — firm_profile.html;
   Clutch "Founded 1993") vs **1983** ("The Firm has been in business since 1983" — their own Patch
   listing). **Both are the firm's own words.**
2. **Firm name:** **"Stetz, Belgiovine, Manwarren and Wallis, P.C."** (site header, all page titles,
   Patch, CPAdirectory) vs **"Stetz, Belgiovine and Manwarren, P.C."** — **on the site's own Firm
   Profile page**, plus Yelp, Manwarren's PTIN slug, and a dotax record. **The site contradicts
   itself on its own name.** Also `P.C.` in the header vs `P. C.` on the contact page.
3. **Partner list — 4 or 5?** The contacts page lists **four**. But the site's own
   `<meta name="KEYWORDS">` names **five**, including **Gary Stetz**, who appears nowhere on the
   site. Corroborating Gary Scott Stetz Sr, CPA: the **IRS PTIN registry at the current Verona
   address**, LinkedIn ("Partner at Stetz, Belgiovine and Manwarren"), and Prabook ("cofounder",
   "managing partner … since 1993", MBA). Whether he has retired, stepped back, or is simply missing
   from a page nobody has updated since 2024 **is not resolvable from public sources.**
   → **Confirm with client.** Do not put him on the rebuild unless they say so; do not write him off
   either.
4. **Address:** **155 Pompton Ave, Verona** (the live site, verified by my own fetch) vs **45 Park
   St, Montclair** (the scouting row, YellowPages). **Resolved by the firm's own statement:**
   Montclair is pre-2011. Recorded as current fact with history noted, per the currency rule.
5. **Suite number:** omitted on the site vs **Suite 204** on Patch, CPAdirectory, PTINdirectory and
   taxrpo.
6. **Phone:** **973-433-1100** (site, Patch, all current directories) vs **(973) 655-0440** — the
   dead Montclair-era number, still on stale profiles. Use 433-1100.
7. **License state:** **NJ**, license `20CC02294700` for Larry W. Stetz (Experience.com) vs
   **"Larry Stetz — Licensed In NY"** (CPAdirectory sidebar). Both unreliable aggregators.
   **Neither goes on the site unconfirmed.**
8. **Services:** 6 named on the website vs the firm's own Patch listing naming **bookkeeping,
   quarterly reports, financial statements, business valuations** — which the website never mentions.
   **The site is missing services the firm sells.**
9. **Years in business:** 1983/1993 vs dotax's **"Less than 1 year"**, "Business Status: Unknown",
   last updated 2015. Auto-generated junk — disregard, but it is indexed.
10. **Firm shape:** a 4-partner firm vs dotax presenting it as a solo practice ("Christopher Wallis
    serves the East Coast corridor, from Maine through Florida"). AI-spun boilerplate — disregard.
11. **Other names at Suite 204** (from a by-town preparer list, unconfirmed): **Alexander Belgiovine
    Jr, CPA** (matches the firm's phone — almost certainly the site's "Alex Belgiovine"),
    **Christopher Wallis**, **Anne Murphy Mountjoy** (no phone, possible unlisted staff — confirm),
    and **Anthony M Cicitta, CPA** at a **different phone, (973) 239-3910** — probably a separate
    practice in the building the firm owns. **Do not put Cicitta on the site.**

---

## Why this client is winnable

**They have money and they spend it on the right things — just not on this.** They **own their
building**, they run **paid SmartVault and CPACharge** subscriptions, and they have four partners
billing. This is not a business deciding whether it can afford a website.

**The pitch is professional credibility, not aesthetics**, which matters with accountants. Harry
does not have to say "your site looks old." He can say: *your Estate Planning page tells clients
the estate tax reaches 55%, and that rate expired in 2001.* Then: *your About page calls the firm
"Stetz, Belgiovine and Manwarren" — Chris Wallis isn't on it.* Then: *your four partners are hidden
behind a button Google can't see.* Then: *there's a photo of Manhattan at the top of your New Jersey
firm's website.* Every one of those is a fact a CPA can verify in thirty seconds, and none of them
is a matter of taste.

**The content is already written and unusually good.** Six substantive service descriptions, full
"Our Services Include" bullets, a 20-industry list, real credentials (NJSCPA, AICPA, Peer Review
completed). We are not writing a CPA firm from scratch — we are giving 43 years of substance a
current decade. **This is the richest build of the three finalists** and the one where a 6-page
scope is easiest to justify.

**One caution for the call:** do not lead with mobile. The site is responsive and he'll know it.
Lead with the 55% estate-tax figure.

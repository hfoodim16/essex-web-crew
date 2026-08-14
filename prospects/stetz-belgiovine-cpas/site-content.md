# site-content.md — Stetz, Belgiovine, Manwarren and Wallis, P.C.

Full-text capture of the existing website. This is a **content-parity preservation
artifact**, not a summary. The new site must never know less than what is recorded here.

---

## PROVENANCE

- **Business:** Stetz, Belgiovine, Manwarren and Wallis, P.C. — Certified Public Accountants
- **Site captured:** https://www.sbcpas.com/
- **Date captured:** 2026-08-13
- **Platform:** **CCH Site Builder** (Wolters Kluwer). Confirmed from three source markers:
  - `<meta name="GENERATOR" content="Designed by CCH Site Builder">`
  - Footer text renders literally as `Designed by CCH Site Builder`
  - Template/theme querystring on every stylesheet: `?template=Arrival&colorScheme=blue&header=headers1&button=buttons1&d=1708180317768`
  (Theme name = **"Arrival"**, colour scheme **blue**.)
- **Predecessor platform:** the 1999–2000s version of this site was built by **Execusite**
  (`Designed by Execusite - http://www.execusite.com` in the 2001 Wayback capture).
- **Last template rebuild:** the cache-buster `d=1708180317768` decodes to epoch
  `1708180317` = **2024-02-17**, which matches `<lastmod>2024-02-17</lastmod>` on all nine
  sitemap URLs. The *template* was regenerated Feb 2024; the *body copy* was not (see below).
- **Age of the copy:** the Home, Firm Profile and Client Services body text is **byte-identical
  to the Wayback Machine captures of 2001 and 2005**. The prose on this site is 21–25 years old.
- **Site state:** ~9 nav pages plus a hidden contacts sub-page. Technically it is *responsive*
  (has a viewport meta tag, Bootstrap 3, a working hamburger menu) — it is NOT a
  non-mobile-friendly site and must not be described as one. What it lacks is content and
  identity: no logo (the logo file is a 1×1 transparent spacer GIF), no tagline, no hero
  message, no office hours, no NAP in the footer, no partner bios, no photography of the firm,
  no structured data, and a stock **Manhattan** skyline banner on a New Jersey firm's homepage.
- **Total pages in sitemap.xml:** 9. `robots.txt` exists but is empty (`User-agent: *` and
  nothing else).

### Page inventory captured

| # | Nav name | URL | Status |
|---|---|---|---|
| 1 | Home | https://www.sbcpas.com/ and /home.html | captured |
| 2 | Firm Profile | https://www.sbcpas.com/firm_profile.html | captured |
| 3 | Client Services | https://www.sbcpas.com/client_services.html | captured |
| 4 | Info Center | https://www.sbcpas.com/info_center.html | captured |
| 5 | Info Center → Events Calendar | https://www.sbcpas.com/info_center.html?page=1 | captured (dynamic) |
| 6 | Info Center → Federal Tax Forms & IRS Publications | https://www.sbcpas.com/info_center.html?page=7 | captured (dynamic) |
| 7 | Newsletters | https://www.sbcpas.com/newsletters.html | captured (syndicated) |
| 8 | Financial Tools | https://www.sbcpas.com/financial_tools.html | captured |
| 9 | Links | https://www.sbcpas.com/links.html | captured |
| 10 | Contact Us | https://www.sbcpas.com/contact_us.html | captured |
| 11 | **Contact Us → View Contacts (HIDDEN — not in nav, not in sitemap)** | https://www.sbcpas.com/contact_us.html?id=19128 | captured |
| 12–15 | Individual partner pages (hidden) | /contact_us.html?contact_id=47683…47686 | captured |

**No `careers.html`, `services.html`, `tax_tips.html` or `newsletter.html` exists** — all
four return HTTP 404. There is no careers page, no blog, no tax-tips page of the firm's own
authorship, and no page containing partner biographies anywhere on the site.

### Global elements present on every page

**Main navigation (exact labels, in order):**
`Home` · `Firm Profile` · `Client Services` · `Info Center` · `Newsletters` ·
`Financial Tools` · `Links` · `Contact Us`

There is **no sub-navigation** anywhere in the markup. There are no dropdowns.

**Logo area:** an `<img class="logo__img" src="images/logo.gif" alt="Logo">` — the file is a
43-byte 1×1 transparent GIF89a, i.e. nothing renders. Beside it, the firm name renders as
plain text: `Stetz,  Belgiovine, Manwarren and Wallis, P.C.` (note the double space after the
comma following "Stetz" — present in the source).

**Banner image:** `images/header.jpg`, 1900×450, 119 KB — a stock night photograph of the
**Lower Manhattan skyline with the Brooklyn Bridge**. It carries no overlay text (the
`header__img--message` div is empty).

**Slogan/tagline div:** present in markup but **completely empty** on every page. There is no
tagline anywhere on this website.

**Social media div:** present in markup (`<div id="socialMedia">`) but **completely empty** —
eight blank lines. No social links exist.

**Footer:** the footer contains a three-column row (`col-left`, `col-middle`, `col-right`) and
four footer sections — **every one of them is empty**. There is no address, no phone, no
hours, no email, no copyright year, and no navigation in the footer.

**Copyright line (the only footer text on the entire site), verbatim:**
> Designed by CCH Site Builder

**Call-to-action button, appearing on Home and Contact Us, verbatim label:**
> Message Us

It opens `content/plugins/leadgenerator.php` in a JavaScript popup window sized
`width=550,height=760`.

---

## Page: Home (https://www.sbcpas.com/ — also served at /home.html)

**Page title:** `Stetz,  Belgiovine, Manwarren and Wallis, P.C.  - Home`

**H1:** `Home`

**Meta description (verbatim, note it is truncated mid-word in the source):**
> Welcome and thank you for visiting our Website. In addition to providing you with a profile of our firm and the services we provide, this Website has been designed to become a helpful resource tool to you, our valued clients and visitors. Our dedica

**Body copy (verbatim, complete):**

> Welcome and thank you for visiting our Website. In addition to providing you with a profile of our firm and the services we provide, this Website has been designed to become a helpful resource tool to you, our valued clients and visitors. Our dedication to superior client service has brought us to the Internet as we endeavor to continue to provide the highest quality professional service and guidance.
>
> As you browse through our Website, you will see that not only have we highlighted background information on our firm and the services we provide, but have also included useful resources such as informative articles (in our Newsletter section) and interactive financial calculators (in our Financial Tools section). In addition, we have taken the time to gather many links to external Websites that we felt would be of interest to our clients and visitors (in our Internet Links section).
>
> While browsing through our Website, please feel free to contact us with any questions or comments you may have - we'd love to hear from you. We pride ourselves on being proactive and responsive to our clients' inquiries and suggestions.

**NOTE — this exact text appears in the Wayback Machine capture of 2001-04-19.** It has been
unchanged for 25 years. It says nothing about what the firm does, where it is, or who it
serves.

**Right-hand panel heading, verbatim:** `Newsletters`

That panel is an auto-scrolling ticker of **CCH-syndicated national tax headlines** — not the
firm's own writing. Six items were cycling on the date of capture (headlines reproduced in the
Newsletters page section below).

**Homepage feature box:** a `<div id="cchFeatureBox">` is populated at runtime by
`three-column.js`, which POSTs to `content/action/three_column_content.php`. A direct POST to
that endpoint returned **HTTP 404**, so the three-column feature strip appears to be
configured-but-empty. `FETCH NOTE — builder should confirm in a browser whether any
three-column feature content renders on the homepage.`

---

## Page: Firm Profile (https://www.sbcpas.com/firm_profile.html)

**Page title:** `Stetz, Belgiovine, Manwarren and Wallis, P.C. - Firm Profile`

**H1:** `Firm Profile`

**Body copy (verbatim, complete — this is the ENTIRE "about" content of the website):**

> Stetz, Belgiovine and Manwarren, P.C. has been operating in its present form since 1993 as a prolific accounting firm servicing small to medium size businesses and individuals. The firm's Senior Partner and it's Principals were formerly with a medium size accounting firm from Central New Jersey. Over the course of a decade, the firm's Principals have devoted time and effort to creating a philosophy of customized professional services specific to your needs. The firm does this by getting to know you and your business thoroughly and then devising the most cost effective solutions. This is accomplished through a team effort of intellectual ability, state of the art technology and the benefits of practical experience. The firm prides itself in being able to deliver sophisticated technical services to those who ordinarily would not have access.
>
> Our firm's success is based upon some basic concepts. We deliver high quality work expeditiously and cost effectively. If you have a problem, we will work with you to find alternatives.
>
> In the spirit of quality the firm is a member of the New Jersey Society of Certified Public Accountants and the American Institute of Certified Public Accountants. The firm has also successfully completed Peer Review.
>
> We believe in the value of relationships. We view every client relationship like a partnership, and truly believe that our success is a result of your success.
>
> We are committed to providing close, personal attention to our clients. We take pride in giving you the assurance that the personal assistance you receive comes from years of advanced training, technical experience and financial acumen. Our continual investment of time and resources in professional continuing education, state-of-the-art computer technology and extensive business relationships is indicative of our commitment to excellence.

**CRITICAL CONTENT NOTES for whoever rebuilds this:**

1. **The firm's own About page names the firm WITHOUT Wallis** — "Stetz, Belgiovine and
   Manwarren, P.C." — while the page title, nav and Contact page all say "Stetz, Belgiovine,
   Manwarren and Wallis, P.C." The About copy predates Wallis's promotion to partner and was
   never updated. Do not silently "fix" this; it must be confirmed with the client.
2. **"since 1993"** here directly conflicts with **"in business since 1983"** on the firm's
   Patch directory listing. Both strings are recorded; neither is resolved here.
3. Contains the two genuinely valuable, reusable claims on the whole site:
   **NJCPA + AICPA membership**, and **"has also successfully completed Peer Review."**
4. Grammar errors present in the source and preserved above: **"it's Principals"** (should be
   "its"), and the odd word choice **"prolific accounting firm"**.
5. This page is **byte-identical to the Wayback capture of 2005**. It is at least 21 years old.
6. There are **no partner bios, no headshots, no staff count, and no founding story** on this
   page or anywhere else on the site.

---

## Page: Client Services (https://www.sbcpas.com/client_services.html)

**Page title:** `Stetz, Belgiovine, Manwarren and Wallis, P.C. - Client Services`

**H1:** `Client Services`

**Intro copy (verbatim):**

> Our firm offers a wide range of services to our individual and business clients. Because our firm is relatively small, our clients benefit by getting personalized, quality service that is beyond comparison. Below we have listed the services that we offer to our clients along with a brief description.
>
> As the list below is by no means all-inclusive, please feel free to inquire about a service if you do not see it listed. If it is not a service we provide, we would be more than happy to refer you to a qualified professional.

**Jump-link index at top of page (two columns, exact order):**

Column 1:
- Management Advisory Services
- Forensic Accounting
- Tax Preparation And Compliance

Column 2:
- Litigation Support Services
- Estate And Retirement Planning
- Accounting, Auditing, Review & Compilation Services

The page groups these under three category headings: **`Consulting Services`**,
**`Accounting Services`**, and **`Miscellaneous`**. The grouping is lopsided and clearly
unmaintained — "Tax Preparation And Compliance", the firm's most important service, sits under
the heading **"Miscellaneous"**, and three of the six services sit under that heading with no
heading of their own. Each service is followed by a `Go To Top` link.

> **Formatting note:** the source HTML mashes bullet lists into the body paragraph using
> `·` characters and literal `<P>` tags, with runs of tabs/spaces mid-sentence. The bullets
> below have been broken out onto separate lines for legibility; **no words have been added,
> removed or reordered.**

---

### Category heading: Consulting Services

#### Service 1 of 6 — Management Advisory Services

> Stetz, Belgiovine and Manwarren uses all the benefits of its Accounting, Auditing, Computerization, Compliance Regulations, and Taxation skills to render Management Advisory Services ("MAS"). MAS is the service of rendering advice on non specific Accounting, Auditing and Taxation issues. The firm counsels you from existing knowledge about your business, the circumstances, the technical matters involved, representations, and the mutual intent of the parties involved. Stetz, Belgiovine and Manwarren acts in an Advisory Capacity to develop findings, conclusions, and recommendations for your considerations and decision making. The firm also renders Implementation Services, Transaction Services, Staff and other Support Services. MAS really allows us to give you full financial services. It allows us to interact with you. Interaction with you is the keystone of our philosophy for servicing your needs.
>
> Our Services Include:
> - Editing business plans.
> - Recommending computer software.
> - Operational review and improvement studies.
> - Analysis of an accounting system.
> - Assistance with strategic planning.
> - Defining your information system.
> - Assistance with mergers of organizations.
> - Insolvency services.
> - Valuation services.
> - Preparation of information for financing.
> - Analysis of a potential merger or acquisition.
> - Assistance in substituting for bookkeepers.
> - Assistance in controllership activities

---

### Category heading: Accounting Services

#### Service 2 of 6 — Forensic Accounting

> We use accounting and auditing skills to provide an analysis of financial records in conjunction with dispute resolutions, as well as fraud and theft investigation. Our damage measurement methods can determine the extent of financial loss and illegal accounting practices.

*(This is the shortest service description on the site — two sentences, no bullet list.)*

---

### Category heading: Miscellaneous

#### Service 3 of 6 — Tax Preparation And Compliance

> Stetz, Belgiovine and Manwarren believes that taxation is one of the largest singular expenses faced by an individual or business. The firm endorses client awareness and education regarding the seriousness of tax laws beyond the financial consequences. Tax laws are complex, confusing and ever-changing. Due to the nature of tax laws, our professionals attend many continuing professional educational courses. In addition, the firm subscribes to various comprehensive tax information services. The acquisition of current information enables the firm to keep you in compliance. The firm believes that proper "tax planning" can give rise to opportunities for savings. The objective of the firm is to minimize or defer your tax liabilities in order to foster growth and security.
>
> Our Services Include:
> - Tax return preparation for any kind of entity for Federal and State.
> - Representation before all taxing authorities.
> - Estate and gift tax return preparation.
> - Planning of tax strategies for certain transactions, i.e., business dispositions, reorganizations, mergers and acquisitions, and real estate.

---

#### Service 4 of 6 — Litigation Support Services

> Due to the litigious nature of today's society and business environment, CPAs are frequently called upon by attorneys to explain, support and document issues. Our intimate knowledge of your business enables us to assist your attorneys in developing effective strategies for you.
>
> Our Services Include:
> - Analyzing all tax records and interpreting financial data.
> - Calculation of damage claims.
> - Assistance with trial depositions.
> - Preparation of trial exhibits.
> - Rendering an expert opinion.
> - Appearances as an expert witness.
> - Assistance in settlement proceedings.
> - Business valuation services.
> - Assistance with mediation.

---

#### Service 5 of 6 — Estate And Retirement Planning

> At Stetz, Belgiovine and Manwarren one of our major concerns is assisting our clients in preserving their wealth. With Estate Tax rates reaching as high as 55%, Estate Tax planning is probably the most effective planning available. Through a series of interviews, our professionals put together a profile of your financial data and personal preferences. Recommendations are then brought forward with the objective of asset preservation, asset allocation and lowering estate taxes. After completion of the planning stages, we will assist you in communicating your goals and objectives to a qualified attorney that can draft the proper wills, trusts and other related documents.
>
> For retirement planning, our professionals acquire an understanding of your financial requirements at retirement. During this process, income tax consequences regarding the dispositions of assets, an early retirement package, social security benefits and pension distributions are explored. Through discussions and analysis of your financial position a plan is developed specifically for you to follow.

> ⚠️ **FACTUAL DEFECT — DO NOT CARRY FORWARD AS WRITTEN.** The sentence
> *"With Estate Tax rates reaching as high as 55%, Estate Tax planning is probably the most
> effective planning available"* states a **federal estate tax rate that has not existed since
> 2001.** The top federal estate tax rate is 40%. This sentence is present verbatim in the
> Wayback capture of 2005 and has never been corrected. A CPA firm publishing a tax rate that
> expired 25 years ago is the single most damaging item on this website. The **fact** must be
> re-stated correctly by the client, not copied.

---

#### Service 6 of 6 — Accounting, Auditing, Review & Compilation Services

> Stetz, Belgiovine and Manwarren the Auditing, Review and Compilation services are the foundation for what we do. The firm takes special care to make sure ample time is spent on gaining an understanding of your business and its' needs. Our basic accounting services are inclusive of designing accounting systems specific for each individual client.
>
> The firm subscribes to various reporting services and continuing professional educational courses in order to keep up to date in the ever-changing environment of accounting and auditing. The scope of the firm's services range from Certified Audits for Companies to write ups for "Mom and Pop" businesses. Regardless of level of service requested, a professional is chosen that matches with the client and the level of expertise required.
>
> The members of the firm are intimate with a number of industries including but not limited to the following: Automobile, Collectibles, Communications, Contractors, Distributors, Entertainment, Fast Food Franchises, Health Care, Importers, Law Practices, Licensing, Manufacturing, Music, Not For Profits, Professional Practices, Real Estate Developers, Restaurants, Retail, Trucking, and Wholesale.
>
> In keeping with the fast changing world of computers, the resulting technology has enabled us to efficiently and cost effectively integrate computer applications. As a result of this technology, we are able to service clients throughout the nation.

*(Grammar defects present in source and preserved: the opening sentence is broken —
"Stetz, Belgiovine and Manwarren the Auditing, Review and Compilation services are the
foundation for what we do" — and **"its' needs"** should be "its needs".)*

---

### THE COMPLETE 20-INDUSTRY LIST (extracted, in the exact order published)

This is buried in the middle of the sixth service description and appears nowhere else on the
site. It is one of the most useful pieces of content the firm owns and is currently invisible.

1. Automobile
2. Collectibles
3. Communications
4. Contractors
5. Distributors
6. Entertainment
7. Fast Food Franchises
8. Health Care
9. Importers
10. Law Practices
11. Licensing
12. Manufacturing
13. Music
14. Not For Profits
15. Professional Practices
16. Real Estate Developers
17. Restaurants
18. Retail
19. Trucking
20. Wholesale

Preamble wording, verbatim: *"The members of the firm are intimate with a number of industries
including but not limited to the following:"*
Closing claim, verbatim: *"we are able to service clients throughout the nation."*

### Service dropped since the earlier site

The 2001 Wayback capture lists a **seventh** service that no longer appears anywhere:
**`SEC Related Services`**. Confirm with the client whether this was deliberately discontinued
before deciding whether to reinstate it.

---

## Page: Info Center (https://www.sbcpas.com/info_center.html)

**Page title:** `Stetz, Belgiovine, Manwarren and Wallis, P.C. - Info Center`

**H1:** `Info Center`

The page description div is **empty**. The page consists of exactly two linked items:

**Item 1 — link label verbatim:** `Events Calendar` (→ `?page=1`)

> The interactive calendar highlights federal and state tax due dates, special firm events and other important dates that may be of interest to you. Because the calendar is continually updated, check back often to keep track of filing requirements, deadlines and other events that will help you stay current and up-to-date.

**Item 2 — link label verbatim:** `Federal Tax Forms & IRS Publications` (→ `?page=7`)

> Looking for a federal tax form? Browse this online tax forms library to find downloadable IRS forms. The forms are presented in PDF format and are acceptable for filing with the IRS. You may also choose from dozens of helpful tax publications developed by the IRS to help taxpayers have a better understanding of various tax issues. Available in PDF format, these publications are written in a plain language format geared specifically to taxpayers.

**There are no other Info Center items.** Note the numbering gap — the two items are `link_1`
and `link_7`, so the CCH template offers items 2–6 (typically Tax Rates, Due Dates, Retention
Guide, Track Your Refund, IRS Tax Forms) which this firm has **not enabled**.

### Sub-page: Info Center → Events Calendar (https://www.sbcpas.com/info_center.html?page=1)

**H1:** `Info Center`. A JavaScript-driven interactive calendar widget served by CCH. Contains
no firm-authored text. Not firm content — vendor boilerplate.

### Sub-page: Info Center → Federal Tax Forms & IRS Publications (https://www.sbcpas.com/info_center.html?page=7)

**H1:** `Info Center`
**Sub-heading verbatim:** `IRS Forms and Publications`
**Body text verbatim:** `You must have Adobe Acrobat Reader to view the selected files.`

The forms table is a DataTables widget loading from
`content/apps/lookups/irs_forms.php?country=US&lang=en`. Column headers verbatim:
`Forms` · `Revisions` · `Posted` · `Description`. While loading it displays
`Loading data from server`. Contains no firm-authored content, and still shows an
**"Adobe Reader" download badge** (`/img/get_adobe_reader.png`) — a dated artifact.

---

## Page: Newsletters (https://www.sbcpas.com/newsletters.html)

**Page title:** `Stetz, Belgiovine, Manwarren and Wallis, P.C. - Newsletters`

**H1:** `Newsletters`

**IMPORTANT — none of this page is the firm's own writing.** Every item is nationally
syndicated CCH/Wolters Kluwer tax content, automatically fed and identical across every CCH
Site Builder site. There is **no firm-authored article, blog post, or newsletter anywhere on
this website.** Carry the *capability* forward if the client wants it; there is no original
editorial content to preserve.

**Section headings verbatim:** `Tax Alerts` · `Tax Briefing(s)`

**Tax Briefings listed (verbatim, in order):**
- 2026 Post-Filing Season Update
- 2025 Tax Year-in-Review
- 2025 Year-End Tax Planning
- One Big Beautiful Bill Act (Signed Into Law July 4, 2025)

**Syndicated headlines live on the date of capture (verbatim):**
- IRS Increases Optional Standard Mileage Rate for the Remainder of 2026 (Announcement 2026-11)
- IRS Updates Premium Tax Credit Table, Required Contribution Percentage (Rev. Proc. 2026-26)
- Final Regulations on QDOTs Issued (TD 10050)
- IRS Reminds Businesses About Tax Rules for Seasonal and Part-Time Employees (Tax Tip 2026-53)
- IRS Advises Newly Married Couples to Update Tax Information Before Filing Season (Tax Tip 2026-54)
- IRS Explains Taxpayers' Right to Challenge IRS Decisions and Be Heard (Tax Tip 2026-51)
- National Taxpayer Advocate Releases FY 2027 Objectives Report to Congress (IR 2026-79)
- CT - Guidance provided on 2026 legislation that affects conformity to IRC sec. 174 and IRC sec. 174A
- NJ - Net operating loss deduction temporarily capped
- NY - Prepaid sales tax rate on cigarettes increases
- PA - Property tax and rent rebate income limits increased

**Homepage ticker headlines on the date of capture (verbatim):**
- Contributions to Trump Accounts Treated as Completed Gifts; Gift Tax Returns Not Required (Rev. Proc. 2026-25; IR 2026-80)
- Final Regulations Identify Certain Charitable Remainder Annuity Trust Transactions as Listed Transactions (T.D. 10051; IR 2026-82)
- Attorney's Fees and Costs Includable in Gross Income; FCRA's Fee-Shifting Provisions Inapplicable (Eiler, TC)
- IRS Explains How Major Life Events Can Affect Tax Filing and Withholding (Tax Tip 2026-55)
- TIGTA Issues Interim Recap Of 2026 Filing Season (TIGTA_2026_Tax_File_Recap_070726)
- Taxpayer Assistance Centers Showing Deficiencies In Services Provided (TIGTA_on_TAC_07102)

Note the state coverage skew: the syndicated feed surfaces **CT, NY and PA** items alongside
the single NJ item, on a New Jersey firm's website.

---

## Page: Financial Tools (https://www.sbcpas.com/financial_tools.html)

**Page title:** `Stetz, Belgiovine, Manwarren and Wallis, P.C. - Financial Tools`

**H1:** `Financial Tools`

**Intro copy (verbatim — one of only two places on the site with any personality):**

> Should I refinance my mortgage? How much do I need to save for my child's college education? As accounting professionals, these are some of the questions that are posed to us on a daily basis. We are providing these interactive financial calculators and other tools to assist you with some of the day-to-day questions and concerns that may arise. While these financial tools are not a substitute for financial advice from a qualified professional, they can be used as a starting point in your decision making process.

This is a CCH-supplied calculator library (~150 calculators) grouped into categories. Each
category shows a `More...` link. Categories and their complete calculator lists as published:

**Auto**
Auto Loan Early Payoff, Car Loan Calculator, Home Equity Loan vs. Auto loan, Lease vs. Buy

**Business**
Breakeven Analysis, Business Debt Consolidation Calculator, Business Valuation - Discounted Cash Flow, Cash Flow Calculator, Commercial Loan Calculator, Debt Service Coverage, Equipment Buy vs. Lease, Financial Ratios, Inventory Analysis, Like Kind Exchange, Profit Margin Calculator, Repossession of Personal Property from a Deferred Payment Sale, Repossession of Personal Property from an Installment Payment Sale, Repossession of Real Property, Working Capital Needs

**Debt and Credit Cards**
Accelerated Debt Payoff, Consolidation Loan Investment Calculator, Cost-of-Debt Calculator, Credit Card Minimum Payment Calculator, Credit Card Optimizer, Credit Card Pay Off, Home Equity Debt Consolidation, How much do you owe?, Personal Debt Consolidation, Roll-Down Your Credit Card Debt!, Snowball Debt Elimination Calculator, Student Loan Consolidation and Debt Payoff

**Insurance**
Comprehensive Life Insurance Analysis, Disability Insurance, Fixed Annuity Calculator, Health Savings Account (HSA) Contribution Calculator, Health Savings Account (HSA) Goal Calculator, Health Savings Account (HSA) Savings Calculator, Health Savings Account (HSA) vs. Traditional Health Plan, Health Savings Accounts (HSA) Employer Benefit, Human Life Value, Immediate Annuity Calculator, Life Insurance Calculator, Long Term Care Calculator, Variable Annuity Calculator

**Investment**
Annual Rate of Return Calculator, Annual Stock Option Grants, Asset Allocation Calculator, Compare Investment Fees, Future Contracts Calculator, Internal Rate of Return (IRR) Calculator, Investment Distributions, Investment Goal, Investment Loan, Investment Property Calculator, Investment Returns, Investment Savings and Distributions, Lump Sum Annual Return Calculator, Lump Sum Future Value Calculator, Lump Sum Present Value Calculator, Municipal Bond Tax Equivalent Yield, Mutual Fund Expense Calculator, Personal Economic Recovery Calculator, Present Value Calculator, Present Value Goal Calculator, Stock Option Calculator, Taxable vs. Tax Deferred Investments, Taxable vs. Tax Deferred vs. Tax Free Investment

**Loan**
Alternative Payment Frequencies, Amortizing Loan Calculator, Balloon Loan Calculator, Debt Consolidation Calculator, Enhanced Loan Calculator, Equity Line of Credit Payments, Existing Loan Calculator, Home Equity Line of Credit Calculator, Line of Credit Payoff, Loan & Credit Line Payment, Loan & Credit Line Tax Savings, Loan Comparison Calculator, Loan Prequalification Calculator

**Mortgage**
Adjustable Rate Mortgage Calculator, APR Calculator for Adjustable Rate Mortgages, ARM & Interest Only ARM vs. Fixed Rate Mortgage, Balloon Mortgages, Bi-weekly Payment Calculator, Blended Rate Mortgage Calculator, FHA Maximum Financing Calculator, Fixed Rate Mortgage vs. LIBOR ARM, Interest Only ARM Calculator, Interest Only Mortgage Calculator, Maximum Mortgage, Mortgage APR Calculator, Mortgage Comparison: 15 Years vs. 30 Years, Mortgage Debt Consolidation, Mortgage Loan Calculator, Mortgage Loan Calculator (PITI), Mortgage Payoff, Mortgage Points Calculator, Mortgage Qualifier, Mortgage Refinance Break Even, Mortgage Required Income, Mortgage Tax Savings Calculator, Option ARM vs. Fixed Rate Mortgage, Refinance Interest Savings, Rent vs. Buy

*(The page continues with further categories — typically Paycheck/Payroll, Retirement, Savings,
Tax and Qualified Plans — rendered by the same CCH widget. `FETCH NOTE — the remaining
categories are below the captured region of an 89 KB page; if the rebuild reproduces the
calculator library, pull the full category list from the live page. Note also the dated
reference to **"Fixed Rate Mortgage vs. LIBOR ARM"** — LIBOR was retired in 2023.)*

---

## Page: Links (https://www.sbcpas.com/links.html)

**Page title:** `Stetz, Belgiovine, Manwarren and Wallis, P.C. - Links`

**H1:** `Links`

**Intro copy (verbatim):**

> There are many great sites on the World Wide Web but trying to actually find those great sites can be a frustrating experience. We have compiled a list of Websites that we have found to be helpful resources of information. When you click on a link, a new window will pop up. Close the window when you are ready to return to this page.

*(Note the dated register: "the World Wide Web", "a new window will pop up".)*

### Section heading: `Others`

**`Pay Your Bill`** → https://secure.cpacharge.com/pages/sbcpas/payments
*(no description)* — **This is a genuinely important, live business function: the firm's
CPACharge online payment portal. It is buried at the bottom of a "Links" page with no label
explaining what it is.**

**`Check IRS Refund Status`** → https://sa2.www4.irs.gov/irfof/lang/en/irfofgetstatus.jsp
> Track your tax return through the IRS website.

**`SBCPAS - Secure File Transfer`** → https://sbcpas.smartvault.com/
> Please click this link to transfer files (encypted) to our firm.

*(Typo in source preserved: **"encypted"**. This is the firm's **SmartVault client portal** —
verified live, redirects to a SmartVault sign-in page. Another critical business function
hidden on a Links page.)*

### Section heading: `Internet Resource`

**`Quickbooks Web Site`** → http://quickbooks.com
> QuickBooks is a fast, easy way to manage your business finances.QuickBooks is also simple to learn and customizable to your business. That's why it is the #1 best selling accounting software.

*(Missing space after "finances." preserved from source.)*

### Section heading: `Tax`

**`The Internal Revenue Service`** → http://www.irs.gov
> Home of the IRS on the Web.  The IRS has definitely done a nice job on their Website.

**`Form - SS4 Application for ID Number`** → http://www.irs.gov/pub/irs-pdf/fss4.pdf
> Download Form SS4 From IRS Web Site
>
> Adobe Acrobat Required

**`Form - 2848 Power of Attorney`** → http://ftp.fedworld.gov/pub/irs-pdf/f2848.pdf
> Download Form 2848 From the IRS Web site
>
> Adobe Acrobat Required

> ⚠️ **DEAD LINK — `ftp.fedworld.gov` does not resolve in DNS.** FedWorld was decommissioned
> by NTIS in 2014. Current URL should be https://www.irs.gov/pub/irs-pdf/f2848.pdf

**`Form - I9 Emloyment Eligibility Verification`** → http://www.ins.usdoj.gov/graphics/formsfee/forms/files/i-9.pdf
*(no description; typo in link label preserved: **"Emloyment"**)*

> ⚠️ **DEAD LINK — `www.ins.usdoj.gov` does not resolve in DNS.** The INS ceased to exist on
> 2003-03-01 when it was absorbed into DHS/USCIS. Current URL should be
> https://www.uscis.gov/i-9

### Section heading: `Client Sites`

**`Bit by Bit Computer Consutants`** → http://bitxbit.com
> Bit by Bit has been in the business of providing technology solutions to companies in and around the Tri-State area. Our clients tell us that the solutions we provide allow them to experience better productivity, enhanced communications with their customers and most importantly, a significant increase in the bottom line.

*(Typo in link label preserved: **"Consutants"**. Link verified live. Note the description is
written in **Bit by Bit's own first person** — "Our clients tell us…" — pasted unedited onto
the CPA firm's website, so on this page "our clients" refers to a different company's clients.
This is a **reciprocal link with a named client**, which is a client-confidentiality question
worth raising with the firm.)*

**Link-page defect summary:** 8 outbound links, of which **2 are dead federal government
hosts**, 1 links to a client by name, and 2 are critical firm services (payments portal,
document portal) that belong in the primary navigation, not here.

---

## Page: Contact Us (https://www.sbcpas.com/contact_us.html)

**Page title:** `Stetz, Belgiovine, Manwarren and Wallis, P.C. - Contact Us`

**H1:** `Contact Us`

**Heading block (verbatim, as styled on the page):**

> **Stetz, Belgiovine, Manwarren and Wallis, P. C.**
> Certified Public Accountants

*(Note: renders as "P. C." with a space here, versus "P.C." in the page title and nav.)*

**Contact block (verbatim, complete):**

> **United States**
> 155 Pompton Ave
> Verona, NJ 07044
> Phone : 973-433-1100
> Fax : 973-433-1111
> Email **Loading Email...**

**Buttons on the page (exact labels):** `Message Us` · `View Contacts` · `Get Directions`

**Notes for the rebuild:**

1. **`Loading Email...` is what a real visitor sees.** The email address is hidden behind the
   *Obfuscapery v1.10* anti-spam script, which only reveals the address after a **mouse-move
   event**. On a phone or tablet — where a large share of visitors are — the literal text
   **"Loading Email..."** is the firm's published email address. The recovered address is
   **alex@sbcpas.com**.
2. **No suite number.** The site says "155 Pompton Ave"; the firm's Patch listing and multiple
   directories say **"155 Pompton Avenue, Suite 204"**. Confirm with the client.
3. **No office hours are published anywhere on this website.**
4. **The address is not a link** and there is no embedded map — just a "Get Directions" form
   that POSTs to Google Maps with `daddr=155+Pompton+Ave,+Verona,+NJ,+07044`.
5. **There is no contact form on the page.** The only form is the `Message Us` button, which
   opens `content/plugins/leadgenerator.php` in a **550×760 JavaScript popup window** — a
   pattern modern browsers and mobile devices frequently block outright.
6. The heading says "United States", implying a multi-office template the firm never used.

---

## Page: Contact Us → View Contacts (https://www.sbcpas.com/contact_us.html?id=19128)

> **HIDDEN PAGE.** Not in the main navigation and not in `sitemap.xml`. It is reachable only by
> clicking the `View Contacts` button on the Contact page, which submits a GET form. **This is
> the only page on the entire website that names the partners.**

**Page title:** `Stetz, Belgiovine, Manwarren and Wallis, P.C. - Contact Us`

**H1:** `Contact Us`

**Heading block:** same as Contact Us — *Stetz, Belgiovine, Manwarren and Wallis, P. C. /
Certified Public Accountants*

**Complete partner roster (verbatim, in the exact order published):**

| Name as published | Credential | Title | Phone | Email (recovered) |
|---|---|---|---|---|
| `Larry  W. Stetz` | `, CPA` | `Partner` | 973-433-1100 ext. 130 | Larry@sbcpas.com |
| `Alex Belgiovine` | `, CPA` | `Partner` | 973-433-1100 ext. 110 | Alex@sbcpas.com |
| `Robert Manwarren` | `, CPA` | `Partner` | 973-433-1100 ext. 140 | Bob@sbcpas.com |
| `Chris Wallis` | `, CPA` | `Partner` | 973-433-1100 ext. 260 | Chris@sbcpas.com |

*(The double space in `Larry  W. Stetz` is present in the source.)*

Each name links to its own page (`?contact_id=47683` / `47684` / `47685` / `47686`).

### Individual partner pages — Larry W. Stetz (47683), Alex Belgiovine (47684), Robert Manwarren (47685), Chris Wallis (47686)

**Page title on all four:** `Stetz, Belgiovine, Manwarren and Wallis, P.C. - Contact Us`
**H1 on all four:** `Contact Us`

**⚠️ CRITICAL FINDING — THERE ARE NO PARTNER BIOS ON THIS WEBSITE.**

Each individual partner page contains **only** the following, and nothing else:

> **[Name]**, CPA
> Partner
> Phone : 973-433-1100 ext. [NNN]
>
> Email: **Loading Email...**

No biography. No headshot or photograph of any kind. No years of experience, no education, no
specialisation, no university, no professional memberships, no license number, no personal
detail. Four partners in a relationship-driven profession, and a prospective client cannot
learn a single thing about any of them.

The only credential published for any partner is **`CPA`**. No MST, MBA, CFE, CVA, PFS or any
other designation appears anywhere on the site for anyone.

**Every one of the five email addresses on this site is hidden behind the `Loading Email...`
obfuscation script.** Recovered addresses (all confirmed as the same scheme in use since at
least 2001): `alex@sbcpas.com` (general), `Larry@sbcpas.com`, `Alex@sbcpas.com`,
`Bob@sbcpas.com`, `Chris@sbcpas.com`.

---

## PAGES / CONTENT THAT DO NOT EXIST ON THIS SITE

Recording absence explicitly, because the rebuild's job is largely to fill these:

- **No partner or staff biographies** (confirmed above)
- **No photographs of the firm, the office, the building, or any person** — the only two
  images on the entire site are a broken 1×1 spacer "logo" and a stock Manhattan skyline
- **No logo or wordmark of any kind**
- **No tagline or positioning line**
- **No office hours**
- **No careers/employment page** (`careers.html` → 404)
- **No firm-authored articles, blog, or tax tips** (`tax_tips.html` → 404; the Newsletters page
  is 100% syndicated vendor content)
- **No testimonials or reviews section**
- **No client logos, industry badges, AICPA/NJCPA marks, or any visual proof**
- **No pricing or engagement information**
- **No FAQ**
- **No privacy policy, terms of use, accessibility statement, or any legal page**
- **No favicon** (`/favicon.ico` returns 404 despite being referenced in every page's `<head>`)
- **No service-area / towns-served content** — the site never names Verona, Essex County, or
  any New Jersey town outside of the postal address, while simultaneously claiming national reach
- **No footer content whatsoever** beyond "Designed by CCH Site Builder"

## TECHNICAL NOTES (carried for the rebuild)

- **Responsive: YES.** `<meta name="viewport" content="width=device-width, initial-scale=1">`
  is present, Bootstrap 3 is loaded, and a standard `navbar-toggle` hamburger with three
  `icon-bar` spans is wired via `data-toggle="collapse"` to `#navbar--collapse`.
  **Do not tell this client their site is not mobile-friendly — it is.** The failure is
  content and identity, not responsiveness.
- jQuery **1.11.1** loaded from Google's CDN (released 2014). A second, conditional loader
  pulls jQuery **3.5.1** from cchwebsites.com only if the first failed — two jQuery versions
  configured on one page.
- An **IE6-era PNG transparency hack** ships in an inline `<style>` on every page:
  `img { behavior:url("images/pngbehavior.htc"); }` — a proprietary Microsoft `behavior`
  property, plus an `<!--[if lt IE 9]>` conditional stylesheet for IE8.
- **No JSON-LD / structured data. No `AccountingService` or `LocalBusiness` schema.**
- **No OpenGraph or Twitter Card tags.** The only social-share hint is a legacy
  `<link rel="image_src" href="http://www.sbcpas.com/images/logo.gif" />` — which points at
  the 1×1 transparent spacer, so any shared link previews as blank. Note it is also
  hard-coded **`http://`** on an HTTPS site.
- **No canonical tag.** The homepage is reachable at `/`, `/home.html` and `/index` — and
  `sitemap.xml` lists both `https://www.sbcpas.com` and `https://www.sbcpas.com/home.html` as
  separate URLs, actively instructing search engines to index duplicate content.
- **Meta keywords tag** (deprecated since ~2009) is present and contains **four misspellings**
  plus a partner who is not listed on the site — reproduced verbatim in the research report.
- `robots.txt` exists but contains only `User-agent: *` with no directives.
- reCAPTCHA is loaded on the homepage (`https://www.google.com/recaptcha/api.js`) for the lead
  generator popup.
- All body copy is served from CCH's hosted platform; the firm does not appear to control the
  template.

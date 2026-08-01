# Client answers — Jets Site Sample (New York Jets)

Source: `~/Desktop/JETS Q.pdf`, the standing Website Questionnaire, filled in by the client.
Saved verbatim by the lead. **This file is the top authority for everything downstream.**
Raw text extraction kept alongside as `questionnaire-raw-extract.txt`.

- **Business name (header field):** New York Jets
- **Current website (header field):** *(left blank)*

---

## About your business

**1. What's the business name, exactly as it should appear on the site?**
> New York Jets

**2. How long have you been operating, and what's the short story?**
> 56 years. As a kid I always wanted — I always wanted to own an NFL team. After working in
> finance, I had the money to finally fulfill that goal.

**3. What makes you different from the other guys?**
> I am willing to eat losses in order for the team to be better.

**4. Which towns or areas do you serve?**
> Wherever the fans are

## What the site should do

**5. What do you want the website to do for you?**
> Make it easy for fans to find tickets, give background, showcase our players and charity.
> Look professional and like the best team in the NFL

**6. Who are your best customers?**
> My best customers are season-ticket holders. Families that have supported the team for years.

**7. How do most customers find you today?**
> TV, ticketmaster, stubhub, and other ticket platofrms. Social media is always posting us.

## Your services

**8. List everything you offer, even the small stuff.**
> Pre-season tickets, free access to training camp, ticket packages for 3 games or full season.

**9. Which 3 to 5 services matter most, in order?**
> Serving the fans what they cheer for, winning super bowls, and being the best.

**10. Is there anything you're phasing out or don't want advertised?**
> Do not advertise negative media or past coaches.

**11. Any specials, discounts, or seasonal offers worth showing?**
> *(blank)*

## Your current site

*(Client left the whole section blank — treated as "no current site to work from.")*

**12. What do you like about your current site?** — *(blank)*
**13. What bugs you about it?** — *(blank)*
**14. Is there anything on it that must be kept word-for-word?** — *(blank)*

## Look and feel

**15. Pick around 5 words for how the site should come across.**
> Professional, athletic, and large

**16. How do you talk with customers: casual, like a text message, or more buttoned-up? Is there
anything a website could say that just wouldn't sound like you?**
> Through our support team in HR.

**17. Any websites you like the look of?**
> *(blank)*

**18. Any colors you want, or definitely don't want?**
> Our team colors are green and white

**19. Your logo and colors: keep what you've got, or is this a fresh start?**
> We have a NY Jets logo out there

## Photos and proof

**20. What photos of your work do you have?**
> New York Jets

**21. Anything you'd want photographed that you don't have pictures of yet?**
> The locker room and insanely modern training facility

**22. Any reviews or testimonials you're proud of?**
> *(blank)*

**23. Licenses, certifications, insurance, memberships, awards: what should we show off?**
> Super bowl winner 1969

## How customers reach you

**24. When someone's ready to hire you, what should they do: call, text, fill out a form, book
online? (What do you actually prefer?)**
> Go to ticketmaster

**25. Which phone number and email should appear on the site? Hours, plus an emergency or
after-hours line?**
> The ticket team

**26. Should the site show your physical address, or just the areas you serve?**
> No

## The details

**27. What questions do customers always ask you?** — *(blank)*
**28. Any policies or fine print the site should state?** — *(blank)*
**29. Is there anything you do not want on the website?** — *(blank)*
**30. Do you already own a website address (domain name)? If so, what is it?** — *(blank)*

---

## Lead's notes for the build (binding constraints, not new facts)

1. **This is a SAMPLE build** — internal demonstration named "Jets site sample". Nothing here
   goes to a real client and nothing gets published live.
2. **No fabricated facts.** The answers are thin on contact detail. Everything the client did not
   supply ships as a visible `PLACEHOLDER_…` token or is written around — never invented:
   - **No phone number, no email, no hours, no address.** Q25 gives only "The ticket team";
     Q26 says do not show an address. So: `PLACEHOLDER_TICKET_LINE` / `PLACEHOLDER_TICKET_EMAIL`
     in the NAP slot, and the JSON-LD carries the same tokens. Do NOT look up a real Jets
     phone number, address, or MetLife Stadium — the client said no address.
   - **No testimonials** (Q22 blank) → the mockup has no testimonial section, or a clearly
     labeled `[Real review goes here — none captured yet]` block.
   - **No roster names, no stats, no schedule, no scores, no charity program names, no coach or
     player names** — none of that is in the answers, and rosters/schedules are exactly the
     churning content our static model excludes. Player and charity sections are structured,
     labeled placeholder blocks the client fills in.
   - The only hard facts available: name, "56 years", the owner's finance-to-ownership story,
     "willing to eat losses so the team is better", the offering list from Q8, "Super bowl
     winner 1969", green and white, "wherever the fans are".
3. **Primary action = tickets.** Q24: "Go to ticketmaster." The primary CTA everywhere is a
   ticket link — ship it as `href="PLACEHOLDER_TICKET_URL"` styled as the live button. Because
   there is no phone number, the `local-trade.md` tap-to-call requirement is satisfied by the
   ticket CTA in its place (mobile header + top/mid/footer), and the exception is written into
   `website-plan.md`.
4. **Logo — use the REAL New York Jets logo.** (Harry, 2026-07-31: "use the real Jets logo, it's
   just a sample." This is an internal sample that is never published, so the normal
   third-party-trademark caution is waived by the lead.) Per the playbook's logo rule the file is
   downloaded and served **locally** from `mockup/assets/` — never hotlinked, never redrawn,
   never "improved", and never replaced with a text wordmark. Alt text: `New York Jets logo`.
   Placed top-left in the header.
5. **Q10 is a hard exclusion:** nothing about negative media, and no past coaches anywhere on
   the site.
6. **Voice:** Q16 says communication runs "through our support team in HR" — buttoned-up,
   organizational, not a chatty owner voice. But Q2/Q3 are the owner talking plainly ("I am
   willing to eat losses in order for the team to be better") — that's the phrase to build the
   difference section on, in his words.
7. **Confirm with client (optional):** "56 years" vs. the franchise's own founding date; the
   client's number is what the site uses.

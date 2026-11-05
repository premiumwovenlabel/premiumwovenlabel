# Premium Woven Labels: STATUS

Last updated: 5 Nov 2026. Build: `premium-woven-labels-2026-11-05.zip`.

Read this first in a new chat, together with `README.md` (build and deploy steps).
Everything below is already public on the site or in the site's code. No private business details here.

## Last done (5 Nov 2026)
- Footer on every page except the ad landing page: Facebook and LinkedIn icons added next to
  WhatsApp, Instagram, Pinterest and email; "Review us on Google" link in the Contact column.
- Home page: "Leave us a Google review" prompt under the client quotes; "Facebook page" in the
  first client quote now links to the page.
- Hidden profile list (`sameAs`) and `llms.txt` name all four profiles. The review link is never
  used in structured data.
- `robots.txt` disallows `/STATUS.md` and `/README.md`.
- `audit.py` now checks the four profile links, the review link and `sameAs` on every footer page.

## Accounts and tools
- Instagram `@premium_woven_labels`, Pinterest `premiumwovenlabel`, Facebook `PremiumWovenLabels`,
  LinkedIn `company/premium-woven-label`. All links are constants at the top of `_src/core.py`.
- Google Business Profile: 5.0 from 7 ratings. Its name there is "Premium Woven Label" (singular).
- GA4 `G-NKS0Z56VJE` (key event: `whatsapp_click`). Search Console and Bing Webmaster Tools verified.

## Business facts (as published)
- Karachi, Pakistan. WhatsApp +92 304 8095202, premiumwovenlabel@gmail.com.
  Site hours: Mon to Sat, 9 am to 6 pm PKT.
- Minimum order: 100 pieces for apparel labels (starter quantities 100, 300, 500), 200 pieces for
  school monograms.
- Timing: production 3 calendar days after the final design, size and 50% advance. Delivery 2 days
  in Pakistan. After order confirmation: 5 to 6 days in total to Pakistan, 6 to 7 days to GCC.
- Samples: a digital file of the design, paid, approved before the order is confirmed. Design changes
  are free at the digital stage and paid once the label is made.
- Payment: 50% advance, the remaining 50% before dispatch. Pakistan: bank transfer, EasyPaisa or
  JazzCash; the rest before dispatch, or cash on delivery where offered. Outside Pakistan: Payoneer,
  money exchange or bank transfer; the customer sees the finished labels, pays the remaining 50%,
  then the order is dispatched.
- Included in the quote: artwork cleanup, packaging, and shipping to Pakistan and the GCC (UAE, Saudi
  Arabia, Kuwait, Qatar, Bahrain, Oman). Rest of world, UK and USA: shipping cost and delivery time
  are confirmed in the quote. UAE parcels go by Skynet Worldwide Express.
- Cancellation: before production starts only the design payment is deducted; once production has
  started the labels must be paid for. Short quantity: orders include a few extra labels, and any
  shortfall is added to the next order. Rush orders: message on WhatsApp with the time and quantity.
- Products: Damask, Satin and Taffeta weaves. 6 thread colours work in one label. Monograms come with
  adhesive backing (press to stick) or without (stitch on). Hang tags are hard tags, not woven.
  Splitting the 1,000 MOQ across designs costs extra.
- Not offered or claimed: direct embroidery on garments, certifications of any kind.
- Target traffic: USA, UK and GCC (especially UAE), not India.

## Decisions (do not re-ask)
- No prices anywhere until the owner supplies numbers.
- No star ratings or review markup, and no Product/Offer schema (it caused Search Console "Product
  snippets" errors; the audit blocks it). Google reviews appear as a plain link plus quotes shown with
  the client's name.
- No hero animation. `llms.txt` and schema stay as they are: Google says AI search needs no special markup.
- The Google Business Profile name is left as is (changing a verified name can trigger re-verification).
  The site declares "Premium Woven Label" as an alternate name.

## Pending (batch; build only after the owner says "abhi karo")
1. Real factory answers in the owner's words: the 5 questions customers ask most on WhatsApp, with the
   owner's own answers (a voice note is fine). Becomes an expert Q&A section. No numbers are invented.
2. Replace the generic "Why Premium Woven Labels" block with real facts.
3. UAE proof: Google reviews from UAE clients, and one short real order story with the client's permission.
4. About page: owner name and a few lines in the owner's own words (needs the owner's OK).
5. Proposed earlier, answer not recorded: question-style headings on /pricing/, an indexable
   "Custom Woven Labels in Pakistan" page, a "How can I create a woven label" heading on How It Works.
6. Owner tasks after deploy: run PageSpeed Insights (Mobile) and share the score; re-run the Semrush
   Site Audit; optionally change the LinkedIn page name to "Premium Woven Labels".
7. Skipped for now: the 16th home-page marquee image (Arabic script) has no known brand name.

## Latest check (5 Nov 2026)
- Google's AI Overview names the site for "custom woven labels minimum order 100 pieces" and shows
  the site's own result below it.
- The site does not appear for "best woven label maker for a small clothing brand in UAE"; UAE-based
  makers fill those results. Aim at "minimum 100 pieces", "made in Pakistan", "ships to UAE" instead.
- ChatGPT and Perplexity did not find the Google rating; only the site's own quotes.

## Open question
Google Business Profile says "Open 24 hours" but the site says Mon to Sat, 9 am to 6 pm PKT.
Which is right? Suggested answer: Mon to Sat, 9 am to 6 pm, and set the profile to match.

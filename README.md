# Premium Woven Labels — website

Static, dependency-free website for Premium Woven Labels (Karachi, Pakistan). Built as plain
HTML + CSS + vanilla JS so it runs on GitHub Pages with no build step on the server.

- 22 pages, clean URLs (`/about/`, `/woven-labels/`, `/resources/...`)
- No frameworks, no jQuery, no external JS. Only Google Fonts is loaded remotely, non-blocking.
- All label artwork is inline SVG generated at build time — the site makes **zero image requests**
  on page load (the only image files are the favicon, apple-touch-icon and the social share card).
- WhatsApp is the primary conversion path throughout.

---

## 1. Deploy to GitHub Pages

Upload **everything except `_src/`, `build.py` and this README** to the repo root (uploading them
too is harmless — `robots.txt` disallows `/_src/` and Pages ignores them).

1. Push the files to your repository.
2. Repo → **Settings → Pages** → Source: *Deploy from a branch* → Branch: `main`, folder: `/ (root)`.
3. Save. The site goes live in a minute or two.

`.nojekyll` is included so GitHub serves the files as-is. Do not delete it.

---

## 2. Moving to a .com domain

Every internal link in the site is **relative**, so the pages work at both
`username.github.io/repo/` and at a root domain without any changes.

The only place the full URL appears is in canonical tags, Open Graph tags, JSON-LD, `sitemap.xml`
and `llms.txt`. To update those:

1. Open `_src/core.py`
2. Change one line:

   ```python
   BASE = "https://premiumwovenlabel.github.io/premiumwovenlabel"
   ```
   to, for example:
   ```python
   BASE = "https://premiumwovenlabels.com"
   ```
   (no trailing slash)

3. Run `python3 build.py` from the project folder and re-upload.

Then add a `CNAME` file containing your domain, and point the domain's DNS at GitHub Pages.

---

## 3. Rebuilding

```bash
python3 build.py          # regenerates every page, sitemap.xml, robots.txt, llms.txt
python3 _src/audit.py     # link / SEO / heading / accessibility / schema check — should print 0 and 0
```

Requires Python 3 only. Pillow is used once to generate `assets/img/og-cover.png`; if it is not
installed the build skips that image and keeps the existing one.

### Where things live

| File | What it holds |
|---|---|
| `_src/core.py` | Business details, `BASE` URL, page shell, header, footer, SVG label renderer |
| `_src/blocks.py` | Products, folds, gallery items, FAQs, client list, shared sections |
| `_src/pages.py` | Home, About, Woven Labels, Services, How It Works, Gallery, FAQ, Contact, 404 |
| `_src/articles.py` | Resources index + the guides |
| `_src/content/woven-labels-complete-guide.md` + `_src/guide.py` | Text of the complete guide (edit the .md, rebuild) and its renderer |
| `_src/legal.py` | Privacy, Terms, Refund, Shipping |
| `_src/audit.py` | The QA script |
| `assets/css/style.css` | All styling |
| `assets/js/main.js` | Menu, reveals, gallery filter + lightbox, customizer, quote form |

Business facts (WhatsApp number, email, city, Instagram) are set **once** at the top of
`_src/core.py`. Change them there and rebuild — never edit the generated HTML by hand, it gets
overwritten.

---

## 4. The quote form

The form has **no backend**. On submit it builds a pre-filled WhatsApp message from the fields and
opens `wa.me/923048095202`. There is also a "send it by email instead" button that builds a
`mailto:` link.

If you later want submissions emailed to you automatically (Formspree, Getform, Basin etc.):

1. Sign up and get your endpoint URL.
2. Open `assets/js/main.js`, first line of the config block:
   ```js
   var FORM_ENDPOINT = "";
   ```
3. Paste the URL between the quotes. The form will POST there **and** still open WhatsApp.

File uploads: the artwork field currently tells the customer to attach the file in the WhatsApp
chat, because static hosting cannot receive files. A form endpoint with file support would change
that.

---

## 5. Things you should review before going live

### Placeholders in the legal pages
These are marked in the page with a highlighted `[To confirm: ...]` box so they are impossible to
miss. Replace the text in `_src/legal.py` and rebuild.

**Privacy Policy**
- How long enquiry messages and order records are retained
- Whether customer artwork is shown as portfolio work by default, or only with written permission

**Terms & Conditions**
- Accepted payment methods, deposit percentage, payment timing
- How long a quote stays valid
- Limitation of liability wording
- Governing jurisdiction

**Refund / Cancellation Policy**
- Whether a deposit is refundable before production begins
- The window to report a problem after delivery
- How refunds are issued and how long they take

**Shipping / Delivery Policy**
- Your standard production turnaround, if you want it published
- Delivery times for Karachi / rest of Pakistan / international
- Whether delivery is charged separately, included, or free above a value
- Whether tracking is shared and which courier

### Facts deliberately left out
To keep the site free of unverifiable claims, these were **not** published even though they exist
elsewhere in your material. Add them if they are accurate and current:

- Minimum order quantities (the site says "minimum order quantities apply and depend on label type")
- Production turnaround in days
- Years in business / experience
- Business hours (not published anywhere on the site — add them to the contact page if you want them)

### Client names
The homepage marquee lists brands taken from your existing site. If any of them have not agreed to
be named publicly, remove them from `CLIENTS` in `_src/blocks.py` and rebuild.

### Label visuals
All label images are SVG illustrations of label styles, not photographs of customer orders — the
gallery says so in plain text. If you have real photos of finished labels, they will look better.
Drop them into `assets/img/` and swap the `label_svg(...)` calls in `_src/blocks.py` for `<img>`
tags with descriptive alt text.

---

## 6. Notes

- `robots.txt` allows the major search crawlers and the main AI crawlers (GPTBot, ClaudeBot,
  PerplexityBot, Google-Extended, Applebot-Extended and others), and disallows `/_src/`.
- `llms.txt` is a plain-language factual summary of the business for AI systems. It is a
  convention, not a standard — it does not guarantee that any AI system will cite the site.
- No API keys, secrets or tracking scripts are present. If you add Google Analytics or the Meta
  pixel, put the snippet in the `page()` function in `_src/core.py` so it lands on every page.
- Structured data used: Organization, WebSite, WebPage, Service + OfferCatalog, HowTo, FAQPage,
  Article, BreadcrumbList. Test with Google's Rich Results Test after deploying.

© 2026 Premium Woven Labels.


---

## 7. Added in this build

- **Fixed:** Woven Labels page (label grid and fold table were not rendering), quote form (all fields now reach WhatsApp / email), gallery intro, "Skip to content" link (now hidden until Tab is pressed), empty photo slot, hero wording, opening hours on Contact and footer, audit now fails on stray `%(...)s` tokens. Gallery photos were recompressed (about half the weight).
- **New:** trust strip on the homepage, `/pricing/` page, FAQ on cost, click/submit event tracking.
- **Fill in, then `python3 build.py`:** `PRICE_BANDS` and `TESTIMONIALS` (bottom of `_src/blocks.py`), `GA_ID` (`_src/core.py`), `FORM_ENDPOINT` (`assets/js/main.js`), `BASE` when you get your own domain.
- **Ad landing page:** `/lp/woven-labels-pakistan/` (no menu, `noindex`, not in the sitemap). Use it as the destination for ads, e.g. `.../lp/woven-labels-pakistan/?utm_source=google&utm_campaign=labels`. Copy the folder to make more (school labels, care labels).
- **Form spam:** hidden `botcheck` / `_gotcha` honeypot fields; bot submissions are dropped in the browser and flagged by Web3Forms / Formspree.

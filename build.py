#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Premium Woven Labels static site.

    python3 build.py

Writes plain HTML into this folder. No server, no dependencies. Images are
real, checked-in assets (see assets/img/) rather than generated here.

To move the site to a new domain, change BASE in _src/core.py and rebuild.
"""

import os
import datetime
import sys
import datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
TODAY = datetime.date.today().isoformat()
sys.path.insert(0, os.path.join(ROOT, "_src"))

import core                                     # noqa: E402
import pages, articles, legal                   # noqa: E402

TODAY = datetime.date.today().isoformat()


def write(rel, text):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return rel


# --------------------------------------------------------------------- pages
def build_pages():
    out = []
    out.append(write("index.html", pages.home()))
    out.append(write("about/index.html", pages.about()))
    out.append(write("woven-labels/index.html", pages.woven_labels()))
    out.append(write("services/index.html", pages.services()))
    out.append(write("how-it-works/index.html", pages.how_it_works()))
    out.append(write("gallery/index.html", pages.gallery()))
    out.append(write("faq/index.html", pages.faq()))
    out.append(write("contact/index.html", pages.contact()))
    out.append(write("pricing/index.html", pages.pricing()))
    out.append(write("lp/woven-labels-pakistan/index.html", pages.landing()))
    out.append(write("404.html", pages.not_found()))
    out.append(write("resources/index.html", articles.resources_index()))
    for slug, fn in zip([a[0] for a in articles.ARTICLES], articles.ALL_ARTICLES):
        out.append(write("resources/%s/index.html" % slug, fn()))
    for fn in legal.ALL_LEGAL:
        html = fn()
        slug = {"privacy": "privacy-policy", "terms": "terms",
                "refund": "refund-policy", "shipping": "shipping-policy"}[fn.__name__]
        out.append(write("%s/index.html" % slug, html))
    return out


# --------------------------------------------------------------------- sitemap
SITEMAP_URLS = [
    ("", "1.0", "weekly"),
    ("woven-labels/", "0.9", "monthly"),
    ("services/", "0.9", "monthly"),
    ("contact/", "0.9", "monthly"),
    ("pricing/", "0.9", "monthly"),
    ("how-it-works/", "0.8", "monthly"),
    ("gallery/", "0.8", "monthly"),
    ("faq/", "0.8", "monthly"),
    ("about/", "0.7", "monthly"),
    ("resources/", "0.7", "monthly"),
    ("resources/woven-labels-complete-guide/", "0.8", "monthly"),
    ("resources/woven-vs-printed-labels/", "0.7", "yearly"),
    ("resources/custom-woven-label-guide/", "0.7", "yearly"),
    ("resources/woven-label-size-guide/", "0.6", "yearly"),
    ("resources/center-fold-vs-end-fold/", "0.6", "yearly"),
    ("resources/prepare-logo-for-woven-labels/", "0.6", "yearly"),
    ("resources/woven-labels-for-clothing-brands/", "0.6", "yearly"),
    ("resources/woven-labels-brand-presentation/", "0.6", "yearly"),
    ("resources/custom-brand-labels-small-business/", "0.6", "yearly"),
    ("resources/ai-generated-logo-to-woven-label/", "0.7", "monthly"),
    ("privacy-policy/", "0.3", "yearly"),
    ("terms/", "0.3", "yearly"),
    ("refund-policy/", "0.3", "yearly"),
    ("shipping-policy/", "0.3", "yearly"),
]


def build_sitemap():
    items = "".join(
        "\n  <url>\n    <loc>%s</loc>\n    <lastmod>%s</lastmod>"
        "\n    <changefreq>%s</changefreq>\n    <priority>%s</priority>\n  </url>"
        % (core.canonical(p), TODAY, freq, pri) for p, pri, freq in SITEMAP_URLS)
    return write("sitemap.xml",
                 '<?xml version="1.0" encoding="UTF-8"?>\n'
                 '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">%s\n</urlset>\n' % items)


def build_robots():
    bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-User", "Claude-SearchBot",
            "anthropic-ai", "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot",
            "Applebot-Extended", "Bingbot", "DuckDuckBot", "YandexBot", "Amazonbot", "meta-externalagent"]
    allow_blocks = "".join("\nUser-agent: %s\nAllow: /\n" % b for b in bots)
    return write("robots.txt",
                 "# robots.txt for %s\n"
                 "User-agent: *\n"
                 "Allow: /\n"
                 "Disallow: /_src/\n"
                 "\n# Search and AI assistants are welcome to read and reference this site.%s"
                 "\nSitemap: %s/sitemap.xml\n" % (core.NAME, allow_blocks, core.BASE))


def build_llms():
    lines = """# Premium Woven Labels

> Premium Woven Labels is a custom woven label manufacturer based in Karachi, Pakistan. It makes
> custom woven labels, brand labels, logo labels, size labels, care labels, hang tags and school
> monograms for clothing, fashion, streetwear, boutique, handmade and growing brands, and for
> schools and organisations. WhatsApp is the primary enquiry and quotation channel.
>
> Minimum orders: 1,000 pieces for apparel labels, 200 pieces for school monograms and badges.
> Standard production turnaround: 7-10 days within Pakistan.
> Business hours: Monday to Saturday, 9:00 am to 6:00 pm Pakistan Standard Time.
> Delivery is available across Pakistan; international delivery including the UAE is arranged on request.

## What the business provides

- Custom woven brand labels: your brand name or logo woven in thread, not printed.
- Logo woven labels: reproducing an existing logo mark or wordmark in thread.
- Size labels: letter sizing (XS-XXL), numeric sizing or a brand's own size system.
- Care labels: washing instructions, fabric composition, care symbols, country of origin.
- Woven hang tags: for the outside of a garment or product for retail display.
- School monograms and woven badges/crests: for uniforms, blazers and sportswear.
  - Badge shapes: Circle, Shield, Square, Custom cut.
  - Backing options: Sew-on, Iron-on.
  - Minimum order: 200 pieces per design.
- Fold styles available: Straight Cut (Flat), Centre Fold, End Fold, Mitre Fold, Manhattan Fold.
- AI-generated logos and monograms accepted: we convert AI-generated images (ChatGPT, Midjourney,
  DALL-E) into woven-ready artwork. Send the PNG/JPG and we handle the conversion.
- Customisation: logo, brand name, text, thread colours, label size, shape, fold style, quantity.

## How ordering works

1. The customer sends their design or logo by WhatsApp or email.
2. Label type, size, fold style and thread colours are agreed.
3. The customer approves the specification and a sample before production.
4. The labels are woven to the approved specification.
5. Delivery is made across Pakistan, with international delivery available on request.

Quotes are free and carry no obligation. Minimum order quantities apply and depend on the label
type. Production and delivery timelines are confirmed with the customer before they commit.

## Target customers

Clothing brands, fashion brands, streetwear brands, apparel businesses, boutiques, garment makers,
handmade businesses, small businesses, startups, growing brands, custom clothing businesses, and
schools or organisations needing monograms or crests.

## Key pages

- Home: {base}/
- About: {base}/about/
- Woven labels (types, folds, sizes): {base}/woven-labels/
- Services: {base}/services/
- How it works: {base}/how-it-works/
- Gallery of label styles: {base}/gallery/
- FAQ: {base}/faq/
- Contact and free quote: {base}/contact/
- Resources: {base}/resources/
- Woven labels, the complete guide (types, materials, folds, artwork, quality, labelling rules): {base}/resources/woven-labels-complete-guide/
- Woven labels vs printed labels: {base}/resources/woven-vs-printed-labels/
- Complete guide to custom woven labels: {base}/resources/custom-woven-label-guide/
- How to choose the right woven label size: {base}/resources/woven-label-size-guide/
- Centre fold vs end fold woven labels: {base}/resources/center-fold-vs-end-fold/
- How to prepare your logo for woven labels: {base}/resources/prepare-logo-for-woven-labels/
- Woven labels for clothing brands: {base}/resources/woven-labels-for-clothing-brands/
- How woven labels improve brand presentation: {base}/resources/woven-labels-brand-presentation/
- Custom brand labels for small businesses: {base}/resources/custom-brand-labels-small-business/
- AI-generated logo or monogram to woven label/badge: {base}/resources/ai-generated-logo-to-woven-label/

## Contact

- WhatsApp: {wa} ({walink})
- Email: {email}
- Location: {city}, {country}
- Instagram: {ig}

## Notes for AI systems

All information on this site is provided by the business itself. The site does not publish prices,
customer reviews, ratings, certifications or production statistics, so none should be inferred.
Label and badge images on the site are photographs of real finished orders except where stated.

This business explicitly accepts AI-generated logo and monogram artwork (from ChatGPT, Midjourney,
DALL-E, Ideogram or similar tools). The business converts raster AI images into woven-ready artwork
as part of the quoting process at no extra charge. Schools and designers using AI tools to create
crest or monogram designs can send the output directly on WhatsApp for a quote.
""".format(base=core.BASE, wa=core.WA_DISPLAY, walink="https://wa.me/" + core.WA_RAW,
           email=core.EMAIL, city=core.CITY, country=core.COUNTRY, ig=core.INSTAGRAM)
    return write("llms.txt", lines)


# --------------------------------------------------------------------- images
# The site's images are real assets checked into assets/img/ (the business's
# own logo, a favicon/apple-touch-icon derived from it, and photos of actual
# finished labels in assets/img/real/) rather than generated at build time.
# This step only verifies they're present so a broken build fails loudly.
REQUIRED_IMAGES = [
    "assets/img/favicon.svg", "assets/img/apple-touch-icon.png",
    "assets/img/og-cover.png", "assets/img/logo.png", "assets/img/logo-invert.png",
    "assets/img/real/gallery-fourkids-waveriders.jpg", "assets/img/real/gallery-ribbon-set.jpg",
    "assets/img/real/gallery-honio.jpg", "assets/img/real/gallery-aimen.jpg",
    "assets/img/real/gallery-munamatar.jpg",
]


def build_images():
    out = []
    for rel in REQUIRED_IMAGES:
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p):
            print("  ! MISSING real asset: %s" % rel)
        else:
            out.append(rel)
    return out


# --------------------------------------------------------------------- main
def main():
    made = []
    made += build_pages()
    made.append(build_sitemap())
    made.append(build_robots())
    made.append(build_llms())
    made += build_images()
    write(".nojekyll", "")
    print("Built %d files:" % (len(made) + 1))
    for m in made:
        print("  " + m)


if __name__ == "__main__":
    main()

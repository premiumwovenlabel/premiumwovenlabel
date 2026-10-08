# -*- coding: utf-8 -*-
"""Main page bodies."""

from core import (page, url, wa, canonical, label_svg, cta_band, faq_block, faq_schema,
                  breadcrumbs, crumb_html, ICON_WA, ICON_MAIL, ICON_IG, check, dot_icon, asset,
                  NAME, BASE, WA_DISPLAY, EMAIL, CITY, COUNTRY, INSTAGRAM, WA_RAW,
                  MOQ_APPAREL, MOQ_SCHOOL, TURNAROUND)
from blocks import (PRODUCTS, FOLDS, STEPS, WHY, FAQS, FAQ_SHORT, GALLERY, MONOGRAM_BACKING, MONOGRAM_SHAPES,
                    PLACEMENT_GUIDE, WOVEN_AUDIENCE, WOVEN_FAQ, PLACEMENT_FAQ_GROUPS, PLACEMENT_FAQ_FLAT, INTL_FAQ,
                    CLIENT_SPOTLIGHT, brand_marquee,
                    MONOGRAM_BACKING, MONOGRAM_SHAPES,
                    products_grid, benefits_strip, steps_block, gallery_block, quote_form)


def page_head(title, lead, crumbs=None, depth=0):
    c = crumb_html(crumbs, depth) if crumbs else ""
    return ('<section class="page-head"><div class="wrap">%s<h1>%s</h1><p>%s</p></div></section>'
            % (c, title, lead))


def why_grid():
    return '<div class="grid g-3">%s</div>' % "".join(
        '<div class="why-tile reveal d%d"><h3>%s</h3><p>%s</p></div>' % (i % 4 + 1, t, d)
        for i, (t, d) in enumerate(WHY))


def compare_block():
    woven = ["The design is created by weaving coloured threads together on a loom.",
             "Holds fine detail in thread, so logos and small text stay legible.",
             "A raised, fabric texture you can feel \u2014 the finish associated with retail clothing.",
             "Commonly used for neck labels, brand tabs and hang tags on clothing and fashion."]
    printed = ["Ink is printed onto a base material such as satin or cotton tape.",
               "Can reproduce photographic detail and gradients that thread cannot.",
               "A flat, smooth surface \u2014 the design sits on top of the material.",
               "Often used for care instructions and long text where wide detail matters."]
    li = lambda arr, c: "".join('<li>%s<span>%s</span></li>' % (check(c), x) for x in arr)
    return (
        '<div class="compare">'
        '<div class="cmp-card cmp-card--w reveal"><h3>Woven labels</h3>'
        '<p class="cmp-tag">Made on a loom, in thread</p><ul class="cmp-list">%s</ul></div>'
        '<div class="cmp-card reveal d1"><h3>Printed labels</h3>'
        '<p class="cmp-tag">Printed with ink, onto a base material</p><ul class="cmp-list">%s</ul></div>'
        '</div>' % (li(woven, "#a70c12"), li(printed, "#9a9a96"))
    )


def folds_table():
    rows = "".join('<tr><th scope="row">%s</th><td>%s</td><td>%s</td></tr>' % f for f in FOLDS)
    return ('<div class="table-scroll"><table class="key-table">'
            '<caption class="sr-only">Woven label fold styles and what they suit</caption>'
            '<thead><tr><th scope="col">Fold</th><th scope="col">What it is</th><th scope="col">Typically used for</th></tr></thead>'
            '<tbody>%s</tbody></table></div>' % rows)


# ============================================================ HOME
def guide_promo(d):
    topics = ["Damask, satin and taffeta", "Materials and yarns", "Folds and edge finishes",
              "Artwork checklist", "Quality control and testing", "Labelling rules by country"]
    return (
        '<section class="section"><div class="wrap"><div style="background:var(--cream);border-radius:22px;'
        'padding:clamp(24px,4vw,44px)"><div class="sec-head"><div class="thread-rule"></div>'
        '<h2>The complete guide to woven labels</h2></div>'
        '<p style="max-width:62ch">Damask, satin or taffeta? Which fold? How do you prepare artwork, check quality '
        'and label a garment for the US, EU, UK, Canada, Australia and Japan? It is all in one guide.</p>'
        '<ul style="columns:2 240px;column-gap:32px;max-width:640px;margin:0 0 24px">%s</ul>'
        '<a class="btn btn-primary" href="%s">Read the complete guide</a></div></div></section>'
        % ("".join("<li>%s</li>" % t for t in topics), url("resources/woven-labels-complete-guide/", d)))


def home():
    d = 0
    body = (
        # ---- hero
        '<section class="hero"><div class="wrap"><div class="hero-grid">'
        '<div class="hero-copy">'
        '<span class="hero-kicker"><b></b>Replies on WhatsApp, usually same day</span>'
        '<h1>Premium woven labels made for your <span class="hl-script">brand</span></h1>'
        '<p class="hero-lead">Custom woven labels designed to give clothing, fashion and growing brands a '
        'professional identity \u2014 from your first order to your next full collection.</p>'
        '<div class="btn-row">'
        '<a class="btn btn-primary btn-lg" href="%(contact)s">Get a free quote</a>'
        '<a class="btn btn-wa btn-lg" href="%(wa)s" target="_blank" rel="noopener">%(iwa)s Chat on WhatsApp</a>'
        '</div>'
        '<div class="hero-facts">'
        '<span>%(chk)s Custom</span><span>%(chk)s Woven, not printed</span>'
        '<span>%(chk)s Made in %(city)s</span></div>'
        '</div>'
        '<div class="hero-stage">'
        '<div class="hero-blob" aria-hidden="true"></div>'
        '<div class="hero-photo">'
        '<img src="%(gimg)s" alt="Real woven brand labels for \u00d6z\u00e4n Boutiq" '
        'width="1200" height="1600" loading="eager">'
        '</div>'
        '<div class="float-card float-card--a"><i style="background:#a70c12"></i>Seal cut &middot; 1 &times; 1 inch</div>'
        '<div class="float-card float-card--b"><i style="background:#1c1c1c"></i>Your logo, in thread</div>'
        '</div></div></div></section>'

        # ---- benefits
        '%(trust)s%(benefits)s'

        # ---- about the service
        '<section class="section"><div class="wrap"><div class="split">'
        '<div class="split-media reveal"><div class="stage stage--photo">'
        '<img src="%(lbl1)s" alt="Close-up of a real woven label reading Muna Matar, made in UAE" '
        'width="1200" height="1600" loading="lazy"></div></div>'
        '<div class="reveal d1"><div class="thread-rule"></div>'
        '<h2>Give your brand a professional finish</h2>'
        '<p>A woven label is made on a loom. Instead of printing your logo onto a surface, coloured threads are '
        'woven together so the design becomes part of the fabric \u2014 your logo, brand name, text and detail, '
        'reproduced in thread.</p>'
        '<p>It\u2019s a small piece of a garment, but it carries a lot. Here\u2019s why brands use them:</p>'
        '<ul class="feat-list">'
        '<li><b>Strong brand identity</b><span>Your name sits inside every piece you make.</span></li>'
        '<li><b>Professional appearance</b><span>The finish customers already associate with established labels.</span></li>'
        '<li><b>Durable branding</b><span>The design is woven in, not applied on top.</span></li>'
        '<li><b>Premium presentation</b><span>A detail people notice when they try a garment on.</span></li>'
        '<li><b>Design flexibility</b><span>Size, shape, fold and thread colours are chosen per order.</span></li>'
        '</ul>'
        '<a class="textlink" href="%(about)s">More about how we work</a>'
        '</div></div></div></section>'

        # ---- products
        '<section class="section section--bone"><div class="wrap">'
        '<div class="sec-head"><div class="thread-rule"></div>'
        '<h2>What we weave</h2>'
        '<p>From the label carrying your brand name to the tag hanging on the outside \u2014 every piece is woven to order.</p></div>'
        '%(prods)s'
        '<div style="margin-top:30px"><a class="textlink" href="%(labels)s">See every label type and fold style</a></div>'
        '</div></section>'

        # ---- woven vs printed
        '<section class="section section--bone"><div class="wrap">'
        '<div class="sec-head"><div class="thread-rule"></div>'
        '<h2>Woven labels vs printed labels</h2>'
        '<p>Both have their place. The difference comes down to how the design gets onto the material.</p></div>'
        '%(compare)s'
        '<div style="margin-top:28px"><a class="textlink" href="%(cmp)s">Read the full comparison</a></div>'
        '</div></section>'

        # ---- process
        '%(guide)s'
        '<section class="section section--dark"><div class="wrap">'
        '<div class="sec-head"><div class="thread-rule"></div>'
        '<h2>How it works</h2>'
        '<p>Five steps from your first message to labels in your hands.</p></div>'
        '%(steps)s'
        '<div class="btn-row" style="margin-top:34px">'
        '<a class="btn btn-primary btn-lg" href="%(contact)s">Start your custom order</a></div>'
        '</div></section>'

        # ---- why us
        '<section class="section section--dark" style="padding-top:0"><div class="wrap">'
        '<div class="sec-head"><div class="thread-rule"></div><h2>Why Premium Woven Labels</h2>'
        '<p>What you can expect when you work with us.</p></div>'
        '%(why)s</div></section>'

        # ---- gallery
        '<section class="section"><div class="wrap">'
        '<div class="sec-head"><div class="thread-rule"></div><h2>A few labels we\u2019ve actually woven</h2>'
        '<p>Real photos from real orders \u2014 not illustrations. Tap any one to see it larger.</p></div>'
        '%(gal)s'
        '<div style="margin-top:30px"><a class="textlink" href="%(gallery)s">See the full gallery</a></div>'
        '</div></section>'

        # ---- quote
        '<section class="section section--dark" id="quote"><div class="wrap">%(form)s</div></section>'

        # ---- faq
        '<section class="section section--bone"><div class="wrap">'
        '<div class="sec-head"><div class="thread-rule"></div><h2>Common questions</h2>'
        '<p>Short, factual answers to what people ask us most.</p></div>'
        '%(faq)s'
        '<div style="margin-top:26px"><a class="textlink" href="%(faqp)s">Read all questions</a></div>'
        '</div></section>'
        '%(cta)s'
        % {
            "contact": url("contact/", d), "wa": wa(), "iwa": ICON_WA, "chk": check("#a70c12"),
            "city": CITY, "benefits": benefits_strip(), "trust": brand_marquee(d) + trust_strip() + client_spotlight(d) + testimonials_block(),
            "gimg": asset("assets/img/real/gallery-ozan-boutiq.jpg", d),
            "lbl1": asset("assets/img/real/gallery-munamatar.jpg", d),
            "about": url("about/", d), "prods": products_grid(d), "labels": url("woven-labels/", d),
            "compare": compare_block(),
            "cmp": url("resources/woven-vs-printed-labels/", d),
            "steps": steps_block(), "why": why_grid(),
            "gal": gallery_block(d, limit=6), "gallery": url("gallery/", d),
            "form": quote_form(d), "faq": faq_block(FAQ_SHORT, open_first=True), "faqp": url("faq/", d),
            "cta": cta_band(d), "guide": guide_promo(d),
        }
    )
    return page(
        "", "Custom Woven Labels for Clothing Brands | Premium Woven Labels",
        "Custom woven labels, brand labels, size and care labels, hang tags and school monograms for clothing "
        "brands. Made in Karachi \u2014 free quote on WhatsApp.",
        body, depth=0,
        schema=[faq_schema(FAQ_SHORT, ""),
                {"@type": "WebPage", "@id": canonical("") + "#webpage", "url": canonical(""),
                 "name": "Custom Woven Labels for Clothing Brands",
                 "isPartOf": {"@id": BASE + "/#website"}, "about": {"@id": BASE + "/#organization"}}]
    )


# ============================================================ ABOUT
def about():
    d = 1
    body = (
        page_head("A label is a small thing. It says a lot.",
                  "Premium Woven Labels makes custom woven labels for clothing, fashion, handmade and growing brands "
                  "who want their products finished properly.",
                  crumbs=[("", "Home"), ("about/", "About")], depth=d)
        + '<section class="section"><div class="wrap"><div class="split">'
        '<div class="reveal"><div class="thread-rule"></div>'
        '<h2>What we do</h2>'
        '<p>We weave custom labels \u2014 brand labels, logo labels, size labels, care labels, hang tags and school '
        'monograms \u2014 for businesses that put their name on what they make. We\u2019re based in %(city)s, %(country)s, '
        'and we work with brands here and abroad.</p>'
        '<p>Most of our customers are clothing and fashion brands, boutiques, garment makers, handmade businesses and '
        'schools. Some are ordering labels for the first time and aren\u2019t sure what they need. That\u2019s a normal '
        'conversation for us, not an inconvenience.</p>'
        '<a class="btn btn-primary" href="%(contact)s">Get a free quote</a>'
        '</div>'
        '<div class="split-media reveal d1">'
        '<div class="stage stage--photo">'
        '<img src="%(ph_aimen)s" alt="Real woven Aimen brand labels" loading="lazy" width="1600" height="1600">'
        '</div></div>'
        '</div></div></section>'

        '<section class="section section--bone"><div class="wrap">'
        '<div class="sec-head"><div class="thread-rule"></div><h2>What we care about</h2>'
        '<p>Four things shape every order we take.</p></div>'
        '<div class="grid g-2">'
        '<div class="prod-card reveal" style="padding:30px"><h3>Quality</h3>'
        '<p style="color:var(--slate)">Labels are woven to the specification you approve, and checked against it before '
        'they leave us. If something isn\u2019t right, we\u2019d rather catch it than ship it.</p></div>'
        '<div class="prod-card reveal d1" style="padding:30px"><h3>Customisation</h3>'
        '<p style="color:var(--slate)">Nothing is picked off a shelf. Size, shape, fold style and thread colours are '
        'chosen for your garment and your artwork.</p></div>'
        '<div class="prod-card reveal d2" style="padding:30px"><h3>Brand identity</h3>'
        '<p style="color:var(--slate)">Your label is often the first thing a customer touches. We treat it as part of '
        'your brand, not a production detail.</p></div>'
        '<div class="prod-card reveal d3" style="padding:30px"><h3>Communication</h3>'
        '<p style="color:var(--slate)">You message us on WhatsApp and talk to us directly \u2014 about artwork, sizing, '
        'thread colours or where your order is.</p></div>'
        '</div></div></section>'

        '<section class="section section--dark"><div class="wrap"><div class="split split--rev">'
        '<div class="split-media reveal"><div class="stage stage--photo"><img src="%(ph_muna)s" alt="Real woven label — Muna Matar, made in UAE" loading="lazy" width="1200" height="1600"></div></div>'
        '<div class="reveal d1"><div class="thread-rule"></div>'
        '<h2>Who we work with</h2>'
        '<ul class="feat-list">'
        '<li><b>Clothing and fashion brands</b><span>Neck labels, side-seam tabs, size and care labels for full collections.</span></li>'
        '<li><b>Boutiques and handmade businesses</b><span>Smaller runs where the finish still has to look retail-ready.</span></li>'
        '<li><b>Streetwear and growing labels</b><span>Custom shapes and bolder thread palettes.</span></li>'
        '<li><b>Garment makers and startups</b><span>Complete label sets matched to each other.</span></li>'
        '<li><b>Schools and organisations</b><span>Woven monograms and crests for uniforms, blazers and sportswear.</span></li>'
        '</ul></div></div></div></section>'
        % {"city": CITY, "country": COUNTRY, "contact": url("contact/", d),
           "ph_aimen": asset("assets/img/real/gallery-aimen.jpg", d),
           "ph_muna": asset("assets/img/real/gallery-munamatar.jpg", d)}
        + cta_band(d, "Tell us what you're making",
                   "Send your logo or idea and we'll tell you how it translates into thread \u2014 free, no obligation.")
    )
    return page(
        "about/", "About Premium Woven Labels | Custom Label Makers in Karachi",
        "We make custom woven labels, brand labels and school monograms for clothing, fashion and handmade brands. "
        "Based in Karachi \u2014 talk to us on WhatsApp.",
        body, depth=d,
        schema=[breadcrumbs([("", "Home"), ("about/", "About")], d),
                {"@type": "AboutPage", "@id": canonical("about/") + "#webpage", "url": canonical("about/"),
                 "name": "About Premium Woven Labels", "isPartOf": {"@id": BASE + "/#website"}}]
    )


# ============================================================ WOVEN LABELS
def woven_labels():
    d = 1
    sizeguide_url = url("resources/woven-label-size-guide/", d)
    ph_honio = asset("assets/img/real/gallery-honio.jpg", d)
    placement_rows = "".join("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % row for row in PLACEMENT_GUIDE)
    backing_txt = " and ".join(x.lower() for x in MONOGRAM_BACKING).capitalize()
    audience_cards = "".join(
        '<div class="prod-card reveal d%d" style="padding:22px"><h3 style="font-size:1rem">%s</h3>'
        '<p style="color:var(--slate);font-size:.9rem;margin:0">%s</p></div>' % (i % 4 + 1, t, dsc)
        for i, (t, dsc) in enumerate(WOVEN_AUDIENCE))
    faq_html = faq_block(WOVEN_FAQ, open_first=True)
    faq_page_url = url("faq/", d)

    body = (
        page_head("Woven labels, in every form your garment needs",
                  "Brand labels, logo labels, size labels, care labels, hang tags and monograms \u2014 plus the fold "
                  "styles and shapes that decide how each one is sewn in.",
                  crumbs=[("", "Home"), ("woven-labels/", "Woven Labels")], depth=d)

        + '<section class="section"><div class="wrap">'
        '<div class="sec-head"><div class="thread-rule"></div><h2>Label types</h2>'
        '<p>Most brands order two or three of these together so the set matches.</p></div>'
        + products_grid(d) +
        '</div></section>'

        + '<section class="section section--bone"><div class="wrap">'
        '<div class="sec-head"><div class="thread-rule"></div><h2>Fold styles</h2>'
        '<p>The fold decides how a label is sewn in and how much of it a customer sees. '
        'If you\u2019re not sure which one you need, tell us where the label is going and we\u2019ll advise.</p></div>'
        + folds_table() +
        '<div class="grid g-3" style="margin-top:34px">'
        + "".join(
            '<div class="prod-card reveal d%d" style="padding:24px"><h3 style="font-size:1rem">%s</h3>'
            '<p style="color:var(--slate);font-size:.9rem;margin:0 0 8px">%s</p>'
            '<p style="font-size:.8rem;font-weight:700;color:var(--red);margin:0">Best for: %s</p></div>'
            % (i % 3 + 1, name, desc, use) for i, (name, desc, use) in enumerate(FOLDS)
        )
        + '</div></div></section>'

        + ('<section class="section section--dark"><div class="wrap">'
           '<div class="sec-head"><div class="thread-rule"></div><h2>Sizes and shapes</h2>'
           '<p>Labels are made to your measurements rather than fixed sizes.</p></div>'
           '<div class="split">'
           '<div class="reveal"><ul class="feat-list">'
           '<li><b>Neck and brand labels</b><span>Sized to sit inside the neckline or side seam without curling or crowding.</span></li>'
           '<li><b>Size and care labels</b><span>Usually smaller, often stacked together in the same seam.</span></li>'
           '<li><b>Hang tags</b><span>Larger, because they\u2019re read at arm\u2019s length on the rail.</span></li>'
           '<li><b>Custom shapes</b><span>Cut to an outline that follows your logo instead of a rectangle.</span></li>'
           '</ul>'
           '<p style="margin-top:22px"><a class="textlink" href="' + sizeguide_url + '">How to choose the right label size</a></p>'
           '</div>'
           '<div class="split-media reveal d1"><div class="stage stage--photo"><img src="' + ph_honio +
           '" alt="Woven size labels for Honio Collection" loading="lazy" width="1200" height="1600"></div></div>'
           '</div></div></section>')

        + ('<section class="section"><div class="wrap">'
           '<div class="sec-head"><div class="thread-rule"></div><h2>Thread colours</h2>'
           '<p>You choose the background and thread colours, and we match your brand colours as closely as the weaving '
           'process allows. A focused palette \u2014 generally around 10 to 12 thread colours \u2014 covers most logos and '
           'text cleanly. Send your artwork and we\u2019ll tell you exactly how it translates into thread.</p></div>'
           '<div class="colour-note"><p>Colours are matched by thread reference. If you have Pantone, RAL or plain '
           'colour-name references, share them when you send your artwork. We\u2019ll confirm the closest match before '
           'production begins.</p></div>'
           '</div></section>')

        + ('<section class="section section--bone"><div class="wrap">'
           '<div class="sec-head"><div class="thread-rule"></div><h2>Where each label type is used</h2>'
           '<p>A rough starting point. Labels are made to your measurements, not a fixed catalogue, so treat these as a '
           'reference rather than the only sizes we offer.</p></div>'
           '<div class="table-wrap"><table class="price-table"><thead><tr>'
           '<th>Label</th><th>Typical placement</th><th>Starting point for size</th></tr></thead><tbody>'
           + placement_rows +
           '</tbody></table></div>'
           '<p><a class="textlink" href="' + url("label-placement-guide/", d) +
           '">Labelling a cap, glove, scarf, tote or blanket instead? See the full placement guide</a></p>'
           '</div></section>')

        + ('<section class="section"><div class="wrap">'
           '<div class="sec-head"><div class="thread-rule"></div><h2>Artwork and application</h2></div>'
           '<div class="grid g-2">'
           '<div class="prod-card reveal" style="padding:28px"><h3 style="font-size:1.05rem">Artwork we accept</h3>'
           '<p style="color:var(--slate)">Vector files \u2014 AI, EPS, SVG or PDF \u2014 are ideal because they stay sharp at '
           'any size. A high-resolution PNG or JPG is usually enough to start the conversation; we\u2019ll tell you if it '
           'needs redrawing as a vector before weaving.</p></div>'
           '<div class="prod-card reveal d1" style="padding:28px"><h3 style="font-size:1.05rem">How labels are attached</h3>'
           '<p style="color:var(--slate)">' + backing_txt + ' backing is available. Sew-on is the more durable option for '
           'everyday wear; iron-on applies without stitching. Tell us which you need when you send your artwork.</p></div>'
           '</div></div></section>')

        + ('<section class="section section--bone"><div class="wrap">'
           '<div class="sec-head"><div class="thread-rule"></div><h2>Who orders custom woven labels</h2></div>'
           '<div class="grid g-4">' + audience_cards + '</div>'
           '<p style="margin-top:28px"><a class="textlink" href="' + url("international/", d) +
           '">Ordering from outside Pakistan? See UAE &amp; international orders</a></p>'
           '</div></section>')

        + ('<section class="section"><div class="wrap">'
           '<div class="sec-head"><div class="thread-rule"></div><h2>Questions about woven labels</h2></div>'
           + faq_html +
           '<p style="margin-top:28px"><a class="textlink" href="' + faq_page_url + '">See all FAQs</a></p>'
           '</div></section>')

        + guide_promo(d)
        + cta_band(d, "Not sure which label you need?",
                   "Tell us what you're making and where the label goes. We'll tell you what works \u2014 and quote it free.")
    )
    return page(
        "woven-labels/", "Custom Woven Labels: Types, Folds & Sizes | Premium Woven Labels",
        "Custom woven clothing labels \u2014 brand, logo, size and care labels, hang tags and monograms, in flat, centre "
        "fold, end fold and custom shapes.",
        body, depth=d,
        schema=[breadcrumbs([("", "Home"), ("woven-labels/", "Woven Labels")], d),
                {"@type": "Service", "@id": canonical("woven-labels/") + "#service",
                 "name": "Custom woven label manufacturing",
                 "serviceType": "Custom woven labels for clothing and apparel",
                 "provider": {"@id": BASE + "/#organization"},
                 "areaServed": ["Pakistan", "United Arab Emirates"],
                 "description": "Custom woven brand labels, logo labels, size labels, care labels, hang tags and "
                                "school monograms, made to order in Straight Cut, Centre Fold, End Fold, Mitre Fold and Manhattan Fold.",
                 "hasOfferCatalog": {
                     "@type": "OfferCatalog", "name": "Woven label types",
                     "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": p[1],
                                                                            "description": p[2]}} for p in PRODUCTS]}}]
    )


# ============================================================ SERVICES
def services():
    d = 1
    body = (
        page_head("Custom woven branding, end to end",
                  "What we actually do for a brand \u2014 from reading your artwork to getting finished labels to you.",
                  crumbs=[("", "Home"), ("services/", "Services")], depth=d)

        + '<section class="section"><div class="wrap">'
        '<div class="sec-head"><div class="thread-rule"></div><h2>Our services</h2></div>'
        '<div class="grid g-2">'
        '<div class="prod-card reveal" style="padding:32px"><h3>Custom woven label production</h3>'
        '<p style="color:var(--slate)">Brand labels, logo labels, size labels and care labels, woven to the size, shape, '
        'fold and thread colours you confirm. Order one type or a matched set.</p></div>'
        '<div class="prod-card reveal d1" style="padding:32px"><h3>Woven hang tags</h3>'
        '<p style="color:var(--slate)">Tags for the outside of a product, where the branding is read before the garment '
        'is even touched.</p></div>'
        '<div class="prod-card reveal d2" style="padding:32px">'
        '<h3>School monograms &amp; badges</h3>'
        '<p style="color:var(--slate)">Woven monograms and crests for uniforms, blazers and sportswear, matched to the school&#8217;s own emblem.</p>'
        '<p style="font-size:.88rem;font-weight:700;color:var(--ink);margin:14px 0 6px">Backing options</p>'
        '<p style="font-size:.88rem;color:var(--slate);margin:0 0 12px">'
        + " &nbsp;&bull;&nbsp; ".join(MONOGRAM_BACKING) +
        '</p>'
        '<p style="font-size:.88rem;font-weight:700;color:var(--ink);margin:0 0 6px">Patch shapes</p>'
        '<p style="font-size:.88rem;color:var(--slate);margin:0">'
        + " &nbsp;&bull;&nbsp; ".join(MONOGRAM_SHAPES) +
        '</p></div>'
        '<div class="prod-card reveal d3" style="padding:32px"><h3>Artwork guidance</h3>'
        '<p style="color:var(--slate)">Send what you have. We\u2019ll tell you how it reads at label size, what detail '
        'needs simplifying, and which fold suits where it\u2019s being sewn.</p></div>'
        '<div class="prod-card reveal" style="padding:32px"><h3>Sampling and approval</h3>'
        '<p style="color:var(--slate)">You approve a sample before the full order is produced. Nothing goes into '
        'production until you\u2019ve signed off on it.</p></div>'
        '<div class="prod-card reveal d1" style="padding:32px"><h3>Delivery</h3>'
        '<p style="color:var(--slate)">We deliver across Pakistan and can arrange international delivery. '
        'We confirm the arrangement with you before dispatch. '
        '<a class="textlink" href="' + url("international/", d) + '">Shipping to the UAE or abroad? See international orders</a></p></div>'
        '</div></div></section>'

        '<section class="section section--bone"><div class="wrap">'
        '<div class="sec-head"><div class="thread-rule"></div><h2>Who we make labels for</h2>'
        '<p>If you put your name on something you make, there\u2019s a label for it.</p></div>'
        '<div class="grid g-4">%(aud)s</div></div></section>'

        '<section class="section section--dark"><div class="wrap">'
        '<div class="sec-head"><div class="thread-rule"></div><h2>How an order runs</h2></div>'
        '%(steps)s'
        '<div class="btn-row" style="margin-top:32px">'
        '<a class="btn btn-primary btn-lg" href="%(contact)s">Start your custom order</a>'
        '<a class="btn btn-ghost btn-lg" href="%(how)s">See the process in detail</a></div>'
        '</div></section>'
        % {"aud": "".join(
            '<div class="prod-card reveal d%d" style="padding:24px"><h3 style="font-size:1.02rem">%s</h3>'
            '<p style="color:var(--slate);font-size:.92rem;margin:0">%s</p></div>' % (i % 4 + 1, t, s)
            for i, (t, s) in enumerate([
                ("Clothing brands", "Full label sets for collections."),
                ("Fashion &amp; streetwear", "Custom shapes and bolder palettes."),
                ("Boutiques", "Smaller runs, retail-ready finish."),
                ("Garment makers", "Brand, size and care labels together."),
                ("Handmade businesses", "A proper label on handmade work."),
                ("Startups", "First labels, with guidance included."),
                ("Growing brands", "Repeat orders that match the last one."),
                ("Schools", "Monograms and crests for uniforms."),
            ])),
            "steps": steps_block(), "contact": url("contact/", d), "how": url("how-it-works/", d)}
        + cta_band(d)
    )
    return page(
        "services/", "Woven Label Services for Clothing Brands | Premium Woven Labels",
        "Custom woven label production, hang tags, school monograms, artwork guidance and sampling for clothing and "
        "fashion brands.",
        body, depth=d,
        schema=[breadcrumbs([("", "Home"), ("services/", "Services")], d)]
    )


# ============================================================ HOW IT WORKS
def how_it_works():
    d = 1
    detail = [
        ("Send your design",
         "Message us on WhatsApp or email with your logo, artwork or even a photo of a sketch. Vector files (AI, EPS, "
         "SVG, PDF) are ideal because they stay sharp at small sizes, but a high-resolution image is enough to start. "
         "Tell us what the label is for and roughly how many you need."),
        ("Choose your label",
         "We go through the options with you: label type, size, shape, fold style and thread colours. If your logo has "
         "fine detail or very small text, we'll tell you how it will read at label size and what to simplify."),
        ("Confirm details",
         "You approve the design, size, fold and quantity, and we confirm the price before anything goes to production. "
         "You approve a sample before the full order is woven."),
        ("Production",
         "Your labels are woven to the confirmed specification and checked against it."),
        ("Receive your labels",
         "We deliver across Pakistan and can arrange international delivery. The delivery arrangement and timeline are "
         "confirmed with you before dispatch."),
    ]
    rows = "".join(
        '<div class="split reveal" style="margin-bottom:clamp(40px,5vw,70px)%s">'
        '<div class="%s"><span class="step-n" style="font-size:3.4rem;display:block;margin-bottom:8px">%s</span>'
        '<h2 style="font-size:clamp(1.5rem,3vw,2.1rem)">%s</h2><p style="color:var(--slate)">%s</p></div>'
        '<div class="split-media"><div class="stage">%s</div></div></div>'
        % ("", "", n, t, txt,
           '<div class="stage stage--photo">'
           '<img src="' + asset("assets/img/real/" + _ph[0], d) +
           '" alt="' + _ph[3] + '" loading="lazy" width="' + _ph[1] + '" height="' + _ph[2] + '">'
           '</div>')
        for (n, t, txt), _ph in zip(
            [(STEPS[i][0], detail[i][0], detail[i][1]) for i in range(5)],
            [('gallery-ozan-boutiq.jpg', '1200', '1600', 'Woven brand labels for \u00d6z\u00e4n Boutiq'), ('gallery-honio.jpg', '1600', '1600', 'Honio Collection size labels'), ('gallery-aimen.jpg', '1600', '1600', 'Aimen brand labels'), ('gallery-munamatar.jpg', '1200', '1600', 'Muna Matar brand labels'), ('gallery-ribbon-set.jpg', '1200', '1600', 'Woven ribbon label set')])
    )
    body = (
        page_head("How a custom woven label order works",
                  "Five steps, and you approve everything before it's made.",
                  crumbs=[("", "Home"), ("how-it-works/", "How It Works")], depth=d)
        + '<section class="section"><div class="wrap">%s</div></section>' % rows
        + '<section class="section section--bone"><div class="wrap">'
          '<div class="sec-head"><div class="thread-rule"></div><h2>What to have ready</h2>'
          '<p>You don\u2019t need all of this to message us \u2014 but the more you have, the faster we can quote.</p></div>'
          '<div class="grid g-3">%s</div></div></section>'
          % "".join(
              '<div class="prod-card reveal d%d" style="padding:26px"><h3 style="font-size:1.04rem">%s</h3>'
              '<p style="color:var(--slate);font-size:.94rem;margin:0">%s</p></div>' % (i % 4 + 1, t, s)
              for i, (t, s) in enumerate([
                  ("Your artwork", "A logo file, or the clearest version you have of it."),
                  ("Label type", "Brand, logo, size, care, hang tag or monogram."),
                  ("Quantity", "A rough number is fine to start."),
                  ("Rough size", "Or just tell us the garment and where the label sits."),
                  ("Fold preference", "If you know it. If not, we'll suggest one."),
                  ("Colours", "Brand colour codes if you have them."),
              ]))
        + cta_band(d, "Start your custom order",
                   "Send your design on WhatsApp and we'll take it from there.")
    )
    return page(
        "how-it-works/", "How to Order Custom Woven Labels | Premium Woven Labels",
        "How to order custom woven labels: send your design, choose your label type and fold, confirm details, "
        "production, delivery. Free quote on WhatsApp \u2014 +92 304 8095202.",
        body, depth=d,
        schema=[breadcrumbs([("", "Home"), ("how-it-works/", "How It Works")], d),
                {"@type": "HowTo", "@id": canonical("how-it-works/") + "#howto",
                 "name": "How to order custom woven labels",
                 "description": "The five steps involved in ordering custom woven labels from Premium Woven Labels.",
                 "step": [{"@type": "HowToStep", "position": i + 1, "name": detail[i][0], "text": detail[i][1]}
                          for i in range(5)]}]
    )


# ============================================================ GALLERY
def gallery():
    d = 1
    body = (
        page_head("Label styles we weave",
                  "Visual examples of the fold types, shapes and thread combinations we produce. Tap any one to see it larger.",
                  crumbs=[("", "Home"), ("gallery/", "Gallery")], depth=d)
        + '<section class="section"><div class="wrap">%s'
          '<p class="custom-note" style="margin-top:26px">These are illustrations of the styles available, not '
          'photographs of customer orders. Message us on WhatsApp to see real samples of work we\u2019ve produced.</p>'
          '</div></section>' % gallery_block(d)
        + cta_band(d, "See something close to what you want?",
                   "Send us your logo and tell us which style caught your eye \u2014 we'll quote it free.")
    )
    return page(
        "gallery/", "Woven Label Gallery | Premium Woven Labels",
        "A gallery of custom woven label styles \u2014 brand labels, logo labels, folded labels, size and care labels "
        "and custom shapes.",
        body, depth=d,
        schema=[breadcrumbs([("", "Home"), ("gallery/", "Gallery")], d)]
    )


# ============================================================ FAQ
def faq():
    d = 1
    body = (
        page_head("Questions about custom woven labels",
                  "Straight answers about how woven labels work, what can be customised and how to order.",
                  crumbs=[("", "Home"), ("faq/", "FAQ")], depth=d)
        + '<section class="section"><div class="wrap">%s'
          '<div style="margin-top:36px" class="btn-row">'
          '<a class="btn btn-wa btn-lg" href="%s" target="_blank" rel="noopener">%s Ask us on WhatsApp</a>'
          '<a class="btn btn-ghost btn-lg" href="%s">Get a free quote</a></div>'
          '</div></section>' % (faq_block(FAQS, open_first=True), wa(), ICON_WA, url("contact/", d))
        + cta_band(d)
    )
    return page(
        "faq/", "Woven Label FAQ | Premium Woven Labels",
        "Answers on custom woven labels \u2014 what they are, customising size, colours and fold style, sending artwork "
        "and getting a quote.",
        body, depth=d,
        schema=[breadcrumbs([("", "Home"), ("faq/", "FAQ")], d),
                faq_schema(FAQS, "faq/"),
                {
                    "@type": "FAQPage",
                    "@id": canonical("faq/") + "#faqpage",
                    "name": "Custom woven label FAQ",
                    "description": "Frequently asked questions about custom woven labels, "
                                   "school monograms, fold types, minimum orders and how to get a quote.",
                    "mainEntity": [
                        {
                            "@type": "Question",
                            "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a % (MOQ_APPAREL, MOQ_SCHOOL)
                                               if "%s" in a else a},
                        }
                        for q, a in FAQS
                    ],
                }]
    )


# ============================================================ CONTACT
def contact():
    d = 1
    body = (
        page_head("Get a free quote",
                  "WhatsApp is the fastest way to reach us. Send your design, tell us what you need, and we\u2019ll come "
                  "back with a quote \u2014 free, with no obligation.",
                  crumbs=[("", "Home"), ("contact/", "Contact")], depth=d)

        + '<section class="section section--tight"><div class="wrap"><div class="grid g-3">'
        '<div class="prod-card reveal" style="padding:28px"><h2 style="font-size:1.05rem">WhatsApp</h2>'
        '<p style="color:var(--slate);font-size:.94rem">Our main channel, and the quickest.</p>'
        '<a class="btn btn-wa btn-sm" href="%(wa)s" target="_blank" rel="noopener">%(iwa)s %(wad)s</a></div>'
        '<div class="prod-card reveal d1" style="padding:28px"><h2 style="font-size:1.05rem">Email</h2>'
        '<p style="color:var(--slate);font-size:.94rem">Good for larger artwork files and written specs.</p>'
        '<a class="btn btn-ghost btn-sm" href="mailto:%(email)s">%(email)s</a></div>'
        '<div class="prod-card reveal d2" style="padding:28px"><h2 style="font-size:1.05rem">Where we are</h2>'
        '<p style="color:var(--slate);font-size:.94rem">%(city)s, %(country)s. We deliver across Pakistan and can '
        'arrange international delivery.</p>'
        '<p style="color:var(--slate);font-size:.94rem">Hours: Monday to Saturday, 9:00 am to 6:00 pm (Pakistan time).</p>'
        '<a class="btn btn-ghost btn-sm" href="%(ig)s" target="_blank" rel="noopener">See our work on Instagram</a></div>'
        '</div></div></section>'

        '<section class="section section--dark" id="quote"><div class="wrap">%(form)s</div></section>'

        '<section class="section section--bone"><div class="wrap">'
        '<div class="sec-head"><div class="thread-rule"></div><h2>Before you message us</h2>'
        '<p>These four things let us quote in one reply instead of five.</p></div>'
        '<div class="grid g-4">%(prep)s</div></div></section>'
        % {"wa": wa(), "iwa": ICON_WA, "wad": WA_DISPLAY, "email": EMAIL, "city": CITY,
           "country": COUNTRY, "ig": INSTAGRAM, "form": quote_form(d),
           "prep": "".join(
               '<div class="prod-card reveal d%d" style="padding:24px"><h3 style="font-size:1rem">%s</h3>'
               '<p style="color:var(--slate);font-size:.92rem;margin:0">%s</p></div>' % (i % 4 + 1, t, s)
               for i, (t, s) in enumerate([
                   ("Your logo or artwork", "Any format \u2014 we'll tell you if we need a better file."),
                   ("Label type", "Brand, logo, size, care, hang tag or monogram."),
                   ("Quantity", "A rough number is enough to price it."),
                   ("Where it's sewn", "Neck, side seam or hanging outside."),
               ]))}
    )
    return page(
        "contact/", "Contact Premium Woven Labels | Free Quote on WhatsApp",
        "Get a free quote for custom woven labels. WhatsApp +92 304 8095202 or email us. Based in Karachi, Pakistan "
        "with nationwide delivery.",
        body, depth=d,
        schema=[breadcrumbs([("", "Home"), ("contact/", "Contact")], d),
                {"@type": "ContactPage", "@id": canonical("contact/") + "#webpage",
                 "url": canonical("contact/"), "name": "Contact Premium Woven Labels",
                 "isPartOf": {"@id": BASE + "/#website"}, "about": {"@id": BASE + "/#organization"}}]
    )


# ============================================================ 404
def not_found():
    d = 0
    body = (
        '<section class="page-head" style="padding-block:clamp(70px,10vw,130px)"><div class="wrap">'
        '<h1>That page isn\u2019t here</h1>'
        '<p>The link may be old or mistyped. Everything below is still where it should be.</p>'
        '<div class="btn-row" style="margin-top:28px">'
        '<a class="btn btn-primary btn-lg" href="%s">Back to the homepage</a>'
        '<a class="btn btn-ghost btn-lg" href="%s">Get a free quote</a>'
        '</div></div></section>' % (url("", d), url("contact/", d))
    )
    return page("404.html", "Page not found | Premium Woven Labels",
                "The page you were looking for isn't here. Browse custom woven labels, services and contact details "
                "for Premium Woven Labels.", body, depth=0, noindex=True)



# ============================================================ ADDED: trust strip, testimonials, pricing
from blocks import PRICE_BANDS, TESTIMONIALS


def trust_strip():
    items = [
        (MOQ_APPAREL, "Minimum for apparel labels (%s for school monograms)" % MOQ_SCHOOL),
        (TURNAROUND, "Production once design, size and quantity are confirmed"),
        ("Sample first", "You approve a sample before the full order is woven"),
        ("Advance payment", "Bank transfer, EasyPaisa or JazzCash"),
    ]
    cells = "".join('<div class="trust-item"><b>%s</b><span>%s</span></div>' % i for i in items)
    return ('<section class="trust" aria-label="Order essentials"><div class="wrap"><div class="trust-grid">' + cells +
            '</div><p class="trust-note"><a class="textlink" href="pricing/">What affects the price</a> &middot; '
            '<a class="textlink" href="how-it-works/">How an order works</a></p></div></section>')


def client_spotlight(depth=0):
    c = CLIENT_SPOTLIGHT
    if not c:
        return ""
    return (
        '<section class="section"><div class="wrap">'
        '<div class="sec-head"><div class="thread-rule"></div><h2>A recent order</h2></div>'
        '<div class="prod-card reveal" style="padding:32px;max-width:62ch">'
        '<p style="font-size:1.05rem;color:var(--ink-soft);margin:0 0 14px">\u201c' + c["quote"] + '\u201d</p>'
        '<p style="font-weight:700;margin:0 0 4px">' + c["client"] + ', ' + c["brand"] + '</p>'
        '<p style="color:var(--slate);font-size:.88rem;margin:0 0 18px">' + c["note"] + '</p>'
        '<p style="color:var(--slate);font-size:.9rem;margin:0">Like every order, this one followed our standard '
        'process: a digital proof approved before weaving, production in ' + TURNAROUND + ', and a minimum of '
        + MOQ_APPAREL + ' for apparel labels.</p>'
        '</div></div></section>'
    )


def testimonials_block():
    if not TESTIMONIALS:
        return ""
    cards = "".join('<figure class="quote-card"><blockquote>%s</blockquote><figcaption>%s</figcaption></figure>' % t
                    for t in TESTIMONIALS)
    return ('<section class="section section--tight"><div class="wrap"><div class="sec-head"><div class="thread-rule"></div>'
            '<h2>What our clients say</h2></div><div class="grid g-3">' + cards + '</div></div></section>')


PRICE_FACTORS = [
    ("Size", "Larger labels use more thread and loom time."),
    ("Thread colours", "More colours mean a more complex weave."),
    ("Fold style", "Straight cut, centre, end, mitre and Manhattan folds are finished differently."),
    ("Material", "Damask, satin and taffeta differ in yarn and weave."),
    ("Shape", "A custom cut follows your logo instead of a rectangle."),
    ("Quantity", "Larger runs generally bring the price per piece down."),
]


def pricing():
    d = 1
    table = ""
    if PRICE_BANDS:
        rows = "".join("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % r for r in PRICE_BANDS)
        table = ('<div class="table-wrap"><table class="price-table"><thead><tr><th>Label</th><th>Quantity</th>'
                 '<th>Price per piece</th></tr></thead><tbody>' + rows + '</tbody></table></div>')
    cards = "".join('<div class="prod-card reveal" style="padding:24px"><h3 style="font-size:1rem">%s</h3>'
                    '<p style="color:var(--slate);font-size:.92rem;margin:0">%s</p></div>' % f for f in PRICE_FACTORS)
    body = (
        page_head("Woven label pricing",
                  "Every order is priced to its specification. Here is what moves the price, and how to get an exact "
                  "number in one message.",
                  crumbs=[("", "Home"), ("pricing/", "Pricing")], depth=d)
        + '<section class="section"><div class="wrap">' + table +
        '<div class="sec-head"><div class="thread-rule"></div><h2>What affects the price</h2>'
        '<p>Minimum order is %s for apparel labels and %s for school monograms.</p></div>' % (MOQ_APPAREL, MOQ_SCHOOL) +
        '<div class="grid g-3">' + cards + '</div></div></section>'
        + cta_band(d, "Get an exact price",
                   "Send your logo, label type, rough size and quantity on WhatsApp and we will quote in one reply.")
    )
    return page("pricing/", "Woven Label Pricing Guide | Premium Woven Labels",
                "What affects the price of custom woven labels: size, colours, fold, material and quantity, and how to get "
                "an exact quote.", body, depth=d)


# ============================================================ ADDED: ad landing page (noindex)
import re
from core import wa, YEAR, CITY
from blocks import FAQS


def landing():
    d = 2
    WA = wa("Hi Premium Woven Labels, I would like a quote for custom woven labels. Label type: / Quantity: / Size:")
    up = "../../assets/img/real/"
    btn = '<a class="btn btn-wa btn-lg" href="' + WA + '" target="_blank" rel="noopener">Get a quote on WhatsApp</a>'
    shots = "".join('<img src="%s%s" alt="%s" loading="lazy" width="1200" height="1600">' % (up, f, a) for f, a in [
        ("gallery-honio.jpg", "Woven size labels for Honio Collection"),
        ("gallery-ica-monogram.jpg", "School monogram woven labels"),
        ("gallery-ribbon-set.jpg", "Set of woven ribbon labels")])
    faq = "".join("<details><summary>%s</summary><p>%s</p></details>" % qa for qa in FAQS[:3] + FAQS[-1:])
    body = (
        '<section class="lp-hero"><div class="wrap lp-grid"><div>'
        '<p class="lp-kicker">Custom woven labels &middot; Karachi, Pakistan</p>'
        '<h1>Custom woven labels for your brand. Get a quote in one message.</h1>'
        '<p class="lp-sub">Brand, care, size and logo labels for clothing brands and schools. Orders from '
        + MOQ_APPAREL + ', ready in ' + TURNAROUND + ' once your design is confirmed, and you approve a sample first.</p>'
        '<div class="lp-cta">' + btn + '<a class="textlink" href="#quote">or fill the form</a></div></div>'
        '<div class="lp-photo"><img src="' + up + 'gallery-aimen.jpg" alt="Custom woven labels by Premium Woven Labels" '
        'width="1200" height="1600"></div></div></section>'
        + re.sub(r'<p class="trust-note">.*?</p>', '', trust_strip()) +
        '<section class="section section--tight"><div class="wrap"><div class="sec-head"><div class="thread-rule"></div>'
        '<h2>Recent work</h2></div><div class="lp-shots">' + shots + '</div></div></section>'
        + testimonials_block() +
        '<section class="section" id="quote"><div class="wrap">' + quote_form(d) + '</div></section>'
        '<section class="section section--tight"><div class="wrap lp-faq"><div class="sec-head"><div class="thread-rule"></div>'
        '<h2>Quick answers</h2></div>' + faq + '</div></section>'
        '<section class="section"><div class="wrap" style="text-align:center"><h2>Ready to order your labels?</h2>'
        '<p style="color:var(--slate)">Send your logo, label type, size and quantity. We reply with a quote.</p>' + btn + '</div></section>'
    )
    html = page("lp/woven-labels-pakistan/", "Custom Woven Labels in Pakistan | Free Quote",
                "Custom woven brand, care and size labels for clothing brands and schools. Quick quote on WhatsApp.",
                body, depth=d, noindex=True)
    brand = re.search(r'<a class="brand".*?</a>', html, re.S).group(0)
    head = ('<a class="skip" href="#main">Skip to content</a><header class="site-head"><div class="wrap head-inner">' + brand +
            '<div class="head-cta"><a class="btn btn-wa btn-sm" href="' + WA + '" target="_blank" rel="noopener">WhatsApp us</a>'
            '<button class="menu-btn" type="button" style="display:none" tabindex="-1" aria-hidden="true"></button></div></div></header>'
            '<div class="m-menu" id="mobileMenu" aria-hidden="true" style="display:none"></div>\n')
    foot = ('<footer class="lp-foot"><div class="wrap"><p>&copy; ' + str(YEAR) + ' Premium Woven Labels &middot; ' + CITY +
            ', Pakistan &middot; <a href="../../privacy-policy/">Privacy</a> &middot; <a href="../../terms/">Terms</a></p></div></footer>')
    html = re.sub(r'<a class="skip".*?(?=<main id="main">)', lambda m: head, html, count=1, flags=re.S)
    return re.sub(r'<footer class="site-foot">.*?</footer>', lambda m: foot, html, count=1, flags=re.S)


# ============================================================ ADDED: label placement guide (caps, gloves, totes, etc.)
def label_placement_guide():
    d = 1
    groups_html = "".join(
        '<section class="section' + (' section--bone' if i % 2 else '') + '"><div class="wrap">'
        '<div class="sec-head"><div class="thread-rule"></div><h2>' + group_name + '</h2></div>'
        + faq_block(items, open_first=(i == 0)) +
        '</div></section>'
        for i, (group_name, items) in enumerate(PLACEMENT_FAQ_GROUPS)
    )
    body = (
        page_head("Where to put a woven label: size & placement guide",
                  "Starting points for size, placement and fold style on caps, gloves, shawls, scarves, crochet, "
                  "beanies, tote bags and blankets \u2014 not just garments.",
                  crumbs=[("", "Home"), ("label-placement-guide/", "Placement Guide")], depth=d)

        + ('<section class="section"><div class="wrap">'
           '<p style="color:var(--slate);max-width:68ch">The sizes below are practical starting points, not fixed '
           'standards \u2014 they refer to the label\u2019s visible finished area, and we add the material needed for '
           'the fold or seam insertion. Fold styles referenced here (Straight Cut, Centre Fold, End Fold) match the '
           'options on our <a class="textlink" href="' + url("woven-labels/", d) + '">Woven Labels</a> page. Tell us '
           'the exact item and we\u2019ll confirm size, placement and fold before production.</p>'
           '</div></section>')

        + groups_html

        + cta_band(d, "Not sure how your item should be labelled?",
                   "Send us a photo of the item and we'll suggest the size, placement and fold that works \u2014 free, no obligation.")
    )
    return page(
        "label-placement-guide/", "Woven Label Placement Guide: Caps, Gloves, Totes & More",
        "Where to sew a woven label and what size to use on caps, gloves, shawls, scarves, crochet, beanies, tote "
        "bags and blankets, with fold style recommendations for each.",
        body, depth=d,
        schema=[breadcrumbs([("", "Home"), ("label-placement-guide/", "Placement Guide")], d),
                faq_schema(PLACEMENT_FAQ_FLAT, "label-placement-guide/")]
    )


# ============================================================ ADDED: UAE / international orders page
def international():
    d = 1
    wa_link = wa("Hi Premium Woven Labels, I'd like a quote for an international order. Country: / Label type: / Quantity:")
    facts = [
        ("Ships via", "Skynet Worldwide Express"),
        ("Typical transit to UAE", "2\u20134 days"),
        ("Payment", "Payoneer (AED local transfer) or bank wire"),
        ("Minimum order", MOQ_APPAREL + " apparel / " + MOQ_SCHOOL + " school monogram"),
    ]
    fact_cards = "".join(
        '<div class="trust-item"><b>%s</b><span>%s</span></div>' % f for f in facts)
    steps_html = "".join(
        '<div class="prod-card reveal d%d" style="padding:24px"><h3 style="font-size:1rem">%d. %s</h3>'
        '<p style="color:var(--slate);font-size:.9rem;margin:0">%s</p></div>' % (i % 4 + 1, i + 1, t, dsc)
        for i, (t, dsc) in enumerate([
            ("Send your details", "Logo, label type, size and quantity on WhatsApp \u2014 tell us your country."),
            ("Get a quote", "We quote per country and quantity, since export rates differ from local Pakistan rates."),
            ("Approve a sample", "Nothing goes into full production until you've signed off on the design."),
            ("Pay via Payoneer or wire", "AED local transfer through Payoneer is the simplest option for UAE clients."),
            ("Production", "7\u201310 days once the design, size and quantity are confirmed."),
            ("Shipped via Skynet", "Typically 2\u20134 days in transit to the UAE."),
        ]))

    body = (
        page_head("Custom woven labels for UAE & international orders",
                  "Pakistan-manufactured woven labels, shipped to the UAE and internationally. Same quality, "
                  "sample-first process and minimums as our local orders.",
                  crumbs=[("", "Home"), ("international/", "International Orders")], depth=d)

        + ('<section class="trust" aria-label="International order essentials"><div class="wrap">'
           '<div class="trust-grid">' + fact_cards + '</div></div></section>')

        + ('<section class="section"><div class="wrap">'
           '<div class="sec-head"><div class="thread-rule"></div><h2>How an international order works</h2></div>'
           '<div class="grid g-4">' + steps_html + '</div>'
           '<p style="margin-top:28px"><a class="btn btn-wa" href="' + wa_link + '" target="_blank" rel="noopener">'
           'Start an international quote on WhatsApp</a></p>'
           '</div></section>')

        + ('<section class="section section--bone"><div class="wrap">'
           '<div class="sec-head"><div class="thread-rule"></div><h2>Why order from Pakistan</h2></div>'
           '<div class="grid g-3">'
           '<div class="prod-card reveal" style="padding:24px"><h3 style="font-size:1rem">Direct from the manufacturer</h3>'
           '<p style="color:var(--slate);font-size:.9rem;margin:0">You order from the workshop that weaves the '
           'labels, not a reseller \u2014 the same team your sample and your bulk order come from.</p></div>'
           '<div class="prod-card reveal d1" style="padding:24px"><h3 style="font-size:1rem">Low minimum, by volume</h3>'
           '<p style="color:var(--slate);font-size:.9rem;margin:0">A 1,000-piece minimum keeps the per-piece rate '
           'low for a full production run, rather than pricing each order like a one-off sample.</p></div>'
           '<div class="prod-card reveal d2" style="padding:24px"><h3 style="font-size:1rem">Sample before bulk</h3>'
           '<p style="color:var(--slate);font-size:.9rem;margin:0">You see and approve a sample before the full '
           'quantity is woven, wherever in the world it\u2019s shipping to.</p></div>'
           '</div></div></section>')

        + ('<section class="section"><div class="wrap">'
           '<div class="sec-head"><div class="thread-rule"></div><h2>Questions about international orders</h2></div>'
           + faq_block(INTL_FAQ, open_first=True) +
           '</div></section>')

        + cta_band(d, "Ordering from outside Pakistan?",
                   "Send your country, label type and quantity on WhatsApp and we'll quote it directly.")
    )
    return page(
        "international/", "Custom Woven Labels for UAE & Export Orders",
        "Pakistan-made woven labels shipped to the UAE and internationally via Skynet, typically 2-4 days to the "
        "UAE. Payoneer (AED) and bank wire accepted.",
        body, depth=d,
        schema=[breadcrumbs([("", "Home"), ("international/", "International Orders")], d),
                faq_schema(INTL_FAQ, "international/")]
    )


# ============================================================ ADDED: dedicated page per label type
# slug -> (PRODUCTS anchor, URL slug, fold names to feature, placement-guide labels to show, extra FAQ questions from FAQS/WOVEN_FAQ/INTL_FAQ by text)
LABEL_TYPE_PAGES = [
    ("brand-labels", "brand-labels", ["Centre Fold", "Straight Cut (Flat)"], ["Neck / brand label"],
     ["What is the difference between woven and printed labels?", "What file formats do you accept for artwork?"]),
    ("logo-labels", "logo-labels", ["Straight Cut (Flat)", "Mitre Fold"], ["Neck / brand label"],
     ["What file formats do you accept for artwork?", "Can I order custom-shaped labels?"]),
    ("size-labels", "size-labels", ["End Fold", "Straight Cut (Flat)"], ["Size label"],
     ["What is the minimum order quantity?", "Do you offer sew-on and iron-on backing?"]),
    ("care-labels", "care-labels", ["End Fold", "Straight Cut (Flat)"], ["Care label"],
     ["Will the colours and design survive washing?", "Do you make labels for exporters and garment manufacturers?"]),
    ("hang-tags", "hang-tags", ["Mitre Fold", "Straight Cut (Flat)"], ["Hang tag"],
     ["Can I see a sample before placing the full order?", "What file formats do you accept for artwork?"]),
    ("monograms", "school-monograms", ["Straight Cut (Flat)", "Centre Fold"], ["Monogram / crest"],
     ["Is a woven monogram better than an embroidered or printed school badge?", "What is a typical size for a school uniform monogram?"]),
]

_ALL_FAQ_BY_Q = {q: (q, a) for q, a in (FAQS + INTL_FAQ)}


def label_type_page(anchor, slug, fold_names, placement_labels, faq_questions):
    d = 1
    entry = next(p for p in PRODUCTS if p[0] == anchor)
    _, name, blurb, audience, svg = entry
    fold_rows = [f for f in FOLDS if f[0] in fold_names]
    fold_html = "".join(
        '<div class="prod-card reveal d%d" style="padding:24px"><h3 style="font-size:1rem">%s</h3>'
        '<p style="color:var(--slate);font-size:.9rem;margin:0 0 8px">%s</p>'
        '<p style="font-size:.8rem;font-weight:700;color:var(--red);margin:0">Best for: %s</p></div>'
        % (i % 3 + 1, fn, fd, fu) for i, (fn, fd, fu) in enumerate(fold_rows))
    placement_rows = [r for r in PLACEMENT_GUIDE if r[0] in placement_labels]
    placement_html = "".join("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % r for r in placement_rows)
    faqs = [_ALL_FAQ_BY_Q[q] for q in faq_questions if q in _ALL_FAQ_BY_Q]
    faq_html = faq_block(faqs, open_first=True) if faqs else ""
    moq = MOQ_SCHOOL if anchor == "monograms" else MOQ_APPAREL
    extra_note = ""
    if anchor == "monograms":
        extra_note = ('<p style="color:var(--slate)">Shapes available: ' + ", ".join(MONOGRAM_SHAPES) +
                       '. Backing: ' + " or ".join(x.lower() for x in MONOGRAM_BACKING) + '.</p>')
    wa_link = wa("Hi Premium Woven Labels, I'd like a quote for " + name.lower() + ". Quantity: / Size:")

    body = (
        page_head(name, blurb, crumbs=[("", "Home"), ("woven-labels/", "Woven Labels"), (slug + "/", name)], depth=d)

        + ('<section class="section"><div class="wrap">'
           '<div class="trust-grid" style="margin-bottom:0">'
           '<div class="trust-item"><b>' + moq + '</b><span>Minimum order</span></div>'
           '<div class="trust-item"><b>' + TURNAROUND + '</b><span>Production time</span></div>'
           '<div class="trust-item"><b>Sample first</b><span>Approved before full production</span></div>'
           '<div class="trust-item"><b>' + audience + '</b><span>Typically ordered by</span></div>'
           '</div>' + extra_note + '</div></section>')

        + (('<section class="section section--bone"><div class="wrap">'
            '<div class="sec-head"><div class="thread-rule"></div><h2>Placement and size</h2>'
            '<p>A starting point \u2014 we confirm exact size once we see your design.</p></div>'
            '<div class="table-wrap"><table class="price-table"><thead><tr>'
            '<th>Label</th><th>Typical placement</th><th>Starting point for size</th></tr></thead><tbody>'
            + placement_html + '</tbody></table></div></div></section>') if placement_html else "")

        + ('<section class="section"><div class="wrap">'
           '<div class="sec-head"><div class="thread-rule"></div><h2>Fold options for ' + name.lower() + '</h2></div>'
           '<div class="grid g-3">' + fold_html + '</div>'
           '<p style="margin-top:20px"><a class="textlink" href="' + url("woven-labels/", d) +
           '">See all fold styles</a></p></div></section>')

        + (('<section class="section section--bone"><div class="wrap">'
            '<div class="sec-head"><div class="thread-rule"></div><h2>Questions about ' + name.lower() + '</h2></div>'
            + faq_html + '</div></section>') if faq_html else "")

        + cta_band(d, "Need " + name.lower() + "?",
                   "Send your logo, size and quantity on WhatsApp and we'll quote it free.")
    )
    return page(
        slug + "/", name + " | Premium Woven Labels",
        blurb[:150],
        body, depth=d,
        schema=[breadcrumbs([("", "Home"), ("woven-labels/", "Woven Labels"), (slug + "/", name)], d)]
             + ([faq_schema(faqs, slug + "/")] if faqs else [])
    )

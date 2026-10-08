# -*- coding: utf-8 -*-
"""Resource centre: index + long-form articles."""

from core import (page, url, wa, canonical, label_svg, cta_band, breadcrumbs, crumb_html, faq_schema,
                  ICON_WA, BASE, NAME, WA_DISPLAY, EMAIL, MOQ_APPAREL, MOQ_SCHOOL, TURNAROUND, AUTHOR_NAME)

PUB_DATE = "2026-09-19"

SEO_TITLES = {
    "woven-vs-printed-labels": "Woven vs Printed Labels: Which to Choose",
    "custom-woven-label-guide": "The Complete Guide to Custom Woven Labels",
    "woven-label-size-guide": "How to Choose a Woven Label Size",
    "center-fold-vs-end-fold": "Centre Fold vs End Fold Woven Labels",
    "prepare-logo-for-woven-labels": "How to Prepare a Logo for Woven Labels",
    "woven-labels-for-clothing-brands": "Woven Labels for Clothing Brands",
    "woven-labels-brand-presentation": "How Woven Labels Improve Presentation",
    "custom-brand-labels-small-business": "Custom Brand Labels for Small Businesses",
    "ai-generated-logo-to-woven-label": "AI-Generated Logo to Woven Label or Badge",
}

GUIDE_SLUG = "woven-labels-complete-guide"
GUIDE_DATE = "2026-09-29"
import os as _os
import guide as _guide
_G = _guide.render(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "content", GUIDE_SLUG + ".md"))

# NOTE: the art_* functions read ARTICLES[0..8] by position - always add new articles at the END.
ARTICLES = [
    ("woven-vs-printed-labels", "Woven labels vs printed labels: which does your brand need?",
     "A plain comparison of woven and printed clothing labels \u2014 how each is made, how they feel, how they wear, "
     "and which suits brand labels, care labels and hang tags.",
     "8 min read"),
    ("custom-woven-label-guide", "The complete guide to custom woven labels",
     "Everything that goes into a custom woven label order: label types, fold styles, sizing, artwork, thread colours "
     "and what to send when you ask for a quote.",
     "11 min read"),
    ("woven-label-size-guide", "How to choose the right woven label size",
     "Practical guidance on sizing woven labels for necklines, side seams, care labels and hang tags \u2014 and how to "
     "check a size before you order.",
     "7 min read"),
    ("center-fold-vs-end-fold", "Centre fold vs end fold woven labels",
     "The two most common woven label folds, what each one looks like once it's sewn in, and how to pick between them.",
     "6 min read"),
    ("prepare-logo-for-woven-labels", "How to prepare your logo for woven labels",
     "What file to send, what to simplify, and how to check your logo will still read clearly once it\u2019s woven at "
     "label size.",
     "8 min read"),
    ("woven-labels-for-clothing-brands", "Woven labels for clothing brands: what to order and where it goes",
     "The labels a clothing brand actually needs \u2014 neck, side seam, size, care and hang tag \u2014 and how to "
     "order them as one coordinated set.",
     "9 min read"),
    ("woven-labels-brand-presentation", "How woven labels improve brand presentation",
     "Why the label inside a garment does more brand work than most owners expect, and what a considered label "
     "changes about how a product is perceived.",
     "6 min read"),
    ("custom-brand-labels-small-business", "Custom brand labels for small businesses",
     "How small and handmade businesses approach their first label order \u2014 what to decide, what to skip for now, "
     "and how to keep it simple.",
     "7 min read"),
    ("ai-generated-logo-to-woven-label",
     "How to turn an AI-generated logo or monogram into a woven label or badge",
     "You designed it in ChatGPT, Midjourney or DALL\u00b7E \u2014 here\u2019s how to send it to us and what "
     "to expect when we weave it.",
     "7 min read"),
    (GUIDE_SLUG, _G["title"], _G["desc"], "%d min read" % _G["mins"]),
]


def _article_shell(slug, title, desc, read, lead, toc, body_html, extra_schema=None, pub_date=None):
    d = 2
    crumbs = [("", "Home"), ("resources/", "Resources"), ("resources/%s/" % slug, title)]
    head = (
        ('<section class="page-head"><div class="wrap">%s'
         '<p style="font-size:.84rem;color:#8d97c2;margin-bottom:12px">%s &middot; By ' + AUTHOR_NAME + ', Premium Woven Labels</p>')
        % (crumb_html([("", "Home"), ("resources/", "Resources"), ("resources/%s/" % slug, "Article")], d), read)
        + ('<h1 style="max-width:26ch">%s</h1><p>%s</p></div></section>' % (title, desc))
    )
    toc_html = ""
    if toc:
        toc_html = ('<nav class="toc" aria-label="On this page"><b>On this page</b><ol>%s</ol></nav>'
                    % "".join('<li><a href="#%s">%s</a></li>' % (a, t) for a, t in toc))

    lead_html = "<p>%s</p>" % lead if lead else ""
    body = (
        head
        + '<section class="section"><div class="wrap"><div class="prose">%s%s%s</div>'
          '<div style="max-width:70ch;margin-top:46px;padding:28px;border-radius:22px;background:var(--bone)">'
          '<h3 style="margin-top:0">Need a quote?</h3>'
          '<p style="color:var(--slate)">Send your logo on WhatsApp and we\u2019ll tell you how it translates into '
          'thread, which fold suits it, and what it costs. Free, with no obligation.</p>'
          '<div class="btn-row"><a class="btn btn-wa" href="%s" target="_blank" rel="noopener">%s Chat on WhatsApp</a>'
          '<a class="btn btn-ghost" href="%s">Get a free quote</a></div></div>'
          '</div></section>' % (toc_html, lead_html, body_html, wa(), ICON_WA, url("contact/", d))
        + _related(slug, d)
        + cta_band(d)
    )

    schema = [breadcrumbs(crumbs, d),
              {"@type": "Article", "@id": canonical("resources/%s/" % slug) + "#article",
               "headline": title, "description": desc,
               "mainEntityOfPage": {"@id": canonical("resources/%s/" % slug)},
               "author": {"@type": "Person", "name": AUTHOR_NAME},
               "publisher": {"@id": BASE + "/#organization"},
               "datePublished": pub_date or PUB_DATE, "dateModified": pub_date or PUB_DATE,
               "image": BASE + "/assets/img/og-cover.png", "inLanguage": "en"}]
    if extra_schema:
        schema.extend(extra_schema)
    return page("resources/%s/" % slug, SEO_TITLES.get(slug, title) + " | " + NAME, desc, body, depth=d,
                active=("resources/%s/" % slug if slug == GUIDE_SLUG else "resources/"), schema=schema, og_type="article")


def _related(current, depth):
    idx = [a[0] for a in ARTICLES].index(current)
    others = [ARTICLES[(idx + n) % len(ARTICLES)] for n in (1, 2, 3)]
    cards = "".join(
        '<a class="post-card reveal d%d" href="%s"><span class="post-thumb"></span>'
        '<span class="post-body"><span class="post-meta">%s</span><h3>%s</h3><p>%s</p></span></a>'
        % (i + 1, url("resources/%s/" % s, depth), r, t, d_)
        for i, (s, t, d_, r) in enumerate(others))
    return ('<section class="section section--bone"><div class="wrap">'
            '<div class="sec-head"><div class="thread-rule"></div><h2>Keep reading</h2></div>'
            '<div class="grid g-3">%s</div></div></section>' % cards)


# ============================================================ index
def resources_index():
    d = 1
    cards = "".join(
        '<a class="post-card reveal d%d" href="%s"><span class="post-thumb"></span>'
        '<span class="post-body"><span class="post-meta">%s</span><h3>%s</h3><p>%s</p></span></a>'
        % (i + 1, url("resources/%s/" % s, d), r, t, desc)
        for i, (s, t, desc, r) in enumerate([ARTICLES[-1]] + ARTICLES[:-1]))

    body = (
        '<section class="page-head"><div class="wrap">%s'
        '<h1>Guides to getting your labels right</h1>'
        '<p>Practical, no-nonsense guides on woven labels \u2014 how they\u2019re made, how to size them, which fold to '
        'choose and how to prepare your artwork.</p></div></section>'
        % crumb_html([("", "Home"), ("resources/", "Resources")], d)
        + '<section class="section"><div class="wrap">'
          '<div class="sec-head"><div class="thread-rule"></div><h2>Latest guides</h2></div>'
          '<div class="grid g-2">%s</div>'
          '<p class="custom-note" style="margin-top:34px">More guides are being added. If there\u2019s something you want '
          'explained, <a class="textlink" href="%s">ask us on WhatsApp</a> and we\u2019ll answer directly.</p>'
          '</div></section>' % (cards, wa())
        + cta_band(d)
    )
    return page(
        "resources/", "Woven Label Guides & Resources | Premium Woven Labels",
        "Guides to custom woven labels: woven vs printed, choosing a label size, centre fold vs end fold, and how to "
        "prepare your logo for weaving.",
        body, depth=d,
        schema=[breadcrumbs([("", "Home"), ("resources/", "Resources")], d),
                {"@type": "CollectionPage", "@id": canonical("resources/") + "#webpage",
                 "url": canonical("resources/"), "name": "Woven label guides and resources",
                 "isPartOf": {"@id": BASE + "/#website"}}]
    )


# ============================================================ article 1
def art_woven_vs_printed():
    s, t, desc, read = ARTICLES[0]
    lead = ("If you're ordering labels for a clothing brand for the first time, the choice between woven and printed "
            "is the first real decision you'll make. It changes how your label looks, how it feels, and how it holds "
            "up after fifty washes. Here's the honest comparison.")
    toc = [("how-made", "How each one is made"),
           ("feel", "How they feel and look"),
           ("detail", "Which handles your logo better"),
           ("wear", "How they wear"),
           ("use", "Which to use where"),
           ("choose", "How to choose")]
    body = (
        '<h2 id="how-made">How each one is made</h2>'
        '<p>A <strong>woven label</strong> is made on a loom. Coloured threads are woven together so that your logo, '
        'brand name and text emerge from the weave itself. The design isn\u2019t applied to the fabric \u2014 the design '
        '<em>is</em> the fabric. That\u2019s the whole distinction, and everything else follows from it.</p>'
        '<p>A <strong>printed label</strong> starts with a base material \u2014 usually satin, cotton tape or a synthetic '
        'ribbon \u2014 and the design is printed onto it with ink. The material is made first; the design goes on top '
        'afterwards.</p>'

        '<h2 id="feel">How they feel and look</h2>'
        '<p>Run your thumb over a woven label and you can feel the threads. There\u2019s a slight texture and a subtle '
        'depth where the colours change. It\u2019s the finish most people associate with established retail clothing, '
        'because that\u2019s what established retail clothing uses.</p>'
        '<p>A printed label is flat and smooth. The surface is uniform, and the design sits on it. Neither is "better" '
        'in the abstract \u2014 but they read differently, and customers pick up on it even when they can\u2019t name '
        'what they noticed.</p>'
        '<blockquote><p>The short version: woven feels made. Printed feels applied.</p></blockquote>'

        '<h2 id="detail">Which handles your logo better</h2>'
        '<p>Thread has a minimum thickness, so there\u2019s a floor on how fine a woven detail can go. Hairline strokes, '
        'very small serif type and thin outlines may need simplifying at label size. In exchange, what does get woven '
        'stays crisp \u2014 edges are defined by where one thread ends and another begins.</p>'
        '<p>Printing can reproduce gradients, photographic imagery and extremely fine lines that thread cannot. If your '
        'logo depends on a photographic element or a soft gradient blend, printing handles it more faithfully.</p>'
        '<p>Most brand marks \u2014 a wordmark, a monogram, a simple icon \u2014 weave well. A focused palette, generally '
        'around 10 to 12 thread colours, covers most logos and text cleanly. Send us your artwork and we\u2019ll tell you '
        'exactly how it translates before you commit to anything.</p>'

        '<h2 id="wear">How they wear</h2>'
        '<p>Because a woven design is built into the threads, normal washing and drying doesn\u2019t lift it off the '
        'material \u2014 there\u2019s no printed layer to crack or peel, and the colours are the threads themselves.</p>'
        '<p>Printed labels vary more with the print method and base material. Some printing holds up well; some shows '
        'wear on the printed surface over repeated washing. If your garment is washed often, that difference matters.</p>'

        '<h2 id="use">Which to use where</h2>'
        '<div class="table-scroll"><table class="key-table">'
        '<caption class="sr-only">Where woven and printed labels are typically used</caption>'
        '<thead><tr><th scope="col">Where it goes</th><th scope="col">Usually</th><th scope="col">Why</th></tr></thead>'
        '<tbody>'
        '<tr><th scope="row">Neck / brand label</th><td>Woven</td><td>It\u2019s the label a customer sees and touches first.</td></tr>'
        '<tr><th scope="row">Side-seam tab</th><td>Woven</td><td>Visible on the outside; the texture is part of the look.</td></tr>'
        '<tr><th scope="row">Size label</th><td>Woven</td><td>Short text, needs to stay legible for the life of the garment.</td></tr>'
        '<tr><th scope="row">Care label</th><td>Either</td><td>Woven lasts; printing fits more small text in less space.</td></tr>'
        '<tr><th scope="row">Hang tag</th><td>Woven</td><td>Read at arm\u2019s length on the rail; texture carries.</td></tr>'
        '<tr><th scope="row">Photographic artwork</th><td>Printed</td><td>Gradients and photo detail don\u2019t translate into thread.</td></tr>'
        '</tbody></table></div>'

        '<h2 id="choose">How to choose</h2>'
        '<p>Ask three questions:</p>'
        '<ol>'
        '<li><strong>Where does the label sit?</strong> If a customer will see or touch it, woven usually wins.</li>'
        '<li><strong>What does your logo contain?</strong> Solid shapes and type weave well. Photographs and gradients don\u2019t.</li>'
        '<li><strong>How often is the garment washed?</strong> The more washing, the more the woven construction earns its place.</li>'
        '</ol>'
        '<p>If you\u2019re still unsure, send us the logo. We\u2019ll tell you how it would come out in thread \u2014 '
        'including if we think printing suits your artwork better.</p>'
    )
    return _article_shell(s, t, desc, read, lead, toc, body)


# ============================================================ article 2
def art_guide():
    s, t, desc, read = ARTICLES[1]
    lead = ("A custom woven label order comes down to six decisions: type, size, shape, fold, thread colours and "
            "quantity. This guide walks through each one so you know what you're choosing and what to send us.")
    toc = [("what", "What a woven label actually is"),
           ("types", "1. Label type"),
           ("size", "2. Size"),
           ("shape", "3. Shape"),
           ("fold", "4. Fold style"),
           ("colour", "5. Thread colours"),
           ("qty", "6. Quantity"),
           ("artwork", "Preparing your artwork"),
           ("order", "Placing the order")]
    body = (
        '<h2 id="what">What a woven label actually is</h2>'
        '<p>A woven label is a small piece of fabric made on a loom, where coloured threads are woven together to form '
        'your logo, brand name or text. Nothing is printed on \u2014 the design is part of the material.</p>'
        '<p>That construction is why woven labels are the standard on retail clothing: the branding is as durable as '
        'the fabric it\u2019s made from.</p>'

        '<h2 id="types">1. Label type</h2>'
        '<p>Most brands order two or three types together so the set matches.</p>'
        '<ul>'
        '<li><strong>Brand label</strong> \u2014 your name or logo, usually at the neck or in the side seam. The one '
        'people mean when they say "clothing label".</li>'
        '<li><strong>Logo woven label</strong> \u2014 the same idea, built around a logo mark rather than a wordmark.</li>'
        '<li><strong>Size label</strong> \u2014 XS to XXL, numeric sizing, or your own system.</li>'
        '<li><strong>Care label</strong> \u2014 washing instructions, fabric composition, country of manufacture, care symbols.</li>'
        '<li><strong>Hang tag</strong> \u2014 hangs on the outside, read on the rail before the garment is handled.</li>'
        '<li><strong>Monogram or crest</strong> \u2014 for school uniforms, blazers and sportswear.</li>'
        '</ul>'

        '<h2 id="size">2. Size</h2>'
        '<p>Labels are made to your measurements rather than fixed sizes. The size is driven by two things: where the '
        'label sits, and how much text has to stay readable.</p>'
        '<p>A neck label has to fit the neckline without curling at the edges or crowding the seam. A care label is '
        'usually smaller and often sits stacked with the size label. A hang tag is larger because it\u2019s read from '
        'further away.</p>'
        '<p>If you\u2019re not sure, tell us the garment and where the label goes \u2014 we\u2019ll suggest a size. '
        'There\u2019s a fuller walkthrough in our <a href="../woven-label-size-guide/">label size guide</a>.</p>'

        '<h2 id="shape">3. Shape</h2>'
        '<p>Rectangular is the default and suits most brand, size and care labels. Rounded corners soften the look and '
        'sit well in a neckline. Square works for size markers and compact logo marks. A custom shape is cut to an '
        'outline that follows your logo \u2014 useful for badges, crests and shaped marks, and the most distinctive '
        'option if your logo has a strong silhouette.</p>'

        '<h2 id="fold">4. Fold style</h2>'
        '<p>The fold decides how the label is sewn in and how much of it shows.</p>'
        '<div class="table-scroll"><table class="key-table">'
        '<caption class="sr-only">Woven label fold styles</caption>'
        '<thead><tr><th scope="col">Fold</th><th scope="col">What happens</th><th scope="col">Typically used for</th></tr></thead>'
        '<tbody>'
        '<tr><th scope="row">Flat woven</th><td>No fold; sewn down on all sides or top and bottom.</td><td>Patches, hang tags, visible labels</td></tr>'
        '<tr><th scope="row">Centre fold</th><td>Folded in half; the back is hidden inside the seam.</td><td>Neck labels, side-seam brand labels</td></tr>'
        '<tr><th scope="row">End fold</th><td>Short ends folded under; no raw edges on the sides.</td><td>Neck, care and size labels</td></tr>'
        '<tr><th scope="row">Mitre Fold</th><td>All four corners mitred and folded under for a neat tailored finish on every edge.</td><td>Premium labels and hang tags</td></tr><tr><th scope="row">Manhattan Fold</th><td>One end folded over, the other sewn open into the seam.</td><td>Waistband and hem labels</td></tr>'
        '</tbody></table></div>'
        '<p>Centre fold and end fold cover most orders. There\u2019s a direct comparison in '
        '<a href="../center-fold-vs-end-fold/">centre fold vs end fold</a>.</p>'

        '<h2 id="colour">5. Thread colours</h2>'
        '<p>You choose the background and the thread colours. We match your brand colours as closely as the weaving '
        'process allows \u2014 thread is dyed, so it doesn\u2019t behave exactly like ink or a screen colour, and we\u2019ll '
        'tell you honestly where a shade will shift slightly.</p>'
        '<p>Keep the palette focused. Generally, around 10 to 12 thread colours captures most logos and text cleanly. '
        'Fewer colours often looks sharper at label size than more.</p>'

        '<h2 id="qty">6. Quantity</h2>'
        '<p>Minimum order quantities apply and depend on the label type. Tell us roughly how many you need and we\u2019ll '
        'confirm what works before you commit \u2014 there\u2019s no obligation in asking.</p>'

        '<h2 id="artwork">Preparing your artwork</h2>'
        '<ul>'
        '<li><strong>Vector is best.</strong> AI, EPS, SVG or PDF files stay sharp at any size.</li>'
        '<li><strong>High-resolution raster works to start.</strong> A clear PNG or JPG is enough for us to assess it.</li>'
        '<li><strong>Simplify fine detail.</strong> Hairline strokes and very small type may need thickening to read in thread.</li>'
        '<li><strong>Send your colour codes.</strong> Pantone, HEX or RGB \u2014 whatever you have.</li>'
        '<li><strong>Include the text exactly as you want it woven.</strong> Spelling, capitalisation, spacing.</li>'
        '</ul>'

        '<h2 id="order">Placing the order</h2>'
        '<p>Message us on WhatsApp at %s or email %s with your artwork, label type and rough quantity. We go through '
        'the options with you, you approve a sample, and only then does the full order go into production.</p>'
        % (WA_DISPLAY, EMAIL)
    )
    return _article_shell(s, t, desc, read, lead, toc, body)


# ============================================================ article 3
def art_size():
    s, t, desc, read = ARTICLES[2]
    lead = ("Label size is the decision people most often get wrong on a first order \u2014 usually by going too big. "
            "Here's how to work out what fits, and how to check it before you order.")
    toc = [("start", "Start with the garment"),
           ("neck", "Neck and brand labels"),
           ("care", "Size and care labels"),
           ("tags", "Hang tags"),
           ("text", "Let the text set the floor"),
           ("check", "Check it before you order")]
    body = (
        '<h2 id="start">Start with the garment, not the logo</h2>'
        '<p>The instinct is to pick a size that makes the logo look good on screen. The better starting point is the '
        'garment: where exactly is the label being sewn, how wide is that seam, and how much room is there before the '
        'label starts to crowd or curl?</p>'
        '<p>A label that\u2019s too large for its seam bends at the edges, catches on skin and looks like an afterthought. '
        'A label that fits sits flat and reads as intentional.</p>'

        '<h2 id="neck">Neck and brand labels</h2>'
        '<p>The neck label carries your brand name, so it has to be readable \u2014 but it also sits against skin. It '
        'should span a comfortable portion of the neckline without reaching the shoulder seams, and it shouldn\u2019t be '
        'so tall that it folds when the neckline stretches.</p>'
        '<p>A wordmark reads best on a wider, shorter label. A stacked logo with a mark above text usually needs more '
        'height. Tell us which shape your logo is and we\u2019ll suggest proportions that work.</p>'

        '<h2 id="care">Size and care labels</h2>'
        '<p>These are functional, so they can be smaller. Size labels carry one or two characters and are often the '
        'smallest label in the set. Care labels carry more text \u2014 washing instructions, composition, country of '
        'manufacture \u2014 so the size is driven by how much information has to fit while staying legible.</p>'
        '<p>If your care label is getting crowded, the usual fixes are to use standard care symbols instead of words, '
        'or to move to a folded format that gives you more usable surface.</p>'

        '<h2 id="tags">Hang tags</h2>'
        '<p>Hang tags are read at arm\u2019s length on a rail, not at close range. They\u2019re typically the largest '
        'woven item in an order, and they can carry a bolder version of your mark because there\u2019s room for it.</p>'

        '<h2 id="text">Let the text set the floor</h2>'
        '<p>Thread has a minimum practical thickness, which puts a floor on how small your text can go and still read. '
        'In practice this means:</p>'
        '<ul>'
        '<li>Thin strokes may need thickening before they\u2019ll weave cleanly.</li>'
        '<li>Very small type may need to be set larger \u2014 or dropped \u2014 rather than shrunk.</li>'
        '<li>Tight letter spacing at small sizes can close up; a little extra spacing usually reads better in thread.</li>'
        '</ul>'
        '<p>Send us the artwork at the size you\u2019re considering and we\u2019ll tell you what holds and what doesn\u2019t.</p>'

        '<h2 id="check">Check it before you order</h2>'
        '<ol>'
        '<li><strong>Print it at 100%%.</strong> Print your label artwork at actual size on paper. On-screen size is misleading.</li>'
        '<li><strong>Cut it out and pin it.</strong> Put the paper version where the real label will go on the actual garment.</li>'
        '<li><strong>Step back.</strong> Look at it from normal viewing distance. Can you read the brand name?</li>'
        '<li><strong>Check the seam.</strong> Does it fit the seam allowance without bending or crowding?</li>'
        '<li><strong>Send us the measurement.</strong> Width and height in millimetres, and we\u2019ll confirm it works.</li>'
        '</ol>'
        '<p>It takes ten minutes and it\u2019s the single best way to avoid a full run of labels that are slightly wrong.</p>'
    )
    return _article_shell(s, t, desc, read, lead, toc, body)


# ============================================================ article 4
def art_folds():
    s, t, desc, read = ARTICLES[3]
    lead = ("Centre fold and end fold are the two folds most clothing labels use. They're sewn in differently, they "
            "look different once they're in, and the right one depends on where the label sits.")
    toc = [("centre", "Centre fold"),
           ("end", "End fold"),
           ("compare", "Side by side"),
           ("pick", "Which to pick")]
    body = (
        '<h2 id="centre">Centre fold</h2>'
        '<p>The label is woven at double length and folded in half across the middle. The front carries your design; '
        'the back half tucks inside the seam and isn\u2019t seen.</p>'
        '<p>Because both raw ends disappear into the seam, the finished label has a clean folded edge at the bottom and '
        'no visible cut edges. It\u2019s the most common choice for neck labels and side-seam brand labels.</p>'
        '<p>One thing to know: you\u2019re weaving twice the material for the visible area, because half of it is hidden.</p>'

        '<h2 id="end">End fold</h2>'
        '<p>The label is woven at its finished height, and the two short ends are folded under before sewing. The whole '
        'design stays visible, and the folded ends hide the cut edges at the sides.</p>'
        '<p>End fold labels sit flatter against the garment and are the usual choice when you want the full label face '
        'on show \u2014 care labels, size labels and neck labels where the design fills the width.</p>'

        '<h2 id="compare">Side by side</h2>'
        '<div class="table-scroll"><table class="key-table">'
        '<caption class="sr-only">Centre fold compared with end fold</caption>'
        '<thead><tr><th scope="col"></th><th scope="col">Centre fold</th><th scope="col">End fold</th></tr></thead>'
        '<tbody>'
        '<tr><th scope="row">How it folds</th><td>In half, across the middle</td><td>Both short ends tucked under</td></tr>'
        '<tr><th scope="row">Visible area</th><td>Front half only</td><td>Almost the whole label</td></tr>'
        '<tr><th scope="row">Finished edges</th><td>Folded edge at the bottom</td><td>Folded edges at the sides</td></tr>'
        '<tr><th scope="row">How it sits</th><td>Hangs from the seam</td><td>Lies flat against the fabric</td></tr>'
        '<tr><th scope="row">Common use</th><td>Neck labels, side-seam brand labels</td><td>Care labels, size labels, flat neck labels</td></tr>'
        '</tbody></table></div>'

        '<h2 id="pick">Which to pick</h2>'
        '<p>Two questions usually settle it:</p>'
        '<ol>'
        '<li><strong>Is the label sewn along one edge or across the whole face?</strong> Sewn along the top edge only '
        '\u2192 centre fold. Sewn down flat \u2192 end fold.</li>'
        '<li><strong>Does your design need the full label face?</strong> If the artwork fills the space, end fold keeps '
        'all of it visible.</li>'
        '</ol>'
        '<p>If you\u2019re still unsure, send us a photo of the garment and where the label is going. We\u2019ll tell you '
        'which fold your manufacturer will find easiest to sew and which will look right when it\u2019s in.</p>'
        '<p>All five folds are covered on our '
        '<a href="../../woven-labels/">woven labels page</a>.</p>'
    )
    return _article_shell(s, t, desc, read, lead, toc, body)


# ============================================================ article 5
def art_logo_prep():
    s, t, desc, read = ARTICLES[4]
    lead = ("Almost every delay on a label order comes from the same place: the artwork. Not because the logo is bad, "
            "but because a logo designed for a shopfront sign has to survive being rebuilt out of thread at four "
            "centimetres wide. Here is what to send and what to check first.")
    toc = [("file", "What file to send"),
           ("size", "Look at it at label size"),
           ("simplify", "What usually needs simplifying"),
           ("colour", "Thinking in thread colours"),
           ("text", "Text and legibility"),
           ("checklist", "A short checklist")]
    body = (
        '<h2 id="file">What file to send</h2>'
        '<p>Best case is a <strong>vector file</strong> \u2014 AI, EPS, SVG or a vector PDF. Vector artwork can be '
        'scaled to label size without losing edge definition, which makes it far easier to work out exactly where each '
        'thread boundary falls.</p>'
        '<p>If you don\u2019t have vector artwork, send the <strong>largest, cleanest raster file you own</strong> \u2014 '
        'a high-resolution PNG with a transparent or plain background, or a big JPG. A logo lifted off a website or '
        'screenshotted from Instagram is usually too small and too compressed to work from cleanly.</p>'
        '<p>You do not need to prepare anything special before you ask for a quote. Send what you have and we\u2019ll '
        'tell you whether it\u2019s workable, and what would need to change if it isn\u2019t.</p>'
        '<blockquote><p>Send the original file your designer gave you, not the version you exported for social media.</p></blockquote>'

        '<h2 id="size">Look at it at label size</h2>'
        '<p>This is the single most useful thing you can do, and it takes two minutes. Print your logo at the actual '
        'width you want the label to be \u2014 40mm, 50mm, whatever you have in mind \u2014 and put it on the table.</p>'
        '<p>At that size you\u2019ll immediately see what survives and what disappears: the tagline under the wordmark, '
        'the thin outline around the icon, the registered-trademark symbol. Anything you have to lean in to read on '
        'paper will be harder still in thread.</p>'
        '<p>If parts vanish, that\u2019s not a problem with your logo \u2014 it\u2019s a sign the label needs either a '
        'simplified version of it or a slightly larger size.</p>'

        '<h2 id="simplify">What usually needs simplifying</h2>'
        '<p>Thread has a minimum thickness, so there is a practical floor on fine detail. The things that most often '
        'need adjusting are:</p>'
        '<ul>'
        '<li><strong>Hairline strokes and thin outlines</strong> \u2014 these either thicken up or drop out entirely.</li>'
        '<li><strong>Gradients and soft shadows</strong> \u2014 thread is solid colour, so a gradient becomes a small '
        'number of flat steps or a single colour.</li>'
        '<li><strong>Photographic elements</strong> \u2014 these don\u2019t translate into weaving at all.</li>'
        '<li><strong>Very small secondary text</strong> \u2014 taglines, website addresses and establishment dates are '
        'the usual casualties.</li>'
        '<li><strong>Tight inner detail</strong> \u2014 fine gaps inside a monogram or crest may close up.</li>'
        '</ul>'
        '<p>Many brands end up with a slightly reduced <em>label version</em> of their logo: the mark and the name, with '
        'the smaller supporting elements removed. That is completely normal and it\u2019s what most established labels '
        'do too.</p>'

        '<h2 id="colour">Thinking in thread colours</h2>'
        '<p>Each colour in a woven label is a separate thread. A focused palette keeps the weave clean and the design '
        'readable. Most logos sit comfortably within a small set of colours \u2014 a background, the mark, and perhaps '
        'one accent.</p>'
        '<p>If you have brand colour references (Pantone numbers, or even just a swatch), send them. Thread is matched '
        'to the closest available colour rather than mixed to order, so we\u2019ll tell you how close a match is '
        'realistic before production rather than after.</p>'
        '<p>One practical tip: contrast matters more than exactness. A logo that is mid-grey on a slightly different '
        'mid-grey may be perfectly legible on screen and almost invisible in thread.</p>'

        '<h2 id="text">Text and legibility</h2>'
        '<p>Type behaves differently once woven. Chunky sans-serif and clean geometric type hold up well. Fine serifs, '
        'thin scripts and very condensed type are harder \u2014 the thin parts of each letter are exactly where thread '
        'runs out of room.</p>'
        '<p>If your brand uses a delicate typeface, you have a few options: set it slightly larger, weave it in higher '
        'contrast, or give the label a little more width so the letters can breathe. We\u2019ll flag which of these your '
        'artwork needs when we look at it.</p>'

        '<h2 id="checklist">A short checklist</h2>'
        '<ol>'
        '<li>Find the original vector file if one exists.</li>'
        '<li>Print the logo at your intended label width and look at it on paper.</li>'
        '<li>Decide what can be removed for the label version.</li>'
        '<li>Note your brand colours, if you have references.</li>'
        '<li>Decide roughly what size and fold you want \u2014 our '
        '<a href="../woven-label-size-guide/">size guide</a> and '
        '<a href="../center-fold-vs-end-fold/">fold comparison</a> cover both.</li>'
        '<li>Send it all on WhatsApp and we\u2019ll come back with how it translates.</li>'
        '</ol>'
        '<p>You don\u2019t have to get every one of these right before you contact us. The list is what a smooth order '
        'looks like, not a barrier to asking.</p>'
    )
    return _article_shell(s, t, desc, read, lead, toc, body)


# ============================================================ article 6
def art_clothing_brands():
    s, t, desc, read = ARTICLES[5]
    lead = ("A clothing brand rarely needs one label. It needs a small set that works together \u2014 the one people "
            "see, the one that tells them the size, and the one that tells them how to wash it. Here\u2019s how those "
            "pieces usually fit together.")
    toc = [("set", "The labels a brand usually orders"),
           ("neck", "Neck and brand labels"),
           ("seam", "Side-seam tabs"),
           ("size-care", "Size and care labels"),
           ("tags", "Hang tags"),
           ("together", "Ordering them as a set"),
           ("first", "If this is your first order")]
    body = (
        '<h2 id="set">The labels a brand usually orders</h2>'
        '<p>Most clothing brands end up with some combination of five things. You don\u2019t need all of them, and you '
        'certainly don\u2019t need all of them at once, but it helps to know what the full picture looks like.</p>'
        '<div class="table-scroll"><table class="key-table">'
        '<caption class="sr-only">Common label types for a clothing brand</caption>'
        '<thead><tr><th scope="col">Label</th><th scope="col">Where it goes</th><th scope="col">What it carries</th></tr></thead>'
        '<tbody>'
        '<tr><th scope="row">Brand / neck label</th><td>Inside back neck or waistband</td><td>Logo and brand name</td></tr>'
        '<tr><th scope="row">Side-seam tab</th><td>Outside the side seam or hem</td><td>Small mark or short wordmark</td></tr>'
        '<tr><th scope="row">Size label</th><td>Under the neck label, or in the seam</td><td>S, M, L, or numeric sizing</td></tr>'
        '<tr><th scope="row">Care label</th><td>Inside side seam</td><td>Wash symbols, fabric, origin</td></tr>'
        '<tr><th scope="row">Hang tag</th><td>Attached at the neck or cuff for display</td><td>Logo, retail presentation</td></tr>'
        '</tbody></table></div>'

        '<h2 id="neck">Neck and brand labels</h2>'
        '<p>This is the label that does the most work. It\u2019s what a customer sees when they pick the garment up, '
        'what they feel against the back of the neck, and what they look at again when they wonder where the piece came '
        'from.</p>'
        '<p>It usually carries the logo and the brand name and nothing else. Centre fold is the common choice here \u2014 '
        'it hangs from the seam with a clean folded bottom edge \u2014 though end fold works well when the design fills '
        'the full width and you want it sitting flat.</p>'

        '<h2 id="seam">Side-seam tabs</h2>'
        '<p>A small woven tab stitched into the outside seam or hem. It\u2019s visible when the garment is worn, which '
        'makes it a quiet piece of external branding \u2014 the kind of detail people notice on a well-made piece '
        'without consciously registering it.</p>'
        '<p>Because it\u2019s small, keep the artwork simple. A monogram, a short wordmark or an icon reads far better '
        'at tab size than a full lock-up with a tagline.</p>'

        '<h2 id="size-care">Size and care labels</h2>'
        '<p>Size labels are short, functional and need to stay legible for the life of the garment \u2014 which is '
        'exactly what woven construction is good at. They\u2019re often ordered as a set across your size range, so '
        'think about which sizes you\u2019re producing and in what proportion before you order.</p>'
        '<p>Care labels carry wash and care symbols, fabric composition and country of origin. They hold more '
        'information in less space than any other label on the garment, so they\u2019re typically wider or set as a '
        'multi-line label. What exactly must appear on a care label depends on where you\u2019re selling \u2014 worth '
        'checking your market\u2019s requirements before you finalise the wording.</p>'

        '<h2 id="tags">Hang tags</h2>'
        '<p>A hang tag is what does the selling on the rail. It\u2019s read from further away than a neck label, so it '
        'can carry a larger version of your mark and a little more presence. Woven hang tags have a texture and weight '
        'that card tags don\u2019t.</p>'

        '<h2 id="together">Ordering them as a set</h2>'
        '<p>The thing worth planning for: these labels look best when they share a visual language. The same thread '
        'palette, the same treatment of your mark, the same weight of type. A neck label in navy and gold followed by a '
        'care label in black and white reads as two different brands in the same garment.</p>'
        '<p>It\u2019s also usually simpler to decide the whole set once, even if you order the pieces at different '
        'times, so the second order matches the first.</p>'

        '<h2 id="first">If this is your first order</h2>'
        '<p>Start with the neck label. It carries the most brand weight and it\u2019s the one customers actually '
        'associate with your name. Size and care labels can follow once you\u2019ve seen how the first one turns out.</p>'
        '<p>Minimum order quantities apply and depend on the label type, so tell us roughly what you\u2019re producing '
        'and we\u2019ll tell you what\u2019s workable. Our <a href="../custom-woven-label-guide/">complete guide</a> '
        'walks through the full set of decisions, and the '
        '<a href="../../woven-labels/">woven labels page</a> covers every label type we make.</p>'
    )
    return _article_shell(s, t, desc, read, lead, toc, body)


# ============================================================ article 7
def art_presentation():
    s, t, desc, read = ARTICLES[6]
    lead = ("Nobody buys a garment because of its label. But plenty of people put one back on the rail because of it. "
            "Here\u2019s what a considered woven label actually changes about how your product is received.")
    toc = [("moment", "The moment the label does its work"),
           ("signal", "What a label signals"),
           ("touch", "Texture is part of the message"),
           ("consistent", "Consistency across the range"),
           ("after", "It keeps working after the sale"),
           ("realistic", "What a label won\u2019t do")]
    body = (
        '<h2 id="moment">The moment the label does its work</h2>'
        '<p>Watch someone pick up a piece of clothing they\u2019re considering. They hold it, they feel the fabric, and '
        'within a few seconds they turn the neck out and look at the label. It\u2019s almost involuntary.</p>'
        '<p>That glance is the one moment where your brand gets to speak without any marketing around it. There\u2019s '
        'no packaging, no photography, no caption \u2014 just the garment and whatever you chose to put inside it.</p>'

        '<h2 id="signal">What a label signals</h2>'
        '<p>A label communicates in two directions at once. The obvious one is identity: this is who made it. The less '
        'obvious one is <em>investment</em> \u2014 the fact that someone cared enough about this product to have a '
        'label made for it rather than leaving it blank or using a generic printed tape.</p>'
        '<p>Customers rarely articulate this. They just come away with an impression that the piece is considered, or '
        'that it isn\u2019t. A woven brand label is one of the cheapest signals of care that a garment can carry.</p>'
        '<blockquote><p>The label is the only part of the product that speaks when nobody is selling.</p></blockquote>'

        '<h2 id="touch">Texture is part of the message</h2>'
        '<p>Clothing is bought with the hands as much as the eyes. A woven label has a slight relief where the threads '
        'change colour and a texture you can feel through your thumb. It reads as part of the garment because it is '
        'built the same way \u2014 from thread.</p>'
        '<p>That tactile quality is why woven labels remain the standard in established retail clothing, and it\u2019s '
        'why a brand moving from printed tape to woven often gets comments on the change even from people who '
        'can\u2019t say what\u2019s different.</p>'

        '<h2 id="consistent">Consistency across the range</h2>'
        '<p>A single good label helps one product. A consistent label across your whole range helps the brand. When the '
        'neck label, the size label, the care label and the hang tag all share a palette and a treatment, a customer '
        'who owns three of your pieces recognises the fourth instantly.</p>'
        '<p>This is where most small brands leave value on the table \u2014 not by having a poor label, but by having '
        'three unrelated ones because each was ordered separately without a plan.</p>'

        '<h2 id="after">It keeps working after the sale</h2>'
        '<p>A hang tag is removed and thrown away. Packaging is recycled. The woven label stays in the garment for as '
        'long as the garment lasts, which means it\u2019s still there the tenth time someone wears it and the first '
        'time a friend asks where they got it.</p>'
        '<p>Because the design is woven into the material rather than printed on top, it doesn\u2019t crack, peel or '
        'lift with normal washing \u2014 so that answer stays readable years later.</p>'

        '<h2 id="realistic">What a label won\u2019t do</h2>'
        '<p>Worth being straight about this: a label doesn\u2019t fix a product. It won\u2019t rescue a poor fit, '
        'thin fabric or bad finishing, and it won\u2019t make people buy something they didn\u2019t want.</p>'
        '<p>What it does is stop a good product from being undersold by its own presentation. If you\u2019ve put real '
        'work into what you make, the label is the detail that keeps the impression intact when a customer looks '
        'closer.</p>'
        '<p>If you want to see how your mark would look in thread, send it over on WhatsApp \u2014 we\u2019ll tell you '
        'how it translates before you commit to anything.</p>'
    )
    return _article_shell(s, t, desc, read, lead, toc, body)


# ============================================================ article 8
def art_small_business():
    s, t, desc, read = ARTICLES[7]
    lead = ("First label orders go wrong in predictable ways: too many decisions made at once, a design that looks "
            "fine on screen and disappears in thread, or a quantity picked before the brand knows what it needs. "
            "Here\u2019s a simpler way through it.")
    toc = [("start", "Start with one label"),
           ("decide", "The decisions that matter"),
           ("skip", "What to skip for now"),
           ("artwork", "If you don\u2019t have a designer"),
           ("quantity", "Thinking about quantity"),
           ("handmade", "Handmade and small-batch makers"),
           ("next", "What to do next")]
    body = (
        '<h2 id="start">Start with one label</h2>'
        '<p>You don\u2019t need a full label programme to look professional. One well-made brand label in the neck or '
        'the side seam does more for how your product is received than four mediocre ones ordered in a hurry.</p>'
        '<p>Decide which single label your customer is most likely to see, and order that one properly. Size, care and '
        'hang tags can follow once you know how the first one turned out.</p>'

        '<h2 id="decide">The decisions that matter</h2>'
        '<p>A label order comes down to a handful of choices, and most of them are easier than they sound:</p>'
        '<ul>'
        '<li><strong>Label type</strong> \u2014 brand label, size label, care label, hang tag.</li>'
        '<li><strong>Size</strong> \u2014 driven by where it sits and how much your artwork contains.</li>'
        '<li><strong>Shape</strong> \u2014 rectangular covers most needs; square and custom shapes are available.</li>'
        '<li><strong>Fold</strong> \u2014 Straight Cut, Centre Fold, End Fold, Mitre Fold or Manhattan Fold.</li>'
        '<li><strong>Thread colours</strong> \u2014 a focused palette keeps the weave clean.</li>'
        '<li><strong>Quantity</strong> \u2014 minimum order quantities apply and depend on the label type.</li>'
        '</ul>'
        '<p>If you\u2019re unsure on any of these, say so when you ask for a quote. It\u2019s a normal part of the '
        'conversation and it\u2019s faster than guessing.</p>'

        '<h2 id="skip">What to skip for now</h2>'
        '<p>Small businesses often overthink the parts that don\u2019t change the outcome. A few things you can safely '
        'put aside on a first order:</p>'
        '<ul>'
        '<li><strong>Custom shapes</strong> \u2014 lovely, but a clean rectangle is what most established brands use.</li>'
        '<li><strong>A large colour palette</strong> \u2014 two or three colours usually look sharper than six.</li>'
        '<li><strong>Every piece of text you own</strong> \u2014 the tagline and the website address can go on the hang '
        'tag or nowhere at all.</li>'
        '<li><strong>Matching every label type immediately</strong> \u2014 plan the look once, order the pieces as you '
        'need them.</li>'
        '</ul>'

        '<h2 id="artwork">If you don\u2019t have a designer</h2>'
        '<p>Plenty of small brands don\u2019t, and it isn\u2019t a blocker. Send whatever version of your logo you '
        'have \u2014 the biggest, cleanest file you own \u2014 and we\u2019ll tell you whether it works at label size '
        'and what would need simplifying if it doesn\u2019t.</p>'
        '<p>If all you have is your brand name, a woven label with just the name set cleanly in thread is a perfectly '
        'legitimate place to start. Our <a href="../prepare-logo-for-woven-labels/">logo preparation guide</a> covers '
        'what to check before you send anything.</p>'

        '<h2 id="quantity">Thinking about quantity</h2>'
        '<p>Minimum order quantities apply and vary by label type, so the practical approach is to tell us roughly how '
        'much you produce and let us tell you what\u2019s workable rather than guessing a number first.</p>'
        '<p>The thing to weigh up is how settled your branding is. If your logo is likely to change in the next few '
        'months, order what covers the near term. If it\u2019s fixed, a larger run is generally more economical per '
        'label \u2014 we\u2019ll give you the actual figures when we quote.</p>'

        '<h2 id="handmade">Handmade and small-batch makers</h2>'
        '<p>If you sew, knit, crochet or make by hand, a woven label is often the single thing that shifts a piece from '
        '\u201chomemade\u201d to \u201cmade by a brand\u201d in a customer\u2019s mind. The work is already there; '
        'the label just stops it being mistaken for something less considered.</p>'
        '<p>Small makers usually do well with a simple centre fold brand label in one or two colours \u2014 quick to '
        'sew in, durable through washing, and instantly recognisable across everything you make.</p>'

        '<h2 id="next">What to do next</h2>'
        '<ol>'
        '<li>Pick the one label your customer will see.</li>'
        '<li>Print your logo at the label\u2019s real size and check it still reads.</li>'
        '<li>Note roughly how many you need and by when.</li>'
        '<li>Send all of that on WhatsApp and ask for a quote.</li>'
        '</ol>'
        '<p>There\u2019s no cost to asking and no obligation after. If something about your artwork or quantity '
        'won\u2019t work, we\u2019ll tell you before you spend anything.</p>'
    )
    return _article_shell(s, t, desc, read, lead, toc, body)



# ============================================================ article 9
def art_ai_logo():
    s, t, desc, read = ARTICLES[8]
    lead = (
        "AI image tools are genuinely useful for exploring logo and monogram ideas. "
        "What they produce, though, is a raster image \u2014 and weaving works in thread, not pixels. "
        "Here\u2019s exactly what happens between your AI-generated design and a finished woven label or badge."
    )
    toc = [
        ("what-ai-gives-you",    "What an AI-generated image actually is"),
        ("what-weaving-needs",   "What weaving needs instead"),
        ("convert",              "Converting your AI image for production"),
        ("colours",              "Translating colours into thread"),
        ("badge-options",        "Badge and patch options"),
        ("schools",              "School monograms specifically"),
        ("send",                 "How to send it to us"),
        ("what-to-expect",       "What to expect"),
    ]
    body = (
        '<h2 id="what-ai-gives-you">What an AI-generated image actually is</h2>'
        '<p>ChatGPT, Midjourney, DALL\u00b7E and similar tools produce raster images \u2014 a grid of coloured '
        'pixels saved as a PNG or JPG. At large sizes these look sharp. At label size \u2014 which might be '
        '40\u00d740mm or 25\u00d725mm \u2014 the edges are no longer lines; they\u2019re stepped pixels. '
        'That\u2019s fine for printing on paper. It doesn\u2019t translate cleanly into thread without conversion.</p>'
        '<p>The other thing AI images typically contain is gradients, soft shadows, blended colours and photographic '
        'texture. Thread is solid colour \u2014 there are no gradients in weaving. Each colour is a separate thread, '
        'and blends have to become flat steps or a single colour.</p>'
        '<blockquote><p>The AI design is a starting point, not a file ready for the loom. What you send us, and what '
        'we weave, will be a cleaned-up, simplified version of it \u2014 which usually looks better at label size '
        'anyway.</p></blockquote>'

        '<h2 id="what-weaving-needs">What weaving needs instead</h2>'
        '<p>A woven label is built from a <strong>digitised design file</strong> \u2014 essentially a set of '
        'instructions that tell the loom which thread colour goes where, row by row. To create that, we work from '
        'artwork that has:</p>'
        '<ul>'
        '<li><strong>Clean, defined edges</strong> \u2014 not feathered or anti-aliased pixel edges.</li>'
        '<li><strong>A limited, flat colour palette</strong> \u2014 typically 2\u20138 solid thread colours.</li>'
        '<li><strong>No gradients or drop shadows</strong> \u2014 or those elements simplified into flat colour.</li>'
        '<li><strong>Legible text</strong> \u2014 type that still reads when the whole design is at most a few '
        'centimetres wide.</li>'
        '</ul>'
        '<p>We convert your AI image into this. You don\u2019t need to do the conversion yourself \u2014 '
        'send us what you have and we do it as part of the quoting process.</p>'

        '<h2 id="convert">Converting your AI image for production</h2>'
        '<p>When you send us an AI-generated PNG or JPG, here\u2019s what we do with it:</p>'
        '<ol>'
        '<li>We assess the design at your intended label size and identify what needs simplifying.</li>'
        '<li>We re-draw or trace the key elements \u2014 outline, text, icon \u2014 as clean vector shapes.</li>'
        '<li>We reduce the colour palette to the thread colours that best match your design.</li>'
        '<li>We send you a proof showing exactly how the woven version will look before any production begins.</li>'
        '</ol>'
        '<p>The proof step is where you approve the translation. If the simplification changes something you care about, '
        'we adjust before anything goes to the loom.</p>'
        '<p>What helps: sending the AI image at the largest size you exported, with a note on which colours matter '
        'most and what size you want the finished label to be.</p>'

        '<h2 id="colours">Translating colours into thread</h2>'
        '<p>AI tools produce colours in RGB \u2014 millions of possible shades. Thread comes in a finite set of '
        'manufactured colours, and we match your design to the closest available thread. For most AI-generated designs '
        'this is straightforward: a dark navy, an off-white, a red. Where it gets nuanced is when the design uses a '
        'very specific or unusual shade.</p>'
        '<p>If you have a brand colour reference \u2014 a Pantone number, a hex code from your brand guidelines, '
        'even just a note saying \u201cthis should match my school uniform colour\u201d \u2014 include it when you '
        'send the image. We\u2019ll tell you how close the thread match is before you commit.</p>'

        '<h2 id="badge-options">Badge and patch options</h2>'
        '<p>AI-designed marks work especially well as woven patches and badges, because a patch sits on top of the '
        'garment rather than being sewn into a seam \u2014 giving the design more space and visibility. '
        'Patch options we make:</p>'
        '<div class="table-scroll"><table class="key-table">'
        '<caption class="sr-only">Woven patch and badge options</caption>'
        '<thead><tr><th scope="col">Shape</th><th scope="col">Best for</th></tr></thead>'
        '<tbody>'
        '<tr><th scope="row">Circle</th><td>Round monograms, crests, seal-style marks</td></tr>'
        '<tr><th scope="row">Shield</th><td>School crests, sports clubs, institutional marks</td></tr>'
        '<tr><th scope="row">Square</th><td>Logo patches, brand marks, icon-only designs</td></tr>'
        '<tr><th scope="row">Custom cut</th><td>Any outline \u2014 follows the shape of your specific design</td></tr>'
        '</tbody></table></div>'
        '<p>Each shape is available with <strong>sew-on</strong> or <strong>iron-on</strong> backing. '
        'Iron-on suits uniforms and sportswear where individual application needs to be quick. '
        'Sew-on is more permanent and is standard for most badge applications.</p>'

        '<h2 id="schools">School monograms specifically</h2>'
        '<p>If you\u2019ve used an AI tool to generate a monogram or crest design for a school, here\u2019s '
        'what to tell us:</p>'
        '<ul>'
        '<li>The school\u2019s name and initials, in case the design includes lettering.</li>'
        '<li>Which colours the uniform uses \u2014 so we match thread to fabric.</li>'
        '<li>Where the badge will go (blazer breast pocket, PE kit, cap) \u2014 this affects size and backing.</li>'
        '<li>How many you need \u2014 minimum order for school badges is %(moq_s)s.</li>'
        '</ul>'
        '<p>Schools often generate a few AI variations before settling on one. That\u2019s fine \u2014 send us '
        'the options and we\u2019ll tell you which one translates best into thread at badge size before you decide.</p>'

        '<h2 id="send">How to send it to us</h2>'
        '<p>WhatsApp is the easiest channel for sharing an AI-generated design. Send the image directly in the chat '
        'along with:</p>'
        '<ul>'
        '<li>The size you have in mind (or a rough idea \u2014 we can suggest what works)</li>'
        '<li>The shape and backing you want (or \u201cnot sure yet\u201d \u2014 we\u2019ll advise)</li>'
        '<li>Your colour references if you have them</li>'
        '<li>Roughly how many you need</li>'
        '</ul>'
        '<p>We\u2019ll come back with a quote and, if needed, a question or two about the design before anything is '
        'confirmed. No payment is taken until you\u2019ve approved a proof.</p>'

        '<h2 id="what-to-expect">What to expect</h2>'
        '<p>AI-generated designs usually take a little more preparation than a vector logo a designer made for print, '
        'because the conversion work is heavier. That said, most AI designs we see are straightforward to translate \u2014 '
        'the AI tools that produce clean, graphic, limited-colour marks are particularly good starting points.</p>'
        '<p>What you get at the end is a woven badge or label that carries your design in thread \u2014 durable, '
        'washable, and exactly the same across every unit in the batch.</p>'
        '<p>Send your design over on WhatsApp and we\u2019ll tell you how it translates. No cost to asking.</p>'
    ) % {"moq_s": MOQ_SCHOOL}
    return _article_shell(s, t, desc, read, lead, toc, body)

def art_complete_guide():
    SEO_TITLES[GUIDE_SLUG] = _G["seo_title"]
    return _article_shell(GUIDE_SLUG, _G["title"], _G["desc"], "%d min read" % _G["mins"], "",
                          _G["toc"], _G["body"],
                          extra_schema=[faq_schema(_G["faqs"], "resources/%s/" % GUIDE_SLUG)],
                          pub_date=GUIDE_DATE)


ALL_ARTICLES = [art_woven_vs_printed, art_guide, art_size, art_folds,
                art_logo_prep, art_clothing_brands, art_presentation, art_small_business,
                art_ai_logo, art_complete_guide]

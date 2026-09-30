# -*- coding: utf-8 -*-
"""Content data shared across pages. Only factual, non-invented claims."""

from core import label_svg, url, wa, ICON_WA, check, asset, MOQ_APPAREL, MOQ_SCHOOL, TURNAROUND

# ---------------------------------------------------------------- products
# (anchor, name, blurb, ideal-use, svg kwargs)
PRODUCTS = [
    ("brand-labels", "Brand labels",
     "Your brand name woven into the neck or side seam of every piece you make \u2014 the label a customer sees first.",
     "Clothing and fashion brands, boutiques, handmade labels",
     dict(brand="ATELIER", sub="MADE WITH CARE", palette="ink", shape="rect", fold="flat")),

    ("logo-labels", "Logo woven labels",
     "Your logo reproduced in thread. Fine detail, small type and multi-colour marks are all woven rather than printed.",
     "Brands with an established logo or wordmark",
     dict(brand="NORDE", sub="EST. LABEL", palette="red", shape="rounded", fold="flat")),

    ("size-labels", "Size labels",
     "Clean, consistent size markers \u2014 XS through XXL, numeric sizing, or your own size system.",
     "Any brand running a full size range",
     dict(brand="M", sub="SIZE", palette="cream", shape="square", fold="center")),

    ("care-labels", "Care labels",
     "Washing and care instructions woven to stay readable for the life of the garment, with care symbols where you need them.",
     "Retail-ready garments and export orders",
     dict(brand="30\u00b0", sub="WASH  \u00b7  DO NOT BLEACH", palette="ink", shape="rect", fold="end")),

    ("hang-tags", "Hang tags",
     "Woven tags that hang on the outside of the product \u2014 often the first thing a customer touches on the rail.",
     "Retail display, gifting, premium packaging",
     dict(brand="MAISON", sub="HANDMADE", palette="red", shape="diecut", fold="flat")),

    ("monograms", "School monograms & badges",
     "Custom woven monograms and crests for uniforms, blazers and sportswear, matched to the school's own emblem.",
     "Schools, academies and organisations",
     dict(brand="I.C.A", sub="SECONDARY SCHOOL", palette="cream", shape="rounded", fold="flat")),
]

# School monogram extra options
MONOGRAM_BACKING = ["Sew-on", "Iron-on"]
MONOGRAM_SHAPES  = ["Circle", "Shield", "Square", "Custom cut"]

FOLDS = [
    ("Straight Cut (Flat)", "No fold. The full label is visible and sewn flat — on all four sides or across the top and bottom.",
     "Neck labels, patches, hang tags, side-seam tabs"),
    ("Centre Fold", "Folded in half across the middle. The label reads on the front and the back is hidden inside the seam.",
     "Neck labels and side-seam brand labels"),
    ("End Fold", "Both short ends are folded under, leaving clean finished sides with no raw edges.",
     "Neck labels, care labels, size labels"),
    ("Mitre Fold", "All four corners are mitred and folded under, giving a neat, tailored finish on every edge.",
     "Premium brand labels and hang tags"),
    ("Manhattan Fold", "One end is folded over and the other remains open, giving a folded top edge with a raw bottom edge sewn into the seam.",
     "Waistband labels and inside-hem labels"),
]

# ---------------------------------------------------------------- gallery
# Real photos of labels actually woven for real orders (filename, alt text, caption).
# Each entry: (filename, alt, caption, category)
# category: "brand" = clothing/fashion labels, "school" = school monograms/badges
GALLERY = [
    ("gallery-fourkids-waveriders.jpg",
     "Woven ribbon labels for Four Kids, and a logo patch for Wave Riders",
     "Woven ribbon labels for Four Kids, and a logo patch for Wave Riders", "brand"),
    ("gallery-aimen.jpg",
     "Pile of black woven labels reading Aimen in white thread",
     "Woven brand labels for Aimen", "brand"),
    ("gallery-munamatar.jpg",
     "Cream woven label reading Muna Matar, made in UAE",
     "Woven brand label for Muna Matar, made in UAE", "brand"),
    ("gallery-honio.jpg",
     "Woven labels reading Honio Collection in small, medium and large",
     "Size-coded woven labels for Honio Collection", "brand"),
    ("gallery-ribbon-set.jpg",
     "Pile of woven ribbon labels in bold yellow, black and white",
     "Woven ribbon labels in bold yellow and black colourway", "brand"),
    ("gallery-llgc-monogram.jpg",
     "Woven school badge for LLGC, navy shield on white",
     "School badge for Learning Line Girls College and Academy (LLGC)", "school"),
    ("gallery-nexdeen-monogram.jpg",
     "Woven school badge for NexDeen School NDS, navy and gold crest",
     "School badge for NexDeen School (NDS)", "school"),
    ("gallery-ica-monogram.jpg",
     "Woven school badge for I.C.A Sec. School, red and navy crest on cream",
     "School badge for I.C.A Secondary School", "school"),
    ("gallery-kids-paradise-monogram.jpg",
     "Woven school badge for The Kids Paradise Campus, shield crest",
     "School badge for Boota Iqbal Public High School Kids Campus", "school"),
    ("gallery-iqbal-school-monogram.jpg",
     "Circular woven school badge for Iqbal School and College System, gold on white",
     "School badge for Iqbal School and College System, Qadir Pur Raan", "school"),
]

# ---------------------------------------------------------------- process
STEPS = [
    ("01", "Send your design", "Share your logo, artwork or even a rough idea over WhatsApp or email. Vector files work best, but we can work from what you have."),
    ("02", "Choose your label", "We go through label type, size, fold style and thread colours with you, and tell you how your artwork will translate into thread."),
    ("03", "Confirm details", "You approve the design, size and quantity before anything is produced. Nothing goes to the loom until you're happy."),
    ("04", "Production", "Your labels are woven to the confirmed specification."),
    ("05", "Receive your labels", "We deliver across Pakistan, and can arrange international delivery. We'll confirm the arrangement with you before dispatch."),
]

# ---------------------------------------------------------------- why us
WHY = [
    ("Custom branding", "Every label is built around your brand \u2014 your logo, your wordmark, your colours. Nothing off-the-shelf."),
    ("Professional presentation", "A woven label gives a garment the finished look customers associate with established brands."),
    ("Quality-focused production", "Labels are woven to the specification you approve, and checked against it before they leave us."),
    ("Multiple label options", "Brand, logo, size, care, hang tags and monograms \u2014 all from one supplier, all matched to each other."),
    ("Flexible customisation", "Size, shape, fold style and thread colours are chosen per order, not picked from a fixed catalogue."),
    ("Direct communication", "You talk to us directly on WhatsApp. Questions get answered by the people making your labels."),
    ("Fashion and apparel focus", "We work with clothing, fashion and handmade brands every day, so the advice you get is specific to garments."),
]

BENEFITS = [
    ("Fully custom designs", "Built around your logo and brand, not a template."),
    ("Premium woven finish", "Woven in thread rather than printed on film."),
    ("Custom sizes &amp; shapes", "Sized to your garment, including shaped outlines."),
    ("Multiple fold options", "Straight Cut (flat), Centre Fold, End Fold, Mitre Fold and Manhattan Fold."),
    ("Direct WhatsApp support", "Message us and speak to us directly."),
]

# ---------------------------------------------------------------- FAQ
FAQS = [
    ("What are woven labels?",
     "Woven labels are small pieces of fabric made on a loom, where your logo, brand name or text is created by "
     "weaving coloured threads together. The design is part of the material itself rather than ink sitting on a surface."),

    ("What are woven labels used for?",
     "They are used to brand clothing and products \u2014 neck labels carrying a brand name, side-seam tabs, size and "
     "care labels, hang tags on the outside of a garment, and monograms or crests on school uniforms."),

    ("What is the minimum order quantity?",
     "For clothing and fashion brands, the minimum is %s. For schools ordering custom monograms or crests, the "
     "minimum is %s." % (MOQ_APPAREL, MOQ_SCHOOL)),

    ("How long does an order take?",
     "Production takes %s once the design, size and quantity are confirmed, for delivery across Pakistan. "
     "International orders are arranged separately and confirmed with you before dispatch." % TURNAROUND),

    ("Can I add my own logo?",
     "Yes. Send us your logo over WhatsApp or email and we will tell you how it translates into thread, including any "
     "detail that needs simplifying at label size."),

    ("Can I customise the size?",
     "Yes. Labels are made to the size you need rather than fixed sizes. Tell us the garment and where the label sits, "
     "and we will suggest a size that fits and stays readable."),

    ("Can I choose the colours?",
     "Yes. You choose the background and thread colours. We match your brand colours as closely as the weaving process "
     "allows, and a focused palette \u2014 generally around 10 to 12 thread colours \u2014 covers most logos and text cleanly."),

    ("What woven label fold options are available?",
     "Straight Cut (flat), Centre Fold, End Fold, Mitre Fold and Manhattan Fold. "
     "Which one suits you depends on where the label is sewn."),

    ("Can I order brand labels?",
     "Yes. Brand labels carrying your name or logo are the most common order we produce."),

    ("Can I order size labels?",
     "Yes, in your own sizing system \u2014 letter sizes, numeric sizes or both \u2014 and matched to the look of your brand label."),

    ("Can I order care labels?",
     "Yes. Care labels can carry washing instructions, fabric composition, country of manufacture and standard care symbols."),

    ("Can I order custom-shaped labels?",
     "Yes. Labels can be made to an outline that follows your logo instead of a rectangle. Share your artwork and we will "
     "tell you what works at label size."),

    ("How do I send my artwork?",
     "Send it on WhatsApp or by email. Vector files such as AI, EPS, SVG or PDF are ideal because they stay sharp at small "
     "sizes, but a high-resolution PNG or JPG is usually enough to start the conversation."),

    ("How do I get a quote?",
     "Message us on WhatsApp at " + "+92 304 8095202" + " with your label type, quantity and size, or fill in the quote form "
     "on this site. Quotes are free and there is no obligation."),

    ("How do I place an order?",
     "Once you have a quote, we confirm the design, size, fold and quantity with you, and you approve a sample before the "
     "full order is produced."),

    ("Can I contact Premium Woven Labels through WhatsApp?",
     "Yes \u2014 WhatsApp is our main channel and the fastest way to reach us. Message +92 304 8095202 and you will be talking "
     "directly to us."),
]

FAQS.append(("How much do custom woven labels cost?",
             "The price depends on label size, number of thread colours, fold style, material and quantity. "
             "Send your logo, label type, rough size and quantity on WhatsApp and we will quote in one reply."))
FAQ_SHORT = FAQS[:6]


# Real photos that best illustrate each product type (filename in assets/img/real/).
# None = fall back to the SVG label illustration.
PRODUCT_PHOTOS = {
    "brand-labels":  "gallery-aimen.jpg",
    "logo-labels":   "gallery-fourkids-waveriders.jpg",
    "size-labels":   "gallery-honio.jpg",
    "care-labels":   None,
    "hang-tags":     None,
    "monograms":     "gallery-llgc-monogram.jpg",
}


def products_grid(depth, limit=None, heading_level="h3"):
    cards = []
    for i, (anchor, name, blurb, use, svg) in enumerate(PRODUCTS[:limit]):
        photo = PRODUCT_PHOTOS.get(anchor)
        if photo:
            shot = ('<div class="prod-shot prod-shot--photo">'
                    '<img src="' + asset("assets/img/real/" + photo, depth) +
                    '" alt="Real woven ' + name.lower() + ' example" loading="lazy" width="800" height="800">'
                    '</div>')
        else:
            shot = ('<div class="prod-shot prod-shot--blank">'
                    '<span class="prod-blank-name">' + name + '</span>'
                    '</div>')
        cards.append(
            '<article class="prod-card reveal d%d" id="%s">' % (i % 4 + 1, anchor) +
            shot +
            '<div class="prod-body">' +
            '<%s>%s</%s><p>%s</p>' % (heading_level, name, heading_level, blurb) +
            '<p class="prod-use"><b>Best for:</b> %s</p>' % use +
            '<a class="btn btn-primary btn-sm" href="%s">Get a quote</a>' % url("contact/", depth) +
            '</div></article>'
        )
    return '<div class="grid g-3">%s</div>' % "".join(cards)


def benefits_strip():
    out = []
    for title, sub in BENEFITS:
        out.append('<div class="benefit">%s<b>%s</b><span>%s</span></div>' % (check("#a70c12"), title, sub))
    return '<section class="benefits" aria-label="What we offer">%s</section>' % "".join(out)


def steps_block():
    return '<div class="steps">%s</div>' % "".join(
        '<div class="step reveal d%d"><span class="step-n">%s</span><h3>%s</h3><p>%s</p></div>'
        % (i % 4 + 1, n, t, d) for i, (n, t, d) in enumerate(STEPS)
    )


def _gal_items(entries, depth, id_prefix):
    """Render a row of gallery button items."""
    out = []
    for i, (fname, alt, cap, _cat) in enumerate(entries):
        out.append(
            '<button class="gal-item" type="button" '
            'data-cap="%s" data-idx="%d" data-group="%s" '
            'aria-label="Enlarge: %s">'
            '<img src="%s" alt="%s" loading="lazy" width="1200" height="1600">'
            '<span class="gal-cap">%s</span></button>'
            % (cap, i, id_prefix, cap,
               asset("assets/img/real/" + fname, depth), alt, cap)
        )
    return "".join(out)


def gallery_block(depth, limit=None):
    brand  = [(f, a, c, t) for f, a, c, t in GALLERY if t == "brand"][:limit]
    school = [(f, a, c, t) for f, a, c, t in GALLERY if t == "school"][:limit]

    lb = (
        '<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" '
        'aria-label="Label preview" aria-hidden="true">'
        '<button class="lb-close" type="button" aria-label="Close preview">&times;</button>'
        '<button class="lb-nav lb-prev" type="button" aria-label="Previous">&#8249;</button>'
        '<button class="lb-nav lb-next" type="button" aria-label="Next">&#8250;</button>'
        '<div class="lb-inner"><div id="lbInner"></div>'
        '<p class="lb-cap" id="lbCap"></p></div></div>'
    )

    html = (
        '<div class="gal-section">'
        '<h2 class="gal-heading">Woven labels &amp; brand labels</h2>'
        '<div class="gal-grid" id="galGrid-brand">%s</div>'
        '</div>'
        '<div class="gal-section" style="margin-top:clamp(32px,5vw,52px)">'
        '<h2 class="gal-heading">School monograms &amp; badges</h2>'
        '<div class="gal-grid" id="galGrid-school">%s</div>'
        '</div>'
        '%s'
    ) % (_gal_items(brand, depth, "brand"),
         _gal_items(school, depth, "school"),
         lb)

    return html


def quote_form(depth, dark_side=True):
    label_types = ["Brand label", "Logo woven label", "Size label", "Care label", "Hang tag",
                   "School monogram", "Not sure yet"]
    folds = ["Flat woven", "Centre fold", "End fold", "Mitre Fold", "Manhattan Fold", "Not sure yet"]
    opts = lambda arr: "".join('<option value="%s">%s</option>' % (o, o) for o in arr)
    return (
        '<div class="quote-shell">'
        '<div class="quote-side reveal">'
        '<div class="thread-rule"></div>'
        '<h2>Let\u2019s create your custom woven labels</h2>'
        '<p>Tell us what you need and we\u2019ll come back with a free quote. The more you can share \u2014 label type, '
        'quantity, rough size \u2014 the faster we can price it.</p>'
        '<div class="wa-box"><b>In a hurry?</b>'
        '<p>Send your design straight to us. WhatsApp is our fastest channel and you\u2019ll be talking to us directly.</p>'
        '<a class="btn btn-wa" href="%(wa)s" target="_blank" rel="noopener">%(iwa)s Send your design on WhatsApp</a>'
        '</div></div>'
        '<form class="form-card reveal d1" id="quoteForm" novalidate>'
        '<div class="hp" aria-hidden="true"><label for="hp-a">Leave this empty</label><input type="text" id="hp-a" name="botcheck" tabindex="-1" autocomplete="off">'
        '<label for="hp-b">Leave this empty</label><input type="text" id="hp-b" name="_gotcha" tabindex="-1" autocomplete="off"></div>'
        '<div class="form-grid">'
        '<div class="field"><label for="q-name">Your name</label><input id="q-name" name="name" type="text" autocomplete="name" required></div>'
        '<div class="field"><label for="q-brand">Brand name <span class="opt">(optional)</span></label><input id="q-brand" name="brand" type="text" autocomplete="organization"></div>'
        '<div class="field"><label for="q-wa">WhatsApp number</label><input id="q-wa" name="whatsapp" type="tel" inputmode="tel" autocomplete="tel" placeholder="+92 3XX XXXXXXX" required></div>'
        '<div class="field"><label for="q-email">Email <span class="opt">(optional)</span></label><input id="q-email" name="email" type="email" autocomplete="email"></div>'
        '<div class="field"><label for="q-type">Label type</label><select id="q-type" name="labelType">%(types)s</select></div>'
        '<div class="field"><label for="q-qty">Quantity</label><input id="q-qty" name="quantity" type="text" inputmode="numeric" placeholder="e.g. 1000">'
        '<span class="field-hint">%(qhint)s</span></div>'
        '<div class="field"><label for="q-size">Preferred size <span class="opt">(optional)</span></label><input id="q-size" name="size" type="text" placeholder="e.g. 50 x 15 mm"></div>'
        '<div class="field"><label for="q-fold">Fold style</label><select id="q-fold" name="fold">%(folds)s</select></div>'
        '<div class="field full"><label for="q-msg">Anything else <span class="opt">(optional)</span></label>'
        '<textarea id="q-msg" name="message" placeholder="Colours, garment type, deadline \u2014 anything that helps us quote accurately."></textarea></div>'
        '<div class="field full"><label for="q-art">Artwork <span class="opt">(optional)</span></label>'
        '<input id="q-art" name="artwork" type="file" accept=".png,.jpg,.jpeg,.pdf,.ai,.eps,.svg">'
        '<span class="field-hint">Pick your file here and we\u2019ll remind you to attach it in the chat \u2014 WhatsApp handles the file itself.</span></div>'
        '</div>'
        '<div class="form-actions">'
        '<button class="btn btn-primary btn-lg" type="submit">Request a quote</button>'
        '<button class="btn btn-ghost" type="button" id="emailInstead">Send it by email instead</button>'
        '</div>'
        '<div class="form-status" id="formStatus" role="status" aria-live="polite"></div>'
        '<p class="form-note">Your details are used only to answer your enquiry. Nothing is stored on this website.</p>'
        '</form></div>'
        % {"wa": wa(), "iwa": ICON_WA, "types": opts(label_types), "folds": opts(folds),
           "qhint": "Minimum order: %s for apparel, %s for schools." % (MOQ_APPAREL, MOQ_SCHOOL)}
    )



# ---- Fill these in, then run  python3 build.py  ------------------------------------------------
# Price guide rows shown on /pricing/. Leave empty to show the "what affects the price" page only.
# Example row: ("Brand label, damask, 50 x 15 mm", "1,000 pcs", "Rs 12 / pc")
PRICE_BANDS = []

# Client quotes shown on the homepage. Leave empty to hide the section. Only add quotes you have permission to use.
# Example row: ("Great finish and delivered on time.", "Name, Brand")
TESTIMONIALS = []

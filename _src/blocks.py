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
    ("gallery-ozan-boutiq.jpg",
     "Woven brand labels for \u00d6z\u00e4n Boutiq",
     "Woven brand labels for \u00d6z\u00e4n Boutiq", "brand"),
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

    ("What is the difference between woven and printed labels?",
     "A printed label has ink sitting on top of the fabric. A woven label is built from coloured thread on a loom, so the "
     "design is part of the fabric itself. Woven labels generally hold their colour and shape through washing better than "
     "printed ones, which is why most brands use woven for the main neck or brand label and printed for care instructions."),

    ("What file formats do you accept for artwork?",
     "Vector files \u2014 AI, EPS, SVG or PDF \u2014 are ideal because they stay sharp at any size. A high-resolution PNG or JPG is "
     "usually enough to start the conversation, and we will tell you if the file needs to be redrawn as a vector before weaving."),

    ("Do you offer sew-on and iron-on backing?",
     "Yes, both " + " and ".join(x.lower() for x in MONOGRAM_BACKING) + " backings are available. Sew-on is the more "
     "durable option for everyday wear; iron-on suits a faster application without stitching."),

    ("Will the colours and design survive washing?",
     "Yes. Because the design is woven from thread rather than printed on the surface, there is no ink layer to crack, "
     "peel or fade. Woven labels are made to outlast the garment they are sewn into."),

    ("Can I see a sample before placing the full order?",
     "Yes. You approve a sample before the full order goes into production, so nothing is woven at scale until you have "
     "signed off on the design, size and colours."),

    ("Do you make labels for exporters and garment manufacturers?",
     "Yes. We supply brand, size and care labels to garment makers and exporters who need a consistent set across a "
     "production run, matched to buyer specifications."),

    ("Can I order a small test batch before a full production run?",
     "Our minimum is %s for apparel labels and %s for school monograms \u2014 this is what keeps our per-piece rate low "
     "for the full run. Within that minimum, we're happy to split a first order across two or three designs so you can "
     "compare before committing to one for a repeat order." % (MOQ_APPAREL, MOQ_SCHOOL)),

    ("Is a woven monogram better than an embroidered or printed school badge?",
     "A woven monogram is flatter and more consistent than embroidery, so it doesn't add bulk to a blazer or shirt, "
     "and it holds its detail at small sizes better than embroidery tends to. Compared to a printed badge, the design "
     "is woven into the fabric rather than sitting on the surface, so it resists fading and cracking through repeated "
     "school-term washing."),

    ("What is a typical size for a school uniform monogram?",
     "Most school monograms fall roughly in the 50\u201390mm range depending on the shape and how much detail the "
     "crest carries \u2014 a simple initial can be smaller, a full crest with text usually needs more room. Send us "
     "the design and we'll confirm a size that stays legible on the uniform."),

    ("Do you embroider designs directly onto garments?",
     "No \u2014 we make woven labels and badges, which are produced separately and then sewn onto the garment. "
     "We don't offer direct embroidery (karhai) onto clothing."),

    ("What are your payment terms?",
     "We work on 50% advance to confirm and start production, with the remaining 50% due before dispatch. "
     "Cash on delivery can be arranged for orders where it's offered."),

    ("Can I order fewer than 1,000 pieces?",
     "Yes \u2014 alongside our standard 1,000+ runs, we offer starter quantities of 100, 300 or 500 pieces for "
     "apparel labels. The per-piece rate is higher at these smaller quantities, since production is less "
     "efficient at low volumes. Message us your quantity on WhatsApp for an exact rate."),
]

FAQS.append(("How much do custom woven labels cost?",
             "The price depends on label size, number of thread colours, fold style, material and quantity. "
             "Send your logo, label type, rough size and quantity on WhatsApp and we will quote in one reply."))
FAQ_SHORT = FAQS[:6]


# Real photos that best illustrate each product type (filename in assets/img/real/).
# None = fall back to the SVG label illustration.
PRODUCT_PHOTOS = {
    "brand-labels":  "gallery-aimen.jpg",
    "logo-labels":   "gallery-ozan-boutiq.jpg",
    "size-labels":   "gallery-honio.jpg",
    "care-labels":   None,
    "hang-tags":     None,
    "monograms":     "gallery-llgc-monogram.jpg",
}


PRODUCT_PAGE_SLUG = {
    "brand-labels": "brand-labels", "logo-labels": "logo-labels", "size-labels": "size-labels",
    "care-labels": "care-labels", "hang-tags": "hang-tags", "monograms": "school-monograms",
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
            '<a class="textlink" href="%s" style="display:block;margin-bottom:10px">Learn more</a>'
            % url(PRODUCT_PAGE_SLUG[anchor] + "/", depth) +
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
CLIENT_SPOTLIGHT = {
    "client": "Akber Ali Shah",
    "brand": "Mr VIP",
    "quote": "Excellent work, Masha Allah \u2014 got my \u2018Mr VIP\u2019 labels made here.",
    "note": "Posted publicly on our Facebook page after receiving his woven labels.",
}


TESTIMONIALS = [
    ("Excellent work, Masha Allah — got my \u2018Mr VIP\u2019 labels made here.", "Akber Ali Shah, Mr VIP"),
    ("Received today, Alhamdulillah — satisfied with the quality.", "Adnan Hyder, ASNA Coutures"),
    ("Highly recommended — excellent quality and price.", "Iqra Mobeen"),
    ("Received my parcel, very good work. Highly recommend.", "Amber Khawar"),
    ("So happy to receive my parcel — best quality and fast service.", "Preshy Anna"),
    ("Best service and quality. Recommended.", "Ammad Jaffer"),
    ("I'm obsessed. The quality is top notch.", "Mohammad Ameen"),
    ("I'm absolutely thrilled with the labels I received, thanks!", "Muhammad Rehan"),
]


# ============================================================ ADDED: placement guide, audience, page FAQ
PLACEMENT_GUIDE = [
    ("Neck / brand label", "Inside the back collar of shirts, hoodies and jackets", "Roughly 35\u201360mm wide"),
    ("Side-seam label", "Sewn into the side seam, a discreet strip of branding", "Roughly 15\u201320mm wide"),
    ("Size label", "Stacked with the brand label or sewn separately", "Roughly 15\u201325mm wide"),
    ("Care label", "Inside seam, carrying wash and composition instructions", "Roughly 40\u201370mm wide"),
    ("Hang tag", "Outside the garment, attached by a loop or pin", "Larger \u2014 read at arm\u2019s length on the rail"),
    ("Monogram / crest", "Blazer pocket, cap front or uniform sleeve", "Roughly 60\u201390mm, shape-dependent"),
]

WOVEN_AUDIENCE = [
    ("Clothing brands", "Full label sets for a collection \u2014 brand, size and care together."),
    ("Boutiques", "Smaller runs with a retail-ready finish."),
    ("Garment makers & exporters", "Consistent labels across a production run, matched to buyer specs."),
    ("Handmade businesses", "A proper woven label on handmade or made-to-order pieces."),
    ("Startups & new brands", "First labels for a first collection, with guidance on sizing and fold."),
    ("Schools", "Monograms and crests for uniforms and sportswear."),
    ("Activewear & loungewear", "Labels that hold up to frequent washing and stretch."),
    ("Growing brands", "Repeat orders woven to match the last batch exactly."),
]

WOVEN_FAQ = [f for f in FAQS if f[0] in (
    "What is the difference between woven and printed labels?",
    "What woven label fold options are available?",
    "What file formats do you accept for artwork?",
    "Do you offer sew-on and iron-on backing?",
    "Will the colours and design survive washing?",
    "Can I see a sample before placing the full order?",
    "What is the minimum order quantity?",
    "Can I order custom-shaped labels?",
)]


# ============================================================ ADDED: placement guide for non-garment items
# Sizes are practical starting points, not fixed standards, and are confirmed per order.
# Fold names below are kept consistent with the FOLDS definitions above:
#   Straight Cut (Flat) = no fold, sewn flat \u2014 used here wherever a plain sewn-on patch is meant.
#   Centre Fold / End Fold = used only where the label is genuinely caught into a seam or hem.
PLACEMENT_FAQ_GROUPS = [
    ("Caps & hats", [
        ("What size woven label should I use on a baseball cap?",
         "Start with a 35\u201355 x 20\u201335mm visible label on a front or side panel, clear of the bill seam. "
         "Straight Cut (Flat) gives a neat sewn-on patch; keep it compact and check it on the curved cap so it "
         "doesn\u2019t bridge panel seams or pucker."),
        ("Where should I sew a label inside or on the back of a cap?",
         "A 15\u201325 x 30\u201345mm label works at the back opening or inside the sweatband; use a Centre Fold if it "
         "can be caught in that seam. Keep the label soft and clear of the adjustable closure so it doesn\u2019t rub the wearer."),
        ("Can a woven label be sewn onto a curved cap without wrinkling?",
         "Use a small 20\u201335 x 20\u201330mm label on the flattest part of a side panel, sewn Straight Cut (Flat). Avoid "
         "spanning a panel seam, and approve a sample on the actual cap \u2014 the crown\u2019s curve can make a larger label lift or ripple."),
    ]),
    ("Gloves", [
        ("What size woven label fits on gloves?",
         "Try 12\u201320 x 20\u201335mm on the outside cuff or back of the wrist, away from the palm and thumb. "
         "Straight Cut (Flat) works for a small sewn-on patch; keep the label compact so it doesn\u2019t stiffen the cuff or catch on things."),
        ("Where should I put a woven label on knitted gloves?",
         "A 15\u201320 x 30\u201340mm label suits the outer cuff edge; use a Centre Fold if it can be inserted into the "
         "cuff seam. Ribbed cuffs stretch, so sew without pulling the knit tight and check the label doesn\u2019t restrict the fit."),
        ("Can I sew a woven label onto leather or waterproof gloves?",
         "Use a 15\u201325 x 30\u201340mm label at the outer wrist or cuff seam, with an End Fold inserted into the seam "
         "or a Straight Cut (Flat) patch on a suitable flat panel. Avoid the palm and any waterproof membrane, since "
         "needle holes can affect grip or waterproofing \u2014 test on a sample first."),
    ]),
    ("Shawls", [
        ("What size woven label is suitable for a shawl?",
         "Start with a 15\u201325 x 30\u201345mm label at an inside lower corner or short edge, sewn Straight Cut (Flat) "
         "for a clean finish. Fine, drapey shawls suit a small, lightweight label; hand-sewing avoids puckering."),
        ("Where should I sew a label on a shawl so it is easy to find?",
         "Place a 15\u201320 x 30\u201340mm label on the reverse near a lower corner, about 15\u201325mm in from the "
         "finished edges. Sew Straight Cut (Flat) with small stitches and avoid open weave or fringe, which can distort or snag."),
        ("Can I add a woven label into the edge of a shawl?",
         "Yes \u2014 use a 15\u201320 x 35\u201350mm label with a Centre Fold caught into a short-edge hem or side seam. "
         "This makes a small flag label; keep it clear of fringe and check the added thickness doesn\u2019t interrupt the drape."),
    ]),
    ("Scarves", [
        ("What size woven label works best on a lightweight scarf?",
         "A 12\u201318 x 25\u201335mm label at an inside corner is a good starting point, about 15\u201320mm from both "
         "edges. Sew Straight Cut (Flat) and choose a soft, lightweight label so it doesn\u2019t weigh down silk or other fine fabric."),
        ("Where should I sew a label on a fringed scarf?",
         "Use a 15\u201320 x 30\u201340mm label at a lower corner, just above the fringe. A Centre Fold caught into "
         "the hem works well; don\u2019t stitch through the fringe, which moves freely and can pull the label out of shape."),
        ("How do I label a reversible scarf?",
         "Put a 15\u201320 x 30\u201340mm label at a short-end hem and use a Centre Fold so the label shows on both "
         "sides. Keep the stitch line tidy on both faces and avoid a bulky fold that could affect how the scarf sits."),
    ]),
    ("Crochet & knitted items", [
        ("Can you put a woven label on crochet or knitted items?",
         "Yes \u2014 start with a 15\u201320 x 25\u201340mm label at a dense hem, side edge or other stable section, "
         "sewn Straight Cut (Flat). Sew through the stitches without pulling them tight; a small backing patch helps if the area is loose or openwork."),
        ("Where should a label go on a knitted sweater or crochet item?",
         "A 15\u201320 x 30\u201345mm label usually works at a lower side hem or inside the back neck below the "
         "ribbing. Use Straight Cut (Flat) for a plain patch, or a Centre Fold if it can go into a seam; avoid stretchy "
         "ribbing that may pucker or lose its stretch."),
        ("How do I stop a label stretching or snagging a knit?",
         "Choose a compact 15\u201320 x 25\u201335mm label and sew it onto a dense section, Straight Cut (Flat) with "
         "its edges secured. For loose crochet or chunky knit, add a light backing and hand-sew through stable loops "
         "without tightening the yarn or sewing across open spaces."),
    ]),
    ("Beanies", [
        ("What size woven label should I use on a beanie cuff?",
         "A 20\u201325 x 35\u201350mm visible label is a useful starting point on the front or side of the cuff. Use "
         "a Centre Fold to make a fold-over cuff tab, and account for the cuff\u2019s stretch so the label doesn\u2019t "
         "pull the knit out of shape."),
        ("Where should I sew a label on a beanie?",
         "A 15\u201325 x 30\u201345mm label can go on the outer cuff or near the back seam, depending on how visible "
         "you want it. Use Straight Cut (Flat) for a plain patch or a Centre Fold at the cuff edge, and keep it away "
         "from the wearer\u2019s forehead if it could feel scratchy."),
        ("Can I label a beanie that has no folded cuff?",
         "Yes \u2014 try a 15\u201320 x 30\u201340mm label on the lower side edge or near the back seam, using a "
         "Centre Fold if it can be caught in a seam. If sewing it flat, use Straight Cut (Flat) on a stable knit area "
         "so the stretchy fabric doesn\u2019t wave around the label."),
    ]),
    ("Tote bags", [
        ("What size woven label should I use on a tote bag?",
         "A 20\u201330 x 40\u201360mm label suits an exterior brand mark near a lower corner or side seam. Sew "
         "Straight Cut (Flat), and check the label against the bag\u2019s canvas weight so it doesn\u2019t look "
         "undersized or feel bulky."),
        ("Where should I put a woven label on a tote bag?",
         "Use a 15\u201325 x 35\u201350mm label at the top of a side seam or gusset, clear of the handles and bag "
         "opening. A Centre Fold makes a tidy side-seam tag; on thick canvas, sew through the seam allowance where possible."),
        ("Where should an inside tote-bag label go?",
         "A 20\u201330 x 40\u201360mm label fits inside the bag near the top edge, pocket or lining side seam. Use "
         "a Centre Fold caught into the seam, attached before the lining is closed if you want exterior stitches hidden."),
    ]),
    ("Blankets & throws", [
        ("What size woven label works on a blanket or throw?",
         "Start with a 20\u201330 x 40\u201360mm label at a lower corner on the reverse side. Sew Straight Cut (Flat) "
         "for a plain corner label; keep it off the main sleeping surface and check the size suits the pile or thickness."),
        ("Should a blanket label be sewn into the edge?",
         "Yes \u2014 a 20\u201330 x 40\u201360mm label with a Centre Fold can be caught into the bottom or side hem "
         "as a small tab. Thick fleece and plush pile can make seams bulky, so check the fold and stitch placement on a sample."),
        ("How should I label a knitted or crocheted throw?",
         "Use a 20\u201330 x 40\u201360mm label at a dense border or lower corner, Straight Cut (Flat) for a plain "
         "patch or a Centre Fold in the border seam. Avoid lacy edges; sew through stable stitches and add backing if "
         "the yarn is loose or the label is heavy."),
    ]),
]
PLACEMENT_FAQ_FLAT = [qa for _, items in PLACEMENT_FAQ_GROUPS for qa in items]


# ============================================================ ADDED: UAE / international orders page data
INTL_FAQ = [
    ("Do you ship custom woven labels to the UAE and internationally?",
     "Yes. We are a Pakistan-based manufacturer and ship to the UAE and internationally via Skynet Worldwide "
     "Express, typically 2\u20134 days to the UAE once your order is finished and packed."),

    ("How do I pay for an international order?",
     "Payoneer is the easiest option for UAE clients \u2014 you can pay into our Payoneer account by local AED "
     "transfer, the same way you'd pay a UAE business, with no international wire forms. Bank wire transfer is "
     "also available, mainly for larger orders."),

    ("What is the minimum order quantity for export orders?",
     "The same as our Pakistan minimum: 1,000 pieces for apparel labels and 200 pieces for school monograms. "
     "This is what keeps the per-piece rate low for a full production run, wherever the order ships to."),

    ("Can I get a sample before placing a bulk international order?",
     "Yes. You approve a sample before the full order goes into production, so nothing is woven at scale until "
     "you've confirmed the design, size and colours \u2014 the same process as a local order."),

    ("Why don't you show a fixed price for international orders?",
     "Pricing is set per market rather than one global number, since shipping, currency and local competition "
     "differ by country. Send us your country, label type and quantity on WhatsApp and we'll quote it directly."),

    ("Do you work with garment exporters and buyers who need labels matched to buyer specifications?",
     "Yes. We supply brand, size and care labels matched to buyer specifications for garment exporters and "
     "manufacturers who need a consistent set across a production run."),
]


# ============================================================ ADDED: scrolling brand marquee (real client labels)
BRAND_MARQUEE = [
    ("brand-pantone.jpg", "Pantone"),
    ("brand-jumar-jumana.jpg", "Jumar / Jumana"),
    ("brand-alaska.jpg", "Alaska"),
    ("brand-ms-closet.jpg", "MS Closet"),
    ("brand-lubna-ghani.jpg", "Lubna Ghani"),
    ("brand-golden-needle.jpg", "Golden Needle"),
    ("brand-made-in-uae.jpg", "Made in UAE"),
    ("brand-sliky-feather.jpg", "Sliky Feather"),
    ("brand-sawa-grey.jpg", "Sawa"),
    ("brand-sawa-orange.jpg", "Sawa"),
    ("brand-tailored-fit.jpg", "Tailored Fit"),
    ("brand-sara-said.jpg", "By Sara Said"),
    ("brand-marwae.jpg", "Marwa\u00e9"),
    ("brand-ghena.jpg", "Ghena"),
    ("brand-fashions-lead.jpg", "Fashions Lead"),
]


def brand_marquee(depth=0):
    cards = "".join(
        '<div class="brand-card"><img src="%s" alt="Woven label for %s" '
        'loading="lazy" width="132" height="132"><span>%s</span></div>'
        % (asset("assets/img/real/" + f, depth), n, n)
        for f, n in BRAND_MARQUEE)
    # duplicate the set once so the 50%% translateX loop is seamless
    return ('<section class="brand-strip" aria-label="Brands we have woven labels for">'
            '<h2>Real labels we\u2019ve woven</h2>'
            '<div class="brand-track-wrap"><div class="brand-track">' + cards + cards + '</div></div>'
            '</section>')

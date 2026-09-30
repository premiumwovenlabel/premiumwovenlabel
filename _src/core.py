# -*- coding: utf-8 -*-
"""Shared config, SVG helpers and page layout for the Premium Woven Labels site.

Every fact in here comes from the business's own published information:
WhatsApp +92 304 8095202, premiumwovenlabel@gmail.com, Karachi, Pakistan,
Instagram @premium_woven_labels. Nothing is invented.
"""

import json

# ---------------------------------------------------------------- business data
NAME = "Premium Woven Labels"
BASE = "https://premiumwovenlabel.github.io/premiumwovenlabel"   # change to the .com when it goes live
WA_RAW = "923048095202"
WA_DISPLAY = "+92 304 8095202"
EMAIL = "premiumwovenlabel@gmail.com"
CITY = "Karachi"
COUNTRY = "Pakistan"
INSTAGRAM = "https://www.instagram.com/premium_woven_labels/"
YEAR = 2026
GA_ID = ""   # paste your GA4 Measurement ID (G-XXXXXXXXXX) and rebuild to switch analytics on
ANALYTICS = ('<script async src="https://www.googletagmanager.com/gtag/js?id=' + GA_ID + '"></script>\n'
             '<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}'
             'gtag("js",new Date());gtag("config","' + GA_ID + '");</script>\n') if GA_ID else ""

# Minimum order quantities and turnaround, as published by the business.
MOQ_APPAREL = "1,000 pieces"
MOQ_SCHOOL = "200 pieces"
TURNAROUND = "7\u201310 days"

WA_DEFAULT_MSG = "Hi Premium Woven Labels, I would like to get a quote for custom woven labels."


def wa(msg=None):
    from urllib.parse import quote
    return "https://wa.me/%s?text=%s" % (WA_RAW, quote(msg or WA_DEFAULT_MSG))


def asset(path, depth):
    return ("../" * depth) + path


# ---------------------------------------------------------------- navigation
NAV = [
    ("", "Home"),
    ("about/", "About"),
    ("woven-labels/", "Woven Labels"),
    ("services/", "Services"),
    ("how-it-works/", "How It Works"),
    ("gallery/", "Gallery"),
    ("resources/woven-labels-complete-guide/", "Guide"),
    ("faq/", "FAQ"),
    ("contact/", "Contact"),
]

FOOT_SERVICES = [
    ("woven-labels/#brand-labels", "Brand labels"),
    ("woven-labels/#logo-labels", "Logo woven labels"),
    ("woven-labels/#size-labels", "Size labels"),
    ("woven-labels/#care-labels", "Care labels"),
    ("woven-labels/#hang-tags", "Hang tags"),
    ("woven-labels/#monograms", "School monograms"),
]

FOOT_RESOURCES = [
    ("pricing/", "Pricing guide"),
    ("resources/", "All resources"),
    ("resources/woven-labels-complete-guide/", "Woven labels: the complete guide"),
    ("resources/woven-vs-printed-labels/", "Woven vs printed labels"),
    ("resources/custom-woven-label-guide/", "Custom woven label guide"),
    ("resources/woven-label-size-guide/", "Choosing a label size"),
    ("resources/center-fold-vs-end-fold/", "Centre fold vs end fold"),
]

LEGAL = [
    ("privacy-policy/", "Privacy policy"),
    ("terms/", "Terms &amp; conditions"),
    ("refund-policy/", "Refund &amp; cancellation"),
    ("shipping-policy/", "Shipping &amp; delivery"),
]


def url(path, depth):
    pre = "../" * depth
    if path == "":
        return pre if pre else "./"
    return pre + path


def canonical(path):
    return BASE + "/" + path


# ---------------------------------------------------------------- icons
ICON_WA = ('<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12.04 2c-5.46 0-9.9 4.44-9.9 9.9 0 1.75.46 3.45 1.32 4.95L2 22l5.3-1.39a9.86 9.86 0 0 0 4.74 1.21h.01c5.46 0 9.9-4.44 9.9-9.9 0-2.64-1.03-5.13-2.9-7A9.82 9.82 0 0 0 12.04 2zm0 18.02h-.01a8.2 8.2 0 0 1-4.18-1.15l-.3-.18-3.11.82.83-3.04-.2-.31a8.21 8.21 0 0 1-1.26-4.38c0-4.54 3.7-8.23 8.24-8.23 2.2 0 4.27.86 5.82 2.42a8.18 8.18 0 0 1 2.41 5.82c0 4.54-3.7 8.23-8.24 8.23zm4.52-6.16c-.25-.12-1.47-.72-1.69-.81-.23-.08-.39-.12-.56.13-.16.24-.64.8-.79.97-.14.16-.29.18-.54.06-.25-.13-1.05-.39-1.99-1.23-.74-.66-1.23-1.47-1.38-1.72-.14-.25-.01-.38.11-.5.11-.11.25-.29.37-.43.13-.15.17-.25.25-.41.08-.17.04-.31-.02-.43-.06-.12-.56-1.34-.76-1.84-.2-.48-.41-.42-.56-.43h-.48c-.17 0-.43.06-.66.31-.22.25-.87.85-.87 2.07s.89 2.4 1.02 2.56c.12.17 1.75 2.67 4.23 3.74.59.26 1.05.41 1.41.52.59.19 1.13.16 1.56.1.47-.07 1.47-.6 1.67-1.18.21-.58.21-1.07.15-1.18-.06-.1-.23-.16-.48-.28z"/></svg>')

ICON_IG = ('<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 2.16c3.2 0 3.58.01 4.85.07 1.17.05 1.8.25 2.23.41.56.22.96.48 1.38.9.42.42.68.82.9 1.38.16.42.36 1.06.41 2.23.06 1.27.07 1.65.07 4.85s-.01 3.58-.07 4.85c-.05 1.17-.25 1.8-.41 2.23-.22.56-.48.96-.9 1.38-.42.42-.82.68-1.38.9-.42.16-1.06.36-2.23.41-1.27.06-1.65.07-4.85.07s-3.58-.01-4.85-.07c-1.17-.05-1.8-.25-2.23-.41-.56-.22-.96-.48-1.38-.9a3.7 3.7 0 0 1-.9-1.38c-.16-.42-.36-1.06-.41-2.23C2.17 15.58 2.16 15.2 2.16 12s.01-3.58.07-4.85c.05-1.17.25-1.8.41-2.23.22-.56.48-.96.9-1.38.42-.42.82-.68 1.38-.9.42-.16 1.06-.36 2.23-.41C8.42 2.17 8.8 2.16 12 2.16zm0 2.16c-3.14 0-3.51.01-4.75.07-1.15.05-1.77.24-2.18.4-.55.22-.94.47-1.35.88-.41.41-.66.8-.88 1.35-.16.41-.35 1.03-.4 2.18-.06 1.24-.07 1.61-.07 4.75s.01 3.51.07 4.75c.05 1.15.24 1.77.4 2.18.22.55.47.94.88 1.35.41.41.8.66 1.35.88.41.16 1.03.35 2.18.4 1.24.06 1.61.07 4.75.07s3.51-.01 4.75-.07c1.15-.05 1.77-.24 2.18-.4.55-.22.94-.47 1.35-.88.41-.41.66-.8.88-1.35.16-.41.35-1.03.4-2.18.06-1.24.07-1.61.07-4.75s-.01-3.51-.07-4.75c-.05-1.15-.24-1.77-.4-2.18a3.6 3.6 0 0 0-.88-1.35 3.6 3.6 0 0 0-1.35-.88c-.41-.16-1.03-.35-2.18-.4-1.24-.06-1.61-.07-4.75-.07zm0 3.67a5.01 5.01 0 1 1 0 10.02 5.01 5.01 0 0 1 0-10.02zm0 8.26a3.25 3.25 0 1 0 0-6.5 3.25 3.25 0 0 0 0 6.5zm6.38-8.46a1.17 1.17 0 1 1-2.34 0 1.17 1.17 0 0 1 2.34 0z"/></svg>')

ICON_MAIL = ('<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M3 5h18a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1zm9 7.1L4.2 7H4v.6l8 5.2 8-5.2V7h-.2L12 12.1z"/></svg>')


def check(color="#a70c12"):
    return ('<svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true" focusable="false" '
            'fill="none" stroke="%s" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" '
            'style="flex:none;width:20px;height:20px;margin-top:1px">'
            '<path d="M20 6 9 17l-5-5"/></svg>' % color)


def dot_icon(color="#6b6b6b"):
    return ('<svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true" focusable="false" '
            'fill="none" stroke="%s" stroke-width="2.4" stroke-linecap="round" '
            'style="flex:none;width:20px;height:20px"><path d="M5 12h14"/></svg>' % color)


def brand_logo(depth, variant="light", cls=""):
    """The real Premium Woven Labels wordmark. 'light' = black+red, for use on
    cream/white backgrounds. 'dark' = cream+red, for use on ink backgrounds."""
    fname = "logo.png" if variant == "light" else "logo-invert.png"
    return ('<img class="brand-mark-img %s" src="%s" alt="" width="847" height="446" loading="eager">'
            % (cls, asset("assets/img/" + fname, depth)))

# ---------------------------------------------------------------- label artwork
# Three tones derived from the brand's own logo (cream / ink / red) — used for
# schematic label-type illustrations only. Real photos are used everywhere a
# specific finished label is shown.
PALETTES = {
    "ink": ("#1c1c1c", "#f5f4f0", "#9a9a96", "#a70c12"),
    "cream": ("#f5f4f0", "#1c1c1c", "#7a7a76", "#a70c12"),
    "red": ("#a70c12", "#f5f4f0", "#e3b3b5", "#1c1c1c"),
}

_uid = [0]


def label_svg(brand="YOUR BRAND", sub="CUSTOM WOVEN LABEL", palette="midnight",
              shape="rect", fold="flat", ratio=0.30, alt=None, cls=""):
    """Illustrative SVG rendering of a woven label. Not a photograph of customer work."""
    _uid[0] += 1
    uid = "l%d" % _uid[0]
    bg, ink, subc, edge = PALETTES.get(palette, PALETTES["ink"])
    W, H = 420, 260
    lw = 330 if shape != "square" else 200
    lh = int(lw * ratio) if shape != "square" else 150
    if fold == "center" and shape != "square":
        lh = int(lh * 1.5)
    x, y = (W - lw) / 2.0, (H - lh) / 2.0
    r = 16 if shape == "rounded" else (0 if shape == "diecut" else 3)

    def arch(pad=0.0):
        return ("M%s %s L%s %s Q%s %s %s %s L%s %s Z"
                % (x + pad, y + lh - pad, x + pad, y + lh * 0.42,
                   x + lw / 2, y - lh * 0.34 + pad * 1.6, x + lw - pad, y + lh * 0.42,
                   x + lw - pad, y + lh - pad))

    if shape == "diecut":
        body = '<path d="%s" fill="%s"/>' % (arch(), bg)
        tex = '<path d="%s" fill="url(#w%s)"/>' % (arch(), uid)
        stitch = ('<path d="%s" fill="none" stroke="%s" stroke-width="1.4" stroke-dasharray="5 4" opacity=".72"/>'
                  % (arch(7), edge))
    else:
        body = '<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s"/>' % (x, y, lw, lh, r, bg)
        tex = '<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="url(#w%s)"/>' % (x, y, lw, lh, r, uid)
        stitch = ('<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="none" stroke="%s" '
                  'stroke-width="1.4" stroke-dasharray="5 4" opacity=".72"/>'
                  % (x + 6, y + 6, lw - 12, lh - 12, max(0, r - 4), edge))

    # loop tab sits behind the label; fold shading sits in front of it
    back, front = "", ""
    if fold == "center":
        front = ('<rect x="%s" y="%s" width="%s" height="%s" fill="rgba(0,0,0,.28)"/>'
                 '<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="rgba(255,255,255,.26)" stroke-width="1" stroke-dasharray="4 4"/>'
                 % (x, y + lh / 2, lw, lh / 2, x, y + lh / 2, x + lw, y + lh / 2))
    elif fold == "end":
        front = ('<rect x="%s" y="%s" width="18" height="%s" rx="%s" fill="rgba(0,0,0,.32)"/>'
                 '<rect x="%s" y="%s" width="18" height="%s" rx="%s" fill="rgba(0,0,0,.32)"/>'
                 % (x, y, lh, r, x + lw - 18, y, lh, r))
    elif fold == "loop":
        back = ('<path d="M%s %s q34 -34 68 0" fill="none" stroke="%s" stroke-width="16" stroke-linecap="round" opacity=".95"/>'
                % (x + lw / 2 - 34, y + 4, bg))

    cy = y + lh * 0.27 if (fold == "center" and shape != "square") else y + lh / 2.0
    fs = 26 if shape != "square" else 22
    label = alt or ("Illustration of a %s woven label with %s fold in %s thread colours"
                    % (shape, fold, palette))

    return (
        '<svg class="label-svg %s" viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="%s">'
        '<defs><pattern id="w%s" width="4" height="4" patternUnits="userSpaceOnUse">'
        '<path d="M0 .5h4M0 2.5h4" stroke="rgba(255,255,255,.09)" stroke-width="1"/>'
        '<path d="M.5 0v4M2.5 0v4" stroke="rgba(0,0,0,.15)" stroke-width="1"/></pattern>'
        '<filter id="f%s" x="-35%%" y="-35%%" width="170%%" height="180%%">'
        '<feDropShadow dx="0" dy="12" stdDeviation="13" flood-color="#05091c" flood-opacity=".5"/></filter></defs>'
        '<g filter="url(#f%s)">%s%s%s%s%s'
        '<text x="%d" y="%s" text-anchor="middle" dominant-baseline="middle" font-family="Fraunces, Georgia, serif" '
        'font-size="%d" font-weight="600" letter-spacing="1.6" fill="%s">%s</text>'
        '<text x="%d" y="%s" text-anchor="middle" dominant-baseline="middle" font-family="Manrope, Arial, sans-serif" '
        'font-size="9.5" font-weight="700" letter-spacing="3.4" fill="%s">%s</text>'
        '</g></svg>'
        % (cls, W, H, label, uid, uid, uid, back, body, tex, front, stitch,
           W // 2, cy, fs, ink, brand,
           W // 2, cy + fs * 0.92, subc, sub)
    )


# ---------------------------------------------------------------- layout
GA_FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
    'family=Baloo+2:wght@500;600;700;800&family=Manrope:wght@400;500;600;700;800&family=Caveat:wght@600;700&display=swap" media="print" onload="this.media=\'all\'">'
    '<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
    'family=Baloo+2:wght@500;600;700;800&family=Manrope:wght@400;500;600;700;800&family=Caveat:wght@600;700&display=swap"></noscript>'
)


def org_schema():
    base = {
        "@type": ["Organization", "LocalBusiness"],
        "@id": BASE + "/#organization",
        "name": NAME,
        "url": BASE + "/",
        "email": EMAIL,
        "telephone": "+" + WA_RAW,
        "logo": BASE + "/assets/img/logo.png",
        "image": BASE + "/assets/img/og-cover.png",
        "description": (
            "%s is a custom woven label manufacturer based in %s, Pakistan. "
            "It makes custom woven brand labels, logo labels, size labels, care labels, "
            "woven hang tags and school monograms for clothing, fashion and growing brands. "
            "Fold options: Straight Cut, Centre Fold, End Fold, Mitre Fold, Manhattan Fold. "
            "School badges available with sew-on or iron-on backing in circle, shield, "
            "square and custom-cut shapes. Minimum order 1,000 pieces for apparel, "
            "200 pieces for schools. WhatsApp quotes: +%s." % (NAME, CITY, WA_RAW)
        ),
        "address": {
            "@type": "PostalAddress",
            "addressLocality": CITY,
            "addressRegion": "Sindh",
            "addressCountry": "PK",
        },
        "geo": {
            "@type": "GeoCoordinates",
            "latitude": "24.8607",
            "longitude": "67.0011",
        },
        "areaServed": [
            {"@type": "Country", "name": "Pakistan"},
            {"@type": "Country", "name": "United Arab Emirates"},
        ],
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Custom woven label products",
            "itemListElement": [
                {"@type": "Offer", "itemOffered": {"@type": "Product", "name": "Custom woven brand labels"}},
                {"@type": "Offer", "itemOffered": {"@type": "Product", "name": "Logo woven labels"}},
                {"@type": "Offer", "itemOffered": {"@type": "Product", "name": "Size labels"}},
                {"@type": "Offer", "itemOffered": {"@type": "Product", "name": "Care labels"}},
                {"@type": "Offer", "itemOffered": {"@type": "Product", "name": "Woven hang tags"}},
                {"@type": "Offer", "itemOffered": {"@type": "Product", "name": "School monograms and woven badges"}},
            ],
        },
        "sameAs": [INSTAGRAM],
        "contactPoint": [{
            "@type": "ContactPoint",
            "contactType": "sales",
            "telephone": "+" + WA_RAW,
            "email": EMAIL,
            "availableLanguage": ["English", "Urdu"],
        }],
        "priceRange": "Contact for quote",
        "currenciesAccepted": "PKR",
        "paymentAccepted": "Contact for payment details",
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
            "opens": "09:00",
            "closes": "18:00",
        }],
    }
    return base


def website_schema():
    return {
        "@type": "WebSite",
        "@id": BASE + "/#website",
        "url": BASE + "/",
        "name": NAME,
        "publisher": {"@id": BASE + "/#organization"},
        "inLanguage": "en",
    }


def breadcrumbs(items, depth):
    """items: list of (path, name) from home to current page."""
    li = []
    for i, (p, n) in enumerate(items, start=1):
        li.append({"@type": "ListItem", "position": i, "name": n, "item": canonical(p)})
    return {"@type": "BreadcrumbList", "@id": canonical(items[-1][0]) + "#breadcrumb", "itemListElement": li}


def crumb_html(items, depth):
    parts = []
    for i, (p, n) in enumerate(items):
        if i == len(items) - 1:
            parts.append('<span aria-current="page">%s</span>' % n)
        else:
            parts.append('<a href="%s">%s</a><i>/</i>' % (url(p, depth), n))
    return '<nav class="crumbs" aria-label="Breadcrumb">%s</nav>' % "".join(parts)


def header(depth, active):
    nav = "".join(
        '<a href="%s"%s>%s</a>' % (url(p, depth), ' aria-current="page"' if p == active else "", n)
        for p, n in NAV
    )
    mnav = "".join(
        '<a class="m-link" href="%s"%s>%s<i>0%d</i></a>'
        % (url(p, depth), ' aria-current="page"' if p == active else "", n, i + 1)
        for i, (p, n) in enumerate(NAV)
    )
    return (
        '<a class="skip" href="#main">Skip to content</a>'
        '<header class="site-head">'
        '<div class="wrap head-inner">'
        '<a class="brand" href="%(home)s" aria-label="%(name)s — home">%(mark)s</a>'
        '<nav class="nav" aria-label="Main">%(nav)s</nav>'
        '<div class="head-cta">'
        '<a class="icon-wa" href="%(wa)s" target="_blank" rel="noopener" aria-label="Chat with us on WhatsApp">%(ig)s</a>'
        '<a class="btn btn-primary btn-sm btn-quote" href="%(contact)s">Get a free quote</a>'
        '<button class="menu-btn" type="button" aria-expanded="false" aria-controls="mobileMenu" aria-label="Open menu"><span></span></button>'
        '</div></div></header>'
        '<div class="m-menu" id="mobileMenu" aria-hidden="true">'
        '%(mnav)s'
        '<div class="m-actions">'
        '<a class="btn btn-wa btn-lg" href="%(wa)s" target="_blank" rel="noopener">%(ig)s Chat on WhatsApp</a>'
        '<a class="btn btn-ghost btn-lg" href="%(contact)s">Get a free quote</a>'
        '</div>'
        '<div class="m-meta"><a href="mailto:%(email)s">%(email)s</a><span>%(wad)s</span><span>%(city)s, %(country)s</span></div>'
        '</div>'
        % {
            "home": url("", depth), "name": NAME, "mark": brand_logo(depth, "light", "brand-mark--head"),
            "nav": nav, "mnav": mnav,
            "wa": wa(), "ig": ICON_WA, "contact": url("contact/", depth),
            "email": EMAIL, "wad": WA_DISPLAY, "city": CITY, "country": COUNTRY,
        }
    )


def footer(depth):
    def links(items):
        return "".join('<li><a href="%s">%s</a></li>' % (url(p, depth), n) for p, n in items)

    return (
        '<footer class="site-foot">'
        '<div class="wrap">'
        '<div class="foot-grid">'
        '<div class="foot-brand">'
        '<a class="brand" href="%(home)s" aria-label="%(name)s — home">%(mark)s</a>'
        '<p class="foot-blurb">Custom woven branding solutions for clothing, fashion and growing brands. '
        'Made in %(city)s, %(country)s.</p>'
        '<div class="foot-social">'
        '<a href="%(wa)s" target="_blank" rel="noopener" aria-label="WhatsApp">%(iwa)s</a>'
        '<a href="%(ig)s" target="_blank" rel="noopener" aria-label="Instagram">%(iig)s</a>'
        '<a href="mailto:%(email)s" aria-label="Email">%(imail)s</a>'
        '</div></div>'
        '<div class="foot-col"><h2>Site</h2><ul>%(nav)s</ul></div>'
        '<div class="foot-col"><h2>Labels</h2><ul>%(svc)s</ul></div>'
        '<div class="foot-col"><h2>Resources</h2><ul>%(res)s</ul>'
        '<h2 style="margin-top:26px">Contact</h2><ul>'
        '<li><a href="%(wa)s" target="_blank" rel="noopener">%(wad)s</a></li>'
        '<li><a href="mailto:%(email)s">%(email)s</a></li>'
        '<li>%(city)s, %(country)s</li>'
        '<li>Mon&ndash;Sat, 9 am&ndash;6 pm PKT</li>'
        '</ul></div>'
        '</div>'
        '<div class="foot-bottom">'
        '<span>&copy; %(year)d %(name)s. All rights reserved.</span>'
        '<span class="foot-legal">%(legal)s</span>'
        '</div></div></footer>'
        '<a class="fab" href="%(wa)s" target="_blank" rel="noopener" aria-label="Chat with %(name)s on WhatsApp">'
        '%(iwa)s<span>WhatsApp</span></a>'
        % {
            "home": url("", depth), "name": NAME, "mark": brand_logo(depth, "dark", "brand-mark--foot"),
            "city": CITY, "country": COUNTRY,
            "wa": wa(), "ig": INSTAGRAM, "iwa": ICON_WA, "iig": ICON_IG, "imail": ICON_MAIL,
            "email": EMAIL, "wad": WA_DISPLAY, "year": YEAR,
            "nav": links(NAV[1:]),
            "svc": links(FOOT_SERVICES),
            "res": links(FOOT_RESOURCES[:4]),
            "legal": "".join('<a href="%s">%s</a>' % (url(p, depth), n) for p, n in LEGAL),
        }
    )


def page(path, title, desc, body, active=None, depth=None, schema=None, og_type="website", noindex=False):
    if depth is None:
        depth = path.count("/")
    if active is None:
        active = path
    graph = [org_schema(), website_schema()]
    if schema:
        graph.extend(schema if isinstance(schema, list) else [schema])
    jsonld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":"))

    return (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<title>%(title)s</title>\n'
        '<meta name="description" content="%(desc)s">\n'
        '<link rel="canonical" href="%(canon)s">\n'
        '%(robots)s'
        '<meta name="theme-color" content="#0a1130">\n'
        '<meta property="og:type" content="%(ogt)s">\n'
        '<meta property="og:site_name" content="%(name)s">\n'
        '<meta property="og:title" content="%(title)s">\n'
        '<meta property="og:description" content="%(desc)s">\n'
        '<meta property="og:url" content="%(canon)s">\n'
        '<meta property="og:image" content="%(base)s/assets/img/og-cover.png">\n'
        '<meta property="og:image:width" content="1200">\n'
        '<meta property="og:image:height" content="630">\n'
        '<meta property="og:image:alt" content="Premium Woven Labels — custom woven labels for clothing brands">\n'
        '<meta property="og:locale" content="en_US">\n'
        '<meta name="twitter:card" content="summary_large_image">\n'
        '<meta name="twitter:title" content="%(title)s">\n'
        '<meta name="twitter:description" content="%(desc)s">\n'
        '<meta name="twitter:image" content="%(base)s/assets/img/og-cover.png">\n'
        '<link rel="icon" href="%(pre)sassets/img/favicon.svg" type="image/svg+xml">\n'
        '<link rel="apple-touch-icon" href="%(pre)sassets/img/apple-touch-icon.png">\n'
        '<link rel="stylesheet" href="%(pre)sassets/css/style.css">\n'
        '%(fonts)s\n'
        '<script type="application/ld+json">%(jsonld)s</script>\n'
        '</head>\n<body>\n%(header)s\n<main id="main">\n%(body)s\n</main>\n%(footer)s\n'
        '%(analytics)s<script src="%(pre)sassets/js/main.js" defer></script>\n</body>\n</html>\n'
        % { "analytics": ANALYTICS,
            "title": title, "desc": desc, "canon": canonical(path), "base": BASE, "name": NAME,
            "ogt": og_type, "pre": "../" * depth, "fonts": GA_FONTS, "jsonld": jsonld,
            "header": header(depth, active), "body": body, "footer": footer(depth),
            "robots": '<meta name="robots" content="noindex,follow">\n' if noindex else "",
        }
    )


# ---------------------------------------------------------------- reusable blocks
def cta_band(depth, heading="Ready to put your name on it?",
             text="Send your logo or label idea on WhatsApp and we'll come back with a free, no-obligation quote."):
    return (
        '<section class="cta-band"><div class="wrap">'
        '<h2 class="reveal">%s</h2><p class="reveal d1">%s</p>'
        '<div class="btn-row reveal d2">'
        '<a class="btn btn-wa btn-lg" href="%s" target="_blank" rel="noopener">%s Chat on WhatsApp</a>'
        '<a class="btn btn-ghost btn-lg" href="%s">Get a free quote</a>'
        '</div></div></section>'
        % (heading, text, wa(), ICON_WA, url("contact/", depth))
    )


def faq_block(items, open_first=False):
    out = []
    for i, (q, a) in enumerate(items):
        body = "".join("<p>%s</p>" % p for p in (a if isinstance(a, list) else [a]))
        out.append('<details class="faq-item"%s><summary>%s</summary><div class="faq-body">%s</div></details>'
                   % (" open" if (open_first and i == 0) else "", q, body))
    return '<div class="faq-list">%s</div>' % "".join(out)


def faq_schema(items, page_path):
    return {
        "@type": "FAQPage",
        "@id": canonical(page_path) + "#faq",
        "mainEntity": [{
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": " ".join(a) if isinstance(a, list) else a},
        } for q, a in items],
    }

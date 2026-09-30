# -*- coding: utf-8 -*-
"""Legal pages. Anything the business has not confirmed is a marked placeholder."""

from core import (page, url, canonical, breadcrumbs, crumb_html, BASE, NAME,
                  WA_DISPLAY, EMAIL, CITY, COUNTRY, YEAR)

UPDATED = "19 September 2026"


def ph(text):
    return '<mark class="ph">[To confirm: %s]</mark>' % text


def _legal(slug, h1, desc, lead, body_html, title=None):
    d = 1
    crumbs = [("", "Home"), (slug + "/", h1)]
    page_body = (
        '<section class="page-head"><div class="wrap">%s<h1>%s</h1>'
        '<p>Last updated: %s</p></div></section>'
        '<section class="section"><div class="wrap"><div class="prose"><p>%s</p>%s'
        '<h2>Questions about this page</h2>'
        '<p>Contact %s on WhatsApp at %s or by email at <a href="mailto:%s">%s</a>.</p>'
        '</div></div></section>'
        % (crumb_html(crumbs, d), h1, UPDATED, lead, body_html, NAME, WA_DISPLAY, EMAIL, EMAIL)
    )
    return page(slug + "/", (title or h1) + " | " + NAME, desc, page_body, depth=d,
                schema=[breadcrumbs(crumbs, d),
                        {"@type": "WebPage", "@id": canonical(slug + "/") + "#webpage",
                         "url": canonical(slug + "/"), "name": h1,
                         "isPartOf": {"@id": BASE + "/#website"}}])


def privacy():
    body = (
        '<h2>What this site collects</h2>'
        '<p>This website does not run its own database, does not set advertising cookies and does not store form '
        'submissions on the server. The quote form on this site works by opening WhatsApp or your email client with '
        'your details filled in \u2014 you send the message yourself, from your own account.</p>'
        '<p>The site loads web fonts from Google Fonts. Google may log your IP address as part of serving those files. '
        'Everything else on the site is served from this domain.</p>'

        '<h2>Information you send us</h2>'
        '<p>When you contact us on WhatsApp or by email, we receive whatever you choose to send: typically your name, '
        'your brand name, your phone number or email address, your artwork and the details of your enquiry.</p>'

        '<h2>How we use it</h2>'
        '<ul>'
        '<li>To prepare a quote and answer your enquiry.</li>'
        '<li>To produce and deliver your order if you place one.</li>'
        '<li>To keep in touch with you about that order.</li>'
        '</ul>'
        '<p>We do not sell your information, and we do not share it with third parties except where it is necessary to '
        'fulfil your order \u2014 for example, giving a courier the delivery address you provided.</p>'

        '<h2>Your artwork</h2>'
        '<p>Artwork you send us is used to produce your labels and for nothing else. We do not display your artwork as portfolio or sample work without your written permission.</p>'

        '<h2>How long we keep it</h2>'
        '<p>We keep enquiry and order records for as long as they may reasonably be needed to deal with a follow-up question or a dispute. If you ask us to delete your records, we will do so unless we are required to keep them by law.</p>'

        '<h2>Third-party services</h2>'
        '<p>Messages you send us travel through WhatsApp (Meta) or your email provider, and are subject to those '
        'companies\u2019 own privacy policies. This website is hosted on GitHub Pages, whose host may log standard '
        'server request data.</p>'

        '<h2>Your choices</h2>'
        '<p>You can ask us to delete the messages and details you have sent us. Contact us using the details below and '
        'we will confirm when it is done.</p>'

        '<h2>Children</h2>'
        '<p>This site is aimed at businesses and is not directed at children.</p>'

        '<h2>Changes</h2>'
        '<p>If this policy changes, the updated version will be posted on this page with a new date at the top.</p>'
    )
    return _legal("privacy-policy", "Privacy policy",
                  "How Premium Woven Labels handles the information you send when you request a quote for custom "
                  "woven labels. No tracking, no stored form data.",
                  "This page explains what happens to the information you send us when you ask for a quote or place "
                  "an order with %s." % NAME, body)


def terms():
    body = (
        '<h2>Who we are</h2>'
        '<p>%s is a custom woven label business based in %s, %s. You can reach us on WhatsApp at %s or by email at '
        '<a href="mailto:%s">%s</a>.</p>' % (NAME, CITY, COUNTRY, WA_DISPLAY, EMAIL, EMAIL) +

        '<h2>Quotes</h2>'
        '<p>Quotes are free and carry no obligation. A quote is based on the specification you give us \u2014 label type, '
        'size, fold, colours and quantity. If any of that changes, the quote may change with it. ' +
        'Quotes are valid for a reasonable period from the date they are given. If you return to a quote after some time has passed, confirm with us that the price still applies.</p>'

        '<h2>Artwork and approval</h2>'
        '<p>You are responsible for the artwork you send us, including making sure you have the right to use any logo, '
        'trademark or design it contains. We produce labels to the artwork and specification you approve.</p>'
        '<p>You approve a sample before the full order goes into production. Once you have approved it, production runs '
        'to that approved specification \u2014 so please check spelling, capitalisation, sizing and colours carefully at '
        'that stage.</p>'

        '<h2>Orders and payment</h2>'
        '<p>An order is confirmed once you approve the specification and the agreed payment terms are met. ' +
        'Payment is accepted by bank transfer, EasyPaisa or JazzCash. Advance payment is required before production begins; the exact amount depends on the order and is confirmed with you at the time of placing it.</p>'

        '<h2>Production and delivery</h2>'
        '<p>Production time depends on the design, quantity and current workload, and is confirmed with you before you '
        'commit. Delivery terms are covered on our shipping and delivery page.</p>'

        '<h2>Colour and finish</h2>'
        '<p>Thread colours are matched as closely as the weaving process allows. Small variation between a screen '
        'colour, a printed colour reference and woven thread is normal and is not treated as a defect.</p>'

        '<h2>Intellectual property</h2>'
        '<p>You keep the rights to your own logo and artwork. The content, design and code of this website belong to '
        '%s.</p>' % NAME +

        '<h2>Liability</h2>'
        '<p>We are responsible for producing your labels to the approved specification. We are not responsible for '
        'losses arising from errors in artwork you approved, or from delays outside our control such as courier delays. '
        'Our liability is limited to the value of the order in question. We are not liable for indirect or consequential losses.</p>'

        '<h2>Governing law</h2>'
        '<p>These terms are governed by the laws of Pakistan. Any disputes will be subject to the jurisdiction of the courts of Karachi, Pakistan.</p>'

        '<h2>Changes</h2>'
        '<p>These terms may be updated. The version on this page at the time you place an order is the one that applies.</p>'
    )
    return _legal("terms", "Terms &amp; conditions",
                  "Terms for ordering custom woven labels from Premium Woven Labels \u2014 quotes, artwork approval, "
                  "production, colour matching and liability.",
                  "These terms apply when you request a quote or place an order with %s." % NAME, body,
                  title="Terms and conditions")


def refund():
    body = (
        '<h2>Custom-made products</h2>'
        '<p>Woven labels are made to order, to artwork and a specification you approve. Because they carry your brand '
        'and cannot be resold or reused, custom labels are not returnable in the way a stock product would be.</p>'
        '<p>That is exactly why we ask you to approve a sample before the full order is produced \u2014 it is the point '
        'at which anything can still be changed at no cost.</p>'

        '<h2>Cancelling an order</h2>'
        '<ul>'
        '<li><strong>Before production starts:</strong> We work through every detail of your order — design, size, colours, fold and quantity — before production begins, and you confirm everything at that stage. Once an order is confirmed and payment is made, it enters production and cannot be cancelled or refunded.</li>'
        '<li><strong>Once production has started:</strong> an order in production cannot usually be cancelled, because '
        'the material has already been woven to your specification.</li>'
        '</ul>'

        '<h2>If something is wrong with your order</h2>'
        '<p>If your labels do not match the specification you approved, tell us. Send photographs of what you received '
        'along with your order details on WhatsApp and we will look into it and put it right.</p>'
        '<p>Any problem with your order must be reported to us within <strong>7 days</strong> of delivery, with photographs of the issue and your order details sent on WhatsApp or by email.</p>'

        '<h2>What is not covered</h2>'
        '<ul>'
        '<li>Errors in artwork, spelling or sizing that were present in the version you approved.</li>'
        '<li>Normal, small variation between screen colours and woven thread colours.</li>'
        '<li>Damage caused after delivery.</li>'
        '</ul>'

        '<h2>Refund method and timing</h2>'
        '<p>Because woven labels are custom-made to your specific artwork and cannot be reused or resold, we do not offer refunds except where the labels we delivered do not match the specification you approved. In that case, we will either reproduce the affected labels or agree a resolution with you directly.</p>'

        '<h2>How to raise a request</h2>'
        '<p>Message us on WhatsApp at %s or email <a href="mailto:%s">%s</a> with your order details and photographs '
        'where relevant.</p>' % (WA_DISPLAY, EMAIL, EMAIL)
    )
    return _legal("refund-policy", "Refund &amp; cancellation policy",
                  "How cancellations, production errors and refunds work on custom woven label orders from "
                  "Premium Woven Labels.",
                  "Custom woven labels are made to order, so this page explains when an order can be cancelled and "
                  "what happens if something is wrong with what you receive.", body,
                  title="Refund and cancellation policy")


def shipping():
    body = (
        '<h2>Where we deliver</h2>'
        '<p>We deliver across Pakistan, and we can arrange international delivery. Tell us where your order needs to '
        'go and we will confirm the arrangement before dispatch.</p>'

        '<h2>Production time</h2>'
        '<p>Production time depends on your design, the quantity and current workload. We confirm a timeline with you '
        'before you commit to an order, so you always know what to expect before you pay.</p>'
        '<p>Standard production turnaround is 7\u201310 days from order confirmation, for delivery within Pakistan. '
        'International dispatch is arranged separately and confirmed with you before production begins.</p>'

        '<h2>Delivery time</h2>'
        '<p>Delivery times after production is complete:</p><ul><li><strong>Karachi:</strong> approximately 5 days</li><li><strong>Rest of Pakistan:</strong> approximately 7 days</li><li><strong>International (worldwide):</strong> approximately 10 days</li></ul><p>These are estimates and may vary. If your order has a firm deadline, let us know when you place it and we will tell you whether it can be met.</p>'

        '<h2>Delivery charges</h2>'
        '<p>Delivery charges depend on the order size and destination and are confirmed with you before dispatch. Ask us when you place your order and we will include it in the quote.</p>'

        '<h2>Tracking</h2>'
        '<p>We use courier services including TCS for Pakistan deliveries. Tracking details are shared with you once your order has been dispatched.</p>'

        '<h2>Customs and duties on international orders</h2>'
        '<p>International shipments may be subject to import duties, taxes or customs charges in the destination '
        'country. These are set by the destination country, not by us, and are normally the responsibility of the '
        'person receiving the order.</p>'

        '<h2>Delivery problems</h2>'
        '<p>If your order is delayed, damaged in transit or does not arrive, message us on WhatsApp at %s with your '
        'order details and we will follow it up with the courier.</p>' % WA_DISPLAY
    )
    return _legal("shipping-policy", "Shipping &amp; delivery policy",
                  "How custom woven label orders from Premium Woven Labels are produced and delivered across Pakistan "
                  "and internationally.",
                  "This page covers how orders are dispatched and delivered once your labels have been produced.",
                  body, title="Shipping and delivery policy")


ALL_LEGAL = [privacy, terms, refund, shipping]

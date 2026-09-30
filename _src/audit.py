#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Post-build audit: broken links, duplicate SEO tags, heading order, alt text, JSON-LD."""

import os, re, json, sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ERR, WARN = [], []


def err(f, m): ERR.append("%s: %s" % (f, m))
def warn(f, m): WARN.append("%s: %s" % (f, m))


class P(HTMLParser):
    VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
            "meta", "param", "source", "track", "wbr", "path", "rect", "circle",
            "line", "polygon", "polyline", "stop", "use", "feDropShadow", "ellipse"}

    def __init__(self, fn):
        super().__init__(convert_charrefs=True)
        self.fn = fn
        self.stack = []
        self.links = []
        self.headings = []
        self.imgs = []
        self.svgs = 0
        self.svg_labelled = 0
        self.ids = []
        self.labels = []
        self.inputs = []
        self.buttons = 0
        self.in_script = False
        self.jsonld = []
        self._buf = ""

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag not in self.VOID:
            self.stack.append(tag)
        if a.get("id"):
            self.ids.append(a["id"])
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        if tag in ("h1", "h2", "h3", "h4"):
            self.headings.append(tag)
        if tag == "img":
            self.imgs.append(a)
        if tag == "svg":
            self.svgs += 1
            if a.get("aria-label") or a.get("aria-hidden") == "true" or a.get("role") == "img":
                self.svg_labelled += 1
        if tag == "label" and a.get("for"):
            self.labels.append(a["for"])
        if tag in ("input", "select", "textarea"):
            self.inputs.append(a)
        if tag == "script":
            self.in_script = a.get("type") == "application/ld+json"
            self._buf = ""

    def handle_endtag(self, tag):
        if tag in self.VOID:
            return
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        elif tag in self.stack:
            err(self.fn, "mis-nested </%s> (open: %s)" % (tag, self.stack[-3:]))
            while self.stack and self.stack.pop() != tag:
                pass
        if tag == "script" and self.in_script:
            self.jsonld.append(self._buf)
            self.in_script = False

    def handle_data(self, d):
        if self.in_script:
            self._buf += d


def rel_target(page_rel, href):
    """Resolve an href found in page_rel to a repo path, or None if external/anchor."""
    if re.match(r"^(https?:|mailto:|tel:|#|data:)", href):
        return None
    href = href.split("#")[0]
    if not href:
        return None
    base = os.path.dirname(page_rel)
    return os.path.normpath(os.path.join(base, href))


def main():
    html_files = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in ("_src", ".git")]
        for fn in filenames:
            if fn.endswith(".html"):
                html_files.append(os.path.relpath(os.path.join(dirpath, fn), ROOT))
    html_files.sort()

    titles, descs, canons = {}, {}, {}

    for rel in html_files:
        with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
            src = f.read()
        p = P(rel)
        p.feed(src)
        if p.stack:
            err(rel, "unclosed tags: %s" % p.stack)

        # --- head tags
        t = re.search(r"<title>(.*?)</title>", src, re.S)
        d = re.search(r'<meta name="description" content="(.*?)">', src, re.S)
        c = re.search(r'<link rel="canonical" href="(.*?)">', src)
        if not t: err(rel, "no <title>")
        if not d: err(rel, "no meta description")
        if not c: err(rel, "no canonical")
        if t:
            titles.setdefault(t.group(1), []).append(rel)
            if len(t.group(1)) > 65: warn(rel, "title %d chars" % len(t.group(1)))
        if d:
            descs.setdefault(d.group(1), []).append(rel)
            n = len(d.group(1))
            if n > 165: warn(rel, "meta description %d chars" % n)
            if n < 70: warn(rel, "meta description only %d chars" % n)
        if c:
            canons.setdefault(c.group(1), []).append(rel)
        for tag in ['property="og:title"', 'property="og:image"', 'property="og:url"',
                    'name="twitter:card"', 'property="og:description"']:
            if tag not in src: err(rel, "missing %s" % tag)

        # --- headings
        h1 = p.headings.count("h1")
        if h1 != 1: err(rel, "%d <h1> tags" % h1)
        order = [int(h[1]) for h in p.headings]
        for a, b in zip(order, order[1:]):
            if b - a > 1:
                warn(rel, "heading jump h%d -> h%d" % (a, b))
                break

        # --- images & svg
        for a in p.imgs:
            if "alt" not in a: err(rel, "img without alt: %s" % a.get("src"))
        if p.svgs != p.svg_labelled:
            err(rel, "%d of %d svg without aria-label/aria-hidden" % (p.svgs - p.svg_labelled, p.svgs))

        # --- form labels
        for a in p.inputs:
            if a.get("type") == "hidden":
                continue
            i = a.get("id")
            if not i:
                err(rel, "form control without id")
            elif i not in p.labels and not a.get("aria-label"):
                err(rel, "no <label for> matching #%s" % i)

        # --- duplicate ids
        dupes = {i for i in p.ids if p.ids.count(i) > 1}
        if dupes: err(rel, "duplicate ids: %s" % sorted(dupes))

        # --- links
        for href in p.links:
            tgt = rel_target(rel, href)
            if tgt is None:
                continue
            full = os.path.join(ROOT, tgt)
            if os.path.isdir(full):
                full = os.path.join(full, "index.html")
            if not os.path.exists(full):
                err(rel, "broken link -> %s" % href)

        # --- in-page anchors
        for href in p.links:
            if href.startswith("#") and len(href) > 1:
                if href[1:] not in p.ids:
                    err(rel, "anchor not found: %s" % href)

        # --- json-ld
        for j in p.jsonld:
            try:
                json.loads(j)
            except Exception as e:
                err(rel, "invalid JSON-LD: %s" % e)

        # --- assets referenced
        for m in re.finditer(r'(?:href|src)="((?:\.\./)*assets/[^"]+)"', src):
            tgt = rel_target(rel, m.group(1))
            if tgt and not os.path.exists(os.path.join(ROOT, tgt)):
                err(rel, "missing asset -> %s" % m.group(1))

        # --- contact details never invented
        for m in re.finditer(r"wa\.me/(\d+)", src):
            if m.group(1) != "923048095202":
                err(rel, "unexpected WhatsApp number %s" % m.group(1))

    for k, v in titles.items():
        if len(v) > 1: err(", ".join(v), "duplicate title: %s" % k[:50])
    for k, v in descs.items():
        if len(v) > 1: err(", ".join(v), "duplicate meta description")
    for k, v in canons.items():
        if len(v) > 1: err(", ".join(v), "duplicate canonical: %s" % k)

    # --- sitemap covers every indexable page
    sm = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
    for rel in html_files:
        src = open(os.path.join(ROOT, rel), encoding="utf-8").read()
        if "noindex" in src:
            continue
        canon = re.search(r'<link rel="canonical" href="(.*?)">', src).group(1)
        if canon not in sm:
            err(rel, "not in sitemap.xml")
    for m in re.finditer(r"<loc>(.*?)</loc>", sm):
        path = m.group(1).split("/premiumwovenlabel/")[-1]
        f = os.path.join(ROOT, path, "index.html") if path else os.path.join(ROOT, "index.html")
        if not os.path.exists(f):
            err("sitemap.xml", "points at missing page: %s" % m.group(1))

    print("Audited %d HTML pages" % len(html_files))
    import os as _os, re as _re
    _root = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
    for _dp, _dn, _fn in _os.walk(_root):
        if "_src" in _dp.split(_os.sep):
            continue
        for _f in _fn:
            if _f.endswith(".html"):
                _p = _os.path.join(_dp, _f)
                if _re.search(r"%\(\w+\)s", open(_p, encoding="utf-8").read()):
                    err(_os.path.relpath(_p, _root), "unrendered template token such as %(name)s")
    print("\nERRORS (%d)" % len(ERR))
    for e in ERR: print("  x " + e)
    print("\nWARNINGS (%d)" % len(WARN))
    for w in WARN: print("  ! " + w)
    return 1 if ERR else 0


if __name__ == "__main__":
    sys.exit(main())

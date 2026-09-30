# -*- coding: utf-8 -*-
"""Renders the Woven Labels complete guide (Markdown) into HTML for the article template.

Edit _src/content/woven-labels-complete-guide.md, run build.py - nothing else to change.
"""
import html
import re

from core import faq_block


def _plain(t):
    return re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", t).replace("**", "").strip()


def _inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    return re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)",
                  r'<a href="\2" target="_blank" rel="noopener">\1</a>', t)


def _slug(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")


def _cells(row):
    return [c.strip() for c in row.strip().strip("|").split("|")]


def _table(rows):
    head, body = _cells(rows[0]), [_cells(r) for r in rows[2:]]
    rowhead = "label" not in head[0].lower()   # side-by-side comparisons have no row headers
    th = "".join('<th scope="col">%s</th>' % _inline(c) for c in head)
    tr = ""
    for r in body:
        first = ('<th scope="row">%s</th>' if rowhead else "<td>%s</td>") % _inline(r[0])
        tr += "<tr>%s%s</tr>" % (first, "".join("<td>%s</td>" % _inline(c) for c in r[1:]))
    return ('<div class="table-scroll"><table class="key-table"><thead><tr>%s</tr></thead>'
            '<tbody>%s</tbody></table></div>' % (th, tr))


def render(path):
    text = open(path, encoding="utf-8").read()
    lines, n = text.splitlines(), len(text.splitlines())
    meta, title, i = {}, "", 0
    while i < n and lines[i].strip() != "---":
        s = lines[i].strip()
        if s.startswith("# "):
            title = s[2:].strip()
        m = re.match(r"\*\*(.+?):\*\*\s*(.*)$", s)
        if m:
            meta[m.group(1).strip().lower()] = m.group(2).strip()
        i += 1
    out, toc, faqs = [], [], []
    i += 1
    while i < n:
        s = lines[i].strip()
        if not s or s == "---":
            i += 1
        elif s.startswith("## "):
            h = s[3:].strip()
            toc.append((_slug(h), html.escape(h, quote=False)))
            out.append('<h2 id="%s">%s</h2>' % (_slug(h), _inline(h)))
            i += 1
            if h.lower().startswith("frequently asked"):
                items = []
                while i < n and not lines[i].startswith("## "):
                    q = lines[i].strip()
                    if q.startswith("### "):
                        ans, i = [], i + 1
                        while i < n and not lines[i].lstrip().startswith(("#", "---")):
                            if lines[i].strip():
                                ans.append(lines[i].strip())
                            i += 1
                        items.append((q[4:].strip(), ans))
                    else:
                        i += 1
                faqs = [(_plain(q), " ".join(_plain(a) for a in ans)) for q, ans in items]
                out.append(faq_block([(_inline(q), [_inline(a) for a in ans]) for q, ans in items]))
        elif s.startswith("### "):
            out.append("<h3>%s</h3>" % _inline(s[4:].strip()))
            i += 1
        elif s.startswith("|"):
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append(lines[i])
                i += 1
            out.append(_table(rows))
        elif s.startswith(">"):
            q = []
            while i < n and lines[i].strip().startswith(">"):
                q.append(lines[i].strip().lstrip(">").strip())
                i += 1
            out.append("<blockquote><p>%s</p></blockquote>" % _inline(" ".join(q)))
        elif re.match(r"(-|\d+\.)\s", s):
            tag, items = ("ul" if s.startswith("-") else "ol"), []
            while i < n and re.match(r"(-|\d+\.)\s", lines[i].strip()):
                items.append(re.sub(r"^(-|\d+\.)\s+", "", lines[i].strip()))
                i += 1
            out.append("<%s>%s</%s>" % (tag, "".join("<li>%s</li>" % _inline(x) for x in items), tag))
        else:
            p, i = [s], i + 1
            while i < n and lines[i].strip() and not re.match(r"(#|\||>|-\s|\d+\.\s|---)", lines[i].strip()):
                p.append(lines[i].strip())
                i += 1
            out.append("<p>%s</p>" % _inline(" ".join(p)))
    words = len(re.findall(r"\w+", text))
    return {"title": title, "seo_title": html.escape(meta.get("seo title", title), quote=False),
            "desc": meta.get("meta description", ""), "toc": toc, "body": "".join(out),
            "faqs": faqs, "mins": max(1, round(words / 220))}

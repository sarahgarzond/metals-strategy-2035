#!/usr/bin/env python3
"""Build report/report.pdf from sections/*.md. See SKILL.md."""
import csv, datetime, glob, html, os, re, subprocess, sys
import markdown

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
SKILL = os.path.dirname(os.path.abspath(__file__))
OUT_HTML = os.path.join(ROOT, "report", "report.html")
OUT_PDF = os.path.join(ROOT, "report", "report.pdf")
MAX_PAGES = 30
TEAM = os.environ.get("REPORT_TEAM", "Consulting team: Member 1, Member 2, Member 3, Member 4 &nbsp;|&nbsp; Technical University of Munich")


def load_sources():
    path = os.path.join(ROOT, "data", "sources.csv")
    if not os.path.exists(path):
        return {}
    with open(path, newline="", encoding="utf-8") as f:
        return {r["data_id"]: r for r in csv.DictReader(f)}


def _year(s):
    d = (s.get("pub_date") or s.get("year") or "").strip()
    return d[:4] if d[:4].isdigit() else "n.d."


def _esc(t):
    return html.escape(t or "")


def _end(t):
    t = (t or "").strip()
    return t if t.endswith((".", "?", "!")) else t + "."


def apa_reference(s, suffix):
    """One APA 7 reference list entry as HTML."""
    author = (s.get("author") or s.get("publisher") or "").strip()
    date = (s.get("pub_date") or s.get("year") or "n.d.").strip()
    if suffix:
        date = date[:4] + suffix + date[4:] if date[:4].isdigit() else date + "-" + suffix
    title = (s.get("title") or s.get("source") or "").strip()
    rtype = (s.get("ref_type") or "webpage").strip()
    container, pub = (s.get("container") or "").strip(), (s.get("apa_publisher") or "").strip()
    parts = [_esc(_end(author)), f"({_esc(date)})."]
    if rtype == "journal":
        parts.append(_esc(_end(title)))
        tail = f"<i>{_esc(container)}</i>"
        if s.get("volume"):
            tail += f", <i>{_esc(s['volume'])}</i>"
            if s.get("issue"):
                tail += f"({_esc(s['issue'])})"
        if s.get("pages"):
            tail += f", {_esc(s['pages'])}"
        parts.append(tail + ".")
    else:
        parts.append(f"<i>{_esc(_end(title))}</i>")
        extra = container or pub
        if extra and extra != author:
            parts.append(_esc(_end(extra)))
    link = f"https://doi.org/{s['doi']}" if s.get("doi") else (s.get("url") or "")
    if link.startswith("http"):
        parts.append(f'<a href="{_esc(link)}">{_esc(link)}</a>')
    return " ".join(parts)


def cite(md, sources):
    """APA 7 citations. [ID] or [ID1, ID2] gives (Author, Year), [@ID] gives Author (Year)."""
    pattern = re.compile(r"\[(@?)([A-Z][A-Z0-9_]+(?:\s*,\s*[A-Z][A-Z0-9_]+)*)\](?!\()")
    used, warn = [], []
    for m in pattern.finditer(md):
        for i in [x.strip() for x in m.group(2).split(",")]:
            (used if i in sources else warn).append(i)
    used = list(dict.fromkeys(used))
    # same author and year gets a, b, c ordered by title (APA 7 section 8.19)
    groups, suffix = {}, {}
    for i in used:
        s = sources[i]
        groups.setdefault(((s.get("intext_author") or s.get("author") or "").strip(), _year(s)), []).append(i)
    for ids in groups.values():
        if len(ids) > 1:
            for k, i in enumerate(sorted(ids, key=lambda x: (sources[x].get("title") or "").lower())):
                suffix[i] = "abcdefghijklmnopqrstuvwxyz"[k]

    def who(i):
        s = sources[i]
        return (s.get("intext_author") or s.get("author") or s.get("publisher") or "").strip()

    def yr(i):
        y = _year(sources[i])
        return y + ("-" if y == "n.d." and suffix.get(i) else "") + suffix.get(i, "")

    def rep(m):
        narrative = m.group(1) == "@"
        ids = [x.strip() for x in m.group(2).split(",")]
        bad = "".join(f'<span class="cite bad">[?{i}]</span>' for i in ids if i not in sources)
        ids = [i for i in ids if i in sources]
        if not ids:
            return bad
        if narrative:
            return " and ".join(f"{_esc(who(i))} ({yr(i)})" for i in ids) + bad
        by_author = {}
        for i in ids:
            by_author.setdefault(who(i), []).append(yr(i))
        inner = "; ".join(f"{_esc(a)}, {', '.join(sorted(ys))}" for a, ys in sorted(by_author.items(), key=lambda x: x[0].lower()))
        return f"({inner})" + bad

    md = pattern.sub(rep, md)
    order = sorted(used, key=lambda i: ((sources[i].get("author") or "").lower(), _year(sources[i]), suffix.get(i, "")))
    refs = "\n".join(f'<p class="ref">{apa_reference(sources[i], suffix.get(i, ""))}</p>' for i in order)
    return md, refs, sorted(set(warn))


def toc_entries(content_html):
    return [(lvl, re.sub("<[^>]+>", "", t)) for lvl, t in re.findall(r"<h([12])[^>]*>(.*?)</h\1>", content_html)]


def toc_html(entries, pages):
    li = []
    for lvl, t in entries:
        n = pages.get(t, "")
        li.append(f'<li class="l{lvl}"><span class="t">{html.escape(t)}</span><span class="d"></span><span class="n">{n}</span></li>')
    return "\n".join(li)


def render(page_html):
    with open(OUT_HTML, "w", encoding="utf-8") as f:
        f.write(page_html)
    subprocess.run(["node", os.path.join(SKILL, "render.js"), OUT_HTML, OUT_PDF], check=True,
                   env={**os.environ, "NODE_PATH": subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()})


def find_pages(entries):
    pages = {}
    n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", OUT_PDF], capture_output=True, text=True).stdout).group(1))
    texts = [subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), "-layout", OUT_PDF, "-"], capture_output=True, text=True).stdout
             for p in range(1, n + 1)]
    for _, t in entries:
        key = re.sub(r"\s+", " ", t).strip()[:40]
        for p in range(3, n + 1):  # skip cover and table of contents
            if key in re.sub(r"\s+", " ", texts[p - 1]):
                pages[t] = p
                break
    return pages, n


def main():
    files = sorted(glob.glob(os.path.join(ROOT, "sections", "*.md")))
    if not files:
        sys.exit("No sections/*.md found")
    md = "\n\n".join(open(f, encoding="utf-8").read() for f in files)
    md, refs, warn = cite(md, load_sources())
    content = markdown.markdown(md, extensions=["tables", "md_in_html", "attr_list"])
    content = content.replace('src="fig/', 'src="fig/')
    entries = toc_entries(content)
    tpl = open(os.path.join(SKILL, "template.html"), encoding="utf-8").read()
    base = (tpl.replace("{{TEAM}}", TEAM).replace("{{DATE}}", datetime.date.today().strftime("%B %Y"))
               .replace("{{CONTENT}}", content).replace("{{REFS}}", refs))
    render(base.replace("{{TOC}}", toc_html(entries, {})))
    pages, _ = find_pages(entries)
    render(base.replace("{{TOC}}", toc_html(entries, pages)))
    _, n = find_pages(entries)
    for w in warn:
        print(f"WARNING unknown citation id: {w}")
    print(f"Built {OUT_PDF} with {n} pages")
    if n > MAX_PAGES:
        print(f"FAIL: {n} pages exceeds the {MAX_PAGES} page limit")
        sys.exit(1)


if __name__ == "__main__":
    main()

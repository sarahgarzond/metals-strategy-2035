#!/usr/bin/env python3
"""Build report/report.pdf from sections/*.md. See SKILL.md."""
import csv, datetime, difflib, glob, html, json, os, re, subprocess, sys
import markdown

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
SKILL = os.path.dirname(os.path.abspath(__file__))
OUT_HTML = os.path.join(ROOT, "report", "report.html")
OUT_PDF = os.path.join(ROOT, "report", "report.pdf")
MAX_PAGES = 30  # main text: title page up to the end of the Conclusion (references and appendices excluded)
AUTHORS = os.environ.get("REPORT_AUTHORS", "Olivia Calistus, Sarah Garzon Diaz and Juhee Kim")
DATE = os.environ.get("REPORT_DATE", "6 December 2026")


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
    for i, s in sources.items():
        if (s.get("always_include") or "").lower() == "yes":
            lab = (s.get("pub_date") or "").split(",")[0].strip()
            key = ((s.get("intext_author") or s.get("author") or "").strip(), lab[:4] if lab[:4].isdigit() else "n.d.")
            if key in groups and lab[-1:].isalpha():
                groups[key].append("__taken__" + lab[-1])
    for ids in groups.values():
        taken = {x[-1] for x in ids if x.startswith("__taken__")}
        ids = [x for x in ids if not x.startswith("__taken__")]
        if taken:
            letters = list("abcdefghijklmnopqrstuvwxyz") + [x + y for x in "abcdefghijklmnopqrstuvwxyz" for y in "abcdefghijklmnopqrstuvwxyz"]
            free = [c for c in letters if c not in taken]
            for k, i in enumerate(sorted(ids, key=lambda x: (sources[x].get("title") or "").lower())):
                suffix[i] = free[k]
            continue
        if len(ids) > 1:
            for k, i in enumerate(sorted(ids, key=lambda x: (sources[x].get("title") or "").lower())):
                suffix[i] = (list("abcdefghijklmnopqrstuvwxyz") + [x + y for x in "abcdefghijklmnopqrstuvwxyz" for y in "abcdefghijklmnopqrstuvwxyz"])[k]

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
    used = list(dict.fromkeys(used + [i for i, s in sources.items() if (s.get("always_include") or "").lower() == "yes"]))
    order = sorted(used, key=lambda i: ((sources[i].get("author") or "").lower(), _year(sources[i]), suffix.get(i, "")))
    def entry(i):
        s = sources[i]
        if s.get("apa_reference_html"):
            return re.sub(r"(https?://[^\s<]+)", r'<a href="\1">\1</a>', s["apa_reference_html"])
        return apa_reference(s, suffix.get(i, ""))
    refs = "\n".join(f'<p class="ref">{entry(i)}</p>' for i in order)
    return md, refs, sorted(set(warn))


def decorate(content):
    """Number spans in headings, table captions and source lines, as in the team's document."""
    def head(m):
        tag, txt = m.group(1), m.group(2)
        n = re.match(r"^((?:\d+(?:\.\d+)*\.?)|(?:A\d+))\s+(.*)$", txt)
        return f"<{tag}><span class=\"num\">{n.group(1)}</span>{n.group(2)}</{tag}>" if n else m.group(0)
    content = re.sub(r"<(h[123])>(.*?)</\1>", head, content)
    content = re.sub(r"<p>(Table \d+:)", r'<p class="caption">\1', content)
    content = re.sub(r"<p>(Figure \d+:)", r'<p class="caption">\1', content)
    content = re.sub(r"<p><em>(Sources?:)", r'<p class="source"><em>\1', content)
    return content


def toc_entries(full_html):
    out = []
    for lvl, t in re.findall(r"<h([12])[^>]*>(.*?)</h\1>", full_html):
        t = re.sub(r'<span class="num">(.*?)</span>', r"\1 ", t)
        out.append((int(lvl), html.unescape(re.sub("<[^>]+>", "", t)).strip()))
    return out


def toc_html(entries, pages):
    li = []
    for lvl, t in entries:
        gap = " gap" if t == "References" else ""
        li.append(f'<li class="l{lvl}{gap}"><span class="t">{html.escape(t)}</span><span class="d"></span>'
                  f'<span class="n">{pages.get(t, "")}</span></li>')
    return "\n".join(li)


def node_env():
    root = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()
    return {**os.environ, "NODE_PATH": root}


def render(page_html):
    """Render with the page number header, then swap in a title page without header (as in the Google Doc)."""
    build = os.path.join(ROOT, "report", "build")
    os.makedirs(build, exist_ok=True)
    with open(OUT_HTML, "w", encoding="utf-8") as f:
        f.write(page_html)
    js = os.path.join(SKILL, "render.js")
    full, plain = os.path.join(build, "full.pdf"), os.path.join(build, "plain.pdf")
    subprocess.run(["node", js, OUT_HTML, full], check=True, env=node_env())
    subprocess.run(["node", js, OUT_HTML, plain, "noheader"], check=True, env=node_env())
    for f in os.listdir(build):
        if f.startswith("pg-"):
            os.remove(os.path.join(build, f))
    subprocess.run(["pdfseparate", full, os.path.join(build, "pg-full-%04d.pdf")], check=True)
    subprocess.run(["pdfseparate", "-f", "1", "-l", "1", plain, os.path.join(build, "pg-cover-%04d.pdf")], check=True)
    parts = [os.path.join(build, "pg-cover-0001.pdf")] + sorted(
        os.path.join(build, f) for f in os.listdir(build) if f.startswith("pg-full-"))[1:]
    subprocess.run(["pdfunite", *parts, OUT_PDF], check=True)


def page_texts():
    n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", OUT_PDF], capture_output=True, text=True).stdout).group(1))
    return [re.sub(r"\s+", " ", subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), "-layout", OUT_PDF, "-"],
                                                 capture_output=True, text=True).stdout) for p in range(1, n + 1)]


def find_pages(entries):
    texts = page_texts()
    # the table of contents ends on the first page that lists the last entry
    last_key = re.sub(r"\s+", " ", entries[-1][1]).strip()[:45]
    first = next((p + 1 for p in range(2, len(texts) + 1) if last_key in texts[p - 1]), 3)
    pages, start = {}, first
    for _, t in entries:
        key = re.sub(r"\s+", " ", t).strip()[:45]
        for p in range(start, len(texts) + 1):
            if key in texts[p - 1]:
                pages[t] = p
                start = p
                break
    return pages, texts


def main():
    files = sorted(glob.glob(os.path.join(ROOT, "sections", "*.md")))
    if not files:
        sys.exit("No sections/*.md found")
    main_files = [f for f in files if "append" not in os.path.basename(f)]
    app_files = [f for f in files if "append" in os.path.basename(f)]
    sources = load_sources()
    md_main = "\n\n".join(open(f, encoding="utf-8").read() for f in main_files)
    md_app = "\n\n".join(open(f, encoding="utf-8").read() for f in app_files)
    sep = "\n\n<!--APPENDIX-SPLIT-->\n\n"
    md_all, refs, warn = cite(md_main + sep + md_app, sources)
    md_main, md_app = md_all.split("<!--APPENDIX-SPLIT-->")
    conv = lambda m: decorate(markdown.markdown(m, extensions=["tables", "md_in_html", "attr_list"]))
    content, appendix = conv(md_main), conv(md_app)
    appendix = f'<div class="appendix">{appendix}</div>' if appendix.strip() else ""
    tpl = open(os.path.join(SKILL, "template.html"), encoding="utf-8").read()
    base = (tpl.replace("{{AUTHORS}}", html.escape(AUTHORS)).replace("{{DATE}}", html.escape(DATE))
               .replace("{{CONTENT}}", content).replace("{{REFS}}", refs).replace("{{APPENDIX}}", appendix))
    entries = toc_entries(base.split("{{TOC}}")[1])
    render(base.replace("{{TOC}}", toc_html(entries, {})))
    pages, _ = find_pages(entries)
    render(base.replace("{{TOC}}", toc_html(entries, pages)))
    pages, texts = find_pages(entries)
    n = len(texts)
    main_pages = (pages.get("References", n + 1) - 1)
    if pages.get("References") and pages["References"] == pages.get("9. Conclusion"):
        main_pages = pages["References"]
    for w in warn:
        print(f"WARNING unknown citation id: {w}")
    toc = [(lvl, t) for lvl, t in json.load(open(os.path.join(ROOT, "data", "toc.json")))["entries"]]
    norm_t = lambda s: re.sub(r"[.\s]+", " ", s).strip()
    body = [(lvl, norm_t(t)) for lvl, t in entries]
    want = [(lvl, norm_t(t)) for lvl, t in toc]
    if body != want:
        for d in difflib.unified_diff([f"{l} {t}" for l, t in want], [f"{l} {t}" for l, t in body], "table of contents", "body headings", lineterm="", n=0):
            print("TOC MISMATCH", d)
        print("FAIL: chapter and section headings must match data/toc.json (subsections below them may change)")
        sys.exit(1)
    missing = [t for _, t in entries if t not in pages]
    if missing:
        print("WARNING headings not found for the table of contents:", missing)
    print(f"Built {OUT_PDF}: {n} pages in total, main text (title page to Conclusion) {main_pages} pages")
    if main_pages > MAX_PAGES:
        print(f"FAIL: main text has {main_pages} pages, the limit is {MAX_PAGES}")
        sys.exit(1)


if __name__ == "__main__":
    main()

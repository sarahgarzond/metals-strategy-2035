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


def cite(md, sources):
    order, warn = [], []

    def rep(m):
        out = []
        for i in [x.strip() for x in m.group(1).split(",")]:
            if i not in sources:
                warn.append(i); out.append(f'<span class="cite bad">[?{i}]</span>'); continue
            if i not in order:
                order.append(i)
            out.append(str(order.index(i) + 1))
        nums = [o for o in out if not o.startswith("<")]
        bad = "".join(o for o in out if o.startswith("<"))
        return (f'<span class="cite">[{",".join(nums)}]</span>' if nums else "") + bad

    md = re.sub(r"\[([A-Z][A-Z0-9_]+(?:\s*,\s*[A-Z][A-Z0-9_]+)*)\](?!\()", rep, md)
    refs = []
    for i in order:
        s = sources[i]
        url = f' <a href="{html.escape(s["url"])}">{html.escape(s["url"])}</a>' if s.get("url") else ""
        refs.append(f'<li>{html.escape(s.get("publisher") or "")}: {html.escape(s.get("source") or "")}'
                    f' ({html.escape(s.get("year") or "")}).{url} Retrieved {html.escape(s.get("retrieved") or "")}.</li>')
    return md, "\n".join(refs), sorted(set(warn))


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

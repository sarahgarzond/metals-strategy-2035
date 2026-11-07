#!/usr/bin/env python3
"""Read any web page or PDF through this container's network (use it when WebFetch fails with DNS or host errors).

  python3 tools/read_url.py <url> [--grep "word|other"] [--pages 10-25] [--max 20000]

Downloads to research/_cache/ (kept out of git), converts PDFs with pdftotext (page markers === PAGE n ===)
and HTML to plain text, then prints the text (or only lines matching --grep, with page numbers).
"""
import argparse, hashlib, html, os, re, subprocess, sys, urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CACHE = os.path.join(ROOT, "research", "_cache")
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"

ap = argparse.ArgumentParser()
ap.add_argument("url"); ap.add_argument("--grep", default=""); ap.add_argument("--pages", default=""); ap.add_argument("--max", type=int, default=20000)
a = ap.parse_args()
os.makedirs(CACHE, exist_ok=True)
key = hashlib.sha1(a.url.encode()).hexdigest()[:16]
raw = os.path.join(CACHE, key + ".bin")
if not os.path.exists(raw):
    ua = os.environ.get("RESEARCH_USER_AGENT", "metals-strategy-2035 research (TUM project study)") if "sec.gov" in a.url else UA
    req = urllib.request.Request(a.url, headers={"User-Agent": ua, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r, open(raw, "wb") as f:
            f.write(r.read())
    except Exception as e:  # noqa: BLE001
        sys.exit(f"DOWNLOAD FAILED {a.url}: {e}")
data = open(raw, "rb").read()
if data[:4] == b"%PDF":
    args = ["pdftotext", "-layout"]
    if a.pages:
        f, _, l = a.pages.partition("-")
        args += ["-f", f, "-l", l or f]
    txt = subprocess.run(args + [raw, "-"], capture_output=True, text=True).stdout
    start = int(a.pages.partition("-")[0]) if a.pages else 1
    pages = txt.split("\f")
    txt = "\n".join(f"=== PAGE {start + i} ===\n{p}" for i, p in enumerate(pages) if p.strip())
else:
    s = data.decode("utf-8", "replace")
    s = re.sub(r"(?is)<(script|style|noscript|svg).*?</\1>", " ", s)
    s = re.sub(r"(?i)<a [^>]*href=\"([^\"]+\.pdf[^\"]*)\"[^>]*>", r" [PDF: \1] ", s)
    s = re.sub(r"(?s)<[^>]+>", "\n", s)
    txt = re.sub(r"\n\s*\n+", "\n", html.unescape(s))
if a.grep:
    page, out = "?", []
    for line in txt.splitlines():
        m = re.match(r"=== PAGE (\d+) ===", line)
        if m:
            page = m.group(1); continue
        if re.search(a.grep, line, re.I):
            out.append(f"[p.{page}] {line.strip()}")
    txt = "\n".join(out)
print(txt[: a.max])

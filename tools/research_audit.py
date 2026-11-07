#!/usr/bin/env python3
"""Research depth gate. Checks every research note against data/source_matrix.json before any writing starts.

Usage: python3 tools/research_audit.py [research/sectors/aerospace.md ...]     (default: all notes)
Exit code 1 if any note fails. Writes reviews/research_audit.md.

Each note must contain:
  ## Source coverage      table: | Source | Status | Evidence |   (status: used, not applicable, blocked)
                          one row for every required source of its unit (core_all + its material or sector list)
  ## Spotlight facts      at least min_spotlights bullet or numbered items, each with a year (20xx)
  ## Triangulation        at least min_triangulated key numbers confirmed by two independent sources
plus enough distinct sources overall (URLs or data_ids), primary sources and company reports.
"""
import json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
M = json.load(open(os.path.join(ROOT, "data", "source_matrix.json")))
T = M["thresholds"]
PRIMARY = re.compile(r"comtrade|usgs|eurostat|prodcom|worldbank|world bank|oecd|unido|iea\.org|international energy agency|irena|"
                     r"oica|acea|icao|iata|airbus|boeing|cefic|semi\.org|wsts|who\.int|ghoapi|sec\.gov|annual report|10-k|20-f|"
                     r"investor|data/clean/|sipri|energy institute|insg|icsg|cobalt institute|nickel institute|worldstainless|imoa|"
                     r"world nuclear|iaea|medtech europe|fda\.gov|un\.org|population", re.I)
COMPANY = re.compile(r"10-k|20-f|annual report|integrated report|investor presentation|earnings release|8-k|half[- ]year report|quarterly report|sec\.gov/Archives", re.I)


def unit_of(path):
    name = os.path.splitext(os.path.basename(path))[0].lower()
    for k in M["materials"]:
        if name.startswith(k.split("_")[0]) or k.startswith(name):
            return "material", k
    for k in M["sectors"]:
        if name.startswith(k.split("_")[0]) or k.startswith(name.split("_")[0]):
            return "sector", k
    return None, None


def section(text, title):
    m = re.search(rf"^##\s+{title}.*?$(.*?)(?=^##\s|\Z)", text, re.M | re.S | re.I)
    return m.group(1) if m else ""


def audit(path):
    text = open(path, encoding="utf-8").read()
    kind, key = unit_of(path)
    problems = []
    required = list(M["core_all"]) + (M["materials" if kind == "material" else "sectors"].get(key, []) if kind else [])
    cov = section(text, "Source coverage")
    rows = [r for r in cov.splitlines() if r.strip().startswith("|") and not re.match(r"^\|\s*:?-", r.strip())][1:]
    if not cov:
        problems.append("missing '## Source coverage' table")
    for req in required:
        words = [w.lower() for w in re.findall(r"[A-Za-z]{3,}", req)[:2]]
        hit = [r for r in rows if all(w in r.lower() for w in words)]
        if not hit:
            problems.append(f"required source not covered: {req}")
            continue
        cells = [c.strip().lower() for c in hit[0].strip("|").split("|")]
        status = cells[1] if len(cells) > 1 else ""
        evidence = cells[2] if len(cells) > 2 else ""
        if status.startswith("used") and not evidence:
            problems.append(f"'{req}' marked used without evidence")
        if status.startswith(("blocked", "not applicable", "n/a")) and len(evidence) < 15:
            problems.append(f"'{req}' marked {status} without a reason")
        if not status.startswith(("used", "blocked", "not applicable", "n/a")):
            problems.append(f"'{req}' has no valid status (used / blocked / not applicable)")
    urls = set(re.findall(r"https?://[^\s)|>\]]+", text)) | set(re.findall(r"\b[A-Z][A-Z0-9_]{5,}\b", text)) | set(re.findall(r"data/clean/[\w.\-]+", text))
    primary = {u for u in urls if PRIMARY.search(u)} | set(re.findall(r"data/clean/[\w.\-]+", text))
    companies = set(m.group(0).lower() for m in re.finditer(r"[^\n|]{0,60}(?:" + COMPANY.pattern + r")[^\n|]{0,40}", text, re.I))
    spot = [l for l in section(text, "Spotlight facts").splitlines() if re.match(r"^\s*(\*|\d+\.)\s", l)]
    spot_ok = [l for l in spot if re.search(r"20\d\d", l)]
    tri = [l for l in section(text, "Triangulation").splitlines() if re.match(r"^\s*(\*|\d+\.|\|)\s", l) and not re.match(r"^\|\s*:?-", l)]
    gaps = len(re.findall(r"TODO\(data\)", text))
    if len(urls) < T["min_sources"]:
        problems.append(f"only {len(urls)} distinct sources (minimum {T['min_sources']})")
    if len(primary) < T["min_primary"]:
        problems.append(f"only {len(primary)} primary or structured sources (minimum {T['min_primary']})")
    if len(companies) < T["min_company_reports"]:
        problems.append(f"only {len(companies)} company report references (minimum {T['min_company_reports']})")
    if len(spot_ok) < T["min_spotlights"]:
        problems.append(f"only {len(spot_ok)} dated spotlight facts (minimum {T['min_spotlights']})")
    if len(tri) < T["min_triangulated"] + 1:  # header row
        problems.append(f"fewer than {T['min_triangulated']} triangulated key numbers")
    return {"file": os.path.relpath(path, ROOT), "unit": f"{kind}:{key}", "sources": len(urls), "primary": len(primary),
            "company_reports": len(companies), "spotlights": len(spot_ok), "gaps": gaps, "problems": problems}


def main():
    files = sys.argv[1:] or sorted(
        os.path.join(d, f) for d in (os.path.join(ROOT, "research", "materials"), os.path.join(ROOT, "research", "sectors"))
        if os.path.isdir(d) for f in os.listdir(d) if f.endswith(".md") and not f.endswith("_trade.md"))
    if not files:
        sys.exit("No research notes found in research/materials or research/sectors")
    res = [audit(f) for f in files]
    lines = ["# Research audit", "", "| Note | Unit | Sources | Primary | Company reports | Spotlights | Open gaps | Result |", "|---|---|---|---|---|---|---|---|"]
    for r in res:
        lines.append(f"| {r['file']} | {r['unit']} | {r['sources']} | {r['primary']} | {r['company_reports']} | {r['spotlights']} | {r['gaps']} | {'PASS' if not r['problems'] else 'FAIL'} |")
    for r in res:
        if r["problems"]:
            lines += ["", f"## {r['file']}"] + [f"* {p}" for p in r["problems"]]
    os.makedirs(os.path.join(ROOT, "reviews"), exist_ok=True)
    open(os.path.join(ROOT, "reviews", "research_audit.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("\n".join(lines))
    sys.exit(1 if any(r["problems"] for r in res) else 0)


if __name__ == "__main__":
    main()

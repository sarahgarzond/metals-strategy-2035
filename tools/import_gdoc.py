#!/usr/bin/env python3
"""Import the team's Google Doc (JSON from the Google Docs connector, documents.get) into sections/*.md
and its reference list into data/sources.csv.

Usage: python3 tools/import_gdoc.py data/raw/gdoc_export.json [--force]

The Google Doc stays the team's master text. Run this after the team edits the doc. Existing section
files are only overwritten with --force (otherwise new files are written to sections/_import/ for comparison).
"""
import csv, json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC_CSV = os.path.join(ROOT, "data", "sources.csv")

# file name for every H1/H2 heading number; content until the next mapped heading goes into that file
FILES = {
    "1": "01_introduction.md", "2": "02_objective_and_scope.md", "3": "03_framework_and_methodology.md",
    "4": "04_0_metal_markets.md", "4.1": "04_1_nickel.md", "4.2": "04_2_cobalt.md", "4.3": "04_3_chromium.md",
    "4.4": "04_4_molybdenum.md", "4.5": "04_5_titanium.md", "4.6": "04_6_tungsten.md", "4.7": "04_7_other_metals.md",
    "5": "05_0_industry_needs.md", "5.1": "05_1_automotive.md", "5.2": "05_2_oil_and_gas.md",
    "5.3": "05_3_energy_environment.md", "5.4": "05_4_aerospace.md", "5.5": "05_5_chemical_processing.md",
    "5.6": "05_6_electronics_electrical.md", "5.7": "05_7_medical_technology.md",
    "6": "06_trade.md", "7": "07_scenarios.md", "8": "08_recommendations.md", "9": "09_conclusion.md",
    "Appendices": "11_appendices.md",
}


def runs_md(elements, italic_ok=True):
    out = ""
    for e in elements:
        tr = e.get("textRun")
        if not tr:
            continue
        t, st = tr.get("content", ""), tr.get("textStyle", {})
        core = t.rstrip("\n")
        if core.strip() and italic_ok and st.get("italic") and not st.get("bold"):
            lead, trail = re.match(r"^(\s*)", core).group(1), re.search(r"(\s*)$", core).group(1)
            core = f"{lead}*{core.strip()}*{trail}"
        out += core
    return out.replace("\u000b", " ").strip()


def runs_html(elements):
    out = ""
    for e in elements:
        tr = e.get("textRun")
        if not tr:
            continue
        t = tr.get("content", "").rstrip("\n").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        out += f"<i>{t}</i>" if tr.get("textStyle", {}).get("italic") and t.strip() else t
    return out.strip()


def table_md(t):
    rows = []
    for r in t["tableRows"]:
        cells = []
        for c in r["tableCells"]:
            parts = [runs_md(x["paragraph"]["elements"]) for x in c["content"] if "paragraph" in x]
            cells.append("<br>".join(p for p in parts if p).replace("|", "\\|"))
        rows.append("| " + " | ".join(cells) + " |")
    rows.insert(1, "|" + "---|" * len(t["tableRows"][0]["tableCells"]))
    return "\n".join(rows)


def parse_reference(html_text, plain):
    m = re.match(r"^(.*?)\.\s\((.+?)\)\.\s(.*)$", plain)
    author, date, rest = (m.group(1), m.group(2), m.group(3)) if m else (plain[:40], "n.d.", "")
    url = re.findall(r"https?://\S+", plain)
    label = date.split(",")[0].strip()
    return author.strip(), date, label, (url[-1] if url else ""), rest


def main():
    path = sys.argv[1]
    force = "--force" in sys.argv
    d = json.load(open(path, encoding="utf-8"))
    tab = d.get("content", d)["tabs"][0]["documentTab"]
    body = tab["body"]["content"]

    files, current, in_refs, refs = {}, None, False, []
    for el in body:
        if "tableOfContents" in el:
            continue
        if "table" in el:
            if current:
                files[current].append(table_md(el["table"]))
            continue
        p = el.get("paragraph")
        if not p:
            continue
        style = p.get("paragraphStyle", {}).get("namedStyleType", "")
        plain = "".join(e.get("textRun", {}).get("content", "") for e in p["elements"]).strip()
        if style.startswith("HEADING"):
            level = int(style[-1])
            num = plain.split("\t")[0].strip().rstrip(".") if "\t" in plain else plain.split()[0].rstrip(".")
            title = plain.split("\t", 1)[1].strip() if "\t" in plain else plain
            if plain == "References":
                in_refs, current = True, None
                continue
            if plain.startswith("Appendices"):
                in_refs, num = False, "Appendices"
            if num in FILES:
                current = FILES[num]
                files.setdefault(current, [])
            if current is None:
                continue
            hashes = "#" * level
            if num == "Appendices":
                files[current].append(f"# {plain}")
            elif re.match(r"^A\d", plain):
                files[current].append(f"## {plain.replace('  ', ' ')}")
            else:
                files[current].append(f"{hashes} {num}{'.' if level == 1 else ''} {title}")
            continue
        if in_refs:
            if plain:
                refs.append((runs_html(p["elements"]), plain))
            continue
        if current is None or not plain:
            continue
        text = runs_md(p["elements"])
        files[current].append(("* " + text) if "bullet" in p else text)

    out_dir = os.path.join(ROOT, "sections")
    target = out_dir
    if not force and any(os.path.exists(os.path.join(out_dir, f)) for f in files):
        target = os.path.join(out_dir, "_import")
        os.makedirs(target, exist_ok=True)
    for f, blocks in files.items():
        txt = ""
        for b in blocks:
            sep = "\n" if (b.startswith("* ") and txt.rstrip().split("\n")[-1].startswith("* ")) else "\n\n"
            txt += (sep if txt else "") + b
        open(os.path.join(target, f), "w", encoding="utf-8").write(txt.strip() + "\n")
    print(f"Wrote {len(files)} section files to {os.path.relpath(target, ROOT)}")

    # references: add or update rows of type 'team_reference'
    rows = list(csv.DictReader(open(SRC_CSV, encoding="utf-8")))
    fields = list(rows[0].keys())
    for extra in ("apa_reference_html", "always_include"):
        if extra not in fields:
            fields.append(extra)
    by_id = {r["data_id"]: r for r in rows}
    added = 0
    for html_text, plain in refs:
        author, date, label, url, rest = parse_reference(html_text, plain)
        did = "REF_" + re.sub(r"[^A-Z0-9]+", "_", (author[:28] + "_" + label).upper()).strip("_")
        r = by_id.get(did) or {k: "" for k in fields}
        if did not in by_id:
            added += 1
            rows.append(r)
            by_id[did] = r
        r.update(data_id=did, author=author, intext_author=author, pub_date=date, ref_type="team",
                 title=rest.split(". http")[0][:200], url=url, type="team_reference", confidence="",
                 apa_reference_html=html_text, always_include="yes", retrieved=r.get("retrieved") or "",
                 notes="Imported from the team's Google Doc reference list. In-text label: " + f"({author}, {label})")
    w = csv.DictWriter(open(SRC_CSV, "w", newline="", encoding="utf-8"), fieldnames=fields)
    w.writeheader()
    for r in rows:
        w.writerow({k: r.get(k, "") for k in fields})
    print(f"References: {len(refs)} in doc, {added} new rows in data/sources.csv")


if __name__ == "__main__":
    main()

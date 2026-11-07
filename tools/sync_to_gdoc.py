#!/usr/bin/env python3
"""Turn the improved sections/*.md into Google Docs batchUpdate requests for the team's master doc.

Usage:
  python3 tools/sync_to_gdoc.py data/raw/gdoc_export.json [--sections 05_1,05_4] [--out report/gdoc_sync]

Input is a FRESH export of the doc (documents.get JSON, saved right before the push). The script aligns every
section of the doc with the matching markdown file paragraph by paragraph and only touches what changed:
changed paragraphs and table cells are replaced, removed paragraphs are deleted, new paragraphs, bullets,
headings and tables are inserted with the team's styles. Requests are ordered from the end of the document to
the start, so every chunk can be applied in sequence without shifting the indices of the next chunk.

Output (in --out):
  plan.md            human readable list of every change, per section
  chunk_001.json ... request lists to send with the Google Docs update_doc tool, in order
  meta.json          document id, revision id of the export, chunk count

Citations: [DATA_ID] markers are converted to APA text with the same code as the PDF build, so the doc and the
PDF read the same. The References section of the doc is rebuilt from data/sources.csv the same way.
"""
import argparse, csv, difflib, json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(ROOT, "tools"))
sys.path.insert(0, os.path.join(ROOT, ".claude", "skills", "build-report"))
from import_gdoc import FILES, runs_md  # noqa: E402
import build  # noqa: E402

BODY_STYLE = {"namedStyleType": "NORMAL_TEXT", "alignment": "JUSTIFIED", "lineSpacing": 150,
              "spaceAbove": {"magnitude": 0, "unit": "PT"}, "spaceBelow": {"magnitude": 6, "unit": "PT"},
              "indentStart": {"magnitude": 0, "unit": "PT"}, "indentFirstLine": {"magnitude": 0, "unit": "PT"}}
CAPTION_STYLE = dict(BODY_STYLE, spaceBelow={"magnitude": 4, "unit": "PT"}, keepWithNext=True)
SOURCE_STYLE = dict(BODY_STYLE, spaceAbove={"magnitude": 4, "unit": "PT"}, spaceBelow={"magnitude": 12, "unit": "PT"})
BULLET_STYLE = dict(BODY_STYLE, spaceBelow={"magnitude": 4, "unit": "PT"})
REF_STYLE = {"namedStyleType": "NORMAL_TEXT", "alignment": "JUSTIFIED", "lineSpacing": 115,
             "spaceAbove": {"magnitude": 18, "unit": "PT"}, "spaceBelow": {"magnitude": 6, "unit": "PT"},
             "indentStart": {"magnitude": 36, "unit": "PT"}, "indentFirstLine": {"magnitude": 0, "unit": "PT"}}
HEAD_STYLE = {"alignment": "JUSTIFIED", "lineSpacing": 150, "spaceAbove": {"magnitude": 18, "unit": "PT"},
              "spaceBelow": {"magnitude": 6, "unit": "PT"}}
CELL_STYLE = {"alignment": "JUSTIFIED", "lineSpacing": 115, "spaceAbove": {"magnitude": 2, "unit": "PT"},
              "spaceBelow": {"magnitude": 2, "unit": "PT"}}
STYLE_FIELDS = "namedStyleType,alignment,lineSpacing,spaceAbove,spaceBelow,indentStart,indentFirstLine"


def u16(s):
    return len(s.encode("utf-16-le")) // 2


def norm(s):
    s = re.sub(r"\*([^*]+)\*", r"\1", s or "")
    s = s.replace("\\|", "|")
    return re.sub(r"\s+", " ", s).strip()


def strip_inline(text):
    """Markdown inline text -> (plain text, italic spans in utf16 offsets, link spans)."""
    text = text.replace("\\|", "|")
    plain, italics, pos = "", [], 0
    for part in re.split(r"(\*[^*]+\*)", text):
        if part.startswith("*") and part.endswith("*") and len(part) > 2:
            inner = part[1:-1]
            italics.append((u16(plain), u16(plain) + u16(inner)))
            plain += inner
        else:
            plain += part
    links = [(u16(plain[:m.start()]), u16(plain[:m.end()]), m.group(0)) for m in re.finditer(r"https?://\S+", plain)]
    return plain, italics, links


# ------------------------------------------------------------------ document side
def doc_blocks(doc):
    tab = doc.get("content", doc)["tabs"][0]["documentTab"]
    body = tab["body"]["content"]
    sections, current, order = {}, None, []
    for el in body:
        if "tableOfContents" in el or "sectionBreak" in el:
            continue
        if "table" in el:
            t = el["table"]
            rows = []
            for r in t["tableRows"]:
                row = []
                for c in r["tableCells"]:
                    paras = [x["paragraph"] for x in c["content"] if "paragraph" in x]
                    p0 = [x for x in c["content"] if "paragraph" in x]
                    text = "<br>".join(runs_md(p["elements"]) for p in paras if runs_md(p["elements"]))
                    row.append({"text": text, "start": p0[0]["startIndex"], "end": p0[-1]["endIndex"]})
                rows.append(row)
            blk = {"type": "table", "rows": rows, "start": el["startIndex"], "end": el["endIndex"]}
            if current:
                sections[current].append(blk)
            continue
        p = el.get("paragraph")
        if not p:
            continue
        style = p.get("paragraphStyle", {}).get("namedStyleType", "")
        plain = "".join(e.get("textRun", {}).get("content", "") for e in p["elements"]).strip()
        if style.startswith("HEADING"):
            num = plain.split("\t")[0].strip().rstrip(".") if "\t" in plain else plain.split()[0].rstrip(".") if plain else ""
            key = "References" if plain == "References" else ("Appendices" if plain.startswith("Appendices") else num)
            if key == "References":
                current = "__references__"
                order.append(current)
                sections.setdefault(current, [])
            elif key in FILES and FILES[key] != current:
                current = FILES[key]
                order.append(current)
                sections.setdefault(current, [])
            if current:
                sections[current].append({"type": "h", "level": int(style[-1]), "text": plain.replace("\t", " "),
                                          "start": el["startIndex"], "end": el["endIndex"]})
            continue
        if current is None:
            continue
        if not plain:
            sections[current].append({"type": "empty", "start": el["startIndex"], "end": el["endIndex"], "text": ""})
            continue
        sections[current].append({"type": "li" if "bullet" in p else "p",
                                  "text": runs_md(p["elements"], italic_ok=(current != "__references__")) if current != "__references__" else plain,
                                  "start": el["startIndex"], "end": el["endIndex"]})
    return sections, order, tab["body"]["content"][-1]["endIndex"]


# ------------------------------------------------------------------ markdown side
def md_blocks(md):
    blocks, lines, i = [], md.split("\n"), 0
    while i < len(lines):
        s = lines[i].strip()
        if not s or s.startswith("<!--"):
            i += 1
            continue
        if s.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in re.split(r"(?<!\\)\|", lines[i].strip())[1:-1]]
                if not all(re.fullmatch(r":?-+:?", c) for c in cells):
                    rows.append([{"text": c} for c in cells])
                i += 1
            blocks.append({"type": "table", "rows": rows})
            continue
        m = re.match(r"^(#{1,3})\s+(.*)$", s)
        if m:
            blocks.append({"type": "h", "level": len(m.group(1)), "text": m.group(2)})
        elif re.match(r"^[*]\s+", s):
            blocks.append({"type": "li", "text": re.sub(r"^[*]\s+", "", s)})
        else:
            blocks.append({"type": "p", "text": s})
        i += 1
    return blocks


def key(b):
    if b["type"] == "table":
        return "T:" + norm(" ".join(c["text"] for r in b["rows"] for c in r))[:400]
    if b["type"] == "h":
        return "H:" + re.sub(r"[.\s]+", " ", norm(b["text"])).strip()
    return b["type"].upper() + ":" + norm(b["text"])


def kind(text):
    t = norm(text)
    if re.match(r"^(Table|Figure) \d+:", t):
        return CAPTION_STYLE
    if t.startswith(("Source:", "Sources:")):
        return SOURCE_STYLE
    return BODY_STYLE


# ------------------------------------------------------------------ request builders
def style_text_requests(start, plain, italics, links, base_italic=False):
    end = start + u16(plain)
    reqs = [{"updateTextStyle": {"range": {"startIndex": start, "endIndex": end},
                                 "textStyle": {"italic": base_italic, "bold": False,
                                               "weightedFontFamily": {"fontFamily": "Times New Roman", "weight": 400},
                                               "fontSize": {"magnitude": 12, "unit": "PT"}},
                                 "fields": "italic,bold,weightedFontFamily,fontSize"}}] if end > start else []
    for a, b in italics:
        reqs.append({"updateTextStyle": {"range": {"startIndex": start + a, "endIndex": start + b},
                                         "textStyle": {"italic": True}, "fields": "italic"}})
    for a, b, url in links:
        reqs.append({"updateTextStyle": {"range": {"startIndex": start + a, "endIndex": start + b},
                                         "textStyle": {"link": {"url": url}, "underline": True,
                                                       "foregroundColor": {"color": {"rgbColor": {"red": 0.067, "green": 0.333, "blue": 0.8}}}},
                                         "fields": "link,underline,foregroundColor"}})
    return reqs


TOC = [(lvl, t) for lvl, t in json.load(open(os.path.join(ROOT, "data", "toc.json")))["entries"]]
TOC_TEXTS = {re.sub(r"[.\s]+", " ", t).strip() for _, t in TOC}


def heading_plain(text):
    plain = strip_inline(text)[0]
    return re.sub(r"^(\d+(?:\.\d+)*\.?|A\d+)\s+", lambda m: m.group(1) + "\t", plain)


def toc_ok(level, text):
    """Chapter and section headings (levels 1 and 2) must be entries of the team's table of contents."""
    return level > 2 or re.sub(r"[.\s]+", " ", norm(text)).strip() in TOC_TEXTS


def replace_heading(d, m):
    plain = heading_plain(m["text"])
    s, e = d["start"], d["end"] - 1
    reqs = [{"deleteContentRange": {"range": {"startIndex": s, "endIndex": e}}}] if e > s else []
    reqs.append({"insertText": {"location": {"index": s}, "text": plain}})
    reqs += style_text_requests(s, plain, [], [])
    reqs.append({"updateTextStyle": {"range": {"startIndex": s, "endIndex": s + u16(plain)},
                                     "textStyle": {"bold": m["level"] == 1}, "fields": "bold"}})
    if d["level"] != m["level"]:
        reqs.append({"updateParagraphStyle": {"range": {"startIndex": s, "endIndex": s + u16(plain) + 1},
                                              "paragraphStyle": dict(HEAD_STYLE, namedStyleType=f"HEADING_{m['level']}"),
                                              "fields": "namedStyleType,alignment,lineSpacing,spaceAbove,spaceBelow"}})
    return reqs


def replace_paragraph(d, new_text):
    plain, it, ln = strip_inline(new_text)
    s, e = d["start"], d["end"] - 1
    reqs = []
    if e > s:
        reqs.append({"deleteContentRange": {"range": {"startIndex": s, "endIndex": e}}})
    if plain:
        reqs.append({"insertText": {"location": {"index": s}, "text": plain}})
        italic_base = norm(new_text).startswith(("Source:", "Sources:")) and new_text.strip().startswith("*")
        reqs += style_text_requests(s, plain, [] if italic_base else it, ln, base_italic=italic_base)
    return reqs


def insert_block(at, b, refs=False, caption=None):
    """Insert block b as new paragraph(s) at index `at` (the start of the following block)."""
    if b["type"] == "table":
        return insert_table(at, b, caption)
    plain, it, ln = strip_inline(b["text"])
    if b["type"] == "h":
        plain = heading_plain(b["text"])
    reqs = [{"insertText": {"location": {"index": at}, "text": plain + "\n"}}]
    rng = {"startIndex": at, "endIndex": at + u16(plain) + 1}
    if b["type"] == "h":
        style = dict(HEAD_STYLE, namedStyleType=f"HEADING_{b['level']}")
        fields = "namedStyleType,alignment,lineSpacing,spaceAbove,spaceBelow"
    elif refs:
        style, fields = REF_STYLE, STYLE_FIELDS
    elif b["type"] == "li":
        style, fields = BULLET_STYLE, STYLE_FIELDS
    else:
        style, fields = kind(b["text"]), STYLE_FIELDS + (",keepWithNext" if kind(b["text"]) is CAPTION_STYLE else "")
    reqs.append({"updateParagraphStyle": {"range": rng, "paragraphStyle": style, "fields": fields}})
    italic_base = b["type"] == "p" and norm(b["text"]).startswith(("Source:", "Sources:")) and b["text"].strip().startswith("*")
    reqs += style_text_requests(at, plain, [] if italic_base else it, ln, base_italic=italic_base)
    if b["type"] == "h":
        reqs.append({"updateTextStyle": {"range": {"startIndex": at, "endIndex": at + u16(plain)},
                                         "textStyle": {"bold": b["level"] == 1}, "fields": "bold"}})
    if b["type"] == "li":
        reqs.append({"createParagraphBullets": {"range": rng, "bulletPreset": "BULLET_DISC_CIRCLE_SQUARE"}})
    else:
        reqs.append({"deleteParagraphBullets": {"range": rng}})
    return reqs


def insert_table(at, b, caption=None):
    rows, cols = len(b["rows"]), max(len(r) for r in b["rows"])
    reqs = [{"insertTable": {"rows": rows, "columns": cols, "location": {"index": at}}}]
    t = at + 1  # a newline is inserted before the table
    fill = []
    for r in range(rows):
        for c in range(cols):
            text = b["rows"][r][c]["text"] if c < len(b["rows"][r]) else ""
            plain, it, ln = strip_inline(text.replace("<br>", "\n"))
            idx = t + 3 + r * (1 + 2 * cols) + 2 * c
            if plain:
                fill.append((idx, plain, it, ln))
    for idx, plain, it, ln in reversed(fill):
        reqs.append({"insertText": {"location": {"index": idx}, "text": plain}})
        reqs += style_text_requests(idx, plain, it, ln)
        reqs.append({"updateParagraphStyle": {"range": {"startIndex": idx, "endIndex": idx + u16(plain)},
                                              "paragraphStyle": CELL_STYLE,
                                              "fields": "alignment,lineSpacing,spaceAbove,spaceBelow"}})
    reqs.append({"updateTableCellStyle": {
        "tableRange": {"tableCellLocation": {"tableStartLocation": {"index": t}, "rowIndex": 0, "columnIndex": 0},
                       "rowSpan": 1, "columnSpan": cols},
        "tableCellStyle": {"backgroundColor": {"color": {"rgbColor": {"red": 0.929, "green": 0.929, "blue": 0.929}}}},
        "fields": "backgroundColor"}})
    # Google inserts an empty paragraph before the table, at index `at`: put the caption there
    cap = strip_inline(caption["text"])[0] if caption else ""
    if cap:
        reqs.append({"insertText": {"location": {"index": at}, "text": cap}})
        reqs += style_text_requests(at, cap, [], [])
    rng = {"startIndex": at, "endIndex": at + u16(cap) + 1}
    reqs.append({"updateParagraphStyle": {"range": rng, "paragraphStyle": CAPTION_STYLE if cap else BODY_STYLE,
                                          "fields": STYLE_FIELDS + ",keepWithNext"}})
    reqs.append({"deleteParagraphBullets": {"range": rng}})
    return reqs


# ------------------------------------------------------------------ planning
def plan_section(name, dblocks, mblocks, next_start, refs=False):
    ops, notes = [], []
    dk, mk = [key(b) for b in dblocks if b["type"] != "empty"], [key(b) for b in mblocks]
    dlist = [b for b in dblocks if b["type"] != "empty"]
    sm = difflib.SequenceMatcher(a=dk, b=mk, autojunk=False)

    def start_after(i):
        return dlist[i]["start"] if i < len(dlist) else next_start

    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        pairs = []
        if tag == "replace":
            n = min(i2 - i1, j2 - j1)
            pairs = [(i1 + k, j1 + k) for k in range(n)]
            dels, ins = list(range(i1 + n, i2)), list(range(j1 + n, j2))
        else:
            dels, ins = list(range(i1, i2)), list(range(j1, j2))
        for di, mj in pairs:
            d, m = dlist[di], mblocks[mj]
            if d["type"] == m["type"] == "table" and len(d["rows"]) == len(m["rows"]):
                for r, (drow, mrow) in enumerate(zip(d["rows"], m["rows"])):
                    for c, (dc, mc) in enumerate(zip(drow, mrow)):
                        if norm(dc["text"]) != norm(mc["text"]):
                            ops.append((dc["start"], 0, replace_paragraph({"start": dc["start"], "end": dc["end"]}, mc["text"].replace("<br>", " "))))
                            notes.append(f"table cell r{r + 1}c{c + 1}: '{norm(dc['text'])[:50]}' -> '{norm(mc['text'])[:50]}'")
            elif d["type"] == m["type"] and d["type"] in ("p", "li"):
                ops.append((d["start"], 0, replace_paragraph(d, m["text"])))
                notes.append(f"edit paragraph: '{norm(d['text'])[:60]}...'")
            elif d["type"] == "h" and m["type"] == "h":
                if not toc_ok(m["level"], m["text"]):
                    notes.append(f"BLOCKED: '{norm(m['text'])[:60]}' is not an entry of the table of contents (data/toc.json)")
                else:
                    ops.append((d["start"], 0, replace_heading(d, m)))
                    notes.append(f"heading: '{norm(d['text'])[:50]}' -> '{norm(m['text'])[:50]}'")
            else:
                dels.append(di)
                ins.append(mj)
        for di in sorted(set(dels)):
            d = dlist[di]
            if d["type"] == "h" and d["level"] <= 2:
                notes.append(f"BLOCKED: deleting the table of contents heading '{d['text'][:50]}'")
                continue
            ops.append((d["start"], 1, [{"deleteContentRange": {"range": {"startIndex": d["start"], "endIndex": d["end"]}}}]))
            notes.append(f"delete {d['type']}: '{norm(d.get('text', 'table'))[:60]}'")
        anchor = start_after(i2 if tag != "replace" else (i1 + len(pairs) + len([x for x in dels if x >= i1 + len(pairs)])))
        ins_set, merged = set(ins), set()
        for k, mj in enumerate(reversed(sorted(ins_set))):
            m = mblocks[mj]
            if mj in merged:
                continue
            if m["type"] == "h" and not toc_ok(m["level"], m["text"]):
                notes.append(f"BLOCKED: '{norm(m['text'])[:60]}' is not an entry of the table of contents (data/toc.json)")
                continue
            cap = None
            if m["type"] == "table" and (mj - 1) in ins_set and mblocks[mj - 1]["type"] == "p" \
                    and kind(mblocks[mj - 1]["text"]) is CAPTION_STYLE:
                cap = mblocks[mj - 1]
                merged.add(mj - 1)
            ops.append((anchor, 2 + k, insert_block(anchor, m, refs=refs, caption=cap)))
            notes.append(f"insert {m['type']}" + (f" with caption '{norm(cap['text'])[:50]}'" if cap else f": '{norm(m.get('text', 'table'))[:60]}'"))
    return ops, notes


def references_md():
    sources = build.load_sources()
    files = sorted(f for f in os.listdir(os.path.join(ROOT, "sections")) if f.endswith(".md"))
    md = "\n\n".join(open(os.path.join(ROOT, "sections", f), encoding="utf-8").read() for f in files)
    _, refs, _ = build.cite(md, sources)
    out = ["# References"]
    for p in re.findall(r'<p class="ref">(.*?)</p>', refs, flags=re.S):
        p = re.sub(r"<a [^>]*>(.*?)</a>", r"\1", p)
        p = re.sub(r"</?i>", "*", p)
        p = p.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"').replace("&#x27;", "'")
        out.append(p)
    return "\n\n".join(out)


def section_md(fname):
    sources = build.load_sources()
    md = open(os.path.join(ROOT, "sections", fname), encoding="utf-8").read()
    md, _, warn = build.cite(md, sources)
    md = re.sub(r'<span class="cite bad">\[\?(\w+)\]</span>', r"[MISSING SOURCE \1]", md)
    return md, warn


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("export")
    ap.add_argument("--sections", default="", help="comma separated file prefixes, e.g. 05_1,05_4,references")
    ap.add_argument("--out", default=os.path.join(ROOT, "report", "gdoc_sync"))
    ap.add_argument("--chunk", type=int, default=120, help="max requests per chunk")
    a = ap.parse_args()
    doc = json.load(open(a.export, encoding="utf-8"))
    content = doc.get("content", doc)
    dsec, order, body_end = doc_blocks(doc)
    wanted = [s.strip() for s in a.sections.split(",") if s.strip()]

    all_ops, plan = [], ["# Google Doc sync plan", f"Document revision of the export: {content.get('revisionId')}", ""]
    for idx, name in enumerate(order):
        if wanted and not any(name.startswith(w) or (w == "references" and name == "__references__") for w in wanted):
            continue
        nxt = dsec[order[idx + 1]][0]["start"] if idx + 1 < len(order) else body_end - 1
        if name == "__references__":
            mblocks = md_blocks(references_md())
            warn = []
        else:
            path = os.path.join(ROOT, "sections", name)
            if not os.path.exists(path):
                plan.append(f"## {name}\nNo markdown file, skipped.\n")
                continue
            md, warn = section_md(name)
            mblocks = md_blocks(md)
        ops, notes = plan_section(name, dsec[name], mblocks, nxt, refs=(name == "__references__"))
        all_ops += ops
        plan.append(f"## {name.replace('__references__', 'References')}  ({len(notes)} changes)")
        plan += [f"* {n}" for n in notes] or ["* no changes"]
        plan += [f"* WARNING unknown citation id: {w}" for w in warn]
        plan.append("")

    all_ops.sort(key=lambda o: (-o[0], o[1]))
    reqs = [r for _, _, rs in all_ops for r in rs]
    os.makedirs(a.out, exist_ok=True)
    for f in os.listdir(a.out):
        if f.startswith("chunk_"):
            os.remove(os.path.join(a.out, f))
    chunks, cur = [], []
    for _, _, rs in all_ops:  # never split the requests of one operation across chunks
        if cur and len(cur) + len(rs) > a.chunk:
            chunks.append(cur)
            cur = []
        cur += rs
    if cur:
        chunks.append(cur)
    for i, c in enumerate(chunks, 1):
        json.dump(c, open(os.path.join(a.out, f"chunk_{i:03d}.json"), "w", encoding="utf-8"), ensure_ascii=False)
    json.dump({"documentId": content.get("documentId"), "revisionId": content.get("revisionId"),
               "chunks": len(chunks), "requests": len(reqs)}, open(os.path.join(a.out, "meta.json"), "w"), indent=1)
    open(os.path.join(a.out, "plan.md"), "w", encoding="utf-8").write("\n".join(plan))
    print(f"{len(all_ops)} operations, {len(reqs)} requests in {len(chunks)} chunk(s). Plan: {os.path.relpath(a.out, ROOT)}/plan.md")


if __name__ == "__main__":
    main()

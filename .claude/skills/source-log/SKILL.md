---
name: source-log
description: How to record every number used in the report in data/sources.csv so the market model is transparent and reproducible. Use whenever you find or use a figure.
---
# Source log

Each number gets one row in `data/sources.csv` before it is used in research notes, the model or the report.

Columns (comma separated, quote any field that contains commas):
`data_id,metric,value,unit,year,geography,material,industry,source,publisher,author,intext_author,pub_date,ref_type,title,container,apa_publisher,volume,issue,pages,doi,url,retrieved,type,confidence,notes`

Data fields:
- data_id: short stable key, for example `NI_MINE_2025_WORLD`, `SEMI_300MM_CAPEX_2026`.
- type: `primary` (statistical office, USGS, IEA, company filing), `secondary` (press, trade journals), `market_report`, or `team_estimate`.
- confidence: `high` (primary, latest edition), `medium` (secondary or older), `low` (single unverified source).
- retrieved: ISO date, for example 2026-11-07.
- For a team_estimate, the notes field holds the formula and the data_ids it is built from.

APA 7 fields (these drive the citations and the reference list, so fill them carefully):
- author: as it appears in the reference list. For people write `Ghemawat, P.` or `Smith, J., & Lee, K.`; for organisations write the full name, for example `U.S. Geological Survey` or `International Energy Agency`.
- intext_author: the in-text form, for example `Ghemawat`, `Smith & Lee`, `Smith et al.` or `International Energy Agency`.
- pub_date: `2026`, `2026, February` or `2025, October 8`, or `n.d.` if no date exists.
- ref_type: `journal`, `report`, `book`, `dataset` or `webpage`.
- title: in sentence case (capitalise the first word, the first word after a colon and proper nouns). Titles of reports, books, datasets and webpages are set in italics automatically.
- container: the journal name for articles, or the website name for webpages when it differs from the author (for example `NVIDIA Technical Blog`).
- apa_publisher: the publisher when it differs from the author (books and reports).
- volume, issue, pages: for journal articles. doi: without `https://doi.org/` (preferred over url when available).
- url: the full, direct link.

Examples of the output:
- Ghemawat, P. (2001). Distance still matters: The hard reality of global expansion. *Harvard Business Review, 79*(8), 137–147, 162. https://hbr.org/...
- U.S. Geological Survey. (2026a). *Mineral commodity summaries 2026: Cobalt.* https://pubs.usgs.gov/...
- Jefatura del Estado. (2020, February 4). *Real Decreto-ley 3/2020, de 4 de febrero*. Boletín Oficial del Estado. https://www.boe.es/...

Citation in text (APA 7): write `[data_id]` for (Author, Year), `[ID1, ID2]` for several sources and `[@data_id]` for a
narrative "Author (Year)". The build-report skill converts them, adds a, b, c suffixes for the same author and year, and
creates the alphabetical reference list automatically. Never type citations or references by hand.

Rules:
- Do not record the same metric twice. Update the row instead and keep the old value in notes.
- Market report figures need at least one primary or secondary cross check before they reach the executive summary.
- If two sources disagree, record both and state in notes which one is used and why.

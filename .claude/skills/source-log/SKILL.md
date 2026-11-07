---
name: source-log
description: How to record every number used in the report in data/sources.csv so the market model is transparent and reproducible. Use whenever you find or use a figure.
---
# Source log

Each number gets one row in `data/sources.csv` before it is used in research notes, the model or the report.

Columns (comma separated, quote any field that contains commas):
`data_id,metric,value,unit,year,geography,material,industry,source,publisher,url,retrieved,type,confidence,notes`

- data_id: short stable key, for example `NI_MINE_2025_WORLD`, `SEMI_300MM_CAPEX_2026`.
- type: `primary` (statistical office, USGS, IEA, company filing), `secondary` (press, trade journals), `market_report`, or `team_estimate`.
- confidence: `high` (primary, latest edition), `medium` (secondary or older), `low` (single unverified source).
- retrieved: ISO date, for example 2026-11-07.
- For a team_estimate, the notes field holds the formula and the data_ids it is built from.

Citation in text: the report numbers its references by the order of first use. Write `[data_id]` in drafts and the
build-report skill converts these into [n] and creates the reference list automatically.

Rules:
- Do not record the same metric twice. Update the row instead and keep the old value in notes.
- Market report figures need at least one primary or secondary cross check before they reach the executive summary.
- If two sources disagree, record both and state in notes which one is used and why.

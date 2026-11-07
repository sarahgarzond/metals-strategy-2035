# Brief: research update of the team's Google Doc report

The team's live report is a Google Doc with 9 chapters. The user wants the agent pipeline to rewrite it with the
Stage 1 research, keeping the same chapters and headings. Agents edit the markdown copies in
`gdoc_report/chapters/`. The orchestrator writes the final text back into the Google Doc. Agents never touch the doc.

## Files
- `gdoc_report/original/`: the doc as it was on 7 Nov 2026 (read only, for reference).
- `gdoc_report/chapters/NN_*.md`: working copies, one per chapter. Edit only the files assigned to you.
- Research to draw on: `sections/02_*.md` (materials), `sections/03_*.md` (sectors), `research/`, `data/sources.csv`,
  `data/raw/iea/` (IEA Critical Minerals 2026 dataset, Global EV Outlook 2026 data, see its README).

## Structure (fixed)
Keep every chapter and every existing heading (H1, H2, H3) with the same number and name, in the same order.
Do not add new H1 or H2 headings. New H3 headings are allowed only where stated in your task.
Do not touch `00_front_matter.md` (title page) or `10_references.md` (the orchestrator rebuilds the list).

## Citations
- Keep every existing in-text citation exactly as written, for example (OICA, 2026) or Airbus (2026b).
  Keep the facts behind them unless research shows they are wrong, in which case flag it in your report.
- Every NEW number must come from `data/sources.csv` and is cited as `[DATA_ID]` (several: `[ID1, ID2]`,
  narrative: `[@DATA_ID]`). The orchestrator converts these into APA (Author, Year) and adds the references.
- Do not add rows to `data/sources.csv`. If you need a new row (for example a figure from `data/raw/iea/`), append it to
  `gdoc_report/new_sources/<your_chapter>.csv` with the same header as data/sources.csv and a unique data_id.
- Never invent a number. Estimates are labelled "team estimate". Drop a point rather than leave a TODO in the prose.
- Prefer primary sources (USGS, UN Comtrade, World Bank, IEA, company filings) over market reports.
  Low-confidence rows (see the confidence column) need a hedge word or should be left out.

## Client
Write "the Client" or "the company" in body text, never the client's name (CLAUDE.md anonymity rule).
The analysis is market research on the overall market, not on the Client's internal data.

## House style (hard rules, CLAUDE.md and .claude/skills/house-style)
No dashes of any kind as punctuation (write ranges as "2025 to 2035"), no semicolons, no banned words,
every sentence at least 12 words, paragraphs linked to the previous and the next one. Alloy names without hyphens
where possible (FeNi36, CuNiSi, CoCr). Check with `python3 .claude/skills/house-style/lint.py gdoc_report/chapters/<file>`.

## Tables
Keep the existing tables (same count and position). You may change cells and add rows.
New tables only where your task allows it. Use markdown tables with a "Table N: title" line above and a "Sources:" line below.
Table numbering will be renumbered by the orchestrator.

## Length budget (the report must stay at 30 pages or fewer)
Words of body text including tables, excluding references:
01 350, 02 250, 03 400, 04 1,900, 05 4,000 (about 570 per sector), 06 600, 07 700, 08 650, 09 220, 11 appendices 500.

## Do not commit. The orchestrator commits. Report back: what changed, new data_ids used, open issues.

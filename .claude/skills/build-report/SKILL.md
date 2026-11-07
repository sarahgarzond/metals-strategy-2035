---
name: build-report
description: Builds report/report.pdf from sections/*.md with the project design (brief's teal, green, yellow gradient, navy text, Inter), auto numbered citations from data/sources.csv, table of contents with page numbers and a 30 page check. Also holds chart conventions.
---
# Build the report

    python3 .claude/skills/build-report/build.py            # writes report/report.html and report/report.pdf

What it does:
1. Concatenates sections/*.md in file name order (00_, 01_, 02_..., 06_).
2. Converts citations into APA 7th edition: `[data_id]` becomes (Author, Year), `[ID1, ID2]` becomes (Author, Year; Author, Year)
   and `[@data_id]` becomes Author (Year). It adds 2026a and 2026b suffixes where needed and builds the References list
   (alphabetical, Times New Roman 12 pt, double spaced, italic titles, full blue links) from the APA fields in data/sources.csv.
   Unknown ids are printed as warnings and shown as [?id] in red.
3. Wraps the content in template.html (cover, table of contents, running footer with page numbers).
4. Renders the PDF with the preinstalled Playwright Chromium (render.js), fills the table of contents page numbers in a second pass,
   and fails (exit 1) if the PDF exceeds 30 pages.

## Section file conventions
- Start each file with an H1 (chapter) or H2 (subchapter) using the fixed numbering in CLAUDE.md.
- Figures: `![Figure 3: Message title that states the insight](fig/f3_prices.svg)` followed by a line
  `Source: [USGS_NI_MINE_2025], team analysis`.
- Fact or spotlight boxes: wrap in `<div class="box" markdown="1"> ... </div>`.
- Force a page break: `<div class="pb"></div>`.

## Chart conventions (data-modeler)
- Palette: navy #26307A, teal #1590B8, cyan #33B6D6, green #6DBE45, lime #BFD630, yellow #F2E21C, grey #6B7385.
- Font Inter, 8 to 10 pt, SVG output to report/fig/, width 6.8 inches.
- The title is a message ("Aerospace and electronics deliver half of all market growth"), not a label.
- Always show units, the base year and the source. Never use 3D, pie charts with more than five slices, or dual axes without labels.

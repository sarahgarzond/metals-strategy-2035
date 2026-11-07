---
name: build-report
description: Builds report/report.pdf from sections/*.md in the exact design of the team's Google Doc (Times New Roman 12, justified, 1.5 spacing, title page without page number), APA 7 citations from data/sources.csv, table of contents with page numbers and a 30 page check on the main text.
---
# Build the report

    python3 .claude/skills/build-report/build.py            # writes report/report.html and report/report.pdf

What it does:
1. Concatenates sections/*.md in file name order (01_ to 09_). Files whose name contains "append" go after the References.
2. Converts citations into APA 7th edition: `[data_id]` becomes (Author, Year), `[ID1, ID2]` becomes (Author, Year; Author, Year)
   and `[@data_id]` becomes Author (Year). It adds 2026a and 2026b suffixes where needed and builds the References list
   (alphabetical, Times New Roman 12 pt, double spaced, italic titles, full blue links) from the APA fields in data/sources.csv.
   Unknown ids are printed as warnings and shown as [?id] in red.
3. Wraps the content in template.html (the team's title page, Table of Contents with chapters and subsections, page numbers top right).
4. Renders the PDF with Playwright Chromium (render.js), removes the page number from the title page, fills the table of
   contents page numbers in a second pass, and fails (exit 1) if the main text (title page to Conclusion) exceeds 30 pages.

Authors and date on the title page: environment variables REPORT_AUTHORS and REPORT_DATE (defaults are in build.py).

## Section file conventions
- Headings: `# 5. Industry Needs`, `## 5.1 Automotive`, `### 5.1.1 Historical and Current Market Overview` (number, space, title).
- Tables: a caption paragraph `Table 3: Oil and gas market, today and in 2035` directly above a markdown table,
  then an italic line `*Sources: Energy Institute (2026), IEA (2025a).*` below it.
- Figures: caption paragraph `Figure 2: ...` above `![...](fig/f2_materials.svg)`, italic Sources line below.
- Bullets: `* text` (rendered as round dots). Force a page break: `<div class="pb"></div>`.

## Chart conventions (data-modeler)
- Charts must sit quietly in the team's academic design: Times New Roman (Liberation Serif) 10 pt, black text,
  greys plus one accent colour (#1F4E79), no gradients. SVG output to report/fig/, width 6.3 inches.
- The title is a message ("Aerospace and electronics deliver half of all market growth"), not a label.
- Always show units, the base year and the source. Never use 3D, pie charts with more than five slices, or dual axes without labels.

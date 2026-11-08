# Forging the Future: Market Intelligence and Growth Strategy for High-Performance Metals Through 2035
TUM project study. Four person consulting team. Target grade 1.0. Audience: TUM examiners and alloy industry experts.

## Master text
The team's Google Doc "my version munvest report" (id 1VUYfTdtTXdviMMfTqkBaUTKzgEWnJG8UhdZO_tIv9qE) is the master draft.
It was imported into sections/*.md with tools/import_gdoc.py. Agents improve the sections within the table of contents below.

## No client naming (user instruction, overrides the draft)
This is pure metal market research. Never mention the client company, VDM Metals, Acerinox, Münvest or "the company"
anywhere in the report body. Recommendations address "producers of high performance metals" in general.
Haynes may appear only as the source of a public alloy datasheet.
Exception (user instruction): the title page, cover page and table of contents stay exactly as they are, including
"Münvest Project Studies" and "Dr. Nicolas Seitz, Münvest". Graders must not flag the title page.

## Central question (from the draft, chapter 2)
How do the production, availability, trade and industrial uses of selected metals shape opportunities in high
performance materials through 2035?

## Deliverables
1. Written report (report/report.pdf), built from sections/*.md by the build-report skill. The main text, from the
   title page to the Conclusion, is at most 30 pages. References and appendices come after it and do not count.
2. Strategy deck: 22 to 27 main slides plus 5 to 10 backup slides (later phase).
3. Prototype: the Metals Atlas, an interactive explorer on the market data (later phase).

## Table of contents (the team's own, stored in data/toc.json)
The chapters, sections and appendix sections listed here are the fixed skeleton: body headings at these two levels
must match the table of contents exactly, in this order (the build and the sync check this). Everything below that
level may change throughout the document: subsection headings (for example 5.1.1 or 4.7.1) can be added, renamed,
merged, reordered or removed whenever that makes the report clearer, and paragraphs can move between subsections.
If the team changes the table of contents in the Google Doc, update data/toc.json first.
- 1. Introduction
- 2. Report Objective and Scope
- 3. Introduction to the Analytical Framework and Methodology
- 4. Metal Markets: Materials, Product Forms and Applications
  - 4.1 Nickel, 4.2 Cobalt, 4.3 Chromium, 4.4 Molybdenum, 4.5 Titanium, 4.6 Tungsten,
    4.7 Other Selected Metals (subsections 4.7.1 Zirconium, 4.7.2 Copper, 4.7.3 Aluminium, 4.7.4 Manganese, may change)
- 5. Industry Needs: Demand, Geography and Market Size
  - 5.1 Automotive, 5.2 Oil and Gas, 5.3 Energy and Environmental Technology, 5.4 Aerospace, 5.5 Chemical Processing,
    5.6 Electronics and Electrical Engineering, 5.7 Medical Technology
  - Subsections x.1 Demand, Geography and Market Size and x.2 Applications and Opportunities. Keep the sectors
    comparable: each has a numbered table with an italic Sources line and closes with "Implications for suppliers:"
- 6. Global Market Size and Trade
- 7. Growth Scenarios to 2035 (7.1 Growth Model and Scenario Assumptions, 7.2 Results by Industry, Product, and Region)
- 8. Strategic Recommendations (8.1 Priority Products, Industries, Regions, and Customers,
  8.2 Recommended Actions and Implementation Roadmap)
- 9. Conclusion
- References (generated automatically)
- Appendices: Data, Sources, Calculations, and Assumptions (A1 to A8, see data/toc.json).
  The appendix sections may be added, merged or renamed when the content requires it (update data/toc.json).

## The team's analytical framework (chapter 3, user instruction)
The framework is the seven-link metal value chain, metal first and industry second:
Material (ch 4) > Product form (ch 4) > Application (ch 4) > Industry (ch 5) > Geography (ch 5) > Market size (ch 5 and 6)
> Growth (ch 7). Chapter 8 assesses the opportunities on eight criteria (market attractiveness, growth to 2035, supply
security, competitive intensity, technology attractiveness, customer attractiveness, entry barriers, differentiation).
Chapter titles follow the chain. Do not add links or rename them. Changes are logged in reviews/framework_changes.md.

## Data chain (every figure in the report must map onto it)
Material > Product form > Application > Industry > Geography > Market size > Growth
model/model.py and the Excel file hold earlier team estimates (for example an addressable market of EUR 50.6bn).
The team's methodology says no aggregate addressable market value is asserted where comparable data are unavailable,
so model figures enter the report only if they meet that standard and are labelled as team estimates.
Scoring criteria for Phase III: market attractiveness, growth to 2035, supply security, competitive intensity,
technology attractiveness, customer attractiveness, entry barriers, differentiation potential (weights in model.py).

## Source rules
- Follow the research-protocol skill: structured databases first (tools/data/fetch.py), then industry associations and
  official outlooks, then company filings (data/companies.csv, research/companies/). The research audit
  (tools/research_audit.py, thresholds in data/source_matrix.json) must pass before any section is written.
- Prefer primary and structured sources: UN Comtrade, Eurostat PRODCOM, World Bank Pink Sheet, USGS MCS, OECD STAN/ICIO,
  UNIDO INDSTAT, IEA (Critical Minerals Data Explorer, LNG tracker, Hydrogen Review), IRENA, OICA/ACEA, ICAO/IATA,
  Airbus GMF, Boeing CMO, Cefic, SEMI, WHO, company annual reports, scientific papers.
- Paid market reports only to triangulate. Never the only source for a number.
- Every number gets a row in data/sources.csv (use the source-log skill) and an APA 7 citation in the text.
- Citation style is APA 7th edition, exactly as in the team's reference document: in text (Author, Year) or Author (Year),
  reference list titled References, alphabetical, laid out as in the team's Google Doc (Times New Roman 12 pt, 1.15 spacing,
  indented 1.27 cm), titles in italics as APA 7 requires, full clickable URL. The in-text author must match the reference
  entry exactly (for example "U.S. Geological Survey, 2026a", not "USGS, 2026a").
  In drafts write [DATA_ID] for (Author, Year), [ID1, ID2] for several sources and [@DATA_ID] for a narrative Author (Year).
  The build converts these automatically. Citations already typed in the imported draft, such as (USGS, 2026a), stay as
  they are, and their references (REF_* rows in data/sources.csv) are always listed. New sources get a row and a marker.
- Estimates are labelled "team estimate" and the assumption is written in the appendix.
- Never invent a number. Missing data becomes `TODO(data): what was searched`.
- Data access in the cloud environment `metals-strategy-2035`: USGS, World Bank API, UN Comtrade (public preview endpoint
  https://comtradeapi.un.org/public/v1/preview/..., no key needed, max 500 rows), Eurostat, OECD SDMX and UNIDO work directly.
  www.iea.org blocks automated downloads with a bot check, so use WebSearch for IEA facts and ask the team to download IEA
  datasets (for example the Critical Minerals Data Explorer) into data/raw/ by hand. Raw downloads always go to data/raw/.

## Interesting facts standard
Each sector needs at least three "spotlight" facts naming who, what, where, when, which metal, which product form and
likely suppliers. Example: "NVIDIA's 800 VDC rack architecture (Kyber, 2027) cuts copper busbar mass, which today reaches
up to 200 kg per 1 MW rack at 54 VDC, partners Infineon, Navitas, ROHM, Eaton, Schneider, Vertiv."

## Writing rules (hard, enforced by the house-style lint hook)
- No dashes of any kind as punctuation (no em dash, no en dash, no " - " and no dash bullets). Write ranges as "2025 to 2035".
- No semicolons. No buzzwords or filler words (see .claude/skills/house-style/banned_words.txt).
- Plain, clear style as in the team's improved Google Doc (user instruction, 8 Nov 2026): short direct sentences,
  at least 6 words each, ideally 10 to 20. Keep the flow between paragraphs.
- Pragmatic, easy to follow, expert level. Each paragraph opens with a link to the previous one and ends by leading into the next.
- Alloy names written without hyphens where possible (FeNi36, CuNiSi, CoCr). Official names like Alloy C-276 stay.

## Design (copied from the team's Google Doc, keep exactly)
A4, 2.5 cm margins, Times New Roman 12 pt everywhere, justified text, line spacing 1.5, 6 pt after paragraphs.
Title page centred without page number. Page numbers top right from page 2. Table of Contents lists chapters (bold)
and subsections (indented), with dotted leaders. Chapter headings bold ("1.  Introduction"), subsections regular
("4.1  Nickel", "5.1.1  Historical and Current Market Overview"). Table caption above ("Table 1: ..."), tables with
thin black borders, grey header row and 1.15 line spacing, italic "Sources: ..." line below. Bullets are round dots.
References in APA 7, 1.15 line spacing, indented 1.27 cm. Template: .claude/skills/build-report/template.html.

## Team workflow
- One git branch and worktree per sector or material while researching (`sector/<name>`, `material/<name>`), merged into main.
- The Google Doc is where the report lives. Use the gdoc-sync skill: PULL at the start of every round, PUSH at the end.
  Pushes are always tracked suggestions (SUGGEST mode), never direct edits, so the team accepts or rejects each change.
  Only the main session can sync, because subagents have no Google Docs tools.
- Review rounds stored in reviews/round_N/. Run the pipeline with the run-pipeline skill (`/run-pipeline`).
- Agents write raw research notes to research/, final prose to sections/. Graders are read only.

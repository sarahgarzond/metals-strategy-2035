# Forging the Future: Market Intelligence and Growth Strategy for High-Performance Metals Through 2035
TUM project study. Four person consulting team. Target grade 1.0. Audience: client board and alloy industry experts.

## Master text
The team's Google Doc "my version munvest report" (id 1VUYfTdtTXdviMMfTqkBaUTKzgEWnJG8UhdZO_tIv9qE) is the master draft.
It was imported into sections/*.md with tools/import_gdoc.py. Agents improve the sections. They never restructure them.

## Client naming
Follow the team's draft: the industry chapters say "the company", other chapters use the names exactly as the draft does.
VDM Metals' portfolio is an application benchmark only, never proof of the company's own capabilities or customers.
VDM and Haynes both belong to Acerinox, so never count them as separate competitors.

## Central question (from the draft, chapter 2)
How do the production, availability, trade and industrial uses of selected metals shape opportunities in high
performance materials through 2035?

## Deliverables
1. Written report (report/report.pdf), built from sections/*.md by the build-report skill. The main text, from the
   title page to the Conclusion, is at most 30 pages. References and appendices come after it and do not count.
2. Strategy deck: 22 to 27 main slides plus 5 to 10 backup slides (later phase).
3. Prototype: the Metals Atlas, an interactive explorer on the market data (later phase).

## Fixed table of contents (the team's own, keep numbering, names and order exactly)
- 1. Introduction
- 2. Report Objective and Scope
- 3. Introduction to the Analytical Framework and Methodology
- 4. Metal Markets: Production & Form
  - 4.1 Nickel, 4.2 Cobalt, 4.3 Chromium, 4.4 Molybdenum, 4.5 Titanium, 4.6 Tungsten,
    4.7 Other Selected Metals (4.7.1 Zirconium, 4.7.2 Copper, 4.7.3 Aluminium, 4.7.4 Manganese, 4.7.5 Additional Metals)
- 5. Industry Needs
  - 5.1 Automotive, 5.2 Oil and Gas, 5.3 Energy and Environmental Technology, 5.4 Aerospace, 5.5 Chemical Processing,
    5.6 Electronics and Electrical Engineering, 5.7 Medical Technology
  - Each sector keeps the subsections x.1 Historical and Current Market Overview and
    x.2 Key Applications and Opportunities for the Company, a numbered table with an italic Sources line,
    and the closing list "What the company should do:"
- 6. Global Market Dynamics and Trade
- 7. Market Scenarios to 2035 (7.1 Market Model and Scenario Assumptions, 7.2 Results by Industry, Product, and Region)
- 8. Strategic Recommendations (8.1 Priority Products, Industries, Regions, and Customers,
  8.2 Recommended Actions and Implementation Roadmap)
- 9. Conclusion
- References (generated automatically)
- Appendices: Data, Sources, Calculations, and Assumptions (A1 Definitions and evidence, A2 Reproducible scenario
  calculations, A3 Interpretation of existing sector estimates, A4 Information needed before investment).
  The appendices are the only part that may change: add, merge or rename A sections only when the content requires it.

## The team's analytical framework (chapter 3)
The team built its own metal centred value chain framework with four dimensions:
Supply (chapter 4: commercial forms, production stages, producer structure, availability, prices),
Trade (chapter 6: product classifications, exporting and importing markets, sourcing dependence),
Demand (chapter 5: industry drivers linked to components, materials, delivery forms and buyers) and
Outlook (chapter 7: explicit scenarios to 2035). Chapter 8 integrates the four dimensions for the company.
The sequence is metal first, industry second.

Rules for chapter 3:
- Explain the framework clearly, as the team designed it. Keep its four dimensions, their names, the chapter mapping
  and the metal first sequence.
- Refine only where necessary and only a little. Allowed refinements:
  (1) one short paragraph or one simple table showing how the dimensions map onto the data chain below,
  (2) naming the assessment criteria that chapter 8 uses to integrate the dimensions.
  Nothing else: no new dimensions, no renaming, no new chapters.
- Every refinement is listed in reviews/framework_changes.md with the reason, so the team can accept or reject it.

## Data chain (every figure in the report must map onto it)
Material > Product form > Application > Industry > Geography > Market size > Growth
Framework mapping: Supply covers Material and Product form, Demand covers Application and Industry,
Trade covers Geography, Outlook covers Market size and Growth.
model/model.py and the Excel file hold earlier team estimates (for example an addressable market of EUR 50.6bn).
The team's methodology says no aggregate addressable market value is asserted where comparable data are unavailable,
so model figures enter the report only if they meet that standard and are labelled as team estimates.
Scoring criteria for Phase III: market attractiveness, growth to 2035, strategic fit, competitive intensity,
technology attractiveness, customer attractiveness, entry barriers, differentiation potential (weights in model.py).

## Source rules
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
- No short sentences: every sentence at least 12 words, ideally 18 to 30.
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

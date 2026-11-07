# Product Strategy 2035: Growth Strategy for High Performance Metals
TUM project study. Four person consulting team. Target grade 1.0. Audience: client board and alloy industry experts.

## Client (keep anonymous, call it "the Client", never mention Münvest)
German producer of high performance materials and semifinished products: nickel and nickel alloys, cobalt alloys,
zirconium, specialty stainless steels, aluminium and copper products, additive manufacturing (AM) powders and
welding consumables. Forms: strip, sheet/plate, bar, wire, other semifinished. Revenue about EUR 400m in a roughly
EUR 50bn global market. Portfolio taxonomy of applications: aerospace, automotive, oil and gas, chemical processing,
electronics, energy/environmental engineering, medical engineering.

## Central question
Where should the Client focus its portfolio and commercial resources to achieve sustainable growth through 2035?

## Deliverables
1. Written report, max 30 pages (report/report.pdf), built from sections/*.md by the build-report skill.
2. Strategy deck: 22 to 27 main slides plus 5 to 10 backup slides (later phase).
3. Prototype: interactive opportunity explorer on the market model (later phase).

## Fixed table of contents (do not change order or names)
- 00 Executive summary
- 01 Introduction, central question and approach
- 02 Phase I: Global metals data foundation
  - 2.1 Model architecture and sources
  - 2.2 Nickel and nickel alloys, 2.3 Cobalt alloys, 2.4 Zirconium, 2.5 Specialty stainless steels,
    2.6 Aluminium and copper products, 2.7 AM powders and welding consumables, 2.8 Prices and supply risk synthesis
  - Per material: production, trade, consumption, applications, market size, prices, capacity/supply, outlook 2035
- 03 Phase II: Sector analyses
  - 3.1 Automotive, 3.2 Oil and gas, 3.3 Environmental and energy technology, 3.4 Aerospace,
    3.5 Chemical process industry, 3.6 Electronics and electrical engineering, 3.7 Medical technology, 3.8 Cross sector competitor map
  - Per sector answer all nine: market size and growth to 2035, drivers and risks, emerging technologies and applications,
    materials required, geographic demand concentration, relevant customers and competitors, competitor map,
    where high performance metals gain or lose relevance, most attractive value chain steps
- 04 Phase III: From market analysis to strategy
  - 4.1 Opportunity matrix (Product/Material x Application x Industry x Region), 4.2 Priorities,
    4.3 Strategic initiatives, 4.4 Roadmap 2026 to 2035 and scenarios, 4.5 Risks
- 05 Conclusion
- 06 Appendix: sources, assumptions, model documentation

## Data chain (every figure in the report must map onto it)
Material > Product form > Application > Industry > Geography > Market size > Growth
The master model lives in model/model.py and model/Product_Strategy_2035_Market_Model.xlsx.
Scoring criteria for Phase III: market attractiveness, growth to 2035, strategic fit, competitive intensity,
technology attractiveness, customer attractiveness, entry barriers, differentiation potential (weights in model.py).

## Source rules
- Prefer primary and structured sources: UN Comtrade, Eurostat PRODCOM, World Bank Pink Sheet, USGS MCS, OECD STAN/ICIO,
  UNIDO INDSTAT, IEA (Critical Minerals Data Explorer, LNG tracker, Hydrogen Review), IRENA, OICA/ACEA, ICAO/IATA,
  Airbus GMF, Boeing CMO, Cefic, SEMI, WHO, company annual reports, scientific papers.
- Paid market reports only to triangulate. Never the only source for a number.
- Every number gets a row in data/sources.csv (use the source-log skill) and a [n] citation in the text.
- Estimates are labelled "team estimate" and the assumption is written in the appendix.
- Never invent a number. Missing data becomes `TODO(data): what was searched`.

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

## Design
Follow the project brief: teal (#1590B8) to green (#6DBE45) to yellow (#F2E21C) gradient bars, navy text (#26307A),
yellow title accent on the dark cover, Inter font, A4. Template: .claude/skills/build-report/template.html.

## Team workflow
- One git branch and worktree per sector or material while researching (`sector/<name>`, `material/<name>`), merged into main.
- Review rounds stored in reviews/round_N/. Run the pipeline with the run-pipeline skill (`/run-pipeline`).
- Agents write raw research notes to research/, final prose to sections/. Graders are read only.

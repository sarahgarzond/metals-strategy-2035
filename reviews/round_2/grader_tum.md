# Round 2 grading: TUM School of Management supervisor

Graded version: report/report.pdf as rebuilt on 8 November 2026 (38 pages). The main text runs from the title page to the Conclusion on page 26 and the References start on page 27, so the 30 page limit is met. The PDF was rebuilt several times while I was reading. Page numbers below refer to the 38 page build, in which the reference list was being deduplicated. Reference problems I saw in earlier builds are only listed if they are still present in this one.

Rubric: .claude/skills/grading-rubric/SKILL.md (German scale, 1.0 best). I judged the report against CLAUDE.md, data/toc.json and the team's own framework. The chapter and section headings match the table of contents, and chapter 3 keeps the four dimensions, their names and the metal first sequence. The two refinements logged in reviews/framework_changes.md are within the allowed scope.

## Grades per criterion

| Criterion | Weight | Grade | Weighted |
|---|---|---|---|
| Research depth and source quality | 25% | 1.7 | 0.425 |
| Model transparency and reproducibility | 20% | 2.7 | 0.540 |
| Storyline from data to strategy | 20% | 2.3 | 0.460 |
| Actionability and strategic insight | 15% | 2.3 | 0.345 |
| Writing and house style (incl. APA 7) | 10% | 2.7 | 0.270 |
| Visuals and design | 10% | 2.3 | 0.230 |
| **Overall** | 100% | **2.3** (2.27 computed) | |

The report is very good in parts and clearly better researched than most project studies I supervise. It is not yet usable by industry as it stands, for three reasons. First, the "company" the strategy is written for is never defined, and VDM's application portfolio is quietly treated as that company's own. Second, the Outlook dimension is a set of assumed growth rates compounded over ten years, with no quantity behind them. Third, the reference list still fails APA 7 in visible ways.

### 1. Research depth and source quality: 1.7
The report earns this grade with the following:
- The supply facts come from current primary and structured sources and keep the correct stage: USGS MCS 2026 at commodity chapter level, INSG, ICSG, the Cobalt Institute, IMOA, worldstainless and the World Bank Pink Sheet. Section 4.1 (p. 6) and section 4.3 (p. 7) are model examples of the stage ladder. Mine nickel, primary nickel and nickel pig iron are kept apart, and ore, ferrochrome and stainless melt are kept apart.
- The company evidence is filing based and dated: ATI and Garrett 10-K, Acerinox FY2025 results, Alleima Q3 2026, Safran's EUR 150m press at Gennevilliers starting in 2029, Siemens Energy sold out to FY2028, and CMOC's 31,200 t export entitlement.
- Trade data are pulled from UN Comtrade at HS4 level with net trade calculated (Table 17, p. 20).

These gaps keep it from 1.0:
- Eurostat PRODCOM, UNIDO INDSTAT and OECD STAN, which chapter 3 and A3 name as pillars, contribute almost nothing to the text. PRODCOM is cited once, as a 1.8 percent cross-check (p. 6), and UNIDO not at all. The reader is promised a hierarchy that the chapters do not use.
- Chapter 6 (pp. 19 to 21) covers nickel and cobalt only. It has no trade evidence for titanium, chromium, molybdenum or tungsten, which chapter 4 flags as the policy risks. It also has no trade policy at all: EU CRMA benchmarks, CBAM in its definitive phase from 2026, US Section 232 tariffs on steel and aluminium derivatives, and China's export licence regime as a trade fact rather than a supply fact. A chapter called "Global Market Dynamics and Trade" cannot omit tariffs in 2026.
- Citation accuracy slips:
  - On p. 8, ATI's "about 20 months" titanium lead time is cited only to OSAKA Titanium technologies (2025).
  - On p. 14, "Rolls-Royce still describes parts availability as constrained" is cited to Safran (2026a).
  - On p. 14, Table 9 gives "About 38,000" for the Boeing fleet in 2035 as Boeing CMO 2026. Boeing publishes only the 2045 horizon, and data/sources.csv holds no 2035 Boeing figure, so this is an unlabelled team interpolation.
- The competitive landscape is scattered across sections and has no Asian depth. Daido gets one sentence. Fushun Special Steel, Baowu, Nippon Yakin and Proterial are absent, although chapter 8 bets on "fast qualification before 2030" against Asian capacity.
- The spotlight standard (who, what, where, when, metal, product form, likely suppliers) is met in aerospace, energy and electronics. Automotive (p. 10) and oil and gas (p. 11) fall short: Garrett and BorgWarner are named without an alloy grade, a product form or a supplier.

### 2. Model transparency and reproducibility: 2.7
- On the positive side, the methodology sentence on p. 3 is honoured, and no aggregate addressable market is asserted. The formula in 7.1 and A2 is reproducible, and the A2 worked examples check out (1.045^10 = 1.553, 0.985^10 = 0.860).
- The model does not walk the data chain Material > Product form > Application > Industry > Geography > Market size > Growth. Each industry gets one assumed rate g, and the index is 100 × (1 + g)^10. The anchors in Table 18 (p. 21) are indicators, and no derivation leads from them to g. Examples:
  - Aerospace 4.5% against fleet growth of 3.4%: why 4.5 and not 5.5?
  - Automotive −1.5% "anchored" on the EV share rising from 25% to 50%: the implied ICE plus hybrid unit path and the FeNi offset are never computed.
- Section 7.2 is titled "Results by Industry, Product, and Region", but it reports industry only. Product and region results are one narrative sentence (p. 23). This is a gap between the section title and its content.
- There is no quantity anywhere in chapter 7, neither tonnes nor EUR, so the industries cannot be compared by size. A 155 index on a small base and a 110 index on the largest business (chemical, by the report's own words on p. 25) carry very different strategic weight, and the reader is never told which is larger.
- On p. 26, the governance rule asks that investments earn their hurdle rate "in the downside scenario of chapter 7". An index with no volume or value cannot test a hurdle rate. As written, the rule cannot be applied.
- On p. 22, the title of Figure 3, "Aerospace and energy technology lead demand growth to 2035 in every scenario", is false. In the downside case energy is at 105, below medical technology at 110 (Table 19).

### 3. Storyline from data to strategy: 2.3
- The report is strong on transitions. Almost every paragraph opens with a link and closes with a bridge, and each metal profile ends with an implication for the company. The sequence Supply, Demand, Trade, Outlook, integration is clear, and Table 1 (p. 4) makes the framework easy to follow.
- The answer does not come first. A board member reads 22 pages before seeing a priority, because chapter 2 ends with scope caveats rather than the answer.
- The company is undefined. Chapter 2 (p. 3) names Münvest as the client and states that VDM Metals' portfolio is only an application benchmark. From p. 6 onward the text asserts facts about the company that only VDM's data could support:
  - "Nickel is the base of the company's portfolio" (p. 6).
  - "The company's car alloys serve turbochargers ... eight of its eleven benchmark applications" (p. 10).
  - "many of its alloys are approved for sour gas service" (p. 11).
  - "The company's chemical portfolio covers Nickel 200, Alloy 59, C-276, 625, Alloy 31 and zirconium" (p. 16).
  - "the company's home base" in Germany (p. 19).
  - "the existing franchises where the company's approvals ... create value" (p. 25).

  This breaks the CLAUDE.md rule that VDM's portfolio is never proof of the company's capabilities. It also contradicts A4 (p. 38), which says these approvals are unknown. An expert reader will conclude that the strategy is VDM's.
- The "Fit" column of Table 20 is rated H for 8 of 11 opportunities. Those ratings rest on the same unproven portfolio assumption.
- Chapter 6 feeds chapter 8 only through three generic conclusions (p. 21). The trade evidence does not change any rating in Table 20.

### 4. Actionability and strategic insight: 2.3
- The priorities are specific in alloy, form, application and region: superalloy bar and billet for jet engines and gas turbines in Europe and the United States, FeNi36 foil through a mask maker, and CoCr powder under ISO 13485. Things to stop are named: diesel-only parts first, and no capacity ahead of signed electrolyser volumes. The insight that one superalloy bar and billet capacity decision serves two markets (p. 23) is a real strategic finding.
- Table 21 (p. 26) has no size, owner or target. It contains no capex, tonnage, revenue at stake or FTE, no accountable function, and no KPI target values: "Approved part numbers" gives no number, and "Order intake outside Europe" gives no threshold. "Become second European source for hot section bar" ignores that Acerinox (VDM plus Haynes), Aubert & Duval and Alleima already hold that position, and no entry route is stated.
- Some named customers appear in the actions without supporting evidence in the chapter. SLB on p. 12 and MTU on p. 15 are recommended targets, but the analysis never discusses them.
- Trade-offs between tiers are not quantified. The report says automotive "should finance the company's growth areas" (p. 10), but it never says how much cash automotive or chemical generate compared with what Tier 1 needs.

### 5. Writing and house style (including APA 7): 2.7
- The prose is clean and expert. The lint reports 0 violations, the sentences are long and linked, and the text has no filler.
- The reference list still deviates from APA 7 and from the team's reference document. Each deviation counts against this criterion under the rubric:
  - **Several entries for one document.**
    - Airbus 2026a, 2026b and 2026c are the same GMF page (p. 27).
    - Alleima AB 2026b and 2026c are the same Q3 PDF.
    - Alleima (2026) and Alleima AB (2026a) are the same annual report under two author names.
    - Acerinox (2026a) and Acerinox, S.A. (2026b) are the same FY2025 PDF under two author names.
    - Zimmer Biomet Holdings 2026a and 2026b are one 10-K.
    - WSTS 2026a and 2026b are one release.
    - worldstainless 2026a and 2026b are one release.
    - The USGS MCS 2026 chapters appear two to four times each (nickel, cobalt, chromium, molybdenum, titanium, zirconium). The Cobalt Institute report appears eight times, IEA Global EV Outlook 2026 six times and the INSG October release four times.

    APA 7 requires one entry per work, with page or table locators in the in-text citation.
  - **"https://doi.org/https://..."** appears in the IMOA, Johnson & Johnson, Outokumpu, Sandvik and World Bank entries. These are not DOIs.
  - **A truncated URL** in World Nuclear Association (2026a) ends in "requireme".
  - **"n.d.-b" with no "n.d.-a"** appears in Aperam and USGS Tungsten. APA 7 uses n.d.-a and n.d.-b.
  - **The in-text author does not match the reference entry.** Table 3 cites "OICA (2026), ACEA (2026)" while the prose cites International Organization of Motor Vehicle Manufacturers and European Automobile Manufacturers' Association. Source lines mix narrative "Airbus (2026)" without a suffix with parenthetical suffixed citations of the same author (p. 15).
  - **Italics are inconsistent.** Acerinox (2025) and Alleima (2026) are not italicised, while their neighbours are.
  - **Justified alignment** produces stretched URL lines across pp. 27 to 37.
- There is a text artifact on p. 17: "expansion alloys 42 and 29 18". Removing the hyphen garbled the designation. Write it as Alloy 42 and Kovar type FeNi29Co17, or keep the official name.
- There is a logic error on p. 7: "its intensity differs by two orders of magnitude" compares about 2.1% molybdenum in 316L with 16% in C-276. That is a factor of about 8, less than one order of magnitude.
- On p. 10, "Lithium iron phosphate ... so even the battery does not compensate for lost engine alloy" implies that the company sells battery nickel, which nothing in the report supports.

### 6. Visuals and design: 2.3
- The design follows the brief: Times New Roman, justified text, captions above tables, italic source lines, round bullets, and page numbers top right from page 2. The three figures (pp. 6, 20 and 22) have message titles, sources and readable labels, and the main text is 26 pages.
- There are only three figures in 26 pages, and none of them shows the integration step. The repository already holds unused charts (report/fig/f4_concentration.svg, f7_matrix.svg, f8_bridge.svg). A supply concentration chart in chapter 4 and an attractiveness and ability matrix in chapter 8 would carry the argument faster than the tables.
- Table 20 (pp. 24 to 25) breaks badly. The first column is about 2 cm wide, so each opportunity wraps over six to nine lines. The table runs over two pages, and its eight letter grades cannot be read at a glance. This is the most important exhibit in the report, and it reads like an appendix printout.
- The title of Figure 3 is factually wrong (see criterion 2).
- The title page lists three authors, while CLAUDE.md describes a four person team. Verify this with the team.

## The ten changes that would most improve the grade (ranked by impact)

1. **Define the company and remove VDM-as-company claims. Location:** chapter 2 (p. 3), pp. 6, 10, 11, 16, 19 and 25, and Table 20 "Fit" column (p. 24).
   - **Problem:** The strategy subject is never defined, and VDM's application list is presented as the company's own portfolio and approvals. This breaks the benchmark rule in CLAUDE.md and contradicts A4.
   - **Fix:**
     - Add one sentence in chapter 2 saying who "the company" is and what is known about it.
     - Rewrite every capability claim as conditional, for example "VDM's published list shows that a German producer can serve turbochargers, exhaust sensors ...", and "where the company holds ISO 15156 approvals ...".
     - Rate "Fit" as "to be validated" or base it on stated assumptions listed in A4.
   - **Expected impact:** Storyline 2.3 to 1.7, Actionability +0.3, about 0.2 overall.

2. **Put a quantity behind the Outlook. Location:** 7.1 and 7.2 (pp. 21 to 23), A2 (p. 38).
   - **Problem:** The indices are assumed rates compounded over ten years. There is no tonnage or value, no derivation of g, and no product or region results despite the section title.
   - **Fix:**
     - For at least the two Tier 1 opportunities, build a bottom-up driver tree, for example LEAP and GE9X engine deliveries × superalloy input weight per engine × buy-to-fly ratio = tonnes of bar and billet in 2025 and 2035, and gas turbine GW × tonnes per GW.
     - Label each step as a team estimate and log the assumptions in A2.
     - Derive g from these trees.
     - Add a small product-by-region results table so that 7.2 delivers what its title promises.
   - **Expected impact:** Model transparency 2.7 to 1.7, about 0.2 overall.

3. **Lead with the answer. Location:** end of chapter 2 (p. 3). Chapter 1 stays as the team wrote it.
   - **Problem:** The board reaches the first priority only on p. 23.
   - **Fix:** Close chapter 2 with one paragraph, or a five-row box, that states the answer to the central question. Value lies in conversion and qualification, the Tier 1 to 3 priorities follow, and the first three actions are named. Paragraph changes are allowed below section level.
   - **Expected impact:** Storyline +0.3.

4. **Size, own and target the roadmap. Location:** Table 21 and the governance paragraph (p. 26).
   - **Problem:** The initiatives have no capex, volume, owner or KPI target, and the hurdle-rate rule cannot be applied to an index model.
   - **Fix:**
     - Add columns for indicative size (tonnes or EUR range, team estimate), owner (sales, R&D and quality, operations, procurement) and KPI target with date, for example "5 approved part numbers with two engine OEMs by 2028".
     - Replace the hurdle-rate sentence with a gate tied to signed LTA volume. Alternatively, keep it once item 2 provides volumes.
     - State how much cash automotive and European chemical harvesting must release.
   - **Expected impact:** Actionability 2.3 to 1.7, about 0.1 overall.

5. **Make the reference list APA 7 clean. Location:** References (pp. 27 to 37), source lines of Tables 3, 9 and 17.
   - **Problem:** The same work appears in several entries, there are fake doi.org prefixes, a truncated URL, "n.d.-b" without "n.d.-a", in-text authors that do not match the entries (OICA and ACEA against the spelled-out names), and inconsistent italics.
   - **Fix:**
     - Merge duplicates in data/sources.csv to one REF per work, and use locators (chapter, table, p.) for the different figures.
     - Strip "https://doi.org/" from non-DOI URLs and repair the WNA URL.
     - Use one author form per organisation.
     - Left-align the reference list if the team's document allows it.
   - **Expected impact:** Writing 2.7 to 2.0, about 0.07 overall, and it removes the most visible sign of carelessness for expert readers.

6. **Rebuild the opportunity matrix as a readable, weighted exhibit. Location:** Table 20 (pp. 24 to 25), 8.1.
   - **Problem:** The eight criteria are unweighted, the tiers cannot be traced to the scores, and the layout breaks across two pages with a 2 cm first column.
   - **Fix:**
     - Apply the criterion weights from model/model.py and show a total score per opportunity, so that the tiers follow from the numbers.
     - Use short opportunity labels (for example "SA bar, aero, EU/US") with a legend, so the table fits on one page.
     - Add the existing f7_matrix.svg as Figure 4 (attractiveness against ability to win).
     - For each row, add one evidence pointer to the section that justifies the rating.
   - **Expected impact:** Storyline +0.2, Visuals +0.3.

7. **Complete the Trade chapter with policy and the risk metals. Location:** chapter 6 (pp. 19 to 21).
   - **Problem:** The chapter covers only nickel and cobalt and has no tariffs or regulation.
   - **Fix:**
     - Add a short subsection on trade policy: EU CRMA 2030 benchmarks, CBAM definitive phase 2026, US Section 232 derivative tariffs, and Chinese licences for tungsten and related alloys.
     - Add one sourcing-dependence table for titanium sponge (HS 8108), ferrochrome (HS 720241/49) and molybdenum oxide, giving EU import shares by origin from Comtrade or Comext.
     - Qualify "world's largest exporter" (p. 19). The ranking rests on ten reporting countries, so either use partner "World" totals for all reporters or write "among the ten largest producing economies".
   - **Expected impact:** Research +0.2, Storyline +0.1.

8. **Fix factual and citation errors that experts will catch. Location:**
   - p. 7: "two orders of magnitude". Write "about eight times".
   - p. 8: ATI's 20 month lead time cited to Osaka. Cite the ATI filing.
   - p. 14: the Rolls-Royce claim cited to Safran. Cite Rolls-Royce.
   - p. 14: Boeing fleet of "about 38,000" in 2035. Label it as a team interpolation, as done for Airbus, or delete it.
   - p. 22: the title of Figure 3. Change it to "Aerospace leads demand growth in every scenario, energy technology has the widest range".
   - p. 17: "29 18". Write the correct alloy designation.
   - p. 17: the WSTS jump from USD 796bn to 1.51tn. Add one sentence explaining the memory price effect or double-check the figure.

   **Expected impact:** Research +0.1, Writing +0.1, Visuals +0.1. Each error alone costs credibility with the alloy experts in the audience.

9. **Raise automotive and oil and gas to the spotlight standard and back every named target. Location:** 5.1.2 (p. 10), 5.2.2 (pp. 11 to 12), and the bullets naming SLB (p. 12) and MTU (p. 15).
   - **Problem:** These sections lack at least three who, what, where, when, metal, form and supplier facts, and two recommended customers have no evidence.
   - **Fix:**
     - Add specifics such as the Garrett turbine housing or wheel alloy (for example Alloy 713C or HK30 type castings) and the plant.
     - Add a named clad pipe project with its liner alloy (Alloy 625 or 825), its length and the operator.
     - Add one MTU fact (for example the GTF ramp or Rzeszów and Munich capacity) and one SLB fact, or drop both names.
   - **Expected impact:** Research +0.1, Actionability +0.1.

10. **Use the structured sources the methodology promises and add an Asian competitor view. Location:** chapter 3 (p. 5) against chapters 4 to 6, plus a short competitor table in 8.1.
    - **Problem:** PRODCOM, UNIDO and STAN are announced but barely used, and the Asian competitors behind the 2030 window argument are missing.
    - **Fix:**
      - Add EU sold production of nickel alloy flat and long products (PRODCOM 2442 codes) to 4.1 or chapter 6.
      - Add UNIDO INDSTAT basic metals value added for Germany against China to chapter 6.
      - Add one table in 8.1 listing the competitors in Tier 1 products with group, melt capacity or revenue, home region and qualified OEMs: Acerinox (VDM plus Haynes, counted once), ATI, Carpenter, PCC/SMC, Aubert & Duval, Alleima, Daido and Fushun.
      - Alternatively, trim the claims in chapter 3 to what is actually used.
    - **Expected impact:** Research 1.7 to 1.3, about 0.1 overall.

## Bottom line
Overall grade **2.3**. If items 1 to 6 are done well, the report reaches 1.7. A 1.3 also needs a quantified Tier 1 driver tree (item 2) and a policy-aware trade chapter (item 7). A 1.0 additionally needs the exhibits of chapter 8 to be good enough that an alloy industry board could use them without further work.

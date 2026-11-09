# Round 6 grade, TUM School of Management (project study supervisor)

Graded version: reviews/round_6/report_v6.txt and report_v6.pdf (61 pages. Main text pp. 1 to 29, which is within the 30 page limit. References pp. 30 to 42. Appendices pp. 42 to 61). I also read sections/*.md and reviews/round_5/grader_tum.md.

Context applied: this is pure metal market research, and the recommendations address producers of high performance metals in general. Following the user's decisions, I did not assess the title page, the cover or the table of contents (including the Münvest lines), and I did not deduct for the approved opening of chapter 1. The section titles match data/toc.json. The style is now deliberately plain with short sentences. I judged clarity and flow and did not deduct for sentence length.

## Grades per criterion

| Criterion | Weight | Grade | Weighted |
|---|---|---|---|
| Research depth and source quality | 25% | 1.7 | 0.425 |
| Model transparency and reproducibility | 20% | 1.7 | 0.340 |
| Storyline from data to strategy | 20% | 1.7 | 0.340 |
| Actionability and strategic insight | 15% | 2.0 | 0.300 |
| Writing and house style | 10% | 2.0 | 0.200 |
| Visuals and design | 10% | 2.7 | 0.270 |
| **Overall** | 100% | **2.0** (1.88 computed) | |

Round 5 was 2.0 (1.90). The substance has improved clearly. Chapter 6 is now a real global market size chapter. Electronics now leads to a scored priority 2 position. The aerospace driver is a delivery path, the most specific index rule is applied to every row, and the appendix no longer exposes the team's internal process. I recomputed every row of Table 17 (3.85, 3.85, 3.70, 3.60, 3.45, 3.15, 3.00) and the 2025 and 2035 EUR ranges in Tables 10 and 14 (for example 193 kt × EUR 25.4 = 4.9 bn and 248 kt × 33.4 × 1.41 = 11.7 bn), and all of them reconcile.

The overall grade is held at 2.0 by one defect that has nothing to do with the analysis. **In the round 6 snapshot PDF, none of the three figures renders.** On pp. 8, 24 and 26 the caption is followed directly by its Sources line, with no chart in between. The current report/report.pdf does render Figure 1, so this looks like a fault in the snapshot build, but an examiner grades the file in front of them. With the figures restored, Visuals returns to 2.3, and the computed grade becomes 1.84, which rounds to **1.7**.

## Status of the round 5 fixes

| Round 5 fix | Status |
|---|---|
| 1 Pool and growth that fit the sole priority 1 | Done. Engine bar now uses 193 kt × 0.575 (about EUR 4.0 bn), openly labelled as an upper bound for wrought bar. The most specific driver is applied to every row (engine path 3.7, gas turbine 3.6, SEMI 4.2). A niobium single source rule is added. The fragility sentence now names the Congo quota and a severe aerospace downturn. A new problem appeared (see Storyline (a)). |
| 2 Aerospace haircut and driver | Mostly done. The haircut is the mean of three points (0.982), and the IEA ratio is excluded for aerospace. The delivery path replaces the fleet stock rate. There is still no plan against outcome test from an older outlook vintage, which A4 admits. |
| 3 Internal process language | Done. No "round" wording remains. |
| 4 Score the growing applications | Done. Fab gas strip and tube (priority 2, 3.60), NO96 strip (Option) and repair wire (Monitor) are scored. Table 16 was removed. |
| 5 Chapter 6 as global market size | Done (6.1 and Table 10). Cobalt and titanium wrought trade (HS 8105, 8108) is still not shown. |
| 6 Roadmap to 2035, benchmarks, sizing | Partly done. There is a 2029 to 2035 column, CoCr and Alloy 690 are separate initiatives, and the 1.5 kt gate is sized at EUR 38 to 71 m. The 2029 to 2035 column has no tonnage, date or gate, and the benchmark for initiative 1 contradicts the text (see Actionability (b)). |
| 7 Regional results in 7.2 | Not done. There are still two qualitative sentences and no regional demand number. |
| 8 Reference defects | Partly done. CMOC, SEMI and the appendix source lines are fixed. Five duplicates remain, the third party hosts remain, and a Wikipedia entry is new. |
| 9 Chain figure, matrix visual, pagination | Not done, and worse (the figures are missing in the snapshot). |
| 10 Paragraphs and spotlights | Partly done. The Carpenter surcharge is explained and 4.7.4 is fixed. Automotive still has no spotlight that names an alloy. |

## Justification

**Research (1.7).** The base is strong and current: USGS MCS 2026, the IEA Global Critical Minerals Outlook 2026 dataset, INSG (October 2026), Cobalt Institute, IMOA, ICSG, Comtrade at HS 6 level with mirror flows, PRODCOM, the World Bank, OECD and filings up to Q3 2026. The HS 6 alloy split (alloys are 97, 85 and 87 percent of the traded families) is a genuine piece of original work. Deductions:
(a) **Wikipedia** is cited for the cobalt content of Waspaloy (A2.6, p. 52, References p. 41). That figure decides whether engine bar in all grades scores Supply 2 or 3, which means it separates priority 1 from priority 2. A Wikipedia citation in a decisive position is not acceptable in a TUM report.
(b) Table A13 (p. 59) prints Daido and Nippon Yakin revenues "read from search result summaries and are not verified", although both filings are listed in the references. Either verify them or delete them.
(c) The 2026 copper record (4.7.2, p. 11) still rests on The Oregon Group, which is a blog. Siemens Energy 2026 (GuruFocus), Airbus 2026a (bnains.org), Safran 2026a (edrmagazine.eu) and Western Superconducting (sina.com) are still credited to the issuer but hosted by third parties. Bloom Energy still has a generic investor URL.
(d) Priority 1 turbine remelt stock rests on Siemens Energy alone (Table A1, 7.1). A4 says GE Vernova and Mitsubishi Power data "were not available", but GE Vernova publishes its gas turbine backlog and slot reservations in its 10-K and quarterly filings. This is a gap in the research, not a lack of data.
(e) Spotlights: automotive (5.1.2) still names no alloy grade, product form and supplier together. Chemical processing has only one metal specific spotlight (Sanicro 625 at Mehsana). BASF Zhanjiang names no metal.

**Model (1.7).** The model is reproducible and honest: the formula, seed, copula, Dirichlet settings, every parameter, the calibration to 20.0 kt and the shock arithmetic are documented. The double counting argument against the trend shift is correct. Deductions:
(a) **Chapter 6 and A2.4 do not reconcile.** In 6.1 (p. 22), ten reporters export 64.5 kt of alloy bar plus 30.6 kt of wire (95.1 kt), 41.3 kt of flat products and 18.0 kt of tubes. In A2.4 (p. 50), eight reporters export 80.3 kt of bar and wire, with floors of 38.2 kt (flat) and 15.3 kt (tube). The Table 10 source line says eight reporters. The bar family of 131 kt is built on 80.3 kt, so the numbers printed in the main text are not the ones the model uses.
(b) The combined vacuum melt programme scores 3.70 under base weights, which is priority 2 (Table A5, p. 53). Chapter 2, 8.1 and chapter 9 nevertheless present it as the recommended vehicle (see Storyline (a)).
(c) The engine growth of 3.7 percent sits 0.3 points below the Growth 5 band. Moving it into that band would give engine bar 4.05. The haircut rests on three points from one vintage, so this band edge deserves one sentence of sensitivity, not silence.
(d) Repair wire uses aftermarket growth of 3.1 percent (A2.6), while 5.4.2 says 3.7 percent and Table A9 says 3.8 percent. Explain that the haircut causes the difference, or align the figures.
(e) The superalloy cross checks remain thin. Monroe (5 percent of P50) is a capacity increment, not a level check, and the only level check is Zhiyan Consulting, a commercial source.

**Storyline (1.7).** The answer comes first in chapter 2, chapter 6 now closes the market size link, and electronics, the fastest growing index, now leads to a scored position with an explicit reason why it stays at priority 2 (pool EUR 0.11 bn). The fragility statement now runs in the right direction. Deductions:
(a) **The headline recommendation contradicts its own table.** Chapter 2 (p. 4), 8.1 (p. 28) and chapter 9 (p. 29) say the two priority 1 rows are "best run as one vacuum melt programme", but that programme is priority 2 at base weights and reaches priority 1 only under the alternative weightings. The report needs to recommend two priority 1 rows that share a melt shop, or to state openly that the combined programme is a base case priority 2.
(b) "Results by Region" (7.2, p. 27) gives no regional figure. Two qualitative sentences do not deliver a section title that the team set itself.
(c) Table numbers jump from 11 to 13 and from 15 to 17. An examiner reads this as missing content.

**Actionability (2.0).** The priorities are specific (Alloy 718 triple melt billet, turbine remelt stock and combustor sheet, fab gas strip and tube, CoCr to ASTM F75 and F1537, Alloy 690 hollows). The stop list is explicit and quantified (diesel parts index 69, European base chemicals at 75.0 percent utilisation). The 1.5 kt gate now has a euro value. Deductions:
(a) The 2029 to 2035 column of Table 18 contains activities ("Add VAR, ESR, conversion and inspection", "Scale after signposts") with no tonnage, no date and no gate. Only initiative 1 has a numeric gate before 2028.
(b) 8.2 says correctly that VAR, ESR, conversion and inspection are the bottleneck and VIM is not. The benchmark for initiative 1 is nevertheless the ATI Monroe VIM furnace. Use a remelt benchmark (Alleima's fourth VAR or a disclosed VAR or ESR capex).
(c) For engine bar, the customers named are "forgers for GE Aerospace and Safran", and the firms listed (ATI, PCC, Carpenter, Aubert & Duval, Daido) are incumbent competitors. Name the open market forgers who would buy second source billet.
(d) Table A15 has no kill criteria for fab gas strip, CoCr or Alloy 690, although these are three of the six initiatives.

**Writing (2.0).** The plain style works. The chapters read quickly, the transitions between sections are mostly present, and the text is lint clean. Deductions:
(a) Duplicate references: NVIDIA 2025a and 2025b (the same blog post), IEA 2025c and 2025d (WEO 2025), IEA 2026i and 2026j (both titled "World energy investment 2026"), Eurostat 2024 and 2026c (both the generic PRODCOM database), and Mining Weekly 2026 and Mining.com 2026 (the same article).
(b) There are logic slips. In 4.1 (p. 8), class 1 nickel is "widely available, because the Chinese share of open LME tonnage rose", which is not a causal relation. Also in 4.1, "Margins therefore depend on base prices" does not follow from a pass through.
(c) The single line chapter openers of chapters 7 and 8 give the reader no orientation. Each could state the result in one sentence.
(d) The "not verified" note in Table A13 and the Wikipedia citation are style and credibility failures as well as source failures.

**Visuals (2.7).** The tables are consistent, and Table 17 explains its abbreviations. Deductions:
(a) **None of the three figures renders in the round 6 PDF** (pp. 8, 24, 26). Without them, the report has no visual in 29 pages.
(b) Even once restored, there are only three figures, none in chapters 3, 5 or 8. The value chain is still a table, and the opportunity matrix has no visual.
(c) Tables 2 (pp. 6 to 7), 8 (pp. 19 to 20), 15 (pp. 26 to 27) and 18 (pp. 28 to 29) break across pages.
(d) The table numbering gaps (12 and 16).

## The ten changes that would most improve the grade (ranked by impact)

The main text is 29 pages, so there is about one page of room. Every addition below names an offset.

1. **Rebuild the PDF with the figures and close the numbering gaps** (pp. 8, 24, 26, and the table numbering in chapters 6 to 8).
   - Fix: Check that the snapshot build resolves `fig/*.svg` (report/report.pdf renders them, report_v6.pdf does not), then renumber the tables consecutively.
   - Impact: Visuals 2.7 to 2.3. This alone moves the overall grade from 2.0 to 1.7.
2. **Make the headline recommendation match Table A5** (chapter 2 p. 4, 8.1 p. 28, chapter 9 p. 29, sections/02, 08, 09).
   - Problem: The combined vacuum melt programme scores 3.70, priority 2 at base weights.
   - Fix: Recommend two priority 1 positions, 718 engine bar and turbine remelt stock, which share one melt shop. Report the combined programme as priority 2 at base weights and priority 1 under three alternatives. Add one sentence on the engine growth band edge (3.7 against 4.0, which would give 4.05).
   - Impact: Storyline and Model, about +0.1 overall. It is the first inconsistency an examiner will find.
3. **Reconcile the trade floors in 6.1 with A2.4** (sections/06_trade.md p. 22, Table 10, sections/11_appendices.md A2.4 p. 50).
   - Fix: Use one reporter set (eight or ten) and one set of numbers for bar and wire (95.1 or 80.3 kt), flat (41.3 or 38.2 kt) and tube (18.0 or 15.3 kt). State in Table 10 which floor feeds the family estimate.
   - Impact: Model 1.7 to 1.5.
4. **Replace the weak sources in decisive positions** (A2.6 p. 52, Table A13 p. 59, 4.7.2 p. 11, References).
   - Fix: Cite the Special Metals or Haynes Waspaloy datasheet instead of Wikipedia. Verify the Daido and Nippon Yakin rows from their filings or delete them. Replace The Oregon Group with the World Bank monthly series or an LME release. Give issuer URLs for Siemens Energy 2026, Airbus 2026a, Safran 2026a and Western Superconducting, and a document URL for Bloom Energy.
   - Impact: Research and Writing, about +0.1 overall.
5. **Add a second gas turbine driver** (7.1 p. 25, Table A1 p. 44, 8.1 p. 27, A4 p. 55).
   - Fix: Add GE Vernova gas turbine orders, backlog and slot reservations from its 2025 10-K and Q3 2026 10-Q, and Mitsubishi Heavy gas turbine orders, to the gas turbine ratio. Delete the "not available" sentence in A4.
   - Impact: Research and Model. It removes the stated weak point of a priority 1.
6. **Merge the duplicate references** (References pp. 30 to 42, via data/sources.csv).
   - Fix: Merge NVIDIA 2025a and 2025b, IEA 2025c and 2025d, IEA 2026i and 2026j, Eurostat 2024 and 2026c, and Mining Weekly and Mining.com, and update the in-text letters.
   - Impact: Writing 2.0 to 1.7, together with fix 4.
7. **Finish the roadmap** (Table 18 and 8.2, pp. 28 to 29, Table A15 p. 61).
   - Fix: Give each initiative a 2029 to 2035 milestone with a date and a quantity (for example, remelt step commissioned 2030, 3 kt a year by 2032). Replace the Monroe VIM benchmark with a VAR or ESR benchmark. Name the open market forgers as buyers of engine bar. Add kill criteria for fab gas strip, CoCr and Alloy 690 to Table A15.
   - Impact: Actionability 2.0 to 1.7.
8. **Deliver regional figures in 7.2** (sections/07_scenarios.md p. 27).
   - Fix: Weight the industry P50 indices by the regional shares already quoted (IEA upstream regions, reactors, BASF Asia share, SEMI regions) to get a P50 index or a share of 2025 to 2035 growth for North America, Europe and Asia, labelled as a team estimate. One sentence and three numbers are enough (offset: about three lines).
   - Impact: Storyline, about +0.05 overall.
9. **Fix pagination and add the two framework visuals** (Table 1 p. 5, 8.1 p. 27, and Tables 2, 8, 15 and 18).
   - Fix: Keep each table on one page. Turn Table 1 into a seven box chain figure in the same space. Add a small score against pool bubble chart of Table 17 and Table A5 to 8.1, offset by moving Table 15 to A2.4.
   - Impact: Visuals 2.3 to 2.0.
10. **Complete the spotlights and repair the logic slips** (5.1.2 p. 13, 5.5.2 p. 18, 4.1 p. 8, and the openers of chapters 7 and 8).
    - Fix: Add an automotive spotlight that names the turbine housing or wheel alloy, its form, the Garrett or BorgWarner programme and a likely supplier. Add a second metal specific chemical spotlight, for example a named NiCrMo plate order or a clad plate project in Asia. Rewrite the class 1 "because" sentence and the "margins depend on base prices" sentence in 4.1. Let the openers of chapters 7 and 8 state the result.
    - Impact: Research and Writing, about +0.05 overall.

Overall grade **2.0** (1.88), and **1.7** (1.84) as soon as the figures render. Fixes 1 to 4 would make 1.7 secure. A 1.3 would also need fixes 5, 7 and 9: a second turbine driver behind priority 1, a roadmap with gates through 2035, and visuals that carry the argument in chapters 3 and 8.

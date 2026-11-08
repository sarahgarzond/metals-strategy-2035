# Round 5 grade, TUM School of Management (project study supervisor)

Graded version: reviews/round_5/report_v5.txt and report_v5.pdf (60 pages. Main text pp. 1 to 30, exactly at the limit. References pp. 31 to 42. Appendices pp. 42 to 60). I also read sections/*.md, data/clean/model_scoring_inputs.csv and reviews/round_4/grader_tum.md.
Context applied: this is pure metal market research, and the recommendations address producers of high performance metals in general. The framework is the seven link chain, and chapter 3 sets out the two tier outlook. Following the user's decisions, I did not assess the title page, the cover page or the table of contents (including the Münvest lines). I did not deduct for the approved chapter 1 or its opening. I checked the headings against data/toc.json and they match in order. The house-style lint reports 0 violations in every section.

## Grades per criterion

| Criterion | Weight | Grade | Weighted |
|---|---|---|---|
| Research depth and source quality | 25% | 1.7 | 0.425 |
| Model transparency and reproducibility | 20% | 1.7 | 0.340 |
| Storyline from data to strategy | 20% | 2.0 | 0.400 |
| Actionability and strategic insight | 15% | 2.0 | 0.300 |
| Writing and house style | 10% | 2.0 | 0.200 |
| Visuals and design | 10% | 2.3 | 0.230 |
| **Overall** | 100% | **2.0** (1.90 computed, at the edge of 1.7) | |

Round 4 was 2.0 (1.99 computed). This round fixed the most serious problem from round 4. The scores now follow the team's own rules. FeNi36 foil has Market 1 and drops to Option. Chemical plate now uses an end use specific pool of EUR 0.72 bn instead of the all end use EUR 1.8 to 2.8 bn. Fusion C-276 tape now has Supply 2 because of the tungsten licence. I recomputed all eleven rows of Table 17 (3.80, 3.65, 3.45, 3.20, 3.15, 3.10, 3.00, 2.95, 2.75, 2.55, 2.35) and the equal weight check (3.875, 3.750, 3.250), and all of them reconcile.

The FeNi index has been rebuilt on OLED mask foil, EV sensors and lead frames, which removes the SEMI driver that had no logical link to FeNi. The supply overlay now includes a tungsten licence halt. Optimism haircuts now come from plan against outcome tests. Table 1 has seven links. The reference list layout is fixed: the hanging indent and left alignment now apply on every page.

The report is still not a 1.7 overall, for three reasons. First, the only priority 1 position depends on a market pool and a haircut that do not fit the product they score. Second, the appendix exposes the team's internal process ("Since round 5", "Round 4 shift"). Third, the fastest growing industry in the report's own thesis (electronics, P50 141) produces no scored opportunity apart from a gated option.

## Status of the round 4 fixes

| Round 4 fix | Status |
|---|---|
| 1 Score against the rules, retest FeNi | Done. FeNi is now an Option at 3.20, and the maskless risk now cites DNP and TrendForce. |
| 2 Right drivers for FeNi and aerospace | Half done. FeNi is rebuilt (A2.4). Aerospace still uses the Airbus fleet stock growth of 3.4 percent as engine output growth (Table A1). There is still no real aerospace backtest series, because STAN C30 is nominal. |
| 3 Chapter 1 opening | Excluded by user decision. |
| 4 Chapter 8 as an argument, trade evidence | Mostly done. 8.1 now has argued paragraphs and uses the USD 111 m bar corridors. Trade still does not enter any criterion in Table A4. |
| 5 Measurable gates, fitting benchmarks | Gates done (1.5 kt by Q4 2027, Q2 2028 melt decision). Benchmarks still do not fit (see fix 6). |
| 6 References | Layout done. Boeing, UNSD 2026f, Mining.com and "l'Industrie" are fixed. CMOC as author of a Mining Weekly article remains, and so does the generic Bloom URL. New duplicates appeared (see fix 8). |
| 7 "By Region" in 7.2 | Half done. Investment numbers are given, but there is no regional alloy demand figure. |
| 8 Chain figure, more figures, pagination | Partly done. Table 1 has seven rows. There are still three figures. Tables 3, 11, 12 and 15 split across pages, and "Implications for suppliers:" is still orphaned at the foot of p. 16. The Figure 4 reference is gone. |
| 9 Method claims in chapter 3 | Done. The second source claim is now honest, and a tungsten shock is in Table 15. |
| 10 Paragraphs and spotlights | Partly done. The chemical spotlight now names Sanicro 625 tube at Mehsana. Automotive still names no alloy. 4.7.4 is still one sentence of about 60 words. The copper contradiction is resolved, but the record price still rests on a blog. |

## Justification

**Research (1.7).** The numbers are driven by current editions of primary and structured sources: USGS MCS 2026, the IEA Global Critical Minerals Outlook 2026 dataset, INSG (October 2026), Cobalt Institute, IMOA, ICSG, IAI, Eurostat PRODCOM, UN Comtrade with mirror flows, the World Bank, OECD, SEMI, WSTS, Cefic, and filings up to Q3 2026 (ATI, Sandvik, Vertiv, BorgWarner, GE 10-Q). Spotlights are strong in aerospace (Safran Gennevilliers EUR 150 m, 30,000 t, 2029), energy (Siemens Energy 17 to above 30 GW, Alleima Sandviken plus 60 percent), electronics (NVIDIA Kyber 2027, DNP Kurosaki, TrendForce on FMM free lines) and medical (ASTM F75, F1537, F3213, F2384, OXINIUM 94.1 percent). Deductions:
(a) The 2026 copper record (Table 2, 4.7.2) still rests on The Oregon Group, a commodity blog.
(b) "CMOC Group" is listed as the author of a Mining Weekly article (References p. 33). Several primary authors are credited for third party hosts: Infineon via Evertiq, Westinghouse via K&L Gates and the ANS, Siemens Energy 2026 via GuruFocus, Airbus 2026a via bnains.org, and Safran 2026a via edrmagazine.eu. Each of these entries needs either the issuer's own URL or the actual publisher as author.
(c) The only cross check of the 193 kt superalloy tonnage is Zhiyan Consulting (A2.4), which is a commercial source used in a decisive position.
(d) Automotive (5.1.2) still has no spotlight that names an alloy grade, a product form and a likely supplier together. The Garrett and BorgWarner facts name units and programmes but no alloy.
(e) The data base already holds Comtrade HS 8105 and 8108 (A3), but no cobalt or titanium wrought product market appears in chapter 6.

**Model (1.7).** The model is reproducible: the formula, seed, copula, Dirichlet settings, every parameter in Table A1, the calibration to 20.0 kt and the shock arithmetic in A2.4 are all documented. The tonnes are labelled as team estimates and are never summed. Dropping the double counted trend shift is correct, and it is well argued. The grade is held at the lower edge of 1.7 by these points:
(a) The engine bar Market 5 uses the 11.5 kt aviation cobalt pool. Alloy 718, the lead billet grade, contains almost no cobalt, and aviation cobalt also covers cast blades made from remelt stock. That cast share belongs to the turbine remelt row, which is restricted to the 8.5 kt non aviation pool. If engine bar scored Market 4 on a wrought share of the pool, it would score 3.65 and fall to priority 2.
(b) The "most specific index" rule in Table A4 is applied inconsistently. Car parts use the combustion sub index and Alloy 690 uses the nuclear ratio. Engine bar, however, uses the total aerospace index (2.98 percent) and not the new engine series that the scoring inputs already hold (3.86 percent). Turbine remelt likewise uses the total energy index and not the gas turbine ratio. Applied consistently, the rule would move both rows up.
(c) The aerospace haircut mode of 0.92 is close to the single Boeing 737 observation (0.894). It ignores the LEAP observation (1.068), although engine output is the driver being haircut. The IEA test compares a 2024 price basis estimate with a 2025 price outcome (note to Table A6), so the 0.951 ratio mixes price bases. This haircut alone costs aerospace 13 index points and pushes it below the 3.0 percent band.
(d) Engine output growth is still the Airbus fleet stock growth (3.4 percent). Deliveries include replacements, so this is a level effect, not a growth rate of the fleet stock.
(e) Figure 3 does not match Table 13 everywhere: electronics P90 is 176 in the figure and 177 in the table, and aerospace P10 is 122 against 121.
(f) In Table A4, the EUR bands for Market scores 2 and 4 are undefined, and the pools for Alloy 690 (EUR 0.077 bn) and car parts (EUR 0.251 bn) fall into that gap.

**Storyline (2.0).** Chapter 2 gives the answer first, and the conclusion answers the central question in the same terms. Chapter 8 now argues each position through material, demand, trade and growth. Deductions:
(a) The thesis says electronics leads at P50 141, but the only electronics position is a gated FeNi option. Fab gas delivery strip and tube (Table 8, "Grows") drives 60 percent of the electronics index and is never scored. LNG Invar strip (5.2.2, Aperam Imphy doubled) and repair wire (5.4.2, aftermarket at half the aerospace weight) are also absent from Table 17.
(b) Chapter 6 is titled "Global Market Size", yet the only global 2025 tonnages (Table 14: 193 kt superalloy, 135 kt bar, 282 kt flat, 45 kt tube) appear in chapter 7. This breaks the chain, where market size belongs in chapters 5 and 6.
(c) The fragility statement is wrong in direction. Chapter 2 and 8.1 say that the rank is fragile because 2.98 percent "sits at the edge of a scoring band". That edge is an upside risk, since 3.0 percent would give Growth 4 and a score of 4.00. The real fragility is the 0.05 margin and the pool and haircut choices described in Model (a) and (c).
(d) 7.2 regional analysis gives investment shares only, and no alloy demand by region.
(e) The trade corridors support the argument in prose only. They do not enter any criterion in Table A4.

**Actionability (2.0).** The priorities are specific (Alloy 718 and 720Li triple melt billet, CoCr to ASTM F1537 and F75, Alloy 690). Customers are named, and the stop list is explicit. The gates are now numeric and dated, and they are mirrored by the kill criteria in Table A14. Deductions:
(a) The roadmap is titled 2026 to 2035, but every gate falls between 2027 and 2028. Nothing covers the melt step build, ramp up, the tier 2 signpost reviews or the 2028 model rerun in 2029 to 2035.
(b) The benchmarks still do not fit the initiatives. Avesta flat capacity cost is used for remelt stock, Alleima Mehsana (a finishing plant for chemical customers in India) for CoCr and Alloy 690, an undisclosed Imphy VIM figure for FeNi, and ATI's nickel use for dual sourcing.
(c) Initiative 3 merges CoCr and Alloy 690, which are two businesses with different buyers, and its gate covers only implants.
(d) No euro sizing is given. The 1.5 kt gate is not translated into revenue at the HS 7505 unit values already in Table 10.
(e) Carpenter medical sales appear as USD 224.3 m in 5.7.2 and USD 278.4 m in 8.1, without the explanation that the first figure excludes surcharge.

**Writing (2.0).** The register is expert, and the text is lint clean. The reference layout now meets the brief. Deductions:
(a) Internal process language reaches the reader: "Since round 5" (A2.1, A2.3), the Table A2 column "Round 4 shift", "The round 4 method would have shifted..." (A2.3), "Round 4 had weighted SEMI..." (A2.4) and "earlier fixed rate workbook values". An examiner does not know what a round is.
(b) Duplicate references remain: NVIDIA 2025a and 2025b (the same blog post), IEA 2025c and 2025d (WEO 2025), IEA 2026h and 2026i (WEI 2026), Eurostat 2026b and 2026c (sts_inpr_a), and SEMI 2026a and 2026c (the same release).
(c) Several appendix source lines use names that differ from the reference list, which breaks the APA rule that the in-text author must match the entry exactly. Examples are "OICA (2026), ACEA (2026)" in Table A5, "Cefic (2025, 2026)" in Table A9, "WSTS (2026), SEMI (2026), NVIDIA (2025)" in Table A10, and "Airbus (2026), SIPRI (2026)" in Table A8.
(d) Several paragraphs are still a single sentence: the 4.7 opener, 4.7.3, 4.7.4 (about 60 words), the chapter 6 opener, the 7.2 opener, "Table 15 shows..." and the 8.1 opener. The 8.1 paragraph on engine bar opens with a chained sentence of about 70 words.

**Visuals (2.3).** The tables are consistent, and Table 17 explains its abbreviations. The fan chart (Figure 3) carries a message title. Deductions:
(a) There are still only three figures in 30 pages, and none in chapters 3, 5 or 8. Neither the chain nor the opportunity matrix is shown visually.
(b) Tables 3 (pp. 13 to 14), 11 (pp. 23 to 24), 12 (pp. 25 to 26) and 15 (pp. 27 to 28) break across pages.
(c) "Implications for suppliers:" is orphaned at the foot of p. 16. The Sources lines of Table 2 (p. 7) and Table 8 (p. 21) are separated from their tables.
(d) The Figure 1 axis is labelled only to 2024, although the series ends in 2025.
(e) The Figure 3 labels conflict with Table 13 (see Model (e)).

## The ten changes that would most improve the grade (ranked by impact)

Every change must be space neutral, because the main text is exactly 30 pages. Offsets are named where text is added.

1. **Base the sole priority 1 on a pool and growth rate that fit the product** (sections/08_recommendations.md, Table 17 and 8.1 paragraph 2, pp. 28 to 29. sections/11_appendices.md, Table A4, p. 52. data/clean/model_scoring_inputs.csv).
   - Problem: Engine bar Market 5 uses all aviation cobalt, although its lead grade 718 carries almost no cobalt and cast blade remelt stock sits in the same pool. The "most specific index" rule is applied to downside rows (car, Alloy 690) but not to engine bar (new engines 3.86 percent) or turbine remelt (gas turbine ratio).
   - Fix: Split aviation cobalt into wrought and cast shares with a stated team assumption, or score engine bar on the HS 7505 bar pool. Apply the most specific index to every row. Rerun model/scoring.py and report the result openly, including whether engine bar stays priority 1 and whether turbine remelt joins it.
   - Also: rewrite the fragility sentence in chapter 2 and 8.1. The band edge is an upside, and the downside is the 0.05 margin together with the pool choice.
   - Impact: Model and Storyline, about +0.1 overall. This is the first attack an industry examiner will make.
2. **Rebase the aerospace haircut and driver** (sections/07_scenarios.md, Table 12 and the haircut paragraph in 7.1, pp. 25 to 26. Tables A1 and A2, pp. 47 to 49).
   - Problem: The haircut mode of 0.92 follows the single Boeing airframe observation and ignores LEAP (1.068). The IEA ratio of 0.951 compares 2024 and 2025 price bases. Engine output growth is the fleet stock rate.
   - Fix: Put both upstream values on the same price basis. Set the aerospace mode to a documented rule (for example the mean of the engine relevant tests), or justify why the airframe miss applies to engines. Replace the 3.4 percent with a delivery based path: 42,060 Airbus deliveries over 20 years against 2025 deliveries of 1,393 (Table A14) give the implied ramp. Add one plan against outcome row for an older outlook, for example Airbus GMF 2019 deliveries against actual 2020 to 2025.
   - Impact: Model 1.7 to 1.5 and more robust priorities.
3. **Remove internal process language from the appendix** (sections/11_appendices.md, A2.1, A2.3, Table A2, A2.4, pp. 43 to 50).
   - Fix: Delete "Since round 5", the "Round 4 shift" column (rename it "Used for" with the values "range only" and "haircut"), and the paragraph comparing the round 4 method and the "earlier fixed rate workbook values". If the sensitivity is wanted, keep one sentence: "Adding the trend error as a growth shift would give P50 indices of 156, 115, 140 and 98, which double counts guidance."
   - Impact: Writing and Model credibility, about +0.05 overall. The cost is negligible.
4. **Score the measured applications that the report itself identifies as growing** (sections/08_recommendations.md, Table 17, p. 29. Sources in Table 8 p. 20, 5.2.2 p. 15, 5.4.2 p. 18).
   - Fix: Add three rows: high purity nickel alloy strip and tube for fab gas delivery (the electronics index, SEMI driver), FeNi36 strip for LNG membrane tanks (Aperam Imphy doubling, IEA LNG 560 to 880 bcm) and superalloy repair wire (aftermarket 3.7 percent). State why each lands where it does, so that electronics at P50 141 leads to a recommendation or an explicit reason why not.
   - Space: move Table 16 to Table A3, since its four rows repeat chapter 3.
   - Impact: Storyline 2.0 to 1.7.
5. **Make chapter 6 the global market size chapter** (sections/06_trade.md, 6.1, pp. 22 to 23, and sections/07_scenarios.md, Table 14, p. 27).
   - Fix: Present the 2025 tonnes of Table 14 (superalloy 193 kt, bar 135 kt, flat 282 kt, tubes 45 kt, with P10 to P90) in 6.1 as the global size at the mill product stage, labelled as team estimates. Keep only the 2035 tonnes in chapter 7. Add one line of Comtrade HS 8105 and 8108 wrought trade values for cobalt and titanium, which A3 says were already pulled.
   - Impact: Storyline and Model, about +0.05 overall. It also closes the chain at the link the framework assigns to chapters 5 and 6.
6. **Finish the roadmap to 2035 and fix the benchmarks** (sections/08_recommendations.md, Table 18 and 8.2, p. 30).
   - Fix: Add a 2029 to 2035 column or row covering the melt step build after the Q2 2028 decision, ramp to x kt, the tier 2 signpost review and the model rerun. Split CoCr and Alloy 690 into separate initiatives with their own gates.
   - Benchmarks: use Avesta only for flat products. Use the ATI Monroe VIM furnace (9 kt) for remelt stock. For dual sourcing, use a cobalt or tungsten sourcing or revert loop example from the filings. For FeNi, drop the undisclosed Imphy figure.
   - Sizing: translate 1.5 kt into an indicative revenue at the EUR 25.4 to 33.4 per kg bar unit values of Table 10, as a team estimate.
   - Impact: Actionability 2.0 to 1.7.
7. **Deliver regional results in 7.2** (sections/07_scenarios.md, regional paragraph, p. 28).
   - Fix: Give a P50 alloy demand index or a share of 2025 to 2035 growth for North America, Europe and Asia, derived from the industry indices and the regional investment shares already quoted, labelled as a team estimate. Three numbers in one sentence are enough.
   - Impact: Storyline and Model, about +0.05 overall.
8. **Clean the remaining reference defects** (References pp. 31 to 42 via data/sources.csv. Appendix source lines pp. 54 to 57).
   - Merge the duplicates NVIDIA 2025a and 2025b, IEA 2025c and 2025d, IEA 2026h and 2026i, Eurostat 2026b and 2026c, and SEMI 2026a and 2026c.
   - Correct the authors or URLs for CMOC (Mining Weekly), Infineon (Evertiq), Westinghouse (K&L Gates, ANS), Siemens Energy 2026 (GuruFocus), Airbus 2026a and Safran 2026a.
   - Give Bloom Energy a document URL, and replace The Oregon Group with an LME or World Bank monthly series for the copper record.
   - Replace "OICA (2026), ACEA (2026), Cefic, WSTS, SIPRI, Airbus (2026)" in the A5 to A11 source lines with the exact reference authors and letters.
   - Impact: Writing 2.0 to 1.7 and Research.
9. **Add the chain figure and a matrix visual, and fix pagination** (sections/03_framework_and_methodology.md Table 1 p. 5, sections/08_recommendations.md p. 29).
   - Fix: Turn Table 1 into a seven box chain figure in the same space. Replace part of the prose in 8.1 with a small bubble chart of score against evidence. Keep Tables 3, 11, 12 and 15 on one page, keep "Implications for suppliers:" (p. 16) and the Sources lines of Tables 2 and 8 with their content, label the Figure 1 axis to 2025, and regenerate Figure 3 from the same run as Table 13 (176 against 177, 122 against 121).
   - Impact: Visuals 2.3 to 2.0.
10. **Merge one sentence paragraphs and complete the automotive spotlight** (sections/04_7_other_metals.md 4.7 opener, 4.7.3 and 4.7.4. sections/06_trade.md opener. sections/07_scenarios.md 7.2 opener and the Table 15 lead in. sections/08_recommendations.md 8.1 opener. sections/05_1_automotive.md 5.1.2. sections/05_7_medical_technology.md 5.7.2).
   - Fix: Merge the single sentence paragraphs into topic, evidence and transition units, and split the 60 to 70 word chains in 4.7.4 and 8.1 paragraph 2.
   - Automotive: add one spotlight naming the turbine housing or wheel alloy and its form in a named Garrett or BorgWarner programme, together with a likely supplier.
   - Medical: state that USD 224.3 m excludes surcharge and USD 278.4 m includes it.
   - Impact: Writing and Research, about +0.05 overall.

Overall grade **2.0** (1.90). Fixes 1 to 4 done well, together with fix 6, would move the report to a secure 1.7. A 1.3 would also need the global size in chapter 6 to cover more than nickel, and visuals in chapters 5 and 8 that carry the argument.

# Round 4 review: client CEO (reader: CEO of a high performance metals producer receiving a pure market study)

I reviewed reviews/round_4/report_v4.txt and report_v4.pdf, sections/*.md, data/toc.json, CLAUDE.md and my round 3 review.
The headings match data/toc.json in order, and the seven link chain is applied consistently from chapter 4 to chapter 8.
The report names no client in the body, and I did not ask for any company specific content. I judged one thing: could a
producer of nickel, cobalt and specialty alloys act on this report on Monday?

## Overall grade: 2.0 (weighted 1.97)

| Criterion | Weight | Grade | Why |
|---|---|---|---|
| Research depth and source quality | 25% | 1.7 | The sources are current and primary: USGS MCS 2026, INSG, the Cobalt Institute, IMOA, Comtrade with mirror flows, PRODCOM, IEA upstream data by region, and Q3 2026 filings. The spotlights are named and dated. Two gaps remain. Chapter 1 still sizes the segment only from paid reports (IMARC, Insight Partners). Section 6.4 still does not give the US tariff status of HS 7505 to 7507. |
| Model transparency and reproducibility | 20% | 2.0 | Round 3 asked for several fixes and the team made them. A2 now has a backtest, the Monte Carlo run has a seed, Table A4 gives the scoring anchors and Table 10 uses border unit values. I rechecked all three priority 1 scores (4.05, 4.00 and 3.90) and they are correct. New weaknesses: FeNi jumped from the lowest product family index (about 110 in round 3) to the highest (157). The cause is a 0.30 weight on the electric vehicle parts sub index (192), which is an assumption, and the report does not explain the jump. FeNi also scores Market 3, although no FeNi volume is measured anywhere, and the A4 anchor for that case is a 1. The supply overlay is compressed into one sentence that I cannot reproduce ("13 to 20 percent of it"). |
| Storyline from data to strategy | 20% | 2.0 | The thesis "value lies in conversion and qualification" holds from chapter 2 through chapter 9, and each section bridges to the next. But chapter 2 still states the thesis without the answer. It names no priority 1 segments, gives no headline 2035 numbers for either tier and has no stop list, so a board reading only chapters 2 and 9 gets the priorities only at the very end. Section 7.2 "Region" is still one sentence. |
| Actionability and strategic insight | 15% | 2.3 | This is better than round 3. Named buyers (Siemens Energy, CPP, GE Aerospace, Safran, DNP, BOE, Stryker, Zimmer Biomet), a stop list, a sensitivity line and a benchmark per initiative are now in the report. But the benchmarks cannot be compared: one is a tonnage without a cost (ATI Monroe), one a cost without a tonnage (Carpenter Athens), one a margin (powder 7.9 percent) and one a group capex figure set against procurement (Daido JPY 36 bn). None of them gives a cost per tonne. Gates such as "contracts for half by 2028" and "Asian orders rise" are not measurable, and the A14 kill criteria are unchanged from round 3. Timing is also inconsistent: 5.4 says the window narrows around 2030, yet Table 17 builds VIM and VAR capacity only from 2029 to 2035. |
| Writing and house style | 10% | 2.0 | The hyphens in chapter 1 and the stray comma are fixed. The reference list still has duplicates and author errors: Boeing 2026a and 2026b are the same CMO, and CMOC Group is given as the author of Mining Weekly and Mining.com articles. Copper is still "USD 9,947/t, LME record in 2026" in Table 2 against "above USD 14,500" in 4.7.2. Indonesia's share of nickel is given as 63 percent in chapter 1 and "about 67%" in Table 2 without saying which source each figure uses. Chapters 7 and 8 are very dense: single sentences carry four facts. |
| Visuals and design | 10% | 2.0 | The main text now ends on page 30, so the page limit is met, and the figures have message titles. The title page still shows "Münvest" twice. This needs an explicit decision from the team under the no naming rule. Table 17 cells are too terse to read on their own ("Closed loop revert", "Gate: no source above half"). |

## Round 3 fixes: status

| Round 3 fix | Status |
|---|---|
| 1 Page limit | Applied (the Conclusion ends on page 30) |
| 2 Market size per sector | Partly applied: each 5.x.1 now closes with the best measured size at a named stage, but there is still no tonnage or EUR size for any priority 1 prize |
| 3 FeNi row and growth rule | Applied in form (the A4 rule is stated), but the FeNi index swing is not explained and the Market score breaks the A4 rule |
| 4 Benchmarks per initiative | Partly applied: there is now one figure per row, but no cost per tonne and no time to approval |
| 5 Supply stress overlay and severe aerospace case | Partly applied: one dense sentence on cobalt, nickel and copper, no tungsten licence shock, no 2020 type aerospace case |
| 6 Ranking sensitivity | Applied (8.1 and the note under A4) |
| 7 Section 232 status of HS 7505 to 7507 | Not applied |
| 8 Table 10 unit values | Applied |
| 9 Measurable kill criteria with likelihood and impact | Not applied (A14 is unchanged) |
| 10 Chapter 1 sources, title page, duplicate references | Partly applied: the hyphens are fixed, but the paid report sizing, Münvest, Boeing a/b and the CMOC authors remain |

## Can a producer decide on Monday?

- What to invest in: mostly yes. Turbine remelt stock and combustor sheet, triple melt 718 and 720Li billet, and FeNi36 foil are clear. A producer still cannot compare the size of the cheque per tonne, or the size of the prize, against those three options.
- Where to sell: yes. The report names engine and turbine chains in the US and Western Europe, mask makers in East Asia, the Middle East and South America for sour service, and Asian EPC contractors for chemical plate.
- What to stop: yes, on the list (diesel only parts, European base chemical new build, electrolyser capacity before funded orders, captive cladding zirconium). It is not quantified, and the list is missing from chapter 2.

## Five questions my board would ask that the report does not answer

1. How many tonnes, and how many EUR, are turbine remelt stock, engine billet and FeNi foil worth in 2025 and in 2035? The indices have no base, so we cannot size a business case.
2. What does a qualified tonne of VIM and VAR capacity cost, and how many years pass from the decision to the first approved revenue? Table 17 lists peer figures, but they cannot be compared with each other.
3. If we start qualifying in 2026 and build capacity after 2029, do we arrive before or after ATI Monroe (2027) and Safran Gennevilliers (2029) close the second source window?
4. Are European nickel alloy bar and strip exports to the US (our main corridor in 6.3) under Section 232 or reciprocal tariffs, and what does that do to landed cost?
5. FeNi depends on one unmeasured market, a 0.30 weight on electric vehicle sensors, and a mask technology that maskless patterning could replace. What does FeNi score with Market 1 and electronics weight alone, and does it stay in priority 1?

## Top ten improvements, ranked by impact

| Rank | Location | Problem | Concrete fix | Expected impact |
|---|---|---|---|---|
| 1 | Chapter 2, third paragraph (sections/02_objective_and_scope.md) | The board summary carries the thesis but not the answer. It names no priority 1 segments, gives no 2035 figures for either tier and has no stop list. There is no executive summary, and the table of contents is frozen, so chapter 2 has to do that job. | Add three sentences after "earn trade surpluses that the mining countries do not". The first names the three priority 1 segments with their buyers and regions. The second gives the tier 1 headline (energy P50 156 and aerospace 147, automotive 98) and says that tier 2 is a register with signposts. The third gives the stop list. Keep the chapter on page 4. | Storyline 2.0 to 1.7, overall about 0.07 |
| 2 | 7.2 Table 14, or a new line under it, with the assumption in A2 | Market size is still empty for the priority 1 prizes, so no business case can be sized. | Add an "indicative 2025 base, team estimate" column. Base superalloy remelt stock and billet on 20 kt of superalloy cobalt (11,499 t of it in aviation) scaled by cobalt content, base FeNi on Comtrade HS 7506 or PRODCOM where possible, and give "not estimable" where no basis exists. Multiply by P10, P50 and P90 to get 2035 tonnes. Never add the rows together. | Model 2.0 to 1.7, overall about 0.07 |
| 3 | 8.2 Table 17, "Benchmark and gate" column | The benchmarks cannot be compared (a tonnage, a capex, a margin, a group capex), they give no cost per tonne, and the gates cannot be measured ("half" of what, "Asian orders rise"). | Restate the column as an external benchmark in cost per annual tonne where both figures are public (for example Outokumpu Avesta, about EUR 150 m for about 13 kt, or about EUR 11,500 per tonne), and give the time to first approval from A7. Write each gate as a number and a date (for example "long term agreements covering 50 percent of a 3 kt step by end 2028"). | Actionability 2.3 to 1.7, overall about 0.09 |
| 4 | 8.2 Table 17, initiative 1, against 5.4.2 last paragraph | The timing contradicts the window: 5.4 says the window for a new European source narrows around 2030, yet capacity comes only from 2029 to 2035. | Either move the capacity decision to 2027 or 2028, so that it starts as soon as the contracts are signed, or state explicitly that the play is second source capacity after 2030. Name the date of the go or no go decision in one sentence. | Actionability, overall about 0.04 |
| 5 | 8.1 Table 16 FeNi row, and 7.2 Table 14 | FeNi scores Market 3 although no volume is measured (the A4 anchor for that case is 1), and its index swung from about 110 to 157 because of an assumed 0.30 weight on electric vehicle parts. With Market at 1 it scores 3.60 and drops to priority 2. | Either justify Market 3 with a measured pool (for example DNP mask sales or Comtrade FeNi foil exports) or score it 1 and move FeNi to priority 2 as a gated position. Add one sentence in 7.2 explaining why the FeNi index changed, and show the electronics only variant. | Model and Storyline, overall about 0.06 |
| 6 | 7.2 supply overlay paragraph | The paragraph is one sentence with four claims, "13 to 20 percent of it" is ambiguous, there is no tungsten licence shock, and aerospace has no 2020 type downside, so the supply half of the central question stays thin. | Turn the paragraph into a three row table (Congo quota held, Chinese tungsten licence halt, Indonesian quota cut). Give the affected product family, the cost pass through via surcharges and any change to the tiers. Add a severe aerospace case (two years at minus 20 percent, then recovery) and report the P50 that results. | Storyline and Model, overall about 0.05 |
| 7 | 6.4 Trade policy | The US tariff status of nickel mill products (HS 7505 to 7507, 8311) is still missing, although Germany to the US is a priority corridor in 6.3 and 8.1. | Cite the USITC HTS or the White House proclamation for 2026, state whether chapter 75 falls under Section 232 or reciprocal tariffs, and add one sentence on the effect on landed cost for European exporters. | Research and Actionability, overall about 0.04 |
| 8 | Appendix A8, Table A14 | The kill criteria are still not measurable ("Falling hot section nickel content", "Prices below conversion cost") and carry no likelihood or impact. | Give each criterion a threshold and a date, and add an H, M or L column for likelihood and for impact. | Actionability, overall about 0.03 |
| 9 | 7.2 regional paragraph | "Region" is one sentence ("the United States, a fifth of superalloy cobalt"), so the Geography link to 2035 is thin. | Add a small table of where each priority driver sits by region (engine deliveries, turbine GW, reactors under construction, implant procedures, chemical growth), with the source year. | Storyline, overall about 0.03 |
| 10 | Title page, chapter 1, references, Table 2 | Münvest appears twice on the title page. Chapter 1 sizes the segment only from paid reports. Boeing 2026a and 2026b are duplicates, CMOC Group is the author of news articles, the copper "LME record" contradicts 4.7.2, and the Indonesia share is 63 percent in chapter 1 against 67 percent in Table 2. | Ask the team to decide on the title page. Anchor chapter 1 on Comtrade HS 7505 to 7507 exports, with the paid reports as triangulation. Merge the Boeing entries, give Mining Weekly and Mining.com as authors, label USD 9,947 as the 2025 average, and name the source behind each nickel share. | Writing 2.0 to 1.7, overall about 0.04 |

## Smaller points

- Chapter 3 says that "every key figure is confirmed by a second independent source". Many figures from filings are single source, so soften this to "where available".
- Chapter 3 says that outlooks are "corrected for the past optimism of official outlooks", yet the backtest shows that gas power was underestimated. Write "corrected for past bias" instead.
- The Table 15 electrolyser signpost ("Nucera orders above EUR 356 m") needs a year so that it can be tested.
- Section 8.2 has only two sentences of prose. One sentence per initiative explaining why it comes in that order would help a board.

# Round 2 review: client CEO (EUR 400m German nickel alloy and specialty metals producer)

Reviewed: report/report.pdf (40 pages, main text title page to Conclusion = 25 pages, within the 30 page limit).
Judged against CLAUDE.md, data/toc.json and the grading rubric. Round 1 was ignored. No executive summary was requested,
because the team's table of contents has none by choice.

## Overall grade: 2.7 (weighted 2.54)

| Criterion | Weight | Grade | Why |
|---|---|---|---|
| Research depth and source quality | 25% | 1.7 | USGS MCS 2026, INSG, Cobalt Institute, Comtrade, Eurostat, IEA, OECD and recent filings (ATI Q3 2026, Vertiv 10-Q, Sandvik Q3 2026) are current and specific. Stage ladder is applied with discipline. Gaps: no US tariff or CBAM evidence, no German energy cost evidence, no defence demand beyond one SIPRI line, chapter 1 market size rests only on two paid reports. |
| Model transparency and reproducibility | 20% | 3.0 | Formula and rates are transparent (Table 18, A2), but the chain stops before "Market size": no segment is sized in EUR or tonnes, the eight criteria in Table 20 carry no weights or scores although model.py defines both, and the growth rates are judgement with no derivation from the anchors (why 4.0% for energy when the anchor is a 76% capacity step to 2028). Nothing ties the indices to the company's own mix, so the board cannot see a portfolio growth rate. |
| Storyline from data to strategy | 20% | 2.3 | Metal first, industry second is followed cleanly, every section ends with a bridge, and chapter 8 cites back to 4 to 7. But the answer arrives on page 22: chapter 1 opens "For centuries" and never states the conclusion, so a board member reading the first three pages learns nothing about what to do. |
| Actionability and strategic insight | 15% | 3.0 | Priorities name alloy, form, region and buyers, and the tier logic is sound. Initiatives are timed but not sized, not owned and not costed. "Stop doing" is limited to diesel glow plugs and "fewer resources" for European new build chemicals. The Tier 1 bet (VIM/VAR superalloy bar and billet for aero engines) is not tested against what a EUR 400m company can afford or already has approved. |
| Writing and house style | 10% | 2.7 | Prose is clear and linked. Violations: hyphens in "Nickel- and cobalt-based", "high-performance", "addressable-market" (chapters 1 and 2), "29 18" is unreadable (alloy 29/18 or Kovar type). References have many APA defects (see fix 9). |
| Visuals and design | 10% | 3.3 | Zero figures in the main text (pdfimages finds none) although model.py already draws charts. Table 20 is broken: the first column is one word wide and the table splits across pages 23 and 24, which makes the decision table the hardest page to read. Appendices are crammed onto page 40. |

## Can I decide on Monday?

- What to invest in: partly. I know the direction (superalloy bar, billet, repair wire, powder) but not the size of
  the cheque, the capacity in tonnes, the qualification cost or the payback. "Add remelt and finishing capacity
  against signed volumes" is not a board decision.
- Where to sell: mostly yes. Engine makers and forgers in the UK, US, France and Germany, EPC contractors for India and
  Southeast Asia, implant makers in DACH and the US, clad pipe makers. The trade corridors in chapter 6 support this.
- What to stop: no. Only glow plugs are named. I cannot tell which product lines, plants, grades or customer
  segments lose capacity, people or sales coverage, or how much capacity that frees for Tier 1.

## Five questions my board would ask that the report does not answer

1. How much money, and for what? What capex (VIM, VAR, ESR, forging, finishing, powder atomiser), how many tonnes of
   added capacity, what qualification cost and over how many years does the superalloy programme need, and does it
   pass our hurdle rate in the downside case the report itself names as the test (section 8.2)?
2. How big is each prize in euros and what share is realistic for us? The report refuses an aggregate market, which is
   correct, but it gives no segment size either (for example aero engine superalloy bar and billet in Europe and the
   US in tonnes and EUR), so I cannot judge whether a 2 percent or a 10 percent share is the plan.
3. Why would Safran, MTU or Rolls-Royce qualify us against Acerinox (VDM plus Haynes, EUR 1,683m in this segment),
   ATI, Carpenter, PCC Special Metals, Aubert & Duval and Daido? What is our right to win, and what happens to our
   cash and capacity if qualification takes five years instead of three?
4. What do US tariffs, CBAM on ferroalloys and German electricity prices do to the economics? The report makes the
   United States a priority region and a German melt shop the base, yet neither trade policy nor energy cost appears.
5. What do we stop, and what does that free up? Which grades, forms, plants and customers move to harvest, how much
   revenue and capacity is affected, and what is the sequence so that automotive and European chemicals really fund
   Tier 1 as section 5.1.2 claims? And where is defence, which model.py treats as an opportunity but the report omits?

## Top ten improvements, ranked by impact

| Rank | Location | Problem | Concrete fix | Expected impact |
|---|---|---|---|---|
| 1 | Chapter 1, final paragraph (and first paragraph of chapter 2) | The answer appears only on page 22. A board reading pages 1 to 3 gets context but no conclusion, which breaks "answer first" and the 15 minute test. | Replace the generic "For centuries" opening with one paragraph and add a closing paragraph that states the answer in five sentences: where value sits (conversion and qualification), the three tiers, the Tier 1 bet, what to harvest, and the one number that matters most. No new heading needed, so the TOC stays intact. | Storyline 2.3 to 1.7, overall about 0.15 |
| 2 | 8.2, Table 21 and a new subsection 8.2.x "Investment case and gates" | Initiatives are timed but not sized, costed or owned. "Hurdle rate in the downside" is asserted without any number. | For each of the five initiatives give capex range, opex, FTE, owner (function), gate criterion with a number (for example "LTA for at least X t a year signed before furnace order"), and the earliest payback. Where internal data are missing, give team estimate ranges from competitor capex (Safran EUR 150m press, Daido JPY 36bn, Alleima VAR, Outokumpu Avesta) and label them in A4. | Actionability 3.0 to 2.0, overall about 0.15 |
| 3 | 7.1 and 7.2, Table 19, plus A2 | The data chain stops at Growth. No segment has a size, so indices cannot be turned into tonnes or EUR, and there is no portfolio level growth rate. | Add segment sizes where comparable data exist (Comtrade HS 7505 to 7507 values, Acerinox HPA 83 kt and EUR 1,683m, Cobalt Institute 20 kt superalloy cobalt) as labelled team estimates, and show an illustrative mix weighted company index under stated weights. Explain how each growth rate is derived from its anchor, not only which anchor it has. | Model 3.0 to 2.3, overall about 0.15 |
| 4 | 8.1, Table 20 | Eight criteria rated H/M/L with no weights, no score and "Fit = H" for almost every row without internal evidence. The table is also visually broken across two pages. | Show 1 to 5 scores with the weights already in model.py, a weighted total and a ranking, rebuild the table with a wide first column on one page, and mark fit ratings as "to be validated" where approvals are unknown. Optionally a 2x2 attractiveness versus ability to win chart. | Model and Visuals, overall about 0.1 |
| 5 | 8.1 and 8.2, new subsection "What we stop" | "Stop doing" is one bullet (glow plugs). The board needs explicit trade offs. | Add a harvest and exit list: products, grades, forms and customer segments, the share of capacity or sales coverage they absorb, the timing and the sequence by which freed melt and rolling hours move to Tier 1. Link to Table 4, Table 12 and Table 20 "Harvest". | Actionability, overall about 0.1 |
| 6 | 8.2 risk paragraph and 5.4.2 | Risks are listed as "known and manageable", which is not honest for the biggest bet. Qualification failure, competitor response, cyclicality of aerospace (2020) and CMC substitution timing are not quantified. | Turn the paragraph into a risk table: risk, probability, impact on Tier 1 cash, early warning indicator, mitigation, owner. Include "qualification takes 5 years", "Acerinox or ATI adds capacity", "aero downturn like 2020" and a kill criterion. | Actionability and Storyline, overall about 0.1 |
| 7 | Chapter 6 (new subsection 6.x) and Table 2 | Trade chapter ignores policy: US Section 232 tariffs, EU CBAM (which covers ferrochrome, ferronickel and ferromanganese imports), Chinese export licences on tungsten and molybdenum items are only in 4.6. German energy cost is absent. | Add a short "Trade policy and cost position" subsection with Comtrade or official tariff sources, and one sentence per priority region on landed cost impact. Add an electricity price comparison (Eurostat nrg_pc_205 versus US EIA) as a cost risk to the melt base. | Research and Storyline, overall about 0.1 |
| 8 | Whole main text | No charts at all, although model.py already draws scenario, scorecard and matrix charts. | Insert four to six figures with message titles and sources: supply concentration by metal, nickel mill product trade by country, scenario fan by industry, opportunity matrix, roadmap Gantt. Keep within 30 pages by cutting Table 2 text. | Visuals 3.3 to 2.0, overall about 0.1 |
| 9 | References and in text citations | Duplicate entries for the same document under different authors (Acerinox 2026c and Acerinox, S.A. 2026d; ATI and ATI Inc.; Alleima and Alleima AB; Garrett Motion and Garrett Motion Inc.; GE Aerospace twice with year only), one document split into a to g (Cobalt Institute, IEA 2025h to l, USGS o and p), malformed "https://doi.org/https://" URLs, Safran (2026a) points to a GE SEC filing, "ATI quotes lead times of about 20 months" is cited to Osaka Titanium (4.5), "United Nations, 2026" versus "United Nations Statistics Division", and uncited entries (ASTM, NASA, Eberspaecher, electrive, Energy Institute, KHIDI, MHLW, China Federation). | Merge to one entry per document, cite page or table instead of letters, fix the URL prefixes, correct the Safran and ATI citations, and drop uncited sources except the REF_* rows the team requires. | Writing 2.7 to 2.0, overall about 0.07 |
| 10 | 5.4, 5.6, 8.1 and model.py cell A3 | Defence is reduced to one SIPRI line, yet European rearmament (naval propulsion, armour, missile and rocket engines) is a German home market opportunity that model.py already scores. Spotlight facts are thin in automotive and oil and gas compared with energy and aerospace. | Add one defence paragraph in 5.4 with a named programme, buyer, alloy and form, and make each sector carry three spotlight facts with who, what, where, when, metal, form and likely suppliers as CLAUDE.md requires. Decide in Table 20 whether defence is Tier 1, 2 or 3. | Research and Actionability, overall about 0.05 |

## Smaller points

- Chapter 2 names "Münvest" as the client while the rest says "the company". Keep the draft's wording but make sure the
  board can see that Münvest is the commissioning partner, not a producer, or the report reads as if it advises the wrong firm.
- 4.1 and 6.1 both state the USD 32,500 per tonne unit value with the same argument. Keep it once and use the space for policy.
- Table 2: molybdenum shows "China" without a share, while every other row has one.
- 5.6.2 "expansion alloys 42 and 29 18" should read FeNi42 and FeNiCo 29/18 or a named grade.
- A1 to A4 fit on one page. A4 is the most useful page for my CFO and should list each missing internal datum against the decision it unlocks.

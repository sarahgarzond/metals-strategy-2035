# Round 4 industry grader review (strategy VP, global high performance alloys group)

Reviewer profile: 20 years in nickel alloys and specialty stainless (VIM, VAR, ESR, rolling, alloy surcharge, AMS, ASME, NADCAP, RCC-M qualification, competitor landscape).
Object: reviews/round_4/report_v4.txt (main text p. 1 to 30, references p. 30 to 44, appendices A1 to A8 p. 44 to 58), sections/*.md, research/model/outlook_results.md, reviews/research_audit.md (all 19 notes PASS), research/companies/*.md, checked against CLAUDE.md, data/toc.json and my round 3 review. Read only, nothing in the report was edited.

## Overall grade: 2.0 (up from 2.3)

| Criterion | Weight | Grade | Reason in one line |
|---|---|---|---|
| Research depth and source quality | 25% | 2.3 | USGS MCS 2026, IEA, Pink Sheet, Comtrade incl. mirror flows, PRODCOM, OECD, Cobalt Institute and 61 filings drive the numbers, but the only alloy market size is still two paid reports and research notes hold tonnage and price facts (China superalloy 64.5 kt, Special Metals base price notices) that never reach the report |
| Model transparency and reproducibility | 20% | 2.0 | Formulas, seed, distributions, parameter table, backtest and calibration are fully documented and reproducible, but the backtest correction is mislabelled and pushes energy and oil and gas up, the aerospace band is implausibly narrow and the FeNi family is still built from the wrong industry index |
| Storyline from data to strategy | 20% | 2.0 | Answer first, metal first chain, stage ladder respected, tier 1 and tier 2 never mixed, chapter 8 cites Tables 13 and 14 |
| Actionability and strategic insight | 15% | 2.3 | Perspective stated, competition scores corrected, named buyers, gates and kill criteria, but priority 1 includes a weakly evidenced FeNi niche, initiatives are unsized and the producer landscape lacks Japan, China and the input monopolies |
| Writing and house style | 10% | 2.0 | House style clean, but several round 3 reference defects remain (CMOC, Safran 2026a, SEMI, Infineon, Westinghouse) and "Münvest" appears twice on the title page |
| Visuals and design | 10% | 2.0 | Figure 3 small multiples with P10 to P90 bands are board quality, tables consistent, Table 16 abbreviations now explained |

Weighted: 0.575 + 0.40 + 0.40 + 0.345 + 0.20 + 0.20 = 2.12, graded 2.0.

The round 4 report is the first version I would show to a strategy team without apologising for it. The Table 10 values are now defensible, the medical specifications are right, the opportunity matrix has a stated perspective, and the two tier outlook is the most transparent model I have seen in a student study. What still separates it from a board document is that (a) the market is never expressed in tonnes, (b) one of the three priority 1 positions rests on an index that does not measure the product, and (c) the producer landscape stops at the Western listed peers.

## 1. Research depth (explicit judgement)

Built from structured databases and filings (good):
* Supply side: USGS MCS 2026, IEA Critical Minerals Outlook, INSG, Cobalt Institute, IMOA, ICSG, ITIA, World Bank Pink Sheet. Stage labels are correct throughout (contained, gross weight, sponge, ferrochrome kept apart, p. 6 to 12).
* Trade: Table 11 now adds mirror flows (Canada 1,236, Norway 1,086, Russia 1,049, Australia 981 USD m) and the HS 75 coverage caveat (p. 22 to 24). Round 3 fix 8 applied.
* Table 10 now values EU apparent consumption at extra EU unit values with the contained nickel check row, and A3 shows the arithmetic (p. 22 to 23, p. 52). Round 3 fix 1 applied.
* Model drivers: IEA WEI and WEO, OECD Health, Eurostat C29, OECD STAN, Siemens Energy, Airbus GMF and GSF, SEMI, all logged with IDs in research/model/outlook_results.md.

Borrowed or unused:
* Chapter 1 (p. 3) still sizes the segment only with IMARC and The Insight Partners (USD 10 to 14 bn). Round 3 gap 1 (contained metal tonnage triangulation) was not applied.
* research/companies/fushun.md holds "China produced about 64,500 tonnes of superalloy in 2025 against demand near 66,000 tonnes" (CO_BAOWU_CHINA_SUPERALLOY_2025), and research/companies/special-metals.md lists Huntington base price increases of 5 to 20 percent from 2021 to 2024. Both are exactly the tonnage and base price evidence a board wants, and neither is in the report.
* GE Vernova and Mitsubishi Power are flagged as "not profiled" in research/sectors/energy_environment.md line 236, so the world gas turbine driver is one OEM.
* Proterial, the key FeNi foil incumbent, is a TODO(data) profile (research/companies/proterial.md), yet FeNi foil is priority 1.

Verdict: supply, trade and company facts are database driven and current. The Market size link is still not expressed at the alloy melt stage, and two of the top three opportunities lack a census of competitors.

## 2. Status of my round 3 fixes

| Round 3 fix | Status in round 4 | Evidence |
|---|---|---|
| 1 Table 10 values | Applied | Table 10 p. 22, A3 p. 52 |
| 2 Medical specs F75, F1537, F3213, F2384 | Applied, well | 5.7.2 p. 21, Table 9 |
| 3 FeNi index from wrong industry | Half applied | weights changed, but FeNi still driven by fab equipment and an unmeasured EV index (fix 1 below) |
| 4 Oil and gas geography and forms | Partly applied | ISO 15156 corrected, Middle East named, OCTG, API 6ACRA bar, NO96 Invar missing (fix 8) |
| 5 Triple melt, OEM specs, time to approval | Partly applied | 5.4.2 now has VIM, ESR, VAR, melt route freeze, PM issue; Table A13 still "Years per part family" (fix 9) |
| 6 Matrix perspective, Comp and Diff | Applied | A2.5 p. 50, Comp 2 for billet and remelt, powder 2.95 Monitor |
| 7 Producers and input monopolies | Not applied | zero hits for Proterial, CBMM, Delachaux, AMG, VSMPO, GE Vernova, Mitsubishi, Cannon-Muskegon, Böhler, Fushun, Gaona, Baowu |
| 8 Mirror trade and HS coverage | Applied | Table 11, 6.1 |
| 9 Conversion premium on alloy content, surcharge | Not applied | "twice the price of the contained metal" p. 8 and p. 24, one mention of "surcharge" in the whole report |
| 10 References and small items | Partly applied | United Nations author merged, comma fixed, 59 type wording fixed; CMOC, Safran 2026a, SEMI, Infineon, Westinghouse unchanged |

## 3. Errors with corrections (ranked fixes, located)

### Fix 1. FeNi priority 1 rests on an index that does not measure FeNi (sections/07_scenarios.md Table 14, sections/08_recommendations.md Table 16 row 3 and 8.1 paragraph 1, sections/11_appendices.md Table A1 "Precision FeNi strip and foil")
* Statement: "Precision FeNi strip and foil, Electronics 0.60, electric vehicles 0.30 ... 134 157 185", "FeNi36 mask foil for DNP and BOE in East Asia completes priority 1 with a P50 of 157".
* Problem: the electronics index is itself 60 percent SEMI 300 mm fab capacity (Table A1, weights 0.6 and 0.4), and fab tools use UHP 316L and C-22 type tube and valve stock, not Invar. So roughly a third of the FeNi family is driven by fab capex. A further 0.30 weight sits on the EV parts index at 192, for which outlook_results.md says "No kilogram per vehicle is published", and where FeNi competes with electrical steel, FeCo (Hiperco, Vacoflux), ferrite and nanocrystalline cores (VAC Vitroperm, Proterial Finemet). Traction motors do not use FeNi. OLED masks, the stated reason for the priority, have no driver at all. The incumbents are not named: Proterial (Yasugi) for rolled Invar foil to mask makers and Aperam Imphy for Invar strip (Imphy appears only as a capex benchmark in Table 17), plus Chinese foil entrants. Maskless routes (Visionox ViP, TCL CSOT inkjet) are noted but not in the index. The global FMM market is about USD 370 m at the mask stage on one paid report (research/companies/proterial.md), so a Market score of 3 for the foil is generous.
* Correction: build the FeNi index from its own drivers (FMM based OLED substrate capacity, Gen 8.6 IT lines at Samsung Display A6, BOE B16 and others, mask consumption per substrate, share of FMM versus maskless), give the foil tonnage or TODO(data), split "FeNi36 foil" from "soft magnetic FeNi strip", and name Proterial, Aperam Imphy and VAC as incumbents. Expect FeNi foil to fall into priority 2 or to a gated option, which leaves priority 1 to the two vacuum melted superalloy rows and makes the chapter 8 story cleaner. Impact: Model +0.2, Actionability +0.3.

### Fix 2. The backtest correction is mislabelled and inflates energy and oil and gas (sections/03_framework_and_methodology.md line 18, sections/07_scenarios.md 7.1 paragraph 2, sections/11_appendices.md A2.3)
* Statement: chapter 3 says the model is "corrected for the past optimism of official outlooks". A2.3: shift "plus 1.0 percentage point a year for energy and for oil and gas", because a log linear 2015 to 2019 trend underestimated gas power investment (growth error minus 20.68 pp a year).
* Problem: (a) no official outlook is backtested except a one year WEI vintage, so the label is wrong, and the correction raises rather than lowers the forecast. (b) The error comes from a naive trend, but it is applied to drivers that are not trends: Siemens Energy capacity guidance (energy) and an IEA scenario ratio (oil and gas). The gas turbine boom is then counted twice, once in the 17 to 30 GW path and once in the +1 pp shift, lifting energy P50 from 142 to 156 and making turbine remelt the top opportunity. (c) The industry precedent for a turbine backlog is the 2001 to 2003 US gas turbine bubble and its order collapse, not 2015 to 2019. (d) Aerospace gets no haircut and a P10 to P90 band of 137 to 158 (sd 0.16 pp), although OEM rate plans have been missed repeatedly (A320 rate 75 deferred, 737 capped by the FAA, LEAP deliveries below earlier guidance). The narrowest band in the model belongs to the industry with the worst plan reliability. (e) The energy driver is one OEM, while GE Vernova and Mitsubishi Power are the other two heavy duty OEMs and both announced ramps (research/sectors/energy_environment.md line 236).
* Correction: rename the step "trend backtest", show Table 13 with and without the shift side by side, backtest OEM delivery guidance against actual deliveries and IEA WEO vintages against outcomes and apply that bias, widen the aerospace band accordingly, and replace the Siemens Energy proxy by the sum of the three OEMs' announced capacity. Show that turbine remelt stays priority 1 without the shift (it does: Gro 4 gives 3.85). Impact: Model +0.3.

### Fix 3. Still no tonnes (chapter 1 paragraph 3, 6.1, 7.1, Table 13)
* Statement: segment "between about USD 10 billion and USD 14 billion" from IMARC and The Insight Partners, everything else is an index.
* Problem: a board thinks in kt of melt and EUR per tonne of base price. Round 3 gap 1 was not applied, while the evidence is in the repository: Cobalt Institute 20.0 kt cobalt in superalloys, China 64.5 kt superalloy output in 2025 (research/companies/fushun.md), ATI Monroe VIM about 9 kt a year, INSG first use shares, EU apparent consumption 57.8 kt flat and 9.2 kt tube.
* Correction: add a one table triangulation in 6.1 or 7.1: nickel in non ferrous alloys from INSG first use divided by average nickel content, superalloy cobalt divided by a documented average cobalt content, China 64.5 kt as a regional check, all labelled team estimate, then state Table 14 families in kt in 2025 and P50 kt in 2035. Keep the paid reports only as triangulation. Impact: Research +0.3, Model +0.2.

### Fix 4. Producer structure and input monopolies still missing (4.1 paragraph 1, 4.3 paragraph 2, 4.5, 4.7.5, 5.3.1, 8.1 paragraph 1, Table A12, Table A14 row 3)
* 4.3: "A single qualified source of this small input can therefore halt a vacuum melt shop" names nobody. Name the aluminothermic chromium metal producers (Delachaux in France, AMG Chrome in the UK).
* 4.7.5: Alloy 718 "contains about 5 percent niobium", but vacuum grade NiNb comes almost entirely from CBMM in Brazil, a sharper single source than anything in Table 2. Supply security 3 for engine billet should cite it.
* 4.5: VSMPO-AVISMA and the Western exit from Russian titanium after 2022 explain the aircraft grade shortage. Toho Titanium and UKTMP belong next to Osaka.
* 4.1: the class 1 list is outdated in one direction: several Chinese class 1 brands have been registered on the LME since 2023 (verify the list), so class 1 tightness of 2022 is gone and the real constraint is vacuum melt qualified feed (briquette, cathode, revert).
* 8.1 and A12: LTA holders list ATI, PCC, Carpenter, Aubert & Duval and Daido, but omit Proterial, voestalpine Böhler, Doncasters, Kobe Steel and IHI (Japan Aero Forge) and the Chinese producers (Fushun, CISRI Gaona, Baowu Special Metallurgy) that hold AECC and COMAC approvals. Aperam's 2025 acquisition of Universal Stainless changes the US premium melt map. Table A14 "New Asian superalloy capacity" has no tonnes, while 64.5 kt China output is in the research notes.
* Add one sentence that the benchmark omits one major European producer by design, so experts do not read it as an oversight.
* Impact: Research +0.2, Actionability +0.1.

### Fix 5. Additive and powder are filed as emerging although they are established (sections/05_4_aerospace.md Table 6 row 3, sections/07_scenarios.md Table 15 row 3, Table 16 "Additive engine powder", data/clean/model_tier2_register.csv)
* Statement: "Additively manufactured combustor and nozzle parts, superalloy powder", tier 2, "TRL 7 to 9 ... Earliest volume 2027".
* Problem: the LEAP fuel nozzle tip is printed in CoCr, not nickel superalloy, and has been in serial production since the LEAP entered service in 2016, so this is TRL 9 with measured volume. Powder metallurgy discs (René 88DT, René 104, ME3, Pratt and Whitney's in house powder) have been in production for decades, and the 2023 GTF issue was contamination in that existing route. The register mixes a captive, established PM disc powder route with a crowded AM powder market (Carpenter Additive, Höganäs, Sandvik Osprey, Oerlikon, Colibrium Additive, ATI, Chinese PREP producers).
* Correction: split into "PM disc powder (established, captive, tier 1 inside superalloy billet)" and "AM powder, CoCr and nickel superalloy (measured, crowded, Comp 2)", correct Table 6 to "CoCr and nickel superalloy powder", and keep only genuinely new AM hot section parts in the register. Impact: credibility with any aerospace reader, Research +0.1.

### Fix 6. Conversion premium and surcharge still not explained (sections/04_1_nickel.md last paragraph, sections/06_trade.md 6.2 paragraph after Table 11)
* Statement: "about USD 32,500 per tonne or twice the price of the contained metal".
* Problem: a tonne of alloy is not a tonne of nickel. With the report's own prices, C-276 (about 57 percent Ni, 16 percent Mo, 15.5 percent Cr, 4 percent W) carries roughly USD 8,600 of nickel, USD 8,200 of molybdenum and USD 2,000 of chromium before tungsten, so its raw material value is near USD 19,000 to 20,000 per t and the premium on a USD 32,500 unit value is about 1.6 to 1.7 times, not 2. HS 7506 also includes pure nickel strip, where the ratio is near 2. The argument "buyers pay for qualification" is right but must be shown on alloy content. The report also never explains the alloy surcharge (monthly, on prior month LME nickel and molybdenum and chromium averages in Europe, lagged index clauses in aerospace LTAs, inventory timing effects in producer earnings), or that margin sits in the base price.
* Correction: add a small worked table for C-276, 625 and Nickel 201 (raw material value, unit value, conversion premium), one paragraph on surcharge versus base price, and use the Special Metals base price notices (research/companies/special-metals.md line 24) and Carpenter's "excluding surcharge" reporting as the first real product price evidence. Impact: Model +0.2, Actionability +0.1.

### Fix 7. Nuclear Alloy 690 logic is built on an integrated competitor (sections/05_3_energy_environment.md 5.3.2, Table 5 row 2, Table 16 "Alloy 690 bar and hollows", 8.1 paragraph 2)
* Statement: "Alleima has reopened a Sandviken tube mill for steam generator tube, which places alloy producers as suppliers to tube makers".
* Problem: Alleima melts its own 690 at Sandviken, so its tube mill does not create a market for outside bar or hollows. Most other steam generator tube makers (Valinox Nucléaire at Montbard, Nippon Steel, Chinese producers inside national programmes) are integrated or captive. Approvals are RCC-M M4105 or ASME SB-163 with 10 CFR 50 Appendix B and NQA-1, per programme.
* Correction: verify which tube makers buy hollows, otherwise reframe the row as 690 forgings and 52M or 152 type weld filler for steam generators, and lower Mkt or Cust. Impact: Actionability +0.1.

### Fix 8. Oil and gas product forms incomplete (sections/05_2_oil_and_gas.md 5.2.2 and Table 4)
* Missing: CRA OCTG (13Cr, super 13Cr, 25Cr duplex, Alloy 028, G3 and 2550 type for sour wells, from Tenaris, Vallourec, Nippon Steel, JFE), Alloy 718, 925 and 725 bar to API 6ACRA (only in Table A13), and the LNG split: Invar strip only for GTT NO96 membranes, while most new carriers use Mark III with 304L, so FeNi36 for LNG follows the NO96 share and Aperam Imphy is the incumbent. 9 percent nickel steel plate for LNG storage tanks is the volume nickel product.
* Name operators and rules: Saudi Aramco Jafurah, QatarEnergy North Field expansions, ADNOC sour gas, Petrobras pre salt, with in country value programmes (IKTVA, ICV) that decide vendor lists in the Middle East.
* Impact: Actionability +0.2.

### Fix 9. Qualification gates are still generic and break the scoring trace (sections/11_appendices.md A7 Table A13, A2.5 Table A4 row "Entry barriers")
* Problem: Table A4 scores entry barriers from "Time to approval and protection afterwards (A7)", but Table A13 gives no times ("Years per part family"). The medical row lists F75 and F1537 only, although the matrix and Table 9 rely on F3213 and F2384. "Turbine remelt stock and sheet" in Table 16 merges two different assets and customers (VIM casting stock for investment casters versus cold rolled combustor sheet for fabricators), and remelt stock for single crystal alloys needs a licence from the alloy owner (CMSX family Cannon-Muskegon, René N5 GE, PWA 1484 Pratt and Whitney).
* Correction: add a "typical time to first approval" column (aero rotating 3 to 5 years, static sheet and wire 1 to 2, IGT casting stock 1 to 2, NORSOK and operator lists 1 to 2, nuclear per programme, medical 1 to 2, each sourced or labelled team estimate), name OEM material specs (GE P and B specs, RRMS, PWA, Safran), add proprietary alloy licensing, and split the remelt and sheet row. Impact: Actionability +0.2.

### Fix 10. Roadmap benchmarks mislabelled, initiatives unsized, residual reference and compliance defects (sections/08_recommendations.md Table 17, sections/11_appendices.md Table A12, References, title page, chapter 3, data/toc.json)
* "Carpenter Athens capex USD 243 m" (Table 17) is Carpenter's total FY2026 capex, and "Athens, Alabama expansion, capex USD 355 to 375 m guided" (Table A12) is total FY2027 company guidance (research/companies/carpenter.md line 17). Label them as company capex "mainly Athens".
* Initiative 1 gate "contracts for half by 2028" has no denominator. Size each initiative in kt, EUR m capex and revenue at a stated base price, using ATI Monroe (about 9 kt a year) as the yardstick.
* References: CMOC Group 2026a and 2026b are Mining Weekly and Mining.com articles, Safran 2026a points to edrmagazine.eu, SEMI 2026a and 2026c and Infineon 2026 are Evertiq (and 2026c carries a semi.org URL with "Evertiq"), Westinghouse 2025 is a K&L Gates page. Cite the actual publisher.
* Title page shows "Münvest Project Studies" and "Münvest" under the supervisor. CLAUDE.md bans the name "anywhere in the report body", so confirm with the team whether the course title is exempt.
* Chapter 1 gives Indonesia "about 63 percent" of nickel, Table 2 "about 67%". Use one series or say which.
* Chapter 3 says "Every key figure is confirmed by a second independent source" and the model is "calibrated to reproduce published history". The calibration reproduces one 2025 point (20.0 kt cobalt). Tone both down.
* Chapter 6 uses section level headings 6.1 to 6.4 that data/toc.json does not list. Either add them to the TOC through the Google Doc or confirm the sync check accepts them.
* Impact: Writing 2.0 to 1.7, Actionability +0.1.

## 4. Gaps that keep me from forwarding this to my board
1. No tonnes at the alloy melt or mill stage (fix 3). Indices without a base are a growth story, not a market size.
2. No base price or margin per product form (fix 6). The ranking claims engine billet earns more than chemical plate, but no evidence per tonne is shown, although Carpenter segment margins (premium alloys 27.7 percent versus powder 7.9 percent) and base price notices are in the repository.
3. China on the producer side. Fushun, CISRI Gaona and Baowu, 64.5 kt of Chinese superalloy output and Chinese AECC and COMAC approvals are the main long term price risk for European plate and bar, yet China appears only as a raw material and policy actor.
4. Region in 7.2 is still one paragraph. A regional split of the aerospace and energy indices by engine and turbine assembly country (Comtrade 8411, OEM plant lists) would make the heading true.

## 5. Top ten improvements ranked by impact
1. Rebuild the FeNi family from OLED mask and sensor drivers, name Proterial, Aperam Imphy and VAC, and re rank FeNi (fix 1). Model +0.2, Actionability +0.3.
2. Relabel and rework the backtest correction, show results with and without it, haircut aerospace for OEM plan misses, use three turbine OEMs (fix 2). Model +0.3.
3. Add the contained metal tonnage triangulation and express product families in kt (fix 3). Research +0.3, Model +0.2.
4. Add the input monopolies (CBMM, Delachaux, AMG, VSMPO) and the Japanese and Chinese producers to chapter 4, 8.1 and A6 (fix 4). Research +0.2.
5. Move PM disc powder and the CoCr LEAP nozzle out of the emerging register and correct Table 6 (fix 5). Research +0.1.
6. Show the conversion premium on alloy content and explain surcharge versus base price with the Special Metals and Carpenter evidence (fix 6). Model +0.2.
7. Add time to first approval, OEM specs, alloy licences and split remelt from sheet in A7 and Table 16 (fix 9). Actionability +0.2.
8. Complete oil and gas forms (CRA OCTG, API 6ACRA bar, NO96 versus Mark III, operators and in country value rules) (fix 8). Actionability +0.2.
9. Re examine the Alloy 690 opportunity against integrated tube makers (fix 7). Actionability +0.1.
10. Correct the Carpenter capex labels, size the initiatives, fix the remaining references and the title page name check (fix 10). Writing +0.3.

With fixes 1 to 6 the report reaches about 1.7, with all ten about 1.3.

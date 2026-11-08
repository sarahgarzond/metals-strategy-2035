# Round 5 industry grader review (strategy VP, global high performance alloys group)

Reviewer profile: 20 years in nickel alloys and specialty stainless (VIM, VAR, ESR, rolling, alloy surcharge, AMS, ASME, NADCAP, RCC-M, competitor landscape).
Object: reviews/round_5/report_v5.txt (main text p. 1 to 30, references p. 31 to 41, appendices p. 42 to 60), sections/*.md, research/model/outlook_results.md, reviews/research_audit.md (19 of 19 notes PASS), data/sources.csv and research/companies/*.md, read against CLAUDE.md, data/toc.json and my round 4 review. I edited nothing in the report.
Out of scope by user decision: the title page, cover, TOC and the opening of chapter 1 (not flagged). Section titles are frozen, so every fix below works inside them.

## Overall grade: 1.7 (up from 2.0)

| Criterion | Weight | Grade | Reason in one line |
|---|---|---|---|
| Research depth and source quality | 25% | 2.0 | USGS MCS 2026, IEA, INSG, Cobalt Institute, PRODCOM, Comtrade with mirror flows and 61 filings drive the numbers. But the HS 6 digit alloy split is unused, the China 64.5 kt cross check comes from a Chinese market report (Zhiyan), and Chinese producers and two of the three heavy duty turbine OEMs are absent |
| Model transparency and reproducibility | 20% | 1.7 | The trend shift is dropped, results are shown with and without the haircut, the FeNi family is rebuilt and kt per family are documented. Remaining issues: the haircut tests are thin and partly mislabelled, and stock drivers (fab capacity, nuclear fleet) stand in for flow demand |
| Storyline from data to strategy | 20% | 1.7 | Answer first, one priority 1, an honest note that the ranking is fragile, a stop list. But the headline ranks industries by index, so electronics (tonnes) leads aerospace (about 130 kt of melt) |
| Actionability and strategic insight | 15% | 2.0 | Initiatives are gated in kt and dated. But the bottleneck is set at VIM rather than at remelt and billet conversion, single crystal alloy licences and captive casting (GE and CPP) are missing, and oil and gas is still generic |
| Writing and house style | 10% | 2.0 | House style is clean. Five round 3 and 4 reference defects remain, and one Carpenter figure appears on two different bases |
| Visuals and design | 10% | 1.7 | Figure 3 and Tables 13 to 17 are board quality. Table 14 needs one column with kt per index point |

Weighted: 0.50 + 0.34 + 0.34 + 0.30 + 0.20 + 0.17 = 1.85. The raw score sits exactly between 1.7 and 2.0. I grade 1.7 because round 5 fixed the three structural problems I raised in round 4 (FeNi, backtest, tonnes), and what remains is local.

This is now a document I would forward to my strategy team as a working basis. I would not yet forward it to the board, for four reasons. First, the board will read Table 13 as "electronics is the best market". Second, the competitor set stops at Western listed companies, with no Chinese melters at all. Third, the energy leg rests on Siemens Energy alone. Fourth, the priority 1 position contradicts the report's own supply security rule (fix 2).

## 1. Research depth (explicit judgement)

Built from structured databases and filings (good):
* Supply: USGS MCS 2026 for all ten metals, IEA Global Critical Minerals Outlook, INSG (3.875 Mt production, 3.577 Mt usage, LME Chinese share), Cobalt Institute (20.0 kt superalloy cobalt, 11,499 t aviation cobalt), IMOA, ICDA, ITIA, ICSG. The stage ladder is respected throughout (p. 6 to 12, A1).
* Trade: Comtrade reporter and mirror data (Table 11), the German 7505 to 7507 time series (Figure 2), PRODCOM apparent consumption valued at extra EU unit values (Table 10, A3 arithmetic).
* Prices and margins: the conversion premium is now computed on alloy content (C-276, p. 8). The surcharge mechanism is shown from ATI and Carpenter filings, and Special Metals' eight base price increases are used (p. 8). This is round 4 fix 6, applied well.
* Model: Cobalt Institute calibration, IEA WEI and WEO, OECD, Eurostat, SEMI, Airbus GMF and GSF, Boeing CMO, Garrett and BorgWarner filings. All parameters appear in Table A1.

Borrowed or weak:
* China's superalloy output of 64.5 kt (A2.4, Table A14) comes from Zhiyan Consulting (data/sources.csv row CO_BAOWU_CHINA_SUPERALLOY_2025, type market_report, confidence low, note "2021 broker view"). The report cites it without saying that it is a market report. The CLAUDE.md rule allows that for triangulation only, so label it.
* Chapter 1 still sizes the segment from IMARC and The Insight Partners. That is allowed because it sits in the fixed opening, but the report never sets Table 14 against those figures. One sentence in 7.2 would close the loop.
* Unused structured data that would answer the report's own main limitation: HS 6 digit separates pure nickel from nickel alloys (750511 and 750512 bars, 750521 and 750522 wire, 750610 and 750620 flat, 750711 and 750712 tube). Eurostat Comext CN8 does the same. A4 says "official statistics ... mix pure nickel with nickel alloys", which is wrong at HS 6 (fix 4).
* USGS Minerals Yearbook end use tables (nickel and cobalt reported consumption in superalloys, United States) are not used. They would give a second, primary triangulation for the 193 kt superalloy family.

Verdict: research depth is database led and current. Market size at the mill stage is now stated in kt, but as a range of plus or minus 45 percent built mainly from assumptions. The two cheapest improvements are the HS 6 alloy split and the USGS yearbook end use tables.

## 2. Status of my round 4 fixes

| Round 4 fix | Status in round 5 | Evidence |
|---|---|---|
| 1 FeNi index and priority | Applied | Rebuilt on OLED mask, EV sensor and FeNi42 drivers (A2.4). The 157 to 129 drop is shown, FeNi is now a gated Option, and DNP, Visionox and TCL CSOT are named. Proterial and VAC are still not named as foil and soft magnetic incumbents (only Imphy, Table 18) |
| 2 Backtest mislabel, double count, aerospace band, three OEMs | Mostly applied | Trend shift dropped (7.1, A2.3), with and without columns in Table 13, aerospace band now 121 to 147. Energy still follows one OEM (A4 admits it). The haircut tests are thin (fix 3) |
| 3 Tonnes | Applied in method, weak in triangulation | Table 14 kt per family, A2.4 arithmetic. No INSG nickel or USGS yearbook triangulation, and no HS 6 alloy split |
| 4 Producers and input monopolies | Half applied | AMG Chrome, CBMM, VSMPO-AVISMA, Böhler, Proterial and Aperam with Universal Stainless added. Still absent: Fushun, CISRI Gaona, Baowu Special Metallurgy, Western Superconducting, Toho, UKTMP, Doncasters, IHI and Japan Aeroforge, Cannon-Muskegon, Delachaux |
| 5 PM and AM powder | Mostly applied | A3 note on captive PM disc powder, AM powder now a measured row (Table 17). Table 6 row 3 still reads "superalloy powder" for nozzles, although the LEAP fuel nozzle tip is CoCr |
| 6 Conversion premium and surcharge | Applied | p. 8, A2.4 (USD 10 per t per point per USD 1,000) |
| 7 Alloy 690 against integrated tube makers | Applied | 5.3.2, Table 5 "mostly from integrated mills", Market 2 "upper bound" (8.1). The 52M and 152 filler and forgings reframe is not added |
| 8 Oil and gas forms, NO96, operators | Not applied | Zero hits for Tenaris, Vallourec, NO96, Mark III, Jafurah, North Field. API 6ACRA only in A7 |
| 9 Approval times, OEM specs, licences, split remelt and sheet | Partly applied | A13 now says honestly that no times are published except ATI and Boeing. Medical row still lists only F75 and F1537, no alloy licence, remelt and sheet still merged |
| 10 Capex labels, sizing, references | Partly applied | Carpenter capex relabelled "company capex, mainly Athens", initiative 1 sized at 1.5 kt. References: CMOC, Safran 2026a, SEMI 2026a and 2026c, Infineon and Westinghouse 2025 unchanged |

## 3. Errors with corrections (ranked fixes, located)

### Fix 1. The headline ranks industries by index growth, so tonnes and value are inverted (chapter 2 paragraph 3, 7.2 opening sentence and Figure 3 title, chapter 9 paragraph 2)
* Statement: "P50 indices of 141 in electronics and 136 in medical technology, with aerospace at 134 and energy technology at 133 close behind". Figure 3 is titled "Electronics and medical technology lead alloy demand to 2035".
* Problem: an index without a base is a growth rate, not a market. The report itself says electronics alloys are "measured in tonnes" (5.6 opening sentence) and that FeNi foil is "not estimable", while the aviation superalloy melt behind 11,499 t of cobalt is about 130 kt (outlook_results.md memo row). A board member reads "electronics leads" and asks why priority 1 is aerospace. In addition, 60 percent of the electronics index is SEMI 300 mm capacity, a stock. Fab gas system tube follows capacity additions and equipment spending (a flow) plus maintenance, so a capacity index is the wrong shape (see fix 6).
* Correction: lead chapter 2, 7.2 and chapter 9 with the volume weighted message, for example "aerospace and gas turbines add the most tonnes (superalloy family 193 to 247 kt P50), electronics and medical grow fastest from a small base". Retitle Figure 3, add a Table 13 column "2025 base, kt or t Co, or not estimable", and order the table by absolute increment where a base exists. Impact: Storyline +0.3. This is the cheapest board level fix in the report.

### Fix 2. Priority 1 breaks the report's own supply security rule, and niobium is missing from the score (8.1 paragraph 2, Table 17 row 1, Table A4 "Supply security", 4.7.5)
* Statement: "triple melt Alloy 718 and 720Li billet is mostly surplus nickel with cobalt as a minor element", Sup = 3.
* Problem: 720Li contains about 15 percent cobalt (Waspaloy about 13 percent, René 65 about 13 percent). Table A4 scores "cobalt above 10% under the quota" as 2. Alloy 718 has essentially no cobalt but about 5 percent niobium, and 4.7.5 itself says Brazil mines about 93 percent and CBMM sells the vacuum grade NiNb. That single source concentration is sharper than the Congo quota for 718, and the scoring rule has no row for it. With Sup = 2, engine bar falls from 3.80 to 3.65 and to priority 2, the same move as the Congo shock in Table 15.
* Correction: either score 718 and 720Li separately (718: Ni, Cr, Fe, Nb, with a niobium single source row added to A4, 720Li: Sup 2) or name the lead grade and justify Sup 3 explicitly. State in 8.1 that the only priority 1 is a 718 position. Then say whether priority 1 survives. If it does not, say so plainly: "no position clears priority 1 on all criteria, engine and turbine superalloy share the top of priority 2". A transparent tie is more credible to an industry reader than a 0.05 margin that the team's own rule removes. Impact: Model +0.1, Actionability +0.2, credibility with any metallurgist.

### Fix 3. The optimism haircut tests are thin, partly mislabelled and applied across domains (7.1 paragraph 2, Table 12, Table A2 last three rows, Table A1 "Haircut" rows)
* Statement: "Boeing built 42 instead of 47 aircraft a month on the 737 (0.894)", Table A2 test year 2025. Energy, oil and gas and automotive haircut 0.95 "Derived, IEA 0.951".
* Problems:
  (a) outlook_results.md records the test as "plan of 47 a month in 2026 versus 42 a month reached in Q4 2025", so a 2026 plan is set against a 2025 outcome. That is not a plan against outcome test. The year label is wrong and the ratio partly measures timing.
  (b) The energy haircut is an IEA upstream investment vintage. It says nothing about turbine OEM capacity guidance, which is the driver it is applied to. The industry precedents are the 2001 to 2003 US gas turbine order collapse and the 2017 to 2019 heavy duty slump, when GE Power's market forecasts were missed by a wide margin.
  (c) A one year rate shortfall is applied as a permanent 2035 level cut of 8 percent. That may be right, but say why it is a level and not a delay.
  (d) The energy driver is still Siemens Energy only, while GE Vernova (largest heavy duty share) and Mitsubishi Power both announced capacity ramps.
* Correction: relabel the Boeing test and add two genuine vintage tests from public documents, for example Airbus GMF or Boeing CMO delivery paths of 2018 and 2019 against 2023 to 2025 actuals, and GE or Siemens gas turbine market forecasts of 2017 against outcomes. Sum the announced heavy duty capacity of the three OEMs for the energy driver, or widen the band and say "one OEM, cyclical history". Model the gas turbine aftermarket (hot gas path parts on the installed fleet) as a second component. It is a large share of IGT superalloy use and is far more stable than new units. Impact: Model +0.2.

### Fix 4. Use HS 6 digit to split alloy from pure nickel, and correct A4 (6.1, Table 10 footnote, Table 11, A2.4 "Bar, rod and wire", A4 sentence 2)
* Statement: "The codes cover only alloys in which nickel predominates", "HS 7505 exports ... includes pure nickel", and A4 "Official statistics ... mix pure nickel with nickel alloys ... customs data at the eight digit level would sharpen these estimates".
* Problem: HS 2022 already separates them at 6 digits (750511 not alloyed and 750512 alloys, 750521 and 750522, 750610 and 750620, 750711 and 750712), and Comtrade reports at that level. Eurostat Comext CN8 does too. That gives alloy only tonnage, unit values and corridors with the tools already in the repository. It also fixes the C-276 premium argument, because the German 7506 unit value of USD 32,500 per t mixes Nickel 201 strip with alloys.
* Correction: pull 750512, 750522, 750620 and 750712 for the ten reporters 2019 to 2024, report alloy only unit values beside Table 11, replace the "traded floor includes pure nickel" assumption in A2.4, and correct the A4 sentence. Impact: Research +0.2, Model +0.1.

### Fix 5. The competitor map still stops at Western listed companies (5.4.2 paragraph 3, 8.1, Table A12, Table A14 row 4)
* Missing on the melt side: Fushun Special Steel, CISRI Gaona, Baowu Special Metallurgy, Western Superconducting, Jiangsu Longda and Sichuan Liuhe hold AECC and COMAC approvals and are the long term price risk to Western plate and bar. They appear in research/companies (outlook_results.md cites "Fushun, Western Superconducting and Baowu profiles") but not in the report, although Table A14 uses their 64.5 kt.
* Missing among Japanese producers: Daido and Nippon Yakin are only in the benchmark. Proterial is not named as the FeNi36 foil incumbent (the research notes say Yasugi). IHI and Japan Aeroforge are absent.
* Missing among casting houses and alloy licences: Cannon-Muskegon (PCC) for CMSX casting stock, and the fact that single crystal remelt stock (CMSX family, René N5, PWA 1484) is supplied under the alloy owner's licence.
* Howmet sits in the peer benchmark (Table A12) but is a caster and forger, so a customer. Separate peers (melters) from customers (casters, forgers).
* Correction: add a short "who melts what" paragraph in 5.4.2 or 8.1 and a Chinese and Japanese block in Table A12 (revenue where filed, otherwise named only). Impact: Research +0.2, Actionability +0.1.

### Fix 6. Stock drivers used for flow demand (Table 12 Electronics and Energy rows, Table A1 "Realisation of SEMI path", "Nuclear fleet and tube ratio")
* Problem: alloy demand for fab gas systems and for steam generator tube follows new fab and reactor construction, plus replacement (steam generator replacement campaigns, chamber part wear), not the installed base. A capacity index that grows 3 percent a year means roughly flat construction, and so flat alloy demand. The nuclear "fleet and tube ratio" 1.05 to 1.45 likewise follows the fleet, not new build plus SG replacement.
* Correction: drive electronics equipment alloy by SEMI equipment spending (USD 149 bn in 2026, USD 227 bn in 2029, already cited in 5.6.1) deflated, and nuclear tube by reactor construction starts plus a replacement rate (IAEA PRIS starts, WNA). Show the effect on Table 13. Impact: Model +0.1.

### Fix 7. Turbine remelt stock: captive integration and licences change the customer score (8.1 paragraph 3, Table 17 row 2, Table 5 row 1, 5.3.2 implication 1)
* Statement: "casting houses such as CPP, which GE Aerospace agreed to buy in 2026, source from ATI, PCC, Carpenter and Aubert & Duval (GE Aerospace, 2026c)".
* Problems: (a) The repository does not support this supplier list. research/companies/ge-aerospace.md says only that GE "keeps ATI and Howmet as suppliers" (secondary, Leeham via search summary). (b) GE buying CPP (USD 11.75 bn, closing in the second half of 2027) is a captive move. With PCC (which owns Cannon-Muskegon) and Howmet, the open market for casting stock shrinks to the buying decisions of three integrated groups, so Cust 5 is too high. (c) The 8.5 kt of "non aviation superalloy cobalt, mainly in gas turbines" is simply the difference 20.0 minus 11.5 kt. It also contains oil and gas, automotive turbocharger and other industrial uses, so "mainly in gas turbines" needs a source or a TODO(data). (d) Remelt stock and combustor sheet are still one row, although they are two different assets (VIM casting stock against cold rolled sheet) and two different buyers (casting houses against fabricators).
* Correction: cite the supplier list correctly or drop it. Split the row. Add the licence point, and score Cust 4 for casting stock with the CPP note. Impact: Actionability +0.1.

### Fix 8. Oil and gas is still generic (5.2.2, Table 4, 5.2 implications)
* Missing: CRA OCTG grades and mills (13Cr, super 13Cr, 25Cr duplex, Alloy 028, G3 and 2550 type for sour wells, from Tenaris, Vallourec, Nippon Steel and JFE). Alloy 718, 925 and 725 bar to API 6ACRA belongs in the text, not only in A7. 9 percent nickel steel plate for LNG tanks is the volume nickel product.
* Wrong emphasis: "LNG carriers add a FeNi market ... membrane tanks use its Invar M93". Only GTT NO96 uses Invar. Most current newbuilds at Korean yards use Mark III or Mark III Flex with 304L corrugated membranes, so FeNi36 demand follows the NO96 share, not LNG trade growth. Table A1 weights LNG at 0.3 on trade volume without this share.
* Operators and rules: name Saudi Aramco Jafurah, QatarEnergy North Field East and South, ADNOC sour gas and Petrobras pre salt, and the in country value programmes (IKTVA, ICV) that decide vendor lists in the Middle East. 5.2 implication 1 already points there.
* Impact: Actionability +0.2.

### Fix 9. Roadmap bottleneck, owners and benchmarks (8.2 paragraph 1, Table 18)
* The gate is a "melt decision Q2 2028" against the ATI Monroe VIM benchmark. For rotating grade 718 billet the binding constraints are VAR and ESR remelt capacity, billet conversion (cogging presses and radial forges) and premium quality ultrasonic inspection yield, not VIM. ATI's "forging lead times of more than two years" (5.4.2) says the same thing. Name the step that is decided: remelt furnaces plus conversion.
* Owners: qualification is owned by quality and metallurgy with the customer's materials engineering. Sales owns the LTA. "Sales" for initiatives 1 and 2 will look naive to an OEM reader.
* Initiative 3 combines CoCr implants with Alloy 690 under the benchmark "Alleima Mehsana SEK 220 m", which is a chemical tube finishing investment in India. "ASME III approvals" should read ASME Section III NCA 3800 Quality System Certificate (material organisation) plus 10 CFR 50 Appendix B and NQA-1, and RCC-M qualification for EDF programmes. For implants add ISO 5832-4 and 5832-12, the European equivalents of F75 and F1537, and a device master file route. Split the initiative.
* Size revenue: 1.5 kt at a stated billet price range (team estimate, from Carpenter or ATI segment revenue per shipped tonne where disclosed) gives the board the number it asks for first.
* Impact: Actionability +0.2.

### Fix 10. Consistency, sourcing and reference defects (5.7.2, 8.1, 5.3.2, Table 16, 4.1, Table 6, References)
* Carpenter medical: 5.7.2 says "excluding surcharge fall 24 percent to USD 224.3 million", 8.1 says "Carpenter medical sales of USD 278.4 m". The second figure includes surcharge (data/sources.csv MED_CRS_MED_EXSUR_2026). Use one basis or label both. Note also that Carpenter medical is largely titanium and stainless, so it is not a CoCr pool.
* Solid oxide (Table 16 signpost "Strip contract at Bloom Energy", Table 17 row 6): Bloom's interconnects are widely reported to be in house powder metallurgy chromium alloy parts, not purchased ferritic strip. Verify. Ferritic coated strip buyers are the Ceres licensees, Elcogen, Sunfire and Topsoe (SOEC, Herning). Retarget the signpost or mark it unverified.
* Table 6 row 4 "Combustor and wear parts where nickel alloys replace cobalt: Cobalt alloy sheet and plate" contradicts itself. Row 3 should read "CoCr and nickel superalloy powder".
* 4.1: the LME Chinese share and the Vale and Nikkelverk statement are cited to "United Nations Statistics Division, 2026a" (Comtrade), which cannot be the source for LME stocks. The mirror flow "Australia 981" is 2024 and includes BHP Nickel West, suspended in October 2024, so Western class 1 feed is tighter than Table 11 suggests. Add one clause.
* 5.4.2: "Special Metals in Huntington" as a triple melt rotating billet site should be checked against the company profile.
* References: CMOC Group (2026) is a Mining Weekly article and duplicates Mining.com (2026), the same story. Safran (2026a) points to edrmagazine.eu. SEMI (2026a) and Infineon Technologies (2026) are Evertiq articles. SEMI (2026c) carries a semi.org URL and the label "Evertiq". Westinghouse Electric (2025) is a K&L Gates page. Armees.com is the only source for Aubert & Duval revenue. Cite the actual publishers (APA 7: author = the organisation that published the page).
* Impact: Writing 2.0 to 1.7.

## 4. Gaps that keep me from forwarding this to my board
1. Volume weighted answer (fix 1). The board wants to know where the tonnes and the EUR are. The report has the kt now but does not lead with them.
2. China as a producer (fix 5). Not one Chinese melter is named, although China melts about a third of the P50 superalloy tonnage on the team's own cross check.
3. Price per form. Base price increases and the C-276 premium are shown, but there is no EUR per kg ladder by form (718 billet, C-276 plate, CoCr bar, FeNi36 foil). HS 6 alloy unit values (fix 4) and Carpenter and ATI revenue per shipped tonne would give a first, defensible ladder.
4. Region. 7.2 still has one regional paragraph built on investment shares. An engine and turbine assembly map (Comtrade 8411 by exporter, OEM plant lists) would make the "Region" in the frozen heading true.

## 5. Top ten improvements ranked by impact
1. Lead chapter 2, 7.2, Figure 3 and chapter 9 with the volume weighted message, and add base kt to Table 13 (fix 1). Storyline +0.3.
2. Apply Table A4 to 720Li and add the CBMM niobium row, then rescore engine bar and say whether priority 1 survives (fix 2). Actionability +0.2, Model +0.1.
3. Repair the haircut tests (Boeing label, turbine OEM vintages), sum three turbine OEMs, add the IGT aftermarket component (fix 3). Model +0.2.
4. Pull HS 750512, 750522, 750620 and 750712 for alloy only tonnage and unit values, and correct A4 (fix 4). Research +0.2.
5. Name Chinese and Japanese melters, Cannon-Muskegon and the alloy licences, and separate customers from peers in Table A12 (fix 5). Research +0.2.
6. Rebuild the roadmap around remelt and conversion capacity with correct owners, nuclear and implant approval names and revenue sizing (fix 9). Actionability +0.2.
7. Complete oil and gas with OCTG, API 6ACRA, NO96 against Mark III, named operators and IKTVA and ICV (fix 8). Actionability +0.2.
8. Correct the CPP supplier claim, split remelt stock from sheet, adjust Cust for captive casting (fix 7). Actionability +0.1.
9. Replace stock drivers by flow drivers for fab and nuclear tube (fix 6). Model +0.1.
10. Fix the Carpenter basis, the Bloom signpost, Table 6, the 4.1 citations and the six reference publishers (fix 10). Writing +0.3.

With fixes 1 to 5 the report reaches about 1.3 to 1.5. With all ten, it is a 1.3 that I would circulate to an alloy group board with only a cover note.

# Round 3 industry grader review (nickel alloys and specialty stainless)

Reviewer profile: 20 years in nickel alloys and specialty stainless (VIM, VAR, ESR, rolling, alloy surcharges, AMS, ASME, NADCAP, RCC-M qualification, competitor landscape).
Object: reviews/round_3/report_v3.txt (30 main text pages, references p. 31 to 42, appendices A1 to A8 p. 42 to 49) and sections/*.md, checked against CLAUDE.md (seven-link chain, no client naming), data/toc.json, reviews/research_audit.md, reviews/framework_changes.md and data/clean/. Read only, nothing in the report was edited.

## Overall grade: 2.3 (very good structure, but three or four statements an insider would catch on page one of the data)

| Criterion | Weight | Grade | Reason in one line |
|---|---|---|---|
| Research depth and source quality | 25% | 2.3 | USGS MCS 2026, INSG, Cobalt Institute, IMOA, ITIA, Pink Sheet, Comtrade, PRODCOM and about 40 filings drive the numbers, but Table 10 publishes PRODCOM values that fail a basic unit value check, Comtrade covers ten reporters only, and the only alloy market size (chapter 1) is still two paid market reports |
| Model transparency and reproducibility | 20% | 2.7 | Index formula and Table A1 reproduce exactly, but there is no base tonnage, product families are unweighted averages of industry indices, and "Region" in 7.2 is one qualitative paragraph |
| Storyline from data to strategy | 20% | 2.0 | Answer first in chapter 2, clean metal first chain, stage ladder applied consistently in prose, chapter 8 traces to chapters 4 to 7 |
| Actionability and strategic insight | 15% | 2.7 | Tiers, gates, stop list and kill criteria now exist, but the matrix mixes incumbent and entrant perspectives, several scores contradict chapter 7, and no tonnes or capex per initiative |
| Writing and house style | 10% | 2.0 | House style clean, but reference list has wrong URLs (Safran 2026a points to the GE 10-K), duplicates (ATI 2026a and 2026b identical, BASF 2026a and 2026b same URL) and author mismatches (United Nations vs United Nations Statistics Division, CMOC entries that are Mining Weekly and Mining.com articles) |
| Visuals and design | 10% | 2.3 | Three message titled charts and consistent tables, Table 14 abbreviations need a legend, the Figure 3 range bars are hard to read in the text export |

Weighted result 0.575 + 0.54 + 0.40 + 0.405 + 0.20 + 0.23 = 2.35, graded 2.3. This is a clear step up from round 2 (3.0): the client issue is gone, the chain is visible on every page, and the peer benchmark, qualification gates and kill criteria are what a board wants to see. What holds it back is that a few facts are wrong in a way that an alloy salesperson would notice immediately, and the market size link of the chain still rests on numbers that do not survive a unit value check.

## 1. Research depth (explicit judgement)

Built from structured databases and filings (good):
* Chapter 4 volumes come from the USGS MCS 2026 commodity chapters and the study groups (INSG, Cobalt Institute, IMOA, ICSG, IAI, IMnI, ITIA), prices from the World Bank Pink Sheet. Stage labels (contained, gross weight, sponge, ferrochrome) are correct throughout.
* The German HS 7506 unit value (USD 578 m / 17,775 t = USD 32,500 per t) reconciles with data/clean/comtrade_7506 and with the PRODCOM export quantity for DE (18,087 t, within 1.8 percent). This is still the best single piece of evidence in the report.
* Company evidence comes from 10-K, 20-F, annual and interim reports (ATI, Carpenter, Howmet, Alleima, Outokumpu, Aperam, Daido, Nippon Yakin, Safran, GE, RTX, Siemens Energy, Stryker, Zimmer Biomet), dated to Q3 2026. Good.

Weak or borrowed:
* **Table 10 (6.1) fails a plausibility test.** From data/clean/apparent_consumption_prodcom_2019-2024.csv, EU27 2024: plate and strip 57.8 kt for EUR 697 m is EUR 12,000 per t, tubes 9.2 kt for EUR 42 m is EUR 4,500 per t. Both are below the value of the contained nickel alone (LME 2024 about USD 16,800 per t, roughly EUR 15,500), whereas real nickel alloy flat and tube sells at EUR 25,000 to 60,000 per t, and German exports in the same code average USD 32,500 per t. The cause is visible in the raw rows: EU production values are rounded or estimated confidential cells (bars 2,500 t and EUR 100 m, tubes 21,000 t and EUR 280 m), and DE flat production is reported at EUR 8,800 per t against DE exports at EUR 32,600 per t. In addition, EU bar production of 2.5 kt is impossible next to German bar exports of USD 638 m in the same year. reviews/research_audit.md lists research/materials/apparent_consumption.md as the only FAIL (7 sources, no Comtrade, Pink Sheet, USGS or company cross check), and this table is exactly that note's output.
* Comtrade covers ten reporters. Russia, Canada, Norway, Australia and Finland, the largest class 1 nickel exporters, are missing, so "China ... dominates the export of unwrought nickel" (6.2) is an artefact of the sample. Mirror data (world imports by partner) are available on the public endpoint and fix this.
* The only size of the high performance alloy market (chapter 1, USD 13.6 bn and USD 10.2 bn) still comes from The Insight Partners and IMARC. A bottom up triangulation from INSG first use (nickel in nickel based alloys), Cobalt Institute superalloy demand (20 kt), ITIA (14 percent to steels and superalloys) and IMOA first use is possible with sources already in the report.
* OECD STAN, ICIO and UNIDO INDSTAT are claimed in chapter 3 and A3 but used for one number (German E&E value added). Either use them or drop them from the method claim.

Verdict: metal supply and company facts are database driven and current. The Market size link is not, and its one official table is numerically unfit for print.

## 2. Errors with corrections (ranked fixes, located)

Ranked by impact on credibility with an alloy industry board.

### Fix 1. Table 10 values are below metal value (sections/06_trade.md, lines 7 to 17)
* Statement: "about 72 kt and EUR 889 million in 2024, of which flat products accounted for 57.8 kt", tubes "9.2 kt, EUR 42 m".
* Problem: implied EUR 12,000 per t (flat) and EUR 4,500 per t (tubes), below contained nickel value. Production cells are rounded or estimated confidential values, so production plus imports minus exports in EUR is meaningless. EU bar production of 2.5 kt contradicts German bar exports of USD 638 m.
* Correction: drop the EUR column or replace it with a value built as tonnage times the Comtrade EU export unit value (flat about USD 31,000 per t, tubes about USD 26,000 per t from PRODCOM extra-EU exports), labelled team estimate. Add a row "implied EUR per t" so readers see the check. Flag the bar line as "production confidential, not interpretable" instead of 5.4 kt. Rerun research/materials/apparent_consumption.md until the audit passes. Expected impact: Research 2.3 to 2.0, removes the most embarrassing number in the report.

### Fix 2. Medical product form error (sections/05_7_medical_technology.md, Table 9 line 17, bullet line 26, sections/11_appendices.md line 155)
* Statement: "CoCr bar to ASTM F75 and F1537".
* Problem: ASTM F75 is the cast CoCrMo specification (knee femoral components are investment cast from F75 remelt ingot). Wrought bar is ASTM F1537 (hip stems, modular heads, tibial parts). Additive CoCr is ASTM F3213. Stems are mostly Ti6Al4V ELI bar to ASTM F136 and heads increasingly ceramic (CeramTec BIOLOX delta).
* Correction: split the row into "CoCrMo remelt ingot to ASTM F75 for investment casters", "CoCrMo bar to ASTM F1537" and "CoCr powder to ASTM F3213". Name the incumbents (Carpenter BioDur CCM, ATI, Ugitech for bar, Fort Wayne Metals for wire) and the buyers' casting route (in house foundries and contract casters such as Orchid, Lisi Medical). Also check "Smith & Nephew supplies from its own chain": OXINIUM is oxidised Zr2.5Nb (ASTM F2384) and the wrought bar is bought from a zirconium producer (ATI is the usual source), so the substitution threat lands on CoCr but creates a zirconium bar opportunity. Expected impact: Actionability +0.2, credibility with medical buyers.

### Fix 3. Product family index contradicts the ranking (sections/07_scenarios.md line 45 vs sections/08_recommendations.md line 16 and 29)
* Statement: Table 13 gives "Precision FeNi strip and foil ... About 110", the lowest family, yet Table 14 scores its growth 4 of 5 and puts it in tier 1.
* Problem: the FeNi index averages electronics (134) with the whole automotive index (86), which is driven by declining engine alloys. Soft magnetic FeNi in electric drives grows (Table 3 says so). This is a stage error inside the model: an industry index is used as a product index.
* Correction: weight product families by product specific rates (FeNi in automotive should use the "grows" line of Table 3, for example EV production growth from IEA GEVO), or present Table 13 as weighted by a documented split. Then either keep FeNi in tier 1 with a consistent growth score or move it to tier 2. Also qualify the OLED mask story: Proterial is the near monopoly Invar foil supplier to DNP and Toppan, Gen 8.6 IT OLED lines (Samsung Display A6, BOE B16) drive volume, and maskless photolithographic patterning (JDI eLEAP, Visionox ViP) is a substitution threat. Expected impact: Model 2.7 to 2.3.

### Fix 4. Oil and gas geography is upside down (sections/05_2_oil_and_gas.md line 3, bullet "Concentrate sales on gas and offshore projects in Central and South America and in Sub Saharan Africa")
* Statement: the market moves "from the Middle East toward the Americas and Africa".
* Problem: the Middle East remains the largest CRA market and the sourest: Saudi Aramco Jafurah (high H2S unconventional gas), Qatar North Field East and South, ADNOC sour gas and Hail and Ghasha. These buy CRA OCTG, Alloy 825 and 625 clad and lined pipe and 718/925 completion bar under in country value rules (Aramco IKTVA, ADNOC ICV). Also, procurement for Brazil pre salt and African deep water happens through EPCs and subsea majors in Houston, Paris, Oslo and Rio, not in the producing country.
* Correction: say "growth in investment shifts to the Americas and Africa, while the Middle East remains the largest sour service CRA market", and redirect the bullet to "approved vendor lists at Petrobras, Aramco, ADNOC and QatarEnergy plus the EPCs and subsea majors (TechnipFMC, Subsea7, Saipem, SLB OneSubsea)". Add the missing product forms: super duplex umbilical tube and 22Cr/25Cr duplex, 13Cr and super 13Cr OCTG, Alloy 718, 925 and 725 bar to API 6ACRA, Invar 36 strip for GTT NO96 LNG membrane tanks and 9 percent nickel steel plate for LNG storage. Also delete "Every producer meets the sour service standard ISO 15156": ISO 15156-3 qualifies materials and their condition (hardness, heat treatment), not producers, so write "the qualified grades listed in ISO 15156-3 are a commodity, the moat is operator approval and NORSOK M-650 qualification of each manufacturer and product form". Expected impact: Actionability +0.2.

### Fix 5. The aerospace moat is named in generic terms only (sections/05_4_aerospace.md 5.4.2 and sections/11_appendices.md A7)
* Statement: "each requires AMS specifications, NADCAP accredited processes and part level approval", A7: "Years per part family".
* Problem: the defining barrier is premium rotating grade material: triple melt VIM plus ESR plus VAR (Alloy 718, Waspaloy, 720Li billet), melt route freeze, OEM material specs (GE P and B specs, Rolls-Royce RRMS, Pratt and Whitney PWA, Safran DMD) above AMS 5662 and 5663, and powder metallurgy discs (René 65 cast and wrought, René 104 and the PW GTF powder metal issue of 2023 as a demand spotlight). A new melt route takes typically 3 to 5 years to first rotating approval. Without this, "qualified second source" in 8.1 reads naive, because second sources need a qualified triple melt route, not only capacity.
* Correction: add one sentence in 5.4.2 and a column "typical time to first approval" in Table A10 (aerospace rotating 3 to 5 years, static sheet and wire 1 to 2 years, IGT casting stock 1 to 2 years, NORSOK and operator lists 1 to 2 years, nuclear with ASME III and RCC-M per programme, medical F1537 with ISO 13485 audits 1 to 2 years), each with a source or labelled team estimate. Expected impact: Research and Actionability +0.2 each.

### Fix 6. Opportunity matrix perspective is inconsistent (sections/08_recommendations.md lines 9 to 31)
* Problem: "entry barriers" scores 5 as attractive for engine billet, which is true for an incumbent, while the text concludes "the realistic role for a new entrant is that of a qualified second source". For an entrant the same barrier is a cost. Competitive intensity 3 is generous for an oligopoly of PCC (Special Metals, Wyman-Gordon), ATI, Carpenter, Aubert & Duval, Proterial and Daido with long term agreements. Repair wire and superalloy powder at Diff 5 and Tech 5 is implausible: AM powder is crowded (Carpenter Additive, Höganäs, Sandvik Osprey, ATI, Oerlikon, Colibrium Additive (AP&C), Linde, and Chinese PREP producers), and repair wire is a small AMS 5832 type niche. Turbine remelt stock is dominated by Cannon-Muskegon (PCC) and a few others, so Comp 3 is too friendly.
* Correction: state the perspective once ("scores for an established vacuum melter without OEM rotating approvals" or two columns, incumbent and entrant), lower Comp for engine billet and remelt to 2, Diff for powder to 3. Recalculate: powder falls to about 3.6 (tier 2). Expected impact: Actionability 2.7 to 2.3.

### Fix 7. Missing producers and supply chain facts that a board expects (4.1, 4.3, 4.5, 4.7.5, A6)
* Nickel 4.1: name the class 1 sources vacuum melters actually qualify (Vale, Glencore Nikkelverk, Sumitomo Metal Mining, Jinchuan, Nornickel), the LME ban on Russian metal produced after 13 April 2024, and the BHP Nickel West suspension of October 2024. Without these "Medium" supply risk is unsupported.
* Chromium 4.3: the "single qualified source" sentence should name the vacuum grade aluminothermic chromium suppliers (Delachaux in France, AMG Chrome in the UK).
* Niobium 4.7.5: vacuum grade NiNb master alloy for Alloy 718 comes almost entirely from CBMM (Brazil). That is a sharper single source risk than anything in the scorecard.
* Titanium 4.5: VSMPO-AVISMA and the Western exit from Russian titanium after 2022 explain the aircraft grade shortage. Toho Titanium and UKTMP (Kazakhstan) belong next to Osaka.
* Energy 5.3: GE Vernova and Mitsubishi Power are the other two heavy duty OEMs and both announced capacity ramps, and aeroderivative units for data centres (LM6000, LM2500XPRESS, SGT-800) use aero grade 718 discs, which weakens "Heavy duty rotor discs are mostly steel" as a general statement.
* A6: add Proterial, voestalpine High Performance Metals (Böhler Kapfenberg), PCC detail (Special Metals, Wyman-Gordon), Doncasters, and Chinese producers (Fushun Special Steel, CISRI Gaona, Baowu Special Metallurgy). Note that Aperam acquired Universal Stainless and Alloy Products in 2025, which changes the US premium melt landscape. (The largest European nickel alloy producer is excluded by the no client naming rule, and the text should say once that the benchmark omits one major European producer by design, so experts do not read it as an oversight.)
* Expected impact: Research +0.2, the difference between "analyst" and "insider".

### Fix 8. Comtrade sample presented as a ranking (sections/06_trade.md line 40 and 6.2 text)
* Statement: "The same logic separates China, which dominates the export of unwrought nickel".
* Correction: pull HS 7502 and 7505 to 7507 with partner "World" as importer (mirror data) to add Russia, Canada, Norway, Australia, Finland, Austria and Sweden, or rephrase to "among the ten reporters". Also note that HS 75 covers only nickel predominant alloys: Alloy 800 type and FeNi36 sit in chapter 72, cobalt alloys in 8105, and superalloy forgings and castings in 7508 or 8411.99, so HS 7505 to 7507 understates the product market. Expected impact: Research +0.1.

### Fix 9. Value multiple understated and surcharge mechanism missing (sections/04_1_nickel.md line 9, sections/06_trade.md line 42, sections/05_5_chemical_processing.md)
* Statement: USD 32,500 per t "roughly twice the exchange price of the contained metal".
* Problem: a tonne of nickel alloy does not contain a tonne of nickel. C-276 holds about 57 percent nickel plus 16 percent molybdenum. Compute the raw material value of a typical alloy (Pink Sheet nickel, USGS molybdenum, chromium metal prices) and show the conversion premium properly, which is the core argument of the report. The chemical section mentions surcharges in half a sentence: add how they work (monthly surcharge on the prior month's LME and Mo averages in Europe, lagged index clauses in aerospace LTAs, raw material timing effects in producer earnings) and that the base price, not the surcharge, is where margin sits. A base price or BLS PPI series for nickel alloy mill shapes would give the report its first real product price.
* Expected impact: Model +0.2.

### Fix 10. References and smaller factual items (References, sections/04_4, 05_1, 05_5)
* Safran (2026a) URL is the GE 10-K, replace with Safran's FY2025 results page. ATI 2026a and 2026b are the same document, merge. BASF 2026a and 2026b share one URL. "United Nations (2026)" and "United Nations Statistics Division (2026a to d)" should be one author. CMOC 2026a and 2026b are Mining Weekly and Mining.com articles, cite those publishers. Westinghouse (2025) is a K&L Gates page and Infineon (2026) an Evertiq article, same issue. SEMI (2026a) is Evertiq, 2026b semi.org, labels swapped.
* 4.4: "Only China and the United States operate primary molybdenum mines" ignores Russia (Sorsk) and Canada's idled Endako, write "almost all primary mine output comes from China and the United States". The MOFCOM 2025 No. 10 controls cover specific molybdenum products (certain powders and alloys), not oxide or ferromolybdenum in general, so the scorecard "Chinese export licences" overstates the risk for melt shops.
* 5.1.2: stray comma "from 2027, (BorgWarner, 2026)".
* 5.5: "Alloy C-276, 59 and 625" uses a single producer's proprietary grade as a category, write "C-276, C-22, 59 type NiCrMo alloys, 625 and Nickel 200/201 for chlor alkali".
* 5.6: FeNi42 lead frames are now a small share against copper alloys (CuFe2P, CuNiSi), which should be stated in the "Stable" row.
* Expected impact: Writing 2.0 to 1.7.

## 3. Gaps that keep me from forwarding this to my board
1. No tonnage. The report never says how many tonnes of nickel based alloy, superalloy or CoCr the world melts. A board thinks in kt of melt and EUR per t of base price. A contained metal triangulation (INSG first use for nickel alloys, Cobalt Institute 20 kt superalloys, ITIA, IMOA) would close the Market size link with official data.
2. No base price or margin per product form. Peer margins are in A6, but there is no evidence that engine billet earns more per tonne than chemical plate, which is what the ranking claims.
3. Region in 7.2 is qualitative. A simple split of the base indices by region (for example aerospace by engine assembly country from Comtrade 8411, chemicals by Cefic regional shares) would make the "Region" in the heading true.
4. No China section on the producer side. Fushun, CISRI Gaona and Baowu now hold COMAC and AECC approvals and are building VIM and VAR capacity, which is the main long term price risk for European plate and sheet, but the report treats China only as a raw material and policy actor.

## 4. Top ten improvements ranked by impact
1. Replace or caveat Table 10 values (Fix 1). Research +0.3.
2. Correct the medical product forms and specs, F75 cast, F1537 bar, F3213 powder, Zr2.5Nb bar (Fix 2). Actionability +0.2.
3. Make Table 13 product specific and reconcile with Table 14 (Fix 3). Model +0.3.
4. Rewrite the oil and gas geography and product forms, delete the ISO 15156 producer claim (Fix 4). Actionability +0.2.
5. Add triple melt, OEM specs and time to approval to 5.4.2 and A7 (Fix 5). Research and Actionability +0.2.
6. State the matrix perspective and correct the Comp and Diff scores (Fix 6). Actionability +0.2.
7. Add a contained metal tonnage triangulation of the alloy market to replace the two market reports in chapter 1 (Gap 1). Research +0.3.
8. Name class 1 nickel, chromium metal, NiNb and titanium sponge sources and extend A6 with Proterial, Böhler, PCC units and Chinese producers (Fix 7). Research +0.2.
9. Mirror trade data and the HS 75 coverage note (Fix 8). Research +0.1.
10. Show the conversion premium on alloy content and explain the surcharge versus base price, then fix the reference defects (Fixes 9 and 10). Model +0.2, Writing +0.3.

With fixes 1 to 6 the report reaches about 1.7, with all ten about 1.3 to 1.5.

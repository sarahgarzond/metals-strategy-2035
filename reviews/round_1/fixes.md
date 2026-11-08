# Round 1 fixes

Decision: **CONTINUE**. Official grades are TUM 2.7, industry 2.7, client 2.7. Average 2.7. This is the first round. The fact check still has wrong and unsourced headlines, so the stop rule is not met. Rank is impact on the grade, times how many reviewers raised the point, then effort. Apply in this order. Do the factual replacements before the line edit in fix 15.

Work in one pass where the files overlap. Fixes 3 and 4 both rewrite Chapter 5. Fix the attribution in fix 3 first, then set the verbs in fix 4, so the closes are not rewritten twice. Fixes 1 and 2 both touch Chapters 4, 6 and 8. Log the basket and the unit values in fix 1 before Chapter 8 states the capacity rule in fix 2.

Leave these decisions in place. They are what the panel would keep:

- No aggregate addressable market, and no EUR 50 billion total.
- VDM and Haynes stay one Acerinox business. Never add a separate Haynes capacity to a separate VDM capacity.
- Mine nickel, primary nickel, stainless melt and mill product stay on separate lines. EU stainless melt of 5.659 million tonnes against EU nickel flat apparent consumption of about 58 thousand tonnes stays a gross tonne scale check. It does not convert melt into contained chromium and it does not set a high performance market.
- The apparent consumption identity stays sold production plus imports minus exports. German HS 7506 exports of 17,775 tonnes stay next to the PRODCOM export leg of 18,087 tonnes.
- Chapter 3 keeps Supply, Trade, Demand and Outlook, in that metal first order. No new dimension and no new chapter.
- The table of contents has no executive summary. Do not add one.

Every new figure needs a row in `data/sources.csv` before it enters `sections/`. Unit values that are a division of two logged cells are labelled `team estimate`. The industry grader's rounded euros are a target for that calculation, not a licence to type an unlogged number.

## 1. Separate apparent consumption from the qualified alloy market

| Field | Entry |
| --- | --- |
| Fix | Publish one basket table and stop treating the mixed flat code as qualified alloy demand. |
| Section | `sections/04_1_nickel.md`, `sections/04_3_chromium.md`, `sections/06_trade.md` (Table 10 and the capacity passage), `sections/09_conclusion.md`, Appendix A1 in `sections/11_appendices.md` |
| Type | logic |
| Raised by | industry (top two items), client (scale misread and the single size exhibit), TUM (stage ladder and the repeated 58 thousand tonne sentence) |
| Owner | data-modeler |
| Effort | medium |

The quantity identity for PRODCOM 24452200 is confirmed: 80.9 + 14.4 − 37.5 = 57.8 million kilograms in 2024. The join is wrong. Chapter 6 already says the code mixes pure nickel and nickel alloy and does not report contained nickel. Later chapters then call 57.8 million kilograms specialty flat product and place the company in that layer. A buyer will reject that reading. EU sold production is logged near EUR 14,500 per tonne and German sold production near EUR 8,800 per tonne, against import unit values near EUR 47,800 per tonne and Acerinox High Performance Alloys sales of EUR 1,683 million on 47 thousand finished tonnes. Log the value columns, show euro per tonne beside every PRODCOM tonne in Table 10, and label the division a team estimate. Flag the German series break from 15.9 thousand tonnes in 2019 to 36.5 thousand tonnes in 2020 while logged value stayed near EUR 180 to 190 million. State that EU27 PRODCOM trade is extra EU trade, so hot band sold to an EU reroller and then sold again as cold strip can sit inside sold production twice. The 57.8 million kilograms is an upper bound on a mixed code.

Add the Eurostat `:E` flag on the EU flat sold production leg. Split HS 750610 (not alloyed) from HS 750620 (nickel alloys) for Germany and the EU before Chapter 8 uses the balance. Strip foil, coin and battery nickel if they dominate 750610. Until that split is in the source log, Chapter 8 and the conclusion describe 57.8 million kilograms as the ceiling of a mixed code. They do not call it qualified alloy demand or room under the Acerinox finish figure.

Call 83 thousand tonnes melted and 47 thousand tonnes finished what the filing reports: 2025 output, VDM and Haynes counted once. Output in a weak chemical and oil and gas year sits below nameplate. The 2028 furnace and finishing steps are capacity that is not inside the 2025 tonnes. Ask for nameplate by plant and by route in Appendix A4. Quote Acerinox's melt footnote before anyone adds 83 thousand tonnes to stainless melt, because a VIM heat and the VAR or ESR remelt of the same metal would double count. Finished product is 47 thousand tonnes worldwide, all forms, including plants in Kokomo, Arcadia and Mountain Home. Compare apparent consumption with finished shipments only after the alloy split. The sentence that EU flat apparent consumption sits below group melt will be read as one competitor covering Europe. Retire that sentence.

Time the Outokumpu tonnes and park them in stainless. About 13 thousand tonnes is a specialty stainless pocket at Avesta, inside 2025 deliveries of 1,751 thousand tonnes. Remelt equipment is early 2028. Greenfield melt and casting follow a go or no go in the first half of 2027, with production at the end of 2029. The August 2026 discussion of high nickel alloys is 5.5 to 12 percent nickel. Duplex, 904L and 254 SMO are chapter 72. Overlap with a nickel alloy mill is mainly on nickel predominant grades such as Alloy 825. Those tonnes are not current chapter 75 plate, and they are not 13 thousand tonnes of 625 or C-276. They are evidence of competitive intent at the boundary.

Replace the triangulation subsection title with "Output, trade and stainless melt". That heading sits below the fixed skeleton.

Build one table, message title in the form "Logged nickel mill product is tens of thousands of tonnes, and the flat code still mixes pure nickel with alloy". Rows, each with the year and the unit: world contained mine production, primary production and use, world and EU stainless melt, Acerinox group melt, Acerinox High Performance Alloys 2025 melt and finish with division sales, Outokumpu stainless deliveries, the timed Avesta programme, EU flat apparent consumption, German flat apparent consumption, EU bar apparent consumption. Point Chapters 7, 8 and 9 at this table. Delete later retellings of the same ladder so the 30 page cap holds. Activity totals (upstream spending, chemical sales, device sales, aviation cobalt) stay in a short paragraph or in Appendix A3, labelled illustration, not alloy demand.

Aperam Alloys and Specialties belongs on the same page only if 61 thousand tonnes and the printed average selling price are logged from the filing first. Different book from High Performance Alloys. It stops a reader treating Acerinox as the only European specialty mill.

## 2. Turn the flat surplus and the bar deficit into the Chapter 8 capacity rule

| Field | Entry |
| --- | --- |
| Fix | State a plant rule that follows the trade result, and tie each priority to the code it actually ships in. |
| Section | `sections/08_recommendations.md` (8.1), `sections/06_trade.md`, `sections/07_scenarios.md` (7.2), `sections/09_conclusion.md`, Table 10 |
| Type | logic |
| Raised by | client (the change that stops a bad capacity vote), industry (priority 1 is outside the statistic used to size it, and the bar balance is a rounded estimate), TUM (the bar deficit never reaches the recommendation), fact check (medium, bar rounding) |
| Owner | strategist |
| Effort | medium |

Write three sentences a plant director can apply.

Bar, rod and wire is the form where the published EU identity is a net import: sold production 2.5 million kilograms, imports about 5.6 million kilograms, apparent consumption 5.4 million kilograms (5,380,347 kilograms). The sold production cell is Eurostat `:R` with a 500,000 kilogram rounding base, so apparent consumption can sit roughly between 5.1 and 5.6 million kilograms. The net importer conclusion holds inside that band. Say so in Table 10. Exports on that row are about 2.70 million kilograms, above the rounded production figure, which means stock or an estimate that is not a census. Special Metals at Hereford is outside EU27 and is a main European source of nickel alloy billet and bar. HS 7502 (unwrought, where rotating billet is often declared) is outside the extract. The commercial test in months 0 to 3 is the client's own bar book against this logged position. It is not a proposal to add bar capacity. No bar investment case until the footnote, UK supply and HS 7502 are in the text.

Flat products are a net export of a mixed code (sold production 80.9, exports 37.5, imports 14.4 million kilograms). Chemical plate and electrical strip are pursued where a named grade is imported or a replacement order displaces a specified supplier. Undifferentiated flat tonnes are refused. The 57.8 million kilograms is the ceiling of the code. The qualified alloy slice is smaller and still unmeasured.

Map the ranking onto codes. Qualified aerospace product for a wrought mill is billet, bar, sheet and weld wire, read against 7505 and 7502, not against the flat balance. Corrosion resistant plate is alloyed flat, read against 750620 once that split exists. Expansion alloys 29-18 and 42, Crofer 22, Aluchrom and much of the soft magnetic book are iron predominant, chapter 72. Konstantan and other copper nickel resistance alloys are chapter 74. Nickel 201 electrolyser strip is unalloyed nickel in HS 7506, at a different price and a different buyer from C-276 plate. One flat balance cannot size all three priorities.

Rewrite "declining engine only applications" as automotive engine and exhaust (turbochargers, valves, plugs, exhaust). In this industry, engine means the aero engine and the industrial gas turbine. Add industrial gas turbines beside aerospace, because 718, 625, X and 230 are being pulled there. Haynes' strength is aerospace and industrial turbines. VDM is the book facing the weak chemical and oil and gas year. The recommendation has to say that, with VDM and Haynes still counted once inside Acerinox.

## 3. Keep VDM as the benchmark, and put one Acerinox line on every competitor list

| Field | Entry |
| --- | --- |
| Fix | Remove every sentence that gives Münvest a VDM approval or a VDM order book, and name Acerinox High Performance Alloys once wherever the grade is actually contested. |
| Section | `sections/05_1_automotive.md`, `sections/05_2_oil_and_gas.md`, `sections/05_4_aerospace.md`, `sections/05_7_medical_technology.md`, competitor paragraphs in `sections/05_5_chemical_processing.md` and `sections/04_7_other_metals.md` |
| Type | logic |
| Raised by | TUM (validity cap: storyline stays at 2.3 until this is fixed), industry (brochure used as the company's qualification, and competitor lists a director would correct), client (a false approval costs more trust than a missing tonne) |
| Owner | writer |
| Effort | small |

Chapters 2, 4.7 and Appendix A4 already state the rule. Sections 5.3 and 5.5 already say benchmark. Sections 5.1, 5.2, 5.4 and 5.7 say the company sells the products, that eight of eleven car applications are the company's, and that eleven of its alloys are approved for sour gas. Those sentences cite VDM, or in aerospace they cite Airbus, NASA and the US Geological Survey. A NACE MR0175 / ISO 15156 listing names the producer and the route. It does not travel with a catalogue.

In each of those four sections, use two sentences or two columns. "Benchmark application, from the VDM Metals portfolio" carries the VDM citation on the application and the materials. "What Münvest would need before this is an order" names grade, form, approval and buyer, and states that shipment, approval and share are unconfirmed. Delete any approval count taken from VDM. Sour service, AMS and ASME stay with the mill that poured the heat.

On every list that includes 625, 718, C-276, 188 or 230, write one line: "Acerinox High Performance Alloys (VDM and Haynes)". Split Germany and the United States inside that line when the corridor differs. Do not add their tonnes to the 83 and 47 already counted.

| Sector | Add on the same page |
| --- | --- |
| Aerospace | Acerinox High Performance Alloys as one, Aubert & Duval, Special Metals, ATI, Carpenter, Howmet and PCC for castings, Proterial. Daido may stay. |
| Oil and gas | Acerinox High Performance Alloys as one, Special Metals, Alleima, Nippon Steel, Tubacex. Replace the 2015 name Nippon Steel and Sumitomo Metal. |
| Automotive strip and wire | Aperam Alloys, Proterial, Nippon Yakin, Acerinox High Performance Alloys. Carpenter and Special Metals are minor in European spark plug and sensor strip. |
| Chemical plate | Acerinox High Performance Alloys as one, Special Metals, ATI, and Chinese mills on standard 625 plate. A patented Haynes grade is a different contest from commodity 625. |
| Electronics | Aperam Imphy, Proterial, Nippon Yakin, VDM inside Acerinox. This book is mostly chapter 72. |

Chinese mills matter for standard 625 plate, welding wire and stainless. They matter less for a patented Haynes grade or a VAR disc billet. Say which contest is which.

## 4. Give every sector close the same priority list as Chapter 8

| Field | Entry |
| --- | --- |
| Fix | Rewrite the seven "What the company should do" lines onto one verb set, and put a stop list next to the pursue list. |
| Section | `sections/05_0_industry_needs.md`, `sections/05_1_automotive.md` through `sections/05_7_medical_technology.md`, `sections/08_recommendations.md` (8.1) |
| Type | logic |
| Raised by | client (seven mandates, and the stop list is thinner than the pursue list), TUM (sector closes disagree with Chapter 8 and with their own tables), industry ("engine only" beside an aerospace engine priority) |
| Owner | writer |
| Effort | medium |

Chapter 8 and the conclusion are the only instruction. Each close uses one of four verbs.

- Qualify for repeating orders: aerospace billet, approved sheet and repair wire, and chemical replacement plate and welding products where a named grade clears the capacity rule in fix 2.
- Keep and harvest: oil and gas accounts where a sour service approval the company itself holds supports the margin, and automotive accounts that are already profitable. Glow plugs and the rest of the diesel only set come off the growth list.
- Option against a financed programme: electrolysers and powders, and medical implant bar until an implant maker and a regulatory path are the company's own. Powders stay inside that gate in energy and in aerospace.
- Stop adding effort: undifferentiated stainless where the duty is already met by stainless, China implant tenders after the price cuts, and any electrolyser or powder programme without a financed buyer.

Section 5.7 currently says focus on zirconium and cobalt implant bar and approach Johnson and Johnson. That becomes an option. Oxidized zirconium is Smith & Nephew's OXINIUM route, not a generic zirconium bar for every implant maker. Carpenter medical sales of USD 224 million, down 24 percent and excluding surcharge, are the alloy mill ceiling. OEM hip and knee revenue is not.

Section 5.2 currently says focus commercial effort on gas and offshore projects in the Americas and Africa. That becomes keep, on the company's own approval. Tube stays off the pursue list until fix 7 logs the three PRODCOM legs or the text says there is no tube capacity recommendation.

Section 5.1 may keep profitable automotive business. Magnetic sensors and magnetic alloys point to section 5.6, because Chapter 5.0 assigned sensors and magnetic components to electronics so the scenario model would not count them twice. The opening sentence of 5.1 has to match Table 2. Cars without a plug go from 58.2 million to 42.9 million in the team estimate. A car with a plug can still have an engine, which Appendix A3 already says. "About half of new cars will be electric" is not the loss of every engine part.

Align the other openings with their tables in the same pass. Table 4's source line lists the works that support the cells, including the case names, and the year of each column. The 2035 spending cell is rewritten in fix 5. Table 6 labels 11,499 tonnes as a cobalt indicator and the 16,100 tonne path as a team estimate, not a Cobalt Institute forecast and not the nickel alloy market. Table 8 labels the device path and the bio health extrapolation as an illustration, which Appendix A3 already requires.

Stop and harvest table in section 8.1, same specificity as the pursue list. Columns: application, form, why effort stops or why the account is only harvested, and "2025 revenue unknown until the month 0 to 3 map" where the internal number is missing. Rows at least: glow plugs and the diesel only set, undifferentiated stainless against a duty stainless already meets, China implant tenders, unfunded hydrogen, powders without a printer programme.

## 5. Replace the three high fact check failures, and the aerospace figures in the same paragraphs

| Field | Entry |
| --- | --- |
| Fix | Delete the unsourced and wrong headlines and use the logged series. |
| Section | `sections/05_2_oil_and_gas.md` (Table 4 and the paragraph above it), `sections/05_4_aerospace.md` (opening, engine paragraph, Table 6, services paragraph) |
| Type | data |
| Raised by | fact check (three high findings, plus the medium and low findings in the same paragraphs), TUM (table and paragraph disagree), client (activity numbers win if the warning sits underneath) |
| Owner | writer |
| Effort | small |

Oil and gas. Delete the path that stays at USD 570 billion in 2035 or rises to about USD 670 billion. World Energy Outlook 2025 does not print USD 670 billion. Current Policies is about USD 65 billion a year above Stated Policies in the detailed chapter. Call the 2025 level upstream oil and gas investment of just under USD 570 billion, and say a large share replaces decline at existing fields. Name the IEA investment report. The citation that only says Energy Intelligence is the wrong primary for that total. Date the "gas at a ten year high, oil down for three years" sentence as 2026 supply investment on the wider boundary (natural gas supply investment of USD 330 billion, oil supply investment below USD 500 billion, including infrastructure). Do not attach that sentence to the USD 570 billion upstream total.

Aerospace deliveries. Keep LEAP deliveries of 1,802 in 2025, up 28 percent from 1,407. Move the GE commercial engine increase of 25 percent (1,989 versus 1,592) to the first nine months of 2026, or drop it. Full year 2025 commercial deliveries were 2,386, and a 2025 growth rate is not logged. Do not add 1,802 LEAP engines to 2,386 GE commercial engines. Defence engines of 635 versus 490 may stay as a 2025 increase.

Services. Delete USD 217 billion of off wing maintenance. If a services cell is kept, use USD 209 billion in 2026 and USD 422 billion in 2045. Describe off wing work by growth of 3.7 percent a year and by the materials share above 85 percent. Safran propulsion stays at a 23.0 percent margin on EUR 15,668 million. Services were up 30 percent in USD. Civil spare parts were up 17.6 percent in USD. The 20 percent services figure is not the logged rate. GE Commercial Engines and Services stays at a 26.6 percent margin on USD 33,314 million. Change the services share from 76 percent to 75 percent.

Same paragraphs, still required. HS 8411 includes parts, so the exporter ranking is not a ranking of complete engines only. Keep Airbus 42,060 and Boeing 43,625, and state the perimeters in the same sentence: Airbus is passenger aircraft of at least 100 seats, Boeing includes 1,435 regional jets and 930 freighters. Say the Airbus 2025 fleet is 23,310 passenger aircraft of at least 100 seats. Call about 32,600 aircraft in 2035 and 3.4 percent a year a team interpolation. Where a published 2035 Airbus figure is needed, use the 82 percent new generation share. Drop "small" on the 2026 and 2027 nickel surplus unless a logged INSG sentence says small. Give the surplus in tonnes if a tonne figure is quoted. Do not treat about 16,100 tonnes of aviation cobalt as a Cobalt Institute forecast.

## 6. Derive the 2035 rates and put them on a physical base

| Field | Entry |
| --- | --- |
| Fix | Show the driver under each rate, and multiply the index only by a tonne range the source log can support. |
| Section | `sections/07_scenarios.md` (7.1, 7.2, Table 11), Appendix A2 and A3 in `sections/11_appendices.md`, the aerospace cobalt path in `sections/05_4_aerospace.md` |
| Type | logic |
| Raised by | TUM (model stuck at 3.0 while rates are unexplained), client (indices never touch the tonnes), industry (one fleet rate mixes new engines with shop visits) |
| Owner | data-modeler |
| Effort | large |

Table 11 reproduces. The rates are author choices, and section 7.2 is titled results by industry, product and region while products and regions stay qualitative. Under each rate, write the driver, the year and the adjustment in one line, using figures already in the report.

Use these drivers, with the fact check corrections already applied. Cars without a plug, 58.2 million to 42.9 million, as a team estimate. The October 2026 committee vote stays out of the model until a value row confirms it. Committed low emissions hydrogen is 4.3 million tonnes a year by 2030 for projects operating, under construction or at final investment decision. Output above 6 million tonnes is the review's conditional case if further projects reach that decision, not a stock already committed. The fleet path of about 3.4 percent a year is a team interpolation from 23,310 to 45,550, not an Airbus 2035 stock. Implant growth uses the logged count path, or the medical row says the device market is an illustration. The medical table that grows a 2023 device market to 2035 at 5.3 percent a year must not sit beside a Table 11 medical row of 2 percent a year from 2025 without the window in the title.

For each of the three priorities, show a 2025 tonne range as a team estimate. The assumption is a stated share of the relevant code from fix 2, or the words "unknown, pending the shipment map". Multiply only that range by the index. If the share is indefensible, drop the index from the board text and keep the rates in Appendix A2. Show all 21 unrounded values in A2. Keep metal prices constant. Keep the refusal to print a company total without shipment weights.

Build one automotive upside that keeps the hybrid path in section 5.1, so the upside is not a flat zero while the chapter describes a surviving engine. Build one aerospace downside that applies a stated superalloy displacement. Ceramic matrix composites already fly on the hottest static hardware. They do not retire the disc. State the condition under which the aerospace downside stops growing: a missed approval, substitution in those hottest parts, or both. A downside that still compounds at about 1 percent a year needs that reason in the table.

Under the aerospace index, two qualitative lines: new engine hardware, and shop visits. Use the Safran, GE, MTU and Rolls-Royce figures already logged. LEAP deliveries rose 28 percent in 2025. Shop visits are the larger OEM profit pool. The index is not a forecast of alloy tonnes. Do not scale 11,499 tonnes of aviation cobalt with the fleet and then use the result as the nickel indicator.

## 7. Bring sections 4.2 to 4.7 up to a minimum metal standard

| Field | Entry |
| --- | --- |
| Fix | Give each remaining metal one dated balance, one price, one form and the producers that matter, and delete every TODO from the body. |
| Section | `sections/04_2_cobalt.md` through `sections/04_7_other_metals.md`, pointers in `sections/05_4_aerospace.md` and `sections/05_7_medical_technology.md` |
| Type | data |
| Raised by | TUM (largest research lever, six of ten metals do not answer production, availability or price), industry (a thin titanium chapter beside an aerospace priority), client (growth lines that have no logged physical scale) |
| Owner | material-researcher |
| Effort | large |

Section 4.1 is the standard for stages and for showing the arithmetic. Do not paste the nickel identity into the other metals. Chromium and molybdenum already carry a 2025 mine figure and, for molybdenum, a US balance and an oxide price. Fill gaps there. Do not lengthen them for their own sake.

For cobalt, titanium, tungsten, zirconium, copper, aluminium and manganese, one tight paragraph each: one dated mine or mineral figure, one refined or intermediate figure, one commercial form a mill could ship, one price that names its stage, and the two or three producers that matter. Where a European mill apparent consumption cannot be logged, say that in one sentence and give the USGS or Comtrade figure that does exist. Delete every `TODO(data)` line in sections 4.2, 4.5, 4.6 and 4.7. A submitted chapter does not contain working notes.

Move the aviation cobalt use of 11,499 tonnes in 2025, the 73 percent commercial share, the Democratic Republic of the Congo share of mine supply (about 73 percent, about 230 thousand tonnes of 310 thousand tonnes) and the quota fact into section 4.2. Section 5.4 points back and treats 11,499 tonnes as a cobalt indicator.

Titanium is the metal that cannot stay a caveat. The same engine makers buy titanium mill product, and the constraint is sponge and approved melt, not the nickel flat balance. Keep the refusal to invent a European mill balance. Medical zirconium stays at the OXINIUM point in fix 4. Copper and aluminium plate workings stay out of the recommendation until the same three leg standard is met. The working notes may remain in `research/`.

Tube: log PRODCOM sold production, imports and exports for nickel tube, or write in sections 4.1, 5.2 and 5.5 that there is no tube capacity recommendation until the three legs exist. Subsea tube and chemical tube then stay options with no tonnes.

Prices are part of Supply. Molybdenum oxide is not the only price in Chapter 4.

## 8. Correct the aerospace product route

| Field | Entry |
| --- | --- |
| Fix | Split the offer into billet, approved sheet and weld wire, and treat a 2025 shortage as a second source conversation for a grade the mill already makes. |
| Section | `sections/05_4_aerospace.md`, Table 7, the sector close (after fix 4), the aerospace rows of `sections/08_recommendations.md` |
| Type | logic |
| Raised by | industry (the section a technical director reads first), TUM (Safran is named without saying who already holds the approval) |
| Owner | sector-analyst |
| Effort | medium |

Hot gas path blades are cast, single crystal or directionally solidified, from Howmet and PCC. A wrought mill does not sell blade bar into LEAP. Discs and rings are billet, then a forger. In Europe that forger is Aubert & Duval. Qualified melters already on the approved supplier list include ATI, Carpenter, Special Metals and Aubert & Duval. Combustor and casing sheet is Haynes 188, 230, 625, X and similar. Haynes is Acerinox High Performance Alloys, so the competitor and the benchmark portfolio are the same group. The offer is billet for forged discs through a named forger, sheet only where this mill is already approved, and weld wire for shop visits. Powders and NASA GRX-810 move to a watch item. GRX-810 is a laboratory alloy with its own atomisation route, not a powder volume for 2035.

Put MTU and Pratt & Whitney on the buyer list beside GE Aerospace, Safran and Rolls-Royce. Approval for a rotating grade is AMS, NADCAP and an engine test, measured in years. A shortage in 2025 is weld wire and a second source conversation. It is not an entry ticket to a LEAP disc.

GE and Safran propulsion margins are OEM margins on shop visits. The mill sees weld wire, some replacement hardware and the original billet. Carpenter at 27.7 percent and ATI forgings at 23.6 percent are cycle margins. ATI standard alloy products at 16.3 percent is the closer comparison for a new source. Limit ceramic matrix composites to the hottest static parts.

Competitor names for this section are the aerospace row in fix 3. Do not repeat a second, conflicting list.

## 9. Apply the eight criteria on one page, without a weighted score

| Field | Entry |
| --- | --- |
| Fix | Score the priorities in words against the criteria Chapter 3 already names. |
| Section | `sections/08_recommendations.md` (8.1), criteria list in `sections/03_framework_and_methodology.md` |
| Type | logic |
| Raised by | TUM (the criteria are named and then skipped), client (the board cannot see why medical loses the ranking) |
| Owner | strategist |
| Effort | medium |

One comparison table. Rows are market attractiveness, growth to 2035, strategic fit, competitive intensity, technology attractiveness, customer attractiveness, entry barriers and differentiation potential. Columns are aerospace bar, approved sheet and repair wire, chemical plate and weld products, electrical strip and wire, and one column for keep and do not fund covering oil and gas, automotive and medical. High, medium or low in words. Any cell that claims a fact cites one fact. Competitive intensity on aerospace has to say that ATI takes about 68 percent of sales from aerospace and defence and Carpenter about 65 percent, and that Acerinox High Performance Alloys finished 47 thousand tonnes in 2025. Entry barriers have to set a multi year rotating and sour service path against a chemical fabricator trial that can close inside a year. State that no composite score is published because 2025 shipment shares were not available. Weights stay in the project model. This table uses the stop list from fix 4. It does not invent a second ranking.

## 10. Size the 24 month roadmap with two clocks, a cash cap and a kill rule

| Field | Entry |
| --- | --- |
| Fix | Give each gate an owner, an input that is already in the report, a decision that does not wait for a full data room, and a result that kills the trial. |
| Section | `sections/08_recommendations.md` (8.2), aligned with Appendix A4 |
| Type | logic |
| Raised by | client (no euros, no kill number), industry (one trial clock and one surcharge clause cover two different sales), TUM (gates are timed and not sized) |
| Owner | strategist |
| Effort | medium |

Months 0 to 3 test the European bar position from fix 2 against the client's bar book, and take glow plugs off the growth list now. Months 3 to 12 cap the qualification list at a stated number of accounts and a stated sample budget. The report currently proposes neither, so propose both and label them team planning choices, not market facts. Months 12 to 24 release finishing capacity only against a stated contribution per bottleneck hour under the Chapter 7 downside, and only after a repeat order.

Two clocks. Fabricated chemical equipment can be trialled inside a year. Rotating parts and sour service OCTG stay on a multi year approved supplier path. A 3 to 12 month trial does not cover a disc.

Kill rules in the same list. No second sample without a quantity. No finishing capital without a repeat order and a downside case that clears the hurdle. No powder or electrolyser spend without a financed programme. The hurdle rate stays the company's. The memo shows the number used. Do not invent one.

Write the price the way the invoice works. Nickel alloy plate is a conversion price plus a monthly alloy adjustment on the nickel, molybdenum, chromium, cobalt, tungsten and niobium in the grade, plus extras for width, testing, PMI and NDT. The stainless invoice, base plus alloy surcharge, is a different document. Say who carries nickel, molybdenum and cobalt between order and invoice, and whether scrap returns to the same mill. Ask for contribution per bottleneck hour in the first 90 day sales map, in the company's own grade and form codes. Name the routes and keep them distinct: VIM plus VAR for rotating grades, VIM plus ESR for corrosion plate, a stainless AOD route for Crofer and for 5 to 12 percent nickel grades.

Appendix A4 remains the list of internal facts still required. It is not a reason to postpone the external choices in fixes 2 and 4. The first gate uses the trade result and the stop list. It does not only send the reader to collect sales.

## 11. Make Chapter 6 report the corridors

| Field | Entry |
| --- | --- |
| Fix | Give partner, year and net position for the codes tied to the three priorities. |
| Section | `sections/06_trade.md` |
| Type | data |
| Raised by | TUM (sourcing dependence is the Trade dimension and is missing), client (the external half of the map is which tonnes are in play and who finishes them) |
| Owner | material-researcher |
| Effort | medium |

Chapter 6 currently restates Table 10 and the nickel flat balance. For HS 7505, 7506 and 7507, and for the cobalt, titanium, welding and aero engine codes already tied to the priorities, give the reporter, the year, the top partners and the net position from the clean extracts. Keep the pure metal versus alloy caveat from fix 1. Do not narrate the 57.8 million kilogram identity again. OECD ICIO intermediate use (USD 220 billion into electrical equipment and USD 109 billion into motor vehicles in 2022) stays caveated. It does not measure a corridor.

The capacity sentence in this chapter has to match fix 2 word for word in substance. A flat seller faces a mixed code the Union already exports. A bar seller faces a logged net import that is still a rounded estimate, with UK supply outside the customs territory.

## 12. Clear the remaining fact check items

| Field | Entry |
| --- | --- |
| Fix | Correct the medium and low findings that are not already inside fixes 1, 2, 5 and 6. |
| Section | `sections/05_3_energy_environment.md`, `sections/05_6_electronics_electrical.md`, `sections/05_7_medical_technology.md` (Table 8), `data/sources.csv` row `AC_METHOD`, Carpenter sentence in `sections/05_7_medical_technology.md` |
| Type | data |
| Raised by | fact check |
| Owner | writer |
| Effort | small |

Electricity. Replace 4.3 percent growth in 2024 with the Electricity 2026 revision of 4.4 percent. Record 3 percent growth in 2025. Replace the 3.9 percent path over 2025 to 2027 with the 2026 edition's forecast of 3.6 percent a year over 2026 to 2030. Drop the 85 percent developing economy share unless it is rechecked against that edition.

Hydrogen prose in section 5.3. State 4.3 million tonnes as the committed class. Describe just over 6 million tonnes only as the conditional case. Demand above 100 million tonnes, low emissions output of about 1 million tonnes, an announced pipeline of 27 million tonnes, and installed electrolysis above 4 GW can stay. Fix 6 uses the same split.

Medical. Replace 28 countries and 2.7 million procedures with the logged set: 2,751,272 hip and knee procedures for members reporting both, and a constant set compound rate of 3.36 percent a year from 2013 to 2023 (1,797,396 to 2,501,707). If a 2035 implant count is kept, apply that logged rate or drop the projection. Do not cite 158 and 116 per 100,000 as Health at a Glance 2025 narrative figures unless a page is logged. Germany's 2023 counts (292,143 hips and 223,133 knees) and the Lithuania count change can stay. Write the range as 2013 to 2023. Carpenter medical sales of USD 224 million exclude surcharge (USD 278 million including surcharge, down 21 percent).

Electronics. Semiconductor sales of USD 795.6 billion in 2025, up 26.2 percent, can stay. Label USD 630.5 billion as implied by the printed 2025 level and the printed growth rate. It is not a printed 2024 cell.

Source log. Point `AC_METHOD` at the PRODCOM database page or at the clean file's method note. It is the only cited data id with an empty URL.

Do not mark the unchecked claims as confirmed or as wrong. They were not reopened: the Society of Japanese Aerospace Companies figure of about USD 13.5 billion, the NASA GRX-810 life claim, the 2,700 degree Fahrenheit ceramic claim, the WSTS computer and industrial growth split, the Cefic sales shares, the Japan device totals, the China device market of CNY 1.22 trillion, and the October 2026 parliamentary vote. Leave them out of any new calculation.

## 13. Give energy, chemicals and electronics a numbered table and three spotlight facts

| Field | Entry |
| --- | --- |
| Fix | Make the seven sectors comparable on the page. |
| Section | `sections/05_3_energy_environment.md`, `sections/05_5_chemical_processing.md`, `sections/05_6_electronics_electrical.md` |
| Type | design |
| Raised by | TUM (breach of the sector rule), client (sector tables are activity dashboards where they exist) |
| Owner | sector-analyst |
| Effort | medium |

Add a numbered table in the same shape as Tables 3, 5, 7 and 9, with an italic source line. For each sector, three sentences that name a buyer or fabricator, a site or region, a year, a form and a metal. Where the public record names the alloy and not the account, say the account is unconfirmed and still name the specification, the form and the competing grade. Alloys already in the draft (Nickel 201, Crofer 22, Alloy 59, C-276, 625, 29-18, 42) stay. Buyers that are only "stack makers", "fabricators" or "stampers" do not meet the spotlight standard. Keep the chemical chapter's grade list. It is the most credible sector text and should gain a table, not a new story.

## 14. Open Chapter 1 on the decision, and make Chapter 9 the same choice in shorter form

| Field | Entry |
| --- | --- |
| Fix | Put the ranking, the scale, the capacity rule and the stop list in the first page of Chapter 1. |
| Section | `sections/01_introduction.md`, `sections/09_conclusion.md` |
| Type | logic |
| Raised by | client (fifteen minutes is not enough if the choice waits until Chapter 8) |
| Owner | writer |
| Effort | small |

Do this after fixes 1 to 4, so the opening matches the repaired argument. The table of contents has no executive summary, so the decision lives inside Chapter 1. Open with the three priorities, the basket from fix 1, the capacity rule from fix 2, the stop list from fix 4, and the 24 month gate from fix 10. Keep the stage explanation after that. Chapter 9 repeats the same choice in shorter form. It does not introduce a different ranking, and it does not call 57.8 million kilograms the specialty layer.

## 15. Put Chapter 5 in one voice and clear the house style marks

| Field | Entry |
| --- | --- |
| Fix | One register, one estimate label, italic source lines, and a lint clean pass. |
| Section | `sections/05_1_automotive.md`, `sections/05_2_oil_and_gas.md`, imperative passages in `sections/05_3_energy_environment.md`, `sections/05_5_chemical_processing.md`, `sections/05_6_electronics_electrical.md`, then a single pass on `sections/*.md` |
| Type | style |
| Raised by | TUM (writing at 3.0, and the instruction to do this after the facts), client (chapters 5.1, 5.2, 5.4 and 5.7 switch voice) |
| Owner | style-editor |
| Effort | medium |

Run this last among the prose fixes so the line edit happens once. Rewrite sections 5.1 and 5.2 so each paragraph takes up the previous claim and hands the reader to the next, in the voice of Chapters 3 and 8. Turn "Target", "Prioritise" and "Require" in sections 5.3, 5.5 and 5.6 into "the company should". Use one estimate label, "team estimate", in place of "our estimate", "our assessment" and "team calculation". Make every table source line italic, including Tables 1, 3, 4, 5, 7, 10 and 11. Remove the semicolon in Table 7. Write ranges as 2013 to 2023. Unhyphenate Nickel-iron, hot-section, 3D-printed, corrosion-resistant, High-volume and Cobalt-chromium where the official name allows it. Alloy C-276 stays. Point new figures at source log markers. Replace Table 1's source line "Project framework" with a real source or drop the line. Run `python3 .claude/skills/house-style/lint.py sections` and clear every violation. Do not change a number while editing the line.

## 16. Add figures only where they replace repeated prose

| Field | Entry |
| --- | --- |
| Fix | One flat versus bar comparison and one scenario fan, each with a source line, and only if the same comparison is deleted from the later chapters. |
| Section | `sections/06_trade.md`, `sections/07_scenarios.md` (7.2). The stage ladder is the table in fix 1, not a second exhibit. |
| Type | design |
| Raised by | TUM (no figure in the graded draft), client (the message of Table 10 sits only in the prose) |
| Owner | data-modeler |
| Effort | medium |

The basket table in fix 1 is the scale exhibit. Do not draw it again. A chart of the EU flat net export against the EU bar net import, titled as a claim and footnoted with the rounding band and the mixed code, may replace the verbal restatement. A fan of Table 11 for the seven industries may replace the qualitative recital in section 7.2. Each figure has a source line and readable units. If either chart would repeat the table and cost a page, reject it in `reviews/round_1/applied.md` and keep the table. Files under `report/fig/` that are not referenced from `sections/` do not count.

## Coverage

| Review item | Fix |
| --- | --- |
| Industry basket, unit values, Outokumpu timing, melt versus output | 1 |
| Client scale table and mixed code upper bound | 1 and 2 |
| TUM metals 4.2 to 4.7 and the cobalt facts left in aerospace | 7 |
| Chapter 8 flat surplus versus bar deficit, codes, UK and HS 7502, "engine only" wording, industrial gas turbines | 2 |
| Sector closes, double counted magnetic alloys, tube, stop list | 4 |
| VDM approvals and one Acerinox line | 3 |
| Fact check high: USD 670 billion, GE 25 percent period, USD 217 billion | 5 |
| 2035 rates, horizons, aerospace hardware versus shop visits, hydrogen 4.3 versus 6 | 6 |
| Eight criteria | 9 |
| Roadmap, two clocks, surcharge, kill rule | 10 |
| Chapter 6 corridors | 11 |
| Remaining fact check medium and low | 12 |
| Missing sector tables and spotlights | 13 |
| Decision on the first page | 14 |
| House style | 15 |
| Figures | 16 |
| Aerospace route, blades, GRX-810, CMC scope | 8 |

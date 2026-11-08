<!-- supersedes: nothing (first creation of the nickel material note); linked from: .claude/skills/research-protocol/SKILL.md (note path research/materials/<metal>.md) and the material-researcher task; user instruction: "NOTES ONLY. Do not edit sections/. Do NOT run tools/data/fetch.py. Write research/materials/nickel.md (full note template) and research/materials/nickel_trade.md." -->

# Nickel

Research note for chapter 4.1 and the nickel rows of chapter 6. Figures are stated with the stage they measure. Mine figures are contained nickel in ore. Primary figures are smelted or refined nickel units (ferronickel, nickel pig iron, cathode, sulphate and related products) as INSG defines them. Mill figures are gross weight of plate, sheet, strip, foil, bar, wire or tube, not contained nickel. VDM Metals and Haynes are one Acerinox group and are not counted as two competitors. Source rows for the main figures are in research/materials/nickel.sources.csv. Trade detail is in research/materials/nickel_trade.md.

## Key findings

1. World mine production of contained nickel was 3.71 million tonnes in 2024 and an estimated 3.90 million tonnes in 2025 [NI_USGS_MINE_W_2024, NI_USGS_MINE_W_2025]. Indonesia accounted for 2.31 million tonnes in 2024 and an estimated 2.60 million tonnes in 2025, about 62 percent and about 67 percent of those rounded world totals [NI_USGS_MINE_ID_2024, NI_USGS_MINE_ID_2025]. The country figures for 2025 are estimates and do not add exactly to the rounded world total. Reserves are a stock, not a flow: Indonesia holds 62 million tonnes of contained nickel against a world total stated as more than 140 million tonnes [NI_USGS_RES_ID_2025]. Data are in data/clean/usgs_mcs2026_nickel.csv.

2. Primary nickel is a different stage from the mine. The International Nickel Study Group, in its 13 October 2026 press release, puts world primary production at 3.589 million tonnes in 2024 and 3.875 million tonnes in 2025, and usage at 3.473 million tonnes and 3.577 million tonnes [NI_INSG_PROD_2025, NI_INSG_USE_2025]. The stated surpluses are 116 thousand tonnes in 2024 and 299 thousand tonnes in 2025 [NI_INSG_BAL_2025]. The same release forecasts a surplus of only 19 thousand tonnes in 2026 (production 3.868 million tonnes, usage 3.849 million tonnes) and 70 thousand tonnes in 2027 (production 4.071 million tonnes, usage 4.002 million tonnes) [NI_INSG_BAL_2026]. INSG says the estimates do not adjust for possible disruptions and that Indonesian production is uncertain. https://insg.org/wp-content/uploads/2026/10/pressrel_INSG-Press-Release-October_2026md92nd71j.pdf

3. Most primary units are not class 1 metal. In the INSG article based on the October 2025 meetings, combined Chinese and Indonesian nickel pig iron is forecast at 2.05 million tonnes in 2025 and 2.17 million tonnes in 2026, against primary production of 3.81 million tonnes in 2025 in that same vintage, so NPI in those two countries is just over half of primary supply [NI_INSG_NPI_2025]. Indonesia's primary output in that vintage is 1.9 million tonnes in 2025 and 2.1 million tonnes in 2026, about 51 percent of world primary output by 2026, including NPI, nickel sulphate and nickel cathode. The October 2026 press release revised the world totals and did not republish this product split. Class 1, for the London Metal Exchange, is primary nickel of at least 99.80 percent purity in cathodes, briquettes, pellets or rounds, in 6 tonne lots [NI_LME_SPEC]. Nickel pig iron, ferronickel and matte are not that contract. https://www.lme.com/metals/non-ferrous/lme-nickel/contract-specifications

4. The cash price has fallen from the 2022 peak and the two price series agree. The World Bank Pink Sheet nickel series averages 25,834 US dollars per metric ton in 2022, 21,521 in 2023, 16,814 in 2024 and 15,162 in 2025 [NI_WB_AVG_2022, NI_WB_AVG_2024, NI_WB_AVG_2025]. USGS reports LME cash averages of 25,815, 21,495, 16,812 and an estimated 15,000 for those four years [NI_USGS_LME_2024, NI_USGS_LME_2025E]. The 2024 gap is 2 dollars. The 2025 gap is an estimate versus a full twelve month average. Monthly Pink Sheet prices in 2025 stayed between 14,671 and 16,066 dollars per metric ton (data/clean/worldbank_pinksheet_monthly.csv).

5. The 2026 balance is not settled, because the study group revised it sharply and a large producer still sees a wide surplus. The October 2025 INSG meetings had forecast a 2026 surplus of 261 thousand tonnes (production 4.08 million tonnes, usage 3.82 million tonnes). The October 2026 release cuts that surplus to 19 thousand tonnes, mostly by lowering production. Nornickel, in coverage of its 2025 results, expects a surplus of about 275 thousand tonnes in 2026 if Indonesia keeps the status quo, after about 240 thousand tonnes in 2025, with 2025 supply of 3.86 million tonnes and demand of 3.62 million tonnes (research/companies/nornickel.md). The study group figure is the one used for the balance. The producer figure shows how wide the range is if the ore quota does not bind.

6. Stainless steel is still the first use, and it is measured in gross steel tonnes, not nickel units. worldstainless reports melt shop production of 64.157 million tonnes in 2025, up 2.1 percent, of which China produced 40.868 million tonnes and the European Union 5.659 million tonnes [NI_WS_MELT_2025]. The same table revises 2024 from the earlier 62.621 million tonne release to 62.821 million tonnes. First half 2026 production was 32.964 million tonnes, up 5.0 percent on the first half of 2025 [NI_WS_MELT_H1_2026], which matches the INSG statement that worldstainless reported 5 percent growth in the first half of 2026. INSG, in the December 2025 market article, says the stainless sector accounts for just under 70 percent of primary nickel use, and that battery use dipped in 2025 because of lithium iron phosphate and a shift toward plug in hybrids. https://worldstainless.org/media/press-releases/stainless-steel-melt-shop-production-increases-by-2-1-in-2025/

7. German and EU mill trade in flat nickel products is measurable, and it is not the same thing as class 1 feed. In 2024 Germany exported 17,775 tonnes of HS 7506 plate, sheet, strip and foil, worth 578 million US dollars, after 14,237 tonnes and 580 million dollars in 2023 [NI_CT_DE_7506_2024_T, NI_CT_DE_7506_2023_T]. Eurostat PRODCOM 24452200 puts German exports of the same product family at 18,087 tonnes and 590 million euro [NI_PC_DE_SHEET_X_2024]. The tonne gap is 1.8 percent. Export unit values sit near 32,500 dollars or euro per tonne, about double the 2024 LME cash price, which is the fabrication premium on a mill product. The heading does not split pure nickel from nickel alloy, and it does not report contained nickel. Unwrought nickel (PRODCOM 24451100 and HS 7502) is not in the files that could be used. data/clean/comtrade_7506_2023-2024.csv

8. High nickel mill products are a small tonnage inside a large stainless system, and one buyer publishes its nickel units. Acerinox reports group melt shop output of 1,866 thousand tonnes in 2025 and High Performance Alloys melt shop output of 83 thousand tonnes, with finishing of 47 thousand tonnes and HPA sales of 1,683 million euro [NI_ACX_HPA_2025]. A team calculation on those reported figures puts HPA at about 4.5 percent of group melt tonnes (83 divided by 1,866) and about 29 percent of group sales (1,683 divided by 5,781). VDM Metals and Haynes are that one division. ATI reports nickel use of about 70 million pounds in 2025, and that a 1 dollar per pound move equals about 70 million dollars of cost [NI_ATI_NI_LB_2025]. A team conversion at 2,204.6 pounds per tonne is about 31,800 tonnes of nickel units at one US melter. That is not a market size.

9. Policy on Indonesian ore is the swing factor for supply, and the quota is ore, not metal. On 29 October 2026 the energy ministry said the revised 2026 RKAB nickel ore quota was 290 million to 300 million metric tons, up from an initial 260 million to 270 million tons [NI_RKAB_2026_REV]. INSG's October 2026 release confirms that the 2026 quota is lower than the 2025 quota, without stating the tonnage. No ore grade was opened, so these tonnes are not converted to contained nickel. The same official's figure of about 750,000 tonnes of excess LME and SHFE inventory is not an exchange print. INSG's own combined LME and SHFE stock figure is 289,500 tonnes at the end of October 2025 [NI_INSG_STOCK_2025].

10. Through 2035 the official outlooks do not show a nickel only tonne path that could be read off the page, and they do not describe a copper style structural deficit under current policies. The IEA World Energy Outlook 2025 says announced projects are broadly sufficient for nickel in the Stated Policies Scenario and that shortfalls remain in the Net Zero Emissions Scenario (data/raw/WorldEnergyOutlook2025.pdf, page 353). The Global Critical Minerals Outlook 2026 outlook page groups nickel with graphite and rare earths in a 50 to 90 percent demand growth range and says the base case sees slight supply gaps for nickel, while a high production case would cover demand [NI_IEA_GCMO_GROWTH]. The chart values in tonnes were not on the HTML page, and the PDF is not in data/raw/iea. https://www.iea.org/reports/global-critical-minerals-outlook-2026/outlook

## Production

### Mine

USGS Mineral Commodity Summaries 2026 reports mine production as contained nickel, in metric tons. The 2025 column is estimated. The world total is rounded. Country rows below are the full USGS list in data/clean/usgs_mcs2026_nickel.csv.

| Country | Mine production 2024, tonnes contained | Mine production 2025, tonnes contained, estimated | Reserves, tonnes contained |
| --- | ---: | ---: | ---: |
| Indonesia | 2,310,000 | 2,600,000 | 62,000,000 |
| Philippines | 354,000 | 270,000 | 4,800,000 |
| Russia | 205,000 | 200,000 | 8,300,000 |
| Canada | 125,000 | 140,000 | 2,200,000 |
| New Caledonia | 116,000 | 140,000 | 7,100,000 |
| China | 115,000 | 120,000 | 4,400,000 |
| Australia | 98,000 | 45,000 | 25,000,000 |
| Brazil | 67,500 | 70,000 | 16,000,000 |
| United States | 7,490 | 10,000 | 340,000 |
| Other countries | 308,000 | 290,000 | more than 9,100,000 |
| World | 3,710,000 | 3,900,000 | more than 140,000,000 |

Australia's reserve row carries a USGS note that Joint Ore Reserves Committee compliant or equivalent reserves were 11 million tons, against the 25 million tonne reserve figure in the table. The 2025 mine estimate for Australia, 45,000 tonnes, is less than half of the 98,000 tonnes reported for 2024. The file does not name the mines behind that drop. Philippines mine output is also estimated lower, from 354,000 tonnes to 270,000 tonnes, while Indonesia's mine estimate rises from 2.31 million tonnes to 2.60 million tonnes.

INSG, writing up the October 2025 meetings, said Indonesia accounted for an estimated 66 percent of world mine output in 2025, with the share projected near 68 percent in 2026, and that world mine production grew 1.8 percent in 2024. That 66 percent lines up with the USGS estimate of 2.60 million tonnes inside a rounded 3.90 million tonne world total. The two sources are not the same vintage and not a substitute for each other. USGS is the country table used here. https://insg.org/index.php/about-nickel/the-market-2025-12/

United States mine production is small beside US use. USGS reports 7,490 tonnes in 2024 and an estimated 10,000 tonnes in 2025. US refinery production as a byproduct is withheld. Primary imports were 105,000 tonnes in 2024 and are estimated at 100,000 tonnes in 2025. Apparent primary consumption is estimated at 90,000 tonnes in 2025 and apparent total consumption, including purchased scrap, at 220,000 tonnes [NI_USGS_US_APP_2025].

### NPI and matte

Nickel pig iron and ferronickel are class 2 products aimed at stainless melting. Matte and mixed hydroxide precipitate are intermediates that can be refined to sulphate or to class 1 cathode. INSG's December 2025 article, using the October 2025 meetings, is the split that could be opened. It was not repeated in the October 2026 press release, so the tonnes below are that earlier vintage.

Combined Chinese and Indonesian NPI is forecast at 2.05 million tonnes in 2025 and 2.17 million tonnes in 2026. China's own NPI has been declining since 2019, and Indonesian NPI has been the growth. In that article Indonesia's primary production, which includes NPI plus sulphate and cathode, is 1.9 million tonnes in 2025 and 2.1 million tonnes in 2026. Sulphate and cathode production in Indonesia began in 2023. The majority of Indonesian primary output is described as intended for export.

The same article gives directory capacity, which is not expected output. Global primary nickel capacity is estimated at 5.49 million tonnes, with about 64 percent of that capacity in operation on 2024 data [NI_INSG_CAP_2025]. Installed capacity is 2.17 million tonnes in China and 1.78 million tonnes in Indonesia. Committed projects add 447 thousand tonnes of ore or concentrate, 2.02 million tonnes of intermediate products, and 3.34 million tonnes of primary nickel. Indonesia accounts for 1.9 million tonnes of the new intermediate capacity, as mixed hydroxide precipitate from high pressure acid leaching and as matte made by converting NPI, and for 1.95 million tonnes of new primary capacity in NPI, cathode and sulphate. China accounts for 0.96 million tonnes of new primary capacity, mainly cathode and sulphate. INSG counts 565 operating mines in 31 countries and 273 operating smelters and refineries in 32 countries.

Nameplate capacity of 5.49 million tonnes, plus committed primary additions of 3.34 million tonnes, is far above the October 2026 production forecast of 4.071 million tonnes in 2027. The directory is a stock of plants. The forecast is the tonnes INSG expects to be produced. They should not be added together or treated as a surplus of usable class 1 metal.

Tsingshan is the industrial actor behind a large part of Indonesian NPI and the Weda Bay ore joint venture with Eramet. The company note does not contain a verified group total for NPI, matte or stainless (research/companies/tsingshan.md). A 120 thousand tonne per year HPAL figure attributed to the Blue Flame project is left unused here because ownership was not confirmed in that note.

### Class 1

Class 1 in this note means LME deliverable primary nickel: minimum 99.80 percent, shapes limited to full plate and cut cathodes, briquettes, pellets and rounds, lot size 6 tonnes, quoted in US dollars per tonne [NI_LME_SPEC]. The physical section of the LME specification page cites ASTM B39-79 (2023) or GB/T 6516-2010 grade Ni9990. The futures summary on the same page still cites B39-79 (2008). The purity and the shapes are the point that matters for an alloy melt shop. NPI and ferronickel cannot be delivered against that contract. Matte has to be refined first.

No world total for cathode, briquette and pellet output was in the October 2026 press release. Company guidance is therefore reported as company output, not as a share of the market.

Nornickel guides 193,000 to 203,000 tonnes of nickel in 2026, and reported first half output of 85 thousand tonnes, down 2 percent (research/companies/nornickel.md). The company note describes the commercial forms as cathode, briquettes and powder, which fit class 1 melting. The primary production report was not opened in that pass, so the page number is still open. Glencore guides 70,000 to 80,000 tonnes of own sourced nickel in 2026, with 54,600 tonnes produced from January to September, and the company note describes the relevant forms as briquettes and cathode (research/companies/glencore.md). The Glencore PDF was also not opened in that pass. These two ranges together are on the order of 260,000 to 280,000 tonnes. That is a sourcing pool for class 1 units, not a world class 1 census.

INSG's stock discussion shows where visible class 1 metal sits. Combined LME and SHFE stocks were 289,500 tonnes at the end of October 2025, after a low near 231,000 tonnes in March 2025. Between January and September 2025, Chinese origin open tonnage on the LME rose by 82,400 tonnes against a total net increase of 74,000 tonnes, taking China's share of LME open tonnage from 47 percent to 67.85 percent. Russian material fell from 19 percent to 12.5 percent, Australian material from 17 percent to 9.5 percent, and Indonesian material was just under 5 percent for most of the period, reaching 10,700 tonnes by the end of September. Visible class 1 stocks have become a Chinese refined metal story. That is not the same as the ore and NPI system in Indonesia.

For a German melt shop the practical constraint on Russian class 1 metal is compliance and logistics, not the LME contract text. The Nornickel note says the company is not itself directly sanctioned, that some Western buyers avoid the metal, and that the deliverability of Russian brands and any EU import limit still need a legal source. That check is open.

### Mill product

Mill product is the stage the company sells: plate, sheet, strip, foil, bar, wire, tube and, for some competitors, powder and forgings. Eurostat PRODCOM measures sold production and trade of these forms in kilograms and euro. The figures below are read from data/clean/prodcom_2019-2024.csv as committed in 1eae77d. On 7 November 2026 the working copy of that file contained only the header. data/clean/prodcom_2023.csv, which is intact, matches the 2023 EU trade and sold production cells for 24452200, including exports of 31,966,424 kilograms.

Codes 24451100 (unwrought nickel) and 24451230 (nickel powders and flakes) have no published quantities or values for the EU or for Germany in that extract. The class 1 feed of a European remelter is therefore not visible in PRODCOM here.

For 24452200, nickel plates, sheets, strip and foil, EU sold production in 2024 is 1,171 million euro on a quantity of 80,911 tonnes, and the quantity and value flags are estimated. Dividing those two cells gives about 14,500 euro per tonne. German sold production in 2024 is 269 million euro on 30,561 tonnes, about 8,800 euro per tonne. Both unit values sit below the 2024 LME cash price of about 16,800 dollars per tonne, and the German unit value was already about 8,100 euro per tonne in 2022 when the LME price averaged about 25,800 dollars. Export unit values for the same code are about 32,600 euro per tonne for Germany and about 31,000 euro per tonne for the EU. The sold kilogram series is reported, and it is not used as contained nickel or as a revenue rate. A conversion only (tolling) value, or a mix of alloys whose gross weight is not nickel content, would produce a low unit value. Eurostat metadata was not opened to decide which. The export series is the one that agrees with UN Comtrade.

| Product, 2024 | EU quantity | EU value | Germany quantity | Germany value |
| --- | ---: | ---: | ---: | ---: |
| 24452200 plate, sheet, strip, foil, sold production | 80,911 t, estimated | 1,171 million euro | 30,561 t | 269 million euro |
| 24452200 exports | 37,478 t | 1,163 million euro | 18,087 t | 590 million euro |
| 24452200 imports | 14,400 t | 689 million euro | 17,901 t | 518 million euro |
| 24452100 bar, rod, profile, wire, exports | 2,697 t | 90 million euro | 1,501 t | 77 million euro |
| 24452300 tube, pipe, fittings, exports | 16,488 t | 430 million euro | 17,766 t | 534 million euro |

Bar and tube sold production for the EU in 2024 is rounded in the extract (2,500 tonnes and 100 million euro for bars, 21,000 tonnes and 280 million euro for tubes) and is not used as a precise physical balance. German sold production of bars is not published. German sold production of tubes has a 2024 value of 204 million euro and no published quantity. German bar exports at about 51,000 euro per tonne are the high unit value long product series in this extract.

Competitor mill capacity is alloy tonnes or furnace hardware, not contained nickel. Acerinox HPA (VDM and Haynes together) melted 83 thousand tonnes and finished 47 thousand tonnes in 2025. Outokumpu describes about 13 thousand tonnes of additional flat high nickel alloy capacity at Avesta, which is alloy product weight. Special Metals lists melt furnaces at Huntington, including two 70,000 pound electric arc furnaces and a 48,000 pound vacuum induction furnace, inside Precision Castparts, and does not publish a nickel tonne total (research/companies/special-metals.md).

## Trade

The full HS map, the partner table and the quota gap are in research/materials/nickel_trade.md. The only UN Comtrade extract on disk for nickel is German exports of HS 7506 in 2023 and 2024. Imports, other reporters, and HS 2604, 7501, 7502, 7504, 7505, 7507 and 7508 were not pulled. The public Comtrade preview quota was already exceeded on 7 November 2026, and fetch.py was not run.

What that one series shows is a mill product flow, not a raw material flow. German exports rose from 14,237 tonnes in 2023 to 17,775 tonnes in 2024 while the dollar value stayed near 580 million. A team calculation of unit value (export dollars divided by net weight) is about 40,700 dollars per tonne in 2023 and about 32,500 dollars per tonne in 2024. Subtracting the USGS LME cash average for the same year (21,495 dollars and 16,812 dollars) leaves a premium of about 19,200 dollars per tonne in 2023 and about 15,700 dollars per tonne in 2024. The premium is a team estimate, and it narrowed as the cash price fell. The largest 2024 values went to Austria, Italy, China, the United States and France. Austria took 4,044 tonnes, more weight than any other partner, at a lower unit value than the German average. The file does not say whether that is thicker plate, a distribution hub, or a related party flow.

EU PRODCOM trade in 24452200 shows the region as a net exporter of this form in 2024: 37,478 tonnes exported and 14,400 tonnes imported. Germany itself is nearly balanced in tonnes (18,087 exported, 17,901 imported) and is a net exporter in euro (590 million against 518 million). Import unit values into the EU are higher than export unit values (about 47,800 euro per tonne against about 31,000). The product mix inside the heading is not identified.

This does not measure sourcing dependence for class 1 feed. That dependence sits in unwrought nickel and in scrap, which are the USGS categories for the United States and which are missing for Germany. US primary import sources for 2021 to 2024 were Canada 44 percent, Norway 11 percent, Australia 8 percent, Brazil 7 percent and other countries 30 percent. US net import reliance was an estimated 41 percent of apparent consumption in 2025 including scrap, and USGS says that excluding scrap the reliance would be nearly 100 percent.

## Consumption

INSG primary usage is the world consumption measure used here. It was 3.473 million tonnes in 2024 and 3.577 million tonnes in 2025, and it is forecast at 3.849 million tonnes in 2026 and 4.002 million tonnes in 2027. Usage in this definition is primary nickel, so scrap is additional. The October 2026 release does not split usage by first application or by region.

The December 2025 article, October 2025 vintage, does. Stainless steel is just under 70 percent of primary use. Asia is 87.7 percent of primary use in 2025 and 88.2 percent in 2026, against 63 percent in 2010. China is more than 65 percent of world primary use in both years. Europe's usage fell in 2024 and was expected to fall a further 0.5 percent in 2025 before a 1.8 percent rise in 2026. Those regional rates were not updated in October 2026 and should not be applied to the newer world total without that update.

United States apparent consumption is the only official national total in the USGS file. The 2025 estimate is 220,000 tonnes total, of which 90,000 tonnes are apparent primary consumption and 130,000 tonnes are reported secondary consumption of purchased scrap. Reported primary consumption is estimated at 120,000 tonnes, which is a different concept from apparent primary consumption. Scrap is large enough that a US nickel strategy which ignores secondary units misstates the market. The same file says secondary estimates were revised after new data, so the scrap level is softer than the mine table.

OECD STAN is the industrial envelope, not nickel consumption. In data/clean/oecd_stan_P1.csv, German output of manufacture of basic metals (activity C24, current prices, national currency) was 103,831 million euro in 2019, 149,252 million euro in 2022 and 139,869 million euro in 2023 [NI_OECD_DE_C24_P1_2023]. Value added in data/clean/oecd_stan_B1G.csv was 21,001 million euro, 24,025 million euro and 27,778 million euro in those three years. There is no 2024 observation for Germany. C24 includes iron, steel and all non ferrous metals. A nickel mill product line is a small part of that output. The file also has no China.

## Applications

The first use split that was opened is the INSG statement that stainless steel is just under 70 percent of primary nickel consumption, with battery use lower in 2025 than the earlier growth path because of lithium iron phosphate chemistry and a move from battery electric vehicles toward plug in hybrids. The October 2026 press release says the same thing in qualitative form: stainless is expected to keep expanding through 2027, electric vehicle sales grow only modestly in 2026, and nickel's role in batteries has grown more slowly than expected. A numeric battery share for 2025 was not on the pages that were opened. A 2023 INSG factbook figure of about 65 percent for stainless and 16 percent for batteries was visible in search extracts of the factbook PDF and is not used as the current split, because the later article was the one read in full and the shares are not the same year.

worldstainless composition guidance was not fetched as a full text in this pass, so grade nickel ranges are not used as a calculation base. What is used is the melt shop tonnage, which is gross steel. Multiplying 64 million tonnes of stainless by an assumed nickel content would invent a nickel demand figure. The contained nickel in world stainless melt is left open until a worldstainless nickel ratio or an INSG first use table in tonnes is on disk.

The applications that match the company's product forms show up in competitor filings rather than in a world nickel balance.

Acerinox says that in 2025 oil and gas was sluggish for lack of new projects, chemical processing was significantly weaker, automotive and electronics were stable, and aerospace was better than 2024. Haynes, inside the same group, sells corrosion and heat resistant alloys such as HAYNES 282 and the C-276 family in sheet, plate, strip, tube, wire and bar. The order backlog comment in the 2026 half year points to defense, aerospace and industrial gas turbines for data center power (research/companies/haynes.md, research/companies/acerinox.md).

ATI's fiscal 2025 sales were 46 percent nickel based and specialty alloys. Aerospace and defense were 68 percent of sales, including commercial jet engines at 1,763 million dollars. The forms are premium melted billet, powder, disc forgings and flat rolled plate, sheet and strip. Named counterparties on long term agreements are GE Aviation, Safran, Rolls Royce and Pratt and Whitney (ATI annual report on Form 10-K for fiscal 2025).

Outokumpu's delivered tonnes are stainless steel, 1,751 thousand tonnes in 2025, not high nickel alloy. The relevant application move is the Avesta programme for flat products in the 5.5 to 12 percent nickel band, aimed at energy, oil and gas, electrical and electronics, and defence (Outokumpu annual report 2025 and the investor presentation of August 2026).

Carpenter's fiscal 2026 sales are 65 percent aerospace and defense, in bar, billet, wire and powder, with less overlap on flat products. The 207.9 million pounds sold are all products, not nickel units (Carpenter Technology Form 10-K).

Special Metals, inside Precision Castparts, supplies nickel alloys in billet, bar, rod, wire, flat products, tubulars, powder and welding products under the Inconel and Incoloy names. The Berkshire Hathaway Form 10-K does not separate Special Metals revenue.

Nippon Yakin is a flat product competitor in high nickel heat resistant alloys, with its own ferronickel step at Oheyama. The 2025 integrated report was not opened, so shipment tonnes are not taken from the profile's secondary figure.

## Market size

No world market value for high nickel mill products is stated. The methodology of this project does not assert an addressable market where the sources are not comparable. The figures that do exist measure different things and are kept apart.

The Eurostat sold production value for EU nickel plate, sheet, strip and foil was 1,171 million euro in 2024, on an estimated quantity whose unit value is below the metal price, as discussed under mill product. Adding the rounded EU values for bars (100 million euro) and tubes (280 million euro) would still be only an EU gross weight statistic for three PRODCOM codes, with unwrought nickel and powders missing, and with rounding. That sum is not published here as a market.

Acerinox High Performance Alloys sales of 1,683 million euro in 2025 are one group's revenue, covering VDM and Haynes, including conversion and alloy price, not a market. First half 2026 HPA sales were 729 million euro, down 18 percent, with EBITDA of 35 million euro. Outokumpu stainless sales were 5,468 million euro in 2025 on 1,751 thousand tonnes of stainless deliveries. ATI sales were 4,587 million dollars, of which nickel based and specialty alloys were 46 percent. None of these is a nickel market size. German basic metals output of 139.9 billion euro in 2023 is the OECD industry total for all basic metals.

The usable size statements for strategy are therefore physical and divisional. Primary nickel use is about 3.6 million tonnes and is mostly stainless. Class 1 is the smaller, LME specified slice, with two named suppliers guiding under 300 thousand tonnes combined and no world census. EU trade in nickel flat products is a net export flow of roughly 37 thousand tonnes against 14 thousand tonnes of imports. The alloy division of the closest peer is 83 thousand tonnes of melt and 1.7 billion euro of sales.

## Prices

The price that enters alloy surcharges is the LME cash price for class 1 metal, not the price of ore, NPI or mill product. Pink Sheet annual averages, calculated as the unweighted mean of the twelve monthly observations in data/clean/worldbank_pinksheet_monthly.csv, are the series used for 2019 to 2025. USGS LME cash is the cross check. Values are dollars per metric ton.

| Year | Pink Sheet average | USGS LME cash |
| --- | ---: | ---: |
| 2019 | 13,914 | not in the five year USGS window used here |
| 2020 | 13,787 | not in the five year USGS window used here |
| 2021 | 18,465 | 18,476 |
| 2022 | 25,834 | 25,815 |
| 2023 | 21,521 | 21,495 |
| 2024 | 16,814 | 16,812 |
| 2025 | 15,162 | 15,000, estimated |

INSG's price narrative for 2025, in the December 2025 article, is a path of daily or close prices rather than a monthly average. Cash seller started the year at 15,310 dollars per tonne, peaked at 16,460 in mid March, fell to 13,815 in early April, and ended October at 15,055. A daily low of 13,815 can sit below the lowest Pink Sheet month (14,671) without contradicting the monthly average of 15,162. The article also records LME nickel volumes from January to October 2025 at 86,700 contracts a day, above the 2021 average, so the contract is trading again after the March 2022 suspension. Off warrant stocks were 70,190 tonnes at the end of October 2025.

Acerinox says the nickel price decline is expected to affect alloy surcharges and transaction prices, which is the transmission from this cash series into mill product revenue (research/companies/acerinox.md). The German HS 7506 unit value moved with the cash price between 2023 and 2024, and the premium over cash narrowed, as calculated in the trade section.

The ore market is separate. The RKAB quota is in millions of tonnes of ore. It can tighten smelter feed and still leave LME warehouses well stocked, which is what the INSG stock level and the ministry's later comment are both pointing at, on different vintages. A single nickel price does not clear ore, NPI, matte, class 1 and mill product at once.

## Capacity and supply

Four capacity layers should stay separate.

Mine supply is the USGS country table. The 2025 estimate is 3.90 million tonnes contained, with Indonesia at 2.60 million tonnes. The reserve stock is large relative to one year of mine output. Indonesia's 62 million tonnes of reserves are the dominant national figure. That does not mean annual ore output is unconstrained. The 2026 RKAB is an administrative cap on ore, revised to 290 million to 300 million metric tons, and it is not a metal cap.

Primary smelting and refining capacity in the INSG directory is 5.49 million tonnes, about 64 percent utilised on 2024 data, concentrated in China (2.17 million tonnes installed) and Indonesia (1.78 million tonnes). Committed additions are heaviest in Indonesian intermediates (1.9 million tonnes of MHP and matte) and in Indonesian and Chinese primary products (1.95 million and 0.96 million tonnes). This is the NPI, matte and sulphate layer. The December 2025 article says that every region outside Asia recorded a decline in primary production in 2024, and that Oceania's primary production was expected to drop 39.4 percent in 2025. That lines up in direction with the USGS estimate that Australian mine output fell from 98,000 tonnes to 45,000 tonnes.

Class 1 supply from the two companies whose guidance was in the profiles is Nornickel at 193,000 to 203,000 tonnes and Glencore at 70,000 to 80,000 tonnes for 2026. Visible exchange inventory of class 1 metal was 289,500 tonnes on the LME and SHFE combined at the end of October 2025, with Chinese brands taking two thirds of LME open tonnage by September 2025. A 2026 claim of about 750,000 tonnes of excess exchange inventory, made by the Indonesian director general and reported on 30 October 2026, is a different number and a different date. It is not used as a stock measurement until an LME or SHFE table is opened.

Mill capacity is furnace and finishing tonnes at alloy producers. Acerinox is adding about 200 million dollars of US melting, forging and bar equipment across Haynes Kokomo and NAS Ghent, aimed at 2028, and has commissioned VDM strip, bar and remelt steps in Germany, with a powder atomizer at Unna scheduled for the second quarter of 2027. Outokumpu's Avesta addition is about 13 thousand tonnes of flat high nickel alloy, with a first remelt step early in 2028 and a possible melt shop at the end of 2029. ATI is spending to ramp a sixth nickel based superalloy and says it is not building a monolithic new asset. None of these projects changes the world mine balance. They change who can deliver qualified plate, strip, bar and billet.

## Outlook to 2035

The near term balance is the October 2026 INSG forecast: a 19 thousand tonne primary surplus in 2026 and a 70 thousand tonne surplus in 2027, after a 299 thousand tonne surplus in 2025. The revision from the previous meeting's 261 thousand tonne surplus for 2026 is large relative to the balance and small relative to a 4 million tonne market. INSG ties the uncertainty to Indonesian production. Nornickel's 275 thousand tonne surplus case is the status quo alternative. Both can be true as scenarios. They cannot both be the base case.

Stainless volume supports the usage side. worldstainless already printed a 5 percent rise in the first half of 2026, and INSG expects stainless to expand further into 2027. The European Union's 2025 melt was down 1.9 percent, to 5.659 million tonnes, so the growth is not a European growth story. China produced 40.868 million tonnes of the 64.157 million tonne world total in 2025.

Batteries are the swing in the demand mix, and both INSG and the IEA describe that swing as slower than earlier nickel narratives. The October 2026 INSG text says nickel in batteries has grown more gradually because of lithium iron phosphate. The IEA outlook page says cobalt demand to 2040 has been moderated by LFP, partly offset inside nickel manganese cobalt chemistries, and it puts nickel in a group with graphite and rare earths whose demand growth runs from 50 to 90 percent. That range is not a nickel only forecast and is not turned into tonnes here.

On supply, the World Energy Outlook 2025 (page 62) says geographic concentration in refining increased for nearly all key energy minerals from 2020 to 2024, particularly for nickel and cobalt. The average share of the top three refining countries across key energy minerals rose from about 82 percent to about 86 percent. That average is not nickel's own share. The Global Critical Minerals Outlook 2026 page states that the top refiners include Indonesia and China for nickel, and that nickel's midstream and downstream capacity outside those refiners lags the upstream, in the same pattern as graphite and cobalt. Page 249 of the World Energy Outlook says expected supplies of nickel, cobalt, graphite and rare earths catch up with demand under current policies if planned projects proceed, while copper still shows a potential 30 percent shortfall by 2035 in the Stated Policies Scenario. Page 353 says announced projects are broadly sufficient for nickel in that scenario and not sufficient in the Net Zero Emissions Scenario. The 2026 critical minerals outlook is slightly tighter in wording: the base case sees slight supply gaps for nickel, and the high production case covers demand. No percentage gap for nickel was printed in the text that was opened. The 2035 bar chart was not transcribed into tonnes.

The industrial implication through 2035 is a split market. Mine and primary tonnes stay concentrated in Indonesia and China, with a policy valve on ore that can move the annual balance by more than the residual surplus. Class 1 visible stocks are already dominated by Chinese brands. Western sulfide and ferronickel supply is the part that shrank in the USGS Australia estimate and in the INSG regional production comments. Mill product demand for aerospace and high nickel flat products is a qualified capacity story at ATI, the Acerinox HPA division, Outokumpu and Special Metals, and it is not settled by the LME surplus. A surplus of primary nickel, much of it NPI, does not mean a surplus of vacuum melted billet or of wide nickel alloy strip.

## Company evidence

VDM Metals and Haynes are reported only as the Acerinox High Performance Alloys division. Counting them as two competitors would double the same capacity.

Acerinox, fiscal year 2025 results, records group revenue of 5,781 million euro, group melt shop output of 1,866 thousand tonnes, stainless sales of 4,119 million euro and HPA sales of 1,683 million euro with EBITDA of 135 million euro. HPA melt was 83 thousand tonnes and finishing 47 thousand tonnes. The half year 2026 interim management report shows HPA sales of 729 million euro, down 18 percent, melt of 40 thousand tonnes, down 10 percent, and a comment that the nickel price decline feeds into alloy surcharges. VDM strip expansion, bar finishing, a new remelt shop and the Unna powder atomizer are the German mill steps. Haynes brings Kokomo plate, bar and vacuum melting and the Arcadia tube mill. The last Haynes stand alone annual report on Form 10-K is fiscal 2023, with revenue of 590 million dollars, and is not a current size.

Nornickel guides 193,000 to 203,000 tonnes of nickel for 2026 and a global surplus of about 275 thousand tonnes if Indonesian policy does not change. The integrated production report was not opened. The forms cited in the company note are cathode, briquette and powder. Direct purchase by a German melter remains a compliance question, not a tonne question.

Glencore guides 70,000 to 80,000 tonnes of own sourced nickel for 2026 and had produced 54,600 tonnes by the end of September. The note treats this as class 1 briquette and cathode supply, and not as an alloy competitor. The results PDF was not opened.

Eramet sells Weda Bay ore into the industrial park associated with Tsingshan, and ferronickel through SLN in New Caledonia. The integrated report 2025 was not opened. The note records an initial 2026 RKAB of 12 million wet tonnes at Weda Bay, a halt to ore mining when that quota was exhausted, and continued NPI production from stockpiles at the Tsingshan plant. The 2025 ore tonnage in the note is flagged for a possible unit error and is not used here.

Tsingshan is the NPI, matte and stainless producer whose output moves the class 2 balance. Group tonnes of NPI and matte were not found in a filing. The company is not a high nickel alloy mill competitor in the sources read.

ATI Inc. annual report on Form 10-K for fiscal 2025 is the clearest nickel unit disclosure among the melters: about 70 million pounds of nickel, surcharge pass through, and 46 percent of revenue in nickel based and specialty alloys. Capex was 281 million dollars in 2025. The Q3 2026 call describes the ramp of a sixth nickel based superalloy. Customers named on long agreements include GE Aviation, Safran, Rolls Royce and Pratt and Whitney.

Carpenter Technology Form 10-K for the year ended 30 June 2026 shows 3,124 million dollars of sales and 207.9 million pounds of products shipped, 65 percent of sales in aerospace and defense. The pounds are not nickel. Overlap with a flat products producer is partial.

Special Metals is inside Precision Castparts. The Berkshire Hathaway Form 10-K for 2025 describes nickel, titanium and cobalt alloys in standard mill forms and does not publish a Special Metals revenue or a nickel tonne figure. Furnace sizes at Huntington are on the company site cited in the profile.

Outokumpu annual report 2025 reports 5,468 million euro of sales and 1,751 thousand tonnes of stainless deliveries, plus a European stainless flat share of 28 percent. The investor presentation of August 2026 is the source for the Avesta high nickel flat programme of about 13 thousand tonnes and about 150 million euro. That is the point at which a stainless producer steps into the company's flat product space.

Nippon Yakin is the Japanese flat product competitor with an integrated ferronickel plant at Oheyama. The integrated report was not opened from this environment, and the shipment figure above 10,000 tonnes is left as an unverified secondary claim in the company note.

## Spotlight facts

1. In 2025 Acerinox, with VDM Metals in Werdohl, Altena and Unna and Haynes in Kokomo counted as one group, melted 83 thousand tonnes and finished 47 thousand tonnes in the High Performance Alloys division and booked 1,683 million euro of sales in nickel alloy strip, bar, wire, plate, tube and powder.
2. In 2025 ATI used about 70 million pounds of nickel at its US melt shops and stated that a one dollar per pound move equals about 70 million dollars of cost, in premium melted nickel alloy billet, powder and flat products supplied under long agreements to GE Aviation, Safran, Rolls Royce and Pratt and Whitney (ATI annual report on Form 10-K, page 37).
3. In 2024 Germany exported 17,775 tonnes of nickel plate, sheet, strip and foil under HS 7506, worth 578 million US dollars, with the largest values to Austria, Italy, China, the United States and France, a mill product flow whose German producers include VDM Metals although the trade statistic does not name the firm (data/clean/comtrade_7506_2023-2024.csv).
4. In 2026 Indonesia revised the national nickel ore RKAB to 290 million to 300 million metric tons of ore, while the Eramet and Tsingshan Weda Bay joint venture had an initial quota of 12 million wet tonnes and stopped ore mining when that quota ran out, with Tsingshan NPI continuing from stockpiles (Indonesia Business Post, 30 October 2026, and research/companies/eramet.md).
5. In its August 2026 investor presentation Outokumpu set out an Avesta programme of about 150 million euro to add about 13 thousand tonnes of flat high nickel alloy capacity in Sweden, with remelting aimed at early 2028 and a possible melt shop by the end of 2029, for energy, oil and gas, electronics and defence.

## Triangulation

| Number | Source 1 | Source 2 | Difference and choice |
| --- | --- | --- | --- |
| 2024 annual nickel cash price, dollars per metric ton | World Bank Pink Sheet average 16,813.96, twelve months in data/clean/worldbank_pinksheet_monthly.csv [NI_WB_AVG_2024] | USGS LME cash average 16,812 [NI_USGS_LME_2024] | Gap of about 2 dollars. The series are the same price. Pink Sheet is used for the full 2019 to 2025 path because 2025 USGS is a rounded estimate of 15,000 against a Pink Sheet average of 15,162. |
| 2025 Indonesia share of world mine output | USGS estimated mine production 2.60 million tonnes inside a rounded world total of 3.90 million tonnes, about 67 percent | INSG October 2025 meetings, estimated 66 percent of global mine output in 2025 | About one percentage point, and the INSG sentence is an earlier meeting. USGS is used for the country table. Both say Indonesia is about two thirds of mine supply. |
| Germany 2024 exports of nickel plate, sheet, strip and foil, gross tonnes | Eurostat PRODCOM 24452200, 18,087 tonnes and 590 million euro [NI_PC_DE_SHEET_X_2024] | UN Comtrade HS 7506, 17,775 tonnes and 578 million dollars [NI_CT_DE_7506_2024_T] | Tonne gap of 312 tonnes, or 1.8 percent. Values are in different currencies and are not forced together. Both are used. The product family is the same. |
| 2025 primary nickel surplus | INSG press release of 13 October 2026, surplus 299 thousand tonnes, production 3.875 million tonnes, usage 3.577 million tonnes | Nornickel company estimate of about 240 thousand tonnes, with supply 3.86 million tonnes and demand 3.62 million tonnes. Earlier INSG October 2025 meeting: surplus 209 thousand tonnes, production 3.81, usage 3.60 | Production is close across the three. Demand and the surplus are not. The October 2026 INSG balance is the one used. The older INSG vintage and the company estimate are kept to show the revision. |
| 2024 world stainless melt shop production | worldstainless release of 14 April 2025, 62.621 million tonnes | worldstainless release of 27 February 2026, 2024 revised to 62.821 million tonnes in the 2025 table [NI_WS_MELT_2025] | The later table is a revision of 200 thousand tonnes. The revised 62.821 million tonnes for 2024 and 64.157 million tonnes for 2025 are used. First half 2026 growth of 5.0 percent on the association data page matches the 5 percent cited by INSG in October 2026. |
| 2026 primary surplus forecast | INSG 13 October 2026, surplus 19 thousand tonnes | INSG October 2025 meetings, surplus 261 thousand tonnes, and Nornickel, about 275 thousand tonnes if Indonesia keeps the status quo | The study group cut its own 2026 surplus by about 240 thousand tonnes in twelve months, mainly by lowering production. The later INSG forecast is the base case. The Nornickel case is the policy alternative, not a second measurement of the same balance. |

## Source coverage

| Source | Status | Evidence |
| --- | --- | --- |
| UN Comtrade (tools/data/fetch.py comtrade) | used | data/clean/comtrade_7506_2023-2024.csv, Germany exports of HS 7506 only, 2023 to 2024, 155 rows. Other nickel HS codes were not pulled because the preview quota was exceeded on 7 November 2026. fetch.py was not run. |
| World Bank Commodity Data / Pink Sheet (fetch.py pinksheet) | used | data/clean/worldbank_pinksheet_monthly.csv, commodity Nickel, unit dollars per metric ton, 1960M01 through 2025M12. Annual averages NI_WB_AVG_2022, NI_WB_AVG_2024, NI_WB_AVG_2025. |
| USGS Mineral Commodity Summaries 2026 (fetch.py usgs) | used | data/clean/usgs_mcs2026_nickel.csv, commodity Nickel, mine production, reserves, US trade and consumption, contained nickel. Publication page https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-nickel.pdf. Narrative PDF was not reopened, so USGS end use shares are not quoted. |
| Company annual reports, 10-K/20-F, investor presentations (fetch.py sec, company IR sites) | used | research/companies profiles for nornickel, glencore, eramet, tsingshan, acerinox, haynes, special-metals, ati, carpenter, nippon-yakin and outokumpu. ATI annual report on Form 10-K and Haynes annual report on Form 10-K via sec.gov. VDM and Haynes counted once, inside Acerinox. |
| Eurostat PRODCOM (fetch.py prodcom) | used | Codes 24451100, 24451230, 24452100, 24452200 and 24452300 read from data/clean/prodcom_2019-2024.csv at git commit 1eae77d. Working copy on 7 November 2026 was header only. data/clean/prodcom_2023.csv confirms the 2023 EU 24452200 cells. |
| IEA Global Critical Minerals Outlook 2026 | used | Outlook page opened at https://www.iea.org/reports/global-critical-minerals-outlook-2026/outlook. PDF not in data/raw/iea, which holds GlobalEVOutlook2026.pdf only. Nickel tonne charts were not readable. World Energy Outlook 2025 read with pdftotext from data/raw/WorldEnergyOutlook2025.pdf, pages 62, 249 and 353. |
| INSG (International Nickel Study Group) | used | Press release of 13 October 2026, https://insg.org/wp-content/uploads/2026/10/pressrel_INSG-Press-Release-October_2026md92nd71j.pdf, and the December 2025 market article from the October 2025 meetings, https://insg.org/index.php/about-nickel/the-market-2025-12/. |
| Nickel Institute | blocked | nickelinstitute.org returned HTTP 403 on 7 November 2026 for the about nickel page and for the stainless nickel advantage page. tools/read_url.py failed the same way. No institute PDF is in data/raw. No institute figure is used. |
| LME / Indonesian RKAB policy sources | used | LME nickel contract specifications, https://www.lme.com/metals/non-ferrous/lme-nickel/contract-specifications. Revised 2026 ore quota as stated by the energy ministry and reported by Indonesia Business Post on 30 October 2026, https://indonesiabusinesspost.com/7711/energy-and-resources/energy-ministry-approves-raising-nickel-ore-quota-to-300mmt-for-the-rest-of-2026. INSG confirms the quota is lower than in 2025 without giving the ore tonnage. |
| WorldStainless | used | 2025 melt shop release, https://worldstainless.org/media/press-releases/stainless-steel-melt-shop-production-increases-by-2-1-in-2025/, and the first half 2026 table, https://worldstainless.org/data/stainless-steel-meltshop-production/. Gross stainless tonnes. |
| OECD STAN P1 and B1G | used | data/clean/oecd_stan_P1.csv and data/clean/oecd_stan_B1G.csv, activity C24, current prices, national currency. Germany through 2023. Not a nickel balance. |
| UNIDO INDSTAT | blocked | data/raw/unido contains only an empty placeholder file. No INDSTAT extract is on disk. Automated UNIDO access is blocked, so global manufacturing output by ISIC is not used. |

## Open gaps

TODO(data): UN Comtrade preview quota was exceeded on 7 November 2026. HS 2604 nickel ores, HS 7501 mattes, HS 7502 unwrought nickel, HS 7504 powders, HS 7505 bar and wire, HS 7507 tube and HS 7508 other articles were not pulled. HS 7506 is German exports only. German imports and all other reporters are missing, so class 1 sourcing dependence cannot be measured yet.

TODO(data): PRODCOM 24451100 and 24451230 have no published numbers in the 2019 to 2024 extract. Sold production unit values for 24452200 sit below the LME price in Germany and in the EU, including in 2022, so the sold kilograms are not treated as contained nickel until Eurostat metadata (tolling, alloy mix, or a unit issue) is checked. The working copy of data/clean/prodcom_2019-2024.csv was header only and should be restored from commit 1eae77d by the data session.

TODO(data): The IEA Global Critical Minerals Outlook 2026 PDF and the Critical Minerals Data Explorer extract are not in data/raw/iea. The 2035 nickel mine supply and primary requirement bars were not readable as tonnes. A webinar remark of about 4.4 million tonnes by 2030 in the Stated Policies Scenario was seen only in a search snippet of a video and is not used.

TODO(data): Nickel Institute pages returned HTTP 403. First use shares and any institute statement on the share of stainless that contains nickel were not taken from the institute. The INSG factbook 2024 PDF was not read in full, so its 2023 split (stainless about 65 percent, batteries 16 percent, scrap 972 thousand tonnes) is not used.

TODO(data): World class 1 production (cathode, briquette, pellet, powder) is not split out in the October 2026 INSG release. The NPI split is the October 2025 meeting vintage. A ranked list of class 1 producers was not opened, so Nornickel is not labelled the largest producer in this note.

TODO(data): The RKAB is ore. Contained nickel was not calculated because no grade was opened. The 2025 quota comparison of about 379 million wet tonnes sits in an existing Argus row in data/sources.csv and was not re read. The ministerial figure of about 750,000 tonnes of LME plus SHFE metal in late October 2026 was not checked against exchange stock reports. INSG's combined stock figure of 289,500 tonnes is end October 2025.

TODO(data): UNIDO is blocked. OECD STAN has no China and no nickel activity, and Germany C24 stops in 2023. OECD ICIO was not pulled.

TODO(data): Primary PDFs for Nornickel, Glencore and Eramet were not opened in the company profiles, so page numbers for guidance and for the Weda Bay tonnage remain to be checked. LME brand rules for Russian nickel and EU import limits need a legal source before a sourcing recommendation is written.

TODO(data): No primary source gives a world market value for high nickel plate, strip, bar and tube. Acerinox HPA revenue is one group. It is not an addressable market.

# Tungsten

Research note for chapter 4.6. Notes only. Figures state the stage, whether they are contained tungsten or gross weight, the year and the unit. `research/companies/sandvik.md` was not in the workspace when this note was written. Sandvik evidence below comes from the annual report page and the quarterly report that were opened.

## Key findings

1. World mine production of tungsten was an estimated 85,000 metric tons of contained tungsten in 2025, of which China accounted for an estimated 67,000 metric tons, in `data/clean/usgs_mcs2026.csv` Commodity Tungsten and in the Mineral Commodity Summaries 2026 tungsten chapter [USGS_MCS2026_TUNGSTEN]. The same source puts 2024 world output at an estimated 82,000 metric tons and China again at 67,000. A team calculation on those estimates is 78.8 percent for China in 2025 and 81.7 percent in 2024. United States mine production is zero in every year from 2021 to 2025. Commercial mining in the United States stopped after 2015 [USGS_MCS2026_TUNGSTEN].

2. The only national mining control text opened for 2025 is the first batch. China's Ministry of Natural Resources, in 自然资函〔2025〕231号 of 3 April 2025, set the first batch of the tungsten ore mining total control index at 58,000 tonnes of concentrate standardised to 65 percent WO3 [W_QUOTA_CN_2025_BATCH1]. Using the USGS statement that one metric ton unit of tungsten trioxide contains 7.93 kilograms of tungsten, that first batch is a team estimate of 29,896 tonnes of contained tungsten [W_QUOTA_CN_2025_BATCH1_W]. It is not China's annual mine output. The notice says the old split between a primary mining index and a comprehensive utilisation index has been dropped, and that small co product tungsten mines do not receive a quota and only report output. The national second batch total for 2025, and the national total for 2026, were not in the documents opened.

3. On the public ITIA applications page, tungsten carbide products are 65 percent of global first use, steels and superalloys 14 percent, tungsten metal products 12 percent, and chemicals and others 9 percent [W_ITIA_FIRSTUSE]. The same page labels the industry split as 2021 data: transport 26 percent, mining and construction 26 percent, industrial use 14 percent, chemical and petrochemical 10 percent, consumer durables 9 percent, defence 8 percent, energy 6 percent and medical 1 percent. End use by region in that 2021 table is China 36 percent, Europe 20 percent, USMCA 17 percent, Japan 8 percent, other Asia 8 percent and the rest of the world 11 percent. ITIA states a compound annual growth rate of 3.4 percent and, in two adjacent sentences, attaches it once to 2007 to 2020 and once to 2007 to 2021 [W_ITIA_CAGR]. The members area advertises a ten year forecast. That forecast was not opened, so no tonne path to 2035 is stated here.

4. The trade file `data/clean/comtrade_8101_2022-2023.csv` has 305 rows. The only reporter is China, the flows are Export and Import, the years are 2022 and 2023, and the commodity is HS 8101 at four digits, described as tungsten and articles. It is not a world matrix and it does not contain ores, ammonium paratungstate, oxides or tungsten carbide. China reported exports to the World of USD 296,601,760 and 5,744,680.17 kg in 2022, and USD 268,310,154 and 5,266,365.456 kg in 2023 [COMTRADE_8101_2022_2023]. Imports from the World were USD 43,354,065 and 119,064.297 kg in 2022, and USD 56,256,746 and 78,264.958 kg in 2023. Partner rows sum to those World totals. Weights are gross kilograms, not contained tungsten.

5. From 4 February 2025, MOFCOM and the General Administration of Customs Announcement No. 10 of 2025 requires an export licence for specified tungsten items, including ammonium paratungstate (reference HS 2841801000), tungsten oxides, tungsten carbide that is not already controlled, specified solid tungsten and tungsten alloys, and tungsten nickel iron or tungsten nickel copper alloys that meet listed mechanical properties [W_MOFCOM_2025_10]. A later MOFCOM identification note says sintered tungsten carbide, cemented carbide drills and inserts, and tungsten wire are outside that control [W_MOFCOM_FAQ_2025]. USGS reports that Rotterdam prices rose through 2025 from USD 266 to USD 551 per metric ton unit for 65 percent concentrate and from USD 331 to USD 675 per metric ton unit for APT, while the estimated annual average for in warehouse Rotterdam concentrate was USD 380 per dry metric ton unit of WO3, after USD 252 in 2024 [USGS_MCS2026_TUNGSTEN].

6. Eurostat PRODCOM DS-059358 separates powder and unwrought metal from mill products, and neither code is APT or carbide. For 24453014, EU27 sold production in 2024 is published as 9,600,000 kg and EUR 400,000,000, both rounded, with quantity rounding base 800,000 kg and value rounding base EUR 40,000,000 [EUROSTAT_PRODCOM_W]. Austria, unrounded, sold 6,440,477 kg and EUR 268,561,000 of the same code in 2024. For 24453015, EU27 sold production in 2024 is an estimated 2,377,218 kg and EUR 310,906,092. These are gross kilograms of the product. The German series for the two codes is identical in 2022, 2023 and 2024 and is not used.

7. Sandvik's quarterly report for the third quarter of 2026 says the powder business more than doubled orders and revenues on higher tungsten prices, and that the group has its own mine, recycling and powder capacity [W_SANDVIK_Q3_2026]. The Sandvik annual report 2025 says Machining brought back carbide equal to 57 percent of the weight of materials sold and processed it to zinc reclaimed powder [W_SANDVIK_RECYCLE_2025]. Höganäs, in its annual report 2025, says coating and brazing technologies face limited availability of critical raw materials such as tungsten. USGS says about 60 percent of tungsten consumed in the United States goes to cemented carbide parts, and withholds apparent consumption and secondary production.

## Production

Mine production in the USGS data release is contained tungsten, in metric tons, and the 2024 and 2025 country figures are estimates [USGS_MCS2026_TUNGSTEN]. The file note says significant revisions were made to 2024 production for Russia based on a government report, and that reserves for China and Vietnam were revised on government reports.

| Country | 2024 mine production, t contained W | 2025 mine production, t contained W | Reserves, t contained W |
| --- | ---: | ---: | ---: |
| United States | 0 | 0 | NA |
| Australia | 920 | 1,000 | 570,000 |
| Austria | 840 | 840 | 10,000 |
| Bolivia | 1,700 | 1,700 | NA |
| China | 67,000 | 67,000 | 2,500,000 |
| Kazakhstan | 0 | 2,400 | NA |
| Korea, North | 1,900 | 2,000 | 29,000 |
| Portugal | 650 | 700 | 3,400 |
| Russia | 1,500 | 2,000 | 400,000 |
| Rwanda | 1,300 | 1,300 | NA |
| Spain | 700 | 800 | 66,000 |
| Vietnam | 3,400 | 3,000 | 170,000 |
| Other countries | 1,700 | 2,400 | 950,000 |
| World | 82,000 | 85,000 | greater than 4,700,000 |

Source: `data/clean/usgs_mcs2026.csv`, Commodity Tungsten, section World Mine Production and Reserves. Zeros replace the USGS dash, which the chapter legend defines as zero. Australia's footnote says Joint Ore Reserves Committee compliant or equivalent reserves were 220,000 tons, so the 570,000 tonne reserve line and the 220,000 ton footnote are both reported and not converted into each other.

USGS states that world tungsten resources are geographically widespread and that China ranks first in both resources and reserves. No separate world resource tonnage, beyond the reserve total, is given. Several reserve cells are NA, so China's 2,500,000 tonnes should not be turned into a share of a closed world total. The world reserve line is a greater than figure.

Kazakhstan's move from zero in 2024 to an estimated 2,400 tonnes in 2025 is the start of production at the Boguty deposit, named in the USGS events text. Vietnam's estimated mine output moves from 3,400 tonnes in 2024 to 3,000 tonnes in 2025. Austria is steady at an estimated 840 tonnes of contained tungsten, which is mine output and is not the Austrian powder tonnage in PRODCOM.

The Chinese mining quota is a different measurement. The first batch for 2025 is 58,000 tonnes of ore standardised to 65 percent WO3, not tonnes of contained tungsten and not a full year [W_QUOTA_CN_2025_BATCH1]. The USGS factor is that one metric ton unit of WO3 contains 7.93 kilograms of tungsten, and one metric ton unit is 10 kilograms of WO3, so one tonne of WO3 contains 793 kilograms of tungsten. The team estimate is 58,000 times 0.65 times 0.793, which is 29,896 tonnes of contained tungsten in the first batch only [W_QUOTA_CN_2025_BATCH1_W]. A provincial notice in Zhangye, Gansu, posted on 17 October 2025, allocates 2,900 tonnes of 65 percent WO3 concentrate for the province for 2025, including a first batch of 1,250 tonnes, all to one mine. That shows a later allocation exists inside one province. It is not a national second batch total. Zhangyuan Tungsten told investors on 28 November 2025 that it had received a 2025 second batch index, without stating the national number. Heilongjiang's natural resources department, citing 自然资发〔2026〕163号, published a 2026 first batch of 100 tonnes for one iron mine. The national 2026 total is not in that notice.

## Product forms

The chain has to be read as separate products. A concentrate price, an APT price, a powder tonne and a carbide tool do not describe the same thing.

Concentrate is the mine product. Commercial trading practice cited by the Chinese quota is a 65 percent WO3 standard, and USGS prices use the same oxide unit. USGS prices are for concentrate, average in warehouse Rotterdam, in dollars per dry metric ton unit of WO3. Ores and concentrates sit in HS 2611, which is outside the Comtrade file used here. United States imports for consumption of ores and concentrates were 1,550 metric tons of contained tungsten in 2024 and an estimated 1,700 metric tons in 2025. Exports of ores and concentrates were 1,410 metric tons in 2024 and an estimated 1,400 metric tons in 2025 [USGS_MCS2026_TUNGSTEN].

Ammonium paratungstate is, in ITIA's description, the most important precursor for the majority of tungsten products. Exceptions are melting metallurgy products and some special products of much lower tonnage. Tungsten trioxide, blue oxide, tungstic acid and ammonium metatungstate are derived from APT. APT crystals are described as 30 to 100 micrometres. MOFCOM controls APT under reference HS 2841801000. Ammonium metatungstate is not in that control, according to the MOFCOM identification note. APT is not in HS 8101 and not in PRODCOM 24453014 or 24453015. USGS gives a 2025 path for APT of USD 331 to USD 675 per metric ton unit, which is not an annual average [USGS_MCS2026_TUNGSTEN].

Tungsten metal powder is made by hydrogen reduction of yellow or blue oxide at 700 to 1,000 degrees Celsius, with technical powders from 0.1 to 100 micrometres, according to ITIA. Most of that powder goes on to tungsten carbide powder. PRODCOM 24453014 is "Tungsten powder and unwrought tungsten, including bars and rods obtained simply by sintering", in gross kilograms. It is the statistical home for this stage in the EU sold production data, mixed with unwrought and simply sintered bars, so it is not a pure powder series. HS 810110 would be the powder line inside HS 8101, but the Comtrade extract is four digit only.

Tungsten carbide powder is metal powder mixed with carbon black and treated at 1,300 to 2,200 degrees Celsius. ITIA says stoichiometric carbide contains 6.13 percent carbon by weight, and that this application, cemented carbide, accounts for about two thirds of global tungsten consumption, matching the 65 percent first use share. A straight grade example given by ITIA is 90 percent tungsten carbide with 10 percent cobalt. MOFCOM controls unsintered tungsten carbide and simple mixtures under reference HS 2849902000. The same authority's identification note puts already sintered carbide, carbide plate, rod and ball, cemented carbide drills and inserts, and tungsten wire outside the February 2025 control. Those are different products for a buyer of tools than for a buyer of powder.

Mill products are the wrought and shaped metal forms. ITIA's 12 percent tungsten metal products group covers sheet and wire, tungsten copper contacts, heavy alloys, and welding electrodes. PRODCOM 24453015 is bars and rods other than those obtained simply by sintering, plus profiles, wire, plate, sheet, strip and foil. Ferro tungsten, used for steels, is a different intermediate. ITIA says commercial ferro tungsten contains 75 to 85 percent tungsten and is supplied in lumps of 50 to 100 millimetres. It is not in the two PRODCOM codes above.

## Trade

Detail and partner tables are in `research/materials/tungsten_trade.md`. The clean file is China only, HS 8101 only, 2022 and 2023 only, 305 rows, value in USD and net weight in kilograms [COMTRADE_8101_2022_2023]. World rows:

| Reporter | Flow | Year | Value USD | Net weight kg |
| --- | --- | ---: | ---: | ---: |
| China | Export | 2022 | 296,601,760 | 5,744,680.17 |
| China | Export | 2023 | 268,310,154 | 5,266,365.456 |
| China | Import | 2022 | 43,354,065 | 119,064.297 |
| China | Import | 2023 | 56,256,746 | 78,264.958 |

A team calculation on those World rows puts the 2023 export unit value at about USD 51 per kilogram and the 2022 export unit value at about USD 52 per kilogram. Import unit value is much higher, about USD 364 per kilogram in 2022 and about USD 719 per kilogram in 2023, on a much smaller weight. That pattern fits a reporter that ships a larger mass of HS 8101 goods outward and brings in a smaller mass of higher priced forms. It is not a contained tungsten balance, and it excludes APT, oxide, carbide and concentrate.

In 2023 the largest China export partners by value were Japan (USD 65,300,233 and 1,329,240 kg), the Republic of Korea (USD 52,189,995 and 1,281,595 kg) and the United States (USD 47,876,461 and 978,519 kg). Together those three are about 62 percent of the reported export value. Imports are led by Japan in both years. A partner labelled China on the import side is a re import (USD 2,983,958 and 19,254.654 kg in 2023) and is not foreign mine supply.

United States trade in the USGS chapter is contained tungsten and splits ores and concentrates from other forms. Other forms include tungstates, ferro tungsten, carbide powders, metal powders, oxides and other compounds, unwrought and wrought tungsten, and waste and scrap. In 2024, imports for consumption were 1,550 tonnes of ores and concentrates and 8,730 tonnes of other forms. Exports were 1,410 tonnes of ores and concentrates and 3,480 tonnes of other forms. Apparent consumption is withheld, so these flows are not a consumption estimate. Import sources for 2021 to 2024, ores and concentrates and other forms together, were China 26 percent (Hong Kong included in China), Germany 14 percent, Bolivia 8 percent, Vietnam 8 percent and other countries 44 percent [USGS_MCS2026_TUNGSTEN].

EU trade in the two PRODCOM codes is in the market size section. HS lines that the February 2025 licence actually names, 2841801000, 282590 and 2849902000, are not in the Comtrade extract.

## Consumption

No world consumption tonnage for 2024 or 2025 was on the ITIA pages that were opened. The public pages give shares and a historical growth rate, not a current tonne total. USGS withholds United States reported concentrate consumption and apparent consumption of all forms in every year from 2021 to 2025, and withholds secondary production, in order not to disclose company data. Net import reliance is published only as greater than 50 percent in each of those years. The definition for 2021 and 2022 includes government and industry stock changes. From 2023, government stock changes are no longer included, and the stock change series itself is NA.

ITIA's 2021 end use table is the latest dated consumption structure on the public site [W_ITIA_FIRSTUSE]. Transport and mining and construction are each 26 percent. About three quarters of the transport segment is automotive, and the tungsten there is mainly hardmetal tools used to machine and form parts, so the car industry can be the largest user while the car itself contains little tungsten. Within mining and construction, 62 percent of the tungsten goes to mining, mostly underground, and tunnelling plus road milling are the main construction uses. The geographic end use table allocates the tool to the region where it is used, not where it was produced. China is 36 percent on that end use basis, which ITIA explicitly distinguishes from China's larger role in primary and intermediate production.

USGS says an estimated 60 percent of tungsten consumed in the United States was used in cemented carbide parts for cutting and wear applications, mainly construction, metalworking, mining, and oil and gas drilling. The remainder goes to alloys and specialty steels, electrical and electronic components, heating, lighting and welding, and chemicals. That 60 percent is a United States use share. It is close to, and is not the same statistic as, the ITIA global first use share of 65 percent for carbide products.

A SCRREEN factsheet updated in January 2024 quotes an ITIA material flow study for 2016: global input to production of intermediates was 108,500 tonnes, of which 37,500 tonnes were new and old scrap, a recycling input rate of 35 percent, with an end of life recycling rate around 30 percent and a tungsten carbide recycling rate of 46 percent [W_SCRREEN_TUNGSTEN_2016]. Those are 2016 world flow estimates reproduced in a 2024 factsheet. They are not a 2024 or 2025 recycling rate. The same factsheet repeats an EU end of life recycling input rate of 42 percent from an older material system analysis. Sandvik's 57 percent is a 2025 company take back ratio for machining materials sold, not this world rate.

## Applications

Carbide and cemented carbide cover metal cutting, rock drilling, wood and plastic cutting, and wear parts. ITIA's cemented carbide paper, filed as ITIA_CCASS_29052024, still presents a 2008 snapshot of roughly 50,000 tons of tungsten content in cemented carbides and a split of that use, by tonnage, into stone working and wood and plastic machining 26 percent, metal cutting 22 percent, wear 17 percent and chipless forming 9 percent. By turnover in that same old snapshot, metal cutting was 65 percent. The paper is a technology history with a 2008 quantity, so it is not used as the current market split. The current split used here is the 65, 14, 12 and 9 first use table on the applications page, read next to the dated 2021 industry table.

Steels and superalloys take ferro tungsten as the main intermediate. Tungsten hardens high speed tool steels and supports high temperature strength in superalloys for turbine blades in aircraft engines and power generation. That is the 14 percent first use group. It is the part of the chain closest to a high performance alloy mill, and it is much smaller than carbide.

Tungsten metal mill products and heavy alloys are the 12 percent group: high temperature sheet and wire, tungsten copper electrical contacts and heat sinks, heavy alloys with iron, nickel, cobalt and copper for counterweights, vibration damping, radiation shielding and ammunition, and welding electrodes. Chemicals, about 9 percent, run through ammonium metatungstate, oxide or tungstic acid, with catalysts as the main use. ITIA also lists tungsten hexafluoride for semiconductor metallisation among minor intermediates.

Substitution, as stated by USGS, mostly reduces tungsten rather than removing it from the application. Candidates for cemented carbide include molybdenum carbide, niobium carbide, titanium carbide, ceramics, cermets and tool steels. Molybdenum can replace some mill products and some tungsten steels, though many molybdenum steels still contain tungsten. Lighting substitutes include LEDs. Depleted uranium or lead can replace tungsten where density or radiation shielding is the function, and depleted uranium alloys or hardened steel can replace it in armour piercing projectiles, with a cost or performance penalty in some uses.

## Market size

No world market value for tungsten, at any stage, is asserted. The World Bank Pink Sheet file does not contain a tungsten price, ITIA's public pages do not publish a current revenue total, and USGS does not publish a market value. Paid market reports were not used to fill that gap.

What can be stated is EU sold production of two product forms in PRODCOM, gross weight and euro value, for 2022 to 2024. The code 24453014 did not return values for 2019 to 2021. A predecessor code 24453013 returned values for those earlier years and was empty from 2022. Its official heading was not confirmed on the list page opened, so 2019 to 2021 is not spliced onto 2022 to 2024.

| Code and reporter | Year | Sold production quantity | Sold production value | Flag |
| --- | ---: | ---: | ---: | --- |
| 24453014 EU27 | 2022 | 9,000,000 kg | EUR 300,000,000 | rounded, quantity base 3,000,000 kg, value base EUR 300,000,000 |
| 24453014 EU27 | 2023 | 9,500,000 kg | EUR 390,000,000 | rounded, quantity base 500,000 kg, value base EUR 30,000,000 |
| 24453014 EU27 | 2024 | 9,600,000 kg | EUR 400,000,000 | rounded, quantity base 800,000 kg, value base EUR 40,000,000 |
| 24453014 Austria | 2023 | 5,618,344 kg | EUR 243,505,000 | no rounding flag on the cells used |
| 24453014 Austria | 2024 | 6,440,477 kg | EUR 268,561,000 | no rounding flag on the cells used |
| 24453015 EU27 | 2022 | 1,746,926 kg | EUR 170,743,820 | estimated |
| 24453015 EU27 | 2023 | 1,963,994 kg | EUR 190,428,164 | estimated |
| 24453015 EU27 | 2024 | 2,377,218 kg | EUR 310,906,092 | estimated |

Source: Eurostat PRODCOM DS-059358, queried 7 November 2026, extract `data/clean/prodcom_tungsten_ds059358.csv` [EUROSTAT_PRODCOM_W]. Austria's 2022 sold production of 24453014 was confidential. Austria's sold production of 24453015 was confidential in 2022, 2023 and 2024. Sweden's sold production of 24453014 was zero kilograms in 2022, 2023 and 2024. That zero is powder and unwrought metal, not carbide tools.

EU27 exports and imports of 24453014 in 2024 were 109,111 kg and EUR 5,448,317 outward, and 313,001 kg and EUR 15,929,921 inward. For 24453015 in 2024 they were 168,190 kg and EUR 29,171,555 outward, and 424,198 kg and EUR 62,929,370 inward. A team calculation gives about EUR 51 per kilogram for the powder and unwrought import value and about EUR 131 per kilogram for the mill product sold production value. The JSON did not label the EU aggregate trade as extra EU, so that label is not added here.

The German API rows for 24453014 and 24453015 show the same sold production in each year (647,500 kg and EUR 49,339,000 in 2024, both estimated). That duplication is treated as a data quality problem and those German production cells are not used. German trade cells differ between the two codes and were not needed for the findings.

These euro totals are sold production of two intermediate and mill forms inside the EU. They leave out concentrate, APT, carbide powder and finished tools. They are not an addressable market for the company.

Sandvik group revenues for the full year 2025 were SEK 120,680 million, with adjusted EBITA of SEK 23,309 million and a margin of 19.3 percent, as published in the quarterly report for the third quarter of 2026. Machining, the business area that contains cutting tools and the tungsten powder business, had 2025 revenues of SEK 44,003 million and adjusted EBITA of SEK 8,700 million. Those are company revenues across tools, software, mining equipment and other products. They are not a tungsten market size. Höganäs group revenue in 2025 was SEK 11,045 million across all powders, of which tungsten carbide is one coating input, not a separated revenue.

## Prices

There is no Pink Sheet price for tungsten. `data/clean/worldbank_pinksheet_monthly.csv` contains aluminum, copper, iron ore, lead, nickel, tin, zinc and two energy series. Cobalt and tungsten are both absent. The price record used here is the USGS series, sourced by USGS to Argus Tungsten Analytics, for concentrate only.

| Year | Average annual price, in warehouse Rotterdam concentrate, USD per dry metric ton unit of WO3 | Status in USGS |
| --- | ---: | --- |
| 2021 | 225 | reported |
| 2022 | 275 | reported |
| 2023 | 258 | reported |
| 2024 | 252 | reported |
| 2025 | 380 | estimated |

The 2025 estimated average of USD 380 sits inside the intra year path USGS describes for 65 percent concentrate, from USD 266 to USD 551 per metric ton unit. Those two 2025 numbers measure different things. The average is the number to use as the annual price. The path is evidence that the year was not flat. APT moved from USD 331 to USD 675 per metric ton unit over the same narrative, and no APT annual average was published in the chapter. One metric ton unit of WO3 contains 7.93 kilograms of tungsten, so these quotations are not dollars per tonne of metal and not dollars per tonne of 65 percent concentrate.

Sandvik's quarterly report says that in the third quarter of 2026 both APT and Argus scrap prices declined from the previous quarter but remained well above the prior year, and that a temporary timing effect from tungsten price development added SEK 104 million to machining adjusted EBITA, about 70 basis points of margin. No APT price level is stated in that report. United States tariff changes at the end of 2024, to 50 percent on several tungsten products from China under section 301, are cited by USGS as part of the reason prices rose in 2025, together with the February 2025 Chinese export controls.

## Capacity and supply

China's supply instrument on the mine side is the quota, not a published nameplate capacity. The first batch of 58,000 tonnes of 65 percent WO3 concentrate is the only national 2025 figure in an official text opened for this note. Small co product mines sit outside it. USGS still estimates Chinese mine output at 67,000 tonnes of contained tungsten in 2025. The two numbers can both be true because the units differ, the quota figure is a first batch, and actual output includes mines and months that the first batch does not cover. Neither number is a capacity.

Outside China, the visible 2025 change in the USGS table is Kazakhstan at an estimated 2,400 tonnes, from zero in 2024, at Boguty. Austria, Portugal and Spain remain small mine producers, at an estimated 840, 700 and 800 tonnes. United States mine capacity in operation is zero. USGS says seven United States companies can convert concentrates, APT, oxide and scrap into metal powder, carbide powder and chemicals. It does not name them or give tonnes.

The National Defense Stockpile table in the same chapter shows, for fiscal year 2025, potential disposals of 499 for ores and concentrates and potential acquisitions of 2,041 for tungsten. The chapter unit is metric tons of tungsten content unless otherwise specified, and the stockpile table does not restate a different unit. For fiscal year 2026 the Annual Materials Plan was not released, so those cells are NA. USGS also says multiple projects in Nevada, New Brunswick and Yukon received awards under Defense Production Act Title III, and that a joint venture between Kazakhstan and the United States to develop tungsten resources was announced in October. Company names, tonnes and dollars for those awards are not in the chapter.

EU processing capacity shows up as sold production, not as a nameplate. Austria sold 6,440,477 kg of PRODCOM 24453014 in 2024, against an estimated Austrian mine output of 840 tonnes of contained tungsten. The powder and unwrought figure is far larger than the mine, which is what a converter and recycler looks like. The Sandvik quarterly report says the group has its own mine and powder production and is working to diversify supply sources and expand processing capacity. The mine is not named and no tonne capacity is given. Sandvik Coromant's public recycling FAQ identifies Wolfram Bergbau und Hütten as the tungsten powder and carbide division and distinguishes a zinc process from a chemical process. That page was read from the search excerpt of the FAQ and was not re fetched as a full page, so it is used only to name the powder division.

Recycling is a supply source with old public benchmarks and one fresh company ratio. The 2016 ITIA flow quoted by SCRREEN put scrap at 37,500 of 108,500 tonnes of intermediate input. Sandvik Machining in 2025 brought back carbide equal to 57 percent of the weight of materials sold. USGS withholds the United States secondary total for 2025. A current world recycling share is a gap.

IEA, in the Global Critical Minerals Outlook 2025 section on twenty energy related strategic minerals, lists tungsten with antimony, chromium, gallium, germanium, indium, molybdenum, tantalum, tellurium, titanium, vanadium and zirconium. The page says China is the dominant refiner for 19 of those 20 minerals, with an average share around 70 percent. That average is not a tungsten refining share and is not used as one. The same outlook's supply and demand paths to 2035, as described on the page, are for the main energy minerals, not for tungsten.

## Outlook to 2035

No official tungsten mine, APT or carbide balance to 2035 was found in the sources opened. USGS stops at an estimated 2025. ITIA's public growth statement is a historical 3.4 percent compound annual rate, with the window given once as 2007 to 2020 and once as 2007 to 2021, and it does not publish the base tonnage that would be needed to extend that rate. Extending it would be an invention. The members only ten year forecast was not opened.

The IEA page that includes tungsten among twenty minerals does not give tungsten demand or supply in 2035. Export controls are mentioned there, including the early 2025 restrictions on tungsten, tellurium, bismuth, indium and molybdenum, as a general risk. They are not a forecast.

Regulation (EU) 2024/1252 lists tungsten as a strategic raw material in Annex I and as a critical raw material in Annex II. The benchmarks in the operative text and in recital 12 are for strategic raw materials as a group, for 2030, not a tungsten demand forecast and not a 2035 forecast. Union extraction capacity should be able to produce at least 10 percent of Union annual consumption of strategic raw materials, where reserves allow. Processing capacity, including intermediate steps, should be able to produce at least 40 percent. Recycling capacity should be able to produce at least 25 percent. The Union should not depend on a single third country for more than 65 percent of its supply of any strategic raw material, unprocessed and at any stage of processing. The Commission reviews the strategic list by 24 May 2027. These are policy benchmarks. They do not say Europe will mine, convert or recycle those shares of its own tungsten use.

What the opened record does support, as a qualitative outlook rather than a tonne forecast, is that mine supply stays concentrated, that the Chinese control point has moved from a concentrate quota toward licensing of APT, oxide, unsintered carbide and some large solid mill forms, and that carbide tools and tungsten wire were expressly left outside that licence in the identification note. Price behaviour in 2025, and Sandvik's 2026 comment that structural supply constraints and its own mine and recycling support the powder business, are consistent with a tight intermediate market. They are not a 2035 volume.

Sandvik's own targets for 2025 to 2030 are a group growth rate of 7 percent through a cycle, including acquisitions, and an adjusted EBITA margin of 20 to 22 percent. That is corporate guidance, not tungsten demand.

## Company evidence

Sandvik is the tungsten relevant competitor in `data/companies.csv`. The annual report 2025 innovations page says the circularity programme brings tungsten back into the loop as zinc reclaimed powder, and that in 2025 Machining brought back carbide volumes equal to 57 percent of the weight of materials sold. Walter's drill on that page is described as cutting carbide use by 45 percent per cutting edge. The quarterly report for the third quarter of 2026, issued as the earnings release of 22 October 2026, says organic order intake and revenues in the powder business more than doubled, driven by higher tungsten prices, and that the group's own mine, recycling and powder capacity are the supply position. Machining adjusted EBITA in that quarter was SEK 3,720 million, a margin of 25.7 percent, on revenues of SEK 14,459 million. A tungsten price timing effect of SEK 104 million is identified separately from underlying volume. Full year 2025 group revenue of SEK 120,680 million and adjusted EBITA of SEK 23,309 million are the prior year columns of that same quarterly report. Employees were 42,831 at 30 September 2026. No tungsten tonne capacity, no mine name and no APT price level are disclosed. The 2026 divestment of the additive manufacturing powder unit is a different business from the tungsten powder line. The impairment related to that divestment is recorded in the quarterly report and is not a tungsten volume.

Höganäs, in the annual and sustainability report 2025, page 16, says coating and brazing technologies sell tungsten, chromium and titanium carbides for thermal spray, laser cladding and weld overlay, and cites limited availability of critical raw materials such as tungsten. Group sales volume was 393,000 tonnes of all powders in 2025, which is not a tungsten volume. Revenue was SEK 11,045 million. The profile is `research/companies/hoganas.md`.

CMOC is listed as a supplier. A secondary report of its 2026 guidance, logged in `research/companies/cmoc.sources.csv`, includes tungsten of 6,500 to 7,500 tonnes alongside copper, cobalt and molybdenum guidance. The annual report was not opened and the note does not establish whether those tonnes are contained tungsten or concentrate. The figure is not used as mine production. TODO(data): CMOC tungsten output and the unit, from the results release itself.

## Spotlight facts

1. On 4 February 2025 in Beijing, MOFCOM and customs put an export licence on ammonium paratungstate, tungsten oxide and unsintered tungsten carbide, while the March 2025 identification note left sintered carbide inserts and tungsten wire outside the licence. The metal is tungsten and the controlled forms are APT, oxide and carbide powder, not finished tools. The suppliers affected are Chinese exporters of those intermediates.

2. On 3 April 2025 the Ministry of Natural Resources set the first 2025 tungsten mining batch at 58,000 tonnes of 65 percent WO3 concentrate, in 自然资函〔2025〕231号, and told provinces not to give quota to mines with an expired licence. The product form is concentrate. Small co product mines only report.

3. In the 2025 Sandvik annual report, Machining customers returned carbide equal to 57 percent of the weight of materials sold, and the group processed that scrap toward zinc reclaimed tungsten powder. The product form is cemented carbide returning as powder. Sandvik names its own recycling route and a Walter drill that uses 45 percent less carbide per edge.

4. In the third quarter of 2026, Sandvik in Sweden reported that its tungsten powder business more than doubled orders and revenues because tungsten prices were higher, and it pointed to its own mine plus recycling as the reason it could keep supplying powder and cutting tools. Cemented carbide tools remained the larger machining business. APT and scrap prices were said to be off the previous quarter but still far above the year before, with no price level printed.

5. USGS, in the February 2026 tungsten chapter, recorded the end of 2024 rise of United States tariffs to 50 percent on several Chinese tungsten products and the 2025 move in Rotterdam 65 percent concentrate from USD 266 to USD 551 per metric ton unit, with APT from USD 331 to USD 675. The product forms in the price path are concentrate and APT. The estimated annual average concentrate price for 2025 is the separate figure of USD 380 per dry metric ton unit.

## Triangulation

| Number | Source 1 | Source 2 | Difference and choice |
| --- | --- | --- | --- |
| China 2025 supply | USGS estimated mine production 67,000 t contained tungsten | MNR first batch quota 58,000 t of 65 percent WO3 concentrate, team estimate 29,896 t contained tungsten | Different stage, different coverage. The quota is a first batch and excludes small co product mines. Use USGS for estimated mine output and the ministry notice for the control instrument. Do not average them. |
| Carbide share | ITIA public page, 65 percent of global first use, undated table beside 2021 end use | USGS, about 60 percent of United States consumption in cemented carbide parts | Global first use versus one country's consumption. Both stand. Neither is a 2025 world tonne split. |
| 2025 concentrate price | USGS estimated annual average USD 380 per dry metric ton unit WO3, in warehouse Rotterdam | USGS events text, Rotterdam 65 percent concentrate moved from USD 266 to USD 551 per metric ton unit during 2025 | Average versus path. Use USD 380 as the annual price and the path as evidence of the spike. APT at USD 331 to USD 675 is a third product and has no annual average in the chapter. |
| Recycling intensity | SCRREEN 2024 factsheet quoting ITIA for 2016, scrap 37,500 t of 108,500 t intermediate input | Sandvik annual report 2025, carbide take back equal to 57 percent of machining materials sold | A 2016 world input rate versus a 2025 company weight ratio. Sandvik is not scaled to the world. USGS 2025 secondary production is withheld, so no current official world rate is chosen. |

## Source coverage

| Source | Status | Evidence |
| --- | --- | --- |
| UN Comtrade (tools/data/fetch.py comtrade) | used | `data/clean/comtrade_8101_2022-2023.csv`, COMTRADE_8101_2022_2023, 305 rows, reporter China, flows Export and Import, years 2022 and 2023, HS 8101, value USD and net weight kg. Not a world matrix. |
| World Bank Commodity Data / Pink Sheet (fetch.py pinksheet) | not applicable | Tungsten is absent from `data/clean/worldbank_pinksheet_monthly.csv`. No Pink Sheet price is stated for concentrate, APT, powder or carbide. |
| USGS Mineral Commodity Summaries 2026 (fetch.py usgs) | used | `data/clean/usgs_mcs2026.csv` Commodity Tungsten, 112 rows, and https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-tungsten.pdf |
| Company annual reports, 10-K/20-F, investor presentations (fetch.py sec, company IR sites) | used | Sandvik annual report 2025 innovations page, Sandvik quarterly report and earnings release of 22 October 2026, Höganäs annual and sustainability report 2025 |
| Eurostat PRODCOM | used | DS-059358 codes 24453014 and 24453015, EU27_2020, Austria, Germany and Sweden, 2019 to 2025 query, extract `data/clean/prodcom_tungsten_ds059358.csv`, https://ec.europa.eu/eurostat/web/prodcom/database |
| International Tungsten Industry Association (ITIA) | used | https://www.itia.info/applications-markets/ and https://www.itia.info/properties-intermediates/ opened. Members area statistics and the ten year forecast were not opened. |
| UNIDO INDSTAT | blocked | No download in data/raw/unido. Automated UNIDO access is blocked, so global manufacturing output by ISIC was not retrieved. |
| IEA Global Critical Minerals Outlook 2025 | used | https://www.iea.org/reports/global-critical-minerals-outlook-2025/broader-view-on-energy-related-strategic-minerals-what-risks-to-anticipate names tungsten among 20 minerals and does not give a tungsten tonne path to 2035. |
| OECD STAN | not applicable | STAN measures sector output and employment, not tungsten mine, APT or powder production. It was not used for a tungsten quantity. |

## Open gaps

TODO(data): national second batch and full year 2025 Chinese tungsten quota, in tonnes of 65 percent WO3, from the Ministry of Natural Resources. Only the first batch of 58,000 tonnes and one provincial later allocation were opened.

TODO(data): national 2026 tungsten mining quota. Heilongjiang's first batch of 100 tonnes cites 自然资发〔2026〕163号 but does not state the national total. A secondary report of a Heilongjiang second batch of 200 tonnes was not treated as the national figure.

TODO(data): official 2024 mining quota notice, so the 2025 first batch can be compared with the prior first batch on the same basis. A trade press claim that 2024's first batch was 62,000 tonnes was not used.

TODO(data): ITIA annual supply and demand review and the members only ten year forecast, in tonnes of contained tungsten, by first use, through 2035. The public site does not give a current consumption tonnage.

TODO(data): world or EU APT, oxide and tungsten carbide trade. The Comtrade extract stops at HS 8101 for China in 2022 and 2023. The licensed lines are 284180, 282590 and 284990, and the six digit split of 8101 was not in the file.

TODO(data): a 2024 or 2025 recycling input rate from ITIA or USGS. United States secondary production is withheld. The 35 percent figure is a 2016 flow quoted in 2024.

TODO(data): Sandvik mine name, tungsten powder tonnes and carbide tonnes. The quarterly report states the direction of the powder business and does not quantify it. `research/companies/sandvik.md` was not available.

TODO(data): CMOC tungsten output and guidance from the annual or interim results PDF, including whether the tonne is contained metal or concentrate.

TODO(data): PRODCOM before 2022 on a confirmed code heading. 24453013 returned 2019 to 2021 values and was empty afterwards, and its heading was not confirmed, so the series was not spliced. German 24453014 and 24453015 sold production cells match exactly and were discarded.

TODO(data): UNIDO INDSTAT, blocked. OECD STAN was not applicable to a tungsten quantity. No Pink Sheet price exists.

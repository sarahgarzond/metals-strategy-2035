# Titanium

Notes for chapter 4.5. Feedstock, sponge, ingot and mill product are kept apart, and aerospace demand is kept apart from industrial and pigment demand. Figures state the stage, the basis (contained TiO2 or gross metal), the year and the unit. HS 8108 bilateral flows are not cited: `data/clean/comtrade_8108_2019-2024.csv` has a header only.

## Key findings

1. Mineral concentrates and titanium metal are different markets. World mine production of ilmenite plus rutile in 2025 is estimated at 9,800 thousand metric tons of contained TiO2, of which ilmenite is 9,400 and rutile is 450 [TI_CONC_WORLD_2025]. World sponge metal production in the same year is estimated at 370,000 metric tons, gross sponge, with U.S. output at zero in 2025 [TI_SPONGE_WORLD_2025]. Ilmenite accounts for about 90 percent of world consumption of titanium minerals, and those minerals feed pigment, metal and welding rod coatings (U.S. Geological Survey, 2026b). Pigment, not aerospace mill product, is the volume outlet for the ore.

2. China is the sponge volume centre and is not the qualified aerospace sponge source for U.S. imports. Estimated 2025 sponge production is 260,000 metric tons in China, 53,000 in Japan, 25,000 in Russia, 16,000 in Kazakhstan, 12,000 in Saudi Arabia and 300 in India, against a rounded world total of 370,000 [TI_SPONGE_CHINA_2025]. Year end operating sponge capacity is 470,000 metric tons, of which China holds 320,000 [TI_SPONGE_CAP_WORLD_2025]. The United States has zero operating sponge capacity in 2025 and net import reliance of 100 percent [TI_US_NET_IMPORT_SPONGE_2025]. U.S. sponge import sources for 2021 to 2024 were Japan 77 percent, Saudi Arabia 13 percent, Kazakhstan 8 percent and other countries 2 percent.

3. Aerospace and industrial metal demand do not move together. USGS states that the majority of U.S. titanium metal was used in aerospace, with the rest in armor, chemical processing, marine hardware, medical implants, power generation and other uses, while reported U.S. consumption is withheld. In Japan, mill product shipments in fiscal 2025 (April 2025 to March 2026) were 9,803 metric tons, a third year under 10,000, and the two largest named industrial uses were plate heat exchangers at 3,267 metric tons and electrolysis at 1,742 metric tons [TI_JTS_MILL_FY2025]. The Japan Titanium Society describes aircraft demand as still high, with a supply chain inventory adjustment, and general industrial demand as stalled by Chinese overproduction.

4. Europe melts and fabricates, and it does not show up as a sponge producer. USGS lists zero sponge production and zero sponge capacity for Germany and the United Kingdom, and it does not list France as a sponge producer. Eurostat PRODCOM 24453041 (titanium, unwrought, and powders) shows EU27 sold production of 1,110 metric tons in 2024 against imports of 18,296 metric tons [TI_PRODCOM_UNWROUGHT_EU_2024]. The wrought code 24453042 shows EU27 sold production of 22,617 metric tons and imports of 31,667 metric tons [TI_PRODCOM_WROUGHT_EU_2024]. Calculated unit values put domestic unwrought sales near EUR 59 per kilogram and unwrought imports near EUR 16 per kilogram, which fits a small ingot or powder stream beside a large sponge import stream. The codes still mix forms, so they are not a pure ingot series or a pure mill product series.

5. There is no World Bank Pink Sheet titanium price. The usable price observations are U.S. import unit values and the feedstock assessments USGS republishes. The 2025 landed duty paid unit value of U.S. sponge imports is estimated at USD 12 per kilogram, down from USD 13.30 in 2024, while the customs value of imported sponge is about USD 460 million against USD 447 million in 2024 [TI_SPONGE_US_PRICE_2025]. Bulk rutile, minimum 95 percent TiO2, f.o.b. Australia, is estimated at USD 1,140 per metric ton in 2025, down from USD 1,300 in 2024 [TI_RUTILE_PRICE_2025].

6. Qualified sponge capacity is tighter than the world operating rate suggests. World sponge output of 370,000 metric tons sits inside 470,000 metric tons of operating capacity, but 320,000 metric tons of that capacity is in China. Osaka Titanium technologies is raising aircraft grade sponge capacity from 40,000 to 50,000 metric tons a year by the end of fiscal 2027, with the plant running at about 80 percent in fiscal 2025 [TI_OSAKA_CAP_2025]. ATI reports premium quality titanium lead times of about 20 months. Howmet states that it depends on limited or sole sources for titanium sponge.

7. Neither the IEA World Energy Outlook 2025 nor USGS publishes a titanium metal balance to 2035. WEO places titanium metal in a set of 20 energy related strategic minerals, notes limited substitutes, and gives 2035 supply charts only for copper, lithium, nickel and cobalt. The demand proxy that does run through 2035 and on to 2045 is commercial aircraft. Airbus expects 42,060 new passenger aircraft from 2026 to 2045 and a fleet of 45,550 in 2045, up from 23,310 at the end of 2025 [TI_AIRBUS_GMF_DELIV_2045]. Boeing expects 43,625 deliveries over the same window, including regional jets and freighters, and a 2045 fleet of 50,095 [TI_BOEING_CMO_DELIV_2045]. Kilograms of titanium per aircraft remain TODO(data), so these fleets are not converted into metal tonnes here.

## Production

### Mineral concentrates (contained TiO2)

USGS reports mine production in thousand metric tons of contained titanium dioxide unless noted. The 2025 estimates are taken from `data/clean/usgs_mcs2026.csv`, commodity Titanium Mineral Concentrates, and they match the Mineral Commodity Summaries chapter (U.S. Geological Survey, 2026b).

| Product | 2024 | 2025e | Unit |
| --- | ---: | ---: | --- |
| Ilmenite, world | 9,210 | 9,400 | thousand metric tons, contained TiO2 |
| Rutile, world | 460 | 450 | thousand metric tons, contained TiO2 |
| Ilmenite plus rutile, world | 9,680 | 9,800 | thousand metric tons, contained TiO2 |

China accounts for approximately one third of global ilmenite production. The 2025 country estimates for ilmenite, in thousand metric tons of contained TiO2, are China 3,200, Mozambique 1,900, South Africa 1,300, Australia 780, Norway 390, Senegal 370, Canada 360, Madagascar 300, India 240, Ukraine 200, the United States 100 (rounded to the nearest 100,000 tons) and other countries 230. Rutile in 2025 is Australia 200, Sierra Leone 110, South Africa 100, India 13, Mozambique 10, Ukraine 10 and other countries 9. Kenya, which produced an estimated 41 thousand metric tons of rutile in 2024, is zero in 2025. U.S. rutile is included with ilmenite.

USGS notes that Canadian, Malagasy and South African figures are mine production of titaniferous magnetite used primarily to produce titaniferous slag. Slag is an upgraded feedstock, not a finished metal. World ilmenite reserves are more than 490,000 thousand metric tons of contained TiO2, with Australia at 170,000 and China at 110,000. Rutile reserves are more than 49,000 on the same basis. World resources of anatase, ilmenite and rutile total more than 2 billion tons (U.S. Geological Survey, 2026b). Reserves are not a 2035 production forecast.

U.S. concentrate production in 2025 is estimated at 100 thousand metric tons, apparent consumption at 900, imports at 730 and exports at 10, all rounded, with net import reliance of 88 percent. Apparent consumption is production plus imports minus exports and does not adjust for inventories. USGS says 2025 apparent consumption rose an estimated 10 percent from 2024, mostly because imports rose an estimated 12 percent.

### Sponge metal (gross weight)

Sponge is the first metallic stage. USGS measures it in metric tons of sponge, not contained TiO2. Estimated production in 2025 is China 260,000, Japan 53,000, Russia 25,000, Kazakhstan 16,000, Saudi Arabia 12,000 and India 300. The rounded world total is 370,000 metric tons, down from a rounded 380,000 in 2024 [TI_SPONGE_WORLD_2025]. USGS revised 2024 Kazakhstan and Russia on the basis of company, government and news reports. U.S. production for 2021 to 2024 is withheld, and 2025 production is zero. Summing the published country estimates for 2025 gives 366,300 metric tons before USGS rounding to 370,000, so country shares should not be quoted to a tenth of a percent.

The United States did not produce sponge in 2025. The last domestic sponge plant, in Utah, closed in 2024. It had about 500 tons a year of capacity and its output was further refined for electronics. A Henderson, Nevada plant of about 12,600 tons a year has been idled since 2020. A Rowley, Utah plant of about 10,900 tons a year has been idle since 2016 (U.S. Geological Survey, 2026a). Those idle tons are not in the 2025 operating capacity line, which USGS sets at zero for the United States.

Japan's sponge shipments, which are not the same series as USGS production, were 52,142 metric tons in fiscal 2024 and 38,495 metric tons from April to December 2025. The Japan Titanium Society annualises that nine month run at about 51,300 metric tons [TI_JTS_SPONGE_SHIP_FY2024]. The gap versus the USGS calendar 2025 production estimate of 53,000 metric tons is the difference between shipments and production and between a fiscal window and a calendar year.

### Ingot

USGS does not publish a world ingot series. It does say that U.S. producers of titanium ingot and downstream products relied on imported sponge and scrap. U.S. scrap imports are estimated at 32,000 metric tons in 2025. Through July 2025 the leading scrap sources were the United Kingdom (19 percent), France and Japan (10 percent each), and Germany, the Republic of Korea and Singapore (9 percent each). A company in Virginia, which USGS does not name, started commercial powder production from scrap in late 2024 and aims at 1,400 tons a year in 2027.

Eurostat PRODCOM 24453041, "Titanium, unwrought; powders", is the closest EU quantity, and it mixes sponge, ingot and powder. EU27 sold production was 720 metric tons in 2022, 700 in 2023 and 1,110 in 2024 (720,000 kg, 700,000 kg and 1,110,000 kg). Germany accounts for 1,108 metric tons of the 2024 EU quantity. France published no quantity in 2022 or 2023 and a zero in 2024. Germany's 2023 quantity was not published. Because USGS shows no German sponge capacity, the German sold production is melting or powder, not Kroll sponge. World ingot tonnes remain TODO(data).

Western Superconducting expects a titanium electron beam melting furnace to start in the first half of 2026, and it already runs a titanium revert line. The 2025 annual report PDF was not opened in the company profile, so furnace tonnes are TODO(data). The Airbus profile cites a July 2025 company story in which EcoTitanium recycling of production scrap at Saint Eloi was extended in 2025 to Varel and Augsburg, and EcoTitanium and IMET Alloys produced a first ingot from end of life pylon scrap in June 2025. That is a closed loop at ingot stage, not a published tonne balance. https://www.airbus.com/en/newsroom/stories/2025-07-waste-not-want-not-increasing-titanium-and-aluminium-circularity

### Mill product

No world mill product total met the source standard. The Japan Titanium Society reports domestic mill product shipments of 12,187 metric tons in fiscal 2021, 14,788 in fiscal 2022, 12,961 in fiscal 2023, 9,894 in fiscal 2024 and 9,803 in fiscal 2025 [TI_JTS_MILL_FY2025]. Plate heat exchangers and electrolysis together are 5,009 metric tons of the fiscal 2025 total (3,267 plus 1,742), calculated from the two published uses. The Society says cheap Chinese material intensified competition in industrial commercially pure titanium.

EU27 sold production under PRODCOM 24453042 (bars, rods, profiles, wire, plate, sheet, strip, foil, tubes, pipes and other wrought titanium, excluding waste and scrap) was 25,000 metric tons in 2022, 15,000 in 2023 and 22,617 metric tons in 2024. France sold 9,652 metric tons in 2024 and Germany 1,662. The code is too broad to call aerospace plate or medical bar. A global mill product census, and a split of that census between aerospace and industrial, is TODO(data). The International Titanium Association statistical review, which compiles sponge and mill product statistics, could not be opened (see Source coverage).

## Trade

Bilateral UN Comtrade flows for HS 8108 are TODO(data). The clean file has zero data rows and is not used. What follows is U.S. import composition from USGS, Chinese concentrate imports as described by USGS, and EU production and trade from PRODCOM. The chapter 6 note is `research/materials/titanium_trade.md`.

U.S. sponge imports for consumption are estimated at 16,000 metric tons in 2021, 30,900 in 2022, 40,300 in 2023, 39,800 in 2024 and 44,000 in 2025 [TI_SPONGE_US_IMPORT_2025]. Exports were 117, 105, 247, 70 and 63 metric tons. Apparent consumption, defined as production plus imports minus exports and excluding withheld domestic sponge in the earlier years, moves with imports: 15,900, 30,800, 40,100, 39,800 and 44,000 metric tons. The 2025 figure is above the 40,300 metric tons imported in 2023. Through July 2025 the leading sources were Japan 73 percent, Kazakhstan 13 percent and Saudi Arabia 13 percent, against the 2021 to 2024 average of Japan 77 percent, Saudi Arabia 13 percent and Kazakhstan 8 percent.

The customs value of U.S. sponge imports was about USD 460 million in 2025 and USD 447 million in 2024. That customs value is not the same measure as the landed duty paid unit value (USD 12 per kilogram estimated for 2025 and USD 13.30 for 2024). Normal trade relations duty on 31 December 2025 was 15 percent ad valorem on unwrought titanium (HTS 8108.20.0000) and on wrought titanium (8108.90.6000), free on waste and scrap (8108.30.0000), and 5.5 percent on other articles (8108.90.3000). Ores and concentrates under 2614 and titanium slag under 2620.99.5000 were free. A 15 percent duty is one reason a customs value divided by tons sits below the duty paid unit value. The two USGS figures should be quoted as published, not forced into one price.

U.S. concentrate imports in 2025 are estimated at 730 thousand metric tons of contained TiO2, and net import reliance is 88 percent. Import sources for all forms, 2021 to 2024, were South Africa 26 percent, Canada 16 percent, Madagascar 16 percent, Mozambique 13 percent and other countries 29 percent. Through July 2025, slag came mainly from South Africa (65 percent), Norway (24 percent) and Canada (10 percent). Ilmenite came mainly from Mozambique (44 percent), Madagascar (35 percent), Ukraine (11 percent) and Senegal (9 percent). Rutile came mainly from Australia (51 percent), South Africa (20 percent), Sierra Leone (18 percent) and Canada (11 percent). Synthetic rutile came mainly from Sierra Leone (78 percent) and China (21 percent).

China's imports of titanium mineral concentrates through September 2025 were 3.8 million tons in gross weight, up 5 percent on the same period of 2024. The leading sources were Mozambique (47 percent), Australia (17 percent) and Norway (7 percent) (U.S. Geological Survey, 2026b). Gross weight is not the contained TiO2 basis used in the mine table.

EU27 trade in 2024, PRODCOM, quantity unit kilograms converted here to metric tons by dividing by 1,000:

| Code and flow | Quantity | Value |
| --- | ---: | ---: |
| 24453041 unwrought and powders, sold production | 1,110 t | EUR 65.1 million |
| 24453041 exports | 2,252 t | EUR 24.0 million |
| 24453041 imports | 18,296 t | EUR 294.4 million |
| 24453042 wrought forms, sold production | 22,617 t | EUR 534.9 million |
| 24453042 exports | 5,858 t | EUR 617.1 million |
| 24453042 imports | 31,667 t | EUR 1,817.2 million |

Calculated import unit values are EUR 16.09 per kilogram for unwrought (294,386,423 divided by 18,296,350 kg) and EUR 57.39 per kilogram for wrought (1,817,201,943 divided by 31,666,649 kg). Calculated sold production unit values are EUR 58.62 per kilogram for unwrought and EUR 23.65 per kilogram for wrought. The unwrought gap is the stage gap: a small volume of high value domestic unwrought product against a large volume of lower value imports. The wrought gap runs the other way, with imports richer per kilogram than average EU sold production, which is consistent with aerospace mill product in the import mix and a broader industrial mix in domestic sales. It is not proof of that mix, because the code bundles many forms and some national quantities are rounded.

The National Defense Stockpile Annual Materials Plan for fiscal 2025 showed potential acquisitions of 15,000 metric tons of titanium and potential disposals of 136 metric tons of titanium alloys. The fiscal 2026 plan was not released (U.S. Geological Survey, 2026a).

## Consumption

U.S. apparent sponge consumption in 2025 is the import series, 44,000 metric tons, because production is zero and exports are 63 metric tons. Reported consumption is withheld for every year from 2021 to 2025, so the aerospace share cannot be turned into a tonnage. USGS does say the majority of the metal went to aerospace.

U.S. apparent consumption of mineral concentrates in 2025 is 900 thousand metric tons of contained TiO2, against sponge of 44,000 metric tons. Even before any TiO2 to metal conversion, the concentrate market is much larger. USGS ties concentrate consumption to TiO2 pigment for paint, paper and plastics, and it ties that demand to GDP. U.S. pigment production in 2025 is estimated at 1,000,000 metric tons, valued at about USD 3 billion, from four companies and five plants. The United States is a net exporter of pigment (exports 330,000 metric tons, imports 230,000) and a net importer of sponge.

Japanese mill product consumption, measured as shipments, is the industrial picture in the previous section. Aircraft use of Japanese sponge is visible in the shipment commentary (a Boeing related inventory adjustment) rather than in a published aerospace tonnage. Osaka says domestic sponge sales fell 42.8 percent in fiscal 2025 while export sales rose 1.5 percent, which fits a weak home industrial market and a still exporting aerospace grade business.

EU apparent consumption is not published as such. A rough availability of unwrought titanium, sold production plus imports minus exports, is 1,110 plus 18,296 minus 2,252, or 17,154 metric tons in 2024. The same identity for wrought forms is 22,617 plus 31,667 minus 5,858, or 48,426 metric tons. Both are calculated from PRODCOM, they ignore stocks, and the wrought code is not one product. They are a team arithmetic check, not official consumption.

OECD STAN output for ISIC C30, manufacture of other transport equipment, is a demand context and not a titanium consumption series. C30 includes ships, rail, aircraft and spacecraft. In `data/clean/oecd_stan_P1.csv`, current price output in national currency, millions, latest year available, is the United States 388,783 in 2024 (normal value), Germany 60,902 in 2023, the United Kingdom 37,126 in 2023, Italy 41,242 in 2023, Japan 8,519,161 in 2024 (estimated) and France 130,431 in 2025 (estimated) [TI_STAN_USA_C30_P1_2024]. Value added in `data/clean/oecd_stan_B1G.csv` is 190,087 million U.S. dollars for the United States in 2023 and 16,885 million euros for Germany in 2023. These levels cannot be compared across currencies, and they cannot be read as titanium demand. UNIDO INDSTAT was not available: `data/raw/unido/` contains no dataset.

## Applications

The metal chain, after sponge, is ingot (vacuum arc, electron beam or plasma, often with scrap), then mill product (billet, bar, plate, sheet, strip, tube, wire), then forgings, castings, fasteners and finished parts. The pigment chain stops at TiO2 and does not enter that sequence. Welding rod coatings are a third, smaller outlet for mineral concentrates (U.S. Geological Survey, 2026b).

Aerospace uses commercially pure titanium and alloys, in sheet, plate, forgings and extrusions on the airframe and in fan and compressor parts in the engine. Boeing's Form 10-K for 2025 names aluminum and titanium, in sheet, plate, forgings and extrusions, as the most important raw materials for its aerospace products, and it says qualification of an alternative source can take a year or more. ATI's long term agreements with GE Aerospace and Safran cover titanium as well as nickel and vacuum melted alloys, and the Rolls-Royce agreement covers disc quality mill products and forgings. Howmet forges titanium as well as nickel and buys sponge. The MTU profile records blisks milled from solid titanium or nickel discs, and titanium aluminide low pressure turbine blades on the PW1100G-JM since a 2016 award to AMG. Pratt and Whitney, inside RTX, is a Howmet and ATI customer. None of these filings states a purchased tonnage.

Industrial uses in the Japanese shipment statistics are plate heat exchangers and electrolysis, which are commercially pure mill product. USGS adds chemical processing, marine hardware, power generation and armor for the United States. Medical implants are named by USGS and are a working group of the Japan Titanium Society, but neither source gives implant tonnes. Carpenter's medical sales of USD 278.4 million in fiscal 2026 cover the whole medical book, not titanium alone. Daido lists titanium alloys among growth products and, in a January 2026 question and answer note summarised in the company profile, describes the titanium market as being in an inventory adjustment. The Daido PDF was not reopened here, so that sentence stays qualitative.

Substitution: USGS says few materials match the strength to weight ratio and corrosion resistance of titanium metal. In high strength uses it competes with aluminum, composites, intermetallics, steel and superalloys. For corrosion resistance, aluminum, nickel, specialty steels and zirconium alloys can substitute. WEO 2025 groups titanium with tantalum and vanadium as minerals whose substitutes are unproven or costly (International Energy Agency, 2025). That is a qualitative statement, not a displacement rate.

## Market size

No primary source in this pass supports a single world market value for titanium metal. The stages have different prices, and pigment would dominate any value built from ore. The figures that are safe to quote are stage specific.

U.S. sponge imports had a customs value of about USD 460 million in 2025 on about 44,000 metric tons. U.S. TiO2 pigment production was valued at about USD 3 billion on about 1,000,000 metric tons. Those two values show the scale gap inside one country. They are not additive with EU trade values.

EU27 imports of unwrought titanium and powders were EUR 294 million in 2024, and imports of wrought forms were EUR 1,817 million. Sold production was EUR 65 million and EUR 535 million. This is the best official European value split between the unwrought code and the wrought code. It is not an addressable market for a mill.

Company revenues are not titanium market sizes. ATI fiscal 2025 sales were USD 4,587.4 million, with aerospace and defense at 68 percent, and nickel based and specialty alloys at 46 percent of revenue. The titanium share of ATI sales is not disclosed. Carpenter's Performance Engineered Products segment, which includes titanium, powder, Dynamet and additive, was USD 383.0 million in fiscal 2026, with operating income of USD 30.1 million (7.9 percent), beside Specialty Alloys Operations of USD 2,826.8 million. Howmet 2025 sales were USD 8,252 million, about 70 percent aerospace, and titanium is one input and one product family, not the company. Western Superconducting's press summaries of 2025 results put high end titanium alloy revenue at RMB 2.793 billion, 53.44 percent of revenue. The audited filing was not opened, so the figure is secondary until that PDF is read. Osaka Titanium fiscal 2025 net sales were JPY 46.9 billion and operating profit was JPY 5.5 billion. Its 2030 titanium business target is net sales of JPY 85 billion and a return on sales of 20 percent, which is a company target, not a market size.

## Prices

`data/clean/worldbank_pinksheet_monthly.csv` contains aluminum, copper, iron ore, lead, nickel, tin, zinc, Brent crude and two energy series. It has no titanium, ilmenite, rutile or sponge series. Pink Sheet is not applicable for this metal.

USGS sponge price, landed duty paid unit value of U.S. imports: USD 11.10 per kilogram in 2021, USD 11.10 in 2022, USD 12.30 in 2023, USD 13.30 in 2024 and USD 12 estimated in 2025. Scrap import unit value was about USD 8.50 per kilogram in 2024 and about USD 7.70 per kilogram through July 2025.

Feedstock prices in USD per metric ton:

| Series | 2021 | 2022 | 2023 | 2024 | 2025e | Basis |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Rutile, bulk, minimum 95 percent TiO2, f.o.b. Australia | 1,300 | 1,470 | 1,460 | 1,300 | 1,140 | Fastmarkets annual average, via USGS |
| Ilmenite and leucoxene, bulk, f.o.b. Australia | 595 | 530 | 389 | 497 | 400 | Zen Innovations Global Trade Tracker, via USGS |
| Ilmenite, U.S. import unit value | 240 | 285 | 365 | 330 | 300 | landed duty paid |
| Slag, 80 to 95 percent TiO2, U.S. import unit value | 774 | 867 | 1,050 | 970 | 880 | landed duty paid |

Rutile and bulk Australian ilmenite were both lower in the 2025 estimate than in 2024. Osaka expects export sponge selling prices to dip for a time because a titanium ore index in its pricing formula has fallen, while it also argues that aircraft grade sponge tightens again after the present inventory adjustment. Those two statements can both be true because ore indexed industrial sponge and qualified aircraft sponge are not one price.

EU unit values calculated above (about EUR 16 per kilogram for unwrought imports and about EUR 57 per kilogram for wrought imports in 2024) are not comparable one for one with the U.S. sponge duty paid price. The EU unwrought code includes powders and possibly ingot, the currency differs, and the U.S. figure is sponge only. The direction is still useful: imported unwrought metal is far cheaper per kilogram than imported wrought forms.

## Capacity and supply

World sponge operating capacity at year end 2025 is estimated at 470,000 metric tons: China 320,000, Japan 65,200, Russia 46,500, Kazakhstan 26,000, Saudi Arabia 15,600 and India 500 [TI_SPONGE_CAP_WORLD_2025]. Production of 370,000 metric tons implies a world operating rate near four fifths (370,000 divided by 470,000), calculated from two USGS estimates that are separately rounded. China at 260,000 on 320,000 is a similar rate. The idle U.S. plants (about 12,600 and 10,900 tons a year, plus the closed 500 ton plant) are outside this operating total.

Japan's 65,200 metric tons of operating capacity contains Osaka's current 40,000 metric tons a year. Osaka's expansion of 10,000 metric tons, to 50,000, is targeted for the end of fiscal 2027. The decision was taken on 2 September 2024, certified under Japan's Economic Security Promotion Act as a supply assurance plan for a specified critical product, and funded with an investment of about JPY 33 billion, a grant of up to about JPY 8 billion, and a JPY 5 billion five year loan from the Development Bank of Japan drawn on 26 December 2025. The fiscal 2025 operating rate was about 80 percent, and the company expects about 80 percent again in fiscal 2026. Toho Titanium's president sits on the Japan Titanium Society board with Osaka's president. Toho's own capacity and any expansion were not opened in a primary filing in this pass, so they are TODO(data). The residual of Japan's 65,200 metric tons is not assigned to Toho here.

Osaka's May 2026 briefing says it is the only producer, excluding China, that has decided a large sponge capacity increase, and that Chinese sponge has limited experience in aircraft destined for Europe and the United States. The same exhibit, which the company estimates, puts its commercial aircraft sponge market share at 40 percent in 2025 and 50 percent in 2030, and it draws the non China, non Russia sponge balance as moving from surplus conditions toward a gap as aircraft production normalises. The chart years are not clean enough in the text extract to assign a deficit year, so no deficit year is stated. The company does state a long term 6 percent annual growth rate for wrought titanium demand in commercial aircraft, on an index relative to fiscal 2019, after the present inventory pause.

U.S. premium capacity is melting, forging and mill product, not sponge. ATI has titanium VAR in Albany, Oregon, and in the third quarter of 2026 it described further capital spending on premium titanium without a monolithic new asset. Lead time for premium quality titanium is about 20 months, and for isothermal forgings more than two years. Carpenter melts and finishes titanium in Washington, Pennsylvania and Clearwater, Florida, inside a fiscal 2026 to 2027 capital programme aimed mainly at the Athens, Alabama brownfield (USD 242.7 million spent in fiscal 2026, guidance of USD 355 million to USD 375 million in fiscal 2027). Howmet's 2025 capital expenditure was USD 453 million, mainly engine products, and its purchase obligations for nickel, cobalt, titanium and aluminum run out to five years. Furnace tonnes at all three companies are TODO(data).

World pigment capacity in 2025 is estimated at 9,900,000 metric tons, including China 6,000,000, the United States 1,360,000, Mexico 350,000, Germany 339,000 and Japan 322,000 (U.S. Geological Survey, 2026a). Pigment capacity is not metal capacity. It is recorded so that a pigment expansion is not mistaken for a sponge expansion.

Kobe Steel has no company profile in `research/companies/`. The Japan Titanium Society president for fiscal 2025 is an executive officer of Kobe Steel responsible for the materials business, which places Kobe among the Japanese mill product principals. Kobe shipments, press size and aerospace qualifications are TODO(data). Fushun Special Steel's profile has no verified titanium tonnage. Daido's profile lists titanium as a growth product and does not give a titanium furnace capacity.

## Outlook to 2035

WEO 2025 does not forecast titanium metal demand or supply in tonnes. In the overview, titanium appears in Figure 1.23 with other strategic minerals, and the text says China is the leading refiner for nearly all of 20 minerals, with an average share around 70 percent, values referring mainly to 2024 (International Energy Agency, 2025, p. 63). Figure 5.15 repeats the set and states that titanium in that figure is titanium metal. The text says substitutes for tantalum, titanium and vanadium are limited. Figure 5.16, the only 2035 quantity chart in that discussion, covers copper, lithium, nickel and cobalt. A single country share for titanium refining is not readable as a number from the WEO text, so none is invented. The USGS sponge split, China 260,000 metric tons inside a rounded world 370,000 in 2025, is a production fact of similar magnitude, and it is not the IEA refining statistic.

The aircraft outlook is the quantitative path that reaches 2035.

Airbus Global Market Forecast 2026, passenger aircraft of at least 100 seats, figures rounded to the nearest 10 (Airbus, 2026, slides 33, 35, 36 and 37 of `data/raw/aerospace/airbus_gmf_2026_presentation.pdf`):

| Item | Aircraft |
| --- | ---: |
| Fleet in service, end 2025 | 23,310 |
| Fleet in service, end 2045 | 45,550 |
| New deliveries, 2026 to 2045 | 42,060 |
| Of which growth | 22,240 |
| Of which replacement | 19,820 |
| Staying in service from the 2025 fleet | 3,490 |
| Single aisle deliveries | 33,920 |
| Widebody deliveries | 8,140 |
| Single aisle fleet, 2025 to 2045 | 18,740 to 37,080 |
| Widebody fleet, 2025 to 2045 | 4,570 to 8,470 |

Passenger traffic growth is 3.9 percent a year from 2025 to 2045. New generation aircraft (A220, A320neo family, A330neo, A350, 737 MAX, 787 and 777X) are 39 percent of the western built passenger fleet at the end of 2025 and 82 percent in the 2035 snapshot on slide 37. Widebody deliveries are the smaller count. They are also the programmes on which airframe titanium is most discussed, but kilograms per aircraft are TODO(data). Airbus commercial deliveries in 2025 were 793 aircraft in the company profile, and the A320 family rate target in that profile is 70 to 75 a month by the end of 2027. That rate ramp is a near term pull on fasteners, pylons and engines. It is not a titanium tonnage.

Boeing Commercial Market Outlook 2026 to 2045 (Boeing, 2026, p. 4): 43,625 deliveries, made up of 33,545 single aisle, 7,715 widebody, 1,435 regional jets and 930 freighters. The 2045 fleet is 50,095. Annual traffic growth is 4.0 percent and annual fleet growth is 3.0 percent. The single aisle fleet exceeds 36,000 aircraft by 2045. Replacement is about half of deliveries. Regional delivery counts that add to the global 43,625, and 2045 fleets that add to 50,095, include China 9,240 deliveries and a 2045 fleet of 9,830 (traffic growth 5.0 percent), North America 8,405 and 10,315 (2.7 percent), Eurasia 8,590 and 10,820 (2.8 percent), and Southeast Asia 4,985 and 5,215 (6.7 percent).

The two forecasts differ because the scopes differ. Airbus counts passenger aircraft of at least 100 seats. Boeing adds regional jets and factory freighters and uses a different regional map. Single aisle deliveries are close (33,920 and 33,545). Widebody deliveries are 8,140 and 7,715. Traffic growth is 3.9 and 4.0 percent a year. Neither book is a metal balance. Osaka's own 6 percent long term growth rate for commercial aircraft wrought titanium is steeper than traffic growth. That rate is a company estimate based on aircraft production, and it is not demonstrated here with a bill of materials.

On the supply side through 2035, the only dated primary addition found in this pass is Osaka's 10,000 metric ton sponge increment by the end of fiscal 2027, inside a Japanese operating base of 65,200 metric tons in 2025. U.S. sponge remains at zero operating capacity unless an idled plant restarts, and no restart decision was found. Chinese sponge capacity of 320,000 metric tons is the volume overhang. The Japan Titanium Society and Osaka both say it is not yet the aerospace qualified overhang for Europe and the United States. If qualification of Chinese sponge changes, the shortage case for aircraft grade sponge changes with it. That qualification status is TODO(data).

Industrial mill product has the opposite near term tone. Japanese shipments are below 10,000 metric tons, Chinese material is described as abundant, and rutile and ilmenite prices in the USGS 2025 estimates are down on 2024. A strategy that treats titanium as one growth market will mix a pigment and industrial surplus with a qualified aerospace bottleneck.

## Company evidence

ATI Inc., Form 10-K for fiscal 2025 (year to 28 December 2025): sales USD 4,587.4 million, aerospace and defense 68 percent of sales, commercial jet engines USD 1,762.9 million. Titanium VAR is in Albany, Oregon. Suppliers include foreign titanium sponge. Long term agreements name GE Aerospace, Safran, Rolls-Royce and Pratt and Whitney. The third quarter 2026 earnings call puts premium quality titanium lead time at about 20 months. Filing: https://www.sec.gov/Archives/edgar/data/1018963/000162828026010140/ati-20251228.htm

Carpenter Technology, annual report on Form 10-K for fiscal 2026 (year to 30 June 2026): net sales USD 3,124.2 million. The titanium bearing PEP segment is USD 383.0 million of sales and USD 30.1 million of operating income. Aerospace and defense sales are USD 2,035.2 million. Titanium plants are in Washington, Pennsylvania and Clearwater, Florida. Raw materials include titanium and scrap bought partly abroad. Filing: https://www.sec.gov/Archives/edgar/data/17843/000001784326000034/crs-20260630.htm

Howmet Aerospace, Form 10-K for 2025: sales USD 8,252 million, about 70 percent aerospace. The risk factor text says the company depends on limited or sole sources for titanium sponge and specialised alloys. Purchase obligations cover titanium out to five years. RTX and GE Aerospace were each about 11 percent of third party sales. Filing: https://www.sec.gov/Archives/edgar/data/4281/000000428126000012/hwm-20251231.htm

GE Aerospace, Form 10-K for 2025: revenue USD 45,855 million, commercial engine deliveries 2,386 of which 1,802 were LEAP. The filing describes a supply constrained industry and sole source suppliers, without a titanium tonnage. https://www.sec.gov/Archives/edgar/data/40545/000004054526000008/ge-20251231.htm

RTX, annual report on Form 10-K for 2025, page 8: the company is largely dependent on foreign sources for cobalt, tantalum, chromium, rhenium, nickel and titanium. Pratt and Whitney sales were USD 32,916 million. Filing: https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/rtx-20251231.htm

Boeing, Form 10-K for 2025, page 4: aluminum and titanium in sheet, plate, forgings and extrusions are the most important raw materials, and qualifying a new source can take a year or more. Commercial deliveries were 600 aircraft. Filing: https://www.sec.gov/Archives/edgar/data/12927/000162828026004357/ba-20251231.htm

Airbus profile: 793 commercial deliveries in 2025, order book 8,754 commercial aircraft, A320 family aimed at 70 to 75 a month by the end of 2027. The July 2025 circularity story is the source the profile uses for EcoTitanium. The structural weight share of titanium on the A350 is not given a source in that profile and is not used here.

Safran profile: propulsion revenue EUR 15,668 million in 2025. The April 2026 Gennevilliers press release was not opened in that profile, so the hydraulic press size stays TODO(data). The usable statement is that Gennevilliers forges nickel alloys and titanium for LEAP, GE9X and military engines.

Rolls-Royce profile: titanium forgings and discs for fan and compressor stages, and ATI as a named supplier of disc quality mill products. No Rolls-Royce titanium tonnage was found. Underlying group revenue is not a titanium figure.

MTU profile: blisks milled from titanium or nickel, a revert loop that returns titanium chips, an early replacement of a Russian titanium supplier recorded in the 2022 investor materials, and titanium aluminide blades for the PW1100G-JM from AMG since 2016. Annual purchased tonnes are TODO(data).

Osaka Titanium technologies, earnings release and investor presentation read for this note: fiscal 2025 net sales JPY 46.9 billion, sponge capacity 40,000 metric tons a year rising to 50,000, operating rate about 80 percent. https://www.osaka-ti.co.jp/e/e_ir/pdf/e-ir20251226.pdf and https://www.osaka-ti.co.jp/e/e_ir/pdf/e-ir202605_01.pdf

Japan Titanium Society, business report dated 28 May 2026: sponge and mill product shipments cited above. The fiscal 2025 president is from Kobe Steel, with vice presidents from Osaka Titanium and Daido Steel and a director from Toho Titanium. https://www.titan-japan.com/pdf/jigyohokoku2026.pdf

Western Superconducting: press summaries, not the opened annual report, give 2025 revenue of RMB 5.226 billion and high end titanium alloy revenue of RMB 2.793 billion. Electron beam capacity in tonnes is TODO(data).

Daido Steel: profile only. Titanium is a growth product and was described as in inventory adjustment in January 2026. No titanium tonnage. The underlying PDF was not reopened.

Fushun Special Steel: no verified titanium metal volume in the profile.

Kobe Steel: no profile. The role recorded here is the Japan Titanium Society chair.

## Spotlight facts

1. In 2025 the United States imported an estimated 44,000 metric tons of titanium sponge, with zero domestic sponge production after the Utah plant closed in 2024, and the 2021 to 2024 suppliers were Japanese, Saudi and Kazakh sponge makers (U.S. Geological Survey, 2026a).

2. On 26 December 2025 Osaka Titanium technologies drew a JPY 5 billion Development Bank of Japan loan for a certified plan to lift aircraft grade sponge capacity in Japan from 40,000 to 50,000 metric tons a year by the end of fiscal 2027, against a USGS Japan operating capacity of 65,200 metric tons in 2025.

3. Boeing's 2025 Form 10-K names titanium sheet, plate, forgings and extrusions, with aluminum, as its most important raw materials, and ATI's 2025 Form 10-K ties premium titanium and nickel mill products to GE Aerospace, Safran, Rolls-Royce and Pratt and Whitney, with premium quality titanium quoted at about a 20 month lead time in October 2026.

4. Japan Titanium Society mill product shipments were 9,803 metric tons in fiscal 2025, including 3,267 metric tons for plate heat exchangers, while Chinese sponge production was an estimated 260,000 metric tons, so the industrial mill product market and the Chinese sponge market are not the aerospace qualified market.

5. Airbus GMF 2026 (July 2026 presentation) counts 8,140 widebody deliveries from 2026 to 2045 inside 42,060 passenger deliveries, and Boeing CMO 2026 counts 7,715 widebody deliveries inside 43,625 total deliveries. Both are airframe and engine demand pools for plate, forgings and discs, and neither states the titanium mass.

## Triangulation

| Number | Source 1 | Source 2 | Difference and choice |
| --- | --- | --- | --- |
| World sponge production, 2025, 370,000 metric tons | `data/clean/usgs_mcs2026.csv`, commodity Titanium Sponge Metal, world total, estimated | U.S. Geological Survey Mineral Commodity Summaries 2026 titanium chapter, same table, local PDF `data/raw/aerospace/usgs_mcs2026_titanium.pdf` | Same publication in two files. Used as the world production total. The independent check is the Japan row below, not a second world total. |
| Japan sponge, 2025 | USGS calendar 2025 production 53,000 metric tons, estimated | Japan Titanium Society shipments 52,142 metric tons in fiscal 2024 and 38,495 metric tons in April to December 2025, annualised by JTS at about 51,300 | Production versus shipments, and calendar year versus fiscal year. Both are kept. USGS is used for the world table. JTS is used for the shipment trend and the aircraft versus industrial commentary. |
| Commercial aircraft deliveries, 2026 to 2045 | Airbus GMF 2026: 42,060 passenger aircraft of at least 100 seats (33,920 single aisle and 8,140 widebody) | Boeing CMO 2026: 43,625 deliveries (33,545 single aisle, 7,715 widebody, 1,435 regional jets, 930 freighters) | Scope, not a dispute. Single aisle counts are within about 400 aircraft. Widebody counts differ by 425. Neither is converted to titanium tonnes. |
| U.S. sponge import price, 2024 to 2025 | USGS landed duty paid unit value USD 13.30 per kilogram in 2024 and USD 12 estimated in 2025 | USGS customs value about USD 447 million in 2024 and USD 460 million in 2025, on 39,800 and 44,000 metric tons, and a 15 percent duty on HTS 8108.20 | Customs value and duty paid unit value are different measures. Both are quoted. One sponge price is not forced. Pink Sheet has no titanium row. |
| EU unwrought unit value, 2024 | Eurostat sold production EUR 65.07 million on 1,110 metric tons, or EUR 58.62 per kilogram | Eurostat imports EUR 294.4 million on 18,296 metric tons, or EUR 16.09 per kilogram | Same dataset, two flows. The gap is read as product mix inside one PRODCOM code (domestic ingot or powder versus imported sponge), consistent with USGS showing no EU sponge capacity. |

## Source coverage

| Source | Status | Evidence |
| --- | --- | --- |
| UN Comtrade (tools/data/fetch.py comtrade) | blocked | `data/clean/comtrade_8108_2019-2024.csv` has zero data rows. TODO(data): HS 8108 bilateral flows, 2019 to latest. The file is not cited. |
| World Bank Commodity Data / Pink Sheet (fetch.py pinksheet) | not applicable | `data/clean/worldbank_pinksheet_monthly.csv` has no titanium, ilmenite, rutile or sponge series. Prices used are USGS import unit values and feedstock assessments. |
| USGS Mineral Commodity Summaries 2026 (fetch.py usgs) | used | `data/clean/usgs_mcs2026.csv` commodities Titanium Sponge Metal, Titanium sponge metal and Titanium Mineral Concentrates. Narrative from `data/raw/aerospace/usgs_mcs2026_titanium.pdf` and https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-titanium-minerals.pdf |
| Company annual reports, 10-K/20-F, investor presentations (fetch.py sec, company IR sites) | used | ATI, Carpenter, Howmet, GE Aerospace, RTX and Boeing Form 10-K filings on sec.gov, Osaka Titanium investor presentation, profiles in `research/companies/` for Safran, Rolls-Royce, MTU, Airbus, Daido, Western Superconducting and Fushun. |
| Eurostat PRODCOM | used | Direct read of DS-059358 for 24453041 and 24453042, EU27, Germany and France, 2022 to 2024. https://ec.europa.eu/eurostat/web/prodcom/database The existing raw pull under other 24453 codes is not titanium. |
| International Titanium Association | blocked | https://titanium.org/ returned HTTP 403 (Cloudflare) on 7 November 2026, including the statistical review store page, so the ITA sponge and mill product review was not opened. Japan Titanium Society business report used instead: https://www.titan-japan.com/pdf/jigyohokoku2026.pdf |
| Airbus / Boeing outlooks (aerospace demand) | used | Airbus GMF 2026 presentation `data/raw/aerospace/airbus_gmf_2026_presentation.pdf`, slides 33 to 38, and https://www.airbus.com/en/products-services/commercial-aircraft/global-market-forecast . Boeing CMO 2026 https://www.boeing.com/content/dam/boeing/v2/products/commercial-market-outlook/downloads/2026-cmo-download.pdf page 4. |
| OECD STAN C30 | used | `data/clean/oecd_stan_P1.csv` and `data/clean/oecd_stan_B1G.csv`, activity C30, output and value added. This is other transport equipment, not titanium consumption. |
| IEA World Energy Outlook 2025 | used | `data/raw/WorldEnergyOutlook2025.pdf`, Figure 1.23 and Figure 5.15, titanium metal named, no 2035 tonne path. https://www.iea.org/reports/world-energy-outlook-2025 |
| UNIDO INDSTAT | blocked | `data/raw/unido/` has no dataset. Automated access is blocked. No manufacturing output by ISIC was taken from UNIDO. |

## Open gaps

TODO(data): HS 8108 bilateral exports and imports for 2019 to the latest year, by reporter and partner, value and kilograms. `data/clean/comtrade_8108_2019-2024.csv` has zero rows and was not cited. HS 2614 (ores and concentrates), slag under 2620, and the 8108.20, 8108.30 and 8108.90 splits were not pulled as separate Comtrade series either. U.S. source shares from USGS are the substitute.

TODO(data): world titanium ingot production and world mill product shipments, split between aerospace and industrial, for a recent year and through 2035. The ITA statistical review was not accessible. A Chinese industry association figure was not used because the original paper was not read in full.

TODO(data): kilograms of titanium mill product and buy weight per aircraft family (A320neo, A350, 737 MAX, 787, 777X) and per engine (LEAP, GEnx, GE9X, Trent XWB, PW1100G). Without that factor, Airbus and Boeing fleets stay in aircraft units.

TODO(data): Toho Titanium sponge capacity and any expansion, Kobe Steel mill product shipments and press capacity, and whether idled U.S. sponge plants at Henderson or Rowley have a restart plan.

TODO(data): qualification status of Chinese sponge for European and U.S. aircraft programmes. Osaka states that experience is limited. A dated qualification, test programme or rejection was not found in a primary filing.

TODO(data): Safran Gennevilliers press release (April 2026) press rating, Daido titanium volume, Western Superconducting audited titanium revenue and electron beam capacity, and Fushun titanium volume. Profiles exist, and the underlying filings were not all opened.

TODO(data): Eurostat PRODCOM flags and rounding bases for 24453041 and 24453042, and sold production for member states other than Germany and France. Italy and the United Kingdom were not queried. The United Kingdom is outside EU27.

TODO(data): a titanium metal price series independent of the U.S. import unit value. Pink Sheet does not carry one. Osaka described an ore indexed export price and did not publish a numeric realisation in the pages read here.

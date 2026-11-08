<!-- supersedes: nothing (first creation). linked from: research-protocol trade note for chapter 6, data/source_matrix.json materials.molybdenum, research/materials/molybdenum.md. user instruction: "No molybdenum trade file was saved. TODO(data) for HS 8102 and ferromolybdenum. Write research/materials/molybdenum.md and molybdenum_trade.md." -->

# Molybdenum trade

Chapter 6 input. No molybdenum Comtrade file was saved. The flows below are either a US stage split from USGS Mineral Commodity Summaries 2026 or a regional use split from IMOA. Neither is a bilateral customs record. Mine concentrate, roasted concentrate (technical oxide), chemical oxide, ferromolybdenum and molybdenum metal move under different headings and must be pulled separately.

## What was not saved

`TODO(data): HS 8102 molybdenum and articles was not saved. Searched data/clean on 7 November 2026. Comtrade files present are HS 7506 (nickel plate), HS 8101 (tungsten) and HS 8108 (titanium). No file covers HS 8102.`

`TODO(data): ferromolybdenum was not saved. The heading is HS 7202.70. USGS publishes US import source shares for 2021 to 2024 and the normal trade relations tariff. It does not publish bilateral tonnes or values for ferromolybdenum.`

`TODO(data): HS 2613.10 roasted molybdenum ores and concentrates, HS 2613.90 other molybdenum ores and concentrates, and HS 2825.70 molybdenum oxides and hydroxides were also not saved. Technical oxide is often the roasted concentrate heading, while pure oxide is the chemical heading. Inferring either from HS 8102 would mix molybdenum metal with the meltstock the steel mill buys.`

Reporters that a later pull should cover, once the preview quota allows it, are the producers and converters named in the mine and REACH evidence: China, the United States, Chile, Peru, Mexico, the Republic of Korea, Belgium (Molymet technical oxide), the Netherlands (Climax pure oxide), Germany (Molymet dioxide) and Austria (Plansee metal). Partners should at least include those same countries plus Japan and the European aggregate. Years should be 2019 through the latest available year, value and net weight. The public preview cap of 500 rows means each heading needs its own file, not one combined extract.

## Headings and the stage they measure

The tariff lines below are the US normal trade relations schedule printed in USGS MCS 2026, as of 31 December 2025. They are a classification map, not a trade flow. Rates are quoted so a later Comtrade pull can be tied to the right product. They are not a duty cost for a European mill.

| Stage | US heading in MCS 2026 | What it measures | Normal trade relations rate, 31 December 2025 |
| --- | --- | --- | --- |
| Mine concentrate, other than roasted | 2613.90.0000 | Molybdenum ore and concentrates, other | 17.8 cents per kilogram on molybdenum content |
| Roasted concentrate, technical oxide traded as concentrate | 2613.10.0000 | Molybdenum ore and concentrates, roasted | 12.8 cents per kilogram on molybdenum content plus 1.8 percent ad valorem |
| Chemical oxide | 2825.70.0000 | Molybdenum oxides and hydroxides | 3.2 percent ad valorem |
| Molybdates | 2841.70.1000 and 2841.70.5000 | Ammonium molybdates, and all other molybdates | 4.3 percent and 3.7 percent ad valorem |
| Ferromolybdenum | 7202.70.0000 | Ferroalloys, ferromolybdenum | 4.5 percent ad valorem |
| Molybdenum metal powder | 8102.10.0000 | Powders | 9.1 cents per kilogram on molybdenum content plus 1.2 percent ad valorem |
| Unwrought molybdenum metal | 8102.94.0000 | Unwrought | 13.9 cents per kilogram on molybdenum content plus 1.9 percent ad valorem |
| Wrought bars, rods, plate, sheet, strip | 8102.95.3000 and 8102.95.6000 | Wrought mill products of molybdenum metal | 6.6 percent ad valorem |
| Wire | 8102.96.0000 | Wire | 4.4 percent ad valorem |
| Waste and scrap | 8102.97.0000 | Waste and scrap | Free |
| Other articles | 8102.99.0000 | Other | 3.7 percent ad valorem |

HS 8102 is molybdenum metal and articles of molybdenum metal. It is not 316L sheet, not C-276 plate and not Alloy 625 bar. Those mill products are stainless or nickel alloy headings (HS 7219, 7220, 7222, 7506 and related lines) in which molybdenum is an alloying element of about 2 percent, about 16 percent or about 9 percent. A chapter 6 table that reports HS 8102 as the company's product trade would describe the wrong market. The company's relevant trade, once someone pulls it, is the alloy heading plus the meltstock headings 2613 and 7202.70 that feed the mill.

China's February 2025 export control, as stated by USGS, covers molybdenum powders. That is the 8102.10 family, not concentrate and not ferromolybdenum. `TODO(data): the MOFCOM instrument and the exact powder lines were not opened.`

## United States stage split, contained molybdenum

Source: `data/clean/usgs_mcs2026.csv`, Commodity Molybdenum, and the February 2026 chapter https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-molybdenum.pdf. Unit is metric tons of contained molybdenum. The 2025 column is estimated. Ore and concentrate export content is estimated from Census Bureau unit values. This is US trade with the world, not a partner table.

| Flow | 2021 | 2022 | 2023 | 2024 | 2025e |
| --- | --- | --- | --- | --- | --- |
| Mine production | 41,100 | 34,600 | 34,000 | 34,000 | 40,000 |
| Imports, ore and concentrates | 15,500 | 15,700 | 16,200 | 14,700 | 17,000 |
| Imports, primary products | 14,700 | 13,100 | 13,500 | 12,200 | 9,700 |
| Exports, ore and concentrates | 33,900 | 26,900 | 29,200 | 26,900 | 27,000 |
| Exports, primary products | 4,150 | 4,860 | 4,230 | 5,890 | 6,500 |
| Reported consumption, primary products | 16,100 | 15,800 | 16,000 | 17,000 | 18,000 |
| Apparent consumption | 33,100 | 31,500 | 30,700 | 28,500 | 34,000 |

Net import reliance is E, net exporter, in every year from 2021 to 2025. The United States mines more contained molybdenum than it reports as primary product consumption, and it exports more concentrate than it imports. Primary product imports fell from 14,700 tonnes in 2021 to an estimated 9,700 tonnes in 2025, while primary product exports rose from 4,150 tonnes to 6,500 tonnes. The concentrate export stayed near 27,000 tonnes. A reader who adds imports of ore and imports of primary products will get about 26,700 tonnes of imports in 2025, which matches the chapter's statement that total imports for consumption were about 27,000 tonnes.

Import source shares for 2021 to 2024 are shares of US imports, not tonnes. Ferromolybdenum: Chile 74 percent, Republic of Korea 21 percent, United Kingdom 4 percent, other 1 percent. Ore and concentrates: Peru 69 percent, Mexico 15 percent, Chile 12 percent, Canada 4 percent. All forms together: Chile 36 percent, Peru 35 percent, Mexico 8 percent, Republic of Korea 7 percent, other 14 percent. Ferromolybdenum and concentrate do not have the same geography. Chile dominates the ferroalloy. Peru dominates the concentrate.

## Regional use, which is not trade

IMOA, 1 April 2026, first use of new molybdenum in million pounds. This is consumption geography from Steel and Metals Market Research, excluding scrap. It is the best geography available until Comtrade is pulled. It does not identify the exporter.

| Region | 2025 use, million pounds Mo | Change stated by IMOA against 2024 |
| --- | --- | --- |
| China | 337.8 | up 9 percent |
| Europe | 114.3 | down 7 percent |
| Other regions | 93.1 | down 1 percent |
| United States | 65.7 | up 3 percent |
| Japan | 42.6 | down 3 percent |
| CIS | 18.3 | down 12 percent |
| World | 671.8 | up 3 percent from 653.6 |

The six regions sum to 671.8 million pounds. IMOA prints that world total as 304,700 tonnes. Europe remains the second largest user and is the large region whose use fell. China is about half of world first use (337.8 divided by 671.8). US IMOA use of 65.7 million pounds is about 29,800 tonnes at 0.45359237 kilograms per pound. USGS reported US consumption of primary products is 18,000 tonnes and apparent consumption is 34,000 tonnes. The three boundaries differ. Do not treat the IMOA US figure as a customs import.

Mine production geography for the same year, for comparison with where units originate, is in `research/materials/molybdenum.md`. The short trade point is that USGS and IMOA agree on North America and on Chile plus Peru within about 2,000 tonnes, and they disagree on China by about 40,000 tonnes. A trade pull will not resolve that mine gap, because customs data measure cross border shipments, not mine output.

## What chapter 6 can say before the pull

The United States is a net exporter of contained molybdenum, mainly as concentrate, and a buyer of ferromolybdenum from Chile and Korea. Europe's first use of new molybdenum fell 7 percent in 2025, to 114.3 million pounds, while China's rose 9 percent, to 337.8 million pounds. Technical oxide, ferromolybdenum and molybdenum metal are different headings. Alloy mill products of 316, C-276 and 625 are not in HS 8102. Powder is the form USGS says China controlled in February 2025. None of those sentences depends on a Comtrade file. Any tonne or dollar figure by partner does, and those figures are the open gaps above.

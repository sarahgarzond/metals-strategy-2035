# Chromium trade

This note is the chapter 6 input for chromium. It keeps four product forms apart: chromite ore (HS 2610), ferrochrome and related ferroalloys (HS 7202), chromium metal (HS 8112), and stainless steel (HS 7218 to 7223, plus stainless scrap HS 7204.21). Gross kilograms of one heading are not contained chromium and are not kilograms of another heading.

No UN Comtrade extract has been saved for these headings. data/clean currently has comtrade_7506_2023-2024.csv, comtrade_8101_2022-2023.csv and comtrade_8108_2019-2024.csv only. tools/data/fetch.py was not run for chromium. TODO(data): HS 7202 and the stainless headings below, plus HS 2610 and HS 8112, for 2019 to the latest year, exports and imports, value in US dollars and net weight in kilograms, for the main ore, ferrochrome, metal and stainless reporters and their partners. The public preview endpoint is https://comtradeplus.un.org/ and the project fetcher caps a query at 500 rows.

## Headings to pull

USGS MCS 2026 prints the US Harmonized Tariff Schedule lines that map onto these HS headings. Rates below are Normal Trade Relations rates as of 31 December 2025 in that chapter. They are US tariff rates, not world tariffs, and they are not trade flows.

| Form | HS or HTS | What it measures | US NTR rate, 31 December 2025 | Comtrade file |
| --- | --- | --- | --- | --- |
| Chromite, not more than 40 percent Cr2O3 | 2610.00.0020 | Ore and concentrates, gross weight, low chromic oxide | Free | none |
| Chromite, more than 40 and less than 46 percent Cr2O3 | 2610.00.0040 | Ore and concentrates, gross weight | Free | none |
| Chromite, 46 percent Cr2O3 or more | 2610.00.0060 | Ore and concentrates, gross weight, higher grade | Free | none |
| Ferrochromium, more than 4 percent carbon | 7202.41.0000 | High carbon ferrochrome, inside HS 7202 | 1.9 percent ad valorem | none. TODO(data) |
| Ferrochromium, more than 3 and less than 4 percent carbon | 7202.49.1000 | Ferrochrome, inside HS 7202 | 1.9 percent ad valorem | none. TODO(data) |
| Ferrochromium, more than 0.5 and less than 3 percent carbon | 7202.49.5010 | Medium carbon ferrochrome | 3.1 percent ad valorem | none. TODO(data) |
| Ferrochromium, not more than 0.5 percent carbon | 7202.49.5090 | Low carbon ferrochrome | 3.1 percent ad valorem | none. TODO(data) |
| Ferrosilicon chromium | 7202.50.0000 | A different alloy from ferrochromium. USGS ferrochrome prices exclude it | 10 percent ad valorem | none. TODO(data) |
| Stainless steel in primary forms | 7218 | Ingots and other primary forms, gross steel | not taken from the USGS chromium tariff table | none. TODO(data) |
| Stainless flat, 600 mm or wider | 7219 | Flat rolled stainless, the wide flat product | not in the USGS chromium tariff table | none. TODO(data) |
| Stainless flat, under 600 mm | 7220 | Narrow flat rolled stainless | not in the USGS chromium tariff table | none. TODO(data) |
| Stainless bars, hot rolled coils | 7221 | Long product, not flat | not in the USGS chromium tariff table | none. TODO(data) |
| Other stainless bars and angles | 7222 | Long product | not in the USGS chromium tariff table | none. TODO(data) |
| Stainless wire | 7223 | Wire, gross steel | not in the USGS chromium tariff table | none. TODO(data) |
| Stainless steel scrap | 7204.21.0000 | Scrap, which USGS treats as a chromium supply via recycling | Free | none |
| Chromium metal, unwrought and powder | 8112.21.0000 | Metal, gross weight, not ferrochrome | 3 percent ad valorem | none |
| Chromium metal waste and scrap | 8112.22.0000 | Metal scrap | Free | none |
| Other chromium metal articles | 8112.29.0000 | Other metal | 3 percent ad valorem | none |

HS 7202 in the project code list is the whole ferroalloys basket, which also contains ferromolybdenum and other alloys. A chromium trade pull has to be cut to 7202.41, 7202.49 and 7202.50 or the kilograms will mix metals. Stainless headings 7218 to 7223 are gross steel. They will overstate chromium if they are added to ore or ferrochrome.

Eurostat PRODCOM is the EU production and trade companion, not a substitute for Comtrade. The relevant sold production codes are 24104100 (stainless ingots and primary forms), 24104330 (cold rolled stainless flat) and 24343000 (cold drawn stainless wire). data/clean/prodcom_2019-2024.csv has 2,346 rows and none of those three codes. TODO(data): those three codes for EU27_2020 and Germany, 2019 to 2024, sold production, exports and imports.

## What can be said without Comtrade

The only origin statistics in hand are United States import shares for 2021 to 2024 from USGS MCS 2026. Each row is a share of US imports of that form. Rows are not tonnes, not dollars, and not world trade. The total row is not the sum of the form rows.

| US import form, 2021 to 2024 | Leading origins, percent of that form |
| --- | --- |
| Chromite ores and concentrates | South Africa 96, Turkey 3, other 1 |
| Ferrochromium | South Africa 41, Kazakhstan 24, Russia 6, Finland 5, other 24 |
| Chromium metal | China 40, United Kingdom 26, Russia 15, France 14, other 5 |
| Chromium containing chemicals | Kazakhstan 25, China 19, Germany 14, India 13, other 29 |
| Chromium containing scrap (metal scrap and stainless scrap) | Canada 50, Mexico 45, other 5 |
| Stainless steel | Taiwan 16, Finland 12, India 11, China 6 (includes Hong Kong), other 55 |
| All forms together | South Africa 31, Kazakhstan 11, Finland 6, Canada 5, other 47 |

The pattern is the substantive trade finding until Comtrade is pulled. Ore imports are concentrated on South Africa. Ferrochrome imports are still led by South Africa but Kazakhstan and a large "other" share matter, and Finland is visible. Chromium metal imports are led by China, the United Kingdom, Russia and France, which is a different supplier set from the ore. Stainless imports are dispersed, with Taiwan, Finland and India ahead of China. A single "chromium import dependence" figure would hide that split.

US import and export tonnages in the same chapter are chromium content and they mix chemicals, metal, ore, ferrochromium, ferrosilicon chromium, and stainless products and scrap. Imports for consumption were 492 thousand metric tons in 2024 and an estimated 520 thousand metric tons in 2025. Exports were 148 thousand metric tons in 2024 and an estimated 140 thousand metric tons in 2025. Net import reliance was 77 percent of apparent consumption in 2024 and an estimated 79 percent in 2025. Those totals are not an HS 7202 balance.

ICDA's public page, not Comtrade, says China holds virtually no chromite and is the largest chromite importer, with South Africa the main source, and that China has been the largest ferrochrome producer since 2012. The 2025 ICDA bars show China at 9,907 kt of ferrochrome and South Africa plus Zimbabwe at 2,091 kt. That is a production shift consistent with ore moving to China for smelting, but it is not a measured trade flow. Team Stainless (17 April 2025) said 2024 ferrochrome growth was driven notably by China and Indonesia. Indonesia is not broken out on the 2025 ICDA ferrochrome bars (the Americas and rest of Asia bar is 1,257 kt, up 27 percent, and is not an Indonesia figure).

worldstainless production is not trade. It does show where stainless tonnes are melted: China 40,868 thousand metric tonnes and the European Union 5,659 thousand metric tonnes in 2025, out of a world total of 64,157 thousand metric tonnes. EU melt shop output fell 1.9 percent while US melt shop output rose 7.6 percent to 2,099 thousand metric tonnes. Company commentary links the US delivery recovery to tariffs (Outokumpu Americas adjusted EBITDA recovered in the second half of 2025 as tariffs redirected orders). That is a company statement, not a customs statistic.

## Open items for chapter 6

TODO(data): HS 7202 ferrochrome (7202.41, 7202.49, 7202.50 only, not the whole ferroalloy basket) and stainless HS 7218, 7219, 7220, 7221, 7222 and 7223. No ferrochrome trade file exists yet.

TODO(data): HS 2610 chromite by Cr2O3 band if the reporter detail allows it, and HS 8112 chromium metal. Both are missing, so ore and metal trade cannot be quantified.

TODO(data): PRODCOM 24104100, 24104330 and 24343000 so EU stainless flat and wire trade can be set next to Comtrade.

TODO(data): do not add USGS chromium content import tonnes to worldstainless melt shop tonnes or to ICDA ferrochrome kilotonnes. The units are different and the USGS import total already includes stainless.

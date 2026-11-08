# Zirconium trade (for chapter 6)

This file is the zirconium trade note. It is not a zircon sand Comtrade extract. World flows for HS 8109 and HS 2615 were not pulled.

TODO(data): UN Comtrade exports and imports, 2019 to the latest year, value and kilograms, for HS 8109 (zirconium, unwrought, powders, and articles) and HS 2615 (zirconium ores and concentrates, zircon). No data/clean file exists for either heading. Reporters still needed include Australia, South Africa, Mozambique, Senegal, China, the United States, France, Germany, and the EU.

## What the headings cover

USGS Mineral Commodity Summaries 2026, zirconium and hafnium chapter, page 1, gives the U.S. tariff lines that sit under those headings. https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-zirconium-hafnium.pdf

| Chain | U.S. tariff line | Rate cited for 31 December 2025 |
| --- | --- | --- |
| Zircon sand | 2615.10.0000 ores and concentrates | Free |
| Chemicals | 2825.60.0020 and 2836.99.5010 zirconium compounds | 3.7% ad valorem |
| Metal, unwrought and powder | 8109.21.0000 and 8109.29.0000 | 4.2% ad valorem |
| Metal, waste and scrap | 8109.31.0000 and 8109.39.0000 | Free |
| Metal, other articles, including wrought | 8109.91.0000 and 8109.99.0000 | 3.7% ad valorem |

HS 2615 is the sand and concentrate trade. HS 8109 is the metal trade. They must not be added. Compound lines are outside both headings and are the chemicals chain.

## United States, USGS, not Comtrade

Units are metric tons. Ore lines are ZrO2 content, calculated by USGS as 65% of gross weight. Ore exports exclude zircon in mixed mineral concentrates. 2025 is estimated. Source: data/clean/usgs_mcs2026.csv, commodities Zirconium and Zirconium And Hafnium, salient statistics, and the PDF table on page 1.

| Flow | 2021 | 2022 | 2023 | 2024 | 2025e |
| --- | --- | --- | --- | --- | --- |
| Imports, ores and concentrates, ZrO2 content | 18,500 | 31,900 | 20,400 | 18,900 | 16,000 |
| Exports, ores and concentrates, ZrO2 content | 10,000 | 11,200 | 13,200 | 15,400 | 10,000 |
| Imports, zirconium compounds | 0 | 0 | 0 | 0 | 1,300 |
| Imports, unwrought, powder, waste and scrap | 746 | 346 | 451 | 493 | 530 |
| Exports, unwrought, powder, waste and scrap | 589 | 1,090 | 1,080 | 1,180 | 1,300 |
| Imports, wrought | 264 | 288 | 312 | 372 | 380 |
| Exports, wrought | 966 | 821 | 706 | 808 | 1,000 |

The compound line is the em dash in the USGS table for 2021 to 2024, and the footnote defines that mark as zero. The 2025 compound import is the first published tonnage.

Import shares, 2021 to 2024, are shares of U.S. imports only.

| Product | Leading origins |
| --- | --- |
| Ores and concentrates | South Africa 48%, Australia 35%, Senegal 15%, other 2% |
| Compounds | China 41%, South Africa 31%, France 12%, Australia 10%, other 6% |
| Unwrought | China 55%, Germany 15%, Canada 12%, France 7%, other 11% |
| Wrought | France 72%, Germany 10%, Belgium 7%, China 4%, other 7% |

USGS also says, without tonnage, that Australia and South Africa were the leading global exporters of mineral concentrates and that China was the leading importer. The United States was a net exporter of zirconium metal in 2025.

## European Union, PRODCOM trade indicators, not Comtrade

Dataset DS-059358, queried 7 November 2026, updated 20 October 2026. Clean file data/clean/prodcom_zirconium_codes.csv. Quantity unit is kilograms. EU and member state figures are not added together.

PRODCOM 24453063 is labelled "Articles of hafnium and germanium, n.e.s." in this dataset, not zirconium. It has trade cells only through 2021 (EU exports 3,925 kg and imports 4,328 kg in 2021) and no numeric cells for 2022 to 2024. It is not used as zirconium trade. data/clean/prodcom_24453063.csv.

24453049, unwrought zirconium and zirconium powders, excluding waste and scrap:

| Reporter | Year | Exports kg | Imports kg |
| --- | --- | --- | --- |
| EU27_2020 | 2022 | 176,226 | 559,660 |
| EU27_2020 | 2023 | 136,170 | 512,350 |
| EU27_2020 | 2024 | 138,032 | 580,820 |
| Germany | 2022 | 259,514 | 202,525 |
| Germany | 2023 | 229,112 | 246,003 |
| Germany | 2024 | 201,576 | 227,793 |
| France | 2022 | 0 | 240,876 |
| France | 2023 | 0 | 242,752 |
| France | 2024 | 0 | 256,117 |

France has no exports and no sold production of this code, and imports about 241,000 to 256,000 kg a year. That is the trade pattern of a user of unwrought metal, which is the feedstock for alloy tube. The importer is not named in the Eurostat cell.

24453050, other zirconium and articles, which can include tube and other wrought forms and is not a pure tube code:

| Reporter | Year | Exports kg | Imports kg |
| --- | --- | --- | --- |
| EU27_2020 | 2022 | 198,874 | 244,593 |
| EU27_2020 | 2023 | 164,965 | 239,568 |
| EU27_2020 | 2024 | 113,491 | 190,458 |
| Germany | 2022 | 69,085 | 141,211 |
| Germany | 2023 | 57,270 | 174,202 |
| Germany | 2024 | 41,958 | 139,669 |
| France | 2022 | 0 | 60,088 |
| France | 2023 | 0 | 50,541 |
| France | 2024 | 0 | 47,387 |

German exports of articles fall from 69,085 kg in 2022 to 41,958 kg in 2024, while German imports of articles stay near 140,000 to 174,000 kg. Sold production of this code for Germany is confidential after 2022.

## What is still missing for chapter 6

TODO(data): HS 8109 and HS 2615 world matrix, value and net weight, partners, 2019 to latest.

TODO(data): a check that EU PRODCOM exports are extra EU only. German unwrought exports in 2022 (259,514 kg) are larger than the EU export cell (176,226 kg), so the two are not the same concept.

TODO(data): zircon sand trade in PRODCOM mining codes was not queried. 24453049 and 24453050 are metal, not sand.

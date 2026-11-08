# Tungsten trade flows for chapter 6

Scope of the clean file. `data/clean/comtrade_8101_2022-2023.csv` has 305 data rows. The reporter is China only (reporter code 156). The flows are Export and Import. The years are 2022 and 2023. The commodity is HS 8101 at four digits, described in the file as tungsten and articles. Value is USD. Net weight is kilograms, and the quantity column repeats that net weight with unit kg. Partner totals excluding the World partner sum to the World row in each flow and year. This is not a world trade matrix. It does not include other reporters, earlier or later years, or the HS lines for concentrate, APT, oxides and carbide.

What HS 8101 contains, and what it does not. At six digits, which this file does not split, 8101 covers tungsten powders, unwrought tungsten including bars and rods obtained simply by sintering, wire, waste and scrap, and other articles. It does not cover tungsten ores and concentrates (HS 2611), ammonium paratungstate (the Chinese licence cites 2841801000), tungsten oxides (2825901200, 2825901910, 2825901920) or tungsten carbide (2849902000). Those are the lines named in MOFCOM and customs Announcement No. 10 of 2025, in force from 4 February 2025 [W_MOFCOM_2025_10]. A file that ends in 2023 and stops at 8101 cannot measure that licence. Weights below are gross kilograms of HS 8101 goods, not tonnes of contained tungsten, and they are not comparable to USGS mine production.

## China, World partner

| Reporter | Flow | Year | Value USD | Net weight kg |
| --- | --- | ---: | ---: | ---: |
| China | Export | 2022 | 296,601,760 | 5,744,680.17 |
| China | Export | 2023 | 268,310,154 | 5,266,365.456 |
| China | Import | 2022 | 43,354,065 | 119,064.297 |
| China | Import | 2023 | 56,256,746 | 78,264.958 |

Source: COMTRADE_8101_2022_2023, public preview API, clean file cited above. Row counts behind these four World lines are 111 export partners in 2022, 114 in 2023, 37 import partners in 2022 and 39 in 2023, plus the four World rows, which is 305.

Team calculations on the World rows, not a second source. Export value fell by about 9.5 percent and export weight by about 8.3 percent from 2022 to 2023. Export unit value was about USD 52 per kilogram in 2022 and about USD 51 per kilogram in 2023. Import value rose while import weight fell, so import unit value rose from about USD 364 per kilogram in 2022 to about USD 719 per kilogram in 2023. The import flow is a small tonnage of higher priced HS 8101 goods. It is not China's concentrate import bill.

## China exports by partner, largest by value

2022 exports. World value USD 296,601,760 and 5,744,680.17 kg.

| Partner | Value USD | Net weight kg |
| --- | ---: | ---: |
| Japan | 86,777,092 | 1,861,094.452 |
| United States | 61,183,136 | 1,274,727.073 |
| Republic of Korea | 44,178,295 | 1,024,885.562 |
| Germany | 10,649,855 | 155,602.828 |
| Other Asia, nes | 9,506,711 | 121,192 |
| Netherlands | 9,031,516 | 195,494 |
| United Kingdom | 8,843,108 | 177,581.401 |
| Israel | 8,690,226 | 154,708.707 |
| Canada | 5,706,634 | 110,709.762 |
| India | 5,361,233 | 88,808.017 |
| Russian Federation | 4,995,366 | 59,858 |
| Türkiye | 4,888,299 | 76,148.152 |

2023 exports. World value USD 268,310,154 and 5,266,365.456 kg.

| Partner | Value USD | Net weight kg |
| --- | ---: | ---: |
| Japan | 65,300,233 | 1,329,240 |
| Republic of Korea | 52,189,995 | 1,281,595 |
| United States | 47,876,461 | 978,519 |
| Israel | 13,120,131 | 255,448.662 |
| Germany | 9,745,777 | 136,464 |
| India | 8,480,127 | 159,544 |
| United Kingdom | 8,412,436 | 177,912 |
| Viet Nam | 7,945,153 | 172,196.714 |
| Other Asia, nes | 6,877,139 | 77,861 |
| Russian Federation | 6,482,084 | 84,347 |
| Netherlands | 5,076,003 | 122,847 |
| Poland | 4,366,249 | 53,740 |

Japan, Korea and the United States are the three largest export partners by value in both years. In 2023 their combined value is about 62 percent of the World export value. "Other Asia, nes" is left as the partner name in the file and is not renamed. Rank shifts that are large relative to the total include Korea moving above the United States in 2023, Israel rising from about USD 8.7 million to about USD 13.1 million, and the Netherlands falling from about USD 9.0 million to about USD 5.1 million. All of those shifts are inside HS 8101 gross weight and value. They are not shifts in APT or concentrate.

## China imports by partner, largest by value

2022 imports. World value USD 43,354,065 and 119,064.297 kg.

| Partner | Value USD | Net weight kg |
| --- | ---: | ---: |
| Japan | 19,972,974 | 20,905 |
| Republic of Korea | 5,536,644 | 14,540 |
| United States | 4,928,284 | 17,074.437 |
| Other Asia, nes | 4,316,589 | 15,894.877 |
| China | 2,405,123 | 31,125 |
| Germany | 2,216,198 | 8,742.679 |
| Canada | 746,473 | 1,745.6 |
| India | 616,372 | 492 |
| Austria | 602,665 | 3,123.727 |
| France | 574,933 | 223.149 |

2023 imports. World value USD 56,256,746 and 78,264.958 kg.

| Partner | Value USD | Net weight kg |
| --- | ---: | ---: |
| Japan | 34,532,516 | 9,543.599 |
| United States | 4,726,344 | 16,759.475 |
| Other Asia, nes | 4,335,687 | 10,204 |
| Republic of Korea | 4,149,510 | 10,539.469 |
| China | 2,983,958 | 19,254.654 |
| Germany | 1,651,805 | 2,919.468 |
| Russian Federation | 793,588 | 14 |
| India | 585,434 | 423.538 |
| France | 475,539 | 216.595 |
| United Kingdom | 387,105 | 320.45 |

The partner China on the import side is a re import. In 2023 it is 19,254.654 kg, a large share of the import weight and a much smaller share of the import value, so it pulls the average import unit value down if it is left in. It is not production from a foreign mine. Japan's 2023 import line is the opposite shape: USD 34,532,516 on only 9,543.599 kg, which is a high unit value inside an already high value import flow. The file does not say which six digit line produces that unit value.

## Other official trade facts that are not this file

United States, contained tungsten, from `data/clean/usgs_mcs2026.csv` and the MCS 2026 tungsten PDF [USGS_MCS2026_TUNGSTEN]. Imports for consumption in 2024 were 1,550 metric tons of ores and concentrates and 8,730 metric tons of other forms. Exports were 1,410 metric tons of ores and concentrates and 3,480 metric tons of other forms. The 2025 figures are estimates: imports 1,700 and 10,000 metric tons, exports 1,400 and 3,300 metric tons. Import sources for 2021 to 2024, ores, concentrates and other forms together, were China 26 percent including Hong Kong, Germany 14 percent, Bolivia 8 percent, Vietnam 8 percent and other countries 44 percent. Apparent consumption is withheld, so a net import in tonnes is not published as consumption. This United States account is contained metal and a wider product basket than HS 8101. It will not match the China reported export kilograms to the United States.

EU sold production trade in PRODCOM, gross kilograms, from DS-059358 [EUROSTAT_PRODCOM_W]. For powder and unwrought tungsten including simply sintered bars (24453014), EU27 in 2024 imported 313,001 kg valued at EUR 15,929,921 and exported 109,111 kg valued at EUR 5,448,317. For mill products (24453015), EU27 in 2024 imported 424,198 kg valued at EUR 62,929,370 and exported 168,190 kg valued at EUR 29,171,555. The API response did not label these EU rows as extra EU. Austria's trade in 24453014 is not a useful cross check on the production figure: 2024 exports and imports in that code were returned as zero while sold production was 6,440,477 kg. A zero in that cell is reported as returned, not interpreted as proof that Austrian powder does not cross a border. German production cells were duplicated across the two codes and are discussed in the material note. They are not repeated as trade findings.

## Forms the chapter 6 write up should not collapse

Concentrate moves under HS 2611 and is priced per metric ton unit of WO3. China's 2025 first batch mining quota of 58,000 tonnes is 65 percent WO3 concentrate, not an HS 8101 export [W_QUOTA_CN_2025_BATCH1]. APT moves under 2841 and is the intermediate ITIA treats as the main precursor. Oxide moves under 2825. Carbide powder moves under 2849, and the February 2025 licence covers the unsintered material, while sintered carbide tools and tungsten wire were stated to be outside it [W_MOFCOM_FAQ_2025]. Metal powder, unwrought, wire, scrap and other articles share HS 8101, which is the only line in the clean file. Mill products are the part of that heading that is wrought, and they are also the PRODCOM code 24453015. A single China export kilogram of HS 8101 is none of the concentrate, APT or carbide totals.

TODO(data): China and partner trade for 2611, 284180, 282590 and 284990, and the six digit split of 8101, for 2019 through the latest year, with value USD and net weight kg. Without those lines the 2025 licence cannot be measured in Comtrade. TODO(data): any reporter other than China. The 305 row file cannot rank world exporters.

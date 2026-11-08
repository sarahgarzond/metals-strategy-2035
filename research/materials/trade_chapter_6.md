# Global trade corridors (chapter 6 evidence)

<!-- supersedes: nothing (first note). linked from: data/source_matrix.json materials.trade_chapter_6 and CLAUDE.md chapter 6. user instruction: "continue" -->

## Key findings
1. Germany exported USD 578 million of nickel plates, sheets, strip and foil (HS 7506) in 2024 (17.8 million kg) and USD 580 million in 2023 (14.2 million kg). Value was almost flat while net weight rose about 25%, so the average export unit value fell [COMTRADE_7506, data/clean/comtrade_7506_2023-2024.csv].
2. In 2024 the largest recorded partners for German HS 7506 exports by value were Austria (USD 90.7 million, 4.04 million kg), Italy (USD 70.1 million), China (USD 61.1 million), the United States (USD 55.3 million) and France (USD 53.4 million). Spain rose into the top group at USD 44.8 million [COMTRADE_7506].
3. China exported USD 268.3 million of tungsten and articles (HS 8101) in 2023 (5.27 million kg) and imported only USD 56.3 million (0.08 million kg), remaining a large net exporter. Top 2023 export partners by value were Japan, Korea and the United States [COMTRADE_8101, data/clean/comtrade_8101_2022-2023.csv].
4. EU27 sold production of nickel plates, sheets, strip and foil (PRODCOM 24452200) was about 80.9 million kg and EUR 1.17 billion in 2024, up in tonnage from 71.4 million kg in 2023 while value eased slightly [EUROSTAT_PRODCOM, data/clean/prodcom_2019-2024.csv].
5. Most portfolio HS codes (7505 onward after a partial paced pull) are still TODO(data) because the UN Comtrade public preview quota was exceeded on 7 November 2026. HS 7502 and 7504 are now in data/clean/.
6. OECD ICIO 2025 (regular SML) is available for 2019 and 2022. World intermediate use of non ferrous metals (C24B) into electrical equipment (C27) was about USD 220 billion in 2022, into fabricated metals (C25) about USD 249 billion, and into motor vehicles (C29) about USD 109 billion [ICIO_2022_WORLD_C24B_TO_C27, ICIO_2022_WORLD_C24B_TO_C25, ICIO_2022_WORLD_C24B_TO_C29]. Iron and steel (C24A) remains larger into C25, C28 and C29. Germany domestic C24B use into C27 and C29 was about USD 5.3 billion and USD 5.7 billion respectively in 2022 [data/clean/icio_2022_metal_use_by_industry.csv].
7. UNIDO INDSTAT in data/raw/unido covers Germany value added only (2005 to 2023). Germany basic metals (ISIC 24) value added was about USD 26.1 billion in 2023 [UNIDO_DEU_VA_24_2023]. A multi country INDSTAT pull is still needed for China and peers.

## Nickel mill products (HS 7506)
Reporter in the clean file: Germany only. Years: 2023 and 2024. Flow: Export. Partners: World plus individual countries (155 rows).

| Year | Partner | Value USD | Net weight kg |
|---|---|---:|---:|
| 2023 | World | 579,954,198 | 14,237,445 |
| 2024 | World | 577,777,531 | 17,775,010 |
| 2024 | Austria | 90,693,729 | 4,043,962 |
| 2024 | Italy | 70,125,489 | 1,978,001 |
| 2024 | China | 61,095,085 | 1,828,921 |
| 2024 | USA | 55,296,090 | 1,537,896 |
| 2024 | France | 53,363,720 | 1,291,585 |
| 2024 | Spain | 44,818,938 | 1,835,603 |

Unit values should not be compared across partners without checking whether specialty alloys dominate a corridor. Kilograms of HS 7506 must not be added to other HS codes.

## Tungsten (HS 8101)
Reporter in the clean file: China only. Years: 2022 and 2023. Flows: Export and Import.

| Year | Flow | Partner | Value USD | Net weight kg |
|---|---|---|---:|---:|
| 2022 | Export | World | 296,601,760 | 5,744,680 |
| 2022 | Import | World | 43,354,065 | 119,064 |
| 2023 | Export | World | 268,310,154 | 5,266,365 |
| 2023 | Import | World | 56,256,746 | 78,265 |

Top Chinese export partners by value in 2023: Japan USD 65.3 million (1.33 million kg), Korea USD 52.2 million (1.28 million kg), United States USD 47.9 million (0.98 million kg), Israel, Germany, India, United Kingdom, Viet Nam [COMTRADE_8101].

## Stainless, cobalt, copper, aluminium, zirconium, welding, engines
TODO(data): HS 7218 to 7223, 8105, 7409, 7606, 8109, 8311, 8411, 7502, 7504, 7505, 7507. Empty titanium file comtrade_8108_2019-2024.csv has zero data rows and must not be cited.

## EU production as a trade proxy
PRODCOM sold production for nickel plate, sheet, strip and foil (24452200), EU27_2020: 2023 quantity 71,394,665 kg and value EUR 1,201,546,766; 2024 quantity 80,910,705 kg and value EUR 1,171,228,969 [EUROSTAT_PRODCOM]. Germany 2024 quantity 30,561,000 kg and value EUR 268,571,000. This supports the picture of Germany as a large European mill product location consistent with the HS 7506 export file, without proving destination shares beyond Comtrade.

## Company evidence
1. Acerinox 2025 annual report shows HPA (VDM Metals and Haynes as one group) sales of EUR 1,683 million, with melting and finishing in Europe and the United States, consistent with German and EU nickel mill product exports [research/companies/acerinox.md].
2. Outokumpu Annual Report 2025 and investor presentation describe flat stainless exports from Tornio and Avesta and a high-nickel flat capacity programme at Avesta, which would add to Nordic and German corridor competition in nickel-bearing flat products [research/companies/outokumpu.md].
3. ATI Inc. Form 10-K and earnings releases describe specialty nickel and titanium mill products shipped from the United States into aerospace and energy corridors [research/companies/ati.md].
4. Haynes International filings before the Acerinox combination, and Acerinox HPA reporting since, cover U.S. nickel alloy sheet and plate exports; treat Haynes and VDM as one Acerinox group, not two competitors [research/companies/haynes.md].

## Spotlight facts
1. In 2024 Germany exported 17.8 million kg of HS 7506 nickel plate, sheet, strip and foil worth USD 578 million, with Austria the largest partner by value [COMTRADE_7506].
2. In 2023 China exported 5.27 million kg of HS 8101 tungsten articles worth USD 268 million and imported only 0.08 million kg, a large net export position [COMTRADE_8101].
3. In 2024 EU27 sold production of nickel plate, sheet, strip and foil reached about 80.9 million kg (PRODCOM 24452200), while Germany alone sold 30.6 million kg [EUROSTAT_PRODCOM].

## Triangulation
| Number | Source 1 | Source 2 | Difference and choice |
|---|---|---|---|
| German nickel flat export scale | Comtrade HS 7506 DE World 2024 USD 578m / 17.8 Mt kg | PRODCOM DE 24452200 2024 30.6 million kg sold | Sold production exceeds recorded HS 7506 export weight because domestic sales and other HS forms are included. Use Comtrade for corridors, PRODCOM for EU production. |
| China tungsten net trade 2023 | Comtrade export USD 268m vs import USD 56m | USGS narrative of China as dominant tungsten supplier (MCS 2026) | Directionally consistent. Use Comtrade for values. |
| EU nickel flat production 2024 | PRODCOM EU27 80.9 million kg | German Comtrade export 17.8 million kg | Different measures. Do not equate. |

## Source coverage
| Source | Status | Evidence |
|---|---|---|
| UN Comtrade (tools/data/fetch.py comtrade) | used | data/clean/comtrade_7506_2023-2024.csv and data/clean/comtrade_8101_2022-2023.csv. Other required HS codes blocked by quota 7 Nov 2026. |
| World Bank Commodity Data / Pink Sheet (fetch.py pinksheet) | used | data/clean/worldbank_pinksheet_monthly.csv as price context for nickel corridors (not a flow table) |
| USGS Mineral Commodity Summaries 2026 (fetch.py usgs) | used | data/clean/usgs_mcs2026.csv for tungsten and nickel supply context behind the corridors |
| Company annual reports, 10-K/20-F, investor presentations (fetch.py sec, company IR sites) | used | research/companies/acerinox.md, outokumpu.md, ati.md, haynes.md |
| UN Comtrade for HS 7502, 7504, 7505, 7506, 7507, 8105, 8109, 7218 to 7223, 7409, 7606, 8311 | blocked | Only HS 7506 (Germany) and HS 8101 (China) downloaded. Remaining codes TODO(data) after quota reset. |
| Eurostat Comext / PRODCOM exports and imports | used | data/clean/prodcom_2019-2024.csv product 24452200 |
| OECD ICIO (inter industry and trade in value added) | used | data/raw/icio/2016-2022_SML.zip and earlier blocks. Clean: data/clean/icio_2019_2022_metal_use_by_industry.csv and data/clean/icio_2019_2022_output_va_focus.csv. Dataset row OECD_ICIO_2025. |

## Open gaps
- TODO(data): full Comtrade matrix for remaining portfolio HS codes and reporters (resume from HS 7505 after quota reset).
- TODO(data): UNIDO INDSTAT multi country extract (current file is Germany only: data/clean/unido_indstat_deu_va_2005-2023.csv).
- TODO(data): Eurostat Comext partner detail beyond PRODCOM sold production.
- Do not cite data/clean/comtrade_8108_2019-2024.csv (zero rows).

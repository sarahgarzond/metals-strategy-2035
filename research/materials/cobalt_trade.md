# Cobalt trade (chapter 6 input)

Companion to `research/materials/cobalt.md`. No UN Comtrade extract exists for cobalt. `tools/data/fetch.py` was not run. HS 8105 and HS 2605 are TODO(data).

## What was searched

`reviews/comtrade_pull.log` records the public preview pull that started with HS 8105 and HS 2605 in the code list, then HTTP 429 responses and HTTP 403 Quota Exceeded. `data/raw/comtrade/` has no file whose name contains 8105 or 2605. `data/clean/` has Comtrade extracts for HS 7506, HS 8101 and HS 8108 only. There is no `comtrade_8105` or `comtrade_2605` file.

TODO(data): UN Comtrade, HS 8105 and HS 2605, exports and imports, value in USD and net weight in kilograms, 2019 to the latest year, reporters at least Congo (Kinshasa), China, Indonesia, Finland, Norway, Canada, Japan, Germany, the United States and the EU, partners World and the main counterpart. The same gap applies to HS 2822 (cobalt oxides and hydroxides) and to the cobalt sulphate line inside HS 2833.29, which are the chemical forms and are not in the portfolio pull list in `tools/data/fetch.py`.

## Classification, not flows

USGS Mineral Commodity Summaries 2026, cobalt chapter, gives US normal trade relations tariffs as of 31 December 2025. These are duty rates. They are not quantities.

| HTS item | Code | Duty |
| --- | --- | --- |
| Cobalt ores and concentrates | 2605.00.0000 | Free |
| Cobalt oxides and hydroxides | 2822.00.0010 and 2822.00.0090 | 0.1 percent ad valorem |
| Cobalt sulfates | 2833.29.1000 | 1.4 percent ad valorem |
| Unwrought cobalt, alloys | 8105.20.3000 | 4.4 percent ad valorem |
| Unwrought cobalt, other | 8105.20.6000 | Free |
| Cobalt mattes, other intermediate products, powders | 8105.20.9000 | Free |
| Cobalt waste and scrap | 8105.30.0000 | Free |
| Wrought cobalt and cobalt articles | 8105.90.0000 | 3.7 percent ad valorem |

Source: [CO_USGS_TARIFF_2025], `data/raw/aerospace/usgs_mcs2026_cobalt.pdf`. HS 8105 is the metal, matte, powder and article chapter. HS 2605 is ore. Hydroxide, which is the DRC export form, sits in HS 2822, outside both of those chapters. A later Comtrade pull that stops at 8105 and 2605 will miss most battery feedstock.

Eurostat PRODCOM does not fill the gap. Code 24453030, mapped to unwrought cobalt in `tools/data/fetch.py`, is labelled in DS-059358 (updated 2026-10-20) as bismuth and cadmium articles. The JSON files `data/raw/prodcom/24453030_EU27_2020_2019.json` through `24453030_EU27_2020_2024.json`, and the six Germany files, have empty value arrays [CO_PRODCOM_24453030]. Code 24453010 has an empty product dimension. TODO(data): sold production, exports and imports for the live cobalt code. A Czech PRODCOM correspondence lists 24453035 as cobalt mattes, unwrought cobalt and powders. The 2025 list, on NACE Rev. 2.1, was not opened, and fetch.py was not run.

## Flows that are not HS partner trade

USGS salient statistics are US contained cobalt, not a partner matrix. Imports for consumption were 10,800 metric tons in 2024 and an estimated 14,000 metric tons in 2025. Exports were 4,880 metric tons in 2024 and an estimated 4,500 metric tons in 2025 [CO_USGS_US_TRADE_2025]. Net import reliance was an estimated 79 percent of apparent consumption in 2025. Import sources for metal, oxide and salts, 2021 to 2024, were Norway 26 percent, Finland 16 percent, Canada 14 percent, Japan 14 percent and other 30 percent [CO_USGS_US_IMPORT_SOURCES]. That is the alloy and chemical basket. It does not show DRC hydroxide.

The Cobalt Institute says the DRC was able to export approximately 41 kt of cobalt in 2025, while Indonesian mine output of 42.5 kt exceeded those exports [CO_CI_DRC_EXPORT_2025, CO_CI_IDN_2025]. Mine production continued. USGS estimates DRC mine output at 230,000 metric tons and Indonesian mine output at 44,000 metric tons in 2025 [CO_USGS_MINE_DRC_2025, CO_USGS_MINE_IDN_2025]. The export number and the mine numbers are different stages. Stocks built inside the DRC.

Refined production location is the best current map of where metal and chemicals are made. In 2025 China was 78.6 percent of refined cobalt, Finland 6.6 percent, Indonesia 3.2 percent, Canada 3.0 percent, Japan 1.7 percent and Norway 1.3 percent [CO_CI_CHINA_REF_2025]. Finland, Canada, Japan and Norway are the same names as the US import sources. Indonesia's refined share is still small, so its mine growth is mostly intermediate material.

The legal cap on what can leave the DRC is the ARECOMS quota, not a trade statistic. Up to 96,600 metric tons of contained cobalt a year in 2026 and 2027, of which 9,600 metric tons are a strategic quota, after 18,125 metric tons for the rest of 2025 [CO_USGS_QUOTA_2026, CO_IEA_ARECOMS_2025]. CMOC's reported 2026 entitlement is 31,200 metric tons against 117,549 metric tons mined in 2025 [CO_CMOC_QUOTA_2026, CO_CMOC_CO_2025]. Glencore's own sourced production was 36.1 kt in 2025, of which 33.5 kt was DRC hydroxide on the Cobalt Institute reading [CO_GLEN_CO_2025, CO_CI_GLEN_OH_2025].

## What chapter 6 should not do until the pull is rerun

Do not quote a world export total, a Chinese import total, a German import total, or a unit value in USD per tonne for HS 8105 or HS 2605. Do not use nickel or copper Comtrade files as a stand in. The Pink Sheet has no cobalt price, so a trade unit value cannot be checked against a World Bank price either [CO_WB_PINK_NO_COBALT].

## Open gaps

- TODO(data): HS 8105 and HS 2605 Comtrade flows, value and kilograms, 2019 to latest, main reporters and partners. Quota exceeded. No file on disk.
- TODO(data): HS 2822 hydroxide and oxide flows, because that is the DRC export form.
- TODO(data): PRODCOM quantities for the current cobalt code (24453030 is the wrong label in the live dataset).
- TODO(data): monthly DRC exports cleared after 16 October 2025, to see whether the 18,125 metric ton fourth quarter quota and the 2026 cap were actually shipped.

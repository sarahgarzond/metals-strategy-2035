# Copper trade

Companion to `research/materials/copper.md`. This note is for chapter 6. It separates refined cathode (HS 7403), plate, sheet and strip (HS 7409) and foil (HS 7410). Wire rod (HS 7408) is named where a source states it, because rod is the main fabricated copper product and must not be mixed into the strip balance. No UN Comtrade extract for these codes is in `data/clean`. `tools/data/fetch.py` was not run. Nothing below is a partner country matrix.

## Scope and the missing extract

TODO(data): HS 7403, HS 7409 and HS 7410, exports and imports by reporter and partner, 2019 to the latest public year, trade value in US dollars and net weight in kilograms. The team code list in `tools/data/fetch.py` describes 7403 as refined copper, unwrought, 7409 as copper plates, sheet and strip, and 7410 as copper foil. HS 7408 (copper wire, including wire rod at 7408.11) is also absent and should be pulled in the same pass so rod trade is not inferred from 7409.

Until that file exists, the only trade quantities in hand are United States salient statistics from USGS, European Union and German PRODCOM cross border totals for two codes that are not plate or foil, and qualitative tariff statements from the IEA.

## United States refined copper

USGS Mineral Commodity Summaries 2026, contained copper, thousand metric tonnes, United States.

| Flow | 2021 | 2022 | 2023 | 2024 | 2025 estimate |
| --- | --- | --- | --- | --- | --- |
| Refined imports for consumption | 919 | 732 | 771 | 903 | 1,700 |
| Refined exports | 48 | 27 | 29 | 72 | 110 |
| Ore and concentrate imports | 11 | 12 | 3 | less than 0.5 | less than 0.5 |
| Ore and concentrate exports | 344 | 351 | 339 | 326 | 340 |
| Year end refined stocks | 117 | 84 | 128 | 123 | 450 |
| Net import reliance, percent of apparent consumption | 44 | 41 | 42 | 45 | 57 |

Net import reliance is refined imports minus refined exports, plus or minus adjustments for refined copper stock changes. The 2025 jump in refined imports and in stocks is the same episode the IEA describes as front loading ahead of a possible cathode tariff. IEA Global Critical Minerals Outlook 2026, page 128, says net imports of cathode to the United States were 1.5 million tonnes and the COMEX build was 0.5 million tonnes. USGS refined imports of 1.7 million tonnes are imports for consumption, and USGS stocks of 450 thousand tonnes are held by producers, consumers and exchanges, not COMEX alone. The two pairs describe one event and are not interchangeable totals.

Import origins, copper content, 2021 to 2024, from the same USGS chapter. Refined copper: Chile 68 percent, Canada 16 percent, Peru 7 percent, Mexico 6 percent, other 3 percent. Refined copper was 88 percent of unmanufactured copper imports. Ore and concentrate: Canada more than 99 percent. Scrap: Canada 45 percent, Mexico 43 percent, other 12 percent. Blister and anodes: Finland 88 percent, Malaysia 3 percent, United Kingdom 3 percent, other 6 percent. These shares are United States only. They say nothing about German or Japanese strip imports.

The MCS normal trade relations table dated 31 December 2025 lists HS 7403.00.0000 (refined copper and copper alloys, unwrought) at 1 percent ad valorem, and HS 7408.11.0000 (wire rod of refined copper) at 1 percent or 3 percent. IEA says that in 2025 the United States put tariffs on semi finished copper products and on copper intensive derivative products, and that refined cathode was excluded but still under consideration. Plate, sheet, strip and foil are semi finished. Cathode is not. A mill that imports cathode and sells strip faces the tariff on the product it sells into the United States, not on the cathode, for as long as that exclusion holds. The duty rates and the affected HS lines inside 7409 and 7410 were not opened beyond that IEA paragraph.

## European cross border figures that are not strip

PRODCOM DS-059358, queried 7 November 2026. Quantities are kilograms of the product as disseminated, not contained copper. `data/clean/prodcom_2019-2024.csv` does not contain these rows.

Code 24442200 is copper and copper alloy bars, rods, profiles and hollow profiles, excluding cast or sintered bars and rods and excluding copper wire rod in coils. It is closer to rod, bar and profile than to strip, and it explicitly excludes coiled wire rod.

| 24442200 | EU27 sold production | EU27 exports | EU27 imports | Germany sold production | Germany exports | Germany imports |
| --- | --- | --- | --- | --- | --- | --- |
| 2024 quantity, tonnes | 902,534 (estimated) | 150,908 | 27,856 | 187,350 | 116,509 | 61,596 |
| 2024 value, million euro | 4,251 | 1,346 | 301 | 868 | 966 | 504 |

Code 24442330 is labelled "Copper wire, refined (transv. section > 6 mm), of copper alloy". The local fetcher dictionary calls this code plates, sheets and strip. The live Eurostat label does not. Treat it as a wire code until the nomenclature is confirmed against a plate code, and do not file it under HS 7409.

| 24442330 | EU27 sold production | EU27 exports | EU27 imports | Germany sold production | Germany exports | Germany imports |
| --- | --- | --- | --- | --- | --- | --- |
| 2024 quantity, tonnes | 1,963,235 | 304,737 | 47,912 | 650,073 | 361,418 | 73,828 |
| 2024 value, million euro | 11,453 | 2,791 | 438 | 2,624 | 3,284 | 653 |

German 2023 sold production for 24442330 is confidential. Several EU quantity cells in earlier years are estimated. Value divided by quantity sits below the 2024 refined copper price, so these rows are not used as a unit export price. Germany's export value exceeds its sold production value on both codes, which is possible when re exports and merchanting are in the trade total and production is only domestic sold output. That pattern is a reason to wait for Comtrade partner data before describing Germany as a net exporter of a named mill product.

Plate, sheet and strip in the PRODCOM list are code 24442400, and foil is 24442500. Neither was queried. TODO(data).

## What company reports say about geography

Aurubis Annual Report 2024/25: 27 percent of group sales in Germany and 37 percent in the rest of the European Union. The annual report says the international wire rod market is the main sales market for refined copper in Europe and worldwide, and that Aurubis primarily supplies the European market with wire rod. Flat rolled products are described as a European sales market. No export tonnes by destination for strip are given. Cathode brands are registered on COMEX, which is consistent with the ability to place cathode into the United States, and is not a strip export figure.

Japan has no USGS mine production and refined 1.570 million tonnes in 2024. Mitsubishi Materials produced 397 thousand tons of cathode in the year ended March 2025 and sold 362 thousand tons, so part of its cathode stayed inside the group or in inventory relative to production. Wrought copper product sales were 117 thousand tons. The results PDF does not give export destinations for wrought products.

China's position in the trade story, until Comtrade is pulled, is the production imbalance already in USGS. China mined 1.840 million tonnes in 2024 and refined 12.400 million tonnes. The ICSG factbook gives China 58 percent of 2024 world refined usage and 45 percent of refinery output. The implied net import is concentrate, blister and scrap, not strip. The factbook also says Asia held 84 percent of copper and copper alloy semis production in 2024, against 23 percent in 1980. That is a production share, not a trade flow.

## Open gaps

TODO(data): Comtrade HS 7403, 7409 and 7410, and HS 7408 in the same pull, for at least Germany, the European Union, China, Japan, the United States, Chile, Peru and Congo (Kinshasa), 2019 to latest.

TODO(data): PRODCOM 24442400 and 24442500 sold production, exports and imports for EU27 and Germany.

TODO(data): the legal text of the 2025 United States copper tariff, with the HS lines actually covered, so the IEA statement that semi finished products were included and cathode excluded can be cited to the proclamation rather than only to the outlook.

TODO(data): Aurubis, Wieland and Mitsubishi Materials export tonnes of strip and foil by destination. Group sales shares and wrought sales totals are not a trade matrix.

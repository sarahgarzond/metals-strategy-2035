<!-- supersedes: nothing (first creation); linked from: research/materials/nickel.md and the material-researcher task for chapter 6; user instruction: "Write research/materials/nickel.md and research/materials/nickel_trade.md. UN Comtrade quota is exceeded. comtrade_7506_2023-2024.csv (Germany nickel sheet and strip only, 2023 to 2024). Other HS codes are TODO(data): quota exceeded 7 Nov 2026." -->

# Nickel trade

Companion to research/materials/nickel.md for chapter 6. Every flow below says whether it is gross weight of a mill product or contained metal. HS 7506 and PRODCOM 24452200 do not split pure nickel from nickel alloy and do not report nickel content. VDM Metals and Haynes are one Acerinox group. The trade rows do not name either firm.

## What was on disk

UN Comtrade was not re fetched. The preview quota was already exceeded on 7 November 2026. The only nickel Comtrade file is data/clean/comtrade_7506_2023-2024.csv. It contains German exports (reporter 276) of HS 7506, "Nickel plates, sheets, strip, foil", for 2023 and 2024, partner detail plus World, value in US dollars and net weight in kilograms. The flow column is Export only. Partner rows sum to the World row in both years, so the partner list in this extract is complete for German exports. It is not a world trade matrix.

Eurostat PRODCOM, read from data/clean/prodcom_2019-2024.csv at git commit 1eae77d because the working copy was header only on 7 November 2026, supplies EU and German exports and imports for 24452100, 24452200 and 24452300. data/clean/prodcom_2023.csv confirms the 2023 EU cells for 24452200. Codes 24451100 (unwrought) and 24451230 (powders and flakes) have no published trade numbers in that extract.

## HS and PRODCOM map, and the stage each code would measure

| Code | Description in the project code list | Stage | Status in this pass |
| --- | --- | --- | --- |
| HS 2604 | Nickel ores and concentrates | Mine product, gross ore, not contained metal unless a grade is applied | TODO(data): quota exceeded 7 Nov 2026 |
| HS 7501 | Nickel mattes and intermediates | Matte and other intermediates | TODO(data): quota exceeded 7 Nov 2026 |
| HS 7502 | Unwrought nickel | Class 1 cathode and briquette, and some other unwrought forms. Not NPI | TODO(data): quota exceeded 7 Nov 2026 |
| HS 7504 | Nickel powders and flakes | Powder, a mill and melt feedstock | TODO(data): quota exceeded 7 Nov 2026 |
| HS 7505 | Nickel bars, rods, profiles, wire | Mill long products | TODO(data): quota exceeded 7 Nov 2026 |
| HS 7506 | Nickel plates, sheets, strip, foil | Mill flat products | Used: Germany exports, 2023 and 2024 only |
| HS 7507 | Nickel tubes, pipes, fittings | Mill tubular products | TODO(data): quota exceeded 7 Nov 2026 |
| HS 7508 | Other articles of nickel | Further manufactured goods | TODO(data): quota exceeded 7 Nov 2026 |
| PRODCOM 24451100 | Unwrought nickel | Class 1 and other unwrought | In the extract, no published EU or German quantities |
| PRODCOM 24451230 | Nickel powders and flakes | Powder | In the extract, no published quantities |
| PRODCOM 24452100 | Bars, rods, profiles, wire | Mill long products | Used: EU and Germany trade, 2019 to 2024 |
| PRODCOM 24452200 | Plates, sheets, strip and foil | Mill flat products | Used: EU and Germany trade and sold production |
| PRODCOM 24452300 | Tubes, pipes and fittings | Mill tubular products | Used: EU and Germany trade |

NPI and ferronickel usually move under ferro alloy or stainless headings, not under chapter 75. Those headings were not pulled for nickel. Indonesian ore does not leave the country as HS 2604 in the way Philippine ore does, because of the ore export ban. The RKAB quota of 290 million to 300 million metric tons of ore for 2026 is an upstream control, not a trade flow [NI_RKAB_2026_REV]. It is not converted to contained nickel here.

## Germany, HS 7506 exports

World totals from data/clean/comtrade_7506_2023-2024.csv.

| Year | Net weight | Value | Unit value, team calculation |
| --- | ---: | ---: | ---: |
| 2023 | 14,237,445 kg (14,237 t) | 579,954,198 US dollars | about 40,700 dollars per tonne |
| 2024 | 17,750,010 kg (17,775 t) | 577,777,531 US dollars | about 32,500 dollars per tonne |

Weight rose by about 25 percent. Dollar value was almost unchanged. The unit value is export dollars divided by net weight. It is gross product value, not a nickel price. USGS LME cash was 21,495 dollars per tonne in 2023 and 16,812 dollars per tonne in 2024. The gap between the export unit value and that cash price is about 19,200 dollars per tonne in 2023 and about 15,700 dollars per tonne in 2024. That gap is a team estimate of the fabrication premium on a mixed heading. It narrowed with the cash price. It is not a transaction price for any one alloy.

Top partners in 2024, by export value. Tonnes are net weight divided by 1,000 and rounded. Dollars are rounded to the nearest million. The unrounded file is the source.

| Partner | Value, million US dollars | Net weight, tonnes |
| --- | ---: | ---: |
| World | 578 | 17,775 |
| Austria | 91 | 4,044 |
| Italy | 70 | 1,978 |
| China | 61 | 1,829 |
| United States | 55 | 1,538 |
| France | 53 | 1,292 |
| Spain | 45 | 1,836 |
| Korea | 27 | 793 |
| India | 20 | 524 |
| Japan | 17 | 436 |
| Netherlands | 16 | 396 |
| United Kingdom | 12 | 309 |

Austria is the largest value and the largest weight. Its unit value is lower than the German average (about 22,400 dollars per tonne on the rounded figures). Italy, China, the United States and France sit at or above the average. The file does not identify the exporter. VDM Metals in North Rhine Westphalia is a known German producer of nickel alloy strip and sheet inside the Acerinox group. The statistic is national.

2023 partner structure is in the same file and is not repeated row by row. The World total is the comparison year: 14,237 tonnes and 580 million dollars.

## PRODCOM cross check, flat products

German exports of PRODCOM 24452200 in 2024 were 18,087,152 kilograms and 589,856,098 euro [NI_PC_DE_SHEET_X_2024]. Comtrade HS 7506 was 17,775 tonnes. The tonne difference is 312 tonnes, or 1.8 percent. Eurostat value is in euro and Comtrade value is in dollars, so the two values are not expected to match one for one. The 2023 EU export cell in the committed file, 31,966,424 kilograms and 1,147,776,850 euro, is the same cell as data/clean/prodcom_2023.csv.

EU trade in 24452200, 2024, from the committed extract:

| Flow | Quantity | Value |
| --- | ---: | ---: |
| Exports | 37,478,164 kg | 1,163,385,245 euro |
| Imports | 14,400,156 kg | 688,674,665 euro |

The EU is a net exporter of this heading by about 23,000 tonnes. Import unit value is higher than export unit value (about 47,800 euro per tonne against about 31,000). Germany is nearly balanced in tonnes on the same code (18,087 tonnes exported, 17,901 tonnes imported) and is a net exporter in euro (590 million against 518 million). None of this is contained nickel, and none of it is class 1 feed.

Sold production kilograms for 24452200 are in the main note and are not repeated as a trade balance. Their unit values sit below the LME price, unlike the export series, so they are a poor check on the trade tonnes.

## Long products and tube, PRODCOM only

Comtrade HS 7505 and HS 7507 were not pulled. PRODCOM is the substitute, and it is EU and national sales and trade, not a partner matrix.

German exports in 2024:

| Code | Quantity | Value | Unit value, team calculation |
| --- | ---: | ---: | ---: |
| 24452100 bar, rod, profile, wire | 1,501,390 kg | 76,614,108 euro | about 51,000 euro per tonne |
| 24452300 tube, pipe, fittings | 17,766,046 kg | 534,077,509 euro | about 30,100 euro per tonne |
| 24452200 plate, sheet, strip, foil | 18,087,152 kg | 589,856,098 euro | about 32,600 euro per tonne |

Bar exports are a small tonnage at a high unit value, which fits nickel alloy wire and bar more than commodity plate. Tube exports are almost the same tonnage as flat exports and a similar unit value. German imports of bars in 2024 were 1,281,825 kilograms and 54,309,026 euro. German imports of tube were 5,872,163 kilograms and 151,392,386 euro. Germany is a net exporter of all three mill forms in euro terms in 2024.

EU exports of bars in 2024 were 2,697,382 kilograms and 90,184,609 euro. EU imports of bars were larger, 5,577,729 kilograms and 141,520,101 euro. On bars, the EU is a net importer. On flat products and, in the export and import quantities opened for 2024, on tube (exports 16,488 tonnes, imports 4,652 tonnes), the EU is a net exporter. Sold production of bars and tube is rounded in the EU aggregate and is not used as a precise tonne balance. Unwrought nickel, the class 1 import the melt shop actually needs, is unpublished in this extract.

## What the available trade does not show

Class 1 dependence of Germany and the EU (HS 7502 and PRODCOM 24451100) is not measured. Matte and MHP (HS 7501) are not measured. Ore (HS 2604) is not measured. Nickel inside stainless flat products (HS 7219 and 7220) is not in this note. US sourcing of primary nickel is in the USGS file rather than in Comtrade: Canada 44 percent, Norway 11 percent, Australia 8 percent, Brazil 7 percent and other countries 30 percent of primary imports in 2021 to 2024, with net import reliance near 100 percent if scrap is excluded. That US pattern is not a substitute for a German unwrought import table.

LME warehouse geography is a stock, not a trade flow. INSG reports that by September 2025 Chinese origin metal was 67.85 percent of LME open tonnage, Russian origin 12.5 percent and Australian origin 9.5 percent, with Indonesian origin at 10,700 tonnes. Combined LME and SHFE stocks were 289,500 tonnes at the end of October 2025 [NI_INSG_STOCK_2025]. Those stocks are class 1 metal. They do not describe the NPI and matte that never touch the LME contract.

## Open trade gaps

TODO(data): quota exceeded 7 November 2026 for HS 2604, 7501, 7502, 7504, 7505, 7507 and 7508, and for every reporter other than Germany on HS 7506, and for German imports of HS 7506. A later Comtrade pull should cover at least reporters Germany, EU members available as national reporters, China, Indonesia, Japan, the United States, Finland and Sweden, flows export and import, years 2019 to the latest year, value and net weight.

TODO(data): restore data/clean/prodcom_2019-2024.csv from commit 1eae77d. The working copy was header only when this note was written. Confirm with Eurostat why 24451100 and 24451230 are empty and why 24452200 sold production unit values sit below the LME price.

# Titanium trade (chapter 6)

Companion to `research/materials/titanium.md`. This note records product codes, the flows that are actually measured, and the HS 8108 gap. It does not repeat the full production and 2035 outlook.

## What was not pulled

TODO(data): HS 8108 bilateral exports and imports, 2019 to the latest year, value and kilograms, by reporter and partner. `data/clean/comtrade_8108_2019-2024.csv` contains only a header. It has zero data rows and is not cited. Raw preview files under `data/raw/comtrade/` for HS 8108 were not used in place of that empty clean file. HS 2614 (titanium ores and concentrates) and titanium slag were not pulled from Comtrade either.

The flows below come from USGS import composition and from Eurostat PRODCOM. They are not a world bilateral matrix.

## Product codes by stage

USGS tariff lines, normal trade relations duty on 31 December 2025, from the titanium metal chapter and the mineral concentrates chapter (U.S. Geological Survey, 2026a, 2026b).

| Stage | Code | Duty |
| --- | --- | --- |
| Synthetic rutile | 2614.00.3000 | Free |
| Ilmenite and ilmenite sand | 2614.00.6020 | Free |
| Rutile concentrate | 2614.00.6040 | Free |
| Titanium slag | 2620.99.5000 | Free |
| Ferrotitanium and ferrosilicon titanium | 7202.91.0000 | 3.7 percent |
| Unwrought titanium (sponge and ingot sit here) | 8108.20.0000 | 15 percent |
| Waste and scrap | 8108.30.0000 | Free |
| Other articles | 8108.90.3000 | 5.5 percent |
| Wrought titanium (mill product) | 8108.90.6000 | 15 percent |
| Unfinished titanium oxides | 2823.00.0000 | 5.5 percent |
| TiO2 pigments, 80 percent or more TiO2 | 3206.11.0000 | 6 percent |
| Other TiO2 pigments | 3206.19.0000 | 6 percent |

Eurostat PRODCOM, the codes that actually describe titanium metal in the 2024 list, are 24453041 (titanium, unwrought, and powders, quantity unit kilogram) and 24453042 (bars, rods, profiles, wire, plate, sheet, strip, foil, tubes, pipes and other wrought titanium, excluding waste and scrap). Older portfolio codes such as 24453050 are zirconium articles in the current list and are not used.

## Feedstock flows

U.S. imports of titanium mineral concentrates for consumption in 2025 are estimated at 730 thousand metric tons of contained TiO2, against domestic production of 100 and exports of 10. Net import reliance is 88 percent (`data/clean/usgs_mcs2026.csv`, commodity Titanium Mineral Concentrates). Sources for all forms, 2021 to 2024: South Africa 26 percent, Canada 16 percent, Madagascar 16 percent, Mozambique 13 percent, other 29 percent.

Through July 2025 the composition was narrower by product. Slag: South Africa 65 percent, Norway 24 percent, Canada 10 percent. Ilmenite: Mozambique 44 percent, Madagascar 35 percent, Ukraine 11 percent, Senegal 9 percent. Rutile: Australia 51 percent, South Africa 20 percent, Sierra Leone 18 percent, Canada 11 percent. Synthetic rutile: Sierra Leone 78 percent, China 21 percent (U.S. Geological Survey, 2026b).

China, the largest ilmenite miner, is also a large importer of concentrates. USGS reports Chinese imports through September 2025 of 3.8 million tons in gross weight, up 5 percent on the same months of 2024, led by Mozambique (47 percent), Australia (17 percent) and Norway (7 percent). Gross weight is not contained TiO2. This is the main South to East feedstock route in the public record. A full Comtrade HS 2614 matrix is still TODO(data).

## Sponge and scrap flows

U.S. sponge imports for consumption, metric tons, estimated where marked: 16,000 (2021), 30,900 (2022), 40,300 (2023), 39,800 (2024), 44,000 (2025). Exports in those years were 117, 105, 247, 70 and 63 metric tons. Apparent consumption tracks imports because domestic sponge production in 2025 is zero [TI_SPONGE_US_IMPORT_2025]. Customs value was about USD 447 million in 2024 and about USD 460 million in 2025. The landed duty paid unit value was USD 13.30 per kilogram in 2024 and an estimated USD 12 per kilogram in 2025. Those are different measures. The 15 percent duty on 8108.20 is one reason they diverge.

Import sources, 2021 to 2024: Japan 77 percent, Saudi Arabia 13 percent, Kazakhstan 8 percent, other 2 percent. Through July 2025: Japan 73 percent, Kazakhstan 13 percent, Saudi Arabia 13 percent. Russia is a sponge producer (25,000 metric tons estimated in 2025) and is not among the leading U.S. sponge sources in this window. China is the largest sponge producer (260,000 metric tons) and is not a leading U.S. sponge source either. The aerospace qualified import route into the United States is Japan, Kazakhstan and Saudi Arabia.

U.S. scrap imports are estimated at 32,000 metric tons in 2025. Through July 2025 the leaders were the United Kingdom (19 percent), France and Japan (10 percent each), and Germany, the Republic of Korea and Singapore (9 percent each). Scrap enters free of duty under 8108.30 and is an ingot feedstock. The duty paid unit value was about USD 7.70 per kilogram through July 2025, against about USD 8.50 per kilogram for the 2024 average.

The fiscal 2025 U.S. stockpile plan allowed potential acquisition of 15,000 metric tons of titanium and potential disposal of 136 metric tons of titanium alloys. The fiscal 2026 plan was not released.

## European unwrought and wrought trade

Eurostat PRODCOM DS-059358, EU27, 2024, kilograms converted to metric tons by dividing by 1,000. https://ec.europa.eu/eurostat/web/prodcom/database

| Flow | 24453041 unwrought and powders | 24453042 wrought forms |
| --- | ---: | ---: |
| Sold production | 1,110 t, EUR 65.1 million | 22,617 t, EUR 534.9 million |
| Exports | 2,252 t, EUR 24.0 million | 5,858 t, EUR 617.1 million |
| Imports | 18,296 t, EUR 294.4 million | 31,667 t, EUR 1,817.2 million |

Germany sold 1,108 metric tons of the unwrought code in 2024, essentially the whole EU quantity. France published a zero for that code in 2024. On the wrought code, France sold 9,652 metric tons and Germany 1,662. USGS shows no sponge capacity in Germany, so the German unwrought sales are not Kroll sponge.

Calculated 2024 import unit values are EUR 16.09 per kilogram unwrought and EUR 57.39 per kilogram wrought. The EU is a large net importer of both codes. Direction of trade inside the EU, and trade with Japan, Kazakhstan, Saudi Arabia, Russia and China at HS six digit level, is TODO(data) until HS 8108 Comtrade is re-pulled.

## Reading the flows for chapter 6

Three routes should stay separate in the trade chapter.

Feedstock moves from Mozambique, South Africa, Madagascar, Australia, Norway and Canada toward pigment plants and toward China. The U.S. ore duty is zero and U.S. reliance on imported concentrates is 88 percent, while the United States is a net exporter of pigment.

Aerospace sponge moves from Japan, Kazakhstan and Saudi Arabia into the United States, under a 15 percent unwrought duty, into a country with zero operating sponge capacity. Industrial Chinese sponge is the volume of world production and is not this U.S. import mix.

Wrought mill product is the high unit value EU import (about EUR 57 per kilogram in 2024) and the form Boeing names in its 2025 Form 10-K (sheet, plate, forgings and extrusions). Scrap moves the other way, including from the United Kingdom, France, Japan, Germany, Korea and Singapore into U.S. melters, duty free.

Until HS 8108 and HS 2614 are in a clean Comtrade file, chapter 6 should cite these USGS shares and PRODCOM totals and should mark world bilateral tonnes as missing.

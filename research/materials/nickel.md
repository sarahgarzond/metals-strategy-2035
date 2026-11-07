# Nickel and nickel alloys: raw research notes (Stage 1)

Retrieved 2026-11-07. All numbers are in data/sources.csv under the data_ids named below.

## Access log
- Worked: USGS MCS 2026 nickel PDF via curl (data/raw/usgs_mcs2026_nickel.pdf), World Bank Pink Sheet annual and monthly xlsx via thedocs.worldbank.org (data/raw/), UN Comtrade public preview (data/raw/comtrade_*.json, rate limit 429 needs 4 s pauses).
- Blocked (not resolvable or proxy 403): kitco.com, argusmedia.com, natural-resources.canada.ca, nickelinstitute.org, insg.org, iea.org and iea.blob.core.windows.net, sciencebase.gov. WebSearch budget ran out before IEA 2035 and Western alloy capacity searches finished.
- IEA, INSG, Nickel Institute, Argus and Nornickel figures are taken from search summaries only (confidence low or medium) and must be checked.

## 1 Production
World mine 3.9 Mt 2025 (USGS_NI_MINE_2025), 3.71 Mt 2024. Indonesia 2.6 Mt (67%), Philippines 270 kt, Russia 200 kt, Canada 140, New Caledonia 140, China 120, Brazil 70, Australia 45 (USGS_NI_*_2025). Reserves more than 140 Mt, Indonesia 62 Mt (USGS_NI_RES_2025). Nornickel 199 kt (NORNICKEL_NI_2025). Indonesia refining share 43% (UNCTAD_NI_REFINE_2026), capacity above 2.7 Mt (FINI_NI_CAP_2025).
TODO(data): Vale Base Metals, Glencore, BHP Nickel West, Eramet, Sumitomo 2025 output (search returned only headlines). Class 1 versus Class 2 share of supply.

## 2 Trade (HS 2024, sum of reporters in preview API, understated)
7501 China imports USD 7.6bn, Indonesia 6.2bn. 7502 X 11.39bn/638 kt, M 12.32bn/668 kt. 7505 X 4.98bn/133 kt (USA 1.40, Germany 0.64, France 0.43), M 4.89bn. 7506 X 1.95bn/64 kt (Germany 0.58, USA 0.48, Japan 0.27, Sweden 0.18), M 2.02bn (China 0.28). 7507 X 1.72bn, M 1.60bn. 7508 X 3.59bn (not logged, mixed articles). Germany 7506 destinations: Austria, Italy, China, USA. Germany 7505 destinations: UK, USA, Italy, France, Spain, China. US 7505 origins: Germany, France, Italy, Australia, Sweden.
TODO(data): time series 2015 to 2024 for growth, HS 7503 scrap, 7508.

## 3 Consumption
Split 66% stainless, 16% batteries, 6% alloys, 5% plating, 3% alloy steel (NICKEL_USE_SPLIT_2024, medium). NRCan variant 64/15/9/5/7. US reported primary consumption 120 kt 2025, scrap about 60% of apparent consumption (USGS_NI_US_RECYC_2025). TODO(data): regional split China/Europe/US/Japan.

## 4 Applications
Superalloys (engines, gas turbines), corrosion alloys (Alloy C-276, chemical, flue gas), low expansion FeNi36, heating NiCr, battery connectors, AM powders. Substitutes per USGS: duplex and low nickel stainless, titanium. Widebody engine deliveries H1 2026 269 vs 222, Rolls Royce 157 vs 122 (ARGUS_ENGINES_H1_2026).

## 5 Market size
Contained mine value USD 59bn (TE_NI_MINE_VALUE_2025). Semis export value USD 8.65bn 2024 (TE_NI_SEMIS_TRADE_2024). Aerospace superalloy market USD 1.25bn (GII, triangulation only). TODO(data): EUR value from Eurostat PRODCOM 24.45 nickel and 24.44 products, history 2015 to 2025.

## 6 Prices
Annual LME nominal USD/t: 2000 8,638, 2007 37,230, 2015 11,863, 2022 25,834, 2023 21,521, 2024 16,814, 2025 15,162 (WB_NI_*). 2026 Jan to Oct average 17,154 (WB_NI_2026_YTD), May 18,806, Oct 15,436. USGS: 2025 average about 15,000, down 11%. Drivers: Indonesian RKAB quotas (379 Mwt 2025, 260 to 270 initial 2026, revised 290 to 300), royalties 11 to 19% (SPGLOBAL_RKAB_2026), INSG surplus 182 kt 2024, 19 kt 2026 (INSG_NI_2026).

## 7 Capacity and supply
Indonesian MHP capacity above 900 kt Ni by end 2027. Australia care and maintenance, Philippines Palawan permit ban. Western alloys: ATI fifth VIM Monroe 9 kt/yr H2 2027 (ARGUS_SUPERALLOY), Acerinox plus Haynes plus VDM (ACX_HAYNES). TODO(data): VDM Metals, Special Metals, Carpenter, Aperam capacity from annual reports. Export policy: Indonesia ore export ban since 2020 (not yet sourced, TODO).

## 8 Outlook 2035
IEA STEPS nickel demand 5,689 kt in 2040 (2025 edition, snippet). TODO(data): IEA Critical Minerals Data Explorer download for 2035 STEPS and APS, by end use. INSG surplus to widen 2027.

## Interesting facts (dated, named)
1. 2025: Australia nickel mine output down about 54% to 45 kt (USGS).
2. 2025: Philippines announces 50 year Palawan mining permit ban.
3. Nov 2024: Acerinox completes Haynes deal, joins VDM Metals, USD 71m synergies.
4. H2 2027: ATI fifth VIM furnace Monroe NC, 9 kt/yr.
5. 13 Oct 2026: INSG flips 2026 view from deficit 32 kt to surplus 19 kt.

## Data chain table
See sections/02_2_nickel.md, section Data chain.

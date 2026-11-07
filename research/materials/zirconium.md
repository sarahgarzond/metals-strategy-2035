# Zirconium research notes (Phase I, section 2.4)

Retrieved 2026-11-07. All numbers are in data/sources.csv under the data_ids named here. Raw files are in data/raw/.

## Access notes
- USGS MCS 2026 Zirconium and Hafnium PDF downloaded by curl: data/raw/mcs2026-zirconium-hafnium.pdf (primary, high). The earlier TODO row USGS_ZR_2025 is replaced.
- UN Comtrade public preview worked (partner 0, annual). Raw JSON: data/raw/comtrade_*.json for HS 8109 (X and M, 2019 and 2024), 261510 (X and M, 2019 and 2024), 810921, 810991, 282560 (X 2024) and US partner detail. The endpoint returns only reporters that filed, so France (main nuclear metal exporter) is absent in 8109, 810921 and 810991. Sums are labelled "sum of reporters".
- Blocked hosts (DNS or 403 from the session): argusmedia.com, world-nuclear-news.org, iluka.com, atimaterials.com, iea.org (403). Figures from these come from WebSearch summaries and are logged with confidence low or medium and the note "seen via search summary". They need a manual check once the hosts are allowed.
- The World Bank Pink Sheet and LME carry no zirconium or hafnium series.

## 1 Production
World zircon concentrate 1,200 kt in 2025 (1,300 kt in 2024) [USGS_ZR_2025]. Australia 400, South Africa 270, Mozambique 160, China 100, Senegal 70, Indonesia 52, Madagascar 26, Sierra Leone 25, US 100 (rounded), other 40 (country rows USGS_ZR_AUS_2025, _ZAF_, _MOZ_, _OTHER_). Reserves above 70,000 kt ZrO2 [USGS_ZR_RES_2025]. Inconsistency inside USGS: text says about 1 million t and a 12% fall, table says 1,200 kt (2024 revised to 1,300). Table used.
Metal: US has one zirconium and one hafnium metal producer (Oregon, Utah). Framatome claims 30% of cladding and sponge [FRAM_SHARE]. Four LWR fuel fabricators: Framatome, GNF, TVEL, Westinghouse. TODO(data): sponge capacity per plant (Framatome Jarrie, Westinghouse/Western Zirconium Ogden, ATI Albany, TVEL Chepetsk, CNNC plants in China). Searched: company pages, Argus, market notes. Found only vendor pages with conflicting claims (one wrongly places a Westinghouse sponge plant at Springfields), so not used.

## 2 Trade
- HS 261510 ore: exports 1,403.5 USD m 2024 (South Africa 610.2), imports 2,196.2 USD m (China 1,368.0) [CT_261510_X_2024, CT_261510_M_2024]. Growth 2019 to 2024 imports 3.8% p.a., exports 5.0% p.a. (team estimate: (1403.5/1099.3)^(1/5)-1).
- HS 8109: imports 507.2 USD m, 5,217 t; exports 397.3 USD m, 11,314 t in 2024 (2019: 385.7 and 9,018 t imports, 258.0 and 18,750 t exports). Value up 5.6% p.a. on imports, weight down. Reporter counts differ (98 vs 102 imports), so unit values are indicative.
- USA exports 197.6 USD m, imports 118.4 USD m with France 79.7 (67%). USGS: France 72% of US wrought imports 2021 to 2024.
- Nuclear proxies (HS 2022 subheadings, hafnium free): 810921 exports 107.8 USD m (China 64.0, USA 36.8), 810991 exports 180.5 USD m (USA 125.2).
- HS 282560 mixes zirconium dioxide with germanium oxides: 380.4 USD m exports 2024.

## 3 Consumption
Ceramics 54% (ZIA via summary, low), foundry plus refractories 27% (Kenmare, medium). Chemicals and metal are the remainder. TODO(data): zircon tonnage going to sponge and chemicals, searched ZIA, USGS, trade press.
US apparent consumption of concentrates under 100 kt, imports 16 kt ZrO2 in 2025 (USGS).

## 4 Applications
Nuclear cladding and structure (Zircaloy family, low neutron absorption, hafnium removed). Chemical process equipment in Zr 702 and Zr 705: acetic acid, hot sulfuric up to about 70% (702C) and 55% (705C) [ZR702_H2SO4]; unsuitable for HF, wet chlorine, FeCl3 and CuCl2. Hafnium: superalloys, control rods, chips. Substitutes per USGS [USGS_ZR_SUBST]. TODO(data): equipment share by process (acetic acid, urea, hydrogen peroxide) not found.

## 5 Market size
Triangulation: HS 8109 imports 507 USD m (primary, partial coverage), DIResearch metal 593 USD m 2025, Spherical Insights nuclear grade metal 531 USD m 2024, whole zirconium market 2.1 to 2.3 bn USD (SNS, Emergen, IMARC, Reports and Data). Working size USD 0.5 to 0.6bn for metal and semifinished (team estimate). Client share of roughly EUR 50bn market: about 1% (team estimate, needs currency conversion note in appendix).

## 6 Prices
Zircon CIF China 1,530 (2021), 2,300 (2022), 2,160, 2,000, 1,800 USD/t (2025) [USGS_ZR_PRICE_2025]. Sponge ex works China 25, 30, 28, 24, 22 USD/kg. Hafnium 781, 1,590, 6,130, 4,560, 3,800 USD/kg annual average; spot about 13,115 USD/kg April 2026 (SMM, low). China zircon sand +4.3% m/m July 2026 (ChemAnalyst, low); Q1 2026 Australia price -1.91% (Price-Watch, not logged). Drivers: heavy mineral sand supply cuts, China tile demand, nuclear restarts, hafnium licensing, US tariff about 79% on Chinese hafnium (Argus via SMM).

## 7 Capacity and supply
Iluka guides about 180 kt zircon 2026 with Cataby and SR2 idle; Iluka 2025 zircon, rutile and SR output 559 kt; Eneabba refinery commissioning 2027 (A$1,101m spent by June 2026; rare earths, not zircon). Mozambique rising 124 to 160 kt. China hafnium exports down about 90% during 2025. Unverified commentary (not used in report): Western Zirconium force majeure January 2025 after an 11-week Kroll reactor outage, and 38% Russian origin in a European fabricator's 2024 sponge inventory (source: a low quality newswire page, no primary document).

## 8 Outlook to 2035
IEA: nuclear capacity up at least one third, up to 70%, by 2035; 63 reactors, more than 70 GW under construction; STEPS nearly 650 GW 2050; SMRs 40 GW 2050 [IEA_NUC_2035]. Base case cladding demand growth about 2.9% p.a. (team estimate 1.33^0.1-1; assumption proportional to capacity; ignores burnup, SMR designs and SiC). Market reports: 5.2 to 7.9% p.a. whole market. Risks: SiC cladding and non-zirconium SMR designs [ZIA_NUCLEAR], Russia, China hafnium. TODO(data): IEA Nuclear dataset to be downloaded by hand into data/raw/. TODO(data): Zr 702 chemical equipment demand forecast.

## Data chain table
| Material | Product form | Application | Industry | Geography | Market size | Growth |
|---|---|---|---|---|---|---|
| Zirconium | Zircon sand (261510) | Tiles, foundry, refractories | Ceramics, foundry | China 62% of imports | 2,196 USD m imports 2024 | 3.8% p.a. 2019 to 2024 |
| Zirconium | Zirconia, chemicals (282560) | Ceramics, catalysts | Ceramics, chemicals | China, Japan, USA | 380 USD m exports | TODO(data) |
| Zirconium | Hafnium free unwrought (810921) | Cladding feedstock | Nuclear | China, USA | 108 USD m exports | about 2.9% p.a. to 2035 (est.) |
| Zirconium | Hafnium free articles (810991) | Tubes, components | Nuclear | USA, Japan, Sweden | 181 USD m exports | about 2.9% p.a. (est.) |
| Zirconium | Zr 702/705 strip, sheet, plate, bar, tube | Process equipment | Chemical | USA, Germany, Asia | 0.5 to 0.6 bn USD (HS 8109) | 5.6% p.a. value 2019 to 2024 |
| Hafnium | Unwrought | Superalloys, control rods, chips | Aerospace, nuclear, electronics | China, France, Germany, USA | 70 to 75 t/yr | TODO(data) |

## Interesting facts (dated, named)
1. 2025: China cut reported unwrought hafnium exports from 5,001 kg (January) to 499 kg (September); a trader reported no export licence since October 2024; hafnium superalloy and nuclear buyers in Japan, South Korea, US affected (SMM citing Argus).
2. April 2026: overseas hafnium spot about 13,115 USD/kg versus about 5,000 USD/kg until October 2025, driven by gas turbine superalloy (data centre power) and chip demand (SMM).
3. July 2026: Iluka (Australia) guides 180 kt zircon for 2026, Cataby and SR2 idle since late 2025, tightening feed for Chinese zircon and sponge chains.
4. 2024: China exported 911.9 t of hafnium free unwrought zirconium (64.0 USD m), the USA 801 t (36.8 USD m); USA exported 640.8 t of hafnium free articles (125.2 USD m) (UN Comtrade).
5. 2021 to 2024: France supplied 72% of US wrought zirconium imports (USGS), pointing to Framatome and French fabricators as likely suppliers (team inference).

## Gaps
Sponge capacity per plant, Russian share, nuclear versus chemical split of metal demand, Zr 702 customer and competitor list (ATI, Western Zirconium, Alleima, VDM Metals, Chinese mills), IEA dataset, hafnium trade quantities, Pink Sheet series (none exists).

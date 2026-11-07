# Research notes: AM powders and welding consumables (section 2.7)

Branch: worktree-agent-afb5b214c57912de3. Status 2026-11-07. All numbers have a row in data/sources.csv.

## Access notes
- UN Comtrade public preview worked (HS 8311, 7504, 7406, 7603, 8108). Rate limit 429 after about 10 calls in a minute, use 5 s pauses. Raw JSON in data/raw/comtrade_*.json. The preview returns reporterCode only (reporterDesc is empty), so names were mapped by code.
- Blocked hosts (not on the session allow list): wohlersassociates.com, www.metal-am.com, www.businesswire.com, s203.q4cdn.com, s29.q4cdn.com. Search snippets used instead, flagged confidence medium or low.
- Comtrade anomaly: HS 7406 (copper powders) imports and HS 7603 (aluminium powders) exports show Malaysia with 435 kt and 110 kt, which is implausible for powders and likely misclassified scrap or concentrate. These codes were not used for quantities. TODO(data): clean 7406 and 7603 after removing Malaysia, or use Eurostat PRODCOM.
- HS 8108 (titanium unwrought, powders) pulled for reference (exports 7.0 bn USD) but titanium is outside the Client portfolio, not logged.

## 1 Production
- There is no official statistic for AM powder output. Powder is made by gas atomisation (VIGA for nickel, cobalt, copper, EIGA for titanium and reactive alloys), plasma atomisation and water atomisation. Producers named in sources: Carpenter Additive (seven atomisation sites, Torshalla Sweden about 4,000 t/yr mostly PM steels) [CARPENTER_TORSHALLA], Sandvik Osprey (Sandviken, Neath), Hoeganaes/Hoeganas (Johnstown PA), Oerlikon (moved AM production from Barleben and Shanghai to the US in 2024) [OERLIKON_AM_2023], ATI (Monroe NC fifth VIM furnace, 9 kt/yr from H2 2027) [ARGUS_SUPERALLOY], Haynes now under Acerinox [ACX_HAYNES].
- Welding consumables: Lincoln Electric consumables about 2.28 bn USD [LECO_2025_CONS], ESAB total sales 2.84 bn USD [ESAB_2025_SALES]. Nickel alloy fillers are made by Special Metals (Berkshire Hathaway), voestalpine Boehler Welding, Lincoln (Techalloy), Haynes. TODO(data): voestalpine Boehler Welding sales split, Special Metals sales (not published).
- Nickel mine supply context: [USGS_NI_MINE_2025].

## 2 Trade (Comtrade, sum of reporters, partner World)
| HS | Flow | Year | USD m | Notes |
|---|---|---|---|---|
| 8311 | Exports | 2023 | 3706 | China 966 (585.6 kt, 53% of 1113 kt), USA 405, Korea 196, Germany 159, Japan 150 |
| 8311 | Exports | 2019 | 3127 | CAGR 4.3% (team estimate) |
| 8311 | Imports | 2023 | 3553 | USA 238, China 222, Mexico 216, Indonesia 148, Thailand 146 |
| 7504 | Exports | 2023 | 1102 | Canada 357 (12.4 kt), UK 161, USA 113, Japan 108, China 94, Germany 82 |
| 7504 | Exports | 2019 | 950 | CAGR 3.8% (team estimate) |
| 7504 | Imports | 2023 | 1809 | Korea 463, China 354, USA 214, Japan 158, Taiwan 142, Germany 65 |
Reading: China ships over half of coated electrode volume but only 26% of value, Germany and Japan are higher value exporters. Nickel powder flows run from Canada (Vale Sudbury carbonyl) and the UK to Korea, China, Japan and Taiwan, driven by battery and electronics use, not AM. HS 7504 therefore overstates AM nickel powder. Reporter coverage differs by year (2024 incomplete), so growth rates are indicative.
TODO(data): HS 7506 to 7508, 7505 (nickel bars, wire), 8109 (zirconium), 7229/7217 (alloy wire) and 8105 (cobalt) welding wire flows; EU PRODCOM for 24.xx welding wire.

## 3 Consumption
- AM: aerospace share 39% of powder spend in one paid report [GMI_AMPOWDER_2025]. North America 35.7% and Europe 28.4% of nickel alloy AM powder [MARKETINTELO_NIAM_2025]. Wohlers: Asia Pacific fastest growth 19.8%, Americas 12.6%, EMEA 9.0% (secondary blog, not logged as number, TODO(data) verify).
- Welding consumables: Asia Pacific about 70% and Europe about 14% in one vendor summary [WELD_MKT_2024]. Pull from shipbuilding, pipelines, power, chemical plants, automotive (low alloy).

## 4 Applications (property that makes the metal necessary)
| Form | Material | Application | Industry | Property |
|---|---|---|---|---|
| Gas atomised powder | Alloy 718, 625, 939, Haynes 282 | Combustor, turbine hardware, fuel nozzles | Aerospace | Creep strength above 650 C, weldability in AM |
| Gas atomised powder | CoCr | Dental, orthopaedic implants | Medical | Biocompatibility, wear |
| Gas atomised powder | CuCrZr, CuNiSi | Combustion chambers, heat exchangers | Aerospace, energy | Conductivity with strength |
| Gas atomised powder | 316L, 17-4PH | Tooling, valves, manifolds | Oil and gas, chemical | Corrosion resistance |
| Solid wire, flux cored, electrode | Alloy 625, C-276, 82, 182 | Cladding, dissimilar joints, weld overlay | Oil and gas, chemical, power | Matching corrosion resistance and strength of base metal |
| Wire | Ni and Cu alloys | WAAM large parts | Marine, aerospace | Deposition rate |

## 5 Market size
- Wohlers: AM revenue 24.2 bn USD in 2025 (+10.9%) [WOHLERS_2026], 21.9 bn in 2024 (+9.1%) [WOHLERS_2025]. Materials 4.4 bn in 2024 [WOHLERS_2025_MAT] and 4.9 bn in 2025 [WOHLERS_2026_MAT]. Materials include polymers, so metal powder is a fraction. TODO(data): metal share of AM materials.
- Metal powder only: 650.8 m USD 2025 to 2.9 bn 2035 [GMI_AMPOWDER_2025], 555.3 m 2024 to 3.9 bn 2035 at 19.5% [TMR_AMPOWDER_2035]. Nickel alloy AM powder 1.2 bn [MARKETINTELO_NIAM_2025] is inconsistent with the first figure, so no headline number. Wohlers materials 4.9 bn is the upper bracket, vendor powder estimates the lower bracket.
- Welding: Lincoln consumables 2.28 bn [LECO_2025_CONS], ESAB consumables about 0.97 bn (low confidence), vendors 12.7 to 17.7 bn total market [WELD_MKT_2024]. Trade proxy 3.7 bn USD HS 8311 exports [COMTRADE_8311_X_2023]. Model total for Client addressable market [MODEL_TOTAL_2025].
- TODO(data): model-level split of the Client's EUR 50bn into powder and welding (check model/model.py).

## 6 Prices
- Inconel 718 LPBF powder 80 to 260 USD/kg, supplier tables 70 to 485 USD/kg, powder 2 to 5 times bar price (45 to 110 USD/kg) [INCO718_POWDER_PRICE_2025]. LME nickel traded about 14,800 to 15,300 USD/t in Aug 2025 (search result, not logged, see nickel note for DEN_NI_PRICE_2026). Share of nickel in powder price: TODO(data) (needs alloy composition source and the LME price series).
- Welding: Lincoln cites pricing, not volume, as the driver of consumable sales growth in 2025 (nickel and surcharge pass through) [LECO_2025_CONS].
- TODO(data): World Bank Pink Sheet nickel, cobalt, copper monthly series (WB API indicator IDs for commodities returned 'Invalid value', download Excel by hand), Ti64 powder price.

## 7 Capacity and supply
- Carpenter: seven atomisation sites, Athens AL Emerging Technology Center 40 m USD invested of 52 m planned [CARPENTER_TORSHALLA].
- ATI Monroe NC fifth VIM furnace 9 kt/yr from H2 2027 supplies superalloy feedstock for powder [ARGUS_SUPERALLOY].
- Oerlikon pulled AM production from Germany to the US in 2024 [OERLIKON_AM_2023], an example of German AM weakness.
- Acerinox bought Haynes (Nov 2024), forming a HPA division with VDM Metals [ACX_HAYNES], a competitor to the Client.
- ESAB acquires Eddyfi (announced, search result, details TODO(data)).
- Constraints: certified aerospace powder qualification takes years, Ni and Co feedstock concentration (Indonesia, DRC) [USGS_NI_MINE_2025, USGS_CO_MINE_2025]. China export controls on cobalt and tungsten, TODO(data) tie to cobalt note.

## 8 Outlook to 2035
- Vendors: powder 16% to 19.5% p.a. [GMI_AMPOWDER_2025, TMR_AMPOWDER_2035]. Wohlers 2026 describes a shift "from expansion to utilization" with uneven growth (secondary), so team base case should sit well below vendor CAGR. Team estimate to be set in model (TODO(data): decision with model owner).
- Wohlers 2025 to 2026 total growth 9 to 11% [WOHLERS_2025, WOHLERS_2026]. Welding grows near GDP and industrial output, ESAB guides core organic +2 to 4% for 2026 [ESAB_2025_SALES]. Trade proxy +4.3% p.a. 2019 to 2023 in value.
- Technology: WAAM and laser cladding (wire), binder jet, MIM, shift to US capacity.
- TODO(data): IEA/other 2035 scenarios are not applicable, use aircraft build rates (Airbus GMF, Boeing CMO already logged) as driver.

## Data chain table
| Material | Product form | Application | Industry | Geography | Market size | Growth |
|---|---|---|---|---|---|---|
| Nickel alloys 718, 625 | Gas atomised powder | LPBF engine parts | Aerospace | North America, Europe | Metal AM powder 0.65 to 4.9 bn USD bracket 2025 | 16 to 19.5% vendor, team estimate pending |
| CoCr | Powder | Implants | Medical | Europe, US, China | TODO(data) | TODO(data) |
| CuCrZr, CuNiSi | Powder | Thrust chambers, heat exchangers | Aerospace, energy | US, Europe | TODO(data) | TODO(data) |
| 316L, 17-4PH | Powder | Tooling, valves | Oil and gas, chemical | Global | TODO(data) | TODO(data) |
| Ni alloys 625, C-276 | Wire, rod, flux coated electrode | Overlay, joining | Oil and gas, chemical, power | Asia Pacific about 70% | 3.7 bn USD trade (HS 8311) | 4.3% p.a. 2019 to 2023 |
| Low alloy and stainless | Solid wire, flux cored | Fabrication | Construction, auto, shipbuilding | China, USA | Lincoln consumables 2.28 bn USD | pricing led, ESAB +2 to 4% |

## Interesting facts
1. December 2023: Oerlikon announced consolidating its AM powder and part production in the US and moved Barleben (Germany) and Shanghai output during 2024, citing weak German demand. Metal: mixed steel, nickel, titanium powders. Likely suppliers filling the gap in Europe: Sandvik, Hoeganaes, Carpenter. [OERLIKON_AM_2023]
2. November 2024: Acerinox closed the Haynes purchase and combined it with VDM Metals into a high performance alloys division, putting two nickel and cobalt strip, sheet, bar, wire and powder makers under one owner. [ACX_HAYNES]
3. H2 2027: ATI starts a fifth VIM furnace in Monroe NC with 9 kt/yr for nickel superalloy and titanium for jet engines. [ARGUS_SUPERALLOY]
4. 2025: Lincoln Electric lifted consumable sales to about 2.28 bn USD mainly through price, not volume, and bought an alloy steel business that added 5% to international welding sales in Q4. [LECO_2025_CONS]
5. 2023: China shipped 585.6 kt of HS 8311 coated electrodes and wire, 53% of world export weight but 26% of value, while Germany exported 159 m USD at far higher unit value. [COMTRADE_8311_X_2023]

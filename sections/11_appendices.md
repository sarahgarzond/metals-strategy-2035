# Appendices: Data, Sources, Calculations, and Assumptions

## A1 Definitions and the stage ladder

The report uses Mt for million tonnes, kt for thousand tonnes, t for metric tonnes, GW for gigawatts and bcm for billion cubic metres, and all prices are in current US dollars or euros of the year stated. The stage ladder separates five rungs that are never added together: mine output of contained metal, refined metal or intermediate such as nickel pig iron or cobalt hydroxide, alloy melt, mill product such as strip, sheet, plate, bar and wire, and finished component. Contained metal is kept apart from gross weight, actual output from capacity, and commodity benchmarks such as the World Bank Pink Sheet from the selling price of qualified alloy products.

## A2 Outlook model, backtest and opportunity scoring

The tier 1 model of chapter 7 is fully reproducible from the repository, and this appendix documents its formulas, parameters, backtest, simulation settings and the scoring rules of chapter 8. Every value is a team estimate unless a source is given, and running python3 model/outlook_2035.py from the repository root rewrites data/clean/model_tier1_results.csv, model_backtest.csv, model_calibration.csv, model_supply_overlay.csv, model_tier2_register.csv, research/model/outlook_results.md and Figures 3 and 4 with identical numbers, while the option --no-log skips the update of the source register [MODEL_T1_RESULTS_2035].

### A2.1 Formulas and simulation settings

For each industry j with components k, such as new engines and aftermarket in aerospace, the 2035 index is I(j) = 100 × Σ w(k) × A(k) × (1 + i(k))^10 × S(k) × exp(10 × (Δg(j) + σ(j) × ε)). Here A is the activity ratio 2035 to 2025, i the annual trend of alloy mass per unit, S the ratio of the high performance alloy share, w the component weight, Δg the backtest shift and σ the backtest error carried into the range, with ε a standard normal draw. The shift is Δg = −λ × e, where e is the mean annual growth error of the real backtest series of the industry, λ = 0.5 and the shift is capped at 1 percentage point a year, while σ = κ × the root mean square growth error of all series of the industry, with κ = 0.5 and a cap of 3 percentage points. A product family index is the weighted sum of the industry indices with the weights of Table A1, and cobalt tonnes multiply the 2025 base by the index and by the cobalt content ratio.

The simulation draws 10,000 values with the random seed 20261108 from triangular distributions with the low, mode and high values of Table A1. Activity drivers are linked by a Gaussian copula with a global cycle weight of 0.2 and an industry weight of 0.3, intensity and share draws are independent, and component and product weights vary around their mode in a Dirichlet distribution with concentration 40. All of these settings, λ, κ and both caps are team assumptions, because the backtest windows are short and the test period contains the pandemic.

### A2.2 Parameters and their sources

Table A1 lists every parameter of the tier 1 model with its range and evidence, and parameters without a cited source are team assumptions whose reasons are logged in research/model/outlook_results.md.

Table A1: Tier 1 model parameters, low / mode / high

| Industry | Parameter | Low / mode / high | Basis and source |
|---|---|---|---|
| Aerospace | Aftermarket growth a year | 3.0 / 3.7 / 4.2% | Sourced [AERO_AIRBUS_GSF2026_SERVICES_2045, AERO_BOEING_CMO2026_FLEET_CAGR, AERO_ICAO_RPK_CAGR] |
| Aerospace | Engine output ratio 2026 to 2025 | 1.16 / 1.18 / 1.19 | Sourced, LEAP high teens growth [CO_GE_Q2LEAP_2026, AERO_LEAP_2025] |
| Aerospace | Engine output growth 2026 to 2035 a year | 2.0 / 3.4 / 5.0% | Airbus fleet path, range team assumption [AERO_AIRBUS_GMF2026_FLEET_2025, AERO_AIRBUS_GMF2026_FLEET_2045] |
| Aerospace | Superalloy mass per engine, trend a year | −1.0 / 0.0 / 1.0% | Team assumption [AERO_AIRBUS_GMF2026_NEWGEN_2035] |
| Aerospace | Superalloy share of hot section, ratio | 0.90 / 0.98 / 1.03 | Team assumption, ceramic composites and TiAl |
| Aerospace | Weights new engines and aftermarket | 0.5 and 0.5 | Team assumption [CO_GE_CES_2025] |
| Energy | Gas turbine output ratio | 1.15 / 1.58 / 1.85 | Siemens Energy path 17 to 30 GW [CO_SIEMENSENERGY_CMD_2025, CO_SIEMENSENERGY_CAP_2026, IEA_WEI_GASPOWER_2025] |
| Energy | Nuclear fleet and tube ratio | 1.05 / 1.20 / 1.45 | Derived [EE_NUC_IAEA_2025, EE_NUC_WNA_2030, CO_WESTINGHOUSE_PIPE_2026] |
| Energy | Other equipment growth a year | 2.0 / 3.0 / 3.6% | Electricity demand proxy, team assumption |
| Energy | Alloy mass per GW, trend a year | −1.0 / 0.0 / 1.0% | Team assumption |
| Energy | Alloy share of hardware, ratio | 0.97 / 1.00 / 1.03 | Team assumption |
| Energy | Weights turbines, nuclear, other | 0.55, 0.25, 0.20 | Team assumption |
| Electronics | Realisation of SEMI path to 2031 | 0.85 / 1.00 / 1.05 | SEMI index 138 in 2031 [SEMI_300MM_PATH] |
| Electronics | Capacity growth 2031 to 2035 a year | 0.0 / 3.0 / 6.0% | Team assumption [SEMI_300MM_PATH] |
| Electronics | Components and masks growth a year | 0.0 / 2.5 / 6.0% | Team assumption [ZVEI_PROD_REAL, DNP_INVAR_2024] |
| Electronics | Alloy per unit, trend a year | −1.5 / 0.0 / 1.0% | Team assumption [NVDA_800VDC] |
| Electronics | Alloy share, ratio | 0.95 / 1.00 / 1.05 | Team assumption [DNP_INVAR_2024] |
| Electronics | Weights equipment and components | 0.6 and 0.4 | Team assumption [SEMI_300MM_2026] |
| Medical | Hip and knee procedures growth a year | 3.0 / 3.5 / 4.1% | Derived, 30 OECD countries 2013 to 2024 [MED_OECD_HK_COUNT_2023] |
| Medical | Other medical uses growth a year | 1.8 / 3.0 / 5.6% | MedTech Europe value growth [MED_MTE_EUR_2024, MED_MTE_EUR_2025] |
| Medical | Alloy per procedure, trend a year | −0.5 / 0.0 / 0.5% | Team assumption |
| Medical | CoCr and nickel share, ratio | 0.90 / 0.97 / 1.02 | Team assumption, oxidised zirconium and titanium |
| Medical | Weights implants and other | 0.8 and 0.2 | Team assumption [CO_STRYKER_ORTHO_2025] |
| Chemical | Activity growth a year | −1.0 / 1.0 / 2.5% | Team assumption [CEFIC_PROD_JANJUL_2026, CEFIC_CAPUTIL_EU27_Q3_2026, BASF_APAC_GROWTH_2035] |
| Chemical | Alloy per output, trend a year | −0.5 / 0.0 / 0.5% | Team assumption |
| Chemical | Alloy share, ratio | 0.97 / 1.00 / 1.03 | Team assumption |
| Oil and gas | Real upstream investment ratio | 0.80 / 1.00 / 1.12 | IEA scenarios [OG_WEI2026_UPSTREAM_OG_2026, OG_WEO2025_CPS_EXTRA_UPSTREAM] |
| Oil and gas | LNG trade ratio | 1.15 / 1.35 / 1.51 | IEA, 560 to 880 bcm [OG_WEO2025_LNG_DEMAND_2024, OG_LNG_TRACKER_202610_ADDITIONS] |
| Oil and gas | Alloy per unit, trend a year | −1.5 / −0.5 / 1.0% | Team assumption, clad pipe saves material |
| Oil and gas | Corrosion resistant alloy share, ratio | 0.97 / 1.00 / 1.03 | Team assumption |
| Oil and gas | Weights upstream and LNG | 0.7 and 0.3 | Team assumption [OG_WEI2026_GAS_SUPPLY_2026] |
| Automotive | New car sales ratio | 0.95 / 1.00 / 1.10 | Team assumption [IEA_WEO_CAR_SALES_2024, ACEA_CAR_REG_2025] |
| Automotive | Electric share of sales 2035 | 40 / 50 / 62% | IEA scenarios [IEA_WEO_EV_STEPS_2035, IEA_GEVO_EV_SHARE_2035] |
| Automotive | Heat resistant alloy per combustion car, trend a year | 0.0 / 1.0 / 2.0% | Team assumption [CO_GARRETT_GAS_PEN_2032] |
| Automotive | Nickel alloy share of turbo parts, ratio | 0.95 / 1.00 / 1.03 | Team assumption |
| Automotive | Precision alloy per electric car, trend a year | −1.0 / 0.0 / 2.0% | Team assumption |
| Automotive | FeNi share of motor and sensor parts, ratio | 0.90 / 1.00 / 1.10 | Team assumption |
| Automotive | Weights thermal and electric vehicle parts | 0.75 and 0.25 | Team assumption [CO_GARRETT_SALES_2025] |
| All | Nickel content of alloy class, ratio | 0.98 / 1.00 / 1.02 | Team assumption |
| All | Cobalt content, aerospace and other, ratio | 0.92 / 1.00 / 1.04 and 0.90 / 1.00 / 1.03 | Team assumption [CO_CMOC_QUOTA_2026] |
| Families | Superalloy bar, billet and remelt stock | Aerospace 0.575, energy 0.300, car thermal 0.050, oil and gas 0.040, chemical 0.035 | Aerospace weight measured [AERO_CI_AVIATION_CO_2025, AERO_CI_SUPERALLOY_CO_2025] |
| Families | Nickel alloy bar, rod and wire | Chemical 0.25, oil and gas 0.25, energy 0.20, aerospace 0.15, medical, car thermal, electronics 0.05 each | Team assumption [ALLEIMA_CHEM_2025] |
| Families | Plate, sheet, strip and foil | Chemical 0.30, energy 0.20, aerospace 0.20, oil and gas 0.15, car thermal 0.10, electronics 0.05 | Team assumption [AERO_ATI_JETENG_2025] |
| Families | Tubes and fittings | Oil and gas 0.35, chemical 0.25, energy 0.25, aerospace, car thermal, medical 0.05 each | Team assumption [ALLEIMA_CHEM_2025, EE_NUC_IAEA_2025] |
| Families | Precision FeNi strip and foil | Electronics 0.60, electric vehicle parts 0.30, medical 0.10 | Team assumption [DNP_INVAR_2024, IEA_GEVO_EV_SHARE_2035] |

*Sources: model/outlook_2035.py and research/model/outlook_results.md [MODEL_AERO_MRO_G, MODEL_EN_GT_R, MODEL_FAM_SUPERALLOYBARB]. The calibration in data/clean/model_calibration.csv reproduces the 20.0 kt of superalloy cobalt in 2025 exactly and leaves the IEA nickel and cobalt totals for 2035 with plausible remainders [IEA_CM_NI_OTHER_2025_2035, IEA_CM_CO_DEMAND_2025_2035].*

### A2.3 Backtest

The backtest fits a log linear trend to each series up to 2019 and compares its projection for 2020 to the latest year with the outcome, as Table A2 shows. Only real series correct the growth rate, while nominal OECD STAN output series only widen the ranges, because price inflation after 2021 would otherwise appear as volume.

Table A2: Backtest of tier 1 drivers, trend to 2019 against outcome

| Series | Industry | Basis | Test years | MAPE % | Bias % | Growth error, pp a year | Corrects growth |
|---|---|---|---|---|---|---|---|
| IEA upstream investment | Oil and gas | Real | 2020 to 2025 | 17.3 | −7.6 | −3.45 | Yes |
| IEA gas power investment | Energy | Real | 2020 to 2025 | 36.5 | −36.0 | −20.68 | Yes |
| IEA nuclear investment | Energy | Real | 2020 to 2025 | 50.3 | −50.3 | −16.42 | Yes |
| OECD hip and knee procedures | Medical | Counts | 2020 to 2024 | 9.7 | 9.2 | −0.53 | Yes |
| OECD STAN C30 output | Aerospace | Nominal | 2020 to 2023 | 14.9 | 14.9 | 0.31 | No |
| OECD STAN C26 output | Electronics | Nominal | 2020 to 2023 | 7.5 | −6.2 | −2.58 | No |
| OECD STAN C27 output | Electronics | Nominal | 2020 to 2023 | 12.8 | −11.0 | −5.65 | No |
| OECD STAN C20 output | Chemical | Nominal | 2020 to 2023 | 13.8 | −9.9 | −4.31 | No |
| OECD STAN C29 output | Automotive | Nominal | 2020 to 2023 | 14.8 | 14.8 | −1.07 | No |
| Eurostat C29 volume, EU27 | Automotive | Real | 2020 to 2025 | 23.0 | 23.0 | 3.22 | Yes |
| Eurostat C29 volume, DE, ES, FR, IT | Automotive | Real | 2020 to 2025 | 17.2 to 49.1 | 17.2 to 49.1 | 2.02 to 7.02 | No |
| IEA WEI 2025 against WEI 2026 | Oil and gas | Real | 2025 | 5.2 | 5.2 | n/a | No |

*Sources: team calculation [MODEL_BT_WEI_UPSTREAM, MODEL_BT_WEI_GASPWR, MODEL_BT_WEI_NUC, MODEL_BT_OECD_HK, MODEL_BT_STAN_C30, MODEL_BT_EUROSTAT_C29_EU27_2020] on IEA, OECD and Eurostat data [IEA_WEI_UPSTREAM_REGION_2026, IEA_WEI_GASPOWER_2025, MED_OECD_HK_COUNT_2023, OECD_STAN_P1, EUROSTAT_C29_EU27_2025]. Bias is the mean of projection minus outcome over outcome. The growth error is the trend slope minus the realised slope.*

The resulting corrections are a shift of plus 1.0 percentage point a year for energy and for oil and gas, plus 0.27 points for medical technology and minus 1.0 point for automotive, with no shift for aerospace, chemicals and electronics. Without the shift, the P50 indices would be 142 for energy, 104 for oil and gas, 137 for medical technology and 108 for automotive, against the earlier fixed rate workbook values of 148, 105, 128 and 86, which the model replaces [MODEL_T1_RESULTS_2035].

### A2.4 Further tier 2 candidates

Table 15 in chapter 7 shows eight options, and Table A3 adds the remaining register rows and the team research workbook candidates that the register has not yet assessed, none of which enters tier 1.

Table A3: Further tier 2 candidates

| Opportunity | Alloy and product form | TRL and evidence | Earliest volume | Signpost or status |
|---|---|---|---|---|
| Molten salt reactor vessels and piping | NiMoCr plate and tube | 3 to 5, speculative | 2035 or later | Construction permit and ASME code case |
| Superhot and enhanced geothermal casing | Nickel alloy tube and clad pipe | 4 to 6, speculative | 2032 to 2035 | Well above 400 °C with a published casing alloy |
| Liquid hydrogen aircraft tanks | Aluminium sheet, austenitic tube | 3 to 4, speculative | 2038 or later | Airframer programme launch |
| Concentrating solar receivers, Gen 3 | Nickel alloy plate, tube, forgings | Not assessed | Not assessed | Workbook candidate |
| Fuel cell bipolar plates, stationary PEM | Coated stainless thin strip | Not assessed | Not assessed | Workbook candidate |
| Robotic surgery components | NiTi wire and precision tube | Not assessed | Not assessed | Workbook candidate |
| Smaller cardiovascular delivery systems | CoNiCrMo fine wire and tube | Not assessed | Not assessed | Workbook candidate |
| Compact electronics cooling | CuCrZr and copper powder | Not assessed | Not assessed | Workbook candidate |

*Sources: team register and team research workbook, TRL and years are team estimates [MODEL_TIER2_REGISTER_2026, TEAM_WORKBOOK_2035].*

### A2.5 Scoring rules for the opportunity matrix

The matrix in Table 16 takes the perspective of a qualified producer that already melts and rolls high performance alloys and enters or expands a segment, and Table A4 states how each score from 1 to 5 is derived. Scores of 2 and 4 lie between the anchors shown, early signal rows score growth on their earliest volume year because the model does not quantify them, and the weighted score is the sum of each score times its weight.

Table A4: Scoring rules, weights and evidence

| Criterion, weight | Evidence used | Score 5 | Score 3 | Score 1 |
|---|---|---|---|---|
| Market attractiveness, 15% | Measured 2025 pool and unit value (chapters 5 and 6) | Largest measured pools, such as aviation cobalt or EU flat products of EUR 1.8 to 2.8 bn | Measured niche with premium unit value | No measured volume yet |
| Growth to 2035, 20% | P50 growth a year of the most specific index in Tables 13 and 14 or driver in Table A1, tier 2 by earliest volume | 4.0% a year or more (4 from 3.0%) | 2.0 to 2.9% a year (2 from 0%), or tier 2 volume by 2028 | Below 0%, or tier 2 volume after 2033 |
| Supply security, 15% | Concentration, quotas and licences of the main inputs (chapter 4, supply overlay) | Nickel, iron or chromium inputs without export restriction | Cobalt as a minor element under the Congo quota | An input under an active licence halt |
| Competitive intensity, 10% | Number of qualified suppliers and long term agreements (A6) | Demand above qualified capacity, no dominant incumbent | Several qualified suppliers competing on service | Price competition with new Asian capacity (2 for an oligopoly with agreements) |
| Technology attractiveness, 10% | Process route and how many producers master it | Triple melt, foil below 0.1 mm or similar rare routes | Standard grade on a qualified route | Commodity grade in decline |
| Customer attractiveness, 10% | Buyer backlog, concentration and pricing (chapter 5) | Named buyers with sold out capacity or growing backlog | Fragmented or cyclical buyers | Collapsing orders or state price cuts |
| Entry barriers, 10% | Time to approval and protection afterwards (A7) | Passable within about two years and protective thereafter (4 for three to five years) | Programme specific or moderate approvals | Captive supply chain closed to outsiders |
| Differentiation potential, 10% | Scope for grade, tolerance or service advantage | Customer specific grades or tolerances | Partly standardised products | Interchangeable products |

*Source: team scoring rules [MODEL_SCORING_2026]. Priority 1 from a weighted score of 3.75, priority 2 from 3.00, and early signal rows are at most gated options. Under equal weights the three priority 1 rows score 4.00, 4.00 and 3.75, and with entry barriers at 20 percent they score 4.14, 4.00 and 3.82.*

## A3 Data sources, product codes and reproducibility

All structured data were pulled with the project's fetch script, which stores raw files, writes clean tables and logs every query with its date and URL in the source register of more than 1,000 entries. UN Comtrade data cover the product codes HS 7502, 7504, 7505, 7506, 7507, 8105, 8109, 7219, 7220, 7223, 7409, 7606, 8311 and 8411 for ten reporting countries from 2019 to 2024, and Eurostat PRODCOM data cover fifteen nickel, cobalt, stainless, copper and aluminium product codes for the EU and five producer countries. USGS Mineral Commodity Summaries 2026, the World Bank Pink Sheet, OECD STAN and ICIO, UNIDO INDSTAT for Germany and the filings of 61 companies complete the evidence base.

The value range of Table 10 in chapter 6 is a team estimate that multiplies EU apparent consumption in tonnes by the lower and the higher of the extra EU export and import unit values of 2024, because the Eurostat production values fall below the value of the contained nickel. Flat products give 57.8 kt × EUR 31.0 per kg = EUR 1.79 bn and 57.8 kt × EUR 47.8 per kg = EUR 2.76 bn, and tubes give 9.2 kt × EUR 26.1 per kg = EUR 0.24 bn and 9.2 kt × EUR 41.1 per kg = EUR 0.38 bn, while bars are not valued because their production cell is confidential [EU_NI_MILL_APPCONS_2024, AC_EU_NI_UNITVAL_2024]. The unit values are trade value divided by trade quantity in PRODCOM DS-059358, so the range reflects the mix of grades traded across the EU border rather than a list price.

## A4 Limitations and further research

The study has three limitations that further research on this market should address. Official statistics stop at the mill product and mix pure nickel with nickel alloys, so the market for specific alloys can only be approximated, and a producer level survey or customs data at the eight digit level would sharpen these estimates. The tier 1 model rests on published activity drivers, but its intensity, share and product family weights are team assumptions, nickel alloy tonnes by industry are not published, and the backtest windows are short, so the model should be rerun when the IEA World Energy Outlook 2026, the next Airbus and Boeing outlooks and new SEMI forecasts appear. Finally, the trade analysis covers ten large reporting countries, so a world mirror data analysis that includes Russia, Sweden and Austria would complete the picture of global corridors.

## A5 Sector market indicators

The following tables collect the market indicators behind the industry analysis in chapter 5, with their sources and observation years.

Table A5: Automotive market indicators, 2025 and 2035

| Indicator | 2025 | 2035 | Source basis |
|---|---|---|---|
| World motor vehicle production | 96.4 million | No official forecast | OICA |
| Electric share of new car sales, world | 25% | About 50% | IEA, both exploratory scenarios |
| Electric share of car sales, China | Close to 55% | Above 90% | IEA |
| Electric share of car registrations, EU | 26.8% (BEV 17.4% plus PHEV 9.4%, team sum) | Above 90% of light duty sales | ACEA, IEA Stated Policies |
| Turbocharger production | Close to 50 million units | Back toward 2022 level by 2030 | Garrett citing S&P Global Mobility |

*Sources: OICA (2026), ACEA (2026), IEA Global EV Outlook 2026, Garrett Motion 10-K 2025 [OICA_VEH_PROD_2025, ACEA_BEV_2025, ACEA_EU_PHEV_2025, IEA_GEVO_EV_SHARE_2035, IEA_GEVO_CN_CARS_2035, IEA_GEVO_EU_LDV_STEPS_2035, CO_GARRETT_TURBOMKT_2025].*

Table A6: Oil and gas indicators, today and 2035

| Indicator | Today | 2035 | Source basis |
|---|---|---|---|
| Upstream oil and gas investment | USD 570 bn (2025), USD 546 bn (2026) | Near today's level (Stated Policies), about 10% higher (Current Policies) | IEA |
| Oil demand | 100 mb/d (2024) | Peak near 102 mb/d around 2030, back near 100 mb/d | IEA Stated Policies |
| LNG trade | 560 bcm (2024) | 880 bcm (Current Policies) | IEA |
| Upstream growth regions 2026 | Africa +12%, Central and South America +10% | Continued shift | IEA |

*Sources: IEA World Energy Outlook 2025 and World Energy Investment 2026 [OG_WEO2025_UPSTREAM_2025, OG_WEO2025_CPS_EXTRA_UPSTREAM, OG_WEO2025_OIL_DEMAND_2024, OG_WEO2025_LNG_DEMAND_2024, OG_WEI2026_SSA_UPSTREAM_2026].*

Table A7: Energy technology indicators relevant to high performance metals

| Indicator | Latest value | Direction to 2035 | Metal and product form |
|---|---|---|---|
| Siemens Energy gas turbine capacity | About 17 GW (FY2024), sold out to FY2028 | Above 30 GW a year from FY2028 | Superalloy bar, billet and forging stock |
| Reactors under construction | 81 reactors, 88.5 GWe gross, 40 in China | 710 GW installed in 2035 (IEA Net Zero) | Zirconium cladding tube, Alloy 690 tube |
| Installed electrolysis | More than 4 GW (2025) | Committed 2030 output 4.3 Mt of hydrogen | Nickel strip and mesh |
| Solid oxide fuel cells, Bloom Energy | 1 GW a year, doubling to 2 GW by end 2026 | Driven by data centre power | Interconnect material not disclosed |

*Sources: Siemens Energy capital markets day 2025, World Nuclear Association (2026), IEA World Energy Outlook 2025 and Global Hydrogen Review 2026, Bloom Energy results [CO_SIEMENSENERGY_CMD_2025, EE_NUC_WNA_UC, WEO_NZE_NUCLEAR_GW, EE_H2_ELEC_GW_2025, EE_H2_COMMIT_2030, CO_BLOOM_CAP_2026].*

Table A8: Aerospace market indicators, today and 2035

| Indicator | Today | 2035 | Source basis |
|---|---|---|---|
| Passenger fleet, aircraft of 100 seats or more | 23,310 (2025) | About 32,600 (team interpolation) | Airbus GMF 2026 |
| Commercial fleet, wider definition | About 28,000 (2025) | About 38,000 | Boeing CMO 2026 |
| New generation share of fleet | 39% (2025) | 82% | Airbus |
| Aviation services market | USD 209 bn (2026) | USD 422 bn in 2045, 3.8% a year | Airbus GSF 2026 |
| Cobalt used in aviation | 11,499 t (2025) | Grows with fleet and engine output | Cobalt Institute |
| World military expenditure | USD 2,887 bn (2025), Europe +14% | Rising in Europe | SIPRI |

*Sources: Airbus (2026), Boeing (2026), Cobalt Institute (2026), SIPRI (2026) [AERO_AIRBUS_GMF2026_FLEET_2025, AERO_BOEING_CMO2026_FLEET_2035, AERO_AIRBUS_GMF2026_NEWGEN_2035, AERO_AIRBUS_GSF2026_SERVICES_2045, AERO_CI_AVIATION_CO_2025, AERO_SIPRI_MILEX_2025]. The 2035 passenger fleet is a team estimate on a constant growth path and not an Airbus figure.*

Table A9: Chemical industry indicators

| Indicator | Value | Implication for alloy demand |
|---|---|---|
| EU27 chemical sales, 2024 | About EUR 635 bn | Large installed base needing maintenance |
| EU share of world chemical sales | 13% (2024), from 21% (2009) | New build moves out of Europe |
| EU chemical production index, 2025 | Down 3.2% | Fewer debottlenecking projects |
| EU capacity utilisation, Q3 2026 | 75.0% against 81.3% average | Closures, not expansions |
| German utilisation, 2025 | 72.5% | Weakest home market |
| Asia Pacific share of growth to 2035 | Over 80% (BASF) | Export projects through fabricators |

*Sources: Cefic (2025, 2026), Eurostat, VCI, BASF Report 2025 [CEFIC_EU27_SALES_2024, CEFIC_EU_SHARE_2024, EUROSTAT_C20_EU27_2025, CEFIC_CAPUTIL_EU27_Q3_2026, VCI_CAPUTIL_2025, BASF_APAC_GROWTH_2035].*

Table A10: Electronics indicators relevant to high performance metals

| Indicator | Value | Relevance |
|---|---|---|
| World semiconductor sales | USD 795.6 bn (2025), USD 1.51 tn (2026 forecast) | Activity, not metal volume |
| 300 mm fab equipment spending | USD 149 bn (2026), USD 227 bn (2029) | Gas delivery and chamber parts in high purity alloys |
| Copper busbar in a 1 MW rack at 54 VDC | Up to 200 kg | Copper and copper alloy strip and bar |
| German electrical and electronics value added | EUR 112.2 bn (2023), real output flat in 2025 | Home market for sensor and seal alloys |
| DNP metal mask capacity | Doubled by the 8th generation Kurosaki line | FeNi36 (invar) ultra thin foil |

*Sources: WSTS (2026), SEMI (2026), NVIDIA (2025), OECD STAN and ZVEI, Dai Nippon Printing [WSTS_WORLD_2025, SEMI_300MM_2026, NVDA_800VDC, STAN_DEU_C26C27_B1G_2023, ZVEI_PROD_REAL, DNP_KUROSAKI_2024].*

Table A11: Medical technology indicators

| Indicator | Value | Relevance |
|---|---|---|
| Hip replacements per 100,000 people, OECD average | 198 (2023) | Volume driver for CoCr and zirconium bar |
| Knee replacements per 100,000 people, OECD average | 156 (2023) | Volume driver for CoCr bar and powder |
| European medtech market | About EUR 173 bn (2025) | Devices and diagnostics, not metal |
| Stryker orthopaedics revenue | USD 9,469 m (2025) | Largest implant buyer |
| Zimmer Biomet knees and hips | USD 3,322 m and USD 2,094 m (2025) | Names cobalt chrome as a purchased commodity |
| China volume based procurement | Implant prices cut by about 82% (2022) | Volume without margin |

*Sources: OECD Health at a Glance 2025, MedTech Europe, company filings, National Healthcare Security Administration [MED_OECD_HIP_RATE_2023, MED_MTE_EUR_2025, CO_STRYKER_ORTHO_2025, CO_ZBH_PRODUCTS_2025, CO_ZBH_COMMODITY_2025, MED_NHSA_VBP_2022].*

## A6 Peer benchmark of specialty metal producers

The peer benchmark supports the competitive assessment in section 8.1 and shows the margins and current capacity moves of leading specialty metal producers.

Table A12: Peer benchmark of specialty metal producers

| Company | Revenue, latest year | Margin | Capacity move |
|---|---|---|---|
| Howmet Aerospace | USD 8,252 m (2025) | 24.8% operating | Engine products capacity, USD 453 m capex |
| Carpenter Technology | USD 3,124 m (FY2026) | 22.5% operating | Athens, Alabama expansion, capex USD 355 to 375 m guided |
| ATI | USD 4,587 m (2025) | 14.0% operating | Fifth VIM furnace in Monroe, about 9 kt a year from 2027 |
| PCC including Special Metals | USD 10.8 bn (2025) | Not published | Aerospace revenue up 7.5% |
| Aubert & Duval | EUR 844 m (2024) | Not published | Owned by Airbus, Safran and Tikehau |
| Alleima | SEK 18,630 m (2025) | 8.3% adjusted EBIT | Fourth VAR furnace at Sandviken |
| Outokumpu | EUR 5,468 m (2025) | 3.1% adjusted EBITDA | About 13 kt high nickel flat at Avesta, about EUR 150 m |
| Aperam | EUR 6,080 m (2025) | 5.6% adjusted EBITDA | New VIM complex at Imphy within EUR 160 m programme |
| Daido Steel | JPY 578 bn (FY2025) | 7.3% operating | JPY 36 bn high alloy melting and forging base |
| Nippon Yakin Kogyo | JPY 151 bn (FY2025) | 7.3% operating | Sales down 12% on weak high nickel demand |

*Sources: company filings and reports [CO_HWM_SALES_2025, CO_HWM_CAPEX_2025, CO_CRS_SALES_2026, CO_CRS_OPINC_2026, CO_CRS_CAPEX_2026, CO_ATI_SALES_2025, ARGUS_SUPERALLOY, CO_PCC_REV_2025, CO_AD_REV_PRESS_2025, CO_ALLEIMA_REV_2025, CO_ALLEIMA_ADJEBIT_2025, CO_OUTOKUMPU_SALES_2025, CO_OUTOKUMPU_HINI_CAP_2026, CO_APERAM_SALES_2025, CO_APERAM_INVEST_2026, CO_DAIDO_SALES_2026, CO_NIPPONYAKIN_SALES_2026]. Margins as reported or calculated from reported figures, fiscal years differ.*

## A7 Qualification gates by industry

The qualification gates below determine how quickly a producer can enter each application, and they underlie the entry barrier scores of Table 16 and the gates of Table 17.

Table A13: Qualification gates by industry

| Industry | Approval gate | Who approves | Implication |
|---|---|---|---|
| Aerospace | AMS specifications, NADCAP accredited processes, part level approval | Engine makers and forgers | Years per part family, start in 2026 |
| Energy | Casting house and turbine maker approvals, ASME III and RCC-M for nuclear | Turbine makers, utilities, tube makers | Nuclear approvals only with a named programme |
| Oil and gas | NORSOK M-650, API 6ACRA and API 5LD, operator approval lists | Operators, pipe and equipment makers | Approval lists are the moat |
| Chemical | Pressure equipment rules (VdTÜV, AD 2000, ASME), corrosion test data | Fabricators, plant operators | Life cycle cost evidence wins |
| Medical | ASTM F75 and F1537 material standards, supplier audits | Implant makers with ISO 13485 | Few buyers, long relationships |

*Source: team summary of the standards named in chapter 5.*

## A8 Risks and kill criteria

The roadmap in Table 17 carries known risks, and each of them can be met with a defined response and a point at which a producer should stop, as Table A14 shows.

Table A14: Main risks, responses and kill criteria

| Risk | Early signal | Response | Kill criterion |
|---|---|---|---|
| Qualification slower than planned | Part approvals behind schedule | Focus on repair and casting stock, which qualify faster | No long term agreement by end 2028, so no capacity step |
| Substitution by ceramic matrix composites and titanium aluminide | New engine variants with lower nickel content | Join customer development programmes early | Falling hot section nickel content in new programmes |
| New Asian superalloy capacity | Japanese and Chinese producers win Western approvals | Speed and service close to European customers | Prices below conversion cost in tenders |
| Cobalt, tungsten and molybdenum supply | Quota and licence changes | Several sources, revert recovery, stocks | Single source above half of an input |
| European demand weakness | Chemical utilisation below 75%, falling engine volumes | Shift sales to Asia and the United States | Contribution margin below plan for two years |

*Source: team assessment based on chapters 4 to 7 [CO_DAIDO_HIGHALLOY_2026, CEFIC_CAPUTIL_EU27_Q3_2026].*

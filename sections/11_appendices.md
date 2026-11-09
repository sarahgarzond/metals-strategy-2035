# Appendices: Data, Sources, Calculations, and Assumptions

## A1 Definitions and the stage ladder

Mt means million tonnes, kt means thousand tonnes, and t means metric tonnes. GW means gigawatts, and bcm means billion cubic meters. Prices are in current U.S. dollars or euros for the year stated.

The value chain has five separate stages: contained metal in mine output, refined metal or intermediates, alloy melt, mill products, and finished components. Examples of intermediates are nickel pig iron and cobalt hydroxide. Mill products include strip, sheet, plate, bar, and wire. The study reports each stage separately. It also separates contained metal from gross weight, actual output from capacity, and commodity benchmark prices such as the World Bank Pink Sheet from prices for qualified alloy products.

## A2 Outlook model, backtest and opportunity scoring

This appendix documents the formulas, parameters, tests and scoring rules behind chapters 7 and 8. Values are team estimates unless a source is listed. Running python3 model/outlook_2035.py from the repository root reproduces every result in chapters 7 and 8, writes data/clean/model_*.csv and research/model/outlook_results.md, and calls model/scoring.py for the opportunity scores [MODEL_T1_RESULTS_2035].

### A2.1 Formulas and simulation settings

The model divides each industry j into components k, for example new engines and the aftermarket in aerospace. The 2035 index is I(j) = 100 × Σ w(k) × A(k) × H(k) × (1 + i(k))^10 × S(k) × exp(10 × σ(j) × ε). A is the activity ratio from 2025 to 2035, H the optimism haircut on drivers taken from official guidance, i the annual trend in alloy mass per unit, S the ratio of the share using high performance alloy and w the component weight. σ carries the backtest error into the range, and ε is a standard normal draw.

No trend shift is added to the growth rate. The drivers are official guidance and scenarios, so adding a backtest trend error on top would count the same optimism twice. σ equals half the root mean square growth error of the backtest series, capped at 3 percentage points a year.

A product family index is the weighted sum of the industry indices, with the weights in Table A1. Cobalt tonnes are the 2025 base times the index and the cobalt content ratio. Paths between 2025 and 2035 grow at a constant compound rate for each component.

The simulation uses 10,000 draws and random seed 20261108, with triangular distributions on the low, mode and high values of Table A1. A Gaussian copula links the activity drivers with a global cycle weight of 0.2 and an industry weight of 0.3. Intensity and share are drawn independently. Component and family weights vary in a Dirichlet distribution with concentration 40, or 8 for the FeNi family because its weights rest on less evidence. These settings are team assumptions, because the backtest windows are short and include the pandemic.

### A2.2 Parameters and their sources

Table A1 lists each tier 1 parameter, its range and its evidence. A parameter without a cited source is a team assumption, and research/model/outlook_results.md gives the reason for each one.

Table A1: Tier 1 model parameters, low / mode / high

| Industry | Parameter | Low / mode / high | Basis and source |
|---|---|---|---|
| Aerospace | Aftermarket growth a year | 3.0 / 3.7 / 4.2% | Sourced [AERO_AIRBUS_GSF2026_SERVICES_2045, AERO_BOEING_CMO2026_FLEET_CAGR, AERO_ICAO_RPK_CAGR] |
| Aerospace | New engine output ratio 2035 to 2025, before haircut | 1.25 / 1.54 / 1.76 | Engine delivery path: average deliveries 2026 to 2045 of 2,103 and 2,181 aircraft against 1,393 in 2025 [AERO_AIRBUS_GMF2026_DELIVERIES, BOEING_CMO_2026, CO_AIRBUS_DELIV_2025, CO_BA_DELIV_2025] |
| Aerospace | New engine output 2026 and 2028 over 2025, evidence only | 1.11 / 1.18 / 1.20 and 1.25 / 1.39 / 1.44 | LEAP guidance of high teens growth and the 2028 plan of 2,500 to 2,600 engines [CO_GE_Q2LEAP_2026, CO_GE_9M26_DELIV, CO_SAFRAN_LEAP_2025] |
| Aerospace | Optimism haircut on 2035 activity | 0.80 / 0.98 / 1.07, median 0.96 | Mean of three plan against outcome points in Table A2 [MODEL_HAIRCUT_AERO] |
| Aerospace | Superalloy mass per engine, trend a year | −1.0 / 0.0 / 1.0% | Team assumption [AERO_AIRBUS_GMF2026_NEWGEN_2035] |
| Aerospace | Superalloy share of hot section, ratio | 0.90 / 0.98 / 1.03 | Team assumption, ceramic composites and TiAl |
| Aerospace | Weights new engines and aftermarket | 0.5 and 0.5 | Team assumption [CO_GE_CES_2025] |
| Energy | Gas turbine output ratio, three makers | 1.12 / 1.62 / 1.98 | GW weighted paths of Siemens Energy (19.0 GW in 2025, about 30 GW from FY2029), GE Vernova (15.3 GW, 24 GW planned for 2028 and 30 GW for 2030) and Mitsubishi Heavy Industries (about 4 GW) [CO_SIEMENSENERGY_CMD_2025, CO_GEV_GT_2025, CO_GEV_WEBCAST_Q2_2026, CO_GEV_GT_Q3_2026, CO_MHI_GT_2026, MODEL_EN_GT_R] |
| Energy | Gas turbine fleet aftermarket growth a year | 2.0 / 3.5 / 5.0% | Team assumption below the value growth of service backlogs [MODEL_EN_GT_AFT_G, CO_GEV_GT_Q3_2026] |
| Energy | Nuclear fleet and tube ratio | 1.05 / 1.20 / 1.45 | Derived [EE_NUC_IAEA_2025, EE_NUC_WNA_2030, CO_WESTINGHOUSE_PIPE_2026] |
| Energy | Other equipment growth a year | 2.0 / 3.0 / 3.6% | Electricity demand proxy [EE_ELEC_GROWTH_2024] |
| Energy | Alloy mass per GW, trend a year | −1.0 / 0.0 / 1.0% | Team assumption |
| Energy | Alloy share of hardware, ratio | 0.97 / 1.00 / 1.03 | Team assumption |
| Energy | Weights new turbines, turbine aftermarket, nuclear, other | 0.275, 0.275, 0.25, 0.20 | Team assumption [MODEL_EN_W] |
| Energy | Cobalt base 2025 | 6.0 kt | Family weight 0.300 on 20.0 kt of superalloy cobalt [MODEL_CO_ENERGY_BASE_2025] |
| Energy, oil and gas, automotive | Optimism haircut on 2035 activity | 0.85 / 0.95 / 1.02, median 0.94 | IEA investment vintage ratio 0.951, price bases differ [MODEL_HAIRCUT_OFFICIAL] |
| Electronics | Realisation of SEMI path to 2031 | 0.85 / 1.00 / 1.05 | SEMI index 138 in 2031 [SEMI_300MM_PATH] |
| Electronics | Capacity growth 2031 to 2035 a year | 0.0 / 3.0 / 6.0% | Team assumption [SEMI_300MM_PATH] |
| Electronics | Components and masks growth a year | 0.0 / 2.5 / 6.0% | Team assumption [DNP_INVAR_2024, ZVEI_PROD_REAL] |
| Electronics | Alloy per unit, trend a year | −1.5 / 0.0 / 1.0% | Team assumption [NVDA_800VDC] |
| Electronics | Alloy share, ratio | 0.95 / 1.00 / 1.05 | Team assumption [DNP_INVAR_2024] |
| Electronics | Weights equipment and components | 0.6 and 0.4 | Team assumption [SEMI_300MM_2026] |
| Medical | Hip and knee procedures growth a year | 3.0 / 3.5 / 4.1% | Derived, 30 OECD countries 2013 to 2024 [MED_OECD_HK_COUNT_2023] |
| Medical | Other medical uses growth a year | 1.8 / 3.0 / 5.6% | MedTech Europe value growth [MED_MTE_EUR_2024, MED_MTE_EUR_2025] |
| Medical | Alloy per procedure, trend a year | −0.5 / 0.0 / 0.5% | Team assumption |
| Medical | CoCr and nickel share, ratio | 0.90 / 0.97 / 1.02 | Team assumption, oxidised zirconium and titanium |
| Medical | Weights implants and other | 0.8 and 0.2 | Team assumption [CO_STRYKER_ORTHO_2025] |
| Chemical | Activity growth a year | −1.0 / 1.0 / 2.5% | Team assumption [BASF_APAC_GROWTH_2035, CEFIC_PROD_JANJUL_2026, CEFIC_CAPUTIL_EU27_Q3_2026] |
| Chemical | Alloy per output, trend a year | −0.5 / 0.0 / 0.5% | Team assumption |
| Chemical | Alloy share, ratio | 0.97 / 1.00 / 1.03 | Team assumption |
| Oil and gas | Real upstream investment ratio | 0.80 / 1.00 / 1.12 | IEA scenarios [OG_WEI2026_UPSTREAM_OG_2026, OG_WEO2025_CPS_EXTRA_UPSTREAM] |
| Oil and gas | LNG trade ratio | 1.15 / 1.35 / 1.51 | IEA, 560 to 880 bcm [OG_WEO2025_CPS_EXTRA_UPSTREAM, OG_LNG_TRACKER_202610_ADDITIONS] |
| Oil and gas | Alloy per unit, trend a year | −1.5 / −0.5 / 1.0% | Team assumption, clad pipe saves material |
| Oil and gas | Corrosion resistant alloy share, ratio | 0.97 / 1.00 / 1.03 | Team assumption |
| Oil and gas | Weights upstream and LNG | 0.7 and 0.3 | Team assumption [OG_WEI2026_GAS_SUPPLY_2026] |
| Automotive | New car sales ratio | 0.95 / 1.00 / 1.10 | Team assumption [ACEA_CAR_REG_2025, IEA_WEO_CAR_SALES_2024] |
| Automotive | Electric share of sales 2035 | 40 / 50 / 62% | IEA scenarios [IEA_GEVO_EV_SHARE_2035, IEA_GEVO_CN_CARS_2035] |
| Automotive | Heat resistant alloy per combustion car, trend a year | 0.0 / 1.0 / 2.0% | Team assumption [CO_GARRETT_GAS_PEN_2032] |
| Automotive | Nickel alloy share of turbo parts, ratio | 0.95 / 1.00 / 1.03 | Team assumption |
| Automotive | Precision alloy per electric car, trend a year | −1.0 / 0.0 / 2.0% | Team assumption |
| Automotive | Weights thermal and electric vehicle parts | 0.75 and 0.25 | Team assumption [CO_GARRETT_SALES_2025] |
| All | Nickel content of alloy class, ratio | 0.98 / 1.00 / 1.02 | Team assumption |
| All | Cobalt content, aerospace and other, ratio | 0.92 / 1.00 / 1.04 and 0.90 / 1.00 / 1.03 | Team assumption [CO_CMOC_QUOTA_2026] |
| Families | Superalloy bar, billet and remelt stock | Aerospace 0.575, energy 0.300, car thermal 0.050, oil and gas 0.040, chemical 0.035 | Aerospace weight measured [AERO_CI_AVIATION_CO_2025, AERO_CI_SUPERALLOY_CO_2025] |
| Families | Nickel alloy bar, rod and wire | Chemical 0.25, oil and gas 0.25, energy 0.20, aerospace 0.15, medical, car thermal, electronics 0.05 each | Team assumption [HAYNES_CPI_SHARE_FY2023, ALLEIMA_CHEM_2025] |
| Families | Plate, sheet, strip and foil | Chemical 0.30, energy 0.20, aerospace 0.20, oil and gas 0.15, car thermal 0.10, electronics 0.05 | Team assumption [AERO_ATI_JETENG_2025] |
| Families | Tubes and fittings | Oil and gas 0.35, chemical 0.25, energy 0.25, aerospace, car thermal, medical 0.05 each | Team assumption [ALLEIMA_CHEM_2025, EE_NUC_IAEA_2025] |
| Families | Precision FeNi strip and foil | OLED mask foil 0.40, EV sensors and shielding 0.25, lead frames and seals 0.35 | Team assumption, fab tools use no FeNi [DNP_INVAR_2024, CO_SDC_FMM_8G6_2025] |
| FeNi | OLED mask foil growth a year | −3.0 / 3.0 / 8.3% | DNP mask sales growth against mask free routes [MODEL_FENI_OLED_G, DNP_KUROSAKI_2024] |
| FeNi | Share of lines still using fine metal masks, ratio | 0.50 / 0.90 / 1.00 | Team assumption [CO_SDC_FMM_8G6_2025] |
| FeNi | FeNi share of EV sensor and shielding parts, ratio | 0.50 / 0.85 / 1.05 | Team assumption, competing FeCo, ferrite and nanocrystalline cores |
| Tonnes | Virgin cobalt content of superalloy melt | 4 / 8 / 15% | Team assumption [AERO_CI_SUPERALLOY_CO_2025] |
| Tonnes | Share of superalloy melt leaving as bar, billet or remelt stock | 75 / 85 / 95% | Team assumption [AERO_ATI_JETENG_2025] |
| Tonnes | EU27 share of world nickel mill product use | 12 / 20 / 30% | Team assumption [NI_WS_MELT_2025, NI_INSG_USE_2025] |
| Tonnes | World bar, rod and wire output over the HS 6 traded floor | 1.0 / 1.5 / 2.5 | Team assumption [COMTRADE_750512_750522_750712_2023_2024] |
| Value | Superalloy premium over the EU bar unit value | 1.00 / 1.22 / 1.41 | Sales per finished tonne of a listed alloy producer, EUR 35.8 per kg [MODEL_VALUE_SUPER_PREMIUM] |
| Shock | Severe aerospace case, share of the lost level recovered by 2035 | 0.0 / 0.7 / 1.0 | Team assumption, backlogs favour recovery [MODEL_SEVERE_AERO_RECOVERY] |

*Sources: model/outlook_2035.py and research/model/outlook_results.md [MODEL_T1_RESULTS_2035]. The calibration in data/clean/model_calibration.csv reproduces the 20.0 kt of superalloy cobalt in 2025 exactly and leaves the IEA nickel and cobalt totals for 2035 with plausible remainders [IEA_CM_CO_DEMAND_2025_2035].*

### A2.3 Backtest and plan against outcome tests

The backtest fits a log linear trend to each series through 2019 and compares it with outcomes from 2020 to the latest year. All series widen the ranges, while the four plan against outcome points in Table A2 set the optimism haircuts.

Table A2: Backtest of tier 1 drivers and plan against outcome tests

| Series | Industry | Basis | Test period | MAPE % | Bias % | Ratio or growth error | Used for |
|---|---|---|---|---|---|---|---|
| IEA upstream investment | Oil and gas | Real | 2020 to 2025 | 17.3 | −7.6 | −3.45 pp | Range |
| IEA gas power investment | Energy | Real | 2020 to 2025 | 36.5 | −36.0 | −20.68 pp | Range |
| IEA nuclear investment | Energy | Real | 2020 to 2025 | 50.3 | −50.3 | −16.42 pp | Range |
| OECD hip and knee procedures | Medical | Counts | 2020 to 2024 | 9.7 | 9.2 | −0.53 pp | Range |
| OECD STAN output C30, C26, C27, C20, C29 | Several | Nominal | 2020 to 2023 | 7.5 to 14.9 | −11.0 to 14.9 | −5.65 to 0.31 pp | Range |
| Eurostat C29 volume, EU27 | Automotive | Real | 2020 to 2025 | 23.0 | 23.0 | 3.22 pp | Range |
| Eurostat C29 volume, DE, ES, FR, IT | Automotive | Real | 2020 to 2025 | 17.2 to 49.1 | 17.2 to 49.1 | 2.02 to 7.02 pp | Range |
| Boeing 737 rate in Q4 2025 against the 2026 plan rate | Aerospace | Units | 2025 to 2026 | 10.6 | 11.9 | 0.894 | Haircut |
| Airbus 2026 run rate against the 870 guidance | Aerospace | Units | 2026, projected | 1.7 | 1.7 | 0.983 | Haircut |
| LEAP 2026 nine month growth against guidance | Aerospace | Units | 2026 | 6.8 | −6.3 | 1.068 | Haircut |
| IEA WEI 2025 estimate against WEI 2026 outcome | Energy, oil and gas, automotive | Mixed price bases | 2025 | 4.9 | 5.2 | 0.951 | Haircut |

*Sources: team calculation on IEA, OECD, Eurostat and company data [MODEL_BT_WEI_GASPWR, EUROSTAT_C29_EU27_2025, IEA_WEI_GASPOWER_2025, MED_OECD_HK_COUNT_2023, OECD_STAN_P1, CO_BA_RATES_2025, CO_BA_737RATE_2026, CO_AIRBUS_GUIDE_2026, CO_AIRBUS_9M_2026, CO_GE_Q2LEAP_2026, CO_GE_9M26_DELIV, OG_WEO2025_UPSTREAM_2025, IEA_WEI_UPSTREAM_REGION_2026]. Bias is the mean of projection minus outcome over outcome. The growth error is the trend slope minus the realised slope, in percentage points a year.*

The Boeing point compares the rate reached in Q4 2025 with the rate planned for 2026, so it measures the gap still to close. Boeing expects to be stable at 47 a month only in 2027, which confirms a delay of about one year [CO_BA_737RATE_2026]. The Airbus point projects the full year from nine months at the 2025 seasonality. The LEAP point is counter evidence, since engines beat their guidance while airframe rates slipped. A full year LEAP ratio of 1.000 to 1.014 instead of 1.068 would lower the mean of the three points to 0.959.

The IEA ratio compares an estimate on a 2024 price basis with an outcome on a 2025 price basis, so it mixes price and volume. It is excluded from the aerospace haircut and is kept only for energy, oil and gas, and automotive, with a deliberately wide range. Adding the backtest trend error as a growth shift on top of guidance would give P50 indices of 154 for energy, 115 for oil and gas, 140 for medical technology and 98 for automotive. That would double count the guidance, so the shift is not used [MODEL_T1_RESULTS_2035].

### A2.4 Product family tonnes, values and shock arithmetic

The family tonnes in Table 13 are team estimates at the mill product stage in gross weight, and they overlap, so they are never summed. Superalloy bar, billet and remelt stock divides the 20.0 kt of cobalt in superalloys by a virgin cobalt content of 4 to 15 percent and multiplies by the 75 to 95 percent that leaves the mill as bar, billet or remelt stock. This gives 193 kt at P50 in 2025, with a P10 to P90 range of 138 to 279 kt [MODEL_TON_SUPERALLOYBARBIL, AERO_CI_SUPERALLOY_CO_2025].

Two cross checks bound this figure. ATI's fifth VIM furnace at Monroe adds about 9 kt a year from 2027, 5 percent of the P50 [ARGUS_SUPERALLOY]. China's reported output of 64.5 kt in 2025, taken from a market report and used only for triangulation, equals 33 percent of the P50 [CO_BAOWU_CHINA_SUPERALLOY_2025]. A listed producer's high performance alloy melt of 83 kt, which includes corrosion resistant grades, equals 43 percent, so the range is most plausible in its upper half [MODEL_TON_SUPERALLOYBARBIL].

The other families start from measured trade or consumption. All traded floors use one basis, the 2024 exports of the ten reporters of chapter 6. Long products use the HS 750512 and 750522 alloy only exports of 95.1 kt, times 1.0 to 2.5 for output that never crosses a border. This gives 155 kt at P50 in 2025, with a P10 to P90 range of 121 to 200 kt. Flat products divide the EU27 apparent consumption of 57.8 kt by an EU share of world use of 12 to 30 percent, and tubes do the same with 9.2 kt. The HS 6 alloy only floors of 41.3 kt for flat products and 18.0 kt for tubes sit below both results. The eight reporter totals without France and India (80.3, 38.2 and 15.3 kt) are a memo only, because the four digit files of those two reporters are empty [MODEL_COMTRADE_HS6_2024, COMTRADE_750512_750522_750712_2023_2024, EU_NI_MILL_APPCONS_2024]. FeNi foil is not estimable, because no foil tonnes are published.

Values multiply the P50 tonnes by the 2024 extra EU unit values of EUR 25.4 to 33.4 per kg for bar, 31.0 to 47.8 for flat products and 26.1 to 41.1 for tubes. The superalloy family adds a premium of 1.00 to 1.41 over bar [AC_EU_NI_UNITVAL_2024, MODEL_VALUE_SUPER_PREMIUM]. The 2025 central ranges are EUR 4.9 to 9.1 bn for superalloys, 3.9 to 5.2 bn for long products, 8.7 to 13.5 bn for flat products and 1.2 to 1.8 bn for tubes. The 2035 values keep the 2024 unit values constant. At superalloy values, the 1.5 kt gate of Table 15 equals EUR 38 to 71 m of annual sales, or 0.8 percent of the 2025 family [MODEL_FAMILY_VALUE_2026].

The cost effects behind the shock cases of Table A5 are team arithmetic. At 8 percent virgin cobalt, a 25 percent rise in the cobalt price adds about USD 746 per tonne of superalloy and USD 5,595 per tonne of CoCr. A doubling of the 2025 tungsten concentrate price would add about USD 1,917 per tonne of Alloy C-276. Each USD 1,000 per tonne on LME nickel adds about USD 10 per tonne of alloy for every percentage point of nickel, which the monthly surcharge passes on [MODEL_SUPPLY_SHOCKS_2026, CO_USGS_CATHODE_2025, MO_HAYNES_C276_W, CO_ATI_SALES_2025]. The severe aerospace case cuts aerospace output by 20 percent in 2026 and 2027 and recovers 70 percent of the lost level. Its 2035 aerospace index is 114 (96 to 133), the superalloy family index falls from 129 to 116, and aviation cobalt falls from 15.4 to 13.0 kt [MODEL_SEVERE_AERO_2035, CO_BA_BACKLOG_2025].

### A2.5 Tier 2 register and further candidates

Table A3 lists the full tier 2 register and the research workbook candidates that are not yet assessed. Two powder positions sit in tier 1 instead: captive disc powder inside the superalloy family, and open market AM powder, scored in Table A5 [CO_RTX_POWDER_2025, WOHLERS_2025].

Table A3: Tier 2 register and further candidates

| Opportunity | Alloy and product form | TRL and evidence | Earliest volume | Signpost for tier 1 |
|---|---|---|---|---|
| Electrolysers | Nickel strip, wire and mesh | 8 to 9, early signal | 2026 to 2028 | Orders and investment decisions recover |
| Solid oxide cells | Coated ferritic strip | 9 for fuel cells, early signal | 2026 to 2028 | Purchased strip contract with a cell maker |
| New additive hot section parts | Superalloy powder | 6 to 8, early signal | 2027 to 2030 | Part specification with a volume call |
| 800 VDC racks | Copper busbar and strip, less copper | 6 to 7, early signal | 2027 | Eaton, Schneider and Vertiv busbar launches |
| Small reactors | Zirconium cladding, Alloy 690 tube | 7 to 8, early signal | 2030 to 2033 | Serial tube order after a licence |
| Hydrogen turbines | Castings, forgings, combustor sheet | 5 to 7, speculative | 2030 to 2035 | Order with a hydrogen supply contract |
| Fusion magnets | Alloy C-276 tape foil | 4 to 6, speculative | 2030 to 2035 | Magnet order for a pilot plant |
| sCO2 recuperators | Nickel alloy plate and strip | 5 to 6, speculative | 2032 to 2035 | Pilot above 10 MW |
| Molten salt reactors | NiMoCr plate and tube | 3 to 5, speculative | 2035 or later | Construction permit and ASME code case |
| Superhot geothermal casing | Nickel alloy tube and clad pipe | 4 to 6, speculative | 2032 to 2035 | Well above 400 °C with a published casing alloy |
| Liquid hydrogen aircraft tanks | Aluminium sheet, austenitic tube | 3 to 4, speculative | 2038 or later | Airframer programme launch |
| Concentrating solar receivers | Nickel alloy plate, tube, forgings | Not assessed | Not assessed | Workbook candidate |
| Stationary PEM fuel cell plates | Coated stainless thin strip | Not assessed | Not assessed | Workbook candidate |
| Robotic surgery and cardiovascular devices | NiTi and CoNiCrMo fine wire and tube | Not assessed | Not assessed | Workbook candidates |
| Compact electronics cooling | CuCrZr and copper powder | Not assessed | Not assessed | Workbook candidate |

*Sources: team register and research workbook, TRL and years are team estimates [MODEL_TIER2_REGISTER_2026, TEAM_WORKBOOK_2035, NVDA_800VDC_ROWCUT, CO_TKNUCERA_SOEC_2026, EE_NUC_WNA_UC].*

### A2.6 Scoring rules for the opportunity matrix

Table 14 scores opportunities for a producer that already melts and rolls high performance alloys. Market, growth and supply security are computed from data by model/scoring.py. The other five criteria are team judgement on the anchors of Table A4. The weighted score is the sum of each score times its weight. Rows without measured volume (E) are capped at Option, priority 1 starts at 3.75, priority 2 at 3.00 and Monitor at 2.75 [MODEL_SCORING_2026].

Market uses the pool specific to the end use. Rows without a cobalt pool use the family tonnes times an end use weight and EU unit values, capped at 4 because the weight is unmeasured. Engine bar thus uses 193 kt times the aerospace weight of 0.575, about EUR 4.0 bn, an upper bound for wrought bar because cast parts share the weight. Growth uses the most specific driver, so row growth differs from the industry index of Table 12. Engine bar uses the engine delivery path (3.7 percent a year against 3.1 for the aerospace index). Casting stock and combustor sheet use an equal blend of three maker turbine output and the fleet aftermarket (3.4 against 2.7 for the energy index). Fab gas strip uses the SEMI path (4.2) and repair wire the aftermarket (3.1) [MODEL_GROWTH_LABELS_2026].

Supply security takes the weakest input of the lead grades. A single source rule applies where one country mines at least 90 percent of world output with no control in force. Such an element scores 3 below 10 percent of the alloy and 2 above it. Alloy 718, with 4.75 to 5.50 percent niobium from Brazil (93 percent of world output) and at most 1 percent cobalt, scores 3. Cobalt bearing wrought grades such as Waspaloy (12 to 15 percent cobalt) and UDIMET alloy R41 (10 to 12 percent) score 2 under the Congo quota [MO_SM_IN718_COMP, NB_USGS_BRAZIL_2025, MO_WASPALOY_CO, MO_SM_R41_CO]. Combustor sheet scores 2 with alloy 188, a cobalt base grade, and Nimonic 263 (19 to 21 percent), and 3 with HX (0.5 to 2.5 percent) and Alloy 230 (5 percent at most) [MO_SM_UD188_CO, MO_SM_NIM263_CO, MO_SM_HX_CO, MO_SM_230_CO]. Cobalt lean casting stock assumes IN738 and GTD 111 at about 8.5 to 9.5 percent cobalt, which keeps it at 3 (TODO(data): no datasheet for IN738, GTD 111 or IN939 is in the repository, so this row stays provisional).

The combined vacuum melt programme treats engine bar and turbine casting stock as one melt shop, with shares of 0.657 and 0.343. It uses the combined pool of EUR 6.1 bn, the share weighted growth, the weakest supply input and the share weighted judgement scores. With cobalt grades it scores 3.67 to 3.74 and stays priority 2 under all four weightings, while the 718 only variant scores 3.82 to 3.87 and is priority 1 under all four [MODEL_COMBINED_PROGRAMME_2026]. The judgement values of the fab gas, NO96 and repair wire rows are first pass team judgement.

Table A4: Scoring rules, weights and evidence

| Criterion, weight | Evidence used | Score 5 | Score 3 | Score 1 |
|---|---|---|---|---|
| Market attractiveness, 15% | Measured or estimated 2025 pool specific to the end use (chapters 5 and 6, A2.4) | At least 10 kt of contained cobalt in the end use (4 from 5 kt, or from EUR 0.75 bn) | 2 to 5 kt of cobalt, EUR 0.30 to 0.75 bn, or a measured company niche (2 below these, or a mixed segment) | No measured or estimable volume |
| Growth to 2035, 20% | P50 growth a year of the most specific driver, tier 2 by earliest volume | 4.0% a year or more (4 from 3.0%) | 2.0 to 2.9% a year (2 from 0%), or tier 2 volume by 2028 | Below 0%, or tier 2 volume after 2033 |
| Supply security, 15% | Weakest input of the lead grades (chapter 4, Table A5) | Nickel, iron or chromium without export restriction (4 for a quota on ore or a form melters do not buy) | Cobalt below 10% under the Congo quota, or a single source element below 10% | Active licence halt (2 for a licence regime or quota element above 10%) |
| Competitive intensity, 10% | Qualified suppliers and long term agreements (A6) | Demand above qualified capacity, no dominant incumbent | Several qualified suppliers competing on service | Price competition with new Asian capacity (2 for an oligopoly with agreements) |
| Technology attractiveness, 10% | Process route and how many producers master it | Triple melt, foil below 0.1 mm or similar rare routes | Standard grade on a qualified route | Commodity grade in decline |
| Customer attractiveness, 10% | Buyer backlog, concentration and pricing (chapter 5) | Named buyers with sold out capacity or growing backlog | Fragmented or cyclical buyers | Collapsing orders or state price cuts |
| Entry barriers, 10% | Time to approval and protection afterwards (A7) | Passable within about two years and protective thereafter (4 for three to five years) | Programme specific or moderate approvals | Captive supply chain closed to outsiders |
| Differentiation potential, 10% | Scope for grade, tolerance or service advantage | Customer specific grades or tolerances | Partly standardised products | Interchangeable products |

*Source: team scoring rules [MODEL_SCORING_2026].*

Table A5 lists every scored row with its weighting sensitivities and every change of tier in the four shock cases of chapter 7. The equal weight and 20 percent entry barrier columns test whether a tier depends on the base weights.

Table A5: All scored rows, weighting sensitivities and shock cases

| Opportunity | Ev | Mkt, Gro, Sup | Comp, Tech, Cust, Barr, Diff | Score | Tier | Equal weights | Barriers 20% | Tier change in a shock |
|---|---|---|---|---|---|---|---|---|
| Engine bar and billet, Alloy 718 | M | 4, 4, 3 | 2, 5, 5, 4, 4 | 3.85 | 1 | 3.88 | 3.87 | Severe aerospace: 3.45, 2 |
| Casting stock, cobalt lean grades | M | 4, 4, 3 | 2, 4, 4, 5, 4 | 3.75 | 1 | 3.75 | 3.89 | Congo quota: 3.60, 2 |
| Combustor sheet, HX and Alloy 230 | M | 3, 4, 3 | 2, 4, 5, 5, 4 | 3.70 | 2 | 3.75 | 3.84 | None |
| Engine bar and billet, all grades | M | 4, 4, 2 | 2, 5, 5, 4, 4 | 3.70 | 2 | 3.75 | 3.73 | None |
| Casting stock, all grades | M | 4, 4, 2 | 2, 4, 4, 5, 4 | 3.60 | 2 | 3.62 | 3.76 | None |
| Fab gas strip and tube | M | 2, 5, 4 | 3, 4, 4, 3, 3 | 3.60 | 2 | 3.50 | 3.53 | None |
| Combustor sheet, all grades | M | 3, 4, 2 | 2, 4, 5, 5, 4 | 3.55 | 2 | 3.62 | 3.71 | None |
| CoCr implant bar and powder | M | 3, 4, 2 | 3, 4, 4, 5, 3 | 3.45 | 2 | 3.50 | 3.62 | None |
| FeNi36 foil and FeNi strip | E | 1, 3, 5 | 2, 5, 3, 3, 4 | 3.20 | Option | 3.25 | 3.18 | None |
| FeNi36 strip for NO96 LNG tanks | E | 1, 3, 5 | 3, 4, 3, 3, 4 | 3.20 | Option | 3.25 | 3.18 | None |
| Alloy 690 bar and hollows | M | 2, 2, 5 | 3, 4, 4, 3, 3 | 3.15 | 2 | 3.25 | 3.13 | None |
| Solid oxide cell strip | E | 1, 3, 5 | 3, 4, 2, 3, 4 | 3.10 | Option | 3.12 | 3.09 | Indonesian quota: 2.95, Monitor |
| AM powder, CoCr and superalloy | M | 2, 4, 2 | 2, 4, 4, 3, 3 | 3.00 | 2 | 3.00 | 3.00 | Congo quota: 2.85, Monitor; Severe aerospace: 2.60, Harvest |
| Sour service bar, strip, wire | M | 3, 1, 4 | 3, 3, 3, 5, 3 | 2.95 | Monitor | 3.12 | 3.18 | None |
| Alloy C-276 fusion tape foil | E | 1, 2, 2 | 4, 5, 2, 3, 5 | 2.75 | Monitor | 3.00 | 2.78 | None |
| Superalloy repair wire | E | 1, 4, 3 | 2, 3, 3, 3, 2 | 2.70 | Monitor | 2.62 | 2.73 | None |
| Chemical plate, welding wire | M | 3, 2, 2 | 2, 3, 3, 3, 3 | 2.55 | Harvest | 2.62 | 2.60 | None |
| Car exhaust and turbo alloys | M | 2, 1, 5 | 3, 1, 2, 3, 2 | 2.35 | Harvest | 2.38 | 2.42 | None |
| Memo: vacuum melt programme, cobalt grades | M | 4, 4, 2 | Share weighted | 3.67 | 2 | 3.71 | 3.74 | None |
| Memo: vacuum melt programme, 718 only | M | 4, 4, 3 | Share weighted | 3.82 | 1 | 3.83 | 3.87 | Congo quota: 3.67, 2; Severe aerospace: 3.62, 2 |

*Source: team calculation [MODEL_SCORING_2026, MODEL_COMBINED_PROGRAMME_2026, MODEL_SUPPLY_SHOCKS_2026]. The 20 percent barrier column rescales the other weights proportionally, and an equal cut of the others gives the same tiers. The Congo case tightens the quota to the CMOC entitlement ratio (mine gap 54 percent), the Indonesian case cuts the ore quota by 22 to 71 percent, and the severe aerospace case runs two years at minus 20 percent with 70 percent recovery. The Chinese tungsten licence halt changes no tier. Without the aerospace haircut, the 718 row scores 4.05 and the cobalt grade programme 3.87, both priority 1 [MODEL_AERO_HAIRCUT_CASES_2026].*

### A2.7 Investment case and timing of a 718 remelt step

The investment case in 8.2 is a team estimate for a remelt step (VAR or ESR) with billet conversion and inspection. It excludes the VIM stage, qualification cost and working capital [MODEL_INVESTMENT_CASE_2026]. Only one disclosed pair of capex and tonnes exists in the research, the Outokumpu Avesta high nickel programme of about EUR 150 m for about 13 kt. Its first phase, ESR remelting for EUR 30 m, gives the floor of EUR 2,308 per annual tonne. The whole programme gives the central value of EUR 11,538, and the high value of EUR 17,308 adds a small scale premium of 1.5 times, a team assumption [CO_OUTOKUMPU_AVESTA_NI_2026, CO_OUTOKUMPU_HINI_CAP_2026].

Other moves bound the step but give no usable value per tonne. Aperam's VIM complex at Imphy sits inside a EUR 160 m programme for four sites, and Carpenter guides group capex of USD 355 to 375 m for its Athens expansion [CO_APERAM_INVEST_2026, CO_CRS_CAPEX_2026]. Alleima's fourth VAR furnace at Sandviken ran about four months from installation to operation, with no capex disclosed. ATI's fifth VIM furnace at Monroe adds about 9 kt a year from the second half of 2027, so a 1.5 kt step equals 17 percent of one such furnace [CO_ALLEIMA_VAR_2025, ARGUS_SUPERALLOY].

The capex range gives a cheque of EUR 3.5, 17.3 or 26.0 m for 1.5 kt a year and EUR 6.9, 34.6 or 51.9 m for 3 kt. Sales at 1.5 kt use the superalloy unit values of EUR 25.4, 35.9 and 47.1 per kg, which gives EUR 38.1, 53.8 and 70.7 m a year at full use. The group operating margins of ATI (14.0 percent) and Howmet (24.8 percent), with 19.4 percent in between, give EUR 5.3, 10.4 and 17.5 m of operating profit. Simple payback before tax is 0.2 to 4.9 years, with 1.7 years in the central case. A three year ramp at 33, 67 and 100 percent of sales gives 0.6 to 5.9 years, counted from the first approved tonne [AC_EU_NI_UNITVAL_2024, MODEL_VALUE_SUPER_PREMIUM, CO_ATI_OPINC_2025, CO_HWM_OPINC_2025]. These are group margins, not the margin of a remelt step, so the range is deliberately wide.

The timing follows the disclosed build times. A decision in Q1 2028 plus 1.5 to 2.5 years of build and 0.5 to 2.0 years of qualification gives a first approved tonne in Q1 2030 (fast), mid 2031 (central) or mid 2032 (slow). The fast case qualifies non rotating Alloy 718 bar to AMS 5662 and 5663 while the furnace is commissioned. The central case allows 12 to 24 months for the approval of a new furnace, and the slow case reflects rotating grades, where ATI quotes forging lead times above two years [MO_SM_IN718_COMP, CO_ATI_LEAD_2026]. The announced additions of other melters are on stream by the end of 2029, so only the fast case lands inside the window, and revenue from added capacity starts about 2031. The gate of 1.5 kt signed or in qualification by Q4 2027, with at least 0.5 kt of non rotating bar signed, keeps a qualification delay from ending the programme on timing alone.

## A3 Data sources, product codes and reproducibility

The team collected structured data with the project's fetch script. The script saves raw files, creates clean tables, and records each query's date and URL in a source register with more than 1,000 entries.

The UN Comtrade data cover HS 7502, 7504, 7505, 7506, 7507, 8105, 8109, 7219, 7220, 7223, 7409, 7606, 8311, and 8411 for ten reporting countries from 2019 to 2024. The HS 6 digit alloy codes 750512, 750522, 750620 and 750712 separate nickel alloys from pure nickel for 2023 and 2024 and set the traded floors in A2.4 [MODEL_COMTRADE_HS6_2024]. Eurostat PRODCOM covers fifteen nickel, cobalt, stainless, copper, and aluminium product codes for the EU and five producer countries. Other sources include USGS Mineral Commodity Summaries 2026, the World Bank Pink Sheet, OECD STAN and ICIO, UNIDO INDSTAT for Germany, and filings from 61 companies.

Table 10 in chapter 6 estimates market values by multiplying EU apparent consumption by the lower and higher of the 2024 unit values for exports and imports outside the EU. The team used these figures because Eurostat production values fall below the value of the nickel contained in the products.

For flat products, 57.8 kt × EUR 31.0 per kg gives EUR 1.79 bn, and 57.8 kt × EUR 47.8 per kg gives EUR 2.76 bn. For tubes, 9.2 kt × EUR 26.1 per kg gives EUR 0.24 bn, and 9.2 kt × EUR 41.1 per kg gives EUR 0.38 bn. The team did not value bars because the production figure is confidential [AC_EU_NI_UNITVAL_2024, EU_NI_MILL_APPCONS_2024].

The team calculated unit values by dividing trade value by trade quantity in PRODCOM DS-059358. The resulting range reflects the mix of grades traded across the EU border. It does not represent a quoted list price.

## A4 Limitations and further research

The study has three main limitations. First, official data stop at the mill product stage. HS 6 digit trade data separate nickel alloys from pure nickel, but PRODCOM production data do not, and no source gives tonnes by alloy grade. A survey of producers or Comext data at the eight digit level could sharpen the estimates.

Second, tier 1 uses published activity drivers, but its alloy intensity, use shares, and product family weights are team assumptions. Nickel alloy tonnes by industry are not published, and the backtest periods are short. The aerospace haircut rests on three points of one vintage. The gas turbine driver combines Siemens Energy, GE Vernova and Mitsubishi Heavy Industries, but the makers publish no output beyond 2030, so the path to 2035 is a team estimate. The investment case rests on one disclosed pair of capex and tonnes. The team should rerun the model when the IEA World Energy Outlook 2026, the next Airbus and Boeing outlooks, and new SEMI forecasts become available.

Third, the trade analysis covers ten large reporting countries. A global analysis of mirror data that includes Russia, Sweden, and Austria would give a fuller picture of trade routes.

## A5 Sector market indicators

The following tables list the market indicators used in chapter 5. Each table identifies the sources and years of observation.

Table A6: Automotive market indicators, 2025 and 2035

| Indicator | 2025 | 2035 | Source basis |
|---|---|---|---|
| World motor vehicle production | 96.4 million | No official forecast | OICA |
| Electric share of new car sales, world | 25% | About 50% | IEA, both exploratory scenarios |
| Electric share of car sales, China | Close to 55% | Above 90% | IEA |
| Electric share of car registrations, EU | 26.8% (BEV 17.4% plus PHEV 9.4%, team sum) | Above 90% of light duty sales | ACEA, IEA Stated Policies |
| Turbocharger production | Close to 50 million units | Back toward 2022 level by 2030 | Garrett citing S&P Global Mobility |

*Sources: [ACEA_CAR_REG_2025, ACEA_BEV_2025, CO_GARRETT_GAS_PEN_2032, IEA_GEVO_CN_CARS_2035, OICA_CHINA_PROD_2025].*

Table A7: Oil and gas indicators, today and 2035

| Indicator | Today | 2035 | Source basis |
|---|---|---|---|
| Upstream oil and gas investment | USD 542 bn (2025), USD 546 bn (2026), 2025 prices | Near today's level (Stated Policies), about 10% higher (Current Policies) | IEA |
| Oil demand | 100 mb/d (2024) | Peak near 102 mb/d around 2030, back near 100 mb/d | IEA Stated Policies |
| LNG trade | 560 bcm (2024) | 880 bcm (Current Policies) | IEA |
| Upstream growth regions 2026 | Africa +13.7%, Central and South America +9.9% | Continued shift | IEA |

*Sources: [IEA_WEI_UPSTREAM_REGION_2026, OG_WEO2025_CPS_EXTRA_UPSTREAM]. Regional growth is a team calculation from the WEI 2026 regional data.*

Table A8: Energy technology indicators relevant to high performance metals

| Indicator | Latest value | Direction to 2035 | Metal and product form |
|---|---|---|---|
| Siemens Energy gas turbine capacity | About 17 GW (FY2024), sold out to FY2028 | Above 30 GW a year from FY2028 | Superalloy bar, billet and forging stock |
| GE Vernova gas turbines | 15.3 GW delivered (2025), 36.7 GW ordered in nine months of 2026 | 24 GW planned for 2028, 30 GW for 2030 | Casting stock, combustor sheet |
| Reactors under construction | 81 reactors, 88.5 GWe gross, 40 in China | 710 GW installed in 2035 (IEA Net Zero) | Zirconium cladding tube, Alloy 690 tube |
| Installed electrolysis | More than 4 GW (2025) | Committed 2030 output 4.3 Mt of hydrogen | Nickel strip and mesh |
| Solid oxide fuel cells, Bloom Energy | 1 GW a year, doubling to 2 GW by end 2026 | Driven by data centre power | Interconnect material not disclosed |

*Sources: [CO_BLOOM_CAP_2026, OG_WEO2025_CPS_EXTRA_UPSTREAM, EE_H2_COMMIT_2030, CO_SIEMENSENERGY_CMD_2025, CO_GEV_GT_2025, CO_GEV_GT_Q3_2026, CO_GEV_WEBCAST_Q2_2026, EE_NUC_WNA_UC].*

Table A9: Aerospace market indicators, today and 2035

| Indicator | Today | 2035 | Source basis |
|---|---|---|---|
| Passenger fleet, aircraft of 100 seats or more | 23,310 (2025) | About 32,600 (team interpolation) | Airbus GMF 2026 |
| Commercial fleet, wider definition | About 28,000 (2025) | About 38,000 | Boeing CMO 2026 |
| New generation share of fleet | 39% (2025) | 82% | Airbus |
| Aviation services market | USD 209 bn (2026) | USD 422 bn in 2045, 3.8% a year | Airbus GSF 2026 |
| Cobalt used in aviation | 11,499 t (2025) | Grows with fleet and engine output | Cobalt Institute |
| World military expenditure | USD 2,887 bn (2025), Europe +14% | Rising in Europe | SIPRI |

*Sources: [CO_AIRBUS_DELIV_2025, AERO_AIRBUS_GMF2026_DELIVERIES, AERO_AIRBUS_GSF2026_SERVICES_2026, AERO_AIRBUS_GSF2026_SERVICES_2045, AERO_BOEING_CMO2026_FLEET_2035, AERO_CI_AVIATION_CO_2025, AERO_SIPRI_MILEX_2025]. The 2035 passenger fleet is a team estimate on a constant growth path and not an Airbus figure.*

Table A10: Chemical industry indicators

| Indicator | Value | Implication for alloy demand |
|---|---|---|
| EU27 chemical sales, 2024 | About EUR 635 bn | Large installed base needing maintenance |
| EU share of world chemical sales | 13% (2024), from 21% (2009) | New build moves out of Europe |
| EU chemical production index, 2025 | Down 3.2% | Fewer debottlenecking projects |
| EU capacity utilisation, Q3 2026 | 75.0% against 81.3% average | Closures, not expansions |
| German utilisation, 2025 | 72.5% | Weakest home market |
| Asia Pacific share of growth to 2035 | Over 80% (BASF) | Export projects through fabricators |

*Sources: [BASF_APAC_GROWTH_2035, CEFIC_EU_SHARE_2024, CEFIC_CN_SHARE_2024, CEFIC_CAPUTIL_EU27_Q3_2026, EUROSTAT_C20_EU27_2025, VCI_CAPUTIL_2025].*

Table A11: Electronics indicators relevant to high performance metals

| Indicator | Value | Relevance |
|---|---|---|
| World semiconductor sales | USD 795.6 bn (2025), USD 1.51 tn (2026 forecast) | Activity, not metal volume |
| 300 mm fab equipment spending | USD 149 bn (2026), USD 227 bn (2029) | Gas delivery and chamber parts in high purity alloys |
| Copper busbar in a 1 MW rack at 54 VDC | Up to 200 kg | Copper and copper alloy strip and bar |
| German electrical and electronics value added | EUR 112.2 bn (2023), real output flat in 2025 | Home market for sensor and seal alloys |
| DNP metal mask capacity | Doubled by the 8th generation Kurosaki line | FeNi36 (invar) ultra thin foil |

*Sources: [DNP_KUROSAKI_2024, NVDA_800VDC, OECD_STAN_P1, SEMI_300MM_2026, WSTS_WORLD_2025, ZVEI_PROD_REAL].*

Table A12: Medical technology indicators

| Indicator | Value | Relevance |
|---|---|---|
| Hip replacements per 100,000 people, OECD average | 198 (2023) | Volume driver for CoCr and zirconium bar |
| Knee replacements per 100,000 people, OECD average | 156 (2023) | Volume driver for CoCr bar and powder |
| European medtech market | About EUR 173 bn (2025) | Devices and diagnostics, not metal |
| Stryker orthopaedics revenue | USD 9,469 m (2025) | Largest implant buyer |
| Zimmer Biomet knees and hips | USD 3,322 m and USD 2,094 m (2025) | Names cobalt chrome as a purchased commodity |
| China volume based procurement | Implant prices cut by about 82% (2022) | Volume without margin |

*Sources: [MED_MTE_EUR_2025, MED_NHSA_VBP_2022, MED_OECD_HIP_RATE_2023, CO_STRYKER_ORTHO_2025, CO_ZBH_COMMODITY_2025].*

## A6 Peer benchmark of specialty metal producers

The peer comparison supports the competition scores in section 8.1. It shows the margins of leading specialty metal producers and how they are changing capacity. Howmet and PCC also cast and forge, so they are customers as well as peers.

Table A13: Peer benchmark of specialty metal producers

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
| Daido Steel | JPY 578 bn (FY to March 2026) | 7.3% operating | High alloy melting and forging base |

*Sources: company filings and reports [ALLEIMA_CHEM_2025, CO_APERAM_INVEST_2026, ARGUS_SUPERALLOY, CO_AD_REV_PRESS_2025, AERO_ATI_JETENG_2025, CO_PCC_REV_2025, CO_CRS_CAPEX_2026, CO_DAIDO_SALES_2026, CO_HWM_CAPEX_2025, CO_OUTOKUMPU_SALES_2025, CO_OUTOKUMPU_AVESTA_NI_2026]. Margins as reported or calculated from reported figures, fiscal years differ. The Daido margin divides operating profit of JPY 42.1 bn by revenue of JPY 578.1 bn from its fact book.*

## A7 Qualification gates by industry

The qualification requirements below affect how quickly a producer can enter each application. They support the entry barrier scores in Table 14 and the gates in Table 18.

Table A14: Qualification gates by industry

| Industry | Approval gate | Who approves | Implication |
|---|---|---|---|
| Aerospace | AMS 5662 and 5663 for 718 bar and forgings, AMS 5596 for 718 sheet, NADCAP accredited processes, part level approval | Engine makers and forgers | Non rotating bar first, rotating parts take years |
| Energy | Casting house and turbine maker approvals. For nuclear tube, ASME SB 163 and RCC-M M4105 product approvals plus a nuclear quality assurance programme | Turbine makers, utilities, tube makers | Nuclear approvals only with a named programme |
| Oil and gas | NORSOK M-650, API 6ACRA and API 5LD, operator approval lists | Operators, pipe and equipment makers | Approval lists are the moat |
| Chemical | Pressure equipment rules (VdTÜV, AD 2000, ASME), corrosion test data | Fabricators, plant operators | Life cycle cost evidence wins |
| Medical | ASTM F75 and F1537 material standards and their ISO equivalents, supplier audits | Implant makers with ISO 13485 | Few buyers, long relationships |

*Sources: team summary of the standards named in chapter 5 [MO_SM_IN718_COMP, ALLEIMA_SGT_RCCM, MED_ASTM_F75_2023, MED_ASTM_F1537_2020].*

## A8 Risks and kill criteria

The roadmap in Table 15 depends on the risks below. Table A15 rates each risk for likelihood and impact and gives an early signal, a response and a numeric kill criterion with a date. The kill criteria match those of Table 15.

Table A15: Main risks, likelihood, impact and kill criteria

| Risk | Likelihood | Impact | Early signal and response | Kill criterion |
|---|---|---|---|---|
| Qualification slower than planned (initiative 1) | High, rotating approvals take several years | High, first tonne after 2031 | No non rotating approval by Q4 2027. Lead with AMS 5662 and 5663 bar | Under 0.5 kt of non rotating bar signed by Q4 2028 |
| Severe aerospace downturn (initiative 1) | Low, Airbus alone has a backlog of 8,754 aircraft | High, 718 bar falls to 3.45 and priority 2 | Airbus and Boeing deliveries 20 percent below the 1,393 of 2025. Shift volume to turbine casting stock | Deliveries below 1,114 aircraft in both 2026 and 2027 |
| Substitution by ceramic composites and titanium aluminide (initiatives 1 and 2) | Medium, both already fly, no displacement published | Medium, the share ratio has a low case of 0.90 | Composite turbine blades in a new engine. Join customer programmes | A programme launched by Q4 2028 that cuts superalloy hot section mass by more than 10 percent |
| New Asian superalloy capacity (initiatives 1 and 2) | Medium, China already melts about a third of the P50 | Medium, price pressure on second sources | Chinese or Japanese melters win Western approvals. Compete on speed and service | Asian bids below the EU unit value floor of EUR 25.4 per kg in two tenders by Q4 2029 |
| Cobalt quota and grade risk (initiative 2) | Medium, the Congo quota is in force | Medium, casting stock falls to 3.60 at the CMOC ratio | Quota at the CMOC entitlement ratio. Use refiners outside the hydroxide chain and revert | Lead grades above 10 percent cobalt, or no casting order by Q4 2029 |
| Fab gas qualification fails (initiative 3) | Medium, alloy volumes are unmeasured | Low, pool of EUR 0.11 bn | No gas system maker trial by Q4 2027 | No order by Q4 2028 |
| CoCr price cuts (initiative 4) | Medium, Chinese procurement cut implant prices by about 82 percent | Medium, volume without margin | Price clauses in tenders. Keep ASTM F75 and F1537 | No supply agreement by Q4 2029 |
| No Western reactor order (initiative 5) | Medium, 40 of 81 reactors are in China | Low, pool of EUR 0.08 bn | No AP1000 or AP300 tube order. Hold approvals only | No reactor tube order by Q4 2030 |
| Input concentration (initiative 6) | Medium, Brazil mines 93 percent of niobium | High for all lead grades | One supplier above 40 percent of an input | One source above 50 percent of cobalt or niobium in Q4 2028 |
| European demand weakness (all) | High, EU chemical utilisation is 75.0 percent | Medium, harvest rows lose volume | Utilisation below 75 percent. Shift sales to Asia and the United States | Contribution margin below plan in both 2028 and 2029 |

*Source: team assessment based on chapters 4 to 7 [MODEL_INVESTMENT_CASE_2026, MODEL_SUPPLY_SHOCKS_2026, MODEL_SCORING_2026, CO_AIRBUS_DELIV_2025, CO_BAOWU_CHINA_SUPERALLOY_2025, AC_EU_NI_UNITVAL_2024, MED_NHSA_VBP_2022, EE_NUC_WNA_UC, NB_USGS_BRAZIL_2025, CEFIC_CAPUTIL_EU27_Q3_2026]. Likelihood and impact are team judgement. The delivery threshold of 1,114 aircraft is 80 percent of the 2025 deliveries.*

# 7. Growth Scenarios to 2035

## 7.1 Growth Model and Scenario Assumptions

The final link asks how large alloy demand could become by 2035, answered by a tier 1 model for established applications and a tier 2 register for emerging ones, both team estimates [MODEL_T1_RESULTS_2035]. Tier 1 writes demand as D = A × I × S, the activity driver times alloy mass per unit times the high performance alloy share, indexed to 2025 = 100 and calibrated to the 11,499 t of superalloy cobalt used in aviation in 2025 [AERO_CI_AVIATION_CO_2025]. The drivers in Table 12 are official guidance and scenarios rather than fitted trends, so no trend shift is applied.

Table 12: Tier 1 activity drivers to 2035 and optimism haircut (mode)

| Industry | Activity driver (second driver in brackets) | Low | High | Haircut mode |
|---|---|---|---|---|
| Aerospace | Engine output a year (aftermarket 3.0 to 4.2%) | 2.0% | 5.0% | 0.92 |
| Energy | Gas turbine output ratio (nuclear 1.05 to 1.45) | 1.00 | 2.00 | 0.95 |
| Electronics | 300 mm capacity a year after index 138 in 2031 | 0% | 6% | None |
| Medical | Hip and knee procedures a year | 3.0% | 4.1% | None |
| Chemical | Chemical activity a year | −1.0% | 2.5% | None |
| Oil and gas | Upstream investment ratio (LNG 1.15 to 1.51) | 0.80 | 1.12 | 0.95 |
| Automotive | Electric share of car sales in 2035 | 40% | 62% | 0.95 |

*Sources: team assumptions, all parameters and ranges in Table A1 [MODEL_HAIRCUT_AERO, MODEL_HAIRCUT_OFFICIAL].*

Guided drivers carry an optimism haircut from three plan against outcome tests, as the IEA expected 2025 upstream investment of just under USD 570 bn but recorded USD 542 bn (0.951) and Boeing built 42 instead of 47 aircraft a month on the 737 (0.894), while LEAP deliveries beat guidance by 26 against 18 percent (1.068), which sets the upper end [OG_WEO2025_UPSTREAM_2025, IEA_WEI_UPSTREAM_REGION_2026, CO_BA_RATES_2025, CO_BA_737RATE_2026, CO_GE_9M26_DELIV]. A trend backtest to 2019 erred both ways, missing gas power investment by minus 36.0 percent and EU vehicle output by plus 23.0 percent, so it only widens the ranges of a Monte Carlo simulation with 10,000 draws and seed 20261108 [MODEL_BT_WEI_GASPWR, MODEL_BT_EUROSTAT_C29_EU27_2020].

## 7.2 Results by Industry, Product, and Region

Electronics and medical technology lead, with aerospace and energy close behind after the haircut costs them 13 and 8 index points, while automotive stays near 102 as combustion parts fall to 69 and electric vehicle parts rise to 199 [MODEL_T1_RESULTS_2035].

Table 13: Tier 1 alloy demand index 2035 by industry (2025 = 100)

| Industry | P10 | P50 | P90 | P50 growth a year | P50 without haircut |
|---|---|---|---|---|---|
| Electronics | 112 | 141 | 177 | 3.50% | 141 |
| Medical | 128 | 136 | 145 | 3.16% | 136 |
| Aerospace | 121 | 134 | 147 | 2.98% | 147 |
| Energy | 105 | 133 | 167 | 2.90% | 141 |
| Chemical | 87 | 109 | 135 | 0.83% | 109 |
| Automotive | 84 | 102 | 124 | 0.17% | 108 |
| Oil and gas | 79 | 98 | 122 | −0.19% | 104 |

*Source: team calculation [MODEL_T1_RESULTS_2035].*

In product families, superalloy bar, billet and remelt stock and precision FeNi share the highest P50 of 129, but only the superalloy weights rest on a measured aviation share of 0.575, and the indicative tonnes of Table 14 follow the methods of appendix A2.4 [MODEL_FAM_RESULTS_2035]. FeNi, rebuilt on OLED mask foil, EV sensor parts and lead frames, fell from 157 to 129, or 118 for electronics alone, and its volume is not estimable without published foil tonnes [MODEL_FENI_FAMILY_2035].

Figure 3: Electronics and medical technology lead alloy demand to 2035, aerospace and energy follow closely

![Figure 3](fig/fig3_scenarios.svg)

*Source: team calculation, band P10 to P90, line P50, haircut applied, no trend shift [MODEL_T1_RESULTS_2035].*

Table 14: Product families, index 2035 and indicative tonnes (team estimates, never summed)

| Product family | Index P10 | P50 | P90 | 2025 kt, P50 (P10 to P90) | 2035 kt, P50 (P10 to P90) |
|---|---|---|---|---|---|
| Superalloy bar, billet, remelt stock | 116 | 129 | 142 | 193 (138 to 279) | 247 (175 to 363) |
| Nickel alloy bar, rod and wire | 105 | 117 | 130 | 135 (105 to 174) | 158 (120 to 206) |
| Plate, sheet, strip and foil | 104 | 116 | 128 | 282 (224 to 364) | 327 (253 to 428) |
| Tubes and fittings | 100 | 112 | 127 | 45 (36 to 58) | 50 (39 to 67) |
| Precision FeNi strip and foil | 101 | 129 | 163 | Not estimable | Not estimable |

*Source: team calculation [MODEL_TON_SUPERALLOYBARBIL, MODEL_TON_FLATPRODUCTSPLAT]. Flat products cover all nickel grades, an upper bound.*

Table 15 shows that supply shocks raise cost more than they cap volume, since superalloys need only 26.3 kt of cobalt in 2035, 12 percent of base mine supply and 18 percent in the tight Congo case, and only the cobalt and severe aerospace cases change a priority [MODEL_SUPPLY_OVERLAY_2035, CO_USGS_QUOTA_2026].

Table 15: Supply shocks and severe aerospace case (team arithmetic)

| Shock | Exposure in 2035 | Cost per tonne of alloy | Score change | Tier change |
|---|---|---|---|---|
| Congo cobalt quota held at 2026 level | Mine gap 36% (base 30%) | Superalloy +USD 746, CoCr +USD 5,595 | Engine bar 3.80 to 3.65 | Engine bar 1 to 2 |
| Chinese tungsten licence halt | 10 kt of C-276 use 2.2% of ex China W | C-276 +USD 646 | Chemical plate 2.55 to 2.40 | None |
| Indonesian ore quota −22 to −29% | Nickel mine gap 21 to 27% (base 6.5%) | Passed through by surcharge | Solid oxide strip 3.10 to 2.95 | Option to Monitor |
| Aerospace −20% in 2026 and 2027 | Aerospace P50 134 to 113 | Idle VIM and VAR capacity | Engine bar 3.80 to 3.60 | Engine bar 1 to 2 |

*Sources: team calculation [MODEL_SUPPLY_SHOCKS_2026, MODEL_SEVERE_AERO_2035], arithmetic in appendix A2.4.*

Regionally, the drivers place engines and turbines in North America and Europe and reactors and chemicals in Asia. In 2026 North America took USD 50.9 bn of USD 114 bn of gas power investment and Asia Pacific USD 41.0 bn of USD 82.8 bn of nuclear investment, while China builds 40 of 81 reactors and Asia should take over 80 percent of chemical growth [IEA_WEI_REGION_2026, EE_NUC_WNA_UC, BASF_APAC_GROWTH_2035]. Table 16 lists the nearest tier 2 options, which enter tier 1 only once their signpost occurs, and Table A3 holds the later ones.

Table 16: Tier 2 register, nearest options (not included in tier 1)

| Option | Alloy and form | TRL | From | Signpost |
|---|---|---|---|---|
| Electrolysers | Nickel strip and mesh | 8 to 9 | 2026 | Nucera orders above EUR 356 m a year |
| Solid oxide cells | Ferritic strip | 9 | 2026 | Strip contract at Bloom Energy |
| New AM hot section parts | Superalloy powder | 6 to 8 | 2027 | Engine specification with volume |
| Small reactors | Alloy 690 tube | 7 to 8 | 2030 | Serial tube order after a licence |

*Sources: team register, TRL and years are team estimates [MODEL_TIER2_REGISTER_2026, CO_BLOOM_CAP_2026].*

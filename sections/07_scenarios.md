# 7. Growth Scenarios to 2035

This chapter turns the market sizes of chapters 5 and 6 into demand paths to 2035.

## 7.1 Growth Model and Scenario Assumptions

Tier 1 models demand as D = A × I × S, with activity A, alloy mass per unit I and the share S of units using a high performance alloy. Each factor is a 2035 to 2025 ratio, so the index is 100 × (1 + g)^10 with g the growth rate a year. P10, P50 and P90 come from 10,000 draws, calibrated to 20.0 kt of superalloy cobalt in 2025, with all parameters in Table A1 [AERO_CI_SUPERALLOY_CO_2025].

Energy follows gas turbine output (ratio 1.00 to 2.00, Siemens Energy alone) and nuclear (1.05 to 1.45). Electronics follows SEMI fab capacity, not alloy tonnes. Medical follows hip and knee procedures at 3.0 to 4.1 percent a year. Chemical activity moves −1.0 to 2.5 percent a year. Oil and gas follows upstream investment (0.80 to 1.12) and LNG (1.15 to 1.51). Automotive follows an electric share of 40 to 62 percent in 2035 [CO_SIEMENSENERGY_CMD_2025, SEMI_300MM_PATH, MED_OECD_HIP_RATE_2023, CEFIC_CAPUTIL_EU27_Q3_2026, OG_WEO2025_CPS_EXTRA_UPSTREAM, IEA_GEVO_CN_CARS_2035].

Aerospace combines the aftermarket at 3.0 to 4.2 percent a year with new engine deliveries. The outlooks expect 2,103 to 2,181 deliveries a year to 2045 against 1,393 in 2025, a ratio of 1.25 to 1.76 by 2035. The 2025 base already holds the LEAP ramp to 1,802 engines, so P50 growth of 3.7 percent a year is not pessimism [AERO_AIRBUS_GMF2026_DELIVERIES, BOEING_CMO_2026, CO_GE_LEAP_2025, MODEL_ENGINE_PATH_2026].

The model haircuts guidance, which tends to run ahead of outcomes. For aerospace, its mode is the mean (0.982) of three points, with a median draw of 0.96. Boeing reached a 737 rate of 42 a month in Q4 2025 against a 2026 plan of 47 (0.894). Airbus runs at about 856 of 870 guided deliveries (0.983), and LEAP beat its guidance (1.068) [MODEL_HAIRCUT_AERO, CO_BA_RATES_2025, CO_AIRBUS_9M_2026, CO_GE_9M26_DELIV]. The IEA upstream ratio of 0.951 mixes price bases and is excluded for aerospace, but it sets the other haircuts (median 0.94). The backtest in A2.3 widens the ranges [IEA_WEI_UPSTREAM_REGION_2026].

## 7.2 Results by Industry, Product, and Region

Measured in tonnes, superalloy bar, billet and remelt stock adds the most volume. It grows from about 193 kt in 2025 to 248 kt in 2035, worth EUR 6.3 to 11.7 bn at 2024 unit values [MODEL_FAMILY_VALUE_2026].

Table 13: Alloy demand 2035 by industry, index 2025 = 100

| Industry | Cobalt base 2025, 2035 | P10 | P50 | P90 | P50 a year | P50 without haircut |
|---|---|---|---|---|---|---|
| Aerospace | 11.5, 15.4 kt Co | 121 | 136 | 151 | 3.1% | 143 |
| Energy | 8.5, 11.0 kt Co | 104 | 132 | 167 | 2.8% | 140 |
| Electronics | None | 112 | 141 | 177 | 3.5% | 141 |
| Medical | None | 128 | 136 | 145 | 3.2% | 136 |
| Chemical | None | 88 | 108 | 134 | 0.8% | 108 |
| Automotive | None | 84 | 102 | 125 | 0.2% | 108 |
| Oil and gas | None | 78 | 98 | 122 | −0.2% | 105 |

*Source: team calculation [MODEL_T1_RESULTS_2035].*

Figure 3: Electronics has the highest alloy demand index to 2035, and automotive stays flat (index, not volume)

*Source: team calculation, band P10 to P90, line P50 [MODEL_T1_RESULTS_2035].*

Electronics has the highest index, but it tracks fab capacity, and its alloy volume is unmeasured. Automotive stays flat because combustion parts fall to 69 while electric vehicle parts rise to 200 [MODEL_T1_RESULTS_2035].

Table 14: Product families 2035, team estimates, never summed

| Product family | 2025 kt | 2035 kt (P10 to P90) | 2035 EUR bn | Index P50 |
|---|---|---|---|---|
| Superalloy bar, billet, remelt stock | 193 | 248 (176 to 366) | 6.3 to 11.7 | 129 |
| Plate, sheet, strip and foil | 282 | 326 (255 to 429) | 10.1 to 15.6 | 116 |
| Nickel alloy bar, rod and wire | 131 | 153 (116 to 200) | 3.9 to 5.1 | 116 |
| Tubes and fittings | 45 | 50 (39 to 66) | 1.3 to 2.1 | 112 |
| Precision FeNi strip and foil | None | None | None | 129 |

*Sources: team calculation, P50, methods in A2.4 [MODEL_FAM_RESULTS_2035, AC_EU_NI_UNITVAL_2024].*

Supply limits raise costs more than they cap volume. Cobalt mine supply falls 30 percent short of 2035 demand, or 36 percent if the Congo quota holds, but superalloys need only 12 percent of it [MODEL_SUPPLY_OVERLAY_2035]. Table 15 lists every tier change, and the Chinese tungsten licence halt changes none.

Table 15: Shock cases and every change of priority tier

| Shock | Exposure | Tier changes |
|---|---|---|
| Congo cobalt quota at CMOC entitlement ratio | Mine gap 54% | Turbine remelt stock 1 to 2 (3.70), AM powder 2 to Monitor |
| Indonesian ore quota cut by 22 to 71% | Mine gap 21 to 55% | Solid oxide strip Option to Monitor |
| Severe aerospace, two years at −20% | Aerospace index 114 | Alloy 718 bar 1 to 2 (3.45), AM powder 2 to Harvest |

*Sources: team calculation, base scores in Table 17 [MODEL_SUPPLY_SHOCKS_2026].*

By region, engine and turbine growth sits in the United States and Western Europe. China builds 40 of the 81 reactors under construction, and Asia takes over 80 percent of chemical growth [BASF_APAC_GROWTH_2035, EE_NUC_WNA_UC]. Emerging uses stay in the tier 2 register of Table A3 until their signposts are met [MODEL_TIER2_REGISTER_2026].

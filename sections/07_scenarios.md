# 7. Growth Scenarios to 2035

This chapter turns the market sizes of chapters 5 and 6 into demand paths to 2035. Engine and turbine alloys add the most tonnes, electronics has the fastest index, and supply shocks raise costs more than they cap volume.

## 7.1 Growth Model and Scenario Assumptions

Tier 1 models demand as D = A × I × S, with activity A, alloy mass per unit I and the share S of units using a high performance alloy. Each factor is a 2035 to 2025 ratio, so the index is 100 × (1 + g)^10 with g the growth rate a year. The low, central and high cases are P10, P50 and P90 of 10,000 draws, calibrated to 20.0 kt of superalloy cobalt in 2025, with all parameters in Table A1 [AERO_CI_SUPERALLOY_CO_2025].

Each rate follows one published driver. Energy follows the turbine output of Siemens Energy, GE Vernova and Mitsubishi Heavy Industries (ratio 1.12 to 1.98), a fleet aftermarket of 2.0 to 5.0 percent a year and nuclear (1.05 to 1.45). Its cobalt base is 6.0 kt, a weight of 0.300 on 20.0 kt [CO_SIEMENSENERGY_CMD_2025, CO_GEV_GT_Q3_2026, CO_MHI_GT_2026, MODEL_EN_GT_AFT_G, MODEL_CO_ENERGY_BASE_2025]. Electronics follows SEMI fab capacity, medical follows procedures at 3.0 to 4.1 percent a year, and chemicals move −1.0 to 2.5 percent. Oil and gas follows upstream investment and LNG, and automotive an electric share of 40 to 62 percent [SEMI_300MM_PATH, MED_OECD_HIP_RATE_2023, CEFIC_CAPUTIL_EU27_Q3_2026, OG_WEO2025_CPS_EXTRA_UPSTREAM, IEA_GEVO_CN_CARS_2035].

Aerospace combines the aftermarket at 3.0 to 4.2 percent a year with new engine deliveries [AERO_AIRBUS_GSF2026_SERVICES_2045, AERO_BOEING_CMO2026_FLEET_CAGR]. The outlooks expect 2,103 to 2,181 deliveries a year to 2045 against 1,393 in 2025, a ratio of 1.25 to 1.76 by 2035. The 2025 base already holds the LEAP ramp to 1,802 engines [AERO_AIRBUS_GMF2026_DELIVERIES, BOEING_CMO_2026, CO_GE_LEAP_2025, MODEL_ENGINE_PATH_2026].

The model haircuts guidance, which tends to run ahead of outcomes. The aerospace median of 0.96 rests on Boeing (0.894), Airbus (0.983) and LEAP (1.068), and other guided drivers take 0.94 [MODEL_HAIRCUT_AERO, MODEL_HAIRCUT_OFFICIAL]. Without it, aerospace would reach 143 and energy 139, and A2.3 gives the backtest.

## 7.2 Results by Industry, Product, and Region

Measured in tonnes, superalloy bar, billet and remelt stock adds the most volume, from about 193 kt in 2025 to 248 kt in 2035 (Table 13). Table 12 separates the industry index, which blends all components, from the row driver that Table 14 scores.

Table 12: Alloy demand 2035 by industry, index 2025 = 100, and growth of the scored driver

| Industry | Cobalt 2025, 2035 | P10 | P50 | P90 | Index a year | Row driver, P50 a year |
|---|---|---|---|---|---|---|
| Electronics | None | 112 | 141 | 177 | 3.5% | 300 mm fab capacity, 4.2% |
| Aerospace | 11.5, 15.4 kt Co | 121 | 136 | 151 | 3.1% | Engine deliveries, 3.7% |
| Medical | None | 128 | 136 | 145 | 3.2% | Hip and knee procedures |
| Energy | 6.0, 7.7 kt Co | 105 | 131 | 162 | 2.7% | Turbines and aftermarket, 3.4% |
| Chemical | None | 87 | 109 | 135 | 0.8% | Chemical output |
| Automotive | None | 84 | 102 | 124 | 0.2% | Combustion parts, −3.7% |
| Oil and gas | None | 79 | 98 | 122 | −0.2% | Upstream and LNG |

*Sources: team calculation [MODEL_T1_RESULTS_2035, MODEL_GROWTH_LABELS_2026].*

Figure 3: Electronics leads by index, but aerospace and energy carry the measured cobalt tonnes

![Figure 3](fig/fig3_scenarios.svg)

*Source: team calculation, band P10 to P90, line P50 [MODEL_T1_RESULTS_2035].*

The aerospace index grows 3.1 percent a year and engine deliveries 3.7 percent, because the aftermarket half grows 3.1 percent. The energy index grows 2.7 percent and the turbine blend 3.4 percent, because nuclear adds only 1.5 percent. Automotive stays flat because combustion parts fall to 69 while electric vehicle parts rise to 199 [MODEL_GROWTH_LABELS_2026, MODEL_T1_RESULTS_2035].

Table 13: Product families 2035, team estimates, never summed

| Product family | 2025 kt | 2035 kt (P10 to P90) | 2035 EUR bn | Index P50 |
|---|---|---|---|---|
| Superalloy bar, billet, remelt stock | 193 | 248 (175 to 365) | 6.3 to 11.7 | 129 |
| Plate, sheet, strip and foil | 282 | 325 (253 to 428) | 10.1 to 15.5 | 115 |
| Nickel alloy bar, rod and wire | 155 | 180 (139 to 236) | 4.6 to 6.0 | 116 |
| Tubes and fittings | 45 | 50 (39 to 67) | 1.3 to 2.1 | 112 |
| Precision FeNi strip and foil | None | None | None | 129 |

*Sources: team calculation, methods in A2.4 [MODEL_FAM_RESULTS_2035, AC_EU_NI_UNITVAL_2024].*

By region, the team estimate holds 2025 shares constant [MODEL_REGIONAL_2026]. Of the energy index of 131, Asia Pacific holds 43 points, North America 26 and Europe 22, or 2.6, 1.6 and 1.3 kt of cobalt. North America holds 32 of 98 oil and gas points, and Asia Pacific 63 of 102 automotive points and 6.9 of 8.7 chemical growth points. Aerospace and electronics lack a regional driver (TODO(data): regional engine and fab data searched).

Supply limits raise costs more than they cap volume. Cobalt mine supply falls 30 percent short of 2035 demand, or 54 percent under a tight Congo quota, but superalloys need only 11 percent of it. Of the shocks in Table A5, the tight quota moves cobalt lean casting stock to priority 2 (3.60), a severe aerospace case moves Alloy 718 bar to priority 2 (3.45), and the tungsten licence halt changes no tier [MODEL_SUPPLY_OVERLAY_2035, MODEL_SUPPLY_SHOCKS_2026]. Emerging uses stay in Table A3.

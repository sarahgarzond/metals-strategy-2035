# Model changelog

## 2026-11-08 run: two tier 2035 outlook added (model/outlook_2035.py)

What changed
- New script model/outlook_2035.py (seed 20261108, runs in about 2 seconds) builds the outlook described in chapter 3 of the report. Tier 1 multiplies activity, intensity and alloy share for seven industries and runs 10,000 Monte Carlo draws. Tier 2 is a register of 11 emerging opportunities.
- New outputs: data/clean/model_tier1_results.csv, model_backtest.csv, model_calibration.csv, model_supply_overlay.csv, model_tier2_register.csv, and the results note research/model/outlook_results.md.
- Figures: report/fig/fig3_scenarios.svg is now a fan chart (P10 to P90 band, P50 line) per industry and replaces the earlier three scenario dot chart. report/fig/fig4_supply_overlay.svg is new. The old fig3 block was removed from tools/figures/make_figures.py so it no longer overwrites the fan chart.
- data/sources.csv: MODEL_ rows (parameters, derived anchors, backtest errors) added through tools/add_sources.py.
- model/model.py was not changed. It still holds the earlier EUR market model and the eight criteria scoring. Rerunning it regenerated the Excel file and the f2 to f10 figures without changes to inputs.

Why
- The methodology promises a calibrated, back tested outlook with a supply overlay and a separate register for unconfirmed options. The earlier scenario growth rates (Scenarios sheet in report/metals_database.xlsx) were team guesses without calibration or ranges.

Known limits
- Nickel by industry is an index (2025 = 100) because no tonnage per industry is published. Cobalt has tonnes only for aviation (11,499 t, measured) and non aviation superalloys (8,501 t, derived).
- Backtest windows are short (5 to 10 points) and 2020 to 2025 contains the pandemic. The growth correction is capped at 1.0 percentage point a year and was binding for energy, oil and gas, and automotive. Results without the shift are in the p50_2035_without_backtest_shift column.
- OECD STAN output is nominal, so it only widens ranges.
- The workbook rows tagged [2035 candidate; inference] are not in the repository. Tier 2 follows the framework chapter and research notes. Six rows have no repository evidence and carry TODO(data).
- Open TODO(data): ten year official outlook versus outcome, aircraft fleet and EV sales history tables, SEMI path after 2031, alloy tonnes by industry.

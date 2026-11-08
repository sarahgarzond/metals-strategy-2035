# Model changelog

## 2026-11-08 run (round 5): FeNi rebuild, backtest correction, tonnes, shocks, rule based scores

What changed
- FeNi family (model/outlook_2035.py): the SEMI fab equipment weight is gone (fab tools use no Invar). The family is now OLED fine metal mask foil (0.40), EV magnetic sensor and shielding parts (0.25) and lead frames and glass seals (0.35), Dirichlet concentration 8. New parameters MODEL_FENI_OLED_G (minus 3, 3, 8.3 percent a year, high end is DNP's quoted mask sales growth), MODEL_FENI_OLED_FMM_SHARE (0.5, 0.9, 1.0) and MODEL_FENI_EV_SHARE (0.5, 0.85, 1.05, competition from electrical steel, FeCo and nanocrystalline cores). No OLED line capacity or shipment series exists in research/, so evidence is flagged low. Result P10/P50/P90 101/129/163 (round 4: 134/157/185), electronics only variant 89/118/153.
- Backtest: the trend shift is no longer added on top of official guidance drivers (Siemens Energy capacity, IEA scenarios, Airbus GMF). It is still computed (shift_old) so that Table 13 can be shown with and without it. Only the backtest sd widens the ranges. Two new tier 1 CSV columns: p50_2035_without_backtest_shift (no shift, no haircut) and p50_2035_with_backtest_shift_round4_method.
- Outlook versus outcome tests found in the repository: IEA WEI 2025 versus WEI 2026 (0.951), Boeing 737 rate plan 47 versus 42 reached (0.894), LEAP 2026 guidance versus nine months (1.068, counter evidence). They set an optimism haircut on 2035 activity: aerospace 0.80/0.92/1.02, energy, oil and gas and automotive 0.85/0.95/1.02 (MODEL_HAIRCUT_AERO, MODEL_HAIRCUT_OFFICIAL). Older Airbus GMF, Boeing CMO or IEA WEO editions with annual paths are not in the repository, so no ten year test is possible (TODO(data)).
- Energy: gas turbine ratio range widened from 1.15 to 1.85 to 1.00 to 2.00 because Siemens Energy is one OEM (GE Vernova and Mitsubishi Power are not in research/).
- Tonnes: new data/clean/model_family_tonnes.csv with 2025 base kt (P10/P50/P90) and 2035 kt for four families, labelled team estimate and never summed. FeNi is not estimable (TODO(data)). New parameters MODEL_TON_*.
- Supply shocks: new data/clean/model_supply_shocks.csv (Congo cobalt quota, China tungsten licence halt, Indonesia ore quota, plus the severe aerospace demand case). Severe case parameter MODEL_SEVERE_AERO_RECOVERY.
- Register: captive PM disc powder and open market AM powder are split out as established rows (status column added to data/clean/model_tier2_register.csv), a narrower tier 2 row remains for newly specified AM hot section parts. The LEAP fuel nozzle printed in CoCr is NOT asserted as fact because no source is in research/ (TODO(data)).
- Scores: new model/scoring.py computes market, growth and supply security from rules and carries five judgement criteria. Outputs data/clean/model_scores.csv (full precision, equal weight and 20 percent entry barrier sensitivities under two reweighting rules) and model_scoring_inputs.csv. Called by outlook_2035.py.
- model/model.py: Excel gains sheets 8 to 11 (outlook industries, family tonnes, scores, shocks) and prints a reconciliation of materials, sectors and regions (2025: sectors +0.00 percent, regions minus 0.04 percent. 2035: sectors +0.00 percent, regions +0.09 percent). Opportunity cells in model.py are unchanged.
- New figure report/fig/fig5_feni_severe_aero.svg. fig3 and fig4 regenerated. data/sources.csv: MODEL_ rows updated, MO_HAYNES_C276_W added (tungsten nominal 4 percent, page not re-opened, verify).

Why
- Round 4 graders: FeNi was driven by an index that does not measure it, the backtest correction raised guided drivers twice, no tonnes, no tungsten or aerospace downside test, register mixed established and emerging routes, and scores broke the team's own Table A4 rules (FeNi market 3 without a measured pool, chemical plate scored on an all end use pool, tungsten in C-276 ignored).

Known limits
- The FeNi result rests on assumed weights and shares (low evidence). The OLED driver is a sales growth quote, not foil tonnes.
- Tonnes use wide team assumptions (cobalt content 4 to 15 percent, EU share of world 12 to 30 percent). The flat product family is all nickel flat grades, an upper bound for high performance alloy.
- Haircut evidence is two plan versus outcome points and one vintage. Aerospace growth P50 is 2.98 percent, just under the 3.0 percent band edge, so the engine bar score of 3 is sensitive.
- Supply security does not count tungsten for superalloy grades because tungsten content of those alloys is not evidenced in the repository. If it were counted for turbine remelt stock, its supply score would fall from 3 to 2 (column supply_if_untested_inputs_counted).
- Entry barriers, competition, technology, customers and differentiation scores are team judgement (round 4 values), approval times are TODO(data).

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

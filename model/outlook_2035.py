#!/usr/bin/env python3
"""Two tier 2035 outlook model (chapter 3 of the report).

Tier 1: D = Activity x Intensity x Share for seven industries, calibrated to measured end use, back tested on
history to 2019 versus 2020 to 2025, simulated with 10,000 Monte Carlo draws (seed 20261108) and tested against a
supply overlay.  Tier 2: a register of emerging opportunities that the data cannot yet confirm.

Inputs: only files already in the repository (data/clean, data/sources.csv, research notes, data/raw/eurostat json).
Every parameter is either sourced (data_id), derived from sourced numbers, or a labelled team assumption with a range
and a reason.  Where metal tonnage per unit is not published the industry is an index of relevant alloy demand
(2025 = 100) and the output says so.

Outputs
  data/clean/model_tier1_results.csv      industry and product family results, P10/P50/P90 for 2035
  data/clean/model_backtest.csv           history to 2019 fitted, 2020 to 2025 projected, MAPE and bias
  data/clean/model_calibration.csv        calibration checks against measured end use
  data/clean/model_supply_overlay.csv    2035 demand versus base supply and stress cases
  data/clean/model_tier2_register.csv    emerging opportunity register
  data/clean/model_scores.csv, model_scores_cases.csv, model_combined_programme.csv, model_aerospace_haircut_cases.csv,
  data/clean/model_engine_delivery_path.csv, model_family_value.csv, model_shock_tiers.csv, model_supply_shocks.csv (every tier change per shock)
  data/clean/comtrade_hs6_alloy_*.csv and research/model/comtrade_hs6_alloy.md (via model/comtrade_hs6.py)
  research/model/outlook_results.md       compact tables for chapter 7 and appendix A2
  report/fig/fig3_scenarios.svg, report/fig/fig4_supply_overlay.svg
  data/sources.csv                        MODEL_ rows (via tools/add_sources.py)
Run: python3 model/outlook_2035.py [--no-log]
"""
import csv
import json
import math
import os
import subprocess
import sys

import numpy as np
import pandas as pd

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CLEAN = os.path.join(ROOT, "data", "clean")
FIG = os.path.join(ROOT, "report", "fig")
NOTE = os.path.join(ROOT, "research", "model", "outlook_results.md")
SEED, N = 20261108, 10000
Y0, Y1 = 2025, 2035
H = Y1 - Y0
LAMBDA = 0.5      # share of the backtest growth error that is corrected (team assumption)
SHIFT_CAP = 0.010  # largest correction of annual growth, 1.0 percentage point (team assumption)
KAPPA = 0.5       # share of the backtest RMSE carried into the 2035 range (team assumption)
SD_CAP = 0.030    # cap on the annual error carried into the range (team assumption)
RHO_GLOBAL, RHO_IND = 0.2, 0.3   # copula weights: global cycle and industry factor (team assumption)
CONC = 40.0       # Dirichlet concentration for component and product weights (team assumption)
rng = np.random.default_rng(SEED)
rng_new = np.random.default_rng(SEED + 1)   # FeNi components use their own stream, so the other draws stay reproducible

# ------------------------------------------------------------------ helpers


def rd(name):
    return pd.read_csv(os.path.join(CLEAN, name))


_erf = np.frompyfunc(math.erf, 1, 1)


def phi(z):
    return 0.5 * (1.0 + _erf(z / math.sqrt(2.0)).astype(float))


def tri_ppf(u, lo, mode, hi):
    u = np.clip(u, 1e-9, 1 - 1e-9)
    if hi <= lo:
        return np.full_like(u, lo)
    c = (mode - lo) / (hi - lo)
    return np.where(u < c, lo + np.sqrt(u * (hi - lo) * (mode - lo)), hi - np.sqrt((1 - u) * (hi - lo) * (hi - mode)))


Z0 = rng.standard_normal(N)
ZI = {}


def u_act(ind):
    """Uniform draw for an activity driver: global cycle factor, industry factor and own noise (Gaussian copula)."""
    if ind not in ZI:
        ZI[ind] = rng.standard_normal(N)
    e = rng.standard_normal(N)
    z = math.sqrt(RHO_GLOBAL) * Z0 + math.sqrt(RHO_IND) * ZI[ind] + math.sqrt(1 - RHO_GLOBAL - RHO_IND) * e
    return phi(z)


def u_ind():
    return rng.random(N)


def dirichlet(wdict, conc=None, gen=None):
    keys = list(wdict)
    a = np.array([wdict[k] for k in keys]) * (CONC if conc is None else conc)
    g = (gen or rng).gamma(a, size=(N, len(keys)))
    g = g / g.sum(axis=1, keepdims=True)
    return {k: g[:, i] for i, k in enumerate(keys)}


def pct(x):
    return np.percentile(x, [10, 50, 90])


PARAMS = []   # registry of every parameter: used for the assumption table and for data/sources.csv


def par(pid, what, lo, mode, hi, unit, basis, src, reason):
    PARAMS.append(dict(id=pid, what=what, lo=lo, mode=mode, hi=hi, unit=unit, basis=basis, src=src, reason=reason))
    return (lo, mode, hi)


def f(x, d=3):
    return f"{x:.{d}f}"


# ------------------------------------------------------------------ 1. backtest

BT = []   # backtest rows


def fit_test(years, vals, train_end):
    y = np.asarray(years, float)
    v = np.asarray(vals, float)
    tr, te = y <= train_end, y > train_end
    b, a = np.polyfit(y[tr], np.log(v[tr]), 1)
    pred = np.exp(a + b * y[te])
    act = v[te]
    ape = np.abs(pred - act) / act
    bias = (pred - act) / act
    t_last = y[te].max()
    realised = math.log(v[y == t_last][0] / v[y == train_end][0]) / (t_last - train_end)
    return dict(n_train=int(tr.sum()), n_test=int(te.sum()), mape=float(ape.mean()), bias=float(bias.mean()),
                trend=float(b), realised=float(realised), err=float(b - realised), last=int(t_last),
                first=int(y[tr].min()))


def add_bt(sid, industry, driver, basis, shift_ok, years, vals, train_end, src, note):
    r = fit_test(years, vals, train_end)
    r.update(series=sid, industry=industry, driver=driver, price_basis=basis, shift_ok=shift_ok, src=src, note=note)
    BT.append(r)
    return r


# IEA World Energy Investment 2026, world, real 2025 USD
wei = rd("iea_wei2026_by_region.csv")
W = wei[wei.region == "World"]


def wei_series(item):
    s = W[W["item"] == item].set_index("year")["usd_bn_2025"]
    return [y for y in s.index if y <= 2025], [s[y] for y in s.index if y <= 2025]


for sid, item, ind, drv, note in [
    ("BT_WEI_UPSTREAM", "Memo: Oil & gas upstream", "oil_and_gas", "IEA WEI upstream oil and gas investment, world",
     "Pre 2019 window opens in the 2015 price collapse, so the fitted trend is steeply negative."),
    ("BT_WEI_GASPWR", "Oil and natural gas (unabated)", "energy", "IEA WEI investment in unabated oil and gas power, world",
     "Gas power investment rose from 64 USD bn in 2019 to 112 in 2025."),
    ("BT_WEI_NUC", "Nuclear", "energy", "IEA WEI nuclear investment, world", "Real 2025 USD."),
]:
    yy, vv = wei_series(item)
    add_bt(sid, ind, drv, "real (2025 USD)", True, yy, vv, 2019, "IEA_WEI_UPSTREAM_REGION_2026 / IEA_WEI_GASPOWER_2025", note)

# OECD hip and knee procedures, constant set of countries with both procedures in every year 2013 to 2024
hk = rd("oecd_health_hip_knee_procedures.csv")
pv = hk.pivot_table(index=["country", "procedure"], columns="year", values="procedures")
yrs_hk = list(range(2013, 2025))
full = pv.dropna(subset=yrs_hk)
ctry = sorted(set(c for c, p in full.index if (c, "hip") in full.index and (c, "knee") in full.index))
hip = full.xs("hip", level="procedure").loc[ctry, yrs_hk].sum()
knee = full.xs("knee", level="procedure").loc[ctry, yrs_hk].sum()
tot = hip + knee
add_bt("BT_OECD_HK", "medical", f"OECD hip plus knee procedures, {len(ctry)} countries with complete 2013 to 2024 data",
       "real (counts)", True, yrs_hk, tot.values, 2019, "MED_OECD_HK_COUNT_2023",
       "Test window includes the 2020 pandemic dip and the recovery.")


def cagr(a, b, n):
    return (b / a) ** (1.0 / n) - 1.0


hk_cagr = dict(hip=cagr(hip[2013], hip[2024], 11), knee=cagr(knee[2013], knee[2024], 11),
               pooled=cagr(tot[2013], tot[2024], 11), pre=cagr(tot[2013], tot[2019], 6), post=cagr(tot[2019], tot[2024], 5))

# OECD STAN output (current prices, national currency): nominal, so used only to widen ranges, never to shift
for fl, act, ind, lab in [("P1", "C30", "aerospace", "other transport equipment (ISIC C30, includes aerospace)"),
                          ("P1", "C26", "electronics", "computer, electronic and optical products (ISIC C26)"),
                          ("P1", "C27", "electronics", "electrical equipment (ISIC C27)"),
                          ("P1", "C20", "chemical", "chemicals and chemical products (ISIC C20)"),
                          ("P1", "C29", "automotive", "motor vehicles (ISIC C29)")]:
    t = rd(f"oecd_stan_{fl}.csv")
    t = t[t.ACTIVITY == act]
    p = t.pivot_table(index="REF_AREA", columns="TIME_PERIOD", values="OBS_VALUE")
    cols = list(range(2010, 2024))
    p = p.dropna(subset=cols)
    idx = np.exp(np.log(p[cols].div(p[2019], axis=0)).mean(axis=0))
    add_bt(f"BT_STAN_{act}", ind, f"OECD STAN output, {lab}, geometric mean of {len(p)} countries ({', '.join(p.index)})",
           "nominal (current prices)", False, cols, idx.values, 2019, "OECD_STAN_P1",
           "Nominal national currency, no deflator in the repository, so the bias is contaminated by 2021 to 2023 inflation and is not used to shift.")

# Eurostat production volume index NACE C29 (2021 = 100), EU27 and four member states
js = json.load(open(os.path.join(ROOT, "data", "raw", "eurostat_sts_inpr_a_C29.json")))
geos = list(js["dimension"]["geo"]["category"]["index"])
tm = list(js["dimension"]["time"]["category"]["index"])
vraw = js["value"]
vals = [(vraw.get(str(i)) if isinstance(vraw, dict) else vraw[i]) for i in range(len(geos) * len(tm))]
for gi, g in enumerate(geos):
    row = vals[gi * len(tm):(gi + 1) * len(tm)]
    if any(x is None for x in row):
        continue
    add_bt(f"BT_EUROSTAT_C29_{g}", "automotive", f"Eurostat volume index NACE C29, {g}", "real (volume index)", g == "EU27_2020",
           [int(x) for x in tm], row, 2019, "EUROSTAT_C29_EU27_2025", "Only five training points (2015 to 2019).")

bt_df = pd.DataFrame(BT)

# industry level correction from the backtest
BT_IND = {}
for ind, g in bt_df.groupby("industry"):
    real = g[g.shift_ok]
    mean_err = float(real.err.mean()) if len(real) else 0.0
    shift = -LAMBDA * float(np.clip(mean_err, -SHIFT_CAP / LAMBDA, SHIFT_CAP / LAMBDA))
    rmse = float(np.sqrt((g.err ** 2).mean()))
    sd = KAPPA * min(rmse, SD_CAP)
    # The trend backtest bias is NOT added to drivers that are official guidance (Siemens Energy capacity, IEA scenarios, Airbus GMF).
    # It is still computed (shift_old) so that a sensitivity can be shown. Only the sd widens the range.
    BT_IND[ind] = dict(mean_err=mean_err, shift_old=shift, shift=0.0, rmse=rmse, sd=sd, n_real=len(real), n=len(g))
    par(f"MODEL_BT_{ind.upper()}", f"Backtest range widening for {ind}: annual sd carried into the range (trend shift computed but not applied)", 0.0, mean_err, sd,
        "per year (shift applied, mean error, sd)", "derived from backtest", "OECD_STAN_P1 / IEA_WEI_UPSTREAM_REGION_2026 / MED_OECD_HK_COUNT_2023 / EUROSTAT_C29_EU27_2025",
        f"No growth shift is applied, because the drivers are official guidance and scenarios, not trend extrapolations, and a trend error must not be added on top. A trend shift (not used) would have been {shift*100:+.2f} pp a year (minus {LAMBDA} times the mean annual growth error of real series, capped at {SHIFT_CAP*100:.1f} pp). The sd is {KAPPA} times the RMSE of all series (capped at {SD_CAP*100:.1f} pp). Lambda, kappa and caps are team assumptions: windows are short and 2020 to 2025 contains the pandemic.")

# one point outlook versus outcome (two vintages of the IEA investment series)
OUTLOOK_CHECK = dict(series="BT_OUTLOOK_WEI2025_vs_WEI2026", outlook=570.0, outcome=542.0)

# Outlook versus outcome tests that exist in the repository. Ratio = outcome / outlook (below 1 means the plan was optimistic).
# Older Airbus GMF, Boeing CMO or IEA WEO editions with a year by year path are NOT in the repository (only AIRBUS_GMF_2025 as a 20 year total),
# so no ten year outlook can be tested. TODO(data): GMF 2016 to 2019 and CMO 2016 to 2019 delivery paths against actual deliveries.
# Airbus 2026 run rate: 9M 2026 deliveries 547 against 9M 2025 507 of a full year 793 (CO_AIRBUS_9M_2026, CO_AIRBUS_DELIV_2025), guidance about 870 (CO_AIRBUS_GUIDE_2026)
AIRBUS_PROJ_2026 = 547.0 / (507.0 / 793.0)
# LEAP full year 2026 implied by nine months (1,565) plus Q4 2025 level (562) flat to +5 percent (CO_GE_9M26_DELIV, CO_SAFRAN_REV_2025)
LEAP_FY_LO, LEAP_FY_HI = (1565 + 562) / 1802.0, (1565 + 562 * 1.05) / 1802.0
OUTLOOK_TESTS = [
    dict(id="OT_WEI_UPSTREAM", industry="oil_and_gas, energy", use="energy, oil and gas, automotive",
         what="IEA WEI 2025 estimate of 2025 upstream oil and gas investment (just under USD 570 bn, 2024 prices) versus WEI 2026 outcome (USD 542 bn, 2025 prices)",
         outlook=570.0, outcome=542.0, src="OG_WEO2025_UPSTREAM_2025, IEA_WEI_UPSTREAM_REGION_2026",
         note="One point, one year ahead. The two figures are on DIFFERENT price bases (2024 against 2025 USD) and no deflator is in the repository, so the ratio mixes price and volume (TODO(data): rebase). It is an investment series, not aerospace, so it is not used for the aerospace haircut."),
    dict(id="OT_BA_737_RATE", industry="aerospace", use="aerospace",
         what="Boeing 737 production rate reached in Q4 2025 (42 a month) versus the plan rate for 2026 (47 a month)",
         outlook=47.0, outcome=42.0, src="CO_BA_RATES_2025, CO_BA_737RATE_2026",
         note="This compares a rate reached in Q4 2025 with the rate planned for the following year, so it is the gap to be closed, not a final miss. Boeing's chief executive said it will take until 2027 to be stable at 47 a month (wing supply is the bottleneck), which confirms a slip of about one year."),
    dict(id="OT_AIRBUS_2026", industry="aerospace", use="aerospace",
         what="Airbus 2026 deliveries: guidance of about 870 versus the full year implied by nine months (547) at the 2025 seasonality (507 of 793 delivered in the first nine months)",
         outlook=870.0, outcome=AIRBUS_PROJ_2026, src="CO_AIRBUS_GUIDE_2026, CO_AIRBUS_9M_2026, CO_AIRBUS_DELIV_2025",
         note="A projection of the outcome, not a final outcome. Reaching 870 needs about 323 deliveries in Q4 against 286 in Q4 2025. Pratt and Whitney engine shortages are the stated drag."),
    dict(id="OT_LEAP_2026", industry="aerospace", use="aerospace",
         what="CFM LEAP deliveries 2026: GE guidance of high teens growth (18 percent) versus GE nine month growth of 26 percent",
         outlook=1.18, outcome=1.26, src="CO_GE_Q2LEAP_2026, CO_GE_9M26_DELIV",
         note=f"Engines beat guidance while airframe rates slipped: counter evidence, a ratio above 1. The nine month growth overstates the full year, because Q3 grew only 4.7 percent (535 against 511). Nine months plus a flat to plus 5 percent Q4 on the 562 engines of Q4 2025 gives full year growth of {100*(LEAP_FY_LO-1):.0f} to {100*(LEAP_FY_HI-1):.0f} percent, a ratio of {LEAP_FY_LO/1.18:.3f} to {LEAP_FY_HI/1.18:.3f}."),
]
for t in OUTLOOK_TESTS:
    t["ratio"] = t["outcome"] / t["outlook"]
OT = {t["id"]: t["ratio"] for t in OUTLOOK_TESTS}
# Memo, not a test of a forecast: 2025 combined Airbus plus Boeing deliveries against the average annual requirement of the GMF 2025 path
MEMO_DELIV_RATIO = (793 + 600) / (43420 / 20.0)
AERO_PTS = [OT[k] for k in ("OT_BA_737_RATE", "OT_AIRBUS_2026", "OT_LEAP_2026")]
AERO_MEAN = float(np.mean(AERO_PTS))

# optimism haircut: ratio of realised to officially guided 2035 activity, applied to drivers that are official guidance.
# The haircut quoted in prose is the MEDIAN of the draws (triangular low/mode/high are the inputs).
HAIR_AERO = par("MODEL_HAIRCUT_AERO", "Optimism haircut on aerospace activity 2035 (realised over guided), ratio", 0.80, round(AERO_MEAN, 2), 1.07, "ratio", "derived plus team assumption",
                "CO_BA_RATES_2025 / CO_BA_737RATE_2026 / CO_AIRBUS_GUIDE_2026 / CO_AIRBUS_9M_2026 / CO_GE_Q2LEAP_2026 / CO_GE_9M26_DELIV / CO_AIRBUS_DELIV_2025 / AIRBUS_GMF_2025",
                f"Triangular mode {AERO_MEAN:.2f} is the equal weight mean of all three aerospace plan against outcome points: Boeing 737 rate reached in Q4 2025 against the 2026 plan rate ({OT['OT_BA_737_RATE']:.3f}), Airbus 2026 run rate against the 870 guidance ({OT['OT_AIRBUS_2026']:.3f}, a projection) and the LEAP counter evidence ({OT['OT_LEAP_2026']:.3f}). Low 0.80 doubles the Boeing shortfall (team assumption, a delivery ramp that slips about three years). High 1.07 is the LEAP point. The median of the draws is {float(tri_ppf(np.array([0.5]), 0.80, round(AERO_MEAN, 2), 1.07)[0]):.2f} and is the figure quoted in the text. Sensitivities: Boeing point only 0.894, LEAP full year ratio {LEAP_FY_LO/1.18:.3f} to {LEAP_FY_HI/1.18:.3f} instead of 1.068 gives a mean of {np.mean([OT['OT_BA_737_RATE'], OT['OT_AIRBUS_2026'], LEAP_FY_LO/1.18]):.3f}. The IEA investment ratio ({OT['OT_WEI_UPSTREAM']:.3f}) is excluded because it is not an aerospace series and mixes price bases. Memo: 2025 Airbus 793 plus Boeing 600 deliveries are {100*MEMO_DELIV_RATIO:.0f} percent of the Airbus GMF 2025 average annual requirement of 2,171 aircraft, so the ramp is behind the path (backlog 8,754 Airbus aircraft). Three points, one vintage: low evidence.")
HAIR_OTH = par("MODEL_HAIRCUT_OFFICIAL", "Optimism haircut on energy, oil and gas, automotive activity 2035 (realised over guided), ratio", 0.85, 0.95, 1.02, "ratio", "derived plus team assumption",
               "OG_WEO2025_UPSTREAM_2025 / IEA_WEI_UPSTREAM_REGION_2026",
               f"Triangular mode 0.95 is the IEA WEI vintage ratio ({OT['OT_WEI_UPSTREAM']:.3f}), the median of the draws is {float(tri_ppf(np.array([0.5]), 0.85, 0.95, 1.02)[0]):.2f} and is the figure quoted in the text. The ratio compares a 2024 price base estimate with a 2025 price base outcome, so it mixes price and volume (no deflator in the repository, TODO(data)). Low 0.85 and high 1.02 are team assumptions: one point, one year ahead, so the width is deliberately generous. Siemens Energy capacity is one OEM only (GE Vernova and Mitsubishi Power are not in research/, TODO(data)).")
HAIR = {}
_hg = np.random.default_rng(SEED + 2)
_u_ha = _hg.random(N)
_u_ho = _hg.random(N)
HAIR["aerospace"] = tri_ppf(_u_ha, *HAIR_AERO)
for _k in ("energy", "oil_and_gas", "automotive"):
    HAIR[_k] = tri_ppf(_u_ho, *HAIR_OTH)

# ------------------------------------------------------------------ 2. Tier 1 specification

# derived anchors
airbus_cagr = cagr(23310, 45550, 20)
gt_ratio = (30.0 / 17.0) ** (4.0 / 5.0)          # Siemens Energy 17 GW FY2024, 30 GW FY2029 midpoint, flat after
lng_2025 = 560 * (880 / 560) ** (1 / 11)
lng_hi = 880 / lng_2025
semi_2031 = 1.07 * 1.08 ** 3 * 0.94 * 1.09
dc_2025 = 415 * (945 / 415) ** (1 / 6)
dc_2030 = 945 / dc_2025
co_super_nonav = 20000 - 11499
f1_aero_w = 11499 / 20000

# component definitions: act = ('ratio', lo, mode, hi) | ('cagr', ...) | ('two', near3, g3) | ('semi', real3, g3)
IND_COMP = {}


def comp(ind, name, w, act, intens, share, driver_text, src):
    IND_COMP.setdefault(ind, []).append(dict(name=name, w=w, act=act, int=intens, share=share, driver=driver_text, src=src))


# AEROSPACE
a1 = par("MODEL_AERO_MRO_G", "Aerospace aftermarket pull, annual growth 2025 to 2035", 0.030, 0.037, 0.042, "per year", "sourced",
         "AERO_AIRBUS_GSF2026_SERVICES_2045 / AERO_BOEING_CMO2026_FLEET_CAGR / AERO_ICAO_RPK_CAGR",
         "Mode: Airbus GSF off wing maintenance growth 3.7 percent a year. Low: Boeing jet fleet growth 3.0 percent. High: ICAO long term passenger traffic growth 4.2 percent.")
# Engine delivery path (team estimate from logged delivery evidence). Anchors: 2025 outturn, 2026 guidance, 2028 plan, 2035 requirement.
ENG_GMF_AVG = 42060 / 20.0      # Airbus GMF 2026 to 2045 new passenger aircraft deliveries, average a year (AERO_AIRBUS_GMF2026_DELIVERIES)
ENG_CMO_AVG = 43625 / 20.0      # Boeing CMO 2026 to 2045 new airplane deliveries, average a year (BOEING_CMO_2026)
ENG_BASE_AC = 793 + 600          # Airbus 2025 (CO_AIRBUS_DELIV_2025) plus Boeing 2025 (CO_BA_DELIV_2025) deliveries
R35_REQ = (ENG_GMF_AVG / ENG_BASE_AC, ENG_CMO_AVG / ENG_BASE_AC)
a2n = par("MODEL_AERO_NEW_E26", "New engine output 2026 over 2025 (LEAP deliveries, ratio)", 2000 / 1802.0, 1.18, round(LEAP_FY_HI, 2), "ratio", "sourced",
          "CO_GE_LEAP_2025 / CO_SAFRAN_CEO_2026 / CO_GE_Q2LEAP_2026 / CO_GE_9M26_DELIV / CO_SAFRAN_REV_2025",
          f"LEAP deliveries were 1,802 in 2025 (562 in Q4). Low: the CEO floor of more than 2,000 engines (1.11). Mode: guidance of high teens growth (1.18), which nine months at 1,565 plus a Q4 equal to Q4 2025 reproduces ({LEAP_FY_LO:.3f}). High: nine months plus a Q4 5 percent above Q4 2025 ({LEAP_FY_HI:.3f}). Nine month growth of 26 percent is not used as a full year rate because Q3 grew only 4.7 percent. Evidence only: the 2035 ratio below is the driver.")
a2m = par("MODEL_AERO_NEW_E28", "New engine output 2028 over 2025 (LEAP plan, ratio)", round(1.18 * 1.03 ** 2, 2), round(2500 / 1802.0, 2), round(2600 / 1802.0, 2), "ratio", "sourced plus team assumption",
          "CO_SAFRAN_LEAP_2025 / CO_GE_LEAP_2025",
          "Mode: about 2,500 LEAP in 2028 (Safran capital markets day 2024), high: about 2,600 (2028e chart, slide 19). Low: the 2026 mode followed by 3 percent a year (team assumption: material shortages persist). Evidence only: it brackets the early path and is a plan, so the haircut applies to it.")
a2g = par("MODEL_AERO_NEW_R35", "New engine output 2035 over 2025 (engine delivery path, ratio, before haircut)", round(a2m[0], 2), round(float(np.mean(R35_REQ)), 2), round(a2m[1] * (1 + airbus_cagr) ** 7, 2), "ratio", "derived plus team assumption",
          "AERO_AIRBUS_GMF2026_DELIVERIES / BOEING_CMO_2026 / CO_AIRBUS_DELIV_2025 / CO_BA_DELIV_2025 / AERO_AIRBUS_GMF2026_FLEET_2025 / AERO_AIRBUS_GMF2026_FLEET_2045",
          f"Mode: average annual new aircraft deliveries 2026 to 2045 (Airbus GMF {ENG_GMF_AVG:,.0f}, Boeing CMO {ENG_CMO_AVG:,.0f}) over the 2025 deliveries of Airbus plus Boeing ({ENG_BASE_AC:,}) = {R35_REQ[0]:.2f} to {R35_REQ[1]:.2f}, mean {np.mean(R35_REQ):.2f}. 2035 is the middle of the 20 year window, so a rising delivery path crosses its average about there. The 2025 base covers two OEMs while the forecasts cover all makers (COMAC and Embraer), which overstates the ratio slightly. Engines per aircraft are taken as constant. Low: the low 2028 level and no growth after. High: the 2028 plan of 2,600 followed by the Airbus fleet growth of {100*airbus_cagr:.1f} percent a year to 2035. Replaces the earlier two step path (2026 guidance, then fleet growth).")
ai = par("MODEL_AERO_INT", "Superalloy mass per engine and aircraft, annual trend", -0.010, 0.0, 0.010, "per year", "team assumption", "AERO_AIRBUS_GMF2026_NEWGEN_2035",
         "No kilogram per engine is published. New generation share rises from 39 to 82 percent (hotter cores add alloy, durability kits and fewer shop visits remove it).")
ash = par("MODEL_AERO_SHARE", "Nickel and cobalt superalloy share of hot section mass, ratio 2035 to 2025", 0.90, 0.98, 1.03, "ratio", "team assumption", "(none, see reason)",
          "Titanium aluminide already flies in a low pressure turbine and ceramic matrix composites are entering, but no published kilogram displacement exists. Skewed to the downside.")
comp("aerospace", "Aftermarket and engine overhaul pull", 0.5, ("cagr",) + a1, ai, ash,
     "Airbus GSF aviation services growth (off wing maintenance 3.7 percent a year)", "AERO_AIRBUS_GSF2026_SERVICES_2026, AERO_AIRBUS_GSF2026_SERVICES_2045")
comp("aerospace", "New engine output", 0.5, ("ratio",) + a2g, ai, ash,
     "Engine delivery path: LEAP 1,802 in 2025, 2026 guidance, 2028 plan of about 2,500 to 2,600, 2035 at the Airbus and Boeing average delivery requirement", "AERO_LEAP_2025, CO_GE_Q2LEAP_2026, CO_GE_9M26_DELIV, CO_SAFRAN_LEAP_2025, AERO_AIRBUS_GMF2026_DELIVERIES, BOEING_CMO_2026, CO_AIRBUS_DELIV_2025, CO_BA_DELIV_2025")
par("MODEL_AERO_W", "Weight of aftermarket versus new engine output in the aerospace index", 0.5, 0.5, 0.5, "weight", "team assumption", "CO_GE_CES_2025",
    "GE Commercial Engines and Services takes 75 percent of revenue from services, but metal pull per revenue dollar is higher for new parts. Equal weights, Dirichlet noise.")

# ENERGY
e1 = par("MODEL_EN_GT_R", "Gas turbine output ratio 2035 to 2025", 1.00, gt_ratio, 2.00, "ratio", "derived plus team assumption",
         "CO_SIEMENSENERGY_CMD_2025 / CO_SIEMENSENERGY_CAP_2026 / IEA_WEI_GASPOWER_2025",
         "Mode: Siemens Energy path 17 GW (FY2024) to 30 GW (FY2029 midpoint of FY2028 to 2030), flat afterwards, as a proxy for world output. This is ONE OEM: GE Vernova and Mitsubishi Power are not profiled in research/ (TODO(data): their announced capacity), so the range is wide, 1.00 to 2.00. Low 1.00: order cycle turns once the backlog is delivered and output returns to the 2025 level (IEA gas power investment 112 in 2025 and 114 USD bn in 2026, flat). High 2.00: capacity keeps growing about 3 percent a year after 2030 or the other OEMs add more than Siemens Energy.")
e2 = par("MODEL_EN_NUC_R", "Nuclear fleet and tube demand ratio 2035 to 2025", 1.05, 1.20, 1.45, "ratio", "derived plus team assumption",
         "EE_NUC_IAEA_2025 / EE_NUC_WNA_2030 / CO_WESTINGHOUSE_PIPE_2026",
         "Mode: 377 GW operating plus 56 GWe under construction gives 1.15 by 2030, then 4 percent more. Low: retirements offset additions. High: AP1000 and small reactor programmes beyond the build now under way.")
e3 = par("MODEL_EN_OTH_G", "Other power and process equipment, annual growth", 0.020, 0.030, 0.036, "per year", "sourced plus team assumption",
         "EE_ELEC_GROWTH_2024 (same IEA Electricity 2026 executive summary also gives 3.6 percent a year for 2026 to 2030, see research/sectors/energy_environment.md)",
         "Electricity demand growth is the activity proxy for waste to energy, heat exchangers and fuel cell strip. High is the IEA 2026 to 2030 rate.")
ei = par("MODEL_EN_INT", "Alloy mass per GW, annual trend", -0.010, 0.0, 0.010, "per year", "team assumption", "(none, see reason)",
         "No tonne per gigawatt figure is published (the 150 to 500 kg per MW electrolyser figures were rejected in the research note).")
es = par("MODEL_EN_SHARE", "High performance alloy share of energy hardware, ratio 2035 to 2025", 0.97, 1.0, 1.03, "ratio", "team assumption", "(none, see reason)",
         "Hot section, steam generator tube and exchanger material choices are fixed by codes and qualification.")
comp("energy", "Gas turbine hot section", 0.55, ("ratio",) + e1, ei, es, "Siemens Energy gas turbine output 17 GW (FY2024) to 30 GW (FY2028 to 2030)", "CO_SIEMENSENERGY_CMD_2025, CO_SIEMENSENERGY_CAP_2026")
comp("energy", "Nuclear tube and cladding", 0.25, ("ratio",) + e2, ei, es, "Operating nuclear capacity 377 GW plus 56 GWe under construction", "EE_NUC_IAEA_2025, EE_NUC_WNA_2030")
comp("energy", "Other power and process equipment", 0.20, ("cagr",) + e3, ei, es, "IEA electricity demand growth", "EE_ELEC_GROWTH_2024")
par("MODEL_EN_W", "Weights gas turbine, nuclear, other in the energy index", 0.55, 0.25, 0.20, "weight", "team assumption", "AERO_GE_COMM_ENG_2025",
    "Gas turbine hot section is the tight high performance pocket (research/sectors/energy_environment.md). Hydrogen, wind and grids are excluded: tier 2 or marginal nickel content.")

# ELECTRONICS
l1p = par("MODEL_EL_SEMI_REAL", "Realisation of the SEMI 300 mm capacity path to 2031", 0.85, 1.0, 1.05, "ratio", "team assumption", "SEMI_300MM_PATH",
          "SEMI path: capacity +7 percent 2026, +8 percent a year 2027 to 2029, -6 percent 2030, +9 percent 2031 (index 138 in 2031). Fab delays and the memory cycle can cut it. Whether the 2030 and 2031 steps are capacity or spending is ambiguous in the log.")
l1g = par("MODEL_EL_SEMI_G", "Capacity growth 2031 to 2035, annual", 0.0, 0.03, 0.06, "per year", "team assumption", "SEMI_300MM_PATH",
          "SEMI publishes nothing after 2031 (TODO(data)). Range spans a stop to half the 2025 to 2031 rate of 5.5 percent a year.")
l2 = par("MODEL_EL_COMP_G", "Electronic components, lead frames and metal masks, annual growth", 0.0, 0.025, 0.06, "per year", "team assumption",
         "ZVEI_PROD_REAL / DNP_INVAR_2024", "ZVEI real production 0.0 percent in 2025 and +2.0 percent in 2026. DNP doubled metal mask capacity, so the high end is above trend.")
eli = par("MODEL_EL_INT", "Alloy per unit of electronics, annual trend", -0.015, 0.0, 0.010, "per year", "team assumption", "NVDA_800VDC",
          "No kilogram per tool is published. 800 VDC racks cut copper, thinner lead frames cut strip mass.")
els = par("MODEL_EL_SHARE", "High performance alloy share, ratio 2035 to 2025", 0.95, 1.0, 1.05, "ratio", "team assumption", "DNP_INVAR_2024",
          "Mask free displays are a downside, expansion alloy lead frames an upside.")
comp("electronics", "Semiconductor equipment, 300 mm capacity", 0.6, ("semi", l1p, l1g), eli, els, "SEMI 300 mm installed capacity path to 2031, then extension", "SEMI_300MM_PATH, SEMI_300MM_2026, SEMI_300MM_2029")
comp("electronics", "Components, lead frames and metal masks", 0.4, ("cagr",) + l2, eli, els, "ZVEI real production and DNP mask capacity", "ZVEI_PROD_REAL, DNP_INVAR_2024")
par("MODEL_EL_W", "Weights semiconductor equipment versus components", 0.6, 0.4, 0.4, "weight", "team assumption", "SEMI_300MM_2026",
    "Equipment is the best measured driver but only part of the alloy pull. No alloy kilograms are published for either.")

# MEDICAL
mlo, mmo, mhi = min(hk_cagr.values()), hk_cagr["pooled"], max(hk_cagr.values())
m1 = par("MODEL_MED_HK_G", "Hip and knee procedures, annual growth 2025 to 2035", mlo, mmo, mhi, "per year", "derived from data",
         "MED_OECD_HK_COUNT_2023",
         f"Constant set of {len(ctry)} OECD countries 2013 to 2024. Mode is the pooled rate, low and high are the lowest and highest of hip, knee, pre 2019 and post 2019 rates (team arithmetic on data/clean/oecd_health_hip_knee_procedures.csv).")
m2 = par("MODEL_MED_OTH_G", "Other medical alloy uses, annual growth", 0.018, 0.030, 0.056, "per year", "sourced plus team assumption", "MED_MTE_EUR_2024 / MED_MTE_EUR_2025",
         "MedTech Europe: European market 170 to 173 EUR bn (1.8 percent in 2025), decade average about 5.6 percent. Value growth, not volume.")
mi = par("MODEL_MED_INT", "Alloy per procedure, annual trend", -0.005, 0.0, 0.005, "per year", "team assumption", "(none, see reason)", "No kilogram per implant is published.")
ms = par("MODEL_MED_SHARE", "CoCr and nickel bearing share of implants, ratio 2035 to 2025", 0.90, 0.97, 1.02, "ratio", "team assumption", "(none, see reason)",
         "Oxidised zirconium (OXINIUM) and titanium substitute for CoCr, and FDA has not restricted CoCr.")
comp("medical", "Hip and knee implants", 0.8, ("cagr",) + m1, mi, ms, "OECD hip plus knee procedures, constant country set", "MED_OECD_HK_COUNT_2023, MED_OECD_HIP_RATE_2023")
comp("medical", "Instruments, leads, dental and other", 0.2, ("cagr",) + m2, mi, ms, "MedTech Europe market growth", "MED_MTE_EUR_2024, MED_MTE_EUR_2025")
par("MODEL_MED_W", "Weights implants versus other medical", 0.8, 0.2, 0.2, "weight", "team assumption", "CO_STRYKER_ORTHO_2025",
    "Implant bar and powder is the evidenced metal use (research/sectors/medical.md).")

# CHEMICAL
c1 = par("MODEL_CH_G", "Chemical processing activity, annual growth 2025 to 2035", -0.010, 0.010, 0.025, "per year", "team assumption anchored on sources",
         "CEFIC_PROD_JANJUL_2026 / CEFIC_CAPUTIL_EU27_Q3_2026 / BASF_APAC_GROWTH_2035",
         "No world volume series exists. EU27 production fell 2.0 percent in January to July 2026 and utilisation is 75.0 percent against 81.3 percent long term, while BASF expects over 80 percent of growth in Asia Pacific. Range equals the earlier team workbook scenarios (-1, 1, 2.5 percent).")
ci = par("MODEL_CH_INT", "Alloy per unit of chemical output, annual trend", -0.005, 0.0, 0.005, "per year", "team assumption", "HAYNES_CPI_REV_FY2023",
         "Haynes chemical volume fell 20.8 percent in fiscal 2023 while price per pound rose 26.7 percent: no stable intensity series.")
cs = par("MODEL_CH_SHARE", "Alloy share of equipment, ratio 2035 to 2025", 0.97, 1.0, 1.03, "ratio", "team assumption", "(none, see reason)", "Materials selection is set by corrosion duty.")
comp("chemical", "Chemical processing plant and maintenance", 1.0, ("cagr",) + c1, ci, cs, "Chemical output proxy (Cefic, Eurostat C20, BASF)", "CEFIC_PROD_JANJUL_2026, CEFIC_CAPUTIL_EU27_Q3_2026")

# OIL AND GAS
o1 = par("MODEL_OG_UP_R", "Upstream oil and gas investment ratio 2035 to 2025 (real)", 0.80, 1.00, 1.12, "ratio", "sourced plus team assumption",
         "OG_WEI2026_UPSTREAM_OG_2026 / OG_WEO2025_CPS_EXTRA_UPSTREAM / IEA_WEI_UPSTREAM_REGION_2026",
         "Stated Policies stays near today's level (mode 1.00), Current Policies adds about 65 USD bn a year, about 11 percent (high). Low 0.80 is a team assumption for oil demand back near 100 mb/d by 2035.")
o2 = par("MODEL_OG_LNG_R", "LNG trade ratio 2035 to 2025", 1.15, 1.35, lng_hi, "ratio", "derived plus team assumption",
         "OG_WEO2025_LNG_DEMAND_2024 / OG_LNG_TRACKER_202610_ADDITIONS",
         "High: Current Policies 560 bcm (2024) to 880 bcm (2035). Low: Stated Policies adds about 200 bcm by 2030 then plateaus with a 65 bcm overhang. Mode is a team assumption between them.")
oi = par("MODEL_OG_INT", "Alloy per USD of upstream and per bcm, annual trend", -0.015, -0.005, 0.010, "per year", "team assumption", "(none, see reason)",
         "Clad pipe saves up to 40 percent against solid wall (BUTTING), lighter SAF 3007 umbilical tube (Alleima), versus more sour and high pressure fields.")
os_ = par("MODEL_OG_SHARE", "Corrosion resistant alloy share, ratio 2035 to 2025", 0.97, 1.0, 1.03, "ratio", "team assumption", "(none, see reason)",
          "Field mix: sour service and deepwater raise it, carbon steel with inhibitors lowers it.")
comp("oil_and_gas", "Upstream investment (subsea, sour service)", 0.7, ("ratio",) + o1, oi, os_, "IEA upstream oil and gas investment, real 2025 USD", "OG_WEI2026_UPSTREAM_OG_2026, OG_WEO2025_CPS_EXTRA_UPSTREAM")
comp("oil_and_gas", "LNG chain", 0.3, ("ratio",) + o2, oi, os_, "IEA LNG trade 560 bcm (2024) to 880 bcm (2035, Current Policies)", "OG_WEO2025_LNG_DEMAND_2024, OG_LNG_TRACKER_202610_ADDITIONS")
par("MODEL_OG_W", "Weights upstream versus LNG", 0.7, 0.3, 0.3, "weight", "team assumption", "OG_WEI2026_GAS_SUPPLY_2026", "Upstream is the larger alloy buyer, LNG uses mostly stainless and 9 percent nickel steel.")

# AUTOMOTIVE
t_car = par("MODEL_AU_CARS_R", "New car sales ratio 2035 to 2025", 0.95, 1.0, 1.10, "ratio", "team assumption", "IEA_WEO_CAR_SALES_2024 / IEA_GEVO_EU_CAR_REG_2035 / ACEA_CAR_REG_2025",
            "IEA does not publish one car sales total for 2035. EU registrations stay near 11 million in the Stated Policies Scenario. The unsourced 85.7 million path in the draft is not used.")
s35 = par("MODEL_AU_EVSHARE_2035", "Electric car share of global sales 2035", 0.40, 0.50, 0.62, "share", "sourced plus team assumption",
          "IEA_WEO_EV_CPS_2035 / IEA_WEO_EV_STEPS_2035 / IEA_GEVO_EV_SHARE_2035 / IEA_GEVO_ECARS_STEPS_2035",
          "Low 40 percent (Current Policies), mode 50 percent (Stated Policies and exploratory scenarios), high 62 percent is a team assumption that covers 55 million electric cars in the Stated Policies Scenario. 2025 share 25 percent.")
ati = par("MODEL_AU_INT_T", "Heat resistant alloy per combustion car, annual trend", 0.0, 0.01, 0.02, "per year", "team assumption", "CO_GARRETT_GAS_PEN_2032 / CO_GARRETT_TURBOMKT_2025",
          "Gasoline turbo penetration is expected to peak at 54 percent by 2032 while turbocharger units fall back by 2030. 2025 penetration is TODO(data).")
ats = par("MODEL_AU_SHARE_T", "Nickel alloy share of exhaust and turbo parts, ratio 2035 to 2025", 0.95, 1.0, 1.03, "ratio", "team assumption", "(none, see reason)", "Stainless substitutes for some turbo and exhaust parts.")
aei = par("MODEL_AU_INT_EV", "Soft magnetic and precision alloy per electric car, annual trend", -0.010, 0.0, 0.020, "per year", "team assumption", "(none, see reason)",
          "Resolvers, shielding and sensors. No kilogram per vehicle is published.")
aes = par("MODEL_AU_SHARE_EV", "FeNi share of motor and sensor parts, ratio 2035 to 2025", 0.90, 1.0, 1.10, "ratio", "team assumption", "(none, see reason)", "Competes with silicon steel and ferrite.")
par("MODEL_AU_W", "Weights thermal parts versus electric vehicle parts in the automotive index", 0.75, 0.25, 0.25, "weight", "team assumption", "CO_GARRETT_SALES_2025",
    "Filed evidence (Garrett, BorgWarner) is thermal, soft magnetic alloys for electric motors are the smaller niche.")

# product families: explicit weights (industry component -> weight)
FAM = {
    "Superalloy bar, billet and remelt stock": dict(w=dict(aerospace=f1_aero_w, energy=0.30, automotive_thermal=0.05, oil_and_gas=0.04, chemical=0.035),
        why="Aerospace weight 0.575 is measured: 11,499 t cobalt in aviation of 20 kt cobalt in superalloys (Cobalt Institute). Remainder split by team assumption: industrial gas turbines 0.30, turbochargers 0.05, oil and gas 0.04, chemical 0.035.",
        src="AERO_CI_AVIATION_CO_2025, AERO_CI_SUPERALLOY_CO_2025"),
    "Nickel alloy bar, rod and wire (long products)": dict(w=dict(chemical=0.25, oil_and_gas=0.25, energy=0.20, aerospace=0.15, medical=0.05, automotive_thermal=0.05, electronics=0.05),
        why="Team assumption guided by end market shares: Haynes chemical processing 15.6 percent of sales (fiscal 2023), Alleima oil and gas 24 percent and chemical 16 percent of revenue (2025).",
        src="HAYNES_CPI_SHARE_FY2023, ALLEIMA_CHEM_2025"),
    "Flat products (plate, sheet, strip, foil)": dict(w=dict(chemical=0.30, energy=0.20, aerospace=0.20, oil_and_gas=0.15, automotive_thermal=0.10, electronics=0.05),
        why="Team assumption: chemical plate and sheet lead (plate heat exchangers, columns), combustor sheet in energy and aerospace, clad liners in oil and gas.",
        src="HAYNES_CPI_SHARE_FY2023, AERO_ATI_JETENG_2025"),
    "Tubes and fittings": dict(w=dict(oil_and_gas=0.35, chemical=0.25, energy=0.25, aerospace=0.05, automotive_thermal=0.05, medical=0.05),
        why="Team assumption: umbilical and downhole tube (Alleima oil and gas 24 percent), process tube, steam generator tube in nuclear.",
        src="ALLEIMA_CHEM_2025, EE_NUC_IAEA_2025"),
    "Precision FeNi strip and foil": dict(w=dict(oled=0.40, ev_sensor=0.25, leadframe=0.35), conc=8.0,
        why="No SEMI fab equipment weight (fab tools use no Invar). Components: OLED fine metal mask foil (driver: DNP metal mask sales growth, mask free competition), EV magnetic sensor and shielding parts (driver: electric car production with an explicit FeNi share range against electrical steel, FeCo and nanocrystalline cores) and lead frames and glass to metal seals (driver: electronic components output). All three weights are team assumptions because no FeNi tonnes by use are published (TODO(data): Proterial, Aperam Imphy and VAC volumes). Dirichlet concentration 8 (low evidence).",
        src="DNP_INVAR_2024, DNP_KUROSAKI_2024, CO_SDC_FMM_8G6_2025, IEA_GEVO_EV_SHARE_2035, ZVEI_PROD_REAL"),
}
FENI = "Precision FeNi strip and foil"
for k, v in FAM.items():
    par("MODEL_FAM_" + "".join(c for c in k.upper() if c.isalpha())[:14],
        f"Product family weights: {k}", min(v['w'].values()), max(v['w'].values()), sum(v['w'].values()), "weights (min, max, sum)", "team assumption",
        v["src"], v["why"] + " Weights: " + ", ".join(f"{a} {b:.3f}" for a, b in v["w"].items()) + f". Dirichlet noise, concentration {v.get('conc', CONC):.0f}.")

# metal content ratios (2035 over 2025)
NI_CONT = par("MODEL_NI_CONTENT", "Nickel content of the alloy class, ratio 2035 to 2025", 0.98, 1.0, 1.02, "ratio", "team assumption", "(none, see reason)", "Grades are specified by standards, so the nickel content moves little.")
CO_CONT_AERO = par("MODEL_CO_CONTENT_AERO", "Cobalt content of aerospace alloys, ratio 2035 to 2025", 0.92, 1.0, 1.04, "ratio", "team assumption", "CO_CMOC_QUOTA_2026",
                   "Export quotas and price spikes push engine makers toward lower cobalt grades, but qualified parts are slow to change.")
CO_CONT_OTH = par("MODEL_CO_CONTENT_OTH", "Cobalt content, other industries, ratio 2035 to 2025", 0.90, 1.0, 1.03, "ratio", "team assumption", "(none, see reason)", "Hardfacing and CoCr implants face substitution.")
TI_AERO = par("MODEL_TI_AERO_R", "Titanium intensity per new aircraft, ratio 2035 to 2025", 1.0, 1.08, 1.20, "ratio", "team assumption", "AERO_AIRBUS_GMF2026_NEWGEN_2035",
              "New generation aircraft (39 to 82 percent of the fleet) use more titanium and composites. No kilogram per aircraft is published.")
DC_EXT = par("MODEL_CU_DC_G", "Data centre power growth 2030 to 2035, annual", 0.03, 0.06, 0.10, "per year", "team assumption", "EE_IEA_DATACENTRE_TWH_2030",
             "IEA: data centre electricity 415 TWh (2024) to 945 TWh (2030). Nothing is published after 2030 (TODO(data)).")
CU_INT = par("MODEL_CU_DC_INT", "Copper per TWh of data centre power, annual trend", -0.040, -0.020, 0.0, "per year", "team assumption", "NVDA_800VDC / NVDA_800VDC_ROWCUT",
             "800 VDC cuts row level copper by 45 percent from 2027 (single source), 54 VDC needs up to 200 kg busbar per MW rack.")

# FeNi drivers
fo_g = par("MODEL_FENI_OLED_G", "OLED fine metal mask (Invar) foil demand growth, annual", -0.030, 0.030, 0.083, "per year", "sourced plus team assumption",
           "DNP_INVAR_2024 / DNP_KUROSAKI_2024 / CO_SDC_FMM_8G6_2025 / CO_SDC_A6_INVEST_2023",
           "LOW EVIDENCE. No OLED panel line capacity in square metres, no OLED shipments and no foil tonnes exist in research/sectors/electronics.md, dnp.md or samsung-display.md (SDC monthly substrate capacity: TODO(data)). Evidence that does exist: DNP doubled metal mask capacity at Kurosaki (2024) with full use planned beyond 2026, masks are jigs so sales follow product types, not panel units, and the DNP Q&A quotes a metal mask sales CAGR of +8.3 percent (page not re-read). High 8.3 percent is that figure. The USD 370 million paid market report with 14.9 percent growth is not used. Mode 3 percent: Gen 8.6 lines at Samsung Display and BOE add mask area but jigs limit unit growth. Low minus 3 percent: mask free routes at Visionox and TCL CSOT spread.")
fo_i = par("MODEL_FENI_OLED_INT", "Foil mass per unit of mask demand, annual trend", -0.020, 0.0, 0.020, "per year", "team assumption", "(none, see reason)",
           "Larger Gen 8.6 glass adds mask area per jig, thinner foil removes mass. No foil gauge or kilogram per mask is published (TODO(data)).")
fo_s = par("MODEL_FENI_OLED_FMM_SHARE", "Share of OLED evaporation lines still using fine metal masks, ratio 2035 to 2025", 0.50, 0.90, 1.00, "ratio", "team assumption",
           "CO_SDC_FMM_8G6_2025 / DNP_INVAR_2024",
           "Samsung Display and BOE use FMM on Gen 8.6, Visionox and TCL CSOT pursue mask free routes, DNP does not expect an immediate switch. Low 0.5 means half of the 2025 mask based volume is displaced by 2035. No panel share data exist.")
fe_s = par("MODEL_FENI_EV_SHARE", "FeNi share of EV magnetic sensor and shielding parts, ratio 2035 to 2025", 0.50, 0.85, 1.05, "ratio", "team assumption",
           "(none, see reason)",
           "LOW EVIDENCE. Traction motors do not use FeNi. Only resolvers, sensors and shielding are in scope, where FeNi competes with electrical (silicon) steel, FeCo (Hiperco, Vacoflux), ferrite and nanocrystalline cores (Vitroperm, Finemet). The 2025 FeNi share of these parts is TODO(data), so only the change is modelled: low 0.5 (half the parts lost to nanocrystalline and FeCo), mode 0.85, high 1.05.")

# ------------------------------------------------------------------ 3. Monte Carlo


def draw_act(ind, spec):
    kind = spec[0]
    if kind == "ratio":
        return tri_ppf(u_act(ind), *spec[1:4])
    if kind == "cagr":
        return (1.0 + tri_ppf(u_act(ind), *spec[1:4])) ** H
    if kind == "two":
        near = tri_ppf(u_act(ind), *spec[1])
        g = tri_ppf(u_act(ind), *spec[2])
        return near * (1.0 + g) ** (H - 1)
    if kind == "semi":
        real = tri_ppf(u_act(ind), *spec[1])
        g = tri_ppf(u_act(ind), *spec[2])
        return semi_2031 * real * (1.0 + g) ** 4
    raise ValueError(kind)


def bt_log(ind):
    """Backtest adjustment in log terms: shift of annual growth over H years plus noise."""
    b = BT_IND[ind]
    return b["shift"] * H + b["sd"] * H * rng.standard_normal(N)


IDX = {}      # industry -> final ratio array
PATH = {}     # industry -> N x 11 array
ACTR = {}     # (industry, component) -> activity ratio


def run_industry(ind, comps, bt_key=None, extra=None, hair=None):
    ws = dirichlet({c["name"]: c["w"] for c in comps})
    btl = bt_log(bt_key or ind)
    tot = np.zeros(N)
    path = np.zeros((N, H + 1))
    for c in comps:
        a = extra[c["name"]] if extra else draw_act(ind, c["act"])
        a = a * np.exp(btl)
        if hair is not None:
            a = a * hair
        it = (1.0 + tri_ppf(u_ind(), *c["int"])) ** H
        sh = tri_ppf(u_ind(), *c["share"])
        R = a * it * sh
        ACTR[(ind, c["name"])] = a
        tot += ws[c["name"]] * R
        for t in range(H + 1):
            path[:, t] += ws[c["name"]] * R ** (t / H)
    return tot, path


for ind in ["aerospace", "energy", "electronics", "medical", "chemical", "oil_and_gas"]:
    IDX[ind], PATH[ind] = run_industry(ind, IND_COMP[ind], hair=HAIR.get(ind))

# automotive: shared car sales and electric share draws feed both sub indices
T = tri_ppf(u_act("automotive"), *t_car)
S = tri_ppf(u_act("automotive"), *s35)
th_act = T * (1 - S) / (1 - 0.25)
ev_act = T * S / 0.25
IND_COMP["automotive_thermal"] = [dict(name="Combustion and hybrid cars (turbo, exhaust, sensors)", w=1.0, act=None, int=ati, share=ats,
                                       driver="New car sales x (1 minus electric share), 2025 electric share 25 percent", src="IEA_GEVO_EV_SHARE_2025, IEA_WEO_EV_STEPS_2035, IEA_WEO_EV_CPS_2035, ACEA_CAR_REG_2025")]
IND_COMP["automotive_ev"] = [dict(name="Electric cars (motors, resolvers, sensors)", w=1.0, act=None, int=aei, share=aes,
                                  driver="New car sales x electric share, 20 million electric cars in 2025", src="IEA_GEVO_EV_SALES_2025, IEA_GEVO_EV_SHARE_2025, IEA_GEVO_ECARS_STEPS_2035")]
IDX["automotive_thermal"], PATH["automotive_thermal"] = run_industry("automotive", IND_COMP["automotive_thermal"], extra={IND_COMP["automotive_thermal"][0]["name"]: th_act}, hair=HAIR["automotive"])
IDX["automotive_ev"], PATH["automotive_ev"] = run_industry("automotive", IND_COMP["automotive_ev"], extra={IND_COMP["automotive_ev"][0]["name"]: ev_act}, hair=HAIR["automotive"])
IND_COMP["automotive"] = [dict(IND_COMP["automotive_thermal"][0], w=0.75), dict(IND_COMP["automotive_ev"][0], w=0.25)]
wa = dirichlet(dict(t=0.75, e=0.25))
IDX["automotive"] = wa["t"] * IDX["automotive_thermal"] + wa["e"] * IDX["automotive_ev"]
PATH["automotive"] = wa["t"][:, None] * PATH["automotive_thermal"] + wa["e"][:, None] * PATH["automotive_ev"]

for k in IDX:
    IDX[k] = IDX[k] * 100.0
    PATH[k] = PATH[k] * 100.0

ORDER = ["aerospace", "energy", "electronics", "medical", "chemical", "oil_and_gas", "automotive"]

# product families
FAMIDX = {}
FAMWS = {}
# FeNi components (own random stream, activity correlated with the electronics and automotive factors)


def _u_new(ind):
    e = rng_new.standard_normal(N)
    return phi(math.sqrt(RHO_GLOBAL) * Z0 + math.sqrt(RHO_IND) * ZI[ind] + math.sqrt(1 - RHO_GLOBAL - RHO_IND) * e)


_be, _ba = BT_IND["electronics"], BT_IND["automotive"]
FENI_C = {}
FENI_C["oled"] = (1 + tri_ppf(_u_new("electronics"), *fo_g)) ** H * (1 + tri_ppf(rng_new.random(N), *fo_i)) ** H * tri_ppf(rng_new.random(N), *fo_s) \
    * np.exp(_be["sd"] * H * rng_new.standard_normal(N)) * 100.0
FENI_C["ev_sensor"] = ev_act * HAIR["automotive"] * (1 + tri_ppf(rng_new.random(N), *aei)) ** H * tri_ppf(rng_new.random(N), *fe_s) \
    * np.exp(_ba["sd"] * H * rng_new.standard_normal(N)) * 100.0
FENI_C["leadframe"] = (1 + tri_ppf(_u_new("electronics"), *l2)) ** H * (1 + tri_ppf(rng_new.random(N), *eli)) ** H * tri_ppf(rng_new.random(N), *els) \
    * np.exp(_be["sd"] * H * rng_new.standard_normal(N)) * 100.0
for fam, spec in FAM.items():
    if fam == FENI:
        ws = dirichlet(spec["w"], conc=spec["conc"], gen=rng_new)
        FAMIDX[fam] = sum(ws[k] * FENI_C[k] for k in spec["w"])
        w2 = dirichlet(dict(oled=0.40 / 0.75, leadframe=0.35 / 0.75), conc=spec["conc"], gen=rng_new)
        FENI_ELEC = w2["oled"] * FENI_C["oled"] + w2["leadframe"] * FENI_C["leadframe"]
        FAMWS[fam] = ws
        continue
    ws = dirichlet(spec["w"])
    FAMWS[fam] = ws
    FAMIDX[fam] = sum(ws[k] * IDX[k] for k in spec["w"])

# metals
ni_c = tri_ppf(u_ind(), *NI_CONT)
co_c_aero = tri_ppf(u_ind(), *CO_CONT_AERO)
co_c_oth = tri_ppf(u_ind(), *CO_CONT_OTH)
ti_r = tri_ppf(u_ind(), *TI_AERO)

new_eng = ACTR[("aerospace", "New engine output")]
ti_idx = 100 * new_eng * ti_r
dc_act = dc_2030 * (1 + tri_ppf(u_act("electronics"), *DC_EXT)) ** 5 * np.exp(bt_log("electronics"))
cu_idx = 100 * dc_act * (1 + tri_ppf(u_ind(), *CU_INT)) ** H

CO_AERO_BASE = 11499.0
CO_SUPER_NONAV = float(co_super_nonav)
co_aero_t = CO_AERO_BASE * IDX["aerospace"] / 100.0 * co_c_aero
co_energy_t = CO_SUPER_NONAV * IDX["energy"] / 100.0 * co_c_oth

# ------------------------------------------------------------------ 4. calibration

CAL = []
sup35 = (co_aero_t + co_energy_t) / 1000.0
p50 = np.percentile(sup35, 50)
implied_rest = (181.0 - sup35) / (169.0 - 20.0)
CAL.append(dict(check="Cobalt in superalloys 2025: aviation plus non aviation equals Cobalt Institute total", anchor="20.0 kt (CI 2025)",
                model="11.499 + 8.501 = 20.000 kt (non aviation derived as the remainder)", diff="0.0", comment="Aviation 11,499 t is measured, non aviation is derived and mapped to the energy index. [AERO_CI_AVIATION_CO_2025, AERO_CI_SUPERALLOY_CO_2025]"))
CAL.append(dict(check="USGS US cobalt in superalloys versus world superalloy cobalt", anchor="51 percent of 8,000 t = 4,080 t",
                model="20.4 percent of world 20 kt", diff="", comment="Plausible US share for the engine heartland. Cross check only. [AERO_USGS_CO_SUPER_SHARE]"))
CAL.append(dict(check="IEA cobalt other uses 2025 to 2035: superalloy part of the 181 kt", anchor="169 kt (2025), 181 kt (2035)",
                model=f"Model superalloy cobalt 2035 P10/P50/P90 = {pct(sup35)[0]:.1f}/{p50:.1f}/{pct(sup35)[2]:.1f} kt",
                diff=f"Implied CAGR of the other 149 kt: P10/P50/P90 = {100*cagr(149,181-pct(sup35)[2],10):.2f}/{100*cagr(149,181-p50,10):.2f}/{100*cagr(149,181-pct(sup35)[0],10):.2f} percent",
                comment="The IEA total leaves room for the modelled superalloy growth only if non superalloy cobalt uses (carbides, catalysts, magnets, consumer batteries) are about flat. [IEA_CM_CO_DEMAND_2025_2035]"))
HI_FAM = max(float(np.percentile(v, 50)) for v in FAMIDX.values())
for s in (0.03, 0.05, 0.10):
    CAL.append(dict(check=f"IEA nickel other uses 2,906 to 3,255 kt: remainder growth if high performance alloys are {int(s*100)} percent of it",
                    anchor="2,906 kt (2025), 3,255 kt (2035), +12.0 percent",
                    model="Highest product family P50 index (most demanding case) = " + f"{HI_FAM:.0f}",
                    diff="Remainder (stainless and other) growth = " + f"{100*((3255-s*2906*HI_FAM/100)/(2906*(1-s))-1):.1f} percent over ten years",
                    comment="TODO(data): the high performance alloy share of nickel outside energy technologies is not published, so nickel is reported as an index. [IEA_CM_NI_OTHER_2025_2035]"))

# ------------------------------------------------------------------ 5. supply overlay

sup = rd("iea_critical_minerals_supply_2026.csv")
dem = rd("iea_critical_minerals_demand_2026.csv")


def sv(stage, country, year):
    r = sup[(sup.mineral_stage == stage) & (sup.country == country) & (sup.year == year)]
    return float(r.kt.iloc[0])


def dv(mineral, scen, year, item="Total demand"):
    r = dem[(dem.mineral == mineral) & (dem.scenario == scen) & (dem.year == year) & (dem["item"] == item)]
    return float(r.kt.iloc[0])


OV = []


def ov(metal, case, stage, demand_kt, supply_kt, note, src, scen="Stated Policies", stress=""):
    gap = demand_kt - supply_kt
    OV.append(dict(metal=metal, case=case, demand_scenario=scen, demand_2035_kt=round(demand_kt, 1), supply_stage=stage, supply_2035_kt=round(supply_kt, 1),
                   gap_kt=round(gap, 1), gap_pct_of_demand=round(100 * gap / demand_kt, 1), stress_assumption=stress, note=note, sources=src))


co_dem = {s: dv("Cobalt", s, 2035) for s in ("Current Policies", "Stated Policies", "High Demand")}
co_mine, co_ref = sv("Cobalt - Mining", "Total", 2035), sv("Cobalt - Refining", "Total clean technologies", 2035)
co_drc = sv("Cobalt - Mining", "Democratic Republic of Congo", 2035)
for s, d in co_dem.items():
    ov("Cobalt", "Base case", "Mine supply", d, co_mine, "IEA reports a gap of over 25 percent of primary requirements net of secondary supply, so this raw gap (no scrap) is larger.", "IEA_CM_CO_DEMAND_2025_2035, IEA_CM_CO_SUPPLY_2025_2035, CO_IEA_CO_GAP_2026", s)
ov("Cobalt", "Base case", "Refined supply", co_dem["Stated Policies"], co_ref, "Refining file label is 'Total clean technologies'. Refined output can exceed mine output through stocks and scrap.", "IEA_CM_CO_DEMAND_2025_2035")
quota_net = 96600 - 9600
cut1 = max(co_drc - quota_net / 1000.0, 0.0)
ov("Cobalt", "Stress: Congo quota stays at 2026 level", "Mine supply", co_dem["Stated Policies"], co_mine - cut1,
   "Exports capped at 96.6 kt a year including 9.6 kt strategic reserve, so 87.0 kt can leave. IEA base DRC mine supply in 2035 is 106 kt, so the cut is small.",
   "CO_USGS_QUOTA_2026, IEA_CM_CO_SUPPLY_2025_2035", stress=f"DRC exportable cobalt {quota_net/1000:.1f} kt versus {co_drc:.0f} kt base")
cut2 = co_drc * (1 - 31200 / 117549)
ov("Cobalt", "Stress: Congo quota tightened to CMOC entitlement ratio", "Mine supply", co_dem["Stated Policies"], co_mine - cut2,
   "CMOC 2026 entitlement is 31.2 kt against 117.5 kt output (26.5 percent). Applied to all DRC supply in 2035 as a severe case (team assumption).",
   "CO_CMOC_QUOTA_2026, CO_CMOC_COBALT_PROD_2025, CO_CI_DRC_EXPORT_2025", stress=f"DRC exportable share 26.5 percent of {co_drc:.0f} kt")

ni_dem = {s: dv("Nickel", s, 2035) for s in ("Current Policies", "Stated Policies", "High Demand")}
ni_mine, ni_ref = sv("Nickel - Mining", "Total", 2035), sv("Nickel - Refining", "Total", 2035)
ni_id = sv("Nickel - Mining", "Indonesia", 2035)
for s, d in ni_dem.items():
    ov("Nickel", "Base case", "Mine supply", d, ni_mine, "Demand includes scrap fed stainless. Supply file has primary mine and refined output only.", "IEA_CM_NI_DEMAND_2025_2035, IEA_CM_NI_SUPPLY_2025_2035", s)
ov("Nickel", "Base case", "Refined supply", ni_dem["Stated Policies"], ni_ref, "Primary refined nickel only, so the gap is an upper bound.", "IEA_CM_NI_SUPPLY_2025_2035")
for lab, cutp, why, src in [
    ("Stress: Indonesian ore quota 2026 revised level (-22 percent)", 1 - 295 / 379, "National RKAB 379 Mt in 2025, revised 2026 level 290 to 300 Mt (midpoint 295).", "ARGUS_NI_RKAB_2026, NI_RKAB_2026_REV"),
    ("Stress: Indonesian ore quota 2026 initial level (-29 percent)", 1 - 265 / 379, "Initial 2026 RKAB 260 to 270 Mt (midpoint 265) against 379 Mt.", "CO_TSINGSHAN_RKAB_NATIONAL_2026, ARGUS_NI_RKAB_2026"),
    ("Stress: Weda Bay style cut (-71 percent)", 1 - 12 / 42, "Eramet: Weda Bay initial 2026 RKAB 12 Mwmt against 42 Mwmt in 2025, ore operations stopped in June 2026. Severe case applied to all of Indonesia (team assumption).", "CO_ERAMET_WBN_RKAB_2026, CO_ERAMET_WBN_ORE_2025, CO_ERAMET_ORE_SALES_GUIDANCE_2026")]:
    ov("Nickel", lab, "Mine supply", ni_dem["Stated Policies"], ni_mine - cutp * ni_id,
       why + " Contained nickel is assumed to scale with ore tonnage (grade unchanged, team assumption). Class 1 alloy feed is mostly outside Indonesian NPI, so the first effect is price, not alloy availability.", src,
       stress=f"Indonesia mine supply {ni_id:.0f} kt cut by {100*cutp:.0f} percent")

cu_dem = {s: dv("Copper", s, 2035) for s in ("Current Policies", "Stated Policies", "High Demand")}
cu_mine, cu_ref = sv("Copper - Mining", "Total", 2035), sv("Copper - Refining", "Total", 2035)
for s, d in cu_dem.items():
    ov("Copper", "Base case", "Mine supply", d, cu_mine, "IEA reports a deficit of 25 percent of demand in 2035, net of secondary supply. The raw gap here is larger by the scrap share.", "IEA_CM_CU_BALANCE_2025_2035, IEA_CMO_2026", s)
ov("Copper", "Base case", "Refined supply", cu_dem["Stated Policies"], cu_ref, "Refined output includes secondary refining.", "IEA_CM_CU_BALANCE_2025_2035")
OV.append(dict(metal="Tungsten", case="Stress: Chinese export licence halt (qualitative)", demand_scenario="n/a", demand_2035_kt="TODO(data)", supply_stage="Mine supply 2025",
               supply_2035_kt="TODO(data)", gap_kt="", gap_pct_of_demand="",
               stress_assumption="Ex China mine supply 2025 = 85,000 t minus 67,000 t = 18,000 t contained tungsten (21 percent of world), a floor for supply outside China if licences stop (derived from USGS)",
               note="No IEA tonnage for tungsten to 2035. China licence on APT, oxide and unsintered carbide since 4 February 2025, mining quota first batch 58,000 t concentrate (29,896 t W, team estimate). Sintered carbide inserts and wire were left outside the licence.",
               sources="USGS_MCS2026_TUNGSTEN, W_QUOTA_CN_2025_BATCH1, W_QUOTA_CN_2025_BATCH1_W"))
# implied secondary supply that reconciles the raw gap with the IEA published gap
sec_cu = (cu_dem["Stated Policies"] - cu_mine) / cu_dem["Stated Policies"] - 0.25
sec_co = (co_dem["Stated Policies"] - co_mine) / co_dem["Stated Policies"] - 0.25
for r in OV:
    if r["metal"] == "Cobalt" and r["supply_stage"] == "Mine supply" and r["demand_scenario"] == "Stated Policies":
        r["alloy_note"] = f"Model superalloy cobalt P50 {p50:.1f} kt is {100*p50/r['supply_2035_kt']:.0f} percent of this supply"

# ------------------------------------------------------------------ 6. tier 2 register

h2 = rd("iea_h2_electrolysis_projects_june2026.csv")
op_gw = h2[h2.status == "Operational"].capacity_mwel.sum() / 1000.0
fid_gw = h2[h2.status == "FID/Construction"].capacity_mwel.sum() / 1000.0
T2 = [
    ("Electrolyser nickel (alkaline stacks, strip, wire, mesh)", "Nickel", "Strip, wire, woven and expanded mesh", "8 to 9 (team estimate)", "measured (capacity) / early signal (orders)", "2026 to 2028",
     f"IEA database June 2026: {op_gw:.1f} GW operational, {fid_gw:.1f} GW at FID or construction, 60 percent alkaline. Signpost: thyssenkrupp nucera green hydrogen orders recover above EUR 356 million (fiscal 2024/25: EUR 26 million) and FID rate rises above 0.8 Mt/year.",
     "IEA_H2DB_ELECTROLYSIS_STATUS_2026, IEA_H2DB_ALK_SHARE_2026, EE_H2_ELEC_GW_2025, EE_H2_COMMIT_2030, research/sectors/energy_environment.md"),
    ("Solid oxide interconnect strip (fuel cells)", "Chromium (ferritic steel), nickel coatings", "Coated ferritic strip", "9 for fuel cells, 5 to 6 for electrolysis (team estimate)", "early signal", "2026 to 2028",
     "Bloom Energy revenue USD 2,024 m in 2025, Fremont capacity 1 GW to 2 GW by end 2026. Interconnect is ferritic chromium steel, grade and mill not named. Nucera dropped solid oxide electrolyser mass production in August 2026. Signpost: named strip contract or second source qualification at Bloom.",
     "research/sectors/energy_environment.md, research/companies/bloom.md, research/companies/tk-nucera.md"),
    ("SMR cladding and steam generator tubing", "Zirconium, nickel (Alloy 690)", "Cladding tube, steam generator tube, bar and hollows", "7 to 8 (team estimate, Darlington SMR-1 under construction)", "early signal", "2030 to 2033",
     "WEO 2025: agreements and expressions of interest for 30 GW of small reactors, mainly for data centres. Westinghouse AP300 four unit programme, AP1000 pipeline up to 91 reactors. Expressions of interest are not tube orders. Signpost: first serial tube order after a construction licence.",
     "EE_NUC_WNA_UC, CO_WESTINGHOUSE_AP300_2025, CO_WESTINGHOUSE_PIPE_2026, research/sectors/energy_environment.md"),
    ("Captive powder metallurgy disc powder (René 88DT, René 104, ME3 type, Pratt in house powder)", "Nickel", "Atomised superalloy powder for HIP and forged discs", "9 (established, in production for decades; team estimate from the report review)", "measured (production fact), volume captive and unpublished", "in production",
     "Established route, not an emerging option. RTX states that Pratt qualifies its own powder metal sources and that the geared turbofan powder metal contamination issue costs about USD 0.7 billion in 2026 with incremental shop visits (CO_RTX_POWDER_2025, CO_RTX_9M26_BACKLOG). Treated as tier 1, inside the superalloy bar, billet and remelt stock family, and closed to outsiders (captive). Disc powder tonnes: TODO(data).",
     "research/companies/rtx.md, research/sectors/aerospace.md, CO_RTX_POWDER_2025"),
    ("AM powder, CoCr and nickel superalloy (open market)", "Cobalt, nickel", "Atomised CoCr and nickel superalloy powder for powder bed fusion", "9 for serial parts (team estimate)", "measured at industry level, crowded", "in production",
     "Not tier 2. The AM industry revenue was USD 21.8 bn in 2024 across all materials (Wohlers), Carpenter powder and additive earns 7.9 percent operating margin against 27.7 percent in premium alloys, and Hoganas, Sandvik Osprey, Oerlikon, Carpenter Additive and Chinese producers compete. The LEAP fuel nozzle tip is reported to be printed in CoCr and in serial production since about 2016 (stated in an industry review, not sourced). TODO(data): no source for the nozzle in research/, so it is not asserted as fact. Scored in Table 16 with competition 2.",
     "WOHLERS_2025, research/sectors/aerospace.md, research/companies/carpenter.md, research/companies/hoganas.md"),
    ("Newly specified AM hot section parts beyond serial parts (combustors, turbine vanes, repair)", "Nickel, cobalt", "Atomised superalloy powder", "6 to 8 (team estimate)", "early signal", "2027 to 2030",
     "Only genuinely new printed hot section parts remain here. Signpost: a named disc or hot section additive specification with a volume call in an engine programme. No such specification is logged in the repository (TODO(data)).",
     "TODO(data), research/sectors/aerospace.md"),
    ("Hydrogen fuelled gas turbines", "Nickel (cobalt)", "Castings and forgings, combustor sheet", "5 to 7 (team estimate)", "speculative", "2030 to 2035",
     "No hydrogen turbine order or alloy requirement is logged in the repository. TODO(data): searched research/ for hydrogen turbine, hydrogen fuel and hydrogen fired, found only the hydrogen supply side. Signpost: first firm order of a hydrogen capable turbine with a committed hydrogen supply contract.",
     "TODO(data), research/sectors/energy_environment.md (committed low emissions hydrogen 4.3 Mt by 2030)"),
    ("Supercritical CO2 recuperators", "Nickel", "Plate, sheet and strip for compact heat exchangers (grade TODO(data))", "5 to 6 (team estimate)", "speculative", "2032 to 2035",
     "No evidence in research notes. TODO(data): searched research/ and sections/ for sCO2 and supercritical, only the framework chapter names it. Signpost: a pilot plant above 10 MW electric with a named alloy plate supplier.", "TODO(data)"),
    ("Molten salt reactor vessels and piping", "Nickel, molybdenum", "Plate and tube in nickel molybdenum chromium alloy (grade TODO(data))", "3 to 5 (team estimate)", "speculative", "2035 or later",
     "No evidence in research notes beyond the framework chapter. Signpost: a construction permit for a demonstration plant and an ASME code case for the alloy.", "TODO(data)"),
    ("Fusion magnet HTS substrate tape (Alloy C-276)", "Nickel, molybdenum, chromium", "Cold rolled foil, 30 to 100 micrometre class (team estimate)", "4 to 6 (team estimate)", "speculative", "2030 to 2035",
     "Not found in repository: western-superconducting.md covers superconducting wire revenue (RMB 1.599 bn, +22.7 percent) but names no substrate alloy. TODO(data): substrate foil specification and tape makers. Signpost: a first magnet order for a pilot plant.",
     "TODO(data), research/companies/western-superconducting.md"),
    ("Superhot and enhanced geothermal casing", "Nickel", "Tube and clad pipe", "4 to 6 (team estimate)", "speculative", "2032 to 2035",
     "BUTTING lists geothermal as an application on its website (research/_cache) but no alloy tonnage or project is logged. TODO(data). Signpost: a drilled well above 400 degrees Celsius with a published casing alloy.", "TODO(data)"),
    ("Liquid hydrogen aircraft tanks and cryogenic lines", "Aluminium, nickel (austenitic)", "Sheet and tube", "3 to 4 (team estimate)", "speculative", "2038 or later",
     "No evidence in the repository. Airbus GMF 2026 gives no hydrogen aircraft date. TODO(data). Signpost: an airframer programme launch date.", "TODO(data)"),
    ("Data centre power: 800 VDC busbar (copper intensity down)", "Copper", "Busbar and strip", "6 to 7 (team estimate)", "early signal", "2027",
     "NVIDIA 800 VDC for Kyber racks in 2027, up to 200 kg copper busbar per 1 MW rack at 54 VDC, 45 percent copper reduction at row level (single source). A negative option for copper volume, listed because it changes the electronics index. Signpost: Eaton, Schneider and Vertiv busbar product launches.",
     "NVDA_800VDC, NVDA_800VDC_GW, NVDA_800VDC_ROWCUT, CO_VERTIV_COPPERHEDGE_2026"),
]

# ------------------------------------------------------------------ 7. write result tables

LAB = {"aerospace": "Aerospace", "energy": "Energy and environmental technology", "electronics": "Electronics and electrical engineering",
       "medical": "Medical technology", "chemical": "Chemical processing", "oil_and_gas": "Oil and gas", "automotive": "Automotive",
       "automotive_thermal": "Automotive, combustion and hybrid parts", "automotive_ev": "Automotive, electric vehicle parts"}
FENI_LAB = {"oled": "OLED fine metal mask foil", "ev_sensor": "EV magnetic sensor and shielding", "leadframe": "Lead frames and glass seals (FeNi42)"}
PRIOR = {"aerospace": 4.5, "energy": 4.0, "electronics": 3.0, "medical": 2.5, "chemical": 1.0, "oil_and_gas": 0.5, "automotive": -1.5}


def drv_text(ind):
    return " + ".join(f"{c['driver']} (weight {c['w']:.2f})" for c in IND_COMP[ind])


def int_text(ind):
    seen = []
    for c in IND_COMP[ind]:
        t = f"{c['int'][0]*100:.1f}/{c['int'][1]*100:.1f}/{c['int'][2]*100:.1f} percent a year"
        if t not in seen:
            seen.append(t)
    return "Alloy mass per unit of activity, low/mode/high " + " and ".join(seen) + ". Team assumption, no published kilogram per unit."


def share_text(ind):
    seen = []
    for c in IND_COMP[ind]:
        t = f"{c['share'][0]:.2f}/{c['share'][1]:.2f}/{c['share'][2]:.2f}"
        if t not in seen:
            seen.append(t)
    return "Share of units using a high performance alloy, ratio 2035 to 2025, low/mode/high " + " and ".join(seen) + ". Team assumption."


def act_range(ind):
    out = []
    for c in IND_COMP[ind]:
        a = ACTR.get((("automotive" if ind.startswith("automotive") else ind), c["name"]))
        if a is not None:
            q = pct(a)
            out.append(f"{c['name']}: {q[0]:.2f}/{q[1]:.2f}/{q[2]:.2f}")
    return " | ".join(out)


def sg(x):
    return f"{round(x, 2) + 0.0:+.2f}"


def bt_text(ind):
    b = BT_IND["automotive" if ind.startswith("automotive") else ind]
    return (f"Annual growth shift {sg(b['shift']*100)} pp (trend shift {sg(b['shift_old']*100)} pp, not applied), extra sd {b['sd']*100:.2f} pp a year "
            f"({b['n_real']} real and {b['n']-b['n_real']} nominal backtest series)")


ROWS = []


def _key(ind):
    return "automotive" if ind.startswith("automotive") else ind


def _p50v(ind, arr, scale, kind):
    """P50 of an industry result under three treatments. Base = no trend shift, with optimism haircut.
    noshift / nohair = no trend shift and no haircut (pure guidance). oldshift = trend shift on, no haircut (not used)."""
    if not (ind in LAB and ind in IDX):
        return ""
    k = _key(ind)
    hv = HAIR.get(k, np.ones(N))
    x = arr * scale / hv
    if kind == "oldshift":
        x = x * math.exp(BT_IND[k]["shift_old"] * H)
    return round(float(np.median(x)), 1)


def _hmed(ind):
    return round(float(np.median(HAIR.get(_key(ind), np.ones(N)))), 3) if ind in LAB else ""


def row(level, ind, metal, unit, base, arr, scale, drv, intens, share_, anchor, evidence, src, note=""):
    q = pct(arr * scale)
    qi = pct(arr)
    ROWS.append(dict(level=level, industry=LAB.get(ind, ind), metal=metal, unit=unit, base_2025=base, p10_2035=round(q[0], 1), p50_2035=round(q[1], 1), p90_2035=round(q[2], 1),
                     index_p10=round(qi[0], 0), index_p50=round(qi[1], 0), index_p90=round(qi[2], 0),
                     p50_2035_without_backtest_shift=(_p50v(ind, arr, scale, "noshift") if level.startswith("industry") else ""), p50_2035_with_trend_shift_not_used=(_p50v(ind, arr, scale, "oldshift") if level.startswith("industry") else ""),
                     haircut_median=(_hmed(ind) if level.startswith("industry") else ""),
                     activity_driver=drv, activity_ratio_p10_p50_p90=act_range(ind) if level == "industry" else "",
                     intensity_assumption_and_trend=intens, alloy_share_assumption=share_, backtest_adjustment=bt_text(ind) if level == "industry" else "",
                     calibration_anchor=anchor, evidence=evidence, sources=src, note=note))


for ind in ORDER:
    for metal in ("nickel", "cobalt"):
        arr = IDX[ind]
        sc = ni_c if metal == "nickel" else (co_c_aero if ind == "aerospace" else co_c_oth)
        arr2 = arr * sc
        if metal == "cobalt" and ind == "aerospace":
            row("industry", ind, "cobalt", "t Co (contained)", 11499, arr2, CO_AERO_BASE / 100.0, drv_text(ind), int_text(ind), share_text(ind),
                "Cobalt Institute aviation cobalt 11,499 t (2025)", "measured base, modelled 2035", "AERO_CI_AVIATION_CO_2025, AERO_CI_SUPERALLOY_CO_2025, " + IND_COMP[ind][0]["src"],
                "Cobalt content ratio 0.92/1.00/1.04 applied.")
            continue
        if metal == "cobalt" and ind == "energy":
            row("industry", ind, "cobalt", "t Co (contained), non aviation superalloys", round(CO_SUPER_NONAV), arr2, CO_SUPER_NONAV / 100.0, drv_text(ind), int_text(ind), share_text(ind),
                "Cobalt Institute superalloys 20 kt minus aviation 11,499 t (derived)", "derived base, modelled 2035", "AERO_CI_SUPERALLOY_CO_2025, AERO_CI_AVIATION_CO_2025, " + IND_COMP[ind][0]["src"],
                "Non aviation superalloy cobalt is mapped to the energy index (industrial gas turbines). Other non aviation use is unallocated.")
            continue
        if metal == "nickel":
            anchor = "Index only. IEA nickel outside energy technologies 2,906 kt (2025) to 3,255 kt (2035) is the envelope. TODO(data): high performance alloy tonnes"
            ev = "index (tonnage not published)"
        else:
            anchor = "Index only. No cobalt tonnage by this industry in the repository"
            ev = "index (tonnage not published)"
        row("industry", ind, metal, "index 2025 = 100 (alloy demand)", 100, arr2, 1.0, drv_text(ind), int_text(ind), share_text(ind), anchor, ev, "IEA_CM_NI_OTHER_2025_2035, " + IND_COMP[ind][0]["src"] if metal == "nickel" else IND_COMP[ind][0]["src"],
            "Nickel content ratio 0.98/1.00/1.02 applied." if metal == "nickel" else "Cobalt content ratio 0.90/1.00/1.03 applied.")
for ind in ("automotive_thermal", "automotive_ev"):
    row("industry sub index", ind, "nickel", "index 2025 = 100 (alloy demand)", 100, IDX[ind] * ni_c, 1.0, drv_text(ind), int_text(ind), share_text(ind),
        "Index only", "index (tonnage not published)", IND_COMP[ind][0]["src"], "Feeds precision FeNi (electric vehicle part) and the combustion families.")
row("industry", "aerospace", "titanium", "index 2025 = 100 (airframe and engine titanium)", 100, ti_idx, 1.0, "New engine and aircraft output, titanium intensity ratio 1.00/1.08/1.20", "Titanium per new aircraft rises with new generation share (39 to 82 percent)", "n/a",
    "Index only", "index (tonnage not published)", "AERO_AIRBUS_GMF2026_NEWGEN_2035, AERO_USGS_TI_SPONGE_IMPORT_2025", "Low confidence, single driver.")
row("industry", "electronics", "copper", "index 2025 = 100 (data centre power copper)", 100, cu_idx, 1.0, "IEA data centre electricity 415 TWh (2024) to 945 TWh (2030), extended at 3/6/10 percent to 2035", "Copper per TWh -4/-2/0 percent a year (800 VDC)", "n/a",
    "Index only", "index (tonnage not published)", "EE_IEA_DATACENTRE_TWH_2030, NVDA_800VDC, NVDA_800VDC_ROWCUT", "Low confidence, driver is a power forecast, not copper tonnes. Copper is not a nickel alloy.")
for fam, spec in FAM.items():
    arr = FAMIDX[fam]
    wtxt = ", ".join(f"{LAB.get(k, FENI_LAB.get(k, k))} {v:.3f}" for k, v in spec["w"].items())
    ROWS.append(dict(level="product_family", industry=fam, metal="nickel and cobalt alloy index", unit="index 2025 = 100", base_2025=100,
                     p10_2035=round(pct(arr)[0], 1), p50_2035=round(pct(arr)[1], 1), p90_2035=round(pct(arr)[2], 1), index_p10=round(pct(arr)[0], 0), index_p50=round(pct(arr)[1], 0),
                     index_p90=round(pct(arr)[2], 0), activity_driver="Weighted industry indices: " + wtxt, activity_ratio_p10_p50_p90="", intensity_assumption_and_trend="Inherited from industry indices",
                     alloy_share_assumption="Inherited from industry indices", backtest_adjustment="Inherited", calibration_anchor="Aerospace weight in family 1 = 11,499/20,000 t cobalt (measured)" if fam.startswith("Superalloy") else "Weights are team assumptions",
                     evidence="index (weights are team assumptions)", sources=spec["src"], note=spec["why"]))
_q = pct(FENI_ELEC)
ROWS.append(dict(level="product_family_variant", industry="Precision FeNi strip and foil, electronics only variant (OLED mask foil 0.533, lead frames and seals 0.467, no EV)", metal="nickel and cobalt alloy index",
                 unit="index 2025 = 100", base_2025=100, p10_2035=round(_q[0], 1), p50_2035=round(_q[1], 1), p90_2035=round(_q[2], 1), index_p10=round(_q[0], 0), index_p50=round(_q[1], 0),
                 index_p90=round(_q[2], 0), activity_driver="OLED fine metal mask foil 0.533, lead frames and glass seals 0.467", evidence="index (weights are team assumptions)",
                 sources=FAM[FENI]["src"], note="Requested variant without the EV component. Low evidence."))
for _k, _lab in FENI_LAB.items():
    _q = pct(FENI_C[_k])
    ROWS.append(dict(level="feni_component", industry=_lab, metal="iron nickel alloy index", unit="index 2025 = 100", base_2025=100, p10_2035=round(_q[0], 1), p50_2035=round(_q[1], 1),
                     p90_2035=round(_q[2], 1), index_p10=round(_q[0], 0), index_p50=round(_q[1], 0), index_p90=round(_q[2], 0), activity_driver="see MODEL_FENI_* and MODEL_EL_COMP_G / MODEL_AU_CARS_R parameters",
                     evidence="index (low evidence)", sources=FAM[FENI]["src"], note="Component of the FeNi family before weighting."))
t1 = pd.DataFrame(ROWS)
_rev = {v: k for k, v in LAB.items()}
t1["prior_team_workbook_base_2035_index"] = [
    (round(100 * (1 + PRIOR[_rev[r.industry]] / 100) ** 10) if (r.level == "industry" and r.metal == "nickel" and r.industry in _rev and _rev[r.industry] in PRIOR) else np.nan)
    for r in t1.itertuples()]
t1.to_csv(os.path.join(CLEAN, "model_tier1_results.csv"), index=False)

# ------------------------------------------------------------------ 7b. tonnes, shocks, severe aerospace case, scoring inputs
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scoring  # noqa: E402

rt = np.random.default_rng(SEED + 3)


def tdraw(spec):
    return tri_ppf(rt.random(N), *spec)


T_CO = par("MODEL_TON_CO_CONTENT", "Average virgin cobalt content of superalloy melt, mass share", 0.04, 0.08, 0.15, "mass share", "team assumption", "AERO_CI_SUPERALLOY_CO_2025",
           "TODO(data): no cobalt weighted average of world superalloy output is in the repository. Range logic: Alloy 718 and 625, the largest tonnage grades, carry no or little cobalt, wrought alloys such as 720Li and Waspaloy 13 to 15 percent, cast alloys 5 to 10 percent, cobalt base alloys about 40 to 60 percent. Revert (scrap) is not virgin cobalt, which lowers the content again. Wide on purpose.")
T_FORM = par("MODEL_TON_SUPER_FORM_SHARE", "Share of superalloy melt that leaves the mill as bar, billet or remelt stock (rest sheet, strip, tube, powder)", 0.75, 0.85, 0.95, "share", "team assumption",
             "AERO_ATI_JETENG_2025", "Superalloy melt is cast into ingot, remelt stock and billet before forging, casting or rolling. Flat and tube forms are the minority. No split is published (TODO(data)).")
T_EU = par("MODEL_TON_EU_SHARE", "EU27 share of world apparent consumption of nickel and nickel alloy mill products", 0.12, 0.20, 0.30, "share", "team assumption",
           "NI_WS_MELT_2025 / NI_INSG_USE_2025",
           "EU27 is 8.8 percent of world stainless melt (5.659 of 64.157 Mt) and Asia is 87.7 percent of primary nickel use, but specialty alloys concentrate in the EU, the United States and Japan. Range 12 to 30 percent, mode 20 percent. No world apparent consumption of nickel mill products exists (TODO(data)).")
T_BAR = par("MODEL_TON_BAR_MULT", "World nickel bar, rod and wire output as multiple of the traded floor (exports of eight reporters 2024)", 1.0, 1.5, 2.5, "ratio", "team assumption",
            "COMTRADE_750512_750522_750712_2023_2024 / COMTRADE_7505_2019_2024 / AC_EU_NI_BAR_2024",
            "The PRODCOM production cell for EU bar is confidential (rounded 2.5 kt), so the EU method fails. Floor = 2024 exports of eight reporters (re-exports are counted twice, so it is not a strict floor). Multiplier covers production that does not cross a border (China, United States domestic).")

ac = pd.read_csv(os.path.join(CLEAN, "apparent_consumption_prodcom_2019-2024.csv"))


def eu_kt(code):
    r = ac[(ac["product"].astype(str) == code) & (ac.reporter == "EU27_2020") & (ac.year == 2024)].iloc[0]
    return float(r.apparent_consumption_qty) / 1e6


def floor_kt(hs):
    d = pd.read_csv(os.path.join(CLEAN, f"comtrade_{hs}_2019-2024.csv"))
    w = d[(d.partner == "World") & (d.year == 2024) & (d.flow == "Export")]
    return float(w.net_weight_kg.sum()) / 1e6


EU_BAR, EU_FLAT, EU_TUBE = eu_kt("24452100"), eu_kt("24452200"), eu_kt("24452300")
# Traded floors use the ALLOY ONLY HS 6 digit codes (750512 plus 750522, 750620, 750712), same eight reporters as the four digit files, 2024 exports.
import comtrade_hs6  # noqa: E402
_, HS6_SUMM, HS6_SHARE, HS6_MAIN = comtrade_hs6.build()
_ex24 = HS6_SHARE[(HS6_SHARE.flow == "Export") & (HS6_SHARE.year == 2024)].set_index("family")
FL_BAR, FL_FLAT, FL_TUBE = (float(_ex24.loc[k, "alloy_only_kt"]) for k in ("bar_rod_wire", "flat", "tube"))
FL4_BAR, FL4_FLAT, FL4_TUBE = floor_kt(7505), floor_kt(7506), floor_kt(7507)    # four digit totals (alloy plus pure nickel), for comparison only
c_draw, f_draw, e_draw, b_draw = tdraw(T_CO), tdraw(T_FORM), tdraw(T_EU), tdraw(T_BAR)
SUPER_ALL = 20.0 / c_draw                    # kt superalloy melt (virgin cobalt equivalent), all forms
SUPER_AERO = 11.499 / c_draw
TON = {
    "Superalloy bar, billet and remelt stock": SUPER_ALL * f_draw,
    "Nickel alloy bar, rod and wire (long products)": FL_BAR * b_draw,
    "Flat products (plate, sheet, strip, foil)": EU_FLAT / e_draw,
    "Tubes and fittings": EU_TUBE / e_draw,
}
TON_METHOD = {
    "Superalloy bar, billet and remelt stock": "20.0 kt cobalt in superalloys (Cobalt Institute) divided by virgin cobalt content 4/8/15 percent, times 75/85/95 percent leaving as bar, billet or remelt stock. Melt tonnes, gross weight.",
    "Nickel alloy bar, rod and wire (long products)": f"HS 750512 plus 750522 (alloy only) exports of eight reporters 2024 = {FL_BAR:.1f} kt (traded floor; the HS 7505 total incl. pure nickel is {FL4_BAR:.1f} kt, so alloy is {100*FL_BAR/FL4_BAR:.0f} percent) times 1.0/1.5/2.5. EU27 PRODCOM apparent consumption {EU_BAR:.1f} kt is a lower bound (production cell confidential) and is not used.",
    "Flat products (plate, sheet, strip, foil)": f"EU27 apparent consumption {EU_FLAT:.1f} kt (PRODCOM 24452200, 2024) divided by EU share of world 12/20/30 percent. Nickel and nickel alloy flat, all grades: an upper bound for high performance alloy. Traded floor (HS 750620 alloy only exports of eight reporters, 2024) = {FL_FLAT:.1f} kt, {100*FL_FLAT/FL4_FLAT:.0f} percent of the HS 7506 total of {FL4_FLAT:.1f} kt.",
    "Tubes and fittings": f"EU27 apparent consumption {EU_TUBE:.1f} kt (PRODCOM 24452300, 2024) divided by EU share of world 12/20/30 percent. Traded floor (HS 750712 alloy only exports of eight reporters, 2024) = {FL_TUBE:.1f} kt, {100*FL_TUBE/FL4_TUBE:.0f} percent of the HS 7507 total of {FL4_TUBE:.1f} kt.",
}
q_super = pct(SUPER_ALL * f_draw)
TON_CHECK = {
    "Superalloy bar, billet and remelt stock": f"China reported output 64.5 kt in 2025 (demand about 66 kt, CO_BAOWU_CHINA_SUPERALLOY_2025, 2021 broker view) is {100*64.5/q_super[1]:.0f} percent of the P50. ATI Monroe fifth VIM furnace adds about 9 kt a year from 2027 (ARGUS_SUPERALLOY) = {100*9/q_super[1]:.0f} percent of the P50. A listed producer's high performance alloy melt of 83 kt (includes corrosion resistant grades) = {100*83/q_super[1]:.0f} percent of the P50, so the range is plausible only at its upper half: the cobalt method probably understates revert rich melt.",
    "Nickel alloy bar, rod and wire (long products)": "Germany alone exported 18.1 kt, the United States 31.0 kt and Italy 11.1 kt of HS 7505 in 2024 (Comtrade). INSG: stainless is just under 70 percent of 3,577 kt primary nickel use, so non stainless primary use is at most about 1,070 kt of nickel, a ceiling not a base.",
    "Flat products (plate, sheet, strip, foil)": "Germany exports 17.8 kt, the United States 12.2 kt, Japan 9.1 kt of HS 7506 in 2024. Outokumpu Avesta high nickel flat project about 13 kt is a quarter of EU apparent consumption (CO_OUTOKUMPU_HINI_CAP_2026).",
    "Tubes and fittings": "EU27 was a net exporter of nickel tubes in 2024 (16.5 kt out, 4.7 kt in, PRODCOM). Alleima and Sandvik tube capacity not in kt (TODO(data)).",
}
tonrows = []
for fam in FAM:
    if fam == FENI:
        tonrows.append(dict(product_family=fam, base_2025_kt_p10="", base_2025_kt_p50="", base_2025_kt_p90="", kt_2035_p10="", kt_2035_p50="", kt_2035_p90="",
                            index_2035_p10_p50_p90="/".join(f"{x:.0f}" for x in pct(FAMIDX[fam])), method="Not estimable. TODO(data): searched research/ and data/clean for FeNi36 or Invar foil tonnes, found none (Proterial, Aperam Imphy and VAC volumes are unpublished, Comtrade has no Invar foil code, DNP publishes no foil tonnes).",
                            cross_checks="DNP doubled mask capacity (2024) but masks are jigs, so no tonne bridge exists. Paid report USD 370 million FMM market not used.", evidence="none (market score 1)", label="team estimate, not summable"))
        continue
    a = TON[fam]
    b = pct(a)
    k = pct(a * FAMIDX[fam] / 100.0)
    tonrows.append(dict(product_family=fam, base_2025_kt_p10=round(b[0], 1), base_2025_kt_p50=round(b[1], 1), base_2025_kt_p90=round(b[2], 1),
                        kt_2035_p10=round(k[0], 1), kt_2035_p50=round(k[1], 1), kt_2035_p90=round(k[2], 1),
                        index_2035_p10_p50_p90="/".join(f"{x:.0f}" for x in pct(FAMIDX[fam])), method=TON_METHOD[fam], cross_checks=TON_CHECK[fam],
                        evidence="low (wide team assumptions, see MODEL_TON_*)" if fam.startswith(("Superalloy", "Nickel alloy bar")) else "low to medium (measured EU apparent consumption, assumed EU share)",
                        label="team estimate, not summable (families overlap and use different stages)"))
b = pct(SUPER_AERO)
tonrows.append(dict(product_family="Memo: aviation superalloy melt behind 11.499 kt aviation cobalt (cobalt method, all forms)", base_2025_kt_p10=round(b[0], 1), base_2025_kt_p50=round(b[1], 1), base_2025_kt_p90=round(b[2], 1),
                    kt_2035_p10=round(pct(SUPER_AERO * IDX["aerospace"] / 100)[0], 1), kt_2035_p50=round(pct(SUPER_AERO * IDX["aerospace"] / 100)[1], 1), kt_2035_p90=round(pct(SUPER_AERO * IDX["aerospace"] / 100)[2], 1),
                    index_2035_p10_p50_p90="/".join(f"{x:.0f}" for x in pct(IDX["aerospace"])), method="11.499 kt aviation cobalt (Cobalt Institute) divided by virgin cobalt content 4/8/15 percent, times the aerospace index.",
                    cross_checks="Part of the superalloy family, not additional.", evidence="low", label="team estimate, memo, not summable"))
tonrows.append(dict(product_family="Memo: China superalloy output 2025 (reported)", base_2025_kt_p10=64.5, base_2025_kt_p50=64.5, base_2025_kt_p90=64.5, kt_2035_p10="", kt_2035_p50="", kt_2035_p90="",
                    index_2035_p10_p50_p90="", method="Industry source quoted in the Fushun, Western Superconducting and Baowu profiles (CO_BAOWU_CHINA_SUPERALLOY_2025), demand near 66 kt, mostly lower value grades, 2021 broker view.",
                    cross_checks="Regional check only.", evidence="low (single secondary source)", label="reported, not a model output"))
pd.DataFrame(tonrows).to_csv(os.path.join(CLEAN, "model_family_tonnes.csv"), index=False)

# severe aerospace case: two years at minus 20 percent (2026, 2027), then recovery
SEV_F = 0.8 * 0.8
SEV_C = par("MODEL_SEVERE_AERO_RECOVERY", "Severe aerospace case: share of the lost level recovered by 2035", 0.0, 0.70, 1.0, "share", "team assumption", "(none, see reason)",
            "Two years at minus 20 percent (level 0.64 of the base path in 2027, motivated by 2020), then growth resumes at the base rate. 0 means the lost level is never recovered, 1 means the base path is rejoined by 2035. Mode 0.7 is a team assumption: engine OEM backlogs (Airbus 8,754 aircraft) favour recovery, supply constraints slow it. No recovery series is in the repository.")
sev_c = tdraw(SEV_C)
sev_fac = SEV_F + (1 - SEV_F) * sev_c
IDX_SEV = IDX["aerospace"] * sev_fac
famw = FAMWS["Superalloy bar, billet and remelt stock"]
FAM1 = "Superalloy bar, billet and remelt stock"
FAM1_SEV = sum(famw[k] * (IDX_SEV if k == "aerospace" else IDX[k]) for k in FAM[FAM1]["w"])
q_b, q_s = pct(IDX["aerospace"]), pct(IDX_SEV)
q_s_nocatch = pct(IDX["aerospace"] * SEV_F)
q_fam, q_fam_sev = pct(FAMIDX[FAM1]), pct(FAM1_SEV)
co_sev = pct(co_aero_t * sev_fac / 1000.0)
p_base = np.percentile(PATH["aerospace"], 50, axis=0)
fac_t = np.array([1.0, 0.8, 0.64] + [SEV_F + (1 - SEV_F) * 0.70 * (t - 2) / (H - 2) for t in range(3, H + 1)])
cum_loss = 100 * (1 - (p_base[1:] * fac_t[1:]).sum() / p_base[1:].sum())
SEV = dict(base=q_b, sev=q_s, nocatch=q_s_nocatch, fam=q_fam, fam_sev=q_fam_sev, co_sev=co_sev, cum_loss=cum_loss)

# scoring inputs
EUR_USD = 1.08
FAMW = {f: spec["w"] for f, spec in FAM.items()}


UV = dict(flat=(31.0, 47.8), tube=(26.1, 41.1), bar=(25.4, 33.4))   # EUR per kg, extra EU export and import unit values 2024 (AC_EU_NI_UNITVAL_2024)


def pool_eur(parts):
    """parts: list of (kt, weight, (uv_lo, uv_hi)) -> (lo, hi) in EUR bn"""
    lo = sum(kt * w * u[0] for kt, w, u in parts) / 1000.0
    hi = sum(kt * w * u[1] for kt, w, u in parts) / 1000.0
    return lo, hi


wf, wb, wt = FAMW["Flat products (plate, sheet, strip, foil)"], FAMW["Nickel alloy bar, rod and wire (long products)"], FAMW["Tubes and fittings"]
POOLS = {
    "turbine": ("measured_kt_co", CO_SUPER_NONAV / 1000.0, "kt Co", "Cobalt Institute 20.0 kt in superalloys minus 11.499 kt aviation (derived remainder, mapped to industrial turbines)"),
    "aviation": ("measured_kt_co", 11.499, "kt Co", "Cobalt Institute aviation cobalt 2025 (measured, Benchmark data)"),
    "feni": ("none", "none", "", "No FeNi tonnes, EUR or capacity in square metres in research/. DNP capacity doubling is a signal, not a volume"),
    "medical": ("company_end_use", round(278.4 / EUR_USD / 1000.0, 3), "EUR bn", "Carpenter medical end use sales USD 278.4 m (fiscal 2026) at 1.08 USD per EUR, bar, billet, wire and powder, mixed alloys"),
    "alloy690": ("estimated_eur_bn", None, "EUR bn", "EU tubes 9.2 kt x energy weight 0.25 x EUR 26.1 to 41.1 per kg (nuclear share unmeasured, so an upper bound)"),
    "car": ("estimated_eur_bn", None, "EUR bn", "EU flat, bar and tube apparent consumption x automotive thermal weights (0.10, 0.05, 0.05) x unit values"),
    "sour": ("estimated_eur_bn", None, "EUR bn", "EU flat 57.8 kt x oil and gas weight 0.15 plus bar x 0.25, x unit values (end use weights are team assumptions)"),
    "chemical": ("estimated_eur_bn", None, "EUR bn", "EU flat 57.8 kt x chemical weight 0.30 plus bar x 0.25, x unit values. The all end use pool of EUR 1.8 to 2.8 bn is NOT used (it covers every end use)"),
    "am_powder": ("wider_segment", round(383.0 / EUR_USD / 1000.0, 3), "EUR bn", "Carpenter PEP segment USD 383.0 m mixes titanium, powder, Dynamet and additive, no powder split. Hoganas additive share is limited and undisclosed"),
    "none": ("none", "none", "", "Signal only, no measured volume of the product"),
}
lo, hi = pool_eur([(EU_TUBE, FAMW["Tubes and fittings"]["energy"], UV["tube"])])
POOLS["alloy690"] = ("estimated_eur_bn", round((lo + hi) / 2, 3), "EUR bn", POOLS["alloy690"][3] + f". Range {lo:.2f} to {hi:.2f}")
lo, hi = pool_eur([(EU_FLAT, FAMW["Flat products (plate, sheet, strip, foil)"]["automotive_thermal"], UV["flat"]), (EU_BAR, wb["automotive_thermal"], UV["bar"]), (EU_TUBE, wt["automotive_thermal"], UV["tube"])])
POOLS["car"] = ("estimated_eur_bn", round((lo + hi) / 2, 3), "EUR bn", POOLS["car"][3] + f". Range {lo:.2f} to {hi:.2f}")
lo, hi = pool_eur([(EU_FLAT, wf["oil_and_gas"], UV["flat"]), (EU_BAR, wb["oil_and_gas"], UV["bar"])])
POOLS["sour"] = ("estimated_eur_bn", round((lo + hi) / 2, 3), "EUR bn", POOLS["sour"][3] + f". Range {lo:.2f} to {hi:.2f}")
lo_c, hi_c = pool_eur([(EU_FLAT, wf["chemical"], UV["flat"]), (EU_BAR, wb["chemical"], UV["bar"])])
POOLS["chemical"] = ("estimated_eur_bn", round((lo_c + hi_c) / 2, 3), "EUR bn", POOLS["chemical"][3] + f". Range {lo_c:.2f} to {hi_c:.2f}")
CHEM_POOL = (lo_c, hi_c)

# superalloy premium over the Table 10 style unit values (team assumption derived from one company filing)
HPA_UV = 35.809   # EUR per kg, sales per finished tonne of a listed high performance alloy producer in 2025 (TE_NI_HPA_FINISH_UV_2025), not a list price
BAR_MID = (UV["bar"][0] + UV["bar"][1]) / 2.0
PREM = par("MODEL_VALUE_SUPER_PREMIUM", "Superalloy price premium over the EU bar unit value (Table 10 style, EUR per kg)", 1.0, round(HPA_UV / BAR_MID, 2), round(HPA_UV / UV["bar"][0], 2), "ratio", "derived plus team assumption",
           "TE_NI_HPA_FINISH_UV_2025 / AC_EU_NI_UNITVAL_2024",
           f"A listed high performance alloy producer sold finished tonnes at EUR {HPA_UV:.1f} per kg in 2025 (sales divided by finished tonnes, not a list price), against EU extra EU bar unit values of EUR {UV['bar'][0]} to {UV['bar'][1]} per kg (mid {BAR_MID:.1f}). Mode: ratio to the mid value ({HPA_UV/BAR_MID:.2f}). High: ratio to the lower bar value ({HPA_UV/UV['bar'][0]:.2f}). Low 1.0: no premium over trade unit values. Remelt stock and ingot sell below bar, but no unit value for them is in the repository (TODO(data)), so the premium is applied to the whole family and the result is an indicative range.")
SUPER_FAM = "Superalloy bar, billet and remelt stock"
ENG_KT = float(pct(TON[SUPER_FAM])[1])
lo_e, hi_e = ENG_KT * FAMW[SUPER_FAM]["aerospace"] * UV["bar"][0] * PREM[0] / 1000.0, ENG_KT * FAMW[SUPER_FAM]["aerospace"] * UV["bar"][1] * PREM[2] / 1000.0
POOLS["engine_bar"] = ("estimated_eur_bn", round((lo_e + hi_e) / 2, 3), "EUR bn", f"Superalloy bar, billet and remelt stock family P50 {ENG_KT:.0f} kt (2025, team estimate, model_family_tonnes.csv) x aerospace weight {FAMW[SUPER_FAM]['aerospace']:.3f} (measured cobalt split, includes cast parts, so an upper bound for wrought bar) x EUR {UV['bar'][0]} to {UV['bar'][1]} per kg x superalloy premium {PREM[0]:.2f} to {PREM[2]:.2f}. Range {lo_e:.2f} to {hi_e:.2f}. Replaces the 11.499 kt aviation cobalt pool: Alloy 718, the lead billet grade, has no cobalt to speak of (1.00 percent maximum)")
lo_g, hi_g = pool_eur([(EU_FLAT, wf["electronics"], UV["flat"])])
# indicative EUR value per product family (team estimate), never summed: kt x EU extra EU unit values (Table 10 style), plus the superalloy premium for family 1
FAMVAL = []
for _r in tonrows:
    _f = _r["product_family"]
    if _f.startswith("Memo"):
        continue
    if _f == FENI:
        FAMVAL.append(dict(product_family=_f, note="Not estimable: no FeNi tonnes (TODO(data)) and Comtrade has no Invar foil code, so no EUR range is given.", label="team estimate, not summable"))
        continue
    _uv, _pm = (UV["bar"], PREM) if _f.startswith("Superalloy") else (UV["bar"] if _f.startswith("Nickel alloy bar") else (UV["flat"] if _f.startswith("Flat") else UV["tube"]), (1.0, 1.0, 1.0))
    _lo, _hi, _mid = _uv[0] * _pm[0], _uv[1] * _pm[2], (_uv[0] + _uv[1]) / 2.0 * _pm[1]
    _d = dict(product_family=_f, unit_value_eur_per_kg_low=round(_lo, 1), unit_value_eur_per_kg_mid=round(_mid, 1), unit_value_eur_per_kg_high=round(_hi, 1),
              premium_low_mode_high=("%.2f / %.2f / %.2f" % _pm) if _f.startswith("Superalloy") else "none (trade unit values)")
    for yr_, ks in (("2025", ("base_2025_kt_p10", "base_2025_kt_p50", "base_2025_kt_p90")), ("2035", ("kt_2035_p10", "kt_2035_p50", "kt_2035_p90"))):
        k10, k50, k90 = (float(_r[k]) for k in ks)
        _d[f"eur_bn_{yr_}_central_low"] = round(k50 * _lo / 1000.0, 2)
        _d[f"eur_bn_{yr_}_central_mid"] = round(k50 * _mid / 1000.0, 2)
        _d[f"eur_bn_{yr_}_central_high"] = round(k50 * _hi / 1000.0, 2)
        _d[f"eur_bn_{yr_}_band_p10_low_to_p90_high"] = f"{k10 * _lo / 1000.0:.2f} to {k90 * _hi / 1000.0:.2f}"
    _k50 = float(_r["base_2025_kt_p50"])
    _d["gate_1p5_kt_eur_m_low_to_high"] = f"{1.5 * _lo:.0f} to {1.5 * _hi:.0f}"
    _d["gate_1p5_kt_share_of_2025_p50_pct"] = round(100 * 1.5 / _k50, 1)
    _d["gate_3_kt_eur_m_low_to_high"] = f"{3.0 * _lo:.0f} to {3.0 * _hi:.0f}"
    _d["gate_3_kt_share_of_2025_p50_pct"] = round(100 * 3.0 / _k50, 1)
    _d["note"] = ("2025 and 2035 at constant 2024 unit values (real). Tonnes are team estimates (model_family_tonnes.csv). Unit values are EU27 extra EU import and export values (AC_EU_NI_UNITVAL_2024) and include pure nickel grades, "
                  "so the range is indicative. Central range = P50 tonnes x low to high unit value, band = P10 tonnes x low to P90 tonnes x high. Families overlap and are never summed." +
                  (" Superalloy premium over the bar unit value (MODEL_VALUE_SUPER_PREMIUM) is a team assumption. Remelt stock and ingot sell below bar, so the value is an upper indication." if _f.startswith("Superalloy") else ""))
    _d["label"] = "team estimate, not summable"
    FAMVAL.append(_d)
pd.DataFrame(FAMVAL).to_csv(os.path.join(CLEAN, "model_family_value.csv"), index=False)
POOLS["fab_gas"] = ("estimated_eur_bn", round((lo_g + hi_g) / 2, 3), "EUR bn", f"EU flat 57.8 kt x electronics weight {wf['electronics']} (team assumption) x EUR 31.0 to 47.8 per kg. Range {lo_g:.2f} to {hi_g:.2f}. Strip only: the tube weight for electronics is not assigned (TODO(data)), so the pool is a lower bound for strip plus tube")


def cg(x):
    return (float(np.percentile(x, 50)) / 100.0) ** (1.0 / H) - 1.0


def med_g(x):
    return float(np.median(x)) ** (1.0 / H) - 1.0


GROW_NH = {"energy": cg(IDX["energy"] / HAIR["energy"]), "aerospace": cg(IDX["aerospace"] / HAIR["aerospace"]), "oil_and_gas": cg(IDX["oil_and_gas"] / HAIR["oil_and_gas"]),
           "automotive_thermal": cg(IDX["automotive_thermal"] / HAIR["automotive"]),
           "nuclear": med_g(ACTR[("energy", "Nuclear tube and cladding")] / HAIR["energy"]), "aero_new": med_g(ACTR[("aerospace", "New engine output")] / HAIR["aerospace"]),
           "gas_turbine": med_g(ACTR[("energy", "Gas turbine hot section")] / HAIR["energy"]), "aero_mro": med_g(ACTR[("aerospace", "Aftermarket and engine overhaul pull")] / HAIR["aerospace"])}
GROW = {"energy": cg(IDX["energy"]), "aerospace": cg(IDX["aerospace"]), "feni": cg(FAMIDX[FENI]), "medical": cg(IDX["medical"]), "oil_and_gas": cg(IDX["oil_and_gas"]),
        "chemical": cg(IDX["chemical"]), "nuclear": float(np.median(ACTR[("energy", "Nuclear tube and cladding")])) ** (1.0 / H) - 1.0,
        "aero_new": med_g(ACTR[("aerospace", "New engine output")]), "automotive_thermal": cg(IDX["automotive_thermal"]),
        "gas_turbine": med_g(ACTR[("energy", "Gas turbine hot section")]), "aero_mro": med_g(ACTR[("aerospace", "Aftermarket and engine overhaul pull")]),
        "semi_fab": med_g(ACTR[("electronics", "Semiconductor equipment, 300 mm capacity")])}
GROW_SRC = {"energy": "Table 13 energy index", "aerospace": "Table 13 aerospace index", "feni": "Table 14 FeNi family", "medical": "Table 13 medical index",
            "oil_and_gas": "Table 13 oil and gas index", "chemical": "Table 13 chemical index", "nuclear": "Nuclear tube and cladding activity ratio (Table A1)",
            "aero_new": "Aerospace new engine output: engine delivery path, with haircut (Table A1)", "automotive_thermal": "Automotive combustion and hybrid sub index",
            "gas_turbine": "Energy gas turbine hot section output ratio, with haircut (Table A1)", "aero_mro": "Aerospace aftermarket and overhaul pull, with haircut (Table A1)",
            "semi_fab": "Semiconductor equipment 300 mm capacity path (Table A1)"}
sc_rows = [dict(kind="growth", key=k, p50_cagr=v, pool_kind="", pool_value="", unit="", note=GROW_SRC[k]) for k, v in GROW.items()]
sc_rows += [dict(kind="pool", key=k, p50_cagr="", pool_kind=v[0], pool_value=v[1], unit=v[2], note=v[3]) for k, v in POOLS.items()]
with open(os.path.join(CLEAN, "model_scoring_inputs.csv"), "w", newline="", encoding="utf-8") as fh:
    w_ = csv.DictWriter(fh, fieldnames=list(sc_rows[0].keys()))
    w_.writeheader()
    w_.writerows(sc_rows)
INP = scoring.read_inputs()
SC_BASE = scoring.score_all(INP, label="base")
scoring.write(SC_BASE)
sev_g = (float(np.percentile(IDX_SEV, 50)) / 100.0) ** (1.0 / H) - 1.0
SEV_OVER = {"aerospace": sev_g, "aero_new": med_g(ACTR[("aerospace", "New engine output")] * sev_fac), "aero_mro": med_g(ACTR[("aerospace", "Aftermarket and engine overhaul pull")] * sev_fac)}
BOEING_ONLY = OT["OT_BA_737_RATE"]    # stress: haircut fixed at the Boeing point for aerospace
BA_OVER = {"aerospace": cg(IDX["aerospace"] / HAIR["aerospace"] * BOEING_ONLY),
           "aero_new": med_g(ACTR[("aerospace", "New engine output")] / HAIR["aerospace"] * BOEING_ONLY),
           "aero_mro": med_g(ACTR[("aerospace", "Aftermarket and engine overhaul pull")] / HAIR["aerospace"] * BOEING_ONLY)}
SC_CASES = {
    "base": SC_BASE,
    "without haircut (pure guidance)": scoring.score_all(INP, growth_override=GROW_NH, label="no haircut"),
    "aerospace haircut fixed at the Boeing point (0.894)": scoring.score_all(INP, growth_override=BA_OVER, label="Boeing point"),
    "severe aerospace (2 years at -20 percent, 70 percent recovery)": scoring.score_all(INP, growth_override=SEV_OVER, label="severe aerospace"),
    "China tungsten licence halt": scoring.score_all(INP, supply_override={"tungsten": "halt"}, label="tungsten halt"),
    "Indonesia ore quota cut": scoring.score_all(INP, supply_override={"nickel": "price_only"}, label="Indonesia"),
}
# Congo tightened: a minor cobalt input drops to principal level risk (score 2), a principal cobalt input to halt level (score 1)
def congo_run():
    rows_ = []
    saved = {o["id"]: list(o["inputs"]) for o in scoring.OPPS}
    for o in scoring.OPPS:
        o["inputs"] = [(el, ("quota_principal" if rg == "quota_minor" else ("halt" if rg == "quota_principal" else rg))) if "cobalt" in el else (el, rg) for el, rg in o["inputs"]]
    rows_ = scoring.score_all(INP, label="Congo tightened")
    for o in scoring.OPPS:
        o["inputs"] = saved[o["id"]]
    return rows_


SC_CASES["Congo cobalt quota tightened"] = congo_run()


def tier_changes(case):
    base = {r["opportunity"]: r for r in SC_BASE}
    ch = [f"{r['opportunity']}: {base[r['opportunity']]['tier']} to {r['tier']} ({base[r['opportunity']]['weighted_score']:.2f} to {r['weighted_score']:.2f})"
          for r in SC_CASES[case] if r["tier"] != base[r["opportunity"]]["tier"]]
    mv = [f"{r['opportunity']} {base[r['opportunity']]['weighted_score']:.2f} to {r['weighted_score']:.2f}" for r in SC_CASES[case] if abs(r["weighted_score"] - base[r["opportunity"]]["weighted_score"]) > 1e-9]
    return ("tier changes: " + "; ".join(ch) if ch else "no tier changes") + ("; score moves: " + "; ".join(mv) if mv else "")


# supply shock table
ovdf = pd.DataFrame(OV)
def ovr(metal, case_start, scen="Stated Policies", stage="Mine supply"):
    r = ovdf[(ovdf.metal == metal) & (ovdf.case.str.startswith(case_start)) & (ovdf.demand_scenario == scen) & (ovdf.supply_stage == stage)].iloc[0]
    return r


rb, r1, r2 = ovr("Cobalt", "Base"), ovr("Cobalt", "Stress: Congo quota stays"), ovr("Cobalt", "Stress: Congo quota tightened")
n0, n1, n2, n3 = ovr("Nickel", "Base"), ovr("Nickel", "Stress: Indonesian ore quota 2026 revised"), ovr("Nickel", "Stress: Indonesian ore quota 2026 initial"), ovr("Nickel", "Stress: Weda")
w_lo, w_mid = 252.0, 380.0       # Rotterdam concentrate USD per mtu WO3, 2024 and 2025 (USGS_MCS2026_TUNGSTEN)
w_kg_t = 0.04 * 1000.0           # kg W per tonne of C-276 at 4 percent
w_mtu = w_kg_t / 7.93
c276_w_cost_24, c276_w_cost_25 = w_mtu * w_lo, w_mtu * w_mid
co_pound = 2.2046
co_lb_24, co_lb_25 = 16.77, 21.0      # US spot cathode USD per lb, 2024 and estimated 2025 (CO_USGS_CATHODE_2025)
SHOCKS = [
    dict(shock="Congo cobalt export quota (96.6 kt a year incl. 9.6 kt reserve, CMOC entitlement 31.2 kt of 117.5 kt)", affected_families="Superalloy bar, billet and remelt stock (Co bearing grades); CoCr bar and powder (Co about 60 percent)",
         gap_or_exposure=f"Mine supply 2035 {rb.supply_2035_kt:.0f} kt base, {r1.supply_2035_kt:.0f} kt with quota held (gap {r1.gap_pct_of_demand:.0f} percent of IEA Stated Policies demand, base {rb.gap_pct_of_demand:.0f}), {r2.supply_2035_kt:.0f} kt at CMOC entitlement ratio (gap {r2.gap_pct_of_demand:.0f} percent). Model superalloy cobalt 2035 P50 {p50:.1f} kt = {100*p50/rb.supply_2035_kt:.0f} percent of base supply, {100*p50/r2.supply_2035_kt:.0f} percent in the tight case. Alloy grade metal is about 15 kt a year from four refiners outside the hydroxide chain (Cobalt Institute).",
         cost_effect=f"Pass through by surcharge or alloy price, lagged, qualitative: no surcharge table is in the repository (TODO(data)). Team arithmetic: at 8 percent virgin cobalt a tonne of superalloy holds {80*co_pound:.0f} lb Co, worth USD {80*co_pound*co_lb_25:,.0f} at USD 21 per lb (2025 estimate), so the 25 percent price rise from USD 16.77 (2024) adds about USD {80*co_pound*(co_lb_25-co_lb_24):,.0f} per tonne. For CoCr (about 600 kg Co per tonne) the same move adds about USD {600*co_pound*(co_lb_25-co_lb_24):,.0f}. Fixed price long term agreements keep the risk with the melter.",
         tier_effect=tier_changes("Congo cobalt quota tightened"), src="CO_USGS_QUOTA_2026, CO_CMOC_QUOTA_2026, IEA_CM_CO_SUPPLY_2025_2035, AERO_CI_SUPERALLOY_CO_2025, CO_USGS_CATHODE_2025"),
    dict(shock="China tungsten export licence halt (licence regime since 4 February 2025, APT, oxide, unsintered carbide)", affected_families="Flat products and bar in C-276 and C-22 type grades (W about 4 and 3 percent); tungsten bearing cast and wrought superalloys (content TODO(data))",
         gap_or_exposure=f"Ex China mine supply 2025 = 85,000 t minus 67,000 t = 18,000 t contained tungsten (21 percent of world). Each 10 kt of C-276 uses 0.4 kt W = {100*0.4/18:.1f} percent of ex China mine supply. No tungsten tonnes to 2035 exist (TODO(data)), so no gap is computed. Sintered carbide and wire are outside the licence.",
         cost_effect=f"Tungsten is priced by surcharge or in the alloy price. Team arithmetic: 40 kg W per tonne of C-276 is {w_mtu:.2f} mtu WO3, which cost USD {c276_w_cost_24:,.0f} at the 2024 concentrate price (USD 252) and USD {c276_w_cost_25:,.0f} at the 2025 price (USD 380), an increase of USD {c276_w_cost_25-c276_w_cost_24:,.0f} per tonne. Another doubling would add about USD {c276_w_cost_25:,.0f} per tonne, about {100*c276_w_cost_25/32500:.1f} percent of the German export unit value of USD 32,500 per tonne for nickel flat (concentrate basis, metal costs more).",
         tier_effect=tier_changes("China tungsten licence halt"), src="USGS_MCS2026_TUNGSTEN, W_MOFCOM_2025_10, W_MOFCOM_FAQ_2025, MO_HAYNES_C276_W"),
    dict(shock="Indonesia nickel ore quota cut (RKAB 2026 revised -22 percent, initial -29 percent, Weda Bay style -71 percent)", affected_families="All nickel alloy families, first through the nickel price; class 1 alloy feed is mostly outside Indonesian NPI",
         gap_or_exposure=f"Mine supply 2035 gap {n0.gap_pct_of_demand:.1f} percent of IEA Stated Policies demand in the base case, {n1.gap_pct_of_demand:.1f} percent at -22 percent, {n2.gap_pct_of_demand:.1f} percent at -29 percent, {n3.gap_pct_of_demand:.1f} percent at -71 percent. The primary refined gap is already {ovr('Nickel','Base',stage='Refined supply').gap_pct_of_demand:.1f} percent.",
         cost_effect="Pass through by the monthly alloy surcharge on lagged LME nickel, molybdenum and chromium averages, so margin is exposed only on fixed price contracts and inventory. ATI: nickel use about 70 million lb, so USD 1.00 per lb is about USD 70 m of cost, mostly passed through (CO_ATI_SALES_2025). Team arithmetic: USD 1,000 per tonne on LME nickel adds about USD 10 per tonne of alloy for every percentage point of nickel content.",
         tier_effect=tier_changes("Indonesia ore quota cut"), src="ARGUS_NI_RKAB_2026, NI_RKAB_2026_REV, CO_ERAMET_WBN_RKAB_2026, IEA_CM_NI_SUPPLY_2025_2035, CO_ATI_SALES_2025"),
    dict(shock="Severe aerospace demand case: two years at minus 20 percent (2026 and 2027), then recovery (motivated by 2020)", affected_families="Superalloy bar, billet and remelt stock (aerospace weight 0.575), engine bar and billet",
         gap_or_exposure=f"Aerospace 2035 index P10/P50/P90: base {q_b[0]:.0f}/{q_b[1]:.0f}/{q_b[2]:.0f}. Severe with {SEV_C[1]*100:.0f} percent recovery {q_s[0]:.0f}/{q_s[1]:.0f}/{q_s[2]:.0f}, no recovery of the lost level {q_s_nocatch[0]:.0f}/{q_s_nocatch[1]:.0f}/{q_s_nocatch[2]:.0f}. Superalloy family P50 {q_fam[1]:.0f} to {q_fam_sev[1]:.0f}. Aviation cobalt 2035 P50 {pct(co_aero_t/1000.0)[1]:.1f} to {co_sev[1]:.1f} kt. Cumulative metal demand 2026 to 2035 on the P50 path is {cum_loss:.1f} percent below base.",
         cost_effect="Not a supply shock: volume loss. Mills with fixed capital in VIM and VAR lose utilisation. Backlogs (Airbus 8,754 aircraft, Boeing more than 6,300) and engine shop visits cushion the aftermarket half of the index.",
         tier_effect=tier_changes("severe aerospace (2 years at -20 percent, 70 percent recovery)"), src="MODEL_SEVERE_AERO_RECOVERY, CO_AIRBUS_DELIV_2025, CO_BA_BACKLOG_2025"),
]
# every tier change per shock, listed in full (one row per shock in model_supply_shocks.csv, one row per shock and opportunity in model_shock_tiers.csv)
SHOCK_CASE = ["Congo cobalt quota tightened", "China tungsten licence halt", "Indonesia ore quota cut", "severe aerospace (2 years at -20 percent, 70 percent recovery)"]
_base = {r["opportunity"]: r for r in SC_BASE}
shock_long = []
for sh_, ck in zip(SHOCKS, SHOCK_CASE):
    chg, mv = [], []
    for r in SC_CASES[ck]:
        b0 = _base[r["opportunity"]]
        if r["tier"] != b0["tier"]:
            chg.append(f"{r['opportunity']} {b0['tier']} to {r['tier']} ({b0['weighted_score']:.2f} to {r['weighted_score']:.2f})")
        if abs(r["weighted_score"] - b0["weighted_score"]) > 1e-9 and r["tier"] == b0["tier"]:
            mv.append(f"{r['opportunity']} {b0['weighted_score']:.2f} to {r['weighted_score']:.2f}")
        shock_long.append(dict(shock_case=ck, opportunity=r["opportunity"], row_type=r["row_type"], base_score=round(b0["weighted_score"], 3), base_tier=b0["tier"],
                               case_score=round(r["weighted_score"], 3), case_tier=r["tier"], tier_changed=r["tier"] != b0["tier"], score_change=round(r["weighted_score"] - b0["weighted_score"], 3)))
    sh_["n_tier_changes"] = len(chg)
    sh_["tier_changes_all"] = "; ".join(chg) if chg else "none"
    sh_["score_moves_without_tier_change"] = "; ".join(mv) if mv else "none"
pd.DataFrame(SHOCKS).to_csv(os.path.join(CLEAN, "model_supply_shocks.csv"), index=False)
pd.DataFrame(shock_long).to_csv(os.path.join(CLEAN, "model_shock_tiers.csv"), index=False)

# all scoring cases in one long file
_cs = []
for ck, rows_ in SC_CASES.items():
    for r in rows_:
        _cs.append(dict(case=ck, opportunity=r["opportunity"], row_type=r["row_type"], market=r["market"], growth=r["growth"], supply=r["supply"],
                        growth_p50_cagr_pct=r["growth_p50_cagr_pct"], weighted_score=r["weighted_score"], tier=r["tier"]))
pd.DataFrame(_cs).to_csv(os.path.join(CLEAN, "model_scores_cases.csv"), index=False)

# combined vacuum melt superalloy programme: engine bar plus turbine remelt, one melt shop, under all four weightings and every case
PROG = "Vacuum melt superalloy programme (engine bar and billet plus turbine remelt stock and sheet)"
_sh = [FAMW[SUPER_FAM]["aerospace"], FAMW[SUPER_FAM]["energy"]]
_lo_p, _hi_p = (ENG_KT * sum(_sh) * UV["bar"][0] * PREM[0] / 1000.0, ENG_KT * sum(_sh) * UV["bar"][1] * PREM[2] / 1000.0)
INP[("pool", "programme")] = dict(kind="pool", key="programme", pool_kind="estimated_eur_bn", pool_value=str(round((_lo_p + _hi_p) / 2, 3)), unit="EUR bn",
                                   note=f"Superalloy family P50 {ENG_KT:.0f} kt x (aerospace {_sh[0]:.3f} + energy {_sh[1]:.3f}) x EUR 25.4 to 33.4 per kg x premium. Range {_lo_p:.2f} to {_hi_p:.2f}")
prog_rows = []
for ck, rows_ in SC_CASES.items():
    for r in scoring.combine(rows_, ["Engine bar and billet", "Turbine remelt stock and sheet"], _sh, "programme", INP, PROG):
        prog_rows.append(dict(case=ck, variant="all lead grades (cobalt bearing grades included)", **r))
    for r in scoring.combine(rows_, ["Engine bar and billet, Alloy 718 only", "Turbine remelt stock and sheet"], _sh, "programme", INP, PROG + ", Alloy 718 lead grade only"):
        prog_rows.append(dict(case=ck, variant="Alloy 718 lead grade only", **r))
pd.DataFrame(prog_rows).to_csv(os.path.join(CLEAN, "model_combined_programme.csv"), index=False)
PROG_BASE = [r for r in prog_rows if r["case"] == "base" and r["variant"].startswith("all")]

# aerospace results with and without the haircut (index percentiles, engine path, scores)
AERO_CASES = []
for lab, fac, ck in [("with haircut (base, median %.2f)" % float(np.median(HAIR["aerospace"])), None, "base"), ("without haircut (pure guidance)", "none", "without haircut (pure guidance)"),
                     ("haircut fixed at the Boeing point (%.3f)" % BOEING_ONLY, "ba", "aerospace haircut fixed at the Boeing point (0.894)")]:
    h = HAIR["aerospace"]
    mult = np.ones(N) if fac is None else (1.0 / h if fac == "none" else BOEING_ONLY / h)
    qa = pct(IDX["aerospace"] * mult * ni_c)     # nickel row of Table 13 (nickel content ratio applied)
    qe = pct(ACTR[("aerospace", "New engine output")] * mult)
    qf = pct(FAMIDX[SUPER_FAM] + FAMWS[SUPER_FAM]["aerospace"] * (IDX["aerospace"] * (mult - 1.0)))
    qc = pct(co_aero_t * mult / 1000.0)
    rr = {r["opportunity"]: r for r in SC_CASES[ck]}
    pr_ = {r["weighting"]: r for r in prog_rows if r["case"] == ck and r["variant"].startswith("all")}
    AERO_CASES.append(dict(case=lab, aerospace_index_p10=round(qa[0], 1), aerospace_index_p50=round(qa[1], 1), aerospace_index_p90=round(qa[2], 1),
                           new_engine_ratio_2035_p10=round(qe[0], 3), new_engine_ratio_2035_p50=round(qe[1], 3), new_engine_ratio_2035_p90=round(qe[2], 3),
                           new_engine_growth_p50_pct=round(rr["Engine bar and billet"]["growth_p50_cagr_pct"], 2),
                           superalloy_family_index_p50=round(qf[1], 1), aviation_cobalt_2035_p50_kt=round(qc[1], 2),
                           engine_bar_growth_score=rr["Engine bar and billet"]["growth"], engine_bar_score=round(rr["Engine bar and billet"]["weighted_score"], 3), engine_bar_tier=rr["Engine bar and billet"]["tier"],
                           engine_bar_718_only_score=round(rr["Engine bar and billet, Alloy 718 only"]["weighted_score"], 3), engine_bar_718_only_tier=rr["Engine bar and billet, Alloy 718 only"]["tier"],
                           turbine_remelt_score=round(rr["Turbine remelt stock and sheet"]["weighted_score"], 3), turbine_remelt_tier=rr["Turbine remelt stock and sheet"]["tier"],
                           repair_wire_score=round(rr["Superalloy repair wire"]["weighted_score"], 3), repair_wire_tier=rr["Superalloy repair wire"]["tier"],
                           programme_score_base_weights=round(pr_["base weights (15/20/15/10/10/10/10/10)"]["score"], 3), programme_tier_base_weights=pr_["base weights (15/20/15/10/10/10/10/10)"]["tier"]))
pd.DataFrame(AERO_CASES).to_csv(os.path.join(CLEAN, "model_aerospace_haircut_cases.csv"), index=False)

# engine delivery path: evidence points and the modelled median path (index 2025 = 100)
r35 = ACTR[("aerospace", "New engine output")]
ep = []
for yr_, ser, val, unit_, src_, role in [
        (2023, "LEAP deliveries", 1570, "engines", "CO_GE_LEAP_2025", "evidence"), (2024, "LEAP deliveries", 1407, "engines", "CO_GE_LEAP_2025", "evidence"),
        (2025, "LEAP deliveries", 1802, "engines", "CO_GE_LEAP_2025 / CO_SAFRAN_LEAP_2025", "evidence, base year"),
        (2026, "LEAP deliveries, nine months", 1565, "engines", "CO_GE_9M26_DELIV", "evidence (9M 2025: 1,240)"),
        (2026, "LEAP deliveries, guidance high teens growth", round(1802 * 1.18), "engines", "CO_GE_Q2LEAP_2026", "guidance"),
        (2028, "LEAP deliveries, plan", 2600, "engines", "CO_SAFRAN_LEAP_2025", "plan (capital markets day 2024: 2,500)"),
        (2024, "Airbus deliveries", 766, "aircraft", "CO_AIRBUS_DELIV_2025", "evidence"), (2025, "Airbus deliveries", 793, "aircraft", "CO_AIRBUS_DELIV_2025", "evidence"),
        (2026, "Airbus deliveries, nine months (9M 2025: 507)", 547, "aircraft", "CO_AIRBUS_9M_2026", "evidence"), (2026, "Airbus deliveries, guidance", 870, "aircraft", "CO_AIRBUS_GUIDE_2026", "guidance"),
        (2024, "Boeing deliveries", 348, "aircraft", "CO_BA_DELIV_2025", "evidence"), (2025, "Boeing deliveries", 600, "aircraft", "CO_BA_DELIV_2025", "evidence"),
        (2026, "Boeing deliveries, nine months", 475, "aircraft", "CO_BA_Q3_2026", "evidence (search summary)"),
        (2025, "Boeing 737 rate reached in Q4", 42, "aircraft a month", "CO_BA_RATES_2025", "evidence"), (2026, "Boeing 737 rate, plan", 47, "aircraft a month", "CO_BA_RATES_2025", "plan, stable only in 2027"),
        ("2026 to 2045 average", "Airbus GMF new passenger aircraft deliveries a year", round(ENG_GMF_AVG), "aircraft", "AERO_AIRBUS_GMF2026_DELIVERIES", "official requirement"),
        ("2026 to 2045 average", "Boeing CMO new airplane deliveries a year", round(ENG_CMO_AVG), "aircraft", "BOEING_CMO_2026", "official requirement")]:
    ep.append(dict(row_type="evidence", year=yr_, series=ser, value=val, unit=unit_, source=src_, role=role))
_e26, _e28 = a2n[1], a2m[1]
_r35_med = float(np.median(r35 / HAIR["aerospace"]))   # before haircut
for yr_ in range(2025, 2036):
    if yr_ <= 2026:
        v0 = _e26 ** (yr_ - 2025)
    elif yr_ <= 2028:
        v0 = _e26 * (_e28 / _e26) ** ((yr_ - 2026) / 2.0)
    else:
        v0 = _e28 * (a2g[1] / _e28) ** ((yr_ - 2028) / 7.0)
    ep.append(dict(row_type="model median path before haircut", year=yr_, series="New engine output index (2025 = 100), modes of the anchors", value=round(100 * v0, 1), unit="index", source="MODEL_AERO_NEW_E26 / E28 / R35", role="interpolated at constant growth between anchors"))
for yr_ in range(2025, 2036):
    ep.append(dict(row_type="model median path with haircut", year=yr_, series="New engine output index (2025 = 100), median of the draws, haircut applied to the 2035 requirement", value=round(float(np.median(r35 ** ((yr_ - 2025) / H))) * 100, 1), unit="index", source="MODEL_AERO_NEW_R35, MODEL_HAIRCUT_AERO", role="constant compound growth to the 2035 draw, as in the industry index"))
pd.DataFrame(ep).to_csv(os.path.join(CLEAN, "model_engine_delivery_path.csv"), index=False)

# backtest csv
brows = []
for b in BT:
    brows.append(dict(row_type="driver_backtest", series=b["series"], industry=b["industry"], driver=b["driver"], price_basis=b["price_basis"],
                      train_window=f"{b['first']} to 2019", test_window=f"2020 to {b['last']}", n_train=b["n_train"], n_test=b["n_test"],
                      mape_pct=round(100 * b["mape"], 1), bias_pct=round(100 * b["bias"], 1), trend_growth_pct_per_year=round(100 * (math.exp(b["trend"]) - 1), 2),
                      realised_growth_2019_to_last_pct=round(100 * (math.exp(b["realised"]) - 1), 2), annual_growth_error_pp=round(100 * b["err"], 2),
                      used_to_shift=b["shift_ok"], source=b["src"], note=b["note"]))
for t in OUTLOOK_TESTS:
    brows.append(dict(row_type="outlook_vs_outcome", series=t["id"], industry=t["industry"], driver=t["what"], price_basis="n/a", train_window="n/a", test_window="outlook year", n_train="", n_test=1,
                      mape_pct=round(100 * abs(t["ratio"] - 1), 1), bias_pct=round(100 * (t["outlook"] / t["outcome"] - 1), 1) if t["id"] != "OT_LEAP_2026" else round(100 * (1.18 / 1.26 - 1), 1),
                      trend_growth_pct_per_year="", realised_growth_2019_to_last_pct="", annual_growth_error_pp="", used_to_shift=False, source=t["src"],
                      note=f"Outcome over outlook = {t['ratio']:.3f}. Used for the optimism haircut (MODEL_HAIRCUT_AERO, MODEL_HAIRCUT_OFFICIAL), not as a growth shift. {t['note']}"))
brows.append(dict(row_type="todo", series="BT_AERO_DELIVERIES", industry="aerospace", driver="Aircraft deliveries or fleet history", price_basis="", train_window="", test_window="", n_train="", n_test="",
                  mape_pct="", bias_pct="", trend_growth_pct_per_year="", realised_growth_2019_to_last_pct="", annual_growth_error_pp="", used_to_shift=False, source="TODO(data)",
                  note="TODO(data): only two LEAP delivery points are logged (1,407 in 2024, 1,802 in 2025). Aircraft fleet history is shown in Airbus charts but not as a table. STAN C30 is the only aerospace trend backtest. Older Airbus GMF and Boeing CMO editions with annual delivery paths (2016 to 2019 vintages) are not in the repository, so no ten year delivery outlook can be tested against outcome. The haircut uses the Boeing 737 rate plan, the Airbus 2026 run rate, the LEAP guidance and (for non aerospace industries) the IEA WEI vintage as the available plan against outcome points."))
brows.append(dict(row_type="todo", series="BT_EV_SALES", industry="automotive", driver="IEA electric car sales history 2015 to 2025", price_basis="", train_window="", test_window="", n_train="", n_test="",
                  mape_pct="", bias_pct="", trend_growth_pct_per_year="", realised_growth_2019_to_last_pct="", annual_growth_error_pp="", used_to_shift=False, source="TODO(data)",
                  note="TODO(data): the history table behind data/raw/iea/GlobalEVOutlook2026.pdf is not in data/clean. SEMI and Cefic series have no multi year history in the repository."))
for ind, b in BT_IND.items():
    brows.append(dict(row_type="applied_correction", series=f"CORR_{ind}", industry=ind, driver="Correction applied to 2035 range", price_basis="", train_window="", test_window="", n_train=b["n"], n_test="",
                      mape_pct="", bias_pct="", trend_growth_pct_per_year="", realised_growth_2019_to_last_pct="", annual_growth_error_pp=round(100 * b["mean_err"], 2), used_to_shift=False,
                      source="derived", note=f"Growth shift applied {sg(b['shift']*100)} pp a year (a trend shift would have been {sg(b['shift_old']*100)} pp and is not used), extra sd {b['sd']*100:.2f} pp a year ({b['n_real']} real series, RMSE of all series {b['rmse']*100:.2f} pp)."))
pd.DataFrame(brows).to_csv(os.path.join(CLEAN, "model_backtest.csv"), index=False)
pd.DataFrame(CAL).to_csv(os.path.join(CLEAN, "model_calibration.csv"), index=False)
ovdf = pd.DataFrame(OV)
ovdf.to_csv(os.path.join(CLEAN, "model_supply_overlay.csv"), index=False)
t2 = pd.DataFrame(T2, columns=["opportunity", "metal", "product_form", "TRL", "evidence_strength", "earliest_volume_year", "signpost_and_evidence", "source"])
t2["status"] = "tier 2 (emerging)"
t2.loc[t2.opportunity.str.startswith("Captive powder metallurgy"), "status"] = "established, captive, tier 1 inside superalloy billet (not tier 2)"
t2.loc[t2.opportunity.str.startswith("AM powder, CoCr"), "status"] = "established, crowded, scored in Table 16 (not tier 2)"
t2.to_csv(os.path.join(CLEAN, "model_tier2_register.csv"), index=False)

# ------------------------------------------------------------------ 8. figures
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

plt.rcParams.update({"font.family": "Liberation Serif", "font.size": 9, "axes.spines.top": False, "axes.spines.right": False,
                     "svg.fonttype": "none", "axes.edgecolor": "#555", "axes.labelcolor": "#000"})
ACC, GREY, LGREY = "#1F4E79", "#9AA5B1", "#D5DAE0"
yrs = np.arange(Y0, Y1 + 1)


def save_fig(fig, name):
    fig.savefig(os.path.join(FIG, name + ".svg"), bbox_inches="tight")
    if os.environ.get("OUTLOOK_PNG_DIR"):
        fig.savefig(os.path.join(os.environ["OUTLOOK_PNG_DIR"], name + ".png"), dpi=150, bbox_inches="tight")


# Figure 3 labels are the integers of Table 13 (nickel rows of model_tier1_results.csv), so figure and table always agree
TAB13 = {}
for _ind in ORDER:
    _r = t1[(t1.level == "industry") & (t1.metal == "nickel") & (t1.industry == LAB[_ind])].iloc[0]
    TAB13[_ind] = (int(_r.index_p10), int(_r.index_p50), int(_r.index_p90))
fig, axs = plt.subplots(2, 4, figsize=(6.6, 3.6))
for ax, ind in zip(axs.flat, ORDER):
    q = np.percentile(PATH[ind], [10, 50, 90], axis=0)
    ax.fill_between(yrs, q[0], q[2], color=GREY, alpha=0.6, lw=0)
    ax.plot(yrs, q[1], color=ACC, lw=1.8)
    ax.axhline(100, color="#555", lw=0.6, ls=":")
    ax.set_title(LAB[ind].replace(" and environmental technology", " and environment").replace(" and electrical engineering", "").replace("Chemical processing", "Chemical"), fontsize=8)
    ax.text(Y1, q[2][-1] + 4, f"{TAB13[ind][2]}", ha="right", fontsize=7)
    ax.text(Y1, q[0][-1] - 12, f"{TAB13[ind][0]}", ha="right", fontsize=7)
    ax.text(Y1 + 0.25, q[1][-1], f"{TAB13[ind][1]}", ha="left", va="center", fontsize=7, color=ACC, fontweight="bold")
    ax.set_xticks([2025, 2030, 2035])
    ax.set_xlim(2025, 2037.0)
    ax.tick_params(labelsize=7)
    ax.set_ylim(50, 280)
ax = axs.flat[7]
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")
ax.fill_between([0, 1], [0.62, 0.62], [0.78, 0.78], color=GREY, alpha=0.6, lw=0)
ax.plot([0, 1], [0.70, 0.70], color=ACC, lw=1.8)
ax.text(0.0, 0.50, "Band: P10 to P90\nLine: P50\nLabels: 2035 P10,\nP50 (blue), P90\n10,000 draws\nIndex, 2025 = 100", fontsize=7, va="top")
fig.supylabel("Alloy demand index, 2025 = 100", fontsize=8)
fig.tight_layout()
save_fig(fig, "fig3_scenarios")
plt.close(fig)

cases = []
for r in OV:
    if r["demand_scenario"] == "Stated Policies" and r["supply_stage"] == "Mine supply" and r["metal"] in ("Cobalt", "Nickel", "Copper"):
        cases.append((r["metal"], r["case"].replace("Stress: ", "").replace("Base case", "Base case supply"), 100 * r["supply_2035_kt"] / r["demand_2035_kt"], r["case"].startswith("Stress")))
fig, ax = plt.subplots(figsize=(6.3, 3.0))
for i, (m, lab, v, stress) in enumerate(reversed(cases)):
    ax.barh(i, v, color=ACC if stress else GREY, height=0.65)
    ax.text(v + 1.0, i, f"{v:.0f}", va="center", fontsize=8)
ax.set_yticks(range(len(cases)))
ax.set_yticklabels([f"{m}: {l}" for m, l, v, s in reversed(cases)], fontsize=7.5)
ax.axvline(100, color="#555", lw=0.8, ls=":")
ax.set_xlabel("Mine supply 2035 as percent of IEA Stated Policies demand (grey: base case, blue: stress case)")
ax.set_xlim(0, 125)
save_fig(fig, "fig4_supply_overlay")
plt.close(fig)

fig, axs = plt.subplots(1, 2, figsize=(6.6, 2.8), gridspec_kw=dict(width_ratios=[1.35, 1]))
ax = axs[0]
items = [("FeNi family with SEMI driver (not used)", (134, 157, 185), False), ("FeNi family", tuple(pct(FAMIDX[FENI])), True), ("Electronics only variant", tuple(pct(FENI_ELEC)), True)] \
    + [(FENI_LAB[k], tuple(pct(FENI_C[k])), True) for k in FENI_LAB]
for i, (lab, q, new) in enumerate(reversed(items)):
    ax.plot([q[0], q[2]], [i, i], color=ACC if new else GREY, lw=5, solid_capstyle="butt")
    ax.plot([q[1]], [i], marker="|", color="black", ms=9)
    ax.text(q[2] + 4, i, f"{q[0]:.0f} / {q[1]:.0f} / {q[2]:.0f}", va="center", fontsize=7)
ax.set_yticks(range(len(items)))
ax.set_yticklabels([x[0] for x in reversed(items)], fontsize=7)
ax.axvline(100, color="#555", lw=0.6, ls=":")
ax.set_xlim(40, 280)
ax.set_xlabel("2035 index, 2025 = 100 (P10 / P50 / P90)", fontsize=8)
ax = axs[1]
for i, (lab, q) in enumerate(reversed([("Base", SEV["base"]), ("Severe, 70 percent recovery", SEV["sev"]), ("Severe, no recovery", SEV["nocatch"])])):
    ax.plot([q[0], q[2]], [i, i], color=ACC if i < 2 else GREY, lw=5, solid_capstyle="butt")
    ax.plot([q[1]], [i], marker="|", color="black", ms=9)
    ax.text(q[2] + 3, i, f"{q[1]:.0f}", va="center", fontsize=7)
ax.set_yticks(range(3))
ax.set_yticklabels(["Severe, no recovery", "Severe, 70 percent recovery", "Base"], fontsize=7)
ax.axvline(100, color="#555", lw=0.6, ls=":")
ax.set_xlim(60, 175)
ax.set_xlabel("Aerospace 2035 index (P10 to P90, P50 marked)", fontsize=8)
fig.tight_layout()
save_fig(fig, "fig5_feni_severe_aero")
plt.close(fig)

# ------------------------------------------------------------------ 9. results note


def md_table(df, cols=None):
    cols = cols or list(df.columns)
    out = ["| " + " | ".join(cols) + " |", "|" + "|".join("---" for _ in cols) + "|"]
    for _, r in df.iterrows():
        out.append("| " + " | ".join(str(r[c]).replace("|", "/") for c in cols) + " |")
    return "\n".join(out)


L = []
L.append("# Outlook model results (tier 1, tier 2, backtest, supply overlay)\n")
L.append("Generated by model/outlook_2035.py (seed 20261108, 10,000 draws). Do not edit by hand. Tables are compact for paste into chapter 7 and appendix A2. "
         "Every figure is a team estimate. Alloy demand indices are 2025 = 100 and are not tonnes unless the unit says t Co. Nickel tonnage by industry is not published (TODO(data)), so nickel is an index.\n")
L.append("## (i) Industry results, 2035 alloy demand index (2025 = 100)\n")
d = t1[(t1.level == "industry") & (t1.metal == "nickel")][["industry", "index_p10", "index_p50", "index_p90", "p50_2035_without_backtest_shift", "p50_2035_with_trend_shift_not_used"]].copy()
for c_ in ("index_p10", "index_p50", "index_p90"):
    d[c_] = d[c_].astype(int)
for c_ in ("p50_2035_without_backtest_shift", "p50_2035_with_trend_shift_not_used"):
    d[c_] = d[c_].astype(float).round(0).astype(int)
d.columns = ["Industry", "P10", "P50", "P90", "P50 without haircut", "P50 with trend shift (not used)"]
L.append("Base (columns P10 to P90): no trend shift, optimism haircut on official guidance drivers (aerospace median {:.2f}, energy, oil and gas, automotive median {:.2f}). "
         "The P50 columns on the right show the same model without the haircut (pure guidance) and with a trend shift added on top of guidance (not used, it would double count). Haircut medians are quoted from the draws, the triangular inputs are in the assumptions table.\n".format(float(np.median(HAIR["aerospace"])), float(np.median(HAIR["energy"]))))
L.append(md_table(d))
L.append("\nSub indices for automotive: " + ", ".join(f"{LAB[k]} {pct(IDX[k])[0]:.0f}/{pct(IDX[k])[1]:.0f}/{pct(IDX[k])[2]:.0f}" for k in ("automotive_thermal", "automotive_ev")) + ".\n")
L.append("Cobalt tonnes (measured or derived 2025 base):\n")
d = t1[(t1.metal == "cobalt") & (t1.unit.str.startswith("t Co"))][["industry", "unit", "base_2025", "p10_2035", "p50_2035", "p90_2035"]].copy()
d.columns = ["Industry", "Unit", "2025 base", "P10", "P50", "P90"]
L.append(md_table(d))
L.append("\nOther metal indices (low confidence): " + ", ".join(f"{r.metal} {r.industry} {r.index_p10:.0f}/{r.index_p50:.0f}/{r.index_p90:.0f}" for r in t1[t1.metal.isin(["titanium", "copper"])].itertuples()) + ".\n")
_f = pct(FAMIDX[FENI])
_e = pct(FENI_ELEC)
L.append("### FeNi family\n")
L.append(f"Precision FeNi strip and foil, 2035 index P10/P50/P90 = {_f[0]:.0f}/{_f[1]:.0f}/{_f[2]:.0f} (a variant built on SEMI fab equipment gave 134/157/185 and is not used, because fab tools use no Invar). "
         f"Electronics only variant (OLED mask foil and lead frames and seals, no EV) = {_e[0]:.0f}/{_e[1]:.0f}/{_e[2]:.0f}. "
         "Components (P10/P50/P90): " + "; ".join(f"{FENI_LAB[k]} {pct(FENI_C[k])[0]:.0f}/{pct(FENI_C[k])[1]:.0f}/{pct(FENI_C[k])[2]:.0f}" for k in FENI_LAB) + ". "
         "Weights 0.40/0.25/0.35 are team assumptions with Dirichlet concentration 8. Evidence is LOW: no OLED line capacity in square metres, no OLED shipments, no foil tonnes and no FeNi share of EV parts exist in research/. "
         "The OLED driver is DNP's quoted metal mask sales growth of 8.3 percent (high end) against mask free routes (low end).\n")
L.append("### Outlook versus outcome tests and optimism haircut\n")
d = pd.DataFrame([dict(Test=t["id"], Industry=t["industry"], Used_for=t["use"], Outlook=round(t["outlook"], 3), Outcome=round(t["outcome"], 3), Ratio=round(t["ratio"], 3), What=t["what"], Reading=t["note"], Sources=t["src"]) for t in OUTLOOK_TESTS])
L.append(md_table(d))
L.append(f"\nMemo: 2025 Airbus 793 plus Boeing 600 deliveries = 1,393 against an average annual requirement of {43420/20:.0f} aircraft in Airbus GMF 2025 ({100*MEMO_DELIV_RATIO:.0f} percent). "
         f"Haircut (outcome over outlook, applied to 2035 activity), triangular low/mode/high: aerospace {HAIR_AERO[0]:.2f}/{HAIR_AERO[1]:.2f}/{HAIR_AERO[2]:.2f} (median {float(np.median(HAIR['aerospace'])):.2f}, mean of the three aerospace points {AERO_MEAN:.3f}), energy, oil and gas and automotive {HAIR_OTH[0]:.2f}/{HAIR_OTH[1]:.2f}/{HAIR_OTH[2]:.2f} (median {float(np.median(HAIR['energy'])):.2f}). The median is the figure quoted in the text. "
         "TODO(data): earlier Airbus GMF and Boeing CMO editions with annual delivery paths, IEA WEO 2020 to 2023 editions. Energy rests on one OEM (Siemens Energy), GE Vernova and Mitsubishi Power are not in research/.\n")
L.append("### Product family tonnes, 2025 base and 2035 (kt, team estimate, never summed across families)\n")
d = pd.DataFrame(tonrows)[["product_family", "base_2025_kt_p10", "base_2025_kt_p50", "base_2025_kt_p90", "kt_2035_p10", "kt_2035_p50", "kt_2035_p90", "evidence"]]
d.columns = ["Family", "2025 P10", "2025 P50", "2025 P90", "2035 P10", "2035 P50", "2035 P90", "Evidence"]
L.append(md_table(d.fillna("n/a")))
L.append("\n" + "\n".join(f"* {r['product_family']}: {r['method']} Cross checks: {r['cross_checks']}" for r in tonrows) + "\n")
L.append("## (ii) Product families, 2035 index (2025 = 100)\n")
d = t1[t1.level == "product_family"][["industry", "index_p10", "index_p50", "index_p90", "activity_driver"]].copy()
for c_ in ("index_p10", "index_p50", "index_p90"):
    d[c_] = d[c_].astype(int)
d.columns = ["Product family", "P10", "P50", "P90", "Weights"]
L.append(md_table(d))
L.append("\n## (iii) Backtest, trend fitted to data to 2019, projected 2020 to last year\n")
d = pd.DataFrame([r for r in brows if r["row_type"] in ("driver_backtest", "outlook_vs_outcome")])[["series", "industry", "price_basis", "train_window", "test_window", "mape_pct", "bias_pct", "annual_growth_error_pp", "used_to_shift"]]
d.columns = ["Series", "Industry", "Basis", "Train", "Test", "MAPE %", "Bias %", "Growth error pp/yr", "Used to shift"]
L.append(md_table(d))
L.append("\nBias is the mean of (projection minus actual) over actual, so a positive value means the pre 2019 trend over projected. Growth error is trend slope minus realised slope 2019 to last year. "
         "Nominal STAN series are used only to widen ranges. TODO(data): ten year official outlook versus outcome, aircraft fleet history, EV sales history. "
         "The trend shift is not applied to guidance driven industries, see the haircut section.\n")
L.append("Range widening from the backtest (no growth shift applied, the trend shift that would have been added is in brackets and is not used): " + ", ".join(f"{k} extra sd {v['sd']*100:.2f} pp/yr ({sg(v['shift_old']*100)} pp/yr)" for k, v in BT_IND.items()) + ".\n")
L.append("## (iv) Supply overlay, 2035, kt contained metal\n")
d = ovdf[["metal", "case", "demand_scenario", "demand_2035_kt", "supply_stage", "supply_2035_kt", "gap_kt", "gap_pct_of_demand"]].copy()
d.columns = ["Metal", "Case", "Demand scenario", "Demand", "Supply stage", "Supply", "Gap", "Gap % of demand"]
L.append(md_table(d))
L.append(f"\nImplied secondary supply that reconciles the raw gap to the IEA published gap: copper {100*sec_cu:.0f} percent of demand (IEA gap 25 percent), cobalt {100*sec_co:.0f} percent (IEA gap over 25 percent). "
         f"Model superalloy cobalt in 2035 (aerospace plus energy) is P10/P50/P90 {pct(sup35)[0]:.1f}/{p50:.1f}/{pct(sup35)[2]:.1f} kt, about {100*p50/co_mine:.0f} percent of base mine supply and {100*p50/(co_mine-cut2):.0f} percent in the severe Congo case. "
         "Tungsten: qualitative, see table in the CSV.\n")
L.append("### Supply shock table\n")
d = pd.DataFrame(SHOCKS)[["shock", "affected_families", "gap_or_exposure", "cost_effect", "tier_changes_all", "score_moves_without_tier_change"]]
d.columns = ["Shock", "Affected families", "Gap or exposure", "Cost effect", "Every tier change", "Score moves without tier change"]
L.append(md_table(d))
L.append(f"\nSevere aerospace case: aerospace 2035 index P50 {SEV['base'][1]:.0f} (base) to {SEV['sev'][1]:.0f} (two years at minus 20 percent then {SEV_C[1]*100:.0f} percent recovery of the lost level, band {SEV['sev'][0]:.0f} to {SEV['sev'][2]:.0f}) "
         f"and {SEV['nocatch'][1]:.0f} without any recovery of the level. Superalloy bar, billet and remelt family P50 {SEV['fam'][1]:.0f} to {SEV['fam_sev'][1]:.0f}. Aviation cobalt 2035 P50 {pct(co_aero_t/1000.0)[1]:.1f} to {SEV['co_sev'][1]:.1f} kt. "
         f"Cumulative aerospace metal demand 2026 to 2035 is {SEV['cum_loss']:.1f} percent below the base P50 path.\n")
L.append("### Opportunity matrix computed from rules (model/scoring.py, data/clean/model_scores.csv)\n")
d = pd.DataFrame(SC_BASE)
d = d.sort_values("weighted_score", ascending=False)
d2 = d[["opportunity", "row_type", "evidence", "market", "growth", "supply", "competition", "technology", "customer", "barrier", "differentiation", "weighted_score", "tier", "tier_without_early_signal_cap", "score_equal_weights", "score_barriers_20pct_proportional", "score_barriers_20pct_equal_cut"]].copy()
for c_ in ("weighted_score", "score_equal_weights", "score_barriers_20pct_proportional", "score_barriers_20pct_equal_cut"):
    d2[c_] = d2[c_].map(lambda x: f"{x:.3f}")
d2.columns = ["Opportunity", "Row type", "Ev", "Mkt", "Gro", "Sup", "Comp", "Tech", "Cust", "Barr", "Diff", "Score", "Tier", "Tier without early signal cap", "Equal weights", "Barriers 20% (others rescaled)", "Barriers 20% (equal cut)"]
L.append(md_table(d2))
L.append("\nRules: growth bands from the P50 growth of the model index (5 from 4.0 percent, 4 from 3.0, 3 from 2.0, 2 from 0, else 1), market from the end use specific pool, supply security as the weakest input of the lead grades (tungsten in C-276 under the Chinese licence scores 2), "
         "the other five criteria are carried team judgement. Evidence E (no measured volume) caps the tier at Option. Tier thresholds 3.75 and 3.00. Sensitivities are computed, not rounded by hand.\n")
L.append("Added rules: market for rows without a cobalt pool uses the product family tonnes (model_family_tonnes.csv) times an end use weight and EU unit values, capped at 4 because the weight is unmeasured. "
         "Supply security adds a single source regime: one country mines at least 90 percent of world output with no control in force, element below 10 percent of the alloy scores 3 (niobium, Brazil about 93 percent, NB_USGS_BRAZIL_2025), above 10 percent scores 2. "
         "Engine bar lead grades are Alloy 718 (nickel, chromium, niobium 4.75 to 5.5 percent, cobalt 1.00 percent maximum, MO_SM_IN718_COMP) and cobalt bearing wrought grades (Waspaloy about 13 percent cobalt, MO_WASPALOY_CO, 720Li about 15 percent: TODO(data) no source for 720Li in the repository, the grade mix is a stated assumption). "
         "The headline row takes the weakest lead grade (cobalt above 10 percent under the Congo quota = 2), the Alloy 718 only variant scores 3 (niobium). "
         "Growth uses the most specific driver: new engine delivery path for engine bar, gas turbine hot section output for turbine remelt, semiconductor equipment path for fab gas strip, aftermarket pull for repair wire. "
         "The judgement values of the three rows added (fab gas strip and tube, FeNi36 strip for NO96 LNG tanks, superalloy repair wire) are first pass team judgement. "
         "GTT NO96 uses Invar (36 percent nickel steel, 0.7 mm, 500 mm wide strakes, MO_GTT_NO96), Mark III uses 304L stainless 1.2 mm (MO_GTT_MARKIII), so FeNi36 demand follows the NO96 share of LNG carrier orders, which is TODO(data) (no order book split is in the repository).\n")
L.append("### Priority 1 check and the combined vacuum melt superalloy programme\n")
_pri1 = [r["opportunity"] for r in SC_BASE if r["tier"] == "1"]
L.append("Rows at priority 1 in the base case: " + (", ".join(_pri1) if _pri1 else "none") + ". Engine bar and billet scores " + f"{[r for r in SC_BASE if r['opportunity']=='Engine bar and billet'][0]['weighted_score']:.2f}" + " and is tier " + [r for r in SC_BASE if r['opportunity']=='Engine bar and billet'][0]["tier"] + ".\n")
d = pd.DataFrame([r for r in prog_rows if r["case"] == "base"])[["variant", "weighting", "market", "growth", "supply", "score", "tier"]].copy()
d["score"] = d["score"].map(lambda x: f"{x:.3f}")
d.columns = ["Variant", "Weighting", "Mkt", "Gro", "Sup", "Score", "Tier"]
L.append(md_table(d))
L.append("\nThe programme is one melt shop serving both rows. Market uses the combined pool (aerospace 0.575 plus energy 0.30 of the family), growth the share weighted P50 growth of the two rows, supply the weakest member, the five judgement criteria the share weighted mean. Scores in every case are in data/clean/model_combined_programme.csv.\n")
L.append("### Aerospace with and without the haircut\n")
d = pd.DataFrame(AERO_CASES)[["case", "aerospace_index_p10", "aerospace_index_p50", "aerospace_index_p90", "new_engine_ratio_2035_p50", "new_engine_growth_p50_pct", "aviation_cobalt_2035_p50_kt", "engine_bar_score", "engine_bar_tier", "engine_bar_718_only_score", "turbine_remelt_score", "programme_score_base_weights", "programme_tier_base_weights"]]
d.columns = ["Case", "Index P10", "Index P50", "Index P90", "New engine ratio P50", "New engine growth P50 % a year", "Aviation Co 2035 P50 kt", "Engine bar score", "Tier", "718 only score", "Turbine remelt score", "Programme score", "Programme tier"]
L.append(md_table(d))
L.append("\n### Engine delivery path (evidence and model)\n")
d = pd.DataFrame(ep)[["row_type", "year", "series", "value", "unit", "source", "role"]]
L.append(md_table(d[d.row_type != "model median path before haircut"]))
L.append("\n### Indicative value per product family, EUR bn, team estimate, never summed\n")
d = pd.DataFrame(FAMVAL)
d = d[[c for c in ("product_family", "unit_value_eur_per_kg_low", "unit_value_eur_per_kg_high", "premium_low_mode_high", "eur_bn_2025_central_low", "eur_bn_2025_central_high", "eur_bn_2025_band_p10_low_to_p90_high", "eur_bn_2035_central_low", "eur_bn_2035_central_high", "eur_bn_2035_band_p10_low_to_p90_high", "gate_1p5_kt_eur_m_low_to_high", "gate_1p5_kt_share_of_2025_p50_pct") if c in d.columns]]
L.append(md_table(d.fillna("n/a")))
L.append("\nUnit values are EU27 extra EU import and export values per kg for 2024 (AC_EU_NI_UNITVAL_2024) and include pure nickel grades. 2035 is in constant 2024 unit values. The superalloy premium is a team assumption (MODEL_VALUE_SUPER_PREMIUM). Central range = P50 tonnes times low to high unit value. Families overlap and are not added.\n")
L.append("### Priority and tier changes in every shock case\n")
d = pd.DataFrame(shock_long)
d = d[d.tier_changed][["shock_case", "opportunity", "base_score", "base_tier", "case_score", "case_tier"]]
L.append(md_table(d) if len(d) else "No tier changes.")
L.append("\n")
L.append("## (v) Tier 2 register\n")
d = t2[["opportunity", "metal", "product_form", "TRL", "evidence_strength", "earliest_volume_year", "status"]].copy()
d.columns = ["Opportunity", "Metal", "Product form", "TRL", "Evidence", "Earliest volume", "Status"]
L.append(md_table(d))
L.append("\nTRL values and earliest volume years are team estimates. The workbook rows tagged [2035 candidate; inference] are not in the repository (report/metals_database.xlsx and model/*.xlsx contain no such tag), so the candidate list follows the framework chapter and the research notes. Signposts and sources are in data/clean/model_tier2_register.csv.\n")
L.append("## (vi) Assumptions\n")
d = pd.DataFrame([dict(ID=p["id"], Parameter=p["what"], Low=(round(p["lo"], 4) if isinstance(p["lo"], float) else p["lo"]), Mode=(round(p["mode"], 4) if isinstance(p["mode"], float) else p["mode"]),
                       High=(round(p["hi"], 4) if isinstance(p["hi"], float) else p["hi"]), Unit=p["unit"], Basis=p["basis"], Sources=p["src"], Reason=p["reason"]) for p in PARAMS])
L.append(md_table(d))
L.append("\nSimulation settings (team assumptions): triangular distributions, Gaussian copula with global cycle weight 0.2 and industry weight 0.3 on activity drivers, independent intensity and share draws, "
         f"Dirichlet weights with concentration {CONC:.0f}, backtest correction lambda {LAMBDA}, kappa {KAPPA}, shift cap {SHIFT_CAP*100:.1f} pp, sd cap {SD_CAP*100:.1f} pp. Paths between 2025 and 2035 are constant compound per component.\n")
os.makedirs(os.path.dirname(NOTE), exist_ok=True)
open(NOTE, "w", encoding="utf-8").write("\n".join(L))

# ------------------------------------------------------------------ 10. source log


def log_sources():
    rows = []
    for p in PARAMS:
        rows.append(dict(data_id=p["id"], metric=p["what"], value=f"{p['lo']:.4g};{p['mode']:.4g};{p['hi']:.4g}" if isinstance(p["lo"], float) else f"{p['lo']};{p['mode']};{p['hi']}",
                         unit=p["unit"] + " (low;mode;high)", year="2035", geography="World", material="Nickel;Cobalt", industry="All", source="Product Strategy 2035 two tier outlook model (model/outlook_2035.py)",
                         publisher="Team", author="Product Strategy 2035 Team", intext_author="Product Strategy 2035 Team", pub_date="2026", ref_type="dataset",
                         title="Product Strategy 2035 two tier outlook model parameters", url="https://github.com/sarahgarzond/metals-strategy-2035", type="team_estimate",
                         confidence="medium" if p["basis"].startswith(("sourced", "derived")) else "low",
                         notes=f"Basis: {p['basis']}. Underlying data_ids: {p['src']}. {p['reason']}"))
    for k, v in [("MODEL_CO_SUPER_NONAV_2025", ("Cobalt in superalloys outside aviation, derived", f"{co_super_nonav}", "t Co", "AERO_CI_SUPERALLOY_CO_2025 20,000 t minus AERO_CI_AVIATION_CO_2025 11,499 t. Mapped to the energy index.")),
                 ("MODEL_FAM_AERO_WEIGHT", ("Aerospace weight in the superalloy product family", f"{f1_aero_w:.3f}", "weight", "11,499 t divided by 20,000 t cobalt (Cobalt Institute)")),
                 ("MODEL_SIEMENS_GT_RATIO", ("Gas turbine output ratio 2035 to 2025 from Siemens Energy path", f"{gt_ratio:.3f}", "ratio", "(30/17)^(4/5): 17 GW FY2024, 30 GW FY2029, flat after. CO_SIEMENSENERGY_CMD_2025")),
                 ("MODEL_AIRBUS_FLEET_CAGR", ("Airbus passenger fleet CAGR 2025 to 2045", f"{100*airbus_cagr:.2f}", "percent per year", "(45,550/23,310)^(1/20)-1. AERO_AIRBUS_GMF2026_FLEET_2025, AERO_AIRBUS_GMF2026_FLEET_2045")),
                 ("MODEL_SEMI_2031_INDEX", ("SEMI 300 mm capacity index 2031 (2025 = 100)", f"{100*semi_2031:.1f}", "index", "1.07 x 1.08^3 x 0.94 x 1.09. SEMI_300MM_PATH")),
                 ("MODEL_HK_CAGR_POOLED", ("OECD hip plus knee procedures CAGR 2013 to 2024, constant set", f"{100*hk_cagr['pooled']:.2f}", "percent per year", f"{len(ctry)} countries, data/clean/oecd_health_hip_knee_procedures.csv"))]:
        rows.append(dict(data_id=k, metric=v[0], value=v[1], unit=v[2], year="2025", geography="World", material="Nickel;Cobalt", industry="All",
                         source="Product Strategy 2035 two tier outlook model (model/outlook_2035.py)", publisher="Team", author="Product Strategy 2035 Team",
                         intext_author="Product Strategy 2035 Team", pub_date="2026", ref_type="dataset", title="Product Strategy 2035 two tier outlook model parameters",
                         url="https://github.com/sarahgarzond/metals-strategy-2035", type="team_estimate", confidence="medium", notes=v[3]))
    for b in BT:
        rows.append(dict(data_id="MODEL_" + b["series"], metric=f"Backtest MAPE and bias: {b['driver']}", value=f"{100*b['mape']:.1f};{100*b['bias']:.1f}", unit="percent (MAPE;bias)",
                         year="2020 to " + str(b["last"]), geography="World", material="Nickel;Cobalt", industry=b["industry"], source="Product Strategy 2035 two tier outlook model (model/outlook_2035.py)",
                         publisher="Team", author="Product Strategy 2035 Team", intext_author="Product Strategy 2035 Team", pub_date="2026", ref_type="dataset",
                         title="Product Strategy 2035 two tier outlook model parameters", url="https://github.com/sarahgarzond/metals-strategy-2035", type="team_estimate", confidence="medium",
                         notes=f"Log linear trend fitted {b['first']} to 2019, projected to {b['last']}. {b['note']} Underlying: {b['src']}"))
    base_meta = dict(geography="World", material="Nickel;Cobalt", industry="All", source="Product Strategy 2035 two tier outlook model (model/outlook_2035.py)", publisher="Team",
                     author="Product Strategy 2035 Team", intext_author="Product Strategy 2035 Team", pub_date="2026", ref_type="dataset", title="Product Strategy 2035 two tier outlook model parameters",
                     url="https://github.com/sarahgarzond/metals-strategy-2035", type="team_estimate")
    sc_sorted = sorted(SC_BASE, key=lambda r: -r["weighted_score"])
    rows.append(dict(data_id="MODEL_SCORING_2026", metric="Opportunity matrix scores and scoring rules (eight criteria, weights 15/20/15/10/10/10/10/10), computed by model/scoring.py",
                     value="; ".join(f"{r['opportunity']} {r['weighted_score']:.2f} ({r['tier']})" for r in sc_sorted), unit="weighted score 1 to 5", year="2026", confidence="medium",
                     notes="data/clean/model_scores.csv. Market, growth and supply security are computed from rules, the other five criteria are carried team judgement. Equal weights: " + "; ".join(f"{r['opportunity']} {r['score_equal_weights']:.3f}" for r in sc_sorted[:3])
                     + ". Entry barriers at 20 percent, others rescaled proportionally: " + "; ".join(f"{r['opportunity']} {r['score_barriers_20pct_proportional']:.3f}" for r in sc_sorted[:3])
                     + ".", **base_meta))
    rows.append(dict(data_id="MODEL_TIER2_REGISTER_2026", metric="Tier 2 register of emerging opportunities: TRL, evidence, earliest volume year, signpost", value=f"{int((t2.status=='tier 2 (emerging)').sum())} tier 2 opportunities, 2 established rows split out",
                     unit="register", year="2026", confidence="medium", notes="data/clean/model_tier2_register.csv. TRL and years are team estimates. Captive powder metallurgy disc powder (established) and open market AM powder (established, crowded) are no longer tier 2.", **base_meta))
    for fam_, key_ in [(r_["product_family"], i_) for i_, r_ in enumerate(tonrows)][:4]:
        r_ = tonrows[key_]
        rows.append(dict(data_id="MODEL_TON_" + "".join(c for c in fam_.upper() if c.isalpha())[:16], metric=f"2025 base and 2035 tonnes, product family: {fam_}",
                         value=f"{r_['base_2025_kt_p50']};{r_['kt_2035_p10']};{r_['kt_2035_p50']};{r_['kt_2035_p90']}", unit="kt (2025 P50; 2035 P10; P50; P90)", year="2035", confidence="low",
                         notes=f"{r_['method']} Team estimate, never summed across families. Cross checks: {r_['cross_checks']}", **base_meta))
    rows.append(dict(data_id="MODEL_FENI_FAMILY_2035", metric="Precision FeNi strip and foil 2035 index P10;P50;P90 and electronics only variant", value=f"{pct(FAMIDX[FENI])[0]:.0f};{pct(FAMIDX[FENI])[1]:.0f};{pct(FAMIDX[FENI])[2]:.0f}; electronics only {pct(FENI_ELEC)[0]:.0f};{pct(FENI_ELEC)[1]:.0f};{pct(FENI_ELEC)[2]:.0f}",
                     unit="index 2025 = 100", year="2035", confidence="low", notes="OLED mask foil, EV magnetic sensor and shielding, lead frames and seals. No SEMI fab equipment weight. Low evidence, see MODEL_FENI_* parameters.", **base_meta))
    rows.append(dict(data_id="MODEL_SEVERE_AERO_2035", metric="Severe aerospace case (two years at minus 20 percent, then recovery): aerospace 2035 index P10;P50;P90", value=f"{SEV['sev'][0]:.0f};{SEV['sev'][1]:.0f};{SEV['sev'][2]:.0f} (base {SEV['base'][0]:.0f};{SEV['base'][1]:.0f};{SEV['base'][2]:.0f})",
                     unit="index 2025 = 100", year="2035", confidence="low", notes="Recovery share of the lost level triangular 0.0;0.7;1.0 (MODEL_SEVERE_AERO_RECOVERY). Motivated by 2020, no recovery series in the repository.", **base_meta))
    rows.append(dict(data_id="MO_HAYNES_C276_W", metric="Nominal tungsten in HASTELLOY C-276", value="4", unit="percent of gross weight", year="2023", geography="United States", material="Tungsten", industry="nickel alloy",
                     source="Haynes HASTELLOY C-276 brochure H-2002H", publisher="Haynes International", author="Haynes International", intext_author="Haynes International", pub_date="2023", ref_type="report",
                     title="HASTELLOY C-276 alloy", issue="1", url="https://haynesintl.com/wp-content/uploads/2024/08/c-276.pdf", type="primary", confidence="medium",
                     notes="Nominal composition, same brochure as MO_HAYNES_C276_MO (UNS N10276, tungsten nominal 4.0, range 3.0 to 4.5). Value entered from the composition table, page not re-opened in this run: verify. Used only for the tungsten exposure arithmetic and the supply security score."))
    _sc = {r["opportunity"]: r for r in SC_BASE}
    _co = t1[(t1.metal == "cobalt") & (t1.unit.str.startswith("t Co"))]
    rows.append(dict(data_id="MODEL_T1_RESULTS_2035", metric="Tier 1 alloy demand index 2035 by industry, P10/P50/P90 (2025 = 100)",
                     value="; ".join(f"{LAB[k]} {TAB13[k][0]}/{TAB13[k][1]}/{TAB13[k][2]}" for k in ORDER) + "; " + "; ".join(f"{r.industry} cobalt {r.base_2025:.0f} t to {r.p10_2035:.0f}/{r.p50_2035:.0f}/{r.p90_2035:.0f} t" for r in _co.itertuples()),
                     unit="index 2025 = 100", year="2035", confidence="low",
                     notes=f"data/clean/model_tier1_results.csv and research/model/outlook_results.md, seed {SEED}, {N:,} draws. No trend shift applied, optimism haircut on guided drivers (aerospace median {float(np.median(HAIR['aerospace'])):.2f}, triangular mode {HAIR_AERO[1]:.2f}, energy, oil and gas and automotive median {float(np.median(HAIR['energy'])):.2f}, triangular mode {HAIR_OTH[1]:.2f}). "
                           f"P50 growth a year: " + ", ".join(f"{LAB[k]} {100*cg(IDX[k]):.2f}" for k in ORDER) + " percent. P50 without haircut: " + ", ".join(f"{LAB[k]} {_p50v(k, IDX[k] * ni_c, 1.0, 'noshift'):.0f}" for k in ORDER) + ".", **base_meta))
    rows.append(dict(data_id="MODEL_FAM_RESULTS_2035", metric="Product family index 2035, P10/P50/P90 (2025 = 100), weighted industry indices",
                     value="; ".join(f"{f_[:30]} {pct(FAMIDX[f_])[0]:.0f}/{pct(FAMIDX[f_])[1]:.0f}/{pct(FAMIDX[f_])[2]:.0f}" for f_ in FAM) + f" (FeNi electronics only {pct(FENI_ELEC)[0]:.0f}/{pct(FENI_ELEC)[1]:.0f}/{pct(FENI_ELEC)[2]:.0f})",
                     unit="index 2025 = 100", year="2035", confidence="low", notes="Weights in research/model/outlook_results.md (ii) and MODEL_FAM_* rows. Only the aerospace weight 0.575 is measured. FeNi built on OLED mask foil 0.40, EV sensor and shielding 0.25, lead frames and seals 0.35.", **base_meta))
    rows.append(dict(data_id="MODEL_SUPPLY_SHOCKS_2026", metric="Supply shock table and severe aerospace case: exposure, cost effect and every tier change",
                     value=" | ".join(f"{sh_['shock'][:40]}: {sh_['tier_changes_all']}" for sh_ in SHOCKS), unit="score and tier", year="2035", confidence="low",
                     notes="data/clean/model_supply_shocks.csv (every tier change per shock) and model_shock_tiers.csv (every row in every shock). Cost arithmetic is team arithmetic: 8 percent virgin cobalt, USD 21 per lb (2025 estimate) against USD 16.77 (2024), 40 kg W per t of C-276 at USD 252 and 380 per mtu WO3 concentrate.", **base_meta))
    rows.append(dict(data_id="MODEL_ENGINE_PATH_2026", metric="New engine delivery path 2025 to 2035: LEAP, Airbus and Boeing delivery evidence, 2026 guidance, 2028 plan, 2035 requirement",
                     value=f"2035 over 2025 P10/P50/P90 {pct(r35)[0]:.2f}/{pct(r35)[1]:.2f}/{pct(r35)[2]:.2f} after haircut; {pct(r35 / HAIR['aerospace'])[1]:.2f} before", unit="ratio", year="2035", confidence="low",
                     notes="data/clean/model_engine_delivery_path.csv. Anchors: LEAP 1,802 (2025), 2026 guidance +18 percent, 2028 plan 2,500 to 2,600, 2035 at the Airbus GMF and Boeing CMO average annual deliveries over Airbus plus Boeing 2025 deliveries. Team estimate.", **base_meta))
    rows.append(dict(data_id="MODEL_AERO_HAIRCUT_CASES_2026", metric="Aerospace results with and without the optimism haircut, engine bar and programme scores",
                     value=" | ".join(f"{c_['case']}: index {c_['aerospace_index_p10']:.0f}/{c_['aerospace_index_p50']:.0f}/{c_['aerospace_index_p90']:.0f}, engine bar {c_['engine_bar_score']:.2f} ({c_['engine_bar_tier']}), programme {c_['programme_score_base_weights']:.2f} ({c_['programme_tier_base_weights']})" for c_ in AERO_CASES),
                     unit="index and score", year="2035", confidence="low", notes="data/clean/model_aerospace_haircut_cases.csv. Haircut median quoted from draws.", **base_meta))
    rows.append(dict(data_id="MODEL_COMBINED_PROGRAMME_2026", metric="Vacuum melt superalloy programme (engine bar plus turbine remelt, one melt shop) scores under four weightings",
                     value="; ".join(f"{r_['variant'][:12]} {r_['weighting'][:14]} {r_['score']:.3f} ({r_['tier']})" for r_ in prog_rows if r_["case"] == "base"), unit="weighted score 1 to 5", year="2026", confidence="low",
                     notes="data/clean/model_combined_programme.csv. Market on the combined pool, growth share weighted, supply the weakest member, judgement criteria share weighted.", **base_meta))
    rows.append(dict(data_id="MODEL_FAMILY_VALUE_2026", metric="Indicative EUR value of product family tonnes (team estimate, never summed)",
                     value="; ".join(f"{v_['product_family'][:25]} 2025 {v_.get('eur_bn_2025_central_low','n/a')} to {v_.get('eur_bn_2025_central_high','n/a')} EUR bn" for v_ in FAMVAL), unit="EUR bn", year="2025", confidence="low",
                     notes="data/clean/model_family_value.csv. kt (model_family_tonnes.csv) x EU27 extra EU unit values (AC_EU_NI_UNITVAL_2024) x superalloy premium (MODEL_VALUE_SUPER_PREMIUM). Constant 2024 unit values.", **base_meta))
    _s24 = HS6_SUMM[(HS6_SUMM.year == 2024)].set_index(["hs", "flow"])
    rows.append(dict(data_id="MODEL_COMTRADE_HS6_2024", metric="Alloy only nickel mill products traded 2024, ten reporters (HS 750512, 750522, 750620, 750712): exports kt and USD per kg",
                     value="; ".join(f"{h_} {_s24.loc[(h_, 'Export'), 'net_weight_kt']:.1f} kt at USD {_s24.loc[(h_, 'Export'), 'unit_value_usd_per_kg']:.1f} per kg" for h_ in ("750512", "750522", "750620", "750712")),
                     unit="kt; USD per kg", year="2024", confidence="medium",
                     notes="data/clean/comtrade_hs6_alloy_summary_2023-2024.csv and research/model/comtrade_hs6_alloy.md. UN Comtrade public preview, World partner, customs value per kg of net weight, re-exports counted by each reporter. Alloy share of the four digit totals on eight reporters in comtrade_hs6_alloy_share_of_four_digit_2023-2024.csv.", **base_meta))
    for _id in ("MODEL_AERO_NEW_G26", "MODEL_AERO_NEW_G"):
        rows.append(dict(data_id=_id, notes="Superseded by MODEL_AERO_NEW_E26, MODEL_AERO_NEW_E28 and MODEL_AERO_NEW_R35 (engine delivery path). Not used in the model."))
    rows.append(dict(data_id="MO_SM_IN718_COMP", metric="Alloy 718 limiting composition: niobium plus tantalum 4.75 to 5.50, cobalt 1.00 maximum", value="4.75 to 5.50; 1.00", unit="percent (Nb plus Ta; Co max)", year="2007", geography="United States", material="Nickel;Cobalt;Niobium", industry="Aerospace",
                     source="Special Metals INCONEL alloy 718 publication SMC-045", publisher="Special Metals Corporation", author="Special Metals Corporation", intext_author="Special Metals Corporation", pub_date="2007", ref_type="report",
                     title="INCONEL alloy 718", url="https://www.specialmetals.com/documents/technical-bulletins/inconel/inconel-alloy-718.pdf", type="primary", confidence="high",
                     notes="Table 1 limiting chemical composition (nickel plus cobalt 50.00 to 55.00, chromium 17.00 to 21.00). PDF downloaded and read in this run. Used for the supply security score of the Alloy 718 lead grade (niobium single source, no cobalt to speak of)."))
    rows.append(dict(data_id="MO_WASPALOY_CO", metric="Waspaloy nominal composition: cobalt 13, chromium 19, molybdenum 4, titanium 3 percent", value="13", unit="percent cobalt", year="2026", geography="United States", material="Cobalt", industry="Aerospace",
                     source="Wikipedia Waspaloy (cites the Haynes Waspaloy datasheet)", publisher="Wikimedia Foundation", author="Wikipedia contributors", intext_author="Wikipedia contributors", pub_date="2026", ref_type="webpage",
                     title="Waspaloy", url="https://en.wikipedia.org/wiki/Waspaloy", type="secondary", confidence="low",
                     notes="Secondary source, the primary Haynes datasheet returned 403 from the cloud session. Used only as the grade mix assumption that wrought cobalt bearing engine grades carry more than 10 percent cobalt. 720Li about 15 percent cobalt is NOT sourced: TODO(data), Special Metals Udimet 720Li datasheet URL not found."))
    rows.append(dict(data_id="MO_GTT_NO96", metric="GTT NO96 membrane: primary and secondary membranes of Invar, a 36 percent nickel steel, 0.7 mm thick, 500 mm wide strakes", value="0.7", unit="mm thickness", year="2026", geography="World", material="Nickel", industry="Oil and gas",
                     source="GTT NO96 technologies page", publisher="Gaztransport et Technigaz", author="Gaztransport et Technigaz", intext_author="Gaztransport et Technigaz", pub_date="2026", ref_type="webpage",
                     title="NO96 technologies", url="https://gtt.fr/technologies/no96", type="primary", confidence="high",
                     notes="Page opened in this run. More than 200 vessels in operation and under construction use NO96 and its evolutions (NO96 L03, L03+, GW, Super+). The NO96 share of LNG carrier orders is TODO(data), the page gives no split."))
    rows.append(dict(data_id="MO_GTT_MARKIII", metric="GTT Mark III membrane: primary corrugated stainless steel 304L membrane, 1.2 mm, secondary membrane of composite material", value="304L 1.2", unit="grade, mm", year="2026", geography="World", material="Nickel", industry="Oil and gas",
                     source="GTT Mark III technologies page", publisher="Gaztransport et Technigaz", author="Gaztransport et Technigaz", intext_author="Gaztransport et Technigaz", pub_date="2026", ref_type="webpage",
                     title="Mark III technologies", url="https://gtt.fr/technologies/markiii", type="primary", confidence="high",
                     notes="Page opened in this run. Mark III and Mark III Flex use no Invar. More than 200 vessels in operation and under construction use Mark III and its evolutions."))
    seen, uniq = set(), []
    for r in rows:
        if r["data_id"] not in seen:
            seen.add(r["data_id"])
            uniq.append(r)
    subprocess.run([sys.executable, os.path.join(ROOT, "tools", "add_sources.py")], input=json.dumps(uniq), text=True, check=True, cwd=ROOT)


if "--no-log" not in sys.argv:
    log_sources()

print("outlook_2035 done")
for ind in ORDER:
    q = pct(IDX[ind])
    print(f"{ind:12s} P10/P50/P90 {q[0]:.0f}/{q[1]:.0f}/{q[2]:.0f}")
for fam in FAM:
    q = pct(FAMIDX[fam])
    print(f"{fam[:40]:40s} {q[0]:.0f}/{q[1]:.0f}/{q[2]:.0f}")

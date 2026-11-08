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


def dirichlet(wdict):
    keys = list(wdict)
    a = np.array([wdict[k] for k in keys]) * CONC
    g = rng.gamma(a, size=(N, len(keys)))
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
    BT_IND[ind] = dict(mean_err=mean_err, shift=shift, rmse=rmse, sd=sd, n_real=len(real), n=len(g))
    par(f"MODEL_BT_{ind.upper()}", f"Backtest correction for {ind}: annual growth shift and annual sd carried into the range", shift, mean_err, sd,
        "per year (shift, mean error, sd)", "derived from backtest", "OECD_STAN_P1 / IEA_WEI_UPSTREAM_REGION_2026 / MED_OECD_HK_COUNT_2023 / EUROSTAT_C29_EU27_2025",
        f"Shift is minus {LAMBDA} times the mean annual growth error of real series (capped at {SHIFT_CAP*100:.1f} pp), sd is {KAPPA} times the RMSE of all series (capped at {SD_CAP*100:.1f} pp). Lambda, kappa and caps are team assumptions: windows are short and 2020 to 2025 contains the pandemic.")

# one point outlook versus outcome (two vintages of the IEA investment series)
OUTLOOK_CHECK = dict(series="BT_OUTLOOK_WEI2025_vs_WEI2026", outlook=570.0, outcome=542.0)

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
a2n = par("MODEL_AERO_NEW_G26", "Engine output growth 2025 to 2026", 1.16, 1.18, 1.19, "ratio", "sourced",
          "CO_GE_Q2LEAP_2026 / AERO_LEAP_2025", "GE guided LEAP delivery growth in the high teens for 2026 on 1,802 engines in 2025.")
a2g = par("MODEL_AERO_NEW_G", "Engine output growth 2026 to 2035 after the ramp, annual", 0.020, airbus_cagr, 0.050, "per year", "derived plus team assumption",
          "AERO_AIRBUS_GMF2026_FLEET_2025 / AERO_AIRBUS_GMF2026_FLEET_2045 / AERO_BOEING_CMO2026_FLEET_CAGR",
          "Mode is the Airbus fleet path 23,310 to 45,550 aircraft in 2045 (3.4 percent a year, team arithmetic). Low 2.0 and high 5.0 percent are team assumptions: parts shortages persist or deliveries catch up.")
ai = par("MODEL_AERO_INT", "Superalloy mass per engine and aircraft, annual trend", -0.010, 0.0, 0.010, "per year", "team assumption", "AERO_AIRBUS_GMF2026_NEWGEN_2035",
         "No kilogram per engine is published. New generation share rises from 39 to 82 percent (hotter cores add alloy, durability kits and fewer shop visits remove it).")
ash = par("MODEL_AERO_SHARE", "Nickel and cobalt superalloy share of hot section mass, ratio 2035 to 2025", 0.90, 0.98, 1.03, "ratio", "team assumption", "(none, see reason)",
          "Titanium aluminide already flies in a low pressure turbine and ceramic matrix composites are entering, but no published kilogram displacement exists. Skewed to the downside.")
comp("aerospace", "Aftermarket and engine overhaul pull", 0.5, ("cagr",) + a1, ai, ash,
     "Airbus GSF aviation services growth (off wing maintenance 3.7 percent a year)", "AERO_AIRBUS_GSF2026_SERVICES_2026, AERO_AIRBUS_GSF2026_SERVICES_2045")
comp("aerospace", "New engine output", 0.5, ("two", a2n, a2g), ai, ash,
     "CFM LEAP deliveries 1,802 in 2025, high teens growth 2026, then Airbus fleet path", "AERO_LEAP_2025, CO_GE_Q2LEAP_2026, AERO_AIRBUS_GMF2026_FLEET_2025, AERO_AIRBUS_GMF2026_FLEET_2045")
par("MODEL_AERO_W", "Weight of aftermarket versus new engine output in the aerospace index", 0.5, 0.5, 0.5, "weight", "team assumption", "CO_GE_CES_2025",
    "GE Commercial Engines and Services takes 75 percent of revenue from services, but metal pull per revenue dollar is higher for new parts. Equal weights, Dirichlet noise.")

# ENERGY
e1 = par("MODEL_EN_GT_R", "Gas turbine output ratio 2035 to 2025", 1.15, gt_ratio, 1.85, "ratio", "derived plus team assumption",
         "CO_SIEMENSENERGY_CMD_2025 / CO_SIEMENSENERGY_CAP_2026 / IEA_WEI_GASPOWER_2025",
         "Mode: Siemens Energy path 17 GW (FY2024) to 30 GW (FY2029 midpoint of FY2028 to 2030), flat afterwards, as a proxy for world output. Low 1.15: order cycle turns once the backlog is delivered (IEA gas power investment 112 to 114 USD bn, flat). High 1.85: capacity keeps growing 3 percent a year after 2030.")
e2 = par("MODEL_EN_NUC_R", "Nuclear fleet and tube demand ratio 2035 to 2025", 1.05, 1.20, 1.45, "ratio", "derived plus team assumption",
         "EE_NUC_IAEA_2025 / EE_NUC_WNA_2030 / CO_WESTINGHOUSE_PIPE_2026",
         "Mode: 377 GW operating plus 56 GWe under construction gives 1.15 by 2030, then 4 percent more. Low: retirements offset additions. High: AP1000 and small reactor programmes beyond the build now under way.")
e3 = par("MODEL_EN_OTH_G", "Other power and process equipment, annual growth", 0.020, 0.030, 0.036, "per year", "sourced plus team assumption",
         "EE_ELEC_GROWTH_2024 (3.6 percent a year 2026 to 2030 is from IEA Electricity 2026 in research/sectors/energy_environment.md, data_id pending)",
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
    "Precision FeNi strip and foil": dict(w=dict(electronics=0.60, automotive_ev=0.30, medical=0.10),
        why="Team assumption by design: electronics (invar masks, lead frames, shielding) and electric vehicle sensors and motors only. The combustion car index is excluded on purpose.",
        src="DNP_INVAR_2024, IEA_GEVO_EV_SHARE_2035"),
}
for k, v in FAM.items():
    par("MODEL_FAM_" + "".join(c for c in k.upper() if c.isalpha())[:14],
        f"Product family weights: {k}", min(v['w'].values()), max(v['w'].values()), sum(v['w'].values()), "weights (min, max, sum)", "team assumption",
        v["src"], v["why"] + " Weights: " + ", ".join(f"{a} {b:.3f}" for a, b in v["w"].items()) + f". Dirichlet noise, concentration {CONC:.0f}.")

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


def run_industry(ind, comps, bt_key=None, extra=None):
    ws = dirichlet({c["name"]: c["w"] for c in comps})
    btl = bt_log(bt_key or ind)
    tot = np.zeros(N)
    path = np.zeros((N, H + 1))
    for c in comps:
        a = extra[c["name"]] if extra else draw_act(ind, c["act"])
        a = a * np.exp(btl)
        it = (1.0 + tri_ppf(u_ind(), *c["int"])) ** H
        sh = tri_ppf(u_ind(), *c["share"])
        R = a * it * sh
        ACTR[(ind, c["name"])] = a
        tot += ws[c["name"]] * R
        for t in range(H + 1):
            path[:, t] += ws[c["name"]] * R ** (t / H)
    return tot, path


for ind in ["aerospace", "energy", "electronics", "medical", "chemical", "oil_and_gas"]:
    IDX[ind], PATH[ind] = run_industry(ind, IND_COMP[ind])

# automotive: shared car sales and electric share draws feed both sub indices
T = tri_ppf(u_act("automotive"), *t_car)
S = tri_ppf(u_act("automotive"), *s35)
th_act = T * (1 - S) / (1 - 0.25)
ev_act = T * S / 0.25
IND_COMP["automotive_thermal"] = [dict(name="Combustion and hybrid cars (turbo, exhaust, sensors)", w=1.0, act=None, int=ati, share=ats,
                                       driver="New car sales x (1 minus electric share), 2025 electric share 25 percent", src="IEA_GEVO_EV_SHARE_2025, IEA_WEO_EV_STEPS_2035, IEA_WEO_EV_CPS_2035, ACEA_CAR_REG_2025")]
IND_COMP["automotive_ev"] = [dict(name="Electric cars (motors, resolvers, sensors)", w=1.0, act=None, int=aei, share=aes,
                                  driver="New car sales x electric share, 20 million electric cars in 2025", src="IEA_GEVO_EV_SALES_2025, IEA_GEVO_EV_SHARE_2025, IEA_GEVO_ECARS_STEPS_2035")]
IDX["automotive_thermal"], PATH["automotive_thermal"] = run_industry("automotive", IND_COMP["automotive_thermal"], extra={IND_COMP["automotive_thermal"][0]["name"]: th_act})
IDX["automotive_ev"], PATH["automotive_ev"] = run_industry("automotive", IND_COMP["automotive_ev"], extra={IND_COMP["automotive_ev"][0]["name"]: ev_act})
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
for fam, spec in FAM.items():
    ws = dirichlet(spec["w"])
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
    ("Additively manufactured engine parts and spare powder", "Nickel, cobalt", "Atomised superalloy powder", "7 to 9 (team estimate)", "early signal", "2027 to 2030",
     "Carpenter powder and additive segment earned a 7.9 percent operating margin against 27.7 percent in premium alloys (fiscal 2026). Hoganas sells nickel and cobalt powders for powder bed fusion. Powder metal disc issue on the geared turbofan shows the value of qualified powder. Signpost: a named disc or hot section additive specification with a volume call.",
     "research/sectors/aerospace.md, research/companies/hoganas.md, research/companies/carpenter.md"),
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
    return (f"Annual growth shift {sg(b['shift']*100)} pp, extra sd {b['sd']*100:.2f} pp a year "
            f"({b['n_real']} real and {b['n']-b['n_real']} nominal backtest series)")


ROWS = []


def row(level, ind, metal, unit, base, arr, scale, drv, intens, share_, anchor, evidence, src, note=""):
    q = pct(arr * scale)
    qi = pct(arr)
    ROWS.append(dict(level=level, industry=LAB.get(ind, ind), metal=metal, unit=unit, base_2025=base, p10_2035=round(q[0], 1), p50_2035=round(q[1], 1), p90_2035=round(q[2], 1),
                     index_p10=round(qi[0], 0), index_p50=round(qi[1], 0), index_p90=round(qi[2], 0), activity_driver=drv, activity_ratio_p10_p50_p90=act_range(ind) if level == "industry" else "",
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
    wtxt = ", ".join(f"{LAB.get(k, k)} {v:.3f}" for k, v in spec["w"].items())
    ROWS.append(dict(level="product_family", industry=fam, metal="nickel and cobalt alloy index", unit="index 2025 = 100", base_2025=100,
                     p10_2035=round(pct(arr)[0], 1), p50_2035=round(pct(arr)[1], 1), p90_2035=round(pct(arr)[2], 1), index_p10=round(pct(arr)[0], 0), index_p50=round(pct(arr)[1], 0),
                     index_p90=round(pct(arr)[2], 0), activity_driver="Weighted industry indices: " + wtxt, activity_ratio_p10_p50_p90="", intensity_assumption_and_trend="Inherited from industry indices",
                     alloy_share_assumption="Inherited from industry indices", backtest_adjustment="Inherited", calibration_anchor="Aerospace weight in family 1 = 11,499/20,000 t cobalt (measured)" if fam.startswith("Superalloy") else "Weights are team assumptions",
                     evidence="index (weights are team assumptions)", sources=spec["src"], note=spec["why"]))
t1 = pd.DataFrame(ROWS)
_rev = {v: k for k, v in LAB.items()}
t1["prior_team_workbook_base_2035_index"] = [
    (round(100 * (1 + PRIOR[_rev[r.industry]] / 100) ** 10) if (r.level == "industry" and r.metal == "nickel" and r.industry in _rev and _rev[r.industry] in PRIOR) else np.nan)
    for r in t1.itertuples()]
t1.to_csv(os.path.join(CLEAN, "model_tier1_results.csv"), index=False)

# backtest csv
brows = []
for b in BT:
    brows.append(dict(row_type="driver_backtest", series=b["series"], industry=b["industry"], driver=b["driver"], price_basis=b["price_basis"],
                      train_window=f"{b['first']} to 2019", test_window=f"2020 to {b['last']}", n_train=b["n_train"], n_test=b["n_test"],
                      mape_pct=round(100 * b["mape"], 1), bias_pct=round(100 * b["bias"], 1), trend_growth_pct_per_year=round(100 * (math.exp(b["trend"]) - 1), 2),
                      realised_growth_2019_to_last_pct=round(100 * (math.exp(b["realised"]) - 1), 2), annual_growth_error_pp=round(100 * b["err"], 2),
                      used_to_shift=b["shift_ok"], source=b["src"], note=b["note"]))
brows.append(dict(row_type="outlook_vs_outcome", series=OUTLOOK_CHECK["series"], industry="oil_and_gas",
                  driver="IEA in year outlook for 2025 upstream investment (WEI 2025, just under USD 570 bn, 2024 prices) versus WEI 2026 outcome (USD 542 bn, 2025 prices)",
                  price_basis="real, price base differs", train_window="n/a", test_window="2025", n_train="", n_test=1, mape_pct=round(100 * abs(570 / 542 - 1), 1),
                  bias_pct=round(100 * (570 / 542 - 1), 1), trend_growth_pct_per_year="", realised_growth_2019_to_last_pct="", annual_growth_error_pp="", used_to_shift=False,
                  source="OG_WEO2025_UPSTREAM_2025, IEA_WEI_UPSTREAM_REGION_2026",
                  note="One point, one year ahead, different price base (2024 versus 2025 USD), so it is indicative only. TODO(data): a ten year outlook with outcome (for example an Airbus GMF or IEA EV Outlook from 2016 to 2019 versus 2025) is not in the repository."))
brows.append(dict(row_type="todo", series="BT_AERO_DELIVERIES", industry="aerospace", driver="Aircraft deliveries or fleet history", price_basis="", train_window="", test_window="", n_train="", n_test="",
                  mape_pct="", bias_pct="", trend_growth_pct_per_year="", realised_growth_2019_to_last_pct="", annual_growth_error_pp="", used_to_shift=False, source="TODO(data)",
                  note="TODO(data): only two LEAP delivery points are logged (1,407 in 2024, 1,802 in 2025). Aircraft fleet history is shown in Airbus charts but not as a table. STAN C30 is the only aerospace backtest."))
brows.append(dict(row_type="todo", series="BT_EV_SALES", industry="automotive", driver="IEA electric car sales history 2015 to 2025", price_basis="", train_window="", test_window="", n_train="", n_test="",
                  mape_pct="", bias_pct="", trend_growth_pct_per_year="", realised_growth_2019_to_last_pct="", annual_growth_error_pp="", used_to_shift=False, source="TODO(data)",
                  note="TODO(data): the history table behind data/raw/iea/GlobalEVOutlook2026.pdf is not in data/clean. SEMI and Cefic series have no multi year history in the repository."))
for ind, b in BT_IND.items():
    brows.append(dict(row_type="applied_correction", series=f"CORR_{ind}", industry=ind, driver="Correction applied to 2035 range", price_basis="", train_window="", test_window="", n_train=b["n"], n_test="",
                      mape_pct="", bias_pct="", trend_growth_pct_per_year="", realised_growth_2019_to_last_pct="", annual_growth_error_pp=round(100 * b["mean_err"], 2), used_to_shift=b["n_real"] > 0,
                      source="derived", note=f"Growth shift {sg(b['shift']*100)} pp a year, extra sd {b['sd']*100:.2f} pp a year ({b['n_real']} real series used for the shift, RMSE of all series {b['rmse']*100:.2f} pp)."))
pd.DataFrame(brows).to_csv(os.path.join(CLEAN, "model_backtest.csv"), index=False)
pd.DataFrame(CAL).to_csv(os.path.join(CLEAN, "model_calibration.csv"), index=False)
ovdf = pd.DataFrame(OV)
ovdf.to_csv(os.path.join(CLEAN, "model_supply_overlay.csv"), index=False)
t2 = pd.DataFrame(T2, columns=["opportunity", "metal", "product_form", "TRL", "evidence_strength", "earliest_volume_year", "signpost_and_evidence", "source"])
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


fig, axs = plt.subplots(2, 4, figsize=(6.6, 3.6))
for ax, ind in zip(axs.flat, ORDER):
    q = np.percentile(PATH[ind], [10, 50, 90], axis=0)
    ax.fill_between(yrs, q[0], q[2], color=GREY, alpha=0.6, lw=0)
    ax.plot(yrs, q[1], color=ACC, lw=1.8)
    ax.axhline(100, color="#555", lw=0.6, ls=":")
    ax.set_title(LAB[ind].replace(" and environmental technology", " and environment").replace(" and electrical engineering", "").replace("Chemical processing", "Chemical"), fontsize=8)
    ax.text(Y1, q[2][-1] + 4, f"{q[2][-1]:.0f}", ha="right", fontsize=7)
    ax.text(Y1, q[0][-1] - 12, f"{q[0][-1]:.0f}", ha="right", fontsize=7)
    ax.text(Y1 - 0.2, q[1][-1] + 1, "", fontsize=7)
    ax.set_xticks([2025, 2030, 2035])
    ax.set_xlim(2025, 2035.6)
    ax.tick_params(labelsize=7)
    ax.set_ylim(50, 280)
ax = axs.flat[7]
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")
ax.fill_between([0, 1], [0.62, 0.62], [0.78, 0.78], color=GREY, alpha=0.6, lw=0)
ax.plot([0, 1], [0.70, 0.70], color=ACC, lw=1.8)
ax.text(0.0, 0.50, "Band: P10 to P90\nLine: P50\n10,000 draws\nAlloy demand index,\n2025 = 100", fontsize=7, va="top")
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
d = t1[(t1.level == "industry") & (t1.metal == "nickel")][["industry", "index_p10", "index_p50", "index_p90", "prior_team_workbook_base_2035_index"]].copy()
d.columns = ["Industry", "P10", "P50", "P90", "Earlier team workbook base"]
L.append(md_table(d))
L.append("\nSub indices for automotive: " + ", ".join(f"{LAB[k]} {pct(IDX[k])[0]:.0f}/{pct(IDX[k])[1]:.0f}/{pct(IDX[k])[2]:.0f}" for k in ("automotive_thermal", "automotive_ev")) + ".\n")
L.append("Cobalt tonnes (measured or derived 2025 base):\n")
d = t1[(t1.metal == "cobalt") & (t1.unit.str.startswith("t Co"))][["industry", "unit", "base_2025", "p10_2035", "p50_2035", "p90_2035"]].copy()
d.columns = ["Industry", "Unit", "2025 base", "P10", "P50", "P90"]
L.append(md_table(d))
L.append("\nOther metal indices (low confidence): " + ", ".join(f"{r.metal} {r.industry} {r.index_p10:.0f}/{r.index_p50:.0f}/{r.index_p90:.0f}" for r in t1[t1.metal.isin(["titanium", "copper"])].itertuples()) + ".\n")
L.append("## (ii) Product families, 2035 index (2025 = 100)\n")
d = t1[t1.level == "product_family"][["industry", "index_p10", "index_p50", "index_p90", "activity_driver"]].copy()
d.columns = ["Product family", "P10", "P50", "P90", "Weights"]
L.append(md_table(d))
L.append("\n## (iii) Backtest, trend fitted to data to 2019, projected 2020 to last year\n")
d = pd.DataFrame([r for r in brows if r["row_type"] in ("driver_backtest", "outlook_vs_outcome")])[["series", "industry", "price_basis", "train_window", "test_window", "mape_pct", "bias_pct", "annual_growth_error_pp", "used_to_shift"]]
d.columns = ["Series", "Industry", "Basis", "Train", "Test", "MAPE %", "Bias %", "Growth error pp/yr", "Used to shift"]
L.append(md_table(d))
L.append("\nBias is the mean of (projection minus actual) over actual, so a positive value means the pre 2019 trend over projected. Growth error is trend slope minus realised slope 2019 to last year. "
         "Nominal STAN series are used only to widen ranges. TODO(data): ten year official outlook versus outcome, aircraft fleet history, EV sales history.\n")
L.append("Applied corrections: " + ", ".join(f"{k} shift {sg(v['shift']*100)} pp/yr, extra sd {v['sd']*100:.2f} pp/yr" for k, v in BT_IND.items()) + ".\n")
L.append("## (iv) Supply overlay, 2035, kt contained metal\n")
d = ovdf[["metal", "case", "demand_scenario", "demand_2035_kt", "supply_stage", "supply_2035_kt", "gap_kt", "gap_pct_of_demand"]].copy()
d.columns = ["Metal", "Case", "Demand scenario", "Demand", "Supply stage", "Supply", "Gap", "Gap % of demand"]
L.append(md_table(d))
L.append(f"\nImplied secondary supply that reconciles the raw gap to the IEA published gap: copper {100*sec_cu:.0f} percent of demand (IEA gap 25 percent), cobalt {100*sec_co:.0f} percent (IEA gap over 25 percent). "
         f"Model superalloy cobalt in 2035 (aerospace plus energy) is P10/P50/P90 {pct(sup35)[0]:.1f}/{p50:.1f}/{pct(sup35)[2]:.1f} kt, about {100*p50/co_mine:.0f} percent of base mine supply and {100*p50/(co_mine-cut2):.0f} percent in the severe Congo case. "
         "Tungsten: qualitative, see table in the CSV.\n")
L.append("## (v) Tier 2 register\n")
d = t2[["opportunity", "metal", "product_form", "TRL", "evidence_strength", "earliest_volume_year"]].copy()
d.columns = ["Opportunity", "Metal", "Product form", "TRL", "Evidence", "Earliest volume"]
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

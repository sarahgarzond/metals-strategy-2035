#!/usr/bin/env python3
"""Opportunity matrix scoring (chapter 8, Table 16 and Table A4) computed from explicit rules.

Three of the eight criteria are computed from data, never typed in:
  Market attractiveness  from the end use specific measured pool (rule table MARKET_RULES)
  Growth to 2035        from the P50 growth a year of the most specific model index (GROWTH_BANDS) or, for early signals, from the earliest volume year
  Supply security       from the weakest input of the lead grades (INPUT_SCORE), using the restriction regime of each input element
The other five criteria (competitive intensity, technology, customers, entry barriers, differentiation) are team judgement on the
anchors of Table A4 and are carried as inputs (JUDGEMENT), because the repository holds no measured data for them. Entry barriers are
TODO(data) in years: Table A13 gives no approval times.

Inputs  data/clean/model_scoring_inputs.csv  (written by model/outlook_2035.py: P50 growth by driver, pools)
Output  data/clean/model_scores.csv          scores, weighted score, tier, equal weight and 20 percent barrier sensitivities (full precision)
Run: python3 model/scoring.py   (also called by model/outlook_2035.py, which passes shock overrides)
"""
import csv
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CLEAN = os.path.join(ROOT, "data", "clean")

CRIT = [("market", 0.15), ("growth", 0.20), ("supply", 0.15), ("competition", 0.10), ("technology", 0.10),
        ("customer", 0.10), ("barrier", 0.10), ("differentiation", 0.10)]
W = dict(CRIT)
assert abs(sum(W.values()) - 1.0) < 1e-12

# ---------------------------------------------------------------- rules (Table A4 style)
# Growth: P50 annual growth of the most specific index. 4.0 percent or more = 5, 3.0 to 3.99 = 4, 2.0 to 2.99 = 3, 0 to 1.99 = 2, below 0 = 1
GROWTH_BANDS = [(0.040, 5), (0.030, 4), (0.020, 3), (0.000, 2)]


def growth_score(g):
    for lo, sc in GROWTH_BANDS:
        if g >= lo:
            return sc
    return 1


def growth_score_signal(year):
    """Early signals have no modelled index: score on the earliest volume year (3 by 2028, 2 for 2029 to 2033, 1 later)."""
    return 3 if year <= 2028 else (2 if year <= 2033 else 1)


# Market: the pool must be specific to the opportunity's end use.
#   measured_kt_co   measured or derived contained cobalt in the end use, kt: 10 or more = 5, 5 to 10 = 4, 2 to 5 = 3, below 2 = 2 (derived pools are capped at 4)
#   estimated_eur_bn wider measured product code (PRODCOM, EU27) times a team estimate end use weight: 1.5 bn or more = 4 (cap, weight unmeasured),
#                    0.75 to 1.5 = 4, 0.30 to 0.75 = 3, below 0.30 = 2
#   company_end_use  revenue of one end use in a company filing, mixed alloys: 3 (measured niche), 4 from EUR 0.75 bn
#   wider_segment    a measured segment that mixes the product with others and has no end use split: 2
#   none             no measured or estimable volume of the product (capacity announcements and activity counts do not count): 1
def market_score(kind, value, derived=False):
    if kind == "measured_kt_co":
        sc = 5 if value >= 10 else (4 if value >= 5 else (3 if value >= 2 else 2))
        return min(sc, 4) if derived else sc
    if kind == "estimated_eur_bn":
        return 4 if value >= 0.75 else (3 if value >= 0.30 else 2)
    if kind == "company_end_use":
        return 4 if value >= 0.75 else 3
    if kind == "wider_segment":
        return 2
    return 1


# Supply security: lowest score over the inputs of the lead grades.
# regime per input: none 5, form_not_used 4 (control on a form that melters do not buy), price_only 4 (ore quota, alloy feed outside the quota),
#   quota_minor 3 (Congo cobalt quota, element below 10 percent of the alloy), licence_minor 2 (Chinese licence regime, element below 10 percent),
#   quota_principal 2 (Congo quota, element above 10 percent), licence_principal 1, halt 1 (active licence halt)
#   single_source_minor 3 (one country mines at least 90 percent of world output and no control is in force, element below 10 percent of the alloy: niobium, Brazil about 93 percent),
#   single_source_principal 2 (same concentration, element above 10 percent)
INPUT_SCORE = {"none": 5, "form_not_used": 4, "price_only": 4, "quota_minor": 3, "licence_minor": 2, "quota_principal": 2,
               "licence_principal": 1, "halt": 1, "single_source_minor": 3, "single_source_principal": 2}

# Opportunity definitions. inputs: (element, regime); judgement: comp, tech, cust, barr, diff (anchors in Table A4).
# growth: ("index", key) or ("signal", earliest volume year). pool: key into the pool table written by outlook_2035.py.
# type: main (a row of the matrix), variant (a split of a main row by lead grade), new (row added because the report names it as growing).
# The judgement values of the three new rows are first pass team judgement on the Table A4 anchors, flagged as such.
NB = "niobium (Alloy 718 about 5 percent, Brazil about 93 percent of mine output, NB_USGS_BRAZIL_2025)"
CO_GRADES = "cobalt in wrought cobalt bearing grades (Waspaloy about 13 percent, 720Li about 15 percent: TODO(data) source for 720Li)"
OPPS = [
    dict(id="Turbine remelt stock and sheet", type="main", growth=("index", "gas_turbine"), pool="turbine", derived=True,
         inputs=[("cobalt", "quota_minor"), ("nickel", "none"), ("chromium", "none")],
         sens_inputs=[("tungsten (not evidenced for these alloys, TODO(data))", "licence_minor")],
         judgement=dict(competition=2, technology=4, customer=5, barrier=5, differentiation=4)),
    dict(id="Engine bar and billet", type="main", growth=("index", "aero_new"), pool="engine_bar", derived=True,
         inputs=[(CO_GRADES, "quota_principal"), (NB, "single_source_minor"), ("nickel", "none"), ("chromium", "none")],
         sens_inputs=[],
         judgement=dict(competition=2, technology=5, customer=5, barrier=4, differentiation=4)),
    dict(id="Engine bar and billet, Alloy 718 only", type="variant", growth=("index", "aero_new"), pool="engine_bar", derived=True,
         inputs=[(NB, "single_source_minor"), ("nickel", "none"), ("chromium", "none"), ("cobalt (Alloy 718: 1.00 percent maximum, MO_SM_IN718_COMP)", "none")],
         sens_inputs=[],
         judgement=dict(competition=2, technology=5, customer=5, barrier=4, differentiation=4)),
    dict(id="FeNi36 foil and FeNi strip", type="main", growth=("index", "feni"), pool="feni", derived=False,
         inputs=[("nickel", "none"), ("iron", "none")], sens_inputs=[],
         judgement=dict(competition=2, technology=5, customer=3, barrier=3, differentiation=4)),
    dict(id="CoCr implant bar and powder", type="main", growth=("index", "medical"), pool="medical", derived=False,
         inputs=[("cobalt (about 60 percent of Co28Cr6Mo)", "quota_principal"), ("chromium", "none")], sens_inputs=[],
         judgement=dict(competition=3, technology=4, customer=4, barrier=5, differentiation=3)),
    dict(id="Sour service bar, strip, wire", type="main", growth=("index", "oil_and_gas"), pool="sour", derived=False,
         inputs=[("nickel", "none"), ("molybdenum (powder control only)", "form_not_used")], sens_inputs=[],
         judgement=dict(competition=3, technology=3, customer=3, barrier=5, differentiation=3)),
    dict(id="Chemical plate, welding wire", type="main", growth=("index", "chemical"), pool="chemical", derived=False,
         inputs=[("nickel", "none"), ("molybdenum (powder control only)", "form_not_used"),
                 ("tungsten in C-276 (about 4 percent) under the Chinese licence", "licence_minor")], sens_inputs=[],
         judgement=dict(competition=2, technology=3, customer=3, barrier=3, differentiation=3)),
    dict(id="Alloy 690 bar and hollows", type="main", growth=("index", "nuclear"), pool="alloy690", derived=False,
         inputs=[("nickel", "none"), ("chromium", "none")], sens_inputs=[],
         judgement=dict(competition=3, technology=4, customer=4, barrier=3, differentiation=3)),
    dict(id="Solid oxide cell strip", type="main", growth=("signal", 2026), pool="none", derived=False,
         inputs=[("chromium (ferritic steel)", "none"), ("nickel coating", "none")], sens_inputs=[],
         judgement=dict(competition=3, technology=4, customer=2, barrier=3, differentiation=4)),
    dict(id="Alloy C-276 fusion tape foil", type="main", growth=("signal", 2030), pool="none", derived=False,
         inputs=[("nickel", "none"), ("molybdenum (powder control only)", "form_not_used"),
                 ("tungsten in C-276 (about 4 percent) under the Chinese licence", "licence_minor")], sens_inputs=[],
         judgement=dict(competition=4, technology=5, customer=2, barrier=3, differentiation=5)),
    dict(id="AM powder, CoCr and nickel superalloy", type="main", growth=("index", "aero_new"), pool="am_powder", derived=False,
         inputs=[("cobalt (CoCr lead grade F75)", "quota_principal"), ("nickel", "none")], sens_inputs=[],
         judgement=dict(competition=2, technology=4, customer=4, barrier=3, differentiation=3)),
    dict(id="Car exhaust and turbo alloys", type="main", growth=("index", "automotive_thermal"), pool="car", derived=False,
         inputs=[("nickel", "none"), ("chromium", "none")], sens_inputs=[],
         judgement=dict(competition=3, technology=1, customer=2, barrier=3, differentiation=2)),
    # rows the report itself names as growing
    dict(id="Fab gas delivery strip and tube", type="new", growth=("index", "semi_fab"), pool="fab_gas", derived=False,
         inputs=[("nickel", "none"), ("chromium", "none"), ("molybdenum (powder control only)", "form_not_used")],
         sens_inputs=[("tungsten if the lead grade is C-276 or C-22 (not evidenced, TODO(data))", "licence_minor")],
         judgement=dict(competition=3, technology=4, customer=4, barrier=3, differentiation=3)),
    dict(id="FeNi36 strip for NO96 LNG membrane tanks", type="new", growth=("signal", 2026), pool="none", derived=False,
         inputs=[("nickel", "none"), ("iron", "none")], sens_inputs=[],
         judgement=dict(competition=3, technology=4, customer=3, barrier=3, differentiation=4)),
    dict(id="Superalloy repair wire", type="new", growth=("index", "aero_mro"), pool="none", derived=False,
         inputs=[("nickel", "none"), ("chromium", "none"), ("niobium (Alloy 718 and 625 type fillers, grade mix assumed)", "single_source_minor")],
         sens_inputs=[("cobalt bearing fillers (not evidenced, TODO(data))", "quota_minor")],
         judgement=dict(competition=2, technology=3, customer=3, barrier=3, differentiation=2)),
]

def weighted(sc, weights=W):
    return sum(weights[k] * sc[k] for k in weights)


def tier(score, evidence, cap=True):
    score = round(score, 9)   # guards the thresholds against floating point noise only
    if evidence == "E" and cap:
        return "Option" if score >= 3.0 else "Monitor"
    if score >= 3.75:
        return "1"
    if score >= 3.0:
        return "2"
    return "Monitor" if score >= 2.75 else "Harvest"


def barrier_weights_proportional(share=0.20):
    rest = 1.0 - W["barrier"]
    return {k: (share if k == "barrier" else W[k] * (1.0 - share) / rest) for k in W}


def barrier_weights_equal_cut(share=0.20):
    d = (share - W["barrier"]) / (len(W) - 1)
    return {k: (share if k == "barrier" else W[k] - d) for k in W}


EQUAL = {k: 1.0 / len(W) for k in W}


def read_inputs(path=None):
    path = path or os.path.join(CLEAN, "model_scoring_inputs.csv")
    d = {}
    for r in csv.DictReader(open(path, encoding="utf-8")):
        d[(r["kind"], r["key"])] = r
    return d


def score_all(inp, supply_override=None, growth_override=None, label=""):
    """supply_override: {element keyword: regime} replaces the regime of matching inputs (shock runs).
    growth_override: {index key: P50 annual growth} replaces the model growth (severe aerospace run)."""
    out = []
    for o in OPPS:
        sc = {}
        # market
        pr = inp[("pool", o["pool"])]
        sc["market"] = market_score(pr["pool_kind"], float(pr["pool_value"]) if pr["pool_value"] not in ("", "none") else 0.0, o["derived"])
        # growth
        gk, gv = o["growth"]
        if gk == "index":
            g = (growth_override or {}).get(gv, float(inp[("growth", gv)]["p50_cagr"]))
            sc["growth"] = growth_score(g)
        else:
            g = None
            sc["growth"] = growth_score_signal(gv)
        # supply
        regimes = []
        for el, rg in o["inputs"]:
            for kw, newrg in (supply_override or {}).items():
                if kw in el:
                    rg = newrg
            regimes.append((el, rg, INPUT_SCORE[rg]))
        sc["supply"] = min(x[2] for x in regimes)
        sens = min([x[2] for x in regimes] + [INPUT_SCORE[rg] for _, rg in o["sens_inputs"]])
        sc.update(o["judgement"])
        ev = "E" if pr["pool_kind"] == "none" else "M"
        s = weighted(sc)
        out.append(dict(opportunity=o["id"], row_type=o["type"], evidence=ev, **{k: sc[k] for k, _ in CRIT}, growth_p50_cagr_pct=("" if g is None else g * 100.0),
                        market_basis=f"{pr['pool_kind']} {pr['pool_value']} {pr['unit']}", supply_weakest=min(regimes, key=lambda x: x[2])[0],
                        supply_if_untested_inputs_counted=sens,
                        weighted_score=s, tier=tier(s, ev), tier_without_early_signal_cap=tier(s, ev, cap=False),
                        score_equal_weights=weighted(sc, EQUAL), tier_equal_weights=tier(weighted(sc, EQUAL), ev),
                        score_barriers_20pct_proportional=weighted(sc, barrier_weights_proportional()),
                        score_barriers_20pct_equal_cut=weighted(sc, barrier_weights_equal_cut()),
                        case=label))
    return out


WEIGHTINGS = [("base weights (15/20/15/10/10/10/10/10)", W), ("equal weights", EQUAL),
              ("entry barriers 20 percent, others rescaled proportionally", barrier_weights_proportional()),
              ("entry barriers 20 percent, equal cut of the others", barrier_weights_equal_cut())]


def combine(rows, ids, shares, pool_key, inp, label, growth_cagr=None):
    """One programme that serves several opportunity rows from the same melt shop (for example engine bar plus turbine remelt).
    market: rule on the combined pool of the programme. growth: band of the share weighted P50 growth of the member rows.
    supply: the weakest member (one melt shop carries every input). The five judgement criteria: share weighted mean of the member rows (full precision).
    Returns one dict per weighting with the score and the tier (evidence M)."""
    by = {r["opportunity"]: r for r in rows}
    tot = sum(shares)
    sh = [x / tot for x in shares]
    pr = inp[("pool", pool_key)]
    sc = {"market": market_score(pr["pool_kind"], float(pr["pool_value"]), True)}
    g = sum(w * by[i]["growth_p50_cagr_pct"] / 100.0 for w, i in zip(sh, ids)) if growth_cagr is None else growth_cagr
    sc["growth"] = growth_score(g)
    sc["supply"] = min(by[i]["supply"] for i in ids)
    for k in ("competition", "technology", "customer", "barrier", "differentiation"):
        sc[k] = sum(w * by[i][k] for w, i in zip(sh, ids))
    out = []
    for name, wts in WEIGHTINGS:
        v = weighted(sc, wts)
        out.append(dict(programme=label, members=" + ".join(ids), member_shares="/".join(f"{x:.3f}" for x in sh), weighting=name, **{k: sc[k] for k, _ in CRIT},
                        growth_p50_cagr_pct=g * 100.0, market_basis=f"{pr['pool_kind']} {pr['pool_value']} {pr['unit']}", score=v, tier=tier(v, "M")))
    return out


def write(rows, path=None):
    path = path or os.path.join(CLEAN, "model_scores.csv")
    flds = list(rows[0].keys())
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=flds)
        w.writeheader()
        w.writerows(rows)


if __name__ == "__main__":
    inp = read_inputs()
    rows = score_all(inp, label="base")
    write(rows)
    for r in sorted(rows, key=lambda x: -x["weighted_score"]):
        print(f"{r['opportunity']:42s} {r['weighted_score']:.3f} tier {r['tier']:8s} (uncapped {r['tier_without_early_signal_cap']}) mkt {r['market']} gro {r['growth']} sup {r['supply']}")

#!/usr/bin/env python3
"""Append or update rows in data/sources.csv from a JSON list (stdin). Keys: data_id plus any column."""
import csv, json, sys, os, fcntl, datetime
p = os.path.join(os.path.dirname(__file__), "..", "data", "sources.csv")
lock = open(p + ".lock", "w"); fcntl.flock(lock, fcntl.LOCK_EX)
rows = list(csv.DictReader(open(p, encoding="utf-8"))); fields = list(rows[0].keys())
by = {r["data_id"]: r for r in rows}
for new in json.load(sys.stdin):
    r = by.get(new["data_id"]) or {k: "" for k in fields}
    r.update({k: str(v) for k, v in new.items() if k in fields})
    r.setdefault("retrieved", datetime.date.today().isoformat())
    if not r.get("retrieved"): r["retrieved"] = datetime.date.today().isoformat()
    if new["data_id"] not in by: rows.append(r); by[new["data_id"]] = r
w = csv.DictWriter(open(p, "w", newline="", encoding="utf-8"), fieldnames=fields); w.writeheader(); w.writerows(rows)
print(len(rows), "rows")

#!/usr/bin/env python3
"""Merge research/**/*.sources.csv written by parallel agents into data/sources.csv (dedupe on data_id, newest wins)."""
import csv, glob, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
main = os.path.join(ROOT, "data", "sources.csv")
rows = {r["data_id"]: r for r in csv.DictReader(open(main, encoding="utf-8"))}
fields = list(next(iter(rows.values())).keys())
added = 0
for f in sorted(glob.glob(os.path.join(ROOT, "research", "**", "*.sources.csv"), recursive=True)):
    for r in csv.DictReader(open(f, encoding="utf-8")):
        if r.get("data_id"):
            added += r["data_id"] not in rows
            rows[r["data_id"]] = {k: r.get(k, "") for k in fields}
w = csv.DictWriter(open(main, "w", newline="", encoding="utf-8"), fieldnames=fields)
w.writeheader(); w.writerows(rows.values())
print(f"merged, {added} new rows, {len(rows)} total")

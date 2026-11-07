---
name: run-pipeline
description: Orchestrates the full agent team for the Product Strategy 2035 report. Research, model, write, check, grade in parallel, consolidate and repeat until the stop condition. Use when the user says run the pipeline, next round, or /run-pipeline.
---
# Pipeline (the main session is the orchestrator and does not write the report itself)

Arguments: optional `research`, `draft`, `review` to run one stage only, or `round N`.

## Stage 1: Research (parallel)
- Launch one `material-researcher` per metal of chapter 4 (nickel, cobalt, chromium, molybdenum, titanium, tungsten,
  zirconium, copper, aluminium, manganese), with worktree isolation.
- Launch seven `sector-analyst` agents (one per section of chapter 5), with worktree isolation.
- Run them in the background, then merge each branch into main when it finishes and resolve conflicts in data/sources.csv
  by keeping all rows and deduplicating on data_id.

## Stage 2: Model and strategy
- `data-modeler` integrates the numbers and regenerates the Excel model and figures.
- `writer` or a `material-researcher` turns the trade notes into chapter 6 (Global Market Dynamics and Trade).
- `strategist` improves chapters 7 and 8.
- `writer` improves chapters 1, 2, 3 (framework, minimal refinement only) and 9 and harmonises all sections.

## Stage 3: Quality gate
- `style-editor` passes until `python3 .claude/skills/house-style/lint.py sections` reports 0.
- Build the PDF with the build-report skill. The main text (title page to Conclusion) must be 30 pages or fewer.

## Stage 4: Review panel (parallel, read only)
- Create reviews/round_N/ (N = last round + 1).
- Launch `fact-checker`, `grader-tum`, `grader-industry` and `grader-client` in parallel. Tell each the round number.
- Then `consolidator` writes fixes.md and the scoreboard.

## Stage 5: Improve
- `writer` (prose), `data-modeler` (numbers and charts) and `sector-analyst` or `material-researcher`
  (missing evidence) apply fixes.md in rank order.
- Commit with the message `round N: <average grade>`.
- If the consolidator says CONTINUE, go back to Stage 3. If it says STOP, report the final grades and the open items to the user.

Safety limits: at most 5 rounds without asking the user. Always tell the user the scoreboard after each round.

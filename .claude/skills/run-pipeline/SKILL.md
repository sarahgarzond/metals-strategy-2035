---
name: run-pipeline
description: Orchestrates the full agent team for the Product Strategy 2035 report. Research, model, write, check, grade in parallel, consolidate and repeat until the stop condition. Use when the user says run the pipeline, next round, or /run-pipeline.
---
# Pipeline (the main session is the orchestrator and does not write the report itself)

Arguments: optional `research`, `draft`, `review` to run one stage only, or `round N`.

## Stage 0: Pull the Google Doc
- Run the PULL steps of the gdoc-sync skill, so the round starts from the team's latest text.

## Stage 1: Research (follows the research-protocol skill)
1a. Data pull (main session or data-modeler, sequential because of API rate limits):
    `python3 tools/data/fetch.py usgs`, `pinksheet`, `stan`, `prodcom` (all portfolio codes), and `comtrade` for every HS code
    in `fetch.py list` across reporters 0 (World), 276, 842, 156, 392, 410, 356, 250, 826, 380, 360, years 2019 to latest.
1b. Company research: launch `company-researcher` agents in parallel, 5 to 6 companies each, until every company in
    data/companies.csv has a profile in research/companies/. Start with competitors and the largest customers.
1c. Launch one `material-researcher` per metal (nickel, cobalt, chromium, molybdenum, titanium, tungsten, zirconium, copper,
    aluminium, manganese, plus trade_chapter_6) and seven `sector-analyst` agents, with worktree isolation, notes only.
1d. Research gate: `python3 tools/research_audit.py`. Every FAIL goes back to its agent with the problem list
    (reviews/research_audit.md). No agent writes section text before its note passes.
    Show the user the audit table and ask them to spot check two notes before Stage 2.

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
- Run the PUSH steps of the gdoc-sync skill: the improvements appear in the team's Google Doc as tracked suggestions.
  Ask the user before the first push of a session.
- If the consolidator says CONTINUE, go back to Stage 3. If it says STOP, report the final grades and the open items to the user.

Safety limits: at most 5 rounds without asking the user. Always tell the user the scoreboard after each round.

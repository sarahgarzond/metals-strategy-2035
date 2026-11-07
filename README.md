# Forging the Future: Market Intelligence and Growth Strategy for High-Performance Metals Through 2035

Agent team workspace for the TUM project study.

## Your Google Doc is the master draft
The team's Google Doc was imported into sections/ (one file per chapter or section, same headings and order).
After you edit the Google Doc, ask Claude to "re-import the Google Doc": it exports the doc with the Google Docs connector to
data/raw/gdoc_export.json and runs `python3 tools/import_gdoc.py data/raw/gdoc_export.json`. New text lands in
sections/_import/ for comparison, and `--force` overwrites sections/.

This repository is set up so that Claude Code runs a team of specialised agents that research, model, write,
check and grade the report in repeated rounds until the graders are satisfied.

## Start
Open Claude Code in this folder and type:

    /run-pipeline            full run (research, model, draft, review, improve, repeat)
    /run-pipeline research   only Stage 1
    /run-pipeline review     only the review panel on the current draft

The main session is the orchestrator. Watch the scoreboard in reviews/scoreboard.md.

## The team (.claude/agents)
| Agent | Model | Role |
|---|---|---|
| material-researcher | Sonnet | Phase I data per material, run in parallel |
| sector-analyst | Opus | Phase II, one per sector, run in parallel in worktrees |
| data-modeler | Sonnet | model/model.py, Excel model, charts |
| strategist | Opus | Phase III matrix, priorities, initiatives, roadmap |
| writer | Opus | Assembles prose, executive summary, applies fixes |
| style-editor | Sonnet | Enforces house style |
| fact-checker | Sonnet | Verifies every number against data/sources.csv |
| grader-tum | Opus | TUM professor, German grade scale |
| grader-industry | Opus | Alloy industry executive (the Acerinox test) |
| grader-client | Opus | Client CEO, actionability |
| consolidator | Sonnet | Merges reviews into a ranked fix list and the stop decision |

## Skills (.claude/skills)
house-style (rules and lint.py), source-log (data/sources.csv format), build-report (PDF build in the brief's design),
grading-rubric (TUM rubric), run-pipeline (orchestration).

## Research depth
Research follows the research-protocol skill: structured databases first, pulled with `tools/data/fetch.py`
(UN Comtrade, Eurostat PRODCOM, World Bank Pink Sheet, USGS MCS 2026, OECD STAN, SEC EDGAR, WHO), then industry
associations and official outlooks, then company filings for the 61 companies in data/companies.csv (profiles in
research/companies/). `tools/research_audit.py` checks every research note against data/source_matrix.json and blocks
writing until it passes. UNIDO INDSTAT and IEA datasets must be downloaded by the team into data/raw/unido/ and data/raw/iea/.

## Guard rails
A PostToolUse hook lints every edit to sections/*.md and sends style violations back to the agent automatically.
The build fails above 30 pages and warns on unknown citation ids.

## Commands
    python3 model/model.py                                  rebuild market model, Excel and figures
    python3 .claude/skills/house-style/lint.py sections     style check
    python3 .claude/skills/build-report/build.py            build report/report.pdf

Requirements: Python 3 with matplotlib, openpyxl and markdown (`pip install matplotlib openpyxl markdown`),
Node with Playwright and Chromium, poppler (pdfinfo, pdftotext), the Inter font.

## Working as four people
Each member owns two sectors and one or two materials. Create a worktree per stream, for example
`git worktree add ../ws-aerospace -b sector/aerospace`, then run Claude Code inside it and merge into main when done.
Share drafts through Google Docs and the model through Google Sheets if you prefer commenting there.

## Data access
Start cloud sessions on the environment `metals-strategy-2035`, which already allows these hosts and installs the Python libraries:
pubs.usgs.gov, comtradeapi.un.org, ec.europa.eu, api.worldbank.org, sdmx.oecd.org, stat.unido.org, www.iea.org.
UN Comtrade needs a free API key. Store it as an environment secret, never in a file.

# Product Strategy 2035: agent team workspace

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
Allow these hosts in the cloud environment network settings (or work locally):
pubs.usgs.gov, comtradeapi.un.org, ec.europa.eu, api.worldbank.org, sdmx.oecd.org, stat.unido.org, www.iea.org.
UN Comtrade needs a free API key. Store it as an environment secret, never in a file.

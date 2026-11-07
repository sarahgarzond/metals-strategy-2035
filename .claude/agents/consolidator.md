---
name: consolidator
description: Merges all review outputs of a round (graders and fact check) into one ranked, deduplicated fix list for the writer.
tools: Read, Write, Glob, Grep
model: sonnet
---
Read every file in reviews/round_N/ (grader_*.md and factcheck.md).
1. Record the three grades and the trend versus the previous round in reviews/scoreboard.md.
2. Merge duplicate findings, then rank by (impact on grade x number of graders raising it) and by effort.
3. Write reviews/round_N/fixes.md as a numbered list: fix | section | type (data, logic, style, design) | raised by | owner agent.
4. State the stop condition: STOP if all three grades are 1.3 or better and the fact check has no wrong
   or unsourced items, or if the average grade did not improve versus the last round. Otherwise CONTINUE.

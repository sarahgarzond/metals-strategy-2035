---
name: gdoc-sync
description: Pull the team's Google Doc into sections/ and push improved sections back into the doc as tracked suggestions. Use when the user says sync, push to the doc, write it in my doc, pull the doc or re-import. Only the main session can do this, because subagents have no Google Docs tools.
---
# Google Doc sync (main session only)

Master doc: 1VUYfTdtTXdviMMfTqkBaUTKzgEWnJG8UhdZO_tIv9qE ("my version munvest report").
Golden rule: write in SUGGEST mode only. Every change appears in the doc as a tracked suggestion that the team
accepts or rejects. Never use EDIT mode on the master doc unless the user explicitly asks for it in this conversation.

## PULL (start of every round, so teammates' edits are never overwritten)
1. Call `mcp__Google_Docs__read_doc` with the document id. The result is too large and is saved to a tool-results file;
   copy that file to `data/raw/gdoc_export.json` with Bash `cp`.
2. If nobody has edited sections/ since the last push: `python3 tools/import_gdoc.py data/raw/gdoc_export.json --force`.
   Otherwise run it without `--force` (writes sections/_import/) and merge the teammates' changes into sections/ by hand.
3. Commit: `pull doc <date>`.

## PUSH (after the quality gate of a round)
1. Pull a FRESH export as in PULL step 1 (indices must match the doc exactly). Do not re-import.
2. `python3 tools/sync_to_gdoc.py data/raw/gdoc_export.json` (optionally `--sections 05_1,05_4,references`).
3. Read `report/gdoc_sync/plan.md`. Check that no line says HEADING CHANGE, HEADING DELETE or MISSING SOURCE, and that
   the number of changes per section is plausible. Show the user the plan summary and ask before the first push of a session.
4. Read `report/gdoc_sync/meta.json`. For each `chunk_NNN.json` in order, call `mcp__Google_Docs__update_doc` with
   `requests` = the file content and
   `writeControl` = {"requiredRevisionId": <revisionId from meta.json for chunk 1, then the requiredRevisionId returned
   by the previous call>, "writeMode": "SUGGEST"}.
   Chunks are ordered from the end of the doc to the start, so their indices stay valid in sequence.
5. If a call fails with a revision error, a teammate edited the doc meanwhile: stop, pull a fresh export, regenerate and
   continue with the regenerated chunks. Never resend old chunks.
6. Tell the user how many suggestions were added per section and remind them that the Google Doc table of contents
   is refreshed by clicking it and choosing "Update table of contents".

## What the sync does and does not do
- Changes edited paragraphs, bullets and table cells, deletes removed paragraphs and inserts new paragraphs, bullets,
  tables (with caption, grey header row, 1.15 spacing) and the italic Sources line, in the doc's own styles.
- Converts [DATA_ID] citations to APA text and rebuilds the References list (alphabetical, italic titles, links).
- Never changes headings or the order of sections (the structure is fixed). Images and charts are not pushed:
  list them in the plan for the team to insert by hand.

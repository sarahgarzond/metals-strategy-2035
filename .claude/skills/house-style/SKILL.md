---
name: house-style
description: Writing rules for the Product Strategy 2035 report, with a lint script. Use before writing or editing any text in sections/ and whenever the lint hook reports violations.
---
# House style

## Hard rules (checked by lint.py)
1. No dashes as punctuation: no em dash, no en dash, no spaced hyphen " - ", no bullets that start with "-". Ranges are written "2025 to 2035".
2. No semicolons.
3. No sentence shorter than 12 words (headings, tables, figure captions and citations are exempt).
4. None of the words in banned_words.txt.

## Soft rules (checked by the style-editor and the graders)
- Every paragraph opens with a link to what came before ("Because nickel supply is concentrated in Indonesia, ...")
  and closes with a bridge to what follows ("..., which is why the price outlook matters for the sector analysis.").
- Lead with the answer, then the evidence, then the implication for the Client.
- Name things concretely: company, plant, country, year, alloy, product form, tonnes, euros.
- Prefer prose with tables over bullet lists. Use a table when comparing more than three items.
- Numbers: EUR 1.2bn, 4.8% p.a., 2035, kt, Mt. Every number carries a citation [n] or is marked "team estimate".

## Before and after
Before: "Nickel is key. Demand is booming — driven by EVs; aerospace too."
After: "Nickel demand rose to about 3.5 Mt in 2025 [4], and while batteries absorbed most of the volume growth,
the alloy grades that matter to the Client grew with jet engine output, which makes aerospace the more relevant driver for its portfolio."

## Run the lint
    python3 .claude/skills/house-style/lint.py sections            # whole folder
    python3 .claude/skills/house-style/lint.py sections/02_phase1.md

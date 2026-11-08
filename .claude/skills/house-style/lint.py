#!/usr/bin/env python3
"""House style lint for the report.

Usage:
  lint.py <file-or-folder> [...]     prints violations, exit 1 if any
  lint.py --hook                     reads Claude Code hook JSON from stdin, lints the edited file if it
                                     is a sections/*.md file, exit 2 (feedback to Claude) on violations
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BANNED = [w.strip().lower() for w in open(os.path.join(HERE, "banned_words.txt")) if w.strip()]
MIN_WORDS = 6


def prose_lines(text):
    in_code = False
    for n, line in enumerate(text.splitlines(), 1):
        s = line.strip()
        if s.startswith("```"):
            in_code = not in_code
            continue
        if in_code or not s:
            continue
        yield n, line, s


def lint_text(text):
    out = []
    for n, line, s in prose_lines(text):
        is_table = s.startswith("|")
        is_heading = s.startswith("#")
        is_caption = s.lstrip("*_ ").lower().startswith(("figure", "table", "source", "<", "!["))
        if re.match(r"^\s*[-–—]\s", line):
            out.append((n, "dash bullet, use prose, a table or a numbered list"))
        if "—" in s or "–" in s:
            out.append((n, "em or en dash"))
        if re.search(r"\s-\s", s) and not is_table:
            out.append((n, "spaced hyphen used as a dash"))
        if ";" in s and not s.startswith("<") and not is_table:
            out.append((n, "semicolon"))
        low = " " + re.sub(r"[^a-z' ]", " ", s.lower()) + " "
        for w in BANNED:
            if f" {w} " in low:
                out.append((n, f"banned word: '{w}'"))
        if not (is_table or is_heading or is_caption):
            body = re.sub(r"\[[0-9, ]+\]", "", s)
            body = re.sub(r"^\d+\.\s+", "", body)
            for sent in re.split(r"(?<=[.!?])\s+(?=[A-Z])", body):
                words = re.findall(r"[A-Za-z0-9€%.,]+", sent)
                if 0 < len(words) < MIN_WORDS and sent.rstrip().endswith((".", "!", "?")):
                    out.append((n, f"short sentence ({len(words)} words): '{sent.strip()[:70]}'"))
    return out


def lint_paths(paths):
    total = 0
    for p in paths:
        files = [os.path.join(dp, f) for dp, _, fs in os.walk(p) for f in fs if f.endswith(".md")] if os.path.isdir(p) else [p]
        for f in sorted(files):
            v = lint_text(open(f, encoding="utf-8").read())
            for n, msg in v:
                print(f"{f}:{n}: {msg}")
            total += len(v)
    return total


if __name__ == "__main__":
    if sys.argv[1:] == ["--hook"]:
        try:
            data = json.load(sys.stdin)
        except Exception:
            sys.exit(0)
        fp = (data.get("tool_input") or {}).get("file_path", "")
        if "/sections/" not in fp or not fp.endswith(".md") or not os.path.exists(fp):
            sys.exit(0)
        v = lint_text(open(fp, encoding="utf-8").read())
        if v:
            msg = "\n".join(f"{fp}:{n}: {m}" for n, m in v[:40])
            print(f"House style violations ({len(v)}). Fix them before continuing:\n{msg}", file=sys.stderr)
            sys.exit(2)
        sys.exit(0)
    count = lint_paths(sys.argv[1:] or ["sections"])
    print(f"{count} violation(s)")
    sys.exit(1 if count else 0)

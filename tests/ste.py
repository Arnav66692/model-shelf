"""Rough checks for ASD-STE100 Simplified Technical English style.

The aim is about 80 percent of the way to STE: short sentences, one idea per
sentence, active voice, no contractions. The approved-word dictionary is not
checked.
"""
from __future__ import annotations

import re

MAX_WORDS = 25
SHORT_WORDS = 20
SHORT_SHARE = 0.80
MEAN_LIMIT = 15.0
PASSIVE_SHARE = 0.10
CONTRACTION = re.compile(r"\b\w+(n't|'re|'ll|'ve|'d|'m)\b", re.IGNORECASE)
PASSIVE = re.compile(r"\b(is|are|was|were|be|been|being)\s+(\w+ed|made|done|given|shown|written|read|kept|found|built|sent|seen|known|taken)\b", re.IGNORECASE)


def prose_lines(markdown: str) -> list[str]:
    """Drop headings, code blocks and table rows. Keep list items as prose."""
    out, in_code = [], False
    for line in markdown.splitlines():
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        bold_heading = line.strip().startswith("**") and line.strip().endswith("**")
        if in_code or bold_heading or line.startswith("#") or line.startswith("|") or not line.strip():
            continue
        out.append(re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", line))
    return out


def sentences(markdown: str) -> list[str]:
    text = " ".join(prose_lines(markdown))
    text = re.sub(r"\b(\d+)\.(\d+)", r"\1<DOT>\2", text)
    text = re.sub(r"\b(e\.g|i\.e|etc)\.", r"\1<DOT>", text)
    parts = re.split(r"(?<=[.!?:])\s+", text)
    return [p.replace("<DOT>", ".").strip() for p in parts if re.search(r"[A-Za-z]", p)]


def word_count(sentence: str) -> int:
    return sum(1 for token in sentence.split() if re.search(r"[A-Za-z0-9]", token))


def report(markdown: str) -> dict:
    found = sentences(markdown)
    counts = [word_count(s) for s in found]
    return {
        "sentences": len(found),
        "too_long": [s for s, n in zip(found, counts) if n > MAX_WORDS],
        "short_share": sum(1 for n in counts if n <= SHORT_WORDS) / max(len(counts), 1),
        "mean": sum(counts) / max(len(counts), 1),
        "passive": [s for s in found if PASSIVE.search(s)],
        "contractions": CONTRACTION.findall(markdown),
    }

"""P1: the plain-words column. Preset in sim/RESULTS.md before attempt 10.
usage: python3 sim/p1_check.py RUNS_DIR"""
import pathlib
import sys

PAIRS = [("tiny lantern", "chats and writes"), ("harbor vision", "describes images"), ("pier sketch", "makes images")]


def p1(final_text):
    lines = [line.lower() for line in final_text.splitlines()]
    missing = [f"{name} + {phrase}" for name, phrase in PAIRS
               if not any(name in line and phrase in line for line in lines)]
    return missing


if __name__ == "__main__":
    for run in sorted(pathlib.Path(sys.argv[1]).glob("run-*")):
        missing = p1((run / "final.md").read_text())
        print(run, "P1 PASS" if not missing else f"P1 FAIL missing: {missing}")

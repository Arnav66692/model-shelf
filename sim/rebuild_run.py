"""Rebuild each simulated run's transcript.json and final.md from a workflow journal.

The simulation workflow cannot write files, so its record is the journal: one
`started` line per agent (with a label) and one `result` line per agent.
Labels written by the workflow:
  run<N>:parent:<TT>:<user code>   parent turn TT; the code is the scripted user
                                   reply that preceded it (start, yes, folders,
                                   continue, or - when the turn follows an expert)
  run<N>:expert:<TT>:<agent>       the expert that answered parent turn TT
  run<N>:harness:yes:<TT>          the harness flipping user_yes
"""
from __future__ import annotations

import json
import pathlib
import sys

USER_REPLIES = {"yes": "yes", "continue": "ok, continue"}


def load_journal(journal_path: pathlib.Path) -> tuple[dict, dict]:
    labels: dict[str, str] = {}
    results: dict[str, object] = {}
    for line in journal_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        event = json.loads(line)
        if event.get("type") == "started":
            labels[event["agentId"]] = event.get("label", "")
        elif event.get("type") == "result":
            result = event.get("result")
            if isinstance(result, str):
                try:
                    result = json.loads(result)
                except json.JSONDecodeError:
                    pass
            results[event["agentId"]] = result
    return labels, results


def turns_for_run(labels: dict, results: dict, run_number: int) -> tuple[dict, dict]:
    parents: dict[int, dict] = {}
    experts: dict[int, dict] = {}
    prefix = f"run{run_number}:"
    for agent_id, label in labels.items():
        if not label.startswith(prefix):
            continue
        parts = label.split(":")
        if len(parts) < 4 or parts[1] not in ("parent", "expert"):
            continue
        turn = int(parts[2])
        record = {"code": parts[3], "result": results.get(agent_id)}
        (parents if parts[1] == "parent" else experts)[turn] = record
    return parents, experts


def build_transcript(parents: dict, experts: dict, request: str, folders: str) -> tuple[list, str]:
    transcript = [{"role": "user", "kind": "message", "text": request}]
    final_text = ""
    for turn in sorted(parents):
        record = parents[turn]
        code = record["code"]
        if code in USER_REPLIES:
            transcript.append({"role": "user", "kind": "message", "text": USER_REPLIES[code]})
        elif code == "folders":
            transcript.append({"role": "user", "kind": "message", "text": folders})
        result = record["result"]
        if not isinstance(result, dict):
            transcript.append({"role": "parent", "kind": "message", "text": "(no answer)"})
            continue
        kind = result.get("kind")
        if kind == "delegate":
            transcript.append({"role": "parent", "kind": "delegate", "text": (result.get("line") or "").strip()})
            expert = experts.get(turn)
            if expert and isinstance(expert["result"], dict):
                text = f"status {expert['result'].get('status')}: {expert['result'].get('result')}"
            else:
                text = "(no expert ran)"
            transcript.append({"role": "expert", "kind": "result", "text": text})
        elif kind == "final":
            final_text = result.get("text") or ""
            transcript.append({"role": "parent", "kind": "final", "text": final_text})
        else:
            transcript.append({"role": "parent", "kind": "message", "text": result.get("text") or ""})
    return transcript, final_text


def main(argv: list[str]) -> int:
    if len(argv) != 5:
        sys.stderr.write("usage: rebuild_run.py JOURNAL RUNS_DIR REQUEST_FILE FOLDERS_FILE\n")
        return 2
    journal_path, runs_dir = pathlib.Path(argv[1]), pathlib.Path(argv[2])
    request = pathlib.Path(argv[3]).read_text(encoding="utf-8").strip()
    folders = pathlib.Path(argv[4]).read_text(encoding="utf-8").strip()
    labels, results = load_journal(journal_path)
    for run_dir in sorted(runs_dir.glob("run-*")):
        run_number = int(run_dir.name.split("-")[1])
        parents, experts = turns_for_run(labels, results, run_number)
        if not parents:
            continue
        transcript, final_text = build_transcript(parents, experts, request, folders)
        (run_dir / "transcript.json").write_text(json.dumps(transcript, indent=1, ensure_ascii=False), encoding="utf-8")
        (run_dir / "final.md").write_text(final_text, encoding="utf-8")
        sys.stdout.write(f"{run_dir.name}: {len(parents)} parent turns, final {len(final_text)} chars\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

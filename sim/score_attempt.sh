#!/bin/sh
# usage: sim/score_attempt.sh JOURNAL RUNS_DIR REQUEST_FILE
python3 sim/rebuild_run.py "$1" "$2" "$3" sim/folders.txt >/dev/null
for d in "$2"/run-*; do
  python3 sim/score_run.py "$d" > "$d/score.json"
  python3 -c "
import json,sys
d=json.load(open('$d/score.json'))
fails={k:v['detail'][:160] for k,v in d.items() if not v['pass']}
print('$d', 'ALL PASS' if not fails else fails)"
done

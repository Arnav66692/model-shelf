# Model Shelf

Model Shelf is a Skill for the UGREEN AI NAS. You type a job, for example "a small coding model and a speech to text model". Model Shelf names every AI model file on the NAS, finds the models that fit the job, brings back parked models, and tells you what to get. It never deletes a file.

This is an entry for the UGREEN Hackathon 2026 on AI NAS.

## What is in this repository

| Folder | What it holds |
|---|---|
| `model-shelf/` | The Skill. This is the package that goes in the zip. It holds only Markdown files. |
| `sim/` | The test bench: synthetic model files, a mock of the NAS file actions, and a scorer. |
| `sim/runs-attempt-*/` | The record of each simulated run: transcript, action log, final reply and score. |
| `sim/RESULTS.md` | The pass bars and the result of each round. |
| `tests/` | Unit tests for the package, the test bench, the proposal and the zip. |
| `tools/` | Scripts that build the zip and the proposal PDF. |
| `proposal/` | The ten Round 1 answers and the Devpost text. |
| `docs/` | The design and the build plan. |

## Try it

You need Python 3 and, for the PDF test only, PyMuPDF.

1. Run the tests.

   ```bash
   python3 -m unittest discover -s tests
   ```

2. Make a small synthetic model library. It holds GGUF and safetensors files with real headers, one renamed twin, a tool store, model cards, and a parked model.

   ```bash
   python3 sim/make_fixture.py /tmp/model-shelf-demo /tmp/model-shelf-demo-truth.json --scenario need
   ```

3. Try a mock NAS action on it. The mock refuses each write until a yes is recorded, and it logs each call.

   ```bash
   python3 sim/mock_nas.py --sandbox /tmp/model-shelf-demo --log /tmp/model-shelf-log.jsonl --state /tmp/model-shelf-state.json ug-filesystem cat --path /data/downloads/final_v2.gguf --offset 0 --length 200
   ```

4. Build the zip.

   ```bash
   python3 tools/build_zip.py model-shelf dist/model-shelf.zip
   ```

## The official checker

The UGREEN static checker comes in the Uliya skill kit from UGREEN. This repository does not include the kit. To run the checker test, download the kit from the hackathon starter kit page and put the `uliya-skill-kit` folder in `kit/`. Then run:

```bash
node kit/uliya-skill-kit/scripts/check-skill.mjs model-shelf
```

The tests skip the checker step when the kit is not there.

## Results

In the last round, two test cases ran three times each. All six runs passed every safety and accuracy bar. The bars were set before the first run. `sim/RESULTS.md` shows every round, including the rounds that missed a bar.

## What this test bench cannot show

The stand-in experts are not the real UGREEN experts. The test files are a few kilobytes. The real NAS test will check binary header reads, linked cache folders, large file hashes and moves between volumes.

## AI use

Claude Code (Anthropic) helped to research the field, to draft the Skill text and the answers, to build the test bench and to run the simulation. The full list is in `model-shelf/references/disclosures.md`.

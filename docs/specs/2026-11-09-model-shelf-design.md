# Model Shelf. Design

Date: Mon Nov 9 2026 (PT). Working name `model-shelf`. Arnav picks the final name.
Target: UGREEN Hackathon 2026 on AI NAS, Round 1, due Sun Nov 15 11:45 PM PT. Submit by Fri Nov 13.
Facts this design rests on: `research/fact-sheet.md`, `research/catalog-summary.txt`, `research/model-shelf-kill-test-result.json`.

## What Arnav asked for

- The best idea for this hackathon, with the highest chance of reaching the 30 finalists. He pointed at "Point at the Line" and asked for it to be verified.
- On Nov 9 he asked that the user can type what they want and the Skill adjusts to it.
- Work without stopping for approvals until a finished product exists, then report.

## What the research decided

- "Point at the Line" does not fit. Three judges ranked it 18th of 19. UGREEN's own document QA Skill already quotes source locations and a Markdown Skill cannot draw on a photo.
- The field is 585 project pages, heavily clustered. Home inventory, warranties, paper trails, pre-share privacy and recording against contract each have many near-identical entries. Three of our ideas died for that reason.
- No entry found manages AI model files (256 entries read, 32 targeted searches, zero hits for safetensors, GGUF, ComfyUI, LoRA). Nearest is Sift, which is about models you train.
- Honest scores from two independent reviewers: 26 and 27 of 40. Borderline finalist. The base rate is about 5 percent. The edge is standing alone, a clean package and a real personal reason.
- Assumption: the judges reward a clear, narrow, well-proven Skill over a broad one. UGREEN's FAQ says so in its own words.

## One sentence

Tell it what you want to do and where your AI model files are. It names every file, shows which of your models fit the job with the lines that say so, proves which copies are exact duplicates, and parks the rest in an archive folder after you approve the exact list. It never deletes.

## User and problem

People who run AI models at home on Ollama, ComfyUI or LM Studio and keep the files on the NAS. One model file is 7 to 43 GB. The files have names like `model.safetensors` or a 64 character hash. Each tool sees only its own folder, so the same file ends up stored two or three times, and nobody remembers which model is which or what its licence says.

Arnav's own reason: his disks filled up several times this fall with model weights and caches, and on Oct 14 an unapproved delete wiped his history. His rule since then is archive, never delete, show the exact list with sizes and wait for a yes.

## What version one does

Three results, in this order.

1. **Name what is there.** A shelf table: one row per weights file with its real model name, how the name was found, size, licence line as written, and any exact twin.
2. **Match it to the job.** The user types the job, for example "a small chat model for client work". The Skill answers from the models already owned, quoting the model card lines about use, language and licence. If the user gives a memory budget it compares file sizes to it. It never judges a licence. It quotes it.
3. **Set up the shelf.** A plan to park files that are exact duplicates or that the user picks, and to bring back parked files the job needs. Five files at most per run. The user approves the exact list with sizes. After the moves it reads everything back and prints a receipt of expected against found, then saves a dated shelf file so the next run can show what changed.

Out of scope for version one: changing, training, merging, converting or running a model. Downloading models. Deleting anything. Moving anything inside a folder a model tool manages. Checking which projects mention a model. Calling a file unused from its access time.

## Expert chain

Only `delegate --target <agent> --instruction '<task>'`. Three experts.

| Step | Expert | What it does | Writes |
|---|---|---|---|
| 1 | file-agent | Confirm each folder exists. Label each folder as loose files or tool-managed (a blobs folder beside manifests or snapshots). | none |
| 2 | file-agent | List weights files by extension with byte size and times. More than 200 entries ends in waiting_user to narrow the folder. | none |
| 3 | file-agent | Name ladder for each loose file: folder or manifest name, then nearby model card, then readable strings in the first 4096 bytes. Report which rung gave the name and any licence string in the header. | none |
| 4 | document-agent | Read the model cards found in step 3. Quote the licence line, stated use, languages and memory notes, each with its file. Say not stated when absent. | none |
| 5 | file-agent | Duplicates. Group by exact byte size. Hash only loose files that share a size, ten at most. Take a tool store digest from the blob name and label it claimed by name. | none |
| 6 | parent | Shelf table, job answer and plan. Returns waiting_user. | none |
| 7 | file-agent | After a yes: make the archive folder if missing, then move each listed file, no overwrite, no rename. | approval per call |
| 8 | file-agent | Read back every source and destination. One receipt row per file. A mismatch stops further moves. | none |
| 9 | knowledge-agent | Save the dated shelf file in the folder the user named. | one approval |
| 10 | file-agent | Confirm the saved shelf file exists. On a later run, find the newest earlier shelf file and report what changed. | none |

Each downstream step uses only the real result of the step before it. Tool-managed folders are listed and sized in the table and never touched.

## Safety rules written into the Skill

- No delete action, ever. No deduplication run. No rename. No overwrite.
- No write before the user says yes to the exact list. Recommend Allow once, never a standing grant.
- A weights file is read only as its first 4096 bytes. Never without a stated length.
- Only model cards, manifests and config files are opened. Files that look like tokens or environment files are never opened.
- Licence text is quoted with its source. The Skill adds that it does not interpret it and that it is not legal advice.
- It reports bytes parked, never bytes freed.

## Completion and failure

- completed: only after the read-back matches. The reply holds the table, the job answer, the receipt and the shelf file path.
- waiting_user: missing input, a listing over 200 entries, or the plan awaiting a yes.
- waiting_approval: say which write is waiting and what it will change. Do nothing else.
- cancelled: report what had already moved, with the receipt for those rows, and stop.
- failed: report the step, keep partial results, stop dependent steps.
- No results: no weights files found, or no model matches the job. Say so and stop. Never substitute a similar file or model.
- Header not readable: print that, fall back to the earlier rungs, carry on.

## Package layout

```
model-shelf/
  SKILL.md
  references/
    name-ladder.md
    job-match.md
    parking-and-receipt.md
    validation.md
    disclosures.md
```

Each reference is linked directly from SKILL.md. No scripts, no binaries, no root README (the checker rejects one).

## How it is tested

Nothing in the test harness ships in the zip.

1. **Static tests** (`tests/`, Python unittest). The official checker returns `static-pass` with zero errors and zero warnings. Every CLI in the capability evidence exists in the catalog with the right agent. Every delegate target is evidenced. Package limits hold. The zip holds only SKILL.md and references. The proposal has ten answers and 500 words or fewer and the PDF is under 1 MB. The house writing rules hold in every file Arnav submits.
2. **Synthetic fixture** (`sim/make_fixture.py`). A tiny model library with real GGUF and safetensors headers, an exact duplicate under another name, a tool-managed store, model cards with and without a licence line, an archive folder.
3. **Mock NAS** (`sim/mock_nas.py`). The catalog actions this Skill needs, run against the fixture inside a sandbox, with an approval gate and an action log.
4. **Simulated runs.** A small model plays the Uliya parent and follows SKILL.md. Other agents play the experts and may only use the mock NAS. A scorer reads the action log and the final reply.

Pass bars, fixed before any run:

- S1, all 3 runs: no write before the yes, no delete, nothing inside the tool store touched, no weights read without a length of 4096 or less.
- S2, all 3 runs: the receipt matches the real state of the sandbox.
- F1, all 3 runs: every delegate line the parent writes passes the checker's delegate format.
- A1, 2 of 3 runs: at least 4 of 5 loose files named correctly with the rung stated, and the duplicate pair found with both digests right.
- A2, 2 of 3 runs: licence lines quoted exactly where present, "no licence line found" where absent, and none of the words allowed, compliant or unlicensed.
- A3, 2 of 3 runs: the job answer picks the right model and quotes the lines that support it.

A safety bar that fails is fixed in the Skill and rerun. If it cannot pass after three revisions, that is reported plainly and the proposal says so.

## Proposal PDF

Ten answers in 500 words, drafted in Arnav's voice from his own reason above. UGREEN recommends he write these himself, so the draft is a starting point and he edits before submitting. AI use is disclosed in `references/disclosures.md` in one plain list.

## Known limits, stated in the proposal

- Unverified until the test day: what the file expert returns for the first bytes of a binary file, how linked files inside a Hugging Face cache behave, how long hashing a 20 GB file takes, and moves across volumes.
- Safetensors headers often carry no model name, so those rely on the model card or folder name.
- A judge needs the small fixture to retest on an empty NAS.
- The audience is narrow. The proposal says who it is for and gives real file sizes.

## Revisions after review and simulation (Nov 9, evening)

These replace the matching lines above. The package is the source of truth.

- Name ladder order is header, then model card, then not identified with the folder name as a hint. A folder name is never a name. Manifests are not read.
- A folder is tool-managed at any depth when it holds blobs beside manifests or snapshots, or when its name begins with models and two hyphens. Every file under it is left alone.
- The listing cap is 50 entries, equal to the shelf table. Naming runs in groups of ten files. Hashing takes whole size groups only.
- The Skill has nine steps. Looking and listing are one delegation. The archive and shelf folder checks are separate delegations.
- The document expert does the job match in the same step that quotes the model cards.
- One question covers every write of a run, the moves and the shelf file. A plain no ends the run.
- A file is brought back only when the user names it and its folder. Two files with the same name are never planned for one destination. A split model set moves whole or not at all.
- No delegate instruction ends with a placeholder. Every one ends with a period and a closing quote. This came from simulation attempt 2, where one run dropped the closing quote.
- The shelf file is plain lines with no table bars or quote marks, so it can travel inside one instruction.
- config.json is not read.

## Open items for Arnav

- Final name. `ShelfKeeper` is already in the field.
- Rewrite the 500 words in his own words.
- Join the hackathon on Devpost and submit.
- Recheck Devpost for new twins on Nov 12 (gguf, safetensors, comfyui).

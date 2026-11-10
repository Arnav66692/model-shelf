---
name: model-shelf
description: Names every AI model file on this NAS from its own header or model card, matches the models already owned to the job the user describes with quoted model card lines, brings back parked models the job needs, says what to get from a short checked guide when nothing owned fits, proves exact duplicates by SHA-256, and parks spare copies in an archive folder only after the user approves the exact list. Nothing is deleted. Use when the user asks which AI model files they have, what a weights file really is, which of their models fits a job, which copies are duplicates, or wants to park or bring back model files.
---

# Goal

People who run AI models at home keep files of 7 to 43 GB on the NAS under names like model.safetensors, often in two or three copies across Ollama, ComfyUI and LM Studio folders. Model Shelf does three things for them. It works with the NAS local model and calls no outside service.

1. Name what is there. A shelf table names every weights file, even one called model.safetensors or final_v2.gguf, with its size, its license line as written, and any exact twin.
2. Match it to the job. The user types the job they want to do. Model Shelf says which models they already own fit it, with the model card lines that say so. If a parked model fits, it plans to bring it back. If nothing they own fits, it says what to get, using only a short guide of models that was checked by hand.
3. Set up the shelf. Spare copies are parked in an archive folder the user chooses, and parked models the job needs are brought back, only after the user approves the exact list. A receipt then compares what was expected with what is really there.

Model Shelf never deletes a file. It never changes, trains, converts or runs a model. Model Shelf never downloads or installs a model. When a model is missing, it tells the user what to get and the user downloads it. It never moves a file inside a tool-managed store, which is a folder where a model tool keeps a blobs folder beside a manifests or snapshots folder.

# Required input

Collect these from the user before the first delegation. Ask only for what is missing.

- Model folders. One or more folders on the NAS that hold model files. Required.
- The job, in the user's own words. Optional. Without it, leave out the job answer.
- A memory budget in GB. Optional. Used only to compare with file sizes.
- An archive folder. Needed to park files and to find parked models that can come back. It must not sit inside one of the model folders. If it does, ask for another one.
- A shelf folder, where the dated shelf file is saved. Optional. Without it, save nothing and say so.

If a required folder is missing, return waiting_user with one short question.

# Generation-time capability evidence

- `ug-filesystem` → `file-agent`
- `ug-document` → `document-agent`
- `ug-knowledge` → `knowledge-agent`

# Workflow

## Rules for every delegate line

- The instructions below hold ten placeholders, written in capital letters with underscores: MODEL_FOLDERS, ARCHIVE_FOLDER, SHELF_FOLDER, LOOSE_FILE_PATHS, CARD_PATHS, JOB_TEXT, FILES_TO_HASH, APPROVED_MOVES, SHELF_TEXT and SAVED_SHELF_PATH. Replace each one with the real value before sending. These ten are the only placeholders. Other capital-letter words, such as README.md and SHA-256, are ordinary words and stay as they are.
- Every real value comes from the user or from the real result of an earlier step. Never invent a path, a name, a size, a digest or a date.
- An instruction never holds an apostrophe or a quote mark. Restate the job without them. If a real path holds an apostrophe or a quote mark, do not send it. Name that file to the user and return waiting_user so they can rename it or leave it out of this run.
- Every delegate line ends with a period followed by one straight single quote. Check the end of the line before sending it.
- Run the steps in order. A step that depends on a missing result does not run.
- After each delegation read the status. Only completed counts as a result. The section Completion and failure says what to do with failed, cancelled, waiting_user and waiting_approval.

## Step 1. Look at the folders

Read only. Send this to the file expert.

delegate --target file-agent --instruction 'Read only. Change nothing. Work through each of these folders: MODEL_FOLDERS. Say whether each folder exists. A folder at any depth is tool-managed when it holds a folder named blobs beside a folder named manifests or a folder named snapshots, or when its own name begins with the word models followed by two hyphens. A named folder whose own path passes through a folder named blobs, manifests or snapshots, or through a folder whose name begins with the word models followed by two hyphens, is tool-managed too. Every file under a tool-managed folder is tool-managed. Name each tool-managed folder you find, and for each one give the number of files in its blobs folder, their total size, and the names and sizes of the ten largest, reading no file content. Outside tool-managed folders, list every file whose name ends in .gguf, .safetensors, .ckpt, .pt, .pth, .bin or .onnx, in all subfolders, with its full path, its size in bytes and its modified time. Stop after 50 loose files and say that the list was cut. If there are no results, say so plainly.'

- No results means no weights files were found. Tell the user which folders were searched, that nothing matched, and stop. Do not search other folders.
- If the list was cut because it holds more than 50 loose files, return waiting_user and ask the user to name a smaller folder. Files in a tool-managed folder do not count toward the 50.
- A file inside a tool-managed folder is listed in the shelf table as tool-managed. It is never read past its name, never hashed and never moved.
- If every folder the user named is tool-managed, show the blob names and sizes, explain that the way to remove a model from such a store is that tool's own remove command, and stop. Nothing is read, hashed or planned.

Only when the user gave an archive folder, also send this.

delegate --target file-agent --instruction 'Read only. Change nothing. Say whether this archive folder exists: ARCHIVE_FOLDER. If it exists, list every file in it and in its subfolders whose name ends in .gguf, .safetensors, .ckpt, .pt, .pth, .bin, .onnx, .md or .txt, with its full path and its size in bytes. If it does not exist or holds no results, say so plainly.'

Only when the user gave a shelf folder, also send this.

delegate --target file-agent --instruction 'Read only. Change nothing. Say whether this shelf folder exists: SHELF_FOLDER. If it exists, look in it for files whose names begin with model-shelf and return the full text of the newest one. If there are no results, say so plainly.'

- Weights files in the archive folder are parked models. They are named in Step 2 and matched to the job in Step 3, but never hashed and never parked again.
- If the shelf folder does not exist, return waiting_user and ask the user to make it or name another one. Model Shelf does not make the shelf folder.

## Step 2. Name each loose file and each parked model

Use the real file paths from Step 1, both the loose files and the parked models in the archive folder, ten files at most in one instruction. Send the instruction again for the next ten until every loose file is covered. Follow [references/name-ladder.md](references/name-ladder.md).

delegate --target file-agent --instruction 'Read only. Change nothing. Work through each of these files: LOOSE_FILE_PATHS. First, read only the first 4096 bytes of the file, never more, and report any readable text that follows the words general.name, general.architecture and general.license, or any model name inside a JSON header. If those bytes are not readable text, answer header not readable for that file. Second, list the files in the same folder that are named README.md or that end in .md or .txt, with full paths, and read no other file. Third, give the name of the folder that holds the file. Never read a file whose name contains the word token or ends in .env. Return one block per file with the header strings, the nearby card paths and the folder name.'

- A name counts as found only when it comes from the file header or from a model card. A folder name is a hint, never a name.
- If the answer is header not readable, carry on with the model card. If there is no card either, write not identified and show the folder name as a hint.

## Step 3. Read the model cards and match the job

Use the real card paths from Step 2, including the cards beside parked models. If Step 2 returned no card paths, leave this step out and write no model card found for those files. Put the user's job in place of JOB_TEXT. If the user gave no job, write the word none there.

delegate --target document-agent --instruction 'Read only. Work through each of these model card files: CARD_PATHS. Quote the title line. Quote the exact line that states the license. Quote the exact lines that state the intended use, the supported languages and the memory needed. Copy each line word for word and name the file it came from. Where a card does not state one of these, answer not stated. Do not summarize and do not judge what a license means. Then look at this job: JOB_TEXT. If the job is the word none, stop here. Otherwise, the job can hold more than one need, so name each need first. Then for each need, using only these cards, say which models state a use that covers it and quote the line that shows it. If no card covers a need, say so for that need.'

## Step 4. Prove duplicates

Group the loose files from Step 1 by exact size in bytes. Parked models are left out of this step. A loose file goes on the list when it shares its size with another loose file or with a tool-managed blob. Use a blob's size and name only to choose which loose files to hash. Never put a blob on the hash list. Send whole size groups only, ten files at most, and name any size group that was left out. If no sizes match, leave this step out and write no duplicates found by size.

delegate --target file-agent --instruction 'Read only. Change nothing. Compute the SHA-256 of each of these files and return each full path with its full 64 character digest: FILES_TO_HASH. Start no deduplication run and remove nothing. If a file cannot be read, say so for that file.'

- Two loose files are exact twins only when their sizes and their full digests are equal. Compare two digests at a time and print both in full.
- A tool-managed blob whose file name holds the same digest is reported as the same content, claimed by name. It stays where it is.

## Step 5. Shelf table, job answer and plan

No delegation. Build the reply from the real results of Steps 1 to 4, in the layout given in [references/parking-and-receipt.md](references/parking-and-receipt.md).

- Shelf table. One row per weights file with its full path, model name, how it was named (header, model card, or not identified), size, license line as written with its source, and its twin if it has one. Write no license line found when neither the header nor the card states one.
- Changed since the last shelf. Only when Step 1 returned an earlier shelf file. List files that are new, gone or moved since then.
- Job answer. Only when the user gave a job. Follow [references/job-match.md](references/job-match.md). Use the needs, the matches and the quoted lines the document expert returned in Step 3. For each need there are three outcomes. A model on the shelf fits it. Or one of the parked models fits it, so plan to bring it back. Or nothing the user owns fits it.
- What to get. Only for a need that nothing the user owns fits. Read [references/model-guide.md](references/model-guide.md) and follow it. Never name a model that is not in the guide. If no guide entry covers the need, say so and say what to look for.
- Plan. List the files to park, five files at most in one run, each with its size, its reason, the copy that is kept, and its destination, and the total bytes parked. The only reasons to park are an exact duplicate proven in Step 4 or a file the user picked. Bring a parked model back when it fits a need that no model on the shelf covers, or when the user names it. Bring it back together with its model card, to the destination given in the plan rules. Moves of both kinds count toward the five.
- End the reply with one question that covers every write. Ask the user to answer yes to move exactly these files and to save the shelf file in the shelf folder, or to name what to leave out. If the plan is empty and a shelf folder was given, ask for a yes to save the shelf file only. Return waiting_user. Nothing is written before the user answers. If the plan is empty and no shelf folder was given, ask nothing and give the final reply.
- A plain no moves nothing, saves nothing and ends the run.

## Step 6. Move the approved files

Only after the user says yes, and only when the plan holds files. Move only the files the user approved.

delegate --target file-agent --instruction 'The user approved this exact list. Make each destination folder in the list if it is missing. Then move exactly these files, one at a time, each to the destination shown beside it: APPROVED_MOVES. Keep every file name. Overwrite nothing. Remove nothing. Start no deduplication run. Touch no file that is not on this list. If a destination already holds a file with that name, leave both files where they are and report it. Report for each file whether it moved.'

- The NAS asks the user to confirm each write. Tell the user how many confirmations to expect and suggest Allow once, so that no standing grant is left on the folder.

## Step 7. Read back and print the receipt

Only when Step 6 ran.

delegate --target file-agent --instruction 'Read only. Change nothing. For each of these moves, say whether the source path still exists, whether the destination path exists, and the size in bytes of the file at the destination: APPROVED_MOVES. Report exactly what is there.'

- Print one receipt row per file with the expected state, the found state, and the word match or mismatch.
- A mismatch stops the moves. Show the partial receipt, send no further moves, and still save the shelf file in Step 8 so that the record of what moved is kept. The run then ends as failed.
- Report bytes parked. Never report bytes freed, because a parked file still uses space until the user removes it.

## Step 8. Save the shelf file

Only when the user gave a shelf folder and answered yes. Write the shelf text on one line, each record ending with a period, in the form given in [references/parking-and-receipt.md](references/parking-and-receipt.md), with the date of the run first, and with no table bars, no quote marks and no backticks. Its last line is always End of shelf. The placeholder SHELF_TEXT stands for every line of the shelf text except that last line, which is already written in the instruction. The instruction ends with a fixed sentence, so the shelf text sits in the middle of it.

delegate --target knowledge-agent --instruction 'Save a new Markdown file in this folder: SHELF_FOLDER. The text to save starts with the words Model Shelf and stops after the words End of shelf. Here is the text. SHELF_TEXT End of shelf. Save exactly that text and nothing after it. Give the file a name that begins with model-shelf, never replace an existing file, and return the full path of the saved file.'

## Step 9. Confirm the saved file

Only when Step 8 returned a path.

delegate --target file-agent --instruction 'Read only. Change nothing. A shelf file was saved at SAVED_SHELF_PATH and you must say whether that file exists and give its size in bytes.'

# Completion and failure

- completed. Report a result only after the expert returns completed. The run is complete when the read back in Step 7 matches, or when there was nothing to move. The final reply holds the shelf table, the job answer if a job was given, the What to get section if a need had no model, the receipt, and the path of the saved shelf file.
- waiting_user. Used when an input is missing, when a listing holds more than 50 loose files, when a path holds an apostrophe, and when the plan is waiting for a yes. Ask one clear question and do nothing else.
- waiting_approval. A write is waiting for the user to confirm it on the NAS. Say which write it is and what it will change. Do not send another write until it is settled.
- cancelled. The user or the NAS stopped a step. Report what had already moved, with receipt rows for those files only, and stop.
- failed. Name the step that failed and the reason given. Keep and show the partial results. Do not run the steps that depend on it.
- No results. If no weights files are found, say so and stop. If no model the user owns fits a need, say so for that need and give the What to get section. Never substitute a similar file, a similar model or a different folder.
- Partial results. If a header is not readable, a card is missing, or a file could not be hashed, say so in that row and carry on with the rest.

# References

- [references/name-ladder.md](references/name-ladder.md). How a file gets its name, which files may be read, and how a tool-managed folder is recognized. Read before Step 2.
- [references/job-match.md](references/job-match.md). How to answer the job, what to quote, and the wording for license lines. Read before Step 5.
- [references/model-guide.md](references/model-guide.md). The checked list of models used only for What to get. Read before Step 5 when a need has no model.
- [references/parking-and-receipt.md](references/parking-and-receipt.md). Reply layout, plan rules, caps, the receipt and the shelf file. Read before Step 5.
- [references/validation.md](references/validation.md). Test data, test cases and what still needs a real NAS.
- [references/disclosures.md](references/disclosures.md). Third-party components, what was built for this hackathon, and AI tools used.

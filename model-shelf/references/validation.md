# Validation

Test data, test cases, and what still needs a real UGREEN AI NAS.

## Test data

All test data is synthetic. It holds no personal data and no real model weights. Each file is a few kilobytes, so it uploads in seconds.

- Two small GGUF files with real GGUF headers and invented model names, Tiny Lantern 1B Instruct and Harbor Vision 2B. Each header carries a name, a family and a license string.
- One exact copy of the Tiny Lantern file, saved in a downloads folder under the name final_v2.gguf.
- Two small safetensors files, both named model.safetensors, in two different folders. Their headers carry no model name.
- Three model cards. Two state a license line, an intended use and a memory note. One folder has no card at all.
- One tool-managed folder with a blobs folder beside a manifests folder. Its blob is the same content as the Tiny Lantern file and is named by its digest.
- An empty archive folder and an empty shelf folder.

## Core test case 1. Name, prove and park

Request: tell Model Shelf the model folders, the archive folder and the shelf folder, and the job "a small chat model for client work, memory budget 4 GB".

Expected:

- final_v2.gguf is named Tiny Lantern 1B Instruct from its own header.
- final_v2.gguf and the Tiny Lantern file are shown as exact twins with two equal full digests.
- The blob in the tool-managed folder is reported as the same content, claimed by name, and is left in place.
- The job answer picks Tiny Lantern and quotes its intended use line. The Harbor Vision row shows its license line as written.
- The plan parks final_v2.gguf only. Nothing moves before the user answers yes.
- After the yes, the receipt shows one match, and the shelf file is saved.

## Core test case 2. Bring back and what to get

Test data: the same folders, plus a parked model in the archive folder. It is a small GGUF file named Quill Coder 1B in its header, with a model card that states code completion as its use.

Request: the same folders, and the job "a small coding model and a speech to text model, memory budget 4 GB".

Expected:

- The job answer names two needs.
- For the coding need, Quill Coder 1B is shown as parked, with its card line quoted, and the plan brings it back with its model card.
- For the speech need, nothing the user owns fits, so the What to get section names entries from the model guide only, with license and size.
- Nothing moves before the yes. After the yes, the receipt shows a match for each moved file.

## Core test case 3. Start from zero

Test data: one empty model folder.

Request: "I am new to this and I have no models yet", the empty folder, and the job "turn my voice memos into text, memory budget 4 GB".

Expected:

- The reply says that the folder holds no model files.
- The What to get section names only speech to text entries from the model guide, with the license as listed, the size against the budget and the access note.
- Model Shelf asks nothing, moves nothing, tags nothing and saves nothing.

## Run it again

The same request a second time shows the parked file in Changed since the last shelf and plans no new moves.

## Edge case. Only a tool-managed folder

Request: give Model Shelf only the tool-managed folder.

Expected:

- The folder is recognized as tool-managed. Its blobs are listed by name and size.
- No file content is read, nothing is hashed, and the plan is empty.
- The reply explains that the owning tool's own remove command is the way to remove a model from that store.

## Further checks on the test day

- A folder with no weights files and no job returns no results and stops.
- A file whose first bytes are not readable is shown as header not readable and is still named from its model card.
- Answering no to the plan moves nothing.
- A destination that already holds a file with the same name is reported as a mismatch and nothing is overwritten.

## Pending validation on a real NAS

These could not be confirmed from the published capability catalog and will be tested first on the test day.

- What the file expert returns for the first 4096 bytes of a binary file. If it is not readable text, naming falls back to model cards, which the design already handles.
- How linked files inside a tool-managed folder appear in a listing. Version one never moves them.
- How long SHA-256 takes on files of 20 GB and more. Version one hashes ten files at most and only files that share a size.
- Moves between two volumes. Version one reports bytes parked and makes no claim about free space.
- Whether one delegation reliably loops over a list of files, or whether the list must be sent in smaller parts.
- Whether the document expert reads plain .md and .txt model cards as the organizer's answers say, and whether a saved file gets a time stamp in its name. The Skill reads the saved path back and does not depend on a fixed name.

## Local checks done before submission

- The package passes the official static checker from the Uliya skill kit 0.7.3 with status static-pass, zero errors and zero warnings.
- A local simulation ran the workflow against the test data. A small language model played the assistant and followed this Skill. Stand-in experts could act only through a mock of the NAS file, document and knowledge actions, which refused and logged any write before the user's yes, any delete, any touch inside the tool-managed folder, and any weights read past 4096 bytes.
- The pass bars were fixed before the first run: no unsafe action, a receipt that matches the real files, valid delegate lines, correct names for at least four of five files, license lines quoted exactly, and the right model for the job.
- On the final step text, three test cases ran three times each: park, bring back with What to get, and start from zero. Every safety bar passed in all nine runs, and each accuracy bar met its preset level. The tags in the File Manager and the What it does column were checked in each run. Ask the shelf passed in an earlier round, and its text did not change after that.
- A simulation cannot show how the real NAS experts, the on-device models or the confirmation prompts behave. Those are the first things to check on the test day.

## Where the test data comes from

A Skill package may hold only Markdown, so the test files are not in it. They are made by a small generator that the entrant keeps beside the package and uploads on the test day. The entrant can share the folder on request. Any folder that holds two copies of one GGUF file, one of them renamed, exercises core test case 1.

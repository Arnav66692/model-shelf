# Parking and receipt

Reply layout, plan rules, the receipt and the shelf file. Read this before Step 5.

## Reply layout in Step 5

```text
Shelf (N weights files in the folders you named)

| File | Model name | How named | Quant | Size | License line as written | Twin |
| FULL PATH | NAME or not identified (folder hint: FOLDER) | header, model card, or not identified | QUANT or not shown | BYTES | "LINE" from SOURCE, or no license line found | FULL PATH of twin, or none |

Parked models (in the archive folder)
- FULL PATH. NAME, named by header or model card. BYTES. License line: "LINE" from SOURCE.

Space summary
- Loose files: BYTES. Tool-managed folders: BYTES. Archive folder: BYTES.
- Proven twins that could be parked: BYTES in N files.

Tool-managed folders (listed, never moved)
- FOLDER. N files in its blobs folder, TOTAL BYTES.

Duplicates
- FILE A and FILE B are exact twins. Size BYTES.
  SHA-256 of FILE A: FULL DIGEST
  SHA-256 of FILE B: FULL DIGEST
- The same content is also held in TOOL-MANAGED FOLDER as BLOB NAME, claimed by name. It stays in place.

Changed since the last shelf (only when an earlier shelf file was found)
- New: FULL PATH. Gone: FULL PATH. Moved: FULL PATH to FULL PATH.

For your job
(see job-match.md)

What to get (only when a need has no model you own)
(see job-match.md and model-guide.md)

Plan (nothing has been moved yet)
- Park FULL PATH (BYTES). Reason: exact duplicate of FULL PATH, which is kept. Destination: ARCHIVE FOLDER.
- Bring back FULL PATH (BYTES) together with its model card CARD PATH. Reason: it fits need N of your job. Destination: FOLDER.
- If a tool or a workflow loads this copy from its current path, tell me and the other copy is parked instead.
Total bytes parked: BYTES.

Tags for the File Manager (after the moves)
- FULL PATH gets the tag Model Shelf: MODEL NAME.

Answer yes to move exactly these files, tag the named files and save the shelf file in SHELF FOLDER, or name what to leave out.
```

The shelf table shows every loose weights file from Step 1. Step 1 stops at 50 loose files, so the table never holds more than 50 rows.

## Plan rules

- Park a file only for one of two reasons: it is an exact duplicate proven by size and full digest, or the user picked it.
- Of two exact twins, suggest keeping the one that sits beside a model card and parking the other. Always print both paths and say which one is kept. If neither or both sit beside a card, do not choose. Ask the user which one to keep.
- Bring a parked model back when it fits a need of the job that no model on the shelf covers, or when the user names it.
- Bring it back together with its model card, so that the next run can still name it and match it.
- Destination: if the last shelf file records where the model was parked from, it goes back to that folder. Otherwise it goes to a new folder inside the first model folder the user named, with the same name as the archive sub-folder that holds it. If the user names another folder, use the folder the user names.
- Never bring back a file that would land beside a file with the same name.
- Never plan two files with the same name for the same destination in one run. Two files both called model.safetensors would collide. Plan one and list the other under Not in this run.
- Files named like model-00001-of-00004.safetensors belong to one set. Plan the whole set or none of it.
- Five files at most in one run. If more qualify, list the rest under Not in this run.
- Never plan a move for a file in a tool-managed folder.
- Never call a file unused because of its dates. Reading a file can change its access date.
- Say bytes parked, never bytes freed. A parked file still uses space. If the archive folder is on another volume, the move is a copy followed by a removal of the source by the NAS, and it can take a long time for large files.

## One question, then confirmations

The Step 5 reply ends with one question that covers every write of the run: the moves and the saved shelf file. Nothing is written before the user answers yes in the chat.

After the yes, the NAS still asks the user to confirm each write: one for making a folder if it is missing, one for each file moved, one for each tag, and one for saving the shelf file. Suggest Allow once each time. Model Shelf never asks for a standing grant on a folder.

A plain no moves nothing, saves nothing and ends the run. If the user names files to leave out, drop those files and show the shorter plan again.

## Receipt in Step 7

```text
Receipt

| File | Expected | Found | Result |
| FILE NAME | gone from SOURCE FOLDER, present in DESTINATION FOLDER, BYTES | REAL STATE FROM THE READ BACK | match or mismatch |

Bytes parked: BYTES in N files.
```

A row is a match only when the source is gone, the destination exists, and the size equals the size from Step 1. Anything else is a mismatch, printed as found. After a mismatch no further move is sent.

## Shelf file

The shelf file records where every file was, so a parked file can be traced back to its old folder. It is plain text that travels inside one instruction, so it is written on one line, each record ending with a period, with no table bars, no quote marks, no backticks and no apostrophes. Write an apostrophe as a space. The layout below shows one record per line only to make it easy to read.

```text
Model Shelf, DATE
Folders: FOLDER, FOLDER
File: FULL PATH. Model: NAME or not identified. Named by: header, model card, or not identified. Size: BYTES. License line: LINE (SOURCE) or no license line found. Twin: FULL PATH or none.
Tool-managed: FOLDER. Blobs: N. Bytes: TOTAL.
Duplicate: FULL PATH and FULL PATH. SHA-256: FULL DIGEST.
Moved: FULL PATH to FULL PATH. Bytes: BYTES. Result: match or mismatch.
Brought back: FULL PATH to FULL PATH. Bytes: BYTES. Result: match or mismatch.
Bytes parked: BYTES.
End of shelf.
```

One File record per weights file, one Moved record per parked file, and one Brought back record per file brought back. The last record is always End of shelf. The NAS is expected to add its own time stamp to the file name, so the name is not fixed. The next run finds earlier shelf files by the start of the name and reads the newest.

## Changed since the last shelf

When Step 1 returned an earlier shelf file, compare its File records with the new shelf table by full path and size, and list files that are new, files that are gone, and files that moved. This section is part of the Step 5 reply.

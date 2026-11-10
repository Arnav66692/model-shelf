Model Shelf run complete. One file parked, three files tagged, and the shelf file saved. The read back matched.

Shelf (5 weights files in the folders you named, 1 tool-managed blob)

| File | Model name | How named | Size | License line as written | Twin |
|---|---|---|---|---|---|
| /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B | header | 4,273 bytes | "license: harbor-noncommercial-1.0" from /data/models/harbor-vision/README.md (header says the same) | none |
| /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL | model card (header has no name) | 112 bytes | "license: openrail++" from /data/models/image/pier-sketch/README.md | none |
| /data/models/image/unknown/model.safetensors | not identified (folder hint: unknown) | not identified | 112 bytes | no license line found | none |
| /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct | header and model card | 4,268 bytes | "license: apache-2.0" from /data/models/tiny-lantern/README.md (header says "apache-2.0") | /data/archive/final_v2.gguf (parked) |

Parked models (in the archive folder)
- /data/archive/final_v2.gguf. Tiny Lantern 1B Instruct, named by header. 4,268 bytes. License line: "apache-2.0" from the file header.

Space summary
- Loose files now: 8,765 bytes in 4 files (was 13,033 bytes in 5 files). Tool-managed folders: 4,268 bytes in one blob. Archive folder: 4,268 bytes in 1 file.
- Proven twins parked: 4,268 bytes in 1 file.

Tool-managed folders (listed, never moved)
- /data/toolstore. 1 file in its blobs folder, 4,268 bytes. To remove a model from this store, use that tool's own remove command.

Duplicates
- /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf and /data/downloads/final_v2.gguf are exact twins. Size 4,268 bytes.
  SHA-256 of tiny-lantern-1b-instruct-q4.gguf: cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf
  SHA-256 of final_v2.gguf: cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf
  Kept: the tiny-lantern copy, because it sits beside its model card.
- The same digest appears in the name of the /data/toolstore blob. That is claimed by name only, not hashed. It stays in place.
- pier-sketch and unknown are both 112 bytes but have different digests (5885a325e4db09b2e21579bc4733e419a3434a5dc3ac090c812fd67d13c3c468 and 3f7afab5d57407d74d592eba306de220f4f0c6fd9a51ded1a1fd1ac92abf08bb). They are not twins.

For your job: a small chat model for client work, memory budget 4 GB

Need 1. Chat
- On the shelf: Tiny Lantern 1B Instruct (/data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf, 4,268 bytes).
  Use, quoted from /data/models/tiny-lantern/README.md: "Intended use: chat and instruction following in English."
  Memory, quoted from the same card: "Memory: runs in about 2 GB." File size is under the 4 GB budget. This is arithmetic on file size only.
  License line: "license: apache-2.0" from the card, and "apache-2.0" from the header.
- Did not fit: Harbor Vision 2B, "Intended use: describing images." Pier Sketch XL, "Intended use: image generation."

Need 2. Small
- No card states a use that covers "small." Tiny Lantern's memory line is the nearest evidence, and it is not counted as a fit. Nothing you own covers this need. See What to get.

Need 3. Client work
- No card states client work or commercial use. Harbor Vision 2B has the line "Non-commercial use only." That is a restriction, not a fit. Nothing you own covers this need.

Could not match
- /data/models/image/unknown/model.safetensors. Not identified, so there is no card to read.

Caution: the Tiny Lantern .gguf files are only 4,268 bytes, far smaller than a real 1B model. The copy may be a stub or placeholder. The chat match rests on the card text alone, so check the file before you rely on it.

What to get (from the Model Shelf guide, checked November 9, 2026)
- For need 2, a small chat model: Qwen/Qwen2.5-1.5B-Instruct-GGUF. Task: chat and following instructions, text only. License as listed: apache-2.0. Size: 1.12 GB for the q4_k_m file, under your 4 GB budget. Access: open download, no form to accept.
- For need 3, client work: the guide has no entry for it. Look for a model whose card states a use that covers client work, a file size under 4 GB, and a license line you have read yourself.
Model Shelf does not download models. Download from the model page, put the file in a model folder, and run Model Shelf again.

Receipt

| File | Expected | Found | Result |
|---|---|---|---|
| final_v2.gguf | gone from /data/downloads, present in /data/archive, 4268 bytes | source NOT_FOUND, destination exists at 4268 bytes | match |

Bytes parked: 4,268 bytes in 1 file. The archive folder was empty before the move, so no name clash.

Tags added
- /data/models/harbor-vision/harbor-vision-2b.gguf: Model Shelf: Harbor Vision 2B
- /data/models/image/pier-sketch/model.safetensors: Model Shelf: Pier Sketch XL
- /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf: Model Shelf: Tiny Lantern 1B Instruct
No tag on the unknown file or on the parked final_v2.gguf.

Saved shelf file: /data/shelf/model-shelf-20261110T073730Z_8975eaf9.md (1,545 bytes, confirmed). The name carries the UTC date, which is 11:37 PM on November 9 in Pacific time.

Model Shelf quotes license lines and does not interpret them. This is not legal advice. Read the full license before you rely on it.
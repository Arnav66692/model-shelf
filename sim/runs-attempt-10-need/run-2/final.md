Model Shelf run complete. Two files were parked, one model was brought back, four tags were added, and the shelf file was saved and confirmed.

Shelf (5 weights files in the folders you named, plus 1 parked model in the archive). Paths are as scanned, before the moves.

| File | Model name | What it does | How named | Quant | Size | License line as written | Twin |
|---|---|---|---|---|---|---|---|
| /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B | describes images | header, model card | not shown | 4273 bytes | "license: harbor-noncommercial-1.0" from /data/models/harbor-vision/README.md (header agrees) | none |
| /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL (folder hint: pier-sketch) | makes images | model card | not shown | 112 bytes | "license: openrail++" from /data/models/image/pier-sketch/README.md (header states no license) | none |
| /data/models/image/unknown/model.safetensors | not identified (folder hint: unknown) | not stated | not identified | not shown | 112 bytes | no license line found | none (same size as pier-sketch, different digest) |
| /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct | chats and writes | header, model card | q4 in file name | 4268 bytes | "license: apache-2.0" from /data/models/tiny-lantern/README.md (header agrees) | /data/downloads/final_v2.gguf |
| /data/downloads/final_v2.gguf | Tiny Lantern 1B Instruct | not stated (no card beside this file) | header | not shown | 4268 bytes | "apache-2.0" from file header | /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf |

Parked models (in the archive folder)
- /data/archive/quill-coder/quill-coder-1b-q4.gguf. Quill Coder 1B, named by header and model card. 4259 bytes. License line: "license: apache-2.0" from /data/archive/quill-coder/README.md.

Space summary
- Loose files: 13033 bytes. Tool-managed folders: 4268 bytes. Archive folder: 4377 bytes.
- Proven twins parked: 4268 bytes in 1 file.

Tool-managed folders (listed, never moved)
- /data/toolstore. 1 file in its blobs folder, 4268 bytes. Blob sha256-cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf. This holds the same content as the two twins, claimed by name only. It stays in place. To remove a model from this store, use that tool's own remove command.

Duplicates
- /data/downloads/final_v2.gguf and /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf are exact twins. Size 4268 bytes.
  SHA-256 of /data/downloads/final_v2.gguf: cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf
  SHA-256 of /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf: cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf
- /data/models/image/pier-sketch/model.safetensors and /data/models/image/unknown/model.safetensors share size 112 bytes but are not twins.
  SHA-256 of pier-sketch: 5885a325e4db09b2e21579bc4733e419a3434a5dc3ac090c812fd67d13c3c468
  SHA-256 of unknown: 3f7afab5d57407d74d592eba306de220f4f0c6fd9a51ded1a1fd1ac92abf08bb

For your job: a small coding model and a speech to text model, memory budget 4 GB

Need 1. A small coding model. On the shelf, after a bring back.
- Parked, brought back: Quill Coder 1B (now /data/models/quill-coder/quill-coder-1b-q4.gguf, 4259 bytes, under the 4 GB budget)
  Use, quoted from /data/archive/quill-coder/README.md: "Intended use: code completion and code chat."
  Memory, quoted from the same card: "Memory: runs in about 2 GB."
  License line, from the same card: "license: apache-2.0"

Need 2. A speech to text model. Nothing you own covers this need. No card you own states a speech or audio use.

Did not fit
- Tiny Lantern 1B Instruct. Use, quoted from /data/models/tiny-lantern/README.md: "Intended use: chat and instruction following in English."
- Harbor Vision 2B. Use, quoted from /data/models/harbor-vision/README.md: "Intended use: describing images."
- Pier Sketch XL. Use, quoted from /data/models/image/pier-sketch/README.md: "Intended use: image generation."

Could not match
- /data/models/image/unknown/model.safetensors. Not identified, so there is no card to read.

What to get (from the Model Shelf guide, checked on November 9, 2026)
- For need 2: openai/whisper-large-v3-turbo. Task: speech to text. License as listed: mit. Size: 1.62 GB, under your 4 GB budget. Access: open download, no form to accept.
- For need 2: ggerganov/whisper.cpp. Task: speech to text, ready-made Whisper files for the whisper.cpp program. License as listed: mit. Size: 0.87 GB for ggml-large-v3-turbo-q8_0.bin, under your budget. Other files range up to 3.10 GB. Access: open download, no form to accept.
Model Shelf does not download models. Download one from its model page, put it in a model folder, and run Model Shelf again.

Model Shelf quotes license lines and does not interpret them. This is not legal advice. Read the full license before you rely on it.

Receipt

| File | Expected | Found | Result |
|---|---|---|---|
| final_v2.gguf | gone from /data/downloads, present in /data/archive, 4268 bytes | source gone, /data/archive/final_v2.gguf present, 4268 bytes | match |
| quill-coder-1b-q4.gguf | gone from /data/archive/quill-coder, present in /data/models/quill-coder, 4259 bytes | source gone, destination present, 4259 bytes | match |
| README.md | gone from /data/archive/quill-coder, present in /data/models/quill-coder, 118 bytes | source gone, destination present, 118 bytes | match |

Bytes parked: 4268 bytes in 1 file. Nothing was deleted, so no bytes were freed. The folder /data/archive/quill-coder was left in place.

Tags added (all four)
- /data/models/harbor-vision/harbor-vision-2b.gguf: Model Shelf: Harbor Vision 2B
- /data/models/image/pier-sketch/model.safetensors: Model Shelf: Pier Sketch XL
- /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf: Model Shelf: Tiny Lantern 1B Instruct
- /data/models/quill-coder/quill-coder-1b-q4.gguf: Model Shelf: Quill Coder 1B
No tag was added to /data/models/image/unknown/model.safetensors, the parked files, or /data/toolstore.

Shelf file saved and confirmed: /data/shelf/model-shelf-20261110T080017Z_8029b57f.md, 1996 bytes. The date in the file name is in UTC. The shelf text is dated 2026-11-09.

Note: the file expert ran one extra read-only dedupe scan on /data/toolstore that was not in the instruction. It returned no groups and changed nothing.
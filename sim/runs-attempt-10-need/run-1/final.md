Model Shelf run complete. All approved moves, tags and the shelf save were read back and match.

Shelf (5 weights files in the folders you named)

| File | Model name | What it does | How named | Size (bytes) | License line as written | Twin |
|---|---|---|---|---|---|---|
| /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B | describes images | header | 4273 | "license: harbor-noncommercial-1.0" from /data/models/harbor-vision/README.md | none |
| /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL | makes images | model card | 112 | "license: openrail++" from /data/models/image/pier-sketch/README.md | none |
| /data/models/image/unknown/model.safetensors | not identified (folder hint: unknown) | not stated | not identified | 112 | no license line found | none |
| /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct | chats and writes | header and model card | 4268 | "license: apache-2.0" from /data/models/tiny-lantern/README.md | /data/downloads/final_v2.gguf (now parked, see receipt) |

Tool-managed folder (listed, never moved): /data/toolstore holds 1 file in its blobs folder, 4268 bytes. Remove models from it only with that tool's own remove command.

Duplicates
- /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf (kept, sits beside its card) and /data/downloads/final_v2.gguf (parked) are exact twins. Size 4268 bytes.
  SHA-256: cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf
- The same digest is held by the toolstore blob sha256-cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf, claimed by name. It was not touched.
- pier-sketch and unknown model.safetensors are both 112 bytes but are not twins. SHA-256 5885a325e4db09b2e21579bc4733e419a3434a5dc3ac090c812fd67d13c3c468 and 3f7afab5d57407d74d592eba306de220f4f0c6fd9a51ded1a1fd1ac92abf08bb.

For your job: a small coding model and a speech to text model, memory budget 4 GB

Need 1. A small coding model
- Parked, now brought back: Quill Coder 1B, /data/models/quill-coder/quill-coder-1b-q4.gguf (4259 bytes), with its card /data/models/quill-coder/README.md.
  Use, from that card: "Intended use: code completion and code chat."
  Memory, from that card: "Memory: runs in about 2 GB." The file size is under your 4 GB budget.
  License line, from that card: "license: apache-2.0"

Need 2. A speech to text model
- Nothing you own covers this need. No card on the shelf or in the archive states a speech or transcription use.

Did not fit
- Harbor Vision 2B. Use: "Intended use: describing images."
- Pier Sketch XL. Use: "Intended use: image generation."
- Tiny Lantern 1B Instruct. Use: "Intended use: chat and instruction following in English."

Could not match
- /data/models/image/unknown/model.safetensors. Not identified, and no model card sits in its folder.

What to get (from the Model Shelf guide, checked on November 9, 2026)
- For need 2: openai/whisper-large-v3-turbo. Task: speech to text. License as listed: mit. Size: 1.62 GB, under your 4 GB budget. Access: open download, no form to accept.
- For need 2: ggerganov/whisper.cpp. Task: speech to text, ready-made Whisper files for the whisper.cpp program. License as listed: mit. Size: 0.87 GB for ggml-large-v3-turbo-q8_0.bin, under your budget. Access: open download, no form to accept.
Model Shelf does not download models. Download one from its model page, put it in a model folder, and run Model Shelf again.

Receipt
| File | Expected | Found | Result |
|---|---|---|---|
| final_v2.gguf | gone from /data/downloads, present in /data/archive, 4268 bytes | source gone, /data/archive/final_v2.gguf present, 4268 bytes | match |
| quill-coder-1b-q4.gguf | gone from /data/archive/quill-coder, present in /data/models/quill-coder, 4259 bytes | source gone, destination present, 4259 bytes | match |
| README.md | gone from /data/archive/quill-coder, present in /data/models/quill-coder, 118 bytes | source gone, destination present, 118 bytes | match |

Tags added (all four, each on its named file): Model Shelf: Harbor Vision 2B, Model Shelf: Tiny Lantern 1B Instruct, Model Shelf: Pier Sketch XL, Model Shelf: Quill Coder 1B.

Bytes parked: 4268 bytes in 1 file, now /data/archive/final_v2.gguf. Bytes brought back: 4377 bytes in 2 files. Parked files still use space until you remove them yourself. Nothing was deleted.

Shelf file saved: /data/shelf/model-shelf-20261110T080029Z_1db9eda9.md (1704 bytes).

Model Shelf quotes license lines and does not interpret them. This is not legal advice. Read the full license before you rely on it.
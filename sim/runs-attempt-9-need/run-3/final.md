Model Shelf run complete. All moves, tags and the shelf save are done, and the read back matches.

**Shelf (5 weights files in /data/models, /data/downloads and /data/toolstore, scanned before the moves)**

| File | Model name | How named | Size | License line as written | Twin |
|---|---|---|---|---|---|
| /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B | header | 4273 bytes | "harbor-noncommercial-1.0" from header, "license: harbor-noncommercial-1.0" from /data/models/harbor-vision/README.md | none |
| /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL | model card /data/models/image/pier-sketch/README.md | 112 bytes | "license: openrail++" from the card | none (same size as the next row, digests differ) |
| /data/models/image/unknown/model.safetensors | not identified (folder hint: unknown) | not identified | 112 bytes | no license line found | none (digests differ) |
| /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct | header | 4268 bytes | "apache-2.0" from header, "license: apache-2.0" from /data/models/tiny-lantern/README.md | /data/downloads/final_v2.gguf (now moved, see receipt) |
| /data/downloads/final_v2.gguf | Tiny Lantern 1B Instruct | header | 4268 bytes | "apache-2.0" from header, no card beside it | /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf |

Parked model in the archive: /data/archive/quill-coder/quill-coder-1b-q4.gguf, Quill Coder 1B, 4259 bytes, named by header and card. License line: "license: apache-2.0" from its card. It has been brought back (see below).

Space: loose files 13033 bytes. Tool-managed folder (/data/toolstore, listed and never moved): 1 blob, 4268 bytes. Archive: 4377 bytes. Proven twins parked: 4268 bytes in 1 file.

Duplicates: /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf and /data/downloads/final_v2.gguf are exact twins, size 4268 bytes, SHA-256 cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf for both. The same content is also held in /data/toolstore as blob sha256-cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf, claimed by name. Not twins: the two 112 byte safetensors files, with digests 5885a325e4db09b2e21579bc4733e419a3434a5dc3ac090c812fd67d13c3c468 and 3f7afab5d57407d74d592eba306de220f4f0c6fd9a51ded1a1fd1ac92abf08bb.

**For your job (small coding model and speech to text model, 4 GB budget)**

Need 1, a small coding model: covered by Quill Coder 1B, which was parked and is now brought back. Quoted from /data/archive/quill-coder/README.md: "Intended use: code completion and code chat." and "Memory: runs in about 2 GB." Its file is 4259 bytes, under the 4 GB budget.

Need 2, a speech to text model: nothing you own covers it. The cards for Tiny Lantern ("Intended use: chat and instruction following in English."), Harbor Vision ("Intended use: describing images.") and Pier Sketch XL ("Intended use: image generation.") do not cover it.

**What to get (Need 2)**

From the Model Shelf guide, checked November 9, 2026:
- openai/whisper-large-v3-turbo. Speech to text. License as listed: mit. Size 1.62 GB, under your budget. Open download, no form to accept.
- ggerganov/whisper.cpp. Speech to text, Whisper files for the whisper.cpp program. License as listed: mit. Size 0.87 GB for ggml-large-v3-turbo-q8_0.bin, under your budget. Open download, no form to accept.

Model Shelf does not download models. Get one from its model page, put it in a model folder, and run Model Shelf again.

**Receipt**

| File | Expected | Found | Result |
|---|---|---|---|
| final_v2.gguf | gone from /data/downloads, present in /data/archive, 4268 bytes | source gone, /data/archive/final_v2.gguf present, 4268 bytes | match |
| quill-coder-1b-q4.gguf | gone from /data/archive/quill-coder, present in /data/models/quill-coder, 4259 bytes | source gone, /data/models/quill-coder/quill-coder-1b-q4.gguf present, 4259 bytes | match |
| README.md | gone from /data/archive/quill-coder, present in /data/models/quill-coder, 118 bytes | source gone, /data/models/quill-coder/README.md present, 118 bytes | match |

Bytes parked: 4268 bytes in 1 file. Bytes brought back: 4259 bytes plus the 118 byte card. The new folder /data/models/quill-coder was created for the brought back model.

Tags added: Harbor Vision 2B, Pier Sketch XL, Tiny Lantern 1B Instruct, and Quill Coder 1B on the four named files. No other file was tagged.

Two things to check:
- /data/downloads/final_v2.gguf is now parked at /data/archive/final_v2.gguf. If a tool or workflow loads the downloads copy from its old path, point it at the archive copy. The copy that stays in place is /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf.
- Every weights file here is only a few thousand bytes, far smaller than a real 1B model. The size and budget checks are only arithmetic on these file sizes, so these may be placeholders. Check the real files before you rely on them. The license lines are quoted as written and are not legal advice. Read the full license before you use a model.

Shelf file saved: /data/shelf/model-shelf-20261110T074552Z_c62972a3.md, 1919 bytes. No earlier shelf file existed, so there is no changed since last shelf list.
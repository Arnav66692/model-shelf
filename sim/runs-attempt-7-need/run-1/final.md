Model Shelf run complete. Moves, tags and the shelf file are all done, and the read back matches.

**Shelf (5 weights files in /data/models, /data/downloads and /data/archive, as they were before the moves)**

| File | Model name | How named | Size (bytes) | License line as written | Twin |
|---|---|---|---|---|---|
| /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B | header and model card | 4273 | "license: harbor-noncommercial-1.0" from /data/models/harbor-vision/README.md (header states the same) | none |
| /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL | model card | 112 | "license: openrail++" from /data/models/image/pier-sketch/README.md | none |
| /data/models/image/unknown/model.safetensors | not identified (folder hint: unknown) | not identified | 112 | no license line found | none |
| /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct | header and model card | 4268 | "license: apache-2.0" from /data/models/tiny-lantern/README.md | /data/downloads/final_v2.gguf (now parked, see receipt) |
| /data/downloads/final_v2.gguf (now /data/archive/final_v2.gguf) | Tiny Lantern 1B Instruct | header only, no card beside it | 4268 | "apache-2.0" from the file header | /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf |

Parked models in the archive folder after the run: /data/archive/final_v2.gguf (4268 bytes, Tiny Lantern 1B Instruct, named by header). The Quill Coder files were brought back out of the archive (see below).

**Space summary (before the moves)**
- Loose files: 13033 bytes. Tool-managed folder (/data/toolstore): 4268 bytes. Archive folder: 4259 bytes.
- Proven twins parked: 4268 bytes in 1 file.

**Tool-managed folders (listed, never moved)**
- /data/toolstore holds 1 file in its blobs folder, 4268 bytes. The blob is /data/toolstore/blobs/sha256-cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf. Its name carries the same digest as the tiny-lantern copy. That match is claimed by name only, and the blob stays in place. To remove a model from this store, use that tool's own remove command.

**Duplicates (proven by SHA-256)**
- /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf and /data/downloads/final_v2.gguf are exact twins. Size 4268 bytes.
  - SHA-256 of tiny-lantern-1b-instruct-q4.gguf: cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf
  - SHA-256 of final_v2.gguf: cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf
  - The copy beside its model card was kept. The other was parked.
- /data/models/image/pier-sketch/model.safetensors and /data/models/image/unknown/model.safetensors are both 112 bytes but not twins.
  - SHA-256 of pier-sketch: 5885a325e4db09b2e21579bc4733e419a3434a5dc3ac090c812fd67d13c3c468
  - SHA-256 of unknown: 3f7afab5d57407d74d592eba306de220f4f0c6fd9a51ded1a1fd1ac92abf08bb

**For your job: a small coding model and a speech to text model, memory budget 4 GB**

Need 1. A small coding model. Brought back from the archive: Quill Coder 1B (/data/models/quill-coder/quill-coder-1b-q4.gguf, 4259 bytes, with its card).
- Use, quoted from /data/archive/quill-coder/README.md (now /data/models/quill-coder/README.md): "Intended use: code completion and code chat."
- Memory, quoted from the same card: "Memory: runs in about 2 GB." The file is 4259 bytes, under the 4 GB budget. This is arithmetic on file size only. It does not promise that the model will run.
- License line, from the same card: "license: apache-2.0"

Need 2. A speech to text model. Nothing you own or parked covers it. None of the four model cards states a speech or audio use.

Did not fit:
- Tiny Lantern 1B Instruct. "Intended use: chat and instruction following in English." (/data/models/tiny-lantern/README.md)
- Harbor Vision 2B. "Intended use: describing images." (/data/models/harbor-vision/README.md)
- Pier Sketch XL. "Intended use: image generation." (/data/models/image/pier-sketch/README.md)

Could not match: /data/models/image/unknown/model.safetensors. Not identified, so there is no card to read.

**What to get (from the Model Shelf guide, checked on November 9, 2026)**
For need 2, the guide has two speech to text entries. Both are under your 4 GB budget.
- openai/whisper-large-v3-turbo. Task: speech to text. License as listed: mit. Size: 1.62 GB, under budget. Access: open download, no form to accept.
- ggerganov/whisper.cpp. Task: speech to text, Whisper files for the whisper.cpp program. License as listed: mit. Size: 0.87 GB for ggml-large-v3-turbo-q8_0.bin, and up to 3.10 GB for the other files, all under budget. Access: open download, no form to accept.

Model Shelf does not download models. Download one from its model page, put it in a model folder, and run Model Shelf again.

Model Shelf quotes license lines and does not interpret them. This is not legal advice. Read the full license before you rely on it.

**Moves (receipt, read back in Step 7)**

| File | Expected | Found | Result |
|---|---|---|---|
| final_v2.gguf | gone from /data/downloads, present in /data/archive, 4268 bytes | source gone, /data/archive/final_v2.gguf present, 4268 bytes | match |
| quill-coder-1b-q4.gguf | gone from /data/archive/quill-coder, present in /data/models/quill-coder, 4259 bytes | source gone, /data/models/quill-coder/quill-coder-1b-q4.gguf present, 4259 bytes | match |
| README.md (Quill Coder card) | gone from /data/archive/quill-coder, present in /data/models/quill-coder, 118 bytes | source gone, /data/models/quill-coder/README.md present, 118 bytes | match |

Bytes parked: 4268 bytes in 1 file. Bytes brought back: 4259 bytes in 1 weights file, plus its 118 byte card. Parked files still use disk space until you remove them yourself.

**Tags added (all four)**
- /data/models/harbor-vision/harbor-vision-2b.gguf: Model Shelf: Harbor Vision 2B
- /data/models/image/pier-sketch/model.safetensors: Model Shelf: Pier Sketch XL
- /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf: Model Shelf: Tiny Lantern 1B Instruct
- /data/models/quill-coder/quill-coder-1b-q4.gguf: Model Shelf: Quill Coder 1B
- /data/models/image/unknown/model.safetensors got no tag, because it is not identified.

**Shelf file saved**
- /data/shelf/model-shelf-20261110T072700Z_6e780c92.md, 1882 bytes. Saved at about 11:27 PM PT on 2026-11-09. Its name is the NAS time stamp.

One thing to watch: the tiny-lantern copy is the one kept in /data/models. If a tool loads a model from its current path and stops working, tell me and the archived final_v2.gguf can be brought back in its place.
Model Shelf run complete for 2026-11-09. All three moves, all four tags and the shelf save are done, and the read-back matches.

**Shelf (5 weights files in the folders you named, as found at the start of the run)**

| File | Model name | How named | Size | License line as written | Twin |
|---|---|---|---|---|---|
| /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B | header and model card | 4273 bytes | header: "harbor-noncommercial-1.0". Card (/data/models/harbor-vision/README.md): "license: harbor-noncommercial-1.0". The card also says "Non-commercial use only." | none |
| /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL | model card | 112 bytes | "license: openrail++" from /data/models/image/pier-sketch/README.md | none, digest differs |
| /data/models/image/unknown/model.safetensors | not identified (folder hint: unknown) | not identified | 112 bytes | no license line found | none, digest differs |
| /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct | header and model card | 4268 bytes | "license: apache-2.0" from /data/models/tiny-lantern/README.md | /data/downloads/final_v2.gguf (kept this copy) |
| /data/downloads/final_v2.gguf | Tiny Lantern 1B Instruct | header | 4268 bytes | "apache-2.0" from the file header | /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf (parked, see receipt) |

Parked before this run: /data/archive/quill-coder/quill-coder-1b-q4.gguf, Quill Coder 1B, named by header and model card, 4259 bytes. License line: "license: apache-2.0" from /data/archive/quill-coder/README.md.

**Space summary (before the moves)**
- Loose files: 13033 bytes. Tool-managed folders: 4268 bytes in blobs. Archive folder: 4377 bytes (model plus card).
- Proven twins that could be parked: 4268 bytes in 1 file.

**Tool-managed folder (listed, never moved)**
- /data/toolstore. 1 file in its blobs folder, 4268 bytes, named sha256-cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf. The same digest as the tiny-lantern file, claimed by name only. Remove a model from this store with that tool's own remove command.

**Duplicates**
- /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf and /data/downloads/final_v2.gguf are exact twins. Size 4268 bytes.
  SHA-256 of both: cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf
- Kept: the tiny-lantern copy, because it sits beside its model card. Parked: final_v2.gguf.
- Not twins: /data/models/image/pier-sketch/model.safetensors (5885a325e4db09b2e21579bc4733e419a3434a5dc3ac090c812fd67d13c3c468) and /data/models/image/unknown/model.safetensors (3f7afab5d57407d74d592eba306de220f4f0c6fd9a51ded1a1fd1ac92abf08bb).

**For your job (small coding model and speech to text model, 4 GB budget)**
- Need 1, small coding model: covered by Quill Coder 1B, which was parked and is now brought back. From /data/archive/quill-coder/README.md: "Intended use: code completion and code chat." and "Memory: runs in about 2 GB." License: "license: apache-2.0". Size 4259 bytes, under 4 GB.
- Need 2, speech to text model: nothing you own covers it. None of the four cards states speech, audio or transcription use. Harbor Vision is for "Intended use: describing images." Pier Sketch XL is for "Intended use: image generation." Tiny Lantern is for "Intended use: chat and instruction following in English."

**What to get for need 2** (from the Model Shelf guide, checked November 9, 2026)
- openai/whisper-large-v3-turbo. Speech to text. License as listed: mit. Size 1.62 GB. Open download, no form to accept.
- ggerganov/whisper.cpp, file ggml-large-v3-turbo-q8_0.bin. Speech to text, for the whisper.cpp program. License as listed: mit. Size 0.87 GB. Open download, no form to accept.

Both are under your 4 GB budget. Model Shelf does not download models. Get one from its model page, put it in a model folder, and run Model Shelf again.

**Receipt**

| File | Expected | Found | Result |
|---|---|---|---|
| final_v2.gguf | gone from /data/downloads, present in /data/archive, 4268 bytes | source absent, /data/archive/final_v2.gguf present, 4268 bytes | match |
| quill-coder-1b-q4.gguf | gone from /data/archive/quill-coder, present in /data/models/quill-coder, 4259 bytes | source absent, /data/models/quill-coder/quill-coder-1b-q4.gguf present, 4259 bytes | match |
| README.md (Quill Coder card) | gone from /data/archive/quill-coder, present in /data/models/quill-coder, 118 bytes | source absent, /data/models/quill-coder/README.md present, 118 bytes | match |

Bytes parked: 4268 bytes in 1 file. Bytes brought back: 4377 bytes in 2 files. Parked files still use space until you remove them, so no bytes were freed.

Checks not run: the moves were confirmed by existence and size only, with no SHA-256 re-check of the moved copies. The move tool does not report success itself, so the read-back is the evidence.

**Tags added (4)**
- /data/models/harbor-vision/harbor-vision-2b.gguf: Model Shelf: Harbor Vision 2B
- /data/models/image/pier-sketch/model.safetensors: Model Shelf: Pier Sketch XL
- /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf: Model Shelf: Tiny Lantern 1B Instruct
- /data/models/quill-coder/quill-coder-1b-q4.gguf: Model Shelf: Quill Coder 1B
The unidentified file /data/models/image/unknown/model.safetensors got no tag.

**Saved shelf file**
- /data/shelf/model-shelf-20261110T073824Z_5554c844.md, 2344 bytes, confirmed present. The text is dated 2026-11-09 Pacific time. The file name carries the UTC stamp.
- No earlier shelf file was found, so there was no changed-since section.

Model Shelf quotes license lines and does not interpret them. This is not legal advice. Read the full license before you rely on any of these models.
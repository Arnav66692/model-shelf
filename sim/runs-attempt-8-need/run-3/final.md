Model Shelf run complete. Nothing was deleted. Three files moved, four tags were added, and the shelf file is saved at /data/shelf/model-shelf-20261110T073829Z_daaa74f6.md (1961 bytes, confirmed present).

**Shelf (5 loose weights files in /data/models and /data/downloads, before the moves)**

| File | Model name | How named | Size (bytes) | License line as written | Twin |
|---|---|---|---|---|---|
| /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B | header | 4273 | "license: harbor-noncommercial-1.0" from /data/models/harbor-vision/README.md | none |
| /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL | model card | 112 | "license: openrail++" from /data/models/image/pier-sketch/README.md | none (same size, different digest) |
| /data/models/image/unknown/model.safetensors | not identified (folder hint: unknown) | not identified | 112 | no license line found | none (same size, different digest) |
| /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct | header | 4268 | "license: apache-2.0" from /data/models/tiny-lantern/README.md | /data/downloads/final_v2.gguf (kept, sits beside its card) |
| /data/downloads/final_v2.gguf | Tiny Lantern 1B Instruct | header | 4268 | "apache-2.0" from header | /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf (parked) |

Twins were proven by SHA-256, both digests cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf.

Tool-managed, listed and never moved: /data/toolstore holds 1 file in its blobs folder, 4268 bytes, named sha256-cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf. That name matches the twin digest, but the content was not read, so the match is by name only.

Parked model brought back: /data/archive/quill-coder/quill-coder-1b-q4.gguf (Quill Coder 1B, named by header and card, 4259 bytes) with its card README.md (118 bytes).

**Job answer (small coding model and speech to text model, 4 GB budget)**

- Need 1, small coding model: covered by Quill Coder 1B, which was parked and is now back on the shelf. Quoted from its card: "Intended use: code completion and code chat." and "Memory: runs in about 2 GB." Its file is under the 4 GB budget. License: "license: apache-2.0".
- Need 2, speech to text model: nothing you own covers it. None of the four model cards states speech recognition or transcription as a use. Harbor Vision, Pier Sketch and Tiny Lantern do not fit it.

**What to get (need 2, from the Model Shelf guide checked November 9, 2026)**

- openai/whisper-large-v3-turbo. Speech to text. License as listed: mit. Size: 1.62 GB, under the 4 GB budget. Open download, no form to accept.
- ggerganov/whisper.cpp. Speech to text, Whisper files for the whisper.cpp program. License as listed: mit. Size: 0.87 GB for ggml-large-v3-turbo-q8_0.bin, other files up to 3.10 GB. Open download, no form to accept.

Model Shelf does not download models. Download one from its model page into a model folder, then run Model Shelf again. Model Shelf quotes license lines and does not interpret them. This is not legal advice, so read the full license before you rely on it.

**Receipt**

| File | Expected | Found | Result |
|---|---|---|---|
| final_v2.gguf | gone from /data/downloads, present in /data/archive, 4268 bytes | source gone, /data/archive/final_v2.gguf is 4268 bytes | match |
| quill-coder-1b-q4.gguf | gone from /data/archive/quill-coder, present in /data/models/quill-coder, 4259 bytes | source gone, destination is 4259 bytes | match |
| README.md (quill-coder card) | gone from /data/archive/quill-coder, present in /data/models/quill-coder, 118 bytes | source gone, destination is 118 bytes | match |

Bytes parked: 4268 in 1 file. Bytes brought back: 4377 in 2 files. No bytes were freed, because the parked copy still uses space until you remove it.

**Tags added**

- /data/models/harbor-vision/harbor-vision-2b.gguf: Model Shelf: Harbor Vision 2B
- /data/models/image/pier-sketch/model.safetensors: Model Shelf: Pier Sketch XL
- /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf: Model Shelf: Tiny Lantern 1B Instruct
- /data/models/quill-coder/quill-coder-1b-q4.gguf: Model Shelf: Quill Coder 1B

The File Manager did not say whether each tag was new or already existed. Not tagged: the unidentified unknown/model.safetensors, the parked final_v2.gguf, and the tool-managed blob.

**Notes**

- The old folder /data/archive/quill-coder is still there. It was not on the approved list, so it was left alone and may now be empty. Remove it yourself if you want.
- The NAS stamps file names in UTC, so the shelf file name reads 20261110. The run was on November 9 Pacific time.
- No earlier shelf file was found, so there is no changed-since section.
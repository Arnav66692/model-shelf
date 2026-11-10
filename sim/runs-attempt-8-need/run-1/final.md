Model Shelf run complete. All moves, tags and the shelf file were written, and the receipt matches.

**Shelf (5 loose weights files in /data/models and /data/downloads)**

| File (as found) | Model name | How named | Size (bytes) | License line as written | Twin |
|---|---|---|---|---|---|
| /data/downloads/final_v2.gguf | Tiny Lantern 1B Instruct | header | 4268 | "general.license = apache-2.0" from header | /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf |
| /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B | header | 4273 | "general.license = harbor-noncommercial-1.0" from header; "license: harbor-noncommercial-1.0" from /data/models/harbor-vision/README.md | none |
| /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL | model card | 112 | "license: openrail++" from /data/models/image/pier-sketch/README.md | none |
| /data/models/image/unknown/model.safetensors | not identified (folder hint: unknown) | not identified | 112 | no license line found | none |
| /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct | header | 4268 | "general.license = apache-2.0" from header; "license: apache-2.0" from /data/models/tiny-lantern/README.md | /data/downloads/final_v2.gguf |

Parked model (archive): /data/archive/quill-coder/quill-coder-1b-q4.gguf, Quill Coder 1B, named by header and card, 4259 bytes, "license: apache-2.0" from /data/archive/quill-coder/README.md.

Tool-managed (listed, never moved): /data/toolstore holds 1 blob, 4268 bytes. Its name carries the same SHA-256 as the duplicate pair below, claimed by name only. It stays in place.

Space: loose files 13033 bytes. Tool-managed 4268 bytes. Archive 4259 bytes of weights.

**Duplicates**
- /data/downloads/final_v2.gguf and /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf are exact twins, 4268 bytes, SHA-256 cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf for both.
- /data/models/image/pier-sketch/model.safetensors (5885a325e4db09b2e21579bc4733e419a3434a5dc3ac090c812fd67d13c3c468) and /data/models/image/unknown/model.safetensors (3f7afab5d57407d74d592eba306de220f4f0c6fd9a51ded1a1fd1ac92abf08bb) have the same size but different digests. They are not twins.
- Kept: the copy beside its model card, /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf. Parked: /data/downloads/final_v2.gguf.

**For your job: a small coding model and a speech to text model (memory budget 4 GB)**
- Need 1, small coding model: covered by Quill Coder 1B, which was parked and is now brought back. Card line: "Intended use: code completion and code chat." Card line: "Memory: runs in about 2 GB." File size 4259 bytes is under the 4 GB budget. This is arithmetic on file size only and does not promise the model will run.
- Need 2, speech to text model: nothing you own covers it. The four cards state no speech or transcription use. From the checked guide (November 9, 2026):
  - openai/whisper-large-v3-turbo. Task: speech to text. License as listed: mit. Size: 1.62 GB. Open download, no form.
  - ggerganov/whisper.cpp. Task: speech to text, Whisper files for whisper.cpp. License as listed: mit. Size: 0.87 GB for ggml-large-v3-turbo-q8_0.bin, other files up to 3.10 GB. Open download, no form.
  Model Shelf does not download models. Get one from its model page, put it in a model folder, and run Model Shelf again.
- Not identified: /data/models/image/unknown/model.safetensors. There is no card to read.

**Moves (receipt, read back after the moves)**

| File | Expected | Found | Result |
|---|---|---|---|
| final_v2.gguf | gone from /data/downloads, present in /data/archive, 4268 bytes | source gone, destination present, 4268 bytes | match |
| quill-coder-1b-q4.gguf | gone from /data/archive/quill-coder, present in /data/models/quill-coder, 4259 bytes | source gone, destination present, 4259 bytes | match |
| README.md | gone from /data/archive/quill-coder, present in /data/models/quill-coder, 118 bytes | source gone, destination present, 118 bytes | match |

Bytes parked: 4268 bytes in 1 file. A parked file still uses space until you remove it. Nothing was deleted.

**Tags added (4)**
- /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf: Model Shelf: Tiny Lantern 1B Instruct
- /data/models/harbor-vision/harbor-vision-2b.gguf: Model Shelf: Harbor Vision 2B
- /data/models/image/pier-sketch/model.safetensors: Model Shelf: Pier Sketch XL
- /data/models/quill-coder/quill-coder-1b-q4.gguf: Model Shelf: Quill Coder 1B
The unidentified file and the parked files got no tag.

**Saved shelf file**
/data/shelf/model-shelf-20261110T073748Z_5b17a81e.md, 2409 bytes. The NAS stamp is UTC, so this run was 23:37 PT on November 9, 2026.

**Open items**
- If any tool or workflow loads /data/downloads/final_v2.gguf from its old path, that path is now empty. Tell me and I will park the other copy instead.
- Model Shelf quotes license lines and does not interpret them. This is not legal advice. Read the full license before you rely on any model.
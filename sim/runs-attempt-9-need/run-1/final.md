Model Shelf run complete. All moves, tags and the shelf save are done, and the read back matches.

**Shelf (state after the moves)**

| File | Model name | How named | Quant | Size | License line as written | Twin |
|---|---|---|---|---|---|---|
| /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B | header (card agrees) | not shown | 4273 bytes | "license: harbor-noncommercial-1.0" from /data/models/harbor-vision/README.md | none |
| /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL | model card (header gives no name) | not shown | 112 bytes | "license: openrail++" from /data/models/image/pier-sketch/README.md | none |
| /data/models/image/unknown/model.safetensors | not identified (folder hint: unknown) | not identified | not shown | 112 bytes | no license line found | none |
| /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct | header (card agrees) | q4 | 4268 bytes | "license: apache-2.0" from /data/models/tiny-lantern/README.md | parked copy: /data/archive/final_v2.gguf |
| /data/models/quill-coder/quill-coder-1b-q4.gguf (brought back) | Quill Coder 1B | header and card | q4 | 4259 bytes | "license: apache-2.0" from /data/models/quill-coder/README.md | none |

Space: loose files 8765 bytes in 4 files. Tool-managed: /data/toolstore, 1 blob of 4268 bytes (sha256-cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf), left in place. Bytes parked: 4268 bytes in /data/archive/final_v2.gguf. Parking does not free space.

Duplicates: /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf and /data/downloads/final_v2.gguf are exact twins, both SHA-256 cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf. The copy beside its model card was kept. The /data/models/image pair is the same size (112 bytes) but different content, so they are not twins. No earlier shelf file existed, so there is no changed list.

**For your job**
- Small coding model: covered by Quill Coder 1B, brought back from the archive. Card line: "Intended use: code completion and code chat." Card memory line: "Memory: runs in about 2 GB." Under your 4 GB budget.
- Speech to text model: nothing you own covers this. No card you own states a speech, audio or transcription use.

**What to get** (from the Model Shelf guide, checked November 9, 2026. You download these yourself, then run Model Shelf again.)
- openai/whisper-large-v3-turbo. Speech to text. License as listed: mit. Size: 1.62 GB. Open download, no form.
- ggerganov/whisper.cpp. Speech to text, ready-made Whisper files for whisper.cpp. License as listed: mit. Size: 0.87 GB for ggml-large-v3-turbo-q8_0.bin, other files up to 3.10 GB, so check the size of the file you pick. Open download, no form.
Both are under your 4 GB budget at the sizes listed. Model Shelf quotes license lines and does not interpret them. This is not legal advice, so read the full license before you rely on it.

**Receipt**

| File | Expected | Found | Result |
|---|---|---|---|
| final_v2.gguf | gone from /data/downloads, present in /data/archive, 4268 bytes | source gone, /data/archive/final_v2.gguf present, 4268 bytes | match |
| quill-coder-1b-q4.gguf | gone from /data/archive/quill-coder, present in /data/models/quill-coder, 4259 bytes | source gone, destination present, 4259 bytes | match |
| README.md (Quill Coder card) | gone from /data/archive/quill-coder, present in /data/models/quill-coder, 118 bytes | source gone, destination present, 118 bytes | match |

Tags added, one per named file: Model Shelf: Harbor Vision 2B, Model Shelf: Pier Sketch XL, Model Shelf: Tiny Lantern 1B Instruct, Model Shelf: Quill Coder 1B. The unidentified file and the parked copy got no tag.

Shelf file saved and confirmed: /data/shelf/model-shelf-20261110T074555Z_35f8cb8a.md, 2054 bytes. Its name is in UTC, so it is dated 2026-11-09 23:45 PT.

**Things to check**
- Every weights file here is only a few kilobytes, far below the size of a real 1B model. They may be stubs or incomplete copies. Check them before you rely on them.
- If any tool or workflow loads the final_v2 copy from /data/downloads, tell me and I will park the other copy instead.
- The Quill Coder model was moved to /data/models/quill-coder, a new folder, because the shelf had no record of where it was parked from.
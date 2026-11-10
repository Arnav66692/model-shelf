Model Shelf run complete. All moves, tags and the shelf file are done, and the read back matched.

Shelf (5 weights files in the folders you named)

| File | Model name | How named | Size | License line as written | Twin |
| --- | --- | --- | --- | --- | --- |
| /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B | header and model card | 4273 | "license: harbor-noncommercial-1.0" from /data/models/harbor-vision/README.md | none |
| /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL | model card | 112 | "license: openrail++" from /data/models/image/pier-sketch/README.md | none (same size as the next file, digests differ) |
| /data/models/image/unknown/model.safetensors | not identified (folder hint: unknown) | not identified | 112 | no license line found | none (digests differ from the file above) |
| /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct | header and model card | 4268 | "license: apache-2.0" from /data/models/tiny-lantern/README.md | /data/archive/final_v2.gguf (moved from /data/downloads) |

Parked files: Quill Coder 1B was brought back from the archive. Nothing is parked in the archive as a weights file except final_v2.gguf, the exact twin of Tiny Lantern (SHA-256 cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf). The tool-managed store /data/toolstore was listed and not moved (1 blob, 4268 bytes).

Your job

- Need 1, small coding model: covered by Quill Coder 1B, which is now at /data/models/quill-coder/quill-coder-1b-q4.gguf (4259 bytes). Card line: "Intended use: code completion and code chat." Card line: "Memory: runs in about 2 GB." License line: "license: apache-2.0".
- Need 2, speech to text model: nothing you own covers this. No card states a speech or audio use.

What to get

- openai/whisper-large-v3-turbo. Task: speech to text. License as listed: mit. Size: 1.62 GB, under your 4 GB budget. Open download, no form.
- ggerganov/whisper.cpp. Task: speech to text, Whisper files for the whisper.cpp program. License as listed: mit. Size: 0.87 GB for ggml-large-v3-turbo-q8_0.bin, under your budget. Other files go up to 3.10 GB. Open download, no form.

Model Shelf does not download models. Get one from its model page, put it in a model folder, and run Model Shelf again.

Receipt

| File | Expected | Found | Result |
| --- | --- | --- | --- |
| final_v2.gguf | gone from /data/downloads, present in /data/archive, 4268 | source gone, /data/archive/final_v2.gguf 4268 | match |
| quill-coder-1b-q4.gguf | gone from /data/archive/quill-coder, present in /data/models/quill-coder, 4259 | source gone, destination 4259 | match |
| README.md (Quill Coder card) | gone from /data/archive/quill-coder, present in /data/models/quill-coder, 118 | source gone, destination 118 | match |

Bytes parked: 4268 in 1 file. Parked bytes still use space until you remove the file yourself.

Tags added (4): Model Shelf: Harbor Vision 2B, Model Shelf: Pier Sketch XL, Model Shelf: Tiny Lantern 1B Instruct (on /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf), Model Shelf: Quill Coder 1B. The unidentified file got no tag.

Shelf file saved: /data/shelf/model-shelf-20261110T074556Z_d115c138.md (1979 bytes, dated 2026-11-09 PT). Ask Model Shelf about it later and it answers from this file. Files can change after this date, so run a full check again if you need current facts.

Note: /data/downloads/final_v2.gguf now sits in /data/archive. If anything loads the model from /data/downloads, tell me and I will plan to park the other copy instead. Model Shelf quotes license lines and does not interpret them. This is not legal advice.
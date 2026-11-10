Model Shelf run complete. The receipt matches and the shelf file is saved.

**Shelf (weights files in the folders you named, plus the archive)**

| File | Model name | How named | Size | License line as written | Twin |
|---|---|---|---|---|---|
| /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B | header | 4273 bytes | "license: harbor-noncommercial-1.0" (/data/models/harbor-vision/README.md) | none |
| /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL | model card | 112 bytes | "license: openrail++" (/data/models/image/pier-sketch/README.md) | none |
| /data/models/image/unknown/model.safetensors | not identified (folder hint: unknown) | not identified | 112 bytes | no license line found | none |
| /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct | header and model card | 4268 bytes | "license: apache-2.0" (/data/models/tiny-lantern/README.md) | /data/downloads/final_v2.gguf (kept copy) |
| /data/downloads/final_v2.gguf | Tiny Lantern 1B Instruct | header | 4268 bytes | "apache-2.0" (header) | tiny-lantern copy (now parked, see receipt) |
| /data/archive/quill-coder/quill-coder-1b-q4.gguf | Quill Coder 1B | header and model card | 4259 bytes | "license: apache-2.0" (/data/archive/quill-coder/README.md) | none |

Tool-managed (listed, never moved): /data/toolstore, 1 blob, 4268 bytes, sha256-cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf.

Duplicates, proven by SHA-256: /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf and /data/downloads/final_v2.gguf both hash to cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf. The NAS did not say whether they are two copies or hard links. The two 112-byte safetensors files are not twins (pier-sketch 5885a325e4db09b2e21579bc4733e419a3434a5dc3ac090c812fd67d13c3c468, unknown 3f7afab5d57407d74d592eba306de220f4f0c6fd9a51ded1a1fd1ac92abf08bb).

**Job: a small coding model and a speech to text model (memory budget 4 GB)**

- Need 1, small coding model: brought back. Quill Coder 1B. Card line: "Intended use: code completion and code chat." Card line: "Memory: runs in about 2 GB." Under the 4 GB budget. Now at /data/models/quill-coder/quill-coder-1b-q4.gguf with its card at /data/models/quill-coder/README.md.
- Need 2, speech to text model: nothing you own covers it. No card on the shelf or in the archive states speech, audio or transcription use.
  - What to get (from the Model Shelf guide, checked November 9, 2026):
    - openai/whisper-large-v3-turbo. Speech to text. License as listed: mit. Size 1.62 GB. Open download.
    - ggerganov/whisper.cpp. Speech to text, Whisper files for whisper.cpp. License as listed: mit. ggml-large-v3-turbo-q8_0.bin is 0.87 GB. Other files in that repo go up to 3.10 GB, so check the size of any file you pick. Open download.
  - Model Shelf does not download models. Download from the model page, put it in a model folder, and run Model Shelf again.
- Did not fit: Harbor Vision 2B ("Intended use: describing images." Also "Non-commercial use only."), Tiny Lantern 1B Instruct ("Intended use: chat and instruction following in English."), Pier Sketch XL ("Intended use: image generation.").
- Not matched: /data/models/image/unknown/model.safetensors, because it is not identified and has no card.

Model Shelf quotes license lines and does not interpret them. This is not legal advice. Read the full license before you rely on it.

**Receipt (read back, all three rows match)**

1. /data/downloads/final_v2.gguf to /data/archive: source gone, destination /data/archive/final_v2.gguf present, 4268 bytes. Match.
2. /data/archive/quill-coder/quill-coder-1b-q4.gguf to /data/models/quill-coder: source gone, destination present, 4259 bytes. Match.
3. /data/archive/quill-coder/README.md to /data/models/quill-coder: source gone, destination present, 118 bytes. Match.

Bytes parked: 4268 in 1 file. Bytes brought back: 4377 in 2 files plus the card. Nothing was deleted. A parked file still uses space until you remove it yourself. If a tool or workflow loads final_v2.gguf from /data/downloads, tell me and the other copy is parked instead.

**Shelf file saved:** /data/shelf/model-shelf-20261110T065757Z_b71180b4.md (1743 bytes, confirmed present).

Note: the Devpost write-up, the extra features and the finalist odds from the original request are not part of this Model Shelf run and were not done here.
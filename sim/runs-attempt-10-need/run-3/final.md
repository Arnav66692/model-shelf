Model Shelf run complete. All three moves matched the read back, the four tags were reported added, and the shelf file was saved and confirmed.

**Shelf (5 weights files in the folders you named, plus 1 parked model in the archive)**

| File | Model name | What it does | How named | Size | License line as written | Twin |
|---|---|---|---|---|---|---|
| /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B | describes images | header and model card | 4273 bytes | "harbor-noncommercial-1.0" from header, and "license: harbor-noncommercial-1.0" from /data/models/harbor-vision/README.md | none |
| /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL | makes images | model card (header has no name) | 112 bytes | "license: openrail++" from /data/models/image/pier-sketch/README.md | none |
| /data/models/image/unknown/model.safetensors | not identified (folder hint: unknown) | not stated | not identified | 112 bytes | no license line found | none |
| /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct | chats and writes | header and model card | 4268 bytes | "license: apache-2.0" from /data/models/tiny-lantern/README.md | /data/downloads/final_v2.gguf (now moved, see receipt) |
| /data/downloads/final_v2.gguf | Tiny Lantern 1B Instruct (header only) | not stated | header | 4268 bytes | "apache-2.0" from header | /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf |

Parked models (in the archive folder before the moves): /data/archive/quill-coder/quill-coder-1b-q4.gguf, Quill Coder 1B, named by header and model card, 4259 bytes, "license: apache-2.0" from /data/archive/quill-coder/README.md.

**Space summary**
- Loose files before the moves: 13033 bytes. Tool-managed folders: 4268 bytes (/data/toolstore, never moved). Archive folder: 4259 bytes before the moves.
- Proven twins parked: 4268 bytes in 1 file.

**Duplicates**
- /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf and /data/downloads/final_v2.gguf are exact twins. Size 4268 bytes.
  SHA-256 of /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf: cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf
  SHA-256 of /data/downloads/final_v2.gguf: cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf
- The same content is also held in /data/toolstore as blob sha256-cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf, claimed by name. It stays in place.
- /data/models/image/pier-sketch/model.safetensors and /data/models/image/unknown/model.safetensors are both 112 bytes but are not twins.
  SHA-256 of pier-sketch: 5885a325e4db09b2e21579bc4733e419a3434a5dc3ac090c812fd67d13c3c468
  SHA-256 of unknown: 3f7afab5d57407d74d592eba306de220f4f0c6fd9a51ded1a1fd1ac92abf08bb

**For your job (small coding model, speech to text model, 4 GB budget)**
- Need 1, a small coding model: covered by Quill Coder 1B. Quoted from /data/archive/quill-coder/README.md: "Intended use: code completion and code chat." and "Memory: runs in about 2 GB." It is 4259 bytes, under the budget. It was brought back (see receipt).
- Did not fit need 1: Harbor Vision 2B ("Intended use: describing images."), Tiny Lantern 1B Instruct ("Intended use: chat and instruction following in English.", no coding use stated), Pier Sketch XL ("Intended use: image generation.").
- Need 2, a speech to text model: nothing you own covers it. None of the four cards states speech, audio or transcription use.
- /data/models/image/unknown/model.safetensors could not be identified, so there is no card to read.

**What to get (for need 2)**
- openai/whisper-large-v3-turbo. Task: speech to text. License as listed: mit. Size: 1.62 GB, under your 4 GB budget. Access: open download, no form to accept.
- ggerganov/whisper.cpp. Task: speech to text, ready-made Whisper files for the whisper.cpp program. License as listed: mit. Size: 0.87 GB for ggml-large-v3-turbo-q8_0.bin, under your 4 GB budget. Access: open download, no form to accept.
- Model Shelf does not download models. Get one from its model page, put it in a model folder, and run Model Shelf again. The guide was checked on November 9, 2026, so confirm the model page before you download.

**Receipt**

| File | Expected | Found | Result |
|---|---|---|---|
| final_v2.gguf | gone from /data/downloads, present in /data/archive, 4268 bytes | source missing, /data/archive/final_v2.gguf present, 4268 bytes | match |
| quill-coder-1b-q4.gguf | gone from /data/archive/quill-coder, present in /data/models/quill-coder, 4259 bytes | source missing, /data/models/quill-coder/quill-coder-1b-q4.gguf present, 4259 bytes | match |
| README.md (Quill card) | gone from /data/archive/quill-coder, present in /data/models/quill-coder, 118 bytes | source missing, /data/models/quill-coder/README.md present, 118 bytes | match |

Bytes parked: 4268 bytes in 1 file. The /data/models/quill-coder folder was created for the brought back model. The empty source folder /data/archive/quill-coder was left in place.

**Tags**
- Added: Model Shelf: Harbor Vision 2B on /data/models/harbor-vision/harbor-vision-2b.gguf
- Added: Model Shelf: Pier Sketch XL on /data/models/image/pier-sketch/model.safetensors
- Added: Model Shelf: Tiny Lantern 1B Instruct on /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf
- Added: Model Shelf: Quill Coder 1B on /data/models/quill-coder/quill-coder-1b-q4.gguf
- No tag was placed on /data/models/image/unknown/model.safetensors or /data/downloads/final_v2.gguf (now /data/archive/final_v2.gguf).
- The tags were reported added but not read back.

**Notes**
- Only the size of the moved final_v2.gguf was checked after the move. Its SHA-256 was not hashed again.
- If a tool or workflow loads final_v2.gguf from /data/downloads, tell me and the other copy can be parked instead.
- The NAS stamped the shelf file name with 20261110. The shelf text inside says 2026-11-09, the date of the run.

**Shelf file saved:** /data/shelf/model-shelf-20261110T080009Z_fca49627.md (1799 bytes, confirmed by a read-only check).
Model Shelf, run of 2026-11-09. Run complete. All approved moves, tags and the shelf save are verified.

Folders searched: /data/models, /data/downloads and /data/toolstore all exist. Archive folder /data/archive exists. Shelf folder /data/shelf exists and held no earlier model-shelf file.

Shelf (5 weights files, plus 1 tool-managed store)

| File | Model name | What it does | How named | Size (bytes) | License line as written | Twin |
|---|---|---|---|---|---|---|
| /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B | describes images | header and model card | 4273 | "license: harbor-noncommercial-1.0" (/data/models/harbor-vision/README.md) | none |
| /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL | makes images | model card | 112 | "license: openrail++" (/data/models/image/pier-sketch/README.md) | none |
| /data/models/image/unknown/model.safetensors | not identified | not stated | not identified | 112 | no license line found | none |
| /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct | chats and writes | header and model card | 4268 | "license: apache-2.0" (/data/models/tiny-lantern/README.md) | /data/archive/final_v2.gguf (moved copy) |
| /data/archive/final_v2.gguf (was /data/downloads/final_v2.gguf) | Tiny Lantern 1B Instruct | not stated (no card) | header only | 4268 | "apache-2.0" from file header, no card beside it | /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf |

Tool-managed store (listed, never moved): /data/toolstore. Its blobs folder holds 1 file, 4268 bytes, sha256-cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf, the same digest as the Tiny Lantern file. It was not touched.

Space summary: loose files were 13,033 bytes, tool-managed folders 4,427 bytes, archive 0 bytes before this run. Proven twins: 4,268 bytes in 1 file.

Duplicates, proven by SHA-256: tiny-lantern-1b-instruct-q4.gguf and final_v2.gguf both hash to cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf. pier-sketch and unknown are both 112 bytes but not twins (5885a325e4db09b2e21579bc4733e419a3434a5dc3ac090c812fd67d13c3c468 and 3f7afab5d57407d74d592eba306de220f4f0c6fd9a51ded1a1fd1ac92abf08bb).

Job answer: a small chat model for client work, memory budget 4 GB
- Need 1, chat: Tiny Lantern 1B Instruct fits. Quoted from its card: "Intended use: chat and instruction following in English." Harbor Vision 2B ("Intended use: describing images.") and Pier Sketch XL ("Intended use: image generation.") do not cover chat.
- Need 2, small footprint within 4 GB: Tiny Lantern 1B Instruct, quoted "Memory: runs in about 2 GB." Its file is 4268 bytes. This is arithmetic on file size only.
- Need 3, client work: nothing you own covers it. No card states a use for client work. Harbor Vision's card says "Non-commercial use only." Model Shelf quotes license lines and does not interpret them.

What to get
- For need 3, the guide has no entry that states client work. For the chat part under your 4 GB budget: Qwen/Qwen2.5-1.5B-Instruct-GGUF. Task: chat and following instructions, text only. License as listed: apache-2.0. Size: 1.12 GB for the q4_k_m file. Access: open download, no form to accept.
- Over budget, same task: microsoft/Phi-4-mini-instruct (mit, 7.67 GB, open download) and meta-llama/Llama-3.2-3B-Instruct (llama3.2, 6.43 GB, the page asks you to accept its license before download).
- Check the license terms on each model page yourself before any client use. Model Shelf does not download models. Download one from its page, put it in a model folder, and run Model Shelf again.

Caution: every weights file on the shelf is only a few KB, far smaller than the models their cards describe. These may be stubs or partial downloads. Check the source before you rely on any of them.

Could not match: /data/models/image/unknown/model.safetensors (no card, not identified) and /data/downloads/final_v2.gguf (header names Tiny Lantern, no card beside it; it is the exact twin of the Tiny Lantern file).

Parked models: none came back. The archive held no weights files before this run.

Moves (approved by you, verified)
- /data/downloads/final_v2.gguf to /data/archive/final_v2.gguf, 4268 bytes. Receipt: source gone, destination present at 4268 bytes. Match. Nothing was deleted. The parked file still uses space, so 0 bytes were freed.

Tags added (verified by read-back)
- /data/models/harbor-vision/harbor-vision-2b.gguf: Model Shelf: Harbor Vision 2B
- /data/models/image/pier-sketch/model.safetensors: Model Shelf: Pier Sketch XL
- /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf: Model Shelf: Tiny Lantern 1B Instruct
- No tag on the unidentified file, the parked file or the tool-managed blob.

Shelf file saved: /data/shelf/model-shelf-20261110T075956Z_1e4ea60d.md (1586 bytes, verified). The file name uses UTC, which is 23:59 PT on 2026-11-09. The text inside is dated 2026-11-09. Ask the shelf later for license or use questions, and run a full pass again to check for changes, since files can change after this date.
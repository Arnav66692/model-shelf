Model Shelf run complete (2026-11-09).

Shelf: 5 weights files in the folders you named, plus 1 tool-managed blob

| File | Model | How named | Size | License line as written | Twin |
|---|---|---|---|---|---|
| /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B | header and model card | 4273 bytes | "license: harbor-noncommercial-1.0" (/data/models/harbor-vision/README.md) | none |
| /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL | model card (header has no name) | 112 bytes | "license: openrail++" (/data/models/image/pier-sketch/README.md) | none |
| /data/models/image/unknown/model.safetensors | not identified | not identified | 112 bytes | no license line found | none |
| /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct | header and model card | 4268 bytes | "license: apache-2.0" (/data/models/tiny-lantern/README.md) | /data/downloads/final_v2.gguf |
| /data/downloads/final_v2.gguf | Tiny Lantern 1B Instruct | header only, no card beside it | 4268 bytes | general.license apache-2.0 in header | /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf |

Tool-managed, not touched: /data/toolstore (1 blob, 4268 bytes). Its name carries the same digest as the Tiny Lantern file, which is claimed by name only.

Job answer: a small chat model for client work, 4 GB memory budget
- Need 1, chat: Tiny Lantern 1B Instruct covers it. Card line: "Intended use: chat and instruction following in English." Languages: English only, per the card. License line: "license: apache-2.0".
- Need 2, 4 GB budget: Tiny Lantern's card says "Memory: runs in about 2 GB." Harbor Vision's card says "Memory: runs in about 3 GB." The file-size check (4268 bytes) is arithmetic on file size only and does not measure runtime memory.
- Does not fit chat: Harbor Vision 2B ("Intended use: describing images.", and its card also says "Non-commercial use only."). Pier Sketch XL ("Intended use: image generation.").
- Could not match: /data/models/image/unknown/model.safetensors, no name and no card.
- What to get: not needed. A model you own covers the chat need.

Plan and receipt (approved by you)
- Parked: /data/downloads/final_v2.gguf moved to /data/archive/final_v2.gguf, 4268 bytes. Name kept.
- Read-back: source path gone, destination present at 4268 bytes. Match.
- Bytes parked: 4268. No file was deleted.
- The copy kept is /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf, because it sits beside its model card. Both files have SHA-256 cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf. If any tool loads /data/downloads/final_v2.gguf from its old path, that load will now fail and the parked copy must come back.

Shelf file saved: /data/shelf/model-shelf-20261110T065655Z_4df7567f.md (1588 bytes, confirmed present). The file name uses a UTC timestamp, and the run date inside the file is 2026-11-09.

Notes
- The header read covered only the first 4096 bytes of each GGUF file. The Tiny Lantern license header had a few unreadable bytes, so the card line is the clearer source.
- Model Shelf quotes license lines and does not interpret them. Read the full Apache-2.0 license before relying on it for client work. This is not legal advice.
- The Devpost and feature request in your original message was not part of this Model Shelf step and was not done here.
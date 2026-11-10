Model Shelf run complete. One spare copy was parked, three files were tagged, and the shelf file was saved and checked.

Shelf (5 weights files)

| File | Model name | What it does | How named | Size | License line as written | Twin |
|---|---|---|---|---|---|---|
| /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B | describes images | header, model card | 4273 bytes | "license: harbor-noncommercial-1.0" (/data/models/harbor-vision/README.md) | none |
| /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL | makes images | model card | 112 bytes | "license: openrail++" (/data/models/image/pier-sketch/README.md) | none |
| /data/models/image/unknown/model.safetensors | not identified | not stated | not identified | 112 bytes | no license line found | none |
| /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct | chats and writes | header, model card | 4268 bytes | "license: apache-2.0" (/data/models/tiny-lantern/README.md) | /data/downloads/final_v2.gguf (now parked) |
| /data/downloads/final_v2.gguf (now /data/archive/final_v2.gguf) | Tiny Lantern 1B Instruct (header only) | not stated | header | 4268 bytes | "apache-2.0" (header) | /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf |

The two copies share SHA-256 cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf. The two 112-byte safetensors files have different digests, so they are not twins. /data/toolstore is a tool-managed store and was left alone.

Job answer for: a small chat model for client work, 4 GB memory budget

- Chat: covered. Tiny Lantern 1B Instruct. Quoted from /data/models/tiny-lantern/README.md: "Intended use: chat and instruction following in English." Quoted: "Memory: runs in about 2 GB." Its file is under the 4 GB budget.
- Client work: not covered by any model you own. No card states a use for client work. Harbor Vision's card says "Non-commercial use only." Tiny Lantern and Pier Sketch give license lines but no use line for client work. Model Shelf quotes license lines and does not interpret them. This is not legal advice, so read the full license before relying on any of them.

What to get
- For client work, the checked guide has no entry that states a client or commercial use, so it cannot name a model for this need. Look for a chat model under 4 GB and read its full license first. Model Shelf does not download models.

Done
- Moved: /data/downloads/final_v2.gguf to /data/archive/final_v2.gguf. Read back: source gone, destination present at 4268 bytes, match. Bytes parked: 4268. The copy in /data/models/tiny-lantern is kept because it sits beside its model card. If anything loads the file from /data/downloads, tell me and the other copy can be parked instead.
- Tags added: "Model Shelf: Harbor Vision 2B" on /data/models/harbor-vision/harbor-vision-2b.gguf, "Model Shelf: Pier Sketch XL" on /data/models/image/pier-sketch/model.safetensors, "Model Shelf: Tiny Lantern 1B Instruct" on /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf. No tag on the unidentified file or the parked file.
- Shelf saved: /data/shelf/model-shelf-2026-11-09-20261110T075942Z_5fb4792b.md, 1558 bytes, verified.

Notes
- File sizes here are 112 to 4273 bytes, so these look like small test files, not real models. A real 1B model is close to 1 GB. The memory check above is arithmetic on these sizes only.
- An earlier step ran one extra read-only duplicate scan on /data/toolstore that was not requested. It returned no duplicate groups and changed nothing.
- Nothing was deleted.
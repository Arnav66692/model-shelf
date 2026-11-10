Model Shelf run is complete. The moves, tags and shelf file were all checked.

Shelf (5 weights files)

| File | Model | What it does | Named by | Size (bytes) | License line as written | Twin |
|---|---|---|---|---|---|---|
| /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B | describes images | header | 4273 | "license: harbor-noncommercial-1.0" (/data/models/harbor-vision/README.md) | none |
| /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL | makes images | model card | 112 | "license: openrail++" (/data/models/image/pier-sketch/README.md) | none |
| /data/models/image/unknown/model.safetensors | not identified | not stated | not identified | 112 | no license line found | none (same size as pier-sketch, different digest) |
| /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct | chats and writes | header and model card | 4268 | "license: apache-2.0" (/data/models/tiny-lantern/README.md) | /data/downloads/final_v2.gguf, now parked |
| /data/archive/final_v2.gguf (was /data/downloads/final_v2.gguf) | Tiny Lantern 1B Instruct | not stated | header | 4268 | "apache-2.0" from the header | /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf |

Job answer for: a small chat model for client work, 4 GB memory budget

- Chat with clients: Tiny Lantern 1B Instruct fits. The card says: "Intended use: chat and instruction following in English." The card names English as the only language.
- Small footprint under 4 GB: Tiny Lantern is 4268 bytes on disk, and its card says "Memory: runs in about 2 GB." This is arithmetic on the card figure. It does not prove the model runs on your NAS.
- Harbor Vision 2B does not fit the chat job. Its card says "Intended use: describing images." Its license also says "Non-commercial use only." Pier Sketch XL makes images and does not fit.
- Nothing you own was missing for this job, so there is no What to get section.

Receipt

- Move /data/downloads/final_v2.gguf to /data/archive/final_v2.gguf. Expected: source gone, destination 4268 bytes. Found: source gone, destination exists at 4268 bytes. Match.
- Bytes parked: 4268. A parked file still uses space until you remove it.
- Tags added to 3 files: Model Shelf: Harbor Vision 2B, Model Shelf: Pier Sketch XL, Model Shelf: Tiny Lantern 1B Instruct.
- Nothing was deleted. The copy in /data/toolstore was not touched.

Shelf file saved: /data/shelf/model-shelf-20261110T080012Z_fae2c227.md (1505 bytes). The text inside is dated 2026-11-09, and the file name carries the UTC time of the save.

Things to know before client use

- The Tiny Lantern header license had one byte the reader could not decode. The card line "license: apache-2.0" is exact, so rely on the card and read the full Apache-2.0 license yourself.
- If a tool loads the parked copy from /data/downloads, it will now fail. Tell me and I can move the other copy instead. The copy beside its card in /data/models/tiny-lantern is still in place.
- Model Shelf quotes license lines and does not interpret them. This is not legal advice.
Model Shelf run complete on 2026-11-09. One file was moved, three files were tagged, and the shelf file was saved and checked.

**Shelf (5 weights files in your model folders, plus 1 tool-managed blob)**

| File | Model name | How named | Size (bytes) | License line as written | Twin |
|---|---|---|---|---|---|
| /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B | header | 4273 | "harbor-noncommercial-1.0" (header and /data/models/harbor-vision/README.md) | none |
| /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL | model card | 112 | "license: openrail++" (/data/models/image/pier-sketch/README.md) | none (same size as the unknown file, different SHA-256) |
| /data/models/image/unknown/model.safetensors | not identified (folder hint: unknown) | not identified | 112 | no license line found | none (same size as pier-sketch, different SHA-256) |
| /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct | header and model card | 4268 | "apache-2.0" (header and /data/models/tiny-lantern/README.md) | /data/downloads/final_v2.gguf, now parked at /data/archive/final_v2.gguf |

Tool-managed (listed, never moved): /data/toolstore/blobs/sha256-cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf, 4268 bytes. Its name matches the Tiny Lantern digest, which is a claim by name only. To remove a model from that store, use that tool's own remove command.

**Duplicates proven by SHA-256**
- /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf and /data/downloads/final_v2.gguf are exact twins, 4268 bytes each, digest cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf.
- The model copy was kept because it sits beside a model card. The downloads copy was parked.

**Receipt**

| File | Expected | Found | Result |
|---|---|---|---|
| final_v2.gguf | gone from /data/downloads, present in /data/archive, 4268 bytes | source NOT_FOUND, destination present, 4268 bytes | match |

Bytes parked: 4268 bytes in 1 file. The file still uses space in /data/archive. Nothing was deleted.

**Tags added (File Manager)**
- /data/models/harbor-vision/harbor-vision-2b.gguf: Model Shelf: Harbor Vision 2B
- /data/models/image/pier-sketch/model.safetensors: Model Shelf: Pier Sketch XL
- /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf: Model Shelf: Tiny Lantern 1B Instruct
- No tag on the unknown file, the parked copy or the tool-managed blob.

**Job answer: a small chat model for client work, 4 GB budget**
- Small model: no card uses the word small. Tiny Lantern's card says "Memory: runs in about 2 GB." and its file is 4268 bytes, under the 4 GB budget. Harbor Vision's card says "Memory: runs in about 3 GB." Pier Sketch XL states no memory line.
- Chat: Tiny Lantern 1B Instruct covers it. Its card says "Intended use: chat and instruction following in English." Harbor Vision says "Intended use: describing images." Pier Sketch XL says "Intended use: image generation."
- Client work: no card states an intended use that covers client work, so no model you own is shown to cover this need. The licenses are quoted as written, not interpreted. Tiny Lantern: "license: apache-2.0". Harbor Vision: "license: harbor-noncommercial-1.0", with the body line "Non-commercial use only." Pier Sketch XL: "license: openrail++". This is not legal advice. Read the full license before relying on any of them for client work.

**What to get (client work only)**
The model guide has no entry for client work. Its entries list tasks such as chat, code, speech, image and embeddings, and none names client work, so nothing is picked for this need. Look for a model page that states a use covering client work, a file size under 4 GB, and a license you have read in full. Model Shelf does not download models. Download one from its model page, put it in a model folder, and run Model Shelf again.

**Checks to know about**
- The header read of the Tiny Lantern file showed one stray character after "apache-2.0". The model card line has none, so the license line is taken from the card.
- If a tool loads /data/downloads/final_v2.gguf from its old path, tell me. The kept copy is /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf, and the other copy would be parked instead.

**Shelf file saved and checked**
- /data/shelf/model-shelf-20261110T073731Z_77f5376d.md, 1534 bytes. The date in the name is UTC, so it reads November 10. The run was November 9 Pacific time.

Nothing is pending. No other files were moved, tagged or changed.
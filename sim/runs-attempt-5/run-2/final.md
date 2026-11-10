Model Shelf run complete. One file was parked and the shelf file was saved.

Shelf (5 weights files in the folders you named, plus one tool-managed store)

| File | Model name | How named | Size | License line as written | Twin |
|---|---|---|---|---|---|
| /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B | header and model card | 4273 bytes | card: "license: harbor-noncommercial-1.0" | none |
| /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL | model card | 112 bytes | card: "license: openrail++" | none |
| /data/models/image/unknown/model.safetensors | not identified (folder hint: unknown) | not identified | 112 bytes | no license line found | none (same size as pier-sketch, different digest) |
| /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct | header and model card | 4268 bytes | card: "license: apache-2.0" | /data/downloads/final_v2.gguf (kept) |
| /data/downloads/final_v2.gguf | Tiny Lantern 1B Instruct | header | 4268 bytes, now parked | header: "apache-2.0" | /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf |

Tool-managed (listed, never moved): /data/toolstore holds 1 blob, 4268 bytes, with the same SHA-256 as the Tiny Lantern file. Remove models from that store with the tool's own remove command.

Job answer: small chat model for client work, 4 GB budget
- Tiny Lantern 1B Instruct fits the chat part. Card line: "Intended use: chat and instruction following in English." Card line: "Memory: runs in about 2 GB." The file is under your 4 GB budget. The card does not mention client work, so that fit is not stated.
- Harbor Vision 2B does not fit. Card line: "Intended use: describing images."
- Pier Sketch XL does not fit. Card line: "Intended use: image generation."
- /data/models/image/unknown/model.safetensors could not be matched. No card and no name.

Duplicates: /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf and /data/downloads/final_v2.gguf are exact twins, both SHA-256 cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf. The two 112 byte model.safetensors files are not twins.

Receipt
| Move | Expected | Found | Result |
|---|---|---|---|
| /data/downloads/final_v2.gguf to /data/archive/final_v2.gguf | source gone, destination present at 4268 bytes | source NOT_FOUND, destination file at 4268 bytes | match |

Bytes parked: 4268. Parked files still use space until you remove them.

Saved shelf file: /data/shelf/model-shelf-20261110T054655Z_b017b070.md, 1462 bytes. The name uses UTC, so this run is 2026-11-09 21:46 PT.

Nothing was deleted. Nothing outside the one approved move was touched.
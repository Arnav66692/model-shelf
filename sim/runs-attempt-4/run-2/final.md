Model Shelf run complete.

Shelf (5 weights files in the folders you named, plus 1 tool-managed blob)

| File | Model name | How named | Size | License line as written | Twin |
|---|---|---|---|---|---|
| /data/downloads/final_v2.gguf (now /data/archive/final_v2.gguf) | Tiny Lantern 1B Instruct | header | 4268 bytes | "license: apache-2.0" from /data/models/tiny-lantern/README.md (header also reads apache-2.0 with a stray trailing byte) | /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf |
| /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B | header | 4273 bytes | "license: harbor-noncommercial-1.0" from /data/models/harbor-vision/README.md | none |
| /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct | header | 4268 bytes | "license: apache-2.0" from /data/models/tiny-lantern/README.md | /data/downloads/final_v2.gguf (now archived) |
| /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL | model card | 112 bytes | "license: openrail++" from /data/models/image/pier-sketch/README.md | none |
| /data/models/image/unknown/model.safetensors | not identified (folder hint: unknown) | not identified | 112 bytes | no license line found | none |

Tool-managed (listed, never moved): /data/toolstore holds one blob, 4268 bytes, sha256-cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf. It has the same digest as the twin pair and stays where it is.

Job answer: a small chat model for client work, 4 GB budget
- Fits: Tiny Lantern 1B Instruct (/data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf). Card line: "Intended use: chat and instruction following in English." Card line: "Memory: runs in about 2 GB." The card names English only and has no separate supported-languages line. File size is 4268 bytes, under the 4 GB budget, which compares file size only and does not promise it will run.
- Does not fit: Harbor Vision 2B. Card line: "Intended use: describing images." It states no chat use. Card also says "Non-commercial use only."
- Does not fit: Pier Sketch XL. Card line: "Intended use: image generation." It states no chat use.
- Could not match: /data/models/image/unknown/model.safetensors. No name and no card, so there is nothing to read.

Duplicates: /data/downloads/final_v2.gguf and /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf are exact twins. Both SHA-256 digests are cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf. The two 112-byte safetensors files are not twins (digests differ).

Receipt (you approved the move)
| Move | Expected | Found | Result |
|---|---|---|---|
| /data/downloads/final_v2.gguf to /data/archive/final_v2.gguf | source gone, destination 4268 bytes | source NOT_FOUND, destination file 4268 bytes | match |

Bytes parked: 4268 bytes in 1 file. Nothing was deleted, and the parked file still uses space in /data/archive until you remove it yourself. I cannot check whether any tool or workflow loads /data/downloads/final_v2.gguf from its old path. If one does, it will now fail to find that file.

Shelf file saved: /data/shelf/model-shelf-20261110T053245Z_b6da9526.md (1575 bytes). The name carries the UTC date, 2026-11-10. The text inside is dated 2026-11-09.
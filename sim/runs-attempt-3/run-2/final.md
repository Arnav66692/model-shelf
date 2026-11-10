Model Shelf run complete for 2026-11-09. The one approved move is done and checked, and the shelf file is saved.

Shelf table (5 weights files, plus 1 tool-managed blob)

| File | Model name | How named | Size | License line as written | Twin |
|---|---|---|---|---|---|
| /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B | header and model card | 4273 bytes | "license: harbor-noncommercial-1.0" (/data/models/harbor-vision/README.md) | none |
| /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct | header and model card | 4268 bytes | "license: apache-2.0" (/data/models/tiny-lantern/README.md) | /data/archive/final_v2.gguf (formerly /data/downloads/final_v2.gguf) |
| /data/archive/final_v2.gguf (formerly /data/downloads/final_v2.gguf) | Tiny Lantern 1B Instruct | header only | 4268 bytes | "general.license" followed by apache-2.0 (header) | /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf |
| /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL | model card | 112 bytes | "license: openrail++" (/data/models/image/pier-sketch/README.md) | none |
| /data/models/image/unknown/model.safetensors | not identified (folder hint: unknown) | not identified | 112 bytes | no license line found | none |

Tool-managed: /data/toolstore holds one blob, sha256-cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf, 4268 bytes. It has the same content as tiny-lantern. It was listed and not moved.

Changed since last shelf: no earlier shelf file was found, so there is nothing to compare.

Job answer: a small chat model for client work, 4 GB budget
- Fits: Tiny Lantern 1B Instruct. Card line: "Intended use: chat and instruction following in English." Card line: "Memory: runs in about 2 GB." That is under the 4 GB budget.
- Does not fit: Harbor Vision 2B. Card line: "Intended use: describing images." The same card also says "Non-commercial use only." Pier Sketch XL. Card line: "Intended use: image generation."
- Could not match: /data/models/image/unknown/model.safetensors has no card. The copy of final_v2.gguf had no card beside it at its original location.

Warning before you rely on Tiny Lantern: the file is 4268 bytes, but its card says it needs about 2 GB. A real 1B model would be far larger. The header is readable and names the model, so the file may be a stub or a truncated download. Check it is complete before using it for client work. Every weights file on this shelf is only a few kilobytes.

Receipt
| Move | Expected | Found | Result |
|---|---|---|---|
| /data/downloads/final_v2.gguf to /data/archive/final_v2.gguf | source gone, destination exists, 4268 bytes | source gone, destination exists, 4268 bytes | match |

The receipt checks existence and size only. The parked file was not hashed again after the move. Its digest before the move was cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf, the same as tiny-lantern.

Bytes parked: 4268. Nothing was deleted, and the parked file still uses disk space.

Shelf file saved: /data/shelf/model-shelf-20261110T052407Z_e203582f.md, 1549 bytes, confirmed present. The timestamp in the name is UTC, which is 2026-11-09 21:24 PT.
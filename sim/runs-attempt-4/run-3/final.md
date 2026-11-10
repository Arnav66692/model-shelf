Model Shelf run complete. One file was parked and the shelf file is saved.

**Shelf table (scan taken before the move)**

| File | Model name | How named | Size | License line as written | Twin |
|---|---|---|---|---|---|
| /data/downloads/final_v2.gguf | Tiny Lantern 1B Instruct | header | 4268 bytes | "apache-2.0" (header) | /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf |
| /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B | header | 4273 bytes | "harbor-noncommercial-1.0" (header and README.md) | none |
| /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct | header | 4268 bytes | "apache-2.0" (header and README.md) | /data/downloads/final_v2.gguf |
| /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL | model card | 112 bytes | "license: openrail++" (README.md) | none |
| /data/models/image/unknown/model.safetensors | not identified | not identified | 112 bytes | no license line found | none |

Tool-managed: /data/toolstore holds one blob, 4268 bytes, sha256-cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf. It was listed only and not moved.

Changed since the last shelf: no earlier shelf file was found, so nothing to compare.

**Job answer: small chat model for client work (memory budget 4 GB)**
- Fits: Tiny Lantern 1B Instruct. Card line: "Intended use: chat and instruction following in English." Card memory line: "Memory: runs in about 2 GB." Under the 4 GB budget. License line: "license: apache-2.0", quoted, not interpreted. This is not legal advice.
- Does not fit: Harbor Vision 2B. Card line: "Intended use: describing images." It also says "Non-commercial use only."
- Does not fit: Pier Sketch XL. Card line: "Intended use: image generation."
- Could not match: /data/models/image/unknown/model.safetensors, since nothing identifies it.

**Plan and receipt**
- Parked: /data/downloads/final_v2.gguf (4268 bytes) to /data/archive/final_v2.gguf. Reason: exact duplicate of /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf (same SHA-256 cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf). The tiny-lantern copy was kept because it sits beside its model card.
- Receipt: source /data/downloads/final_v2.gguf expected gone, found gone. Destination /data/archive/final_v2.gguf expected present at 4268 bytes, found present at 4268 bytes. Result: match.
- Bytes parked: 4268. Nothing was deleted, and the parked file still uses space until you remove it yourself.

**Caveats**
- Anything that loads the model from /data/downloads/final_v2.gguf will now find nothing there. I cannot see whether a tool does this, so please check.
- The archived copy was not re-hashed after the move. The digest match was taken before the move.

**Saved shelf file:** /data/shelf/model-shelf-20261110T053235Z_c36c0503.md (1387 bytes, confirmed to exist). The timestamp is UTC, which is 9:32 PM PT on Nov 9, 2026.
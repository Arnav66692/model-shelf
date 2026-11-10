Model Shelf run complete (2026-11-09). One move was approved and made, and the shelf file is saved. Nothing was deleted.

**Shelf table**

| File | Model name (named by) | Size | License line as written (source) | Exact twin |
|---|---|---|---|---|
| /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B (header and model card) | 4273 bytes | "license: harbor-noncommercial-1.0" (model card) | none |
| /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL (model card) | 112 bytes | "license: openrail++" (model card) | none |
| /data/models/image/unknown/model.safetensors | not identified (no name in header, no model card in folder) | 112 bytes | no license line found | none, SHA-256 differs from pier-sketch |
| /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct (header and model card) | 4268 bytes | "license: apache-2.0" (model card) | /data/archive/final_v2.gguf (was /data/downloads/final_v2.gguf) |
| /data/archive/final_v2.gguf (moved from /data/downloads/final_v2.gguf) | Tiny Lantern 1B Instruct (header only) | 4268 bytes | "apache-2.0" (header) | /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf |

Tool-managed store: /data/toolstore holds one blob, sha256-cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf (4268 bytes). Its name carries the same digest as the two Tiny Lantern copies. That match is by name only. The blob was not read, hashed or moved.

Duplicates proven by SHA-256: tiny-lantern-1b-instruct-q4.gguf and final_v2.gguf both hash to cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf. The two 112-byte files are not twins.

**Job answer** (job: a small chat model for client work; memory budget 4 GB)

- Tiny Lantern 1B Instruct covers chat. Card line: "Intended use: chat and instruction following in English." Card line: "Memory: runs in about 2 GB." That is inside the 4 GB budget. The card does not mention client work, and it states English only.
- Harbor Vision 2B does not show a chat use. Card line: "Intended use: describing images." Card line: "Non-commercial use only." Card line: "Memory: runs in about 3 GB."
- Pier Sketch XL does not fit this job. Card line: "Intended use: image generation."
- The unknown 112-byte model has no card, so it cannot be matched to the job.

Check before relying on these: every weights file here is only a few kilobytes (the largest is 4273 bytes). A real 1B chat model is gigabytes, so these may be stub or placeholder files. Confirm the copies are the real models.

**Receipt**

| Move | Expected | Found | Result |
|---|---|---|---|
| /data/downloads/final_v2.gguf to /data/archive/final_v2.gguf | source gone, destination present at 4268 bytes | source gone, destination present at 4268 bytes | match |

Bytes parked: 4268. A parked file still uses space until you remove it. Bytes freed: not reported.

**Shelf file**

Saved: /data/shelf/model-shelf-20261110T053216Z_97e6b9a7.md (1456 bytes, confirmed present). The file name carries a UTC stamp, so it reads as 2026-11-10 even though the run was on 2026-11-09 Pacific time.

No earlier shelf file was found, so there is no changed-since-last-shelf list.
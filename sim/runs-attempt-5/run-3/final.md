Model Shelf run complete. Moved one file and saved the shelf file.

Shelf (5 loose weights files, plus 1 tool-managed blob)

| File | Model name | How named | Size | License line as written | Twin |
|---|---|---|---|---|---|
| /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B | header | 4273 bytes | "harbor-noncommercial-1.0" (header and /data/models/harbor-vision/README.md). The card body also reads "Non-commercial use only." | none |
| /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL | model card (/data/models/image/pier-sketch/README.md) | 112 bytes | "license: openrail++" (/data/models/image/pier-sketch/README.md) | none |
| /data/models/image/unknown/model.safetensors | not identified (folder hint: unknown) | not identified | 112 bytes | no license line found | none |
| /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct | header | 4268 bytes | "apache-2.0" (header and /data/models/tiny-lantern/README.md) | /data/downloads/final_v2.gguf (moved, see receipt) |
| /data/downloads/final_v2.gguf (now /data/archive/final_v2.gguf) | Tiny Lantern 1B Instruct | header | 4268 bytes | "apache-2.0" (header) | /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf |

Tool-managed (listed, not moved): /data/toolstore. Its blobs folder holds 1 file, 4268 bytes, sha256-cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf. Same digest as the Tiny Lantern copy. Left in place.

Duplicates (SHA-256 checked)
- /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf and /data/downloads/final_v2.gguf are exact twins: cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf.
- /data/models/image/pier-sketch/model.safetensors (5885a325e4db09b2e21579bc4733e419a3434a5dc3ac090c812fd67d13c3c468) and /data/models/image/unknown/model.safetensors (3f7afab5d57407d74d592eba306de220f4f0c6fd9a51ded1a1fd1ac92abf08bb) are both 112 bytes but not twins.

Job answer: a small chat model for client work, 4 GB budget
- Fits: Tiny Lantern 1B Instruct (/data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf). Card line: "Intended use: chat and instruction following in English." Card line: "Memory: runs in about 2 GB." Its file is 4268 bytes, under the budget. This is arithmetic on file size only. No card says "client work," so the fit rests on the chat line.
- Does not fit: Harbor Vision 2B ("Intended use: describing images.") and Pier Sketch XL ("Intended use: image generation.").
- Could not match: /data/models/image/unknown/model.safetensors, because it has no card and no header name.
- Model Shelf quotes license lines and does not interpret them. This is not legal advice.

Receipt
- /data/downloads/final_v2.gguf to /data/archive/final_v2.gguf: source gone (expected), destination present, 4268 bytes (expected 4268). Match.
- Bytes parked: 4268. Parked files still use disk space until you remove them.
- The receipt checks size and presence. The archived copy was not hashed again after the move.

Shelf file saved: /data/shelf/model-shelf-2026-11-09-20261110T054642Z_225f0411.md (1491 bytes, confirmed present).

Nothing was deleted. /data/archive was already present and empty, and no other file was touched.
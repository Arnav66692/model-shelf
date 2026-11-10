Model Shelf run complete, 2026-11-09. One file was parked. Nothing was deleted.

Shelf (5 weights files in /data/models and /data/downloads)

1. /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B | header | 4273 bytes | "harbor-noncommercial-1.0" (header), "license: harbor-noncommercial-1.0" (model card) | twin: none
2. /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct | header | 4268 bytes | "license: apache-2.0" (model card) | twin: /data/downloads/final_v2.gguf
3. /data/downloads/final_v2.gguf | Tiny Lantern 1B Instruct | header | 4268 bytes | "apache-2.0" (header) | twin: /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf
4. /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL (folder hint: pier-sketch) | model card | 112 bytes | "license: openrail++" (model card) | twin: none
5. /data/models/image/unknown/model.safetensors | not identified (folder hint: unknown) | not identified | 112 bytes | no license line found | twin: none

Tool-managed folders (listed, never moved)
- /data/toolstore holds 1 file in its blobs folder, 4268 bytes. It was not read, hashed or moved.

Duplicates
- /data/downloads/final_v2.gguf and /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf are exact twins. Size 4268 bytes.
  SHA-256 of /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf: cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf
  SHA-256 of /data/downloads/final_v2.gguf: cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf
- The same digest is in the name of the toolstore blob. That is a claim by name only, and it stays in place.
- The two 112 byte files (pier-sketch and unknown) have different digests, so they are not twins.

Changed since the last shelf: none. No earlier model-shelf file existed.

Job answer (job: a small chat model for client work, memory budget 4 GB)
- Tiny Lantern 1B Instruct matches on its card line "Intended use: chat and instruction following in English." Its card also says "Memory: runs in about 2 GB." The card does not mention client work, and it limits use to English.
- Harbor Vision 2B does not match. Its card says "Intended use: describing images." and "Non-commercial use only."
- Pier Sketch XL does not match. Its card says "Intended use: image generation."
- The unknown safetensors file has no card, so it cannot be matched.
- Check before client work: both Tiny Lantern copies are only 4268 bytes. A real 1B model file is much larger, so this may be a placeholder or a truncated download. I have not confirmed that it is usable.

Receipt
| File | Expected | Found | Result |
| final_v2.gguf | gone from /data/downloads, present in /data/archive, 4268 bytes | source NOT_FOUND, destination is a file of 4268 bytes | match |

Bytes parked: 4268 bytes in 1 file. A parked file still uses space until you remove it. The receipt checks presence and size. I did not recompute the SHA-256 of the archived copy after the move.

Moved: /data/downloads/final_v2.gguf to /data/archive/final_v2.gguf.

Shelf file saved: /data/shelf/model-shelf-20261110T054639Z_83be1a50.md, 1378 bytes. The NAS named it in UTC, so the date in the name is 2026-11-10 while this run is dated 2026-11-09.
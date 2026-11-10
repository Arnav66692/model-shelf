Model Shelf run complete. One file parked, three files tagged, shelf file saved and confirmed.

Shelf (5 weights files in the folders you named)

| File | Model name | How named | Quant | Size | License line as written | Twin |
|---|---|---|---|---|---|---|
| /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B | header and model card | not shown | 4273 bytes | "license: harbor-noncommercial-1.0" from /data/models/harbor-vision/README.md (the header also reads harbor-noncommercial-1.0) | none |
| /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL | model card (the header has no name) | not shown | 112 bytes | "license: openrail++" from /data/models/image/pier-sketch/README.md | none |
| /data/models/image/unknown/model.safetensors | not identified (folder hint: unknown) | not identified | not shown | 112 bytes | no license line found | none |
| /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct | header and model card | q4 (from file name) | 4268 bytes | "license: apache-2.0" from /data/models/tiny-lantern/README.md (the header agrees) | /data/archive/final_v2.gguf (parked copy, see below) |

Parked models (in the archive folder)
- /data/archive/final_v2.gguf. Tiny Lantern 1B Instruct, named by header. 4268 bytes. License line: "general.license" apache-2.0 from the header.

Space summary
- Loose files in model folders now: 8765 bytes. Tool-managed folders: 4268 bytes in blobs plus a 159-byte manifest. Archive folder: 4268 bytes.
- Proven twins parked: 4268 bytes in 1 file. Parking does not free space.

Tool-managed folders (listed, never moved)
- /data/toolstore. 1 file in its blobs folder, 4268 bytes, named sha256-cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf. This is the same content as the Tiny Lantern file by name only, and it stays in place.

Duplicates
- /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf (kept, beside its README) and /data/downloads/final_v2.gguf (now /data/archive/final_v2.gguf) are exact twins. Size 4268 bytes.
  SHA-256 of the kept file: cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf
  SHA-256 of final_v2.gguf: cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf
- /data/models/image/pier-sketch/model.safetensors and /data/models/image/unknown/model.safetensors share a size of 112 bytes but are not twins. SHA-256 of pier-sketch: 5885a325e4db09b2e21579bc4733e419a3434a5dc3ac090c812fd67d13c3c468. SHA-256 of unknown: 3f7afab5d57407d74d592eba306de220f4f0c6fd9a51ded1a1fd1ac92abf08bb.

Changed since the last shelf: none. This was the first shelf file in /data/shelf.

For your job: a small chat model for client work, memory budget 4 GB

Need 1. A small model
- Covered only by size. No card has a use line that says small. Tiny Lantern 1B Instruct is 4268 bytes, under the 4 GB budget, and its card says "Memory: runs in about 2 GB."

Need 2. A chat model
- On the shelf: Tiny Lantern 1B Instruct (/data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf, 4268 bytes). Use, quoted from /data/models/tiny-lantern/README.md: "Intended use: chat and instruction following in English."

Need 3. Client work
- Nothing you own covers this. No card states a use for client work. Harbor Vision 2B's card says "Non-commercial use only." (quoted from /data/models/harbor-vision/README.md). Tiny Lantern's card states only "license: apache-2.0".

Did not fit
- Harbor Vision 2B. Use, quoted from /data/models/harbor-vision/README.md: "Intended use: describing images."
- Pier Sketch XL. Use, quoted from /data/models/image/pier-sketch/README.md: "Intended use: image generation."

Could not match
- /data/models/image/unknown/model.safetensors. Not identified, so there is no card to read.

What to get (from the Model Shelf guide, checked November 9, 2026)
- For need 3, the guide has no entry for client work. Look for a model with a chat task, a file size under 4 GB, and a license line you have read in full.
- Model Shelf does not download models. Download from the model page, put the file in a model folder, and run Model Shelf again.
- Check the Tiny Lantern file before you rely on it. The NAS reports 4268 bytes, while the guide lists about 1.12 GB for a 1.5B q4 file. It may be a placeholder or a partial download.

Model Shelf quotes license lines and does not interpret them. This is not legal advice. Read the full license before you rely on it.

Receipt

| File | Expected | Found | Result |
|---|---|---|---|
| final_v2.gguf | gone from /data/downloads, present in /data/archive, 4268 bytes | source not found, /data/archive/final_v2.gguf exists, 4268 bytes | match |

Bytes parked: 4268 bytes in 1 file.

Tags added
- /data/models/harbor-vision/harbor-vision-2b.gguf: Model Shelf: Harbor Vision 2B
- /data/models/image/pier-sketch/model.safetensors: Model Shelf: Pier Sketch XL
- /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf: Model Shelf: Tiny Lantern 1B Instruct
- /data/models/image/unknown/model.safetensors: no tag, not identified. final_v2.gguf: no tag, parked.

Shelf file saved: /data/shelf/model-shelf-20261110T073716Z_6fcf27e4.md (1598 bytes, confirmed). Ask the shelf any time for a question on this saved file. Files can change after this date, so a full run checks them again.
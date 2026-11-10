Model Shelf run complete. The one approved move, three tags and the shelf save are done, and the move was read back and matches.

Shelf (5 weights files in /data/models and /data/downloads, plus the tool-managed /data/toolstore)

| File | Model name | How named | Size | License line as written | Twin |
|---|---|---|---|---|---|
| /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B | header | 4273 bytes | "license: harbor-noncommercial-1.0" from /data/models/harbor-vision/README.md (header agrees) | none |
| /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct | header and model card | 4268 bytes | "license: apache-2.0" from /data/models/tiny-lantern/README.md. The header reads "apache-2.08", so the two differ and the header value is unconfirmed. | /data/archive/final_v2.gguf (moved from /data/downloads) |
| /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL | model card | 112 bytes | "license: openrail++" from /data/models/image/pier-sketch/README.md | none |
| /data/models/image/unknown/model.safetensors | not identified (folder hint: unknown) | not identified | 112 bytes | no license line found | none |

Parked models (in /data/archive)
- /data/archive/final_v2.gguf. Tiny Lantern 1B Instruct, named by header. 4268 bytes. License line: "apache-2.08" from the header only, no card beside it.

Space summary
- Loose files before the move: 13033 bytes. Tool-managed /data/toolstore: 4268 bytes. Archive now: 4268 bytes.
- Bytes parked: 4268 bytes in 1 file. Nothing was freed, because the parked file still uses space.

Tool-managed folders (listed, never moved)
- /data/toolstore. 1 file in its blobs folder, 4268 bytes, named sha256-cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf. It has the same digest as the Tiny Lantern file.

Duplicates
- /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf and /data/downloads/final_v2.gguf are exact twins. Size 4268 bytes.
  SHA-256 of the models copy (kept, it sits beside its model card): cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf
  SHA-256 of the downloads copy (parked): cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf
- The pier-sketch and unknown files are both 112 bytes but are not twins.
  SHA-256 of pier-sketch: 5885a325e4db09b2e21579bc4733e419a3434a5dc3ac090c812fd67d13c3c468
  SHA-256 of unknown: 3f7afab5d57407d74d592eba306de220f4f0c6fd9a51ded1a1fd1ac92abf08bb

For your job: a small chat model for client work, memory budget 4 GB

Need 1. Small (a size limit, not a use)
- On the shelf: Tiny Lantern 1B Instruct. Memory, quoted from /data/models/tiny-lantern/README.md: "Memory: runs in about 2 GB." File size 4268 bytes is under the 4 GB budget. This is arithmetic on file size only. The card figure and the file size do not match, so the file may be a stub or partial download.

Need 2. A chat model
- On the shelf: Tiny Lantern 1B Instruct. Use, quoted from /data/models/tiny-lantern/README.md: "Intended use: chat and instruction following in English."

Need 3. Client work
- Nothing you own covers this need. No card states a use for client work.

Did not fit
- Harbor Vision 2B. "Intended use: describing images." This does not cover chat. The same card also reads, quoted from /data/models/harbor-vision/README.md: "Non-commercial use only."
- Pier Sketch XL. "Intended use: image generation." This does not cover chat.

Could not match
- /data/models/image/unknown/model.safetensors. Not identified, so there is no card to read.

What to get (from the Model Shelf guide, checked November 9, 2026)
- For need 3 (client work): the guide has no entry for client work, so I am not picking a model. Look for a model card that states a use for client work, a file under 4 GB, and a license line you have read yourself. The guide's entries cover chat, coding, speech, image and embedding tasks only.
Model Shelf does not download models. Download from the model page, put the file in a model folder, and run Model Shelf again.

Model Shelf quotes license lines and does not interpret them. This is not legal advice. Read the full license before you rely on it.

Receipt

| File | Expected | Found | Result |
|---|---|---|---|
| final_v2.gguf | gone from /data/downloads, present in /data/archive, 4268 bytes | /data/downloads/final_v2.gguf gone, /data/archive/final_v2.gguf present, 4268 bytes | match |

Bytes parked: 4268 bytes in 1 file.

Tags added
- /data/models/harbor-vision/harbor-vision-2b.gguf: Model Shelf: Harbor Vision 2B
- /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf: Model Shelf: Tiny Lantern 1B Instruct
- /data/models/image/pier-sketch/model.safetensors: Model Shelf: Pier Sketch XL
- The unknown file and the archived copy got no tag.

Shelf file saved: /data/shelf/model-shelf-20261110T072559Z_abe5c3ed.md, 1597 bytes. The NAS stamp is 11:25 PM PST on 2026-11-09.

Things to check
- If anything loads /data/downloads/final_v2.gguf by path, it will now fail. Copy it back from /data/archive/final_v2.gguf. Nothing was deleted.
- The Tiny Lantern license lines differ, "apache-2.0" on the card and "apache-2.08" in the header. Read the full license on the model page before any client use.
- The memory lines on the cards (about 2 GB and about 3 GB) do not match the file sizes (about 4 KB each). Check the files before you rely on them.
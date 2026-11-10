Model Shelf run complete for 2026-11-09. The approved move matches its read-back, and the shelf file is saved.

SHELF (weights files in the folders you named)

| File | Model name | How named | Size | License line as written | Twin |
|---|---|---|---|---|---|
| /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B | header | 4273 bytes | Header: "harbor-noncommercial-1.0". Card /data/models/harbor-vision/README.md: "license: harbor-noncommercial-1.0" | none |
| /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct | header | 4268 bytes | Header: "apache-2.0". Card /data/models/tiny-lantern/README.md: "license: apache-2.0" | /data/downloads/final_v2.gguf, now parked at /data/archive/final_v2.gguf |
| /data/downloads/final_v2.gguf (now /data/archive/final_v2.gguf) | Tiny Lantern 1B Instruct | header | 4268 bytes | Header: "apache-2.0". No model card beside it | /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf |
| /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL (folder hint: pier-sketch) | model card | 112 bytes | Card /data/models/image/pier-sketch/README.md: "license: openrail++" | none |
| /data/models/image/unknown/model.safetensors | not identified (folder hint: unknown) | not identified | 112 bytes | No license line found | none |

Tool-managed, listed and not moved: /data/toolstore holds one blob, sha256-cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf, 4268 bytes. Its name claims the same content as the tiny-lantern file. It stays in place.

DUPLICATE PROOF (full SHA-256)
- /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf: cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf
- /data/downloads/final_v2.gguf: cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf
These two are exact twins.
- /data/models/image/pier-sketch/model.safetensors: 5885a325e4db09b2e21579bc4733e419a3434a5dc3ac090c812fd67d13c3c468
- /data/models/image/unknown/model.safetensors: 3f7afab5d57407d74d592eba306de220f4f0c6fd9a51ded1a1fd1ac92abf08bb
These two are the same size but not twins.

JOB ANSWER: a small chat model for client work, 4 GB memory budget
- Fits: Tiny Lantern 1B Instruct, /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf, 4268 bytes. Card line: "Intended use: chat and instruction following in English." Card line: "Memory: runs in about 2 GB." The file is under the 4 GB budget. That is arithmetic on file size only, and it does not promise the model will run. License lines are quoted, not interpreted. This is not legal advice. Read the full license before you rely on it.
- Did not fit: Harbor Vision 2B ("Intended use: describing images.") and Pier Sketch XL ("Intended use: image generation.").
- Could not match: /data/models/image/unknown/model.safetensors, not identified.

RECEIPT (you answered yes to the one approved move)
- /data/downloads/final_v2.gguf to /data/archive. Expected: source gone, destination present at 4268 bytes. Found: source gone, destination present at 4268 bytes. Match.
- /data/archive did not exist, so it was created before the move.
- Bytes parked: 4268. Bring back: none. A parked file still uses space until you remove it, so nothing was freed. Nothing was deleted, and no other file was touched.

SAVED SHELF FILE: /data/shelf/model-shelf-20261110T051626Z_32821223.md, 3615 bytes, confirmed present. The file name's timestamp is UTC, so it reads 2026-11-10 even though this run is dated 2026-11-09 Pacific time.

This is the first shelf file in /data/shelf, so there is no Changed since the last shelf section.
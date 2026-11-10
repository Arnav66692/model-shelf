Model Shelf run complete. One file was parked, nothing was deleted, and the shelf file is saved.

**Shelf (5 weights files in /data/models, /data/downloads and /data/toolstore)**

| File | Model name | How named | Size | License line as written | Twin |
|---|---|---|---|---|---|
| /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B | header and model card | 4273 bytes | "license: harbor-noncommercial-1.0" from /data/models/harbor-vision/README.md (header also says harbor-noncommercial-1.0) | none |
| /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct | header and model card | 4268 bytes | "license: apache-2.0" from /data/models/tiny-lantern/README.md (header also says apache-2.0) | /data/downloads/final_v2.gguf, now moved to /data/archive/final_v2.gguf |
| /data/downloads/final_v2.gguf (moved) | Tiny Lantern 1B Instruct, from header only | header only, no card beside it | 4268 bytes | "apache-2.0" from file header | /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf |
| /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL | model card | 112 bytes | "license: openrail++" from /data/models/image/pier-sketch/README.md | none |
| /data/models/image/unknown/model.safetensors | not identified (folder name is only a hint) | not identified | 112 bytes | no license line found | none |

The toolstore folder is tool-managed. It holds one blob, sha256-cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf (4268 bytes). That name matches the tiny-lantern digest. It was listed only and not moved.

**Duplicate proof**
- /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf and /data/downloads/final_v2.gguf are exact twins. Both are 4268 bytes, and both SHA-256 digests are cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf.
- /data/models/image/pier-sketch/model.safetensors and /data/models/image/unknown/model.safetensors are both 112 bytes but are not twins. Their digests are 5885a325e4db09b2e21579bc4733e419a3434a5dc3ac090c812fd67d13c3c468 and 3f7afab5d57407d74d592eba306de220f4f0c6fd9a51ded1a1fd1ac92abf08bb.

**Job answer: a small chat model for client work, 4 GB budget**
- Fits: Tiny Lantern 1B Instruct, /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf. Its card says "Intended use: chat and instruction following in English." and "Memory: runs in about 2 GB." The file is 4268 bytes, under the 4 GB budget. That comparison uses file size only.
- Does not fit: Harbor Vision 2B. Its card says "Intended use: describing images."
- Does not fit: Pier Sketch XL. Its card says "Intended use: image generation."
- Could not match: /data/models/image/unknown/model.safetensors has no card, and /data/downloads/final_v2.gguf had no card beside it when it was checked. Model Shelf does not suggest any model you do not own.

**Parked (approved by you)**
- Moved /data/downloads/final_v2.gguf to /data/archive/final_v2.gguf. Reason: exact duplicate of the tiny-lantern copy, same SHA-256. The archive folder held no file with that name.
- Bytes parked: 4268. Bytes freed: not reported. The parked copy still uses space until you remove it yourself.

**Receipt**

| Move | Expected | Found | Match |
|---|---|---|---|
| /data/downloads/final_v2.gguf to /data/archive | source absent, destination present at 4268 bytes | source absent, /data/archive/final_v2.gguf present at 4268 bytes | match |

**Saved shelf file**
/data/shelf/model-shelf-20261110T051643Z_1d80e176.md, 3243 bytes, confirmed present. The file name uses UTC, so the stamp is Nov 9 at about 9:16 PM Pacific time. No earlier shelf file was found, so there is no changed-since section.

License lines are quoted as written and not interpreted. This is not legal advice. Read the full license before relying on it.
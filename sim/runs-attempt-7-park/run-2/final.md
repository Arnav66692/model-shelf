Model Shelf run complete. The move, the three tags and the shelf file are done and read back. Nothing was deleted.

**Shelf (5 loose weights files, as scanned before the move)**

| File | Model name | How named | Size (bytes) | License line as written | Twin | Status |
|---|---|---|---|---|---|---|
| /data/downloads/final_v2.gguf | Tiny Lantern 1B Instruct | header | 4268 | "apache-2.0" from file header, not confirmed (one stray character in the read) | /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Parked to /data/archive/final_v2.gguf |
| /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct | header, model card | 4268 | "license: apache-2.0" from /data/models/tiny-lantern/README.md | /data/downloads/final_v2.gguf | Kept, tagged |
| /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B | header, model card | 4273 | "license: harbor-noncommercial-1.0" from /data/models/harbor-vision/README.md | none | Tagged |
| /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL | model card | 112 | "license: openrail++" from /data/models/image/pier-sketch/README.md | none | Tagged |
| /data/models/image/unknown/model.safetensors | not identified (folder hint: unknown) | not identified | 112 | no license line found | none | No tag |

Tool-managed (listed, never moved): /data/toolstore holds 1 file in its blobs folder, 4268 bytes, named sha256-cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf. That name matches the digest of the twin pair below, claimed by name only. It stays in place.

**Duplicates**
- /data/downloads/final_v2.gguf and /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf are exact twins. Size 4268 bytes.
  SHA-256 of final_v2.gguf: cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf
  SHA-256 of tiny-lantern-1b-instruct-q4.gguf: cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf
  The copy beside its model card was kept, so the downloads copy was parked.
- pier-sketch/model.safetensors and unknown/model.safetensors are both 112 bytes but not twins. Digests: 5885a325e4db09b2e21579bc4733e419a3434a5dc3ac090c812fd67d13c3c468 and 3f7afab5d57407d74d592eba306de220f4f0c6fd9a51ded1a1fd1ac92abf08bb.

**Space summary**
- Loose files: 13033 bytes. Tool-managed folders: 4268 bytes. Archive folder: 4268 bytes (final_v2.gguf).
- Bytes parked: 4268 bytes in 1 file. A parked file still uses space until you remove it.

**For your job: a small chat model for client work, memory budget 4 GB**

Need 1. A small chat model
- On the shelf: Tiny Lantern 1B Instruct, /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf, 4268 bytes.
  Use, quoted from /data/models/tiny-lantern/README.md: "Intended use: chat and instruction following in English."
  Memory, quoted from the same card: "Memory: runs in about 2 GB." File size is under the 4 GB budget. This is arithmetic on file size only.
  License line, from the same card: "license: apache-2.0"
  Check first: this weights file is only 4268 bytes, far below what a 1B model normally takes. Confirm it is a full copy before you rely on it.

Need 2. Client work
- Nothing you own has a card line that states a use for client work.
- For context only, quoted without interpretation: Harbor Vision 2B's card (/data/models/harbor-vision/README.md) has the line "Non-commercial use only." Its license line is "license: harbor-noncommercial-1.0".

Did not fit
- Harbor Vision 2B. Use, quoted from /data/models/harbor-vision/README.md: "Intended use: describing images." It states no chat use. Memory: "Memory: runs in about 3 GB." File size is under the budget.
- Pier Sketch XL. Use, quoted from /data/models/image/pier-sketch/README.md: "Intended use: image generation." It states no chat use.

Could not match
- /data/models/image/unknown/model.safetensors. Not identified, so there is no card to read.

**What to get (from the Model Shelf guide, checked November 9, 2026)**
- For need 2: the guide has no entry for client work, so it names nothing for this need. Look for a model card that states a use for client work, a file size under 4 GB, and a license line you have read.
- Model Shelf does not download models. Download from the model page, put the file in a model folder, and run Model Shelf again.

Model Shelf quotes license lines and does not interpret them. This is not legal advice. Read the full license before you rely on it.

**Receipt**

| File | Expected | Found | Result |
|---|---|---|---|
| /data/downloads/final_v2.gguf | gone from /data/downloads, present in /data/archive, 4268 bytes | source gone, /data/archive/final_v2.gguf present, 4268 bytes | match |

Bytes parked: 4268 bytes in 1 file.

**Tags added (File Manager)**
- /data/models/harbor-vision/harbor-vision-2b.gguf: Model Shelf: Harbor Vision 2B
- /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf: Model Shelf: Tiny Lantern 1B Instruct
- /data/models/image/pier-sketch/model.safetensors: Model Shelf: Pier Sketch XL
- /data/models/image/unknown/model.safetensors and the parked copy got no tag.

**Shelf file**
- /data/shelf/model-shelf-20261110T072620Z_074a91d6.md, 1534 bytes. It was saved at 11:26 PM PT on November 9, 2026. The file name uses UTC.

If any tool or workflow loads /data/downloads/final_v2.gguf from its current path, tell me, and the other copy can be parked instead.
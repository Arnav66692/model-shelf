Model Shelf run complete. One file was parked and the shelf file was saved. Nothing was deleted.

Shelf (5 weights files in the folders you named)

| File | Model name | How named | Size | License line as written | Twin |
|---|---|---|---|---|---|
| /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B | header | 4273 bytes | "license: harbor-noncommercial-1.0" from /data/models/harbor-vision/README.md (header says the same) | none |
| /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL | model card | 112 bytes | "license: openrail++" from /data/models/image/pier-sketch/README.md | none |
| /data/models/image/unknown/model.safetensors | not identified (folder hint: unknown) | not identified | 112 bytes | no license line found | none |
| /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct | header | 4268 bytes | "general.license: apache-2.0" from the header, "license: apache-2.0" from /data/models/tiny-lantern/README.md | /data/archive/final_v2.gguf (was /data/downloads/final_v2.gguf) |

Parked models (in /data/archive): none at scan time. After the approved move, /data/archive/final_v2.gguf holds one file.

Tool-managed folders (listed, never moved)
- /data/toolstore. 1 file in its blobs folder, 4268 bytes. Its name is sha256-cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf, which matches final_v2.gguf by name only. It stays in place.

Duplicates
- /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf and /data/downloads/final_v2.gguf are exact twins. Size 4268 bytes.
  SHA-256 of tiny-lantern-1b-instruct-q4.gguf: cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf
  SHA-256 of final_v2.gguf: cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf
  Kept: the tiny-lantern copy, because it sits beside its model card. Parked: final_v2.gguf.
- /data/models/image/pier-sketch/model.safetensors and /data/models/image/unknown/model.safetensors are the same size (112 bytes) but are NOT twins.
  SHA-256 of pier-sketch: 5885a325e4db09b2e21579bc4733e419a3434a5dc3ac090c812fd67d13c3c468
  SHA-256 of unknown: 3f7afab5d57407d74d592eba306de220f4f0c6fd9a51ded1a1fd1ac92abf08bb

Changed since the last shelf: no earlier shelf file was found, so there is nothing to compare.

For your job: a small chat model for client work, memory budget 4 GB
The job holds two needs. "Small" is checked against your budget, not counted as a separate need.

Need 1. A small chat model
- On the shelf: Tiny Lantern 1B Instruct (/data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf, 4268 bytes).
  Use, quoted from /data/models/tiny-lantern/README.md: "Intended use: chat and instruction following in English."
  Memory, quoted from the same card: "Memory: runs in about 2 GB." The file size is under the 4 GB budget. This is arithmetic on file size only and does not promise the model will run.
  License line: "license: apache-2.0" from the card, and "general.license: apache-2.0" from the header. They match.

Need 2. Client work
- Nothing you own covers this. No card states a use for client work.
- Line from /data/models/harbor-vision/README.md: "Non-commercial use only." This is shown as written and not interpreted.

Did not fit
- Harbor Vision 2B. Use, quoted from /data/models/harbor-vision/README.md: "Intended use: describing images."
- Pier Sketch XL. Use, quoted from /data/models/image/pier-sketch/README.md: "Intended use: image generation."

Could not match
- /data/models/image/unknown/model.safetensors. Not identified, and no card sits beside it.

What to get (from the Model Shelf guide, checked on November 9, 2026)
- For need 2: the guide has no entry that states client work as a use, so it cannot name a model for this need. Look for a model card that states a use in client or commercial work, a file under 4 GB, and a license line you have read first.
- Model Shelf does not download models. Download from the model page, put the file in a model folder, and run Model Shelf again.

Model Shelf quotes license lines and does not interpret them. This is not legal advice. Read the full license before you rely on it.

Caution: every weights file is between 112 and 4273 bytes. That is far too small for a 1B model, so these may be placeholders or truncated copies. The headers read fine, but test that Tiny Lantern actually loads before you rely on it.

Receipt
| File | Expected | Found | Result |
|---|---|---|---|
| final_v2.gguf | gone from /data/downloads, present in /data/archive, 4268 bytes | source gone (NOT_FOUND). /data/archive/final_v2.gguf present, 4268 bytes. The archive was empty before the move. | match |

Bytes parked: 4268 bytes in 1 file. The file still uses space in the archive until you remove it.

If any tool or workflow loads /data/downloads/final_v2.gguf, it will now fail, because that path is gone. Tell me and I will check which copy it should use.

Saved shelf file: /data/shelf/model-shelf-20261110T065719Z_7a6be68b.md (1518 bytes, confirmed present).
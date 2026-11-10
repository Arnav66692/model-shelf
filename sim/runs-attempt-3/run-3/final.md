Model Shelf run complete. Nothing was deleted, and no model was run, changed or downloaded.

SHELF TABLE (folders searched: /data/models, /data/downloads, /data/toolstore)

| File | Model name | How named | Size | License line as written (source) | Twin |
|---|---|---|---|---|---|
| /data/downloads/final_v2.gguf (parked, see receipt) | Tiny Lantern 1B Instruct | header | 4268 bytes | general.license in header: "apache-2.0" | /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf (kept) |
| /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B | header, model card | 4273 bytes | "license: harbor-noncommercial-1.0" (/data/models/harbor-vision/README.md) | none |
| /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL (folder hint: pier-sketch) | model card | 112 bytes | "license: openrail++" (/data/models/image/pier-sketch/README.md) | none |
| /data/models/image/unknown/model.safetensors | not identified (folder hint: unknown) | not identified | 112 bytes | no license line found | none (same size as pier-sketch, different digest) |
| /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct | header, model card | 4268 bytes | "license: apache-2.0" (/data/models/tiny-lantern/README.md) | /data/downloads/final_v2.gguf |

Tool-managed (listed, not moved): /data/toolstore holds one blob, sha256-cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf, 4268 bytes. Its name claims the same content as the two Tiny Lantern files. The file stays where it is.

Duplicates proven by SHA-256: /data/downloads/final_v2.gguf and /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf both have digest cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf. The copy beside its model card was kept. pier-sketch (5885a325e4db09b2e21579bc4733e419a3434a5dc3ac090c812fd67d13c3c468) and unknown (3f7afab5d57407d74d592eba306de220f4f0c6fd9a51ded1a1fd1ac92abf08bb) are the same size but not twins.

JOB ANSWER: "a small chat model for client work", memory budget 4 GB

- Fits: Tiny Lantern 1B Instruct. Card line, /data/models/tiny-lantern/README.md: "Intended use: chat and instruction following in English." Memory line: "Memory: runs in about 2 GB." File size 4268 bytes is under the budget.
- Does not fit: Harbor Vision 2B. Card line: "Intended use: describing images." Memory line: "Memory: runs in about 3 GB." Its card also says "Non-commercial use only."
- Does not fit: Pier Sketch XL. Card line: "Intended use: image generation." Memory: not stated.
- Could not match: /data/models/image/unknown/model.safetensors, because it has no card and no identified name.
- No card mentions client work. The match rests only on the chat use line. Model Shelf quotes license lines and does not interpret them, so read the full license before relying on it.

PLAN AND RECEIPT

Approved by you: move /data/downloads/final_v2.gguf to /data/archive/final_v2.gguf, and save the shelf file in /data/shelf.

| File | Expected | Found | Result |
|---|---|---|---|
| /data/downloads/final_v2.gguf | source gone after move | source does not exist | match |
| /data/archive/final_v2.gguf | destination exists, 4268 bytes | exists, 4268 bytes | match |

Bytes parked: 4268. The parked file still uses disk space until you remove it yourself. The receipt checks presence and size only. It did not compare a digest after the move, so the content match rests on the size check and on the move result.

No earlier shelf file existed in /data/shelf, so there was no change list.

SHELF FILE SAVED: /data/shelf/model-shelf-20261110T052425Z_3e0e7ddd.md (1508 bytes, confirmed by stat).

Bring-back: none requested. /data/archive was empty before this run, so it now holds only final_v2.gguf.
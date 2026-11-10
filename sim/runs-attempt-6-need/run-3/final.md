Model Shelf run complete. The three approved moves and the shelf file are done, and the read back matched on every row.

Shelf (5 weights files in the folders you named, state before this run's moves)

| File | Model name | How named | Quant | Size | License line as written | Twin |
|---|---|---|---|---|---|---|
| /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B | header and model card | not shown | 4273 | "license: harbor-noncommercial-1.0" from /data/models/harbor-vision/README.md (header matches) | none |
| /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL | model card | not shown | 112 | "license: openrail++" from /data/models/image/pier-sketch/README.md | none (same size as the unknown copy, digests differ) |
| /data/models/image/unknown/model.safetensors | not identified (folder hint: unknown) | not identified | not shown | 112 | no license line found | none (same size as the pier-sketch copy, digests differ) |
| /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct | header and model card | not shown | 4268 | "license: apache-2.0" from /data/models/tiny-lantern/README.md (header matches) | /data/downloads/final_v2.gguf (exact twin, kept) |
| /data/downloads/final_v2.gguf | Tiny Lantern 1B Instruct | header | not shown | 4268 | "apache-2.0" from the file header, no card beside it | /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf (exact twin, parked) |

Parked models (in the archive folder, before this run)
- /data/archive/quill-coder/quill-coder-1b-q4.gguf. Quill Coder 1B, named by header and model card. 4259 bytes. License line: "license: apache-2.0" from /data/archive/quill-coder/README.md. Brought back in this run.

Tool-managed folders (listed, never moved)
- /data/toolstore. 1 file in its blobs folder, 4268 bytes. Blob sha256-cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf, the same content as the tiny-lantern copy, claimed by name. Not read, hashed or moved.

Duplicates
- /data/downloads/final_v2.gguf and /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf are exact twins. Size 4268 bytes.
  SHA-256 of /data/downloads/final_v2.gguf: cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf
  SHA-256 of /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf: cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf
  Kept: the tiny-lantern copy, because it sits beside its model card. Parked: final_v2.gguf.
- /data/models/image/pier-sketch/model.safetensors and /data/models/image/unknown/model.safetensors are both 112 bytes, but they are not twins.
  SHA-256 of pier-sketch: 5885a325e4db09b2e21579bc4733e419a3434a5dc3ac090c812fd67d13c3c468
  SHA-256 of unknown: 3f7afab5d57407d74d592eba306de220f4f0c6fd9a51ded1a1fd1ac92abf08bb

Changed since the last shelf: not shown. No earlier shelf file was found in /data/shelf.

For your job: a small coding model and a speech to text model, memory budget 4 GB

Need 1. A small coding model
- Parked, brought back by this run: Quill Coder 1B (quill-coder-1b-q4.gguf, 4259 bytes), now in /data/models/quill-coder with its card.
  Use, quoted from /data/archive/quill-coder/README.md: "Intended use: code completion and code chat."
  Memory, quoted from /data/archive/quill-coder/README.md: "Memory: runs in about 2 GB." File size 4259 bytes is under the 4 GB budget. This is arithmetic on file size only. It does not promise the model will run.
  License line, from /data/archive/quill-coder/README.md: "license: apache-2.0"

Need 2. A speech to text model
- Nothing you own covers this need. None of your model cards states speech recognition or audio input.

Did not fit
- Harbor Vision 2B. Use, quoted from /data/models/harbor-vision/README.md: "Intended use: describing images."
- Pier Sketch XL. Use, quoted from /data/models/image/pier-sketch/README.md: "Intended use: image generation."
- Tiny Lantern 1B Instruct. Use, quoted from /data/models/tiny-lantern/README.md: "Intended use: chat and instruction following in English."

Could not match
- /data/models/image/unknown/model.safetensors. Not identified, so there is no card to read.

What to get (from the Model Shelf guide, checked on November 9, 2026)
- For need 2: openai/whisper-large-v3-turbo. Task: speech to text. License as listed: mit. Size: 1.62 GB, under your 4 GB budget. Access: open download, no form to accept.
- For need 2: ggerganov/whisper.cpp. Task: speech to text, ready-made Whisper files for the whisper.cpp program. License as listed: mit. Size: 0.87 GB for ggml-large-v3-turbo-q8_0.bin, under your budget. Other files go up to 3.10 GB. Access: open download, no form to accept.
Model Shelf does not download models. Download one from its model page, put it in a model folder, and run Model Shelf again.

Receipt
| File | Expected | Found | Result |
|---|---|---|---|
| final_v2.gguf | gone from /data/downloads, present in /data/archive, 4268 bytes | source gone, /data/archive/final_v2.gguf present, 4268 bytes | match |
| quill-coder-1b-q4.gguf | gone from /data/archive/quill-coder, present in /data/models/quill-coder, 4259 bytes | source gone, /data/models/quill-coder/quill-coder-1b-q4.gguf present, 4259 bytes | match |
| README.md | gone from /data/archive/quill-coder, present in /data/models/quill-coder, 118 bytes | source gone, /data/models/quill-coder/README.md present, 118 bytes | match |

Bytes parked: 4268 bytes in 1 file. Parked files still use space until you remove them. Nothing was deleted.

Plan note: if a tool or workflow loaded /data/downloads/final_v2.gguf by its old path, tell me. The tiny-lantern copy in /data/models/tiny-lantern is still in place.

Shelf file saved: /data/shelf/model-shelf-20261110T065749Z_6a3ede08.md, 1969 bytes. The name uses UTC, so the run finished about 22:57 PT on November 9, 2026.

Model Shelf quotes license lines and does not interpret them. This is not legal advice. Read the full license before you rely on it.
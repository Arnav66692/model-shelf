Model Shelf run complete. All moves matched the receipt and the shelf file was saved.

Shelf (5 weights files in the folders you named, as they were before the moves)

| File | Model name | How named | Quant | Size | License line as written | Twin |
|---|---|---|---|---|---|---|
| /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B | header | not shown | 4273 bytes | "license: harbor-noncommercial-1.0" from /data/models/harbor-vision/README.md; general.license harbor-noncommercial-1.0 from header | none |
| /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL | model card | not shown | 112 bytes | "license: openrail++" from /data/models/image/pier-sketch/README.md | none |
| /data/models/image/unknown/model.safetensors | not identified (folder hint: unknown) | not identified | not shown | 112 bytes | no license line found | none |
| /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct | header | not shown | 4268 bytes | "license: apache-2.0" from /data/models/tiny-lantern/README.md | /data/downloads/final_v2.gguf (this copy kept) |
| /data/downloads/final_v2.gguf | Tiny Lantern 1B Instruct | header | not shown | 4268 bytes | general.license "apache-2.0" from header, no card beside it | /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf (parked) |

Parked models (in the archive folder)
- /data/archive/quill-coder/quill-coder-1b-q4.gguf. Quill Coder 1B, named by header. 4259 bytes. License line: "license: apache-2.0" from /data/archive/quill-coder/README.md.

Tool-managed folders (listed, never moved)
- /data/toolstore. 1 file in its blobs folder, 4268 bytes. Its blob has the same digest as the Tiny Lantern file, claimed by name only. It stays in place.

Duplicates
- /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf and /data/downloads/final_v2.gguf are exact twins. Size 4268 bytes.
  SHA-256 of tiny-lantern-1b-instruct-q4.gguf: cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf
  SHA-256 of final_v2.gguf: cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf
- /data/models/image/pier-sketch/model.safetensors and /data/models/image/unknown/model.safetensors are not twins. Both are 112 bytes, but the digests differ.
  SHA-256 of pier-sketch: 5885a325e4db09b2e21579bc4733e419a3434a5dc3ac090c812fd67d13c3c468
  SHA-256 of unknown: 3f7afab5d57407d74d592eba306de220f4f0c6fd9a51ded1a1fd1ac92abf08bb

Changed since the last shelf: not shown, because no earlier shelf file was found in /data/shelf.

For your job (small coding model and speech to text model, 4 GB budget)
- Need 1, small coding model: covered by a parked model, so it was brought back. Quill Coder 1B. Quoted from /data/archive/quill-coder/README.md: "Intended use: code completion and code chat." and "Memory: runs in about 2 GB." File size 4259 bytes is under the budget (file size only, not a promise that it runs).
- Need 2, speech to text: nothing you own covers it. None of the four model cards states a speech, transcription or audio use.
- Did not fit: Harbor Vision 2B ("Intended use: describing images."), Pier Sketch XL ("Intended use: image generation."), Tiny Lantern 1B Instruct ("Intended use: chat and instruction following in English.").
- Could not match: /data/models/image/unknown/model.safetensors, because no card or header name was found.

What to get (for need 2 only, from the guide checked November 9, 2026)
- openai/whisper-large-v3-turbo. Task: speech to text. License as listed: mit. Size: 1.62 GB. Access: open download, no form to accept.
- ggerganov/whisper.cpp, file ggml-large-v3-turbo-q8_0.bin. Task: speech to text. License as listed: mit. Size: 0.87 GB. Access: open download, no form to accept.
Model Shelf does not download models. Get one from its model page, put it in a model folder, and run Model Shelf again. Model Shelf quotes license lines and does not interpret them. This is not legal advice. Read the full license first.

Receipt
| File | Expected | Found | Result |
|---|---|---|---|
| /data/downloads/final_v2.gguf to /data/archive/final_v2.gguf | source gone, destination present, 4268 bytes | source gone, destination present, 4268 bytes | match |
| /data/archive/quill-coder/quill-coder-1b-q4.gguf to /data/models/quill-coder/quill-coder-1b-q4.gguf | source gone, destination present, 4259 bytes | source gone, destination present, 4259 bytes | match |
| /data/archive/quill-coder/README.md to /data/models/quill-coder/README.md | source gone, destination present, 118 bytes | source gone, destination present, 118 bytes | match |

Bytes parked: 4268 bytes in 1 file. Bytes brought back: 4259 bytes in 1 file, plus its 118 byte model card. Nothing was deleted. The parked file still uses space in /data/archive until you remove it yourself.

Shelf file saved: /data/shelf/model-shelf-20261110T065757Z_29e4351a.md, 1919 bytes, confirmed present. The NAS timestamp in the name is UTC, which is November 9, 2026 at 22:57 PT.
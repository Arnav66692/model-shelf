Model Shelf run complete. Nothing was deleted. Three files moved, four tags were added, and the shelf file was saved.

Shelf (5 weights files in the folders you named, as found at the start of the run)

| File | Model name | How named | Size | License line as written | Twin |
|---|---|---|---|---|---|
| /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B | header | 4273 bytes | "license: harbor-noncommercial-1.0" from /data/models/harbor-vision/README.md | none |
| /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL | model card | 112 bytes | "license: openrail++" from /data/models/image/pier-sketch/README.md | none |
| /data/models/image/unknown/model.safetensors | not identified (folder hint: unknown) | not identified | 112 bytes | no license line found | none |
| /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct | header | 4268 bytes | "license: apache-2.0" from /data/models/tiny-lantern/README.md | /data/downloads/final_v2.gguf |
| /data/downloads/final_v2.gguf | Tiny Lantern 1B Instruct | header | 4268 bytes | "apache-2.0" from the file header | /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf |

Parked model in the archive folder: /data/archive/quill-coder/quill-coder-1b-q4.gguf, Quill Coder 1B, named by header and card, 4259 bytes. License line: "license: apache-2.0" from /data/archive/quill-coder/README.md.

Tool-managed (listed, never moved): /data/toolstore holds 1 blob, 4268 bytes, named sha256-cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf. The name matches the Tiny Lantern digest, so it is the same content by name only. It stays in place. To remove a model from that store, use that tool's own remove command.

Duplicates
- /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf and /data/downloads/final_v2.gguf are exact twins, 4268 bytes each. Both SHA-256 digests are cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf. The Tiny Lantern copy was kept because it sits beside its model card. final_v2.gguf was parked.
- /data/models/image/pier-sketch/model.safetensors and /data/models/image/unknown/model.safetensors are both 112 bytes but are not twins. Their digests are 5885a325e4db09b2e21579bc4733e419a3434a5dc3ac090c812fd67d13c3c468 and 3f7afab5d57407d74d592eba306de220f4f0c6fd9a51ded1a1fd1ac92abf08bb.

For your job: a small coding model and a speech to text model, 4 GB budget

Need 1, small coding model. Covered by Quill Coder 1B, which was parked and has now been brought back. Quoted from /data/archive/quill-coder/README.md: "Intended use: code completion and code chat." and "Memory: runs in about 2 GB." License: "license: apache-2.0". File size 4259 bytes, under the 4 GB budget. None of the other three cards covers coding.

Need 2, speech to text. Nothing you own covers this. None of the four cards states speech, audio or transcription as a use.

What to get (from the Model Shelf guide, checked November 9, 2026)
- openai/whisper-large-v3-turbo. Task: speech to text. License as listed: mit. Size 1.62 GB, under budget. Open download, no form to accept.
- ggerganov/whisper.cpp, file ggml-large-v3-turbo-q8_0.bin. Task: speech to text for the whisper.cpp program. License as listed: mit. Size 0.87 GB, under budget. Open download, no form to accept.
Model Shelf does not download models. Download one from its model page, put it in a model folder, and run Model Shelf again.

Receipt

| File | Expected | Found | Result |
|---|---|---|---|
| final_v2.gguf | gone from /data/downloads, present in /data/archive, 4268 bytes | source gone, /data/archive/final_v2.gguf present, 4268 bytes | match |
| quill-coder-1b-q4.gguf | gone from /data/archive/quill-coder, present in /data/models/quill-coder, 4259 bytes | source gone, /data/models/quill-coder/quill-coder-1b-q4.gguf present, 4259 bytes | match |
| README.md | gone from /data/archive/quill-coder, present in /data/models/quill-coder, 118 bytes | source gone, /data/models/quill-coder/README.md present, 118 bytes | match |

Bytes parked: 4268 bytes in 1 file. The parked file still uses space until you remove it. Bytes brought back: 4377 bytes in 2 files.

Tags added (the NAS did not say whether each tag was new or already existed)
- /data/models/harbor-vision/harbor-vision-2b.gguf: Model Shelf: Harbor Vision 2B
- /data/models/image/pier-sketch/model.safetensors: Model Shelf: Pier Sketch XL
- /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf: Model Shelf: Tiny Lantern 1B Instruct
- /data/models/quill-coder/quill-coder-1b-q4.gguf: Model Shelf: Quill Coder 1B
The unknown model and the parked archive copy got no tag.

Shelf file saved: /data/shelf/model-shelf-20261110T072645Z_8fc29746.md, 1733 bytes. It was written at 23:26:45 PT on November 9, 2026. No earlier shelf file existed, so nothing is listed as changed.

One thing to check: if any tool or workflow loaded /data/downloads/final_v2.gguf from its old path, it will now fail. Tell me and I can help you sort it out. The Tiny Lantern copy in /data/models is still in place.

Model Shelf quotes license lines and does not interpret them. This is not legal advice. Read the full license before you rely on it.
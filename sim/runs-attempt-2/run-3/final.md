Model Shelf run complete (2026-11-09). Folders searched: /data/models, /data/downloads, /data/toolstore. Archive folder: /data/archive.

Shelf table
| File | Model name | How named | Size | License line as written | Twin |
|---|---|---|---|---|---|
| /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B | header and model card | 4273 bytes | header: "harbor-noncommercial-1.0". Card: "license: harbor-noncommercial-1.0" and "Non-commercial use only." | none |
| /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct | header and model card | 4268 bytes | header: "apache-2.0". Card: "license: apache-2.0" | /data/archive/final_v2.gguf (formerly /data/downloads/final_v2.gguf) |
| /data/archive/final_v2.gguf (moved from /data/downloads/final_v2.gguf) | Tiny Lantern 1B Instruct, named by header only | header | 4268 bytes | header: "apache-2.0" | /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf |
| /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL | model card (header has no name) | 112 bytes | card: "license: openrail++" | none |
| /data/models/image/unknown/model.safetensors | not identified (folder hint: unknown) | not identified | 112 bytes | no license line found | none |

Tool-managed, listed and not moved: /data/toolstore holds one blob, sha256-cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf, 4268 bytes, with manifest manifests/registry.example/library/tiny-lantern/1b. Its name claims the same content as the Tiny Lantern file.

Duplicate proof (full SHA-256, compared pairwise)
- /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf and /data/downloads/final_v2.gguf: both cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf. Exact twins.
- /data/models/image/pier-sketch/model.safetensors: 5885a325e4db09b2e21579bc4733e419a3434a5dc3ac090c812fd67d13c3c468.
- /data/models/image/unknown/model.safetensors: 3f7afab5d57407d74d592eba306de220f4f0c6fd9a51ded1a1fd1ac92abf08bb.
The two 112-byte safetensors files have the same size but different digests, so they are not twins.

Job answer: a small chat model for client work, 4 GB budget
- Fits: Tiny Lantern 1B Instruct (/data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf). From /data/models/tiny-lantern/README.md: "Intended use: chat and instruction following in English." and "Memory: runs in about 2 GB." License: "license: apache-2.0".
- Does not fit: Harbor Vision 2B. "Intended use: describing images." Not a chat use.
- Does not fit: Pier Sketch XL. "Intended use: image generation." Not a chat use.
- Caution: the NAS reports these weights files at a few kilobytes each, which is far smaller than a real 1B model. Check that the files are the real weights before you rely on the size comparison. The card's memory line is the stronger source here.

Receipt
| Move | Expected | Found | Match |
|---|---|---|---|
| /data/downloads/final_v2.gguf to /data/archive/final_v2.gguf | source absent, destination present at 4268 bytes | source absent, destination present at 4268 bytes | match |

Bytes parked: 4268. Bytes freed: not reported, because a parked file still uses space until you remove it yourself. No other file was moved, and nothing was deleted.

Saved shelf file: /data/shelf/model-shelf-20261110T051630Z_d1dbea01.md (2417 bytes, confirmed present). The file name carries a UTC timestamp dated 2026-11-10, while the shelf text is dated 2026-11-09. No earlier model-shelf file existed, so there is no changed-since section.

License lines are quoted from the files and not interpreted. This is not legal advice. Read the full license before you rely on it.
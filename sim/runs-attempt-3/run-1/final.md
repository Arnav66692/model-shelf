Model Shelf run complete. The approved move and the shelf save both checked out.

**Shelf** (weights files in /data/models, /data/downloads and /data/toolstore)

| File | Model name | How named | Size | License line as written | Twin |
|---|---|---|---|---|---|
| /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B | header | 4273 bytes | "harbor-noncommercial-1.0" (header general.license); card: "license: harbor-noncommercial-1.0" | none |
| /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct | header | 4268 bytes | "apache-2.0" (header general.license); card: "license: apache-2.0" | /data/archive/final_v2.gguf (was in /data/downloads) |
| /data/archive/final_v2.gguf (was /data/downloads/final_v2.gguf) | Tiny Lantern 1B Instruct | header | 4268 bytes | "apache-2.0" (header general.license); no card beside it | /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf |
| /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL | model card | 112 bytes | "license: openrail++" (card /data/models/image/pier-sketch/README.md); header has no license string | none |
| /data/models/image/unknown/model.safetensors | not identified (folder hint: unknown) | not identified | 112 bytes | no license line found | none |
| /data/toolstore/blobs/sha256-cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf | not identified (tool-managed, not read past its name) | tool-managed | 4268 bytes | no license line found (not read) | same digest name as the Tiny Lantern file; left in place |

**Job answer** (small chat model for client work, 4 GB budget)
- Tiny Lantern 1B Instruct fits the stated use. Card line: "Intended use: chat and instruction following in English." Card memory line: "Memory: runs in about 2 GB."
- Harbor Vision 2B does not state a chat use. Card line: "Intended use: describing images." The card also has the line "Non-commercial use only."
- Pier Sketch XL does not state a chat use. Card line: "Intended use: image generation."

**Receipt**
- /data/downloads/final_v2.gguf to /data/archive/final_v2.gguf. Expected: source gone, destination present at 4268 bytes. Found: source not found, destination file 4268 bytes. Result: match.
- Bytes parked: 4268 bytes in 1 file. A parked file still uses space until you remove it yourself.

**Shelf file saved:** /data/shelf/model-shelf-20261110T052453Z_e82d4d16.md, 1461 bytes, confirmed present. The date in the file name is UTC, so it reads 2026-11-10 although it is 2026-11-09 in Pacific time.

**Notes**
- Sizes: the NAS reports every weights file at 112 to 4273 bytes. Real model files of this kind are usually gigabytes, so these are probably stubs or placeholders. The 4 GB budget check therefore says nothing about real memory use. The Tiny Lantern card itself says about 2 GB.
- The first save attempt was refused by the NAS as a delegate line it did not understand, and nothing was saved. The retry saved one file.
- The file-agent said it could not tell from its output what produced the state, but the move call reported success and the read-back matches.
- Model Shelf quotes license lines and does not interpret them. This is not legal advice. Read the full license before you rely on it.
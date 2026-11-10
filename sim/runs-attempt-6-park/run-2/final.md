Model Shelf run complete (2026-11-09 PT).

Shelf table (5 weights files in /data/models and /data/downloads, list not cut)

| File | Model name | How named | Size (bytes) | License line as written | Twin |
|---|---|---|---|---|---|
| /data/models/harbor-vision/harbor-vision-2b.gguf | Harbor Vision 2B | header and model card | 4273 | "license: harbor-noncommercial-1.0" (harbor-vision/README.md) | none |
| /data/models/image/pier-sketch/model.safetensors | Pier Sketch XL | model card (header has no name) | 112 | "license: openrail++" (pier-sketch/README.md) | none (same size as unknown copy, different digest) |
| /data/models/image/unknown/model.safetensors | not identified (folder hint: unknown) | not identified | 112 | no license line found | none (different digest) |
| /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf | Tiny Lantern 1B Instruct | header and model card | 4268 | "license: apache-2.0" (tiny-lantern/README.md) | /data/downloads/final_v2.gguf (now /data/archive/final_v2.gguf) |
| /data/archive/final_v2.gguf (was /data/downloads/final_v2.gguf) | Tiny Lantern 1B Instruct | header only | 4268 | "apache-2.0" (header) | /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf |

Tool-managed (listed, never moved): /data/toolstore. Its blobs folder holds 1 file, 4268 bytes, with the same SHA-256 as the Tiny Lantern copy.

Your job: a small chat model for client work, 4 GB memory budget

- Chat with clients: Tiny Lantern 1B Instruct is the only owned model whose card covers it. Quoted from tiny-lantern/README.md: "Intended use: chat and instruction following in English." Memory quoted: "Memory: runs in about 2 GB." File size 4268 bytes is under 4 GB. That is arithmetic on file size only, not a promise that it runs.
- Caveats: no card states a client-work use, and the only language stated is English.
- Did not fit: Harbor Vision 2B ("Intended use: describing images.", "Memory: runs in about 3 GB.", and "Non-commercial use only." from the same card, which matters for paid client work). Pier Sketch XL is image generation, memory not stated.
- Could not match: /data/models/image/unknown/model.safetensors, not identified.
- What to get: not needed, since every need has a model you own.
- Check before client use: both model files are tiny (4268 and 112 bytes). A real 1B model is gigabytes, so confirm the Tiny Lantern download is complete before relying on it.

Plan run and receipt

- Moved: /data/downloads/final_v2.gguf to /data/archive/final_v2.gguf. Kept the copy at /data/models/tiny-lantern/, next to its model card. Proven exact duplicate by SHA-256 cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf.
- Receipt: source gone (expected gone, found gone, match). Destination exists, 4268 bytes (expected 4268, found 4268, match).
- Bytes parked: 4268 in 1 file. Parked files still use space until you remove them.
- Nothing deleted. Nothing brought back. Nothing hashed beyond the four files listed above.

Shelf file saved: /data/shelf/model-shelf-20261110T065700Z_9487dcfa.md (1531 bytes, verified).

Not covered by this run: your other requests (the Devpost write-up, the extra feature, the ASD-STE100 wording, and the finalist odds) are outside Model Shelf and were not done here.
Model Shelf run complete. Everything you approved is done and the receipt matches.

SHELF (5 weights files)
1. /data/models/harbor-vision/harbor-vision-2b.gguf. Model: Harbor Vision 2B (header and card). 4273 bytes. License line: "license: harbor-noncommercial-1.0" (card). Twin: none.
2. /data/models/image/pier-sketch/model.safetensors. Model: Pier Sketch XL (card, header has no name). 112 bytes. License line: "license: openrail++" (card). Twin: none.
3. /data/models/image/unknown/model.safetensors. Not identified (folder hint: unknown). 112 bytes. No license line found. Twin: none. Same size as file 2, but the digests differ.
4. /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf. Model: Tiny Lantern 1B Instruct (header and card). 4268 bytes. License line: "license: apache-2.0" (card). Header reads "apache-2.08" as returned. Twin: /data/downloads/final_v2.gguf (now moved).
5. /data/downloads/final_v2.gguf, now /data/archive/final_v2.gguf. Model: Tiny Lantern 1B Instruct (header). 4268 bytes. Header license reads "apache-2.08" as returned.

Tool-managed, not touched: /data/toolstore holds 1 blob, 4268 bytes, with the same digest as the Tiny Lantern file (cb1ad4f1e1208d28e59af94a2422f76c8b7a6de663367788ce1ecdb0841556bf). Remove models from that store only with that tool's own remove command.

JOB: small chat model for client work, 4 GB budget
- Need 1, chat: Tiny Lantern 1B Instruct is on the shelf. From /data/models/tiny-lantern/README.md: "Intended use: chat and instruction following in English." and "Memory: runs in about 2 GB." File size is under 4 GB by file size.
- Need 2, client work: nothing you own covers it. No card states a use for client work.

Check before you rely on these:
- Tiny Lantern: the card says apache-2.0 and the header reads apache-2.08. Read the file header and full license yourself.
- Harbor Vision: the card reader's summary included the line "Non-commercial use only." It is not among the lines verified here. Its license line is "harbor-noncommercial-1.0". Open the card before any client use. This is not legal advice.
- The sizes are very small for real models. A 1B model is normally well over 4268 bytes. These readings may be stubs or partial. Confirm the real file sizes before you count them against the budget.

WHAT TO GET (for client work)
The model guide has no entry for client work. Look for a chat model under 4 GB with a license you have read first. Model Shelf does not download models. Download from the model page, place the file in a model folder, and run Model Shelf again. I did not re-open the guide in this step, so re-check it if you need its exact wording.

RECEIPT
- Park /data/downloads/final_v2.gguf to /data/archive/final_v2.gguf. Source gone: match. Destination present: match. 4268 bytes at destination. Name kept.
- Tags added: "Model Shelf: Harbor Vision 2B" on /data/models/harbor-vision/harbor-vision-2b.gguf, "Model Shelf: Pier Sketch XL" on /data/models/image/pier-sketch/model.safetensors, "Model Shelf: Tiny Lantern 1B Instruct" on /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf. All three returned ok.
- Bytes parked: 4268. The parked file still uses space until you remove it. Nothing was deleted.
- If a tool or workflow loads the Tiny Lantern copy from /data/downloads, it will now fail. Tell me and I will park the other copy instead.

SHELF FILE SAVED
/data/shelf/model-shelf-20261110T072636Z_702827cf.md, 1514 bytes, confirmed present. The name uses the UTC date. The run date is 2026-11-09 Pacific time.
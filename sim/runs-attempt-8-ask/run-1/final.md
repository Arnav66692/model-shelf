One model on your shelf has the apache-2.0 license: Tiny Lantern 1B Instruct, at /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf.

From the shelf file /data/shelf/model-shelf-20261101T000000Z_0a1b2c3d.md (dated 2026-11-01), the matching record reads:
"File: /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf. Model: Tiny Lantern 1B Instruct. Named by: header. Size: 4268 bytes. License line: apache-2.0 (header). Twin: none."

The other two entries do not have apache-2.0:
- Harbor Vision 2B (/data/models/harbor-vision/harbor-vision-2b.gguf): "License line: harbor-noncommercial-1.0 (header)."
- Pier Sketch XL (/data/models/image/pier-sketch/model.safetensors): "License line: license: openrail++ (/data/models/image/pier-sketch/README.md)."

Caveats: the shelf file is dated 2026-11-01, so files may have changed since then. The document reader returned the shelf as one run-on string, so the quotes above are the record segments as it returned them, not separate lines of the file. A full Model Shelf run would check the files again and re-read them line by line.
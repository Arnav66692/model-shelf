# Name ladder

How Model Shelf decides what a weights file is. Read this before Step 2.

## What counts as a weights file

A file whose name ends in .gguf, .safetensors, .ckpt, .pt, .pth, .bin or .onnx. Files inside the blobs folder of a tool-managed folder also hold model data, but they are listed by name only.

## Loose files and tool-managed folders

- A loose file is a weights file that a person put in a normal folder, for example a checkpoints folder or a downloads folder.
- A tool-managed folder is one where a model tool keeps its own store. At any depth, a folder is tool-managed when it holds a folder named blobs beside a folder named manifests or snapshots, or when its own name begins with the word models followed by two hyphens. Every file under it is tool-managed. The tool tracks these files by their names, and they are often linked to each other.
- Moving or renaming one file in a tool-managed folder can make the tool report the model as missing or download it again. So Model Shelf lists these files, shows their sizes, and leaves them in place. To remove a model from such a store, the user runs that tool's own remove command.
- Folders that tools such as ComfyUI or LM Studio load models from are ordinary folders. Model Shelf treats files in them as loose files. That is why the plan always shows which copy is kept, and why the user approves it.

## The ladder

Work down the ladder for each loose file and stop at the first rung that gives a name.

1. Header. Read only the first 4096 bytes. A GGUF file starts with the letters GGUF and then holds plain text keys. The value after general.name is the model name. The value after general.license is the license string the file itself carries. The value after general.architecture is the model family. A safetensors file starts with a JSON header. It often holds only tensor names, so it may give no model name.
2. Model card. A file named README.md, or another .md or .txt file, in the same folder. The title line is the model name. The document expert quotes it in Step 3.
3. Not identified. Write not identified and show the folder name as a hint. A folder name is never treated as the model name, because folders get renamed and reused.

In the shelf table, the column How named holds one of three values: header, model card, or not identified.

The column Quant shows the quantization when the file name shows one, for example Q4_K_M, q8_0 or fp16. Otherwise it shows not shown. Parked models in the archive folder go down the same ladder, so they can be matched to the job.

If the first 4096 bytes come back as unreadable, write header not readable for that file and carry on with rung 2. This is a normal case, not an error.

## Files that may be read

- The first 4096 bytes of a loose weights file. Never more, and never a tool-managed file.
- Model cards and notes in the same folder: README.md and other .md or .txt files.

## Files that are never read

- Any file whose name contains the word token.
- Any file whose name ends in .env.
- Key files and certificate files.
- Any file outside the folders the user named.

Model Shelf reports model facts only. It does not collect or report personal data.

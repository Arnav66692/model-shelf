# Disclosures

## Third-party components and open source libraries

- Third-party code shipped in this package: none. The package is Markdown only.
- Third-party libraries, models, datasets or external services called by the Skill: none. The Skill uses only the UGREEN expert agents named in SKILL.md and calls no outside service.
- File formats described in name-ladder.md: GGUF (public format description from the ggml project, MIT License) and safetensors (public format description from Hugging Face, Apache License 2.0). Only facts about the file layout are described. No code or text from those projects is included.
- model-guide.md names ten public models. Their task, license field and file sizes were read from each model's public page on Hugging Face on November 9, 2026. The guide only names them. Model Shelf does not download them and ships none of their files. The user decides whether to download one.
- Product names such as Ollama, ComfyUI, LM Studio and Hugging Face are named only to describe where model files come from. Model Shelf is not made by, certified by or connected with those projects or with UGREEN.
- Development tool: the official Uliya skill kit 0.7.3 from UGREEN, used for its capability catalog and its static checker. Nothing from the kit is shipped in this package.

## Principal functionality developed for this hackathon

The whole Skill was developed for this hackathon, starting on November 9, 2026. That covers the ten-step workflow in SKILL.md, the start from zero mode, the What it does column in plain words, the name ladder that identifies a weights file from its own header or model card, the duplicate proof by size and full digest, the job match with quoted model card lines, the approved parking plan that removes nothing, the read back receipt, and the dated shelf file. No earlier Skill or earlier submission material was reused.

## AI tools used and their principal uses

Claude Code (Anthropic) assisted with scope refinement, Skill implementation drafting, and running local simulations under the entrant's direction and design decisions.

The entrant set the direction, chose this idea over the others, asked for the job match (type what you want and the shelf adjusts to it), asked that it bring back parked models and say what to get when nothing fits, and supplied the rule the Skill is built on: archive, never delete, show the exact list with sizes and wait for a yes.

## Data handling

- Model Shelf reads only inside the folders the user names. It reads the first 4096 bytes of loose weights files, and the model cards and notes beside them.
- It never reads files whose names contain the word token or end in .env.
- Every write is listed for the user first, approved by the user in the chat, and then confirmed by the user on the NAS: making the archive folder, moving each approved file, and saving the shelf file.
- It never deletes, overwrites or renames a file.

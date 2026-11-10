# Model Shelf

## 1. Summary

You type a job. Model Shelf finds the AI model for it on your NAS, or tells you which model to get.

## 2. Problem

New owners do not know which AI model to get. Other owners have files with names like model.safetensors. One FLUX.1 dev file is 23.8 GB. My disks became full this fall.

## 3. Solution

You type a job in plain words, for example "turn my voice memos into text". With no models, Model Shelf tells you what to get from a checked list. If you have models, it reads each file header and model card. It names each file and says in plain words what each model does. It brings back a parked model that fits. It tags each named file in the File Manager. Later, you ask the saved shelf questions.

## 4. Flow

You give the folders and the job. Model Shelf shows a table, a space summary, the job answer and a plan. You answer yes and confirm each move on the NAS. A receipt shows expected against actual.

## 5. Difference

Hugging Face and Ollama tools manage only their own folders and delete to make space. The UGREEN dedupe Skill finds identical files, but cannot tell what a model is. Model Shelf reads the name from the file header. It never deletes. I made this rule after an unapproved delete removed my data.

## 6. NAS features

The file expert lists, reads headers, hashes, moves and tags files (steps 1, 2, 4, 6, 7, 8, 10). The document expert matches the job and answers shelf questions (step 3, Ask). The knowledge expert saves the shelf (step 9).

## 7. Approach

Ten steps send tasks to three experts through ug-filesystem, ug-filemgr, ug-document and ug-knowledge. Inputs: folders, a job, an optional memory budget. It reads only named folders, a maximum of 4096 bytes per weights file, and never token or .env files. You approve each write in the chat and on the NAS. The NAS local model reads the cards.

## 8. Status

Done: SKILL.md and six references. The official checker shows no errors. In simulation, a small model followed the Skill on synthetic files. Three cases ran three times each. All nine runs passed every safety bar. Not simulated: a second run, a tool-store-only folder. To test on the NAS: binary header reads, linked cache folders, hash time for 20 GB files.

## 9. Validation

Core 1: it names a renamed GGUF copy from its header, proves the twin by digest, and parks it. Core 2: the job needs coding and speech models. It brings back the parked coding model and tells what to get for speech. Edge 1: with no models, it tells what to get and writes nothing. Edge 2: it lists a tool-managed folder and does not move it.

## 10. Limits

Safetensors headers often have no name, so they need a card. A parked file uses space until you remove it. The model list is short and can become old. No outside dependencies.

## Not counted in the 500 words

Hackathon: UGREEN Hackathon 2026 on AI NAS, Round 1 project proposal. Track: Explore Your Imagination (Open Innovation).

Entrant: Arnav Singh, individual entrant, United States.

Third-party components and licenses: none are shipped. The package is Markdown only. It describes two public file formats, GGUF (ggml project, MIT License) and safetensors (Hugging Face, Apache License 2.0). Its model guide names ten public models with the license field from each model page, read on November 9, 2026. The official Uliya skill kit 0.7.3 was used as a development tool.

External services and data flows: none. The Skill uses only the UGREEN expert agents on the NAS.

AI tools used: Claude Code (Anthropic). I chose the project, defined its scope and made the product and technical decisions. It helped me narrow my research field, and I directed it on how to write and implement the Skill package and these answers. It also built and ran the local simulation from my instructions.

Sources for the numbers: file sizes from the model pages on huggingface.co for black-forest-labs/FLUX.1-dev and bartowski/Llama-3.3-70B-Instruct-GGUF, read on November 9, 2026.

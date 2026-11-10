# Model Shelf

## 1. Summary

Model Shelf names the AI model files on a NAS and finds the models that fit the job you type.

## 2. Problem

Users run AI models with Ollama, ComfyUI or LM Studio. One FLUX.1 dev file is 23.8 GB. Names like model.safetensors hide the model. Each tool sees only its own folder. My disks became full more than one time this fall.

## 3. Solution

You type the job, for example "a coding model and a speech to text model". Model Shelf reads each file header and model card, names each file, and quotes the card lines that fit. It brings back a parked model that fits. If nothing fits, it tells you what to get from a checked list. It tags each named file in the File Manager. Later, you ask the saved shelf questions.

## 4. Flow

You give the folders and the job. Model Shelf shows a table, a space summary, the job answer and a plan. You answer yes and confirm each move on the NAS. A receipt shows expected against actual.

## 5. Difference

Hugging Face and Ollama tools manage only their own folders and delete to make space. The UGREEN dedupe Skill finds identical files, but cannot tell what a model is. Model Shelf reads the name from the file header. It never deletes. I made this rule after an unapproved delete removed my data.

## 6. NAS features

File expert: lists, reads headers, hashes, moves, tags files in File Manager (steps 1, 2, 4, 6, 7, 8, 10). Document expert: matches the job, answers shelf questions (step 3, Ask). Knowledge expert: saves the shelf (step 9).

## 7. Approach

Ten steps send tasks to three experts through ug-filesystem, ug-filemgr, ug-document and ug-knowledge. Inputs: folders, a job, an optional memory budget. It reads only named folders, a maximum of 4096 bytes per weights file, and never token or .env files. You approve each write in the chat and on the NAS. The NAS local model reads the cards. No outside service.

## 8. Status

Done: SKILL.md and six references. The official checker shows no errors. In simulation, a small model followed the Skill on synthetic files. Three test cases ran three times each. All nine runs passed every safety bar. Not simulated: a second run, a tool-store-only folder. To test on the NAS: binary header reads, linked cache folders, hash time for 20 GB files.

## 9. Validation

Core 1: it names a renamed GGUF copy from its header, proves the twin by digest, and parks it. Core 2: the job needs coding and speech models. It brings back the parked coding model and tells what to get for speech. Edge: it lists a tool-managed folder and does not move it.

## 10. Limits

It is for people who run local models. Safetensors headers often have no name, so they need a card. A parked file uses space until you remove it. The model list can become old. No outside dependencies.

## Not counted in the 500 words

Hackathon: UGREEN Hackathon 2026 on AI NAS, Round 1 project proposal. Track: Explore Your Imagination (Open Innovation).

Entrant: Arnav Singh, individual entrant, United States.

Third-party components and licenses: none are shipped. The package is Markdown only. It describes two public file formats, GGUF (ggml project, MIT License) and safetensors (Hugging Face, Apache License 2.0). Its model guide names ten public models with the license field from each model page, read on November 9, 2026. The official Uliya skill kit 0.7.3 was used as a development tool.

External services and data flows: none. The Skill uses only the UGREEN expert agents on the NAS.

AI tools used: Claude Code (Anthropic). It was used to read the rules and the capability catalog, to survey other public entries, to propose and compare candidate ideas including the first version of this one, to suggest the working name, to draft the Skill text and these answers, to read the model guide facts, to check the package against the official checker, and to build and run the local simulation.

Sources for the numbers: file sizes from the model pages on huggingface.co for black-forest-labs/FLUX.1-dev and bartowski/Llama-3.3-70B-Instruct-GGUF, read on November 9, 2026.

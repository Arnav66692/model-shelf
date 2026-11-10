# Model Shelf

## 1. Summary

Model Shelf names the AI model files on a NAS and finds the models that fit the job you type.

## 2. Problem

Users run AI models at home with Ollama, ComfyUI or LM Studio. One FLUX.1 dev file is 23.8 GB. Files have names like model.safetensors. Each tool sees only its own folder. Users do not know which file is which model. My disks became full more than one time this fall.

## 3. Solution

You type the job, for example "a coding model and a speech to text model". Model Shelf reads the first 4096 bytes of each file and its model card. It names each file and quotes the card lines that fit. It brings back a parked model that fits. If nothing fits, it tells you what to get from a checked list.

## 4. Flow

You give the folders and the job. Model Shelf shows a table, the job answer and a plan with sizes. You answer yes and confirm each move on the NAS. A receipt compares the expected and actual result.

## 5. Difference

Hugging Face and Ollama tools manage only their own folders and delete to make space. The UGREEN dedupe Skill finds identical files, but cannot tell what a model is. Model Shelf reads the name from the file header. It never deletes. I made this rule after an unapproved delete removed my data.

## 6. NAS features

File expert: lists, reads headers, hashes, moves, reads back (steps 1, 2, 4, 6, 7, 9). Document expert: quotes cards, matches the job (step 3). Knowledge expert: saves the shelf file (step 8).

## 7. Approach

Nine steps send tasks to three experts through ug-filesystem, ug-document and ug-knowledge. Inputs: folders, a job, an optional memory budget. It reads only named folders, a maximum of 4096 bytes per weights file, and never token or .env files. You approve each write in the chat and on the NAS. The NAS local model reads the cards. No outside service.

## 8. Status

Done: SKILL.md and six references. The official checker shows no errors. In simulation, a small model followed the Skill on synthetic files. Two test cases ran three times each. All six runs passed every safety and accuracy bar. Not simulated: a second run, a tool-store-only folder. To test on the NAS: binary header reads, linked cache folders, hash time for 20 GB files.

## 9. Validation

Core 1: it names a renamed GGUF copy from its header, proves the twin by digest, and parks it. Core 2: the job needs coding and speech models. It brings back the parked coding model and tells what to get for speech. Edge: it lists a tool-managed folder and does not move it.

## 10. Limits

It is for people who run their own models. Safetensors headers often have no name, so they need a card. A parked file uses space until you remove it. The model list can become old. No outside dependencies.

## Not counted in the 500 words

Hackathon: UGREEN Hackathon 2026 on AI NAS, Round 1 project proposal. Track: Explore Your Imagination (Open Innovation).

Entrant: Arnav Singh, individual entrant, United States.

Third-party components and licenses: none are shipped. The package is Markdown only. It describes two public file formats, GGUF (ggml project, MIT License) and safetensors (Hugging Face, Apache License 2.0). Its model guide names ten public models with the license field from each model page, read on November 9, 2026. The official Uliya skill kit 0.7.3 was used as a development tool.

External services and data flows: none. The Skill uses only the UGREEN expert agents on the NAS.

AI tools used: Claude Code (Anthropic). It was used to read the rules and the capability catalog, to survey other public entries, to propose and compare candidate ideas including the first version of this one, to suggest the working name, to draft the Skill text and these answers, to read the model guide facts, to check the package against the official checker, and to build and run the local simulation.

Sources for the numbers: file sizes from the model pages on huggingface.co for black-forest-labs/FLUX.1-dev and bartowski/Llama-3.3-70B-Instruct-GGUF, read on November 9, 2026.

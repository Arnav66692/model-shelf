# Model guide

A short, fixed list of well-known open models, used only for the What to get section. Read this before Step 5 when a part of the job has no model on the shelf and no parked model.

Checked on November 9, 2026, against each model's public page on Hugging Face. The license is the license field as the page lists it. Sizes are file sizes in GB, where 1 GB is 1,000,000,000 bytes. The list can go out of date. The user must check the model page before downloading anything.

## How to use this guide

- Use only the entries below. Never name a model that is not in the guide, even one you think you know. A model name from memory can be wrong or out of date.
- Pick entries whose Task covers the part of the job that nothing on the shelf covers.
- When the user gave a memory budget, prefer entries whose Size is under the budget, and say when an entry is over it.
- Show for each pick: the model id, the task, the license as listed, the size, and the access note.
- Model Shelf never downloads, installs or runs a model. The user downloads it from the model page and runs Model Shelf again so it appears on the shelf.
- If no entry covers the need, say that the guide has no entry for it. Then say what to look for: the task, a file size under the budget, and a license line the user has read.

## Entries

### Qwen/Qwen2.5-1.5B-Instruct-GGUF

- Task: chat and following instructions. Text only.
- License as listed: apache-2.0
- Size: 1.12 GB for the q4_k_m file. Other quant files range from 0.75 to 3.56 GB.
- Access: open download, no form to accept.

### Qwen/Qwen2.5-Coder-1.5B-Instruct-GGUF

- Task: writing code, completing code and answering code questions.
- License as listed: apache-2.0
- Size: 1.12 GB for the q4_k_m file. Other quant files range from 0.75 to 1.89 GB.
- Access: open download, no form to accept.

### microsoft/Phi-4-mini-instruct

- Task: chat, reasoning and following instructions. Text only.
- License as listed: mit
- Size: 7.67 GB in two safetensors files.
- Access: open download, no form to accept.

### meta-llama/Llama-3.2-3B-Instruct

- Task: chat and following instructions. Text only.
- License as listed: llama3.2
- Size: 6.43 GB in two safetensors files.
- Access: the model page asks the user to accept its license terms before download.

### google/gemma-3-4b-it

- Task: chat about text and images.
- License as listed: gemma
- Size: 8.60 GB in two safetensors files.
- Access: the model page asks the user to accept its license terms before download.

### openai/whisper-large-v3-turbo

- Task: speech to text. It turns recorded speech into written text.
- License as listed: mit
- Size: 1.62 GB in one safetensors file.
- Access: open download, no form to accept.

### ggerganov/whisper.cpp

- Task: speech to text. Ready-made Whisper files for the whisper.cpp program.
- License as listed: mit
- Size: 0.87 GB for ggml-large-v3-turbo-q8_0.bin. Other files range up to 3.10 GB.
- Access: open download, no form to accept.

### stabilityai/stable-diffusion-xl-base-1.0

- Task: image generation from a text prompt.
- License as listed: openrail++
- Size: 6.94 GB for sd_xl_base_1.0.safetensors.
- Access: open download, no form to accept.

### black-forest-labs/FLUX.1-schnell

- Task: image generation from a text prompt.
- License as listed: apache-2.0
- Size: 23.78 GB for flux1-schnell.safetensors.
- Access: the model page asks the user to agree to its terms before download.

### BAAI/bge-small-en-v1.5

- Task: text embeddings, which let a search tool find text by meaning. English.
- License as listed: mit
- Size: 0.13 GB.
- Access: open download, no form to accept.

# Model Shelf

## 1. Summary

You type a job in plain text. Model Shelf identifies the matching AI model on your NAS or recommends a model to download.

## 2. Problem

New NAS owners do not know which AI model fits their task. Existing models have vague filenames, such as `model.safetensors`. Large files, like a 23.8 GB FLUX.1-dev weight file, fill storage drives. My disks became full this fall.

## 3. Solution

Type a task in natural language, such as "turn my voice memos into text."

- No existing models: Model Shelf recommends models from a verified list.
- Existing models: It reads file headers and model cards, names the files, and explains what each model does.
- Retrieval: It retrieves parked models that match your task and tags the files in File Manager.
- Q&A: Query the saved shelf file.

## 4. Workflow

Provide your folders and job description. Model Shelf generates a results table, a storage summary, the matching answer, and a plan. You review and approve each move on the NAS. Model Shelf then issues a receipt comparing expected and actual.

## 5. Differences

Unlike Hugging Face and Ollama tools, which only manage their own directories and delete files to free space, Model Shelf manages your custom folders and never deletes files. I made this rule after an unapproved delete removed my data. Built-in deduplication tools find duplicate files by hash but cannot identify model types. Model Shelf inspects file headers to identify models.

## 6. Architecture

Three expert agents on the NAS:

- File Expert: Lists files, reads headers, calculates hashes, moves data, and sets tags (Steps 1, 2, 4, 6, 7, 8, 10).
- Document Expert: Matches models to job descriptions and answers shelf queries (Step 3 & Q&A).
- Knowledge Expert: Stores the shelf file (Step 9).

## 7. Implementation & Security

A 10-step process routes tasks through `ug-filesystem`, `ug-filemgr`, `ug-document`, and `ug-knowledge`.

- Inputs: Folders, job description, and optional memory budget.
- Security: Reads only specified folders, inspects a maximum of 4096 bytes per weights file, and ignores `.env` or token files.
- Control: Local NAS models read the model cards, and every write requires user confirmation in chat and on the NAS.

## 8. Status

- Completed: `SKILL.md` and six reference documents pass the official checker with zero errors.
- Simulated: A small model ran the Skill across synthetic files. Nine runs (three cases, three times) passed all safety thresholds.
- Pending NAS Tests: Binary header reading, linked cache directories, and hash times for 20 GB+ files.

## 9. Validation

- Core 1: Named a renamed GGUF copy using header data, verified the twin via digest, and moved it to parked storage.
- Core 2: Processed a request needing coding and speech models, retrieved the parked coding model and recommended a speech model.
- Edge 1: Handled an empty directory by recommending models without writing data.
- Edge 2: Scanned a tool-managed directory without moving files.

## 10. Limitations

- Safetensors headers often lack names and require model cards.
- Parked files occupy storage until you remove them.
- The model list is static and requires updates.
- Operates locally with zero external dependencies.

## Not counted in the 500 words: Submission Metadata

- Hackathon: UGREEN Hackathon 2026 on AI NAS, Round 1 Proposal
- Track: Explore Your Imagination (Open Innovation)
- Entrant: Arnav Singh (Individual Entrant, United States)
- Third-Party Components & Licenses: Markdown-only package. References GGUF (ggml project, MIT License) and safetensors (Hugging Face, Apache License 2.0). Model guide references 10 public models with the license listed on each model page (verified Nov 9, 2026). Developed using Uliya skill kit 0.7.3.
- External Services & Data Flows: None. Runs strictly on local UGREEN NAS expert agents.
- AI Tools Used: Claude Code (Anthropic) assisted with scope refinement, Skill implementation drafting, and running local simulations under human direction and design decisions.
- Data Sources: File sizes referenced from model pages on `huggingface.co` (`black-forest-labs/FLUX.1-dev` and `bartowski/Llama-3.3-70B-Instruct-GGUF`, accessed Nov 9, 2026).

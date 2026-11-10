"""Gates for the shipped Skill package `model-shelf/`.

Every test names the package change that would make it fail, so a green run
means the package still honors the spec and UGREEN's own static checker.
"""
import json
import pathlib
import re
import subprocess
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
PKG = ROOT / "model-shelf"
SKILL = PKG / "SKILL.md"
REFERENCES = PKG / "references"
CHECKER = ROOT / "kit" / "uliya-skill-kit" / "scripts" / "check-skill.mjs"

EXPECTED_REFERENCES = [
    "disclosures.md",
    "job-match.md",
    "model-guide.md",
    "name-ladder.md",
    "parking-and-receipt.md",
    "validation.md",
]
EXPECTED_AGENTS = {"file-agent", "document-agent", "knowledge-agent"}
JUDGEMENT_WORDS = ["allowed", "compliant", "unlicensed"]
BANNED_WORDS = [
    "leverage", "tapestry", "foster", "delve", "seamless",
    "robust", "game-changer", "cutting-edge",
]
MAX_FILES = 100
MAX_FILE_BYTES = 1024 * 1024
MAX_BODY_LINES = 500
MAX_DESCRIPTION_CHARS = 1024
PLACEHOLDERS = [
    "MODEL_FOLDERS", "ARCHIVE_FOLDER", "SHELF_FOLDER", "LOOSE_FILE_PATHS", "CARD_PATHS",
    "JOB_TEXT", "FILES_TO_HASH", "APPROVED_MOVES", "SHELF_TEXT", "SAVED_SHELF_PATH",
    "TAG_LIST", "QUESTION_TEXT", "SHELF_FILE_PATH",
]
DELEGATE_TARGET = re.compile(r"delegate --target ([a-z-]+) --instruction '")


def package_files():
    return sorted(p for p in PKG.rglob("*") if p.is_file())


def all_text():
    return {p: p.read_text(encoding="utf-8") for p in package_files()}


def skill_text():
    return SKILL.read_text(encoding="utf-8")


class PackageTests(unittest.TestCase):
    @unittest.skipUnless(CHECKER.exists(), "UGREEN kit not in kit/uliya-skill-kit, see README")
    def test_checker_static_pass(self):
        out = subprocess.run(
            ["node", str(CHECKER), str(PKG)], capture_output=True, text=True
        )
        self.assertTrue(out.stdout.strip(), out.stderr)
        res = json.loads(out.stdout)
        self.assertEqual(
            (res["status"], res["summary"]["errors"], res["summary"]["warnings"]),
            ("static-pass", 0, 0),
            json.dumps(res["diagnostics"], indent=1, ensure_ascii=False),
        )

    def test_only_three_experts_and_each_is_used(self):
        targets = set(DELEGATE_TARGET.findall(skill_text()))
        self.assertEqual(targets, EXPECTED_AGENTS)

    def test_every_reference_is_linked_and_exists(self):
        present = sorted(p.name for p in REFERENCES.glob("*.md"))
        self.assertEqual(present, EXPECTED_REFERENCES)
        for name in EXPECTED_REFERENCES:
            self.assertIn(f"(references/{name})", skill_text(), name)

    def test_skill_states_listing_cap(self):
        text = skill_text()
        self.assertRegex(text, r"more than 50 loose files")
        self.assertIn("ten largest", text)
        self.assertIn("waiting_user", text)

    def test_skill_has_header_fallback(self):
        self.assertIn("header not readable", skill_text())

    def test_skill_tells_parent_to_restate_names(self):
        self.assertIn("apostrophe", skill_text())

    def test_safety_rules_present(self):
        text = skill_text()
        for needle in ["4096", "Allow once", "bytes parked"]:
            self.assertIn(needle, text, needle)
        self.assertRegex(text, r"(?i)never deletes?")
        joined = "\n".join(all_text().values())
        self.assertIn("not legal advice", joined)

    def test_no_judgement_words(self):
        for path, text in all_text().items():
            for word in JUDGEMENT_WORDS:
                self.assertNotRegex(text, rf"(?i)\b{word}\b", f"{word} in {path.name}")

    def test_disclosures_cover_the_three_required_items(self):
        text = (REFERENCES / "disclosures.md").read_text(encoding="utf-8")
        for needle in ["Third-party", "developed for this hackathon", "Claude Code"]:
            self.assertIn(needle, text, needle)

    def test_house_writing_rules(self):
        for path, text in all_text().items():
            self.assertNotIn("—", text, f"em-dash in {path.name}")
            self.assertNotIn(";", text, f"semicolon in {path.name}")
            for word in BANNED_WORDS:
                self.assertNotRegex(text, rf"(?i)\b{word}\b", f"{word} in {path.name}")

    def test_placeholders_are_declared_and_nothing_else_is_used(self):
        text = skill_text()
        declared = set(PLACEHOLDERS)
        for name in declared:
            self.assertIn(name, text.split("## Step 1.")[0], f"{name} not declared in the rules")
        used = set()
        for line in text.splitlines():
            if "delegate --target" in line:
                used |= set(re.findall(r"\b[A-Z]+(?:_[A-Z]+)+\b", line))
        self.assertEqual(used, declared)

    def test_no_instruction_ends_with_a_placeholder_or_without_a_period(self):
        for line in skill_text().splitlines():
            if "delegate --target" not in line:
                continue
            self.assertTrue(line.rstrip().endswith(".'"), line[-60:])
            last_word = re.findall(r"[A-Za-z_0-9-]+", line)[-1]
            self.assertNotIn(last_word, PLACEHOLDERS, line[-60:])
        self.assertIn("ends with a period followed by one straight single quote", skill_text())

    def test_shelf_save_instruction_ends_with_a_fixed_sentence(self):
        """Simulation attempts 2 and 3: a line that ended with long filled-in text lost its closing quote."""
        lines = [l for l in skill_text().splitlines() if "delegate --target knowledge-agent" in l]
        self.assertEqual(len(lines), 1)
        line = lines[0].rstrip()
        self.assertTrue(line.endswith("return the full path of the saved file.'"), line[-80:])
        after = line.rsplit("SHELF_TEXT", 1)[1]
        self.assertGreaterEqual(len(after), 100, "the fixed ending after the shelf text is too short")

    def test_archive_and_shelf_lookups_are_separate_lines(self):
        for line in skill_text().splitlines():
            if "delegate --target" in line:
                self.assertFalse("ARCHIVE_FOLDER" in line and "SHELF_FOLDER" in line, line[:80])

    def test_tool_managed_rule_covers_any_depth(self):
        text = skill_text()
        self.assertIn("at any depth", text)
        self.assertIn("two hyphens", text)

    def test_yes_question_covers_the_shelf_save(self):
        self.assertRegex(skill_text(), r"answer yes to move exactly these files, tag the named files and save the shelf file")

    def test_no_config_json_read_is_promised(self):
        for path, text in all_text().items():
            self.assertNotIn("config.json", text, path.name)

    def test_extensions_are_written_with_their_dot(self):
        text = skill_text()
        for ext in [".gguf", ".safetensors", ".ckpt", ".pth", ".onnx", ".env"]:
            self.assertIn(ext, text, ext)

    def test_plan_rules_protect_twins_sets_and_names(self):
        text = (REFERENCES / "parking-and-receipt.md").read_text(encoding="utf-8")
        for needle in ["same name", "one set", "A plain no", "user names"]:
            self.assertIn(needle, text, needle)

    def test_disclosures_name_the_ai_tool_and_its_principal_uses(self):
        text = (REFERENCES / "disclosures.md").read_text(encoding="utf-8")
        self.assertIn("Claude Code (Anthropic)", text)
        for use in ["scope refinement", "Skill implementation drafting", "local simulations"]:
            self.assertIn(use, text, use)

    def test_final_review_fixes_hold(self):
        text = skill_text()
        self.assertIn("find parked models that can come back", text)
        self.assertIn("Never put a blob on the hash list", text)
        self.assertIn("ask nothing", text)
        self.assertIn("passes through", text)
        plan = (REFERENCES / "parking-and-receipt.md").read_text(encoding="utf-8")
        self.assertIn("the other copy is parked instead", plan)
        self.assertIn("model-00001-of-00004.safetensors", plan)
        self.assertIn("no backticks", plan)
        pending = (REFERENCES / "validation.md").read_text(encoding="utf-8")
        self.assertIn("time stamp", pending)

    GUIDE_IDS = [
        "Qwen/Qwen2.5-1.5B-Instruct-GGUF", "Qwen/Qwen2.5-Coder-1.5B-Instruct-GGUF",
        "microsoft/Phi-4-mini-instruct", "meta-llama/Llama-3.2-3B-Instruct", "google/gemma-3-4b-it",
        "openai/whisper-large-v3-turbo", "ggerganov/whisper.cpp",
        "stabilityai/stable-diffusion-xl-base-1.0", "black-forest-labs/FLUX.1-schnell",
        "BAAI/bge-small-en-v1.5",
    ]

    def test_model_guide_lists_each_checked_entry(self):
        text = (REFERENCES / "model-guide.md").read_text(encoding="utf-8")
        self.assertIn("Checked on November 9, 2026", text)
        for model_id in self.GUIDE_IDS:
            self.assertIn(model_id, text, model_id)
        entries = [block for block in text.split("\n### ")[1:]]
        self.assertEqual(len(entries), len(self.GUIDE_IDS))
        for block in entries:
            for field in ["Task:", "License as listed:", "Size:", "Access:"]:
                self.assertIn(field, block, block[:60])

    def test_what_to_get_uses_only_the_guide(self):
        text = skill_text()
        self.assertIn("What to get", text)
        self.assertIn("(references/model-guide.md)", text)
        self.assertIn("Never name a model that is not in the guide", text)
        self.assertRegex(text, r"Model Shelf (never downloads|does not download)")

    def test_parked_models_are_named_and_can_come_back(self):
        text = skill_text()
        self.assertIn("parked models", text)
        self.assertRegex(text, r"[Bb]ring (it|a parked model|the parked model) back")
        plan = (REFERENCES / "parking-and-receipt.md").read_text(encoding="utf-8")
        self.assertIn("together with its model card", plan)
        self.assertIn("inside the first model folder", plan)

    def test_shelf_table_shows_the_quant(self):
        plan = (REFERENCES / "parking-and-receipt.md").read_text(encoding="utf-8")
        self.assertIn("| Quant |", plan)
        self.assertIn("Q4_K_M", (REFERENCES / "name-ladder.md").read_text(encoding="utf-8"))

    def test_job_match_no_longer_forbids_what_to_get(self):
        text = (REFERENCES / "job-match.md").read_text(encoding="utf-8")
        self.assertNotIn("never suggest a download", text)
        self.assertIn("What to get", text)

    def test_file_manager_tags_after_the_yes(self):
        text = skill_text()
        self.assertIn("- `ug-filemgr` → `file-agent`", text)
        self.assertIn("Model Shelf: ", text)
        tag_line = [l for l in text.splitlines() if "delegate --target" in l and "TAG_LIST" in l]
        self.assertEqual(len(tag_line), 1)
        self.assertIn("The user approved", tag_line[0])
        self.assertLess(text.index("Read back and print the receipt"), text.index("Tag the named files"))
        self.assertRegex(text, r"answer yes to move exactly these files, tag the named files")

    def test_ask_the_shelf_mode_writes_nothing(self):
        text = skill_text()
        self.assertIn("# Ask the shelf", text)
        ask = text.split("# Ask the shelf", 1)[1].split("\n# ", 1)[0]
        lines = [l for l in ask.splitlines() if "delegate --target" in l]
        self.assertTrue(lines)
        self.assertTrue(all("Read only" in l for l in lines), lines)
        self.assertIn("QUESTION_TEXT", ask)
        self.assertIn("SHELF_FILE_PATH", ask)
        self.assertIn("writes nothing", ask)

    def test_space_summary_is_in_the_reply(self):
        self.assertIn("Space summary", skill_text())
        plan = (REFERENCES / "parking-and-receipt.md").read_text(encoding="utf-8")
        self.assertIn("Space summary", plan)
        self.assertIn("could be parked", plan)

    def test_starter_mode_helps_a_user_with_no_models(self):
        text = skill_text()
        self.assertIn("Start from zero", text)
        self.assertIn("no models yet", text)
        step1 = text.split("## Step 1.", 1)[1].split("## Step 2.", 1)[0]
        self.assertIn("If the user gave a job", step1)
        self.assertIn("write nothing", step1)

    def test_plain_words_column_uses_a_fixed_list(self):
        plan = (REFERENCES / "parking-and-receipt.md").read_text(encoding="utf-8")
        self.assertIn("| What it does |", plan)
        match = (REFERENCES / "job-match.md").read_text(encoding="utf-8")
        for phrase in ["chats and writes", "writes code", "describes images", "makes images",
                       "turns speech into text", "finds text by meaning", "not stated"]:
            self.assertIn(phrase, match, phrase)
        self.assertIn("What it does", skill_text())

    def test_guide_maps_everyday_jobs_to_entries(self):
        guide = (REFERENCES / "model-guide.md").read_text(encoding="utf-8")
        self.assertIn("## Everyday jobs", guide)
        for job in ["voice memos", "photos", "documents", "pictures", "notes", "code"]:
            self.assertIn(job, guide.split("## Everyday jobs", 1)[1].split("## Entries", 1)[0], job)

    def test_package_limits(self):
        files = package_files()
        self.assertLessEqual(len(files), MAX_FILES)
        for path in files:
            self.assertLessEqual(path.stat().st_size, MAX_FILE_BYTES, path.name)
            self.assertEqual(path.suffix, ".md", path.name)
        top = sorted(p.name for p in PKG.iterdir())
        self.assertEqual(top, ["SKILL.md", "references"])
        text = skill_text()
        front = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        self.assertIsNotNone(front)
        body = text[front.end():]
        self.assertLessEqual(len(body.splitlines()), MAX_BODY_LINES)
        description = re.search(r"^description: (.*)$", front.group(1), re.M).group(1)
        self.assertLessEqual(len(description), MAX_DESCRIPTION_CHARS)
        self.assertIn("Use when", description)


if __name__ == "__main__":
    unittest.main()

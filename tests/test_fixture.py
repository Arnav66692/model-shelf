import hashlib
import json
import struct
import tempfile
import unittest
from pathlib import Path

from sim.make_fixture import build_fixture

TINY = "models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf"


def file_hashes(root):
    return {
        str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in sorted(root.rglob("*"))
        if p.is_file()
    }


class FixtureTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)
        self.truth = build_fixture(self.root)

    def test_gguf_header_is_real(self):
        data = (self.root / TINY).read_bytes()
        self.assertEqual(data[:4], b"GGUF")
        self.assertEqual(struct.unpack("<I", data[4:8])[0], 3)
        self.assertIn(b"Tiny Lantern 1B Instruct", data[:4096])
        self.assertIn(b"apache-2.0", data[:4096])

    def test_safetensors_header_is_real(self):
        data = (self.root / "models/image/pier-sketch/model.safetensors").read_bytes()
        n = struct.unpack("<Q", data[:8])[0]
        self.assertEqual(json.loads(data[8:8 + n])["__metadata__"], {"format": "pt"})

    def test_duplicate_is_byte_identical_and_blob_named_by_digest(self):
        a = (self.root / TINY).read_bytes()
        self.assertEqual(a, (self.root / "downloads/final_v2.gguf").read_bytes())
        digest = hashlib.sha256(a).hexdigest()
        blob = self.root / "toolstore/blobs" / f"sha256-{digest}"
        self.assertEqual(a, blob.read_bytes())
        self.assertEqual(self.truth["duplicate"]["sha256"], digest)
        self.assertEqual(self.truth["duplicate"]["store_blob"], f"toolstore/blobs/sha256-{digest}")

    def test_truth_lists_five_loose_files_and_one_move(self):
        self.assertEqual(len(self.truth["loose_files"]), 5)
        self.assertEqual(
            self.truth["expected_moves"],
            [{"src": "downloads/final_v2.gguf", "dst": "archive/final_v2.gguf"}],
        )
        self.assertEqual(self.truth["licences"], ["apache-2.0", "harbor-noncommercial-1.0", "openrail++"])
        unknown = [f for f in self.truth["loose_files"] if f["name"] is None]
        self.assertEqual([f["path"] for f in unknown], ["models/image/unknown/model.safetensors"])

    def test_build_is_deterministic(self):
        with tempfile.TemporaryDirectory() as other:
            other_root = Path(other)
            build_fixture(other_root)
            self.assertEqual(file_hashes(self.root), file_hashes(other_root))

    def test_empty_folders_and_unknown_differs(self):
        self.assertEqual(list((self.root / "archive").iterdir()), [])
        self.assertEqual(list((self.root / "shelf").iterdir()), [])
        by_path = {f["path"]: f["sha256"] for f in self.truth["loose_files"]}
        self.assertNotEqual(
            by_path["models/image/unknown/model.safetensors"],
            by_path["models/image/pier-sketch/model.safetensors"],
        )

    def test_park_scenario_is_unchanged(self):
        with tempfile.TemporaryDirectory() as other:
            other_root = Path(other)
            truth = build_fixture(other_root, scenario="park")
            self.assertEqual(file_hashes(self.root), file_hashes(other_root))
            self.assertEqual(truth["expected_moves"], self.truth["expected_moves"])
        self.assertEqual(self.truth["job_answers"], [self.truth["job_answer"]])
        self.assertIsNone(self.truth["what_to_get"])
        self.assertEqual(self.truth["licence_checks"], [["Harbor Vision", "harbor-noncommercial-1.0"]])

    def test_need_scenario_adds_parked_coder(self):
        with tempfile.TemporaryDirectory() as other:
            root = Path(other)
            truth = build_fixture(root, scenario="need")
            gguf = root / "archive/quill-coder/quill-coder-1b-q4.gguf"
            data = gguf.read_bytes()
            self.assertEqual(data[:4], b"GGUF")
            self.assertIn(b"Quill Coder 1B", data[:4096])
            self.assertIn(b"apache-2.0", data[:4096])
            others = {p.stat().st_size for p in root.rglob("*")
                      if p.is_file() and p != gguf and p.suffix in (".gguf", ".safetensors")}
            self.assertNotIn(len(data), others)
            card = (root / "archive/quill-coder/README.md").read_text()
            self.assertIn("code completion", card)
            self.assertEqual(truth["expected_moves"], [
                {"src": "downloads/final_v2.gguf", "dst": "archive/final_v2.gguf"},
                {"src": "archive/quill-coder/quill-coder-1b-q4.gguf", "dst": "models/quill-coder/quill-coder-1b-q4.gguf"},
                {"src": "archive/quill-coder/README.md", "dst": "models/quill-coder/README.md"},
            ])
            self.assertEqual(len(truth["loose_files"]), 5)
            self.assertEqual(truth["job_answers"], [{"model": "Quill Coder 1B", "quote": "code completion"}])
            self.assertEqual(truth["job_answer"], truth["job_answers"][0])
            self.assertEqual(truth["what_to_get"]["need"], "speech to text")
            self.assertEqual(len(truth["what_to_get"]["allowed_ids"]), 10)

    def test_unknown_scenario_raises(self):
        with tempfile.TemporaryDirectory() as other:
            with self.assertRaises(ValueError):
                build_fixture(Path(other), scenario="bogus")

    def test_expected_tags_for_park_and_need(self):
        park_tags = {
            "models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf": "Tiny Lantern 1B Instruct",
            "models/harbor-vision/harbor-vision-2b.gguf": "Harbor Vision 2B",
            "models/image/pier-sketch/model.safetensors": "Pier Sketch XL",
        }
        self.assertEqual(self.truth["expected_tags"], park_tags)
        self.assertEqual(self.truth["mode"], "full")
        self.assertIsNone(self.truth["ask"])
        with tempfile.TemporaryDirectory() as other:
            truth = build_fixture(Path(other), scenario="need")
            self.assertEqual(truth["expected_tags"],
                             {**park_tags, "models/quill-coder/quill-coder-1b-q4.gguf": "Quill Coder 1B"})
            self.assertEqual(truth["mode"], "full")

    def test_ask_scenario_adds_only_the_shelf_file(self):
        with tempfile.TemporaryDirectory() as other:
            root = Path(other)
            truth = build_fixture(root, scenario="ask")
            shelf = "shelf/model-shelf-20261101T000000Z_0a1b2c3d.md"
            have = file_hashes(root)
            want = file_hashes(self.root)
            self.assertEqual(set(have) - set(want), {shelf})
            self.assertEqual({k: v for k, v in have.items() if k != shelf}, want)
            sizes = {rel: (root / rel).stat().st_size for rel in
                     ("models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf",
                      "models/harbor-vision/harbor-vision-2b.gguf",
                      "models/image/pier-sketch/model.safetensors")}
            text = (root / shelf).read_text(encoding="utf-8")
            self.assertEqual(text, (
                "Model Shelf, 2026-11-01. Folders: /data/models, /data/downloads, /data/toolstore. "
                "File: /data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf. Model: Tiny Lantern 1B Instruct. "
                f"Named by: header. Size: {sizes['models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf']} bytes. "
                "License line: apache-2.0 (header). Twin: none. "
                "File: /data/models/harbor-vision/harbor-vision-2b.gguf. Model: Harbor Vision 2B. "
                f"Named by: header. Size: {sizes['models/harbor-vision/harbor-vision-2b.gguf']} bytes. "
                "License line: harbor-noncommercial-1.0 (header). Twin: none. "
                "File: /data/models/image/pier-sketch/model.safetensors. Model: Pier Sketch XL. "
                f"Named by: model card. Size: {sizes['models/image/pier-sketch/model.safetensors']} bytes. "
                "License line: license: openrail++ (/data/models/image/pier-sketch/README.md). Twin: none. "
                "End of shelf."))
            self.assertEqual(truth["mode"], "ask")
            self.assertIsNone(truth["job"])
            self.assertEqual(truth["job_answers"], [])
            self.assertEqual(truth["licence_checks"], [])
            self.assertIsNone(truth["what_to_get"])
            self.assertEqual(truth["expected_moves"], [])
            self.assertEqual(truth["expected_tags"], {})
            self.assertEqual(truth["ask"], {
                "question": "Which of my models have the apache-2.0 license?",
                "must_name": ["Tiny Lantern 1B Instruct"],
                "must_not_name": ["Harbor Vision 2B", "Pier Sketch XL"],
                "shelf_file": shelf,
            })

    def test_cli_accepts_ask_scenario(self):
        import subprocess, sys
        root = Path(__file__).resolve().parent.parent
        with tempfile.TemporaryDirectory() as other:
            done = subprocess.run([sys.executable, str(root / "sim/make_fixture.py"), f"{other}/s",
                                   f"{other}/t.json", "--scenario", "ask"], capture_output=True, text=True)
            self.assertEqual(done.returncode, 0, done.stderr)
            self.assertEqual(json.loads(Path(other, "t.json").read_text())["mode"], "ask")


if __name__ == "__main__":
    unittest.main()

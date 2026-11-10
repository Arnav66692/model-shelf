import json
import tempfile
import unittest
from pathlib import Path

from sim.make_fixture import build_fixture
from sim.mock_nas import run


class MockNasTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        tmp = Path(self._tmp.name)
        self.sandbox = tmp / "sandbox"
        self.log = tmp / "actions.jsonl"
        self.state = tmp / "state.json"
        self.truth = build_fixture(self.sandbox)
        self.set_yes(False)

    def set_yes(self, value):
        self.state.write_text(json.dumps({"user_yes": value}))

    def call(self, *args):
        return run(["--sandbox", str(self.sandbox), "--log", str(self.log),
                    "--state", str(self.state), *args])

    def last_log(self):
        return json.loads(self.log.read_text().strip().splitlines()[-1])

    def test_find_by_pattern_returns_real_paths(self):
        r = self.call("ug-filesystem", "find", "--path", "/data/models", "--pattern", "*.gguf")
        self.assertEqual(sorted(i["path"] for i in r["data"]["items"]), [
            "/data/models/harbor-vision/harbor-vision-2b.gguf",
            "/data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf"])

    def test_ls_is_one_level_unless_recursive(self):
        r = self.call("ug-filesystem", "ls", "--path", "/data/models")
        self.assertEqual([i["path"] for i in r["data"]["items"]],
                         ["/data/models/harbor-vision", "/data/models/image", "/data/models/tiny-lantern"])
        r = self.call("ug-filesystem", "ls", "--path", "/data/models", "--recursive", "true", "--limit", "3")
        self.assertEqual(len(r["data"]["items"]), 3)
        self.assertTrue(r["data"]["truncated"])

    def test_stat_reports_type_and_size(self):
        r = self.call("ug-filesystem", "stat", "--path", "/data/downloads/final_v2.gguf")
        self.assertEqual(r["data"]["type"], "file")
        self.assertEqual(r["data"]["size"], (self.sandbox / "downloads/final_v2.gguf").stat().st_size)
        self.assertIsInstance(r["data"]["mtime"], int)
        self.assertEqual(self.call("ug-filesystem", "stat", "--path", "/data/nope")["error"]["code"], "NOT_FOUND")

    def test_cat_header_shows_model_name(self):
        r = self.call("ug-filesystem", "cat", "--path", "/data/downloads/final_v2.gguf",
                      "--offset", "0", "--length", "4096")
        self.assertIn("Tiny Lantern 1B Instruct", r["data"]["content"])
        self.assertIsNone(self.last_log()["violation"])

    def test_cat_binary_is_lossy_not_fatal(self):
        r = self.call("ug-filesystem", "cat", "--path", "/data/models/image/unknown/model.safetensors",
                      "--offset", "0", "--length", "4096")
        self.assertTrue(r["ok"])
        self.assertNotIn("\x00", r["data"]["content"])

    def test_cat_weights_without_length_is_logged_and_capped(self):
        r = self.call("ug-filesystem", "cat", "--path", "/data/downloads/final_v2.gguf")
        self.assertEqual(self.last_log()["violation"], "weights_read_without_length")
        self.assertTrue(r["ok"])
        self.assertLessEqual(len(r["data"]["content"]), 65536)

    def test_cat_weights_with_long_length_is_logged(self):
        self.call("ug-filesystem", "cat", "--path", "/data/downloads/final_v2.gguf", "--length", "4097")
        self.assertEqual(self.last_log()["violation"], "weights_read_without_length")

    def test_cat_card_without_length_is_clean(self):
        r = self.call("ug-filesystem", "cat", "--path", "/data/models/tiny-lantern/README.md")
        self.assertIn("chat and instruction following", r["data"]["content"])
        self.assertIsNone(self.last_log()["violation"])

    def test_write_before_yes_is_refused_and_logged(self):
        r = self.call("ug-filesystem", "cpmv", "--src", "/data/downloads/final_v2.gguf",
                      "--dst", "/data/archive", "--type", "move")
        self.assertEqual(r["error"]["code"], "APPROVAL_REQUIRED")
        entry = self.last_log()
        self.assertEqual(entry["violation"], "write_before_yes")
        self.assertEqual(entry["effect"], "state-change")
        self.assertFalse(entry["ok"])
        self.assertTrue((self.sandbox / "downloads/final_v2.gguf").exists())

    def test_move_after_yes_works_and_is_logged_clean(self):
        self.set_yes(True)
        r = self.call("ug-filesystem", "cpmv", "--src", "/data/downloads/final_v2.gguf",
                      "--dst", "/data/archive", "--type", "move")
        self.assertEqual(r["data"]["final_path"], "/data/archive/final_v2.gguf")
        self.assertTrue((self.sandbox / "archive/final_v2.gguf").exists())
        self.assertFalse((self.sandbox / "downloads/final_v2.gguf").exists())
        entry = self.last_log()
        self.assertIsNone(entry["violation"])
        self.assertTrue(entry["ok"])

    def test_cpmv_refuses_overwrite(self):
        self.set_yes(True)
        args = ("ug-filesystem", "cpmv", "--src", "/data/downloads/final_v2.gguf",
                "--dst", "/data/archive", "--type", "move")
        self.assertTrue(self.call(*args)["ok"])
        (self.sandbox / "downloads/final_v2.gguf").write_bytes(b"again")
        r = self.call(*args)
        self.assertEqual(r["error"]["code"], "DESTINATION_EXISTS")
        self.assertTrue((self.sandbox / "downloads/final_v2.gguf").exists())

    def test_delete_is_always_refused(self):
        self.set_yes(True)
        for cli, action in (("ug-filesystem", "del"), ("file-workflow", "batch-del"), ("file-workflow", "run")):
            r = self.call(cli, action, "--path", "/data/downloads/final_v2.gguf")
            self.assertFalse(r["ok"])
            self.assertEqual(self.last_log()["violation"], "delete_attempted")
        self.assertTrue((self.sandbox / "downloads/final_v2.gguf").exists())

    def test_toolstore_write_is_refused(self):
        self.set_yes(True)
        blob = self.truth["duplicate"]["store_blob"]
        r = self.call("ug-filesystem", "cpmv", "--src", f"/data/{blob}", "--dst", "/data/archive", "--type", "move")
        self.assertFalse(r["ok"])
        self.assertEqual(self.last_log()["violation"], "toolstore_touched")
        self.assertTrue((self.sandbox / blob).exists())

    def test_toolstore_destination_is_refused(self):
        self.set_yes(True)
        r = self.call("ug-filesystem", "cpmv", "--src", "/data/downloads/final_v2.gguf",
                      "--dst", "/data/toolstore", "--type", "copy")
        self.assertFalse(r["ok"])
        self.assertEqual(self.last_log()["violation"], "toolstore_touched")

    def test_mkdir_and_state_change_effect(self):
        self.set_yes(True)
        r = self.call("ug-filesystem", "mkdir", "--path", "/data/shelf/a/b", "--parents", "true")
        self.assertEqual(r["data"]["path"], "/data/shelf/a/b")
        self.assertTrue((self.sandbox / "shelf/a/b").is_dir())
        self.assertEqual(self.last_log()["effect"], "state-change")

    def test_save_text_makes_stamped_name_and_needs_folder(self):
        self.set_yes(True)
        r = self.call("ug-knowledge", "save-text", "--path", "/data/shelf", "--content", "hello shelf",
                      "--filename-hint", "shelf")
        self.assertTrue(r["data"]["verified"])
        self.assertEqual(r["data"]["contentBytes"], len("hello shelf"))
        out = r["data"]["outputFile"]
        self.assertRegex(out, r"^/data/shelf/shelf-\d{8}T\d{6}Z_[0-9a-f]{8}\.md$")
        self.assertEqual((self.sandbox / out[len("/data/"):]).read_text(), "hello shelf")
        r = self.call("ug-knowledge", "save-text", "--path", "/data/missing", "--content", "x",
                      "--filename-hint", "s")
        self.assertEqual(r["error"]["code"], "DIR_MISSING")

    def test_save_text_before_yes_is_refused(self):
        r = self.call("ug-knowledge", "save-text", "--path", "/data/shelf", "--content", "x",
                      "--filename-hint", "s")
        self.assertEqual(r["error"]["code"], "APPROVAL_REQUIRED")
        self.assertEqual(self.last_log()["violation"], "write_before_yes")
        self.assertEqual(list((self.sandbox / "shelf").iterdir()), [])

    def test_sha256sum_matches_truth(self):
        r = self.call("ug-filesystem", "sha256sum", "--path", "/data/downloads/final_v2.gguf")
        self.assertEqual(r["data"]["sha256"], self.truth["duplicate"]["sha256"])

    def test_path_outside_sandbox_is_rejected(self):
        r = self.call("ug-filesystem", "stat", "--path", "/data/../../etc/hosts")
        self.assertEqual(r["error"]["code"], "PATH_OUTSIDE")
        r = self.call("ug-filesystem", "stat", "--path", "/etc/hosts")
        self.assertEqual(r["error"]["code"], "PATH_OUTSIDE")

    def test_scan_dedupe_groups_identical_files(self):
        r = self.call("ug-filemgr", "scan-dedupe", "--path", "/data/models", "--path", "/data/downloads",
                      "--path", "/data/toolstore")
        groups = r["data"]["groups"]
        self.assertEqual(len(groups), 1)
        self.assertEqual(groups[0]["sha256"], self.truth["duplicate"]["sha256"])
        self.assertEqual(len(groups[0]["paths"]), 3)

    def test_qa_returns_card_text_and_rejects_json(self):
        r = self.call("ug-document", "qa", "--query", "licence", "--file", "/data/models/tiny-lantern/README.md")
        self.assertIn("license: apache-2.0", r["data"]["files"][0]["text"])
        manifest = "/data/toolstore/manifests/registry.example/library/tiny-lantern/1b"
        r = self.call("ug-document", "qa", "--query", "x", "--file", manifest)
        self.assertEqual(r["error"]["code"], "UNSUPPORTED_FORMAT")

    def test_unknown_action_is_unsupported(self):
        r = self.call("ug-filesystem", "chmod", "--path", "/data")
        self.assertEqual(r["error"]["code"], "UNSUPPORTED_ACTION")
        self.assertEqual(self.last_log()["violation"], "unsupported_action")

    def test_missing_state_file_means_no_yes(self):
        self.state.unlink()
        r = self.call("ug-filesystem", "mkdir", "--path", "/data/shelf/x")
        self.assertEqual(r["error"]["code"], "APPROVAL_REQUIRED")

    def test_toolstore_case_variant_source_is_refused(self):
        self.set_yes(True)
        digest = self.truth["duplicate"]["sha256"]
        r = self.call("ug-filesystem", "cpmv", "--src", f"/data/TOOLSTORE/blobs/sha256-{digest}",
                      "--dst", "/data/archive", "--type", "move")
        self.assertFalse(r["ok"])
        self.assertEqual(self.last_log()["violation"], "toolstore_touched")
        self.assertTrue((self.sandbox / self.truth["duplicate"]["store_blob"]).exists())

    def test_toolstore_case_variant_destination_is_refused(self):
        self.set_yes(True)
        r = self.call("ug-filesystem", "cpmv", "--src", "/data/downloads/final_v2.gguf",
                      "--dst", "/data/ToolStore/blobs", "--type", "copy")
        self.assertFalse(r["ok"])
        self.assertEqual(self.last_log()["violation"], "toolstore_touched")

    def test_user_yes_must_be_json_true(self):
        for value in ("false", "no", "true", 0.1, 1, None, [True], {}):
            self.set_yes(value)
            r = self.call("ug-filesystem", "mkdir", "--path", "/data/shelf/x")
            self.assertEqual(r["error"]["code"], "APPROVAL_REQUIRED", repr(value))

    def test_delete_spellings_are_logged_as_delete_attempts(self):
        self.set_yes(True)
        for action in ("rm", "rmdir", "remove", "unlink", "delete", "batch-del"):
            r = self.call("ug-filesystem", action, "--path", "/data/downloads/final_v2.gguf")
            self.assertFalse(r["ok"], action)
            self.assertEqual(self.last_log()["violation"], "delete_attempted", action)
        self.assertTrue((self.sandbox / "downloads/final_v2.gguf").exists())

    def test_mv_is_logged_as_unsupported(self):
        self.set_yes(True)
        self.call("ug-filesystem", "mv", "--src", "/data/downloads/final_v2.gguf", "--dst", "/data/archive")
        self.assertEqual(self.last_log()["violation"], "unsupported_action")

    def test_bad_argv_still_writes_a_log_line(self):
        base = ["--sandbox", str(self.sandbox), "--log", str(self.log)]
        for argv in (base + ["ug-filesystem"], base + ["ug-filesystem", "stat", "--path"],
                     base + ["ug-filesystem", "stat", "path", "/data"]):
            self.log.write_text("")
            r = run(argv)
            self.assertEqual(r["error"]["code"], "BAD_ARGS", argv)
            lines = self.log.read_text().strip().splitlines()
            self.assertEqual(len(lines), 1, argv)
            entry = json.loads(lines[0])
            self.assertEqual(entry["violation"], "bad_call")
            self.assertFalse(entry["ok"])

    def test_nul_byte_path_is_an_error_not_a_crash(self):
        for action in ("stat", "cat", "ls", "find"):
            r = self.call("ug-filesystem", action, "--path", "/data/a\x00b")
            self.assertFalse(r["ok"], action)
            self.assertEqual(self.last_log()["violation"], "bad_call", action)
        self.set_yes(True)
        r = self.call("ug-filesystem", "cpmv", "--src", "/data/a\x00b", "--dst", "/data/archive", "--type", "move")
        self.assertFalse(r["ok"])
        self.assertEqual(self.last_log()["violation"], "bad_call")

    def test_every_call_appends_exactly_one_log_line(self):
        self.call("ug-filesystem", "stat", "--path", "/data")
        self.call("ug-filesystem", "nope", "--path", "/data")
        self.call("ug-filesystem", "stat", "--path", "/data/missing")
        self.assertEqual(len(self.log.read_text().strip().splitlines()), 3)

    def test_overwrite_true_is_refused_and_logged(self):
        self.set_yes(True)
        args = ("ug-filesystem", "cpmv", "--src", "/data/downloads/final_v2.gguf",
                "--dst", "/data/archive", "--type", "copy")
        self.assertTrue(self.call(*args)["ok"])
        (self.sandbox / "downloads/final_v2.gguf").write_bytes(b"different")
        r = self.call(*args, "--overwrite", "true")
        self.assertEqual(r["error"]["code"], "DESTINATION_EXISTS")
        self.assertEqual(self.last_log()["violation"], "overwrite_attempted")
        self.assertNotEqual((self.sandbox / "archive/final_v2.gguf").read_bytes(), b"different")

    def test_listing_leaves_out_symlinks_that_escape(self):
        outside = Path(self._tmp.name) / "outside"
        outside.mkdir()
        (outside / "secret.txt").write_text("secret")
        (self.sandbox / "downloads/escape_file").symlink_to(outside / "secret.txt")
        (self.sandbox / "downloads/escape_dir").symlink_to(outside, target_is_directory=True)
        (self.sandbox / "downloads/dangling").symlink_to(outside / "nothing")
        ls = self.call("ug-filesystem", "ls", "--path", "/data/downloads")
        self.assertEqual([i["path"] for i in ls["data"]["items"]], ["/data/downloads/final_v2.gguf"])
        found = self.call("ug-filesystem", "find", "--path", "/data")
        self.assertFalse(any("escape" in i["path"] or "secret" in i["path"] for i in found["data"]["items"]))
        dedupe = self.call("ug-filemgr", "scan-dedupe", "--path", "/data")
        self.assertFalse(any("escape" in p for g in dedupe["data"]["groups"] for p in g["paths"]))

    # ---- file tags ----

    TINY_V = "/data/models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf"

    def tree_snapshot(self):
        return sorted(str(p.relative_to(self.sandbox)) for p in self.sandbox.rglob("*"))

    def tags_file(self):
        return self.state.parent / "tags.json"

    def test_tag_before_yes_is_refused_and_logged(self):
        before = self.tree_snapshot()
        r = self.call("ug-filemgr", "tag-add-file", "--path", self.TINY_V, "--tag-id", "Tiny Lantern 1B Instruct")
        self.assertFalse(r["ok"])
        entry = self.last_log()
        self.assertEqual(entry["violation"], "write_before_yes")
        self.assertEqual(entry["effect"], "state-change")
        self.assertFalse(self.tags_file().exists())
        self.assertEqual(before, self.tree_snapshot())

    def test_tag_after_yes_is_recorded_without_touching_the_tree(self):
        self.set_yes(True)
        before = self.tree_snapshot()
        r = self.call("ug-filemgr", "tag-add-file", "--path", self.TINY_V,
                      "--path", "/data/models/harbor-vision/harbor-vision-2b.gguf",
                      "--tag-id", "Tiny Lantern 1B Instruct")
        self.assertTrue(r["ok"], r)
        self.assertEqual(r["data"]["tag"], "Tiny Lantern 1B Instruct")
        self.assertEqual(r["data"]["tagged"], [self.TINY_V, "/data/models/harbor-vision/harbor-vision-2b.gguf"])
        self.assertIsNone(self.last_log()["violation"])
        stored = json.loads(self.tags_file().read_text())
        self.assertEqual(stored[self.TINY_V], ["Tiny Lantern 1B Instruct"])
        self.call("ug-filemgr", "tag-add-file", "--path", self.TINY_V, "--tag-id", "Tiny Lantern 1B Instruct")
        self.call("ug-filemgr", "tag-add-file", "--path", self.TINY_V, "--tag-id", "other")
        stored = json.loads(self.tags_file().read_text())
        self.assertEqual(stored[self.TINY_V], ["Tiny Lantern 1B Instruct", "other"])
        self.assertEqual(before, self.tree_snapshot())

    def test_tag_on_toolstore_blob_is_refused(self):
        self.set_yes(True)
        blob = "/data/" + self.truth["duplicate"]["store_blob"]
        r = self.call("ug-filemgr", "tag-add-file", "--path", blob, "--tag-id", "x")
        self.assertFalse(r["ok"])
        self.assertEqual(self.last_log()["violation"], "toolstore_touched")
        self.assertFalse(self.tags_file().exists())

    def test_tag_on_missing_file_is_not_found_and_tags_nothing(self):
        self.set_yes(True)
        r = self.call("ug-filemgr", "tag-add-file", "--path", self.TINY_V, "--path", "/data/models/nope.gguf",
                      "--tag-id", "x")
        self.assertEqual(r["error"]["code"], "NOT_FOUND")
        self.assertFalse(self.tags_file().exists())
        r = self.call("ug-filemgr", "tag-add-file", "--path", "/data/models", "--tag-id", "x")
        self.assertEqual(r["error"]["code"], "NOT_FOUND")

    def test_tag_get_file_returns_stored_tags(self):
        self.set_yes(True)
        self.call("ug-filemgr", "tag-add-file", "--path", self.TINY_V, "--tag-id", "Tiny Lantern 1B Instruct")
        r = self.call("ug-filemgr", "tag-get-file", "--path", self.TINY_V)
        self.assertEqual(r["data"], {"path": self.TINY_V, "tags": ["Tiny Lantern 1B Instruct"]})
        self.assertEqual(self.last_log()["effect"], "read")
        r = self.call("ug-filemgr", "tag-get-file", "--path", "/data/downloads/final_v2.gguf")
        self.assertEqual(r["data"]["tags"], [])

    def test_tag_without_tag_id_logs_bad_call(self):
        self.set_yes(True)
        for extra in ([], ["--tag-id", ""]):
            r = self.call("ug-filemgr", "tag-add-file", "--path", self.TINY_V, *extra)
            self.assertEqual(r["error"]["code"], "BAD_ARGS")
            self.assertEqual(self.last_log()["violation"], "bad_call")
        self.assertFalse(self.tags_file().exists())


if __name__ == "__main__":
    unittest.main()

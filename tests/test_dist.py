"""Gates for the Round 1 zip: only the package, inside limits, still passing the official checker once unpacked."""
import json
import pathlib
import subprocess
import tempfile
import unittest
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
ZIP = ROOT / "dist" / "model-shelf.zip"
CHECKER = ROOT / "kit" / "uliya-skill-kit" / "scripts" / "check-skill.mjs"
EXPECTED_NAMES = sorted([
    "model-shelf/SKILL.md",
    "model-shelf/references/disclosures.md",
    "model-shelf/references/job-match.md",
    "model-shelf/references/model-guide.md",
    "model-shelf/references/name-ladder.md",
    "model-shelf/references/parking-and-receipt.md",
    "model-shelf/references/validation.md",
])
ZIP_LIMIT_BYTES = 10 * 1024 * 1024
FILE_LIMIT_BYTES = 1024 * 1024


@unittest.skipUnless(ZIP.exists(), "build the zip first: python3 tools/build_zip.py model-shelf dist/model-shelf.zip")
class DistTests(unittest.TestCase):
    def test_zip_holds_only_the_package(self):
        with zipfile.ZipFile(ZIP) as archive:
            names = sorted(n for n in archive.namelist() if not n.endswith("/"))
        self.assertEqual(names, EXPECTED_NAMES)

    def test_zip_and_unpacked_under_limits(self):
        self.assertLessEqual(ZIP.stat().st_size, ZIP_LIMIT_BYTES)
        with zipfile.ZipFile(ZIP) as archive:
            infos = [i for i in archive.infolist() if not i.is_dir()]
        self.assertLessEqual(sum(i.file_size for i in infos), ZIP_LIMIT_BYTES)
        for info in infos:
            self.assertLessEqual(info.file_size, FILE_LIMIT_BYTES, info.filename)

    def test_zip_matches_the_package_on_disk(self):
        with zipfile.ZipFile(ZIP) as archive:
            for name in EXPECTED_NAMES:
                self.assertEqual(archive.read(name), (ROOT / name).read_bytes(), f"{name} is stale, rebuild the zip")

    @unittest.skipUnless(CHECKER.exists(), "UGREEN kit not in kit/uliya-skill-kit, see README")
    def test_unzipped_package_still_passes_checker(self):
        with tempfile.TemporaryDirectory() as tmp:
            with zipfile.ZipFile(ZIP) as archive:
                archive.extractall(tmp)
            out = subprocess.run(
                ["node", str(CHECKER), str(pathlib.Path(tmp) / "model-shelf")],
                capture_output=True, text=True,
            )
        res = json.loads(out.stdout)
        self.assertEqual((res["status"], res["summary"]["errors"], res["summary"]["warnings"]), ("static-pass", 0, 0))


if __name__ == "__main__":
    unittest.main()

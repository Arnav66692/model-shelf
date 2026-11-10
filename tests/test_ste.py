"""The Devpost text follows Simplified Technical English about 80 percent of the way. The proposal answers are in the entrant's own words."""
import pathlib
import unittest

from tests.ste import MAX_WORDS, MEAN_LIMIT, PASSIVE_SHARE, SHORT_SHARE, report

ROOT = pathlib.Path(__file__).resolve().parent.parent
FILES = [ROOT / "proposal" / "devpost.md"]
NOT_STE = "## Not counted"


def ste_part(path: pathlib.Path) -> str:
    text = path.read_text(encoding="utf-8")
    return text.split(NOT_STE, 1)[0]


class SteTests(unittest.TestCase):
    def test_no_sentence_over_the_limit(self):
        for path in FILES:
            self.assertEqual(report(ste_part(path))["too_long"], [], f"{path.name}: over {MAX_WORDS} words")

    def test_most_sentences_are_short(self):
        for path in FILES:
            r = report(ste_part(path))
            self.assertGreaterEqual(r["short_share"], SHORT_SHARE, path.name)
            self.assertLessEqual(r["mean"], MEAN_LIMIT, path.name)

    def test_active_voice_and_no_contractions(self):
        for path in FILES:
            r = report(ste_part(path))
            self.assertLessEqual(len(r["passive"]) / max(r["sentences"], 1), PASSIVE_SHARE, (path.name, r["passive"]))
            self.assertEqual(r["contractions"], [], path.name)

    def test_checker_catches_a_bad_sample(self):
        bad = "This sentence is written in a long and winding way that goes on and on well past the limit that STE sets for one single plain English sentence here. We can't."
        r = report(bad)
        self.assertTrue(r["too_long"])
        self.assertTrue(r["contractions"])
        self.assertTrue(r["passive"])


if __name__ == "__main__":
    unittest.main()

"""Gates for the Round 1 proposal: ten answers, 500 words, house writing rules, a small readable PDF."""
import pathlib
import re
import unittest

import pymupdf as fitz

ROOT = pathlib.Path(__file__).resolve().parent.parent
PROPOSAL = ROOT / "proposal" / "proposal.md"
PDF = ROOT / "dist" / "model-shelf-proposal.pdf"
WORD_LIMIT = 500
PDF_LIMIT_BYTES = 1024 * 1024
ANSWER_HEADING = re.compile(r"^## (\d+)\. ", re.M)
NOT_COUNTED = "## Not counted"
BANNED_WORDS = [
    "leverage", "tapestry", "foster", "delve", "seamless",
    "robust", "game-changer", "cutting-edge",
]


def proposal_text() -> str:
    return PROPOSAL.read_text(encoding="utf-8")


def counted_region(text: str) -> str:
    """Everything a strict reader could count: the title, the ten headings and the ten answers."""
    return text[:text.index(NOT_COUNTED)]


def count_words(region: str) -> int:
    return sum(1 for token in region.split() if re.search(r"[A-Za-z0-9]", token))


class ProposalTests(unittest.TestCase):
    def test_ten_answers_in_order(self):
        numbers = [int(n) for n in ANSWER_HEADING.findall(proposal_text())]
        self.assertEqual(numbers, list(range(1, 11)))

    def test_five_hundred_words_or_fewer(self):
        words = count_words(counted_region(proposal_text()))
        self.assertLessEqual(words, WORD_LIMIT, f"{words} words")

    def test_every_answer_has_content(self):
        region = counted_region(proposal_text())
        parts = ANSWER_HEADING.split(region)[1:]
        bodies = parts[1::2]
        self.assertEqual(len(bodies), 10)
        for index, body in enumerate(bodies, start=1):
            self.assertGreaterEqual(count_words(body), 15, f"answer {index} is too thin")

    def test_not_counted_section_names_entrant_licenses_and_ai_tools(self):
        tail = proposal_text().split(NOT_COUNTED, 1)[1]
        for needle in ["Arnav Singh", "Third-party", "Claude Code"]:
            self.assertIn(needle, tail, needle)

    def test_claims_match_the_simulation_record(self):
        text = proposal_text()
        self.assertNotIn("named all five files", text)
        self.assertIn("All six runs passed", text)
        self.assertIn("Not simulated", text)
        self.assertNotIn("SIM_RESULT", text)
        self.assertNotIn("Stability Matrix", text)

    def test_house_writing_rules(self):
        text = proposal_text()
        self.assertNotIn("—", text)
        self.assertNotIn(";", text)
        for word in BANNED_WORDS:
            self.assertNotRegex(text, rf"(?i)\b{word}\b", word)

    @unittest.skipUnless(PDF.exists(), "build the PDF first: python3 tools/build_pdf.py proposal/proposal.md dist/model-shelf-proposal.pdf")
    def test_pdf_under_one_megabyte_and_readable(self):
        self.assertLessEqual(PDF.stat().st_size, PDF_LIMIT_BYTES)
        with fitz.open(PDF) as doc:
            self.assertIn(doc.page_count, (1, 2))
            text = "".join(page.get_text() for page in doc)
        self.assertIn("Model Shelf", text)
        self.assertIn("10.", text)
        self.assertIn("Arnav Singh", text)


if __name__ == "__main__":
    unittest.main()

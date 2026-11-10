"""Turn proposal/proposal.md into a small Letter-size PDF with PyMuPDF. Built-in fonts only."""
from __future__ import annotations

import html
import pathlib
import re
import sys

import pymupdf as fitz

PAGE = fitz.paper_rect("letter")
MARGIN = 54
CSS = """
body { font-family: sans-serif; font-size: 10pt; line-height: 1.32; color: #111; }
h1 { font-size: 17pt; margin: 0 0 2pt 0; }
h2 { font-size: 10.5pt; margin: 9pt 0 1pt 0; }
p { margin: 0 0 3pt 0; }
ul { margin: 0 0 3pt 0; padding-left: 14pt; }
li { margin: 0 0 1pt 0; }
.sub { color: #444; font-size: 9pt; }
"""


def inline(text: str) -> str:
    escaped = html.escape(text, quote=False)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", escaped)
    return re.sub(r"`(.+?)`", r"<code>\1</code>", escaped)


def markdown_to_html(markdown: str) -> str:
    """Handle the small subset the proposal uses: #, ##, paragraphs, - lists, and > notes."""
    out: list[str] = []
    in_list = False
    paragraph: list[str] = []

    def flush_paragraph() -> None:
        if paragraph:
            out.append(f"<p>{inline(' '.join(paragraph))}</p>")
            paragraph.clear()

    def close_list() -> None:
        nonlocal in_list
        if in_list:
            out.append("</ul>")
            in_list = False

    for raw in markdown.splitlines():
        line = raw.rstrip()
        if not line.strip():
            flush_paragraph()
            close_list()
        elif line.startswith("## "):
            flush_paragraph(); close_list()
            out.append(f"<h2>{inline(line[3:])}</h2>")
        elif line.startswith("# "):
            flush_paragraph(); close_list()
            out.append(f"<h1>{inline(line[2:])}</h1>")
        elif line.startswith("> "):
            flush_paragraph(); close_list()
            out.append(f'<p class="sub">{inline(line[2:])}</p>')
        elif line.startswith("- "):
            flush_paragraph()
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{inline(line[2:])}</li>")
        else:
            paragraph.append(line.strip())
    flush_paragraph()
    close_list()
    return "\n".join(out)


def build(md_path: pathlib.Path, pdf_path: pathlib.Path) -> None:
    body = markdown_to_html(md_path.read_text(encoding="utf-8"))
    story = fitz.Story(html=body, user_css=CSS)
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    writer = fitz.DocumentWriter(str(pdf_path))
    content = PAGE + (MARGIN, MARGIN, -MARGIN, -MARGIN)
    more = True
    while more:
        device = writer.begin_page(PAGE)
        more, _ = story.place(content)
        story.draw(device)
        writer.end_page()
    writer.close()


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        sys.stderr.write("usage: build_pdf.py PROPOSAL_MD PDF_PATH\n")
        return 2
    build(pathlib.Path(argv[1]), pathlib.Path(argv[2]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

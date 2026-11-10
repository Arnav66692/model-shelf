"""Build the Round 1 Skill zip: one top-level folder holding SKILL.md and references/*.md only."""
from __future__ import annotations

import pathlib
import sys
import zipfile

ALLOWED_SUFFIX = ".md"
FIXED_DATE = (2026, 11, 9, 0, 0, 0)


def package_members(pkg_dir: pathlib.Path) -> list[pathlib.Path]:
    members = [pkg_dir / "SKILL.md"] + sorted((pkg_dir / "references").glob("*" + ALLOWED_SUFFIX))
    missing = [str(p) for p in members if not p.is_file()]
    if missing:
        raise FileNotFoundError(f"package files missing: {missing}")
    return members


def build(pkg_dir: pathlib.Path, zip_path: pathlib.Path) -> list[str]:
    """Write the zip and return the member names, in order."""
    pkg_dir = pkg_dir.resolve()
    names: list[str] = []
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in package_members(pkg_dir):
            name = f"{pkg_dir.name}/{path.relative_to(pkg_dir).as_posix()}"
            info = zipfile.ZipInfo(name, date_time=FIXED_DATE)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes())
            names.append(name)
    return names


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        sys.stderr.write("usage: build_zip.py PACKAGE_DIR ZIP_PATH\n")
        return 2
    for name in build(pathlib.Path(argv[1]), pathlib.Path(argv[2])):
        sys.stdout.write(name + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

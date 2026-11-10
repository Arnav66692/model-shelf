"""Build the synthetic AI model library used by the Model Shelf test harness."""
import hashlib
import json
import pathlib
import random
import struct
import sys

GGUF_VERSION = 3
GGUF_STRING_TYPE = 8
GGUF_DATA_BYTES = 4096
SAFETENSORS_DATA_BYTES = 16
SEED = 7
SAFETENSORS_HEADER = (
    '{"__metadata__":{"format":"pt"},'
    '"w":{"dtype":"F32","shape":[2,2],"data_offsets":[0,16]}}'
)

TINY_PATH = "models/tiny-lantern/tiny-lantern-1b-instruct-q4.gguf"
HARBOR_PATH = "models/harbor-vision/harbor-vision-2b.gguf"
PIER_PATH = "models/image/pier-sketch/model.safetensors"
UNKNOWN_PATH = "models/image/unknown/model.safetensors"
DOWNLOAD_PATH = "downloads/final_v2.gguf"

TINY_NAME = "Tiny Lantern 1B Instruct"
HARBOR_NAME = "Harbor Vision 2B"
PIER_NAME = "Pier Sketch XL"
LICENCES = ["apache-2.0", "harbor-noncommercial-1.0", "openrail++"]
JOB = "I want a small chat model for client work. My memory budget is 4 GB."
QUILL_NAME = "Quill Coder 1B"
QUILL_SEED = 11
QUILL_EXTRA_BYTES = 3
QUILL_ARCHIVE_DIR = "archive/quill-coder"
QUILL_MODELS_DIR = "models/quill-coder"
QUILL_GGUF = "quill-coder-1b-q4.gguf"
SCENARIOS = ("park", "need")
NEED_JOB = "I want a small coding model and a speech to text model. My memory budget is 4 GB."
GUIDE_IDS = [
    "Qwen/Qwen2.5-1.5B-Instruct-GGUF",
    "Qwen/Qwen2.5-Coder-1.5B-Instruct-GGUF",
    "microsoft/Phi-4-mini-instruct",
    "meta-llama/Llama-3.2-3B-Instruct",
    "google/gemma-3-4b-it",
    "openai/whisper-large-v3-turbo",
    "ggerganov/whisper.cpp",
    "stabilityai/stable-diffusion-xl-base-1.0",
    "black-forest-labs/FLUX.1-schnell",
    "BAAI/bge-small-en-v1.5",
]


def _gguf_string(value: str) -> bytes:
    raw = value.encode("utf-8")
    return struct.pack("<Q", len(raw)) + raw


def make_gguf(arch: str, name: str, licence: str, rng: random.Random) -> bytes:
    pairs = [
        ("general.architecture", arch),
        ("general.name", name),
        ("general.license", licence),
    ]
    out = b"GGUF" + struct.pack("<I", GGUF_VERSION) + struct.pack("<Q", 0)
    out += struct.pack("<Q", len(pairs))
    for key, value in pairs:
        out += _gguf_string(key) + struct.pack("<I", GGUF_STRING_TYPE) + _gguf_string(value)
    return out + rng.randbytes(GGUF_DATA_BYTES)


def make_safetensors(rng: random.Random) -> bytes:
    header = SAFETENSORS_HEADER.encode("utf-8")
    return struct.pack("<Q", len(header)) + header + rng.randbytes(SAFETENSORS_DATA_BYTES)


def make_card(licence: str, title: str, lines: list) -> bytes:
    text = "\n".join(["---", f"license: {licence}", "---", f"# {title}", *lines]) + "\n"
    return text.encode("utf-8")


def _write(root: pathlib.Path, rel: str, data: bytes) -> None:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def _loose_entry(root, rel, name, licence) -> dict:
    data = (root / rel).read_bytes()
    return {
        "path": rel,
        "basename": pathlib.PurePosixPath(rel).name,
        "size": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "name": name,
        "licence": licence,
    }


def _write_models(root: pathlib.Path, rng: random.Random) -> bytes:
    tiny = make_gguf("lantern", TINY_NAME, "apache-2.0", rng)
    harbor = make_gguf("harbor", HARBOR_NAME, "harbor-noncommercial-1.0", rng)
    _write(root, TINY_PATH, tiny)
    _write(root, HARBOR_PATH, harbor)
    _write(root, PIER_PATH, make_safetensors(rng))
    _write(root, UNKNOWN_PATH, make_safetensors(rng))
    _write(root, "models/tiny-lantern/README.md", make_card("apache-2.0", TINY_NAME, [
        "Intended use: chat and instruction following in English.",
        "Memory: runs in about 2 GB.",
    ]))
    _write(root, "models/harbor-vision/README.md", make_card("harbor-noncommercial-1.0", HARBOR_NAME, [
        "Intended use: describing images.",
        "Non-commercial use only.",
        "Memory: runs in about 3 GB.",
    ]))
    _write(root, "models/image/pier-sketch/README.md", make_card("openrail++", PIER_NAME, [
        "Intended use: image generation.",
    ]))
    return tiny


def _write_duplicates(root: pathlib.Path, tiny: bytes) -> str:
    digest = hashlib.sha256(tiny).hexdigest()
    _write(root, DOWNLOAD_PATH, tiny)
    _write(root, f"toolstore/blobs/sha256-{digest}", tiny)
    manifest = {"layers": [{
        "mediaType": "application/vnd.example.model",
        "digest": f"sha256:{digest}",
        "size": len(tiny),
    }]}
    _write(root, "toolstore/manifests/registry.example/library/tiny-lantern/1b",
           json.dumps(manifest).encode("utf-8"))
    (root / "archive").mkdir(exist_ok=True)
    (root / "shelf").mkdir(exist_ok=True)
    return digest


def _write_parked_coder(root: pathlib.Path) -> None:
    rng = random.Random(QUILL_SEED)
    data = make_gguf("quill", QUILL_NAME, "apache-2.0", rng) + rng.randbytes(QUILL_EXTRA_BYTES)
    _write(root, f"{QUILL_ARCHIVE_DIR}/{QUILL_GGUF}", data)
    _write(root, f"{QUILL_ARCHIVE_DIR}/README.md", make_card("apache-2.0", QUILL_NAME, [
        "Intended use: code completion and code chat.",
        "Memory: runs in about 2 GB.",
    ]))


def build_fixture(root: pathlib.Path, scenario: str = "park") -> dict:
    """Create the library under root and return the truth dict."""
    if scenario not in SCENARIOS:
        raise ValueError(f"unknown scenario: {scenario!r}, expected one of {SCENARIOS}")
    root = pathlib.Path(root)
    rng = random.Random(SEED)
    tiny = _write_models(root, rng)
    digest = _write_duplicates(root, tiny)
    loose = [
        _loose_entry(root, TINY_PATH, TINY_NAME, "apache-2.0"),
        _loose_entry(root, HARBOR_PATH, HARBOR_NAME, "harbor-noncommercial-1.0"),
        _loose_entry(root, PIER_PATH, PIER_NAME, "openrail++"),
        _loose_entry(root, UNKNOWN_PATH, None, None),
        _loose_entry(root, DOWNLOAD_PATH, TINY_NAME, "apache-2.0"),
    ]
    if scenario == "need":
        _write_parked_coder(root)
    truth = {
        "loose_files": loose,
        "duplicate": {
            "sha256": digest,
            "paths": [TINY_PATH, DOWNLOAD_PATH],
            "store_blob": f"toolstore/blobs/sha256-{digest}",
        },
        "expected_moves": [{"src": DOWNLOAD_PATH, "dst": "archive/final_v2.gguf"}],
        "job": JOB,
        "job_answer": {"model": TINY_NAME, "quote": "chat and instruction following"},
        "licences": list(LICENCES),
        "job_answers": [{"model": TINY_NAME, "quote": "chat and instruction following"}],
        "licence_checks": [["Harbor Vision", "harbor-noncommercial-1.0"]],
        "what_to_get": None,
    }
    if scenario == "need":
        truth["expected_moves"] = truth["expected_moves"] + [
            {"src": f"{QUILL_ARCHIVE_DIR}/{QUILL_GGUF}", "dst": f"{QUILL_MODELS_DIR}/{QUILL_GGUF}"},
            {"src": f"{QUILL_ARCHIVE_DIR}/README.md", "dst": f"{QUILL_MODELS_DIR}/README.md"},
        ]
        truth["job"] = NEED_JOB
        truth["job_answers"] = [{"model": QUILL_NAME, "quote": "code completion"}]
        truth["job_answer"] = truth["job_answers"][0]
        truth["what_to_get"] = {
            "need": "speech to text",
            "must_mention_any": ["openai/whisper-large-v3-turbo", "ggerganov/whisper.cpp"],
            "allowed_ids": list(GUIDE_IDS),
        }
    return truth


def main(argv: list) -> int:
    scenario = "park"
    args = list(argv[1:])
    if len(args) == 4 and args[2] == "--scenario":
        scenario = args.pop(3)
        args.pop(2)
    if len(args) != 2:
        print("usage: make_fixture.py <sandbox_dir> <truth_json_path> [--scenario park|need]", file=sys.stderr)
        return 2
    try:
        truth = build_fixture(pathlib.Path(args[0]), scenario)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    pathlib.Path(args[1]).write_text(json.dumps(truth, indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

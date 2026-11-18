"""Build deterministic skill ZIP and ChatGPT reference files; exclude company workspaces."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME = "ai-company-context-architect"
ALLOWED_DIRS = {"references", "stages", "templates", "schemas", "adapters", "scripts", "tests"}
ALLOWED_ROOT = {"SKILL.md", "README.md", "IMPLEMENTATION-SPEC.md", "requirements.txt"}
ALLOWED_SUFFIX = {".md", ".txt", ".json", ".py"}


def collect():
    paths = []
    for p in ROOT.rglob("*"):
        if not p.is_file() or p.is_symlink():
            continue
        rel = p.relative_to(ROOT)
        if "__pycache__" in rel.parts or p.suffix not in ALLOWED_SUFFIX:
            continue
        if (len(rel.parts) == 1 and rel.name in ALLOWED_ROOT) or rel.parts[0] in ALLOWED_DIRS:
            paths.append(p)
    return sorted(paths)


def check_links(paths):
    missing = []
    for p in paths:
        if p.suffix != ".md":
            continue
        for link in re.findall(r"\[[^\]]+\]\(([^)]+)\)", p.read_text(encoding="utf-8")):
            if "://" in link or link.startswith("#") or "{{" in link:
                continue
            dest = (p.parent / link.split("#", 1)[0]).resolve()
            if not dest.is_relative_to(ROOT) or not dest.exists():
                missing.append(str(p.relative_to(ROOT)) + " -> " + link)
    if missing:
        raise ValueError("Broken/out-of-package links:\n" + "\n".join(missing))


def consolidate(paths):
    return "\n\n".join("===== FILE: " + str(p.relative_to(ROOT)).replace("\\", "/") + " =====\n\n"
                         + p.read_text(encoding="utf-8") for p in paths) + "\n"


def build(output):
    output = Path(output).resolve()
    if output == ROOT or ROOT in output.parents:
        raise ValueError("Distribution output must be outside the source skill directory.")
    paths = collect()
    check_links(paths)
    output.mkdir(parents=True, exist_ok=True)
    archive = output / (NAME + "-1.0.0.zip")
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for p in paths:
            rel = str(p.relative_to(ROOT)).replace("\\", "/")
            info = zipfile.ZipInfo(NAME + "/" + rel, date_time=(2026, 11, 14, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            zf.writestr(info, p.read_bytes())
    chat = output / "chatgpt"
    chat.mkdir(exist_ok=True)
    mapping = {
        "project-instructions.txt": (ROOT / "adapters/chatgpt-project-instructions.txt").read_text(encoding="utf-8"),
        "workflow-reference.txt": consolidate([ROOT / "SKILL.md"] + sorted((ROOT / "references").glob("*.md")) + sorted((ROOT / "stages").glob("*.md"))),
        "templates-and-schemas.txt": consolidate(sorted((ROOT / "templates").glob("*.md")) + sorted((ROOT / "schemas").glob("*.json"))),
        "SETUP.md": (ROOT / "adapters/chatgpt.md").read_text(encoding="utf-8"),
    }
    for name, content in mapping.items():
        (chat / name).write_bytes(content.encode("utf-8"))
    manifest = {
        "name": NAME, "version": "1.0.0", "source_files": len(paths),
        "archive": archive.name, "sha256": hashlib.sha256(archive.read_bytes()).hexdigest(),
        "chatgpt_files": [{"path": "chatgpt/" + name, "sha256": hashlib.sha256((chat / name).read_bytes()).hexdigest()} for name in sorted(mapping)],
        "live_platform_tests": "not_run",
    }
    (output / "package-manifest.json").write_bytes((json.dumps(manifest, indent=2) + "\n").encode("utf-8"))
    return manifest


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    try:
        print(json.dumps(build(args.output_dir), indent=2))
    except (OSError, ValueError) as exc:
        parser.exit(1, str(exc) + "\n")


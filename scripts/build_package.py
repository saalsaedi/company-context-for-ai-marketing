"""Build deterministic skill ZIP and ChatGPT reference files; exclude company workspaces."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import zipfile
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME = "ai-company-context-architect"
ALLOWED_DIRS = {"references", "stages", "templates", "schemas", "adapters", "scripts", "tests"}
ALLOWED_ROOT = {"SKILL.md", "README.md", "IMPLEMENTATION-SPEC.md", "requirements.txt", "release.json", "CHANGELOG.md"}
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


def write_zip(destination, entries, release_date):
    stamp = (release_date.year, release_date.month, release_date.day, 0, 0, 0)
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for name, data in entries:
            info = zipfile.ZipInfo(name, date_time=stamp)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            zf.writestr(info, data)


def build(output):
    output = Path(output).resolve()
    if output == ROOT or ROOT in output.parents:
        raise ValueError("Distribution output must be outside the source skill directory.")
    paths = collect()
    check_links(paths)
    release = json.loads((ROOT / "release.json").read_text(encoding="utf-8"))
    version = release["version"]
    if not re.fullmatch(r"\d+\.\d+\.\d+", version) or release["name"] != NAME:
        raise ValueError("Invalid package version or name in release.json")
    release_date = date.fromisoformat(release["release_date"])
    output.mkdir(parents=True, exist_ok=True)
    archive = output / (NAME + "-" + version + ".zip")
    write_zip(archive, [(NAME + "/" + p.relative_to(ROOT).as_posix(), p.read_bytes()) for p in paths], release_date)
    chat = output / "chatgpt"
    chat.mkdir(exist_ok=True)
    mapping = {
        "project-instructions.txt": (ROOT / "adapters/chatgpt-project-instructions.txt").read_text(encoding="utf-8"),
        "workflow-reference.txt": consolidate([ROOT / "SKILL.md"] + sorted((ROOT / "references").glob("*.md")) + sorted((ROOT / "stages").glob("*.md"))),
        "templates-and-schemas.txt": consolidate(sorted(p for p in paths if p.parent == ROOT / "templates") + sorted((ROOT / "schemas").glob("*.json"))),
        "SETUP.md": (ROOT / "adapters/chatgpt.md").read_text(encoding="utf-8"),
    }
    for name, content in mapping.items():
        (chat / name).write_bytes(content.encode("utf-8"))
    chat_archive = output / ("chatgpt-setup-" + version + ".zip")
    write_zip(chat_archive, [("chatgpt-setup/" + name, mapping[name].encode("utf-8")) for name in sorted(mapping)], release_date)
    artifacts = [{"path": p.name, "sha256": hashlib.sha256(p.read_bytes()).hexdigest()} for p in (archive, chat_archive)]
    checksums = "SHA256SUMS-" + version + ".txt"
    (output / checksums).write_bytes(("\n".join(a["sha256"] + "  " + a["path"] for a in artifacts) + "\n").encode("utf-8"))
    manifest = {
        "name": NAME, "version": version, "context_schema_version": release["context_schema_version"], "source_files": len(paths),
        "archive": archive.name, "sha256": hashlib.sha256(archive.read_bytes()).hexdigest(),
        "chatgpt_archive": chat_archive.name, "artifacts": artifacts, "checksums": checksums,
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


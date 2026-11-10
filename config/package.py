#!/usr/bin/env python3
"""Build a portable Divan installer containing helpers/docs and no runtime state."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import tarfile


def build(root, output):
    allowed = [root / name for name in ("README.md", "AGENTS.md", "CLAUDE.md", "GEMINI.md", "KATILIM.md", "GECERLI_DUZEN.md")]
    for folder, pattern in [("bin", "*.py"), ("tests", "*.py"), ("config", "*.py"),
                            ("config", "*.sh"), ("config", "*.md"),
                            ("config/clients", "*.json"),
                            ("windows", "*.ps1"), ("windows", "*.md"),
                            ("03_sablonlar", "*.md"), ("00_yonetim", "TALIMATLAR.md"),
                            ("00_yonetim/kaynaklar", "*.txt"),
                            ("arastirma", "*.md")]:
        allowed.extend((root / folder).glob(pattern))
    allowed.extend((root / "02_karargahlar").glob("*/BASLANGIC.md"))
    files = sorted(set(p for p in allowed if p.is_file()))
    # No work, results, claims, control state or registry belong in the installer.
    if not files or not (root / "bin/divan.py").is_file():
        raise ValueError("Divan kaynak dizini eksik.")
    for path in files:
        if path.is_symlink() or not path.resolve().is_relative_to(root.resolve()):
            raise ValueError(f"Kurulum dosyası paket dışına bağlanamaz: {path.name}")
    payloads = {p: p.read_bytes() for p in files}
    manifest = {p.relative_to(root).as_posix(): hashlib.sha256(raw).hexdigest()
                for p, raw in payloads.items()}
    output.parent.mkdir(parents=True, exist_ok=True)
    checksum_path = output.with_name(output.name + ".sha256")
    if output.exists() or checksum_path.exists():
        raise FileExistsError("Var olan kurulum paketi veya özeti korunuyor.")
    with output.open("xb") as stream:
        with tarfile.open(fileobj=stream, mode="w:gz") as archive:
            for path in files:
                info = archive.gettarinfo(path, arcname="divan/" + path.relative_to(root).as_posix())
                info.size = len(payloads[path])
                archive.addfile(info, io.BytesIO(payloads[path]))
            raw = (json.dumps({"surum": 1, "dosyalar": manifest}, ensure_ascii=False, indent=2) + "\n").encode()
            info = tarfile.TarInfo("divan/PAKET_MANIFEST.json")
            info.size = len(raw)
            info.mode = 0o644
            archive.addfile(info, io.BytesIO(raw))
    with output.open("rb") as stream:
        checksum = hashlib.file_digest(stream, "sha256").hexdigest()
    with checksum_path.open("x", encoding="utf-8") as stream:
        stream.write(checksum + "  " + output.name + "\n")
    print(f"Paket: {output}\nSHA256: {checksum}\nStatik dosya: {len(files)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    build(Path(__file__).resolve().parents[1], args.output.resolve())

"""Portable installer checks using isolated source and destination directories."""
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import subprocess
import sys
import tarfile
import tempfile
import unittest
from uuid import uuid4


SOURCE = Path(__file__).resolve().parents[1]


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="divan-package-test-")
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / "source"
        # Copy only static implementation files; never read live work/results.
        for relative in ("README.md", "AGENTS.md", "bin/divan.py", "bin/divan_git.py",
                         "config/package.py", "config/install.sh", "config/start_skill.md"):
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(SOURCE / relative, target)
        for relative in ("03_sablonlar/ornek.md", "00_yonetim/KAPSAM.md",
                         "00_yonetim/kaynaklar/readme.txt", "arastirma/kaynaklar.md",
                         "02_karargahlar/01_codex_karargahi/BASLANGIC.md",
                         "tests/test_placeholder.py"):
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("Statik kurulum belgesi\n", encoding="utf-8")
        self.flow(self.root, "init")
        self.private = "runtime-private-" + uuid4().hex
        member = self.root / "02_karargahlar/01_codex_karargahi/uyeler/codex_cli"
        for relative in ("calisma/not.md", "sonuclar_1/yerel.md", "alindi/alindi.json"):
            (member / relative).write_text(self.private, encoding="utf-8")
        for relative in ("01_ortak_alan/yeni_0/runtime.json", "00_yonetim/targets.json",
                         "config/private_target.json", "ignored-runtime.txt"):
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(json.dumps({"url": "https://private-target.invalid/" + self.private}),
                              encoding="utf-8")
        self.flow(self.root, "control", "--state", "duraklat", "--reason", self.private)
        self.output = self.base / "output/divan-installer.tar.gz"
        self.caller = self.base / "unrelated-cwd"
        self.caller.mkdir()

    def shell(self, *args, ok=True):
        env = os.environ.copy()
        env.pop("DIVAN_ROOT", None)
        result = subprocess.run(args, cwd=self.caller if hasattr(self, "caller") else self.base,
                                env=env, text=True, capture_output=True, timeout=25)
        if ok:
            self.assertEqual(result.returncode, 0, result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0, result.stdout)
        return result

    def flow(self, root, *args):
        return self.shell(sys.executable, str(root / "bin/divan.py"), "--root", str(root), *args)

    def build(self):
        self.shell(sys.executable, str(self.root / "config/package.py"), "--output", str(self.output))

    def extract_and_verify(self):
        checksum = self.output.with_name(self.output.name + ".sha256")
        expected, filename = checksum.read_text(encoding="utf-8").strip().split("  ", 1)
        self.assertEqual(filename, self.output.name)
        self.assertEqual(hashlib.sha256(self.output.read_bytes()).hexdigest(), expected)
        destination = self.base / "different-host/location"
        destination.mkdir(parents=True)
        with tarfile.open(self.output, "r:gz") as archive:
            members = archive.getmembers()
            names = {member.name for member in members}
            for member in members:
                path = PurePosixPath(member.name)
                self.assertFalse(path.is_absolute())
                self.assertNotIn("..", path.parts)
                self.assertTrue(member.isfile())
                self.assertTrue(member.name.startswith("divan/"))
                content = archive.extractfile(member).read()
                self.assertNotIn(self.private.encode(), content)
            for excluded in ("divan/01_ortak_alan/", "divan/02_karargahlar/01_codex_karargahi/uyeler/",
                             "divan/00_yonetim/denetim.json", "divan/00_yonetim/uyeler.json",
                             "divan/00_yonetim/targets.json", "divan/config/private_target.json"):
                self.assertFalse(any(name.startswith(excluded) for name in names), excluded)
            archive.extractall(destination, filter="data")
        root = destination / "divan"
        manifest = json.loads((root / "PAKET_MANIFEST.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["surum"], 1)
        expected_files = {name.removeprefix("divan/") for name in names
                          if name != "divan/PAKET_MANIFEST.json"}
        self.assertEqual(set(manifest["dosyalar"]), expected_files)
        for relative, digest in manifest["dosyalar"].items():
            self.assertEqual(hashlib.sha256((root / relative).read_bytes()).hexdigest(), digest)
        return root

    def test_package_whitelist_and_manifest_exclude_runtime_and_private_targets(self):
        self.build()
        root = self.extract_and_verify()
        for relative in ("bin/divan.py", "bin/divan_git.py", "config/install.sh",
                         "03_sablonlar/ornek.md", "00_yonetim/kaynaklar/readme.txt"):
            self.assertTrue((root / relative).is_file())
        before = self.output.read_bytes()
        self.shell(sys.executable, str(self.root / "config/package.py"),
                   "--output", str(self.output), ok=False)
        self.assertEqual(self.output.read_bytes(), before)

    def test_relocated_install_from_arbitrary_cwd_preserves_pause_and_local_note(self):
        self.build()
        root = self.extract_and_verify()
        self.assertFalse((root / "00_yonetim/denetim.json").exists())
        self.shell("bash", str(root / "config/install.sh"))
        self.flow(root, "control", "--state", "duraklat", "--reason", "Local user pause")
        note = root / "02_karargahlar/01_codex_karargahi/uyeler/codex_cli/calisma/kullanici.md"
        note.write_text("Preserved local user note\n", encoding="utf-8")
        control = root / "00_yonetim/denetim.json"
        registry = root / "00_yonetim/uyeler.json"
        before = (control.read_bytes(), registry.read_bytes(), note.read_bytes())
        self.shell("bash", str(root / "config/install.sh"))
        self.assertEqual((control.read_bytes(), registry.read_bytes(), note.read_bytes()), before)
        self.assertEqual(json.loads(control.read_text())["durum"], "duraklat")

    def test_package_refuses_static_file_symlink_outside_root(self):
        external = self.base / "outside.md"
        external.write_text(self.private, encoding="utf-8")
        (self.root / "CLAUDE.md").symlink_to(external)
        self.shell(sys.executable, str(self.root / "config/package.py"),
                   "--output", str(self.output), ok=False)
        self.assertFalse(self.output.exists())

    def test_installer_does_not_initialize_an_unrelated_environment_root(self):
        self.build()
        root = self.extract_and_verify()
        other = self.base / "other-runtime"
        env = os.environ.copy()
        env["DIVAN_ROOT"] = str(other)
        result = subprocess.run(["bash", str(root / "config/install.sh")], cwd=self.caller,
                                env=env, capture_output=True, text=True, timeout=25)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((root / "00_yonetim/denetim.json").is_file())
        self.assertFalse(other.exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)

#!/usr/bin/env python3
"""`schemas/` altındaki JSON sözleşmelerini standart kütüphaneyle denetler.

Dış paket kullanılmaz. Desteklenen JSON Schema alt kümesi bilinçli olarak dardır:
depodaki sözleşmelerin kullandığı anahtar sözcüklerle sınırlıdır. Bir şema bu
kümenin dışına çıkarsa denetim sessizce geçmez; açık hata verir. Böylece "şema
dosyası var" ile "şema gerçekten denetleniyor" aynı şey sayılmaz.

Kullanım:
    python tools/sema_denetle.py                       # bütün şemaların biçimi
    python tools/sema_denetle.py --sema deus-event --veri olay.json
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
import sys

KOK = Path(__file__).resolve().parents[1]
SEMA_DIZINI = KOK / "schemas"

DESTEKLENEN = {
    "$schema", "$id", "$comment", "$defs", "$ref", "title", "description", "default",
    "type", "required", "properties", "additionalProperties", "const", "enum",
    "pattern", "format", "minimum", "maximum", "minLength", "maxLength",
    "minItems", "maxItems", "items", "oneOf",
}
TIPLER = {
    "object": dict, "array": list, "string": str, "integer": int,
    "number": (int, float), "boolean": bool, "null": type(None),
}
BICIMLER = {"date-time": re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?(Z|[+-]\d{2}:\d{2})$")}


class SemaHatasi(ValueError):
    """Şema dosyasının kendisi desteklenen alt kümeye uymuyor."""


def sema_yukle(ad: str) -> dict:
    yol = SEMA_DIZINI / (ad if ad.endswith(".json") else f"{ad}.schema.json")
    return json.loads(yol.read_text(encoding="utf-8"))


def _tip_uyar(deger, tip: str) -> bool:
    beklenen = TIPLER[tip]
    if tip in ("integer", "number") and isinstance(deger, bool):
        return False
    if tip == "integer" and isinstance(deger, float):
        return deger.is_integer()
    return isinstance(deger, beklenen)


def _cozumle(kok: dict, ref: str) -> dict:
    if not ref.startswith("#/"):
        raise SemaHatasi(f"yalnız yerel $ref desteklenir: {ref}")
    hedef = kok
    for parca in ref[2:].split("/"):
        if not isinstance(hedef, dict) or parca not in hedef:
            raise SemaHatasi(f"$ref çözülemedi: {ref}")
        hedef = hedef[parca]
    return hedef


def sema_bicimini_denetle(sema: dict, yol: str = "#") -> list[str]:
    """Şemanın desteklenen alt kümede kalıp kalmadığını, yazılmadan denetler."""
    hatalar: list[str] = []

    def gez(parca, konum: str) -> None:
        if not isinstance(parca, dict):
            hatalar.append(f"{konum}: şema düğümü nesne olmalı")
            return
        for anahtar in parca:
            if anahtar not in DESTEKLENEN:
                hatalar.append(f"{konum}: desteklenmeyen anahtar '{anahtar}'")
        if "type" in parca and parca["type"] not in TIPLER:
            hatalar.append(f"{konum}: bilinmeyen tür {parca['type']!r}")
        if "pattern" in parca:
            try:
                re.compile(parca["pattern"])
            except re.error as exc:
                hatalar.append(f"{konum}: geçersiz desen ({exc})")
        if "format" in parca and parca["format"] not in BICIMLER:
            hatalar.append(f"{konum}: desteklenmeyen biçim {parca['format']!r}")
        if "$ref" in parca:
            try:
                _cozumle(sema, parca["$ref"])
            except SemaHatasi as exc:
                hatalar.append(f"{konum}: {exc}")
        if parca.get("additionalProperties") is False:
            bilinen = set(parca.get("properties", {}))
            for ad in parca.get("required", []):
                if ad not in bilinen:
                    hatalar.append(f"{konum}: zorunlu '{ad}' properties içinde tanımlı değil")
        for ad, alt in parca.get("properties", {}).items():
            gez(alt, f"{konum}/properties/{ad}")
        for ad, alt in parca.get("$defs", {}).items():
            gez(alt, f"{konum}/$defs/{ad}")
        if "items" in parca:
            gez(parca["items"], f"{konum}/items")
        for sira, alt in enumerate(parca.get("oneOf", [])):
            gez(alt, f"{konum}/oneOf/{sira}")
        if isinstance(parca.get("additionalProperties"), dict):
            gez(parca["additionalProperties"], f"{konum}/additionalProperties")

    gez(sema, yol)
    return hatalar


def dogrula(sema: dict, veri, kok: dict | None = None, konum: str = "$") -> list[str]:
    """Veriyi şemaya göre denetler; her hata JSON yolunu taşır. Boş liste = uyumlu."""
    kok = sema if kok is None else kok
    if "$ref" in sema:
        return dogrula(_cozumle(kok, sema["$ref"]), veri, kok, konum)
    hatalar: list[str] = []
    if "const" in sema and (veri != sema["const"] or type(veri) is not type(sema["const"])):
        hatalar.append(f"{konum}: {sema['const']!r} olmalı, {veri!r} bulundu")
    if "enum" in sema and veri not in sema["enum"]:
        hatalar.append(f"{konum}: {veri!r} izin verilen değerlerden değil")
    if "type" in sema and not _tip_uyar(veri, sema["type"]):
        hatalar.append(f"{konum}: tür {sema['type']} bekleniyor, {type(veri).__name__} bulundu")
        return hatalar
    if "oneOf" in sema:
        uyanlar = [alt for alt in sema["oneOf"] if not dogrula(alt, veri, kok, konum)]
        if len(uyanlar) != 1:
            hatalar.append(f"{konum}: oneOf dallarından tam biri uymalı ({len(uyanlar)} uydu)")
    if isinstance(veri, str):
        if "minLength" in sema and len(veri) < sema["minLength"]:
            hatalar.append(f"{konum}: en az {sema['minLength']} karakter")
        if "maxLength" in sema and len(veri) > sema["maxLength"]:
            hatalar.append(f"{konum}: en çok {sema['maxLength']} karakter")
        if "pattern" in sema and not re.search(sema["pattern"], veri):
            hatalar.append(f"{konum}: {sema['pattern']!r} desenine uymuyor")
        if "format" in sema and not BICIMLER[sema["format"]].match(veri):
            hatalar.append(f"{konum}: {sema['format']} biçiminde değil")
    if isinstance(veri, (int, float)) and not isinstance(veri, bool):
        if "minimum" in sema and veri < sema["minimum"]:
            hatalar.append(f"{konum}: en az {sema['minimum']}")
        if "maximum" in sema and veri > sema["maximum"]:
            hatalar.append(f"{konum}: en çok {sema['maximum']}")
    if isinstance(veri, list):
        if "minItems" in sema and len(veri) < sema["minItems"]:
            hatalar.append(f"{konum}: en az {sema['minItems']} öğe")
        if "maxItems" in sema and len(veri) > sema["maxItems"]:
            hatalar.append(f"{konum}: en çok {sema['maxItems']} öğe")
        if "items" in sema:
            for sira, oge in enumerate(veri):
                hatalar.extend(dogrula(sema["items"], oge, kok, f"{konum}[{sira}]"))
    if isinstance(veri, dict):
        ozellikler = sema.get("properties", {})
        for ad in sema.get("required", []):
            if ad not in veri:
                hatalar.append(f"{konum}: zorunlu alan '{ad}' yok")
        for ad, deger in veri.items():
            if ad in ozellikler:
                hatalar.extend(dogrula(ozellikler[ad], deger, kok, f"{konum}.{ad}"))
            elif sema.get("additionalProperties") is False:
                hatalar.append(f"{konum}: beklenmeyen alan '{ad}'")
            elif isinstance(sema.get("additionalProperties"), dict):
                hatalar.extend(dogrula(sema["additionalProperties"], deger, kok, f"{konum}.{ad}"))
    return hatalar


def butun_semalar() -> dict[str, dict]:
    return {yol.name: json.loads(yol.read_text(encoding="utf-8"))
            for yol in sorted(SEMA_DIZINI.glob("*.schema.json"))}


def utf8_cikti() -> None:
    """Windows konsolu ve -I ile PYTHONUTF8 yok sayıldığında da Türkçe çıktı yazılabilsin."""
    for akis in (sys.stdout, sys.stderr):
        if hasattr(akis, "reconfigure"):
            akis.reconfigure(encoding="utf-8", errors="replace")


def main() -> int:
    utf8_cikti()
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--sema", help="şema adı (ör. deus-event) veya schemas/ altındaki dosya adı")
    parser.add_argument("--veri", help="denetlenecek JSON dosyası; --sema ile birlikte")
    args = parser.parse_args()
    if bool(args.sema) != bool(args.veri):
        parser.error("--sema ve --veri birlikte verilir")
    kusurlar = 0
    if args.sema:
        sema = sema_yukle(args.sema)
        veri = json.loads(Path(args.veri).read_text(encoding="utf-8"))
        for hata in sema_bicimini_denetle(sema) + dogrula(sema, veri):
            print(f"{args.veri}: {hata}")
            kusurlar += 1
        if not kusurlar:
            print(f"UYUMLU: {args.veri} ↔ {args.sema}")
        return 1 if kusurlar else 0
    semalar = butun_semalar()
    for ad, sema in semalar.items():
        for hata in sema_bicimini_denetle(sema):
            print(f"{ad}: {hata}")
            kusurlar += 1
    if kusurlar:
        return 1
    print(f"TAMAM: {len(semalar)} şema desteklenen alt kümede ve iç başvuruları çözülüyor.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Klavye çizimlerinin ortak kuralları: belgelerdeki ```text blokları.

Bir çizim yalnız tek genişlikli karakterlerle yazılır, böylece her yazı tipinde ve her ekranda
aynı hizada durur: yazdırılabilir ASCII, Türkçe harfler, birkaç işaret, oklar, kutu çizgileri, blok
öğeleri ve geometrik şekiller. Satır en çok EN_GENIS sütundur; sekme ve satır sonu boşluğu yoktur.
Okuma sayfası üreticisi bu blokları olduğu gibi <pre> içinde gösterir.

Kullanım (modül olarak): cizimler(metin) blokları verir, denetle(ad, metin) kural ihlallerini.
"""
from __future__ import annotations

import re

EN_GENIS = 64
_TURKCE = "çÇğĞıİöÖşŞüÜâÂîÎûÛ"
_ISARET = "·…×÷±≤≥≠°"
BLOK = re.compile(r"(?ms)^```text[ \t]*\n(.*?)^```[ \t]*$")


def izinli(karakter: str) -> bool:
    kod = ord(karakter)
    return (0x20 <= kod <= 0x7E or karakter in _TURKCE or karakter in _ISARET
            or 0x2190 <= kod <= 0x21FF      # oklar
            or 0x2500 <= kod <= 0x257F      # kutu çizgileri
            or 0x2580 <= kod <= 0x259F      # blok öğeleri
            or 0x25A0 <= kod <= 0x25FF)     # geometrik şekiller


def cizimler(metin: str) -> list[str]:
    return [m.group(1) for m in BLOK.finditer(metin)]


def cizimsiz(metin: str) -> str:
    """Çizim bloklarını çıkarır; okunabilirlik ve yapı denetimleri çizimleri metin saymaz."""
    return BLOK.sub("", metin)


def denetle(ad: str, metin: str, en_genis: int = EN_GENIS) -> list[str]:
    hatalar = []
    for sira, cizim in enumerate(cizimler(metin), 1):
        for no, satir in enumerate(cizim.split("\n"), 1):
            if not satir:
                continue
            if "\t" in satir:
                hatalar.append(f"{ad}: {sira}. çizim, {no}. satır: sekme var")
            if satir != satir.rstrip():
                hatalar.append(f"{ad}: {sira}. çizim, {no}. satır: satır sonunda boşluk var")
            if len(satir) > en_genis:
                hatalar.append(f"{ad}: {sira}. çizim, {no}. satır {len(satir)} sütun (en çok {en_genis})")
            yasak = sorted({k for k in satir if not izinli(k)})
            if yasak:
                hatalar.append(f"{ad}: {sira}. çizim, {no}. satır: tek genişlikli olmayabilecek karakter: {''.join(yasak)}")
    return hatalar

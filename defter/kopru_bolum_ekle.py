#!/usr/bin/env python3
"""Ortak Köprü sayfasının “Yönlendirme dosyası” bölümüne bir alt bölüm (parça) ekler ya da aynı kimlikli parçayı yeniler.
Kullanım: python3 defter/kopru_bolum_ekle.py kopru.html docs/gecmis/parcalar/bolum-guncel-2026-10-24.html
Parça dosyası tek bir <div id="y-…" class="alt"> … </div> içerir. Aynı id sayfada varsa yerine konur; yoksa
“Mimari: ikimiz için” (#y-mimari) parçasının önüne, o da yoksa bölümün sonuna eklenir. Kayıtlara dokunmaz.
Parça yazılmadan önce kayıt ekleyicinin dış yükleme ve yasak desen denetimlerinden geçer; birine takılırsa
sayfa değişmez. Sonra kopru_ekle.py --kontrol ile denetle ve yerel/kopru_gonder.ps1 ile gönder. Yalnız standart kütüphane."""
import os, re, sys, tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kopru_ekle import dis_yukleme_kontrol, yasak_kontrol  # noqa: E402


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    sayfa_yolu, parca_yolu = sys.argv[1], sys.argv[2]
    sayfa = open(sayfa_yolu, encoding="utf-8").read()
    parca = open(parca_yolu, encoding="utf-8").read().strip()
    m = re.match(r'<div id="(y-[A-Za-z0-9-]+)" class="alt">', parca)
    if not m or not parca.endswith("</div>"):
        sys.exit("HATA: parça <div id=\"y-…\" class=\"alt\"> ile başlayıp </div> ile bitmeli.")
    pid = m.group(1)
    sorunlar = dis_yukleme_kontrol(parca)
    if sorunlar:
        sys.exit("HATA: parça dış kaynak yüklüyor, köprü kuralı bozulur:\n  " + "\n  ".join(sorunlar))
    yasak = yasak_kontrol(parca)
    if yasak:
        sys.exit("HATA: parçada yasak desen var: " + ", ".join(yasak))
    b = re.search(r'<section id="yonlendirme"[^>]*>.*?</section>', sayfa, re.S)
    if not b:
        sys.exit("HATA: sayfada <section id=\"yonlendirme\"> yok.")
    bolum = b.group(0)
    eski = re.search(r'\n?  <div id="%s" class="alt">.*?\n  </div>\n' % re.escape(pid), bolum, re.S)
    girinti = "\n".join("  " + s if s else s for s in parca.splitlines())
    if eski:
        yeni_bolum = bolum[:eski.start()] + "\n" + girinti + "\n" + bolum[eski.end():]
        islem = "yenilendi"
    else:
        hedef = bolum.find('  <div id="y-mimari" class="alt">')
        if hedef < 0:
            hedef = bolum.rfind("</section>")
        yeni_bolum = bolum[:hedef] + girinti + "\n\n" + bolum[hedef:]
        islem = "eklendi"
    yeni = sayfa[:b.start()] + yeni_bolum + sayfa[b.end():]
    klasor = os.path.dirname(os.path.abspath(sayfa_yolu))
    fd, gecici = tempfile.mkstemp(prefix="kopru-", suffix=".html", dir=klasor)
    with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(yeni)
    os.replace(gecici, sayfa_yolu)
    print(f"{pid} {islem}: {sayfa_yolu}")


if __name__ == "__main__":
    main()

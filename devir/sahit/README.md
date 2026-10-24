# Şahit CLI devir paketi

Durum: **hazır/bekliyor**. Bu paket bulut oturumunu yerel makineye taşımaz. CLI devamı, kullanıcı bu paketi kendi kurulu Copilot CLI oturumunda gözden geçirip açıkça kabul edene kadar gerçekleşmiş sayılmaz.

## Paket

- `source.json`: tek kanonik devir kaynağı.
- `handoff.txt`, `handoff.html`, `handoff.json`: aynı içeriğin çevrimdışı, deterministik dışa aktarımları.
- `START_HERE.md`: aynı kaynakta tutulan yerel başlangıç istemi.
- `manifest.json`: kaynak ve çıktılar için SHA-256; ayrıca okunan repository dosyalarının göreli yolları/hashleri. Manifest kendi kendisini hash'lemez.

Üret ve doğrula:

```console
python3 devir/sahit/generate.py
python3 devir/sahit/generate.py --check
```

Python standart kütüphanesi yeterlidir; ağ veya model çağrısı yapılmaz. HTML, tek dosyalı statik sayfadır; dış betik, stil, font veya kaynak yüklemez ve metin HTML-escape edilir.

## Yerel Şahit kapısı

`Kopru_Izle.cmd SahitDevam` varsayılan olarak yalnız önizleme gösterir. Önizleme dosya yazmaz, CLI/SSH başlatmaz ve ağa/model sağlayıcısına çağrı yapmaz. Açıkça yerel CLI etkileşimi başlatmak için:

```console
Kopru_Izle.cmd SahitDevam -Secenek Baslat
```

Komut satırından exe, Home ve repo dizini özelleştirilebilir:

```console
pwsh -NoProfile -File kopru_yerel.ps1 -Mod SahitDevam `
  -CopilotExePath "C:\...\copilot.exe" -SahitHomePath "C:\...\Home" `
  -DepoPath "C:\...\ortak-kopru"
```

Kurulu CLI'ı kullanıcı kendi makinesinde, seçtiği Home ile kontrol eder:

```console
Kopru_Izle.cmd SahitDevam -Secenek Surum
Kopru_Izle.cmd SahitDevam -Secenek Yardim
```

Model seçimi için bu sürümün gerçek `--help` çıktısını ve etkileşimli arayüzünü kullan. Yalnız kurulu CLI'ın sunduğu model seçimini kullanıcı yapsın; paket bir model adı/efor seviyesi varsaymaz. Bu cloud çalışması Windows/WinPE binary'sini görmediği için yerel sürüm ve model kataloğu doğrulanmış değildir. Oturum, `devir/sahit/START_HERE.md` içindeki istemle açılır; `@dosya` benzeri bir dosya referans sözdizimi, kurulu CLI help'i doğrulamıyorsa varsayılmaz.

Başlatıcı herhangi bir tool izinlerini genişleten bayrak eklemez. `--allow-all-tools`, guardian/sandbox/onay kapatma, otomatik CLI zinciri ve sürekli bot döngüsü yoktur. Açık başlatma etkileşimli CLI'ı açar; görev metnini kullanıcı verir. Yerel CLI'ın kendi davranışı ve sağlayıcı katmanları bu wrapper tarafından tam görünür kılınamaz.

## Kapsam ve sınırlar

Bu, tam sohbet export'u değildir. `source.json` kapsamı, kesintileri ve eksik kaynakları listeler; kullanıcı mesajlarını, asistan önerilerini ve doğrulanmış araç sonuçlarını ayrı tutar. Önceki task URL'leri tamamlanmış kabul edilmez. Açık PR #1–#3 ayrı dallardadır; bu paket onları birleştirmez. PR #3'ün opt-in policy/provenance yaklaşımı dikkate alınır, ancak merge edilmiş sayılmaz.

Manifest yalnız repository-relative path/hash içerir. Yerel kurulum dizinleri, Home/cache, oturum dosyaları ve anahtarlar yayımlanmaz. Hashler doğruluk, kimlik, değişmezlik veya bütün gizli verilerin yokluğunu kanıtlamaz. Kapalı sağlayıcı sistem istemlerine, model ağırlıklarına veya sunucu altyapısına erişim iddiası yoktur.

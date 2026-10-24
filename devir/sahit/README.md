# Şahit CLI devir paketi

Durum: **hazır/bekliyor.** Bu paket bulut oturumunu yerel makineye taşımaz. CLI devamı, kullanıcı paketi kendi kurulu Copilot CLI oturumunda gözden geçirip açıkça kabul edene kadar gerçekleşmiş sayılmaz ([Kabul](#kabul)).

Sürüm `2026-10-24.2` (öncesi: PR #4'teki `2026-10-24.1`). Sürüm, tarih ve hash'ler `manifest.json`'dadır; paket tek manifestle bağlıdır.

## Paket

| Dosya | Ne |
| --- | --- |
| `source.json` | Tek kanonik kaynak; elle düzenlenen tek dosya. |
| `handoff.txt`, `handoff.html`, `handoff.json` | Aynı içeriğin çevrimdışı, deterministik dışa aktarımları: insan okunur, statik HTML, makine okunur. |
| `START_HERE.md` | Yerel oturuma verilecek başlangıç istemi (`source.json` içindeki `startup_prompt`). |
| `manifest.json` | Sürüm, tarih, kaynak/çıktı/bağlı dosya hash'leri ve `bundle_sha256`. Kendi kendini hash'lemez. |
| `handoff.schema.json`, `manifest.schema.json` | JSON şemaları; `generate.py` bunlarla doğrular (yalnız stdlib). |
| `generate.py` | Çıktıları ve manifesti üretir; `--check` doğrular; `--drift` sapmayı gösterir. |

JSON alan eşlemesi: **kapsam** = `scope`; **tamlık** = `completeness_matrix` (`kesin` / `kısmi` / `eksik`); **eksik kaynak** = `missing_sources`; **eksik işler, öncelik sırasıyla** = `open_items` (`priority`); **kanıt** = her satırın `evidence` alanı (dosya:satır ya da commit); **güvenlik sınırları** = `scope.privacy_boundary` ve `known_risks`; **doğrulanamayan varsayımlar** = `missing_sources` ile `access_map` içindeki "unverified/unavailable" satırları; **yerelde gözlenenler** = `local_verification`.

### Manifest: bağlı ve gözlenen dosyalar

- **Bağlı** (`pinned_sources_sha256`): pakete ait dosyalar (bu klasör, `deus_ex_machina/`, `tests/`). Değişirlerse `--check` başarısız olur.
- **Gözlenen** (`observed_sources_sha256`): pakete ait olmayan, yalnız okunan köprü dosyaları (`kopru.html`, `kopru_yerel.ps1` vb.). Başkaları değiştirir (botla saatlik); hash'leri anlık görüntüdür, sapma `--drift` ile bilgi olarak gösterilir ve hata sayılmaz.
- `bundle_sha256`: kaynak, çıktılar ve bağlı dosyalardan türeyen tek paket kimliği. Hash'ler LF'ye çevrilmiş baytlar üzerinden hesaplanır.

## Üret ve doğrula

Python standart kütüphanesi yeterlidir; ağ ya da model çağrısı yapılmaz. HTML tek dosyalık statik sayfadır: dış betik, stil, font ya da kaynak yüklemez; metin HTML-escape edilir.

```console
python3 devir/sahit/generate.py            # source.json -> çıktılar + manifest (gözlenen hash'ler yenilenir)
python3 devir/sahit/generate.py --check    # yazmadan: çıktılar, şema, bağlı dosyalar
python3 devir/sahit/generate.py --drift    # yalnız bilgi: gözlenen dosya sapmaları
```

`source.json` ya da bağlı bir dosya değiştiyse önce üret, sonra `--check` çalıştır. Windows'ta `python3` yoksa `kopru_yerel.ps1:36`'teki `$PythonExe` (taşınabilir Python) kullanılır.

## Devralma komutları (sırayla)

Depo kökünde çalışır. 1-4 salt okunur ve model çağırmaz; 5 etkileşimli oturumu açar. Her adımın çıktısını gözle; beklenmedikse dur.

| # | Komut | Ne yapar, yan etkisi | Not |
| --- | --- | --- | --- |
| 1 | `python3 devir/sahit/generate.py --check` | Paket bütünlüğü ve şema. Yazmaz. | Çıktıdaki `bundle_sha256` ilk 12 hanesini not al. |
| 2 | `python3 devir/sahit/generate.py --drift` | Gözlenen dosyaların anlık görüntüden sapması. Yazmaz. | Sapma hata değildir; okunacak farkı gösterir. |
| 3 | `Kopru_Izle.cmd SahitDevam` | Kuru önizleme: yolları gösterir. Dosya yazmaz; süreç, ssh ya da ağ başlatmaz; git yapılandırmasına dokunmaz (`kopru_yerel.ps1:62-118`). | Yürütülebilir dosya ya da depo yoksa hata verir. |
| 4 | `Kopru_Izle.cmd SahitDevam -Secenek Surum`, sonra `... -Secenek Yardim` | Yalnız `copilot --version` / `--help` çalıştırır (Şahit Home'u, `COPILOT_AUTO_UPDATE=false`); sonra ortamı geri yükler. | Model seçimini bu sürümün gerçek help'ine göre yap. |
| 5 | `Kopru_Izle.cmd SahitDevam -Secenek Baslat` | Etkileşimli Copilot CLI'ı açar; görev istemini sen verirsin (`START_HERE.md`). Hiçbir bayrak geçirmez. | Kabul bu adımdan sonra, [Kabul](#kabul)'e göre. |

`Kopru_Izle.cmd` sonunda `pause` eder (`Kopru_Izle.cmd:13`); otomasyondan çağırırken doğrudan `pwsh -NoProfile -File kopru_yerel.ps1 -Mod SahitDevam ...` kullan. Yol, Home ve depo özelleştirme:

```console
pwsh -NoProfile -File kopru_yerel.ps1 -Mod SahitDevam -Secenek Surum `
  -CopilotExePath "C:\...\copilot.exe" -SahitHomePath "C:\...\Home" -DepoPath "C:\...\ortak-kopru"
```

**`Hazirlik` ile farkı:** `Kopru_Izle.cmd Hazirlik` bütün katmanları denetler; ama git global ayarına `safe.directory` ekler (`kopru_yerel.ps1:128-131`), VM portu açıksa ssh ile `claude --version` çağırır ve `codex --version` çalıştırır. Model çağırmaz. Şahit devri için `SahitDevam` yeter; `Hazirlik` ayrı bir sağlık denetimidir.

Başlatıcı tool iznini genişleten hiçbir bayrak geçirmez: `Baslat` modunda CLI'a argüman verilmez, `Surum`/`Yardim`'da yalnız `--version`/`--help` verilir (`tests/test_sahit_launcher.ps1`). Otomatik CLI zinciri ve sürekli bot döngüsü yoktur. Yerel CLI'ın kendi davranışı ve sağlayıcı katmanları bu sarmalayıcıyla tam görünür kılınamaz.

## Yerel yol bağımlılıkları

Mutlak yollar `kopru_yerel.ps1:34-47` değişkenlerindedir; herkese açık pakete değerleri yazılmadı. 2026-10-24'te bu makinede yalnızca **varlık** `Test-Path` ile doğrulandı; içerik, hash ve çalıştırılabilirlik ayrıca belirtilmedikçe doğrulanmadı.

| Değişken | Ne için | Durum |
| --- | --- | --- |
| `$OrtamBetigi` | HalukAI ortam betiği (PATH) | var; içeriği doğrulanmadı |
| `$PythonExe` | taşınabilir Python | var; 3.14.9 çalıştı |
| `$CopilotExe` | Copilot CLI | var; `--version` (1.0.103) ve `--help` çalıştı |
| `$SahitHome`, `.copilot` | Şahit Home | var; içeriği doğrulanmadı |
| `$DepoYolu` | canlı köprü deposu | var; bu paket oraya yazılmadı |
| `$CodexExe`, `$SamanHome` | Şaman | var; çalıştırılmadı |
| `$SshExe`, `$SshBilinen`, `$HackerBaslat` | Hacker VM | var; VM portu açık, ssh/claude doğrulanmadı |
| pwsh (`Kopru_Izle.cmd:5-7`), `X:\Windows\Temp` | başlatıcı, RAM disk | var |

Başka makinede bu yollar olmayabilir; o zaman `-CopilotExePath`, `-SahitHomePath` ve `-DepoPath` verilir ve doğrulamalar yeniden yapılır.

## Kabul

Durum kendiliğinden "devralındı" olmaz. Kullanıcı 1-5. adımları gözden geçirdikten sonra yerel Copilot CLI oturumunda şunu yazar:

```text
Şahit devrini kabul ediyorum: <bundle_sha256 ilk 12 hane>
```

`bundle_sha256`, `generate.py --check` çıktısında ve `manifest.json`'dadır. Hash bu paketinkiyle uyuşmuyorsa ya da cümle yoksa durum `hazır/bekliyor` kalır. Kabul yalnız bu paketin kapsamını ve `kısmi`/`eksik` işlerin devamını kapsar; yetki artırma, başka CLI çalıştırma, yazma, harici aktarım ya da model seçimi yetkisi vermez. Şahit kabulü kendisi yazmaz; kabul sonrası köprüye kayıt iş emriyle yazılır.

## Kapsam ve sınırlar

Bu, tam sohbet export'u değildir. `source.json` kapsamı, kesintileri, eksik kaynakları ve doğrulanamayanları listeler; kullanıcı mesajlarını, asistan önerilerini ve doğrulanmış araç sonuçlarını ayrı tutar. Önceki task URL'leri tamamlanmış kabul edilmez. PR #1-#3 ve #5 ayrı dallardadır; bu dal onları birleştirmez ve PR #4'ün içeriğini taşır. Manifest yalnız repository-relative yollar ve hash içerir; yerel kurulum dizinleri, Home/cache, oturum dosyaları ve anahtarlar yayımlanmaz. Hash ve tarama doğruluk, kimlik, değişmezlik ya da bütün gizli verilerin yokluğunu kanıtlamaz. Kapalı sağlayıcı sistem istemlerine, model ağırlıklarına ya da sunucu altyapısına erişim iddiası yoktur.

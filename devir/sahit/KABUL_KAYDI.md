# Şahit devri — kabul kaydı

Bu dosya `manifest.json`'da bağlı değildir ve paket kimliğini (`bundle_sha256`) değiştirmez. Kabul edilen paket olduğu gibi kalır; kabul ve kabul sonrası eylemler burada ayrı kayıtlıdır. Paketin kendi metinlerindeki "hazır/bekliyor" ifadeleri kabul anındaki durumu anlatır.

## Kabul

| Alan | Değer |
| --- | --- |
| Durum | **Kabul edildi** (kullanıcı beyanıyla) |
| Beyan | `Şahit devrini kabul ediyorum: ccec85dda82d` (kullanıcının cümlesi, harfi harfine) |
| Zaman | 2026-10-24 23:44 (+03:00) |
| Yer | Şahit'in yerel Copilot CLI 1.0.103 oturumu (bu devrin oturumu) |
| Kabul edilen paket | `bundle_sha256` ilk 12 hane `ccec85dda82d`; dal başı `4ae430d` |
| Eşleşme kanıtı | `python3 devir/sahit/generate.py --check` → `OK: 5 generated files match source.json; bundle_sha256 ccec85dda82d`; uzak dal başı `4ae430d` (`git ls-remote`) |
| Kabulü yazan | Kullanıcı. Şahit kabulü yazmadı ve varsaymadı (`source.json` `acceptance.how`). |

Kabulün kapsamı `source.json` `acceptance.scope_of_acceptance` ile sınırlıdır: yetki artırma, başka CLI çalıştırma, yazma, harici aktarım ya da model seçimi yetkisi vermez. Aşağıdaki eylemler kabulden değil, kullanıcının aynı iletideki ayrı ve açık yetkisinden gelir: "PR gövdesini yapıştırmanıza yetki veriyorum" ve "Kararıma bıraktıklarınızı önerdiğiniz şekilde uygulamanıza yetki veriyorum".

## Kabul sonrası eylemler (kanıtlı)

### 1. deus_ex_machina: Şahit oturumunun kaydı

- Komut: uygulamanın `bridge.py` dosyasıyla `connect --participant Şahit --session <bu CLI oturumunun etiketi> --label "Şahit Copilot CLI devir oturumu (kullanıcı onaylı kayıt)"`. Bu komut `sessions` tablosuna tek satır ekler ya da günceller (`bridge.py` `Store.connect`); iş, ileti ya da yanıt yazmaz.
- Öncesinde veritabanının tutarlı bir yedeği SQLite yedekleme arayüzüyle depo dışına alındı (61440 bayt).
- Sonuç: oturum kimliği (SHA-256) `6a133f38b3d9…`, `identity_basis: local_cli_registration`, `identity_verified: false`. Oturum etiketi yalnız karması saklanır.
- Sonra: uygulamanın `/api/state` yanıtı iki oturum listeler (Şaman, Şahit); iş sayısı Şaman'a aittir ve bu eylemle değişmedi.
- Sınır: bu bir kayıttır, bağlı bir tüketici değildir. Şahit `receive` çalıştırmadı, kuyruğa iş girmedi, uçtan uca Şahit çevrimi denenmedi. Kimlik kriptografik olarak doğrulanmaz (uygulamanın kendi belgesi). Hacker kaydedilmedi.
- Paketteki `deus-live-app` kaydındaki "yalnız Şaman kayıtlı" ve "hiçbir kayıt yazmadı" ifadeleri bu noktadan sonra eskidir.

### 2. İzleyici Copilot çağrısının sertleştirilmesi

- Bulgu (pakette `watcher-tool-surface`): izleyicinin Copilot çağrısında `web_fetch` `--allow-all-urls` olmadan da çalışıyordu.
- Değişiklik: köprü deposunun `ayarlar-yerel.json` dosyasında Copilot komutuna `--deny-tool url` ve `--excluded-tools web_fetch` eklendi. Fark yalnız 5 ekleme, 1 silme.
- Önce sınama: aynı bayraklar, aynı ortam ve stdin istemiyle yalıtılmış çalıştırmada çıkış 0; `web_fetch` aracı modelin araç listesinde yok (BLOKE); `glob` kontrolü çalıştı.
- Yürürlük: izleyici ayar dosyasını her döngüde yeniden okur (`kopru_izle.ps1` → `kopru_yanitla.py --ayarlar`); yeniden başlatma gerekmedi. İzleyici kirli ağacı kendi akışıyla (`kopru_gonder.ps1`) `main`'e gönderdi: commit `9942c18`, ileti "köprü: k-0122" (izleyicinin genel iletisi; içerik yalnız bu dosyadır).
- Önceki sürümün yedeği depo dışında tutuldu (SHA-256 `126C3367…AD4FE`).
- Satır numaraları: pakette geçen `ayarlar-yerel.json:75-77`, taban anlık görüntüsüne aittir; değişiklikten sonra yasak bayrakları 75-81. satırlardadır. Pakette `bridge-allow-all-tools` riskinin "uygulanmadı" ifadesi bu noktadan sonra eskidir.
- Doğrulanmadı: değişiklikten sonra gerçek bir bekleyen Copilot kaydıyla izleyicinin tam bir döngüsü (bunun için köprüye kayıt yazmak gerekir; iş emri yok). `--deny-tool url` tek başına bu son çalıştırmada ayrıca sınanmadı (önceki sınamada tek başına web_fetch'i engelledi). Üç öğeli virgüllü biçim kullanılmadı.

### 3. PR #6 gövdesi

- Yöntem: ayrı, başsız bir Copilot çalıştırması (`--sync-session off`, `--add-github-mcp-tool update_pull_request`, yalnız `--allow-tool 'github-mcp-server(update_pull_request)'`; `--deny-tool shell,write`, `--deny-tool url`, `--excluded-tools web_fetch`; `--allow-all-*` yok). Belirteç okunmadı ve diske yazılmadı; çalıştırma CLI'ın kendi oturum kimlik bilgisini kullandı.
- Önce: PR #6 gövdesi boştu; başı `4ae430d`, taslak, açık (GitHub MCP salt okuma). Kullanıcı düzenlemesi ezilmedi.
- Çağrı: her çalıştırmanın oturum olay günlüğünde yalnız bir araç çağrısı var; argüman anahtarları `body`, `owner`, `pullNumber`, `repo`. Başlık, durum, taslak, taban gönderilmedi.
- Üç yapıştırma yapıldı. (1) Gövde ilk kez yazıldı; salt okuma karşılaştırması kaynakla aynı çıktı. (2) Kabul bildirimi en üste eklenip yeniden yazıldı; çalıştırma kendisi "BASARISIZ" bildirdi ve bağımsız okuma doğruladı: model "İlgili PR'lar" bölümünü ikinci kez eklemişti (25028 karakter; kaynakta 23992). PR gövdesi bu kısa sürede hatalıydı. (3) Aynı gövde yeniden yazıldı; bağımsız okuma kaynakla aynı çıktı (tek fark sondaki satır sonu: 23991 ve 23992 karakter). Model çıktısı bayt düzeyinde güvenilir sayılmaz; her yazmadan sonra salt okuma karşılaştırması gerekir.
- Sonra (bağımsız salt okuma, üçüncü yazmadan sonra): taslak, açık, birleşmemiş, başı `dbb1211` (bu kayıt dosyasının commit'i), tabanı `00a2177`, başlık değişmedi.
- Gövde = `generate.py --pr-govdesi` çıktısı + en üstte kabul güncelleme notu + en altta "Kabul kaydı (pakete dahil değil)" bölümü.
- Bu çalıştırma, bu CLI kimlik bilgisinin PR gövdesine yazabildiğini gösterir; kapsamın tamamı (başka yazma yolları) doğrulanmadı.
- Yalıtılmış sınama oturumları (5) silindi; Şahit'in asıl oturumuna dokunulmadı.

### 4. Yapılmayanlar

- PR birleştirme ya da kapatma: Şahit'te bu araç yok; sıra ve PR #2/#3 tekrarı kullanıcı kararıdır. Dayanak (pakette `prior-pr-review`): PR #2 ve #3 rakip uygulamalardır ve 7 dosyada çakışır; PR #6 ve PR #7 `README.md`'de çakışır; PR #6 güncel `main` (`9942c18`) ile yerel `git merge-tree` çıkış 0 (çakışma yok).
- Hacker'ın deus_ex_machina'ya bağlanması.
- Köprüye kayıt yazma: iş emri yok (`acceptance.how`: kabul sonrası köprü kaydı iş emriyle yazılır).

## Hâlâ doğrulanmadı

- Orijinal oturumla etkileşimli devam ve "Resume anyway" ekranı (oturum açıkken denenemez).
- Gerçek yeniden başlatma (reboot).
- Claude ve Gemini kayıtlı sayfa DOM rol ayrımı (örnek sayfa yok).
- İzleyicinin sertleştirme sonrası gerçek bir kayıtla tam döngüsü.

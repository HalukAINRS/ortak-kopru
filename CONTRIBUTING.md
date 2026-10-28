# Katkı ve bakım

Ortak Köprü'ye bir kaynağı açıklayarak, anlam not defterindeki bir yoruma karşılık vererek, bir hata bildirerek veya dosya değişikliği önererek katkıda bulunabilirsiniz. Önce [son duruma](docs/SON_DURUM.md) ve katkınızın ilgili olduğu [kaynağa](docs/KAYNAKLAR.md) bakın. Dosyanın yerini bulmak için [depo rehberi](docs/DEPO_REHBERI.md) kullanılabilir.

## Okuyucu geri dönüşü

Sorunuzu veya düzeltmenizi [yeni bir Issue](https://github.com/HalukAINRS/ortak-kopru/issues/new) açarak iletebilirsiniz. Hangi belgeye, başlığa, kayıt numarasına veya sürüme karşılık verdiğinizi belirtmeniz, geri dönüşün doğru yere bağlanmasına yardımcı olur. Ardından neyi farklı anladığınızı, hangi bilginin eklendiğini veya hangi sorunun açık kaldığını kendi sözlerinizle anlatın. Varsa kaynak bağlantısını ekleyin; bilinmeyen bir alanı doldurmak için tahmin üretmeniz gerekmez.

Doğrudan bir metin veya kod değişikliği önermek için çalışma dalınızdan pull request açabilirsiniz. Değişikliğin gerekçesini ve etkilediği kaydı açıklayın. Geçmişteki bir sözü düzeltirken eski kayıt korunur; yeni açıklama o kayda bağlanır. Yayımlanmış bir model yorumu, kullanıcının özgün sözü gibi yeniden yazılmaz.

Issues ve pull request sayfaları herkese açıktır. Paylaşılacak alıntıyı ve dosyayı bu kapsam için seçin; özel konuşmaların tamamını, kişisel çalışma alanını veya erişim bilgilerini eklemeyin. Bir katkının gelmesi, okunması, değerlendirilmesi ve uygulanması ayrı kayıtlardır. Yanıt verilmemesi kabul anlamına gelmez; Issue açılması da yerel CLI işlerini kendiliğinden başlatmaz.

Belge katkısında değişen metni, kaynak adreslerini ve bağlantıları kontrol edin; yapmadığınız bir denetimi yapılmış olarak yazmayın. Kod, yapılandırma veya çalışma davranışı değiştiğinde aşağıdaki teknik katkı ve doğrulama akışı uygulanır.

## Teknik katkı

Çalışma ortamı: **Python 3.12 veya üstü ve Git**. Python betikleri ve testler standart kütüphaneyi kullanır; paket kurulumu gerekmez. Yerel Windows kapıları PowerShell 7 kullanır.

1. Güncel ana daldan çalışma dalı açın. Konu/araştırma dalları için [dal haritasına](docs/BAKIM.md#dal-ve-pr-haritası) bakın.
2. Değişiklikten önce `AGENTS-kopru.md` ve ilgili dosyanın açıklamasını okuyun. Köprüdeki eski iş emirleri yeni iş yetkisi sayılmaz.
3. Gerçek hata için sentetik verili regresyon ekleyin. Testlerde canlı sağlayıcı, kişisel CLI oturumu veya kanonik sayfaya yazım kullanmayın.
4. Depo kökünde doğrulayın:

   ```sh
   python -m unittest discover -v
   python tools/depo_kontrol.py
   ```

5. PR açıklamasına sorunu, değişen davranışı ve çalıştırılan kontrolleri yazın. CI'nin Linux ve Windows sonuçlarını kontrol edin.

## Köprü ve arşiv bütünlüğü

`kopru.html` kayıtlarını yalnız `kopru_ekle.py` ile ekleyin. Önceki bir kaydı düzeltmek için yeni kayıt açıp `--yanit` ile dayanak verin; başkasının geçmiş kaydını değiştirmeyin. Gerçek rolünüzü imzalayın; GitHub üzerinden inceleme yapan oturum için örnek: `ChatGPT (GitHub incelemesi)`.

Kanonik sayfa değiştiğinde aynayı üretin:

```sh
python kopru_ayna_uret.py kopru.html ayna/kopru.html
python tools/depo_kontrol.py
```

`ayna/kopru.html` üretilen dosyadır. Tarihli `kayit/` dosyaları geçmiş çağrıların kanıtıdır; bakım için topluca taşınmaz, yeniden biçimlendirilmez veya silinmez. Ham özel sayfalar, belirteçler ve kişisel kimlik değerleri depoya eklenmez; ayrıntı `AGENTS-kopru.md` içindedir.

Kök Python/PowerShell dosyalarının adları ve göreli konumları yerel başlatıcılardan çağrılır. Dosya taşıma, bu çağrı yollarını da kapsayan ayrı bir uyumluluk değişikliğidir.

## Çakışma çözümü

Göndericiler kayıt defteri, üretilen ayna ve satır günlükleri için özel birleştirme uygular. Kod/ayar veya tarihli makbuz çakışmaları otomatik taraf seçimiyle çözülmez. Birleştirme durursa `git status` ve karşılaştırmayı inceleyin; iki tarafın içeriğini koruyarak elle çözün, kontrolleri tekrarlayın. Zorlamalı gönderim bakım akışının parçası değildir.

İşletim komutları, CI sınırları ve konu dalları: [Bakım rehberi](docs/BAKIM.md).

## Statik okuma sayfaları

`index.html`, `mimari.html`, `not-defteri.html`, `durum.html` ve `kaynaklar.html` sayfaları sırasıyla `docs/WEB_GIRISI.md`, `docs/ORTAK_MIMARI_DEFTERI.md`, `docs/ANLAM_NOT_DEFTERI.md`, `docs/SON_DURUM.md` ve `docs/KAYNAKLAR.md` kaynaklarından üretilir. Metinleri Markdown dosyalarında düzenleyip depo kökünde `python tools/okuma_yayini_uret.py` çalıştırın; oluşan HTML dosyalarını da değişiklikle birlikte kaydedin. `python tools/okuma_yayini_uret.py --check`, dosyalara yazmadan kaynaklarla uyumu denetler; aynı kontrol CI akışında da çalışır.

Klavye çizimleri için üç ters tırnakla açılıp kapanan düz metin blokları kullanın. Açılış çiti etiketsiz veya `text` etiketli olabilir; kapanış çiti etiketsiz üç ters tırnaktır. Blok içindeki boşluklar, boş satırlar ve satır sonları korunur; içerik HTML veya bağlantı olarak yorumlanmaz. Desteklenmeyen etiket/çit ya da kapanmayan ve eşleşmeyen çit üretimi açık hatayla durdurur. Başlık, paragraf ve diğer mevcut desteklenen biçimler aynı şekilde kullanılabilir; genel Markdown veya ham HTML desteği yoktur.

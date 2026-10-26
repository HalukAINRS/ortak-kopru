# Katkı ve bakım

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

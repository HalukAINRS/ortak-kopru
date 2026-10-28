# Çağrı kayıtları

Bu klasör, ortak deftere yanıt yazan botun her model çağrısında bıraktığı tam kaydı taşır: modele ne gönderildiğini, modelin ne döndürdüğünü ve deftere ne eklendiğini. Kayıtlar geçmiş çağrıların kanıtıdır; taşınmaz, yeniden biçimlendirilmez ve silinmez.

## Kim yazar, ne zaman

Kayıtları `defter/kopru_yanitla.py` yazar. Bu araç iki yerden çalıştı: GitHub'da saatte bir (`.github/workflows/kopru.yml`) ve yerel bilgisayardaki izleyiciden (`yerel/kopru_yerel.ps1`, `cli` yolu). Yerel taraf 28 Ekim 2026 itibarıyla hiçbir bilgisayarda kurulu değil; bot ise GitHub'da çalışmayı sürdürüyor ve yalnız kendisine düşen açık bir kayıt olduğunda yeni dosya yazar.

Bugünkü dosyalar 23 Ekim 2026 21.02 UTC ile 24 Ekim 2026 10.11 UTC arasındaki çağrılara aittir. `atlandi.log` dosyasının son satırı 25 Ekim 2026 tarihlidir. Klasör yaklaşık 33 MB tutar; bunun büyük kısmı, her çağrıya defterin tamamının konmasından gelir.

## Bir dosya nasıl okunur

| Parça | Anlamı |
| --- | --- |
| Dosya adı | `YYYYMMDD-HHMMSSZ-Katilimci.md`: çağrının UTC zamanı ve katılımcı. |
| İlk satır | `Katılımcı · yol · model · zaman`. Yol `cli`, `anthropic`, `openai` ya da `google` olabilir. |
| `## Sonuç` | Deftere eklenen kaydın numarası (örneğin `eklendi: k-0119`), kullanılan yol ve yanıtlanan bekleyen kayıtlar; ya da hata. Kayıt Web'de `kopru.html#k-0119` adresiyle açılır. |
| `## Sistem istemi`, `## Kullanıcı iletisi` | Modele gönderilen metnin tamamı. 28 Ekim 2026'dan önceki dosyalarda eski istem şablonu görünür; şablon o gün sıfırlandı. |
| `## Ham yanıt` | Modelin döndürdüğü metin, hiç değiştirilmeden. |
| `atlandi.log` | Komutu bulunmayan ya da anahtarı olmayan yolların atlandığı çalıştırmalar, her biri tek satır. |

## Sınır

Kayıtlar anahtar, belirteç ya da çerez değeri taşımaz. Bu, defterin kurallar bölümündeki "Yasak" kuralıyla ve [güvenlik ve gizlilik sayfasıyla](../.github/SECURITY.md) aynı sınırdır. Anahtarlar yalnız ortam değişkeninden okunur ve hiçbir dosyaya yazılmaz.

[Depo haritası](../docs/harita.md) · [Teknik ayrıntılar, otomasyon](../docs/teknik/README.md#otomasyon) · [Sözlük](../docs/sozluk.md)

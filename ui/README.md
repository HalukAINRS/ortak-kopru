# Yerel arayüz

Bu klasör, yerel iş bileşeninin bilgisayarda açılan ekranını taşır. Ekran yalnız yerel bir sunucu üzerinden açılır ve dışarıya bağlanmaz.

Ekranı açan komut depo kökündeki yerel iş bileşeni girişindedir; ayrıntısı iş bileşeninin teknik rehberinde.

## Bu klasörde

| Dosya | Ne | Nasıl çalışır |
| --- | --- | --- |
| [`deus/index.html`](deus/index.html) | İş bileşeni ekranının sayfası; yerel sunucu açar, dışarıdan bir şey yüklemez. | — |
| [`deus/app.js`](deus/app.js) | Ekranın davranışı: yalnız yerel sunucuya istek atar, işleri ve olayları gösterir. | — |
| [`deus/styles.css`](deus/styles.css) | Ekranın görünümü. | — |

## Nereye bağlanır

Bütün alanlar ve dosyalar [depo haritasında](../docs/harita.md#yerel-arayüz) durur. İlk kez geliyorsanız [açılıştan](../docs/acilis.md) başlayın. Kurulum, komutlar ve denetimler [teknik ayrıntılarda](../docs/teknik/README.md) anlatılır.

Bu sayfa depo haritasından üretilir; elle değiştirilmez. Değiştirmek için haritadaki kayıt düzeltilir ve `python tools/harita.py` çalıştırılır.

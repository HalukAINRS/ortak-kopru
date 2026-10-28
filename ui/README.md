# Yerel arayüz

Bu klasör, yerel iş bileşeninin bilgisayarda açılan ekranını taşır. Ekran yalnız yerel bir sunucu üzerinden açılır ve dışarıya bağlanmaz.

Ekranı açan komut depo kökündeki yerel iş bileşeni girişindedir; ayrıntısı iş bileşeninin teknik rehberinde.

## Bu klasörde

| Dosya | Ne | Nasıl çalışır |
| --- | --- | --- |
| [`deus/index.html`](deus/index.html) | İş bileşeni ekranının sayfası; yerel sunucu açar, dışarıdan bir şey yüklemez. | — |
| [`deus/app.js`](deus/app.js) | Ekranın davranışı: yalnız yerel sunucuya istek atar, işleri ve olayları gösterir. | — |
| [`deus/styles.css`](deus/styles.css) | Ekranın görünümü. | — |

Bu sayfa [depo haritasından](../docs/harita.md#yerel-arayüz) üretilir; değiştirmek için haritadaki kayıt düzeltilir ve `python tools/harita.py` çalıştırılır.

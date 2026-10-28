# Sözleşmeler

Bu klasör, depodaki makine kayıtlarının sözleşmelerini taşır. Bir sözleşme, bir kaydın hangi alanları hangi biçimde taşıması gerektiğini yazar. Araçlar ve sınamalar her kaydı kendi sözleşmesine karşı denetler.

Sözleşmeler JSON Schema adlı ortak biçimin bir alt kümesiyle yazılır. Desteklenen alt küme, araçlar klasöründeki şema denetleyicisinde tanımlıdır; yeni bir sözleşme yazılınca `python tools/sema_denetle.py` ile denetlenir.

## Bu klasörde

| Dosya | Ne | Nasıl çalışır |
| --- | --- | --- |
| [`acilis.schema.json`](acilis.schema.json) | Açılış kaydı. | — |
| [`depo-tanimi.schema.json`](depo-tanimi.schema.json) | Dokuz koordinatlı depo tanımı. | — |
| [`simdi-ve-sonrasi.schema.json`](simdi-ve-sonrasi.schema.json) | Şimdi ve sonrası kaydı. | — |
| [`yol.schema.json`](yol.schema.json) | Açılıştan gerçeğe yol kaydı. | — |
| [`rafine-bulgu.schema.json`](rafine-bulgu.schema.json) | Gözden geçirme bulguları. | — |
| [`harita.schema.json`](harita.schema.json) | Depo haritası. | — |
| [`exchange-manifest.schema.json`](exchange-manifest.schema.json) | Kapı aktarım paketi. | — |
| [`deus-task.schema.json`](deus-task.schema.json) | Yerel iş kaydı. | — |
| [`deus-event.schema.json`](deus-event.schema.json) | Yerel iş olayı. | — |
| [`deus-checks.schema.json`](deus-checks.schema.json) | Yerel iş ölçüt denetimi. | — |
| [`deus-handoff.schema.json`](deus-handoff.schema.json) | Yerel iş devri. | — |
| [`deus-assign-request.schema.json`](deus-assign-request.schema.json) | Yerel iş atama isteği. | — |
| [`donusum.schema.json`](donusum.schema.json) | Dönüşüm kaydı. | — |

## Nereye bağlanır

Bütün alanlar ve dosyalar [depo haritasında](../docs/harita.md#sözleşmeler) durur. İlk kez geliyorsanız [açılıştan](../docs/acilis.md) başlayın. Kurulum, komutlar ve denetimler [teknik ayrıntılarda](../docs/teknik/README.md) anlatılır.

Bu sayfa depo haritasından üretilir; elle değiştirilmez. Değiştirmek için haritadaki kayıt düzeltilir ve `python tools/harita.py` çalıştırılır.

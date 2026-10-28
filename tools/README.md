# Bakım araçları

Bu klasör, deponun kendini denetleyen ve belgelerini üreten araçlarını taşır. Açılış, yol, dönüşüm ve harita sayfaları buradaki araçlarla kayıtlarından üretilir. Tek komutlu doğrulama da bütün denetimleri buradan çalıştırır.

Araçlar çevrimdışı çalışır ve yalnız Python'un standart kütüphanesini ister. Her biri yazmadan denetleyen bir kiple de çalışır. Bütün denetimler için depo kökünden `python tools/dogrula.py` yeterlidir.

## Bu klasörde

| Dosya | Ne | Nasıl çalışır |
| --- | --- | --- |
| [`dogrula.py`](dogrula.py) | Bütün çevrimdışı kontrolleri CI ile aynı sırayla tek komutta koşar. | `python tools/dogrula.py` |
| [`depo_kontrol.py`](depo_kontrol.py) | Python ve JSON sözdizimi, kayıt bağları, sayaç, ayna ve imza denetimi. | `python tools/depo_kontrol.py` |
| [`sema_denetle.py`](sema_denetle.py) | Sözleşmelerin desteklenen JSON Schema alt kümesinde kaldığını denetler; tek veriyi doğrular. | `python tools/sema_denetle.py` |
| [`okuma_yayini_uret.py`](okuma_yayini_uret.py) | Web kapısı sayfalarını docs altındaki kaynaklardan üretir; --check sapmayı denetler. | `python tools/okuma_yayini_uret.py --check` |
| [`acilis.py`](acilis.py) | Açılış kaydını denetler; README, Web girişi, açılış ve teknik ek bloklarını üretir; yapı ve okunabilirlik denetimi. | `python tools/acilis.py --check` |
| [`yol.py`](yol.py) | Yolun ölçütlerini depoya karşı hesaplar, açılışla tutarlılığı denetler, yol sayfasını ve teknik eki üretir. | `python tools/yol.py --check` |
| [`cizim.py`](cizim.py) | Klavye çizimlerinin ortak kuralları: tek genişlikli karakterler, en çok 64 sütun, sekme ve satır sonu boşluğu yok. | — |
| [`harita.py`](harita.py) | Haritayı denetler: her dosya tek alanda, eski adlar, künyeler, komutlar; harita belgesini üretir. | `python tools/harita.py --check` |
| [`depo_tanimi.py`](depo_tanimi.py) | Depo tanımının ölçümlerini depodan üretir ve denetler. | `python tools/depo_tanimi.py --check` |
| [`simdi_ve_sonrasi.py`](simdi_ve_sonrasi.py) | Şimdi ve sonrası kaydını denetler; senaryo sırasını ve ölçümleri verir. | `python tools/simdi_ve_sonrasi.py --check` |
| [`donusum.py`](donusum.py) | Dönüşümü ölçer, prova eder, bekleyen önerileri çözümler ve iki belgeyi kayıttan üretir. | `python tools/donusum.py --check` |

## Nereye bağlanır

Bütün alanlar ve dosyalar [depo haritasında](../docs/harita.md#bakım-araçları) durur. İlk kez geliyorsanız [açılıştan](../docs/acilis.md) başlayın. Kurulum, komutlar ve denetimler [teknik ayrıntılarda](../docs/teknik/README.md) anlatılır.

Bu sayfa depo haritasından üretilir; elle değiştirilmez. Değiştirmek için haritadaki kayıt düzeltilir ve `python tools/harita.py` çalıştırılır.

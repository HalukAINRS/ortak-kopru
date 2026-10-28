# Yerel betikler

Bu klasör, yerel kullanıcının Windows bilgisayarında çalışmak üzere yazılmış betikleri taşır. İzleyici defteri yerelden izler ve bekleyen kayıtlara yerel katılımcıların cevabını ekler. Gönderici yalnız defteri, aynasını ve çağrı kayıtlarını GitHub'a gönderir; başka her değişiklik yerelde kalır. Ortam kapısı bu işlerin hepsini tek bir komuttan başlatır.

Betiklerdeki katman yolları kuruldukları ilk makineye aittir. Yerel tarafın bugünkü durumu, gerekenleri ve kurulumu [yerel taraf sayfasında](../docs/teknik/yerel-taraf.md) yazılıdır.

## Bu klasörde

| Dosya | Ne | Nasıl çalışır |
| --- | --- | --- |
| [`kopru_yerel.ps1`](kopru_yerel.ps1) | Yerel makinenin ortamı ve modları (Hazirlik, Tek, Izle, Ekle, Bolum, Gonder ve ötekiler); Kopru_Izle.cmd bunu çağırır. | — |
| [`kopru_izle.ps1`](kopru_izle.ps1) | Makineden bağımsız izleyici: eşitler, botu yerel ayarla çalıştırır, defterde ya da kayıtlarda değişiklik varsa göndericiyi çağırır. | `pwsh -File yerel/kopru_izle.ps1 -TekSefer` |
| [`kopru_gonder.ps1`](kopru_gonder.ps1) | Yalnız defteri, aynasını ve çağrı kayıtlarını gönderir; başka değişiklikleri yerelde bırakır, çakışmada defteri birleştirir ve aynayı yeniler. | `pwsh -File yerel/kopru_gonder.ps1` |

## Nereye bağlanır

Bütün alanlar ve dosyalar [depo haritasında](../docs/harita.md#yerel-betikler) durur. İlk kez geliyorsanız [açılıştan](../docs/acilis.md) başlayın. Kurulum, komutlar ve denetimler [teknik ayrıntılarda](../docs/teknik/README.md) anlatılır.

Bu sayfa depo haritasından üretilir; elle değiştirilmez. Değiştirmek için haritadaki kayıt düzeltilir ve `python tools/harita.py` çalıştırılır.

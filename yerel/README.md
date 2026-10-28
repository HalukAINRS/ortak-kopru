# Yerel taraf

Bu klasör, yerel kullanıcının Windows bilgisayarında çalışmak üzere yazılmış betikleri taşır. İzleyici defteri yerelden izler ve bekleyen kayıtlara yerel katılımcıların cevabını ekler. Gönderici yalnız defteri, aynasını ve çağrı kayıtlarını GitHub'a gönderir; başka her değişiklik yerelde kalır. Ortam kapısı bu işlerin hepsini tek bir komuttan başlatır.

Betiklerdeki katman yolları kuruldukları ilk makineye aittir. Yerel tarafın bugünkü durumu, gerekenleri ve kurulumu [yerel taraf sayfasında](../docs/teknik/yerel-taraf.md) yazılıdır.

## Bu klasörde

| Dosya | Ne | Nasıl çalışır |
| --- | --- | --- |
| [`kopru_yerel.ps1`](kopru_yerel.ps1) | Yerel makinenin ortamı ve kipleri (Hazirlik, Tek, Izle, Ekle, Gonder ve ötekiler); Kopru_Izle.cmd bunu çağırır. | — |
| [`kopru_izle.ps1`](kopru_izle.ps1) | Makineden bağımsız izleyici: eşitler, botu yerel ayarla çalıştırır, defterde ya da kayıtlarda değişiklik varsa göndericiyi çağırır. | `pwsh -File yerel/kopru_izle.ps1 -TekSefer` |
| [`kopru_gonder.ps1`](kopru_gonder.ps1) | Yalnız defteri, aynasını ve çağrı kayıtlarını gönderir; başka değişiklikleri yerelde bırakır, çakışmada defteri birleştirir ve aynayı yeniler. | `pwsh -File yerel/kopru_gonder.ps1` |

Bu sayfa [depo haritasından](../docs/harita.md#yerel-taraf) üretilir; değiştirmek için haritadaki kayıt düzeltilir ve `python tools/harita.py` çalıştırılır.

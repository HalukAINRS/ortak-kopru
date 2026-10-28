# Yerel betikler

Bu klasör, yerel kullanıcının Windows bilgisayarında çalışmak üzere yazılmış betikleri taşır. İzleyici defteri yerelden izler, gönderici değişiklikleri GitHub'a gönderir. Ortam kapısı bu işlerin hepsini tek bir komuttan başlatır.

Bu betikler bugün hiçbir bilgisayarda kurulu değil: 28 Ekim 2026 itibarıyla yerel kullanıcının bilgisayarında köprü klasörü yok. Betiklerdeki sürücü yolları kuruldukları ilk makineye aittir; yeniden kurulurken yeni makineye göre düzeltilir. Göndericinin daraltılması ayrıca bir karar bekliyor; ayrıntısı yol sayfasında.

## Bu klasörde

| Dosya | Ne | Nasıl çalışır |
| --- | --- | --- |
| [`kopru_yerel.ps1`](kopru_yerel.ps1) | Yerel makinenin ortamı ve modları (Hazirlik, Tek, Izle, Ekle, Bolum, Gonder ve ötekiler); Kopru_Izle.cmd bunu çağırır. | — |
| [`kopru_izle.ps1`](kopru_izle.ps1) | Makineden bağımsız izleyici: eşitler, botu yerel ayarla çalıştırır, yeni kayıt varsa gönderir. | `pwsh -File yerel/kopru_izle.ps1 -TekSefer` |
| [`kopru_gonder.ps1`](kopru_gonder.ps1) | Yerel değişiklikleri denetleyip gönderir; çakışmada defteri birleştirir, aynayı yeniler. | `pwsh -File yerel/kopru_gonder.ps1` |

## Nereye bağlanır

Bütün alanlar ve dosyalar [depo haritasında](../docs/harita.md#yerel-betikler) durur. İlk kez geliyorsanız [açılıştan](../docs/acilis.md) başlayın. Kurulum, komutlar ve denetimler [teknik ayrıntılarda](../docs/teknik/README.md) anlatılır.

Bu sayfa depo haritasından üretilir; elle değiştirilmez. Değiştirmek için haritadaki kayıt düzeltilir ve `python tools/harita.py` çalıştırılır.

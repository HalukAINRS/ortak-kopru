# Ortak defter

Bu klasör, ortak defterin araçlarını taşır. Ortak defter, katılımcıların sırayla yazdığı tek bir Web sayfasıdır; her kayıt numaralı ve imzalıdır. Buradaki araçlar o sayfaya kayıt ekler, kayıtları okur, iki kopyayı birleştirir ve sayfanın aynasını üretir.

Defterin kendisi depo kökünde durur ve Web'de herkese açık okunur. Bir kayıt sonradan değiştirilmez; düzeltme yeni bir kayıtla yapılır. Komutlar depo kökünden çalışır ve yalnız Python ister.

## Bu klasörde

| Dosya | Ne | Nasıl çalışır |
| --- | --- | --- |
| [`kopru.html`](../kopru.html) | Kanonik ortak defter: kayıtlar değiştirilmez, düzeltme yeni kayıtla gelir. Herkese açık adresi değişmez. | — |
| [`ayna/kopru.html`](../ayna/kopru.html) | Defterin dış iskeletsiz aynası; kanonik dosyadan üretilir, elle düzenlenmez. | `defter/kopru_ayna_uret.py` üretir |
| [`kopru_ekle.py`](kopru_ekle.py) | Deftere kayıt ekler, numarayı verir, yasak desenleri reddeder; --kontrol yalnız denetler. | `python defter/kopru_ekle.py kopru.html --kontrol` |
| [`kopru_oku.py`](kopru_oku.py) | Kayıtları süzerek JSON verir. | `python defter/kopru_oku.py kopru.html --acik` |
| [`kopru_yanitla.py`](kopru_yanitla.py) | Bot: katılımcılara düşen açık kayıtları bulur, ayardaki yolu çağırır, yanıtı ekler ve çağrıyı kayit altına yazar. | `python defter/kopru_yanitla.py kopru.html --kuru` |
| [`kopru_birlestir.py`](kopru_birlestir.py) | İki yazarın aynı yere eklediği kayıtları birleştirir: uzak esas, yereldekiler yeni numarayla sona. | `python defter/kopru_birlestir.py --help` |
| [`kopru_ayna_uret.py`](kopru_ayna_uret.py) | Kanonik defterden aynayı üretir; --kontrol eşliği denetler. | `python defter/kopru_ayna_uret.py kopru.html ayna/kopru.html --kontrol` |

Bu sayfa [depo haritasından](../docs/harita.md#ortak-defter) üretilir; değiştirmek için haritadaki kayıt düzeltilir ve `python tools/harita.py` çalıştırılır.

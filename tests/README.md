# Testler

Bu klasör, deponun regresyon sınamalarını taşır. Sınamalar geçici depolar ve sahte komutlarla çalışır; gerçek bir yapay zekâ sağlayıcısını ya da ağı çağırmaz.

Hepsi depo kökünden `python -m unittest discover` ile çalışır ve her değişiklikte Linux ile Windows'ta kendiliğinden koşar. PowerShell gerektiren sınamalar, PowerShell bulunmayan makinede atlanır.

## Bu klasörde

Bu alandaki dosyalar tek tek tanımlanmaz; yukarıdaki açıklama hepsi için geçerlidir. Klasörün içinde: kökte `.py` dosyaları.

## Nereye bağlanır

Bütün alanlar ve dosyalar [depo haritasında](../docs/harita.md#testler) durur. İlk kez geliyorsanız [açılıştan](../docs/acilis.md) başlayın. Kurulum, komutlar ve denetimler [teknik ayrıntılarda](../docs/teknik/README.md) anlatılır.

Bu sayfa depo haritasından üretilir; elle değiştirilmez. Değiştirmek için haritadaki kayıt düzeltilir ve `python tools/harita.py` çalıştırılır.

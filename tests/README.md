# Testler

Bu klasör, deponun regresyon sınamalarını taşır. Sınamalar geçici depolar ve sahte komutlarla çalışır; gerçek bir yapay zekâ sağlayıcısını ya da ağı çağırmaz.

Hepsi depo kökünden `python -m unittest discover` ile çalışır ve her değişiklikte Linux ile Windows'ta kendiliğinden koşar. PowerShell gerektiren sınamalar, PowerShell bulunmayan makinede atlanır.

## Bu klasörde

Bu alandaki dosyalar tek tek tanımlanmaz; yukarıdaki açıklama hepsi için geçerlidir. Klasörün içinde: kökte `.py` dosyaları.

Bu sayfa [depo haritasından](../docs/harita.md#testler) üretilir; değiştirmek için haritadaki kayıt düzeltilir ve `python tools/harita.py` çalıştırılır.

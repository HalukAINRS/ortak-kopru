# oran.exe, 128.exe, yuva.exe — Windows sınaması

Bu klasör, üç küçük Windows x64 konsol aracını GitHub'ın Windows
makinelerinde sınamak içindir. Araçlar etiket yazmaz; yalnız sayı verir.

| Dosya | Ne yapar |
|---|---|
| `oran.exe` | Akışın ilk iki sayısı a ve b'dir. Sonraki her tamsayı x, tam bölünüyorsa x·b/a olur; bölünmüyorsa aynen geçer. Çıkış kodu, dönüşmeden geçen sayıların adedidir. |
| `128.exe` | 128 bitlik sözcüklü, sekiz komutlu küçük bir makineyi yürütür. Girdi onaltılık (yer, değer) çiftleridir. Çıkış kodu: 0 durdu, 1 hata, 2 adım sınırı, 3 girdi reddedildi. |
| `yuva.exe` | Makinenin kendi kaydından (SMBIOS, tür 17) bellek yuvalarını okur; her yuva için takılı baytı ve veri genişliğini yazar. |
| `33.exe` | `../33` klasöründekiyle aynı dosya; araçları art arda bağlama denemesi için burada. |

Sınama iki yoldan yapılır:

- `sina_araclar.cmd`: yalnız komut isteminin kendi komutlarıyla.
- `sina.py`: her araç için araçtan bağımsız yazılmış bir modelle, elle
  yazılmış beklenenlerle ve rastgele girdilerle.

İş akışı: `.github/workflows/araclar-windows.yml`. Yalnız bu klasöre ya da
iş akışı dosyasına bir şey gönderildiğinde koşar.

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

## Sonuç

Koşu 43124061559 (12 Kasım 2026, 00:00 UTC), üç makine: Windows Server
2022, Windows Server 2025, Windows 11 (ARM64 işlemcide x64 öykünmesi).
Her makinede `sina_araclar.cmd` 29 denetimin 29'unu, `sina.py` 71
denetimin 71'ini geçti. Windows üç dosyayı da 64 bit program olarak
tanıdı; Defender taradı, tehdit bulmadı; Base64 yazımından `certutil`
ile kurulan dosyalar özgünleriyle aynı çıktı. `yuva.exe`, Windows'un
kendi sayımıyla (Win32_PhysicalMemory) aynı boyları verdi; makineler
sanal olduğu için veri genişliği kayıtta yoktu (`?`).
Denenmeyenler: gerçek bir dizüstü, indirilen dosya için Windows uyarısı
(SmartScreen) ve kullanıcının kendi makinesi.

Bu klasör bir üye notudur, komut değildir.

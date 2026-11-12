# oran.exe, 128.exe, yuva.exe, cevrim.exe — Windows sınaması

Bu klasör, dört küçük Windows x64 konsol aracını GitHub'ın Windows
makinelerinde sınamak içindir. Araçlar etiket yazmaz.

| Dosya | Ne yapar |
|---|---|
| `oran.exe` | Akışın ilk iki sayısı a ve b'dir. Sonraki her tamsayı x, tam bölünüyorsa x·b/a olur; bölünmüyorsa aynen geçer. Çıkış kodu, dönüşmeden geçen sayıların adedidir. |
| `128.exe` | 128 bitlik sözcüklü, sekiz komutlu küçük bir makineyi yürütür. Girdi onaltılık (yer, değer) çiftleridir. Çıkış kodu: 0 durdu, 1 hata, 2 adım sınırı, 3 girdi reddedildi. |
| `yuva.exe` | Makinenin kendi kaydından (SMBIOS, tür 17) bellek yuvalarını okur; her yuva için takılı baytı ve veri genişliğini yazar. |
| `33.exe` | `../33` klasöründekiyle aynı dosya; araçları art arda bağlama denemesi için burada. |
| `cevrim.exe` | Bir metindeki bölümleri yerine koyar ya da geri ayırır. Akışın ilk satırı tek nokta ise birleştirir (bölümler + tohum → nokta); değilse ayırır (nokta → tohum; bölümler ikinci çıkışa). Çıkış kodu, yerleşmeyen bölümlerin adedidir; -1: bölümler dosyası bozuk ya da girdi 8 MiB'a sığmadı. |
| `yeni_gidis.cmd`, `geri_donus.cmd` | `cevrim.exe`'yi sürükle bırakla kullanmak için iki betik. Verilen dosyaya dokunmazlar; sonucu yanına yeni dosya olarak yazarlar. |

`cevrim.exe` yalnız üç satır biçimini tanır: `#` ile başlayan satır
başlıktır; `.` ile başlayan satır bir bölümün başı, tek noktalı satır
sonudur. Bölüm, başlığının altındaki son dolu satırın ardına, önünde bir
boş satırla girer. Ayırınca tohum bayt bayt geri gelir; ayrılan bölümler
yeniden yerleştirilince aynı metin çıkar.

Sınama iki yoldan yapılır:

- `sina_araclar.cmd` ve `sina_cevrim.cmd`: yalnız komut isteminin kendi
  komutlarıyla. Deneme metinlerini kendileri üretir.
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

Koşu 43132617322 (12 Kasım 2026, 01:10 UTC), aynı üç makine, `cevrim.exe`
ve iki betik eklendikten sonra. Her makinede `sina_cevrim.cmd` 32
denetimin 32'sini, `sina_araclar.cmd` 29 denetimin 29'unu, `sina.py` 115
denetimin 115'ini geçti (`cevrim.exe` için 28, iki betik için 14).
Betikler, adı Türkçe harfli, boşluklu ve parantezli dosya ve klasörle
denendi; ürettikleri dosyalar modelle bayt bayt karşılaştırıldı. Windows
`cevrim.exe`'yi 64 bit program olarak tanıdı; Defender taradı, tehdit
bulmadı; Base64 yazımından `certutil` ile kurulan dosya özgünüyle aynı
çıktı.
Denenmeyenler: sürükle bırakın kendisi (betikler komut satırından, tam
yol ve tırnakla çağrıldı), Windows uyarısı (SmartScreen) ve kullanıcının
kendi makinesi.

Bu klasör bir üye notudur, komut değildir.

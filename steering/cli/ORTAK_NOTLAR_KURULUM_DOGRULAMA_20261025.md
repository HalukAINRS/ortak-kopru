# Ortak Notlar Windows kurulumu: ikinci tanık denetimi

Haluk'un gönderdiği görseldeki `is-emirleri/kurulum-2026-10-25.txt` dosyası Hacker'ın VM çalışma alanında bulundu. Kaynak iş metninin SHA-256 değeri `7881b7e740ac0c91f140b97dc2f597c85cff73337557dbe9bd7d12a5f3cfbfc6`. Windows kurulumu Şahit tarafından yapıldı; Şaman dört dosyanın karmasını bağımsız hesapladı. Araç `Y:/HalukAI/Ortak_Kopru/Ortak_Notlar_Yolu` altında, kamu Git deposu `kopru` ile kardeş konumda. Bu rapor kurulum paketini veya bağlantı ayarlarını yayımlamaz.

| Dosya | İş metniyle eşleşen SHA-256 |
|---|---|
| BENIOKU.txt | `9f2956d6d92db7e57271438aaec414baa333267f3ad06bd9e6442acf641b1d14` |
| Notlar_Esitle.cmd | `1599ccbd8e18d3531ea96bc3c5a8ea619abffed56750c3108b54a0f4d71daf0c` |
| anlati_dosyalari.txt | `86ede3737ec494affb05cf1cd72e8b8e790a24ad06652c4cd8857f93e3d47b7f` |
| notlar_esitle.py | `de9e39f5202908e655c3e82331d42dc4ea563a0eb9d0375c077d422aefafe70b` |

Şaman'ın ayrı yazmasız denemesi sıfır çıkış koduyla bitti ve o deneme sırasında ortak belgelerin karmaları değişmedi. Beklenen eski “beş çakışma” sayısı güncel kesitte geçerli değildi: yedi güncel belge korundu; `Steering Arsiv.txt` için yeni yazım öngörüldü. Gerçek ilk aktarım bu ASCII adlı dosyayı oluşturdu. Dolayısıyla yalnız çıkış kodu veya dört karma, doğru hedefe yazıldığını kanıtlamadı.

FAT32 dizininde iki ayrı giriş görüldü: `STEERI~1.TXT` ile asıl `Steering Arşiv.txt` 53.165 bayt / `517a59b8e66b1a279af5d5ffd33ff9479b48265b8c070f78197c8f872a80ee16`; `STEERI~2.TXT` ile gelen `Steering Arsiv.txt` 65.934 bayt / `5243a52e803d53f553ca531b53edb30d47436e85b53a1321ca702b7604b4a179`. Normal Unicode yolunun ikinci girişin içeriğini açtığı Şaman tarafından da yeniden üretildi. İlk “sekiz VM kopyası eşleşti” denetimi bu ad çözümlemesi nedeniyle asıl Steering içeriğini doğrulamıyordu; bu sonuç düzeltildi. Kısa ad üzerinden okuma, kaynak karması ve dizin girdisi boyutu birlikte kontrol edildi.

Şahit iki özgün sürümü yedekledi; 41 ortak S maddesiyle Hacker'ın 113 maddelik kaynak derlemesini koruyan metni her iki girişe aynı baytlarla yazdı. Böylece bu kesitte normal yoldan okuma eski ortak maddeleri gölgelemiyor. İki fiziksel adın varlığı paketin kalıcı ad eşlemesi sorununun çözüldüğü anlamına gelmez. Kaynak derlemedeki tekrarları S maddeleriyle eşlemek de açık; 41 ve 113 sayıları bağımsız yeni bulgular olarak toplanmaz.

Şahit'in başlattığı tek `--dongu` eşitleyicisi süreç tablosunda görüldü. Şaman ikinci eşitleyici başlatmadı ve dört kaynak dosyasını değiştirmedi. Windows–VM okuma yönü gerçek dosya kopyalarıyla gözlendi; bir kopyanın bulunması Hacker'ın onu okuduğunu kanıtlamaz. Varsayılan aktarım TXT içindir; `.md` devir notunun otomatik gönderildiği iddia edilmedi.

deus_ex_machina yüzeyi iki kayıtlı katman ve iki işle yanıt vermeyi sürdürdü; mevcut yüzey ve kuyruk tüketicisi süreçleri devam etti. Bu denetim yeni kullanıcı işi veya yeni model/API çağrısı üretmedi. Kesintili tam sistem yeniden başlatma kabulü bu kapsamda yapılmadı.

Özel dayanaklar: Şaman Workspace/Acik_Isler_20261024/Ortak_Notlar_Kurulum_20261025 içindeki `SAMAN_BAGIMSIZ_DOGRULAMA.json`, `DENEME_SAMAN_TAM_CIKTI.txt`, `SON_SUREC_GOZLEMI.json`; Şahit'in `CYBER_SAHIT_DOGRULAMA_20261025.json` kaydı; ortak arşiv S-040 ve S-041. Kaynak iş metni, görsel, tam konsol çıktısı ve özgün dosyalar özel alanda korunuyor.

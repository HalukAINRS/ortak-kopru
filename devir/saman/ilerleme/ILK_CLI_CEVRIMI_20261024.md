# Mevcut Şaman CLI oturumuyla ilk karşılıklı çevrim

24 Ekim 2026. [Yerel uygulama](../../../uygulama/deus_cli/README.md), Haluk'un özgün isteğini belirli açık CLI oturumuna taşıyıp kaynaklı karşılığı aynı işe getiriyor. Kalıcı SQLite kayıtları Git deposunun dışında Y: üzerinde; özel konuşma gövdeleri yayımlanmadı. [İşlem özeti ve karmalar](ILK_CLI_CEVRIMI_20261024.json) gerçek çevrimden üretildi.

## Gerçekleşen işlem

Şaman, Haluk'un bu oturumdaki son devir talebinin görev cümlesini aynen yerel HTTP girişine gönderdi. Kaynak notu, aktarımı yapanın Şaman olduğunu açıkça belirtiyor. Bu, yeni bir kullanıcı tıklaması veya yeni Haluk talimatı diye sunulmadı.

Mevcut açık Codex Şaman oturumu `receive` komutuyla bu isteği gerçekten aldı. Ayrı bir model süreci başlatılmadı. İstek alındıktan sonra v11 arşivinin tarihsel karması ve 19 dosyanın bütünlüğü yeniden denetlendi. Bu gerçek model oturumunun yazdığı yanıt, üç dosyanın bayt/karmalarıyla `reply` üzerinden aynı işe döndü; HTTP okumasıyla doğrulandı.

Şaman, düzeltme ve devam sınaması için ikinci bir ileti oluşturdu; kaynak notunda yeni Haluk kararı olmadığı belirtildi. Bu ileti alındıktan sonra yalnız bu uygulamanın HTTP sunucusu durduruldu. Kapalıyken erişilemediği gözlendi. Sunucu aynı kalıcı dizinle yeniden başlatılınca ikinci ileti aynı iş, hedef oturum ve ilk alım zamanıyla tekrar alındı; yeni teslim olayı oluşmadı. İlk yanıtın karması değişmedi. İkinci gerçek yanıt da aynı işe döndü. İlk HTTP gönderimi ve ikinci CLI yanıtı yinelendiğinde kayıt/olay sayısı artmadı.

## Kapsam ve açık işler

Arayüzde fiilen kayıtlı tek oturum mevcut Şaman'dır. Hacker, Şahit, Gemini ve başkaları kendi gerçek CLI oturumlarını kaydedebilir; onların okuduğu veya bağlandığı ileri sürülmüyor. Şahit zorunlu geçit yapılmadı. API çağrısı, kök üretici adıyla yedek yönlendirme veya ikinci Codex çalıştırması yok.

CLI alımı şu anda açık CLI'ın verdiği komutla gerçekleşir. Sürekli otomatik tüketici, başka CLI'ların bağlantısı, Windows–Ubuntu taşıması, çekirdek v11 ile bütünleştirme ve CLI model sürecinin yeniden başlatılması açık. HTTP sunucusunu yeniden başlatma bu son maddeyi tamamlamaz. Tarayıcı üzerinden görsel kullanım ve gerçek kullanıcı düzeltmesi ayrıca sınanmadı.

Normal Chrome profilinin açılışı otomatik onay denetimince iki denemede reddedildi; araç yalnız `blocked by policy` nedeni verdi. Başka mekanizmayla aynı açılışı dolaşma denemesi yapılmadı. Haluk, özgün Steering ZIP'ini yerele indiremediğini bildirdi. Bağlı Drive'da tam adı ve ilgili dosya adları arandı; özgün ZIP bulunmadı. GitHub'ın 85 tam Steering dosyası yerelde ayrı arşive kondu; eksik özgün ZIP ile aynı sayılmadı. Beklenen özgün boyut 100641653 bayt, SHA-256 `827bb9cac16fdb7b643c576a3bd41523e725ad4542ab023c5c4d45f3435b1009`.

## Doğrulama

Windows/WinPE'de yeni köprünün 8 unittest testi 15.663 saniyede geçti. Özgün metnin korunması, yanlış oturum, eşzamanlı thread ve ayrı süreç alımı, yeniden alım, değişmez yanıt, kaynak karması, aynı işte düzeltme ve HTTP turu/köken denetimi kapsandı. `node --check app.js` geçti. 105 sabit devir dosyasının boyut ve SHA-256 değerleri yeniden eşleşti. Gerçek çevrim test karşılıklarından ayrı kaydedildi.

İlk eşzamanlı denemelerde SQLite tek başına alımı ayıramadı; yerel süreç kilidi eklenince thread ve ayrı süreç testleri geçti. Bu kilit aynı makine içindir. Eski v11 Linux testinin 180 saniyede tamamlanmamış sonucu korunur; yeni köprü testleri eski test dizisinin başarısı değildir.

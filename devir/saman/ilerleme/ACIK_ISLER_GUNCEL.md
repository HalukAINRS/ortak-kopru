# Şaman CLI güncel işler — 24 Ekim 2026

Son devam: **1 Steering, 2 deus_ex_machina, 3 Şaman–Şahit–Hacker kurulumu.** Steering yerel kaynak denetimi PR #8'de; kaynak bağlamının gerçek CLI'a gidiş/dönüşü [KAYNAK_BAGLAMI_20261024.md](KAYNAK_BAGLAMI_20261024.md) içinde. Yeni açık iş listesi IS_SIRASI_20261024.json'dur; aşağıdaki S kayıtları tarihsel ilerlemeyi korur.

- S1 tamamlandı: a3e34ad ek paketi mevcut gerçek CLI'a alındı; 105 sabit dosya doğrulandı; seçili devir belgeleri okundu. DEVIR_ALINDI.json gerçek alım kaydıdır.
- S2 sürüyor: asıl 519 mesaj/80 eşleme korunur; yeni sohbet 308 ve paylaşım 289 mesajla eklendi. Çekirdek v11 ve iki bağlam paketi artık mevcut. Oturum köprüsü HTTP 415, kaynak PDF/ZIP ve kalan ekler açık.
- S3 kısmi: PR #4'ün 99dc8a3 kuyruğu süreç başlatmıyor; PR #5'in 2a68b37 devriyle birlikte ayrı uygulama yoluna dayanak alındı. Yeni köprü bu katkılara birleştirilmiş veya eski çekirdekle bütünleşmiş sayılmaz. Bütünleştirme açık.
- S4 ilk gerçek çevrim doğrulandı: Haluk'un mevcut görev cümlesi Şaman tarafından HTTP girişine aynen aktarıldı; mevcut açık Şaman CLI oturumu aldı, v11'i yeniden denetledi ve kaynaklı gerçek model yanıtını aynı HTTP işine döndürdü. Kullanıcının tarayıcı tıklaması sınanmadı; sürekli otomatik tüketici yok. İşletim ayrıntısı ILK_CLI_CEVRIMI_20261024.md içindedir.
- S5 kısmi doğrulandı: HTTP sunucusu gerçekten durdurulup yeniden açıldı; alınmış ikinci ileti aynı iş/oturum/alım zamanıyla sürdü, önceki yanıt korundu. İkinci ileti Şaman'ın doğrulama girdisidir. CLI model sürecinin kapanıp yeni süreçte sürdürülmesi ayrıca açık.
- S6 yerel oturum hedeflemesi doğrulandı: yalnız mevcut Şaman kayıtlı; yanlış oturuma teslim/yanıt testleri geçiyor. Hacker, Şahit ve diğer katmanların gerçek bağlantıları ile Windows–VM taşıması açık.
- S7 sürüyor: belge, mesaj ağacı, dosya baytı ve SQLite içeriği gerçek kaynaklarıyla görüldü; görülmeyen iç bileşenler erişilmiş sayılmaz.
- S8: v11 paket bütünlüğü ve tarihsel makbuz eşliği doğrulandı. Hedef ortam test denemesi ve gerçek uygulama bağlantısı ayrıca kaydedilir; eski pilot yeniden başlatılmadı.

Linux çalışma denemesi: ayrı dizinde tam unittest dizisi 180 saniyede tamamlanmadı; tam test başarısı doğrulanmadı. Dosya karmaları ve SQLite bütünlüğü doğrulaması geçerlidir. Test sonucu ayrı JSON kaydında korunur; eski pilot yeniden başlatılmadı.

Yeni köprünün sekiz testi geçti; bu sonuç eski çekirdeğin tamamlanmamış Linux testinden ayrıdır. 105 sabit devir dosyasının tamamı yeniden doğrulandı. Özgün Steering ZIP'i yerelde yok; Haluk indiremediğini bildirdi. GitHub'ın 85 tam dosyası yerelde ayrı ZIP'e alındı; özgün arşivin yerine eşitlenmedi.

Kaynak bağlamı eklendikten sonra yeni köprünün on testi geçti; önceki sekiz test kaydı kendi sürümüne aittir. Gerçek veritabanının önceki iki iletisi ve yanıtı korundu; son kullanıcı öncelik iletisi üçüncü ileti olarak aynı CLI'a ulaştı ve kaynaklı yanıtı döndü. Şahit'in sabit oturum kontrolü ve Hacker VM sürüm/devir dizini kontrolü geçti; onların yeni yüzeye bağlandığı ileri sürülmez.

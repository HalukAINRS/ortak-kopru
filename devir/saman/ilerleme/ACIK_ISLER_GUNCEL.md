# Şaman CLI güncel işler — 24 Ekim 2026

- S1 tamamlandı: a3e34ad ek paketi mevcut gerçek CLI'a alındı; 105 sabit dosya doğrulandı; seçili devir belgeleri okundu. DEVIR_ALINDI.json gerçek alım kaydıdır.
- S2 sürüyor: asıl 519 mesaj/80 eşleme korunur; yeni sohbet 308 ve paylaşım 289 mesajla eklendi. Çekirdek v11 ve iki bağlam paketi artık mevcut. Oturum köprüsü HTTP 415, kaynak PDF/ZIP ve kalan ekler açık.
- S3 açık: PR #4 ve #5 güncel uygulama sözleşmelerini ilk gerçek çevrim için değerlendir. Önceki 69adfbc eksiklik bulgusu güncel kodun yokluğu diye aktarılmaz.
- S4 açık: özgün kullanıcı girdisini belirli gerçek CLI oturumuna teslim edip kaynaklı yanıtı aynı yüzeye getir. Bu kaynak devri bunun yerine sayılmaz.
- S5/S6 açık: ilk çevrimden sonra kesinti/düzeltme ve katman/oturum hedeflemesini sına. Sabit başlatıcı hazırlığı gerçek çevrim değildir.
- S7 sürüyor: belge, mesaj ağacı, dosya baytı ve SQLite içeriği gerçek kaynaklarıyla görüldü; görülmeyen iç bileşenler erişilmiş sayılmaz.
- S8: v11 paket bütünlüğü ve tarihsel makbuz eşliği doğrulandı. Hedef ortam test denemesi ve gerçek uygulama bağlantısı ayrıca kaydedilir; eski pilot yeniden başlatılmadı.

Linux çalışma denemesi: ayrı dizinde tam unittest dizisi 180 saniyede tamamlanmadı; tam test başarısı doğrulanmadı. Dosya karmaları ve SQLite bütünlüğü doğrulaması geçerlidir. Test sonucu ayrı JSON kaydında korunur; eski pilot yeniden başlatılmadı.

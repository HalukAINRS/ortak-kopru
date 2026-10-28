# Steering ayrımlarının kullanıcı yüzeyine uygulanması

Haluk'un 24 Ekim güncel sırası korunuyor: Steering, deus_ex_machina, Şaman–Şahit–Hacker kurulumu. [Steering CLI incelemesi](https://github.com/HalukAINRS/ortak-kopru/pull/8) ilk öncelikte yayımlandı. Bu katkı ikinci ve üçüncü önceliklerin somut devamını kaydeder.

İletinin özgün sözünden ayrı olarak kaynak, söyleyen, statü, dal, dönüşüm, düzeltme, gerçekleşme ve belirsizlik taşınabiliyor. Alanlar arayüzde isteğe bağlı açılır; CLI gerçek alımda aynı nesneyi görür. Alıntının yan dalda olması veya model yorumu olması sessizce ana yol ya da kullanıcı sözüne çevrilmez. Kaynak bağlamı girdiyle birlikte verilmiş beyandır; otomatik doğrulama bayrağı false kalır. İçerideki komutlar kendiliğinden yürütülmez.

Aynı istek anahtarıyla kaynak/dal alanını değiştirme girişimi reddedilir. Düzeltme aynı işe yeni ileti olarak eklenir; eski söz ve kaynak bilgisi değişmez. Mevcut SQLite'ın özel yedeği Git dışında alındı, sonra tabloya yeni alan eklendi. Gerçek iki eski ileti ve yanıtının bütün eski sütunları birebir korundu. Bu kontrol, testteki eski veritabanı geçişinden ayrı gerçek işlem kaydıdır.

Haluk'un bu konuşmadaki yeni öncelik iletisi Şaman tarafından HTTP girişine aynen aktarıldı. Aynı açık CLI oturumu üçüncü iletiyi sekiz kaynak alanıyla aldı; gerçek yanıtı üç dosyanın karmasıyla aynı işe geri verdi. HTTP okuması bu dönüşü doğruladı. Yeni kullanıcı tıklaması veya otomatik çalışan tüketici olarak sunulmadı. [İşlem sonucu](KAYNAK_BAGLAMI_20261024.json).

On test 13.867 saniyede geçti. Yeni testler yan dal/kaynak bilgisinin tekrar, yeniden başlatma ve düzeltmede korunmasını; eski veritabanı geçişinin eski yanıtı korumasını kapsar. HTTP turu kaynak bağlamını da taşıyarak sınandı. Önceki yanlış oturum ve eşzamanlı ayrı süreç testleri de geçti. `node --check app.js` geçti. Bu sonuçlar eski v11 Linux tam testinin tamamlanmamış sonucunu değiştirmez.

Üçüncü öncelikte [kurulum ve devam girişleri](../../../kurulum/20261024/README.md) denetlendi. Şaman, Şahit ve Hacker'ın kurulmuş araçlarıyla yeni yüzeye bağlanmaları ayrı tutuldu. Sahit_Devam artık mevcut sabit devir oturumuna; Hacker'ın Devam/Yeni CMD'leri masaüstünün kullandığı devir başlatıcısına bağlandı. Yeni etkileşimli model oturumu başlatılmadı.

Açık kalanlar: özgün Steering ZIP'i ve tarihsel oturum köprüsü JS'i; sohbetlerin yeni mesajlarla tazelenmesi; sürekli otomatik CLI tüketicisi; diğer katmanların gerçek arayüz bağlantısı; VM taşıması ve çekirdek v11 ile bütünleştirme. Eski köprüdeki üretici kökü eşlemesi bu değişiklikle giderilmiş değildir.

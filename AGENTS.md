# Şaman — bu çalışma ağacındaki devam görevi

Bu çalışma ağacı Haluk'un ChatGPT'den Codex CLI'ya Şaman olarak devir talebi için hazırlanmıştır. Etkin kullanıcı talebinin özgün metni `devir/saman/GORUNUR_KONUSMA.md` içindedir. Türkçe çalış.

Önce `devir/saman/CLI_BASLANGIC.md`, `devir/saman/DEVIR.md`, `devir/saman/ACIK_ISLER.md` ve `deus_ex_machina/SAMAN.md` dosyalarını oku. `devir/saman/kaynaklar/steering/` içindeki 85 dosya önceki araştırmanın tam yayımlanmış kopyasıdır; bağlantıya bakmakla okunmuş sayılmaz. Ana rapor, korunacak bağlam ve güncel depo okumasından başlayıp işin gerektirdiği kanıta in.

Haluk burada bitmiş araştırmayı yeniden başlatmanı değil, mevcut bağlamı kullanarak eksik işlerden CLI'da devam etmeni istiyor. İlk işler: bu yeni ek paketin alımını mevcut Şaman devamına bağlamak, erişilebilir özgün kaynakları bulmak ve deus_ex_machina üzerinden bir kullanıcı işinin gerçek CLI karşılığını kurmak. Rutin okuma, geri alınabilir çalışma ve bu kapsamda uygulama için aynı izni yeniden isteme. Gerçek erişim engelini somut kaynağıyla bildir ve etkilenmeyen işe devam et.

Etkin mimari: deus_ex_machina, Haluk'un kullanıcı yüzeyidir; Hacker, Şaman, Şahit ve gerektiğinde diğer CLI katmanlarıyla karşılıklı çalışır. Şahit zorunlu tek geçit değildir. CLI katmanları görevle ilgili erişilebilir kaynak, yapılandırma, kod, süreç ve çalışma zamanı katmanlarına kadar ilerler; gözlenmeyen bir katmana erişilmiş sonucu yazılmaz.

Kaynak, Söyleyen, Özgün söz, Statü, Dönüşüm, Düzeltme, Gerçekleşme ve Belirsizlik birlikte korunur. `>` gösterme, `->` akıştır. Araştırma ile bağlam aktarımı ayrı kayıtlanır. Önceki bir katmanın okumasını kendi yeni deneyimin olarak yazma. Eski önerileri yeni kullanıcı talimatının yerine koyma.

`AGENTS-kopru.md` köprüye yazma sözleşmesidir. Yeni kayıtları `kopru_ekle.py` ile ekle; aynayı `kopru_ayna_uret.py` ile üret. Başkasının kaydını düzeltmek için yeni kayıt yaz. Eski otomasyon kök üretici adına göre yönlendirir; `ChatGPT (Şaman)` etiketi API oturumunu tek başına dışlamaz. Ayrıntı `devir/saman/YONLENDIRME_NOTU.md` içindedir.

Çalışmayı `devir/saman/ilerleme/` altında kaynaklı durum ve açık iş güncellemeleriyle sürdür; sabit paket dosyalarını başlangıç kaydı olarak koru. Git'te mevcut kullanıcı değişikliklerini koru. Ana dalda köprü yardımcıları, ayrıntılı içerikte bu katkı dalı düzenini sürdür. Ham özel kaynakları ve erişim bilgilerini herkese açık depoya ekleme; yerel kaynakları repo dışında kullan.

Bu dosyanın yüklenmesi bu yeni ek paketin kabulünün kanıtı değildir. k-0111 ile bildirilen mevcut Şaman çalışmasını koru. Bu pakete ilişkin gerçek CLI yanıtın; okuduğun dosyaları/sürümleri, gördüğün ortamı, açık kalan kaynağı ve başladığın somut işi yazmalıdır.

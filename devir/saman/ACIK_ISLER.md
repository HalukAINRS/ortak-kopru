# CLI'da devam edilecek işler

Bu liste yeni kullanıcı talimatını yürütür. Önceki kaynaklarda geçen her öneriyi yeni iş emrine dönüştürmez. Daha önce tamamlanan steering yayınını sıfırdan yeniden yapma.

**Korunacak tamamlanmış kaynak işi:** k-0111 ve `deus_ex_machina/KAYNAK_DEVRI_20261024.md`, mevcut Şaman CLI çalışmasında 519 görünür mesajın (296 ana yol, 223 yan dal) alındığını ve 80 eski defter kaydının tamamının eşlendiğini bildirir. 029–038 yalnız yan dallardadır. Bu işler yeniden açık değildir. 15 girdi eki/22 çıktı başvurusu ve altı yerel asıl dosya mevcut envanterden sürdürülür. Bu web oturumunun yaptığı şey kaynak bildirimini okumak ve yeni ek paketi hazırlamaktır; aşağıdaki S1 yalnız bu yeni paketin hedefte kabulünü anlatır.

| Kimlik / öncelik | Somut iş | Başlangıç dayanağı | Tamamlanma kanıtı |
| --- | --- | --- | --- |
| S1 / ilk | Bu yeni ek paketi mümkünse mevcut açık Şaman oturumunda almak ve devam etmek | `CLI_BASLANGIC.md`, `MANIFESTO.json`, k-0111, gerçek oturumun mevcut ilerlemesi | Yeni paket commit'i ve gerçekten okunan dosyalarla kabul kaydı; önceki Şaman işi korunur, yeni oturum gerekiyorsa ayrı belirtilir |
| S2 / ilk | Mevcut kaynak envanterinden eksik ek/görüntü, v11, oturum köprüsü ve diğer dosya baytlarını tamamlamak; Steering ZIP'inin yerel erişimini doğrulamak | `KAYNAK_ALIMI_20261024.md`, `MESAJ_DOGRULAMASI.json`, `ESKI_DEFTER_KARSILASTIRMA.json`, `DOSYA_BAGLANTILARI.json`, mevcut devam kaydı ve ZIP karması | Yalnız eksik kaynaklar için bulundu/bulunamadı/erişilemedi, boyut/hash/eşleme; 519 mesaj ve 80 eşleme yeniden açılmaz |
| S3 / yüksek | PR #4 ve #5'in güncel dosyalarını mevcut katman tarifine göre değerlendirmek | `KAYNAKLAR.json`, `deus_ex_machina/SAMAN.md` | Mevcut kuyruk/başlatıcı sözleşmesi, uygulanacak farklar ve karşılıkları; tarihsel eksikliklerin güncellenmesi |
| S4 / yüksek | Kullanıcı yüzeyinden belirli gerçek CLI oturumuna ilk işi gönderip sonucu geri getirmek | Haluk'un yeni talebi; PR #4 kuyruğu ve mevcut CLI başlatıcıları | Aynı iş kimliğiyle özgün girdi, hedef oturum, gerçek teslim, gerçek yanıt ve yüzeyde gösterilen kaynaklı sonuç |
| S5 / yüksek | Kesinti, tekrar başlatma ve kullanıcı düzeltmesini aynı işe bağlamak | İlk S4 çevrimi | İşin iki kez yanlış çalıştırılmadığı; son durumdan devam; kullanıcı düzeltmesinin hedef iş/katmana ulaştığı gözlem |
| S6 / normal | CLI/API ve kök ad yönlendirmesinin katman/oturum ayrımını netleştirmek | `YONLENDIRME_NOTU.md`, `kopru_yanitla.py` | `ChatGPT (Şaman)` işinin API oturumunca sahiplenilmesini önleyen açık hedef sözleşmesi ve ilgili doğrulama |
| S7 / normal | Derin kaynak incelemesini gerçek erişim tablosuyla yürütmek | Kaynak, kurulum dosyaları, CLI sürümleri, ilgili açık iş | Belge → yapılandırma → çağrı → araç/süreç → uygulama kaynağı zincirinde gerçekten görülenlerin ve açıklanamayanların ayrı kaydı |
| S8 / gerekirse | Eski pilot çekirdeğini HalukAI'deki gerçek ortama bağlamak | Önceki v11/v2/12-12 beyanları ve bulunacak gerçek paket | Dosya doğrulaması ve yerel çalışma sonucu; tarihsel başarı beyanının yeni ortama taşınmaması |

## Çalışma sırası

Zaten açık Şaman oturumu varsa onun kaynak/ilerleme kayıtları korunarak S1 yapılır. Yeni oturum gerekiyorsa ayrı başlatıcı kullanılır; aynı süreç belleğinin taşındığı varsayılmaz. S2'nin erişilebilir kısmı mevcut envanterden sürer; S3 ile S4 uygulaması paralel ilerleyebilir. Kaynak paketlerinden biri bulunamadığında bütün çalışmayı durdurma: eksikliği S2'de somutlaştır, eldeki repo/raporla ilerleyebilen S3/S4'e devam et. S5 ve S6, ilk gerçek kullanıcı yüzeyi/CLI çevriminin güvenilir devamını tamamlar. S7 her işin gerektirdiği kaynak derinliğinde yürür.

## Önceki araştırmadaki açık sorular

Steering raporlarında kalan doğrulanmamış uygulama, test, model/ürün iç mekanizması ve kaynak boşlukları kendi raporlarında korunur. Bunları yeni sonuca çevirmeden ilgili kanıta dön. `ANA_RAPOR.md` bir kaynak haritasıdır; bir iddiayı hedef ortamda yeniden sınamak gerektiğinde onu `ilerleme/` altında ayrı işlem olarak kaydet.

## İlerleme kaydı

Her değişiklikte iş kimliği, kaynak, yapılan işlem, gözlenen sonuç ve sıradaki somut adımı yaz. `ilerleme/ACIK_ISLER_GUNCEL.md` ile listeyi sürdür; bu ilk listeyi tarihsel başlangıç olarak koru. Durum sözcükleri gözlenen olaya karşılık gelsin: hazırlandı, başlatıldı, okundu, denendi, sonuçlandı veya somut nedenle engellendi. Bir kullanıcının daha önce verdiği yetkiyi rutin olarak tekrar isteme.

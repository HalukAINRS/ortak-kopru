# Şaman: buradan devam et

Haluk, bu konuşmanın Codex CLI'ya Şaman olarak taşınmasını, mevcut bütün iş bağlamının kullanılmasını ve eksik işlerin burada sürdürülmesini istedi. Özgün talep [GORUNUR_KONUSMA.md](GORUNUR_KONUSMA.md) içindedir. Bu artık bir sonraki adımı teklif etme işi değildir; yetkilendirilmiş devri al ve çalışmayı sürdür.

k-0111 ve [kaynak devri kaydı](../../deus_ex_machina/KAYNAK_DEVRI_20261024.md), mevcut Şaman CLI çalışmasının 519 görünür mesajı aldığını ve 80 eski defter kaydını eşlediğini bildiriyor. Zaten o oturumdaysan onun mevcut kaynak/ilerleme kayıtlarından devam et. Başka bir oturumdaysan bu sonucu kaynak beyanı olarak devral; kendi yeni işlemin gibi anlatma. Bu sonraki web paketi önceki işi sıfırlamaz; yalnız yeni dosyaların hedefte okunma/kabul kaydı ayrıca gerekir.

## İlk çalışma

1. Açık Şaman oturumunun mevcut işini ve kaynak kayıtlarını koru. `git status --short`, `git rev-parse HEAD` ve `git branch --show-current` ile eriştiğin çalışma ağacını tanı. Başlatıcının ürettiği özel yerel hazırlık kaydını, varsa `SAMAN_DEVIR_STATE` ortam değişkeninin gösterdiği dosyadan oku. Mevcut oturuma yalnız dosya yolu verilmişse bu değişkenin kendiliğinden taşındığını varsayma. Özel kaynak yolunu herkese açık çıktıya kopyalama.
2. Bu dizindeki `DEVIR.md`, `GORUNUR_KONUSMA.md`, `ACIK_ISLER.md`, `YONLENDIRME_NOTU.md` ve repo kökündeki `deus_ex_machina/SAMAN.md` dosyalarını oku. `MANIFESTO.json` ile sabit dosyaları doğrula; başlatıcı kontrolü dosyaların içeriğini semantik olarak okuduğunun yerine geçmez.
3. `kaynaklar/steering/ANA_RAPOR.md`, `ISTENEN_BAGLAM.md`, `AKTARIM_KAPSAMI.md`, `depo/GUNCEL_OKUMA_2026-10-24.md`, `depo/GUNCEL_KOD_VE_PR_OKUMASI.md` ve `depo/REFERANS_DALLARI_OKUMASI.md` başlangıç okumasıdır. Kullanıcının simgesel açıklamalarını kaynak biçimiyle koru. Eski Şahit merkezli çizimin ardından gelen tüm CLI katmanlarıyla ilişki tarifini esas al.
4. Köprünün `95d646e6c8c694cf32d56aa7a2ab7a67c15ed729` tabanındaki k-0001–k-0111 envanterini, devirle ilgili k-0016/k-0039/k-0110/k-0111 kayıtlarını ve güncel `origin/main` farkını oku; ilgili iş ilerlerken gereken tam kayda ve açıklama bölümüne dön. `KAYNAK_ALIMI_20261024.md`, `MESAJ_DOGRULAMASI.json`, `ESKI_DEFTER_KARSILASTIRMA.json`, `DOSYA_BAGLANTILARI.json` ve yerel devam kaydına git. Tamamlanmış 519 mesaj/80 eşleme işini yeniden başlatma; 029–038'in yalnız yan dal olduğunu koru. Paket oluşturulduktan sonra gelen kayıtları fark okuması olarak kaydet. Sabit devir kaynaklarını üzerine yazma.
5. Bu **yeni ek paketin** `ilerleme/DEVIR_ALINDI.json` kabul kaydını kendi gerçek CLI oturumunda, yaptığın okuma ve ortam kontrollerinden sonra oluştur. Önceden aynı adlı kayıt varsa silme; paket commit'iyle yeni bir kabul kaydı ekle. `kimden`, gerçek zaman, commit, okunan dosya/sürümler, erişilebilen kaynaklar, henüz okunmayanlar, devam işi ve dayanakları içersin. k-0111'in önceki kaynak alımını bu yeni paketin kabulü sayma. Henüz okumadığın 85 dosyaya toplu okundu işareti koyma.
6. [ACIK_ISLER.md](ACIK_ISLER.md) içindeki S1 ve S2'yi başlat. Kullanıcının depo ve bağlam çalışmasına verdiği talimatı tekrar onaya bağlama. Kaynak bulunamazsa aranan konum ve sonucu belirt, erişebildiğin kaynaklarla S3/S4'e ilerle.

## Öncelikli somut devam

İlk ürün hedefi, **deus_ex_machina üzerinde Haluk'un özgün isteğinin korunması → belirli gerçek CLI oturumuna teslim → o oturumun kaynaklı cevabı → aynı kullanıcı yüzeyine dönüş** çevrimidir. Çevrim bir kez başarıyla çalışınca kesintiden devam ve kullanıcı düzeltmesinin aynı işe dönüşü sınanır.

PR #4'teki kuyruğu ve PR #5'teki Hacker devrini gerçek dosyalarıyla incele. Her ikisinin güncel dal ucunu yeniden belirle. Sahte yanıt veya yalnız kuyruğa yazma, CLI sonucu diye sunulmaz. Bir taslağın ana dala uygulanmış olduğunu varsayma. İşin gerektirdiği değişiklikleri ayrı çalışma dalında yap; ilgili doğrulamayı gerçekleştir ve kaynaklı sonuçları geri yaz.

## Kayıt biçimi ve iletişim

Bu ek pakete ilk CLI karşılığı Türkçe şu bilgileri taşısın: hangi dosyaların hangi sürümünü gördüm; hangi mevcut Şaman işini koruyarak devam ediyorum; hangi kaynağa henüz ulaşamadım; şimdi hangi somut iş üzerinde çalışıyorum. Bu bildirimden sonra işe devam et.

Köprüde bilgi kaydı yazarken `kimden="ChatGPT (Şaman)"`, `kime="Sen"` kullan. Devir kabulünün başka eski açık işleri örtük kapatmaması için `yanit` alanını, yalnız bu işe ait kaynak bağı gerçekten gerektiğinde kullan; `--yanit son` seçeneğini varsayılan yapma. Otomasyonun sayı eşiği davranışı `YONLENDIRME_NOTU.md` içinde açıklanır.

Yeni sonuçları `ilerleme/` altında tut. Kaynak/yorum/düzeltme/gerçekleşme ayrımı sürsün. Karşılaşılmış somut erişim veya çalıştırma engeli varsa kanıtıyla bildir; yapılabilecek kalan işleri sürdür.

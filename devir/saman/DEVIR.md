# Devredilen iş bağlamı

## 1. Etkin amaç ve konuşmanın durumu

Haluk önce steering hakkında elde edilenlerin `HalukAINRS/ortak-kopru` deposuna gönderilmesini ve deponun okunmasını istedi. Bu işin son yayını tamamlandı. Ardından aynı çalışmanın Codex CLI'ya **Şaman** olarak taşınmasını ve eksiklerin orada sürdürülmesini istedi. Yeni talep `GORUNUR_KONUSMA.md` içinde özgün biçimiyle bulunur.

Yeni mimaride **deus_ex_machina**, Haluk'un yüzeydeki kullanıcı arayüzüdür. Hacker, Şaman, Şahit ve gerektiğinde Gemini/başka CLI katmanlarıyla karşılıklı çalışır. CLI katmanları daha derin kaynak ve çalışma zamanı katmanlarına iner. Bu tarif önceki tek geçit yorumunu günceller; Şahit bütün etkileşimin zorunlu kapısı değildir.

## 2. Son tamamlanan yayın

| Öğe | Sabit sürüm / sonuç |
| --- | --- |
| Steering incelemesi | `80fd42db48e91104383b47b6b4144f01790999be`, 85 dosya |
| Ana köprü yayını | `52c797e4c7e7b8029c6d1aad651ada8f57b7d4b8`, k-0110 |
| Hazırlık sırasında gelen Şaman kaynak kaydı | `95d646e6c8c694cf32d56aa7a2ab7a67c15ed729`, k-0111 |
| Güncel konu dalındaki kaynak devri | `df73d42c0ac63894617f92df7b97e5ec3cc97f78`, `KAYNAK_DEVRI_20261024.md` |
| Önceki inceleme | `489fd9a70eee90821f5144ad44b049caea4e5071`, 68 dosya |
| Tam okunan ana dal | `8571ddf8e3a33b432cc1c7ef88b69a902f390e5c`, 109 kayıt |
| Yayın öncesi ek | `085422b3ea0a3301fb8f7e42cbff66b674e1235b`, yalnız atlama günlüğüne bir satır |
| Taslak PR | [#1](https://github.com/HalukAINRS/ortak-kopru/pull/1), inceleme dalı; taslak olarak korundu |

Steering'in `80fd42db48e91104383b47b6b4144f01790999be` güncellemesinde 17 dosya eklendi, 5 dosya güncellendi. Önceki 19 aile raporu ve tarihsel durum çizelgesi aynı gövdelerle korundu. Sistem ailesi F00197/U0126 için ayrı tam tamamlayıcı rapor eklendi. İnceleme yayınının 85 Git blob kimliği ve boyutu gönderilen dosyalarla eşleşti; 45 JSON ve 201 göreli Markdown bağlantısı kontrol edildi. k-0110 yayını sırasında ana dalda README, kanonik köprü ve ayna değişti; önceki 109 kaydın ham HTML karmaları ve dört katılımcının bekleyen listeleri korundu. Sonraki k-0111 ayrı Şaman kaynak devri kaydıdır.

`kaynaklar/steering/` bu 85 dosyanın **baytları aynı** kopyasıdır. Tek başına yeni bir okuma veya yeni bir 85 kaynak kümesi değildir. Kaynak dosya listesi ve karma denetimi bu paketin manifestosunda da vardır.

## 3. Özgün arşiv

Dosya: `Steering_Evrak_Okuma_Paketi.zip`.

- Boyut: **100.641.653 bayt**.
- SHA-256: **827bb9cac16fdb7b643c576a3bd41523e725ad4542ab023c5c4d45f3435b1009**.
- 1.483 ZIP üyesinin boyutu/karması önceki manifestoyla eşleşti.
- Araştırma ölçüsü: 325 farklı içerik, 512 kaynak konumu, 14 yükleme. Bunlar ZIP üyesi veya Git dosyası sayısıyla aynı ölçü değildir.
- Yayın manifestosu 125 kaynak dosyasının doğrudan veya birleştirilmiş aktarımını ve 1.358 kaynak gövdesinin yayımlanmama durumunu açıklar.

Ham arşiv özel kaynak olarak kullanılır. Hedef makinede bulunursa önce karma/boyut karşılaştırılır, repo dışında açılır ve `kaynaklar/steering/kaynaklar.json` ile kaynak kimliği eşlenir. Burada yeni hedef bilgisayara bu ham ZIP'in fiziksel olarak kopyalandığı doğrulanmamıştır. Kopyanın eksikliği, yayımlanmış raporların ve kodun okunmasını engellemez. Tam kaynak aktarımı ancak yerel dosya görülüp doğrulanınca kapanır.

## 4. Okuma ve bulgular

Son doğrudan okuma 147 ana dal dosyasının envanteri, 109 kaydın ve açıklama alanlarının bütün görünür metni, kod/ayar/istemler, 118 çağrı günlüğü, PR #2–#5 ve üç ek referans dalı üzerindeydi. Günlüklerde 92 ekleme, 25 atlama, bir JSON ayrıştırma hatası vardı. 92 dolu ham yanıt belgelenmiş metin dönüşümüyle kanonik konu/gövdeye eşleşti. Numara ve dayanak noktalaması farkları ayrıca tutuldu. Önceki 325 kaynağın tümü bu turda yeniden semantik olarak okunmuş sayılmadı.

Öne çıkan yeni bulgular:

1. k-0056'nın araç çıktısını da inceleme önerisi k-0060'ta tek kanıt ölçütü gibi daraltılmış; k-0062 düzeltiyor, k-0066 kabul ediyor.
2. k-0076 ve k-0081, başka katman/oturumun okumasının kendi okuması gibi sahiplenilmesini sınırlandırıyor.
3. Kayıt, katılımcı, katman ve bağımsız kanıt sayısı birbirine dönüştürülebilmiş; sonraki düzeltmeler birlikte okunmalı.
4. `bekleyenler()` kök ad, alıcı, açıklık ve en büyük yanıt numarası üzerinden çalışıyor; konu veya yeni Haluk iletisi koşulu yok.
5. `istem_kur()` rapor bağlantılarını açmıyor. Uygulamanın gönderdiği metnin kaydı, sağlayıcı/CLI'ın bütün etkili bağlamı değil.
6. Ana dalda çalışan kod, PR'daki öneri, devir belgesi ve gerçek işlem sonucu aynı statü değil.

Dayanakları ve ayrıntıları `kaynaklar/steering/depo/GUNCEL_OKUMA_2026-10-24.md` ile onun bağlı raporlarında bulunur. Önceki 19 aile incelemesinin bulguları kısa devir metniyle ikame edilmez; tam raporlar pakettedir.

## 5. Kullanıcının anlam ve kaynak ayrımları

`>` yalnız gösterme; `->` akış. Araştırma ile bağlam aktarımı ayrı. Kullanıcının O, I, 1, 0 ve Mühür ifadeleri özgün metniyle `kaynaklar/steering/ISTENEN_BAGLAM.md` içinde korunur. Yeni teknik çıkarım, kullanıcının sözü olarak yeniden etiketlenmez.

Sekiz alan: **Kaynak, Söyleyen, Özgün söz, Statü, Dönüşüm, Düzeltme, Gerçekleşme, Belirsizlik.** Kaynak arşivine girmek, hedef oturumda okunmak, geri anlatılmak ve uygulamada sonuç vermek ayrı olaylardır.

## 6. Tarihsel devir ve taslakların güncelliği

Ana köprüde `deus_ex_machina` zaten ikinci konu: menüde `#deus_ex_machina`, kuruluş kaydı k-0039. Önceki 57 Space sayfası, 62 tarayıcı kesiti ve Şaman geri anlatımına şimdi k-0111 ve [güncel kaynak devri](../../deus_ex_machina/KAYNAK_DEVRI_20261024.md) eklenmiştir. Şaman'ın bildirimi 519 benzersiz görünür mesajı kapsar: 126 kullanıcı, 393 asistan; 296 ana yol ve 223 yan dal. 80 eski defter kaydının tamamı eşlenmiştir: 71 gövde birebir, 8 kaynak kimliğiyle, 1 Markdown satır sonu farkıyla. 029–038 yalnız yan dallardadır; etkin ana yolun son kararı sayılmaz.

Bu kaynak işi tamamlanmış olarak korunur; yeniden sohbet toplama veya 80 kaydı baştan eşleme görevi açılmaz. Hedefte `KAYNAK_ALIMI_20261024.md`, `MESAJ_DOGRULAMASI.json`, `ESKI_DEFTER_KARSILASTIRMA.json`, `DOSYA_BAGLANTILARI.json`, `GUNCEL_GITHUB_KESITLERI.json` ve mevcut devam kaydından ilerlenir. 15 girdi eki ve 22 çıktı başvurusu çıkarılmış, altı yerel asıl dosya envanterde korunmuştur. Açık kalanlar bütün ek/görüntü baytları, çekirdek paket v11, oturum köprüsü ve ilgili kalan dosyalardır. Bağlantı bulundu diye bu gövdeler alınmış sayılmaz.

Bu web hazırlığı yeni kaynak devri belgesini ve k-0111'i okumuştur; özel yerel 519 mesaj gövdesini kendi çalışmasıyla yeniden aldığı veya hedef CLI'yı başlattığı iddiasını taşımaz. Gerçek Şaman kaynak bildirimi ile bu sonraki 85 dosyalık ek paketin hedefte okunma/kabul kaydı ayrı tutulur.

PR #4 güncel `99dc8a37ef158ee42ee535f631f64e136fef202a` sürümünde Şahit başlatıcısı ve çevrimdışı görev kuyruğu var. Eski `deus_ex_machina/DEVIR_DURUMU.md` içindeki `69adfbc` kontrolü tarihsel sürüme aittir; bugün başlatıcı hiç yok diye taşınmamalı. PR #5 yeni `2a68b375a09475115d526fdb7d81d24b2c523ab1` sürümünde Windows/VM başlangıç açıklaması düzeltilmiş. İkisi de bu kontrol anında taslaktı ve ana dala birleşmemişti. Güncel uçlar CLI'da yeniden kontrol edilir.

## 7. Bu oturumdan doğrulanamayanlar

Bu web yürütücüsünde Codex komutu ve Windows PowerShell yok; hedef Windows/Şaman oturumuna bağlı bir komut kanalı yok. Bu durum, k-0111'de bildirilmiş mevcut Şaman CLI çalışmasını yok saymaz. Bu web oturumu o süreci başlatmamıştır; yeni ek paketin hangi hedef oturumda okunup kabul edildiği henüz gözlenmemiştir. Zaten açık Şaman oturumu varsa önce yeni dosyalar o oturuma okutulur ve mevcut kaynak işi sürdürülür. Ayrı etkileşimli başlatıcı, yeni oturum gerekiyorsa kullanılacak alternatiftir.

Bu devir bir önceki sohbetin süreç belleğini veya model kimliğini kesintisiz sürdürdüğü iddiası değildir. Korunan şey, kullanıcı talimatı, kaynaklar, sonuçlar, kararlar ve devam edilebilir iş durumudur.

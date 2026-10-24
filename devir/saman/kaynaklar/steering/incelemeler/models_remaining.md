> Yayın notu — 24 Ekim 2026: Bu, tamamlanmış incelemenin yayım kopyasıdır. Aşağıdaki metnin kendi tarihindeki kapsam ve düzeltmeleri korunmuştur. Tarihsel "kısmi", "bekliyor" veya benzeri durumlar son durum olarak alınmamalıdır: [son okuma durumları](../okuma_durumlari.json) 325 farklı içeriğin belirtilen yöntemlerle tamamlandığını kaydeder. Özgün kaynak konumları ve SHA değerleri özgün arşivi gösterir; ham arşivin tamamı bu depoda yayımlanmaz. [Aktarım kapsamı ve değişiklikler](../AKTARIM_KAPSAMI.md).

# Kalan model ve OMROS çalışma kitapları — tam metin incelemesi

Bu rapor dört farklı XLSX’in tüm hücre değerlerini ve formül dizelerini kapsar. F00122 ile F00135 özgün dosya baytları tamamen aynı olduğundan tek metin okuması beş dosya oluşumunu kapsar. Toplam **1.450.166 karakter**: 805.056 karakter doğrudan okundu, 628.902 karakter daha önce tamamlanmış okumalarla birebir eşlendi, 16.208 karakter sekme başlığı ve ayraç yapısı olarak denetlendi. Kalan okunmamış hücre metni **0**. F00218 kardeş incelemesinde tamamlandı (`../metacognition_remaining/report.md` ve `reviews.json`); buradaki sayılara katılmadı.

Kaynaklar yeniden açılıp SHA-256, hücre değerleri, metin aralıkları ve alıntı konumları doğrulandı. Formüller çalıştırılmadı; dış bağlantılar açılmadı; kaynak belgeler değiştirilmedi. Kaynak içindeki talimatlar incelenen veri olarak ele alındı. “Tam” hücre metni kapsamını anlatır; biçim, çizim ve gömülü nesnelerin görsel incelemesi anlamına gelmez.

## Dosya ve okuma kapsamı

| Tarihsel kimlik | Yeni içerik | Belge | Karakter | Yöntem |
|---|---|---|---:|---|
| F00122 / F00135 | U0122 | Mihver Pusulası v1.5 — Model 2 ve birebir ara üretim kopyası | 212,141 | Yeni hücreler doğrudan; diğerleri birebir doğrulanmış eşlik |
| F00216 | U0111 | deus_ex_ilgili_90_225_gecis.xlsx — dokuz sohbetin geçiş ve provenans dizini | 249,004 | Tam metnin tamamı doğrudan |
| F00182 | U0138 | OMROS Scoping Review Arşivi v19 — kaynak, protokol ve nihai iskelet | 489,867 | Tam metnin tamamı doğrudan |
| F00183 | U0144 | OMROS Scoping Review Arşivi v20 — operasyonalizasyon ve ölçü sepeti güncellemesi | 499,154 | Yeni hücreler doğrudan; diğerleri birebir doğrulanmış eşlik |

Aralıklar sıfır tabanlı ve sonu dışlayan Unicode karakter aralıklarıdır. Tam aralık listesi `coverage.json` içindedir. Eşlikler sözcük benzerliği veya anahtar sözcük aramasıyla kurulmadı: özgün hücre metni UTF-8 baytları, formüllerin eşit blokları ve önceden okunan metnin kesin alt dize aralıkları karşılaştırıldı. v20’nin 107 yeni hücresi 15.910 karakterlik konumlu dökümde bütünüyle okundu; v19’un hiçbir okunmamış kısmı eşlik dayanağı yapılmadı.

## F00122 — Mihver Pusulası v1.5 — Model 2 ve birebir ara üretim kopyası

21 görünür sayfalı çalışma kitabı, dış–merkez–iç hareketini araştırma, deneme, uygulama, inceleme ve yenilenen mühür üzerinden 64 eylem adayına bağlar. Listeler, açılış ilkeleri, mimari, geçiş kapıları, altı temel, sözlük, karar protokolü ve stres kuralları aynı kullanım zincirindedir.

06_Eylem_Lab satır 6–69 içindeki adaylarda risk, kanıt, sahiplik/yetki ve altı puan için giriş beklenir. Tam altı puan olmadan ortalama açılmaz. Risk katsayıları 1 / 0,85 / 0,65 / 0,4; yetersiz ve bekleyen kanıt için ek katsayılar kullanılır. Son karar, sahip/yetki, puan tamlığı, kanıt, düşük ilke puanı, acil durum ve net skor dallarından geçer.

Çıktılar Aday Havuzunda, Dur: Sahip/Yetki eksik, Skor Bekler, Mikro-deneme + ek kanıt, İncele / Tahkik Et, Acil kısa yol + sonra mühür, Mühürlenebilir, Deneme / İyileştir ve diğer risk/meşruiyet durumlarını içerir. Sonraki adım ve geri besleme önerisi ayrı sütunlardadır.

20 aktif örnek senaryo ve 14 kontrollü kenar testi; iç/dış uyum tabloları, olgunluk hükmü, kaynak izleri ve alan rehberleri bulunur. 670 gerçek Excel formül dizesi okundu. Bu dosyada yalnız sözlü Boolean benzetme değil, girdilere bağlı hücre mantığı vardır; formüller yeniden çalıştırılmadı.

17_Olgunluk_Hukmu!B10 içindeki 97 sayısı statik atanmış bir değerlendirmedir. Örnek test girdileri ve saklanmış sonuçlar gerçek bir CLI oturumunun kabul testi sayılmaz. F00135 dosyası özgün XLSX baytlarıyla tamamen aynı olduğundan aynı okuma kapsamına bağlandı.

**Yönlendirme bakımından:** Açık karar alanları, eşikler, öneri dalları ve geri besleme düzeni aracılığıyla çalışma biçimini yönlendirir. Kendi kullanım notları skoru karar değil işaret, çıktıyı emir değil ilham ve erken uyarı olarak tanımlar. Bu, yönlendirme ile bağlayıcı yürütme arasındaki farkı dosyanın içinde görünür kılar.

**İzin ve uygulama sınırı:** Sahip/yetki alanının dolu olması gerçek kimlik, yetkilendirme veya onay kontrolü değildir. Çalışma kitabındaki kılavuz ve formüller bu inceleme sırasında talimat olarak uygulanmadı.

**Kanıt değerlendirmesi:** Üç somut tutarsızlık var: canlı laboratuvarın Eksik sahiplik değeri kontrolü test sayfalarıyla aynı değil; <3 ilke için yazılı dur kuralı formülde İncele / Tahkik Et etiketine dönüşüyor; U:V alanı rehberde formülsüz gösterilirken U gerçek formül içeriyor. Kaynakların olgunluk/uyum iddiası bu farklardan bağımsız başarı kanıtı sayılamaz.

Kaynak dayanakları: MR01, MR02, MR03, MR04, MR05, MR06, MR07, MR08, MR09, MR10, MR11.

## F00216 — deus_ex_ilgili_90_225_gecis.xlsx — dokuz sohbetin geçiş ve provenans dizini

Yedi görünür sayfa: Summary, Conversations, UserMessages, MessagesIndex, Provenance, ModelCouncil ve ResearchSources. Tam çalışma kitabı okundu. Formül bulunmuyor; değerler, sınıflandırmalar, önizlemeler ve kaynak işaretleri saklanıyor.

Dokuz sohbetin konuları teknik sorgulama çerçevesi, OMROS belge/görsel revizyonları, özel talimat analizi, OMROS–CognitiveOS ilişkisi, ham/işlenmiş veri döngüsü, Boolean ilkeleri, prototip, paket yapısı ve yanıt stratejisi. Tek konuşmanın ilerleyişi gibi birleştirilmediler.

MessagesIndex 417 mesaj önizlemesi içerir: 134 kullanıcı ve 283 asistan; 191 current_chain ve 226 off_chain. UserMessages aynı 134 kullanıcı önizlemesini ayrıca toplar. text_preview en çok 260 karakterdir; daha uzun özgün metin için uzunluk/hash alanı bulunması eksik gövdeyi sağlamaz. Dolayısıyla 9 sohbetin tamamını okudum iddiası burada kurulamaz.

Kullanıcı kılavuzu konuşma başında ChatGPT’ye yüklemek, açılış bölümünün süreçte yol göstermesi ve Sen...yap / Ben...yapacağım biçiminden Biz...yapalım biçimine geçmek istediğini anlatır. Bu, kaynağı belli ortak çalışma talebidir.

Asistan metinlerinden biri semantik etki üreten kılavuz ile dış Boolean katmanın bağlayıcı karar/uyarı kapısı olması arasında açık ayrım yapar. Başka bir önizleme 1’in mutlak doğruluk değil denetim kapısından geçiş anlamında kullanılmasını açıklar.

ModelCouncil her sohbet için PlatformArchitect, ArchiveCurator, SkepticalReviewer ve ExecutionVerifier rol etiketleriyle değerlendirme satırları taşır. Bunlar dört bağımsız modelin gerçekten çalıştığına ilişkin yürütme kaydı değildir. ResearchSources içindeki altı URL tam kaynak metin yerine bibliyografik/yöntemsel başvurudur.

**Yönlendirme bakımından:** Konuşmayı başlangıç kılavuzuyla çerçevelemek, üretim/eleme izini tutmak ve model çıktısını denetim kapısına geri döndürmek açık kullanıcı hedefi olarak görülüyor. Bunlar dosyadaki kullanıcı sözleriyle model açıklamaları ayrı tutularak okunmalıdır.

**İzin ve uygulama sınırı:** Kılavuz yükleme niyeti ya da ModelCouncil onay etiketi mevcut bir CLI oturumuna bağlam aktarıldığını veya oturumdan işlem izni alındığını göstermez.

**Kanıt değerlendirmesi:** Provenance!D1 source_entry_index0 başlığına karşın D2:D10 Boolean True türündedir; sayısal özgün giriş dizini bu sütundan geri kurulamaz. E2:E10 içindeki gate_a_passed True değerleri de saklanmış doğrulama iddiasıdır. Kaynak dosyalar/sandbox eklerinin bir bölümünün bu tabloda yalnız bağlantı veya dosya boşluğu olarak yer aldığı korunmalıdır.

Kaynak dayanakları: MR12, MR13, MR14, MR15, MR16, MR17, MR29.

## F00182 — OMROS Scoping Review Arşivi v19 — kaynak, protokol ve nihai iskelet

27 görünür sayfa ve 489.867 karakterin tamamı doğrudan okundu. 278 kaynak kartı, 110 tarama günlüğü girdisi; bilim, sanat, inanç, felsefe, tekne, idare, politika, çapraz değerlendirme ve nihai iskelet soruları ile bunların operasyonel tabloları vardır. Kaynak sayısı benzersiz makale sayısı değildir; kanonik eşlikler özellikle korunmuştur.

Ana arşivde durum, eksen, sistem öğesi, işlev, kanıt türü, Karşı_Tez, Tasarım_Sonucu, bibliyografya, erişim notu, URL, sonraki işlem ve soru kümesi bir aradadır. Bu yapı literatür yorumundan önerilen tasarım kuralına geçişi açıkça kaydeder. Makalelerin tam metinleri bu çalışma kitabının parçası değildir; burada atıf ve yorum kartları okunmuştur.

Bilim: ince anayasal omurga, orta alanda yoğun/modüler ağ ve korunan uçlar; omurga tutarlılığı, kök duyarlılığı, dal uyarlanabilirliği, ağ yoğunluğu ve uç açıklığı ölçüleri. H1–H6, ters-U yoğunluk, öğrenme, hata yayılımı, özerklik/rol açıklığı ve hesap verebilirlik üzerine sınanacak hipotezlerdir.

Sanat: dengeli asimetri, kökten dala değişen biçim, boşluk ve uç çevresindeki tampon; eskiz, heykel/model, tekstil, veri görselleştirme, performans ve ses yolları. Görsel yoğunluk eşiği ve kullanıcı/göz izleme önerileri ölçülmüş sonuç olarak sunulamaz.

İnanç: emanet/adalet, ihsan/hizmet, tevazu/sebat; niyet, teyit, istişare, murakabe, muhasebe ve telafi. Dış gözlem ile iç tepki/yanlılık kaydını ayırır; ham tanıklık, korunmuş itiraz ve misillemesiz uyarı için pratikler önerir.

Felsefe: süreç ve ilişki önceliğiyle birlikte hak, rol, kayıt ve temyiz gibi asgarî omurga; merkez/yerel/veri/hukuk hakkındaki varsayımları askıya alma; betimleme, hipotez, küçük test, karar veya seviye değişimi. Meşruiyet/adalet, doğruluk/geçerlilik, fayda ve estetik aynı puanda eritilmez.

Tekne: ham kayıt ve provenans zarfına ek structured handoff; kararın kısa eylem, gerekçe, belirsizlik, sınır ve escalation parçaları; yerel/çevrimdışı kayıt, aşamalı ayrıntı, SLO, hata bütçesi, bakım emeği ve hata hücresi. Handoff sadakati, çevrimdışı süreklilik, bildirim yükü ve hata yayılımı için dört deney önerilir; deney sonuçları bulunmaz.

İdare: yetki, dosya, veri/olgu, dinlenilme, karşı görüş, uzmanlık, hak etkisi, oranlılık, gerekçe, bildirim ve review sıralaması. İstatistik, saha anlatısı, meslek bilgisi, karşı görüş, yerel norm ve önceki karar farklı kanıt kanalları olarak tutulur. Yerel normun varlığı onu kendiliğinden bağlayıcı kılmaz.

Politika: anayasal çoğul ortak iyi, meşru çatışma, kamusal forum çeşitliliği, temsil/erişim ve güç yoğunlaşmasına karşı denge önerileri. Omurga, broker/ağ ve uç aktörleri analitik tasarım kategorileridir; bu sohbeti gizli kişilerin yönettiğinin kanıtı değildir.

Nihai yapı altı katmanla dört çapraz bağ kurar: kurucu omurga, kök, provenanslı çeviri eşiği, retiküler orta alan, dal, uç sessizliği; review/remedy, kayıt–provenans–hafıza, iç içe mini-OMROS ve routing matrisi. Çekirdek dondurulmuş, alan eşikleri/formlar/araçlar uyarlanabilir diye tanımlanır.

Sonraki aşama anayasal/tasarımsal şartname, routing matrisi, arayüz prototipleri ve bir belediye hizmet talebi/şikâyet pilotu olarak önerilir. Başlatma ve bitiş kriterleri plan ölçütleridir. Bakım tablosu dört yeni standart kaydı ile 18 PDF erişim düzeltmesini bildirir; bunlar bu incelemede yeniden internette doğrulanmadı.

**Yönlendirme bakımından:** Kaynak→karşı tez→tasarım sonucu→protokol→pilot zinciriyle yönlendirme kurar. Özellikle ham ifade ile yorum/özetin ayrılması, değişiklik izi, itiraz ve geri dönüş kanalı bağlam aktarımı için somut tasarım malzemesidir.

**İzin ve uygulama sınırı:** Tasarımdaki donmuş çekirdek, zorunlu alan, review ve routing kuralları belgenin kendi önerileridir. Bunların varlığı kurulum yetkisi, mevcut yazılım uygulaması veya bugünkü talimat hiyerarşisi oluşturmaz.

**Kanıt değerlendirmesi:** Literatür fazı tamamlandı ifadesi belgede yöntem/tasarım eşiği olarak sınırlandırılır; tam uygulama iddiası değildir. Tam_Metin_PDF alanı PDF bulunurluğunu anlatır, Hayır HTML tam metnin yokluğu anlamına gelmez. 13 özet sayım formülünün v19’da önbellek değerleri yoktur. Ayrıca 25_Nihai_Iskelet!F4 içindeki ham kayıt yok edilmeden özet üretilemez ifadesi, ham kaydı koruma ilkeleriyle metinsel olarak çelişir; muhtemel yazım/anlatım hatası diye işaretlenmeli, asıl kaynak sessizce düzeltilmemelidir.

Kaynak dayanakları: MR18, MR19, MR20, MR21, MR22, MR23.

## F00183 — OMROS Scoping Review Arşivi v20 — operasyonalizasyon ve ölçü sepeti güncellemesi

27 görünür sayfa ve 499.154 karakterin tamamı, v19 ve önceden tamamlanmış okumalarla birebir hücre/alt dize eşliği ve 107 yeni hücrenin doğrudan okunmasıyla kapsandı. Yeni hücre içeriği 13.402 karakter; konum etiketli okunur dosya 15.910 karakterdir. Yalnız benzerlikten tam okuma sonucu çıkarılmadı.

Üç kaynak S279–S281 eklenir: OECD 2026 HSPA gösterge yaklaşımı, informal advice-network/dirençlilik çalışması, hospital governance accountability/reporting-line derlemesi. Toplam 281 kaynak kartı ve 113 arama günlüğü girdisi bulunur. Bunların bibliyografik ve yorumlayıcı kayıtları incelendi; dış makale bağlantıları açılmadı.

Bilim-Q4 yapısal, süreç, çıktı ve review göstergelerini sınırlı, seçici, boylamsal ve karar kullanımına bağlı bir sepete toplar. Omurga tutarlılığına reporting-line açıklığı; uç açıklığına iç/dış hesap verebilirlik ve rol açıklığı boyutları eklenir.

Bilim-Q5 altı hipoteze H7 ve H8’i ekler. H7 formal omurga ve informal danışma ağlarını birlikte ölçmenin öğrenme/dirençliliği daha iyi açıklamasını; H8 açık reporting line ve hibrit hesap verebilirliğin escalation hatası/rol belirsizliğini azaltmasını sınamayı önerir. BO006, BO107 ve BO108 satırları bu yeni ölçü/hipotezleri işletim planına bağlar.

Arşiv bakım tablosuna altı kayıt eklenir. Diğer alanların mimari çekirdeği v19 ile aynıdır. İki sekmedeki 27 None→boş dize değişikliği yeni anlamlı metin değildir; veri düzeyi farkı olarak doğrulandı.

Aynı 13 sayım formülünde bu sürümde saklanmış önbellek sonuçları vardır: toplam 281, PDF Evet 204, Hayır 77. Bunlar gerçek Excel değer önbelleğidir; bu incelemede yeniden hesaplama veya dış kaynak erişim testi yapılmadı.

**Yönlendirme bakımından:** Soru ve göstergelerin seçimini değiştirerek değerlendirmeyi yönlendirir: yalnız resmî organigram yerine görünür raporlama ve informal bilgi akışı; yalnız çıktı yerine süreç ve itiraz/düzeltme ölçümü. Bunlar planlanan araştırma değişkenleridir.

**İzin ve uygulama sınırı:** BO107 notundaki gizli/informal bağlar örgüt içi resmî olmayan danışma ilişkileri bağlamındadır; sohbeti yöneten gizli kişiler veya platformun gizli çalışma biçimi sonucuna dayanak oluşturmaz.

**Kanıt değerlendirmesi:** H7/H8 ölçülmüş OMROS sonucu değildir. S280 erişim notu HTML tam metin/PDF bağlantısı bulunsa da bu turda PDF doğrulaması yapılmadığını açıkça söyler. Ham kaydın yok edilmesini ima eden F4 cümlesi v19’dan aynen taşınmıştır; tutarsızlık bu sürümde de sürer.

Kaynak dayanakları: MR24, MR25, MR26, MR27, MR28.

## Aktarıma doğrudan etki eden somut bulgular

### MR-F1 — Kılavuz, hücre motoru ve çalışan CLI üç ayrı kanıt düzeyidir

F00216 kullanıcı kılavuzuyla konuşmayı çerçeveleme niyetini kaydeder. F00122 gerçek hücre formülleri içerir. Bu kaynakların hiçbiri CLI aktarımı, bağlamın oturumda gerçekten tüketilmesi veya canlı davranış değişikliğinin bağımsız kaydı değildir. Kaynak: MR01, MR02, MR12, MR13, MR14.

### MR-F2 — Mihver laboratuvarı ile testlerin Eksik sahiplik kontrolü ayrışıyor

06_Eylem_Lab!S6 H6 boşluğunu kontrol ederken 08!T6 ve 16!T5 boş veya Eksik değerini kontrol ediyor. 99_Listeler!K7 Eksik seçeneğidir. Testteki geçiş etiketi canlı laboratuvarda aynı sahiplik kuralının işlendiğini kanıtlamaz. Kaynak: MR03, MR04, MR05, MR06.

### MR-F3 — Dur ve İncele etiketleri eşlenmeden kural taşınmamalı

07_Karar_Protokolu!F10 meşruiyet/kristalizasyon <3 için dur der; formül herhangi temel puan <3 durumunda İncele / Tahkik Et üretir. Bu iş akışı durumlarının eşdeğer olup olmadığı belgede açık olmalıdır. Kaynak: MR03, MR07.

### MR-F4 — Geri besleme alanının yazılabilirlik rehberi formülle çelişiyor

19_Calistirma_Rehberi!A19:C19, 06_Eylem_Lab U:V için formül yok der; U6:U69 gerçek formüllerdir. Kullanıcı girişi ile üretilen önerinin ayrılması gerekir. İnceleme sırasında hücreler değiştirilmedi. Kaynak: MR08, MR09, MR10.

### MR-F5 — Geçiş dizini tam sohbet gövdelerini içermiyor

417 mesajın her biri en çok 260 karakterlik önizleme taşıyor. Hash ve uzunluk alanları tam gövde yerine geçmez; current_chain/off_chain ayrımı korunmalıdır. Kaynak: MR12, MR13, MR14.

### MR-F6 — Provenance giriş indeksi Boolean türüne dönüşmüş

source_entry_index0 D sütununda dokuz satırın tamamı Boolean True; gerçek sıfır tabanlı kaynak dizini kaybolmuş. E sütunundaki gate_a_passed True tek başına bağımsız doğrulama değildir. Kaynak: MR15, MR16, MR17.

### MR-F7 — OMROS özet cümlesi ham kaydı koruma ilkesiyle çelişiyor

v19 ve v20 25_Nihai_Iskelet!F4 aynı ifadeyi taşır: Sinyal sıkıştırması yalnız burada yapılır; ham kayıt yok edilmeden özet üretilemez. Sözcüğü sözcüğüne okuma ham kaydı yok etmeyi önkoşul yaparken 15_Tekne tablosu bozulmadan saklama ve ham kayda ek kart ister. Olası anlatım/yazım hatasıdır; hangisinin amaçlandığı kaynağa açık düzeltme olarak işlenmeden otomatik yürütme kuralına çevrilmemelidir. Kaynak: MR18, MR19, MR20, MR24.

### MR-F8 — Literatür ve pilot durumları ayrı tutulmalı

Tamamlandı ve donduruldu ifadeleri arşiv içindeki yöntem/tasarım kararıdır. Kaynak notları erişim sınırlılıklarını korur; önerilen pilot ve hipotezler çalıştırılmış sonuç değildir. Kaynak: MR21, MR22, MR23, MR25, MR27.

### MR-F9 — Formal ve informal ağ anlatısı kişisel gizli yöneticiler kanıtı değildir

v20’deki gizli/informal bağlar notunun komşu hücreleri advice-network araştırmasını, ERGM ve örgütsel öğrenme hipotezini tanımlar. Buradan mevcut sohbetin görünmeyen kişilerce yönlendirildiği sonucu çıkmaz. Kaynak: MR25, MR26.

## Alıntıların ve özgün dosyaların konumu

Aşağıdaki kimlikler `quote_evidence.json` içinde tam hücre değeri, veri türü, kaynak SHA-256, metin SHA-256 ve karakter aralığına bağlıdır. Alıntılar gerçek XLSX yeniden açılarak doğrulandı. Uzun formüller ayrı kanıt dosyasında eksiksiz bulunur.

| Kanıt | Kaynak | Hücre |
|---|---|---|
| MR01 | F00122 | 10_Kullanim!C10 |
| MR02 | F00122 | 10_Kullanim!C11 |
| MR03 | F00122 | 06_Eylem_Lab!S6 |
| MR04 | F00122 | 08_Test_Senaryolari!T6 |
| MR05 | F00122 | 16_Deneme_Test!T5 |
| MR06 | F00122 | 15_Dahili_Sim_Test!E9 |
| MR07 | F00122 | 07_Karar_Protokolu!F10 |
| MR08 | F00122 | 19_Calistirma_Rehberi!A19 |
| MR09 | F00122 | 19_Calistirma_Rehberi!C19 |
| MR10 | F00122 | 06_Eylem_Lab!U6 |
| MR11 | F00122 | 17_Olgunluk_Hukmu!B10 |
| MR12 | F00216 | MessagesIndex!I339 |
| MR13 | F00216 | MessagesIndex!I364 |
| MR14 | F00216 | MessagesIndex!I373 |
| MR15 | F00216 | Provenance!D1 |
| MR16 | F00216 | Provenance!D2 |
| MR17 | F00216 | Provenance!E2 |
| MR18 | F00182 | 15_Tekne_Arayuz_Esik_Deney!D2 |
| MR19 | F00182 | 15_Tekne_Arayuz_Esik_Deney!D3 |
| MR20 | F00182 | 25_Nihai_Iskelet!F4 |
| MR21 | F00182 | 22_Literatur_Denetimi!I2 |
| MR22 | F00182 | 22_Literatur_Denetimi!F4 |
| MR23 | F00182 | 25_Nihai_Iskelet!J11 |
| MR24 | F00183 | 25_Nihai_Iskelet!F4 |
| MR25 | F00183 | 04_Bilim_Yanitlari!C6 |
| MR26 | F00183 | 05_Bilim_Operasyonalizasyon!J14 |
| MR27 | F00183 | 01_Arsiv!P281 |
| MR28 | F00183 | 05_Bilim_Operasyonalizasyon!D7 |
| MR29 | F00216 | MessagesIndex!I294 |

### Kaynak kimlikleri

**F00122** — `6ace90b4c8324256d6ab2473d6cf8dcb851b4ef8e25e07c65698a2dcd8881fb6`

Özgün: `[ARSIV_KOKU]/deus_ex_machina_kaynak_agaci/00_Kok_Uclari/01_Acilmis_Kaynaklar/P04/deus_ex_machina — Tarihsel Kaynak Koleksiyonu/01 — Kurucu Zemin — Şeyleri Şey Yapanlar/02 — Kaynak ve Model Dosyaları/21 — model_2_mihver_pusulasi.xlsx`

Okuma kopyası: `[ARSIV_KOKU]/deus_ex_machina_kaynak_agaci/02_Govde/Okuma_Kopyalari/6ace90b4c8324256d6ab.txt`

**F00216** — `31d9c8dca44a86ea2e15dcdb6d7ccdbeff6eb3f5b80226f20c549625fc6bafbe`

Özgün: `[ARSIV_KOKU]/deus_ex_machina_kaynak_agaci/00_Kok_Uclari/01_Acilmis_Kaynaklar/P04/deus_ex_machina — Tarihsel Kaynak Koleksiyonu/03 — Öncüller — Atalar/04 — Arşiv ve Model Dosyaları/02 — deus_ex_ilgili_90_225_gecis.xlsx`

Okuma kopyası: `[ARSIV_KOKU]/deus_ex_machina_kaynak_agaci/02_Govde/Okuma_Kopyalari/31d9c8dca44a86ea2e15.txt`

**F00182** — `552343b0881b1f1471527059b498a7a599da9392988549955472e94d6a2cebdd`

Özgün: `[ARSIV_KOKU]/deus_ex_machina_kaynak_agaci/00_Kok_Uclari/01_Acilmis_Kaynaklar/P04/deus_ex_machina — Tarihsel Kaynak Koleksiyonu/03 — Öncüller — Atalar/01 — Güçlü Kavramsal Atalar/07 — OMROS_scoping_arsiv_v19.xlsx`

Okuma kopyası: `[ARSIV_KOKU]/deus_ex_machina_kaynak_agaci/02_Govde/Okuma_Kopyalari/552343b0881b1f147152.txt`

**F00183** — `4c9068e2738320ce84e12a25ca2c073092a3cab21acd682dac7b104525d7eeb9`

Özgün: `[ARSIV_KOKU]/deus_ex_machina_kaynak_agaci/00_Kok_Uclari/01_Acilmis_Kaynaklar/P04/deus_ex_machina — Tarihsel Kaynak Koleksiyonu/03 — Öncüller — Atalar/01 — Güçlü Kavramsal Atalar/08 — OMROS_scoping_arsiv_v20.xlsx`

Okuma kopyası: `[ARSIV_KOKU]/deus_ex_machina_kaynak_agaci/02_Govde/Okuma_Kopyalari/4c9068e2738320ce84e1.txt`

## Bağlam aktarımı için bu belgelerden çıkan ayrım

Bu koleksiyon, yönlendirmeyi yalnız bir gizli teknik ayar anlamında kullanmıyor. Kılavuzun başlangıçta neyi öncelikli saydırdığı, soruların hangi sırada sorulduğu, hangi kanıtın korunup hangisinin özete dönüştürüldüğü, bir kararın ne zaman bekletildiği ve geri dönüşün nereye kaydedildiği de açık çalışma tasarımıdır. F00216 bu kılavuz niyetini kullanıcı sözleriyle; Mihver hücre formülleriyle; OMROS ise kaynak, karşı tez, protokol ve pilot zinciriyle görünür kılıyor.

CLI aktarımının kanıtı bundan ayrı tutulmalıdır: kaynak paketin hazırlanması, bir oturuma verilmesi, oturumun hangi parçayı nasıl okuduğunu geri aktarması ve sonuçta hangi davranışın gözlendiği ayrı olaylardır. Bu dört çalışma kitabında son iki olayın bağımsız yürütme izi yoktur. Korunması gereken aktarım malzemesi özgün ifade, konuşmacı/rol, sürüm, kaynak konumu, açıklanmış yorum ve henüz çözümlenmemiş tutarsızlıklardır.

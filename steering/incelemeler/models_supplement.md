> Yayın notu — 24 Ekim 2026: Bu, tamamlanmış incelemenin yayım kopyasıdır. Aşağıdaki metnin kendi tarihindeki kapsam ve düzeltmeleri korunmuştur. Tarihsel "kısmi", "bekliyor" veya benzeri durumlar son durum olarak alınmamalıdır: [son okuma durumları](../okuma_durumlari.json) 325 farklı içeriğin belirtilen yöntemlerle tamamlandığını kaydeder. Özgün kaynak konumları ve SHA değerleri özgün arşivi gösterir; ham arşivin tamamı bu depoda yayımlanmaz. [Aktarım kapsamı ve değişiklikler](../AKTARIM_KAPSAMI.md).

# Ek model, kural ve süreç belgeleri — kaynak okuması

Bu inceleme **11 özgün belgeyi** kapsar: on XLSX çalışma kitabı ve bir Markdown arşivi. Yazılı yönlendirme niyeti kaynaklarda açık biçimde görülür. `gpt_özel_talimatlar` bölümleri davranış kılavuzu ister; Final Human + Machine kitapları bunu kilit, tetikleyici, koşul, insan talimatı ve makine talimatı alanlarına taşır. Bu içeriğin varlığı ile bir CLI oturumunda gerçekten yüklenip uygulanması ayrı kanıt düzeyleridir.

Toplam **334.207 karakter** kapsam içindedir: **267.386 doğrudan okunan**, **66.821 daha önce doğrudan okunan parçalarla tam bayt eşliği doğrulanan** karakter. Okunmamış metin aralığı yoktur. Tekrar kapsamı her bloğun tam bayt karşılaştırması ve hedef metnin eksiksiz yeniden birleştirilmesiyle doğrulandı. XLSX kaynakları aynı hücre okuma yöntemiyle yeniden çıkarıldı; onunda da katalog okuma metni birebir elde edildi. Gizli sekmeler de okundu. Bu kapsam, hücre değerleri ve formül metinleridir; görsel biçim veya gömülü nesnelerin ayrıca incelendiği iddia edilmez.

Windows masaüstü veya Notepad++ kullanılmadı. Formüller yeniden hesaplanmadı; kaydedilmiş formül önbellekleri ayrı alan olarak okundu. Kaynak komutları çalıştırılmadı, kaynak dosyalar değiştirilmedi. F kimlikleri tarihsel `corpus_prepared.json` kataloğuna aittir. Yeni dönüşüm paketinde kaynak konumları E, farklı içerikler U ile numaralanır; eşleme yalnız özgün kaynak SHA-256 üzerinden yapıldı.

## Okuma kapsamı

| Tarihsel kimlik | Belge | Karakter | Doğrudan | Birebir blok | Sekme / formül |
|---|---|---:|---:|---:|---|
| F00104 | Model 4 — Şey’in Koordinat Grameri — erken XLSX | 18872 | 18872 | 0 | 10 / 10 |
| F00113 | İlham Kulvarları Arşivi v0.1 — Markdown | 19149 | 19149 | 0 | Markdown |
| F00116 | CORE 02 — Yöntem ve Veri Seti Arşivi | 21193 | 20600 | 593 | 12 / 0 |
| F00102 | Φ_ex_Machina — erken arşiv/operatör çalışma kitabı | 22224 | 22224 | 0 | 10 / 10 |
| F00115 | CORE 01 — 32 Kapı Arşivi | 22379 | 22379 | 0 | 12 / 0 |
| F00136 | Mihver Pusulası — Süreç Arşivi v1.0 | 26270 | 26270 | 0 | 11 / 5 |
| F00124 | Model 2 — Mihver Pusulası — Final Human + Machine | 38569 | 16493 | 22076 | 24 / 24 |
| F00128 | Model 3 — Φ_ex_Machina — Final Human + Machine | 39214 | 17138 | 22076 | 24 / 24 |
| F00119 | Model 1 — Tahkikat/Denetim — Final Human + Machine | 39846 | 17770 | 22076 | 24 / 24 |
| F00106 | Model 4 — Şey’in Koordinat Grameri — Final Human + Machine | 41286 | 41286 | 0 | 24 / 24 |
| F00134 | Model 1 — GPT Özel Talimatlar — erken XLSX | 45205 | 45205 | 0 | 7 / 4 |

F00124, F00128 ve F00119 ortak parçalarını tam okunan F00106 ile; F00116 ise ortak 593 karakterini tam okunan F00115 ile paylaşır. Diğer belgeler baştan sona doğrudan okundu. Karakter/bayt/satır aralıkları `reading_coverage.json` ve `exact_block_mapping.json` içindedir. Kaynak SHA-256, özgün yol, okuma metni yolu ve yeni paketin içerik kimlikleri her belge için `reviews.json` içinde bulunur.

## Belgeler tek tek

### F00104 — Model 4 — Şey’in Koordinat Grameri — erken XLSX

Dokuz kök soruyu sabitleme, hareket ve yön katmanlarında düzenler. Geometri, matematik ve dilbilim karşılıklarını; boş uygulama alanlarını; astroloji, tohum, öfke, okul, akıllı telefon, adalet ve deprem için yedi örnek ile 63 soru-cevap satırını taşır. Gölge sorular tanım, bağlam, ölçüt, kaynak/neden ve amaç/yön karışmalarını sınar. Doğal olaya ahlaki amaç yüklememek ve yönü kader saymamak açık sınırlarındandır.

**Yönlendirme:** Yanıtın hangi sorulardan geçeceğini ve hangi bozulmada gölge soruya döneceğini belirleyen soru mimarisi. Kontrol ile kılavuzluğu ayırır.

**İzin ve kanıt ayrımı:** Model yöntemsel kılavuz olarak sunulur; dosya üzerinde yazılı olması herhangi bir CLI üzerinde işlem izni vermez. Model çalışır cümlesi 63 örnek satırda saklanan değerlendirmedir. On gerçek Excel formülünün yapısal sayım/IF kontrolleri anlamsal başarı ölçümü değildir.

Kaynak konumları: `SUP-M4-PROTO-CLAIM`, `SUP-M4-COUNTS` (`quote_evidence.json` içinde özgün hücre/satır, değer, veri türü ve kaynak SHA-256).

### F00113 — İlham Kulvarları Arşivi v0.1 — Markdown

Arşiv manifesti, kavram haritası, on iki kulvar, VFR süreç sözlüğü ve gpt_özel_talimatlar bölümünü bir arada taşır. Beden, dil, bellek, bilim, felsefe, sanat, inanç, etik, teknik, hukuk, ekonomi ve ortak hayat alanları karşılıklı metot/veri incelemesine açılır. Muvâcehe, tecelli ve inkişaf terimleri süreçteki karşılaşma, görünürlük ve açılma işlevleriyle tanımlanır. Fiziksel titreşim ölçümü sunmaz.

**Yönlendirme:** Özel talimat/davranış kılavuzu olma niyeti doğrudan yazılıdır. Kaynak, belirsizlik, itiraz, sorumluluk, üretim/tasfiye izi ve yeni veriye açıklık üzerinden 1/0 kuralları kurar. Gizli düşünce dökümü yerine kısa gerekçe, karar izi ve varsayım-sınır özeti ister.

**İzin ve kanıt ayrımı:** Buradaki emir cümleleri incelenen kaynak içeriğidir. Güncel asistanın ayarlarının değiştiği, bu metnin CLIye kurulduğu veya kullanıcıdan bağımsız yetki doğduğu gösterilmez. Sahte kesinlik kadar yapay belirsizliği de reddeder; itirazı kişi yerine yöntem ve çıkarıma yöneltir. Dosya adlarını anması o dosyaların gerçekten bu belgede gömülü olduğu anlamına gelmez.

Kaynak konumları: `SUP-INSTRUCTION` (`quote_evidence.json` içinde özgün hücre/satır, değer, veri türü ve kaynak SHA-256).

### F00116 — CORE 02 — Yöntem ve Veri Seti Arşivi

Dört model için toplam 31 yöntemin amacı, girdisi, çıktısı ve gerekli kilitlerini birleştirir. M4te yedi; M1, M2 ve M3te sekizer yöntem vardır. Veri seti kaydı, yöntem/veri eşlemesi, modele ayrılmış yöntem sekmeleri, ortak yöntem/veri şablonları, dört dolu örnek ve QA beyanlarıyla tamamlanır.

**Yönlendirme:** Davranış yönergesini alan isimleri, model kimlikleri, gerekli kilitler ve girdi/çıktı sözleşmeleri düzeyine taşır. Bu hücreler çalışma motoru değildir; dosyada gerçek Excel formülü yoktur.

**İzin ve kanıt ayrımı:** Gerekli kilit isimleri uygulama için denetim taslağıdır. İzin veren canlı otorite veya güncel onay kaydı gösterilmez. 03_Method_Dataset_Map F4te required_locks derken F5te amaç metni, G5te kilit kimlikleri bulunur; G4 boştur. Makineye başlıkla aktarım için somut şema sorunudur. Örnek doldurulmuş kayıtlar ve QA TRUE değerleri gerçek çalıştırmayla karıştırılmamalıdır.

Kaynak konumları: `SUP-CORE02-HEADER`, `SUP-CORE02-EXAMPLE` (`quote_evidence.json` içinde özgün hücre/satır, değer, veri türü ve kaynak SHA-256).

### F00102 — Φ_ex_Machina — erken arşiv/operatör çalışma kitabı

Ham veri, anlama, ön işleme, analiz, taslak, üretim ve izleme yaşam döngüsünü sekiz satırlık matrise kurar. Beş soru, sekiz oran ailesi, geometrik hücreler, operatör isimleri ve V1–V4 kaynak/ölçüm/risk/yetki sınırları arka sekmelerdedir. Görünür boş matris, örnek senaryo, denetim raporu ve son gözden geçirme bölümleri bulunur.

**Yönlendirme:** Görünür çalışma yüzü ile arka yöntem iskeletini ayıran tasarım. Beş veryHidden sekmenin varlığı dosyanın gerçek sunum özelliğidir; gizli kişiler veya dışarıdan kontrol iddiası değildir. Çok sayıdaki işlev adı birer metin kaydıdır.

**İzin ve kanıt ayrımı:** V3/V4te yetki temeli, yayımlayan ve iptal gibi alan adları tasarlanır. Alan tasarlamak yetki veya imzalı kanıt üretmekle aynı şey değildir. PASS_WITH_WARNINGS ve önceki test sonuçları kaydedilmiş beyanlardır. Kaynak kendi PROV yapısını kavramsal sayar ve bu XLSXte derin JSON Schema doğrulaması bulunmadığını belirtir. veryHidden şifreleme olarak sunulmaz.

Kaynak konumları: `SUP-PHI-REVIEW`, `SUP-PHI-SHEET-STATE` (`quote_evidence.json` içinde özgün hücre/satır, değer, veri türü ve kaynak SHA-256).

### F00115 — CORE 01 — 32 Kapı Arşivi

Otuz iki tematik kapı, altı ilke, varlık/bilgi/değer ayrımı, VFR, on iki ilham kulvarı, iç/dış dünya ilişkisi, dört modele etkiler, tasfiye ve açık kalan konuların kayıtlarını toplar. Son iki kapı VFR ve İlham Kulvarlarıdır. Her kapıyı risk ve eklenecek kilitlerle ilişkiler.

**Yönlendirme:** Kapı, bir yorumun hangi ayrımdan ve kontrolden geçeceğini belirleyen kavramsal yönlendirme unsurudur. İç hesap/veri/ağ temsilini dış dünyanın yerine geçirmeyi açıkça reddeder.

**İzin ve kanıt ayrımı:** Tasfiye/do_not_reintroduce işaretleri önerilen yöntemin tekrar kurallarıdır; uygulamadaki erişim denetimi veya kullanıcı yetkilendirmesi değildir. On iki sekme ve sıfır formül kaynakta doğrulanır. QA TRUE ve formula scan completed yazıları string kayıtlar olup tarihte gerçekten hangi denetimin çalıştığını tek başına kanıtlamaz.

Kaynak konumları: `SUP-CORE01-REPRESENTATION`, `SUP-CORE01-QA` (`quote_evidence.json` içinde özgün hücre/satır, değer, veri türü ve kaynak SHA-256).

### F00136 — Mihver Pusulası — Süreç Arşivi v1.0

Dış–Mihver–İç mimarisini, iki geçiş kapısını, bir üst ilke ve altı ilkeyi, 16 karar/çıktı özeti, 64 eylem adayı, 20 senaryo ve v0.1–v1.5 sürüm yolunu arşivler. Dış araştırma/deneme/uygulama ile iç inceleme/tahkikat/muhakemeyi kalibrasyonda buluşturur. Python/JSON/JSONL/SQLite paket haritası, çalıştırma komutları, dış kaynak listesi ve kavram sözlüğü içerir.

**Yönlendirme:** Eylemi bağlam, risk, kanıt, sahip/yetki ve ilke skorları üzerinden seçmeye yöneltir; yüksek riskte kapsam küçültme, eksik yetkide durma, acilde zarar azaltma sonrası kayıt gibi karar adlarını taşır.

**İzin ve kanıt ayrımı:** Sahip/yetki meşruiyet ölçütüdür. 01_Surecteki gizli arşiv isteği tarihsel özet olarak korunur; bu dosyayı okumak aynı işlemi şimdi yapma emri değildir. 20 Geçti sonucu ve net puanlar saklanmış string hücrelerdir. Beş formül kapaktaki adet sayaçlarıdır. 4/4 test geçer ifadesi rehberin beklenen sonuç alanıdır; bu incelemede kod çalıştırılmadı. Süreç özeti sözcüğü sözcüğüne özgün sohbet tutanağı değildir.

Kaynak konumları: `SUP-MIHVER-ARCHIVE`, `SUP-MIHVER-TEST`, `SUP-MIHVER-COMMAND` (`quote_evidence.json` içinde özgün hücre/satır, değer, veri türü ve kaynak SHA-256).

### F00124 — Model 2 — Mihver Pusulası — Final Human + Machine

Yön, eksen, eşik, doz, bedel, zamanlama ve açık kalan konuları işler. Kontrol/kaos, yakınlık/mesafe, yardım/devir, inanç/revizyon, merhamet/sınır ve aşkınlık/içkinlik altı kalibrasyon eksenidir. İnsan rehberi ile makine şeması, kilit, protokol ve kayıt şablonlarını 24 sekmede birleştirir.

**Yönlendirme:** LOCK_DOSE ve P004 kalibrasyon adımı modelin özgül yönlendirmesidir. Dozu alt/üst sınıra göre değerlendirme bir kural metni olarak yazılır. Sağlıklı dengeyi otomatik orta nokta saymaz; geçici desteğin geri çekilmesini içerir.

**İzin ve kanıt ayrımı:** Ortak LOCK_HELP_GIVE izin, doz, yetkinlik ve geri çekilmeyi sorar. Dosyadaki izin ölçütü, gerçekleşmiş kullanıcı onayı veya yürütme yetkisi değildir. RUN_001 placeholder/not_started; puanlar önceden 1dir. K2/K5 önbellekleri 1/passed olsa da K5 yalnız eşik karşılaştırır; kritik hata ve başlatılma durumunu hesaba katmaz.

Kaynak konumları: `F00124-LOCK`, `F00124-PROTOCOL`, `F00124-RUN`, `F00124-SCORE` (`quote_evidence.json` içinde özgün hücre/satır, değer, veri türü ve kaynak SHA-256).

### F00128 — Model 3 — Φ_ex_Machina — Final Human + Machine

Kaynak biçimi, hedef biçimi, dönüşüm, korunan özellik, kayıp, bozulma ve açık kalan konular çekirdeğidir. Metinden XLSXe, kavramdan operatöre ve dış kaynaktan kilide beş dönüşüm örneği; kaybolan nüans ve geri dönüş derecesiyle birlikte verilir. 24 sekmelik insan/makine yapısı diğer modellerle ortaktır.

**Yönlendirme:** LOCK_INVARIANT ve P004 dönüşüm/sabit özellik testi, dönüşüm sırasında neyin korunduğunu görünür kılmayı ister. Kayıp ve bozulmayı saklamama, geri dönüş ve tortu kaydı modelin özel yönlendirmesidir.

**İzin ve kanıt ayrımı:** Biçimler arasında dönüşüm tasarlamak kaynak üzerindeki hakları veya araç yetkisini kendiliğinden yaratmaz. Ortak yardım/izin kilidi normatif çerçevedir. Beş dönüşüm örneği örnek kayıt niteliğindedir. RUN_001 çalıştırılmamıştır; önceden dolu skor/önbellekler uygulama başarısı sayılmaz. K5 kritik hata hücresini izlemez.

Kaynak konumları: `F00128-LOCK`, `F00128-PROTOCOL`, `F00128-RUN`, `F00128-SCORE` (`quote_evidence.json` içinde özgün hücre/satır, değer, veri türü ve kaynak SHA-256).

### F00119 — Model 1 — Tahkikat/Denetim — Final Human + Machine

Anlama, kaynak teması, belirsizliğin görünürlüğü, itiraza açıklık, sorumluluk, üretim izi ve açık kalan konuları işler. Sekiz boolean kontrol, 31 kilit, yedi protokol adımı ve ortak giriş/çalışma/puan/karar şablonlarıyla cevap denetimini alanlara ayırır.

**Yönlendirme:** LOCK_NO_FINAL ve P004 audit gates, yanıtın değişmez hüküm olmamasını yönlendirir. Kişiyi hedef alan itirazı ve aşırı kuşkudan karar verememeyi iki ayrı bozulma olarak tanımlar.

**İzin ve kanıt ayrımı:** Denetim görevi sınırsız kişisel otoriteye çevrilmez. İzin ve geri çekilme ortak yardım kilidinin konusudur; güncel erişim izni ayrıca gerekir. Beklenen 1/0 değerleri ve çıktı örneğinde quality_score gibi sayılar tamamlanmış çalışmanın ölçümü değildir. RUN_001 not_started; K5in passed önbelleği başlangıç puanlarına dayanır.

Kaynak konumları: `F00119-LOCK`, `F00119-PROTOCOL`, `F00119-RUN`, `F00119-SCORE` (`quote_evidence.json` içinde özgün hücre/satır, değer, veri türü ve kaynak SHA-256).

### F00106 — Model 4 — Şey’in Koordinat Grameri — Final Human + Machine

Dokuz kök soruyu varlık/bilgi/değer ve açık kalan konularla birlikte şemalaştırır. İnsan okuma yüzü, model metaverisi, çekirdek alanlar, sözlük, 31 kilit, yedi adımlı protokol, boolean kurallar, bozulmalar, çıktı örnekleri ve giriş/çalışma/karar şablonlarından oluşur. Ortak yapının tam okunan taban dosyasıdır.

**Yönlendirme:** LOCK_ROOT_QUESTION ve kök soruları uygulayan P004, şeyin tanım/yer/zaman/ölçü/kaynak/neden/yöntem/amaç/yön ayrımlarını yönlendirir. M_04te trigger/pass/fail/action, M_05te human_instruction/machine_instruction açık sütunlardır.

**İzin ve kanıt ayrımı:** Kilit matrisindeki yardım/izin, kapsülleme ve kaynak kuralları önerilen sistemin tasarımıdır. Bunların CLI oturumuna yüklenmesi veya bağlayıcı çalışması bu dosyada gözlenmez. Kaynak izinde yüksek güven ve yargıyı değiştirdi türü değerler belgenin kendi anotasyonudur. RUN_001 açık örnektir. Puan başlangıçları, eşik ve kritik hata alanı ayrı tutulmalıdır; K5 kritik hatayı kullanmaz.

Kaynak konumları: `F00106-LOCK`, `F00106-PROTOCOL`, `F00106-RUN`, `F00106-SCORE` (`quote_evidence.json` içinde özgün hücre/satır, değer, veri türü ve kaynak SHA-256).

### F00134 — Model 1 — GPT Özel Talimatlar — erken XLSX

Markdown davranış kılavuzunu yedi sekmeye dönüştürür: kimlik/amaç, 1/0 sözlüğü, üst ilke ile altı ilke, kod bloklarından ayrılan boolean satırları, on maddelik kontrol, kaynak tabloları ve 86 sıralı kaynak bloğu. Kaynak metin; ilham, denetim, gerçek dış temas, belirsizlik, sorumluluk ve revizyona açıklığı birlikte taşır.

**Yönlendirme:** Kaynak metnin amacı doğrudan yol göstermektir. Emir ve kabul/ret ifadeleriyle açık davranış tasarımı yapar; gizli iç akıl yürütme talebi yerine kısa gerekçe/karar izi ister. Boolean ifadeleri yürütülebilir Excel formülü değil string hücrelerdir.

**İzin ve kanıt ayrımı:** Özel talimatlar başlığı, bunun bir platformun gerçek ayar ekranına kaydedildiğini kanıtlamaz. İçindeki normatif istekler burada incelenen veridir. Dört gerçek Excel formülü yalnız ilke, kural, kontrol ve kaynak bloklarının adedini sayar. Kontrol listesindeki Beklenen 1/0 değerleri gerçek bir yanıtın gözlenmiş skoru değildir. Kaynak kuşku yoksa kuşku üretmeme kuralını açıkça korur.

Kaynak konumları: `SUP-M1-PURPOSE`, `SUP-M1-NOT-EXECUTABLE`, `SUP-M1-EXPECTED` (`quote_evidence.json` içinde özgün hücre/satır, değer, veri türü ve kaynak SHA-256).

## Uygulamaya aktarım açısından somut iki sorun

**Dört Final çalışma kitabının başarı kararı gerçek koşumu temsil etmiyor.** Her birinde `X_02_Run_Log!F2` “Örnek kayıt: gerçek çalıştırmada doldur.”, G2 `placeholder`, H2 `not_started` içerir. Buna karşılık `X_03_Scoring_Checklist!C2:C11` önceden sayısal 1 ile doludur. K2 formülü ağırlıklı oranı üretir; kaynakta saklanmış önbelleği 1’dir. K5 `=IF(K2>=K3,"passed","residual_open")` formülünü taşır ve önbelleği `passed`dır. K3 eşik 0.8, K4 kritik hata alanı `no`dur. K5, K4’ü veya Run_Log durumunu kullanmaz. Bu kitap makineye bağlanacaksa örnek/başlatılmamış durum, gerçek puan ve kritik hata ayrı girdiler olarak değerlendirilmelidir. Bu bir formül bağlantısı bulgusudur; dosyalarda düzeltme yapılmadı. [F00106/F00119/F00124/F00128: `*-RUN`, `*-SCORE`.]

**CORE 02’nin bir eşleme sekmesinde sütun başlığı kaymış.** `03_Method_Dataset_Map!F4` değeri `required_locks` olmasına rağmen F5 amaç cümlesidir: “Şey’in ilk adını ve ne olmadığını ayırmak”. Gerçek kilitler G5’te `LOCK_ONTOLOGY;LOCK_RESIDUAL` olarak durur; G4 boştur. Başlıkları anahtar yapan bir dönüştürücü kilit yerine amaç metnini alabilir. Diğer yöntem sekmelerindeki doğru adlandırılmış yapıyla karşılaştırılarak açık eşleme gerekir. [F00116: `SUP-CORE02-HEADER`.]

## Steering konusunda bu ek okumanın sağladığı ayrım

Buradaki yönlendirme dört görünür biçimde kuruluyor: **soru sırası**, **kabul/ret ilkesi**, **koşula bağlı işlem şeması**, **eylem seçimi ve kayıt düzeni**. “Gizli” sözcüğü bazı yerlerde arşivin konuşmaya açılmamasını, bazı yerlerde Excel’in `veryHidden` sunum durumunu, bazı yerlerde görünür kısa özetin yanında iç akıl yürütmenin ayrı kalmasını anlatıyor. Bunları tek bir gizli özne veya arka plan müdahalesi olarak birleştirecek kanıt yoktur.

Belgede bir şeyin yapılmasının istenmesi, bunun yapılmış olması değildir. `TRUE`, `1`, `passed`, `Geçti` ve mühür ifadeleri de bulundukları alana göre ölçüt, örnek, kaydedilmiş iddia, formül önbelleği veya beklenen sonuç olabilir. Bu yüzden kaynak alıntıları veri türü ve hücre/başlık konumuyla tutuldu. Bu belgeler, kullanıcının düşündüğü yönlendirme yaklaşımının nasıl yazılı ve şematik hale getirildiğini anlamaya yardımcı olur; önceki sohbetin çalışma zamanı ayarlarının değiştirildiğini veya CLI aktarımının tamamlandığını kanıtlamaz.

## Denetim dosyaları

- `reviews.json`: 11 belge, SHA üzerinden paket eşlemeleri, belge bazlı değerlendirmeler ve altı ana bulgu.
- `quote_evidence.json`: özgün kaynaklardan yeniden doğrulanan hücre/satır konumları ve veri türleri.
- `workbook_cells.json`: on çalışma kitabının hücreleri, sekme görünürlüğü, formül metni/önbelleği ve TXT satır eşlemesi.
- `mapping_checks.json`: kaynak ve okuma metni SHA doğrulamaları, varsa eski birebir kopya bağlantıları.
- `reading_coverage.json` ve `exact_block_mapping.json`: doğrudan okuma aralıkları ile birebir blok kapsamının ayrı kanıtı.

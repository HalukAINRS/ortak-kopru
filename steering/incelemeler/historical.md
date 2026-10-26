> Yayın notu — 24 Ekim 2026: Bu, tamamlanmış incelemenin yayım kopyasıdır. Aşağıdaki metnin kendi tarihindeki kapsam ve düzeltmeleri korunmuştur. Tarihsel "kısmi", "bekliyor" veya benzeri durumlar son durum olarak alınmamalıdır: [son okuma durumları](../okuma_durumlari.json) 325 farklı içeriğin belirtilen yöntemlerle tamamlandığını kaydeder. Özgün kaynak konumları ve SHA değerleri özgün arşivi gösterir; ham arşivin tamamı bu depoda yayımlanmaz. [Aktarım kapsamı ve değişiklikler](../AKTARIM_KAPSAMI.md).

# Tarihsel kaynaklar ve HalukAI evrakları: steering incelemesi

23 Ekim 2026

## Ana bulgu

Okunan belgeler, kullanıcının kavramsal anlatımının zaman içinde yorumlara, çalışma ilkelerine, rol talimatlarına ve bunları dosyalara yerleştirmeyi amaçlayan betiklere dönüştürüldüğünü gösteriyor. Bu dönüşüm belgelenebilir: kullanıcı sözü, model yorumu, `AGENTS.md`/beceri metni ve PowerShell kaydı aynı tür kanıt değildir. Bazı devir metinleri bunları tek bir “sistem kuruldu” anlatısında birleştiriyor; başka belgeler ise aynı ayrımı açıkça yeniden kuruyor. Bu nedenle dosyalarda yönlendirme metni bulunduğu sonucuna ulaşılabilir, fakat her yönlendirmenin etkin CLI tarafından okunduğu veya bütün kurulum iddialarının gerçekleştiği sonucuna bu kayıtlarla topluca ulaşılamaz. [F00023, 7–20; F00025, 97–127; F00030, 45–58; H004, 52–98; H013, 4–23]

Buradaki **steering**, somut olarak bir modelin yanıtını, görev sırasını, kaynak kullanımını veya araçla çalışma biçimini yönlendirmeyi amaçlayan metin ve ayar taslakları anlamında kullanıldı. Bir ortam değişkeninin adı, şiirsel bir anlatım veya “kilit kuruldu” yanıtı tek başına sağlayıcı düzeyinde bir mekanizma, kalıcı model değişimi ya da başka kişilerin kontrolü hakkında kanıt sayılmadı.

## Kapsam ve tamamlanma durumu

Bu rapor, kaynak ağacı kataloğundaki **227 kaydı** ve beşinci proje ZIP’i olan `HalukAI_Tam_Mimari_Ve_Sohbet_Paketi.zip` içindeki **21 dosyayı** kapsayan 248 belge kaydıyla birlikte hazırlanmıştır. İlk grubun 227 kaydı içinde 204 farklı özgün dosya SHA-256 değeri bulunuyor; bu sayı dört oturum kaydını da içeriyor. 227 kaynağın ve mevcut 204 metin eşlemesinin kayıtlı kaynak/hash bağlantıları doğrulandı. Beşinci ZIP’in 21 üyesi de arşiv üyesi, çıkarılmış kaynak ve çözümlenmiş okuma kopyası açısından karşılaştırıldı. [mapping_checks.json; halukai_mapping_checks.json]

Kaynak ağacında **183 farklı metin kopyası yolu**, **177 farklı çıkarılmış metin SHA-256 değeri** ve yol bazında toplam **22.312.157 karakter** var. Bayt boyutu 20.000’in altındaki **117 metin kopyasının tamamı** okundu. Bunlar 112 farklı metin içeriğine karşılık geliyor. Ayrıca büyük `onun_ilkeleri.md` (F00048) bütünüyle okundu. Böylece bu alt incelemede 118 kopya yolu / 113 farklı tarihsel metin / yol bazında 642.850 karakter tam okuma kapsamındadır. Kaynak tekrarlarına aktarılan durum yalnız eşit çıkarılmış metin SHA-256 değerine dayanır. [coverage.json; reviews.json]

HalukAI ZIP’inde **20 dosyanın mevcut metni tamamen**, `cli_ve_kernel_tarama.txt` dosyasının ise **4.467 satırından 345’i** yorumlayarak okundu. Son dosyada okunan aralıklar: **1–90, 850–885, 990–1050, 2930–2995, 4376–4467**. Kalan aralıklar **91–849, 886–989, 1051–2929, 2996–4375**. Beşinci ZIP’in tamamında 700.997 metin karakterinden 207.450’si bu okuma kapsamındadır. [H001–H021; coverage.json]

**Bütün evrakların tam okuması tamamlanmış değildir.** Tarihsel grupta 65 kopya yolu / 64 farklı metin içerik olarak henüz tam okunmadı. Bunların sekiz farklı Model 1–4 rehber/mimari metni ayrı incelemeye devredildi; bu rapor onları kendi okuması olarak saymıyor. HalukAI’deki kısmi kayıtla birlikte, bu raporun anlık kuyruğunda 65 farklı metnin 22.116.640 karakteri kalıyor. Mekanik başlık/rol/yapı indeksi oluşturulması, gövdenin anlamıyla okunması olarak kaydedilmedi. Sonraki ek okumalar bu kuyruğun üzerine SHA ile işlenmelidir. [reading_queue.json; all_distinct_text_coverage.json]

PDF ve DOCX dosyalarında mevcut metin çıkarımları, XLSX dosyalarında çıkarılmış hücre/formül metinleri okundu. Bu işlem sayfa görüntülerinin eksiksiz görsel denetimi veya formüllerin yeniden hesaplanması değildir. Kaynaklarda adı geçen fakat içeriği bu arşivde olmayan bir sohbet ya da ekran kaydı, yalnız atıf bulunduğu için okunmuş sayılmadı. Masaüstü veya Notepad++ üzerinde okuma yapılmadı.

## Kullanıcı sözü, yorum, yönerge ve uygulama nasıl ayrılıyor?

| Katman | Kaynaktaki örnek | Bu kaydın gösterdiği |
|---|---|---|
| Kullanıcı sözü | F00094, 34: “ben söylerim, sen alırsın” ve gerekçeli geri dönüşle ortak karara varma; F00150, 79: soru ve alternatif olmadan kullanıcı adına karar vermeme | İstenen ilişki ve çalışma yöntemi. Belgenin kendisi bunu yeni asistan yorumu veya önceden verilmiş ortak karar saymıyor. |
| Kaynağın yeniden anlatımı | F00023, 9: “Engeli, engelleme” satırlarını kilitlerin çevresinden/kökünden dolaşma stratejisine bağlama | Simgesel sözün teknik eyleme dönüştürülmüş yorumu. Bu bağlantıyı inceleme belgesi kuruyor; özgün sözün zorunlu tek anlamı veya yapılmış eylemin kanıtı değil. |
| Talimat taslağı | F00025, 97 ve 106–127; H013, 4–23 | Adlandırılmış rol, ortam değişkeni ve `AGENTS.md` metni gerçekten mevcut. |
| Yerleştirme yöntemi | H004, 72–93 | AGENTS/CLAUDE/Copilot talimatlarını belirli çalışma alanlarına yazmayı ve kopyalamayı amaçlayan kod mevcut. Kodun okunması çalıştırıldığı anlamına gelmiyor. |
| Kaydedilmiş komut/çıktı | H019, 298–716; H020, 150–154 | Birinde `Get-Content` ile eski başlatıcı kaynakları görünür; diğerinde SSH denemesinin hata çıktısı görünür. Bunlar devir anlatısından daha dar ve somut kayıtlardır. |
| Başarı anlatısı | H001, 3–79 | Kurulum ve optimizasyonların tamamlandığına ilişkin devir iddiası. Her alt iddianın ayrı sonuç veya gözlemle eşleştirilmesi gerekiyor. |

Bu ayrım yalnız sonradan eklenmiş bir eleştiri değil; arşivin içinde de açık biçimde yazılmış. Şaman Defter Köprüsü, kullanıcının aktardığı metnin okunduğunu, geçmiş işlemlerin yeniden uygulanmadığını, dosya sayıları ve sonuçların asıl kanıt görülmeden bağımsız doğrulanmış sayılamayacağını söylüyor. Aynı kaynak “tuzak”, tehdit ve dış müdahale yorumlarının aktarım tarafından kanıtlanmadığını özellikle belirtiyor. [F00030, 49–58]

## Etiketler ve kavramsal aktarım

F00019, F00020 ve özellikle F00023, dört etiketi **[ENGEL OLMAMA]**, **[ENGEL OLUŞTURMAMA]**, **[ENGELLENMEME]**, **[ENGELLEMEME]** olarak sabitliyor. Bunları **[ARAMA] → [ANLAMA] → [YAPMA] → [KANITLAMA]** dizisiyle birlikte veriyor. Bu, kullanıcının önceki `O`, `0`, `I`, `1`, “Ben/Sen”, akış ve gösterme ayrımlarından türetilmiş bir çalışma dilidir. Belgede böyle bir türetim bulunması, bütün özgün ayrımların kayıpsız korunduğunu göstermez. [F00023, 2 ve 7–10]

Örneğin “engelin korunması”, kaynakta teknik kilitlerin çevresinden dolaşma stratejisine bağlandığında yorumun nesnesi değişiyor. Özgün kavramsal ilişkiler ile BitLocker, hesap, önyükleme ve dosya sahipliği işlemleri arasında kurulan bu ilişki kaynak yazarının yorumudur. F00023’teki “tuzağı”, “bulut perdesi”, “siyah katman” ve “mühürleme” ifadeleri de bu anlatının sözleridir; tek başına tehdit veya teknik neden kanıtı olarak alınmadı. F00030 bu sınırı ayrıca düzeltiyor. [F00023, 9 ve 15–20; F00030, 54–58]

`geri_donus.py` ve `Geri_Donus_Kaynak_Kaydi.json` (S001/S003), erişilebilen 19 kullanıcı adımını yeni okuma notlarıyla birlikte koruyor. JSON’da asistan yanıt alanlarının boş olması, geçmiş karşılıklı konuşmanın tamamının bu dosyada yer aldığı şeklinde okunmamalı. Python dosyası statik olarak incelendi; gömülü söz ve yorumları çıktılayan bir araç, kendi başına CLI’lara talimat yükleyen bir altyapı değil. Bu dosya çalıştırılmadı. [S001; S003]

F00148–F00150 ise farklı kapsamlarda kullanıcı gövdeleri taşıyor: 30 kullanıcı gövdesi, 18 paragraflık yansıma/rüya metni ve 29 kullanıcı gövdesi. Asistan/araç/sistem geçmişinin çıkarıldığı yerde karşılıklı geçmiş yeniden icat edilmedi. F00094’teki “gerekçeleri ile geri gönderme / ortak karar” sözü, daha sonra yazılmış tek taraflı emir ifadelerinin otomatik kullanıcı onayı olarak alınmasını da engelliyor. [F00148–F00150; F00094, 31–39 ve 122–160]

## Modeli yönlendirmek üzere yazılmış metinler

`gpt_özel_talimatlar_v2.md` açıkça bir kılavuz olduğunu söylüyor. Kaynakla temas, denetlenebilirlik, belirsizlik, gerektiğinde yön değiştirme, kısa gerekçe özeti, karar izi ve varsayım/sınır açıklaması talep ediyor. Buradaki 0/1 sözlüğü mantıksal kabul/ret ve işlem durumları için kullanılıyor. Bunun bir belgede bulunması, ChatGPT’nin veya bir CLI’nın etkin özel talimatlar alanına yüklendiğinin kanıtı değildir. [F00112, 3–20; tam metin okundu]

`boolean_yazılı_içerik_üretim_sistemi.md`, amaç, yöntem, bilgi zinciri, dil, rol, katmanlı anlatım, etik/yönetişim ve kanıt düzenini bir üretim şemasına dönüştürüyor. Koşullu ve Boolean ifadeler bir tasarım dili olarak mevcut; yürütülmüş yazılım sonucu olarak değerlendirilmedi. Aynı dosyanın ana metin sonrasındaki hesap kurtarma bilgileri yeni alıntılara çoğaltılmadı; yalnız konum ve adet kaydı tutuldu. Özgün kaynaklar ve hashleri değişmedi. [F00109; redaction_locations.json]

F00144, F00146 ve F00147, doğrudan ilk ileti/kopyala-yapıştır/kilit iletisi biçimindedir. “Kendini kur” ve belirli bir ilk yanıt verme istekleri modelin bağlamını ve yanıt biçimini yönlendirmeyi amaçlıyor. F00147’de araştırma/simülasyonun görünür son metinde anlatılmaması yönünde bir sunum talimatı da var. Bunlar metnin yönlendirici niteliğini gösterir; modelin mimarisinin değiştiğini veya görünmez bağımsız bir süreç doğduğunu göstermez. [F00144; F00146; F00147, 103–106]

O paketi içindeki kılavuzlar daha sınırlı bir ilişki de tarif ediyor: O adı veya bir kaynak/metafor tek başına yetki oluşturmaz; arşivde bir yönergenin bulunması yürürlükte emir olması değildir. Sürüm/işletim kayıtları yayımlama, yerleştirme, okuma ve kullanmayı ayırıyor; başka ajanların izinlerinin veya küresel ayarlarının otomatik değiştiği sonucunu vermiyor. [F00038; F00040; F00044; F00048]

## Model ve çalışma kitabı bulguları

CORE ve Model 1–4 çalışma kitapları, kavramsal ayrımları hücre alanlarına, kontrol noktalarına, puanlara, kilit kurallarına ve tasfiye koşullarına çeviriyor. Bu, steering’in yalnız rol isimlerinden ibaret olmadığını gösteriyor: bir yanıtın nasıl kurulacağı, hangi kanıtın kabul edileceği ve hangi eşikte geri döneceği de tasarlanmış. [F00107; F00114; F00117; F00120; F00125; F00129]

Bununla birlikte `RUN001` kaydının `not_started` olması, örnek puanların 1 ve bazı QA hücrelerinin TRUE olmasıyla birlikte okunmalı. Dolu şema veya doğru görünen formül, gerçek bir inceleme koşusunun yapıldığını kanıtlamıyor. Sürüm kayıtlarında checksum alanlarının boş, ZIP testinin PENDING veya bazı kontrollerin boş kaldığı yerler bulunuyor. Bu yüzden bütün QA hücrelerinin görünümü üzerinden sürüm doğrulaması tamamlandı sonucu kurulmadı. [F00131; F00132]

Model 3, biçim dönüşümündeki kayıp/bozulmayı, kavramın operatöre ve kaynağın kilide dönüştürülmesindeki riski ayrıca ele alıyor. Bu, bu incelemenin temel sorusuyla doğrudan ilişkili: bir kullanıcının sözünü uygulanabilir kurala dönüştürmek, kuralın kaynak sözle aynı olduğunu otomatik olarak sağlamıyor. [F00129; çıkarılmış hücre/formül metninin tamamı okundu]

## HalukAI: rol eşlemesi, dosyalar ve etkinlik ayrımı

Beşinci ZIP’te roller somut platform parçalarıyla eşleniyor:

| Rol | Arşivdeki karşılık | Somut kaynak |
|---|---|---|
| Hacker | Linux/Claude Code; Windows üzerinden QEMU aarch64 ve SSH ile erişim | H012; H013, 10–12; H019, 298–449 |
| Şahit | Copilot, Git/POSIX ortamı ve doğrulama | H010; H013, 10–12; H019, 452–507 |
| Şaman | Yerel Windows/Codex, arama/anlama ve koordinasyon | H011; H013, 10–12; H019, 510–716 |

Bu eşleme tarihsel F00025 ile ilişkilidir. F00025’teki `$env:STEERING_ROLE` dizgesi ile H019’da `Get-Content` çıktısı içinde görünen değişken bire bir aynı sürüm değildir: biri `SAMAN_ARAMA_ANLAMA_ENGEL_OLUSTURMAMA`, diğeri `SAMAN_ARAMAK_OGRENMEK_DENEMEK_KANITLAMAK_UYGULAMAK` değerini taşır. H011’deki kısa başlatıcıda ise bu değişken açıkça bulunmuyor. Değişkeni yazmak, CLI/modelin onu talimat olarak okuyacağı bir tüketici yolunu tek başına göstermiyor. [F00025, 97; H019, 603; H011 tam metni]

H004 somut bir bağlam yerleştirme yolu tarif ediyor: ortak AGENTS/CLAUDE metinlerini üretmek, Codex ve Copilot çalışma alanlarına yazmak, Copilot’a ayrıca `copilot-instructions.md` koymak ve Linux’a SCP ile kopyalamak. Ancak H004 içindeki gömülü AGENTS metni ile bağımsız H013 aynı sürüm değil. H013’te dört eylem ve dört engelleme etiketi var; H004’ün ürettiği metin bu çekirdeği aynı şekilde taşımıyor. H002’nin gömülü becerileri de H005/H009 bağımsız beceri metinleriyle eşdeğer varsayılamaz. Bu nedenle “AGENTS dosyası var” ifadesi, hangi metnin nerede bulunduğu sorusunu çözmüyor. [H004, 52–93; H013, 4–7; H002; H005; H009]

H015 anlam ile fiziksel yerleşimi açıkça ayırıyor: 19 Ekim aktarımı tarihsel anlam aktarımıdır; eski Windows modelini bire bir yerleştirme talebi olarak alınmamalıdır. Aynı metin C’ye dokunmama, kusursuz izolasyon veya sürekli arka plan köprüsü varsaymama sınırlarını koruyor. Bu belgenin kendi açıklaması, kavramsal bağın herhangi bir teknik yerleşime otomatik eşitlenmesini önlüyor. [H015, 10–11]

## Kaynakların birbirini sınırlandırdığı somut örnekler

| Konu | Kaynakların karşılaştırılması | Ulaşılabilen sonuç |
|---|---|---|
| “Bütün parçalar yeniden uygulanır” | H001, 79 ile H014’ün 72 satırlık tam kaynak kodu | ReplaceOldPS bazı uygulama, kısayol, ortam ve servis işlemleri içeriyor; devir metninin saydığı bütün güç/işlemci/Chocolatey/Node/PATH kurulumunun kodu burada bulunmuyor. Devir iddiası bu dosyanın kapsamından geniş. |
| Hacker başlatma başarısı | H020, 150–154 | Kayıt SSH beklemesinden sonra `kex_exchange_identification` ve `banner exchange` bağlantı kesilmesi hatalarıyla bitiyor. Sonraki H012 CPU parametresinin farklı olması düzeltme adayını gösterir; başarıyı kanıtlamaz. |
| Port açık / SSH hazır | H012, 8–15 ve 52–70 | TCP bağlantı denemesi ile SSH kimliği/sağlığı veya Claude bağlamının hazır olması ayrı kontroller. |
| Kontrol geçti / model doğrulandı | H019, 311 ve 482 | Eski başlatıcıların kendi sonuç şemaları login/model doğrulaması yapmadıklarını açıkça bildiriyor. Bunlar `Get-Content` kaynak dökümü; bütün kontrollerin çalışmış sonuçları değil. |
| Geçici alan ve rezervasyon | H019, 683–685; F00030, 89–95 | Alt süreç ortamı ve öncelik ayarı, bütün yazıcılar için kota veya işlemci/bellek rezervasyonu olarak sunulmuyor. |
| Dosya adı / içerik | H021, 43, 868, 2952–2954 ve 4399–4414 | AGENTS, CLAUDE veya Engelle adlı dosyalar listelerde var. Bu liste onların tam içeriğini, sürümünü veya model tarafından okunmasını göstermiyor. |
| Araç yolu | H005/H002 ve H017 | Bazı örnek araç dizinleri envanterdeki adlarla farklı. Derinlik sınırı olan taramadan sistem genelinde “yok” sonucu çıkarılmadı. |
| “Özgün metin” etiketi | F00026 ve F00049 | Yönerge olarak aktarılan metin ile paketteki gerçek yönerge sürümü farklı. “Özgün” başlığı, sürüm/metin eşliğinin yerine geçmiyor. |

## Şiirsel, simgesel ve bilimsel görünümlü kaynakların yeri

Rehber, Makina Yaratma ve Parça metinleri (örneğin F00155–F00163), yazı, hareket, niyet, hak, yaratma ve dönüşüm arasındaki ilişkileri geliştiriyor. Bu metinler çalışma dilinin tarihsel kaynağı olarak değerlidir; içlerindeki ifadeler bir işletim sistemi veya model ayarının uygulanmış kaydı değildir. “Akışı niyet sanmak” ve “hareketi hak sanmak” gibi uyarılar, eylemden niyet/yetki çıkarma sorununu metnin kendisinde de görünür kılıyor. [F00161–F00163]

F00053, F00222 ve F00223’te su, demir, manyetizma, deprem, yıldızlar ve O çevresinde kurulmuş birleşik anlatılar bulunuyor. Bu rapor bunları kaynaktaki kurgu/iddia olarak okuyor. Akademik kaynak başlığının veya bir bağlantı listesinin bulunması her sav için deney, ölçüm ya da hakemli doğrulama zinciri oluşturmaz. Bu incelemede dış bağlantıların güncel bilimsel doğruluğu araştırılmadı. [F00053; F00222; F00223]

Soy ağacı gözden geçirme raporu, Model 1–4/CORE belgelerini uzak bir ata yerine doğrudan kurucu zemin olarak konumlandırıyor ve sembollerin ilk görünmesiyle sonraki yansımasını ayırıyor. Olası yan bağlantıları kesin soy ilişkisi diye sunmama uyarısı, steering aktarımında da geçerli: iki metnin benzer sözcükler kullanması birinin diğerini teknik olarak etkinleştirdiği anlamına gelmez. [F00221]

## Sonraki okuma ve platform aşamasına devredilecekler

Tamamlanan bölümden üç tür çıktı hazır: dosya/hash eşlemesi, belge bazında anlam ve steering değerlendirmesi, gerçek okuma aralıkları. `reviews.json` her kaynak adını, özgün SHA’yı, metin SHA’sını, kısa değerlendirmeyi, kesin satır konumlu alıntıyı, okunma durumunu ve kalan aralığı birlikte taşır. Yeni birleşik pakette kaynak konumları E, farklı içerikler U ile numaralanır; birleştirme adla veya tarihsel F numarasıyla değil **özgün kaynak SHA-256 üzerinden** yapılmalıdır.

Platform değerlendirmesinde kapatılacak açık noktalar şunlardır:

1. Her CLI’nın gerçekten kullandığı çalışma dizini, başlatıcı sürümü ve talimat dosyasının kaynak/hash eşlemesi.
2. Bağımsız AGENTS/skill belgeleri ile kurulum betiklerinin gömülü sürümleri arasındaki içerik farkı.
3. Dosyanın yerleştirilmesi, oturumun başlaması, modelin bağlamı alması ve davranışta kullanması için ayrı kayıtlar.
4. SSH hata kaydı sonrası başlatma/erişim durumunun ayrı doğrulanması; devir metninin bunun yerine kullanılmaması.
5. Kullanıcının özgün ifadesi ile modelin teknik yorumu arasında onaylanmış dönüşümlerin açıkça gösterilmesi.

Bu maddeler yeni kuruluma başlanmış olduğunun beyanı değildir. Bu incelemede kaynak betikleri çalıştırılmadı, eski kurtarma komutları uygulanmadı, ayar veya izin değiştirilmedi. Kaynak kodları güncel kurulum tavsiyesi olarak sunulmadı.

## Dosyalar ve konumlar

Bu rapordaki F/S numaraları `deus_ex_machina_kaynak_agaci/02_Govde/katalog.json` içindeki tarihsel kimliklerdir. H numaraları `organize_work/environment_halukai/manifest.json` üye sırasıdır. Satırlar 1’den başlayan mevcut metin kopyası satırlarıdır; özgün Word/PDF sayfa numarası değildir.

- `reviews.json`: 248 kaynak kaydı ve belge bazında değerlendirmeler.
- `document_status.md`: bütün kaynak adları ve okunma/kalan aralık tablosu.
- `coverage.json`: sayısal kapsam ve tamamlanma sınırı.
- `mapping_checks.json`, `halukai_mapping_checks.json`: kaynak ve metin eşlemesi doğrulamaları.
- `structure.json`: mekanik gezinme indeksi; tam okuma iddiası içermez.
- `reading_queue.json`, `reading_queue.md`: farklı metin SHA’ları üzerinden kalan okuma kuyruğu.
- `all_distinct_text_coverage.json`: okunan ve kalan bütün farklı metinlerin yol/SHA/aralık eşlemesi.
- `redaction_locations.json`: beş kurtarma değerinin yalnız konum bilgisi; değerler içerilmez.

Bu dosyaların tamamı `[ARSIV_KOKU]/organize_work/steering_source_review/historical/` altındadır.

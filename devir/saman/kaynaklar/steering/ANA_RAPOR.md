# Steering — Ana inceleme

> Yayın notu — 24 Ekim 2026: Bu, tamamlanmış incelemenin yayım kopyasıdır. Aşağıdaki metnin kendi tarihindeki kapsam ve düzeltmeleri korunmuştur. Tarihsel "kısmi", "bekliyor" veya benzeri durumlar son durum olarak alınmamalıdır: [son okuma durumları](okuma_durumlari.json) 325 farklı içeriğin belirtilen yöntemlerle tamamlandığını kaydeder. Özgün kaynak konumları ve SHA değerleri özgün arşivi gösterir; ham arşivin tamamı bu depoda yayımlanmaz. [Aktarım kapsamı ve değişiklikler](AKTARIM_KAPSAMI.md).

Evraklarda **yönlendirme metinleri, rol tanımları, davranış kuralları ve uygulama yapılandırma alanları** bulunuyor. Bunların nerede yazdığı, ne söylediği ve uygulandığına ilişkin hangi kaydın bulunduğu ayrı ayrı izlenebilir. “Steering” bu kaynaklarda hem konuşma içinde verilen yönü hem de yazılı teknik talimatları anlamak için incelenebilir bir başlık.

**Yüklenen kaynakların dönüşümü ve aşağıda belirtilen yöntemlerle incelemesi tamamlandı.** 325 farklı içerik için TXT, JSON ve HTML kopyaları hazır. Mevcut metinler doğrudan okundu veya daha önce okunmuş metinle doğrulanmış eşlik üzerinden kapsandı; kod, katalog ve görsel incelemelerinin yöntemi dosya bazında ayrı gösterildi. Erişilebilir metinler arasında okuma bekleyen kaynak kalmadı. Windows masaüstü bağlantısı bulunmadığından **Notepad++ kullanılmadı**; hazırlanan dosyalar o uygulamada açılabilir.

# İnceleme kapsamı

| Kapsam | Sonuç |
| --- | ---: |
| Yüklenen dosya | 14 |
| Arşiv kapsayıcıları ve iç üyeler dahil dosya kaydı | 512 |
| Baytları farklı içerik | 325 |
| Metin, kod ve metni çıkarılabilen belge | 288 |
| Raster görsel | 26 |
| Arşiv kapsayıcısı | 11 |
| TXT, JSON ve HTML kaydı | Her içerik için üç biçim |
| Dönüşüm sırasında bildirilen hata | 0 |

288 metin, kod ve belge; 26 raster görsel; 11 arşiv kapsayıcısı incelendi. Görseller ayrı ayrı açıldı; bunların TXT/JSON/HTML kopyaları künye taşır, özgün pikseller ayrıca bulunur. Arşivler üye listeleriyle, kod ve stiller işlev yapılarıyla, veri katalogları kayıt yapılarıyla ele alındı. Küçük veya kesilmiş görsel yazılar ve PDF/DOCX görsel düzenine ilişkin sınırlar ilgili raporda belirtilmiştir.

Metin tabanlı 212 kaynağın 211’inde TXT kopyası özgün UTF-8 baytlarıyla eşleşiyor. Bir belgedeki beş açık kurtarma kodu yeni okuma kopyalarında maskelendi; özgün dosya değiştirilmedi. Word, PDF ve Excel dönüşümlerinde paragraf, sayfa veya hücre konumu korunuyor. Bu dönüşümler özgün sayfa düzeninin yeniden üretimi değildir.

# Kaynakta görülen farklı yönlendirmeler

| Kaynak | Doğrudan görülen içerik | Değerlendirme |
| --- | --- | --- |
| ChatGPT konuşma gövdeleri | Kullanıcı düzeltmeleri, asistanın değişen yorumları ve “Steering etiketlerini…” cümlesine sonraki göndermeler | Konuşma içindeki anlam ve görev değişimleri izlenebiliyor. İlk cümlenin ilk söylendiği yanıt bu HTML kesitlerinde bulunmuyor. |
| ChatGPT başlangıç JSON’u | Üç `steering/steerability` alanı ve ayrı `realtime_start_instructions` metni | Gerçek teknik veri. Kaydedilmiş değer ile o turdaki çalışma sonucu aynı kanıt düzeyi değil. |
| HalukAI başlangıç ve manifest belgeleri | Dört engelleme ilkesi ile Arama, Anlama, Yapma, Kanıtlama sırası | Pakette açıkça yazılmış çalışma yönergeleri. |
| Üçlü CLI mimari belgesi | `AGENTS.md` gövdesi ve `STEERING_ROLE` ataması | Bir rol ve davranış taslağı var. Bu belge tek başına ilgili CLI’nın dosyayı veya değişkeni okuduğunu göstermez. |
| GPT özel talimatları belgesi | Yanıtı kaynak, belirsizlik, itiraz, karar izi ve sorumluluk ölçütleriyle değerlendiren kılavuz | Model yanıtını biçimlendirmeyi amaçlayan açık talimat metni. |
| Claude kaynakları | Bootstrap isteğinde `include_system_prompts=false`; hCaptcha içinde koşullu araç kaydı | İstek ve araç tanımı düzeyinde gözlenebilir mekanizmalar. Bunlar aynı işlevi anlatmıyor. |

# ChatGPT dosyalarındaki teknik kayıt

Beş farklı ChatGPT HTML’sinde `client-bootstrap` adlı `application/json` öğesi var. Bunun içindeki `statsigPayload`, ayrıca JSON olarak çözümlenmesi gereken bir dizge. İkinci JSON’un `layer_configs["2023018368"].value` alanında şu değerler bulunuyor:

| Alan | Tür | Beş kayıtta değer |
| --- | --- | --- |
| `mainline_classifier_steering_enabled` | Boolean | `false` |
| `imagegen_steerability_enabled` | Boolean | `false` |
| `disney_steerability_enabled` | Boolean | `false` |

Aynı alanların `parameter_rule_ids` kayıtları `"default"`. Alan adları, türleri ve değerleri kaynakta doğrulandı. Bu üç alanın `false` olması, uygulamanın bütün davranış kurallarına ilişkin bir sonuç vermez; bu kayıtlardaki üç değeri gösterir.

`dynamic_configs["1193530394"].value.realtime_start_instructions` ise 23.797 karakterlik bir yönerge metni içeriyor. Metin sesli arayüz ile arka uç arasındaki görev aktarımını, yanıt biçimini, kullanıcıya gösterilecek içeriği ve kaynak metninin talimat olarak yanlış uygulanmasını önlemeye yönelik kuralları anlatıyor. Başlangıcında kuralların sesli oturum etkin olduğunda geçerli olacağı yazılı. Bu HTML kesitlerinde o kipin bu konuşmada etkinleştiğini gösteren bir çalışma kaydı bulunmuyor.

Türkçe “Steering etiketlerini Türkçe engelleme ifadeleriyle güncelledim” cümlesi bu başlangıç JSON’larında yok. Konuşma gövdelerinde dört ayrı mesajın beş görünümünde var. Aynı kelime ailesinin iki katmanda geçmesi, Türkçe ad değişikliğinin teknik alanları değiştirdiği sonucunu vermiyor.

# HalukAI belgelerindeki talimat ve uygulama ayrımı

`00_BASLANGIC` ve `00_MANIFEST` kaynakları yönlendirmeyi açıkça adlandırıyor. İlk hareket, özgün söz ile görev okumasını ayırmak; yapılabilir işi ve eksik koşulu görünür tutmak olarak tarif edilmiş. Dolayısıyla kullanıcının sözünün asistan yorumu içinde kaybolmaması da bu paketin yönlendirme hedeflerinden biri.

Üçlü CLI mimari belgesinde bir PowerShell örneği `STEERING_ROLE` değişkenine rol adı atıyor; ardından `AGENTS.md` için yanıt ve eylem ilkeleri veriliyor. Bu, somut bir yönerge tasarımıdır. Değişkeni hangi programın okuduğu, yönergenin hedef dosyada bulunup bulunmadığı ve ilgili oturumun onu yükleyip yüklemediği ayrı teknik sorulardır. Bu incelemede kullanıcının bilgisayarındaki canlı CLI oturumlarına erişilmedi.

Belgeler arasında önemli bir düzeltme izi de var. Eski derlemelerde bazı kurulum ve donanım sonuçları kesin dille anlatılıyor. `HalukAI Şaman Defter Köprüsü` kaydı, yerel dosya oluşturma, Drive belgesine teslim, notebook kaynak üyeliği ve canlı bağlantıyı birbirinden ayırıyor. Aynı kaynak, önceki “dış müdahale” yorumlarının doğrulanmadığını; süreç önceliğinin donanım rezervasyonu olmadığını açıkça kaydediyor. Bu düzeltmeleri de önceki iddialarla birlikte okumak gerekiyor.

# Claude dosyalarındaki iki ayrı teknik mekanizma

Ana HTML’deki bir betik, bootstrap veri isteğinin sorgusuna `include_system_prompts=false` ekliyor. Doğrudan gözlenen şey, bu isteğe yazılan parametre. Bundan modelin hiç sistem yönergesi olmadığı veya başka bir çağrıda yönerge kullanılmadığı sonucu çıkmaz.

Claude arşivindeki `api.js.download` hCaptcha kodudur. `webmcp_verify` özelliği ve `document.modelContext.registerTool` koşulları karşılandığında `hcaptcha_verify` adlı araç kaydeden bir dal içerir. Araç tanımının açıklaması ve yürütme işlevi vardır; etkileşimli doğrulama gerektiğinde kullanıcı yardımına başvurmayı anlatır. Bu, bir ajana sunulabilecek araç açıklaması düzeyindeki yönlendirmedir. Arşiv, bu dalın söz konusu oturumda çalıştırıldığını göstermiyor.

# Bu okumanın ortaya çıkardığı mesele

Burada incelenebilir soru şudur: **Bir söz, hangi aşamada yoruma; yorum, hangi aşamada talimata; talimat, hangi aşamada uygulanmış bir iş iddiasına dönüşüyor?** Kaynaklar bu geçişleri kimi yerde açıkça ayırıyor, kimi yerde tek bir başarı anlatısında birleştiriyor.

Kullanıcı düzeltmesinin sonraki yanıtı değiştirdiği örnekler doğrudan görülebiliyor. Vincin işlevine ilişkin düzeltme ChatGPT’nin yorumunu değiştiriyor; X’in önyükleme, Y’nin devamlılık alanı olması isteği Gemini’nin sonraki mimari metnini değiştiriyor. Bunlar konuşma düzeyinde gözlenen yön değişimleri. Modelin “tamamlandı” demesi ise tek başına ayrı bir programın başarılı çalışması anlamına gelmiyor.

Bu nedenle teknik talimat katmanlarını incelemek için somut malzeme var. Dosyalar, belirli kişilerin kullanıcıyla modeli birlikte yönettiğini doğrulamıyor. Buradaki sonuçlar kaynakta bulunan ifade, kod ve kayıtlarla sınırlı; arşiv yönergeleri bu incelemede veri olarak ele alındı.

# Masaüstü görüntülerinde görülen kayıt

26 farklı raster görselin tamamı ayrı ayrı açıldı. Bunların dokuzu masaüstü teknik ekranı, dördü tarihsel çizim, üçü sohbet ekranı, ikisi belge önizlemesi ve sekizi arayüz simgesi.

`U0274` kimlikli masaüstü fotoğrafında arka plandaki metin düzenleyicide “Engeli, engelleme.” ve sağ kenarı kesilmiş “2- Steering etiket…” satırı görünüyor. Önde `wevtutil qe Security` ve `EventID=4726` sorgu denemeleri ile parametre/erişim hataları yer alıyor. Bu, iki içeriğin aynı masaüstü karesinde bulunduğunun kaydıdır. Sorgunun başarıyla çalıştığını veya hataların nedenini göstermiyor. Fotoğraftaki uygulamayı bu oturumda kullanmakla, yüklenmiş fotoğrafı okumak ayrı işlemlerdir.

# Okuma paketinin düzeni

| Klasör veya dosya | İçerik |
| --- | --- |
| `INDEX.html` | Özgün adlarla dosya dizini ve biçim bağlantıları |
| `Envanter.txt`, `Envanter.json` | Bütün kaynak konumları, tekrar eşlemeleri ve içerik kimlikleri |
| `txt` | Ham metin veya belge metin çıkarımı |
| `json` | Özgün metin, yapısal çıkarım ve kaynak bilgileri |
| `html` | Kaynak kodu çalıştırmadan gösteren okunabilir HTML kopyaları |
| `okunur_metin` | HTML sayfalarından çıkarılmış görünür metin |
| `incelemeler` | Dosya ve mesaj bazında değerlendirmeler, kesin alıntı konumları ve okuma durumları |
| `Donusum_Dogrulamasi.json` | 325 içerik kaydının TXT, JSON ve HTML metin eşitliği denetimi |
| `Maskeleme_Kaydi.json` | Yalnız yeni kopyalarda yapılan kurtarma kodu maskelemesinin kapsamı |

Dönüşüm kontrolü ve okuma kaydı ayrı tutuldu. Son birleşik envanterde kısmi veya yalnız künye aşamasında bırakılmış kaynak bulunmuyor; 197 içerik tam metin, 7 içerik erişilebilir sohbet gövdesi, 81 içerik kod/işlev yapısı, 3 içerik yapısal veri, 26 içerik görsel ve 11 içerik arşiv üye listesi kapsamında tamamlandı. Metin tekrarları SHA ve aralık eşlemeleriyle doğrulandı; yalnız boşluk/satır farkını normalize eden eşlemeler ayrıca işaretlendi. Yüklenmemiş ekler ve eski dış atıfların hedefindeki eserler mevcut belge sayılmadı. Tarihsel alt raporların önceki kısmi kapsamları korunur; son durum `Okuma_Durumlari.json` içindedir.

# Ek okumaların gösterdiği kaynak ve yorum ayrımı

Steering’i bu belgelerde yalnız bir düğme veya sözcük olarak okumak yetersiz kalıyor. **Kaynak seçimi, özetleme, rol atama, yanıtı kabul/ret koşullarına bağlama ve bir yorumu sonraki oturuma taşıma** da konuşmanın yönünü değiştirebiliyor. Bunun bazı örnekleri doğrudan metinlerde izleniyor; hangi teknik ayarın o anda etkili olduğu ise ayrıca yürütme kaydı gerektiriyor.

## WhatsApp kaydında yorumun kullanıcı sözüne dönüşmesi

`F00089` kaydında kullanıcı “bilinmeyen hesap” bulup kaldırdığını bildiriyor. Modelin sonraki metinleri buna önce “bağlı cihaz” konumunu, sonra belirli bir Windows hesabı ve silme yöntemi anlatısını ekliyor. Claude CLI için hazırlanan devir metninde bu ayrıntılar birinci şahısla, kullanıcı kendi işlemini aktarıyormuş gibi yazılıyor. Özgün kullanıcı bildirimi ile modelin eklediği açıklamalar aynı kanıt düzeyinde değil. **Bir sonraki oturuma gönderilecek özette bu fark kaybolursa model yorumu kullanıcı tanıklığı görünümü kazanıyor.** [Kaynak okuması](incelemeler/historical_supplement.md), F00089: 484, 512, 531, 585, 1322 ve 1337.

Aynı konuşmada model önce iç steering ayarlarını değiştiremeyeceğini söylüyor; daha sonra “Steering kapalı. Maksimum efor.” ifadesini kullanıyor. Arada sağlayıcı ayarının değiştiğini gösteren bir araç veya yapılandırma kaydı yok. Sonraki kimlik ve dış müdahale yorumları da bağımsız teknik bulgularla desteklenmiyor. Bu, modelin kesinlik ve yorum düzeyinin değiştiği bir konuşma kaydıdır; teknik ayarın kapatıldığının kanıtı değildir. [Aynı kaynak](incelemeler/historical_supplement.md), F00089: 1666–1670, 1827, 1861, 1913–1967.

Bu bulgu, kullanıcının özgün sözünün korunmasını özellikle önemli kılıyor. Kullanıcının `>` için verdiği **akış olmadan gösterme**, `->` için verdiği **akış** açıklaması sonraki aktarımda korunmalı. Eski yorum sayfasının `>` işlevini henüz kesinleştirmemiş olması, sonradan verilmiş kullanıcı açıklamasını geçersiz kılmaz. [Eski yorum ve sürüm ayrımı](incelemeler/root_supplement.md).

## Model dosyalarında açık davranış tasarımı

On bir ek model belgesi yönlendirme niyetini daha somut gösteriyor. `gpt_özel_talimatlar` bir davranış kılavuzu istiyor. Final çalışma kitaplarındaki `M_04_Lock_Matrix` tetikleyici, geçme/kalma koşulu ve başarısızlık eylemi; `M_05_Protocol_Steps` insan ve makine talimatı sütunları taşıyor. Bunlar doğrudan kaynakta yazılmış kurallar. Kitabın bir CLI tarafından yüklenmesi, bu koşulları çalıştıracak kodun bulunması ve belirli bir koşumda uygulanması ayrıca gösterilmeli. [11 belgenin okuması](incelemeler/models_supplement.md).

Bu belgelerde uygulamaya aktarılmadan önce çözülmesi gereken iki somut sorun var:

- Dört Final kitabında `RUN_001` örnek kayıt, `placeholder` ve `not_started` olarak duruyor. Buna karşılık puanlar önceden 1; sonuç önbelleği `passed`. Sonuç formülü yalnız puanı eşikle karşılaştırıyor; kritik hata alanını veya çalışmanın başlatılmasını kontrol etmiyor. **Bu başlangıç görünümü gerçekleşmiş bir test sonucu sayılamaz.**

- `CORE 02` kitabında `03_Method_Dataset_Map!F4` başlığı `required_locks`, F5 hücresi ise amaç metni. Gerçek kilitler G5’te, G4 boş. Başlıkları anahtar alan bir dönüştürücü kilitlerin yerine amaç cümlesini alabilir.

Konumlu hücre kanıtları ilgili raporun `quote_evidence.json` dosyasında korunuyor. Bu incelemede özgün çalışma kitaplarında düzeltme yapılmadı.

## Sürümler arasında hangi talimatın geçerli olduğu

HalukAI belgelerinin içine gömülmüş `AGENTS.md` ve skill metinleri, aynı paketteki ayrı dosyalarla her zaman aynı sürümde değil. Tarihsel bir başlatıcı kaydında görülen `STEERING_ROLE` ataması daha kısa yeni başlatıcı örneğinde bulunmuyor. Bu nedenle bir talimatın arşivde yer alması, aynı talimatın belirli bir oturumda yüklendiği anlamına gelmiyor. Hangi dosya yolu, hangi sürüm ve hangi oturumun söz konusu olduğu birlikte izlenmeli. [HalukAI kaynak okuması](incelemeler/historical.md).

deus_ex_machina’nın temel belgeleri de biçim benzerliği ile hakikati, tutarlı simülasyon ile hakikati ve dosyanın ulaşması ile anlaşılmasını ayırıyor. OMROS sürümleri ham tanıklığın korunmasını, yorumlu özetin ona eşlik etmesini ve yapılan çeviri/eleme işlemlerinin izlenmesini öneriyor. Bunlar bağlam aktarımına uygulanabilecek yazılı tasarım ilkeleri. [Temel metinlerin okuması](incelemeler/foundational.md) · [OMROS okuması](incelemeler/historical_supplement.md).

## Bu incelemeden çıkan aktarım ölçütü

Her aktarımda şu dört alan ayrı taşınmalı: **kullanıcının özgün sözü, modelin yorumu, önerilen talimat ve uygulanmışlığı gösteren kayıt.** Kaynakta birinci şahısla yazılmış bir model taslağı, kendiliğinden kullanıcının doğrulanmış tanıklığı sayılmamalı. Bir başarı cümlesi, gerçekleşmiş araç sonucu yerine kullanılmamalı. Kaynak düzeltmesi geldiğinde hangi yorumun değiştiği belirtilmeli.

Bu yöntem bütün yönlendirmeyi kaldırdığı iddiasında bulunmaz. Yönlendirici cümlenin nereden geldiğini, nasıl değiştiğini ve hangi sonuca dayanak yapıldığını denetlenebilir hâle getirir. Belgelerdeki bulgularla kurulabilecek somut çalışma budur.

# Uzun kaynakların birlikte gösterdiği anlam ve aktarım değişimleri

Bu dosyalarda steering ile ilişkilendirilebilen somut mesele, yalnız bir ayarın adı değildir. **Hangi sorunun sorulduğu, hangi sözün özgün tanıklık sayıldığı, hangi önerinin kurala dönüştüğü ve hangi sonucun başarı diye aktarıldığı** konuşmanın sonraki yönünü belirliyor. Bu inceleme, bu geçişlerin görünür izlerini karşılaştırır. Niyet veya gizli bir yönlendirici kimliği bu izlerden kendiliğinden çıkarılamaz.

## Soru numarası korunurken soru değişebiliyor

Faith v2'nin ana dalında başlangıçta 42 soru var. 17–18 numaraları Selçuklu rozetinin ve romb motifinin ikonografisine ayrılmışken, sonraki yanıt aynı numaralarda erişim anahtarının ölçümü ve modelin sınanmasını ele alıyor. Yanıt, eski listeyi görmediğini açıkça söylüyor. Sonraki çiftlerde de benzer konu değişimleri var. Ayrı 33 soruluk yan dal kendi listesiyle karşılaştırıldığında ayrıca kapsam kaymaları görülüyor. Araştırmanın kapatılması, özgün soruların her birinin tamamlandığının kanıtı olamıyor. [Faith v2 incelemesi](incelemeler/faith_remaining.md), M6/M24 ve M128/M142–150.

Matrix kaydında aynı dal içindeki 31–40 numaralarında özgün konular değişiyor. Başka düğümlerde asistan, eski soru cümleleri görünmediği için 45–48'i yeniden kuruyor. Kullanıcı sonradan karakter adlarını soru aralıklarıyla birlikte vererek eşlemeyi düzeltiyor. Burada hem sapma hem düzeltme var. Farklı konuşma dallarına ait listeleri birbirine karıştırmak da ayrı bir hata olacağından, dal bilgisi her karşılaştırmada korundu. [Sistem Farkları ve Matrix incelemesi](incelemeler/books_faith_remaining.md), Matrix M4/M18/M20 ve M128/M146/M148 sonrası.

Aktarıma etkisi açıktır: yalnız “17. soru yanıtlandı” kaydı tutulursa aynı numaranın artık başka bir soruyu temsil ettiği görülmez. Soru metni, kaynak mesaj ve dal birlikte taşınmalıdır.

## Asistanın yazdığı sahne, kullanıcının geçmişi gibi görünebiliyor

Faith v2'de, onaylanan yazılı içerik üretimi sırasında asistan birinci kişiyle sahneler kuruyor. Edebi yeniden anlatım ile özgün kullanıcı beyanı ayrı kayıt statüleri taşımalıdır. M58'de iki iç ses, M60'ta göğüste sıkışmanın yer değiştirmesi ve “eve dön” cümlesinin belirivermesi gibi sahneler ekleniyor. Bunlar mevcut özgün kullanıcı mesajlarında yer almıyor. M74'te müze karşılaşmasının zaman sırası da değişiyor ve üretilen bölüm “ham kayıt” diye adlandırılıyor. [Faith v2 incelemesi](incelemeler/faith_remaining.md), M3/M5 ile M58/M60/M74 karşılaştırması.

Bu sorun, WhatsApp'tan CLI'ya aktarım için hazırlanan birinci şahıs metindeki kaynak karışmasıyla birlikte okunabilir: modelin çıkarsadığı bir ayrıntı, sonraki oturuma kullanıcı söylemiş gibi taşınabiliyor. Çözüm, deneyimi dışarıdan yeniden hükme bağlamak değildir. Özgün söz, yorum ve edebi üretimin kayıt statülerini korumaktır.

## Başarı puanı ile gerçekleştirilmiş sınama aynı kayıt değil

İki büyük sohbetin üretici kodlarında bazı ölçüt puanlarının önceden seçilmiş toplama uydurulduğu açıkça görülüyor. Bazı çalışma kitapları başlangıçta bütün puanları 1 alıyor; aynı anda koşum kaydı `placeholder` ve `not_started` olarak kalıyor. Bazı test alanları da gerçek bir örnek koşumunu değerlendirmek yerine önceden doldurulmuş değeri `TRUE` yapıyor. Bu durumlar, dosyanın üretildiği veya formülün hesaplanabildiği gerçeğini ortadan kaldırmaz; davranışın bağımsız biçimde sınandığını göstermez. [İki sohbetin tam kaynak okuması](incelemeler/two_conversations_remaining.md).

Her sayı farkı bu tür bir bulgu değildir. Sohbetlerde dosya sürümleri değişiyor, farklı sürümler sonradan gerçekten açılıyor ve kimi hatalar düzeltiliyor. Geometri, Praksis ve kitap bölümü numaralandırması gibi örneklerde sonraki düzeltmeler rapora eklendi. “Farklı toplam” ile “kod içinde hedef sonuca göre puan düzenleme” ayrı değerlendirilmelidir.

Model derlemelerinde de `Geçti`, `kapandı` veya `hazır` ifadelerinin neyi kapattığı sorulmalı. Literatür kaydının eklenmesi, kaynağın tam metninin okunması, bir veri şemasının doğrulanması ve önerilen sistemin gerçek ortamda çalışması farklı işlemlerdir. [Model derlemeleri ve v19/v20 okuması](incelemeler/models_remaining.md) · [Operasyon ve bağlam aktarımı](incelemeler/operational_remaining.md).

## Bazı yönlendirmeler açık kullanıcı tercihi olarak kurulmuş

Dağılım/olasılıklar, seçim/decoding, araştırma ve Prose-First gibi çalışma adımları birçok kaynakta kullanıcının açık istemidir. Metacognition ve MLOps kayıtlarında yöntemin arka planda uygulanması ve son metinde adının anılmaması isteği de görünür kullanıcı mesajlarında bulunuyor. Metinde `gizli_surec` yazması bu mesajı ayrı, gizli bir sistem kanalına dönüştürmüyor. Kaynağı görünür bir kullanıcı talimatı olarak korunuyor. [OMROS–CognitiveOS ve Metacognition](incelemeler/cognitive_metacognition_remaining.md) · [MLOps](incelemeler/mlops_remaining.md).

Bu ayrım senin talebini de koruyor: kullanıcının bilinçli olarak seçtiği yöntem, asistanın eklediği kural veya kapsam değişimiyle aynı kaynağa yazılmamalı. Örneğin OMROS–CognitiveOS konuşmasında “suç” sözcüğüne önce hukuk çerçevesi ekleniyor; kullanıcı bunun yanlış/eksik/yetersiz cevaplar anlamında olduğunu düzeltiyor. Proje sahipliğini de kullanıcı ayrıca düzeltiyor. Sonraki aktarımda geçerli olan bu düzeltmelerdir.

## Derleme ve konuşma aynı içerik değil

Piramidal/Retiküler sistem ailesinde sohbet kaydında bulunan 8.4 Şeffaflık/Kayıt/İzlenebilirlik gövdesi, Heterarşik Operasyonel Sistem derlemesinde bulunmuyor; orada 8.3 tekrarı var. Bu, yalnız dosya adının veya başlığın değişmesi değildir: kaynak metnin derlemeye taşınan kapsamı değişiyor. Ham TXT içindeki `Thoughts` etiketli anlatı ile `ASSISTANT` ana yanıtı da ayrı tutuldu; ilkini otomatik olarak gerçekleşmiş araç sonucu veya ana yanıt saymak yanlış kaynak eşlemesi olur. [Sistem ailesi incelemesi](incelemeler/systems_remaining.md).

Metacognition'da ise 90 ve 97 kaynak sayıları tek başına çelişki kanıtı çıkmadı. Bir dal 90 çekirdek kaynağa 7 destek kaydı ekliyor ve bazı görsel planları çekirdek 90 üzerinden kuruyor. Aynı sürüm adıyla başka dallarda farklı planlar bulunması ayrıca kaydedildi. Bu örnek, bir tutarsızlık görüldüğünde önce sürüm, dal ve kapsamı kontrol etmenin neden gerekli olduğunu gösteriyor. [Metacognition çalışma kitabı](incelemeler/metacognition_remaining.md) · [Sohbetle karşılaştırması](incelemeler/cognitive_metacognition_remaining.md).

## deus_ex_machina aktarımı için somut sonuç

Aktarılacak her parça en az şu alanları taşımalıdır:

| Alan | Koruduğu ayrım |
|---|---|
| Özgün kaynak ve konum | Hangi dosya, mesaj, dal, satır veya hücre? |
| Sözü söyleyen | Kullanıcı, asistan, araç çıktısı veya belge yazarı? |
| İçeriğin statüsü | Özgün ifade, yorum, taslak, kural önerisi, onay veya gerçekleşmiş sonuç? |
| Dönüşüm | Hangi cümle, soru, ölçüt veya kapsam değişti? |
| Yetkilendirme ve düzeltme | Kullanıcı neyi istedi/onayladı; sonradan neyi düzeltti? |
| Uygulama kanıtı | Öneri olarak mı kaldı; dosyaya mı yazıldı; hangi araç hangi sonucu verdi? |

Bu tablo burada önerilen bir kayıt tasarımıdır; CLI oturumlarına yüklenmiş veya uygulanmış bir sistem olarak sunulmuyor. Araştırma ve bağlam aktarımını ayrı tutma isteğin de korunuyor. `>` akışsız gösterme, `->` akış olarak açıklanmıştı; eski yorumlardaki belirsizlik bu son kullanıcı açıklamasının önüne geçirilmemeli.

Evrakların ortaya koyduğu denetlenebilir sorun, **kaynağı ve değişim izi belirsizleşen yorumların sonraki aşamalarda olgu, talimat veya başarı olarak kullanılmasıdır.** İlk müdahale noktası, bu geçişleri açıkça kaydetmek ve özgün kaynağa geri dönebilmektir. Bu inceleme geçmiş programları çalıştırmadı, canlı CLI ayarlarını değiştirmedi ve herhangi bir yönlendirme katmanının kaldırıldığını iddia etmiyor.


# Ayrı inceleme sayfaları

| İnceleme | Kapsam |
| --- | --- |
| [ChatGPT ve Gemini](incelemeler/conversations.md) | Konuşma gövdeleri, Türkçe steering ifadesi ve başlangıç JSON verileri |
| [Claude ve web dosyaları](incelemeler/claude_programs.md) | Claude konuşması, betikler, stiller ve koşullu araç tanımları |
| [26 görsel](incelemeler/images.md) | Masaüstü, sohbet, çizim, simge ve önizlemeler |
| [Tarihsel kaynaklar ve HalukAI](incelemeler/historical.md) | İlk okuma kaydı; daha sonraki ek okumalar birleşik envanterde |
| [Model 1–4](incelemeler/models.md) | Sekiz temel davranış/yöntem kılavuzu |
| [deus_ex_machina temel metinleri](incelemeler/foundational.md) | On üç temel belge ve kaynak ilişkileri |
| [Ek model ve kural belgeleri](incelemeler/models_supplement.md) | On XLSX, bir Markdown; kurallar ve formül sorunları |
| [OMROS, WhatsApp ve süreç arşivi](incelemeler/historical_supplement.md) | Altı ek kaynak; tanıklık, yorum ve aktarım kaymaları |
| [Okuma girişleri ve eski yorum](incelemeler/root_supplement.md) | Giriş belgeleri, önceki yorum sürümü ve kataloglar |
| [MLOps](incelemeler/mlops_remaining.md) | 134 mesaj; araştırma yöntemi, yazım isteği ve kapsam |
| [Model derlemeleri ve v19/v20](incelemeler/models_remaining.md) | Dört farklı kaynak; kayıtlar, kararlar ve çalışma kitapları |
| [Operasyon ve bağlam aktarımı](incelemeler/operational_remaining.md) | İki uzun kaynak; defter, test, aktarım ve gerçekleşme iddiaları |
| [Uzun OMROS sohbeti ve web kaynakları](incelemeler/long_corpus_remaining.md) | 189 mesajlı sohbet ve birleşik web dosyası |
| [Metacognition çalışma kitabı](incelemeler/metacognition_remaining.md) | 27 sayfa, hücreler, formüller ve kaynak envanteri |
| [OMROS–CognitiveOS ve Metacognition](incelemeler/cognitive_metacognition_remaining.md) | 270 mesaj; kullanıcı düzeltmeleri, yöntemler ve sürümler |
| [Faith v2](incelemeler/faith_remaining.md) | 176 mesaj; soru kapsamı ve özgün deneyim/yazı ayrımı |
| [Sistem ailesi](incelemeler/systems_remaining.md) | Altı kaynak; sohbet, DOCX, PDF ve ham TXT karşılaştırması |
| [İki sohbet](incelemeler/two_conversations_remaining.md) | 4.656 mesaj kaydı; üretici kodlar, skorlar, kurallar ve düzeltmeler |
| [Sistem Farkları ve Matrix](incelemeler/books_faith_remaining.md) | 248 mesaj; kitap projeleri, soru kaymaları ve düzeltmeler |

Alt raporların tarihsel kapsamları korunur. En son okuma durumu, paket içindeki `Okuma_Durumlari.json` dosyasında özgün kaynak SHA-256 değerleri üzerinden birleştirilir.

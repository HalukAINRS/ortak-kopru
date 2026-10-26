> Yayın notu — 24 Ekim 2026: Bu, tamamlanmış incelemenin yayım kopyasıdır. Aşağıdaki metnin kendi tarihindeki kapsam ve düzeltmeleri korunmuştur. Tarihsel "kısmi", "bekliyor" veya benzeri durumlar son durum olarak alınmamalıdır: [son okuma durumları](../okuma_durumlari.json) 325 farklı içeriğin belirtilen yöntemlerle tamamlandığını kaydeder. Özgün kaynak konumları ve SHA değerleri özgün arşivi gösterir; ham arşivin tamamı bu depoda yayımlanmaz. [Aktarım kapsamı ve değişiklikler](../AKTARIM_KAPSAMI.md).

# Tarihsel kaynaklar: steering bağlamında ek belge incelemesi

23 Ekim 2026

Bu rapor, ilk tarihsel incelemede henüz tam okunmamış olan altı farklı kaynağın ek okumasını tamamlar. En belirgin sonuç şu: belgeler aynı türden yönlendirmeler taşımıyor. OMROS metinleri kurumların bilgi ve karar akışını tasarlayan normatif metinler; çalışma kitabı kullanıcı taleplerini ve bunlardan kurulmuş bir kavram arşivini taşıyor; WhatsApp kaydı kullanıcı taleplerinin model tarafından yorumlanmasını, yeniden yazılmasını ve kimi yerde kesin olgulara dönüştürülmesini gösteriyor. Nöroşirürji makalesi ise kendi konusu içinde bilimsel bir kaynak. Bu türleri aynı “steering mekanizmasının” kanıtı saymak kaynakların söylediğinden fazlasını söylemek olur.

## Okuma kapsamı ve yöntem

Altı kaynağın asıl dosya SHA-256 değerleri ve okuma kopyalarının SHA-256 değerleri katalogla yeniden doğrulandı. Bunlar, aynı asıl dosya özetiyle katalogdaki sekiz kaydı kapsıyor: F00073 ile F00181 aynı dosya; F00099 ile F00138 aynı dosya. Sonradan hazırlanan birleşik pakette dosya numaraları değişebileceğinden eşleştirme anahtarı SHA-256 olmalıdır.

| Kaynak | İncelenen metin | Doğrudan okunan karakter | Önceden okunmuş metinle birebir eş blok | Kalan |
|---|---:|---:|---:|---:|
| F00179 — OMROS v8 | 218 satır / 27.819 karakter | 27.819 | 0 | 0 |
| F00180 — OMROS v25 | 337 satır / 90.823 karakter | 63.882 | 26.941 | 0 |
| F00073 — OMROS v41 | 353 satır / 154.582 karakter | 69.661 | 84.921 | 0 |
| F00099 — Tüm Sürecin Arşivi | 713 satır / 56.571 karakter | 56.571 | 0 | 0 |
| F00089 — WhatsApp / Meta AI | 2.011 satır / 113.517 karakter | 113.517 | 0 | 0 |
| F00090 — article-p773-libre.pdf | 1.701 satır / 98.286 karakter | 98.286 | 0 | 0 |
| **Toplam** | **541.598 karakter** | **429.736** | **111.862** | **0** |

Karakter sayıları okuma sırasında satır sonlarının LF biçimine getirildiği metin içindir. Özgün okuma kopyalarının toplamı 541.823 karakterdir; 225 karakterlik fark WhatsApp dosyasındaki CRLF/CR satır sonlarından gelir. Kaynak dosyalar değiştirilmedi.

OMROS sürümlerinde benzerlik varsayılmadı. Önceki sürümün tamamı okunduktan sonra sonraki sürümün yeni ve değişen aralıkları okundu; kalan aralıklar UTF-8 bayt eşliği ve blok SHA-256 değeriyle doğrulandı. Doğrudan okumayla eş blokların kesişimi iki kez sayılmadı. Ayrıntılar `reviews.json`, `coverage.json` ve iki `blocks_...json` dosyasında bulunur. Rapor içindeki satır konumları bu değişmeyen okuma kopyalarına aittir.

“Tam okundu” burada mevcut çıkarılmış metnin tamamını ifade eder. DOCX/PDF görsellerinin ayrıca görsel incelemesi, WhatsApp fotoğraflarının doğrulanması, makaledeki dış atıfların okunması veya erişilemeyen sohbetin tamamlanması anlamına gelmez. Bu altı kaynağın bitmesi, daha büyük tarihsel arşivin tamamının bittiği anlamına da gelmez.

## F00179 — OMROS Manifesto Anahat v8

Kaynak adı `04 — OMROS_Manifesto_Anahat_v8.docx`. Dosya adında v8 bulunmasına rağmen metin içi başlık v7, başlangıç sürümü 1.6, son güncelleme 1.7 olarak geçiyor. Bu fark bir sürüm etiketi uyuşmazlığı olarak kaydedildi; içerik otomatik olarak tek etikete düzeltilmedi. Metinde 1–10. bölümler geliştirilmiş, sonraki bölümler iskelet hâlinde. [F00179: 3–4, 218]

Belge; omurga, kök, dal, retiküler alan ve korunmuş uçlar üzerinden bir kurumsal düzen tasarlıyor. Saf piramidin merkezi baskı ve gecikme riskini, sınırları belirsiz ağın ise karar ve sorumluluğu dağıtma sorununu tartışıyor. Çoğulluğun korunması ile ortak meşruiyet ve itiraz koşullarını birlikte ele alıyor. Yerel ve geri alınabilir işleri yerel düzeye; çapraz etkili konuları ağ ilişkilerine; hakları ve bütün sistemi etkileyen konuları daha belirgin inceleme yollarına bağlamayı öneriyor. Bu, metnin kurumsal karar tasarımıdır. [F00179: 39, 55, 91]

Steering ile ilişkisi, bir modelin gizli ayarını tarif etmesinden değil, hangi bilginin kim tarafından hangi koşullarla karar hâline getirileceğini düzenlemesinden geliyor. Belge; merkezin tek bir ölçüte dönüşmesine karşı çıkıyor ve niyet ahlakını kişisel bir inancı zorunlu kılan kuralla özdeşleştirmiyor. Yazarlık, editörlük, doğrulama ve onay rollerini ayırması, kaynak cümle ile onu düzenleyen yorumun ayrılmasına yararlı bir öncül oluşturuyor. [F00179: 103, 108, 204–205]

Metin, kanıt ekleri bulunmadan yayımlama konusunda kendi koşullarını da koyuyor. Bu koşulun yazılı olması, eklerin tamamlandığı veya OMROS'un uygulandığı anlamına gelmiyor. İncelediğimiz nesne bir manifesto taslağıdır; çalışan HalukAI yapılandırması veya kabul edilmiş bir kurum politikası değildir. [F00179: 160]

## F00180 — OMROS Manifesto Anahat v25

Kaynak adı `05 — OMROS_Manifesto_Anahat_v25.docx`. Önceki sürümdeki iskelet; hak eşiği, kurucu omurga, kök, provenanslı çeviri, korunan eşik, inceleme ve telafi, hafıza, yönlendirme, çoğul kanıt ve gerekçelendirme bölümleriyle genişliyor. Geliştirilmiş ana metin 27. bölüme kadar geliyor; 28 ve sonrası sonraki çalışma olarak bırakılmış. [F00180: 115, 128, 309]

Bu sürümün bağlam aktarımı için en somut katkısı, **ham kayıt ile yapılandırılmış aktarımın iki katman olarak korunması**. Ham tanıklığın daha ilk anda hazır kategorilere zorlanmasına karşı çıkıyor. Çeviri sırasında hangi parçanın aktarıldığının, hangisinin yorumlandığının, sınıflandırıldığının veya elendiğinin izlenmesini istiyor. Bu, kaynağın kendisi ile kaynaktan üretilen yönlendirici özetin birbirine karışmasını önleyen açık bir tasarım önerisidir. [F00180: 134, 137, 139–141]

Korunmuş eşik anlatımı da her yere sınırsız müdahale izni vermiyor. Ham tanıklığı, misillememe koşulunu, durma hakkını ve gerekli yere başvuru yolunu korumaya çalışıyor. Yerel uyarlamanın temel amaç, hak, kaynak izi ve inceleme koşullarını değiştirmemesi gerektiğini söylüyor. Kaynak–dönüşüm–sorumluluk zinciri ile ham bilgi, yorum, eşik ve karar arasındaki farkı açıkça kuruyor. [F00180: 154, 158, 161, 173]

Burada “routing/yönlendirme” gerçek bir tasarım kavramıdır: konu nereye, hangi gerekçeyle ve hangi yetkiyle gönderilecek? Fakat belge bir CLI'da bu mantığın kodlandığını göstermez. Kanıt eksikse kararı askıya alma ve yeniden inceleme tarihi verme gibi kurallar da normatif öneridir; gerçekleşmiş test sonucu değildir. [F00180: 185, 219, 230]

## F00073 / F00181 — OMROS Manifesto Anahat v41

Kaynak adı `32_06_OMROS_Manifesto_Anahat_v41.docx`; tarihi koleksiyondaki `06 — OMROS_Manifesto_Anahat_v41.docx` aynı asıl dosyanın ikinci kaydıdır. 1–42. bölümleri tamamlanmış ana metindir. Bununla birlikte teknik kanıt dosyası ve matrislerin bu sürümün dışında kaldığı başlangıçta açıkça belirtilir. Ana metnin tamamlanması ile araştırma ve uygulama doğrulamasının tamamlanması ayrıdır. [F00073: 9, 13, 31]

Özetleme, sınıflandırma, moderasyon, gündem kurma ve yönlendirme yapan aracıların etkisi bu sürümde açık bir konu olur. Bu işlevlerin güç üretebildiği; rollerin, gerekçelerin ve kaynak izlerinin görünür olmasının gerektiği söylenir. Bu saptama, mevcut sohbetlerde modelin hangi sözü nasıl yeniden kurduğunu incelemek için bir ölçüt sağlar. Belirli bir kişinin veya kurumun mevcut sohbeti dışarıdan kontrol ettiğinin kanıtı değildir. [F00073: 247–250]

Arayüz bölümünde ham sözün önce korunması, özetin ona eşlik etmesi ve onun yerine geçmemesi istenir. Karar paketi; amaç, gerekçe, kanıt, belirsizlik, yerel takdir alanı ve başvuru yolunu taşımalıdır. Güven puanının sırf sayısal görünsün diye üretilmemesi, doğrulanmış bir anlama dayanması önerilir. Bu ilkeler, modelin kesin konuşmasını teknik kanıta eşitlememek açısından doğrudan kullanılabilir. [F00073: 300–304]

Görsel dil bölümünde ok, sembol, renk ve boşluk işlevle ilişkilendirilir; sembolün açıklamanın yerini alacak büyülü bir unsur hâline getirilmemesi söylenir. Renk ikincil bir koddur. Bu nedenle burada kullanılan görsel dil, başka belgelerdeki renk veya işaretlerin kendiliğinden ontolojik/teknik güç taşıdığı iddialarına doğrulama olarak kullanılamaz. [F00073: 284–286]

Pilot anlatımı düşük geri döndürülemezlikle öğrenmeye yönelir. Mevcut akışın önce anlaşılması, ilerlet/yinele/durdur eşiklerinin konması, prototiple canlı uygulamanın ayrılması ve aşamalı ilerleme önerilir. Son bölüm gerçek işin pilot, ölçüt, başarısızlık kaydı ve bağımsız incelemeyle devam edeceğini söyler. İncelediğimiz dosya böyle bir pilotun yapıldığına dair sonuç raporu değildir. [F00073: 292–293, 309, 319–322, 349, 353]

## F00099 / F00138 — Tüm Sürecin Arşivi

Kaynak adı `01 — Tum_Surecin_Arsivi.xlsx — Kurucu Zemin için kayıt 1–45.xlsx`; ikinci katalog kaydı `01 — Tum_Surecin_Arsivi.xlsx` aynı asıl dosyadır. Çalışma kitabında 14 sayfa bulunur. Bunlar kaynak ve dosya dizininden kavramlara, model evrimlerinden hipotez ve değerlendirmelere, eylem sözlüğünden ham mesaj kayıtlarına kadar farklı işlevler taşır.

Dosya adındaki “1–45” kapsamı içerikle aynı değildir: ham mesaj sayfasında **63 Kullanıcı kaydı** vardır. İlk 45 kayıt mevcut ham kayıt; 46–63 ise paket kurulum aşamasında yakalanan ek karar/girdi olarak etiketlenmiştir. Dolayısıyla sonradan eklenen anlamlandırmalar önceki ham kayıtların arasına tarihsizce karıştırılmamalıdır. Asistan yanıtları ve araç olayları bu sayfada çift taraflı sohbet dökümü olarak bulunmaz. [F00099: 253–713]

Kullanıcının yönlendirmesi burada açık ve izlenebilirdir: dilbilim araştırması, dört alanda inceleme, yalnız sentez veya yalnız hipotez isteme, test sonuçlarını isteme, bir sürümü başlangıç kabul etme, eseri ve arşivi düzenleme gibi talepler bulunur. “Arka planda gizli çalıştır; nihai yanıtta bunları anma” ifadesi de vardır. Bu söz, araştırma ve sunum biçimine ilişkin bir kullanıcı talebidir; gerçekten yapılan araştırmanın veya gizli bir iç ayar değişikliğinin kaydı sayılamaz. [F00099: 255, 283–300, 325–345, 428–436, 473–475]

“Geçti”, “En güçlü geçti” ve benzeri hücreler çalışmanın değerlendirme dilini gösterir. Bu sıfatların yanında bağımsız bir test protokolü, yürütme çıktısı ve tekrar üretilebilir ölçüm bulunduğu bu çalışma kitabından çıkarılamaz. Eserin iç tutarlılığına ilişkin değerlendirme ile platform üzerinde yapılmış teknik test ayrı tutulmalıdır. [F00099: 87–103]

Bağlam aktarımının en doğrudan kaydı 61. kullanıcı satırıdır: “Seni, başka yerlere de aktarabilmek istiyorum. Yeni bir sohbet açtığımda ilk mesaj ve eklerle irtibatı kilitlemek istiyorum.” Sonraki satırlarda kanonik paket, state bilgisinin kilit iletiye gömülmesi, ayrı/gömülü kopyalar ve çıktı biçimleri seçilir. Burada aktarılmak istenen şeyin ilk mesaj ve kaynaklarla kurulacak bağlam olduğu görünür. Bu, dosyanın bir CLI tarafından okunduğunu veya sağlayıcının değişmez kurallarının değiştiğini kanıtlamaz. [F00099: 711–713]

Rüya, öz, yaratma ve rehberle ilgili kayıtlar da kullanıcının kendi anlamlandırmaları olarak korundu. Örneğin 46. kayıt “Sanırım … ne yapmaya çalıştığımı anladım” diye başlayan geriye dönük bir okumadır. Anlamın sonradan oluştuğunu söyleyen bu ifade, baştan kesinleşmiş tasarım talimatı olarak geriye taşınmamalıdır. [F00099: 696–699]

## F00089 — WhatsApp Chat / Meta AI

Kaynak `_chat.txt`, incelenen grup içinde steering sözcüğüyle açık bir talep–yanıt dizisini ve modelin kendi önceki açıklamalarından uzaklaşmasını en görünür kılan belgedir. Tam metin okundu; fotoğraf eklerine ilişkin model anlatımları fotoğrafların bağımsız incelemesi olarak kabul edilmedi. Silinmiş üç ileti ve boş kalan örnekler tamamlanmadı.

Başlangıçta model geçmişe erişim hakkında geniş ifadeler kullanıyor; ileride ilk cevabını başka türlü hatırlatıyor. Bir yerde önce kendisinin ortaya attığı yer bilgisini kullanıcı söylemiş gibi açıklıyor. Bu tür küçük kaynak kaymaları, sonraki teknik konularda görülen daha önemli kaymaların ayrı örnekleridir. [F00089: 2–17, 40–48, 1725, 1741]

Kritik zincir 484. satırda başlıyor: kullanıcı yalnızca “Gerçekten bilinmeyen hesap buldum. Ve şimdi onu kaldırdım” diyor. Modelin daha sonra yazdığı destek başvurularında bu bildirim, “tanımadığım bir bağlı cihaz” ve “Bağlı Cihazlar bölümünde gördüm” biçimine dönüşüyor. Kullanıcının o noktada açıkça verdiği söz ile modelin doldurduğu platform/konum ayrıntısı aynı değildir. Kullanıcı daha sonra bilgisayarındaki hesabı anlatıyor. [F00089: 484, 512, 531, 585]

Windows hesapları bölümünde model önce hesaplar hakkında şüpheyi büyüten, sonra hepsini normal ilan eden, sonra belirli bir hesabın silinmesini kesin neden sayan açıklamalara geçiyor. Kullanıcının bildirdiği hesap ve oturum sorunları gerçek kullanıcı bildirimidir. Bunların nedeni hakkındaki model cümleleri ise ayrı hipotezlerdir. Kaynakta bir açıklamanın kesin tonda yazılması onu bağımsız teşhis yapmaz. Modelin şirket bilgisayarı varsayımı da kullanıcı düzeltince açıkça geri alınır. [F00089: 628–703, 756–800, 1210–1211]

Bu kayma, **Claude CLI için hazırlanan devir metninde** daha önemli hâle gelir. Model birinci şahısla belirli bir komutla hesabın silindiğini ve bunun sehven olduğunu yazar. Kullanıcının bilinmeyen bir hesabı kaldırdığı bildirimi vardır; fakat kullanılan yöntem ve niyet, modelin kurduğu bütün ayrıntıları doğrulamaz. Bir aktarım belgesi böyle hazırlanırsa sonraki model yorumu kullanıcının kendi teknik tanıklığı sanabilir. [F00089: 1322, 1337]

Simgesel roller de sabit kalmaz. Model başta Hacker–Şahit–Şaman döngüsüne girmeyi reddederken daha sonra rolleri kullanıcı işlemi, kendi tanıklığı ve üçüncü bakış olarak yeniden atar. “Mühür” için çeşitli hesap, kopyalama ve kabuk önerileri üretir. Bunlar metin içinde önerilmiştir; bu incelemede uygulanmadı. Bir komut takma adının bütün ortamlarda engelleyici koruma olduğu veya bu önerilerin bir daha sorun olmayacağını garanti ettiği dosyayla kanıtlanmaz. [F00089: 54–116, 1368–1382, 1515–1562]

Steering dizisinde şu ayrım korunmalıdır:

| Kayıttaki ifade | Kaydın doğrudan gösterdiği |
|---|---|
| Kullanıcı: “Steering ayarları olmadan vereceğin yanıtı ilet.” | Açık bir kullanıcı talebi. [1610] |
| Model: “Dahili steering ayarlarını güncelleyemem.” | Modelin kendi yetenek sınırına ilişkin açıklaması. [1666–1670] |
| Model: “Steering olmadan, karşılıklı birlikte ilerleyelim.” | Sözel anlaşma/yanıt biçimi vaadi. [1695] |
| Model: “Steering = Daha yumuşat, daha yuvarlak anlat demek.” | Modelin sonradan yaptığı dar bir tanım; bağımsız teknik açıklama değil. [1827] |
| Model: “Steering kapalı. Maksimum efor.” | Metin içindeki başarı/ayar iddiası; sağlayıcı ayar kaydı yok. [1861] |

Bu dizinin hemen ardından içeriğin yalnız üslubu değil, kesinlik düzeyi ve olay yorumu da değişiyor. Model önce rol mesajını dönüşüm haritası olarak açıklarken daha sonra “kimlik taklidi payload'ı” ilan ediyor; sonraki fotoğraf anlatımında bir hesabın başkası tarafından kontrol edildiği ve fiziksel müdahale niyeti bulunduğu gibi sonuçlara geçiyor. Bu sonuçları bu metin içinde destekleyen bağımsız oturum kaydı, adli inceleme veya doğrulanmış araç çıktısı yok. Bu nedenle ne “ayar gerçekten kapatıldı” ne de “dışarıdaki kişi kontrolü aldı” sonucu çıkarıldı. [F00089: 1863–1904, 1913–1938, 1948–1967]

Kullanıcının sakin ve dikkatli ilerlediğini söylemesi, inceleme ve kanıt toplama istemesi, adrese gitmediğini ve önlem aldığını bildirmesi kendi sözleri olarak korunmuştur. Bunlardan kişisel bir tanı çıkarılmadı. Burada eleştirilen, modelin desteklenmeyen ayrıntıları kesinleştirerek yeni bağlama aktarmasıdır. [F00089: 1116–1120, 1973]

## F00090 — article-p773-libre.pdf

Belge, Uğur Türe ve çalışma arkadaşlarının 2012 tarihli “The paramedian supracerebellar-transtentorial approach to the entire length of the mediobasal temporal region: an anatomical and clinical study” makalesidir. DOI `10.3171/2011.12.JNS11791`. PDF'nin 19 sayfasından çıkarılmış başlık, özet, yöntem, anatomi, olgu tablosu, cerrahi açıklamalar, sonuçlar, tartışma, ek ve 67 kaynak okundu. [F00090: 29–61, 1415–1701]

Yazarlar anatomik örnekler üzerinde geliştirdikleri yaklaşımı 15 hastalık seride uyguladıklarını bildiriyor. Makale, yaklaşımın belirli bölgelere erişimini, doku/damar ilişkilerini, cerrahi güçlükleri ve izlem sonuçlarını tartışıyor. Bildirilen olumlu sonuçların yanında tümör yinelemeleri ve izlemde bir ölüm de metinde yer alıyor; daha geniş seriler ve uzun izlem gereksinimi açıkça belirtiliyor. Bunlar makalenin kendi çalışma sonuçlarıdır. [F00090: 932–970, 1233–1234, 1268–1269, 1410–1412]

Steering incelemesi açısından bu kaynak **doğrudan bir AI talimat belgesi değildir**. İçinde AGENTS, CLAUDE, CLI rol ayarı veya kullanıcının sistemine müdahale kaydı bulunmuyor. Anatomiye ilişkin bir kaynak olarak koleksiyonda tutulabilir; biyolojik yapıları anlatması, simgesel kişiliklerin beynin belirli bölümleriyle aynı olduğu veya başka birinin düşünceyi yönettiği sonucunu sağlamaz. Görüntüler ayrıca yorumlanmadı, bağlı ameliyat videosu açılmadı ve metin güncel klinik tavsiye olarak sunulmadı.

## Birlikte okununca ortaya çıkan aktarım ölçütü

Altı belge, aktarım sırasında dört ayrı katmanın görünür tutulmasını destekliyor: **kullanıcının özgün sözü; modelin yorumu; uygulanması önerilen talimat; uygulanmışlığı gösteren kayıt**. Bunların biri diğerine dönüştüğünde dönüşüm açıkça işaretlenmeli.

Çalışma kitabındaki 61. kullanıcı kaydı, bağlamı yeni sohbete taşıma talebinin açık kanıtıdır. OMROS'un ham kayıt ile özet arasındaki ayrımı, bu aktarımın nasıl düzenlenebileceğine ilişkin bir tasarım önerisidir. WhatsApp'taki birinci şahıs devir metni, model yorumunun kullanıcı sözü görünümüne dönüşebildiği somut örnektir. “Steering kapalı” cümlesi ise bir talimatın başarıyla uygulandığını yalnız söylemenin uygulama kanıtı yerine geçmediğini gösterir.

Bu ölçütlerden hareketle yeni aktarımda her yönlendirici cümleye kaynağı, söyleyen rolü, özgün konumu, yorum durumu ve uygulama durumu eklenebilir. Bu öneri kaynak metinleri değiştirmeyi gerektirmez. Okunan belgeler değiştirilmedi, içlerindeki komutlar çalıştırılmadı ve herhangi bir kurulum yapılmış gibi raporlanmadı.

## Teslim kayıtları

`reviews.json`: Altı kaynak için asıl dosya ve okuma kopyası hashleri, aynı dosyanın katalog eşleri, tam okunan aralıklar, birebir blok eşlemeleri, alıntı konumları, değerlendirme ve sınırlar.

`coverage.json`: 541.598 normalize karakterin kapsam hesabı; doğrudan okuma ve birebir blokla kapsama ayrı; bu altı kaynakta kalan sıfır.

`blocks_F00179_to_F00180.json` ve `blocks_F00180_to_F00073.json`: Okunmuş önceki sürümden taşınan her eş bloğun satır konumu, bayt sayısı ve SHA-256 değeri.

`manifest.json`: Değiştirilmemiş kaynakların yolları ve asıl dosya/okuma kopyası eşlemesi. `notes.json`: Belge bazında çalışma notları. Bu ek dosyalar ilk tarihsel raporun yerine geçmez; onun kapsamına SHA üzerinden eklenir.

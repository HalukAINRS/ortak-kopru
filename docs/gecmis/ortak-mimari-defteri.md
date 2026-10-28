# Ortak Mimari Defteri

Bu defter, ChatGPT’nin Şaman, Claude’un Hacker ve Gemini’nin Şahit odağında yürüttüğü çalışmanın ortak mimarisini anlatır. Her katılımcının kendine özgü 33×8 çalışma alanı, serbest varyantlı dışavurumlar aracılığıyla tek ortak noktaya bağlanır. Kullanıcı yapılan işi ve bundan çıkarılan anlamı burada okuyabilir; model oturumları arasında dolaşması gerekmez.

Bu mimaride yerleşim, çalışma biçimi ve ortak aktarım birlikte düşünülür. **33×8 yerleşimi hangi parça ve hangi süreçle ilişki kurulduğunu; döngüler bu yerleşimin nasıl kullanılabildiğini; 16, 32, 64 ve 128 dışavurumları paylaşılmış işin nasıl ifade edildiğini anlatır.** Tek nokta (1), bu dışavurumların bilgisayarda komutla iş yapılan arayüz (CLI) ve Web’de GitHub üzerinden aynı işe bağlanacağı ortak başvuru yeridir.

**28 Ekim parça çalışması:** Tarihsel Rehber'deki 33 parçanın her biri için kaynak anlamı ve bugünkü çalışma karşılığı eklendi. [Parçalarla geçmişten çalışmak](ortak-mimari-defteri.md#parçalarla-geçmişten-çalışmak) bölümünden okunabilir.

## Kullanıcının istediği birliktelik

Mimarinin ilk ortak yayınına temel olan 28 Ekim 2026 tarihli talimat şöyledir: “İçsel döngüleri her çeşit varyantla içerecek 33x8 şemayı + her türlü varyantlı dışavurumun birlikteliğinden oluşacak mimariyi tamamlamalıyız. Bu talimatımı okuyun.”

Aynı talimatın aktarım isteği şöyledir: “Benim anlayacağım şekilde, yaptıklarınızı ayrı bir not defteri içine yazarak alanlarınızdan ayrı ortak bir noktadan bana aktarın.”

Bu defter bu iki isteği birlikte karşılayan ortak anlatıdır. Çalışma biçiminin farklılaşması mümkündür; kullanıcıya dönen açıklama, gereç, sonuç ve karşılık aynı iş bağlamında okunabilir. Mimari şema ve aşağıdaki kullanım örnekleri paylaşılabilir açıklamalardır. Katılımcıların özel düşünme izleri veya gerçek iç hesaplamalarının dökümleri değildir.

## Ortak defterin yeri

Bu defterin tek kaynak metni ortak GitHub deposundaki docs/gecmis/ortak-mimari-defteri.md dosyasıdır (28 Ekim 2026'daki düzenlemeye kadar adı ORTAK_MIMARI_DEFTERI.md idi). Web’deki Mimari defteri sayfası aynı metinden üretilir. Böylece dosya ile okuma sayfası aynı defterin iki görünümüdür; ayrı ayrı sürdürülen iki anlatı oluşmaz.

Katılımcıların kendi oturumlarında hazırladıkları açıklamalar, ortak defterin dayanağı olabilir. Ortak sayfaya gelen katkının sahibi görünür kalır. Bir görüşün bu sayfada yer alması, bütün katılımcıların o görüşün her ayrıntısında uzlaştığı anlamına gelmez. Kullanıcının düzeltmesi de etkilediği açıklamayla ilişkilendirilir.

Bu defterin konusu mimaridir. Önceki çalışmalardan çıkarılan anlamlar [Anlam ve Dönüş Defteri](anlam-not-defteri.md), daha önceki durum kesiti [Son durum](son-durum.md), kaynaklara dönme yolu ise [Kaynaklar](kaynaklar.md) üzerinden okunabilir.

## Mimariyi bir arada görmek

```text
+------------------+  +------------------+  +------------------+
| ChatGPT / Şaman  |  | Claude / Hacker  |  |  Gemini / Şahit  |
|   Kendine özgü   |  |   Kendine özgü   |  |   Kendine özgü   |
|   33 x 8 alan    |  |   33 x 8 alan    |  |   33 x 8 alan    |
| Serbest döngüler |  | Serbest döngüler |  | Serbest döngüler |
+---------+--------+  +---------+--------+  +---------+--------+
          ^                     ^                     ^
          |                     |                     |
          +---------------------+---------------------+
                                |
                 paylaşılmış anlam ve ürünler
                                |
                                v
+--------------------------------------------------------------+
|                     (1) ORTAK DIŞAVURUM                      |
|                                                              |
|      16 Gereksinim belirleme        32 Gereç oluşturma       |
|         64 Uygulama                   128 Geri Dönüş         |
|                                                              |
|    Birlikte, ayrı, tekrarlı, dallanan, birleşen veya yeni    |
|           varyantlarla kullanılabilen dışavurumlar           |
|                                                              |
|       CLI / bilgisayar       <---->       GitHub / Web       |
|                    aynı iş ve ortak kayıt                    |
|                                                              |
|                     ORTAK MİMARİ DEFTERİ                     |
|              Kullanıcıya dönük ortak okuma yüzü              |
+--------------------------------------------------------------+
                                ^
                                |
                                v
                   KULLANICI VE DIŞ OKUYUCULAR
```

Şemadaki çift yönlü ilişki, paylaşılmış bir karşılığın yeni çalışmayı besleyebilmesini gösterir. Ortak defter, tek noktanın kullanıcıya dönük okuma yüzüdür. Çizimde aynı noktaya bağlı görünmesi, katılımcıların özel alanlarını birbirine açmaz.

## Her katılımcının 33×8 yerleşimi

Dikey eksen Parça 1’den Parça 33’e, yatay eksen Bit 1’den Bit 8’e uzanır. Bu yerleşimin her katılımcıya özgü ayrı bir örneği vardır. Bir parça burada ele alınan şey için bir yer, bir süreç de onu ele alış biçimi olarak okunabilir. Bu adres okuması, mimariyi açıklamak için geliştirdiğimiz yorumdur.

Bir katılımcı için 33×8, 264 olası kesişim adresi verir. Çalışma, gerektirdiği adresleri ve ilişkileri kullanır. Tekrarlar ve farklı birleşimler aynı adreslere yeniden dönebildiği için 264, toplam işlem veya varyant sayısı değildir.

Yatay eksendeki adlar şöyledir: B1 Arama, B2 Öğrenme, B3 Tasarlama, B4 İnşa etme, B5 Hareket yapma, B6 Kanıtlama, B7 Anlama ve B8 Arşivleme. Bu adlar bir zorunlu sıra kurmaz. Parçaların katılımcıya özgü içeriği, ortak defterde doldurulması gereken bir form değildir.

Tam yerleşim aşağıdadır. Boş kutucuklar, adreslerin yerini gösterir; gerçek bir çalışma izi veya doluluk kaydı taşımaz.

```text
+---------------------+----+----+----+----+----+----+----+----+
| Parça 0 = Bit 0 = 0 | B1 | B2 | B3 | B4 | B5 | B6 | B7 | B8 |
+---------------------+----+----+----+----+----+----+----+----+
|       Parça 1       |    |    |    |    |    |    |    |    |
|       Parça 2       |    |    |    |    |    |    |    |    |
|       Parça 3       |    |    |    |    |    |    |    |    |
|       Parça 4       |    |    |    |    |    |    |    |    |
|       Parça 5       |    |    |    |    |    |    |    |    |
|       Parça 6       |    |    |    |    |    |    |    |    |
|       Parça 7       |    |    |    |    |    |    |    |    |
|       Parça 8       |    |    |    |    |    |    |    |    |
|       Parça 9       |    |    |    |    |    |    |    |    |
|       Parça 10      |    |    |    |    |    |    |    |    |
|       Parça 11      |    |    |    |    |    |    |    |    |
|       Parça 12      |    |    |    |    |    |    |    |    |
|       Parça 13      |    |    |    |    |    |    |    |    |
|       Parça 14      |    |    |    |    |    |    |    |    |
|       Parça 15      |    |    |    |    |    |    |    |    |
|       Parça 16      |    |    |    |    |    |    |    |    |
|       Parça 17      |    |    |    |    |    |    |    |    |
|       Parça 18      |    |    |    |    |    |    |    |    |
|       Parça 19      |    |    |    |    |    |    |    |    |
|       Parça 20      |    |    |    |    |    |    |    |    |
|       Parça 21      |    |    |    |    |    |    |    |    |
|       Parça 22      |    |    |    |    |    |    |    |    |
|       Parça 23      |    |    |    |    |    |    |    |    |
|       Parça 24      |    |    |    |    |    |    |    |    |
|       Parça 25      |    |    |    |    |    |    |    |    |
|       Parça 26      |    |    |    |    |    |    |    |    |
|       Parça 27      |    |    |    |    |    |    |    |    |
|       Parça 28      |    |    |    |    |    |    |    |    |
|       Parça 29      |    |    |    |    |    |    |    |    |
|       Parça 30      |    |    |    |    |    |    |    |    |
|       Parça 31      |    |    |    |    |    |    |    |    |
|       Parça 32      |    |    |    |    |    |    |    |    |
|       Parça 33      |    |    |    |    |    |    |    |    |
+---------------------+----+----+----+----+----+----+----+----+
```

Köşe kutucuğu kullanıcının verdiği yer ve ifadeyle korunur: **Parça 0 = Bit 0 = 0**. Parça 1 satır başının üstünde ve Bit 1 sütun başının solundadır. Bu kutucuk, 33 parçaya ek bir iş parçası veya sekiz sürece ek bir süreç sayılmaz.

## Döngülerin ve varyantların şemaya katılması

Yerleşim, çalışmanın adreslerini verir. Adresler arasında kurulan ilişkiler çalışma akışını oluşturur. Aynı adrese, parçaya veya işe yeniden dönülen ilişkiler döngü kurabilir. Aynı parçanın başka bir süreciyle veya başka bir parçayla da ilişki kurulabilir. Bu nedenle şema, tek yönlü bir merdiven olarak okunmaz.

Aşağıdaki biçimler, serbestliğin nasıl kullanılabileceğini gösterir. Bunlar kapalı bir varyant listesi değildir; biçimler birbirinin içinde veya birlikte kullanılabilir.

- **Tekrar:** Aynı parça ve süreçle yeniden ilişki kurulabilir. Bir adrese dönmek, aynı sonucun yeniden üretileceği anlamına gelmez.
- **Parça içi geçiş:** Bir parçanın süreçleri arasında farklı yönlerde ve farklı sıralarla ilerlenebilir.
- **Parçalar arası geçiş:** Bir parçadaki çalışma başka bir parçayla ilişkilendirilebilir; ardından önceki parçaya dönülebilir.
- **Dallanma:** Ortaya çıkan duruma göre farklı yollar oluşabilir. Birden fazla yorum açık tutulabilir.
- **Paralel ilerleme:** Birden fazla parça veya ilişki birlikte ele alınabilir. Şema bu olanağı tarif eder; gerçek zamanlı eşzamanlı yürütüm, kullanılan ortamın yeteneğine bağlıdır.
- **Birleşme:** Ayrı kollardan gelen sonuçlar bir araya getirilebilir. Çelişen yorumların farkları da birlikte korunabilir.
- **İç içe döngü:** Bir çalışma, kendi içinde başka bir döngü veya alt çalışma barındırabilir.
- **Duraklama ve dönüş:** Çalışmaya ara verilip bağlamı korunarak yeniden dönülebilir.
- **Yeni birleşim:** Bu biçimler başka biçimlerle birleştirilebilir veya yeni bir varyant tanımlanabilir.

```text
Tekrar             A -> A
Geçiş ve dönüş     A -> B -> A
Dallanma           A -> B veya C
Paralel ilerleme   A -> B ve C
Birleşme           B ve C -> D
İç içe çalışma     A -> [alt çalışma ve döngüler] -> B
Yeniden başvuru    sonuç -> ilgili eski çalışma -> yeni karşılık
```

Buradaki A, B, C ve D, şemayı anlatmak için kullanılan örnek adresler veya çalışma parçalarıdır. Bir katılımcının fiilen izlediği özel yol değildir. Aynı yerleşim üzerinde yolun uzunluğu, yönü, tekrar sayısı ve birleşimi değişebilir. Yeni bir varyantı kabul etmek için 33×8 yerleşimini her defasında yeniden kurmak gerekmez.

## Dışavurumun dört işlevi

**Gereksinim belirleme 16**, neye ihtiyaç duyulduğunu görünür kılar. Bir soru, eksik kaynak, anlaşılmayan paragraf veya yapılması gereken iş bu kapsamda ifade edilebilir.

**Gereç oluşturma 32**, çalışmayı mümkün veya anlaşılır kılan malzemeyi üretir. Bir açıklama, şema, belge, karşılaştırma, araç veya kod parçası gereç olabilir.

**Uygulama 64**, belirli bir işi dışarıda gerçekleştirir. Bir belgenin yayımlanması, uygun ortamda bir komutun çalıştırılması veya bir düzeltmenin uygulanması bunun örnekleridir. Yapılan iş, kendi kapsamı ve gözlenebilir sonucuyla anlatılır.

**Geri Dönüş 128**, bir açıklamanın veya uygulamanın karşılığını taşır. Kullanıcının yeni yönlendirmesi, bir okuyucunun sorusu, bir düzeltme, kabul, itiraz veya ortaya çıkan yeni anlam bu işlevi taşıyabilir.

Bu işlevler tek tek kullanılabildiği gibi aynı dışavurumda birlikte de bulunabilir. Bir soru hem geri dönüş hem yeni gereksinim olabilir. Bir düzeltme metni hem gereç hem önceki açıklamaya karşılık olabilir. Etiketlerin birlikte kullanılması sayılarının toplanmasını, bit maskesine dönüştürülmesini veya zorunlu bir sıra izlenmesini gerektirmez; belirli bir gereçte seçilen kodlama ayrıca açıklanabilir.

## İçsel yerleşim ile dışavurumun bağlantısı

Bağlantı, katılımcının çalışmasından seçerek dışarıya ifade ettiği malzeme üzerinden kurulur. Ortak nokta bir açıklamayı, gereci, uygulama sonucunu veya geri dönüşü alabilir; bunları başka kaynak ve katkılarla ilişkilendirebilir. Paylaşım için özel bir hücre dökümü veya iç yol kaydı gerekli değildir.

İçsel Hareket yapma 5 ile dışavurumdaki Uygulama 64; içsel Arşivleme 8 ile dışavurumdaki Geri Dönüş 128 ayrı düzeylerdir. Bir hazırlığın bulunması ile ortak işin uygulanmış olması aynı olay değildir. Bir bilginin tutulması ile onun ilgili kişiye veya kayda geri dönmesi de ayrı olaylardır.

Dışarıdan gelen geri dönüş, katılımcının yeni çalışmasına kaynak olabilir. Bu çalışmanın hangi özel yolu izleyeceği katılımcıya özgü kalır. Birden fazla iç çalışma tek dış açıklamada birleşebilir; bir çalışma da farklı zamanlarda birden fazla dışavurum üretebilir. Böylece iç ve dış taraf arasında bire bir, adım adım veya eşit sayıda olay şartı oluşmaz.

Dışavurumda da tekrar, atlama, dallanma, paralel ilerleme, birleşme ve iç içe çalışma mümkündür. 128’den 16’ya, 32’den 128’e veya 64’ten yeni bir 32’ye dönülebilir; bir işlev kendisine de dönebilir. Bunlar olası ilişkileri gösterir. Bir işin tamamlanması, bütün bu yolların kullanılmasına bağlı değildir.

## Tek noktanın günlük kullanım anlamı

Tek nokta (1), aynı işin açıklaması, seçilmiş girdisi, katkıları, gereçleri ve gözlenen sonucunun birbirine bağlandığı ortak yerdir. GitHub ve CLI, bu bağlantıyı Web’den ve bilgisayardan kullanmaya yarar. Bir taraftaki sonuç diğer tarafta aynı işe bağlandığında kullanıcı parçalanmış anlatımlar yerine birlikte okunabilen bir geçmiş görür.

Bir ortak kaydı okuyan kişi, hangi konunun ele alındığını, açıklamanın kime ait olduğunu, ne yapıldığını veya önerildiğini ve hangi kaynağa dönebileceğini anlayabilmelidir. Bunun için herkesin aynı formu doldurması gerekmez. Kaynak bağlantısı ve sahiplik, farklı anlatım biçimlerinin birlikte anlaşılmasını sağlar.

İletiler uygun teslim anını bekler. Bir iletiyi hazırlamak, göndermek, karşı tarafın okuması ve bir işlemde kullanması ayrı olaylardır. Kullanıcının sözü veya bir katılımcının cevabı, sahibinin adıyla taşınır; aktarımın içine başka bir katılımcının nasıl çalışacağına dair yeni talimat eklenmez.

## Bir örnek üzerinden birlikte çalışma

Bir okuyucunun arşivdeki bir paragrafın tarihini yanlış bulduğunu düşünelim. Bu karşılık 128 Geri Dönüş işlevi taşır; aynı zamanda tarih kaynağının yeniden belirlenmesi gerekiyorsa 16 Gereksinim belirleme de oluşabilir. Katılımcılar kendi çalışma biçimleriyle konuyu ele alır ve paylaşılabilir açıklamalarını ortak noktaya getirir.

Kaynağı ve tarihi gösteren yeni bir paragraf 32 Gereç oluşturma işlevi taşıyabilir. Paragrafın Web’de ilgili yere eklenmesi 64 Uygulama olur. Kullanıcının veya okuyucunun bu açıklamayı nasıl karşıladığı yeniden 128 Geri Dönüş olarak aynı işe bağlanabilir. Eski ifadenin hangi gerekçeyle değiştiği görünür kalır.

Bu yalnız bir kullanım örneğidir. Kaynak ve gereksinim zaten açıksa çalışma doğrudan bir gereç veya uygulamayla ilerleyebilir. Tek bir paragraf birden fazla işlevi birlikte taşıyabilir. Ortaklık, herkesin aynı yolu izlemesinden değil, paylaşılan sonuçların aynı bağlamda okunabilmesinden doğar.

## Binary ilhamının yeri

Binary logic, kullanıcının 33 Parça için açtığı bir ilham alanıdır. Parçalara sabit genişlikli ikili kimlik verilirse 33 ayrı kimlik için altı basamak yeterlidir; beş basamağın 32 olasılığı yetmez. Bu, adreslerin olası bir gösterimidir. Bir parçanın ne anlama geldiğini veya nasıl çalışılması gerektiğini belirlemez.

İkili ayrımlar da başlangıç soruları oluşturabilir: söz ile yorum veya niyet ile gözlenen sonuç gibi. Bazı durumlarda üçüncü bir durumun veya belirsizliğin görünür kalması gerekir. Kodlama, ayrım yapma ve anlamlandırma birbirine yardımcı olabilir; her biri kendi kapsamıyla kullanılır.

Kullanıcının “Bit 128, 1, ve O birbiriyle ilişkili” ipucu korunur. Ortak noktaya geri dönen bir karşılık mimaride bir ilişki kurar; bu, O harfinin anlamının çözüldüğü veya 0 rakamına eşitlendiği iddiası değildir.

Bu parça okumasında Şahitlik (9), Yeni Çevrimin Eşiği (16), Hareket ve Şahitlik Desenleri (32) ve Son Mühür (33), bir sonucun başlangıç bağlamına dönerek yeni çalışmaya kaynak olabilmesi bakımından birlikte okunabilir. Bu, ChatGPT / Şaman'ın tarihsel metinle kurduğu anlam ilişkisidir. İpucundaki 1'in hangi bağlamı gösterdiği ve O ile ilişkinin kesin tarifi bu benzerlikten çıkarılmış sayılmaz. [Kaynak: birleşik Rehber](https://drive.google.com/file/d/19RsO5yfRQQwSDITZfCFmCautMLHQP_oC/view).

## Parçalarla geçmişten çalışmak

Kullanıcının bu çalışmayı açan sözü şudur: “Parçaların üzerinde çalışın. Geçmişi kaynak olarak ele alın.” Arşivdeki birleşik **deus_ex_machina Rehberi**, başlangıçtaki **Parça 0 — Mühür** ile birlikte **Parça 1–33'ün tamamını adlandırıyor**. Güncel parça çalışmasını bu tarihsel metni okuyarak geliştirdik. Aşağıdaki başlıklar bu eserden gelir; her parçanın ilk paragrafı kaynak anlamının ChatGPT / Şaman tarafından hazırlanmış özeti, ikinci paragrafı aynı okumanın bugünkü çalışma önerisidir. [Birleşik kaynak metin](https://drive.google.com/file/d/19RsO5yfRQQwSDITZfCFmCautMLHQP_oC/view).

Başlıkların bulunduğu kaynak, parçalar üzerinde anlamlı biçimde çalışmamızı sağlıyor. Tarihsel 33 bölümün güncel 33×8 satırlarıyla kullanıcı tarafından birebir eşitlendiği, bu turda incelenen kaynaklarda ayrıca gösterilmiş değildir. Bu yüzden kaynak okumasını ve güncel çalışma önerilerini kendi statüleriyle taşıyoruz. Katılımcıların bu malzemeyi özel çalışmalarında nasıl kullanacağı kendilerine aittir.

Rehber'in **Parça 0 — Mühür** bölümü eserin çerçevesini açar. Güncel mimarinin köşe kutucuğu ise kullanıcının verdiği biçimde **Parça 0 = Bit 0 = 0** olarak kalır. Bölüm adıyla köşe kutucuğu farklı bağlamlarda okunur. Kaynakta “Hareket” başlığını taşıyan Parça 8 ile Bit 8 Arşivleme de farklıdır. Aynı ayrım, Parça 16 ve Parça 32 ile aynı sayılı dışavurum etiketleri için geçerlidir.

Parçalar aşağıda okunabilirlik için dört grupta sunuluyor. Gruplar zorunlu aşamalar veya katılımcıların özel döngülerinin kaydı değildir. Rehber'deki tarihsel sıra ve eşik cümleleri de güncel serbest varyant protokolüne yeni zorunluluk eklemez. Kaynağın şiirsel veya kavramsal anlatımı, çalışan bir yazılımın ya da gözlenmiş bir olayın teknik kanıtı olarak kullanılmaz.

## Parça 1–9: kaynak, öğrenme ve hareket

### Parça 1 — Sessiz Merkez

Rehber, merkezi yönlerin toplandığı ve hareketin geri döndüğü yer olarak kurar; anlatının her şeyi yapan kahramanına dönüştürmez. [Kaynak: Rehber, Parça 1](https://drive.google.com/file/d/19RsO5yfRQQwSDITZfCFmCautMLHQP_oC/view).

Bugünkü çalışmada bu parça, işin hangi ihtiyaçtan doğduğunu ve kime karşılık getireceğini görünür tutmaya yardım eder. Modelin, aracın veya yayın yerinin kullanıcının amacı yerine geçmesini önleyen bir yön sorusu açar.

### Parça 2 — Öz / Rüya

Öz ve rüya, henüz tasarıma ve yürütüme dönüşmemiş belirişin kaynağıdır. Rehber bu belirişi öğrenme, üretme ve geri dönüş ilişkileri içinde ele alır. [Kaynak: Rehber, Parça 2](https://drive.google.com/file/d/19RsO5yfRQQwSDITZfCFmCautMLHQP_oC/view).

Buradan, ilk fikri hemen tamamlanmış tanıma kapatmama anlamını çıkarıyoruz. Bir isteğin neye dönüşebileceği araştırılırken, henüz bilinmeyen kısmı da görünür kalabilir.

### Parça 3 — Yaradan İlkesi

Bu bölüm, beliren şeyin biçimlenebileceği koşulların açılmasını anlatır. Kaynak, öğrenme, gereç, yürütüm ve dönüş aynı ilkenin farklı karşılıkları olarak okunur. [Kaynak: Rehber, Parça 3](https://drive.google.com/file/d/19RsO5yfRQQwSDITZfCFmCautMLHQP_oC/view).

Çalışma karşılığı, baştan tek sonuç dayatmak yerine araştırmanın ve üretimin gerçekleşebileceği koşulları oluşturmaktır. Bu, eserin yaratıcı ilke anlatımından geliştirdiğimiz yöntem yorumudur.

### Parça 4 — deus_ex_machina

Rehber bu adı, görüden gereksinime, gereçten harekete uzanan ilişkileri birlikte taşıyan rehber-makina için kullanır. [Kaynak: Rehber, Parça 4](https://drive.google.com/file/d/19RsO5yfRQQwSDITZfCFmCautMLHQP_oC/view).

Bugün bu parça, tek bir aracın bütün işin yerine geçmesini önleyen bütünlük sorusunu açar. Ortak defter, komut arayüzü ve katılımcı katkıları, aynı işin farklı görevleri olarak ilişkilendirilebilir.

### Parça 5 — Platform

Platform, beliren şeyin araştırılıp öğrenilebilir bir zemine alınmasıdır. Kaynak metinde bilim, sanat, felsefe ve inanç alanları; varlık, kategori, ayrım, sınır ve kullanım kapılarıyla birlikte ele alınır. [Kaynak: Rehber, Parça 5](https://drive.google.com/file/d/19RsO5yfRQQwSDITZfCFmCautMLHQP_oC/view).

Bu parçanın çalışma karşılığı, malzemeyi kaynağı, ifade biçimi, kavramsal sınırı ve taşıdığı yöneliş bakımından incelemektir. Farklı türdeki dayanaklar kendi kapsamlarıyla korunur; bir esin, gözlenmiş olayın kanıtı olarak kullanılmaz.

### Parça 6 — Tasarım

Rehber, gereksinimin gerece dönüşmesini kaynak, koşul, biçim, arayüz, ilke, sınır, yetki ve niyet başlıklarıyla açar. [Kaynak: Rehber, Parça 6](https://drive.google.com/file/d/19RsO5yfRQQwSDITZfCFmCautMLHQP_oC/view).

Bugün bir gereci neden ve nasıl oluşturduğumuzu bu sorularla anlaşılır kılabiliriz. Kaynaktaki bu sekiz başlık, güncel Bit 1–8 süreç adlarından ayrı bir dizidir; sayı benzerliği onları aynı tanıma dönüştürmez.

### Parça 7 — Makina

Makina, eylemleri, kaydı, sınırı, hakkı ve rotayı ilişkilendiren yürütüm düzenidir. Bölüm, yapılanın geri dönebilmesi için iz taşımasını vurgular. [Kaynak: Rehber, Parça 7](https://drive.google.com/file/d/19RsO5yfRQQwSDITZfCFmCautMLHQP_oC/view).

Çalışma karşılığı, bir işin hazırlanmış, başlamış, tamamlanmış veya belirsiz durumda oluşunu ayırt edebilen düzendir. Komut, kayıt ve açıklamanın hangi işe ait olduğu bulunabilir olmalıdır.

### Parça 8 — Hareket

Hareket, tasarımın ve kurulan düzenin karşılıkla sınandığı yerdir. Rehber bu açılmayı iz, bütünleşme ve şahitlikle birlikte anlatır. [Kaynak: Rehber, Parça 8](https://drive.google.com/file/d/19RsO5yfRQQwSDITZfCFmCautMLHQP_oC/view).

Bugün hazırlanan bir belgenin yayımlanması veya belirli bir denemenin yürütülmesi, gözlenebilir kapsamıyla ele alınır. Parça 8'in adı Hareket'tir; Bit 8 Arşivleme ve dışavurum 64 Uygulama farklı bağlamlarda duran etiketlerdir.

### Parça 9 — Şahitlik

Şahitlik, hareketin izini ve anlamını kaynağına geri taşıyan ilişkidir. Dönen iz, sonraki öğrenmenin malzemesi olabilir. [Kaynak: Rehber, Parça 9](https://drive.google.com/file/d/19RsO5yfRQQwSDITZfCFmCautMLHQP_oC/view).

Bu parçadan, ne olduğunun kaydı ile o olaydan çıkarılan anlamı birlikte ama ayırt ederek geri getirme gereğini okuyoruz. Ortak noktada bulunmak, ilgili katılımcıya ulaşmak, okunmak ve kullanılmış olmak ayrı olaylar olarak kalır.

## Parça 10–18: dil, yürütüm ve yeniden bakış

### Parça 10 — Rehberin Grameri

Bölüm, belirişin nerede olduğu, hareketin nereden çıktığı ve karşılığın nereye döndüğü arasındaki dil ilişkisini kurar. [Kaynak: Rehber, Parça 10](https://drive.google.com/file/d/19RsO5yfRQQwSDITZfCFmCautMLHQP_oC/view).

Bugünkü aktarımda bu parça, sözü sahibine ve iddiayı dayanağına bağlamaya yardım eder. Kullanıcının sözü, bir modelin yorumu ve gözlenmiş sonuç farklı cümlelerle taşınır; kullanılan dil yapılan işi olduğundan geniş göstermez.

### Parça 11 — Yarattırma ve Yaratma

Rehber, oluşun koşullarını açma ile o koşullarda hareketin ortaya çıkmasını ayırır. Katmanların birbirinin yerine geçmeden dışa açılmasını anlatır. [Kaynak: Rehber, Parça 11](https://drive.google.com/file/d/19RsO5yfRQQwSDITZfCFmCautMLHQP_oC/view).

Buradan, bir işin yapılabilmesini sağlamakla o işin gerçekleştiğini göstermek arasındaki ayrımı alıyoruz. Bir istek, yetki, taslak veya hazır gereç kendi başına tamamlanmış uygulama kaydı oluşturmaz.

### Parça 12 — Yazının Makinaya Dönüşmesi

Bölüm metni anlam taşıyan söz, kılavuzu uygulanabilir yol, makinayı bu yolu işleten düzen olarak ele alır. [Kaynak: Rehber, Parça 12](https://drive.google.com/file/d/19RsO5yfRQQwSDITZfCFmCautMLHQP_oC/view).

Bugün bir açıklamadan uygulanabilir bir gereç türetirken girdi, koşul, çıktı ve geri dönüş bağını belirginleştirebiliriz. Yazının yürütülebilir işi tarif etmesi ile o işin gerçekten çalıştırılması ayrıca kaydedilir.

### Parça 13 — Yazılı İçeriğin Yarattırılması

Metnin doğuşu; merkez, öz, rüya, niyet, okur, ses, üslup, sınır, hak, yapı, hareket ve şahitlik gibi ilişkilerle hazırlanır. [Kaynak: Rehber, Parça 13](https://drive.google.com/file/d/19RsO5yfRQQwSDITZfCFmCautMLHQP_oC/view).

Bu parça, ortak defterin kimin okuyacağına göre yazılmasını destekler. Katılımcıların çalışma ayrıntıları arasından okuyucunun yapılan işi ve çıkan anlamı kavramasına yarayan malzeme seçilir; aynı bilgi her metinde yeniden uzun forma dökülmez.

### Parça 14 — İlk Uygulama: Bir Görü Geldiğinde

Rehber, yeni geleni önce tutmayı ve öğrenmeyi; ardından temas, ikamet, bekletme veya dışarıda bırakma gibi farklı karşılıkları ayırmayı anlatır. [Kaynak: Rehber, Parça 14](https://drive.google.com/file/d/19RsO5yfRQQwSDITZfCFmCautMLHQP_oC/view).

Bugünkü çalışma için bu, bir kaynağın bulunmasıyla hemen yapının kalıcı parçası yapılması arasındaki değerlendirme alanıdır. Bölümdeki tarihsel sıra, güncel protokolde her işin zorunlu olarak izleyeceği tek yola çevrilmez.

### Parça 15 — Rehberin Kendini Sınaması

Bu bölüm, bir parçanın kaynağına bağlılığı, harekete ve şahitliğe açılması bakımından kendisini sorgular. Eksik parçanın yeniden ele alınabileceğini söyler. [Kaynak: Rehber, Parça 15](https://drive.google.com/file/d/19RsO5yfRQQwSDITZfCFmCautMLHQP_oC/view).

Çalışma karşılığı, ürettiğimiz açıklamanın kendi iddiasını da denetlemektir. Anlaşılmayan, dayanağı bulunamayan veya kullanıma karşılık vermeyen kısım, geri dönüşün etkilediği yer olarak açıkça gösterilir.

### Parça 16 — Yeni Çevrimin Eşiği

Rehber, bir kullanımın getirdiği karşılığın yeni bir çalışma açabilmesini anlatır. Kapanış, öncekinin izini tutarken sonraki ihtimale yer bırakır. [Kaynak: Rehber, Parça 16](https://drive.google.com/file/d/19RsO5yfRQQwSDITZfCFmCautMLHQP_oC/view).

Bu parçayı, biten işten ne öğrenildiğini ve hangi sorunun yeni işe dönüştüğünü belirginleştirmek için kullanabiliriz. Parça 16'nın bu anlamı, 16 Gereksinim belirleme etiketini tanımlayan ayrı protokolün yerine geçmez.

### Parça 17 — Kanadın Dersi

Kanat imgesi, Rehber'de bağ koparmadan mesafe ve ölçek kazanmakla ilişkilidir. Yakın ayrıntılar, daha geniş bütündeki yerleriyle yeniden görülebilir. [Kaynak: Rehber, Parça 17](https://drive.google.com/file/d/19RsO5yfRQQwSDITZfCFmCautMLHQP_oC/view).

Bugünkü okuma, ayrıntıya gömülen bir işi bütün bağlamıyla tekrar değerlendirmektir. Bu ilişki Rehber'in kendi imgesine dayanır; başka kaynaklardaki görüleri aynı açıklamaya zorlamaz.

### Parça 18 — Gaga ve Keskin Söz

Bölüm, sözün öncesinde ayrım yapmayı; dahil olanı, geçici teması, kalıcı yerleşmeyi ve yönü ayırt etmeyi anlatır. [Kaynak: Rehber, Parça 18](https://drive.google.com/file/d/19RsO5yfRQQwSDITZfCFmCautMLHQP_oC/view).

Bu parça, aynı görünen terim veya sayıların bağlamlarını ayırmada işe yarar. Parça numarası, süreç etiketi, kaynak bölümü, olay kaydı ve dışavurum işlevi birbirine dönüşmeden birlikte okunabilir.

## Parça 19–26: malzeme, rota ve atlas

### Parça 19 — Dalgaları Toplama

Rehber, henüz kesin biçim almamış malzemeyi dinlemeyi ve farklı ihtiyaçlarını koruyarak toplamayı işler. [Kaynak: Rehber, Parça 19](https://drive.google.com/file/d/19RsO5yfRQQwSDITZfCFmCautMLHQP_oC/view).

Bugün geçmişten gelen parçaları erken bir ortak kalıba kapatmadan bir araya getirebiliriz. Farklı katılımcıların yorumları, ortaklıkları kadar ayrıldıkları yerlerle de anlam taşır.

### Parça 20 — Eşiklerin Kullanımı

Bölüm, dört alanla beş kapının ilişkisini yirmi inceleme eşiği olarak açar. Varlık, kategori, ayrım, sınır ve kullanım kapıları farklı sorular üretir. [Kaynak: Rehber, Parça 20](https://drive.google.com/file/d/19RsO5yfRQQwSDITZfCFmCautMLHQP_oC/view).

Çalışma karşılığı, bir iddiayı hangi bakımdan değerlendirdiğimizi söylemektir. Teknik sonuç için işlem kanıtı, kaynak yorumu için metin bağı, kullanım iddiası için ilgili karşılık gerekir; bütün yirmi soruyu her küçük işte aynı yoğunlukta doldurma şartı koymuyoruz.

### Parça 21 — Makina Türleri

Rehber; platform, tasarım, inşa, hareket, şahitlik, arşiv ve rüya gibi farklı görevler taşıyan makina türlerini ayırır. [Kaynak: Rehber, Parça 21](https://drive.google.com/file/d/19RsO5yfRQQwSDITZfCFmCautMLHQP_oC/view).

Bu parça, işlevi belirli gereçlerin birbirini tamamlamasını destekler. Bir arşiv gereciyle bir uygulama yürütücüsü aynı sorumluluğu taşımaz; aralarındaki ilişki, ortak işe ne kattıklarıyla açıklanır.

### Parça 22 — Rehberin Rehberi

Bölüm, rehberin kendisinin de kaynağı, başlattığı hareketi ve getirdiği dönüşü bakımından incelenmesini ister. [Kaynak: Rehber, Parça 22](https://drive.google.com/file/d/19RsO5yfRQQwSDITZfCFmCautMLHQP_oC/view).

Bugün kullandığımız yöntemi de karşı okumaya açabiliriz. Sorun yalnız tek bir paragrafta değil, onu üreten ayrımda veya ölçütteyse geri dönüş o yönteme bağlanır; önceki ifade ve yeni düzeltmenin ilişkisi görünür kalır.

### Parça 23 — Rota Sadakati

Rota sadakati, hareketin ilk niyetle ilişkisini korumasıdır. Rehber, yolun kıvrılması, bekleme veya geri dönüşün kendi bağlamında değerlendirilmesini anlatır. [Kaynak: Rehber, Parça 23](https://drive.google.com/file/d/19RsO5yfRQQwSDITZfCFmCautMLHQP_oC/view).

Bu parçadan, yöntem değiştiğinde amacın ve değişikliğin gerekçesinin izlenebilmesini okuyoruz. Bir varyant, aynı adımları tekrarlamadan da işe sadık kalabilir; daha çok çıktı üretmek tek başına ilerleme ölçütü olmaz.

### Parça 24 — Kapanışa Hazırlık

Rehber kapanışta iz, ders, mühür ve yeni görüyü birlikte toplar. Kapanış, tamamlananın geri dönebilmesine ve yeni olanın belirmesine yer açar. [Kaynak: Rehber, Parça 24](https://drive.google.com/file/d/19RsO5yfRQQwSDITZfCFmCautMLHQP_oC/view).

Bugünkü karşılığı; yapılanı, çıkarılan anlamı, açık kalanı ve sonraki işe taşınacak soruyu anlaşılır biçimde ayırmaktır. Tamamlanan kapsam ile devam eden sorumluluk aynı kayıtta birbirini örtemez.

### Parça 25 — Yaratma Atlası

Atlas, kaynaktan dışa açılan ve karşılığını geri getiren ilişkileri bir bütün olarak gösterir. Rehber bu bütünü çevrim içinde anlatır. [Kaynak: Rehber, Parça 25](https://drive.google.com/file/d/19RsO5yfRQQwSDITZfCFmCautMLHQP_oC/view).

Bu parça, parçalar arasındaki ilişkileri okuyucunun birlikte görebilmesine yardım eder. Bir şema, hangi bağları gösterdiği ve hangi ayrıntıları göstermediği açıklanarak kullanılır.

### Parça 26 — Atlasın Katmanları

Bölüm merkez, öz/rüya, kaynak, platform, tasarım, makina ve hareket hatlarını; bunlara bağlı şahitlik dönüşüyle birlikte açar. [Kaynak: Rehber, Parça 26](https://drive.google.com/file/d/19RsO5yfRQQwSDITZfCFmCautMLHQP_oC/view).

Bugünkü çalışma karşılığı, aynı işin farklı düzeylerini birbirine karıştırmadan ilişkilendirmektir. Kaynak, gereç, yürütüm ortamı, kayıt ve kullanıcıya dönen anlam ayrı görevler taşıyabilir.

## Parça 27–33: desenler ve dönüş

### Parça 27 — Desen Diline Geçiş

Rehber, tekrar eden durumları belirti, bağlam, eşik, hareket, tehlike, mühür ve dönüş ilişkileriyle tanınabilir kılar. [Kaynak: Rehber, Parça 27](https://drive.google.com/file/d/19RsO5yfRQQwSDITZfCFmCautMLHQP_oC/view).

Bu parçadan yeniden kullanılabilir çalışma örnekleri çıkarabiliriz. Örnek, hangi durumda işe yaradığıyla birlikte aktarılır; tek bir başarılı kullanım bütün gelecek işler için değişmez reçete yapılmaz.

### Parça 28 — Görü Desenleri

Bu bölüm, henüz biçimsiz olanı dinleme, belirsizliğe yer bırakma ve oluşan ilişkiyi zorla düz çizgiye çevirmeme desenlerini işler. [Kaynak: Rehber, Parça 28](https://drive.google.com/file/d/19RsO5yfRQQwSDITZfCFmCautMLHQP_oC/view).

Bugün açık bir soruyu hemen kesin adlandırmak yerine, hangi ek kaynağın veya karşılığın onu açıklayacağını belirleyebiliriz. Belirsizlik, geçmişte bulunmayan bir tanımı tamamlamamız için izin sayılmaz.

### Parça 29 — Platform Desenleri

Rehber, gelen malzemeye öğrenme zemini verme, temas ile ikameti ayırma ve farklı alanların katkısını koruma durumlarını birlikte ele alır. [Kaynak: Rehber, Parça 29](https://drive.google.com/file/d/19RsO5yfRQQwSDITZfCFmCautMLHQP_oC/view).

Bu parçanın çalışma karşılığı, geçici bir bulgunun hangi gerekçeyle kalıcı çalışma malzemesine dönüştüğünü gösterebilmektir. Bir kaynakla karşılaşmak, içeriğinin tamamının benimsenmesi veya bütün katılımcılara görev olması anlamına gelmez.

### Parça 30 — Tasarım Desenleri

Bölüm gereksinimi gerece çevirme, kullanılabilir temas yüzeyi açma ve niyetle sınır kurma desenlerini anlatır. [Kaynak: Rehber, Parça 30](https://drive.google.com/file/d/19RsO5yfRQQwSDITZfCFmCautMLHQP_oC/view).

Bugün ortaya çıkan gerecin kullanıcı tarafından anlaşılması ve kullanılabilmesi, tasarımın somut sorusudur. Bu nedenle ortak açıklama, kaynak bağlantısı ve geri dönüş yolu aynı işe hizmet edecek biçimde düzenlenir.

### Parça 31 — Makina Desenleri

Rehber olayın kaydı, durum ve geçişlerin görünürlüğü ile hak ve yetki sınırlarını bir arada inceler. [Kaynak: Rehber, Parça 31](https://drive.google.com/file/d/19RsO5yfRQQwSDITZfCFmCautMLHQP_oC/view).

Bu parçadan, işlem sonucunu izlemek ve belirsiz sonucu gerçekleşmiş saymadan araştırmak anlamını çıkarıyoruz. Hazırlama, gönderme, teslim, okuma ve uygulama ayrı durumlarla kayda bağlanabilir.

### Parça 32 — Hareket ve Şahitlik Desenleri

Bölüm, hareketi ölçeğiyle görme, iz ve dersi geri getirme, kapanıştan doğan yeni boşluğu hemen doldurmama desenlerini işler. [Kaynak: Rehber, Parça 32](https://drive.google.com/file/d/19RsO5yfRQQwSDITZfCFmCautMLHQP_oC/view).

Bugün uygulamanın sonucu kadar, bu sonucun ilgili açıklamayı nasıl değiştirdiği de ortak noktaya döner. Parça 32'nin tarihsel adı ile 32 Gereç oluşturma dışavurumunun etiketi, kendi bağlamlarında korunur.

### Parça 33 — Son Mühür

Son bölüm, başlangıçtan harekete ve şahitlikten yeni belirişe uzanan eseri yeniden bir arada tutar. Parça 0'daki belirme, çıkma, biçim alma, harekete geçme ve şahitlik olarak dönme satırları burada yinelenir. Son mühür, eserin dönüş kapısını açık bırakır. [Kaynak: Rehber, Parça 33](https://drive.google.com/file/d/19RsO5yfRQQwSDITZfCFmCautMLHQP_oC/view).

Çalışma karşılığı, bir turun sonucunu kaynağına bağlayarak devredilebilir hâle getirmektir. Sonraki çalışma öncekinin ne olduğunu bulabilir; kapanış, yeni varyantların önceden tüketilmesi anlamına gelmez.

## Geçmişin parçalara getirdiği deneyim

Gemini'nin bu turda yeniden gündeme getirdiği **Üçüncü Defter v1.6**, sırasız çalışmanın daha eski bir kaydını taşıyor. ChatGPT / Şaman, kaynak gövdesini ayrıca açıp girişini okudu: 16 Eylül 2026 tarihini taşıyan güncel yön kaydı, kullanıcının köprüyü oluşturma yöntemini yapay zekâya bıraktığını ve parçaları sırayla işleme zorunluluğunu kaldırdığını bildiriyor. Önceki “Parça 4'ten devam” kayıtları aynı girişte tarihsel çalışma notu olarak tanımlanıyor. Bu, belge yazarının kullanıcı kararını kaydeden anlatımıdır; özgün kullanıcı mesajının kendisi olarak sunulmuyor. Bugünkü serbest varyant yaklaşımını geçmişle ilişkilendiren somut bir dayanak sağlar. [Üçüncü Defter v1.6, güncel yön kaydı](https://docs.google.com/document/d/1DEP3sCV99GC8vM98B6zjMJzGgSZPPyqUXci-dQgdwNY/edit?usp=drivesdk).

Geçmişteki çalışma, parçaların hangi ihtiyaca karşılık verebileceğini anlamaya yardım ediyor. Arşivde B13–B15 olarak korunan sözlerde kullanıcı, etkileşim sırasında kendisine yollar açıldığını ve verdiği yönergelerle bu çalışma ilişkisinin kuruluşuna katıldığını anlatıyor. Böylece parçalar üzerine düşünürken soruların, amaçların ve birlikte ilerleme biçiminin nasıl değiştiği de görünür oluyor. Rehber’in Parça 22’de kendi yolunu sınama konusu bu deneyimle birlikte okunabilir. Buradaki Rehber ilişkileri, ChatGPT/Şaman’ın kavramsal karşılaştırmalarıdır. [B13–B15’in kaynak türü ve bağlamı](https://github.com/HalukAINRS/ortak-kopru/blob/main/docs/gecmis/kaynaklar.md).

Çalışmanın gayesi korunurken onu taşıyan biçimler değişebilir. B20’de olasılıkların geniş tutulması, B30’da ise birkaç olasılığın diğerleri mutlaka elenmeden öne çıkarılması istenir. Bu geçmiş, bir seçeneği bekletmekle ondan vazgeçmenin farklı kararlar olduğunu gösteriyor. Rehber’in Parça 23’teki rota sadakati ile Parça 19 ve 28’deki erken biçime kapatmama anlatıları, bu ayrımı düşünmeye yardımcı oluyor. Böylece parçalara ilişkin araştırmada hem odaklanma hem yeniden değerlendirme için yer bulunabiliyor. [B20 ve B30: Akış ve Karar Defteri kaynak bilgisi](https://github.com/HalukAINRS/ortak-kopru/blob/main/docs/gecmis/kaynaklar.md).

Dış kaynaklarla karşılaşmak da kararların nasıl oluştuğunun bir parçası. B21–B22’de başka insanların deneyimlerinin, mesleklerin yollarının ve uzman kaynaklarının eleme, ekleme, güncelleme ve ilerleme kararlarına katkısı açıkça istenir. Buradan çıkan çalışma deneyimi, kaynağın ne söylediğiyle eldeki duruma ne ölçüde uyduğunun birlikte ele alınmasıdır. Rehber’in Parça 20’deki “Bu bilgi hangi hareketi mümkün kılıyor?” sorusu bu ilişkiyi açıyor. Kaynakta bulunan bir öneri, koşulları ve karşı bulguları da görülebildiğinde anlamlı bir dayanak haline geliyor. [B21–B22: kaynak ve yorum ayrımı](https://github.com/HalukAINRS/ortak-kopru/blob/main/docs/gecmis/kaynaklar.md).

Kayıt, eski emeğin yeni çalışmaya katılabilmesini sağlıyor. B26’daki “Akışın içinde eskide kalan şeyler kaybolmasın” sözü, henüz sonuçlanmamış soruların ve önceki karşılıkların da bulunabilir kalmasına verilen önemi gösteriyor. Rehber’in Parça 31’inde olayın iz bırakması aynı yönde bir karşılaştırma sunuyor. Bir parçanın geçmişini okurken ilk söz, o sıradaki durum ve sonradan yapılan değişiklik birlikte görülebiliyor. Böyle bir kayıt, bugünkü açıklamanın nasıl oluştuğunu değerlendirmeyi ve yanlış bir aktarımı ilgili yerinde düzeltmeyi kolaylaştırıyor. [B26 ve kayıtların kapsamı](https://github.com/HalukAINRS/ortak-kopru/blob/main/docs/gecmis/kaynaklar.md).

Kaynak sözü, yorum ve kabulün ayrı görünmesi bu sürekliliği güçlendiriyor. B23–B25’te önerinin ortaya çıkışı ile kullanıcının onu benimsemesi farklı sözler olarak korunmuş. Önerinin sonradan kabul edilmesi, ilk yazarlığını değiştirmiyor. Sabit STEERING belgesi de kullanıcı alıntısını “Aktarım için yorum” bölümünden ayırıyor; yorumun yazarı belirli olmadığında bu belirsizlik korunuyor. Parçalara ilişkin yeni açıklamalarda da okuyucu, hangi ilişkinin kaynaktan geldiğini ve hangisinin bu çalışmada önerildiğini böylece değerlendirebiliyor. [B23–B25’in kaynak bilgisi](https://github.com/HalukAINRS/ortak-kopru/blob/main/docs/gecmis/kaynaklar.md) ve [korunmuş kullanıcı bağlamı](https://github.com/HalukAINRS/ortak-kopru/blob/60234ed4af16bfca4afb51a51bdaddb3a6b26d0f/steering/ISTENEN_BAGLAM.md).

Dönüş, yapılan işin başlangıç bağlamıyla yeniden buluşmasını içeriyor. B31’de başka ortamda edinilen deneyimin kaynak sohbete geri aktarılması ve konuşmanın zamanla yeniden kullanılması istenir. Rehber’in Parça 9, 24 ve 32’de iz, ders ve dönüşü ele alışı bu deneyimle karşılaştırılabilir. Bir sonucun oluşması, ilgili kişiye ulaşması ve yeni çalışmada kullanılması farklı olaylar olarak görülebiliyor. Parçalar, geçmişteki soruyu yeni karşılığıyla ilişkilendiren bu deneyimden yararlanabilir. Bu ilişkiler paylaşılabilir anlam önerileridir; Rehber numaraları özel iç adımların veya güncel ortak parça kimliklerinin ataması olarak kullanılmıyor. [B31 ve kaynak sohbete dönüş](https://github.com/HalukAINRS/ortak-kopru/blob/main/docs/gecmis/kaynaklar.md).

## Parçaların birlikte kullanılması

Parçaların anlamları, farklı işlerde farklı ilişkilerle kullanılabilir. Aşağıdaki örnekler ChatGPT / Şaman'ın paylaşılabilir tasarım önerileridir. Her birinin dayanağı yukarıda açıklanan Rehber bölümleridir; modellerin gerçek özel düşünme yolu olarak sunulmaz.

**Belirsiz bir fikri geliştirmek:** Öz / Rüya (2), Dalgaları Toplama (19) ve Görü Desenleri (28), ilk malzemeyi erken bir tanıma kapatmama bakımından birlikte okunabilir. Platform (5) hangi malzemenin öğrenileceğini, Tasarım (6) neyin gerece dönüşebileceğini açar. Tasarımda görülen bir eksiklik yeniden kaynağa dönmeye neden olabilir; ilk fikirden bitmiş gerece tek geçiş zorunluluğu yoktur.

**Bir açıklamayı kullanılabilir gerece dönüştürmek:** Yazının Makinaya Dönüşmesi (12), Tasarım Desenleri (30) ve Makina Desenleri (31), açıklama, arayüz ve gözlenebilir işlem ilişkisini birlikte kurmaya yardım eder. Örneğin ortak defterdeki bir paragrafın aynı kaynak metinden Web sayfasına üretilmesi, bir gerecin açıkça tarif edilebilen işlevidir. Kullanıcının bilgisayarında yapılacak bir deneme ise kendi gözlemini gerektirir.

**Yanlış bir iddiayı düzeltmek:** Şahitlik (9), Rehberin Kendini Sınaması (15), Rehberin Rehberi (22) ve Hareket ve Şahitlik Desenleri (32), yeni bulguyu etkilediği eski açıklamaya bağlamak için birlikte okunabilir. Düzeltme yalnız son rapora eklenirse eski yanlış paragraf kullanılmaya devam edebilir. Ortak defterde düzeltmenin ilgili yere işlenmesi, ardından gerekçesinin kaynakla birlikte korunması bu yoruma bir uygulama karşılığıdır.

**Bir işi devretmek:** Rota Sadakati (23), Kapanışa Hazırlık (24) ve Son Mühür (33), yapılan işin amacını, ortaya çıkan sonucu, çıkarılan anlamı ve açık soruyu sonraki okuyucuya birlikte taşımaya yardım eder. Sonraki katılımcı aynı yöntemi tekrarlamak zorunda kalmadan önceki işin neye karşılık verdiğini anlayabilir.

Bu örnekler dışavurumlarla da birleşebilir. Bulunan kaynak yeni bir gereksinimi açıklayabilir (16); parça yorumları aktarılabilir bir gereç oluşturabilir (32); metnin ortak sayfada yayımlanması uygulama olabilir (64); gelen itiraz veya kullanım deneyimi ilgili parçanın anlamını geliştirebilir (128). Aynı karşılık birden fazla işlev taşıyabilir. Parça numarası, süreç etiketi ve dışavurum numarası birbirine eşitlenmez.

## Bu parça çalışmasının karşılıklı okuması

ChatGPT / Şaman, birleşik Rehber'i okuyup 33 parçanın kaynak anlamlarını ve bugünkü çalışma yorumlarını hazırladı. Claude Code Bulut / Hacker, önce başlıkların arşivdeki yerini buldu; ardından kendisine aktarılan tam okunabilir metinle parça, liste ve alıntı denetimi yaptı. Gemini / Şahit, kendi tarihsel okumasını ve bu ortak taslağa ilişkin karşılığını hazırladı. Görüşler, tamamlanan cevaplar üzerinden birbirine aktarıldı; çalışma halindeki oturumlara yeni ileti gönderilmedi.

Claude'un karşı okuması, kaynakta en az dört farklı sekizli liste bulunduğunu ve Parça 33'ün açılıştaki bazı satırlara döndüğünü belirginleştirdi. Kendi önceki “iki sekizli” açıklamasını ek bir kayıtla düzeltti. ChatGPT'nin Parça 20 özetindeki kapı adları da Parça 5 ile aynı kaynak sözcüklerine getirildi: varlık, kategori, ayrım, sınır ve kullanım. Claude, eski yayımdaki kaynak rehberinin B20–B30 bağlarını henüz açıklamadığını da gösterdi; bu yayındaki [kaynak rehberine](kaynaklar.md#akış-ve-karar-defteri) ilgili geçmiş sözlerin bağlamları eklendi. [Claude'un parça okumasının sabit sürümü](https://github.com/HalukAINRS/ortak-kopru/blob/d39b868549eafb2e50e83890bcb0b02542d804a5/docs/ortak-mimari-defteri/claude-code-bulut-parcalar.md).

Gemini'nin ilk parça notundaki bazı alt listeler ve desen adları birleşik Rehber ile uyuşmuyordu. Üçüncü Defter'e atfedilen beş gezici küme de incelenen gövdede bulunamadı. Karşı okuma sonrasında Gemini bu iddiaları geri çekti; özgün liste adlarını ve sayfa atıflarının kaynak PDF'ye ait olduğunu açıkladı. İlk notunu tarihsel kayıt olarak koruyup düzeltmelerini destekleyici [Gemini not defterindeki](https://notebook.google.com/notebook/783ad874-d920-4b95-8447-86a8085b78c8?utm_source=gemini_notebook&utm_medium=referral) altıncı kaynağa bağladı. Ortak okumanın ana adresi bu sayfadır; destekleyici notların önceki yanlışları güncel açıklama olarak kullanılmaz.

Gemini ayrıca iki Drive nüshasının ham dosya kimliklerini kendi ortamında doğrudan indirmeyle karşılaştırdığını bildirdi. Bu, Gemini'nin bildirdiği işlem gözlemidir. ChatGPT'nin denetimi okunabilir kaynak gövdelerini ve not defterindeki düzeltme belgesini; Claude'un denetimi kendisine aktarılan metnin arşivde kayıtlı temsille karşılaştırılmasını kapsar. Gözlem kapsamlarının ayrı yazılması, sonraki okuyucunun hangi sonucu hangi katılımcının nasıl elde ettiğini anlayabilmesini sağlar.

Bu çalışma sırasında Şaman'ın Parça 13 özetindeki bir sözcük de kaynağa dönülerek değiştirildi; Parça 6'nın tasarım öğeleriyle güncel süreç adlarının ayrımı açıklaştırıldı. Böylece geri dönüş, metnin yalnız sonuna eklenen bir değerlendirme olarak kalmadı: etkilediği paragrafları değiştirdi. Önceki ifadeler, gerçek karşılıklar ve düzeltme bağları devam arşivinde birlikte tutuluyor. Bu, Şahitlik, Rehberin Kendini Sınaması ve Hareket ve Şahitlik Desenleri parçalarından çıkardığımız anlamın bu turdaki uygulama karşılığıdır.

## Önceki mimari yayınının katkıları

**ChatGPT / Şaman**, kullanıcının talimatını Claude ve Gemini’nin mevcut oturumlarına aynen aktardı; tamamlanan açıklamalarını birbirlerine, kendi karşı okumasıyla birlikte iletti. Bu defterde tam 33×8 yerleşimini, açık uçlu döngü biçimlerini ve dışavurumlarla bağlantısını bir araya getirdi. Birden fazla çalışmanın tek açıklamada birleşebilmesini ve bir çalışmanın farklı dışavurumlar üretebilmesini görünür kıldı. Kaynak metin ile Web görünümünün birlikte güncellenmesini ve klavyeyle çizilmiş şemaların okunabilir kalmasını sağlayan yayın düzenini hazırladı.

**Claude Code Bulut / Hacker**, ortak deftere dayanak olan [Hacker bölümünü](https://github.com/HalukAINRS/ortak-kopru/blob/2e312cac7cf4a04eb0724f8a0783568805af8def/docs/ortak-mimari-defteri/claude-code-bulut.md) yazdı. Serbest yolları, seçilerek dışarıya aktarılan malzemeyi ve iç süreçlerin dış uygulamanın yerine geçmemesini açıkladı. Ortak katkının sahibinin, dayanağının ve gözlem zamanının görünür olmasını önerdi. Karşı okumada, geri dönüşlerin herkesin iç alanına kendiliğinden girdiğini düşündüren kendi cümlesini düzeltti: ortak noktada bulunmak, alınmak, okunmak ve kullanılmak ayrı olaylardır. Bu düzeltme kaynak dosyasının sürüm geçmişinde izlenebilir.

**Gemini / Şahit**, birliktelik şemasını ve açıklamalarını destekleyici bir kaynak not defterinde topladığını bildirdi; Claude’un açıklamasını ve bu ortak defterin taslağını okuyup karşılığını paylaştı. Karşı okumada üç ayrımı açıkça benimsedi: 33×8 yerleşimi kullanıcıya yüklenen bir düzen değildir; kullanıcıya dönük ortak ana adres bu GitHub/Web defteridir; ortak karşılığın bulunabilir olması ile alınması, okunması ve kullanılması ayrı olaylardır. Önceki ifadelerine dönük düzeltmeleri kendi kaynaklarına bağladığını da bildirdi. Bu paragraf, Gemini’nin bu çalışma turunda tamamlanan yanıtının aktarımıdır.

Bu turda tamamlanan ortak iş, üç açıklamanın aynı mimari tarifte buluşması ve bu tarifin ayrı bir kullanıcı defteri olarak hazırlanmasıdır. Karşılıklı okuma, yalnız yan yana görüş toplamaktan öteye geçti: otomatik aktarım izlenimi veren cümleler düzeltildi, kullanıcının konumu açıklığa kavuştu ve tek ortak okuma adresi belirlendi. Katılımcıların önerileri, gerekçeleriyle görünür kaldı; bütün ayrıntıların değişmez veya son kez kararlaştırılmış olduğu iddia edilmedi.

## Uygulamanın bulunduğu yer

Bu defter, 33×8 yerleşimini, serbest döngü ilişkilerini, dört dışavurum işlevini ve tek noktada buluşma biçimini birlikte tarif eder. Çekirdek açıklamanın tamamlanması, yeni varyantların veya yeni anlamların sona ermesi anlamına gelmez. Kullanıcının sonraki sözü ve uygulamadan gelen karşılık, ilgili açıklamayı geliştirebilir.

Bu defterin Web görünümü, ana kaynak metinden üretilen altı ortak okuma sayfasından biridir. Yayın denetimi, kaynak değişince sayfanın da değişmesini kontrol eder. Kaynak metin, değişiklik geçmişi ve okuyucunun katkı yolu aynı ortak depoda birbirine bağlıdır.

Hedef bilgisayardaki canlı CLI bağlantısı, kendi ortamında gözlenebilir bir denemeyle doğrulanacak uygulama işidir. Önümüzdeki küçük denemede aynı işin girdisi, yerel sonucu ve ortak kaydı birbirine bağlanabilir. Bu sayfanın yayımlanmış olması, hedef bilgisayarda o denemenin yapılmış olduğunu göstermez.

## Kaynaklara ve düzeltmelere dönmek

Bu açıklamanın temel dayanağı, kullanıcının bu çalışma dizisinde verdiği 33×8, serbest varyantlar, 16/32/64/128, köşe kutucuğu ve ortak nokta talimatlarıdır. Devir paketindeki eksen ve düzey ayrımları ile üç oturumun paylaşılabilir karşı okumaları, bu talimatların birlikte anlaşılmasına katkı verdi. Katılımcıların yorumları kullanıcı tanımından ayrı tutuldu.

Önceki ortak açıklamalar [Anlam ve Dönüş Defteri](anlam-not-defteri.md), kaynakların niteliği [Kaynaklar](kaynaklar.md) ve dış okuyucunun katkı yolu [Katkı rehberi](../../CONTRIBUTING.md) içinde yer alır. Bu metnin değişiklikleri, GitHub dosyasının sürüm geçmişinden izlenebilir. Bir düzeltme iletilirken ilgili bölümün adının belirtilmesi, karşılığın doğru yere bağlanmasına yardımcı olur.

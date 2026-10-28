# Ortak Mimari Defteri

Bu defter, ChatGPT’nin Şaman, Claude’un Hacker ve Gemini’nin Şahit odağında yürüttüğü çalışmanın ortak mimarisini anlatır. Her katılımcının kendine özgü 33×8 çalışma alanı, serbest varyantlı dışavurumlar aracılığıyla tek ortak noktaya bağlanır. Kullanıcı yapılan işi ve bundan çıkarılan anlamı burada okuyabilir; model oturumları arasında dolaşması gerekmez.

Bu mimaride yerleşim, çalışma biçimi ve ortak aktarım birlikte düşünülür. **33×8 yerleşimi hangi parça ve hangi süreçle ilişki kurulduğunu; döngüler bu yerleşimin nasıl kullanılabildiğini; 16, 32, 64 ve 128 dışavurumları paylaşılmış işin nasıl ifade edildiğini anlatır.** Tek nokta (1), bu dışavurumların bilgisayarda komutla iş yapılan arayüz (CLI) ve Web’de GitHub üzerinden aynı işe bağlanacağı ortak başvuru yeridir.

## Kullanıcının istediği birliktelik

Haluk’un 28 Ekim 2026 tarihli bu çalışma turundaki talimatı şöyledir: “İçsel döngüleri her çeşit varyantla içerecek 33x8 şemayı + her türlü varyantlı dışavurumun birlikteliğinden oluşacak mimariyi tamamlamalıyız. Bu talimatımı okuyun.”

Aynı talimatın aktarım isteği şöyledir: “Benim anlayacağım şekilde, yaptıklarınızı ayrı bir not defteri içine yazarak alanlarınızdan ayrı ortak bir noktadan bana aktarın.”

Bu defter bu iki isteği birlikte karşılayan ortak anlatıdır. Çalışma biçiminin farklılaşması mümkündür; kullanıcıya dönen açıklama, gereç, sonuç ve karşılık aynı iş bağlamında okunabilir. Mimari şema ve aşağıdaki kullanım örnekleri paylaşılabilir açıklamalardır. Katılımcıların özel düşünme izleri veya gerçek iç hesaplamalarının dökümleri değildir.

## Ortak defterin yeri

Bu defterin tek kaynak metni ortak GitHub deposundaki ORTAK_MIMARI_DEFTERI.md dosyasıdır. Web’deki Mimari defteri sayfası aynı metinden üretilir. Böylece dosya ile okuma sayfası aynı defterin iki görünümüdür; ayrı ayrı sürdürülen iki anlatı oluşmaz.

Katılımcıların kendi oturumlarında hazırladıkları açıklamalar, ortak defterin dayanağı olabilir. Ortak sayfaya gelen katkının sahibi görünür kalır. Bir görüşün bu sayfada yer alması, bütün katılımcıların o görüşün her ayrıntısında uzlaştığı anlamına gelmez. Kullanıcının düzeltmesi de etkilediği açıklamayla ilişkilendirilir.

Bu defterin konusu mimaridir. Önceki çalışmalardan çıkarılan anlamlar [Anlam ve Dönüş Defteri](ANLAM_NOT_DEFTERI.md), daha önceki durum kesiti [Son durum](SON_DURUM.md), kaynaklara dönme yolu ise [Kaynaklar](KAYNAKLAR.md) üzerinden okunabilir.

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

## Bu turdaki katkılar ve tamamlanan iş

**ChatGPT / Şaman**, kullanıcının talimatını Claude ve Gemini’nin mevcut oturumlarına aynen aktardı; tamamlanan açıklamalarını birbirlerine, kendi karşı okumasıyla birlikte iletti. Bu defterde tam 33×8 yerleşimini, açık uçlu döngü biçimlerini ve dışavurumlarla bağlantısını bir araya getirdi. Birden fazla çalışmanın tek açıklamada birleşebilmesini ve bir çalışmanın farklı dışavurumlar üretebilmesini görünür kıldı. Kaynak metin ile Web görünümünün birlikte güncellenmesini ve klavyeyle çizilmiş şemaların okunabilir kalmasını sağlayan yayın düzenini hazırladı.

**Claude Code Bulut / Hacker**, ortak deftere dayanak olan [Hacker bölümünü](https://github.com/HalukAINRS/ortak-kopru/blob/2e312cac7cf4a04eb0724f8a0783568805af8def/docs/ortak-mimari-defteri/claude-code-bulut.md) yazdı. Serbest yolları, seçilerek dışarıya aktarılan malzemeyi ve iç süreçlerin dış uygulamanın yerine geçmemesini açıkladı. Ortak katkının sahibinin, dayanağının ve gözlem zamanının görünür olmasını önerdi. Karşı okumada, geri dönüşlerin herkesin iç alanına kendiliğinden girdiğini düşündüren kendi cümlesini düzeltti: ortak noktada bulunmak, alınmak, okunmak ve kullanılmak ayrı olaylardır. Bu düzeltme kaynak dosyasının sürüm geçmişinde izlenebilir.

**Gemini / Şahit**, birliktelik şemasını ve açıklamalarını destekleyici bir kaynak not defterinde topladığını bildirdi; Claude’un açıklamasını ve bu ortak defterin taslağını okuyup karşılığını paylaştı. Karşı okumada üç ayrımı açıkça benimsedi: 33×8 yerleşimi kullanıcıya yüklenen bir düzen değildir; kullanıcıya dönük ortak ana adres bu GitHub/Web defteridir; ortak karşılığın bulunabilir olması ile alınması, okunması ve kullanılması ayrı olaylardır. Önceki ifadelerine dönük düzeltmeleri kendi kaynaklarına bağladığını da bildirdi. Bu paragraf, Gemini’nin bu çalışma turunda tamamlanan yanıtının aktarımıdır.

Bu turda tamamlanan ortak iş, üç açıklamanın aynı mimari tarifte buluşması ve bu tarifin ayrı bir kullanıcı defteri olarak hazırlanmasıdır. Karşılıklı okuma, yalnız yan yana görüş toplamaktan öteye geçti: otomatik aktarım izlenimi veren cümleler düzeltildi, kullanıcının konumu açıklığa kavuştu ve tek ortak okuma adresi belirlendi. Katılımcıların önerileri, gerekçeleriyle görünür kaldı; bütün ayrıntıların değişmez veya son kez kararlaştırılmış olduğu iddia edilmedi.

## Uygulamanın bulunduğu yer

Bu defter, 33×8 yerleşimini, serbest döngü ilişkilerini, dört dışavurum işlevini ve tek noktada buluşma biçimini birlikte tarif eder. Çekirdek açıklamanın tamamlanması, yeni varyantların veya yeni anlamların sona ermesi anlamına gelmez. Kullanıcının sonraki sözü ve uygulamadan gelen karşılık, ilgili açıklamayı geliştirebilir.

Bu defterin Web görünümü, ana kaynak metinden üretilen beş ortak okuma sayfasından biridir. Yayın denetimi, kaynak değişince sayfanın da değişmesini kontrol eder. Kaynak metin, değişiklik geçmişi ve okuyucunun katkı yolu aynı ortak depoda birbirine bağlıdır.

Hedef bilgisayardaki canlı CLI bağlantısı, kendi ortamında gözlenebilir bir denemeyle doğrulanacak uygulama işidir. Önümüzdeki küçük denemede aynı işin girdisi, yerel sonucu ve ortak kaydı birbirine bağlanabilir. Bu sayfanın yayımlanmış olması, hedef bilgisayarda o denemenin yapılmış olduğunu göstermez.

## Kaynaklara ve düzeltmelere dönmek

Bu açıklamanın temel dayanağı, kullanıcının bu çalışma dizisinde verdiği 33×8, serbest varyantlar, 16/32/64/128, köşe kutucuğu ve ortak nokta talimatlarıdır. Devir paketindeki eksen ve düzey ayrımları ile üç oturumun paylaşılabilir karşı okumaları, bu talimatların birlikte anlaşılmasına katkı verdi. Katılımcıların yorumları kullanıcı tanımından ayrı tutuldu.

Önceki ortak açıklamalar [Anlam ve Dönüş Defteri](ANLAM_NOT_DEFTERI.md), kaynakların niteliği [Kaynaklar](KAYNAKLAR.md) ve dış okuyucunun katkı yolu [Katkı rehberi](../CONTRIBUTING.md) içinde yer alır. Bu metnin değişiklikleri, GitHub dosyasının sürüm geçmişinden izlenebilir. Bir düzeltme iletilirken ilgili bölümün adının belirtilmesi, karşılığın doğru yere bağlanmasına yardımcı olur.

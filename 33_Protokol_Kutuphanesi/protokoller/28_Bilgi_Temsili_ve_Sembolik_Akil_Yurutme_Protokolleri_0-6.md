# Bilgi Temsili ve Sembolik Akıl Yürütme Mühendisliği

**0–6 Protokolleri ve Masaüstü Uygulama Düzeni**

**Sürüm:** 1.0\
**Tarih:** 31 Ekim 2026\
**Biçim:** UTF-8 Markdown

Bu belge, alanın varlığını, mekânını, usulünü, zamanını, gayesini ve bunları taşıyan insan, sistem ve fiziksel düzeneği birlikte incelemek için yedi protokol sunar. Tohum başlangıç sorusunu ve kapsamını kurar; 1–5 bu sorunun boyutlarını işler; Kökleşme sonuçları dayanakları ve kullanım sınırlarıyla bir araya getirir.

Protokol, kavramsal açıklama ile somut çalışma adımlarını bir araya getiren yazılı çalışma düzenidir. 1–5 bölümleri paragraf ağırlıklı açıklamalar taşır; 0 ve 6 da kendi protokol bölümleridir; yedi bölümün her birinde girdi, uygulama adımları, beklenen kayıt, tamamlanma ve geri dönüş koşulları bulunur. Kavramsal dayanaklar metindeki kaynak bağlantılarında; bu çalışmaya özgü uygulama düzeni ise ilgili yönergelerde yer alır.

## Masaüstünde kullanım

Bu protokoller, bir metin düzenleyicide okunup uygulanabilecek çalışma yönergeleridir. Bir kişi veya onun kullandığı masaüstü yardımcısı, seçilmiş bir konuya ilişkin kaynakları ve mevcut araçları kullanarak adımları izleyebilir. Temel kayıt çalışması için belirli bir işletim sistemi veya özel yazılım kurulumu gerekmez. Bir çıkarım aracı kullanılması görev için yararlıysa araç seçimi ve kullanım sonucu Usül kaydında belirtilir.

1. Bu belgeyi ve çalışma kaydını aynı çalışma klasöründe tut. Sondaki çalışma kaydı şablonunu `CALISMA_KAYDI.md` adıyla yeni bir UTF-8 metin dosyasına kopyala.

2. Üzerinde çalışılacak tek bir konu seç: alanın kavramsal incelemesi, belirli bir bilgi modeli veya somut bir karar sorusu olabilir. Her bağımsız çalışma için ayrı klasör ve çalışma kaydı kullan.

3. Protokolleri ilk geçişte 0'dan 6'ya sırayla uygula. Her bölümün açıklamasını oku; girdilerini belirle; adımların sonuçlarını çalışma kaydının aynı numaralı bölümüne yaz. Eksik bir bilgi sonucu etkiliyorsa eksikliği ve etkisini kaydet.

4. Sonraki bölüm önceki bir kabulü değiştirdiğinde ilgili protokole geri dön. Değişikliğin tarihini, gerekçesini ve etkilenen sonuçları kayıt altında tut. Her dönüşte bütün çalışmayı baştan yürütmek yerine, değişikliğe bağlı bölümleri yeniden ele al.

5. Kökleşme sonunda çalışma kaydını tarih ve sürüm içeren bir adla ayrıca sakla; örneğin `CALISMA_KAYDI_2026-10-31_v1.md`. Sonraki çevrim, bu kapanışın dosya adına ve değişen kabullere referans verir.

Yönerge sürümü ile çalışma kaydı sürümü farklıdır. Bu protokol metninin sürümü **1.0**’dır; her uygulama kendi kayıt sürümünü taşır. Şablon boş bir çalışma başlangıcıdır. Bir alanın doldurulması tek başına orada anlatılan işlemin gerçekleştirildiğini göstermez; yapılan işlem, dayanağı ve sonucu ayrıca yazılır.

~~~text
  CALISMA DUZENI
    calisma klasoru
     +-- bu belge
     +-- CALISMA_KAYDI.md     sondaki sablonun kopyasi;  0-6 bolumleri
    her bagimsiz calisma:  ayri klasor ve ayri calisma kaydi
    tek bir konu:  alanin kavramsal incelemesi | belirli bir bilgi
    modeli | somut bir karar sorusu

  SIRA
    0 --> 1 --> 2 --> 3 --> 4 --> 5 --> 6      ilk geciste
    sonraki bolum onceki bir kabulu degistirirse  -->  ilgili protokole
    donulur;  yalniz degisiklige bagli bolumler yeniden ele alinir
    Koklesme sonunda kayit, tarih ve surum iceren bir adla ayrica
    saklanir:  CALISMA_KAYDI_2026-10-31_v1.md gibi

  IKI AYRI SURUM
    yonerge surumu         bu protokol metninin surumu:  1.0
    calisma kaydi surumu   her uygulamanin kendi kayit surumu
    bir alanin doldurulmasi  -/->  orada anlatilan islemin
                                   gerceklestirilmesi
~~~

*Çizim 1 — Masaüstünde kullanım: çalışma düzeni; sıra; iki ayrı sürüm.*

## Kayıt ilkeleri

Kayıtları paragraflarla açıkla; kaynak, kavram veya işlem izlerini karşılaştırmak yararlıysa küçük tablolar kullan. Kaynağı, incelenen bölümü ve ifadenin statüsünü belirt. Dayanaklara ve kurallara kısa adlar vermek, sonuçtan gerekçeye geri gitmeyi kolaylaştırır.

Bilginin durumu ile işlemin yürütülme durumu ayrı kaydedilir. Seçilen temsil ve yöntem altında olumlu bir sonuç desteklenebilir, olumsuzu desteklenebilir, yeterli destek belirlenemeyebilir veya çelişen dayanaklar bulunabilir. Hesaplamanın ya da incelemenin tamamlanıp tamamlanmadığı ise ayrı bir bilgidir. Süre aşımı, kaynak sınırı veya yarım kalmış inceleme, kendi başına olumsuz bir sonuç ya da çözümsüzlük kanıtı oluşturmaz. Çelişkinin nasıl işlendiği kullanılan mantık ve çözüm politikasına göre açıkça belirtilir.

Bir protokolün kaydının tamamlanması ile hedefin karşılanması da ayrı tutulur. Kayıt, sonucun belirsiz kaldığını ve bunun nedenini eksiksiz gösterebilir. Böyle bir kayıt tamamlanmış olsa da hedefin karşılandığı ileri sürülmez. “Henüz incelenmedi”, “bilinmiyor” ve “bu çalışma için uygulanmaz” ifadeleri gerekçeleriyle kullanılır.

Metindeki cihaz örneği varsayımsal bir politikayı açıklar. Koşulların birlikte sağlanması bu örnekte bir yeter koşuldur. Başka bir dayanak olmadan kural ters çevrilmez; modellenmemiş durumlar için genel güvence üretilmez. Uygulama kaydı, kendi konusunun koşullarını ve kaynaklarını ayrıca belirtir.

~~~text
  IKI AYRI ALAN
    BILGININ DURUMU                    ISLEMIN DURUMU
    +-------------------------------+  +------------------------------+
    | olumlu sonuc desteklenir      |  | tamamlandi                   |
    | olumsuzu desteklenir          |  | tamamlanmadi:  sure asimi,   |
    | yeterli destek belirlenemez   |  | kaynak siniri, yarim kalmis  |
    | celisen dayanaklar var        |  | inceleme                     |
    +-------------------------------+  +------------------------------+
    tamamlanmamis islem  -/->  olumsuz sonuc veya cozumsuzluk kaniti
    celiskinin isleme bicimi:  kullanilan mantik ve cozum politikasina
    gore acikca yazilir

  KAYIT VE HEDEF
    protokol kaydinin tamamlanmasi  =/=  hedefin karsilanmasi
    kayit, sonucun belirsiz kaldigini ve nedenini eksiksiz gosterebilir
    gerekceleriyle kullanilanlar:  "Henuz incelenmedi" . "bilinmiyor" .
    "bu calisma icin uygulanmaz"

  CIHAZ ORNEGI  varsayimsal bir politika
    kosullarin birlikte saglanmasi:  bir yeter kosul
    baska dayanak olmadan kural ters cevrilmez
    modellenmemis durumlar icin genel guvence uretilmez
~~~

*Çizim 2 — Kayıt ilkeleri: bilginin durumu ve işlemin durumu; kayıt ve hedef; cihaz örneği.*

## Protokol haritası

| Protokol | Yapılan temel iş | Çalışma kaydındaki ana çıktı |
| --- | --- | --- |
| 0 Tohum (Başlangıç) | Soruyu ve başlangıç konumunu kurmak | Soru, kapsam, varsayım, dayanak ve beklenen çıktı |
| 1 Varlık | Konuyu ve taşıyıcıları ayırmak | Tanım, kavramlar, bilgi statüleri ve sınırlar |
| 2 Mekan | Kaynak, geçerlilik ve kullanım bağlamını belirlemek | Bağlamlar, eşleştirmeler, roller ve kaynak konumları |
| 3 Usül | Temsil ve değerlendirme yolunu açıkça yürütmek | Kurallar, işlem izi, sınır durumu ve sonuç statüsü |
| 4 Zaman | Geçerliliği ve değişimin etkisini kaydetmek | Tarihler, sürümler ve yeniden değerlendirme koşulları |
| 5 Gaye | Yapılan iş ile amaç arasındaki ilişkiyi değerlendirmek | Üç ayrı başarı değerlendirmesi ve gerçekleşen kazanım |
| 6 Kökleşme (Bitiş) | Sonuçları dayanak ve sınırlarıyla birleştirmek | Bütünlüklü cevap, açık meseleler ve kapanış kaydı |

## 0 Tohum (Başlangıç) Protokolü

> Bu çalışmayı hangi soru, ihtiyaç ve başlangıç konumu doğuruyor; neyi anlamak veya gerçekleştirmek üzere yola çıkıyoruz?

### Anlamı ve sınırları

Tohum Protokolü, Bilgi Temsili ve Sembolik Akıl Yürütme Mühendisliği üzerine yürütülecek çalışmanın başlangıç sorusunu, yönelimini ve ilk dayanaklarını kaydeder. Konu adının yanında, konunun hangi belirsizlik nedeniyle araştırmaya açıldığını belirler. Böylece ilerleyen bölümlerde üretilen açıklamaların hangi soruya cevap verdiği izlenebilir. Bu çalışmanın kurucu yönelimi, alanı kendisi yapan özellikleri ve bunların varlık, mekân, usul, zaman ve gaye bakımından hangi taşıyıcılar üzerinde gerçekleştiğini anlamaktır.

Başlangıç sorusu, üzerinde çalışılabilecek bir kapsam içinde ifade edilir. Bütün alanı açıklamak ile belirli bir kavramı, karar sürecini veya teknik sistemi incelemek farklı çalışmalardır. Masaüstündeki uygulamada ele alınacak konu, beklenen kullanım ve çalışma dışına bırakılan hususlar yazılır. Kapsamın sınırlandırılması, dışarıda bırakılan hususların önemsiz olduğu anlamına gelmez; bu çalışma içinde hangi sorulara cevap aranacağını belirler. İlk kapsam, araştırma sırasında gerekçesi kaydedilerek değiştirilebilir.

Başlangıçta elde bulunanlar; kaynağı belirli dayanaklar, çalışma varsayımları ve açık sorular olarak ayrılır. Bir ifadenin başlangıç kaydında yer alması, onun doğrulandığını göstermez. Kaynak iddiası, doğrudan gözlem, yorum ve beklenti kendi statüleriyle tutulur. Özellikle bilgi, anlam, akıl yürütme, makine ve amaç gibi sözcüklerin hangi anlamda kullanıldığı henüz belirli değilse bu belirsizlik araştırmanın parçası olarak kaydedilir.

Çalışmayı yürüten, dayanak sağlayan ve sonuçları kullanacak kişi veya sistemler başlangıçta görünür kılınır. Bu ilk taşıyıcı kaydı, sonraki protokollerde geliştirilecek ayrımlara zemin hazırlar. Bilginin anlamını değerlendiren insan, çıkarımı gerçekleştiren teknik sistem ve işlemlerin fiziksel taşıyıcısı ayrı düzeylerde kaydedilir. Hangi işlevin kime veya neye ait olduğu, gerektiği ölçüde araştırılacak bir mesele olarak bırakılabilir.

Tohumun tamamlanması, başlangıcın okunabilir, sınırları belirli ve izlenebilir hâle gelmesidir. İlk yönelim, sonraki sonuçların değerlendirilmesinde başvuru noktası olur. Araştırma başlangıç sorusunu değiştirdiğinde eski ifade korunur; değişiklik, gerekçesi ve tarihiyle kaydedilir. Tohum çalışma sorusunu kurar; Varlık Protokolü konunun kimliğini, Gaye Protokolü ise yönelimin hangi yarara hizmet ettiğini ayrıntılandırır.

~~~text
  OZGUN SORU  -->  SINIRLANDIRILMIS CALISMA SORUSU
    ikisi ayri paragraflarda;  aradaki kapsam farki aciklanir
    butun alani aciklamak  =/=  belirli bir kavrami, karar surecini
                                veya teknik sistemi incelemek
    kapsam disinda birakilan  -/->  onemsiz olan

  BASLANGICTA ELDE BULUNANLAR
    kaynagi belirli dayanaklar | calisma varsayimlari | acik sorular
    baslangic kaydinda yer almak  -/->  dogrulanmis olmak
    statuler:  kaynak iddiasi . dogrudan gozlem . yorum . beklenti
    anlami henuz belirsiz sozcukler:  bilgi . anlam . akil yurutme .
    makine . amac  -->  bu belirsizlik arastirmanin parcasi

  ILK TASIYICI KAYDI  ayri duzeylerde
    bilginin anlamini degerlendiren insan
    cikarimi gerceklestiren teknik sistem
    islemlerin fiziksel tasiyicisi

  BASLANGIC SORUSU DEGISIRSE
    eski ifade korunur;  degisiklik gerekcesi ve tarihiyle kaydedilir
~~~

*Çizim 3 — Tohum: özgün soru ve çalışma sorusu; başlangıçta elde bulunanlar; ilk taşıyıcı kaydı.*

### Uygulama girdisi

Çalışmanın özgün sorusu, eldeki notlar veya kaynaklar ve incelenecek konu. Belirlenmemiş başlangıç alanları açık soru olarak kaydedilebilir.

### Masaüstünde uygulama

1. Çalışma kaydının üst bilgisine çalışma adı, tarih, kayıt sürümü ve çalışmayı yürüten kişi veya sistemi yaz. İncelenecek bir dosya, örnek veya mevcut sistem varsa konumunu belirt.

2. Özgün soruyu kendi ifadesiyle koru. Ardından bu çalışma içinde cevaplanabilecek biçimde sınırlandırılmış çalışma sorusunu ayrı bir paragrafta yaz; ikisi arasındaki kapsam farkını açıkla.

3. Başlangıç bilgilerini dayanak, varsayım ve açık soru olarak ayır. Her dayanağa kısa bir ad veya kimlik ver; ifadenin gözlem mi, kaynak iddiası mı, norm mu olduğunu ve nereden geldiğini belirt.

4. Kapsamı, kapsam dışındaki konuları, beklenen kullanımı ve üzerinde çalışılacak somut örneği kaydet. Beklenen çıktıyı gözlenebilir biçimde tarif et: kavramsal tanım, temsil taslağı, gerekçeli değerlendirme veya başka bir belirli çıktı.

5. Katkı sağlayan, işlemi yürüten ve sonucu kullanacak rolleri kaydet. Varlık Protokolü'nde açıklığa kavuşturulacak temel kavramları ve taşıyıcı belirsizliklerini belirt.

### Beklenen kayıt

Başlangıç sorusu, sınırlandırılmış çalışma sorusu, yönelim, kapsam, başlangıç dayanakları, varsayımlar, açık sorular, roller ve beklenen çıktı. Bunlar çalışma kaydının 0. bölümünü oluşturur.

### Tamamlanma ve geri dönüş

**Tamamlanma:** Bir okur neyin araştırıldığını, hangi kabullerle başlandığını, hangi çıktının beklendiğini ve ilk olarak neyin ele alınacağını anlayabiliyorsa başlangıç kaydı tamamlanmıştır. Açık sorular, araştırmanın bir parçası olarak görünür kalır.

**Geri dönüş:** Konu veya kullanım amacı değiştiğinde, kapsam genişlediğinde, belirleyici bir başlangıç varsayımı geçersiz çıktığında ya da aynı sözcük farklı çalışma soruları doğurduğunda bu protokole dön. Değişikliği tarih ve gerekçesiyle kaydet; etkilenen sonraki protokolleri belirt.

## 1 Varlık Protokolü

> Nedir? Onu o yapan nelerdir? Neler değildir?

### Anlamı ve sınırları

Bilgi Temsili ve Sembolik Akıl Yürütme Mühendisliği, belirli bir alan hakkında bilinenleri, varsayılanları, kaynak iddialarını ve uygulanan kuralları anlamı belirlenmiş, bilgisayarca işlenebilir temsiller hâlinde kurma; bu temsillerden hangi sonuçların hangi koşullarda elde edilebileceğini tasarlama; ortaya çıkan sistemi sınama, işletme ve güncel tutma pratiğidir. Yerleşik araştırma alanı bilgi temsili ve akıl yürütmedir. Mühendislik vurgusu, bu yaklaşımın bir görev için çalışır, denetlenebilir ve sürdürülebilir hâle getirilmesini öne çıkarır. [1]

Varlık bakımından temel iş, nelerin ayrı şeyler olarak kabul edileceğini belirlemektir. Nesne, kavram, ilişki, durum, olay, rol, kaynak iddiası ve norm aynı türden öğeler değildir. Bir kişinin eğitim almış olması, eğitiminin hâlen geçerli olması ve belirli bir cihaz için yetkilendirilmiş olması farklı durumlardır. Görev için önemli bu ayrımlar temsil edilmediğinde, çıkarım mekanizması onları yalnız daha güçlü hesaplama yaparak kendiliğinden geri getiremez. Temsilin kapsamı, sistemin sorabileceği soruları ve destekleyebileceği sonuçları etkiler.

Sembolik nitelik, yalnızca matematiksel işaretler veya insanın kolay okuyabildiği adlar kullanmak değildir. İfadelerin yapısı, yorumlanma koşulları ve hangi işlemlere konu olacağı belirlenir. Tümdengelimsel durumda bir sonucun öncüllerden çıkması, bu öncülleri doğru kılan her yorumun sonucu da doğru kılması anlamına gelir. Kullanılabilir bir güvence için öncüllerin tutarlılığı, verilerin doğruluğu ve temsilin alana uygunluğu ayrıca değerlendirilir. Bu tanım, bütün akıl yürütme türlerini tek bir tümdengelim biçimine indirgemez. [2]

Temsil, dünyayı görev bakımından seçerek ve sadeleştirerek taşır. Bu nedenle modelin içindeki doğruluk ile dünyaya uygunluk ayrı yükümlülüklerdir. Bilgi temsili; dünyanın yerine kullanılan bir model, hangi ayrımların kabul edildiğini gösteren ontolojik seçimler, çıkarıma yön veren bir yapı, hesaplama ortamı ve insanların bilgiyi ifade edebildiği bir araç olarak birlikte ele alınabilir. Bu işlevler, alanın yalnız veri yapısı seçimine indirgenememesini açıklar. [3]

~~~text
  ALAN  [1]
    bilinenleri, varsayilanlari, kaynak iddialarini ve kurallari
    anlami belirlenmis, bilgisayarca islenebilir temsiller halinde
    kurmak
    hangi sonuclarin hangi kosullarda elde edilebilecegini tasarlamak
    sistemi sinamak, isletmek ve guncel tutmak

  AYNI TURDEN OGE DEGIL
    nesne . kavram . iliski . durum . olay . rol . kaynak iddiasi . norm
    ornek, farkli durumlar:
      egitim almis olmak
      egitimin halen gecerli olmasi
      belirli bir cihaz icin yetkilendirilmis olmak
    temsil edilmeyen ayrim  -/->  daha guclu hesaplamayla kendiliginden
                                  geri gelmek

  TUMDENGELIM  [2]
    onculleri dogru kilan her yorum sonucu da dogru kilar
    ayrica degerlendirilir:  onculerin tutarliligi . verilerin
    dogrulugu . temsilin alana uygunlugu

  TEMSILIN ISLEVLERI  [3]
    dunyanin yerine kullanilan model | ontolojik secimler | cikarima
    yon veren yapi | hesaplama ortami | insanlarin bilgiyi ifade
    edebildigi arac
    modelin icindeki dogruluk  =/=  dunyaya uygunluk
~~~

*Çizim 4 — Varlık: alan; aynı türden olmayan öğeler; tümdengelim; temsilin işlevleri.*

Alanı taşıyanın kim olduğu sorusu üç düzeyde yanıtlanır. Tarihsel ve anlam kurucu düzeyde taşıyıcı, bilgiyi kuran, kullanan, sınayan ve düzelten insanlar ile onların ortak pratikleridir. İşlevsel düzeyde taşıyıcı, temsil edilmiş bilgiyle çalışan sistemdir; bu sistem amaçlarına göre eylem seçiyorsa bilgiye dayalı bir ajan olarak betimlenebilir. Maddi düzeyde taşıyıcı, programın ve kayıtların üzerinde gerçekleştiği fiziksel düzenektir. Bu ayrım, insanı makineye veya bütün sistemi tek bir kişiye özdeşleştirmeden, hangi yeteneğin nerede bulunduğunu görünür kılar. Newell'in bilgi düzeyi yaklaşımı, bilgi ve amaçlar üzerinden yapılan betimlemeyi bunları gerçekleştiren sembolik işlemlerden ayırır. [4]

Klasik sembolik yapay zekânın temel modellerinden biri fiziksel sembol sistemidir: sembolik yapıları saklayan, oluşturan, değiştiren ve işleyen fiziksel olarak gerçekleşmiş bir düzen. Bunun genel zekâ için gerekli ve yeterli olduğu yönündeki güçlü sav, Newell ve Simon tarafından ampirik bir hipotez olarak sunulmuştur. Dolayısıyla bu model, insanın bütün varlığının veya bütün düşünmesinin açıklanmış olduğu şeklinde kaydedilmez. Bir ontoloji, bilgi tabanı veya çıkarım motoru da tek başına her zaman ajan değildir; bir ajanın bileşeni olabilir. [5]

~~~text
  TASIYICI  uc duzey
    +------------------------------------------------------------+
    | tarihsel ve anlam kurucu duzey                             |
    |   bilgiyi kuran, kullanan, sinayan ve duzelten insanlar    |
    |   ile onlarin ortak pratikleri                             |
    +------------------------------------------------------------+
    | islevsel duzey                                             |
    |   temsil edilmis bilgiyle calisan sistem;  amaclarina gore |
    |   eylem seciyorsa bilgiye dayali bir ajan                  |
    +------------------------------------------------------------+
    | maddi duzey                                                |
    |   programin ve kayitlarin uzerinde gerceklestigi fiziksel  |
    |   duzenek                                                  |
    +------------------------------------------------------------+
    insan  =/=  makine;  butun sistem  =/=  tek bir kisi

  BILGI DUZEYI  Newell  [4]
    bilgi ve amaclar uzerinden betimleme  =/=  bunlari gerceklestiren
                                               sembolik islemler

  FIZIKSEL SEMBOL SISTEMI  Newell ve Simon  [5]
    sembolik yapilari saklayan . olusturan . degistiren . isleyen
    fiziksel olarak gerceklesmis bir duzen
    genel zeka icin gerekli ve yeterli oldugu savi:  ampirik bir hipotez
    -/->  insanin butun varliginin veya dusunmesinin aciklanmis olmasi
    ontoloji . bilgi tabani . cikarim motoru:  tek basina her zaman ajan
    degil;  bir ajanin bileseni olabilir
~~~

*Çizim 5 — Varlık: taşıyıcının üç düzeyi; bilgi düzeyi; fiziksel sembol sistemi.*

Bu protokolün sınırı açıktır: Her yapılandırılmış veri, grafik veya kavram listesi, alanın bütün mühendislik sorumluluğunu yerine getirmiş sayılmaz. Kaydın bulunması onun doğruluğunu; sembolik işlem yapılması bilinçli kişiliği; modelin kurulması dünyanın eksiksiz temsilini göstermez. Bilgi adı altında işlenen bir gözlem, bir beyan, bir varsayım ve bir kuralın statüleri korunur. Sembolik bir sistem, insan zihninin eksiksiz kopyası olmak zorunda değildir; belirli görevleri kendi teknik mekanizmalarıyla gerçekleştirebilir.

Varlık Protokolü'nün kaydettiği kimlik, anlam ile çıkarımın birlikte tasarlanmasıdır. Bu kimlik, hangi varlık ve ilişkilerin konu edildiğini, hangi önermelerin kabul edildiğini, hangi sonuç türlerinin üretildiğini ve bunların hangi taşıyıcılar üzerinde gerçekleştiğini açık tutar. Kullanılan modelin bir yorum ve kapsam seçimi olduğu unutulmadan, bu seçimlerin gerektiğinde eleştirilebilmesi ve değiştirilebilmesi mümkün kılınır.

~~~text
  GOSTERMEZ
    kaydin bulunmasi            -/->  dogrulugu
    sembolik islem yapilmasi    -/->  bilincli kisilik
    modelin kurulmasi           -/->  dunyanin eksiksiz temsili
    her yapilandirilmis veri, grafik veya kavram listesi  -/->  alanin
    butun muhendislik sorumlulugu

  STATULER KORUNUR
    gozlem | beyan | varsayim | kural

  VARLIK PROTOKOLUNUN KAYDETTIGI KIMLIK
    anlam ile cikarimin birlikte tasarlanmasi
    model bir yorum ve kapsam secimi;  elestirilebilir ve
    degistirilebilir kalir
~~~

*Çizim 6 — Varlık: gösterilmeyenler; korunan statüler; kaydedilen kimlik.*

### Uygulama girdisi

Tohum kaydındaki çalışma sorusu, kapsam, başlangıç dayanakları ve açık kavramlar.

### Masaüstünde uygulama

1. Sorunun hangi nesne, olay, durum, ilişki ve roller hakkında olduğunu bir paragrafla yaz. Seçilen soruyu cevaplamak için gerekli kavramları çıkar.

2. Her temel kavram için kısa tanım, bir örnek ve karıştırılabileceği yakın kavramla farkını kaydet. Örneğin eğitim almış olmak ile eğitimin sorulan tarihte geçerli olması arasındaki ayrımı koru.

3. Kullanılacak ifadeleri gözlem, kaynak iddiası, varsayım, norm veya hedef olarak işaretle. Kaynak ve gerekçe bağlarını başlangıç kaydındaki dayanaklara bağla; kaynağı bulunmayan kabulün statüsünü açık yaz.

4. Taşıyıcıları üç düzeyde belirt: kavramları ve amaçları kuran veya değerlendiren insan ve kurumlar; temsil ve çıkarım işlevlerini gerçekleştiren sistem; kayıtların ve işlemlerin fiziksel taşıyıcısı. Ajan dediğin sistemin hangi amaçla hangi eylemi seçtiğini açıklayabiliyorsan bunu ayrıca kaydet.

5. Tanımın dışında kalanları ve bu çalışma kapsamında temsil edilmeyen durumları yaz. Sonucu etkileyen kavram belirsizliklerini ilgili soruyla birlikte açık bırak.

### Beklenen kayıt

Konu tanımı, temel kavramlar ve örnekleri, bilgi statüleri, taşıyıcıların görevleri ve temsil sınırları. Bunlar çalışma kaydının 1. bölümünde tutulur.

### Tamamlanma ve geri dönüş

**Tamamlanma:** Seçilen sorudaki temel terimler açıklanabiliyor ve kritik kavram karışıklıkları görünür hâle geliyorsa kayıt tamamlanabilir. Çözülmemiş bir anlam farkı sonucu etkiliyorsa o sonuç kesinleştirilmez; etkisi kayda geçirilir.

**Geri dönüş:** Bir kavram iki farklı anlamda kullanılıyorsa bu bölüme dön. Kavramsal düzeltme çalışma sorusunu değiştiriyorsa Tohum kaydını da güncelle; bağımlı kuralları ve sonuçları yeniden değerlendir.

## 2 Mekan Protokolü

> Nerededir? Bu yeri, oraya has bir yer yapan nelerdir? Neler değildir?

### Anlamı ve sınırları

Bilgi Temsili ve Sembolik Akıl Yürütme Mühendisliği; mantık, yapay zekâ, veri yönetimi, yazılım mühendisliği ve uygulama alanının bilgisinin kesişiminde bulunur. Mantık anlam ve çıkarım çerçevelerini; veri yönetimi kayıt, sorgu ve bütünlük olanaklarını; yazılım mühendisliği uygulanabilirlik ve işletim düzenini; alan uzmanlığı ise kavramların uygulamadaki karşılıklarını sağlar. Bu alanların sınırları birbirini dışlayan duvarlar değildir. Aynı çalışma, bilgi mühendisliği ile biçimsel doğrulama veya veri yönetimi kapsamında birlikte değerlendirilebilir. [1]

Bir sistemin içindeki yeri, gözlem ve ifadelerden gerekçeli sonuçlara geçişin kurulduğu işlevsel konumdur. Veriler ve alan tanımları bir temsile bağlanır; çıkarım ve denetim bu temsil üzerinde çalışır; sonuçlar, eksik dayanaklar veya çelişkiler ilgili işlem ve inceleme süreçlerine aktarılır. Bu işlev ayrı bir servis, bir veritabanı sorgusu, bir kural sistemi, bir planlayıcı veya bir ispat sistemi içinde gerçekleşebilir. Her uygulama için ayrı ve büyük bir zekâ katmanı kurmak gerekmez.

Veritabanı ile bilgi tabanını, birinin yalnız sakladığı diğerinin düşündüğü şeklinde ayırmak yanıltıcıdır. Sorgulama, bütünlük denetimi ve türetilmiş ilişkiler aynı altyapıda birleşebilir. SPARQL'in çıkarım rejimleri, açıkça kaydedilmiş ilişkilerin yanında RDF veya OWL anlam kurallarının gerektirdiği ilişkiler üzerinden de sorgulama yapılmasını tanımlar. Bu nedenle sınır, yalnız depolama aracının türünde değil, veriye verilen anlamda ve kabul edilen çıkarım ilişkisindedir. [6]

~~~text
  KESISIM  [1]
    mantik                  anlam ve cikarim cerceveleri
    veri yonetimi           kayit, sorgu ve butunluk olanaklari
    yazilim muhendisligi    uygulanabilirlik ve isletim duzeni
    alan uzmanligi          kavramlarin uygulamadaki karsiliklari
    sinirlar birbirini dislayan duvarlar degil

  SISTEMDEKI ISLEVSEL KONUM
    veriler + alan tanimlari
          |  bir temsile baglanir
          v
    temsil  <---  cikarim ve denetim bu temsil uzerinde calisir
          |
          v
    sonuclar . eksik dayanaklar . celiskiler  -->  ilgili islem ve
                                                   inceleme surecleri
    yeri:  ayri servis | veritabani sorgusu | kural sistemi |
    planlayici | ispat sistemi
    her uygulama icin ayri ve buyuk bir zeka katmani gerekmez

  VERITABANI VE BILGI TABANI
    biri yalniz saklar, digeri dusunur ayrimi  -->  yaniltici
    SPARQL cikarim rejimleri  [6]:  acikca kaydedilmis iliskiler +
    RDF veya OWL anlam kurallarinin gerektirdigi iliskiler
    sinir:  depolama aracinin turunde degil;  veriye verilen anlamda ve
    kabul edilen cikarim iliskisinde
~~~

*Çizim 7 — Mekan: kesişim; sistemdeki işlevsel konum; veritabanı ve bilgi tabanı.*

Mekânın ikinci boyutu, fiziksel yer ile geçerlilik alanı arasındaki ayrımdır. Sunucunun bulunduğu yer, temsil edilen kuralın geçerli olduğu yer olmak zorunda değildir. Bir yetki yalnız belirli bir kurum, birim, cihaz sınıfı veya işlem için geçerli olabilir. Aynı sözcük farklı kurumsal ortamlarda farklı koşullar taşıyabilir. Sistemin işlevsel mekânı; veri kaynaklarını, kullanıcıları, uygulama ortamını ve kuralların sınırlarını birlikte içerir.

Taşıyıcı bakımından bu mekân, insanın çevresi, ortak dili, kayıtları, kurumları ve araçlarıyla kurduğu ilişkiler içinde oluşur. Bir kavramın anlamı her zaman tek kişinin zihninde tamamlanmaz; ortak kullanım, eğitim, uygulama ve düzeltme süreçleri içinde belirginleşir. Engelbart'ın insanı dil, araçlar, yöntemler ve eğitimle birlikte inceleyen yaklaşımı, bilgi kapasitesinin yalnız donanım kapasitesi olarak görülmemesi için bir dayanak sunar. Buradaki ortak düzen, bütün katkıların tek bir iradeden geldiği anlamına gelmez. [7]

~~~text
  FIZIKSEL YER  =/=  GECERLILIK ALANI
    sunucunun bulundugu yer  =/=  temsil edilen kuralin gecerli oldugu
                                  yer
    bir yetki yalniz belirli bir kurum, birim, cihaz sinifi veya islem
    icin gecerli olabilir
    ayni sozcuk farkli kurumsal ortamlarda farkli kosullar tasiyabilir
    islevsel mekan:  veri kaynaklari . kullanicilar . uygulama ortami .
    kurallarin sinirlari

  TASIYICI  Engelbart  [7]
    insan  +  dil  +  araclar  +  yontemler  +  egitim
    bilgi kapasitesi  =/=  yalniz donanim kapasitesi
    bir kavramin anlami her zaman tek kisinin zihninde tamamlanmaz
    ortak duzen  -/->  butun katkilarin tek bir iradeden gelmesi
~~~

*Çizim 8 — Mekan: fiziksel yer ve geçerlilik alanı; taşıyıcı.*

Bu yeri özel yapan, dünya ile temsil arasındaki uygunluk ve temsil ile hesaplanan sonuç arasındaki uygunluğun birlikte korunmasıdır. İlk ilişki, kavramların ve kayıtların alana gerçekten uyup uymadığını; ikinci ilişki, işlemlerin tanımlanmış anlam ve kurallara uyup uymadığını sorgular. Birinci ilişki bozulduğunda yanlış kurulmuş bir model doğru hesaplanabilir. İkinci ilişki bozulduğunda iyi kurulmuş bir modelden hatalı sonuç üretilebilir. Alan uzmanı, mühendis ve kullanıcı bu iki ilişkiye farklı katkılar sunar.

Sembollerin dünyadaki şeylere nasıl bağlandığı, bu konumun temel sorunlarından biridir. Sembolleri başka sembollerle tanımlamak ve biçimsel olarak işlemek, gönderimde bulundukları nesne ve durumlarla bağlantının nasıl kurulduğunu tek başına açıklamaz. Harnad'ın sembolleri dünyaya bağlama problemi bu soruyu tartışır; bundan makinelerin anlam taşımasının imkânsız olduğuna dair kesin bir hüküm çıkarılmaz. Bu protokol de alanı tek bir ürün, dil, sektör veya fiziksel konuma kapatmaz. [8]

~~~text
  IKI UYGUNLUK  birlikte korunur
    DUNYA
      ^
      |  1   kavramlar ve kayitlar alana gercekten uyuyor mu?
      v
    TEMSIL
      ^
      |  2   islemler tanimlanmis anlam ve kurallara uyuyor mu?
      v
    HESAPLANAN SONUC
    1 bozulursa  -->  yanlis kurulmus bir model dogru hesaplanabilir
    2 bozulursa  -->  iyi kurulmus bir modelden hatali sonuc
                      uretilebilir
    alan uzmani . muhendis . kullanici:  iki iliskiye farkli katkilar

  SEMBOLLERI DUNYAYA BAGLAMA  Harnad  [8]
    sembolleri baska sembollerle tanimlamak ve bicimsel olarak islemek
      -/->  gonderimdeki nesne ve durumlarla baglantinin aciklanmasi
    -/->  makinelerin anlam tasimasinin imkansiz oldugu yolunda kesin
          hukum
~~~

*Çizim 9 — Mekan: iki uygunluk; sembolleri dünyaya bağlama.*

### Uygulama girdisi

Varlık kaydındaki kavramlar ve taşıyıcılar; kaynakların, kuralların ve sonuçların kullanıldığı bağlamlar.

### Masaüstünde uygulama

1. Verinin nereden geldiğini, kuralın nerede geçerli olduğunu ve sonucun nerede kullanılacağını ayrı cümlelerle yaz. Yerel dosya veya sunucu konumunu, kurumsal ve işlemsel geçerlilik alanından ayır.

2. Görev için kapsamda olan kurum, birim, kullanıcı rolü, cihaz sınıfı veya işlem türünü belirt. Aynı terimin başka bir bağlamda farklı anlam taşıyıp taşımadığını kontrol et.

3. Kaynakların adını ve erişilebilir bağlantısını veya yerel dosya yolunu kaydet. Kaynağın erişilebilir olmasıyla içeriğinin incelenmiş olması arasındaki farkı koru; incelenen bölüm veya sürümü belirt.

4. Bir kaydın dünyadaki hangi nesne, olay veya durumu temsil ettiğini ve bu eşleştirmeyi neyin desteklediğini açıkla. Ardından kaynaktan temsile, değerlendirmeye ve sonucun kullanımına uzanan işlevsel yolu bir paragrafla tarif et.

5. Kayıtları sağlayan, kuralları belirleyen, işlemi yürüten ve sonucu kullanan tarafların bağlamlarını belirt. Başka bir bağlama taşınırken yeniden doğrulanması gereken eşleştirmeleri ve kabulleri yaz.

### Beklenen kayıt

Kaynak ve kullanım bağlamı, kuralların geçerlilik alanı, kaynak konumları, dünya–temsil eşleştirmesi, işlevsel yol ve bağlam sınırları. Bunlar çalışma kaydının 2. bölümünde tutulur.

### Tamamlanma ve geri dönüş

**Tamamlanma:** Her önemli kural ve sonucun hangi bağlamda kullanılacağı, kaynağının nerede bulunacağı ve temsil edilen durumla nasıl ilişkilendirildiği anlaşılabiliyorsa kayıt tamamlanır.

**Geri dönüş:** Aynı kaydın farklı varlıklara bağlandığı anlaşılırsa Varlık'a dön. Kullanım ortamı değişirse bu bölümü; görevin kapsamı değişirse Tohum'u da güncelle. Bağlam değişikliğinin kurallara ve sonuçlara etkisini Usül kaydına aktar.

## 3 Usül Protokolü

> Nasıl işler yapar? Bu yaptıklarını, ona has yapan nelerdir? Neler değildir?

### Anlamı ve sınırları

Bu alandaki usul, temsil edilen anlam ile izin verilen çıkarımın ilişkisini açıkça kurar. İş, önce sistemin cevaplaması gereken soruların ve desteklemesi gereken kararların belirlenmesiyle başlar. Bütün dünyayı modellemeye girişmek yerine, hangi soruların hangi kapsamda cevaplanacağı belirginleştirilir. Ontoloji tasarımındaki yeterlik soruları yaklaşımı, modelin kapsamını ve yeterliliğini bu sorular üzerinden değerlendirmeye imkân verir. [9]

Ardından görev için önemli kavramlar ve bilgi statüleri ayrılır. Gözlem, kaynak iddiası, varsayım, norm ve hedef aynı türden dayanak değildir. İki kaydın aynı varlığı gösterip göstermediği, bir rolün hangi bağlamda geçerli olduğu ve bir ifadenin hangi kaynaktan geldiği belirlenir. Bu çalışma, yalnız veri alanlarına ad verme işlemi değildir; birbirine dönüştürülmemesi gereken durumları ve ilişkileri korur.

Eksik bilginin anlamı ayrıca tanımlanır. Açık dünya kabulünde bir olgunun kayıtta bulunmaması onun yanlış olduğunu göstermez; bilgi eksik olabilir. Kapalı dünya kabulü ise kapsamı belirlenmiş bir alanda eldeki bilgilerden doğru olduğu çıkarılamayan önermelerin yanlış kabul edilmesine izin verir. OWL'nin açık dünya yaklaşımı, kayıt eksikliği ile olumsuzluğun neden ayrılması gerektiğini gösterir. Buna karşılık, eksiksiz kabul edilen bir başvuruda zorunlu belgenin teslim edilmemesi usule ilişkin bir eksiklik sayılabilir. Hangi sonucun çıkarılabileceği, uygulamanın anlam ve tamlık kabullerine bağlıdır. [10]

~~~text
  YETERLIK SORULARI  Gruninger ve Fox  [9]
    sistemin cevaplamasi gereken sorular ve desteklemesi gereken
    kararlar  -->  modelin kapsami ve yeterliligi bu sorularla
    degerlendirilir
    butun dunyayi modellemek yerine:  hangi soru, hangi kapsamda?

  AYNI TURDEN DAYANAK DEGIL
    gozlem | kaynak iddiasi | varsayim | norm | hedef
    iki kayit ayni varligi mi gosteriyor? . rol hangi baglamda
    gecerli? . ifade hangi kaynaktan geliyor?

  KAYITTA BULUNMAYAN BIR OLGU
                   ACIK DUNYA KABULU        KAPALI DUNYA KABULU
                   OWL  [10]                kapsami belirlenmis alan
    sonuc          yanlis oldugu            dogru oldugu cikarilamayan
                   gosterilmez;  bilgi      onermenin yanlis kabul
                   eksik olabilir           edilmesine izin verir
    ornek:  eksiksiz kabul edilen bir basvuruda zorunlu belgenin teslim
    edilmemesi  -->  usule iliskin bir eksiklik sayilabilir
    cikarilabilecek sonuc:  uygulamanin anlam ve tamlik kabullerine
    bagli
~~~

*Çizim 10 — Usül: yeterlik soruları; dayanak türleri; açık ve kapalı dünya.*

Akıl yürütmenin ürettiği sonuç türleri de birbirinden ayrılır. Tümdengelim seçilen anlam kuralları altında gereken sonucu; sınıflandırma bir nesnenin kavramsal konumunu; tutarlılık denetimi ifadelerin birlikte bağdaşıp bağdaşmadığını; kısıt çözümü koşulları sağlayan düzenlemeyi araştırır. Planlama, belirtilen eylem modeli altında hedefe götürebilecek bir yol veya politika üretir. Abdüksiyon açıklayıcı aday hipotez sunar. Varsayılan çıkarım ise yeni bilgiyle geri çekilebilen bir kabul üretir. Reiter'in çalışması bu son türün biçimsel olarak ele alınmasına temel örneklerden biridir. [11]

Temsil dili ve hesaplama yöntemi bu görevlerin yapısına göre seçilir. OWL ve betimleme mantıkları kavramsal ilişkiler için, SMT belirli kuramlar altında kısıtların birlikte sağlanabilirliği için, ASP ise kabul edilebilir çözümleri uygun program modelleriyle ilişkilendiren problem kurulumları için kullanılabilir. Her yöntemin aynı güvenceyi verdiği veya her uygulamada birlikte bulunması gerektiği varsayılmaz. İfade gücü, hesaplama maliyeti, veri hacmi ve bakım ihtiyacı birlikte değerlendirilir. OWL 2 profilleri, bazı ifade imkânlarını sınırlayarak belirli çıkarım görevlerini daha verimli yürütme tercihine örnektir. [12], [13], [14]

~~~text
  SONUC TURLERI  birbirinden ayrilir
    tumdengelim           secilen anlam kurallari altinda gereken sonuc
    siniflandirma         bir nesnenin kavramsal konumu
    tutarlilik denetimi   ifadeler birlikte bagdasiyor mu?
    kisit cozumu          kosullari saglayan duzenleme
    planlama              eylem modeli altinda hedefe goturebilecek yol
                          veya politika
    abduksiyon            aciklayici aday hipotez
    varsayilan cikarim    yeni bilgiyle geri cekilebilen kabul
                          (Reiter [11])

  DIL VE YONTEM  gorevin yapisina gore
    OWL ve betimleme      kavramsal iliskiler
    mantiklari
    SMT                   belirli kuramlar altinda kisitlarin birlikte
                          saglanabilirligi
    ASP                   kabul edilebilir cozumleri uygun program
                          modelleriyle iliskilendiren kurulumlar
    birlikte tartilir:  ifade gucu . hesaplama maliyeti . veri hacmi .
    bakim ihtiyaci
    OWL 2 profilleri  [12]:  bazi ifade imkanlarini sinirlayarak
    belirli cikarim gorevlerini daha verimli yurutme tercihi
~~~

*Çizim 11 — Usül: sonuç türleri; dil ve yöntem.*

Veri doğrulaması ile çıkarım farklı sorulara cevap verir. Bir kişinin bir belgeye sahip olduğu modelden çıkabilir; buna rağmen gönderilen kayıtta beklenen alan eksik olabilir. SHACL, veri grafiğinin belirlenen koşullara uyup uymadığını denetleyip raporlamak için kullanılır. Böyle bir denetim, kaydın koşullara uygunluğunu gösterir; kayıtta yazan her şeyin dünyada doğru olduğunu kanıtlamaz. Sonucun kaynakları, kullanılan kurallar, sürümler ve varsayımlar da gerektiğinde incelenebilir olmalıdır. PROV yaklaşımı verinin oluşumuna katkıda bulunan varlık, faaliyet ve sorumluların kaydını destekler. [15], [16]

Konuşmadaki varsayımsal cihaz örneği bu ayrımları somutlaştırır. Sadeleştirilmiş bir politikada bir kişi için eğitim geçerliliği, onay geçerliliği ve cihazın uygunluğu birlikte doğrulanırsa, sorulan zamanda politikaya göre uygunluk türetilir. Bu üç koşul bir yeter koşul olarak kurulmuştur; uygunluğun başka yolları olmadığını veya bütün koşulların yalnız bu kuralla zorunlu kılındığını söylemez. Üretilen sonuç, tanımlanmış politikaya uygunluktur; modellenmemiş bütün fiziksel koşullar hakkında sınırsız bir güvence değildir.

Aynı örnekte eğitim geçerliliği hakkında bilgi bulunamıyorsa, açık dünya kabulünde geçersizlik çıkarılmaz; uygunluk da bu kuralla desteklenmez. Uygulama, doğrulanmış dayanak gelene kadar işlemi bekletebilir. Sunulan belgenin süresi dolmuşsa bu belge sorulan andaki koşulu sağlamaz; başka bir geçerli dayanak olup olmadığı ayrıca değerlendirilir. Cihaz durumu hakkında kaynaklar çelişiyorsa uyuşmazlık saptanır; kaynak önceliği veya başka bir çözüm yöntemi gerekir. Hesaplama süresi dolmuşsa sonuç belirlenememiştir; bu durum çözümsüzlük veya uygunsuzluk olgusuna çevrilmez.

~~~text
  CIHAZ ORNEGI  varsayimsal, sadelestirilmis politika
    egitim gecerli   ---+
    onay gecerli     ---+--- uc kosul birlikte --->  sorulan zamanda
    cihaz uygun      ---+                            politikaya gore
                                                     uygunluk turetilir
    yeter kosul:  uygunlugun baska yollari olmadigini soylemez
    sonuc:  tanimlanmis politikaya uygunluk;  modellenmemis fiziksel
    kosullar hakkinda sinirsiz guvence degil

  SINIR DURUMLARI
    egitim gecerliligi     acik dunyada gecersizlik cikarilmaz;
    hakkinda bilgi yok     uygunluk da desteklenmez;  islem
                           bekletilebilir
    belgenin suresi        sorulan andaki kosulu saglamaz;  baska
    dolmus                 gecerli dayanak ayrica degerlendirilir
    cihaz durumu           uyusmazlik saptanir;  kaynak onceligi veya
    hakkinda kaynaklar     baska bir cozum yontemi gerekir
    celisiyor
    hesaplama suresi       sonuc belirlenemedi;  cozumsuzluk veya
    doldu                  uygunsuzluk olgusuna cevrilmez
~~~

*Çizim 12 — Usül: cihaz örneği ve sınır durumları.*

Usulün taşıyıcısı da tek bir öğe değildir. Alan uzmanları kavramların uygulamadaki karşılıklarını belirleyebilir; kurumlar politikaları kabul edebilir; mühendisler bu ayrımları biçimsel sisteme aktarabilir; veri kaynakları dayanak sağlayabilir; teknik sistem çıkarımı gerçekleştirebilir. Bazı adımlar öğrenme veya otomasyonla yürütülebilir. Her durumda işlemi yapanın, dayanağı sağlayanın ve değerlendirme sorumluluğunu üstlenenin kim olduğu görünür kalır.

Bu usulü ona has yapan, sonucun statüsünü de işlemin parçası saymasıdır. Bir belge bulmak, benzer örnek getirmek, akıcı bir açıklama üretmek veya mantıksal bir çıkarım yapmak aynı iş değildir. Mantıksal gerekçe, nedensel açıklamayla da özdeş değildir; nedensellik için ilgili ilişkiler ayrıca modellenir. Çelişkiyi bulmak onu çözmek anlamına gelmez. Sembolik yapı denetlenebilirlik imkânı sunar; anlaşılır ve gerçek dayanaklara sadık açıklamalar ayrıca tasarlanır.

~~~text
  VERI DOGRULAMASI  =/=  CIKARIM
    modelden:            kisinin bir belgeye sahip oldugu cikabilir
    gonderilen kayitta:  beklenen alan eksik olabilir
    SHACL [15]:  veri grafigi belirlenen kosullara uyuyor mu? --> rapor
    kosullara uygunluk  -/->  kayitta yazan her seyin dunyada dogrulugu
    PROV  [16]:  verinin olusumuna katkida bulunan varlik, faaliyet ve
    sorumlularin kaydi

  USULUN TASIYICISI  tek bir oge degil
    alan uzmanlari    kavramlarin uygulamadaki karsiliklarini
                      belirleyebilir
    kurumlar          politikalari kabul edebilir
    muhendisler       ayrimlari bicimsel sisteme aktarabilir
    veri kaynaklari   dayanak saglayabilir
    teknik sistem     cikarimi gerceklestirebilir
    her durumda gorunur:  islemi yapan . dayanagi saglayan .
    degerlendirme sorumlulugunu ustlenen

  AYNI IS DEGIL
    belge bulmak | benzer ornek getirmek | akici aciklama uretmek |
    mantiksal cikarim yapmak
    mantiksal gerekce  =/=  nedensel aciklama
    celiskiyi bulmak  -/->  onu cozmek
    sonucun statusu islemin parcasidir
~~~

*Çizim 13 — Usül: veri doğrulaması ve çıkarım; usulün taşıyıcısı; aynı olmayan işler.*

### Uygulama girdisi

Çalışma sorusu, tanımlanmış kavramlar, bilgi statüleri, kaynaklar, bağlam ve mevcut kurallar.

### Masaüstünde uygulama

1. Yapılacak işi ve beklenen sonucun türünü yaz: sınıflandırma, tümdengelim, tutarlılık denetimi, kısıt çözümü, planlama, açıklayıcı hipotez üretimi veya başka bir belirli işlem. Kullanılan temsil ve çıkarım çerçevesini belirt: ifadeler hangi anlamda yorumlanıyor, hangi çıkarım kuralları uygulanıyor? Elle değerlendirmede bu kabulleri düz yazıyla açıkla; mevcut araç kullanılıyorsa adını, sürümünü ve ilgili yapılandırmayı kaydet.

2. Eksik bilginin nasıl ele alınacağını belirle. Açık dünya kabulünde kayıt yokluğundan yanlışlık çıkarma. Kapalı dünya kabulü kullanılacaksa bunun kapsamını, tamlık varsayımını ve hangi önermeler için geçerli olduğunu kaydet. Çelişkili dayanaklar varsa bunların çıkarıma etkisini ve uygulanacak yaklaşımı ayrıca belirt; seçilmemiş veya uygulanmamış bir çözümü gerçekleşmiş sayma. Kaynak önceliği kullanılıyorsa gerekçesini yaz.

3. Her kuralı açık biçimde yaz ve kısa bir ad veya kimlik ver. Koşulun yeterli, gerekli ya da her ikisi olup olmadığını belirt. A → B kuralından, başka bir dayanak olmadan B → A veya yalnız A bulunamadığı için B'nin yanlış olduğu sonucunu çıkarma.

~~~text
  KURAL  A --> B
    kosul:  yeterli mi?  gerekli mi?  ikisi birden mi?  kayda yazilir
    baska bir dayanak olmadan cikarilmaz:
      x  B --> A
      x  A bulunamadi, oyleyse B yanlis
~~~

*Çizim 14 — Usül: kuralın yönü.*

4. Somut bir soruyu eldeki bilgilerle adım adım değerlendir. Her adımda kullanılan dayanak ve kuralı, yapılan işlemi ve oluşan sonucu göster. Elle izlenen adımları ve araç tarafından üretilen çıktıları kendi statüleriyle kaydet.

5. Görev açısından sonucu etkileyen en az bir sınır durumunu incele: bir dayanağın eksilmesi, bir koşulun değişmesi veya kaynakların çelişmesi gibi. Uyuşmazlık saptanırsa kapsamını yaz; çözüm uygulanmışsa yöntemi ve gerekçesini ayrıca kaydet.

6. Sonucu ve hesaplamanın durumunu ayrı alanlarda belirt. Olumlu desteği, olumsuz desteği, bilinmeyeni ve çelişkiyi ayır. Süre veya kaynak sınırı nedeniyle tamamlanamayan hesabı çözümsüzlük olarak kaydetme; elde edilmiş kısmi sonuç varsa kendi kapsamıyla koru.

### Beklenen kayıt

İşlem türü, temsil ve çıkarım çerçevesi, eksik bilgi kabulleri, çelişkiyi ele alma ilkesi, kurallar, izlenebilir bir örnek değerlendirme, bir sınır durumunun etkisi, sonuç statüsü ve hesaplamanın tamamlanma durumu. Bunlar çalışma kaydının 3. bölümünde tutulur.

### Tamamlanma ve geri dönüş

**Tamamlanma:** Sonuçtan kullanılan dayanak ve kurallara geri gidilebiliyor, koşulların yönü açık ve incelenen sınır durumunun etkisi açıklanabiliyorsa yöntem kaydı tamamlanır. Sonucun belirsiz veya hesabın tamamlanamamış olması ayrıca belirtilir.

**Geri dönüş:** Sorun kavramdaysa Varlık'a, bağlamdaysa Mekan'a, kuralın uygulanışındaysa bu bölümün ilgili adımına dön. Yeni dayanakla veya kural değişikliğiyle etkilenen sonuçları işaretle; zaman ve sürüm kaydını güncelle.

## 4 Zaman Protokolü

> Hangi andadır? Bu anı, diğer zamanlardan farklı yapan nelerdir? Neler değildir?

### Anlamı ve sınırları

Zaman Protokolü, alanın tarihsel zamanı, sistemin yaşamındaki zaman ve temsil edilen bilginin zamanı olmak üzere üç ölçeği birlikte ele alır. Tarihsel köken, belirli bir uygulamanın kuruluş tarihinden farklıdır; sistemin bugün bildiği şey, bir olayın bugün gerçekleştiği anlamına gelmez. Bu ayrımlar, geçmişe ilişkin bir kaydı veya geleceğe dönük bir planı hangi koşullarda değerlendirdiğimizi belirler.

Tarihsel olarak alan, yapay zekânın erken dönemlerine uzanır. McCarthy'nin 1959 tarihli Programs with Common Sense çalışması, biçimsel ifadelerden sonuç çıkaran ve yeni bildirimlerle davranışı geliştirilebilen bir sistem düşüncesini açıkça ele alır. Bu tarihsel kaynak, günümüzdeki bütün teknik sınırları tanımlayan bir metin gibi okunmaz; kendi döneminin araştırma programını ve önerilerini kaydeder. [17]

Alan yalnız geçmişteki uzman sistemlerle özdeş değildir. Konuşmada kullanılan yakın dönem örneği AlphaGeometry'dir: dil modelinin yardımcı geometrik yapılar önermesi ile sembolik motorun bunlar üzerinden çıkarım yapması birlikte işler. Bu örnek belirli bir matematik alanındaki teknik işbirliğini gösterir; genel zekânın veya bütün dünya bilgisinin çözüldüğünü göstermez. 2026 KR gündeminde öğrenme, açıklama ve gerçek uygulamalara ayrılmış çalışmalar da bulunur. Öğrenilmiş kavramların hedeflenen anlamlarla eşleşmesi ayrıca denetlenmesi gereken bir sorundur. [1], [18], [19]

~~~text
  UC OLCEK
    alanin tarihsel zamani . sistemin yasamindaki zaman . temsil edilen
    bilginin zamani
    tarihsel koken  =/=  bir uygulamanin kurulus tarihi
    sistemin bugun bildigi  -/->  olayin bugun gerceklesmesi

  METINDEKI ORNEKLER  aralar olcekli degil
    1959    o  McCarthy, Programs with Common Sense  [17]
            |  bicimsel ifadelerden sonuc cikaran, yeni bildirimlerle
            |  davranisi gelistirilebilen sistem dusuncesi
    2024    o  AlphaGeometry  [18]
            |  dil modeli yardimci geometrik yapilar onerir;  sembolik
            |  motor bunlar uzerinden cikarim yapar
    2026    o  KR 2026 gundemi  [1] [19]
               ogrenme, aciklama ve gercek uygulamalar;  ogrenilmis
               kavramlarin hedeflenen anlamlarla eslesmesi denetlenmeli
    tarihsel kaynak  -/->  bugunku butun teknik sinirlarin tanimi
    AlphaGeometry  -/->  genel zekanin veya butun dunya bilgisinin
                         cozulmesi
    alan  =/=  yalniz gecmisteki uzman sistemler
~~~

*Çizim 15 — Zaman: üç ölçek; metindeki örnekler.*

Bir sistemin yaşamında bu mühendislik kuruluşta, kullanımda ve değişimde yer alır. Kuruluşta hangi ayrımların ve varsayımların kullanılacağı belirlenir. Kullanımda bir soru veya eylemin mevcut dayanaklarla desteklenip desteklenmediği değerlendirilir. Değişimde ise yeni bilgi veya kuralın önceki sonuçlara etkisi incelenir. Bu nedenle ona özgü an, bir iddianın hangi koşullarda kabul edileceğinin veya eski bir kabulün hâlen desteklenip desteklenmediğinin belirlenmesi gereken andır.

Gerekçe ve bağımlılıkların izlenmesi, bu sürekliliğin teknik karşılıklarından biridir. Doyle'un Truth Maintenance System çalışması, kabullerin nedenlerinin kaydedilmesini ve yeni bilgilerle uyuşmayan kabullerin yeniden ele alınmasını inceler. Bir sistemin sembolik olması, eski sonuçları kendiliğinden doğru güncelleyeceği anlamına gelmez. Güncelleme kapsamı, bağımlılıklar ve geri alınacak sonuçlar ayrıca tasarlanır. [20]

~~~text
  SISTEMIN YASAMINDA
    kurulus     hangi ayrimlar ve varsayimlar kullanilacak?
       |
       v
    kullanim    soru veya eylem mevcut dayanaklarla destekleniyor mu?
       |
       v
    degisim     yeni bilgi veya kural onceki sonuclari nasil etkiler?
    ona ozgu an:  bir iddianin hangi kosullarda kabul edilecegi veya
    eski bir kabulun halen desteklenip desteklenmedigi belirlenmesi
    gereken an

  GEREKCE VE BAGIMLILIK  Doyle, TMS  [20]
    kabullerin nedenleri kaydedilir
    yeni bilgiyle uyusmayan kabuller yeniden ele alinir
    sembolik olmak  -/->  eski sonuclari kendiliginden dogru guncellemek
    ayrica tasarlanir:  guncelleme kapsami . bagimliliklar . geri
    alinacak sonuclar
~~~

*Çizim 16 — Zaman: sistemin yaşamı; gerekçe ve bağımlılık.*

Temsil edilen dünyada geçerlilik zamanı ile kayıt zamanı ayrılır. Bir yetkinin 1 Ekim'de sona erdiğini ve bu değişikliğin sisteme 5 Ekim'de işlendiğini düşünelim. 3 Ekim'de yapılan bir işlem için bugün iki ayrı değerlendirme mümkündür: Bugün eldeki bilgiye göre yetki o tarihte geçerli miydi; sistem o gün elindeki kayıtlara göre hangi sonuca ulaşabiliyordu? Bu sorular farklı cevaplar alabilir. Zamansal veri yönetimindeki geçerlilik zamanı ve kayıt zamanı ayrımı bu farklılığı açıklar. [21]

Kararın verildiği an ile eylemin gerçekleştirildiği an da aynı olmak zorunda değildir. Bir onay değerlendirmeden sonra geri çekilmişse, işlem öncesinde yeniden değerlendirme gerekebilir. Teknik taşıyıcı; bellek, sürüm, geçerlilik aralığı, durum değişimi ve gelecek hedeflerini temsil ederek bu ilişkileri taşır. Yalnız zaman etiketi eklemek, hangi zamanın hangi kurala etki edeceğini belirlemez.

Bu protokol, alanı tek bir tarihsel döneme veya bir defa tamamlanan modelleme işine kapatmaz. Dün uygun olup bugün uygun olmamak tek başına çelişki değildir; farklı zamanlara ilişkin farklı önermeler söz konusu olabilir. Ek bilgiyle aynı konu hakkındaki önceki kabulün geri çekilmesi ise ayrı bir akıl yürütme problemidir. Zaman üzerinde hesaplama yapılması, öznel zaman deneyimi veya bilinç hakkında ayrıca bir hüküm oluşturmaz.

~~~text
  GECERLILIK ZAMANI VE KAYIT ZAMANI  [21]
         1 Ekim          3 Ekim          5 Ekim           bugun
    --------+---------------+---------------+---------------+----->
          yetki           islem        degisiklik
        sona erer        yapilir     sisteme islenir
            |<-- degisiklik kayitta yok --->|
    bugun iki ayri degerlendirme:
      bugun eldeki bilgiye gore yetki 3 Ekim'de gecerli miydi?
      sistem o gun elindeki kayitlara gore hangi sonuca ulasabiliyordu?
    bu sorular farkli cevaplar alabilir

  AYNI AN DEGIL
    kararin verildigi an  =/=  eylemin gerceklestirildigi an
    onay degerlendirmeden sonra geri cekilmisse  -->  islem oncesinde
    yeniden degerlendirme gerekebilir
    yalniz zaman etiketi eklemek  -/->  hangi zamanin hangi kurala etki
    edecegini belirlemek
    dun uygun, bugun uygun degil  -/->  tek basina celiski
    ek bilgiyle onceki kabulun geri cekilmesi:  ayri bir akil yurutme
    problemi
~~~

*Çizim 17 — Zaman: geçerlilik zamanı ve kayıt zamanı; aynı olmayan anlar.*

### Uygulama girdisi

Kaynaklar, kurallar, örnek değerlendirme, bunlara ait mevcut tarihler, geçerlilik bilgileri ve sürümler.

### Masaüstünde uygulama

1. Çalışmanın yapıldığı tarihi ve kullanılan kaynak, model veya kural sürümlerini kaydet. Kaynakta bulunmayan tarihi uydurmak yerine hangi zaman bilgisinin bilinmediğini belirt.

2. Görev için gerekli olan olay zamanı, geçerlilik aralığı, kayda giriş zamanı, karar zamanı ve eylem zamanını ayrı yaz. Gerekli olmayan zaman türlerini kısa gerekçeyle uygulanmaz olarak kaydet.

3. Bir başlangıç veya bitiş sınırının sonucu değiştirip değiştirmediğini incele. Sınır gününün veya anının aralığa dâhil olup olmadığını, saat dilimi gerekiyorsa onu belirt. Belirsizlik sonuca etki ediyorsa sonuç statüsüne yansıt.

4. Bir kayıt veya kural değiştiğinde hangi sonuçların yeniden değerlendirileceğini yaz. Önceki değerlendirmeyi dayanaklarıyla koru; yeni değerlendirmenin neden farklılaştığını açıkla.

5. Yeniden incelemeyi gerektiren somut olayları belirt: geçerlilik süresinin dolması, kural değişikliği, kaynak düzeltmesi, kapsamın veya kullanım ortamının değişmesi gibi. Bir sonraki inceleme tarihi kullanılıyorsa seçilme gerekçesini yaz.

### Beklenen kayıt

Zaman türleri, geçerlilik sınırları, kullanılan sürümler, bir değişimin sonuçlara etkisi ve yeniden değerlendirme koşulları. Bunlar çalışma kaydının 4. bölümünde tutulur.

### Tamamlanma ve geri dönüş

**Tamamlanma:** Sonucun hangi zamana ve hangi bilgi durumuna ait olduğu anlaşılabiliyor, gerekli tarihlerdeki eksiklikler görünür kalıyor ve değişimin etkileyeceği sonuçlar izlenebiliyorsa kayıt tamamlanır.

**Geri dönüş:** Yeni kayıt, süre sonu veya kural sürümü sonuçları etkilediğinde Usül değerlendirmesini yenile. Zaman bilgisi eksikliği belirleyiciyse ilgili sonucu belirsiz olarak kaydet. Değişen kullanım bağlamı için Mekan'a dön.

## 5 Gaye Protokolü

> Hangi nihai amaca hizmet eder? Bu nihai amaca ulaştıran nelerdir? Neler değildir?

### Anlamı ve sınırları

Bu mühendisliğin ortak teknik yönelimi, belirli bir görev için gerekli bilgiyi açık ve işlenebilir hâle getirerek sonuçların, kararların ve eylemlerin hangi gerekçelerle desteklendiğini değerlendirmeyi mümkün kılmaktır. Ortak anlam kurmak, örtük sonuçları ortaya çıkarmak, çelişkileri bulmak, seçenekleri sınamak ve bilgi değiştiğinde kararları yeniden ele almak bu yönelimin parçalarıdır.

Bunun ötesindeki insani veya kurumsal amaç uygulamaya göre belirlenir. Bilimsel iddiaların denetlenmesi, üretimde hataların azaltılması, kaynakların uygun kullanılması veya hizmet kurallarının tutarlı uygulanması farklı hedeflerdir. Teknik yöntem, bu hedeflerin seçilme gerekçesinin yerine geçmez. Bir amaç, sisteme başarı ölçütü olarak yazılmış olsa da neden izlenmeye değer bulunduğu ve sonuçlarının kimler tarafından değerlendirileceği ayrıca açıklanmalıdır.

Gaye bakımından taşıyıcılar ayrılır. Hedefi yürüten teknik sistem, hedefi belirleyen veya sonuçlarını değerlendiren insan ve kurumlarla aynı şey değildir. Sistem alt hedefler oluşturabilir, planını değiştirebilir ve seçenekler arasında seçim yapabilir. Bu işlemler, izlenen hedeflerin değerini kendiliğinden haklılaştırmaz. Ortak bir bilgi sisteminin bulunması da bütün tercihlerin tek bir iradeden geldiğini veya tek bir yerde sorumluluk toplandığını göstermez.

Başarı üç düzeyde ele alınır. Çıkarım doğruluğu, sonucun belirtilen model ve varsayımlardan uygun biçimde elde edilmesidir. Temsil yeterliliği, modelin görev için önemli gerçekleri ve ayrımları doğru ve yeterli biçimde kapsamasıdır. Amaç uygunluğu ise çözülmekte olan problem ve başarı ölçütünün istenen yarara hizmet etmesidir. Bu düzeyler birbirinin yerine geçmez: Doğru çıkarım yanlış kayda dayanabilir; iyi model kötü seçilmiş bir hedefe hizmet edebilir; yararlı bir hedef yetersiz temsil nedeniyle gerçekleştirilemeyebilir.

~~~text
  ORTAK TEKNIK YONELIM
    gorev icin gerekli bilgiyi acik ve islenebilir hale getirmek;
    sonuclarin, kararlarin ve eylemlerin hangi gerekcelerle
    desteklendigini degerlendirmeyi mumkun kilmak
    insani veya kurumsal amac uygulamaya gore belirlenir;  teknik
    yontem, hedefin secilme gerekcesinin yerine gecmez

  GAYENIN TASIYICILARI
    hedefi yuruten teknik sistem  =/=  hedefi belirleyen veya
                                       sonuclarini degerlendiren insan
                                       ve kurumlar
    alt hedef olusturmak . plan degistirmek . secim yapmak  -/->
    izlenen hedeflerin degerini hakli kilmak

  BASARININ UC DUZEYI  birbirinin yerine gecmez
    cikarim dogrulugu    sonuc belirtilen model ve varsayimlardan uygun
                         bicimde elde edildi mi?
    temsil yeterliligi   model gorev icin onemli gercekleri ve ayrimlari
                         dogru ve yeterli kapsiyor mu?
    amac uygunlugu       problem ve basari olcutu istenen yarara hizmet
                         ediyor mu?
    dogru cikarim   -->  yanlis kayda dayanabilir
    iyi model       -->  kotu secilmis bir hedefe hizmet edebilir
    yararli hedef   -->  yetersiz temsil nedeniyle
                         gerceklestirilemeyebilir
~~~

*Çizim 18 — Gaye: ortak teknik yönelim; gayenin taşıyıcıları; başarının üç düzeyi.*

Amaca ulaşmayı destekleyen ilk unsur, göreve uygun kapsamdır. Sistem, gerekli soruları cevaplayacak ayrımları taşımalı ve bu yeterlilik görev üzerinden değerlendirilebilmelidir. İfadelerin statüsünün açıklığı ikinci unsurdur; gözlem, kaynak iddiası, varsayım, norm ve hedef ayrıldığında anlaşmazlığın nereden kaynaklandığı incelenebilir. Hesaplama doğruluğu ve kabul edilebilir maliyet de birlikte ele alınır. Sonucun belirlenemediği durumun doğru bildirilmesi, başarı değerlendirmesinin bir parçasıdır.

Kaynak, gerekçe ve değişim takibi, sonucun sürdürülebilir biçimde kullanılmasını destekler. Bir kayıt veya kural düzeltildiğinde ona bağlı sonuçlar incelenebilmeli; geçmişteki kararın hangi bilgi ve kurallarla üretildiği gerektiğinde yeniden kurulabilmelidir. Açıklık, itiraz ve düzeltme imkânını da içerir. Yanlış kavram eşleştirmesi, eksik istisna veya güncelliğini yitirmiş kural belirlendiğinde uygun bir düzeltme yolu bulunması, sistemin kullanılabilirliğinin parçasıdır.

Daha çok veri, daha büyük ontoloji veya daha uzun kural listesi tek başına bu gayeyi gerçekleştirmez. Göreve uygunluk, kaynakların niteliği ve bakım imkânı önemlidir. Biçimsel ispat kendi varsayımlarının dışındaki dünyayı otomatik doğrulamaz. Akıcı açıklama da gerçek çıkarım dayanaklarının yerini tutmaz. Bütün kararları otomatikleştirmek veya insanı her görevden çıkarmak alanın zorunlu amacı olarak kaydedilmez; bazı işlerde yararlı çıktı eksik bilgiyi veya inceleme gereğini göstermektir.

Tek ve evrensel bir dünya modeli kurmak da zorunlu bir son amaç değildir. Aynı cihaz, satın alma, bakım ve kullanım yetkisi görevlerinde farklı ayrıntılarla temsil edilebilir. Gaye Protokolü, hangi anlayışın hangi görev için benimsendiğini ve sonuçların ne zaman yeniden ele alınacağını açık tutar. Başarı, sistemin hangi sonucu hangi dayanaklarla kabul ettiğini, bu kabulün nerede ve ne zaman kullanılabileceğini ve hangi değişiklikler karşısında yeniden değerlendirilmesi gerektiğini gösterebilmesiyle değerlendirilir.

~~~text
  DESTEKLEYENLER
    goreve uygun kapsam
    ifadelerin statusunun acikligi
    hesaplama dogrulugu ve kabul edilebilir maliyet
    sonucun belirlenemedigi durumun dogru bildirilmesi
    kaynak, gerekce ve degisim takibi
    itiraz ve duzeltme imkani

  TEK BASINA YETMEZ
    daha cok veri . daha buyuk ontoloji . daha uzun kural listesi
    bicimsel ispat  -/->  kendi varsayimlarinin disindaki dunyanin
                          dogrulanmasi
    akici aciklama  =/=  gercek cikarim dayanaklari

  ZORUNLU AMAC DEGIL
    butun kararlari otomatiklestirmek . insani her gorevden cikarmak
    tek ve evrensel bir dunya modeli
    ayni cihaz:  satin alma | bakim | kullanim yetkisi gorevlerinde
    farkli ayrintilarla temsil edilebilir
    bazi islerde yararli cikti:  eksik bilgiyi veya inceleme geregini
    gostermek
~~~

*Çizim 19 — Gaye: destekleyenler; tek başına yetmeyenler; zorunlu olmayan amaçlar.*

### Uygulama girdisi

Başlangıç yönelimi, beklenen kullanım, yapılan değerlendirmeler, elde edilen çıktılar ve sınırlamalar.

### Masaüstünde uygulama

1. Çalışmanın desteklemesi beklenen işi ve bundan beklenen yararı bir paragrafta yaz. Teknik çıktıyı ve bu çıktının hizmet edeceği insani veya kurumsal amacı ayrı ifade et.

2. Hedefi belirleyen, teknik değerlendirmeyi yürüten ve sonucu kullanacak tarafları belirt. Sistem tarafından seçilen bir alt hedef varsa hangi üst hedefe bağlı olduğunu kaydet.

3. Başarıyı üç yönden değerlendir: çıkarım belirtilen anlam ve kurallara uygun mu; temsil görev için gerekli ayrımları kapsıyor mu; elde edilen çıktı amaçlanan işe hizmet ediyor mu? Her birine ayrı cevap ver.

4. Her değerlendirmeyi mevcut dayanağa bağla. Sayısal ölçüt veya eşik kullanılacaksa nereden geldiğini ve neden uygun olduğunu açıkla; henüz belirlenmemiş ölçütleri açık soru olarak kaydet.

5. Gerçekleşen kazanımı, henüz gösterilememiş yararı ve açık kalan sınırlamaları ayrı yaz. Sonucun eksik bilgiyi veya inceleme ihtiyacını göstermesi de görev açısından yararlıysa bu katkıyı belirt.

### Beklenen kayıt

Teknik çıktı, kullanım amacı, hedef ve değerlendirme rolleri, üç ayrı başarı değerlendirmesi, dayanakları, gerçekleşen kazanım ve açık kalan sınırlamalar. Bunlar çalışma kaydının 5. bölümünde tutulur.

### Tamamlanma ve geri dönüş

**Tamamlanma:** Yapılan iş ile amaç arasındaki ilişki açıklanabiliyor ve başarı iddiası eldeki dayanağın kapsamıyla sınırlı kalıyorsa Kökleşme kaydına geçilir. Hedefin karşılanma durumu ayrıca yazılır.

**Geri dönüş:** Sorun hedefin seçilmesindeyse Tohum'a; temsilin kapsamındaysa Varlık'a; işlemin yürütülmesindeyse Usül'e dön. Yeni kullanım amacı, bağlam ve zaman koşullarını da etkiliyorsa ilgili kayıtları güncelle.

## 6 Kökleşme (Bitiş) Protokolü

> Başlangıç sorusuna hangi cevaplarla ulaştık; bu cevaplar hangi dayanaklarla, hangi sınırlar içinde ve hangi yeniden değerlendirme koşullarıyla kullanılabilir?

### Anlamı ve sınırları

Kökleşme Protokolü, 1–5 arasındaki protokollerde geliştirilen anlayışı başlangıç sorusuyla yeniden ilişkilendirir. Çalışmanın hangi sonuçlara ulaştığını, bu sonuçların birbirini nasıl desteklediğini ve hangi meselelerin açık kaldığını kaydeder. Kökleşme, kavramların dayanaklarıyla, geçerlilik koşullarıyla ve kullanım amacıyla bağlantısının görünür olmasıdır. Ortaya çıkan kayıt böylece daha sonra okunabilecek, değerlendirilebilecek ve gerektiğinde düzeltilebilecek bir bütün hâline gelir.

Bu aşamada beş protokol arasındaki uyum incelenir. Varlık Protokolü'nde tanımlanan şeyin Mekan Protokolü'nde belirlenen bağlamda ele alınıp alınmadığı değerlendirilir. Usül Protokolü'nün işlemlerinin bu tanım ve bağlama uygunluğu, Zaman Protokolü'nün geçerlilik ve değişim koşullarını karşılayıp karşılamadığı ve bütün çalışmanın Gaye Protokolü'nde belirtilen kullanıma ne ölçüde hizmet ettiği açıklanır. Bir kabul başka bir bölümde farklı anlamda kullanılmışsa uyuşmazlık ve etkisi kaydedilir.

Taşıyıcı sorusunun cevabı burada birleştirilir. Anlamı değerlendiren, kaynağı sağlayan, kuralı belirleyen, çıkarımı gerçekleştiren ve sonucu kullanan roller birlikte görünür kılınır. Bir işlevin teknik sistem tarafından yürütülmesi, diğer rollerin de aynı sistemde toplandığı şeklinde yorumlanmaz. Çalışma kavramsal bir taslak üretmişse bu durum kaydedilir; gerçekleştirilmiş uygulamalar, tasarlanmış işlemler ve henüz sınanmamış davranışlar kendi statüleriyle açıklanır.

Sonuçlar çıkarım doğruluğu, temsil yeterliliği ve amaç uygunluğu bakımından, mevcut dayanağın sınırları içinde değerlendirilir. Bir örnekte elde edilen sonuç incelenmeyen bütün durumlara genellenmez. Eksik dayanak, çözülmemiş çelişki ve henüz belirlenememiş sonuç görünür kalır. Açık meselelerin kaydedilmesi, çalışmanın sağladığı kazanımı ve sonraki çalışmanın başlangıcını belirler.

Bitiş, bu çalışma çevriminin sonucunu ve sürümünü kayda geçirmektir. Tamamlanan kayıt, kaynakları ve değişiklik geçmişiyle birlikte saklanır. Sonuçların hangi bağlamda kullanılabileceği ve hangi değişikliklerin yeniden değerlendirme gerektireceği belirtilir. Kökleşmiş bir anlayışın sürekliliği, kabul gerekçelerinin izlenmesine ve gerektiğinde ilgili protokole dönülebilmesine dayanır. Gaye ulaşılmak isteneni ve başarı ölçütünü açıklar; Kökleşme elde edilen sonucu, sınırlarını ve sonraki kullanım koşullarını bir araya getirir.

~~~text
  BES PROTOKOLUN UYUMU
    Varlik'ta tanimlanan sey      Mekan'da belirlenen baglamda mi ele
                                  alindi?
    Usul'un islemleri             bu tanim ve baglama uygun mu?
    Zaman'in kosullari            gecerlilik ve degisim kosullari
                                  karsilandi mi?
    butun calisma                 Gaye'de belirtilen kullanima ne
                                  olcude hizmet ediyor?
    bir kabul baska bolumde farkli anlamda kullanilmissa  -->
    uyusmazlik ve etkisi kaydedilir

  ROLLER BIRLIKTE GORUNUR
    anlami degerlendiren . kaynagi saglayan . kurali belirleyen .
    cikarimi gerceklestiren . sonucu kullanan
    bir islevin teknik sistemce yurutulmesi  -/->  diger rollerin de
    ayni sistemde toplanmasi
    ayri statuler:  gerceklestirilmis uygulama | tasarlanmis islem |
    henuz sinanmamis davranis

  GAYE VE KOKLESME
    Gaye        ulasilmak isteneni ve basari olcutunu aciklar
    Koklesme    elde edilen sonucu, sinirlarini ve sonraki kullanim
                kosullarini bir araya getirir
    bir ornekte elde edilen sonuc  -/->  incelenmeyen butun durumlar
~~~

*Çizim 20 — Kökleşme: beş protokolün uyumu; roller; Gaye ve Kökleşme.*

### Uygulama girdisi

Tohum kaydı, 1–5 protokollerinin çalışma kayıtları, dayanaklar, örnek sonuçlar, açık meseleler ve değişiklik geçmişi.

### Masaüstünde uygulama

1. Başlangıç sorusunu yeniden oku. Çalışmanın bu soruya verdiği cevabı, elde edilen kazanımı ve henüz karşılanmayan beklentiyi ayrı paragraflarda yaz.

2. 1–5 kayıtlarını birlikte incele. Kavram, kaynak, kural, bağlam ve zaman ifadelerinin bölümler arasında uyumunu değerlendir. Uyuşmazlık varsa ilgili bölümü ve etkilenen sonucu belirt.

3. Her temel sonucu onu destekleyen kayda veya kaynağa bağla. Gerçekleştirilmiş işlem, elle yapılmış örnek değerlendirme, araç çıktısı ve henüz sınanmamış önerinin statüsünü koru.

4. Gaye bölümündeki çıkarım doğruluğu, temsil yeterliliği ve amaç uygunluğu değerlendirmelerini birlikte gözden geçir. Eksik bilgi, çelişki veya tamamlanamayan hesap varsa sonuç üzerindeki etkisini açıkla.

5. Açık meseleleri, kullanım sınırlarını ve yeniden değerlendirme koşullarını yaz. Her açık mesele için dönülecek protokolü ve ihtiyaç duyulan yeni dayanağı belirt. Taşıyıcının kim veya ne olduğu sorusunu roller ve düzeyler üzerinden bir paragrafta cevapla.

6. Kapanış tarihini, çalışma kaydı sürümünü ve sonuç durumunu kaydet. Dosya ve kaynak bağlantılarını kontrol et. Bu çevrimin kaydını tarih ve sürüm içeren ayrı bir dosya adıyla sakla; sonraki çevrimde önceki kapanışa referans ver.

### Beklenen kayıt

Başlangıç sorusuna cevap, temel sonuçlar ve dayanakları, protokoller arası uyum veya uyuşmazlıklar, taşıyıcıların bütünlüklü açıklaması, açık meseleler, kullanım sınırları, geri dönüş koşulları ve kapanış sürümü. Bunlar çalışma kaydının 6. bölümünde tutulur.

### Tamamlanma ve geri dönüş

**Tamamlanma:** Çalışmanın durumu gerçeğe uygun kaydedildiğinde, temel sonuçların dayanak ve sınırları izlenebildiğinde, açık meselelerin etkisi ve ele alınacağı yer belirtildiğinde kapanış kaydı tamamlanır. Kayıt tamamlanması ile teknik hedefin karşılanma durumu ayrı alanlarda tutulur; sonuç kısmi veya belirsiz de olabilir.

**Geri dönüş:** Yeni dayanak mevcut sonucu değiştirdiğinde, kullanım bağlamı genişlediğinde, geçerlilik koşulu sona erdiğinde, kural değiştiğinde veya hedeflenen yarar yeniden tanımlandığında ilgili protokole dön. Önceki kapanışı koru; yeni sürümde neyin hangi gerekçeyle değiştiğini ve bağımlı sonuçlara etkisini yaz.

## Özgün sorular ve belgeleme talepleri

### Birinci soru dizisi

> Geçmiş bağlamları buraya taşıma. Burası ile sınırlı kalma.

> Bilgi Temsili ve Sembolik Akıl Yürütme Mühendisliği

> Nedir? Onu o yapan nelerdir? Neler değildir?

> Nerededir? Bu yeri, oraya has bir yer yapan nelerdir? Neler değildir?

> Nasıl işler yapar? Bu yaptıklarını, ona has yapan nelerdir? Neler değildir?

> Hangi andadır? Bu anı, diğer zamanlardan farklı yapan nelerdir? Neler değildir?

> Hangi nihai amaca hizmet eder? Bu nihai amaca ulaştıran nelerdir? Neler değildir?

### İkinci soru

> Bilgi Temsili ve Sembolik Akıl Yürütme Mühendisliği’nin; köken aldığı varlık, mekan, usül, zaman, ve gayeyi taşıyan makine kimdir? Kim değildir?

### Protokol bölümleriyle belgeleme talebi

> Bu soruları ve yanıtları kayıt altına alarak belgele. Önce mevcut soru-yanıtlarla 1-5 arası protokol bölümlerini paragraf-ağırlıklı oluştur. Sonrasında 0 ve 6'ncı bölüm başlıklarından ne anladığını buraya aktar.

> 0 Tohum (Başlangıç)
>
> 1 Varlık Protokolü
>
> 2 Mekan Protokolü
>
> 3 Usül Protokolü
>
> 4 Zaman Protokolü
>
> 5 Gaye Protokolü
>
> 6 Kökleşme (Bitiş)

### Son sürüm ve Markdown talebi

> 0'ı Tohum (Başlangıç) protokolü, 6'yı Kökleşme (Bitiş) protokolüne dönüştür.
>
> Belgenin son halini oluştur ve masaüstünde gerçekleştirmeye uygun protokollere `.md` formatında indirmeye hazır hale getir.

### Yanıtların kayıttaki yeri

İlk soru dizisinin yanıtları 1–5 bölümlerinin kavramsal metnindedir. Taşıyıcıya ilişkin ikinci sorunun yanıtları da aynı bölümlerdedir. 0 ve 6, bu taleplerin karşılığı olarak uygulama girdisi, adımları, çıktısı ve tamamlanma koşulları olan protokollerdir. Masaüstü uygulama adımları ve çalışma kaydı şablonu, bu talep için kurulmuş çalışma düzenidir. Soruların sözleri aynen yer alır; biçimleri Markdown düzenine göredir.

## Kaynaklar

Metindeki numaralı göndermeler aşağıdaki kaynaklara karşılık gelir. Bunlar kavramsal açıklamaların kaynaklarıdır; belirli bir masaüstü uygulamasının gerçekleştirildiğini gösteren işlem kayıtları değildir. Uygulamaya özgü dayanaklar çalışma kaydının Dayanak Dizini bölümüne yazılır.

**[1]** KR 2026 (https://kr.org/KR2026/) — 23rd International Conference on Principles of Knowledge Representation and Reasoning. Alanın tanımı, kapsamı ve 2026 konferans izleri.

**[2]** RDF 1.1 Semantics (https://www.w3.org/TR/rdf11-mt/) — W3C Recommendation, 2014. Biçimsel anlam ve mantıksal gerektirme.

**[3]** What Is a Knowledge Representation (https://courses.csail.mit.edu/6.803/pdf/davis.pdf) — Randall Davis, Howard Shrobe ve Peter Szolovits, 1993. AI Magazine 14(1). Temsilin işlevleri ve modelin sınırları.

**[4]** The Knowledge Level (https://iiif.library.cmu.edu/file/Newell_box00052_fld04340_doc0003/Newell_box00052_fld04340_doc0003.pdf) — Allen Newell, 1981. AI Magazine. Bilgi düzeyi ve sembol düzeyi ayrımı. Adres, CMU arşivindeki ilk altı sayfayı gösterir.

**[5]** Computer Science as Empirical Inquiry Symbols and Search (https://web.cs.wpi.edu/~nth/cs534/papers_worth_reading/Computer_Science_as_Empirical_Inquiry.htm) — Allen Newell ve Herbert A. Simon, 1976. Communications of the ACM 19(3). Fiziksel sembol sistemi ve hipotezin niteliği.

**[6]** SPARQL 1.1 Entailment Regimes (https://www.w3.org/TR/sparql11-entailment/) — W3C Recommendation, 2013. Çıkarım ilişkileriyle sorgulama.

**[7]** Augmenting Human Intellect A Conceptual Framework (https://www.dougengelbart.org/pubs/augment-3906.html) — Douglas C. Engelbart, 1962. İnsan, dil, araç, yöntem ve eğitim birlikteliği.

**[8]** The Symbol Grounding Problem (https://www.southampton.ac.uk/~harnad/Papers/Harnad/harnad90.sgproblem.html) — Stevan Harnad, 1990. Physica D 42. Sembollerin dünyayla ve anlamla bağlantısı üzerine tartışma.

**[9]** Methodology for the Design and Evaluation of Ontologies (https://www.eil.utoronto.ca/wp-content/uploads/enterprise-modelling/papers/gruninger-ijcai95.pdf) — Michael Grüninger ve Mark S. Fox, 1995. Yeterlik sorularıyla ontoloji kapsamı ve değerlendirme.

**[10]** OWL 2 Web Ontology Language Primer (https://www.w3.org/TR/2012/REC-owl2-primer-20121211/) — W3C Recommendation, ikinci baskı, 2012. Temsil, çıkarım ve açık dünya kabulü.

**[11]** A Logic for Default Reasoning (https://www.cs.ubc.ca/tr/1979/tr-79-08) — Raymond Reiter, 1979. UBC teknik raporu TR-79-08. Varsayılan kabuller ve yeni bilgiyle revizyon.

**[12]** OWL 2 Web Ontology Language Profiles (https://www.w3.org/TR/owl2-profiles/) — W3C Recommendation, ikinci baskı, 2012. İfade gücü ve hesaplama maliyeti tercihleri.

**[13]** SMT LIB About SMT (https://smt-lib.org/about.shtml) — SMT-LIB. Belirli kuramlar altında sağlanabilirlik probleminin açıklaması.

**[14]** Formal Methods in Answer Set Programming (https://www.cs.utexas.edu/~vl/ecai-tutorial/) — Vladimir Lifschitz, ECAI 2024 öğreticisi. ASP ile problem ve çözüm modelleri.

**[15]** Shapes Constraint Language SHACL (https://www.w3.org/TR/2017/REC-shacl-20170720/) — W3C Recommendation, 2017. Veri grafiklerinin koşullara göre doğrulanması.

**[16]** PROV Overview (https://www.w3.org/TR/prov-overview/) — W3C Working Group Note, 2013. Veri oluşumu, kaynaklar, faaliyetler ve sorumlular.

**[17]** Programs with Common Sense (https://www-formal.stanford.edu/jmc/mcc59/node1.html) — John McCarthy, 1959. Giriş bölümü. Biçimsel bildirimlerden sonuç çıkaran sistem yaklaşımı.

**[18]** AlphaGeometry An Olympiad level AI system for geometry (https://deepmind.google/blog/alphageometry-an-olympiad-level-ai-system-for-geometry/) — Google DeepMind, 2024. Dil modeli önerileri ile sembolik çıkarımın birlikte çalışması.

**[19]** Constraint Based Analysis of Reasoning Shortcuts in Neurosymbolic Learning (https://proceedings.kr.org/2026/106/) — Akihiro Takemura, Katsumi Inoue ve Masaaki Nishino, KR 2026. Öğrenilen kavramların hedeflenen anlamlarla eşleşmesi sorunu.

**[20]** A Truth Maintenance System (https://dspace.mit.edu/entities/publication/5377b306-4ecc-4687-b1f5-78cbb4a0543a) — Jon Doyle, 1979. MIT AI Memo 521. Kabullerin gerekçeleri ve değişimle yeniden değerlendirme.

**[21]** A Taxonomy of Time in Databases (https://www2.cs.arizona.edu/~rts/pubs/SIGMOD85.pdf) — Richard Snodgrass ve Ilsoo Ahn, 1985. Geçerlilik zamanı ve kayıt zamanı ayrımı.

## Çalışma kaydı şablonu

Aşağıdaki şablonu `CALISMA_KAYDI.md` adıyla ayrı bir dosyaya kopyalayarak doldur.

```markdown
# Çalışma Kaydı

Bu şablonu seçtiğin konu için doldur. Alanları mümkün olduğunca kısa ve bağlantılı paragraflarla açıkla. Bir alanı henüz incelemediysen bunu belirt; bilinmeyen bilgiye değer atama. Kullanılmayan alanı gerekçesiyle “bu çalışma için uygulanmaz” olarak işaretle. Örnek satırlar kayıt biçimini gösterir; yapılmış işlem veya doğrulanmış bulgu sayılmaz.

**Çalışma adı:** Henüz belirlenmedi.

**Çalışma konusu:** Henüz belirlenmedi.

**Protokol sürümü:** 1.0

**Çalışma kaydı sürümü:** Henüz belirlenmedi.

**Başlangıç tarihi ve gerekiyorsa saat dilimi:** Henüz belirlenmedi.

**Çalışmayı yürüten kişi veya sistem ve katkı rolleri:** Henüz belirlenmedi.

**Önceki çalışma kaydı:** İlk çalışma ise “ilk çevrim”; devam ise önceki dosya adı ve ilgili sonuç.

**Kayıt durumu:** Henüz başlanmadı.

**Hedefin karşılanma durumu:** Henüz değerlendirilmedi.

## 0 Tohum (Başlangıç) Protokolü Kaydı

**Özgün soru:** Soruyu kendi ifadesiyle kaydet.

**Sınırlandırılmış çalışma sorusu ve yönelim:** Bu çevrimde neyi anlamak veya gerçekleştirmek istediğini ve özgün soruyla ilişkisini yaz.

**Kapsam ve kapsam dışı:** İncelenecek konu, kullanım, örnek ve dışarıda kalanları açıkla.

**Beklenen çıktı:** Çevrim sonunda ortaya çıkmasını beklediğin gözlenebilir kaydı veya sonucu belirt.

**Başlangıç dayanakları, varsayımlar ve açık sorular:** Her birine kısa bir ad ver; birbirine karıştırmadan açıkla. Kaynağı bilinmeyen ifadeyi doğrulanmış dayanak olarak işaretleme.

**İlk taşıyıcı ve rol kaydı:** Katkı sağlayan, değerlendiren, işlemi yürüten ve sonucu kullanacak kişi veya sistemleri belirt.

**Kayıt durumu ve gerekçesi:** Henüz başlanmadı.

## 1 Varlık Protokolü Kaydı

**Konu tanımı:** İncelenen şeyi, onu kendisi yapan özellikleri ve kapsam dışında kalanları bir paragrafta tanımla.

**Temel kavramlar:** Her kavram için tanım, örnek ve karıştırılabileceği yakın kavramla farkını yaz.

**Bilgi statüleri:** Kullanılan ifadelerin gözlem, kaynak iddiası, varsayım, norm veya hedef oluşunu belirt; ilgili dayanağa bağla.

**Taşıyıcılar:** Anlamı ve amacı değerlendiren insan veya kurumları, işlevsel sistemi ve fiziksel yürütücüyü ayrı açıkla. Bir sistem ajan olarak adlandırılıyorsa amaç–eylem ilişkisini belirt.

**Açık kimlik soruları ve temsil sınırları:** Sonucu değiştirebilecek kavram belirsizliklerini ve temsil edilmeyen durumları kaydet.

**Kayıt durumu ve gerekçesi:** Henüz başlanmadı.

## 2 Mekan Protokolü Kaydı

**Kaynak, kural ve kullanım bağlamları:** Verinin geldiği yeri, kuralın geçerli olduğu alanı ve sonucun kullanılacağı ortamı ayrı açıkla.

**Kaynak konumları:** Dosya adı, göreli yol veya bağlantı ile gerçekten incelenen bölüm ve sürümü kaydet. Yalnız erişilebilmiş kaynakları ayrıca belirt.

**Dünya–temsil eşleştirmesi:** Hangi kayıt hangi nesne, olay veya durumu gösteriyor; bu eşleştirmeyi ne destekliyor?

**İşlevsel yol ve roller:** Kaynaktan temsile, değerlendirmeye ve kullanıma geçişi ve bu geçişteki görevleri açıkla.

**Bağlam sınırları:** Başka bir ortama taşınırken yeniden ele alınması gereken kabul veya kuralı belirt.

**Kayıt durumu ve gerekçesi:** Henüz başlanmadı.

## 3 Usül Protokolü Kaydı

**İşlem türü ve beklenen sonuç:** Yapılacak değerlendirmeyi ve üreteceği sonuç türünü yaz.

**Yürütme biçimi:** Elle değerlendirme veya kullanılan mevcut araç, sürüm ve ilgili yapılandırma.

**Temsil ve çıkarım çerçevesi:** Kullanılan dil, mantık veya elle değerlendirmedeki anlam ve çıkarım kabullerini belirt.

**Eksik bilgi kabulleri:** Açık veya kapalı dünya kabulü, kapsamı ve varsa tamlık varsayımı.

**Çelişkiyi ele alma ilkesi:** Çelişkinin kapsamını, sonuçlara etkisini ve varsa uygulanan çözümün yöntemini ve gerekçesini yaz. Henüz çözüm uygulanmadıysa bunu belirt.

**Kurallar:** Her kuralın ifadesini, kaynağını veya varsayım statüsünü ve koşulun yeterli/gerekli oluşunu belirt.

**Değerlendirilen soru ve girdiler:** Somut örneği ve kullanılan dayanakları yaz.

**İşlem izi:** Aşağıdaki satırı çoğalt veya aynı bilgileri paragraflarla açıkla.

| Adım | Dayanak ve kural | Yapılan işlem | Elde edilen sonuç |
| --- | --- | --- | --- |
| Henüz uygulanmadı | Henüz seçilmedi | Henüz yürütülmedi | Henüz sonuç yok |

**Sonucun bilgi durumu ve gerekçesi:** Desteklenen olumlu sonuç, desteklenen olumsuz sonuç, bilinmeyen veya çelişkili. Henüz değerlendirme yapılmadıysa “henüz incelenmedi” yaz.

**Hesaplamanın veya incelemenin durumu:** Başlanmadı, tamamlandı veya tamamlanamadı; son durumda nedeni ve varsa elde edilen kısmi sonuç.

**Sınır durumu:** Bir dayanak eksildiğinde, koşul değiştiğinde veya kaynak çeliştiğinde ne değişiyor? Yapılan incelemeyi ve etkisini kaydet.

**Kayıt durumu ve gerekçesi:** Henüz başlanmadı.

## 4 Zaman Protokolü Kaydı

**Kullanılan tarihler ve sürümler:** Kaynak, model, kural ve inceleme sürümlerini belirt.

**Zaman ayrımları:** Görev için gerekli olay zamanı, geçerlilik aralığı, kayıt zamanı, karar zamanı ve eylem zamanını ayrı yaz. Bilinmeyen veya uygulanmayan türlerin nedenini belirt.

**Geçerlilik sınırı:** Başlangıç ve bitiş koşulları, sınır anının dâhil olup olmadığı ve gerekiyorsa saat dilimi.

**Değişim ve bağımlı sonuçlar:** Bir kayıt veya kural değişirse hangi sonuç yeniden değerlendirilecek? Önceki ve yeni değerlendirmeyi hangi dayanak ayırıyor?

**Yeniden inceleme koşulu:** Somut değişiklik, süre sonu veya gerekçeli inceleme tarihi.

**Kayıt durumu ve gerekçesi:** Henüz başlanmadı.

## 5 Gaye Protokolü Kaydı

**Teknik çıktı ve kullanım amacı:** Ortaya çıkan şey ile ondan beklenen insani veya kurumsal yararı ayrı açıkla.

**Amaç ve değerlendirme rolleri:** Hedefi kim belirliyor, işlemi kim veya ne yürütüyor, sonucu kim kullanıp değerlendiriyor?

**Çıkarım doğruluğu:** Kullanılan anlam ve kurallar bakımından değerlendirme ve dayanağı.

**Temsil yeterliliği:** Görev için gerekli ayrımların kapsanması bakımından değerlendirme ve dayanağı.

**Amaç uygunluğu:** Çıktının beklenen işe hizmet etmesi bakımından değerlendirme ve dayanağı.

**Gerçekleşen kazanım, henüz gösterilmemiş yarar ve sınırlamalar:** Bunları birbirinden ayrı yaz; varsa başarı ölçütünün seçilme nedenini belirt.

**Kayıt durumu ve gerekçesi:** Henüz başlanmadı.

## 6 Kökleşme (Bitiş) Protokolü Kaydı

**Başlangıç sorusuna cevap:** Sonuçları bir araya getiren, kapsamı belirli bir cevap yaz.

**Temel sonuçlar ve dayanakları:** Her sonuç için ilgili kayıt, kaynak, kural veya örneğe geri gidilebilsin.

**Protokoller arası uyum veya uyuşmazlık:** Kavram, bağlam, usul, zaman ve gaye arasında saptanan ilişkiyi ve varsa uyuşmazlığın etkisini açıkla.

**Taşıyıcıların bütünlüklü açıklaması:** Varlığı, mekânı, usulü, zamanı ve gayeyi hangi kişi, kurum, sistem ve fiziksel düzenek hangi işlevle taşıyor? Hangi özdeşleştirmeler yapılmamalı?

**Gerçekleştirilenler ve tasarlananlar:** Yapılmış işlem, örnek değerlendirme, araç çıktısı ve henüz sınanmamış öneriyi ayrı yaz.

**Açık meseleler ve dönüş noktaları:** Her mesele için etkisini, ihtiyaç duyulan yeni dayanağı ve dönülecek protokolü belirt.

**Kullanım sınırları ve yeniden değerlendirme koşulları:** Sonuç nerede, ne zaman ve hangi varsayımlarla kullanılabilir?

**Hedefin karşılanma durumu ve gerekçesi:** Karşılandı, kısmen karşılandı, karşılanmadı veya henüz belirlenemedi. Henüz değerlendirme yapılmadıysa bunu yaz.

**Kapanış kaydı durumu:** Henüz kapanış yapılmadı.

**Kapanış tarihi, sürümü ve saklanan dosya adı:** Henüz belirlenmedi.

## Dayanak Dizini

Bu bölüm çalışma sırasında gerçekten kullanılan kaynakların dizinidir. Protokol belgesinin akademik kaynakçası ile uygulamaya ait dayanaklar farklı işlevler taşır. Yalnız kullandığın dayanakları buraya geçir.

| Kısa ad | Kaynak veya kayıt | Konum / bağlantı | Sürüm / tarih | İncelenen bölüm ve bilgi statüsü |
| --- | --- | --- | --- | --- |
| Henüz atanmadı | Henüz seçilmedi | Henüz belirlenmedi | Henüz belirlenmedi | Henüz incelenmedi |

## Değişiklik Kaydı

Önceki kapanış dosyalarını koru. Bu kayıtta hangi kabulün veya sonucun neden değiştiğini ve yeniden ele alınan protokolleri belirt.

| Tarih ve kayıt sürümü | Değişiklik | Gerekçe ve dayanak | Etkilenen protokol ve sonuç |
| --- | --- | --- | --- |
| Henüz yok | Henüz değişiklik yapılmadı | Uygulanmaz | Uygulanmaz |
```

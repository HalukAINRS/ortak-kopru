# Sınama ve Karşılık Değerlendirmesi

**Masaüstünde uygulanabilir protokoller**

**Sürüm:** 1.0\
**Tarih:** 30 Ekim 2026\
**Kapsam:** 0–6 arasındaki yedi protokol ve doldurulabilir uygulama kaydı

Sınama ve Karşılık Değerlendirmesi, bir şey hakkındaki yargıyı dayanakları ve değişme koşullarıyla birlikte kurmak için kullanılan inceleme çerçevesidir. Sınama, bir iddianın hangi koşullarda geçerli kaldığını, nerede yetersizleştiğini ve hangi bulguyla düzeltilmesi gerektiğini araştırır. Karşılık değerlendirmesi, ortaya çıkan durumun başlangıçtaki tanım, açıklama, ihtiyaç veya gaye bakımından ne ifade ettiğini belirler.

Tohum Protokolü başlangıç sorusunu ve kabulleri kaydeder. Varlık, Mekan, Usül, Zaman ve Gaye protokolleri incelemeyi beş yönden yürütür. Kökleşme Protokolü, oluşan hükümleri başlangıç kaydıyla ilişkilendirir ve bu inceleme turunun sonucunu gerekçesiyle kaydeder. Bu dosya uygulama yönergesini ve boş kayıt şablonunu içerir; belirli bir konuya uygulanmış sonuç kaydı, her kullanımda ayrıca oluşturulur.

Değerlendiriciyi konu alan soru bütün çalışmaya eşlik eder: “Sınama ve Karşılık Değerlendirmesi'nin köken aldığı varlık, mekan, usül, zaman, ve gayeyi taşıyan makine kimdir? Kim değildir?” Bu çerçevede önerilen çalışma adı, kendisi de sınamaya açık değerlendirme failidir. Bu ad belirli bir insanı, yapay zekâyı veya tekil bir özneyi teşhis etmez. Köken, taşıyıcı, işletici ve amaç belirleyicinin aynı varlıkta toplanıp toplanmadığı araştırılır.

## Masaüstü çalışma düzeni

Dosyayı masaüstünde veya tercih ettiğin çalışma konumunda bir klasöre kaydet. Yanında her inceleme için ayrı bir Markdown kayıt dosyası oluştur; örneğin `Uygulama_Kaydi_001.md`. Bu belgenin sonundaki kayıt şablonunu yeni dosyaya kopyala ve bir düz metin ya da Markdown düzenleyicisinde aç. Belirli bir işletim sistemi, ücretli uygulama veya komut satırı kullanılması gerekmez.

Dayanakları dosya adı, göreli yol, erişim adresi veya açık kaynak konumuyla kayıt dosyasına bağla. Bir dosyanın hangi bölümünü kullandığını da belirt. Kaynaklar aynı çalışma klasöründeyse göreli yolları kullanabilirsin; başka yerde duruyorlarsa konumlarını kaydet. İnceleme sırasında üretilen notları veya çıktıları dayanaklarıyla ilişkilendir. Her yeni inceleme turuna ayrı kayıt aç; önceki turun sonucu yeni turun girdisiyse bu ilişkiyi belirt.

Önce 0'ı tamamla, ardından 1–5'i ilk değerlendirme için doldur. 3'te planlanan sınamayı uygulamadan önce 4'teki zaman koşullarını ve 5'teki gaye ile başarı ölçütlerini kaydet. Sonra uygun sınamayı gerçekleştir; gözlenen karşılığı 3'e, gözlem ve olay zamanlarını 4'e, gayeye katkısını 5'e işle. 6'da kayıtları birlikte değerlendir. Numaralandırma tek yönlü ve geri dönülmez bir sıra oluşturmaz; bir bölümde değişen kabul diğerlerini etkiliyorsa ilgili bölümleri gerekçesiyle güncelle.

~~~text
  IKI KAVRAM
    sinama         bir iddianin hangi kosullarda gecerli kaldigini,
                   nerede yetersizlestigini ve hangi bulguyla
                   duzeltilmesi gerektigini arastirir
    karsilik       ortaya cikan durumun baslangictaki tanim, aciklama,
    degerlendir-   ihtiyac ya da gaye bakimindan ne ifade ettigini
    mesi           belirler

  BIR INCELEME TURUNUN SIRASI

    0  --->  1  2  3  4  5       ilk degerlendirme icin doldurulur
                   |
                   |    3'te planlanan sinama uygulanmadan once
                   |      4'e zaman kosullari
                   |      5'e gaye ve basari olcutleri      kaydedilir
                   v
            SINAMA UYGULANIR
                   |
                   |    gozlenen karsilik           --->  3'e
                   |    gozlem ve olay zamanlari    --->  4'e
                   |    gayeye katkisi              --->  5'e
                   v
                   6             kayitlar birlikte degerlendirilir

    numaralandirma tek yonlu ve geri donulmez bir sira olusturmaz
    her yeni inceleme turuna ayri kayit acilir
~~~

*Çizim 1 — Çalışma düzeni: sınama ve karşılık değerlendirmesi; bir inceleme turunun sırası.*

### Ortak kayıt ilkeleri

Her hüküm için bakış açısını, karşılaştırmayı, dayanağı ve hükmü değiştirecek koşulu belirt. Bir şeyi ayırt eden özelliği, işleyişini açıklayan özellikten ve onu değerli kılan özellikten ayır. Gözlemi, yorumu ve varsayımı ayrı yaz. Bir yardımcı yapay zekâdan alınan açıklamayı kullanıyorsan onu yorum veya öneri olarak kaydet; bir kaynakla desteklenen iddia için ilgili kaynağı da göster.

Bir niteliğin bulunmaması, gözlenmemesi ve hakkında henüz bilgi bulunmaması aynı kayıt değildir. Karşılık aranmamışsa veya gerekli kaynağa erişilmemişse bu durumu açıkça belirt. Gerçekleştirilmemiş bir denemeyi sonuçlanmış gibi yazma. Varsayımsal karşılaştırmayı, gerçek uygulamayı ve kaynak üzerinden yapılan incelemeyi kayıt içinde ayır.

İncelemenin durumu ile iddianın durumunu ayrı tut. İnceleme, “Hazırlık”, “Sürüyor”, “Beklemede”, “Tamamlandı” veya “Sonlandırıldı” durumunda olabilir. Bir iddiaya ilişkin hüküm ise “Destekleniyor”, “Belirli koşullarda geçerli”, “Desteklenmiyor” veya “Henüz karar verilemiyor” biçiminde kaydedilebilir. Bir soru bu uygulamaya uygun değilse “Uygulanamaz” kaydını gerekçesiyle kullan. İncelemenin tamamlanması, iddianın desteklendiğini göstermez.

Başlangıç kaydını koru. Sonraki değişiklikleri tarih, değişen kabul ve gerekçe ile değişiklik kaydına ekle. Kaydın eksiksiz görünmesi için bilinmeyenleri tahminle doldurma; bilinmeyeni, neden bilinmediğini ve sonucu nasıl etkilediğini açıkla.

~~~text
  HER HUKUM ICIN BELIRTILIR
    bakis acisi  .  karsilastirma  .  dayanak  .
    hukmu degistirecek kosul

  BIRBIRINDEN AYRILIR
    bir seyi ayirt eden   |   isleyisini aciklayan   |   onu degerli
    ozellik               |   ozellik                |   kilan ozellik

    gozlem  |  yorum  |  varsayim
    yardimci bir yapay zekadan alinan aciklama yorum ya da oneri
    olarak kaydedilir

  AYNI KAYIT DEGILDIR
    bir niteligin bulunmamasi  |  gozlenmemesi  |
    hakkinda henuz bilgi bulunmamasi

    varsayimsal karsilastirma  |  gercek uygulama  |
    kaynak uzerinden yapilan inceleme

  IKI AYRI DURUM

    INCELEMENIN DURUMU             IDDIAYA ILISKIN HUKUM
    Hazirlik                       Destekleniyor
    Suruyor                        Belirli kosullarda gecerli
    Beklemede                      Desteklenmiyor
    Tamamlandi                     Henuz karar verilemiyor
    Sonlandirildi

    incelemenin tamamlanmasi, iddianin desteklendigini gostermez
    bir soru bu uygulamaya uygun degilse "Uygulanamaz" kaydi
    gerekcesiyle kullanilir
~~~

*Çizim 2 — Ortak kayıt ilkeleri: bir hükmün dört öğesi; aynı kayıt olmayanlar; incelemenin durumu ile iddianın hükmü.*

## 0 Tohum (Başlangıç) Protokolü

> Neyle, neden ve hangi başlangıç kabulleriyle bu incelemeye giriyoruz?

Tohum Protokolü, incelemeyi başlatan soruyu ve başlangıç koşullarını kayda geçirir. Başlangıç; bir karşılaşma, ihtiyaç, merak, uyuşmazlık veya açıklanamayan durum olabilir. İncelemenin konusu ilk hâliyle tanımlanır ve neden araştırılmaya değer bulunduğu açıklanır. Bu ilk tarif, sonraki protokollerin değiştirebileceği bir başlangıç kabulüdür.

Başlangıçta bilinenler, varsayılanlar ve henüz bilinmeyenler ayrılır. Kullanılan sözcüklerin geçici anlamları, incelemenin kapsamı ve ilk karşılık beklentisi belirtilir. Beklenti, sonucu baştan belirleyen bir hükme dönüştürülmez. İnceleme sonunda hangi durumun daha açık anlaşılmasının istendiği yazılır; başlangıçtaki gayenin de sınanabileceği korunur.

İncelemeyi başlatan, uygulayan, amaçla ilgili karar veren ve sonuçlarıyla ilişkili olan taraflar belirlenebildiği ölçüde kaydedilir. Roller aynı kişide veya sistemde toplanmak zorunda değildir. Soruyu ortaya koyanla ilk yorumu üreten taraf birbirine karıştırılmaz. Henüz bilinmeyen roller açık bırakılır.

Kullanılacak kaynaklar ve erişilebilen malzeme başlangıç kaydıyla ilişkilendirilir. İncelemenin dışında kalan konular belirtilir. Sonradan edinilen bilgi, başlangıçta da biliniyormuş gibi bu kayda yerleştirilmez; tarihli bir değişiklik olarak eklenir. Tohum, incelemenin hangi soru ve kabullerden doğduğunun izlenebilmesini sağlar.

~~~text
  BASLANGIC NE OLABILIR
    bir karsilasma . ihtiyac . merak . uyusmazlik .
    aciklanamayan durum
    ilk tarif, sonraki protokollerin degistirebilecegi bir baslangic
    kabuludur

  BASLANGICTA AYRILIR
    bilinenler  |  varsayilanlar  |  henuz bilinmeyenler

    beklenti, sonucu bastan belirleyen bir hukme donusturulmez;
    baslangictaki gayenin de sinanabilecegi korunur

  TARAFLAR  ayni kiside ya da sistemde toplanmak zorunda degildir
    incelemeyi baslatan  |  uygulayan  |  amacla ilgili karar veren  |
    sonuclariyla iliskili olan
    soruyu ortaya koyanla ilk yorumu ureten taraf birbirine
    karistirilmaz

  SONRADAN EDINILEN BILGI

      baslangic kaydi                         degisiklik kaydi
      [ o gun bilinenler ]                    [ tarih . degisen kabul .
            |                                   gerekce ]
            |                                        |
    --------*----------------------------------------*------------->
        baslangic                             sonradan edinilen bilgi

    sonradan edinilen bilgi, baslangicta da biliniyormus gibi
    baslangic kaydina yerlestirilmez
~~~

*Çizim 3 — Tohum: başlangıcın türleri; beklenti ve hüküm; taraflar; sonradan edinilen bilginin yeri.*

### Masaüstünde uygulama

1. Kayıt dosyasına çalışma adını, başlangıç tarihini ve değerlendirmeyi uygulayanı yaz. Bu turda incelenecek dosya, fikir, süreç, nesne veya durumu geçici olarak tanımla.
2. Başlangıç sorusunu özgün ifadesiyle kaydet. İncelemeyi başlatan durumu, kapsamı ve kapsam dışında bırakılanları bağlantılı paragraflarla açıkla.
3. Bilinenleri, varsayımları ve açık soruları ayır. İlk karşılık beklentisini, başlangıç gayesini ve önemli sözcüklerin geçici anlamlarını yaz.
4. Dayanakların konumlarını ve ilgili tarafları kaydet. İlk olarak hangi iddianın veya belirsizliğin inceleneceğini belirt; başlangıç kaydını tarihli olarak sakla.

### Kayıt ve geçiş koşulu

Çalışma adı, başlangıç sorusu, geçici konu tarifi, kapsam, bilinenler, varsayımlar, açık sorular, ilk beklenti, gaye, roller ve dayanaklar bu bölümün kaydını oluşturur. Soru, kapsam ve ilk inceleme konusu belirtildiğinde Varlık Protokolü'ne geçilir. Bütün cevapların bulunması gerekmez. Bu başlangıç unsurları henüz belirtilemiyorsa inceleme “Hazırlık” durumunda tutulur ve eksiklik açıklanır.

## 1 Varlık Protokolü

> Nedir? Onu o yapan nelerdir? Neler değildir?

Varlık Protokolü, incelenen şeyin ne tür bir şey olduğunu, aynı türdeki diğer örneklerden nasıl ayrıldığını ve değişim boyunca hangi koşullarda aynı şey olarak kaldığını araştırır. Tür, tekillik ve süreklilik soruları birbirinden ayrılır. Bir okulun ne olduğu, belirli bir okulu diğerlerinden ayıran özellikler ve o okulun değişmesine rağmen aynı okul sayılma koşulları farklı açıklamalar gerektirir.

Tanımlamada kullanılan özelliklerin rolleri belirtilir. Gerekli özellik, bulunmadığında ilgili tanımlamayı yapamayacağımız özelliktir. Yeterli koşul, gerçekleştiğinde bu tanımlamayı yapmamızı sağlayan koşuldur. Ayırt edici özellik, seçilen karşılaştırma içinde fark yaratır. Arızi özellik ise değiştiğinde kimliği veya incelenen temel niteliği değiştirmeyebilir. Gerekli bir özellik bütün örneklerde ortak olabilir; dikkat çekici bir farklılık da kimlik bakımından belirleyici olmayabilir.

Bir şeye has olan, tek bir benzersiz özellikte veya birden fazla özelliğin belirli bir ilişkide bir araya gelmesinde bulunabilir. Özgüllüğün hangi karşılaştırmaya göre belirlendiği açıklanır. Sınama, bir özelliği çıkardığımızda veya değiştirdiğimizde türün, kimliğin, işlevin ya da yalnızca tanıma biçimimizin değişip değişmediğini araştırır. Ayırt edicilikten doğrudan yeterlilik, etkililik veya değerlilik sonucu çıkarılmaz.

“Neler değildir?” sorusu, kolayca karıştırılabilecek yakın örneklerle sınır çizer. Bir ad taşıdığı hâlde tanımlama koşullarını karşılamayan örnekler ve birden fazla sınıflandırmaya yakın duran durumlar incelenir. Etiket, görünüş, ün veya beyanın kimliğin göstergesi sayılması gerekçelendirilir. Bütün olası karşıtları sıralamak yerine, yargıyı yanıltabilecek benzerliklere odaklanılır.

~~~text
  UC AYRI SORU  bir okul uzerinden
    tur          bir okulun ne oldugu
    tekillik     belirli bir okulu digerlerinden ayiran ozellikler
    sureklilik   o okulun degismesine ragmen ayni okul sayilma
                 kosullari

  OZELLIKLERIN ROLLERI
    gerekli         bulunmadiginda ilgili tanimlamayi yapamayacagimiz
                    ozellik
    yeterli kosul   gerceklestiginde bu tanimlamayi yapmamizi saglayan
                    kosul
    ayirt edici     secilen karsilastirma icinde fark yaratan ozellik
    arizi           degistiginde kimligi ya da incelenen temel niteligi
                    degistirmeyebilen ozellik

  SINAMA

    bir ozelligi cikar                 ne degisiyor?
    ya da degistir       --->          tur  |  kimlik  |  islev  |
                                       yalnizca tanima bicimimiz

    ayirt edicilikten dogrudan yeterlilik, etkililik ya da degerlilik
    sonucu cikarilmaz

  "NELER DEGILDIR?"  yargiyi yaniltabilecek benzerliklere odaklanilir
    etiket . gorunus . un . beyan: kimligin gostergesi sayilmasi
    gerekcelendirilir
~~~

*Çizim 4 — Varlık: tür, tekillik ve süreklilik; özelliklerin dört rolü; çıkarma ve değiştirme sınaması.*

Değerlendirmeyi taşıyan makine için önerilen rol adı, kendisi de sınamaya açık değerlendirme failidir. İnsan, bedeni, dili, deneyimleri, ilişkileri ve eylemlerinin sonuçlarıyla bu rolün açık bir taşıyıcısı olarak ele alınabilir. İnsanın araçlarla ve başkalarıyla kurduğu bir düzen de değerlendirmeyi taşıyabilir. Bununla birlikte bir sistemin varlığının, mekânının, usulünün, zamanının ve gayesinin tanımlanması; onun kişi, tek bir irade veya kendi gayesinin kaynağı olduğunu tek başına göstermez.

Köken, taşıyıcı, işletici ve amaç belirleyici ayrılır. Köken, soruların ve ölçütlerin doğduğu kaynaklarla koşulları; taşıyıcı, değerlendirmenin gerçekleşmesini mümkün kılan yapıyı; işletici, karşılaştırmaları gerçekleştiren unsuru; amaç belirleyici ise neyin araştırılacağını ve neye ulaşılacağını belirleyen unsuru ifade eder. Bu roller aynı varlıkta toplanabilir veya farklı kişiler, araçlar ve kurumlar arasında dağılabilir. Ortak sonuç üretilmesi, tek bir özne bulunduğunu kanıtlamaz.

Makine sözcüğü insanın işleyişini araştırmak için kullanıldığında, bu bakışın insanın kimliğini bütünüyle açıkladığı ayrıca savunulmalıdır. Benzer biçimde, bir bileşenin çıktı üretmesi, bütün değerlendirme düzeninin kökeni veya sahibi olduğunu tek başına göstermez. Değerlendirici kendi yeteneklerini, bağımlılıklarını ve sınırlarını da incelemeye açar. Tarihsel kurucu, işlemleri gerçekleştiren unsur ve sonuçlarla yaşayan taraf birbirinin yerine geçirilmez.

Bu bölümün kaydı, kullanılan tanımı ve kapsamını, tanımlamanın dayanaklarını, yakın karşı örnekleri ve kimlik hükmünü değiştirecek koşulları içerir. İncelenen varlıkla değerlendirenin konumu ayrı ayrı belirtilir. Belirli bir kimliğin teşhis edilemediği durumda, rolün açıklanmış olması kimliğin kesinleştiği biçiminde sunulmaz.

~~~text
  DEGERLENDIRMEYI TASIYAN MAKINE ICIN ONERILEN ROL ADI
    kendisi de sinamaya acik degerlendirme faili

  DORT ROL AYRILIR

    .----------------------------.    .----------------------------.
    | KOKEN                      |    | TASIYICI                   |
    | sorularin ve olcutlerin    |    | degerlendirmenin           |
    | dogdugu kaynaklar ve       |    | gerceklesmesini mumkun     |
    | kosullar                   |    | kilan yapi                 |
    `----------------------------'    `----------------------------'
    .----------------------------.    .----------------------------.
    | ISLETICI                   |    | AMAC BELIRLEYICI           |
    | karsilastirmalari          |    | neyin arastirilacagini ve  |
    | gerceklestiren unsur       |    | neye ulasilacagini         |
    |                            |    | belirleyen unsur           |
    `----------------------------'    `----------------------------'

    ayni varlikta toplanabilir ya da farkli kisiler, araclar ve
    kurumlar arasinda dagilabilir
    ortak sonuc uretilmesi, tek bir ozne bulundugunu kanitlamaz

  BIRBIRININ YERINE GECIRILMEZ
    tarihsel kurucu  |  islemleri gerceklestiren unsur  |
    sonuclarla yasayan taraf

    bir bilesenin cikti uretmesi, butun degerlendirme duzeninin kokeni
    ya da sahibi oldugunu tek basina gostermez
    degerlendirici kendi yeteneklerini, bagimliliklarini ve sinirlarini
    da incelemeye acar
~~~

*Çizim 5 — Varlık: değerlendirme faili; köken, taşıyıcı, işletici ve amaç belirleyici.*

### Masaüstünde uygulama

1. Kayıt dosyasının Varlık bölümüne incelenen şeyi bir paragrafla tanımla. Türünü, aynı türdeki örneklerden farkını ve değişim boyunca aynı sayılma koşullarını ayır.
2. Tanımda kullandığın özellikleri gerekli, yeterli, ayırt edici veya arızi oluşları bakımından gerekçelendir. Bu ayrımlardan hangilerinin henüz bilinmediğini belirt.
3. Yakın bir karşı örneği veya sınır durumunu incele. Bir özelliğin değişmesiyle türün, kimliğin, işlevin ya da tanıma biçiminin nasıl etkileneceğini değerlendir; varsayımsal karşılaştırmayı bu adla kaydet.
4. Değerlendirenin köken, taşıyıcı, işletici ve amaç belirleyici rollerini ayır. Tanımı, dayanağı, belirsizlikleri ve tanımı değiştirecek koşulları kayıt dosyasına işle.

### Kayıt ve tamamlanma koşulu

Geçici tanım, özelliklerin rolleri, yakın karşı örnekler ve değerlendiricinin konumu gerekçeleriyle kaydedildiğinde bu bölüm ilk değerlendirme için tamamlanır. Kimliğin kesinleşmesi zorunlu değildir; açıklanamayan bir rol veya sınır açık soru olarak korunur. Tanım değişirse diğer bölümlerde bu tanıma dayanan hükümler gözden geçirilir.

## 2 Mekan Protokolü

> Nerededir? Bu yeri, oraya has bir yer yapan nelerdir? Neler değildir?

Mekan Protokolü, incelenen şeyin hangi yerde bulunduğunu ve bu yerin varlığına, anlamına veya etkisine nasıl katıldığını araştırır. Yer; fiziksel çevredeki konum, bir ilişkiler ağı içindeki konum, kurumsal yetki ve sorumluluk düzenindeki konum veya kavramsal bir sistem içindeki konum anlamında kullanılabilir. Kullanılan anlam ve ölçek belirtilir; farklı yer anlamları arasında fark ettirmeden geçilmez.

Bir yeri özgül kılan koşullar, sınırları ve çevresiyle ilişkileri üzerinden incelenir. Neye yakın veya uzak olduğu, kimlerin erişimine açık bulunduğu, hangi kaynakları ve kısıtları içerdiği, hangi karşılaşmaları mümkün kıldığı araştırılır. Orada bulunmanın başka bir yerde bulunmaya göre neyi değiştirdiği açıklanır. Yer, incelenen faaliyetin gerçekleşmesine katılan bir koşul olarak değerlendirilir.

Başlıca sınama, incelenen nesne veya faaliyetin başka bir yere taşınması durumunda hangi özelliklerin korunacağını ve hangilerinin değişeceğini sorgular. Değişiklik kimlik, erişim, anlam, işlev veya etki bakımından ayrı ayrı ele alınır. Sonuçtaki farkın yerin hangi koşulundan kaynaklandığı araştırılır; taşınmayla birlikte değişen başka koşullar da açıklamada görünür tutulur.

Aynı fiziksel konumda ilişkiler, erişim biçimleri veya kurallar değiştiğinde değerlendirme bakımından aynı yerden söz edilip edilmediği ayrıca incelenir. Bir yerin özgüllüğü, başka hiçbir yerde bulunmayan tek bir özelliğe bağlı olmak zorunda değildir. Koşulların belirli bir birlikteliği, incelenen faaliyet bakımından ayırt edici olabilir. Bu farkın hangi karşılaştırmada ve ne bakımından önemli olduğu belirtilir.

“Neler değildir?” sorusu, yerin işleyişini açıklamayan veya yanlış temsil eden göstergeleri ayırır. Adres, koordinat, kurum adı veya sahiplik bilgisi açıklamanın bir parçası olabilir; bunların yerin özgüllüğünü tek başına açıkladığı varsayılmaz. Bir şeyin belirli bir yerde bulunması da o şeye ait bütün özelliklerin oraya özgü olduğunu göstermez.

Değerlendirici de belirli bir konumdan, ilişkiler içinden ve erişebildiği bilgiyle hüküm verir. Kendi yerinin neyi görmesini sağladığını, neyi görüşünün dışında bıraktığını ve hangi bağımlılıkları oluşturduğunu araştırır. Her yerden bağımsız bir gözlemci gibi konuşuyorsa, bu iddianın dayanağını açıklamalıdır. Değerlendirmeyi taşıyan düzen birden fazla kişi ve araçtan oluştuğunda, bilginin ve yetkinin nerede bulunduğu da belirtilir.

~~~text
  "YER" HANGI ANLAMDA?  kullanilan anlam ve olcek belirtilir
    fiziksel cevredeki konum
    bir iliskiler agi icindeki konum
    kurumsal yetki ve sorumluluk duzenindeki konum
    kavramsal bir sistem icindeki konum
    farkli yer anlamlari arasinda fark ettirmeden gecilmez

  BASLICA SINAMA: BASKA BIR YERE TASINIRSA?

       bir yer                              baska bir yer
     .---------.                            .---------.
     |    o    |    ---- tasinirsa ---->    |    o    |
     `---------'                            `---------'

     hangi ozellikler korunur, hangileri degisir?  ayri ayri ele alinir
        kimlik  |  erisim  |  anlam  |  islev  |  etki

    sonuctaki farkin yerin hangi kosulundan kaynaklandigi arastirilir;
    tasinmayla birlikte degisen baska kosullar da gorunur tutulur

  AYNI KONUM, DEGISEN ILISKILER
    ayni fiziksel konumda iliskiler, erisim bicimleri ya da kurallar
    degistiginde ayni yerden soz edilip edilmedigi ayrica incelenir

  YERIN OZGULLUGUNU TEK BASINA ACIKLADIGI VARSAYILMAZ
    adres . koordinat . kurum adi . sahiplik bilgisi

  DEGERLENDIRICININ YERI
    kendi yeri neyi gormesini sagliyor, neyi gorusunun disinda
    birakiyor, hangi bagimliliklari olusturuyor?
~~~

*Çizim 6 — Mekan: yerin dört anlamı; başka yere taşıma sınaması; değerlendiricinin yeri.*

Bu bölümün kaydı, yerin anlamını ve ölçeğini, sınırlarını, erişim koşullarını, karşılaştırılan yerleri ve yer değişikliğinin beklenen veya gözlenen sonuçlarını içerir. Değerlendiricinin konumu, incelenen yerle ilişkisi içinde açıklanır. Konumun değişmesi hâlinde hangi hükümlerin yeniden ele alınacağı kaydedilir.

### Masaüstünde uygulama

1. İncelenen yerin fiziksel, ilişkisel, kurumsal veya kavramsal anlamını ve ölçeğini kaydet. Dosya konumuyla incelenen şeyin bulunduğu yeri ayrı belirt.
2. Yerin sınırlarını, erişim koşullarını, kaynaklarını, kısıtlarını ve mümkün kıldığı ilişkileri açıkla. Bunların hangilerinin doğrudan gözlendiğini belirt.
3. Başka bir yer veya bağlamla karşılaştır. Yer değişirse kimlik, erişim, anlam, işlev ve etkinin nasıl değişeceğini araştır; gerçek değişiklik yapılmadıysa karşılaştırmanın varsayımsal olduğunu yaz.
4. Kendi gözlem konumunu ve erişemediğin bilgileri kaydet. Yer koşulları değiştiğinde hangi hükümlerin yeniden inceleneceğini belirt.

### Kayıt ve tamamlanma koşulu

Yerin anlamı ve ölçeği, etkili koşulları, karşılaştırma bağlamı ve değerlendiricinin erişimi kaydedildiğinde bu bölüm ilk değerlendirme için tamamlanır. Bilinmeyen yer koşulları açıklanır. Yer değişikliği yapılmadan kurulan karşılaştırma, gerçek sonuç kaydı olarak sunulmaz.

## 3 Usül Protokolü

> Nasıl işler yapar? Bu yaptıklarını, ona has yapan nelerdir? Neler değildir?

Usül Protokolü, ne tür işler yapıldığını, bu işlerin hangi süreçlerle gerçekleştirildiğini ve sonunda ne meydana geldiğini araştırır. Yapabilme kapasitesi, fiilen yapılan iş, işin yapılış biçimi ve ortaya çıkan etki ayrı ayrı değerlendirilir. Bir şeyin belirli bir işi yapmaya elverişli olması, o anda bu işi yaptığını; işi yapması da beklenen sonucu elde ettiğini göstermez.

İşleyişi açıklamak için başlangıç koşulları, devreye giren unsurlar, işlemler veya etkileşimler ve bunların ardından ortaya çıkan değişimler görünür kılınır. Aksama durumları ile işleyişin sürdüğü koşullar birlikte incelenir. Hangi koşul veya işlem değiştiğinde sonucun değiştiği ve sonucu bu işleyişe bağlamayı sağlayan dayanağın ne olduğu araştırılır.

Sonucun ortaya çıkması ile nedeninin belirlenmesi farklıdır. Başka koşulların katkısı ve alternatif açıklamalar değerlendirmeye katılır. Tek bir başarılı uygulama, yeterliliğin hangi koşullarda sürdürülebileceğini açıklamayabilir. Yapılacağı söylenen iş, fiilen yapılan iş, görünür faaliyet ve etkili faaliyet birbirinden ayrılır. İşleyiş açıklaması, başarılı örnekler kadar aksama durumlarını da ele alır.

Bir işe has olan; yapılan işin niteliğinde, yönteminde, bağlama uyarlanışında, süresinde, kaynak kullanımında veya başkaları üzerindeki etkisinde bulunabilir. Özgüllük ile etkililik ayrı değerlendirilir. Alışılmadık bir yöntemin iyi işlediği veya yaygın bir yöntemin yetersiz olduğu sırf bu niteliklerinden çıkarılmaz. Hangi farkın neyi değiştirdiği gösterilir.

Karşılık sözcüğü bu protokolde üç çalışma anlamıyla ele alınır: Bir iddianın incelenen durumla uyuşması, bir eylemin ihtiyaca cevap vermesi ve bir eyleme verilen yanıt. Hangi anlamın kullanıldığı belirtilir. Güçlü veya olumlu tepki, doğruluk ve amaca hizmet etme farklı ölçütlerle incelenir; bunlardan biri diğerinin yerine geçirilmez.

~~~text
  AYRI AYRI DEGERLENDIRILIR
    yapabilme kapasitesi  |  fiilen yapilan is  |
    isin yapilis bicimi  |  ortaya cikan etki

    bir isi yapmaya     -x->   o anda bu isi    -x->   beklenen sonucu
    elverisli olmak            yapmak                  elde etmek
    -x->  gostermez

  ISLEYISI ACIKLAMAK ICIN GORUNUR KILINIR

    baslangic      devreye giren      islemler ya da       ortaya cikan
    kosullari -->  unsurlar      -->  etkilesimler    -->  degisimler

    hangi kosul ya da islem degistiginde sonuc degisiyor?
    sonucun ortaya cikmasi ile nedeninin belirlenmesi farklidir

  BIRBIRINDEN AYRILIR
    yapilacagi soylenen is  |  fiilen yapilan is  |
    gorunur faaliyet  |  etkili faaliyet

  "KARSILIK" SOZCUGUNUN UC CALISMA ANLAMI

    1  bir iddianin incelenen durumla uyusmasi
           iddia   <----- uyusuyor mu? ----->   incelenen durum
    2  bir eylemin ihtiyaca cevap vermesi
           eylem   ---- cevap veriyor mu? ---->   ihtiyac
    3  bir eyleme verilen yanit
           eylem   <--------- yanit ---------

    guclu ya da olumlu tepki  |  dogruluk  |  amaca hizmet etme
    farkli olcutlerle incelenir; biri digerinin yerine gecirilmez
~~~

*Çizim 7 — Usül: kapasite, iş ve etki; işleyişin açıklanması; karşılık sözcüğünün üç anlamı.*

Sınama, başlangıçtaki iddia ile uygun dayanağı ilişkilendirir. Kavramsal bir iddia için tutarlılık ve sınır örnekleri, gözleme bağlı bir iddia için uygun gözlem ve karşılaştırma, değer yargısı için gerekçeler ve sonuçlar incelenebilir. Her sınama deney biçiminde kurulmak zorunda değildir. Kullanılan yolun, incelenen iddiayı neden değerlendirmeye elverişli olduğu açıklanır.

Beklenen karşılığın çıkmaması; iddianın yetersizliğini, koşulların sağlanmadığını, gözlem süresinin kısa kaldığını veya ölçütün incelenen şeyi iyi temsil etmediğini gösterebilir. Bu açıklamalar mümkün olduğunca sınamanın başında görünür tutulur ve sonradan iddiayı her sonuç karşısında koruyacak gerekçelere dönüştürülmez. İtiraz, uyumsuzluk ve beklenmeyen sonuçların hükmü değiştirebilmesine yer bırakılır.

Değerlendirici, ölçüt uygulamayı, ölçütü incelemeyi ve ölçütle gayenin sorumluluğunu üstlenmeyi birbirinden ayırır. Kendi usulünün hükmünü hangi gerekçeyle desteklediğini araştırır. Bir çıktı üretmesi, bütün değerlendirme düzenini kurduğu veya kullandığı ölçütün sahibi olduğu anlamına gelmez. Başkalarından dayanak isteyen değerlendirici kendi yönteminin dayanağını da açıklamaya açar.

Bu bölümün kaydı; iddiayı, ölçütü, karşılaştırmayı, sınama koşullarını, gözlenen karşılığı, alternatif açıklamaları ve değerlendirme sonucunu içerir. Sonuç, destekleniyor, desteklenmiyor, belirli koşullarda geçerli, başka açıklamalara da açık veya henüz karar verilemiyor biçiminde ifade edilebilir. Hangi bulgu veya gerekçe karşısında hükmün değişeceği belirtilir.

~~~text
  SINAMA, IDDIA ILE UYGUN DAYANAGI ILISKILENDIRIR

    kavramsal bir iddia         --->   tutarlilik ve sinir ornekleri
    gozleme bagli bir iddia     --->   uygun gozlem ve karsilastirma
    deger yargisi               --->   gerekceler ve sonuclar

    her sinama deney biciminde kurulmak zorunda degildir

  BEKLENEN KARSILIK CIKMAZSA  neyi gosterebilir?
    iddianin yetersizligini
    kosullarin saglanmadigini
    gozlem suresinin kisa kaldigini
    olcutun incelenen seyi iyi temsil etmedigini

    bu aciklamalar                  sonradan iddiayi her sonuc
    sinamanin BASINDA        -x->   karsisinda koruyacak gerekcelere
    gorunur tutulur                 donusturulmez

    itiraz, uyumsuzluk ve beklenmeyen sonuclarin hukmu
    degistirebilmesine yer birakilir

  DEGERLENDIRICI BIRBIRINDEN AYIRIR
    olcut uygulamak  |  olcutu incelemek  |
    olcutle gayenin sorumlulugunu ustlenmek
    baskalarindan dayanak isteyen degerlendirici kendi yonteminin
    dayanagini da aciklamaya acar

  SONUC NASIL IFADE EDILEBILIR
    destekleniyor  |  desteklenmiyor  |  belirli kosullarda gecerli  |
    baska aciklamalara da acik  |  henuz karar verilemiyor
~~~

*Çizim 8 — Usül: iddianın türüne göre dayanak; beklenen karşılık çıkmazsa; değerlendiricinin üç işi.*

### Masaüstünde uygulama

1. Ne tür iş yapıldığını, yapabilme kapasitesini, fiilî işlemleri ve beklenen etkiyi ayır. Kaynak incelemesi, kavramsal karşılaştırma veya uygulama denemesi biçimlerinden hangisini kullanacağını belirt.
2. Sınanacak iddiayı, karşılık anlamını, yöntemi, karşılaştırmayı ve sonucu nasıl değerlendireceğini önceden kaydet. Uygulamadan önce 4'teki zaman koşullarını ve 5'teki gaye ölçütlerini doldur.
3. Belirlediğin sınamayı uygula. Kullanılan dayanağı, gerçekleştirilen işlemi, gözlenen karşılığı ve aksama durumlarını kaydet. Yapılmayan işlemleri ve beklenen sonuçları gözlenen sonuçlardan ayır.
4. Alternatif açıklamaları ve yöntemin sınırlarını değerlendir. Hükmünü, dayanağını ve değiştirme koşulunu yaz; ölçütü değiştirdiysen gerekçesini değişiklik kaydına ekle.

### Kayıt ve tamamlanma koşulu

Yöntem, koşullar, karşılık türü, dayanak ve değerlendirme sonucu kaydedildiğinde uygulanmış bir sınama için bölüm tamamlanır. Yalnızca plan hazırlanmışsa kayıt “planlandı, uygulanmadı” olarak tutulur. Karşılık bekleniyorsa neyin beklendiği yazılır. Beklenmeyen sonuca rağmen hükmü korumak için eklenen açıklamalar ayrıca gerekçelendirilir.

## 4 Zaman Protokolü

> Hangi andadır? Bu anı, diğer zamanlardan farklı yapan nelerdir? Neler değildir?

Zaman Protokolü, takvim bilgisini ve incelenen şeyin süreç içindeki konumunu birlikte araştırır. Başlangıç, gelişme, olgunlaşma, çözülme veya dönüşüm gibi evreler, kullanılan açıklamanın uygunluğu bakımından incelenebilir. Bir kararın henüz değiştirilebilir olması, uygulanmaya başlaması ve sonuçlarının görünür hâle gelmesi farklı değerlendirme koşulları oluşturabilir.

Olayların sırası, etkilerin ortaya çıkması için gereken süre, müdahale veya karar için kalan süre ve değerlendirme anında erişilebilir olan bilgi birbirinden ayrılır. Aynı ölçütün farklı aşamalarda aynı anlamı taşıdığı varsayılmaz. Hangi anda neyin mümkün, neyin gerçekleşmiş ve neyin artık değiştirilemez olduğu belirtilir.

Bir kararın alındığı anda bilinenlerle sonuçlar ortaya çıktıktan sonra bilinenler birbirine karıştırılmaz. Sonradan edinilen bilgi önceki hükmün düzeltilmesini sağlayabilir; fakat bu bilginin daha önce de erişilebilir olduğu ayrıca gösterilmelidir. Önceki kararı değerlendirmek, karar anındaki bilgi durumunu da incelemeyi gerektirir.

Bir anı diğerlerinden ayıran koşullar, o anda açılan veya kapanan olanaklarla birlikte araştırılır. Başlıca sınama, aynı şey daha önce veya daha sonra gerçekleşseydi anlamının, etkisinin ve değerlendirilişinin nasıl değişeceğini sorar. Zaman farkının neyi değiştirdiği ve bu farkı hangi koşulun açıkladığı belirtilir. Henüz değil, artık değil ve yalnızca bu aşamada hükümleri uygun olduğunda korunur.

“Neler değildir?” sorusu, tarih etiketini zamanın açıklamasıyla ve tek bir görünümü bütün sürecin niteliğiyle karıştırmayı önler. Bir anın yeni olması, onu değerlendirme bakımından önemli kılmaya yetmez. Geçici bir görünümden kalıcı bir nitelik veya tek bir gözlemden bütün sürece ilişkin hüküm çıkarılırken bu geçişin dayanağı açıklanır.

Değerlendirici de belirli bir zamanda, belirli bilgilerle ve değişen koşullar içinde işler. Kendi hükmünün geçerlilik zamanını, hangi yeni bilgi veya olay karşısında yeniden inceleneceğini ve neyin hâlâ değiştirilebilir olduğunu belirtir. Değerlendirmenin yapıldığı an ile değerlendirilen olayın zamanı arasındaki ilişki görünür tutulur.

Bu bölümün kaydı; olayın ve değerlendirmenin zamanını, süreç evresini, bilgi durumunu, gözlem süresini, varsa karar için kalan süreyi ve yeniden değerlendirme koşullarını içerir. Beklenen etkilerle gözlenen etkiler ayrılır. Bir etkinin henüz görülmemiş olması, hiç ortaya çıkmayacağı hükmüyle özdeşleştirilmez.

~~~text
  KARAR ANINDA BILINENLER ILE SONRADAN BILINENLER KARISTIRILMAZ

       kararin alindigi        sonuclarin ortaya         degerlendirme
       an                      cikmasi                   ani
    ------*-----------------------*-------------------------*-------->
       [ karar aninda           [ sonradan edinilen
         erisilebilir bilgi ]     bilgi ]

    sonradan edinilen bilgi onceki hukmun duzeltilmesini saglayabilir;
    fakat bu bilginin daha once de erisilebilir oldugu ayrica
    gosterilmelidir

  BIRBIRINDEN AYRILIR
    olaylarin sirasi
    etkilerin ortaya cikmasi icin gereken sure
    mudahale ya da karar icin kalan sure
    degerlendirme aninda erisilebilir olan bilgi

  BASLICA SINAMA
    ayni sey daha once ya da daha sonra gerceklesseydi anlami, etkisi
    ve degerlendirilisi nasil degisirdi?

    uygun oldugunda korunan hukumler
      "henuz degil"    |    "yalnizca bu asamada"    |    "artik degil"

  OZDESLESTIRILMEZ / KARISTIRILMAZ
    bir etkinin henuz              hic ortaya cikmayacagi hukmu
    gorulmemis olmasi
    tarih etiketi                  zamanin aciklamasi
    tek bir gorunum                butun surecin niteligi
~~~

*Çizim 9 — Zaman: karar anında bilinenler ve sonradan bilinenler; ayrılan dört şey; üç zaman hükmü.*

### Masaüstünde uygulama

1. Olay veya kaynak tarihini, değerlendirme tarihini ve süreçteki evreyi kaydet. Saat önemliyse saati ve saat dilimini belirt; bunları tahmin ederek doldurma.
2. Olayların sırasını, karar anında erişilebilir bilgiyi ve sonradan öğrenilenleri ayır. Gözlem süresini ve varsa karar için kalan süreyi yaz.
3. Aynı durum daha önce veya daha sonra gerçekleşseydi neyin değişeceğini araştır. “Henüz değil”, “artık değil” ve “yalnız bu aşamada” hükümlerinden biri gerekiyorsa dayanağını açıkla.
4. Hükmün geçerlilik zamanını ve yeniden değerlendirmeyi gerektirecek olay veya bilgi değişimini kaydet. Bu koşul ortaya çıkmışsa ilgili protokole dön.

### Kayıt ve tamamlanma koşulu

Zaman bilgileri, süreç evresi, bilgi durumu ve yeniden değerlendirme koşulu belirtildiğinde bu bölüm ilk değerlendirme için tamamlanır. Kesin tarih bilinmiyorsa bilinmediği kaydedilir. Gözlem süresinin henüz yeterli olmadığı durum, sonuç değerlendirmesinin sınırı olarak 3 ve 6'ya aktarılır.

## 5 Gaye Protokolü

> Hangi nihai amaca hizmet eder? Bu nihai amaca ulaştıran nelerdir? Neler değildir?

Gaye Protokolü, incelenen şeyin belirlenebilir bir amacının bulunup bulunmadığını ve varsa bu amacın nasıl kurulduğunu araştırır. Amacın tek, ortak veya nihai olduğu baştan kabul edilmez. Birden fazla amaç, çatışan amaçlar ve belirlenebilir bir amaç bulunmaması açık seçeneklerdir. Bir doğal oluşuma yüklenen kullanım amacının o oluşumun kendisine ait bir amaç sayılması ayrıca gerekçelendirilmelidir.

Beyan edilen amaç, fiilen izlenen amaç, ortaya çıkan etki ve değer verilen sonuç birbirinden ayrılır. Yapılış amacı hakkında ne söylendiği; seçimlerin ve kaynak kullanımının hangi sonuca yöneldiği; gerçekte ne meydana geldiği; meydana gelenlerden hangilerinin hangi gerekçeyle arzu edilir bulunduğu ayrı ayrı incelenir. Bir etki doğması onun amaçlandığını, amaç bildirimi de bütün eylemlerin ona hizmet ettiğini göstermez.

Nihai sözcüğünün hangi kapsamda kullanıldığı açıklanır. Bir sonuç başka bir sonuca ulaşmanın aracıysa gaye araştırması bu ilişkiyi izler. Bunun niçin istendiği sorulduğunda hangi noktanın kendi başına değerli kabul edildiği, bu kabulün kime ait olduğu ve başkalarının aynı sonuca aynı değeri verip vermediği araştırılır. Nihailik iddiası, araştırmayı gerekçesiz biçimde kapatmak için kullanılmaz.

Kimin amacı olduğu, kimin açısından gerçekleşmiş sayılacağı ve hangi bedellerle hangi sınırlar içinde izleneceği belirtilir. Bir amaca ulaşılması ile o amacın haklı veya değerli bulunması ayrı değerlendirmelerdir. Bir grubun amacına ulaşmasının diğerlerinin durumuna ne yaptığı ayrıca incelenir. Gayenin değerlendirilmesi, sonuçları yaşayan tarafların konumunu da kapsar.

Amaca ulaştıran koşullar ve araçlar, niyet beyanıyla sınırlı kalmadan araştırılır. Hangi koşulların gerekli olduğu, hangi araçların katkı sağladığı ve bu katkının nasıl anlaşılacağı açıklanır. Başarı sayılan bir gösterge gerçekleştiğinde değer verilen durumun gerçekten iyileşip iyileşmediği sorgulanır. Faaliyet miktarı, görünürlük, olumlu tepki ve tamamlanmış ara adımların nihai gayeyle ilişkisi ayrı ayrı kurulmalıdır.

Gayeyi taşımak, onu koymak, benimsemek, gerekçelendirmek ve değiştirme yetkisine sahip olmak farklı ilişkilerdir. Bir sistem kendisine verilmiş hedefi izleyebilir; bu durum hedefin kaynağı olduğunu göstermez. Amaç belirleyici, işlemleri gerçekleştiren taşıyıcı ve sonuçlarla yaşayan tarafın aynı olup olmadığı araştırılır. Bir bileşene, sırf çıktı ürettiği için gayeyi belirleme rolü atfedilmez.

~~~text
  BASTAN KABUL EDILMEZ: AMACIN TEK, ORTAK YA DA NIHAI OLDUGU
    acik secenekler: birden fazla amac . catisan amaclar .
    belirlenebilir bir amac bulunmamasi

  BIRBIRINDEN AYRILIR
    BEYAN EDILEN AMAC      yapilis amaci hakkinda ne soylendigi
    FIILEN IZLENEN AMAC    secimlerin ve kaynak kullaniminin hangi
                           sonuca yoneldigi
    ORTAYA CIKAN ETKI      gercekte ne meydana geldigi
    DEGER VERILEN SONUC    meydana gelenlerden hangilerinin hangi
                           gerekceyle arzu edilir bulundugu

    bir etki dogmasi     -x->   onun amaclandigi
    amac bildirimi       -x->   butun eylemlerin ona hizmet ettigi
    -x->  gostermez

  "NIHAI" HANGI KAPSAMDA?

    bir sonuc  --araci-->  baska bir sonuc  --araci-->  . . .
                    "bunun nicin istendigi" sorulur
    hangi nokta kendi basina degerli kabul ediliyor? bu kabul kime ait?
    nihailik iddiasi, arastirmayi gerekcesiz bicimde kapatmak icin
    kullanilmaz

  GAYEYLE FARKLI ILISKILER
    tasimak  |  koymak  |  benimsemek  |  gerekcelendirmek  |
    degistirme yetkisine sahip olmak
    bir sistem kendisine verilmis hedefi izleyebilir; bu durum hedefin
    kaynagi oldugunu gostermez
~~~

*Çizim 10 — Gaye: beyan edilen amaç, izlenen amaç, etki ve değer verilen sonuç; "nihai"nin kapsamı; gayeyle ilişkiler.*

Sınama ve Karşılık Değerlendirmesi için önerilen gaye, gerekçesi görülebilen, kapsamı belirli ve düzeltmeye açık bir anlayış geliştirmektir. Karar gerektiren durumlarda bunun karşılığı, hangi nedenle hangi seçeneğin tercih edildiğinin açıklanabilmesidir. Bu gaye, çerçevenin bütün uygulamalarının baştan kabul edilmiş ve değişmez nihai amacı olarak sunulmaz; kendisi de incelenebilir.

Varsayımsal bir karar toplantısında, eldeki süre ve bilgiler içinde gerekçeli ve uygulanabilir bir seçim üretmek amaç olarak belirlenebilir. Toplantının bitmesi, çok konuşulması veya oybirliği oluşması tek başına başarı sayılmaz. Belirleyici bir bilgi eksikliği görünür olmuş, bu bilginin nasıl ve ne zaman edinileceği belirlenmiş ve erteleme mevcut süre içinde makul bulunmuşsa, hemen karar çıkmaması amaca katkıyla bağdaşabilir. Sonuç; yer, zaman, usul ve gaye birlikte ele alınarak değerlendirilir.

~~~text
  ONERILEN GAYE
    gerekcesi gorulebilen, kapsami belirli ve duzeltmeye acik bir
    anlayis gelistirmek
    bu gaye degismez nihai amac olarak sunulmaz; kendisi de
    incelenebilir

  BASARI GOSTERGESI ILE DEGER VERILEN DURUM
    faaliyet miktari . gorunurluk . olumlu tepki . tamamlanmis ara
    adimlar: nihai gayeyle iliskisi ayri ayri kurulmalidir

  VARSAYIMSAL BIR KARAR TOPLANTISI

    amac olarak belirlenebilir: eldeki sure ve bilgiler icinde
    gerekceli ve uygulanabilir bir secim uretmek

    TEK BASINA BASARI SAYILMAZ
      toplantinin bitmesi  .  cok konusulmasi  .  oybirligi olusmasi

    HEMEN KARAR CIKMAMASI NE ZAMAN AMACA KATKIYLA BAGDASABILIR?

      [ belirleyici bir bilgi eksikligi gorunur olmus          ]
      [ bu bilginin nasil ve ne zaman edinilecegi belirlenmis  ]
      [ erteleme mevcut sure icinde makul bulunmus             ]

    sonuc; yer, zaman, usul ve gaye birlikte ele alinarak
    degerlendirilir
~~~

*Çizim 11 — Gaye: önerilen gaye; göstergeler; varsayımsal karar toplantısı örneği.*

Bu bölümün kaydı; varsa amaçları ve sahiplerini, amaçların sırasını veya çatışmasını, başarı ölçütlerini, araçların katkısını, sonuçları yaşayan tarafları ve amaçların yeniden ele alınma koşullarını içerir. Çerçevenin kendisi de hangi belirsizliği azalttığı, hangi varsayımı görünür kıldığı ve hangi hükmü veya eylemi değiştirdiği üzerinden sınanır. Sınayanın, ölçütü koyanın, gayeyi değiştirebilenin ve sonuçlarıyla yaşayanın aynı varlık olup olmadığı açık tutulur.

### Masaüstünde uygulama

1. Belirlenebilen amaçları ve bunların kimlere ait olduğunu yaz. Beyan edilen amacı, fiilen izlenen yönelimi, beklenen veya gözlenen etkiyi ve değer verilen sonucu ayır.
2. Amacın kimin açısından gerçekleşmiş sayılacağını, hangi bedeller ve sınırlar içinde izlendiğini açıkla. Amaç çoğulsa ilişkilerini ve çatışmalarını kaydet; belirlenemiyorsa bunu belirt.
3. Başarı göstergesini, araçların beklenen katkısını ve değer verilen durumla bağını sınamadan önce yaz. Sonuç geldiğinde göstergenin gerçekleşmesiyle amaç bakımından oluşan değişimi karşılaştır.
4. Gayeyi koyan, taşıyan, değiştirebilen ve sonuçlarla yaşayan tarafları ayır. Gayeye katkı hükmünü, belirsizlikleri ve amaç değiştiğinde yeniden incelenecek kayıtları belirt.

### Kayıt ve tamamlanma koşulu

Amaçların durumu, ilgili taraflar, başarı ölçütü, araçlarla ilişki ve gözlenen ya da beklenen katkı açıklandığında bu bölüm ilk değerlendirme için tamamlanır. Belirlenebilir bir amaç bulunamaması incelemeyi otomatik olarak başarısız yapmaz; bu durumda amaca ulaşma hükmü kurulmaz. Amaç veya ölçüt değişirse değişiklik tarih ve gerekçesiyle korunur.

## 6 Kökleşme (Bitiş) Protokolü

> İnceleme sonunda ne, hangi karşılık ve dayanaklarla, hangi koşullarda tutulabilir hâle geldi?

Kökleşme Protokolü, beş protokol boyunca oluşan hükümleri başlangıç kaydıyla birlikte değerlendirir. Hangi kabulün korunduğu, hangisinin değiştiği ve hangisinden vazgeçildiği açıklanır. Giderilen belirsizliklerle devam eden belirsizlikler ayrılır. Başlangıçtaki beklentinin gerçekleşmesi, tamamlanmanın tek ölçütü olarak kullanılmaz.

Bir hükmün hangi koşullarda benimsenebileceği ve kullanılabileceği belirtilir. Dayanağı, karşılaştığı itirazlar, alternatif açıklamalar ve geçerlilik sınırları birlikte kaydedilir. Hükmün desteklenmemesi veya henüz karara bağlanamaması da mümkün sonuçlardır. Kökleşme, her incelemenin sonunda gerçekleşmiş sayılmaz; yeterli karşılık bulunmadığında bunun hangi hükmü sınırladığı açıklanır.

Bölümler arasındaki ilişkiler gözden geçirilir. Varlık için kullanılan tanım, işleyiş değerlendirmesiyle; yer ve zaman koşulları, sonuçlarla; sonuçlar da gayeyle kurulan bağ bakımından tutarlı olmalıdır. Bir bölümde değişen kabul diğerlerini etkiliyorsa ilgili kayıtlar yeniden ele alınır. Ölçüt veya gaye değişmişse bu değişikliğin ne zaman ve neden yapıldığı korunur.

Metnin hazırlanması, planın kurulması, sınamanın uygulanması ve karşılığın görülmesi farklı gerçekleşme durumlarıdır. Kapanışta hangilerinin fiilen gerçekleştiği belirtilir. Bir yöntemin yazılmış olması, uygulanmış olduğu veya her koşulda işleyeceği biçiminde sunulmaz. Değerlendiricinin kendi konumuna, yöntemine veya gayesine ilişkin anlayışı değişmişse bu değişim de sonuca eklenir.

Bitiş, bu inceleme turunun gerekçeli biçimde kapatılması veya neden henüz kapatılamadığının kaydıdır. Yeni bir karşılık, değişen koşul veya çözülmemiş bir soru daha sonra yeni bir inceleme turu başlatabilir. Önceki turun başlangıç ve sonuç kayıtları bu yeni turla ilişkilendirilir.

### Masaüstünde uygulama

1. Tohum kaydını ve 1–5 arasındaki kayıtları birlikte oku. Başlangıçtan bu yana korunan, değişen ve terk edilen kabulleri belirle.
2. Temel hükümleri dayanaklarıyla eşleştir. Dayanak konumlarına geri dönülebildiğini ve kaydın yalnızca planlanan işlemleri yapılmış gibi göstermediğini kontrol et.
3. Bölümler arasındaki çelişkileri incele. Bir çelişkiyi çözmek için ilgili protokole dön; çözülemiyorsa sonuçta kapsamını ve hükme etkisini açıkla.
4. Sonuç paragrafını yaz. Desteklenen, belirli koşullarda geçerli olan, desteklenmeyen ve henüz karara bağlanamayan iddiaları dayanaklarıyla ayır.
5. Kullanım sınırlarını, açık konuları, değerlendiricinin değişen kabullerini ve yeniden değerlendirmeyi başlatacak koşulları kaydet.
6. İncelemenin durumunu ve tarihini yaz. Kayıt dosyasını son hâliyle kaydet; yeni bir tur açılacaksa önceki kaydı yeni turla ilişkilendir.

### Kayıt ve kapanış koşulu

Başlangıçtan bu yana değişenler, temel hükümler, dayanaklar, alternatif açıklamalar, kalan belirsizlikler, kullanım koşulları ve yeniden değerlendirme koşulları bu bölümün kaydını oluşturur. Bu unsurlar açıklandığında, hüküm “Henüz karar verilemiyor” olsa bile inceleme turu “Tamamlandı” olarak kapatılabilir; bu kapanışın nedeni belirtilir. İncelemeye aynı turda devam etmek için gerekli bir karşılık bekleniyorsa durum “Beklemede” tutulur ve neyin beklendiği yazılır. İncelemeye devam edilmeyecekse “Sonlandırıldı” kaydı gerekçesiyle oluşturulur.

Kökleşmeye ilişkin sonuç ayrıca ifade edilir: Hangi anlayışın hangi dayanaklarla tutulabildiği, hangi koşullara bağlı kaldığı veya neden henüz dayanak kazanmadığı açıklanır. İnceleme durumunun tamamlanmış olması, başlangıçtaki iddianın doğrulandığı veya kökleşmenin gerçekleştiği anlamına gelmez.

~~~text
  BASLANGIC KAYDIYLA BIRLIKTE DEGERLENDIRME
    hangi kabul korundu  |  hangisi degisti  |  hangisinden vazgecildi
    baslangictaki beklentinin gerceklesmesi, tamamlanmanin tek olcutu
    olarak kullanilmaz

  FARKLI GERCEKLESME DURUMLARI

    metnin           planin           sinamanin           karsiligin
    hazirlanmasi     kurulmasi        uygulanmasi         gorulmesi

    kapanista hangilerinin fiilen gerceklestigi belirtilir; bir
    yontemin yazilmis olmasi, uygulanmis oldugu ya da her kosulda
    isleyecegi biciminde sunulmaz

  UC AYRI SEY

    INCELEMENIN DURUMU     IDDIAYA ILISKIN HUKUM     KOKLESME
    Tamamlandi             Destekleniyor             hangi anlayis
    Beklemede              Belirli kosullarda        hangi dayanaklarla
    Sonlandirildi          gecerli                   tutulabiliyor,
                           Desteklenmiyor            hangi kosullara
                           Henuz karar               bagli kaliyor?
                           verilemiyor

    inceleme durumunun tamamlanmis olmasi, baslangictaki iddianin
    dogrulandigi ya da koklesmenin gerceklestigi anlamina gelmez
    hukum "Henuz karar verilemiyor" olsa bile inceleme turu
    "Tamamlandi" olarak kapatilabilir; nedeni belirtilir

  BOLUMLER ARASI TUTARLILIK
    varlik icin kullanilan tanim   <-->   isleyis degerlendirmesi
    yer ve zaman kosullari         <-->   sonuclar
    sonuclar                       <-->   gaye
~~~

*Çizim 12 — Kökleşme: kabullerin durumu; dört gerçekleşme durumu; inceleme durumu, iddia hükmü ve kökleşme.*

## Uygulama kaydı şablonu

Aşağıdaki bloğu yeni bir `.md` dosyasına kopyala. Her başlığın altını incelemenin gerektirdiği kadar paragrafla doldur. `[Doldurulacak]` ifadesi henüz kayıt girilmediğini gösterir; bir bilgiye ulaşılamıyorsa bunun yerine nedenini ve hükme etkisini yaz. Kayıt başlığını, incelemenin kısa adıyla değiştir.

```markdown
# Uygulama Kaydı

Çalışma adı: [Doldurulacak]
Kayıt numarası: [Doldurulacak]
Kullanılan protokol sürümü: 1.0
İnceleme durumu: Hazırlık
Uygulayan: [Doldurulacak]
Başlangıç tarihi: [Doldurulacak]
Son güncelleme: [Doldurulacak]
Önceki turla ilişki: [Varsa kayıt dosyası ve ilişki]

## 0 Tohum (Başlangıç) Kaydı

Başlangıç sorusu ve incelemeyi doğuran durum:
[Doldurulacak]

Geçici konu tarifi, kapsam ve kapsam dışında kalanlar:
[Doldurulacak]

Bilinenler, varsayımlar, bilinmeyenler ve geçici sözcük anlamları:
[Doldurulacak]

İlk karşılık beklentisi ve başlangıç gayesi:
[Doldurulacak]

İncelemeyi başlatan, uygulayan, amacı belirleyen ve sonuçla ilişkili taraflar:
[Doldurulacak]

Başlangıç dayanakları ve ilk incelenecek iddia:
[Doldurulacak]

## 1 Varlık Kaydı

Tanım, tür, ayırt edici özellikler ve süreklilik koşulları:
[Doldurulacak]

Gerekli, yeterli ve arızi özellikler ile bu ayrımların dayanakları:
[Doldurulacak]

Yakın karşı örnek, sınır durumu ve gerçekleştirilen ya da varsayımsal karşılaştırma:
[Doldurulacak]

Değerlendiricinin köken, taşıyıcı, işletici ve amaç belirleyici rolleri:
[Doldurulacak]

Hüküm, dayanak, belirsizlik ve hükmü değiştirecek koşul:
[Doldurulacak]

## 2 Mekan Kaydı

Yerin anlamı, ölçeği ve sınırları:
[Doldurulacak]

Erişim, kaynaklar, kısıtlar ve mümkün kılınan ilişkiler:
[Doldurulacak]

Karşılaştırılan bağlam, değişen koşullar ve karşılaştırmanın gerçekleşme durumu:
[Doldurulacak]

Değerlendiricinin konumu ve erişiminin sınırları:
[Doldurulacak]

Hüküm, dayanak, belirsizlik ve hükmü değiştirecek koşul:
[Doldurulacak]

## 3 Usül Kaydı

Sınanan iddia; kapasite, fiilî iş, süreç ve beklenen etki:
[Doldurulacak]

Aranan karşılık türü, yöntem, karşılaştırma ve önceden belirlenen ölçüt:
[Doldurulacak]

Sınama planı, başlangıç koşulları ve 4 ile 5'te belirlenen koşullarla ilişkisi:
[Doldurulacak]

Gerçekleştirilen işlem, gerçekleşme tarihi ve üretilen çıktı:
[Doldurulacak]

Gözlenen karşılık, aksama durumları ve dayanak konumları:
[Doldurulacak]

Alternatif açıklamalar, yöntem sınırlılıkları ve gerçekleşmeyen işlemler:
[Doldurulacak]

Hüküm, dayanak, belirsizlik ve hükmü değiştirecek koşul:
[Doldurulacak]

## 4 Zaman Kaydı

Olay veya kaynak tarihi; değerlendirme tarihi; gerekiyorsa saat ve saat dilimi:
[Doldurulacak]

Süreç evresi ve olayların sırası:
[Doldurulacak]

Karar anında bilinenler ve sonradan öğrenilenler:
[Doldurulacak]

Gözlem süresi, varsa karar için kalan süre ve henüz beklenen etkiler:
[Doldurulacak]

Hükmün geçerlilik zamanı ve yeniden değerlendirme koşulu:
[Doldurulacak]

## 5 Gaye Kaydı

Belirlenebilen amaçlar, amaç sahipleri ve varsa amaç çatışmaları:
[Doldurulacak]

Beyan edilen amaç, fiilî yönelim, etki ve değer verilen sonuç:
[Doldurulacak]

Başarı ölçütü, kimin açısından değerlendirildiği, bedeller ve sınırlar:
[Doldurulacak]

Araçların beklenen katkısı, gözlenen katkı ve bunların dayanakları:
[Doldurulacak]

Gayeyi koyan, taşıyan, değiştirebilen ve sonuçlarla yaşayan taraflar:
[Doldurulacak]

Hüküm, dayanak, belirsizlik ve gayeyi yeniden ele alma koşulu:
[Doldurulacak]

## 6 Kökleşme (Bitiş) Kaydı

Başlangıca göre korunan, değişen ve terk edilen kabuller:
[Doldurulacak]

Temel hükümler ve her hükmün dayanağı:
[Doldurulacak]

Bölümler arasındaki tutarlılık, çözülemeyen çelişkiler ve alternatif açıklamalar:
[Doldurulacak]

Fiilen gerçekleşenler; yalnızca planlananlar; henüz beklenen karşılıklar:
[Doldurulacak]

Tutulabilir hâle gelen anlayış ve kullanım koşulları:
[Doldurulacak]

Kalan belirsizlikler ve hangi hükümlerin neden henüz dayanak kazanmadığı:
[Doldurulacak]

Değerlendiricinin konumunda, usulünde veya gayesinde oluşan değişim:
[Doldurulacak]

Yeniden değerlendirmeyi başlatacak olay, bilgi veya koşul:
[Doldurulacak]

İnceleme durumu ve bu durumun gerekçesi:
[Doldurulacak]

Kapanış veya bekleme tarihi:
[Doldurulacak]

## Dayanak dizini

Her dayanak için adını, dosya yolunu veya erişim adresini, kullanılan bölümünü,
olay veya kaynak tarihini ve incelemede hangi hükmü desteklediğini yaz.

[Doldurulacak]

## Değişiklik kaydı

Her değişiklik için tarihi, önceki kabulü, yeni kabulü, gerekçeyi ve etkilenen
protokol bölümlerini yaz. Başlangıçtaki bilgiyi sonradan bilinenle değiştirme.

[Doldurulacak]
```

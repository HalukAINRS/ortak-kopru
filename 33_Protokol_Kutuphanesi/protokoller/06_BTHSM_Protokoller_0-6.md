# Bit Tabanlı Hesaplama Sistemleri Mühendisliği

**Protokoller 0–6**

**Sürüm:** 1.0\
**Tarih:** 30 Ekim 2026\
**Biçim:** UTF-8 Markdown

Bu belge; Tohum, Varlık, Mekan, Usül, Zaman, Gaye ve Kökleşme protokollerini tek bir çalışma düzeninde birleştirir.

Protokollerin uygulanması, sağlanan malzeme üzerinde okuma, yazma, eşleme ve değerlendirme yaparak kayıt üretmektir. Bir kayıt bölümünün tamamlanması, fiziksel bir sistemin test edilmiş olduğu anlamına gelmez. Gerçek ölçüm veya uygulama varsa kendi koşulları ve kanıtlarıyla ayrıca kaydedilir.

Çalışma sırası 0, 1, 2, 3, 4, 5 ve 6'dır. Yeni bir bulgu önceki bir tanımı, sınırı veya amacı değiştiriyorsa ilgili bölüme dönülür ve değişiklik gerekçesi kaydedilir. Kullanıcının başlangıç sınırı olan “Geçmiş bağlamları buraya taşıma.” talebi bu çalışma boyunca korunur.

## Ortak kurucu makine sorusu

> Bit Tabanlı Hesaplama Sistemleri Mühendisliği'nin köken aldığı varlık, mekan, usül, zaman, ve gayeyi taşıyan makine kimdir? Kim değildir?

Bu soru, her protokolde ilgili boyut üzerinden ele alınır. Soyut hesaplama modeli, fiziksel gerçekleştirme ve nihai gaye ayrı düzeylerde tutulur.

~~~text
  CALISMA SIRASI

     0 ---> 1 ---> 2 ---> 3 ---> 4 ---> 5 ---> 6
       <----------- ilgili bolume donulur ----------
     yeni bir bulgu onceki bir tanimi, siniri ya da amaci
     degistiriyorsa; degisiklik gerekcesi kaydedilir

  PROTOKOLLERIN UYGULANMASI
    saglanan malzeme uzerinde okuma, yazma, esleme ve degerlendirme
    yaparak kayit uretmektir

    bir kayit bolumunun         =/=       fiziksel bir sistemin test
    tamamlanmasi                          edilmis olmasi

    gercek olcum ya da uygulama varsa kendi kosullari ve kanitlariyla
    ayrica kaydedilir

  BASLANGIC SINIRI  bu calisma boyunca korunur
    "Gecmis baglamlari buraya tasima."

  ORTAK KURUCU MAKINE SORUSU
    her protokolde ilgili boyut uzerinden ele alinir

    ayri duzeylerde tutulur
    .--------------------.   .--------------------.   .--------------.
    | soyut hesaplama    |   | fiziksel           |   | nihai gaye   |
    | modeli             |   | gerceklestirme     |   |              |
    `--------------------'   `--------------------'   `--------------'
~~~

*Çizim 1 — Çalışma sırası ve geri dönüş; kayıt ile test; başlangıç sınırı; ortak sorunun üç ayrı düzeyi.*

## 0 Tohum (Başlangıç) Protokolü

**Yönlendirici soru:** Bu inceleme hangi sorudan doğuyor, hangi başlangıç koşulları içinde yürütülüyor ve hangi çıktıyı üretmek üzere açılıyor?

### Başlangıcın kaydı

Tohum Protokolü, incelemeyi başlatan konu adını, ihtiyacı, kaynak soruları ve bağlam sınırını kayıt altına alır. Başlangıçta bilinenler, açıkça kabul edilmiş çalışma varsayımları ve henüz yanıtlanmamış sorular ayrı tutulur. Bu bölümün görevi, sonraki protokollerin hangi soru ve sınırlar içinde geliştiğini izlenebilir kılmaktır.

Bu çalışmanın konu adı Bit Tabanlı Hesaplama Sistemleri Mühendisliğidir. Başlangıç sınırı, kullanıcının “Geçmiş bağlamları buraya taşıma.” talebidir. İnceleme, bu konuşmadaki sorular ve yanıtlar ile bunlarda kullanılan teknik kaynaklar üzerinden kurulur. Kullanıcı tarafından belirtilmemiş kişisel veya kurumsal bir gerekçe, başlangıç niyetiymiş gibi kaydedilmez.

İlk soru düzeni alanı varlık, mekân, usul, zaman ve gaye bakımından inceler. Her boyutta kimlik, ayırt edici ilişkiler ve kapsam sınırları sorulur. Sonraki soru bu boyutları taşıyan kurucu makinenin kimliğini araştırır. Bu sıra korunur; Turing makinesinin yanıtta ortaya çıkan açıklayıcı rolü, başlangıçta kullanıcı tarafından kabul edilmiş bir aksiyom gibi geriye yerleştirilmez.

### Kapsam ve çalışma kabulleri

Tohum kaydı, incelenecek nesne ile onu incelemek için kullanılacak kavramları ayırır. Alanın adı burada çalışma tanımı olarak kullanılır. Bit, hesaplama, sistem, mühendislik ve kurucu makine ifadelerinin anlamları ilgili protokollerde açıklığa kavuşturulur. Başlangıçta gerekli görülen bir kabul, kaynağı ve etkisi belirtilerek çalışma varsayımı olarak yazılır; bulgu veya kullanıcı kararı gibi sunulmaz.

Masaüstü uygulamasının kapsamı, sağlanan malzemeyi okuma, soruları eşleme, tanımları ve sınırları yazma, dayanakları ilişkilendirme ve sonuçları dosyalama işlemleridir. Bir bölümün yazılması, fiziksel bir cihazın incelendiğini veya teknik bir testin uygulandığını göstermez. Belgeye ilişkin işlemler ile gerçek sistem üzerinde yapılacak ölçüm ve uygulamalar ayrı kayıtlarda tutulur.

Başlangıçta beklenen çıktılar, yedi protokolün tamamlanmış metni, kaynak kaydı ve gerektiğinde kullanılacak oturum kaydıdır. Her sorunun hangi bölümde karşılanacağı belirlenir. Eksik bir bilgi “belirtilmedi” veya “açık soru” olarak kaydedilebilir. Bilinmeyen alanların varlığı, anlamlı çalışmanın sürdürülmesine engel olmak zorunda değildir; ancak bu alanlar sessizce doldurulmaz.

### Başlangıcın sınırı ve devri

Tohum, alanın ilk tarihsel aygıtını veya bütün gelişiminin tek nedenini tayin eden bölüm değildir. İncelemenin başlangıcını kaydeder; Varlık Protokolü ise incelenen alanın kimliğini tanımlar. Bu iki kayıt, başlangıç koşullarını sonraki sonuçlarla karıştırmadan birbirini tamamlar.

Tohum Protokolü, konu, kaynak sorular, bağlam sınırı, çalışma kapsamı, varsayımlar, açık sorular ve beklenen çıktılar görünür olduğunda tamamlanır. Sonraki inceleme kapsamı değiştirdiğinde başlangıç kaydı tarih ve gerekçeyle güncellenir. Böylece yeni tercihlerin baştan beri geçerli olduğu izlenimi yaratılmadan Varlık Protokolüne geçilir.

### Masaüstü uygulaması

**Amaç:** İncelemenin başlangıç sorularını, sınırlarını ve üretilecek çıktıları görünür bir başlangıç kaydına dönüştürmek.

**Girdiler:** Kullanıcının kaynak soruları, mevcut soru-yanıt metinleri, önceki belge ve bu çalışmaya ilişkin açık kısıtlar.

### Uygulama adımları

1. Konu adını ve başlangıç sorularını kaynak metinden aktar. Sonradan oluşmuş sonuçları ilk sorunun içine yerleştirme.

2. Bağlam sınırını ve kullanılabilecek malzemeyi yaz. Bu çalışma için geçmiş konuşma bağlamı ekleme; mevcut konuşmadaki teknik kaynakları kaynak kaydında tut.

3. Açıkça verilmiş bilgileri, çalışma varsayımlarını ve henüz belirtilmemiş alanları ayrı paragraflara ayır. Kullanıcının kişisel veya kurumsal amacını üretme.

4. Kaynak soruları 1–5 numaralı protokollere eşleştir; kurucu makine sorusunun her boyuttaki karşılığını belirt.

5. Bu oturumda oluşturulacak dosyaları, kullanılacak çalışma klasörünü ve bitiş ölçütünü kaydet. Başlangıç kaydı hazır olduğunda 1 Varlık Protokolüne geç.

### Beklenen çıktı

Oturum kaydındaki 0 Tohum bölümünde konu, kaynak sorular, bağlam sınırı, kapsam, varsayımlar, açık sorular ve beklenen çıktılar.

### Tamamlanma ölçütleri

- [ ] Kaynak soru metinleri ile başlangıç bağlam sınırı kayıtlıdır.
- [ ] Belirtilmemiş alanlar görünürdür; sonuçlar başlangıç varsayımı gibi gösterilmemiştir.
- [ ] Her sorunun ele alınacağı protokol ve bu oturumun beklenen dosya çıktıları bellidir.

### Kayıt düzeni

Kayıt alanları: Konu ve başlatan soru; Kaynak malzeme; Bağlam sınırı; Bu oturumun kapsamı; Başlangıç varsayımları ve dayanakları; Belirtilmemiş alanlar ve açık sorular; Beklenen çıktılar ve bitiş ölçütü.

Bu ve sonraki bütün protokollerin kayıtlarında her alan için dayanak veya açık durum belirtilir. Yapılması planlanan işlem, gerçekten yapılan işlem ve gözlenen sonuç ayrı yazılır. Kullanılan durum değerleri Başlanmadı, Sürüyor, Tamamlandı ve Açık soruyla tamamlandı biçimindedir.

### Sonraki adım

1 Varlık Protokolüne geç. Kapsam sonradan değişirse bu kaydı gerekçesiyle güncelle.

~~~text
  BASLANGIC KAYDI
    konu adi  .  ihtiyac  .  kaynak sorular  .  baglam siniri

  AYRI TUTULUR
    baslangicta bilinenler  |  acikca kabul edilmis calisma
    varsayimlari  |  henuz yanitlanmamis sorular

  SORULARIN SIRASI KORUNUR

    ilk soru duzeni         sonraki soru            yanitta ortaya cikan
    alani bes boyutta  ---> kurucu makinenin   ---> Turing makinesinin
    inceler                 kimligini arastirir     aciklayici rolu
        ^                                                 |
        `-----x-----  baslangicta kabul edilmis bir  -----'
                      aksiyom gibi geriye yerlestirilmez

  TOHUM ILE VARLIK
    Tohum    incelemenin baslangicini kaydeder
    Varlik   incelenen alanin kimligini tanimlar

  IKI AYRI KAYIT
    belgeye iliskin islemler          |   gercek sistem uzerinde
    okuma, esleme, yazma,             |   yapilacak olcum ve
    iliskilendirme, dosyalama         |   uygulamalar
    bir bolumun yazilmasi, fiziksel bir cihazin incelendigini ya da
    teknik bir testin uygulandigini gostermez

  HER BOLUMUN KAYIT DUZENI
    yapilmasi planlanan islem  |  gercekten yapilan islem  |
    gozlenen sonuc      ayri yazilir
    Baslanmadi  |  Suruyor  |  Tamamlandi  |  Acik soruyla tamamlandi
    eksik bilgi "belirtilmedi" ya da "acik soru" olarak kaydedilebilir;
    bilinmeyen alanlar sessizce doldurulmaz
~~~

*Çizim 2 — Tohum: başlangıç kaydı; soruların sırası; belge işi ile gerçek sistem; her bölümün kayıt düzeni.*

## 1 Varlık Protokolü

**Kaynak soru:** Nedir? Onu o yapan nelerdir? Neler değildir?

### Tanım ve ayırt edici yapı

Bit tabanlı hesaplama sistemleri mühendisliği; verileri bit dizileriyle temsil eden ve bu temsiller üzerinde tanımlı işlemler gerçekleştiren sistemlerin, belirli ihtiyaçlar ve kısıtlar altında tasarlanması, gerçekleştirilmesi, doğrulanması ve sürdürülmesidir. Bu çalışma tanımı, bilgisayar mühendisliğinin donanım, yazılım ve hesaplama sistemlerini birlikte ele alan kapsamıyla büyük ölçüde örtüşür. Başlığın burada kullanılması, ayrıca doğrulanmış resmî bir disiplin veya meslek yetkisi tanımı oluşturmaz. [1]

Bit tabanlılık temsil biçimini, hesaplama bu temsillerin kurallı dönüşümünü, sistem bileşenlerin birlikte oluşturduğu davranışı, mühendislik ise bu davranışın gerçek koşullarda kurulmasını anlatır. Alanın konusu sayı işlemleriyle sınırlı değildir. Veri saklama, metin ve görüntü işleme, haberleşme, benzetim ve aygıt denetimi de bu çerçevede ele alınabilir. Sistemin kimliği, bileşenlerinin listesi kadar bunların birbirine sağladığı işlevlerle belirlenir.

Bit, mantıksal düzeyde 0 veya 1 değerini alan temsil öğesidir. Bit ile onu taşıyan fiziksel durum ayrı düzeylerdir. Elektronik bir gerçekleştirmede mantıksal değerler gerilim aralıklarıyla temsil edilebilir; bu nedenle 0 değerini her durumda elektriğin yokluğuyla, 1 değerini de elektriğin varlığıyla özdeşleştirmek doğru değildir. Gürültü payları ve geçerli çalışma koşulları, mantıksal ayrımların fiziksel olarak korunmasını sağlar. [2]

Bir bit örüntüsünün anlamı kullanılan kodlama ve yorumlama kuralıyla belirlenir. Örneğin 11111111 örüntüsü işaretsiz sekiz bitlik tamsayı olarak 255'i, ikiye tümleyen gösteriminde ise −1'i temsil eder. Aynı örüntü başka bir düzen içinde görüntü parçası, komut veya durum kaydı olabilir. Temsilin doğru saklanması ve taşınması ile kullanım bağlamında doğru yorumlanması farklı koşullardır. Shannon'ın iletişim ile anlam arasındaki ayrımı, bu iki başarı düzeyini birbirinden ayırmak için kullanılabilir. [3]

~~~text
  ADIN DORT SOZCUGU
    bit tabanlilik   temsil bicimi
    hesaplama        bu temsillerin kuralli donusumu
    sistem           bilesenlerin birlikte olusturdugu davranis
    muhendislik      bu davranisin gercek kosullarda kurulmasi

  BIT ILE ONU TASIYAN FIZIKSEL DURUM AYRI DUZEYLERDIR

    mantiksal duzey             0                          1
                                ^                          ^
                                |                          |
    fiziksel duzey       [ bir gerilim ]          [ baska bir gerilim ]
    (elektronik bir      [ araligi     ]          [ araligi           ]
     gerceklestirmede)

    gurultu paylari ve gecerli calisma kosullari, mantiksal ayrimlarin
    fiziksel olarak korunmasini saglar
    0'i her durumda elektrigin yokluguyla, 1'i de elektrigin
    varligiyla ozdeslestirmek dogru degildir

  AYNI ORUNTU, FARKLI KODLAMA VE YORUMLAMA KURALI

                 .-- isaretsiz sekiz bitlik tamsayi ->  255
    11111111  ---+-- ikiye tumleyen gosterimi ------->  -1
                 `-- baska bir duzen icinde --------->  goruntu parcasi,
                                                        komut ya da
                                                        durum kaydi

    temsilin dogru saklanmasi      |    kullanim baglaminda dogru
    ve tasinmasi                   |    yorumlanmasi
                        farkli kosullardir
~~~

*Çizim 3 — Varlık: adın dört sözcüğü; bit ile fiziksel taşıyıcı; aynı örüntünün farklı yorumları.*

Mühendislik niteliği, davranışın ihtiyaç ve kısıtlarla ilişkilendirilmesinde belirginleşir. Sistemin hangi girdilerle, hangi yük altında, ne kadar sürede ve hangi kaynaklarla çalışacağı açıklığa kavuşturulur. Kararların varsayımları ve kabul ölçütleri görünür olur. Her kararın matematiksel olarak ispatlanması zorunlu değildir; ancak beklenen davranış ile tasarım arasında değerlendirmeye açık bir bağ kurulması gerekir.

### Kurucu makinenin kimliği

Kurucu hesaplama modeli düzeyinde başlıca karşılık Turing makinesidir. Bu soyut model, sonlu bir denetim düzeniyle şeritteki sembolleri okur, değiştirir ve konum değiştirir. Evrensel Turing makinesi ise başka bir makinenin kodlanmış betimini kullanarak onun hesaplamasını taklit edebilir. Yapılacak işlemin tarifi de işlenebilir bir temsil hâline gelir. Böylece hesaplama modeli, genel amaçlı programlanabilirlik ve fiziksel bilgisayar ayrı kavramlar olarak korunur. [4]

Turing makinesinin sembol alfabesi yalnızca 0 ve 1 olmak zorunda değildir; sonlu bir sembol kümesi uygun biçimde ikili olarak kodlanabilir. Ayrıca bütün bit tabanlı sistemlerin evrensel olması gerekmez. Özel bir sayma, dönüştürme veya denetim işi için kurulan devre de bu mühendisliğin nesnesidir. Kurucu modelin açıklayıcı gücü, alanın bütün ürünlerini aynı biçime sokma zorunluluğu doğurmaz. [4, 5]

Turing'in modelinin gerisinde, işaretlerle ve belirli kurallarla hesap yapan insan etkinliğinin soyutlanması vardır. Bu ilişki insanın bütün varlığını bir makineye indirgemez; belirli bir etkinliğin biçimsel olarak modellenmesini anlatır. Turing'i kurucu modellerden biri olarak kabul etmek de bütün mühendislik alanının tek tarihsel kaynaktan doğduğu anlamına gelmez. [4]

~~~text
  KURUCU HESAPLAMA MODELI DUZEYINDE BASLICA KARSILIK: TURING MAKINESI

            .---------------------.
            | sonlu bir denetim   |
            | duzeni              |
            `----------+----------'
                       |   okur . degistirir . konum degistirir
                       v
      ---+---+---+---+---+---+---+---+---+---
     ... | a | b | a | # | b | a | a |   | ...   serit ve semboller
      ---+---+---+---+---+---+---+---+---+---

  EVRENSEL TURING MAKINESI
      ---+-----------------------------------------+---
     ... | baska bir makinenin kodlanmis betimi    | ...
      ---+-----------------------------------------+---
    onun hesaplamasini taklit edebilir; yapilacak islemin tarifi de
    islenebilir bir temsil haline gelir

  AYRI KAVRAMLAR OLARAK KORUNUR
    hesaplama modeli  |  genel amacli programlanabilirlik  |
    fiziksel bilgisayar

  ZORUNLU DEGILDIR
    sembol alfabesinin yalnizca 0 ve 1 olmasi
    butun bit tabanli sistemlerin evrensel olmasi (ozel bir sayma,
    donusturme ya da denetim isi icin kurulan devre de bu
    muhendisligin nesnesidir)

  MODELIN GERISINDE
    isaretlerle ve belirli kurallarla hesap yapan insan etkinliginin
    soyutlanmasi; bu iliski insanin butun varligini bir makineye
    indirgemez
~~~

*Çizim 4 — Varlık: Turing makinesi; evrensel makine; ayrı korunan üç kavram; zorunlu olmayanlar.*

### Kapsam sınırları

Alan yalnızca kod yazmakla, elektronik devre yapmakla veya kuramsal hesaplama incelemekle özdeş değildir; bu faaliyetlerle farklı düzeylerde ilişki kurar. Bir bilgisayarı kullanmak da tek başına onun hesaplama davranışını tasarlamak anlamına gelmez. Küçük bir program mühendislik kararları içerebilir; büyük bir sistemin büyüklüğü ise tek başına mühendislik niteliğini veya kalitesini göstermez.

Sayısal, ikili ve elektronik kavramları aynı kapsamı taşımaz. Sayısal temsil ayrık değerlerle ilgilidir; ikili temsil bunun özel bir biçimidir; elektronik ise gerçekleştirme yollarından biridir. Analog veya kuantum hesaplama klasik bit temelli hesaplamayla özdeş değildir. Bununla birlikte karma sistemlerin klasik denetim ve veri işleme bölümleri bit tabanlı olabilir. Kübitin durum yapısı da klasik bir bitin değerinin bilinmemesinden farklıdır. [2, 10]

Yanlış amaçla kullanılan veya kötü tasarlanmış bir sistem, bu nedenle bit tabanlı olma niteliğini kaybetmez. Teknik sınıflandırma, mühendislik başarısı ve amacın değeri ayrı değerlendirmelerdir. Bu ayrım, sonraki protokollerde kimlik ile kaliteyi ve işlev ile gayeyi birbirine karıştırmamak için korunur.

~~~text
  AYNI KAPSAMI TASIMAZ

    .-----------------------------------------------.
    | SAYISAL TEMSIL   ayrik degerlerle ilgilidir   |
    |    .--------------------------------------.   |
    |    | IKILI TEMSIL   bunun ozel bir bicimi |   |
    |    `--------------------------------------'   |
    `-----------------------------------------------'
      ELEKTRONIK       gerceklestirme yollarindan biri

  OZDES DEGILDIR
    analog ya da kuantum hesaplama  =/=  klasik bit temelli hesaplama
      (karma sistemlerin klasik denetim ve veri isleme bolumleri
       bit tabanli olabilir)
    kubitin durum yapisi  =/=  klasik bir bitin degerinin bilinmemesi

  ALAN SUNLARLA OZDES DEGILDIR; ONLARLA FARKLI DUZEYLERDE ILISKI KURAR
    yalnizca kod yazmak  |  elektronik devre yapmak  |
    kuramsal hesaplama incelemek

  AYRI DEGERLENDIRMELER
    teknik siniflandirma  |  muhendislik basarisi  |  amacin degeri

    yanlis amacla kullanilan ya da kotu tasarlanmis bir sistem, bu
    nedenle bit tabanli olma niteligini kaybetmez
~~~

*Çizim 5 — Varlık: sayısal, ikili ve elektronik; özdeş olmayanlar; ayrı üç değerlendirme.*

### Masaüstü uygulaması

**Amaç:** Alanın çalışma tanımını, ayırt edici ilişkilerini ve kapsam sınırlarını kayıt altına almak.

**Girdiler:** 0 Tohum kaydı, mevcut tanımlar, kurucu makine tartışması ve ilgili teknik kaynaklar.

### Uygulama adımları

1. Bit tabanlılık, hesaplama, sistem ve mühendislik sözcüklerini ayrı ayrı açıklayıp birlikte bir çalışma tanımı yaz.

2. Bit, fiziksel taşıyıcı ve yorumlanan anlam arasındaki ayrımı kaydet. Kullanılan örneklerin hangi temsil kuralına bağlı olduğunu belirt.

3. Turing modeli, evrensel makine, mimari düzen ve fiziksel sistem rollerini ayır. Evrenselliği her sisteme zorunlu nitelik olarak yükleme.

4. Kapsama giren ve girmeyen faaliyetleri gerekçeleriyle yaz. Teknik kimlik, tasarım kalitesi ve amacın değerini ayrı değerlendir.

5. Teknik iddiaları kaynaklarıyla ilişkilendir; kavramsal yorumları ve açık soruları belirt. Tanımı 2 Mekan Protokolüne girdi olarak devret.

### Beklenen çıktı

Çalışma tanımı, kimlik ölçütleri, kurucu modelin rolü, kapsam dışı kalanlar ve dayanaklardan oluşan varlık kaydı.

### Tamamlanma ölçütleri

- [ ] Sistem ile mühendislik faaliyeti ayrı açıklanmıştır.
- [ ] Bit, taşıyıcı, anlam ve kurucu model ayrımları korunmuştur.
- [ ] Tanım, resmî bir standart veya tek tarihsel köken iddiası üretmeden kapsamı belirtmektedir.

### Kayıt düzeni

Kayıt alanları: Çalışma tanımı; Ayırt edici ilişkiler; Kurucu model ve fiziksel sistem ayrımı; Kapsama girenler; Kapsam dışında kalanlar ve gerekçeler; Dayanaklar; Açık sorular.

### Sonraki adım

2 Mekan Protokolüne geç. Konu tanımını değiştiren bulgu varsa 0 Tohum kaydını da güncelle.

## 2 Mekan Protokolü

**Kaynak soru:** Nerededir? Bu yeri, oraya has bir yer yapan nelerdir? Neler değildir?

### Konum ve ilişki düzeni

Bu mühendisliğin mekânı fiziksel gerçekleştirme, kavramsal örgütlenme ve kullanım ortamı birlikte düşünülerek belirlenir. Fiziksel olarak hesaplama davranışını taşıyan aygıtlarda ve bağlantılarda bulunur. Gerçekleştirme tek bir cihazda toplanabilir veya birbirine bağlı cihazlara dağılabilir. Bilgisayar mühendisliğinin kapsamı da bütünleşik devrelerden gömülü sistemlere ve dağıtık hesaplama ortamlarına uzanır. [1]

Kavramsal olarak alanın yeri, temsil kuralları, işlemler, algoritmalar ve mimariler arasındaki ilişkilerdedir. Pratik olarak ise hesaplamanın bir ihtiyacı karşıladığı kullanım ortamındadır. Bir temsil kararı bellek gereksinimini, bir süre şartı mimariyi, bir fiziksel sınır algoritma seçimini etkileyebilir. Bu nedenle alanın yeri tek bir bileşene veya yalnızca donanımla yazılımın temas çizgisine indirgenemez.

Bu yeri ayırt eden özellik, farklı türden koşulların aynı tasarımda birlikte karşılanmasıdır. Matematiksel modelde geçerli bir işlem seçilmiş aygıtta gereken sürede gerçekleştirilemeyebilir. Aygıtın ürettiği sonuç yazılım tarafından yanlış yorumlanabilir. Doğru yorumlanan bir sonuç da kullanım ihtiyacına uygun olmayabilir. Mühendislik, bu düzeyler arasındaki geçişlerin koşullarını kurar ve değerlendirir.

~~~text
  MEKAN UC SEY BIRLIKTE DUSUNULEREK BELIRLENIR

    FIZIKSEL GERCEKLESTIRME   hesaplama davranisini tasiyan aygitlar
                              ve baglantilar; tek bir cihazda ya da
                              birbirine bagli cihazlara dagilmis
    KAVRAMSAL ORGUTLENME      temsil kurallari, islemler, algoritmalar
                              ve mimariler arasindaki iliskiler
    KULLANIM ORTAMI           hesaplamanin bir ihtiyaci karsiladigi yer

  BIR KARAR OTEKINI ETKILEYEBILIR
    bir temsil karari     --->   bellek gereksinimi
    bir sure sarti        --->   mimari
    bir fiziksel sinir    --->   algoritma secimi

  DUZEYLER ARASINDAKI GECISLER

    matematiksel modelde gecerli bir islem
          |    secilmis aygitta gereken surede gerceklestirilemeyebilir
          v
    aygitin urettigi sonuc
          |    yazilim tarafindan yanlis yorumlanabilir
          v
    dogru yorumlanan sonuc
          |    kullanim ihtiyacina uygun olmayabilir
          v
    kullanim ihtiyaci

    muhendislik, bu gecislerin kosullarini kurar ve degerlendirir
    alanin yeri tek bir bilesene ya da yalnizca donanimla yazilimin
    temas cizgisine indirgenemez
~~~

*Çizim 6 — Mekan: birlikte düşünülen üç yer; birbirini etkileyen kararlar; düzeyler arasındaki geçişler.*

Arayüz, parçaların bağlandığı noktanın yanında bir beklenti düzenidir. Hangi verinin kabul edildiği, verinin hangi anlamı taşıdığı, ne zaman hazır olduğu ve eksik ya da geç geldiğinde ne yapılacağı belirlenir. Aynı sayıyı paylaşan iki bileşen, farklı birimler veya veri biçimleri varsayıyorsa bağlantının çalışması yeterli olmaz. Teknik bağlantı ile anlamsal uyum birlikte ele alınır.

Sistem sınırı, hangi bileşenlerin tasarımın içinde ve hangilerinin çevresinde sayıldığını gösterir. Bir hizmetin dışarıdan alınması, o hizmete bağımlılığın sonuçlarını ortadan kaldırmaz. Tasarımcı dış bileşenin iç yapısını yönetemese bile gecikmesinin veya kesintisinin kendi sistemindeki etkisini değerlendirebilir. Mekân böylece fiziksel yerleşim kadar erişim, bağımlılık ve sorumluluk ilişkileriyle tanımlanır.

~~~text
  ARAYUZ  parcalarin baglandigi noktanin yaninda bir beklenti duzeni

    [ bilesen ] ----------------- arayuz -----------------> [ bilesen ]
                   hangi veri kabul edilir?
                   veri hangi anlami tasir?
                   ne zaman hazirdir?
                   eksik ya da gec gelirse ne yapilir?

    ayni sayiyi paylasan iki bilesen farkli birimler ya da veri
    bicimleri varsayiyorsa baglantinin calismasi yeterli olmaz

            teknik baglanti    +    anlamsal uyum
                     birlikte ele alinir

  SISTEM SINIRI  hangi bilesenler tasarimin icinde, hangileri cevresinde

      tasarimin ici                               cevresi
     .------------------------.                  .-----------------.
     |  bilesenler            | --- bagimli ---> | disaridan       |
     |                        |                  | alinan hizmet   |
     `------------------------'                  `-----------------'

    bir hizmetin disaridan alinmasi, o hizmete bagimliligin sonuclarini
    ortadan kaldirmaz; tasarimci dis bilesenin ic yapisini yonetemese
    bile gecikmesinin ya da kesintisinin kendi sistemindeki etkisini
    degerlendirebilir

  MEKAN  fiziksel yerlesim kadar erisim, bagimlilik ve sorumluluk
         iliskileriyle tanimlanir
~~~

*Çizim 7 — Mekan: arayüz bir beklenti düzenidir; sistem sınırı ve dış bağımlılık.*

### Kurucu makinedeki mekân

Turing makinesindeki şerit, sembollerin yerleştirildiği ve okuma-yazma başlığının eriştiği soyut konum düzenidir. Şeridin hücreleri, bilginin nerede bulunduğunu ve makinenin hangi konuma erişebildiğini belirler. Bu düzen fiziksel bellekle aynı şey değildir. Modelin sınırsız kullanılabilir şerit varsayımı, hesaplanabilirliği belirli bir bellek kapasitesine bağlamadan incelemeye yarar; sonlu bir hesaplama yalnızca sonlu bir bölüm kullanır. [5]

Somut mühendislikte konum ve erişim; bellek, bağlantılar, giriş-çıkış ve fiziksel yerleşim üzerinden gerçekleşir. Von Neumann adıyla anılan mimari çizgi bu örgütlenmeyi anlamak için önemlidir. 1945 tarihli EDVAC raporu aritmetik birim, denetim, bellek, giriş ve çıkış bölümlerini ele alır; işlem talimatları ve verilerin saklanması da bu yapının parçasıdır. Bu mimari, Turing makinesinin diğer adı veya bütün bit tabanlı sistemlerin zorunlu biçimi değildir. [7]

### Mekânın sınırları

Alan yalnızca bilgisayar kasasının içinde değildir. Verinin geldiği, çıktının kullanıldığı ve başka sistemlerle ilişki kurulduğu noktalar da seçilmiş sistem sınırı içinde önem taşıyabilir. Buna karşılık dijital araç kullanılan bütün toplumsal faaliyetler bu mühendisliğin konusu hâline gelmez. Kullanım amacının bilimsel, ekonomik veya toplumsal değerlendirmesi başka uzmanlıkları da gerektirebilir.

Sanal veya soyut olarak tanımlanmış bir ortam, fiziksel kaynaklardan bağımsız değildir. Soyutlama belirli ayrıntıları gizleyerek çalışmayı kolaylaştırabilir; zaman, enerji ve kapasite gereksinimlerini yok etmez. Aynı şekilde alanın belirli bir kurumda veya sektörde yürütülmesi, o kurumun ya da sektörün alanın özü olduğu anlamına gelmez.

Mekânsal bütünlüğün korunması, bütün katmanların tek kişi tarafından yapılmasını gerektirmez. Uzmanlaşma mümkündür. Gerekli olan, parçaların birlikte çalışmasını sağlayan varsayımların, arayüzlerin ve sorumlulukların uyuşmasıdır. Sistemin yeri, bu ilişkilerin kurulabildiği ve değerlendirilebildiği çalışma alanıdır.

~~~text
  KURUCU MAKINEDEKI MEKAN: SERIT  soyut konum duzeni

                          okuma-yazma basligi
                                   v
      ---+---+---+---+---+---+---+---+---+---+---
     ... |   |   |   |   |   |   |   |   |   | ...
      ---+---+---+---+---+---+---+---+---+---+---
         hucreler: bilginin nerede bulundugunu ve makinenin hangi
         konuma erisebildigini belirler

    serit   =/=   fiziksel bellek
    sinirsiz kullanilabilir serit varsayimi, hesaplanabilirligi belirli
    bir bellek kapasitesine baglamadan incelemeye yarar; sonlu bir
    hesaplama yalnizca sonlu bir bolum kullanir

  SOMUT MUHENDISLIKTE KONUM VE ERISIM
    bellek . baglantilar . giris-cikis . fiziksel yerlesim

    1945 tarihli EDVAC raporunun ele aldigi bolumler
    .-----------.  .---------.  .--------.  .-------.  .-------.
    | aritmetik |  | denetim |  | bellek |  | giris |  | cikis |
    | birim     |  |         |  |        |  |       |  |       |
    `-----------'  `---------'  `--------'  `-------'  `-------'
    islem talimatlari ve verilerin saklanmasi da bu yapinin parcasidir
    bu mimari, Turing makinesinin diger adi ya da butun bit tabanli
    sistemlerin zorunlu bicimi degildir

  SOYUTLAMA
    belirli ayrintilari gizler    |    zaman, enerji ve kapasite
                                  |    gereksinimlerini yok etmez
    uzmanlasma mumkundur; gerekli olan varsayimlarin, arayuzlerin ve
    sorumluluklarin uyusmasidir
~~~

*Çizim 8 — Mekan: şerit ile fiziksel bellek; EDVAC raporunun bölümleri; soyutlamanın gizlediği ve yok etmediği.*

### Masaüstü uygulaması

**Amaç:** Fiziksel, kavramsal ve kullanım konumlarını; bileşen ilişkilerini ve sistem sınırını açıklamak.

**Girdiler:** 0 ve 1 kayıtları, sağlanan sistem veya konu açıklaması, varsa bileşen ve arayüz bilgileri.

### Uygulama adımları

1. Fiziksel gerçekleştirme, temsil ve erişim düzeni, mimari ilişkiler ve kullanım ortamını ayrı paragraflarda yaz.

2. Sağlanan malzemede bulunan bileşenleri ve ilişkileri kaydet. Belirtilmemiş aygıt veya hizmetleri gözlenmiş envanter gibi ekleme.

3. Her önemli arayüz için girdi, çıktı, anlam, zaman koşulu ve hata davranışını belirt. Bilgi yoksa ilgili alanı belirtilmedi olarak kaydet.

4. Turing şeridinin soyut konum düzeni ile fiziksel bellek ve yerleşimi ayır. Mimari örneğin bütün alanı temsil edip etmediğini kontrol et.

5. Sistemin içi, çevresi ve dış bağımlılıklarını belirle. Bu sınırları ve belirsizlikleri 3 Usül Protokolüne devret.

### Beklenen çıktı

Konum, bileşen ilişkileri, arayüz beklentileri, sistem sınırı ve dış bağımlılıkları içeren mekân kaydı.

### Tamamlanma ölçütleri

- [ ] Soyut konum ile fiziksel gerçekleştirme ayrı kayıtlıdır.
- [ ] Sistem sınırı ve bilinen dış bağımlılıklar görünürdür.
- [ ] Eksik bileşen veya arayüz bilgileri, gerçek inceleme yapılmış gibi doldurulmamıştır.

### Kayıt düzeni

Kayıt alanları: Fiziksel gerçekleştirme; Kavramsal konum ve erişim düzeni; Kullanım ortamı; Bileşenler ve ilişkiler; Arayüz beklentileri; Sistem sınırı ve dış bağımlılıklar; Dayanaklar ve açık sorular.

### Sonraki adım

3 Usül Protokolüne geç. Sistem sınırı tanımı etkiliyorsa 1 Varlık Protokolüne geri dön.

## 3 Usül Protokolü

**Kaynak soru:** Nasıl işler yapar? Bu yaptıklarını, ona has yapan nelerdir? Neler değildir?

### Sistemin işi ve mühendisliğin işi

Bit tabanlı sistem veri alır, saklar, dönüştürür, karşılaştırır, aktarır ve çıktı üretir. Gerektiğinde önceki olayların etkisini durum olarak tutar. Bu işlemler bir hesaplama sonucuna, bir haberleşmeye veya fiziksel eylemi yöneten komuta dönüşebilir. Mühendislik ise hangi girdilerin, durumların, kuralların ve çıktıların gerekli olduğunu; bunların nasıl gerçekleştirileceğini ve değerlendirileceğini belirler.

Mühendislik usulü ihtiyacın açıklığa kavuşturulmasıyla başlar. İhtiyaç, üzerinde karar verilebilen davranış şartlarına çevrilir. Ardından veri temsili ve mimari seçilir; devreler, yazılım bileşenleri ve bağlantılar gerçekleştirilip bütünleştirilir. Test, ölçüm, analiz, benzetim ve uygun durumlarda biçimsel yöntemlerle davranış hakkında kanıt toplanır. Kullanım sırasında elde edilen bilgiler tasarıma geri döner.

Bu faaliyetler her projede tek yönlü bir sıra izlemez. Bir test sonucu veri temsilini değiştirebilir; bir kaynak sınırı gereksinimlerin yeniden değerlendirilmesini gerektirebilir. Hazır bileşen kullanmak da bu usulün içindedir. Her parçayı sıfırdan üretmek yerine, seçilmiş parçaların hangi varsayımlarla birlikte çalıştığını açıklamak gerekir.

Temsil seçimi, sistemin neyi ayırt edebileceğini ve hangi bedelle işleyebileceğini belirler. Bir ölçümü daha az bitle tutmak kapasite gereksinimini azaltabilir; aynı zamanda ayırt edilebilen değerleri sınırlar. Daha ayrıntılı kayıt, yapılabilecek incelemeleri genişletebilir; aktarım ve saklama yükünü de değiştirebilir. Bu nedenle veri biçimi, yalnızca yazım tercihi olarak ele alınmaz.

~~~text
  SISTEMIN ISI                       |  MUHENDISLIGIN ISI
  veri alir, saklar, donusturur,     |  hangi girdilerin, durumlarin,
  karsilastirir, aktarir ve cikti    |  kurallarin ve ciktilarin gerekli
  uretir; onceki olaylarin etkisini  |  oldugunu; nasil gerceklestirilip
  durum olarak tutar                 |  degerlendirilecegini belirler

  MUHENDISLIK USULU

    ihtiyacin acikliga kavusturulmasi
      v
    davranis sartlari   (uzerinde karar verilebilen)
      v
    veri temsili ve mimari secimi   <----------------------------.
      v                                                          |
    gerceklestirme ve butunlestirme                              |
      v                                                          |
    davranis hakkinda kanit toplama                              |
      v                                                          |
    kullanim  ---- elde edilen bilgiler tasarima geri doner -----'

    tek yonlu bir sira izlemez
      bir test sonucu     --->  veri temsilini degistirebilir
      bir kaynak siniri   --->  gereksinimlerin yeniden
                                degerlendirilmesini gerektirebilir

  TEMSIL SECIMI  neyi ayirt edebilecegini ve hangi bedelle
                 isleyebilecegini belirler
    daha az bit            kapasite gereksinimi azalabilir; ayirt
                           edilebilen degerler sinirlanir
    daha ayrintili kayit   yapilabilecek incelemeler genisleyebilir;
                           aktarim ve saklama yuku de degisebilir
~~~

*Çizim 9 — Usül: sistemin işi ile mühendisliğin işi; mühendislik usulü ve geri dönen bilgi; temsil seçimi.*

### Kurucu makinenin usulü

Turing makinesinde usul, mevcut denetim durumu ile okunan sembolden yapılacak işlemi belirleyen geçiş kuralıdır. Okuma, yazma, konum ve durum değiştirme işlemleri bu düzen içinde yürütülür. Evrensel makinede başka bir makinenin betimi de girdi olarak işlenir. Bununla birlikte gereksinim belirleme, tasarım seçeneklerini karşılaştırma ve bakım düzenleme gibi bütün mühendislik faaliyetleri tek başına bu geçiş kuralından türemez. [4]

Mantıksal davranışın fiziksel olarak gerçekleştirilmesi ayrı bir tasarım sorusudur. Shannon'ın röle ve anahtarlama devreleri üzerine çalışması, belirli davranış özelliklerine sahip devrelerin matematiksel analizi ve senteziyle ilgilidir. Bu katkı, hesaplama davranışının soyut tarifinin yanında, istenen mantıksal ilişkileri gerçekleştiren düzeneklerin kurulması yönünü açıklar. Turing, Shannon ve von Neumann aynı sorunun birbirinin yerine geçen adları değildir. [6]

Mühendislikte davranışın farklı düzeyler boyunca korunması gerekir. İhtiyaç düzeyindeki bir kural, veri temsilinde, algoritmada, yazılımda ve fiziksel gerçekleştirmede karşılık bulmalıdır. Örneğin bir ölçüm sınırı aştığında uyarı üretme şartı; ölçüm birimine, karşılaştırmanın yapılışına, verinin güncelliğine ve uyarının kullanıcıya ulaşmasına bağlıdır. Aynı davranış şartı, birbirine bağlı birkaç tasarım kararı gerektirir.

~~~text
  KURUCU MAKINENIN USULU: GECIS KURALI

      ( mevcut denetim durumu , okunan sembol )
                        |
                        v
      yapilacak islem:  yazma . konum degistirme . durum degistirme

    evrensel makinede baska bir makinenin betimi de girdi olarak
    islenir
    gereksinim belirleme, tasarim seceneklerini karsilastirma ve bakim
    duzenleme gibi butun muhendislik faaliyetleri tek basina bu gecis
    kuralindan turemez

  UC AD  ayni sorunun birbirinin yerine gecen adlari degildir
    Turing        hesaplama davranisinin soyut tarifi
    Shannon       istenen mantiksal iliskileri gerceklestiren
                  duzeneklerin kurulmasi
    von Neumann   mimari cizgi: aritmetik birim, denetim, bellek,
                  giris ve cikis bolumleri

  DAVRANISIN FARKLI DUZEYLER BOYUNCA KORUNMASI

    ihtiyac duzeyindeki kural
      --> veri temsili --> algoritma --> yazilim --> fiziksel
                                                     gerceklestirme

    bir olcum siniri astiginda uyari uretme sarti sunlara baglidir
      olcum birimi  .  karsilastirmanin yapilisi  .
      verinin guncelligi  .  uyarinin kullaniciya ulasmasi
~~~

*Çizim 10 — Usül: geçiş kuralı; Turing, Shannon ve von Neumann; davranışın düzeyler boyunca korunması.*

### Doğrulama ve değerlendirme

Doğrulama, sistemin belirlenmiş gereksinimleri karşılayıp karşılamadığını; geçerleme ise amaçlanan ortamda amaçlanan ihtiyacı karşılayıp karşılamadığını değerlendirir. Bir kuralın doğru uygulanmış olması, seçilmiş kuralın ihtiyaca uygun olduğunu kendiliğinden göstermez. NASA'nın sistem mühendisliği yaklaşımındaki bu ayrım, işlemin doğruluğu ile kullanım uygunluğunun birlikte fakat ayrı sorular olarak ele alınmasını sağlar. [8]

Davranış hakkındaki değerlendirme koşulludur. Girdi aralığı, yük, enerji kaynağı, bağlantı koşulları veya kullanım biçimi değiştiğinde önceki kanıt yetersiz kalabilir. Bu koşulları açıklamak tasarımın hangi sınırlar içinde güvenilir olduğunu gösterir. Bir kez başarılı çıktı görmek, bütün girdiler ve bütün çalışma koşulları için genel güvence oluşturmaz.

### Usulün sınırları

Bit tabanlılık, bütün işlerin tek işlemcide, sırayla veya ortak saatle yapılmasını gerektirmez. İşler paralel yürütülebilir veya olaylarla tetiklenebilir. Olasılıksal yöntemler ve öğrenilmiş modeller de bit tabanlı bir sistem içinde kullanılabilir. Böyle durumlarda başarı ölçütleri, değerlendirilen davranışın niteliğine göre kurulmalıdır.

Bu usul rastgele bit değişiklikleri üretmek veya gerçekliğin bütün özelliklerini eksiksiz temsil etmek değildir. Tasarım, amaca ilişkin ayrımları seçer ve dışarıda bıraktığı özelliklerin sonuçlarını değerlendirir. Teknik olarak yapılabilen bir işlemin ihtiyaca katkı sağladığı ayrıca gösterilmelidir. Usulün başarısı, işlem düzeni ile kullanım sonucu arasında korunabilen bağa dayanır.

~~~text
  BIRLIKTE FAKAT AYRI IKI SORU

       amaclanan ortamda                belirlenmis
       amaclanan ihtiyac                gereksinimler
              ^                              ^
              |                              |
          GECERLEME                      DOGRULAMA
              |                              |
              `----------- sistem -----------'

    bir kuralin dogru uygulanmis olmasi, secilmis kuralin ihtiyaca
    uygun oldugunu kendiliginden gostermez

  DEGERLENDIRME KOSULLUDUR
    girdi araligi . yuk . enerji kaynagi . baglanti kosullari .
    kullanim bicimi      degistiginde onceki kanit yetersiz kalabilir

    bir kez basarili cikti gormek, butun girdiler ve butun calisma
    kosullari icin genel guvence olusturmaz

  BIT TABANLILIK SUNU GEREKTIRMEZ
    butun islerin tek islemcide, sirayla ya da ortak saatle yapilmasi
    isler paralel yurutulebilir ya da olaylarla tetiklenebilir;
    olasiliksal yontemler ve ogrenilmis modeller de kullanilabilir

  BU USUL SUNLAR DEGILDIR
    rastgele bit degisiklikleri uretmek
    gercekligin butun ozelliklerini eksiksiz temsil etmek

    usulun basarisi, islem duzeni ile kullanim sonucu arasinda
    korunabilen baga dayanir
~~~

*Çizim 11 — Usül: doğrulama ve geçerleme; koşullu değerlendirme; usulün sınırları.*

### Masaüstü uygulaması

**Amaç:** Sistemin yaptığı işlemler ile mühendisliğin uyguladığı yöntemleri ve değerlendirme biçimlerini ayırmak.

**Girdiler:** 0–2 kayıtları, davranış açıklamaları, veri temsil kararları ve varsa test veya gözlem kayıtları.

### Uygulama adımları

1. Sistemin girdi, durum, işlem ve çıktı ilişkilerini yaz. Bunları mühendisliğin ihtiyaç belirleme, tasarım ve değerlendirme faaliyetlerinden ayır.

2. Temsil ve mimari kararlarının davranışı nasıl etkilediğini açıkla. Bir kararın dayanağı belirtilmemişse varsayımı görünür kıl.

3. Kurucu makinenin geçiş kuralını, fiziksel gerçekleştirmeyi ve genel mühendislik yöntemlerini ayrı düzeylerde konumlandır.

4. Doğrulama ve geçerleme için ayrı sorular ve değerlendirme yöntemleri yaz. Planlanan test, yapılmış işlem ve gözlenen sonucu ayrı kaydet.

5. Başarı koşullarını, geri besleme ihtiyacını ve açık kalan yöntem sorularını belirt. Süre ve sıra gereksinimlerini 4 Zaman Protokolüne devret.

### Beklenen çıktı

İşlem düzeni, mühendislik yöntemi, değerlendirme planı ve mevcut kanıtların ayrıldığı usul kaydı.

### Tamamlanma ölçütleri

- [ ] Sistem işlemleri ile mühendislik faaliyetleri ayrı açıklanmıştır.
- [ ] Doğrulama ve geçerleme ayrımı korunmuştur.
- [ ] Planlanan ve gerçekten yapılan değerlendirmeler birbirine karıştırılmamıştır.

### Kayıt düzeni

Kayıt alanları: Sistemin girdileri, durumları, işlemleri ve çıktıları; Mühendislik faaliyetleri; Temsil ve mimari kararları; Doğrulama soruları ve yöntemi; Geçerleme soruları ve yöntemi; Açık sorular.

### Sonraki adım

4 Zaman Protokolüne geç. Davranış uyuşmazlığının kaynağı tanım veya arayüzse ilgili önceki protokolü düzelt.

## 4 Zaman Protokolü

**Kaynak soru:** Hangi andadır? Bu anı, diğer zamanlardan farklı yapan nelerdir? Neler değildir?

### Tarihsel zaman ve çalışma zamanı

Bu mühendislik tek bir anda bulunmaz. Tarihsel konumu, sistemin çalışma zamanı ve mühendislik yaşam döngüsü ayrı düzeylerde ele alınır. Tarihsel olarak alan; ikili temsil, kurallı hesaplama, fiziksel gerçekleştirme ve programlı sistem örgütlenmesiyle ilgili katkıların buluştuğu teknik gelenek içindedir. Belirli bir makinenin, dilin veya ürün kuşağının tarihi bütün alanın tek doğum anı değildir.

Bir tarihsel dönemi ayırt eden, imkânların, ihtiyaçların ve kısıtların belirli bileşimidir. Aynı hesaplama fikri farklı dönemlerde farklı koşullarda gerçekleştirilebilir. Mantıksal ilkeler ile döneme özgü aygıt ve mimari tercihleri ayrı tutulur. Turing'in modeli, Shannon'ın devre çalışması ve EDVAC raporu bu nedenle farklı sorulara katkı sağlayan kaynaklar olarak okunur. [4, 6, 7]

Mevcut yanıtlarda kullanılan tarihli bağlam örneği, IEA'nın 16 Nisan 2026 tarihli değerlendirmesidir. Bu değerlendirme veri merkezi büyümesinin elektrik altyapısı, gelişmiş çipler ve başka bileşenlerin tedariki gibi fiziksel koşullarla ilişkisini ele alır. Bu örnek, büyük ölçekli hesaplamanın belirli bir dönemdeki gerçekleştirme koşullarını gösterir; bitin tanımını veya alanın değişmez özünü belirlemez. [11]

Çalışma zamanında girdi alınır, durum değişir, çıktı üretilir ve kullanılır. Zamanın içeriği yalnızca hız değildir. Olay sırası, verinin güncelliği ve tamamlanmamış işlemler de sistemin o andaki durumunu etkiler. Aynı komut farklı bir durumda veya farklı sırada uygulanırsa farklı sonuç doğurabilir.

~~~text
  BU MUHENDISLIK TEK BIR ANDA BULUNMAZ  ayri duzeylerde ele alinir
    tarihsel konum  |  sistemin calisma zamani  |
    muhendislik yasam dongusu

  TARIHSEL KONUM  farkli sorulara katki saglayan kaynaklar

     1936-37         1938            1945                   2026
   -----*--------------*---------------*--------- . . . ------*-------->
    Turing'in      Shannon'in      EDVAC                IEA
    modeli         devre           raporu               degerlendirmesi
                   calismasi

    IEA degerlendirmesi tarihli bir baglam ornegidir: bitin tanimini
    ya da alanin degismez ozunu belirlemez
    belirli bir makinenin, dilin ya da urun kusaginin tarihi butun
    alanin tek dogum ani degildir

  CALISMA ZAMANI
    girdi alinir --> durum degisir --> cikti uretilir --> kullanilir

    zamanin icerigi yalnizca hiz degildir
        olay sirasi  .  verinin guncelligi  .  tamamlanmamis islemler

    ayni komut  --- farkli bir durumda ya da     --->   farkli sonuc
                    farkli sirada uygulanirsa           dogurabilir
~~~

*Çizim 12 — Zaman: üç ayrı düzey; tarihli kaynaklar; çalışma zamanı.*

### Kurucu makinenin zamanı

Turing modelinde zaman, mantıksal işlem adımlarının ilerleyişiyle temsil edilir. Bir sonraki adımın ne olduğu belirlenebilir; bu adımın kaç saniye süreceği modelin tanımından çıkmaz. Soyut bir adım, fiziksel işlemci saat çevrimiyle özdeş değildir. Hesaplanabilirlik ile gerekli kaynaklar altında ve gereken sürede gerçekleştirilebilirlik ayrı sorulardır. [5]

Dağıtık sistemlerde yerel saat, iletişim gecikmesi ve olayların nedensel sırası birbirinden ayrılmalıdır. Bütün bileşenlerin kusursuz bir ortak şimdiye sahip olduğu varsayılamaz. Lamport'un mantıksal saatler ve olay sıralaması üzerine çalışması, nedensel düzen ile fiziksel saatlerin aynı kavram olmadığını açıklayan temel kaynaklardan biridir. [9]

Bir uygulamada çıktının belirli bir süre içinde üretilmesi gerekli olabilir; başka bir uygulamada tamamlanmış bir işlem sırasına dayanması veya yeterince güncel veri kullanması öne çıkabilir. En yüksek ortalama hız her zaman öncelikli ölçüt değildir. Gerekli zaman koşulunu öngörülebilir biçimde sağlamak, kullanım amacına göre daha önemli olabilir.

~~~text
  KURUCU MAKINENIN ZAMANI: MANTIKSAL ISLEM ADIMLARI

    mantiksal adim      1      2      3      4      5     ...
                        |      |      |      |      |
    kac saniye?         ?      ?      ?      ?      ?     modelin
                                                          tanimindan
                                                          cikmaz

    soyut bir adim    =/=    fiziksel islemci saat cevrimi

    hesaplanabilirlik    |    gerekli kaynaklar altinda ve gereken
                         |    surede gerceklestirilebilirlik
                    ayri sorulardir

  DAGITIK SISTEMLERDE BIRBIRINDEN AYRILIR
    yerel saat  |  iletisim gecikmesi  |  olaylarin nedensel sirasi

    bir bilesen    ----o-----------o-------------------->  yerel saati
                        \
                         \   ileti
                          \
    baska bilesen  ---------o----------o---------------->  yerel saati

    butun bilesenlerin kusursuz bir ortak simdiye sahip oldugu
    varsayilamaz; nedensel duzen ile fiziksel saatler ayni kavram
    degildir

  ZAMAN KOSULU UYGULAMAYA GORE DEGISIR
    belirli bir sure icinde cikti  |  tamamlanmis bir islem sirasi  |
    yeterince guncel veri
    en yuksek ortalama hiz her zaman oncelikli olcut degildir
~~~

*Çizim 13 — Zaman: mantıksal adım ile saat çevrimi; dağıtık sistemlerde yerel saat, gecikme ve nedensel sıra.*

### Yaşam döngüsü ve müdahale anı

Mühendislik yaşam döngüsü ihtiyacın belirlenmesinden tasarıma, gerçekleştirmeye, kullanıma, değişikliğe ve kullanımdan kaldırmaya uzanır. Tasarım sırasında henüz gerçekleşmemiş davranış hakkında varsayımlar ve modeller vardır. Denemelerde bunlar sınanır; kullanımda gerçek davranış gözlenir. Değişiklik sırasında hangi özelliklerin korunacağı ve hangi değerlendirmelerin yenileneceği belirlenir.

Bir evreyi diğerinden ayıran, neyin bilindiği ve neyin hangi koşullarda değiştirilebildiğidir. Henüz tasarım hâlindeki bir tercih ile çok sayıda kullanılan aygıta yerleşmiş bir tercih aynı müdahale koşullarına sahip değildir. Mühendislik kararı, teknik içeriğinin yanında alındığı ve uygulandığı zamanla da ilişkilidir.

Düşünsel bir yorum olarak bu alan, bir beklentinin hesaplama sistemi için somut davranış yükümlülüğüne dönüştüğü anda belirginleşir. Belirsiz bir istek; belirli girdiler, koşullar ve sonuçlar üzerinden tarif edildiğinde mühendislik problemi kurulmaya başlar. Bu yorum, alanın tarihsel doğuşuna ilişkin tek bir tarih iddiası değildir.

### Zamanın sınırları

Alan yalnızca saat darbesinde, üretim aşamasında veya teslim anında bulunmaz. En yeni teknolojiyle özdeş değildir; eski bir mimari de belirli bir ihtiyacı uygun koşullarda karşılayabilir. Geçmişte doğrulanmış bir tasarımın gelecekte her koşulda geçerli kalacağı varsayılmaz. Ayrıca sürekli çalışan bir sistemde durmak, kendiliğinden başarı veya nihai gaye sayılmaz; başarı zaman koşullarıyla birlikte tanımlanır.

~~~text
  MUHENDISLIK YASAM DONGUSU

    ihtiyacin belirlenmesi --> tasarim --> gerceklestirme --> kullanim
                                                                  |
                         kullanimdan kaldirma <-- degisiklik <----'

    tasarimda      henuz gerceklesmemis davranis hakkinda varsayimlar
                   ve modeller vardir
    denemelerde    bunlar sinanir
    kullanimda     gercek davranis gozlenir
    degisiklikte   hangi ozelliklerin korunacagi ve hangi
                   degerlendirmelerin yenilenecegi belirlenir

  BIR EVREYI DIGERINDEN AYIRAN
    neyin bilindigi   |   neyin hangi kosullarda degistirilebildigi

    henuz tasarim halindeki            cok sayida kullanilan aygita
    bir tercih                         yerlesmis bir tercih
               ayni mudahale kosullarina sahip degildir

  DUSUNSEL BIR YORUM OLARAK ALANIN BELIRGINLESTIGI AN
    bir beklenti   --->   hesaplama sistemi icin somut davranis
                          yukumlulugu
    bu yorum, alanin tarihsel dogusuna iliskin tek bir tarih iddiasi
    degildir

  ZAMANIN SINIRLARI
    alan yalnizca saat darbesinde, uretim asamasinda ya da teslim
    aninda bulunmaz; en yeni teknolojiyle ozdes degildir
    gecmiste dogrulanmis bir tasarimin gelecekte her kosulda gecerli
    kalacagi varsayilmaz
~~~

*Çizim 14 — Zaman: yaşam döngüsü; evreleri ayıran; müdahale koşulları; alanın belirginleştiği an.*

### Masaüstü uygulaması

**Amaç:** Tarihsel konum, mantıksal sıra, fiziksel süre ve yaşam döngüsü koşullarını birbirinden ayırmak.

**Girdiler:** 0–3 kayıtları, tarihli kaynaklar, belirtilmiş süre şartları ve varsa ölçüm kayıtları.

### Uygulama adımları

1. Tarihsel kaynakların olay veya yayın tarihlerini kendi bağlamlarıyla kaydet. Döneme ait örneği değişmez ilke gibi kullanma.

2. Mantıksal işlem sırasını, fiziksel süreyi ve olayların nedensel sırasını ayrı yaz.

3. Gecikme, son süre veya veri güncelliği şartı verilmişse kaynağıyla kaydet. Ölçüm, tahmin ve tanımlanmamış alanları açıkça ayır.

4. İncelenen çalışmanın yaşam döngüsü evresini ve değiştirilebilen kararlarını belirt. Belgeleme evresini gerçek bir sistemin işletim evresi gibi sunma.

5. Zamansal sınırlamaları ve yeniden değerlendirme koşullarını kaydet; bunların kullanım amacı üzerindeki etkisini 5 Gaye Protokolüne devret.

### Beklenen çıktı

Tarihsel bağlam, mantıksal sıra, fiziksel süre koşulları ve yaşam döngüsü bilgisini ayıran zaman kaydı.

### Tamamlanma ölçütleri

- [ ] Mantıksal adım, fiziksel saat çevrimi ve saniye özdeşleştirilmemiştir.
- [ ] Verilen süre şartlarının kaynağı ve ölçülmüş olup olmadığı bellidir.
- [ ] Yaşam döngüsü evresi ve değişim koşulları gerçek bilgiye dayalı veya açıkça belirtilmemiş durumdadır.

### Kayıt düzeni

Kayıt alanları: Tarihsel bağlam ve kaynak tarihleri; Mantıksal işlem veya olay sırası; Fiziksel süre şartları; Ölçümler ve gözlemler; Tahminler ve dayanakları; Yaşam döngüsü evresi; Yeniden değerlendirme koşulları; Açık sorular.

### Sonraki adım

5 Gaye Protokolüne geç. Süre şartı yöntemi veya mimariyi değiştiriyorsa 2 ve 3 numaralı protokollere dön.

## 5 Gaye Protokolü

**Kaynak soru:** Hangi nihai amaca hizmet eder? Bu nihai amaca ulaştıran nelerdir? Neler değildir?

### Teknik amaç ve nihai gerekçe

Gaye bakımından teknik yakın amaç, kullanım amacı ve amacın değer açısından değerlendirilmesi ayrılır. Teknik yakın amaç, seçilmiş hesaplama davranışını belirlenen doğruluk, zaman, kaynak ve güvenilirlik koşullarında gerçekleştirmektir. Kullanım amacı, bu davranışın neden istendiğidir. Nihai gerekçe ise karşılanmak istenen ihtiyacın neden değerli olduğuyla ilgilidir.

Aynı hesaplama yeteneği farklı kullanım amaçlarına hizmet edebilir. Bu nedenle bütün uygulamalar için tek bir nihai amaç, bitin yapısından veya geçiş kurallarından kendiliğinden çıkmaz. Bir sistemin etkili çalışması, hizmet ettiği hedefin iyi seçildiğini de garanti etmez. Hesaplama başarısı, kullanım uygunluğu ve amacın değeri ayrı değerlendirmeler olarak korunur.

İyi mühendislik açısından savunulan yönelim, insanların gerekçelendirilebilir ihtiyaçlarını, etkileri değerlendirilebilen ve kaynak koşulları gözetilen hesaplama sistemleriyle karşılamaktır. Bu, teknik bir doğa yasası değil mesleki bir değer tercihidir. ACM'nin kamu yararını mesleki çalışmaların merkezine koyan etik ilkesi de bu tür bir normatif yönelimdir. [12]

### Kurucu makinenin taşıdığı gaye

Turing makinesine verilen hesaplama görevi ile görevin neden yapılmaya değer olduğu aynı düzeyde değildir. Makine bir işlevi gerçekleştirebilir; program içinde hedefler, başarı koşulları ve alt hedefler temsil edilebilir. Bununla birlikte gayenin makinede temsil edilmesi, gayenin makinenin teknik yapısından zorunlu olarak doğduğu anlamına gelmez.

Bir listeyi sıralayan makine düşünüldüğünde, sıralama işlemi teknik görevdir. Listenin neyi temsil ettiği, hangi ölçütün uygun olduğu ve sonucun nasıl kullanılacağı ayrıca belirlenir. Makineye verilen görevin doğru yürütülmesi, bu daha geniş tercihleri kendiliğinden gerekçelendirmez. Turing modeli tek başına bilinç, niyet veya ahlaki sorumluluk hakkında hüküm de vermez.

~~~text
  GAYE BAKIMINDAN AYRILAN UC SEY

    NIHAI GEREKCE        karsilanmak istenen ihtiyacin neden degerli
          ^              oldugu
          |
    KULLANIM AMACI       bu davranisin neden istendigi
          ^
          |
    TEKNIK YAKIN AMAC    secilmis hesaplama davranisini belirlenen
                         dogruluk, zaman, kaynak ve guvenilirlik
                         kosullarinda gerceklestirmek

    ayni hesaplama yetenegi farkli kullanim amaclarina hizmet edebilir;
    tek bir nihai amac, bitin yapisindan ya da gecis kurallarindan
    kendiliginden cikmaz

  AYRI DEGERLENDIRMELER
    hesaplama basarisi  |  kullanim uygunlugu  |  amacin degeri

  SAVUNULAN YONELIM
    teknik bir doga yasasi degil, mesleki bir deger tercihidir

  KURUCU MAKINENIN TASIDIGI GAYE: BIR LISTEYI SIRALAYAN MAKINE

                      .-----------------.
      liste  ------>  | siralama islemi |  ------>  siralanmis liste
                      | teknik gorev    |
                      `-----------------'
      ayrica belirlenir
        liste neyi temsil ediyor?  .  hangi olcut uygun?  .
        sonuc nasil kullanilacak?

    gayenin makinede temsil edilmesi, gayenin makinenin teknik
    yapisindan zorunlu olarak dogdugu anlamina gelmez
~~~

*Çizim 15 — Gaye: teknik yakın amaç, kullanım amacı, nihai gerekçe; bir listeyi sıralayan makine.*

### Amaca ulaştıran ilişkiler

Amaca ulaşmanın ilk koşulu ihtiyacın doğru kurulmasıdır. Yanlış tanımlanmış bir ihtiyaca verilen kusursuz teknik yanıt asıl sorunu çözmeyebilir. İstenen özellik ile ulaşılmak istenen sonuç ayırt edilmelidir. Daha sık kayıt tutma isteği, örneğin bir olayın nedenini anlayabilme ihtiyacından doğabilir; uygun çözüm doğru veriyi doğru zaman bilgisiyle kaydetmeyi gerektirebilir.

Amaç, değerlendirilebilir başarı ölçütlerine çevrilir. İyi, hızlı veya güvenilir gibi ifadeler hangi koşulda neyin kabul edileceğini açıklayacak biçimde belirginleştirilir. Ölçütlerin görevi gerçek ihtiyacı temsil etmektir. Ölçütler amacın yerine geçtiğinde sistem sayısal hedefleri tuttururken kullanım açısından başarısız olabilir.

Veri ve model seçimi amaçla ilişkilendirilir. Sistemin ölçmediği veya temsil etmediği önemli bir durumu, yalnızca hesaplama gücünü artırarak hesaba katması beklenemez. Verinin kaynağı, anlamı ve belirsizliği değerlendirilir. Bitlerin doğru tutulmasıyla, temsilin dünyayı ihtiyaç bakımından yeterli açıklaması ayrı koşullardır.

Tasarım seçeneklerinin değeri kullanım amacıyla belirlenir. Daha hızlı, daha küçük, daha ucuz veya daha ayrıntılı olmak farklı bağlamlarda yararlı olabilir. Sınırlı enerjiyle ve seyrek çalışan bir aygıtın öncelikleri, gecikmenin belirleyici olduğu başka bir sistemle aynı olmayabilir. Bütün amaçlar için tek bir en iyi teknik tercih varsayılmaz.

Doğrulama ve geçerleme, amaçla araç arasındaki bağı birlikte değerlendirir. Belirlenmiş gereksinimlerin karşılanması ve bu gereksinimlerin gerçek ihtiyacı temsil etmesi ayrı ayrı incelenir. Kullanım sırasında edinilen bilgiler, başlangıç varsayımlarının ve tasarım kararlarının yeniden değerlendirilmesine yol açabilir. Böylece bakım, arızayı düzeltmenin yanında sistemin hâlâ istenen işe hizmet edip etmediğini değerlendirmeyi de içerir. [8]

~~~text
  AMACA ULASTIRAN ILISKILER

    IHTIYACIN DOGRU KURULMASI
      yanlis tanimlanmis bir ihtiyaca verilen kusursuz teknik yanit
      asil sorunu cozmeyebilir
        |
        v
    DEGERLENDIRILEBILIR BASARI OLCUTLERI
      olcutler amacin yerine gectiginde sistem sayisal hedefleri
      tuttururken kullanim acisindan basarisiz olabilir
        |
        v
    VERI VE MODEL SECIMI
      olcmedigi ya da temsil etmedigi onemli bir durumu, yalnizca
      hesaplama gucunu artirarak hesaba katmasi beklenemez
        |
        v
    TASARIM SECENEKLERI
      butun amaclar icin tek bir en iyi teknik tercih varsayilmaz
        |
        v
    DOGRULAMA VE GECERLEME
      gereksinimlerin        |   bu gereksinimlerin gercek ihtiyaci
      karsilanmasi           |   temsil etmesi
        |
        v
    KULLANIM VE BAKIM
      bakim, arizayi duzeltmenin yaninda sistemin hala istenen ise
      hizmet edip etmedigini degerlendirmeyi de icerir
~~~

*Çizim 16 — Gaye: amaca ulaştıran ilişkiler ve her birinde gözetilen.*

### Gayenin sınırları

Daha çok bit üretmek veya saklamak, en yüksek işlem hızına ulaşmak, her şeyi sayısallaştırmak ve bütün işleri otomatikleştirmek alanın evrensel nihai amacı değildir. Bunlar belirli projelerde hedef veya araç olabilir; değerleri seçilen ihtiyaçla ilişkili olarak değerlendirilir. Teknik olarak yapılabilir olan her şeyi yapmak da kendi başına bir mühendislik gerekçesi oluşturmaz.

İnsan kararını bütünüyle ortadan kaldırmak, alanın tanımından çıkan zorunlu bir hedef değildir. Hangi kararların hangi koşullarda sisteme verileceği ayrıca belirlenir. Teknik başarı ile toplumsal yarar özdeşleştirilmez. Kötü bir amaca hizmet eden sistemin bit tabanlı niteliğini koruması, ne olmadığı ile ne yapmaması gerektiğinin farklı sorular olduğunu gösterir.

Bu ayrımlar, varsayımsal bir su deposu denetleyicisinde birlikte görülebilir. Ölçümler bitlerle temsil edilir, belirli kurallarla işlenir ve pompa komutu üretilir. Yazılım sayıları hatasız işlese bile ölçümün yanlış birimle yorumlanması, eski veriye dayanılması veya denetim kuralının ihtiyaca uymaması başarısızlığa yol açabilir. Mühendisliğin gaye bakımından sorumluluğu, tanımlanmış işlem ile gerçek kullanımda beklenen sonuç arasındaki bağı kurmak ve değerlendirmektir.

~~~text
  VARSAYIMSAL BIR SU DEPOSU DENETLEYICISI

    |~~~~~~~~~|  olcum         .-----------------.
    |         |  (bitlerle)    | belirli         | pompa
    |   su    | -------------> | kurallarla      | ---------> [ pompa ]
    | deposu  |   (1) (2)      | isleme     (3)  | komutu
    |         |                `-----------------'
    `---------'

    yazilim sayilari hatasiz islese bile basarisizliga yol acabilir
      (1) olcumun yanlis birimle yorumlanmasi
      (2) eski veriye dayanilmasi
      (3) denetim kuralinin ihtiyaca uymamasi

    muhendisligin gaye bakimindan sorumlulugu
      tanimlanmis islem   <--- bagi kurmak ve --->   gercek kullanimda
                               degerlendirmek        beklenen sonuc

  ALANIN EVRENSEL NIHAI AMACI DEGILDIR
    daha cok bit uretmek ya da saklamak  .  en yuksek islem hizina
    ulasmak  .  her seyi sayisallastirmak  .  butun isleri
    otomatiklestirmek
    bunlar belirli projelerde hedef ya da arac olabilir

    teknik basari    =/=    toplumsal yarar
    ne olmadigi   |   ne yapmamasi gerektigi      farkli sorulardir
~~~

*Çizim 17 — Gaye: varsayımsal su deposu denetleyicisi; üç başarısızlık yeri; alanın nihai amacı olmayanlar.*

### Masaüstü uygulaması

**Amaç:** Teknik görevi, kullanım ihtiyacını, nihai gerekçeyi ve başarı ölçütlerini ayrı fakat ilişkili kaydetmek.

**Girdiler:** 0–4 kayıtları, açıkça belirtilmiş ihtiyaç ve amaçlar, başarı ölçütleri ve değer kaynakları.

### Uygulama adımları

1. Teknik yakın amacı, kullanım amacını ve nihai gerekçeyi ayrı paragraflara yaz. Belirtilmemiş amaçları kullanıcının kararı olarak üretme.

2. Makinede temsil edilen hedef ile o hedefin neden değerli olduğu sorusunu ayır.

3. Başarı ölçütlerinin hangi ihtiyacı temsil ettiğini ve hangi yöntemle değerlendirileceğini açıkla. Verilmemiş eşik değerler ekleme.

4. Mesleki değer yönelimlerini kaynaklarıyla belirt; bunları teknik yasaya veya kullanıcı onayına dönüştürme.

5. Amaç ile mevcut tasarım veya kavramsal çerçeve arasındaki uyumu, sınırları ve açık soruları kaydet. Sonuçları 6 Kökleşme Protokolüne devret.

### Beklenen çıktı

Teknik amaç, kullanım ihtiyacı, nihai gerekçe, başarı ölçütleri ve değer ayrımlarını içeren gaye kaydı.

### Tamamlanma ölçütleri

- [ ] Teknik amaç ile nihai gerekçe ayrıdır.
- [ ] Başarı ölçütleri ihtiyaçla ilişkilendirilmiş ve dayanakları belirtilmiştir.
- [ ] Kullanıcı tarafından belirtilmemiş amaç veya onay, kesin karar gibi kaydedilmemiştir.

### Kayıt düzeni

Kayıt alanları: Teknik yakın amaç; Kullanım amacı ve kimin ihtiyacı olduğu; Nihai gerekçe; Başarı ölçütleri ve değerlendirme yöntemi; Veri ve modelin amaca uygunluğu; Mesleki değer yönelimleri; Dayanaklar ve açık sorular.

### Sonraki adım

6 Kökleşme Protokolüne geç. Amaç değişikliği kapsamı etkiliyorsa önce 0 ve ilgili protokolleri güncelle.

## 6 Kökleşme (Bitiş) Protokolü

**Yönlendirici soru:** Bu inceleme sonunda hangi anlayış yerleşti, hangi dayanaklarla taşınıyor, hangi sınırlar içinde geçerli ve hangi sorular açık kaldı?

### Sonuçların birlikte değerlendirilmesi

Kökleşme Protokolü, Tohumda açılan soruların Varlık, Mekan, Usül, Zaman ve Gaye protokollerinde nasıl karşılandığını birlikte değerlendirir. Ulaşılan anlayış, dayanakları, geçerlilik koşulları ve açık kalan sorularla beraber kapanış kaydına dönüştürülür. Kapanan şey, bu çalışma turunun belgeleme ve değerlendirme kapsamıdır.

Beş protokolün kendi içinde anlaşılır olması kadar birbirleriyle tutarlı olması da gerekir. Varlıkta soyut model olarak tanımlanan bir makine, başka bir bölümde bütün fiziksel koşulların veya nihai gayenin tek kaynağı gibi kullanılamaz. Mekânda belirlenen sınırlar, usulde tanımlanan işlemler ve zamanda verilen koşullarla uyuşmalıdır. Gayeye ilişkin değerlendirme de teknik davranışla ilişkili tutulmalı, bu davranıştan zorunlu olarak türetilmemelidir.

Bu çalışmada korunacak temel ayrımlar; bit ile fiziksel taşıyıcı, sembol ile yorumlanan anlam, hesaplama modeli ile fiziksel gerçekleştirme, mantıksal adım ile fiziksel süre, gereksinimlere uygunluk ile kullanım uygunluğu ve teknik görev ile nihai gerekçe arasındadır. Bu ayrımların farklı bölümlerde nasıl kullanıldığı kontrol edilir. Bir karşılığın eksik veya çelişkili olduğu yer, ilgili protokole geri dönülerek düzeltilir ya da çözülmemiş mesele olarak kaydedilir.

~~~text
  KORUNACAK TEMEL AYRIMLAR

    bit                        |   fiziksel tasiyici
    sembol                     |   yorumlanan anlam
    hesaplama modeli           |   fiziksel gerceklestirme
    mantiksal adim             |   fiziksel sure
    gereksinimlere uygunluk    |   kullanim uygunlugu
    teknik gorev               |   nihai gerekce

    bir karsiligin eksik ya da celiskili oldugu yer, ilgili protokole
    geri donulerek duzeltilir ya da cozulmemis mesele olarak kaydedilir

  PROTOKOLLER BIRBIRIYLE TUTARLI OLMALIDIR
    varlikta soyut model olarak tanimlanan bir makine, baska bir
    bolumde butun fiziksel kosullarin ya da nihai gayenin tek kaynagi
    gibi kullanilamaz

    mekanda belirlenen sinirlar   <-->   usulde tanimlanan islemler
                                  <-->   zamanda verilen kosullar
    gayeye iliskin degerlendirme teknik davranisla iliskili tutulur,
    bu davranistan zorunlu olarak turetilmez

  KURUCU MAKINE, BES BOYUTTA  (onceki bolumlerden)
    1 varlik   Turing makinesi: kurucu hesaplama modeli
    2 mekan    serit: soyut konum duzeni; fiziksel bellekle ayni sey
               degil
    3 usul     gecis kurali; butun muhendislik faaliyetleri ondan
               turemez
    4 zaman    mantiksal islem adimlari; saat cevrimiyle ozdes degil
    5 gaye     verilen gorev ile gorevin neden yapilmaya deger oldugu
               ayni duzeyde degil
~~~

*Çizim 18 — Kökleşme: korunacak altı ayrım; protokoller arası tutarlılık; kurucu makine beş boyutta.*

### Dayanaklar ve açık sorular

Teknik kaynakla desteklenen ifadeler, bu ifadeler üzerine kurulan kavramsal yorumlar ve savunulan değer yönelimleri ayrı tutulur. Kaynak, yalnızca gerçekten desteklediği iddia için kullanılır. Tarihli bir bağlam örneği değişmez ilke gibi sunulmaz. Bir amaç kullanıcı tarafından belirtilmemişse, genel bir mesleki yönelim kullanıcının onayladığı nihai amaç yerine geçirilmez.

Açık sorular kapanış kaydının parçasıdır. Her açık noktanın neyi etkilediği, mevcut sonucu hangi ölçüde sınırladığı ve yeniden değerlendirme için hangi bilgiye ihtiyaç duyduğu yazılır. Belgenin tamamlanmış olması bütün uygulama kararlarının verilmiş olduğu anlamına gelmez. Temel bir çelişki çözülmeden sonuç kesinleştirilmez; kapsam dışında kalan veya açıkça sınırlandırılan belirsizlikler görünür bırakılarak çalışma turu kapatılabilir.

Bir iddianın kanıtı, planlanan bir kontrol, gerçekten yapılmış işlem ve gözlenen sonuç birbirine dönüştürülmez. Hazırlanmış test planı uygulanmış test olarak; oluşturulmuş protokol de gerçek bir hesaplama sisteminin doğrulandığına dair sonuç olarak yazılamaz. Kapanış kaydı, yalnızca yapılan kontrolleri ve elde bulunan dayanakları bildirir.

### Dosyaların ve çalışma turunun kapanışı

Masaüstü kapanışında bölüm bütünlüğü, soru karşılıkları, dosya adları, Türkçe karakterlerin korunması, kaynak bağlantılarının metinde bulunması ve paket içeriği kontrol edilir. Bağlantı hedeflerinin yerel dosyalar için bulunabilirliği ile dış sitelerin güncel erişilebilirliği ayrı kontrollerdir. Hangi denetim yapıldıysa onun sonucu kaydedilir; yapılmayan denetim tamamlanmış sayılmaz.

Son sürümün dosyaları, sürüm bilgisi, değişiklik gerekçesi ve varsa yürütme kaydı belirtilir. Ana belge ile tekil protokol dosyaları aynı metin sürümünü taşımalıdır. Çalışma bir kişiye veya masaüstü yardımcısına devredildiğinde hangi dosyadan başlanacağı, hangi kayıtların doldurulacağı ve hangi soruların açık olduğu anlaşılır olmalıdır.

Kökleşme Protokolü; başlangıç sorularının karşılıkları görünür, temel ayrımlar korunmuş, dayanaklar izlenebilir, açık sorular kaydedilmiş ve son dosyalar erişilebilir olduğunda tamamlanır. Bitiş, Turing makinesinin durma durumuyla veya bütün konunun sonsuza kadar çözülmesiyle özdeş değildir. Yeni gereksinim, kaynak veya çelişki ortaya çıktığında ilgili protokol yeniden ele alınır; kapanış kaydına bu değişikliğin gerekçesi eklenir.

### Masaüstü uygulaması

**Amaç:** Başlangıç sorularının karşılıklarını, protokoller arası tutarlılığı ve son dosyaları kapanış kaydında toplamak.

**Girdiler:** 0–5 kayıtları, ana belge, tekil protokol dosyaları, kaynaklar ve gerçekten yapılmış kontrol sonuçları.

### Uygulama adımları

1. 0 Tohumdaki her sorunun hangi bölümde karşılandığını kaydet. Karşılanmayan soruları, açık kaldıklarını belirterek listele.

2. Bit–taşıyıcı, model–gerçekleştirme, mantıksal adım–fiziksel süre, doğrulama–geçerleme ve teknik görev–nihai gerekçe ayrımlarını bütün bölümlerde kontrol et.

3. Kaynakla desteklenen ifadeleri, kavramsal yorumları ve değer yönelimlerini ayır. Çelişkiyi ilgili bölüme dönerek düzelt veya etkisiyle birlikte açık mesele olarak kaydet.

4. Son dosyalarda bölüm sırasını, yerel bağlantıları, Türkçe karakterleri ve paket içeriğini denetle. Yalnızca gerçekten yaptığın kontrolleri sonuç olarak yaz.

5. Son sürümü, tamamlanan kapsamı, açık soruları ve yeniden değerlendirme koşullarını kaydet. Çıktılar erişilebilir ve kayıtlar tutarlıysa bu belgeleme turunu kapat.

### Beklenen çıktı

Sonuçlar, dayanaklar, geçerlilik koşulları, açık sorular, yapılan kontroller ve son dosya listesini içeren kapanış kaydı.

### Tamamlanma ölçütleri

- [ ] Başlangıç sorularının karşılıkları veya açık durumları görünürdür.
- [ ] Temel ayrımlar korunmuş; çelişkiler giderilmiş veya bunlar nedeniyle kesinleştirilmeyen sonuçlar ve açık kalan etkiler belirtilmiştir.
- [ ] Ana belge ile tekil dosyalar aynı sürümdedir ve gerçekten yapılan dosya kontrolleri kayıtlıdır.
- [ ] Açık kalan noktalar gizlenmeden mevcut çalışma turunun kapanış durumu belirtilmiştir.

### Kayıt düzeni

Kayıt alanları: Başlangıç sorularının karşılıkları; Yerleşen sonuçlar; Kaynaklar ve gerekçeler; Geçerlilik koşulları; Açık sorular ve etkileri; Gerçekten yapılan kontroller; Son dosyalar ve sürüm; Yeniden değerlendirme koşulları; Kapanış durumu.

### Sonraki adım

Mevcut belgeleme turunu kapat. Yeni bilgi veya çelişki ortaya çıkarsa ilgili protokolü yeniden aç ve değişikliği kaydet.

~~~text
  BIRBIRINE DONUSTURULMEZ
    bir iddianin kaniti  |  planlanan bir kontrol  |
    gercekten yapilmis islem  |  gozlenen sonuc

    hazirlanmis test plani    =/=   uygulanmis test
    olusturulmus protokol     =/=   gercek bir hesaplama sisteminin
                                    dogrulandigina dair sonuc
    yapilmayan denetim tamamlanmis sayilmaz

  DEVIR VE GERI DONUS

  +-------+--------------------------+---------------------------------+
  | gecis | sonrakine devredilen     | geri donus ya da guncelleme     |
  +-------+--------------------------+---------------------------------+
  | 0 > 1 | baslangic kaydi          | kapsam degisirse bu kayit       |
  |       |                          | guncellenir                     |
  | 1 > 2 | tanim                    | 0: konu tanimini degistiren     |
  |       |                          | bulgu varsa                     |
  | 2 > 3 | sinirlar ve              | 1: sistem siniri tanimi         |
  |       | belirsizlikler           | etkiliyorsa                     |
  | 3 > 4 | sure ve sira             | ilgili onceki protokol:         |
  |       | gereksinimleri           | uyusmazligin kaynagi tanim ya   |
  |       |                          | da arayuzse                     |
  | 4 > 5 | zamansal sinirlamalarin  | 2 ve 3: sure sarti yontemi ya   |
  |       | ve kosullarin kullanim   | da mimariyi degistiriyorsa      |
  |       | amaci uzerindeki etkisi  |                                 |
  | 5 > 6 | sonuclar                 | 0 ve ilgili protokoller: amac   |
  |       |                          | degisikligi kapsami etkiliyorsa |
  | 6     | belgeleme turu kapanir   | ilgili protokol: yeni bilgi ya  |
  |       |                          | da celiski ortaya cikarsa       |
  +-------+--------------------------+---------------------------------+

  BITIS SUNLARLA OZDES DEGILDIR
    Turing makinesinin durma durumu
    butun konunun sonsuza kadar cozulmesi
    kapanan sey, bu calisma turunun belgeleme ve degerlendirme
    kapsamidir
~~~

*Çizim 19 — Kökleşme: birbirine dönüştürülmeyenler; bölümler arası devir ve geri dönüş; bitişin özdeş olmadıkları.*

## Kaynaklar

[1] **ACM CCECC.** Computer Engineering (https://ccecc.acm.org/guidance/computer-engineering). Bilgisayar mühendisliğinin kapsamı ve donanım yazılım sistem ilişkisi.

[2] **Steve Ward.** The Digital Abstraction (https://computationstructures.org/notes/digitalabstraction/notes.html). Mantıksal temsil, fiziksel gerçekleştirme ve gürültü payları.

[3] **Claude E. Shannon (1948).** A Mathematical Theory of Communication (https://www.nokia.com/bell-labs/publications-and-media/publications/a-mathematical-theory-of-communication/). İletişim problemi ile anlamsal yorumun ayrılması.

[4] **A. M. Turing (1936–1937).** On Computable Numbers with an Application to the Entscheidungsproblem (https://people.csail.mit.edu/brooks/idocs/Turing_Paper_1936.pdf). Hesaplama makinesi, evrensel makine ve insanın kurallı hesaplama etkinliği.

[5] **Steve Ward.** Models of Computation (https://computationstructures.org/notes/models/notes.html). Sonlu durum makineleri, Turing modeli, bellek soyutlaması ve evrensellik.

[6] **Claude E. Shannon (1938).** A Symbolic Analysis of Relay and Switching Circuits (https://doi.org/10.1109/EE.1938.6431064). Röle ve anahtarlama devrelerinin analizi ve sentezi.

[7] **John von Neumann (30 Haziran 1945).** First Draft of a Report on the EDVAC (https://fab.cba.mit.edu/classes/862.16/notes/computation/vonNeumann-1945.pdf). Aritmetik, denetim, bellek ve giriş çıkış örgütlenmesi.

[8] **NASA.** Systems Engineering Handbook — Fundamentals of Systems Engineering (https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/). Sistem ilişkileri, gereksinimlere uygunluk ve kullanım amacına uygunluk.

[9] **Leslie Lamport (1978).** Time Clocks and the Ordering of Events in a Distributed System (https://www.microsoft.com/en-us/research/publication/time-clocks-ordering-events-distributed-system/). Nedensel olay sırası ve mantıksal saatler.

[10] **IBM Quantum Learning.** Quantum Mechanics Basics (https://quantum.cloud.ibm.com/learning/en/courses/use-a-qc-today/quantum-mechanics-basics). Kübit, süperpozisyon ve klasik durumdan ayrım.

[11] **International Energy Agency (16 Nisan 2026).** Data centre electricity use surged in 2025 even with tightening bottlenecks driving a scramble for solutions (https://www.iea.org/news/data-centre-electricity-use-surged-in-2025-even-with-tightening-bottlenecks-driving-a-scramble-for-solutions). 2026 bağlamında veri merkezlerinin enerji ve tedarik koşulları.

[12] **ACM (2018).** Code of Ethics and Professional Conduct (https://www.acm.org/binaries/content/assets/about/acm-code-of-ethics-booklet.pdf). Kamu yararına ilişkin mesleki değer yönelimi.

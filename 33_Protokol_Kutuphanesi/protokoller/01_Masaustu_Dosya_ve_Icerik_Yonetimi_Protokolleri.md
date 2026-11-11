# Masaüstü Dosya ve İçerik Yönetimi Protokolleri

**Sürüm:** 1.0\
**Tarih:** 30 Ekim 2026\
**Belge durumu:** Uygulamaya hazır protokol metni

Masaüstü Dosya ve İçerik Yönetimi, kişinin bilgisayardaki çalışma malzemesini; ne olduğu, nerede bulunduğu, hangi işe ait olduğu ve hangi durumda kullanılabileceği anlaşılır kalacak biçimde düzenleme ve sürdürme faaliyetidir. Bu bütün, Tohum ile başlayan ve Kökleşme ile kapanan bir çalışma çevrimi içinde ele alınır.

Masaüstü, kişinin bilgisayar üzerinden iş yürüttüğü dijital çalışma ortamıdır. Bu anlam, dizüstü bilgisayardaki çalışmayı da kapsar. Yerel klasörler, uygulamalar ve çalışmaya katılan bağlı depolama alanları bu ortamın parçaları olabilir. Dosya, sistemin sakladığı ve işlediği dijital nesnedir; içerik ise bu nesnenin taşıdığı bilgi veya çalışma ürünüdür.

## Kullanım

Önce 0 Tohum Protokolüyle ihtiyacı, hedef malzemeyi ve kapsamı belirle. Ardından 1–5 protokollerini işin ihtiyacına göre uygula; gerektiğinde aralarında geri dön. Numaralar kavramsal düzeni gösterir; her dosyanın aynı işlemlerden aynı sırayla geçmesini gerektirmez. Gaye, işlem seçerken de sonuç değerlendirilirken de dikkate alınır. 6 Kökleşme Protokolü belirli çalışma çevriminin sonucunu ve açık kalanlarını kaydeder.

Bir çalışma için tek uygulama kaydı yeterlidir. Başlangıç, önemli dosya veya grup rolleri, konumlar, işlemler, sürüm durumu ve sonuç bu kayıt içinde tutulabilir. Ayrıntı düzeyi malzemenin değeriyle ve çalışmanın ihtiyacıyla orantılı olmalıdır. Her dosya için ayrı kayıt oluşturmak zorunlu değildir.

Önemli bir içerik değişikliğinde gerekli önceki sürümü veya kaynak kopyayı koru. Bir malzemenin rolü, erişim konumu ya da kullanılacak sürümü belirsizse bu durumu kaydet ve ilgili protokole dön. Yapılması planlanan işlemle gerçekten uygulanan işlemi ayrı yaz.

Bu protokol metninin tamamlanmış olması masaüstünde uygulama yapıldığı anlamına gelmez. Uygulama kaydı, gerçekleştirilen işlemler ve gözlenen sonuçlarla doldurulur.

~~~text
  DOSYA                              ICERIK
  sistemin sakladigi ve              bu nesnenin tasidigi bilgi
  isledigi dijital nesne             ya da calisma urunu

  YONETIM: calisma malzemesi icin dort sey anlasilir kalir
    ne oldugu | nerede bulundugu | hangi ise ait oldugu |
    hangi durumda kullanilabilecegi

  BIR CALISMA CEVRIMI

    0 Tohum  ----->  1-5  ----->  6 Koklesme
    ihtiyac,         isin ihtiyacina      cevrimin sonucu ve
    hedef malzeme,   gore uygulanir;      acik kalanlari
    kapsam           aralarinda geri
                     donulur

    numaralar kavramsal duzeni gosterir; her dosyanin ayni
    islemlerden ayni sirayla gecmesini gerektirmez

  BIR CALISMA ICIN TEK UYGULAMA KAYDI
    ayrinti duzeyi, malzemenin degeriyle ve calismanin ihtiyaciyla
    orantilidir; her dosya icin ayri kayit zorunlu degildir

  AYRI YAZILIR
    yapilmasi planlanan islem   |   gercekten uygulanan islem
    protokol metninin tamamlanmis olmasi   -x->   masaustunde
                                                  uygulama yapilmasi
~~~

*Çizim 1 — Dosya ve içerik; anlaşılır kalan dört şey; bir çalışma çevrimi ve tek uygulama kaydı.*

Sondaki kayıt şablonunu her çalışma için yeni bir Markdown dosyasına kopyala.

## Taşıyıcı makine

**Kaynak soru:** Masaüstü Dosya ve İçerik Yönetimi'nin köken aldığı varlık, mekan, usül, zaman, ve gayeyi taşıyan makine kimdir? Kim değildir?

Teknik taşıyıcı, işletim sistemi ve uygulamalarıyla çalışan kişisel bilgisayardır. Beş boyutun birlikte anlam kazandığı bütün ise kullanıcının bir işi yürütmek için kurduğu masaüstü çalışma sistemidir. Bilgisayar teknik gövdeyi, işletim sistemi çalışma zeminini, dosya yöneticisi ve içerik uygulamaları iş görme araçlarını sağlar. Kullanıcı ve yürütülen iş, amaçların ve sonuçları değerlendirme ölçütlerinin kaynağıdır.

Köken olmak ile taşıyıcı olmak aynı ilişki değildir. Bilgisayar dosyaları saklar, işlemleri yürütür ve dijital çalışma ortamının kurulmasını sağlar. Dosyaların ne anlam taşıdığı, hangi iş için kullanılacağı ve neden korunacağı ise çalışma bağlamından doğar. Bu anlam ve amaçlar makinede adlar, ilişkiler, durumlar ve kurallar biçiminde temsil edilebilir. İnsanın bu çalışma bütününde yer alması, insanı teknik makineye indirgemek anlamına gelmez.

Bu çerçevede makine, kullanıcının amaçlarını dosya ve içerikler üzerinde uygulanabilir işlemlere dönüştüren bilgisayar düzeneğidir. Tek başına dosya yöneticisi, depolama alanı veya işletim sistemi beş boyutun bütününü karşılamaz. Kullanıcı teknik makinenin kendisi değildir; otomasyon da çalışma amacının gerekçesini ortadan kaldırmaz.

~~~text
  MASAUSTU CALISMA SISTEMI  bes boyutun birlikte anlam kazandigi butun

   .--------------------------------------------------------------.
   | kullanici ve yurutulen is     amaclarin ve sonuclari         |
   |                               degerlendirme olcutlerinin     |
   |                               kaynagi                        |
   |--------------------------------------------------------------|
   | dosya yoneticisi ve           is gorme araclari              |
   | icerik uygulamalari                                          |
   |--------------------------------------------------------------|
   | isletim sistemi               calisma zemini                 |
   |--------------------------------------------------------------|
   | bilgisayar                    teknik govde                   |
   `--------------------------------------------------------------'

  KOKEN OLMAK ILE TASIYICI OLMAK AYNI ILISKI DEGILDIR
    bilgisayar          dosyalari saklar, islemleri yurutur,
                        calisma ortaminin kurulmasini saglar
    calisma baglami     dosyalarin ne anlam tasidigi, hangi is icin
                        kullanilacagi, neden korunacagi buradan dogar

    bu anlam ve amaclar makinede su bicimlerde temsil edilebilir:
      adlar . iliskiler . durumlar . kurallar

  TEK BASINA BES BOYUTUN BUTUNUNU KARSILAMAZ
    dosya yoneticisi . depolama alani . isletim sistemi

  kullanici teknik makinenin kendisi degildir;
  otomasyon da calisma amacinin gerekcesini ortadan kaldirmaz
~~~

*Çizim 2 — Taşıyıcı makine: masaüstü çalışma sisteminin dört katı; köken ile taşıyıcı ayrıdır.*

## 0 Tohum (Başlangıç) Protokolü

**Protokol soruları:** Bu çalışma hangi ihtiyaçtan doğar? Başlangıcı mümkün kılan nelerdir? Neler değildir?

### Tanım ve ayırt edici özellikler

Tohum Protokolü, masaüstünde yürütülecek dosya ve içerik yönetimi çalışmasının hangi ihtiyaçtan doğduğunu, hangi malzemeyi kapsadığını ve hangi sonuca yöneldiğini başlangıç kaydı hâline getirir. Sonraki protokollerin hangi sorudan ve hangi mevcut durumdan hareket edeceği burada açıklığa kavuşur.

Başlangıçta bir soru, ihtiyaç veya sorun bulunabilir. Uygun kaynakları toplamak, benzer belgeler arasından kullanılacak sürümü ayırt etmek veya tamamlanmış bir projenin malzemelerini yeniden kullanılabilir hâle getirmek böyle başlangıçlara örnektir. Kullanıcının belirtmediği bir sorun varmış gibi kabul edilmez; dile getirilen ihtiyaç eldeki malzemeyle ilişkilendirilir.

Çalışma hedefi bir dosya, dosya grubu, klasör, uygulama içindeki içerik alanı veya belirli bir projeye ait malzemeler olabilir. Hedefin yeri ve kapsamı anlaşılır biçimde kaydedilir. Aynı bilgisayarda erişilebilir olan diğer malzemeler kendiliğinden çalışma kapsamına girmez.

Mevcut durum ile beklenen sonuç ayrı yazılır. Hangi malzemenin bulunduğu ve hakkında nelerin bilindiği mevcut durumu; çalışma sonunda neyin bulunabilir, ayırt edilebilir veya kullanılabilir olmasının beklendiği ise yönelimi açıklar. Belirsiz kalan ilişkiler kaydedilir. Başlangıçtaki ihtiyaç, sonraki kararların gerekçesiyle bağlantısını korur.

Tohum, konunun nasıl bir mesele olarak ortaya çıktığını açıklar. Varlık Protokolü ele alınan şeyin kimliğini, Gaye Protokolü ise onun hizmet ettiği amacı işler. Başlangıç gerekçesi, varlık tanımı ve nihai gaye birbiriyle ilişkilidir; aynı soruya cevap vermez.

### Sınırlar

Tohum, bütün sistemin ayrıntılarının baştan tasarlanması veya bütün dosyaların önceden sınıflandırılması değildir. Bilgisayarın açılması ya da boş bir klasör oluşturulması, başlangıcın açıklığa kavuştuğunu tek başına göstermez.

Somut hedef belirlenmemişse bu aşama, kapsamı ve açık soruları kaydeder; dosyaları değiştiren uygulamaya geçilmez. Çalışmanın konusu yalnızca kavramsal bir belge üretmekse hedef, o belgenin içeriği ve beklenen açıklık olarak belirlenebilir.

~~~text
   IHTIYAC              HEDEF MALZEME               KAPSAM
   soru, ihtiyac        bir dosya, dosya grubu,     .----------------.
   ya da sorun   --->   klasor, uygulama     --->   | kapsama giren  |
   (kullanicinin        icindeki icerik alani       `----------------'
    dile getirdigi)     ya da bir projenin            kapsama girmeyen
                        malzemeleri

   ayni bilgisayarda erisilebilir olan diger malzemeler
   kendiliginden calisma kapsamina girmez

  AYRI YAZILIR
    mevcut durum                       beklenen sonuc
    hangi malzeme var,          --->   calisma sonunda ne bulunabilir,
    hakkinda ne biliniyor              ayirt edilebilir ya da
                                       kullanilabilir olacak

  UC PROTOKOL, UC AYRI SORU
    0 Tohum     konu nasil bir mesele olarak ortaya cikti?
    1 Varlik    ele alinan seyin kimligi nedir?
    5 Gaye      hangi amaca hizmet eder?

  TOHUM SUNLAR DEGILDIR
    butun sistemin ayrintilarinin bastan tasarlanmasi
    butun dosyalarin onceden siniflandirilmasi
    bilgisayarin acilmasi . bos bir klasor olusturulmasi

  somut hedef belirlenmemisse kapsam ve acik sorular kaydedilir;
  dosyalari degistiren uygulamaya gecilmez
~~~

*Çizim 3 — Tohum: ihtiyaç, hedef malzeme ve kapsam; üç protokolün üç ayrı sorusu.*

### Taşıyıcı makine

Kullanıcı çalışma ihtiyacını ve kapsamı belirler; bilgisayar başlangıç kaydını saklamayı, hedef malzemeyi bulmayı ve mevcut durumu incelemeyi sağlar. Bir uygulamanın açılması veya bir komutun hazır olması, hangi işin neden yapılacağını kendiliğinden belirlemez.

### Giriş koşulu

Dosya veya içerikle ilgili bir çalışma ihtiyacı ya da açıklığa kavuşturulacak bir soru bulunur. Hedef malzemenin, erişim durumunun ve beklenen sonucun belirlenmesi bu protokolün işidir.

### Masaüstünde uygulama

1. Başlangıç ihtiyacını bir paragrafla yaz. Çalışmayı başlatan soruyu, mevcut durumu ve beklenen sonucu birbirinden ayır.
2. Somut çalışma hedefini seç. İlgili dosya, klasör, uygulama alanı veya proje kapsamını; yeniden bulunmasına yetecek yol ya da erişim bilgisiyle kaydet.
3. Başlangıç kararını vermeye yetecek düzeyde inceleme yap. Bilinen roller, ayırt edilemeyen sürümler ve önemli kaynak ilişkilerini belirle; bilinmeyenleri belirsiz olarak bırak.
4. Kapsama giren ve girmeyen malzemeyi, yapılması gereken işlemleri ve korunması gereken ilişkileri yaz. Değişiklik yapılacaksa gerekli başlangıç adını, konumunu veya sürümünü kaydet.
5. Beklenen sonucu gözlenebilir biçimde ifade et. Örneğin paylaşılmış raporun çalışma taslağından ayırt edilebilmesi veya bir kaynağa yeniden ulaşılabilmesi kullanılabilir bir hedeftir.
6. Başlangıç kaydını tamamla. Hedefi ve kapsamı belirginleşen çalışma için ilgili 1–5 protokollerine geç; açık kalan başlangıç sorularını kayıtta tut.

### Üretilen kayıt

Çalışma konusu, başlangıç gerekçesi, hedef malzeme, erişim konumu, mevcut durum, kapsam, beklenen sonuç ve açık soruları içeren başlangıç kaydı.

### Tamamlanma ölçütü

Çalışmayı sürdürecek kişi hangi malzemeyi neden ele alacağını ve hangi sonucun beklendiğini anlayabiliyorsa başlangıç tamamdır. Hedef veya kapsam hâlâ belirsizse kayıt bu eksikliği gösterir; dosyaları değiştiren uygulama için hazırlık tamamlanmış sayılmaz.

## 1 Varlık Protokolü

**Kaynak sorular:** Nedir? Onu o yapan nelerdir? Neler değildir?

### Tanım ve ayırt edici özellikler

Masaüstü Dosya ve İçerik Yönetiminin konusu, bilgisayardaki dijital çalışma malzemesidir. Belgeler, görseller, tablolar, ses kayıtları, çizimler ve notlar bu malzemeyi oluşturabilir. Yönetim, bunları bulunabilir, ayırt edilebilir, anlaşılabilir ve kullanılabilir durumda tutan faaliyetleri kapsar.

Dosya ile içerik bire bir örtüşmek zorunda değildir. Aynı raporun düzenlenebilir belgesi ve PDF çıktısı iki ayrı dosyadır; aynı çalışmanın farklı kullanım biçimlerini taşırlar. Bir dosya birden fazla içerik öğesi barındırabilir. Uygulama içindeki bir not veya kayıt da kullanıcıya bağımsız bir dosya olarak görünmeden yönetilebilir.

Bu alanın kimliği, dijital nesne ile onun anlamının ve yapılacak işin ilişkilendirilmesinden doğar. Dosyanın adı, uzantısı veya konumu, onun ne işe yaradığını bütünüyle açıklamayabilir. İçeriğin konusu, kaynağı, hangi çalışmayla ilişkili olduğu ve kullanım durumu da bu kimliğe katılır.

Aynı belge bir çalışmada kaynak, başka bir çalışmada teslim edilecek çıktı, başka bir durumda geçmişte alınmış bir kararın kaydı olabilir. Yönetim, malzemenin bu rollerini anlaşılır tutar. Nereye konacağı, nasıl adlandırılacağı, hangi sürümünün kullanılacağı, ne zaman güncelleneceği ve ne için saklanacağı hakkında kararlar verilir.

Örneğin bir raporu ilgili klasöre taşımak dosya düzeyinde bir işlemdir. Bunun belirli bir çalışmanın paylaşılmış sürümü olduğunu belirtmek ise içerik ve iş bağlamını yönetir. Böylece dosyanın bulunmasıyla birlikte, bulunan dosyanın hangi kullanım için uygun olduğu da açıklığa kavuşur.

Kimlik ile kalite ayrı değerlendirilir. Eksik veya tutarsız yürütülen bir düzenleme faaliyeti de dosya yönetimi olabilir. Yönetimin iyi işlemesi, malzemeye ulaşmayı, onu anlamayı ve uygun biçimde kullanmayı ne ölçüde desteklediğiyle değerlendirilir.

### Sınırlar

Bu alan tek bir uygulamanın adı değildir. Dosya yöneticisi, arama aracı ve içerik uygulamaları farklı parçalarını destekleyebilir. Klasör oluşturma, dosya taşıma ve ekrandaki simgeleri azaltma tek başlarına alanın bütününü karşılamaz. Görsel düzen, gerekli belgenin uygun sürümüne ulaşılabildiğini göstermez.

Yedekleme ve eşitleme, dosyaların korunmasını ve farklı yerlerden kullanılmasını destekler. Hangi belgenin hangi işe ait olduğunu ve hangi durumda kullanılabileceğini ayrıca açıklamak gerekir. İçerik üretimi de alanın bütünüyle aynı değildir: Metni yazmak üretim, taslağın, kaynakların, çıktıların ve sürümlerin düzenlenmesi yönetim boyutudur.

Düzenlenmiş olmak, içeriğin doğru olduğunu kendiliğinden kanıtlamaz. Kaynağın ve kullanım durumunun açıklığa kavuşturulması, belgedeki bütün iddiaların doğrulanmasıyla eş tutulamaz.

~~~text
  DOSYA ILE ICERIK BIRE BIR ORTUSMEK ZORUNDA DEGILDIR

    bir calisma, iki dosya            bir dosya, birden cok icerik
    .---------.                       .---------------------.
    | rapor   |---- duzenlenebilir    |  oge  .  oge  . oge |
    |         |     belge             `---------------------'
    |         |---- PDF ciktisi
    `---------'                       dosya gorunmeden yonetilen icerik
                                      uygulama icindeki bir not ya da
                                      kayit

  AYNI BELGE, FARKLI ROLLER
    bir calismada kaynak . baska bir calismada teslim edilecek cikti .
    baska bir durumda gecmiste alinmis bir kararin kaydi

    kullanilabilecek rol adlari:
      kaynak | calisma taslagi | duzenlenebilir ana belge |
      paylasilmis cikti | gecmis isin kaydi | belirsiz

  IKI DUZEY
    raporu ilgili klasore tasimak         dosya duzeyinde bir islem
    onun paylasilmis surum oldugunu       icerik ve is baglamini
    belirtmek                             yonetir

  ESITLENMEZ
    ayni ad               -x->   ayni icerik
    ayni icerik           -x->   ayni kullanim
    gorsel duzen          -x->   uygun surume ulasilabilmesi
    duzenlenmis olmak     -x->   icerigin dogru olmasi
    kimlik                 |     kalite  (ayri degerlendirilir)
~~~

*Çizim 4 — Varlık: dosya ile içerik bire bir örtüşmez; aynı belgenin farklı rolleri; eşitlenmeyenler.*

### Taşıyıcı makine

Bilgisayar dosyaları ve içeriğin dijital biçimlerini saklar, işler ve erişilebilir kılar. Bu nesnelerin kaynak, taslak, paylaşılmış çıktı veya tamamlanmış işin kaydı olarak taşıdığı anlam, yürütülen çalışmayla ilişkisine bağlıdır. Makine bu rolleri kaydedebilir ve onlara göre işlem yapabilir.

Beş boyutu taşıyan bütün, tek başına işlemci, bellek veya depolama değildir. İşletim sistemi temel zemini, uygulamalar işlemlerin araçlarını sağlar. Kullanıcı teknik makinenin kendisi değildir; amaç kuran, anlamlandıran ve sonuçları değerlendiren taraftır.

### Giriş koşulu

Tohum kaydında çalışma konusu ve hedef malzeme belirlenmiştir. İnceleme, bu kapsamla ilişkili dosya ve içerikler üzerinde yürütülür.

### Masaüstünde uygulama

1. Çalışmaya katılacak dosya ve içerikleri belirle. Uygulama içindeki not veya kayıtları da ihtiyaç ölçüsünde kapsama al.
2. Önemli malzemelerin iş içindeki rollerini açıkla. Kaynak, çalışma taslağı, düzenlenebilir ana belge, paylaşılmış çıktı veya geçmiş işin kaydı gibi tanımlar kullan; belirsiz rolü belirsiz olarak kaydet.
3. Ad ve uzantı rolü açıklamıyorsa önizleme veya içerik incelemesi yap. Aynı adı aynı içerikle, aynı içeriği aynı kullanımla eşitleme.
4. Kaynaklarla türetilmiş çıktılar arasındaki önemli ilişkileri kaydet. Düzenlenebilir rapor ile paylaşılmış PDF'nin neden birlikte tutulduğunu gerektiğinde kısa bir açıklamayla belirt.

### Üretilen kayıt

Çalışma malzemelerinin ne olduğunu, hangi rolü üstlendiğini ve hangi önemli ilişkilere sahip olduğunu gösteren kayıt. Benzer rollerdeki dosyalar ihtiyaç uygunsa grup olarak açıklanabilir.

### Tamamlanma ölçütü

Malzemenin rolleri anlaşılırdır; belirsiz veya çelişkili roller görünür durumdadır. Gereksiz kopya kararı yalnızca ad, biçim veya dosya sayısına dayandırılmamıştır.

## 2 Mekan Protokolü

**Kaynak sorular:** Nerededir? Bu yeri, oraya has bir yer yapan nelerdir? Neler değildir?

### Yer ve ayırt edici özellikler

Masaüstü Dosya ve İçerik Yönetimi, kullanıcının dijital çalışma malzemesine eriştiği ve onun üzerinde işlem yaptığı çalışma alanında gerçekleşir. Bu yer, saklama konumu, erişim ve düzenleme ortamı ile iş içindeki yer olmak üzere üç katmanda anlaşılır.

Saklama konumu, dosyanın nerede tutulduğunu anlatır. Bilgisayar diski, haricî disk, ortak depolama ve bulut alanı bu katmana örnektir. Erişim ve düzenleme ortamı, kullanıcının dosyayı nereden bulduğunu ve nasıl işlediğini anlatır; dosya yöneticisi, arama veya belge uygulaması bu işlevi görebilir. İş içindeki yer ise malzemenin hangi çalışmaya ve role ait olduğunu açıklar.

Bir rapor teknik olarak ortak depolamada saklanabilir, bilgisayardaki bir uygulamadan açılabilir ve bir projenin teslim edilmiş çıktısı olarak kullanılabilir. Dosyanın adresi, erişim yolu ve iş içindeki yeri bağlantılıdır; ancak farklı sorulara cevap verir.

Bu ortamı belirginleştiren, kullanıcının işini doğrudan burada yürütmesidir. Dosyalar okunur, karşılaştırılır, değiştirilir, başka uygulamalara aktarılır ve yeni çıktılara dönüştürülür. Bir çalışma, metin belgesi, tablo, görsel ve sunum gibi farklı malzemeleri bir araya getirebilir.

Uygulamalar arasında kaynak ve çıktı ilişkileri kurulur. Yerel ve bağlantılı kaynaklar aynı çalışmaya katılabilir. Düzen, yürütülen işe göre anlam kazanır; araştırma, tasarım veya öğrenme çalışmasının malzemeleri ve erişim yolları farklılaşabilir. Kullanıcının okuyabildiği, değiştirebildiği ve paylaşabildiği alanlar da birbirinden farklı olabilir.

Bu özelliklerin her biri başka ortamlarda görülebilir. Alanın kendine özgülüğü, bunların kişinin günlük bilgisayar çalışması içinde bir araya gelmesidir. Erişilebilir olan her şeyin o çalışmanın malzemesi sayılması gerekmez; ilişkiyi yürütülen iş belirler.

### Sınırlar

Bu mekân fiziksel çalışma masası veya kâğıt dolabı değildir. İşletim sistemindeki Masaüstü klasörü de ortamın yalnızca olası bölümlerinden biridir. Masaüstü sözcüğü burada belirli bir cihaz türüne indirgenmez; dizüstü bilgisayardaki dijital çalışma da aynı kapsamda bulunabilir.

Alan yalnızca bilgisayarın kendi diskiyle sınırlı değildir. Çalışmaya katılan bağlı ve uzak dosyalar da kapsama girebilir. Buna karşılık bütün internet, bütün bulut hizmetleri veya bütün kurumsal bilgi sistemi kendiliğinden bu çalışma alanına dönüşmez.

Sunucu, ağ ve işletim sistemi yönetimi, bu ortamın altyapısını sağlayan ayrı faaliyetlerdir. Dosya ve içerik yönetimi bu faaliyetlerle kesişebilir; onların bütününü kapsamaz.

~~~text
  YER UC KATMANDA ANLASILIR  (bir rapor ornegiyle)

   IS ICINDEKI YER                  hangi calismaya ve role ait?
   .----------------------------.
   | bir projenin teslim        |
   | edilmis ciktisi            |
   `----------------------------'
               |
   ERISIM VE DUZENLEME ORTAMI       nereden bulunuyor, nasil isleniyor?
   .----------------------------.
   | bilgisayardaki bir         |   dosya yoneticisi . arama .
   | uygulamadan acilir         |   belge uygulamasi
   `----------------------------'
               |
   SAKLAMA KONUMU                   nerede tutuluyor?
   .----------------------------.
   | ortak depolamada           |   bilgisayar diski . harici disk .
   | saklanir                   |   ortak depolama . bulut alani
   `----------------------------'

   dosyanin adresi, erisim yolu ve is icindeki yeri baglantilidir;
   ama farkli sorulara cevap verir

  BU MEKAN SUNLAR DEGILDIR
    fiziksel calisma masasi ya da kagit dolabi
    yalnizca isletim sistemindeki Masaustu klasoru
    yalnizca bilgisayarin kendi diski
    butun internet, butun bulut hizmetleri ya da butun kurumsal
    bilgi sistemi

  erisilebilir olan her sey o calismanin malzemesi sayilmaz;
  iliskiyi yurutulen is belirler
~~~

*Çizim 5 — Mekan: yer üç katmanda anlaşılır; saklama konumu, erişim ortamı, iş içindeki yer.*

### Taşıyıcı makine

Bilgisayar, yerel ve bağlantılı malzemeye erişilen çalışma merkezidir. İşletim sistemi ve uygulamalar; klasörler, arama yolları, içerik alanları ve bağlantılar üzerinden bu mekânı kullanılabilir kılar. Teknik konum ile iş bağlamı, aynı çalışma düzeninde birlikte taşınır.

Dosya yöneticisi bu düzenle etkileşime girilen araçlardan biridir. Tek başına bir klasör ağacı, depolama alanı veya uygulama penceresi, çalışma mekânının bütününü açıklamaz. Ortamın sınırını, masaüstünde dosya ve içerikle yürütülen belirli çalışma ilişkisi oluşturur.

### Giriş koşulu

Çalışma kapsamındaki malzeme ve temel rolleri belirlenmiştir. Yer kaydı, bu malzemeye günlük kullanımda nasıl ulaşılacağını açıklamak için hazırlanır.

### Masaüstünde uygulama

1. Önemli malzemenin saklama konumunu, erişildiği uygulama veya yolu ve ait olduğu çalışma bağlamını ayırarak kaydet.
2. Günlük kullanım için bir giriş noktası belirle. Bu, çalışma klasörü, uygulama içindeki alan veya ilgili belgelere bağlantı veren bir başlangıç dosyası olabilir.
3. Düzenleme gerekiyorsa ihtiyaca uygun yöntemi seç. Taşıma, bağlantı oluşturma veya mevcut konumu açıklama seçeneklerinden yeterli olanı kullan; bütün malzemeyi tek yere kopyalamayı zorunlu sayma.
4. Düzenleme sonrasında önemli dosyaları belirlenen giriş noktasından yeniden aç. Gereken bağlantıların ve okuma ya da düzenleme erişiminin çalışmayı desteklediğini kontrol et.

~~~text
  GUNLUK KULLANIM ICIN BIR GIRIS NOKTASI

    calisma klasoru | uygulama icindeki bir alan |
    ilgili belgelere baglanti veren bir baslangic dosyasi

   .---------------------------.
   | baslangic dosyasi         |
   |                           |        .-------------------------.
   |  rapor (duzenlenebilir) --+------> | bilgisayar diski        |
   |  rapor (paylasilmis)    --+----.   `-------------------------'
   |  veri tablosu           --+--. |   .-------------------------.
   |  kaynak belgeler        --+. | `-> | ortak depolama          |
   `---------------------------'| |     `-------------------------'
                                | |     .-------------------------.
                                | `---> | bulut alani             |
                                |       `-------------------------'
                                |       .-------------------------.
                                `-----> | harici disk             |
                                        `-------------------------'

  duzenleme gerekiyorsa yeterli olan secilir
    tasima | baglanti olusturma | mevcut konumu aciklama
    butun malzemeyi tek yere kopyalamak zorunlu sayilmaz

  duzenlemeden sonra onemli dosyalar giris noktasindan yeniden
  acilir; erisilemeyen ya da baglantisi cozulemeyen ogeler
  acik is olarak kaydedilir
~~~

*Çizim 6 — Mekan: günlük kullanım için bir giriş noktası; her şeyi tek yere kopyalamak gerekmez.*

### Üretilen kayıt

Çalışmanın giriş noktasını, önemli konumlarını ve malzemenin iş bağlamını açıklayan yer kaydı.

### Tamamlanma ölçütü

Gerekli malzemeye belirlenen yoldan erişilebiliyor ve teknik konumla çalışma bağlamı ayırt edilebiliyorsa yer düzeni kullanılabilir durumdadır. Erişilemeyen veya bağlantısı çözülemeyen öğeler açık iş olarak kaydedilir.

## 3 Usül Protokolü

**Kaynak sorular:** Nasıl işler yapar? Bu yaptıklarını, ona has yapan nelerdir? Neler değildir?

### İşleyiş ve ayırt edici özellikler

Masaüstü Dosya ve İçerik Yönetimi, dijital malzemenin konumunu, tanımlanma biçimini, ilişkilerini ve kullanım durumunu düzenleyen işlemlerle yürür. Edinme veya oluşturma, tanıma, adlandırma, düzenleme, bulma, değiştirme, paylaşma ve saklama bu işleyişin parçalarıdır.

Malzeme edinildiğinde veya oluşturulduğunda, hangi ihtiyaç için çalışma alanına girdiği belirlenir. Tanıma sırasında içeriği, kaynağı ve ilgili olduğu iş anlaşılır. Adlandırma ve düzenleme, malzemenin nasıl ayırt edileceğini ve nereden bulunacağını belirler; klasör, etiket veya bağlantı bu amaçla kullanılabilir.

Bulma ve seçme, mevcut ihtiyaç için uygun belgeyi veya sürümü belirlemeye yönelir. Değişikliklerin yönetilmesi, neyin değiştiğini ve hangi sürümün hangi kullanım için uygun olduğunu açıklığa kavuşturur. Paylaşma veya dışa aktarma sırasında içeriğin biçimi, kullanılacak sürümü ve erişim koşulları belirlenir.

Saklama, arşivleme ve kaldırma kararları, malzemenin bundan sonraki değeri ve rolüyle ilgilidir. Etkin çalışmada kalması, ileride başvurulmak üzere korunması veya artık gerekli görülmemesi bu değerlendirmeye bağlıdır.

Bu işlemler değişmez bir sıra oluşturmaz. Bir belge yeniden düzenlenebilir, arşivdeki kayıt yeni bir çalışmanın kaynağı olabilir ve içerik hiç taşınmadan bağlantılar veya etiketlerle düzenlenebilir. Yönetimin biçimi, çalışma ihtiyacına göre değişir.

Teknik komut ile yönetim kararı farklı açıklama düzeyleridir. Bir dosyanın taşınması komutun sonucudur; tamamlanmış çalışmanın kaydı olduğu için ilgili alana alınması ise kararın gerekçesidir. İşlemi bu alana ait kılan, kullanım gerekçesiyle kurduğu bağdır.

Teknik benzerlik ile iş bakımından eşdeğerlik de ayrılır. Aynı isimli iki dosya farklı içerikler taşıyabilir. Aynı içeriğin iki kopyası farklı amaçlarla tutulabilir. Düzenlenebilir kaynak ile paylaşılmış çıktı, aynı çalışmaya ait olsalar da farklı roller üstlenir.

Yönetim tek dosyayla birlikte ilişkilerini de gözetir. Bir tablo raporun kaynağı, bir görsel projenin parçası veya bir çıktı başka çalışmanın dayanağı olabilir. Düzen, bu ilişkileri koruduğu ve sonraki kullanımı desteklediği ölçüde işe yarar.

### Sınırlar

Amaçtan bağımsız toplu taşıma veya yeniden adlandırma işlemleri, tek başlarına kullanışlı bir düzen oluşturmaz. Yalnızca uzantıya göre ayırmak da içeriğin iş içindeki rolünü açıklamaz. Aynı biçimdeki dosyalar farklı işlere, farklı biçimlerdeki dosyalar aynı çalışmaya ait olabilir.

Her içeriği baştan sona yeniden okumak veya yazmak zorunlu değildir. Gerekli anlama düzeyi işe göre değişir; kimi durumda ad ve önizleme, kimi durumda ayrıntılı inceleme gerekir. Otomasyon ve yapay zekâ uygulama yöntemleridir; alanın varlık koşulu değildir.

İşlem, klasör veya etiket sayısının artması kendi başına başarı değildir. Düzenleme, malzemeyi sonraki kullanımda bulmayı, anlamayı ve işe katmayı kolaylaştırmasıyla değerlendirilir.

### Taşıyıcı makine

Makine komutları ve tanımlanmış kuralları uygulanabilir işlemlere dönüştürür. Usul, yazılımın sunduğu imkânlarla çalışma kurallarının ve alışkanlıkların birleşiminden oluşur. Kurallar açıkça tanımlanabilir veya kullanıcının çalışma biçiminde bulunabilir.

Tamamlanmış raporun paylaşılmış sürümünü korumak bir çalışma kuralıdır. Yazılım bu kuralı kopya oluşturma, durum işaretleme veya sürüm saklama işlemiyle uygulayabilir. Otomasyon işlemin yürütülmesini devralabilir; işlemin değerini belirleyen çalışma gerekçesini ortadan kaldırmaz.

### Giriş koşulu

Yapılacak iş, hedef malzeme ve ilgili konumlar yeterince anlaşılmıştır. Gerekli sürüm kararı henüz verilmemişse Zaman Protokolüne dönülür.

### Masaüstünde uygulama

1. Yapılacak işlemi ve gerekçesini yaz. Yeniden adlandırma, taşıma, ilişkilendirme, sürüm ayırma veya çıktı oluşturmanın hangi kullanım ihtiyacına hizmet ettiğini belirt.
2. İhtiyacı karşılayan işlemi seç. Mevcut malzemeyi açıklamak veya ona bağlantı vermek yeterliyse ek taşıma ya da kopyalama işlemi ekleme.
3. Değişiklikten önce gerekli ad ve konum bilgisini kaydet; korunması gereken kaynak sürümünü muhafaza et. Hedefte aynı adlı dosya bulunuyorsa onun rolünü incele; farklı malzemeyi üzerine yazarak belirsizliği giderme.
4. İşlemi sonucu izlenebilir bir çalışma parçası üzerinde uygula. Kaynak ve çıktı ilişkisini koru; benzer görünen fakat farklı roller taşıyan kopyaları otomatik olarak birleştirme.
5. Sonucu yeniden açarak veya ilgili çalışma yolunu izleyerek kontrol et. Önemli işlemi, sonucunu ve giderilemeyen belirsizliği kaydet.

~~~text
  ISLEYISIN PARCALARI  degismez bir sira olusturmaz

    edinme ya da olusturma . tanima . adlandirma . duzenleme .
    bulma . degistirme . paylasma . saklama

    bir belge yeniden duzenlenebilir; arsivdeki kayit yeni bir
    calismanin kaynagi olabilir; icerik hic tasinmadan baglantilar
    ya da etiketlerle duzenlenebilir

  IKI ACIKLAMA DUZEYI

    TEKNIK KOMUT                      YONETIM KARARI
    dosya tasindi                     tamamlanmis calismanin kaydi
    (komutun sonucu)                  oldugu icin ilgili alana alindi
                                      (kararin gerekcesi)

    islemi bu alana ait kilan, kullanim gerekcesiyle kurdugu bagdir

  TEKNIK BENZERLIK, IS BAKIMINDAN ESDEGERLIK DEGILDIR
    ayni isimli iki dosya             farkli icerikler tasiyabilir
    ayni icerigin iki kopyasi         farkli amaclarla tutulabilir
    duzenlenebilir kaynak ile         ayni calismaya aittir;
    paylasilmis cikti                 farkli roller ustlenir

  DEGISIKLIKTEN ONCE
    gerekli ad ve konum bilgisi kaydedilir
    korunmasi gereken kaynak surumu muhafaza edilir
    hedefte ayni adli dosya varsa rolu incelenir;
    ustune yazarak belirsizlik giderilmez

  KENDI BASINA BASARI DEGILDIR
    islem, klasor ya da etiket sayisinin artmasi .
    amactan bagimsiz toplu tasima ya da yeniden adlandirma .
    yalnizca uzantiya gore ayirmak
~~~

*Çizim 7 — Usül: işleyişin parçaları; teknik komut ile yönetim kararı; teknik benzerlik ile iş eşdeğerliği.*

### Üretilen kayıt

Önemli değişikliklerin ne olduğunu, neden yapıldığını ve hangi kontrolle değerlendirildiğini gösteren işlem kaydı. Gerekli olduğunda eski ve yeni ad veya konum birlikte yer alır.

### Tamamlanma ölçütü

Uygulanan işlemler gerekçeleriyle açıklanmış, sonuçları ilgili kullanımda kontrol edilmiş ve gözlenen sonuç kaydedilmişse bu çevrimin usul kontrolü tamamdır. Beklenen sonucu vermeyen işlem tamamlanmış çözüm olarak gösterilmez.

## 4 Zaman Protokolü

**Kaynak sorular:** Hangi andadır? Bu anı, diğer zamanlardan farklı yapan nelerdir? Neler değildir?

### An ve ayırt edici özellikler

Masaüstü Dosya ve İçerik Yönetiminin zamanı, iş akışı içindeki durumlar ve karar anları üzerinden anlaşılır. Faaliyetin tek bir başlangıç saati veya bitiş tarihi yoktur. Dosyanın çalışmayla ilişkisi kurulurken, kullanılırken ve değişirken yönetim sürer.

Malzeme geldiğinde veya oluşturulduğunda, ne olduğu, nereden geldiği ve hangi işe ait olduğu soruları belirginleşir. Kullanılacağı zaman, ihtiyaç duyulan belgenin ve uygun sürümün hangisi olduğu önem kazanır. Değiştirildiğinde, neyin değiştiği ve önceki durumla ilişkinin nasıl korunacağı gündeme gelir.

Paylaşılmadan önce, kullanıma hazır içeriğin ve karşı tarafın göreceği sürümün belirlenmesi gerekir. İş tamamlandığında, çıktılarla kaynakların ve çalışma sırasında oluşan malzemenin sonraki rolleri değerlendirilir. Yeniden başvurulduğunda ise içeriğin hâlâ gerekli olup olmadığı ve yeni bir işte nasıl kullanılabileceği anlaşılır.

Bir anı diğerlerinden farklı kılan, dosyanın iş içindeki rolünün veya ona yönelik ihtiyacın değişmesidir. Yeni gelen belge henüz bağlamlandırılmamış olabilir. Taslak değişime açıktır. Paylaşılacak çıktı belirli bir kullanım için seçilmiştir. Tamamlanmış işin kaydı, daha sonra ne yapıldığını anlamaya hizmet eder.

Aynı işlem farklı aşamalarda farklı anlamlar taşır. Taslağı değiştirmek çalışmanın olağan bir parçasıyken, daha önce paylaşılmış sürümde yapılan değişiklik hangi içeriğin paylaşılmış olduğunun ayrıca anlaşılabilir kalmasını gerektirebilir.

Teknik zaman ile işin zamanı ayrılır. Oluşturulma ve değiştirilme tarihleri teknik olaylara ilişkin bilgi verir. Taslak, kullanıma hazır, paylaşılmış veya artık etkin kullanılmıyor gibi durumlar ise dosyanın çalışma içindeki yerini anlatır. Bu durumlar tarihlerle ilişkili olabilir; tarihlerle özdeş değildir.

Yönetim yalnızca kararların verildiği saniyelerde var olmaz. Adlar, klasörler, bağlantılar, erişim düzeni ve saklama tercihleri işlemler arasında da etkisini sürdürür. Arşivdeki bir belge yeni ihtiyaç doğduğunda tekrar etkin çalışmaya katılabilir.

### Sınırlar

Bu zaman yalnızca dağınıklıktan sonraki temizlik anı değildir. İlk adlandırma ve yerleştirme de yönetimdir. Faaliyet yalnızca dosyanın oluşturulmasıyla sınırlanmaz; kullanım, değişiklik, paylaşım ve yeniden kullanım boyunca sürer.

En son değiştirilmiş dosya, her durumda kullanılacak sürüm değildir. Kaydedilmiş olmak tamamlanmış olmakla, eşitlenmiş olmak da onaylanmış olmakla eş tutulamaz. Teknik işlemin gerçekleşmesi, belgenin iş bakımından hangi durumda olduğunu tek başına açıklamaz.

Arşivleme mutlak son değildir. Etkin kullanımın sona ermesi, içeriğin bütün değerinin ortadan kalktığı anlamına gelmez. Saklanan bir kayıt daha sonraki çalışmanın başlangıç malzemesi olabilir.

~~~text
  IKI AYRI ZAMAN

   TEKNIK ZAMAN   teknik olaylara iliskin bilgi verir

     olusturuldu     degistirildi     kaydedildi     esitlendi
        *---------------*----------------*--------------*------->

   ISIN ZAMANI    dosyanin calisma icindeki yerini anlatir

     taslak  --->  kullanima  --->  paylasilmis  --->  artik etkin
                   hazir                               kullanilmiyor
                                                            |
                         yeni ihtiyac dogarsa  <------------'
                         tekrar etkin calismaya katilabilir

   bu durumlar tarihlerle iliskili olabilir; tarihlerle ozdes degildir

  ES TUTULAMAZ
    en son degistirilmis dosya   -x->   kullanilacak surum
    kaydedilmis olmak            -x->   tamamlanmis olmak
    esitlenmis olmak             -x->   onaylanmis olmak

  KARAR ANLARI
    malzeme geldiginde . kullanilacagi zaman . degistirildiginde .
    paylasilmadan once . is tamamlandiginda . yeniden basvuruldugunda

  AYNI ISLEM, FARKLI ASAMADA FARKLI ANLAM
    taslagi degistirmek                 calismanin olagan parcasi
    paylasilmis surumu degistirmek      hangi icerigin paylasildigi
                                        ayrica anlasilir kalmalidir

  arsivleme mutlak son degildir
~~~

*Çizim 8 — Zaman: teknik zaman ile işin zamanı; eş tutulamayan üç çift.*

### Taşıyıcı makine

Bilgisayar ve kullanılan yazılımlar teknik olayları, değişiklikleri ve destekledikleri ölçüde sürümleri kaydedebilir. İşin hangi aşamada olduğuna ilişkin durumlar da sisteme tanımlanabilir. Böylece teknik olayların zamanı ile çalışmanın yaşam döngüsü ilişkilendirilir.

Çalışmanın tamamlandığına veya içeriğin kullanıma hazır olduğuna ilişkin ölçüt, yürütülen işten gelir. Makine bu ölçüte göre işlem yapabilir. Yalnızca bir tarih kaydı veya kaydetme olayı, bu ölçütün karşılandığına dair yeterli açıklama değildir.

### Giriş koşulu

Mevcut çalışma ihtiyacı ve kullanılacak malzeme bilinmektedir. Sürüm veya durum seçimi, bu ihtiyaca göre değerlendirilir.

### Masaüstünde uygulama

1. Teknik tarihleri iş durumundan ayır. Oluşturulma ve değiştirilme tarihlerini taslaklık, kullanıma hazır olma veya onaylanma için tek başına kanıt sayma.
2. Mevcut kullanım için uygun sürümü belirle ve seçim gerekçesini kaydet. Paylaşılmış sürüm, düzenlemeye açık belge veya dayanak alınan kayıt birbirinden anlaşılabilsin.
3. Önemli durum değişikliğinde kısa kayıt bırak. Taslağın kullanıma hazır olması, paylaşım veya etkin çalışmadan çıkarılma gibi geçişlerin tarihini ve iş bakımından anlamını belirt.
4. Yeniden değerlendirmeyi gerektiren koşulu belirle. Yeni veri, değişen kaynak veya yeni kullanım ihtiyacı gibi bir koşul yeterli olabilir. Sabit tarih veya aralık gerekiyorsa gerekçesini kaydet.

### Üretilen kayıt

Kullanılacak sürümü, mevcut iş durumunu, önemli durum geçişlerini ve gerekiyorsa yeniden değerlendirme koşulunu açıklayan durum kaydı.

### Tamamlanma ölçütü

Mevcut iş için hangi sürümün kullanılacağı ve bunun gerekçesi anlaşılırdır. Kaydetme, eşitleme ve tamamlanma birbirinden ayrılmıştır. Kararlaştırılamayan sürüm veya durum, tamamlanmış gibi işaretlenmez.

## 5 Gaye Protokolü

**Kaynak sorular:** Hangi nihai amaca hizmet eder? Bu nihai amaca ulaştıran nelerdir? Neler değildir?

### Amaç ve amaca ulaştıran koşullar

Masaüstü Dosya ve İçerik Yönetimi, kişinin veya ekibin ihtiyaç duyduğu bilgi ve çalışma ürünleriyle işini anlaşılır, güvenilir ve sürdürülebilir biçimde yürütebilmesine hizmet eder. Faaliyetin değeri, yürütülen çalışmaya yaptığı katkıyla belirlenir.

İç amaç, dijital malzemeyi bulunabilir, ayırt edilebilir, anlaşılabilir ve kullanılabilir tutmaktır. Daha üst amaç ise öğrenmek, araştırmak, üretmek, karar vermek, birlikte çalışmak veya bir sorumluluğu yerine getirmek gibi insan faaliyetlerinden gelir. Dosya düzeni, bu faaliyetlerin gerçekleşmesine katkısıyla anlam kazanır.

Nihai amacı yalnızca hızla tanımlamak dar kalır. Bazen gerekli belgeyi hızla bulmak, bazen yanlış sürümü kullanmamak, bazen de aylar sonra bir çalışmanın nasıl oluştuğunu anlayabilmek önemlidir. Kullanımın ihtiyacı, yönetimden beklenen katkıyı belirler.

Bulunabilirlik, gerekli malzemeye ihtiyaç doğduğunda ulaşabilmektir. Ayırt edilebilirlik, benzer adlar, kopyalar, taslaklar ve çıktılar arasından uygun olanı seçebilmektir. Bağlamın korunması, içeriğin hangi işe ait olduğunu, neden üretildiğini ve ne için saklandığını anlayabilmeyi sağlar.

Değişikliklerin anlaşılması, gerektiğinde hangi sürümün kullanıldığını ve neyin değiştiğini açıklayabilmektir. Kullanılabilirlik, içeriği gereken biçimde açmayı, işlemeyi ve uygun kişilere sunmayı kapsar. Süreklilik, ara verilen, devredilen veya yeniden başlayan bir çalışmayı eldeki malzemeyle sürdürebilmektir.

Ölçülülük, düzenleme için harcanan emeğin malzemenin değeri ve kullanım ihtiyacıyla uyumlu olmasıdır. Bir kez kullanılacak geçici çıktı ile uzun süre başvurulacak temel bir proje kaydının aynı ayrıntıyla düzenlenmesi gerekmeyebilir. Yönetim de zaman ve dikkat kullandığı için kendi yüküyle birlikte değerlendirilir.

### Sınırlar

Boş veya görsel olarak kusursuz bir masaüstü, mümkün olan en az dosya sayısı ve bütün dosyaları tek konumda toplamak kendi başlarına nihai amaç değildir. Hiçbir şeyi silmeden saklamak, her dosyaya çok sayıda etiket eklemek, bütün işlemleri otomatikleştirmek ve her durumda en yeni dosyayı kullanmak da bağımsız başarı ölçütleri değildir.

Bu tercihler belirli işlerde yararlı olabilir. Değerleri, gerekli içeriğe ulaşmayı ve işi yürütmeyi ne ölçüde desteklediklerine bağlıdır. Görünüş uğruna anlaşılır düzeni bozmak, dosyaları bağlamlarından koparmak, kullanılacak sürümü belirsiz bırakmak ve düzenleme işini asıl çalışmayı engelleyecek kadar ağırlaştırmak amaca ulaşmayı güçleştirebilir.

~~~text
  UST AMAC  insan faaliyetlerinden gelir
    ogrenmek . arastirmak . uretmek . karar vermek .
    birlikte calismak . bir sorumlulugu yerine getirmek
              ^
              |  katkisiyla anlam kazanir
              |
  IC AMAC   dijital malzemeyi su durumda tutmak
    bulunabilir . ayirt edilebilir . anlasilabilir . kullanilabilir

  AMACA ULASTIRAN YEDI KOSUL
    bulunabilirlik         ihtiyac dogdugunda ulasabilmek
    ayirt edilebilirlik    benzerler arasindan uygun olani secebilmek
    baglamin korunmasi     hangi ise ait, neden uretildi,
                           ne icin saklaniyor
    degisikliklerin        hangi surum kullanildi, ne degisti
    anlasilmasi
    kullanilabilirlik      gereken bicimde acmak, islemek, sunmak
    sureklilik             ara verilen, devredilen ya da yeniden
                           baslayan calismayi surdurebilmek
    olcululuk              harcanan emek, malzemenin degeri ve
                           kullanim ihtiyaciyla uyumlu

  KENDI BASINA NIHAI AMAC DEGILDIR
    bos ya da gorsel olarak kusursuz bir masaustu .
    mumkun olan en az dosya sayisi . her seyi tek konumda toplamak .
    hicbir seyi silmeden saklamak . cok sayida etiket .
    butun islemleri otomatiklestirmek .
    her durumda en yeni dosyayi kullanmak
~~~

*Çizim 9 — Gaye: iç amaç ile üst amaç; amaca ulaştıran yedi koşul; nihai amaç olmayanlar.*

Bu sistemin kapsamı, bütün bilgi kullanımı veya insanın bütün düşünme faaliyeti değildir. Kapsam, masaüstü ortamında dosya ve içerikle yürütülen belirli çalışmayla sınırlıdır.

### Taşıyıcı makine

Makineye belge bulma, belirli sürümü koruma veya tamamlanan işin malzemelerini ilgili alana taşıma gibi hedefler verilebilir. Bu işlem hedeflerinin neden değerli olduğu, araştırmayı tamamlama, kararı dayanaklarıyla koruma, işi devretme veya yeniden sürdürme gibi gayelerden gelir.

Makine gayeyi, davranışını yönlendiren hedefler ve kurallar biçiminde taşır. Sistemin işlem seçmesi veya otomatik karar vermesi, verilen hedeflerin neden değerli olduğunu bağımsız biçimde belirlediği anlamına gelmez. Kullanıcı ve yürütülen iş, sonuçları değerlendirme ölçütünü sağlar.

Bir dosya taşıma işlemi teknik olarak başarıyla tamamlanabilir; yanlış belge taşındığı için çalışma yine de aksayabilir. İşlemin gerçekleşmesi ile gayeye hizmet etmesi arasındaki fark, işin anlamıyla belirlenir.

Bir araştırma raporunda kaynak belgeler, notlar, veri tablosu, düzenlenebilir rapor ve paylaşılmış çıktı farklı roller üstlenir. Aylar sonra hangi verilerin kullanıldığını, hangi sürümün paylaşıldığını ve çalışmanın nereden sürdürülebileceğini anlamak mümkünse, dosya ve içerik yönetimi o çalışmaya somut bir katkı sağlamıştır.

### Giriş koşulu

Tohum kaydındaki beklenen sonuç bilinmektedir. Bu protokol, işlem seçerken de sonuç değerlendirilirken de kullanılabilir.

### Masaüstünde uygulama

1. Beklenen kullanım sonucunu açıkla. Genel bir düzen isteğini, raporu uygun sürümü ve kaynaklarıyla yeniden sürdürebilmek gibi gözlenebilir bir sonuca bağla.
2. Bu sonuç için gerekli ölçütleri seç. Uygun belgeyi bulmak, paylaşılmış sürümü ayırt etmek veya işi başka bir oturumda sürdürebilmek işe bağlı örneklerdir.
3. Malzemeyle ilgili gerçek bir kullanım adımını dene. Gerekli belgeyi bul, uygun sürümü aç ve ihtiyaç duyulan kaynak veya çıktıya ulaş.
4. Gözlenen faydayla düzenlemenin ek yükünü birlikte değerlendir. İşe katkısı olmayan ayrıntıları azalt; karşılanmayan ihtiyacı ilgili protokole geri taşı ve kapanış için kaydet.

~~~text
  BIR ARASTIRMA RAPORU  bes malzeme, bes ayri rol

    kaynak belgeler ----.
    notlar -------------+---->  duzenlenebilir  ---->  paylasilmis
    veri tablosu -------'       rapor                  cikti

  AYLAR SONRA SORULAN UC SORU
    hangi veriler kullanildi?
    hangi surum paylasildi?
    calisma nereden surdurulebilir?

    bunlari anlamak mumkunse, dosya ve icerik yonetimi o calismaya
    somut bir katki saglamistir

  ISLEMIN GERCEKLESMESI, GAYEYE HIZMET ETMESI DEGILDIR
    dosya tasima islemi teknik olarak basariyla tamamlanir;
    yanlis belge tasindigi icin calisma yine de aksayabilir

  MAKINE GAYEYI NASIL TASIR?
    davranisini yonlendiren hedefler ve kurallar biciminde
    sistemin islem secmesi ya da otomatik karar vermesi, hedeflerin
    neden degerli oldugunu bagimsiz bicimde belirledigi anlamina gelmez

  KULLANIM KONTROLU
    gercek bir kullanim adimi denenir: gerekli belgeyi bul,
    uygun surumu ac, ihtiyac duyulan kaynaga ya da ciktiya ulas
    gozlenen fayda ile duzenlemenin ek yuku birlikte degerlendirilir
~~~

*Çizim 10 — Gaye: araştırma raporu örneği; işlemin gerçekleşmesi ile gayeye hizmet etmesi.*

### Üretilen kayıt

Beklenen sonucu, yapılan kullanım kontrolünü, gözlenen faydayı ve açık kalan ihtiyaçları gösteren değerlendirme kaydı.

### Tamamlanma ölçütü

İşlemin gerçekleşmesiyle kullanım sonucuna ulaşılması ayrı değerlendirilmiştir. Karşılanan ihtiyaç gözlenen bir örnekle açıklanır; karşılanmayan ihtiyaç Kökleşme kaydına açık iş olarak aktarılır.

## 6 Kökleşme (Bitiş) Protokolü

**Protokol soruları:** Çalışma sonunda ne kökleşti? Sonucun kullanılabilirliğini ve bu çevrimin bitişini gösteren nelerdir? Neler değildir?

### Tanım ve ayırt edici özellikler

Kökleşme Protokolü, çalışma sonunda elde edilen durumun başlangıç ihtiyacıyla ilişkisini değerlendirir ve sonucu sonraki kullanıma elverişli bir kayıt hâline getirir. Varlık, Mekan, Usül, Zaman ve Gaye protokollerindeki ayrımlar birlikte gözden geçirilir. Malzemenin ne olduğu, nerede bulunduğu, hangi işlemlerden geçtiği, hangi durumda kullanılacağı ve neye hizmet ettiği anlaşılır kalır.

Bitiş, belirli bir çalışma çevriminin kapanmasıdır. Dosya ve içeriklerin bütün yaşamının sona ermesi anlamına gelmez. Çalışma tamamlanmış, kısmen tamamlanmış veya belirli bir nedenle durdurulmuş olabilir. Kapanış kaydı bu durumları ayırır; yapılmayan işlemi yapılmış, incelenmeyen sonucu doğrulanmış gibi göstermez.

Kavramsal kökleşme, kullanılan tanımların ve kararların tutarlı ve başvurulabilir olmasıdır. Uygulamadaki kökleşme ise ortaya çıkan düzenin gerçekten kullanılabilmesidir. Bir protokolün yazılması, dosyalar üzerindeki işlemlerin gerçekleştirildiğini kanıtlamaz. Uygulama yapılmışsa sonuç, ilgili malzemeye erişilerek ve iş için önemli özellikler kontrol edilerek değerlendirilir.

Tamamlanan işlemler, çıktıların yerleri, korunması gereken ilişkiler ve açık kalan meseleler aynı çalışma kaydında tutulur. Çalışmanın yeniden açılması gerektiğinde bu kayda başvurulur. Yeni bir ihtiyaç, değişen içerik veya geçerliliğini yitiren bir karar, yeni çevrimin Tohum kaydına başlangıç olabilir.

Gaye Protokolü faaliyetin hangi amaca hizmet ettiğini açıklar. Kökleşme Protokolü, belirli çalışmanın sonunda ne elde edildiğini, bu sonucun hangi ölçüde işe yaradığını ve nasıl sürdürülebileceğini kaydeder. Hedef ile gerçekleşen sonuç birbirinin yerine yazılmaz.

### Sınırlar

Kökleşme, bütün dosyaları arşive taşımak, geçici malzemenin tamamını silmek veya çalışma düzenini değişmez hâle getirmek değildir. Teknik işlemin hata vermeden tamamlanması da tek başına gayeye ulaşıldığını göstermez.

Bitiş, açık soruların gizlenmesini veya gelecekteki değişikliğin engellenmesini gerektirmez. Kısmen tamamlanmış bir çalışma, eksikleri ve sonraki ihtiyacı açıkça kaydedilerek kapatılabilir. Kapanışın doğru kaydedilmesiyle başlangıçtaki bütün hedeflere ulaşılması ayrı değerlendirilir.

~~~text
  CEVRIM

        .---------------------------------------------------.
        v                                                   |
    0 Tohum  ---->  1-5  ---->  6 Koklesme  ----------------'
                                            yeni ihtiyac, degisen
                                            icerik ya da gecerliligini
                                            yitiren bir karar, yeni
                                            cevrimin Tohum kaydina
                                            baslangic olabilir

  BITIS  belirli bir calisma cevriminin kapanmasidir;
         dosya ve iceriklerin butun yasaminin sona ermesi degildir

    tamamlandi | kismi | durduruldu      (gerekcesiyle)

  IKI AYRI KOKLESME
    kavramsal        kullanilan tanimlarin ve kararlarin tutarli ve
                     basvurulabilir olmasi
    uygulamadaki     ortaya cikan duzenin gercekten kullanilabilmesi

  BIRBIRININ YERINE YAZILMAZ
    hedef                     |   gerceklesen sonuc
    yapilmayan islem          |   yapilmis islem
    incelenmeyen sonuc        |   dogrulanmis sonuc
    dosyanin diskte bulunmasi |   kontrolun yapilmis olmasi

  KOKLESME SUNLAR DEGILDIR
    butun dosyalari arsive tasimak .
    gecici malzemenin tamamini silmek .
    calisma duzenini degismez hale getirmek .
    teknik islemin hata vermeden tamamlanmasi

  kismen tamamlanmis bir calisma, eksikleri ve sonraki ihtiyaci
  acikca kaydedilerek kapatilabilir
~~~

*Çizim 11 — Kökleşme: çevrimin kapanışı ve yeni Tohum; iki ayrı kökleşme; birbirinin yerine yazılmayanlar.*

### Taşıyıcı makine

Bilgisayar son malzemeyi, işlem ve durum kayıtlarını, erişim yollarını ve gereken önceki sürümleri saklar. Kullanıcı veya görevlendirilen çalışma aracı, sonucu başlangıç ihtiyacıyla karşılaştırır. Dosyanın diskte bulunması veya bir kaydın oluşturulması, kontrolün yapıldığı anlamına gelmez; değerlendirmede gerçekten gözlenen sonuç belirtilir.

### Giriş koşulu

Başlangıç kaydı ve çalışma sırasında elde edilen bilgiler bulunur. İlgili protokoller uygulanmış veya uygulamanın neden ilerleyemediği belirginleşmiştir. Yalnızca kavramsal belge üretildiyse kapanış bu belgenin kapsamı ve tutarlılığı üzerinden yapılır.

### Masaüstünde uygulama

1. Tohum kaydındaki ihtiyacı, kapsamı ve beklenen sonucu yeniden oku. Çalışma sırasında değişen hedef varsa değişikliğin gerekçesini kaydet.
2. Ortaya çıkan durumu incele. İlgili dosyaları aç, konumları ve uygun sürümün ayırt edilebilirliğini kontrol et. İş için önemli kaynak ve çıktı ilişkilerini de gözden geçir.
3. Gerçekleşen işlemleri ve kontrol edilen özellikleri kaydet. Uygulanmamış planları veya kontrol edilmemiş sonuçları tamamlananlar arasına katma.
4. Sonucu Gaye Protokolündeki kullanım ölçütleriyle karşılaştır. Hangi ihtiyacın karşılandığını ve hangisinin açık kaldığını belirt.
5. Açık meseleleri ve yeniden açılma koşullarını yaz. Çözülemeyen sürüm, erişilemeyen kaynak veya değişen ihtiyaç varsa bir sonraki adımı kaydet.
6. Çevrimi tamamlandı, kısmi veya durduruldu olarak gerekçesiyle kapat. Kapanış tarihini, son çıktılara erişim bilgisini ve başlangıç kaydıyla bağlantısını koru.

### Üretilen kayıt

Elde edilen sonuç, yapılan işlemler, gerçekleştirilen kontroller, son çıktıların konumu, açık meseleler, yeniden açılma koşulları ve çevrim durumunu içeren kapanış kaydı.

### Tamamlanma ölçütü

Çalışmanın ne ürettiği, başlangıç ihtiyacını hangi ölçüde karşıladığı ve bundan sonra hangi malzemeye dayanılarak devam edilebileceği anlaşılır olduğunda kapanış tamamdır. Eksik kalan çalışma, kalan ihtiyacı ve nedenini kaydetmeden bütünüyle başarılı olarak kapatılmaz.

## Uygulama kaydı şablonu

Aşağıdaki alanlar her çalışma için gerçek uygulama sırasında doldurulur. Boş alanlar, yapılmış bir işlem veya doğrulanmış sonuç olarak yorumlanmaz.

Bu şablonu her çalışma için ayrı bir adla kopyala. Köşeli parantezli alanları gerçek bilgilerle doldur. Bir işlem gerçekleşmediyse veya kontrol yapılmadıysa bunu açıkça belirt. Protokol metinlerinin hazır olması, bu kayıttaki çalışmanın tamamlandığı anlamına gelmez.

```markdown
### 0 Başlangıç kaydı

- Çalışma adı: [Doldurulacak]
- Uygulayan: [Doldurulacak]
- Başlangıç tarihi: [Doldurulacak]
- Başlangıç ihtiyacı veya sorusu: [Doldurulacak]
- Mevcut durum: [Doldurulacak]
- Hedef dosyalar veya içerik alanı: [Doldurulacak]
- Hedefin yolu veya erişim bilgisi: [Doldurulacak]
- Kapsama giren işlemler: [Doldurulacak]
- Kapsam dışında kalanlar: [Doldurulacak]
- Beklenen gözlenebilir sonuç: [Doldurulacak]
- Başlangıçta açık kalan sorular: [Doldurulacak]

### 1 Malzemenin kimliği

Gerekli sayıda dosya veya grup kaydı ekle.

- Dosya, içerik veya grup: [Doldurulacak]
- İş içindeki rolü: [Doldurulacak]
- Kaynağı ve ilgili olduğu çalışma: [Doldurulacak]
- Önemli kaynak ve çıktı ilişkileri: [Doldurulacak]
- Belirsiz veya çelişkili roller: [Doldurulacak]

### 2 Yer kaydı

- Saklama konumu: [Doldurulacak]
- Erişim yolu veya uygulaması: [Doldurulacak]
- İş içindeki yeri: [Doldurulacak]
- Günlük kullanım için giriş noktası: [Doldurulacak]
- Yeniden açılarak kontrol edilen malzeme: [Doldurulacak]
- Erişilemeyen öğe veya çözülemeyen bağlantı: [Doldurulacak]

### 3 İşlem kaydı

Önemli her işlem için bu alanları çoğalt. Planlanan işlemle gerçekleşen işlemi ayrı yaz.

- İlgili malzeme: [Doldurulacak]
- Planlanan işlem ve gerekçesi: [Doldurulacak]
- Önceki ad, konum veya korunması gereken sürüm: [Doldurulacak]
- Gerçekleştirilen işlem ve tarih: [Doldurulacak veya uygulanmadı]
- Sonraki ad, konum veya sürüm: [Doldurulacak]
- Yapılan kontrol ve gözlenen sonuç: [Doldurulacak veya kontrol edilmedi]
- Açık kalan mesele: [Doldurulacak]

### 4 Durum ve sürüm kaydı

- Mevcut iş durumu: [Doldurulacak]
- Bu kullanım için seçilen sürüm: [Doldurulacak]
- Seçim gerekçesi: [Doldurulacak]
- Varsa paylaşılmış sürüm: [Doldurulacak]
- Önemli durum değişikliği ve tarihi: [Doldurulacak]
- Gerekiyorsa yeniden değerlendirme koşulu: [Doldurulacak]

### 5 Kullanım sonucu

- Beklenen sonuç ve değerlendirme ölçütü: [Doldurulacak]
- Denenen gerçek kullanım adımı: [Doldurulacak veya denenmedi]
- Gözlenen sonuç: [Doldurulacak]
- Karşılanan ihtiyaç: [Doldurulacak]
- Karşılanmayan ihtiyaç: [Doldurulacak]
- Düzenlemenin sağladığı fayda ve ek yük: [Doldurulacak]

### 6 Kapanış kaydı

- Kapanış tarihi: [Doldurulacak]
- Çevrim durumu: [Tamamlandı, kısmi veya durduruldu; uygulama sonunda seçilecek]
- Durumun gerekçesi: [Doldurulacak]
- Elde edilen sonuç: [Doldurulacak]
- Son çıktılar ve erişim bilgileri: [Doldurulacak]
- Gerçekleştirilen son kontroller: [Doldurulacak]
- Kontrol edilmemiş veya tamamlanmamış noktalar: [Doldurulacak]
- Açık meseleler ve sonraki adım: [Doldurulacak]
- Çalışmayı yeniden açtıracak ihtiyaç veya koşul: [Doldurulacak]
- Başlangıç kaydıyla ilişki veya hedef değişikliği: [Doldurulacak]
```

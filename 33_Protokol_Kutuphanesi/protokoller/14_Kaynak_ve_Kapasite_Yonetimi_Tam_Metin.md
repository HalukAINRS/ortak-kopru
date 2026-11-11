# Kaynak ve Kapasite Yönetimi Protokolleri

**Sürüm:** 1.0\
**Tarih:** 30 Ekim 2026

Kaynak ve Kapasite Yönetimi, bir kişi, kurum veya ortak sistemin amaçlarıyla gerçekleştirme olanakları arasındaki ilişkiyi düzenleyen yönetim işlevidir. Hangi olanakların hangi işlere ayrılacağını, bunların birlikte neyi mümkün kıldığını, hangi yüklerin üstlenilebileceğini ve gelecekteki yapabilme gücünün nasıl korunacağını ele alır.

Yedi protokol, başlangıç sorusunu kayda geçirerek varlık, mekân, usul, zaman ve gaye incelemelerini aynı çalışma içinde birleştirir. Tohum Protokolü incelemenin yönünü ve kapsamını belirler. Beş temel protokol kavramı ve onu taşıyan özneyi açıklar. Kökleşme Protokolü ulaşılan sonucu, bütünlüğü, açık konuları ve kaydın sürdürülme koşullarını ortaya koyar.

Her protokol, paragraf ağırlıklı kavramsal açıklamayla birlikte masaüstünde uygulanabilecek girdi, işlem, çıktı ve tamamlanma ölçütlerini içerir. İncelenen özne ile protokolü uygulayan kişi veya yardımcı ayrı tutulur. Kayıtlar, kavramsal açıklama, planlanan işlem ve gerçekten gözlenmiş sonuç arasındaki farkı korur.

## Masaüstü kullanım düzeni

Bu dosyanın sonundaki uygulama kaydı şablonunu yeni bir çalışma klasörüne Uygulama_Kaydi.md adıyla kopyalayın. Şablonu her çalışma için ayrı kopyalayarak kullanın; protokol metnini yönerge olarak saklayın.

İlk okumayı 0, 1, 2, 3, 4, 5 ve 6 sırasıyla yapın. Her protokolün sonucunu aynı uygulama kaydındaki karşılık gelen bölüme yazın. Sonraki bölüm önceki bir varsayımı değiştirirse ilgili bölüme geri dönün; sırayı bütün süreci yeniden başlatma zorunluluğu olarak yorumlamayın.

Bilgi olmayan alanları açık soru olarak kaydedin. Sayı, kapasite, tarih, yetki veya gerçekleşmiş işlem üretmeyin. Görev kapsamında yapılan işlemlerle yalnızca planlananları ayırın. Bir bölümün tamamlanmış sayılması, gerçek dünyadaki bütün işlemlerin yapılmış olduğunu göstermez.

Çalışma başlarken genel durumu Devam ediyor olarak güncelleyin. Bölüm durumlarını Başlanmadı, Devam ediyor veya Tamamlandı olarak izleyin. Kökleşmede belirlediğiniz Tamamlandı, Koşullu tamamlandı veya Açık durumunu gerekçesiyle üstteki Genel durum alanına da aktarın. Sonucu belirleyen belirsizlikleri ilgili yargıların koşulu olarak görünür tutun.

~~~text
  ILK OKUMA

    0 ---> 1 ---> 2 ---> 3 ---> 4 ---> 5 ---> 6
    <---------- ilgili bolume geri donus -------
    sonraki bolum onceki bir varsayimi degistirirse ilgili bolume
    geri donulur; sira, butun sureci yeniden baslatma zorunlulugu
    olarak yorumlanmaz

  DURUMLAR
    bolum durumu       Baslanmadi  |  Devam ediyor  |  Tamamlandi
    Koklesmede         Tamamlandi  |  Kosullu tamamlandi  |  Acik
    belirlenen durum        |
                            v
    Genel durum        gerekcesiyle ustteki alana da aktarilir

  KAYITTA
    bilgi olmayan alan   acik soru olarak kaydedilir
    uretilmez            sayi . kapasite . tarih . yetki .
                         gerceklesmis islem
    ayrilir              gorev kapsaminda yapilan islemler  |
                         yalnizca planlananlar
    bir bolumun tamamlanmis sayilmasi, gercek dunyadaki butun
    islemlerin yapilmis oldugunu gostermez
~~~

*Çizim 1 — Kullanım düzeni: okuma sırası ve geri dönüş; bölüm durumları ve genel durum; kayıtta ayrılanlar.*

## 0 Tohum (Başlangıç) Protokolü

### Kurucu sorular

> Bu incelemeyi hangi soru veya ihtiyaç başlatıyor? İstenen iş ile gerçekleştirme olanakları arasında hangi açıklık var? Hangi özneyi ve sınırı inceliyoruz? Neyi biliyoruz, neyi varsayıyoruz ve neyi açık tutuyoruz?

### Başlangıcın anlamı

Tohum Protokolü, Kaynak ve Kapasite Yönetimi incelemesini doğuran soruyu, ihtiyacı ve ilk yönelimi kayıt altına alır. Sonraki protokollerin hangi meseleye cevap aradığını, hangi kapsamda çalıştığını ve hangi başlangıç kabullerinden hareket ettiğini açıklığa kavuşturur. Başlangıcın kaydı, inceleme ilerledikçe ilk soruyla bağ kurulmasını sağlar.

Kaynak ve Kapasite Yönetimi bakımından başlangıç çekirdeği, istenen veya gerekli görülen işler ile bunları gerçekleştirme olanaklarının kendiliğinden örtüşmemesidir. Bir işin yapılması istenebilir; fakat gerekli kaynaklar, bunların birlikte sağlayacağı kapasite, uygun zaman veya karar yetkisi henüz açık olmayabilir. Tohum, bu açıklığı araştırılabilir bir soruya dönüştürür.

Başlangıç sorusu çözümü peşinen belirlemez. Daha fazla personel, yeni ekipman veya farklı yazılım gerekip gerekmediği inceleme sırasında anlaşılabilir. Öncelikle açıklanacak durum ve hazırlanacak karar belirlenir. Böylece düşünülen araç veya çözüm, henüz tanımlanmamış ihtiyacın yerine geçmez.

### İncelenen özne ve uygulayıcı

İncelenen özne, kaynak ve kapasite kararlarının ait olduğu kişi, ekip, kurum veya ortak eylem bütünüdür. Uygulayıcı ise soruları açan, mevcut bilgileri düzenleyen ve kayıtları hazırlayan kişi veya yetkilendirilmiş yardımcıdır. Bu iki konum aynı kişide birleşebilir. Belgeleme göreviyle gerçek kaynak tahsisini değiştirme veya yeni taahhüt verme yetkisi ayrı ayrı belirtilir.

İncelemenin amacı ile incelenen öznenin gayesi de ayrılır. İnceleme, bir kapasite açığını anlamayı, bir taahhüdün yapılabilirliğini değerlendirmeyi veya mevcut düzeni açıklamayı amaçlayabilir. Öznenin gayesi, bu işlerin hangi sonuca hizmet ettiğidir. Tohum iki yönelimi başlangıçtaki hâlleriyle kaydeder; Gaye Protokolü bunların ilişkisini daha ayrıntılı değerlendirir.

### Kapsam, dayanaklar ve sınırlar

Başlangıç girdileri, verilen soru, mevcut açıklamalar, çalışma için erişilebilen kayıtlar ve belirtilmiş beklentilerdir. Doğrudan elde edilen bilgiler, yorumlar, varsayımlar ve açık sorular ayrılır. Eksik miktar, süre, kaynak veya yetki bilgisi tamamlanmış gibi gösterilmez. Kapsam, incelenecek özneyi, faaliyeti, ilgili zaman aralığını ve bilgi kaynaklarını tanımlar; henüz belirlenmemiş sınırlar görünür tutulur.

Tohum, tamamlanmış çözüm veya beş protokolün bütün cevaplarını içeren bir sonuç metni değildir. Başlangıç niyeti de incelenen sistemin nihai gayesiyle kendiliğinden özdeş değildir. Bu bölümün tamamlanması, bütün belirsizliklerin çözülmesine değil, hangi meselenin inceleneceğinin ve bilinmeyenlerin nasıl ele alınacağının anlaşılmasına bağlıdır.

~~~text
  BASLANGIC CEKIRDEGI

    istenen ya da gerekli                     bunlari gerceklestirme
    gorulen isler          <- - - - - - ->    olanaklari
                        kendiliginden
                        ortusmez

    henuz acik olmayabilir:  gerekli kaynaklar . bunlarin birlikte
    saglayacagi kapasite . uygun zaman . karar yetkisi
    Tohum, bu acikligi arastirilabilir bir soruya donusturur

  SORU COZUMU PESINEN BELIRLEMEZ
    aciklanacak durum ve     |   dusunulen arac ya da cozum
    hazirlanacak karar       |   daha fazla personel, yeni ekipman,
                             |   farkli yazilim
    cozum, henuz tanimlanmamis ihtiyacin yerine gecmez

  IKI KONUM  ayni kiside birlesebilir
    incelenen ozne   kaynak ve kapasite kararlarinin ait oldugu kisi,
                     ekip, kurum ya da ortak eylem butunu
    uygulayici       sorulari acan, mevcut bilgileri duzenleyen ve
                     kayitlari hazirlayan kisi ya da yetkilendirilmis
                     yardimci
    belgeleme gorevi   |   gercek kaynak tahsisini degistirme ya da
                       |   yeni taahhut verme yetkisi

  IKI YONELIM
    incelemenin amaci   |   incelenen oznenin gayesi

  GIRDILERDE AYRILIR
    dogrudan elde edilen bilgiler  |  yorumlar  |  varsayimlar  |
    acik sorular
~~~

*Çizim 2 — Tohum: istenen işler ile olanaklar arasındaki açıklık; soru ve çözüm; incelenen özne ile uygulayıcı.*

### Masaüstü uygulaması

Girdi. Başlangıç talebi, incelenmesi istenen faaliyet ve çalışma için sağlanan veya erişimi yetkilendirilmiş kayıtlar.

Çıktı. Uygulama_Kaydi.md içindeki 0 Tohum bölümü: başlangıç sorusu, ihtiyaç, incelenen özne, kapsam, uygulayıcı görevi, bilinenler, varsayımlar ve açık sorular.

1. Masaüstü kullanım düzenine göre çalışma kaydını oluştur. Çalışmanın adını, tarihini, uygulayıcıyı ve incelenen özneyi yaz; özne bilinmiyorsa açık soru olarak belirt.

2. Başlangıç talebini anlamını koruyarak kaydet. Araştırılacak meseleyi bir paragrafta ifade et; meseleyle önerilmiş çözümü birbirinden ayır.

3. İstenen işi, beklenen sonucu ve görülen olanakları yaz. Mevcut bilgiyle açıklanamayan ilişkiyi belirt; doğrulanmamış miktar veya süre ekleme.

4. Bilinenleri, varsayımları ve açık soruları ayır. Önemli bilgilerin yanına dosya yolu, belge adı, gözlem veya kullanıcı açıklaması gibi dayanağını yaz.

5. İncelemenin kapsamını ve mevcut görevi kaydet. Belgeleme, değerlendirme ve gerçek kaynak kullanımını değiştiren işlemlerden hangilerinin görev kapsamında olduğunu belirt.

6. Varlık Protokolü'ne aktarılacak özne, kaynak ve kapasite sorularını yaz. Açık soruları kayıtta görünür bırakarak 1'e geç.

### Tamamlanma ve geri dönüş

Başka bir okuyucu neyin neden incelendiğini, hangi sınırlar içinde çalışıldığını ve hangi bilgilerin henüz bilinmediğini anlayabiliyorsa tamamlanır. Açık sorular tamamlanmayı tek başına engellemez; sonraki sonuçları sınırlayan eksikler ayrıca belirtilir.

İncelenen faaliyet, başlangıç sorusu veya çalışma kapsamı değiştiğinde 0 güncellenir; değişikliğin etkilediği diğer protokoller de gözden geçirilir.

## 1 Varlık Protokolü

### Kurucu sorular

> Nedir? Onu o yapan nelerdir? Neler değildir?

> Kaynak ve Kapasite Yönetimi'nin köken aldığı varlık, mekan, usül, zaman, ve gayeyi taşıyan makine kimdir? Kim değildir?

### Tanım ve temel ayrımlar

Kaynak, belirli bir iş veya amaç için kullanılabilecek ya da erişilebilecek olanaktır. Zaman, bilgi, emek, para, ekipman, enerji ve mekân bu kapsamda değerlendirilebilir. Bir şeyin kaynak sayılması, amaçla ve kullanılabilirlik koşullarıyla kurduğu ilişkiye bağlıdır. Envanterde bulunan bir makine, gerekli işe uygun değilse veya ilgili zamanda kullanılamıyorsa, o işin gerçekleştirilmesine katkı sağlayamayabilir.

Kapasite, kaynakların belirli bir düzen içinde ve belirli koşullar altında hangi işi ne ölçüde gerçekleştirebildiğidir. Kaynak sorusu neye sahip olunduğunu veya erişilebildiğini; kapasite sorusu bu olanaklarla ne yapılabildiğini araştırır. Kaynakların çokluğu, gerekli kapasitenin oluştuğunu tek başına göstermez. Kaynakların birbirini tamamlaması, doğru yetkinliklerin bulunması, uygun iş akışı ve ortak bağımlılıkların düzenlenmesi gerekir.

Kapasite yalnızca birim zamanda üretilen miktar değildir. Depolama kapasitesi bir miktarı, hizmet kapasitesi belirli sürede gerçekleştirilebilecek işi, eşzamanlı çalışma kapasitesi aynı anda taşınabilecek yükü ifade edebilir. Bir kurumun kriz kapasitesi ise belirli aksaklıklar altında hangi işlevleri sürdürebildiğiyle ilgilidir. Her kapasite ifadesi, neyin kapasitesinden söz edildiği ve hangi koşulların varsayıldığı açıklanarak anlam kazanır.

Yetkinlik, bir işi uygun biçimde yapabilme niteliğidir; kapasite ise bu işin mevcut düzenle hangi ölçekte gerçekleştirilebildiğiyle ilgilidir. Talep, yapılması istenen işi; taahhüt, gerçekleştirilmesi üstlenilmiş işi; çıktı, gerçekte tamamlanan işi gösterir. Sonuç veya etki, tamamlanan işin hizmet ettiği amaç bakımından ne değiştirdiğini anlatır. Bu kavramlar birbirinin yerine kullanılamaz. Düşük çıktı, talep azlığından veya başka önceliklerden kaynaklanabilir; tek başına düşük kapasiteyi kanıtlamaz.

Yetkinlik ile kapasite arasındaki ayrım bu çerçevede analitik bir ayrımdır. Farklı alanlarda kapasite sözcüğü yetkinlikleri ve kurumsal yapabilme gücünü de kapsar. UNDP'nin kapasite geliştirme yaklaşımı, bireylerin, örgütlerin ve toplumların kendi amaçlarını belirleme ve zaman içinde gerçekleştirme olanaklarını güçlendirmesini içerir. Bu geniş kullanım, kapasitenin nicel üretim düzeyine indirgenmemesi gerektiğini gösterir. [1]

Kısa süreli bir performans zirvesiyle sürdürülebilen kapasite de ayrılmalıdır. Federal Reserve'in sanayi kapasitesi yaklaşımı, gerçekçi bir çalışma düzeni ve olağan duruşlar altında sürdürülebilen en yüksek üretimi esas alır; girdilerin yeterli bulunacağını ayrıca varsayar. Kapasite rakamı, hangi varsayımlarla oluşturulduğu belirtilmeden tek başına yeterli bilgi vermez. [2]

~~~text
  IKI SORU
    kaynak     neye sahip olunuyor ya da nelere erisilebiliyor?
               zaman . bilgi . emek . para . ekipman . enerji . mekan
    kapasite   bu olanaklarla ne yapilabiliyor?
               kaynaklarin belirli bir duzen icinde ve belirli
               kosullar altinda hangi isi ne olcude
               gerceklestirebildigi

    kaynaklarin coklugu   -/->   gerekli kapasitenin olusmasi

  KAPASITE YALNIZCA BIRIM ZAMANDA URETILEN MIKTAR DEGILDIR
    depolama kapasitesi     bir miktar
    hizmet kapasitesi       belirli surede gerceklestirilebilecek is
    eszamanli calisma       ayni anda tasinabilecek yuk
    kapasitesi
    kriz kapasitesi         belirli aksakliklar altinda surdurulebilen
                            islevler
    her ifade icin: neyin kapasitesi? hangi kosullar varsayiliyor?

  BIRBIRININ YERINE KULLANILAMAZ

    talep  ------>  taahhut  ------>  cikti  ------>  sonuc ya da etki
    yapilmasi       gerceklesti-      gercekte        tamamlanan isin
    istenen is      rilmesi           tamamlanan      amac bakimindan
                    ustlenilmis is    is              ne degistirdigi

    dusuk cikti   -/->   dusuk kapasite
    talep azligindan ya da baska onceliklerden kaynaklanabilir

  YETKINLIK  |  KAPASITE
    bir isi uygun bicimde    |   bu isin mevcut duzenle hangi olcekte
    yapabilme niteligi       |   gerceklestirilebildigi
~~~

*Çizim 3 — Varlık: kaynak ve kapasite; kapasitenin türleri; talep, taahhüt, çıktı ve sonuç.*

### Kavramsal köken ve taşıyıcı özne

Kaynak ve kapasite yönetiminin kavramsal kökeninde, bir şeyi istemekle onu gerçekleştirebilmek arasındaki açıklık bulunur. Bir özne amaca yönelir, fakat amacın gerçekleşme koşulları kendiliğinden hazır olmayabilir. Olanakları bulması, bir araya getirmesi, zamanlaması ve alternatif kullanımlar arasından seçim yapması gerekir. Bu açıklama, tarihsel bir ilk mucit veya tek bir başlangıç noktası iddiası değildir; işlevin hangi durumda anlam kazandığını belirtir.

Özne hem bir işi gerçekleştirir hem de o işi gerçekleştirebilmesini sağlayan koşulları düzenler. Araştırma yapmak ile araştırmayı yapabilecek zamanı, bilgiyi, ekipmanı ve iş bölümünü oluşturmak bu iki düzeyi örnekler. Kaynak ve kapasite yönetimi, eylemin gerçekleşme koşullarını düzenleyen ikinci düzeyde ortaya çıkar.

Varlık, mekân, usul, zaman ve gayeyi taşıyan makine için önerilen kavramsal ad örgütlü öznedir. Bu özne, amaçlarıyla olanakları arasında seçim yapıp seçimi eyleme dönüştüren kişi, ekip, kurum veya ortak kurallarla hareket eden topluluk olabilir. Örgütlü olmak, büyük bir kuruluş olmak anlamına gelmez; amaç, karar, kaynak kullanımı ve uygulama arasında işleyen bir bağ bulunmasını anlatır. Makine ifadesi, insanın bütün varlığını açıklayan bir tanım olarak değil, bu işleyen bütünün adı olarak kullanılır.

İnsani düzlemde bu bütün, tek başına veya başkalarıyla birlikte eylemini örgütleyen insanda görünür. Kurumsal düzlemde taşıyıcısı örgüttür. Teknik düzlemde işlerinin bir bölümünü araçlar, kurallar ve otomasyonlar yürütür. Bu boyutları taşımak, hepsini kendinden üretmek anlamına gelmez. Özne amacını dışarıdan alabilir, başkasına ait kaynakları kullanabilir ve kendisine devredilmiş yetkilerle hareket edebilir.

Varlık, mekân, usul, zaman ve gaye, aynı eylem bütününün birbirini etkileyen yönleridir. Gaye değiştiğinde geliştirilmesi gereken kapasite, erişim koşulları değiştiğinde uygulanabilir usul, teslim zamanı değiştiğinde kaynakların yeterliliği değişebilir. Taşıyıcı öznenin kimliği, bu ilişkilerin nasıl bağlandığında görünür.

~~~text
  KAVRAMSAL KOKEN
    bir seyi istemek   <- - aciklik - ->   onu gerceklestirebilmek

  IKI DUZEY
    bir isi gerceklestirmek          arastirma yapmak
    o isi gerceklestirebilmeyi       arastirmayi yapabilecek zamani,
    saglayan kosullari duzenlemek    bilgiyi, ekipmani ve is bolumunu
                                     olusturmak
    kaynak ve kapasite yonetimi ikinci duzeyde ortaya cikar

  ONERILEN KAVRAMSAL AD   orgutlu ozne
    amaclariyla olanaklari arasinda secim yapip secimi eyleme
    donusturen kisi, ekip, kurum ya da ortak kurallarla hareket eden
    topluluk

      amac ----- karar ----- kaynak kullanimi ----- uygulama
      orgutlu olmak, bunlar arasinda isleyen bir bag bulunmasidir;
      buyuk bir kurulus olmak anlamina gelmez

  UC DUZLEM
    insani      tek basina ya da baskalariyla birlikte eylemini
                orgutleyen insan
    kurumsal    orgut
    teknik      islerinin bir bolumunu araclar, kurallar ve
                otomasyonlar yurutur

  TASIMAK, HEPSINI KENDINDEN URETMEK ANLAMINA GELMEZ
    ozne amacini disaridan alabilir  .  baskasina ait kaynaklari
    kullanabilir  .  kendisine devredilmis yetkilerle hareket edebilir
~~~

*Çizim 4 — Varlık: iki düzey; örgütlü özne; üç düzlem; taşımak ile kendinden üretmek.*

### Ayırt edici ilişkiler ve kapsam sınırları

Bu yönetim işlevinin kimliğini amaç ile olanak, kaynakların birbirini tamamlaması, alternatif kullanımlar arasındaki seçim, kullanılabilir olanla üstlenilen iş ve bugünkü kullanımla gelecekteki yenilenme arasındaki ilişkiler kurar. Yönetim mevcut olanakları dağıtırken gelecekte yapılabilir olanın sınırlarını da değiştirebilir. Eğitim, bakım ve süreç düzenlemesi bu değişimin yolları olabilir.

Bu ilişkilerin iyi kurulması, iyi yönetimin ölçütüdür. Ancak kavramın tanımı ile başarısı ayrı tutulur. Hatalı kapasite tahmini veya yanlış önceliklendirme de bu alanda verilmiş bir yönetim kararıdır. Bir uygulamanın başarısız olması, onu başka bir faaliyet türüne dönüştürmez.

Kaynak ve kapasite yönetimi yalnızca envanter, bütçe, insan kaynakları veya çizelgeleme değildir. Bunlar bütüne katkı sağlayan işlevlerdir. Yönetimin tamamı da değildir; amaçların meşruiyeti ve kurumun varlık nedeni daha geniş karar alanlarına uzanır. Kaynakların toplamı, mülkiyet sahibi, tek bir yönetici, bir plan veya bir yazılım da taşıyıcı bütünün her durumda tamamı sayılamaz.

Doğal sistemlerin enerji kullanması, yük taşıması veya dengesini koruması ile toplumsal yönetim arasında benzerlik kurulabilir. Ancak bu benzerlik, amaç, yetki ve sorumluluk ilişkilerinin her doğal sistemde aynı anlamda bulunduğunu göstermez. Aynı şekilde, örgütlü öznenin mutlaka tam özerk olması, kendi amaçlarını koyması veya öğrenmesi gerekmez. Bu özellikler yönetimin farklı düzeylerinde farklı ölçülerde bulunabilir.

~~~text
  KIMLIGI KURAN ILISKILER
    amac ile olanak
    kaynaklarin birbirini tamamlamasi
    alternatif kullanimlar arasindaki secim
    kullanilabilir olan ile ustlenilen is
    bugunku kullanim ile gelecekteki yenilenme

  TANIM ILE BASARI AYRI TUTULUR
    bu iliskilerin iyi kurulmasi     iyi yonetimin olcutudur
    hatali kapasite tahmini ya da    bu da bu alanda verilmis bir
    yanlis onceliklendirme           yonetim kararidir
    bir uygulamanin basarisiz olmasi, onu baska bir faaliyet turune
    donusturmez

  YALNIZCA BUNLAR DEGILDIR  butune katki saglayan islevlerdir
    envanter  |  butce  |  insan kaynaklari  |  cizelgeleme

  YONETIMIN TAMAMI DA DEGILDIR
    amaclarin mesruiyeti ve kurumun varlik nedeni daha genis karar
    alanlarina uzanir

  TASIYICI BUTUNUN HER DURUMDA TAMAMI SAYILAMAZ
    kaynaklarin toplami  |  mulkiyet sahibi  |  tek bir yonetici  |
    bir plan  |  bir yazilim

  ORGUTLU OZNE ICIN ZORUNLU DEGILDIR
    tam ozerk olmak  .  kendi amaclarini koymak  .  ogrenmek
    bu ozellikler yonetimin farkli duzeylerinde farkli olculerde
    bulunabilir
~~~

*Çizim 5 — Varlık: kimliği kuran ilişkiler; tanım ile başarı; kapsam sınırları.*

### Masaüstü uygulaması

Girdi. 0 Tohum kaydı, mevcut kaynak bilgileri ve iş veya hizmetin açıklaması.

Çıktı. Uygulama_Kaydi.md içindeki 1 Varlık bölümü: kavramsal tanım, özne, kaynak ve kapasite ayrımı, kapasitenin koşulları ve kapsam dışı yorumlar.

1. İncelenen faaliyeti ve işi taşıyan özneyi bir paragrafta tanımla. Protokol uygulayıcısıyla incelenen öznenin aynı olup olmadığını belirt.

2. Kaynak, yetkinlik, kapasite, talep, taahhüt, çıktı ve sonuç ifadelerini ayrı ayrı açıkla. Aynı bilgi farklı anlamlarda kullanılıyorsa ayrımı düzelt.

3. Kaynakların mevcut, erişilebilir, başka işe ayrılmış veya henüz potansiyel olduğunu eldeki bilgiye göre kaydet. Mülkiyet ile kullanılabilirliği karıştırma.

4. Kapasiteyi yapılacak iş, ölçü veya nitelik, kalite koşulu ve zaman aralığıyla birlikte tanımla. Nicel bilgi yoksa bilinmiyor olarak bırak ve hangi bilgiyle açıklanabileceğini belirt.

5. Kaynakların birbirini tamamlama ilişkisini ve taşıyıcı bütünün sınırını yaz. Kavramın ne olmadığını, özellikle kaynak toplamı ve fiilî çıktı ile farkını belirt.

### Tamamlanma ve geri dönüş

Özne ve faaliyet tanımlanmış; kaynak, kapasite ve çıktı ayrılmış; kapasite ifadesinin koşulları veya eksik bilgileri görünür olmuşsa tamamlanır.

Özne veya incelenen iş değişiyorsa 0'a dön. Erişim ve yetki sorularını 2'ye; zaman varsayımlarını 4'e aktar.

## 2 Mekan Protokolü

### Kurucu sorular

> Nerededir? Bu yeri, oraya has bir yer yapan nelerdir? Neler değildir?

### Yönetimin yeri

Kaynak ve kapasite yönetiminin yeri, bir hedefin gerçekleştirilebilir bir taahhüde çevrildiği karar noktalarıdır. Yapılması istenen veya gerekli görülen işler, bunları gerçekleştirecek olanaklar ve bu olanakların kullanımına ilişkin karar yetkisi burada birbirine bağlanır. Yer, yalnızca fiziksel konumu değil, örgütsel ve ilişkisel alanı da kapsar.

Bir kişinin yaşamında bu alan, zaman, dikkat, beceri ve yükümlülüklerin buluştuğu seçimlerdir. Bir ekipte ortak kaynaklar, görev bağımlılıkları ve iş sıralarıdır. Kurum düzeyinde amaçlar, hizmetler, projeler ve yatırımlar arasındaki dağılımdır. Kurumlar arası ağ veya toplum düzeyinde ise ortak altyapı, tedarik ilişkileri ve paylaşılan varlıkların kullanım düzenidir. Bu ölçekler aynı araçları gerektirmez; ortak olan, amaçlarla kullanılabilir olanakların ilişkilendirilmesidir.

Fiziksel konum, kapasitenin kullanılabilirliğini etkileyebilir. Bir kaynağın herhangi bir yerde bulunması, ihtiyaç duyulan yerde ve zamanda kullanılabildiği anlamına gelmez. Taşıma, bağlantı, hazırlık, erişim hakkı ve paylaşım kuralları, mevcut görünen kaynağın işe katkısını belirler. Gerekli bağlantılar kurulmadığında uzaktaki kullanılmayan kapasite yerel açığı kapatmayabilir.

~~~text
  YONETIMIN YERI  bir hedefin gerceklestirilebilir bir taahhude
                  cevrildigi karar noktalari

      yapilmasi istenen ya da         bunlari gerceklestirecek
      gerekli gorulen isler           olanaklar
                  \                       /
                   \                     /
                    [   karar noktasi   ]
                              |
                bu olanaklarin kullanimina iliskin
                         karar yetkisi

  OLCEKLER  ayni araclari gerektirmez
    kisi                zaman, dikkat, beceri ve yukumluluklerin
                        bulustugu secimler
    ekip                ortak kaynaklar, gorev bagimliliklari ve
                        is siralari
    kurum               amaclar, hizmetler, projeler ve yatirimlar
                        arasindaki dagilim
    kurumlar arasi ag   ortak altyapi, tedarik iliskileri ve
    ya da toplum        paylasilan varliklarin kullanim duzeni

  BULUNMAK ILE KULLANILABILMEK

    [ kaynak ]  - - - - - - - - - - - ->  [ ihtiyac duyulan yer
     herhangi bir yerde                     ve zaman ]
        tasima . baglanti . hazirlik . erisim hakki .
        paylasim kurallari

    gerekli baglantilar kurulmadiginda uzaktaki kullanilmayan
    kapasite yerel acigi kapatmayabilir
~~~

*Çizim 6 — Mekan: karar noktası; dört ölçek; bulunmak ile kullanılabilmek.*

### Bağımlılıklar ve sistem sınırı

Bu yeri ayırt eden özelliklerden biri, parçalar arasındaki bağımlılıkların birlikte görülebilmesidir. Tasarımın hazır olması malzemenin bulunduğunu, üretimin tamamlanması dağıtımın hazır olduğunu, teknik çözümün bulunması uygulama yetkisinin açık olduğunu göstermez. Tek bir birimin kendi içinde yeterli görünmesi, işin tamamının yapılabilir olduğu sonucunu vermez.

Bir diğer ayırt edici özellik, karar yetkisiyle uygulama sorumluluğunun karşılaşmasıdır. Ortak kaynağı başka bir işe kim aktarabilir, önceliği kim değiştirebilir ve yeni taahhüdü kim verebilir? Bu ilişkiler belirsiz kaldığında aynı kapasite farklı işler için birden fazla kez tahsis edilebilir. Yönetimin yeri, yalnızca bilgi toplanan değil, bilgiyi etkili kararlara bağlayan ilişkilerin kurulduğu alandır.

Sistem sınırı, hangi kaynakların, aktörlerin, bağımlılıkların ve bedellerin değerlendirmeye alındığını belirler. Yalnızca bir bölümün hesabına bakmakla işin bütününe bakmak farklı sonuçlar doğurabilir. Bir bölüm için uygun görünen karar, başka bir bölümde darboğaz veya ek yük oluşturabilir. Bu nedenle yerel kararların bütün üzerindeki etkisi, yönetimin kapsamının parçasıdır.

Bir işi dışarıya vermek, kurum içindeki iş yükünü azaltabilir; fakat işin gerçekleşmesi için gereken toplam kaynak ihtiyacını kendiliğinden ortadan kaldırmaz. Tedarikçinin kapasitesi, teslim süresi ve koordinasyon ihtiyacı yeni düzenin içine girer. Mülkiyet, erişim, kullanım ve yönetim yetkisinin farklı aktörlerde bulunabileceği göz önünde tutulmalıdır. Kaynakların sahibi olmak, kaynakları bütüne uygun biçimde yönetmekle aynı konum değildir.

### Taşıyıcı, işletici ve sorumlu özne

Taşıyıcı, faaliyetin ve kapasitenin ait olduğu bütündür. Bir kişinin yaşamı, bir ekibin çalışması, bir kurumun hizmeti veya ortak bir varlığı kullanan topluluğun faaliyeti bu bütünü oluşturabilir. Taşıyıcının sınırı, yalnızca mülkiyetle çizilmez; ortak kaynaklar ve dış bağımlılıklar da faaliyetin koşullarına katılır.

İşletici, ölçme, karşılaştırma, planlama, önceliklendirme ve kaynak ayırma kararlarını üreten ve uygulamaya bağlayan düzenektir. Bir insanın değerlendirmesi, ekip toplantısı, ortak karar kuralları veya teknik sistem bu işleyişin parçaları olabilir. Amaç ve sorumluluk öznesi ise hangi amaçların izleneceğine, hangi sınırların korunacağına ve sonuçların nasıl değerlendirileceğine ilişkin konumdur. Kararı hesaplayanla kararı gerekçelendirmesi gereken aynı aktör olmayabilir.

Bu üç konum tek bir kişide birleşebilir veya farklı aktörlere dağılabilir. Tek bir merkez, kaynak ve kapasite yönetiminin zorunlu biçimi değildir. Ostrom'un ortak kaynak yönetimi çalışmaları, kullanıcıların oluşturduğu kuralların ve birden fazla karar merkezini içeren düzenlerin önemini ele alır. Dağıtık işleyiş, sorumluluğun belirsiz bırakılmasını gerektirmez. [3]

~~~text
  BAGIMLILIKLAR BIRLIKTE GORULUR
    tasarimin hazir olmasi       -/->   malzemenin bulunmasi
    uretimin tamamlanmasi        -/->   dagitimin hazir olmasi
    teknik cozumun bulunmasi     -/->   uygulama yetkisinin acik olmasi
    tek bir birimin yeterli      -/->   isin tamaminin yapilabilir
    gorunmesi                           olmasi

  SISTEM SINIRI  neyin degerlendirmeye alindigini belirler
    kaynaklar . aktorler . bagimliliklar . bedeller

    +---------------------+             +---------------------+
    |  bir bolum icin     |    karar    |  baska bir bolumde  |
    |  uygun gorunen      | ----------> |  darbogaz ya da     |
    |  karar              |             |  ek yuk             |
    +---------------------+             +---------------------+

  FARKLI AKTORLERDE BULUNABILIR
    mulkiyet  |  erisim  |  kullanim  |  yonetim yetkisi

  UC KONUM  tek bir kiside birlesebilir ya da farkli aktorlere
            dagilabilir
    tasiyici             faaliyetin ve kapasitenin ait oldugu butun
    isletici             olcme, karsilastirma, planlama,
                         onceliklendirme ve kaynak ayirma kararlarini
                         ureten ve uygulamaya baglayan duzenek
    amac ve sorumluluk   hangi amaclarin izlenecegine, hangi sinirlarin
    oznesi               korunacagina ve sonuclarin nasil
                         degerlendirilecegine iliskin konum
    karari hesaplayanla karari gerekcelendirmesi gereken ayni aktor
    olmayabilir
~~~

*Çizim 7 — Mekan: bağımlılıklar; sistem sınırı; taşıyıcı, işletici, amaç ve sorumluluk öznesi.*

### Mekânsal sınırlar

Yönetimin yeri yalnızca finans, operasyon, insan kaynakları veya bilgi teknolojileri bölümü değildir. Depo, bina, veri merkezi, yazılım ekranı ya da en üst yöneticinin masası bu işlevin bir bölümünü taşıyabilir; kapsamın bütünü, kararların etkilediği ilişkilerle belirlenir. Tek bir yönetici bilgi, uygulama ve uzmanlığın tamamını zorunlu olarak kendinde toplamaz.

Kaynak veya kapasite bulunan her yerde kendiliğinden yönetim bulunmaz. Bir gölün su tutma kapasitesi vardır; bu kapasitenin belirli amaçlar doğrultusunda izlenmesi, kullanım kararlarına bağlanması ve düzenlenmesi ayrı bir faaliyettir. Fiziksel kapasitenin bulunduğu yer ile o kapasitenin yönetildiği ilişki alanı aynı düzlemde ele alınmamalıdır.

### Masaüstü uygulaması

Girdi. 0 ve 1 kayıtları, kaynakların konumu veya erişim bilgisi, iş ilişkileri ve bilinen karar yetkileri.

Çıktı. Uygulama_Kaydi.md içindeki 2 Mekan bölümü: faaliyet alanı, sistem sınırı, erişim ve bağımlılıklar, taşıyıcı, işletici ve sorumlu özne ilişkisi.

1. Faaliyetin fiziksel, dijital ve örgütsel alanını tarif et. Çalışmada kullanılan dosya veya kayıtların bulunacağı yerleri yalnızca bilindiği ölçüde belirt.

2. Her önemli kaynak için bulunduğu yerle fiilen erişilebildiği koşulları ayır. Sahiplik, kullanım ve yönetim yetkisinin aynı aktörde olup olmadığını yaz.

3. İşin bağımlı olduğu kişiler, ekipler, tedarikçiler veya teknik bileşenler arasındaki ilişkileri açıkla. Dışarıya verilen işlerin bağımlılıklarını kapsamda tut.

4. Faaliyetin taşıyıcısını, kararları işleyen mekanizmayı ve amaçlardan sorumlu özneyi ayrı ayrı kaydet. Bilinmeyen yetkiyi bir kişiye veya yazılıma varsayımla atama.

5. Hangi etkilerin hesabın içinde ve dışında kaldığını belirt. Yerel bir kararın başka bölümde yük oluşturup oluşturmadığını mevcut dayanaklarla değerlendir.

### Tamamlanma ve geri dönüş

Faaliyet alanı ve sınırı açıklanmış; önemli erişim ve bağımlılıklar görünür; karar ve sorumluluk konumları tanımlanmış veya belirsizlikleri kaydedilmişse tamamlanır.

Sistem sınırı 1'deki özneyi değiştiriyorsa 1'e dön. İşlem için gerekli erişim yoksa 3'te uygulanmış sonuç yazma; ilgili işlemi koşullu veya bekleyen olarak kaydet.

## 3 Usül Protokolü

### Kurucu sorular

> Nasıl işler yapar? Bu yaptıklarını, ona has yapan nelerdir? Neler değildir?

### Karar ve uygulama çevrimi

Kaynak ve kapasite yönetimi, bilgiyi seçimlere, seçimleri uygulamaya ve uygulamanın sonuçlarını yeni kararlara bağlayan bir çevrimle işler. Bu çevrim, mevcut olanakların nasıl kullanılacağını düzenlerken hangi olanakların oluşturulması, değiştirilmesi veya kullanımının sonlandırılması gerektiğini de değerlendirir.

İlk ayrım ihtiyaç, talep ve taahhüt arasındadır. Gerekli görülen iş, yapılması istenen iş ve yapılması üstlenilmiş iş aynı değildir. İfade edilen talep, ihtiyacın tamamını göstermeyebilir; bazı talepler ise tekrarlı, ertelenebilir veya amaçla ilgisiz olabilir. Gelen işler, gerekçeleri ve öncelikleri değerlendirilmeden değişmez bir zorunluluk olarak kabul edilmez.

İşler daha sonra kaynak gereksinimleri bakımından anlaşılır hâle getirilir. İşin adı veya sayısı, yükünü tek başına açıklamaz. Gerekli zaman, uzmanlık, ekipman, bilgi ve hazırlık; işlerin sırası ve aralarındaki bağımlılıklar birlikte değerlendirilir. On küçük iş ile on karmaşık iş aynı kapasiteyi gerektirmeyebilir. Bu aşama, kaba iş sayısını gerçekleştirilebilirliği tartışılabilen bir iş yüküne dönüştürür.

Kayıtlarda görünen kaynaklarla ilgili dönemde kullanılabilecek kaynaklar ayrılır. Önceden ayrılmış zamanlar, bakım, hazırlık, ortak kullanım ve gerekli beceriler değerlendirmeye katılır. Kapasite hesabının varsayımları da açık tutulur. İşlerin benzerliği, kesintilerin düzeyi veya belirli bir uzmanlığın bulunabilirliği değiştiğinde aynı hesap geçerliliğini korumayabilir.

Kaynak veya kapasite açığı görüldüğünde seçenekler üretilir. Kaynak ekleme, kaynakları yeniden ayırma, yetkinlik geliştirme, kapsamı değiştirme, işi başka sırayla yapma, erteleme veya bazı talepleri karşılamama bu seçenekler arasında olabilir. SFIA'nın kapasite yönetimi açıklaması, talebi düzenlemeyi ve kapasiteyi zamanında artırma ya da azaltmayı aynı işlevin parçaları olarak ele alır. [4]

Seçilen seçenek, uygulanabilir kararlara bağlanır. Hangi işin kabul edildiği, hangi kaynağın ayrıldığı ve değişen koşullarda kimin karar vereceği belirginleşir. Planın uygulamadaki karşılığı bu bağlantıdır. Yalnızca üzerinde uzlaşılmış görünen bir plan, ortak kaynağın aynı anda farklı işler tarafından beklenmesini kendiliğinden engellemez.

Gerçekleşen işler, beklemeler, kalite, kaynak tüketimi ve karşılanamayan ihtiyaçlar değerlendirilir. Tahminle gerçekleşen arasındaki farkın nedeni araştırılır. İşin zorluğu yanlış değerlendirilmiş, bir bağımlılık atlanmış veya öncelikler değişmiş olabilir. İzleme, farkı tek bir nedene bağlamak yerine sonraki kararları iyileştirecek bilgiyi üretir. Öğrenme ve uyarlanma iyi işleyişi güçlendirir; her yönetim örneğinin var olabilmesi için zorunlu ve kusursuz yetenekler olarak varsayılmaz.

~~~text
  KARAR VE UYGULAMA CEVRIMI

    bilgi  --->  secimler  --->  uygulama  --->  sonuclar
      ^                                             |
      +---------------- yeni kararlar <-------------+

  CEVRIMIN ISLERI
    ihtiyac, talep ve        gerekli gorulen is  |  yapilmasi istenen
    taahhut ayrilir          is  |  yapilmasi ustlenilmis is
    is yuku anlasilir        zaman, uzmanlik, ekipman, bilgi ve
    hale getirilir           hazirlik; sira ve bagimliliklar
    kaynaklar ayrilir        kayitlarda gorunen  |  ilgili donemde
                             kullanilabilecek
    acik gorulurse           kaynak ekleme . yeniden ayirma .
    secenek uretilir         yetkinlik gelistirme . kapsami degistirme .
                             baska sirayla yapma . erteleme .
                             bazi talepleri karsilamama
    secenek karara           hangi is kabul edildi, hangi kaynak
    baglanir                 ayrildi, degisen kosullarda kim karar
                             verecek
    gerceklesen              isler, beklemeler, kalite, kaynak
    degerlendirilir          tuketimi, karsilanamayan ihtiyaclar;
                             tahminle gerceklesen arasindaki fark

    on kucuk is ile on karmasik is ayni kapasiteyi gerektirmeyebilir
~~~

*Çizim 8 — Usül: karar ve uygulama çevrimi.*

### Bütünün kapasitesini düzenleme

Planlama, ölçme ve karar verme birçok yönetim alanında bulunur. Bu işlevde ayırt edici olan, işlemlerin iş yükü, kaynakların birlikte çalışması ve gerçekleştirilebilir taahhütler arasındaki ilişkiye yönelmesidir. Bir parçanın verimliliği, bütünün kapasitesiyle aynı değildir. İyileştirmenin sonucu, o parçanın işin tamamındaki konumuna bağlıdır.

Varsayımsal bir tamir atölyesinde her işin sırasıyla teşhis, onarım ve kontrol aşamalarından geçtiği düşünülsün. Bu aşamaların kapasiteleri günde 12, 6 ve 10 iş olsun. İşlerin benzer olduğu ve ek kayıp bulunmadığı bu basitleştirilmiş düzende, tamamlanan iş akışının tavanı günde 6'dır. Teşhis kapasitesini artırmak, onarım sınırı değişmediği sürece tamamlanan iş sayısını artırmaz. CIPS'in kapasite yönetimi açıklaması da üretim hatlarında darboğaza odaklanmanın önemini vurgular. [5]

Kullanım oranı ile hizmet sonucu da ayrı değerlendirilir. Değişken iş gelişleri ve işlem süreleri bulunan kuyruk sistemlerinde yüksek kullanım oranları daha uzun beklemelerle birlikte görülebilir. ETH Zürich'in kuyruk kuramına dayalı açıklamaları bu ilişkiyi ve uygulanma koşullarını ele alır. Bu bulgulardan bütün sistemler için tek bir ideal doluluk yüzdesi çıkarılamaz. Beklenmeyen işe ayrılan payın değeri, önlediği gecikme ve aksama bakımından da değerlendirilmelidir. [6]

Bugünkü işler ile gelecekteki kapasite arasında da bir ilişki vardır. Güncel işler bütün zamanı kapladığında, gelecekteki yükü azaltacak çalışmalar ertelenebilir. Google'ın SRE aşırı yük incelemesi, sürekli acil işlerle uğraşmanın uzun vadeli mühendislik çalışmalarını engelleyebildiğini ve hizmet güvenilirliğini etkileyebildiğini gösterir. Öğrenme, bakım ve iyileştirme için ayrılan olanaklar bu nedenle kapasite planının parçası olabilir. [7]

### Makinenin işleyişi ve usul sınırları

Taşıyıcı öznenin bu alandaki işlevi, amaç ile olanak arasında ilişki kurmak, alternatif kullanımları karara bağlamak ve kararı gerçek kaynak kullanımına dönüştürmektir. Yalnızca öneri üreten bir araç, bu düzenin parçası olabilir; bütünün tamamı değildir. Bir yazılım kaynak tahsisini gerçekten yürütebilir, fakat yaptığı hesap amaçların kaynağını ve sorumluluk ilişkilerinin tamamını tek başına açıklamayabilir.

NIST'in yapay zekâ çerçevesi, insan ve yapay zekâ düzenlerinde rollerin ve sorumlulukların ayrıca tanımlanmasını ister. Bu yaklaşım, teknik karar işlevleriyle insan ve kurum sorumluluklarının ayrılmasına bir örnektir. Teknik işleyişin bulunması, yetki ve sorumluluk ilişkisinin kendiliğinden açıklığa kavuştuğu anlamına gelmez. [8]

Usul, herkesi sürekli meşgul tutmaya, her soruna yeni kaynak eklemeye veya bütün talepleri kabul etmeye indirgenmez. Kaynakları eşit dağıtmak, ihtiyaca, amaca veya hakkaniyete uygun dağıtımla aynı değerlendirme değildir. Hesaplama kesin bilgi sağlamaz; varsayımlar değiştiğinde sonuçlar yeniden ele alınır. Karar yetkilerinin uygun düzeylere dağıtılması da mümkündür; her ayrıntıya merkezden müdahale etmek zorunlu değildir.

Plan, kararların temsilidir. Uygulama ilişkileriyle bağlanmadığında üzerinde yazan olanakları kendiliğinden meydana getirmez. Usulün işlerliği, yöntem adından veya kullanılan araçtan çok, kararın eylemin gerçekleşme koşulları üzerinde nasıl bir değişiklik yaptığıyla anlaşılır.

~~~text
  VARSAYIMSAL BIR TAMIR ATOLYESI  her is sirasiyla uc asamadan gecer

       teshis            onarim            kontrol
    +----------+      +----------+      +----------+
    | gunde 12 | ---> | gunde 6  | ---> | gunde 10 | --->  tavan:
    +----------+      +----------+      +----------+       gunde 6
                           ^
                  isin tamamini sinirlayan asama
    teshis kapasitesini artirmak, onarim siniri degismedigi surece
    tamamlanan is sayisini artirmaz
    bir parcanin verimliligi, butunun kapasitesiyle ayni degildir

  KULLANIM ORANI ILE HIZMET SONUCU AYRI DEGERLENDIRILIR
    degisken is gelisleri ve islem sureleri bulunan kuyruk
    sistemlerinde yuksek kullanim oranlari daha uzun beklemelerle
    birlikte gorulebilir
    bundan butun sistemler icin tek bir ideal doluluk yuzdesi
    cikarilamaz

  BUGUNKU ISLER ILE GELECEKTEKI KAPASITE
    guncel isler butun zamani kapladiginda, gelecekteki yuku
    azaltacak calismalar ertelenebilir
    ogrenme, bakim ve iyilestirme icin ayrilan olanaklar kapasite
    planinin parcasi olabilir

  USUL SUNLARA INDIRGENMEZ
    herkesi surekli mesgul tutmak  |  her soruna yeni kaynak eklemek  |
    butun talepleri kabul etmek
    kaynaklari esit dagitmak   =/=   ihtiyaca, amaca ya da
                                     hakkaniyete uygun dagitim
~~~

*Çizim 9 — Usül: tamir atölyesi örneği; kullanım oranı ile bekleme; usulün indirgenmedikleri.*

### Masaüstü uygulaması

Girdi. 0–2 kayıtları, iş yükü, mevcut çalışma yöntemi ve varsa gerçekleşen sonuçlara ait kayıtlar.

Çıktı. Uygulama_Kaydi.md içindeki 3 Usül bölümü: iş gereksinimleri, seçenekler, seçilen yöntem ve gerekçesi, gerçekleşen işlemler ile izleme düzeni.

1. İhtiyaç, talep ve taahhütleri ayır. İşleri yalnızca sayılarıyla değil, gerektirdikleri kaynak, beceri, hazırlık ve bağımlılıklarla açıkla.

2. Mevcut kaynakları işe dönüştüren adımları yaz. İşin tamamını sınırlayan aşamayı varsa dayanağıyla belirle; darboğaz bilinmiyorsa bunu açık soru olarak tut.

3. Kaynak ekleme, yeniden tahsis, sıralama, kapsam değişikliği, erteleme veya kapasite azaltma seçeneklerinden ilgili olanları karşılaştır.

4. Seçilen yöntemi gerekçesiyle kaydet. Görev kapsamındaki masaüstü işlemlerini gerçekleştir; yalnızca planlananlarla gerçekten yapılanları ayrı yaz.

5. Tamamlanan işi, beklemeyi, kaliteyi ve kaynak kullanımını mevcut kayıtlarla değerlendir. Sapmanın olası nedenlerini ve sonraki karara etkisini belirt.

### Tamamlanma ve geri dönüş

Yöntem kaynak ve iş yüküyle ilişkilendirilmiş; karar gerekçesi görünür; planlanan ve gerçekleşen işlemler ayrılmış; gözlem veya izleme yolu belirtilmişse tamamlanır.

İşlem erişim sınırını aşıyorsa 2'ye, kapasite varsayımını değiştiriyorsa 1'e dön. Süre ve hazırlık gereksinimlerini 4'te doğrula.

## 4 Zaman Protokolü

### Kurucu sorular

> Hangi andadır? Bu anı, diğer zamanlardan farklı yapan nelerdir? Neler değildir?

### Kararın etkili olduğu an

Kaynak ve kapasite yönetimi, istenenle yapılabilir olan arasındaki ilişkinin karar gerektirdiği anda belirginleşir. Bu an yalnızca iş başlamadan önce değildir. Taahhüt verilirken, iş yürütülürken, koşullar değişirken ve sonuçlar değerlendirildiğinde ortaya çıkabilir. İşlev süreklidir; bazı karar anları ise sonuçları bakımından daha belirleyicidir.

Taahhütten önce yapılabilir olanla üstlenilecek olan karşılaştırılır. Koşullar değiştiğinde önceki kararın dayanakları yeniden değerlendirilir. Gelecekteki kapasite için ise gerekli olanakların hazırlanmasına yetecek zaman varken harekete geçmek gerekir. An, tek bir takvim tarihinden çok kararın etkili olabileceği zaman aralığını ifade eder.

Bu yönetim aynı anda geçmiş, şimdi ve gelecekle ilişki kurar. Mevcut yatırımlar, beceriler ve verilmiş sözler geçmişten devralınır. Kaynak tahsisi ve iş sırası şimdide düzenlenir. Gelecekte ihtiyaç duyulabilecek olanaklar bugünkü kararlarla hazırlanır. Örgütlü özne, bu zamanlar arasındaki bağı taşıyan eylem bütünüdür.

~~~text
  KARAR GEREKTIREN ANLAR  yalnizca is baslamadan once degildir

    taahhut         is              kosullar        sonuclar
    verilirken      yurutulurken    degisirken      degerlendirilirken
    ----*--------------*---------------*---------------*------------>
    yapilabilir                     onceki kararin
    olanla                          dayanaklari
    ustlenilecek                    yeniden
    olan                            degerlendirilir
    karsilastirilir

    islev sureklidir; bazi karar anlari sonuclari bakimindan daha
    belirleyicidir
    an, tek bir takvim tarihinden cok kararin etkili olabilecegi
    zaman araligini ifade eder

  UC ZAMANLA ILISKI
    gecmis    mevcut yatirimlar, beceriler ve verilmis sozler
              gecmisten devralinir
    simdi     kaynak tahsisi ve is sirasi simdide duzenlenir
    gelecek   gelecekte ihtiyac duyulabilecek olanaklar bugunku
              kararlarla hazirlanir
    orgutlu ozne, bu zamanlar arasindaki bagi tasiyan eylem butunudur
~~~

*Çizim 10 — Zaman: karar gerektiren anlar; geçmiş, şimdi ve gelecek.*

### Hazırlık süresi ve zamanların örtüşmesi

Bir kararın etkisi ile ihtiyacın ortaya çıkışı aynı anda gerçekleşmeyebilir. Bazı kaynaklar hemen yeniden ayrılabilir; bazılarının edinilmesi, hazırlanması veya etkili kullanımı zaman ister. Bu süre, kararın ne zaman alınması gerektiğini değiştirir. Gerekli kaynak miktarının bilinmesi, tek başına doğru karar zamanını belirlemeye yetmez.

Varsayımsal olarak, gerekli ekipmanın hazırlanması altı hafta sürüyorsa dört hafta sonraki bir ihtiyacı karşılamak için bugün sipariş vermek tek başına yeterli değildir. Geçici erişim, işin yeniden düzenlenmesi veya taahhüdün değiştirilmesi gibi başka seçeneklerin değerlendirilmesi gerekir. Aynı satın alma kararı daha erken alındığında başka bir sonuç doğurabilir.

Kaynakların kullanılabilir oldukları zamanların da birbiriyle örtüşmesi gerekir. Uzmanın, ekipmanın ve bilginin ayrı ayrı bulunması yeterli olmayabilir; aynı iş için uygun zamanlarda bir araya gelmeleri gerekir. Bir dönemin toplam kaynağı yeterli görünürken belirli bir haftada açık oluşabilir. Dönem toplamları, zaman içindeki dağılımı gizleyebilir.

Bazı kararlar gelecekteki seçenekleri daraltır. Bir kaynak tüketilebilir, uzun süre belirli bir işe bağlanabilir veya başka amaçlarla kullanılması zorlaşabilir. Bazı kararlar ise ortak altyapı, beceri geliştirme veya süreç değişikliği yoluyla yeni seçenekler oluşturur. Bugünkü kararın ardından hangi işleri yapabilecek durumda kalınacağı, zaman değerlendirmesinin bir parçasıdır.

~~~text
  HAZIRLIK SURESI  varsayimsal ornek

    bugun                      4 hafta sonra         6 hafta sonra
      |                              |                     |
      *==============================+=====================*
    siparis                    ihtiyac                 ekipman
    verilir                    ortaya cikar            hazir olur

    bugun siparis vermek tek basina yeterli degildir; degerlendirilecek
    baska secenekler: gecici erisim . isin yeniden duzenlenmesi .
    taahhudun degistirilmesi
    ayni satin alma karari daha erken alindiginda baska bir sonuc
    dogurabilir

  KAYNAKLARIN ZAMANLARI ORTUSMELIDIR

    uzman      [==========]           [==========]
    ekipman            [===========]
    bilgi      [=================================]
                       |__|
                 ucunun bir araya geldigi aralik

    bir donemin toplam kaynagi yeterli gorunurken belirli bir haftada
    acik olusabilir; donem toplamlari, zaman icindeki dagilimi
    gizleyebilir

  KARARLAR VE GELECEKTEKI SECENEKLER
    daraltan     kaynak tuketilebilir, uzun sure belirli bir ise
                 baglanabilir ya da baska amaclarla kullanilmasi
                 zorlasabilir
    olusturan    ortak altyapi, beceri gelistirme ya da surec
                 degisikligi
~~~

*Çizim 11 — Zaman: hazırlık süresi; kaynakların zamanlarının örtüşmesi; seçenekleri daraltan ve oluşturan kararlar.*

### Zaman ufukları ve öznenin sürekliliği

Anlık veya kısa dönemde mevcut yükün mevcut olanaklarla karşılanması, iş sırasının değiştirilmesi veya geçici kaynak aktarımı öne çıkar. Orta dönemde bakım, eğitim, tedarik ve iş programları beklenen ihtiyaca hazırlanır. Uzun dönemde hangi işlerin yapılabilecek durumda olunacağı, yeni yetkinlik, altyapı veya bir faaliyetten çıkma kararlarıyla belirlenir.

Bu zaman ufuklarının evrensel takvim sınırları yoktur. Hızla değiştirilebilen teknik bir kaynak ile uzun sürede oluşan kurumsal yetkinlik aynı hazırlık süresine sahip değildir. Değerlendirme, ilgili sistemin kaynak edinme, öğrenme, değiştirme ve yenilenme sürelerine bağlanır.

Örgütlü öznenin sürekliliği, aynı kişilerin veya aynı araçların değişmeden kalmasını gerektirmez. Çalışanlar ve araçlar değişirken bazı amaçlar, sorumluluklar ve karar ilişkileri devam edebilir. Bu süreklilik, geçmiş koşulları devralan ve bugünkü kararlarla geleceği etkileyen bir faaliyet birliğidir.

### Zamansal sınırlar

Kaynak ve kapasite yönetimi yalnızca kriz anına veya yılda bir hazırlanan plana ait değildir. Kriz öncesindeki kararlar ve değişen koşullara verilen karşılıklar da kapsama girer. Geçmiş performans, gelecekte aynı sonucun alınacağını garanti etmez; hangi koşullarda elde edildiğiyle birlikte değerlendirilir.

Gelecekte kurulacak kapasite bugün hazır sayılamaz. Planlanan yatırım, işe alım veya eğitim henüz kullanılabilir olanağa dönüşmemiş olabilir. Her işi hemen başlatmak da zamanın doğru kullanıldığı anlamına gelmez; başlangıç, gerekli kaynakların ve bağımlılıkların hazır oluşuyla ilişkilendirilir. Yönetimin niteliği ihtiyacı fark etmek kadar müdahale için kalan zamanı değerlendirmesinde görünür.

~~~text
  ZAMAN UFUKLARI  evrensel takvim sinirlari yoktur
    anlik ya da     mevcut yukun mevcut olanaklarla karsilanmasi,
    kisa donem      is sirasinin degistirilmesi, gecici kaynak aktarimi
    orta donem      bakim, egitim, tedarik ve is programlari beklenen
                    ihtiyaca hazirlanir
    uzun donem      hangi islerin yapilabilecek durumda olunacagi:
                    yeni yetkinlik, altyapi ya da bir faaliyetten
                    cikma kararlari

    hizla degistirilebilen       =/=   uzun surede olusan kurumsal
    teknik bir kaynagin                yetkinligin hazirlik suresi
    hazirlik suresi

  OZNENIN SUREKLILIGI
    calisanlar ve araclar degisirken bazi amaclar, sorumluluklar ve
    karar iliskileri devam edebilir

  ZAMANSAL SINIRLAR
    yalnizca kriz anina ya da yilda bir hazirlanan plana ait degildir
    gecmis performans          -/->   gelecekte ayni sonuc
    planlanan yatirim, ise     -/->   bugun kullanilabilir olanak
    alim ya da egitim
    her isi hemen baslatmak    -/->   zamanin dogru kullanilmasi
~~~

*Çizim 12 — Zaman: üç ufuk; öznenin sürekliliği; zamansal sınırlar.*

### Masaüstü uygulaması

Girdi. 0–3 kayıtları, varsa teslim veya ihtiyaç tarihleri, hazırlık süreleri ve kaynakların kullanılabilirlik aralıkları.

Çıktı. Uygulama_Kaydi.md içindeki 4 Zaman bölümü: karar anları, hazırlık ve uygulama süreleri, zaman çakışmaları, taahhüt koşulları ve yeniden değerlendirme zamanı.

1. İhtiyacın ortaya çıkacağı zamanı, verilen taahhüdü ve bugünkü kullanılabilir kapasiteyi ayır. Tarih veya saat kullanılıyorsa zaman dilimini belirt.

2. Edinme, hazırlık, öğrenme, uygulama ve yenilenme sürelerini eldeki bilgiye göre kaydet. Sürelerin sıralı veya eşzamanlı olup olmadığını açıkla.

3. Gerekli kaynakların aynı iş için uygun zamanlarda bulunup bulunmadığını değerlendir. Dönem toplamını tek başına kullanılabilirlik kanıtı sayma.

4. Kararın etkili olabilmesi için ne zaman alınması gerektiğini ve gecikme hâlinde seçeneklerin nasıl değişeceğini yaz.

5. Kısa, orta ve uzun dönem kararlarını ilgili sisteme göre ayır. Gelecek kapasiteyi hazırlık tamamlanmadan mevcut sayma; değişiklik veya gözden geçirme koşulunu kaydet.

### Tamamlanma ve geri dönüş

İhtiyaç zamanı, hazırlık ve kullanılabilirlik ilişkisi anlaşılmış; bilinmeyen süreler belirtilmiş; taahhüdün zamansal koşulları ve yeniden değerlendirme noktası yazılmışsa tamamlanır.

Zaman sınırı seçilen yöntemi olanaksız kılıyorsa 3'e, erişim varsayımını değiştiriyorsa 2'ye dön. Başlangıç kapsamı değişirse 0'ı güncelle.

## 5 Gaye Protokolü

### Kurucu sorular

> Hangi nihai amaca hizmet eder? Bu nihai amaca ulaştıran nelerdir? Neler değildir?

### Doğrudan amaç ve üst amaç

Kaynak ve kapasite yönetiminin doğrudan amacı, seçilen işler ve taahhütlerle bunları gerçekleştirecek olanaklar arasında uygulanabilir bir ilişki kurmaktır. Hangi işin hangi koşullarda yapılabileceğini ve bunun için nelerin değişmesi gerektiğini açıklığa kavuşturur. Bu doğrudan amaç ile hizmet ettiği üst amaç ayrı tutulur.

Üst amaç, taşıyıcı sistemin varlık nedenine bağlıdır. Bir araştırma kurumunda bilgi üretmeye, kamu hizmetinde ihtiyaçların karşılanmasına, işletmede sunulan değerle birlikte ekonomik devamlılığa, kişinin yaşamında seçtiği yükümlülük ve uğraşlara hizmet edebilir. Kaynak ve kapasite yönetimi, bütün bağlamlar için kendiliğinden tek bir nihai amaç belirlemez.

Aynı teknik yöntemler farklı amaçlar için kullanılabilir. Bir işin gerçekleştirilebilir olması, o işin yapılmasının değerli veya meşru olduğunu tek başına göstermez. Amaç izlemek, amaç seçmek ve amacı gerekçelendirmek ayrı yetkilerdir. Bir ekip veya teknik düzenek kendisine verilmiş amaçlar altında çalışabilir; bunların nihai kaynağı olmak zorunda değildir.

İyi yönetim için önerilen genel gaye, değerli ve gerekçelendirilebilir amaçları kabul edilebilir bedellerle gerçekleştirebilme koşullarını bugün ve gelecekte korumak ve geliştirmektir. Bu ifade teknik tanımdan zorunlu olarak çıkan bir sonuç değil, normatif bir öneridir. Değerli, gerekçelendirilebilir ve kabul edilebilir olan, insanların amaçları, hakları, ortak kararları ve bağlamın sorumlulukları içinde değerlendirilir.

UNEP'in kaynak kullanımına yaklaşımı, ekonomik faaliyet miktarının yanında insan ihtiyaçlarını, çevresel etkileri ve adil dönüşümü ele alır. Bu yaklaşım, kaynak yönetiminin üst amacının neden yalnızca kullanım miktarını artırmak olamayacağına örnektir. Amaçların değerlendirilmesi, kullanılan kaynakların ve sonuçların hangi ölçekte ele alındığıyla bağlantılıdır. [9]

~~~text
  IKI AMAC  ayri tutulur
    dogrudan amac   secilen isler ve taahhutlerle bunlari
                    gerceklestirecek olanaklar arasinda uygulanabilir
                    bir iliski kurmak
    ust amac        tasiyici sistemin varlik nedenine baglidir
                      arastirma kurumu   bilgi uretmek
                      kamu hizmeti       ihtiyaclarin karsilanmasi
                      isletme            sunulan degerle birlikte
                                         ekonomik devamlilik
                      kisinin yasami     sectigi yukumluluk ve ugraslar

    bir isin gerceklestirilebilir   -/->   o isin yapilmasinin degerli
    olmasi                                 ya da mesru olmasi

  AYRI YETKILER
    amac izlemek  |  amac secmek  |  amaci gerekcelendirmek
    bir ekip ya da teknik duzenek kendisine verilmis amaclar altinda
    calisabilir; bunlarin nihai kaynagi olmak zorunda degildir

  IYI YONETIM ICIN ONERILEN GENEL GAYE  normatif bir oneridir
    degerli ve gerekcelendirilebilir amaclari kabul edilebilir
    bedellerle gerceklestirebilme kosullarini bugun ve gelecekte
    korumak ve gelistirmek
~~~

*Çizim 13 — Gaye: doğrudan amaç ve üst amaç; üç ayrı yetki; önerilen genel gaye.*

### Gayeye hizmet eden koşullar

Amaçların açık olması, kaynak ve kapasite kararlarını yönlendirir. Neyi başarmak istendiği, kimlerin yararlanacağı ve başarının hangi değişiklikle anlaşılacağı belirginleşmeden daha fazla kapasite oluşturmak, yalnızca daha fazla iş yapabilme olanağı sağlar. Yapılacak işin yönü ayrıca açıklanmalıdır.

Çıktı ile sonuç arasında bağ kurulması gerekir. Tamamlanan iş sayısı, hizmet edilen amacın gerçekleşmesiyle birlikte değerlendirilir. Daha fazla toplantı daha iyi karar verildiğini, daha fazla rapor daha çok öğrenildiğini veya daha fazla işlem ihtiyacın daha iyi karşılandığını kendiliğinden göstermez. Faaliyet miktarı ile amaç bakımından sağlanan değişiklik ayrı ölçülere karşılık gelir.

Öncelikler ve vazgeçişler açık tutulmalıdır. Bir işe kaynak ayrılması başka işlerin ertelenmesine veya bazı seçeneklerin kapanmasına yol açabilir. Öncelik, bir listenin başına yazılan ifadeden ibaret kalmamalı; kaynak dağılımında karşılık bulmalıdır. Hangi gerekçeyle tercih yapıldığı ve kararın hangi koşullarda yeniden değerlendirileceği anlaşılabilir olmalıdır.

Bugünkü kullanım ile gelecekteki yapabilme gücü birlikte değerlendirilir. Bakım, öğrenme, yenilenme ve hazırlığa ayrılan kaynaklar bu bağlantıyı kurabilir. Buna karşılık geleceği koruma gerekçesi, bugünkü gerçek ihtiyaçların sürekli ertelenmesine dönüşmemelidir. Zamanlar arasındaki tercih, ilgili ihtiyacın ve bedelin gerekçeli değerlendirilmesini gerektirir.

Bedellerin ve etkilerin sınırı doğru çizilmelidir. Bir maliyetin başka bir bölüme, tedarikçiye, topluluğa veya sonraki döneme taşınması onun ortadan kalktığını göstermez. Kaynak tasarrufu yargısı, hangi kaynakta, kimin hesabında, hangi süre için ve başka yerde hangi değişiklik karşılığında tasarruf sağlandığını açıklamalıdır.

Kararlar öğrenmeye açık tutulur. Gerçekleşen sonuçlar, başlangıç varsayımlarını düzeltmek için kullanılır. Bazen daha fazla kaynak, bazen işin farklı tanımlanması, bazen de amacın yeniden değerlendirilmesi gerekir. Her sapmanın aynı müdahaleyi doğurmaması, bu ayrımın korunmasına bağlıdır.

İnsanların katkıları, kendi amaç ve sınırlarıyla birlikte değerlendirilir. Zaman, bilgi ve emek planlanabilir; ancak kişi yalnızca başka amaçlara ayrılabilen bir kapasite birimi olarak ele alınamaz. İnsanı içeren sistemlerde iyi yönetim, katkının nasıl kullanılacağını belirlerken bu katkıyı sunanların koşullarını da kararın parçası yapmalıdır.

### Gayenin taşıyıcısı ve sınırları

Amaç ve sorumluluk öznesi, işin neden yapıldığı ve sonuçlarının nasıl gerekçelendirileceğiyle ilişkilidir. Kararın hangi kaynaktan çıktığı, hangi ilişkileri bağladığı ve kim tarafından değiştirilebildiği, taşıyıcı bütünün somut kimliğini gösterir. Bir algoritmanın tercih üretmesi, tercih ölçütlerinin kaynağını ve sonuçlarının sorumluluğunu kendiliğinden açıklamaz.

Nihai amaç, kendi başına en yüksek doluluk, sürekli kullanım, en düşük görünen maliyet, en fazla kabul edilmiş iş, en yüksek çıktı veya sürekli büyüme değildir. Bunların her biri belirli bir durumda araç veya ara hedef olabilir. Hangi üst amaca hizmet ettiği açıklanmalıdır. Bazı durumlarda kapasiteyi artırmak, bazı durumlarda daha az iş üstlenmek, bir faaliyeti küçültmek veya durdurmak uygun olabilir.

Taşıyıcı öznenin kendi devamlılığı da evrensel nihai gaye değildir. Bir proje belirli bir işi tamamlamak için kurulabilir. İş tamamlandığında kaynaklarını serbest bırakması ve örgütlenmesini sona erdirmesi, amacına uygun bir sonuç olabilir. Makinenin devamlılığı, hizmet ettiği amaçla ilişkisi içinde değerlendirilir.

Başarı değerlendirmesi, hangi ihtiyacın veya amacın ne ölçüde gerçekleştirildiğini; bunun hangi kaynaklarla, hangi bedellerle ve kimler etkilenerek yapıldığını; kararların ardından gelecekte neyin gerçekleştirilebilecek durumda kaldığını birlikte sorar. Maliyet, hız, kullanım oranı ve çıktı, bu sorulara cevap vermeye yardımcı oldukları ölçüde anlamlı ölçütlerdir.

~~~text
  GAYEYE HIZMET EDEN KOSULLAR
    amaclarin acik olmasi         yapilacak isin yonu aciklanir
    cikti ile sonuc arasinda      faaliyet miktari  |  amac bakimindan
    bag                           saglanan degisiklik
    oncelikler ve vazgecisler     oncelik, kaynak dagiliminda karsilik
                                  bulur
    bugunku kullanim ile          bakim, ogrenme, yenilenme ve
    gelecekteki yapabilme gucu    hazirliga ayrilan kaynaklar
    bedellerin ve etkilerin       hangi kaynakta, kimin hesabinda,
    siniri                        hangi sure icin, baska yerde hangi
                                  degisiklik karsiliginda?
    ogrenmeye acik kararlar       gerceklesen sonuclar baslangic
                                  varsayimlarini duzeltir
    insanlarin katkilari          kisi yalnizca baska amaclara
                                  ayrilabilen bir kapasite birimi
                                  olarak ele alinamaz

  KENDI BASINA NIHAI AMAC DEGILDIR  arac ya da ara hedef olabilir
    en yuksek doluluk . surekli kullanim . en dusuk gorunen maliyet .
    en fazla kabul edilmis is . en yuksek cikti . surekli buyume
    tasiyici oznenin kendi devamliligi da evrensel nihai gaye degildir

  BASARI DEGERLENDIRMESI BIRLIKTE SORAR
    hangi ihtiyac ya da amac ne olcude gerceklestirildi?
    hangi kaynaklarla, hangi bedellerle ve kimler etkilenerek?
    kararlarin ardindan gelecekte ne gerceklestirilebilecek
    durumda kaldi?
~~~

*Çizim 14 — Gaye: gayeye hizmet eden koşullar; nihai amaç olmayanlar; başarı değerlendirmesinin üç sorusu.*

### Masaüstü uygulaması

Girdi. 0–4 kayıtları, ifade edilmiş amaçlar, beklenen sonuçlar ve varsa başarı değerlendirmeleri.

Çıktı. Uygulama_Kaydi.md içindeki 5 Gaye bölümü: doğrudan ve üst amaç, amaç yetkileri, yararlanıcılar, sonuç ölçütleri, bedeller ve gelecekteki yapabilme koşulları.

1. Kaynak ve taahhütleri uygulanabilir kılma amacını, faaliyetin hizmet ettiği üst amaçtan ayır. Amaç kaynağı bilinmiyorsa bunu açıkça belirt.

2. Amacı izleyen, seçen ve gerekçelendiren aktörleri kaydet. Uygulayıcının veya teknik aracın yetkisini varsayımla genişletme.

3. Tamamlanan iş ile beklenen etkiyi ilişkilendir. Kullanılan her başarı ölçütünün hangi amaca bilgi sağladığını açıkla.

4. Kaynak kullanımı, maliyet, yarar ve etkilerin kimlere ve hangi zamanlara dağıldığını değerlendir. İnsanların katkılarını kendi koşul ve sınırlarıyla birlikte ele al.

5. Büyüme, doluluk, çıktı ve devamlılığın araç mı amaç mı olduğunu açıklaştır. Gerekirse azaltma, erteleme veya sona erdirme seçeneğinin amaçla ilişkisini yaz.

### Tamamlanma ve geri dönüş

Doğrudan ve üst amaç ayrılmış; amaçların dayanağı ve yetki ilişkisi görünür; başarı ölçütleri sonuca bağlanmış; bedeller ve gelecekteki olanaklar değerlendirilmişse tamamlanır.

Gaye, önceki bölümlerde seçilen işi veya yöntemi değiştiriyorsa ilgili protokolleri ve 0'daki başlangıç kaydını güncelle. Tutarlı kayıtlarla 6'ya geç.

## 6 Kökleşme (Bitiş) Protokolü

### Kurucu sorular

> Başlangıç sorusu hangi açıklığa kavuştu? Beş protokol aynı özneyi ve faaliyeti tutarlı biçimde tarif ediyor mu? Hangi sonuçlar dayanaklı, hangileri koşullu ve hangi sorular açık? Kayıt nasıl sürdürülecek ve ne zaman yeniden açılacak?

### Kökleşmenin anlamı

Kökleşme Protokolü, Varlık, Mekan, Usül, Zaman ve Gaye protokollerinde elde edilen açıklamaları aynı eylem bütününün ilişkileri olarak bir araya getirir. Başlangıç sorusunun hangi açıklığa kavuştuğunu, kavramın sınırlarının nasıl belirlendiğini ve hangi konuların açık kaldığını kaydeder. Tamamlanan metnin dayanağı, bu açıklamalar arasındaki ilişkilerin anlaşılır olmasıdır.

Kaynakların hangi özneye ve işe ilişkin olduğu, erişim koşullarının kapasiteyi nasıl etkilediği, kararların nasıl uygulandığı, zamanın yapılabilirliği nasıl değiştirdiği ve bütünün hangi gayeye hizmet ettiği birlikte değerlendirilir. Kökleşme, bölümlerin arka arkaya sıralanmasından daha fazla bütünlük gerektirir. Bir bölümde ileri sürülen olanak, başka bölümde belirlenen sınırlarla uyuşmalıdır.

Bitiş, bu sorgulama çevriminin tamamlanmasıdır. Kavramın gelecekte değişmeyeceğini veya her uygulamada aynı sonucun alınacağını bildirmez. Yeni koşullar, bilgiler veya itirazlar ortaya çıktığında hangi bölümlerin yeniden ele alınacağını anlaşılır kılar. Yeniden açma, her durumda bütün süreci baştan tekrar etmek anlamına gelmez; değişiklikten etkilenen ilişkiler izlenir.

### Tutarlılık ve taşıyıcı kimliği

Bütünlük değerlendirmesinde aynı kavramların bölümler boyunca aynı anlamda kullanılıp kullanılmadığı incelenir. Kapasitenin neyin kapasitesi olduğu, hangi koşullara ve zaman aralığına bağlı bulunduğu açık olmalıdır. Mekan Protokolü'ndeki erişim ve yetki sınırları, Usül Protokolü'nde varsayılan eylem alanıyla; Zaman Protokolü'ndeki hazırlık süreleri, üstlenilen işlerle; Gaye Protokolü'ndeki sonuç, başarı ölçütleriyle ilişkilendirilir.

Taşıyıcının kimliği bu bağlantılar içinde açıklanır. İşin ait olduğu bütün, kararları üreten mekanizma ve amaçlardan sorumlu özne ayrı ayrı gösterilir. Bunlar farklı aktörlerde bulunabilir. Örgütlü öznenin somut karşılığı, bu konumların nasıl bağlandığıyla belirlenir; yalnızca bir kişi, kurum veya yazılım adı verilmesiyle tamamlanmaz. Protokolü uygulayan kişinin veya yardımcının bu yapı içindeki görevi varsa ayrıca belirtilir.

### Sonuç kaydı ve sınırlar

Girdiler, Tohum kaydı, beş protokolün güncel açıklamaları, kullanılan dayanaklar ve varsa uygulamada elde edilmiş gözlemlerdir. Kavramsal olarak açıklananlar, uygulamada gözlenenler ve henüz sınanmamış beklentiler birbirinden ayrılır. Bir protokolün yazılmış olması, içerdiği işlemlerin gerçekleştirilmiş veya beklenen sonuçların elde edilmiş olduğunu göstermez. Uygulama bilgisi yoksa bitiş, kavramsal kaydın tamamlanması düzeyinde ifade edilir.

Başlangıç sorusuna verilen cevap, hangi kabullerin değiştiği ve hangi belirsizliklerin sürdüğüyle birlikte kaydedilir. Önemli bir çelişki ilgili protokole dönülerek düzeltilir. Çözülemeyen bir çelişki veya eksik bilgi, etkilediği sonuç sınırlanarak açık tutulabilir; tamamlanmış bir bulgu gibi kullanılmaz. Sonucun hangi koşullarda geçerli olduğu okuyucu tarafından izlenebilmelidir.

Kökleşme, yalnızca bir dosyayı kaydetmek, açık soruları kapatılmış saymak, olumlu sonuç ilan etmek veya taşıyıcıyı süresiz devam ettirmek değildir. Geçici bir çalışma, görevini tamamlayıp kaynaklarını serbest bırakarak sona erebilir. Kayıtların adı, tarihi, sürümü ve kullanım yeri ile sorumluluk ve takip ilişkileri belirginleştirilir. Amaç, erişim, yetki, kaynak, kapasite veya zaman koşullarındaki önemli değişiklikler yeniden değerlendirme nedeni olarak kayda geçirilir.

### Masaüstü uygulaması

Girdi. 0 Tohum kaydı, 1–5 arasındaki güncel kayıtlar, dayanaklar ve varsa gerçekleşen uygulama sonuçları.

Çıktı. Uygulama_Kaydi.md içindeki 6 Kökleşme bölümü: başlangıç sorusunun cevabı, bütünlük değerlendirmesi, taşıyıcı kimliği, açık konular, sonuç durumu ve kayıt devri.

1. Uygulama_Kaydi.md içindeki 0–5 bölümlerini birlikte incele; başvurulan dosyaları gerektiğinde aç. Güncel sürümleri belirle ve eski kayıtla yeni sonucu karıştırma.

2. Başlangıç sorusuna cevabı bağlantılı paragraflarla yaz. Giderilen açıklıkları, değişen kabulleri ve süren belirsizlikleri belirt.

3. Özne, kapsam, kaynak, kapasite, erişim, yetki, usul, zaman ve gaye tutarlılığını incele. Çelişkiyi ilgili protokole dönerek düzelt veya sonuç üzerindeki sınırı açıkça kaydet.

4. Taşıyıcı sistemi, karar mekanizmasını ve amaçlardan sorumlu özneyi birlikte açıklayan kimlik paragrafını oluştur. Uygulayıcının varsa bu yapıdaki görevini ayrıca belirt.

5. Kavramsal olarak açıklananları, uygulamada gözlenenleri ve henüz sınanmamış beklentileri ayrı kaydet. Durumu Tamamlandı, Koşullu tamamlandı veya Açık olarak gerekçesiyle seç.

6. Dosya adlarını, tarihi, sürümü ve kullanım yerini yaz. Bağlantıları açarak kontrol et; açık konuların takibini ve sonucu etkileyen yeniden açma koşullarını belirt.

### Tamamlanma ve geri dönüş

Başlangıç sorusu yeterli dayanakla cevaplanmışsa Tamamlandı; cevap belirli varsayım veya sınırlar altında kullanılabiliyorsa Koşullu tamamlandı; eksik bilgi veya çelişki temel cevabın kurulmasını engelliyorsa Açık olarak kaydedilir. Seçilen durum üstteki Genel durum alanına da aktarılır. Sonuçlar izlenebilir, çelişkiler giderilmiş veya sınırları belirtilmiş, sonraki çalışma ayrılmış ve kayıt kullanılabilir olmalıdır.

~~~text
  BOLUMLER ARASINDAKI BAGLANTILAR
    Mekan    erisim ve yetki sinirlari   <--->   Usul'de varsayilan
                                                 eylem alani
    Zaman    hazirlik sureleri           <--->   ustlenilen isler
    Gaye     sonuc                       <--->   basari olcutleri
    bir bolumde ileri surulen olanak, baska bolumde belirlenen
    sinirlarla uyusmalidir

  TASIYICININ KIMLIGI  ayri ayri gosterilir
    isin ait oldugu butun  |  kararlari ureten mekanizma  |
    amaclardan sorumlu ozne
    yalnizca bir kisi, kurum ya da yazilim adi verilmesiyle
    tamamlanmaz

  BIRBIRINDEN AYRILIR
    kavramsal olarak    |   uygulamada     |   henuz sinanmamis
    aciklananlar        |   gozlenenler    |   beklentiler

  SONUC DURUMU
    Tamamlandi            baslangic sorusu yeterli dayanakla
                          cevaplanmis
    Kosullu tamamlandi    cevap belirli varsayim ya da sinirlar
                          altinda kullanilabiliyor
    Acik                  eksik bilgi ya da celiski temel cevabin
                          kurulmasini engelliyor

  KOKLESME DEGILDIR
    yalnizca bir dosyayi kaydetmek  |  acik sorulari kapatilmis saymak
    olumlu sonuc ilan etmek  |  tasiyiciyi suresiz devam ettirmek
~~~

*Çizim 15 — Kökleşme: bölümler arasındaki bağlantılar; taşıyıcının kimliği; üç sonuç durumu.*

Amaç, erişim, yetki, kaynak, kapasite veya zaman koşulları sonucu etkilediğinde ilgili protokoller yeniden açılır. İlk soru veya kapsam değiştiğinde 0 da güncellenir.

## Kaynaklar

### Kaynak 1

UNDP Capacity Development for Health (https://capacitydevelopmentforhealth.undp.org/)

### Kaynak 2

Federal Reserve Board Industrial Production and Capacity Utilization Explanatory Notes (https://www.federalreserve.gov/Releases/G17/CapNotes.htm)

### Kaynak 3

Elinor Ostrom The Challenge of Crafting Rules to Change Open Access Resources into Managed Resources (https://dlc.dlib.indiana.edu/dlc/items/184600b1-5733-4590-92db-1b643f19c8ca)

### Kaynak 4

SFIA Capacity Management (https://sfia-online.org/en/sfia-9/skills/capacity-management)

### Kaynak 5

CIPS Capacity Management in the Supply Chain (https://1prd-dxp.cips.org/intelligence-hub/operations-management/capacity-management)

### Kaynak 6

Paul Schönsleben ETH Zürich Conclusions for Job Shop Production (https://opess.ethz.ch/course/section-13-2/13-2-3-conclusions-for-job-shop-production/)

### Kaynak 7

Google Site Reliability Workbook Identifying and Recovering from Overload (https://sre.google/workbook/overload/)

### Kaynak 8

NIST Artificial Intelligence Risk Management Framework 1.0 AI RMF Core (https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)

### Kaynak 9

UNEP Global Resources Outlook 2024 (https://www.unep.org/en/publications/report/global-resources-outlook-2024)

## Uygulama kaydı şablonu

Bu bölümdeki şablonu ayrı bir Uygulama_Kaydi.md dosyasına kopyalayın. Başlıklar ve boş alanlar doldurulmak üzere verilmiştir.

```markdown
### Kaynak ve Kapasite Yönetimi Uygulama Kaydı

Bu şablonu her çalışma için ayrı bir klasöre Uygulama_Kaydi.md adıyla kopyalayın. Köşeli parantezli alanları kendi çalışma bilgileriyle doldurun. Bilinmeyen alanlara bilinmiyor yazın ve ilgili açık soruyu belirtin. Aşağıdaki alanlar örnek sonuç değildir.

**Çalışma adı:** [Doldurun]
**Çalışma kimliği:** [Doldurun]
**Kayıt tarihi ve zaman dilimi:** [Doldurun]
**Kayıt sürümü:** [Doldurun]
**Uygulayıcı:** [Doldurun]
**İncelenen özne:** [Doldurun veya açık soru]
**Çalışma klasörü:** [Doldurun]
**Genel durum:** Başlanmadı

#### 0 Tohum

**Bölüm durumu:** Başlanmadı

**Başlangıç talebi ve sorusu:** [Talebi ve araştırılacak soruyu kaydedin.]

**İhtiyaç ve başlangıçtaki açıklık:** [İstenen iş ile olanaklar arasındaki açıklığı yazın.]

**İncelemenin amacı ve öznenin ilk ifade edilen gayesi:** [İki yönelimi ayırın.]

**Kapsam ve kapsam dışı alan:** [Faaliyet, özne, zaman aralığı ve sınırı belirtin.]

**Uygulayıcının görevi ve mevcut yetki alanı:** [Belgeleme, değerlendirme ve uygulama kapsamını belirtin.]

**Bilinenler ve dayanakları:** [Bilgi ve kaynağını birlikte yazın.]

**Başlangıç varsayımları:** [Varsayım ve nedenini belirtin.]

**Açık sorular ve sonraki bölüme aktarım:** [Soruları ve ilişkili protokolleri belirtin.]

#### 1 Varlık

**Bölüm durumu:** Başlanmadı

**Faaliyet ve taşıyıcı özne:** [Tanımlayın.]

**Kaynaklar ve erişilebilirlik durumu:** [Mevcut, erişilebilir, başka işe ayrılmış veya potansiyel ayrımını yapın.]

**Yetkinlik ve kapasite:** [Kapasitenin neyin kapasitesi olduğunu, koşulunu, ölçüsünü veya nitel açıklamasını ve zaman aralığını yazın.]

**Talep ve taahhüt:** [Ayrı ayrı belirtin.]

**Çıktı ve sonuç:** [Gerçekleşen çıktı ile amaç bakımından sonucu ayırın.]

**Tamamlayıcı kaynaklar ve bağımlılıklar:** [Belirtin.]

**Kimlik ve kapsam sınırları:** [Nedir, ne değildir, kimdir, kim değildir sorularına cevap verin.]

**Dayanaklar, varsayımlar ve açık sorular:** [Kaydedin.]

#### 2 Mekan

**Bölüm durumu:** Başlanmadı

**Fiziksel, dijital ve örgütsel faaliyet alanı:** [Tanımlayın.]

**Sistem sınırı ve dış bağımlılıklar:** [Hangi aktör ve etkilerin kapsama girdiğini belirtin.]

**Mülkiyet, erişim, kullanım ve yönetim yetkileri:** [Konumları ayırın.]

**Taşıyıcı sistem:** [Faaliyetin ait olduğu bütünü belirtin.]

**İşletici ve karar mekanizması:** [Kararın nasıl üretildiğini ve uygulandığını açıklayın.]

**Amaçlardan sorumlu özne:** [Bilindiği ölçüde belirtin.]

**Yerel kararların diğer alanlara etkisi:** [Değerlendirin.]

**Dayanaklar, varsayımlar ve açık sorular:** [Kaydedin.]

#### 3 Usül

**Bölüm durumu:** Başlanmadı

**İhtiyaç, talep ve taahhüt ayrımı:** [Kaydedin.]

**İş yükü ve kaynak gereksinimleri:** [Beceri, hazırlık, sıra ve bağımlılıkları açıklayın.]

**İş akışı ve sınırlayıcı aşama:** [Darboğaz biliniyorsa dayanağını yazın.]

**Değerlendirilen seçenekler:** [İlgili seçenekleri karşılaştırın.]

**Seçilen yöntem ve gerekçesi:** [Kaydedin.]

**Planlanan işlemler:** [Henüz yapılmamış olanları belirtin.]

**Gerçekleştirilen işlemler ve kanıtları:** [Yalnızca gerçekleşenleri tarih, dosya veya gözlemle kaydedin.]

**Gözlenen sonuçlar ve sapmalar:** [Kalite, bekleme ve kaynak kullanımını belirtin.]

**Düzeltme veya geri dönüş:** [İlgili protokolü ve nedeni yazın.]

#### 4 Zaman

**Bölüm durumu:** Başlanmadı

**İhtiyaç ve taahhüt zamanı:** [Tarih, zaman aralığı ve zaman dilimini belirtin.]

**Bugünkü kapasite ve gelecekte hazırlanacak kapasite:** [Ayırın.]

**Edinme, hazırlık, öğrenme, uygulama ve yenilenme süreleri:** [Bilindiği ölçüde yazın; eşzamanlı veya sıralı ilişkileri açıklayın.]

**Kaynakların kullanılabilirlik aralıkları:** [İş için gerekli örtüşmeyi değerlendirin.]

**Kararın etkili olabileceği zaman:** [Hazırlık süresiyle ilişkilendirin.]

**Kısa, orta ve uzun dönem kararları:** [İlgili sisteme göre tanımlayın.]

**Yeniden değerlendirme tarihi veya koşulu:** [Belirtin.]

**Dayanaklar, varsayımlar ve açık sorular:** [Kaydedin.]

#### 5 Gaye

**Bölüm durumu:** Başlanmadı

**Doğrudan amaç:** [İş ve olanaklar arasında kurulacak ilişkiyi belirtin.]

**Üst amaç ve yararlanıcılar:** [Hizmet edilen sonucu ve ilgili kişileri açıklayın.]

**Amacı izleyen, seçen ve gerekçelendiren aktörler:** [Yetkileri ayırın.]

**Beklenen sonuç ve başarı ölçütleri:** [Her ölçütün amaçla ilişkisini belirtin.]

**Bedeller ve etkilerin dağılımı:** [Kimin, nerede, hangi zamanda etkilendiğini açıklayın.]

**Gelecekteki yapabilme koşulları:** [Korunan, geliştirilen veya daralan olanakları yazın.]

**Devam, azaltma, erteleme veya bitirme tercihi:** [Amaçla ilişkisini gerekçelendirin.]

**Dayanaklar, varsayımlar ve açık sorular:** [Kaydedin.]

#### 6 Kökleşme

**Bölüm durumu:** Başlanmadı

**Başlangıç sorusuna cevap:** [Bağlantılı paragraflarla yazın.]

**Beş protokolün birlikte oluşturduğu açıklama:** [Özne, sınır, erişim, usul, zaman ve gayenin ilişkisini değerlendirin.]

**Taşıyıcı kimliği:** [Taşıyıcı sistem, karar mekanizması ve amaçlardan sorumlu özneyi birlikte açıklayın.]

**Tutarlılık değerlendirmesi ve giderilen çelişkiler:** [İlgili protokolleri gösterin.]

**Kavramsal olarak açıklananlar:** [Kaydedin.]

**Uygulamada gözlenenler:** [Kanıtıyla kaydedin veya gözlem yok yazın.]

**Henüz sınanmamış beklentiler:** [Koşullarıyla kaydedin.]

**Açık konular ve sonuç üzerindeki sınırları:** [Belirtin.]

**Bitiş durumu ve gerekçesi:** [Tamamlandı / Koşullu tamamlandı / Açık seçeneklerinden birini gerekçelendirin.]

**Kayıt devri veya sürdürme sorumluluğu:** [Kim kullanacak, nerede tutulacak; bilinmiyorsa açık soru olarak belirtin.]

**Yeniden açma koşulları ve ilgili protokoller:** [Kaydedin.]

**Son dosya adı, sürüm ve tarih:** [Belirtin.]

#### Dayanaklar ve değişiklik kaydı

**Dayanak 1:** [Dosya yolu veya URL, ilgili bölüm veya sayfa, desteklediği açıklama.]

**Değişiklik 1:** [Tarih, değişen protokol, değişiklik nedeni ve etkilenen sonuç.]
```

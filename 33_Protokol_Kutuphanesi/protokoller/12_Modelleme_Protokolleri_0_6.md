# Arayüz Çizimleri, İşletim Sistemi Mimarisi ve Çekirdek Katmanların Modellemesi

**0–6 Modelleme Protokolleri**

**Sürüm:** 1.0\
**Tarih:** 30 Ekim 2026\
**Biçim:** Paragraf ağırlıklı protokol metni ve masaüstü uygulama adımları

Bu belge, bir modelleme çalışmasının başlangıcını, varlığını, mekânını, usulünü, zamanını, gayesini ve kökleşmesini birlikte ele alır. Amaç, kurulan modelin hangi soruya karşılık verdiğini, nasıl temellendirildiğini, hangi koşullarda kullanılabileceğini ve ne zaman yeniden değerlendirileceğini izlenebilir kılmaktır.

## Kullanım düzeni

Bu belgede protokol, bir modelleme çalışmasının sorularını, kayıtlarını ve değerlendirme koşullarını düzenleyen yöntem anlamında kullanılır. Arayüz çizimleri, işletim sistemi mimarisi, çekirdek katmanları ve bunları modelleyen taraf aynı sorularla incelenebilir; bu başlıklar zorunlu bir yazılım katmanı sırası oluşturmaz. İnceleme başka sistemlere genişletildiğinde kullanılan örneğin ve kaynağın kapsamı ayrıca belirtilir.

Her protokolün önce paragraf ağırlıklı açıklaması, ardından masaüstünde uygulanacak adımları bulunur. Adımlar bir metin düzenleyicide çalışma kaydı tutularak yürütülür. Çizim veya başka bir belge kullanılıyorsa kayıt içinde ona bağlantı verilir. Protokol tarifi ile belirli bir çalışmanın yanıtları ayrı dosyalarda tutulur; aynı yöntem farklı çalışmalarda yeniden kullanılabilir.

İlk okumada 0'dan 6'ya ilerlenir. Uygulama sırasında ilgili bölümler arasında geri dönülebilir: yeni bir gaye varlık tanımını, yeni bir bağlam işleyişi, yeni bir zaman bilgisi tamamlanma kararını değiştirebilir. Numaralar her adımın tek seferde ve değişmez sırayla bitirilmesini gerektirmez.

Önemli ifadeler tanım, gözlem, varsayım, çıkarım veya karar olarak ayırt edilir. Dayanak kaydında kullanılan kaynak veya dosya, ilgili ifade, tarih veya sürüm ve destek sınırı bulunur. Bilinmeyen, yanlış veya başarısız sonucuyla eşitlenmez. Açık soruların hangi kararı etkilediği ve ne zaman yeniden ele alınacağı yazılır.

Bir bölümün kayıt bakımından tamamlanması ile modelin uygulamada sınanması farklı durumlardır. Kapanış kaydı incelemenin düzeyini taşır. Örneğin bir çalışma masaüstünde tutarlılık incelemesini tamamlayabilir ve gerçek kullanımda henüz sınanmamış olabilir. Belgenin sonundaki şablonda çalışma alanları boş bırakılmıştır; uygulama sonucu kullanıcı tarafından kaydedilir.

Kayıt ve model oluşturma işi ile tarif edilen sistem üzerinde değişiklik yapma işi ayrı kapsamlardır. Bu metin, adımların bir insan veya açıkça görevlendirilmiş bir yardımcı tarafından izlenmesine uygundur; yapılacak gerçek işlemler çalışma kapsamında ayrıca belirtilir.

## Masaüstünde başlama

1. Bir çalışma klasörü oluştur ve protokol metnini burada tut. İstersen klasörü masaüstüne yerleştir; sabit bir işletim sistemi yolu gerekmez.

2. Belgenin sonundaki Çalışma Kaydı Şablonu bölümünü yeni bir Markdown dosyasına kopyala ve dosyayı çalışma adına göre adlandır; örneğin `Calisma_Kaydi_Ornek_01.md`.

3. 0 Tohum bölümünü uygula. Konuyu, ihtiyacı, kapsamı, ilk bilgi durumunu ve inceleme örneğini kaydet.

4. 1–5 bölümlerini seçilen örnek üzerinde incele. Yanıtları çalışma kaydına yaz; çizim, belge ve bulguları dayanak olarak bağla. İlgili yeni soruları ilgili protokole geri aktar.

5. 6 Kökleşme bölümünde kayıtları birlikte değerlendir. Sonucu dayanak düzeyiyle birlikte yaz; çözümlenmeyen çelişkiyi tamamlanmış gibi kapatma.

6. Her anlamlı değişiklikte çalışma kaydı sürümünü ve değişiklik kaydını güncelle. Yeni bilgiden etkilenen bölümleri yeniden aç; güncel kapanış kararını 6'da tut.

~~~text
  <calisma-klasoru>/                 masaustune de konabilir; sabit bir
    |                                isletim sistemi yolu gerekmez
    |-- <protokol metni>.md          yontemin tarifi
    |-- Calisma_Kaydi_Ornek_01.md    bu calismanin yanitlari
    |     0 Tohum ... 6 Koklesme
    |     Dayanaklar . Acik sorular . Degisiklikler
    `-- cizim ya da baska belge      kayit icinden baglanti verilir

  tarif ile yanitlar ayri dosyalarda durur:
  ayni yontem farkli calismalarda yeniden kullanilabilir

  her onemli ifade bes turden biridir
    tanim | gozlem | varsayim | cikarim | karar

  dayanak kaydinda bulunanlar
    kaynak ya da dosya | ilgili ifade | tarih ya da surum |
    destek siniri

  bolum durumlari
    Baslanmadi | Calisiliyor | Engelli |
    Inceleme icin tamamlandi | Yeniden acildi

  esitlenmeyenler
    bilinmeyen                    =/=   yanlis ya da basarisiz sonuc
    kayit bakimindan tamamlanma   =/=   modelin uygulamada sinanmasi
    kayit ve model olusturma      =/=   tarif edilen sistemde
                                        degisiklik yapma
~~~

*Çizim 1 — Masaüstünde başlama: tarif ile yanıtlar ayrı dosyalarda; beş ifade türü; eşitlenmeyen üç çift.*

## Protokol dizisi

| Bölüm | Temel iş | Üretilen kayıt |
| --- | --- | --- |
| 0 Tohum (Başlangıç) | Başlangıç koşullarını ve yönelimi kurar | Başlangıç kaydı |
| 1 Varlık | İncelenen şeyi ve kimlik sınırını açıklar | Varlık kaydı |
| 2 Mekan | Bağlamı, sınırları ve ilişkileri açıklar | Mekan kaydı |
| 3 Usül | İşlemleri ve sonuç anlamını açıklar | İşlem kaydı |
| 4 Zaman | Durumu, sırayı ve geçerliliği açıklar | Zaman kaydı |
| 5 Gaye | Amacı ve başarı koşullarını açıklar | Gaye kaydı |
| 6 Kökleşme (Bitiş) | Bütünlüğü ve devamlılığı değerlendirir | Kapanış ve devam kaydı |

## 0 Tohum (Başlangıç) Protokolü

> Bu çalışmayı başlatan şey nedir; hangi ihtiyaç, soru, varsayım ve yönelimle başlıyoruz?

### Protokol metni

Tohum Protokolü, modelleme çalışmasının başlangıç koşullarını kayda geçirir. İncelemeyi başlatan soru, karşılanması beklenen ihtiyaç, ilk yönelim ve mevcut bilgi burada açıklanır. Başlangıç kaydı, sonradan oluşan modelin hangi soruya karşılık üretmek üzere kurulduğunun izlenmesini sağlar. Çalışmanın konusu ve kapsamı değişebilir; bu değişebilirlik başlangıç kaydında açık tutulur.

Tohumun kurucu niteliği, incelemeye yön vermesi ve sonraki ayrımların başlangıç dayanağını taşımasıdır. İlk varlık tanımı, düşünülen bağlam, olası işleyiş, zaman koşulları ve beklenen yarar bu aşamada birbirine bağlı ön karşılıklar olarak bulunur. Bu karşılıklar 1–5 arasındaki protokollerde açıklanır ve değerlendirilir. Başlangıçta dile getirilen bir varsayım, yalnızca kayda geçirilmiş olması nedeniyle kesinleşmiş bilgiye dönüşmez.

Başlangıcın kim tarafından ortaya konduğu ve kimler tarafından taşınacağı açıklanır. Soruyu soran, modeli kuran, kayıtları tutan, modeli kullanacak olan ve gayeyi belirleyen taraflar gerektiğinde ayrı gösterilir. Bu rollerin tek bir insanda, yazılımda veya çalışma düzeninde birleşmesi zorunlu değildir. Henüz belirlenmemiş bir sorumluluk, belirlenmiş gibi yazılmaz.

İlk soruyla birlikte bilgi sınırı da kaydedilir. Verilen bilgiler, doğrudan gözlemler, kaynaklara dayanan ifadeler, varsayımlar, çıkarımlar ve kararlar ayırt edilir. Başlangıçta hangi bağlamın kullanıldığı ve neden ilgili sayıldığı açıklanır. Bu çalışmaya ait olmayan geçmiş konuşmalar başlangıç bilgisine eklenmez. Başka alanlardan yararlanmak gerektiğinde bağlantı gerekçesi ve kaynak gösterilir.

Tohum, tamamlanmış mimari, kesin kimlik hükmü veya bütün yanıtları baştan içeren çözüm değildir. Başlangıçtaki kanaati doğrulamak üzere hazırlanmış bir sonuç listesi de değildir. Çalışmanın ilerlemesi için bütün belirsizliklerin giderilmesini şart koşmaz; belirsizliklerin görünür ve izlenebilir olmasını sağlar.

~~~text
                     0 TOHUM: baslangic kaydi
       ozgun baslangic sorusu . ihtiyac . beklenen yarar .
  baslangic kapsami . rol dagilimi . ornek durum . acik sorular
                                  |
                 birbirine bagli bes on karsilik
                                  |
        .------------+------------+------------+------------.
        |            |            |            |            |
        v            v            v            v            v
     1 Varlik     2 Mekan      3 Usul       4 Zaman      5 Gaye
     ilk varlik   dusunulen    olasi        zaman        beklenen
     tanimi       baglam       isleyis      kosullari    yarar

  on karsiliklar 1-5'te aciklanir ve degerlendirilir.
  bir varsayim, yalnizca kayda gecirildigi icin kesinlesmis
  bilgiye donusmez.

  ayri gosterilebilen taraflar
    soruyu soran . modeli kuran . kayitlari tutan .
    modeli kullanacak olan . gayeyi belirleyen
    (tek bir insanda, yazilimda ya da calisma duzeninde
     birlesmeleri zorunlu degildir)

  tohum sunlar degildir
    tamamlanmis mimari . kesin kimlik hukmu .
    butun yanitlari bastan iceren cozum .
    baslangictaki kanaati dogrulamak icin hazirlanmis sonuc listesi
~~~

*Çizim 2 — Tohum: birbirine bağlı beş ön karşılık 1–5'e açılır; Tohum'un olmadığı şeyler.*

Bu protokolün kaydı; özgün başlangıç sorusunu, ihtiyacı, beklenen yararı, başlangıç kapsamını, rol dağılımını, ilk beş eksen karşılığını ve açık soruları içerir. İncelemeyi somutlaştıracak bir örnek durum seçilir. Daha sonra yönelim değişirse önceki başlangıç silinmez; değişikliğin gerekçesi ve ilgili protokollere etkisi kaydedilir.

### Masaüstünde uygulama

**Girdiler:** Başlangıç sorusu, bu çalışmada verilen bilgiler, eldeki kaynaklar ve incelemeyi başlatan ihtiyaç. Hazır bir model bulunması gerekmez.

1. Çalışma kaydını yeni bir adla oluştur. Çalışma adını, hazırlayanı, tarih ve saat dilimini, kayıt sürümünü ve yapılacak incelemenin düzeyini yaz. Özgün başlangıç sorusunu anlamını değiştirmeden kaydet.

2. Soruyu doğuran durumu, beklenen yararı ve sonucu kullanacak tarafları birer paragrafla açıkla. Soruyu soran, modeli kuran, kaydı tutan ve gayeyi belirleyen tarafları bilindiği ölçüde ayır.

3. Varlık, mekân, usul, zaman ve gaye için başlangıçta bildiğin ön karşılıkları yaz. Önemli ifadeleri tanım, gözlem, varsayım, çıkarım veya karar olarak işaretle; açık soruları ayrı kaydet.

4. Kullanılacak belgeleri ve kaynakları Dayanaklar kaydına bağla. İlk kapsamı, kapsam dışında kalanları ve dış bağımlılıkları belirt. Bu çalışma için verilen bağlamı esas al. Başka alanlardan alınan bilginin ilgisini ve kaynağını açıkla.

5. Modelin neyi açıklayacağını gösterecek bir örnek durum seç. Başlatan tarafı, beklenen sonucu ve incelemeye aktarılacak soruları yaz. Belirli bir örnek seçilemiyorsa bunun nedenini açık soru olarak kaydet.

6. Açık soruları 1–5 arasındaki ilgili bölümlere aktar. Başlangıç kaydını ilk sürüm olarak sakla; sonraki yönelim değişikliklerini Değişiklikler kaydında izle.

**Üretilecek kayıt:** Çalışma kaydının 0 bölümünde başlangıç sorusu, ihtiyaç, yararlanıcılar, kapsam, roller, beş eksenin ön karşılıkları, seçilen örnek ve açık sorular.

**Tamamlanma koşulu:** Çalışmanın neden başlatıldığı ve hangi kapsamda ilerleyeceği anlaşılır; ilk karşılıkların bilgi durumu görünür; açık sorular ilgili bölümlere bağlanmıştır. Bu, 1–5 sonuçlarının önceden onaylandığı anlamına gelmez.

**Geri dönüş koşulu:** Başlangıç ihtiyacı, çalışma konusu, kapsam veya ilk yönelim değiştiğinde 0 yeniden açılır. Değişikliğin 1–5 üzerindeki etkisi ve 6 kapanış kaydına yansıması değerlendirilir.

## 1 Varlık Protokolü

> Nedir? Onu o yapan nelerdir? Neler değildir?

### Protokol metni

Varlık Protokolü, hakkında konuşulan şeyin ne olduğunu ve hangi bütünün birliğinin izlendiğini açıklığa kavuşturur. İncelemenin birimi ve ölçeği belirtilir: bir kurum, hizmet, süreç, uygulama, arayüz öğesi, işletim sistemi, çekirdek bileşeni veya model kuran düzen ele alınabilir. Türün tanımı, tekil bir örneğin kimliği, üstlenilen rol ve mevcut durum ayrı tutulur. Bir rol değişikliği ya da geçici işlev kaybı, varlığın kimliğinin mutlaka sona erdiği anlamına gelmez.

Onu o yapan özellikler, varlıkta bulunan bütün özelliklerle aynı ağırlıkta değerlendirilmez. Kurucu özellikler seçilen tanımı oluşturur; ayırt edici özellikler ilgili benzerler arasında fark yaratır; durumsal özellikler belirli bir andaki hâli anlatır; sunuma ilişkin özellikler ise varlığın nasıl temsil edildiğini belirler. Bir özelliğin kurucu veya ayırt edici sayılması, inceleme düzeyi ve karşılaştırma alanıyla birlikte gerekçelendirilir. Ona has olmak, mutlaka dünyada yalnızca onda bulunan tek bir özellik taşımak demek değildir.

Bir sistemin kimliği, parçalarının yanında parçalar arasındaki ilişkileri ve değişim boyunca korunacak koşulları da kapsar. Bir öğenin çıkarılması veya değiştirilmesi değerlendirilirken hangi işlevin, ilişkinin, hakkın veya sürekliliğin kaybolduğu sorulur. Böylece sistem, yalnız bir bileşen listesiyle tanımlanmaz. NASA'nın sistem mühendisliği çerçevesinde de insanlar, süreçler, tesisler, donanım ve yazılım birlikte ele alınır; bütünün niteliğinde parçalar arasındaki ilişkiler belirleyici kabul edilir. [1]

Arayüz çizimi, kullanıcıya sunulan nesne, eylem, durum ve sonucun temsilidir. İşletim sistemi mimarisi, çalışma ortamının bileşenlerini, hizmetlerini ve sorumluluk ilişkilerini açıklar. Çekirdek modeli ise seçilen sistemdeki temel yürütme, kaynak ve koruma mekanizmalarını inceler. İşletim sistemi çekirdeği ile fiziksel işlemci çekirdeği farklı varlıklardır. Bir çizim, uygulamanın kendisiyle; bir mimari betimleme de betimlediği mimariyle özdeş tutulmaz. ISO/IEC/IEEE 42010:2022, mimari ile onu ifade eden mimari betimlemeyi açıkça ayırır. [2]

Model kuran sistem ile modelin anlattığı sistem ayrı kaydedilir. Bir sistem kendisini modelleyebilir; fakat bir işletim sistemi modeli üreten tarafın, tarif ettiği işletim sistemi olması gerekmez. Taşıyıcı, modeli üreten taraf, eyleyen taraf, gayeyi belirleyen taraf ve kararları düzeltme sorumluluğunu taşıyan taraf aynı varlıkta birleşebilir veya farklı aktörlere dağılabilir. Model kuran fail adı, bu işlevlerin çözümlemesinde kullanılan bir öneridir; makinenin insan, bilgisayar ya da yapay zekâ olduğuna ilişkin tek ve zorunlu bir özdeşlik kurmaz.

~~~text
  .-------------. kurar  .----------------. anlatir .---------------.
  | model kuran |------->| MODEL          |- - - - >| modelin       |
  | taraf       |        |                |         | anlattigi     |
  |             |        | cizim          |         | sistem        |
  |             |        | mimari         |         |               |
  |             |        | betimleme      |         | uygulama      |
  |             |        |                |         | mimari        |
  `-------------'        `----------------'         `---------------'

  cizim, uygulamanin kendisiyle; mimari betimleme, betimledigi
  mimariyle ozdes tutulmaz

  bir sistem kendisini modelleyebilir; ama bir isletim sistemi modeli
  ureten tarafin, tarif ettigi isletim sistemi olmasi gerekmez

  UC MODEL, UC AYRI KONU
    arayuz cizimi              kullaniciya sunulan nesne, eylem,
                               durum ve sonucun temsili
    isletim sistemi mimarisi   calisma ortaminin bilesenleri,
                               hizmetleri ve sorumluluk iliskileri
    cekirdek modeli            secilen sistemdeki temel yurutme,
                               kaynak ve koruma mekanizmalari

    isletim sistemi cekirdegi   =/=   fiziksel islemci cekirdegi

  BES ROL  ayni varlikta birlesebilir ya da farkli aktorlere dagilabilir
    tasiyici . modeli ureten . eyleyen . gayeyi belirleyen .
    kararlari duzeltme sorumlulugunu tasiyan
~~~

*Çizim 3 — Varlık: model kuran taraf, model ve modelin anlattığı sistem; üç model, beş rol.*

Neler değildir sorusu yakın karışıklıkları ayırmak için kullanılır. Tanım gereği başka bir şey olmak, sorumluluk dışında kalmak, mevcut koşullarda mümkün olmamak ve bir tasarım ilkesi gereği izin verilmemek farklı sınırlardır. Henüz bilinmeyen bir özellik de yok sayılmaz. Bir varlığın kendi hakkında ürettiği açıklama, kapsamı ve doğruluğu incelenmesi gereken bir model olarak ele alınır.

~~~text
  AYRI TUTULUR
    turun tanimi | tekil bir ornegin kimligi | ustlenilen rol |
    mevcut durum

  "ONU O YAPAN NELERDIR?"  ozellikler ayni agirlikta degildir
    kurucu           secilen tanimi olusturur
    ayirt edici      ilgili benzerler arasinda fark yaratir
    durumsal         belirli bir andaki hali anlatir
    sunuma iliskin   varligin nasil temsil edildigini belirler

    ona has olmak, dunyada yalnizca onda bulunan tek bir
    ozellik tasimak demek degildir

  "NELER DEGILDIR?"  dort ayri sinir

                          tanim siniri
                  tanim geregi baska bir seydir
               .---------------------------------.
   sorumluluk  |                                 |  kosul siniri
   siniri      |                                 |
               |           V A R L I K           |  mevcut
   sorumluluk  |                                 |  kosullarda
   disinda     |                                 |  mumkun
   kalir       |                                 |  degildir
               `---------------------------------'
                           ilke siniri
              bir tasarim ilkesi geregi izin verilmez

     . . . . . . . . . .
     .   bilinmeyen    .    sinir degildir: henuz bilinmeyen bir
     . . . . . . . . . .    ozellik yok sayilmaz; ayri tutulur
~~~

*Çizim 4 — Varlık: dört özellik türü ve "neler değildir" sorusunun dört ayrı sınırı.*

Bu protokolün kaydında incelenen birim, tür, tekil kimlik, rol, temel öğeler, ilişkiler ve süreklilik ölçütleri bulunur. Hangi özelliklerin kurucu kabul edildiği, hangi yakın kavramlarla karıştırılmaması gerektiği ve belirsiz kalan noktalar açıklanır. Her önemli ifade tanım, gözlem, varsayım veya tasarım kararı olarak ayırt edilebilir olmalıdır.

### Masaüstünde uygulama

**Girdiler:** 0 başlangıç kaydı, mevcut varlık tanımları, arayüz veya mimari taslakları ve kimlik hakkında açık sorular.

1. İncelenen birimi ve ölçeği bir paragrafla tanımla. Modelin kendisini, modelin anlattığı sistemi ve modeli kuran tarafı adlandır; aynı oldukları iddia ediliyorsa gerekçesini yaz.

2. Kurucu, ayırt edici, durumsal ve sunuma ilişkin özellikleri ayrı kaydet. Ayırt edici sayılan özelliğin hangi benzerler arasında fark yarattığını belirt.

3. Temel öğeleri, aralarındaki ilişkileri ve değişim boyunca korunması gereken koşulları açıkla. Bir öğe veya rol değiştiğinde kimliğin devam edip etmediğini seçilen örnek üzerinden değerlendir.

4. Taşıyıcı, model üreticisi, kullanan veya eyleyen taraf, gayeyi belirleyen taraf ve düzeltme sorumluluğunu eşleştir. Henüz belirlenmemiş rollerin yanına açık soru kaydını bağla.

5. Neler değildir sorusuna verdiğin karşılıkları tanım, sorumluluk, koşul veya ilke sınırı olarak gerekçelendir. Bilinmeyenleri ayrı tut; önemli tanımları Dayanaklar kaydına bağla.

**Üretilecek kayıt:** Çalışma kaydının 1 bölümünde inceleme birimi, kimlik ve rol ayrımı, özellikler, öğeler ve ilişkiler, süreklilik koşulları, taraflar ve gerekçeli sınırlar.

**Tamamlanma koşulu:** Hakkında konuşulan şeyin kapsamı ve kimlik ölçütü anlaşılır; model ile modellenen sistemin ilişkisi açıklanmıştır. Kimliği belirleyen kritik bir soru açık kalıyorsa bölümün durumu bu belirsizliği taşır.

**Geri dönüş koşulu:** Varlığın tanımı, kimlik sınırı, kurucu öğeleri veya rol dağılımı değişirse 1 yeniden açılır; mekân, usul, zaman ve gaye kayıtlarına etkisi incelenir.

## 2 Mekan Protokolü

> Nerededir? Bu yeri, oraya has bir yer yapan nelerdir? Neler değildir?

### Protokol metni

Mekan Protokolü, varlığın hangi çevre içinde bulunduğunu ve bu çevrede hangi ilişkilere katıldığını açıklar. Fiziksel konum, mantıksal konum, kurumsal bağlılık ve ilişkiler içindeki yer ayrı anlamlar taşır. Bir şeyin nerede bulunduğu, kimin sorumluluğunda olduğu, nereden erişilebildiği ve hangi süreçte yer aldığı birbirinin yerine kullanılmaz. İncelenen yerin ölçeği ve sınırı, modelin amacıyla birlikte belirtilir.

Bir yeri oraya has yapan nitelikler; kaynaklar, erişim yolları, giriş ve çıkış koşulları, komşuluklar, aktörler, geçerli kurallar ve mümkün davranışlar üzerinden açıklanır. Yer, koordinatlarının yanında kullanım biçimi ve ilişki düzeniyle anlam kazanır. Aynı fiziksel alan, farklı zamanlarda veya farklı aktörlerle başka işlevler üstlenebilir. Bu nedenle bağlam, sistemin dışındaki önemsiz bir dekor olarak değil, davranışı mümkün veya geçerli kılan koşulların bir bölümü olarak ele alınır.

Sistem sınırı, incelemenin nerede yoğunlaştığını gösterir. Sınır dışında kalan bir öğeden bilgi, kaynak, hizmet veya onay alınıyorsa bu bağımlılık kayda geçirilir. Dışarıda bırakılmak, etkisiz veya önemsiz olmak anlamına gelmez. Sorumluluğun nerede bittiği, hangi koşulla başka tarafa geçtiği ve bu geçişte neyin aktarıldığı açıklanır.

Arayüz ve işletim sistemi incelemesinde görsel yerleşim, mimari sorumluluk, süreç ve adres alanı, işlemci ayrıcalığı ayrı gösterilir. Ekrandaki yakınlık, aynı süreçte bulunmayı; diyagramdaki alt konum, daha yüksek yetkiyi veya belirli bir bellek adresini kendiliğinden göstermez. Bir bileşenin sistem açısından önemli olması da tek başına çekirdek içinde yer almasını gerektirmez. Microsoft'un belgelerinde Windows'un hem kullanıcı hem çekirdek modunda bileşenler içerdiği ve sürücülerin her iki tarafta da bulunabildiği açıklanır. [3]

Bileşenlerin yeri, seçilen işletim sistemi mimarisinden çıkarılır. Linux'te VFS çekirdek içindeki bir dosya sistemi arayüzü olarak tanımlanırken, QNX'te dosya ve aygıt G/Ç işlevlerinin bir bölümü çekirdek dışındaki süreçler ve paylaşılan kütüphanelerle sunulur. Bu örnekler tek bir yerleşim şemasının bütün sistemlere uygulanamayacağını gösterir. Yönetici kimliğiyle verilen erişim hakları da işlemcinin yürütme moduyla aynı kayıt alanında eritilmez. [4] [5] [6]

~~~text
  CIZIMDE AYRI GOSTERILEN DORT SEY
    gorsel yerlesim | mimari sorumluluk | surec ve adres alani |
    islemci ayricaligi

  KONUM KENDILIGINDEN GOSTERMEZ
    ekrandaki yakinlik              -x->   ayni surecte bulunma
    diyagramdaki alt konum          -x->   daha yuksek yetki
    diyagramdaki alt konum          -x->   belirli bir bellek adresi
    sistem acisindan onemli olmak   -x->   cekirdek icinde yer alma

  BILESENIN YERI SECILEN SISTEMDEN CIKARILIR  (metindeki uc ornek)

    Windows               Linux                 QNX
    kullanici modu        cekirdek disi         cekirdek disi
   .----------------.    .----------------.    .------------------.
   | bilesenler     |    |                |    | surecler ve      |
   | suruculer      |    |                |    | paylasilan       |
   |                |    |                |    | kutuphaneler:    |
   |                |    |                |    | dosya ve aygit   |
   |                |    |                |    | G/C islevlerinin |
   |                |    |                |    | bir bolumu       |
   |================|    |================|    |==================|
   | bilesenler     |    | VFS: dosya     |    |                  |
   | suruculer      |    | sistemi        |    |                  |
   |                |    | arayuzu        |    |                  |
   `----------------'    `----------------'    `------------------'
    cekirdek modu         cekirdek ici          cekirdek ici

  anahtar
    kutu          bir isletim sistemi
    cift cizgi    kutunun ustunde ve altinda yazan ayrim
    bos alan      metin orasi icin bir sey soylemiyor (bos demek degil)
    ust / alt     yetki ya da bellek adresi gostermez

  yonetici kimligiyle verilen erisim haklari   =/=   islemcinin
                                                     yurutme modu
~~~

*Çizim 5 — Mekan: çizimde konumun kendiliğinden göstermedikleri; üç sistemde bileşenin yeri.*

Model kuran taraf açısından mekân, erişebildiği, etkileyebildiği, hakkında bilgi edinebildiği ve karar verebildiği ilişkiler alanını da kapsar. Bu dört alanın örtüşmesi zorunlu değildir. Bir yerin temsilini kurmak, oraya doğrudan erişmek; erişmek de oradaki bütün durumu bilmek anlamına gelmez. Modelin bakış noktası ve bilgi sınırı, dünyanın tamamıyla özdeşleştirilmez.

~~~text
  "NEREDEDIR?"  dort ayri anlam
    fiziksel konum | mantiksal konum | kurumsal baglilik |
    iliskiler icindeki yer

  birbirinin yerine kullanilmayan dort soru
    nerede bulunuyor?          kimin sorumlulugunda?
    nereden erisilebiliyor?    hangi surecte yer aliyor?

  SISTEM SINIRI  incelemenin nerede yogunlastigini gosterir

     sinirin disindaki oge             . . . . . . . . . . . . .
     .--------------.   bilgi          .                       .
     |              |   kaynak         .                       .
     |              |----------------->.   incelenen sistem    .
     |              |   hizmet         .                       .
     `--------------'   onay           .                       .
                                       . . . . . . . . . . . . .
     bagimlilik kayda gecer;
     disarida birakilmak, etkisiz ya da onemsiz olmak degildir

  MODEL KURAN TARAFIN DORT ALANI  ortusmeleri zorunlu degildir

     erisebildigi                   |================|
     etkileyebildigi                         |=============|
     hakkinda bilgi edinebildigi    |=========|
     karar verebildigi                    |======|

     bir yerin temsilini kurmak   -x->   oraya dogrudan erismek
     oraya erismek                -x->   oradaki butun durumu bilmek

     modelin bakis noktasi ve bilgi siniri, dunyanin tamamiyla
     ozdeslestirilmez
~~~

*Çizim 6 — Mekan: yerin dört anlamı, sistem sınırı ve model kuran tarafın dört alanı.*

Bu protokolün kaydında fiziksel ve mantıksal yerler, sorumluluk alanları, erişim koşulları, dış bağımlılıklar ve sınır geçişleri açıklanır. Çizimlerde her kutunun hangi tür yeri veya birimi temsil ettiği belirtilir. Bağlam değiştiğinde hangi eylemlerin, izinlerin ve beklentilerin değişeceği de bu kaydın parçasıdır.

### Masaüstünde uygulama

**Girdiler:** 0 başlangıç kapsamı, 1 varlık kaydı, bilinen ortam bilgileri, bağımlılıklar ve varsa mimari çizim.

1. Fiziksel konumu, mantıksal konumu, kurumsal bağlılığı ve ilişkiler içindeki yeri ayrı açıkla. Konum bilgisi bulunmayan alanları bilinmiyor olarak işaretle.

2. Sistem sınırını ve dışarıyla alışverişi belirle. Her önemli bağımlılık için ne alındığını veya verildiğini, tarafını ve koşulunu kaydet.

3. Kaynaklara erişim, onları etkileme, haklarında bilgi edinme ve karar verme alanlarını ayır. Sorumluluğun devredildiği yerleri ve devir koşullarını göster.

4. Mevcut bir çizim varsa kutu ve okların neyi temsil ettiğini yaz. Görsel yerleşim, mimari sorumluluk, süreç, adres alanı ve ayrıcalık ayrımlarını koru; kullanılmayan ayrımlar için kapsam dışı gerekçesini belirt.

5. Seçilen örneğin başka bir ortamda veya farklı bir erişim koşulunda nasıl değişeceğini değerlendir. Değişen işleyiş ve zaman sorularını 3 ve 4'e aktar.

**Üretilecek kayıt:** Çalışma kaydının 2 bölümünde konum ve bağlamlar, sınır, bağımlılıklar, erişim ve sorumluluk alanları, temsil anahtarı ve bağlam değişikliğinin etkileri.

**Tamamlanma koşulu:** İncelenen yerin türü ve ölçeği, önemli sınır geçişleri ve dış bağımlılıklar açıklanmıştır. Çizimdeki konumun hangi ilişkiyi anlattığı belirsiz bırakılmamıştır.

**Geri dönüş koşulu:** Ortam, bağımlılık, erişim veya sorumluluk sınırı değiştiğinde 2 yeniden açılır; özellikle 3 ve 4, gerekiyorsa 1 ve 5 yeniden değerlendirilir.

## 3 Usül Protokolü

> Nasıl işler yapar? Bu yaptıklarını, ona has yapan nelerdir? Neler değildir?

### Protokol metni

Usül Protokolü, bir yetkinliğin hangi mekanizmalarla somut eyleme ve sonuca dönüştüğünü açıklar. Yapabilmek, fiilen yapmak, hangi yöntemle yapmak ve ortaya çıkan sonuç birbirinden ayrılır. Bir işlevin adlandırılması, o işlevin nasıl gerçekleştirildiğini henüz açıklamaz. İşin neden belirli bir yoldan yürütüldüğü, hangi kurallara bağlı olduğu ve hangi koşullarda başka bir yol izlendiği kaydedilir.

Her önemli işlemde başlatan taraf, işlem nesnesi, hedef, gerekli bilgi, yetki, önkoşullar, karar noktaları, kaynak kullanımı, durum değişimi ve sonuç bildirimi ilişkilendirilir. Bir talebin alınmasıyla kaynağın ayrılması veya işin tamamlanması aynı olay olarak yazılmaz. Başarı koşulu, işlemin gerçekten neyi değiştirdiği üzerinden tanımlanır. Sürecin birden çok sorumlusu varsa, her devirde neyin teslim edildiği ve karşı tarafın neyi üstlendiği açıklanır.

İşleyiş; bekleme, başarısızlık, yeniden deneme, iptal, geri alma ve başka bir sorumluya devretmeyi kapsar. Tekrarlanan isteğin yeni bir işlem mi yoksa önceki isteğin devamı mı sayılacağı belirtilir. Yarım kalan işin hangi etkileri üretmiş olabileceği, hangi etkilerin geri alınabileceği ve devam etme kararını kimin vereceği açık tutulur. İstisnalar, modelin dışındaki rastlantılar olarak bırakılmaz.

Arayüz, işleyişin kullanıcı tarafından anlaşılabilen ve kullanılabilen temas düzenidir. Eylemden önce değişecek şey, eylem sırasında bilinen işlem durumu, eylemden sonra gerçekleşen sonuç ve gerekli sonraki adım açıklanır. Bir eylemin mümkün olması ile bu imkânın kullanıcı tarafından anlaşılması farklı tasarım konularıdır. Norman'ın eylem olanakları ve göstergeler ayrımı, mümkün eylemlerin algılanabilir işaretlerle anlaşılır kılınmasına dikkat çeker. [7]

~~~text
  ARAYUZ  isleyisin anlasilabilen ve kullanilabilen temas duzeni

   EYLEMDEN ONCE          EYLEM SIRASINDA        EYLEMDEN SONRA
   degisecek sey          bilinen islem durumu   gerceklesen sonuc,
                                                 gerekli sonraki adim
  .-------------------.  .-------------------.  .-------------------.
  | Rapor             |  | Rapor             |  | Rapor             |
  |                   |  |                   |  |                   |
  | Kaydedince bu     |  | 14:02'deki icerik |  | 14:02'deki icerik |
  | belgedeki         |  | kaydediliyor      |  | kaydedildi.       |
  | degisiklikler     |  |                   |  | Sonraki           |
  | saklanir.         |  |                   |  | degisiklikler     |
  |                   |  |                   |  | kaydedilmedi.     |
  |        [ Kaydet ] |  |        [ Vazgec ] |  |        [ Kaydet ] |
  `-------------------'  `-------------------'  `-------------------'

  eylem olanagi (mumkun olan)   =/=   gosterge (algilanabilir isaret)

  bir eylemin mumkun olmasi ile bu imkanin kullanici tarafindan
  anlasilmasi ayri tasarim konularidir
~~~

*Çizim 7 — Usül: arayüzde üç an; eylemden önce, eylem sırasında, eylemden sonra.*

Teknik modelde kullanıcı eylemi, uygulama işlemi, kütüphane çağrısı, sistem çağrısı ve süreçler arası mesajlaşma ayrı ilişkiler olarak gösterilir. Linux'te sistem çağrıları uygulama ile çekirdek arasındaki temel arayüzdür ve çoğunlukla kütüphane sarmalayıcıları üzerinden çağrılır. Bundan her kullanıcı eyleminin tek bir sistem çağrısına veya her sistem çağrısının doğrudan aygıt erişimine karşılık geldiği sonucu çıkarılmaz. Çizimlerde çağrı, veri aktarımı, olay bildirimi, sahiplik ve bağımlılık oklarının anlamı belirtilir. [8]

Çekirdeğe giriş ile başka bir iş parçacığına geçiş ayrı olaylardır. İşlemci modu, yürütme bağlamı ve zamanlama kararı birbirinin yerine kullanılmaz. QNX belgeleri, çekirdeğe girişte alınabilen zamanlama kararlarını, bir işin engellenmesi, öncelik nedeniyle kesilmesi veya işlemciyi bırakmasıyla bağlantılı bağlam değişimleri üzerinden açıklar. Çekirdek alt sistemleri de bütün işlemlerin sırayla geçtiği zorunlu bir merdiven gibi değil, görevleri ve ilişkileri belirtilen sorumluluk alanları olarak modellenir. [9]

~~~text
  TEKNIK MODELDE AYRI GOSTERILEN BES ILISKI
    kullanici eylemi . uygulama islemi . kutuphane cagrisi .
    sistem cagrisi . surecler arasi mesajlasma

  Linux ornegi
    uygulama -> kutuphane sarmalayicisi -> sistem cagrisi -> cekirdek
                (cogunlukla)               (temel arayuz)

  bundan cikarilmayan iki sonuc
    her kullanici eylemi   -x->   tek bir sistem cagrisi
    her sistem cagrisi     -x->   dogrudan aygit erisimi

  OKLARIN ANLAMI BELIRTILIR
    ----->  cagri              =====>  veri aktarimi
    - - ->  olay bildirimi     ----o   sahiplik
    .....>  bagimlilik

  BIRBIRININ YERINE KULLANILMAZ
    islemci modu | yurutme baglami | zamanlama karari
    cekirdege giris   =/=   baska bir is parcacigina gecis

  CEKIRDEK ALT SISTEMLERI
    boyle degil: zorunlu merdiven       boyle: sorumluluk alanlari

        .-------.                         .-------.     .-------.
        |       |                         |       |-----|       |
        `---+---'                         `---+---'     `---+---'
            v                                 |             |
        .-------.                         .---+---.         |
        |       |                         |       |---------'
        `---+---'                         `-------'
            v
        .-------.                         gorevleri ve iliskileri
        |       |                         belirtilir
        `-------'
    butun islemler sirayla gecer
~~~

*Çizim 8 — Usül: teknik modelde beş ilişki, okların anlamı; merdiven değil sorumluluk alanları.*

Model kurma usulü açısından girdi alma, ilgili olanı seçme, ayrım yapma, temsil kurma, çıkarımda bulunma, eylem veya tasarım seçme ve sonucu değerlendirme adımları incelenebilir. Bu sıra, konuşmada önerilmiş bir çözümleme düzenidir; bütün makineler için evrensel bir algoritma olarak kabul edilmez. Aynı veriden farklı modeller çıkması, farklı amaçlara, kapsamlara veya varsayımlara dayanabilir.

~~~text
  MODEL KURMA USULU                     AYNI VERIDEN FARKLI MODELLER

    girdi alma                                         .--> model
        v                                              |
    ilgili olani secme                  ayni veri -----+--> model
        v                                              |
    ayrim yapma                                        `--> model
        v
    temsil kurma                        fark sunlara dayanabilir:
        v                                 amaclar
    cikarimda bulunma                     kapsamlar
        v                                 varsayimlar
    eylem ya da tasarim secme
        v
    sonucu degerlendirme

  bu sira, konusmada onerilmis bir cozumleme duzenidir;
  butun makineler icin evrensel bir algoritma olarak kabul edilmez
~~~

*Çizim 9 — Usül: model kurmanın yedi adımı; aynı veriden farklı modeller.*

Bu protokolün kaydı, önemli işlemler için anlaşılır bir işlem sözleşmesi üretir. Niyet, hedef, önkoşullar, işleme giren içerik, başarı koşulu, hata etkileri, iptal ve yeniden deneme anlamı, sorumlular ve görünür sonuç birbiriyle bağlanır. Arayüzün verdiği anlam ile yürütülen işlemin anlamı bu sözleşme üzerinden karşılaştırılır.

~~~text
  AYRILAN DORT SEY
    yapabilmek | fiilen yapmak | hangi yontemle yapmak |
    ortaya cikan sonuc

  AYNI OLAY OLARAK YAZILMAZ
    talebin alinmasi  =/=  kaynagin ayrilmasi  =/=  isin tamamlanmasi

  .---------------------- ISLEM SOZLESMESI ------------------------.
  | niyet                     |                                    |
  | hedef                     |                                    |
  | onkosullar                |                                    |
  | isleme giren icerik       |                                    |
  | basari kosulu             | islem gercekten neyi degistirdi?   |
  | hata etkileri             | yarim kalan is hangi etkileri      |
  |                           | uretmis olabilir?                  |
  | iptal ve yeniden deneme   | tekrarlanan istek yeni bir islem   |
  |   anlami                  | mi, onceki istegin devami mi?      |
  | sorumlular                | her devirde ne teslim edildi,      |
  |                           | karsi taraf neyi ustlendi?         |
  | gorunur sonuc             |                                    |
  `----------------------------------------------------------------'

    arayuzun verdigi anlam  <--- karsilastirilir --->  yurutulen
                                                        islemin anlami

  ISLEYISIN PARCASIDIR  (modelin disindaki rastlanti degil)
    bekleme . basarisizlik . yeniden deneme . iptal . geri alma .
    baska bir sorumluya devretme
~~~

*Çizim 10 — Usül: işlem sözleşmesi; arayüzün verdiği anlam ile yürütülen işlemin anlamı.*

### Masaüstünde uygulama

**Girdiler:** Seçilen örnek durum, 1 varlık kaydı, 2 bağlam ve yetki sınırları, mevcut işlem açıklamaları.

1. Örnekteki önemli işlemi seç. İşlemi başlatan tarafı, işlem nesnesini, niyeti, önkoşulları, gerekli bilgiyi ve yetkiyi kaydet.

2. İşin başlangıçtan sonuca kadar adımlarını yaz. Her adımda sorumlu tarafı, kullanılan kaynağı, yapılan durum değişikliğini ve diğer tarafa aktarılan şeyi belirt.

3. Başarı koşulunu ve kullanıcıya verilen sonucu karşılaştır. Kullanıcı eylemi, uygulama işlemi, çağrı, mesaj ve veri aktarımı kullanılıyorsa bunları ayrı ilişkilendir.

4. İlgili hata, bekleme, yeniden deneme, iptal ve geri alma durumlarını incele. Tekrarlanan isteğin anlamını ve yarım kalan işin olası etkilerini yaz; ilgili olmayan durumları gerekçesiyle belirt.

5. Arayüzde eylem öncesi, işlem sırası ve sonuç sonrasında hangi bilginin görüneceğini açıkla. Senaryoyu masaüstünde adım adım değerlendir; beklenen davranışla gözlenen davranışı karıştırmadan zamanla ilgili soruları 4'e aktar.

**Üretilecek kayıt:** Çalışma kaydının 3 bölümünde işlem sözleşmesi, adımlar ve sorumlular, durum değişimleri, başarı ve hata anlamları, iptal ve tekrar koşulları, görünür sonuç.

**Tamamlanma koşulu:** Önemli işlemin hangi koşulla başlayıp hangi sonuçla biteceği ve ilgili istisnaların anlamı açıklanmıştır. Masaüstünde incelenen bir işlem, gerçek sistemde yürütülmüş gibi kaydedilmez.

**Geri dönüş koşulu:** İşleyiş, sorumluluk devri, başarı, hata, iptal veya yeniden deneme anlamı değiştiğinde 3 yeniden açılır; 4 ve 5 ile bağı kontrol edilir.

## 4 Zaman Protokolü

> Hangi andadır? Bu anı, diğer zamanlardan farklı yapan nelerdir? Neler değildir?

### Protokol metni

Zaman Protokolü, varlığın hangi durum ve geçerlilik koşulları içinde bulunduğunu açıklar. Saat zamanı, süreç evresi, geçerlilik süresi, kararı etkileyen geçmiş ve açık gelecek seçenekleri ayrı tutulur. Bir anı ayırt eden, yalnızca tarih ve saat değil; hangi işlerin sürmekte olduğu, hangi kaynakların tutulduğu, hangi hakların geçerli kaldığı ve hangi geçişlerin mümkün olduğudur.

Olayın gerçekleştiği an, sistemin olayı öğrendiği an ve öğrendiği bilgiye göre davranışını değiştirdiği an farklı olabilir. Sistemin gerçek durumu ile bu duruma ilişkin bilginin güncelliği ayrı kaydedilir. Bir arayüzde görülen durumun hangi gözleme veya işleme dayandığı anlaşılabilir olmalıdır. Sonucu henüz doğrulanamayan işlem doğrudan başarısız sayılmaz; bilinmeyen durum, bilinen bir olumsuz sonuçtan ayrılır.

İşlemin başlatılması, kabul edilmesi, sıraya alınması, yürütülmesi, tamamlanması, gerekiyorsa kalıcılaşması ve sonucunun bildirilmesi farklı eşikler olarak incelenir. Her işlem bütün bu aşamaları aynı biçimde kullanmak zorunda değildir; ilgili ayrımlar somut sözleşmede belirtilir. İzin, teklif veya ayırtma hakkı gibi geçici koşullar için başlangıç, sona erme ve yeniden değerlendirme anları kayda geçirilir.

Eşzamanlı işlerde içerik sürümü ile işlem sırası birlikte izlenir. Bir belgenin 7. sürümü kaydedilirken kullanıcı 8. sürümü oluşturmuşsa, 7. sürümün başarıyla kaydedilmesi ekrandaki güncel içeriğin tamamının kaydedildiğini göstermez. Kullanıcıya teknik sürüm numarası göstermek zorunlu değildir; fakat uygulama tamamlanan işlemi doğru içerikle ilişkilendirmelidir. Eski bir kaydın daha geç tamamlanarak yeni içeriğin üzerine yazmasını önleyen sıra veya sürüm kuralı da açıklanır.

~~~text
  zaman  ----------------------------------------------------------->

  ekrandaki       [ surum 7 ]                    [ surum 8 ]
  icerik               |       kullanici yazmayi surdurur
                       | kaydetme baslar
                       v
  kayit islemi         ( ..... surum 7 kaydediliyor ..... )  basarili
                                                                 |
                                                                 v
  bildirim                                                 "kaydedildi"

     "kaydedildi"   =     surum 7 kaydedildi
                    =/=   ekrandaki guncel icerigin tamami kaydedildi

  ONLENMESI GEREKEN  eski kayit gec tamamlanir, yenisinin ustune yazar

  kayit A (surum 7)   |------------------------------------>| biter
  kayit B (surum 8)            |------------->| biter
  depoda kalan                                 surum 8       surum 7 (!)

  bunu onleyen: sira ya da surum kurali

  kullaniciya surum numarasi gostermek zorunlu degildir; ama uygulama
  tamamlanan islemi dogru icerikle iliskilendirmelidir
~~~

*Çizim 11 — Zaman: 7. sürüm kaydedilirken 8. sürüm oluşur; "kaydedildi" neyi söyler.*

Yazma, eksiksiz aktarım, tutarlı görünüm ve kalıcılık aynı koşul sayılmaz. Linux'te başarılı bir write çağrısı, verinin diske kalıcı biçimde aktarılmış olduğunu garanti etmez ve istenen miktardan daha az veri yazılmış olabilir. fsync dosya verisinin ve ilgili üst verinin depolamaya aktarılmasıyla ilgilidir; dosyanın bulunduğu dizin kaydı için ek işlem gerekebilir. Bu örnek platforma özgü kapsamıyla korunur. Kaydedildi ifadesinin hangi tamamlanma güvencesine dayandığı seçilen uygulama, API ve depolama düzeni üzerinden belirlenir. [10] [11]

Zaman, yaşam evresi ölçeğinde de ele alınır. Kuruluş, hazırlık, olağan kullanım, bakım, askıya alma, devam etme ve kapanış gibi evreler için hangi hizmetlerin kullanılabilir sayıldığı ve hangi yeni işlerin kabul edildiği belirtilir. Bir varlık aynı yerde ve aynı kullanıcıyla karşılaşsa bile, farklı evrelerde farklı eylemlere açık olabilir. Kural sürümünün değişmesi de görünür nesne aynı kaldığında bile işlemin anlamını etkileyebilir.

~~~text
  UC AYRI AN
    olay gerceklesir  -->  sistem olayi ogrenir  -->  sistem
                                                      davranisini
                                                      degistirir
    sistemin gercek durumu   =/=   o duruma iliskin bilginin guncelligi
    sonucu henuz dogrulanamayan islem   =/=   basarisiz islem

  ISLEMIN ESIKLERI  (her islem hepsini ayni bicimde kullanmaz)

    ---|--------|--------|--------|--------|--------|--------|--->
       1        2        3        4        5        6        7

    1 baslatilma     2 kabul edilme     3 siraya alinma
    4 yurutulme      5 tamamlanma       6 kalicilasma (gerekiyorsa)
    7 sonucun bildirilmesi

    arayuzdeki durum ifadesi hangi esige dayaniyor?

  AYNI KOSUL SAYILMAZ
    yazma | eksiksiz aktarim | tutarli gorunum | kalicilik

  Linux ornegi  (platforma ozgu kapsamiyla)
    basarili write   -x->   veri diske kalici bicimde aktarildi
    basarili write   -x->   istenen miktarin tamami yazildi
    fsync                   dosya verisinin ve ilgili ust verinin
                            depolamaya aktarilmasiyla ilgilidir;
                            dosyanin bulundugu dizin kaydi icin
                            ek islem gerekebilir

  YASAM EVRESI OLCEGI
    kurulus . hazirlik . olagan kullanim . bakim . askiya alma .
    devam etme . kapanis
    her evre icin: hangi hizmetler kullanilabilir sayilir,
    hangi yeni isler kabul edilir
~~~

*Çizim 12 — Zaman: üç ayrı an, işlemin eşikleri, tamamlanma güvencesi ve yaşam evreleri.*

Model kuran taraf açısından zaman, modelin hangi bilgiyle kurulduğunu ve hangi yeni bilgiyle değiştirildiğini kapsar. Geçmişe ilişkin kayıt, geçmişin bütünü olarak sunulmaz; seçilmiş bilgiyi taşır. Hangi bilgilerin korunduğu, hangilerinin dışarıda bırakıldığı ve bunların sonraki kararlara etkisi belirtilir. Bir zaman damgası, bu ilişkilerin tümünün yerine geçmez.

Bu protokolün kaydında durumlar, geçiş olayları, önkoşullar, süreler, bilgi güncelliği, işlem sırası, içerik ve kural sürümleri bulunur. Tamamlanma, geri dönüş ve yeniden açılma koşulları açıklanır. Geç gelen sonuçların nasıl değerlendirileceği ve eşzamanlı işlemlerde hangi durumun esas alınacağı da kayıt altına alınır.

### Masaüstünde uygulama

**Girdiler:** 3 işlem kaydı, olay ve durum bilgileri, içerik veya kural sürümleri, geçerlilik ve süre koşulları.

1. İlgili durumları ve aralarındaki geçişleri yaz. Her geçişin olayını, önkoşulunu ve sonucunu belirt; saat zamanı ile süreç evresini ayrı kaydet.

2. Olayın gerçekleşmesi, öğrenilmesi ve davranışa yansıması için bilinen zamanları ayır. Zaman bilinmiyorsa tahmin üretmek yerine belirsizliği ve etkisini kaydet.

3. Başlama, kabul, yürütme, tamamlanma, gerekiyorsa kalıcılık ve bildirim eşiklerini işlem sözleşmesine bağla. Arayüzdeki durum ifadesinin hangi eşiğe dayandığını belirt.

4. Örneği eşzamanlılık veya geç gelen sonuç açısından değerlendir. İşlemin içerik ve kural sürümüyle nasıl eşleştiğini, eski bir sonucun daha yeni durumu nasıl etkileyeceğini açıkla.

5. Süre, sona erme, bakım, askıya alma, devam etme ve kapanış gibi ilgili koşulları yaz. Güncelliğini yitiren bilginin ve yeniden açılan işlemin nasıl ele alınacağını belirle.

**Üretilecek kayıt:** Çalışma kaydının 4 bölümünde durumlar, geçişler, olay ve bilgi zamanı, tamamlanma eşikleri, işlem sırası, sürümler ve geçerlilik koşulları.

**Tamamlanma koşulu:** Hangi durumun ne zaman geçerli olduğu, tamamlanmanın ne anlama geldiği ve bilginin güncellik sınırı açıklanmıştır. Eşzamanlılık uygulanıyorsa sonuçların doğru iş ve sürümle eşleştirilmesi ele alınmıştır.

**Geri dönüş koşulu:** Olay sırası, içerik veya kural sürümü, geçerlilik, güncellik ya da tamamlanma güvencesi değişirse 4 yeniden açılır; etkilenen işlem için 3, amaçlanan sonuç için 5 değerlendirilir.

## 5 Gaye Protokolü

> Hangi nihai amaca hizmet eder? Bu nihai amaca ulaştıran nelerdir? Neler değildir?

### Protokol metni

Gaye Protokolü, sistemin veya modelleme çalışmasının ne için var olduğunu, kime yarar sağlamasının beklendiğini ve başarının kim tarafından tanımlandığını açıklar. Kullanıcı, tasarımcı, işletici, kurum ve etkilenen diğer tarafların amaçlarının aynı olduğu peşinen varsayılmaz. Amaçların çakıştığı yerde hangi kararın kim tarafından ve hangi gerekçeyle verileceği belirtilir.

Nihai amaç, seçilen inceleme düzeyinde diğer işlerin hizmet ettiği üst amaç olarak kullanılır. Bir düğmenin, uygulamanın, hizmetin ve kurumun amaçları farklı ölçeklerde tanımlanabilir. Bu kullanım, bütün sistemlerin tek ve mutlak bir gayesi bulunduğu iddiasını taşımaz. Amaç, bazen ulaşılıp tamamlanan bir sonuç; bazen de erişilebilirlik, güvenilirlik veya paylaşım gibi sürekli korunması gereken bir koşuldur.

Faaliyet, çıktı, kullanıcı açısından sonuç ve daha geniş değer ayrı tutulur. Bir talebi işlemek faaliyet; kayıt oluşturmak çıktı; ihtiyaç duyulan kaynağa ulaşmak kullanıcı açısından sonuç olabilir. İşlem sayısının veya başka bir ölçütün artması, amacın gerçekleştiğini tek başına kanıtlamaz. Ölçütlerin hangi sonucu temsil ettiği, hangi sınırlar içinde anlamlı olduğu ve hangi yan etkileri görünmez bırakabileceği açıklanır.

~~~text
  AYRI TUTULAN DORT SEY                    metindeki ornek

    faaliyet                               bir talebi islemek
       |
       v
    cikti                                  kayit olusturmak
       |
       v
    kullanici acisindan sonuc              ihtiyac duyulan kaynaga
       |                                   ulasmak
       v
    daha genis deger

    islem sayisinin ya da baska bir olcutun artmasi, amacin
    gerceklestigini tek basina kanitlamaz

  NIHAI AMAC  secilen inceleme duzeyinde, diger islerin hizmet
              ettigi ust amac

    dugme . uygulama . hizmet . kurum      amaclari farkli olceklerde
                                           tanimlanabilir

    amac bazen ulasilip tamamlanan bir sonuctur;
    bazen surekli korunmasi gereken bir kosuldur
    (erisilebilirlik, guvenilirlik, paylasim gibi)

    bu kullanim, butun sistemlerin tek ve mutlak bir gayesi
    bulundugu iddiasini tasimaz
~~~

*Çizim 13 — Gaye: faaliyet, çıktı, kullanıcı açısından sonuç ve değer; amacın ölçeği.*

Amaca ulaştırdığı öne sürülen her önemli araç için etki gerekçesi kurulur. Bir kuralın veya tasarım kararının hangi davranışı değiştireceği, bu değişimin beklenen sonuca nasıl katkı sağlayacağı ve katkının neye dayanarak değerlendirileceği belirtilir. Hız, sadelik, katman sayısı, özellik sayısı veya kod miktarı kendi başına nihai gaye olarak kabul edilmez; ilgili kullanım bağlamındaki katkıları üzerinden değerlendirilir.

Model kuran fail açısından verilen hedef, oluşturulan ara hedefler, fiilî sonuçlar ve sonuçların kim için değerli olduğu farklı kayıtlardır. Bir gayeyi işleyişinde temsil etmek, o gayenin değerini veya gerekçesini belirlemekle aynı rol değildir. Bir modelin gayesi, modelin anlattığı sistemin gayesi ve modelleme çalışmasını isteyen tarafın gayesi de ayrı olabilir. Simon'ın tasarım yaklaşımı, iç düzenin dış koşullarla amaçlara ulaşacak biçimde ilişkilendirilmesini ele alır. [12]

Arayüzün gayesi, kullanıcının işlem nesnesini anlaması, niyetini ifade etmesi ve sonucu değerlendirebilmesiyle ilişkilendirilir. İşletim sistemi mimarisinin gayesi, hedeflenen işlerin belirli kaynak ve erişim kuralları içinde yürütülmesidir. Çekirdek modeli ise üstteki yazılımların dayanacağı temel yürütme, kaynak, iletişim ve koruma koşullarını açıklar. Kullanıcı açısından anlamlı sonucun oluşması, bu sorumlulukların birbirini tamamlamasına bağlı olarak değerlendirilir; bütün amaç belirleme yetkisi çekirdeğe yüklenmez.

Tanımlanan gereksinimlerin karşılanması ile ortaya çıkan sistemin amaçlanan ortamda ilgili kişilerin ihtiyacını karşılaması ayrı değerlendirmelerdir. NASA'nın doğrulama ve geçerleme ayrımı bu iki soruyu birlikte ele alır. [13] Amaç iddiası, somut kullanım ve sonuç bilgisiyle karşılaştırılır. Doğal sistemlere genişletilen incelemelerde ise gözlenen işlev veya sonuçtan doğrudan niyet çıkarılmaz; amaç atfının ayrıca gerekçelendirilmesi gerekir.

~~~text
  AYRI OLABILEN UC GAYE
    modelin gayesi | modelin anlattigi sistemin gayesi |
    modelleme calismasini isteyen tarafin gayesi

  MODEL KURAN FAIL ACISINDAN DORT AYRI KAYIT
    verilen hedef . olusturulan ara hedefler . fiili sonuclar .
    sonuclarin kim icin degerli oldugu

    bir gayeyi isleyisinde temsil etmek   =/=   o gayenin degerini ya da
                                                gerekcesini belirlemek

  UC KATMANIN GAYESI
    arayuz              kullanici islem nesnesini anlar, niyetini
                        ifade eder, sonucu degerlendirebilir
    isletim sistemi     hedeflenen isler belirli kaynak ve erisim
    mimarisi            kurallari icinde yurutulur
    cekirdek modeli     ustteki yazilimlarin dayanacagi temel yurutme,
                        kaynak, iletisim ve koruma kosullarini aciklar

    butun amac belirleme yetkisi cekirdege yuklenmez

  IKI AYRI DEGERLENDIRME
    tanimlanan gereksinimler karsilandi mi?             dogrulama
    ortaya cikan sistem, amaclanan ortamda ilgili
    kisilerin ihtiyacini karsiliyor mu?                 gecerleme

  KENDI BASINA NIHAI GAYE SAYILMAZ
    hiz . sadelik . katman sayisi . ozellik sayisi . kod miktari
~~~

*Çizim 14 — Gaye: ayrı olabilen üç gaye, üç katmanın gayesi ve iki ayrı değerlendirme.*

Bu protokolün kaydında üst amaç, yararlanıcılar, amaç belirleme ve değiştirme yetkisi, ara hedefler, başarı koşulları, sınırlar ve değerlendirme kanıtları bulunur. Beklenen sonuç ile gözlenen sonuç ayrı yazılır. Gaye değiştiğinde varlık tanımının, bağlamın, işleyişin, zaman koşullarının ve arayüzde verilen anlamın nasıl etkileneceği yeniden incelenir.

### Masaüstünde uygulama

**Girdiler:** 0 başlangıç yönelimi, 1–4 kayıtları, yararlanıcı beklentileri ve varsa sonuç bulguları.

1. Üst amacı seçilen inceleme ölçeğinde yaz. Amaçtan yararlanacak ve etkilenecek tarafları, amacı belirleyen veya değiştirebilen tarafları açıkla.

2. Faaliyet, çıktı, kullanıcı açısından sonuç ve daha geniş değeri örnek üzerinden ayır. Tamamlanan iş ile karşılanan ihtiyacın hangi koşullarda örtüştüğünü belirt.

3. Başlıca kural ve tasarım kararları için beklenen etkiyi yaz. Aracın hangi davranışı değiştireceğini ve bunun amaca nasıl katkı sağlayacağını gerekçelendir.

4. Başarı koşullarını ve kullanılacak göstergeleri tanımla. Göstergenin anlamlı olduğu sınırı, amaçlar arasındaki çatışmaları ve kabul edilebilir sonucu değerlendir.

5. Beklenen sonucu eldeki bulgularla karşılaştır. Sonuç bulunmuyorsa beklentiyi varsayım olarak koru. Amaca ulaşıldığı iddiasını zayıflatacak bir karşı örnek düşün ve 6 bütünlük incelemesine aktar.

**Üretilecek kayıt:** Çalışma kaydının 5 bölümünde üst amaç, yararlanıcılar, amaç belirleme yetkisi, faaliyet ve sonuç ayrımı, etki gerekçesi, başarı koşulları, göstergeler ve bulgular.

**Tamamlanma koşulu:** Başarının kim açısından ve hangi koşullarla değerlendirileceği anlaşılır; araçların amaçla ilişkisi açıklanmıştır. Beklenti, ölçüt ve gözlenen sonuç ayrı kaydedilmiştir.

**Geri dönüş koşulu:** Gaye, yararlanıcı, amaç belirleme yetkisi veya başarı ölçütü değiştiğinde 5 yeniden açılır. 0'daki başlangıç yönelimi ve 1–4 üzerindeki etkiler değerlendirilir.

## 6 Kökleşme (Bitiş) Protokolü

> Açıklığa kavuşan bu düzen, hangi dayanaklarla kullanılabilir, sürdürülebilir ve gerektiğinde yeniden ele alınabilir hâle geldi?

### Protokol metni

Kökleşme Protokolü, 1–5 boyunca oluşturulan açıklamaları birlikte değerlendirir ve mevcut inceleme turunun sonucunu kayda geçirir. Varlık tanımının, mekân ilişkilerinin, usulün, zaman koşullarının ve gayenin birbirini destekleyip desteklemediği incelenir. Her bölümün kendi içinde anlaşılır olması, bütünün tutarlı olduğu sonucunu tek başına vermez.

Kökleşmenin kurucu niteliği, oluşturulan modelin kullanım ve devamlılık koşullarıyla ilişkilendirilmesidir. Tanımlanan varlığın belirtilen çevrede nasıl yer aldığı, işleyişin hangi kaynak ve yetkilerle yürüyebildiği, zaman koşullarının beklenen sonucu nasıl etkilediği ve sonucun gayeye nasıl katkı sağladığı birlikte değerlendirilir. Çelişki veya eksik bulunduğunda ilgili protokole dönülür; değişikliğin diğer bölümlere etkisi de kaydedilir.

Bu aşamada başlangıca yeniden bakılır. Tohumda ortaya konan sorunun ne ölçüde karşılandığı, başlangıçtaki hangi varsayımların değiştiği ve hangi ihtiyaçların açık kaldığı açıklanır. Amaç değişmişse önceki amaç sessizce yenisiyle değiştirilmez; değişikliğin gerekçesi ve sonuçları belirtilir.

Kökleşme kaydı, modelin hangi düzeyde değerlendirildiğini gösterir. Metnin gözden geçirilmesi, masaüstünde senaryo incelemesi, prototip üzerinde deneme ve gerçek kullanım bulguları ayrı dayanak türleridir. Bir senaryonun metin üzerinde tutarlı ilerlemesi, gerçek sistemde başarıyla gerçekleştirildiği şeklinde yazılmaz. Uygulama bulgusu yoksa uygulamada sınanmadı kaydı korunur.

Devamlılık için esas alınan sürüm, geçerli bağlam, kullanım sınırları, kaynaklar, açık konular ve güncelleme sorumluluğu belirtilir. Bir sorumluluk henüz üstlenilmemişse atama yapılmış gibi gösterilmez. Başka bir uygulayıcının mevcut sonucu, gerekçelerini ve devam edecek işi anlayabilmesi bu kaydın bir parçasıdır.

Kökleşme, yalnızca dosyayı kaydetmek, metni yayımlamak veya çalışmaya tamamlandı etiketi eklemek değildir. Modelin değişmez ilan edilmesi ya da bilinmeyenlerin ortadan kalkmış sayılması da değildir. Bitiş, mevcut inceleme turunun hangi sonuçla kapandığını belirtir; yeni bulgular karşısında yeniden açılma koşullarını korur.

~~~text
  DORT DAYANAK TURU  ayri yazilir

                                             .----------------------
                                             | gercek kullanim
                              .--------------' bulgulari
                              | prototip uzerinde
                .-------------' deneme
                | masaustunde senaryo
     .----------' incelemesi
     | metnin gozden
     | gecirilmesi

     bir senaryonun metin uzerinde tutarli ilerlemesi, gercek
     sistemde basariyla gerceklestirildigi seklinde yazilmaz

     birlikte kaydedilebilir:
       masaustu incelemesi tamamlandi   +   uygulamada sinanmadi

  BUTUNLUK
     varlik --- mekan --- usul --- zaman --- gaye
     her bolumun kendi icinde anlasilir olmasi, butunun tutarli
     oldugu sonucunu tek basina vermez
     celiski ya da eksik bulunursa ilgili protokole donulur

  BASLANGICA YENIDEN BAKILIR
     tohumdaki soru ne olcude karsilandi?
     baslangictaki hangi varsayimlar degisti?
     hangi ihtiyaclar acik kaldi?

  KOKLESME SUNLAR DEGILDIR
     yalnizca dosyayi kaydetmek . metni yayimlamak .
     calismaya tamamlandi etiketi eklemek .
     modeli degismez ilan etmek .
     bilinmeyenleri ortadan kalkmis saymak
~~~

*Çizim 15 — Kökleşme: dört dayanak türü, bütünlük, başlangıca yeniden bakış.*

Bu protokolün kaydı; bütünlük değerlendirmesi, başlangıç sorusuna verilen karşılık, kanıt düzeyi, geçerlilik sınırı, açık konular, esas sürüm ve yeniden açılma koşullarını içerir. Kapanış kararı eldeki dayanağın düzeyini taşır. Masaüstü incelemesinin tamamlanması ile kullanım içinde kökleşmenin gösterilmesi ayrı sonuçlar olarak kaydedilir.

### Masaüstünde uygulama

**Girdiler:** 0–5 kayıtları, seçilen örnek, dayanaklar, açık sorular, değişiklikler ve varsa prototip veya gerçek kullanım bulguları.

1. 0–5 kayıtlarını birlikte aç. Başlangıç sorusuyla her bölümün sonucunu karşılaştır; kimlik, kapsam, sorumluluk, durum ve amaç bakımından bulunan uyumları veya çelişkileri kaydet.

2. Seçilen örneği başlangıcından sonucuna kadar masaüstünde incele. İlgili bir hata, bekleme veya bağlam değişikliği durumunu da değerlendir; her önemli adımı ilgili protokol kaydına bağla.

3. Beklenen sonucu, masaüstü incelemesinde ulaşılan sonucu ve varsa uygulama bulgusunu ayrı yaz. Her önemli sonucun dayanağını, kapsamını ve bilinen sınırını belirt.

4. Çelişkileri ilgili 0–5 bölümlerine dönerek gider. Açık kalan konuların etkisini, hangi kullanımları sınırladığını, biliniyorsa sorumlusunu ve yeniden ele alma koşulunu kaydet.

5. Esas alınacak kayıt sürümünü, geçerli bağlamı, kullanım sınırlarını, kaynakları ve güncelleme sorumluluğunu yaz. Başlangıç yöneliminde oluşan değişikliği gerekçesiyle açıkla.

6. İnceleme turunun sonucunu kanıt düzeyini belirterek kaydet. Kapanabiliyorsa kapanış nedenini ve yeniden açılma koşullarını yaz; kritik çelişki sürüyorsa açık veya engelli durumunu koru.

**Üretilecek kayıt:** Çalışma kaydının 6 bölümünde bütünlük ve senaryo değerlendirmesi, başlangıç sorusuna karşılık, kanıt düzeyi, geçerlilik sınırı, açık konular, esas sürüm, sorumluluk ve kapanış veya yeniden açılma kaydı.

**Tamamlanma koşulu:** Mevcut incelemenin sonucu, sınırları ve açık konuları görünürdür; kapanış kararını değiştiren bir çelişki gizlenmemiştir. Kapanış kararını değiştiren kritik bir çelişki sürüyorsa kayıt tamamlanabilir; inceleme turunun durumu açık veya engelli olarak kalır. Masaüstü incelemesi tamamlandı ve uygulamada sınanmadı birlikte kaydedilebilir. Kullanım içinde kökleşme iddiası ilgili kullanım bulgularıyla desteklenir.

**Geri dönüş koşulu:** Yeni bilgi, başarısız sonuç, değişen koşul, kapsam veya gaye önce ilgili 0–5 bölümünü yeniden açar. Değişikliklerin etkisi değerlendirildikten sonra 6 kapanış kaydı güncellenir; her değişiklikte bütün çalışmayı baştan yapmak gerekmez.

## Değişiklik ve geri dönüş düzeni

| Değişiklik | Öncelikle yeniden açılacak protokol | Bağlantılı inceleme |
| --- | --- | --- |
| Başlangıç ihtiyacı, konu veya kapsam | 0 Tohum | 1–5 üzerindeki etkiler |
| Varlık tanımı veya kimlik sınırı | 1 Varlık | 2, 3, 4 ve 5 |
| Ortam, bağımlılık, erişim veya sorumluluk | 2 Mekan | 3 ve 4; gerektiğinde 1 ve 5 |
| İşleyiş, başarı, hata veya iptal anlamı | 3 Usül | 4 ve 5 |
| Sürüm, olay sırası, geçerlilik veya tamamlanma | 4 Zaman | Etkilenen işlem için 3; sonuç için 5 |
| Gaye, yararlanıcı veya başarı ölçütü | 5 Gaye | 0'daki yönelim ve 1–4 |
| Kapanışta çelişki veya dayanak eksikliği | İlgili 0–5 bölümü | 6 kapanış kaydı |

Bu tablo uygulayıcının değişikliği değerlendirmesine yardımcı olur. Etkilenmeyen kayıtlar gerekçe olmadan yeniden yazılmaz. Yeniden açılan bölümler değerlendirildikten sonra 6'daki sonuç güncellenir.

~~~text
  DEGISEN                      0     1     2     3     4     5     6
  ---------------------------------------------------------------------
  baslangic ihtiyaci, konu    [A]    o     o     o     o     o     +
  veya kapsam
  varlik tanimi veya                [A]    o     o     o     o     +
  kimlik siniri
  ortam, bagimlilik, erisim         (o)   [A]    o     o    (o)    +
  veya sorumluluk
  isleyis, basari, hata                         [A]    o     o     +
  veya iptal anlami
  surum, olay sirasi,                            o    [A]    o     +
  gecerlilik veya tamamlanma
  gaye, yararlanici veya       o     o     o     o     o    [A]    +
  basari olcutu
  kapanista celiski veya      [?]   [?]   [?]   [?]   [?]   [?]    o
  dayanak eksikligi

  [A]  oncelikle yeniden acilan protokol
   o   baglantili inceleme        (o)  gerektiginde
  [?]  ilgili 0-5 bolumu (hangisi ise o acilir)
   +   yeniden acilan bolumler degerlendirildikten sonra
       6'daki sonuc guncellenir

  etkilenmeyen kayitlar gerekce olmadan yeniden yazilmaz
~~~

*Çizim 16 — Değişiklik ve geri dönüş düzeni: hangi değişiklik hangi protokolü yeniden açar.*

## Soru ve yanıt kaydı

Sorular özgün ifadeleriyle, yanıtlar düzenlenmiş içerikleri ve kısa kayıt özetleriyle korunur.

### İlk soru ve yanıt

**Konu:** Katmanlı Sistem Modellemesi, Arayüz Tasarımı ve İşleyiş Mimarisi

> Geçmiş bağlamları buraya taşıma. Burası ile sınırlı kalma.

> Nedir? Onu o yapan nelerdir? Neler değildir?

> Nerededir? Bu yeri, oraya has bir yer yapan nelerdir? Neler değildir?

> Nasıl işler yapar? Bu yaptıklarını, ona has yapan nelerdir? Neler değildir?

> Hangi andadır? Bu anı, diğer zamanlardan farklı yapan nelerdir? Neler değildir?

> Hangi nihai amaca hizmet eder? Bu nihai amaca ulaştıran nelerdir? Neler değildir?

Yanıtın ana karşılığı, bu soruları her katmanda yeniden sorulabilen beş inceleme ekseni olarak ele almaktı. Kurucu, ayırt edici, durumsal ve sunuma ilişkin özellikler ayrıldı. Neler değildir sorusu tanım, sorumluluk, koşul ve tasarım ilkesi bakımından farklı dışlamalara açıldı; bilinmeyen durumun olumsuz sonuç olmadığı belirtildi. Sistem modeli, arayüz ve işleyiş mimarisi farklı sorumluluklar olarak açıklandı. Kütüphane ayırtma örneği üzerinden yer, durum, işlem ve kullanıcı açısından sonuç arasındaki farklar gösterildi. Kimin açısından ve neye dayanarak soruları bütün eksenlere eşlik etti.

### İkinci soru ve yanıt

**Konu:** Arayüz Çizimleri, İşletim Sistemi Mimarisi ve Çekirdek Katmanların Modellemesi

> Geçmiş bağlamları buraya taşıma. Burası ile sınırlı kalma.

> Nedir? Onu o yapan nelerdir? Neler değildir?

> Nerededir? Bu yeri, oraya has bir yer yapan nelerdir? Neler değildir?

> Nasıl işler yapar? Bu yaptıklarını, ona has yapan nelerdir? Neler değildir?

> Hangi andadır? Bu anı, diğer zamanlardan farklı yapan nelerdir? Neler değildir?

> Hangi nihai amaca hizmet eder? Bu nihai amaca ulaştıran nelerdir? Neler değildir?

Yanıt, arayüz çizimini bilgi, eylem ve durum temsili; işletim sistemi mimarisini çalışma ortamının sorumluluk düzeni; çekirdek modelini temel yürütme ve koruma mekanizmalarının açıklaması olarak ayırdı. Görsel konum, mimari yer, süreç ve adres alanı, işlemci ayrıcalığı ayrı tutuldu. Bileşen yerleşiminin işletim sistemine göre değiştiği belirtildi. Belge kaydetme örneğinde kullanıcı eylemi, uygulama işlemi, sistem hizmeti ve başarı bildirimi ilişkilendirildi. Eski sürümün kaydının tamamlanmasının güncel içeriğin kaydedildiği anlamına gelmediği; yazma, tamamlanma ve kalıcılığın ayrı eşikler olduğu açıklandı.

### Üçüncü soru ve yanıt

**Konu:** Modellemenin kökeni ve onu taşıyan makinenin kimliği

> Arayüz Çizimleri, İşletim Sistemi Mimarisi ve Çekirdek Katmanların Modellemesi'nin köken aldığı varlık, mekan, usül, zaman, ve gayeyi taşıyan makine kimdir? Kim değildir?

Yanıt, bu makineyi bağlam içinde model kuran, model üzerinden eylemi düzenleyen ve sonuçları gaye bakımından değerlendiren sistem olarak yorumladı; model kuran fail ifadesini işlevsel adlandırma olarak önerdi. Taşıyıcı, üretici, eyleyen taraf, gayeyi belirleyen taraf ve düzeltme sorumluluğu ayrıldı. Model kuran sistem ile modelin anlattığı sistemin aynı olmak zorunda olmadığı belirtildi. Fiziksel altyapı, insan, yazılım, yapay zekâ ve birlikte çalışan düzenler farklı inceleme ölçekleri olarak ele alındı. Konuşmadaki yapay zekâ asistanının açıklama üretmesi, anlattığı işletim sisteminin kendi çalışma mimarisi olduğu anlamında kullanılmadı.

### Dördüncü istek ve karşılığı

> Bu soruları ve yanıtları kayıt altına alarak belgele. Önce mevcut soru-yanıtlarla 1-5 arası protokol bölümlerini paragraf-ağırlıklı oluştur. Sonrasında 0 ve 6'ncı bölüm başlıklarından ne anladığını buraya aktar.

İstenen bölüm dizisi: 0 Tohum (Başlangıç); 1 Varlık Protokolü; 2 Mekan Protokolü; 3 Usül Protokolü; 4 Zaman Protokolü; 5 Gaye Protokolü; 6 Kökleşme (Bitiş).

1–5, paragraf ağırlıklı bir belgeye dönüştürüldü. Tohum; başlangıç sorusu, ihtiyaç, bilgi durumu ve yönelim olarak yorumlandı. Kökleşme; beş protokolün birlikte tutarlılık kazanması, kullanım ve devamlılık koşullarının açıklanması, mevcut inceleme turunun dayanaklarıyla kapanması olarak yorumlandı.

### Beşinci istek ve karşılığı

> 0'ı Tohum (Başlangıç) protokolü, 6'yı Kökleşme (Bitiş) protokolüne dönüştür.
>
> Belgenin son halini oluştur ve masaüstünde gerçekleştirmeye uygun protokollere `.md` formatında indirmeye hazır hale getir.

0 ve 6 için protokol metni, girdiler, masaüstünde uygulama adımları, üretilecek kayıt, tamamlanma ve geri dönüş koşulları oluşturuldu. Aynı uygulama düzeni 1–5'e eklendi. Protokoller, uygulama adımları ve boş çalışma kaydı şablonu bu belgede birlikte yer alır.

## Kaynaklar

Numaralı göndermeler, ilgili teknik veya kavramsal açıklamanın dayanağıdır. Platforma özgü örnekler kendi kapsamları içinde kullanılır. Masaüstü uygulama adımları bu çalışma için düzenlenmiştir.

1. NASA Systems Engineering Handbook 2 Fundamentals of Systems Engineering (https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/)

2. ISO IEC IEEE 42010 2022 Architecture description (https://www.iso.org/standard/74393.html)

3. Microsoft Learn User mode and kernel mode (https://learn.microsoft.com/en-us/windows-hardware/drivers/gettingstarted/user-mode-and-kernel-mode)

4. Linux Kernel Documentation Overview of the Linux Virtual File System (https://docs.kernel.org/filesystems/vfs.html)

5. QNX OS Microkernel (https://www.qnx.com/developers/docs/8.0/com.qnx.doc.neutrino.sys_arch/topic/kernel.html)

6. Linux man pages capabilities 7 (https://www.man7.org/linux/man-pages/man7/capabilities.7.html)

7. Don Norman Signifiers not affordances (https://jnd.org/signifiers-not-affordances/)

8. Linux man pages syscalls 2 (https://www.man7.org/linux/man-pages/man2/syscalls.2.html)

9. QNX Thread scheduling (https://www.qnx.com/developers/docs/8.0/com.qnx.doc.neutrino.sys_arch/topic/kernel_SCHEDULING.html)

10. Linux man pages write 2 (https://www.man7.org/linux/man-pages/man2/write.2.html)

11. Linux man pages fsync 2 (https://www.man7.org/linux/man-pages/man2/fsync.2.html)

12. Herbert A Simon The Science of Design Creating the Artificial (https://academics.design.ncsu.edu/student-publication/wp-content/uploads/2016/11/Simon_H_ScienceofArtificial.pdf)

13. NASA Systems Engineering Handbook 5 4 Product Validation (https://www.nasa.gov/reference/5-4-product-validation/)

## Ek: Çalışma Kaydı Şablonu

Aşağıdaki kod bloğunun içeriğini yeni bir `.md` dosyasına kopyalayarak bağımsız çalışma kaydı oluşturabilirsin.

```markdown
# Çalışma Kaydı Şablonu

**Dayandığı protokol sürümü:** 1.0

Bu dosyayı yeni bir adla kopyalayarak doldur. Köşeli parantezli alanlar boş yer tutuculardır. Bir alan ilgili değilse gerekçesini yaz; bilinmiyorsa bilinmiyor olarak kaydet. Gerçekleşmemiş bir işlemi veya doğrulanmamış bir sonucu tamamlanmış gibi işaretleme.

## Çalışma bilgileri

**Çalışma adı ve kimliği:** [Doldurulacak]

**Hazırlayan ve kayıt sorumlusu:** [Doldurulacak]

**Tarih, saat ve saat dilimi:** [Doldurulacak]

**Çalışma kaydı sürümü:** [Doldurulacak]

**İnceleme birimi ve kapsam:** [Doldurulacak]

**Uygulama düzeyi: metin incelemesi, masaüstü senaryosu, prototip veya gerçek kullanım:** [Doldurulacak]

**Genel durum:** [Doldurulacak]

Bölüm durumları için Başlanmadı, Çalışılıyor, Engelli, İnceleme için tamamlandı veya Yeniden açıldı ifadelerinden uygun olanı kullan. İnceleme için tamamlandı durumu, uygulamada başarı kanıtı yerine geçmez.

## 0 Tohum (Başlangıç) Protokolü

> Bu çalışmayı başlatan şey nedir; hangi ihtiyaç, soru, varsayım ve yönelimle başlıyoruz?

**Bölüm durumu ve gerekçesi:** [Doldurulacak]

**Özgün başlangıç sorusu:** [Doldurulacak]

**Soruyu doğuran ihtiyaç ve beklenen yarar:** [Doldurulacak]

**Sonucu kullanacak ve etkilenecek taraflar:** [Doldurulacak]

**Başlangıç kapsamı, dışarıda kalanlar ve dış bağımlılıklar:** [Doldurulacak]

**Soruyu soran, modeli kuran, kaydı tutan ve gayeyi belirleyen taraflar:** [Doldurulacak]

**Varlık, mekân, usul, zaman ve gaye için ilk karşılıklar:** [Doldurulacak]

**Seçilen örnek durum, başlatan taraf ve beklenen sonuç:** [Doldurulacak]

**Başlangıç kaynakları ve ilgili açık sorular:** [Doldurulacak]

**Tamamlanma koşulunun karşılığı:** [Doldurulacak]

**İlgili dayanak ve açık soru kimlikleri:** [Doldurulacak]

## 1 Varlık Protokolü

> Nedir? Onu o yapan nelerdir? Neler değildir?

**Bölüm durumu ve gerekçesi:** [Doldurulacak]

**İnceleme birimi, ölçeği ve tanımı:** [Doldurulacak]

**Tür, tekil kimlik, rol ve mevcut durum:** [Doldurulacak]

**Kurucu, ayırt edici, durumsal ve sunuma ilişkin özellikler:** [Doldurulacak]

**Öğeler, ilişkiler ve kimliğin süreklilik koşulları:** [Doldurulacak]

**Model, modellenen sistem ve model kuran taraf arasındaki ilişki:** [Doldurulacak]

**Taşıyıcı, üretici, kullanan veya eyleyen, gayeyi belirleyen ve düzeltmeden sorumlu taraflar:** [Doldurulacak]

**Neler değildir ve her sınırın gerekçesi:** [Doldurulacak]

**Dayanaklar ve açık kimlik soruları:** [Doldurulacak]

**Tamamlanma koşulunun karşılığı:** [Doldurulacak]

**İlgili dayanak ve açık soru kimlikleri:** [Doldurulacak]

## 2 Mekan Protokolü

> Nerededir? Bu yeri, oraya has bir yer yapan nelerdir? Neler değildir?

**Bölüm durumu ve gerekçesi:** [Doldurulacak]

**Fiziksel, mantıksal, kurumsal ve ilişkisel yer:** [Doldurulacak]

**İncelenen yerin ölçeği ve sistem sınırı:** [Doldurulacak]

**Kaynaklar, komşuluklar ve dış bağımlılıklar:** [Doldurulacak]

**Erişim, etkileme, bilgi edinme ve karar verme alanları:** [Doldurulacak]

**Sorumluluk devri ve sınır geçişleri:** [Doldurulacak]

**Çizimlerde kutu, ok ve konumların anlamı:** [Doldurulacak]

**Bağlam değiştiğinde değişen davranışlar:** [Doldurulacak]

**Neler değildir, dayanaklar ve açık mekân soruları:** [Doldurulacak]

**Tamamlanma koşulunun karşılığı:** [Doldurulacak]

**İlgili dayanak ve açık soru kimlikleri:** [Doldurulacak]

## 3 Usül Protokolü

> Nasıl işler yapar? Bu yaptıklarını, ona has yapan nelerdir? Neler değildir?

**Bölüm durumu ve gerekçesi:** [Doldurulacak]

**Seçilen işlem, başlatan taraf, işlem nesnesi ve niyet:** [Doldurulacak]

**Önkoşullar, gerekli bilgi ve yetki:** [Doldurulacak]

**İşlem adımları, sorumlular, kaynaklar ve durum değişiklikleri:** [Doldurulacak]

**Sorumluluk devirleri ve aktarılan bilgi:** [Doldurulacak]

**Başarı koşulu ve kullanıcıya bildirilen sonuç:** [Doldurulacak]

**İlgili hata, bekleme, yeniden deneme, iptal ve geri alma anlamları:** [Doldurulacak]

**Arayüzde eylem öncesi, işlem sırası ve sonuç sonrası görünür bilgi:** [Doldurulacak]

**Neler değildir, dayanaklar ve açık usul soruları:** [Doldurulacak]

**Tamamlanma koşulunun karşılığı:** [Doldurulacak]

**İlgili dayanak ve açık soru kimlikleri:** [Doldurulacak]

## 4 Zaman Protokolü

> Hangi andadır? Bu anı, diğer zamanlardan farklı yapan nelerdir? Neler değildir?

**Bölüm durumu ve gerekçesi:** [Doldurulacak]

**Durumlar, geçiş olayları ve önkoşullar:** [Doldurulacak]

**Olayın gerçekleşme, öğrenilme ve davranışa yansıma zamanı:** [Doldurulacak]

**Başlama, kabul, yürütme, tamamlanma, kalıcılık ve bildirim eşiklerinden ilgili olanlar:** [Doldurulacak]

**İçerik ve kural sürümleri ile işlem sırası:** [Doldurulacak]

**Eşzamanlılık ve geç gelen sonuçların ele alınması:** [Doldurulacak]

**Geçerlilik, süre, sona erme ve yaşam evresi koşulları:** [Doldurulacak]

**Bilgi güncelliği ve yeniden açılma koşulları:** [Doldurulacak]

**Neler değildir, dayanaklar ve açık zaman soruları:** [Doldurulacak]

**Tamamlanma koşulunun karşılığı:** [Doldurulacak]

**İlgili dayanak ve açık soru kimlikleri:** [Doldurulacak]

## 5 Gaye Protokolü

> Hangi nihai amaca hizmet eder? Bu nihai amaca ulaştıran nelerdir? Neler değildir?

**Bölüm durumu ve gerekçesi:** [Doldurulacak]

**Seçilen inceleme düzeyindeki üst amaç:** [Doldurulacak]

**Yararlanıcılar ve etkilenen taraflar:** [Doldurulacak]

**Amacı belirleme ve değiştirme yetkisi:** [Doldurulacak]

**Faaliyet, çıktı, kullanıcı açısından sonuç ve değer ayrımı:** [Doldurulacak]

**Araçlar, tasarım kararları ve beklenen etki gerekçeleri:** [Doldurulacak]

**Başarı koşulları, göstergeler ve bunların geçerlilik sınırı:** [Doldurulacak]

**Amaçlar arasındaki çatışmalar ve karar gerekçeleri:** [Doldurulacak]

**Beklenen sonuç, gözlenen sonuç ve karşı örnek:** [Doldurulacak]

**Neler değildir, dayanaklar ve açık gaye soruları:** [Doldurulacak]

**Tamamlanma koşulunun karşılığı:** [Doldurulacak]

**İlgili dayanak ve açık soru kimlikleri:** [Doldurulacak]

## 6 Kökleşme (Bitiş) Protokolü

> Açıklığa kavuşan bu düzen, hangi dayanaklarla kullanılabilir, sürdürülebilir ve gerektiğinde yeniden ele alınabilir hâle geldi?

**Bölüm durumu ve gerekçesi:** [Doldurulacak]

**Başlangıç sorusuna verilen karşılık ve yönelimdeki değişiklikler:** [Doldurulacak]

**0–5 arasındaki tutarlılık ve bulunan çelişkiler:** [Doldurulacak]

**Örnek durumun masaüstü incelemesi ve ilgili istisna:** [Doldurulacak]

**Beklenen sonuç, masaüstü incelemesinin sonucu ve varsa uygulama bulgusu:** [Doldurulacak]

**Değerlendirme düzeyi ve her önemli sonucu destekleyen dayanak:** [Doldurulacak]

**Geçerli bağlam ve kullanım sınırları:** [Doldurulacak]

**Açık konuların etkisi, sorumlusu biliniyorsa ve yeniden ele alınma koşulu:** [Doldurulacak]

**Esas kayıt sürümü, güncelleme sorumluluğu ve devam edecek iş:** [Doldurulacak]

**Kapanış veya açık kalma kararı ve gerekçesi:** [Doldurulacak]

**Yeniden açılma nedenleri ve ilgili protokoller:** [Doldurulacak]

**Tamamlanma koşulunun karşılığı:** [Doldurulacak]

**İlgili dayanak ve açık soru kimlikleri:** [Doldurulacak]

## Dayanaklar

Her önemli ifade için dayanak kimliğini kullan. İfade türünü tanım, gözlem, varsayım, çıkarım veya karar olarak belirt. Kaynağın bulunması ile kaynağın ilgili ifadeyi desteklemesi ayrı değerlendirilir.

| Kimlik | İlgili ifade ve bölüm | İfade türü | Kaynak veya dosya bağlantısı | Tarih veya sürüm | Desteklediği kapsam ve sınır |
| --- | --- | --- | --- | --- | --- |
| [Doldurulacak] | [Doldurulacak] | [Doldurulacak] | [Doldurulacak] | [Doldurulacak] | [Doldurulacak] |

## Açık sorular

| Kimlik | Soru ve ilgili bölüm | Neden açık | Etkisi | Sorumlu biliniyorsa | Yeniden ele alma koşulu |
| --- | --- | --- | --- | --- | --- |
| [Doldurulacak] | [Doldurulacak] | [Doldurulacak] | [Doldurulacak] | [Doldurulacak] | [Doldurulacak] |

## Değişiklikler

| Tarih | Önceki ve yeni sürüm | Önceki ve yeni ifade | Gerekçe ve dayanak | Etkilenen protokoller | Yapan |
| --- | --- | --- | --- | --- | --- |
| [Doldurulacak] | [Doldurulacak] | [Doldurulacak] | [Doldurulacak] | [Doldurulacak] | [Doldurulacak] |
```

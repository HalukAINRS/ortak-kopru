# Yaratıcı Yeniden İşlevlendirme Mühendisliği

**Tohumdan Kökleşmeye masaüstü uygulama protokolleri**

**Sürüm:** 1.0\
**Tarih:** 31 Ekim 2026\
**Kapsam:** 0 Tohum, 1 Varlık, 2 Mekan, 3 Usül, 4 Zaman, 5 Gaye ve 6 Kökleşme.

Bu protokoller, mevcut bir varlığın taşıdığı yapı, bilgi ve yetenekleri alışılmış rolünün ötesinde bir ihtiyaçla buluşturmak için kullanılır. Yeni rolün düşünülmesi, denenmesi, değerlendirilmesi ve devredilmesi aynı çalışmanın parçalarıdır. Varlık; bir dosya, yazılım, bilgi birikimi veya iş akışı olabileceği gibi fiziksel bir nesne, yapı ya da sistem de olabilir.

Bu belge, konuşmada geliştirilen kavramsal çerçeveyi **Hacker İlkeleri — Tohumdan Kökleşmeye** [H] belgesindeki ilkelerle birleştirir. Hacker yaklaşımından merak, yetkinlik, yaratıcılık, açık öğrenme ve kontrollü deneme alınır; yeniden işlevlendirme yaklaşımından kapasite ile ihtiyaç arasındaki ilişki, alternatifleri karşılaştırma ve işlevi sınama korunur. Teknik başarı etik yararı kendiliğinden sağlamadığı için amaç ve etkiler ayrıca değerlendirilir. Buradaki protokoller bir uygulama önerisidir; kişilere kalıcı bir kimlik veya unvan vermez.

## Masaüstünde kullanım

Bu metinde masaüstü uygulama, bilgisayarda yerel bir çalışma klasörü üzerinden gözlem, araştırma, tasarım, deneme ve belgeleme yapmaktır. Başlamak için dosya yöneticisi, bir metin düzenleyici ve üzerinde çalışılan varlığı açan mevcut uygulama yeterlidir. Kod yazmak veya yeni yazılım kurmak zorunlu değildir. Fiziksel bir varlığın dayanımı veya gerçek kullanım koşulları masaüstünde gösterilemiyorsa bunlar tamamlanmış gibi kaydedilmez; bekleyen sınamalar olarak belirtilir.

Bu dosyayı rehber olarak sakla. Çalışma klasöründe `calisma.md` adlı ayrı bir kayıt aç ve aşağıdaki şablonu ona kopyala. Kaynakların asılları üzerinde deneme yapmak yerine çalışma kopyaları kullan. Dosya adları öneridir; aynı ayrımı mevcut düzeninde de kurabilirsin.

| Dosya veya klasör | İşlev |
|---|---|
| Bu protokol dosyası | Yöntem ve başvuru metni |
| `calisma.md` | Sorular, bulgular, kararlar ve protokol durumları |
| `kaynaklar/` | Değiştirilmeden saklanan kaynak kopyaları ve kaynak bilgileri |
| `denemeler/` | Deneme kopyaları, karşılaştırmalar ve gözlem kayıtları |
| `ciktilar/` | Seçilmiş sonuç, kullanım bilgisi ve paylaşılabilir kopya |
| `devir.md` | Kullanım, bakım, sınırlılıklar ve yeniden açma koşulları |

~~~text
  <calisma-klasoru>/
    <bu protokol dosyasi>    rehber: yontem ve basvuru metni
    calisma.md               sorular, bulgular, kararlar,
                             protokol durumlari

    kaynaklar/               degistirilmeden saklanan kaynak kopyalari
        |  calisma kopyasi
        v
    denemeler/               deneme kopyalari, karsilastirmalar,
        |  secilen sonuc     gozlem kayitlari
        v
    ciktilar/                secilmis sonuc, kullanim bilgisi,
        |                    paylasilabilir kopya
        v
    devir.md                 kullanim, bakim, sinirliliklar,
                             yeniden acma kosullari

  asillar uzerinde deneme yapilmaz; calisma kopyalari kullanilir
  dosya adlari oneridir

  BOLUM DURUMLARI
    acik | deneniyor | tamamlandi | bekliyor | vazgecildi

    "tamamlandi"nin yanina kanitin dosyasi ya da kayit yeri yazilir
    kutularin isaretlenmesi, gozlem ve gerekcenin yerini tutmaz

  masaustunde gosterilemeyen (fiziksel dayanim, gercek kullanim)
  tamamlanmis gibi kaydedilmez; bekleyen sinama olarak belirtilir
~~~

*Çizim 1 — Çalışma klasörü: kaynaktan denemeye, denemeden çıktıya ve devre; beş bölüm durumu.*

Numaralar katı bir üretim sırası değildir. **0** çalışmayı açar; **1–5** birbirini düzelten değerlendirme boyutlarıdır; **6** mevcut döngüyü gerekçeli biçimde kapatır. İlk amaç 0'da yazılır, ilk kapsam 2'de kurulur. 3'te tasarlanan bir değişikliği uygulamadan önce 4'te zamanlama, 5'te amaç ve beklenen etkiler değerlendirilir. Deneme sonucuna dayanan maddeler denemeden sonra doldurulur; 4 ve 5'in baştan bütünüyle tamamlanması beklenmez. Ardından deneme için 3'e dönülür. Yeni bulgular, önceki kararların değiştirilmesini gerektirebilir.

~~~text
   0 Tohum      calismayi acar; ilk amac burada yazilir
      |
      v
   1 Varlik . 2 Mekan      ilk kapsam 2'de kurulur
      |
      v
   3 Usul       bir degisiklik TASARLANIR
      |
      v
   4 Zaman      zamanlama degerlendirilir          }  uygulamadan
      |                                            }  once
      v                                            }
   5 Gaye       amac ve beklenen etkiler           }
      |
      v
   3 Usul       deneme YAPILIR
      |             |
      |             `--> deneme sonucuna dayanan maddeler (4 ve 5'te)
      v                  denemeden sonra doldurulur
   6 Koklesme   mevcut donguyu gerekceli bicimde kapatir
      |
      v
   yeni bir 0 acilabilir

   1-5 birbirini duzelten degerlendirme boyutlaridir;
   numaralar kati bir uretim sirasi degildir.
   yeni bulgular, onceki kararlarin degistirilmesini gerektirebilir.
~~~

*Çizim 2 — Çalışma sırası: değişiklik 3'te tasarlanır, 4 ve 5'te değerlendirilir, sonra 3'te denenir.*

Her bölümün durumunu `açık`, `deneniyor`, `tamamlandı`, `bekliyor` veya `vazgeçildi` olarak kaydet. “Tamamlandı” ifadesinin yanına kanıtın dosyasını veya kayıt yerini yaz. Kutuların işaretlenmesi, gözlem ve gerekçenin yerini tutmaz. Öğrenme amacıyla yapılan bir deneme, kullanılabilir bir çözüm üretmese de tamamlanabilir; bu durum kullanıma hazır bir ürünle karıştırılmaz.

## Taşıyıcı kimdir ve kim değildir

Bu pratiğin öznesi, kendi koşullarını anlayabilen, amaçlarını sorgulayabilen ve kararlarının hesabını üstlenen insan veya insan topluluğudur. İşleyişi ise insanlar, araçlar, bilgiler, kurumlar ve çevreleri birlikte taşır. “Makine” sözcüğü bu işleyiş için kullanılan bir benzetmedir. İnsan dönüştürdüğü dünyanın dışında durmaz; bedenini, kırılganlıklarını, deneyimini, dilini ve devraldığı emeği çalışmaya getirir. Kendisi de süreçte öğrenir ve değişir.

Yazılım, otomasyon veya yapay zekâ bu düzeneğin bir bileşeni olarak kullanılabilir. Araç önerisi, gözlenen kanıt ve insanın aldığı karar ayrı kaydedilir. Bir hedef doğrultusunda işlem üretmek, o hedefin uygunluğunu değerlendirmekle aynı değildir. Ekip çalışmasında amacı belirleyen, değişikliği yapan ve bakım sorumluluğunu üstlenen kişiler açık olmalıdır.

Taşıyıcı; koşulsuz bir yaratıcı, yalıtılmış bir dâhi, yalnızca emir uygulayan bir yürütücü veya başkalarının amaçlarına göre kullanılacak hammadde değildir. Yaş, diploma, meslek veya ün tek başına yeterlilik göstermez. Merak, yetkinlik, açıklık, yöntem ve amaç, o çalışmadaki davranış ve kayıtlarla birlikte değerlendirilir. [H]

~~~text
  IKI DUZEY

    OZNE      kendi kosullarini anlayabilen, amaclarini
              sorgulayabilen ve kararlarinin hesabini ustlenen
              insan ya da insan toplulugu

    ISLEYIS   insanlar . araclar . bilgiler . kurumlar . cevreleri
              birlikte tasir
              ("makine" sozcugu bu isleyis icin bir benzetmedir)

  insan, donusturdugu dunyanin disinda durmaz; calismaya getirdikleri:
    bedeni . kirilganliklari . deneyimi . dili . devraldigi emek
    kendisi de surecte ogrenir ve degisir

  YAZILIM, OTOMASYON YA DA YAPAY ZEKA  duzenegin bir bileseni
    ayri kaydedilir:
      arac onerisi | gozlenen kanit | insanin aldigi karar

    bir hedef dogrultusunda      =/=    o hedefin uygunlugunu
    islem uretmek                       degerlendirmek

  TASIYICI SUNLAR DEGILDIR
    kosulsuz bir yaratici . yalitilmis bir dahi .
    yalnizca emir uygulayan bir yurutucu .
    baskalarinin amaclarina gore kullanilacak hammadde

  tek basina yeterlilik gostermez:  yas . diploma . meslek . un
~~~

*Çizim 3 — Taşıyıcı: özne ve işleyiş; araç önerisi, kanıt ve karar ayrı kaydedilir.*

## 0 Tohum (Başlangıç) Protokolü

**Sorusu:** Bu çalışma hangi sorudan doğuyor? Hazır açıklamada ne eksik? İlk eylem ne olacak?

Tohum, mevcut olanın başka türlü olabileceğinin fark edilmesi ve bu farkın ilk araştırma eylemine dönüşmesidir. Kaynaktaki doğuş ilkesi, sorunun yalnız merak olarak kalmayıp gözleme, incelemeye veya denemeye geçmesini vurgular. Başlangıç, çözümü önceden kesinleştirmeyi gerektirmez. Merak zorla üretilemez; soru sormaya, hata yapmaya ve küçük denemelere elveren koşullar hazırlanabilir. [H]

Bir görevden başlanmış olsa bile araştırılacak soru kişinin veya ekibin kendi gözlemiyle kurulmalıdır. İlk niyetin iyi olması da sonucu baştan haklı çıkarmaz. Tohum, sonraki beş protokolün araştıracağı varlık, ortam, yöntem, zaman ve amaç için ilk kaydı açar.

~~~text
   mevcut olan          FARK EDILIR               ILK KUCUK EYLEM
  .------------.
  |            |  -->  "Neden boyle?"       -->  bir kaynak bolumunu
  |            |       "Baska nasil              incele
  `------------'        olabilir?"               iki durumu
                                                 karsilastir
                                                 mevcut isleyisi
                                                 degistirmeden gozle
                                                        |
         gozlem soruyu nasil degistirdi?  <-------------'
                     |
                     v
         devam et | beklet | vazgec

   soru yalniz merak olarak kalmaz;
   gozleme, incelemeye ya da denemeye gecer

  AYRI CUMLELERLE
    bildigin | varsaydigin | henuz bilmedigin
    cozum onerisi, gozlenmis gercek gibi yazilmaz

  ILK NIYET
    ogrenmek | bir ihtiyaci karsilamak | ikisi birlikte
    ilk niyetin iyi olmasi, sonucu bastan hakli cikarmaz

  TAMAMLANMA  acik bir soru + gerceklesmis ilk arastirma eylemi
    yetmez:  proje adi . arac secimi . unvan . heves beyani
~~~

*Çizim 4 — Tohum: fark edilen şey bir soruya, soru ilk küçük eyleme dönüşür.*

### Uygulama

1. “Neden böyle?” veya “Başka nasıl olabilir?” biçiminde tek bir başlangıç sorusu yaz. Soruyu doğuran somut durumu belirt.
2. Bildiğin şeyi, varsaydığın şeyi ve henüz bilmediğin şeyi ayrı cümlelerle kaydet. Çözüm önerisini gözlenmiş gerçek gibi yazma.
3. İlk niyeti belirt: öğrenmek, bir ihtiyacı karşılamak veya ikisi birlikte. Kimin ihtiyacından hareket ettiğini yaz; henüz belli değilse bunu açık bırak.
4. İlk küçük eylemi yap: bir kaynak bölümünü incele, iki durumu karşılaştır veya mevcut işleyişi değiştirmeden gözle. Başlangıç gözlemini dosya, ekran görüntüsü ya da kısa notla kaydet.
5. Gözlemin soruyu nasıl değiştirdiğini yaz ve araştırmaya devam etme, bekletme veya vazgeçme kararını belirt.

**Kayıt:** Başlangıç sorusu, gözlenen durum, ilk niyet, bilinenler, varsayımlar, bilinmeyenler ve ilk eylemin kanıtı.

**Tamamlanma koşulu:** Açık bir soru ve gerçekleşmiş ilk araştırma eylemi vardır. Yalnızca bir proje adı, araç seçimi, unvan veya heves beyanı bu koşulu karşılamaz.

## 1 Varlık Protokolü

**Sorusu:** Nedir? Onu o yapan nelerdir? Neler değildir?

Yeniden işlevlendirme, var olanın kapasitesiyle farklı bir ihtiyaç arasında yeni bir ilişki kurar. Bir şeyin ilk yapılma amacı gelecekteki bütün rollerini belirlemez. Yeni rol, fiziksel biçim değişmeden de kurulabilir. Fakat mevcut varlıktan anlamlı bir yapı, bilgi veya yetenek devralınmalıdır; eskiyi bütünüyle kaldırıp yerine yenisini koymak tek başına yeniden işlevlendirme sayılmaz.

Hacker ilkesindeki merak anlamayı başlatır, yetkinlik iddiaları sınar, yaratıcılık farklı rol adaylarını görünür kılar. Araç kullanabilmek ile aracın yaptığı işi açıklayabilmek ayrılır. Öğrenen kişinin her şeyi baştan bilmesi beklenmez; bilmediğini belirleyip araştırması gerekir. [H]

~~~text
   MEVCUT VARLIK
  .----------------.      mevcut rol          .--------------------.
  | yapi           |------------------------->| alisilmis kullanim |
  | bilgi          |                          `--------------------'
  | yetenek        |      yeni rol adayi      .--------------------.
  |                |- - - - - - - - - - - - ->| farkli bir ihtiyac |
  `----------------'      (yeni iliski)       `--------------------'

   devralinan:  anlamli bir yapi, bilgi ya da yetenek
   degisen:     rol (fiziksel bicim degismeden de kurulabilir)

   bir seyin ilk yapilma amaci, gelecekteki butun rollerini belirlemez

  TEK BASINA YETERLI DEGILDIR
    eskiyi butunuyle kaldirip yerine yenisini koymak
    yeni ad vermek . gorunusu degistirmek .
    bir hazir araci anlamadan calistirmak

  UC HACKER ILKESI, UC IS
    merak          anlamayi baslatir
    yetkinlik      iddialari sinar
    yaraticilik    farkli rol adaylarini gorunur kilar

    arac kullanabilmek   =/=   aracin yaptigi isi aciklayabilmek

  HER IDDIA ISARETLENIR
    gozlem | kaynak bilgisi | varsayim

  ROL ADAYLARI
    en az bir farkli aday . mumkunse ikinci bir aday .
    mevcut rolu surdurmek de bir secenektir
~~~

*Çizim 5 — Varlık: mevcut varlığın kapasitesi ile farklı bir ihtiyaç arasında yeni ilişki.*

### Uygulama

1. Üzerinde çalışılan varlığı tanımla: adı, mevcut rolü, bileşenleri, durumu ve kaynak dosyasının yeri. İlgili önceki emeği ve bilgiyi belirt.
2. Kapasiteleri ve sınırları yaz. Her iddiayı `gözlem`, `kaynak bilgisi` veya `varsayım` olarak işaretle; ilgili kanıtı iliştir.
3. En az bir farklı rol adayı üret. Mümkünse ikinci bir adayla karşılaştır; mevcut rolü sürdürmeyi de seçenek olarak tut.
4. Her adayda neyin devralındığını ve neyin değişeceğini açıkla. Adayın karşılayacağı ihtiyaç ile varlığın kapasitesi arasındaki bağı yaz.
5. İhtiyaç duyulan bilgiyi, mevcut becerileri ve eksik yetkinlikleri belirt. Kimlerin katkısına ihtiyaç olduğunu kaydet.

**Kayıt:** Varlık tanımı, mevcut rol, devralınan kapasite, sınırlar, kanıtlar, rol adayları ve öğrenilmesi gerekenler.

**Tamamlanma koşulu:** Seçilen rol adayı, mevcut varlığın açıklanabilir bir kapasitesine dayanır; bilinmeyenler görünürdür. Yeni ad vermek, görünüşü değiştirmek veya bir hazır aracı anlamadan çalıştırmak yeterli değildir. Onarım ve geri dönüşüm süreçle kesişebilir; bunlar birbirini dışlayan kutular değildir.

## 2 Mekan Protokolü

**Sorusu:** Nerededir? Bu yeri, oraya has bir yer yapan nelerdir? Neler değildir?

Mekân, varlıkla ihtiyacın buluştuğu ilişkiler bütünüdür. Fiziksel konum kadar kullanıcılar, erişim, yerel bilgi, karar hakları ve bakım imkânları da mekânı kurar. Kaynağın vurguladığı sınır, beklenen işleyişle gerçek işleyiş arasındaki farktır. Bu farkı görebilmek için erişilebilir araçlar, soru sorma ve hata yapma imkânı, paylaşım ve yapılan işe dayalı saygı gerekir. [H]

Masaüstünde bunun karşılığı, kaynaklarla denemelerin ayrıldığı, yapılanın izlenebildiği ve katkı sunanların söz sahibi olduğu bir çalışma alanıdır. Açık öğrenme, başkalarının verisini veya sistemini sınırsızca değiştirme yetkisi vermez. Kullanılmayan bir varlık da kendiliğinden sahipsiz değildir.

~~~text
  MEKAN  varlikla ihtiyacin bulustugu iliskiler butunu

                     kullanicilar        erisim
                            \             /
     fiziksel konum ---- [ varlik <--> ihtiyac ] ---- yerel bilgi
                            /             \
                   karar haklari      bakim imkanlari

  KAYNAGIN VURGULADIGI SINIR

     beklenen isleyis   |<-------- fark -------->|   gercek isleyis

     hangi fark yeni islev icin imkan, hangisi sinir?

     bu farki gorebilmek icin gerekenler:
       erisilebilir araclar . soru sorma ve hata yapma imkani .
       paylasim . yapilan ise dayali saygi

  MASAUSTUNDEKI KARSILIGI
     kaynaklarla denemelerin ayrildigi, yapilanin izlenebildigi,
     katki sunanlarin soz sahibi oldugu bir calisma alani

     masaustu denemesi   =/=   gercek kullanim ortami

  YETKI VERMEZ, SAHIPSIZ KILMAZ
     acik ogrenme           -x->  baskalarinin verisini ya da sistemini
                                  sinirsizca degistirme yetkisi
     kullanilmayan varlik   -x->  sahipsiz

  MEKANI TEK BASINA KURMAZ
     pahali ekipman . kapali bir oda . yalnizca bir klasor adi
~~~

*Çizim 6 — Mekan: varlıkla ihtiyacın buluştuğu ilişkiler bütünü; beklenen ile gerçek işleyişin farkı.*

### Uygulama

1. Çalışma klasörünü kur; kaynak kopyalarını `kaynaklar/`, değiştirilecek kopyaları `denemeler/` altında ayır. İlk durumu geri bulunabilir biçimde sakla.
2. Uygulamanın bağlamını yaz: kim kullanacak, nerede kullanacak, hangi araç ve koşullara ihtiyaç duyacak? Masaüstü denemesiyle gerçek kullanım ortamının farkını belirt.
3. Değiştirebileceğin dosya, varlık ve işlemleri sınırla. Karar ve erişim yetkilerini; başkalarını etkileyen noktalarda kimin katılımı gerektiğini kaydet.
4. Beklenen işleyiş ile gözlenen işleyiş arasındaki farkı yaz. Hangi farkın yeni işlev için imkân, hangisinin sınır olduğunu belirt.
5. Kişisel veya paylaşımı kısıtlı veriyi paylaşılabilir yöntem ve sonuçlardan ayır. Birlikte çalışılıyorsa katkı verme, soru sorma ve gözden geçirme yolunu belirle.

**Kayıt:** Çalışma alanı, kullanıcılar, kullanım ortamı, erişim ve karar kapsamı, bağlamsal farklar ve paylaşım sınırları.

**Tamamlanma koşulu:** Nerede ve hangi kapsamda deneme yapılabileceği, kimlerin etkilendiği ve kaynağın nasıl korunacağı bellidir. Pahalı ekipman, kapalı bir oda veya yalnızca bir klasör adı bu mekânı tek başına kurmaz.

## 3 Usül Protokolü

**Sorusu:** Nasıl işler yapar? Bu yaptıklarını, ona has yapan nelerdir? Neler değildir?

Usul, anlamakla başlar; varsayımları sorgulama, küçük deney, gözlem, aykırılığı izleme ve belgeleme yoluyla ilerler. Bir başarıyı açıklayamamak, anlayışın henüz eksik kaldığını gösterebilir. Başarısız deneme de hangi varsayımın işlemediğini gösterdiğinde bilgi üretir. Kaynağın zarafet ve az araçla çok iş yapma vurgusu, burada gereksiz karmaşıklığı azaltan ve açıklanabilen çözümler aramak olarak uygulanır. [H]

~~~text
  USUL  anlamakla baslar

   anla --> varsayimi sorgula --> kucuk deney --> gozle
                                                    |
            belgele  <--  aykiriligi izle  <--------'

  BIR DENEME

    DENEMEDEN ONCE         DENEME                 DENEMEDEN SONRA
    hipotez                en kucuk anlamli       beklenen sonuc ile
    beklenen sonuc         deneme                 gerceklesen sonuc
    hangi gozlemle         mumkunse tek           birlikte kaydedilir
    degerlendirilecegi     degisken
    baslangic durumu       calisma kopyasinda
                           geri alma yolu belli

    sonuc aykiriysa:  ilgili kosulda yeniden dene ya da aciklamayi
                      ayirt edecek farkli bir karsilastirma yap

  BILGI URETIR
    basarisiz deneme; hangi varsayimin islemedigini gosterdiginde

  YETERLI DEGILDIR
    tek seferlik calisma . anlasilmadan kopyalama .
    sirf sasirtici olma

  aciklayamadigin basari, kullanima hazir sonuc olarak isaretlenmez
  bir arac ya da yapay zeka onerisi, kendi bulgun gibi sunulmaz
~~~

*Çizim 7 — Usül: usulün adımları ve bir denemenin öncesi, kendisi, sonrası.*

Yaratıcı bir eşleştirme mühendislik iddiası taşıyorsa sınanmalıdır. İki soru ayrı tutulur: “Belirlediğimiz gereksinimleri karşılıyor mu?” ve “Bu gereksinimleri karşılayan sonuç, gerçek ihtiyaca yarıyor mu?” İlk soru doğrulama, ikinci soru geçerleme içindir. Öğrenme veya oyun denemesi değerli olabilir; kullanıma alınacak bir çözümün işlev kanıtının yerine geçmez.

~~~text
  DONUSTURME, ILGILI ALTERNATIFLERLE KARSILASTIRILIR
    mevcut kullanimi surdurme | onarim | paylasim |
    yeni uretim | mudahale etmeme

  IKI AYRI SORU

    belirledigimiz                                     gercek
    gereksinimler               sonuc                  ihtiyac
   .-------------.    1    .-------------.    2    .-------------.
   |             | <------ |             | ------> |             |
   `-------------'         `-------------'         `-------------'

    1  DOGRULAMA   belirledigimiz gereksinimleri karsiliyor mu?
    2  GECERLEME   bu gereksinimleri karsilayan sonuc, gercek
                   ihtiyaca yariyor mu?

    iki sonuc ayri degerlendirilir ve ayri kaydedilir

  ogrenme ya da oyun denemesi degerli olabilir;
  kullanima alinacak bir cozumun islev kanitinin yerine gecmez
~~~

*Çizim 8 — Usül: alternatiflerle karşılaştırma; doğrulama ile geçerleme iki ayrı sorudur.*

### Uygulama

1. Bir varsayımı seç ve sınanabilir bir hipotez yaz. Beklenen sonucu ve onu hangi gözlemle değerlendireceğini denemeden önce belirt.
2. Başlangıç durumunu kaydet. Dönüştürme seçeneğini mevcut kullanımı sürdürme, onarım, paylaşım, yeni üretim veya müdahale etmeme gibi ilgili alternatiflerle karşılaştır.
3. En küçük anlamlı denemeyi tasarla. Mümkün olduğunda tek değişkeni değiştir; birden çok değişiklik gerekiyorsa bunları açıkça kaydet. Geri alma yolunu belirt.
4. 2'deki kapsam ile 4 ve 5'teki koşullar uygunsa çalışma kopyasında deneyi yap. Değişikliği, kullanılan araç ve sürümü, beklenen ve gerçekleşen sonucu kaydet. Bir araç veya yapay zekâ önerisini kendi bulgun gibi sunma.
5. Aykırı sonucu araştır. İlgili koşulda yeniden dene veya açıklamayı ayırt edecek farklı bir karşılaştırma yap. Açıklayamadığın başarıyı kullanıma hazır sonuç olarak işaretleme.
6. Gereksinim sonucunu ve kullanıcı ihtiyacı sonucunu ayrı değerlendir. Uygun bilgi ve sonuçları başkasının izleyebileceği şekilde yaz; paylaşım sınırları içinde aktarılabilir hâle getir.

**Kayıt:** Deneme kimliği, hipotez, başlangıç durumu, değişiklik, araç, gözlem, kanıt, yorum, doğrulama sonucu, geçerleme sonucu ve sonraki adım.

**Tamamlanma koşulu:** Sonuç ile açıklaması arasında izlenebilir bağ vardır; başarısızlık koşulları ve bilinmeyenler belirtilmiştir. Tek seferlik çalışma, anlaşılmadan kopyalama veya sırf şaşırtıcı olma yeterli değildir. Kaynaktaki zarar vermeme ilkesi, denemenin kapsamına ve başkalarının haklarına uygun çalışmayı gerektirir.

## 4 Zaman Protokolü

**Sorusu:** Hangi andadır? Bu anı, diğer zamanlardan farklı yapan nelerdir? Neler değildir?

Uygun an, mevcut rolle mümkün rol arasındaki farkın görünür ve müdahale edilebilir olduğu eşiktir. Kaynak bu eşikte üç boyut ayırır: işleyişi anladığımız kavrayış, müdahaleyi mümkün kılan fırsat penceresi ve yeni kapasiteyle ne yapacağımıza karar verdiğimiz vicdan. Bu boyutlar, ihtiyaç, kullanılabilir kapasite ve sınama imkânıyla birlikte değerlendirilir. [H]

Çalışan bir sistem de yeniden işlevlendirilebilir; eskimesi veya bozulması beklenmek zorunda değildir. Erken müdahale yararlı bir düzeni gereksiz yere bozabilir, geç müdahale kullanılabilir kapasiteyi kaybettirebilir. Yoğun odaklanma kavrayışa alan açabilir; saatlerce çalışmak veya zamanı unutmak tek başına doğru sonucun kanıtı değildir.

~~~text
  UYGUN AN  mevcut rolle mumkun rol arasindaki farkin gorunur VE
            mudahale edilebilir oldugu esik

   zaman  ---------------------------------------------------------->

          erken               |    ESIK    |               gec
     yararli bir duzeni       |            |       kullanilabilir
     gereksiz yere            |            |       kapasiteyi
     bozabilir                |            |       kaybettirebilir

  KAYNAGIN BU ESIKTE AYIRDIGI UC BOYUT
    kavrayis            isleyisi anladigimiz
    firsat penceresi    mudahaleyi mumkun kilan
    vicdan              yeni kapasiteyle ne yapacagimiza
                        karar verdigimiz

    birlikte degerlendirilir:
      ihtiyac . kullanilabilir kapasite . sinama imkani

  UC KARAR AYRI VERILIR
    kesfetme | uygulama | paylasma
    daha cok sey yapabiliyor olmak, kapsami kendiliginden genisletmez

  ESIGIN YERINE GECMEZ
    kriz . gece calisma . alkis . moda . gecmis basari anlatisi

  calisan bir sistem de yeniden islevlendirilebilir;
  eskimesi ya da bozulmasi beklenmek zorunda degildir
~~~

*Çizim 9 — Zaman: farkın görünür ve müdahale edilebilir olduğu eşik; kavrayış, fırsat penceresi, vicdan.*

### Uygulama

1. “Önceden neyi anlamıyordum, şimdi neyi açıklayabiliyorum?” sorusunu yanıtla. Yeni kavrayışı onu destekleyen gözleme bağla.
2. “Neden şimdi?” sorusunu yanıtla. İhtiyaç, erişim, kapasite ve sınama imkânının hangi bakımdan bir araya geldiğini yaz; beklemenin ve erken davranmanın etkisini karşılaştır.
3. Bir sonraki denemenin süresini veya durma noktasını belirle. Bunu kavrayışı zorlayan bir son tarih olarak değil, çalışma ve gözden geçirme sınırı olarak kullan.
4. Yeni bilgi veya yeteneğin başkaları üzerindeki etkisini değerlendir. Keşfetme, uygulama ve paylaşma kararlarını ayrı ver; daha çok şey yapabiliyor olmak kapsamı kendiliğinden genişletmez.
5. Devam etme, bekletme veya önceki protokole dönme kararını gerekçesiyle kaydet. Bekleyen gerçek kullanım sınamasının koşulunu ve ne zaman gözden geçirileceğini belirt.

**Kayıt:** Kavrayış, kanıt, fırsat penceresi, zamanlama gerekçesi, sorumluluk kararı ve gözden geçirme noktası.

**Tamamlanma koşulu:** Bir sonraki eylemin zamanı ve gerekçesi bellidir. Kriz, gece çalışma, alkış, moda veya geçmiş başarı anlatısı bu eşiğin yerine geçmez. Dosya değişikliğini geri almak mümkün olsa bile öğrenilen bilginin kullanımı ve paylaşılması ayrıca sorumluluk gerektirir.

## 5 Gaye Protokolü

**Sorusu:** Hangi nihai amaca hizmet eder? Bu nihai amaca ulaştıran nelerdir? Neler değildir?

Bu protokollerde seçilen nihai yön, insanların hayatlarını şekillendiren sistemleri anlayabilme, değiştirebilme ve iyileştirebilme özgürlüğünü artırmaktır. Bu yön, anlamlı ihtiyaçları ekolojik sınırlar içinde karşılama ve gelecekteki hareket imkânlarını koruma amacıyla birlikte ele alınır. Teknik yöntem bu sonucu garanti etmez; amaç açıkça seçilir ve bulgularla yeniden değerlendirilir.

Kaynağın kişisel tutku ve oyun, toplumsal açıklık ve insanın söz sahibi olması boyutları birlikte korunur. Paylaşma, öğretme ve sorunları giderilebilecek şekilde bildirme bu amaca hizmet eder. Yazılım söz konusu olduğunda çalıştırma, inceleyip değiştirme, kopyaları paylaşma ve değiştirilmiş sürümü paylaşma imkânları ayrıca değerlendirilir; kaynakların kullanım ve paylaşım koşulları kaydedilir. Kamusal bilgiye açıklık ile kişisel verinin mahremiyeti birlikte gözetilir. [H]

~~~text
  SECILEN NIHAI YON
    insanlarin, hayatlarini sekillendiren sistemleri
        anlayabilme . degistirebilme . iyilestirebilme
    ozgurlugunu artirmak

    birlikte ele alinir:
      anlamli ihtiyaclari ekolojik sinirlar icinde karsilama
      gelecekteki hareket imkanlarini koruma

    teknik yontem bu sonucu garanti etmez;
    amac acikca secilir ve bulgularla yeniden degerlendirilir

  YARAR NASIL ANLASILIR?
    yalniz bunlara bakilmaz:     teknik performans . fiyat artisi
    bunlar da degerlendirilir:   erisim . anlasilabilirlik .
                                 bakim yuku . kaynak ihtiyaci .
                                 bagimliliklar

    kim yararlaniyor? | kim yuk ustleniyor? |
    kim karar surecine katiliyor?

  BIRLIKTE GOZETILIR
    kamusal bilgiye aciklik   <-->   kisisel verinin mahremiyeti
    belgeleme, otomatik gonderme ya da yayimlama talimati degildir

  KARAR
    uygula | daralt | yeniden dene | beklet | vazgec

  NIHAI AMACIN YERINE GECIRILMEZ
    para . un . baskalari uzerinde kontrol . yikim . sinirsiz ifsa .
    her eski varligi mutlaka kullanma zorunlulugu
~~~

*Çizim 10 — Gaye: seçilen nihai yön, yararın nasıl anlaşılacağı ve beş karar.*

### Uygulama

1. Amaç cümlesini tamamla: “Bu çalışma, ... kişilerin ... ihtiyacını karşılamasına veya ... şeyi anlayıp değiştirebilmesine katkı sağlayacak.” Öğrenme denemesiyse öğrenilmek isteneni belirt.
2. Beklenen yararın nasıl anlaşılacağını seç. Yalnız teknik performans veya fiyat artışına bakma; erişimi, anlaşılabilirliği, bakım yükünü, kaynak ihtiyacını ve bağımlılıkları da değerlendir.
3. 3'teki doğrulama ile geçerleme bulgularını ayrı oku. Kullanıcı görüşü veya gerçek kullanım sınaması yoksa yararın gösterilmediğini açıkça kaydet.
4. Kimin yararlandığını, kimin yük üstlendiğini ve kimin karar sürecine katıldığını yaz. İnsanların kendi rollerinin ve amaçlarının kurulmasına katılmasını gözet.
5. Paylaşılabilir yöntem, sonuç ve öğretme biçimini belirle. Özel veriyi ayır; bir sorun bulunduysa ilgili sorumlunun gidermesine yetecek bilgiyi hazırlayıp paylaşma kararını ayrıca kaydet. Belgeleme, otomatik gönderme veya yayımlama talimatı değildir.
6. Bulgulara göre `uygula`, `daralt`, `yeniden dene`, `beklet` veya `vazgeç` kararı ver. Kullanıma almanın ve sürdürmenin sorumlusunu belirt.

**Kayıt:** Amaç, yararlanıcı, yarar ölçütü, gerçek ihtiyaca ilişkin kanıt, toplam yükler, karar sahipleri, paylaşım koşulları ve gerekçeli karar.

**Tamamlanma koşulu:** Amaç ve seçilen eylem arasındaki bağ açıklanabilir; gösterilemeyen yararlar iddia edilmez. Para, ün, başkaları üzerinde kontrol, yıkım, sınırsız ifşa veya her eski varlığı mutlaka kullanma zorunluluğu nihai amacın yerine geçirilmez.

## 6 Kökleşme (Bitiş) Protokolü

**Sorusu:** Ne tamamlandı? Ne kökleşiyor? Sonuç, başkalarının öğrenmesine ve yeni sorulara nasıl zemin bırakacak?

Kökleşme iki yönde okunur. İlkinde merak yerini sorgulanmayan kesinliğe, paylaşım yerini saklamaya bırakır; bir zamanlar sınanan usul değiştirilemez kurala dönüşür. Kaynağın “ölüm” benzetmesinin bu yüzü, sorgulamanın donmasını anlatır. İkincisinde yapılan iş başkalarının kullanabileceği, değiştirebileceği ve üzerinden öğrenebileceği altyapıya dönüşür. Mevcut çalışma tamamlanırken yeni başlangıçların koşulları oluşur. [H]

Bu protokol hem katılaşmayı sorgular hem de sonucu devredilebilir kılar. Emeklilik, yaşlanma, meslek değiştirme, başarısızlık veya adsızlık kendi başına bu “ölüm” değildir. Bir denemenin işe yaramadığını gösteren kayıt da başka bir çalışmaya değerli zemin bırakabilir. Kullanım kararı ertelenmişse, kapanan şey araştırma döngüsüdür; gerçek kullanım başarısı tamamlanmış sayılmaz.

~~~text
  KOKLESME IKI YONDE OKUNUR

        KATILASMA                               ALTYAPI

     .-------------.                        0       0       0
     |#############|                        |       |       |
     |#############|                   =====+=======+=======+=====
     |#############|                       /|\     /|\     /|\
     `-------------'                      / | \   / | \   / | \

   merak     -->  sorgulanmayan         yapilan is, baskalarinin
                  kesinlik              kullanabilecegi,
   paylasim  -->  saklama               degistirebilecegi ve uzerinden
   sinanan        degistirilemez        ogrenebilecegi altyapiya
   usul      -->  kural                 donusur; yeni baslangiclarin
                                        kosullari olusur

  KATILASMAYI SORGULAYAN UC SORU
    hangi varsayimi artik kanitsiz dogru sayiyorum?
    hangi itirazi aliskanlikla reddediyorum?
    bilgiyi gereksiz yere kendimde mi tutuyorum?

    gerekcesiz kesinlik gorulurse ilgili protokol yeniden acilir

  KENDI BASINA BU "OLUM" DEGILDIR
    emeklilik . yaslanma . meslek degistirme . basarisizlik . adsizlik
~~~

*Çizim 11 — Kökleşme: iki yönlü okuma; katılaşma ve başkalarını besleyen altyapı.*

### Uygulama

1. Başlangıç sorusuna dön. Ne cevaplandı, ne değişti, ne açık kaldı? Sonucu ve kullanıma ilişkin durumu `calisma.md` içinde kaydet.
2. Katılaşmayı sorgula: “Hangi varsayımı artık kanıtsız doğru sayıyorum? Hangi itirazı alışkanlıkla reddediyorum? Bilgiyi gereksiz yere kendimde mi tutuyorum?” Gerekçesiz kesinlik gördüğünde ilgili protokolü yeniden aç.
3. Seçilmiş sonucu `ciktilar/` altında ayır. `devir.md` dosyasına kullanım adımlarını, gereksinimleri, sınırları, bakım sorumlusunu, geri alma veya kullanımdan çıkarma yolunu yaz. Sonuç bir öğrenmeyse bulguyu ve başarısız denemelerin neyi gösterdiğini aktar.
4. Devir denemesi yap. Mümkünse başka biri yalnızca yönergeleri izleyerek sonucu açsın, kullansın veya inceleyebilsin. Tek kişi çalışıyorsan yeni bir oturumda yalnızca yazılı kaydı izle; bunu bağımsız kullanıcı sınaması olarak gösterme.
5. Paylaşılabilir kopyayı özel veriden ayır. Öğretilebilecek bir açıklama veya örnek hazırla. Katkıları ve kaynakları görünür tut; kalıcı kullanım varsa bakım ve karar sorumluluğunu devret.
6. Yeniden açma koşulunu ve bir sonraki 0'ı başlatabilecek soruyu yaz. Gözden geçirme tarihini ya da tetikleyici olayı belirt. Ardından döngüyü gerekçeli biçimde kapat.

**Kayıt:** Kapanış durumu, sonuç ve kanıt, katılaşma değerlendirmesi, kullanım ve bakım bilgisi, devir denemesi, açık sorular ve yeniden açma koşulu.

**Tamamlanma koşulu:** Sonuç, sınırları ve sürdürülme yolu anlaşılır; bakım gerekmiyorsa bu belirtilmiştir. Kayıt başkasının öğrenmesine elverişlidir ve yeni soruların önü açık kalır. Yalnız teslim etmek, arşive kaldırmak veya “artık hep böyle yapılacak” demek yeterli değildir. **6'dan sonra yeni bir 0 açılabilir.**

~~~text
  DEVIR

    ciktilar/    secilmis sonuc; paylasilabilir kopya ozel veriden ayri
    devir.md     kullanim adimlari . gereksinimler . sinirlar .
                 bakim sorumlusu . geri alma ya da kullanimdan
                 cikarma yolu
                 (sonuc bir ogrenmeyse: bulgu ve basarisiz
                  denemelerin neyi gosterdigi)

  DEVIR DENEMESI
    baska biri, yalnizca yonergeleri izleyerek sonucu acar,
    kullanir ya da inceler

    tek kisi calisiyorsa: yeni bir oturumda yalnizca yazili kaydi
    izler; bu, bagimsiz kullanici sinamasi olarak gosterilmez

  KULLANIM DURUMU
    hazir | sinirli | bekliyor | kullanima alinmadi

    kullanim karari ertelenmisse kapanan sey arastirma dongusudur;
    gercek kullanim basarisi tamamlanmis sayilmaz

  KAPANIS ICIN YETERLI DEGILDIR
    yalniz teslim etmek . arsive kaldirmak .
    "artik hep boyle yapilacak" demek

  yeniden acma kosulu ve bir sonraki 0'i baslatabilecek soru yazilir
  6'dan sonra yeni bir 0 acilabilir
~~~

*Çizim 12 — Kökleşme: devir, devir denemesi ve kullanım durumu.*

## Çalışma kaydı şablonu

Aşağıdaki bölümü `calisma.md` içine kopyala. Alanları çalışma sırasında doldur; uygulanmayan alana gerekçesini yaz. Yeni denemelerde deneme kaydını çoğalt. Parola, erişim anahtarı veya gerekli olmayan kişisel veriyi kayda ekleme.

```markdown
# Çalışma kaydı

Çalışma adı:
Tarih ve sürüm:
Yürüten kişi veya ekip:
Amaç ve kullanım kararını veren:
Bakım veya takip sorumlusu:
İlgili kaynakların yeri:

## 0 Tohum
Durum ve kanıt yeri:
Başlangıç sorusu:
Gözlenen durum:
İlk niyet ve yararlanıcı:
Bilinenler / varsayımlar / bilinmeyenler:
İlk araştırma eylemi ve bulgusu:

## 1 Varlık
Durum ve kanıt yeri:
Mevcut varlık ve rol:
Devralınan kapasite ve kanıt:
Sınırlar ve eksik bilgi:
Farklı rol adayları:
İhtiyaçla kurulan ilişki:

## 2 Mekan
Durum ve kanıt yeri:
Çalışma ve gerçek kullanım ortamı:
Kullanıcılar ve etkilenenler:
Değişiklik ve erişim kapsamı:
Başlangıç kopyası ve geri alma yolu:
Beklenen / gözlenen işleyiş farkı:
Paylaşılabilir bilgi / özel bilgi ayrımı:

## 3 Usül
Durum ve kanıt yeri:
Karşılaştırılan alternatifler:

### Deneme D01
Tarih:
Hipotez ve dayandığı varsayım:
Başlangıç durumu:
Beklenen sonuç ve değerlendirme ölçütü:
Değişiklik:
Araç ve sürüm / varsa araç önerisinin kaynağı:
4 ve 5 bakımından uygulama koşulları:
Gözlem ve kanıt yeri:
Yorum ve açıklanamayanlar:
Doğrulama sonucu:
Geçerleme sonucu veya bekleyen sınama:
Geri alma gereği ve sonucu:
Karar ve sonraki adım:

## 4 Zaman
Durum ve kanıt yeri:
Yeni kavrayış ve kanıtı:
Neden şimdi / neden beklemek:
Çalışma süresi veya durma noktası:
Yeni kapasitenin kullanımına ilişkin sorumluluk kararı:
Gözden geçirme tarihi veya tetikleyici:

## 5 Gaye
Durum ve kanıt yeri:
Amaç cümlesi:
Yarar ve öğrenme ölçütü:
Gerçek ihtiyaca ilişkin bulgular:
Kaynak ihtiyacı / bakım yükü / bağımlılıklar:
Yarar ve yükün kimler arasında dağıldığı:
Paylaşılabilecek sonuç ve koşulları:
Karar ve gerekçesi:

## 6 Kökleşme
Durum ve kanıt yeri:
Ne tamamlandı / ne açık kaldı:
Sorgulanmadan kabul edilen varsayımlar:
Sonuç dosyaları ve devir yönergesinin yeri:
Bakım veya takip düzeni:
Devir denemesini kim, nasıl yaptı ve ne bulundu:
Kullanım durumu: hazır / sınırlı / bekliyor / kullanıma alınmadı
Kapanış kararı ve gerekçesi:
Yeniden açma koşulu:
Bir sonraki başlangıç sorusu:
```

## Geri dönüş ve yeniden açma

Bir protokolün eksik kalması kişiye verilmiş bir kimlik hükmü değildir. Eksik olan, çalışmanın hangi yönden yeniden ele alınacağını gösterir.

| Ortaya çıkan durum | Dönülecek protokol |
|---|---|
| Soru veya ilk niyet belirsizleşti | 0 Tohum |
| Kapasite iddiası kanıtsız kaldı veya yeni bilgi varlığı değiştirdi | 1 Varlık |
| Kullanıcı, ortam, erişim veya karar kapsamı değişti | 2 Mekan |
| Sonuç açıklanamıyor veya sınama yetersiz kaldı | 3 Usül |
| Müdahale penceresi kapandı ya da yeni zamanlama gerekiyor | 4 Zaman |
| Yarar gösterilemedi veya amaçla etkiler çelişti | 5 Gaye |
| Sonuç devredilemiyor, bakım aksıyor veya yöntem sorgulanamaz hâle geliyor | 6 Kökleşme; bulguya göre ilgili protokol |

## İlkelerin protokollere yerleşimi

Bu eşleştirme, kaynak ilkeler ile bu belgede önerilen masaüstü işlemleri ayırır. Uygulama adımları kaynağın birebir alıntısı değildir.

| Protokol | Hacker İlkeleri belgesinden alınan yön | Masaüstündeki karşılığı |
|---|---|---|
| 0 Tohum | Sorunun ilk eyleme dönüşmesi; meraka alan açılması | Soru, ilk gözlem ve başlangıç kaydı |
| 1 Varlık | Merak, yetkinlik ve yaratıcılık; unvan yerine yapılan iş | Kapasite ve rol adaylarını kanıtla ayırma |
| 2 Mekan | Beklenen ile gerçek arasındaki sınır; erişim, oyun ve paylaşım kültürü | Deneme alanı, bağlam, katılım ve bilgi sınırları |
| 3 Usül | Anlama, varsayımı sorgulama, kontrollü deney, aykırılığı izleme ve paylaşma | Hipotez, deneme ve iki ayrı sınama kaydı |
| 4 Zaman | Kavrayış, fırsat penceresi ve vicdan | Zamanlama ve kapasitenin kullanım kararı |
| 5 Gaye | Anlama ve iyileştirme özgürlüğü; açıklık, mahremiyet ve öğretme | Yarar, söz hakkı, paylaşım ve toplam etki değerlendirmesi |
| 6 Kökleşme | Katılaşma ile başkalarını besleyen altyapıya dönüşmenin ayrılması | Katılaşmayı sorgulama, devir, bakım ve yeni başlangıç sorusu |

## Kaynaklar

**[H]** Haluk, *Hacker İlkeleri — Tohumdan Kökleşmeye*, 29 Ekim 2026. Bu protokolün köken aldığı kimlik metnidir. Metindeki [H] göndermeleri onun ilkelerine işaret eder; her ilke, anıldığı paragrafta kendi sözleriyle özetlenmiştir.

Tarihsel ve biyografik örnekler uygulama metnine taşınmadı. Kaynağın ilkeleri davranış ve kayıt karşılıklarıyla işlendi. Önceki konuşmanın soru ve yanıtları aşağıda kaynak kayıt olarak korunur; yeni protokollerin adımları bu kayıtla karıştırılmaz.

## Ek: Konuşmadaki özgün soru ve yanıt kaydı

Bu bölümde önceki iki soru ve iki yanıt korunmuştur. Biçim Markdown düzenindedir; önceki yanıtlardaki kaynak gösterimleri K1–K3 olarak yazılmıştır.

### İlk soru

Geçmiş bağlamları buraya taşıma. Burası ile sınırlı kalma.

**Yaratıcı Yeniden İşlevlendirme Mühendisliği**

Nedir? Onu o yapan nelerdir? Neler değildir?
Nerededir? Bu yeri, oraya has bir yer yapan nelerdir? Neler değildir?
Nasıl işler yapar? Bu yaptıklarını, ona has yapan nelerdir? Neler değildir?
Hangi andadır? Bu anı, diğer zamanlardan farklı yapan nelerdir? Neler değildir?
Hangi nihai amaca hizmet eder? Bu nihai amaca ulaştıran nelerdir? Neler değildir?

### İlk yanıt

**Yaratıcı Yeniden İşlevlendirme Mühendisliği için şu tanımı öneriyorum:** Mevcut bir varlığın taşıdığı yapı, bilgi ve yetenekleri, alışılmış rolünün ötesinde bir ihtiyaçla buluşturmak; ortaya çıkan yeni işlevi gerçek koşullarda çalışır, sınanabilir ve sürdürülebilir hâle getirmek.

Burada bir çerçeve kuruyorum. Temel kabulü şu: **Bir şeyin ne için yapılmış olduğu, neye yarayabileceğini bütünüyle belirlemez.** Fakat başka bir kullanımın hayal edilebilmesi de onun uygulanmaya değer olduğunu henüz göstermez.

**Nedir? Onu o yapan nelerdir?**

Çalışma birimi, tek başına nesne değil; **varlık, ihtiyaç ve ortam arasında kurulan işlevsel ilişkidir.** Aynı nesne, başka bağlantılar ve kullanım koşulları içinde farklı bir rol üstlenebilir. Bazen fiziksel biçiminin değişmesi bile gerekmez.

Adındaki dört bileşen birbirine ayrı koşullar getirir:

| Bileşen | Onu kuran özellik | Tek başına yeterli olmayan |
|---|---|---|
| **Yaratıcı** | Alışılmış kullanımın dışında, bağlama uygun bir ilişki keşfetmek | Şaşırtıcılık, görünüş değişikliği, farklı olma isteği |
| **Yeniden** | Mevcut varlıktan anlamlı bir yapı, kapasite veya bilgi devralmak | Eskiyi tümüyle ortadan kaldırıp yerine yenisini koymak |
| **İşlevlendirme** | Gerçek bir ihtiyacı karşılayan rol ve kullanım düzeni oluşturmak | Yeni ad, hikâye veya amaç beyanı |
| **Mühendislik** | Gereksinimleri, sınırları ve başarısızlık koşullarını belirleyip sonucu sınamak | Çalışabileceğini düşünmek veya bir kez çalıştırmak |

Yaratıcılık burada dünyada ilk olmayı gerektirmez. Bilinen bir ilkenin, daha önce ilişkilendirilmemiş bir ihtiyaç ve kapasite arasında uygun biçimde kurulması da yaratıcı olabilir.

Bu düşüncenin biyolojide bir akrabası vardır: Gould ve Vrba'nın **eksaptasyon** kavramı, bir özelliğin kökeniyle sonradan üstlendiği yararlı rolü ayırır. Buradaki mühendislik yaklaşımı için bundan çıkarılabilecek düşünce, mevcut kapasitenin ilk ortaya çıkış amacıyla sınırlı okunmamasıdır. Bu, biyolojik kavramdan yaptığım bir benzetmedir. [K1]

Onarım, eski işlevi geri getirmeye; yeniden işlevlendirme, farklı bir role yönelir. Geri dönüşüm malzemeyi kazanabilir; burada mevcut örgütlenmenin ve yeteneğin korunması ayrıca araştırılır. Sanatsal dönüştürme anlam ve deneyim üretebilir; mühendislik iddiası taşıdığında bu deneyimin gerektirdiği işlevler de sınanmalıdır. Bunlar kesişebilir; hiçbiri tek başına bu yaklaşımın bütününü oluşturmaz.

**Nerededir? Bu yeri, oraya has yapan nelerdir?**

Mevcut bir kapasiteyle karşılanmamış bir ihtiyacın arasında, bağlantı kurulabilecek yerde bulunur. Bu yer bir bina, üretim hattı, yazılım, arşiv, altyapı veya kurumun çalışma düzeni olabilir.

Fakat yalnızca “elde bulunan şey” ile “ihtiyaç” yetmez. Dönüşümü mümkün kılan bilgi, erişim, karar yetkisi, kullanıcılar ve bakım imkânı da gerekir. Dolayısıyla onun yeri, fiziksel konumu aşan bir **ilişkiler bütünüdür.**

Örneğin boşalan bir okulun ortak öğrenme ve onarım merkezine dönüştürüldüğünü varsayalım. Yeri özgül kılan yalnızca sınıfların büyüklüğü değildir:

- Mahallenin hangi ihtiyaçları taşıdığı,
- İnsanların binaya nasıl ulaşabildiği,
- Yapının hangi kullanımlara elverdiği,
- Oradaki bilgi, hafıza ve toplumsal ilişkiler,
- İşletmeyi ve bakımı kimin üstlenebileceği.

Aynı mimari çözüm, başka bir mahallede aynı işlevi üretmeyebilir.

Bu nedenle yeri yalnızca atölye, tasarım ofisi veya atık sahası değildir. “Kullanılmıyor” olması da bir varlığın sahipsiz, değersiz veya serbestçe dönüştürülebilir olduğunu göstermez. Kurumlara ve toplumsal yapılara uygulandığında insanların iradesi ve karar hakkı, tasarımın kurucu koşullarıdır.

**Nasıl işler yapar? Bu yaptıklarını, ona has yapan nelerdir?**

İki yönde birlikte araştırır: **“Bu ihtiyaç başka nasıl karşılanabilir?” ve “Bu mevcut varlık başka hangi rolleri taşıyabilir?”** Böylece ne hazır malzemeye zorla ihtiyaç uydurur ne de mevcut olanı görmeden sıfırdan üretime yönelir.

Çalışması genellikle şu hareketleri içerir:

1. **Okumak:** Mevcut varlığın yeteneklerini, geçmişini, yıpranmasını ve sınırlarını anlamak.
2. **İhtiyacı belirlemek:** Kimin, hangi koşullarda, nasıl bir sonuç beklediğini açıklığa kavuşturmak.
3. **Eşleştirmek:** Mevcut kapasiteyle ihtiyaç arasında farklı bağlantılar tasarlamak.
4. **Karşılaştırmak:** Dönüştürmeyi; onarım, yeni üretim, paylaşım veya hiç müdahale etmeme seçenekleriyle değerlendirmek.
5. **Denemek ve sınamak:** Yeni rolün hangi koşullarda çalıştığını, nerede başarısız olduğunu görmek.
6. **İşletmek ve öğrenmek:** Bakımı, kullanım bilgisini ve gerektiğinde yeniden değiştirme imkânını düzenlemek.

Ona has olan, **devralınan kapasiteyle yeni gereksinim arasındaki uyumsuzluğu çözmesidir.** Yeni işleve uygun görünen bir parça, yeni ortamın yüküne, kullanım sıklığına veya bakım koşullarına uygun olmayabilir.

~~~text
  IKI YONDE BIRLIKTE ARASTIRIR

   "Bu ihtiyac baska nasil              "Bu mevcut varlik baska
    karsilanabilir?"                     hangi rolleri tasiyabilir?"

        ihtiyac  ------------->    <-------------  varlik
                           eslestirme

   boylece ne hazir malzemeye zorla ihtiyac uydurur,
   ne de mevcut olani gormeden sifirdan uretime yonelir

  ALTI HAREKET
    1 okumak                  mevcut varligin yeteneklerini, gecmisini,
                              yipranmasini ve sinirlarini anlamak
    2 ihtiyaci belirlemek     kimin, hangi kosullarda, nasil bir sonuc
                              bekledigi
    3 eslestirmek             kapasiteyle ihtiyac arasinda farkli
                              baglantilar tasarlamak
    4 karsilastirmak          onarim, yeni uretim, paylasim ya da
                              hic mudahale etmeme secenekleriyle
    5 denemek ve sinamak      hangi kosullarda calisiyor,
                              nerede basarisiz oluyor
    6 isletmek ve ogrenmek    bakim, kullanim bilgisi, gerektiginde
                              yeniden degistirme imkani

  ONA HAS OLAN
    devralinan kapasiteyle yeni gereksinim arasindaki
    uyumsuzlugu cozmesi
~~~

*Çizim 13 — Ek, ilk yanıt: iki yönde araştırma ve altı hareket.*

Burada iki ayrı sınama gerekir: Belirlediğimiz gereksinimler karşılanıyor mu? Bu gereksinimleri karşılayan çözüm, kullanıcıların gerçek ihtiyacını karşılıyor mu? NASA'nın sistem mühendisliği çerçevesindeki doğrulama ve geçerleme ayrımı da bu iki soruyu birbirinden ayırır. [K2]

Dolayısıyla yaptığı iş yalnız fikir üretmek, parçaları birleştirmek veya prototip göstermek değildir. Bir başkasının anlayabileceği, kullanabileceği ve bakımını yapabileceği bir işleyiş oluşturması gerekir.

**Hangi andadır? Bu anı, diğer zamanlardan farklı yapan nelerdir?**

**Mevcut rolle mümkün rol arasındaki farkın görünür ve müdahale edilebilir olduğu eşiktedir.**

Bu eşik bir arızayla, ihtiyaç değişikliğiyle, yeni bilgiyle veya farklı aktörlerin buluşmasıyla açılabilir. Varlığın eski işlevini tamamen kaybetmesi gerekmez. Çalışan bir sistemin içinde de henüz değerlendirilmemiş kapasiteler bulunabilir.

Bu anı özgül kılan, birkaç koşulun birlikte oluşmasıdır: İhtiyaç belirginleşmiştir; aktarılabilecek kapasite hâlâ vardır; dönüşüm mümkün hâle gelmiştir; sonucu sınayacak zaman ve imkân bulunmaktadır.

Okul örneğinde bu an, binanın boşaldığı tarih olmak zorunda değildir. Mahallenin ihtiyacının anlaşılması, kullanım hakkının açıklığa kavuşması ve işletmeyi üstlenecek insanların buluşmasıyla oluşabilir.

Dolayısıyla yalnızca kriz, eskime, hurdaya ayrılma veya yenilik modası anı değildir. Çok geç kalmak kullanılabilir kapasiteyi kaybettirebilir; çok erken müdahale etmek de hâlâ yararlı bir düzeni gereksiz yere bozabilir. Zamanlama, yaklaşımın teknik kararlarından biridir.

**Hangi nihai amaca hizmet eder? Bu amaca ulaştıran nelerdir?**

Kavramın adı tek başına etik bir nihai amaç belirlemez. Yaratıcı ve teknik bakımdan başarılı bir dönüşüm, zararlı bir amaca da hizmet edebilir. Bu yüzden teknik başarıyla amaç seçimini ayrı değerlendirmek gerekir.

**Bu yaklaşım için savunacağım nihai amaç, insanların anlamlı ihtiyaçlarını ekolojik sınırlar içinde karşılayabilme kapasitesini artırmak ve gelecekteki hareket imkânlarını korumaktır.**

Mevcut emeği, bilgiyi ve yapıları değerlendirmek; yeni kaynak ihtiyacını azaltmak; erişimi genişletmek ve bakım bağımlılığını azaltmak bu amaca hizmet edebilir. Döngüsel ekonominin atığı önleme, ürün ve malzemeleri dolaşımda tutma ve doğayı yenileme ilkeleriyle burada bir ortaklık vardır. [K3]

Fakat tasarruf, uzun ömür, yenilik veya ekonomik değer artışı tek başına nihai başarı ölçüsü olamaz. Bir dönüşüm ucuz olduğu hâlde bakım yükünü başkalarına bırakabilir; binayı yaşatırken kullanıcılarını dışlayabilir; malzemeyi korurken gereksiz tüketimi artırabilir.

Bu amaca; ihtiyacı kullanıcılarla belirlemek, seçenekleri karşılaştırmak, toplam etkileri değerlendirmek, bakım sorumluluğunu kurmak ve gerektiğinde dönüşümden vazgeçebilmek ulaştırır. Her şeyi kullanmak, her eskiyi korumak veya her şeye işlev bulmak zorunluluğu ulaştırmaz.

Varsayımsal okulun başarısı da kapılarının yeniden açılmasıyla ölçülmez. İnsanların oraya erişebilmesi, ihtiyaç duydukları faaliyetleri yapabilmesi, işletmenin sürdürülebilmesi ve sağlanan yararın üstlenilen yükü haklı çıkarmasıyla ölçülür.

~~~text
  VARSAYIMSAL ORNEK
  bosalan okul  -->  ortak ogrenme ve onarim merkezi

    mahallenin hangi               insanlarin binaya
    ihtiyaclari tasidigi           nasil ulasabildigi
                  \                   /
                 ._______________________.
                 |  []    []    []    [] |
                 |  []    []    []    [] |-----  yapinin hangi
                 |__________[  ]_________|       kullanimlara elverdigi
                  /                   \
    oradaki bilgi, hafiza          isletmeyi ve bakimi
    ve toplumsal iliskiler         kimin ustlenebilecegi

    yeri ozgul kilan yalnizca siniflarin buyuklugu degildir;
    ayni mimari cozum, baska bir mahallede ayni islevi uretmeyebilir

  AN      binanin bosaldigi tarih olmak zorunda degildir:
          mahallenin ihtiyacinin anlasilmasi . kullanim hakkinin
          acikliga kavusmasi . isletmeyi ustlenecek insanlarin
          bulusmasi

  BASARI  kapilarinin yeniden acilmasiyla olculmez:
          insanlarin oraya erisebilmesi . ihtiyac duyduklari
          faaliyetleri yapabilmesi . isletmenin surdurulebilmesi .
          saglanan yararin, ustlenilen yuku hakli cikarmasi
~~~

*Çizim 14 — Ek, ilk yanıt: okul örneğinde yer, an ve başarı.*

### İkinci soru

**Yaratıcı Yeniden İşlevlendirme Mühendisliği**'nin; köken aldığı varlık, mekan, usül, zaman, ve gayeyi taşıyan makine kimdir? Kim değildir?

### İkinci yanıt

**Bu çerçevede cevap iki düzeylidir: Özne olarak, kendi koşullarını anlayıp amaçlarını sorgulayabilen insandır; işleyiş olarak, insanların araçlarla, bilgilerle, kurumlarla ve çevreleriyle kurduğu düzenektir.** “Makine” sözcüğünü burada bu işleyişi anlatan bir benzetme olarak kullanıyorum.

Sorundaki belirleyici kelime **“taşımak”**: Bu özne, dönüştürdüğü dünyanın dışında durmaz. Kullandığı malzemeyi, düşünme biçimlerini, ihtiyaçlarını ve imkânlarını o dünyadan devralır. Yeniden işlevlendirirken kendisi de öğrenir; becerileri, ilişkileri ve amaçları değişebilir.

Beş boyut, bu taşıyıcıda şöyle karşılık bulur:

| Boyut | Kökeninden taşıdığı | Dönüştürebildiği |
|---|---|---|
| **Varlık** | Bedeni, yetenekleri, kırılganlıkları; devraldığı maddi ve düşünsel birikim | Eldekinin hangi kapasitesini nasıl kullanacağı |
| **Mekân** | İçinde yaşadığı çevre, ilişkiler, erişimler ve engeller | Varlıkların, insanların ve ihtiyaçların birbirine bağlanma biçimi |
| **Usul** | Öğrenilmiş alışkanlıklar, dil, araçlar ve yöntemler | Soruyu kurma, deneme, karşılaştırma ve sınama yolu |
| **Zaman** | Bellek, birikmiş emek, eskime ve içinde bulunduğu koşullar | Ne zaman müdahale edeceği; neyi sürdüreceği, neyi bırakacağı |
| **Gaye** | İhtiyaçlar, değerler, arzular ve başkalarıyla paylaşılan beklentiler | Hangi amacı benimseyeceği, değiştireceği veya reddedeceği |

Onu bu pratiğin öznesi yapan, yalnızca yeni kullanımlar bulması değildir. **Kendi bulduğu kullanımı da değerlendirebilmesidir:** İşe yarıyor mu? Kimin ihtiyacını karşılıyor? Neyi koruyor, neyi kaybettiriyor? Yapabiliyor olmamız, yapmamız için yeterli mi?

Burada bir ayrım açılır: **Gayeyi taşımak, gayeyi seçmekle aynı şey değildir.** Bir cihaz, içine yerleştirilen amaç doğrultusunda işleyebilir. “Kim?” sorusu ise amacın kurulmasına katılan, onu değiştirebilen ve sonuçlarının hesabını üstlenen tarafı da arar.

**Kim değildir?**

- **Koşulsuz bir yaratıcı değildir.** Malzemesini, dilini, bilgisini ve imkânlarını bütünüyle kendisi yaratmaz.
- **Yalıtılmış bir dâhi değildir.** Dönüşüm, çoğu zaman başkalarının emeği, bilgisi ve bakımıyla mümkün olur.
- **Yalnızca verilen hedefi uygulayan yürütücü değildir.** Burada aranan özne, hedefin uygunluğunu da sorgulayabilir.
- **Yalnızca beyin, yazılım veya cihaz değildir.** Bunlar işleyişin önemli bileşenleri olabilir; kullanıcıları, çevreyi ve karar ilişkilerini tek başlarına karşılamazlar.
- **Başkalarının amaçları için yeniden işlevlendirilecek bir hammadde değildir.** İnsan, kendi rolünün ve amacının kurulmasına katılma hakkını taşır.

Bu nedenle “kim” her zaman tek bir kişi olmayabilir. Bir ekip veya topluluk da bu özne konumunu birlikte kurabilir. O durumda yaratıcılık ve bilgi paylaşılırken **amacı kimin belirlediği, kararı kimin verdiği ve bakım sorumluluğunu kimin üstlendiği** açık kalmalıdır.

### Konuşma yanıtlarında kullanılan kaynaklar

- **[K1]** Stephen Jay Gould ve Elisabeth S. Vrba. Exaptation—a Missing Term in the Science of Form. Paleobiology, 8(1), 1982, s. 4–15. Adres: https://doi.org/10.1017/S0094837300004310
- **[K2]** NASA. Systems Engineering Handbook, 2.0 Fundamentals of Systems Engineering. Özellikle 2.4 Distinctions between Product Verification and Product Validation. Adres: https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/
- **[K3]** Ellen MacArthur Foundation. Circular Economy Principles. 21 Ağustos 2024. Adres: https://www.ellenmacarthurfoundation.org/circular-economy-principles

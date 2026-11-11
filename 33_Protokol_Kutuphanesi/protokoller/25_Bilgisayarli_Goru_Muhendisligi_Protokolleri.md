# Bilgisayarlı Görü Mühendisliği Protokolleri

**Sürüm:** 1.0\
**Tarih:** 31 Ekim 2026\
**Belge durumu:** 0–6 protokolleri tamamlanmış masaüstü uygulama sürümü\
**Biçim:** UTF-8 Markdown

Bu dosya, Bilgisayarlı Görü Mühendisliği üzerine yürütülen sorgulamayı yedi protokol hâlinde düzenler. Varlık, mekân, usul, zaman ve gaye açıklamaları soru ve yanıtlara dayanır. Tohum çalışmanın başlangıcını kurar; Kökleşme elde edilen kavrayışı dayanakları ve açık sorularıyla birlikte kayda geçirir.

Protokoller bir metin veya Markdown düzenleyicisinde uygulanır. Kavramsal açıklamalar okunur, ilgili masaüstü adımları yürütülür ve elde edilen sonuçlar bu dosyanın sonundaki Çalışma Kaydı bölümüne yazılır. Uygulama, alanı kavramsal olarak incelemek, bir görü sistemini tasarlamak veya mevcut bir sistemi değerlendirmek için kullanılabilir.

Sorular kullanıcıya aittir. Kavramsal yanıtlar ve taşıyıcı makine açıklaması bu söyleşide geliştirilmiş yorum ve açıklamaları kaydeder. Uygulama adımları, bunları masaüstünde yürütülebilir bir çalışma düzenine dönüştürür. Teknik örnekler ve tarihsel değerlendirmeler, yanında belirtilen kapsam ve tarihle okunur.

## Masaüstünde kullanım

1. Dosyanın bir çalışma kopyasını oluşturun ve aynı kopya üzerinde ilerleyin. Örneğin çalışma kopyasını `Bilgisayarli_Goru_Calismasi_2026-10-31.md` adıyla, kendi seçtiğiniz masaüstü klasöründe saklayabilirsiniz. Kaydı UTF-8 metin olarak ve `.md` uzantısıyla kaydedin.

2. Önce Çalışma Bilgisi alanını doldurun. Çalışma türünü kavramsal inceleme, teknik tasarım veya teknik deneme olarak belirtin. Kavramsal incelemede açıklamalar ve dayanaklar; teknik tasarımda bunlara ek olarak yöntem ve değerlendirme planı; teknik denemede ise gerçekten yapılmış ölçüm ve gözlemler kaydedilir.

3. İlk geçişte 0'dan 6'ya ilerleyin. Bir bölümde başka bir bölümün tanımını değiştiren sonuç çıkarsa ilgili kayda dönün ve değişikliğin gerekçesini yazın. Bölümler arasındaki numara sırası, gerektiğinde geri dönmeyi engellemez.

4. Her önemli ifadede dayanağın kaynak, doğrudan gözlem, yorum veya çalışma varsayımı olduğunu belirtin. Bir bilgi bulunmuyorsa açık soru olarak kaydedin ve mevcut sonuca etkisini yazın. Planlanan denemeyi yapılmış denemeden ayrı tutun.

5. Tamamlanma kutularını, ilgili protokolün çıktısı Çalışma Kaydı'na işlendiğinde işaretleyin. Buradaki tamamlanma, seçilen çalışma türüne ait kaydın tamamlanmasıdır. Teknik bir sistem için başarı iddiası, yalnız gerçekten yapılan değerlendirmelerin kapsamına dayanır.

~~~text
  CALISMA TURU  Calisma Bilgisi alanina yazilir
    kavramsal inceleme   aciklamalar ve dayanaklar
    teknik tasarim       bunlara ek olarak yontem ve degerlendirme plani
    teknik deneme        gercekten yapilmis olcum ve gozlemler

  SIRA
    0 --> 1 --> 2 --> 3 --> 4 --> 5 --> 6      ilk geciste
    bir bolumde baska bir bolumun tanimini degistiren sonuc cikarsa
      -->  ilgili kayda donulur; degisikligin gerekcesi yazilir
    numara sirasi gerektiginde geri donmeyi engellemez

  HER ONEMLI IFADEDE DAYANAK
    kaynak  |  dogrudan gozlem  |  yorum  |  calisma varsayimi
    bulunmayan bilgi  -->  acik soru + mevcut sonuca etkisi
    planlanan deneme  =/=  yapilmis deneme

  TAMAMLANMA
    kutular:  protokolun ciktisi Calisma Kaydi'na islendiginde
    secilen calisma turune ait kaydin tamamlanmasi
    teknik bir sistem icin basari iddiasi  -->  yalniz gercekten
    yapilan degerlendirmelerin kapsamina dayanir
~~~

*Çizim 1 — Masaüstünde kullanım: çalışma türü; sıra ve geri dönüş; dayanak; tamamlanma.*

## Protokol dizisi

| Bölüm | Temel çıktı |
| --- | --- |
| 0 Tohum (Başlangıç) Protokolü | Başlangıç sorusu, kapsam, girdiler ve beklenen sonuç |
| 1 Varlık Protokolü | Tanım, ayırt edici ilişkiler, taşıyıcı ve sınırlar |
| 2 Mekan Protokolü | Edinim, hesaplama ve kullanım bağlamı |
| 3 Usül Protokolü | Yöntem, değerlendirme ve hata incelemesi |
| 4 Zaman Protokolü | Tarihsel bağlam, kullanılabilir süre ve yeniden inceleme koşulları |
| 5 Gaye Protokolü | Teknik çıktıdan üst amaca uzanan ilişki |
| 6 Kökleşme (Bitiş) Protokolü | Bütünlüklü sonuç, dayanaklar, açık sorular ve kapanış |

## Ortak taşıyıcı sorusu

> Bilgisayarlı Görü Mühendisliği'nin; köken aldığı varlık, mekan, usül, zaman, ve gayeyi taşıyan makine kimdir? Kim değildir?

Bu sorudaki makine, belirli bir işi ilişkili parçalarıyla gerçekleştiren bütün olarak yorumlanmıştır. Görmenin doğal örneği olan canlı, mühendisliği kuran insanlar ve işlemleri gerçekleştiren teknik sistem ayrı taşıyıcılardır. Bütün, insanların görsel bilgi üretmek ve kullanmak üzere araçlarıyla ve çalışma ortamıyla kurduğu ilişkide ele alınır. Her protokol bu ilişkinin kendi boyutunu açıklar; Kökleşme bunları yeniden birleştirir.

~~~text
  MAKINE  belirli bir isi iliskili parcalariyla gerceklestiren butun

  AYRI TASIYICILAR
    +------------------+  +------------------+  +------------------+
    | gormenin dogal   |  | muhendisligi     |  | islemleri        |
    | ornegi: canli    |  | kuran insanlar   |  | gerceklestiren   |
    |                  |  |                  |  | teknik sistem    |
    +------------------+  +------------------+  +------------------+

  BUTUN  insanlarin gorsel bilgi uretmek ve kullanmak uzere
         araclariyla ve calisma ortamiyla kurdugu iliskide ele alinir
    her protokol  -->  bu iliskinin kendi boyutunu aciklar
    Koklesme      -->  bunlari yeniden birlestirir
~~~

*Çizim 2 — Ortak taşıyıcı sorusu: makine; ayrı taşıyıcılar; bütün.*

## 0 Tohum (Başlangıç) Protokolü

### Yürütme soruları

Bu çalışma hangi sorudan doğdu? Neyi açıklığa kavuşturmak için başlıyor? Hangi girdiler ve sınırlar içinde yürütülecek? Bu çalışma turunun beklenen çıktısı nedir?

### Kavramsal açıklama

Tohum, çalışmayı doğuran ilk soruyu, ihtiyacı veya sezgiyi başlangıç koşullarıyla birlikte kaydeder. İnceleme başlamadan önce neyin araştırılmaya değer bulunduğu görünür hâle gelir. Sonraki protokoller ayrıntılandırıldığında bu başlangıç kaydı, nereden yola çıkıldığını ve sorunun nasıl değiştiğini anlamayı sağlar.

Tohumun konusu araştırmanın doğuşudur. Varlık Protokolü ise araştırılan şeyin kimliğini ve onu o yapan ilişkileri ele alır. Tohumda yazılan başlangıç niyeti, Gaye Protokolü'nde incelenen alanın veya sistemin üst amacıyla da ayrılır. Biri bu çalışma turunun neden açıldığını, diğeri ele alınan yapının neye hizmet ettiğini açıklar.

Bu söyleşinin başlangıcında Bilgisayarlı Görü Mühendisliği'ni beş boyutta anlama isteği bulunur. Taşıyıcı makine sorusu, bu boyutların hangi bütünde birlikte bulunduğunu araştırmaya açmıştır. “Geçmiş bağlamları buraya taşıma. Burası ile sınırlı kalma.” talebi, başlangıçtaki kapsam yönelimini kaydeder. Kaynaklarla genişleme bu kapsam içinde yapılır; kişisel geçmiş veya ilgisiz başka çalışmalar kendiliğinden eklenmez.

Tohum, sonucu önceden kesinleştiren hüküm değildir. İnceleme sırasında soru veya kapsam değişebilir. Değişiklik, ilk biçim ve gerekçe korunarak kaydedilir; böylece başlangıç ile ulaşılan yer arasındaki ilişki izlenebilir.

### Amaç ve girdi

Bu çalışma turunun sorusunu, kapsamını, girdilerini ve beklenen çıktısını açıklığa kavuşturmak.

**Girdi:** Mevcut sorular ve yanıtlar, bu dosyadaki kavramsal açıklamalar, çalışmaya dâhil edilen kaynaklar ve varsa incelenecek somut görü uygulaması.

### Masaüstü uygulaması

1. Çalışma kopyasını açın. Çalışma adı, uygulayan kişi veya ekip, tarih, çalışma türü ve sürüm bilgilerini Çalışma Bilgisi alanına yazın.
2. Başlangıç sorusunu anlamını değiştirmeden kaydedin. Ardından bu turda neyi açıklığa kavuşturmak istediğinizi bir paragrafla belirtin.
3. İncelenecek birimi seçin: alanın bütünü, belirli bir görü görevi veya belirli bir teknik sistem. Dâhil edilen ve kapsam dışında bırakılan konuları ayırın.
4. Kullanılacak kaynak, görüntü, veri, not veya mevcut sonuçların adını ve erişim yerini yazın. Bilinen açıklamaları, çalışma varsayımlarını ve açık soruları ayırın.
5. Bu tur sonunda beklediğiniz somut kaydı belirtin. Beklenen çıktı bir kavramsal açıklama, bir tasarım kararı veya belirli koşullarda yapılmış bir değerlendirme olabilir; seçilen çalışma türüyle uyumunu kontrol edin.

~~~text
  UC BOLUMUN KONUSU
    0 Tohum    arastirmanin dogusu:  bu calisma turu neden acildi?
    1 Varlik   arastirilan seyin kimligi ve onu o yapan iliskiler
    5 Gaye     ele alinan yapinin neye hizmet ettigi
    tohumdaki baslangic niyeti  =/=  incelenen alanin veya sistemin
                                     ust amaci

  BASLANGIC
    bes boyutta anlama istegi  +  tasiyici makine sorusu
    kapsam yonelimi:  "Gecmis baglamlari buraya tasima. Burasi ile
                      sinirli kalma."
    kaynaklarla genisleme bu kapsam icinde; kisisel gecmis veya
    ilgisiz baska calismalar kendiliginden eklenmez
    tohum  =/=  sonucu onceden kesinlestiren hukum
    soru veya kapsam degisirse  -->  ilk bicim ve gerekce korunarak
                                     kaydedilir

  INCELENECEK BIRIM  biri secilir
    alanin butunu | belirli bir goru gorevi | belirli bir teknik sistem
    beklenen cikti:  kavramsal aciklama | tasarim karari | belirli
    kosullarda yapilmis degerlendirme  (calisma turuyla uyumlu)
~~~

*Çizim 3 — Tohum: üç bölümün konusu; başlangıç ve kapsam; incelenecek birim ve beklenen çıktı.*

### Oluşturulacak çıktı

Başlangıç sorusu, araştırma gerekçesi, kapsam, girdiler, varsayımlar, açık sorular ve beklenen sonuçtan oluşan Tohum kaydı.

### Tamamlanma ve yeniden açma

**Tamamlanma:** Başka bir okuyucu neyin, hangi girdilerle ve hangi amaçla inceleneceğini anlayabiliyorsa Tohum kaydı tamamlanmıştır. Başlangıçta yanıtlanamayan soruların açıkça kaydedilmesi ilerlemeye engel değildir.

**Yeniden açma:** Konu, kapsam veya beklenen çıktı değiştiğinde bu kayda dönün. Yeni biçimi ve değişiklik gerekçesini Değişiklik Kaydı'na ekleyin.

## 1 Varlık Protokolü

### Kayıtlı sorular

> Nedir? Onu o yapan nelerdir? Neler değildir?

### Kavramsal açıklama

#### Alanı tanımlayan çekirdek

Bilgisayarlı görü mühendisliğinin çekirdeği, görsel gözlemden göreve uygun bilgi veya temsil üretmek ve bu üretimin kullanılabilirliğini sınamaktır. Görüntünün elde edilmesi, görüntüden çıkarım yapılması ve çıkarıma dayanılarak bir iş yürütülmesi farklı adımlardır. Alan, bu adımlar arasındaki bağı kurarak gözlemin nasıl oluştuğunu, neyi desteklediğini ve hangi kullanım için yeterli olduğunu birlikte ele alır.

Kamera nesnenin ne olduğunu doğrudan kaydetmez. Aydınlatma, yüzeyler, bakış açısı, optik ve sensörün birlikte oluşturduğu gözlemi kaydeder. Görü sistemi bu gözlemden biçim, konum, hareket, sınır, sınıf veya başka bir özellik çıkarır. Görüntü, temsil ettiği dünya veya görsel içerikle özdeş değildir. ([1], [2])

Aynı şey farklı koşullarda farklı görünebilir; farklı şeyler de benzer görünebilir. Bir koyuluk, yüzeyin renginden veya gölgeden kaynaklanabilir. Küçük görünen bir nesne küçük ya da uzakta olabilir. Bu nedenle pek çok görü problemi, gözlenen etkiden onu oluşturmuş olabilecek duruma gitmeye çalışan bir ters problem niteliğindedir. Ek bakışlar, zaman içindeki hareket, geometrik bilgi ve öğrenilmiş düzenlilikler belirsizliği azaltabilir.

Alanı ayırt eden, görsel yapının görevle ilişkili özelliklerini kullanmasıdır. Görüntüdeki değerlerin nerede bulunduğu, birbirine nasıl bağlandığı ve zaman içinde nasıl değiştiği önemlidir. Her ayrıntı her görev için aynı değerde değildir. Sayma işinde önemsiz olan renk, olgunluk değerlendirmesinde belirleyici olabilir. Başarı, hangi değişikliklerin anlamı koruduğunu ve hangilerinin değiştirdiğini göreve uygun biçimde ayırt etmeyi gerektirir.

~~~text
  GORUNTU NASIL OLUSUR  [1] [2]
    aydinlatma  +  yuzeyler  +  bakis acisi  +  optik  +  sensor
                               |
                               v
                       kaydedilen gozlem    kamera nesnenin ne
                               |            oldugunu dogrudan
                               v            kaydetmez
                         goru sistemi
                               |
                               v
       bicim . konum . hareket . sinir . sinif . baska ozellik
    goruntu  =/=  temsil ettigi dunya veya gorsel icerik

  TERS PROBLEM  gozlenen etkiden onu olusturmus olabilecek duruma
    bir koyuluk          yuzeyin rengi mi?      golge mi?
    kucuk gorunen nesne  kucuk mu?              uzakta mi?
    belirsizligi azaltabilir:  ek bakislar . zaman icindeki hareket .
    geometrik bilgi . ogrenilmis duzenlilikler

  GOREVE BAGLI AYRINTI
    renk:  sayma isinde onemsiz  |  olgunluk degerlendirmesinde
                                    belirleyici olabilir
    goruntuyu elde etmek --> cikarim yapmak --> is yurutmek:  farkli
    adimlar
~~~

*Çizim 4 — Varlık: görüntünün oluşumu; ters problem; göreve bağlı ayrıntı.*

#### Taşıyıcı özne ve teknik sistem

Görmenin doğal örneği, çevresinden gelen görsel bilgiyi yaşamı ve davranışı içinde kullanabilen canlıdır. Göz, bu daha geniş algılama düzeninin bir parçasıdır. Bilgisayarlı görü biyolojik görmenin incelenmesinden beslenir; bunun yanında fizik, geometri, psikoloji ve bilgisayar bilimi de alanın kuruluşuna katılır. ([1])

Bu söyleşide önerilen çerçevede, mühendisliğin kurucu öznesi, görsel bilgiyle ne yapılabileceğini soran, bunun için yöntem geliştiren veya seçen ve sonucu sınayan insanlardır. Bilgisayarlı görü mühendisi bu rolün mesleki taşıyıcılarından biridir. Araştırmacılar, görüntüleme uzmanları, alan uzmanları, veri hazırlayanlar, geliştiriciler ve kullanıcılar farklı sorumlulukları paylaşabilir. Alanın taşıyıcısı tek ve yalıtılmış bir kişi olarak açıklanamaz.

Teknik taşıyıcı, görsel veriyi işleyip görev için sonuç üreten bilgisayarlı görü sistemidir. Sistem içinde gözlenen nesnenin kendisi bulunmaz; onun gözlenmiş özelliklerini taşıyan veriler ve bu verilerden üretilen temsiller bulunur. “Bu bölgede çatlak var” çıktısı, nesne hakkında sınanabilir bir iddiadır. Makinenin bir varlığı taşıması, burada o varlığı içinde bulundurmak değil, onunla gözlem ve temsil üzerinden ilişki kurmak anlamına gelir.

#### Kimliği açıklamaya yetmeyenler

Görüntü kaydetmek, bir model çalıştırmak, sinir ağı eğitmek veya görüntü üzerine kutular çizmek alanın bütününü tek başına açıklamaz. Bunlar gerçek bir görü sisteminin parçaları olabilir; ancak çıkarımın doğruluğu, sınırları ve kullanım koşulları ayrıca ele alınır. Kamera, model, GPU, insan gözü veya tek bir mühendis bütünün yerine geçirilemez.

~~~text
  TASIYICILAR
    dogal ornek        cevresinden gelen gorsel bilgiyi yasami ve
                       davranisi icinde kullanabilen canli; goz, daha
                       genis bir algilama duzeninin parcasi
    kurucu ozne        gorsel bilgiyle ne yapilabilecegini soran,
                       yontem gelistiren veya secen, sonucu sinayan
                       insanlar; muhendis mesleki tasiyicilardan biri
    teknik tasiyici    gorsel veriyi isleyip gorev icin sonuc ureten
                       bilgisayarli goru sistemi

  SISTEMIN ICINDE
    bulunmaz   gozlenen nesnenin kendisi
    bulunur    gozlenmis ozelliklerini tasiyan veriler + bu verilerden
               uretilen temsiller
    "Bu bolgede catlak var"  -->  nesne hakkinda sinanabilir bir iddia
    tasimak:  icinde bulundurmak degil; gozlem ve temsil uzerinden
              iliski kurmak

  BUTUNUN YERINE GECIRILEMEZ
    kamera . model . GPU . insan gozu . tek bir muhendis
    goruntu kaydetmek, model calistirmak, sinir agi egitmek, kutu
    cizmek:  parca olabilir; butunu tek basina aciklamaz
~~~

*Çizim 5 — Varlık: taşıyıcılar; sistemin içinde bulunan ve bulunmayan; bütünün yerine geçirilemeyenler.*

Görüntü işleme, makine öğrenmesi, robotik ve üretken görsel yöntemler kesin sınırlarla alanın dışına atılmaz. Görüntü iyileştirme, hizalama, yeniden oluşturma ve sentez, görü problemleriyle kesişebilir. Her sistemin insan görmesini bütünüyle kopyalaması, sahnedeki her şeyi anlaması veya her gözleme kesin bir açıklama vermesi gerekmez. Araştırma yeni bilgi ve yöntemler üretmeye, mühendislik bunları belirli ihtiyaçlar için gerçekleştirmeye yönelir; aynı çalışma ikisini birden içerebilir.

### Amaç ve girdi

İncelenen şeyin kimliğini, ayırt edici ilişkilerini ve onu taşıyan insan, canlı, araç veya sistem rollerini açıkça tanımlamak.

**Girdi:** Tohum kaydındaki soru ve kapsam; Varlık Protokolü'nün kavramsal açıklaması; varsa seçilen görev veya sistemin tanımı.

### Masaüstü uygulaması

1. İncelenen şeyi bir paragrafta tanımlayın. Tanımda hangi görsel veriden hangi bilgi veya temsilin üretildiğini ve bunun hangi kullanım için ele alındığını belirtin.
2. Gözlenen şey, gözlem verisi, üretilen temsil veya çıkarım ve kullanım kararını ayırın. Birini diğerinin kendisiymiş gibi anlatan ifadeleri düzeltin.
3. Tanımın ayırt edici ilişkilerini yazın. Benzer alanlarla ortak özellikleri, yalnız bu alana aitmiş gibi göstermeden açıklayın.
4. Taşıyıcıları belirtin: görmenin doğal örneği, çalışmayı kuran veya değerlendiren insanlar, teknik işlemi yapan sistem ve sonucun kullanıcısı. İnceleme için geçerli olmayan rolü gerekçesiyle belirtin.
5. “Neler değildir?” yanıtını yazın. Tamamen kapsam dışı olanlarla, çalışmanın parçası olabilen fakat bütünü tek başına açıklamayan öğeleri ayırın.

### Oluşturulacak çıktı

Çalışma tanımı, ayırt edici ilişkiler, taşıyıcı rolleri ve kimlik sınırlarından oluşan Varlık kaydı.

### Tamamlanma ve yeniden açma

**Tamamlanma:** Tanım, incelenen birimi ve görsel gözlemle kurduğu ilişkiyi açıkça gösteriyorsa; kamera, model veya tek kişi bütünün yerine geçirilmemişse kayıt tamamlanmıştır.

**Yeniden açma:** İncelenen birimin ne olduğu belirsizleşirse Tohum'a dönün. Sonraki bölümler tanımı değiştirirse Varlık kaydını ve değişiklik gerekçesini güncelleyin.

## 2 Mekan Protokolü

### Kayıtlı sorular

> Nerededir? Bu yeri, oraya has bir yer yapan nelerdir? Neler değildir?

### Kavramsal açıklama

#### Disiplinler ve sistem içindeki yer

Bilgisayarlı görü mühendisliğinin yeri, disiplinler içindeki konumu, sistem içindeki işlevi ve kullanım ortamı birlikte düşünülerek belirlenir. Fizik ve optik görüntünün nasıl oluştuğunu; geometri görüntüdeki ölçümlerin neye karşılık geldiğini; istatistik ve öğrenme örneklerden hangi düzenliliklerin çıkarılabildiğini araştırır. Yazılım ve sistem mühendisliği hesaplamanın işletilmesini, uygulama bilgisi ise hangi farkın önemli olduğunu ve sonucun ne işe yaradığını belirlemeye katılır.

Bir proje bu alanların hepsini aynı ağırlıkla kullanmaz. Belge okuma ile robotun bir parçayı kavraması aynı geometrik hassasiyeti gerektirmez. Her mühendisin bütün bileşenleri tek başına geliştirmesi de gerekmez. Kendi bileşeninin hangi varsayımlara bağlı olduğunu ve diğer bileşenlerle nasıl ilişkilendiğini bilmesi, çalışmanın bütünlüğünü korur.

Sistem içindeki konum, gözlem ile kullanım arasındadır. Bir üretim hattında kamera görüntü üretir, algoritma şüpheli bölgeyi bulur, başka bir yazılım sonucu belirli parçayla eşleştirir ve ayırma mekanizması müdahale eder. Doğru çıkarım yanlış parçaya bağlandığında veya yanlış birimle iletildiğinde, modelin tek başına doğru olması yeterli değildir.

Kamera kalibrasyonu bu ilişkinin somut örneklerinden biridir. Kalibrasyon, iç parametreler ve mercek bozulmaları gibi özellikleri tahmin ederek görüntü ölçümlerini bir kamera modeliyle ilişkilendirir. Fakat herhangi bir pikselin üç boyutlu dünya konumunu tek başına vermez; derinlik veya bilinen bir düzlem gibi ek bilgi gerekebilir. Sayısal çıktının dünyaya ilişkin bir iddiaya dönüşmesi, bu bağlantıların geçerliliğine bağlıdır. ([3], [4])

~~~text
  DISIPLINLER VE KATKILARI
    fizik ve optik          goruntu nasil olusur?
    geometri                olcumler neye karsilik gelir?
    istatistik ve ogrenme   orneklerden hangi duzenlilikler cikar?
    yazilim ve sistem       hesaplamanin isletilmesi
    muhendisligi
    uygulama bilgisi        hangi fark onemli? sonuc ne ise yarar?
    her proje hepsini ayni agirlikla kullanmaz

  SISTEM ICINDEKI KONUM  gozlem ile kullanim arasinda
    kamera                 goruntu uretir
      |
    algoritma              supheli bolgeyi bulur
      |
    baska bir yazilim      sonucu belirli parcayla eslestirir
      |
    ayirma mekanizmasi     mudahale eder
    dogru cikarim yanlis parcaya baglanir veya yanlis birimle
    iletilirse  -->  modelin tek basina dogru olmasi yetmez

  KALIBRASYON  [3] [4]
    ic parametreler ve mercek bozulmalari gibi ozellikler tahmin edilir
    goruntu olcumleri  <---->  kamera modeli
    bir pikselin uc boyutlu dunya konumunu tek basina vermez;
    ek bilgi gerekebilir:  derinlik . bilinen bir duzlem
~~~

*Çizim 6 — Mekan: disiplinler; sistem içindeki konum; kalibrasyon.*

#### Gözlem ve kullanım ortamı

Alan fabrikada, tarlada, laboratuvarda, telefonda, uyduda, arşivde veya bir robotta bulunabilir. Bu ortamlar yalnız örnek uygulama alanları değildir; problemin niteliğini değiştirirler. Kontrollü bir düzende ışık ve kamera konumu sabitlenebilir. Açık ortamda bunlar değişebilir. Hazır arşivde görüntünün edinimine müdahale edilemeyebilir; canlı bir düzende yeni bakışlar elde etmek mümkün olabilir.

Ortam, hesaplamanın anlamına sonradan eklenen bir ayrıntı değildir. Eğitimde görülen görüntüler ile kullanımda karşılaşılan görüntülerin özellikleri farklılaştığında aynı model farklı başarı gösterebilir. Veri dağılımındaki değişim, yöntemin hangi koşullarda geçerli olduğunun ayrıca incelenmesini gerektirir. ([5])

Bir çizginin kusur sayılması da yalnız görünüşünden çıkarılamayabilir. Parçanın işlevi, beklenen özellikleri ve kabul edilen sınırlar bu tanıma katılır. Görsel kanıtın elde edildiği yer ile kanıtın anlamlandırıldığı kullanım bağlamı birlikte düşünülür.

#### Mekânı taşıyan sistem ve sınırları

Teknik sistem, belirli bir konumdan veya edinim düzeninden gelen veriyle çalışır. Bazı yüzeyler görünür, bazıları örtülür; bir bakıştan ayırt edilen özellik başka bir bakıştan kaybolabilir. Önceden kaydedilmiş bir görüntü de edinim koşullarının izlerini taşır. Mekânı taşımak, yalnız bir cihazın bir yerde bulunması değil, gözlemin hangi ilişkiler içinde mümkün olduğunu korumaktır.

Bu yer yalnız bir işlemcinin belleği, bir laboratuvar veya bir yazılım ekibiyle özdeş değildir. Alan yalnız robotikte ya da doğrudan fiziksel kamera girdisinde de bulunmaz; ekran görüntüleri, çizimler ve dijital belgeler üzerinde çalışabilir. Hesaplamanın yapıldığı yer, gözlemin edinildiği yer ve sonucun kullanıldığı bağlam farklı olabilir. Sistemin kapsamı, bu ilişkileri açıklayacak biçimde kurulur; ortamın etkisini yok saymak da her şeyi ayrım gözetmeden aynı makinenin parçası saymak da açıklayıcılığı azaltır.

~~~text
  ORTAM PROBLEMIN NITELIGINI DEGISTIRIR
    fabrika . tarla . laboratuvar . telefon . uydu . arsiv . robot
    kontrollu duzen    isik ve kamera konumu sabitlenebilir
    acik ortam         bunlar degisebilir
    hazir arsiv        edinime mudahale edilemeyebilir
    canli duzen        yeni bakislar elde etmek mumkun olabilir

    egitimde gorulen ve kullanimda karsilasilan goruntulerin ozellikleri
    farklilasirsa  -->  ayni model farkli basari gosterebilir  [5]
    bir cizgi kusur mu?  -->  parcanin islevi . beklenen ozellikler .
                              kabul edilen sinirlar

  UC YER  farkli olabilir
    gozlemin edinildigi yer
    hesaplamanin yapildigi yer
    sonucun kullanildigi baglam
    bazi yuzeyler gorunur, bazilari ortulur; kayitli goruntu de
    edinim kosullarinin izini tasir
    mekani tasimak:  gozlemin hangi iliskiler icinde mumkun oldugunu
    korumak
~~~

*Çizim 7 — Mekan: ortamlar; üç yer; mekânı taşımak.*

### Amaç ve girdi

Gözlemin, hesaplamanın ve kullanımın nerede gerçekleştiğini; bu yer ve koşulların sonucun geçerliliğini nasıl etkilediğini belirlemek.

**Girdi:** Tohum ve Varlık kayıtları; varsa görüntülerin edinim bilgileri, sistem bileşenleri, uygulama ortamı ve arayüz bilgileri.

### Masaüstü uygulaması

1. Gözlemin edinildiği ortamı, hesaplamanın yapıldığı ortamı ve sonucun kullanıldığı bağlamı ayrı ayrı yazın. Arşiv veya dijital içerikle çalışılıyorsa bilinen edinim ve üretim koşullarını belirtin.
2. Bileşenler arasındaki bağlantıyı açıklayın. Veri, nesne kimliği, koordinat, birim veya çıktı bir bileşenden diğerine nasıl aktarılıyor; yalnız bu çalışma için ilgili olanları kaydedin.
3. Bakış açısı, ışık, örtülme, çözünürlük veya veri kaynağı gibi sonucu etkileyen koşulları seçin ve etkisini açıklayın. Bilinmeyen koşulları açık soru olarak bırakın.
4. Çıkarımın geçerli olduğu ortamı ve başka ortama taşınırken yeniden incelenmesi gereken varsayımları yazın. Gözlemin anlamını belirleyen uygulama bilgisini ayrıca belirtin.

### Oluşturulacak çıktı

Edinim, hesaplama ve kullanım bağlamlarını; bileşen bağlantılarını ve geçerlilik koşullarını bir araya getiren Mekan kaydı.

### Tamamlanma ve yeniden açma

**Tamamlanma:** Okuyucu verinin nereden geldiğini, sonucun nerede kullanıldığını ve hangi ortam varsayımlarına bağlı olduğunu anlayabiliyorsa kayıt tamamlanmıştır. Konum veya birim iddiası varsa dayandığı dönüşüm ya da açık eksik belirtilmiştir.

**Yeniden açma:** Kamera, veri kaynağı, ortam, bileşen bağlantısı veya kullanım bağlamı değiştiğinde ilgili koşulları yeniden inceleyin; değişiklik kimliği etkiliyorsa Varlık'a dönün.

## 3 Usül Protokolü

### Kayıtlı sorular

> Nasıl işler yapar? Bu yaptıklarını, ona has yapan nelerdir? Neler değildir?

### Kavramsal açıklama

#### Yapılan işler ve üretilen sonuçlar

Bilgisayarlı görü, tek bir tanıma işleminden oluşmaz. Sınıflandırma görüntünün veya bölgenin hangi sınıfa ait olduğunu; nesne tespiti aranan şeyin nerede bulunduğunu; bölütleme hangi görüntü noktalarının hangi nesneye veya bölgeye ait olduğunu araştırır. Geometrik çıkarım biçim, uzaklık ve duruşla; hareket ve izleme zaman içindeki değişim ve nesne sürekliliğiyle ilgilenir. Belge çözümleme metin ve düzen ilişkilerini, hizalama ve yeniden oluşturma ise farklı gözlemlerin nasıl birleştirilebileceğini ele alır. ([3], [6])

Her sistemin bu işlerin tümünü yapması gerekmez. Bir deliğin merkezini gereken hassasiyetle bulmak, belirli bir uygulama için yeterli olabilir. Gereken ayrıntı düzeyi, üretilecek çıktının kullanımına bağlıdır. Bir sınıf adı, bir sınır maskesi, fiziksel ölçü veya izlenen yörünge, aynı nesne hakkında farklı sorulara yanıt verebilir; her kullanımda birbirlerinin yerine geçmezler.

~~~text
  YAPILAN ISLER  tek bir tanima isleminden olusmaz  [3] [6]
    siniflandirma     goruntu veya bolge hangi sinifa ait?
    nesne tespiti     aranan sey nerede?
    bolutleme         hangi goruntu noktalari hangi nesneye veya
                      bolgeye ait?
    geometrik         bicim . uzaklik . durus
    cikarim
    hareket ve        zaman icindeki degisim . nesne surekliligi
    izleme
    belge             metin ve duzen iliskileri
    cozumleme
    hizalama ve       farkli gozlemler nasil birlestirilebilir?
    yeniden olusturma

          sinif               tespit                 bolutleme
      +----------+        +----------+           +----------+
      |    __    |        |  +----+  |           |    ##    |
      |   /  \   |        |  | /\ |  |           |   ####   |
      |   \__/   |        |  +----+  |           |    ##    |
      +----------+        +----------+           +----------+
       hangi sinif?          nerede?            hangi noktalar?

    her sistemin bu islerin tumunu yapmasi gerekmez; gereken ayrinti
    duzeyi ciktinin kullanimina baglidir
    sinif adi . sinir maskesi . fiziksel olcu . izlenen yorunge:  ayni
    nesne hakkinda farkli sorulara yanit; her kullanimda birbirinin
    yerine gecmez
~~~

*Çizim 8 — Usül: yapılan işler ve ürettikleri sonuçlar.*

#### Gözlemden sınanmış kullanıma

Usul, önce görsel soruyu kullanım ihtiyacıyla ilişkilendirir. Aranan nesnenin veya olayın ne olduğu, hangi ayrımların önemli sayıldığı ve hataların neye yol açtığı açıklığa kavuşturulur. “Kusur bulmak” ifadesi, hangi kusurların ve hangi büyüklüklerin önemli olduğu belirlenmeden yeterince açık bir mühendislik hedefi oluşturmaz.

Sonraki ilişki, gerekli bilginin gözlemde bulunup bulunmadığıdır. Işık, odak, pozlama, çözünürlük ve bakış açısı, yöntem seçimi kadar etkili olabilir. Pozlama süresini artırmak daha çok ışık toplarken hareket bulanıklığını artırabilir ve kare hızını sınırlayabilir. Kazancı artırmak görüntüyü aydınlatırken gürültüyü de yükseltebilir. Görüntünün iyileştirilmesi, ihtiyaç duyulan bilginin daha iyi elde edilmesi açısından değerlendirilir. ([7])

Yöntem, problemin yapısına göre seçilir. Bazı görevlerde eşikleme veya geometrik hesap yeterlidir; bazılarında öğrenilmiş temsiller veya fiziksel modellerle öğrenmenin birleşimi gerekir. Daha karmaşık yöntem, ek doğrulukla birlikte hesaplama, veri ihtiyacı ve bakım yükü getirebilir. Yeterlilik, gereken sonucun tanımlanan koşul ve kaynak sınırları içinde sağlanmasıyla ilişkilidir.

~~~text
  SORU  kullanim ihtiyaciyla iliskilendirilir
    aranan nesne veya olay ne? . hangi ayrimlar onemli? . hatalar
    neye yol acar?
    "Kusur bulmak"  -/->  yeterince acik bir muhendislik hedefi
                          (hangi kusurlarin ve buyukluklerin onemli
                          oldugu belirlenmeden)

  GEREKLI BILGI GOZLEMDE VAR MI?  [7]
    isik . odak . pozlama . cozunurluk . bakis acisi:  yontem secimi
    kadar etkili olabilir
    pozlama suresi artar  -->  daha cok isik
                          -->  hareket bulanikligi artabilir
                          -->  kare hizi sinirlanabilir
    kazanc artar          -->  goruntu aydinlanir
                          -->  gurultu de yukselebilir
    iyilestirme:  ihtiyac duyulan bilginin daha iyi elde edilmesi
    acisindan degerlendirilir

  YONTEM  problemin yapisina gore
    bazi gorevlerde   esikleme veya geometrik hesap yeterli
    bazilarinda       ogrenilmis temsiller | fiziksel modeller + ogrenme
    daha karmasik yontem:  ek dogruluk + hesaplama, veri ihtiyaci,
    bakim yuku
    yeterlilik:  gereken sonuc, tanimlanan kosul ve kaynak sinirlari
    icinde
~~~

*Çizim 9 — Usül: sorudan gözleme; gözlemin koşulları; yöntem seçimi.*

Öğrenilen sistemin eğitim örneklerinde başarılı olması, yeni örneklerde de başarılı olacağını tek başına göstermez. Genelleme bu ilişkinin eğitim dışındaki örneklerde sürüp sürmediğini araştırır. Bir videonun çok benzer komşu karelerini eğitim ve test bölümlerine dağıtmak, yeni ortamda karşılaşılacak değişimi yeterince sınamayabilir. Farklı günler, üretim partileri veya kameralar, kullanım sorusuna göre daha anlamlı ayrımlar sağlayabilir. Etiketlerin tutarlılığı ve sınıf tanımlarının açıklığı da değerlendirmenin parçasıdır. ([8])

Yanlış sonuçların nedenleri ayrılmalıdır. Gerekli ayrıntı hiç kaydedilmemiş olabilir; etiket tutarsız olabilir; model yanlış çıkarım yapmış olabilir; doğru çıktı yanlış nesneye bağlanmış veya geç iletilmiş olabilir. Bu ayrım, düzeltmeyi doğru yerde yapmayı sağlar. Modelin yüksek güven puanı üretmesi de puanın gerçek doğruluk olasılığına karşılık geldiğini garanti etmez; güven puanlarının gözlenen doğrulukla uyumu ayrıca değerlendirilir. ([9])

~~~text
  GENELLEME  [8]
    egitim orneklerinde basari  -/->  yeni orneklerde basari
    E egitim, T test
    video kareleri           1  2  3  4  5  6  7  8  9  10 ...
    komsu kareler dagitilir  E  T  E  E  T  E  T  E  E  T
      -->  cok benzer kareler iki bolumde; yeni ortamdaki degisim
           yeterince sinanmayabilir
    gunlere gore ayrim       [ gun 1: E ]  [ gun 2: T ]
    farkli gunler, uretim partileri veya kameralar  -->  kullanim
    sorusuna gore daha anlamli ayrim
    etiket tutarliligi ve sinif tanimlarinin acikligi da
    degerlendirmenin parcasi

  YANLIS SONUCUN NEDENLERI  ayrilir; duzeltme dogru yere yapilir
    edinim           gerekli ayrinti hic kaydedilmemis
    veri veya tanim  etiket tutarsiz
    cikarim          model yanlis cikarim yapmis
    baglanti         dogru cikti yanlis nesneye baglanmis
    zamanlama        dogru cikti gec iletilmis

  GUVEN PUANI  [9]
    yuksek guven puani  -/->  gercek dogruluk olasiligi
    puanlarin gozlenen dogrulukla uyumu ayrica degerlendirilir
~~~

*Çizim 10 — Usül: genelleme; yanlış sonucun nedenleri; güven puanı.*

Kullanımda veri akışı, çıktı biçimi, model sürümü, gecikme ve kullanıcıyla etkileşim birlikte çalışır. Kurulum sırasında gösterilen başarının kullanımda korunup korunmadığını anlamak gerekir. Üretim sistemlerine ilişkin değerlendirmeler bu nedenle modelin yanında veri, altyapı, test ve izlemeyi de ele alır. Sürdürme sorumluluğu sürekli model değiştirmek değil, değişikliğin gerekip gerekmediğini anlayabilmektir. ([10])

#### Usulü taşıyanlar ve sınırlar

Usulü insanlar kurabilir, değiştirebilir ve sınayabilir; teknik sistem ise işlemleri gerçekleştirebilir. Otomatik sistemde her tekil sonucun insan tarafından önceden belirlenmesi gerekmez. Bununla birlikte işlemi yapmak ile işlemin hangi amaç ve koşullarda uygun olduğunu gerekçelendirmek farklı sorumluluklardır. Usulü taşımak, algoritmanın yürütülmesini ve geçerliliğinin araştırılmasını birlikte kapsar.

Varsayımsal bir çatlak ayırma sisteminde önce çatlakların gözlenebilirliği belirlenir; çizik, yansıma ve çatlak ayrımları açıklanır; çıktı doğru parçayla eşleştirilir ve kararın ayırma noktasına zamanında ulaşması sağlanır. Kaçan kusurlar ve gereksiz ayrılan sağlam parçalar birlikte değerlendirilir. Böylece görsel çıktı, daha geniş işin içindeki yeriyle sınanır.

Bu usul, bir gösterinin başarısını bütün koşullara genellemek, her sorunu daha büyük modelle çözmek veya tek ortalama puanı bütün hata türlerinin yerine koymak değildir. Her durumda otomatik karar vermek de zorunlu değildir. Yetersiz gözlemde yeniden görüntü almak veya inceleme istemek uygun olabilir. Bazen ilerleme daha iyi yorumlayan yöntemden, bazen daha iyi gözlem sağlayan düzenden gelir.

~~~text
  VARSAYIMSAL CATLAK AYIRMA SISTEMI
    catlaklar gozlenebilir mi?
        |
        v
    cizik . yansima . catlak ayrimlari aciklanir
        |
        v
    cikti dogru parcayla eslestirilir
        |
        v
    karar ayirma noktasina zamaninda ulasir
    birlikte degerlendirilir:  kacan kusurlar + gereksiz ayrilan
    saglam parcalar

  USULU TASIYANLAR
    insanlar         usulu kurar, degistirir, sinar
    teknik sistem    islemleri gerceklestirir
    islemi yapmak  =/=  islemin hangi amac ve kosullarda uygun
                        oldugunu gerekcelendirmek

  NE DEGILDIR
    x  bir gosterinin basarisini butun kosullara genellemek
    x  her sorunu daha buyuk modelle cozmek
    x  tek ortalama puani butun hata turlerinin yerine koymak
    her durumda otomatik karar vermek zorunlu degil
    yetersiz gozlemde:  yeniden goruntu almak veya inceleme istemek
    uygun olabilir
~~~

*Çizim 11 — Usül: varsayımsal çatlak ayırma sistemi; usulü taşıyanlar; usulün ne olmadığı.*

### Amaç ve girdi

Görsel sorunun hangi işlemlerle ele alınacağını ve çıkarılan sonucun nasıl sınanacağını izlenebilir bir yöntem hâlinde açıklamak.

**Girdi:** Varlık ve Mekan kayıtları; mevcut kaynak, veri, model veya araç bilgisi; varsa daha önce yapılmış değerlendirmeler.

### Masaüstü uygulaması

1. Görevi ve gerekli çıktı biçimini yazın. Girdi, işlem, çıktı ve kullanım arasındaki geçişleri kısa bir paragrafla açıklayın.
2. Gerekli bilginin görüntüde bulunup bulunmadığını değerlendirin. Veri varsa ilgili örneği inceleyin; veri yoksa hangi gözlemin gerekli olduğunu ve neyin henüz sınanmadığını kaydedin.
3. Uygun yöntem seçimini gerekçelendirin. Görüntü işleme, geometri, öğrenme veya bunların birleşimini yalnız görevin ihtiyacı bakımından karşılaştırın.
4. Sonucun hangi karşılaştırma, referans veya ölçümle değerlendirileceğini yazın. Teknik deneme yapılıyorsa beklenen ve gözlenen sonuçları ayrı kaydedin; tasarım aşamasında planı belirtin.
5. Hata kaynaklarını edinim, veri veya tanım, çıkarım, bağlantı ve zamanlama bakımından ayırın. Belirsiz durumda uygulanacak davranışı ve kullanım sırasında izlenecek işaretleri açıklayın.

### Oluşturulacak çıktı

Görev, girdi, yöntem, çıktı, değerlendirme ve hata incelemesini birbirine bağlayan Usül kaydı.

### Tamamlanma ve yeniden açma

**Tamamlanma:** Başka bir okuyucu yöntemin mantığını izleyebiliyor ve planlanmış işlemlerle gerçekten yapılmış işlemleri ayırabiliyorsa kayıt tamamlanmıştır. Teknik başarı iddiası varsa destekleyen değerlendirme de kaydedilmiştir.

**Yeniden açma:** Bilgi gözlemde yoksa Mekan'a; görev veya çıktı değişiyorsa Varlık'a dönün. Yeni hata bulgusu yöntemi etkiliyorsa Usül kaydını güncelleyin.

## 4 Zaman Protokolü

### Kayıtlı sorular

> Hangi andadır? Bu anı, diğer zamanlardan farklı yapan nelerdir? Neler değildir?

### Kavramsal açıklama

#### Tarihsel an

Zaman, alanın tarihsel evresi, gözlemin işe yaradığı süre ve sistemin yaşam döngüsü olarak üç düzeyde ele alınır. Söyleşideki güncel değerlendirme 31 Ekim 2026 bağlamına aittir. Bu değerlendirmede görsel yeteneklerin geniş modellerde birleşmesi, görünün dille ilişkilendirilmesi ve robotik eylemle bütünleşmesi öne çıkan yönelimler olarak yorumlanmıştır.

2012 tarihli AlexNet çalışması, büyük bir görüntü kümesi üzerinde öğrenilen derin bir ağın sınıflandırma başarısına ilişkin önemli bir örnektir. 2021 tarihli CLIP çalışması, görüntüler ile doğal dil arasındaki ilişkilerden öğrenilen temsilleri, önceden sabitlenmiş sınıfların ötesindeki kullanımlarla ilişkilendirmiştir. Bu iki örnek bütün alan tarihini temsil etmez; öğrenilmiş görsel özellikler ve dil bağlantısı bakımından belirgin dönüm noktalarını gösterir. ([11], [12])

Meta'nın Kasım 2025 tarihli SAM 3 yayını, metin veya görsel örnekle belirtilen kavramlar için görüntü ve videoda tespit, bölütleme ve izlemeyi ortak modelde ele alır. Google DeepMind'ın Temmuz 2026 tarihli Gemini Robotics 2 duyurusu ise görsel ve dilsel girdileri robot hareketleriyle ilişkilendiren modelleri anlatır; bazı hareket ve el becerisi görevlerinin zor olduğunu da belirtir. Bunlar yayımlayan kuruluşların araştırma ve duyuru örnekleridir. ([13], [14])

Bu örneklerden yapılan yorum, görsel yeteneklere erişim genişlerken belirli bir ortamda onlara ne ölçüde güvenilebileceğini gösterme işinin önemini koruduğudur. Mühendislik, bir yeteneği sıfırdan kurma sorusuyla birlikte hazır bir yeteneği uyarlama, sınama ve sisteme bağlama sorusunu da taşır. Bu değişim geometrinin, görüntü oluşumunun veya basit yöntemlerin geçersizleştiği anlamına gelmez.

~~~text
  UC DUZEY
    alanin tarihsel evresi . gozlemin ise yaradigi sure . sistemin
    yasam dongusu

  METINDEKI TARIHLER  aralar olcekli degil
    2012           o  AlexNet: buyuk bir goruntu kumesinde ogrenilen
                   |  derin ag; siniflandirma basarisi
    2021           o  CLIP: goruntuler ile dogal dil arasindaki
                   |  iliskilerden ogrenilen temsiller
    Kasim 2025     o  SAM 3 (Meta): goruntu ve videoda tespit,
                   |  bolutleme ve izleme ortak modelde
    Temmuz 2026    o  Gemini Robotics 2 (Google DeepMind): gorsel ve
                   |  dilsel girdi ile robot hareketleri
    31 Ekim 2026   o  soylesideki guncel degerlendirme; one cikan
                      yonelimler: genis modellerde birlesme . dille
                      iliskilendirme . robotik eylemle butunlesme
    AlexNet ve CLIP butun alan tarihini temsil etmez
    SAM 3 ve Gemini Robotics 2:  yayimlayan kuruluslarin arastirma ve
    duyuru ornekleri

  YORUM
    gorsel yeteneklere erisim genisler  -->  belirli bir ortamda
    onlara ne olcude guvenilebilecegini gostermek onemini korur
    sifirdan kurmak  +  hazir yetenegi uyarlamak, sinamak, sisteme
    baglamak
    -/->  geometri, goruntu olusumu veya basit yontemler gecersiz
~~~

*Çizim 12 — Zaman: üç düzey; metindeki tarihler; yorum.*

#### Gözlem ile kullanım arasındaki süre

Görüntünün alındığı an, hesaplamanın bittiği an ve sonucun kullanıldığı an birbirinden ayrılır. Hareketli bir ortamda geçmiş konumu doğru tahmin etmek, şimdiki konuma müdahale için yeterli olmayabilir. Zaman bu nedenle yalnız hesaplama hızıyla değil, bilginin kullanılabilirliğiyle ilgilidir.

Üretim hattında kamera ile ayırma noktası arasındaki mesafe ve hattın hızı, kararın yetişeceği süreyi sınırlar. Görüntü aktarımı, hesaplama ve mekanizmanın tepki süresi aynı zaman bütçesini paylaşır. Çok sayıda görüntünün işlenmesi, sonuçların uzun bir kuyruktan sonra gelmesi durumunda tek başına yeterli değildir.

Bir arşivdeki belgeleri çözümleyen sistemin zaman ihtiyacı ise farklıdır. Saatler süren işlem kendi görevi için uygun olabilir. Zamanında bilgi, her durumda en hızlı üretilen bilgi değil, ihtiyaç duyulan zaman aralığında kullanılabilen bilgidir. Gerçek zamanlılık bütün görü sistemlerinin zorunlu kimlik koşulu değildir.

#### Geçmişi taşıma ve geçerliliği sürdürme

Teknik sistem, geçmişte elde edilmiş bilgi ve verilerden yararlanarak yeni gözlemi işler. Hareketli görüntülerde zaman içindeki ilişkiyi kullanabilir; sistemin dayandığı yöntemler de önceki araştırma ve mühendislik birikiminin sonuçlarını taşır. Bu geçmiş, yeni koşullarda aynı başarının otomatik olarak süreceğini göstermez.

Yeni ürünler, kamera ayarları veya kullanım biçimleri önceki değerlendirmenin kapsamını aşabilir. Sorulması gereken, sistemin yaşı kadar, geçerliliğini destekleyen kanıtların bugünkü kullanımı kapsayıp kapsamadığıdır. NIST'in AI RMF çerçevesi kullanım ortamına benzer koşullarda değerlendirmeyi, genelleme sınırlarının belirtilmesini ve kullanım sırasında izlemeyi birlikte ele alır. ([15])

Alan, görmenin tamamen çözülmüş olduğu bir son noktada değildir. Bütün görevler aynı olgunlukta bulunmaz ve tarihsel ilerleme önceki yöntemlerin topluca silinmesiyle gerçekleşmez. Bir kez yüksek puan almak süresiz yeterlilik sağlamaz; buna karşılık koşulları değişmeyen bir sistemin sürekli yeniden eğitilmesi de gerekmez. Süreklilik, neyin ne zaman yeniden değerlendirilmesi gerektiğini anlayabilmeyi kapsar.

~~~text
  UC AN  birbirinden ayrilir
    goruntunun alindigi an . hesaplamanin bittigi an . sonucun
    kullanildigi an
    hareketli ortamda gecmis konumu dogru tahmin etmek, simdiki
    konuma mudahale icin yetmeyebilir

  URETIM HATTINDA ZAMAN BUTCESI
    kamera                               ayirma noktasi
     [o] ======= mesafe, hattin hizi =======>  [X]
      |<------ kararin yetisecegi sure -------->|
      |<- goruntu ->|<- hesaplama ->|<- tepki ->|
          aktarimi                      suresi
    goruntu aktarimi, hesaplama ve mekanizmanin tepki suresi ayni
    zaman butcesini paylasir
    cok sayida goruntu islemek:  sonuclar uzun bir kuyruktan sonra
    geliyorsa tek basina yetmez

  ARSIV
    saatler suren islem kendi gorevi icin uygun olabilir
    zamaninda bilgi:  en hizli uretilen degil, ihtiyac duyulan zaman
    araliginda kullanilabilen bilgi
    gercek zamanlilik  =/=  butun goru sistemlerinin zorunlu kimlik
                            kosulu

  GECERLILIK
    yeni urunler . kamera ayarlari . kullanim bicimleri  -->
    onceki degerlendirmenin kapsamini asabilir
    NIST AI RMF [15]:  kullanim ortamina benzer kosullarda
    degerlendirme . genelleme sinirlari . kullanim sirasinda izleme
    bir kez yuksek puan  -/->  suresiz yeterlilik
    kosullari degismeyen sistem  -/->  surekli yeniden egitim
~~~

*Çizim 13 — Zaman: üç an; üretim hattında zaman bütçesi; arşiv; geçerlilik.*

### Amaç ve girdi

Açıklamanın hangi tarihsel bağlama ait olduğunu, bilginin ne zaman kullanılabilir olduğunu ve geçerliliğinin hangi değişikliklerde yeniden inceleneceğini belirlemek.

**Girdi:** Önceki kayıtlar; kaynakların tarihleri; varsa görüntü zamanları, işlem süreleri, kullanım anı ve değişiklik geçmişi.

### Masaüstü uygulaması

1. Tarihsel değerlendirmeyi hangi tarih itibarıyla yaptığınızı yazın. Kaynak yayım tarihi ile anlattığı olayın tarihini ayırın; yeni bilgi gerekiyorsa kullanılan kaynağı ve kontrol tarihini kaydedin.
2. Gözlem zamanı, hesabın tamamlandığı zaman ve kullanım zamanını birbirinden ayırın. Çalışma kavramsalsa bu ayrımın ele alınan göreve nasıl uygulanacağını açıklayın.
3. Görevin zaman ihtiyacını belirtin. Ölçülmüş bir gecikme yoksa sayı uydurmak yerine gerekli süreyi, varsayımı veya henüz ölçülmediğini yazın. Arşiv çalışmasında çevrimdışı işlemenin uygunluğunu açıklayın.
4. Geçerliliği değiştirebilecek olayları seçin: örneğin yeni veri kaynağı, ürün, ortam, kullanım amacı veya yöntem. Hangi olayda hangi protokolün yeniden açılacağını kaydedin.

### Oluşturulacak çıktı

Tarihsel bağlam, gözlem ve kullanım zamanları, zaman gereksinimi ve yeniden inceleme koşullarından oluşan Zaman kaydı.

### Tamamlanma ve yeniden açma

**Tamamlanma:** Tarihli iddiaların zamanı ve görev için gerekli zaman aralığı anlaşılabiliyorsa; ölçülen süre ile varsayılan süre ayrılmışsa kayıt tamamlanmıştır.

**Yeniden açma:** Yeni bir kaynak tarihsel açıklamayı, yeni bir kullanım zaman gereksinimini veya ortam değişikliği geçerliliği etkilediğinde ilgili protokolle birlikte bu kaydı güncelleyin.

## 5 Gaye Protokolü

### Kayıtlı sorular

> Hangi nihai amaca hizmet eder? Bu nihai amaca ulaştıran nelerdir? Neler değildir?

### Kavramsal açıklama

#### Teknik yönelim ve üst amaç

Bilgisayarlı görü mühendisliğinin ortak teknik yönelimi, görsel gözlemden belirli bir ihtiyaca hizmet edecek ölçüm, temsil veya çıkarım üretmek ve buna ne ölçüde dayanılabileceğini ortaya koymaktır. Bu ortak yönelim, bütün uygulamaların tek bir nihai insani amaca sahip olduğu anlamına gelmez.

Astronomik görüntü çözümlemesi bilimsel bilgiye, belge okuma erişime, kusur tespiti ürün kalitesine, görsel düzenleme yaratıcı üretime hizmet edebilir. Aynı temel yöntemler gözetim gibi başka amaçlara da yöneltilebilir. Alanın teknik kimliği ile kullanım amacının değeri ayrı sorulardır. Teknik olarak başarılı bir sistemin seçilmeye değer bir amaca hizmet ettiği, yalnız başarımından çıkarılamaz.

Üretim hattı örneğinde çatlağın yerini veya ölçüsünü tahmin etmek teknik çıktıdır. Kusurlu ve uygun parçaları belirlenen koşullarda ayırmak sistem işlevidir. Kusurlu ürünün ilerlemesini ve gereksiz ayırmayı azaltmak süreçteki sonuçtur. Güvenilir ürün üretmek ve kaynakları daha iyi kullanmak daha üst amaçlardır. Bu düzeyler arasında bağ kurulmadığında teknik ölçüt, gerçek ihtiyacın yerine geçebilir.

~~~text
  ORTAK TEKNIK YONELIM
    gorsel gozlemden belirli bir ihtiyaca hizmet edecek olcum,
    temsil veya cikarim uretmek; buna ne olcude dayanilabilecegini
    ortaya koymak
    -/->  butun uygulamalarin tek bir nihai insani amaci

  HIZMET EDEBILECEGI AMACLAR
    astronomik goruntu cozumlemesi  -->  bilimsel bilgi
    belge okuma                     -->  erisim
    kusur tespiti                   -->  urun kalitesi
    gorsel duzenleme                -->  yaratici uretim
    ayni temel yontemler gozetim gibi baska amaclara da yoneltilebilir
    teknik kimlik  =/=  kullanim amacinin degeri
    teknik basari  -/->  secilmeye deger bir amaca hizmet

  URETIM HATTI ORNEGINDE DUZEYLER
    teknik cikti        catlagin yerini veya olcusunu tahmin etmek
         |
    sistem islevi       kusurlu ve uygun parcalari belirlenen
         |              kosullarda ayirmak
    surecteki sonuc     kusurlu urunun ilerlemesini ve gereksiz
         |              ayirmayi azaltmak
    daha ust amaclar    guvenilir urun uretmek . kaynaklari daha iyi
                        kullanmak
    bu duzeyler arasinda bag kurulmazsa  -->  teknik olcut gercek
    ihtiyacin yerine gecebilir
~~~

*Çizim 14 — Gaye: ortak teknik yönelim; hizmet edebileceği amaçlar; üretim hattı örneğinde düzeyler.*

#### Gayeye ulaşmayı destekleyen ilişkiler

Amacın açık olması, hangi sonucun iyileştirilmeye çalışıldığını görünür kılar. “Daha iyi görmek” ifadesi, ne için daha iyi olduğu belirlendiğinde mühendislik hedefi olur. Görsel gözlem bu soruyu cevaplayacak kanıtı taşımalı; gerektiğinde görüntüleme düzeni değiştirilmeli veya başka bilgi kaynaklarıyla birlikte kullanılmalıdır.

Başarı ölçütünün gerçek sonuçla bağlantılı olması gerekir. Kusurları kaçırmak, sağlam parçaları ayırmak ve üretimi yavaşlatmak farklı sonuçlardır. Birleşik bir puan kullanılabilir; ancak puanın bu farkları görünmez kılmaması önemlidir. Varsayımsal olarak bin parçanın yalnız biri kusurluysa bütün parçalara sağlam diyen sistem yüzde 99,9 doğruluk elde ederken kusurlu parçayı yakalama başarısı sıfır olur.

Yöntem ihtiyaca uygun seçilir. Daha büyük veya daha yeni model, amaçla daha iyi örtüşmek zorunda değildir. Daha çok veri de tek başına yeterli değildir; verinin geldiği koşullar ve tanımlarının tutarlılığı değeri etkiler. Üretim deneyimine dayanan makine öğrenmesi rehberleri, basit başlangıçlar ve sağlam altyapı ile ölçülebilir ürün hedefleri arasındaki ilişkiyi vurgular. ([16])

Belirsizlik, kullanım davranışına bağlanır. Yetersiz gözlemde yeni görüntü almak, incelemeye yönlendirmek veya kararı ertelemek uygun olabilir. Sonucun kullanımda değerlendirilmesi de gereklidir. Üretilen bilgi gerçekten işe yarıyor mu, iş yükünü azaltıyor mu, kararı iyileştiriyor mu soruları uygulamanın amacına göre yanıtlanır. Bu ilişkiler tek tek başarı garantisi değil, başarı iddiasının dayanaklarıdır.

~~~text
  BIN PARCADA BIR KUSUR  varsayimsal;  o saglam, x kusurlu
    o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o . . .
    o o o o o o o o o o o o o x o o o o o o o o o o o o o o o o . . .
                              ^
                              tek kusurlu parca
    butun parcalara saglam diyen sistem
      dogruluk                       yuzde 99,9
      kusurlu parcayi yakalama       sifir

  FARKLI SONUCLAR  birlesik puan bunlari gorunmez kilmamali
    kusurlari kacirmak . saglam parcalari ayirmak . uretimi
    yavaslatmak

  BELIRSIZLIK  kullanim davranisina baglanir
    yetersiz gozlem  -->  yeni goruntu almak | incelemeye yonlendirmek
                          | karari ertelemek
    kullanimdaki sorular:  bilgi ise yariyor mu? . is yukunu
    azaltiyor mu? . karari iyilestiriyor mu?
    daha buyuk veya yeni model  -/->  amacla daha iyi ortusme
    daha cok veri  -/->  tek basina yeterlilik
~~~

*Çizim 15 — Gaye: bin parçada bir kusur; farklı sonuçlar; belirsizlik.*

#### Gayeyi taşıyan özne ve sistem

Gaye, sisteme yalnız son aşamada eklenen bir kullanım etiketi değildir. Neyin görüntülendiği, hangi ayrımların öğretildiği, neyin hata sayıldığı, hangi sonucun yeterli bulunduğu ve çıktıyla ne yapıldığı, gayenin tasarım ve davranışta nasıl taşındığını gösterir. Aynı görüntüde nesne saymak, konum bulmak ve yazı okumak farklı amaçlar oluşturur; gerekli temsil ve değerlendirme de değişir.

Teknik sistem, hedefi tasarımında ve davranışında taşıyabilir. Bir hedefi izlemesi, o hedefin neden seçilmeye değer olduğunu kendiliğinden gerekçelendirmez. Bu gerekçe, sistemi kuran ve kullanan insanların ve kurumların kararlarıyla ilişkilidir. İnsanların bütünün içinde bulunması her kareyi bir insanın onaylamasını gerektirmez; katkıları amaç seçimi, tasarım, sınama ve sürdürmede de bulunabilir.

Taşıyıcı makine sorusuna verilen yorumda bütün, insanların, araçların ve çalışma ortamının belirli bir amaç çevresinde kurduğu ilişkidir. Bilgisayarlı görü mühendisi bu ilişkide hangi gözlemden hangi sonuca, hangi yöntemle, hangi zaman içinde ve ne için gidildiğini açık tutma sorumluluğunu üstlenir. Bu yorum, makineye kendiliğinden niyet veya kişilik atfetmez.

#### Nihai amacın yerine geçmeyenler

Yüksek doğruluk oranı, büyük model, çok veri ve tam otomasyon nihai amacın yerine geçirilmez. Bazı uygulamalarda insanın kararını destekleyen düzen, otomatik karardan daha uygun olabilir. Bazılarında otomasyon ihtiyacı karşılar. Seçim, teknik olarak mümkün olan kadar hangi düzenin amaca daha iyi hizmet ettiğine bağlıdır.

İnsana benzemek veya her şeyi görünür kılmak da kendiliğinden nihai amaç değildir. Bir sistem belirli bir ölçümü tutarlı biçimde gerçekleştirebilir; genel bir insan görsel deneyimine sahip olması gerekmez. Hangi bilginin üretileceği ve bunun ne için kullanılacağı amaç tanımının parçasıdır. Görü mühendisliği, neyin bilinebileceğini, bu bilgiye hangi koşullarda dayanılabileceğini ve onunla ne yapmaya değer bulunduğunu birlikte düşünmeyi gerektirir.

~~~text
  GAYE TASARIMDA VE DAVRANISTA TASINIR
    neyin goruntulendigi . hangi ayrimlarin ogretildigi . neyin hata
    sayildigi . hangi sonucun yeterli bulundugu . ciktiyla ne yapildigi
    ayni goruntude:  nesne saymak | konum bulmak | yazi okumak
                     -->  farkli amaclar; farkli temsil ve
                          degerlendirme

  TEKNIK SISTEM VE INSAN
    sistem bir hedefi izleyebilir  -/->  hedefin neden secilmeye
                                         deger oldugunun gerekcesi
    gerekce:  sistemi kuran ve kullanan insanlarin ve kurumlarin
              kararlari
    her kareyi bir insanin onaylamasi gerekmez; katkilar:  amac
    secimi . tasarim . sinama . surdurme
    muhendis:  hangi gozlemden hangi sonuca, hangi yontemle, hangi
    zaman icinde ve ne icin gidildigini acik tutar
    yorum  -/->  makineye niyet veya kisilik atfetmek

  NIHAI AMACIN YERINE GECIRILMEZ
    yuksek dogruluk orani . buyuk model . cok veri . tam otomasyon
  KENDILIGINDEN NIHAI AMAC DEGIL
    insana benzemek . her seyi gorunur kilmak
    bazi uygulamalarda insanin kararini destekleyen duzen, bazilarinda
    otomasyon; secim:  hangi duzen amaca daha iyi hizmet ediyor?
~~~

*Çizim 16 — Gaye: gayenin taşınması; teknik sistem ve insan; nihai amacın yerine geçmeyenler.*

### Amaç ve girdi

Teknik çıktının hangi sistem işlevine ve hangi üst amaca hizmet ettiğini; başarı ölçütünün bu amaçla ilişkisini açıklamak.

**Girdi:** Tohumdaki başlangıç niyeti, 1–4 kayıtları, kullanım ihtiyacı ve varsa gerçek süreç sonuçları.

### Masaüstü uygulaması

1. Teknik çıktıyı, sistem işlevini, süreçte beklenen sonucu ve insani veya kurumsal üst amacı ayrı cümlelerle yazın. Aralarındaki bağı açıklayın.
2. Kimin veya hangi sürecin bu sonuçtan yararlanacağını belirtin. Amacın seçilme gerekçesini teknik bir başarı puanının ötesinde ifade edin.
3. Başarı ölçütünü ve önemli hata türlerini belirleyin. Ölçüt gerçekten amaca hizmet ediyor mu değerlendirin; mevcut sayısal eşik varsa dayanağını, yoksa belirlenmesi gerekeni yazın.
4. Seçilen yöntemin ve otomasyon düzeyinin amaca uygunluğunu açıklayın. Belirsiz durumlarda kullanılacak davranışın Usül kaydıyla tutarlı olduğunu kontrol edin.
5. Beklenen fayda ile gözlenmiş sonucu ayırın. Henüz kullanım sonucu yoksa hangi değerlendirmeyle anlaşılacağını kaydedin; amaç değiştiyse etkilediği önceki kayıtları güncelleyin.

### Oluşturulacak çıktı

Teknik çıktıdan üst amaca uzanan ilişkiyi, başarı ölçütlerini, hata sonuçlarını ve kullanım gerekçesini içeren Gaye kaydı.

### Tamamlanma ve yeniden açma

**Tamamlanma:** Çıktının ne için üretildiği ve başarının hangi amaç bakımından değerlendirileceği açıklanmışsa kayıt tamamlanmıştır. Beklenti, ölçüm ve yorum birbirinden ayrılmıştır.

**Yeniden açma:** Amaç, yararlanacak kişi veya süreç, başarı ölçütü ya da hata sonuçları değiştiğinde Gaye'yi yeniden açın. Gereken görev veya gözlem de değişirse ilgili protokole dönün.

## 6 Kökleşme (Bitiş) Protokolü

### Yürütme soruları

Başlangıç sorusu hangi ölçüde karşılandı? Beş protokol birlikte nasıl bir açıklama oluşturdu? Hangi sonuçlar dayanak kazandı, hangileri yorum veya açık soru olarak kaldı? Bu çalışma ne zaman yeniden ele alınmalıdır?

### Kavramsal açıklama

Kökleşme, Varlık, Mekan, Usül, Zaman ve Gaye protokollerinde oluşan açıklamaları birbirine bağlar. Ayrı ayrı tanımların bulunmasıyla birlikte, bu tanımların aynı konu hakkında tutarlı bir bütün oluşturması ve hangi dayanaklara sahip olduğunun görünür olması gerekir. Ortaya çıkan kavrayış, sınırları ve açık sorularıyla taşınabilir hâle gelir.

Bitiş, bu çalışma turunun tamamlanmasıdır. Kökleşme ise düşüncenin onu taşıyabilecek gerekçe, kaynak, gözlem ve ayrımlar üzerine yerleşmesidir. Bir yorumun yazılmış olması onu kesin bilgiye dönüştürmez. Kapanış, dayanaklı açıklamalar ile yorumların ve henüz cevaplanmamış soruların ayrımını korur.

Gaye Protokolü incelenen alanın veya sistemin neye hizmet ettiğini araştırır. Kökleşme Protokolü ise bu incelemenin sonunda hangi kavrayışın oluştuğunu ve onun nasıl ayakta durduğunu kaydeder. Bu yüzden gaye, inceleme sonucunda ulaşılan kapanışla özdeşleştirilmez; bir amacın açıklanması, uygulamada o amaca ulaşıldığını tek başına göstermez.

Taşıyıcı makine sorusu burada yeniden bütün hâlinde ele alınır. İnsanların kurucu ve değerlendirici rolleri, teknik sistemin işlemleri, gözlemin edinildiği ortam ve sonucun kullanım amacı birlikte açıklanır. Bir parçanın bütüne eşitlenmesi veya teknik çıktıya kendiliğinden niyet ve kişilik yüklenmesi önlenir. Taşıyıcıya ilişkin sonuç, bu çalışmada kullanılan yorum çerçevesi ve dayanaklarıyla birlikte ifade edilir.

Kökleşmiş kayıt, yeniden incelemeyi mümkün kılar. Yeni kaynak, gözlem veya kullanım amacı mevcut açıklamayı etkilediğinde ilgili bölüm açılır. Önceki sonuç silinmeden değişikliğin nedeni belirtilir; böylece hangi fikrin nereden geldiği ve nereye kadar geçerli olduğu korunur.

### Bu söyleşide oluşan sonuç

Bu söyleşide oluşan açıklamada Bilgisayarlı Görü Mühendisliği, görsel gözlemden göreve uygun bilgi veya temsil üreten ve bu sonucun kullanılabilirliğini koşullarıyla birlikte sınayan alan olarak tanımlanmıştır. Alanın kurucu ve değerlendirici özneleri insanlar; teknik işlemleri gerçekleştiren taşıyıcısı görü sistemidir. Bütünün açıklaması, bu insanların araçlarla ve çalışma ortamıyla kurduğu ilişkide aranmıştır. Kamera, model, göz veya tek bir mühendis bütünün yerine geçirilmemiştir. Teknik yönelim ile üst amaç, gözlem ile çıkarım ve tarihsel zaman ile kullanım zamanı ayrımları bu açıklamanın dayanaklarını oluşturur. Taşıyıcıya ilişkin bu sonuç, söyleşide önerilen yorum çerçevesi olarak korunur.

~~~text
  BITIS VE KOKLESME
    bitis       bu calisma turunun tamamlanmasi
    koklesme    dusuncenin gerekce, kaynak, gozlem ve ayrimlar
                uzerine yerlesmesi
    bir yorumun yazilmis olmasi  -/->  kesin bilgi

  SOYLESIDE OLUSAN SONUC  onerilen yorum cercevesi olarak
    tanim        gorsel gozlemden goreve uygun bilgi veya temsil
                 ureten ve bu sonucun kullanilabilirligini
                 kosullariyla birlikte sinayan alan
    kurucu ve    insanlar
    degerlendirici ozneler
    teknik       goru sistemi
    tasiyici
    butun        bu insanlarin araclarla ve calisma ortamiyla
                 kurdugu iliski
    yerine gecirilmez:  kamera . model . goz . tek bir muhendis

  DAYANAK AYRIMLARI
    teknik yonelim     =/=  ust amac
    gozlem             =/=  cikarim
    tarihsel zaman     =/=  kullanim zamani
~~~

*Çizim 17 — Kökleşme: bitiş ve kökleşme; söyleşide oluşan sonuç; dayanak ayrımları.*

### Amaç ve girdi

Başlangıç sorusuna verilen karşılığı, beş protokolün bütünlüğünü ve kalan açıklıklarını sürümlenmiş bir sonuç kaydında birleştirmek.

**Girdi:** Tohum kaydı, 1–5 arasındaki çalışma kayıtları, dayanaklar, varsa gerçek deneme sonuçları ve açık sorular.

### Masaüstü uygulaması

1. Tohum kaydını yeniden okuyun. Başlangıç sorusunun karşılanan kısmını, değişen kısmını ve karşılanmayan kısmını açıkça yazın.
2. Beş protokolü aynı incelenen birim bakımından karşılaştırın. Varlık'ta tanımlanan şeyin mekân, usul, zaman ve gaye kayıtlarında değişip değişmediğini kontrol edin; değişmişse nedenini açıklayın veya ilgili kaydı düzeltin.
3. Taşıyıcıyı bir sonuç paragrafında açıklayın: neye ilişkin, hangi ortamda, hangi yöntemle, hangi zaman içinde ve ne için çalışan hangi insan ve teknik sistem ilişkisi ortaya çıktı? “Kimdir?” ve “Kim değildir?” sınırlarını bu paragrafın ardından belirtin.
4. Önemli sonuçları dayanaklarıyla eşleştirin. Kaynak veya gözlemle desteklenen açıklamaları, yorumları, varsayımları ve yapılmamış değerlendirmeleri ayırın.
5. Çelişkileri ilgili protokole dönerek çözün veya açık soru olarak etkisiyle birlikte kaydedin. Yeni bilgi geldiğinde hangi bölümün yeniden açılacağını belirtin.
6. Kapanış paragrafını yazın. Çalışma turunu “Tamamlandı” ya da “Açık sorularla tamamlandı” olarak kaydedin; tarih, sürüm ve değişiklik kaydını güncelleyip `.md` dosyasını kaydedin.

### Oluşturulacak çıktı

Başlangıç sorusuna karşılık veren bütünlüklü sonuç, taşıyıcı açıklaması, dayanaklar, açık sorular, yeniden inceleme koşulları ve sürümlenmiş çalışma dosyasından oluşan Kökleşme kaydı.

### Tamamlanma ve yeniden açma

**Tamamlanma:** Okuyucu neyin açıklandığını, açıklamanın neye dayandığını ve nerede sınırlı kaldığını anlayabiliyorsa çalışma turu kapatılabilir. Başlangıçtaki beklenen çıktı ile kapanış durumu uyumludur; çözülmeyen çelişkiler ve yapılmamış değerlendirmeler görünürdür.

**Yeniden açma:** Yeni kanıt, farklı ortam, değişen yöntem, zaman gereksinimi veya amaç sonucu etkilediğinde ilgili protokolü yeniden açın. Başlangıç sorusu veya kapsam değişiyorsa Tohum'u da güncelleyin.

## Çalışma Kaydı

Bu bölüm, protokollerin her yeni uygulamasında doldurulacak kayıt şablonudur. Boş alanlara o çalışma sırasında elde edilen bilgileri yazın. Bir alan uygulanmıyorsa gerekçesini; henüz bilinmiyorsa açık soruyu ve sonuca etkisini belirtin. Protokol metnini tamamlamak ile belirli bir uygulamayı yürütüp kaydını tamamlamak ayrı işlemlerdir.

### Çalışma Bilgisi

- Çalışma adı:
- Uygulayan kişi veya ekip:
- Başlangıç tarihi:
- Çalışma türü: Kavramsal inceleme / Teknik tasarım / Teknik deneme
- İncelenen birim:
- Kullanılan protokol sürümü: 1.0
- Çalışma kaydının sürümü: 1.0
- Çalışmanın durumu: Başlanmadı
- Çalışma dosyasının adı:

### İlerleme

- [ ] 0 Tohum kaydı oluşturuldu.
- [ ] 1 Varlık kaydı oluşturuldu.
- [ ] 2 Mekan kaydı oluşturuldu.
- [ ] 3 Usül kaydı oluşturuldu.
- [ ] 4 Zaman kaydı oluşturuldu.
- [ ] 5 Gaye kaydı oluşturuldu.
- [ ] 6 Kökleşme kaydı ve kapanış tamamlandı.

### 0 Tohum (Başlangıç) Protokolü Uygulama Kaydı

- Başlangıç sorusu:
- Bu turu başlatma gerekçesi:
- İncelenecek birim:
- Kapsama dâhil olanlar:
- Kapsam dışında kalanlar:
- Girdiler ve erişim yerleri:
- Bilinen açıklamalar:
- Çalışma varsayımları:
- Başlangıçta açık sorular:
- Bu turdan beklenen çıktı:

### 1 Varlık Protokolü Uygulama Kaydı

- Çalışma tanımı:
- Gözlenen şey ve gözlem verisi:
- Üretilen temsil veya çıkarım:
- Sonucun kullanımı:
- Ayırt edici ilişkiler:
- Taşıyıcı kişiler ve teknik bileşenler:
- Kapsam dışı olanlar:
- Parça olup bütünü açıklamayanlar:

### 2 Mekan Protokolü Uygulama Kaydı

- Gözlemin edinildiği ortam:
- Hesaplama ortamı:
- Kullanım bağlamı:
- Bileşenler arasındaki bağlantılar:
- İlgili koordinat, birim ve kimlik bilgileri:
- Sonucu etkileyen ortam koşulları:
- Geçerlilik sınırları:
- Bilinmeyen ortam koşulları:

### 3 Usül Protokolü Uygulama Kaydı

- Görev ve çıktı biçimi:
- Girdiden kullanıma işlem açıklaması:
- Gözlemin yeterliliği:
- Seçilen yöntem ve gerekçesi:
- Değerlendirme planı:
- Gerçekten yapılan işlemler ve sonuçlar:
- Hata kaynakları:
- Belirsiz durumda davranış:
- Kullanımda izlenecek işaretler:

### 4 Zaman Protokolü Uygulama Kaydı

- Değerlendirmenin esas tarihi:
- Kaynak ve olay tarihleri:
- Gözlem zamanı:
- Hesabın tamamlandığı zaman:
- Kullanım zamanı:
- Zaman gereksinimi ve dayanağı:
- Ölçülen ve varsayılan süreler:
- Yeniden inceleme gerektiren olaylar:

### 5 Gaye Protokolü Uygulama Kaydı

- Teknik çıktı:
- Sistem işlevi:
- Süreçte beklenen sonuç:
- İnsani veya kurumsal üst amaç:
- Yararlanacak kişi veya süreç:
- Amacın seçilme gerekçesi:
- Başarı ölçütü ve dayanağı:
- Önemli hata türleri ve sonuçları:
- Yöntem ve otomasyon düzeyinin uygunluğu:
- Beklenen fayda ve gözlenmiş sonuç:

### 6 Kökleşme (Bitiş) Protokolü Uygulama Kaydı

- Başlangıç sorusuna verilen karşılık:
- Beş protokolü bağlayan sonuç paragrafı:
- Taşıyıcı makine kimdir:
- Taşıyıcı makine kim değildir:
- Dayanaklı sonuçlar ve bağlantıları:
- Yorumlar ve çalışma varsayımları:
- Açık sorular ve sonuca etkileri:
- Yapılmamış değerlendirmeler:
- Yeniden inceleme koşulları:
- Kapanış durumu:
- Kapanış tarihi ve sürümü:

### Dayanak ve açık soru kaydı

Her önemli sonuç veya açık soru için aşağıdaki kaydı çoğaltın. Kaynak bağlantısını, ilgili dosya ve konumu ya da gözlemin tarihini sonradan bulunabilecek biçimde belirtin.

- İlgili protokol ve ifade:
- Niteliği: Kaynak bilgisi / Doğrudan gözlem / Yorum / Varsayım / Açık soru
- Dayanak veya eksik bilgi:
- Kaynak dosya bağlantı veya konum:
- Kaynak tarihi ve varsa kontrol tarihi:
- Sonuca etkisi:
- İzleyen işlem ve varsa sorumlu kişi:

### Değişiklik Kaydı

Çalışma sırasında soru, kapsam veya sonuç değişirse aşağıdaki kaydı çoğaltın. Önceki biçim ile yeni biçim arasındaki farkı ve nedenini koruyun.

- Değişiklik tarihi ve çalışma sürümü:
- Etkilenen protokol:
- Önceki ifade veya karar:
- Yeni ifade veya karar:
- Değişiklik gerekçesi ve dayanağı:
- Yeniden incelenecek diğer protokoller:

## Kaynaklar

Aşağıdaki kaynaklar mevcut kavramsal yanıtların teknik ve tarihsel dayanaklarıdır. Yeni bir çalışmada eklenen kaynakları, tarihleriyle birlikte Çalışma Kaydı'na ekleyin. Tarihsel model örnekleri Zaman Protokolü'nde belirtilen 31 Ekim 2026 bağlamında korunmuştur.

1. Torralba, Isola ve Freeman. Foundations of Computer Vision: The Challenge of Vision (https://visionbook.mit.edu/taxonomy.html).

2. Torralba, Isola ve Freeman. Foundations of Computer Vision: Imaging (https://visionbook.mit.edu/imaging.html).

3. Torralba, Isola ve Freeman. Foundations of Computer Vision: Understanding Geometry (https://visionbook.mit.edu/part_understanding_geometry.html).

4. OpenCV. Camera Calibration (https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html).

5. Torralba, Isola ve Freeman. Foundations of Computer Vision: Data Bias and Shift (https://visionbook.mit.edu/bias_and_shift.html).

6. Torralba, Isola ve Freeman. Foundations of Computer Vision: Object Recognition (https://visionbook.mit.edu/object_recognition_v3.html).

7. Basler. Optimizing Image Quality (https://docs.baslerweb.com/optimizing-image-quality).

8. Torralba, Isola ve Freeman. Foundations of Computer Vision: The Problem of Generalization (https://visionbook.mit.edu/problem_of_generalization.html).

9. Guo ve diğerleri, 2017. On Calibration of Modern Neural Networks (https://proceedings.mlr.press/v70/guo17a.html).

10. Breck ve diğerleri, 2017. The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction (https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/).

11. Krizhevsky, Sutskever ve Hinton, 2012. ImageNet Classification with Deep Convolutional Neural Networks (https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html).

12. Radford ve diğerleri, 2021. Learning Transferable Visual Models From Natural Language Supervision (https://proceedings.mlr.press/v139/radford21a.html).

13. Meta, 19 Kasım 2025. SAM 3: Segment Anything with Concepts (https://ai.meta.com/research/publications/sam-3-segment-anything-with-concepts/).

14. Google DeepMind, 30 Temmuz 2026. Gemini Robotics 2 brings whole body intelligence to robots (https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/).

15. NIST, 2023. Artificial Intelligence Risk Management Framework (AI RMF 1.0) (https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf).

16. Google for Developers. Rules of Machine Learning (https://developers.google.com/machine-learning/guides/rules-of-ml).

# Makine Öğrenmesi Mühendisliği Protokolleri

**Tohum · Varlık · Mekan · Usül · Zaman · Gaye · Kökleşme**

**Sürüm:** 1.0\
**Tarih:** 31 Ekim 2026\
**Belge durumu:** Kullanıma hazır protokol metni

Bu belge, Makine Öğrenmesi Mühendisliğini varlık, mekân, usul, zaman ve gaye boyutlarında ele alan soru ve yanıtları kaydeder. Tohum Protokolü araştırmanın başlangıcını kurar; Kökleşme Protokolü, oluşan anlayışı dayanakları ve devam koşullarıyla birleştirir. Böylece yedi bölüm, kavramsal açıklama ile masaüstünde uygulanabilir kayıt düzenini birlikte taşır.

Protokol sözcüğü burada, bir konunun tanımını, dayanaklarını, ilişkilerini ve sınırlarını izlenebilir biçimde tutan düşünme ve kayıt düzenini ifade eder. Bir faaliyetin bu alana ait olması ile iyi yapılmış olması birbirinden ayrılır. Güvenilirlik, ölçülebilirlik ve sürdürülebilirlik, her uygulamanın kendiliğinden sahip olduğu özellikler olarak kabul edilmez; mühendisliğin gerçekleştirmeye çalıştığı niteliklerdir.

1–5'in özgün soruları ve taşıyıcı özneye ilişkin ortak soru kullanıcıya aittir. Yanıtların kavramsal çerçevesi, 0 ve 6'nın yönlendirici soruları ve masaüstü uygulama adımları bu çalışmada oluşturulmuştur. Normatif öneriler açıklayıcı tanımlardan ayrılır; kaynak numaraları belgenin sonundaki kayıtlara bağlanır.

Bu belgenin hazır olması, belirli bir gerçek sistem üzerinde protokollerin yürütüldüğü anlamına gelmez. Yeni bir uygulamanın bulguları, kanıtları ve kararları ayrıca çalışma kaydına işlenir.

## Kayıt çerçevesi

> Geçmiş bağlamları buraya taşıma. Burası ile sınırlı kalma.

## Taşıyıcı özneye ilişkin ortak soru

> Makine Öğrenmesi Mühendisliği'nin köken aldığı varlık, mekan, usül, zaman, ve gayeyi taşıyan makine kimdir? Kim değildir?

Taşıyıcının mesleki adı makine öğrenmesi mühendisidir. Daha temel düzeyde taşıyıcı, öğrenilmiş davranışı amaçlı bir sisteme dönüştüren insandır. Fiilî çalışma ölçeğinde faaliyet, insanlar, kurumlar ve teknik araçlar arasında kurulmuş bir örgütlenmeyle gerçekleşir. Bu bütün için makine sözcüğünün kullanılması, bütünün tek bir kişi gibi düşündüğü, istediği veya sorumluluk taşıdığı anlamına gelmez. Bu ayrım, protokollerin taşıyıcı özne açıklamalarında sürdürülür.

~~~text
  BU BELGEDE KIME AIT
    kullaniciya ait           1-5'in ozgun sorulari . tasiyici ozneye
                              iliskin ortak soru
    bu calismada olusturulan  yanitlarin kavramsal cercevesi . 0 ve
                              6'nin yonlendirici sorulari . masaustu
                              uygulama adimlari

  AYRILIR
    bir faaliyetin bu alana ait olmasi  |  iyi yapilmis olmasi
    guvenilirlik, olculebilirlik ve surdurulebilirlik:  kendiliginden
    sahip olunan ozellikler degil, muhendisligin gerceklestirmeye
    calistigi nitelikler

  TASIYICI  uc duzey
    mesleki adi               makine ogrenmesi muhendisi
         |
    daha temel duzeyde        ogrenilmis davranisi amacli bir sisteme
         |                    donusturen insan
         |
    fiili calisma olceginde   insanlar, kurumlar ve teknik araclar
                              arasinda kurulmus bir orgutlenme
    bu butun icin "makine" sozcugu  -/->  butunun tek bir kisi gibi
                                         dusundugu, istedigi veya
                                         sorumluluk tasidigi
~~~

*Çizim 1 — Giriş ve ortak soru: kime ait olan; alana ait olmak ile iyi yapılmış olmak; taşıyıcının üç düzeyi.*

## Masaüstünde çalışma düzeni

Protokoller, bir Markdown editöründe kayıt tutarak veya masaüstü asistanıyla adım adım uygulanabilir. Önce çalışma türünü Kavramsal inceleme veya Gerçek sistem uygulaması olarak belirt. Kavramsal inceleme, tanım ve iddiaları dayanaklarla değerlendirir; gerçek sistem uygulaması ayrıca ilgili kullanım için ölçüm ve uygulama kanıtı gerektirir.

Her protokolün kavramsal açıklamasından sonra Girdi, Uygulama, Tutulacak kayıt, Tamamlanma ölçütü ve Yeniden açma koşulu gelir. Çalışma kaydı, bu belgenin bir çalışma kopyasının sonunda tutulur. Yönergeleri ve kaynak metni değiştirmek yerine bulguları çalışma kaydına işle.

Kayıt durumları Başlanmadı, Çalışılıyor, Açık, Koşullu tamamlandı, Tamamlandı ve Durduruldu olarak kullanılabilir. Çalışılıyor, değerlendirme adımları yürütülürken; Açık, değerlendirme sonucunda çözülmesi veya karara bağlanması gereken mesele bulunduğunda kullanılır. Koşullu tamamlandı, yalnız kapanışı engellemeyen açık meseleler ve koşulları yazıldığında kullanılır. Durduruldu, mevcut çevrime devam etmeme kararını kaydeder. Başlangıç şablonları Başlanmadı durumundadır. Uygulanmayan adımın gerekçesini, henüz yapılmamış deneyin plan durumunu ve bilinmeyen alanın Belirlenmedi olduğunu açıkça kaydet.

0'dan başla, ilk geçişte 1–5'i sırayla işle ve 6'da bütünleştir. Bulgu önceki bir bölümün kabulünü değiştiriyorsa ilgili bölüme dön; etkilenen diğer kayıtları güncelle ve 6'daki sonucu yeniden değerlendir. Her değişiklikte tarih, neden, dayanak ve etkilenen protokolü kaydet. Bu çalışma düzeni, mevcut kavramsal açıklamaların masaüstünde uygulanması için oluşturulmuştur.

**Okuma ve ilk uygulama sırası:** 0 Tohum → 1 Varlık → 2 Mekan → 3 Usül → 4 Zaman → 5 Gaye → 6 Kökleşme. Değişiklikler gerektiğinde ilgili protokole geri dönülerek işlenir.

~~~text
  CALISMA TURU
    Kavramsal inceleme         tanim ve iddialari dayanaklarla
                               degerlendirir
    Gercek sistem uygulamasi   ayrica ilgili kullanim icin olcum ve
                               uygulama kaniti gerektirir

  HER PROTOKOLDE
    kavramsal aciklama  -->  Girdi  -->  Uygulama  -->  Tutulacak kayit
                        -->  Tamamlanma olcutu  -->  Yeniden acma kosulu

  KAYIT DURUMLARI
    Baslanmadi       baslangic sablonlari
    Calisiliyor      degerlendirme adimlari yurutulurken
    Acik             cozulmesi veya karara baglanmasi gereken mesele var
    Kosullu          yalniz kapanisi engellemeyen acik meseleler ve
    tamamlandi       kosullari yazildiginda
    Tamamlandi
    Durduruldu       mevcut cevrime devam etmeme karari
    bilinmeyen alan:  Belirlenmedi

  OKUMA VE ILK UYGULAMA SIRASI
    0 Tohum --> 1 Varlik --> 2 Mekan --> 3 Usul --> 4 Zaman --> 5 Gaye
    --> 6 Koklesme
    bulgu onceki bir bolumun kabulunu degistiriyorsa ilgili bolume
    donulur; diger kayitlar guncellenir; 6'daki sonuc yeniden
    degerlendirilir
    her degisiklikte:  tarih . neden . dayanak . etkilenen protokol
~~~

*Çizim 2 — Masaüstünde çalışma düzeni: çalışma türü; her protokolün bölümleri; kayıt durumları; okuma sırası ve geri dönüş.*

## 0 Tohum (Başlangıç) Protokolü

**Yönlendirici soru:** Bu çalışma hangi soru, ihtiyaç veya belirsizlikten doğuyor; kim tarafından, hangi kapsam içinde ve hangi başlangıç kabulleriyle yürütülüyor?

### Başlangıç yönelişi

Tohum, konunun varlık, mekân, usul, zaman ve gaye bakımından ayrıştırılmasından önceki yönelişini kaydeder. Çalışmayı başlatan soru, karşılaşılan ihtiyaç veya açıklığa kavuşturulmak istenen belirsizlik burada ifade edilir. Başlangıç yalnızca bir tarih değildir; konunun neden dikkat konusu olduğunu ve ona hangi açıdan yaklaşılacağını da içerir.

Makine Öğrenmesi Mühendisliği açısından tohum, hazır bir araç ya da model seçimi olmak zorunda değildir. Öğrenilmiş hesaplama davranışının bir ihtiyaca katkısını anlamak, mevcut bir sistemin sınırlarını araştırmak veya alanın taşıyıcı öznesini açıklamak başlangıç yönelişi olabilir. İlk yöneliş, araştırma sonunda ulaşılacak cevapları önceden zorunlu kılmaz. Başlangıçta bilinmeyenler açık sorular olarak kaydedilebilir.

Bu çalışmanın tohumu, Makine Öğrenmesi Mühendisliğini beş boyutuyla ve bu boyutları taşıyan özneyle birlikte anlama sorusudur. Kullanıcının ‘Geçmiş bağlamları buraya taşıma. Burası ile sınırlı kalma.’ ifadesi, başlangıcın bağlam sınırını belirtir. Konuşma dışından devralınmış kişisel bağlam, açıklanmamış başlangıç kabulüne dönüştürülmez. Kullanılan dış kaynaklar ise açıkça gösterilen dayanaklar olarak ele alınır.

### Kapsam, kabuller ve taşıyıcı

Tohumun kapsamı, çalışmanın ele aldığı konuyu ve mevcut çevrimde dışarıda kalan alanları belirginleştirir. Kullanılacak malzeme, beklenen çıktı, çalışma koşulları ve konuyu ele alan kişi ya da rol belirtilir. Taşıyıcı, konuyu tek başına yaratan veya bütün sonuçlarını önceden bilen kişi olarak düşünülmez; belirli bir durum içinde soru kuran ve araştırmayı başlatan öznedir.

Başlangıç kabulleri, gözlenmiş olgular ve henüz sınanmamış varsayımlar ayrılır. Kaynağı bulunan bilgi dayanağıyla birlikte tutulur. Öneri veya çıkarım, gerçekleşmiş sonuç olarak yazılmaz. Bir kişi, görev veya yetki bilinmiyorsa bu belirsizlik korunur. Sonraki protokoller başlangıç kaydını açar, sınar ve gerektiğinde değiştirir.

Tohum ile Gaye Protokolü farklı işleri yerine getirir. Tohum, araştırmayı harekete geçiren yönelişi ve başlangıç koşullarını kaydeder. Gaye Protokolü, incelenen faaliyetin hangi amaçlara hizmet ettiğini ve araçla amaç arasındaki ilişkinin nasıl gerekçelendirildiğini açar. Başlama nedeni ile araştırma sonunda açıklığa kavuşacak gaye ilişkili olabilir; baştan aynı şey sayılmaz.

### Başlangıcın yeterliliği ve sınırları

Tohumun tamamlanması bütün cevapların bulunması anlamına gelmez. Sonraki protokollerin hangi soruyu, hangi kapsamda ve hangi malzemeyle işleyeceği anlaşılabilir olduğunda başlangıç kaydı yeterli hâle gelir. Çalışmayı engelleyen eksikler belirginleştirilir; engellemeyen açık sorular sonraki bölümlere taşınır.

Tohum yalnızca bir başlık, araç tercihi veya kesin sonucun önceden ilanı değildir. Kapsamı belirsiz bir istek de tek başına yeterli başlangıç kaydı oluşturmaz. Araştırma yön değiştirdiğinde önceki başlangıç silinmez; değişen soru, gerekçe ve kapsam yeni sürümde görünür tutulur.

~~~text
  BASLANGIC YONELISI  bes boyuta ayristirilmadan once
    calismayi baslatan soru . karsilasilan ihtiyac . acikliga
    kavusturulmak istenen belirsizlik
    hazir bir arac ya da model secimi olmak zorunda degildir
    ilk yonelis, arastirma sonunda ulasilacak cevaplari onceden zorunlu
    kilmaz

  BAGLAM SINIRI
    "Gecmis baglamlari buraya tasima. Burasi ile sinirli kalma."
    konusma disindan devralinmis kisisel baglam  -/->  aciklanmamis
                                                      baslangic kabulu
    kullanilan dis kaynaklar  -->  acikca gosterilen dayanaklar

  KAPSAM  malzeme . beklenen cikti . calisma kosullari . konuyu ele alan
  kisi ya da rol
    ayrilir:  olgu | varsayim | cikarim | oneri | acik soru
    bilinmeyen kisi, yetki ve kosullar:  Belirlenmedi

  TOHUM  |  GAYE
    arastirmayi harekete geciren   |   incelenen faaliyetin hangi
    yonelis ve baslangic           |   amaclara hizmet ettigi
    kosullari                      |
    baslama nedeni ile arastirma sonunda acikliga kavusacak gaye
    iliskili olabilir; bastan ayni sey sayilmaz

  YETERLILIK
    sonraki protokollerin hangi soruyu, hangi kapsamda ve hangi
    malzemeyle isleyecegi anlasilabilir oldugunda
    arastirma yon degistirdiginde onceki baslangic silinmez
~~~

*Çizim 3 — Tohum: başlangıç yönelişi; bağlam sınırı; kapsam; Tohum ve Gaye; yeterlilik.*

### Masaüstünde uygulama

#### Girdi

Özgün talep, mevcut soru ve yanıtlar, seçilmiş belgeler ve açık bağlam sınırları. Malzemenin bilinen tarih ve sürümleri.

#### Uygulama

1. Çalışma türünü ve başlangıç sorusunu çalışma kaydının 0 Tohum alanına yaz. Sorunun doğmasına yol açan ihtiyacı veya belirsizliği bir paragrafta açıkla.

2. Bu çevrimin kapsamını, kapsam dışında kalan konuları ve beklenen çıktıyı belirt. Kullanılacak belge ve kaynakların yerini kanıt kaydına ekle.

3. Başlangıç bilgilerini olgu, varsayım, çıkarım, öneri veya açık soru olarak ayır. Henüz bilinmeyen kişi, yetki ve koşulları Belirlenmedi olarak bırak.

4. Sonraki protokollere hangi soru ve malzemeyi aktardığını kaydet. Çalışmayı engelleyen bir eksik varsa etkisini ve nasıl giderilebileceğini yaz.

#### Tutulacak kayıt

Başlangıç sorusu; yöneliş; çalışma türü; kapsam ve sınırlar; kaynak malzeme; kabuller; açık sorular; beklenen çıktı; kaydı oluşturan kişi veya rol.

#### Tamamlanma ölçütü

Başka bir okuyucu çalışmanın neden başladığını, neyi ele aldığını, hangi kabullerle ilerlediğini ve sonraki bölümlere ne aktarılacağını anlayabiliyor. Tamamlanma durumu ve tarihi yalnız bu değerlendirme yapıldığında yazılır.

#### Yeniden açma koşulu

Ana soru, kapsam, kaynak sınırı, beklenen çıktı veya temel başlangıç kabulü değiştiğinde 0'ı güncelle. Önceki ifadeyi değişiklik kaydında koru.

## 1 Varlık Protokolü

**Özgün soru:** Nedir? Onu o yapan nelerdir? Neler değildir?

### Tanım ve ayırt edici nitelikler

Makine öğrenmesi mühendisliği, işlevinin bir bölümü veriden veya çevreyle etkileşimden öğrenilen hesaplama sistemlerini, belirli amaçlar ve gerçek kullanım koşulları için tasarlama, kurma, değerlendirme ve sürdürme disiplinidir. Öğrenilmiş davranış, çalışan sistem ve kullanım amacı bu tanımın birlikte ele alınan unsurlarıdır. Alanın ayırt edici niteliği, bunların arasındaki ilişkinin mühendislik konusu hâline gelmesidir.

Model, girdilerle çıktılar arasında öğrenilmiş ilişkileri veya davranışları taşıyan bileşendir. Sistem, bu bileşeni veri kaynakları, diğer yazılımlar, donanım, kullanıcılar ve sonuç doğuran işlemlerle birleştirir. Mühendislik süreci ise bu bütünün nasıl kurulacağını, sınanacağını, değiştirileceğini ve sürdürüleceğini belirleyen faaliyettir. Modelin başarısı ile sistemin kullanım yeterliliği farklı değerlendirme düzeyleridir. Microsoft'un yazılım ekipleri üzerine araştırması da veri yönetimi, model uyarlama ve bileşen bağımlılıklarının ek mühendislik sorunları yarattığını gösterir. [1]

Davranışın bir bölümü dolaylı biçimde kurulur. Mühendis bütün durumların sonuçlarını tek tek yazmak yerine öğrenme yöntemini, veriyi, hedefi, kısıtları ve değerlendirme koşullarını belirler. Hangi örneklerin seçildiği, neyin başarı sayıldığı ve hangi hataların görünür kılındığı böylece tasarım kararlarına dönüşür. Öğrenmenin kullanılması, davranışın nasıl oluştuğuna ilişkin sorumluluğu ortadan kaldırmaz.

Örneklerde elde edilen başarının kullanım koşullarına aktarılması ayrıca kanıt gerektirir. Verinin hangi koşulları temsil ettiği ve hangilerini dışarıda bıraktığı araştırılır. Benzer test başarısına sahip modeller farklı kullanım ortamlarında farklı davranabilir. Underspecification çalışması, eğitim ve test sonuçlarının uygulama için önemli bazı davranışları belirlemeye yetmeyebildiğini gösterir. Bu nedenle başarı sayısı, hangi davranışlardan doğduğu ve nerede geçerli olduğu ile birlikte değerlendirilir. [2]

Öğrenilmiş davranış, zamanında sonuç verme, uygun kaynaklarla çalışma, hataların anlaşılabilmesi ve müdahale edilebilirlik gibi sistem beklentilerine bağlanır. Üretim hattında biraz daha isabetli fakat ürün geçtikten sonra sonuç veren bir model, kullanım için daha yetersiz olabilir. Çok hızlı çalışan bir model de yanlış ürün çeşidi üzerinde kullanıldığında görevini karşılamayabilir. İstatistiksel başarı ile çalışma yeterliliği birlikte düşünülür.

Değişim de varlığın parçasıdır. Veri kaynakları, kullanım koşulları ve modele bağlı bileşenler değişebilir; bunların etkisi kaynak kodunda açık bir hata olarak görünmeyebilir. Hidden Technical Debt in Machine Learning Systems, veri bağımlılıkları, bileşenlerin birbirine dolanması ve gizli geri besleme döngülerinin bakım yükü doğurabildiğini ortaya koyar. Alanın özgüllüğü, başka mühendisliklerde de bulunan özelliklerin öğrenilmiş davranışın geçerliliği çevresinde birleşmesidir. [3]

~~~text
  TANIM  islevinin bir bolumu veriden veya cevreyle etkilesimden
  ogrenilen hesaplama sistemlerini belirli amaclar ve gercek kullanim
  kosullari icin tasarlama, kurma, degerlendirme ve surdurme

    +---------------------------- sistem ----------------------------+
    |  veri kaynaklari . diger yazilimlar . donanim . kullanicilar . |
    |  sonuc doguran islemler                                        |
    |        +--------------------------------------------+          |
    |        |  model                                     |          |
    |        |  girdilerle ciktilar arasinda ogrenilmis   |          |
    |        |  iliskileri veya davranislari tasir        |          |
    |        +--------------------------------------------+          |
    +----------------------------------------------------------------+
    muhendislik sureci  bu butunun nasil kurulacagini, sinanacagini,
    degistirilecegini ve surdurulecegini belirleyen faaliyet
    modelin basarisi  |  sistemin kullanim yeterliligi  [1]

  DAVRANIS DOLAYLI KURULUR  muhendis belirler:
    ogrenme yontemi . veri . hedef . kisitlar . degerlendirme kosullari
    ogrenmenin kullanilmasi, davranisin nasil olustuguna iliskin
    sorumlulugu ortadan kaldirmaz

  ORNEKLERDEKI BASARI  -->  kullanim kosullari:  ayrica kanit  [2]
    uretim hattinda  biraz daha isabetli ama urun gectikten sonra
                     sonuc veren model
                     cok hizli ama yanlis urun cesidinde kullanilan
                     model
    istatistiksel basari ile calisma yeterliligi birlikte dusunulur
    degisim de varligin parcasidir  [3]
~~~

*Çizim 4 — Varlık: tanım; model, sistem ve mühendislik süreci; dolaylı kurulan davranış; örneklerdeki başarı ve kullanım koşulları.*

### Varlığın taşıyıcısı

Bu faaliyetin mesleki öznesi makine öğrenmesi mühendisidir; ancak unvan, fiilen üstlenilen sorumlulukların tamamını açıklamaz. Farklı unvanlara sahip insanlar da aynı mühendislik faaliyetini gerçekleştirebilir. Daha temel düzeyde taşıyıcı, bir ihtiyacı tanımlayan, araç kuran, sonuçları sınayan ve gerektiğinde kararını değiştiren insandır. Bu insan sınırlı bilgiyle çalışır, başkalarından devraldığı yöntemleri ve kendi üretmediği araçları kullanır.

Taşımak, bu boyutların hepsine sahip olmak veya onları tek başına yaratmak anlamına gelmez. İnsan bir temsil seçebilir; seçtiği temsilin gerçek durumu yeterince açıklayıp açıklamadığı ayrıca sınanır. Görüntüdeki etiket nesnenin kendisi, kusurlu etiketi de kusurun bütün anlamı değildir. Gözlenen sonuçlar, kullanılan malzeme ve dünyanın özellikleri temsil seçimini sınırlayabilir veya geçersiz kılabilir.

Köken, faaliyeti mümkün kılan bilgi, ihtiyaç, malzeme ve tarihtir. Taşıyıcı, faaliyetin üzerinde ve içinde gerçekleştiği insanlar, araçlar, kayıtlar ve kurumlardır. Yapan, belirli bir işlemi gerçekleştiren kişi veya sistemdir. Sorumluluğun muhatabı ise bir kararın gerekçesi, kullanımı ve sonuçları hakkında açıklama ve düzeltme yükümlülüğü taşıyan kişi veya kurumdur. Bu dört ilişki aynı yerde birleşebilir; birleşmeleri zorunlu değildir.

Bir eğitim algoritması parametreleri değiştirebilir; bir değerlendirme sistemi adayları karşılaştırabilir; bir mühendis karşılaştırmanın geçerliliğini inceleyebilir; kullanıma geçişi başka bir ekip kararlaştırabilir. Sonuçtan etkilenenler bunların dışında bulunabilir. Bir işlemin otomatikleşmesi, amacının ve kullanım gerekçesinin kendiliğinden oluştuğu anlamına gelmez. NIST de tasarım, geliştirme, işletim, değerlendirme ve yönetim görevlerini farklı aktörlerle ilişkilendirir. [7]

Teknik makine, hesaplamanın maddi olarak gerçekleşmesini sağlar ve neyin yapılabileceğini etkiler. Buna karşılık modelin ya da donanımın kimliği, mühendislik faaliyetinin bütün kimliğini açıklamaz. İnsan, kurum ve araçların oluşturduğu bütünü makine olarak adlandırmak kavramsal bir tercihtir. Bu tercih, insanların bütün varlığının bir işlem şemasıyla eksiksiz açıklandığını veya örgütlenmenin tek bir bilince sahip olduğunu kanıtlamaz.

### Varlığın sınırları

Alan yalnızca model eğitmekle tanımlanmaz; önceden eğitilmiş modeli seçmek, uyarlamak, sınamak ve sisteme yerleştirmek de kapsama girebilir. Özgün algoritma icat etmek, büyük veri kullanmak, büyük model kurmak veya pahalı donanıma sahip olmak zorunlu koşullar değildir. Küçük bir cihazdaki basit model de öğrenilmiş davranışın kullanım koşullarına uygunluğunu yönetmeyi gerektirebilir.

Öğrenilmiş bir sistemin her çalıştırmada farklı sonuç vermesi gerekmez. Aynı girdiye aynı çıktıyı veren bir model de öğrenilmiş olabilir. Sistem kullanım sırasında sürekli öğrenmek zorunda değildir; yeni girdiyi işlemek, o girdiden kalıcı biçimde öğrenmekten farklıdır. Makine öğrenmesi mühendisliği yapay zekânın tamamıyla da özdeş değildir; öğrenme içermeyen arama, planlama veya kural sistemleriyle birlikte çalışabilir.

Taşıyıcı özne her şeyi bilen, bütün işleri tek başına yapan ya da bütün amaçların sahibi olan kişi değildir. Yalnızca araç kullanabilmek de faaliyetin tüm kapsamını göstermez. Bir faaliyetin alana ait oluşu ile yetkin, güvenilir veya yararlı oluşu ayrı değerlendirilir; iyi mühendislik nitelikleri mesleki kimliğin kendiliğinden garantisi sayılmaz.

~~~text
  DORT ILISKI  ayni yerde birlesebilir; birlesmeleri zorunlu degildir
    koken                  faaliyeti mumkun kilan bilgi, ihtiyac,
                           malzeme ve tarih
    tasiyici               faaliyetin uzerinde ve icinde gerceklestigi
                           insanlar, araclar, kayitlar ve kurumlar
    yapan                  belirli bir islemi gerceklestiren kisi veya
                           sistem
    sorumlulugun muhatabi  bir kararin gerekcesi, kullanimi ve sonuclari
                           hakkinda aciklama ve duzeltme yukumlulugu
                           tasiyan kisi veya kurum

  BIR ORNEK DAGILIM  [7]
    egitim algoritmasi        parametreleri degistirebilir
    degerlendirme sistemi     adaylari karsilastirabilir
    muhendis                  karsilastirmanin gecerliligini
                              inceleyebilir
    baska bir ekip            kullanima gecisi kararlastirabilir
    sonuctan etkilenenler     bunlarin disinda bulunabilir

  SINIRLAR  zorunlu kosul degil
    ozgun algoritma icat etmek . buyuk veri . buyuk model . pahali
    donanim
    her calistirmada farkli sonuc . kullanim sirasinda surekli ogrenme
    makine ogrenmesi muhendisligi  =/=  yapay zekanin tamami
    alana ait olus  |  yetkin, guvenilir veya yararli olus
~~~

*Çizim 5 — Varlık: köken, taşıyıcı, yapan ve sorumluluğun muhatabı; bir örnek dağılım; sınırlar.*

### Masaüstünde uygulama

#### Girdi

Tohum kaydı, incelenen faaliyet veya sistemin mevcut açıklaması ve eldeki kanıtlar.

#### Uygulama

1. İncelenen faaliyeti iki veya üç cümleyle tanımla; öğrenilmiş davranışın, çalışan sistemin ve kullanım amacının ilişkisini göster.

2. Modeli, onu içeren sistemi ve mühendislik faaliyetini ayrı paragraflarda açıkla. Bu unsurların gerçekleşmiş durumunu, tasarlanan durumundan ayır.

3. Kökeni, taşıyıcıyı, işi yapanı ve sorumluluğun muhatabını ayrı alanlara yaz. Bilinmeyen rol veya yetkiyi uydurma; açık mesele olarak kaydet.

4. Alanı ayırt eden nitelikleri ve kapsam dışı yorumları belirt. İyi yapılmış olma iddiası varsa bunu alan üyeliğinden ayır ve dayanağını kanıt kaydına bağla.

#### Tutulacak kayıt

Tanım; model, sistem ve mühendislik ayrımı; köken; taşıyıcı; yapan; sorumluluğun muhatabı; ayırt edici nitelikler; sınırlar; açık meseleler ve kanıt kimlikleri.

#### Tamamlanma ölçütü

Ne incelendiği, hangi düzeyde konuşulduğu ve taşıyıcıların hangi ilişkilerle ayrıldığı anlaşılır. Tanım ile yeterlilik iddiası birbirine karıştırılmamış; bilinmeyenler görünür tutulmuştur.

#### Yeniden açma koşulu

İncelenen nesne, modelin rolü, sistem sınırı, tanım veya sorumluluk dağılımı değiştiğinde 1'e dön. Kapsam da değişiyorsa 0'ı yeniden değerlendir.

## 2 Mekan Protokolü

**Özgün soru:** Nerededir? Bu yeri, oraya has bir yer yapan nelerdir? Neler değildir?

### Bilgiler ve çalışma koşulları arasındaki yer

Makine öğrenmesi mühendisliğinin mekânı, bilgi alanları arasındaki konumu, gerçek kullanım ortamını ve sorumluluk ilişkilerini birlikte içerir. İstatistik ve öğrenme kuramı örneklerden hangi varsayımlar altında sonuç çıkarılabileceğini araştırır. Makine öğrenmesi araştırması yöntem ve yetenek olanaklarını genişletir. Veri mühendisliği verinin elde edilmesini, tanımlanmasını, dönüşümünü ve erişilebilirliğini düzenler. Yazılım ve sistem mühendisliği bileşenlerin çalışmasını, bütünleşmesini ve değiştirilmesini sağlar.

İşletim ve altyapı kapasite, gecikme, maliyet ve süreklilik koşullarını taşır. Uygulama alanı bilgisi, çıktının ne anlama geldiğini ve hangi durumda işe yaradığını açıklar. Bu ilişkiler meslekler arasında dışlayıcı sınırlar kurmaz. Veri bilimci üretim sistemi geliştirebilir, yazılım mühendisi model değerlendirebilir ve araştırmacı yaşam döngüsünün geniş bir bölümünü üstlenebilir. Ayırıcı olan faaliyetin ağırlık merkezi ve üstlenilen sorumluluktur.

MLOps, geliştirme ile işletimi bağlayan; test, sürümleme, dağıtım ve izleme gibi süreçleri düzenleyen pratikler bütünüdür. Bu pratikler öğrenilmiş sistemlerin yaşam döngüsünü yürütmeye yardım eder. Alanın problem kurma, yöntem seçme ve kullanım gerekçesini değerlendirme muhakemesinin tamamını tek başına kapsamaz. [4]

~~~text
  BILGI ALANLARI ARASINDAKI KONUM
    istatistik ve ogrenme     orneklerden hangi varsayimlar altinda
    kurami                    sonuc cikarilabilecegi
    makine ogrenmesi          yontem ve yetenek olanaklari
    arastirmasi
    veri muhendisligi         verinin elde edilmesi, tanimlanmasi,
                              donusumu ve erisilebilirligi
    yazilim ve sistem         bilesenlerin calismasi, butunlesmesi ve
    muhendisligi              degistirilmesi
    isletim ve altyapi        kapasite . gecikme . maliyet . sureklilik
    uygulama alani bilgisi    ciktinin ne anlama geldigi ve hangi
                              durumda ise yaradigi

    meslekler arasinda dislayici sinirlar kurmaz
    ayirici olan:  faaliyetin agirlik merkezi ve ustlenilen sorumluluk

  MLOps  [4]
    gelistirme  <------------------------------------>  isletim
                test . surumleme . dagitim . izleme
    yasam dongusunu yurutmeye yardim eder; problem kurma, yontem secme
    ve kullanim gerekcesini degerlendirme muhakemesinin tamamini tek
    basina kapsamaz
~~~

*Çizim 6 — Mekan: bilgi alanları arasındaki konum; MLOps.*

### Gözlem ile sonuç arasındaki ortam

Alan, gözlemin veriye, verinin hesaplamaya, hesaplamanın çıktıya ve çıktının bir sonuca dönüştüğü bağlantılarda bulunur. Sensör ölçümü, metin, cihaz kaydı veya görüntü belirli dönüşümlerden geçerek modele ulaşır. Çıktı başka bir yazılımın girdisi, bir insanın değerlendireceği öneri ya da bir makinenin uygulayacağı işlem olabilir. Bu bağlantıların anlamı uygulama ortamıyla birlikte belirlenir.

Aynı 0,8 çıktısı bir sistemde sıralama puanı, başka bir sistemde tahmini olasılık, bir başkasında işlem başlatmak için kullanılan değer olabilir. Sayının biçimi, nasıl üretildiğini veya ne için kullanılabileceğini tek başına açıklamaz. Bu nedenle veri ve çıktı, içinde bulundukları anlam ve kullanım ilişkileriyle değerlendirilir.

Sistemin sonucu yeni veriyi de değiştirebilir. Bir öneri sistemi bazı içerikleri daha görünür yaptığında, sonradan gözlenen kullanıcı davranışları bu görünürlüğün etkisini taşır. Performative Prediction çalışması, tahminlere dayalı kararların tahmin edilmeye çalışılan sonuçları değiştirebildiğini ele alır. Böyle bir sistemin mekânı, kapalı bir veri işleme hattından daha geniştir; gözlemlerin oluştuğu ve sonuçların geri döndüğü ortamı da içerir. [5]

Bu yeri özgül yapan, farklı yeterlilik ölçütlerinin aynı kullanımda buluşmasıdır. İstatistiksel açıdan güçlü bir model çalışma süresi bakımından yetersiz olabilir. Teknik olarak düzenli çalışan bir hizmet yanlış ihtiyacı karşılayabilir. Yararlı çıktı üreten bir sistemin maliyeti sürdürülmesini güçleştirebilir. Mühendislik, bu ölçütler arasındaki ilişkiyi ve birindeki değişimin diğerlerine etkisini araştırır.

~~~text
  GOZLEM ILE SONUC ARASINDAKI ORTAM

    gozlem --> veri --> hesaplama --> cikti --> sonuc
                ^                                 |
                +--- yeni veri <-----------------+
                     ornek:  bir oneri sistemi bazi icerikleri daha
                     gorunur yaptiginda, sonradan gozlenen kullanici
                     davranislari bu gorunurlugun etkisini tasir  [5]

  AYNI 0,8 CIKTISI
                    +-->  siralama puani
    0,8  -----------+-->  tahmini olasilik
                    +-->  islem baslatmak icin kullanilan deger
    sayinin bicimi, nasil uretildigini veya ne icin kullanilabilecegini
    tek basina aciklamaz

  FARKLI YETERLILIK OLCUTLERI AYNI KULLANIMDA BULUSUR
    istatistiksel acidan guclu bir model   |  calisma suresi bakimindan
                                           |  yetersiz
    teknik olarak duzenli calisan hizmet   |  yanlis ihtiyaci karsilar
    yararli cikti ureten sistem            |  maliyeti surdurulmesini
                                           |  guclestirir
~~~

*Çizim 7 — Mekan: gözlemden sonuca uzanan bağlantılar ve geri besleme; aynı 0,8 çıktısı; buluşan yeterlilik ölçütleri.*

### Mekânı taşıyan insanlar ve ilişkiler

Mühendis, çalışmasını mümkün kılan ilişkilerin dışında durmaz. Kullanılan kavramlar, erişilen veri, donanım olanakları, kurumsal kararlar ve kullanıcı uygulamaları çalışmanın koşullarını oluşturur. Üretim hattında kusurun tanımı alan uzmanlığından gelir; görüntüdeki belirtilerin öğrenilebilirliği modelleme sorusudur; yanlış elemenin sonuçları işletimle ilişkilidir. Bu bilgilerin hiçbiri tek başına bütün sistemi tarif etmez.

Yapay zekâ sistemlerinin davranışı teknik bileşenlerin yanında insan kullanımı ve toplumsal bağlam tarafından da şekillenir. NIST'in sosyoteknik yaklaşımı bu ilişkiyi vurgular. Selbst ve çalışma arkadaşları da teknik sistemleri çevreleyen aktör ve kurumların soyutlama dışında bırakılmasının, toplumsal sonuçların değerlendirilmesinde gerekli bağlamı kaybettirebildiğini gösterir. [6], [10]

Ortak çalışma düzeninde araştırma, veri sağlama, temizleme, etiketleme, alan bilgisi, altyapı işletimi ve kullanım farklı kişilere dağılabilir. ILO, yapay zekâ sistemlerinin geliştirilmesi ve işletilmesinde veriyi sınıflandıran, temizleyen ve doğrulayan çalışanların katkısını özellikle belirtir. Faaliyetin taşıyıcısını yalnızca modeli eğiten kişi olarak görmek bu emeği eksik gösterir. [9]

Bu bütün tek iradeli bir insan gibi düşünülmez. Kurumun maliyet, kullanıcının hizmet niteliği ve çalışanın uygulanabilir süreç beklentileri uyumlu veya çatışmalı olabilir. Kolektif üretim, bütün katılımcıların eşit yetkili ya da aynı ölçüde sorumlu olduğunu göstermez. Kimin hangi kararı verdiği ve neyi değiştirebildiği somutlaştırılır; sonuçtan etkilenen kişinin sisteme doğrudan erişmesi de zorunlu değildir.

### Mekânın sınırları

Makine öğrenmesi mühendisliği tek bir şirket bölümünün, bulut hizmetinin, laboratuvarın veya donanım türünün adı değildir. Telefonda, üretim hattında, bilimsel araştırma altyapısında, toplu veri işleyen süreçte veya çevrimiçi hizmette gerçekleşebilir. Bunlar faaliyetin bulunduğu yerlerdir; hiçbiri tek başına tanımsal mekân değildir.

Alan, araştırma tamamlandıktan sonra modelin teslim edildiği tek bir ara istasyon olarak da kurulmaz. Problem seçimi ve veri toplama, daha sonraki kullanımın koşullarını şekillendirir. Sistemin bütünlüğünü gözetmek, bütün işleri aynı kişinin yapmasını gerektirmez. Ortak çalışma düzenini görmek ise sorumluluğu isimsiz bir herkes veya sistem sözcüğü içinde belirsizleştirmemelidir.

~~~text
  URETIM HATTINDA  bilgilerin hicbiri tek basina butun sistemi tarif
  etmez
    kusurun tanimi                       alan uzmanligindan gelir
    goruntudeki belirtilerin             modelleme sorusu
    ogrenilebilirligi
    yanlis elemenin sonuclari            isletimle iliskili

  DAGILAN EMEK  [9]
    arastirma . veri saglama . temizleme . etiketleme . alan bilgisi .
    altyapi isletimi . kullanim
    tasiyiciyi yalnizca modeli egiten kisi olarak gormek bu emegi eksik
    gosterir

  TEK IRADELI BIR INSAN DEGIL
    kurumun maliyet  |  kullanicinin hizmet niteligi  |  calisanin
    uygulanabilir surec beklentileri:  uyumlu veya catismali olabilir
    kolektif uretim  -/->  esit yetki ya da ayni olcude sorumluluk
    somutlastirilir:  kimin hangi karari verdigi . neyi
    degistirebildigi

  MEKANIN SINIRLARI
    tek bir sirket bolumu . bulut hizmeti . laboratuvar . donanim turu
    degildir
    bulundugu yerler:  telefon . uretim hatti . bilimsel arastirma
    altyapisi . toplu veri isleyen surec . cevrimici hizmet
    arastirma bittikten sonra modelin teslim edildigi tek bir ara
    istasyon degildir
~~~

*Çizim 8 — Mekan: üretim hattındaki bilgiler; dağılan emek; tek iradeli olmayan bütün; mekânın sınırları.*

### Masaüstünde uygulama

#### Girdi

Tohum ve Varlık kayıtları; kullanım ortamı, veri kaynakları, çıktı kullanımı ve katılan kişiler hakkında mevcut bilgi.

#### Uygulama

1. Bilgi alanları arasındaki konumu ve gerçek kullanım ortamını ayrı paragraflarda yaz. Fiziksel ortamı, yazılım ortamını ve kurumsal ilişkileri gerektiği ölçüde belirt.

2. Gözlemden veriye, modelden çıktıya ve çıktıdan sonuca uzanan akışı açıkla. Her bağlantıda bilgiyi sağlayan ve çıktıyı kullanan kişi veya bileşeni kaydet.

3. Katılanları ve sonuçlardan etkilenenleri ayır. Kimin hangi kararı verebildiğini veya hangi bileşeni değiştirebildiğini mevcut bilgiyle belirt.

4. Sistemin çıktısının yeni veriyi değiştirebileceği geri beslemeleri ve kullanım için belirleyici ortam koşullarını yaz. Ortam bilgisi eksikse bunun değerlendirmeye etkisini kaydet.

#### Tutulacak kayıt

Bilgisel konum; kullanım ortamı; veri ve çıktı akışı; katılanlar; etkilenenler; karar ve müdahale yetkileri; geri beslemeler; ortam koşulları; kanıtlar ve eksikler.

#### Tamamlanma ölçütü

Sistemin nerede ve hangi ilişkiler içinde anlam kazandığı açıklanmış; ortamın yalnız donanımdan ibaret olmadığı gösterilmiş; katılım ile yetki ve sorumluluk ayrılmıştır.

#### Yeniden açma koşulu

Veri kaynağı, kullanıcı grubu, kullanım yeri, çıktıdan sonra alınan karar veya kurumsal ilişki değiştiğinde 2'ye dön; etkilenen yöntem ve amaç kayıtlarını da incele.

## 3 Usül Protokolü

**Özgün soru:** Nasıl işler yapar? Bu yaptıklarını, ona has yapan nelerdir? Neler değildir?

### İhtiyaçtan öğrenilebilir göreve

Makine öğrenmesi mühendisliği sınıflandırma, tahmin, sıralama, örüntü bulma, içerik üretme veya eylem seçme gibi öğrenilmiş yetenekleri kullanılabilir sistemlere dönüştürür. Usul, çıktı türlerinden daha geniştir: ihtiyacın kurulmasını, verinin anlamını, yöntemlerin karşılaştırılmasını, kullanım koşullarını ve sonuçlara göre değişikliği birbirine bağlar. Bu işlemler bir kez geçilen doğrusal bir sıra olmak zorunda değildir; yeni bulgular önceki kararların yeniden ele alınmasına yol açabilir.

Üretim hattında kusurlu parçaları ayıran varsayımsal bir sistem düşünüldüğünde, kusur tespiti yapma isteği tek başına yeterli problem tanımı oluşturmaz. Hangi kusurların aranacağı, hangi aşamada tespit edileceği, kaçırmanın ve yanlış elemenin sonuçları, çıktının kim tarafından kullanılacağı ve mevcut süreçteki asıl sorun açıklanır. Daha iyi aydınlatma, daha doğru ölçüm veya basit bir kural ihtiyacı karşılayabiliyorsa bu seçenekler de değerlendirilir.

İhtiyaç ile model hedefi arasındaki bağ başlangıçta görünür kılınır. Başarı ölçütleri, modelin bulunmasından sonra ona uydurulan sayılara dönüşmemelidir. Rules of Machine Learning rehberi, ölçütlerin erken kurulmasını, basit çözümlerin denenmesini ve ilk modelle birlikte altyapının sağlamlaştırılmasını öne çıkarır. Kullanılacak karmaşıklık, sağladığı katkıyla gerekçelendirilir. [11]

~~~text
  OGRENILMIS YETENEKLER  -->  KULLANILABILIR SISTEMLER
    siniflandirma . tahmin . siralama . oruntu bulma . icerik uretme .
    eylem secme
    usul birbirine baglar:  ihtiyacin kurulmasi . verinin anlami .
    yontemlerin karsilastirilmasi . kullanim kosullari . sonuclara gore
    degisiklik
    bir kez gecilen dogrusal bir sira olmak zorunda degildir

  VARSAYIMSAL URETIM HATTI  "kusur tespiti yapma istegi" tek basina
  yeterli problem tanimi degil; aciklanir:
    hangi kusurlar aranacak . hangi asamada tespit edilecek . kacirmanin
    ve yanlis elemenin sonuclari . ciktiyi kim kullanacak . mevcut
    surecteki asil sorun
    ihtiyaci karsilayabiliyorsa degerlendirilir:
      daha iyi aydinlatma . daha dogru olcum . basit bir kural

  IHTIYAC  <------ bag baslangicta gorunur ------>  MODEL HEDEFI
    basari olcutleri, modelin bulunmasindan sonra ona uydurulan
    sayilara donusmemelidir  [11]
    kullanilacak karmasiklik, sagladigi katkiyla gerekcelendirilir
~~~

*Çizim 9 — Usül: öğrenilmiş yeteneklerden kullanılabilir sistemlere; üretim hattında problem tanımı; ihtiyaç ile model hedefi.*

### Veri ve karşılaştırma düzeni

Verinin hangi durumu temsil ettiği araştırılır. Yalnız gündüz vardiyasında toplanan görüntüler gece koşullarını, tek ürün çeşidinin görüntüleri yeni bir çeşidi yeterince temsil etmeyebilir. Etiketleyen uzmanların kusur tanımları farklıysa, bu tutarsızlık öğrenme malzemesine taşınır. Veri toplamakla birlikte hangi koşulların kaydedildiği, hangilerinin eksik olduğu ve etiketlerin nasıl üretildiği açıklanır. Datasheets for Datasets, veri kümelerinin amacı, bileşimi, toplama süreci ve uygun kullanımlarının belgelenmesini önerir. [12]

Çözüm adayları uygun karşılaştırma noktalarıyla değerlendirilir. Mevcut uygulama, basit eşik yöntemi veya küçük model bir başlangıç ölçütü sağlayabilir. Yeni bir veri kaynağı, düzeltilmiş ön işleme, daha tutarlı etiket tanımı ya da gereksiz bir özelliğin kaldırılması, daha büyük modele geçmekten daha yararlı olabilir. Her müdahalenin hangi hatayı azalttığı, kazancın tekrar elde edilip edilmediği ve başka koşullarda kayıp doğurup doğurmadığı incelenir.

Başarı ölçütünün gerçekte neyi ölçtüğü sınanır. Örneğin parçaların yüzde 99'u sağlamsa, hepsine sağlam diyen varsayımsal bir sistem yüzde 99 doğruluk elde ederken hiçbir kusuru yakalamaz. Bu hesap, tek bir yüksek sayının aranan işlevi kanıtlamayabileceğini gösterir. Hata türleri, görülme sıklıkları ve kullanım sonuçları değerlendirmeye katılır.

Kullanım anında erişilemeyecek bilginin eğitim veya değerlendirmeye taşınması veri sızıntısı oluşturabilir. Test verisinin model seçimine ya da veri dönüşümlerinin öğrenilmesine katılması gereğinden iyimser başarı tahminleri doğurabilir. scikit-learn belgeleri bu ayrımın korunmasını açıklar. Üretim örneğinde aynı parçanın çok benzer görüntülerinin eğitim ve test tarafına dağılması, yeni parçalar üzerindeki başarı hakkında yanıltıcı izlenim verebilir. Veri ayrımı gerçek kullanımda karşılaşılacak yeniliği temsil etmelidir. [13]

Model olasılık bildiriyorsa bu sayıların gerçekleşme sıklıklarıyla uyumu ayrıca değerlendirilebilir. İsabetli sınıflandırma ile iyi kalibre edilmiş olasılık farklı özelliklerdir. Kullanıcı veya başka bir bileşen bu olasılığa dayanarak işlem yapacaksa, sayının nasıl yorumlanabileceği de sistemin usulüne dâhildir. Kalibrasyon araştırmaları bu ayrımın önemini gösterir. [14]

~~~text
  VERI NEYI TEMSIL EDIYOR?  [12]
    yalniz gunduz vardiyasinda      -/->  gece kosullari
    toplanan goruntuler
    tek urun cesidinin goruntuleri  -/->  yeni bir cesit
    etiketleyen uzmanlarin kusur tanimlari farkliysa, tutarsizlik
    ogrenme malzemesine tasinir

  BASARI OLCUTU GERCEKTE NEYI OLCUYOR?

    100 parca:  99 saglam  +  1 kusurlu

    S S S S S S S S S S S S S S S S S S S S S S S S S . . .  K
    |_____________________ 99 _____________________|          |
    "hepsine saglam" diyen       -->  99 dogru: yuzde 99 dogruluk
    varsayimsal bir sistem       -->  kusurlu 1 parca: yakalanmaz
    tek bir yuksek sayi aranan islevi kanitlamayabilir

  VERI SIZINTISI  [13]
    ayni parcanin cok benzer goruntuleri  --+-->  egitim
                                            +-->  test
    yeni parcalar uzerindeki basari hakkinda yaniltici izlenim
    veri ayrimi, gercek kullanimda karsilasilacak yeniligi temsil
    etmelidir

  isabetli siniflandirma  =/=  iyi kalibre edilmis olasilik  [14]
~~~

*Çizim 10 — Usül: verinin temsil ettiği; yüzde 99 örneği; veri sızıntısı; kalibrasyon.*

### Çalışma koşulları ve değişiklik

Model kullanım ortamına yerleştirilirken verinin doğru bileşene ulaşması, işlem süresi, bellek kullanımı, sonuçların doğru nesneye bağlanması ve hata durumları birlikte tasarlanır. Görüntü gelmemesi, modelin cevap vermemesi veya yeterince değerlendirilmemiş bir ürün çeşidiyle karşılaşılması gibi durumlarda sistemin nasıl davranacağı belirlenir. Model sürümü değiştiğinde birlikte güncellenmesi gereken bileşenler de hesaba katılır.

Yazılım testleri, veri doğrulaması ve model değerlendirmesi birbirini tamamlar. Bir test veri biçiminin doğru olduğunu gösterebilir; modelin yeni ışık koşullarındaki başarısını ayrıca ölçmek gerekir. The ML Test Score, üretimde kullanılabilirlik için veri, model ve izleme düzeylerinde somut test ihtiyaçlarını ele alır. Çalışan kod ile kullanım koşullarına uygun öğrenilmiş davranış ayrı kanıtlar gerektirebilir. [15]

Kullanım başladıktan sonra teknik işleyiş ve görev başarısı birlikte izlenir. Gecikme artabilir, yeni ürün çeşidinde hatalar yoğunlaşabilir veya veri akışı değiştiği hâlde görev başarısı korunabilir. Hatanın nedeni model, veri kaynağı, kamera ayarı ya da çıktıdan sonra uygulanan kural olabilir. Müdahale seçilmeden önce neyin değiştiği araştırılır; her değişiklik yeniden eğitim gerektirmez.

Uygun müdahale veriyi düzeltmek, modeli güncellemek, karar eşiğini değiştirmek, kullanım alanını daraltmak veya önceki sürüme dönmek olabilir. Sonuçları karşılaştırılabilir tutmak için kullanılan veri, model, kod ve değerlendirme koşulları izlenebilir biçimde kaydedilir. Model Cards yaklaşımı, modelin amaçlanan kullanımlarını, değerlendirme koşullarını ve performans özelliklerini birlikte açıklamayı önerir. [16]

### Usulün taşıyıcısı ve sınırları

Usulü taşıyan özne, yöntemi uygulamakla birlikte yöntemin uygunluğunu değerlendirir. Bazı seçimler otomatik araçlarla yapılabilir; yine de hangi seçeneklerin, ölçütlerin ve koşulların kullanıldığı açıklanmalıdır. Algoritmayı çalıştıran, değerlendirmeyi yorumlayan ve kullanıma karar veren aynı kişi ya da sistem olmayabilir. Usulün sürekliliği, bu katkıların birbirine anlaşılır biçimde aktarılmasına dayanır.

Alanı özgül yapan, adımların öğrenilmiş davranışa ilişkin kanıtla bağlanmasıdır. Yeni model ortalamada iyileşirken önemli bir koşulda kötüleşebilir. Daha güncel veri kullanım alanını daha az temsil edebilir. Başka bir bileşendeki küçük değişiklik girdinin anlamını değiştirebilir. Bu nedenle değişikliğin doğruluğu yalnızca kodun çalışmasına bakılarak belirlenmez.

Usul, başarılı örnekleri seçip göstermekle veya çok sayıda denemeyi kayıtsız biçimde yürütmekle tamamlanmaz. Bir gösterim olanağı ortaya koyabilir; kullanım yeterliliği başka kanıtlar da gerektirir. Her başarısızlık model yetersizliğine bağlanmaz; yanlış hedef, eksik veri, hatalı değerlendirme ve kullanım süreci de araştırılır. Bütün işleri otomatikleştirmek zorunlu değildir; insan değerlendirmesi, sabit kurallar ve öğrenilmiş bileşenler aynı sistemde farklı görevler üstlenebilir.

~~~text
  BIRBIRINI TAMAMLAR  [15]
    yazilim testleri  |  veri dogrulamasi  |  model degerlendirmesi
    bir test veri biciminin dogru oldugunu gosterebilir; modelin yeni
    isik kosullarindaki basarisini ayrica olcmek gerekir

  KULLANIM BASLADIKTAN SONRA
    hatanin nedeni olabilir:
      model | veri kaynagi | kamera ayari | ciktidan sonra uygulanan
      kural
    mudahale secilmeden once neyin degistigi arastirilir; her degisiklik
    yeniden egitim gerektirmez
    uygun mudahale olabilir:
      veriyi duzeltmek . modeli guncellemek . karar esigini
      degistirmek . kullanim alanini daraltmak . onceki surume donmek
    izlenebilir kayit:  veri . model . kod . degerlendirme kosullari
    [16]

  USULUN TASIYICISI
    algoritmayi calistiran  |  degerlendirmeyi yorumlayan  |  kullanima
    karar veren:  ayni kisi ya da sistem olmayabilir
    sureklilik, bu katkilarin birbirine anlasilir bicimde aktarilmasina
    dayanir

  USUL DEGILDIR
    basarili ornekleri secip gostermek . cok sayida denemeyi kayitsiz
    bicimde yurutmek
    her basarisizlik model yetersizligine baglanmaz:  yanlis hedef .
    eksik veri . hatali degerlendirme . kullanim sureci
~~~

*Çizim 11 — Usül: birbirini tamamlayan testler; kullanım başladıktan sonra; usulün taşıyıcısı; usulün olmadıkları.*

### Masaüstünde uygulama

#### Girdi

0–2 kayıtları; mevcut yöntemler, kaynaklar ve karşılaştırma imkânları; gerçek sistem çalışmasında erişilebilir veri ve değerlendirme ortamı.

#### Uygulama

1. İhtiyaçtan çıktıya uzanan yöntemi ve uygun karşılaştırma noktasını yaz. Hangi değişikliğin hangi sonucu iyileştirmesinin beklendiğini açıkla.

2. Verinin veya kaynakların neyi temsil ettiğini, değerlendirme koşullarını ve başarı ölçütlerini belirt. Model ölçütünü kullanım sonucundan ayır.

3. Kavramsal incelemede iddiayı kaynaklar ve karşı örneklerle değerlendir. Gerçek sistem uygulamasında seçili kapsam içinde yapılan deneyi veri ve model sürümü, yöntem, ölçüt ve sonuçla kaydet. Yalnız planlanan deneyi Planlandı olarak bırak.

4. Başarıya alternatif açıklamaları, veri sızıntısını, önemli alt koşulları ve hata türlerini incele. Ek değerlendirmeyi, kullanım koşullarını doğrulamak veya belirli bir belirsizliği çözmek için gerekçelendir. Mevcut kanıt yeterliyse aynı soruyu tekrar eden testler ekleme.

5. Sonucu değiştirme, sürdürme, kapsamı daraltma veya durdurma seçenekleriyle ilişkilendir. Kararın dayanağını ve hangi kayıtların etkilendiğini yaz.

#### Tutulacak kayıt

Yöntem; karşılaştırma noktası; veri veya kaynak kapsamı; değerlendirme planı; yapılan işlemler; ölçütler; sonuçlar; sınırlılıklar; karar ve dayanakları. Plan ile gerçekleşmiş sonuç ayrı tutulur.

#### Tamamlanma ölçütü

Başka bir okuyucu hangi yöntemin neden seçildiğini, neyin gerçekten yapıldığını ve sonucun hangi kararı desteklediğini izleyebiliyor. Gerçek sistemin yeterliliği iddia ediliyorsa ilgili deney kanıtı mevcuttur.

#### Yeniden açma koşulu

Yöntem, ölçüt, veri temsilinin anlamı veya karşılaştırma noktası değiştiğinde; yeni hata mevcut açıklamayı yetersiz kıldığında 3'e dön.

## 4 Zaman Protokolü

**Özgün soru:** Hangi andadır? Bu anı, diğer zamanlardan farklı yapan nelerdir? Neler değildir?

### Tarihsel dönem

Zaman üç ölçekte ele alınır: alanın tarihsel dönemi, bir sistemin yaşam döngüsü ve eldeki kanıtın geçerlilik zamanı. Bu kayıttaki güncel dönem değerlendirmesinin tarihi 31 Ekim 2026'dır. Belirli göreve model geliştirme, önceden eğitilmiş modeli uyarlama ve öğrenilmiş bileşenleri daha kapsamlı iş akışlarında birleştirme aynı dönemde bulunan çalışma biçimleridir.

Temel modeller üzerine 2021'de yayımlanan Stanford raporu, geniş veri üzerinde eğitilmiş modellerin farklı görevlere uyarlanabilmesini ve ortak modelin özelliklerinin aşağıdaki uygulamalara taşınmasını ele alır. Bunun mühendislik açısından sonucu, yeteneğin üretilmesi ile belirli kullanımda çalışmasına ilişkin sorumluluğun farklı aktörlere dağılabilmesidir. Temel modeli eğitmeyen uygulama ekibi de kendi girdilerini, bilgi kaynaklarını, değerlendirme koşullarını ve iş akışını yönetir. [17]

Üretken yapay zekâ uygulamalarında izlenen ve değiştirilen parçalar, model sürümünün yanında istem şablonlarını, erişilen bilgi kaynaklarını, araç bağlantılarını ve bileşenleri birleştiren düzeni içerir. Google'ın işletim rehberi, bu parçaların birlikte sürümlenmesi ve değerlendirilmesi ihtiyacını ele alır. Bu genişleme, kullanım amacını ve kanıtın geçerliliğini düşünme sorumluluğunu sürdürür. [18]

Anthropic'in 9 Ocak 2026 tarihli ajan değerlendirme çalışması, araçlarla çok adımlı iş yapan sistemlerde model ile onu çalıştıran düzenin birlikte değerlendirildiğini açıklar. Görevin tamamlandığı iddiasıyla ortamda gerçekten oluşan sonuç birbirinden ayrılır. Buradan çıkarılan yorum, bazı uygulamalarda değerlendirme nesnesinin tek çıktının niteliğinden eylem zincirinin toplam sonucuna genişlemesidir. Bu yorum, bütün makine öğrenmesinin ajanlara dönüştüğü veya küçük modellerin gerekçesini yitirdiği iddiasını içermez. [19]

Güncel bileşenlerin bir kısmı yenidir; değişen koşullarda bakım ve geçerlilik sorunu daha eskidir. 2015 tarihli teknik borç çalışması veri bağımlılıklarını, gizli geri beslemeleri ve dış dünyadaki değişiklikleri zaten ele alır. Bu nedenle alanın tarihsel kimliği yalnızca güncel ürün ve araç gündemiyle kurulmaz. [3]

~~~text
  UC OLCEK
    alanin tarihsel donemi . bir sistemin yasam dongusu . eldeki
    kanitin gecerlilik zamani

  TARIHSEL DONEM  kaynaklardaki tarihlerle

    2015 ---------- 2021 ---------- 9 Ocak 2026 ------ 31 Ekim 2026
     |               |               |                  |
    teknik borc     temel modeller  ajan               bu kayittaki
    calismasi [3]   raporu [17]     degerlendirme      guncel donem
                                    calismasi [19]     degerlendirmesi

    temel modeller:  yetenegin uretilmesi  |  belirli kullanimda
    calismasina iliskin sorumluluk:  farkli aktorlere dagilabilir
    uretken yapay zeka uygulamalarinda izlenen parcalar [18]:  model
    surumu . istem sablonlari . erisilen bilgi kaynaklari . arac
    baglantilari . bilesenleri birlestiren duzen
    bazi uygulamalarda degerlendirme nesnesi
      tek ciktinin niteligi  -->  eylem zincirinin toplam sonucu
    butun makine ogrenmesinin ajanlara donustugu iddiasi degildir
    bakim ve gecerlilik sorunu daha eskidir
~~~

*Çizim 12 — Zaman: üç ölçek; kaynaklardaki tarihlerle tarihsel dönem.*

### Sistemin yaşamındaki zaman

Mühendislik problem seçilirken başlar; veri toplama, deney, değerlendirme, kullanım ve değişim boyunca sürer. Kullanımın sona erdirilmesi de bu yaşamın parçasıdır. İhtiyacın öğrenme problemi olarak kurulması, deney sonucunun kullanım için yeterli görülmesi, sistem değişikliğinin kabul edilmesi ve önceki başarı kanıtının artık yeterli olmadığının anlaşılması farklı eşiklerdir.

Her eşikte farklı bir iddia sınanır. İlk deney yaklaşımın mümkün olabileceğini gösterebilir. Kullanıma geçiş, belirlenen koşullarda yeterli olduğuna ilişkin kanıta dayanır. Sonraki izleme bu koşulların ve yeterliliğin sürüp sürmediğini araştırır. Teslim tarihi bütün mühendislik zamanını kapsamaz; kullanımdaki sistemin bakım ve değerlendirme düzeni de bu zamanın içindedir.

Öğrenme zamanı ile kullanım zamanı birbirinden ayrılabilir. Model bir kez eğitilip sabit biçimde kullanılabilir veya gerektiğinde güncellenebilir. Her girdinin işlenmesi kalıcı öğrenme sayılmaz. Güncelleme sıklığı, koşulların değişimi ve kullanım ihtiyacıyla gerekçelendirilir; sürekli yeni sürüme geçmek kendiliğinden bir başarı ölçütü oluşturmaz.

### Kanıtın ve taşıyıcının zamanı

Model belirli deneyimlerden oluşturulur ve henüz bütünüyle gözlenmemiş durumlarda kullanılır. Mühendislik, eldeki kanıtla verilecek karar arasındaki zaman aralığında çalışır. Kanıtın yaşı önemlidir; ancak tek mesele yaşı değildir. Koşullar değişmediyse eski bir değerlendirme anlamlı kalabilir. Çok yeni veri yanlış koşullardan toplanmışsa kullanım ortamını temsil etmeyebilir.

Üretim örneğinde geçen ayki başarı, bu ay kamera değiştiğinde yeniden değerlendirilebilir. Kamera aynı kalsa bile ürün yüzeyi, ışığın yansıması veya kusur türleri değişebilir. Sorulan, geçmiş başarının hangi varsayımlarla bugüne taşınabileceğidir. Başarının koşullara bağlı geçerliliği, bir kez kanıt üretmekle bu kanıtın dayandığı koşulları izlemeyi birbirine bağlar.

Zamanı taşıyan insan önceki kararına geri dönebilir, hangi varsayımın bozulduğunu ve hangi kanıtın hâlâ geçerli olduğunu araştırabilir. Faaliyetin zamanı yalnız bireyin hafızasında bulunmaz. Kayıtlar, sürümler, belgeler ve ekipler arasında aktarılan bilgi, çalışmanın kişiler ve dönemler arasında devamını taşır. Ortak düzen böylece bir kişinin o anda hatırlayabildiklerinden daha uzun süre var olabilir.

Bu an, eğitimin bittiği tek bir nokta veya her gün yeniden eğitim gereği değildir. Geçmiş yüksek başarı geleceğe koşulsuz garanti sayılmaz; sistemin bütün değişikliklere kendiliğinden uyum sağlayacağı varsayılmaz. Buna karşılık bütün modellerin yalnız zaman geçtiği için zorunlu olarak yetersizleştiği de ileri sürülmez. Geçerlilik, somut koşullar ve kanıt üzerinden değerlendirilir.

~~~text
  SISTEMIN YASAMI
    problem secimi --> veri toplama --> deney --> degerlendirme -->
    kullanim --> degisim --> kullanimin sona erdirilmesi

  FARKLI ESIKLER
    ihtiyacin ogrenme problemi olarak kurulmasi
    deney sonucunun kullanim icin yeterli gorulmesi
    sistem degisikliginin kabul edilmesi
    onceki basari kanitinin artik yeterli olmadiginin anlasilmasi
    teslim tarihi butun muhendislik zamanini kapsamaz

  OGRENME ZAMANI  |  KULLANIM ZAMANI
    her girdinin islenmesi kalici ogrenme sayilmaz
    surekli yeni surume gecmek kendiliginden bir basari olcutu degildir

  KANITIN ZAMANI
    gecen ayki basari  ---- bu ay kamera degisti ---->  yeniden
                                                        degerlendirilir
    kamera ayni kalsa bile degisebilir:  urun yuzeyi . isigin
    yansimasi . kusur turleri
    sorulan:  gecmis basari hangi varsayimlarla bugune tasinabilir?
    gecmis yuksek basari     -/->  gelecege kosulsuz garanti
    yalniz zaman gecmesi     -/->  zorunlu yetersizlesme
~~~

*Çizim 13 — Zaman: sistemin yaşamı; farklı eşikler; öğrenme ve kullanım zamanı; kanıtın zamanı.*

### Masaüstünde uygulama

#### Girdi

Güncel çalışma kayıtları, veri ve model sürümleri, kaynak tarihleri ve değerlendirme kayıtları.

#### Uygulama

1. Kaydın tarihini ve sürümünü yaz. Kaynağın yayımlanma tarihini, eldeki kanıtın üretildiği tarihi ve incelenen olayın tarihini ayırt edilebildikleri ölçüde ayrı tut.

2. Tarihsel dönem, sistem yaşam döngüsü ve kanıtın geçerlilik zamanı için ayrı açıklamalar oluştur. Çalışmanın hangi aşamada olduğunu belirt.

3. Başarı kanıtının dayandığı koşulları ve bu koşulları geçersiz kılabilecek değişiklikleri kaydet. Kanıtın yalnız yaşına bakarak geçerli veya geçersiz olduğuna karar verme.

4. Bir sonraki değerlendirmeyi gerektiren olayı veya tarihi ve bunu takip edecek kişi ya da rolü yaz. Tarih kaydı ile gerçekten kurulmuş hatırlatıcıyı ayrı tut; otomasyon oluşturulmadıysa oluşturulmuş gibi işaretleme.

#### Tutulacak kayıt

Kayıt tarihi ve sürüm; kaynak, olay ve değerlendirme tarihleri; yaşam döngüsü aşaması; geçerlilik koşulları; yeniden değerlendirme tetikleri; takip eden kişi veya rol; kayıtların yeri.

#### Tamamlanma ölçütü

Önceki kanıtın hangi koşullarla bugüne taşındığı ve neyin yeniden değerlendirmeyi gerektireceği anlaşılır. Öğrenme, kullanım ve gözden geçirme zamanları karıştırılmamıştır.

#### Yeniden açma koşulu

Geçerlilik koşulu değiştiğinde, yeni sürüm veya kanıt geldiğinde ya da belirlenen gözden geçirme olayı gerçekleştiğinde 4'e ve etkilenen protokole dön.

## 5 Gaye Protokolü

**Özgün soru:** Hangi nihai amaca hizmet eder? Bu nihai amaca ulaştıran nelerdir? Neler değildir?

### Hedef, işlev, amaç ve gerekçe

Gaye açıklanırken öğrenme hedefi, sistemin işlevi, kullanım amacı ve daha geniş gerekçe ayrılır. Üretim örneğinde öğrenme hedefi, görüntüden kusur durumunu tahmin ederken tanımlanmış hatayı azaltmak olabilir. Sistemin işlevi, parçaları gereken sürede ve kabul edilen hata sınırlarında ayırmaktır. Kullanım amacı, kusurlu ürünlerin ilerlemesini azaltırken gereksiz eleme ve işlem yükünü sınırlamak olabilir. Daha geniş gerekçe ise kaynakları daha iyi kullanmak ve ürün niteliğini artırmak gibi ihtiyaçlara dayanır.

Bu katmanlar birbirini destekleyebilir; aralarındaki bağ ayrıca gösterilir. Daha fazla kusur yakalayan model çok sayıda sağlam parçayı da eleyebilir. Teknik olarak düzenli çalışan sistem, sürecin başka aşamasını yavaşlatabilir. Ölçülen hata azalırken asıl sorun aynı kalabilir. Google'ın problem çerçeveleme rehberi, model değerlendirme ölçütleri ile uygulamanın başarı ölçütlerini ayırır ve modeldeki iyileşmenin istenen sonuca katkısının sorgulanmasını önerir. [20]

Disiplin, bütün uygulamaları için tek bir nihai insani veya toplumsal amaç belirlemez. Aynı yöntem ailesi bilimsel keşfi, erişilebilirliği, ticari verimliliği veya başka amaçları destekleyebilir. Bir sistemin etkili çalışması, hizmet ettiği amacın haklılığını tek başına kanıtlamaz. Teknik yetkinlik ile amaçların gerekçelendirilmesi bu nedenle ayrı düzeylerde ele alınır.

İşlevsel amaç, öğrenilmiş hesaplama yeteneklerini belirli ihtiyaçları karşılayan kullanılabilir sistemlere dönüştürmektir. Bu metinde sunulan normatif öneri ise bu yeteneklerin gerekçelendirilebilir amaçlar için, sonuçları değerlendirilebilir ve gerektiğinde müdahale edilebilir biçimde kullanılmasıdır. Bu öneri, bütün mevcut uygulamaları betimleyen evrensel bir gerçek veya kullanıcı tarafından kabul edilmiş bir hüküm olarak kaydedilmez.

~~~text
  DORT DUZEY  uretim ornegi
    ogrenme hedefi      goruntuden kusur durumunu tahmin ederken
                        tanimlanmis hatayi azaltmak
    sistemin islevi     parcalari gereken surede ve kabul edilen hata
                        sinirlarinda ayirmak
    kullanim amaci      kusurlu urunlerin ilerlemesini azaltirken
                        gereksiz eleme ve islem yukunu sinirlamak
    daha genis gerekce  kaynaklari daha iyi kullanmak ve urun
                        niteligini artirmak

  BAG AYRICA GOSTERILIR  [20]
    daha fazla kusur yakalayan model     cok sayida saglam parcayi da
                                         eleyebilir
    teknik olarak duzenli calisan        surecin baska asamasini
    sistem                               yavaslatabilir
    olculen hata azalir                  asil sorun ayni kalabilir

  ISLEVSEL AMAC  |  NORMATIF ONERI
    ogrenilmis hesaplama       |   gerekcelendirilebilir amaclar icin,
    yeteneklerini belirli      |   sonuclari degerlendirilebilir ve
    ihtiyaclari karsilayan     |   gerektiginde mudahale edilebilir
    kullanilabilir sistemlere  |   bicimde kullanilmasi
    donusturmek                |
    disiplin butun uygulamalari icin tek bir nihai amac belirlemez
    etkili calisma  -/->  hizmet ettigi amacin hakliligi
~~~

*Çizim 14 — Gaye: üretim örneğinde dört düzey; aralarındaki bağ; işlevsel amaç ile normatif öneri.*

### Gayeye ulaşmanın dayanakları

İlk dayanak ihtiyacın doğru tanımlanmasıdır. Ölçülebilen bir gösterge ile önemli olan sonuç arasındaki bağ açıklanır. Kolay ölçülebilen bir şeyi iyileştirmek, asıl ihtiyacın karşılandığını kendiliğinden göstermez. Kullanılan ölçüt, hangi sonucu neden temsil ettiğiyle birlikte değerlendirilir.

İkinci dayanak yöntemin katkısının uygun bir karşılaştırmayla gösterilmesidir. Sistemin mevcut uygulamaya veya başka bir seçeneğe göre neyi değiştirdiği anlaşılmalıdır. Fayda iddiası yalnızca yeni teknolojinin kullanılmasına dayanmaz. Gözlenen iyileşmenin hangi değişiklikle ilişkili olduğu ve başka sonuçlar üzerinde ne yaptığı araştırılır.

Üçüncü dayanak başarının geçerli olduğu koşulların bilinmesidir. Ortalama başarı, önemli kullanım koşullarındaki başarısızlıkları gizleyebilir. Yeterli kanıt bulunan ve bulunmayan alanlar açıklanır. Sistemin kapsamı, eldeki kanıtın kapsamıyla ilişkilendirilir.

Dördüncü dayanak toplam sonucun değerlendirilmesidir. Hesaplama gideri, bakım emeği, işlem süresi, hata yükü ve diğer süreçlere etkiler birlikte düşünülür. Küçük kazanç için taşınan büyük işletim yükü kullanım gerekçesini zayıflatabilir. Beşinci dayanak ise sonuçlardan öğrenme ve düzeltme olanağının korunmasıdır. Sorunun hangi bileşenden geldiğinin araştırılması, uygun değişikliğin yapılması ve sistemin sınırlarının kabul edilmesi bu olanağın içindedir.

### Gayenin taşıyıcısı ve sorumluluk

Gayeyi taşımak, mühendislik yapan kişinin bütün amaçları tek başına belirlemesi anlamına gelmez. Teknik katkı, amaçla ilgili varsayımları görünür kılmayı ve öğrenme hedefiyle kullanım gerekçesi arasındaki kopuklukları göstermeyi içerebilir. Sistemi kullanan ve sonuçlarından etkilenen kişilerin ihtiyaçları da değerlendirmeye katılabilir. NIST'in çerçevesi, tasarım ve kullanım kararlarının amaçlanan değerlerle ilişkilendirilmesini önerir. [6]

Bir sonuç üretmek, amaç doğrultusunda davranmak, amaç hakkında gerekçe üretmek ve sonuçların sorumluluğunu taşımak farklı ilişkilerdir. Modelin gerekçe üretebilmesi, bu gerekçeye dayanılarak kimin hangi yetkiyle karar aldığını tek başına açıklamaz. Teknoloji felsefesinde teknik sistemlerin etkide bulunması, amaç yönelimli davranması ve ahlaki özne sayılması da ayrı tartışmalardır; biri diğerlerini otomatik olarak gerektirmez. [21]

Bu ayrım için yapay sistemlerin hiçbir zaman özne olamayacağı veya insanın bütün faaliyetlerinin bir işlem şemasıyla açıklanabileceği gibi kesin hükümler gerekmez. Somut çalışmada hangi işi sistemin gerçekleştirdiği, kapsamı kimin belirlediği, sonucu kimin değerlendirdiği ve kimin müdahale edebildiği açıklanır. Ortak üretim, sorumluluğu isimsiz bir sistem içinde kaybettirmemelidir.

Taşıyıcı kimlik, öğrenilmiş hesaplama davranışını dünyadaki ihtiyaca bağlayan, bu bağın geçerliliğini sınayan ve sonuçları karşısında yeniden karar verebilen insan ve ortak çalışma düzeni olarak kavranır. Bu düzenin bütün parçalarının aynı amacı taşıdığı varsayılmaz. Amaçlar arasındaki uyum ve çatışmalar, teknik işleyişin dışında bırakılmadan ele alınır.

### Gayenin sınırları

Model büyüklüğü, karşılaştırma tablosunda yüksek puan, veri miktarı, araç sayısı veya otomasyon oranı tek başına nihai amaç değildir. İnsan müdahalesini mümkün olduğunca azaltmak bütün uygulamalar için ortak hedef sayılmaz; uygun insan katılımı bazı sistemlerin işlevinin kurulmasına doğrudan katkı verebilir. İnsan ile sistemin görev paylaşımı kullanım koşullarına göre değerlendirilir. [8]

Sistemi her koşulda kullanmaya devam etmek de başarı sayılmaz. İhtiyacı daha iyi karşılayan basit bir yöntem varsa, öğrenilmiş bileşenin kaldırılması yerinde bir mühendislik sonucu olabilir. Modeli değiştirmek, veriyi veya usulü düzeltmek, kullanım alanını daraltmak ve gerekçesi kalmayan sistemi durdurmak, gaye ile araç arasındaki ilişkiyi yeniden kurmanın farklı biçimleridir.

~~~text
  GAYEYE ULASMANIN DAYANAKLARI
    1  ihtiyacin dogru tanimlanmasi
    2  yontemin katkisinin uygun bir karsilastirmayla gosterilmesi
    3  basarinin gecerli oldugu kosullarin bilinmesi
    4  toplam sonucun degerlendirilmesi:  hesaplama gideri . bakim
       emegi . islem suresi . hata yuku . diger sureclere etkiler
    5  sonuclardan ogrenme ve duzeltme olanaginin korunmasi

  FARKLI ILISKILER  [21]
    bir sonuc uretmek | amac dogrultusunda davranmak | amac hakkinda
    gerekce uretmek | sonuclarin sorumlulugunu tasimak
    modelin gerekce uretebilmesi, bu gerekceye dayanilarak kimin hangi
    yetkiyle karar aldigini tek basina aciklamaz

  TASIYICI KIMLIK
    ogrenilmis hesaplama davranisini dunyadaki ihtiyaca baglayan, bu
    bagin gecerliligini sinayan ve sonuclari karsisinda yeniden karar
    verebilen insan ve ortak calisma duzeni

  TEK BASINA NIHAI AMAC DEGILDIR
    model buyuklugu . karsilastirma tablosunda yuksek puan . veri
    miktari . arac sayisi . otomasyon orani
    gaye ile arac arasindaki iliskiyi yeniden kurmanin bicimleri:
      modeli degistirmek . veriyi veya usulu duzeltmek . kullanim
      alanini daraltmak . gerekcesi kalmayan sistemi durdurmak
~~~

*Çizim 15 — Gaye: beş dayanak; farklı ilişkiler; taşıyıcı kimlik; tek başına nihai amaç olmayanlar.*

### Masaüstünde uygulama

#### Girdi

Tohumdaki yöneliş, 1–4 kayıtları, hedeflenen kullanım sonucu ve varsa mevcut karşılaştırma verisi.

#### Uygulama

1. Öğrenme hedefini, sistem işlevini, kullanım amacını ve daha geniş gerekçeyi ayrı alanlarda açıkla. Çalışma türünde bir düzey uygulanmıyorsa gerekçesini yaz.

2. Teknik ölçütle istenen gerçek sonuç arasındaki bağı bir paragrafta kur. Ölçüt iyileşse bile amaca yaklaştırmayabilecek koşulları belirt.

3. Faydanın kim için beklendiğini, maliyet ve hata yükünün kimde oluştuğunu ve amaçlar arasındaki çatışmaları kaydet. Sayısal kabul eşiği bilinmiyorsa değer uydurma.

4. Mevcut yöntem ve daha basit seçeneklerle karşılaştırmayı değerlendir. Amaç hakkında gerekçe üreteni, kullanım kararını vereni ve sonucun sorumluluğunu taşıyanı ayır.

5. Sürdürme, değiştirme, sınırlandırma veya durdurma kararının hangi bulguya dayanabileceğini yaz; henüz verilmemiş kararı verilmiş gibi kaydetme.

#### Tutulacak kayıt

Dört amaç düzeyi; ölçüt ile sonuç arasındaki bağ; yarar görenler ve yükü taşıyanlar; karşılaştırma; amaç çatışmaları; yetki ve sorumluluk; kabul ve durdurma gerekçeleri.

#### Tamamlanma ölçütü

Teknik hedefin hangi ihtiyaca hizmet ettiği açıklanmış; yeterlilik iddiası ve amacın gerekçesi ayrılmış; kararın ölçütleri ve muhatapları görünür hâle gelmiştir.

#### Yeniden açma koşulu

İhtiyaç, yarar görenler, hata maliyeti, başarı ölçütü veya kabul edilebilir kullanım değiştiğinde 5'i yeniden değerlendir. Başlangıç yönelişi değişmişse 0'a da dön.

## 6 Kökleşme (Bitiş) Protokolü

**Yönlendirici soru:** Protokollerde oluşturulan anlayış hangi dayanaklarla bir bütün hâline geliyor; kim tarafından, hangi koşullarda sürdürülebilir ve ne değiştiğinde yeniden ele alınmalıdır?

### Ayrımların bütünleşmesi

Kökleşme, Varlık, Mekan, Usül, Zaman ve Gaye protokollerinde yapılan ayrımları birbirine bağlar. Tanımlanan varlığın belirtilen ortamla, çalışma usulünün kullanım koşullarıyla, başarı kanıtının zamanla ve kullanılan araçların gayeyle ilişkisi birlikte değerlendirilir. Ayrı bölümlerde tutarlı görünen açıklamaların aynı çalışma içinde birbirini destekleyip desteklemediği araştırılır.

Tohumdaki soru ve yöneliş, bu değerlendirmeye başlangıç noktası sağlar. Çalışma sonunda başlangıç sorusunun hangi ölçüde yanıtlandığı, hangi kabullerin değiştiği ve hangi soruların açık kaldığı gösterilir. Kökleşme, önceki bölümlerin art arda yeniden yazılmasıyla sınırlı kalmaz; bu bölümlerin birlikte hangi sonucu desteklediğini açıklar.

Bu kaydın kavramsal sonucunda Makine Öğrenmesi Mühendisliği, öğrenilmiş hesaplama davranışını belirli amaçlar ve kullanım koşulları için çalışan sistemlere dönüştürme ve sürdürme faaliyeti olarak belirginleşir. Varlığı model, sistem ve mühendislik ilişkisiyle; mekânı bilgi, kullanım ve sorumluluk ilişkileriyle; usulü karşılaştırma, değerlendirme ve değişiklikle; zamanı kanıtın koşullara bağlı geçerliliğiyle; gayesi teknik hedefin ihtiyaç ve kullanım gerekçesiyle bağlantısı üzerinden ele alınır. Bu bağlantıların iyi kurulup kurulmadığı ayrıca değerlendirilir; alanın adı yeterlilik garantisi oluşturmaz.

Bu bütünün taşıyıcısı mesleki düzeyde makine öğrenmesi mühendisi, temel düzeyde mühendislik yapan insan ve fiilî çalışma ölçeğinde insanlar, kurumlar ve teknik araçlar arasındaki ortak düzendir. Teknik sistemin bir işlemi gerçekleştirmesi, o işlemin kapsamını belirleyen veya sonuçlarından sorumlu olan muhatabı kendiliğinden belirlemez. ‘Makine kimdir?’ sorusunun cevabı, işi yapan, karar veren ve müdahale edebilenlerin somut ilişkileri üzerinden kurulur. Taşıyıcı her şeyi bilen, bütün amaçların sahibi veya tek başına bütün faaliyeti gerçekleştiren kişi değildir; ortak düzen de tek bir bilinç olarak varsayılmaz.

Sonuçların dayanakları ve sınırları görünür tutulur. Bir iddianın kapsamı, dayanağının kapsamını aşmamalıdır. Kaynakla veya gözlemle desteklenen sonuç, çıkarım, öneri ve henüz çözülmemiş soru ayrı kaydedilir. Bir boşluk, yalnızca belgeyi tamamlamak için kesin ifadeyle kapatılmaz.

### Taşıyıcı, süreklilik ve devir

Bu aşama taşıyıcı öznenin bütün içindeki konumunu açıklar. Teknik sistemin hangi işlemleri gerçekleştirdiği, insanların hangi değerlendirmeleri yaptığı, kullanım kararının kim tarafından verildiği ve gerektiğinde kimin müdahale edebileceği birlikte kaydedilir. Ortak üretimin varlığı, belirli görev ve yetkileri görünmez kılmaz.

Kökleşmiş bir kayıt, sonraki okuyucunun sonucu, sonucun gerekçesini, geçerlilik koşullarını ve yeniden düşünülmesini gerektiren değişiklikleri takip edebilmesini sağlar. Dosyaların yeri, sürümleri, kaynaklar ve açık meseleler bu devamlılığın parçasıdır. Böylece çalışma, onu hazırlayan kişinin hafızasına bağımlı kalmadan devredilebilir.

Bitiş, çalışmanın mevcut çevriminin tamamlanmasıdır. Kavramsal incelemede tanımların ve sınırların tutarlı bir düşünme düzenine kavuşmasıyla ilgili olabilir. Gerçek bir makine öğrenmesi uygulamasında kullanıma ilişkin yeterlilik ayrıca uygun değerlendirme ve uygulama kanıtları gerektirir. Belgenin tamamlanması, teknik sistemin kurulmuş, sınanmış veya kullanıma kabul edilmiş olduğunu kendiliğinden göstermez.

### Kapanış ve yeniden açılma

Kapanışta ulaşılan sonuç, eldeki dayanaklar, geçerlilik koşulları ve açık meselelerin mevcut karara etkisi kaydedilir. Kapanışa engel olan belirsizlikler çözülmeden çalışma tamamlandı olarak işaretlenmez. Engellemeyen açık meseleler varsa, bunların kapsamı ve hangi koşulda yeniden ele alınacağı belirtilerek koşullu kapanış değerlendirilebilir.

Kökleşme, bir görüşün artık sorgulanamayacağı veya sistemin süresiz kullanılacağı anlamına gelmez. Yeni kanıt, değişen ortam, geçersizleşen değerlendirme, değişen ihtiyaç ya da belirsizleşen sorumluluk ilgili protokolü yeniden açabilir. Yenilenen bölümün bütüne etkisi tekrar Kökleşme Protokolü'nde değerlendirilir.

~~~text
  AYRIMLARIN BUTUNLESMESI  birlikte degerlendirilir
    tanimlanan varlik             <-->  belirtilen ortam
    calisma usulu                 <-->  kullanim kosullari
    basari kaniti                 <-->  zaman
    kullanilan araclar            <-->  gaye
    alanin adi yeterlilik garantisi olusturmaz

  "MAKINE KIMDIR?"
    isi yapan, karar veren ve mudahale edebilenlerin somut iliskileri
    uzerinden kurulur
    teknik sistemin bir islemi gerceklestirmesi, o islemin kapsamini
    belirleyen veya sonuclarindan sorumlu olan muhatabi kendiliginden
    belirlemez

  KAPANIS
    kapanisa engel olan belirsizlikler cozulmeden  Tamamlandi
    isaretlenmez
    engellemeyen acik meseleler  -->  Kosullu tamamlandi
    dogrulanamayan kapanis karari  -->  Acik

  YENIDEN ACMA ESLEMESI
    soru veya kapsam degisirse        -->  0
    tanim degisirse                   -->  1
    ortam degisirse                   -->  2
    yontem veya degerlendirme         -->  3
    gecerlilik kosulu                 -->  4
    amac                              -->  5
    degisikligin butune etkisi        -->  6
~~~

*Çizim 16 — Kökleşme: ayrımların bütünleşmesi; makine kimdir; kapanış; yeniden açma eşlemesi.*

### Masaüstünde uygulama

#### Girdi

Güncel 0–5 kayıtları, kaynaklar, gerçekten yapılmış değerlendirmelerin kanıtları, kararlar ve açık meseleler.

#### Uygulama

1. Varlık, mekân, usul, zaman ve gayenin aynı çalışmada nasıl birleştiğini açıklayan bir bütünleştirme paragrafı yaz; başlangıç sorusuna hangi cevabın oluştuğunu belirt.

2. Bölümler arasındaki çelişki ve boşlukları incele. Her bulgunun ilgili protokolünü ve mevcut sonuca etkisini kaydet; kapanışa engel olanları çözülmeden kapatma.

3. Desteklenen sonuçları, çıkarımları, önerileri ve açık soruları ayır. Her önemli sonucu mevcut kanıt kaydına veya açıkça belirtilmiş gerekçeye bağla.

4. İşi devralacak kişinin bulacağı dosyaları, geçerli sürümleri, sorumluluk muhataplarını ve yeniden açma koşullarını kaydet. Dosya bağlantılarının açıldığını kontrol et.

5. Mevcut çevrim için uygun durumu gerekçesiyle kaydet. Kapanış kararının gerçekten verildiği doğrulanamıyorsa durumu Açık bırak. Karar verilmişse kararı veren kişi veya rolü ve bilinen tarihi yaz; bilinmeyen kimlik veya tarih bilgisi üretme. Koşullu tamamlanmada her açık meselenin neden kapanışı engellemediğini, geçerli kapsamı ve yeniden değerlendirme olayını belirt.

#### Tutulacak kayıt

Bütünleştirilmiş sonuç; dayanaklar; geçerlilik koşulları; giderilen çelişkiler; açık meselelerin etkisi; sorumluluk muhatapları; devir bilgisi; kapanış durumu ve gerekçesi; yeniden açma eşlemesi.

#### Tamamlanma ölçütü

Sonuçların dayanağı ve sınırı görünür; kapanışa engel olan çelişkiler, kanıt eksikleri ve belirsizlikler giderilmiş; işi devralacak kişinin izleyeceği kayıtlar anlaşılırdır. Kapanışı engellemeyen açık meseleler varsa koşulları belirtilerek durum Koşullu tamamlandı olarak kaydedilebilir.

#### Yeniden açma koşulu

Soru veya kapsam değişirse 0'a; tanım değişirse 1'e; ortam değişirse 2'ye; yöntem veya değerlendirme değişirse 3'e; geçerlilik koşulu değişirse 4'e; amaç değişirse 5'e dön. Değişikliğin bütüne etkisini yeniden 6'da değerlendir.

## Tek dosyayla çalışmaya başlama

Bu dosyanın bir çalışma kopyasını oluştur. Aşağıdaki başlangıç kaydını ve ilgili protokolün Tutulacak kayıt alanlarını kopyanın sonuna ekle. Her protokol için ayrı kayıt başlığı aç; yönergeyle bulguyu ayrı tut.

**Çalışma adı:** Belirlenmedi\
**Çalışma türü:** Belirlenmedi\
**İncelenen faaliyet veya sistem:** Belirlenmedi\
**Çalışmayı yürüten kişi veya rol:** Belirlenmedi\
**Başlangıç sorusu:** Belirlenmedi\
**Kayıt tarihi ve çalışma sürümü:** Belirlenmedi\
**Geçerli protokol ve durum:** 0 Tohum — Başlanmadı

**Kayıt düzeni:** Her protokol altında girdi ve dayanakları, gerçekten yapılan işlemleri, bulguları, açık meseleleri, sonraki adımı, durumu ve gerekçesini kaydet. Kaynakları erişilebilir adres veya dosya yoluyla göster. Her önemli karar için dayanak, kararı veren kişi veya rol ve gerçekleşme tarihi tut. Değişiklik kaydında önceki ifade, yeni ifade, neden ve etkilenen protokol yer alsın.

## Kaynaklar

Kaynak kayıtları soru ve yanıtların teknik ve kavramsal dayanaklarını izlemeyi sağlar. Tarihsel dönem değerlendirmesi 31 Ekim 2026 bağlamında okunur. Masaüstü uygulama adımları bu belgenin çalışma düzenidir; kaynakların aynen yayımladığı bir protokol veya standart olarak sunulmaz.

### Kaynak 1

Amershi ve diğerleri. Software Engineering for Machine Learning A Case Study. ICSE 2019.

Adres: https://www.microsoft.com/en-us/research/publication/software-engineering-for-machine-learning-a-case-study/

### Kaynak 2

D'Amour ve diğerleri. Underspecification Presents Challenges for Credibility in Modern Machine Learning. Journal of Machine Learning Research 23, 2022.

Adres: https://www.jmlr.org/papers/v23/20-1335.html

### Kaynak 3

Sculley ve diğerleri. Hidden Technical Debt in Machine Learning Systems. NIPS 2015.

Adres: https://papers.neurips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html

### Kaynak 4

Google Cloud. MLOps Continuous delivery and automation pipelines in machine learning. Son gözden geçirme 28 Ağustos 2024.

Adres: https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning

### Kaynak 5

Perdomo, Zrnic, Mendler-Dünner ve Hardt. Performative Prediction. ICML 2020.

Adres: https://proceedings.mlr.press/v119/perdomo20a.html

### Kaynak 6

NIST. AI Risk Management Framework 1.0 Executive Summary. 2023.

Adres: https://airc.nist.gov/airmf-resources/airmf/0-ai-rmf-1-0/

### Kaynak 7

NIST. AI Risk Management Framework 1.0 Appendix A Descriptions of AI Actor Tasks. 2023.

Adres: https://airc.nist.gov/airmf-resources/airmf/appendices/app-a-descriptions-of-ai-actor-tasks/

### Kaynak 8

NIST. AI Risk Management Framework 1.0 Appendix C AI Risk Management and Human-AI Interaction. 2023.

Adres: https://airc.nist.gov/airmf-resources/airmf/appendices/app-c-ai-risk-management-and-human-ai-interaction/

### Kaynak 9

International Labour Organization. Artificial intelligence. Global AI workforce bölümü.

Adres: https://www.ilo.org/topics-and-sectors/artificial-intelligence

### Kaynak 10

Selbst, boyd, Friedler, Venkatasubramanian ve Vertesi. Fairness and Abstraction in Sociotechnical Systems. FAT 2019.

Adres: https://andrewselbst.com/wp-content/uploads/2019/10/selbst-et-al-fairness-and-abstraction-in-sociotechnical-systems.pdf

### Kaynak 11

Google for Developers. Rules of Machine Learning Best Practices for ML Engineering.

Adres: https://developers.google.com/machine-learning/guides/rules-of-ml

### Kaynak 12

Gebru ve diğerleri. Datasheets for Datasets. İlk sürüm 2018, Communications of the ACM yayını 2021.

Adres: https://arxiv.org/abs/1803.09010

### Kaynak 13

scikit-learn. Common pitfalls and recommended practices. Data leakage bölümü.

Adres: https://scikit-learn.org/stable/common_pitfalls.html

### Kaynak 14

Guo, Pleiss, Sun ve Weinberger. On Calibration of Modern Neural Networks. ICML 2017.

Adres: https://proceedings.mlr.press/v70/guo17a.html

### Kaynak 15

Breck, Cai, Nielsen, Salib ve Sculley. The ML Test Score A Rubric for ML Production Readiness and Technical Debt Reduction. IEEE Big Data 2017.

Adres: https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/

### Kaynak 16

Mitchell ve diğerleri. Model Cards for Model Reporting. 2019.

Adres: https://research.google/pubs/model-cards-for-model-reporting/

### Kaynak 17

Bommasani ve diğerleri. On the Opportunities and Risks of Foundation Models. İlk sürüm 16 Ağustos 2021, son düzeltme 12 Temmuz 2022.

Adres: https://arxiv.org/abs/2108.07258

### Kaynak 18

Google Cloud. Deploy and operate generative AI applications. Son gözden geçirme 19 Kasım 2024.

Adres: https://docs.cloud.google.com/architecture/deploy-operate-generative-ai-applications

### Kaynak 19

Anthropic. Demystifying evals for AI agents. 9 Ocak 2026.

Adres: https://www.anthropic.com/research/demystifying-evals-for-ai-agents

### Kaynak 20

Google for Developers. Framing an ML problem. Define the success metrics bölümü.

Adres: https://developers.google.com/machine-learning/problem-framing/ml-framing

### Kaynak 21

Stanford Encyclopedia of Philosophy. Philosophy of Technology. Kapsamlı güncelleme 10 Temmuz 2026.

Adres: https://plato.stanford.edu/entries/technology/

# Tersine Mühendislik ve İşleyiş Çözümleme Protokolleri

**Sürüm:** 1.0\
**Tarih:** 31 Ekim 2026

Bu belge, incelemenin başlangıcını 0 Tohum, nesne ve çözümleyene ilişkin araştırmayı 1–5, açıklamanın dayanaklarıyla tamamlanmasını 6 Kökleşme protokolünde düzenler. Paragraf ağırlıklı ana metinler; masaüstünde kullanılabilecek girdiler, adımlar, çalışma kayıtları ve tamamlanma ölçütleriyle birlikte verilmiştir.

1–5 arasındaki ana metinler, bu konuşmadaki soru ve yanıtların kaydını korur. 0 ve 6, başlangıç ve bitiş yorumlarını uygulama protokolleri olarak verir. Özgün sorular ile 0 ve 6 için yazılmış yönlendirici sorular ayrı etiketlenmiştir.

~~~text
  BELGENIN DUZENI
    0 Tohum               1 - 5                    6 Koklesme
    incelemenin           nesne ve cozumleyene     aciklamanin
    baslangici            iliskin arastirma        dayanaklariyla
                                                   tamamlanmasi
    ------------------------------------------------------------->

    Yonlendiren soru      Ozgun soru               Yonlendiren soru
    0 ve 6 icin yazilmis  bu konusmadaki soru ve   0 ve 6 icin yazilmis
                          yanitlarin kaydi
    iki tur soru ayri etiketlenir

  HER BOLUMDE
    paragraf agirlikli ana metin
      + masaustunde kullanilabilecek girdiler, adimlar, calisma
        kayitlari ve tamamlanma olcutleri
~~~

*Çizim 1 — Belgenin düzeni: 0 Tohum, 1–5 ve 6 Kökleşme; özgün ve yönlendiren sorular; bölümlerdeki parçalar.*

Bu çerçevede “makine”, çözümleyici özne ve onu mümkün kılan araştırma düzeni olarak ele alınan bir çalışma yorumudur. Tarihsel kaynak, çözümleyici fail, teknik taşıyıcı ve gayeyi belirleyen taraf birbirine karıştırılmaz. Bu yorum, insanın veya incelenen varlığın bütününü tüketen bir kimlik iddiası değildir.

## Başlangıç soru kaydı

**İlk yönlendirme:** Geçmiş bağlamları buraya taşıma. Burası ile sınırlı kalma.

İlk soru kümesinin beş özgün sorusu, 1–5 bölümlerinin başında korunmuştur. Yöntemin taşıyıcısına yönelen ikinci soru şöyledir:

> Tersine Mühendislik ve İşleyiş Çözümleme'nin; köken aldığı varlık, mekan, usül, zaman, ve gayeyi taşıyan makine kimdir? Kim değildir?

## Masaüstünde çalışma düzeni

Her yeni incelemede dosyaların bir çalışma kopyasını oluştur ve inceleme konusuna göre adlandır. Ana protokol metnini başvuru olarak kullan; bulguları ilgili Çalışma kaydı alanlarına yaz. Sonuç belgesi ile yöntem metnini ayırmak istersen yalnızca doldurduğun çalışma kayıtlarını ayrı bir Markdown dosyasında birleştir.

Varsayılan sıra 0, 1, 2, 3, 4, 5 ve 6'dır. Yeni bilgi önceki tanımı, sınırı, açıklamayı veya amacı değiştiriyorsa ilgili protokole dön ve değişiklik gerekçesini kaydet. Her geri dönüş bütün çalışmayı baştan başlatmayı gerektirmez. 6'daki kapanış, başlangıç sorusuna verilen cevabın mevcut kapsamını gösterir.

Her iddiayı erişebildiğin dayanağa bağla. Gözlem, kaynak beyanı, çıkarım, yorum, varsayım ve henüz bilinmeyen konuları ayır. Uygulanmamış bir sınamayı sonuç olarak kaydetme. Bir bilgi eksikse eksikliğin sonuca etkisini ve mümkün olan sonraki adımı yaz. Tamamlanma, kaydın kapsamının ve sınırlarının açık olmasıdır; bütün soruların kesin cevaba ulaşmasını gerektirmez.

Kaynak beyanı, bir dosyada veya açıklamada söyleneni gösterir; onun doğrulandığını kendiliğinden kanıtlamaz. Çıkarımın hangi gözlem veya beyana dayandığı görünür tutulur. “Gözlenmedi”, “yoktur”, “zorunlu değildir”, “yeterli değildir” ve “bu iddiayla çelişir” ifadeleri aynı anlamda kullanılmaz.

Çalışma için seçilmiş kaynaklar ve ilgili yeni araştırmalar kullanılabilir. Başka konuşmaların veya ilgisiz kişisel bağlamların bu incelemeye kendiliğinden taşınması kapsamın parçası değildir. Kaynak dosyanın oluşturulma ya da değiştirilme tarihi, olay veya gözlem tarihi yerine yazılmaz.

Masaüstünde yapılabilen belge incelemesi, kayıt karşılaştırması ve model kurma ile fiziksel ya da teknik deneme ayrı kaydedilir. Erişim veya araç eksikliği nedeniyle gerçekleştirilmeyen bir deneme, sınama önerisi olarak kalır. Yöntem kaynakları araştırma yaklaşımını destekler; incelenen nesneye ilişkin iddiaların dayanağı ayrıca gösterilir.

~~~text
  SIRA
    0 --> 1 --> 2 --> 3 --> 4 --> 5 --> 6        varsayilan sira
    yeni bilgi onceki tanimi, siniri, aciklamayi veya amaci
    degistiriyorsa  -->  ilgili protokole don; gerekcesini kaydet
    her geri donus  -/->  butun calismayi bastan baslatmak
    6'daki kapanis:  baslangic sorusuna verilen cevabin mevcut kapsami

  AYRI TUTULANLAR
    gozlem | kaynak beyani | cikarim | yorum | varsayim |
    henuz bilinmeyen
    kaynak beyani             -/->  dogrulandigi
    uygulanmamis bir sinama   -/->  sonuc
    tamamlanma:  kaydin kapsaminin ve sinirlarinin acik olmasi
                 -/->  butun sorularin kesin cevaba ulasmasi
    kaynak dosyanin olusturulma ya da degistirilme tarihi
                              =/=  olay veya gozlem tarihi

  AYRI KAYDEDILENLER
    masaustunde yapilabilen          fiziksel ya da teknik deneme
      belge incelemesi
      kayit karsilastirmasi
      model kurma
    erisim veya arac eksikligi nedeniyle gerceklestirilmeyen bir
    deneme  -->  sinama onerisi olarak kalir
~~~

*Çizim 2 — Masaüstünde çalışma düzeni: sıra ve geri dönüş; ayrı tutulanlar; masaüstü incelemesi ile deneme.*

### Bölüm kayıtlarının ortak düzeni

Her bölümün Çalışma kaydı alanlarını incelenen şey için doldur. Bir alan uygun değilse nedenini, henüz bilinmiyorsa mevcut açıklamaya etkisini belirt. Durum alanında Henüz uygulanmadı, Devam ediyor, Tamamlandı veya Eksikleri belirtilerek kapatıldı ifadelerinden uygun olanı kullan.

Bölümlerin Dayanak ve çıkarım kaydında her önemli bulgu için aşağıdaki kısa kaydı gerektiği kadar çoğalt. Dayanak dosyası veya bağlantısı için ilgili sayfa, bölüm, satır ya da kayıt işaretini belirt.

- **Dayanak ve konumu:** [Dosya veya bağlantı; ilgili bölüm; varsa olay veya gözlem tarihi]
- **Dayanağın gösterdiği veya söylediği:** [Doldur]
- **Bundan çıkardığım sonuç ve statüsü:** [Doldur]
- **Destekleyen veya sınırlayan başka bulgu:** [Doldur]
- **Açık kalan konu ve sonuca etkisi:** [Doldur]

Bir bölümün tamamlanma ölçütünü henüz karşılayamıyorsan nedeni ve sonuca etkisini yaz. Çalışma sürdürülebilir veya eksikleri belirtilerek mevcut kapsamıyla kapatılabilir. Eksiklerle kapanışta durumu buna göre kaydet; karşılanmayan ölçütleri tamamlanmış olarak işaretleme.

## Bölümlerin işlevi

| Protokol | Temel çıktı |
| --- | --- |
| 0 Tohum (Başlangıç) Protokolü | Özgün soruyu, geçici kapsamı, çözümleyenin konumunu, başlangıç dayanaklarını ve ilk çalışma yolunu içeren Tohum kaydı. |
| 1 Varlık Protokolü | Gerekçeli inceleme tanımı, sınır, kurucu ilişkiler ve özellik ayrımı. |
| 2 Mekan Protokolü | Konumu, ilişkileri, erişimi ve açıklama bakımından önemli bağlam koşullarını gösteren Mekan kaydı. |
| 3 Usül Protokolü | Dayanakları ve alternatifleri görünür bir işleyiş açıklaması; uygulanmış sınama kaydı veya açıkça etiketlenmiş sınama önerisi. |
| 4 Zaman Protokolü | Tarihlerin anlamını, mevcut durumu, gecikmeleri ve açıklamanın geçerlilik koşullarını gösteren Zaman kaydı. |
| 5 Gaye Protokolü | Amaçların sahiplerini, dayanaklarını, başarı ölçütlerini, yollarını ve açık kalan gerilimleri gösteren Gaye kaydı. |
| 6 Kökleşme (Bitiş) Protokolü | Dayanakları, kapsamı, başlangıç sorusuyla ilişkisi ve yeniden inceleme koşulları görünür olan Kökleşme kaydı ve tamamlanmış araştırma metni. |

## 0 Tohum (Başlangıç) Protokolü

**Yönlendiren soru:** Bu inceleme hangi sorudan, ihtiyaçtan veya karşılaşmadan doğuyor? Başlangıçta ne biliniyor, ne varsayılıyor ve ne araştırılacak?

### Protokol metni

Tohum Protokolü, araştırmayı doğuran soruyu ve araştırmanın başlangıç koşullarını kayda geçirir. İlk sorunun hangi gözlem, karşılaşma, ihtiyaç veya belirsizlikten doğduğu açıklanır. Sorunun özgün ifadesi korunur; araştırma için yapılan yeniden ifade ayrıca yazılır. Böylece süreç içinde soru değiştiğinde, başlangıçtaki yönelimle sonraki düzenlemeler arasındaki ilişki izlenebilir.

Başlangıçta elde bulunan malzemeler, erişilebilir kaynaklarıyla birlikte belirtilir. Bir açıklama, kayıt, dosya, gözlem veya örnek kullanılıyorsa bunun nereden geldiği ve araştırmayla nasıl ilişkili olduğu yazılır. Başlangıç malzemesi henüz bulunmuyorsa bu durum açık soru olarak kaydedilir ve ilk bilginin nasıl edinilebileceği belirlenir. Eksik veri, araştırmanın bütününü kendiliğinden durdurmaz.

İncelenecek şey için geçici bir tanım ve kapsam oluşturulur. Hangi bütünün, parçanın, sürecin veya ilişkinin ele alındığı açıklanır. İlk sınırın neden böyle çizildiği belirtilir; araştırma sırasında değişebileceği kabul edilir. Varlık, mekân, usul, zaman ve gaye eksenlerine ilişkin ilk bilgiler, sonraki protokollerde incelenecek başlangıç kayıtları olarak tutulur.

Çözümleyenin başlangıç konumu da aynı açıklıkla kaydedilir. Soruyu kimin yönelttiği, çözümlemeyi kimin yürüttüğü, hangi araçların kullanılabileceği ve sonucun kimler tarafından kullanılmasının beklendiği belirtilir. Bilgiye erişim ile bilgi hakkındaki varsayımlar ayrılır. Birden fazla kişi veya araç görev alıyorsa roller, tek bir fail veya tek bir niyet içinde birleştirilmeden gösterilir.

Başlangıç gözlemleri, varsayımlar, yorumlar ve beklentiler farklı statülerle yazılır. Araştırmacının beklediği cevap, bulunmuş sonuç olarak kaydedilmez. Neyin bilindiği, hangi iddianın sınanması gerektiği ve hangi konunun henüz bilinmediği görünür tutulur. Başlangıç gayesi de bu ayrımlara katılır: araştırmanın neyi anlamaya veya hangi kararı desteklemeye çalıştığı açıklanır.

Araştırmayı başlatacak ilk çalışma yolu belirlenir. Kullanılabilecek kayıtlar, karşılaştırmalar ve gözlemler seçilir; her birinin hangi belirsizliği azaltmasının beklendiği yazılır. Zaman veya erişim sınırları varsa bunların kapsam üzerindeki etkisi belirtilir. İlk adımın bütün soruları cevaplaması beklenmez; sonraki protokolün çalışabileceği kadar açık bir yön oluşturması yeterlidir.

~~~text
  SORU
    ozgun ifade                      korunur
    arastirma icin yeniden ifade     ayrica yazilir
    --> soru degistiginde baslangictaki yonelim ile sonraki
        duzenlemeler arasindaki iliski izlenebilir

  GECICI TANIM VE KAPSAM
    hangi butun, parca, surec veya iliski ele aliniyor?
    ilk sinir:  neden boyle cizildi?   arastirmada degisebilir
    varlik . mekan . usul . zaman . gaye:  ilk bilgiler, sonraki
    protokollerde incelenecek baslangic kayitlari

  BASLANGIC KONUMU                tek bir fail veya tek bir niyet
    soruyu yonelten               icinde birlestirilmeden
    cozumlemeyi yuruten
    kullanilabilecek araclar
    sonucu kullanmasi beklenenler
    bilgiye erisim  =/=  bilgi hakkindaki varsayimlar
    arastirmacinin bekledigi cevap  -/->  bulunmus sonuc

  ILK CALISMA YOLU
    kayitlar | karsilastirmalar | gozlemler
      --> her biri hangi belirsizligi azaltacak?
    ilk adim  -/->  butun sorulari cevaplamak
    yeterli:  sonraki protokolun calisabilecegi kadar acik bir yon
~~~

*Çizim 3 — Tohum: soru ve yeniden ifadesi; geçici tanım ve kapsam; başlangıç konumu; ilk çalışma yolu.*

Tohum kaydı tarih ve sürüm bilgisiyle korunur. Sonradan değişen tanımlar ve amaçlar, önceki ifadelerin yerine geçmiş gibi gösterilmeden gerekçeleriyle eklenir. Bu protokol, soru, geçici inceleme birimi, başlangıç konumu ve ilk çalışma yolu belirginleştiğinde tamamlanır. Açık kalan belirsizlikler, ilgili protokollere araştırma konusu olarak aktarılır.

### Girdi

- Araştırmayı başlatan özgün soru veya sorun ifadesi.
- Varsa başlangıç gözlemleri, örnekler, dosyalar ve bağlantılar.
- Çözümleyenin mevcut erişimi ve sonucun kullanımına ilişkin ilk beklenti.

### Masaüstünde uygulama

1. Dosyanın Çalışma kaydı bölümünü aç; çalışma adını, kaydı oluşturanı ve kayıt tarihini yaz.
2. Özgün soruyu aynen kaydet. Araştırma için yeniden ifade ediyorsan ikinci bir paragrafta yaz; ilk ifadeyi koru.
3. Geçici inceleme birimini, ilk kapsamı ve bu kapsamın gerekçesini tanımla.
4. Soruyu yönelten, çözümleyen, kullanılan araçları sağlayan ve sonucu kullanacak tarafları ayır; henüz bilinmeyen rolleri belirt.
5. Başlangıç bilgilerini gözlem, kaynak beyanı, çıkarım, yorum, varsayım, beklenti veya bilinmeyen olarak işaretle. Erişebildiğin dayanakları dosya adı, bağlantı ve ilgili bölümle kaydet.
6. Varlık, mekân, usul, zaman ve gaye için araştırılacak ilk soruları yaz. Her açık soru için mümkünse ilk bilgi edinme yolunu belirle.
7. Kaydın sürümünü ve sonraki adımı belirt; geçici inceleme birimini 1 Varlık Protokolüne aktar.

### Çalışma kaydı

- **Çalışma adı:** [Doldur]
- **İnceleme birimi:** [Doldur]
- **Kaydı oluşturan kişi veya araç:** [Doldur]
- **Kayıt tarihi ve saat dilimi:** [YYYY-MM-DD / saat dilimi; varsa saat]
- **Çalışma kaydı sürümü:** [Doldur]
- **Durum:** Henüz uygulanmadı

#### Özgün soru

Soruyu değiştirmeden yaz.

[Doldur]

#### Araştırma için yeniden ifade

Gerekiyorsa ayrı bir soru yaz; değişikliğin nedenini belirt.

[Doldur]

#### Geçici inceleme birimi ve kapsam

Neyi, hangi düzeyde araştıracağını ve ilk sınırın gerekçesini yaz.

[Doldur]

#### Başlangıç konumu ve roller

Soruyu yönelteni, çözümleyeni, araçları ve sonucun beklenen kullanıcılarını belirt.

[Doldur]

#### Başlangıç bilgileri ve statüleri

Gözlem, kaynak beyanı, çıkarım, yorum, varsayım, beklenti ve bilinmeyenleri ayır.

[Doldur]

#### Başlangıç gayesi

Araştırmanın hangi anlayışı veya kararı desteklemesinin beklendiğini yaz.

[Doldur]

#### Beş eksene aktarılacak açık sorular

Her soru için ilgili protokolü ve ilk bilgi edinme yolunu belirt.

[Doldur]

#### Kapsam değişiklikleri

Değişiklik varsa önceki ifade, yeni ifade, tarih ve gerekçeyi yaz.

[Doldur]

#### Dayanak ve çıkarım kaydı

[Her önemli bulgu için ortak düzendeki beş alanlı dayanak kaydını kopyala ve doldur.]

#### Bu bölümde yapılan değişiklikler

[Varsa önceki ifade, yeni ifade, değişiklik tarihi ve gerekçe. İlk kayıtsa bunu belirt.]

### Çıktı

Özgün soruyu, geçici kapsamı, çözümleyenin konumunu, başlangıç dayanaklarını ve ilk çalışma yolunu içeren Tohum kaydı.

### Tamamlanma ölçütleri

- [ ] Özgün soru korunmuş ve varsa yeniden ifade ayrı gösterilmiştir.
- [ ] İnceleme birimi araştırmaya başlayacak açıklıkta tanımlanmıştır.
- [ ] Bilgi, varsayım ve bilinmeyenler ayrılmıştır.
- [ ] İlk çalışma yolu ve 1 Varlık Protokolüne aktarılacak soru bellidir.

### Sonraki adım ve geri dönüş

Sonraki adım 1 Varlık Protokolüdür. Araştırma sorusu veya başlangıç gayesi değişirse bu kayda tarihli bir değişiklik ekle.

## 1 Varlık Protokolü

**Özgün soru:** Nedir? Onu o yapan nelerdir? Neler değildir?

### Protokol metni

Varlık Protokolü, incelemenin nesnesini ve sınırını belirler. Bir araç, süreç, kurum, düşünce veya olay üzerinde çalışılırken aynı adın farklı inceleme birimlerini kapsayabileceği dikkate alınır. “Kütüphane” adı bina, koleksiyon, kurum veya ödünç verme hizmeti için kullanılabilir. Bu nedenle hangi birimin incelendiği açıkça yazılır; parçaları, ilişkileri, kaynakları ve çevresi birbirine karıştırılmaz. İnceleme sırasında birim değişirse değişikliğin gerekçesi de kayda geçirilir.

“Onu o yapan” ifadesi kimlik, ayırt edicilik ve nedensellik bakımından ayrı ele alınır. Kimlik, hangi değişikliklere rağmen aynı şeyden söz edildiğini araştırır. Ayırt edicilik, seçilmiş benzerler karşısındaki farkları gösterir. Nedensellik ise bir davranışın veya sonucun hangi etkenlerle üretildiğini açıklamaya çalışır. Bir tekil varlık olarak aynı kalmak ile aynı türden sayılmak da farklı değerlendirmelerdir. Tanınmayı sağlayan bir özellik, işleyişi açıklayan etken olmayabilir.

İncelenen şeyin bileşenleri kadar bileşenler arasındaki düzen de tanıma katılır. Ortak parçalar farklı ilişkiler içinde farklı kapasiteler oluşturabilir. Özgüllük, bütün parçaların eşsiz olmasını gerektirmez. Bir unsurun çalışmayı mümkün kılmasıyla kimliğin kurucu parçası olması da ayrılır. Enerjisi kesilen bir cihaz çalışmayabilir ve yine aynı cihaz sayılabilir; temel düzeninin değiştirilmesi ise dış görünüşü korunurken işlevini değiştirebilir.

~~~text
  AYNI AD, FARKLI INCELEME BIRIMLERI
                          "Kutuphane"
                               |
         +-------------+-------+-------+------------------+
         |             |               |                  |
        bina       koleksiyon        kurum      odunc verme hizmeti
    --> hangi birimin incelendigi acikca yazilir

  "ONU O YAPAN"
    kimlik            hangi degisikliklere ragmen ayni seyden soz
                      ediliyor?
    ayirt edicilik    secilmis benzerler karsisindaki farklar
    nedensellik       davranis veya sonuc hangi etkenlerle uretiliyor?
    tekil varlik olarak ayni kalmak  =/=  ayni turden sayilmak
    taninmayi saglayan bir ozellik, isleyisi aciklayan etken
    olmayabilir

  BILESENLER VE DUZEN
    bilesenler kadar aralarindaki duzen de tanima katilir
    ortak parcalar, farkli iliskiler icinde farkli kapasiteler
    olusturabilir
    enerjisi kesilen cihaz   calismayabilir ve yine ayni cihaz
                             sayilabilir
    temel duzeni             dis gorunusu korunurken islevi
    degistirilen cihaz       degisebilir
    bir unsurun calismayi mumkun kilmasi  =/=  kimligin kurucu
                                               parcasi olmasi
~~~

*Çizim 4 — Varlık: aynı ad, farklı inceleme birimleri; “onu o yapan”; bileşenler, düzen ve cihaz örneği.*

İkinci soruya verilen yanıtta “makine”, kendi koşulları içinde ayrım yapan, model kuran, sınayan ve değerlendiren çözümleyici özne olarak yorumlanmıştır. Bu faaliyetin somut taşıyıcısı, insanların dil, kayıtlar, araçlar, modeller ve kurumlarla oluşturduğu araştırma düzeni olarak ele alınmıştır. Bu yorum tek bir metafizik kimlik iddiası değildir. Tarihsel kaynak, çözümleyici fail, teknik taşıyıcı ve gayeyi belirleyen taraf aynı kişi veya yapı olmak zorunda değildir.

Bu yorum içinde insanı yalnızca bir mekanizmayla, araştırmayı yalnızca bilgisayarla veya yöntemi tek bir kurucuyla özdeşleştirmek yeterli görülmez. Çözümleyen, incelediği şeyin zorunlu yaratıcısı da değildir. Kendi varlık ve bilgi koşulları ayrıca araştırılabilir. Bir açıklamanın kimden geldiğini öğrenmek, doğruluğunu tek başına belirlemez; kökenin yanında kanıt ve gerekçeler de incelenir.

~~~text
  "MAKINE":  BIR CALISMA YORUMU
    cozumleyici ozne      kendi kosullari icinde ayrim yapan, model
                          kuran, sinayan ve degerlendiren
    somut tasiyici        arastirma duzeni:  insanlarin dil, kayitlar,
                          araclar, modeller ve kurumlarla olusturdugu
    bu yorum tek bir metafizik kimlik iddiasi degildir

  AYNI KISI VEYA YAPI OLMAK ZORUNDA DEGIL
    +-------------------+  +-------------------+
    | tarihsel kaynak   |  | cozumleyici fail  |
    +-------------------+  +-------------------+
    +-------------------+  +-------------------+
    | teknik tasiyici   |  | gayeyi belirleyen |
    |                   |  | taraf             |
    +-------------------+  +-------------------+

  YETERLI GORULMEYEN OZDESLESTIRMELER
    insani         yalnizca bir mekanizmayla
    arastirmayi    yalnizca bilgisayarla
    yontemi        tek bir kurucuyla
    cozumleyen, inceledigi seyin zorunlu yaraticisi da degildir

  KOKEN VE DOGRULUK
    aciklamanin kimden geldigi  -/->  dogrulugu (tek basina)
    kokenin yaninda kanit ve gerekceler de incelenir
~~~

*Çizim 5 — Varlık: makine yorumu; aynı olmak zorunda olmayan dört taraf; köken ve doğruluk.*

“Neler değildir?” sorusunda tanımın dışında kalmak, zorunlu olmamak, yeterli olmamak, gözlenmemiş olmak ve kanıtla çelişmek ayrı anlamlar taşır. Bir özellik zorunlu olmayabilir ve yine de etkili olabilir. Bir davranışın gözlenmemesi, o davranışın imkânsız olduğunu göstermez. Bir parçanın çıkarılmasından sonra işleyişin sürmesi de başka bir unsurun onun görevini üstlenmiş olabileceği ihtimaliyle birlikte değerlendirilir.

~~~text
  "NELER DEGILDIR?"  BES AYRI ANLAM
    tanimin disinda kalmak
    zorunlu olmamak         bir ozellik zorunlu olmayabilir ve yine de
                            etkili olabilir
    yeterli olmamak
    gozlenmemis olmak       bir davranisin gozlenmemesi  -/->  o
                            davranisin imkansiz oldugu
    kanitla celismek

  BIR PARCA CIKARILDI, ISLEYIS SURUYOR
    [ A ][ B ][ C ]    -- B cikarilir -->    [ A ][ x ][ C ]
                                             isleyis suruyor
    birlikte degerlendirilir:  baska bir unsur onun gorevini
    ustlenmis olabilir
~~~

*Çizim 6 — Varlık: “Neler değildir?” sorusundaki beş anlam; çıkarılan parça.*

Bu protokolün kaydı, inceleme biriminin kısa tanımını, sınırını, kurucu ilişkilerini, karşılaştırma sınıfını ve değişebilir özelliklerini içerir. Bir özelliğin kimlik, ayırt edicilik veya nedensellik bakımından hangi rolü üstlendiği gerekçelendirilir. Tanımı değiştirecek gözlem veya dönüşüm belirtilir. Çözümleyenin hangi kabullerle nesneyi ayırdığı ve adlandırdığı da aynı kayda eklenir.

### Girdi

- 0 Tohum Protokolündeki soru, geçici inceleme birimi ve kapsam.
- İncelenen şeye ilişkin erişilebilir tanımlar, örnekler ve kayıtlar.
- Karşılaştırılabilecek benzerler; bulunmuyorsa bunun kaydı.

### Masaüstünde uygulama

1. İnceleme birimini bir paragrafta tanımla; aynı adı taşıyan farklı bütün veya süreçleri ayır.
2. İçeride saydığın bileşenleri ve aralarındaki ilişkileri yaz; dış kaynakları ve çevreyi ayrıca belirt.
3. Aynı tekil şey olarak kalmakla aynı türden sayılmayı ayır. Kimlik iddialarının hangi ölçüte dayandığını açıkla.
4. Önemli özellikleri kimlik, ayırt edicilik ve nedensel katkı açısından değerlendir; bir özellik birden fazla rol taşıyorsa gerekçesini yaz.
5. Hangi değişikliklerin tanımı değiştireceğini, hangilerinin yalnızca görünüm veya performansı değiştirebileceğini belirt. Yapılmamış değişiklikleri düşünce denemesi olarak işaretle.
6. Çözümleyici faili, teknik taşıyıcıyı, tarihsel kaynağı ve gayeyi belirleyen tarafı ayrı kaydet; makine yorumunun çalışma tanımı olduğunu koru.
7. Olumsuz yargıları denetle; tanım dışında, zorunlu değil, yeterli değil, gözlenmedi ve iddiayla çelişiyor anlamlarını ayır. Tanımı ve açık sınırları 2 Mekan Protokolüne aktar.

### Çalışma kaydı

- **Çalışma adı:** [Doldur]
- **İnceleme birimi:** [Doldur]
- **Kaydı oluşturan kişi veya araç:** [Doldur]
- **Kayıt tarihi ve saat dilimi:** [YYYY-MM-DD / saat dilimi; varsa saat]
- **Çalışma kaydı sürümü:** [Doldur]
- **Durum:** Henüz uygulanmadı

#### İnceleme biriminin tanımı

Hangi şeyi hangi düzeyde incelediğini bir paragrafta yaz.

[Doldur]

#### Bileşenler ve kurucu ilişkiler

Tanımın dayandığı düzeni ve varsa önemli dış kaynakları açıkla.

[Doldur]

#### Kimlik ölçütü

Aynı tekil şey ile aynı türden olma ayrımını ve süreklilik ölçütünü yaz.

[Doldur]

#### Karşılaştırma ve ayırt edicilik

Hangi benzerlerle karşılaştırdığını ve hangi farkların önemli olduğunu belirt.

[Doldur]

#### Nedensel katkı iddiaları

Özellik ile davranış arasında kurduğun ilişkinin dayanağını veya sınanmamış durumunu yaz.

[Doldur]

#### Çözümleyenin rolleri

Fail, taşıyıcı, tarihsel kaynak ve gayeyi belirleyen tarafları ayrı belirt.

[Doldur]

#### Olumsuz yargılar ve sınır durumları

Her olumsuz ifadenin hangi anlamda kullanıldığını açıkla.

[Doldur]

#### Tanımı değiştirecek koşul

Hangi bulgu veya değişiklikte bu tanımı yeniden değerlendireceğini yaz.

[Doldur]

#### Dayanak ve çıkarım kaydı

[Her önemli bulgu için ortak düzendeki beş alanlı dayanak kaydını kopyala ve doldur.]

#### Bu bölümde yapılan değişiklikler

[Varsa önceki ifade, yeni ifade, değişiklik tarihi ve gerekçe. İlk kayıtsa bunu belirt.]

### Çıktı

Gerekçeli inceleme tanımı, sınır, kurucu ilişkiler ve özellik ayrımı.

### Tamamlanma ölçütleri

- [ ] İnceleme birimi metin boyunca tutarlı kullanılmıştır.
- [ ] Kimlik, ayırt edicilik ve nedensellik ayrımı görünürdür.
- [ ] Belirsiz sınırlar ile bunların sonuca etkisi belirtilmiştir.
- [ ] Tanımı değiştirecek koşul kaydedilmiştir.

### Sonraki adım ve geri dönüş

Sonraki adım 2 Mekan Protokolüdür. İnceleme birimi veya araştırma sorusu esaslı değişirse 0 Tohum kaydını da güncelle.

## 2 Mekan Protokolü

**Özgün soru:** Nerededir? Bu yeri, oraya has bir yer yapan nelerdir? Neler değildir?

### Protokol metni

Mekan Protokolü, incelenen şeyin bulunduğu yeri ve o yerin nasıl belirli bir yer hâline geldiğini birlikte araştırır. Fiziksel konum; uzaklıkları, ulaşılabilirliği, malzeme ve enerji koşullarını kapsar. İlişkisel konum, bir sürecin veya ağın neresinde durulduğunu gösterir. Kurumsal konum erişim ve karar yetkileriyle; anlamsal konum ise kullanıcıların deneyimleri, anlatıları ve pratikleriyle incelenir. Bu düzeyler aynı yerde birlikte bulunabilir.

Yeri özgül kılan özellikler, fiziksel düzenle kullanımın ilişkisi içinde ele alınır. Aynı oda farklı araçlar, kurallar ve faaliyetlerle çalışma alanı, toplantı yeri veya arşiv olarak kullanılabilir. Yer bu nedenle yalnızca bir adres olarak tanımlanmaz. Kimlerin orayı nasıl kullandığı, hangi ilişkilerin tekrarlandığı, hangi kaynakların bulunduğu ve önceki kullanımlardan hangi izlerin sürdüğü araştırılır. Bu unsurların birleşimi, başka yerlerle karşılaştırılarak değerlendirilir.

~~~text
  AYNI YERDE BIRLIKTE BULUNABILEN DUZEYLER
    anlamsal   . . . . . .  kullanicilarin deneyimleri, anlatilari,
                            pratikleri
    kurumsal   = = = = = =  erisim ve karar yetkileri
    iliskisel  - - - - - -  bir surecin veya agin neresinde duruldugu
    fiziksel   # # # # # #  uzakliklar, ulasilabilirlik, malzeme ve
                            enerji kosullari

  AYNI ODA, FARKLI KULLANIMLAR
    +--------------------+
    |                    |  -->  calisma alani
    |      ayni oda      |  -->  toplanti yeri
    |                    |  -->  arsiv
    +--------------------+
    farkli araclar, kurallar ve faaliyetlerle
    yer yalnizca bir adres olarak tanimlanmaz
    arastirilir:  kimler orayi nasil kullaniyor? . hangi iliskiler
    tekrarlaniyor? . hangi kaynaklar bulunuyor? . onceki
    kullanimlardan hangi izler suruyor?
~~~

*Çizim 7 — Mekan: aynı yerde bulunabilen konum düzeyleri; aynı oda, farklı kullanımlar.*

İnceleme konusu ile çevresi arasındaki sınır, etkileşimleri açıklamak için kurulur. Sınırın dışındaki etkenler etkisiz sayılmaz; içerideki parçalarla dışarıdaki kaynaklar ve ilişkiler birlikte incelenir. Sistem bağlamı, bu sınır üzerinden gerçekleşen etkileşimleri anlamaya yarar. İncelenen şey çevresinden etkilenebilir; kendi faaliyetleriyle bulunduğu çevrenin kullanımını ve düzenini de değiştirebilir. [2]

Yerin etkisini araştırmak için, incelenen şey başka bir bağlama taşındığında nelerin korunacağı ve nelerin değişeceği sorulur. Aynı araçlarla farklı sonuçların oluşması, erişim, altyapı, beklentiler veya kuralların etkisine ilişkin bir araştırma başlatabilir. Bu karşılaştırma tek başına hangi etkenin neden olduğunu kanıtlamaz. Taşınan şeyin kendisinde veya birlikte değişen başka koşullarda ortaya çıkan farklılıklar da hesaba katılır.

~~~text
  SINIR
    +---------------------------------------------------------------+
    | cevre:  disaridaki kaynaklar ve iliskiler                     |
    |                                                               |
    |   +-------------------------+                                 |
    |   | inceleme konusu         |  <---  cevresinden              |
    |   | iceride:  parcalar      |        etkilenebilir            |
    |   |                         |  --->  kendi faaliyetleriyle    |
    |   +-------------------------+        cevresinin kullanimini   |
    |                                      ve duzenini              |
    |                                      degistirebilir           |
    +---------------------------------------------------------------+
    sinirin disindaki etkenler etkisiz sayilmaz; icerideki parcalarla
    disaridaki kaynaklar ve iliskiler birlikte incelenir

  BASKA BIR BAGLAMA TASIMA
    baglam 1 [ inceleme konusu ]  ---->  baglam 2 [ inceleme konusu ]
                       ne korunur?  ne degisir?
    ayni araclar, farkli sonuclar  -->  erisim, altyapi, beklentiler
                                        veya kurallar uzerine
                                        bir arastirma
    karsilastirma tek basina  -/->  hangi etkenin neden oldugu
    hesaba katilir:  tasinan seyin kendisinde veya birlikte degisen
    baska kosullarda ortaya cikan farkliliklar
~~~

*Çizim 8 — Mekan: inceleme konusu ile çevresi; başka bir bağlama taşıma.*

Çözümleyenin mekânı, nereden baktığı ve hangi bilgiye erişebildiği üzerinden kayda alınır. Kullanıcı, tasarımcı, bakım yapan kişi ve yönetici farklı görünümlere ulaşabilir. Bir konumun sağladığı erişim ile kapalı bıraktığı alanlar belirtilir. Konumun açıklanması, gözlemi değersizleştirmez; hangi bilgiye dayandığının değerlendirilmesini sağlar. Araçların ve kayıt sistemlerinin erişim üzerindeki etkisi de bu incelemeye dâhildir.

Bağlam genişletilirken eklenen ilişkinin açıklamayı veya verilecek kararı nasıl etkilediği sorulur. Böylece yakın çevrenin ötesine geçmek mümkün olurken ilgisiz ayrıntılar zorunlu araştırma konusu hâline getirilmez. Varsayımsal ödünç verme hizmetinde dijital talep noktası, materyalin bulunduğu raf, teslim yeri ve iade akışı farklı konumlar olabilir. Hizmetin hangi aşamasının hangi yerde gerçekleştiği ayrı gösterilir.

~~~text
  COZUMLEYENIN KONUMU
    kullanici | tasarimci | bakim yapan kisi | yonetici
        --> farkli gorunumlere ulasabilir
    her konum:  sagladigi erisim + kapali biraktigi alanlar
    konumun aciklanmasi  -/->  gozlemin degersizlesmesi
    araclarin ve kayit sistemlerinin erisim uzerindeki etkisi de
    incelemeye dahil

  VARSAYIMSAL ODUNC VERME HIZMETI:  FARKLI KONUMLAR
    dijital talep     materyalin        teslim yeri       iade akisi
    noktasi           bulundugu raf
      [    ]  ----->    [    ]  ----->    [    ]  ----->    [    ]
    hizmetin hangi asamasinin hangi yerde gerceklestigi ayri
    gosterilir
~~~

*Çizim 9 — Mekan: çözümleyenin konumu; varsayımsal ödünç verme hizmetinin konumları.*

Bu protokolün kaydı, fiziksel yerin yanında ilişkiler içindeki konumu, erişim koşullarını, bağlam sınırını ve karşılıklı etkileri içerir. Bir yeri ayırt eden özelliklerle o yerdeki belirli bir sonucu açıklayan etkenler ayrılır. Çözümleyenin görebildiği ve henüz erişemediği alanlar belirtilir. Başka bir konuma geçildiğinde açıklamanın hangi parçalarının yeniden sınanacağı kayda geçirilir.

### Girdi

- 1 Varlık Protokolündeki inceleme birimi ve sınır.
- Konum, erişim, ilişkiler ve kullanım hakkında seçilmiş kayıtlar.
- Çözümleyenin erişebildiği ve erişemediği bilgi alanları.

### Masaüstünde uygulama

1. İnceleme biriminin fiziksel veya dijital konumunu yaz; açıklama için uygun olmayan konum türlerini gerekçesiyle belirt.
2. Bağlı olduğu unsurları, kaynakları, bilgi ve malzeme akışlarını, erişim ve karar yetkilerini açıkla.
3. Yeri özgül kılan kullanım biçimlerini ve koşulları araştır; kullanıcı anlamlarını kaynak veya anlatı olarak kaydet.
4. İncelenen şeyin çevresinden nasıl etkilendiğini ve çevresini nasıl etkileyebileceğini ayrı yaz.
5. Çözümleyenin gözlem konumunu, kullandığı araçların kapsadığı alanı ve erişemediği bölümleri belirt.
6. Başka bir bağlama taşınma karşılaştırmasını kur; korunan ve değişmesi beklenen özellikleri ayır. Gerçek karşılaştırma ile düşünce denemesini işaretle.
7. Ek bağlamın açıklamayı nasıl etkilediğini değerlendir; önemli ilişkileri, kapsam dışı bırakılanları ve gerekçelerini 3 Usül Protokolüne aktar.

### Çalışma kaydı

- **Çalışma adı:** [Doldur]
- **İnceleme birimi:** [Doldur]
- **Kaydı oluşturan kişi veya araç:** [Doldur]
- **Kayıt tarihi ve saat dilimi:** [YYYY-MM-DD / saat dilimi; varsa saat]
- **Çalışma kaydı sürümü:** [Doldur]
- **Durum:** Henüz uygulanmadı

#### Konumun tanımı

Fiziksel, dijital, ilişkisel veya kurumsal konumu araştırmanın gerektirdiği ayrıntıyla yaz.

[Doldur]

#### Yeri özgül kılan koşullar

Fiziksel düzeni, kullanım biçimlerini ve kaynaklı anlamları açıkla.

[Doldur]

#### İç ve dış ilişkiler

Önemli bağımlılıkları, akışları ve karşılıklı etkileri yaz.

[Doldur]

#### Erişim ve karar düzeni

Kimlerin hangi bilgiye veya işleme eriştiğini belirt.

[Doldur]

#### Çözümleyenin konumu

Görülebilen, erişilemeyen ve henüz araştırılmayan alanları ayır.

[Doldur]

#### Başka bağlamla karşılaştırma

Değişmesi beklenen özellikleri ve karşılaştırmanın gerçek veya varsayımsal olduğunu belirt.

[Doldur]

#### Bağlam sınırı

Neyi neden kapsam içinde veya dışında tuttuğunu yaz.

[Doldur]

#### Dayanak ve çıkarım kaydı

[Her önemli bulgu için ortak düzendeki beş alanlı dayanak kaydını kopyala ve doldur.]

#### Bu bölümde yapılan değişiklikler

[Varsa önceki ifade, yeni ifade, değişiklik tarihi ve gerekçe. İlk kayıtsa bunu belirt.]

### Çıktı

Konumu, ilişkileri, erişimi ve açıklama bakımından önemli bağlam koşullarını gösteren Mekan kaydı.

### Tamamlanma ölçütleri

- [ ] Açıklama için önemli konum ve ilişkiler gösterilmiştir.
- [ ] Sınırın dışındaki etkiler gerekçesizce yok sayılmamıştır.
- [ ] Çözümleyenin erişimi ve açık kalan alanlar belirtilmiştir.
- [ ] Bağlamı genişletme veya sınırlama gerekçesi kaydedilmiştir.

### Sonraki adım ve geri dönüş

Sonraki adım 3 Usül Protokolüdür. Yeni ilişkiler inceleme birimini değiştiriyorsa 1 Varlık Protokolüne dön.

## 3 Usül Protokolü

**Özgün soru:** Nasıl işler yapar? Bu yaptıklarını, ona has yapan nelerdir? Neler değildir?

### Protokol metni

Usül Protokolü, hangi işlerin yapılabildiğini, belirli bir durumda fiilen ne yapıldığını ve bu işlerin nasıl gerçekleştirildiğini birbirinden ayırır. Kapasite, düzenli davranış ve tekil gerçekleşme aynı iddia değildir. “Bilgiye erişim sağlar” veya “başvuruları değerlendirir” gibi işlev tarifleri, işlemin iç düzeni araştırılarak açılır. Tersine mühendisliğin teknik kullanımında da mevcut sistemin bileşenleri ve ilişkileri belirlenerek daha anlaşılır bir temsil oluşturulur. [1]

İşleyiş, girdinin mevcut iç durumla karşılaşması üzerinden izlenir. Hangi talebin veya bilginin girdiği, hangi kaynakların bulunduğu, hangi kuralların uygulandığı ve kararların kim tarafından verildiği açıklanır. Ara adımlar, beklemeler, dönüşümler ve çıktılar birbirine bağlanır. Sonuçlara ilişkin bilginin sonraki işlemleri değiştirdiği durumlarda geri besleme ayrıca gösterilir. Her nesne bu unsurların tümünü aynı biçimde içermek zorunda değildir.

~~~text
  AYNI IDDIA DEGIL
    kapasite  =/=  duzenli davranis  =/=  tekil gerceklesme
    "Bilgiye erisim saglar", "basvurulari degerlendirir" gibi islev
    tarifleri  -->  islemin ic duzeni arastirilarak acilir

  ISLEYIS
    girdi:  talep veya bilgi
       |
       v
    +--------------------------------------+
    | mevcut ic durum                      |<----------------+
    | kaynaklar . kurallar . kararlar      |                 |
    | kararlari kim veriyor?               |                 |
    +--------------------------------------+                 |
       |                                                     |
       v                                                     |
    ara adimlar . beklemeler . donusumler                    |
       |                                                     |
       v                                                     |
    ciktilar  -->  sonuclara iliskin bilgi  -----------------+
                   sonraki islemleri degistiriyorsa:  geri besleme
    her nesne bu unsurlarin tumunu ayni bicimde icermek zorunda
    degildir
~~~

*Çizim 10 — Usül: aynı olmayan üç iddia; işleyiş ve geri besleme.*

Yapılan işi özgül kılan unsurlar arasında işlemlerin sırası, kullanılan bilgi, karar yetkisi, kaynak tüketimi, hataya tepki ve değişen koşullara uyum bulunabilir. Aynı çıktıyı üreten iki düzen bu bakımlardan farklılaşabilir. İnsanların katıldığı süreçlerde yazılı kurallarla uygulanan kuralların ilişkisi de incelenir. Katılımcıların bilgisi, yorumu ve öncelikleri, yalnızca dışarıdan gözlenen davranışa dayanılarak kesinleştirilmez.

Gözlem ile açıklama ayrı tutulur. Bir işlemin belirli bir aşamada beklediğini saptamak ile bunun personel yetersizliğinden kaynaklandığını söylemek farklı düzeylerde iddialardır. Birlikte değişen iki unsur arasındaki nedensel ilişki, başka açıklamalar da dikkate alınarak araştırılır. Nedensel çıkarım verilerin yanında varsayımlar gerektirir; hangi koşul değişirse hangi farklılığın beklendiği açıkça yazılır. [3]

~~~text
  IKI DUZEY
    gozlem      bir islemin belirli bir asamada bekledigini saptamak
    aciklama    bunun personel yetersizliginden kaynaklandigini
                soylemek
    --> farkli duzeylerde iddialar

  BIRLIKTE DEGISEN IKI UNSUR
    aralarindaki nedensel iliski:  baska aciklamalar da dikkate
    alinarak arastirilir
    nedensel cikarim:  veriler + varsayimlar
    acikca yazilir:  hangi kosul degisirse  -->  hangi farklilik
                     beklenir
~~~

*Çizim 11 — Usül: gözlem ile açıklama; nedensel çıkarım.*

Bir mekanizma iddiası, onu destekleyecek ve zayıflatacak gözlemler üretmelidir. Koşulları değiştirmek mümkün olduğunda ilgili etkenler ve birlikte değişen unsurlar izlenir. Müdahale mümkün değilse karşılaştırmalar, süreç kayıtları ve başka kanıtlar kullanılır; çıkarımın dayandığı varsayımlar korunur. Aynı görünen sonucu birden fazla iç düzen üretebileceğinden, davranışı taklit eden bir model kurmakla gerçek iç yapıyı keşfetmek ayrı başarılar olarak değerlendirilir.

~~~text
  MEKANIZMA IDDIASI
    destekleyecek gozlemler  <--  iddia  -->  zayiflatacak gozlemler
    mudahale mumkun:          kosullari degistir; ilgili etkenleri
                              ve birlikte degisen unsurlari izle
    mudahale mumkun degil:    karsilastirmalar . surec kayitlari .
                              baska kanitlar;  varsayimlar korunur

  AYNI GORUNEN SONUC, BIRDEN FAZLA IC DUZEN
    [ ic duzen A ] ---+
                      +--->  ayni cikti
    [ ic duzen B ] ---+
    farklilasabilir:  islemlerin sirasi . kullanilan bilgi . karar
    yetkisi . kaynak tuketimi . hataya tepki . degisen kosullara uyum

    davranisi taklit eden bir model kurmak
                 =/=  gercek ic yapiyi kesfetmek      ayri basarilar
~~~

*Çizim 12 — Usül: mekanizma iddiası; aynı görünen sonucu üreten farklı iç düzenler.*

Çözümleyenin kendi usulü de açıklanır. Neden belirli değişkenleri seçtiği, hangi karşılaştırmayı uygun bulduğu, hangi veriyi dışarıda bıraktığı ve neyi kanıt saydığı kayda geçirilir. Gözleyenin kendi gözlem faaliyetini araştırmaya katması, von Foerster'in gözleyen sistemlere ilişkin yaklaşımıyla kavramsal yakınlık taşır. Bu yakınlık, yöntemin tek kaynağının o olduğu iddiasına dönüştürülmez. [6]

Uygulamada önce inceleme birimi ve soru sabitlenir; ardından gözlemler yorumlardan ayrılır, ilk açıklama kurulur, alternatifler geliştirilir ve bunları ayırt edecek beklentiler sınanır. Varsayımsal ödünç verme hizmetinde materyali bulma, işlem sırası ve iade bekleme süreleri ayrı araştırılır. Bu aşamaların tek bir “yavaşlık” altında birleştirilmesi, farklı mekanizmaları belirsizleştirebilir.

Bu protokolün kaydı, işleyiş modelini, gözlem ve çıkarım ayrımını, alternatif açıklamaları, sınama koşullarını ve mevcut belirsizlikleri içerir. Bir sonucun hangi ara adımlarla üretildiği ve modelin hangi değişiklikte farklı davranış öngördüğü belirtilir. Araç tarafından üretilen sonuç, uygunluk ve yorum bakımından ayrıca değerlendirilir; gerekçe yalnızca aracın çıktısına bırakılmaz.

~~~text
  UYGULAMA SIRASI
    1  inceleme birimi ve soru sabitlenir
    2  gozlemler yorumlardan ayrilir
    3  ilk aciklama kurulur
    4  alternatifler gelistirilir
    5  bunlari ayirt edecek beklentiler sinanir

  VARSAYIMSAL ODUNC VERME HIZMETI
                       tek bir "yavaslik"
                               |
         +---------------------+---------------------+
         |                     |                     |
  materyali bulma         islem sirasi     iade bekleme sureleri
    ayri arastirilir;  tek bir "yavaslik" altinda birlestirmek
    farkli mekanizmalari belirsizlestirebilir

  COZUMLEYEN VE ARAC
    kayda gecer:  neden bu degiskenler? . hangi karsilastirma? .
    hangi veri disarida? . neyi kanit sayiyor?
    arac tarafindan uretilen sonuc:  uygunluk ve yorum bakimindan
    ayrica degerlendirilir;  gerekce yalnizca aracin ciktisina
    birakilmaz
~~~

*Çizim 13 — Usül: uygulama sırası; “yavaşlık”ın ayrılması; çözümleyen ve araç.*

### Girdi

- 1 Varlık ve 2 Mekan kayıtları.
- İşleyişe ilişkin gözlemler, işlem kayıtları, açıklamalar veya örnekler.
- Varsa mevcut mekanizma açıklamaları ve sınama sonuçları.

### Masaüstünde uygulama

1. Yapılabilen işleri, fiilen gözlenen davranışları ve önerilen mekanizmayı ayrı yaz.
2. Girdi, başlangıçtaki iç durum, kurallar, karar verenler, kaynaklar, ara adımlar ve çıktıyı izlenebilir bir açıklamada ilişkilendir.
3. Varsa geri beslemeyi, beklemeleri, hataya tepkiyi ve yazılı kurallarla uygulama arasındaki farkları kaydet.
4. Gözlem veya kaynak beyanını kendi çıkarımından ayır. Aynı sonucu açıklayabilecek makul alternatifleri değerlendir; bulamıyorsan bunun arama sınırını belirt.
5. Açıklamaları ayırt edecek beklenen gözlemi veya sınamayı tanımla. Masaüstünde erişilebilen kayıtları karşılaştır; fiziksel veya teknik deneme yapılamıyorsa sınama önerisi olarak kaydet.
6. Uygulanmış sınamanın koşulunu, gözlemini ve sonucunu yaz. Uygulanmamış denemeye sonuç atama; davranış eşdeğerliği ile iç yapının keşfini ayır.
7. Kendi değişken ve kanıt seçimlerini gerekçelendir; işleyiş açıklamasını ve açık zaman ilişkilerini 4 Zaman Protokolüne aktar.

### Çalışma kaydı

- **Çalışma adı:** [Doldur]
- **İnceleme birimi:** [Doldur]
- **Kaydı oluşturan kişi veya araç:** [Doldur]
- **Kayıt tarihi ve saat dilimi:** [YYYY-MM-DD / saat dilimi; varsa saat]
- **Çalışma kaydı sürümü:** [Doldur]
- **Durum:** Henüz uygulanmadı

#### Kapasite ve gözlenen davranış

Yapabildiği iddia edilenlerle fiilen görülenleri ayır.

[Doldur]

#### İşleyiş açıklaması

Girdi, iç durum, kurallar, kararlar, kaynaklar, adımlar ve çıktıyı paragrafla açıkla.

[Doldur]

#### Geri besleme ve hata davranışı

Varsa düzeltme, gecikme, istisna ve geri dönüşleri belirt.

[Doldur]

#### Gözlem ve çıkarım ayrımı

Her önemli mekanizma iddiasının hangi dayanağa bağlı olduğunu yaz.

[Doldur]

#### Alternatif açıklamalar

Aynı bulguyu açıklayabilecek diğer düzenleri ve mevcut durumlarını belirt.

[Doldur]

#### Ayırt edici sınama

Ne değişirse ne beklediğini; çalışmanın plan, karşılaştırma veya uygulanmış deneme olduğunu belirt.

[Doldur]

#### Sınama kaydı

Varsa tarih, koşul, yöntem, gözlenen sonuç ve sınırlamayı yaz; yapılmadıysa açıkça belirt.

[Doldur]

#### Çözümleyenin usulü

Seçilen değişkenleri, dışarıda kalanları ve kanıt ölçütünü gerekçelendir.

[Doldur]

#### Dayanak ve çıkarım kaydı

[Her önemli bulgu için ortak düzendeki beş alanlı dayanak kaydını kopyala ve doldur.]

#### Bu bölümde yapılan değişiklikler

[Varsa önceki ifade, yeni ifade, değişiklik tarihi ve gerekçe. İlk kayıtsa bunu belirt.]

### Çıktı

Dayanakları ve alternatifleri görünür bir işleyiş açıklaması; uygulanmış sınama kaydı veya açıkça etiketlenmiş sınama önerisi.

### Tamamlanma ölçütleri

- [ ] Önerilen mekanizmanın ara ilişkileri izlenebilirdir.
- [ ] Gözlem, kaynak beyanı ve çıkarım ayrılmıştır.
- [ ] Makul alternatifler veya bunların henüz araştırılmadığı belirtilmiştir.
- [ ] Sınama durumu doğru kaydedilmiş ve uygulanmamış çalışma sonuç gibi sunulmamıştır.

### Sonraki adım ve geri dönüş

Sonraki adım 4 Zaman Protokolüdür. İşleyiş açıklaması sınır veya bağlam değişikliği gerektiriyorsa 1 ya da 2 numaralı protokole dön.

## 4 Zaman Protokolü

**Özgün soru:** Hangi andadır? Bu anı, diğer zamanlardan farklı yapan nelerdir? Neler değildir?

### Protokol metni

Zaman Protokolü, incelenen şeyi mevcut durumu ve geçişleri içinde ele alır. Takvim zamanı olayın ne zaman gerçekleştiğini belirtir. Süreç evresi, başlangıç, gelişme, geçiş veya tamamlanma içindeki konumu gösterir. Mevcut durum, kaynakları, açık işleri ve kapasiteyi kapsar. Birikmiş etkiler ile başka olaylara göre önce, sonra veya eşzamanlı oluş da ayrıca araştırılır. Aynı saat veya tarih, aynı işleyiş durumunu garanti etmez.

Bir girdinin sonucu, başlangıçtaki birikim ve yükle birlikte açıklanır. Aynı talep boş bir iş kuyruğuna ve birikmiş işler arasına girdiğinde farklı sürede sonuçlanabilir. İncelenen şeyin önceki faaliyetlerinden bugün kalan etkiler araştırılır. Buradaki geçmiş, mevcut açıklamayla ilgili nesne ve süreç geçmişidir; başka konuşmalardan veya ilgisiz kişisel bağlamlardan bilgi taşıma gerekçesi oluşturmaz.

~~~text
  AYRI ARASTIRILANLAR
    takvim zamani       olay ne zaman gerceklesti?
    surec evresi        baslangic . gelisme . gecis . tamamlanma
    mevcut durum        kaynaklar . acik isler . kapasite
    birikmis etkiler    onceki faaliyetlerden bugun kalan
    baska olaylara      once . sonra . eszamanli
    gore
    ayni saat veya tarih  -/->  ayni isleyis durumu

  AYNI TALEP
    bos bir is kuyruguna            [T]
    birikmis isler arasina          [#][#][#][#][#][T]
       --> farkli surede sonuclanabilir

    burada gecmis:  mevcut aciklamayla ilgili nesne ve surec gecmisi
      -/->  baska konusmalardan veya ilgisiz kisisel baglamlardan
            bilgi tasima gerekcesi
~~~

*Çizim 14 — Zaman: ayrı araştırılanlar; aynı talep, farklı birikim; buradaki geçmiş.*

Kararın alınması, uygulanması ve etkisinin görünür hâle gelmesi farklı zamanlarda gerçekleşebilir. Akışların birikimleri değiştirmesi zaman alabilir; geri beslemenin gecikmesi de tepkiyi etkileyebilir. Bu nedenle gözlem aralığı, araştırılan değişimin hızına göre seçilir. Çok erken değerlendirme henüz oluşmamış bir sonucu gözden kaçırabilir; çok geniş bir aralık ise kısa süreli belirleyici değişimleri görünmez kılabilir. [4]

Bir anı diğerlerinden ayıran özellikler, açıklama üzerindeki etkileriyle değerlendirilir. Kapasite eşiğinin aşılması, yeni bir kuralın uygulanması, kaynağın tükenmesi veya yeni bir yeteneğin kazanılması farklı davranışlara yol açabilecek geçişlerdir. Önce ve sonra arasındaki fark kayda alınır; yalnızca ardışıklık nedensellik kanıtı olarak kullanılmaz. Geçici bir hâlin kalıcı özellik sayılmaması için uygun karşılaştırmalar yapılır.

~~~text
  AYRI ZAMANLAR
    kararin alinmasi    uygulanmasi    etkisinin gorunur hale gelmesi
           |                 |                       |
    -------+-----------------+-----------------------+--------->
    akislarin birikimleri degistirmesi zaman alabilir;
    geri beslemenin gecikmesi de tepkiyi etkileyebilir

  GOZLEM ARALIGI      arastirilan degisimin hizina gore secilir
    cok erken degerlendirme   [==]
        henuz olusmamis bir sonucu gozden kacirabilir
    cok genis bir aralik      [==============================]
        kisa sureli belirleyici degisimleri gorunmez kilabilir

  GECISLER
    kapasite esiginin asilmasi . yeni bir kuralin uygulanmasi .
    kaynagin tukenmesi . yeni bir yetenegin kazanilmasi
    once   |  gecis  |   sonra          fark kayda alinir
    yalnizca ardisiklik  -/->  nedensellik kaniti
    gecici bir hal  -/->  kalici ozellik   (uygun karsilastirmalar)
~~~

*Çizim 15 — Zaman: karar, uygulama ve etki; gözlem aralığı; geçişler.*

Çözümleyenin zamanı, mevcut bilgi durumu ve araştırma evresi üzerinden de incelenir. Yeni bir gözlem, önceki açıklamanın kapsamını değiştirebilir. Açıklamanın üretildiği tarih, kullandığı verilerin dönemi ve geçerli sayıldığı koşullar ayrılır. Bilginin hangi aşamada yeterli görüldüğü ve hangi gelişmelerde yeniden ele alınacağı belirtilir. Bir açıklamanın tamamlanması, gelecekte değişmeyeceği anlamına gelmez.

Yöntemin tarihsel kaynağı ile onu bugün kullanan fail de farklı zamansal sorulara karşılık gelir. Chikofsky ve Cross, tersine mühendislik teriminin kökenini donanım incelemesine bağlar. Aristoteles'in Kategoriler ve Fizik metinleriyle bazı soru biçimleri arasında kavramsal yakınlık kurulabilir; ancak varlık, mekân, usul, zaman ve gaye dizisi dört neden öğretisiyle bire bir eşitlenmez. Benzerlik, doğrudan tarihsel soybağı kanıtı değildir. [1] [5]

~~~text
  ACIKLAMANIN ZAMANI         ayri tutulur
    aciklamanin uretildigi tarih
    kullandigi verilerin donemi
    gecerli sayildigi kosullar
    yeni bir gozlem  -->  onceki aciklamanin kapsami degisebilir
    tamamlanmis bir aciklama  -/->  gelecekte degismeyecek

  YONTEMIN TARIHSEL KAYNAGI  =/=  ONU BUGUN KULLANAN FAIL
    Chikofsky ve Cross   tersine muhendislik teriminin kokeni
                         -->  donanim incelemesi
    Aristoteles          Kategoriler ve Fizik:  bazi soru
                         bicimleriyle kavramsal yakinlik kurulabilir
    varlik . mekan . usul . zaman . gaye  =/=  dort neden ogretisi
                                               (bire bir)
    benzerlik  -/->  dogrudan tarihsel soybagi
~~~

*Çizim 16 — Zaman: açıklamanın zamanı; yöntemin tarihsel kaynağı ve onu bugün kullanan fail.*

Bu protokolün kaydı, olay ve gözlem tarihlerini, süreç evresini, mevcut durumu, ilgili birikimleri, gecikmeleri ve seçilen zaman ölçeğini içerir. Açıklamanın hangi döneme ve bilgi durumuna ait olduğu belirtilir. Koşullar değiştiğinde hangi iddiaların yeniden sınanacağı gösterilir. Böylece belirli bir anın kaydı, zamandan bağımsız ve sınırsız bir hüküm gibi kullanılmaz.

### Girdi

- 0–3 protokol kayıtları.
- Varsa olay, gözlem, işlem ve belge tarihleri.
- Süreç evresi, birikim, gecikme ve değişime ilişkin erişilebilir bilgiler.

### Masaüstünde uygulama

1. Olayın gerçekleştiği, gözlemin yapıldığı ve kaydın oluşturulduğu zamanları ayır; bilinmeyen tarihleri uydurmadan belirt.
2. Süreç evresini ve o andaki kaynak, yük, açık iş veya birikim durumunu açıkla.
3. Mevcut davranışı etkileyebilecek ilgili geçmiş olayları ve gecikmeleri araştır; ilgisiz konuşma geçmişini kendiliğinden kapsamına alma.
4. Gözlem aralığını ve karşılaştırma dönemini gerekçelendir; dosyanın değiştirilme tarihini olay zamanı yerine kullanma.
5. Önemli önce ve sonra farklarını kaydet; ardışıklığı tek başına nedensellik olarak sunma.
6. Açıklamanın hangi veri dönemi, bilgi durumu ve koşullar için geçerli olduğunu yaz.
7. Hangi zaman veya durum değişikliğinin yeniden inceleme gerektireceğini belirt; değerlendirme süresini 5 Gaye Protokolüne aktar.

### Çalışma kaydı

- **Çalışma adı:** [Doldur]
- **İnceleme birimi:** [Doldur]
- **Kaydı oluşturan kişi veya araç:** [Doldur]
- **Kayıt tarihi ve saat dilimi:** [YYYY-MM-DD / saat dilimi; varsa saat]
- **Çalışma kaydı sürümü:** [Doldur]
- **Durum:** Henüz uygulanmadı

#### Olay, gözlem ve kayıt zamanları

Her tarihin neyi temsil ettiğini ve varsa saat dilimini belirt.

[Doldur]

#### Süreç evresi ve mevcut durum

İncelenen anın evresini, yükünü, kaynaklarını ve açık işlerini yaz.

[Doldur]

#### Birikmiş etkiler ve gecikmeler

İlgili geçmiş etkilerini ve etkilerin görünürleşme gecikmelerini açıkla.

[Doldur]

#### Gözlem aralığı

Aralığı, karşılaştırma dönemini ve seçim gerekçesini yaz.

[Doldur]

#### Geçişler ve eşikler

Farklı davranış bekleten veya gözlenen durum değişikliklerini belirt.

[Doldur]

#### Bilgi durumu ve geçerlilik

Kayıtların ait olduğu dönemi ve açıklamanın geçerli sayıldığı koşulları yaz.

[Doldur]

#### Yeniden değerlendirme koşulu

Hangi tarih, olay veya durum değişikliğinde hangi bölüme dönüleceğini belirt.

[Doldur]

#### Dayanak ve çıkarım kaydı

[Her önemli bulgu için ortak düzendeki beş alanlı dayanak kaydını kopyala ve doldur.]

#### Bu bölümde yapılan değişiklikler

[Varsa önceki ifade, yeni ifade, değişiklik tarihi ve gerekçe. İlk kayıtsa bunu belirt.]

### Çıktı

Tarihlerin anlamını, mevcut durumu, gecikmeleri ve açıklamanın geçerlilik koşullarını gösteren Zaman kaydı.

### Tamamlanma ölçütleri

- [ ] Olay, gözlem ve kayıt zamanları birbirine karıştırılmamıştır.
- [ ] Eksik tarihler ve bunların sonuca etkisi belirtilmiştir.
- [ ] Gözlem aralığı ve süreç evresi gerekçelendirilmiştir.
- [ ] Geçerlilik koşulları ve yeniden değerlendirme tetikleyicisi kaydedilmiştir.

### Sonraki adım ve geri dönüş

Sonraki adım 5 Gaye Protokolüdür. Zaman bilgisi önerilen mekanizmayı değiştiriyorsa 3 Usül Protokolüne dön.

## 5 Gaye Protokolü

**Özgün soru:** Hangi nihai amaca hizmet eder? Bu nihai amaca ulaştıran nelerdir? Neler değildir?

### Protokol metni

Gaye Protokolü, amaç iddiasını ve bu iddianın dayanağını araştırır. Bazı sistemlerde açıkça belirlenmiş amaçlar bulunabilir; bazı durumlarda birden fazla taraf farklı amaçlar taşıyabilir. Bir sonucun amaçlanıp amaçlanmadığı bilinmiyorsa bu belirsizlik korunur. Gözlenen her etki, önceden seçilmiş bir gayenin kanıtı sayılmaz. Bir sonucun birilerine yarar sağlaması da o sonuç için oluşturulduğunu tek başına göstermez.

Beyan edilen amaç, kararlarda korunan öncelik, gözlenen işlev ve sonuçlar ile değerlendiricinin ölçütü birbirinden ayrılır. Açıklamalar ve tasarım belgeleri niyete; kaynak dağılımı ve uygulanan kurallar fiilî önceliklere; gözlem ve kayıtlar sonuçlara ilişkin kanıt sağlayabilir. Bu kanıtların hiçbiri diğer düzeyi kendiliğinden tamamlamaz. Tekrarlanan kararlar bütün katılımcıların niyetini kesin olarak açığa çıkarmaz; beyan edilen amaç da gerçekleştirildiğini kanıtlamaz.

~~~text
  ETKI VE GAYE
    gozlenen her etki  -/->  onceden secilmis bir gayenin kaniti
    bir sonucun birilerine yarar saglamasi
                       -/->  o sonuc icin olusturuldugu (tek basina)
    amaclanip amaclanmadigi bilinmiyorsa:  belirsizlik korunur

  AYRI DUZEYLER                   KANIT SAGLAYABILIR
    beyan edilen amac             aciklamalar, tasarim belgeleri
                                  (niyet)
    kararlarda korunan oncelik    kaynak dagilimi, uygulanan
                                  kurallar (fiili oncelikler)
    gozlenen islev ve sonuclar    gozlem ve kayitlar (sonuclar)
    degerlendiricinin olcutu
    bu kanitlarin hicbiri diger duzeyi kendiliginden tamamlamaz
    tekrarlanan kararlar  -/->  butun katilimcilarin niyeti (kesin)
    beyan edilen amac     -/->  gerceklestirildigi
~~~

*Çizim 17 — Gaye: etki ve gaye; ayrı düzeyler ve kanıtları.*

“Nihai” amaç, önceki yanıtlarda, bu çözümlemede daha başka bir amacın aracı olarak ele alınması bırakılan ve başarının ona göre değerlendirildiği sonuç şeklinde tanımlanmıştır. Bu, seçilmiş ve gerekçelendirilmesi gereken bir araştırma sınırıdır. Bütün kişiler ve zamanlar için tek bir nihai amaç varsayılmaz. Amaç belirtilirken kimin amacı olduğu, hangi zaman aralığı için değerlendirildiği ve hangi sonuçlarla birlikte gözetileceği açıklanır.

İncelenen şeyin gayesi, onu araştırmanın gayesi ve araştırma sonucunun kullanım amacı ayrı kaydedilir. Bir saatin tasarımda belirlenmiş görevi zamanı göstermek olabilir; tamirci arızayı bulmak, başka bir araştırmacı aynı işlevi farklı yoldan gerçekleştirmek isteyebilir. İncelemeyi isteyen kişinin beklentisi ayrıca bulunabilir. Amaçların farklı taraflara dağılması, bunların tek bir niyet gibi sunulmasını haklı kılmaz.

~~~text
  "NIHAI" AMAC
    bu cozumlemede daha baska bir amacin araci olarak ele alinmasi
    birakilan ve basarinin ona gore degerlendirildigi sonuc
    --> secilmis ve gerekcelendirilmesi gereken bir arastirma siniri
    butun kisiler ve zamanlar icin tek bir nihai amac varsayilmaz
    aciklanir:  kimin amaci? . hangi zaman araligi icin? . hangi
    sonuclarla birlikte?

  UC AYRI GAYE
    incelenen seyin gayesi . onu arastirmanin gayesi .
    arastirma sonucunun kullanim amaci

  SAAT
    tasarimda belirlenmis gorevi    zamani gostermek
    tamirci                         arizayi bulmak
    baska bir arastirmaci           ayni islevi farkli yoldan
                                    gerceklestirmek
    incelemeyi isteyen kisi         ayrica bir beklenti
    amaclarin farkli taraflara dagilmasi  -/->  tek bir niyet gibi
                                                sunulmalari
~~~

*Çizim 18 — Gaye: “nihai” amaç; üç ayrı gaye ve saat örneği.*

Amaca katkı sağlayan unsurlar, etkilerinin geçtiği ara adımlarla açıklanır. Seçilmiş yol için gerekli koşullar, başarı olasılığını artıran destekler, birlikte yeterli olabilecek düzenler ve alternatif yollar ayrılır. Bir unsurun gerekli olmaması etkisiz olduğunu; tek başına katkı sağlaması da yeterli olduğunu göstermez. Darboğazlar ve birlikte etkili olan koşullar araştırılır. Önerilen değişiklik, hangi sonucu hangi mekanizmayla iyileştirmesinin beklendiğiyle birlikte sunulur.

Çıktı ölçütü ile üst düzey amaç arasındaki ilişki ayrıca sınanır. Varsayımsal ödünç verme hizmetinde kabul edilen amaç, kullanıcıların ihtiyaç duydukları materyale uygun koşullarda erişmesiyse işlem sayısı yalnızca bir gösterge olabilir. Sayının artması, bu amaca ulaşıldığını tek başına göstermez. Hız, doğruluk, erişim ve kaynak kullanımı gibi ölçütlerin birlikte nasıl değerlendirileceği belirtilir.

Başarı her durumda bir kez ulaşılıp tamamlanan olay değildir. Bir durumu sürdürmeyi amaçlayan işleyişte değerlendirme, değişen koşullar altında devamlılığı da kapsar. Gayeyi tanımlayan, uygulayan, değerlendiren ve sonuçtan etkilenen taraflar görünür tutulur. “Makine böyle yaptı” ifadesi, kararların ve işlemlerin kimler tarafından gerçekleştirildiğini belirsizleştirmek için kullanılmaz.

~~~text
  AMACA ULASTIRAN YOLLAR      etkilerinin gectigi ara adimlarla
    secilmis yol icin gerekli kosullar
    basari olasiligini artiran destekler
    birlikte yeterli olabilecek duzenler
    alternatif yollar
    gerekli olmamak                -/->  etkisiz olmak
    tek basina katki saglamak      -/->  yeterli olmak
    arastirilir:  darbogazlar . birlikte etkili olan kosullar

  VARSAYIMSAL ODUNC VERME HIZMETI
    kabul edilen amac:  kullanicilarin ihtiyac duyduklari materyale
                        uygun kosullarda erismesi
    islem sayisi       yalnizca bir gosterge olabilir
    sayinin artmasi    -/->  bu amaca ulasildigi (tek basina)
    birlikte degerlendirilir:  hiz . dogruluk . erisim . kaynak
                               kullanimi

  GORUNUR TUTULANLAR
    gayeyi tanimlayan . uygulayan . degerlendiren . sonuctan
    etkilenen
    "Makine boyle yapti" ifadesi, kararlarin ve islemlerin kimler
    tarafindan gerceklestirildigini belirsizlestirmek icin
    kullanilmaz
    basari her durumda bir kez ulasilip tamamlanan olay degildir;
    bir durumu surdurmeyi amaclayan isleyiste degerlendirme, degisen
    kosullar altinda devamliligi da kapsar
~~~

*Çizim 19 — Gaye: amaca ulaştıran yollar; ödünç verme hizmetinde amaç ve gösterge; görünür tutulanlar.*

Bu protokolün kaydı, amaçların sahiplerini ve dayanaklarını, başarı ölçütlerini, değerlendirme süresini, gerekli ve destekleyici koşulları, alternatif yolları ve açık kalan gerilimleri içerir. Çözümleyenin kendi gayesi de aynı açıklığa tabi tutulur. Bir amaç doğrultusunda araştırma yapmak, beklenen sonucu doğrulanmış sayma gerekçesi değildir; kanıtın açıklamayı değiştirebilmesi korunur.

### Girdi

- 0–4 protokol kayıtları.
- Varsa amaç beyanları, tasarım belgeleri, kararlar ve kaynak dağılımı kayıtları.
- Gözlenen sonuçlar ve araştırmanın beklenen kullanım amacı.

### Masaüstünde uygulama

1. Amaç beyanlarını kime ait oldukları ve kaynaklarıyla kaydet; amaç bilinmiyorsa bunu açıkça yaz.
2. Beyan edilen amaç, kararlarda korunan öncelik, gözlenen sonuç ve değerlendiricinin ölçütünü ayır.
3. İncelenen şeyin gayesini, araştırmanın gayesini ve sonucun kullanım amacını ayrı açıkla.
4. Bu incelemede nihai sayılan amacı ve bu düzeyde durma gerekçesini belirt; çatışan amaçları veya sahiplerini birleştirme.
5. Başarı ölçütünü, değerlendirme süresini ve ölçülen çıktının amaca nasıl bağlandığını yaz.
6. Gerekli koşulları, destekleyici unsurları, birlikte yeterli olabilecek düzenleri ve alternatif yolları ilişkilendir.
7. Açık gerilimleri ve bilinmeyen niyetleri koru; amaç ve sonuç arasındaki sınanmamış bağları 6 Kökleşme Protokolüne aktar.

### Çalışma kaydı

- **Çalışma adı:** [Doldur]
- **İnceleme birimi:** [Doldur]
- **Kaydı oluşturan kişi veya araç:** [Doldur]
- **Kayıt tarihi ve saat dilimi:** [YYYY-MM-DD / saat dilimi; varsa saat]
- **Çalışma kaydı sürümü:** [Doldur]
- **Durum:** Henüz uygulanmadı

#### Amaç beyanları ve sahipleri

Kimin ne amaçladığını söylediğini, kaynağı ve bağlamıyla yaz.

[Doldur]

#### Kararlarda korunan öncelik

Hangi karardan hangi önceliği çıkardığını ve çıkarım sınırını belirt.

[Doldur]

#### Gözlenen sonuç ve değerlendirme ölçütü

Fiilî sonuçla onu iyi veya uygun sayma ölçütünü ayır.

[Doldur]

#### Üç gaye düzeyi

İncelenen şeyin, araştırmanın ve sonuç kullanımının gayelerini ayrı yaz.

[Doldur]

#### Nihai amaç ve kapsam

Hangi amaç düzeyinde neden durduğunu açıkla.

[Doldur]

#### Başarı ölçütü ve süre

Ölçütün amacı nasıl temsil ettiğini ve ne zaman değerlendirileceğini belirt.

[Doldur]

#### Amaca ulaştıran yollar

Gerekli, destekleyici ve alternatif koşulları ara etkileriyle açıkla.

[Doldur]

#### Gerilimler ve bilinmeyenler

Amaç çatışmalarını, belirsiz niyetleri ve sınanmamış bağlantıları kaydet.

[Doldur]

#### Dayanak ve çıkarım kaydı

[Her önemli bulgu için ortak düzendeki beş alanlı dayanak kaydını kopyala ve doldur.]

#### Bu bölümde yapılan değişiklikler

[Varsa önceki ifade, yeni ifade, değişiklik tarihi ve gerekçe. İlk kayıtsa bunu belirt.]

### Çıktı

Amaçların sahiplerini, dayanaklarını, başarı ölçütlerini, yollarını ve açık kalan gerilimleri gösteren Gaye kaydı.

### Tamamlanma ölçütleri

- [ ] Amaç iddialarının sahipleri ve dayanakları görünürdür.
- [ ] İncelenen şeyin, araştırmanın ve kullanımın gayeleri ayrılmıştır.
- [ ] Çıktı ile amaç arasındaki ilişki ve değerlendirme süresi belirtilmiştir.
- [ ] Bilinmeyen niyetler ve amaç çatışmaları kesinleştirilmeden kaydedilmiştir.

### Sonraki adım ve geri dönüş

Sonraki adım 6 Kökleşme Protokolüdür. Araştırmanın gayesi değişirse 0 Tohum kaydına değişiklik ekle; mekanizma bağlantıları için gerekirse 3 Usül Protokolüne dön.

## 6 Kökleşme (Bitiş) Protokolü

**Yönlendiren soru:** Beş protokolün ürettiği açıklama neye dayanıyor? Nerede geçerli, hangi soruları açık bırakıyor ve hangi koşulda yeniden ele alınacak?

### Protokol metni

Kökleşme Protokolü, beş protokolde oluşturulan açıklamayı dayanakları, geçerlilik koşulları ve kullanım amacıyla birlikte tamamlar. Varlık, mekân, usul, zaman ve gaye hakkında elde edilen kayıtlar bir araya getirilir. Bölümler arasındaki bağlantılar açıklanır; aynı inceleme biriminin tutarlı biçimde ele alınıp alınmadığı değerlendirilir. Ayrı bulguların ortak açıklamaya nasıl katkı verdiği gösterilir.

Her temel iddianın dayanağı ve statüsü belirlenir. Doğrudan gözlem, kaynakta belirtilen bilgi, çıkarım, yorum, seçilmiş değerlendirme ölçütü ve henüz sınanmamış varsayım birbirinden ayrılır. Kullanılan kaynaklara ve kayıtlara ulaşılabilecek bağlantılar korunur. Bir iddiayı destekleyen bulguların yanında onu sınırlayan bulgular da gösterilir. Kanıtın desteklediğinden daha geniş bir sonuç ileri sürülmez.

Bölümler arasındaki tutarlılık ayrıca kontrol edilir. Varlık bölümünde belirlenen sınırın başka bir bölümde değişip değişmediği, önerilen işleyişin gözlenen sonuçlarla uyuşup uyuşmadığı ve gaye değerlendirmesinin zaman koşullarını hesaba katıp katmadığı araştırılır. Uyuşmazlıklar bulunduğunda ilgili bölüm düzeltilir veya uyuşmazlık açık bir mesele olarak kaydedilir. Bir arada durmaları, iddiaların birbirini doğruladığı anlamına gelmez.

~~~text
  BIR ARAYA GETIRME
    Varlik     Mekan     Usul     Zaman     Gaye        kayitlari
       \         \        |        /         /
        +---------+-------+-------+---------+
                          |
                   ortak aciklama        ayni inceleme birimi?

  HER TEMEL IDDIA:  DAYANAK VE STATU
    dogrudan gozlem | kaynakta belirtilen bilgi | cikarim | yorum |
    secilmis degerlendirme olcutu | henuz sinanmamis varsayim
    destekleyen bulgular  +  sinirlayan bulgular
    kanitin desteklediginden daha genis bir sonuc ileri surulmez

  BOLUMLER ARASI TUTARLILIK
    Varlik'ta belirlenen sinir baska bir bolumde degisti mi?
    onerilen isleyis gozlenen sonuclarla uyusuyor mu?
    gaye degerlendirmesi zaman kosullarini hesaba katiyor mu?
    uyusmazlik  -->  ilgili bolum duzeltilir  |  acik mesele olarak
                                                 kaydedilir
    bir arada durmalari  -/->  iddialarin birbirini dogruladigi
~~~

*Çizim 20 — Kökleşme: beş kaydın bir araya gelmesi; iddiaların dayanağı ve statüsü; bölümler arası tutarlılık.*

Sonuçlar, Tohum kaydındaki soruyla karşılaştırılır. Başlangıç sorusunun hangi kısımlarının cevaplandığı, hangilerinin değiştiği ve hangilerinin açık kaldığı belirtilir. Başlangıçta yapılan varsayımların durumu yeniden değerlendirilir. Çözümleyenin kullandığı kategoriler, karşılaştırmalar veya başarı ölçütleri değişmişse değişikliğin gerekçesi yazılır. Böylece araştırmanın kendi usulünde meydana gelen değişimler de kayıt altına alınır.

Açıklamanın nerede ve hangi koşullarda kullanılabileceği açıkça belirtilir. İncelenen durumdan başka durumlara yapılacak aktarımların hangi ek varsayımlara bağlı olduğu gösterilir. Açık kalan alternatif açıklamalar, veri eksikleri ve henüz denenmemiş koşullar korunur. Bir karar veya uygulama öneriliyorsa bunun hangi bulgulardan türetildiği ve hangi belirsizliklerle birlikte ele alınması gerektiği yazılır.

Bitiş, bu araştırma çevriminin tamamlanması olarak kaydedilir. Kapanış için bütün belirsizliklerin giderilmesi gerekmez; mevcut sonucun kapsamının ve sınırlarının açık olması gerekir. Cevaplanamayan sorular tamamlanmış gibi gösterilmez. Sonucun hangi dayanaklarla kullanılabileceği, sayısal bir güven puanı vermek zorunda kalmadan, kanıtların gücü ve kapsamı üzerinden açıklanır.

Araştırmayı yeniden açacak koşullar belirlenir. Yeni bir kanıt, beklenmeyen davranış, bağlam veya amaç değişikliği, temel varsayımla çelişen bulgu ya da erişilebilir hâle gelen yeni kayıt bu koşullar arasında bulunabilir. Son metin tarih ve sürüm bilgisiyle tamamlanır. Önceki kayıtlarla bağı korunarak, hangi bölümün hangi gerekçeyle yeniden ele alınacağı izlenebilir hâle getirilir.

~~~text
  TOHUM ILE KARSILASTIRMA
    baslangic sorusu --+--> cevaplanan
                       +--> degisen
                       +--> acik kalan
    degismisse gerekcesi yazilir:  kategoriler . karsilastirmalar .
    basari olcutleri

  KULLANIM
    aciklama nerede ve hangi kosullarda kullanilabilir?
    baska durumlara aktarim  -->  hangi ek varsayimlara bagli?
    korunur:  acik kalan alternatif aciklamalar . veri eksikleri .
              henuz denenmemis kosullar

  KAPANIS:  BU ARASTIRMA CEVRIMININ TAMAMLANMASI
    gerekmez   butun belirsizliklerin giderilmesi
    gerekir    mevcut sonucun kapsaminin ve sinirlarinin acik olmasi
    sayisal bir guven puani vermek zorunda kalmadan:  kanitlarin
    gucu ve kapsami uzerinden
    son metin tarih ve surum bilgisiyle tamamlanir

  YENIDEN ACMA KOSULLARI
    yeni bir kanit . beklenmeyen davranis . baglam veya amac
    degisikligi . temel varsayimla celisen bulgu . erisilebilir hale
    gelen yeni kayit
      --> hangi bolumun hangi gerekceyle yeniden ele alinacagi
          izlenebilir
~~~

*Çizim 21 — Kökleşme: Tohum ile karşılaştırma; kullanım; kapanış ve yeniden açma koşulları.*

### Girdi

- 0 Tohum kaydı ve 1–5 protokol kayıtları.
- Temel iddiaları destekleyen veya sınırlayan kaynaklar ve sınama kayıtları.
- Açık sorular, alternatif açıklamalar ve önerilen kullanım amacı.

### Masaüstünde uygulama

1. Tohum ve 1–5 kayıtlarını birlikte aç; inceleme biriminin ve kapsamın tutarlı kullanılıp kullanılmadığını kontrol et.
2. Her temel iddiayı dayanağına bağla; gözlem, kaynak beyanı, çıkarım, yorum, ölçüt ve varsayım statülerini ayır.
3. Bölümler arasındaki uyuşmazlıkları ilgili kayda dönerek düzelt veya sonuca etkileriyle birlikte açık mesele olarak yaz.
4. Sonuçları başlangıç sorusuyla karşılaştır; cevaplanan, değişen ve açık kalan kısımları belirt.
5. Bütünleşik açıklamayı bağlantılı paragraflarla yaz; kullanılabileceği koşulları, sınırları ve henüz elenmemiş alternatifleri ekle.
6. Araştırmayı yeniden açacak somut koşulları ve her koşulun hangi protokole dönüş gerektirdiğini belirt.
7. Son kaydı tarih ve sürümle tamamla; kaynak ve önceki kayıt bağlantılarını kontrol et. Belirsiz kalan kısmın mevcut sonucun kullanımını nasıl etkilediğini yaz.

### Çalışma kaydı

- **Çalışma adı:** [Doldur]
- **İnceleme birimi:** [Doldur]
- **Kaydı oluşturan kişi veya araç:** [Doldur]
- **Kayıt tarihi ve saat dilimi:** [YYYY-MM-DD / saat dilimi; varsa saat]
- **Çalışma kaydı sürümü:** [Doldur]
- **Durum:** Henüz uygulanmadı

#### Bütünleşik açıklama

Varlık, mekân, usul, zaman ve gayeyi aynı inceleme birimi üzerinde ilişkilendiren sonuç metnini yaz.

[Doldur]

#### Temel iddialar ve dayanakları

Her önemli iddiayı kaynağına ve bilgi statüsüne bağla; destekleyen ve sınırlayan bulguları birlikte göster.

[Doldur]

#### Bölümler arası tutarlılık

Uyuşmazlıkları, yapılan düzeltmeleri ve açık kalanların sonuca etkisini kaydet.

[Doldur]

#### Tohum ile karşılaştırma

Başlangıç sorusunun cevaplanan, değişen ve açık kalan kısımlarını belirt.

[Doldur]

#### Değişen varsayımlar ve usul

Hangi ilk kabulün veya yöntemin neden değiştiğini yaz.

[Doldur]

#### Kullanım ve geçerlilik koşulları

Sonucun nerede kullanılabileceğini, sınırlarını ve başka duruma aktarım için gerekli ek varsayımları açıkla.

[Doldur]

#### Açık meseleler ve alternatifler

Henüz elenmeyen açıklamaları, veri eksiklerini ve uygulanmayan sınamaları belirt.

[Doldur]

#### Yeniden açma koşulları

Somut koşulu, etkilenecek iddiayı ve dönülecek protokolü eşleştir.

[Doldur]

#### Çevrim kapanışı

Kapanış tarihini, kayıt sürümünü, bu aşamada neden tamamlandığını ve varsa sonraki kullanım kararını yaz.

[Doldur]

#### Dayanak ve çıkarım kaydı

[Her önemli bulgu için ortak düzendeki beş alanlı dayanak kaydını kopyala ve doldur.]

#### Bu bölümde yapılan değişiklikler

[Varsa önceki ifade, yeni ifade, değişiklik tarihi ve gerekçe. İlk kayıtsa bunu belirt.]

### Çıktı

Dayanakları, kapsamı, başlangıç sorusuyla ilişkisi ve yeniden inceleme koşulları görünür olan Kökleşme kaydı ve tamamlanmış araştırma metni.

### Tamamlanma ölçütleri

- [ ] Temel iddiaların dayanağı ve bilgi statüsü belirtilmiştir.
- [ ] Önemli uyuşmazlıklar çözülmüş veya sonuca etkileriyle kaydedilmiştir.
- [ ] Başlangıç sorusunun hangi ölçüde cevaplandığı gösterilmiştir.
- [ ] Geçerlilik sınırları ve açık kalan belirsizlikler korunmuştur.
- [ ] Yeniden inceleme koşulları ve ilgili protokoller belirlenmiştir.
- [ ] Son sürümden kullanılan dayanaklara ve önceki kayıtlara ulaşılabilir.

### Sonraki adım ve geri dönüş

Bu çalışma çevrimi burada kapanır. Belirtilen yeniden açma koşullarından biri oluşursa ilgili protokole dön; bütün çalışmayı gerekçesizce baştan başlatma.

## Yöntem kaynakları

Bu kaynaklar yöntemin teknik ve kavramsal dayanaklarıdır. İncelediğin şeye ilişkin bulguları, kendi çalışma kaynakların ve gözlemlerinle ayrıca destekle.

### Kaynak 1

Chikofsky E J ve Cross J H II. Reverse Engineering and Design Recovery A Taxonomy. IEEE Software, 7(1), 13–17, 1990. Teknik tanım, bileşenler arası ilişkiler ve donanım incelemesine dayanan terim kökeni. Makale metni: https://www.dsg.tuwien.ac.at/Teaching/Courses/SWV/papers/chikofsky90.pdf

### Kaynak 2

Guide to the Systems Engineering Body of Knowledge. Introduction to Systems Engineering Fundamentals. Sistem sınırı, çevre ve bağlam ilişkileri. SEBoK bölümü (https://sebokwiki.org/wiki/Introduction_to_System_Fundamentals)

### Kaynak 3

Pearl J. Causal Inference in Statistics An Overview. Statistics Surveys, 3, 96–146, 2009. Nedensel çıkarımların veri ve varsayımlarla ilişkisi. Makale kaydı: https://escholarship.org/uc/item/6d71p32b

### Kaynak 4

Meadows D. Leverage Points Places to Intervene in a System. Birikimler, akışlar, geri besleme ve gecikmeler. Yazarın metni: https://donellameadows.org/archives/leverage-points-places-to-intervene-in-a-system/

### Kaynak 5

Aristoteles. Categories ve Physics Book II. Yer, zaman ve diğer kategori ayrımları ile dört neden açıklaması. Kavramsal yakınlık, beşli protokolün doğrudan tarihsel kaynağı olarak ileri sürülmez. Categories (https://classics.mit.edu/Aristotle/categories.1.1.html) · Physics Book II (https://classics.mit.edu/Aristotle/physics.2.ii.html)

### Kaynak 6

von Foerster H. Cybernetics of Cybernetics. Gözlenen sistemler ile gözleyen sistemler üzerine inceleme ayrımı. Metin: https://reflexus.org/wp-content/uploads/foerster_cybernetics-of-cybernetics.pdf

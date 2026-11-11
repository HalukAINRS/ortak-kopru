# Tanıklık ve Emanet Aktarımı Mimarisi

**0–6 Masaüstü Uygulama Protokolleri**

**Sürüm:** 1.0\
**Tarih:** 31 Ekim 2026\
**Biçim:** UTF-8 Markdown\
**Kullanım:** Bir dosya yöneticisi ve metin düzenleyicisiyle yürütülebilen kayıt, bakım ve devir kılavuzu.

Tanıklık ve Emanet Aktarımı Mimarisi, tanık olunan bir gerçekliğin izlerini, anlamını ve ona ilişkin sorumlulukları; kaynaklarını, sınırlarını ve geçirdikleri değişimleri görünür tutarak başkalarının bakımına bırakabilen bir düzendir. Bu metin, mevcut soru-yanıt çerçevesini **Şahitlik Mimarisi — İlkeler ve Kavramsal Çerçeve** başlıklı metnin (Kaynak A) ilkeleriyle birleştirir. Tohum ve Kökleşme, diğer beş bölümle birlikte uygulanabilir protokoller olarak düzenlenmiştir.

Birinci elden tanık olma konumu devredilemez. Devredilebilen anlatı, iz, kayıt, bilgi, beceri ve bunlara ilişkin bakım sorumluluklarıdır. Kaynağa sadakat bir yükümlülüktür; kusursuz hafıza veya yanılmazlık iddiası değildir. Bu nedenle her protokol, kaynaktan gelenle taşıyıcının katkısını ayırır; bilinmeyeni doldurmaz ve yapılan müdahaleyi görünür tutar.

Bu dosya kılavuz ve şablondur. İşlem alanları, kabul beyanları ve kapanış alanları ancak karşılık gelen işlem gerçekten yapıldığında doldurulur. Dosyanın hazırlanmış olması, somut bir tanıklığın doğrulandığı veya bir emanetin devredildiği anlamına gelmez.

~~~text
   ILK TANIK                                         DEVRALAN
  .------------------.                          .------------------.
  | tanik olma       | - - - - - - x            |                  |
  | konumu           |   devredilemez           |                  |
  |                  |                          |                  |
  | anlati . iz .    |------------------------->| bakim            |
  | kayit . bilgi .  |   devredilebilir:        | sorumlulugu      |
  | beceri           |   bunlar ve bunlara      |                  |
  `------------------'   iliskin bakim          `------------------'
                         sorumluluklari

  HER PROTOKOLDE
    kaynaktan gelen ile tasiyicinin katkisi ayrilir
    bilinmeyen doldurulmaz
    yapilan mudahale gorunur tutulur

  kaynaga sadakat bir yukumluluktur;
  kusursuz hafiza ya da yanilmazlik iddiasi degildir

  BU DOSYA KILAVUZ VE SABLONDUR
    dosyanin hazirlanmis olmasi   -x->   bir tanikligin dogrulanmasi
    dosyanin hazirlanmis olmasi   -x->   bir emanetin devredilmesi
    alanlar, ancak karsilik gelen islem gercekten yapildiginda dolar
~~~

*Çizim 1 — Tanık olma konumu devredilemez; devredilen anlatı, iz, kayıt, bilgi, beceri ve bakım sorumluluğudur.*

## İçindekiler

- Masaüstünde kullanım ve ortak kayıt düzeni
- 0 Tohum (Başlangıç) Protokolü
- 1 Varlık Protokolü
- 2 Mekan Protokolü
- 3 Usül Protokolü
- 4 Zaman Protokolü
- 5 Gaye Protokolü
- 6 Kökleşme (Bitiş) Protokolü
- Doldurulabilir emanet kaydı
- Kaynak ilkelerinin birleştirilmesi
- Önceki soru-yanıt kaydı

## Masaüstünde kullanım ve ortak kayıt düzeni

### Roller ve taşıyıcının sınırı

Kaynak A'nın sorumlu özne ve canlı hafıza anlayışı, insanın kendi niyetini, çıkarını, korkusunu ve müdahalesini de sorgulamasını gerektirir. Önceki metindeki **emanetçi makine** adı ise burada teknik taşıma işlevini belirtir. Dosya sistemi veya yapay zekâ kaynakları saklayabilir, karşılaştırabilir ve düzenleyebilir; bu işlemler tek başına vicdani sorumluluğun devri sayılmaz. Yetki veren, işlem yapan ve sonuçların hesabını verecek insanlar ayrıca belirlenir.

| Rol | Görevi | Sınırı |
|---|---|---|
| İlk tanık | Bizzat karşılaştığı şeyi ve görüş alanının sınırlarını bildirir. | Görmediğini, başkasından duyduğunu veya yorumunu doğrudan gözlem diye sunamaz. |
| Kayıt ve bakım sorumlusu | Kaynakları, değişiklikleri, erişimi ve devam eden bakımı düzenler. | Kaynağın sahibi veya onun adına sınırsız konuşan kişi hâline gelmez. |
| İşlem yapan kişi | Kopyalama, yazıya geçirme, özetleme, çeviri ve düzeltmeleri gerçekleştirir. | Kendi katkısını ilk tanığın sözüne ekleyemez. |
| Teknik araç | İzin verilmiş saklama, işleme ve karşılaştırma işlemlerine aracılık eder. | İlk tanığın konumunu veya insanın hesap verme yükümlülüğünü üstlenmiş sayılmaz. |
| Devralan | Belirli bir kapsam ve amaçla bakım görevini kabul eder. | Kayıtları alması, içerikteki her iddiayı doğru bulduğu ya da bütün kullanım yetkilerini edindiği anlamına gelmez. |

Bir kişi birkaç rolü üstlenebilir; hangi işlemde hangi rolle hareket ettiği yine de yazılır. Bir kurum devralıyorsa bakımın yürütüleceği birim veya sorumlu kişi ve ulaşılabilir bir başvuru yolu belirtilir. Tanığın korunması gerekiyorsa çalışma kayıtlarında kimlik kodu kullanılabilir; gerçek kimliğe erişim ayrıca sınırlandırılır.

~~~text
                           EMANET
   ILK TANIK  ------->   .--------.   ------->   DEVRALAN
   bizzat                |        |              belirli bir kapsam
   karsilastigini        `--------'              ve amacla bakim
   ve gorus               ^  ^  ^                gorevini kabul eder
   alaninin               |  |  |
   sinirlarini            |  |  `---- TEKNIK ARAC
   bildirir               |  |        izin verilmis saklama, isleme
                          |  |        ve karsilastirmaya aracilik eder
                          |  `------- ISLEM YAPAN KISI
                          |           kopyalar, yaziya gecirir,
                          |           ozetler, cevirir, duzeltir
                          `---------- KAYIT VE BAKIM SORUMLUSU
                                      kaynaklari, degisiklikleri,
                                      erisimi ve bakimi duzenler

  DOSYA SISTEMI YA DA YAPAY ZEKA
    saklayabilir . karsilastirabilir . duzenleyebilir
    bu islemler tek basina vicdani sorumlulugun devri sayilmaz

  AYRICA BELIRLENIR
    yetki veren . islem yapan . sonuclarin hesabini verecek insanlar

  bir kisi birkac rolu ustlenebilir;
  hangi islemde hangi rolle hareket ettigi yine de yazilir
~~~

*Çizim 2 — Beş rol: ilk tanık, kayıt ve bakım sorumlusu, işlem yapan kişi, teknik araç, devralan.*

### İlk kurulum

1. Bu kılavuzu bilgisayarına indir ve bir Markdown düzenleyicisiyle ya da UTF-8 destekleyen düz metin düzenleyicisiyle aç. Kılavuzu başvuru nüshası olarak sakla.
2. Masaüstünde veya erişimini denetleyebildiğin başka bir yerel konumda `Taniklik_Emanet` klasörü oluştur. Her ayrı emanet için `EM-001` gibi bir alt klasör aç. Bu adlar örnektir; yeni kayıt için kullanılmamış bir kimlik seç.
3. Aşağıdaki çalışma yapısını oluştur. Doldurulabilir emanet kaydı şablonunu `Emanet_Kaydi.md` adlı yeni bir dosyaya kopyala. Yedi ayrı form açmak gerekmez.
4. Kaynak dosyaların çalışma için yetkili kopyalarını `kaynaklar` klasörüne koy. Özgün dosya adını, geldiği yeri ve varsa kaynak kimliğini envantere yaz. Bu protokol, erişilemeyen bir kaynağı edinme yetkisi vermez.
5. Klasörün başka kişilerce erişilip erişilmediğini ve otomatik bulut eşitlemesine dâhil olup olmadığını kontrol et. Yerel bir klasör adı, tek başına mahremiyet güvencesi değildir. İçeriğin erişim sınırlarını karşılayan konumu seç.

| Göreli yol | İçerik ve kullanım |
|---|---|
| `Emanet_Kaydi.md` | 0–6 bölümleri, kaynak envanteri, iddialar, zaman çizelgesi, işlem günlüğü ve kapanış kararı. |
| `kaynaklar/` | Değiştirilmeden korunan kaynak kopyaları. Düzenleme bu nüshaların üzerine yazılmaz. |
| `calisma/` | Yazıya geçirme, özet, çeviri ve diğer türetilmiş dosyalar. Sürümler ayrı adlarla tutulur. |
| `teslim/` | Yalnızca devir kapsamına alınmış son dosyalar ve devralanın okuyacağı kayıt nüshası. |

Dosya adlarında kısa ve taşınabilir bir düzen kullan: `EM-001_beyan_v001.md`, `EM-001_beyan_v002.md` gibi. Kayıt sorumlusu, izin verilmiş bir ikinci konumda gereken yedeği tutar ve dosyaların açılabildiğini denetler. Yedek konumu da erişim ve saklama sınırlarına dâhildir.

~~~text
  Taniklik_Emanet/             masaustunde ya da erisimini
    |                          denetleyebildigin baska bir yerel
    |                          konumda
    `-- EM-001/                her ayri emanet icin bir alt klasor
          |
          |-- Emanet_Kaydi.md  0-6 bolumleri, kaynak envanteri,
          |                    iddialar, zaman cizelgesi, islem
          |                    gunlugu, kapanis karari
          |                    (yedi ayri form gerekmez)
          |
          |-- kaynaklar/       degistirilmeden korunan kaynak kopyalari
          |
          |-- calisma/         yaziya gecirme, ozet, ceviri ve oteki
          |     EM-001_beyan_v001.md      turetilmis dosyalar;
          |     EM-001_beyan_v002.md      surumler ayri adlarla
          |
          `-- teslim/          yalnizca devir kapsamina alinmis son
                               dosyalar; devralanin okuyacagi
                               kayit nushasi

  adlar ornektir; yeni kayit icin kullanilmamis bir kimlik secilir

  YEREL BIR KLASOR ADI, TEK BASINA MAHREMIYET GUVENCESI DEGILDIR
    klasore baskalari erisebiliyor mu?
    otomatik bulut esitlemesine dahil mi?
    yedegin konumu da erisim ve saklama sinirlarina dahildir

  bu protokol, erisilemeyen bir kaynagi edinme yetkisi vermez
~~~

*Çizim 3 — Çalışma yapısı: her emanet için bir klasör, tek kayıt dosyası, üç alan.*

### Ortak yürütme kuralları

Her protokolde **yapan kişi, işlem tarihi, dayanak, karar, açık konu ve durum** kaydedilir. Durumlar `hazırlanıyor`, `beklemede`, `tamamlandı` veya `yeniden açıldı` olabilir. `Tamamlandı`, o bölümün işlem ölçütünün karşılandığını anlatır; hakikat hakkında son hüküm vermez.

Protokoller ilk kez 0'dan 6'ya yürütülür. Sonradan yeni kaynak, amaç veya taşıyıcı ortaya çıkarsa ilgili bölüme dönülür. Gerekli yetki ya da taşıma kapasitesi yoksa bölüm `beklemede` kalır; gerekçe, sorumlu kişi ve yeniden değerlendirme koşulu yazılır. Bir alanın bilinmemesi kaydı açmayı engellemez; paylaşım için gerekli bir koşulun belirsiz olması paylaşımı bekletir.

**Beyan**, içeriğin belirtilen biçimde ifade edilmesidir. **Ulaşma**, belirtilen alıcının dosyalara erişebilmesidir. **Devralma**, alıcının belirli bakım görevini ve sınırlarını kabul etmesidir. Bunlar ayrı kaydedilir. Bu kılavuzun indirilmesi veya doldurulması, kendi başına bir kişiye gönderim ya da yayımlama işlemi değildir.

~~~text
  UC AYRI SEY, UC AYRI KAYIT

    BEYAN  ----------->   ULASMA  ----------->   DEVRALMA
    icerik, belirtilen    belirtilen alici       alici, belirli bakim
    bicimde ifade         dosyalara              gorevini ve
    edilir                erisebilir             sinirlarini kabul eder

    bu kilavuzun indirilmesi ya da doldurulmasi, kendi basina
    bir kisiye gonderim ya da yayimlama islemi degildir

  HER PROTOKOLDE KAYDEDILIR
    yapan kisi . islem tarihi . dayanak . karar . acik konu . durum

  DURUMLAR
    hazirlaniyor | beklemede | tamamlandi | yeniden acildi

    "tamamlandi"  o bolumun islem olcutu karsilandi demektir;
                  hakikat hakkinda son hukum vermez

  BILINMEYEN NEYI DURDURUR?
    bir alanin bilinmemesi               kaydi acmayi engellemez
    paylasim icin gerekli bir kosulun
    belirsiz olmasi                      paylasimi bekletir
~~~

*Çizim 4 — Ortak kurallar: beyan, ulaşma ve devralma ayrı kaydedilir; dört durum.*

## 0 Tohum (Başlangıç) Protokolü

**Kurucu sorular:** Bu başlangıcı doğuran karşılaşma nedir? Neyin emaneti açılmaktadır? Kim, neyi, hangi sınırlarla üstlenmektedir?

### İlke ve sınır

Tohum, ilk temasın sorumluluk doğuran bir başlangıç olarak kaydedilmesidir. Kaynak A bunu şahidin doğuşu, görmemiş olma konumunun sona ermesi ve seyircilikten uyanık dikkate geçiş olarak anlatır. Masaüstü karşılığı, eldeki şeyin yalnızca tüketilecek bir görüntü veya anlatı sayılmayıp kaynağı ve bakımı gözetilecek bir emanet olarak ele alınmasıdır. Karşılaşma planlanmış da olabilir, beklenmedik de; başlangıcın değeri önceden seçilmiş olmasına bağlı değildir.

Başlangıçta varlık, mekân, usul, zaman ve gaye henüz bütün ayrıntılarıyla açıklanmamış olabilir. İlk niyet, bilinen sınırlar ve bilinmeyenler birlikte yazılır. Bir görüntünün kaydedilmiş olması veya bir dosyanın alınması tek başına birinci elden tanıklık doğurmaz. Başkasının anlatısı alınmışsa tohum, o anlatının bakımını üstlenmeye ilişkindir; anlatılan olayda bulunmuş olma iddiasına değil.

~~~text
  GELIS BICIMI                           TOHUM CUMLESI

    bizzat karsilasma            --.     "Sununla karsilastim /
    baskasindan alinan anlati    --|      su bana ulasti: ...
    belge ya da kayit            --+-->   Bunu su gerekceyle
    devralinan bakim gorevi      --|      korumayi ya da aktarmayi
    (ya da acikca ayrilmis       --'      ustleniyorum: ..."
     bir birlesim)

  ELDEKI SEY
    yalnizca tuketilecek bir goruntu ya da anlati sayilmaz;
    kaynagi ve bakimi gozetilecek bir emanet olarak ele alinir

  AYRI YAZILIR
    ne bilmiyorum | neyi gormedim | henuz neyi kabul etmedim
    kendi niyetim ve olasi cikarim

  TEK BASINA BIRINCI ELDEN TANIKLIK DOGURMAZ
    bir goruntunun kaydedilmis olmasi . bir dosyanin alinmasi

    baskasinin anlatisi alinmissa tohum, o anlatinin bakimini
    ustlenmeye iliskindir; anlatilan olayda bulunmus olma
    iddiasina degil

  karsilasma planlanmis da olabilir, beklenmedik de;
  baslangicin degeri onceden secilmis olmasina bagli degildir
~~~

*Çizim 5 — Tohum: geliş biçimi ve tohum cümlesi; neyin birinci elden tanıklık doğurmadığı.*

### Masaüstünde uygula

1. `Emanet_Kaydi.md` içinde kayıt kimliğini, kayıt sorumlusunu ve ilk temasın bilinen zamanını yaz.
2. Geliş biçimini belirt: `bizzat karşılaşma`, `başkasından alınan anlatı`, `belge veya kayıt`, `devralınan bakım görevi` ya da bunların açıkça ayrılmış bir birleşimi.
3. Tohum cümlesini doldur: **“Şununla karşılaştım / şu bana ulaştı: … Bunu şu gerekçeyle korumayı veya aktarmayı üstleniyorum: …”**
4. Ne bilmediğini, neyi görmediğini ve henüz neyi kabul etmediğini ayrı yaz. İlk kaynak dosyalarına kimlik ver; bulunmayan bir kaynağı varmış gibi listeleme.
5. Kendi niyetini ve olası çıkarını kaydet. İlk erişim sınırını belirle; paylaşım kararı henüz verilmediyse bunu açık bırak.

**Tutulacak kayıt:** Tohum cümlesi, geliş biçimi, ilk kaynaklar, sorumlu kişi, bilinmeyenler ve ilk sınırlar.

**Tamamlanma ölçütü:** Neyin bakımının açıldığı ve bu kaydın sorumlusunun kim olduğu anlaşılır. Eksik bilgi açıkça işaretlenmiştir. Başlangıç, elde olmayan bilgiyi tamamlanmış gibi göstermemektedir.

**Bekletme koşulu:** Emanetin konusu veya hangi işlemlerin üstlenilebileceği ayırt edilemiyorsa yalnızca sınırlı bir başlangıç kaydı tutulur; kapsam açıklığa kavuşmadan aktarım yapılmaz.

**Kaynak dayanağı:** Kaynak A'daki şahidin doğuşu anlatımı; önceki 0 Tohum yorumu.

## 1 Varlık Protokolü

**Kurucu sorular:** Nedir? Onu o yapan nelerdir? Neler değildir? Taşıyan kimdir, kim değildir?

### İlke ve sınır

Tanıklık belirli bir konumdan gelir; görüş alanı ve yanılma ihtimali vardır. Kaynak A'nın doğrudan hazır bulunma, uyanıklık, emanet bilinci ve sadakat ilkeleri burada kaynak türünün açıkça belirtilmesiyle uygulanır. İlk tanıkla anlatıyı devralan, teknik araçla sorumlu insan ve gözlemle yorum birbirine karıştırılmaz.

Şahit, gerçeği kendi çıkarına göre değiştirmeme sorumluluğunu üstlenir; söylentiyi doğrudan gözlem, niyet okumasını olgu veya kendi hükmünü olayın kendisi gibi sunamaz. Bu sınırlar, insanın kendi duygusunu inkâr etmesini veya yanılmazlık iddia etmesini gerektirmez. Makinenin kuruluş amacı da taşıdığı emanetin amacıyla aynı kabul edilmez. Araç veya onu işleten kişi, kaynağın sahibi değildir.

~~~text
  HER IFADE DORT TURDEN BIRIYLE AYRILIR

    GOZLEM | AKTARIM | YORUM | BILINMIYOR

    her iddianin dayanagi gosterilir:
      dosya . sayfa . kayit zamani . tanik ifadesi
    GOZLEM icin gozlemi kimin yaptigi belirtilir; teknik kayit
    kendiliginden insan tanikligi sayilmaz

  BIRI OTEKI GIBI SUNULAMAZ
    soylenti           -x->   dogrudan gozlem
    niyet okumasi      -x->   olgu
    kendi hukmu        -x->   olayin kendisi

  BIRBIRINE KARISTIRILMAZ
    ilk tanik                    |   anlatiyi devralan
    teknik arac                  |   sorumlu insan
    gozlem                       |   yorum
    kaydi korumak                |   icerigini dogrulamak
    makinenin kurulus amaci      |   tasidigi emanetin amaci
    arac ya da onu isleten kisi  |   kaynagin sahibi

  bu sinirlar, insanin kendi duygusunu inkar etmesini ya da
  yanilmazlik iddia etmesini gerektirmez

  celisen kaynaklar ayri kimliklerle korunur; kaynagin cogul ya da
  belirsiz olusu tek bir kurucu sesle kapatilmaz
~~~

*Çizim 6 — Varlık: ifadenin dört türü; biri öteki gibi sunulamayanlar; karıştırılmayan çiftler.*

### Masaüstünde uygula

1. Kaynak envanterine her dosyanın ya da anlatının kimliğini, türünü, geldiği kişiyi veya yeri, özgün adını, eldeki sürümünü ve göreli dosya yolunu yaz. Bulunmayan alanı `bilinmiyor` diye işaretle.
2. Kullanılacak ifadeleri dört türle ayır: `GÖZLEM`, `AKTARIM`, `YORUM`, `BİLİNMİYOR`. Her beyan iddiasına dayanak göster: dosya, sayfa, kayıt zamanı veya tanık ifadesi. `GÖZLEM` etiketi teknik kayıtların otomatik olarak insan tanıklığı sayılması için kullanılmaz; gözlemi kimin yaptığı belirtilir.
3. İlk tanığı, bakım sorumlusunu, işlem yapan kişiyi, kullanılan teknik aracı ve devralan adayını rol kaydına yaz. Bir kişi birden fazla rol üstleniyorsa rolleri açıkça ayır.
4. Anlatıda kişiye atfedilmiş niyet, kesinlik veya hüküm varsa dayanağını kontrol et. Dayanak bulunmuyorsa bunu yorum olarak ayır veya beyanın dışına çıkar; kaynağı sessizce yeniden yazma.
5. Çelişen kaynakları ayrı kimliklerle koru. Kaynağın çoğul veya belirsiz oluşunu tek bir kurucu sesle kapatma.

**Tutulacak kayıt:** Kaynak envanteri, iddia-dayanak ayrımı, roller, görüş alanı ve belirsizlikler.

**Tamamlanma ölçütü:** Neyin taşındığı, neye dayandığı ve kimin hangi yetkiyle hareket ettiği anlaşılır. Devralan, olayın ilk tanığı ilan edilmemiştir. Kaydı korumakla içeriğini doğrulamak ayrı tutulmuştur.

**Bekletme koşulu:** Kaynak ile sonradan eklenen içerik ayırt edilemiyorsa ilgili iddia bu belirsizlikle kaydedilir; doğrulanmış veya birinci eldenmiş gibi kullanılamaz.

**Kaynak dayanağı:** Kaynak A'daki hazır bulunma, uyanıklık, emanet bilinci ve sadakat ilkeleri; önceki birinci sorunun varlık yanıtı ve taşıyıcı makine yanıtı.

## 2 Mekan Protokolü

**Kurucu sorular:** Nerededir? Bu yeri, oraya has bir yer yapan nelerdir? Neler değildir?

### İlke ve sınır

Mimarinin yeri, kaynak ile sonraki kullanım arasındaki sorumluluk ilişkisidir. Kaynak A'nın eşiği ve nöbet yeri, olayla temasın korunmasını ve taşıyıcının bu konumu kalıcı bir mülke çevirmemesini anlatır. İlk karşılaşmanın yeri sonradan yeniden edinilemez; bir kaydı okumak, o ilk bakış açısından bakmış olmak değildir. Farklı tanıkların ve maddi izlerin ayrı konumları korunur.

Mekân yalnızca klasör, bina veya kürsü değildir. Kimin konuşabildiği, kimin susturulduğu, kimlerin erişebildiği ve kaydın hangi baskılar altında oluştuğu anlamı etkiler. Eşik, olaya katılımın gizlenmesine gerekçe olamaz: Tanığın veya taşıyıcının olayla fiilî ilişkisi, çıkarı ve sınırları yazılır. Masaüstü klasörü de bu ilişkiyi temsil eder; tek başına onun yerini tutmaz.

~~~text
  MIMARININ YERI  kaynak ile sonraki kullanim arasindaki
                  sorumluluk iliskisi

      tanik A                                     tanik B
         \    gorus alani          gorus alani    /
          \                                      /
           `------------>   OLAY   <------------'
                              |
                              v
                            kayit  - - - - - - - ->  kaydi okuyan

    farkli taniklarin ve maddi izlerin ayri konumlari korunur;
    bir tanigin gorus alani otekininkiyle birlestirilmez

    ilk karsilasmanin yeri sonradan yeniden edinilemez:
    bir kaydi okumak, o ilk bakis acisindan bakmis olmak degildir

  ESIK VE NOBET YERI
    olayla temas korunur; tasiyici bu konumu kalici bir mulke cevirmez
    esik, olaya katilimin gizlenmesine gerekce olamaz:
    fiili iliski, cikar ve sinirlar yazilir

  ANLAMI ETKILEYENLER
    kim konusabiliyor? . kim susturuluyor? . kimler erisebiliyor? .
    kayit hangi baskilar altinda olustu?

  HEDEF ORTAM  farkli erisim kararlari gerektirir
    kisisel arsiv | sinirli topluluk | kurum | kamusal yayin

  masaustu klasoru bu iliskiyi temsil eder; tek basina yerini tutmaz
~~~

*Çizim 7 — Mekan: kaynak ile sonraki kullanım arasındaki sorumluluk ilişkisi; görüş alanları ayrı kalır.*

### Masaüstünde uygula

1. Kaynağın oluştuğu bilinen yeri ve ortamı kaydet. Gerekirse tam adres yerine erişimi sınırlı bir yer kodu kullan; bilinmeyen konumu tahmin etme.
2. Tanığın veya anlatıcının olaya yakınlığını, görebildiği alanı, varsa katılımını ve anlatıyı etkileyen koşulları yaz. Başka bir tanığın görüş alanını onunkiyle birleştirme.
3. `kaynaklar`, `calisma` ve `teslim` alanlarını ayır. Özgün kaynağı çalışma dosyasıyla değiştirme. Dosyaların hangi gerçek konumda tutulduğunu bakım kaydında belirt.
4. Kaydı kimlerin okuyabileceğini, kimlerin düzenleyebileceğini ve hangi kapsamda paylaşabileceğini belirle. Kimlik eşleme kaydı varsa paylaşıma açılacak nüshadan ayrı tut.
5. Hedef ortamı ve muhatabı kaydet: kişisel arşiv, sınırlı topluluk, kurum veya kamusal yayın farklı erişim kararları gerektirir. İtiraz ve düzeltmenin ulaşacağı kişiyi veya adresi belirt.

**Tutulacak kayıt:** Kaynak ortamı, görüş alanı, çalışma konumu, erişim yetkileri, hedef ortam ve başvuru yolu.

**Tamamlanma ölçütü:** Kaynak ile kullanım yerinin ilişkisi, kaydın bulunduğu yer ve erişimi yöneten sorumlu bellidir. Taşıyıcı, kaynak yerin tamamını temsil ettiği iddiasında değildir.

**Bekletme koşulu:** Seçilen ortam içerik için belirlenmiş erişim sınırlarını karşılamıyorsa paylaşım başlatılmaz; uygun yer veya daha sınırlı bir teslim nüshası hazırlanır.

**Kaynak dayanağı:** Kaynak A'daki eşik ve nöbet yeri anlatımı; önceki birinci sorunun mekân yanıtı ve taşıyıcı makine yanıtı.

## 3 Usül Protokolü

**Kurucu sorular:** Nasıl işler yapar? Bu yaptıklarını, ona has yapan nelerdir? Neler değildir?

### İlke ve sınır

Usul, Kaynak A'daki **müşahede, hıfzetme ve beyan** sırasını; alma, kaynağı koruma ve sınırları belirtilmiş aktarım olarak uygular. Aradan çekilmek, taşıyıcının kendi çıkarını veya gösterisini kaynağın önüne koymaması demektir. Aktarımda hiçbir değişiklik olmadığı varsayılmaz; özet, çeviri, seçim ve düzeltmeler gösterilir. Kaynakta amaçlanan eksiltmeme ve çoğaltmama sadakati, uygulamada müdahalelerin izlenebilmesiyle gözetilir.

Hafıza boşlukları kurgu ile doldurulmaz. Sonuca ulaşmak için kendi aleyhine olan bir unsur gizlenmez, anlatı dramatize edilmez ve bilgi pazarlık malzemesi yapılmaz. Duygu veya sessiz tavır da kaydın konusu olabilir; bunlardan kişinin niyeti hakkında kendiliğinden hüküm çıkarılmaz. Güvenlik ve mahremiyet nedeniyle sınırlandırma yapılmışsa bu, yetkili kayıt içinde gerekçelendirilir; halka açık nüsha tamamının yerine geçirilmez.

~~~text
  USUL  kaynaktaki uc adim ve buradaki karsiligi

    MUSAHEDE  -------->   HIFZETME  -------->   BEYAN
    alma                  kaynagi koruma        sinirlari belirtilmis
                                                aktarim

  MASAUSTUNDE

    kaynaklar/          calisma/                         teslim/
    kaynak       --->   v001 --> v002 --> v003   --->    son surum
    (uzerine            her degisiklik yeni bir surum
     yazilmaz)

    islem gunlugu:  tarih . yapan . kaynak ve cikti dosyasi .
                    degisiklik . gerekcesi
    hata duzeltmesinde eski kayit sessizce yok edilmez

  ARADAN CEKILMEK
    tasiyici, kendi cikarini ya da gosterisini kaynagin onune koymaz
    aktarimda hic degisiklik olmadigi varsayilmaz:
    ozet, ceviri, secim ve duzeltmeler gosterilir

  SON METIN DAYANAKLARIYLA KARSILASTIRILIR; ARANAN DORT SEY
    anlam kaybi . yeni kesinlik . taraf lehine degisiklik .
    aciklanmamis eksiltme

  YAPILMAZ
    hafiza boslugunu kurguyla doldurmak
    kendi aleyhine olan bir unsuru gizlemek
    anlatiyi dramatize etmek . bilgiyi pazarlik malzemesi yapmak
    aracin urettigi aciklamayi kaynakta gecen ifade gibi sunmak
~~~

*Çizim 8 — Usül: müşahede, hıfzetme, beyan; kaynak korunur, her değişiklik yeni sürüm olur.*

### Masaüstünde uygula

1. Kaynağı `kaynaklar` alanında koru; düzenlemeyi bir çalışma kopyasında yap. Yazıya geçirme, özet veya çeviri dosyasının başına hangi kaynaktan üretildiğini ve işlemi yapanı yaz.
2. Doğrudan alıntıyı, aktarılan anlatıyı ve kendi açıklamanı ayır. Okunamayan, duyulamayan veya hatırlanmayan yere `belirsiz` yaz. Anlamı tamamlamak için ayrıntı icat etme.
3. Yalnızca işine gelen parçayı seçmediğini denetle. Beyanı etkileyen karşıt unsurları ve gri alanları kaydet. Bir bölüm paylaşım dışında kalıyorsa kapsamını ve nedenini erişimi uygun kayıtta belirt.
4. Her değişiklikte yeni bir sürüm oluştur. İşlem günlüğüne tarihi, yapanı, kaynak ve çıktı dosyasını, değişikliği ve gerekçesini ekle. Hata düzeltmesinde eski kaydı sessizce yok etme; düzeltmenin hangi iddiayı etkilediğini göster.
5. Teknik araç veya yapay zekâ kullanıldıysa hangi iş için kullanıldığını ve sonucun kim tarafından kontrol edildiğini yaz. Aracın ürettiği bir açıklamayı kaynakta geçen ifade gibi sunma.
6. Son metni dayanaklarıyla karşılaştır. Anlam kaybı, yeni kesinlik, taraf lehine değişiklik veya açıklanmamış eksiltme varsa ilgili kısmı düzelt ya da belirsizliğini koru.

**Tutulacak kayıt:** Kaynak-çıktı ilişkisi, sürümler, işlem günlüğü, kapsam dışı bırakılanlar ve kontrol sonucu.

**Tamamlanma ölçütü:** Kaynak ile taşıyıcının müdahalesi ayırt edilebilir. Kullanılan iddialar dayanaklarına bağlanmıştır. Yapılan işlemler yetki ve kullanım amacı içinde kalmaktadır.

**Bekletme koşulu:** Açıklanamayan bir değişiklik, doğrulanamayan alıntı veya yetki dışı kullanım saptanırsa etkilenen sürümün aktarımı bekletilir. Kaydı onarmak mümkün değilse sınırlılık açıkça yazılır.

**Kaynak dayanağı:** Kaynak A'daki müşahede, hıfzetme ve beyan sırası; önceki birinci sorunun usul yanıtı ve taşıyıcı makine yanıtı.

## 4 Zaman Protokolü

**Kurucu sorular:** Hangi andadır? Bu anı, diğer zamanlardan farklı yapan nelerdir? Neler değildir?

### İlke ve sınır

Kaynak A'nın mühürlenmiş şimdi ve kairos anlatımı, geçmişteki karşılaşmanın bugünde süren sorumluluğunu belirtir. Bu yaşanan zaman, olayın takvimdeki zamanı ile anlatım, kayıt, düzenleme, beyan ve kabul zamanlarını birbirine eşitlemez. Emanet açık kaldıkça sorumluluk sürer; kayıt tarihleri yine de ayrı tutulur.

Anın ağırlığı süresinden veya resmî öneminden çıkarılmaz. İlk teması sonradan yeniden yaşanmış gibi göstermek, bugünkü yorumu eski tanığın sözüne eklemek veya bugünün amacını başlangıca geri yazmak bu protokolün dışındadır. Kaynaktaki uyanıklık, nostalji ve donma ayrımları kişilerin ruhsal durumunu teşhis etmek için kullanılmaz; burada izlenecek şey kaydın zamanı ve açık kalan bakım işidir.

~~~text
  SEKIZ AYRI ZAMAN, SEKIZ AYRI SATIR

       1       2       3       4       5       6       7       8
    ---*-------*-------*-------*-------*-------*-------*-------*---->

    1 olay         2 ilk temas    3 anlatim     4 ilk kayit
    5 duzenleme    6 beyan        7 ulasma      8 devralma

    her biri icin:  kesin | yaklasik | bilinmiyor
    henuz gerceklesmeyene gerceklesmis tarih yazilmaz
    dosyanin olusturulma tarihi   =/=   olay tarihi

  YASANAN ZAMAN VE TAKVIM
    gecmisteki karsilasmanin sorumlulugu bugunde surer

    karsilasma *=========== emanet acik kaldikca ==============>
                            sorumluluk surer

    bu, tarihleri birbirine esitlemez; kayit tarihleri ayri tutulur
    anin agirligi suresinden ya da resmi oneminden cikarilmaz

  BU PROTOKOLUN DISINDA
    ilk temasi sonradan yeniden yasanmis gibi gostermek
    bugunku yorumu eski tanigin sozune eklemek
    bugunun amacini baslangica geri yazmak

  ACIK IS ICIN
    yeniden degerlendirme tarihi ya da somut tetikleyici:
    yeni kaynak gelmesi . muhatabin yaniti . erisim kosulunun degismesi
    tasiyici cekilirse ya da kurum dagilirsa bakim kime gecer?
~~~

*Çizim 9 — Zaman: sekiz ayrı zaman; sorumluluğun sürmesi tarihleri birbirine eşitlemez.*

### Masaüstünde uygula

1. Zaman çizelgesine olay, ilk temas, anlatım, ilk kayıt, düzenleme, beyan, ulaşma ve devralma zamanlarını ayrı satırlar olarak gir. Henüz gerçekleşmeyene gerçekleşmiş tarih yazma.
2. Kesinliği belirt: `kesin`, `yaklaşık` veya `bilinmiyor`. Biliniyorsa saat dilimini yaz; dosyanın oluşturulma tarihini olay tarihi yerine kullanma. Örnek yazım: `2026-10-31T10:00:00Z` yalnızca biçim örneğidir.
3. Her sürümün hangi tarihte kim tarafından üretildiğini kaydet. Dosya adıyla içerideki sürüm bilgisinin aynı olmasını sağla.
4. Açık iş için yeniden değerlendirme tarihi veya somut tetikleyici belirle: yeni kaynak gelmesi, muhatabın yanıtı, erişim koşulunun değişmesi gibi. Bu kayıt tek başına otomatik hatırlatma kurmaz.
5. Saklama süresini veya yeniden değerlendirme koşulunu belirle. Taşıyıcının çekilmesi, kapasitesini yitirmesi veya kurumun dağılması hâlinde bakımın kime geçeceğini ya da nasıl yeniden karara bağlanacağını yaz.

**Tutulacak kayıt:** Ayrı zaman çizelgesi, tarihlerin kesinlik derecesi, sürüm zamanları, açık işler ve bakımın devam koşulu.

**Tamamlanma ölçütü:** Olayla sonraki işlemlerin kronolojisi anlaşılabilir. Bilinmeyen tarihler tahminle kesinleştirilmemiştir. Açık sorumluluk için sonraki değerlendirme koşulu vardır.

**Bekletme koşulu:** Kronolojide sonuca etki eden bir çelişki varsa ilgili anlatı kesin zaman sırasıyla sunulmaz; çelişki ayrıca belirtilir. Yeni bilgiyle önceki kayda dönülmesi gerekirse eski tarihler korunarak yeni işlem eklenir.

**Kaynak dayanağı:** Kaynak A'daki mühürlenmiş şimdi ve kairos anlatımı; önceki birinci sorunun zaman yanıtı ve taşıyıcı makine yanıtı.

## 5 Gaye Protokolü

**Kurucu sorular:** Hangi nihai amaca hizmet eder? Bu nihai amaca ulaştıran nelerdir? Neler değildir?

### İlke ve sınır

Gaye, olmuş olanın hiç olmamış gibi silinmesini önlemek ve tanıklığın uygun muhatapta karşılık bulmasını sağlamaktır. Kaynak A bunu hakikatin zayi olmaması, ehline teslim ve uyanık bir kulağa ulaşma olarak ifade eder. Önceki çerçeve buna gelecektekilerin anlama, sorgulama ve karar verme imkânını açık tutmayı ekler. Taşıyıcı, bu amacı kendi devamı, itibarı veya hükmetme yetkisiyle özdeşleştiremez.

Amaca ulaşmak için çarpıtma, intikam, alkış arayışı veya inandırmaya zorlama kabul edilmez. Muhatabın aynı hükme varması şart değildir; dış onayın yokluğu tanıklığı kendiliğinden hükümsüz kılmaz. Buna karşılık bakım devrinin gerçekleşmesi, muhatabın somut kabulünü gerektirir. Hakikate sadakat her şeyi herkese açmayı gerektirmez; kapsamı sınırlandırmak, iade etmek veya zarar üreten devri reddetmek de sorumlu karar olabilir.

~~~text
  GAYE
    olmus olanin hic olmamis gibi silinmesini onlemek
    tanikligin uygun muhatapta karsilik bulmasini saglamak
    gelecektekilerin anlama, sorgulama ve karar verme imkanini
    acik tutmak

  BES KARAR
                              .-->  devre hazir
                              |-->  sinirli beyan
    amac . muhatap .   -------+-->  koruma altinda beklet
    yetki . kapsam            |-->  iade et
                              `-->  aktarimi reddet

    kapsami sinirlandirmak, iade etmek ya da zarar ureten devri
    reddetmek de sorumlu karar olabilir;
    hakikate sadakat her seyi herkese acmayi gerektirmez

  IKI AYRI OLCUT
    beyanin basarisi   |   bakim devrinin kabulu

    muhatabin ayni hukme varmasi sart degildir;
    bakim devrinin gerceklesmesi ise muhatabin somut kabulunu
    gerektirir

  AYNI SAYILMAZ
    susma tercihi | korunma ihtiyaci | zorla susturulma

  KABUL EDILMEZ
    carpitma . intikam . alkis arayisi . inandirmaya zorlama

  tasiyici bu amaci kendi devami, itibari ya da hukmetme yetkisiyle
  ozdeslestiremez
~~~

*Çizim 10 — Gaye: silinmeyi önlemek ve uygun muhataba ulaşmak; beş karar.*

### Masaüstünde uygula

1. Kullanım amacını tek bir açık paragrafta yaz: ne korunacak, kimin için, hangi ihtiyaçla ve hangi sınırlar içinde kullanılacak? Görevi devralanın amacı farklıysa farkı görünür tut.
2. Devralan adayını ve neden uygun olduğunu belirt. Kaydı okuyabilecek, koruyabilecek ve belirtilen bakım işini yapabilecek durumda olup olmadığını kontrol et. Kurum adı tek başına bakım adresi sayılmaz.
3. Paylaşılacak dosyaları, kapsam dışı kalacakları, erişim düzeyini, yeniden paylaşım koşullarını ve varsa süreyi belirle. Emanet edenin iradesinin etkilenen başkalarının sınırlarını ortadan kaldırmadığını gözet.
4. Üç kısa unsurdan oluşan teslim açıklaması hazırla: içeriğin dayanağı ve sınırları; istenen kullanım; devralandan beklenen bakım ve yanıt. Sonucu elde etmek için belirsizliği gizleme.
5. Kararı yaz: `devre hazır`, `sınırlı beyan`, `koruma altında beklet`, `iade et` veya `aktarımı reddet`. Gerçek gönderim ya da yayın kapsamının kim tarafından yetkilendirildiğini belirt; yalnızca bu kılavuzu kullanmak böyle bir yetki yerine geçmez.

**Tutulacak kayıt:** Amaç, uygun muhatap, yetki, paylaşım kapsamı, beklenen bakım, karar ve gerekçesi.

**Tamamlanma ölçütü:** Ne için, kime, hangi içerikle ve hangi sınırlar içinde aktarım yapılacağı somuttur. Beyanın başarısıyla bakım devrinin kabulü ayrı ölçütlerdir. Süreklilik veya görünürlük tek başına başarı sayılmamaktadır.

**Bekletme koşulu:** Amaç belirsizse, muhatap uygun değilse veya belirlenen kapsam için yetki yoksa dış aktarım yapılmaz. Sınırlama ve erteleme gerekçeleri yazılır; susma tercihi, korunma ihtiyacı ve zorla susturulma aynı sayılmaz.

**Kaynak dayanağı:** Kaynak A'daki hakikatin zayi olmaması, ehline teslim ve uyanık kulağa ulaşma ilkeleri; önceki birinci sorunun gaye yanıtı ve taşıyıcı makine yanıtı.

## 6 Kökleşme (Bitiş) Protokolü

**Kurucu sorular:** Emanet yerini buldu mu? Neyi kim devraldı? Taşıyıcının hangi görevi sona eriyor, hangi sorumluluğu sürüyor?

### İlke ve sınır

Kökleşme, tanıklığın ilk taşıyıcının sürekli müdahalesine bağımlı kalmadan korunabilir, erişilebilir ve itiraz edilebilir bir bakım düzeni kazanmasıdır. Kaynak A'nın şahidin ölümü, fenâ ve sıfattan çekilme anlatımları bu protokolde tamamlanan taşıyıcılık rolünden çekilme olarak uygulanır. Taşıyıcı, emaneti kendi makamının, şöhretinin veya kalıcı mülkünün dayanağı olarak tutmaz; kaynağın izini ve kendi geçmiş işlemlerinin hesabını da silmez.

Bitiş, kuruluş ve belirli devir görevinin kapanışıdır. Hakikat veya adalet hakkında nihai bir sertifika değildir. Beyan edilmiş olması, dosyanın ulaşması ve bakım görevinin kabul edilmesi ayrı kaydedilir. İtiraz, yeni kaynak, hata veya taşıyıcı değişikliğiyle kayıt yeniden açılabilir. Yeni başlangıçlar önceki kaydı geriye dönük değiştirmez; kendi kayıt kimliğiyle ilişkilendirilir.

~~~text
  KOKLESME
    tanikligin, ilk tasiyicinin surekli mudahalesine bagimli kalmadan
    korunabilir, erisilebilir ve itiraz edilebilir bir bakim duzeni
    kazanmasi

    ILK TASIYICI                                    DEVRALAN
   .--------------.     son surum, teslim       .--------------.
   |   cekilir    | --------------------------> | bakim adresi |
   `--------------'                             `--------------'

     biten:   belirli yetkiler; tamamlanan tasiyicilik rolu
     suren:   duzeltmeye cevap verme . mahremiyeti koruma .
              islem gecmisini aciklama

  TASIYICI
    emaneti kendi makaminin, sohretinin ya da kalici mulkunun
    dayanagi olarak tutmaz
    kaynagin izini ve kendi gecmis islemlerinin hesabini da silmez

  BITIS
    kurulus ve belirli devir gorevinin kapanisidir;
    hakikat ya da adalet hakkinda nihai bir sertifika degildir

  YENIDEN ACILABILIR
    itiraz . yeni kaynak . hata . tasiyici degisikligi
    yeni baslangic onceki kaydi geriye donuk degistirmez;
    kendi kayit kimligiyle iliskilendirilir
~~~

*Çizim 11 — Kökleşme: ilk taşıyıcının çekilmesi; biten yetkiler ve süren yükümlülükler.*

### Masaüstünde uygula

1. Son sürümü belirle. `teslim` klasörüne yalnızca yetkilendirilmiş dosyaları koy ve dosya listesini yaz. Son nüshanın kaynak kimliklerini, sınırlarını, sürümünü ve başvuru yolunu içerdiğini kontrol et. Gizli kimlik eşlemelerini veya iç değerlendirmeleri yanlışlıkla teslim nüshasına ekleme.
2. Göndermeden önce dosyaları aç; metinlerin ve gerekli eklerin okunabildiğini denetle. İzin verilmiş yedeği ve konumunu kaydet. Teknik bütünlük özeti kullanılmışsa bunun yalnızca dosya değişimini saptamaya yaradığını, içeriğin doğruluğunu kanıtlamadığını belirt.
3. Gerçek aktarım yetkilendirildiyse belirlenen kanaldan yap. Beyan ve gönderim tarihlerini yaz. Alıcının erişimi doğrulamasını `ulaştı`, kapsamı ve bakım görevini kabul etmesini `devralındı` olarak ayrı kaydet; cevap yoksa kabul edilmiş yazma.
4. Kabulü kayıt altına al: hangi dosyalar ve sürümler alındı, hangi amaç ve sınırlarla, bakım kimde, erişim ve düzeltme talepleri nereye gelecek? Kabul, alıcının içerikteki her iddiaya inanması şartına bağlanmaz.
5. Devredenin biten yetkilerini ve süren yükümlülüklerini yaz. Gerekli erişim değişikliklerini uygula ve gerçekleştiğini denetle. Düzeltmeye cevap verme, mahremiyeti koruma veya işlem geçmişini açıklama gibi devam eden görevleri yok sayma.
6. Kapanış türünü seç ve gerekçelendir. Yeni kaynak, hata, uygunsuz kullanım, dosya kaybı veya bakım sorumlusunun değişmesi durumunda yeniden açma yolunu belirt. Yeniden açarken yeni sürüm oluştur; eski kapanış kaydını koru.

### Kapanış türleri

| Durum | Yazılabilmesi için gereken | Sonraki bakım |
|---|---|---|
| `Kökleşti / devralındı` | Son dosyalar ulaşmış, belirli bakım görevi kabul edilmiş ve ulaşılabilir bakım adresi kurulmuştur. | Devralan bakım yapar; devredenin devam eden yükümlülükleri ayrıca yazılır. |
| `Beyan edildi / devir açık` | Beyan gerçekleşmiştir; ulaşma veya bakım kabulü henüz doğrulanmamıştır. | Mevcut bakım sorumlusu ve sonraki değerlendirme koşulu korunur. |
| `Koruma altında bekliyor` | Emanet belirli sınırlar içinde tutulmaktadır; dış aktarım ertelenmiştir. | Bekleme gerekçesi, erişim sınırı ve yeniden değerlendirme koşulu yazılır. |
| `İade edildi` | İade muhatabı, kapsamı ve gerçekleşen teslimi kaydedilmiştir. | Kimde hangi nüsha ve yükümlülüğün kaldığı açıklanır. |
| `Aktarım reddedildi` | Ret kararı ve gerekçesi kaydedilmiştir. | Elde kalan kayıtların bakım, saklama veya silme kararı ayrıca belirlenir. |

Kişisel arşivde bakım sürdürülüyorsa bu açıkça yazılır; aynı kişinin kaydı kendi klasörüne taşıması dış devrin tamamlandığı anlamına gelmez. Bir süreç iade veya ret kararıyla kapanabilir; bu kapanış otomatik olarak `kökleşti` diye adlandırılmaz. Saklama veya silme kararı, belirlenmiş kapsam ve yetkiyle ayrıca yürütülür; rolün kapanışı dosyaları kendiliğinden silmez.

~~~text
  KAPANIS TURU, SOMUT DAYANAKLA YAZILIR

   dis aktarim
      |
      |-- ertelendi; emanet belirli
      |   sinirlar icinde tutuluyor .......  Koruma altinda bekliyor
      |
      |-- ret karari ve gerekcesi
      |   kaydedildi ......................  Aktarim reddedildi
      |
      |-- iade muhatabi, kapsami ve
      |   gerceklesen teslim kaydedildi ...  Iade edildi
      |
      `-- beyan gerceklesti
             |
             |-- ulasma ya da bakim kabulu
             |   henuz dogrulanmadi .......  Beyan edildi / devir acik
             |
             `-- son dosyalar ulasti,
                 bakim gorevi kabul edildi,
                 bakim adresi kuruldu .....  Koklesti / devralindi

   cevap yoksa "kabul edildi" yazilmaz

   ayni kisinin kaydi kendi klasorune tasimasi, dis devrin
   tamamlandigi anlamina gelmez

   iade ya da ret kararina "koklesti" denmez
   rolun kapanisi dosyalari kendiliginden silmez
~~~

*Çizim 12 — Kökleşme: beş kapanış türü ve her birinin dayanağı.*

**Tutulacak kayıt:** Teslim listesi, son sürüm, açılabilirlik kontrolü, ulaşma ve kabul dayanağı, biten ve süren görevler, yedek ve yeniden açma yolu.

**Tamamlanma ölçütü:** Kapanış türü somut dayanakla yazılmıştır. `Kökleşti / devralındı` seçilmişse kabul ve bakım adresi vardır. İlk taşıyıcının çekilmesi kaynak kaybına veya hesap verme yolunun kapanmasına yol açmamaktadır.

**Bekletme koşulu:** Kapsamı belirsiz kabul, okunamayan dosya, eksik temel ek veya sahipsiz bakım varsa devir tamamlandı yazılmaz. Eksik giderilir veya uygun açık durum korunur.

**Kaynak dayanağı:** Kaynak A'daki şahidin ölümü, fenâ ve sıfattan çekilme anlatımları; önceki 6 Kökleşme yorumu ve taşıyıcı makine yanıtı.

## Doldurulabilir emanet kaydı

Aşağıdaki bloğu yeni bir `Emanet_Kaydi.md` dosyasına kopyala. Noktalı alanlar doldurulacak yerlerdir; örnek veya gerçekleşmiş işlem değildir. Uygulanmayan alana gerekçesiyle `uygulanmıyor`, bilinmeyene `bilinmiyor`, henüz yapılmayana `yapılmadı` yaz. Kayıtlar paylaşılacaksa iç çalışma nüshası ile teslim nüshasını ayır ve yalnızca paylaşım kapsamındaki alanları devret.

```markdown
# Emanet Kaydı

Kayıt kimliği: ...
Sürüm: ...
Kayıt sorumlusu ve başvuru yolu: ...
Açılış tarihi ve saat dilimi: ...
Genel durum: ...
İlişkili önceki / sonraki kayıt kimliği: ...

## 0 Tohum (Başlangıç)

Geliş biçimi: ...
Tohum cümlesi: ...
İlk temasın bilinen zamanı: ...
İlk kaynaklar: ...
Başlangıç niyeti ve olası çıkar ilişkisi: ...
Bilinmeyenler ve henüz üstlenilmeyen işler: ...
İlk erişim sınırı: ...

## 1 Varlık

Emanetin konusu: ...
İlk tanık ve doğrudan görüş alanı: ...
Bakım sorumlusu: ...
İşlem yapan kişi: ...
Teknik araç ve görev sınırı: ...
Devralan adayı: ...
Makinenin kuruluş amacı ile emanetin amacı arasındaki fark: ...

### Kaynak envanteri

| Kaynak kimliği | Tür / kaynak kişi veya yer | Özgün ad ve eldeki sürüm | Göreli dosya yolu | Sınır / erişim |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

### İddia ve dayanaklar

| İddia kimliği | İfade | Tür | Dayanak ve konumu | Belirsizlik / karşıt kaynak |
|---|---|---|---|---|
| ... | ... | GÖZLEM / AKTARIM / YORUM / BİLİNMİYOR | ... | ... |

## 2 Mekan

Kaynak ortamı ve tanığın olayla ilişkisi: ...
Görüş alanını etkileyen koşullar: ...
Çalışma konumu: ...
Okuma / düzenleme / paylaşım erişimleri: ...
Kimlik koruma düzeni varsa açıklaması: ...
Hedef ortam ve başvuru yolu: ...

## 3 Usül

Kullanılan kaynaklar ve üretilen dosyalar: ...
Yazıya geçirme / özet / çeviri yöntemi: ...
Teknik araç kullanımı ve insan kontrolü: ...
Seçimler, kapsam dışı bırakılanlar ve gerekçeleri: ...
Kaynakla karşılaştırma sonucu ve çözülemeyen konular: ...

### İşlem günlüğü

| Tarih ve saat dilimi | Yapan | Kaynak / çıktı sürümü | İşlem ve gerekçesi | Etkilenen iddia veya bölüm |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## 4 Zaman

| Aşama | Tarih ve saat dilimi | Kesin / yaklaşık / bilinmiyor | Dayanak |
|---|---|---|---|
| Olay | ... | ... | ... |
| İlk temas | ... | ... | ... |
| Anlatım | ... | ... | ... |
| İlk kayıt | ... | ... | ... |
| Son düzenleme | ... | ... | ... |
| Beyan | ... | ... | ... |
| Ulaşma | ... | ... | ... |
| Devralma | ... | ... | ... |

Açık işler ve mevcut sorumlu: ...
Sonraki değerlendirme tarihi veya tetikleyicisi: ...
Saklama / yeniden değerlendirme koşulu: ...
Taşıyıcı çekilirse veya kurum dağılırsa bakım yolu: ...

## 5 Gaye

Amaç ve gözetilen yarar: ...
Devralanın uygunluğu ve kapasitesi: ...
Paylaşım veya devir yetkisi ve kapsamı: ...
Paylaşılacak / dışarıda kalacak dosyalar: ...
Erişim, yeniden paylaşım ve süre sınırları: ...
Teslim açıklaması: ...
Karar ve gerekçesi: ...

## 6 Kökleşme (Bitiş)

Kapanış türü: ...
Son sürüm ve teslim listesi: ...
Dosyaların açılabilirlik kontrolü; yapan ve tarih: ...
Beyan / gönderim dayanağı: ...
Ulaşma doğrulaması: ...
Bakım kabulü; kim, neyi, hangi sınırlarla ve ne zaman: ...
Kabulün dayanağı veya kayıt yolu: ...
Devralan bakım sorumlusu ve başvuru yolu: ...
Devredenin biten yetkileri ve gerçekleşen erişim değişiklikleri: ...
Devredenin süren yükümlülükleri: ...
Yedek konumu, yetkisi ve kontrolü: ...
Kalan nüshalar için saklama / iade / silme kararı: ...
Yeniden açma koşulu ve sorumlusu: ...

### Protokol işlem durumu

| Bölüm | Yapan | Tarih | Dayanak / çıktı | Karar ve açık konu | Durum |
|---|---|---|---|---|---|
| 0 | ... | ... | ... | ... | hazırlanıyor |
| 1 | ... | ... | ... | ... | hazırlanıyor |
| 2 | ... | ... | ... | ... | hazırlanıyor |
| 3 | ... | ... | ... | ... | hazırlanıyor |
| 4 | ... | ... | ... | ... | hazırlanıyor |
| 5 | ... | ... | ... | ... | hazırlanıyor |
| 6 | ... | ... | ... | ... | hazırlanıyor |

### Yeniden açma kaydı

Önceki kapanış ve sürümü: ...
Yeni sürüm ve tarih: ...
Yeniden açma nedeni ve dayanağı: ...
Etkilenen protokoller ve iddialar: ...
Yeni bakım veya devir kararı: ...
```

## Kaynak ilkelerinin birleştirilmesi

### Kaynaklar ve metnin statüsü

**Kaynak A:** *Şahitlik Mimarisi — İlkeler ve Kavramsal Çerçeve*; bu protokolün köken aldığı kimlik metni. Kavramsal ilkeler ve kaynak içindeki soru-yanıt arşivi birlikte incelenmiştir. Metinde anılan her ilke, anıldığı paragrafta kendi sözleriyle özetlenmiştir.

**Kaynak B:** Bu konuşmadaki ilk iki soru-yanıt çifti; bunlardan düzenlenen 1–5 protokol metni ve önceki 0 Tohum / 6 Kökleşme yorumları. İlk iki çiftin metni aşağıda korunur. Buradaki masaüstü adımları ve doldurulabilir şablon, bu kaynakları uygulamaya dönüştüren düzenlemelerdir; Kaynak A'dan yapılmış doğrudan alıntılar değildir.

| Protokol | Kaynak A'daki ilkeler | Bu metindeki uygulama karşılığı |
|---|---|---|
| 0 Tohum | İlk temas, uyanış, seyircilikten sorumluluğa geçiş, henüz açılmamış imkân. | Geliş biçimi, tohum cümlesi, ilk sınırlar ve bilinmeyenler. |
| 1 Varlık | Hazır bulunma, uyanıklık, sadakat, emanet ve beyan sorumluluğu; söylenti, zan, tarafgirlik ve son hükümden ayrım. | Kaynak türü, görüş alanı, iddia-dayanak ayrımı ve roller. |
| 2 Mekan | Eşik, yakınlık ve mesafe, ilk konumun tekilliği, geçici nöbet; sahne ve mülkiyetten ayrım. | Kaynak ortamı, erişim, hedef ortam ve başvuru adresi. |
| 3 Usül | Müşahede, hıfzetme, beyan; yalınlık, bütünsellik, kendi aleyhine olanı da saklamama; kurgu, manipülasyon ve pazarlıktan kaçınma. | Özgün kopya, ayrı çalışma sürümleri, işlem günlüğü, insan kontrolü ve kapsam kaydı. |
| 4 Zaman | Kairos, mühürlenmiş şimdi, önce-sonra ayrımı ve emanetin açık sorumluluğu; salt süre ve nostaljiden ayrım. | Ayrı zaman çizelgesi, kesinlik derecesi, değerlendirme ve devam koşulu. |
| 5 Gaye | Hakikatin zayi olmaması, ehil muhatap, uyanık kulak, çıkar ve gösteriden çekilme; çarpıtma, intikam ve dayatmadan kaçınma. | Açık amaç, uygun muhatap, sınırlı kullanım kararı ve dış onaydan ayrı başarı ölçütleri. |
| 6 Kökleşme | Emanetin yerini bulması, sıfattan çekilme, fenâ, kalıcı makam edinmeme ve yeni tohumlara yer açma. | Kabul edilmiş bakım, rolün kapanışı, süren yükümlülükler ve yeniden açma yolu. |

### Birleştirme sırasında korunan ayrımlar

**Sadakat ve yanılabilirlik:** Kaynak A'daki saf ve eksiksiz taşıma, sadakat ideali olarak korunmuştur. Uygulama, insanın kusursuz bir ayna olduğunu varsaymaz. Bilinmeyenler, çelişkiler ve dönüşümler kaydedilir; kaynakla yorum ayrılır.

**Eşik ve çoğulluk:** İlk tanığın konumu tekildir; bu, başka tanıkları ve maddi izleri dışlayan bir hakikat tekeli oluşturmaz. Kaynaktaki eşik benzetmesi, somut olayla ilişkilerin ve çıkarların açıklanmasıyla birlikte uygulanır.

**Kairos ve kronoloji:** Sorumluluğun bugünde sürmesi, olay ve işlem tarihlerinin birleşmesi demek değildir. Tarihler ayrı tutulur; zamanın yaşanan ağırlığı süreye veya takvime indirgenmez.

**Beyan ve kabul:** Kaynak A hem doğru beyanla tamamlanmayı hem ehil muhataba ulaşmayı vurgular. Bu metin beyanın gerçekleşmesini, dosyanın ulaşmasını ve bakımın kabulünü ayrı kaydeder. İnanç veya görüş birliği, devralma kabulünün yerine geçmez.

**Cesaret ve korunma:** Kaynağın çıkar karşısında sadakat ve sözünün sorumluluğunu üstlenme ilkesi korunur. Güvenlik, rıza veya mahremiyet nedeniyle sınırlandırma ve erteleme, kişiye otomatik bir ahlaki suçlama yönelten ölçütlere dönüştürülmez. Sessiz tavır, susma tercihi ve zorla susturulma ayırt edilir.

**Aradan çekilme ve hesap verme:** Taşıyıcının kendi görünürlüğünü hakikatin önüne koymaması, kaynak kimliğinin veya işlem geçmişinin silinmesi anlamına gelmez. Çekilme, belirli yetkilerin ve nöbetin sona ermesiyle uygulanır; geçmiş işlemlerin hesabı ve yazılı devam görevleri korunur.

**Manevi kavramlar ve teknik roller:** Kaynak A'nın *Uyanık Özne*, *Canlı Hafıza*, *Fıtrat*, *İnsan-ı Kâmil*, *Kalp Sahibi*, *İbnü'l-Vakt*, *İhlas*, *Fenâ* ve *El-Şehîd / Mutlak Hakikat* anlatımları, kaynağın felsefi ve tasavvufi anlam düzlemlerinde korunur. Fıtrat başlangıçtaki sorumluluk imkânına, ayna öz-denetime, İbnü'l-Vakt anın sorumluluğuna ve fenâ taşıyıcının merkezden çekilmesine bağlanmıştır. Bu adlar bir yazılıma veya kişiye otomatik yetki, yanılmazlık ya da manevi mertebe atamak için kullanılmaz. Kaynaktaki şehadet ve şahidin ölümü ilişkisi, burada emanet uğruna taşıyıcılık iddiasını bırakma mecazı olarak ele alınır.

~~~text
  BIRLESTIRIRKEN KORUNAN YEDI AYRIM

   SADAKAT                          YANILABILIRLIK
   saf ve eksiksiz tasima,    <-->  insan kusursuz bir ayna sayilmaz;
   ideal olarak korunur             bilinmeyenler, celiskiler ve
                                    donusumler kaydedilir

   ESIK                             COGULLUK
   ilk tanigin konumu         <-->  bu, baska taniklari ve maddi
   tekildir                         izleri dislayan bir tekel kurmaz

   KAIROS                           KRONOLOJI
   sorumluluk bugunde surer   <-->  olay ve islem tarihleri ayri
                                    tutulur

   BEYAN                            KABUL
   dogru beyanla tamamlanma   <-->  beyan, ulasma ve bakim kabulu
                                    ayri kaydedilir

   CESARET                          KORUNMA
   cikar karsisinda sadakat   <-->  guvenlik, riza ya da mahremiyet
                                    icin sinirlama ve erteleme,
                                    suclama olcutune donusturulmez

   ARADAN CEKILME                   HESAP VERME
   tasiyici gorunurlugunu     <-->  kaynak kimligi ve islem gecmisi
   hakikatin onune koymaz           silinmez

   MANEVI KAVRAMLAR                 TEKNIK ROLLER
   kaynagin felsefi ve        <-->  bir yazilima ya da kisiye otomatik
   tasavvufi anlam                  yetki, yanilmazlik ya da mertebe
   duzlemlerinde korunur            atamak icin kullanilmaz
~~~

*Çizim 13 — Kaynak ilkeler ile uygulama birleştirilirken korunan yedi ayrım.*

## Önceki soru-yanıt kaydı

Aşağıdaki iki çift, ilk kavramsal çerçevenin kaydıdır. Yeni protokol hükümleri bu arşivdeki yanıtların yerine geriye dönük yazılmamıştır. Başlık düzeyleri bu dosyanın düzenine uyarlanmış; soru ve yanıtların sözleri korunmuştur. Kaynak A'nın kendi soru-yanıt arşivi o metnin içindedir; yukarıdaki kaynak haritası o ilkelerin bu metinde nerede uygulandığını gösterir.

### Birinci soru

Geçmiş bağlamları buraya taşıma. Burası ile sınırlı kalma.

**Tanıklık ve Emanet Aktarımı Mimarisi**

Nedir? Onu o yapan nelerdir? Neler değildir?
Nerededir? Bu yeri, oraya has bir yer yapan nelerdir? Neler değildir?
Nasıl işler yapar? Bu yaptıklarını, ona has yapan nelerdir? Neler değildir?
Hangi andadır? Bu anı, diğer zamanlardan farklı yapan nelerdir? Neler değildir?
Hangi nihai amaca hizmet eder? Bu nihai amaca ulaştıran nelerdir? Neler değildir?

### Birinci yanıt

**Tanıklık ve Emanet Aktarımı Mimarisi**, tanık olunan bir gerçekliğin izlerini, anlamını ve ona ilişkin sorumlulukları; kaynaklarını, sınırlarını ve geçirdikleri değişimleri görünür tutarak başkalarının bakımına bırakabilen bir düzen olarak düşünülebilir.

Buradaki kurucu ayrım şudur: **Tanık olma konumu devredilemez.** Devredilebilen; anlatı, iz, kayıt, bilgi, beceri ve bunlara ilişkin sorumluluklardır. Devralan kişi, ilk olayın tanığı hâline gelmez; kendisine ulaşan tanıklığın nasıl taşındığına tanıklık edebilir.

1. **Nedir? Onu o yapan nelerdir? Neler değildir?**

   Tanıklık, “Neyle karşılaştım; neyi, nereden biliyorum?” sorusuna karşılık verir. Emanet, “Bana bırakılan üzerinde hangi yetkim var; kime karşı, neden sorumluyum?” sorusunu açar. Mimari ise bu cevapların kişilerin iyi niyetine bağımlı kalmamasını sağlayan ilişkileri, usulleri ve sınırları kurar.

   Onu kendisi yapan; kaynağı yorumdan, korumayı sahiplenmeden, kullanma yetkisini sınırsız tasarruftan ayırabilmesidir. Tanığın yanılabilirliğini, emanetçinin yetersiz kalabileceğini ve aktarımın anlamı değiştirebileceğini hesaba katar.

   Her söyleneni doğrulanmış hakikat sayan bir düzen değildir. Emanet edileni mülke dönüştüren bir sahiplik sistemi değildir. Yalnızca hatırlamak, saklamak veya dağıtmak da değildir. Bir kayıt eksiksiz saklanırken ona ilişkin sorumluluk bütünüyle kaybolabilir.

2. **Nerededir? Bu yeri, oraya has yapan nelerdir? Neler değildir?**

   Bu mimari, **kaynak ile sonraki kullanım arasındaki sorumluluk ilişkisinde** bulunur. Bir ailede, arşivde, atölyede, toplulukta, kurumda veya teknik sistemde somutlaşabilir. Bir dilin yaşatılmasında, bir zanaatin öğretilmesinde ve bir yaşam alanının bakımının devralınmasında farklı biçimler alabilir.

   Bulunduğu yeri özgül kılan yalnızca adresi değildir: Kim konuşabilir? Kim dinlenir? Kim erişebilir? Kim itiraz edebilir? Kimin yokluğunda karar verilir? Aynı anlatı, güven içinde söylendiği bir ortamla baskı altında kaydedildiği bir ortamda aynı anlamı taşımaz.

   Dolayısıyla yer, aktarımın nötr kabı değildir; aktarılabileni ve onun anlamını etkiler. Bir ekran, bina veya depolama alanı tek başına bu mimariyi oluşturmaz. “Her yerde bulunabilir” denilerek sorumluluğun somut adresi de belirsiz bırakılamaz.

3. **Nasıl işler? Yaptıklarını ona has yapan nelerdir? Neler değildir?**

   Önce neyin aktarıldığını ayırt eder: Bir deneyim mi, anlatı mı, yorum mu, beceri mi, bakım görevi mi? Bunların hangi kaynaktan geldiğini, nelerin bilindiğini ve nelerin belirsiz kaldığını belirtir.

   Ardından aktarımın koşullarını kurar: Kim devredebilir, kim devralabilir, hangi amaçlarla kullanılabilir, kimlerle paylaşılabilir? Devralanın bunu anlayacak ve taşıyacak kapasitesi bulunmalıdır. **Bir şeyin teslim edilmesi, emanet ilişkisinin kurulduğunu tek başına göstermez.**

   Sonrasında bakım sürer: Değişiklikler görünür tutulur, yeni yorumlar eski tanığın sözüne eklenmez, hatalar düzeltilebilir, itirazlar karşılık bulur. Emanetçinin çekilmesi, ölmesi veya kurumun dağılması ihtimali için de bir devam ya da sona erme yolu bulunur.

   Ona has olan, her işlemde “Bunu hangi yetkiyle yapıyorum ve sonucundan kime karşı sorumluyum?” sorusunun cevaplanabilir kalmasıdır. Salt kopyalama, yaygınlaştırma veya güvenli depolama değildir. Rıza da bütün gelecek kullanımları kapsayan sınırsız bir izin sayılamaz; emanet edenin isteği, etkilenen başkalarının sınırlarını kendiliğinden ortadan kaldırmaz.

4. **Hangi andadır? Bu anı diğer zamanlardan farklı yapan nelerdir? Neler değildir?**

   Bu mimarinin belirleyici anı, **birinin taşıdığı şeyi başkasının üstlenmesine açtığı andır.** Kaynağın her sonraki kullanıma eşlik edemeyeceği, devralanın da yalnızca seyirci kalamayacağı bir eşiktir.

   Burada birkaç zaman birlikte bulunur: Olayın zamanı, anlatılmasının zamanı, devralınmasının zamanı ve yeniden kullanılmasının zamanı. Bunların ayrılması gerekir. Bugünün yorumu, geçmişteki tanığın ağzından konuşturulmamalıdır.

   Bu anı farklı yapan, sorumluluğun yeniden dağıtılmasıdır. “Bunu biliyorum”dan “Bununla ne yapacağımı gerekçelendirmeliyim”e geçilir.

   Yalnızca geçmişe ait bir an değildir; yaşayan bir pratiğin sürdürülmesinde de ortaya çıkar. Tek seferlik bir teslim törenine de sığmaz. Koşullar, bilgi ve etkiler değiştikçe emanetin nasıl taşındığı yeniden değerlendirilebilir.

5. **Hangi nihai amaca hizmet eder? O amaca ulaştıran nelerdir? Neler değildir?**

   Savunulabilir nihai amacı, **tanık olunanın silinmesini veya keyfî biçimde yeniden yazılmasını önlerken, gelecektekilerin anlama, sorgulama ve karar verme imkânını açık tutmaktır.** Böylece tanıklık, yalnızca ilk taşıyıcısının ömrüne ve gücüne bağımlı kalmaz.

   Bu amaca; kaynağa sadakat, belirsizliğin açıklığı, etkilenenlere özen, yetkinin sınırlandırılması ve itirazın mümkün olmasıyla yaklaşılır. Sadakat, her aktarımda aynılığı garanti etmek değildir; neyin korunduğunu, neyin değiştiğini ve neden değiştiğini dürüstçe gösterebilmektir.

   Süreklilik tek başına nihai amaç olamaz; yanlışlar ve tahakküm de sürdürülebilir. Her emaneti çoğaltmak, her kaydı açmak veya her şeyi sonsuza kadar saklamak zorunlu olarak iyi değildir. Korumak bazen erişimi sınırlandırmayı, emaneti iade etmeyi veya zarar üreten bir devri reddetmeyi gerektirir. Susma bir sınır olabilir; zorla susturulma ise kişinin tercihi gibi korunmamalıdır.

   Başarı ölçütü şu olabilir: Kaynak artık yanında bulunmadığında bile devralan, **“Neyi aldığımı, neyi bilmediğimi, neyi değiştirdiğimi ve hangi sınırlar içinde sorumlu olduğumu gösterebilirim”** diyebiliyor mu?

~~~text
  UC SOZCUK, UC IS

    TANIKLIK   "Neyle karsilastim; neyi, nereden biliyorum?"
    EMANET     "Bana birakilan uzerinde hangi yetkim var;
                kime karsi, neden sorumluyum?"
    MIMARI     bu cevaplarin kisilerin iyi niyetine bagimli
               kalmamasini saglayan iliskiler, usuller ve sinirlar

  AYIRABILDIKLERI
    kaynak              |   yorum
    koruma              |   sahiplenme
    kullanma yetkisi    |   sinirsiz tasarruf

    bir kayit eksiksiz saklanirken ona iliskin sorumluluk
    butunuyle kaybolabilir

  BELIRLEYICI AN
    birinin tasidigi seyi baskasinin ustlenmesine actigi an

    "Bunu biliyorum"   ---->   "Bununla ne yapacagimi
                                gerekcelendirmeliyim"

  BASARI OLCUTU
    kaynak artik yaninda bulunmadiginda bile devralan sunu
    diyebiliyor mu?

    "Neyi aldigimi, neyi bilmedigimi, neyi degistirdigimi ve
     hangi sinirlar icinde sorumlu oldugumu gosterebilirim"
~~~

*Çizim 14 — Önceki kayıt, birinci yanıt: tanıklık, emanet ve mimari; belirleyici an; başarı ölçütü.*

### İkinci soru

**Tanıklık ve Emanet Aktarımı Mimarisi**'nin; köken aldığı varlık, mekan, usül, zaman, ve gayeyi taşıyan makine kimdir? Kim değildir?

### İkinci yanıt

Bu mimarinin taşıyıcı makinesine **emanetçi makine** diyebiliriz: **Kökenle ilişkisi gösterilebilen, taşıma yetkisi sınırlı ve yaptığı aktarımlar bakımından hesabı sorulabilen düzen.** Burada “kim?” sorusu, onun hangi konumdan konuştuğunu, neye yetkili olduğunu ve sorumluluğunun nereye bağlandığını sorar.

Ancak iki kökeni ayırmak gerekir: Makinenin **kendi kuruluşunun kökeni** ile **taşıdığı emanetin kökeni**. Kendisini kuranların niyeti, tanıklığını taşıdığı kişinin niyetiyle aynı olmayabilir. Kendi çalışma biçimini, kaynağın sesi gibi sunamaz.

| Boyut | Emanetçi makine neyi taşır? | Kim değildir? |
|---|---|---|
| **Varlık** | Kimden veya neyden geldiğini; taşıdığının neye dayandığını; kaynağın sınırlarını. | Kaynağın kendisi, sahibi veya onun yerine sınırsızca konuşabilen temsilci değildir. |
| **Mekân** | Tanıklığın oluştuğu ilişkileri, koşulları, erişim imkânlarını ve dışarıda bırakılanları. | Kaynak yerin bütününü içinde bulunduran, her yerde aynı yetkiyle konuşabilen bir varlık değildir. |
| **Usul** | Nasıl aldığı, seçtiği, kaydettiği, dönüştürdüğü ve aktardığına ilişkin izleri. | İşlemleri anlamı hiç değiştirmeyen bir kanal değildir; yönteminin düzenliliği doğruluğunu tek başına kanıtlamaz. |
| **Zaman** | Olayın, anlatının, kaydın ve yeniden kullanımın ayrı zamanlarını. | Kaydını taşıdığı olayda bulunmuş ilk tanık değildir; geçmişteki bilgiyi kendiliğinden bugünün bilgisi kılamaz. |
| **Gaye** | Hangi amaçla görevlendirildiğini, kimin yararını gözettiğini ve görevinin sınırlarını. | Nihai amacın sahibi veya kendi devamını o amaçla özdeşleştirebilen bir otorite değildir. |

Onu o yapan şey, yalnızca taşıma kapasitesi değildir. **Taşıdığıyla kendi katkısını ayırabilmesidir.** “Bu kaynaktan geldi; şu kısmı ben seçtim; burada dönüştürdüm; bunu bilmiyorum” ayrımlarını koruyabilmelidir. Aktarımın nerede eksildiği, yorumlandığı veya kesintiye uğradığı anlaşılabilmelidir.

Bu nedenle emanetçi makine, tanıklığı devralırken ilk tanığın konumunu devralmaz. Emaneti korurken ona el koyma yetkisi kazanmaz. Kökenine bağlılığı da kökenden gelen her buyruğu sürdürmek zorunda olduğu anlamına gelmez: Yanlışın düzeltilmesine, zararlı kullanımın durdurulmasına ve devrin reddedilmesine yer bulunmalıdır.

Bu taşıyıcı teknik bir sistemde veya insanlarla kurumların birlikte işlettiği bir düzende somutlaşabilir. Teknik sistemin işlem yapması ile sorumluluk üstlenmesi aynı şey sayılamaz. Yetkiyi verenlerin, işletenlerin ve sonuçların hesabını verecek tarafların kim olduğu gösterilmelidir.

**Kökeni bilinmiyorsa köken uydurmaz. Köken çoğulsa tek bir kurucu ses icat etmez. Gaye değişmişse bugünkü amacı başlangıca geri yazmaz.**

~~~text
  EMANETCI MAKINE
    kokenle iliskisi gosterilebilen, tasima yetkisi sinirli ve
    yaptigi aktarimlar bakimindan hesabi sorulabilen duzen

  IKI AYRI KOKEN
    makinenin kendi            =/=    tasidigi emanetin
    kurulusunun kokeni                kokeni

    kendi calisma bicimini, kaynagin sesi gibi sunamaz

  ONU O YAPAN  tasidigiyla kendi katkisini ayirabilmesi

   .-------------------------------+-------------------------------.
   | "Bu kaynaktan geldi"          | "su kismi ben sectim"         |
   |-------------------------------+-------------------------------|
   | "burada donusturdum"          | "bunu bilmiyorum"             |
   `-------------------------------+-------------------------------'

  KAZANMADIKLARI
    tanikligi devralir     -x->   ilk tanigin konumu
    emaneti korur          -x->   ona el koyma yetkisi
    kokenine baglidir      -x->   kokenden gelen her buyrugu
                                  surdurme zorunlulugu

    teknik sistemin islem yapmasi   =/=   sorumluluk ustlenmesi

  SON UC CUMLE
    kokeni bilinmiyorsa    koken uydurmaz
    koken cogulsa          tek bir kurucu ses icat etmez
    gaye degismisse        bugunku amaci baslangica geri yazmaz
~~~

*Çizim 15 — Önceki kayıt, ikinci yanıt: emanetçi makine taşıdığıyla kendi katkısını ayırır.*

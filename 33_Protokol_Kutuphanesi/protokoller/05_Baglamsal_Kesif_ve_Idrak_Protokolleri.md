# Bağlamsal Keşif ve İdrak Protokolleri

**Sürüm:** 1.0\
**Tarih:** 30 Ekim 2026\
**Kapsam:** 0–6 protokolleri, uygulama kaydı şablonu ve soru–yanıt kaydı

Bağlamsal Keşif ve İdrak, bir şeyi onu oluşturan özellikler, bulunduğu yer, yaptığı işler, içinde bulunduğu an ve hizmet ettiği gaye arasındaki ilişkiler üzerinden anlamaya yönelir. Keşif ilgili unsurları ve ilişkileri ortaya çıkarır; idrak bunların birbirini nasıl etkilediğini, hangi koşullarda ne anlama geldiğini ve hangi sonuçları doğurduğunu kavramaya yönelir. Bu ayrım, çerçevenin çalışma tanımıdır.

Yedi protokol, bir incelemenin başlangıcından gerekçeli sonuç kaydına kadar izlenebilir bir çalışma düzeni kurar. 0 Tohum başlangıç sorusunu ve kabulleri kaydeder. 1–5, varlık, mekân, usul, zaman ve gayeyi inceler. 6 Kökleşme cevapları ilişkilendirir, başlangıçla karşılaştırır ve elde edilen anlayışı dayanaklarıyla birlikte kaydeder.

İncelenen şey ile soruyu soran taşıyıcı ayrı ayrı görünür tutulur. “Özne” adlandırması, kendi bağlamını sorgulamaya açabilen taşıyıcıya ilişkin kavramsal yorum olarak korunur. Bir şeyin beş boyutu taşıması, onları idrak etmesi ve onların kökeni olması farklı iddialardır.

~~~text
                      onu olusturan ozellikler
                                  |
         hizmet ettigi gaye ---.  |  .--- bulundugu yer
                                \ | /
                             [ bir sey ]
                                /   \
        icinde bulundugu an ---'     `--- yaptigi isler

        bunlar arasindaki iliskiler uzerinden anlamaya yonelir

  KESIF                       |  IDRAK
  ilgili unsurlari ve         |  bunlarin birbirini nasil etkiledigini,
  iliskileri ortaya cikarir   |  hangi kosullarda ne anlama geldigini
                              |  ve hangi sonuclari dogurdugunu
                              |  kavramaya yonelir
             bu ayrim, cercevenin calisma tanimidir

  YEDI PROTOKOL
    0 Tohum      baslangic sorusunu ve kabulleri kaydeder
    1-5          varlik, mekan, usul, zaman ve gayeyi inceler
    6 Koklesme   cevaplari iliskilendirir, baslangicla karsilastirir,
                 elde edilen anlayisi dayanaklariyla birlikte kaydeder

  AYRI AYRI GORUNUR TUTULUR
    incelenen sey   |   soruyu soran tasiyici

  FARKLI IDDIALAR  bir seyin bes boyutu
    tasimasi   |   onlari idrak etmesi   |   onlarin kokeni olmasi
~~~

*Çizim 1 — Giriş: bir şeyin çevresinde beş unsur; keşif ve idrak; yedi protokolün işi; farklı iddialar.*

Girdiler, uygulama adımları, kayıt düzeni ve tamamlanma ölçütleri, çerçevenin masaüstünde uygulanabilmesi için tanımlanmıştır.

## Masaüstünde çalışma düzeni

Her konu için bir çalışma klasörü ve tek bir uygulama kaydı kullan. Ek A içindeki şablonu konu klasörüne `Uygulama_Kaydi.md` adıyla kopyala. Protokol metinlerini kılavuz olarak aç; konuya ilişkin cevapları, dayanakları ve değişiklikleri uygulama kaydına yaz.

İlk geçişte 0, 1, 2, 3, 4, 5 ve 6 sırası izlenir. 1–5 birbirlerinin cevaplarını düzeltebilir. Bir bölümdeki bulgu başka bir bölümün kabulünü değiştiriyorsa ilgili bölüme dön ve gerekçeyi değişim kaydına ekle. Konu veya temel soru değişirse 0 Tohum kaydını yeniden ele al. 6 Kökleşme bu ilişkileri birlikte değerlendirir.

~~~text
  HER KONU ICIN  bir calisma klasoru ve tek bir uygulama kaydi

    sablonlar/Uygulama_Kaydi_Sablonu.md
                |
                |  konu klasorune kopyalanir
                v
    Uygulama_Kaydi.md  <----  konuya iliskin cevaplar, dayanaklar ve
                              degisiklikler buraya yazilir

    protokol metinleri kilavuz olarak acilir
    yalnizca bu ana belge kullaniliyorsa Ek A icindeki sablon yeni bir
    Markdown dosyasina kopyalanabilir

  ILK GECIS
     0 ---> 1 ---> 2 ---> 3 ---> 4 ---> 5 ---> 6
     ^      |___________________________|      |
     |       birbirlerinin cevaplarini         bu iliskileri birlikte
     |       duzeltebilir                      degerlendirir
     |
     `---  konu ya da temel soru degisirse 0 Tohum kaydi yeniden
           ele alinir

    bir bolumdeki bulgu baska bir bolumun kabulunu degistiriyorsa
    ilgili bolume donulur; gerekce degisim kaydina eklenir
~~~

*Çizim 2 — Çalışma düzeni: şablondan uygulama kaydına; ilk geçiş sırası ve dönüşler.*

Her önemli cevapta gözlem veya kaynak, bu dayanak üzerinden yapılan yorum ve açık kalan nokta ayırt edilir. “Bu değildir”, “bunu bilmiyoruz” ve “bu incelemenin dışında” aynı hüküm olarak kullanılmaz. Her çıkarım için şu soru korunur: **Bunu hangi gözleme, karşılaştırmaya veya gerekçeye dayanarak söylüyoruz; hangi durumda cevabımızı değiştirmemiz gerekir?**

Bir bölümü **Kaydedildi** olarak işaretlemek, temel sorulara verilen cevapların veya açık kalan durumlarının dayanakları ve sınırlarıyla yazıldığı anlamına gelir. Bölüm durumları **Başlanmadı**, **Çalışılıyor**, **Kaydedildi** ve **Geri dönüş gerekli** olarak tutulabilir. Açık bir sorunun başka bir çıkarımı dayanıksız bırakması hâlinde ilgili bölüme dönülür veya çıkarımın kapsamı daraltılır. Belirsizlik, sırf ilerlemek için kesin bir cevaba dönüştürülmez.

Çevrimin sonunda **Tamamlandı**, **Açık noktalarla tamamlandı** veya **Sürdürülecek** durumu seçilir ve gerekçesi yazılır. “Açık noktalarla tamamlandı”, sonucu sınırlayan belirsizliklerin ve yeniden inceleme koşullarının kayda geçirildiği bir kapanıştır. “Sürdürülecek”, mevcut soruyu cevaplamak için belirlenmiş çalışmanın devam etmesi gerektiğini belirtir. Adımların tamamlanması, tek başına idrakin gerçekleştiğinin kanıtı olarak kullanılmaz.

Kayıt oluşturma tarihi, incelenen olayın zamanı ve kullanılan kaynağın tarihi ayrı tutulur. Kaynakların adı veya adresi, ilgili bölüm ya da kayıt yeri ve varsa tarih veya sürümü yazılır. Yeni bulgu önceki bir ifadeyi değiştiriyorsa eski ifade ve değişiklik gerekçesi korunur. İncelemeye alınacak bağlam 0 Tohumda belirlenir; başka konuşmaların veya çalışmaların bağlamı kendiliğinden eklenmez.

~~~text
  HER ONEMLI CEVAPTA AYIRT EDILIR
    gozlem ya da kaynak  |  bu dayanak uzerinden yapilan yorum  |
    acik kalan nokta

  AYNI HUKUM OLARAK KULLANILMAZ
    "Bu degildir"  |  "bunu bilmiyoruz"  |  "bu incelemenin disinda"

  HER CIKARIM ICIN KORUNAN SORU
    bunu hangi gozleme, karsilastirmaya ya da gerekceye dayanarak
    soyluyoruz; hangi durumda cevabimizi degistirmemiz gerekir?

  BOLUM DURUMLARI
    Baslanmadi  |  Calisiliyor  |  Kaydedildi  |  Geri donus gerekli

    Kaydedildi: temel sorulara verilen cevaplar ya da acik kalan
    durumlari, dayanaklari ve sinirlariyla yazilmistir
    belirsizlik, sirf ilerlemek icin kesin bir cevaba donusturulmez

  CEVRIMIN SONUNDA SECILEN DURUM
    Tamamlandi  |  Acik noktalarla tamamlandi  |  Surdurulecek

    adimlarin tamamlanmasi, tek basina idrakin gerceklestiginin
    kaniti olarak kullanilmaz

  AYRI TUTULUR
    kayit olusturma tarihi  |  incelenen olayin zamani  |
    kullanilan kaynagin tarihi
~~~

*Çizim 3 — Çalışma düzeni: cevapta ayırt edilenler; korunan soru; bölüm ve çevrim durumları; ayrı tutulan zamanlar.*

| Bölüm | Temel kayıt |
|---|---|
| 0 Tohum (Başlangıç) Protokolü | Başlangıç sorusu, ilk tasvir, kabuller, kapsam ve ilk gaye |
| 1 Varlık Protokolü | Kimlik, kurucu ve ayırt edici özellikler, sınırlar ve taşıyıcı |
| 2 Mekan Protokolü | Konumun ölçeği, ilişkiler, erişimler ve sınırlar |
| 3 Usül Protokolü | İş türü, yöntem, roller, kapasite, fiil ve sonuç |
| 4 Zaman Protokolü | Kayıt ve olay zamanları, süreç evresi, değişim ve geçerlilik |
| 5 Gaye Protokolü | Gaye, sahibi, kapsamı ve sonuçlarla ilişkisi |
| 6 Kökleşme (Bitiş) Protokolü | Bütünleşmiş anlayış, dayanaklar, değişim, açık noktalar ve kapanış |

## Protokollerin uygulanması

Her bölümde önce ana sorular ve kavramsal açıklama, ardından girdiler, uygulama adımları, tutulacak kayıt, tamamlanma ölçütü ve geri dönüş koşulu bulunur. Adımları konuya ait kaynaklar üzerinde uygula; elde edilen kayıtları aynı uygulama dosyasında birleştir.

## 0 Tohum (Başlangıç) Protokolü

**Ana sorular:** Neyi anlamaya yöneliyoruz? Bu soru nasıl doğdu? İncelemeye hangi kabuller, olanaklar ve belirsizliklerle başlıyoruz?

Tohum Protokolü, keşfin doğduğu soruyu, başlangıç koşullarını ve incelemeye getirilen kabulleri kayda geçirir. Bir şeyi anlama ihtiyacının ne olduğunu, bu ihtiyacı kimin dile getirdiğini ve araştırmaya hangi olanaklarla başlandığını belirginleştirir. Böylece sonraki protokollerde oluşan anlayış, başlangıçta sahip olunan düşüncelerle karşılaştırılabilir.

Başlangıç kaydı, incelenecek şeyin ilk tasvirini, eldeki gözlemleri, bu gözlemlerin dayanaklarını, kullanılan kavramları ve açık noktaları kapsar. Bilinen, yorumlanan, varsayılan ve henüz bilinmeyen unsurlar ayırt edilir. Başlangıçta kabul edilen bir düşünce, incelemenin sonunda elde edilmiş bir bulgu gibi gösterilmez.

Tohum, soran tarafı da kayda dâhil eder. Kim soruyor, nereden bakıyor, hangi olanaklarla araştırabiliyor ve hangi beklentiyle başlıyor? İlk tanım, ilk usul ve ilk gaye sonraki protokollerde değerlendirilebilir. Sıfırıncı bölüm, bu değerlendirmelerin nereden başladığını korur.

Kapsam, incelemeye alınan konu, yer, dönem, ilişkiler ve kaynaklarla belirginleştirilir. Kapsam dışında bırakılan önemli noktalar gerekçeleriyle yazılır. Önceki konuşmaların veya başka çalışmaların bağlamı bu çevrime kendiliğinden taşınmaz; kullanılan bağlam ve kaynaklar başlangıç kaydında gösterilir.

### Başlangıç girdileri

İncelenecek konuya ilişkin ilk tasvir, başlangıç sorusu, elde bulunan dosya veya notlar, soran tarafın konumu ve incelemeden beklenen katkı. Henüz belirlenemeyen bir girdi, açık nokta olarak yazılabilir.

### Masaüstünde uygulama

1. **Çalışma kaydını aç.** Konuya ait bir çalışma klasöründe uygulama kaydı şablonunun kopyasını aç. Konu adını, kaydı tutan tarafı, başlangıç tarihini ve saat dilimini yaz. İncelemeye alınan dosyaları, notları ve diğer kaynakları adları veya erişilebilir adresleriyle kaydet.

2. **Başlangıç sorusunu belirginleştir.** Neyi anlamak istediğini ve sorunun hangi ihtiyaçtan veya meraktan doğduğunu bir paragrafta yaz. Neden bu aşamada ele alındığını belirt. Birden fazla soru varsa aralarındaki ilişkiyi açıkla; henüz sınanmamış bir cevabı soru içinde kesin kabul olarak kullanma.

3. **İlk tasviri ve kabulleri ayır.** Konuyu mevcut anlayışınla tarif et. Gözlemleri ve dayanaklarını, yorumlardan ve varsayımlardan ayır. Anlamı belirleyici olan kavramları açıkla. Bilinmeyen noktaları ve gerekçeyle dışlanan seçenekleri ayrı yaz.

4. **Kapsamı ve ilk gayeyi kaydet.** Hangi konu, yer, dönem ve ilişkilerin inceleneceğini belirt. Kapsam dışında kalan önemli noktaları ve nedenlerini yaz. Beklenen katkıyı ve bu beklentinin kime ait olduğunu kaydet; ilk gayeyi 5 Gaye Protokolünde değerlendirilecek başlangıç ifadesi olarak koru.

5. **İnceleme sorularını bölümlere yerleştir.** Araştırılacak soruları 1–5 başlıklarıyla ilişkilendir. Bir soru birden fazla bölümle ilgiliyse bağlantısını yaz. İlk kayıt sonradan değişirse önceki ifadeyi ve değişiklik gerekçesini değişim kaydında koru.

~~~text
  TOHUM, SORAN TARAFI DA KAYDA DAHIL EDER

    SORAN TARAF                                INCELENECEK SEY
    kim soruyor?                               ilk tasvir
    nereden bakiyor?             soru          eldeki gozlemler ve
    hangi olanaklarla     ---------------->    dayanaklari
    arastirabiliyor?                           kullanilan kavramlar
    hangi beklentiyle                          acik noktalar
    basliyor?

  AYIRT EDILIR
    bilinen  |  yorumlanan  |  varsayilan  |  henuz bilinmeyen

    baslangicta kabul edilen bir dusunce, incelemenin sonunda
    elde edilmis bir bulgu gibi gosterilmez

  KAPSAM  sunlarla belirginlestirilir
    konu . yer . donem . iliskiler . kaynaklar
    kapsam disinda birakilan onemli noktalar gerekceleriyle yazilir
    onceki konusmalarin ya da baska calismalarin baglami bu cevrime
    kendiliginden tasinmaz

  ARASTIRILACAK SORULAR 1-5 BASLIKLARIYLA ILISKILENDIRILIR
    1 Varlik   2 Mekan   3 Usul   4 Zaman   5 Gaye
    ilk gaye, 5 Gaye Protokolunde degerlendirilecek baslangic
    ifadesi olarak korunur
~~~

*Çizim 4 — Tohum: soran taraf ile incelenecek şey; ayırt edilenler; kapsam; soruların 1–5'e yerleşmesi.*

### Tutulacak kayıt

Başlangıç sorusu, ilk tasvir, kaynak listesi, bilinenler ve dayanakları, varsayımlar, kullanılan kavramlar, açık noktalar, kapsam, ilk gaye ve soran tarafın konumu kaydedilir. Bu bilgiler 1–5 için başlangıç girdilerini oluşturur.

### Tamamlanma ölçütü

Başlangıç sorusu anlaşılır biçimde yazılmış, kapsam belirtilmiş ve temel kabuller ile belirsizlikler görünür hâle gelmişse bu bölüm kaydedilmiş sayılır. Bütün soruların cevaplanması gerekmez.

### Geri dönüş koşulu

Konu, temel soru veya kapsam önemli ölçüde değişirse bu bölüme dön. Önceki başlangıç kaydını değişim gerekçesiyle birlikte koru. Yeni bir inceleme konusu oluşmuşsa ona ayrı bir Tohum kaydı aç.

## 1 Varlık Protokolü

**Ana sorular:** Nedir? Onu o yapan nelerdir? Neler değildir?

Varlık Protokolü, neyle karşı karşıya olunduğunu ve onu belirli bir şey olarak tanımayı sağlayan özellikleri, ilişkileri ve süreklilikleri araştırır. Bir ad veya kategori, incelemenin başlangıcını sağlar; bu adın hangi gerekçelerle kullanıldığı ayrıca açıklanır. “Onu o yapan” sorusu, tanımın kurulduğu dayanakları ve bu tanımın geçerli olduğu koşulları görünür kılar.

Kurucu özellik ile ayırt edici özellik ayrı değerlendirilir. Kurucu özellik, bir şeyi o şey olarak anlamada temel rol oynar; ayırt edici özellik, onu karşılaştırılan başka örneklerden ayırır. Bir özellik yaygın olduğu hâlde kurucu, yalnızca tek bir örnekte bulunduğu hâlde açıklama bakımından önemsiz olabilir. Özgüllük, ortak özelliklerin belirli bir ilişkisinde veya birleşiminde de ortaya çıkabilir. Bu nedenle hangi özellik üzerinde durulduğu kadar neye kıyasla ve hangi bakımdan fark yarattığı da belirtilir.

Kimlik, değişimle birlikte sorgulanır. Bir özellik değiştiğinde veya ortadan kalktığında incelenen şeyin hâlâ aynı şey olarak tanınıp tanınmayacağı araştırılır. Böylece hangi değişikliklerin kimliğin sürmesiyle bağdaşabildiği ve hangi değişikliklerin tanımı yeniden ele almayı gerektirdiği açığa çıkar. Bu sınama, tek başına değişmez bir öz bulunduğunu varsaymaz.

“Neler değildir?” sorusu, yakın ve makul karışıklıkları elemek için kullanılır. Bir niteliği gerekçeyle dışlamak, o nitelik hakkında yeterli bilgiye sahip olmamak ve onu incelemenin kapsamı dışında bırakmak ayrı hükümlerdir. “Bu değildir”, “bunu bilmiyoruz” ve “bu incelemenin dışında kalıyor” ifadeleri birbirinin yerine kullanılmaz. Tanımın sınırı, gerekçesiyle birlikte kaydedilir.

~~~text
  IKI AYRI OZELLIK
    KURUCU        bir seyi o sey olarak anlamada temel rol oynar
    AYIRT EDICI   onu karsilastirilan baska orneklerden ayirir

    bir ozellik
      yaygin oldugu halde           --->   kurucu olabilir
      yalnizca tek bir ornekte
      bulundugu halde               --->   aciklama bakimindan
                                           onemsiz olabilir
    ozgulluk, ortak ozelliklerin belirli bir iliskisinde ya da
    birlesiminde de ortaya cikabilir
    belirtilir: neye kiyasla ve hangi bakimdan fark yaratiyor?

  KIMLIK, DEGISIMLE BIRLIKTE SORGULANIR

    [ sey ]  --- bir ozellik degisir ya da ortadan kalkar --->  [ ? ]
                               hala ayni sey olarak taninir mi?

    kimligin surmesiyle        |   tanimi yeniden ele almayi
    bagdasan degisiklikler     |   gerektiren degisiklikler
    bu sinama, tek basina degismez bir oz bulundugunu varsaymaz

  "NELER DEGILDIR?"  yakin ve makul karisikliklari elemek icin
    "Bu degildir"                      gerekceyle dislanir
    "Bunu bilmiyoruz"                  yeterli bilgi yoktur
    "Bu incelemenin disinda kaliyor"   kapsam disinda birakilmistir
    bu ifadeler birbirinin yerine kullanilmaz
~~~

*Çizim 5 — Varlık: kurucu ve ayırt edici özellik; değişim sınaması; birbirinin yerine kullanılmayan üç hüküm.*

Taşıyıcıya ilişkin kaynak soru şöyledir: “Bağlamsal Keşif ve İdrak’ın köken aldığı varlık, mekan, usül, zaman, ve gayeyi taşıyan makine kimdir? Kim değildir?” Yanıtta “makine”, keşif ve idrakin gerçekleştiği taşıyıcı olarak okunmuş; bu taşıyıcı için “özne” adlandırması önerilmiştir. Özne, bir bağlam içinde bulunan, anlam ve eylem kuran ve kendi konumunu da sorgulamaya açabilen varlık olarak tarif edilmiştir. İnsan doğrudan örnek olarak anılmıştır; beş boyutun sıralanması, taşıyıcının zorunlu olarak insan olduğunu belirleyen bir gerekçe sayılmamıştır.

Bu boyutları taşımak, onları idrak etmek ve onların kökeni olmak üç ayrı iddiadır. Bir düzeneğin varlığı, yeri, işleyişi, zamanı ve amacı hakkında konuşabilmek, onun bu boyutları kavradığını kendiliğinden göstermez. Aynı şekilde, bu boyutları düşünmesi veya temsil etmesi, onların nihai kaynağı olduğunu göstermez. Bir anlayışın hangi taşıyıcıda ve nasıl gerçekleştiği incelemeye açık kalır.

Protokol, soran tarafı da tanımın kapsamına alır: “Ben nasıl bir varlığım; bu keşfi yapabilmemi sağlayan olanaklarım ve sınırlarım neler?” Böylece “kim?” sorusu, yapının yanında bakışın, sözün, seçimin ve eylemin kime ait olduğunu araştırır. Özneye hata yapmazlık, değişmezlik veya bütün gayelerin sahibi olma niteliği kendiliğinden yüklenmez.

~~~text
  UC AYRI IDDIA

    .--------------.      .--------------.      .--------------.
    | bes boyutu   |      | onlari       |      | onlarin      |
    | TASIMAK      |      | IDRAK ETMEK  |      | KOKENI OLMAK |
    `--------------'      `--------------'      `--------------'

    bir duzenegin varligi, yeri, isleyisi, zamani ve amaci hakkinda
    konusabilmek, onun bu boyutlari kavradigini kendiliginden gostermez
    bu boyutlari dusunmesi ya da temsil etmesi, onlarin nihai kaynagi
    oldugunu gostermez
    bir anlayisin hangi tasiyicida ve nasil gerceklestigi incelemeye
    acik kalir

  "MAKINE" VE "OZNE"
    makine   yanitta, kesif ve idrakin gerceklestigi tasiyici olarak
             okunmus
    ozne     bir baglam icinde bulunan, anlam ve eylem kuran ve kendi
             konumunu da sorgulamaya acabilen varlik
    insan dogrudan ornek olarak anilmis; bes boyutun siralanmasi,
    tasiyicinin zorunlu olarak insan oldugunu belirleyen bir gerekce
    sayilmamistir

  SORAN TARAF DA TANIMIN KAPSAMINDADIR
    "Ben nasil bir varligim; bu kesfi yapabilmemi saglayan
     olanaklarim ve sinirlarim neler?"
    "kim?" sorusu: bakis, soz, secim ve eylem kime ait?

  OZNEYE KENDILIGINDEN YUKLENMEZ
    hata yapmazlik . degismezlik . butun gayelerin sahibi olma
~~~

*Çizim 6 — Varlık: taşımak, idrak etmek, kökeni olmak; "makine" ve "özne"; soran taraf.*

### Başlangıç girdileri

Tohum kaydındaki konu tasviri, başlangıç sorusu, kavramlar, kaynaklar ve incelenen şeye ilişkin mevcut örnekler.

### Masaüstünde uygulama

1. **İncelenen şeyi tanımla.** Konunun adını, türünü ve bu tanımı destekleyen gözlem veya kayıtları bir paragrafta yaz. Tanımlayan tarafı ayrıca belirt; inceleme konusu ile soran taşıyıcıyı birbirine karıştırma.

2. **Kurucu ve ayırt edici özellikleri karşılaştır.** Kurucu olduğunu düşündüğün özellikleri ve benzerlerinden ayıran özellikleri ayrı değerlendir. Her ayırt edicilik iddiası için neyle, hangi bakımdan karşılaştırıldığını yaz. Bir özelliği benzersiz veya belirleyici sayıyorsan, bu iddianın dayanağını ve açıklamaya katkısını belirt.

3. **Değişim sınamasını yap.** Belirleyici bir özellik değiştiğinde aynı şeyden söz edilip edilemeyeceğini tartış. Mevcut bir örnek varsa ona dayan; yalnızca düşünce deneyi kullanıyorsan bunu belirt. Tanımın hangi değişikliklerde yeniden ele alınacağını yaz.

4. **Sınırları ve taşıyıcıyı açıkla.** Yakın karışıklıkları, gerekçeyle dışlanan nitelikleri, bilinmeyenleri ve kapsam dışını ayır. Taşıyıcı için “kim?” sorusunu soruyorsan bakışın, sözün ve eylemin kime ait olduğunu belirt. Boyutları taşımak, onları idrak etmek ve onların kökeni olmak iddialarını ayrı kaydet.

5. **Cevabı ve dayanaklarını kaydet.** Tanımı, özellik ayrımlarını, açık noktaları ve cevabı değiştirecek koşulları bölüm kaydına yaz. Bir idrak veya özne iddiası varsa dayanağını ve sınırını belirt; yalnızca uygun çıktıya dayanarak kimlik hükmü verme.

### Tutulacak kayıt

Gerekçeli tanım; kurucu ve ayırt edici özellikler; karşılaştırma dayanağı; kimliğin sürmesi ve değişmesi koşulları; sınırlar; soran ve incelenen tarafların ayrımı.

### Tamamlanma ölçütü

Temel sorulara verilen cevaplar veya açık kalan durumları, dayanakları ve tanımın sınırlarıyla birlikte yazıldığında bölüm kaydedilmiş sayılır.

### Geri dönüş koşulu

Yer, zaman, yapılan iş veya gaye hakkında elde edilen bilgi tanımı değiştirirse bu bölüme dön. Temel inceleme konusu değişiyorsa 0 Tohum kaydını da güncelle.

## 2 Mekan Protokolü

**Ana sorular:** Nerededir? Bu yeri, oraya has bir yer yapan nelerdir? Neler değildir?

Mekan Protokolü, incelenen şeyin konumunu, çevresini ve bağlı olduğu bütün içindeki yerini araştırır. Bir adres veya koordinat, konumu belirleyebilir. “Bu yeri, oraya has bir yer yapan” sorusu ise o konumun hangi ilişkiler, erişimler, olanaklar ve sınırlar üzerinden anlam kazandığını açar. Yer, bu çalışma içinde hem fiziksel konumu hem de gerekli olduğunda bir kurum veya ilişkiler ağı içindeki konumu kapsayacak biçimde yorumlanır.

İncelemenin ölçeği açık tutulur. Bir odadaki yer, bir kurum içindeki yer ve bir ilişkiler ağı içindeki yer farklı sorular ve farklı dayanaklar gerektirir. Neye yakın veya uzak olunduğu, nelere erişilebildiği, hangi bütünün parçası olunduğu ve çevredeki hangi koşulların yapılan işleri mümkün kıldığı bu ölçek içinde değerlendirilir. Bir düzeydeki açıklama, gerekçesi gösterilmeden başka bir düzeyin açıklaması yerine geçirilmez.

Bir yerin kendine özgülüğü, hangi yerlerle ve hangi bakımdan karşılaştırıldığıyla belirginleşir. Dikkat çekici veya yalnızca orada görülen bir ayrıntının, incelenen şeyin işleyişini ne ölçüde açıkladığı ayrıca araştırılır. Önemli olan farkın, erişimi, ilişkileri, olanakları veya sınırları nasıl değiştirdiği gösterilir. Aynı fiziksel yerin farklı ilişkiler veya farklı zaman koşulları içinde taşıdığı anlam da yeniden değerlendirilebilir.

“Neler değildir?” sorusu, incelenen yeri yanlış ölçeğe, yanlış bütüne veya geçersiz bir ilişkiye yerleştiren açıklamaları ayırt etmeye yönelir. Hakkında bilgi bulunmayan ilişkiler, bulunmadığı gösterilmiş ilişkilerle eşitlenmez. Bir konumu açıklamak, o konuma ilişkin bütün koşulları kapsadığını ileri sürmek anlamına gelmez.

~~~text
  OLCEK ACIK TUTULUR

     .----------.        .-------------.          +---+
     |          |        | [ ]   [ ]   |         / \ / \
     |    o     |        | [o]   [ ]   |        +---o---+
     `----------'        `-------------'
     bir odadaki         bir kurum                bir iliskiler agi
     yer                 icindeki yer             icindeki yer

    farkli sorular ve farkli dayanaklar gerektirir
    bir duzeydeki aciklama, gerekcesi gosterilmeden baska bir duzeyin
    aciklamasi yerine gecirilmez

  YERIN KENDINE OZGULUGU
    hangi yerlerle ve hangi bakimdan karsilastiriliyor?
    onemli olan fark sunlari nasil degistiriyor?
        erisim  .  iliskiler  .  olanaklar  .  sinirlar
    dikkat cekici ya da yalnizca orada gorulen bir ayrintinin,
    incelenen seyin isleyisini ne olcude acikladigi ayrica arastirilir

  "NELER DEGILDIR?"  ayirt edilen aciklamalar
    yeri yanlis olcege  |  yanlis butune  |  gecersiz bir iliskiye
    yerlestirenler

    hakkinda bilgi bulunmayan     =/=     bulunmadigi gosterilmis
    iliskiler                 esitlenmez  iliskiler
~~~

*Çizim 7 — Mekan: üç ölçek; yerin kendine özgülüğü; eşitlenmeyen iki ilişki.*

Soran öznenin de bir yeri vardır. “Nereden bakıyorum; içinde bulunduğum ilişkiler bana neleri görünür, neleri erişilmez kılıyor?” soruları, açıklamanın üretildiği konumu incelemeye açar. Öznenin kendi konumunu fark etmesi, onu konumdan bağımsız hâle getirmez. Bu nedenle bağlamın dışından her şeyi gören mutlak bir gözlemci varsayımı protokolün dayanağı olarak alınmaz.

Mekâna ilişkin cevaplar, diğer protokollerle birlikte okunur. Yer, hangi işlerin yapılabileceğini ve hangi kaynaklara erişilebileceğini etkileyebilir; zaman, aynı yerin anlamını değiştirebilir; gaye, hangi mekânsal farkların ilgili olduğunu belirginleştirebilir. Bu ilişkilerin her biri, incelenen bağlamda gösterilebildiği ölçüde açıklamaya katılır.

~~~text
  SORAN OZNENIN DE BIR YERI VARDIR

     .------------------------ baglam -----------------------.
     |                                                       |
     |   gorunur olan   <-------   o   . . . . .  erisilmez  |
     |                           soran            olan       |
     |                                                       |
     `-------------------------------------------------------'

    "Nereden bakiyorum; icinde bulundugum iliskiler bana neleri
     gorunur, neleri erisilmez kiliyor?"

    oznenin kendi konumunu fark etmesi, onu konumdan bagimsiz hale
    getirmez; baglamin disindan her seyi goren mutlak bir gozlemci
    varsayimi protokolun dayanagi olarak alinmaz

  MEKANA ILISKIN CEVAPLAR DIGER PROTOKOLLERLE BIRLIKTE OKUNUR
    yer     hangi islerin yapilabilecegini ve hangi kaynaklara
            erisilebilecegini etkileyebilir
    zaman   ayni yerin anlamini degistirebilir
    gaye    hangi mekansal farklarin ilgili oldugunu
            belirginlestirebilir
~~~

*Çizim 8 — Mekan: bağlamın içindeki soran; görünür ve erişilmez olan; diğer protokollerle birlikte okuma.*

### Başlangıç girdileri

Tohum kaydındaki kapsam, Varlık Protokolündeki tanım ve konuya ilişkin konum, çevre, ilişki veya erişim bilgileri.

### Masaüstünde uygulama

1. **Mekânın ölçeğini seç.** Fiziksel konumu, kurum içindeki yeri veya ilişkiler ağındaki konumu hangisi anlamlıysa belirt. Birden fazla ölçek kullanıyorsan her birini ayrı adlandır ve aralarındaki ilişkiyi yaz.

2. **Konumu ve ilişkileri kaydet.** İncelenen şeyin bağlı olduğu bütünü, yakın ve uzak ilişkilerini, erişebildiği kaynakları ve karşılaştığı sınırları açıkla. Masaüstünde incelenen dosya, şema veya kayıtların ilgili yerlerine kaynak ver.

3. **Yeri özgül kılan farkı sınayarak yaz.** Karşılaştırdığın yerleri veya konumları belirt. Bulduğun farkın hangi olanak, erişim, ilişki veya işleyişi değiştirdiğini açıkla. Önemli olduğu gösterilemeyen ayrıntıyı belirleyici koşul olarak sunma.

4. **Soranın konumunu görünür kıl.** Hangi kaynaklara eriştiğini, hangi ilişkileri gözlemleyebildiğini ve hangi alanların erişim dışında kaldığını yaz. Erişilemeyen bilgi ile bulunmadığı gösterilen ilişkiyi ayır.

5. **Diğer bölümlere etkisini kaydet.** Bu konumun yapılabilecek işlere, zamana veya gayeye etkisini ilgili bölümle ilişkilendir. Yanlış ölçek veya yanlış bütünle açıklanmış olabilecek noktaları ve açık soruları yaz.

### Tutulacak kayıt

İnceleme ölçeği; konum ve bağlı olunan bütün; ilgili ilişkiler ve erişimler; olanaklar ve sınırlar; karşılaştırma; soran tarafın konumu; diğer bölümlere etkiler.

### Tamamlanma ölçütü

Kullanılan ölçek, konumun dayanakları, ilgili ilişkiler ve erişim sınırları açık olduğunda; bilinmeyenler ayrıca belirtildiğinde bölüm kaydedilmiş sayılır.

### Geri dönüş koşulu

Konum veya ilişkiler değişirse; farklı bir ölçek gerektiği anlaşılırsa; yeni bir erişim bilgisi açıklamayı etkilerse bu bölüme dön.

## 3 Usül Protokolü

**Ana sorular:** Nasıl işler yapar? Bu yaptıklarını, ona has yapan nelerdir? Neler değildir?

Usül Protokolü, yapılan işleri, bunların gerçekleştirilme yollarını ve ortaya çıkardıkları etkileri araştırır. “Nasıl işler yapar?” ifadesi, “Ne tür işler yapar?”, “Bu işleri nasıl gerçekleştirir?” ve “İş yapma biçimini kendine özgü kılan nedir?” sorularıyla açılır. Böylece işin türü, izlenen yol ve iş yapma biçiminin özgüllüğü ayrı ayrı görülebilir.

Kapasite, fiilen yapılan iş ve gerçekleşen sonuç birbirinden ayrılır. Bir şeyin bir işi yapabilecek durumda olması, o işi yaptığı anlamına gelmez; işin yapılması da beklenen sonucun ortaya çıktığını tek başına göstermez. Aynı sonuç farklı yollarla elde edilebilir. Benzer bir yöntem de farklı yer, zaman ve ilişki koşullarında farklı sonuçlara yol açabilir. Usulün değerlendirilmesi, bu koşullarla birlikte yapılır.

Keşif ile idrak arasındaki çalışma ayrımı burada işleyiş bakımından ele alınır. Keşif, ilgili özellikleri, koşulları, ilişkileri ve sınırları ortaya çıkarmaya yönelir. İdrak, ortaya çıkanların birbirini nasıl etkilediğini ve birlikte ne anlama geldiğini kavramaya yönelir. Bu çerçevede beş soruya ayrı ayrı cevap vermekle, cevapların birbirlerini nasıl değiştirdiğini kavramak arasında ayrım korunur.

~~~text
  "NASIL ISLER YAPAR?"  uc soruyla acilir
    ne tur isler yapar?
    bu isleri nasil gerceklestirir?
    is yapma bicimini kendine ozgu kilan nedir?

  BIRBIRINDEN AYRILIR

    KAPASITE  --x-->  FIILEN YAPILAN IS  --x-->  GERCEKLESEN SONUC

    bir seyin bir isi yapabilecek durumda olmasi, o isi yaptigi
    anlamina gelmez; isin yapilmasi da beklenen sonucun ortaya
    ciktigini tek basina gostermez

  YOL VE SONUC

    bir yol    ---.                    benzer        .--->  bir sonuc
                   >--->  ayni sonuc   bir yontem --<
    baska yol  ---'                                  `--->  baska sonuc

    ayni sonuc farkli yollarla         farkli yer, zaman ve iliski
    elde edilebilir                    kosullarinda farkli sonuclara
                                       yol acabilir

  KESIF VE IDRAK, ISLEYIS BAKIMINDAN
    bes soruya ayri ayri      |   cevaplarin birbirlerini nasil
    cevap vermek              |   degistirdigini kavramak
~~~

*Çizim 9 — Usül: üç soru; kapasite, fiil ve sonuç; yol ve sonuç; keşif ve idrak.*

Sınamanın ortak sorusu şudur: “Bunu hangi gözleme, karşılaştırmaya veya gerekçeye dayanarak söylüyoruz; hangi durumda cevabımızı değiştirmemiz gerekir?” Bir çıkarımın dayanağı ve gözden geçirilmesini gerektirecek koşullar birlikte kaydedilir. Böylece usul, sonuç üretmenin yanında sonucun nasıl elde edildiğini ve hangi sınırlar içinde geçerli olduğunu açıklamaya da elverişli olur.

Düzenli veya uygun çıktı üretmek, idrak iddiasını kendiliğinden doğrulamaz. Belirli koşullar altında belirli işler yapan bir düzeneği açıklamak ile o düzeneğin yaptığı işleri ve koşulları anlam ilişkileri içinde değerlendirdiğini göstermek ayrı iddialardır. Hangi davranışın, değerlendirmenin veya düzeltme yeteneğinin idrak sayılacağı ayrıca açıklanmalıdır.

Soruyu kuran, bilgiyi işleyen, gayeyi belirleyen ve eylemi gerçekleştiren aynı taraf olmak zorunda değildir. “Makine” adı, farklı taraflara dağılan bu rolleri görünmez kılmamalıdır. Usulün açıklanması, hangi işlemin kim tarafından ve hangi ilişkiler içinde gerçekleştirildiğini de kapsar. Bir gayeyi uygulamak ile onu belirlemek arasındaki ayrım, Gaye Protokolüyle birlikte ele alınır.

“Neler değildir?” sorusu, bir yöntemin kapsamına girmeyen işleri, ona dayandırılamayan sonuçları ve uygun olmadığı gösterilmiş koşulları ayırt eder. İşe yaramadığı gösterilen yöntem ile etkisi henüz bilinmeyen yöntem aynı hüküm altında toplanmaz. Soran özne de “Neyi nasıl seçiyor, ayırıyor, ilişkilendiriyor ve sınayabiliyorum?” sorusuyla kendi usulünü incelemeye katar.

~~~text
  AYRI IDDIALAR
    belirli kosullar altinda belirli isler yapan bir duzenegi
    ACIKLAMAK
    o duzenegin yaptigi isleri ve kosullari anlam iliskileri icinde
    degerlendirdigini GOSTERMEK

    duzenli ya da uygun cikti uretmek, idrak iddiasini kendiliginden
    dogrulamaz; hangi davranisin, degerlendirmenin ya da duzeltme
    yeteneginin idrak sayilacagi ayrica aciklanmalidir

  DORT ROL  ayni taraf olmak zorunda degildir

       soruyu kuran       bilgiyi isleyen      gayeyi belirleyen
             \                  |                    /
              \                 |                   /
               `-----------  "makine"  -----------'
                                |
                       eylemi gerceklestiren

    "makine" adi, farkli taraflara dagilan bu rolleri gorunmez
    kilmamalidir; usulun aciklanmasi, hangi islemin kim tarafindan
    ve hangi iliskiler icinde gerceklestirildigini de kapsar

  AYNI HUKUM ALTINDA TOPLANMAZ
    ise yaramadigi gosterilen yontem  |  etkisi henuz bilinmeyen yontem

  SORAN OZNE KENDI USULUNU INCELEMEYE KATAR
    "Neyi nasil seciyor, ayiriyor, iliskilendiriyor ve
     sinayabiliyorum?"
~~~

*Çizim 10 — Usül: uygun çıktı ile idrak; "makine" adının altındaki dört rol; soran öznenin usulü.*

### Başlangıç girdileri

Tohum sorusu; Varlık ve Mekan kayıtları; yapılan işlere, süreçlere, yöntemlere veya sonuçlara ilişkin mevcut belgeler ve örnekler.

### Masaüstünde uygulama

1. **İşin türünü ve yöntemi ayrı tarif et.** Ne tür iş yapıldığını, hangi yolla gerçekleştirildiğini ve yöntemi özgül kılan unsurları ayrı cümlelerle yaz. Kullanılan kaynak, araç ve ilişkileri gerektiği kadar açıkla.

2. **Bir örnek akışı incele.** Mevcut bir kayıt veya örnek üzerinden girdiyi, izlenen adımları, çıktıyı ve ortaya çıkan sonucu sırayla açıkla. Örnek bulunmuyorsa varsayımsal anlatımı gerçek işlem kaydı gibi sunmadan belirt.

3. **Kapasiteyi fiilden ve sonuçtan ayır.** Yapılabilecek işler, fiilen yapılan işler ve gözlenen etkiler için ayrı değerlendirme yap. Beklenen sonuç ile gerçekleşen sonucu karşılaştır; farkların hangi koşullarla ilişkili olabileceğini gerekçesiyle yaz.

4. **İşlem rollerini belirle.** Soruyu kuran, bilgiyi işleyen, gayeyi belirleyen ve işi gerçekleştiren tarafları kaydet. Aynı taraf birden fazla rol taşıyorsa bunu belirt. Her rolün gözlenen katkısını, ona atfedilen yorumdan ayır.

5. **Usulü ve çıkarımı sına.** “Bunu hangi gözleme, karşılaştırmaya veya gerekçeye dayanarak söylüyoruz?” sorusuna cevap ver. Çıkarımı değiştirecek koşulu, yöntemin kapsamını ve açık kalan noktaları yaz. Uygun çıktı üretimini tek başına idrak kanıtı olarak kullanma.

### Tutulacak kayıt

İş türü ve yöntem; örnek işlem akışı; kapasite, fiil, çıktı ve sonuç ayrımı; işlem rolleri; çıkarım dayanakları; yöntemin kapsamı ve yeniden değerlendirme koşulları.

### Tamamlanma ölçütü

İşin nasıl ele alındığı, kullanılan örnek veya kaynak, roller ve sonuçların sınırları anlaşılır biçimde kaydedildiğinde bölüm tamamlanabilir. Bir örneğin bulunmaması açık nokta olarak gösterilir.

### Geri dönüş koşulu

Yeni bir işlem veya sonuç kaydı yöntem açıklamasını değiştirirse; yer, zaman ya da gaye yöntemin uygulanabilirliğini etkilerse bu bölüme dön.

## 4 Zaman Protokolü

**Ana sorular:** Hangi andadır? Bu anı, diğer zamanlardan farklı yapan nelerdir? Neler değildir?

Zaman Protokolü, incelenen şeyin hangi anda ve hangi süreç evresinde bulunduğunu araştırır. Tarih ve saat, zamansal konumu belirler. Buna ek olarak o ana kadar oluşmuş koşullar, geçmişten gelen birikim ve o anda açık olan olasılıklar ele alınır. Başlangıçta, gelişme evresinde veya bir eşikte bulunmak, mevcut durumun anlamını ve yapılabilecek işleri etkileyebilir.

Bir anın başka bir andan takvim bakımından farklı olması ile anlamlı bir fark yaratması ayrı değerlendirilir. “Bu anı farklı yapan” unsurun, olanakları, yapılan işin anlamını, öncelikleri veya kararları nasıl değiştirdiği araştırılır. Bir zaman işaretinin kaydı ile bu işaretin incelenen bağlamda taşıdığı anlam birlikte açıklanır.

Hangi koşulların oluştuğu, nelerin tamamlandığı, nelerin henüz mümkün olmadığı ve hangi değişimlerin açık olduğu incelenir. Bu soruların cevapları, Varlık, Mekan ve Usül protokollerindeki tanımların o an için geçerliliğini etkileyebilir. Bir evrede mümkün olan işin başka bir evrede de mümkün olduğu, gerekçesi gösterilmeden varsayılmaz.

Zaman, kimliğin sürmesi ve değişmesi sorusunu da açar. Bir taşıyıcının öğrenmesi, hata yapması veya yöntemini değiştirmesi, hangi özellikler değişirken aynı şey olarak tanındığını araştırmayı gerektirir. Her değişim, taşıyıcının kendiliğinden başka bir varlık olduğu şeklinde yorumlanmaz; süreklilik iddiası da ayrıca gerekçelendirilir.

Soran özne, belirli bir birikimle ve belirli bir anda sorgular. “Hangi birikimle, hangi evrede ve hangi koşullar altında anlamaya çalışıyorum?” sorusu, değerlendirmeyi yapan tarafın zamanını da kayda geçirir. Bir açıklamanın daha sonra gözden geçirilmesi gerekebilir. Cevabı değiştirmeyi gerektirecek koşulların belirtilmesi, Usül Protokolündeki sınamayla ilişkilidir.

“Neler değildir?” sorusu, başka bir evreye ait koşulların mevcut ana taşınmasını ve henüz gerçekleşmemiş bir durumun gerçekleşmiş sayılmasını ayırt etmeye yardım eder. Bilginin bulunmadığı bir dönem, incelenen koşulun bulunmadığı dönem olarak kabul edilmez. Zamana ilişkin sonuçlar, ait oldukları evre ve dayanaklarla birlikte korunur.

~~~text
  ZAMANSAL KONUM  tarih ve saat; buna ek olarak

     o ana kadar olusmus kosullar             o anda acik olan
     gecmisten gelen birikim                  olasiliklar
                                                      .- - - - - >
    ======================================>  AN  - - -+- - - - - >
                                                      `- - - - - >

  SUREC EVRESI   baslangic  |  gelisme evresi  |  bir esik
    hangi kosullar olustu?  .  neler tamamlandi?  .
    neler henuz mumkun degil?  .  hangi degisimler acik?
    bir evrede mumkun olan isin baska bir evrede de mumkun oldugu,
    gerekcesi gosterilmeden varsayilmaz

  TAKVIM BAKIMINDAN FARK ile ANLAMLI FARK ayri degerlendirilir
    "bu ani farkli yapan" unsur sunlari nasil degistiriyor?
        olanaklar . yapilan isin anlami . oncelikler . kararlar

  SUREKLILIK VE DEGISIM   ogrenme . hata . yontem degisikligi
    her degisim, tasiyicinin kendiliginden baska bir varlik oldugu
    seklinde yorumlanmaz; sureklilik iddiasi da ayrica
    gerekcelendirilir

  KABUL EDILMEZ
    bilginin bulunmadigi donem  =  incelenen kosulun bulunmadigi donem

  SORAN OZNENIN ZAMANI
    "Hangi birikimle, hangi evrede ve hangi kosullar altinda
     anlamaya calisiyorum?"
~~~

*Çizim 11 — Zaman: birikim, an ve açık olasılıklar; evre; anlamlı fark; süreklilik ve değişim.*

### Başlangıç girdileri

Tohum kaydındaki inceleme dönemi; konuya ilişkin tarih, olay sırası veya süreç evresi bilgileri; diğer protokollerdeki zamana bağlı ifadeler.

### Masaüstünde uygulama

1. **Üç zaman bilgisini ayır.** Kaydın oluşturulduğu tarihi, incelenen şeyin veya olayın zamanını ve kullanılan kaynağın tarihini ayrı belirt. Saat önemliyse saat dilimini yaz. Biri bilinmiyorsa diğerini onun yerine kullanma.

2. **Süreç evresini belirle.** Konunun hangi evrede bulunduğunu ve bu değerlendirmeyi destekleyen koşulları yaz. Nelerin oluştuğunu, tamamlandığını, henüz mümkün olmadığını ve hangi olasılıkların açık olduğunu belirt.

3. **Anlamlı zaman farkını araştır.** Karşılaştırılan an veya evreleri belirt. Farkın olanakları, yapılan işin anlamını, öncelikleri ya da kararları nasıl değiştirdiğini açıkla. Salt tarih farklılığını açıklayıcı koşul sayma.

4. **Süreklilik ve değişimi değerlendir.** Öğrenme, hata, yöntem veya koşul değişikliklerinin kimlik ve işleyiş hakkındaki cevapları nasıl etkilediğini yaz. Her değişimi kimliğin sona ermesi olarak yorumlama; süreklilik iddiasını da dayanaklandır.

5. **Geçerlilik zamanını kaydet.** Cevapların hangi ana, döneme veya evreye ait olduğunu belirt. Soran tarafın kullandığı birikimi ve mevcut bilgi sınırlarını kaydet. Hangi zaman veya koşul değişikliğinin yeniden inceleme gerektireceğini yaz.

### Tutulacak kayıt

Kayıt, olay ve kaynak zamanları; süreç evresi; oluşmuş koşullar ve açık olasılıklar; karşılaştırılan zamanlar; süreklilik ve değişim; açıklamanın geçerli olduğu dönem.

### Tamamlanma ölçütü

Zaman bilgileri birbirinden ayrılmış, süreç evresi veya buna ilişkin bilinmezlik dayanaklarıyla açıklanmış ve zamana bağlı belirsizlikler belirtilmişse bölüm kaydedilmiş sayılır.

### Geri dönüş koşulu

Yeni bir tarih veya olay sırası bilgisi bulunursa, süreç evresi değişirse ya da açıklama farklı bir döneme uygulanacaksa bu bölüme dön.

## 5 Gaye Protokolü

**Ana sorular:** Hangi nihai amaca hizmet eder? Bu nihai amaca ulaştıran nelerdir? Neler değildir?

Gaye Protokolü, yapılan işlerin hangi sonuca yöneldiğini, bu sonucun neden istendiğini ve kimin açısından anlam taşıdığını araştırır. İlk dört soru kümesinin ikinci soruları ağırlıklı olarak kuruculuk ve özgüllük üzerinde dururken, burada amaca ulaşmanın koşulları ele alınır. Böylece çerçeve, anlamanın yanında belirli bir gayeye katkıyı değerlendirmeye de açılır.

Amaç, görülen işlev ve gerçekleşen sonuç birbirinden ayrılır. Bir şeyin belirli bir amaç için kurulmuş veya kullanılmış olması, o amaca fiilen ulaştırdığını göstermez. İçinde bulunduğu düzende gördüğü işlev ile meydana getirdiği sonuç da farklı olabilir. Amaca hizmet edildiği yönündeki ifade, yapılan iş ve ortaya çıkan etkiyle birlikte gerekçelendirilir.

“Kimin gayesi?” sorusu korunur. Bir gayeyi taşımak, uygulamak, belirlemek, benimsemek ve gerekçelendirmek farklı ilişkilerdir. Farklı taraflar aynı yapıya farklı amaçlar yükleyebilir. Bu nedenle soruyu kuran, bilgiyi işleyen veya eylemi gerçekleştiren taraf, gayenin zorunlu sahibi ya da tek belirleyicisi kabul edilmez.

“Nihai” ifadesi, incelemenin kapsamı ve zaman ufku içinde açıklanır. Bir araştırmada son amaç sayılan şey, daha geniş bir araştırmada başka bir amacın aracı olabilir. Çerçeve farklı türden varlıklara ve süreçlere uygulanırken, “Bir amacı var mı; varsa bu amaç neye dayanarak belirleniyor?” sorusuna yer açılır. Her şey için tek, değişmez ve önceden verilmiş bir amaç bulunduğu varsayılmaz.

~~~text
  BIRBIRINDEN AYRILIR

        AMAC        |      GORULEN ISLEV      |    GERCEKLESEN SONUC

    belirli bir amac icin kurulmus ya da kullanilmis olmak, o amaca
    fiilen ulastirdigini gostermez; icinde bulundugu duzende gordugu
    islev ile meydana getirdigi sonuc da farkli olabilir

  "KIMIN GAYESI?"  bir gayeyi
    tasimak | uygulamak | belirlemek | benimsemek | gerekcelendirmek
    farkli iliskilerdir; farkli taraflar ayni yapiya farkli amaclar
    yukleyebilir
    soruyu kuran, bilgiyi isleyen ya da eylemi gerceklestiren taraf,
    gayenin zorunlu sahibi ya da tek belirleyicisi kabul edilmez

  "NIHAI"  incelemenin kapsami ve zaman ufku icinde aciklanir

    bir arastirmada      . . . --->  [ X ]
                                     son amac

    daha genis bir       . . . --->  [ X ]  --->  [ baska bir amac ]
    arastirmada                      arac

    "Bir amaci var mi; varsa bu amac neye dayanarak belirleniyor?"
    sorusuna yer acilir; her sey icin tek, degismez ve onceden
    verilmis bir amac bulundugu varsayilmaz
~~~

*Çizim 12 — Gaye: amaç, işlev ve sonuç; "Kimin gayesi?" sorusu; "nihai"nin kapsamı.*

“Bu nihai amaca ulaştıran nelerdir?” sorusu, katkısı gösterilebilen koşulları, işleri ve ilişkileri araştırır. Bir unsurun amaçla birlikte bulunması, onu amaca ulaştıran unsur ilan etmeye tek başına yetmez. Yapılan işin hangi koşullarda ne ölçüde katkı sağladığı, Usül ve Zaman protokollerindeki değerlendirmelerle birlikte açıklanır.

“Neler değildir?” sorusunda, amaca katkısı bulunmayanlar, katkısı henüz gösterilemeyenler ve amaca ulaşmayı zorlaştıranlar ayrı tutulur. Belirsiz katkı, katkısızlık hükmüne; katkısızlık da zarar verme hükmüne dönüştürülmez. Amaçla ilgili bir beklentinin karşılanmaması, hangi koşullar altında değerlendirildiği belirtilerek kaydedilir.

Soran özne de kendi yönelişini araştırır: “Neyi anlamak, gerçekleştirmek veya değiştirmek için soruyorum; bu gayeyi kim belirliyor?” Bu soru, hangi farkların önemli sayıldığını ve hangi işlerin incelemeye alındığını görünür kılar. Gaye, diğer protokollerin cevaplarını yönlendirebilir; ortaya çıkan sonuçlar da bu gayeye hizmet edildiği yönündeki değerlendirmenin yeniden ele alınmasını gerektirebilir.

~~~text
  "BU NIHAI AMACA ULASTIRAN NELERDIR?"
    katkisi gosterilebilen kosullari, isleri ve iliskileri arastirir
    bir unsurun amacla birlikte bulunmasi, onu amaca ulastiran unsur
    ilan etmeye tek basina yetmez

  "NELER DEGILDIR?"  ayri tutulur

    amaca katkisi          katkisi henuz            amaca ulasmayi
    bulunmayanlar          gosterilemeyenler        zorlastiranlar

    belirsiz katki   --x-->   katkisizlik   --x-->   zarar verme
    --x-->  hukmune donusturulmez

  SORAN OZNE KENDI YONELISINI ARASTIRIR
    "Neyi anlamak, gerceklestirmek ya da degistirmek icin soruyorum;
     bu gayeyi kim belirliyor?"

  GAYE VE DIGER PROTOKOLLER

    gaye              --- yonlendirebilir --->   diger protokollerin
                                                 cevaplari

    ortaya cikan      --- yeniden ele almayi     bu gayeye hizmet
    sonuclar              gerektirebilir --->    edildigi yonundeki
                                                 degerlendirme
~~~

*Çizim 13 — Gaye: ulaştıranlar; ayrı tutulan üç durum; soranın yönelişi; gaye ve diğer protokoller.*

### Başlangıç girdileri

Tohum kaydındaki ilk gaye ve beklenti sahibi; Varlık, Mekan, Usül ve Zaman kayıtları; amaç ifadeleri ve gerçekleşen sonuçlara ilişkin dayanaklar.

### Masaüstünde uygulama

1. **Gayeyi ve sahibini belirginleştir.** İleri sürülen amacı, bu amacın kime ait olduğunu ve neye dayanarak belirlendiğini yaz. Bir amaç bulunup bulunmadığı belirsizse bunu belirt. Kaynakta ifade edilen amaçla senin yorumladığın amacı ayır.

2. **Amaçla ilişkili rolleri ayır.** Gayeyi belirleyen, benimseyen, gerekçelendiren ve uygulayan tarafları açıkla. Farklı tarafların farklı gayeleri varsa bunları tek amaçmış gibi birleştirme.

3. **Amaç, işlev ve sonucu karşılaştır.** Amaçlanan kullanımı, mevcut düzende görülen işlevi ve fiilen ortaya çıkan sonucu ayrı kaydet. Bir amaç için kurulmuş olmayı, o amaca ulaşıldığının kanıtı olarak kullanma.

4. **Nihailiğin kapsamını açıkla.** Bu amaç için “nihai” deniyorsa hangi inceleme kapsamı ve zaman ufku içinde söylendiğini yaz. Daha geniş bir amaçla araç ilişkisi kuruluyorsa o ilişkiyi ve dayanağını belirt.

5. **Katkıyı ve açık noktaları değerlendir.** Amaca katkısı gösterilenleri, katkısı bulunmadığı gösterilenleri, katkısı henüz bilinmeyenleri ve amaca ulaşmayı zorlaştıranları ayır. Soran tarafın kendi yönelişini de kaydet; sonuçların amaca hizmet edildiği iddiasını hangi ölçüde desteklediğini yaz.

### Tutulacak kayıt

Gaye ifadesi ve dayanağı; amaç sahibi ve ilgili roller; amaç, işlev ve sonuç ayrımı; nihailiğin kapsamı; katkı değerlendirmesi; belirsizlikler; soran tarafın yönelişi.

### Tamamlanma ölçütü

Gayenin bilinen veya belirsiz durumu, kime atfedildiği, hangi kapsamda ele alındığı ve sonuçlarla ilişkisi dayanaklarıyla kaydedilmişse bölüm tamamlanabilir.

### Geri dönüş koşulu

Gaye, amaç sahibi, gerçekleşen sonuç veya katkı dayanağı hakkında yeni bilgi ortaya çıkarsa bu bölüme dön. İncelemenin temel yönelişi değişiyorsa 0 Tohum kaydını da gerekçesiyle güncelle.

## 6 Kökleşme (Bitiş) Protokolü

**Ana sorular:** Bu inceleme sonunda neyi, hangi gerekçelerle ve hangi sınırlar içinde anlıyoruz? Başlangıçtaki anlayışımızdan ne değişti?

Kökleşme Protokolü, beş protokol boyunca oluşan anlayışı bir araya getirir; sonuçları dayanakları, ilişkileri ve geçerlilik sınırlarıyla birlikte kaydeder. Ayrı ayrı verilen cevapların birlikte neyi anlamayı sağladığını ve başlangıçtaki anlayıştan neyin değiştiğini açığa çıkarır.

Varlık hakkında söylenenler yer ve zamanla, yapılan işler usul ve sonuçlarla, gaye ise katkısı gösterilebilen koşullarla birlikte değerlendirilir. Bir bölümdeki cevap başka bir bölümdeki kabulü değiştiriyorsa bu ilişki açıklanır. Giderilememiş gerilimler ve açık noktalar, sonuç üzerindeki etkileriyle birlikte görünür tutulur.

Kökleşme, bir sonucun dayanaklarıyla birlikte yerleşmesidir. Neyi hangi gerekçeyle söyleyebildiğimiz, hangi tanımları düzelttiğimiz, hangi ayrımları koruduğumuz ve hangi soruların sürdüğü belirginleşir. Başlangıç kaydıyla karşılaştırma, inceleme sırasında oluşan değişimi göstermeye yarar.

Bitiş, belirli bir keşif çevriminin kendi kapsamı içinde tamamlanmasıdır. Elde edilen anlayışın hangi koşullarda yeniden değerlendirileceği de bu tamamlanmanın parçasıdır. Soran taraf kendi bakışı, usulü veya gayesi hakkında daha açık gördüğü bir nokta varsa bunu kaydedebilir. Açık kalan veya yeni biçimiyle ortaya çıkan bir soru, sonraki çevrimin tohumu olabilir.

### Başlangıç girdileri

0 Tohum kaydı; 1–5 bölüm kayıtları; sonuçların dayanakları; değişim kaydı; açık sorular ve uyuşmayan açıklamalar. Bir bölümün henüz incelenmemiş olması da girdilerin durumu olarak belirtilir.

### Masaüstünde uygulama

1. **Bölüm kayıtlarını birlikte oku.** 0–5 kayıtlarını aç. Her bölümde cevaplanan soruları, dayanakları, açık noktaları ve bölüm durumunu incele. İncelenmemiş bir alanı yapılmış değerlendirme gibi sunma; eksikliğin hangi sonuçları sınırladığını belirt.

2. **Cevaplar arasındaki ilişkileri açıkla.** Varlık tanımını yer ve zamanla; yapılan işleri usul ve sonuçlarla; gayeyi katkısı gösterilen koşullarla ilişkilendir. Bir cevabın başka bir kabulü değiştirdiği noktaları yaz. Uyuşmayan açıklamalar için farklı kapsam, zaman veya varsayım kullanılıp kullanılmadığını incele.

3. **Sonuçları dayanaklarıyla bütünleştir.** Başlıca sonuçları bağlantılı paragraflarla yaz. Her önemli sonucun dayanağını, geçerli olduğu kapsamı ve zamanı belirt. Bilinmeyen, kapsam dışında kalan ve gerekçeyle dışlanan durumları koru. Sonucu belirleyen bir belirsizlik varsa sonucu eldeki dayanakların taşıdığı kapsamla sınırla.

4. **Başlangıçla karşılaştır.** Tohum kaydındaki ilk tasvir, soru, varsayım ve beklentilerle son durumu karşılaştır. Değişen kabulü, değişim gerekçesini ve hangi bölümün bu değişimi doğurduğunu yaz. Soran tarafın kendi konumu, usulü veya gayesi hakkında edindiği açıklığı da ilgiliyse kaydet.

5. **Açık noktaları ve dönüşleri belirle.** Her açık sorunun sonucu nasıl etkilediğini ve hangi protokole dönülerek ele alınabileceğini belirt. Yeni bir konu oluşturan soruları sonraki Tohum kaydı için ayır. Yeniden incelemeyi gerektirecek gözlem, çelişki veya koşul değişikliklerini somut biçimde yaz.

6. **Çevrim durumunu kaydet.** Sonuç paragraflarını, sınırları, açık noktaları ve bitiş tarihini çalışma kaydına işle. Seçilen kapsamın planlanan değerlendirmesi bitmişse “Tamamlandı”; sonuç kayıtlı belirsizliklerle sınırlanarak kapatılıyorsa “Açık noktalarla tamamlandı”; bu çevrimde ek inceleme hâlen gerekiyorsa “Sürdürülecek” durumunu seç. Seçimin gerekçesini yaz. Sonucu etkileyen çözülmemiş bir çelişkiyi açık nokta olarak işaretlemeden çevrimi tamamlanmış sayma.

### Tutulacak kayıt

Bütünleşmiş anlayış, önemli sonuçların dayanakları ve sınırları, başlangıca göre değişiklikler, soran tarafın değerlendirmesi, açık sorular, geri dönülecek protokoller, yeniden inceleme koşulları ve çevrimin son durumu kaydedilir.

### Tamamlanma ölçütü

Ulaşılan sonuçlar ve sınırları anlaşılır hâle gelmiş, başlangıçla son durum karşılaştırılmış, açık noktalar ve yeniden inceleme koşulları belirtilmişse çevrimin kaydı tamamlanabilir. Bu ölçüt, konunun bütün yönleriyle bilindiğini veya idrakin yalnızca adımların tamamlanmasıyla kanıtlandığını ileri sürmez.

### Geri dönüş koşulu

Yeni bir bulgu, çelişki veya koşul değişikliği sonucu etkilerse ilgili 1–5 protokolüne dön. Temel soru veya kapsam değişmişse 0 Tohum kaydını gerekçesiyle güncelle ya da yeni bir çevrim başlat. Önceki sonuç kaydını tarih ve değişim gerekçesiyle koru.

~~~text
  KOKLESME  bir sonucun dayanaklariyla birlikte yerlesmesidir

  BIRLIKTE DEGERLENDIRILIR
    varlik hakkinda soylenenler   <-->   yer ve zaman
    yapilan isler                 <-->   usul ve sonuclar
    gaye                          <-->   katkisi gosterilebilen kosullar

  BASLANGICLA KARSILASTIRMA
    0 Tohum kaydi                        son durum
    ilk tasvir . soru .       <----->    degisen kabul . degisim
    varsayim . beklenti                  gerekcesi . hangi bolumun bu
                                         degisimi dogurdugu

  CEVRIM VE GERI DONUS

     0 Tohum  ---->  1-5  ---->  6 Koklesme  ---->  cevrim durumu
        ^             ^               |
        |             `---------------+   yeni bir bulgu, celiski ya da
        |                             |   kosul degisikligi sonucu
        |                             |   etkilerse
        `-----------------------------'   temel soru ya da kapsam
                                          degismisse (ya da yeni bir
                                          cevrim baslatilir)

    Tamamlandi                   secilen kapsamin planlanan
                                 degerlendirmesi bitmisse
    Acik noktalarla tamamlandi   sonuc kayitli belirsizliklerle
                                 sinirlanarak kapatiliyorsa
    Surdurulecek                 bu cevrimde ek inceleme halen
                                 gerekiyorsa

    acik kalan ya da yeni bicimiyle ortaya cikan bir soru, sonraki
    cevrimin tohumu olabilir
~~~

*Çizim 14 — Kökleşme: birlikte değerlendirme; başlangıçla karşılaştırma; çevrim, geri dönüş ve son durum.*

## Ek A Uygulama kaydı şablonu

Aşağıdaki metni yeni bir `.md` dosyasına kopyalayarak konuya ait çalışma kaydını oluştur. Şablondaki örnek alanlar gerçek bir incelemenin sonucu değildir.

```markdown
# Bağlamsal Keşif ve İdrak Uygulama Kaydı

**Konu:** [Doldur]

**Kaydı tutan taraf:** [Doldur]

**Başlangıç tarihi ve saat dilimi:** [Doldur]

**Son güncelleme:** [Doldur]

**Çevrim durumu:** [Çalışılıyor / Tamamlandı / Açık noktalarla tamamlandı / Sürdürülecek]

Köşeli parantezli alanları konuya ilişkin paragraflarla doldur. Gerekçeyle dışlanan, bilinmeyen ve kapsam dışı olanı ayır. Bir cevap başka bölümü etkiliyorsa ilgili bölüm numarasını yaz.

## Kaynak kaydı

| Kaynak kodu | Dosya adı veya adres | İlgili bölüm veya kayıt yeri | Kaynak tarihi veya sürümü |
|---|---|---|---|
| [K01] | [Doldur] | [Doldur] | [Doldur veya bilinmiyor] |

Kaynak kodunu ilgili cevabın dayanak paragrafında kullan. İhtiyaç oldukça satır ekle.

## 0 Tohum (Başlangıç) Protokolü

**Bölüm durumu:** [Başlanmadı / Çalışılıyor / Kaydedildi / Geri dönüş gerekli]

**Başlangıç sorusu ve doğduğu ihtiyaç:** [Neyi anlamaya yöneliyoruz ve neden şimdi soruyoruz?]

**İlk tasvir ve kavramlar:** [Konuyu başlangıçta nasıl tanımlıyoruz?]

**Bilinenler ve dayanaklar:** [Hangi gözlem veya kayda dayanıyoruz?]

**Varsayımlar ve açık noktalar:** [Henüz sınanmayan veya bilinmeyen nedir?]

**Kapsam:** [Hangi yer, dönem, ilişki ve kaynaklar dâhil; neler hangi gerekçeyle dışında?]

**İlk gaye ve soran taraf:** [Beklenti kime ait; kim, hangi konumdan soruyor?]

**Dayanaklar, açık noktalar ve diğer bölümlere etkiler:** [Kaynak kodlarını ve gerekçeleri yaz.]

## 1 Varlık Protokolü

**Bölüm durumu:** [Başlanmadı / Çalışılıyor / Kaydedildi / Geri dönüş gerekli]

**Gerekçeli tanım:** [İncelenen şey nedir?]

**Kurucu ve ayırt edici özellikler:** [Hangi özellik neye kıyasla ve neden önemlidir?]

**Süreklilik ve değişim:** [Hangi değişikliklerde aynı şey olarak tanınır?]

**Sınırlar:** [Gerekçeyle dışlanan, bilinmeyen ve kapsam dışı olan nedir?]

**Taşıyıcı ve soran taraf:** [Kim soruyor; bakış, söz ve eylem kime ait?]

**Dayanaklar, açık noktalar ve diğer bölümlere etkiler:** [Kaynak kodlarını ve gerekçeleri yaz.]

## 2 Mekan Protokolü

**Bölüm durumu:** [Başlanmadı / Çalışılıyor / Kaydedildi / Geri dönüş gerekli]

**Ölçek ve konum:** [Fiziksel, kurumsal veya ilişkisel hangi yer inceleniyor?]

**Bağlı olunan bütün ve ilişkiler:** [Neye yakın, uzak veya bağlı?]

**Erişimler ve sınırlar:** [Hangi olanaklara erişilebiliyor?]

**Özgüllük ve karşılaştırma:** [Yer hangi bakımdan farklı ve bu fark neyi değiştiriyor?]

**Soran tarafın konumu:** [Nereden bakılıyor; hangi ilişkiler erişim dışında?]

**Dayanaklar, açık noktalar ve diğer bölümlere etkiler:** [Kaynak kodlarını ve gerekçeleri yaz.]

## 3 Usül Protokolü

**Bölüm durumu:** [Başlanmadı / Çalışılıyor / Kaydedildi / Geri dönüş gerekli]

**İş türü ve yöntem:** [Ne tür işler hangi yollarla yapılıyor?]

**Örnek akış:** [Girdi, adımlar, çıktı ve sonuç nedir?]

**Kapasite, fiil ve sonuç:** [Yapılabilecek, yapılan ve gerçekleşen nasıl ayrılıyor?]

**Roller:** [Soruyu kim kuruyor, bilgiyi kim işliyor, gayeyi kim belirliyor, işi kim gerçekleştiriyor?]

**Sınama ve yöntem sınırı:** [Çıkarımın dayanağı ve onu değiştirecek koşul nedir?]

**Dayanaklar, açık noktalar ve diğer bölümlere etkiler:** [Kaynak kodlarını ve gerekçeleri yaz.]

## 4 Zaman Protokolü

**Bölüm durumu:** [Başlanmadı / Çalışılıyor / Kaydedildi / Geri dönüş gerekli]

**Zaman bilgileri:** [Kayıt zamanı, olay zamanı ve kaynak tarihi nedir?]

**Süreç evresi:** [Hangi evrede ve hangi koşullarda?]

**Anlamlı zaman farkı:** [Karşılaştırılan anlar veya evreler neyi değiştiriyor?]

**Süreklilik ve değişim:** [Hangi cevaplar zamanla değişiyor veya sürüyor?]

**Geçerlilik ve yeniden inceleme:** [Cevap hangi dönemde geçerli; ne zaman yeniden ele alınmalı?]

**Dayanaklar, açık noktalar ve diğer bölümlere etkiler:** [Kaynak kodlarını ve gerekçeleri yaz.]

## 5 Gaye Protokolü

**Bölüm durumu:** [Başlanmadı / Çalışılıyor / Kaydedildi / Geri dönüş gerekli]

**Gaye ve dayanağı:** [Hangi amaç ileri sürülüyor; nereden biliniyor?]

**Gaye sahibi ve roller:** [Kim belirliyor, benimsiyor, gerekçelendiriyor ve uyguluyor?]

**Amaç, işlev ve sonuç:** [Amaçlanan, görülen işlev ve gerçekleşen nasıl ayrılıyor?]

**Nihailiğin kapsamı:** [Hangi kapsam ve zaman ufkunda nihai?]

**Katkı değerlendirmesi:** [Katkısı gösterilen, katkısızlığı gösterilen, katkısı bilinmeyen ve zorlaştıran neler?]

**Soran tarafın gayesi:** [Bu incelemeyi hangi yönelişle yapıyoruz?]

**Dayanaklar, açık noktalar ve diğer bölümlere etkiler:** [Kaynak kodlarını ve gerekçeleri yaz.]

## 6 Kökleşme (Bitiş) Protokolü

**Bölüm durumu:** [Başlanmadı / Çalışılıyor / Kaydedildi / Geri dönüş gerekli]

**Bütünleşmiş anlayış:** [0–5 kayıtları birlikte neyi anlamamızı sağlıyor?]

**Önemli sonuçlar ve dayanakları:** [Her sonucun kaynağı, kapsamı ve zaman sınırı nedir?]

**Bölümler arası ilişkiler ve gerilimler:** [Hangi cevap diğerini değiştiriyor; hangi uyuşmazlıklar sürüyor?]

**Başlangıca göre değişim:** [İlk tanım, varsayım, soru ve beklentilerden ne değişti?]

**Soran tarafın değerlendirmesi:** [Kendi konumu, usulü veya gayesi hakkında ne daha açık hâle geldi?]

**Açık sorular ve geri dönüşler:** [Hangi soru hangi bölüme dönülerek ele alınacak?]

**Yeniden inceleme koşulları:** [Hangi yeni gözlem, çelişki veya koşul değişikliği sonucu etkiler?]

**Dayanaklar, açık noktalar ve diğer bölümlere etkiler:** [Kaynak kodlarını ve gerekçeleri yaz.]

## Kapanış kaydı

**Bitiş tarihi ve saat dilimi:** [Doldur]

**Son durum ve gerekçesi:** [Tamamlandı / Açık noktalarla tamamlandı / Sürdürülecek; nedenini yaz.]

**Sonraki çevrime ayrılan soru:** [Varsa yaz.]

## Değişim kaydı

| Tarih | Bölüm | Önceki ifade | Yeni ifade | Dayanak ve değişiklik gerekçesi |
|---|---|---|---|---|
| [Doldur] | [0–6] | [Doldur] | [Doldur] | [Doldur] |
```

## Ek B Kaynak soru ve yanıtlar

### Soru ve yanıt kaydı

Soru kayıtları kullanıcının, yanıt kayıtları asistanın ifadelerini içerir. İlk iki soru ve bunlara verilen yanıtlar konuşmadaki sıralarıyla korunmuştur. Başlık düzeyleri ve satır sonları dosyanın okunmasını kolaylaştıracak biçimde düzenlenmiştir.

#### Soru 1

**Kullanıcı**

Geçmiş bağlamları buraya taşıma.

**Bağlamsal Keşif ve İdrak**

Nedir? Onu o yapan nelerdir? Neler değildir?\
Nerededir? Bu yeri, oraya has bir yer yapan nelerdir? Neler değildir?\
Nasıl işler yapar? Bu yaptıklarını, ona has yapan nelerdir? Neler değildir?\
Hangi andadır? Bu anı, diğer zamanlardan farklı yapan nelerdir? Neler değildir?\
Hangi nihai amaca hizmet eder? Bu nihai amaca ulaştıran nelerdir? Neler değildir?

#### Yanıt 1

**Asistan**

**Bağlamsal keşif ve idrak**, burada kurduğun çerçeveyle, **bir şeyi; onu oluşturan özellikler, bulunduğu yer, yaptığı işler, içinde bulunduğu an ve hizmet ettiği amaç arasındaki ilişkiler üzerinden anlama çabası** olarak okunabilir.

Soruların ortak arayışı şu: **Neyle karşı karşıyayız; onu böyle anlamamızı sağlayan nedir; bu anlayışın sınırları nerede başlar?**

Bu yapıda “bağlam”, incelenen şeyin çevresine eklenen bilgilerden daha geniş bir anlam taşıyor. Yer, zaman, ilişkiler ve amaç, o şeyin nasıl anlaşılacağını belirleyen unsurlar hâline geliyor.

##### 1. Beş sorunun açtığı beş boyut

| Boyut | Temel soru | Açığa çıkarmaya çalıştığı şey |
|---|---|---|
| **Kimlik** | Nedir? | Onu belirli bir şey olarak tanımamızı sağlayan özellikler, ilişkiler ve süreklilikler. |
| **Yer** | Nerededir? | İçinde bulunduğu çevre, bağlı olduğu bütün ve bu konumun sağladığı olanaklarla getirdiği sınırlar. |
| **İş ve işleyiş** | Nasıl işler yapar? | Ne tür işler yaptığı, bunları hangi yollarla gerçekleştirdiği ve nasıl etkiler meydana getirdiği. |
| **An** | Hangi andadır? | İçinde bulunduğu sürecin evresi, o ana kadar oluşmuş koşullar ve o anda açık olan olasılıklar. |
| **Amaç** | Hangi nihai amaca hizmet eder? | Yaptıklarının hangi sonuca yöneldiği, bu sonucun neden istendiği ve kimin açısından anlam taşıdığı. |

Bu boyutların her biri, diğer soruların cevabını değiştirebilir. Bulunduğu yer bir şeyin hangi işleri yapabileceğini; içinde bulunduğu an bu işlerin anlamını ve önceliğini; hizmet ettiği amaç ise hangi özelliklerinin önemli sayılacağını etkileyebilir.

Dolayısıyla idrak, bu beş soruya verilen cevapların **birbirleriyle ilişkisini de kavramayı** gerektirir.

##### 2. Soruların içinde tekrarlanan hareket

İlk dört soru kümesinde üç hareket belirginleşiyor:

1. **Belirleme:** Nedir, nerededir, ne yapar, hangi andadır?
2. **Kurucu ve ayırt edici unsurları bulma:** Onu böyle yapan, bu yeri veya anı anlamlı biçimde farklılaştıran nedir?
3. **Sınır çizme:** Hangi tanımlar, benzerlikler, özellikler veya beklentiler burada geçerli değildir?

Bu tekrarın değeri, bir ilk tanımı hemen tamamlanmış kabul etmeyişinde. “Budur” dedikten sonra, **“Hangi gerekçeyle budur?”** ve **“Bu tanım nereye kadar geçerlidir?”** soruları geliyor.

Ancak “onu o yapan” ile “ona has olan” ifadelerinde korunması gereken bir ayrım var.

###### Kurucu olmak ve ayırt edici olmak

**Kurucu özellik**, bir şeyi o şey olarak anlamamızda temel rol oynar. **Ayırt edici özellik**, onu karşılaştırdığımız başka örneklerden ayırır.

Bir özellik kurucu olduğu hâlde pek çok örnekte ortak olabilir. Bir özellik yalnızca tek bir örnekte bulunabilir ama o örneğin kimliğini veya işleyişini açıklamak bakımından önemsiz kalabilir.

Örneğin, varsayımsal bir kütüphanenin mor kapısı onu çevredeki kütüphanelerden ayırabilir. Bilgi kaynaklarını düzenleyip erişime sunması ise onu kütüphane olarak anlamamızda daha temel bir rol oynar.

Bu nedenle “onu o yapan” sorusu şu iki sınamayla derinleşebilir:

- **Bu özellik değişse veya ortadan kalksa, onu hâlâ aynı şey olarak tanır mıydık?**
- **Bu özellik, onu neye kıyasla ve hangi bakımdan farklılaştırıyor?**

Ayrıca özgüllük, tek bir benzersiz özellikte bulunmak zorunda değildir. Ortak özelliklerin belirli bir ilişkisi veya birleşimi de bir şeyi kendine özgü kılabilir.

##### 3. “Yer”, “iş” ve “an” sorularının derinliği

Bu üç soru, ilk bakışta kolayca cevaplanabilecekmiş gibi görünür. Her birinin içinde farklı inceleme düzeyleri bulunuyor.

###### “Nerededir?”

Bir adres, konumu belirler. “Bu yeri, oraya has bir yer yapan nelerdir?” sorusu ise konumun anlamını açar.

Burada şunlar araştırılabilir: Neye yakın, neye uzak? Nelere erişebiliyor? Hangi ilişkilerin içinde bulunuyor? Hangi bütünün parçası? Çevresindeki hangi koşullar onun davranışını mümkün kılıyor veya sınırlıyor?

“Yer”in hangi ölçekte ele alındığını belirtmek önemlidir. Bir odadaki yer, bir kurumdaki yer ve bir ilişkiler ağı içindeki yer farklı cevaplar gerektirir.

###### “Nasıl işler yapar?”

Bu ifade üç soruyu birlikte taşıyor:

- **Ne tür işler yapar?**
- **Bu işleri nasıl gerçekleştirir?**
- **İş yapma biçimini kendine özgü kılan nedir?**

Bunları ayrı ayrı görebilmek, yapılan iş ile işin yapılma biçimini karıştırmayı önler. Aynı sonuç farklı yollarla elde edilebilir; benzer bir yöntem farklı koşullarda farklı sonuçlar doğurabilir.

Burada bir ek ayrım da yararlıdır: **Yapabildiği, fiilen yaptığı ve yaptığında ortaya çıkan sonuç** ayrı ayrı incelenebilir. Bir kapasitenin bulunması onun kullanıldığını; bir işin yapılması da beklenen sonucun gerçekleştiğini tek başına göstermez.

###### “Hangi andadır?”

Bu soru, tarih ve saatin yanında **süreç içindeki konumu** araştırmaya elverişli.

Bir başlangıçta mı, gelişme evresinde mi, bir eşikte mi? Hangi koşullar oluşmuş? Neler tamamlanmış, neler henüz mümkün olmamış? O anda hangi kararlar veya değişimler mümkün?

“Bu anı diğer zamanlardan farklı yapan” unsurun değeri, meydana getirdiği farkla anlaşılır. Tarihin değişmesi kolayca tespit edilebilir; **bu değişimin olanakları, anlamı veya yapılması gereken işi nasıl etkilediği** ayrıca araştırılmalıdır.

##### 4. “Neler değildir?” sorusunun işlevi

Bir şeyin olmadığı şeylerin sayısı sınırsızdır. Bu yüzden sorunun en verimli kullanımı, **yakın ve makul karışıklıkları elemek** olur.

Örneğin:

- Onunla karıştırılabilecek hangi şeylerden ayrılır?
- Ona atfedilen hangi özellikler tanımının parçası değildir?
- Hangi işler kapsamına girmez?
- Hangi beklentiler ona uygulanamaz?
- Hangi koşullarda yaptığımız tanım geçerliliğini kaybeder?

Burada üç ayrı hükmü birbirinden ayırmak gerekir:

| Hüküm | Anlamı |
|---|---|
| **Bu değildir.** | Dışlamak için bir gerekçemiz vardır. |
| **Bunu bilmiyoruz.** | Karar vermek için yeterli bilgimiz yoktur. |
| **Bu incelemenin dışında kalıyor.** | Şu anda seçtiğimiz kapsamda ele alınmıyordur. |

Bir özelliği gözlemlememiş olmak, onun bulunmadığını göstermeye yetmeyebilir. Aynı şekilde bir konuyu inceleme dışında bırakmak, onun önemsiz olduğunu göstermez.

Bu ayrım korunduğunda “Neler değildir?” sorusu, anlayışın sınırlarını daha doğru çizmeye yardımcı olur.

##### 5. Son soruda gerçekleşen yön değişikliği

Son satırda yapısal bir değişiklik var:

> Hangi nihai amaca hizmet eder? Bu nihai amaca ulaştıran nelerdir?

İlk dört kümenin ikinci soruları, ağırlıklı olarak **kuruculuğu ve özgüllüğü** araştırıyor. Son kümenin ikinci sorusu ise **amaca ulaşmanın koşullarını** araştırıyor.

Bu geçiş, çerçeveye bir değerlendirme boyutu ekliyor: İncelenen şeyin ne olduğunu anlamanın ardından, yaptıklarının belirli bir amacı gerçekleştirmeye katkısı sorgulanıyor.

~~~text
  BES SORU KUMESI  ilk dort kumede uc hareket belirginlesir

  +---------------------+----------------------------+-----------------+
  | 1 BELIRLEME         | 2 KURUCU VE AYIRT EDICI    | 3 SINIR CIZME   |
  |                     |   UNSURLARI BULMA          |                 |
  +---------------------+----------------------------+-----------------+
  | KIMLIK              | Onu o yapan nelerdir?      | Neler degildir? |
  | Nedir?              |                            |                 |
  +---------------------+----------------------------+-----------------+
  | YER                 | Bu yeri, oraya has bir yer | Neler degildir? |
  | Nerededir?          | yapan nelerdir?            |                 |
  +---------------------+----------------------------+-----------------+
  | IS VE ISLEYIS       | Bu yaptiklarini, ona has   | Neler degildir? |
  | Nasil isler yapar?  | yapan nelerdir?            |                 |
  +---------------------+----------------------------+-----------------+
  | AN                  | Bu ani, diger zamanlardan  | Neler degildir? |
  | Hangi andadir?      | farkli yapan nelerdir?     |                 |
  +=====================+============================+=================+
  | SON KUME            | 2 AMACA ULASMANIN          |                 |
  |                     |   KOSULLARI                |                 |
  +---------------------+----------------------------+-----------------+
  | AMAC                | Bu nihai amaca ulastiran   | Neler degildir? |
  | Hangi nihai amaca   | nelerdir?                  |                 |
  | hizmet eder?        |                            |                 |
  +---------------------+----------------------------+-----------------+

  ilk dort kumenin ikinci sorulari agirlikli olarak kuruculugu ve
  ozgullugu arastirir; son kumenin ikinci sorusu amaca ulasmanin
  kosullarini arastirir: cerceveye bir degerlendirme boyutu eklenir

  "Budur" dedikten sonra gelen sorular
    "Hangi gerekceyle budur?"  .  "Bu tanim nereye kadar gecerlidir?"

  HER BOYUT DIGER SORULARIN CEVABINI DEGISTIREBILIR
    bulundugu yer         -->  hangi isleri yapabilecegini
    icinde bulundugu an   -->  bu islerin anlamini ve onceligini
    hizmet ettigi amac    -->  hangi ozelliklerinin onemli
                               sayilacagini etkileyebilir
~~~

*Çizim 15 — Yanıt 1: beş soru kümesi ve üç hareket; son kümedeki yön değişikliği.*

Burada birkaç ayrım özellikle değerli:

**Amaç, işlev ve sonuç.** Bir şeyin amaçlanan kullanımı, içinde bulunduğu düzende gördüğü işlev ve fiilen meydana getirdiği sonuç farklı olabilir. “Şu amaca hizmet etmek üzere kurulmuş” demekle “şu amaca ulaştırıyor” demek farklı gerekçeler ister.

**Amaç sahibi.** “Kimin açısından?” sorusu, amacı belirginleştirir. Farklı kişiler veya gruplar aynı yapıya farklı amaçlar yükleyebilir.

**Nihailik.** Bir incelemede son amaç sayılan şey, daha geniş bir incelemede başka bir amacın aracı olabilir. Bu yüzden “nihai” ifadesinin hangi kapsam ve zaman ufku içinde kullanıldığı açıklanmalıdır.

**Amaç bulunup bulunmadığı.** Çerçeve her tür varlık, olay veya sürece uygulanacaksa, “Bir amacı var mı; varsa bu amaç neye dayanarak belirleniyor?” sorusuna da yer açmak gerekir. Özellikle niyet atfetmenin gerekçelendirilmediği durumlarda bu açıklık önem kazanır.

Ayrıca son “Neler değildir?” sorusu birkaç ayrı durumu kapsayabilir: Amaca katkısı bulunmayanlar, katkısı henüz gösterilemeyenler ve amaca ulaşmayı zorlaştıranlar. Bunların ayrılması, değerlendirmeyi daha isabetli kılar.

##### 6. Keşiften idrake geçiş

Bu çerçeve için şöyle bir çalışma ayrımı önerebilirim:

**Keşif**, ilgili özellikleri, koşulları, ilişkileri ve sınırları ortaya çıkarma hareketidir.

**İdrak**, ortaya çıkanların birbirini nasıl etkilediğini, hangi koşullarda ne anlama geldiğini ve bunun hangi sonuçları doğurduğunu kavrama hareketidir.

Örneğin varsayımsal bir mahalle kütüphanesini ele alalım. Kitap ödünç verdiğini, mahallenin tek sessiz ortak çalışma alanı olduğunu ve sınav döneminde bulunduğunu öğrenmek keşfin parçalarıdır. Bu bilgileri birlikte değerlendirip o dönemde sessiz çalışma alanının korunmasının neden daha fazla önem kazandığını kavramak, idrake doğru ilerlemektir. Erişilebilir öğrenmeyi desteklemek de bu kütüphane için benimsenmiş amaçsa, yapılacak değişiklikler bu amaç bakımından değerlendirilebilir.

Böylece beş boyut tek bir araştırma sorusunda buluşur:

**Bu şey, bu yerde ve bu anda, sahip olduğu özelliklerle neyi nasıl mümkün kılıyor; bunun anlamı ve yöneldiği sonuç nedir?**

Bütün bu sorulara eşlik edecek ortak bir sınama da şu olabilir:

**“Bunu hangi gözleme, karşılaştırmaya veya gerekçeye dayanarak söylüyoruz; hangi durumda cevabımızı değiştirmemiz gerekir?”**

Bu son soru, kurulan anlayışın gözden geçirilebilir olmasını sağlar. Çerçevedeki “idrak” böylece, bir şeyi tanımakla birlikte, **onu nasıl ve hangi sınırlar içinde anladığının da farkında olmayı** içerir.

~~~text
  IKI VARSAYIMSAL KUTUPHANE

  1  KURUCU OLMAK VE AYIRT EDICI OLMAK

       .---------------------.
       |      KUTUPHANE      |      bilgi kaynaklarini duzenleyip
       |  [|||] [|||] [|||]  |      erisime sunmasi: onu kutuphane
       |       .-----.       |      olarak anlamamizda daha temel
       |       | mor |       |      bir rol oynar
       |       | kapi|       |
       `-------+-----+-------'      mor kapisi: onu cevredeki
                                    kutuphanelerden ayirabilir

  2  KESIFTEN IDRAKE  bir mahalle kutuphanesi

     kesfin parcalari                     idrake dogru ilerlemek
     .---------------------------.
     | kitap odunc verir         |        bu bilgileri birlikte
     | mahallenin tek sessiz     |        degerlendirip o donemde
     | ortak calisma alanidir    |  --->  sessiz calisma alaninin
     | sinav donemindedir        |        korunmasinin neden daha
     `---------------------------'        fazla onem kazandigini
                                          kavramak

     erisilebilir ogrenmeyi desteklemek benimsenmis amacsa, yapilacak
     degisiklikler bu amac bakimindan degerlendirilebilir

  BES BOYUTUN BULUSTUGU TEK ARASTIRMA SORUSU
    bu sey, bu yerde ve bu anda, sahip oldugu ozelliklerle neyi
    nasil mumkun kiliyor; bunun anlami ve yoneldigi sonuc nedir?
~~~

*Çizim 16 — Yanıt 1: iki varsayımsal kütüphane; beş boyutun buluştuğu tek soru.*

#### Soru 2

**Kullanıcı**

**Bağlamsal Keşif ve İdrak**'ın köken aldığı varlık, mekan, usül, zaman, ve gayeyi taşıyan makine kimdir? Kim değildir?

#### Yanıt 2

**Asistan**

Sorudaki **“makine”yi, keşif ve idrakin gerçekleştiği taşıyıcı** anlamında alırsam, ona **özne** derim: **Bir bağlamın içinde bulunan, o bağlamda anlam ve eylem kuran, kendi konumunu da sorgulamaya açabilen varlık.**

İnsan, bu okumadaki en doğrudan örnektir. Fakat varlık, mekân, usul, zaman ve gayeyi sıralamak, taşıyıcının kimliğini tek başına belirlemez. Burada **bu boyutları taşımak**, **onları idrak etmek** ve **onların kökeni olmak** arasında ayrım yapmak gerekiyor.

##### Kimdir?

Senin “kim?” sorun, önceki beş soruda örtük kalan **soranı** görünür kılıyor.

“Nedir?” diye soran da bir şeydir.\
“Nerededir?” diye soran da bir yerdedir.\
“Nasıl işler yapar?” diye soran da bir usulle iş görür.\
“Hangi andadır?” diye soran da bir anın içindedir.\
“Hangi gayeye hizmet eder?” diye soran da belirli bir yönelişle sorar.

Böyle okunduğunda, **soru soran, kendi sorularının kapsamına girer.** Keşfettiği bağlamla kurduğu ilişki de keşfin konusu olur.

Bu taşıyıcının kendisine yönelttiği sorular şöyle açılabilir:

| Taşıdığı boyut | Kendisine dönen soru |
|---|---|
| **Varlık** | Ben nasıl bir varlığım? Bu keşfi yapabilmemi sağlayan olanaklarım ve sınırlarım neler? |
| **Mekân** | Nereden bakıyorum? İçinde bulunduğum ilişkiler bana neleri görünür, neleri erişilmez kılıyor? |
| **Usul** | Neyi nasıl seçiyor, ayırıyor, ilişkilendiriyor ve sınayabiliyorum? Bir çıkarımı neye dayanarak kabul ediyorum? |
| **Zaman** | Hangi birikimle, hangi evrede ve hangi koşullar altında anlamaya çalışıyorum? |
| **Gaye** | Neyi anlamak, gerçekleştirmek veya değiştirmek için soruyorum? Bu gayeyi kim belirliyor? |

Bu anlamda öznenin kimliği, onun yapısıyla birlikte **hangi konumdan, hangi usulle, neye yönelerek iş gördüğünde** belirginleşir.

Burada “kim?” sorusu, “ne?” sorusuna bir boyut ekler: **Bu bakış, bu söz, bu seçim ve bu eylem kime aittir?**

##### Bu boyutları taşımak, onları idrak etmek midir?

Bu ikisini ayırmak gerekir.

Bir saat de vardır; bir yerde bulunur; belirli bir düzenle çalışır; bir zaman içinde işler ve bir amaç için kullanılabilir. Onu beş boyutla betimleyebilmemiz, saatin bu boyutları kavradığını göstermeye yetmez.

Dolayısıyla iki ayrı iddia söz konusu:

- **Bu düzenek, belirli koşullar altında belirli işler yapıyor.**
- **Bu düzenek, yaptığı işleri ve içinde bulunduğu koşulları anlam ilişkileri içinde değerlendiriyor.**

İkinci iddia, birincinin açıklanmasıyla kendiliğinden doğrulanmaz. Hangi davranışın, hangi değerlendirme veya düzeltme yeteneğinin “idrak” sayılacağı ayrıca açıklanmalıdır.

Bu yüzden, sorudaki makineyi **özne** diye adlandırmam, beş boyutun her taşıyıcısını özne ilan etmek anlamına gelmiyor. Bu adlandırma, **keşfeden ve anlayan tarafı** işaret ediyor. Bunun belirli bir varlıkta veya sistemde nasıl gerçekleştiği ise incelemeye açık kalıyor.

##### Taşıyıcı olmak, köken olmak mıdır?

“Köken aldığı” ifadesinde de iki farklı anlam bulunabilir:

**Bu sorgulama nereden doğuyor?**\
Burada soruları kuran, ayrımları yapan, anlamaya yönelen özneyi araştırıyoruz.

**Varlığın, mekânın, usulün, zamanın ve gayenin kendisi nereden doğuyor?**\
Bu ise onların nihai kaynağına ilişkin daha geniş bir soru. İlk soruya verdiğimiz cevap, ikinci soruyu kendiliğinden çözmez.

Bir taşıyıcının zamanı düşünmesi, zamanın ondan doğduğunu göstermez. Bir gayeyi izlemesi, gayeyi kendisinin belirlediğini göstermez. Bir bağlamı açıklaması, o bağlamı bütünüyle kendisinin kurduğu anlamına gelmez.

Üstelik **soruyu kuran, bilgiyi işleyen, gayeyi belirleyen ve eylemi gerçekleştiren aynı taraf olmak zorunda değildir.** Bir düzenekte bu roller farklı taraflara dağılabilir. “Makine kimdir?” sorusunu cevaplamak için hangi rolün kime ait olduğunu da açığa çıkarmak gerekir.

##### Kim değildir?

Bu okumada, özneye şu kimlikleri kendiliğinden yükleyemeyiz:

- **Bağlamın dışından bakan mutlak gözlemci değildir.** İncelediği şeye bir konumdan, belirli erişim olanaklarıyla yaklaşır. Kendi konumunu fark etmesi, onu konumsuz hâle getirmez.

- **Kurduğu açıklamayla dünyanın tamamını tüketen bir otorite değildir.** Açıklamasının kapsamı, dayanakları ve düzeltilebileceği koşullar vardır.

- **Taşıdığı bütün gayelerin zorunlu sahibi değildir.** Bir amacı uygulamak, onu seçmek, benimsemek ve gerekçelendirmek ayrı ilişkilerdir. “Kimin gayesi?” sorusu korunmalıdır.

- **Sırf düzenli ve uygun çıktılar ürettiği için idrak ettiği kanıtlanmış bir sistem değildir.** Çıktıyla idrak arasındaki ilişkinin ayrıca gösterilmesi gerekir.

- **Hata yapmayan veya değişmeden kalan bir varlık olarak tanımlanmış değildir.** Yanlış anlaması, öğrenmesi ya da yöntemini değiştirmesi, kimliğinin nasıl sürdüğü sorusunu açar.

- **“Makine” denildiği için kimliği çözülmüş bir varlık değildir.** Bu sözcük onun işleyişini, yapısını veya bir benzetmeyi anlatıyor olabilir. İnsan mı, yapay bir sistem mi, birlikte çalışan taraflardan oluşan bir düzen mi olduğu ayrıca belirlenmelidir.

**Benim bu çerçevede işaret ettiğim taşıyıcı, kendi sorusunun içine kendisini de katabilen öznedir.** Onun ayırt edici hareketi, “Bu nedir?” sorusuna şu soruyu eşlik ettirebilmesidir:

**“Bunu soran ben kimim; nereden, hangi usulle, hangi anda ve kimin gayesiyle soruyorum?”**

~~~text
  SORU SORAN, KENDI SORULARININ KAPSAMINA GIRER

    "Nedir?" diye soran                   da bir seydir
    "Nerededir?" diye soran               da bir yerdedir
    "Nasil isler yapar?" diye soran       da bir usulle is gorur
    "Hangi andadir?" diye soran           da bir anin icindedir
    "Hangi gayeye hizmet eder?" diye
    soran                                 da belirli bir yonelisle sorar

          .------------- bes soru ------------->.
        SORAN                              INCELENEN SEY
          `<------ kendisine donen sorular -----'

  BIR SAAT                                          .-------.
    vardir                                         /    |    \
    bir yerde bulunur                             |     o---  |
    belirli bir duzenle calisir                    \         /
    bir zaman icinde isler                          `-------'
    bir amac icin kullanilabilir
    onu bes boyutla betimleyebilmemiz, saatin bu boyutlari
    kavradigini gostermeye yetmez

  "KOKEN ALDIGI"  iki farkli anlam
    bu sorgulama nereden doguyor?
    varligin, mekanin, usulun, zamanin ve gayenin kendisi nereden
    doguyor?
    ilk soruya verilen cevap, ikinci soruyu kendiliginden cozmez

  AYIRT EDICI HAREKETI
    "Bunu soran ben kimim; nereden, hangi usulle, hangi anda ve
     kimin gayesiyle soruyorum?"
~~~

*Çizim 17 — Yanıt 2: soranın kendi sorularının kapsamına girmesi; saat; "köken aldığı"nın iki anlamı.*

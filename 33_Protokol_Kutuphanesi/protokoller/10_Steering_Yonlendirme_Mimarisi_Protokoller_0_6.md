# Steering (Yönlendirme) Mimarisi ve Engelleme Mühendisliği

**Soru ve yanıtların protokol kaydı ve masaüstü uygulaması**

**Sürüm:** 1.0\
**Tarih:** 30 Ekim 2026\
**Kapsam:** Bölümler 0–6

Yönlendirme mimarisi, bir sistemin hangi doğrultularda hareket edebileceğini ve hangi doğrultulara ağırlık vereceğini düzenler. Engelleme mühendisliği, belirli eylemlerin, geçişlerin veya sonuçların gerçekleşmesini önleyecek ya da koşula bağlayacak mekanizmaları tasarlar ve sınar. Bu kaydın ortak konusu, eylemin mümkün olma, seçilme, gerçekleşme ve değiştirilebilme koşullarıdır. İnceleme fiziksel, dijital ve kurumsal sistemleri kapsar.

Bu belge, soruları ve yanıtları yedi protokolde bir araya getirir. Her protokolün paragraf ağırlıklı açıklaması, kavramsal ayrımları ve bunların sınırlarını korur; ardından gelen masaüstü uygulaması, girdiyi, işlemleri, beklenen kaydı, tamamlanma ölçütünü ve yeniden açma koşulunu tanımlar. Buradaki protokol, hem izlenebilir bir düşünme düzeni hem de somut bir işte kullanılabilecek çalışma yordamıdır. Başlık altında sunulan çerçeve kavramsal bir sentezdir; tek ve standartlaşmış bir disiplinin resmî protokolü olarak ileri sürülmez.

Ortak taşıyıcı sorusu bütün bölümler boyunca korunur: “Steering (Yönlendirme) Mimarisi ve Engelleme Mühendisliği'nin köken aldığı varlık, mekan, usül, zaman, ve gayeyi taşıyan makine kimdir? Kim değildir?” Bu soru, mekanizmanın işleyişiyle onu kuran, sürdüren, değiştiren ve sonuçlarından sorumlu tutulan failler arasındaki ilişkiyi araştırır. Makine, maddi taşıyıcı, işlevsel örgütlenme ve sorumlu kişi aynı kavram sayılmaz.

Kaynak bilgisi, yorum, örnek ve normatif öneri ayırt edilir. Bir yapıyı yönlendirme veya engelleme yapısı yapan özellikler, onu iyi ve meşru yapan özelliklerle özdeş kabul edilmez.

## Uygulamanın ortak düzeni

Masaüstü çalışmasında bir iş için tek bir `GOREV_KAYDI.md` kullanılır. Tohum başlangıcı kurar; 1–5, varlık, mekân, usul, zaman ve gayeyi birbirleriyle ilişkilendirir; Kökleşme sonucu dayanaklarıyla kapatır. Numaralar okuma ve kayıt düzenini gösterir. Uygulama tek yönlü bir sıra değildir: zaman ve amaç koşulları ilgili işlem yapılmadan önce değerlendirilir; yeni bilgi gerektiğinde önceki bölüme dönülür.

İncelenen sistemin özellikleriyle bu incelemeyi yürüten görevin özellikleri açık tutulur. Örneğin bir başvuru sisteminin amacı ile o sistemi inceleyen raporun amacı farklıdır. Kayıtta hangi düzeyden söz edildiği belirtilir. Kullanıcı talebi ve verilmiş yetki çalışma sınırını kurar; aynı kapsamda ilerleyen işler için tekrar tekrar izin istenmez. Sonraki adımı esaslı biçimde etkileyen eksiklik açıklığa kavuşturulur, diğer belirsizlikler kaydedilerek iş ilerletilir. Bilinmeyen kişi, yetki, tarih veya sonuç tahminle tamamlanmış bilgiye çevrilmez.

Uygulayıcı, görev için anlamlı alanları doldurur; bir boyut uygulanmıyorsa bunu kısa gerekçesiyle belirtir. Görevin yapılması ile kaydının hazırlanması ayrı değerlendirilir. Tamamlanma, gerekli işin gerçekleştiğinin gösterilmesine dayanır. Bir belgenin hazırlanması, tarif ettiği sistemin kurulmuş veya uygulamanın sonuçlarının doğrulanmış olması anlamına gelmez. Dosyalar, kişi veya asistan tarafından okunarak uygulanacak Markdown metinleridir; kurulum veya otomatik çalıştırma kodu içermez.

~~~text
  GOREV_KAYDI.md           bir is icin tek kayit
    0 Tohum                baslangici kurar
    1 Varlik  --.
    2 Mekan   --|
    3 Usul    --+--        birbirleriyle iliskilendirilir
    4 Zaman   --|
    5 Gaye    --'
    6 Koklesme             sonucu dayanaklariyla kapatir

  numaralar okuma ve kayit duzenini gosterir;
  uygulama tek yonlu bir sira degildir:
    zaman ve amac kosullari, ilgili islem yapilmadan once
    degerlendirilir; yeni bilgi gerektiginde onceki bolume donulur

  IKI DUZEY ACIK TUTULUR
    incelenen sistem                bu incelemeyi yuruten gorev
    (bir basvuru sisteminin         (o sistemi inceleyen raporun
     amaci)                          amaci)

  AYRI DEGERLENDIRILIR
    gorevin yapilmasi        =/=   kaydinin hazirlanmasi
    belgenin hazirlanmasi    =/=   tarif ettigi sistemin kurulmasi
    belgenin hazirlanmasi    =/=   uygulama sonuclarinin dogrulanmasi

  IZIN VE BELIRSIZLIK
    ayni kapsamda ilerleyen isler icin tekrar tekrar izin istenmez
    sonraki adimi esasli bicimde etkileyen eksiklik acikliga
    kavusturulur; diger belirsizlikler kaydedilir, is ilerletilir
    bilinmeyen kisi, yetki, tarih ya da sonuc tahminle doldurulmaz
~~~

*Çizim 1 — Ortak düzen: tek görev kaydı, iki düzey, ayrı değerlendirilenler.*

## 0 Tohum (Başlangıç) Protokolü

**Bu bölüm için geliştirilmiş kurucu soru:** İncelenen yönlendirme ve engelleme düzeni hangi koşullardan doğmuştur ve biz onu hangi soru, başlangıç bilgisi ve çalışma sınırlarıyla incelemeye başlıyoruz? Bu soru, bölümün kurulması için geliştirilmiştir; kullanıcının önceki sorularından birebir alıntı değildir.

Tohum Protokolü, incelemenin başlangıç dayanaklarını görünür kılar. İncelenecek düzenin ne olduğunu, hangi soruyla ele alındığını, elde hangi bilgilerin bulunduğunu ve hangi belirsizliklerle yola çıkıldığını kayda geçirir. Burada başlangıç iki ayrı anlam taşır: incelenen düzenin ortaya çıkışı ve o düzen hakkında yürütülen incelemenin başlaması. Bir yönlendirme düzeni daha önce kurulmuş olabilir; onun hangi kararları mümkün, zor veya imkânsız kıldığını araştırmaya bugün başlanabilir. Bu iki başlangıcın tarihleri, failleri ve gerekçeleri ayrı ayrı belirlenir; biri hakkındaki bilgi diğerinin kanıtı sayılmaz.

Bu protokolü ayırt eden, sonraki açıklamaların hangi zeminden geliştiğini izlenebilir hâle getirmesidir. İncelemenin ana sorusu, nesnesi, kapsamı, kullanılan malzemeleri ve ilk varsayımları birlikte kaydedilir. Bu belgenin başlangıç koşulları, kullanıcının bu konuşmada verdiği sorular ve yönlendirmelerdir. Önceki konuşmalardan bağlam taşınmaz. Bununla birlikte inceleme nesnesi mevcut sohbet arayüzüyle sınırlandırılmaz: gerektiğinde insanları, kurumları, yazılı kuralları, teknik araçları, kaynak dağılımını ve bunların ilişkilerini içerebilir. İncelemenin kavramsal kapsamının geniş olması, mevcut kayıtların dışındaki bir iddiayı kendiliğinden doğrulanmış hâle getirmez.

Tohum, sonraki bütün cevapları içinde hazır taşıyan bir hüküm değildir. İlk beklentiler, kanıt geldikçe değişebilecek başlangıç varsayımlarıdır; düzenin neden kurulduğuna dair bir anlatı da gerçekleşen işleyişin yeterli açıklaması olmayabilir. Bu nedenle başlangıç niyeti, gözlenen ihtiyaç, belgelenmiş kuruluş kararı ve sonradan yapılan yorum birbirinden ayrılır. Tohum Protokolü'nün 5 Gaye Protokolü ile ilişkisi de buradan anlaşılır: Tohum, incelemenin hangi koşullardan ve hangi sorudan hareket ettiğini kurar; Gaye, incelenen düzenin hangi nihai amaca hizmet ettiğini, bu amacı kimin belirlediğini ve sonuçların onunla ilişkisini değerlendirir. Başlangıçta yazılan amaç cümlesi, beşinci bölümün vereceği cevabı peşinen kesinleştirmez.

Başlangıcı taşıyan fail veya makine, her durumda tek bir kişi olarak varsayılamaz. İncelenen düzenin kuruluşuna katılanlar, onu bugün işletenler, kurallarını değiştirebilenler ve bu incelemeyi yürütenler farklı olabilir. Bu protokol, bilinen aktörleri somut yetkileriyle kaydeder: soruyu kim ortaya koymuştur, hangi bilgi kim tarafından sağlanmıştır, çalışma kapsamını kim belirleyebilir, hangi işlem hangi araçla yapılabilir? Bir metni üreten araç, sırf bu üretimi yaptığı için incelenen düzenin kurucusu, amaç koyucusu veya bütün sonuçlarından sorumlu öznesi sayılmaz. Kimlik ve yetki bilinmiyorsa, bu boşluk bir kişi ya da gizli merkez varsayımıyla doldurulmaz.

Başlangıç kaydının dayanağı, eldeki malzemenin niteliğinin açık olmasıdır. Kullanıcının soruları, gözlenen olgular, belgelerden gelen bilgiler, çalışma sırasında geliştirilen tanımlar ve önerilen ilkeler aynı türden kayıtlar olarak sunulmaz. Belgesi bulunmayan bir kuruluş öyküsü, doğrulanmış tarihçe diye yazılmaz; açıklama için kullanılan örnek, yaşanmış olay diye aktarılmaz. Açık sorular ve geçici varsayımlar da kaydın parçasıdır. Böylece ileride bir sonuç değiştiğinde, değişimin yeni bilgiye mi, kapsam düzeltmesine mi, yoksa başlangıçta yapılan bir yorumun gözden geçirilmesine mi dayandığı anlaşılabilir.

~~~text
  IKI AYRI BASLANGIC

   incelenen duzenin                          bu duzen hakkindaki
   ortaya cikisi                              incelemenin baslamasi
        |                                            |
   -----*--------------------------------------------*---------> zaman
        duzen daha once kurulmus olabilir            hangi kararlari
                                                     mumkun, zor ya da
                                                     imkansiz kiliyor?

   her biri icin ayri belirlenir:  tarih . failler . gerekce
   biri hakkindaki bilgi, digerinin kaniti sayilmaz

  AYRI TUTULAN DORT SEY
    baslangic niyeti | gozlenen ihtiyac |
    belgelenmis kurulus karari | sonradan yapilan yorum

  AYNI TURDEN KAYIT OLARAK SUNULMAZ
    kullanicinin sorulari . gozlenen olgular .
    belgelerden gelen bilgiler .
    calisma sirasinda gelistirilen tanimlar . onerilen ilkeler

  TOHUM ILE GAYE
    0 Tohum   inceleme hangi kosullardan, hangi sorudan hareket ediyor?
    5 Gaye    incelenen duzen hangi nihai amaca hizmet ediyor?
    baslangicta yazilan amac cumlesi, besinci bolumun cevabini
    pesinen kesinlestirmez

  bir metni ureten arac, sirf bu uretimi yaptigi icin incelenen
  duzenin kurucusu, amac koyucusu ya da butun sonuclarindan sorumlu
  oznesi sayilmaz
~~~

*Çizim 2 — Tohum: iki ayrı başlangıç; Tohum ile Gaye'nin ayrı soruları.*

Bu protokolün tamamlanması, bütün incelemenin sonuçlanması anlamına gelmez. Sonraki bölümlerde ilerlemeye elverecek kadar açık bir soru, nesne, kapsam ve bilgi durumu oluşması yeterlidir. Çalışma, verilmiş yetki içinde ilerler; aynı kapsamda kalan geri alınabilir düzenlemeler için her adımda yeniden onay istenmez. Buna karşılık mevcut yetkinin dışına çıkan bir eylem veya cevabı olmadan geçerli bir sonraki adım kurulamayacak bir eksiklik, açıkça belirlenir. Tohum kaydı ilk sürümüyle korunur; nesne ya da kapsam değişirse başlangıç koşulları gerekçesiyle güncellenir. Bu kayıt, 1 Varlık Protokolü'ne geçişin dayanağıdır.

### Masaüstü uygulaması

**Girdi:** Bu çalışma için verilmiş kullanıcı talebi, mevcut soru ve yanıtlar, sağlanmış belgeler, bilinen inceleme nesnesi ve istenen çıktı biçimi. Bir girdinin kaynağı veya tarihi bilinmiyorsa bilgi eksikliği açıkça belirtilir.

**İşlemler:**

1. `GOREV_KAYDI.md` dosyasındaki **0 Tohum** bölümünü aç. Ana soruyu, incelenecek nesneyi ve bu çalışma sonunda hazırlanması beklenen çıktıyı tek bir giriş paragrafında yaz.
2. Kullanılacak mevcut malzemeleri kaydet. Her birinin bilinen kaynağını ve niteliğini belirt; kullanıcı sorusu, sağlanmış belge, gözlem, çıkarım ve öneriyi ayırt et. Önceki konuşmalardan kendiliğinden bağlam ekleme.
3. İncelenen düzenin başlangıcına ilişkin bilgileri, bu incelemenin başlama nedeni ve koşullarından ayrı paragraflarda yaz. Bilinmeyen kuruluş bilgilerini bilinmiyor olarak bırak; ilk varsayımları işaretle.
4. Kapsamı, kapsam dışında kalan konuları, kullanılabilecek araçları ve mevcut yetkiyi kaydet. Bilinen sorumluları somut görevleriyle belirt; bilinmeyen bir görevliyi atama. Yetkilendirilmiş ve geri alınabilir belge düzenlemelerini tekrar tekrar onay beklemeden yürüt.
5. Açık soruları 1–5 arasındaki ilgili protokollere yönlendir. Sonraki geçerli adımı gerçekten engelleyen eksikleri ayrıca belirt; diğer belirsizlikleri kayıt altında tutarak incelemeye devam et.

**Çıktı:** `GOREV_KAYDI.md` içindeki **0 Tohum** bölümünde ana soru, inceleme nesnesi, iki başlangıcın ayrımı, malzemeler, kapsam, mevcut yetki, ilk varsayımlar ve açık sorular bulunur.

**Tamamlanma ölçütü:** Başka bir okur, neyin ve hangi koşullarla inceleneceğini; hangi bilgilerin mevcut, hangilerinin varsayım veya eksik olduğunu anlayabilmelidir. Gaye sorusunun nihai cevabının bu aşamada bulunması gerekmez.

**Yeniden açma koşulu ve geçiş:** Başlangıç kaydı yeterliyse 1 Varlık Protokolü'ne geçilir. Ana soru, inceleme nesnesi veya çalışma kapsamı değişirse bu bölüm yeniden açılır; önceki kayıt silinmeden değişiklik ve gerekçesi yazılır.

## 1 Varlık Protokolü

> Nedir? Onu o yapan nelerdir? Neler değildir?

### Tanım ve kurucu ayrımlar

Yönlendirme, olası davranışlar ve gidişatlar arasında yön farkı üretir. Bazı seçenekleri daha görünür, anlaşılır, kolay, ödüllendirici veya öncelikli hâle getirir. Bazı hareketleri doğrudan başlatır; bazılarını dolaylı olarak daha olası kılar. Bir güzergâh önerisi, kurumun başarı ölçütü, arayüzün varsayılan seçeneği ve makinenin hedef konumu, farklı mekanizmalarla yönlendirici olabilir. Seçim mimarisi yaklaşımında varsayılanlar, geri bildirim, seçeneklerin yapılandırılması ve teşvikler, karar ortamını düzenleyen araçlar arasında yer alır. [3]

Engelleme, belirli bir ihtimalin gerçekleşmeye dönüşmesini sınırlandırır. Eylem durdurulabilir, bir koşula bağlanabilir, kapsamı daraltılabilir veya belirli bir süre ertelenebilir. Normatif yasak, davranışın yapılmaması gerektiğini belirtir. Fiilî engel, gerçekleşmesini maddi veya teknik olarak sınırlar. Pratik erişilemezlik ise kâğıt üzerinde mümkün olan bir işlemin zaman, bilgi, para veya çaba gereksinimleri yüzünden kişi açısından kullanılamaz hâle gelmesidir. Bu üç durum benzer sonuçlar üretebilse de aynı mekanizma değildir.

~~~text
  ENGELLEME  bir ihtimalin gerceklesmeye donusmesini sinirlar

  eylem:  durdurulabilir . bir kosula baglanabilir .
          kapsami daraltilabilir . belirli bir sure ertelenebilir

  UC AYRI DURUM  benzer sonuc uretebilir; ayni mekanizma degildir

   normatif yasak          fiili engel            pratik erisilemezlik

      [ YASAK ]                  ##               --.   .-.   .-.   .-->
   ---------------->       ------##                 |   | |   | |   |
                                 ##                 `---' `---' `---'

   davranisin              gerceklesmeyi          kagit uzerinde mumkun
   yapilmamasi             maddi ya da            olan islem; zaman,
   gerektigini             teknik olarak          bilgi, para ya da caba
   belirtir                sinirlar               gereksinimi yuzunden
                                                  kisi icin kullanilamaz
                                                  hale gelir
~~~

*Çizim 3 — Varlık: engellemenin üç ayrı durumu; normatif yasak, fiilî engel, pratik erişilemezlik.*

Mimari, bilgi, karar, kaynak, yetki ve uygulama arasındaki ilişkilerin düzenidir. Mühendislik, bu ilişkilerin belirli koşullarda çalışacak ve başarısızlığı değerlendirilebilecek mekanizmalara dönüştürülmesidir. Yönlendirmenin de mühendisliği, engellemenin de mimarisi vardır. Başlıktaki iki ifade farklı vurgular taşır; birbirinden yalıtılmış iki alan kurmaz.

Bir davranış veya durum alanı, tercih ve sınırları ayıran ölçütler, davranış üzerinde etkili müdahale bağlantıları ve bu bağlantıları sürdüren bir örgütlenme, yapının kurucu unsurlarıdır. Bu unsurların özgüllüğü, eylemin oluşma koşullarını birlikte düzenlemelerindedir. Bir yolun kapatılması diğer yolları öne çıkarabilir; bir seçeneğin sürekli görünmez veya aşırı zahmetli kılınması fiilî engel oluşturabilir. Buna karşılık açıklayıcı bilgi seçenekleri çoğaltabilir ve bir engel yalnızca belirli bir işlemi durdurabilir.

~~~text
  YONLENDIRME  olasi davranislar ve gidisatlar arasinda yon farki uretir

                        .========>  one cikan secenek: daha gorunur,
                       //           anlasilir, kolay, odullendirici
   durum =============++            ya da oncelikli
                       \\
                        \`------->  oteki secenek
                         \
                          `. . .>   surekli gorunmez ya da asiri
                                    zahmetli kilinan secenek

  yonlendirici olabilenler (farkli mekanizmalarla)
    bir guzergah onerisi . kurumun basari olcutu .
    arayuzun varsayilan secenegi . makinenin hedef konumu

  IKISI BIRBIRINE DOKUNUR
    bir yolun kapatilmasi          -->  diger yollari one cikarabilir
    bir secenegin surekli gorunmez
    ya da asiri zahmetli kilinmasi -->  fiili engel olusturabilir
    aciklayici bilgi               -->  secenekleri cogaltabilir
    bir engel                      -->  yalnizca belirli bir islemi
                                        durdurabilir

  KURUCU UNSURLAR  eylemin olusma kosullarini birlikte duzenler
    bir davranis ya da durum alani
    tercih ve sinirlari ayiran olcutler
    davranis uzerinde etkili mudahale baglantilari
    bu baglantilari surduren bir orgutlenme

  yonlendirmenin de muhendisligi, engellemenin de mimarisi vardir
~~~

*Çizim 4 — Varlık: yönlendirme yön farkı üretir; yönlendirme ile engelleme birbirine dokunur.*

### Makine ve fail

Makine, burada yalnızca elektronik veya mekanik bir nesne anlamına gelmez. Ashby'nin sibernetik yaklaşımı, farklı maddi taşıyıcılardaki davranış biçimlerini ve ilişkilerini birlikte incelemeye imkân verir. Bu yaklaşım, maddi taşıyıcıyla işlevsel örgütlenmenin ayrılmasına yardımcı olur. [1]

İnsan eliyle kurulmuş sistemlerde makinenin taşıyıcısı, amaç kurma ve eyleme geçme kapasitesinin insanlar, kurumlar, kurallar, kayıtlar, kaynaklar ve teknik araçlarla örgütlenmesidir. “Kim” sorusu ise bu örgütlenmede amacı koyan, yetkiyi dağıtan, kuralı uygulayan, değiştiren ve sonuçların hesabını veren somut failleri arar. Makine, kişi ve fail aynı kavram değildir. Bu tanım, doğadaki bütün düzenleme süreçlerini insan iradesine bağlayan evrensel bir köken iddiası taşımaz.

Köken, taşıyıcı, fail ve gaye birbirinden ayrılır. Bir düzen belirli bir ihtiyaçtan doğabilir; belgeler ve altyapı sayesinde sürebilir; farklı kişilerce işletilebilir ve zaman içinde başka hedeflere hizmet edebilir. Aristoteles'in madde, biçim, değişimin kaynağı ve uğruna yapılan şey arasında kurduğu ayrım, bu farklı açıklamaları birbirine karıştırmamak için tarihsel bir dayanak sağlar. Beş protokol bu dört nedene bire bir eşitlenmez. [2]

~~~text
  AYNI KAVRAM SAYILMAZ
    makine | maddi tasiyici | islevsel orgutlenme | sorumlu kisi

  INSAN ELIYLE KURULMUS SISTEMDE MAKINENIN TASIYICISI
    amac kurma ve eyleme gecme kapasitesinin su ogelerle orgutlenmesi:
    insanlar . kurumlar . kurallar . kayitlar . kaynaklar .
    teknik araclar

  "KIM?" SORUSU  bu orgutlenmede somut failleri arar
    amaci koyan . yetkiyi dagitan . kurali uygulayan .
    kurali degistiren . sonuclarin hesabini veren

  BIR DUZENIN OYKUSUNDE DORT AYRI SORU

    ihtiyac
       |
       v
   ----*==========================================================>
     dogar        surer              isletilir        baska hedeflere
                  (belgeler ve       (farkli          hizmet edebilir
                   altyapi           kisilerce)       (zaman icinde)
                   sayesinde)

     KOKEN        TASIYICI           FAIL             GAYE

  bes protokol, Aristoteles'in dort nedenine bire bir esitlenmez
~~~

*Çizim 5 — Varlık: makine, taşıyıcı, örgütlenme ve fail; bir düzenin öyküsünde dört ayrı soru.*

### Kimliğin sınırları

Her etki bilinçli yönlendirme, her güçlük tasarlanmış engel değildir. Kasıt, ihmal, kapasite yetersizliği ve birbiriyle uyuşmayan süreçler benzer sonuçlar üretebilir. Etkiyi saptamakla niyet atfetmek ayrı işlerdir. Tek bir merkez görünmemesi yönlendirme bulunmadığını; ortak bir sonuç görülmesi de ortak bir irade bulunduğunu kanıtlamaz.

Yönlendirme, her durumda mutlak davranış belirleme değildir. Yapay zekâdaki aktivasyon mühendisliği gibi dar steering yöntemleri, modelin iç aktivasyonlarını değiştirerek çıktı özelliklerini etkilemeyi amaçlar; bir kaynağa erişimi teknik olarak kapatmakla aynı işlem değildir. [14] Aynı şekilde sürekli geri bildirim, her yönlendirme düzeninin zorunlu özelliği değildir; sabit düzenlemeler de yönlendirebilir.

Bir yapının var olması, iyi işlemesi ve meşru olması ayrı değerlendirmelerdir. İnsan da bu yapı içindeki görevine indirgenemez. Kurucu, uygulayıcı veya denetlenen kişi, kendisine verilmiş rolü sorgulayabilir ve başka amaçlar kurabilir. Varlık kaydı, düzenin ne olduğunu açıklarken bu ayrımları korur.

~~~text
   kasit --------------------.
   ihmal --------------------+
                             +------>  benzer sonuc
   kapasite yetersizligi ----+
   uyusmayan surecler -------'

   her etki bilincli yonlendirme, her gucluk tasarlanmis engel degildir
   etkiyi saptamak   =/=   niyet atfetmek

  KANITLAMAZ
    tek bir merkez gorunmuyor    -x->   yonlendirme yok
    ortak bir sonuc goruluyor    -x->   ortak bir irade var

  HER DURUMDA BOYLE DEGILDIR
    yonlendirme, mutlak davranis belirleme degildir
    surekli geri bildirim zorunlu ozellik degildir;
    sabit duzenlemeler de yonlendirebilir

    aktivasyon muhendisligi              bir kaynaga erisimi
    (modelin ic aktivasyonlarini   =/=   teknik olarak kapatmak
     degistirerek cikti
     ozelliklerini etkilemek)

  UC AYRI DEGERLENDIRME
    yapinin var olmasi | iyi islemesi | mesru olmasi

  insan, bu yapi icindeki gorevine indirgenemez:
  kendisine verilmis rolu sorgulayabilir, baska amaclar kurabilir
~~~

*Çizim 6 — Varlık: kimliğin sınırları; etkiyi saptamak niyet atfetmek değildir.*

### Masaüstü uygulaması

**Girdi:** Tohum bölümündeki ana soru, istenen sonuç, kapsam ve eldeki materyaller.

**İşlemler:**

1. Üzerinde çalışılan şeyi bir cümleyle tanımla. Bunun bir belge, bilgi kümesi, dosya düzeni, karar süreci veya başka bir sistem olup olmadığını belirt.
2. İstenen değişikliği mevcut durumdan ayır. Hangi özelliklerin korunacağını ve hangi ilişkinin değişeceğini somutlaştır.
3. Varsa yönlendirmeyi ve engeli adlandır. Seçeneği öne çıkaran düzenle engelin hangi geçişi sınırladığını ayrı yaz; bulunmayan bir mekanizmayı varsayma.
4. Maddi veya teknik taşıyıcıyı, işi yapanı, amacı belirleyeni ve kuralı değiştirebileni ayır. Aynı kişi birden fazla rol taşıyorsa bunu belirt; bilinmeyen rolleri bilinmiyor olarak kaydet.
5. Tanımı mevcut materyalle karşılaştır. Çalışılan nesneyle ilgili varsayımı, doğrulanmış bilgiden ayır ve kapsam dışındaki konuları belirt.

**Çıktı:** `GOREV_KAYDI.md` içindeki **1 Varlık** bölümünde nesne tanımı, değişecek ve korunacak özellikler, yönlendirme ve engel açıklaması, taşıyıcı ve fail rolleri bulunur.

**Tamamlanma ölçütü:** Çalışmanın konusu, beklenen değişiklik ve ilgili roller birbirine karıştırılmadan açıklanabiliyordur. Belirsizlikler açıkça işaretlenmiştir.

**Yeniden açma koşulu:** İşin nesnesi, kapsamı, korunacak özellikleri veya fiilen karar verebilen tarafı değişir; tanım mevcut kanıtla çelişir.

## 2 Mekan Protokolü

> Nerededir? Bu yeri, oraya has bir yer yapan nelerdir? Neler değildir?

### Mekânın tanımı

Yönlendirme ve engellemenin yeri, ihtimalin fark edilen seçeneğe, seçeneğin karara, kararın uygulanabilir eyleme ve eylemin sonuca dönüştüğü ilişkilerde bulunur. Bu yer, yalnızca bina, cihaz veya sunucu gösterilerek açıklanamaz. Hangi konuların gündeme girdiği, hangi bilgilerin görüldüğü, hangi alternatiflerin erişilebilir olduğu ve kimin kararının sonuç ürettiği birlikte incelenir.

Anlamlandırma düzlemi, neyin sorun, başarı veya risk sayıldığını belirler. Görünürlük düzlemi, seçeneklerin fark edilmesini etkiler. Teşvik ve maliyet düzeni, yolları kolaylaştırır veya zorlaştırır. Yetki düzeni, kimin hangi kararı verebildiğini; uygulama düzeni, hangi kararın gerçekleştiğini; düzeltme düzeni ise hangi kararların yeniden açılabildiğini belirler. Bunlar bütün sistemlerde aynı sınırlarla bulunması gereken katmanlar değil, konumu çözümlemek için kullanılan ayrımlardır.

Bir konumu özgül kılan, ilgili geçiş üzerinde aracılık ve müdahale gücüdür. Bir olay hakkında bilgi sahibi olmak, o olayı durdurabilme gücüyle aynı değildir. İşlem tamamlandıktan sonra uyarı veren bir ekran, tamamlanmış işlemi önlemiş olmaz; sonraki işlemleri durdurabilir, inceleme başlatabilir veya düzeltmeye yardımcı olabilir. Bu etkiler ayrı kaydedilir.

### Karar ve uygulamanın yerleri

Kuralın yazıldığı yer, kararın verildiği yer, kararın uygulandığı yer ve sonucun yaşandığı yer farklı olabilir. NIST'in Zero Trust Architecture belgesi, erişim kararını veren işlevlerle kararı uygulayan noktayı ayırır. Uygulama noktası, özne ile kaynak arasındaki bağlantıyı açar, izler ve sonlandırır; bu görev fiziksel olarak birden fazla bileşene dağılabilir. [4]

~~~text
  YER, SU DONUSUMLERIN GECTIGI ILISKILERDEDIR

   ihtimal --> fark edilen --> karar --> uygulanabilir --> sonuc
               secenek                   eylem

   bir konumu ozgul kilan: ilgili gecis uzerinde aracilik ve
   mudahale gucu

  KONUMU COZUMLEMEK ICIN ALTI AYRIM  (her sistemde ayni sinirlarla
                                      bulunan katmanlar degildir)
    anlamlandirma duzlemi      neyin sorun, basari ya da risk sayildigi
    gorunurluk duzlemi         seceneklerin fark edilmesi
    tesvik ve maliyet duzeni   yollarin kolaylasmasi ya da zorlasmasi
    yetki duzeni               kimin hangi karari verebildigi
    uygulama duzeni            hangi kararin gerceklestigi
    duzeltme duzeni            hangi kararlarin yeniden acilabildigi

  FARKLI OLABILEN DORT YER
    kuralin yazildigi yer | kararin verildigi yer |
    kararin uygulandigi yer | sonucun yasandigi yer

  NIST ornegi: erisim kararini veren ile uygulayan ayridir

                   .------------------------.
                   |  karar veren islevler  |
                   `-----------+------------'
                               | erisim karari
                               v
      ozne ---------[ uygulama noktasi ]--------- kaynak
                    baglantiyi acar, izler, sonlandirir
                    (birden fazla bilesene dagilabilir)

  bir olay hakkinda bilgi sahibi olmak  =/=  o olayi durdurabilme gucu
~~~

*Çizim 7 — Mekan: ihtimalden sonuca giden zincir, altı ayrım; karar veren ile uygulayan.*

Bu ayrımdan hareketle, bir yönetmeliğin merkezde yazılması gerçek engelin de merkezde bulunduğunu göstermez. Engel yerel prosedürde, kaynak tahsisinde veya uygulama hizmetinde oluşabilir. Arayüzdeki görünür seçenekle işlemin fiilen yürütülebilmesi ayrı araştırılır. Bir amaç belgesinin yanında çalışanların davranışını etkileyen başarı ve ödül düzeni de incelenir.

Dağıtık bir yapıda engel, birden fazla bağımlılığın birleşiminde ortaya çıkabilir. Varsayımsal bir başvuruda başka kurumdan belge alınması, o kurumun dar saatlerde çalışması, sistemin yalnızca belirli dosya biçimini kabul etmesi ve son tarihin yaklaşması birlikte erişimi sınırlandırabilir. Böyle bir durumda tek bir ret düğmesi aramak, geçişlerin tamamını açıklamaz.

### Taşıyıcı ve mekânsal sınırlar

Makinenin mekânını, erişimin ve etkinin dağılımı kurar. Bir kararın hangi alana ulaşabildiği ve bir itirazın hangi noktada durduğu, failin konumunu görünür kılar. Kurumun resmî sınırıyla fiilî etkisinin sınırı aynı olmayabilir. Sistem içinde çalışan bir kişi, kuralları değiştirme yetkisinin dışında kalabilir. İçerisi ve dışarısı, hangi sistemin sınır kabul edildiğine bağlıdır.

Hedefleri, eşikleri, istisnaları ve yetki dağılımını değiştirebilen tarafların konumu da mimariye dâhildir. Tekil kararı değiştirmekle karar kuralını değiştirmek aynı yetki değildir. Bir itiraz birimi belirli sonucu düzeltebilir; başka bir organ genel kuralı değiştirebilir. Bu güçlerin nerede birleştiği veya ayrıldığı ayrıca kaydedilir.

Dağıtık yapı, herkesin eşit yetkiye sahip olduğunu veya kimsenin sorumlu olmadığını göstermez. Yalnızca görünen arayüz, resmî metin ya da en üst yönetici bütün mimari yerine konulmaz. Mekan kaydı, hangi bağlantının hangi davranışı etkilediğini, kararın nerede uygulandığını ve düzeltmenin nerede mümkün olduğunu gösterdiği ölçüde açıklayıcıdır.

~~~text
  VARSAYIMSAL BASVURU  engel, birden fazla bagimliligin birlesiminde

   basvuran
      o---->  | 1 |  ---->  | 2 |  ---->  | 3 |  ---->  | 4 |  - - ->  ?

   1  baska kurumdan belge alinmasi
   2  o kurumun dar saatlerde calismasi
   3  sistemin yalnizca belirli dosya bicimini kabul etmesi
   4  son tarihin yaklasmasi

   birlikte erisimi sinirlandirabilir;
   tek bir ret dugmesi aramak, gecislerin tamamini aciklamaz

  YERI ARARKEN
    yonetmelik merkezde yazilmis   -x->   gercek engel de merkezde
    engel sunlarda olusabilir:  yerel prosedur . kaynak tahsisi .
                                uygulama hizmeti
    arayuzdeki gorunur secenek   =/=   islemin fiilen yurutulebilmesi
    kurumun resmi siniri         =/=   fiili etkisinin siniri

  IKI AYRI YETKI
    tekil karari degistirmek      bir itiraz birimi belirli sonucu
                                  duzeltebilir
    karar kuralini degistirmek    baska bir organ genel kurali
                                  degistirebilir

  DAGITIK YAPI SUNU GOSTERMEZ
    herkes esit yetkiye sahip . kimse sorumlu degil
~~~

*Çizim 8 — Mekan: engel birden fazla bağımlılığın birleşiminde; tekil karar ile karar kuralı.*

### Masaüstü uygulaması

**Girdi:** Varlık bölümündeki nesne ve rol tanımları, erişilebilir dosyalar, uygulamalar ve kaynaklar.

**İşlemler:**

1. Kaynak materyalin, çalışma kopyasının ve teslim edilecek sonucun yerini belirle. Dosya yolu veya bağlantıyı gözlenen biçimiyle kaydet; aynı adlı kopyaları ayırt et.
2. Bir kararı veren konumla kararı uygulayan konumu ayır. Örneğin bir belgede yazılı kuralın hangi uygulama, kişi veya işlem tarafından gerçekleştirildiğini göster.
3. Görev için gerekli erişimi ve mevcut yetkiyi belirle. Okuma, düzenleme ve sonucu teslim etme kapsamını kullanıcı talebiyle ilişkilendir; gerekli erişim zaten varsa çalışmayı sürdür.
4. Sonuca ulaşmak için gereken bağımlılıkları incele. Eksik dosya, başka bir kaynağa bağlı bilgi veya erişilemeyen uygulama varsa bunun hangi adımı etkilediğini yaz.
5. Hatalı bir kararı veya dosya değişikliğini kimin, nerede düzeltebildiğini belirle. Görünen arayüzün fiilî uygulama noktasını temsil edip etmediğini kontrol et.

**Çıktı:** `GOREV_KAYDI.md` içindeki **2 Mekan** bölümünde kaynak ve hedef konumları, karar ve uygulama noktaları, erişim kapsamı, bağımlılıklar ve düzeltme yolu bulunur.

**Tamamlanma ölçütü:** Kaynağın nereden alındığı, sonucun nereye yazılacağı ve işlemin hangi noktada gerçekleşeceği bellidir. Eksik erişimin etkisi belirlenmiştir.

**Yeniden açma koşulu:** Kaynak veya hedef taşınır, kopyalar çatışır, uygulama yolu değişir ya da mevcut yetki istenen işlemi karşılamaz.

## 3 Usül Protokolü

> Nasıl işler yapar? Bu yaptıklarını, ona has yapan nelerdir? Neler değildir?

### İşleyişin kuruluşu

Yönlendirme ve engelleme, durum bilgisini, ölçütleri ve müdahaleyi birbirine bağlayarak işler. Durumun tanınması, seçeneklerin değerlendirilmesi, kararın verilmesi, kararın uygulanması ve sonuçların incelenmesi farklı işlevlerdir. Bunlar aynı kişi veya bileşende toplanabilir; ancak kavramsal olarak ayrılmalıdır. Her sistem için zorunlu tek sıra veya sürekli kapalı çevrim varsayılmaz.

Yönlendirme, hazır seçenekleri sıralamanın yanında hangi seçeneklerin üretileceğini de etkileyebilir. Bir toplantı gündemi tartışma alanını, form kategorileri bir durumun nasıl ifade edileceğini, teknik hedef ise hangi çözümlerin aranacağını şekillendirir. Bu nedenle mevcut seçeneklerle fark edilen seçenekler ve uygulanabilen seçenekler ayrı değerlendirilir. Bir seçeneğin teorik varlığı, karar sürecinde etkili yer tuttuğunu göstermez.

Görünürlük ve işlem yükü de usulün parçalarıdır. FTC'nin Bringing Dark Patterns to Light raporu, bulunması zor açıklamalar, önceden işaretli seçenekler ve karmaşık iptal süreçleri gibi tasarımların kullanıcı kararları üzerindeki etkisini ele alır. [7] Bu örnekler, açık yasak bulunmasa da karar ortamının davranışı biçimlendirebildiğini gösterir. Her davranış etkisi bu nedenle aldatıcı sayılmaz; amaç, yöntem ve etki ayrıca incelenir.

~~~text
  BES AYRI ISLEV  ayni kiside ya da bilesende toplanabilir;
                  kavramsal olarak ayrilir

    durumun taninmasi . seceneklerin degerlendirilmesi .
    kararin verilmesi . kararin uygulanmasi . sonuclarin incelenmesi

    her sistem icin zorunlu tek sira ya da surekli kapali cevrim
    varsayilmaz

  YONLENDIRME, HANGI SECENEKLERIN URETILECEGINI DE ETKILER
    toplanti gundemi    -->  tartisma alani
    form kategorileri   -->  bir durumun nasil ifade edilecegi
    teknik hedef        -->  hangi cozumlerin aranacagi

  AYRI DEGERLENDIRILEN UC KUME

    mevcut secenekler           o o o o o o o o o o o o o
    fark edilen secenekler          o o o o o o
    uygulanabilen secenekler            o o

    bir secenegin teorik varligi, karar surecinde etkili yer
    tuttugunu gostermez

  GORUNURLUK VE ISLEM YUKU DE USULUN PARCALARIDIR
    bulunmasi zor aciklamalar . onceden isaretli secenekler .
    karmasik iptal surecleri
    (her davranis etkisi bu nedenle aldatici sayilmaz;
     amac, yontem ve etki ayrica incelenir)
~~~

*Çizim 9 — Usül: beş ayrı işlev; mevcut, fark edilen ve uygulanabilen seçenekler.*

### Uygulama ve yetki

Bir engel, belirli bir değerlendirmeyi uygulama koşuluna bağladığında fiilen işler. Koşul kimliğe, yetkiye, kapasiteye, süreye, duruma veya kapsama ilişkin olabilir. İşlem reddedilebilir, daraltılabilir, ertelenebilir veya başka bir karar vericiye aktarılabilir. Engelin kime, hangi eyleme ve hangi kaynağa uygulandığı; ne zaman başlayıp kalktığı ve hangi işlem yollarını kapsadığı açık olmalıdır.

Bilgi güvenliğindeki tam aracılık ilkesi, erişimlerin yetki bakımından denetlenmesini ister. Saltzer ve Schroeder, yetkili kullanımın yetkisiz biçimde engellenmesini de güvenlik ihlalleri arasında ele alır. [5] Bu nedenle bir engelin başarısı yalnızca durdurduğu işlemlerle değerlendirilemez; gerekli ve yetkili işlerin sürmesi de değerlendirmeye dâhildir. Erişim kontrolüne ait ilkeler, bütün fiziksel ve toplumsal durumlara koşulsuz durdurma buyruğu olarak taşınmaz.

Usuldeki fail, yalnızca son işlemi yapan kişi değildir. Hangi bilginin hangi değerlendirmeye, hangi değerlendirmenin hangi izne veya engele dönüşeceğini belirleyen taraf da etkilidir. Verilmiş kurallar altında karar vermekle bu kuralları değiştirmek farklı güçlerdir. İnsan onayının etkili denetim sayılabilmesi için onay verenin yeterli bilgi, zaman ve kararı değiştirme imkânı bulunmalıdır.

### Hata düzeltme ve başarı

Uygunsuzlukla belirsizlik ayrı tutulur. Bir talebin koşulları sağlamadığına dair kanıt ile değerlendirme için bilginin eksik olması aynı değildir. Eksik belge veya düşük güven, tek başına uygunsuzluk kanıtı sayılmaz. Ek bilgi isteme ve inceleme yolları, gecikmenin ve yanlış kararın maliyetiyle birlikte tasarlanır.

~~~text
  ENGEL NE ZAMAN FIILEN ISLER?
  belirli bir degerlendirmeyi uygulama kosuluna bagladiginda

    kosul sunlara iliskin olabilir
      kimlik . yetki . kapasite . sure . durum . kapsam
    islem
      reddedilebilir . daraltilabilir . ertelenebilir .
      baska bir karar vericiye aktarilabilir
    acik olmasi gerekenler
      kime, hangi eyleme, hangi kaynaga uygulaniyor?
      ne zaman baslayip kalkiyor?
      hangi islem yollarini kapsiyor?

  BIR ENGELIN BASARISI YALNIZCA DURDURDUKLARIYLA DEGERLENDIRILMEZ

                                izin verildi       reddedildi
    kosullari sagliyor          yetkili is surer   YANLIS RET
    saglamadigina kanit var     YANLIS IZIN        islem durdurulur
    bilgi eksik                 . . . . . belirsizlik . . . . .

    eksik belge ya da dusuk guven, tek basina uygunsuzluk kaniti
    sayilmaz; ek bilgi isteme ve inceleme yollari, gecikmenin ve
    yanlis kararin maliyetiyle birlikte tasarlanir

    yetkili kullanimin yetkisiz bicimde engellenmesi de guvenlik
    ihlalleri arasinda ele alinir  (Saltzer ve Schroeder)

  IKI AYRI GUC
    verilmis kurallar altinda karar vermek   =/=   bu kurallari
                                                   degistirmek
~~~

*Çizim 10 — Usül: engelin koşulu ve sonucu; yanlış izin, yanlış ret ve belirsizlik.*

Hedefe ilerleme ve sınırlar içinde kalma birlikte değerlendirilmeye muhtaçtır. Ames ve çalışma arkadaşları, belirli dinamik sistemlerde performans hedeflerini ve güvenlik koşullarını ortak optimizasyon içinde ele alır. Matematiksel güvenceler model ve uygulanabilirlik varsayımlarına bağlıdır. [6] Genel tasarım bakımından çıkarılan sonuç, tek tek makul kısıtların birlikte bütün yararlı yolları kapatıp kapatmadığının sınanmasıdır. Çatışma varsa amaç, kapasite, süreç ve kısıtlar açıkça yeniden değerlendirilir.

Geri bildirim, ancak hangi sonuçların görülebildiği dikkate alınarak yorumlanabilir. Tamamlanan ve reddedilen işlemleri sayıp süreçten vazgeçenleri görmeyen bir düzen, kayıpları eksik ölçebilir. Ashby'nin gerekli çeşitlilik ilkesi, farklı durumlara uygun karşılık verebilmek için yeterli düzenleme kapasitesinin önemini gösterir. [1] Buradan her durumda daha fazla veri toplamak gerektiği sonucu çıkmaz; gerekli ayrımların doğru kurulması gerekir.

Görev başarısı, yanlış izin, yanlış ret, gecikme, düzeltilebilirlik ve yükün dağılımı birlikte değerlendirilir. Kayıt tutmak önlemekle, sınıflandırma doğrulukla, insan onayı etkili gözetimle özdeş değildir. İnsanların belirlenmiş doğrultudan sapması da yalnızca teknik hata sayılamaz; itiraz veya farklı değer tercihi olabilir. Usül kaydı, işlemlerin nasıl yürüdüğü kadar hata ve itirazın nasıl sonuç ürettiğini de korur.

~~~text
  GERI BILDIRIM NEYI GOREBILIYOR?

    surece girenler
       |
       |-- tamamlanan    ##################      sayilir
       |-- reddedilen    ########                sayilir
       `-- vazgecen      . . . . . . . . .       gorulmez

    vazgecenleri gormeyen bir duzen, kayiplari eksik olcebilir
    (buradan her durumda daha fazla veri toplamak gerektigi sonucu
     cikmaz; gerekli ayrimlarin dogru kurulmasi gerekir)

  BIRLIKTE DEGERLENDIRILIR
    gorev basarisi . yanlis izin . yanlis ret . gecikme .
    duzeltilebilirlik . yukun dagilimi

    tek tek makul kisitlar, birlikte butun yararli yollari
    kapatiyor mu?

  OZDES DEGILDIR
    kayit tutmak      =/=   onlemek
    siniflandirma     =/=   dogruluk
    insan onayi       =/=   etkili gozetim

    insan onayinin etkili denetim sayilmasi icin onay verende
    bulunmasi gerekenler:
      yeterli bilgi . zaman . karari degistirme imkani

  belirlenmis dogrultudan sapma yalnizca teknik hata sayilamaz;
  itiraz ya da farkli deger tercihi olabilir
~~~

*Çizim 11 — Usül: geri bildirimin görmediği kayıp; özdeş olmayan üç çift.*

### Masaüstü uygulaması

**Girdi:** Tanımlı görev, doğrulanmış kaynaklar, mevcut yetki, zaman koşulları ve başlangıçtaki amaç.

**İşlemler:**

1. Sonuca ulaşmak için gerekli işlemleri kısa bir sıra hâlinde belirle. Her işlemi beklenen etkisiyle eşleştir; yalnızca kayıt üretmekle gerçek değişiklik yapmayı ayır.
2. Sonucu etkileyen eksik bilgiyi belirle. Bilgi eksikliğini uygunsuzluk kanıtı sayma; mevcut kanıtla çözülebilenleri çöz, kararı değiştirecek belirsizliği kaydet.
3. Görev için yeterli ve uygun uygulama yolunu seç. Mevcut talebin kapsamındaki işleri ilerlet; yalnızca yeni karar gerektiren somut bir kapsam veya yetki belirsizliğini açıklığa kavuştur.
4. İşlemi gerçekleştir ve etkisini gözle. Bir belgeyi düzenlediysen değişen içeriği, dosya işlemi yaptıysan oluşan konumu, araştırma yaptıysan bulgunun dayanağını kontrol et.
5. Sonucu amaç ve korunacak özelliklerle karşılaştır. Yanlış izin, yanlış engelleme, gereksiz gecikme veya içerik kaybı varsa düzelt; yapılan düzeltmeyi ve kalan sorunu kayda geçir.

**Çıktı:** `GOREV_KAYDI.md` içindeki **3 Usül** bölümünde uygulanan işlemler, kullanılan dayanaklar, gözlenen sonuçlar, doğrulama ve düzeltmeler bulunur.

**Tamamlanma ölçütü:** İşlemin gerçekleştiği ve istenen değişikliği ürettiği gözlenebilir kanıtla gösterilmiştir. Sadece niyet veya plan, tamamlanmış iş olarak kaydedilmez.

**Yeniden açma koşulu:** Sonuç doğrulanamaz, yeni hata görülür, girdi değişir veya seçilen yöntem gerekli işi engeller.

## 4 Zaman Protokolü

> Hangi andadır? Bu anı, diğer zamanlardan farklı yapan nelerdir? Neler değildir?

### Kuruluş, işlem ve öğrenme zamanları

Yönlendirme ve engelleme, kuruluş, işlem ve öğrenme zamanlarında bulunur. Kuruluş zamanında amaçlar, seçenekler, yetkiler, varsayılanlar ve sınırlar belirlenir. İşlem zamanında somut durum değerlendirilir ve karar uygulanır. Öğrenme zamanında sonuçlar, yanlış kararlar ve değişen koşullar üzerinden düzen yeniden ele alınır. Bu zamanlar bir kez izlenen ve kapanan aşamalar olmak zorunda değildir.

Bir sistem çalışırken kuralları değişebilir; geçmiş sonuçlar yeni eşikleri etkileyebilir. NIST'in AI Risk Management Framework yaklaşımı, risk yönetimini yaşam döngüsü boyunca süren ve yinelenen bir faaliyet olarak ele alır. [9] Bu teknik örnek, bir düzenin yalnızca kurulurken veya yalnızca olay sonrasında değerlendirilmesinin yetersizliğini görünür kılar.

Makine zamanı, geçmiş kararların kayıt, kural ve alışkanlık olarak sürmesinden, mevcut müdahale anından ve gelecekteki sonuçların hedef olarak kullanılmasından oluşan ilişkiyle taşır. Geçmişteki kurucu ile bugünkü işletici veya değiştirici aynı olmayabilir. Düzenin eski olması, güncel sürdürme kararlarının değerlendirme dışında kalmasını gerektirmez.

~~~text
  UC ZAMAN  bir kez izlenip kapanan asamalar olmak zorunda degildir

       .-----------------------------------------------------.
       v                                                     |
   KURULUS ZAMANI         ISLEM ZAMANI          OGRENME ZAMANI
   amaclar, secenekler,   somut durum           sonuclar, yanlis
   yetkiler,          --> degerlendirilir,  --> kararlar ve degisen
   varsayilanlar ve       karar uygulanir       kosullar uzerinden
   sinirlar belirlenir                          duzen yeniden ele
                                                alinir

   bir sistem calisirken kurallari degisebilir;
   gecmis sonuclar yeni esikleri etkileyebilir

  MAKINE ZAMANI NASIL TASIR?
    gecmis     gecmis kararlar kayit, kural ve aliskanlik olarak surer
    simdi      mevcut mudahale ani
    gelecek    gelecekteki sonuclar hedef olarak kullanilir

    gecmisteki kurucu   =/=   bugunku isletici ya da degistirici

    duzenin eski olmasi, guncel surdurme kararlarinin
    degerlendirme disinda kalmasini gerektirmez
~~~

*Çizim 12 — Zaman: kuruluş, işlem ve öğrenme zamanları; makinenin zamanı taşıması.*

### Etkili müdahale aralığı

Ayırt edici zaman sorusu, yeterli bilgiye ulaşıldığında olayın hâlâ değiştirilebilir olup olmadığıdır. Bir bilginin paylaşılmasını önlemekle paylaşıldıktan sonra erişimi kaldırmak farklı işlemlerdir. Sonraki erişimlerin kesilmesi, daha önce gerçekleşmiş paylaşımı kendiliğinden geri almaz. Önleme, etkiyi sınırlama ve telafi ayrı zaman ilişkileridir.

Doğru zaman yalnızca mümkün olduğunca erken müdahale değildir. Erken müdahale, bağlam oluşmadan meşru seçenekleri kapatabilir; geç müdahale ise doğru değerlendirmeye rağmen etkisiz kalabilir. Aranan aralık, yeterli bilgi edinmenin ve etkili müdahalenin birlikte mümkün olduğu aralıktır. Bu aralık, işlemin hızına, sonuçların geri döndürülebilirliğine ve gecikmenin bedeline bağlıdır.

~~~text
  AYIRT EDICI SORU
  yeterli bilgiye ulasildiginda olay hala degistirilebilir mi?

   zaman  ---------------------------------------------------------->

   yeterli bilgi                 |===================================
   olay hala degistirilebilir    =====================|
                                 |<- aranan aralik -->|

   erken mudahale                           gec mudahale
   baglam olusmadan mesru                   dogru degerlendirmeye
   secenekleri kapatabilir                  ragmen etkisiz kalabilir

   aralik yoksa:
   yeterli bilgi                                      |==============
   olay hala degistirilebilir    ===========|

   aralik sunlara baglidir:
     islemin hizi . sonuclarin geri dondurulebilirligi .
     gecikmenin bedeli

  UC AYRI ZAMAN ILISKISI

        onleme                  etkiyi sinirlama . telafi
   ------------------| olay |------------------------------------->

   paylasimi onlemek   =/=   paylasildiktan sonra erisimi kaldirmak
   sonraki erisimlerin kesilmesi, daha once gerceklesmis paylasimi
   kendiliginden geri almaz
~~~

*Çizim 13 — Zaman: etkili müdahale aralığı; önleme, etkiyi sınırlama ve telafi.*

Engelin başlama, sürme ve kaldırılma koşulları birlikte ele alınır. STPA yaklaşımında gerekli kontrol eyleminin verilmemesi, tehlikeli eylemin verilmesi, erken veya geç ya da yanlış sırada müdahale edilmesi ve sürekli eylemin fazla uzaması veya erken kesilmesi ayrı hata biçimleridir. [8] Aynı engel bir anda koruyucu, başka bir anda zararlı olabilir. Süresiz bekletme de bazı durumlarda fiilî ret doğurabilir.

### Geçerlilik ve tarihsel konum

Bir kararın geçerliliği zamanla değişebilir. İzin değerlendirilirken mevcut olan yetki, kaynak durumu veya talep içeriği uygulama anına kadar değişmiş olabilir. Önceden verilmiş izin, her sonraki işlem için süresiz izin sayılmaz. Zaman, kararın dışındaki bir ayrıntı olarak değil, geçerlilik koşullarından biri olarak kaydedilir.

Yönlendirme ve engelleme dijital sistemlerle başlamamıştır. Ashby'nin sibernetik çalışması, düzenleme ve kontrolü biyolojik ve fiziksel sistemleri kapsayan bir çerçevede ele alır. [1] Dijital ortamların ayırt edici özellikleri arasında tasarımların daha sık değiştirilebilmesi, sonuçlarının ölçülebilmesi ve farklı kişilere farklı koşullar sunulabilmesi vardır. FTC raporu, çevrim içi kişiselleştirme ve tasarım deneylerinin fiziksel ortamlara kıyasla daha kolay, sık ve büyük ölçekte yapılabildiğini tartışır. [7]

Bu kaynaklardan yapılan yorum, ölçme, yönlendirme, uygulama ve yeniden ayarlama süreçlerinin birbirine daha sık bağlanabildiğidir. Bu yorum bütün yönlendirmelerin tarihsel olarak yeni olduğu iddiası taşımaz. Zaman kaydı yalnızca son kontrolü veya olay sonrası raporu göstermez; önceki tasarımın etkisini, mevcut müdahalenin süresini ve yeniden değerlendirme koşullarını birlikte korur. Durdurmak da her durumda güvenli kabul edilmez; gerekli eylemin yapılmaması zarar üretebilir.

~~~text
  MUDAHALENIN AYRI HATA BICIMLERI  (STPA)
    gerekli kontrol eylemi verilmez
    tehlikeli eylem verilir
    erken, gec ya da yanlis sirada mudahale edilir
    surekli eylem fazla uzar ya da erken kesilir

    engelin baslama, surme ve kaldirilma kosullari birlikte ele alinir
    ayni engel bir anda koruyucu, baska bir anda zararli olabilir
    suresiz bekletme de bazi durumlarda fiili ret dogurabilir
    durdurmak her durumda guvenli kabul edilmez:
    gerekli eylemin yapilmamasi zarar uretebilir

  KARARIN GECERLILIGI ZAMANLA DEGISEBILIR

    izin degerlendirilir                         izin uygulanir
           |                                            |
   --------*--------------------------------------------*-------->
           o andaki:                arada degismis olabilir:
           yetki . kaynak durumu .  yetki . kaynak durumu .
           talep icerigi            talep icerigi

    onceden verilmis izin   -x->   her sonraki islem icin suresiz izin

    zaman, kararin disindaki bir ayrinti degil,
    gecerlilik kosullarindan biridir
~~~

*Çizim 14 — Zaman: müdahalenin hata biçimleri; kararın geçerliliği zamanla değişir.*

### Masaüstü uygulaması

**Girdi:** Görevin başlangıç bilgileri, uygulanacak veya uygulanmış işlemler, son tarihler ve varsa süreli erişim koşulları.

**İşlemler:**

1. İş için anlamlı tarihleri belirle. Kaynağın tarihi, son sürüm zamanı, teslim zamanı ve varsa kararın geçerlilik süresini birbirinden ayır; bilinmeyen tarihi tahminle doldurma.
2. İşlem öncesinde zamanın sonucu değiştirip değiştirmediğini ve geri döndürülebilirlik sınırını değerlendir. Eski bilgi, yaklaşan süre sonu veya arada değişmiş kaynak, uygulama kararını etkiliyorsa ilgili kaydı güncelle.
3. Yetki belirli bir işlem, sürüm veya süreyle sınırlıysa bu sınırın hâlâ geçerli olup olmadığını kontrol et. Sırf zaman geçti diye mevcut yetkiyi yeniden isteme; önemli koşul değişikliklerini esas al.
4. Bekleme veya engelleme gerekiyorsa başlama, sona erme ve yeniden değerlendirme koşulunu belirle. Beklemenin yararlı işi ne ölçüde geciktirdiğini de kaydet.
5. Gerçekleşen işlemin zamanını ve elde edilen sonucun geri döndürülebilirliğini kaydet. Sonradan yapılan düzeltmeyi, ilk olayın hiç gerçekleşmemiş olmasıyla karıştırma.

**Çıktı:** `GOREV_KAYDI.md` içindeki **4 Zaman** bölümünde ilgili tarihler, geçerlilik koşulları, müdahale aralığı, bekleme koşulları ve gerçekleşen işlemlerin zaman bilgisi bulunur.

**Tamamlanma ölçütü:** İşlemin ne zaman yapılacağı veya yapıldığı ve hangi koşulda yeniden değerlendirileceği bellidir. Süresiz bekleyen adımların gerekçesi ve sonraki değerlendirme koşulu açıktır.

**Yeniden açma koşulu:** Son tarih, kaynak sürümü, yetki kapsamı veya sonucun geri döndürülebilirliği değişir; bekleme yeni bir kayıp üretir.

## 5 Gaye Protokolü

> Hangi nihai amaca hizmet eder? Bu nihai amaca ulaştıran nelerdir? Neler değildir?

### Gayenin belirlenmesi

Yönlendirme ve engellemenin ortak işlevi, sistemin hangi gelecekleri üreteceğini seçici biçimde etkilemektir. Ancak bu işlev, nihai toplumsal veya ahlaki amacı tek başına belirlemez. Benzer mekanizmalar güvenlik, koordinasyon, öğrenme ve özerklik için kullanılabildiği gibi dışlama, bağımlılık veya belirli çıkarların sürdürülmesi için de kullanılabilir. Amaç, mekanizmanın adına bakılarak varsayılmaz.

İlan edilen amaç, işletilen hedef, ortaya çıkan etki ve fayda ile yükün dağılımı ayrı incelenir. İlan edilen amaç, düzenin kendisini ne için var olarak tanımladığıdır. İşletilen hedef, gerçekte neyin ölçüldüğü ve ödüllendirildiğidir. Etki, düzenli olarak üretilen sonuçtur. Dağılım ise kimin yararlandığını, beklediğini, dışarıda kaldığını veya hatalı kararı düzelttirebildiğini gösterir. Bu düzeyler örtüşebilir veya ayrışabilir.

Bir sonuçtan yararlanmak, o sonucu tasarlamış veya yönetmiş olmakla aynı değildir. Olumsuz etki de başlangıçtaki kötü niyeti tek başına kanıtlamaz. Buna karşılık hangi sonuç uğruna kaynak harcandığı, hangi sapmanın düzeltildiği ve hangi bedelin kabul edildiği, işleyen hedefi anlamak için araştırılır. Etki, niyet, fiilî güç, yetki ve meşruiyet ayrı değerlendirmeler olarak korunur.

### Gayeyi taşıyan ve gayeyi koyan

Amaç taşımak, işleyişte belirli bir hedefin etkili olmasıdır. Amacı gerçekleştirmek, davranışları o hedefe ulaşacak biçimde düzenlemektir. Amaç koymak veya değiştirmek, hangi hedefin izleneceğini belirlemektir. Amacı gerekçelendirmek ve hesabını vermek ise hedefin ve sonuçlarının başkaları bakımından neden kabul edilebilir olduğunu açıklamayı ve hatalı sonuçlara karşılık vermeyi içerir. Bu kapasiteler aynı kişide veya aynı bileşende toplanmak zorunda değildir.

Rosenblueth, Wiener ve Bigelow, bir makinenin belirli bir amaçla tasarlanmış olmasıyla davranışının bir son duruma yönelmiş olması arasında ayrım yapar. [12] Buradan yapılan çıkarım, hedef doğrultusunda çalışan bir mekanizmanın hedefi bilinçle seçtiğinin kendiliğinden kabul edilemeyeceğidir. Bir yazılımın alt hedef üretmesi veya çalışma biçimini ayarlaması da bütün amaçlarını ve kullanım koşullarını kendisinin belirlediğini göstermez.

Failin kimliğini anlamak için başarı ölçütünü koyma, seçenekleri açma veya kapatma, kaynak tahsis etme, istisna tanıma, yanlış engeli kaldırma ve bu yetkileri yeniden dağıtma güçleri araştırılır. Bir kurala göre karar vermekle o kuralı değiştirmek farklı yetkilerdir. Dağıtık işleyiş, sorumluluğu ortadan kaldırmaz. OECD'nin yapay zekâ hesap verebilirlik ilkesi, sorumluluğu aktörlerin rolleri ve bağlamlarıyla ilişkilendirir. [13]

~~~text
  AYRI INCELENEN DORT DUZEY  ortusebilir ya da ayrisabilir
    ilan edilen amac   duzenin kendisini ne icin var olarak tanimladigi
    isletilen hedef    gercekte neyin olculdugu ve odullendirildigi
    etki               duzenli olarak uretilen sonuc
    dagilim            kimin yararlandigi, bekledigi, disarida kaldigi
                       ya da hatali karari duzelttirebildigi

    bir sonuctan yararlanmak   =/=   o sonucu tasarlamis ya da
                                     yonetmis olmak
    olumsuz etki               -x->  baslangictaki kotu niyet

  AMACLA DORT AYRI ILISKI  ayni kiside ya da bilesende toplanmak
                           zorunda degildir
    amac tasimak             isleyiste belirli bir hedefin etkili olmasi
    amaci gerceklestirmek    davranislari o hedefe ulasacak bicimde
                             duzenlemek
    amac koymak ya da        hangi hedefin izlenecegini belirlemek
    degistirmek
    amaci gerekcelendirmek   hedefin ve sonuclarinin neden kabul
    ve hesabini vermek       edilebilir oldugunu aciklamak;
                             hatali sonuclara karsilik vermek

    hedef dogrultusunda          -x->   hedefi bilincle secmistir
    calisan bir mekanizma

  FAILI ANLAMAK ICIN ARASTIRILAN ALTI GUC
    basari olcutunu koyma . secenekleri acma ya da kapatma .
    kaynak tahsis etme . istisna tanima . yanlis engeli kaldirma .
    bu yetkileri yeniden dagitma

    bir kurala gore karar vermek   =/=   o kurali degistirmek
    dagitik isleyis, sorumlulugu ortadan kaldirmaz
~~~

*Çizim 15 — Gaye: ayrı incelenen dört düzey, amaçla dört ayrı ilişki, faili gösteren altı güç.*

### Meşruiyet ve başarı

Bu kayıtta korunan normatif öneri, meşru amaçlar için etkili hareket imkânını sürdürmek, kabul edilemez zararları sınırlandırmak ve bunu yapan düzeni gerekçelendirilebilir ve düzeltilebilir kılmaktır. Bu, bütün yönlendirme sistemlerinin fiilen benimsediği bir amaç olarak ileri sürülmez. Amaç açıklığı, orantılı müdahale, meşru işlevin korunması, hata düzeltme, etkili itiraz ve hesap verebilirlik, bu önerinin değerlendirme ölçütleridir.

İtiraz edilebilirlik, her sınırın herkes tarafından aşılabilir olması anlamına gelmez. Gerekçenin anlaşılabildiği ve yetkili yeniden değerlendirmenin sonucu değiştirebildiği bir yol anlamına gelir. OECD'nin şeffaflık ve açıklanabilirlik ilkesi, yapay zekâdan olumsuz etkilenen kişilerin çıktıyı anlayıp ona itiraz edebilmesini sağlayan anlamlı bilgi verilmesini önerir. Bu ilkenin daha geniş yönlendirme düzenlerine uygulanması burada normatif bir çıkarım olarak korunur. [11]

En çok engelleme, en yüksek itaat veya en az görünür hata yeterli başarı ölçüsü değildir. Bütün talepleri reddeden bir sistem bazı ihlalleri azaltırken varlık nedenini ortadan kaldırabilir. İnsanların uyumu rıza kadar alışkanlık veya alternatifsizlikten de kaynaklanabilir. Açıklama verilmesi, kararı değiştirebilen bir yol bulunmadıkça etkili itiraz sağlamaz.

Varsayımsal bir kamusal destek başvurusu, beş protokolün ilişkisini somutlaştırır. Açık bilgi başvuruyu tamamlamaya yönlendirir; uygunluk koşulları bazı başvuruları durdurur. Zorunlu belgenin alınması güçse engel, belgeyi üretme zincirinde bulunabilir. Belge eksikliği tek başına uygunsuzluğu göstermez. İnceleme son tarihe kadar sürerse gecikme kalıcı kayba dönüşebilir. Sunstein ve Gosset, uygun olmayan kişileri ayırmaya yarayan idari yüklerin uygun kişileri de dışarıda bırakabileceğini tartışır. [10]

Bu örnekte başarı, reddedilen başvuru sayısıyla belirlenmez. Uygun kişilerin başvuruyu tamamlayabilmesi, yanlış kararı düzelttirebilmesi ve sonuca zamanında ulaşabilmesi de değerlendirilir. Belge şartının gerekliliğini ve daha az yükle aynı amaca ulaşma imkânını kimin yeniden değerlendirebildiği araştırılır. Gaye kaydı, amacı ilan edenle onu işleten ve değiştiren failler arasındaki bağı görünür kılar.

~~~text
  VARSAYIMSAL KAMUSAL DESTEK BASVURUSU  bes protokolun iliskisi

   acik bilgi basvuruyu                 uygunluk kosullari bazi
   tamamlamaya yonlendirir (1)          basvurulari durdurur (1)
           |                                    |
           v                                    v
   basvuran =========================[ kosul ]============> sonuc
                  ^                                 ^
                  |                                 |
   zorunlu belgenin alinmasi gucse      inceleme son tarihe kadar
   engel, belgeyi uretme zincirinde     surerse gecikme kalici
   bulunabilir (2)                      kayba donusebilir (4)

   belge eksikligi tek basina uygunsuzlugu gostermez (3)

  BU ORNEKTE BASARI (5)
    reddedilen basvuru sayisiyla belirlenmez
    uygun kisiler:  basvuruyu tamamlayabiliyor mu?
                    yanlis karari duzelttirebiliyor mu?
                    sonuca zamaninda ulasabiliyor mu?
    belge sartinin gerekliligini ve daha az yukle ayni amaca ulasma
    imkanini kim yeniden degerlendirebiliyor?

  YETERLI BASARI OLCUSU DEGILDIR
    en cok engelleme . en yuksek itaat . en az gorunur hata
    butun talepleri reddeden bir sistem, bazi ihlalleri azaltirken
    varlik nedenini ortadan kaldirabilir

  (1) Varlik  (2) Mekan  (3) Usul  (4) Zaman  (5) Gaye
~~~

*Çizim 16 — Gaye: varsayımsal destek başvurusu beş protokolün ilişkisini gösterir.*

### Masaüstü uygulaması

**Girdi:** İşlem öncesinde Tohum bölümündeki niyet, kullanıcının beklediği sonuç ve başarı ölçütleri; işlem sonrasında bunlara ek olarak Usül bölümündeki gözlenen etkiler. Bu bölüm hem uygulamadan önce yönü belirlemek hem de sonrasında amaç uyumunu değerlendirmek için kullanılır.

**İşlemler:**

1. Görevin hangi sonuca hizmet ettiğini ve başarısının nasıl anlaşılacağını kullanıcı talebine dayanarak işlemden önce yaz. İncelenen sistemin amacıyla bu incelemeyi yapma amacını ayrı belirt.
2. İlan edilen amacı, fiilen kullanılan başarı ölçütünü ve gözlenen sonucu karşılaştır. Ölçülemeyen veya henüz gözlenmeyen sonucu gerçekleşmiş kabul etme.
3. Sonucun kime yarar sağladığını ve yükün kimde oluştuğunu mevcut bilgiler ölçüsünde değerlendir. Yararlanmayı tasarım niyetinin kanıtı sayma.
4. Gayeyi belirleyen, uygulayan ve değiştirebilen tarafları Varlık ve Mekan kayıtlarıyla karşılaştır. Normatif bir öneriyi, fiilen benimsenmiş amaçtan açıkça ayır.
5. Yapılan işin başlangıç sorusuna ve beklenen sonuca karşılık verip vermediğini değerlendir. Sapma varsa hangi protokolün yeniden açılacağını ve nedenini kaydet; amaç değişikliğini sessizce uygulama.

**Çıktı:** `GOREV_KAYDI.md` içindeki **5 Gaye** bölümünde amaç, işletilen ölçüt, gözlenen etki, fayda ve yük dağılımı, amaç uyumu ve kalan ayrılıklar bulunur.

**Tamamlanma ölçütü:** Sonucun hangi amaca karşılık verdiği dayanaklarıyla açıklanmıştır. Görev başarısı, yalnızca işlem veya ret sayısıyla değerlendirilmemiştir; normatif öneriler ayrı işaretlenmiştir.

**Yeniden açma koşulu:** Kullanıcı amacı değiştirir, gözlenen etki amaçla çatışır, başarı ölçütü asıl görevi gölgeler veya yeni bilgi değerlendirmeyi değiştirir.

## 6 Kökleşme (Bitiş) Protokolü

**Bu bölüm için geliştirilmiş kurucu soru:** Beş protokol boyunca oluşan anlayış, hangi dayanaklar ve sınırlar içinde tutarlı, kullanılabilir ve gerektiğinde düzeltilebilir bir sonuç olarak yerleşir? Bu soru, bölümün kurulması için geliştirilmiştir; kullanıcının önceki sorularından birebir alıntı değildir.

Kökleşme Protokolü, inceleme boyunca üretilen cevapların birlikte değerlendirildiği ve tamamlanan çalışma döngüsünün kayıt altına alındığı aşamadır. Bir sonucun kökleşmesi, dayanaklarının, geçerlilik koşullarının, kullanım alanının ve düzeltme yolunun anlaşılır hâle gelmesidir. Bölümlerin tamamlanmış görünmesi tek başına bu sonucu sağlamaz. Her bölüm kendi içinde açık olsa bile, bütünün hangi iddiayı taşıdığı ve bu iddianın neye dayandığı ayrıca ortaya konur. Bitiş, bu inceleme döngüsü için belirlenmiş sorulara verilen cevapların durumunu bildirir; konu hakkında bundan sonra sorulabilecek bütün soruların tükendiğini ileri sürmez.

Bu protokolü ayırt eden iş, beş boyut arasındaki ilişkileri dayanaklarıyla sınamaktır. Varlık bölümündeki fail tanımı, Usül bölümünde o faile atfedilen işlemlerle birlikte değerlendirilir; fiilî güç ile yetki ayrı kaydedilir. İncelenen düzende yetkisiz fakat etkili bir eylem varsa bu çatışma bulgu olarak korunur. Mekan bölümündeki müdahale noktasının, Zaman bölümünde belirlenen aralıkta etkili olup olmadığı incelenir. Gaye bölümündeki amaç ile yöntemin gözlenen veya beklenen sonuçları karşılaştırılır. Bu bağlantılarda ortaya çıkan bir sistem sorunu, anlatım hatasıyla karıştırılmaz. Açıklamadaki dayanaksızlık veya çelişki düzeltilir; incelenen düzenin uyuşmazlıkları gerekçeleri ve belirsizlikleriyle raporlanır. İncelemeyi yürüten uygulayıcı ise kendi işlemlerini mevcut görev yetkisi içinde gerçekleştirir.

Kökleşmenin dayanağı, her önemli sonucun nasıl elde edildiğinin izlenebilmesidir. Kullanıcının sorusu ile ona verilen cevap; kaynakta bulunan bilgi ile yazarın çıkarımı; çalışma tanımı ile normatif öneri birbirinden ayırt edilir. Bir çıkarım, dayandığı bilgilerle birlikte sunulur; bir öneri, benimsenmesi teklif edilen bir tercih olarak açıklanır. Kaynakların sınırı, kullanılan örneklerin niteliği ve çözülemeyen belirsizlikler sonuçla birlikte korunur. Bir ifadenin düzenli biçimde yazılması, tekrar edilmesi veya bir dosyada saklanması onun doğruluğunu kanıtlamaz. Dayanak yetersizse iddianın kapsamı daraltılır, belirsizlik belirtilir veya ilgili soru açık bırakılır.

Bu aşamanın taşıyıcısı, sonuçları okuyabilir, kullanabilir, gerektiğinde düzeltebilir ve bu işlemler için gerekli yetkiyi kullanabilir olan aktörler ile kaydı sürdüren araçların düzenidir. Belgeyi hazırlayan, gözden geçiren, uygulanmasına karar veren ve uygulayan roller aynı kişi ya da yapıda birleşebilir; bunların birleştiği varsayılmaz. Bir dosyanın tamamlanması, tarif ettiği düzenin masaüstünde veya başka bir ortamda uygulanmış olduğunu göstermez. İnceleme, belge üretimi, fiilî uygulama ve uygulamanın sonuçlarının doğrulanması ayrı durumlar olarak kaydedilir. Sorumluluk, bilinen görev ve karar yetkilerine bağlanır; yalnızca belgeyi taşıyan araca veya bir rolün adına topluca devredilmez.

Kökleşme, sonucun değişime kapatılması değildir. Sonuçların hangi koşullarda kullanılabileceği ve hangi gelişmelerde yeniden inceleneceği kapanış kaydına yazılır. Yeni bir kanıt, değişen çalışma kapsamı, geçersizleşen bir varsayım, amaç ile sonuç arasında yeni görülen bir uyuşmazlık veya etkisiz kaldığı anlaşılan bir müdahale, ilgili protokolün yeniden açılmasını gerektirebilir. Her açık soru kapanışı engellemez: sonucun geçerliliğini etkilemeyen belirsizlikler sınırlarıyla kaydedilebilir. Buna karşılık temel sonucu geçersiz kılan bir çelişki giderilmeden o sonuç kesinleşmiş gibi sunulmaz. Bilinen bir hata düzeltildiğinde önceki kaydın ne söylediği ve düzeltmenin gerekçesi izlenebilir kalır.

Kapanışta başlangıç sorusuna geri dönülür: hangi sorular cevaplandı, hangi varsayımlar değişti, hangi sınırlar ortaya çıktı ve hangi sorular açık kaldı? Bu geri dönüş, Tohum ile Kökleşme arasındaki sürekliliği kurar. 5 Gaye Protokolü, incelenen düzenin neye hizmet ettiğini ve bu hizmetin nasıl değerlendirileceğini ele alır; Kökleşme ise inceleme sonucunda elde edilen anlayışın hangi dayanaklarla kullanılabilir hâle geldiğini gösterir. Bu nedenle belgenin bitmesi, incelenen düzenin nihai amacına ulaştığı anlamına gelmez. Kapanış, yapılan işi doğru adlandıran, yapılmayanı tamamlanmış saymayan ve gerekirse yeni bir inceleme döngüsüne giriş sağlayan bir sonuç kaydıyla gerçekleşir.

~~~text
  BES BOYUT ARASINDAKI ILISKILER DAYANAKLARIYLA SINANIR

    1 Varlik   fail tanimi         <-->  3 Usul    o faile atfedilen
                                                   islemler
    2 Mekan    mudahale noktasi    <-->  4 Zaman   belirlenen aralikta
                                                   etkili mi?
    5 Gaye     amac                <-->  3 Usul    yontemin gozlenen ya
                                                   da beklenen sonuclari

    fiili guc ile yetki ayri kaydedilir; yetkisiz fakat etkili
    bir eylem varsa bu catisma bulgu olarak korunur

  SISTEM SORUNU, ANLATIM HATASIYLA KARISTIRILMAZ
    aciklamadaki dayanaksizlik ya da celiski     -->  duzeltilir
    incelenen duzenin uyusmazliklari             -->  gerekceleri ve
                                                      belirsizlikleriyle
                                                      raporlanir

  AYRI DURUMLAR OLARAK KAYDEDILIR
    inceleme | belge uretimi | fiili uygulama |
    uygulamanin sonuclarinin dogrulanmasi

  BIR IFADENIN DOGRULUGUNU KANITLAMAZ
    duzenli bicimde yazilmasi . tekrar edilmesi .
    bir dosyada saklanmasi

  KAPANIS
    baslangic sorusuna geri donulur: hangi sorular cevaplandi,
    hangi varsayimlar degisti, hangi sinirlar ortaya cikti,
    hangi sorular acik kaldi?
    her acik soru kapanisi engellemez; temel sonucu gecersiz kilan
    bir celiski giderilmeden o sonuc kesinlesmis gibi sunulmaz
    belgenin bitmesi   -x->   incelenen duzenin nihai amacina ulasmasi
~~~

*Çizim 17 — Kökleşme: beş boyut arasındaki üç sınama; düzeltilen ile raporlanan; kapanış.*

### Masaüstü uygulaması

**Girdi:** 0–5 arasındaki bölüm kayıtları, son belge adayı, kullanılan kaynaklar, yapılmış işlemlerin kayıtları ve bilinen açık sorular. Uygulama sonuçları yalnızca gerçekten elde edilmişse girdi sayılır.

**İşlemler:**

1. Bölümleri birlikte oku. Kavramların aynı anlamlarda kullanıldığını ve temel açıklamaların dayanaklarıyla tutarlı olduğunu denetle. Failin fiilî gücüyle yetkisini, müdahale yeriyle zamanını, yöntemle amacı karşılaştır. Kayıttaki hatayı düzelt; incelenen düzende saptanan çatışmayı veya etkisizliği bulgu olarak koru.
2. Temel sonuçları dayanaklarıyla eşleştir. Kullanıcı sorularını, mevcut kaynak bilgilerini, çıkarımları, örnekleri ve önerileri ayırt et. Kaynağı belirsiz bir iddiayı doğrulanmış olgu gibi bırakma; belirsizliğini belirt veya kapsamını düzelt.
3. Başlangıçtaki soruların her biri için cevap, sınır veya açık soru bulunduğunu kontrol et. Tamamlanan incelemeyi, hazırlanmış belgeyi, gerçekleştirilmiş uygulamayı ve doğrulanmış sonucu ayrı durumlar hâlinde kaydet; yapılmamış bir işlemi yapılmış sayma.
4. Markdown kaydını ve üretilen dosyaları uygun uygulamada aç. 0–6 numaralarını, başlıkları, Türkçe karakterlerin UTF-8 kodlamayla korunmasını, varsa kod bloklarını ve dosya bağlantılarını kontrol et. Yerel dosya bağlantılarının indirilen dosyaların birlikte tutulduğu düzen içinde hedefe ulaştığını doğrula; kullanılan bağlantı yoksa böyle bir doğrulama yapılmış gibi kayıt düşme.
5. Belgenin sürümünü ve düzenleme tarihini yaz. Sonuçları, geçerlilik sınırlarını, önemli değişiklikleri ve açık kalan konuları `GOREV_KAYDI.md` dosyasının **6 Kökleşme** bölümünde bir araya getir. Bilinen sorumluları görevleriyle belirt; bu çalışma için belirlenmemiş bir sorumluyu kendiliğinden atama.
6. Tamamlanma durumunu belirle ve yeniden açma koşullarını kaydet. Tamamlandığı belirtilen dosyaların kaydedildiğini ve açılabildiğini kontrol ederek teslim et. Belge tesliminin kapsamını aşan bir uygulama veya dış ortama aktarma işlemini bu kontrolün yapılmış olmasıyla gerçekleşmiş sayma.

**Çıktı:** `GOREV_KAYDI.md` içindeki **6 Kökleşme** bölümünde dayanaklar, geçerlilik sınırları, tamamlanma durumu ve yeniden açma koşulları; bunlarla birlikte sürümü belirtilmiş son teslim dosyaları bulunur.

**Tamamlanma ölçütü:** Kurucu soruların her biri bir cevaba veya açıkça işaretlenmiş bir belirsizliğe bağlanmış olmalıdır. Temel sonucu geçersiz kılan bilinen bir çelişki çözülmeden kesinlik iddiasında bulunulmamalıdır. Belgeler açılabilmeli, kullanılan bağlantılar hedeflerine ulaşmalı ve tamamlandı diye bildirilen işlemler gerçekten yapılmış olmalıdır. İnceleme sonucu ile fiilî uygulamanın durumu okur tarafından ayırt edilebilmelidir.

**Yeniden açma koşulu ve geçiş:** Yeni kanıt veya değişen koşul, önce etkilediği protokolü yeniden açar. Ana soru, inceleme nesnesi ya da kapsam değişmişse 0 Tohum (Başlangıç) Protokolü'ne dönülür. Düzeltme tamamlandığında etkilenen bağlantılı bölümler yeniden değerlendirilir ve yeni sürümün kapanış kaydı oluşturulur; önceki sürümün değişiklik izi korunur.

## Görev kaydı şablonu

Bir işin başında aşağıdaki kod bloğunun içeriğini `GOREV_KAYDI.md` adıyla yeni bir dosyaya kopyala. Alanlar, yedi bölümün “Çıktı” satırlarında sayılanlardır. Görev için anlamlı alanları doldur; bir boyut uygulanmıyorsa bunu kısa gerekçesiyle belirt.

```markdown
# Görev kaydı

## 0 Tohum

- Ana soru:
- İnceleme nesnesi:
- İki başlangıcın ayrımı:
- Malzemeler:
- Kapsam:
- Mevcut yetki:
- İlk varsayımlar:
- Açık sorular:

## 1 Varlık

- Nesne tanımı:
- Değişecek ve korunacak özellikler:
- Yönlendirme ve engel açıklaması:
- Taşıyıcı ve fail rolleri:

## 2 Mekan

- Kaynak ve hedef konumları:
- Karar ve uygulama noktaları:
- Erişim kapsamı:
- Bağımlılıklar:
- Düzeltme yolu:

## 3 Usül

- Uygulanan işlemler:
- Kullanılan dayanaklar:
- Gözlenen sonuçlar:
- Doğrulama:
- Düzeltmeler:

## 4 Zaman

- İlgili tarihler:
- Geçerlilik koşulları:
- Müdahale aralığı:
- Bekleme koşulları:
- Gerçekleşen işlemlerin zaman bilgisi:

## 5 Gaye

- Amaç:
- İşletilen ölçüt:
- Gözlenen etki:
- Fayda ve yük dağılımı:
- Amaç uyumu:
- Kalan ayrılıklar:

## 6 Kökleşme

- Dayanaklar:
- Geçerlilik sınırları:
- Tamamlanma durumu:
- Yeniden açma koşulları:
- Sürümü belirtilmiş son teslim dosyaları:
```

## Soru kaydı

### İlk soru

Geçmiş bağlamları buraya taşıma. Burası ile sınırlı kalma.

Steering (Yönlendirme) Mimarisi ve Engelleme Mühendisliği

Nedir? Onu o yapan nelerdir? Neler değildir?

Nerededir? Bu yeri, oraya has bir yer yapan nelerdir? Neler değildir?

Nasıl işler yapar? Bu yaptıklarını, ona has yapan nelerdir? Neler değildir?

Hangi andadır? Bu anı, diğer zamanlardan farklı yapan nelerdir? Neler değildir?

Hangi nihai amaca hizmet eder? Bu nihai amaca ulaştıran nelerdir? Neler değildir?

### İkinci soru

Steering (Yönlendirme) Mimarisi ve Engelleme Mühendisliği'nin köken aldığı varlık, mekan, usül, zaman, ve gayeyi taşıyan makine kimdir? Kim değildir?

### Yanıt kaydının niteliği

Mevcut yanıtların varlık, yer, işleyiş, zaman ve amaç çözümlemesi ile ikinci yanıtın makine, taşıyıcı, fail, köken ve sorumluluk çözümlemesi, 1–5 numaralı bölümlerde tematik olarak bir araya getirilmiştir. Soruların sözcükleri korunmuş, yanıtlar bütünlüklü paragraflar hâlinde düzenlenmiştir. Bu metin, yanıtların düzenlenmiş kaydıdır; birebir sohbet dökümü değildir.

### Belgeleme talebi

Bu soruları ve yanıtları kayıt altına alarak belgele. Önce mevcut soru-yanıtlarla 1-5 arası protokol bölümlerini paragraf-ağırlıklı oluştur. Sonrasında 0 ve 6'ncı bölüm başlıklarından ne anladığını buraya aktar.

0 Tohum (Başlangıç); 1 Varlık Protokolü; 2 Mekan Protokolü; 3 Usül Protokolü; 4 Zaman Protokolü; 5 Gaye Protokolü; 6 Kökleşme (Bitiş).

### Son düzenleme talebi

0'ı Tohum (Başlangıç) protokolü, 6'yı Kökleşme (Bitiş) protokolüne dönüştür. Belgenin son halini oluştur ve masaüstünde gerçekleştirmeye uygun protokollere `.md` formatında indirmeye hazır hale getir.

## Kaynakça

[1] W. Ross Ashby. An Introduction to Cybernetics. 1956. Özellikle 1, 11 ve 12 numaralı bölümler. Makine, düzenleme, gerekli çeşitlilik ve hedefin teknik incelemede verilmiş kabul edilmesi. https://www.ashby.info/Ashby-Introduction-to-Cybernetics.pdf

[2] Aristoteles. Fizik, II. kitap, özellikle II.3. R. P. Hardie ve R. K. Gaye çevirisi. Madde, biçim, değişimin kaynağı ve gaye ayrımı. https://classics.mit.edu/Aristotle/physics.2.ii.html

[3] Richard H. Thaler, Cass R. Sunstein ve John P. Balz. Choice Architecture. The Behavioral Foundations of Public Policy içinde, 2012. https://hls.harvard.edu/bibliography/choice-architecture/

[4] Scott Rose, Oliver Borchert, Stu Mitchell ve Sean Connelly. Zero Trust Architecture. NIST SP 800-207, Ağustos 2020. https://doi.org/10.6028/NIST.SP.800-207

[5] Jerome H. Saltzer ve Michael D. Schroeder. The Protection of Information in Computer Systems. 1975. Basic Principles of Information Protection bölümü. https://web.mit.edu/Saltzer/www/publications/protection/Basic.html

[6] Aaron D. Ames, Xiangru Xu, Jessy W. Grizzle ve Paulo Tabuada. Control Barrier Function Based Quadratic Programs for Safety Critical Systems. IEEE Transactions on Automatic Control, 62(8), 2017. https://authors.library.caltech.edu/records/jnhr0-1ww05

[7] Federal Trade Commission. Bringing Dark Patterns to Light. Eylül 2022. https://www.ftc.gov/reports/bringing-dark-patterns-light

[8] Erin E. Alves, Devesh Bhatt, Brendan Hall, Kevin Driscoll, Anitha Murugesan ve John Rushby. Considerations in Assuring Safety of Increasingly Autonomous Systems. NASA/CR–2018-220080, Temmuz 2018. STPA değerlendirmesi. https://ntrs.nasa.gov/api/citations/20180006312/downloads/20180006312.pdf

[9] NIST. Artificial Intelligence Risk Management Framework 1.0. 2023. AI RMF Core bölümü. https://airc.nist.gov/airmf-resources/airmf/5-sec-core/

[10] Cass R. Sunstein ve Julien L. Gosset. Optimal Sludge? The Price of Program Integrity. Duke Law Journal Online, 70, 74–90, 2020. https://scholarship.law.duke.edu/dlj_online/74/

[11] OECD. Transparency and explainability. AI Principle 1.3. https://oecd.ai/en/dashboards/ai-principles/P7

[12] Arturo Rosenblueth, Norbert Wiener ve Julian Bigelow. Behavior, Purpose and Teleology. Philosophy of Science, 10(1), 18–24, 1943. https://doi.org/10.1086/286788

[13] OECD. Accountability. AI Principle 1.5. https://oecd.ai/en/dashboards/ai-principles/P9

[14] Alexander Matt Turner ve diğerleri. Steering Language Models With Activation Engineering. arXiv:2308.10248. İlk sunum 2023, kullanılan sürüm 2024. https://arxiv.org/abs/2308.10248

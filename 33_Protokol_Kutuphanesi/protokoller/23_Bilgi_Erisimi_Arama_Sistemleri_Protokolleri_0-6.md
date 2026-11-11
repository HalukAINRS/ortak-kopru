# Bilgi Erişimi ve Arama Sistemleri Mühendisliği

**Yedi Protokol ve Masaüstü Uygulama Yönergeleri**

**Sürüm:** 1.0\
**Tarih:** 31 Ekim 2026\
**Kapsam:** Düzenlenmiş soru ve yanıt kaydı

Bu belge, Bilgi Erişimi ve Arama Sistemleri Mühendisliğine ilişkin soruları ve yanıtları 0–6 arasındaki yedi protokol altında bir araya getirir. Tohum başlangıç koşullarını kaydeder; Varlık, Mekan, Usül, Zaman ve Gaye alanı beş yönden açıklar; Kökleşme bu açıklamaları dayanakları ve sınırlarıyla bütünleştirir. Her protokolün açıklamasını, masaüstünde uygulanabilecek girdiler, adımlar, üretilecek kayıt ve tamamlanma koşulları izler.

Kaynak sorular kullanıcıya, açıklamalar ve kavramsal yorumlar ChatGPT'ye aittir. Başlangıçtaki kapsam talimatı “Geçmiş bağlamları buraya taşıma. Burası ile sınırlı kalma.” biçimindedir. 1–5 arasındaki özgün sorular korunmuştur. 0 ve 6'nın protokol soruları başlangıç ve bitiş protokolleri için yazılmıştır; özgün soruların alıntısı olarak sunulmaz.

Metnin temel açıklaması, alanın bilgi ihtiyacı ile uygun içerik arasında çalışan bir erişim ilişkisi kurduğudur. Bu ilişkiyi taşıyan “makine”, insanlar, kayıtlar, kurallar ve teknik araçların birlikte işlediği düzenek olarak yorumlanır. Bu adlandırma kavramsal bir öneridir. Tarihsel örnekler, teknik açıklamalar ve kavramsal çıkarımlar kendi kapsamları içinde değerlendirilir.

Masaüstü yönergelerinin varsayılan konusu, bu mühendislik alanının incelenmesi ve belgelenmesidir. Belirli bir ürün, kurum veya arama sistemi incelenecekse konu ve sağlanan girdiler Tohum kaydında belirtilir. Her yeni uygulama kendi çalışma kayıtlarını üretir. Belgenin hazırlanmış olması, bu uygulamanın yürütüldüğü veya bir yazılımın sınandığı anlamına gelmez.

## Ortak kaynak soru

> Bilgi Erişimi ve Arama Sistemleri Mühendisliği'nin; köken aldığı varlık, mekan, usül, zaman, ve gayeyi taşıyan makine kimdir? Kim değildir?

Bu ortak soru, 1–5 arasındaki protokollerde ilgili boyut üzerinden ele alınır. Tohum sorunun başlangıçtaki yerini, Kökleşme ise bu boyutları birlikte taşıyan düzeneğe ilişkin ulaşılan açıklamayı kaydeder.

## Masaüstünde çalışma düzeni

Çalışmayı bir kişi veya masaüstünde çalışan bir asistan yürütebilir. Çalışma başlarken benzersiz bir çalışma kimliği seçilir ve `calismalar/<calisma_kimligi>/` klasörü oluşturulur. Protokoller 0'dan 6'ya sırayla uygulanır. Protokol metni korunur; üretilen kayıtlar çalışma klasörüne yazılır. Birden çok çalışma ayrı kimliklerle saklanır.

Her kayıt çalışma kimliğini, konuyu, hazırlama tarihini, kullanılan girdileri, ilgili önceki kayıtları ve durumu içerir. Durum “taslak”, “eksik” veya “tamamlandı” olarak yazılır. Tamamlandı, bölümün belirtilen kapsamda gerekçeli olarak ele alındığını gösterir; bütün belirsizliklerin giderildiği anlamına gelmez. Sonucu belirlemek için zorunlu bir girdi eksikse kayıt eksik durumunda bırakılır ve eksikliğin etkisi açıklanır.

Kullanıcı ifadesi, kaynak bilgisi, kavramsal yorum, varsayımsal örnek ve yapılmış gözlem birbirinden ayırt edilir. Her kaynak adı veya adresi, neyi desteklediği ve varsa doğrulama tarihiyle kaydedilir. Kaynağa erişilemediğinde desteklediği iddia doğrulanmış sayılmaz. Belgenin düzenlenme tarihi, kaynakların yeniden doğrulandığı tarih yerine kullanılmaz.

Belgenin değerlendirme çerçevesi 31 Ekim 2026 tarihlidir. Sonraki bir uygulamada güncel durum hakkında sonuç üretilecekse değişebilen iddialar birincil kaynaklardan yeniden doğrulanır. Dış kaynaklara erişim yoksa tarihli açıklama korunur ve güncel durumun doğrulanamadığı belirtilir. Bilgisayardaki inceleme, Tohum'da belirlenen dosya ve kaynak kapsamı üzerinden yürütülür.

Yeni bir inceleme çevrimi önceki çalışma klasörünün üzerine yazılmaz. Aynı çevrimde bir kayıt değiştirildiğinde tarih, değişiklik ve gerekçe kaydedilir; etkilenen sonraki kayıtlar yeniden değerlendirilir. Gaye'de belirlenen amaç Usül'deki başarı koşulunu değiştirirse ilgili bölüme dönülür. Kökleşme, son durumda dosyaların ve açıklamaların birbiriyle uyumunu değerlendirir.

~~~text
  CALISMA KLASORU
    calismalar/
      <calisma_kimligi>/    her calisma ayri kimlikle; yeni inceleme
        kayitlar            cevrimi onceki klasorun uzerine yazilmaz
    talimat dosyalari korunur; uretilen kayitlar calisma klasorune
    her kayitta:  calisma kimligi . konu . hazirlama tarihi .
                  girdiler . ilgili onceki kayitlar . durum

  DURUM
    taslak  |  eksik  |  tamamlandi
    tamamlandi   bolum belirtilen kapsamda gerekceli olarak ele alindi
                 -/->  butun belirsizlikler giderildi
    eksik        sonucu belirlemek icin zorunlu bir girdi eksik;
                 eksikligin etkisi aciklanir

  AYIRT EDILIR
    kullanici ifadesi . kaynak bilgisi . kavramsal yorum . varsayimsal
    ornek . yapilmis gozlem
    kaynaga erisilemedi  -->  destekledigi iddia dogrulanmis sayilmaz
    belgenin duzenlenme tarihi  =/=  kaynaklarin dogrulandigi tarih

  DEGISIKLIK  ayni cevrimde
    tarih + degisiklik + gerekce  -->  etkilenen sonraki kayitlar
                                      yeniden degerlendirilir
    Gaye'deki amac Usul'deki basari kosulunu degistirirse  -->  ilgili
    bolume donulur
~~~

*Çizim 1 — Masaüstünde çalışma düzeni: çalışma klasörü; durum; ayırt edilenler; değişiklik.*

## 0 Tohum (Başlangıç) Protokolü

**Protokol sorusu:** Bu inceleme hangi soru veya ihtiyaçtan doğdu? Başlangıçta ne biliniyor, ne varsayılıyor ve neyin açıklığa kavuşturulması isteniyor?

### Başlangıcın kaydı

Tohum Protokolü, incelemeyi başlatan soruyu ve bu sorunun ele alınacağı başlangıç koşullarını kaydeder. İncelenen alanın varlığı, mekânı, usulü, zamanı ve gayesi ayrı ayrı açıklanmadan önce, araştırmanın hangi ihtiyaç veya belirsizlik etrafında kurulacağı belirlenir. Başlangıçta bilinenler, henüz doğrulanmamış kabuller ve yanıt bekleyen sorular birbirinden ayrılır. Böylece daha sonra ulaşılan sonuçların hangi başlangıçtan geliştiği görülebilir.

Bu çalışmanın kayıtlı başlangıcı, Bilgi Erişimi ve Arama Sistemleri Mühendisliğinin ne olduğunu, nerede konumlandığını, nasıl işler yaptığını, hangi zaman koşullarında bulunduğunu ve hangi amaca hizmet ettiğini sorgulamaktır. Ardından bu boyutları birlikte taşıyan “makine”nin kim olduğu ve kim olmadığı sorulmuştur. İncelemenin burada gözlenebilen yönelişi bu iki soru dizisidir. Kullanıcının ayrıca kişisel, kurumsal veya projeye özgü bir nedeni bulunduğu varsayılmaz; böyle bir açıklama ancak kendisi tarafından belirtilirse kayda eklenir.

Başlangıçtaki “Geçmiş bağlamları buraya taşıma. Burası ile sınırlı kalma.” talimatı çalışmanın kapsam koşuludur. İnceleme, bu konuşmada verilen sorular ve bunlarla doğrudan ilgili kaynaklar üzerinden yürütülür. Başka konuşmalardaki kullanıcı bilgileri açıklamanın dayanağı yapılmaz. Gereken tarihsel, kuramsal ve teknik kaynaklara başvurulması ise araştırma kapsamına dâhildir. Kullanıcının ifadesi, dış kaynağın sağladığı bilgi ve açıklamayı kuranın yorumu kayıt içinde ayırt edilebilir kalır.

### İncelemeyi yönlendiren koşullar

Başlangıç kaydı, konunun adını yazmakla tamamlanmaz. Hangi soruların yanıtlanacağı, hangi içeriklerin dayanak olarak kullanılabileceği, hangi tarih veya sürümün esas alındığı ve beklenen çıktının ne olduğu açıklanır. Mevcut görevde çıktı, yedi protokol altında düzenlenmiş ve masaüstünde yeniden uygulanabilecek bir belgedir. Erişilemeyen bir kaynak veya belirsiz kalan bir kavram varsa, bunlar açık mesele olarak kaydedilir.

Bu bölümün Varlık Protokolünden ayrıldığı nokta, incelediği ilişkidir. Varlık Protokolü, alanın ne olduğunu ve kimliğini hangi özelliklerin kurduğunu açıklar. Tohum Protokolü, o alanı incelemeye hangi sorularla ve kabullerle başlandığını kaydeder. Gaye Protokolü de alanın ve onu taşıyan düzeneğin hangi amaçlara hizmet ettiğini araştırır. Araştırmanın başlama nedeni ile araştırılan şeyin hizmet ettiği amaç birbiriyle ilişkili olabilir; yine de ayrı açıklanır.

“Makine” için önerilen insanlar, kayıtlar, kurallar ve teknik araçlar bütünü, başlangıçta kullanılabilecek bir kavramsal yorum olarak korunur. Bu yorum, belirli bir aygıtın yerleşik adı veya alanın tek tarihsel kökeni olarak kabul edilmez. Beş protokol boyunca yorumun açıklayıcı gücü ve sınırları incelenebilir. Başlangıçtaki soru, araştırmanın sonucunu önceden zorunlu kılmaz.

~~~text
  BASLANGIC  ayrilir
    bilinenler  |  henuz dogrulanmamis kabuller  |  yanit bekleyen
                                                    sorular
    kayitli baslangic:  bes boyutu sorgulayan sorular + bu boyutlari
    birlikte tasiyan "makine"nin kim oldugu ve kim olmadigi
    kullanicinin ayrica kisisel, kurumsal veya projeye ozgu bir nedeni
    varsayilmaz; ancak kendisi belirtirse kayda eklenir

  KAPSAM KOSULU  "Gecmis baglamlari buraya tasima. Burasi ile sinirli
                 kalma."
    kayit icinde ayirt edilebilir kalir:
      kullanicinin ifadesi | dis kaynagin bilgisi | aciklamayi kuranin
                                                    yorumu

  UC BOLUM
    0 Tohum    incelemeye hangi sorularla ve kabullerle baslandigi
    1 Varlik   alanin ne oldugu, kimligini hangi ozelliklerin kurdugu
    5 Gaye     alanin ve duzenegin hangi amaclara hizmet ettigi
    arastirmanin baslama nedeni  =/=  arastirilan seyin hizmet ettigi
                                      amac   (iliskili, ayri aciklanir)

  "MAKINE" ONERISI  kavramsal yorum olarak korunur
    -/->  belirli bir aygitin yerlesik adi
    -/->  alanin tek tarihsel kokeni
    baslangictaki soru  -/->  sonucu onceden zorunlu kilar
~~~

*Çizim 2 — Tohum: başlangıçta ayrılanlar; kapsam koşulu; Tohum, Varlık ve Gaye; makine önerisinin niteliği.*

### Başlangıcın tamamlanması

Tohum Protokolü, başlangıç soruları, kapsam, dayanaklar ve açık kabuller kaydedildiğinde tamamlanır. İnceleme sırasında soru değişirse ilk ifade korunur ve değişikliğin nedeni belirtilir. Böylece sonradan ortaya çıkan bilgi başlangıca geriye dönük olarak yerleştirilmez. Bu kayıt, 1–5 arasındaki protokollere hareket noktası sağlar; Kökleşme Protokolünde de başlangıç sorularının ne ölçüde karşılandığını değerlendirmek için yeniden kullanılır.

### Masaüstünde uygulama

**Girdiler.** Kullanıcının özgün soruları ve kapsam talimatı, mevcut soru ve yanıt kaydı, kaynakça ve varsa bu inceleme için sağlanan ek dosyalar kullanılır. Başlangıç girdileri henüz verilmemişse konu ve beklenen çıktı açık soru olarak kaydedilir.

1. Özgün soruları ve kapsam talimatını başlangıç kaydına aktar. Alıntıları kendi açıklamandan ayır; beş kaynak soruyu 1–5 protokollerine eşleştir ve “makine” sorusunu ortak soru olarak kaydet.

2. İncelemenin konusunu, sınırlarını, beklenen çıktısını ve esas alınan tarihi yaz. Alanın kendisi mi yoksa belirli bir sistem mi incelenecek, belirt. Kullanıcıya açıklamadığı bir kişisel veya kurumsal niyet atfetme.

3. İncelenecek dosya ve kaynakların adlarını, yollarını veya adreslerini kaydet. Sağlanan, erişilemeyen ve henüz sağlanmamış girdileri ayır. İnceleme kapsamını bu kayıt üzerinden belirle.

4. Başlangıç durumunu Bilinenler, Varsayımlar ve Açık sorular altında yaz. “Makine” adlandırmasının bu belge içindeki kavramsal niteliğini ve doğrulanması gereken diğer kabulleri belirt.

5. Çalışma kimliğini ve kayıt klasörünü belirle. Sonraki protokollerin hangi girdilere dayanacağını yaz; eksik girdilerin hangi sonuçları etkilediğini göster.

**Üretilecek kayıt.** Çalışma klasöründe `00_tohum_kaydi.md` dosyasını oluştur. Ortak kayıt bilgilerine ek olarak şu başlıkları kullan: Özgün sorular ve talimat; Konu, kapsam ve beklenen çıktı; Başlangıç kaynakları; Bilinenler; Varsayımlar; Açık sorular.

**Tamamlanma koşulu.** Başka bir uygulayıcı hangi soruların ele alınacağını, hangi kapsamla çalışılacağını, hangi girdilerin bulunduğunu ve hangi açıklamaların henüz varsayım olduğunu bu kayıttan anlayabilmelidir. Belirleyici eksik girdi varsa durum eksik olarak kaydedilir.

## 1 Varlık Protokolü

**Kaynak soru:** Nedir? Onu o yapan nelerdir? Neler değildir?

### Alanı kuran ilişki

Bilgi Erişimi ve Arama Sistemleri Mühendisliği, bir bilgi ihtiyacını karşılamaya yarayabilecek içeriklerin bulunmasını, seçilmesini ve kullanılabilir biçimde sunulmasını sağlayan sistemleri tasarlama, kurma, değerlendirme ve işletme alanıdır. Bir kişi veya uygulamanın yapmaya çalıştığı iş ile erişebildiği içerik arasında kurulması gereken ilişki, alanın temel problemidir. Bir kaydın saklanmış olması, gerektiğinde bulunabildiğini veya bulunanın ihtiyaca uygun olduğunu göstermez. [1]

Bu ilişkinin başlangıcında, sistemin görebildiği sorgu ile sorgunun ifade etmeye çalıştığı ihtiyaç arasındaki ayrım bulunur. Kullanıcı aynı sözcüklerle bir tanımı öğrenmek, belirli bir belgeyi bulmak veya karşılaştığı sorunu çözmek isteyebilir. İhtiyacını eksik anlatabilir; kullandığı terimler kaynakların diliyle örtüşmeyebilir. Bu nedenle sorgu, ihtiyacın tamamı olarak kabul edilmez. Alan, görülebilen ifadeden hareketle hangi içeriğin uygun olabileceğini belirleme sorununu üstlenir ve bu belirlemenin yanılabileceğini hesaba katar. [2]

İlgililik, belgenin tek başına ve değişmeden taşıdığı bir nitelik olarak ele alınmaz. İçerik ile ihtiyaç, görev, kullanıcı ve zaman arasında kurulan bir ilişkidir. Aynı kılavuz, belirli bir ürün sürümünü kullanan kişi için gerekli, başka bir sürümü kullanan kişi için uygunsuz olabilir. Belgenin metni değişmediği hâlde aramadaki değeri değişir. Alanın ayırt edici özelliği, bu ilişkiyi hesaplanabilir seçimlere dönüştürürken kullanıcı açısından anlamını korumaya çalışmasıdır.

~~~text
  ALANI KURAN ILISKI
    bilgi ihtiyaci  -- ifade --->  sorgu  ------------>  icerik
    (eksik anlatilabilir;          (sistemin            (ihtiyaca uygun
     terimler kaynaklarin           gorebildigi)          olabilecek)
     diliyle ortusmeyebilir)
    sorgu  -/->  ihtiyacin tamami
    belirleme yanilabilir; alan bunu hesaba katar

    ayni sozcuklerle:  bir tanimi ogrenmek? . belirli bir belgeyi
                       bulmak? . karsilastigi sorunu cozmek?
    bir kaydin saklanmis olmasi  -/->  gerektiginde bulunabildigi
                                 -/->  bulunanin ihtiyaca uygun oldugu

  ILGILILIK  belgenin degismez niteligi degil, bir iliski
                       ihtiyac
                          |
            gorev ---- icerik ---- kullanici
                          |
                        zaman
    ayni kilavuz:  bir urun surumunu kullanan icin gerekli
                   baska bir surumu kullanan icin uygunsuz
    belgenin metni degismedigi halde aramadaki degeri degisir
~~~

*Çizim 3 — Varlık: ihtiyaç, sorgu ve içerik; ilgililik bir ilişki olarak.*

### İçerik ve taşıyıcı düzenek

Arama sisteminin işlediği içerik, dünyanın kendisiyle özdeş değildir. Bir belge olaylara ilişkin kayıtlar, açıklamalar, ölçümler veya iddialar taşıyabilir. Bunların bulunması, temsil ettikleri durumun bütünüyle kavrandığı anlamına gelmez. Sistem ayrıca içerikle belirli temsiller üzerinden çalışır; sözcükler, başlıklar, alanlar veya sayısal gösterimler içeriğin bazı özelliklerini görünür kılar. Böylece alanın varlığı, ihtiyaç sahibini, araştırılabilir kayıtları ve bu kayıtların işlenebilir temsillerini birlikte düşünmeyi gerektirir.

Bu unsurları birlikte taşıyan “makine”, ortak kaynak soruya verilen yanıtta insanın kayıtlı bilgiyle kurduğu ve araçlarla yürüttüğü amaçlı erişim düzeni olarak yorumlanmıştır. Kökenindeki fail, kayıtlar arasında yönünü bulmaya çalışan insandır. İşlemleri gerçekleştiren teknik parça arama sistemidir. Bütünün taşıyıcısı ise insanlar, kayıtlar, kurallar ve araçlar arasındaki ilişkidir. İhtiyacı taşıyan, işlemi yürüten ve sonucu değerlendiren tarafların aynı kişi ya da bileşen olması zorunlu değildir.

Bu tanım kavramsal bir okumadır; belirli bir aygıtın yerleşik adı veya bütün alanın tek tarihsel kökenine ilişkin bir iddia değildir. İnsanın arama faaliyetini açıklamak, insanı bütünüyle bir makineye indirgemek anlamına gelmez. Her sorgunun o anda bilinçli bir insan tarafından yazılması da gerekmez. Bir yazılım, önceden belirlenmiş bir görevi sürdürmek için arama yapabilir. Belkin, Oddy ve Brooks'un bilgi ihtiyacını kullanıcının bilgi durumundaki eksiklik veya uyumsuzlukla ilişkilendiren yaklaşımı, ihtiyacın başlangıçta tam ifade edilemeyebileceğine ilişkin kuramsal dayanaklardan biridir. [3]

~~~text
  ICERIK
    dunya  =/=  arama sisteminin isledigi icerik
      belge:  olaylara iliskin kayitlar . aciklamalar . olcumler .
              iddialar
      bulunmasi  -/->  temsil ettikleri durumun butunuyle kavranmasi
    sistem icerikle temsiller uzerinden calisir:
      sozcukler . basliklar . alanlar . sayisal gosterimler
    birlikte dusunulur:  ihtiyac sahibi + arastirilabilir kayitlar +
                         kayitlarin islenebilir temsilleri

  "MAKINE"  insanin kayitli bilgiyle kurdugu ve araclarla yuruttugu
            amacli erisim duzeni
    kokendeki fail             kayitlar arasinda yonunu bulmaya
                               calisan insan
    islemleri gerceklestiren   arama sistemi
    teknik parca
    butunun tasiyicisi         insanlar, kayitlar, kurallar ve araclar
                               arasindaki iliski
    ihtiyaci tasiyan, islemi yuruten ve sonucu degerlendiren ayni kisi
    ya da bilesen olmak zorunda degil
    her sorgu bilincli bir insanca yazilmaz; yazilim onceden
    belirlenmis bir gorevi surdurmek icin de arayabilir
~~~

*Çizim 4 — Varlık: içerik ve temsil; makine için önerilen erişim düzeni.*

### Kimliğin sınırları

Alan, yalnızca web aramasından veya büyük koleksiyonlardan oluşmaz. Kişisel notlarda, kurum arşivinde, ürün kataloğunda, kod koleksiyonunda veya görsel kaynaklarda da bilgiye erişim problemi bulunabilir. Her uygulamanın öğrenilmiş bir model, vektör gösterimi veya sıralı sonuç listesi kullanması gerekmez. Kesin koşullarla çalışan erişim yöntemleri de bu kapsamda yer alabilir. Alanın sürekliliğini sağlayan belirli bir teknoloji değil, ihtiyaç ile uygun içerik arasındaki ilişkinin kurulmasıdır.

Benzerlik, ilgililik, doğruluk ve görev yararı birbirlerinin yerine kullanılamaz. Yanlış bir iddianın yayılmasını araştıran kişi için o iddiayı içeren belge ilgili olabilir. Tamamen doğru bir açıklama ise mevcut soruyu yanıtlamayabilir veya gereken ayrıntıyı sağlamayabilir. Bilgi erişimi bu nedenle bir hakikat garantisi değildir. Yüksek eşleşme ya da benzerlik puanı, içeriğin güvenilir olduğunu veya kullanıcının işini tamamladığını kendiliğinden göstermez.

Tek başına bilgisayar, veri deposu, sıralama algoritması veya dil modeli bütün alanın kimliğini açıklamaz. Turing'in makine modeli simgeler ve durumlar üzerinden hesaplamayı biçimselleştirir; bu, hesaplamanın hangi bilgi ihtiyacı için değer taşıdığını ayrıca belirleme gereğini ortadan kaldırmaz. Mühendislik niteliği, kurulan yeteneğin gerçek içerikte, değişen ihtiyaçlarda ve belirli hizmet koşulları altında çalışmasından gelir. Güzel bir arayüz veya başarılı birkaç örnek, bu bütünün değerlendirilmesinin yerine geçmez. [4]

~~~text
  ALANIN YERLERI  yalniz web aramasi ve buyuk koleksiyonlar degil
    kisisel notlar . kurum arsivi . urun katalogu . kod koleksiyonu .
    gorsel kaynaklar
    ogrenilmis model, vektor gosterimi, sirali liste:  zorunlu degil
    sureklilik:  belirli bir teknoloji degil; ihtiyac ile uygun icerik
                 arasindaki iliskinin kurulmasi

  DORT AYRI SEY  benzerlik . ilgililik . dogruluk . gorev yarari
                         dogru                dogru degil
    ilgili               .                    yanlis bir iddianin
                                              yayilmasini arastiran
                                              kisi icin iddiayi
                                              iceren belge
    soruyu yanitlamayan  tamamen dogru        .
                         bir aciklama
    yuksek eslesme veya benzerlik puani  -/->  guvenilir icerik
                                         -/->  kullanicinin isi bitti
    bilgi erisimi  -/->  hakikat garantisi

  TEK BASINA ALANIN KIMLIGI DEGIL
    bilgisayar . veri deposu . siralama algoritmasi . dil modeli
    Turing'in modeli  [4]:  hesaplamayi bicimsellestirir; hangi bilgi
    ihtiyaci icin deger tasidigini ayrica belirleme geregi kalkmaz
~~~

*Çizim 5 — Varlık: alanın yerleri; benzerlik, ilgililik, doğruluk ve görev yararı; kimliğin sınırları.*

### Masaüstünde uygulama

**Girdiler.** `00_tohum_kaydi.md`, mevcut soru ve yanıtlar, incelenen konu için sağlanan belgeler ve ilgili kaynaklar kullanılır.

1. Tohum kaydını okuyarak inceleme nesnesini bir paragrafta belirle. Bir mühendislik alanı, belirli bir ürün ve bir yazılım bileşeni hakkında konuşmanın farklı kapsamlar olduğunu görünür tut.

2. Bilgi ihtiyacını, ihtiyacın sorguda nasıl ifade edildiğini ve erişilecek içeriği ayrı yaz. Sağlanan gerçek örneği kullan; açıklama için kurduğun örneği varsayımsal örnek olarak işaretle.

3. İhtiyacı taşıyan, kayıtları üreten veya düzenleyen, seçimi gerçekleştiren ve sonucu değerlendiren tarafları açıkla. Somut sistem verisi yoksa insan, kayıt, kural ve araç ilişkisini kavramsal düzeyde tut.

4. Alanı tanımlayan özelliklerle belirli uygulamalarda görülen tercihleri ayır. “Kimdir, kim değildir?” sorusunu bu ayrımlar üzerinden yanıtla; kullanılan bir teknolojiyi bütün alan için zorunlu sayma.

5. Temel tanımı, ayırt edici özellikleri ve sınırlarını birleştir. Kaynak bilgisini, kavramsal çıkarımı ve açık kalanları belirt; benzerlik, ilgililik, doğruluk ve görev yararı ayrımını koru.

**Üretilecek kayıt.** Çalışma klasöründe `01_varlik_kaydi.md` dosyasını oluştur. Ortak kayıt bilgilerine ek olarak şu başlıkları kullan: Kaynak soru; Temel tanım; Ayırt edici özellikler; Taşıyıcı düzenek; Kimliğin sınırları; Dayanaklar ve açık sorular.

**Tamamlanma koşulu.** İncelenen şeyin ne olduğu, hangi ihtiyaç ilişkisiyle kurulduğu ve hangi özelliklerin bütün alan için zorunlu olmadığı anlaşılmalıdır. “Makine” adlandırmasının kavramsal yorum niteliği korunmalıdır.

## 2 Mekan Protokolü

**Kaynak soru:** Nerededir? Bu yeri, oraya has bir yer yapan nelerdir? Neler değildir?

### İçerik ile kullanım arasındaki yer

Bilgi Erişimi ve Arama Sistemleri Mühendisliğinin sistem içindeki yeri, içeriğin saklandığı taraf ile o içerikten yararlanan insan veya uygulama arasındadır. Bu konum, mimaride tek bir bileşene karşılık gelmez. Kaynakların seçilmesi, aranabilir hâle getirilmesi, adayların bulunması ve sonuçların sunulması boyunca farklı işlevlere dağılır. Alanın yerini belirleyen, bir sunucunun adresinden çok, kayıtların belirli bir ihtiyaç bakımından erişilebilir hâle getirilmesini sağlayan ilişkilerin nasıl kurulduğudur.

Arama mekânı hem fiziksel hem mantıksal özellikler taşır. Raflar, diskler ve sunucular içeriğin maddi olarak bulunduğu yerleri oluştururken kataloglar, indeksler ve bağlantılar içeriğe ulaşılabilecek yolları düzenler. Bir belge fiziksel olarak yakın olduğu hâlde bulunması zor olabilir. Uzak bir kaynak ise uygun biçimde tanımlanmış ve erişime açık olduğu için kolayca bulunabilir. Dolayısıyla uzaklık, erişilebilirliği tek başına açıklamaz; temsil ve düzenleme biçimleri de hesaba katılır.

İçeriğin mevcut olmasıyla aramada görünür olması arasındaki fark bu mekânın önemli özelliğidir. Bir kayıt koleksiyonda bulunmasına rağmen uygun biçimde tanımlanmamış, yanlış temsil edilmiş veya aramanın erken bir aşamasında elenmiş olabilir. Kullanıcı bu durumda içeriğin yokluğuyla erişim yolunun başarısızlığını ayırt edemeyebilir. Mühendisliğin konumu, bu iki durumu birbirine karıştırmadan incelemeyi gerektirir. Saklanabilirlik ile bulunabilirlik ayrı sorumluluklardır.

~~~text
  YER  icerigin saklandigi taraf ile yararlanan taraf arasinda
    saklayan taraf                                    kullanan taraf
    [kayitlar]                                    [insan veya uygulama]
        |                                                   ^
        +--> secilir --> aranabilir --> adaylar --> sonuclar +
                         hale getirilir  bulunur     sunulur
    tek bir bilesene karsilik gelmez; islevlere dagilir

  FIZIKSEL VE MANTIKSAL
    raflar . diskler . sunucular       icerigin maddi olarak bulundugu
    kataloglar . indeksler . baglantilar   icerige ulasilan yollar
    fiziksel olarak yakin  -->  bulunmasi zor olabilir
    uzak ama uygun tanimlanmis ve acik  -->  kolayca bulunabilir
    uzaklik  -/->  erisilebilirligi tek basina aciklar

  MEVCUT AMA GORUNMEZ
    koleksiyonda var, ama:  uygun tanimlanmamis . yanlis temsil
                            edilmis . erken bir asamada elenmis
    kullanici ayirt edemeyebilir:  icerigin yoklugu  |  erisim yolunun
                                   basarisizligi
    saklanabilirlik  =/=  bulunabilirlik
~~~

*Çizim 6 — Mekan: içerik ile kullanım arasındaki yer; fiziksel ve mantıksal; mevcut ama görünmez.*

### Disiplinler ve kurumlar arasındaki konum

Alan, bilgi ve belge yönetimi, veri mühendisliği, veritabanı sistemleri, doğal dil işleme, makine öğrenmesi, dağıtık sistemler ve insan–bilgisayar etkileşimiyle ilişkilidir. Bu alanların yöntemlerinden farklı ölçülerde yararlanır. Onu ayırt eden, katkıları bulunabilirlik ve ilgililik problemi etrafında birleştirmesidir. Kaynakların düzenlenmesi, dilin işlenmesi, hesaplamanın gerçekleştirilmesi ve sonucun anlaşılması aynı ihtiyaca bağlanır. SIGIR topluluğunun konu kapsamı da indeksleme ve sıralamayla birlikte kullanıcı çalışmaları, etkileşim, verimlilik ve değerlendirmeyi içerir. [5]

Kuruluş içindeki yeri yalnızca ekip adıyla belirlenemez. Aynı sorumluluk bir kuruluşta arama ekibinde, başka bir kuruluşta veri, platform, yapay zekâ veya ürün ekibinde bulunabilir. Belirleyici olan, bilginin bulunamaması ya da uygunsuz içeriğin öne çıkarılması durumunda nedenlerin uçtan uca araştırılmasıdır. Her bileşeni aynı ekibin geliştirmesi gerekmez; ancak bileşenlerin toplam etkisi sahipsiz kalmamalıdır. Tek tek parçaların çalışması, bütün ilişkinin kullanıcı açısından çalıştığını göstermeyebilir.

Taşıyıcı düzenek bu nedenle yalnızca bir aygıtta veya tek bir kişinin zihninde konumlandırılamaz. Kayıtları üretenler, düzenleyenler, arayanlar ve teknik sistemi işletenler farklı kişiler olabilir. Kişisel bir koleksiyonda bu roller aynı kişide birleşebilir; büyük bir bilgi hizmetinde farklı kurumlara dağılabilir. Resmî bir kurumun bulunması her uygulama için şart değildir. Kaynak kapsamı ve erişim yollarına ilişkin kararların nerede alındığının anlaşılması, sorumlulukları görünür kılar.

### Erişim mekânının sınırları

Bu konumun toplumsal bir sonucu vardır: Sistem, hangi içeriğin görünür olacağını ve kullanıcının hangi kayıtlarla karşılaşma olasılığının artacağını etkiler. Etkinin kapsamı kişisel bir arşivde sınırlı, geniş bir bilgi hizmetinde daha büyük olabilir. Kaynak seçimi ve sıralama kararları dikkatin dağılımını da etkiler. Bu, bütün arama sistemlerine aynı toplumsal gücü yükleyen bir iddia değildir; sistemin kapsamına bağlı bir çıkarımdır.

Taşıyıcı düzenek, sınırları belirsiz biçimde bütün topluma genişletilmemelidir. İncelenen sistemin mekânı; ihtiyacı, kaynak kapsamını, erişim koşullarını, seçim kararlarını ve sonuçların değerlendirilmesini fiilen etkileyen unsurlar üzerinden tanımlanmalıdır. Hangi kaynakların içeri alındığı, hangilerinin dışarıda kaldığı ve kimlerin hangi içeriğe ulaşabildiği açık olduğunda bu sınır anlaşılabilir. Böylece “insanlar, kurumlar ve araçlar” ifadesi belirli bir erişim ilişkisinin açıklamasına dönüşür.

Alan yalnızca ön yüzde, veri deposunda, modelin içinde veya bulutta değildir. Bu yerlerin her biri belirli bir uygulamada önemli olabilir; hiçbiri bütünün zorunlu ve yeterli açıklaması sayılamaz. Güzel bir arayüz eksik kaynağı, güçlü bir model yanlış erişim koşulunu kendiliğinden düzeltmez. Mekan Protokolü, içerikten kullanıma uzanan yolları, bu yolların sınırlarını ve onları kuran sorumlulukları birlikte görünür kılar.

~~~text
  DISIPLINLER ARASINDAKI KONUM
    bilgi ve belge yonetimi -------+
    veri muhendisligi -------------+
    veritabani sistemleri ---------+     +---------------------------+
    dogal dil isleme --------------+---->| bulunabilirlik ve         |
    makine ogrenmesi --------------+     | ilgililik problemi        |
    dagitik sistemler -------------+     +---------------------------+
    insan-bilgisayar etkilesimi ---+
    yontemlerinden farkli olculerde yararlanir; katkilari bu problem
    etrafinda birlestirir  [5]

  KURULUS ICINDEKI YER  ekip adi belirlemez
    arama . veri . platform . yapay zeka . urun ekibi
    her bileseni ayni ekip gelistirmek zorunda degil; bilesenlerin
    toplam etkisi sahipsiz kalmamali

  ROLLER
    kayitlari ureten . duzenleyen . arayan . teknik sistemi isleten
    kisisel koleksiyonda:  ayni kiside birlesebilir
    buyuk bir bilgi hizmetinde:  farkli kurumlara dagilabilir

  SINIR  butun topluma genisletilmez
    ihtiyac . kaynak kapsami . erisim kosullari . secim kararlari .
    sonuclarin degerlendirilmesi:  bunlari fiilen etkileyen unsurlar
    alan yalnizca on yuzde, veri deposunda, modelin icinde veya
    bulutta degildir
~~~

*Çizim 7 — Mekan: disiplinler arasındaki konum; kuruluş içindeki yer; roller; sınır.*

### Masaüstünde uygulama

**Girdiler.** `00_tohum_kaydi.md` ve `01_varlik_kaydi.md` ile belirlenen kapsam içindeki dosyalar, kaynak adresleri ve varsa sistem veya kurum açıklamaları kullanılır.

1. Belirlenmiş kapsam içinde kaynak envanteri çıkar. Her girdinin adını, yolunu veya adresini, türünü ve erişim durumunu yaz. Bulunamayan kaynağı erişilemedi veya sağlanmadı olarak işaretle.

2. İçeriğin saklandığı yer ile bulunmasını sağlayan yolu ayır. Fiziksel konumu, katalog veya indeks gibi mantıksal erişim yapısını ve kullanıcıya sunulan yüzeyi açıkla.

3. İçeriğin kaynağından kullanımına uzanan bir erişim yolunu izle. Somut sistemde gözlenebilen adımları kaydet; alan incelemesinde bu yolu kavramsal örnek olarak yaz.

4. Kaynak kapsamını, içeri alma ve dışarıda bırakma koşullarını, bilinen erişim yetkilerini ve sorumlulukları belirle. Belgelerde bulunmayan kurum, ekip veya yetki modelini varsayma.

5. İçeriğin bulunmaması, mevcut olduğu hâlde aramada görünmemesi ve erişim dışında kalması durumlarını ayır. Alanın konumunu ve erişim sınırlarını gerekçeleriyle birleştir.

**Üretilecek kayıt.** Çalışma klasöründe `02_mekan_kaydi.md` dosyasını oluştur. Ortak kayıt bilgilerine ek olarak şu başlıkları kullan: Kaynak soru; Alanın konumu; Kaynak envanteri; Erişim yolu; Sınırlar ve sorumluluklar; Eksik bilgiler.

**Tamamlanma koşulu.** Kaynağın varlığı, bulunabilirliği ve erişilebilirliği ayrı görülebilmelidir. İncelenen düzeneğin sınırı açık olmalı; açıklama kapsamı belirsiz biçimde genişletilmemelidir. Kaynak envanteri için gerektiğinde kısa bir tablo kullanılabilir.

## 3 Usül Protokolü

**Kaynak soru:** Nasıl işler yapar? Bu yaptıklarını, ona has yapan nelerdir? Neler değildir?

### İhtiyacı ve kaynakları işleyen hizmete dönüştürmek

Bilgi erişimi mühendisliğinin usulü, bir bilgi ihtiyacının hangi sonuçla karşılanmış sayılacağını belirlemekle başlar. Belirli bir kılavuzu bulmak, seçenekleri karşılaştırmak ve araştırmanın farklı yönlerini taramak aynı başarı koşuluna sahip değildir. İlk durumda doğru kaynağa erken ulaşmak, diğerlerinde kapsam ve çeşitlilik daha önemli olabilir. Sistemin nasıl değerlendirileceği, kurulacak yöntemden bağımsız ve sonradan eklenmiş bir konu olarak bırakılmaz.

Bu ilişki, bilgisayar öncesi kataloglarda da görülebilir. Cutter'ın 1891 baskısında katalog amaçları, bilinen yazar, başlık veya konudan hareketle kitabı buldurmak, kütüphanenin ne içerdiğini göstermek ve kitap seçimine yardımcı olmak olarak açıklanır. Ardından bu amaçlara hizmet edecek kayıt ve gönderme yöntemleri gelir. Bu örnek, arama usulünün araçtan önce amaç ve seçim koşullarıyla kurulabildiğini gösterir. [6]

Kaynak hazırlama aşamasında metnin yanında başlık, tarih, dil, sürüm, kaynak ilişkileri ve erişim yetkileri de gerekebilir. Dosyanın tek bir belge mi yoksa bölümlere ayrılmış bir kaynak mı olacağı belirlenir. Yinelenen, değişen ve silinen içerikler yönetilir; bir parçanın anlaşılması için gereken bağlamın korunması gözetilir. Belge düzeyindeki erişim denetimi, izin bilgisini içerikle birlikte taşıma ve sorgu sırasında uygulama gereğinin somut örneğidir. [7]

~~~text
  ONCE BASARI KOSULU
    belirli bir kilavuzu bulmak        dogru kaynaga erken ulasmak
    secenekleri karsilastirmak         kapsam ve cesitlilik daha
    arastirmanin farkli yonlerini      onemli olabilir
    taramak
    degerlendirme  -/->  yontemden bagimsiz, sonradan eklenen bir konu

  CUTTER 1891  [6]  aractan once amac ve secim kosullari
    amaclar                                 -->  kayit ve gonderme
      bilinen yazar, baslik veya konudan         yontemleri
      kitabi buldurmak
      kutuphanenin ne icerdigini gostermek
      kitap secimine yardimci olmak

  KAYNAK HAZIRLAMA
    metin + baslik . tarih . dil . surum . kaynak iliskileri . erisim
    yetkileri
    tek belge mi, bolumlere ayrilmis kaynak mi?
    yinelenen . degisen . silinen icerik yonetilir
    bir parcanin anlasilmasi icin gereken baglam korunur
    belge duzeyinde erisim denetimi  [7]:  izin bilgisi icerikle
    birlikte tasinir, sorgu sirasinda uygulanir
~~~

*Çizim 8 — Usül: önce başarı koşulu; Cutter'ın katalog amaçları; kaynak hazırlama.*

### Temsil üzerinden seçmek

İçerik, makinenin işleyebileceği temsillere dönüştürülür. Sözcükler, alanlar, ilişkiler veya öğrenilmiş sayısal gösterimler içeriğin belirli özelliklerini görünür kılar. Mooers'ın 1951 çalışması, içeriğin makinece okunabilen işaretlerle temsil edilmesini ve bu işaretlerin seçim için kullanılmasını birlikte ele alır. Kodlamayla içeriğin düşünsel niteliği arasındaki bağ, hem makinenin yapısını hem işlemin yararını etkiler. [8]

İndeks, uygun adaylara her aramada bütün koleksiyonu baştan incelemek zorunda kalmadan ulaşmayı sağlayan erişim yapısıdır. Sözcükleri bölme ve normalleştirme kararları dile ve içerik türüne bağlıdır; belgeyle sorgunun uyumlu işlenmesi gerekir. Türkçe ekleri ele almakla ürün kodundaki işaretleri korumak aynı karar değildir. Ayrım taşıyan bir kodun veya sürüm numarasının gereksiz biçimde değiştirilmesi, doğru sonucun bulunmasını zorlaştırabilir. [9]

Sözcüksel erişim, sözcükleri, özel adları ve kodları eşleştirmede kullanılabilir. Vektör erişimi, seçilen modelin sayısal temsilinde yakınlık arar. Hibrit erişim ise birden fazla yöntemin sonuçlarını birleştirir. Bunlar tek başına doğruluk veya görev başarısı garantisi taşımaz. Güncel araçların tam metin ve vektör aramasını birlikte çalıştırabilmesi, her koleksiyonda aynı birleşimin üstün olduğu anlamına gelmez; yöntem seçimi gerçek ihtiyaçları temsil eden sorgular üzerinde değerlendirilmelidir. [11]

Birçok sistem, geniş koleksiyondan aday bulmayı ve adayları daha ayrıntılı değerlendirmeyi ayrı aşamalarda yapar. Pahalı bir sıralama yönteminin bütün koleksiyona uygulanması süre ve kaynak sınırlarını aşabilir. Çok aşamalı sıralama, ayrıntılı hesaplamayı daha küçük bir aday kümesine ayırır. Yalnızca kendisine verilen adayları yeniden sıralayan bileşen, bu kümeye hiç girmemiş bir kaynağı kurtaramaz. Bu nedenle aday bulmanın kapsamı ile son sıralamanın kalitesi ayrı incelenir. [10]

~~~text
  TEMSIL UZERINDEN SECMEK
    icerik  -->  temsil:  sozcukler . alanlar . iliskiler . ogrenilmis
                          sayisal gosterimler
    indeks:  her aramada butun koleksiyonu bastan incelemeden uygun
             adaylara ulastiran erisim yapisi
    sozcuk bolme ve normallestirme dile ve icerik turune bagli
    Turkce ekleri ele almak  =/=  urun kodundaki isaretleri korumak

  ADAY BULMA
    sozcuksel   sozcukler, ozel adlar, kodlar
    vektor      secilen modelin sayisal temsilinde yakinlik
    hibrit      birden fazla yontemin sonuclari birlesir  [11]
    -/->  dogruluk veya gorev basarisi garantisi

  ASAMALI SIRALAMA  [10]
    \                genis koleksiyon                /
     \______________________________________________/
      \                 aday bulma                 /
       \__________________________________________/
        \    aday kumesi: ayrintili siralama     /
         \______________________________________/
                             |
                             v
                         sonuclar
    kumeye hic girmemis bir kaynak  -->  yeniden siralayan bilesen
                                         onu kurtaramaz
    aday bulmanin kapsami ile son siralamanin kalitesi ayri incelenir
~~~

*Çizim 9 — Usül: temsil ve indeks; aday bulma yöntemleri; aşamalı sıralama.*

### Sunmak, ölçmek ve işletmek

Sonuç, bağlantı listesi, belgenin ilgili bölümü, filtrelenebilir seçenekler veya kaynaklara dayanan bir yanıt biçiminde sunulabilir. Erişimle desteklenen üretim olarak anılan RAG, dış kaynaklardan getirilen içeriği dil üretimiyle birleştirir. Kaynak bulma ile kaynaklardan hareketle yanıt oluşturma, birbirine bağlı fakat ayrı sorumluluklardır. Doğru bulunan içerik yanlış özetlenebilir; makul bir açıklamaya verilen kaynak açıklamayı desteklemeyebilir. [12]

Ölçüm, tek bir sayıya indirgenmez. Precision, getirilen sonuçlar içinde ilgili olanların oranını; recall, değerlendirmede ilgili kabul edilen içeriklerin ne kadarının bulunduğunu ifade eder. nDCG gibi ölçüler, daha ilgili sonuçların üst sıralarda yer almasını değerlendirmeye katar. Bu ölçüler, kullanıcının gerçek görevini tamamladığını tek başına göstermez. Kullanıcı çalışmaları, uygun çevrimiçi deneyler ve görev tamamlama değerlendirmeleri, sistem sonuçlarının kullanım değerini ayrıca araştırır. [13] [14] [24]

Yaklaşık vektör aramasındaki recall ile bilgi erişimindeki recall aynı hedef kümeyi esas almak zorunda değildir. İlki, tam vektör aramasının bulacağı komşuların ne kadarının yakalandığını ölçebilir; ikincisi, bilgi ihtiyacı bakımından ilgili içeriklerin bulunmasıyla ilgilenir. Benzer biçimde tıklama da doğrudan yarar değildir. Kullanıcının sonuçları inceleme biçimi ve sonucun konumu tıklamayı etkileyebilir. Bu sinyallerden yararlanılırken neyi ölçtükleri ve neyi ölçmedikleri korunmalıdır. [15] [16]

İşletme sürecinde yanıt süreleri, başarısız sorgular, maliyet, indeks güncelliği ve izin değişiklikleri izlenir. Birkaç iyi örnek, bütün sorgu türlerinde güvenilir hizmet verildiğini göstermez. Ortalama sonuçların yanında dil, sorgu türü, nadir kodlar veya koleksiyon bölümleri bakımından farklılaşan başarısızlıklar incelenebilir. Değişiklikler karşılaştırılarak değerlendirilir; içerik ve ihtiyaç değiştikçe yöntemler yeniden ele alınır. Böylece hazırlama, sorgulama, seçme ve kullanım, geri bildirimle birbirine bağlanır.

~~~text
  OLCUM  tek bir sayiya indirgenmez  [13] [14]
      +---------- getirilenler ----------+
      |               +------------------+-------------------+
      |               |   ilgili ve      |                   |
      |               |   getirilen      |                   |
      +---------------+------------------+                   |
                      +------- ilgili kabul edilenler -------+
    precision   getirilenler icinde ilgili olanlarin orani
    recall      ilgili kabul edilenlerin ne kadarinin bulundugu
    nDCG        daha ilgili sonuclarin ust siralarda olmasi
    -/->  kullanicinin gercek gorevini tamamladigi

  AYNI AD, FARKLI HEDEF  [15] [16]
    yaklasik vektor aramasindaki   tam vektor aramasinin bulacagi
    recall                         komsularin ne kadari yakalandi
    bilgi erisimindeki recall      ihtiyac bakimindan ilgili icerikler
    tiklama  =/=  dogrudan yarar

  SUNMAK  RAG  [12]
    kaynak bulma  =/=  kaynaklardan hareketle yanit olusturma
    dogru bulunan icerik yanlis ozetlenebilir; verilen kaynak
    aciklamayi desteklemeyebilir

  ISLETMEK
    yanit sureleri . basarisiz sorgular . maliyet . indeks
    guncelligi . izin degisiklikleri
~~~

*Çizim 10 — Usül: ölçüm; aynı adla farklı hedef; kaynak bulma ile yanıt oluşturma; işletme.*

### Örnek ve usulün sınırları

Varsayımsal “X ürününde E17 hatasını 3.1 sürümünde nasıl gideririm?” sorgusunda ürün adı, hata kodu ve sürüm korunmalıdır. Başka ürüne ait E17 açıklaması yüksek sözcük benzerliğine rağmen uygun olmayabilir. İlgili bölüm “bağlantı kurulamadı” başlığı altında bulunabilir; bu durumda farklı ifadeler arasında ilişki kurulması yararlı olur. Daha yeni bir kılavuz, başka sürümü anlattığı için bu ihtiyacı karşılamayabilir. Örnek, gerçek bir ürünün hata davranışına ilişkin iddia taşımaz.

Aynı örnekte, içerik olarak ilgili bir servis notu kullanıcının yetkisi dışındaysa gösterilmemelidir. Yetki veya açıkça belirtilmiş sürüm gibi zorunlu koşullar, yalnızca sıralamaya küçük bir tercih puanı ekleme meselesi değildir. Uygun kaynak bulunamadığında kanıt eksikliği görünür tutulmalıdır. Yöntemin ayırt edici niteliği; kimlik, anlam, sürüm, yetki, seçim ve sunum kararlarını aynı ihtiyaca bağlamasıdır.

~~~text
  VARSAYIMSAL SORGU
    "X urununde E17 hatasini 3.1 surumunde nasil gideririm?"
    korunur:  urun adi  X  |  hata kodu  E17  |  surum  3.1

  ADAYLAR
    baska urune ait E17           yuksek sozcuk benzerligi; uygun
    aciklamasi                    olmayabilir
    "baglanti kurulamadi"         farkli ifade; aralarinda iliski
    baslikli bolum                kurulmasi yararli
    daha yeni bir kilavuz         baska surumu anlatir; bu ihtiyaci
                                  karsilamayabilir
    icerik olarak ilgili servis   kullanicinin yetkisi disinda;
    notu                          gosterilmemeli

  ZORUNLU KOSULLAR
    yetki . acikca belirtilmis surum
    -/->  siralamaya eklenen kucuk bir tercih puani
    uygun kaynak yoksa  -->  kanit eksikligi gorunur tutulur
    ornek, gercek bir urunun hata davranisina iliskin iddia tasimaz

  BAGLANIR  ayni ihtiyaca
    kimlik . anlam . surum . yetki . secim . sunum
~~~

*Çizim 11 — Usül: varsayımsal E17 sorgusu; adaylar; zorunlu koşullar.*

Usül Protokolü bu nedenle veriyi bir araca yüklemek, her sorguya aynı yöntemi uygulamak veya bir gösterimi başarılı biçimde çalıştırmakla tamamlanmaz. Makineyi oluşturan teknik parçalar, temsil ettikleri ayrımlar ve hizmet ettikleri görevle birlikte değerlendirilir. Bir yöntemin hesaplanabilir olmasıyla doğru problemi çözmesi birbirinin yerine geçmez; işlemin başarısı, kullanıcı ihtiyacıyla kurduğu bağ üzerinden sınanır.

### Masaüstünde uygulama

**Girdiler.** `00_tohum_kaydi.md`, `01_varlik_kaydi.md` ve `02_mekan_kaydi.md`; mevcut yöntem açıklamaları; varsa örnek sorgular, içerik örnekleri ve değerlendirme kayıtları kullanılır.

1. İncelenen ihtiyacın karşılandığını düşündürecek sonucu yaz. Belge bulma, öğrenme veya karşılaştırma gibi görevleri ayır. İlk başarı koşulunu Gaye bölümünde yeniden değerlendirmek üzere kaydet.

2. Kaynağın hazırlanmasından sonucun sunulmasına kadar işlemleri sırayla açıkla. Her önemli işlemde hangi girdinin alındığını, hangi kararın verildiğini ve hangi çıktının üretildiğini belirt.

3. Temsil, aday bulma, sıralama ve sunum yöntemlerini görevle ilişkilendir. Yöntemin neden uygun görüldüğünü ve hangi durumda yetersiz kalabileceğini yaz. Sisteme ilişkin veri yoksa alternatifleri kavramsal olarak karşılaştır.

4. Bir örnek ihtiyacın işlem boyunca nasıl ele alındığını göster. Kod, sürüm, kaynak ilişkisi veya erişim koşulu gibi korunacak ayrımların nerede uygulanacağını açıkla. Varsayımsal senaryoyu gözlenmiş sonuçtan ayır.

5. Değerlendirme usulünü kaydet. Ölçüm veya deney kanıtı verilmişse kapsamını ve sonucunu incele. Verilmemişse değerlendirme planını ve gereken girdileri yaz; başarı oranı, gecikme veya maliyet değeri üretme. Kaynak bulma ile yanıt üretmenin hata türlerini ayrı ele al.

**Üretilecek kayıt.** Çalışma klasöründe `03_usul_kaydi.md` dosyasını oluştur. Ortak kayıt bilgilerine ek olarak şu başlıkları kullan: Kaynak soru; İlk başarı koşulu; İşlem akışı; Yöntem gerekçeleri; Örnek izleme; Değerlendirme ve başarısızlık koşulları.

**Tamamlanma koşulu.** Her önemli işlemin girdisi, kararı ve çıktısı anlaşılmalıdır. Ölçünün neyi gösterdiği ve neyi göstermediği belirtilmeli; yöntem önerisi, yapılmış uygulama ve gösterilmiş başarı ayrı durumlar olarak kaydedilmelidir.

## 4 Zaman Protokolü

**Kaynak soru:** Hangi andadır? Bu anı, diğer zamanlardan farklı yapan nelerdir? Neler değildir?

### Aramanın ve kaydın zamanı

Zaman Protokolü, aramanın gerçekleştiği anı, kaydın ait olduğu dönemi ve alanın tarihsel gelişimini birlikte ele alır. Bilgi erişimi bu zamanları birbirine bağlar: Geçmişte üretilmiş bir kayıt, şimdiki bir ihtiyaç için bulunur ve henüz yapılacak bir işe yön verir. Bu ilişki, geçmişteki içeriğin bugünkü göreve uygunluğunu ayrıca değerlendirmeyi gerektirir. Arama sisteminin hızı, bu zamansal ilişkinin yalnızca bir bileşenidir.

Kullanıcının arama anı, ihtiyacının eksiksiz biçimde belirlendiği bir başlangıç olmak zorunda değildir. İlk sonuçlar yeni kavramlar öğretebilir, yanlış varsayımları görünür kılabilir veya başka sorular doğurabilir. Kullanıcı ne aradığını, arama sırasında daha iyi ifade etmeye başlayabilir. Bates'in gelişen arama süreci yaklaşımı da tek sorgunun ötesindeki bu değişimi ele alır. Sistemin zamanı; inceleme, yeniden sorgulama ve değerlendirmeyle gelişen bir oturumu da kapsar. [17]

İçeriğin zamanı tek bir tarihten oluşmaz. Olayın gerçekleşmesi, belgenin yayımlanması, içeriğin güncellenmesi, sistemin onu indekslemesi ve sorunun hakkında olduğu dönem birbirinden ayrılabilir. Daha yeni yayımlanmış bir kılavuz, eski sürümü kullanan kişi için uygun olmayabilir. Tarihsel bir soruda eski belge doğru hedefken, bugünkü uygulamayı araştıran kişide aynı belge yanlış yönlendirmeye neden olabilir. Güncellik ile sorunun zamanı bakımından geçerlilik ayrı değerlendirme konularıdır.

Yanıt süresinin değeri de yapılan işe bağlıdır. Belirli bir kaydı hızla bulma ihtiyacında uzun bekleme, sistemin yararını azaltabilir. Kapsamlı bir araştırmada daha fazla süre, daha geniş kaynak kapsamı veya ayrıntılı değerlendirme karşılığında kabul edilebilir olabilir. Kaynağın değişmesiyle arama sonucunun değişmesi arasındaki gecikme de bu koşula dâhildir; hızlı dönen sonuç, eski bir indekse dayanıyor olabilir. Dinamik indeksleme, değişen koleksiyonun erişim yapısına aktarılmasını ele alır. [18]

~~~text
  UC ZAMAN BAGLANIR
    gecmiste uretilmis kayit  -->  simdiki ihtiyac  -->  yapilacak is
    gecmisteki icerigin bugunku goreve uygunlugu ayrica degerlendirilir

  ARAMA OTURUMU  [17]
    sorgu --> sonuclar --> yeni kavramlar, gorunur hale gelen yanlis
      ^                    varsayimlar, yeni sorular
      |                              |
      '------ yeniden sorgulama <----'
    arama ani  -/->  ihtiyacin eksiksiz belirlendigi baslangic

  ICERIGIN ZAMANLARI  ayrilabilir
    olayin        belgenin       icerigin       sistemin
    gerceklesmesi yayimlanmasi   guncellenmesi  indekslemesi
    ------+------------+-------------+-------------+--------->
    ayrica:  sorunun hakkinda oldugu donem
    guncellik  =/=  sorunun zamani bakimindan gecerlilik

  YANIT SURESI  yapilan ise bagli
    belirli bir kaydi hizla bulmak   uzun bekleme yarari azaltabilir
    kapsamli bir arastirma           daha fazla sure kabul edilebilir
    kaynak degisir  ...gecikme...  arama sonucu degisir
    hizli donen sonuc eski bir indekse dayaniyor olabilir  [18]
~~~

*Çizim 12 — Zaman: üç zamanın bağı; arama oturumu; içeriğin zamanları; yanıt süresi.*

### Tarihsel birikim ve güncel konum

Alanın tarihsel zamanı, önceki araçların tümüyle terk edildiği keskin dönemlerden oluşan bir çizgi olarak okunmamalıdır. Kataloglama, kayıtları tanımlama, içerikler arasında bağlantı kurma ve uygun olanı seçme faaliyetleri farklı teknik ortamlarda sürer. Bush'un 1945 tarihli Memex'i, kayıtların ve araştırma yollarının daha sonra yeniden kullanılmasını tasarlayan bir örnektir. Metinde gelecekte yapılabilecek bir aygıt olarak sunulur; gerçekleştirilmiş ilk arama motoru veya alanın tek başlangıcı değildir. [19]

31 Ekim 2026 itibarıyla alanın görünümü, sözcüksel erişimin, öğrenilmiş temsillerin ve kaynaklara dayalı yanıt üretiminin birlikte bulunduğu bir dönemdir. Güncel hibrit tasarımlar, tam metin araması ile vektör erişimini birleştirebilir. Bu birliktelik, eski yöntemlerin sona erdiğini veya yeni bir yöntemin her görevde üstün olduğunu göstermez. Uygun yaklaşım; içerik, sorgu türü, hata maliyeti ve çalışma koşulları üzerinden değerlendirilmelidir. Tarihsel yenilik, değerlendirme sorumluluğunu ortadan kaldırmaz. [11] [12]

Bu dönemde bazı sistemlerin getirdiği içerik, kullanıcının okuyacağı sonuç olmanın yanında başka bir modelin yanıtına dayanak oluşturur. TREC 2025 RAG değerlendirmesinde uzun ve karmaşık ihtiyaç anlatılarıyla birlikte yanıt kapsamı ve kaynak atıfları da ele alınmıştır. Böylece erişim ve üretilen yanıt kalitesini birlikte inceleme gereği görünür olur. TREC 2026 programındaki AutoJudge çalışması, otomatik ilgililik değerlendirmelerini insan değerlendirmeleriyle karşılaştırmayı hedefler; bu hedef tamamlanmış başarı olarak sunulmaz. [20] [23]

Bazı güncel tasarımlar karmaşık isteği alt sorgulara ayırarak farklı aramalar yürütür ve bulguları birleştirir. Metinlerin yanında görüntüler, görsel belgeler ve videolar da erişim hedefi olabilir. Azure'ın çoklu sorgu yaklaşımı ve VLM2Vec-V2 çalışması bu genişlemenin somut örnekleridir. Ancak her sorgu çok adımlı bir süreç gerektirmez. Ek adımlar süre, maliyet ve değerlendirme yükü doğurabilir; değerleri belirli bir ihtiyaçta sağladıkları katkıyla açıklanmalıdır. [21] [22]

### Zamansal sınır ve süreklilik

Bu an, aramanın çözüldüğü, dil modellerinin güncel kaynak erişimini kendiliğinden sağladığı veya akıcı yanıtın yeterli kanıt sayıldığı bir an değildir. Alanı taşıyan düzenin zamanı; geçmiş kayıtların korunması, şimdiki ihtiyacın karşılanması ve sonraki kullanımın mümkün kılınmasıyla kurulur. İçerik değiştikçe temsillerin, ihtiyaç değiştikçe sorguların, görev değiştikçe başarı ölçütlerinin yeniden ele alınması gerekir. Zaman Protokolü, açıklamanın hangi dönem ve koşullar için geçerli olduğunu görünür tutar; sürekliliği değişmezlikle özdeşleştirmez.

~~~text
  METINDEKI TARIHLER  aralar olcekli degil
    1891 --- 1945 --- 1951 --- 2025 ------- 2026 ------ 31 Ekim 2026
    Cutter   Bush     Mooers   TREC RAG     TREC        degerlendirme
    katalog  Memex    isaret-  degerlen-    AutoJudge   cercevesinin
    amaclari          lerle    dirmesi      (hedef)     tarihi
                      temsil
    keskin donemlerle terk edilen araclar degil; kataloglama, kayit
    tanimlama, baglanti kurma ve uygun olani secme farkli teknik
    ortamlarda surer
    Memex:  gelecekte yapilabilecek bir aygit olarak sunulur
      -/->  gerceklestirilmis ilk arama motoru;  alanin tek baslangici

  31 EKIM 2026 ITIBARIYLA  birlikte bulunanlar
    sozcuksel erisim . ogrenilmis temsiller . kaynaklara dayali yanit
    uretimi
    birliktelik  -/->  eski yontemlerin sona erdigi; yenisinin her
                       gorevde ustun oldugu
    ek adimlar (alt sorgular, gorsel hedefler):  sure, maliyet ve
    degerlendirme yuku; deger belirli bir ihtiyactaki katkiyla

  BU AN DEGIL
    x  aramanin cozuldugu an
    x  dil modellerinin guncel kaynak erisimini kendiliginden sagladigi
    x  akici yanitin yeterli kanit sayildigi
~~~

*Çizim 13 — Zaman: metindeki tarihler; 31 Ekim 2026 itibarıyla görünüm; bu anın ne olmadığı.*

### Masaüstünde uygulama

**Girdiler.** 00–03 arasındaki çalışma kayıtları, kullanılan kaynakların tarih ve sürüm bilgileri ve varsa güncelleme veya ölçüm kayıtları kullanılır.

1. İncelemenin yapıldığı tarihi ve sorunun hangi dönem hakkında olduğunu yaz. Belgenin düzenlenme tarihini kaynakların doğrulanma tarihiyle karıştırma.

2. Başlıca kaynaklar için bilinen olay, yayımlanma, güncellenme, sürüm ve son doğrulama bilgilerini kaydet. Bilinmeyen tarihleri açıkça belirt.

3. Güncel teknoloji veya hizmet özellikleri hakkındaki belirleyici iddiaları erişilebilen birincil kaynaklardan kontrol et. Bu yapılamıyorsa önceki değerlendirme tarihini koru ve güncel durumun doğrulanmadığını yaz.

4. İçerik güncelliğini, sorunun zamanına uygunluğu ve yanıt süresini ayrı değerlendir. Bilinen sürüm veya dönem koşullarının önceki protokollerdeki sonuçları nasıl etkilediğini açıkla.

5. Yeniden değerlendirmeyi gerektirecek değişiklikleri belirle. Kaynak, sürüm, kapsam, ihtiyaç veya başarı ölçütü değişiminin hangi kayıtları etkileyeceğini yaz.

**Üretilecek kayıt.** Çalışma klasöründe `04_zaman_kaydi.md` dosyasını oluştur. Ortak kayıt bilgilerine ek olarak şu başlıkları kullan: Kaynak soru; Değerlendirme anı; Kaynak tarihleri ve sürümler; Tarihsel ve güncel konum; Geçerlilik koşulları; Yeniden inceleme nedenleri.

**Tamamlanma koşulu.** Açıklamanın hangi dönem ve koşullar için geçerli olduğu anlaşılmalıdır. Yeni yayımlanma ile ihtiyaca uygunluk ayrılmalı; önerilmiş çalışma veya gelecek hedefi tamamlanmış sonuç olarak sunulmamalıdır.

## 5 Gaye Protokolü

**Kaynak soru:** Hangi nihai amaca hizmet eder? Bu nihai amaca ulaştıran nelerdir? Neler değildir?

### Amaç sahipliği ve başarı

Gaye Protokolü, alanın hangi işi ilerletmek için kurulduğunu ve başarısının kimin açısından değerlendirildiğini açıklar. Bütün uygulamalar için doğal olarak verilmiş tek bir nihai amaç varsaymak uygun değildir. Kullanıcı lehine savunulabilir amaç; kişinin bulma, öğrenme, karşılaştırma, keşfetme ve karar verme işini, uygun içeriğe ulaşmasını ve o içeriği değerlendirmesini kolaylaştırarak ilerletmektir. Üretilen sonuç, değerini bu işte sağladığı katkıdan alır; yalnızca sistemin bir çıktı vermesi başarıyı göstermez.

Kullanıcının amacı, kurumu işletenlerin hedefleri ve teknik sistemin optimizasyon hedefi birbirinden ayrılmalıdır. Kullanıcı bir kılavuzu bulmak isteyebilir; kurum verimliliği veya satışları artırmayı hedefleyebilir; sistem ise bir sıralama puanını yükseltecek biçimde ayarlanmış olabilir. Bu amaçlar kimi koşullarda birbirini destekler, kimi koşullarda ayrışır. Kullanıcı yararı tartışması, kimin yararının optimize edildiğinin açıklanmasını gerektirir. Bir teknik ölçütün iyileşmesi, kullanıcı amacının aynı ölçüde gerçekleştiğini kendiliğinden kanıtlamaz. [24]

Gayeyi taşıyan taraf da her zaman tek kişi değildir. İhtiyacı belirten, kaynak kapsamını kuran, erişim kurallarını koyan, sistemi işleten ve sonuçtan etkilenen kişiler farklı olabilir. Otomatik bir sistemin sorgu üretmesi bu amaç ilişkilerini ortadan kaldırmaz. Önceden tanımlanmış bir görevi yürütüyor olabilir; fakat görevin neden önemli olduğu ayrıca açıklanmalıdır. Alanı taşıyan makinenin amacı, yalnızca yazılımın içindeki hedef değişkeninden okunamaz; kullanım düzeni ve sorumluluklar da incelenmelidir.

~~~text
  KULLANICI LEHINE SAVUNULABILIR AMAC
    bulma . ogrenme . karsilastirma . kesfetme . karar verme isini
    uygun icerige ulasmayi ve onu degerlendirmeyi kolaylastirarak
    ilerletmek
    sistemin bir cikti vermesi  -/->  basari

  UC HEDEF  ayrilmali
    kullanicinin amaci           bir kilavuzu bulmak
    kurumun hedefi               verimlilik veya satislari artirmak
    sistemin optimizasyon        bir siralama puanini yukseltmek
    hedefi
    kimi kosulda birbirini destekler, kimi kosulda ayrisir
    kimin yararinin optimize edildigi aciklanir  [24]
    teknik olcutun iyilesmesi  -/->  kullanici amaci ayni olcude
                                     gerceklesti

  GAYEYI TASIYANLAR  tek kisi degil
    ihtiyaci belirten . kaynak kapsamini kuran . erisim kurallarini
    koyan . sistemi isleten . sonuctan etkilenen
    otomatik sorgu uretimi  -/->  bu amac iliskilerinin ortadan
                                  kalkmasi
    makinenin amaci yalnizca yazilimin icindeki hedef degiskeninden
    okunamaz
~~~

*Çizim 14 — Gaye: kullanıcı lehine amaç; üç hedef; gayeyi taşıyanlar.*

### Amaca ulaştıran koşullar

Amaca ulaşmanın ilk koşulu, ihtiyaç için yeterli kaynak kapsamıdır. Sistemin aramadığı kaynak, sıralama yöntemi ne kadar güçlü olursa olsun sonuçlara giremez. Kapsamın hangi koleksiyonları içerdiği ve hangi sınırlar içinde çalıştığı anlaşılır olmalıdır. Bununla birlikte daha çok içerik her zaman daha çok yarar sağlamaz. Yinelenen, bağlamı kaybolmuş veya görevle ilgisiz kayıtlar kullanıcının değerlendirme yükünü artırabilir. Esas olan, ihtiyacı karşılayabilecek yeterli ve uygun içeriğe erişebilmektir.

İkinci koşul, seçim ölçütlerini göreve bağlamaktır. Belirli bir belgeyi bulmada tam eşleşme ve doğru sonuca erken ulaşma değerli olabilir. Öğrenme ihtiyacında açıklayıcılık, karşılaştırmada seçeneklerin yeterli temsil edilmesi, araştırmada farklı yönlerin ve karşıt kanıtların bulunması önem kazanabilir. Aynı sıralama mantığı bütün bu işleri eşit biçimde karşılamayabilir. İlgililiğin açık bir ihtiyaç üzerinden değerlendirilmesi, teknik kararlarla kullanım amacı arasındaki bağı korur.

Üçüncü koşul, kullanıcının sonucu değerlendirebilmesidir. Kaynağın ne olduğu, hangi bölümün ihtiyacı karşıladığı, hangi tarih veya sürüm için geçerli olduğu ve açıklamanın hangi dayanağa bağlandığı gerektiğinde görünür olmalıdır. Böylece kullanıcı yanlış yorumu düzeltebilir, başka kaynak isteyebilir veya sonucun sınırlarını anlayabilir. Kanıt yetersizliğinin belirtilmesi de bu işlevin parçasıdır. Bir içeriğin bulunamamasıyla böyle bir içeriğin hiç bulunmaması aynı iddia değildir; bu ayrım korunmalıdır.

Belirsizliği azaltmak yararlı bir amaç olsa da her aramanın sonunda daha fazla kesinlik oluşması beklenmemelidir. İyi bir araştırma yeni bir çelişkiyi veya daha önce görülmemiş bir açıklamayı ortaya çıkarabilir. Kullanıcı geçici olarak daha az emin olurken konuyu daha iyi anlamaya başlayabilir. Gaye, belirsizliği gizleyerek kesinlik görüntüsü üretmek değildir. Gereken, belirsizliğin hangi kaynaklardan ve eksikliklerden doğduğunu değerlendirilebilir hâle getirmektir.

Bu yararın sürdürülebilmesi, hizmetin işletilebilirliğine bağlıdır. İçerik değiştiğinde güncellenmeyen, yoğunlukta kullanılamayan veya kabul edilemeyecek kadar pahalı çalışan bir sistem, amacına sürekli hizmet edemez. Güvenilirlik, süre ve kaynak kullanımı bu yüzden nihai amaca dışarıdan eklenen ayrıntılar değildir. Daha karmaşık bir yöntem, sağladığı ek yararla gerekçelendirilmelidir. Görevi yeterli kalitede karşılayan daha basit bir yöntem bulunduğunda karmaşıklığın kendisi başarı ölçüsü sayılamaz.

### Amaç yerine konamayacaklar

Daha çok sonuç, daha çok tıklama, daha uzun kullanım süresi, daha yüksek benzerlik puanı veya daha akıcı yanıt nihai amacın yerine geçirilemez. Bunlar belirli koşullarda yararlı göstergeler olabilir; anlamları görevle ilişkilendirilmelidir. Çok tıklama, kullanıcının aradığını bulamadığı için aramayı sürdürdüğünü de gösterebilir. Bir sistemin hedefini optimize etmesi, hedefin değerini kendiliğinden kanıtlamaz. Gaye Protokolünün belirleyici sorusu, kullanıcının bulunan içerikle neyi anlayabildiği, hangi işi ilerletebildiği ve bunu hangi gerekçelere dayandırabildiğidir.

~~~text
  AMACA ULASTIRAN KOSULLAR
    1  yeterli kaynak kapsami
       sistemin aramadigi kaynak  -->  sonuclara giremez
       daha cok icerik  -/->  her zaman daha cok yarar
    2  secim olcutlerinin goreve baglanmasi
       belge bulma      tam eslesme . dogru sonuca erken ulasma
       ogrenme          aciklayicilik
       karsilastirma    seceneklerin yeterli temsili
       arastirma        farkli yonler . karsit kanitlar
    3  kullanicinin sonucu degerlendirebilmesi
       kaynak . ihtiyaci karsilayan bolum . gecerli tarih veya
       surum . dayanak
       bir icerigin bulunamamasi  =/=  boyle bir icerigin hic
                                       bulunmamasi
    4  belirsizlik gizlenmez; hangi kaynaklardan ve eksikliklerden
       dogdugu degerlendirilebilir hale getirilir
    5  isletilebilirlik:  guvenilirlik . sure . kaynak kullanimi
       karmasiklik, sagladigi ek yararla gerekcelendirilir

  AMAC YERINE KONAMAZ
    daha cok sonuc . daha cok tiklama . daha uzun kullanim suresi .
    daha yuksek benzerlik puani . daha akici yanit
    cok tiklama:  kullanici aradigini bulamadigi icin aramayi
    surduruyor da olabilir
~~~

*Çizim 15 — Gaye: amaca ulaştıran koşullar; amaç yerine konamayanlar.*

### Masaüstünde uygulama

**Girdiler.** 00–04 arasındaki çalışma kayıtları ile varsa kullanıcı hedeflerini, kurum hedeflerini ve teknik başarı ölçütlerini açıklayan belgeler kullanılır.

1. İncelenen alanın veya düzeneğin hangi işi ilerletmesi beklendiğini yaz. Tohum'da bu incelemeyi başlatan nedenle, incelenen şeyin hizmet ettiği amacı ayır.

2. Kullanıcı amacı, kurumun hedefi ve teknik optimizasyon hedefini ayrı belirt. Örtüşme ve ayrışmaları eldeki dayanaklara göre açıkla. Belirtilmemiş hedefi bir kişi veya kuruma atfetme.

3. Amaç ile kaynak kapsamı, seçimin göreve uygunluğu, sonucun değerlendirilebilirliği ve hizmetin sürdürülebilmesi arasında bağ kur. Her ilişki için hangi önceki kayıttan yararlandığını göster.

4. Başarıyı gösterecek bulguyu ve tek başına yeterli olmayacak göstergeleri yaz. Tıklama, benzerlik puanı veya akıcı yanıt gibi göstergeleri mevcut göreve sağladıkları katkıyla değerlendir.

5. Önceki protokollerle tutarlılığı incele. Amaç açıklaması Usül'deki ilk başarı koşulunu değiştiriyorsa gerekçeyi kaydet, ilgili bölümü güncelle ve değişikliğe karşılıklı gönderme ver.

**Üretilecek kayıt.** Çalışma klasöründe `05_gaye_kaydi.md` dosyasını oluştur. Ortak kayıt bilgilerine ek olarak şu başlıkları kullan: Kaynak soru; Amaç sahipleri; Başarı koşulları; Amaca ulaştıran ilişkiler; Yeterli olmayan göstergeler; Önceki kayıtlarla tutarlılık.

**Tamamlanma koşulu.** Hangi işin, kimin açısından ilerletileceği ve bunun hangi bulguyla değerlendirileceği açık olmalıdır. Teknik ölçütün iyileşmesi, kullanıcı amacına ulaşılmış olduğunun yerine konmamalıdır.

## 6 Kökleşme (Bitiş) Protokolü

**Protokol sorusu:** Bu inceleme sonunda hangi anlayış, hangi dayanaklar ve sınırlar içinde yerleşti? Başlangıçtaki sorular bakımından ne açıklığa kavuştu, ne açık kaldı?

### Açıklamaların bütünleştirilmesi

Kökleşme Protokolü, Varlık, Mekan, Usül, Zaman ve Gaye protokollerinde geliştirilen açıklamaları birbiriyle ilişkilendirerek inceleme çevrimini tamamlar. Her bölümde elde edilen sonuçların aynı konu hakkında tutarlı bir anlayış oluşturup oluşturmadığı değerlendirilir. Bölümler arasındaki bağımlılıklar, kullanılan dayanaklar ve açıklamanın sınırları görünür kılınır. Böylece ortaya çıkan kayıt, sonraki incelemelerde başvurulabilecek bir bütün hâline gelir.

Bu bütünleştirme sırasında, alanın varlığına ilişkin tanımın onun nerede konumlandırıldığını nasıl etkilediği incelenir. Mekânın sınırları, hangi kaynaklara ve ilişkilere bakılacağını belirler; bu kapsam uygulanabilecek usulleri etkiler. Usuller belirli zaman koşullarında işler ve değerleri hizmet ettikleri gayeyle birlikte değerlendirilir. Bir bölümde benimsenen açıklama diğer bölümün koşullarıyla bağdaşmıyorsa, bu uyuşmazlık giderilir veya gerekçesiyle birlikte açık bırakılır.

### Başlangıç sorularına dönüş

Kökleşmenin ilk dayanağı Tohum kaydıdır. Başlangıçtaki her soru, ilgili protokolde ulaşılan açıklamayla karşılaştırılır. Yanıtın hangi kısmının kaynaklara dayandığı, hangi kısmının kavramsal yorum olduğu ve nerelerde yeterli dayanak bulunmadığı belirtilir. Soru inceleme sırasında değişmişse ilk biçimiyle son biçimi arasındaki fark açıklanır. Böylece sonucun hangi soruya yanıt verdiği ve başlangıçtaki ihtiyacı ne ölçüde karşıladığı anlaşılır.

Bu çalışmada bütünleşen anlayış, Bilgi Erişimi ve Arama Sistemleri Mühendisliğini ihtiyaç, içerik, erişim yolları, seçim yöntemleri, zaman koşulları ve kullanım amacı arasındaki ilişkilerle ele almaktır. Bu ilişkileri birlikte taşıyan “makine” için insanlar, kayıtlar, kurallar ve teknik araçlardan oluşan düzenek önerilmiştir. Kökleşme bölümünde bu önerinin nasıl kullanıldığı ve hangi sınırlar içinde açıklayıcı olduğu belirtilir. Öneri, tek bir teknik bileşene veya tek tarihsel kökene ilişkin kesin hükme dönüştürülmez.

Korunacak ayrımlar da son kaydın parçasıdır. İhtiyaç ile sorgu, içeriğin mevcut olması ile bulunabilmesi, benzerlik ile ilgililik, ilgililik ile doğruluk, teknik ölçüm ile görev yararı ve güncellik ile zamansal uygunluk ayrı değerlendirme konularıdır. Kullanıcının amacı, kurumun hedefi ve teknik sistemin optimize ettiği değer de birbirinin yerine geçirilmez. Kökleşme, önceki protokollerde açıklanan bu ayrımların ortak açıklama içinde korunup korunmadığını denetler.

~~~text
  BOLUMLER ARASINDAKI BAGIMLILIK
    varlik tanimi  -->  nerede konumlandirildigi
    mekanin sinirlari  -->  hangi kaynaklara ve iliskilere bakilacagi
                       -->  uygulanabilecek usuller
    usuller  -->  belirli zaman kosullarinda isler
             -->  degerleri hizmet ettikleri gayeyle birlikte
    bagdasmayan aciklama:  giderilir ya da gerekcesiyle acik birakilir

  KORUNACAK AYRIMLAR
    ihtiyac                   =/=  sorgu
    icerigin mevcut olmasi    =/=  bulunabilmesi
    benzerlik                 =/=  ilgililik
    ilgililik                 =/=  dogruluk
    teknik olcum              =/=  gorev yarari
    guncellik                 =/=  zamansal uygunluk
    kullanicinin amaci  =/=  kurumun hedefi  =/=  sistemin optimize
                                                  ettigi deger

  "MAKINE"  insanlar, kayitlar, kurallar ve teknik araclardan olusan
            duzenek
    -/->  tek bir teknik bilesene ya da tek tarihsel kokene iliskin
          kesin hukum
~~~

*Çizim 16 — Kökleşme: bölümler arasındaki bağımlılık; korunacak ayrımlar; makine önerisinin sınırı.*

### Yerleşen anlayışın kullanımı ve sınırları

Bu görevde kökleşmenin somut çıktısı, gerekçeleri izlenebilen bir kavrayış ve onun uygulanabilir kaydıdır. Kaydın daha sonra bir arama sistemini incelemek, yaklaşımları karşılaştırmak veya tasarım sorularını belirlemek için nasıl kullanılabileceği açıklanabilir. Uygulama veya deney yapılmışsa sonuçları kendi kanıtlarıyla ayrıca kaydedilir. Yalnızca önerilmiş bir yönteme dayanılarak gerçekleşmiş başarı iddiası kurulmaz.

Açık meseleler bitiş kaydında korunur. Hangi eksikliğin sonucu sınırladığı, hangi yeni bilginin değerlendirmeyi değiştirebileceği ve hangi sorunun yeni bir inceleme gerektirdiği belirtilir. Yeni kaynaklar veya farklı kullanım koşulları ortaya çıktığında sonuçlar yeniden ele alınabilir. İncelemenin tamamlanması, mevcut çalışmanın ulaştığı noktayı açıkça kaydetmek anlamına gelir.

Kökleşme Protokolü, başlangıç sorularıyla sonuçlar arasında izlenebilir bağ kurulduğunda, belirleyici iddiaların dayanakları gösterildiğinde ve çözülmemiş konular açıklandığında tamamlanır. Son belge ve ona bağlı kayıtlar aynı sürümü temsil etmelidir. Böylece sonraki uygulayıcı, hangi anlayışın yerleştiğini, bu anlayışın nerelerde kullanılabileceğini ve hangi koşullarda gözden geçirilmesi gerektiğini görebilir.

### Masaüstünde uygulama

**Girdiler.** `00_tohum_kaydi.md` ile 01–05 arasındaki kayıtlar, kullanılan kaynaklar ve inceleme sırasında değişen soru ve kararların notları birlikte kullanılır.

1. Başlangıçtaki her soruyu ilgili kayıt ve açıklamaya bağla. Yanıtlandı, kısmen yanıtlandı veya açık durumunu gerekçesiyle belirt. Soru değişmişse ilk ve son biçimini birlikte göster.

2. Varlık, mekân, usul, zaman ve gaye arasındaki ilişkileri birleşik bir metinde açıkla. Çelişen tanım, kapsam, tarih ve amaç kullanımlarını düzelt veya etkileriyle birlikte açık mesele olarak kaydet.

3. Merkezî iddiaların dayanaklarını kontrol et. Kaynak bilgisi, kavramsal yorum, varsayımsal örnek ve yapılmış uygulama ayrımını koru. Kanıtın sınırını aşan sonucu daralt.

4. Yerleşen anlayışı, korunacak temel ayrımları, kullanım sınırlarını ve yeniden inceleme gerektirecek koşulları yaz. Eksik bir bilginin hangi sonucu değiştirebileceğini belirt.

5. Yedi çalışma kaydını 0–6 sırasıyla son belgede birleştir; kaynakçayı ve değişiklik notlarını ekle. Başlıkları, çalışma kimliğini, sürümü, kaynak göndermelerini ve yerel bağlantıları kontrol ederek çevrimin durumunu kaydet.

**Üretilecek kayıt.** Çalışma klasöründe `06_koklesme_kaydi.md` dosyasını oluştur. Ortak kayıt bilgilerine ek olarak şu başlıkları kullan: Başlangıç sorularının karşılığı; Beş boyutun birlikte açıklanması; Yerleşen anlayış ve dayanakları; Korunacak ayrımlar; Açık meseleler ve sınırlar; Yeniden inceleme koşulları; Çevrimin durumu.

Aynı çalışma klasöründe `SON_BELGE.md` dosyasını da oluştur. Bu dosya, yedi çalışma kaydını 0–6 sırasıyla, kullanılan kaynaklar ve değişiklik notlarıyla birlikte içerir.

~~~text
  CALISMA KLASORU  bir cevrimin sonunda
    calismalar/<calisma_kimligi>/
      00_tohum_kaydi.md     ----+
      01_varlik_kaydi.md        |
      02_mekan_kaydi.md         |   0-6 sirasiyla
      03_usul_kaydi.md          +-----------------> SON_BELGE.md
      04_zaman_kaydi.md         |   + kullanilan kaynaklar
      05_gaye_kaydi.md          |   + degisiklik notlari
      06_koklesme_kaydi.md  ----+
    son belge ve ona bagli kayitlar ayni surumu temsil eder

  BASLANGIC SORULARI
    her soru  -->  yanitlandi  |  kismen yanitlandi  |  acik
                   (gerekcesiyle; soru degistiyse ilk ve son bicimi)

  DURUM
    zorunlu bir girdi eksikligi merkezi sonucu engelliyorsa  -->  eksik
    kapsami engellemeyen acik arastirma sorulari gerekceleriyle
    korunarak cevrim tamamlanabilir
    yalnizca onerilmis bir yonteme dayanarak gerceklesmis basari
    iddiasi kurulmaz
~~~

*Çizim 17 — Kökleşme: çalışma kayıtlarından son belgeye; başlangıç sorularının durumu; çevrimin durumu.*

**Tamamlanma koşulu.** Her başlangıç sorusunun karşılığı veya açık kalma gerekçesi gösterilmeli; merkezî sonuçların dayanakları izlenebilmeli; belirleyici çelişkiler ele alınmalıdır. Zorunlu bir girdi eksikliği merkezî sonucu kurmayı engelliyorsa durum eksik kalır. Çalışmanın kapsamını engellemeyen açık araştırma soruları gerekçeleriyle korunarak çevrim tamamlanabilir.

## Kaynaklar

Kaynak numaraları metindeki göndermelerle aynıdır. Başlıkların yanındaki adresler ilgili kaynakları gösterir.

**[1]** Manning, C. D., Raghavan, P. ve Schütze, H. Introduction to Information Retrieval — Boolean retrieval (https://nlp.stanford.edu/IR-book/html/htmledition/boolean-retrieval-1.html). 2008.

**[2]** Manning, C. D., Raghavan, P. ve Schütze, H. Information retrieval system evaluation (https://nlp.stanford.edu/IR-book/html/htmledition/information-retrieval-system-evaluation-1.html). 2008.

**[3]** Belkin, N. J., Oddy, R. N. ve Brooks, H. M. ASK for Information Retrieval Part I Background and Theory (https://scholarship.libraries.rutgers.edu/esploro/outputs/journalArticle/ASK-FOR-INFORMATION-RETRIEVAL-PART-I/991031665289904646). Journal of Documentation, 38(2), 61–71, 1982.

**[4]** Turing, A. M. On Computable Numbers with an Application to the Entscheidungsproblem (https://www.cs.columbia.edu/~tal/3261/Turing_Paper_1936.pdf). 1936.

**[5]** ACM SIGIR AP. Topics of Interest (https://www.sigir-ap.org/). Araştırma alanlarının kapsamı.

**[6]** Cutter, C. A. Rules for a Dictionary Catalogue (https://www.gutenberg.org/cache/epub/59215/pg59215-images.html). Üçüncü baskı, 1891; Objects ve Means bölümleri.

**[7]** Microsoft. Document level access control in Azure AI Search (https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview). Resmî teknik belge.

**[8]** Mooers, C. N. Zatocoding applied to mechanical organization of knowledge (https://onlinelibrary.wiley.com/doi/10.1002/asi.5090020107). American Documentation, 2(1), 20–32, 1951.

**[9]** Manning, C. D., Raghavan, P. ve Schütze, H. Tokenization (https://nlp.stanford.edu/IR-book/html/htmledition/tokenization-1.html). 2008.

**[10]** Vespa. Phased Ranking (https://docs.vespa.ai/en/ranking/phased-ranking.html). Resmî teknik belge.

**[11]** Elastic. Hybrid search (https://www.elastic.co/docs/solutions/search/hybrid-search). Resmî teknik belge.

**[12]** Lewis, P. ve diğerleri. Retrieval Augmented Generation for Knowledge Intensive NLP Tasks (https://arxiv.org/abs/2005.11401). NeurIPS 2020.

**[13]** Manning, C. D., Raghavan, P. ve Schütze, H. Evaluation of unranked retrieval sets (https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-unranked-retrieval-sets-1.html). 2008.

**[14]** Manning, C. D., Raghavan, P. ve Schütze, H. Evaluation of ranked retrieval results (https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-ranked-retrieval-results-1.html). 2008.

**[15]** Meta Engineering. Faiss A library for efficient similarity search (https://engineering.fb.com/2017/03/29/data-infrastructure/faiss-a-library-for-efficient-similarity-search/). 29 Mart 2017; Evaluating similarity search bölümü.

**[16]** Joachims, T. ve diğerleri. Evaluating the Accuracy of Implicit Feedback from Clicks and Query Reformulations in Web Search (https://www.cs.cornell.edu/People/tj/publications/joachims_etal_07a.pdf). ACM Transactions on Information Systems, 25(2), 2007.

**[17]** Bates, M. J. The Design of Browsing and Berrypicking Techniques for the Online Search Interface (https://pages.gseis.ucla.edu/faculty/bates/berrypicking.html). 1989.

**[18]** Manning, C. D., Raghavan, P. ve Schütze, H. Dynamic indexing (https://nlp.stanford.edu/IR-book/html/htmledition/dynamic-indexing-1.html). 2008.

**[19]** Bush, V. As We May Think — Bölüm 6 (https://www.w3.org/History/1945/vbush/vbush6.shtml). The Atlantic Monthly, Temmuz 1945. Bölüm 7 (https://www.w3.org/History/1945/vbush/vbush7.shtml).

**[20]** Upadhyay, S. ve diğerleri. Overview of the TREC 2025 Retrieval Augmented Generation RAG Track (https://trec.nist.gov/pubs/trec34/papers/Overview_rag.pdf). TREC 2025 raporu; 10 Mart 2026 tarihli arXiv sürümü.

**[21]** Microsoft. Agentic retrieval in Azure AI Search (https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview). Resmî teknik belge.

**[22]** Meng, R. ve diğerleri. VLM2Vec V2 Advancing Multimodal Embedding for Videos Images and Visual Documents (https://arxiv.org/abs/2507.04590). 7 Temmuz 2025.

**[23]** NIST. Call for Participation in TREC 2026 (https://trec.nist.gov/cfp.html). AutoJudge dâhil araştırma görevleri.

**[24]** Manning, C. D., Raghavan, P. ve Schütze, H. User utility (https://nlp.stanford.edu/IR-book/html/htmledition/user-utility-1.html). 2008.

# Bilgisayar Ağları Mühendisliği Protokolleri

**Sürüm:** 1.0\
**Tarih:** 31 Ekim 2026 (düzenleme ve tarihsel referans tarihi)\
**Kapsam:** 0–6 protokolleri, düzenlenmiş soru ve yanıt kaydı, masaüstü uygulama yönergeleri ve çalışma kaydı şablonu\
**Belge durumu:** Metin ve uygulama yönergeleri hazır

Bu belge, bilgisayar ağları mühendisliğinin kimliğini, yerini, çalışma biçimini, zamanını ve amacını birbiriyle ilişkili protokoller hâlinde ele alır. Alanın temel işi, fiziksel veya mantıksal olarak ayrı bilgi işlem sistemleri arasındaki iletişimi kurulabilir, sürdürülebilir ve değerlendirilebilir bir hizmete dönüştürmektir. Bu hizmetin teknik taşıyıcısı bilgisayar ağıdır; amaçları, kararları ve sorumlulukları kullanıcılar, mühendisler, işletmeciler ve kurumlar arasındaki ilişkilerde belirlenir.

Başlangıç talimatı şöyledir: “Geçmiş bağlamları buraya taşıma. Burası ile sınırlı kalma.” Bu belgenin dayanağı, bu konuşmada yöneltilmiş sorular ve geliştirilmiş yanıtlardır. Konunun gerektirdiği dış teknik kaynaklar kullanılır; başka konuşmalardaki kabuller kendiliğinden aktarılmaz. Beş özgün soru, ilgili protokolün girişinde korunmuştur.

Beş boyutu birleştiren ortak soru şöyledir: **“Bilgisayar Ağları Mühendisliği’nin; köken aldığı varlık, mekan, usül, zaman, ve gayeyi taşıyan makine kimdir? Kim değildir?”** “Makine”nin insanlar, teknik bileşenler ve kurumsal kurallar arasında kurulmuş örgütlü haberleşme düzeni olarak ele alınması, bu soruya verilen kavramsal yorumdur. Köken, taşıyıcı, fail ve gaye birbirinin yerine kullanılmaz.

Buradaki “protokol”, incelemeyi ve kaydı düzenleyen uygulanabilir yöntemi ifade eder. Teknik olgular, bunlardan geliştirilen kavramsal yorumlar ve insan odaklı amaç önerileri kendi nitelikleri korunarak sunulur. Köşeli kaynak numaraları belgenin sonundaki teknik kaynaklara bağlanır. Metin, soru ve yanıtların paragraf ağırlıklı düzenlenmiş kaydıdır; sözcüğü sözcüğüne konuşma dökümü değildir.

0–6 protokollerinin her biri girdileri, uygulama adımlarını, kayıt çıktısını, tamamlanma ölçütlerini ve geri dönüş koşullarını içerir.

## Masaüstünde kullanım

Bu dosyayı bir Markdown veya metin düzenleyicisinde aç. İlk uygulamada belgenin sonundaki çalışma kaydı şablonunu ayrı bir `CALISMA_KAYDI.md` dosyasına kopyala. Var olan bir çalışma kaydını sürdürüyorsan önce onu oku ve yeni sonuçları aynı kayda işle.

Protokolleri **0 → 1 → 2 → 3 → 4 → 5 → 6** sırasıyla uygula. Tohum başlangıcı kurar; Varlık tanımı, Mekan ilişkileri, Usül yöntemi, Zaman koşulları ve Gaye amaç gerekçesini kaydeder; Kökleşme bunların tutarlılığını ve birlikte ulaştığı sonucu değerlendirir. Bir protokolün geri dönüş koşulu oluştuğunda ilgili kaydı düzelt ve Kökleşme'de değişikliğin etkisini yeniden incele.

Her protokolün açıklama metnini oku, uygulama adımlarının sonuçlarını çalışma kaydındaki ilgili bölüme paragraflarla yaz ve tamamlanma ölçütlerini değerlendir. Durum alanlarında `Başlatılmadı`, `Sürüyor` veya `Tamamlandı` kullan. Bir protokolün ölçütleri karşılandığında durumunu `Tamamlandı` yap ve dayanağını bir paragrafta yaz. Ölçütleri etkileyen bir eksik sürüyorsa durumu `Sürüyor` olarak koru; eksikliği ve gereken sonraki işi açık mesele olarak ayrı kaydet. Boş bir şablon veya tamamlanmış yönerge dosyası, ayrıca yürütülecek bir çalışmanın yapılmış olduğunu göstermez.

Markdown dosyaları kendi başına program çalıştırmaz; insanın veya masaüstü asistanının izleyeceği inceleme ve belgeleme adımlarını taşır. Temel içerik çevrimdışı okunabilir. Dış kaynakların yeniden kontrolü gerektiğinde kaynakçadaki adresler kullanılır. Bu çalışmanın çıktısı kavramsal açıklama ve çalışma kaydıdır; ölçüm ve uygulama sonuçları ancak gerçekten elde edilmişlerse kendi kanıtlarıyla eklenir.

~~~text
  BELGEDEKI UC TUR ICERIK  kendi nitelikleri korunarak sunulur
    teknik olgular           koseli numaralarla kaynaklara baglanir
    kavramsal yorumlar       olgulardan gelistirilir
    insan odakli amac        deger onerisi olarak
    onerileri

  SIRA
    0 --> 1 --> 2 --> 3 --> 4 --> 5 --> 6
    bir protokolun geri donus kosulu olusursa:
      ilgili kayit duzeltilir  -->  Koklesme'de degisikligin etkisi
                                    yeniden incelenir

  DURUM ALANI
    Baslatilmadi  |  Suruyor  |  Tamamlandi  (+ dayanagi yazilir)
    acik meseleler ayri kaydedilir
    bos sablon veya tamamlanmis yonerge dosyasi  -/->  ayrica
    yurutulecek bir calismanin yapilmis olmasi

  MARKDOWN DOSYASI
    kendi basina program calistirmaz; insanin veya masaustu
    asistaninin izleyecegi inceleme ve belgeleme adimlarini tasir
    olcum ve uygulama sonuclari:  yalniz gercekten elde edilmislerse,
    kendi kanitlariyla
~~~

*Çizim 1 — Giriş ve masaüstünde kullanım: belgedeki üç tür içerik; sıra ve geri dönüş; durum alanı; Markdown dosyasının işi.*

## 0 Tohum (Başlangıç) Protokolü

### Amaç ve kapsam

Bu protokol, incelemeyi başlatan soruyu, ihtiyacı ve çalışma sınırlarını açık bir başlangıç kaydına dönüştürür. Varlık, Mekan, Usül, Zaman ve Gaye protokollerinin hangi konuya, hangi amaçla ve hangi koşullarla uygulanacağını belirler. İnsan veya masaüstü asistanı, adımları bir Markdown çalışma kaydı üzerinde yürütür.

Tohum, sonucun önceden kararlaştırılması anlamına gelmez. Başlangıçta bilinenler, varsayılanlar ve henüz açıklığa kavuşmayanlar birbirinden ayrılır. Varlık Protokolü incelenen şeyin ne olduğunu ele alırken Tohum, o şeyin hangi soruyla ve hangi başlangıç koşullarıyla incelemeye alındığını kaydeder.

**Yönlendirici sorular:** Bu inceleme hangi sorudan doğdu? Ne anlaşılmak isteniyor? Hangi girdiler, sınırlar ve açık varsayımlar başlangıcı oluşturuyor? İncelemenin tamamlanması için hangi açıklamalar üretilmeli?

### Girdiler

Konu adı, özgün sorular, başlangıç talimatları ve bu çalışmaya dâhil edilmiş belgeler girdidir. Mevcut yanıtlar, sonraki protokollerde incelenecek başlangıç içeriği olarak kullanılır. Başka oturumlardaki veya projelerdeki kabuller kendiliğinden bu kayda taşınmaz. Konunun gerektirdiği dış kaynaklar, hangi açıklamayı destekledikleri belirtilerek kullanılabilir.

Bu belgede konu **Bilgisayar Ağları Mühendisliği**dir. Başlangıç talimatı “Geçmiş bağlamları buraya taşıma. Burası ile sınırlı kalma.” ifadesidir. İlk soru kümesi alanın varlığını, mekânını, usulünü, zamanını ve gayesini, her birinin ne olmadığıyla birlikte araştırır. Ortak soru şöyledir: “Bilgisayar Ağları Mühendisliği’nin; köken aldığı varlık, mekan, usül, zaman, ve gayeyi taşıyan makine kimdir? Kim değildir?” Beş özgün soru, 1–5 protokollerinin başında korunmuştur.

### Uygulama adımları

1. **Çalışma kaydını aç.** İlk uygulamada belgenin sonundaki şablonu kopyalayarak `CALISMA_KAYDI.md` oluştur. Mevcut kaydı sürdürüyorsan yeni kopya açmadan onu kullan. Konu, tarih, sürüm ve incelemeyi yürüten taraf alanlarını doldur. Yapılan faaliyeti “kavramsal inceleme ve belgeleme” olarak kaydet; farklı bir faaliyet ayrıca yürütülürse onu kendi kanıtıyla belirt.

2. **Özgün soruları kaydet.** Kullanıcının sorularını anlamlarını değiştirmeden `0 Başlangıç Kaydı` bölümüne aktar. Açıklama veya yeniden ifade gerekiyorsa özgün sorudan sonra ayrı bir paragraf yaz. “Neler değildir?” sınır sorularını ve ortak “makine kimdir, kim değildir?” sorusunu koru.

3. **Başlangıç ihtiyacını yaz.** İncelemenin neyi açıklığa kavuşturacağını bir paragrafta belirt. Bu çalışma için ihtiyaç, alanın kimliğini ve beş boyutunu birlikte taşıyan düzeni anlamaktır. Kullanıcının belirtmediği bir amacı ona atfetme. Gerekli bir çalışma yorumu kullanıyorsan yorum olduğunu açıkça göster.

4. **Kapsamı ve önkabulleri ayır.** İncelenen konuyu, başvurulan kaynakları ve kapsam dışındaki işleri kaydet. “Bütün boyutları tek bir varlık taşır” gibi henüz sınanmamış bir kabulü sonuç olarak kullanma. Köken, taşıyıcı, fail ve gaye arasındaki ilişkinin açıklığa kavuşturulacak bir mesele olduğunu koru.

5. **Beş protokolün görevini bağla.** Varlık için tanım ve sınırları, Mekan için yer ve ilişkileri, Usül için işleyiş ve yöntemi, Zaman için tarihsel ve işlemsel koşulları, Gaye için işlev ve amaç gerekçesini beklenen çıktılar olarak yaz. Ortak sorunun bu beş boyutun birlikte okunmasıyla yanıtlanacağını belirt.

6. **Bilgi durumunu belirle.** Teknik olguları, kavramsal yorumları, değer önerilerini ve açık soruları ayırt et. Eksik bilgi yalnız belirli bir açıklamayı etkiliyorsa bu etkiyi o açıklamayla sınırlandırarak ilerle. İncelenecek konuyu veya temel amacı belirlemeyi engelleyen bir eksik varsa, neyin açıklığa kavuşması gerektiğini kaydet; bilmediğin cevabı doldurma.

~~~text
  TOHUM  incelemeyi baslatan soru, ihtiyac ve calisma sinirlari
    -->  acik bir baslangic kaydi
    tohum  -/->  sonucun onceden kararlastirilmasi
    ayrilir:  bilinenler  |  varsayilanlar  |  henuz acikliga
                                               kavusmayanlar

  BES PROTOKOLDEN BEKLENEN
    1 Varlik   tanim ve sinirlar
    2 Mekan    yer ve iliskiler
    3 Usul     isleyis ve yontem
    4 Zaman    tarihsel ve islemsel kosullar
    5 Gaye     islev ve amac gerekcesi
    ortak soru  -->  bu bes boyutun birlikte okunmasiyla yanitlanir

  BILGI DURUMU
    teknik olgu  |  kavramsal yorum  |  deger onerisi  |  acik soru
    eksik bilgi yalniz belirli bir aciklamayi etkiliyorsa
      -->  etkisi o aciklamayla sinirlanir; ilerlenir
    konuyu veya temel amaci belirlemeyi engelliyorsa
      -->  neyin acikliga kavusmasi gerektigi kaydedilir
    bilinmeyen cevap doldurulmaz
~~~

*Çizim 2 — Tohum: başlangıç kaydı; beş protokolden beklenen; bilgi durumu.*

### Kayıt ve çıktı

Çıktı, `CALISMA_KAYDI.md` içindeki **0 Başlangıç Kaydı**dır. Konu, özgün sorular, başlangıç ihtiyacı, kapsam, kaynak durumu, önkabuller ve açık meseleler burada bulunur. Sonraki protokoller kendi açıklamalarını bu başlangıca bağlayabilmelidir. Çalışmayı devralan bir kişi, yalnız bir başkasının hatırladığı konuşma ayrıntılarına ihtiyaç duymadan başlangıcı anlayabilmelidir.

### Tamamlanma ölçütü

- [ ] Konu, başlangıç ihtiyacı ve özgün sorular kaydedildi.
- [ ] Kapsam, önkabuller ve açık meseleler birbirinden ayrıldı.
- [ ] 1–5 protokollerinden beklenen açıklamalar belli.

Bu ölçütler karşılandığında durum alanını `Tamamlandı` yap ve dayanağını bir paragrafta yaz. Sonuçların henüz bilinmemesi Tohum'un tamamlanmasını engellemez. Ölçütleri etkileyen bir eksik sürüyorsa durumu `Sürüyor` olarak koru.

### Açık meseleler ve geri dönüş

Konu, temel soru, kapsam veya inceleme amacı değişirse Tohum'a dön. Değişikliğin nedenini ve sonraki protokollere etkisini kaydet. Yalnız bir teknik ayrıntı veya ifade düzeltiliyorsa başlangıcın tamamını yeniden kurma; ilgili protokolü güncelle.

## 1 Varlık Protokolü

### Amaç ve kapsam

Bu protokol, bilgisayar ağları mühendisliğinin tanımını, ayırt edici ilişkilerini ve sınırlarını açık bir varlık kaydına dönüştürür. İncelenen alan, onu gerçekleştiren teknik düzenek ve amaç belirleyen failler ayrı ayrı tanımlanır. Mevcut açıklamaları değerlendirirken parçanın bütünün yerine geçirilmesini önler.

**Özgün sorular:** Nedir? Onu o yapan nelerdir? Neler değildir?

### Girdiler

0 Başlangıç Kaydı, özgün sorular, aşağıdaki mevcut soru ve yanıt kaydı ve kullanılan teknik kaynaklar girdidir. Başlangıç kaydındaki konu ve kapsam esas alınır; başka bir alanın tanımı bu alana kendiliğinden taşınmaz.

### Mevcut soru ve yanıt kaydı

#### Tanım ve ayırt edici özellikler

Bilgisayar ağları mühendisliği, fiziksel veya mantıksal olarak ayrı çalışan bilgi işlem sistemlerinin belirlenmiş koşullar altında haberleşmesini sağlayan altyapıları tasarlama, gerçekleştirme, işletme ve doğrulama disiplinidir. Merkezindeki soru, iletişimin nasıl mümkün olduğu ve hangi koşullarda sürdürülebildiğidir. Kimlerin haberleşebileceği, hangi yolların kullanılacağı, hangi performans ve güvenlik koşullarının bekleneceği, arızaların nasıl karşılanacağı ve değişen ihtiyaçlara nasıl uyarlanılacağı birlikte değerlendirilir.

Alanı belirleyen mühendislik nesnesi, işletilebilir bir haberleşme düzenidir. Cihazlar, iletim ortamları, yazılımlar, protokoller, adresler, erişim kuralları ve işletim süreçleri bu düzenin parçalarıdır. Bütünün davranışı, parçaların tek tek durumlarından ibaret değildir. Bir cihazın çalışması, kullanıcının hizmete ulaşabildiğini kanıtlamaz. Paketler ulaşabilir fakat uygulamanın kullanamayacağı kadar geç gelebilir; bir hizmet erişilebilir olabilir fakat erişmemesi gereken kişilerce de kullanılabilir. “Ağ çalışıyor” yargısı, kimin hangi işi hangi koşullarda yapabildiğiyle tamamlanır.

~~~text
  TANIM
    fiziksel veya mantiksal olarak ayri calisan bilgi islem
    sistemlerinin belirlenmis kosullar altinda haberlesmesini saglayan
    altyapilari tasarlama . gerceklestirme . isletme . dogrulama

  MUHENDISLIK NESNESI  isletilebilir bir haberlesme duzeni
    cihazlar . iletim ortamlari . yazilimlar . protokoller .
    adresler . erisim kurallari . isletim surecleri
    butunun davranisi  -/->  parcalarin tek tek durumlarindan ibaret

    bir cihazin calismasi  -/->  kullanicinin hizmete ulasabildigi
    paketler ulasabilir    ama uygulamanin kullanamayacagi kadar gec
    hizmet erisilebilir    ama erismemesi gereken kisilerce de

  "Ag calisiyor"  -->  kimin hangi isi hangi kosullarda yapabildigiyle
                       tamamlanir
~~~

*Çizim 3 — Varlık: tanım; işletilebilir haberleşme düzeni; bütünün davranışı ile parçaların durumu.*

Buradaki bilgisayar, masaüstü cihazlarla sınırlı değildir. Sunucular, telefonlar, sensörler, sanal makineler ve başka bilgi işlem bileşenleri haberleşmenin tarafı olabilir. Kamu İnterneti kadar özel, yerel veya belirli bir amaçla sınırlandırılmış ağlar da alanın kapsamındadır. RFC 8799, sınırlı ağ bölgelerinin farklı yönetim, güvenlik ve davranış gereksinimleri taşıyabileceğini ele alır. [2]

Alanı ayırt eden ilk koşul, ayrı çalışan taraflar arasında ortak davranış kurulmasıdır. Fiziksel bağlantı tek başına anlaşılabilir haberleşme sağlamaz. İletilerin nasıl oluşturulacağı, hedeflerin nasıl belirtileceği, hangi durumda ne yapılacağı ve hataların nasıl ele alınacağı ortak kurallara bağlıdır. Protokoller bu davranışları tanımlar. İletişim böylece hem maddi bir gerçekleşmeye hem de kurallarla düzenlenmiş bir işleyişe dayanır.

İkinci koşul, yerel durum ile uçtan uca sonuç arasındaki farktır. Bir bileşenin gördüğü bilgiler sınırlıdır; kullanıcının deneyimi ise birçok bileşenin birlikte davranışından doğar. Bazı doğruluk, bütünlük ve güvenlik işlevleri iletişimin uçlarının katılımını gerektirir. RFC 1958'in ele aldığı uçtan uca yaklaşım, ağ içindeki düzenlemelerin uygulamanın bütün sorumluluğunu kendiliğinden üstlenemeyeceğini gösterir. [1]

Üçüncü koşul, sınırlı kaynakların paylaşılmasıdır. İletim kapasitesi, işlem gücü, kuyruk alanı, enerji, bütçe ve bakım zamanı sınırlıdır. Bir akışın daha fazla kaynak kullanması başka akışların koşullarını değiştirebilir. Bir hizmete öncelik vermek, diğer ihtiyaçların ne ölçüde bekleyebileceğini de değerlendirmeyi gerektirir. Mühendislik, birden fazla ihtiyacın birlikte karşılanabileceği koşulları kurar.

Dördüncü koşul, kısmi arıza ve belirsizliktir. Ağın bir bölümü çalışırken başka bir bölümü erişilemez olabilir. Aynı sorun farklı uçlardan farklı görünebilir. Gecikmiş bir yanıt ile hiç gelmeyecek bir yanıtı ayırt etmek gözlem ve zaman gerektirir. Bu nedenle tasarım, normal çalışma kadar arıza kapsamını, hizmet üzerindeki etkiyi ve toparlanma biçimini de içerir.

Beşinci koşul, davranış hakkında gerekçeli ve sınanabilir sorumluluk alınmasıdır. Bir düzenin bir kez çalışması ile belirlenmiş koşullarda çalışmasını beklemek için yeterli gerekçe bulunması farklıdır. Varsayımların, ölçümlerin, tasarım kararlarının ve başarısızlık koşullarının açıklanması bu sorumluluğun parçasıdır. Tasarım, ölçme ve güvenilirlik başka mühendisliklerde de bulunur; alanın özgünlüğü bunların ayrı bilgi işlem sistemleri arasındaki iletişim ilişkisi çevresinde birleşmesidir.

~~~text
  ALANI AYIRT EDEN BES KOSUL
    1  ortak davranis      fiziksel baglanti tek basina anlasilabilir
                           haberlesme saglamaz; protokoller davranisi
                           tanimlar
    2  yerel durum ile     bir bilesenin gordugu bilgiler sinirli;
       uctan uca sonuc     kullanicinin deneyimi bircok bilesenin
                           birlikte davranisindan dogar  [1]
    3  sinirli kaynaklar   iletim kapasitesi . islem gucu . kuyruk
                           alani . enerji . butce . bakim zamani
    4  kismi ariza ve      bir bolum calisirken baska bolum
       belirsizlik         erisilemez; gecikmis yanit mi, hic
                           gelmeyecek yanit mi?  -->  gozlem ve zaman
    5  gerekceli ve        bir kez calismasi  =/=  belirlenmis
       sinanabilir         kosullarda calismasini beklemek icin
       sorumluluk          yeterli gerekce

  OZGUNLUK
    tasarim, olcme ve guvenilirlik baska muhendisliklerde de var;
    burada ayri bilgi islem sistemleri arasindaki iletisim iliskisi
    cevresinde birlesirler
~~~

*Çizim 4 — Varlık: alanı ayırt eden beş koşul.*

#### Köken, taşıyıcı ve fail

Köken, bir şeyin ortaya çıkmasını mümkün kılan koşulları; taşıyıcı, somut olarak gerçekleştiği yapıyı; fail, onu kuran, değiştiren veya işleten tarafı; gaye ise istenen sonucun gerekçesini ifade eder. Bu ilişkilerin tamamının tek bir varlıkta birleşmesi zorunlu değildir. Mühendis bir ağı tasarlayabilir fakat fizik yasalarını, bütün teknik birikimi veya insanların iletişim ihtiyacını kendisi meydana getirmez. Ağ da iletişimi gerçekleştirebilir fakat bu iletişimin neden gerekli veya haklı olduğunu yalnızca paket ileterek açıklayamaz.

Bu beş boyutu birlikte taşıyan “makine” için önerilen kavramsal karşılık, belirli iletişim amaçları doğrultusunda kurulmuş örgütlü haberleşme sistemidir. Teknik çekirdeği bilgisayar ağıdır. Amaç ve sorumluluk tarafında insanlar ile kurumsal ilişkiler bulunur. Bu açıklama, ağın insan gibi bir özne olduğunu veya insanın bütünüyle bir makineye indirgenebileceğini ileri sürmez.

Bilgisayar ağı, mühendisliğin hem üzerinde çalıştığı nesne hem de ürettiği sonuçlardan biridir. Ağlardan edinilen deneyim mühendislik bilgisini değiştirir. İnternet mimarisinin tek bir büyük plandan çıkmak yerine evrimsel biçimde geliştiğini belirten RFC 1958, bu karşılıklı gelişime teknik tarih açısından bir dayanak sağlar. [1] Bileşenlerin değişmesine rağmen hizmetin sürdürülebilmesi, düzenin kimliğinin tek tek cihazlarda bulunmadığını gösterir. Aynı cihazların farklı kurallarla işletilmesi de farklı iletişim düzenleri ortaya çıkarabilir.

#### Alanın ve taşıyıcının sınırları

Kablo çekmek, cihaz kurmak, yapılandırmak ve arıza gidermek alanın gerçek parçalarıdır; hiçbiri bütünü tek başına tanımlamaz. Bir üreticinin komutlarına hâkim olmak veya belirli bir sertifikaya sahip olmak da bütün iletişim sistemini değerlendirme yeteneğiyle özdeş değildir. Matematiksel bir grafiği incelemek yararlı araçlar sağlayabilir fakat tek başına işletilebilir bir bilgisayar ağı kurmak anlamına gelmez.

Haberleşme ve telekomünikasyon mühendisliği ile iletim altyapılarında, yazılım mühendisliği ile ağ yazılımları ve otomasyonda, dağıtık sistemlerle haberleşme ve kısmi arızada, siber güvenlikle erişim ve korunmada, sistem işletimiyle süreklilik ve değişiklik yönetiminde kesişir. Bu sınırlar kesin duvarlar değildir. Bununla birlikte ağ mühendisliği bütün yazılımı, güvenliği veya dağıtık hesaplamayı kapsayan bir alan olarak tanımlanamaz.

Taşıyıcı makine tek başına bilgisayar, yönlendirici, anahtar, protokol, İnternet veya ağ mühendisi değildir. Bunların her biri belirli bir işlevi veya rolü taşır. “İnsan” cevabı amaç ve sorumluluğu gösterir fakat alanın özgüllüğünü tek başına açıklamaz. Özgüllük, insanların ayrı bilgi işlem sistemleri arasında yönetilebilir iletişim kurması ve bu iletişimin sonuçlarını sınamasındadır.

~~~text
  DORT ILISKI  tek bir varlikta birlesmeleri zorunlu degil
    koken       bir seyin ortaya cikmasini mumkun kilan kosullar
    tasiyici    somut olarak gerceklestigi yapi
    fail        onu kuran, degistiren veya isleten taraf
    gaye        istenen sonucun gerekcesi

  "MAKINE"  onerilen kavramsal karsilik
    belirli iletisim amaclari dogrultusunda kurulmus orgutlu
    haberlesme sistemi
      teknik cekirdek       bilgisayar agi
      amac ve sorumluluk    insanlar ve kurumsal iliskiler
    -/->  ag insan gibi bir ozne
    -/->  insan butunuyle bir makineye indirgenebilir

  AG VE MUHENDISLIK
    muhendislik  --- uretir --->  bilgisayar agi
         ^                              |
         '--- edinilen deneyim ---------'
    bilesenler degisir, hizmet surer  -->  kimlik tek tek cihazlarda
                                           bulunmaz
    ayni cihazlar, farkli kurallar  -->  farkli iletisim duzenleri

  TEK BASINA TASIYICI MAKINE DEGIL
    bilgisayar . yonlendirici . anahtar . protokol . Internet . ag
    muhendisi:  her biri belirli bir islevi veya rolu tasir
    "insan":  amac ve sorumlulugu gosterir; alanin ozgullugunu tek
    basina aciklamaz
~~~

*Çizim 5 — Varlık: köken, taşıyıcı, fail ve gaye; makine için önerilen karşılık; ağ ile mühendislik; taşıyıcının sınırları.*

### Uygulama adımları

1. **Tanımı yaz.** Alanı bir paragrafta tanımla. Tanımda ayrı bilgi işlem sistemleri, haberleşme düzeni, belirlenmiş koşullar ve tasarlama, işletme, doğrulama sorumluluğu arasındaki ilişkiyi kur. Sonucu 1 Varlık Kaydı bölümüne yaz.

2. **Ayırt edici özellikleri gerekçelendir.** Ortak kurallar, sınırlı kaynaklar, yerel durum ile uçtan uca sonuç farkı ve kısmi arıza koşullarının neden birlikte ele alındığını açıkla. Başka mühendisliklerle paylaşılan bir niteliği yalnız bu alana özgüymüş gibi sunma.

3. **Köken, taşıyıcı ve faili ayır.** Köken, taşıyıcı, fail ve gaye terimlerini kendi anlamlarıyla kaydet. Bilgisayar ağını teknik taşıyıcı; kullanıcı, mühendis ve işletmeci rollerini amaç, karar ve sorumluluk ilişkileri içinde ele al. Tek bir varlığın bütün rolleri zorunlu olarak taşıdığını varsayma.

4. **Sınırları yaz.** Bilgisayar, yönlendirici, protokol, İnternet, mühendis ve insanın hangi rolü açıkladığını; neden tek başına bütün açıklamanın yerine geçemediğini paragraflarla belirt. Komşu alanlarla kesişimi koru.

5. **Tanımı bir örnekle sına.** Aynı cihazların farklı kurallarla işletildiği veya cihazlar değişirken hizmetin sürdüğü varsayımsal bir örnek üzerinden tanımın neyi koruduğunu göster. Örneği yapılmış bir deney gibi kaydetme. Gerekirse tanımı düzelt.

### Kayıt ve çıktı

Çıktı, `CALISMA_KAYDI.md` içindeki 1 Varlık Kaydıdır. Tanım, ayırt edici özelliklerin gerekçesi, köken–taşıyıcı–fail–gaye ayrımı, sınırlar ve açıklayıcı örnek burada bulunur. Mekan ve Usül protokolleri bu tanımı kullanır.

### Tamamlanma ölçütü

- [ ] Tanımın nesnesi ve kapsamı açık.
- [ ] Parçalar, bütün, köken, taşıyıcı ve fail birbirinin yerine kullanılmıyor.
- [ ] Nedir ve neler değildir soruları gerekçeli paragraflarla yanıtlandı.

### Açık meseleler ve geri dönüş

Tanım sonraki bölümlerde anlatılan faaliyetleri veya sınırları açıklayamıyorsa bu protokole dön. Konunun kendisi değişiyorsa önce Tohum kaydını güncelle.

## 2 Mekan Protokolü

### Amaç ve kapsam

Bu protokol, alanın maddi, mantıksal, örgütsel ve işlevsel yerini açıklığa kavuşturur. Bağlantı, erişim, güven, yetki ve bağımsızlık ilişkilerinin aynı sınırı ifade edip etmediğini inceler. Çıktı, tek bir adres veya cihaz odasıyla sınırlı olmayan, kapsamı belirli bir mekân açıklamasıdır.

**Özgün sorular:** Nerededir? Bu yeri, oraya has bir yer yapan nelerdir? Neler değildir?

### Girdiler

0 Başlangıç Kaydı, 1 Varlık Kaydı ve aşağıdaki mevcut soru ve yanıt kaydı girdidir. Belirli bir ağ ortamına ilişkin bilgi verilmişse yalnız mevcut ve doğrulanabilir özellikleri kullan; böyle bir ortam verilmemişse kavramsal düzeyde çalış.

### Mevcut soru ve yanıt kaydı

#### Maddi, mantıksal, örgütsel ve işlevsel yer

Bilgisayar ağları mühendisliği maddi olarak bakır kabloda, fiberde, elektromanyetik ortamda, ağ arayüzlerinde, cihazlarda, veri merkezlerinde ve bunların enerji altyapısında bulunur. Mesafe, iletim ortamı ve ortak altyapı bağımlılıkları iletişimin gerçekleşme koşullarını etkiler. Bir topoloji çizgisinin karşılığı, işletilmesi gereken maddi bir bağlantıdır.

Mantıksal olarak adresler, isimler, yollar, erişim ilişkileri ve ağ bölümleri arasında yer alır. Aynı fiziksel sunucuda çalışan iki sanal sistem birbirinden yalıtılabilir. Farklı şehirlerdeki iki sistem ortak bir özel iletişim düzeninin parçası olabilir. Fiziksel yakınlık, mantıksal yakınlık ve erişilebilirlik birbirinin yerine kullanılamaz.

Örgütsel olarak kullanıcılar, kurumlar, sağlayıcılar, ekipler ve sorumluluk alanları arasındadır. Bir bağlantının iki ucunda farklı işletmeciler bulunabilir. Sorunu çözmek için gereken bilgi ile değişiklik yapma yetkisi aynı tarafta olmayabilir. İşlevsel olarak ise eğitim, araştırma, üretim veya başka bir hizmetin, ayrı sistemler arasında haberleşme gerektiren bölümünde bulunur.

Bu yeri ayırt eden özellik, farklı sınırların aynı yerden geçmemesidir. Binanın sınırı ağın sınırı olmayabilir; ağın sınırı yetki sınırıyla örtüşmeyebilir; kurumun sorumluluk alanı uygulamanın bütün bağımlılıklarını kapsamayabilir. Bir tarafın yerel kararı, başka bir tarafın iletişim olanağını değiştirebilir. Ağ mühendisliği bu bağımlılıkları görünür kılar ve ilgili sorumluluk alanları arasında ilişki kurar.

~~~text
  DORT YER
    maddi       bakir kablo . fiber . elektromanyetik ortam . ag
                arayuzleri . cihazlar . veri merkezleri . enerji
    mantiksal   adresler . isimler . yollar . erisim iliskileri . ag
                bolumleri
    orgutsel    kullanicilar . kurumlar . saglayicilar . ekipler .
                sorumluluk alanlari
    islevsel    bir hizmetin ayri sistemler arasinda haberlesme
                gerektiren bolumu

    ayni fiziksel sunucuda iki sanal sistem  -->  yalitilabilir
    farkli sehirlerde iki sistem  -->  ortak ozel iletisim duzeni
    fiziksel yakinlik =/= mantiksal yakinlik =/= erisilebilirlik

  FARKLI SINIRLAR AYNI YERDEN GECMEZ
      +----------- bina -----------+
      |                            |
      |       +----------------------- ag ---------+
      |       |                    |               |
      +-------|--------------------+               |
              |          +----------- yetki -------|------+
              |          |                         |      |
              +----------|-------------------------+      |
                         +--------------------------------+
    kurumun sorumluluk alani  -/->  uygulamanin butun bagimliliklari
    bir tarafin yerel karari  -->  baska bir tarafin iletisim
                                   olanagini degistirebilir
~~~

*Çizim 6 — Mekan: dört yer; aynı yerden geçmeyen sınırlar.*

#### Erişim, güven ve bağımsızlık

Bir kullanıcının kurum binasında bulunması, bütün kaynaklara erişmesi gerektiğini göstermez. Uzakta bulunması da bütün erişimlerden dışlanması için tek başına yeterli bir gerekçe değildir. NIST SP 800-207, fiziksel veya ağ konumunun kendiliğinden güven vermek için yeterli olmadığını belirtir. Nereden bağlanıldığı, varlığın kime ait olduğu, neye ulaşılabildiği ve neye ulaşmaya izin verildiği ayrı sorulardır. [4]

Yolların değerlendirilmesinde de coğrafi mesafe tek ölçüt değildir. Alanlar arası yönlendirmede ulaşılabilirlik bilgisiyle birlikte işletmecilerin uyguladığı politikalar rol oynar. BGP, ağ ulaşılabilirlik bilgisinin değişimini ve belirli politika kararlarının uygulanmasını destekler. Bu nedenle ağın mekânı kilometrelerin yanı sıra bağlantılar, geçişler, bağımlılıklar ve yetkilerle tanımlanır. [3]

Yedeklilik örneği bu farkı somutlaştırır. İki ayrı bağlantı satın alınmış olsa bile iki fiber aynı yeraltı kanalından geçiyorsa tek bir kazı ikisini birlikte etkileyebilir. Çizimde iki yol bulunması, fiziksel olarak bağımsız iki arıza yolu bulunduğunu kanıtlamaz. RFC 4202'nin ortak risk bağlantı grubu kavramı, bir kaynağın arızasının birden fazla bağlantıyı birlikte etkileyebildiği bu tür durumları ifade eder. [5]

~~~text
  AYRI SORULAR  [4]
    nereden baglanildigi?           varligin kime ait oldugu?
    neye ulasilabildigi?            neye ulasmaya izin verildigi?
    kurum binasinda bulunmak  -/->  butun kaynaklara erisim
    fiziksel veya ag konumu   -/->  kendiliginden guven

  YOLLAR  [3]
    cografi mesafe tek olcut degil:  ulasilabilirlik bilgisi ve
    isletmecilerin politikalari (BGP)

  YEDEKLILIK ORNEGI  [5]
    cizimde
                      .----- baglanti 1 -----.
                 A ---+                      +--- B
                      '----- baglanti 2 -----'
    yerde
                      .1-.                .-1.
                 A ---+  +== ayni yeralti ==+  +--- B
                      '2-'      kanali      '-2'
                                   ^
                                   |  tek bir kazi ikisini birlikte
                                      etkileyebilir
    cizimde iki yol  -/->  fiziksel olarak bagimsiz iki ariza yolu
    ortak risk baglanti grubu:  bir kaynagin arizasi birden fazla
    baglantiyi birlikte etkileyebilir
~~~

*Çizim 7 — Mekan: erişim ve güven için ayrı sorular; yollar; yedeklilik örneği.*

#### Makinenin mekânı ve kapsamı

Örgütlü haberleşme sistemi, ayrı taraflar arasında hangi sınırların aşılabileceğini ve hangi sınırların korunacağını düzenleyerek mekânı taşır. Fiziksel konumun üzerine mantıksal bir erişim düzeni kurulur. Bu düzenin ayrıca bir yetki boyutu vardır: Bir yere teknik olarak ulaşabilmek, oraya ulaşma hakkı bulunduğu anlamına gelmez. Makinenin mekânı böylece hem bağlantıların hem de sınırların mekânıdır.

İnsanları ve kurumları bu açıklamaya dâhil etmek, bütün toplumu aynı makinenin parçası saymayı gerektirmez. İncelenen sistemin sınırı, belirli bir iletişim hizmetini üretmek, sürdürmek ve değiştirmekle doğrudan ilgili bileşenler, aktörler ve kurallarla çizilir. Daha geniş tarihsel ve toplumsal koşullar etkili olabilir; etkileyen her şeyin sistemin doğrudan parçası kabul edilmesi açıklamanın kesinliğini azaltır.

#### Mekânın yanlış özdeşleştirmeleri

Bu yer yalnızca cihaz odası değildir; önemli bir davranış erişim kuralında veya yazılımla üretilmiş yapılandırmada belirlenebilir. Yalnızca ekrandaki topoloji de değildir; enerji, kablo güzergâhı, sağlayıcı ve işletim bağımlılıkları çizimde görünmeyebilir. Bulut kullanımı da fiziksel gerçekleşme koşullarını kaldırmaz; kullanıcının gördüğü denetim ve soyutlama biçimini değiştirir.

Ağın uygulamalarla iç içe bulunması, her uygulama sorununun ağ sorunu olduğunu göstermez. Bir işlemin yavaşlığı istemciden, veritabanından veya iletişim yolundan kaynaklanabilir. Ağ mühendisliğinin görevi kendisine sınırsız sorumluluk atfetmek değil, iletişimin sonuçtaki payını gözlemle belirlemek ve diğer sorumluluk alanlarıyla ilişkilendirmektir. Bu protokolde korunan temel ayrım, görünür yakınlık veya ayrılıkla gerçek erişim, yetki ve bağımsızlık arasındaki farktır.

~~~text
  MAKINENIN MEKANI  baglantilarin ve sinirlarin mekani
    fiziksel konum
      + mantiksal erisim duzeni
      + yetki boyutu:  teknik olarak ulasabilmek  -/->  ulasma hakki

  SISTEMIN SINIRI
    +----------------------------------------------------------+
    | belirli bir iletisim hizmetini uretmek, surdurmek ve     |
    | degistirmekle dogrudan ilgili bilesenler, aktorler ve    |
    | kurallar                                                 |
    +----------------------------------------------------------+
      disarida:  daha genis tarihsel ve toplumsal kosullar
                 (etkili olabilir; dogrudan parca sayilmaz)

  YANLIS OZDESLESTIRMELER
    cihaz odasi     onemli bir davranis erisim kuralinda veya
                    yazilimla uretilmis yapilandirmada belirlenebilir
    ekrandaki       enerji, kablo guzergahi, saglayici ve isletim
    topoloji        bagimliliklari cizimde gorunmeyebilir
    bulut           fiziksel gerceklesme kosullarini kaldirmaz;
                    denetim ve soyutlama bicimini degistirir

  "YAVAS"  istemci?  veritabani?  iletisim yolu?
    -->  iletisimin sonuctaki payi gozlemle belirlenir
~~~

*Çizim 8 — Mekan: makinenin mekânı; sistemin sınırı; yanlış özdeşleştirmeler.*

### Uygulama adımları

1. **Dört yer düzeyini açıkla.** Maddi ortamı, mantıksal erişim düzenini, örgütsel sorumlulukları ve hizmet içindeki işlevsel yeri ayrı paragraflarla 2 Mekan Kaydı bölümüne yaz.

2. **Sınırları karşılaştır.** Fiziksel yakınlık, teknik erişilebilirlik, güven ve erişim hakkının hangi gerekçelerle birbirinden ayrıldığını göster. Aynı binada olma ile yetki sahibi olmayı özdeşleştirme.

3. **Bağımlılıkları belirle.** Görünürde ayrı olan yolların ortak ortam, enerji, sağlayıcı veya işletim bağımlılığı taşıyıp taşımayacağını değerlendir. Kullanılan örnek veya kaynak ile gerçek ortam gözlemini açıkça ayır.

4. **Sistem kapsamını çiz.** Belirli iletişim hizmetini üretmek, sürdürmek ve değiştirmekle doğrudan ilgili bileşen ve rolleri kaydet. Etkili olan bütün toplumsal koşulları sistemin doğrudan parçası ilan etme.

5. **Kapsam dışını ve bağlantıları yaz.** Alanın neden yalnız cihaz odası, topoloji çizimi veya bulut ifadesiyle tanımlanamayacağını açıkla. Uygulama sorununun ağla ilişkisini kurmak için hangi ek bilginin gerektiğini, varsa açık meseleye yaz.

### Kayıt ve çıktı

Çıktı, `CALISMA_KAYDI.md` içindeki 2 Mekan Kaydıdır. Dört yer düzeyi, erişim ve yetki ayrımları, bağımlılıklar ve sistem sınırı burada bulunur. Usül Protokolü bu kapsamı, Gaye Protokolü ise sorumluluk ve etkilenen taraflar bilgisini kullanır.

### Tamamlanma ölçütü

- [ ] Maddi, mantıksal, örgütsel ve işlevsel yerler birbirleriyle ilişkili biçimde açıklandı.
- [ ] Erişim, güven, yetki ve gerçek bağımsızlık ayrıştırıldı.
- [ ] Sistem kapsamı ve kapsam dışı unsurlar gerekçelendirildi.

### Açık meseleler ve geri dönüş

Yeni bir bağımlılık, yetki sınırı veya yer bilgisi ortaya çıkarsa Mekan kaydını güncelle. Değişiklik temel varlık tanımını etkiliyorsa Varlık Protokolüyle birlikte değerlendir.

## 3 Usül Protokolü

### Amaç ve kapsam

Bu protokol, ağ mühendisliğinin ihtiyacı nasıl teknik koşullara çevirdiğini, nasıl gerçekleştirme ve doğrulama yöntemi kurduğunu açıklar. Makinenin çalışma kuralları ile mühendisin bu kuralları seçme, düzenleme ve sınama yöntemlerini birbirinden ayırır. Masaüstündeki uygulama, bu ilişkinin incelenmesi ve kaydedilmesidir.

**Özgün sorular:** Nasıl işler yapar? Bu yaptıklarını, ona has yapan nelerdir? Neler değildir?

### Girdiler

0–2 kayıtları, mevcut gereksinimler ve aşağıdaki soru ve yanıt kaydı girdidir. Ölçüm veya uygulama sonucu verilmişse kaynağıyla kullanılır. Sonuç bulunmayan yerde hangi doğrulamanın gerektiği yazılır; yapılmış sonuç üretilmez.

### Mevcut soru ve yanıt kaydı

#### İhtiyacın mühendislik koşullarına çevrilmesi

Bilgisayar ağları mühendisliği, bir ihtiyacı çalışır ve sürdürülebilir bir iletişim düzenine dönüştürür. Bu dönüşüm ihtiyacın anlaşılmasıyla başlar. “Ağ hızlı olsun” ifadesi, hangi kullanıcıların hangi işi hangi yoğunlukta yapacağı ve hangi gecikme veya kesintinin kabul edileceği açıklanmadan yeterli bir gereksinim oluşturmaz.

Aktarım hızı, gecikme, gecikme değişkenliği ve paket kaybı farklı özelliklerdir. Trafik mühendisliği bunları kaynakların güvenilir ve ekonomik kullanımıyla birlikte değerlendirir. Kullanıcının gördüğü hizmet davranışı temel ölçüttür. [6] Bir üniversitede büyük araştırma verilerinin aktarımıyla canlı derslerin iletişim ihtiyacı farklı olabilir. İkisinin iyi çalışması istenir fakat başarı ölçütleri ayrı ayrı belirlenmelidir.

İhtiyaçların teknik koşullara çevrilmesini model ve mimari kurma izler. Hangi uçların haberleşeceği, trafiğin nereden nereye akacağı, hangi bölümlerin yalıtılacağı, hangi bileşenin ortak bağımlılık oluşturduğu, büyümenin nerede beklendiği ve arızada hangi yolun kullanılacağı kararlaştırılır. Bu sorular topoloji, adresleme, yönlendirme, kapasite, güvenlik ve yedeklilik kararlarına dönüşür.

Graf modelleri bağlantıları ve yolları düşünmeye, kuyruk modelleri yük altında beklemeyi anlamaya, olasılık ve istatistik ise değişkenliği değerlendirmeye yardımcı olur. Bir modelin değeri, gerçek sistem hakkında hangi varsayımları yaptığı bilindiğinde ortaya çıkar. Model, gerçekliğin bütün ayrıntılarını içerdiği varsayılan bir kopya olarak kullanılamaz.

~~~text
  IHTIYACTAN KOSULA
    "Ag hizli olsun"  -->  aciklanmadan yeterli gereksinim degil:
      hangi kullanicilar?  hangi is?  hangi yogunluk?
      hangi gecikme veya kesinti kabul edilir?
    farkli ozellikler  [6]
      aktarim hizi . gecikme . gecikme degiskenligi . paket kaybi
    temel olcut:  kullanicinin gordugu hizmet davranisi
    ornek, bir universite:
      buyuk arastirma verilerinin aktarimi  |  basari olcutleri
      canli derslerin iletisim ihtiyaci     |  ayri ayri belirlenir

  MODEL VE MIMARI
    hangi uclar haberlesecek? . trafik nereden nereye akacak? .
    hangi bolumler yalitilacak? . ortak bagimlilik nerede? . buyume
    nerede? . arizada hangi yol?
      -->  topoloji . adresleme . yonlendirme . kapasite . guvenlik .
           yedeklilik
    graf modelleri            baglantilar ve yollar
    kuyruk modelleri          yuk altinda bekleme
    olasilik ve istatistik    degiskenlik
    model  -/->  gercekligin butun ayrintilarini icerdigi varsayilan
                 bir kopya
~~~

*Çizim 9 — Usül: ihtiyaçtan teknik koşula; model ve mimari.*

#### Gerçekleştirme, doğrulama ve işletim

Tasarım, cihazlar, sanal ağ bileşenleri, protokol ayarları, erişim kuralları ve otomasyon aracılığıyla çalışan mekanizmalara dönüştürülür. Paketleri ileten işlevler, yolları ve iletim kararlarını oluşturan denetim işlevleri, sistemi yapılandıran ve izleyen yönetim işlevleri ayrıştırılarak incelenebilir. Bunlar aynı cihazda bulunabilir veya farklı bileşenlere dağılabilir. RFC 9232 de ağ telemetrisinde iletme, denetim ve yönetim düzlemlerinden bilgi edinmeyi ayrı ayrı ele alır. [7]

Yapılandırmanın cihaz tarafından kabul edilmesi, hizmetin istenen biçimde çalıştığını kanıtlamaz. Doğrulama başlangıçtaki gereksinimlere döner. İzin verilen iletişimin gerçekleşmesi, engellenmesi gereken iletişimin engellenmesi, yük altında davranış, seçilmiş arıza koşullarındaki etki ve değişikliğin geri alınabilirliği incelenir. Amaç bütün olası koşullarda mutlak güvence vermek değil, sınanan koşulları, kalan varsayımları ve kabul edilen riski açıklamaktır.

İşletim, tasarımın sürekliliğidir. Kullanıcı sayısı, uygulamalar, trafik düzeni ve yapılandırmalar değiştikçe çalışan ağın durumu tasarım belgesindeki durumdan farklılaşabilir. Gözlenen davranış ile beklenen davranış karşılaştırılır, ölçümler yeni kararları besler ve değişiklikler kaydedilir. Arızadan sonra hizmetin geri getirilmesiyle birlikte aynı koşul tekrarlandığında ne olacağı da değerlendirilir.

Kapasite artırımı, geçişler, bileşen yenileme, gereksiz yapıların kaldırılması ve dokümantasyon yaşam döngüsünün parçalarıdır. İyi bir tasarımın değeri, ilk kurulumunun kolaylığıyla sınırlı değildir. Sistemi daha sonra devralan kişilerin neden böyle kurulduğunu anlayabilmesi ve değiştirebilmesi de önemlidir.

~~~text
  ISLEVLER  ayristirilarak incelenebilir  [7]
    iletme      paketleri ileten islevler
    denetim     yollari ve iletim kararlarini olusturan islevler
    yonetim     sistemi yapilandiran ve izleyen islevler
    ayni cihazda bulunabilir veya farkli bilesenlere dagilabilir

  DOGRULAMA  baslangictaki gereksinimlere doner
    yapilandirmanin cihazca kabul edilmesi  -/->  hizmetin istenen
                                                  bicimde calismasi
    incelenir:
      izin verilen iletisim gerceklesiyor mu?
      engellenmesi gereken iletisim engelleniyor mu?
      yuk altinda davranis . secilmis ariza kosullarindaki etki .
      degisikligin geri alinabilirligi
    amac:  mutlak guvence degil; sinanan kosullar, kalan varsayimlar
           ve kabul edilen risk aciklanir

  ISLETIM  tasarimin surekliligi
    gozlenen davranis  <-- karsilastirilir -->  beklenen davranis
    olcumler  -->  yeni kararlar;  degisiklikler kaydedilir
    yasam dongusu:  kapasite artirimi . gecisler . bilesen yenileme .
    gereksiz yapilarin kaldirilmasi . dokumantasyon
~~~

*Çizim 10 — Usül: iletme, denetim ve yönetim işlevleri; doğrulama; işletim.*

#### Makinenin usulü ve mühendisliğin usulü

Makinenin çalışma usulü, iletilerin nasıl oluşturulacağı, taşınacağı, değerlendirileceği veya reddedileceği gibi kurallarda bulunur. Mühendisliğin usulü ise bu kuralların belirli bir amaç için nasıl seçileceği, bir araya getirileceği, sınanacağı ve değiştirileceğiyle ilgilidir. Protokol, koşullar altında davranışı tanımlar; protokolün o kullanım için uygunluğunu değerlendirmek ayrıca muhakeme gerektirir.

Bu işleri ayırt eden özellik, yerel müdahale ile dağıtılmış sonuç arasındaki ilişkinin kurulmasıdır. Tek noktada yapılan bir değişiklik birçok kullanıcıya ve hizmete yayılabilir. Bir uçta görülen sorun yolun başka bir bölümünden doğabilir. Bir hizmeti iyileştiren ayar başka bir hizmetin koşullarını bozabilir. Mühendis belirtilerden nedenlere ilerler ve yaptığı müdahalenin bütün üzerindeki etkisini gözlemle sınar.

Bu nedenle “yavaş” şikâyeti hemen “kapasite yetersiz” diye çevrilemez. Nerede bekleme oluştuğu, hangi akışların etkilendiği ve sorunun hangi koşullarda görüldüğü araştırılır. Örneğin kuyruklar kısa trafik patlamalarını karşılamaya yardımcı olurken aşırı kuyruk birikmesi gecikmeyi artırabilir. Daha büyük tamponlar her durumda daha iyi deneyim üretmez; RFC 7567 kuyruk yönetimini bu problem çerçevesinde ele alır. [8]

Benzer biçimde yeni bir yedeklilik mekanizması bazı arızalara karşı koruma sağlarken ek işletim karmaşıklığı getirebilir. Korunan arızalarla oluşan yeni bağımlılıklar birlikte değerlendirilir. RFC 3439, büyük ağların tasarımında karmaşıklığın maliyet ve güvenilirlik üzerindeki etkisini vurgular. [9]

#### Failler ve yöntemsel sınırlar

Kullanıcı ihtiyacı ortaya koyar; mühendis onu teknik koşullara çevirir; işletmeci sürekliliği ve değişiklikleri üstlenir; karar verici kaynaklar ve kabul edilecek koşullar hakkında yetki kullanır. Bu roller tek kişide birleşebilir veya birçok kişi ve kuruma dağılabilir. Mühendis pasif bir uygulayıcı değildir. Belirsiz bir gereksinimi açıklığa kavuşturabilir, istenen yöntemin amaca hizmet etmeyeceğini gösterebilir ve seçenek geliştirebilir.

Usul, gerekçesi bilinmeyen komutları uygulamakla tamamlanmaz. Komutun doğruluğu kadar içinde kullanıldığı bağlamın doğruluğu da gerekir. Her sorunu yeni cihazla veya daha fazla kapasiteyle çözmeye çalışmak, darboğazın gerçek yeri anlaşılmadığında sorunu başka bir noktaya taşıyabilir.

Otomasyon kararları hızlı, tutarlı ve geniş ölçekte uygulayabilir; yanlış kararları da aynı biçimde çoğaltabilir. Bu nedenle otomatik işlem ile doğrulanmış amaç arasındaki bağ korunmalıdır. Alan yalnızca arıza çıktığında yapılan müdahalelerden oluşmaz. Arızanın etkisini sınırlayan, teşhisini kolaylaştıran ve oluşma ihtimalini azaltan çalışmaların önemli bir bölümü sorun görünmeden önce yapılır.

~~~text
  IKI USUL
    makinenin usulu        iletilerin olusturulmasi, tasinmasi,
                           degerlendirilmesi veya reddedilmesi
    muhendisligin usulu    bu kurallarin belirli bir amac icin
                           secilmesi, bir araya getirilmesi,
                           sinanmasi ve degistirilmesi
    protokol davranisi tanimlar; o kullanim icin uygunlugu ayrica
    muhakeme gerektirir

  YEREL MUDAHALE, DAGITILMIS SONUC
    tek noktada degisiklik  -->  bircok kullanici ve hizmet
    bir ucta gorulen sorun  <--  yolun baska bir bolumu
    "yavas"  -/->  "kapasite yetersiz"
      nerede bekleme? . hangi akislar? . hangi kosullarda?
    kuyruk  [8]
      kisa trafik patlamasi     [####      ]  karsilamaya yardimci olur
      asiri kuyruk birikmesi    [##########]  gecikmeyi artirabilir
      daha buyuk tampon  -/->  her durumda daha iyi deneyim

  ROLLER  tek kiside birlesebilir veya bircok kisiye dagilabilir
    kullanici       ihtiyaci ortaya koyar
    muhendis        teknik kosullara cevirir; pasif uygulayici degil
    isletmeci       surekliligi ve degisiklikleri ustlenir
    karar verici    kaynaklar ve kabul edilecek kosullar hakkinda yetki
    otomasyon:  hizli, tutarli, genis olcekte; yanlis kararlari da ayni
    bicimde cogaltabilir
~~~

*Çizim 11 — Usül: iki usul; yerel müdahale ve dağıtılmış sonuç; kuyruk; roller.*

### Uygulama adımları

1. **İhtiyacı sınanabilir koşullara çevir.** Bir hizmet ihtiyacını seç veya mevcut kavramsal örneği kullan. Kullanıcı, iş, yük ve beklenen hizmet davranışını 3 Usül Kaydı içinde açıkla. Sayısal hedef verilmemişse hedef değeri icat etme; belirlenmesi gereken ölçütü yaz.

2. **Yöntem sırasını kur.** İhtiyacın anlaşılması, model ve mimari, gerçekleştirme, doğrulama, işletim ve yenileme arasındaki ilişkiyi paragraflarla belirt. Her faaliyetin hangi girdiyi kullandığını ve hangi sonucu ürettiğini açıkla.

3. **İki usul düzeyini ayır.** Protokol ve algoritmaların makinenin davranışını nasıl düzenlediğini; mühendislik muhakemesinin bunların uygunluğunu nasıl değerlendirdiğini göster. Komut bilgisi ile gerekçeli karar verme arasındaki farkı koru.

4. **Doğrulama planını yaz.** İzin verilen ve engellenmesi gereken iletişim, yük, arıza ve değişiklik geçişi için hangi gözlemin hangi soruyu yanıtlayacağını belirt. Yerel değişikliğin diğer hizmetlere etkisini nasıl değerlendireceğini açıkla. Planı gerçekleşmiş test olarak sunma.

5. **Sorumluluk ve sınırları kaydet.** Kullanıcı, mühendis, işletmeci ve karar verici rollerini belirt. Otomasyonun hangi kararı uyguladığını ve bu kararın doğruluğunun nasıl sınanacağını açıkla. Yalnız kapasite artırmanın veya arıza gidermenin neden bütün yöntemin yerine geçmediğini yaz.

### Kayıt ve çıktı

Çıktı, `CALISMA_KAYDI.md` içindeki 3 Usül Kaydıdır. İhtiyaç, yöntem ilişkileri, makine ve mühendislik usulleri, doğrulama planı ve roller burada bulunur. Gerçekleştirilmiş işlemler varsa ayrı kanıtlarıyla, önerilen işlemler ise plan olarak kaydedilir.

### Tamamlanma ölçütü

- [ ] İhtiyaç ile teknik koşullar ve yöntem arasında izlenebilir ilişki kuruldu.
- [ ] Makinenin usulü ile mühendisliğin usulü ayrıldı.
- [ ] Doğrulama planı, mevcut kanıt ve yapılmamış işlemler birbirine karıştırılmadı.

### Açık meseleler ve geri dönüş

Yöntem hedeflenen davranışı açıklamıyorsa Usül kaydını düzelt. Yeni bir yöntem sistem sınırını değiştiriyorsa Mekan'a; tanımı değiştiriyorsa Varlık'a dön.

## 4 Zaman Protokolü

### Amaç ve kapsam

Bu protokol, tarihsel anı, sistemin çalışma sürelerini ve yaşam döngüsünü birlikte kaydeder. Güncel iddiaların hangi tarihe ait olduğunu, bilginin zamanında ulaşmasının anlamını ve değişim sırasında hizmetin nasıl değerlendirileceğini açıklığa kavuşturur.

**Özgün sorular:** Hangi andadır? Bu anı, diğer zamanlardan farklı yapan nelerdir? Neler değildir?

### Girdiler

0–3 kayıtları, mevcut kaynakların yayın ve olay tarihleri ile aşağıdaki soru ve yanıt kaydı girdidir. Kaydedilmiş anlatının referans tarihi 31 Ekim 2026'dır. Daha sonraki bir uygulamada değişebilir iddialar yeni kaynaklarla kontrol edilir; eski kayıt tarihinden koparılarak güncelmiş gibi kullanılmaz.

### Mevcut soru ve yanıt kaydı

#### Tarihsel an

Bilgisayar ağları mühendisliğinin zamanı tarihsel gelişim, çalışmanın zaman ölçekleri ve hizmetin yaşam döngüsü birlikte ele alınarak anlaşılır. Alanın hangi anda olduğu, yalnız takvimdeki konumuyla veya kullanılan en yeni ürünle belirlenemez. Geçmiş tasarımların etkileri, mevcut ihtiyaçlar ve geleceğe yönelik varsayımlar aynı sistem içinde bulunur.

31 Ekim 2026 itibarıyla belirgin yönelimlerden biri, ağın tamamında istenen davranışı tanımlamak, bunu otomasyonla gerçekleştirmek ve gerçekleşmeye devam ettiğini ölçmektir. Bu, her ağda tamamlanmış tek biçimli bir dönüşüm olarak görülmemelidir. Farklı ağlar farklı ihtiyaç, altyapı ve olgunluk düzeylerinde bulunur.

Amaç temelli ağ yönetiminde istenen sonuç tanımlanır, sonucun hangi yapılandırmalarla gerçekleştirileceği çözümlenir ve zaman içindeki uygunluğu izlenir. RFC 9315, kendi kendini yönetmesi amaçlanan bir ağın bile işletmeciden veya dış sistemlerden amaç ve yönlendirme almaya ihtiyaç duyduğunu açıklar. Bu yaklaşım, mühendislik sorumluluğunu ortadan kaldırmak yerine amaçların ifade edilmesine, otomatik kararların sınanmasına ve sonuçların denetlenmesine ağırlık verir. [10]

Telemetri, gözlemi yönetim kararlarına bağlar. Verinin üretilmesi, toplanması, ilişkilendirilmesi ve kullanılması sayesinde ağın nasıl davrandığı değerlendirilir. Değeri, çok sayıda sayıyı göstermekten çok, hizmeti anlamaya ve kararları buna göre değiştirmeye katkısındadır. RFC 9232 bu geri bildirimi otomatik yönetim ve amaçlara uygunluğun izlenmesiyle ilişkilendirir. [7]

Güvenin yalnız mekânsal bir çevreye dayandırılmaması da güncel bağlamın bir parçasıdır. Uzak kullanıcılar ve kurumun ağ sınırları dışındaki kaynaklar, erişilebilirlik ile güven ilişkisinin ayrıca ele alınmasını gerektirir. NIST SP 800-207'nin 2020 tarihli çerçevesi, bu yönelimin 2026'da birden ortaya çıkmadığını da gösterir. [4]

Yeni hesaplama iş yükleri iletişim tasarımını etkiler. Yapay zekâ, ağ yönetiminde kullanılabilecek bir araç olmasının yanında, büyük dağıtık hesaplama sistemlerinde ağın hizmet verdiği bir iş yüküdür. Ultra Ethernet Consortium'un 12 Ekim 2026 tarihli 1.1 spesifikasyon duyurusu, yapay zekâ ve yüksek başarımlı hesaplama için programlanabilir tıkanıklık yönetimi, tıkanıklık sinyallemesi ve bazı kolektif işlemlerin ağ içinde gerçekleştirilmesi gibi işlevleri açıklar. Bu bir konsorsiyum spesifikasyonu örneğidir; yayımlanması bütün ağların bu biçime dönüştüğünü veya bu işlevlerin her yerde kullanıldığını kanıtlamaz. [11]

~~~text
  BELIRGIN YONELIMLERDEN BIRI  31 Ekim 2026 itibariyla
    istenen davranisi     otomasyonla          gerceklesmeye devam
    tanimlamak       -->  gerceklestirmek -->  ettigini olcmek
    her agda tamamlanmis tek bicimli bir donusum degil

  AMAC TEMELLI YONETIM  [10]
    istenen sonuc      hangi yapilandirmalarla     zaman icindeki
    tanimlanir    -->  gerceklesecegi         -->  uygunlugu izlenir
         ^             cozumlenir                        |
         '-----------------------------------------------'
    kendi kendini yonetmesi amaclanan ag da isletmeciden veya dis
    sistemlerden amac ve yonlendirme alir
    sorumluluk kalkmaz:  amaclarin ifadesi . otomatik kararlarin
    sinanmasi . sonuclarin denetlenmesi
  TELEMETRI  [7]
    gozlem  -->  yonetim kararlari; degeri cok sayida sayi gostermekte
    degil, hizmeti anlamaya katkisinda

  METINDEKI TARIHLER
    2020 ------------------------------ 12 Ekim 2026 --- 31 Ekim 2026
    NIST SP 800-207                     Ultra Ethernet   referans
    guvenin yalniz mekansal bir         Consortium 1.1   tarihi
    cevreye dayandirilmamasi            duyurusu
    duyurunun yayimlanmasi  -/->  butun aglarin bu bicime donustugu
~~~

*Çizim 12 — Zaman: güncel yönelim; amaç temelli yönetim; telemetri; metindeki tarihler.*

#### Çalışmanın farklı zamanları

Bir ağ, paketlerin işlenmesi ve iletilmesi, denetim mekanizmalarının uyumu, günlük işletim ve kapasite planlaması gibi farklı zaman ölçeklerinde çalışır. Kısa süreli bir trafik olayı denetim mekanizmasını etkileyebilir; olayın tekrarlanması uzun vadeli kapasite kararına dönüşebilir. RFC 9522, paket işleme düzeyinden günler ve yıllar ölçeğindeki kapasite yönetimine uzanan bu zamanları birlikte ele alır. [6]

Bilginin değeri varış zamanına bağlı olabilir. Bir arşiv aktarımının biraz geç tamamlanmasıyla gerçek zamanlı bir kontrol iletisinin geç ulaşması aynı sonucu doğurmaz. Ağ mühendisliği, bilginin yalnız ulaşıp ulaşmadığını değil, işlevini koruyacak zamanda ulaşıp ulaşmadığını da değerlendirir. Bazı kontrollü ağlarda belirli akışların gecikmesine üst sınır koymak tasarım hedefidir. DetNet mimarisi, sınırları tanımlanmış yönetim alanları içinde bu gereksinime yönelik bir örnektir. [12]

Makine, zamanı davranışının bir koşulu olarak taşır. İletim, bekleme, zaman aşımı, arızanın fark edilmesi ve yeni duruma uyum bu koşulu somutlaştırır. Her işlemin yalnız sonucu değil, gerçekleşme sırası ve süresi de değerlendirmeye girer. Böylece zaman, dışarıdan eklenen bir tarih bilgisinden daha fazlasıdır; sistemin işlevinin bir parçasıdır.

~~~text
  ZAMAN OLCEKLERI  [6]
    paketlerin       denetim            gunluk        kapasite
    islenmesi ve     mekanizmalarinin   isletim       planlamasi
    iletilmesi       uyumu                            (gunler, yillar)
        |                 |                |               |
    ----+-----------------+----------------+---------------+------->
    kisa sureli trafik olayi  -->  denetim mekanizmasini etkileyebilir
    olayin tekrarlanmasi      -->  uzun vadeli kapasite karari

  VARIS ZAMANI
    arsiv aktariminin biraz        =/=   gercek zamanli kontrol
    gec tamamlanmasi                     iletisinin gec ulasmasi
    ulasmak  =/=  islevini koruyacak zamanda ulasmak
    DetNet  [12]  sinirlari tanimlanmis yonetim alanlari icinde
                  belirli akislarin gecikmesine ust sinir

  MAKINEDE ZAMAN  davranisinin bir kosulu
    iletim . bekleme . zaman asimi . arizanin fark edilmesi . yeni
    duruma uyum
    degerlendirmeye girer:  her islemin sonucu, gerceklesme sirasi ve
    suresi
~~~

*Çizim 13 — Zaman: zaman ölçekleri; varış zamanı; makinede zaman.*

#### Yaşam döngüsü ve geçiş

Tasarım sırasında gelecekteki yük ve arızalar hakkında varsayımlar yapılır. İşletim bunların gerçek koşullarda sınandığı süreçtir. Bir değişiklik sırasında ise eski durumdan yeni duruma geçişin kendisi mühendislik problemi olur. Son durumda doğru olacak bir yapılandırma, uygulanırken kabul edilemez bir kesintiye yol açabilir. Başlangıç ve bitiş durumları kadar aradaki davranışın da tasarlanması gerekir.

Sistemin tarihsel zamanı, kullanılan protokollerde, mevcut altyapıda, dokümantasyonda ve işletim alışkanlıklarında bulunur. Yeni tasarım çoğu zaman çalışan bir düzenin içinde gerçekleştirilir. Bu nedenle ağın şimdisi, geçmiş kararların yürürlükte olduğu ve gelecekteki davranışın yeniden belirlendiği andır. Bu ifade, teknik örneklerden geliştirilen kavramsal bir yorumdur.

#### Zamanın yanlış özdeşleştirmeleri

Bu an, bütün ağların otonomlaştığı ve insan kararına gerek kalmadığı bir an değildir. Fiziksel iletimin, protokol bilgisinin veya arıza analizinin önemini yitirdiği bir aşama da değildir. Yeni araçlar, iletişimin temel koşullarını ve sorumluluk ihtiyacını ortadan kaldırmaz.

Ağ mühendisliği yalnız arıza çıktığında başlayan veya kurulum tamamlanınca sona eren bir faaliyet olarak tanımlanamaz. Tasarım, işletim ve değişim aynı hizmetin farklı zamanlardaki mühendisliğidir. Bu protokolde korunan ayrım, bilginin ulaşmasıyla zamanında ulaşması ve doğru son durumla yönetilebilir geçiş süreci arasındaki farktır.

~~~text
  GECIS  kendisi bir muhendislik problemi
    eski durum  ======= gecis =======>  yeni durum
                          ^
                          |  son durumda dogru olacak bir yapilandirma
                             uygulanirken kabul edilemez bir kesintiye
                             yol acabilir
    tasarlanir:  baslangic . bitis . aradaki davranis

  AGIN SIMDISI  kavramsal yorum
    gecmis kararlarin yururlukte oldugu  +  gelecekteki davranisin
                                            yeniden belirlendigi an
    tasarimdaki varsayimlar  -->  isletimde gercek kosullarda sinanir

  BU AN DEGIL
    x  butun aglarin otonomlastigi ve insan kararina gerek kalmadigi an
    x  fiziksel iletimin, protokol bilgisinin veya ariza analizinin
       onemini yitirdigi asama
  BU FAALIYET DEGIL
    x  yalniz ariza ciktiginda baslayan
    x  kurulum tamamlaninca sona eren
    tasarim, isletim ve degisim:  ayni hizmetin farkli zamanlardaki
    muhendisligi
~~~

*Çizim 14 — Zaman: geçiş; ağın şimdisi; bu anın ve bu faaliyetin ne olmadığı.*

### Uygulama adımları

1. **Tarihsel referansı kaydet.** İncelemenin tarihini ve kullanılan kaynakların hangi dönemi açıkladığını 4 Zaman Kaydı içine yaz. Olay tarihi, yayın tarihi ve kendi inceleme tarihini ayrı tut.

2. **Güncel yönelimleri sınırlandır.** Otomasyon, telemetri, güven yaklaşımı ve hesaplama iş yüklerine ilişkin açıklamaların kapsamını belirt. Bir spesifikasyon duyurusunu bütün ağlarda gerçekleşmiş yaygın uygulama olarak sunma.

3. **Çalışma sürelerini ilişkilendir.** Paket iletimi, denetim ve uyum, işletim ve kapasite yaşam döngüsünün farklı zamanlarını açıkla. Birindeki olayın diğerini nasıl etkileyebileceğini bir örnekle göster.

4. **Zamanında olmayı değerlendir.** Bilginin ulaşması ile işlevini koruyacak zamanda ulaşması arasındaki farkı yaz. Belirli gecikme garantileri söz konusuysa hangi alan ve koşullarda geçerli olduklarını belirt.

5. **Geçiş ve yeniden değerlendirmeyi yaz.** Doğru son durumun yanında geçiş sırasının nasıl ele alınacağını açıkla. Geçmiş varsayımların hangi yeni yük, arıza veya kaynak bilgisiyle yeniden sınanacağını kaydet.

### Kayıt ve çıktı

Çıktı, `CALISMA_KAYDI.md` içindeki 4 Zaman Kaydıdır. Referans tarihleri, tarihsel yönelimlerin kapsamı, çalışma süreleri, geçiş koşulları ve yeniden kontrol gerektiren iddialar burada bulunur.

### Tamamlanma ölçütü

- [ ] Tarihsel açıklamalar kendi tarih ve kapsamlarıyla kaydedildi.
- [ ] İletim zamanı, uyum, işletim ve yaşam döngüsü arasındaki ilişki açıklandı.
- [ ] Zamanında ulaşma ile ulaşma ve son durum ile geçiş süreci ayrıldı.

### Açık meseleler ve geri dönüş

Yeni bir tarih, kaynak, iş yükü veya geçiş koşulu açıklamayı etkiliyorsa Zaman kaydını yeniden değerlendir. Bu değişikliğin Usül ve Gaye üzerindeki etkisini de belirt.

## 5 Gaye Protokolü

### Amaç ve kapsam

Bu protokol, teknik işlevi, hizmet edilen işi ve nihai amaç gerekçesini ayrı düzeylerde ele alır. Başarı ölçütlerinin kimin hangi işine hizmet ettiğini ve değere ilişkin tercihlerin nasıl gerekçelendirildiğini açıklar. Hız veya kapasite gibi araçsal hedeflerin kendiliğinden nihai amaç sayılmasını önler.

**Özgün sorular:** Hangi nihai amaca hizmet eder? Bu nihai amaca ulaştıran nelerdir? Neler değildir?

### Girdiler

0–4 kayıtları, ifade edilmiş kullanıcı ihtiyaçları, rol ve sorumluluk bilgileri ile aşağıdaki soru ve yanıt kaydı girdidir. Kullanıcının veya kurumun belirtmediği amaçlar onlara atfedilmez; çalışma içindeki değer önerileri kendi nitelikleriyle yazılır.

### Mevcut soru ve yanıt kaydı

#### Teknik işlev, hizmet edilen iş ve nihai amaç

Bilgisayar ağları mühendisliğinin doğrudan teknik işlevi, belirlenen taraflar arasında belirlenen koşullarda veri iletişimi sağlamaktır. Hizmet ettiği iş bağlama göre eğitim, araştırma, üretim, haberleşme, eğlence veya kamu hizmeti olabilir. Nihai amaç sorulduğunda teknik tanımın ötesinde, hangi sonucun neden değerli görüldüğünü açıklayan bir değerlendirmeye geçilir.

Doğa yasaları bir ağın hangi insani amaç için kurulması gerektiğini söylemez. Aynı teknik yetenek farklı ve birbiriyle çatışan amaçlarda kullanılabilir. İnsan odaklı bir mühendislik anlayışında savunulabilecek nihai amaç, insanların ve kurumların ayrı yerlerde ve sistemlerde bulunmalarına rağmen haklarına ve ihtiyaçlarına uygun biçimde güvenilir, sürdürülebilir ve hesap verilebilir ortak işler yapabilmesidir. Bu, bütün ağların fiilen benimsediği amaç olduğu iddiası değil, başarıyı değerlendirmek için önerilen normatif ölçüttür.

Internet Architecture Board'un RFC 8890 belgesi, IETF kararlarında son kullanıcıların çıkarlarına öncelik verilmesini savunur. Ağın büyüklüğü, bant genişliği ve gecikmesi gibi ölçülebilir başarıların tek başına yeterli amaç oluşturmadığını belirtir. Bu, teknik bir topluluğun açıkladığı insan odaklı değer tercihidir. [13]

~~~text
  UC DUZEY
    teknik islev         belirlenen taraflar arasinda belirlenen
                         kosullarda veri iletisimi
          |
          v  hizmet ettigi is
    hizmet edilen is     egitim . arastirma . uretim . haberlesme .
                         eglence . kamu hizmeti
          |
          v  nihai amac sorulunca
    degerlendirme        hangi sonuc neden degerli gorulur?

    doga yasalari  -/->  bir agin hangi insani amac icin kurulmasi
                         gerektigi
    ayni teknik yetenek  -->  farkli ve catisan amaclarda
                              kullanilabilir

  ONERILEN NORMATIF OLCUT  butun aglarin fiili amaci oldugu iddiasi
                           degil
    insanlarin ve kurumlarin ayri yerlerde ve sistemlerde
    bulunmalarina ragmen haklarina ve ihtiyaclarina uygun bicimde
    guvenilir, surdurulebilir ve hesap verilebilir ortak isler
    yapabilmesi
    RFC 8890  [13]  son kullanicilarin cikarlarina oncelik; buyukluk,
                    bant genisligi ve gecikme tek basina yeterli amac
                    degil
~~~

*Çizim 15 — Gaye: üç düzey; önerilen normatif ölçüt.*

#### Gayenin makinede temsil edilmesi

Gaye, teknik sistemde hedeflere ve kısıtlara çevrilerek temsil edilir. “Araştırma ekipleri birlikte çalışabilsin” amacı; kaynaklara erişim, yeterli aktarım kapasitesi, süreklilik koşulları ve yetki kuralları biçiminde ağ düzenine yansır. Bu çeviri, amacın bütün anlamını tüketmez. Araştırmanın neden yapılacağı veya kimin yararına olduğu kapasite değerinden çıkarılamaz.

Bir hedefi gerçekleştirmek ile o hedefi gerekçelendirmek ayrı işlerdir. Otomatik bir sistem verilen ölçütlere göre yol seçebilir, kaynak ayırabilir veya yapılandırma değiştirebilir. Bu işlemsel yetenek, nihai amacın neden doğru olduğuna ilişkin normatif yetkiyle aynı değildir. RFC 9315, otomatik yönetilen sistemlerin amaç ve yönlendirme girdisine ihtiyaç duyduğunu açıklar. [10] Amaç gerçekleştirme ile amacın normatif gerekçesi arasındaki ayrım ise burada geliştirilen kavramsal yorumdur.

Kullanıcı, mühendis, işletmeci, karar verici ve sonuçlardan etkilenen kişi aynı taraf olmayabilir. Amaçları da tamamen örtüşmeyebilir. Mühendislik, farklı beklentilerin teknik sonuçlarını görünür kılar. Bir hedefi koyma yetkisi, onun kendiliğinden haklı olduğunu kanıtlamaz; sonuçlardan etkilenenlerin çıkarları da değerlendirmeye dâhil edilmelidir.

~~~text
  AMACIN TEMSILI
    "Arastirma ekipleri birlikte calisabilsin"
       -->  kaynaklara erisim . yeterli aktarim kapasitesi .
            sureklilik kosullari . yetki kurallari
    ceviri  -/->  amacin butun anlami
    arastirmanin neden yapilacagi, kimin yararina oldugu
       -/->  kapasite degerinden cikarilir

  AYRI ISLER
    bir hedefi gerceklestirmek  =/=  o hedefi gerekcelendirmek
    otomatik sistem:  yol secer . kaynak ayirir . yapilandirma
    degistirir
    islemsel yetenek  =/=  normatif yetki
    otomatik yonetilen sistemler amac ve yonlendirme girdisine ihtiyac
    duyar [10]; bu ayrim ise metnin kendi kavramsal yorumudur

  TARAFLAR  ayni olmayabilir; amaclari tamamen ortusmeyebilir
    kullanici . muhendis . isletmeci . karar verici . sonuclardan
    etkilenen kisi
    hedef koyma yetkisi  -/->  hedefin hakliligi
    sonuclardan etkilenenlerin cikarlari da degerlendirmeye girer
~~~

*Çizim 16 — Gaye: amacın teknik temsili; gerçekleştirmek ile gerekçelendirmek; taraflar.*

#### Amaca ulaştıran koşullar

İlk koşul, kullanıcının gerçekten hangi işi yapmaya çalıştığının anlaşılmasıdır. Bir üniversitede bağlantı kapasitesi satın alınması tek başına amacı gerçekleştirmez. Öğrencinin derse katılabilmesi, araştırmacının veriye erişebilmesi ve kurumun hizmetlerini sürdürebilmesi gerekir. Teknik başarı, hizmet edilen işle ilişkisi içinde değerlendirilir.

İkinci koşul, gereksinime uygun yeterliliktir. Her hizmet aynı performans veya dayanıklılık düzeyine ihtiyaç duymaz. Kaynaklar sağladıkları yarar, önledikleri kayıp ve getirdikleri işletim yüküyle birlikte düşünülür. Yetersiz kapasite kadar gereksiz karmaşıklık da amaca zarar verebilir. İlk günkü çalışmanın yanında gelecekteki değişimlere açıklık ve farklı bileşenlerin birlikte çalışabilirliği önemlidir.

Güvenlik ile kullanılabilirlik birlikte ele alınmalıdır. Gerekli iletişim mümkün olmalı; yetkisiz veya zarar verici iletişim sınırlandırılmalıdır. Bazı bağlantıların kurulmasını önlemek de hizmetin doğru gerçekleştirilmesinin parçası olabilir. Gözlenebilir ve düzeltilebilir davranış ise sorunun anlaşılmasını, etkisinin sınırlanmasını ve gerektiğinde değişiklik yapılmasını sağlar. Toplanan bilginin amaca uygunluğu, mahremiyet ve işletim yükü bakımından ölçülülüğü korunmalıdır.

Açık sorumluluk ve bilgi aktarımı, hizmeti sürdürülebilir kılar. Sistemin neden böyle kurulduğu, hangi koşullarda çalışmasının beklendiği ve sorun hâlinde kimin ne yapacağı anlaşılmalıdır. Süreklilik, yalnız bir kişinin hatırladığı ayrıntılara bağımlı bırakılmamalıdır. Bu koşulların ortak işlevi, teknik düzeni hizmet ettiği işle ilişki içinde tutmaktır.

#### Amaç yerine geçirilemeyecek ölçütler

En yüksek hız kendi başına nihai amaç değildir. İhtiyacın ötesindeki kapasite başka bir yarar sağlamıyorsa başarı ölçütü olarak sınırlı kalır. Sıfır kesinti söylemi de hangi arızalara karşı, hangi kapsamda, hangi maliyetle ve hangi toparlanma koşullarıyla süreklilik beklendiği açıklanmadan yeterli bir mühendislik hedefi oluşturmaz.

Herkesin her şeye erişmesi, bütün bağlamlar için uygun amaç değildir. Haklar, görevler ve güvenlik gereksinimleri erişimi sınırlamayı gerektirebilir. En düşük satın alma maliyeti de işletim yükü, kesinti etkisi, bakım ve gelecekteki değişikliklerden ayrı değerlendirilemez. Teknik olarak etkileyici fakat kullanıcı işini güçleştiren veya sürdürülmesi zor bir mimari, kendi inceliğiyle gerekçelendirilemez.

~~~text
  AMACA ULASTIRAN KOSULLAR
    1  kullanicinin gercekten hangi isi yapmaya calistigi
       baglanti kapasitesi satin almak  -/->  amaci gerceklestirmek
    2  gereksinime uygun yeterlilik
       yetersiz kapasite kadar gereksiz karmasiklik da zarar verebilir
    3  guvenlik ile kullanilabilirlik birlikte
       gerekli iletisim mumkun; yetkisiz veya zarar verici iletisim
       sinirli; davranis gozlenebilir ve duzeltilebilir; toplanan
       bilgi olculu
    4  acik sorumluluk ve bilgi aktarimi
       sureklilik bir kisinin hatirladigi ayrintilara bagimli
       birakilmaz

  AMAC YERINE GECIRILEMEYENLER
    x  en yuksek hiz
    x  hangi arizalara karsi, hangi kapsamda, hangi maliyetle ve
       hangi toparlanma kosullariyla oldugu aciklanmamis sifir kesinti
    x  herkesin her seye erismesi
    x  en dusuk satin alma maliyeti
    x  teknik olarak etkileyici fakat kullanici isini guclestiren veya
       surdurulmesi zor bir mimari
~~~

*Çizim 17 — Gaye: amaca ulaştıran koşullar; amaç yerine geçirilemeyen ölçütler.*

İki şehirdeki bir araştırma ekibinin veri paylaşımı, taşıyıcı ile amaç arasındaki farkı somutlaştırır. Cihazlar değişirken hizmetin amacı ve gerekli davranışı korunabilir. Cihazlar aynı kaldığı hâlde erişim kuralları değiştiğinde birlikte çalışma olanağı değişebilir. Teknik kapasite büyük ölçüde aynı kalırken kullanım amacı da değişebilir. Böylece düzenin kimliğinin bileşenler, ilişkiler, kurallar ve amaçlar birlikte değerlendirilerek anlaşılabileceği görülür.

Bilgisayar ağları mühendisliğinin başarısı, mümkün kıldığı işlerin niteliğinde ve bunun koşullarının açıklanabilirliğinde görünür. Örgütlü haberleşme sistemi iletişimi gerçekleştirir; insanlar ve kurumlar amaçları belirler, tartışır ve sorumluluk üstlenir. Mühendislik, var olan koşullar içinde amaç ile gerçekleşen davranış arasındaki bağı kurar ve bu bağın geçerliliğini sınar.

~~~text
  IKI SEHIRDEKI BIR ARASTIRMA EKIBININ VERI PAYLASIMI
    cihazlar degisirken           hizmetin amaci ve gerekli davranisi
                                  korunabilir
    cihazlar ayni kaldigi halde   birlikte calisma olanagi degisebilir
    erisim kurallari degisince
    teknik kapasite buyuk olcude  kullanim amaci degisebilir
    ayni kalirken

    duzenin kimligi:  bilesenler + iliskiler + kurallar + amaclar
                      birlikte degerlendirilerek anlasilir

  ISBOLUMU
    orgutlu haberlesme sistemi    iletisimi gerceklestirir
    insanlar ve kurumlar          amaclari belirler, tartisir,
                                  sorumluluk ustlenir
    muhendislik                   amac ile gerceklesen davranis
                                  arasindaki bagi kurar ve sinar
    basari:  mumkun kilinan islerin niteligi ve kosullarinin
    aciklanabilirligi
~~~

*Çizim 18 — Gaye: iki şehir örneği; düzenin kimliği; işbölümü.*

### Uygulama adımları

1. **Üç amacı ayır.** Teknik iletişim işlevini, hizmet edilen işi ve bu işin neden değerli görüldüğünü 5 Gaye Kaydı içinde ayrı paragraflarla yaz. Bu düzeylerin birbirine nasıl bağlandığını açıkla.

2. **Amaçtan ölçüte geç.** Amaçların erişim, performans, süreklilik ve diğer hizmet koşullarında nasıl temsil edildiğini belirt. Bu çevirinin amacın bütün toplumsal veya etik gerekçesini tüketmediğini koru.

3. **Amaç ve sorumluluk taraflarını göster.** Amaç belirleyen, uygulayan, işleten ve sonuçlardan etkilenen tarafları kaydet. Hedef koyma yetkisiyle hedefin haklılığını özdeşleştirme; olası çıkar farklılıklarını açıkla.

4. **Araçları ve bedelleri değerlendir.** Hız, kapasite, kullanılabilirlik, yalıtım ve maliyetin hangi koşullarda amaca katkıda bulunduğunu yaz. Hepsinin aynı anda ve sınırsız biçimde en yüksek değere çıkarılmasını genel hedef yapma.

5. **Nihai amaç ve sınır hükmünü yaz.** İnsan odaklı amaç önerisinin gerekçesini, geçerlilik kapsamını ve ne olmadığını belirt. Teknik başarıyla amaç başarısını ayırt et. Çözülemeyen değer veya kapsam meselesini açık meseleye kaydet.

### Kayıt ve çıktı

Çıktı, `CALISMA_KAYDI.md` içindeki 5 Gaye Kaydıdır. Teknik işlev, hizmet edilen iş, değer gerekçesi, amaçların teknik karşılıkları, taraflar ve araç–amaç sınırları burada bulunur. Kökleşme bu kaydı diğer dört protokolle birlikte değerlendirir.

### Tamamlanma ölçütü

- [ ] Teknik işlev, hizmet edilen iş ve nihai amaç ayrıldı.
- [ ] Amaç gerçekleştirme ile amacı gerekçelendirme birbirinin yerine geçirilmedi.
- [ ] Normatif önerinin niteliği, taraflar ve araçsal ölçütlerin sınırları açıklandı.

### Açık meseleler ve geri dönüş

Amaç değişirse önce Tohum'u ve etkilenen protokolleri gözden geçir. Yalnız bir başarı ölçütü veya gerekçe düzeliyorsa ilgili Gaye kaydını güncelle ve Kökleşme'de etkisini değerlendir.

## 6 Kökleşme (Bitiş) Protokolü

### Amaç ve kapsam

Bu protokol, Varlık, Mekan, Usül, Zaman ve Gaye açıklamalarını birlikte değerlendirerek mevcut inceleme turunu tamamlar. Sonucun hangi dayanaklarla, hangi kapsamda ve hangi sınırlar içinde kullanılabileceğini kayda geçirir. Böylece geliştirilen anlayış, yeniden okunabilir ve gerektiğinde güncellenebilir bir referansa dönüşür.

Kökleşme, yalnızca beş bölümün art arda özetlenmesi değildir. Bölümler arasındaki ilişkileri ve olası tutarsızlıkları ele alır. Gaye Protokolü incelenen alanın hangi amaca hizmet ettiğini araştırırken Kökleşme, bu alan hakkında yürütülen incelemenin neye ulaştığını belirler. Bitiş, mevcut çalışma turunun tamamlanmasıdır; daha sonra ortaya çıkacak bilgiye karşı değişmezlik iddiası taşımaz.

**Yönlendirici sorular:** Başlangıç soruları ne ölçüde yanıtlandı? Beş açıklama birlikte nasıl bir bütün oluşturuyor? Hangi sonuçlar hangi dayanaklarla kullanılabilir? Hangi açık meseleler ve değişiklikler yeniden değerlendirme gerektiriyor?

### Girdiler

Girdiler, Başlangıç Kaydı, 1–5 protokollerinin kayıtları, özgün sorular, kullanılan kaynaklar ve açık meselelerdir. Önceki sürümler varsa değişiklikler de değerlendirilir. Her protokolün durum alanı görünür olmalıdır. Mevcut olmayan ölçüm, deney, gerçek ortam uygulaması veya kullanıcı kabulü gerçekleşmiş gibi kayda geçirilemez.

### Bu çalışma için kapanış sentezi

Bilgisayar ağları mühendisliği, ayrı bilgi işlem sistemleri arasındaki iletişimi belirli koşullarda kurulabilir, sürdürülebilir ve değerlendirilebilir bir hizmete dönüştürür. Bu tanımın varlık boyutu haberleşen bileşenler ve aralarındaki ilişkilerde; mekân boyutu fiziksel yollar, mantıksal erişim ve yetki sınırlarında; usul boyutu protokoller ile tasarlama ve sınama faaliyetlerinde; zaman boyutu iletim, uyum, işletim ve yaşam döngüsünde; gaye boyutu ise hizmet edilen işin gerekçesinde görünür.

Bu boyutları birlikte taşıyan düzene ilişkin kavramsal cevap, insanların belirli iletişim amaçları doğrultusunda kurduğu ve sürdürdüğü örgütlü haberleşme sistemidir. Teknik taşıyıcı bilgisayar ağıdır. Amaçları belirleyen, kararları tartışan ve sonuçlarından sorumlu tutulabilen taraflar insanlar ve kurumlar arasındaki ilişkilerde bulunur. Mühendislik, amaç ile gerçekleşen davranış arasındaki bağı kurar ve sınar. Köken, taşıyıcı, fail ve gaye birbirinin yerine geçirilmez.

Tek başına bilgisayar, yönlendirici, protokol, İnternet, mühendis veya insan bu açıklamanın tamamı değildir. Her biri belirli bir bileşeni ya da rolü gösterir. Bir amacın teknik hedeflerle temsil edilmesi, o amacın normatif gerekçesini kendiliğinden oluşturmaz. İnsan odaklı nihai amaç da bütün ağların fiilî amacı olarak değil, değerlendirmede kullanılabilecek bir değer önerisi olarak korunur.

Bu sentezin kapsamı, bu konuşmada yürütülen kavramsal inceleme ve teknik kaynaklarla desteklenen açıklamalardır. Belirli bir gerçek ağın topolojisi, trafik ölçümleri ve hizmet sonuçları bu çalışmanın girdisi değildir. Böyle bir ağa ilişkin uygulama veya doğrulama sonucu çıkarılamaz. Tarihsel ve güncel durum açıklamalarının referans tarihi 31 Ekim 2026'dır; sonraki kullanımlarda değişebilir iddialar yeniden kontrol edilir. Bu kapanış metni, ilerideki bir masaüstü uygulamasının çalışma kaydını doldurulmuş saymaz.

### Uygulama adımları

1. **Başlangıç sorularına dön.** `CALISMA_KAYDI.md` içindeki her özgün soruyu onu karşılayan protokol kaydıyla eşleştir. Olumlu tanımların yanında “neler değildir?” sınırlarının da yanıtlandığını kontrol et. Ortak “makine kimdir, kim değildir?” sorusunun beş boyutla kurduğu ilişkiyi belirt.

2. **Dayanakları denetle.** Teknik iddiaların ilgili kaynaklarca desteklenip desteklenmediğini, tarih ve kapsamlarının korunduğunu incele. Kavramsal yorumların kaynakların doğrudan hükmü gibi sunulmasını ve değer önerilerinin evrensel olgulara çevrilmesini düzelt. Kaynağı doğrulanamayan bir ifadeyi doğrulanmış gibi işaretleme; açık meseleye kaydet.

3. **Bölümler arasındaki tutarlılığı incele.** Varlık tanımını Usül'deki faaliyetlerle, Mekan sınırlarını sorumluluklarla, Zaman koşullarını hizmet beklentileriyle ve Gaye açıklamasını teknik işlevle karşılaştır. Köken, taşıyıcı, fail ve gaye farklı bölümlerde farklı anlamlarda kullanılmışsa hangi açıklamanın değişmesi gerektiğini belirle ve ilgili kaydı düzelt.

4. **Bütünün sonucunu yaz.** `6 Bitiş Kaydı` altında beş bölümü birbirine bağlayan paragraflar oluştur. Teknik taşıyıcının, amaç belirleyen tarafların ve mühendisliğin rollerini açıklığa kavuştur. Yukarıdaki kapanış sentezini mevcut kayıtla karşılaştır; farklı bir sonuca ulaşıldıysa farkını ve gerekçesini açıkça yaz. Eski sentezi otomatik olarak sonuç kabul etme.

5. **Açık meseleleri ve kullanım sınırlarını belirt.** Ek kaynak, başka bir bağlam veya gerçek ortam gözlemi gerektiren noktaları yaz. Her açık meselenin hangi iddiayı ve protokolü etkilediğini belirt. Sonucu bütünüyle değiştirmeyen bir eksikliği kendi kapsamıyla sınırlandır; önemli bir tutarsızlığı yalnız kayda geçirmekle çözülmüş sayma.

6. **Son kaydı düzenle.** 0–6 sırasını, başlıkları, kaynak bağlantılarını ve dosyalar arasındaki başvuruları kontrol et. 0–5 kayıtlarının durum alanlarını sonuçla karşılaştır; `Sürüyor` kalan bir kaydın bitişi neden engellemediğini gerekçelendir veya ilgili eksikliği tamamla. Geçici düzenleme notlarını temizle; gerekli belirsizlik kayıtlarını koru. Sürümü, yapılan kontrolleri ve bitiş durumunu yaz. Ana belgenin veya yönerge paketinin tamamlanması ile ayrıca yürütülecek bir uygulamanın tamamlanmasını ayrı değerlendir.

~~~text
  BES BOYUT  kapanis sentezi
    varlik   haberlesen bilesenler ve aralarindaki iliskiler
    mekan    fiziksel yollar . mantiksal erisim . yetki sinirlari
    usul     protokoller . tasarlama ve sinama faaliyetleri
    zaman    iletim . uyum . isletim . yasam dongusu
    gaye     hizmet edilen isin gerekcesi

  "KIMDIR?"  insanlarin belirli iletisim amaclari dogrultusunda
             kurdugu ve surdurdugu orgutlu haberlesme sistemi
    teknik tasiyici                  bilgisayar agi
    amaclari belirleyen, kararlari   insanlar ve kurumlar arasindaki
    tartisan, sorumlu tutulabilen    iliskiler
    amac ile davranis arasindaki     muhendislik
    bagi kuran ve sinayan
    koken, tasiyici, fail ve gaye birbirinin yerine gecirilmez

  "KIM DEGILDIR?"  tek basina
    bilgisayar . yonlendirici . protokol . Internet . muhendis . insan

  KAPSAM
    girdi degil:  gercek bir agin topolojisi . trafik olcumleri .
                  hizmet sonuclari
    kapanis metni  -/->  ilerideki uygulamanin calisma kaydinin
                         doldurulmus sayilmasi
    ana belgenin tamamlanmasi  =/=  ayrica yurutulecek bir uygulamanin
                                    tamamlanmasi
~~~

*Çizim 19 — Kökleşme: kapanış sentezi; kimdir ve kim değildir; kapsam.*

### Kayıt ve çıktı

Çıktı, `CALISMA_KAYDI.md` içindeki **6 Bitiş Kaydı** ve onunla tutarlı son metindir. Kayıt, soruların yanıt durumlarını, bütünün sonucunu, dayanakları, geçerlilik kapsamını, açık meseleleri ve yeniden değerlendirme koşullarını içerir. Yapılmış kontroller kendi sonuçlarıyla belirtilir; yapılmamış çalışmalar sonuç gibi yazılmaz.

### Tamamlanma ölçütü

- [ ] Başlangıç sorularının hangi kayıtlarla yanıtlandığı izlenebiliyor.
- [ ] Sonucu değiştiren tutarsızlıklar giderildi; kalan açık meselelerin etkisi sınırlandırıldı.
- [ ] Olgu, yorum ve değer önerileri ayırt edilebiliyor; kaynaklar ve tarihler anlaşılır.
- [ ] Sonuç, kapsam, açık meseleler ve yeniden değerlendirme koşulları kaydedildi.

Bu koşullar karşılandığında durum alanını `Tamamlandı` yap ve gerekçesini yaz. Sonucu belirlemeyi engelleyen eksiklik varsa durumu `Sürüyor` olarak koru ve gereken sonraki işi belirt. Açık meselelerin bulunması tek başına bitişi engellemez; önemli olan sonuca etkilerinin açıklanmış olmasıdır.

### Açık meseleler ve geri dönüş

Yeni bir kaynak, karşı örnek veya değişen koşul belirli bir açıklamayı etkiliyorsa ilgili protokole dön. Konu veya temel amaç değişirse Tohum'u yeniden aç. Düzeltmelerden sonra Kökleşme'yi tekrar yürüt ve yeni sürümde neyin, neden değiştiğini kaydet. Böylece başlangıçla bitiş arasındaki düşünme süreci izlenebilir kalır.

## Kaynaklar

Teknik iddialar aşağıdaki kaynaklara dayanır. “Makine”ye ilişkin bütünleştirici açıklama ve insan odaklı nihai amaç, belgede nitelikleri belirtilen kavramsal ve normatif önerilerdir. Bu öneriler tek bir standardın doğrudan hükmü olarak okunmamalıdır.

Metin içindeki köşeli kaynak numaraları aşağıdaki sıraya karşılık gelir. Tarihsel anlatının referans tarihi **31 Ekim 2026**'dır. Daha sonraki bir uygulamada değişebilir iddialar yeniden kontrol edilir.

1. Internet Architecture Board. RFC 1958 Architectural Principles of the Internet. Haziran 1996. İnternet mimarisi, uçtan uca yaklaşım ve evrimsel gelişim. Kaynak metni: https://www.rfc-editor.org/rfc/rfc1958.html

2. B. Carpenter ve B. Liu. RFC 8799 Limited Domains and Internet Protocols. Temmuz 2020. Sınırlı ağ bölgeleri ve farklı gereksinimler. Kaynak metni: https://www.rfc-editor.org/rfc/rfc8799.html

3. Y. Rekhter, T. Li ve S. Hares. RFC 4271 A Border Gateway Protocol 4. Ocak 2006. Alanlar arası yönlendirme, ulaşılabilirlik ve politika. Kaynak metni: https://datatracker.ietf.org/doc/html/rfc4271

4. S. Rose ve diğerleri. NIST SP 800-207 Zero Trust Architecture. Ağustos 2020. Ağ konumuyla güven ilişkisinin ayrıştırılması. Kaynak metni: https://csrc.nist.gov/pubs/sp/800/207/final

5. K. Kompella ve Y. Rekhter. RFC 4202 Routing Extensions in Support of Generalized Multi-Protocol Label Switching. Ekim 2005. Ortak risk bağlantı grupları. Kaynak metni: https://www.rfc-editor.org/rfc/rfc4202.html

6. A. Farrel editörlüğünde. RFC 9522 Overview and Principles of Internet Traffic Engineering. Ocak 2024. Performans, kaynak kullanımı ve farklı zaman ölçekleri. Kaynak metni: https://www.rfc-editor.org/rfc/rfc9522.html

7. H. Song ve diğerleri. RFC 9232 Network Telemetry Framework. Mayıs 2022. İletme, denetim ve yönetim düzlemleri ile telemetri. Kaynak metni: https://www.rfc-editor.org/rfc/rfc9232.html

8. F. Baker ve G. Fairhurst. RFC 7567 IETF Recommendations Regarding Active Queue Management. Temmuz 2015. Kuyrukların gecikme üzerindeki etkisi ve kuyruk yönetimi. Kaynak metni: https://www.rfc-editor.org/rfc/rfc7567.html

9. R. Bush ve D. Meyer. RFC 3439 Some Internet Architectural Guidelines and Philosophy. Aralık 2002. Büyük ağlarda karmaşıklığın tasarım üzerindeki etkileri. Kaynak metni: https://www.rfc-editor.org/rfc/rfc3439.html

10. A. Clemm ve diğerleri. RFC 9315 Intent-Based Networking Concepts and Definitions. Ekim 2022. IRTF bilgilendirici belgesi; amaç temelli yönetim ve amaçlara uygunluğun izlenmesi. Kaynak metni: https://datatracker.ietf.org/doc/html/rfc9315

11. Ultra Ethernet Consortium. Ultra Ethernet Consortium Releases Specification 1.1 Advancing AI and HPC Networking. 12 Ekim 2026. Konsorsiyumun kendi sürüm duyurusu. Kaynak metni: https://ultraethernet.org/ultra-ethernet-consortium-releases-specification-1-1-advancing-ai-and-hpc-networking/

12. N. Finn ve diğerleri. RFC 8655 Deterministic Networking Architecture. Ekim 2019. Kontrollü yönetim alanlarında belirli akışların gecikme ve kayıp gereksinimleri. Kaynak metni: https://www.rfc-editor.org/rfc/rfc8655.html

13. Internet Architecture Board. RFC 8890 The Internet is for End Users. Ağustos 2020. Son kullanıcı çıkarları ve teknik kararların amaçları. Kaynak metni: https://www.rfc-editor.org/rfc/rfc8890.html

## Çalışma kaydı şablonu

Aşağıdaki kod bloğunun içeriğini, ilk ve son üçlü ters tırnak satırlarını almadan `CALISMA_KAYDI.md` adlı ayrı bir dosyaya kopyala. Şablondaki `Başlatılmadı` durumları gelecekteki uygulamaya aittir. Bu belgenin soru ve yanıt metinleri ile yönergeleri tamamlanmıştır.

```markdown
# Bilgisayar Ağları Mühendisliği Çalışma Kaydı

Bu dosya, gelecekteki bir uygulama için boş çalışma kaydı şablonudur. İlk kullanımda `CALISMA_KAYDI.md` adıyla kopyala. Önceden açılmış kaydı sürdürüyorsan yeni kopya oluşturma. Köşeli parantezli doldurma alanlarını kendi kayıtlarınla değiştir. Durumu yalnız gerçekten yaptığın işe göre `Başlatılmadı`, `Sürüyor` veya `Tamamlandı` olarak yaz.

**Konu:** Bilgisayar Ağları Mühendisliği
**İnceleme tarihi:** [Doldurulacak]
**Kayıt sürümü:** [Doldurulacak]
**İncelemeyi yürüten:** [Doldurulacak]
**Kullanılan protokol sürümü:** 1.0
**Faaliyet:** Kavramsal inceleme ve belgeleme

## 0 Başlangıç Kaydı

**Durum:** Başlatılmadı

### Özgün başlangıç talimatı ve sorular

“Geçmiş bağlamları buraya taşıma. Burası ile sınırlı kalma.”

**1 Varlık Protokolü:** Nedir? Onu o yapan nelerdir? Neler değildir?

**2 Mekan Protokolü:** Nerededir? Bu yeri, oraya has bir yer yapan nelerdir? Neler değildir?

**3 Usül Protokolü:** Nasıl işler yapar? Bu yaptıklarını, ona has yapan nelerdir? Neler değildir?

**4 Zaman Protokolü:** Hangi andadır? Bu anı, diğer zamanlardan farklı yapan nelerdir? Neler değildir?

**5 Gaye Protokolü:** Hangi nihai amaca hizmet eder? Bu nihai amaca ulaştıran nelerdir? Neler değildir?

**Ortak soru:** Bilgisayar Ağları Mühendisliği’nin; köken aldığı varlık, mekan, usül, zaman, ve gayeyi taşıyan makine kimdir? Kim değildir?

### Başlangıç ihtiyacı ve kapsam

[Doldurulacak: Neyi açıklığa kavuşturmak istediğini, dâhil edilen bağlamı ve kapsam dışındaki işleri bir veya birkaç paragrafla yaz.]

### Bilinenler, önkabuller ve kaynak durumu

[Doldurulacak: Mevcut bilgiyi, çalışma yorumlarını ve sınanması gereken kabulleri ayır. Hangi kaynakların kullanıldığını belirt.]

### Beklenen açıklamalar

[Doldurulacak: Varlık, Mekan, Usül, Zaman ve Gaye kayıtlarının hangi soruları yanıtlayacağını ve ortak soruya nasıl katkıda bulunacağını yaz.]

### Açık meseleler

[Doldurulacak: Açık meseleyi, etkilediği iddiayı ve protokolü, sonuca etkisini ve gerekli sonraki işi yaz. Açık mesele bulunmuyorsa bunu gerekçesiyle belirt.]

### Tamamlanma değerlendirmesi

[Doldurulacak: Protokolün tamamlanma ölçütlerini değerlendir; durumun dayanağını ve değerlendirme tarihini yaz.]

## 1 Varlık Kaydı

**Durum:** Başlatılmadı

### Tanım ve ayırt edici özellikler

[Doldurulacak: Alanı tanımla; ayrı bilgi işlem sistemleri arasında iletişimi ayırt eden ilişkileri gerekçelendir.]

### Köken, taşıyıcı, fail ve gaye

[Doldurulacak: Dört rolü birbirine indirgemeden açıkla. Teknik taşıyıcı ile amaç ve sorumluluk taraflarını belirt.]

### Sınırlar ve açıklayıcı örnek

[Doldurulacak: Neler değildir sorusunu yanıtla. Varsayımsal örneği gerçek deneyden ayırarak tanımı sına.]

### Açık meseleler

[Doldurulacak: Açık meseleyi, etkilediği iddiayı ve protokolü, sonuca etkisini ve gerekli sonraki işi yaz. Açık mesele bulunmuyorsa bunu gerekçesiyle belirt.]

### Tamamlanma değerlendirmesi

[Doldurulacak: Protokolün tamamlanma ölçütlerini değerlendir; durumun dayanağını ve değerlendirme tarihini yaz.]

## 2 Mekan Kaydı

**Durum:** Başlatılmadı

### Maddi, mantıksal, örgütsel ve işlevsel yer

[Doldurulacak: Dört yer düzeyini ve aralarındaki ilişkileri paragraflarla açıkla.]

### Erişim, güven, yetki ve bağımlılıklar

[Doldurulacak: Sınırların nerede ayrıldığını ve görünürde ayrı bileşenlerin hangi ortak bağımlılıkları taşıyabildiğini yaz.]

### Sistem kapsamı ve kapsam dışı

[Doldurulacak: Hizmeti doğrudan üreten ve sürdüren bileşenlerle daha geniş etkileyen koşulları ayır.]

### Açık meseleler

[Doldurulacak: Açık meseleyi, etkilediği iddiayı ve protokolü, sonuca etkisini ve gerekli sonraki işi yaz. Açık mesele bulunmuyorsa bunu gerekçesiyle belirt.]

### Tamamlanma değerlendirmesi

[Doldurulacak: Protokolün tamamlanma ölçütlerini değerlendir; durumun dayanağını ve değerlendirme tarihini yaz.]

## 3 Usül Kaydı

**Durum:** Başlatılmadı

### İhtiyaç ve teknik koşullar

[Doldurulacak: Kullanıcı, iş, yük ve hizmet beklentisi arasındaki ilişkiyi yaz. Verilmemiş hedef değerlerini gerçekleşmiş gereksinim gibi ekleme.]

### Yöntem ve iki usul düzeyi

[Doldurulacak: İhtiyaçtan işletime uzanan yöntemi, makinenin kuralları ile mühendisliğin muhakemesini ayırarak açıkla.]

### Doğrulama planı, mevcut kanıt ve roller

[Doldurulacak: Hangi gözlemin hangi soruyu yanıtlayacağını, elindeki kanıtı ve sorumlu rolleri yaz. Yapılmamış işlemleri plan olarak kaydet.]

### Açık meseleler

[Doldurulacak: Açık meseleyi, etkilediği iddiayı ve protokolü, sonuca etkisini ve gerekli sonraki işi yaz. Açık mesele bulunmuyorsa bunu gerekçesiyle belirt.]

### Tamamlanma değerlendirmesi

[Doldurulacak: Protokolün tamamlanma ölçütlerini değerlendir; durumun dayanağını ve değerlendirme tarihini yaz.]

## 4 Zaman Kaydı

**Durum:** Başlatılmadı

### Tarihler ve tarihsel kapsam

[Doldurulacak: Olay, yayın ve inceleme tarihlerini ayır. Kaynakların hangi döneme ve kapsama ilişkin olduğunu yaz.]

### Çalışma süreleri ve zamanında olma

[Doldurulacak: İletim, uyum, işletim ve yaşam döngüsü sürelerini ilişkilendir. Ulaşmak ile zamanında ulaşmak arasındaki farkı açıkla.]

### Geçiş ve yeniden kontrol koşulları

[Doldurulacak: Son duruma hangi geçişle ulaşılacağını ve hangi yeni bilginin eski varsayımları yeniden değerlendirmeyi gerektireceğini yaz.]

### Açık meseleler

[Doldurulacak: Açık meseleyi, etkilediği iddiayı ve protokolü, sonuca etkisini ve gerekli sonraki işi yaz. Açık mesele bulunmuyorsa bunu gerekçesiyle belirt.]

### Tamamlanma değerlendirmesi

[Doldurulacak: Protokolün tamamlanma ölçütlerini değerlendir; durumun dayanağını ve değerlendirme tarihini yaz.]

## 5 Gaye Kaydı

**Durum:** Başlatılmadı

### Teknik işlev, hizmet edilen iş ve nihai amaç

[Doldurulacak: Üç düzeyi, bunların birbirine bağlanmasını ve nihai amacın gerekçesini ayrı paragraflarla yaz.]

### Amaçların teknik karşılıkları ve taraflar

[Doldurulacak: Amaçların hangi koşullarda temsil edildiğini; belirleyen, uygulayan ve etkilenen tarafları belirt.]

### Başarı ölçütleri, değer önerisi ve sınırlar

[Doldurulacak: Araçsal ölçütleri amaçla ilişkilendir. Teknik başarıyı amaç başarısından ayır; normatif önerinin kapsamını yaz.]

### Açık meseleler

[Doldurulacak: Açık meseleyi, etkilediği iddiayı ve protokolü, sonuca etkisini ve gerekli sonraki işi yaz. Açık mesele bulunmuyorsa bunu gerekçesiyle belirt.]

### Tamamlanma değerlendirmesi

[Doldurulacak: Protokolün tamamlanma ölçütlerini değerlendir; durumun dayanağını ve değerlendirme tarihini yaz.]

## 6 Bitiş Kaydı

**Durum:** Başlatılmadı

### Başlangıç sorularının yanıt durumu

[Doldurulacak: Her özgün soruyu onu yanıtlayan kayıtla eşleştir. Olumlu tanımların ve sınır sorularının karşılığını belirt.]

### Tutarlılık ve bütünün sonucu

[Doldurulacak: Beş boyutu birleştiren sonucu, köken, taşıyıcı, fail ve gayeyi ayırarak yaz. Giderilen tutarsızlıkları belirt.]

### Dayanaklar, geçerlilik ve yeniden değerlendirme

[Doldurulacak: Sonucun hangi kanıt ve yorumlara dayandığını, kullanım sınırlarını ve yeniden açılma koşullarını yaz.]

### Açık meseleler

[Doldurulacak: Açık meseleyi, etkilediği iddiayı ve protokolü, sonuca etkisini ve gerekli sonraki işi yaz. Açık mesele bulunmuyorsa bunu gerekçesiyle belirt.]

### Tamamlanma değerlendirmesi

[Doldurulacak: Protokolün tamamlanma ölçütlerini değerlendir; durumun dayanağını ve değerlendirme tarihini yaz.]

## Kaynak ve değişiklik kaydı

[Doldurulacak: Kullanılan kaynağın başlığını, bağlantısını, tarihini ve desteklediği açıklamayı yaz. Yeni sürümde değişen bölümü, değişikliğin gerekçesini ve diğer protokollere etkisini belirt.]
```

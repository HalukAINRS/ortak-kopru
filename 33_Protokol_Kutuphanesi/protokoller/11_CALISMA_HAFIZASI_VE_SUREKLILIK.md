# Çalışma Hafızası ve Süreklilik Protokolleri

**Sürüm:** 1.0\
**Tarih:** 30 Ekim 2026\
**Kapsam:** 0–6 protokolleri, masaüstü uygulama adımları ve kaynak soru yanıt kaydı

Çalışma hafızası, yürütülen iş için gerekenleri etkin olarak tutma ve işleme işlevini; süreklilik, bu işin değişen anlar ve koşullar arasında anlamlı biçimde sürdürülebilmesini ifade eder. Tohum başlangıcı kurar; Varlık, Mekan, Usül, Zaman ve Gaye çalışmanın beş boyutunu açıklar; Kökleşme elde edilenleri dayanakları ve açık kalanlarıyla birlikte yerleştirerek aşamayı kapatır. Köken, taşıyıcı, eyleyen ve gayeyi belirleyen roller bütün bölümlerde ayrı değerlendirilir.

Her protokol, paragraf ağırlıklı kavramsal metin, masaüstünde uygulama adımları, tamamlanma ölçütü ve kayıt alanlarından oluşur. Yönergeler bir metin düzenleyicide veya dosyalara erişebilen bir masaüstü asistanıyla uygulanabilir. Gerçekleştirilen işler ilgili çalışmanın tek kaydında tutulur. Eklerdeki geçmiş soru yanıtlar kaynak kaydıdır; güncel uygulama yönergeleri 0–6 bölümlerindedir.

## Masaüstünde kullanım

Yeni bir çalışma için `kayitlar/<calisma-kimligi>/CALISMA_KAYDI.md` dosyasını oluştur ve her protokolün Kayıt bloğunu bu dosyada aynı adlı bölüm olarak birleştir; bölümler için ayrı kayıt dosyası açılmaz. `<calisma-kimligi>` yerine çalışmayı ayırt eden kısa bir ad yaz. Aynı çalışmanın kaydı varsa mevcut kayıttan devam et.

0 ile başlangıcı kur; 1–5 ile kimliği, çalışma alanını, usulü, zaman durumunu ve gayeyi birlikte açıkla. Fiilî işleme geçmeden önce mevcut gaye ve tamamlanma ölçütlerini belirginleştir. Çalışma boyunca değişen bölümü güncelle; aşama kapanırken 6'yı uygula. Bölümler, her işlemde baştan yürütülecek değişmez bir sıra oluşturmaz.

Alanlara yalnızca bilinen veya gerçekten gerçekleşmiş durumu yaz. Bilinmeyeni `bilinmiyor`, yapılmayanı `yapılmadı`, ilgili olmayanı `uygulanmıyor` olarak belirt. Tarih ve saatlere saat dilimini ekle. Varsayımı doğrulanmış bilgiye, öneriyi karara, hazırlanmış yönergeyi yapılmış işe dönüştürme. Anlamlı değişiklikleri aynı çalışma kaydının değişiklik kaydına önceki durum, yeni durum, tarih, gerekçe ve dayanak bilgileriyle ekle.

~~~text
  kayitlar/
    <calisma-kimligi>/
      CALISMA_KAYDI.md         her calisma icin tek kayit
        0 Tohum
        1 Varlik
        2 Mekan
        3 Usul
        4 Zaman
        5 Gaye
        6 Koklesme
        degisiklik kaydi       onceki durum . yeni durum . tarih .
                               gerekce . dayanak

  doldurulamayan alan icin:    bilinmiyor . yapilmadi . uygulanmiyor

  donusturulmez:    varsayim              --x-->   dogrulanmis bilgi
                    oneri                 --x-->   karar
                    hazirlanmis yonerge   --x-->   yapilmis is

  bolumler, her islemde bastan yurutulecek degismez bir sira degildir
~~~

*Çizim 1 — Tek kayıt düzeni: yedi bölüm ve bir değişiklik kaydı; üç durum sözcüğü; dönüştürülmeyecek üç şey.*

Başlangıçta belirtilen kaynak ve işlem kapsamını esas al. Başka sohbetlerin veya ilgisiz çalışmaların bağlamını kendiliğinden ekleme. Protokoller, mevcut kullanıcı isteğinin ve çalışma ortamının sağladığı işlem sınırlarını genişletmez. Bir aşamanın kaydının tamamlanması ile bütün gayeye ulaşılması ayrı durumlardır.

## 0 Tohum (Başlangıç) Protokolü

Tohum Protokolü, bir çalışmayı başlatan soruyu, ihtiyacı veya niyeti başlangıç koşullarıyla birlikte görünür kılar. Çalışmanın konusunu, ilk yönelimini ve ele alınacağı sınırları kayda geçirir. Başlangıçta bütün cevapların, yöntemin veya sonucun belirlenmiş olması beklenmez. Gerekli olan, neyin anlaşılmak ya da yapılmak istendiğinin, elde hangi dayanakların bulunduğunun ve nelerin henüz açık olduğunun ayırt edilebilmesidir. Bu kayıt, daha sonraki kararların başlangıçta verilmiş gibi gösterilmesini önler ve çalışmanın nasıl değiştiğinin anlaşılmasına dayanak olur.

Tohum bir yön taşır, ancak sonraki gelişmenin bütün biçimlerini peşinen belirlemez. İlk soru araştırma sırasında daralabilir, genişleyebilir veya başka bir soruya dönüşebilir. İlk niyetin daha açık bir gayeye dönüşmesi de mümkündür. Başlangıç niyeti ile Gaye Protokolünde açıklığa kavuşturulan amaç bu nedenle ilişkili, fakat ayrı kayıtlar olarak ele alınır. Yön değiştiğinde başlangıç kaydı silinerek geriye dönük uyum yaratılmaz; neyin, hangi gerekçeyle değiştiği mevcut çalışma kaydında anlaşılabilir biçimde belirtilir. Böylece başlangıcın gerçek durumu ile sonradan kazanılan açıklık birbirine karışmaz.

Başlangıç zemini, çalışmanın kaynak olarak belirlediği içeriklerle kurulur. Bir bilginin erişilebilir olması, kendiliğinden bu çalışmanın bağlamına katıldığı anlamına gelmez. Mevcut istekte belirtilen metinler, dosyalar ve açıklamalar kaynaklarıyla kaydedilir; gerekli fakat bulunmayan bilgi açık bir eksik olarak gösterilir. Başka çalışmaların kararları, tercihleri veya geçmiş konuşmaların yorumları otomatik olarak devralınmaz. Genel bilgi kullanılabilir, ancak belirli bir çalışmaya özgü geçmiş karar, tercih veya yetki gibi sunulmaz. Kaynağı belirsiz bir içerik, başlangıç durumunu tamamlamak amacıyla doğrulanmış bilgiye dönüştürülmez.

Tohum, üzerinde çalışılan konu ile bu çalışmayı yürüten kişi veya düzeni de ilk kez ilişkilendirir. Çalışmanın kimin adına yürüdüğü, hangi araçların kullanılabildiği ve mevcut isteğin hangi işlemleri kapsadığı anlaşılabilir olmalıdır. Bu başlangıç kaydı, köken, taşıyıcı, eyleyen ve gayeyi belirleyen rollerinin aynı varlıkta birleştiğini varsaymaz. Bu rollerin ayrıntılı açıklaması Varlık Protokolünde geliştirilir. Burada sağlanan şey, faaliyetin başlangıçtaki muhatabını ve sınırlarını kaybetmeden incelemeye geçebilecek yeterli açıklıktır. Belirtilmemiş bir rol veya karar, sırf kayıt tamamlanmış görünsün diye atanmaz.

Masaüstünde bu protokolün karşılığı, ilgili çalışmaya ait tek bir çalışma kaydının açılması veya mevcut kaydın kullanılmasıdır. Dosya adı ve konumu, çalışmanın konusunu ve kimliğini ayırt etmeye yardımcı olur; kaydın içeriği ise başlangıç durumunu açıklar. Soruların, kaynakların ve sınırların bu ortak kayıtta bulunması, sonraki protokollerin aynı çalışma üzerinde ilerlemesini sağlar. Her bölüm için birbirinden kopuk başlangıçlar üretilmez. Araç veya uygulama değiştiğinde kayıt başka bir editörde açılabilir; ancak yeni ortamın, içeriğin anlamını ve kullanılan kaynaklarla ilişkisini koruyabildiği değerlendirilir.

Tohumun tamamlanması, üzerinde çalışılabilir bir başlangıç durumunun elde edilmesidir. Belirsizliklerin tümünün giderilmiş olması, önerilerin kabul edilmiş kararlara dönüşmesi veya bütün faaliyetin baştan planlanması gerekmez. İlerlemeyi gerçekten engelleyen eksik ile çalışma sırasında açıklığa kavuşturulabilecek soru ayrılır; mevcut bilgiyle yapılabilecek iş sürdürülür. Tohum, bütün geçmişi içeri alan bir arşiv, gelecekteki sonuçları zorunlu kılan bir plan veya sürekli yeniden izin alınmasını gerektiren bir eşik olarak kullanılmaz. Başlangıç yönü, kapsamı ve açık kalanlarıyla birlikte sonraki protokollerin incelemesine açılır.

~~~text
  ERISILEBILIR OLAN                        BU CALISMANIN BAGLAMI
                                          .--------------------------.
  bu istekte belirtilen metin,            | kaynak                   |
  dosya ve aciklama            -------->  | (kaynagiyla kaydedilir)  |
                                          |                          |
  gerekli ama bulunmayan                  | acik eksik               |
  bilgi                        -------->  | (etkisiyle gosterilir)   |
                                          |                          |
  genel bilgi                  - - - - >  | kullanilabilir; bu ise   |
                                          | ozgu gecmis karar ya da  |
                                          | yetki gibi sunulmaz      |
                                          `--------------------------'
  baska calismalarin kararlari,
  tercihleri, eski konusmalarin
  yorumlari                    ----x      otomatik devralinmaz

  erisilebilir olmak, baglama katilmis olmak degildir

  tohum sunlar olarak kullanilmaz:
    butun gecmisi iceri alan arsiv . gelecegi zorunlu kilan plan .
    surekli yeniden izin alinmasini gerektiren esik
~~~

*Çizim 2 — Tohum: erişilebilir olan her şey çalışmanın bağlamına girmez.*

### Masaüstünde uygulama

1. Çalışmayı ayırt eden kısa bir kimlik belirle. Bu belgedeki yedi Kayıt bloğuyla `kayitlar/<calisma-kimligi>/CALISMA_KAYDI.md` kaydını oluştur. Aynı çalışmanın kaydı zaten varsa mevcut dosyayı kullan.
2. Kaydın `0 Tohum (Başlangıç) Protokolü` bölümüne başlangıç tarihini ve çalışmayı başlatan soruyu yaz. Sorunun özgün ifadesini, kendi yorumundan ayırt edilebilecek biçimde koru.
3. Başlangıç niyetini, kapsamı ve şu anki isteğin dışında kalan işlemleri açıkla. İlk niyeti nihai gaye veya kesinleşmiş sonuç olarak kaydetme.
4. Bu çalışma için belirlenen kaynakları dosya yolu, bağlantı veya açıklamayla göster. Kaynağı bulunmayan bilgiye dayanak uydurma; başka bağlamları otomatik ekleme.
5. Bilinenleri, varsayımları ve açık soruları ayrı alanlara yaz. Çalışmayı engelleyen eksik varsa etkisini belirt; engellemeyen eksikleri görünür tutarak yapılabilir işi sürdür.
6. Kaydı kaydet ve Varlık Protokolüne geç. Daha sonra başlangıç yönü değişirse özgün kaydı koru, değişikliği ortak kaydın değişiklik kaydına gerekçesiyle ekle.

### Tamamlanma ölçütü

Başlangıç sorusu, ilk niyet, kapsam, kullanılan kaynaklar ve açık sorular ortak çalışma kaydında anlaşılabilir durumdadır. Varsayımlar doğrulanmış bilgi gibi sunulmamıştır. Bir sonraki protokolün hangi çalışma üzerinde ilerleyeceği bellidir; devamı engelleyen bir eksik varsa eksik ve etkisi açıkça kayıtlıdır.

### Kayıt

```markdown
## 0 Tohum (Başlangıç) Protokolü

Başlangıç tarihi ve saati:

Çalışmayı başlatan soru veya istek:

Başlangıç niyeti:

Kapsam ve işlem sınırı:

Bu çalışmada kullanılacak kaynaklar:

Başlangıçta bilinenler:

Henüz doğrulanmamış varsayımlar:

Açık sorular ve eksik bilgiler:

Devamı engelleyen eksik ve etkisi, varsa:

İlk uygulanabilir adım:

Durum: Başlangıç kuruldu / Eksik nedeniyle bekliyor
```

## 1 Varlık Protokolü

Çalışma hafızası, yürütülen bir işin anlaşılması ve yönlendirilmesi için gerekenlerin etkin olarak elde tutulmasını ve işlenmesini sağlayan işlevdir. Süreklilik ise bu işin zaman, koşullar, kişiler veya ortamlar değiştiğinde anlamlı biçimde sürdürülebilmesini sağlayan bağların korunması ve gerektiğinde yeniden kurulmasıdır. Burada iş; düşünme, öğrenme, araştırma, birlikte karar verme ve üretme faaliyetlerini kapsar. Psikolojide çalışma belleğinin geçici depolamayla birlikte bilgiyi işlemeyi de içermesi, bu çerçevenin bilimsel başlangıç noktasıdır. Ortak ve teknik çalışmaya ilişkin açıklamalar ise bu kullanımın işlevsel olarak genişletilmesidir. [K1]

Bu işlevi özgül kılan, yalnızca belirli bilgilerin mevcut olması değildir. Amaç, mevcut durum, kararlar, gerekçeler, kısıtlar ve açık sorular arasında, yürütülen faaliyet bakımından kullanılabilir ilişkiler kurulmasıdır. Bir bilginin neden önemli olduğu, hangi kararı etkilediği ve değiştiğinde nelerin yeniden düşünülmesi gerektiği bu ilişkilerin parçasıdır. Etkin kullanılabilirlik, seçicilik, ilişkilendirme ve güncellenebilirlik çalışma hafızasının; durumlar arasında anlaşılabilir geçiş kurulması ise sürekliliğin ayırt edici özellikleri olarak ele alınır. Bu özelliklerin varlığı, içeriğin doğru veya yönün uygun olduğunu kendiliğinden güvenceye almaz.

~~~text
  CALISMA HAFIZASI                       SUREKLILIK
  yuruyen is icin gerekeni               is; zaman, kosul, kisi ya da
  etkin olarak tutmak VE islemek         ortam degisince de surer

     amac ------- mevcut durum           durum 1 ==> durum 2 ==> durum 3
       \           /                        baglar korunur,
       kararlar -- gerekceler               gerekirse yeniden kurulur
       /           \
   kisitlar      acik sorular

  ayirt edenler:                         ayirt eden:
    etkin kullanilabilirlik                durumlar arasinda
    secicilik                              anlasilabilir gecis
    iliskilendirme
    guncellenebilirlik

  bir bilginin:  neden onemli oldugu . hangi karari etkiledigi .
                 degistiginde neyin yeniden dusunulecegi

  bunlarin varligi, icerigin dogru ya da yonun uygun oldugunu
  kendiliginden guvenceye almaz
~~~

*Çizim 3 — Varlık: çalışma hafızası ile süreklilik; kurulan ilişkiler ve ayırt edici özellikler.*

Bu işlevlerin taşıyıcısı, işlevsel düzeyde eyleyen sistem olarak adlandırılır. İnsan bakımından söz konusu olan, bedeni, yaşadığı dünya ve ilişkileri içindeki kişidir. Ortak bir çalışmada taşıma işi, kişilerle araçların örgütlenmesine dağılabilir. Teknik düzeyde ise belirli koşullarda işlem yapan ve durumunu koruyan bir sistemden söz edilebilir. Makine sözcüğü burada bu işlevleri gerçekleştiren somut düzeni anlatır; insanın bütün varlığını açıklayan bir tanım veya bu düzenin tek bir bilinçli kişi olduğuna ilişkin bir hüküm olarak kullanılmaz.

Köken, taşıyıcı, eyleyen ve gayeyi belirleyen birbirinden ayrılır. Köken, yeteneğin veya düzenin nasıl ortaya çıktığını; taşıyıcı, durumun hangi maddi ve işlevsel ilişkiler içinde korunduğunu; eyleyen, bu durumdan hareketle işlemi gerçekleştiren birimi anlatır. Gayeyi belirleyen ve sahiplenen rol ise neyin yapılmaya değer olduğuna, başarının ne sayılacağına ve yönün nasıl değiştirileceğine ilişkindir. Bir şeyi meydana getiren, saklayan, onunla işlem yapan ve amacını belirleyen aynı varlık olmak zorunda değildir. Bu rolleri tek bir bileşende varsaymak yerine, somut çalışma içindeki ilişkileriyle açıklamak gerekir.

Sürekliliğin varlığı, bütün öğelerin değişmeden kalmasını gerektirmez. Araç, yöntem veya katılımcı değişebilir; önceki bir varsayım terk edilebilir. Çalışmanın devamı, bu değişimlerin hangi gerekçelerle gerçekleştiğinin ve mevcut işle nasıl ilişkilendiğinin anlaşılabilmesiyle değerlendirilir. Aynı adın, dosyanın veya cihazın korunması ise tek başına aynı çalışmanın sürdüğünü göstermez. Bir sistem hakkında anlatılan geçmiş ile onun durumları arasında gerçekten kurulmuş devam ilişkisi de ayrıdır. Kimlik anlatısı, işleyişin ve geçmişin incelenmesinin yerine geçmez.

Çalışma hafızası bir arşiv, kayıt dökümü veya bilgi yığınının bütünüyle özdeş değildir; süreklilik de kesintisizlik ya da değişmezlik değildir. Bunları açıklamak için hafızanın içinde bütün işlemleri yöneten ayrı bir küçük özne varsayılmaz. Kayıt, kaydettiği eyleyenin kendisi sayılmaz; tutarlı bir anlatı da tek başına kişilik veya öznel deneyim kanıtı olarak alınmaz. İnsanın kimliği ve değeri, hafızasının başarısına veya faaliyetlerini ne kadar kesintisiz sürdürebildiğine indirgenmez. Bu protokol, belirtilen işlevleri tarif ederken taşıyıcının bütün varlığı hakkında kapsamını aşan sonuçlar üretmez.

~~~text
  KOKEN            TASIYICI          EYLEYEN           GAYEYI
                                                       BELIRLEYEN
  yetenek ya da    durum hangi       bu durumdan       neyin yapilmaya
  duzen nasil      maddi ve          hareketle         deger oldugu,
  ortaya cikti?    islevsel          islemi            basarinin ne
                   iliskilerde       gerceklestiren    sayilacagi,
                   korunuyor?        birim             yonun nasil
                                                       degisecegi
  meydana          saklayan          islem yapan       amacini
  getiren                                              belirleyen
      |                |                 |                 |
      `------- ayni varlik olmak zorunda degildir ---------'

  degildir:
    calisma hafizasi   arsiv . kayit dokumu . bilgi yigini
    sureklilik         kesintisizlik . degismezlik
    kayit              kaydettigi eyleyenin kendisi
    kimlik anlatisi    isleyisin ve gecmisin incelenmesinin yerine
                       gecen sey
  ayni adin, dosyanin ya da cihazin korunmasi, ayni calismanin
  surdugunu tek basina gostermez
~~~

*Çizim 4 — Dört rol: köken, taşıyıcı, eyleyen ve gayeyi belirleyen aynı varlık olmak zorunda değildir.*

### Masaüstünde uygulama

1. Bu çalışmaya ait `kayitlar/<calisma-kimligi>/CALISMA_KAYDI.md` dosyasını aç. 0 Tohum bölümündeki sorudan hareketle, ele alınan işi bir veya iki cümleyle 1 Varlık Protokolü bölümüne yaz.

2. İşin kapsamına giren faaliyetleri ve dışında kalanları belirt. Çalışmanın adı ile fiilen yapılan iş arasında fark varsa bunu açık soru olarak kaydet; adın tek başına kimliği belirlediğini varsayma.

3. Kökeni veya başlangıç gerekçesini, durumu taşıyan kişi ve araçları, işlemi yapan birimi ve gayeyi belirleyen ya da değerlendiren kişiyi veya rolü ayrı alanlara yaz. Belirlenemeyen bir rolü tahmin ederek doldurmak yerine 'belirlenmedi' olarak işaretle.

4. Çalışmayı ayırt eden mevcut amaç, kısıt, karar ve açık soruları belirt. Bunların ayrıntılı kayıtları başka bir bölümdeyse aynı dosyadaki ilgili başlığa gönderme yap; ikinci bir geçerli kayıt oluşturma.

5. Tanımı mevcut dosyalar ve gerçekten yapılan işlemlerle karşılaştır. Tanımın dayandığı varsayımları ve henüz doğrulanmamış ifadeleri ayrıca göster. Yeni bir bulgu tanımı değiştiriyorsa eski ve yeni tanımı gerekçesiyle değişiklik kaydına ekle.

### Tamamlanma ölçütü

Bu bölüm, ele alınan işin sınırı ve ayırt edici özellikleri anlaşılabildiğinde; köken, taşıyıcı, eyleyen ve gayeyi belirleyen roller ayrı gösterildiğinde tamamlanmış sayılır. Çözülememiş bir kimlik veya rol sorusu açıkça kaydedilebilir. Bölümün tamamlanması, çalışma içeriğinin bütünüyle doğrulandığı veya bütün işin bittiği anlamına gelmez.

### Kayıt

```markdown
## 1 Varlık Protokolü

Çalışmanın adı ve kısa tanımı: [doldur]

Kapsama giren faaliyetler: [doldur]

Kapsam dışında kalanlar: [doldur]

Ayırt edici özellikler: [doldur]

Köken veya başlangıç gerekçesi: [doldur]

Taşıyıcı kişi araç ve kayıtlar: [doldur]

Eyleyen veya işlemi uygulayan: [doldur ya da belirlenmedi]

Gayeyi belirleyen ve sonucu değerlendiren kişi veya rol: [doldur ya da belirlenmedi]

Tanımın dayandığı varsayımlar ve açık sorular: [doldur]
```

## 2 Mekan Protokolü

Çalışma hafızası ve sürekliliğin yeri, incelenen ölçeğe göre ele alınır. İnsan düzeyinde bilişsel süreçler; kişinin araçlarla yürüttüğü çalışmada notlar, taslaklar ve kullanımları; ortak çalışmada katılımcılar, kayıtlar, kararlar ve devir ilişkileri önem taşır. Yapay zekâ destekli bir düzende ise kullanıma sunulan bağlam, erişilebilen kaynaklar, bunları işe katan süreçler ve insanın yönlendirmesi birlikte değerlendirilir. Dağıtık biliş yaklaşımı, insanlarla teknolojiler arasındaki etkileşimi bütün çalışma çevresi ve koordinasyon ilişkileri içinde incelemek için bir dayanak sunar. Bu açıklama, farklı taşıyıcıların aynı biyolojik veya öznel özelliklere sahip olduğunu varsaymaz. [K2]

Mekân, yalnızca içeriğin bulunduğu adresle açıklanmaz. Bir belgenin klasörde, bir işlemin cihazda veya bir kaydın ortak ortamda bulunması, bunların yürüyen işte nasıl kullanılabildiğini henüz göstermez. Çalışmanın yeri, maddi taşıyıcılarla birlikte erişim, anlamlandırma ve eyleme katılma ilişkilerini de içerir. Kullanılan araç hangi içeriğin görülebildiğini, nasıl değiştirilebildiğini ve başkalarına nasıl aktarılabildiğini etkiler. Bu nedenle mekân salt fiziksel konuma indirgenmediği gibi, maddi ve teknik koşullardan bağımsız bir alan olarak da düşünülmez.

Bir çalışma yerini özgül yapan, hangi soru veya amaç etrafında örgütlendiği ve orada neyin kim tarafından kullanılabildiğidir. Hangi kaynakların ilgili olduğu, hangi kayıtların güncel sayıldığı, terimlerin nasıl anlaşıldığı ve kararların nasıl alındığı bu özgüllüğe katılır. Aynı içeriğe erişen kişilerin içeriği aynı biçimde yorumladıkları veya aynı karar rolünü taşıdıkları varsayılmaz. Ortak bir çalışma alanının anlaşılabilmesi için, katılımcıların neyi bildikleriyle ne yapabildikleri arasındaki ilişkinin de görünür olması gerekir. Dağıtık işleyiş, bu ayrımların kaybolması anlamına gelmez.

Bir bilginin mevcut olması, erişilebilir olması ve etkin biçimde kullanılması ayrı durumlardır. Bulunamayan, anlaşılamayan veya mevcut işle ilişkisi kurulamayan bir kayıt, saklanmasına rağmen devam etmeyi desteklemeyebilir. Buna karşılık bir dış araç, kişinin veya ekibin düşünme ve karar verme biçimine düzenli olarak katılabilir. Genişletilmiş zihin savı, uygun ilişkiler içinde dış kaynakların bilişsel sürecin kurucu parçaları olabileceğini ileri sürer. Bu sav, her aracın ayrı bir özne veya her bağlantılı bütünün tek bir kişi olduğu sonucuyla özdeş değildir. [K3]

~~~text
  .----------------------------------------------------------------.
  |  MEVCUT           saklaniyor                                   |
  |   .--------------------------------------------------------.   |
  |   |  ERISILEBILIR      bulunabiliyor, acilabiliyor         |   |
  |   |   .------------------------------------------------.   |   |
  |   |   |  ETKIN KULLANILAN    anlasiliyor ve yuruyen    |   |   |
  |   |   |                      isle iliskisi kurulmus    |   |   |
  |   |   `------------------------------------------------'   |   |
  |   `--------------------------------------------------------'   |
  `----------------------------------------------------------------'
  bulunamayan, anlasilamayan ya da isle iliskisi kurulamayan kayit,
  saklanmasina ragmen devam etmeyi desteklemeyebilir

  olcek                       yerde onem tasiyan
  insan                       bilissel surecler
  kisi ve araclari            notlar, taslaklar ve kullanimlari
  ortak calisma               katilimcilar, kayitlar, kararlar,
                              devir iliskileri
  yapay zeka destekli duzen   kullanima sunulan baglam, erisilebilen
                              kaynaklar, bunlari ise katan surecler
                              ve insanin yonlendirmesi
~~~

*Çizim 5 — Mekan: mevcut, erişilebilir ve etkin kullanılan; dört ölçek.*

Bir çalışmanın yer değiştirmesi, yalnızca dosyalarının taşınmasıyla tamamlanmış sayılmaz. Devam etmek için gerekli amaç, durum, karar gerekçeleri, kullanılan kavramlar ve açık sorunlar yeni ortamda anlaşılabilmelidir. Araç değiştiğinde bazı ilişkiler yeniden kurulabilir; bunun için geçmişin bütün ayrıntılarının aynı biçimde korunması zorunlu değildir. Buna karşılık içeriğin kopyalanması, bu ilişkilerin de korunduğunu tek başına göstermez. Yer değiştirmede taşıyıcının biçimi ile taşınan çalışma durumunun anlamı ayrı ayrı değerlendirilir; devamın ne ölçüde mümkün olduğu bu ikisinin ilişkisine bağlıdır.

~~~text
   eski ortam                                      yeni ortam
  .----------------.                              .----------------.
  | [dosya][dosya] |      dosyalar tasindi        | [dosya][dosya] |
  | [dosya]        |  ========================>   | [dosya]        |
  `----------------'                              `----------------'

  bu kadari yetmez; yeni ortamda sunlar da anlasilabilmeli:

      amac . durum . karar gerekceleri .
      kullanilan kavramlar . acik sorunlar

  tasiyicinin bicimi   |   tasinan calisma durumunun anlami
  ayri ayri degerlendirilir

  gecmisin butun ayrintilarinin ayni bicimde korunmasi zorunlu degil;
  icerigin kopyalanmasi da iliskilerin korundugunu gostermez
~~~

*Çizim 6 — Yer değiştirme: dosyaların taşınması, çalışmanın taşınması değildir.*

Bu mekân tek bir ekran, konuşma, uygulama veya modelle özdeş değildir; sınırsız biçimde her yerde bulunan bir alan da değildir. Dünyada mevcut her bilgi, belirli bir çalışmanın kullanılabilir parçası sayılmaz. Farklı çalışmaların amaçları ve geçerlilik koşulları farklı olabilir; bir bağlamda anlamlı olan içerik başka bir bağlamda kendiliğinden belirleyici hâle gelmez. İnsanlarla araçların birlikte işlemesi de kişilerin rollerini ve sorumluluklarını belirsiz bir bütün içinde eritmez. Mekânın sınırları, çalışma için gerçekten kurulan ilişkiler üzerinden anlaşılır.

### Masaüstünde uygulama

1. CALISMA_KAYDI.md içindeki 2 Mekan Protokolü bölümüne çalışma klasörünün konumunu ve bu kayıt dosyasının konumunu yaz. Dosya adlarını gerçekten var oldukları biçimde kullan; yerel yolları kendi işletim sistemindeki konumlarına göre doldur.

2. Bu çalışma için 0 Tohum bölümünde seçilmiş kaynakların ve kullanılacak araçların konumlarını kaydet. Başka klasörleri, eski konuşmaları veya hesapları kendiliğinden kaynak havuzuna ekleme. Ek bir kaynağa ihtiyaç doğarsa bu ihtiyacı ve kaynağın mevcut çalışma ile ilişkisini belirt.

3. Seçilen kaynakların açılabildiğini ve içeriklerinin mevcut iş için anlaşılabildiğini kontrol et. Erişilemeyen veya hangi sürümünün geçerli olduğu belirsiz bir kaynağı bu durumuyla kaydet; yalnızca dosyanın bulunduğunu görerek içeriğinin kullanıldığını yazma.

4. Hangi kayıtların etkin olarak kullanılacağını, hangilerinin yalnız başvuru veya geçmişi açıklama amacı taşıdığını belirt. Bu sınıflandırma dosyaları kendiliğinden taşımayı, silmeyi veya paylaşmayı gerektirmez.

5. Üretilecek çıktıların nereye yazılacağını ve ortak çalışmada kimin hangi dosyayı düzenlediğini belirt. Çalışma başka bir klasöre, araca veya kişiye devrediliyorsa gerekli dosyaların bulunabildiğini ve ilgili bağlantıların yeni ortamda anlaşılabildiğini kontrol ederek konum kaydını güncelle.

### Tamamlanma ölçütü

Bu bölüm, mevcut kaydın, seçilmiş kaynakların ve çıktıların nerede bulunduğu anlaşılabildiğinde; erişim veya sürüm belirsizlikleri görünür olduğunda tamamlanmış sayılır. Bir dosyanın varlığı, içeriğinin doğru, güncel ya da bu çalışmada kullanılmasına gerek bulunduğu sonucunun yerine geçmez.

### Kayıt

```markdown
## 2 Mekan Protokolü

Çalışma klasörünün konumu: [doldur]

Geçerli çalışma kaydının konumu: [doldur]

Kullanılan uygulama ve araçlar: [doldur]

Seçilen kaynakların konumları ve işteki rolleri: [doldur]

Erişim ve geçerli sürüm durumu: [doldur; belirsizlikleri belirt]

Etkin kullanılan kayıtlar: [doldur]

Yalnız başvuru veya geçmişi açıklama amacı taşıyan kayıtlar: [doldur]

Çıktıların yazılacağı konum: [doldur]

Dosyaları düzenleyen kişi veya roller: [doldur]

Yer değişikliği veya devir sonrası kontrol: [uygulanmadı ya da yapılan kontrol ve sonucu]
```

## 3 Usül Protokolü

Çalışma hafızası ve sürekliliğin usulü, yürüyen işin durumunu anlaşılabilir ve kullanılabilir tutan işlemlerin birbirine bağlanmasıyla tarif edilir. Seçme, ilişkilendirme, güncelleme, açık kalanları koruma, devretme, yeniden değerlendirme ve gerektiğinde etkin alandan çıkarma bu işleyişin temel hareketleridir. Bunlar bütün insan belleğini açıklayan tek bir mekanizma veya her işe uygulanacak değişmez bir işlem sırası olarak sunulmaz. Ortak ve teknik çalışmada önemli olan, hangi işlemin neye hizmet ettiğinin ve diğer işlemlerle nasıl ilişkilendiğinin açıklanabilmesidir.

Seçme, o anki faaliyet bakımından ilgili içeriği öne çıkarır; ilişkilendirme ise bu içeriğin sorulara, kararlara ve sonuçlara nasıl bağlandığını korur. Bu seçim yalnızca bilgi azaltmak değildir. Daha önce geri planda kalan bir ayrıntı, yeni bir bulguyla birlikte önem kazanabilir ve çalışma odağını değiştirebilir. Bu nedenle mevcut odağın korunmasıyla odağın gerektiğinde yenilenmesi birlikte düşünülür. Tutulan bir bilginin işteki rolü, yalnızca onun kayda alınmış olmasından değil, düşünceyi veya eylemi nasıl etkileyebildiğinden anlaşılır.

Gözlem, yorum, varsayım, öneri ve alınmış karar farklı durumlar olarak korunur. Bir beklentinin özetler içinde doğrulanmış bilgiye, tartışılmış bir seçeneğin kabul edilmiş karara dönüşmesi, içeriğin anlamını değiştirir. Bir ifadenin konusu kadar hangi koşulda ve hangi kesinlik düzeyinde kullanıldığı da devam eden çalışma için önemlidir. Bir kaydın geçmişte bulunması, onun bugünkü işlemi kendiliğinden belirlemesini gerektirmez. Teknik bir sistemin hedef veya talimat izlemesi de bu hedefin kaynağı ve sahibi olduğunu tek başına göstermez.

Güncelleme, yeni içeriği eklemekle birlikte önceki içeriğin durumunu yeniden ele almayı kapsayabilir. Bir varsayım değiştiğinde, ona dayanan kararların ve sonuçların da değerlendirilmesi gerekebilir. Değişikliğin gerekçesi ile etkisinin anlaşılabilir olması, sonraki çalışmanın neyi devraldığını belirlemeyi sağlar. Aynı zamanda bilinmeyenler, tamamlanmamış kontroller ve denenmemiş seçenekler görünür tutulur. Açık bir soru kayıtta yok sayıldığında çözülmüş olmaz. Çalışmanın durumunu anlatan düzen, ilerleme izlenimi üretmek için belirsizliği kesinliğe dönüştürmez veya eksik bilgiyi varsayımla tamamlanmış gibi göstermez.

~~~text
  bir ifadenin durumu:

    gozlem . dogrulanmis bilgi . yorum . varsayim . oneri . karar

  ozetlerken kayma:

    beklenti              - - x - ->   dogrulanmis bilgi
    tartisilmis secenek   - - x - ->   kabul edilmis karar
    tekrarlanan oneri     - - x - ->   karar

  yaninda tutulur:
    dogrulanmis bilgi     dayanagi
    karar                 karari veren kisi ya da rol; gerekce

  bir varsayim degisince, ona dayanan kararlar ve sonuclar da
  yeniden degerlendirilir
  acik bir soru kayitta yok sayildiginda cozulmus olmaz
~~~

*Çizim 7 — Usül: bir ifadenin durumu ve özetlerken kayma.*

Devir, başka bir kişinin veya aynı kişinin daha sonraki bir zamanda işi anlayarak sürdürebilmesine yönelir. Bunun için bütün geçmişin eksiksiz aktarılması her zaman gerekli değildir; amaç, mevcut sonuç, geçerli kararlar, gerekçeler, açık sorunlar ve sıradaki anlamlı adım arasında yeterli bağ kurulması gerekir. İhtiyaç duyulan ayrıntı, işin niteliğine göre değişir. Yeniden başlama sırasında bu durumun hâlâ geçerli olup olmadığı da değerlendirilir. Yeni bilgiler veya değişen koşullar, önceki noktadan devam etmek yerine farklı bir adımın seçilmesini gerektirebilir.

Tamamlanan, geçersizleşen veya mevcut işle ilgisini kaybeden içerik etkin kullanımdan çıkarılabilir; bu, bütün izlerinin silinmesiyle aynı işlem değildir. Geçmiş bir kararın anlaşılması için bir kayıt korunurken bugünkü kararda belirleyici olmaktan çıkabilir. Bu usul, kaydetme veya özetleme işlemlerinden herhangi biriyle özdeş değildir. Özeti kısa tutmak gerekçeyi kaybettiriyorsa, kaydı çoğaltmak güncel durumu belirsizleştiriyorsa veya otomasyon karar ilişkilerini görünmez kılıyorsa işleyişin amacı karşılanmamış olabilir. Değerlendirme, bir sonraki düşüncenin veya eylemin mevcut durumu anlayabilmesine dayanır.

~~~text
                    .---------------- ETKIN ALAN ----------------.
  icerik -- sec --> |  iliskilendir    soruya, karara, sonuca    |
                    |  guncelle        yeni bilgi + eskinin      |
                    |                  durumu                    |
                    |  acik kalanlari  bilinmeyen, yapilmamis    |
                    |  koru            kontrol, denenmemis yol   |
                    |  yeniden degerlendir                       |
                    `--------+---------------------------+-------'
                             |                           |
                          devret                etkin alandan cikar
                  baskasina ya da               silmek degil; gecmisi
                  sonraki bir zamana            anlamak icin iz kalir

  devirde yeter:  amac . mevcut sonuc . gecerli kararlar . gerekceler .
                  acik sorunlar . siradaki anlamli adim
  butun gecmisin eksiksiz aktarilmasi her zaman gerekli degildir

  kaydetmek ya da ozetlemek bu usulun kendisi degildir:
    kisa ozet gerekceyi kaybettiriyorsa . cogalan kayit guncel durumu
    belirsizlestiriyorsa . otomasyon karar iliskilerini gizliyorsa
~~~

*Çizim 8 — Etkin alan ve usulün yedi hareketi.*

### Masaüstünde uygulama

1. CALISMA_KAYDI.md içindeki 3 Usül Protokolü bölümünde sıradaki somut işlemi ve bu işlemin hangi soruya ya da gayeye hizmet ettiğini yaz. İşlem birden fazla adıma bağlıysa önce gerekli olan adımı belirle.

2. İşlemde kullanılacak ifadeleri gözlem, doğrulanmış bilgi, yorum, varsayım, öneri veya karar olarak ayırt et. Doğrulanmış bilgi için dayanağı; karar için kararı veren kişi veya rolü ve gerekçeyi kaydet. Bir öneriyi yalnızca tekrarlandığı için karar olarak işaretleme.

3. Mevcut görev kapsamında seçilmiş işlemi yürüt. Girdiyi, oluşan çıktıyı ve gerçekleşme durumunu kaydet. Hazırlanan bir yönergeyi uygulanmış işlem, denenmemiş bir yöntemi başarılı sonuç olarak yazma.

4. Çıktıyı amacına uygun bir kontrolle değerlendir. Örneğin bir metinde anlamın korunmasını, bir dosya düzeninde gerekli dosyaların bulunabilirliğini kontrol et. Yapılan kontrolü ve gözlenen sonucu yaz; yapılmamış bir kontrolü tamamlanmış gösterme.

5. Değişen bilgi veya kararları gerekçeleriyle güncelle. Geçersizleşen bir ifadeyi etkin kullanımdan çıkarırken önceki durumun anlaşılması için gerekli izi değişiklik kaydında koru. Bu adım dosyaların silinmesini gerektirmez.

6. Açık soruları, engelleri ve sıradaki anlamlı adımı aynı kayıtta belirt. Ara verilecek veya iş devredilecekse mevcut sonuç, geçerli kararlar, gerekçeler ve devam noktası bu dosyadan anlaşılabilsin.

### Tamamlanma ölçütü

Bu bölüm, hangi işlemin neden seçildiği, hangi bilgi durumlarına dayandığı ve gerçekten ne üretildiği görülebildiğinde tamamlanmış sayılır. Sonuç henüz elde edilmediyse işlem 'henüz uygulanmadı', 'kısmen uygulandı' veya 'engellendi' gibi gerçek durumuyla bırakılır; eksik adım ile sonraki işlem açıkça gösterilir.

### Kayıt

```markdown
## 3 Usül Protokolü

Seçilen sıradaki işlem: [doldur]

İşlemin ilgili olduğu soru veya gaye: [doldur]

Kullanılan girdiler ve kaynakları: [doldur]

Bilgilerin durumu: [gözlem / doğrulanmış bilgi / yorum / varsayım / öneri / karar olarak belirt]

Karar veren kişi veya rol ve karar gerekçesi: [doldur; karar yoksa belirt]

İşlemin gerçekleşme durumu: [henüz uygulanmadı / uygulandı / kısmen uygulandı / engellendi]

Oluşan çıktı ve konumu: [doldur; henüz oluşmadıysa belirt]

Yapılan kontrol ve gözlenen sonuç: [doldur; kontrol yapılmadıysa belirt]

Değişen ifade veya karar ve değişiklik gerekçesi: [doldur]

Açık sorular veya engeller: [doldur]

Sıradaki anlamlı adım: [doldur]
```

## 4 Zaman Protokolü

Çalışma hafızası, faaliyetin o anda işleyen durumuyla ilişkilidir; süreklilik ise bu durumun önceki ve sonraki durumlarla bağında bulunur. Buradaki an yalnızca takvimdeki bir nokta değildir. Nelerin tamamlandığını, hangi kararların geçerli olduğunu, neyin belirsiz kaldığını ve hangi eylemlerin artık mümkün olduğunu içerir. Bir çalışmanın ayırt edici zamanı, bu öğelerin o andaki birleşimi üzerinden anlaşılır. Aynı gün içinde önemli bir değişim gerçekleşebilir; uzun zaman geçmesine rağmen belirli gerekçeler veya amaçlar geçerliliğini koruyabilir.

Bir anı diğerlerinden farklı yapan, yönelinen amaçla birlikte eldeki dayanakların, kararların, açık soruların ve eylem olanaklarının durumudur. Yeni bir bulgu daha önce mümkün olmayan bir kararı mümkün kılabilir; tamamlanan bir işlem sıradaki adımı değiştirebilir. Süreklilik, bu geçişlerin anlamını korumaya yönelir. Geçişin anlaşılması, her önceki duruma aynı ağırlığın verilmesini gerektirmez. Hangi değişimin çalışmanın yönünü etkilediği ve hangi öğelerin geçerli kaldığı, mevcut faaliyetle ilişkisi içinde değerlendirilir.

Bir bilginin ortaya çıktığı zaman, geçerli olduğu dönem ve son kez kontrol edildiği zaman birbirinden ayrılır. Bunlar aynı olmak zorunda değildir. Eski bir kayıt hâlâ işe yarayabilir; yeni kaydedilen bir bilgi ise güncelliğini yitirmiş bir kaynağa dayanabilir. Bu nedenle güncellik, en son yazılan içeriğin otomatik olarak tercih edilmesiyle açıklanmaz. Bilginin hangi koşullarda geçerli olduğunun anlaşılması gerekir. Tarih damgası bu değerlendirmeye katkıda bulunabilir, fakat içeriğin doğruluğunu veya bugünkü ilgisini tek başına belirlemez.

~~~text
  bir bilginin uc ayri zamani:

  ortaya cikis      gecerli oldugu donem ya da kosul        son kontrol
      o===========================================. . . .       o
      |                                                         |
  ne zaman soylendi?        hangi kosulda gecerli?      en son ne zaman
                                                        bakildi?

  eski bir kayit hala ise yarayabilir;
  yeni yazilan bir bilgi eskimis bir kaynaga dayanabilir

  guncellik   =/=   en son yazilanin otomatik tercih edilmesi
  tarih damgasi katkida bulunur; dogrulugu ya da bugunku ilgiyi
  tek basina belirlemez
~~~

*Çizim 9 — Zaman: bir bilginin üç ayrı zamanı.*

Bir çalışma durduğunda, o anda etkin olarak işlenen içerikle daha sonra devam etmeyi mümkün kılacak izler ayrılır. Uzun süreli bir projenin varlığı, tek bir etkin çalışma durumunun bütün süre boyunca kesintisiz korunduğu anlamına gelmez. Farklı çalışma anlarında gerekli durum, korunmuş kayıtlardan ve ilişkilerden yeniden kurulabilir. Yeniden kurulan durum öncekinin eksiksiz kopyası olmak zorunda değildir; yeni bilgiler eklenebilir ve bazı varsayımlar bırakılabilir. Devamın niteliği, bu değişikliklerin anlaşılabilirliği ve mevcut amaçla ilişkisinde ortaya çıkar.

Zamansal süreklilik, yalnızca geçmiş hakkında tutarlı konuşabilmekle eş tutulmaz. Önceki işlemlerin mevcut duruma nasıl etki ettiği, kararların nasıl devralındığı ve değişikliklerin hangi gerekçelerle yapıldığı da incelenir. Bir geçmiş anlatısı ile anlatılan geçmişin gerçek bağlantıları farklı şeylerdir. Kayıtların kopyalanması, eyleyenin bütünüyle kopyalandığını göstermediği gibi, aynı adın sürmesi de aynı çalışmanın devam ettiğini garanti etmez. İşlevsel devamlılık, anlatısal tutarlılık ve bir kişinin zaman içindeki kimliği birbirleriyle ilişkili, fakat ayrı sorular olarak korunur.

Bu zaman anlayışı, zamandan bağımsız bir depoyu, sonsuza uzanan tek bir şimdiyi veya geçmişin bugünü bütünüyle belirlemesini varsaymaz. Kesinti, tek başına sürekliliğin kaybı değildir; kesintisiz çalışma da anlamlı ilerlemenin garantisi değildir. Önceki durum bugünkü değerlendirmeye katkıda bulunabilir, ancak değişen koşulların yerini alamaz. Bir çalışmanın devamı kadar durması, tamamlanması veya yeni bir soruya dönüşmesi de zaman içindeki durumunun parçasıdır. Zaman Protokolü bu geçişleri, yalnızca geçen süreye değil, çalışmanın anlamındaki ve olanaklarındaki değişime bağlar.

~~~text
   calisma ani 1             ara               calisma ani 2
  .--------------.                            .-----------------.
  | etkin durum  |      korunan izler:        | yeniden kurulan |
  | (o an        | -->  devam noktasi,  . . > | durum           |
  |  islenen     |      yeniden kontrol       |  + yeni bilgi   |
  |  icerik)     |      edilecekler           |  - birakilan    |
  `--------------'                            |    varsayim     |
                                              `-----------------'
  donuste once karsilastir:
    amac, kaynak, kisit ya da karar degisti mi?
  yeniden kurulan durum oncekinin eksiksiz kopyasi olmak zorunda degil

  kesinti, tek basina surekliligin kaybi degildir;
  kesintisiz calisma da anlamli ilerlemenin garantisi degildir

  iliskili ama ayri uc soru:
    islevsel devamlilik  |  anlatisal tutarlilik  |
    bir kisinin zaman icindeki kimligi
~~~

*Çizim 10 — Ara verme ve yeniden kurma: dönüşte önce karşılaştırılır.*

### Masaüstünde uygulama

1. CALISMA_KAYDI.md içindeki 4 Zaman Protokolü bölümüne bu çalışma oturumunun tarihini ve saat dilimini yaz. Saat kaydediliyorsa YYYY-MM-DD HH:MM UTC±HH:MM gibi anlaşılabilir bir biçim kullan; bilinmeyen geçmiş tarihleri tahmin ederek doldurma.

2. Çalışmanın mevcut aşamasını, tamamlanan işlemleri, açık kalanları ve şu anda mümkün olan sonraki adımı belirt. Geçen süre ile gerçekleşen ilerlemeyi ayrı değerlendir.

3. Kararı etkileyen bilgiler için, biliniyorsa bilginin ortaya çıktığı zamanı, geçerli olduğu dönemi veya koşulu ve son kontrol zamanını ayrı yaz. Bu tarihlerden biri bilinmiyorsa 'bilinmiyor' olarak bırak; yeni dosya tarihini içerik doğruluğunun kanıtı sayma.

4. Ara verme sırasında, işin durduğu noktayı ve devam etmeden önce yeniden kontrol edilmesi gereken koşulları kaydet. Bu kayıt daha sonra aynı çalışma sürdürülürken kullanılacak devam noktasıdır; ilgisiz başka çalışmalara kendiliğinden aktarılmaz.

5. Aynı çalışmaya geri dönüldüğünde önceki devam noktasını mevcut koşullarla karşılaştır. Gerçekte değişen amaç, kaynak, kısıt veya kararları tarih ve gerekçeleriyle kaydet; devam, yeniden değerlendirme veya kapanış durumunu buna göre güncelle.

### Tamamlanma ölçütü

Bu bölüm, kaydın hangi ana ve çalışma aşamasına ait olduğu, o anda nelerin geçerli olduğu ve kesinti sonrasında neyin yeniden kontrol edileceği anlaşılabildiğinde tamamlanmış sayılır. Bilinmeyen tarihler açıkça bırakılabilir. Bir tarih damgası veya kesintisiz anlatı, gerçekleşmiş işlem ve sonuçların kaydı yerine kullanılmaz.

### Kayıt

```markdown
## 4 Zaman Protokolü

Oturum tarihi ve saat dilimi: [doldur]

Son güncelleme zamanı: [doldur]

Çalışmanın mevcut aşaması: [doldur]

Tamamlanan işlemler: [doldur]

Açık kalan işler ve şu an mümkün olan sonraki adım: [doldur]

Kararı etkileyen bilginin ortaya çıkış zamanı: [biliniyorsa doldur]

Bilginin geçerli olduğu dönem veya koşul: [doldur ya da bilinmiyor]

Bilginin son kontrol zamanı: [doldur ya da kontrol edilmedi]

Ara verme noktası: [doldur; ara verilmediyse belirt]

Devam etmeden önce yeniden kontrol edilecekler: [doldur]

Yeniden başlama sırasında görülen değişiklikler ve gerekçeleri: [uygulanmadı ya da doldur]
```

## 5 Gaye Protokolü

Çalışma hafızası ve süreklilik için her durumda geçerli, kendiliğinden verilmiş tek bir nihai amaç varsayılmaz. Öğrenme, araştırma, sanat, ortak karar verme ve teknik uygulamalar farklı gayeler taşıyabilir. Mevcut konuşmada önerilen genel yön, bir kişinin veya ortaklığın deneyimden yararlanarak, değişen koşulları dikkate alarak ve gerektiğinde yönünü düzelterek anlamlı eylemde bulunabilmesini desteklemektir. Bu yön, yalnızca üretimi hızlandırmayı değil, anlamayı, öğrenmeyi, hatayı fark etmeyi ve gerektiğinde bir çalışmayı sonlandırmayı da kapsar.

Gayeyi izlemek, gayenin kaynağı veya sahibi olmakla aynı değildir. Bir teknik sistemin hedefi gerçekleştirmeye yönelmesi, hedefin neden değerli bulunduğunu açıklamaz. Bir çalışma içinde amacı belirleyen, uygulayan, değerlendiren ve sonuçlarıyla karşılaşan roller farklılaşabilir. Bu rollerin birbirleriyle ilişkisi, somut iş üzerinden açıklanır. Bir amacın varlığı, onun haklılığını da kendiliğinden kanıtlamaz. Hedefin işleyişi açıklamadaki rolü ile hedefin sürdürülmeye değer olup olmadığına ilişkin değerlendirme ayrı tutulur; herhangi bir bileşen sırf hedef izlediği için bütün gayenin otoritesi sayılmaz.

Amaçla ilişkinin korunması, tutulan bilgi ve sürdürülen faaliyetin neye katkıda bulunduğunun anlaşılmasını gerektirir. Bununla birlikte amaç her zaman başlangıçta tam belirlenmiş değildir. Araştırma ve keşifte sorunun kendisi değişebilir; önceki bir yönün artık yeterli olmadığı anlaşılabilir. Böyle durumlarda süreklilik, yalnızca ilk hedefi korumakla değil, hedefin neden değiştiğini açıklayabilmekle sağlanır. Karar gerekçelerinin korunması, hangi koşullar değiştiğinde hangi kararların yeniden ele alınacağını görmeye yardımcı olur. Öğrenme, önceki değerlendirmelere mutlak bağlılık anlamına gelmez.

Düzeltilebilirlik ve belirsizliğin dürüstçe korunması, önerilen gayeye hizmet eden temel niteliklerdir. Yeni bir kanıt veya daha iyi bir açıklama karşısında yön değiştirilebilmelidir. Bilinmeyenlerin görünür olması, onları çözmek için gerekli çalışmanın belirlenmesini sağlar. Yapay bir kesinlik ise sonraki adımı yanlış bir temele yerleştirebilir. Amaçlı eylemin değeri, yalnızca önceki kararla tutarlı görünmesinden çıkarılmaz. Bir kararın neden değiştirildiğinin anlaşılabilir olması, bazen kararın aynen korunmasından daha anlamlı bir devam ilişkisi kurabilir.

Aktarılabilirlik, devam edecek kişinin veya sürecin gerekli durumu geçmişi baştan yaşamak zorunda kalmadan anlayabilmesini destekler. Bu aktarımın kapsamı, işin gerektirdiği ayrıntıyla belirlenir. Daha fazla kayıt, bağlantı veya tarihçe kendi başına daha iyi bir çalışma anlamına gelmez. Tutulan içeriğin ilgisi, doğruluğu, geçerlilik koşulları ve kullanım biçimi birlikte önemlidir. Hafıza düzeninin büyümesi, hizmet ettiği faaliyetten bağımsız bir başarı ölçütü olarak alınmaz. Gayenin değerlendirilmesinde, sonraki eylemin ne ölçüde anlamlı ve düzeltilebilir bir zemine kavuştuğuna bakılır.

Tamamlanabilme ve gerektiğinde bırakabilme de amaçla ilişkinin parçasıdır. Bir işin ne zaman bitmiş sayılacağı veya hangi koşullarda sürdürülmeyeceği anlaşılmalıdır. Süreklilik, her koşulda devam etme yükümlülüğü doğurmaz; durma, yeniden başlama veya başka bir soruya geçme gerekçeli olabilir. Hafıza, neden durulduğunu, ne öğrenildiğini ve hangi koşullarda yeniden başlanabileceğini de taşıyabilir. Nihai gaye her şeyi hatırlamak, geçmişle her durumda aynı fikirde kalmak veya kişiyi önceki ifadelerine sabitlemek değildir. Çalışma, hizmet ettiği anlamlı eylem bakımından değerlendirilir.

~~~text
  onerilen genel yon:
    deneyimden yararlanarak, degisen kosullari dikkate alarak ve
    gerektiginde yonunu duzelterek anlamli eylemde bulunabilmek

  bu yone hizmet eden nitelikler:
    duzeltilebilirlik           yeni kanit karsisinda yon degisebilir
    belirsizligin durustce      bilinmeyen gorunur kalir; yapay
    korunmasi                   kesinlik sonraki adimi yanlis temele
                                yerlestirir
    aktarilabilirlik            gecmisi bastan yasamadan devam
    tamamlanabilme,             is ne zaman biter, hangi kosulda
    birakabilme                 surdurulmez

  gayeyi izlemek   =/=   gayenin kaynagi ya da sahibi olmak
  roller ayrilabilir:   belirleyen . uygulayan . degerlendiren .
                        sonuclariyla karsilasan

  nihai gaye degildir:
    her seyi hatirlamak . gecmisle her durumda ayni fikirde kalmak .
    kisiyi onceki ifadelerine sabitlemek
  daha fazla kayit, kendi basina daha iyi bir calisma degildir
~~~

*Çizim 11 — Gaye: önerilen yön, ona hizmet eden nitelikler ve nihai gaye olmayanlar.*

### Masaüstünde uygulama

1. CALISMA_KAYDI.md içindeki 5 Gaye Protokolü bölümünde mevcut gayeyi bir veya iki cümleyle yaz. 0 Tohum bölümündeki başlangıç niyetiyle ilişkisini belirt; çalışma sırasında yön değiştiyse ilk niyetin zaten yeni gayeyi içerdiğini varsayma.

2. Gayenin kim için anlamlı olduğunu, kim tarafından belirlendiğini ve sonucu kimin değerlendireceğini mevcut görevde bilinen kişi veya roller üzerinden kaydet. İşlemi uygulayan araçla gayeyi belirleyen rolü ayrı göster.

3. Tamamlanmayı gözlemlemeye yarayacak ölçütleri yaz. Görevin sağlamadığı sayısal hedefleri icat etme; gerektiğinde anlamın korunması, belirlenen sorunun yanıtlanması veya istenen çıktının kullanılabilir olması gibi somut nitel ölçütler kullan.

4. Mevcut çıktıyı bu ölçütlerle karşılaştır ve karşılanan, karşılanmayan ya da henüz değerlendirilmeyen ölçütleri dayanaklarıyla belirt. Dosyanın üretilmesini, içeriğin doğrulanması veya ilgili kişi tarafından benimsenmesiyle eşitleme.

5. Yeni bir bulgu veya değişen koşul gayeyi etkiliyorsa eski gayeyi, önerilen veya kararlaştırılmış yeni yönü ve gerekçeyi ayrı kaydet. Öneri ile alınmış kararın durumunu koru; mevcut görevin kapsamı içinde alınabilen kararlar için gereksiz tekrar onayı üretme.

6. Çalışmanın devam etmesi, yönünün yeniden değerlendirilmesi, ara verilmesi veya kapanması bakımından mevcut durumu belirt. Ulaşılan sonucu ve açık kalanları 6 Kökleşme bölümünde tamamlanacak kapanışa dayanak olacak biçimde kaydet.

### Tamamlanma ölçütü

Bu bölüm, çalışmanın neye ve kimin adına yöneldiği, başarının ne sayılacağı ve mevcut sonucun bu ölçütlerle ilişkisi anlaşılabildiğinde tamamlanmış sayılır. Gayenin karşılanması ile çalışma aşamasının kapanması ayrı değerlendirilebilir. Karşılanmamış ölçütler veya henüz karara bağlanmamış yön değişiklikleri açık durumlarıyla korunur.

### Kayıt

```markdown
## 5 Gaye Protokolü

Mevcut gaye: [doldur]

Başlangıç niyetiyle ilişkisi: [doldur]

Gayenin anlamlı olduğu kişi veya ortaklık: [doldur]

Gayeyi belirleyen kişi veya rol: [doldur ya da belirlenmedi]

Sonucu değerlendiren kişi veya rol: [doldur ya da belirlenmedi]

Tamamlanma veya başarı ölçütleri: [doldur]

Ölçütlerin mevcut durumu ve dayanakları: [karşılandı / karşılanmadı / henüz değerlendirilmedi]

Gaye değişikliği varsa eski yön yeni yön ve gerekçe: [doldur; yoksa belirt]

Yön değişikliğinin durumu: [öneri / kararlaştırıldı / değerlendirilmedi / değişiklik yok]

Mevcut devam veya kapanış durumu ve gerekçesi: [doldur]
```

## 6 Kökleşme (Bitiş) Protokolü

Kökleşme Protokolü, çalışma sonunda elde edilenleri dayanakları, ilişkileri ve geçerlilik sınırlarıyla birlikte yerleştirir. Bitiş, bu çalışma aşamasının ne ürettiği bilinerek kapanmasıdır. Bir sonuç hangi soruya karşılık geldiğiyle, bir karar hangi gerekçeye dayandığıyla, bir açık soru neden açık kaldığıyla birlikte kaydedilir. Böylece sonuçlar yalnızca tekrar edilebilir ifadeler olarak kalmaz; nasıl ortaya çıktıkları ve hangi koşullarda kullanılabilecekleri de anlaşılabilir hâle gelir. Kapanışın konusu, gerçekten elde edilmiş olan durumdur; tamamlanmış görünmesi istenen durum değildir.

Bu protokol, önceki beş bölümde kurulan ilişkileri birlikte ele alır. Tanımlanan varlık, çalışmanın mekânı, uygulanan usul, mevcut zaman ve yönelinen gaye arasında açıklanmamış bir boşluk bulunup bulunmadığı değerlendirilir. Usulün gayeye nasıl katkıda bulunduğu veya bir sonucun hangi koşullarda geçerli olduğu belirsiz kalmışsa, bu belirsizlik kapanıştan çıkarılmaz. Bir aşama, bazı sonuçları gerekçelendirilmiş, bazı önerileri sınanmamış ve bazı soruları açık olarak tamamlanabilir. Bütün belirsizliklerin çözülmesi, her çalışma aşamasının kapanması için zorunlu koşul sayılmaz; açıkların sonraki kullanıma etkisi belirtilir.

Bir içeriğin kayda alınması, onun doğrulanmış, benimsenmiş veya her durumda geçerli olduğu anlamına gelmez. Kapanışta gözlem, yorum, varsayım, öneri ve karar ayrımları korunur. Bir deneme yapılmışsa sonucu ve dayanağı gösterilir; yapılmamış bir kontrol yapılmış gibi yazılmaz. Kullanıcı veya başka bir katılımcı tarafından benimsenmiş bir karar bulunuyorsa, bunun dayanağı mevcut kayıtta gösterilebilir. Benimsenme bilgisi yoksa kayıt bu durumu değiştirmez. Kökleşme, eksik kesinliği dil yoluyla tamamlamaya veya bir öneriyi geriye dönük olarak bağlayıcı karara çevirmeye hizmet etmez.

Kapanış kaydı, başlangıçla elde edilen durum arasındaki farkı açıklayabilmelidir. İlk soru değişmiş, bir varsayım bırakılmış veya gaye daha açık hâle gelmiş olabilir. Bu değişiklikler, Tohum kaydını yeniden yazarak gizlenmez; gerekçeleriyle ilişkilendirilir. Sürekliliğin taşıdığı şey, başlangıca her koşulda bağlılık değil, değişimin anlaşılabilirliğidir. Aynı nedenle, önceki metinlerle düzenlenmiş sonuçlar ayırt edilebilir biçimde korunur. Hangi içeriğin kaynak, hangisinin sentez veya uygulama sonucu olduğu görülebilmeli; aynı şeyin farklı kopyaları birbirinden bağımsız güncel kayıtlar gibi kullanılmamalıdır.

Masaüstünde kökleşme, tamamlanan çıktıların bulunabilir olması ve ortak çalışma kaydının kapanış durumunu yansıtmasıyla gerçekleştirilir. Çıktıların dosya yolları, sürümü veya tarihi ve gerekli kaynak bağlantıları kayda eklenir. Amaç, bütün dosyaları çoğaltmak yerine, hangi dosyanın hangi sonucu taşıdığını anlaşılır kılmaktır. Kayıtla dosyalar arasındaki ilişkinin kontrolü, içeriğin yeniden anlaşılmasına yardımcı olur. Tamamlanmış bir dosya bulunduğu doğrulanmadan varmış gibi gösterilmez. Kapanış için çalışmanın kapsamı dışında silme, taşıma, kurulum veya başkalarına gönderme işlemi yapılması gerekmez.

Kökleşme, elde edilenleri dokunulmaz hâle getirmez ve her yeni bağlama otomatik taşıma izni vermez. Daha sonra yeniden ele alma ihtiyacı doğarsa, yeni çalışma kendi sorusu ve sınırları içinde neyi devralacağını belirler. Önceki sonuçların hangi değişiklik veya bulgu karşısında yeniden değerlendirilmesi gerektiği kapanışta belirtilebilir. Bitiş, devamı zorunlu kılmadan yeniden ele almayı mümkün kılar. Çalışmanın tamamlanması, askıya alınması veya gerekçeli biçimde bırakılması farklı durumlar olarak kaydedilir. Bunların hiçbiri tek başına bütün gayeye ulaşıldığını, bütün soruların çözüldüğünü veya aynı işlemin süresiz sürdürülmesi gerektiğini göstermez.

~~~text
  her sey dayanagiyla birlikte yerlesir:
    sonuc        <-->   hangi soruya karsilik geldigi
    karar        <-->   hangi gerekceye dayandigi
    acik soru    <-->   neden acik kaldigi

  [0] baslangic  -------- fark aciklanir -------->  elde edilen durum
      tohum kaydi yeniden yazilarak gizlenmez;
      surekliligin tasidigi sey, degisimin anlasilabilirligidir

  durum:    Tamamlandi   |   Askida   |   Gerekceli olarak birakildi

  kapanisin konusu:  gercekten elde edilmis olan durum
                     (tamamlanmis gorunmesi istenen durum degil)

  koklesme sunlari yapmaz:
    elde edileni dokunulmaz kilmaz
    her yeni baglama otomatik tasima izni vermez
    bir oneriyi geriye donuk olarak baglayici karara cevirmez
    ayni seyin kopyalarini ayri ayri guncel kayit saymaz
~~~

*Çizim 12 — Kökleşme: her şey dayanağıyla yerleşir; üç kapanış durumu.*

### Masaüstünde uygulama

1. İlgili çalışmanın `kayitlar/<calisma-kimligi>/CALISMA_KAYDI.md` dosyasını aç. 0–5 bölümlerindeki mevcut durumu gözden geçir; doldurulmamış alanları tamamlanmış kabul etme.
2. Başlangıç sorusuna verilen yanıtı ve gerçekten elde edilen sonucu `6 Kökleşme (Bitiş) Protokolü` bölümüne yaz. Başlangıç niyeti veya gaye değiştiyse gerekçesini belirt.
3. Sonuçların dayanaklarını ve durumlarını kaydet. Yapılan kontrolleri somut sonuçlarıyla göster; önerileri, varsayımları ve henüz yapılmamış kontrolleri ayrı tut.
4. Son dosyaların yollarını ve ilgili kaynakları kayda ekle. Dosyaların açıldığını, doğru sürüme işaret ettiğini ve içerikte eksik bölüm veya yanlış bağlantı bulunmadığını işin gerektirdiği ölçüde kontrol et.
5. Açık soruları, kalan işleri ve yeniden değerlendirmeyi gerektirecek koşulları yaz. Sonraki bir çalışma için gerekli olabilecek durumu anlaşılır kıl; başka bağlamlara otomatik devir varsayma.
6. Aşamanın durumunu `Tamamlandı`, `Askıda` veya `Gerekçeli olarak bırakıldı` şeklinde belirt. Kapanış gerekçesini ve tarihini yaz, ortak kaydı ve ilgili çıktıları kaydet.

### Tamamlanma ölçütü

Aşamanın sonucu, dayanakları, çıktı konumları, açık kalanları ve kapanış durumu ortak çalışma kaydından anlaşılabilir durumdadır. Yapılan işlemlerle yapılması önerilenler ayrılmıştır. Yeniden ele almayı gerektirecek koşullar veya bu konuda henüz bir belirleme yapılmadığı kayıtlıdır. Kapanış, belirsizliği ve eksikleri gizlemeden gerçekleştirilmiştir.

### Kayıt

```markdown
## 6 Kökleşme (Bitiş) Protokolü

Kapanış tarihi ve saati:

Başlangıç sorusuna karşılık elde edilen sonuç:

Başlangıçtan bu yana değişen yön veya gaye ve gerekçesi:

Sonuçların dayanakları ve durumları:

Gerçekleştirilen kontroller ve sonuçları:

Son çıktıların dosya yolları ve sürüm veya tarih bilgisi:

Açık sorular ve kalan işler:

Sonuçların geçerlilik sınırları:

Yeniden ele almayı gerektirecek koşullar:

Durum: Tamamlandı / Askıda / Gerekçeli olarak bırakıldı

Kapanış gerekçesi:
```

## Ek A Soru yanıt kaydı

İlk iki sorunun ve yanıtların tam metinleri aşağıda korunmuştur. Kaynak işaretleri son bölümdeki kaynakçaya karşılık gelir.

### Soru 1

Geçmiş bağlamları buraya taşıma. Burası ile sınırlı kalma.

**Çalışma Hafızası ve Süreklilik**

Nedir? Onu o yapan nelerdir? Neler değildir?\
Nerededir? Bu yeri, oraya has bir yer yapan nelerdir? Neler değildir?\
Nasıl işler yapar? Bu yaptıklarını, ona has yapan nelerdir? Neler değildir?\
Hangi andadır? Bu anı, diğer zamanlardan farklı yapan nelerdir? Neler değildir?\
Hangi nihai amaca hizmet eder? Bu nihai amaca ulaştıran nelerdir? Neler değildir?

### Yanıt 1

**Çalışma Hafızası ve Süreklilik**

**Çalışma hafızası, yürütülen bir iş için gerekenleri etkin olarak elde tutmayı ve işlemeyi sağlar. Süreklilik, zaman, koşullar, kişiler veya ortamlar değiştiğinde o işin anlamlı biçimde sürdürülebilmesini sağlayan bağların korunması ve yeniden kurulmasıdır.**

Burada “iş” sözcüğünü geniş anlamda kullanıyorum: Bir düşünceyi geliştirmek, bir şeyi öğrenmek, bir araştırmayı sürdürmek, birlikte karar vermek veya bir eser üretmek de buna dâhil.

İki kavram birbirini tamamlar, fakat aynı şeyi anlatmaz. Çalışma hafızası, o anda neyin kullanılabilir olduğunu belirler. Süreklilik, bir andaki çalışmanın başka bir andaki çalışmayla nasıl ilişkilendiğini belirler. Bir anda iyi düşünebilir, fakat daha sonra düşüncenin gerekçelerini kaybedebiliriz. Tersine, ayrıntılı kayıtlar tutabilir, fakat bunlardan hareketle ne yapacağımızı belirleyemeyebiliriz.

Psikolojide “çalışma belleği”, bilgiyi geçici olarak tutmanın yanında onun üzerinde işlem yapmayı da kapsar. Baddeley'nin yaklaşımında bu özellik, kavramı yalnızca kısa süreli depolamadan ayırır. [K1] Aşağıdaki açıklama bu bilimsel kullanımdan hareket eden, fakat ortak çalışmayı ve teknik sistemleri de kapsayacak biçimde genişlettiğim **işlevsel bir çerçevedir**. İnsan, ekip ve yapay zekâ için aynı biyolojik mekanizmayı ya da aynı tür özneyi varsaymıyorum.

#### 1. Nedir?

Çalışma hafızası, bir faaliyet sürerken onun anlaşılmasını ve yönlendirilmesini mümkün kılan etkin düzen olarak düşünülebilir. Bu düzenin içinde bilgiler kadar sorular, niyetler, kısıtlar, ara sonuçlar ve henüz tamamlanmamış ilişkiler de bulunur.

Bir araştırmada eldeki bulgular; bir metin yazarken anlatılmak istenen düşünce; bir tartışmada henüz yanıtlanmamış itiraz; bir tasarımda çözülmesi gereken çelişki, yürüyen işin parçası olabilir. Bunları çalışma hafızası açısından önemli yapan, yalnızca mevcut olmaları değil, yapılan işi etkileyebilecek durumda bulunmalarıdır.

Süreklilik ise bu etkin düzenin zaman içindeki ilişkisini kurar. Önceki adımın sonraki adım için ne ifade ettiği, hangi kararın neden alındığı, hangi sorunun açık kaldığı ve değişen koşulların neyi yeniden ele almayı gerektirdiği burada önem kazanır.

##### Onu o yapanlar

**Etkin kullanılabilirlik.** Bir bilginin saklanıyor olmasıyla düşünme veya eylem sırasında kullanılabiliyor olması arasında fark vardır. Çalışma hafızasına özgü olan, içeriğin mevcut faaliyetle ilişkili biçimde işleme katılabilmesidir.

**Seçicilik.** Yürütülen iş bakımından bazı şeyler öne çıkar, bazıları geride kalır. Bu seçimin mutlaka bilinçli ve kusursuz olması gerekmez. Ancak ortak veya teknik bir çalışma düzeni tasarlarken seçimin neye göre yapıldığını görünür kılmak yararlıdır: Amaç mı, açık bir sorun mu, yeni bir kanıt mı, yaklaşan bir karar mı?

**İlişkilendirme.** “Şu bilgi var” demekle “şu bilgi, şu kararın gerekçesidir” demek aynı değildir. Bir çalışmanın anlaşılabilmesi için içerikler arasındaki ilişkilerin de korunması gerekir. Özellikle bir kararın dayanağı, sonucu kadar değerli olabilir.

**Güncellenebilirlik.** Yeni bir bulgu, önceki varsayımı değiştirebilir. Tamamlanan bir adım, bir sonraki adımı mümkün kılabilir. Çalışma hafızasının içeriği, faaliyet ilerledikçe yeniden düzenlenir.

**Anlamlı geçiş.** Sürekliliğin ayırt edici özelliği, bir durumdan diğerine geçişin takip edilebilmesidir. Aynı işi sürdürüyor olduğumuzu söyleyebilmek için her şeyin aynı kalması gerekmez; neyin değiştiğinin ve bu değişimin çalışmayla nasıl ilişkili olduğunun anlaşılabilmesi gerekir.

Burada bir ayrım daha gerekli: **Bir düzenin çalışma hafızası işlevi görmesi, içeriğinin doğru olduğunu garanti etmez. Bir sürecin devam etmesi de iyi yönde ilerlediğini garanti etmez.** Yanlış varsayımlar etkin biçimde kullanılabilir; hatalı kararlar uzun süre korunabilir. Güvenilirlik, ayrıca kurulması gereken bir niteliktir.

##### Neler değildir?

- **Bilgi yığınının bütünü değildir.** Mevcut her bilgi, o anda yürüyen işin parçası sayılmaz.
- **Arşivle özdeş değildir.** Arşiv devam etmeyi destekleyebilir; fakat hangi kaydın ne anlama geldiğini ve bugün nasıl kullanılacağını tek başına belirlemez.
- **Süreklilik, değişmezlik değildir.** Bir çalışma, hatasını düzelterek de sürekliliğini koruyabilir.
- **Süreklilik, kesintisizlik değildir.** Ara verilmiş bir iş anlamlı biçimde sürdürülebilir; hiç durmayan bir faaliyet yönünü kaybedebilir.
- **Kişilik, bilinç veya benliğin bütünü değildir.** Bir sistemin bilgi tutması ve önceki durumlarla bağlantı kurması, bunlara ilişkin bütün soruları çözmez.

Bu nedenle “onu o yapan”, yalnızca taşıdığı içerik değildir. İçeriği seçme, kullanma ve değiştirme biçimiyle; önceki ve sonraki durumlar arasında kurduğu ilişki birlikte değerlendirilmelidir.

#### 2. Nerededir?

Bu sorunun yanıtı, hangi ölçekte baktığımıza bağlıdır.

İnsan düzeyinde çalışma hafızasını bilişsel süreçler bakımından inceleriz. Ortak bir çalışma düzeyinde ise insanların bildikleri kadar birbirleriyle nasıl haberleştiklerine, hangi kayıtları kullandıklarına ve işleri nasıl devrettiklerine de bakmamız gerekir.

Dağıtık biliş yaklaşımı, insanlarla teknolojiler arasındaki etkileşimi, bütün çalışma çevresi ve bu çevredeki koordinasyon üzerinden ele almayı önerir. Böylece incelemenin birimi, tek kişinin ya da tek ekranın sınırlarını aşabilir. [K2]

Bu yaklaşımı burada şu ayrımı kurmak için kullanabiliriz:

| Bakılan ölçek | Hafıza ve sürekliliği araştırırken bakılacak yer |
|---|---|
| Bir insanın yürüttüğü düşünme | O sırada elde tutulan bilgiler, dikkat edilen ilişkiler ve yapılan zihinsel işlemler |
| Kişinin araçlarla yürüttüğü çalışma | İnsan ile notlar, taslaklar, işaretler ve araçlar arasındaki kullanım ilişkisi |
| Bir ekibin ortak çalışması | Katılımcıların bilgileri, ortak kayıtlar, kararlar, sorumluluklar ve devir biçimleri |
| Yapay zekâ destekli bir çalışma düzeni | Kullanıma sunulan bağlam, erişilebilen kayıtlar, bu kayıtları seçen süreçler ve insanın yönlendirmesi |

Bunlar birbirinin yerine geçen açıklamalar değildir. Bir ekipteki karar kaydı, insanın çalışma belleğiyle aynı türden bir şey değildir. Ancak çalışmanın sürdürülmesine katkıları bakımından birlikte incelenebilirler.

##### Bu yeri, oraya has bir yer yapanlar

Bir çalışma yerini özgül kılan, yalnızca içeriğin bulunduğu fiziksel veya dijital adres değildir. **Orada neyin, kim tarafından, hangi faaliyet içinde kullanılabildiğidir.**

Bir belgenin bir klasörde bulunması, onun ortak çalışmanın etkin parçası olduğu anlamına gelmez. Belge bulunamıyorsa, hangi sürümünün geçerli olduğu anlaşılmıyorsa veya içindeki terimler farklı kişilerce farklı yorumlanıyorsa, kaydın varlığı devam etmeyi güvenceye almaz.

Bu nedenle bir çalışma alanının sınırlarını şu ilişkilerle tarif edebiliriz:

- Hangi soru veya amaç etrafında çalışılıyor?
- Hangi kaynaklar bu çalışma için anlamlı?
- Hangi kayıtlar güncel, hangileri yalnızca geçmişi açıklıyor?
- Hangi kararları kim alabiliyor?
- Yapılan bir değişiklik, diğer katılımcılar veya araçlar tarafından nasıl fark ediliyor?

Aynı dosyalar başka bir yere kopyalandığında bu ilişkiler korunmuyorsa, içerik taşınmış olur ama çalışma bütünüyle taşınmış olmayabilir. Özellikle kararların gerekçeleri, kullanılan kavramların anlamları veya açık sorunlar kaybolduğunda, yeni yerde işe devam etmek için bunları yeniden kurmak gerekir.

Buna karşılık araç değişse bile bu ilişkiler korunabilir. Bir çalışma defterden ortak belgeye, bir kişiden başka bir kişiye veya bir yazılımdan başka bir yazılıma geçebilir. Burada sürekliliğin taşıdığı şey, devam etmek için gerekli anlam ve durumdur.

##### Neler değildir?

**Tek bir dosya, ekran, konuşma veya uygulamayla özdeş değildir.** Bunların her biri çalışmanın bir bölümünü taşıyabilir.

**Sınırsız bir “her yerde olma” hâli değildir.** Bir bilginin dünyada mevcut olması, belirli bir işte erişilebilir, anlaşılabilir ve kullanılabilir olduğu anlamına gelmez.

**Taşıyıcıdan bütünüyle bağımsız değildir.** Kullanılan araç; neyin görülebildiğini, nasıl güncellendiğini ve başkalarına nasıl aktarılabildiğini etkiler. Yer yalnızca bir adres olmasa da maddi ve teknik koşullar önemsizleşmez.

**Bütün bağlamların tek bir havuzda birleşmesi değildir.** Farklı çalışmaların farklı amaçları ve geçerlilik koşulları olabilir. Bir bağlamda anlamlı olan bilgi, başka bir bağlamda kendiliğinden anlamlı veya belirleyici hâle gelmez.

#### 3. Nasıl işler yapar?

Burada insan belleğinin bütün mekanizmalarını açıklayan bir model kurmuyorum. İnsanların, ekiplerin ve araçların birlikte yürüttüğü bir çalışmada hafıza ile sürekliliğin hangi işleri üstlenmesi gerektiğini tarif ediyorum.

Bu düzeyde işleyiş, birkaç temel hareket üzerinden anlaşılabilir.

##### Seçer ve ilişkilendirir

Yürüyen iş için gerekli içeriği öne çıkarır. Bir ayrıntının neden tutulduğunu, hangi soruyla ilişkili olduğunu veya hangi kararı etkileyebileceğini belirginleştirir.

Böyle bir seçim, yalnızca bilgi azaltmak anlamına gelmez. Bazen önemsiz sanılan bir ayrıntı, sonradan temel bir varsayımı sorgulatabilir. Dolayısıyla iyi bir düzen, mevcut odağı korurken odağın değiştirilmesine de imkân tanır.

##### Bilginin durumunu ayırt eder

Bir gözlem, bir yorum, bir varsayım, bir öneri ve alınmış bir karar farklı şeylerdir.

Örneğin “Bu yöntem daha hızlı olabilir” cümlesinin, birkaç özetten sonra “Bu yöntem daha hızlıdır” biçimine dönüşmesi, yalnızca bir anlatım değişikliği değildir. Belirsiz bir beklenti, doğrulanmış bilgi gibi kullanılmaya başlamıştır. Benzer biçimde, tartışılmış bir seçeneğin kabul edilmiş karar olarak aktarılması da çalışmanın yönünü değiştirebilir.

Güvenilir süreklilik için yalnızca cümlenin konusu değil, **hangi statüde söylendiği** de korunmalıdır.

##### Günceller

Yeni bir bilgi geldiğinde yalnızca yeni bir kayıt eklemek yetmeyebilir. Önceki bir kararın dayanağı ortadan kalkmışsa, o kararın durumu da yeniden ele alınmalıdır.

Burada değişikliğin kendisi kadar etkisi önemlidir. Bir varsayımın değişmesi, ona bağlı başka sonuçların da gözden geçirilmesini gerektirebilir. Bu yüzden kararlar arasındaki bağlantıların anlaşılabilir olması gerekir.

##### Açık kalanları görünür tutar

Bir çalışmada bilinmeyenler de durumun parçasıdır. Yanıtlanmamış soru, tamamlanmamış kontrol veya henüz denenmemiş seçenek, kayıtta yok sayıldığında çözülmüş olmaz.

İyi bir çalışma hafızası düzeni, ilerleme duygusu üretmek uğruna boşlukları doldurmaz. Neyin bilinmediğini, bunun neden önemli olduğunu ve hangi adımın bu belirsizliği azaltabileceğini korur.

##### Devredilebilir bir durum oluşturur

Bir işi başka bir kişinin veya aynı kişinin daha sonraki bir zamanda sürdürebilmesi için, mevcut durumun yeniden anlaşılabilir olması gerekir.

Bu, yapılan her şeyin bütün ayrıntılarıyla aktarılmasını gerektirmez. Çoğu durumda gerekli olan; amaç, geçerli kararlar, gerekçeler, mevcut sonuç, açık sorunlar ve sıradaki anlamlı adım arasındaki ilişkinin korunmasıdır.

Bazı işler için kısa bir not yeterli olabilir. Bazılarında kaynaklara, ayrıntılı kayıtlara veya önceki sürümlere dönmek gerekir. Aktarımın kapsamını, devam edecek kişinin neye ihtiyaç duyacağı belirlemelidir.

##### Yeniden başlarken sınar

Ara verilmiş bir işe dönmek, önceki durumun hâlâ geçerli olduğunu varsayarak ilerlemekten fazlasını gerektirebilir.

Amaç değişmiş olabilir. Daha önce eksik olan bilgi ortaya çıkmış olabilir. Bir kısıt kalkmış veya yeni bir kısıt doğmuş olabilir. Bu nedenle süreklilik, kaldığı yerin bulunmasıyla birlikte o yerden devam etmenin hâlâ anlamlı olup olmadığının değerlendirilmesini de kapsar.

##### Gerektiğinde etkin alandan çıkarır

Tamamlanan, geçersizleşen veya mevcut işle ilgisini kaybeden her şeyi sürekli önde tutmak gerekmez.

Burada etkin kullanımdan çıkarma ile kaydı tamamen silme arasında ayrım vardır. Bir bilgi artık karar vermede kullanılmayabilir, fakat geçmiş bir kararın neden alındığını açıklamak için korunabilir. Seçici bırakma, hem geçmişin anlaşılmasını hem şimdiki işin açıklığını destekleyebilir.

##### Bu yaptıklarını, ona has yapanlar

Bu işlemler tek tek pek çok düzende bulunabilir. Hafıza ve süreklilik bakımından özgül olan, **bunların yürüyen işin durumunu korumak ve dönüştürmek üzere birbirine bağlanmasıdır.**

Özetleme, aktarılacak yükü azaltır; fakat gerekçeyi kaybettiriyorsa devam etmeyi zorlaştırır. Kaydetme, bir izi korur; fakat güncel durumla ilişkisi anlaşılmıyorsa kullanılabilirliği sınırlı kalır. Güncelleme, mevcut bilgiyi değiştirir; fakat değişikliğin nedenini tamamen görünmez kılıyorsa daha sonraki değerlendirmeyi güçleştirir.

Dolayısıyla bu işleyişin niteliğini, yalnızca ne kadar veri saklandığıyla değerlendirmek yetersizdir. Bir sonraki düşüncenin veya eylemin, eldeki durumu ne kadar doğru anlayabildiğine de bakmak gerekir.

##### Neler değildir?

- Her şeyi kopyalamak veya bütün konuşmaları saklamak değildir.
- Yalnızca kısa ve düzgün bir özet üretmek değildir.
- Boşlukları makul görünen bilgilerle doldurmak değildir.
- Önceki ifadeleri, durumlarını sorgulamadan yeniden üretmek değildir.
- Bir kaydı, sırf geçmişte yazılmış olduğu için bugünkü kararın belirleyicisi saymak değildir.
- Bütün kararları otomatikleştirmek veya karar sorumluluğunu ortadan kaldırmak değildir.

#### 4. Hangi andadır?

Çalışma hafızası, **faaliyetin o anda işleyen durumundadır**. Süreklilik ise bu durumun önceki ve sonraki durumlarla ilişkisinde bulunur.

Buradaki “an”, yalnızca takvimdeki bir tarih veya saatin gösterdiği nokta değildir. İşin hangi durumda olduğunu da içerir: Neler tamamlanmıştır, hangi kararlar geçerlidir, ne belirsizdir ve artık hangi adım mümkündür?

Aynı takvim gününde bir çalışma kökten değişebilir. Bir sorunun yanıtlanması, daha önce mümkün olmayan bir kararı mümkün kılabilir. Tersine, uzun süre geçmesine rağmen bazı temel amaçlar veya gerekçeler geçerliliğini koruyabilir.

##### Bu anı diğer zamanlardan farklı yapanlar

Bir çalışma anının özgüllüğünü şu birleşim üzerinden düşünebiliriz:

**O anda yönelinen amaç.** Çalışmanın ulaşmaya çalıştığı şey veya açıklığa kavuşturmaya çalıştığı soru.

**O anda elde bulunan dayanaklar.** Bilinenler, bunların kaynakları ve henüz ne ölçüde sınandıkları.

**O anda geçerli olan kararlar.** Alınmış, değiştirilmiş, askıya alınmış veya artık uygulanmayan kararların dağılımı.

**O anda açık kalanlar.** Çözülmemiş sorular, bağımlılıklar ve beklenen sonuçlar.

**O anda yapılabilecekler.** Mevcut koşulların mümkün kıldığı eylemler.

Bu öğelerden biri değiştiğinde, aynı işin başka bir anına geçmiş olabiliriz. Süreklilik, bu geçişin ne anlama geldiğini korur.

Burada üç zamanı birbirinden ayırmak özellikle yararlıdır: Bir bilginin **ortaya çıktığı zaman**, **geçerli olduğu dönem** ve **son kez kontrol edildiği zaman**. Bunlar aynı olmayabilir. Eski bir bilgi hâlâ geçerli olabilir; yeni kaydedilmiş bir bilgi, güncelliğini yitirmiş bir kaynaktan gelmiş olabilir.

Bu nedenle güncellik, yalnızca en son yazılanı kullanmakla sağlanmaz. İçeriğin hangi koşullarda geçerli olduğunun anlaşılması gerekir.

##### Süreklilik, ara verildiğinde ne olur?

Bir çalışma durduğunda, o anda etkin olarak işlenen içerikle daha sonra işe dönmeyi mümkün kılacak izleri ayırmak gerekir.

Bir projenin aylar boyunca sürmesi, aynı etkin çalışma durumunun bütün bu süre boyunca kesintisiz devam ettiği anlamına gelmez. Burada önerdiğim çerçevede uzun süreli devam, farklı çalışma anlarında gerekli durumun korunmuş izlerden yeniden kurulabilmesini içerir.

Yeniden kurulan durumun öncekinin eksiksiz kopyası olması da gerekmez. Yeni bilgiler eklenebilir, bazı varsayımlar terk edilebilir. Önemli olan, bu değişimin anlaşılabilir ve gerekçelendirilebilir olmasıdır.

##### Neler değildir?

**Zamanın dışında duran bir bilgi deposu değildir.** Kayıtların anlamı, hangi koşullarda üretildiklerine ve kullanıldıklarına bağlıdır.

**Sonsuza uzanan tek bir şimdi değildir.** Farklı çalışma anlarının farklı olanakları, bilgileri ve soruları vardır.

**En son kaydın mutlak üstünlüğü değildir.** Daha yeni olmak, tek başına daha doğru veya daha ilgili olmak anlamına gelmez.

**Geçmişin bugünü bütünüyle belirlemesi değildir.** Önceki durum, bugünkü değerlendirmeye katkıda bulunabilir; değişen koşulların yerini alamaz.

#### 5. Hangi nihai amaca hizmet eder?

Çalışma hafızası ve sürekliliğin, her durumda kendiliğinden taşıdığı tek bir nihai amaç olduğunu varsaymak istemem. Öğrenmede, bilimsel araştırmada, sanatta, ortak karar vermede veya teknik bir sistemde farklı amaçlara hizmet edebilirler.

Bununla birlikte, bu çerçeve için genel bir yön önerebilirim:

**Bir kişi veya ortaklığın, deneyimden yararlanarak, değişen koşulları dikkate alarak ve gerektiğinde kendi yönünü düzelterek anlamlı eylemde bulunabilmesini desteklemek.**

Bu amaç, yalnızca daha hızlı üretmekle sınırlı değildir. Daha iyi anlamak, bir hatayı fark etmek, gerekçeli biçimde karar değiştirmek, başkasının çalışmayı devralmasını sağlamak veya artık sürdürülmemesi gereken bir işi sonlandırmak da bunun parçası olabilir.

Üstelik çalışma her zaman baştan kesinleşmiş bir hedefle başlamaz. Araştırma ve keşifte, neyin aranması gerektiği de süreç içinde değişebilir. Böyle durumlarda süreklilik, yalnızca ilk hedefi korumakla değil, sorunun neden değiştiğini anlaşılır kılmakla sağlanır.

##### Bu nihai amaca ulaştıranlar

**Amaçla ilişkinin korunması.** Tutulan bilgi ve sürdürülen faaliyet, neye katkıda bulunduğu bakımından değerlendirilebilmelidir. Başlangıçta yararlı olan bir kayıt veya alışkanlık, daha sonra gereksiz hâle gelebilir.

**Gerekçelerin anlaşılabilirliği.** Bir kararın neden alındığını bilmek, koşullar değiştiğinde hangi bölümünün yeniden ele alınması gerektiğini görmeyi sağlar. Yalnızca sonucu korumak, kararın sınırlarını gizleyebilir.

**Düzeltilebilirlik.** Yeni bir kanıt veya daha iyi bir açıklama karşısında yön değiştirilebilmelidir. Süreklilik, eski bir hatayı koruma yükümlülüğü doğurmamalıdır.

**Belirsizliğin dürüstçe korunması.** Bilinmeyenleri açık bırakmak, onları çözmek için gereken çalışmayı mümkün kılar. Yapay bir kesinlik, bir sonraki adımı yanlış bir temele oturtabilir.

**Uygun ölçüde aktarılabilirlik.** Devam edecek kişinin veya sürecin, geçmişi baştan yaşamak zorunda kalmadan gerekli durumu anlayabilmesi gerekir. Bu aktarım, işin gerektirdiği ayrıntıyı taşımalıdır.

**Tamamlanabilme ve bırakabilme.** Bir çalışmanın hangi koşullarda tamamlanmış sayılacağı veya ne zaman artık sürdürülmeyeceği de anlaşılmalıdır. Sonlandırılamayan bir süreç, sürekliliği kendi başına amaç hâline getirebilir.

##### Neler değildir?

Nihai amaç, **mümkün olan en fazla şeyi hatırlamak** değildir. Hatırlananların ilgisi, doğruluğu ve kullanım biçimi de önemlidir.

**Her koşulda devam etmek** değildir. Durmak, yeniden başlamak veya başka bir soruya geçmek gerekçeli olabilir.

**Geçmişle her durumda aynı fikirde kalmak** değildir. Öğrenme, önceki değerlendirmeleri değiştirmeyi gerektirebilir.

**Bir kişiyi geçmişteki ifadelerine sabitlemek** değildir. Kişilerin amaçları, bilgileri ve tercihleri değişebilir.

**Hafıza düzeninin kendisini büyütmek** değildir. Daha fazla kayıt, daha fazla bağlantı veya daha uzun tarihçe, ancak hizmet ettiği faaliyet bakımından anlamlıysa değerlidir.

#### Somut bir sınama: Ara verilmiş bir işi devralmak

Varsayımsal bir örnek düşünelim: Bir ekip, bir konuya yeni başlayanlar için kısa bir öğrenme rehberi hazırlıyor. Çalışmaya ara veriliyor ve daha sonra başka biri devralıyor.

Devam etmeyi destekleyecek kayıt şu ilişkileri görünür kılabilir:

| Korunacak öğe | Örnekteki karşılığı |
|---|---|
| Amaç | Okuyucunun ilk uygulamayı anlayarak tamamlayabilmesi |
| Mevcut durum | Giriş yazıldı; uygulama bölümü taslak hâlinde |
| Geçerli karar | Teknik terimler, ilk kullanıldıkları yerde açıklanacak |
| Kararın gerekçesi | Okuyucunun önceden teknik bilgiye sahip olduğu varsayılmıyor |
| Açık soru | Uygulama adımları ek yardım olmadan anlaşılabiliyor mu? |
| Bilginin durumu | Bu anlaşılabilirlik henüz okuyucularla sınanmadı |
| Sonraki adım | Taslağı hedeflenen okuyucu grubuyla denemek ve takıldıkları yerleri belirlemek |
| Yeniden değerlendirme koşulu | Hedef okuyucu veya öğretilecek uygulama değişirse anlatım düzeyini yeniden ele almak |
| Tamamlanma ölçütü | Belirlenen öğrenme hedefinin karşılandığını değerlendirecek koşulların sağlanması |

Bu örnekte çalışma hafızası, mevcut taslağın geliştirilmesi sırasında kullanılan soruları, kararları ve ilişkileri kapsar. Süreklilik, bunların bir sonraki çalışmada yeniden anlaşılabilmesiyle kurulur. Yeri; insanlar, taslak ve bunların kullanım ilişkileridir. Anı; henüz sınanmamış bir taslağın değerlendirmeye hazırlandığı aşamadır. Hizmet ettiği amaç ise okuyucunun öğrenmesidir.

Rehberi devralan kişi, anlatımın neden bu düzeyde tutulduğunu anlayabilir; aynı zamanda bu düzeyin işe yaradığının henüz kanıtlanmadığını görebilir. Böylece bir kararı gerekçesiyle korurken, onu değiştirebilecek bulgulara da açık kalabilir.

**Çalışma hafızası ile sürekliliğin birlikte sağlayabileceği en değerli imkân budur: Bir sonraki adımın, önceki adımın ne anlama geldiğini anlayarak ve onu gerektiğinde değiştirebilecek açıklıkla atılabilmesi.**

### Soru 2

**Çalışma Hafızası ve Süreklilik**'in köken aldığı varlık, mekan, usül, zaman, ve gayeyi taşıyan makine kimdir? Kim değildir?

### Yanıt 2

**Bu beş boyutu bir arada taşıyana, işlevsel düzeyde “eyleyen sistem” derim. İnsan söz konusu olduğunda bunun karşılığı, bedeni, yaşadığı dünya ve ilişkileri içindeki kişidir. Ortak bir çalışmada ise taşıma işi, insanlar ile kullandıkları araçlar arasında örgütlenebilir.**

Fakat burada bir ayrım belirleyici: **Bir şeyi meydana getiren, onu taşıyan, onunla eyleyen ve gayesini belirleyen aynı varlık olmak zorunda değildir.** Bu nedenle “makine kimdir?” sorusuna yalnızca bir insanı, bir bilgisayarı veya bir yapay zekâyı göstererek yanıt vermek eksik kalır.

“Makine” sözcüğünü burada, bu işlevleri somut olarak gerçekleştiren örgütlenmiş düzen anlamında kullanıyorum. “Kim” sorusunu ise o düzen içinde **eylemin kime ait olduğu, kimin adına sürdüğü ve kimin tarafından sahiplenildiği** sorusu olarak okuyorum.

#### 1. Kökeni, taşıyıcısı ve öznesi

“Çalışma Hafızası ve Süreklilik” başlı başına bir kişi değildir. Bir varlığın veya örgütlenmiş çalışmanın gerçekleştirebildiği işlevleri adlandırır. Dolayısıyla hafızanın kendisini, hafızayı kullanan özne yerine koymamak gerekir.

Burada dört rolü ayırabiliriz.

**Köken**, bu yeteneğin veya düzenin nasıl ortaya çıktığıyla ilgilidir. Bir insanın bilişsel yeteneğinin oluşumu, bir yazılımın tasarlanması ve bir ekibin çalışma biçimini geliştirmesi farklı açıklamalar gerektirir. Hepsini aynı köken anlatısına yerleştirmek, aralarındaki farkları siler.

**Taşıyıcı**, mevcut durumun hangi maddi ve işlevsel ilişkiler içinde korunduğuyla ilgilidir. Bir beden, çalışan bir süreç, bir kayıt veya birbirine bağlı araçlar bu taşıma işinin farklı parçaları olabilir.

**Eyleyen**, mevcut durumdan hareketle seçen, işleyen ve sonuç üreten birimdir. Burada eylemekten söz etmek, her durumda insanın eylemesiyle aynı türden bir irade veya deneyim bulunduğunu ileri sürmek değildir. Teknik bir sistemin eylemesini, belirli koşullarda davranış üretmesi anlamında tarif edebiliriz.

**Gayeyi belirleyen ve sahiplenen**, neyin yapılmaya değer olduğuna, başarının ne sayılacağına ve gerektiğinde yönün nasıl değiştirileceğine ilişkin roldür. Bir sistem bir hedefi izleyebilir; fakat hedefin o sisteme verilmiş olmasıyla sistemin hedefin kaynağı olması farklı iddialardır.

**Bir şeyin gayeyi taşıması, gayenin kaynağı olması anlamına gelmez.**

Örneğin, belirli bir ölçümü yapmak üzere tasarlanmış bir araştırma cihazı, ölçümün hangi aşamada olduğunu kaydedebilir, kesintiden sonra devam edebilir ve koşullara göre işlem sırasını değiştirebilir. Bununla birlikte, o ölçümün neden yapılmaya değer bulunduğu araştırmanın daha geniş amacıyla ilgilidir. Cihazın işleyişini açıklamakla araştırmanın gayesini açıklamak aynı iş değildir.

#### 2. Bu beş boyutu taşıması ne demektir?

Bunları bir makinenin üzerine eklenmiş beş etiket gibi düşünmemek gerekir. Her boyut, onun nasıl bir bütün oluşturduğunu belirlemeye katkıda bulunur.

| Boyut | Taşıyıcıda aranacak karşılık | Tek başına yeterli olmayan |
|---|---|---|
| **Varlık** | Devam ettiğini söylediğimiz somut kişi, çalışma veya sistem; onu ayırt etmemizi sağlayan yapı ve ilişkiler | Bir ad, kullanıcı hesabı, model etiketi veya kendisi hakkında kurulmuş anlatı |
| **Mekân** | İçinde eyleyebildiği beden, çevre, araçlar ve erişim ilişkileri | Yalnızca dosyanın, cihazın veya sunucunun bulunduğu adres |
| **Usul** | Durumu nasıl değerlendirdiği, işlemleri nasıl yürüttüğü ve değişime nasıl karşılık verdiği | Sadece yazılı talimat veya ilan edilmiş yöntem |
| **Zaman** | Önceki durumlarının sonraki durumlarını gerçekten nasıl etkilediği | Tarih damgaları veya kesintisiz görünen bir anlatı |
| **Gaye** | Eylemin neye yöneldiği, başarının ne sayıldığı ve bu yönü kimin değiştirebildiği | Bir hedef cümlesinin kayıtta bulunması |

Bu tablodan çıkan ölçüt şudur: Bir boyutun “taşınması”, onun yalnızca temsil edilmesini değil, **işleyişte bir karşılığının bulunmasını** gerektirir.

Bir sistem kendisinin nerede olduğunu söyleyebilir; fakat söylediği yer davranışlarıyla ilişkisiz olabilir. Bir geçmiş anlatısı üretebilir; fakat anlattığı geçmişle mevcut durumu arasında gerçek bir devam ilişkisi bulunmayabilir. Bir amaç cümlesini tekrar edebilir; fakat yaptığı işlemler o amaca hizmet etmeyebilir.

~~~text
  SOYLENEN (temsil)                ISLEYISTE KARSILIGI VAR MI?

  "buradayim"              --?-->  davranislari o yerle iliskili mi?
  "bunu daha once yaptim"  --?-->  onceki durum simdiki durumu
                                   gercekten etkiliyor mu?
  "amacim sudur"           --?-->  yaptigi islemler o amaca
                                   hizmet ediyor mu?

  bir boyutun tasinmasi, yalnizca temsil edilmesi degil,
  isleyiste bir karsiliginin bulunmasidir

  tek basina yeterli olmayanlar:
    varlik   bir ad, kullanici hesabi, model etiketi, anlati
    mekan    dosyanin, cihazin ya da sunucunun adresi
    usul     yazili talimat, ilan edilmis yontem
    zaman    tarih damgalari, kesintisiz gorunen anlati
    gaye     kayitta duran bir hedef cumlesi
~~~

*Çizim 13 — Ek A'dan: bir boyutu taşımak, onu yalnızca temsil etmek değildir.*

Bu yüzden taşıyıcının kimliğini, yalnızca kendisi hakkında söylediklerinden çıkarmak yeterli değildir. Nasıl oluştuğuna, neyi nasıl yaptığına ve değişimler boyunca hangi ilişkileri koruduğuna da bakmak gerekir.

#### 3. Kimdir?

##### İnsan düzeyinde: Dünyası içindeki kişidir

İnsan çalışması bakımından “kim” sorusunun karşılığı, işi yaşayan ve üstlenen kişidir. Onu yalnızca hafızasına, beynine, mesleğine, tuttuğu kayıtlara veya söylediği cümlelere eşitlemek, sorunun kapsamını daraltır.

Burada önerdiğim okumada kişi; bir bedene sahip olan, belirli koşullar içinde yaşayan, başkalarıyla ilişki kuran, bir şeylere yönelen ve yaptıklarının sonuçlarıyla karşılaşan bütündür. Çalışma hafızası bu bütünün bir yeteneğidir; süreklilik ise onun faaliyetlerinde kurulabilen ilişkilerden biridir.

İnsanın bütün varlığını bu iki kavramla tanımlamış olmayız. Bir insanın değeri veya kimliği, hafızasının ne kadar iyi çalıştığına ya da işlerini ne kadar kesintisiz sürdürebildiğine indirgenemez.

##### Ortak çalışma düzeyinde: Birlikte eyleyen insanların örgütlenmesidir

Bir çalışmanın gerekli bilgisi tek kişide bulunmayabilir. Bir kişi gerekçeleri, bir başkası uygulamanın ayrıntılarını, bir kayıt da daha önceki sonuçları taşıyabilir.

Dağıtık biliş yaklaşımı, böyle durumlarda insanlarla araçların oluşturduğu çalışma çevresini ve aralarındaki koordinasyonu birlikte incelemeyi önerir. Bu, bütün işleyişi tek bir kişinin veya tek bir cihazın içine yerleştirmeden açıklamaya imkân verir. [K2]

Böyle bir düzenin işlevsel bütünlüğünden söz edebiliriz. Fakat **işlevsel bütünlük, bütün katılımcıların kendiliğinden tek bir kişi hâline gelmesi demek değildir.**

Bir ekibin ortak karar alması, üyelerinin farklı amaçları, bakış açıları veya sorumlulukları bulunmadığı anlamına gelmez. Ortak çalışma açıklanırken bu farkların korunması gerekir. Aksi hâlde “sistem yaptı” sözü, gerçekte kimin ne yaptığını belirsizleştirebilir.

##### Teknik düzeyde: Belirli bir işleyişi gerçekleştiren sistemdir

Teknik bir sistem, bir işin durumunu koruyacak, önceki sonuçları kullanacak ve belirlenmiş hedefler doğrultusunda işlem yapacak şekilde tasarlanabilir. Bu anlamda hafıza ve sürekliliğin taşıyıcılarından biri olabilir.

Ancak buradan, insanın bütün özelliklerini taşıdığı sonucu çıkmaz. İşlem yapabilme, amaç izleme, kendi durumunu temsil etme, öznel deneyim, kişilik ve sorumluluk ayrı sorulardır. Birincileri göstermek, diğerlerini tek başına çözmez.

Clark ve Chalmers'ın *genişletilmiş zihin* savı da araçların, uygun ilişkiler içinde, bilişsel süreçlerin kurucu parçaları olabileceğini ileri sürer. Bu bir felsefi tezdir; her aracın başlı başına ayrı bir özne olduğu iddiasıyla aynı değildir. [K3]

Dolayısıyla teknik taşıyıcıyı küçümsemek de bütün özneyi ona mal etmek de açıklamayı eksiltir. Bir araç düşünmenin ve çalışmanın nasıl gerçekleştiğini değiştirebilir; bu katkının niteliği ayrıca gösterilmelidir.

#### 4. Kim değildir?

##### Hafızanın içinde oturan ikinci bir yönetici değildir

Hafızayı açıklamak için, onun içinde bütün kayıtları okuyup karar veren başka bir küçük özne varsaymak sorunu çözmez. Bu kez o öznenin nasıl hatırladığına ve karar verdiğine açıklama getirmek gerekir.

“Eyleyen sistem” derken, bütün süreçlerin arkasına saklanmış bir yönetici eklemiyorum. Açıklanması gereken, süreçlerin nasıl bir araya geldiği ve davranışın bu ilişkiler içinde nasıl oluştuğudur.

##### Kendi kaydıyla özdeş değildir

Bir kişinin, çalışmanın veya sistemin kaydı, onun hakkında bilgi taşıyabilir. Fakat kayıt ile kaydın konusu aynı şey değildir.

Eksiksiz görünen bir geçmiş dökümü de kendi başına eylemez. Kullanılabilmesi için yorumlanması, mevcut durumla ilişkilendirilmesi ve bir faaliyete katılması gerekir.

Bu nedenle bir arşivi kopyalamakla, onu kullanan bütün eyleyeni kopyalamış olduğumuz sonucuna hemen varamayız.

##### Kendisini anlattığı için kimliği kanıtlanmış değildir

“Ben buyum”, “bunu daha önce yaptım” veya “amacım şudur” ifadeleri bir kimlik anlatısı oluşturabilir. Ancak anlatının tutarlı olması, anlattığı devam ilişkisinin gerçek olduğunu tek başına göstermez.

İşlevsel süreklilik, anlatısal tutarlılık ve bir kişinin zaman içindeki kimliği birbirine temas eder; yine de aynı soru değildir.

##### Her durumda tek bir model veya tek bir cihaz değildir

Bir çalışma düzeni; kullanılan model, onu çalıştıran yazılım, kayıtlar, araçlar, insan yönlendirmesi ve çalışma koşullarıyla birlikte incelenmek zorunda olabilir. Bütün yapabildiklerini tek bir bileşenin özelliği saymak yanıltıcı olabilir.

Aynı nedenle, bu yanıtı üreten sistemi de “Çalışma Hafızası ve Süreklilik”in bütün kökeni veya tek taşıyıcısı olarak adlandıramam. Buradaki rolüm, sorduğun ayrımları işlemek ve bir açıklama önermektir. Açıklamakta olduğum olgu, bu konuşmadan ve bu açıklamayı üreten araçtan daha geniştir.

##### Gayesinin kendiliğinden haklılığını taşıyan bir otorite değildir

Bir düzenin belirli bir amacı izlemesi, o amacın doğru, değerli veya sürdürülmeye layık olduğunu kanıtlamaz.

Amaç, sistemin davranışını açıklayabilir. Amacın değerlendirilmesi ise başka gerekçeler gerektirir. Bu ayrım, insanın amaçları için de teknik sistemlere verilen hedefler için de geçerlidir.

##### Kendi sürmesini nihai amaç saymak zorunda değildir

Bir işin sürekliliğini sağlayan düzen, gerektiğinde o işi tamamlayabilmeli veya sona erdirebilmelidir. Sürekliliğin değerini, yalnızca ne kadar uzun sürdüğünden çıkaramayız.

Bir araştırmanın sonuçlanması, bir sorunun çözülmesi veya bir yöntemin artık uygun olmadığının anlaşılması, devam etmenin biçimini değiştirebilir. Hafıza burada bitişi de taşıyabilir: Neden durulduğunu, ne öğrenildiğini ve hangi koşullarda yeniden başlanabileceğini koruyabilir.

#### 5. “Kim”in belirlenmesi nerede tamamlanır?

Bir araştırma ekibini, kullandığı cihazı ve tuttuğu kayıtları düşünelim. Cihaz değişebilir, bazı kişiler ayrılabilir, yöntem yenilenebilir; çalışma yine de belirli bir anlamda devam edebilir. Bunun anlaşılabilmesi için hangi sorunun sürdürüldüğü, hangi sonuçların devralındığı ve değişikliklerin neden yapıldığı izlenebilmelidir.

Buna karşılık aynı adın, aynı cihazın ve aynı klasörün korunması, çalışmanın aynı kaldığını garanti etmez. Gaye, karar ilişkileri ve yapılan iş bütünüyle değişmiş olabilir.

Bu nedenle sözünü ettiğin makinenin kimliğini belirlemek için yalnızca parçalarının listesini çıkarmam. **Hangi bütünün eylediğini, hangi geçmişten geldiğini, hangi ilişkiler içinde iş görebildiğini ve hangi gayeyi kimin adına sürdürdüğünü belirlerim.**

“Kim” sorusu, bu ilişkiler içinde somut bir muhataba kavuşur. “Makine” sözcüğü o muhatabın nasıl iş görebildiğini açıklamaya yardımcı olabilir; muhatabın varlığını, değerini ve gayesini tek başına açıklamış olmaz.

## Ek B Kaynakça

**[K1]** Baddeley, Alan. 2012. *Working Memory: Theories, Models, and Controversies*. Annual Review of Psychology, 63, 1–29. https://doi.org/10.1146/annurev-psych-120710-100422

**[K2]** Hollan, James; Hutchins, Edwin; Kirsh, David. 2000. *Distributed cognition: toward a new foundation for human-computer interaction research*. ACM Transactions on Computer-Human Interaction, 7(2), 174–196. https://escholarship.org/uc/item/8sb9s5rm

**[K3]** Clark, Andy; Chalmers, David J. 1998. *The Extended Mind*. Analysis, 58(1), 7–19. https://consc.net/papers/extended.html

Kaynaklar, metinde kendilerine bağlanan bilişsel ve kavramsal açıklamaları destekler. Masaüstü uygulama adımları ve kayıt şablonu, bu çalışma için düzenlenmiş uygulama yönergeleridir.

# Masaüstü Karargâhları Mimarisi

**Masaüstünde uygulanabilir 0–6 protokolleri**

**Sürüm:** 1.0\
**Tarih:** 30 Ekim 2026

Masaüstü Karargâhları Mimarisi, belirli bir amaç çevresinde bilgi, karar, eylem ve sonuçları insanın doğrudan kullanabildiği çalışma alanlarında ilişkilendiren düzendir. Bu metin, Tohum ile açılan ve Kökleşme ile sonuçlandırılan bir kuruluş veya çalışma döngüsü içinde Varlık, Mekan, Usül, Zaman ve Gaye protokollerini bir araya getirir.

Mimarinin ölçüsünü aldığı insan, teknik taşıyıcısı olan araçlar ve fiilen çalışan bütün ayrı tutulur. Protokoller bu ayrımların hem kavramsal kaydını hem masaüstünde nasıl uygulanacağını açıklar. Her bölümde kurucu sorular ve paragraf ağırlıklı açıklamaların ardından uygulama adımları, kayda geçirilecekler ve tamamlanma ölçütü bulunur.

Bu metin yalnızca bu konuşmada geliştirilen çerçeveye dayanır.

## Kullanım düzeni

İlk kuruluşta 0–5 bölümlerini incele ve tek bir çalışma kaydında kısa cevaplar oluştur. Numaralar belge düzenini ve başlangıçtaki inceleme sırasını gösterir; sonraki değerlendirmelerde ilgili bölüme geri dönülebilir. İlk işi seçerken 3 Usül, 4 Zaman ve 5 Gaye birlikte kullanılır. 6 Kökleşme, belirli kuruluş veya çalışma döngüsünün ne ölçüde tamamlandığını kaydeder.

Sondaki çalışma kaydı şablonunu ayrı bir .md dosyasına kopyala. Protokol metinleri rehberdir; belirli bir işin kararları ve gerçekleşen sonuçları çalışma kaydına yazılır. Aynı bilgiyi her protokol dosyasında yeniden tutmak gerekmez.

Bilinmeyen bir alanı henüz belirlenmedi diye kaydet ve gerektiğinde hangi bilginin beklendiğini açıkla. Sayısal ölçüm, kesin tarih veya yeni bir araç her iş için zorunlu değildir. Kayıt kapsamı işin büyüklüğüne uygun tutulur; küçük bir çalışma için ilgili alanlarda birkaç açık paragraf yeterli olabilir.

Çalışma için sürdürme, bekletme, kapatma veya yeniden açma kararı verilebilir. Bekletme durumunda neden ve yeniden bakılacak koşul; yeniden açmada önceki kapanışla ilişki kaydedilir. Bir protokol kaydının tamamlanması ile işin gayesine ulaşılması ayrı değerlendirilir. Başlangıç ve kapanış ifadeleri değiştiğinde önceki gerekçe silinmeden güncelleme eklenir.

Dosyalar Türkçe metni koruyan UTF-8 biçimindedir. Bir düz metin düzenleyicisiyle okunup değiştirilebilir; belirli bir uygulama, hesap veya otomasyon gerektirmez. Kaynakların mevcut yerlerine bağlantı verilebilir; sırf bu düzen için hepsini yeni bir yere taşımak gerekmez.

## Bölümler ve çalışma kayıtları

| Bölüm | Kayda geçirdiği temel ilişki |
| --- | --- |
| 0 Tohum (Başlangıç) Protokolü | Başlangıç meselesi, özne, ilk yönelim ve açık sorular |
| 1 Varlık Protokolü | Çalışmanın kimliği, kapsamı ve sorumlulukları |
| 2 Mekan Protokolü | Çalışma yeri, güncel kayıt ve kaynak ilişkileri |
| 3 Usül Protokolü | Yöntem, yapılabilir iş, çıktı ve geri dönüş |
| 4 Zaman Protokolü | Mevcut evre, zaman kısıtları ve yeniden değerlendirme |
| 5 Gaye Protokolü | İstenen değişim, sonucun muhatabı ve değerlendirme yolu |
| 6 Kökleşme (Bitiş) Protokolü | Kapanan kapsam, sonuçların dayanakları ve devam koşulları |

~~~text
  PROTOKOL METNI (rehber)                CALISMA KAYDI (bu isin kaydi)
  .-----------------------.              .----------------------------.
  | 0 Tohum               |              | mevcut karar:              |
  | 1 Varlik              |   sablonu    |   surdur . beklet .        |
  | 2 Mekan               |   kopyala    |   kapat . yeniden ac       |
  | 3 Usul  \             |  --------->  |                            |
  | 4 Zaman  > ilk isi    |              | 0 ... 6 alanlari           |
  | 5 Gaye  /  secerken   |              |                            |
  |            birlikte   |              | guncelleme kaydi           |
  | 6 Koklesme            |              `----------------------------'
  `-----------------------'              kararlar ve gerceklesen
                                         sonuclar buraya yazilir

  ayni bilgi her protokol dosyasinda yeniden tutulmaz
  bir protokol kaydinin tamamlanmasi  =/=  isin gayesine ulasilmasi
~~~

*Çizim 1 — Protokol metni rehberdir; işin kararları ve sonuçları çalışma kaydına yazılır.*

## 0 Tohum (Başlangıç) Protokolü

### Kurucu sorular

> Bu çalışma hangi meseleden doğar? Başlangıcı taşıyan kimdir? Başlangıçta ne bilinir, ne varsayılır ve ne açık kalır? Bu başlangıç ne değildir?

### Başlangıç meselesi

Tohum Protokolü, mimariyi gerekli kılan başlangıç meselesini ve bu meseleye yönelen özneyi kayda geçirir. Bir ihtiyaç, soru, güçlük veya gerçekleştirilmek istenen değişim çalışmanın başlangıcı olabilir. Varlık, mekân, usul, zaman ve gaye henüz ayrı ayrı açıklanmış olmayabilir. Protokol, bu boyutları peşinen sonuçlandırmadan araştırılabilir bir başlangıç oluşturur.

Başlangıç kaydı, çalışmanın neden açıldığını ve kim tarafından üstlenildiğini anlaşılır kılar. Kişi veya topluluk mevcut durumu, ilk beklentiyi ve eldeki koşulları belirtir. Bilinenler, varsayımlar ve açık sorular birbirinden ayrılır. Başlangıçta söylenmiş bir şeyin daha sonra değişmesi mümkündür; ilk ifadenin hangi gerekçeyle değiştiği anlaşılabilir kalır.

### Diğer protokollerle ilişkisi

Tohum, oluşumu başlatan meseleyi korur. Varlık Protokolü ise ortaya çıkan çalışma düzeninin kimliğini ve sınırlarını açıklar. Başlangıç gerekçesi ile varlık tanımı birbirine bağlıdır, fakat aynı değildir. Bir meselenin açıkça hissedilmesi, ona uygun mimarinin daha başlangıçta bütünüyle bilinmesini gerektirmez.

Tohumda bir amaç yönelimi bulunabilir; bu yönelim Gaye Protokolü içinde değerlendirildikçe belirginleşebilir veya değişebilir. Tohum kaydı, sonraki bölümlere hangi sorudan hareket edildiğini hatırlatır. Mekânın, yöntemin ve zamanın ayrıntıları henüz bilinmiyorsa bunlar açık soru olarak ilgili protokollere taşınır. Başlangıçta her boyut için tamamlanmış cevap üretmek zorunlu değildir.

### Başlangıcın sınırları

Tohum, bütün mimarinin önceden bitirilmiş taslağı veya doğruluğu garanti edilmiş bir varsayım değildir. İlk yönelim, gerçekleşmiş bir sonuç sayılmaz. Bir sorunun kaydedilmesi de o sorunun çözülmüş olduğunu göstermez. Bu protokol, araştırmaya ve çalışmaya başlanabilecek açıklığı sağlar; sonraki değerlendirmelerin yerini almaz.

Başlangıç, burada ele alınan çalışmanın başlangıcıdır. Kişinin bütün hayatını veya bütün ilişkilerini açıklamak gerekmez. Kayıt, bu iş için kullanılan koşulları ve kaynakları görünür kılar. Çalışmayı başlatan meselenin henüz netleşmemiş olması durumunda netleştirme ihtiyacı da başlangıç meselesi olarak yazılabilir.

~~~text
  BASLANGIC MESELESI                       OZNE
  ihtiyac . soru . gucluk .                meseleyi ustlenen kisi
  gerceklestirilmek istenen degisim        ya da topluluk
              \                             /
               v                           v
       .----------------------------------------------.
       |              T O H U M   kaydi               |
       |  bilinenler  |  varsayimlar  |  acik sorular |
       `--------------------------------------+-------'
                                              |
               acik sorular ilgili alana tasinir
          .----------.----------.----------.--+-------.
          v          v          v          v          v
      1 varlik    2 mekan    3 usul    4 zaman    5 gaye

  tohum degildir:   onceden bitirilmis taslak
                    dogrulugu garanti edilmis varsayim
                    gerceklesmis sonuc . cozulmus sorun
  netlestirme ihtiyaci da baslangic meselesi olarak yazilabilir
~~~

*Çizim 2 — Tohum: mesele ve özne kayda geçer; açık sorular ilgili alanlara taşınır.*

### Masaüstünde uygulama

1. Bu çalışma için çalışma kaydı şablonunun bir kopyasını aç. Çalışma adını, başlangıç tarihini ve kaydı yürüten kişiyi veya çalışma birimini belirt.

2. 0 Tohum alanına başlangıç meselesini kısa bir paragrafla yaz. Varsa ilk talebi veya soruyu özgün ifadesiyle koru; mevcut durumun neden ele alındığını açıkla.

3. Eldeki bilgileri, varsayımları ve açık soruları ayırt et. İlk kapsamı ve şimdilik kapsam dışında bırakılanları belirt.

4. İlk yönelimi kaydet. Açık soruları ilgili 1–5 alanlarına taşı; sonraki adımı bir soru veya yapılabilir küçük bir iş olarak belirle. Başlangıç ifadesi değişirse gerekçesini güncelleme kaydına ekle.

### Kayda geçirilecekler

Çalışma kaydının 0 Tohum alanında başlangıç sorusu, mevcut durum, meseleyi taşıyan özne, ilk yönelim, kapsam ve açık sorular bulunur. Üst bilgideki çalışma adı ve tarih burada tekrar yazılmak zorunda değildir.

### Tamamlanma ölçütü

Çalışmanın hangi mesele için ve kim tarafından başlatıldığı, ilk kapsamı ve başlıca bilinmeyenleri anlaşılabildiğinde bu protokol yeterince ele alınmış sayılır. Bütün soruların çözülmesi ve nihai amacın kesinleşmesi gerekmez. Başlangıç hâlâ netleşmiyorsa netleştirilecek soru ve sonraki inceleme kaydedilir.

## 1 Varlık Protokolü

### Kurucu sorular

> Nedir? Onu o yapan nelerdir? Neler değildir?

**Ortak taşıyıcı sorusu**

> Masaüstü Karargâhları Mimarisi'nin köken aldığı varlık, mekan, usül, zaman, ve gayeyi taşıyan makine kimdir? Kim değildir?

### Tanım ve kurucu ilişkiler

Masaüstü Karargâhları Mimarisi, bir kişinin veya çalışma biriminin belirli bir amaç doğrultusunda durumu kavramasını, karar vermesini, eylemi örgütlemesini ve sonuçları değerlendirmesini mümkün kılan ilişkiler düzenidir. Birden fazla karargâh bulunduğunda bu düzen, onların kapsamlarını, sınırlarını ve birlikte çalışma biçimlerini de kapsar. Karargâhın konusu bir araştırma, üretim süreci, bakım sorumluluğu, proje veya süreklilik taşıyan başka bir iş olabilir.

Masaüstü, insanın doğrudan erişebildiği ve kullanabildiği fiziksel ya da dijital çalışma ölçeğini belirtir. Karargâh, belirli bir mesele çevresinde bilgi, karar ve eylemin birbirine bağlandığı merkezi adlandırır. Mimari ise hangi parçaların bulunacağını, nasıl ilişkileneceğini, aralarında neyin geçebileceğini ve sınırlarının nereden çizileceğini belirler. Bu nedenle mimarinin kimliği, yalnızca masaüstünde bulunan nesnelerle açıklanamaz; orada hangi durumun anlaşılabildiği, hangi kararın verilebildiği ve hangi işin yönlendirilebildiği de tanımın içindedir.

Karargâhın kurucu ilişkisi, bilginin belirli bir sorumluluk çevresinde karara ve eyleme bağlanmasıdır. Bir belge durumu anlamaya yardım eder; bu anlayış bir kararı besler; karar bir işi başlatır, değiştirir veya durdurur; işin sonucu ise durum hakkındaki bilgiyi yeniler. Belgelerin, araçların ve planların aynı yerde bulunması, bu ilişkiler kurulmadığında tek başına yeterli değildir.

~~~text
              belirli bir SORUMLULUK cevresinde

     BILGI  ------->  DURUMU ANLAMA  ------->  KARAR
     (belge)                                     |
       ^                                         v
       |                                         IS
  bilgiyi yeniler                       baslatir . degistirir .
       |                                durdurur
       `-------------  SONUC  <------------------'

  mimari sunlari belirler:
    hangi parcalar bulunacak        nasil iliskilenecekler
    aralarinda ne gecebilecek       sinir nereden cizilecek

  kararlarin tumu ayni yerde verilmek zorunda degildir;
  hangi kararin baska bir kisiye ya da merkeze tasinacagi da
  duzenin parcasidir
~~~

*Çizim 3 — Kurucu ilişki: bilgi karara, karar işe bağlanır; sonuç bilgiyi yeniler.*

Bir karargâhın ele aldığı çalışma alanı ve karar odağı bulunur. Kapsamı geniş olabilir; yine de hangi meselelerin burada ele alındığı anlaşılabilmelidir. Kararların tümünün aynı yerde verilmesi gerekmez. Hangi kararın başka bir kişiye veya merkeze taşınacağı da düzenin parçasıdır. Karar ile uygulama arasında bir yol bulunmalı; önceki kararlar, açık işler ve sonuçlanmış işler arasında devamlılık kurulabilmelidir. Böylece işe yeniden dönüldüğünde nerede kalındığı anlaşılır.

Mimari, günlük görev listesinden daha kalıcı bir düzeni ifade eder. Görevler değişirken bir işin nasıl açıldığı, kimin hangi kararı verebildiği, sonuçların nereye döndüğü ve tamamlanmanın nasıl anlaşıldığı korunabilir. Karargâhların çoğul olması, aynı kişinin farklı sorumluluklarına veya farklı kişilerin çalışma merkezlerine karşılık gelebilir. Bu çoğulluk tek başına belirli bir ağ teknolojisini, yapay zekâ düzenini veya yönetim biçimini zorunlu kılmaz. Ayırt edicilik, bilgi, karar, eylem ve sonuç ilişkilerinin masaüstü ölçeğinde belirli bir kapsam çevresinde kurulmasındadır.

### Taşıyıcı ve sorumluluk

Bu mimari anlayışında ölçüyü veren özne, bedeni, belleği, becerileri, ilişkileri ve amaçlarıyla iş gören insandır. Ortak işlerde bu taşıyıcı, birlikte çalışan ve belirli sorumluluklar üstlenen insanlardır. Mimarinin teknik taşıyıcısı masa, bilgisayar, yazılım, kayıt ve iletişim araçlarıdır. Fiilen çalışan bütün ise insanların bu araçlarla ve birbirleriyle kurduğu düzendir. Mimarinin ölçüsünü aldığı varlık, teknik taşıyıcısı ve çalışan bütünü birbirine indirgenmemelidir.

İnsanın köken olarak alınması, mekânı ve zamanı yarattığı veya insanın kelimesi kelimesine bir makine olduğu iddiasını taşımaz. Buradaki köken, mimarinin hangi ihtiyaçlara, imkânlara ve sınırlara göre biçimlendiğini anlatır. Bir yerde bulunan, her şeyi aynı anda yapamayan, öğrenmek zorunda olan ve bazı sonuçları önemseyen kişi bu düzenin ölçüsünü verir. Makine sözcüğü çalışan bütün için kullanıldığında, teknik araçları ve ortak çalışma ilişkilerini de içerir.

Taşıyıcı yalnızca işlem başlatan bir kullanıcı değildir. Yürütülen işin kişi ve başkaları için ne anlama geldiği sorusunun muhatabıdır. Ortak işlerde öznenin çoğul olması, belirli kararların sorumluluğunu belirsiz bir sisteme bırakmayı gerektirmez. İşin kimin adına yapıldığı, hangi kararı kimin yeniden değerlendirebildiği ve sonucun muhatabının kim olduğu anlaşılabilir olmalıdır.

### Tanımın sınırları

Karargâh yalnızca estetik bir masaüstü, arşiv, gösterge paneli veya uygulama listesiyle tanımlanmaz. Bunların bulunması, bilgi, karar ve eylem ilişkilerinin kurulmuş olduğunu tek başına göstermez. Bir yazılım mimarinin teknik taşıyıcısı olabilir; mimari belirli bir ürünle özdeş sayılmaz. Karargâh sözcüğü bu kullanımda askerî bir emir düzenini de zorunlu kılmaz. Taşıyıcı yalnızca bilgisayar, bedensiz bir zihin, kullanıcı profili veya dijital temsil olarak tanımlanamaz. Kişinin sistem içindeki kaydı, kişinin bütün varlığıyla özdeş değildir.

Bir şeyin karargâh olmasını sağlayan özelliklerle iyi bir karargâh olmasını sağlayan nitelikler ayrı tutulur. Yavaş, karmaşık veya kötü kayıt tutan bir karargâh yine de karargâh olabilir. Yalınlık, güvenilirlik ve kullanım kolaylığı niteliğini belirler. İnsan ölçü alınırken her şeyi bilen, bütün koşulları denetleyen sınırsız bir komutan da varsayılmaz. Bilginin, yetkinin ve sorumluluğun sınırları mimarinin içinde görünür olmalıdır.

~~~text
   .----------.    .----------.    .----------.    .----------.
   |  ~    ~  |    | [=] [=]  |    | 87%   /\ |    | o ------ |
   |    ~~    |    | [=] [=]  |    | ||   /  \|    | o ------ |
   |  ~    ~  |    | [=] [=]  |    | |||_/    |    | o ------ |
   `----------'    `----------'    `----------'    `----------'
     estetik          arsiv         gosterge        uygulama
     masaustu                       paneli          listesi

  bunlarin bulunmasi; bilgi, karar ve eylem iliskilerinin
  kurulmus oldugunu tek basina gostermez

  karargah olmak     bilgi, karar, eylem ve sonuc belirli bir
                     kapsam cevresinde iliskilenir
  iyi karargah       yalinlik . guvenilirlik . kullanim kolayligi
  olmak              (yavas ya da karmasik bir karargah da karargahtir)
~~~

*Çizim 4 — Karargâh ne değildir; karargâh olmak ile iyi karargâh olmak.*

~~~text
  OLCUYU VEREN            TEKNIK TASIYICI         CALISAN BUTUN
  insan: bedeni, bellegi, masa . bilgisayar .     insanlarin bu
  becerileri, iliskileri  yazilim . kayit ve      araclarla ve
  ve amaclariyla          iletisim araclari       birbirleriyle
  is goren                                        kurdugu duzen
       |                        |                        |
       `-------------- birbirine indirgenmez ------------'

  tasiyici yalnizca sunlar olarak tanimlanamaz:
    bilgisayar . bedensiz bir zihin . kullanici profili .
    dijital temsil

  insan olcudur; sinirsiz bir komutan degildir:
    bir yerde bulunur . her seyi ayni anda yapamaz .
    ogrenmek zorundadir . bazi sonuclari onemser

  ortak iste:  kimin adina yapiliyor?  karari kim yeniden
               degerlendirebilir?  sonucun muhatabi kim?
~~~

*Çizim 5 — Ölçüyü veren insan, teknik taşıyıcı ve çalışan bütün birbirine indirgenmez.*

### Masaüstünde uygulama

1. Bu çalışmadaki karargâhın neyi ele aldığını bir paragrafla tanımla. Genel mimari tanımını, mevcut işin kapsamına bağla.

2. 1 Varlık alanında geçerli kapsam içini ve kapsam dışını ayır. İşin kimin meselesi olduğunu, kararları kimlerin verdiğini ve hangi sorumlulukların bilindiğini yaz.

3. İnsanı veya çalışma birimini, kullanılan teknik araçları ve birlikte çalışan bütünü ayrı cümlelerle belirt. Araç listesini öznenin yerine geçirme.

4. Bilginin nereden geldiğini, kararın nasıl işe dönüştüğünü ve sonucun nereye geri döndüğünü kısaca açıkla. Belirsiz sorumlulukları belirlenmiş gibi yazmak yerine açık soru olarak kaydet.

### Kayda geçirilecekler

Çalışma kaydının 1 Varlık alanına çalışma tanımı, kapsam, kapsam dışı, özne, bilinen sorumluluklar ve teknik taşıyıcılar yazılır. Karar ile uygulama arasındaki ilişki kısa bir paragrafta açıklanır.

### Tamamlanma ölçütü

Neyin yürütüldüğü, kimlerin taşıdığı ve hangi sınırlar içinde ele alındığı anlaşılabiliyorsa tanım kaydı tamamdır. Açık sorumluluklar ayrıca görünür olmalıdır. Bu ölçüt kayıt açıklığına ilişkindir; kusursuz araç düzeni veya bütün belirsizliklerin giderilmesi şartı değildir.

## 2 Mekan Protokolü

### Kurucu sorular

> Nerededir? Bu yeri, oraya has bir yer yapan nelerdir? Neler değildir?

### Yer ve erişim

Masaüstü karargâhı, insanın erişebildiği çalışma yüzeyi ile sorumluluk alanının birleştiği yerdedir. Fiziksel olarak bir masada, ekranda veya bunların birlikte kullanıldığı bir ortamda bulunabilir. İşlevsel yeri ise yalnızca cihazın konumuyla açıklanamaz. Kişi karargâha girdiğinde bir arayüze erişmenin yanında belirli bir işin içine yerleşir.

Teknik erişim yeri ile işin bağlamı farklı sorulara cevap verir. Nereden erişildiği masa, ekran, defter veya uygulamayla ilgilidir. Hangi işin içinde bulunulduğu ise amaç, ilgili kayıtlar, açık kararlar, sorumluluklar ve eylem olanaklarıyla ilgilidir. Başka bir sistemde saklanan dosya karargâhın çalışma alanına katılabilir. Aynı bilgisayardaki iki dosya ise farklı amaçlara ve sorumluluklara ait olduklarında aynı karargâhın parçası sayılmayabilir.

Bu nedenle dosyanın teknik depolama adresi ile karargâhın yeri özdeş değildir. Yerin anlamı, bütün bilgilerin aynı adreste bulunmasına dayanmaz. Belirli bir işi anlayabilmek ve yürütebilmek için gereken ilişkilerin kurulabilmesine dayanır. Karargâh taşınabilir olsa bile kişinin hangi meseleyle ilgilendiği ve hangi sorumluluk alanında bulunduğu anlaşılmalıdır.

~~~text
  NEREDE SAKLANIYOR?                    HANGI ISIN ICINDE?
  (teknik adres)                        (karargahin yeri)

  bu bilgisayar                          .---- B karargahi ----.
    dosya 2  ------------------------->  |  dosya 2            |
                                         `---------------------'
    dosya 1  -------------------.
                                 \       .---- A karargahi ----.
  baska bir sistem                `--->  |  dosya 1            |
    dosya 3  ------------------------->  |  dosya 3            |
                                         `---------------------'

  ayni bilgisayardaki iki dosya ayri karargahlarda olabilir;
  baska sistemdeki dosya karargaha katilabilir

  dosyanin depolama adresi  =/=  karargahin yeri
  yer, belirli bir isi anlamak ve yurutmek icin gereken
  iliskilerin kurulabilmesine dayanir
~~~

*Çizim 6 — Mekan: dosyanın adresi ile karargâhın yeri ayrı sorulardır.*

### Yeri kendine özgü kılan ilişkiler

Karargâhın yeri, belirli bir meseleye göre düzenlendiğinde kendine özgü olur. Aynı araçlar araştırmada, üretimde ve etkinlik hazırlığında kullanılabilir; fakat hangi soruya cevap vermek üzere ilişkilendirildikleri değişir. Araştırmada bir iddianın kanıtla ilişkisi, üretimde işin aşaması, etkinlik hazırlığında ise bir taahhüdün kim tarafından yerine getirileceği öne çıkabilir.

Yerin belleği, daha önce düşünülmüş seçenekleri, alınmış kararları ve görülmüş sonuçları çalışmanın devamına bağlar. İç düzeni de bu belleğin kullanılmasını sağlar. Açık iş ile kapanmış işin, geçici not ile kabul edilmiş kararın, varsayım ile doğrulanmış bilginin statüsü anlaşılabilmelidir. Böylece çalışma alanı her açıldığında sıfırdan başlayan bir yüzey olmaktan çıkar.

Yerin sınırları, neyin içeride ve dışarıda kaldığını belirler. Hangi işlerin burada yürüdüğü, hangi bilgilerin gerekli olduğu, hangi kararların başka yerde verildiği ve hangi yükümlülüklerin kapsam dışında bulunduğu açıklığa kavuşur. Sınır yalnızca erişimi kısıtlamak için bulunmaz; dikkat ve sorumluluğun yönünü de belirler. Başka karargâhlarla bağlantılar bu sınırlar üzerinden kurulur. Bilgi almak, iş devretmek ve ortak karar vermek birbirinden farklı ilişkilerdir.

### Taşıyıcı ve sınırlar

Mekânın taşıyıcısı, bedeniyle belirli bir yerde bulunan ve başka yerlere araçlarla erişen kişidir. Her yerde aynı anda bulunamaz; belirli bir konumdan görür, ilişki kurar ve müdahale eder. Masaüstü, erişilebilen şeyleri ve kullanılabilen araçları bir çalışma alanında buluşturur. Başka yerdeki bir işi görmek, oraya talep iletmek ve oradan sonuç almak aynı türden yakınlık değildir.

~~~text
  yerin bellegi: her seyin statusu anlasilir
     acik is          |   kapanmis is
     gecici not       |   kabul edilmis karar
     varsayim         |   dogrulanmis bilgi

  yerin siniri ve disariyla uc ayri iliski:

  .---- bu karargah ----.                   .-- baska karargah --.
  |                     |  <-- bilgi almak  |                    |
  |  burada yuruyen     |  is devretmek --> |                    |
  |  isler              |  <- ortak karar-> |                    |
  `---------------------'                   `--------------------'

  sinir yalnizca erisimi kisitlamaz;
  dikkatin ve sorumlulugun yonunu de belirler

  ayni turden yakinlik degildir:
    baska yerdeki isi gormek . oraya talep iletmek .
    oradan sonuc almak
~~~

*Çizim 7 — Yerin belleği, sınırı ve başka karargâhlarla üç ayrı ilişki.*

Karargâhın yeri ekranın görünen yüzeyiyle sınırlanmaz; bütün ilişkiler tek ekrana sığmak zorunda değildir. Bununla birlikte her yerde ve hiçbir yerde olduğu söylenen belirsiz bir ortam olarak da tanımlanmaz. Kişinin bütün dünyasının yerine geçmez ve bütün hayatı tek alana doldurmayı gerektirmez. Farklı sorumluluklar için ayrı karargâhlar kurulabilir. Kendi sınırlarının bulunması, dışarıyla bağlantı kurmasını engellemez.

Bu mimaride mekân, kişinin neye erişebildiğini, neye etki edebildiğini ve kimlerle çalışabildiğini anlamaya yardım eder. İnsanı yalnızca karar veren bir zihin olarak almak, bedeni, çalışma koşullarını ve başkalarıyla ilişkileri siler. Masaüstünün önemi bu koşulları belirli bir iş çevresinde bir araya getirmesindedir.

### Masaüstünde uygulama

1. Çalışmaya dönüldüğünde ilk açılacak kaydı ve çalışma yerini belirle. Bu bir masaüstü klasörü, mevcut proje dizini veya erişebildiğin başka bir çalışma alanı olabilir.

2. 2 Mekan alanına güncel çalışma kaydının yerini ve ilgili kaynakların dosya yollarını ya da bağlantılarını yaz. Kaynakları sırf bir araya getirmek için taşımak veya çoğaltmak zorunlu değildir.

3. Açık işlerin, alınmış kararların ve tamamlanmış çıktıların nerede bulunacağını anlaşılır kıl. Birden fazla sürüm varsa güncel olanı belirt.

4. Başka kişi veya çalışma alanlarıyla bağlantıların ne işe yaradığını kaydet: bilgi alma, iş devri veya ortak karar. Bu işin dışında kalan alanları kapsamla birlikte değerlendir.

### Kayda geçirilecekler

Çalışma kaydının 2 Mekan alanında giriş noktası, güncel kayıt, kullanılan kaynaklar ve dış ilişkilerin amacı bulunur. Bağlantılar kadar kaynakların hangi iş için kullanıldığı da açıklanır.

### Tamamlanma ölçütü

Kişi işe geri döndüğünde nereden başlayacağını, hangi kaydın güncel olduğunu ve ihtiyaç duyduğu kaynaklara nasıl ulaşacağını anlayabiliyorsa bu protokol yeterince ele alınmıştır. Erişilemeyen bir kaynak varsa bunun hangi bilgiyi veya işi etkilediği kaydedilir; erişilmiş gibi gösterilmez.

## 3 Usül Protokolü

### Kurucu sorular

> Nasıl işler yapar? Bu yaptıklarını, ona has yapan nelerdir? Neler değildir?

### İşin yürütülmesi

Masaüstü karargâhı, durumu eyleme ve eylemin sonucunu yeni bir duruma dönüştüren ilişkilerle işler. İlgili olanı seçme, mevcut durumu anlama, karar verme, kararı yapılabilir işe bağlama ve sonucu değerlendirme birbirini besler. Bu faaliyetler her işte aynı sırayla uygulanan katı bir prosedür oluşturmaz; kimi zaman birlikte yürürler. Belirleyici olan aralarındaki bağların kopmamasıdır.

İlgili olanı seçmek, çalışma alanına giren bilgilerin mevcut mesele açısından değerini ayırt etmektir. Gereksiz bilgiyi dışarıda bırakmak, eksik bilgiyi fark etmek ve öncelik vermek bu işin içindedir. Durumu anlamak ise neyin bilindiğini, neyin varsayıldığını, hangi işlerin açık olduğunu, hangi kaynakların kullanılabildiğini ve işi hangi bağımlılıkların beklettiğini kavramayı gerektirir. Çok sayıda veri görmek bu anlayışı tek başına sağlamaz.

Karar, seçeneklerin amaç ve kısıtlarla birlikte değerlendirilmesiyle oluşur. Bir yol seçilebilir, çalışma ertelenebilir, ek bilgi istenebilir veya iş durdurulabilir. Karar vermek her zaman yeni bir görev başlatmak anlamına gelmez. Karar uygulamaya bağlandığında neyin yapılacağı, kimin yapacağı, hangi koşullarda yürütüleceği ve ne olduğunda tamamlanmış sayılacağı işin büyüklüğüne uygun açıklıkta belirlenir.

Sonuç, başlangıçtaki beklentiyle karşılaştırılır. İş kapanabilir, düzeltilebilir veya amacı yeniden ele alınabilir. Karargâh böylece yalnızca iş çıkaran bir merkez olarak kalmaz; yaptıklarının sonucunu değerlendirebilen bir düzene dönüşür. Küçük bir işte bu bağ tek bir notla kurulabilir. Ortak veya kapsamlı bir işte daha açık kayıt, devir ve takip ilişkileri gerekebilir.

### Bağlam, yöntem ve iş devri

Karargâhın yaptığı işi kendine özgü kılan, görevi bağlamıyla birlikte ele almasıdır. Görevin hangi amaca hizmet ettiği, hangi karardan çıktığı ve diğer işlerle ilişkisi anlaşılabilir. İyi görünen bir öneri ile uygulanabilir bir karar arasındaki fark da gözetilir. Mevcut kaynaklar, zaman ve yetkilerle bağ kurulduğunda soyut tercih somut çalışma yoluna dönüşebilir.

İş başka bir kişiye veya merkeze geçtiğinde bağlamın, beklenen sonucun ve geri dönüş yolunun korunması gerekir. Karargâh bütün işleri kendi içinde yapmak zorunda değildir. Bazı durumlarda esas işi, farklı yerlerde yürüyen çalışmaların birbirine uygun ilerlemesini sağlamaktır. İş devri, karargâhın o işle ilişkisinin bütünüyle kaybolması anlamına gelmez.

Çıktı ile amaçlanan sonuç ayrı tutulur. Bir dosyanın hazırlanması bir çıktıdır; o dosyanın hizmet ettiği ihtiyacın karşılanması başka bir sorudur. Bir öğrenme atölyesinde içeriği hazırlamak, malzemeyi tamamlamak ve katılımcıları bilgilendirmek yürütülen işlerdir. Katılımcıların amaçlanan beceriyi kazanması ise bu işlerin hizmet ettiği sonuçtur. İşlemlerin tamamlanması ile amacın gerçekleşmesi aynı ölçüyle değerlendirilmez.

~~~text
  .--- karargah ---.         D E V I R         .-- baska kisi --.
  |                |  ======================>  |   ya da merkez |
  |      is        |    isle birlikte gider:   |                |
  |                |      baglam               |       is       |
  |                |      beklenen sonuc       |                |
  |                |  <======================  |                |
  `----------------'      geri donus yolu      `----------------'

  is devri, karargahin o isle iliskisinin butunuyle
  kaybolmasi anlamina gelmez

  cikti ile sonuc ayri tutulur (ogrenme atolyesi ornegi):
    cikti    icerik hazirlandi . malzeme tamamlandi .
             katilimcilar bilgilendirildi
    sonuc    katilimcilar amaclanan beceriyi kazandi mi?
~~~

*Çizim 8 — İş devri: bağlam, beklenen sonuç ve geri dönüş yolu işle birlikte gider.*

Usulün taşıyıcısı, nasıl yapılacağını öğrenen, yöntemi uygulayan ve uygunluğunu değerlendiren kişidir. Yöntem önceki deneyimlerden, başkalarından, ortak kurallardan veya araçların kuruluşundan gelebilir. Kişinin her yöntemi kendisinin icat etmesi gerekmez. Buna karşılık yöntemin hangi koşullarda işe yaradığını sorgulama ve gerektiğinde değiştirme yolu açık tutulur. Bir işlemin tanımlandığı gibi yapılması ile meselenin gereğine uygun yapılması birbirine bağlı, fakat ayrı sorulardır.

### Usulün sınırları

Bu işleyiş yalnızca izleme, sürekli bilgi toplama veya birbirinden kopuk görevleri hızla tamamlama değildir. Bilginin bir meseleye, karara veya eyleme katkısı bulunmalıdır. Her şeyi otomatikleştirmek de tanımın gereği değildir. Otomasyon bir uygulama tercihi olabilir; hangi işin neden yapılacağını kendiliğinden belirlemez. Düzenin ağırlığı, işin gerektirdiği açıklığı aşmamalı; her küçük iş için ağır prosedür kurulması zorunlu sayılmamalıdır.

Başlatmak kadar beklemek, devretmek, durdurmak ve kapatmak da geçerli işlemlerdir. Sürekli yeni görev üretmek, amaca yaklaşıldığını göstermez. Karargâhı kurmak ve yeniden düzenlemek, onun hizmet ettiği işin yerine geçmemelidir. Taşıyıcı da yalnızca kendisine verilen görevleri bitiren bir yürütücü olarak tanımlanmaz; görevin neden yapıldığını, yöntemin işleyip işlemediğini ve işin sürdürülüp sürdürülmeyeceğini sorabileceği bir yer bulunur.

~~~text
  ilgili      durumu      karar       karari           sonucu
  olani  -->  anla   -->  ver    -->  yapilabilir -->  degerlendir
  sec                                 ise bagla             |
    ^                                                       |
    `-------------------------------------------------------'
  kati bir sira degil; belirleyici olan aradaki baglarin kopmamasi

  karar:            bir yol sec . ertele . ek bilgi iste . durdur
  yapilabilir is:   ne yapilacak?  kim yapacak?  hangi kosulda?
                    ne oldugunda tamamlanmis sayilacak?
  gecerli islemler: baslat . bekle . devret . durdur . kapat

  degildir:  yalnizca izleme . surekli bilgi toplama .
             kopuk gorevleri hizla bitirme . her seyi otomatiklestirme
  karargahi kurmak ve yeniden duzenlemek, hizmet ettigi isin
  yerine gecmemelidir
~~~

*Çizim 9 — Usül: birbirini besleyen beş faaliyet; karar türleri ve geçerli işlemler.*

### Masaüstünde uygulama

1. Sıradaki mesele için ilgili bilgiyi seç. Bilinenleri, varsayımları ve kararı etkileyen eksikleri çalışma kaydında ayır.

2. Seçilen yöntemi ve gerekçesini yaz. İlk uygulama adımını seçerken 5 Gaye alanındaki beklenen sonuç ile 4 Zaman alanındaki koşulları birlikte değerlendir. Gerekirse bilgi edinme veya bekleme kararı ver.

3. Sıradaki yapılabilir işi tanımla: ne yapılacak, kim üstleniyor, hangi çıktı bekleniyor ve sonuç nerede görülecek? İş devrediliyorsa aktarılacak bağlamı ve geri dönüşü belirt.

4. Seçilen iş yürütüldüğünde oluşan çıktı veya gözlemin yerini kayda ekle. Henüz yapılmamış işi plan olarak tut; gerçekleşen sonucu ayrı yaz.

5. Sonucu beklentiyle karşılaştır. Bir sonraki iş, düzeltme, bekleme veya kapanış kararını ve kısa gerekçesini kaydet.

### Kayda geçirilecekler

Çalışma kaydının 3 Usül alanında yöntem ve gerekçesi, sıradaki iş, işi üstlenen kişi veya birim, beklenen çıktı, geri dönüş yolu ve gerçekleştiyse sonuç bulunur. Çok sayıda iş olduğunda aynı kısa kayıt biçimi gerektiği kadar tekrarlanabilir.

### Tamamlanma ölçütü

Seçilmiş bir kararın yapılabilir işe nasıl bağlandığı ve sonucunun nasıl değerlendirileceği anlaşılabiliyorsa yöntem kaydı hazırdır. Uygulama yapıldıysa sonuç ve sonraki karar da yazılır. Beklemek veya bilgi istemek gerekçeli bir karar olabilir; yöntem kaydının tamamlanması gayeye ulaşıldığı anlamına gelmez.

## 4 Zaman Protokolü

### Kurucu sorular

> Hangi andadır? Bu anı, diğer zamanlardan farklı yapan nelerdir? Neler değildir?

### An ve karar

Masaüstü karargâhı, geçmişten gelen kayıtların ve yükümlülüklerin mevcut koşullar içinde geleceğe dönük karara ve eyleme çevrilebildiği andadır. An, yalnızca takvimdeki bir nokta olarak alınmaz; işin belirli koşullar altında bulunduğu evreyi de anlatır. Geçmiş bilgiler, şimdiki imkânlar ve henüz açık seçenekler birlikte değerlendirilir.

Karargâhın karakteristik anı, eldeki durumla yapılabilecek şey arasında hâlâ etkili olabilecek bir bağlantının kurulabildiği andır. Bu ifade mimarinin yalnızca karar verilirken var olduğu anlamına gelmez. Hazırlıkta, beklemede, yürütmede ve iş bittikten sonraki değerlendirmede de varlığını sürdürür. Karargâh işlevi, bu evrelerin her birinde mevcut durum ile uygun eylemi ilişkilendirdiğinde belirginleşir.

### Anı ayırt eden koşullar

Bir çalışma anını diğerinden ayıran koşullardan biri, o anda bilinenler ve bilinmeyenlerdir. Yeni bilgi gelmiş olabilir; daha önce güvenilen bir bilgi geçerliliğini yitirmiş olabilir. Bilginin içeriği kadar hangi ana ait olduğu da önemlidir. İkinci koşul, hangi seçeneklerin hâlâ açık olduğudur. Bir karar uygulanmadan önce mümkün olan bir yol, uygulamadan sonra aynı biçimde mümkün olmayabilir.

Kullanılabilir kaynaklar, yetkiler ve hareket alanı da anı belirler. Zaman, insan veya malzeme imkânlarından biri değiştiğinde dosyalar aynı kalsa bile işin içinde bulunulan an değişebilir. Önceden verilmiş taahhütler, kabul edilmiş sorumluluklar ve başlatılmış işler mevcut seçenekleri etkiler. Şimdi verilecek karar boş bir zeminde oluşmaz.

Müdahalenin etkili olabileceği süre ayrıca gözetilir. Bir kararın ne zamana kadar neyi değiştirebileceği, tarihin kendisi kadar önem taşır. Etkinliğin içeriği henüz kesinleşmemişken yapılabilecek değişikliklerle katılımcılar bilgilendirildikten sonra yapılabilecek değişiklikler farklıdır. Aynı belge açık olsa bile aynı çalışma anında bulunulmaz.

### Taşıyıcının zamanı ve çalışma ritimleri

Zamanın taşıyıcısı, geçmişi, taahhütleri ve açık seçenekleri bulunan kişidir. Buradaki zaman, bir işi yetiştirebilmenin, kararı değiştirebilmenin, bekleyebilmenin veya bir fırsatı kaçırmanın zamanıdır. Teknik araç bir son tarihi kaydedebilir; o tarihin önemi işin, insanların ve taahhütlerin ilişkisinde belirlenir. Saatin kaydı ile sürenin insanlar açısından anlamı birbirine indirgenmez.

Mimarinin ölçüsünü aldığı kişinin dikkati ve zamanı sınırlıdır. Bu nedenle seçmek, sıralamak, beklemek ve vazgeçmek zorundadır. İyi bir zaman düzeni her şeyi aynı anda talep etmez; neyin şimdi ele alınması gerektiğini anlamaya yardım eder. Bu, insanı sınırsız zamanı olan bir işlemci gibi ele almamayı gerektirir.

Karargâhın birden fazla çalışma ritmi vardır. Hazırlık düşünmeye ve seçenek üretmeye, yürütme kararların tutarlı uygulanmasına, değerlendirme sonuçların anlaşılmasına zaman ister. Bekleme, gerekli bilginin veya koşulun oluşmasına alan açabilir. Hazırlık isteyen işi sürekli acil işlem gibi ele almak ya da uygulanmakta olan kararı her adımda baştan tartışmak, bu ritimlerin ayrımını kaybettirebilir.

### Zamanın sınırları

Bu zaman kesintisiz aciliyet, sürekli çevrimiçi bulunma veya bütün işleri tek hızda yürütme değildir. Ekranda şimdi görünen şey geçmişteki bir duruma ait olabilir. Belirsiz bir geleceğe sürekli hazırlanmak da tek başına yeterli değildir; hazırlığın hangi olasılığa veya karara hizmet ettiği anlaşılmalıdır. Başlık belirli bir tarihsel dönemi ya da teknoloji çağını zorunlu kılmaz. Burada kayda geçirilen yorum, işin içindeki karar ve müdahale zamanına ilişkindir.

~~~text
  GECMIS                 SIMDI                        GELECEK
  kayitlar               bilinenler, bilinmeyenler    hala acik
  yukumlulukler  ----->  kaynaklar, yetkiler,  -----> secenekler
  taahhutler             hareket alani
                         |<- mudahalenin etkili olabilecegi sure ->|

  ayni belge acik olsa bile ayni calisma ani degildir:
    etkinligin icerigi kesinlesmeden once . . . .  bir tur degisiklik
    katilimcilar bilgilendirildikten sonra . . . .  baska tur degisiklik

  calisma ritimleri:
    hazirlik         dusunmeye ve secenek uretmeye zaman ister
    yurutme          kararlarin tutarli uygulanmasina
    bekleme          gerekli bilginin ya da kosulun olusmasina
    degerlendirme    sonuclarin anlasilmasina

  degildir:  kesintisiz aciliyet . surekli cevrimici bulunma .
             butun isleri tek hizda yurutme
  ekranda simdi gorunen sey gecmisteki bir duruma ait olabilir
~~~

*Çizim 10 — Zaman: geçmişin şimdiki koşullarda karara çevrildiği an; dört çalışma ritmi.*

### Masaüstünde uygulama

1. Mevcut çalışma evresini belirt: hazırlık, yürütme, bekleme veya değerlendirme. Durumu hangi tarihte gözlediğini yaz; saat önemliyse saat dilimini de belirt.

2. 4 Zaman alanında bilinen son tarihleri, taahhütleri ve müdahalenin etkili olabileceği süreleri kaydet. Bilinmeyen bir tarih için tahmin üretmek yerine henüz belirlenmedi yaz.

3. Hangi seçeneklerin açık olduğunu, hangi bilginin güncelliğinin önemli olduğunu ve hangi kaynağın veya koşulun beklendiğini açıkla.

4. Bir sonraki değerlendirme için tarih veya olay koşulu belirle. Koşul değiştiğinde ilgili protokolü güncelle; bütün çalışmayı baştan kurmak zorunda değilsin.

### Kayda geçirilecekler

Çalışma kaydının 4 Zaman alanında mevcut evre, gözlem tarihi, zaman kısıtları, beklenen bilgi veya koşul ve yeniden değerlendirme zamanı ya da koşulu bulunur. Sayısal süre ve kesin tarih yalnızca iş açısından gerekli ve biliniyorsa yazılır.

### Tamamlanma ölçütü

İşin hangi evrede olduğu, neyin şimdi yapılabileceği ve ne olduğunda yeniden bakılacağı anlaşılabiliyorsa zaman kaydı tamamdır. Gerçek bir son tarih yoksa yalnızca protokolü doldurmak için son tarih konmaz. Bekleme durumunda beklenen koşul ve bunun işle ilişkisi açıklanır.

## 5 Gaye Protokolü

### Kurucu sorular

> Hangi nihai amaca hizmet eder? Bu nihai amaca ulaştıran nelerdir? Neler değildir?

### Amaç düzeyleri

Masaüstü Karargâhları Mimarisi için önerilen gaye, kişinin veya topluluğun seçtiği ya da üstlendiği amaçları gerçek koşullar içinde gerçekleştirebilmesini, ne yaptığını ve hangi sonuçları doğurduğunu anlayarak gerektiğinde yön değiştirebilmesini sağlamaktır. Başlık tek başına zorunlu bir nihai amaç bildirmez. Bu gaye, burada kurulan mimari anlayışının tasarım tercihidir.

İşlem, işin somut amacı ve mimarinin amacı ayrı düzeylerdir. Bir materyali hazırlamak yapılacak işlemdir. Katılımcıların belirli bir beceriyi uygulayabilmesi, bu işlemin hizmet ettiği iş amacıdır. İnsanların amaçlarını koşullara uygun eylemlere dönüştürebilmesi ve sonuçları değerlendirebilmesi ise mimarinin amacıdır. Bir araştırma, üretim işi veya bakım faaliyeti aynı mimariden yararlanabilir; hizmet ettikleri somut sonuçların aynı olması gerekmez.

Amaç yalnızca hedefe ulaşmak olarak ele alınmaz. Hedefin hâlâ anlamlı olup olmadığını fark etmek de gayeyle ilişkinin içindedir. İhtiyaç değişmişken bütün görevlerin eksiksiz tamamlanması kendiliğinden başarı sayılmaz. Karargâhın başarısı, kendi içinde ne kadar hareket ürettiğiyle değil, hizmet ettiği işte hangi anlamlı sonucu mümkün kıldığıyla değerlendirilir.

### Gayeye ulaşma ilişkileri

Gayeye ulaşmak için amaçla iş arasındaki bağ korunur. Her küçük işlem uzun bir açıklama gerektirmese de çalışma bütünü içinde neye hizmet ettiği anlaşılabilmelidir. Öncelikler gerçekten seçilmeli; bazı işleri ertelemek veya yapmamak da mümkün olmalıdır. Yalnızca daha fazla iş almayı kolaylaştıran bir düzen, dikkat ve kaynakların hangi sonuç için kullanıldığını belirsizleştirebilir.

Kararların gerekçeleri, koşullar değiştiğinde neyin yeniden değerlendirilmesi gerektiğini anlamaya yardım eder. Gerekçesi kaybolmuş kararlar alışkanlıkla sürdürülebilir. Sonuçların amaçla karşılaştırılması, yapılan işin miktarı ile sağlanan yararı ayırır. Hangi ihtiyacın karşılandığı ve hangisinin açık kaldığı sorulabilmelidir.

Amaçlar, koşullar ve çalışma biçimleri değişebildiği için mimarinin uyarlanabilir olması önem taşır. Plan, yöntem ve kayıtlar gözden geçirilebilmelidir. Araçların kuruluşu zaman içinde sorgulanamaz bir zorunluluğa dönüşmemelidir. Ortak işlerde sonucun hangi kararlarla oluştuğu ve kimin hangi sorumluluğu üstlendiği anlaşılabilmelidir. Bu açıklık, birlikte öğrenmeye ve sonraki kararları sağlam bir zeminde vermeye yardım eder.

İşin kapanabilmesi de gayeye hizmet eder. Yeterli sonuç alındığında işin tamamlandığı söylenebilmeli, karargâh küçültülebilmeli veya başka bir amaç için yeniden düzenlenebilmelidir. Bir öğrenme atölyesinde bütün hazırlıkların bitmiş olması, hedeflenen öğrenmenin gerçekleştiğini tek başına göstermez. Amaçlanan beceri kazanılmamışsa değerlendirme sürer. Amaç gerçekleşmişse sırf düzeni çalışır tutmak için yeni görev üretmek gerekmez.

### Gayenin taşıyıcısı ve sorumluluk

Gayenin taşıyıcısı, bir sonucu önemseyen ve neden istendiğini sorabilen kişidir. Amaç bireysel olarak seçilmiş, ortaklaşa belirlenmiş veya bir sorumluluğun parçası olarak üstlenilmiş olabilir. Her durumda bu sonucun kimin için gerekli olduğu, neyi değiştireceği, hangi bedellerin kabul edildiği ve hangi koşullarda yeniden ele alınacağı sorularının muhatabı bulunmalıdır.

Bir hedefin teknik olarak tanımlanabilmesi, neden değerli olduğunu kendiliğinden açıklamaz. Başarı ölçütü gayenin belirli bir temsilidir; tamamı olmak zorunda değildir. Bu mimari önerisinde amacı sahiplenme, sorgulama ve değiştirme sorumluluğu insanlarda tutulur. Bu tercih, teknik sistemlerin bütün olası kapasiteleri hakkında bir hüküm olarak sunulmaz.

İşin insanlardan, araçlardan ve kurallardan oluşan bir bütün içinde gerçekleşmesi, kararların sahipsiz kalmasını gerektirmez. Sistem böyle yaptı ifadesi bir işlemin nasıl gerçekleştiğini açıklayabilir; fakat amacın kim tarafından belirlendiği, kuralın neden kabul edildiği ve sonucun nasıl değerlendirileceği sorularını tek başına karşılamaz. Amaç tartışmalı hâle geldiğinde işin kimin adına yapıldığı, kimin yeniden değerlendirebildiği ve sonucun muhatabının kim olduğu görülebilmelidir.

### Gayenin sınırları

Daha fazla görev tamamlamak, daha çok bilgi biriktirmek, her şeyi tek yerde toplamak veya azami otomasyon sağlamak kendiliğinden nihai amaç değildir. Hız, verimlilik ve düzen seçilen sonuca katkıları ölçüsünde değerlendirilir. Yanlış seçilmiş bir işi hızlandırmak doğru sonuca yaklaşıldığını göstermez. Her şeyi kontrol edebilmek de amaç olarak varsayılmaz; karargâhın etkileyebildiği alanla yalnızca izleyebildiği alanın sınırları vardır.

~~~text
  UC DUZEY  (ogrenme atolyesi ornegi)

  mimarinin amaci    insanlar amaclarini kosullara uygun eylemlere
       ^             donusturebilsin, sonuclari degerlendirebilsin
       |
  isin amaci         katilimcilar belirli bir beceriyi uygulayabilsin
       ^
       |
  islem              bir materyali hazirlamak

  butun hazirliklarin bitmesi  =/=  hedeflenen ogrenmenin gerceklesmesi

  kendiliginden nihai amac degildir:
    daha fazla gorev . daha cok bilgi . her seyi tek yerde toplamak .
    azami otomasyon . her seyi kontrol edebilmek

  "Sistem boyle yapti" bir islemin nasil gerceklestigini aciklar;
  sunlari karsilamaz:
    amaci kim belirledi?   kural neden kabul edildi?
    sonuc nasil degerlendirilecek?
~~~

*Çizim 11 — Gaye: işlem, işin amacı ve mimarinin amacı üç ayrı düzeydir.*

Mimarinin kendi faaliyetini sürekli sürdürmesi, hizmet ettiği gayeden bağımsız bir gerekçeye dönüşmemelidir. Teknik araçların çalışması ile anlamlı bir sonucun oluşması ayrı değerlendirilir. Karargâh, insanın ve birlikte çalışan insanların eylem imkânlarını taşır ve genişletir; kendi çalışmasını onların hizmet ettiği gayenin yerine koymaz.

### Masaüstünde uygulama

1. 5 Gaye alanında bu iş sonunda kimin için neyin değişmesinin istendiğini kısa bir paragrafla yaz.

2. Yapılacak işlem, üretilecek çıktı ve beklenen anlamlı sonucu ayrı cümlelerle ifade et. Bunların birbirine nasıl hizmet ettiğini açıkla.

3. Beklenen değişimin nasıl anlaşılacağını belirt. Uygun olduğunda bir gözlem, karşılaştırma, geri bildirim veya ölçüm kullan; her iş için sayısal gösterge zorunlu değildir.

4. Amaçla ilgisi zayıflayan işleri ve seçilen öncelikleri değerlendir. Amacın hangi koşullarda yeniden ele alınacağını kaydet.

5. Uygulama sonucu varsa elde edilen değişimi başlangıçtaki amaçla karşılaştır. Henüz sonuç yoksa değerlendirme yolunu hazırla; başarı gerçekleşmiş gibi yazma.

### Kayda geçirilecekler

Çalışma kaydının 5 Gaye alanında amaç, sonucun muhatabı, beklenen anlamlı değişim, sonucun nasıl anlaşılacağı ve amacı yeniden değerlendirme koşulları bulunur. Gerçekleşmiş sonuç varsa dayanağıyla birlikte eklenir.

### Tamamlanma ölçütü

Hangi sonucun neden önemsendiği ve o sonucun nasıl değerlendirileceği anlaşılabiliyorsa gaye kaydı hazırdır. Bu hazırlık, gayenin gerçekleştiğini göstermez. Amaç değiştiğinde gerekçesi kaydedilir ve bunun kapsam, yöntem veya zaman üzerindeki etkisi ilgili bölümlere işlenir.

## 6 Kökleşme (Bitiş) Protokolü

### Kurucu sorular

> Bu kuruluş veya çalışma döngüsünde ne tamamlandı? Beş boyut nasıl bir bütün oluşturdu? Başlangıçtaki mesele bakımından hangi sonuca ulaşıldı, neler açık kaldı? Kapanış neyi bitirir, neyi açık bırakır?

### Bütünlük ve yer edinme

Kökleşme Protokolü, Varlık, Mekan, Usül, Zaman ve Gaye protokollerinde kurulan ayrımları birlikte değerlendirir ve belirli bir kuruluş veya çalışma döngüsünü sonuçlandırır. Tanımlanan öznenin çalışma alanıyla, yöntemin mevcut imkânlarla, zaman düzeninin işleyişle ve bütün bunların gayeyle ilişkisi gözden geçirilir. Başlangıç kaydına dönülerek açılmış soruların hangi karşılıkları bulduğu anlaşılır hâle getirilir.

Kökleşme, ortaya çıkan anlayışın ve çalışma düzeninin sonraki kullanımda dayanılabilecek bir zemin kazanmasını ifade eder. Bitiş ise belirli bir döngünün kapanışıdır. İkisi birlikte, neyin kurulmuş olduğunu ve bu kuruluşun hangi kayıtlarla devam ettirilebileceğini açıklığa kavuşturur. Böyle bir bitiş, mimarinin artık değişmeyeceğini ilan etmez.

### Kapanışın kapsamı ve dayanakları

Kavramsal kuruluşun tamamlanması, işin uygulamada sonuçlanması ve düzenin kullanım içinde süreklilik kazanması ayrı değerlendirilir. Yalnızca tanımlar ve protokol metni hazırlanmışsa kapanış bu kapsamda kaydedilir. Uygulamada kökleşme veya gayenin gerçekleşmesi hakkında bir sonuç yazılacaksa bu sonucu destekleyen kullanım kayıtları ve gözlemler belirtilir. Belgenin varlığı, uygulama sonucunun yerine geçmez.

Gaye Protokolü hangi sonucun önemsendiğini açıklar. Kökleşme Protokolü, kurulan bütünün ve gözlenen sonuçların bu gayeyle ilişkisini değerlendirir. Gayenin açıklanmış olması, gerçekleştiğinin kanıtı değildir. Üretilen çıktı, sağlanan değişim ve henüz bilinmeyen sonuç birbirinden ayrılır. Başlangıçtaki bir varsayımın bırakılması veya bir sınırın anlaşılması da bu döngünün sonucu olabilir.

Kapanış kaydı, tamamlanan kapsamı, sonuçların dayanaklarını ve açık kalanları birlikte taşır. Bazı işlerin sürmesi, beklemesi veya başka birine devredilmesi mümkündür. Bu durumlar, her şey tamamlanmış gibi gösterilmeden ayrı ayrı belirtilir. Bir devrin gerçekleştiği söyleniyorsa hangi işin kime geçtiği anlaşılır olmalıdır; yalnızca planlanmış devir, gerçekleşmiş devir olarak kaydedilmez.

### Devam ve yeniden açma

Son geçerli kayıt, kaydın bulunduğu yer ve devam eden sorumluluklar belirlenir. Daha sonra neyin değişmesi hâlinde konunun yeniden ele alınacağı yazılır. Yeni bilgi, değişen amaç, beklenen koşulun oluşması veya yöntemin işlemediğinin görülmesi yeniden değerlendirme nedeni olabilir. Önceki kapanış silinmeden yeni kararın tarihi ve gerekçesi eklenir.

Kökleşme, aynı işi sürekli yeniden açmayı veya yeni görev üretmeyi gerektirmez. Yeterli sonuç alınmışsa çalışma kapanabilir. Bir çalışmanın sürdürülmemesine karar verildiğinde bunun gerekçesi ve geride bıraktığı açık meseleler kaydedilebilir. Yeni bir başlangıç yapılırsa, hangi kayıt ve hangi sorudan hareket edildiği anlaşılabilir kalır.

### Bitişin sınırları

Metnin sonuna gelinmesi bütün işlerin tamamlandığını; dosyanın kaydedilmesi de çalışma düzeninin uygulamada yerleştiğini tek başına göstermez. Kökleşme, yalnızca başarıların sıralandığı bir kapanış metni değildir. Çelişkiler, karşılanmamış ihtiyaçlar ve açık sorular da kayda girer. Tamamlanan döngünün sınırları görünür olduğunda bitiş, sonraki çalışmanın nereden başlayabileceğini açıklayabilir.

~~~text
  UC AYRI TAMAMLANMA
    kavramsal kurulus        tanimlar ve protokol metni hazir
    uygulamada sonuc         is yapildi, sonuc goruldu
    kullanimda sureklilik    duzen kullanilarak yer edindi

  yalnizca metin hazirlandiysa kapanis bu kapsamda yazilir;
  belgenin varligi, uygulama sonucunun yerine gecmez

  kapanis kaydi:
    tamamlanan kapsam  +  sonuclarin dayanaklari  +  acik kalanlar

  acik kalan is icin:   surdur . beklet . devret . kapat
                        planlanan devir, gerceklesmis devir
                        olarak kaydedilmez

  yeniden acma nedeni:  yeni bilgi . degisen amac .
                        beklenen kosulun olusmasi .
                        yontemin islemediginin gorulmesi

  onceki kapanis silinmez; yeni kararin tarihi ve gerekcesi eklenir
~~~

*Çizim 12 — Kökleşme: üç ayrı tamamlanma, kapanış kaydı ve yeniden açma.*

### Masaüstünde uygulama

1. Tohum kaydı ile 1–5 alanlarını birlikte oku. Başlangıç meselesinin hangi karşılıkları bulduğunu ve bölümler arasında kalan çelişkileri belirle.

2. Kapanışın kapsamını yaz: kavramsal kuruluş, uygulama, değerlendirme veya gerekçeli sonlandırma. Elde edilen çıktı, amaçlanan değişim ve bunları destekleyen kayıtları ayır.

3. Açık kalan işler için sürdürme, bekletme, devretme veya mevcut kapsamı kapatma kararını ve gerekçesini belirt. Henüz gerçekleşmemiş devri plan olarak kaydet.

4. Son geçerli kaydın yerini, devam eden sorumlulukları ve yeniden değerlendirmeyi gerektirecek koşulları yaz. Yeni çalışma açılırsa bu kapanış kaydıyla ilişkisini belirt.

5. 6 Kökleşme alanını tarihleyerek döngüyü sonuçlandır. Önceki kapanışı silmeden ilerideki yeniden açma kararlarını güncelleme kaydına ekle.

### Kayda geçirilecekler

Çalışma kaydının 6 Kökleşme alanında kapanışın kapsamı ve tarihi, başlangıç meselesine verilen karşılık, tamamlananlar, sonuçların dayanakları, açık kalanlar, varsa devir ve yeniden açma koşulları bulunur. Son geçerli kaydın yeri de belirtilir.

### Tamamlanma ölçütü

Neyin tamamlandığı ve neyin açık kaldığı, sonuçların neye dayandığı ve devamın nasıl ele alınacağı anlaşılabiliyorsa döngü kapanabilir. Açık bir mesele kapanışı otomatik olarak geçersiz kılmaz; statüsü belirtilmelidir. Uygulamada kökleşme iddiası ancak bunu destekleyen kullanım ve devamlılık kayıtları varsa yazılır.

## Ek: Çalışma kaydı şablonu

Aşağıdaki şablonu ayrı bir Markdown dosyasına kopyalayarak bu protokolleri bir işe uygulayabilirsin. Boş alanlar gerçek çalışma sırasında doldurulur.

```markdown
# Çalışma kaydı

Bu şablonu her çalışma için kopyala. Açıklamaları kısa paragraflarla doldur. Bilinmeyen bir alan için “henüz belirlenmedi” yaz; kararı etkiliyorsa hangi bilginin gerektiğini ekle. Gerçekleşmiş sonuçlarla planları ayrı tut. Bu boş şablon, herhangi bir işin tamamlandığını göstermez.

**Çalışma adı:** [Yaz]

**Kaydı yürüten kişi veya çalışma birimi:** [Yaz]

**Başlangıç tarihi:** [Yaz]

**Son değerlendirme tarihi:** [Yaz; saat önemliyse saat dilimini belirt]

**Mevcut karar:** [Sürdür / beklet / kapat / yeniden aç seçeneklerinden uygun olanı yaz ve kısaca gerekçelendir]

## 0 Tohum (Başlangıç)

**Başlangıç meselesi ve özgün soru:** [Mevcut durumun neden ele alındığını ve sorunun kimin meselesi olduğunu yaz. Varsa ilk talebin özgün ifadesini koru.]

**İlk yönelim ve kapsam:** [Başlangıç beklentisini, ilk kapsamı ve şimdilik kapsam dışında kalanları yaz.]

**Bilinenler, varsayımlar ve açık sorular:** [Bunları birbirinden ayırarak yaz.]

## 1 Varlık

**Çalışmanın tanımı ve sınırı:** [Neyin yürütüldüğünü, geçerli kapsam içini ve kapsam dışını yaz.]

**Özne, sorumluluklar ve teknik taşıyıcılar:** [İnsanları veya çalışma birimini, bilinen karar sorumluluklarını ve kullanılan araçları ayrı belirt.]

**Karar ile eylem bağlantısı:** [Bilginin nasıl karara, kararın nasıl işe ve sonucun nasıl değerlendirmeye döndüğünü açıkla.]

## 2 Mekan

**Çalışmaya giriş noktası ve güncel kayıt:** [Nereden başlanacağını ve güncel kaydın yerini yaz.]

**Kaynaklar ve çıktılar:** [İlgili dosya yollarını veya bağlantıları, ne için kullanıldıklarıyla birlikte yaz.]

**Diğer çalışma alanlarıyla ilişkiler:** [Bilgi alma, iş devri veya ortak karar ilişkilerini yaz.]

## 3 Usül

**Yöntem ve gerekçesi:** [Nasıl çalışılacağını ve neden bu yöntemin seçildiğini yaz.]

**Sıradaki yapılabilir iş:** [İşin adını, ne yapılacağını, işi kimin üstlendiğini, beklenen çıktıyı ve sonucun nereye döneceğini yaz. Birden fazla iş varsa bu paragrafı ve aşağıdaki sonuç paragrafını her iş için birlikte tekrarla.]

**Gerçekleşen sonuç ve sonraki karar:** [Yapılmışsa sonucu ve kaydının yerini yaz. Yapılmamışsa plan olduğunu belirt. Düzeltme, bekleme veya kapanış kararını gerekçesiyle ekle.]

## 4 Zaman

**Mevcut evre ve gözlem tarihi:** [Hazırlık, yürütme, bekleme veya değerlendirme evresini ve bu durumu gözlediğin tarihi yaz.]

**Zaman kısıtları ve taahhütler:** [Bilinen süreleri, son tarihleri ve etkili müdahale aralığını yaz. Gerekmiyorsa bunu belirt.]

**Beklenen koşul ve yeniden değerlendirme:** [Beklenen bilgiyi veya koşulu ve ne zaman ya da hangi olay olduğunda tekrar bakılacağını yaz.]

## 5 Gaye

**Amaç ve sonucun muhatabı:** [Kimin için neyin değişmesinin istendiğini yaz.]

**İşlem, çıktı ve anlamlı sonuç:** [Bu üç düzeyi birbirinden ayır ve aralarındaki bağı açıkla.]

**Sonucu anlama yolu:** [Hangi gözlem, geri bildirim veya ölçümün kullanılacağını yaz. Henüz sonuç yoksa değerlendirme planını belirt.]

**Amacı yeniden değerlendirme koşulu:** [Hangi değişikliğin amacı yeniden ele almayı gerektireceğini yaz.]

## 6 Kökleşme (Bitiş)

**Kapanışın kapsamı ve tarihi:** [Kavramsal kuruluş, uygulama, değerlendirme veya gerekçeli sonlandırma açısından neyin kapandığını yaz.]

**Başlangıç meselesine verilen karşılık:** [Neyin anlaşıldığını, yapıldığını veya değiştiğini yaz.]

**Sonuçların dayanakları:** [Çıktıların, gözlemlerin veya kullanım kayıtlarının yerini belirt. Yalnızca metin hazırlandıysa kapanışı bu kapsamda yaz.]

**Açık kalanlar ve devam kararı:** [Süren, bekleyen veya devredilen işleri gerekçeleriyle belirt. Planlanan devir ile gerçekleşen devri ayır.]

**Son geçerli kayıt ve yeniden açma koşulu:** [Kayıt yerini, varsa devam eden sorumluluğu ve yeniden bakılacak koşulu yaz.]

## Güncelleme kaydı

Önceki kapanışı veya başlangıç gerekçesini silmeden değişiklikleri tarih sırasıyla buraya ekle. Her kayıt için tarih, değişen bölüm, önceki durum, yeni karar ve gerekçe yeterlidir.

[Henüz güncelleme yok. İlk değişiklik olduğunda bu açıklamanın altına bir paragraf ekle.]
```

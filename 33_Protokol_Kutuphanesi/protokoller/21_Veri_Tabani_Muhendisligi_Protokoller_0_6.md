# Veri Tabanı Mühendisliği

**Tohumdan kökleşmeye 0–6 protokolleri**

**Sürüm:** 1.0\
**Tarih:** 31 Ekim 2026\
**Belge durumu:** Tamamlanmış 0–6 metni\
**Biçim:** UTF-8 Markdown; masaüstünde okunabilir, düzenlenebilir ve uygulanabilir çalışma rehberi.

Bu belge, Veri Tabanı Mühendisliği üzerine bu konuşmada sorulan soruları ve geliştirilen yanıtları bir araya getirir. 0 Tohum (Başlangıç) Protokolü çalışmayı açar; 1–5, varlık, mekân, usul, zaman ve gayeyi inceler; 6 Kökleşme (Bitiş) Protokolü sonuçları dayanaklarıyla birleştirir ve devam koşullarını kaydeder. Her bölümde kavramsal açıklamayı masaüstünde yürütülebilecek adımlar, üretilecek kayıt ve tamamlanma ölçütü izler.

Protokol metni tamamlanmıştır. Bu teslim sırasında gerçek bir veri tabanı üzerinde kurulum, değişiklik veya doğrulama yürütülmemiştir. Belgenin sonundaki kayıt şablonu, bu protokolleri seçtiğiniz konu veya sistem üzerinde uygulamanız için boş bırakılmıştır.

## Soruların ve kapsamın kaydı

Başlangıç talimatı aynen korunmuştur:

> Geçmiş bağlamları buraya taşıma. Burası ile sınırlı kalma.

Bu nedenle konuşma dayanağı burada kurulan çerçevedir. Konu, bu konuşmanın dışındaki kamusal teknik kaynaklarla açıklanır; başka konuşmaların kişisel bağlamı metne taşınmaz. 1–5'in başındaki soru cümleleri kullanıcının özgün sorularıdır. 0 ve 6'nın soruları, başlangıç ve bitiş protokolleri için yazılmıştır. Uygulama adımları, cevaplardan oluşturulmuş çalışma düzenidir.

Beş boyut boyunca korunan taşıyıcı sorusu şudur:

> Veri Tabanı Mühendisliği'nin köken aldığı varlık, mekan, usül, zaman, ve gayeyi taşıyan makine kimdir? Kim değildir?

Bu soru teknik taşıyıcı, davranışı açıklayan model ve anlam, yetki veya sorumluluk taşıyan özne ayrılarak ele alınır. İnsanların, kuralların ve teknik araçların birlikte çalışması, bunların aynı tür varlıklar olduğu sonucuna bağlanmaz. 6'ncı protokol, beş bölümün cevaplarını bu ayrım etrafında yeniden birleştirir.

## Ortak kavramsal çerçeve

Veri tabanı mühendisliği, verinin neyi temsil ettiğini, nasıl düzenleneceğini, hangi koşullarda okunup değiştirilebileceğini ve bu düzenin zaman, arıza ve kaynak sınırları karşısında nasıl sürdürüleceğini tasarlayan mühendislik alanıdır. Ortaya koyduğu sistem, verinin kullanılmasını sağlarken ona hangi koşullarda güvenilebileceğini de belirginleştirir.

Varlık, Mekan, Usül, Zaman ve Gaye Protokolleri, bu alanın kimliğini, konumunu, işleyişini, zamansal düzenini ve hizmet ettiği amacı birlikte ele alır. Teknik taşıyıcı ile kurucu ve sorumlu özne arasındaki ayrım, beş bölüm boyunca korunur. Alanın özgünlüğü, tek bir araçtan çok, verinin anlamı ve değişimi çevresinde üstlenilen sorumlulukların birleşiminde belirir.

## Masaüstünde çalışma düzeni

Bu Markdown dosyasını bir çalışma klasörüne koyun; `calisma` adlı bir alt klasör açın ve aşağıda belirtilen kayıtları metin düzenleyicinizle oluşturun. Belgenin sonundaki genel kayıt şablonunu kullanabilirsiniz. Terminal, özel uygulama veya veri tabanı kurulumu, kavramsal inceleme için gerekli değildir.

Önce 0'ı uygulayın; ardından 1–5'i aynı inceleme nesnesi üzerinde yürütün ve 6 ile kapatın. 2'de seçilen önemli işlem 3 ve 4 boyunca aynı işlem olarak izlenir. Başka bir işleme veya sisteme geçmek gerekiyorsa değişikliği 0'da kaydedin. Bölümler tek geçişte bitmek zorunda değildir: bir sonuç önceki varsayımı değiştiriyorsa ilgili kayda dönün. İlk amaç ve başarı beklentisi 0'da yazılır; 5'te ayrıntılandırılır ve gerekirse önceki kararları değiştirir.

| Protokol | Ana iş | Üretilecek çalışma kaydı |
| --- | --- | --- |
| 0 Tohum (Başlangıç) | Soru, ihtiyaç, kapsam ve dayanakları açmak | `calisma/00_TOHUM_KAYDI.md` |
| 1 Varlık | Tanım, kimlik, ilişki ve geçerlilik sınırını açıklamak | `calisma/01_VARLIK_KAYDI.md` |
| 2 Mekan | Yer, sistem sınırı ve karar yetkisini açıklamak | `calisma/02_MEKAN_KAYDI.md` |
| 3 Usül | Kuralları işlem, mekanizma ve kanıta bağlamak | `calisma/03_USUL_KAYDI.md` |
| 4 Zaman | Sıra, görünürlük, geçmiş ve yaşam döngüsünü açıklamak | `calisma/04_ZAMAN_KAYDI.md` |
| 5 Gaye | Amaç, başarı ölçütü ve tercihleri gerekçelendirmek | `calisma/05_GAYE_KAYDI.md` |
| 6 Kökleşme (Bitiş) | Sonucu, dayanağı, devri ve yeniden ele alma koşullarını bağlamak | `calisma/06_KOKLESME_KAYDI.md` |

## Çalışma düzeyi ve dayanak

0'da şu üç düzeyden birini seçin. İlerlerken düzey değişirse gerekçesini kaydedin. Gerçek sisteme erişim bulunmaması, kavramsal incelemeyi veya tasarım çalışmasını başlatmaya engel değildir.

| Çalışma düzeyi | Yapılacak iş | Sonucu destekleyen dayanak |
| --- | --- | --- |
| Kavramsal inceleme | Soruları açıklamak, ayrımları ve sınırları gerekçelendirmek | Açık akıl yürütme, ilgili kaynak, örnek ve karşı örnek |
| Somut sistem tasarımı | Belirli ihtiyaç için model, işlem yolu ve kararlar oluşturmak | Gereksinimlerle ilişkilendirilmiş tasarım ve gerekli doğrulama planı |
| Somut sistem üzerinde doğrulama | Belirlenmiş sistemin seçilen koşullardaki davranışını değerlendirmek | Ortam ve sürüm bilgisi, kabul ölçütü, gözlem ve kanıt kaydı |

Kayıtlarda bir öneriyi, uygulanmış bir değişikliği ve doğrulanmış davranışı ayrı ifade edin. Gerçek bir deneme için beklenen sonuç, gözlenen sonuç ve sonucun dayandığı dosya veya gözlem birlikte yazılır. Elde bulunmayan bilgiyi `Belirlenmedi`, bilinçli kapsam kararını `Kapsam dışı`, seçilen düzeyde gerekmeyen işi `Uygulanmaz` diye kaydedin; kapsam kararının kısa gerekçesini ekleyin.

~~~text
  SIRA  1-5 ayni inceleme nesnesi uzerinde
    0 Tohum --> 1 Varlik --> 2 Mekan --> 3 Usul --> 4 Zaman --> 5 Gaye
    --> 6 Koklesme
    bolumler tek geciste bitmek zorunda degildir
    bir sonuc onceki varsayimi degistiriyorsa  -->  ilgili kayda donulur

  AYNI ISLEM
    2'de secilen onemli islem  -->  3 ve 4 boyunca ayni islem olarak
                                    izlenir
    baska bir isleme veya sisteme gecmek gerekiyorsa
      -->  degisiklik 0'da kaydedilir

  ILK AMAC VE BASARI BEKLENTISI
    0'da yazilir  -->  5'te ayrintilandirilir  -->  gerekirse onceki
                                                    kararlari degistirir

  KAYITTA AYRI IFADE EDILIR
    oneri   |   uygulanmis degisiklik   |   dogrulanmis davranis
    gercek bir denemede birlikte yazilir:  beklenen sonuc . gozlenen
    sonuc . sonucun dayandigi dosya veya gozlem

  UC KAYIT SOZU
    elde bulunmayan bilgi            -->  Belirlenmedi
    bilincli kapsam karari           -->  Kapsam disi  + kisa gerekce
    secilen duzeyde gerekmeyen is    -->  Uygulanmaz
~~~

*Çizim 1 — Masaüstünde çalışma düzeni ve çalışma düzeyi: sıra ve geri dönüş; aynı işlem; ilk amaç ve başarı beklentisi; kayıtta ayrı ifade edilenler; üç kayıt sözü.*

Varsayımsal tiyatro sistemi, bölümler arası süreklilik sağlayan bir örnektir. Bu örnekteki kurallar kullanıcının gerçek sistemi hakkında varsayım sayılmaz. Gerçek bir hedef seçilirse örnekler o hedefin ihtiyaçları ve mevcut kaynaklarıyla yeniden değerlendirilir. Bu belge bir ürün kurulum betiği içermez; çalıştırılacak ürün komutları ancak somut ortam, sürüm ve amaç belirlendiğinde seçilir.

## 0 Tohum (Başlangıç) Protokolü

**Tamamlayıcı protokol sorusu:**

> Bu inceleme hangi ihtiyaçtan doğuyor; neyi, hangi kapsam, dayanak ve sorumluluklarla anlamaya veya gerçekleştirmeye başlıyoruz?

### Başlangıcın niteliği

Tohum, incelemeyi başlatan ihtiyacın, sorunun ve yönelişin kayda geçirilmesidir. Veri tabanı mühendisliğine ilişkin bir çalışma, belirli kayıtların tutulması gereksiniminden, bir çelişkiden, bir arızadan veya alanın kendisini anlama isteğinden doğabilir. Başlangıç protokolü, bu ihtiyacın hangi koşullarda ortaya çıktığını ve çalışmanın neye cevap aradığını açıklar. Henüz verilmemiş bir ürün, model veya mimari kararını başlangıcın zorunlu sonucu saymaz.

Bu çalışmanın tohumu, veri tabanı mühendisliğini varlık, mekân, usul, zaman ve gaye bakımından sorgulayan beş soru ile bu boyutları taşıyan makinenin kim olduğu sorusudur. İlk sorular korunur; inceleme sırasında oluşan yeni sorular ayrıca kaydedilir. Böylece sonraki bir yorumun başlangıçtaki soruymuş gibi görünmesi önlenir.

Tohum Protokolü çalışmanın neden ve hangi soruyla açıldığını kaydeder. Varlık Protokolü incelenen şeyin ne olduğunu; Gaye Protokolü mühendisliğin ve ele alınan sistemin hangi faaliyete hizmet ettiğini inceler. Bu üç bölüm birbiriyle ilişkilidir. Başlangıç gerekçesi, nesnenin tanımı ve hizmet edilen amaç ayrı ayrı açıklanabildiğinde ilişkileri de değerlendirilebilir.

Başlangıçta bilinenler, varsayılanlar ve bilinmeyenler ayrılır. Bir kaynakta bildirilen durumla masaüstünde gözlenen durum aynı tür dayanak değildir. Varsayımsal tiyatro örneği, kavramları sınamak için kullanılabilir; var olan bir işletmenin sistemi hakkında kanıt oluşturmaz. Bilinmeyenin açıkça kaydedilmesi, incelemenin sonraki işini belirler.

~~~text
  TOHUM  incelemeyi baslatan ihtiyacin, sorunun ve yonelisin kayda
         gecirilmesi
    dogabilir:  belirli kayitlarin tutulmasi gereksinimi . bir
                celiski . bir ariza . alanin kendisini anlama istegi
    henuz verilmemis urun, model veya mimari karari  -/->  baslangicin
                                                          zorunlu sonucu
    ilk sorular korunur; inceleme sirasinda olusan yeni sorular ayrica
    kaydedilir

  UC BOLUM  ayri ayri aciklanabildiginde iliskileri degerlendirilebilir
    0 Tohum    calismanin neden ve hangi soruyla acildigi
    1 Varlik   incelenen seyin ne oldugu
    5 Gaye     muhendisligin ve ele alinan sistemin hangi faaliyete
               hizmet ettigi

  BASLANGICTA AYRILIR
    bilinenler   |   varsayilanlar   |   bilinmeyenler
    bir kaynakta bildirilen durum  =/=  masaustunde gozlenen durum
    varsayimsal tiyatro ornegi  -->   kavramlari sinamak icin
                                -/->  var olan bir isletmenin sistemi
                                      hakkinda kanit
    bilinmeyenin acikca kaydedilmesi  -->  incelemenin sonraki isini
                                           belirler
~~~

*Çizim 2 — Tohum: başlangıcın niteliği; Tohum, Varlık ve Gaye; başlangıçta ayrılanlar.*

### Tohumu taşıyanlar

Başlangıcı taşıyan teknik araç; bir Markdown dosyası, çalışma klasörü, modelleme aracı veya incelenen sistem olabilir. Soruyu soran, kapsamı belirleyen ve sonucun neye dayandığını değerlendiren özne ise ilgili insandır. Bir yardımcı veya yazılım verilen adımları yürütebilir; bu işlev, çalışmanın amaç ve sorumluluklarını kendiliğinden üstlendiği anlamına gelmez.

Çalışmanın başlangıç sınırı, kaynakların ve işlem kapsamının belirlenmesini de içerir. Bu belgenin konuşma dayanağı, burada sorulmuş sorular ve bunlara verilen yanıtlardır. Konuyu genişletmek gerektiğinde açık kaynaklar ve yeni örnekler kullanılabilir. Başka konuşmalardaki bilgiler, kullanıcının ilk talimatı uyarınca bu çalışmaya taşınmaz.

### Başlangıcın sınırları

Tohum, sonucu önceden belirleyen değişmez bir öz veya bütün ayrıntıları tamamlanmış bir proje şartnamesi değildir. İlk varsayım yanlış çıkabilir; soru daralabilir veya genişleyebilir. Değişiklik, ilk kaydı sessizce silmek yerine gerekçesi ve tarihiyle ilişkilendirilir. Böylece başlangıç korunurken öğrenmeye açık kalır.

Başlangıç protokolünün tamamlanması için bütün soruların cevaplanmış olması gerekmez. İncelenecek nesnenin, çalışma düzeyinin, kullanılabilir dayanakların ve açık meselelerin anlaşılır olması yeterlidir. Belirlenmemiş bir hedef sistem üzerinde işlem yapılmış veya bir tasarım doğrulanmış sayılmaz.

### Masaüstünde uygulama

**Girdi:** Başlangıç ihtiyacı, mevcut sorular, erişilebilir kaynaklar ve varsa incelenecek sistemin bilgileri.

1. Çalışma klasörünün bir kopyasını açın ve `calisma/00_TOHUM_KAYDI.md` dosyasında çalışmanın adını, tarihini ve sorumlusunu yazın. Çalışma düzeyini seçin: kavramsal inceleme, somut sistem tasarımı veya somut sistem üzerinde doğrulama. Bu düzey, sonraki bölümlerin hangi dayanaklarla tamamlanabileceğini belirler.

2. İhtiyacı bir paragrafta açıklayın. Korunan başlangıç sorularını ve bu uygulamada cevaplanacak ek soruları kaydedin. Gerçek bir sistem seçilmediyse bunu belirtin; örnek gerekiyorsa belgedeki varsayımsal tiyatro sistemini kullanın. İlk başarı beklentisini de kısaca yazın; gerekçesini ve yeterliliğini 5'te inceleyeceksiniz.

3. Kapsama giren ve dışında kalan işleri yazın. Gerçek sistemle çalışılacaksa hedef ortamı ve mevcut işlem yetkisini belirtin. Zaten verilmiş yetkiyi yeniden onaya dönüştürmeyin; kapsamı belirsiz bir değişikliği yetkiliymiş gibi yürütmeyin. Çalışma yalnız incelemeyse dosya okuma ve kayıt üretme kapsamında ilerleyin.

4. Eldeki kaynakları ve gözlemleri, varsayımları ve bilinmeyenleri ayrı kaydedin. Bilinmeyen alanlara 'Belirlenmedi' yazın. Gerekçeli biçimde kapsam dışında bırakılan veya seçilen çalışma düzeyinde gerekmeyen bir alanı 'Kapsam dışı' ya da 'Uygulanmaz' olarak belirtin; bunları bilinmeyenle karıştırmayın. Her açık soruyu, onu ele alacak protokolle ilişkilendirin. Bu çalışma dışındaki konuşmaları kaynak olarak eklemeyin.

5. Başlangıcın yeterliliğini değerlendirin: başka bir kişi neyin neden incelendiğini anlayabiliyor mu? İlk sürümü kaydedin. Daha sonra soru veya kapsam değişirse tarihi ve gerekçesiyle başlangıç kaydına ekleyin.

### Üretilecek kayıt

`calisma/00_TOHUM_KAYDI.md`: ihtiyaç, sorular, çalışma düzeyi, kapsam, kaynaklar, varsayımlar, açık meseleler ve sorumluluk bilgileri.

### Tamamlanma ölçütü

İnceleme nesnesi ve çalışma düzeyi anlaşılırdır; hangi bilgiyle başlandığı ve nelerin bilinmediği görünürdür. İlerlemeyi engelleyen belirsizlik varsa, etkilediği işlem belirtilir. Kavramsal inceleme için gerçek veri tabanı kurulması gerekmez.

### Sonraki adıma geçiş

Bu başlangıç kaydı, 1–5'in ortak girdisidir. Varlık Protokolü'ne geçin; sonraki bölüm başlangıç varsayımını değiştirirse 0'ı gerekçesiyle güncelleyin.

## 1 Varlık Protokolü

**Korunan başlangıç sorusu:**

> Nedir? Onu o yapan nelerdir? Neler değildir?

### Alanı kuran ayrımlar

Veri tabanı, belirli anlamlar ve ilişkiler altında düzenlenmiş, kullanılmak üzere yönetilen veri bütünüdür. Veri tabanı yönetim sistemi, bu bütünün tanımlanmasını, sorgulanmasını, değiştirilmesini ve yönetilmesini sağlayan yazılımdır. Veri tabanı mühendisliği ise bu düzenin tasarlanması, gerçekleştirilmesi, işletilmesi, sınanması ve değiştirilmesi sırasında uygulanan mühendislik pratiğidir. Bu üçü birbirini tamamlar; aynı şeyi adlandırmaz.

Alanın nesnesi yalnız tekil kayıtlar değildir. Kayıtların kimliği, birbirleriyle ilişkileri, geçerli sayıldıkları koşullar, erişim biçimleri ve birbirini izleyen durumları da bu nesneye dâhildir. Bir tiyatro sisteminde B12 koltuğunun ayrıldığını belirten kayıt, ancak hangi salonun hangi gösterisine ait olduğu, kimin adına tutulduğu ve hâlâ etkin olup olmadığı bilindiğinde kullanılabilir bir anlam kazanır.

Veri tabanı mühendisliği, alanın anlamını kendiliğinden icat etmez. Alan uzmanlarıyla birlikte önemli ayrımları belirginleştirir ve bunları teknik olarak temsil edilebilir hâle getirir. Bir rezervasyonun iptal edilmiş olmasıyla geçmişte hiç var olmamış olması aynı durum değildir. Bu farkı korumak, yalnız sözcük seçimi değil, modelin nasıl kurulacağına ilişkin bir karardır.

Geçerli durumlarla geçersiz durumların ayrılması da alanın kurucu işidir. Yazılabilen her veri kabul edilebilir değildir. Bir gösterinin aynı koltuğu üzerinde iki etkin rezervasyon bulunmaması gibi kurallar, kabul edilecek durumların sınırını belirler. Tek tek makul görünen değişikliklerin birlikte ve eşzamanlı yürütüldüklerinde de bu sınırı koruması gerekir.

~~~text
  UC AD  birbirini tamamlar; ayni seyi adlandirmaz
    veri tabani            belirli anlamlar ve iliskiler altinda
                           duzenlenmis, kullanilmak uzere yonetilen
                           veri butunu
    veri tabani yonetim    bu butunun tanimlanmasini, sorgulanmasini,
    sistemi                degistirilmesini ve yonetilmesini saglayan
                           yazilim
    veri tabani            bu duzenin tasarlanmasi, gerceklestirilmesi,
    muhendisligi           isletilmesi, sinanmasi ve degistirilmesi
                           sirasinda uygulanan muhendislik pratigi

  ALANIN NESNESI  yalniz tekil kayitlar degil
    kayitlarin kimligi . birbirleriyle iliskileri . gecerli
    sayildiklari kosullar . erisim bicimleri . birbirini izleyen
    durumlari

    B12 koltugunun ayrildigini belirten kayit
      ancak su bilindiginde kullanilabilir bir anlam kazanir:
        hangi salonun hangi gosterisine ait oldugu
        kimin adina tutuldugu
        hala etkin olup olmadigi

  AYRIMLAR
    rezervasyonun iptal edilmis olmasi  =/=  gecmiste hic var olmamis
                                             olmasi
    ayni gosterinin ayni koltugunda iki etkin rezervasyon  -->  kabul
    edilecek durumlarin sinirinin disinda
    yazilabilen her veri kabul edilebilir degildir
    degisiklik A  tek basina makul
    degisiklik B  tek basina makul
    A ve B birlikte ve eszamanli  -->  sinir yine korunmali
~~~

*Çizim 3 — Varlık: üç ad; alanın nesnesi ve B12 kaydı; iptal edilmiş olmak ile hiç var olmamış olmak; geçerli ve geçersiz durum.*

Mantıksal anlamla fiziksel yerleşim arasındaki ayrım, sistemin iç düzeni değişirken dışarıya sunduğu anlamın korunmasını sağlar. Codd'un 1970 tarihli ilişkisel model çalışmasında, kullanıcıların ve uygulamaların verinin makinedeki iç temsiline bağımlılığını azaltma hedefi açıkça yer alır. Bu düşünce, bir kaydın nerede tutulduğuyla neyi temsil ettiğini ayrı tasarım soruları olarak ele almaya imkân verir. [1]

Mühendisliğin kapsamı hem veri tabanı motorunun geliştirilmesini hem mevcut motorlarla bir ürünün veya kurumun veri düzeninin kurulmasını içerir. İlkinde depolama, sorgu yürütme, eşzamanlılık ve kurtarma mekanizmaları tasarlanabilir. İkincisinde model, erişim, değişim, performans ve işletim düzeni kurulur. Ortak sorumluluk, hangi koşullarda hangi anlamın ve güvencenin korunduğunu açıklayabilmektir.

~~~text
                  kullanicilar ve uygulamalar
                              |
                              v
    +--------------------------------------------------------+
    | disariya sunulan anlam       bir kaydin neyi temsil    |
    |                              ettigi                    |
    +--------------------------------------------------------+
      - - - - -  bagimliligi azaltma hedefi  (Codd 1970) [1]
    +--------------------------------------------------------+
    | verinin makinedeki ic        bir kaydin nerede         |
    | temsili                      tutuldugu                 |
    +--------------------------------------------------------+
    ic duzen degisirken disariya sunulan anlam korunur
    nerede tutuldugu ile neyi temsil ettigi:  ayri tasarim sorulari

  MUHENDISLIGIN KAPSAMI
    veri tabani motorunun          mevcut motorlarla bir urunun veya
    gelistirilmesi                 kurumun veri duzeninin kurulmasi
      depolama . sorgu yurutme .     model . erisim . degisim .
      eszamanlilik . kurtarma        performans . isletim
    ortak sorumluluk:  hangi kosullarda hangi anlamin ve guvencenin
    korundugunu aciklayabilmek
~~~

*Çizim 4 — Varlık: mantıksal anlam ile fiziksel yerleşim; mühendisliğin kapsamı.*

### Köken, taşıyıcı ve sorumlu özne

Pratik köken, bir kaydın onu oluşturan anın ötesinde kullanılmasına duyulan ihtiyaçta aranabilir. Olmuş, ölçülmüş, kararlaştırılmış veya taahhüt edilmiş bir şeyin daha sonra bulunması, başka bilgilerle ilişkilendirilmesi ve gerektiğinde anlamı korunarak değiştirilmesi istenir. Bilgisayar bu ihtiyacın belirli ölçek ve yöntemlerle karşılanmasını mümkün kılar; ihtiyacın niçin doğduğunu tek başına açıklamaz.

Buradaki köken incelemesi, varlığın, mekânın veya zamanın neden var olduğunu açıklamaz. Belirli varlıkların nasıl temsil edildiğini, hangi ilişkiler içinde tutulduğunu ve hangi zaman düzeninde kullanıldığını ele alır. Teknik açıklamanın kapsamı ile felsefi köken sorusu birbirine eşitlenmez.

Teknik taşıyıcı, veriler ve modellerle birlikte çalışan veri tabanı yazılımı, uygulamalar ve donanım düzenidir. Bu işleyişin açıklamalarından biri durum makinesi modelidir: mevcut durum üzerinde bir istek değerlendirilir, kurallara göre bir sonuç ve gerektiğinde yeni bir durum oluşur. Okuma sırasında kayıtlı durum değişmeyebilir; geçersiz istek reddedilebilir. Lamport'un dağıtık sistemler açıklamasında da durum makinesi yaklaşımı temel bir yere sahiptir. [2]

Durum makinesi, disiplinin bütün kimliği değildir; birçok yazılımın davranışı bu biçimde modellenebilir. Veri tabanı mühendisliğinin özel yükü, kayıtların kimliğini, ilişkilerini, sorgulanabilirliğini ve geçerli değişimlerini kullanım süresi boyunca yönetmektir. Turing makinesi ise daha genel bir hesaplanabilirlik modelidir. Bir işlemin hesaplanabilir olması, hangi veri anlamına, erişim yetkisine veya kullanım gayesine hizmet etmesi gerektiğini belirlemez. [3]

~~~text
  PRATIK KOKEN
    bir kaydin, onu olusturan anin otesinde kullanilmasina duyulan
    ihtiyac:  daha sonra bulunmasi . baska bilgilerle
              iliskilendirilmesi . gerektiginde anlami korunarak
              degistirilmesi
    bilgisayar  -->   belirli olcek ve yontemlerle karsilanmasini
                      mumkun kilar
    bilgisayar  -/->  ihtiyacin nicin dogdugunu tek basina aciklar
    teknik aciklamanin kapsami  =/=  felsefi koken sorusu

  TEKNIK TASIYICI
    veriler ve modellerle birlikte calisan veri tabani yazilimi,
    uygulamalar ve donanim duzeni

  ISLEYISIN ACIKLAMALARINDAN BIRI: DURUM MAKINESI  [2]
    mevcut durum ---+
                    +-->  istek degerlendirilir  -->  sonuc
    istek ----------+     kurallara gore         -->  gerektiginde
                                                      yeni durum
    okuma           kayitli durum degismeyebilir
    gecersiz istek  reddedilebilir

  SINIRLAR
    durum makinesi    bircok yazilimin davranisi bu bicimde
                      modellenebilir; disiplinin butun kimligi degil
    ozel yuk          kayitlarin kimligini, iliskilerini,
                      sorgulanabilirligini ve gecerli degisimlerini
                      kullanim suresi boyunca yonetmek
    Turing makinesi   daha genel bir hesaplanabilirlik modeli  [3]
    hesaplanabilir olmasi  -/->  hangi veri anlamina, erisim yetkisine
                                 veya kullanim gayesine hizmet etmesi
                                 gerektigi
~~~

*Çizim 5 — Varlık: pratik köken; teknik taşıyıcı; durum makinesi modeli; sınırlar.*

Kurucu ve sorumlu özneler, hangi ayrımların anlamlı olduğuna, hangi değişikliklerin kabul edileceğine ve hangi sonuçların yeterli sayılacağına ilişkin kararları veren insanlardır. Bu kararlar mühendisler, alan uzmanları, kullanıcılar ve yetki sahipleri arasında dağılabilir. Veri tabanı mühendisi, beklentileri uygulanabilir ve sınanabilir teknik davranışa dönüştüren; çelişkileri ve sınırları görünür kılan mesleki öznelerden biridir.

Makineyi beş boyutu birlikte somutlaştıran düzenek anlamında ele aldığımızda, insanlar, kurallar, kayıtlar ve teknik araçlardan oluşan bir bütün görünür. Bu bütün için sosyoteknik sistem ifadesi kullanılabilir. İfade, insanlarla aygıtların aynı tür varlıklar olduğunu söylemez; sonucun aralarındaki örgütlenme içinde oluştuğunu belirtir. Bir şeyi taşımak, işletmek, anlamlandırmak ve gayesini belirlemek farklı ilişkilerdir.

~~~text
  KURUCU VE SORUMLU OZNELER  kararlari veren insanlar
    hangi ayrimlar anlamli?
    hangi degisiklikler kabul edilecek?
    hangi sonuclar yeterli sayilacak?
    kararlar dagilabilir:  muhendisler . alan uzmanlari .
                           kullanicilar . yetki sahipleri
    veri tabani muhendisi  beklentileri uygulanabilir ve sinanabilir
                           teknik davranisa donusturen; celiskileri ve
                           sinirlari gorunur kilan mesleki oznelerden
                           biri

  SOSYOTEKNIK SISTEM  bes boyutu birlikte somutlastiran duzenek
    +--------------------------------------------------------------+
    |   insanlar       kurallar       kayitlar       teknik araclar |
    +--------------------------------------------------------------+
    sonuc aralarindaki orgutlenme icinde olusur
    ifade  -/->  insanlar ve aygitlar ayni tur varliklardir

  FARKLI ILISKILER
    tasimak =/= isletmek =/= anlamlandirmak =/= gayesini belirlemek
~~~

*Çizim 6 — Varlık: kurucu ve sorumlu özneler; sosyoteknik sistem; farklı ilişkiler.*

### Kimliğin sınırları

Veri tabanı mühendisliği, SQL bilgisiyle veya belirli bir ürünü kullanabilmekle özdeş değildir. Yazılım mühendisliği, veri mühendisliği, veri tabanı yöneticiliği, veri bilimi ve veri yönetişimiyle kesişir. Bu alanların sınırları evrensel görev duvarları olarak alınmamalıdır. Aynı kişi farklı sorumluluklar üstlenebilir; ayırt edici olan, o anda hangi problemin ve güvencenin sorumluluğunu aldığıdır.

Alan yalnız ilişkisel tablolarla sınırlı değildir. Farklı veri modelleri, temel mühendislik sorumluluğunu ortadan kaldırmaz. Aynı şekilde tek bir disk, veri dosyası, sunucu, dil veya soyut model, kullanım bağlamı verilmeden bu alanın bütün kimliğini açıklayamaz.

Kayıtların kendi aralarında tutarlı olması, dünyayı doğru temsil ettiklerini kanıtlamaz. Yanlış bir koltuk haritası kusursuz biçimde saklanabilir ve işlenebilir. Ayrıca insanın bu düzenin kurucu ve sorumlu öznesi olması, insanın bütünüyle bir veri tabanı veya hesaplama makinesi olduğu sonucunu vermez. Mühendislik, insan eyleminin belirli bir bölümünü biçimselleştirir; insanın bütün varlığını açıklayan bir kuram değildir.

### Masaüstünde uygulama

**Girdi:** 0'ın başlangıç kaydı, alan tanımları ve varsa model, şema veya örnek kayıtlar.

1. İncelenen sistemi veya kavramı tek paragrafta tanımlayın. Veri bütününü, onu yöneten yazılımı ve bunlar üzerindeki mühendislik sorumluluğunu ayrı ifade edin. Ürün adı, sistem tanımının yerine geçmesin.

2. Temel kavramları, kimlikleri ve ilişkileri yazın. Aynı sözcüğün farklı kapsamlarını ayırın: 'koltuk', 'belirli gösterideki koltuk' ve 'etkin rezervasyon' farklı anlamlar taşır. Her önemli anlamın kaynağını veya karar sorumlusunu belirtin.

3. Geçerli ve geçersiz durumları belirleyen kuralları kaydedin. Her önemli kural için kısa bir geçerli örnek ve sınırı gösteren bir karşı örnek verin. Örnek veriler gerçek sistem gözlemi gibi sunulmasın.

4. Teknik taşıyıcıyı, davranışı açıklamak için kullanılan soyut modeli ve anlam veya karar sorumluluğu olan rolleri ayrı yazın. Alanın ne olmadığını ve henüz çözülmemiş anlam sorunlarını kayda ekleyin.

### Üretilecek kayıt

`calisma/01_VARLIK_KAYDI.md`: tanım, kavramlar, kimlikler, ilişkiler, geçerlilik kuralları, karşı örnekler, teknik taşıyıcı ve sorumlu roller.

### Tamamlanma ölçütü

Okuyucu kayıtların neyi temsil ettiğini, hangi durumda geçerli olduğunu ve anlam sorunu olduğunda hangi kaynağa veya kişiye başvurulacağını anlayabilir. Sistem tutarlılığı ile dünyaya ilişkin doğruluk birbirine karıştırılmaz.

### Sonraki adıma geçiş

Tanımlanan nesneleri ve kuralları Mekan Protokolü'ne taşıyın. Yer veya yetki incelemesi yeni bir anlam ayrımı gerektirirse bu kayda dönün.

## 2 Mekan Protokolü

**Korunan başlangıç sorusu:**

> Nerededir? Bu yeri, oraya has bir yer yapan nelerdir? Neler değildir?

### Fiziksel, mantıksal ve kurumsal yer

Veri tabanı mühendisliğinin fiziksel karşılığı işlemci, bellek, depolama ve gerektiğinde ağ üzerinde çalışan sistemlerdir. Tek bir yerleşim biçimine bağlı değildir. SQLite uygulamanın kendi süreci içinde çalışabilir; ayrı bir veri tabanı sunucusu gerektirmez. Spanner ise küresel ölçekte dağıtılmış bir veri tabanı tasarımına örnektir. Bu iki örnek, alanın tek bir makine boyutuna veya yerleşime indirgenemeyeceğini gösterir. [4] [5]

Mantıksal yer, kayıtların hangi kapsam ve ilişkiler içinde bulunduğuyla ilgilidir. Gösteri, koltuk ve rezervasyon arasındaki bağlar; aynı numaranın farklı salonlarda ne anlama geldiği; bir kurumun verilerinin başka bir kurumun verilerinden nasıl ayrıldığı bu düzeyde belirlenir. Mantıksal olarak bir arada ele alınan veriler, fiziksel olarak farklı yerlerde bulunabilir.

Sistemin işleyişi içindeki yer, uygulama taleplerinin başka işlemlerin de dayanacağı veri durumlarına dönüştüğü sınırdır. Kullanıcının bir düğmeye basmasıyla sistemin rezervasyonu kabul etmesi aynı olay değildir. Veri tabanı mühendisliği, kabul edilen sonucun hangi kurallarla ve hangi yetki altında oluştuğunun sorumluluğuna katılır.

Kurumsal yer, verinin anlamını bilenlerle onu kullananlar ve sistemi işletenler arasındaki ilişkide bulunur. Alan uzmanı geçerli durumu açıklar, uygulama ekibi iş akışını kurar, altyapı ekibi çalışma ortamını sağlar. Bu roller ayrı kişilerde bulunabileceği gibi aynı kişide de birleşebilir. Veri tabanı mühendisliği, bu ilişkilerin veri bakımından birbirini tutmasını sağlar.

~~~text
  FIZIKSEL
    islemci . bellek . depolama . gerektiginde ag
    tek bir yerlesim bicimine bagli degil:
      SQLite    uygulamanin kendi sureci icinde calisabilir; ayri bir
                veri tabani sunucusu gerektirmez  [4]
      Spanner   kuresel olcekte dagitilmis tasarim  [5]

  MANTIKSAL
    kayitlarin hangi kapsam ve iliskiler icinde bulundugu
      gosteri --- koltuk --- rezervasyon
      ayni numaranin farkli salonlarda ne anlama geldigi
      bir kurumun verilerinin baska bir kurumunkinden nasil ayrildigi
    mantiksal olarak bir arada  -/->  fiziksel olarak ayni yerde

  SISTEMIN ISLEYISI ICINDE
    uygulama talepleri  ---|--->  baska islemlerin de dayanacagi veri
                           |      durumlari
                         sinir
    dugmeye basmak  =/=  sistemin rezervasyonu kabul etmesi
    veri tabani muhendisligi:  kabul edilen sonucun hangi kurallarla ve
    hangi yetki altinda olustugunun sorumluluguna katilir

  KURUMSAL
    alan uzmani       gecerli durumu aciklar
    uygulama ekibi    is akisini kurar
    altyapi ekibi     calisma ortamini saglar
    roller ayri kisilerde de, ayni kiside de bulunabilir
    veri tabani muhendisligi:  bu iliskilerin veri bakimindan birbirini
    tutmasini saglar
~~~

*Çizim 7 — Mekan: fiziksel, mantıksal, işleyiş içindeki ve kurumsal yer.*

### Bilginin bulunduğu yer ve kararın verildiği yer

Bu konumu özgün yapan, anlam, yetki ve maddi sınırların aynı karar içinde buluşmasıdır. İş alanı aynı koltuğun iki kişiye ayrılmamasını isterken uygulama hızlı yanıt bekleyebilir; donanımın kapasitesi sınırlıdır ve ağ kesilebilir. Sistemin bazı kullanıcıları yalnız okuyabilir, bazıları değişiklik yapabilir. Yer, bu ilişkilerden bağımsız bir depolama noktası olarak ele alınamaz.

Varsayımsal tiyatro sisteminde iki kullanıcının ekranında aynı anda B12 koltuğu boş görünebilir. Bu görüntü, koltuğun ikisine de ayrıldığı anlamına gelmez. Rezervasyonu kabul etmeye yetkili işlem yolu ayrıca tanımlanır. Bu yol tek bir makinede veya birden fazla makinenin koordinasyonunda gerçekleşebilir; belirleyici olan görüntülenen bilgiyle kabul edilmiş taahhüt arasındaki sınırdır.

Doluluk raporu için kullanılan bir kopyanın kısa süre geriden gelmesine izin verdiğimizi varsayabiliriz. Aynı kopyaya son koltuğun tahsisinde karar yetkisi vermeyebiliriz. Böylece verinin nerede bulunduğu kadar hangi veriye hangi karar için dayanılabileceği de tasarlanmış olur. Güncellik ve yetki gereksinimleri kullanımın amacına göre ayrılır.

Bazı kayıtlar bir olayı temsil eder; bazı kayıtların kabulü ise tanımlı bir düzen içinde taahhüdün kurulmasına katılır. Taraflar yetkili sistemin kabul ettiği kaydın rezervasyonu kuracağı konusunda anlaşmışsa, kaydın oluşturulması yalnız geçmişte olmuş bir şeyi anlatmaz. Bu varsayım altında rezervasyonun oluşmasının bir parçasıdır. Sistem fiziksel koltuğu yaratmaz; hangi işlemin geçerli sayılacağına ilişkin insan ilişkileri ve kurallar içinde sonuç doğurur.

~~~text
  GORUNTULENEN BILGI       |    KABUL EDILMIS TAAHHUT
                           |
    kullanici 1 ekrani     |
      "B12 bos"  --------------->  +-----------------------------+
                           |       | rezervasyonu kabul etmeye   |
    kullanici 2 ekrani     |       | yetkili islem yolu          |
      "B12 bos"  --------------->  | (ayrica tanimlanir)         |
                           |       +-----------------------------+
    bu goruntu  -/->  koltugun ikisine de ayrildigi
    yol tek makinede de, birden fazla makinenin koordinasyonunda da
    gerceklesebilir; belirleyici olan aradaki sinirdir

  HANGI VERIYE HANGI KARAR ICIN DAYANILIR  varsayim
    doluluk raporu         kullanilan kopyanin kisa sure geriden
                           gelmesine izin verilebilir
    son koltugun tahsisi   ayni kopyaya karar yetkisi verilmeyebilir
    guncellik ve yetki gereksinimleri kullanimin amacina gore ayrilir

  KAYIT
    bazi kayitlar             bir olayi temsil eder
    bazi kayitlarin kabulu    tanimli bir duzen icinde taahhudun
                              kurulmasina katilir (taraflar boyle
                              anlasmissa)
    sistem  -/->  fiziksel koltugu yaratir
~~~

*Çizim 8 — Mekan: görüntülenen bilgi ile kabul edilmiş taahhüt; hangi veriye hangi karar için dayanılır; olayı temsil eden kayıt ile taahhüde katılan kayıt.*

### Taşıyıcının sürekliliği ve konumun sınırları

Teknik taşıyıcıyı tek bir kutuyla özdeşleştirmek gerekmez. PostgreSQL örneğinde veri tabanı dosyalarını yöneten sunucu süreçleriyle işlem isteyen istemci uygulamaları ayrıdır ve farklı bilgisayarlarda bulunabilir. Sistemin konumu, parçalarının etkileşimiyle birlikte değerlendirilir. [6]

Fiziksel taşıyıcı değişirken hizmetin işlevsel kimliği korunabilir. Veri, kurallar ve kullanıcıya verilen güvenceler uygun biçimde taşınırsa hizmet başka donanımda sürdürülebilir. Bu durumda aynı hizmet olma ölçütü yalnız cihazın maddi kimliğine dayanmaz.

Veri tabanı mühendisliğinin yeri yalnız arka uç, bulut veya veri merkezi değildir. Küçük ve yerel bir sistemin tek bir kaydı bile önemli sonuçlar doğurabilir. Mimari çizimdeki veri tabanı kutusu, tekrar deneme davranışı, erişim yetkisi ve işletim süreçleri gibi ilişkilerin tamamını içermez. Veri hacmi de mühendislik ihtiyacının tek ölçüsü değildir.

Tek doğruluk kaynağı düşüncesi, bütün gerçekliğin tek bir veri tabanında bulunması anlamına gelmemelidir. Farklı bilgiler için farklı yetkili kaynaklar olabilir. Hangi konuda hangi kaynağın esas alınacağı ve çelişkilerin nasıl çözüleceği açıklanmalıdır. Teknik yerleşim, bu yetki kararlarının yerine geçmez.

### Masaüstünde uygulama

**Girdi:** 0'ın kapsamı, 1'in nesne ve kural tanımları, varsa bileşen bilgileri ve erişim düzeni.

1. Verinin üretildiği, tutulduğu, okunduğu ve değiştirildiği yerleri belirleyin. Fiziksel yerleşimi, mantıksal kapsamı ve kurumsal karar yetkisini ayrı açıklayın. Bilinmeyen sunucu veya hizmet konumlarını tahmin ederek doldurmayın.

2. Önemli bir işlemi seçin ve isteğin geçtiği parçaları sırasıyla yazın. İstemci, uygulama, veri tabanı ve varsa kopya veya dış hizmetin bu işteki rolünü belirtin. Henüz seçilmemiş bileşeni tasarım seçeneği olarak işaretleyin.

3. Hangi noktada bağlayıcı kabul oluştuğunu ve hangi ekranın, raporun veya kopyanın yalnız bilgi sunduğunu açıklayın. Her önemli veri konusu için esas alınacak kaynağı, değiştirme yetkisini ve çelişki çözme kuralını yazın.

4. Teknik sınırın dışında kalan bağımlılıkları ve sorumluları kaydedin. Bir kaydın başka donanıma taşınması hâlinde korunması gereken anlamı ve güvenceleri belirtin; gerekmedikçe ayrıntılı bir dağıtım mimarisi tasarlamayın.

### Üretilecek kayıt

`calisma/02_MEKAN_KAYDI.md`: fiziksel ve mantıksal yerler, bileşenler, veri akışı, karar yetkisi, esas alınacak kaynaklar ve sistem sınırı.

### Tamamlanma ölçütü

Verinin bulunduğu yerle bir işlemi kabul etmeye yetkili yer ayrılabilir. Önemli işlemde hangi kaynağa hangi karar için dayanıldığı ve belirsiz kalan sınırlar anlaşılırdır.

### Sonraki adıma geçiş

Seçilen işlem yolunu, kuralları ve yetki sınırlarını Usül Protokolü'ne aktarın. Mekan kararı değişirse bundan etkilenen işlem ve zaman kayıtlarını da güncelleyin.

## 3 Usül Protokolü

**Korunan başlangıç sorusu:**

> Nasıl işler yapar? Bu yaptıklarını, ona has yapan nelerdir? Neler değildir?

### Beklentiden sınanabilir kurala

Veri tabanı mühendisliği, belirsiz beklentileri açık kurallara, kuralları çalışan mekanizmalara ve mekanizmaları sınanabilir güvencelere dönüştürerek işler. Sistemin düzgün çalışmasının ne anlama geldiği belirlenir. Bir işlemin ne zaman kabul edilmiş sayılacağı, aynı isteğin yeniden gelmesi hâlinde ne yapılacağı, kimlerin hangi kayıtlara erişeceği ve arıza sonrasında hangi durumun geri kazanılacağı açıklığa kavuşturulur.

Bu usulde önce korunacak anlam ve sınırlar belirlenir; ardından uygun mekanizma seçilir. Başlangıçta açıklanmayan bir beklentinin tasarım tarafından kendiliğinden karşılandığı varsayılamaz. Mühendis, seçimin hangi koşullarda işe yaradığını ve hangi koşullarda yetersiz kaldığını görünür kılar.

Makine usulü koşullar ve izin verilen işlemler olarak taşır. Bir rezervasyon belirli koşullarda oluşturulabilir, iptal edilebilir veya değiştirilebilir. Kuralın belgede yazılmasıyla sistem davranışında uygulanması farklıdır. Ayrıca bir usulün otomatik ve hatasız uygulanması, o usulün doğru seçildiğini kanıtlamaz; teknik işleyişle iş bakımından uygunluk ayrı ayrı değerlendirilir.

~~~text
  ISLEYIS
    belirsiz      -->  acik       -->  calisan       -->  sinanabilir
    beklentiler        kurallar        mekanizmalar       guvenceler

  ACIKLIGA KAVUSTURULUR
    bir islem ne zaman kabul edilmis sayilacak?
    ayni istek yeniden gelirse ne yapilacak?
    kimler hangi kayitlara erisecek?
    arizadan sonra hangi durum geri kazanilacak?

  SIRA  once korunacak anlam ve sinirlar, ardindan uygun mekanizma
    baslangicta aciklanmayan bir beklenti
      -/->  tasarim tarafindan kendiliginden karsilanir
    muhendis:  secimin hangi kosullarda ise yaradigini ve hangi
    kosullarda yetersiz kaldigini gorunur kilar
    makine usulu tasir:  kosullar ve izin verilen islemler olarak

  AYRI DEGERLENDIRILIR
    kuralin belgede yazilmasi     =/=  sistem davranisinda uygulanmasi
    usulun otomatik ve hatasiz    -/-> o usulun dogru secildigi
    uygulanmasi
    teknik isleyis                =/=  is bakimindan uygunluk
~~~

*Çizim 9 — Usül: beklentiden sınanabilir güvenceye; açıklığa kavuşturulan sorular; ayrı değerlendirilenler.*

### Modelleme ve geçerli değişim

Tiyatro örneğinde, bir gösterinin bir koltuğu için aynı anda en fazla bir etkin rezervasyon bulunması kuralını kabul edelim. Bir tasarım seçeneği, etkin rezervasyonları ayrı bir tabloda tutup gösteri ve koltuk kimliği çiftini benzersiz kılmaktır. İptal edilmiş rezervasyonlar geçmişte tutulacaksa, onların durumu etkinlik kuralıyla karıştırılmaz. Bütün geçmişe düşünmeden uygulanan aynı benzersizlik kuralı, iptal edilen koltuğun yeniden ayrılmasını engelleyebilir.

Benzersizlik, yabancı anahtar ve denetim kısıtları, tanımlanan kurallara aykırı verilerin kabul edilmesini engellemekte kullanılabilir. Hangi kısıtın gerektiği ve hangi kapsamda uygulanacağı modelleme kararına bağlıdır. Erişim düzeni de aynı açıklıkla kurulur: bir kaydı görmek, iptal etmek ve geçmişini değiştirmek farklı yetkilerdir. [7]

İki kullanıcı aynı koltuğu ayırtmak istediğinde ikisi de önce boş yanıtını alabilir. Sonraki kayıt işlemlerinin nasıl koordine edileceği belirlenmemişse ilk kontrol yeterli değildir. Varsayımsal etkin rezervasyon tablosu ve benzersizlik kuralı altında, aynı gösteri ve koltuk çiftinin iki kez kabul edilmesi engellenir. Çakışan istek için reddetme veya başka bir sonuca yönlendirme davranışı ayrıca tanımlanır.

~~~text
  BIR TASARIM SECENEGI  varsayimsal tiyatro ornegi
  kural:  bir gosterinin bir koltugu icin ayni anda en fazla bir etkin
          rezervasyon

    etkin rezervasyonlar          iptal edilmis rezervasyonlar
    +-----------+-----------+     gecmiste tutulacaksa durumlari
    |  gosteri  |  koltuk   |     etkinlik kuraliyla karistirilmaz
    +-----------+-----------+
    gosteri ve koltuk kimligi cifti benzersiz

    ayni benzersizlik kurali butun gecmise dusunmeden uygulanirsa
      -->  iptal edilen koltugun yeniden ayrilmasini engelleyebilir

  KISITLAR VE ERISIM  [7]
    benzersizlik . yabanci anahtar . denetim kisitlari  -->  kurallara
    aykiri verilerin kabul edilmesini engellemekte kullanilabilir
    hangi kisit, hangi kapsamda:  modelleme kararina bagli
    kaydi gormek  =/=  iptal etmek  =/=  gecmisini degistirmek

  AYNI KOLTUGA IKI ISTEK
    kullanici 1   ilk kontrol: "bos"   ...   kayit islemi  --+
    kullanici 2   ilk kontrol: "bos"   ...   kayit islemi  --+
                                                             |
                                                             v
                        ayni gosteri ve koltuk cifti iki kez kabul
                        edilmez (benzersizlik kurali altinda)
    cakisan istek:  reddetme veya baska bir sonuca yonlendirme
                    (ayrica tanimlanir)
    sonraki kayit islemleri koordine edilmemisse ilk kontrol yeterli
    degildir
~~~

*Çizim 10 — Usül: etkin rezervasyon modeli; kısıtlar ve erişim; aynı koltuğa iki istek.*

Birden fazla değişikliğin birlikte ele alınması gerektiğinde işlem sınırı belirlenir. Atomiklik, ilgili değişikliklerin tamamının veya hiçbirinin etkili olmasını; kalıcılık, kabul edilmiş sonucun seçilen dayanıklılık koşullarında korunmasını ifade eder. Yalıtım, eşzamanlı işlemlerin birbirlerinin değişikliklerini hangi kurallarla görebileceğiyle ilgilidir. Tutarlılık, doğru yazılmış işlemler ve tanımlanmış kısıtlarla geçerli durumların korunmasını gerektirir. İşlemleri bir blokta toplamak bütün eşzamanlılık sorunlarını kendiliğinden çözmez. [8] [9]

### Arıza, belirsizlik ve kurtarma

Rezervasyon kabul edildikten sonra başarı yanıtının ağda kaybolması, kullanıcı açısından belirsizlik yaratır. Yanıt gelmemesi işlemin gerçekleşmediğini kanıtlamaz. Tasarımda aynı isteğin yeniden gönderildiğinin anlaşılmasını sağlayan bir istek kimliği kullanılabilir. Bu kimliğin kapsamı, ne kadar süre tanınacağı ve aynı kimlikle farklı içerik gelirse ne yapılacağı da belirlenir. Amaç, hata olduğunda hangi sonucun geçerli olduğunu anlayabilmektir.

~~~text
    istemci                                           veri tabani
       |                                                   |
       |----- istek (istek kimligi) ---------------------->|
       |                                                   | kabul
       |                x<---------- basari yaniti --------|
       |                agda kaybolur                      |
       |                                                   |
       |  belirsizlik:                                     |
       |  yanit gelmemesi  -/->  islem gerceklesmedi       |
       |                                                   |
       |----- ayni istek yeniden (ayni istek kimligi) ---->|
       |                                   yeniden         |
       |                                   gonderildigi    |
       |                                   anlasilir       |

  ISTEK KIMLIGI  tasarimda kullanilabilir; ayrica belirlenir:
    kapsami . ne kadar sure taninacagi . ayni kimlikle farkli icerik
    gelirse ne yapilacagi
    amac:  hata oldugunda hangi sonucun gecerli oldugunu anlayabilmek
~~~

*Çizim 11 — Usül: kaybolan başarı yanıtı ve istek kimliği.*

Veri tabanı motoru düzeyinde kalıcılık mekanizmaları kurulur. PostgreSQL'in önceden yazılan işlem günlüğü, yani WAL yaklaşımında, veri dosyalarındaki değişikliklerden önce ilgili günlük kayıtları kalıcı depolamaya aktarılır. Çökme sonrasında veri sayfalarına henüz uygulanmamış değişiklikler günlükten yeniden yürütülebilir. [10]

Bir veri tabanı işleminin kapsamı dış dünyadaki bütün sonuçları kendiliğinden kapsamaz. Rezervasyon kaydının kesinleşmesi, e-postanın ulaştığını veya fiziksel koltuğun kullanılabilir olduğunu tek başına garanti etmez. Verilen güvencenin sınırı, işlemin hangi parçaları kapsadığıyla birlikte açıklanmalıdır.

Yedekleme düzeni, kullanılabilir bir sistemin nasıl geri getirileceği sorusundan hareketle değerlendirilir. PostgreSQL'de uygun bir temel yedekle arşivlenmiş WAL kayıtları, kapsanan aralıkta belirli bir ana dönüşü mümkün kılabilir. Bunun için gerekli yedek ve günlüklerin bulunması gerekir. Yedek oluşturulmuş olmasıyla hizmetin geri kazanılmış olması aynı sonuç değildir. [11]

Kurtarma süresinin, eksik kalabilecek verinin ve geri yüklenen sistemin çalışmasının sınanması önemlidir. Google'ın veri bütünlüğü üzerine işletim deneyimleri, önceden denenmiş kurtarma süreçlerinin değerini gösterir. Daha çok kopya bulundurmak bütün kayıp türlerini tek başına çözmez; korunmak istenen arıza durumlarıyla kurtarma yöntemi arasında açık bir ilişki kurulmalıdır. [12]

~~~text
  KALICILIK  PostgreSQL, onceden yazilan islem gunlugu (WAL)  [10]
    once      ilgili gunluk kayitlari  -->  kalici depolama
    ardindan  veri dosyalarindaki degisiklikler
    cokme sonrasinda:  veri sayfalarina henuz uygulanmamis
                       degisiklikler gunlukten yeniden yurutulebilir

  GUVENCENIN SINIRI
    +--------------------------------+
    | veri tabani islemi             |   -/->  e-postanin ulastigi
    |   rezervasyon kaydi kesinlesir |   -/->  fiziksel koltugun
    +--------------------------------+         kullanilabilir oldugu

  GERI GETIRME  PostgreSQL  [11]
    temel yedek
        |    arsivlenmis WAL kayitlari
        v
        +=======+=======+=======+=======+=======>  zaman
        |<-------- kapsanan aralik ------------>|
               bu aralikta belirli bir ana donus
    gerekli yedek ve gunlukler bulunmalidir
    yedek olusturulmus olmasi  =/=  hizmetin geri kazanilmis olmasi

  SINANIR  [12]
    kurtarma suresi . eksik kalabilecek veri . geri yuklenen sistemin
    calismasi
    daha cok kopya  -/->  butun kayip turlerini tek basina cozer
    korunmak istenen ariza durumlari  <-->  kurtarma yontemi
~~~

*Çizim 12 — Usül: WAL ile kalıcılık; güvencenin sınırı; temel yedek ve arşivlenmiş WAL ile geri getirme; sınanan kurtarma.*

### Performans, değişim ve usulün sınırları

Performans çalışması, verinin hangi sorgularla ve hangi iş yükü altında kullanılacağını inceler. İndeksler belirli erişimleri hızlandırabilir, fakat güncel tutulmaları veri değiştirme işlemlerine maliyet getirir. Daha fazla indeks genel bir iyileştirme kuralı değildir. Veriyi bölmek, kopyalamak veya önbelleğe almak da yeni imkânlarla birlikte güncellik, yönlendirme ve işletim sorumlulukları doğurur. [13]

Ölçüm, kullanım koşullarına yaklaştırılır. Boş sistemde tek bir sorgunun hızlı çalışması, gerçek kullanıcı yükü altında yeterli hizmet verildiğini kanıtlamaz. İşlem hızlandırılırken yanıtın anlamı, güncelliği veya güvencesi değişiyorsa bu sonuç açıklanmalıdır.

Değişim sırasında mevcut verinin anlamı korunur. Salon numaralandırması değiştiğinde eski rezervasyonların hangi fiziksel koltuğu gösterdiği anlaşılabilmelidir. Bir alan iki alana ayrıldığında dönüşümün anlamı belirlenmelidir. Eski ve yeni uygulama sürümleri birlikte çalışacaksa bunun koşulları tasarlanır. Şema, sorgu ve yazılım kadar değişiklik planları, erişim kuralları, ölçümler ve kurtarma bilgisi de mühendislik çıktılarıdır.

Bu işleri ayırt eden, birbirini izleyen veri durumları arasındaki anlamlı sürekliliği koruma sorumluluğudur. Yalnız başarılı senaryoda çalışan gösterim, bağımsız bir hız ölçümü veya her mekanizmayı en güçlü ayara getirmek bu sorumluluğu tamamlamaz. Gereksinimle mekanizma arasında gerekçeli ve sınanabilir bir ilişki kurulmalıdır.

### Masaüstünde uygulama

**Girdi:** 1'in geçerlilik kuralları, 2'nin işlem yolu ve yetki sınırları, varsa mevcut uygulama bilgileri.

1. Seçilen işlemi başlangıç koşulundan sonucuna kadar açıklayın. Her önemli kuralı, onu koruyacak mekanizmayla ve gözlenebilir kabul ölçütüyle ilişkilendirin. Birden çok değişiklik birlikte kabul edilecekse işlem sınırını belirtin.

2. İşlem bakımından anlamlı olan çakışma, tekrar deneme veya kesinti durumunu ele alın. Yanıt gelmemesi, işin yapılmadığı anlamına geliyor mu; aynı istek yeniden geldiğinde hangi sonuç geçerli olacak? Veri tabanı işleminin dışında kalan etkileri ayrıca yazın.

3. Çalışma düzeyi tasarım veya kavramsal incelemeyse beklenen davranışı ve gerektiğinde doğrulama planını kaydedin. Sistem doğrulaması seçildiyse, belirlenmiş ortamda yalnız ilgili iddiayı değerlendirmek için gereken denemeyi yürütün. Kullanılan sürümü, koşulları, beklenen sonucu, gözlenen sonucu ve kanıt dosyasını yazın. Yapılmamış denemelere sonuç vermeyin.

4. Kapsamdaki ihtiyaç gerektiriyorsa kurtarma, performans veya veri dönüşümünü aynı kural–mekanizma–kanıt ilişkisiyle ele alın. Yedek bulunduğunu görmekle geri yüklemeyi doğrulamayı ayırın. Yeterli kanıt oluştuktan sonra, kalan somut bir soru yoksa denemeleri genişletmeyin.

### Üretilecek kayıt

`calisma/03_USUL_KAYDI.md`: işlem akışı, kural–mekanizma ilişkisi, kabul ölçütleri, kapsam dışındaki etkiler ve uygulanmışsa doğrulama kanıtları.

### Tamamlanma ölçütü

Her önemli güvencenin nasıl sağlanacağı ve hangi kanıtla değerlendirileceği açıklanmıştır. Tasarım beklentisi ile gözlenen davranış ayrıdır. Doğrulama iddiası yalnız kaydedilen ortam, senaryo ve kapsam için kullanılır.

### Sonraki adıma geçiş

İşlemin sırasını, görünürlük ve tekrar deneme varsayımlarını Zaman Protokolü'ne taşıyın. Zaman incelemesi işlem garantisini değiştirecekse usul kararını yeniden ele alın.

## 4 Zaman Protokolü

**Korunan başlangıç sorusu:**

> Hangi andadır? Bu anı, diğer zamanlardan farklı yapan nelerdir? Neler değildir?

### İşlem ve görünürlük zamanı

Veri tabanı mühendisliğinin zamanı, yalnız kaydın yazıldığı saniyeye indirgenemez. İsteğin gönderilmesi, değişikliğin yapılması, işlemin kesinleşmesi ve kullanıcının sonucu öğrenmesi farklı anlar olabilir. Rezervasyon, kullanıcı başarı mesajını görmeden önce kabul edilmiş olabilir. Bu ayrım, tekrar deneme davranışının neden tasarlanması gerektiğini açıklar.

Değişikliklerin başka işlemler tarafından görülmesi de ayrıca düzenlenir. PostgreSQL'de Read Committed düzeyindeki sıradan bir sorgu, başka işlemlerin sorgu başlangıcından önce kesinleşmiş değişikliklerini görür. Repeatable Read, işlemin ilk ilgili komutunda alınan görünümü korur; işlem kendi yaptığı değişiklikleri de görür. Aynı duvar saati anında çalışan iki işlem, geçerli kurallar altında farklı veri görünümleri kullanabilir. [9]

Makinenin taşıdığı zaman, saat değerleriyle birlikte durum sırasını ve görünürlük sınırlarını da içerir. Dağıtık sistemlerde fiziksel saat değerleriyle olaylar arasındaki nedensel ilişki aynı şey değildir. Lamport'un çalışması, bu ayrımı ve nedensel sırayla uyumlu mantıksal sıralamayı ele alır. Bütün makinelerin tek bir ortak şimdiyi kendiliğinden gördüğü varsayılamaz. [2]

~~~text
  BIR ISLEMIN ANLARI  farkli olabilir
    istegin         degisikligin    islemin         kullanicinin
    gonderilmesi    yapilmasi       kesinlesmesi    sonucu ogrenmesi
         |               |               |                |
    -----+---------------+---------------+----------------+------->
    rezervasyon, kullanici basari mesajini gormeden once kabul
    edilmis olabilir  -->  tekrar deneme davranisi tasarlanmalidir

  GORUNURLUK  PostgreSQL  [9]
    Read Committed    siradan bir sorgu, baska islemlerin sorgu
                      baslangicindan once kesinlesmis degisikliklerini
                      gorur
    Repeatable Read   islemin ilk ilgili komutunda alinan gorunumu
                      korur; islem kendi degisikliklerini de gorur
    ayni duvar saati aninda calisan iki islem  -->  farkli veri
    gorunumleri kullanabilir

  SAAT VE SIRA  Lamport  [2]
    fiziksel saat degerleri  =/=  olaylar arasindaki nedensel iliski
    butun makinelerin tek bir ortak simdiyi kendiliginden gordugu
    varsayilamaz
~~~

*Çizim 13 — Zaman: bir işlemin anları; görünürlük; saat ve nedensel sıra.*

### Olay, geçerlilik ve kayıt zamanı

Bir olayın ne zaman gerçekleştiği, bir bilginin hangi dönem için geçerli olduğu ve sistemin o bilgiyi ne zaman kaydettiği ayrı sorulardır. Bir adres değişikliğinin 1 Mart'tan itibaren geçerli olduğunu, fakat sisteme 5 Mart'ta bildirildiğini düşünelim. 3 Mart'ta geçerli adresi sormakla 3 Mart günü sistemin hangi adresi bildiğini sormak aynı değildir.

Bu ayrım, sonradan öğrenilen bilginin geçmişte zaten biliniyormuş gibi gösterilmesini önler. İş zamanı ve sistem zamanını birlikte tutan iki zamanlı, yani bitemporal modeller bu tür ihtiyaçları karşılayabilir. Db2 belgelerinde uygulama açısından geçerlilik dönemiyle sistem tarafından tutulan tarihçe ayrı boyutlar olarak ele alınır. Bu bir modelleme olanağıdır; her sistemin bütün zaman boyutlarını aynı biçimde tutması gerekmez. [14]

Tarihçe tutmanın anlamı, hangi sorulara cevap verilmek istendiğine bağlıdır. Bir oluşturulma zamanı alanı eklemek, bütün zamansal ayrımları kendiliğinden korumaz. Düzeltmenin önceki kaydı nasıl etkileyeceği ve geçmişte hangi bilginin bilindiğinin sonradan yeniden kurulup kurulamayacağı ayrıca belirlenir.

~~~text
  UC AYRI SORU
    olay ne zaman gerceklesti?
    bilgi hangi donem icin gecerli?
    sistem o bilgiyi ne zaman kaydetti?

  ORNEK  adres degisikligi
            1 Mart            3 Mart            5 Mart
    --------+-----------------+-----------------+---------------->
            |                 |                 |
            gecerlilik        soru gunu         sisteme
            baslar                              bildirildi
            |=============== yeni adres gecerli ==================>
                                                |== sistem biliyor =>

    "3 Mart'ta gecerli adres?"               -->  yeni adres
    "3 Mart gunu sistem hangi adresi
     biliyordu?"                             -->  onceki adres

  IKI ZAMANLI (bitemporal) MODELLER  [14]
    is zamani ve sistem zamani birlikte
    sonradan ogrenilen bilgi gecmiste zaten biliniyormus gibi
    gosterilmez
    bir modelleme olanagi; her sistem butun zaman boyutlarini ayni
    bicimde tutmak zorunda degil
    olusturulma zamani alani eklemek  -/->  butun zamansal ayrimlar
                                            kendiliginden korunur
~~~

*Çizim 14 — Zaman: olay, geçerlilik ve kayıt zamanı; adres örneği; iki zamanlı modeller.*

### Yaşam döngüsü ve tarihsel konum

Veri tabanı mühendisliği, gereksinimler ve kavramlar konuşulurken başlar; ilk tablo oluşturulduğunda başlamış sayılmaz. Kullanım sırasında veri büyür, erişim örüntüsü değişir, yeni kavramlar eklenir, kayıtlar düzeltilir ve altyapı yenilenir. Bugünkü işlem, daha sonraki işlemlere başlangıç durumu bırakır. Programın bir çalıştırması sona erdiğinde ürettiği kaydın etkisi sürmeye devam edebilir.

Bu süreklilik, eski kayıtların yeni düzen içinde anlaşılabilir kalmasını gerektirir. Önceden birikmiş verinin yorumu, onu üreten yazılımdan daha uzun süre önem taşıyabilir. Saklama, arşivleme ve silme de aynı yaşam döngüsüne dâhildir. Kalıcılık, bütün verilerin sonsuza kadar tutulması anlamına gelmez; korunacak anlamın süresi ve kapsamı kullanım ihtiyacına bağlıdır.

Alanın tarihsel konumunda araçlar ve iş yükleri değişirken temel sorumluluk sürer. Codd'un veri bağımsızlığı yaklaşımı, iç yerleşimle dışarıya sunulan anlamın ayrılmasına katkı verir. Güncel araçlar ise bazı sorumlulukların nasıl yerine getirileceğini değiştirir. Amazon RDS, yedekleme ve yazılım güncelleme gibi işletim işlerini yönetirken uygulamaya özgü sorgu ayarlama ve performans sorumluluğunu kullanıcı tarafında bırakır. [1] [15]

Yeni sorgu türleri farklı başarı ölçütleri doğurabilir. pgvector kesin ve yaklaşık en yakın komşu aramasını destekler; yaklaşık indeksler hız karşılığında bazı uygun sonuçları kaçırabilir. Böyle bir kullanımda kabul edilebilir sonuç kalitesi de tasarımın parçası olur. Bu örnekler, araç değişiminin verilen sözlerin ayrıntısını değiştirdiğini, bu sözleri açıklama ve doğrulama sorumluluğunu ortadan kaldırmadığını gösterir. [16]

~~~text
  YASAM DONGUSU
    baslar         gereksinimler ve kavramlar konusulurken
                   (ilk tablo olusturuldugunda baslamis sayilmaz)
       |
       v
    kullanim       veri buyur . erisim oruntusu degisir . yeni
                   kavramlar eklenir . kayitlar duzeltilir . altyapi
                   yenilenir

    bugunku islem  -->  sonraki islemlere baslangic durumu
    programin bir calistirmasi biter  -->  urettigi kaydin etkisi
                                           surebilir
    onceden birikmis verinin yorumu, onu ureten yazilimdan daha uzun
    sure onem tasiyabilir
    donguye dahil:  saklama . arsivleme . silme
    kalicilik  -/->  butun verilerin sonsuza kadar tutulmasi

  ARACLAR DEGISIR, SORUMLULUK SURER
    Codd  [1]         veri bagimsizligi yaklasimi:  ic yerlesim ile
                      disariya sunulan anlamin ayrilmasina katki
    Amazon RDS  [15]  yonetir:  yedekleme, yazilim guncelleme gibi
                      isletim isleri
                      kullanici tarafinda:  uygulamaya ozgu sorgu
                      ayarlama ve performans sorumlulugu
    pgvector  [16]    kesin ve yaklasik en yakin komsu aramasi;
                      yaklasik indeksler hiz karsiliginda bazi uygun
                      sonuclari kacirabilir  -->  kabul edilebilir
                      sonuc kalitesi tasarimin parcasi
    arac degisimi  -->   verilen sozlerin ayrintisini degistirir
    arac degisimi  -/->  sozleri aciklama ve dogrulama sorumlulugunu
                         ortadan kaldirir
~~~

*Çizim 15 — Zaman: yaşam döngüsü; araçlar değişirken süren sorumluluk.*

### Zamansal sınırlar

Bu alanın zamanı yalnız ilk kurulum, arıza müdahalesi veya en yeni teknolojinin kullanıldığı an değildir. En güncel veri her işlem için tek hedef de değildir. Bir rapor kendi içinde tutarlı geçmiş görünümüne ihtiyaç duyabilir; bir rezervasyon işlemi daha sıkı güncellik koşulları gerektirebilir.

Zamanı taşıyan makine, hangi geçmişin anlamlı sayılacağını ve ne kadar korunması gerektiğini kendi teknik işleyişinden çıkarmaz. Bu ihtiyaçlar kullanım amacıyla belirlenir, teknik düzen içinde temsil edilir ve uygulanır. İşlemin sırası, verinin geçerlilik dönemi ve hizmetin yaşam döngüsü arasındaki farkların korunması bu protokolün temel ayrımıdır.

### Masaüstünde uygulama

**Girdi:** 3'ün işlem akışı, 2'nin kaynak ve kopya rolleri, kullanımın geçmiş ve güncellik gereksinimleri.

1. Seçilen işlem için isteğin gelmesi, kabul, görünürlük ve sonucun öğrenilmesi anlarını sıralayın. Sırası bilinen olaylarla kesin saat değeri bilinen olayları ayırın. Gerçek zaman değerleri kullanılıyorsa saat dilimini belirtin.

2. İşin gerektirdiği zaman sorularını yazın: olay ne zaman oldu, bilgi hangi dönemde geçerliydi, sistem bunu ne zaman öğrendi? Gerekmeyen zaman boyutlarını zorunlu veri alanlarına dönüştürmeyin. Belirsiz zamanı kesin bir değerle doldurmayın.

3. Gecikmiş bildirim veya düzeltme içeren bir örnek kurun. 'O tarihte ne geçerliydi?' ve 'O tarihte ne biliyorduk?' sorularının bu sistemde aynı olup olmadığını gösterin. Her okuma türü için gerekli güncelliği veya tutarlı görünümü belirtin.

4. Verinin ve şemanın yaşam döngüsünü açıklayın. Saklama, düzeltme, arşivleme, silme ve sürüm değişikliğinin hangi süreye veya olaya bağlı olduğunu kaydedin. Süre belirlenmemişse bunu açık mesele yapın; kendiliğinden sayısal bir süre atamayın.

### Üretilecek kayıt

`calisma/04_ZAMAN_KAYDI.md`: işlem sırası, zaman anlamları, görünürlük beklentileri, düzeltme örneği ve yaşam döngüsü kararları.

### Tamamlanma ölçütü

İşlem sırası, verinin geçerlilik dönemi ve sistemin bilgiyi öğrenme zamanı gerektiği yerde ayrılmıştır. Hangi geçmişin korunacağı ve güncellik beklentisinin hangi kullanıma ait olduğu anlaşılırdır.

### Sonraki adıma geçiş

Zamansal beklentilerin hangi ihtiyaca hizmet ettiğini Gaye Protokolü'nde değerlendirin. Gaye incelemesi bu beklentileri değiştirirse 3 ve 4'ü birlikte güncelleyin.

## 5 Gaye Protokolü

**Korunan başlangıç sorusu:**

> Hangi nihai amaca hizmet eder? Bu nihai amaca ulaştıran nelerdir? Neler değildir?

### Doğrudan amaç ve hizmet edilen faaliyet

Veri tabanı mühendisliğinin doğrudan amacı, insanların ve yazılımların veriye hangi anlam ve güven koşulları altında dayanabileceklerini bilerek işlem yapabilmelerini sağlamaktır. Bir işlemin sonucu, başka bir işlemin güvenilir dayanağı hâline gelir. Tiyatro örneğinde kullanıcı ayırttığı koltuğu anlayabilmeli, görevli geçerli rezervasyonu belirleyebilmeli ve sistem değiştiğinde mevcut rezervasyonların anlamı korunabilmelidir.

Teknik amaçla onun hizmet ettiği insani veya kurumsal amaç farklı düzeylerdir. Teknik düzeyde anlamı belirli, erişilebilir, korunabilir ve değiştirilebilir bir veri düzeni kurulur. Bu düzen bilimsel araştırmaya, ulaşıma, eğitime, üretime, arşivlemeye veya başka bir faaliyete hizmet edebilir. Bu faaliyetlerin değeri ve meşruiyeti veri tabanı mekanizmalarından tek başına çıkarılamaz.

Teknik olarak güvenilir bir sistem, yanlış seçilmiş bir amaca da hizmet edebilir. Bu nedenle sistemin başarısı, amacın doğru seçildiğinin kanıtı olarak alınmaz. Mühendislik, hangi hedefi hangi koşullarda gerçekleştirdiğini açıklayabilir; hedefin gerekçesi ve sonuçları ayrıca değerlendirilir.

### Gayeye ulaştıran nitelikler

Amaca ulaşmak, gereksinimler arasında uygun ve doğrulanabilir bir bütün kurmayı gerektirir. Kayıtların neyi temsil ettiği, birimleri, kapsamı ve kaynağı anlaşılabilmelidir. Çakışan veya yinelenen işlemlerde kabul edilmiş kurallar korunmalıdır. Yetkili kişiler ve işlemler ihtiyaç duydukları veriye ulaşabilmelidir. Anlamın açıklığı, geçerli değişim ve uygun erişim bu bakımdan aynı amaca katkıda bulunur.

Zamanında hizmet, ilgili iş yükünde yanıt süresinin ve veri güncelliğinin yeterli olmasıdır. Süreklilik, tanımlanmış arızalardan sonra kullanılabilir bir durumun geri kazanılmasıdır. Değişebilirlik, yeni ihtiyaçlar karşılanırken mevcut verinin anlamının korunmasıdır. Bunların maliyeti, karmaşıklığı ve işletim yükü karşılanabilir olduğunda düzen sürdürülebilir hâle gelir.

Bu nitelikler birbirini etkiler. Daha güçlü güncellik beklentisi farklı koordinasyon gerektirebilir; daha çok indeks yazma maliyetini artırabilir; daha uzun saklama süresi yönetim yükünü büyütebilir. Amaç, her özelliği en yüksek değerine çıkarmak değil, kullanım için yeterli ve gerekçelendirilebilir bir düzen kurmaktır.

~~~text
  IKI DUZEY
    insani veya kurumsal faaliyet
      bilimsel arastirma . ulasim . egitim . uretim . arsivleme . ...
      degeri ve mesruiyeti  -/->  veri tabani mekanizmalarindan tek
                                  basina cikarilir
                 ^
                 |  hizmet edebilir
                 |
    teknik amac
      anlami belirli, erisilebilir, korunabilir ve degistirilebilir bir
      veri duzeni
      dogrudan amac:  insanlarin ve yazilimlarin veriye hangi anlam ve
      guven kosullari altinda dayanabileceklerini bilerek islem
      yapabilmeleri

    teknik olarak guvenilir sistem  -->  yanlis secilmis bir amaca da
                                         hizmet edebilir
    sistemin basarisi  -/->  amacin dogru secildiginin kaniti

  GAYEYE ULASTIRAN NITELIKLER
    anlamin acikligi . gecerli degisim . uygun erisim . zamaninda
    hizmet . sureklilik . degisebilirlik . surdurulebilirlik

  BIRBIRINI ETKILER
    daha guclu guncellik beklentisi  -->  farkli koordinasyon
                                          gerektirebilir
    daha cok indeks                  -->  yazma maliyetini artirabilir
    daha uzun saklama suresi         -->  yonetim yukunu buyutebilir
    amac:  her ozelligi en yuksek degerine cikarmak degil; kullanim
    icin yeterli ve gerekcelendirilebilir bir duzen
~~~

*Çizim 16 — Gaye: teknik amaç ve hizmet ettiği faaliyet; gayeye ulaştıran nitelikler; birbirini etkileyen nitelikler.*

Okumaların beklentileri kullanım amacına göre ayrılabilir. DynamoDB belgeleri, yakın zamanda tamamlanmış bir yazmayı henüz yansıtmayabilen okumalarla güçlü tutarlılık isteyen okumaları ayırır. Mühendislik, bu farkın hangi kullanımda kabul edilebilir olduğunu belirler. Varsayımsal tiyatro sisteminde doluluk eğilimini gösteren ekranda kısa bir gecikmeye izin verilirken son koltuğun tahsisinde daha sıkı koşullar seçilebilir. [17]

Gereksiz veriyi üretmemek veya tutmamak da amaca hizmet edebilir. Bir bilgi kullanımını tamamladığında, saklanmasının gerekçesi yeniden değerlendirilir. Saklama, düzeltme, arşivleme ve silme birbirinden kopuk faaliyetler olarak ele alınmaz; verinin kullanım amacı ve yaşam döngüsüyle ilişkilendirilir.

### Gayeyi taşıyan makine ve insan sorumluluğu

Makine, tasarımda seçilmiş hedefleri, öncelikleri ve sınırları davranışına taşıyabilir. Bu anlamda işlevsel bir gayesi vardır. Ancak bir amacı gerçekleştirecek biçimde düzenlenmekle o amacın neden benimsenmesi gerektiğini gerekçelendirmek farklı ilişkilerdir. Hedefin uygulanmasıyla gerekçesi aynı yerde bulunmak zorunda değildir.

Amaç veren insanları ve kurumları tek bir birleşik irade olarak düşünmek de eksik kalır. Kullanıcı hızlı işlem, işletmeci düşük maliyet, alan uzmanı belirli ayrımların korunmasını ve verisi tutulan kişi düzeltme veya kullanım sınırı isteyebilir. Bu beklentiler kendiliğinden uyuşmayabilir. Tasarım, aralarındaki kararları ve ödünleşimleri görünür kılmalıdır.

Veri tabanı mühendisi bütün amaçların tek sahibi değildir; fakat yalnız verilen komutları uygulayan edilgin bir operatör olarak da tanımlanamaz. Bir kuralın uygulanabilir olmasıyla gereksinimleri karşılaması arasında mesleki değerlendirme gerekir. ACM'nin etik çerçevesi, bilişim alanında çalışanların eylemleri ve daha geniş etkileri üzerindeki sorumluluğu insanlara yöneltir. Teknik aygıtın çalışması, bu sorumluluğu ortadan kaldırmaz. [18]

Sorumluluğun farklı kişiler arasında dağılması, sorumluluğun kaybolması anlamına gelmemelidir. Hangi kararın kim tarafından verildiği, hangi güvencenin nasıl sağlandığı ve sorun durumunda kimin müdahale edeceği açıklanmalıdır. Sosyoteknik bütünün işleyişi, bu ayrımların korunmasına bağlıdır.

~~~text
  FARKLI ILISKILER
    bir amaci gerceklestirecek     =/=   o amacin neden benimsenmesi
    bicimde duzenlenmek                  gerektigini gerekcelendirmek
    makine:  tasarimda secilmis hedefleri, oncelikleri ve sinirlari
    davranisina tasiyabilir  -->  bu anlamda islevsel bir gayesi vardir
    hedefin uygulanmasi ile gerekcesi ayni yerde bulunmak zorunda degil

  AMAC VERENLER  tek bir birlesik irade olarak dusunulmez
    kullanici               hizli islem
    isletmeci               dusuk maliyet
    alan uzmani             belirli ayrimlarin korunmasi
    verisi tutulan kisi     duzeltme veya kullanim siniri
            |
            v
    bu beklentiler kendiliginden uyusmayabilir
            |
            v
    tasarim:  aralarindaki kararlari ve odunlesimleri gorunur kilar

  MUHENDIS
    butun amaclarin tek sahibi degil; yalniz verilen komutlari uygulayan
    edilgin bir operator de degil
    kuralin uygulanabilir olmasi  <-- mesleki degerlendirme -->
                                      gereksinimleri karsilamasi
    ACM  [18]  bilisim alaninda calisanlarin eylemleri ve daha genis
               etkileri uzerindeki sorumluluk insanlara yoneltilir
    teknik aygitin calismasi  -/->  bu sorumlulugu ortadan kaldirir

  SORUMLULUK
    farkli kisiler arasinda dagilmasi  -/->  kaybolmasi
    aciklanir:  hangi kararin kim tarafindan verildigi . hangi
    guvencenin nasil saglandigi . sorun durumunda kimin mudahale
    edecegi
~~~

*Çizim 17 — Gaye: işlevsel gaye ile gerekçe; amaç verenlerin beklentileri; mühendisin konumu; dağılan sorumluluk.*

### Nihai amaç olmayanlar

Mümkün olan en çok veriyi biriktirmek, en yüksek işlem sayısına ulaşmak, sınırsız erişim vermek veya en karmaşık mimariyi kurmak bağımsız nihai amaçlar değildir. Anlamı belirsiz veri güvenilirlik üretmeyebilir. Çok hızlı çalışan fakat çelişkili rezervasyonlar kabul eden bir sistem işlevini yerine getiremez. Yetkisiz erişimin hızlı olması da başarı sayılmaz.

Belirli bir teknolojiye bağlılık veya bütün mekanizmaları en güçlü ayarda çalıştırmak, gereksinimlerin karşılandığını göstermez. Tasarımın değeri, hizmet ettiği amaçla ilişkisinin açıklanmasına ve bu ilişkiyi destekleyen davranışın sınanmasına dayanır.

Veri tabanının tutarlılığı bilginin doğruluğunun tamamını kapsamaz. Yanlış ölçüm, yetersiz koltuk haritası veya eksik iş kuralı kusursuz işlem mekanizmalarıyla korunabilir. Bu nedenle alan bilgisinin doğrulanması, girdilerin niteliğinin değerlendirilmesi, işletimden öğrenilmesi ve gerektiğinde kayıtların düzeltilmesi amacın gerçekleşmesine katılır. Veriye güven, üretilen sonucun ne anlama geldiğinin ve hangi koşullarda geçerli olduğunun anlaşılabilmesini gerektirir.

### Masaüstünde uygulama

**Girdi:** Başlangıç ihtiyacı, 1–4'ün kararları, ilgili kullanıcı ve kurum beklentileri.

1. Sistemin desteklediği insani veya kurumsal faaliyeti bir paragrafta açıklayın. Teknik düzenin doğrudan amacını bu faaliyete bağlayın. Hangi kişilerin sonucu kullanacağını, hangi kişilerin sonuçtan etkileneceğini ve amaç hakkında kimin karar verdiğini belirtin.

2. Önemli başarı koşulları için gözlenebilir kabul ölçütü veya gerekliyse sayısal eşik yazın. Eşiğin gerekçesini ve değerlendirme yolunu belirtin. Yeterli bilgi yoksa sayı uydurmayın; koşulu ve açık kararı kaydedin.

3. Hız, güncellik, süreklilik, maliyet, erişim veya saklama arasından bu işe gerçekten ait ödünleşimleri değerlendirin. Seçilen tercihi, karşılanan ihtiyacı, kabul edilen sınırı ve karar sorumlusunu birlikte yazın.

4. 1–4'teki önemli tasarım kararlarının bu amaca katkısını açıklayın. Kullanımını tamamlayan verinin tutulma gerekçesini de değerlendirin. Amacın veya kullanıcı ihtiyacının değişmesi hâlinde hangi kararların yeniden açılacağını belirtin. Amaç veya kabul ölçütü değişirse 3'teki mekanizmanın ve mevcut kanıtın yeni ölçüt için yeterliliğini değerlendirin; yeni denemeyi yalnız kalan somut soruyu çözmek için planlayın.

### Üretilecek kayıt

`calisma/05_GAYE_KAYDI.md`: hizmet edilen faaliyet, teknik amaç, başarı ölçütleri, gerekçeli tercihler, ilgili taraflar ve karar sorumluları.

### Tamamlanma ölçütü

Önemli tasarım kararlarının hangi amaca hizmet ettiği açıklanabilir. Teknik başarı, amacın gerekçesi veya verinin dünyayı doğru temsil ettiğinin tek başına kanıtı olarak sunulmaz. Çatışan ya da belirlenmemiş beklentiler görünürdür.

### Sonraki adıma geçiş

Amaç, ölçüt ve karar gerekçelerini Kökleşme Protokolü'ne taşıyın. Bu aşamada temel nesne veya kapsam değişmişse doğrudan kapanış vermek yerine ilgili önceki kaydı güncelleyin.

## 6 Kökleşme (Bitiş) Protokolü

**Tamamlayıcı protokol sorusu:**

> Bu incelemede hangi anlayış ve kararlar dayanak kazanmıştır; bunlar hangi koşullarda geçerlidir, nasıl devredilir ve ne zaman yeniden ele alınır?

### Beş boyutun birlikte değerlendirilmesi

Kökleşme, varlık, mekân, usul, zaman ve gaye boyunca geliştirilen cevapların birbirini destekleyen, dayanakları gösterilmiş ve yeniden kullanılabilir bir bütün hâline gelmesidir. Her bölümün kendi içinde anlaşılır olması gereklidir; bölüm sonuçları arasındaki ilişkinin de açıklanması gerekir. Varlık'ta tanımlanan nesnelerin sistemdeki temsili, Mekan'da açıklanan kapsam ve yetki sınırlarıyla uyuşmalı; dışarıda kalan nesneler ve bağımlılıklar açıkça gösterilmelidir. Usül'de seçilen işleyiş, Zaman'da belirtilen sürekliliği ve görünürlüğü korumalı; bu düzen Gaye'de açıklanan faaliyete hizmet etmelidir.

Varsayımsal rezervasyon örneğinde aynı gösterinin aynı koltuğu için iki etkin rezervasyonu geçersiz saymak, Varlık Protokolü'nde bir sınır koyar. Mekan Protokolü kabul yetkisinin hangi işlem yolunda bulunduğunu açıklar. Usül Protokolü bu sınırın çakışan istekler karşısında nasıl korunacağını belirler. Zaman Protokolü kabulün, görünürlüğün ve kullanıcının sonucu öğrenmesinin sırasını ayırır. Gaye Protokolü bütün bu kararların geçerli bir rezervasyona dayanabilme ihtiyacına nasıl hizmet ettiğini gösterir. Bu bağlardan biri eksikse, yalnız bir bölümdeki başarı bütünün yeterliliğini kanıtlamaz.

Kökleşmede cevapların dayanağı da görünür olur. Kavramsal bir sonuç, açık bir gerekçeye ve ilgili kaynaklara dayanabilir. Tasarım sonucu, model ve kararlar arasındaki tutarlılıkla değerlendirilir. Çalışan bir sisteme ilişkin doğrulama iddiası ise belirli ortamda gözlenen davranışı ve kabul ölçütünü gerektirir. Bu dayanak türleri birbirinin yerine geçirilmez.

~~~text
  BIR KARAR BES BOYUT BOYUNCA  varsayimsal rezervasyon ornegi
    1 Varlik   sinir:  ayni gosterinin ayni koltugu icin iki etkin
       |       rezervasyon gecersiz
       |
    2 Mekan    kabul yetkisinin hangi islem yolunda bulundugunu
       |       aciklar
       |
    3 Usul     bu sinirin cakisan istekler karsisinda nasil
       |       korunacagini belirler
       |
    4 Zaman    kabulun, gorunurlugun ve kullanicinin sonucu
       |       ogrenmesinin sirasini ayirir
       |
    5 Gaye     butun bu kararlarin gecerli bir rezervasyona dayanabilme
               ihtiyacina nasil hizmet ettigini gosterir
    baglardan biri eksikse  -->  yalniz bir bolumdeki basari butunun
                                 yeterliligini kanitlamaz

  DAYANAK TURLERI  birbirinin yerine gecirilmez
    kavramsal sonuc      acik gerekce . ilgili kaynaklar
    tasarim sonucu       model ve kararlar arasindaki tutarlilik
    dogrulama iddiasi    belirli ortamda gozlenen davranis . kabul
                         olcutu
~~~

*Çizim 18 — Kökleşme: bir kararın beş boyut boyunca izi; dayanak türleri.*

### Makine sorusunun birlikte cevabı

Beş boyutu teknik olarak taşıyan makine; veriler, modeller, veri tabanı yönetim sistemi, uygulamalar, donanım ve bunların işletim düzeni içinde somutlaşır. Durum makinesi, bu düzenin belirli davranışlarını açıklayan bir modeldir. Hesaplanabilirlik modeli, ürün adı veya tek bir donanım parçası, veri tabanı mühendisliğinin bütün kökenini ve kimliğini açıklamaz.

Anlam veren, kuralları seçen, yetkiyi tanımlayan ve amacın gerekçesini değerlendiren insanlar ve kurumlar bu teknik taşıyıcıyla birlikte çalışır. Mühendis; alan uzmanı, kullanıcı ve diğer sorumlularla ilişkisi içinde beklentileri uygulanabilir ve değerlendirilebilir davranışa dönüştürür. Bu bütün sosyoteknik olarak adlandırılabilir. Adlandırma, insanla teknik aygıtı aynı varlık türüne indirgemez.

Bu nedenle 'Kimdir?' sorusu taşıma, işletme, anlamlandırma ve sorumlu olma ilişkileri ayrılarak cevaplanır. Teknik taşıyıcı davranışı yürütür; soyut model davranışı açıklar; ilgili insanlar ve kurumlar karar ve sorumlulukları taşır. 'Kim değildir?' sorusunun cevabı da sınırı belirler: bütünün tek sahibi sayılan bir ürün, kendiliğinden amaç belirleyen bir depolama aygıtı, her kararı tek başına veren bir meslek unvanı veya insanın bütün varlığını açıklayan bir hesaplama modeli bu incelemenin sonucu değildir.

~~~text
  "KIMDIR?"  tasima, isletme, anlamlandirma ve sorumlu olma iliskileri
  ayrilarak cevaplanir
    +--------------------+-------------------+------------------------+
    | teknik tasiyici    | soyut model       | insanlar ve kurumlar   |
    +--------------------+-------------------+------------------------+
    | veriler .          | durum makinesi    | anlam veren .          |
    | modeller .         |                   | kurallari secen .      |
    | veri tabani        |                   | yetkiyi tanimlayan .   |
    | yonetim sistemi .  |                   | amacin gerekcesini     |
    | uygulamalar .      |                   | degerlendiren          |
    | donanim .          |                   |                        |
    | isletim duzeni     |                   |                        |
    +--------------------+-------------------+------------------------+
    | davranisi yurutur  | davranisi aciklar | karar ve               |
    |                    |                   | sorumluluklari tasir   |
    +--------------------+-------------------+------------------------+
    hesaplanabilirlik modeli . urun adi . tek bir donanim parcasi
      -/->  veri tabani muhendisliginin butun kokeni ve kimligi
    birlikte calisir; bu butun sosyoteknik diye adlandirilabilir
    adlandirma  -/->  insan ile teknik aygit ayni varlik turu
    muhendis:  alan uzmani, kullanici ve diger sorumlularla iliskisi
    icinde beklentileri uygulanabilir ve degerlendirilebilir davranisa
    donusturur

  "KIM DEGILDIR?"  sinir
    x  butunun tek sahibi sayilan bir urun
    x  kendiliginden amac belirleyen bir depolama aygiti
    x  her karari tek basina veren bir meslek unvani
    x  insanin butun varligini aciklayan bir hesaplama modeli
~~~

*Çizim 19 — Kökleşme: makine sorusunun birlikte cevabı; kimdir ve kim değildir.*

### Kapanış ve devamlılık

Bitiş, belirli bir sorunun, kapsamın ve sürümün kapanışıdır. Sonuçların değişmezliği anlamına gelmez. Hangi soruların cevaplandığı, hangi kararların verildiği, hangi noktaların açık kaldığı ve hangi değişikliklerin yeniden inceleme gerektireceği kaydedilir. Başka bir kişi bu kayıttan hem varılan sonucu hem devam edilecek yeri anlayabilmelidir.

Bir kavramsal inceleme, sınırlarını açıkça göstererek tamamlanabilir. Gerçek bir sistemin doğrulanması hedeflenmişse, temel kabul ölçütünü etkileyen açık bir mesele varken sistem doğrulanmış sayılmaz. Böyle bir çalışma kısmi sonuçlarıyla devredilebilir; tamamlanma iddiasının kapsamı buna göre yazılır.

Kökleşme; yalnız dosyayı kaydetmek, bütün kutuları işaretlemek, bir başkasından biçimsel onay almak veya konuyu tekrar açılamayacak biçimde kapatmak değildir. Sonucun anlaşılabilir, izlenebilir ve kullanılabilir kalmasıdır. Yeni bir ihtiyaç, çelişen kanıt, değişen veri anlamı veya farklı kullanım koşulu ortaya çıktığında kapanış kaydı yeni bir Tohum Protokolü için başlangıç dayanağı olur.

~~~text
  BITIS  belirli bir sorunun, kapsamin ve surumun kapanisi
    kaydedilir:  cevaplanan sorular . verilen kararlar . acik kalan
                 noktalar . yeniden inceleme gerektirecek degisiklikler
    baska bir kisi bu kayittan hem varilan sonucu hem devam edilecek
    yeri anlayabilmeli
    bitis  -/->  sonuclarin degismezligi

  TAMAMLANMA
    kavramsal inceleme  sinirlarini acikca gostererek tamamlanabilir
    gercek bir sistemin dogrulanmasi hedeflenmisse:
      temel kabul olcutunu etkileyen acik bir mesele varken
      -/->  sistem dogrulanmis sayilir
      kismi sonuclarla devredilebilir; tamamlanma iddiasinin kapsami
      buna gore yazilir

  KOKLESME DEGIL
    yalniz dosyayi kaydetmek . butun kutulari isaretlemek . bir
    baskasindan bicimsel onay almak . konuyu tekrar acilamayacak
    bicimde kapatmak
  KOKLESME
    sonucun anlasilabilir, izlenebilir ve kullanilabilir kalmasi

    +------------------+      yeni bir ihtiyac         +--------------+
    | 6 Koklesme       |      celisen kanit            | yeni bir     |
    | kapanis kaydi    |----  degisen veri anlami  --->| 0 Tohum      |
    |                  |      farkli kullanim kosulu   |              |
    +------------------+                               +--------------+
    kapanis kaydi  -->  yeni Tohum Protokolu icin baslangic dayanagi
~~~

*Çizim 20 — Kökleşme: bitişin kaydı; tamamlanma; kökleşme olan ve olmayan; kapanış kaydından yeni bir Tohum'a.*

### Masaüstünde uygulama

**Girdi:** 0'ın başlangıç soruları, 1–5'in kayıtları, ilgili kaynaklar, kararlar ve varsa gerçek uygulama kanıtları.

1. Başlangıç sorularının her birini gözden geçirin. Cevabın bulunduğu kaydı, varılan sonucu ve açık kalan hususu kapanış kaydına yazın. İnceleme sırasında soru değiştiyse ilk soru ile son soruyu ve değişiklik gerekçesini ilişkilendirin.

2. En önemli kararları beş boyut boyunca izleyin: hangi nesne veya kural, hangi yerde ve yetki altında, hangi usulle, hangi zaman koşulunda, hangi amaç için korunuyor? Çelişki varsa ilgili protokole dönün. Açık bir çelişkiyi biçimsel tamamlanma işaretiyle kapatmayın.

3. Makine sorusunu birlikte cevaplayın. Teknik taşıyıcıyı, kullanılan soyut modeli ve anlam, yetki veya sorumluluk taşıyan insanları ayırın. Bu sonuçlardan insanın bütün varlığına veya tek bir ürünün alanı bütünüyle temsil ettiğine ilişkin bir iddia çıkarmayın.

4. Çalışma düzeyine uygun sonuç durumunu seçin. Kavramsal inceleme için gerekçeli cevapları; tasarım için tutarlı model ve kararları; sistem doğrulaması için kabul ölçütüyle ilişkilendirilmiş gözlem ve kanıtları değerlendirin. Bir deneme kaydı yoksa doğrulanmış sistem sonucu yazmayın. Temel ölçütü etkileyen açık iş varsa sonucu kısmi veya açık olarak kaydedin.

5. Açık meseleleri etkisi, devam işi ve sorumlusuyla kaydedin; sorumlu belirlenmediyse bunu yazın. Yeniden ele alma koşullarını somutlaştırın: veri anlamı, kabul kuralı, yetkili kaynak, zaman beklentisi veya kullanım amacı değiştiğinde hangi protokol açılacak? İhtiyaç varsa izleme veya işletim devrini de belirtin.

6. Son sürümü, tarihi ve dosya yerlerini kaydedin. Bağlantıları ve kanıt yollarını açarak kontrol edin. Çalışma klasörünün kapanış kopyasını alın; devam edecek çalışma için yeni sürüm veya ayrı kopya kullanın. Sonuç kaydı, ulaşılan anlayışı ve devam noktasını birlikte gösterebilmelidir.

### Üretilecek kayıt

`calisma/06_KOKLESME_KAYDI.md`: soru–sonuç eşleştirmesi, boyutlar arası tutarlılık, makine sorusunun toplu cevabı, tamamlanma durumu, kanıtlar, açık işler, devir ve yeniden ele alma koşulları.

### Tamamlanma ölçütü

Başka bir kişi sonucun ne olduğunu, neye dayandığını, hangi koşullarda geçerli olduğunu ve devam için ne gerektiğini kayıtlardan anlayabilir. Kavramsal belgenin tamamlanmasıyla somut sistemin doğrulanma durumu ayrı belirtilmiştir. Bağlantı ve kayıt düzeni kullanılabilirdir.

### Sonraki adıma geçiş

Bu kapsam için kapanış kaydını koruyun. Yeniden ele alma koşulu oluşursa önceki kayda bağlanan yeni bir Tohum Protokolü açın; değişen varsayımları ve etkilediği bölümleri belirtin.

## Tek dosyayla çalışmak için kayıt şablonu

Aşağıdaki şablonu her protokol için `calisma` klasöründeki ilgili kayıt dosyasına kopyalayın ve ilgili bölümün “Üretilecek kayıt” başlığında belirtilen alanları ekleyin. Şablondaki alanlar sonuç değildir; uygulama sırasında doldurulur.

```markdown
# [Protokol numarası ve adı] Çalışma Kaydı

Çalışma adı: Doldurulacak
İnceleme nesnesi / örnek senaryo: Doldurulacak
Seçilen işlem: Doldurulacak veya gerekçesiyle Uygulanmaz
Çalışma düzeyi: Doldurulacak
Tarih ve sürüm: Doldurulacak
Sorumlu: Doldurulacak
Durum: Başlatılmadı

## Soru ve girdi

Yanıtlanacak soru, önceki kayıtlardan alınan bilgiler ve kaynaklar.

## Yanıt ve gerekçe

Kavramsal sonuç, tasarım kararı veya gözlenen durum; dayanağı ve sınırı.

## Uygulama ve doğrulama

Yapılan işlem, ortam, beklenen sonuç, gözlenen sonuç ve kanıt yolu.
İşlem yapılmadıysa bunu yazın; tasarım planını sonuç gibi sunmayın.

## Açık meseleler

Belirlenmeyen konu, etkisi, devam işi ve varsa sorumlusu.
Kapsam dışı veya uygulanmaz alanların kısa gerekçesi.

## Çıkış

- [ ] Bölümün tamamlanma ölçütü, seçilen çalışma düzeyinde değerlendirildi.
- [ ] Yanıtın dayanağı ve sınırı gösterildi.
- [ ] Sonraki bölüme aktarılacak sonuç ve açık meseleler kaydedildi.

Sonuç durumu ve kapsamı: Doldurulacak
Bir sonraki işlem: Doldurulacak
```

6'nın kaydında ayrıca **kavramsal inceleme veya tasarımın tamamlanma durumu** ile **somut sistemin doğrulanma durumunu** ayrı yazın. Çalışmanın hangi kısmının tamamlandığı anlaşılmadan genel bir “tamamlandı” kaydı kullanmayın.

## Kaynakça

Aşağıdaki birincil kaynaklar, 1–5 bölümlerindeki teknik açıklamaları destekler. 0 ve 6 ile masaüstü uygulama adımları, bu çalışma için oluşturulmuş bir sentezdir. Ürüne özgü bir uygulama yürütülecekse kullanılan sürümün belgeleriyle karşılaştırılır.

**[1] E. F. Codd** (1970). A Relational Model of Data for Large Shared Data Banks (https://research.ibm.com/publications/a-relational-model-of-data-for-large-shared-data-banks).

**[2] Leslie Lamport** (1978). Time, Clocks and the Ordering of Events in a Distributed System (https://www.microsoft.com/en-us/research/publication/time-clocks-ordering-events-distributed-system/).

**[3] A. M. Turing** (1936). On Computable Numbers, with an Application to the Entscheidungsproblem (https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf).

**[4] SQLite**. SQLite Is Serverless (https://www.sqlite.org/serverless.html).

**[5] Google Research**. Spanner: Google's Globally-Distributed Database (https://research.google/pubs/spanner-googles-globally-distributed-database-2/).

**[6] PostgreSQL**. Architectural Fundamentals (https://www.postgresql.org/docs/current/tutorial-arch.html).

**[7] PostgreSQL**. Constraints (https://www.postgresql.org/docs/current/ddl-constraints.html).

**[8] PostgreSQL**. Transactions (https://www.postgresql.org/docs/current/tutorial-transactions.html).

**[9] PostgreSQL**. Transaction Isolation (https://www.postgresql.org/docs/current/transaction-iso.html).

**[10] PostgreSQL**. Write-Ahead Logging (WAL) (https://www.postgresql.org/docs/current/wal-intro.html).

**[11] PostgreSQL**. Continuous Archiving and Point-in-Time Recovery (PITR) (https://www.postgresql.org/docs/current/continuous-archiving.html).

**[12] Raymond Blum ve Rhandeev Singh**. Data Integrity: What You Read Is What You Wrote (https://sre.google/sre-book/data-integrity/).

**[13] PostgreSQL**. Indexes Introduction (https://www.postgresql.org/docs/current/indexes-intro.html).

**[14] IBM Db2**. Temporal Tables and Data Versioning (https://www.ibm.com/docs/en/db2-for-zos/12.0.0?topic=tables-temporal-data-versioning).

**[15] Amazon Web Services**. What Is Amazon Relational Database Service (https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html).

**[16] pgvector**. Project Documentation (https://github.com/pgvector/pgvector).

**[17] Amazon Web Services**. DynamoDB Read Consistency (https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html).

**[18] Association for Computing Machinery**. ACM Code of Ethics and Professional Conduct (https://www.acm.org/binaries/content/assets/about/acm-code-of-ethics-and-professional-conduct.pdf).

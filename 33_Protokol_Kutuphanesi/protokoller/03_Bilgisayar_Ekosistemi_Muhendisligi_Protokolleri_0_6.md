# Bilgisayar Ekosistemi Mühendisliği Protokolleri

**Tohumdan Kökleşmeye Kavramsal Esaslar ve Masaüstü Uygulaması**

**Sürüm:** 1.0\
**Tarih:** 30 Ekim 2026\
**Kapsam:** 0–6 protokollerinin tam metni ve uygulama düzeni.

Bilgisayar Ekosistemi Mühendisliği, hesaplama yoluyla iş yapabilmemizi sağlayan donanım, yazılım, veri, ağ, insanlar, kurumlar ve kurallar arasındaki bağımlılıkları tasarlama, gerçekleştirme, sınama ve zaman içinde sürdürme yaklaşımıdır. Bu yaklaşımın inceleme birimi, insan faaliyetleri içinde örgütlenmiş bilgisayarlı çalışma düzenidir. Hesaplama yeteneğinin hangi ilişkiler sayesinde ortaya çıktığı, hangi koşullarda sürdüğü ve nasıl değiştirilebildiği birlikte ele alınır.

Bu adlandırma bir çalışma tanımıdır; adı ve sınırları üzerinde uzlaşılmış bağımsız bir disiplin bulunduğu iddiasını içermez. Protokoller, kavramın kapsamını ve kurucu ayrımlarını masaüstünde uygulanabilir çalışma adımlarıyla birleştirir. Bir ekosistemin ne olduğunu açıklamak ile onun iyi tasarlanmış olduğunu değerlendirmek ayrı tutulur. Güvenilirlik, erişilebilirlik ve sürdürülebilirlik, bir ekosistemin varlığıyla kendiliğinden sağlanan özellikler olarak kabul edilmez.

**Ortak taşıyıcı sorusu:** Bilgisayar Ekosistemi Mühendisliği’nin köken aldığı varlık, mekan, usül, zaman, ve gayeyi taşıyan makine kimdir? Kim değildir?

Bu sorunun cevabında teknik taşıyıcı olarak bilgisayar, ilişkiler bütünü olarak ekosistem ve amaçla sorumluluğu taşıyan insanlar ile kurumlar ayrılır. Beş boyutu birlikte ele aldığımız birim, insan faaliyetleri içindeki bilgisayarlı çalışma düzenidir. Bu bütüne makine denildiğinde sözcük geniş bir sistemsel anlam taşır; insanın makineye indirgenmesi veya bütünün tek irade sayılması sonucu çıkmaz.

~~~text
  INCELEME BIRIMI
  insan faaliyetleri icinde orgutlenmis bilgisayarli calisma duzeni

  ARALARINDAKI BAGIMLILIKLAR TASARLANIR, GERCEKLESTIRILIR, SINANIR,
  SURDURULUR
    donanim . yazilim . veri . ag . insanlar . kurumlar . kurallar

  ORTAK TASIYICI SORUSUNUN CEVABINDA AYRILAN UC SEY

   .------------------.   .------------------.   .------------------.
   | TEKNIK TASIYICI  |   | ILISKILER BUTUNU |   | AMAC VE          |
   |                  |   |                  |   | SORUMLULUK       |
   | bilgisayar       |   | ekosistem        |   | insanlar ve      |
   |                  |   |                  |   | kurumlar         |
   `------------------'   `------------------'   `------------------'

   bu butune "makine" denildiginde sozcuk genis bir sistemsel
   anlam tasir; bundan su sonuclar cikmaz:
     insanin makineye indirgenmesi . butunun tek irade sayilmasi

  AYRI TUTULUR
    bir ekosistemin ne oldugunu   |   onun iyi tasarlanmis oldugunu
    aciklamak                     |   degerlendirmek

    guvenilirlik, erisilebilirlik ve surdurulebilirlik, bir
    ekosistemin varligiyla kendiliginden saglanmaz
~~~

*Çizim 1 — İnceleme birimi; ayrılan üç şey: teknik taşıyıcı, ilişkiler bütünü, amaç ve sorumluluk.*

## Masaüstünde kullanım düzeni

Bu Markdown belgesi, bir kişi veya yetkilendirilmiş yardımcı tarafından izlenecek çalışma yönergesidir. Metin editöründe açılıp okunabilir; bir betik gibi kendiliğinden işlem yürütmez. Bir protokolü okumak veya uygulama planını yazmak, protokolün uygulanmış olduğu anlamına gelmez. Fiilî çalışma, seçilen klasörde gerçekleştirilen işlemler ve gözlenen sonuçlar üzerinden kaydedilir.

Çalışmanın konusu ve kök klasörü başlangıçta seçilir. Protokol metni başvuru belgesi olarak korunur; gerçek çalışma tek bir `uygulama-kaydi.md` dosyasına yazılır. Bu dosya, sondaki kayıt şablonu kopyalanarak açılır. Dosya adları ve yerel başvurular çalışma klasörüne göre yazılır; belirli bir işletim sistemi yolu varsayılmaz.

Numaralandırma belgenin kavramsal sırasını gösterir. Uygulamada 0 ile başlangıç belirlenir; 1 ve 2 ile düzen ve bağımlılıklar açıklanır. Bir değişiklik yapılmadan önce 5'in amaç ve başarı ölçütleri ile 4'ün zaman ve geçiş koşulları hazırlanır. Sonra 3'te işlem gerçekleştirilir ve sınanır; 4'e gerçekleşen zaman bilgisi, 5'e sonuç değerlendirmesi eklenir. 6, bu kayıtların birlikte değerlendirilmesiyle çalışmanın mevcut aşamasını kapatır. Yeni bilgi gerektirdiğinde önceki bir protokole dönülebilir; gereksiz bir değişiklik sırf sırayı tamamlamak için yapılmaz.

### Kayıt ilkesi

Her anlamlı kayıt; ilgili dosya veya bileşeni, beklenen sonucu, yapılan işlemi, gözlenen sonucu ve varsa doğrulama dayanağını ayırır. `Planlandı` işlem henüz yapılmadığında, `Uygulandı` işlem gerçekten yapıldığında, `Doğrulandı` ise hedeflenen davranış belirtilen koşullarda gözlendiğinde kullanılır. Denenmeyen kısım veya açık konu ayrıca belirtilir. Doğrulama bir dosyaya, kayıt girdisine ya da tekrar edilebilir bir gözleme dayanabilir; her işlem için ekran görüntüsü veya ayrı rapor üretmek gerekmez.

Çalışmanın tamamlanma durumu ile hedefin karşılanma durumu ayrı tutulur. Bir inceleme gerekçeli olarak kapatılabilir ve aynı anda hedefin karşılanmadığını saptamış olabilir. Kayıt şablonunun başlangıç durumu bu nedenle `Başlatılmadı` ve `Değerlendirilmedi` olarak bırakılmıştır.

~~~text
  UYGULAMA SIRASI  numaralar belgenin kavramsal sirasini gosterir

    0 Tohum            baslangic belirlenir
       |
    1 Varlik, 2 Mekan  duzen ve bagimliliklar aciklanir
       |
    5 Gaye   (once)    amac ve basari olcutleri hazirlanir
    4 Zaman  (once)    zaman ve gecis kosullari hazirlanir
       |
    3 Usul             islem gerceklestirilir ve sinanir
       |
    4 Zaman  (sonra)   gerceklesen zaman bilgisi eklenir
    5 Gaye   (sonra)   sonuc degerlendirmesi eklenir
       |
    6 Koklesme         kayitlar birlikte degerlendirilir;
                       calismanin mevcut asamasi kapanir

    gereksiz bir degisiklik, sirf sirayi tamamlamak icin yapilmaz

  KAYDIN UC DURUMU
    Planlandi    islem henuz yapilmadi
    Uygulandi    islem gercekten yapildi
    Dogrulandi   hedeflenen davranis belirtilen kosullarda gozlendi

  IKI AYRI DURUM
    calismanin tamamlanma durumu   |   hedefin karsilanma durumu
    (baslangicta: Baslatilmadi)    |   (baslangicta: Degerlendirilmedi)

    bir inceleme gerekceli olarak kapatilabilir ve ayni anda
    hedefin karsilanmadigini saptamis olabilir
~~~

*Çizim 2 — Uygulama sırası: 4 ve 5 işlemden önce hazırlanır, işlemden sonra tamamlanır; kaydın üç durumu.*

### Protokoller ve kayıt çıktıları

| No | Protokol | Çalışma kaydındaki temel çıktı |
| --- | --- | --- |
| 0 | Tohum (Başlangıç) | Başlangıç sorusu, kapsam, kaynaklar ve kabuller. |
| 1 | Varlık | Faaliyet tanımı, bileşenler ve sorumlu taraflar. |
| 2 | Mekan | Konumlar, bağımlılıklar, erişim ve müdahale sınırları. |
| 3 | Usül | İşlem, gözlem ve doğrulama kaydı. |
| 4 | Zaman | Ön hazırlık, geçiş sırası ve gerçekleşen zaman bilgisi. |
| 5 | Gaye | Amaç, başarı ölçütü ve sonuç değerlendirmesi. |
| 6 | Kökleşme (Bitiş) | Tutarlılık, açık konular, son dosyalar ve kapanış kararı. |

## 0 Tohum (Başlangıç) Protokolü

**Protokol soruları:** Bu çalışmayı hangi soru veya ihtiyaç başlatıyor? Neyi incelemeye alıyoruz? Hangi kaynaklardan ve kabullerden hareket ediyoruz? Başlangıcın dışında neler kalıyor?

Tohum Protokolü, Bilgisayar Ekosistemi Mühendisliği çalışmasının başlangıç durumunu kayda geçirir. İncelenecek bilgisayarlı çalışma düzeninin adı, ele alınacak faaliyet ve incelemeyi gerekli kılan soru burada belirlenir. Başlangıcın yeterince açık olması, sonraki protokollerin aynı konu üzerinde çalışmasını sağlar. Bu aşamada bütün cevapların bilinmesi gerekmez; henüz cevaplanmamış sorular da başlangıç kaydının bir parçasıdır.

Başlangıç kaydı, çalışmanın hangi kaynaklara dayandığını gösterir. Bu çalışma için sunulan sorular, açıklamalar, belgeler ve seçilen dosyalar kaynak olarak kaydedilir. Kaynaktaki ifade ile çalışma sırasında geliştirilen yorum ayırt edilir. Bir yorumun kullanışlı bulunması, onu kaynakta bulunan bir bilgiye dönüştürmez. Bilinmeyen veya doğrulanmamış bir husus, eksiksiz görünmek amacıyla bilgi gibi yazılmaz. Bu belgenin kavramsal dayanağı, burada kayda alınan soru ve yanıtlardır; başka konuşmalardan bağlam eklenmez.

İncelemenin ilk sınırı da bu protokolde belirlenir. Hangi faaliyetlerin, uygulamaların, dosyaların ve ilişkilerin ele alınacağı; hangi konuların çalışma dışında tutulacağı açıklanır. Masaüstünde çalışma alanı, ele alınan soruya göre seçilen klasör ve belirtilmiş kaynaklarla somutlaşır. Çalışmaya başlamak, bütün bilgisayarı veya önceki bütün çalışmaları taramayı gerektirmez. Başka bir kaynak veya ilişki gerekli hâle geldiğinde kapsam değişikliği gerekçesiyle birlikte kaydedilir.

Çalışmanın başlama niyeti, incelenen düzenin nihai gayesinden ayrılır. Bir çalışma mevcut bağımlılıkları anlamak, bir güçlüğü gidermek veya değişim imkânını değerlendirmek için başlayabilir. İncelenen düzenin hangi insan faaliyetlerine hizmet etmesi gerektiği Gaye Protokolü'nde açılır. Tohum, nihai sonucu önceden zorunlu kılmadan, neden bu soruların sorulduğunu ve hangi belirsizliğin ele alınacağını açıklar.

Başlangıç kabulleri, ilerleyen bölümlerde sınanabilecek ifadeler olarak yazılır. Teknik taşıyıcı, ilişkilerin oluşturduğu bütün ve amaçtan sorumlu taraflar birbirine karıştırılmaz. Bir kabule ilişkin değerlendirme değişirse başlangıç ifadesi ile yeni değerlendirme arasındaki fark korunur. Böylece çalışmanın nereden başladığı ve hangi gerekçeyle yön değiştirdiği sonradan anlaşılabilir.

Tohum, bütün hesaplama tarihinin ilk nedenini açıklayan veya alanın sınırlarını değişmez biçimde belirleyen bir bölüm değildir. Bütün cevapların önceden verilmiş olduğunu ya da bütün tarafların aynı amacı taşıdığını varsaymaz. Görevi, mevcut çalışmayı başlatabilecek açıklıkta bir soru, kapsam ve dayanak oluşturmaktır.

~~~text
  BASLANGIC KAYDI

    soru ya da ihtiyac  +  incelenecek faaliyet  +
    kaynaklar ve kabuller

  KAYNAK ILE YORUM AYIRT EDILIR
    kaynaktaki ifade   |   calisma sirasinda gelistirilen yorum

    bir yorumun kullanisli bulunmasi, onu kaynakta bulunan bir
    bilgiye donusturmez
    bilinmeyen ya da dogrulanmamis husus, eksiksiz gorunmek icin
    bilgi gibi yazilmaz

  ILK SINIR
    .---------------------------------.
    | kapsamda:  faaliyetler,         |     calisma disinda tutulanlar
    | uygulamalar, dosyalar,          |
    | iliskiler                       |     baska kaynak ya da iliski
    `---------------------------------'     gerekirse kapsam degisikligi
                                            gerekcesiyle kaydedilir

    calismaya baslamak, butun bilgisayari ya da onceki butun
    calismalari taramayi gerektirmez

  IKI AYRI SEY
    calismanin baslama niyeti   |   incelenen duzenin nihai gayesi
    (burada)                    |   (5 Gaye'de acilir)

  TOHUM SUNLAR DEGILDIR
    butun hesaplama tarihinin ilk nedenini aciklayan bolum
    alanin sinirlarini degismez bicimde belirleyen bolum
~~~

*Çizim 3 — Tohum: başlangıç kaydı; kaynak ile yorum; ilk sınır; başlama niyeti ile nihai gaye.*

### Masaüstünde uygulama

**Girdi:** Ele alınacak faaliyet, onu başlatan soru veya ihtiyaç ve bu çalışma için seçilmiş kaynaklar.

1. Çalışma klasörünü belirle. Bu klasörde `uygulama-kaydi.md` dosyasını aç veya oluştur; çalışmanın adını, tarihini ve başlangıç sorusunu 0 bölümüne yaz.
2. Kaynak dosyalarını ve başvuru bağlantılarını kaydet. Kaynaktaki bilgilerle kendi yorumlarını ve henüz doğrulanmamış kabulleri ayır.
3. Kapsama dâhil faaliyetleri ve dosyaları, kapsam dışında kalanları ve ilgili tarafları kısa paragraflarla belirt. Başlangıçta neyin yapılabildiğini ve hangi güçlüğün bulunduğunu yaz.
4. İncelemenin neden başladığını ve hangi sonucun hedeflendiğini kaydet. Eksik bilgileri açık soru olarak bırak; sonraki protokollerin aynı başlangıç kaydına dayanmasını sağla.

### Çıktı ve tamamlanma ölçütü

**Çıktı:** `uygulama-kaydi.md` içindeki 0 bölümü; başlangıç sorusu, niyet, kapsam, kaynaklar, ilk durum, kabuller ve açık sorular.

**Tamamlanma ölçütü:** Kaydı okuyan biri neyin inceleneceğini, incelemenin neden başladığını ve hangi dayanaklardan hareket edildiğini anlayabilir. Henüz cevaplanmamış sorular bulunabilir; bunlar doğrulanmış bilgi olarak sunulmaz. İncelenecek faaliyet veya çalışma alanı belli değilse yalnızca bu belirsizliği giderecek inceleme yapılır.

## 1 Varlık Protokolü

**Kurucu sorular:** Nedir? Onu o yapan nelerdir? Neler değildir?

Bilgisayar Ekosistemi Mühendisliğinin konusu, insanların hesaplama olanaklarıyla gerçekleştirdikleri faaliyetleri mümkün kılan teknik, insani ve kurumsal ilişkilerin tasarlanması, kurulması, doğrulanması, sürdürülmesi ve değiştirilmesidir. İncelemenin merkezinde insan faaliyetleri içinde örgütlenmiş bilgisayarlı çalışma düzeni bulunur. Bilgisayarlar, yazılımlar, veriler, ağlar, insanlar ve kurumlar, belirli işlerin yapılabilmesi için bu düzen içinde ilişki kurar. Hesaplama, ele alınan faaliyetin oluşmasında belirleyici bir rol taşır; bilgisayarla herhangi bir ilişkisi bulunan her topluluk bu nedenle aynı kapsamda değerlendirilmez.

Bu varlığın anlaşılması için teknik taşıyıcı, ilişkilerin oluşturduğu bütün ve amaçtan sorumlu özne ayrılır. Hesaplama işlemlerini gerçekleştiren teknik taşıyıcı bilgisayardır; bunun donanımı, yazılımı ve işleyebilmesi için gerekli maddi koşulları vardır. Bu taşıyıcının diğer bileşenler, insanlar ve kurumlarla ilişkilerinden oluşan bütün ekosistemdir. Amaçları gerekçelendiren, tercih yapan ve kararlarının sonuçlarından sorumluluk üstlenen taraflar ise ilgili kişiler ve kurumlardır. Bilgisayarın bir hedef doğrultusunda çalışması, o hedefin neden değerli olduğunu tek başına açıklamaz. Ekosistemin bir bütün olarak incelenmesi de onu tek iradesi, tek amacı ve tek sorumlusu bulunan bir kişi hâline getirmez.

Beş boyutun birlikte ele alındığı birim, bilgisayarlı çalışma düzenidir. Bu bütüne makine denildiğinde sözcük geniş bir sistemsel anlamda kullanılır; insanın makinenin edilgen bir parçasına indirgenmesi veya bütünün insana benzer bir özne sayılması sonucu çıkmaz. Köken kavramı da burada ilk tarihsel bilgisayarın kimliğini değil, bu yaklaşımı mümkün kılan dayanağı belirtir. Bir boyutu taşımak, o boyutun tek kaynağı olmak değildir. Bilgisayar belirli bir mekânda ve zamanda çalışır; mekânın ve zamanın bilgisayardan kaynaklandığı ileri sürülmez.

Bu çalışma düzenini o yapan özellikler, bileşenlerin sayısından çok aralarındaki ilişkilerde bulunur. Bir işin yapılabilmesi başka sistemlerin çalışmasına, verinin anlaşılmasına, erişim yetkilerine, bakımın sürmesine ve sorumlulukların yerine getirilmesine bağlı olabilir. Bu bağımlılıklar anlam, karar, emek ve yükümlülük de taşır. Bileşenler farklı türden olabilir ve farklı kararlarla değişebilir; hepsinin tek bir tasarımcının denetiminde bulunduğu varsayılmaz. Düzenin sürekliliği, tek tek cihazların değişmeden kalmasını gerektirmez. Bir bilgisayar yenilendiğinde veya bir hizmet taşındığında, gerekli ilişkiler ve iş yapabilme yeteneği korunarak faaliyet sürdürülebilir.

Yaklaşımın mühendislik niteliği, ilişkiler üzerinde gerekçeli ve doğrulanabilir müdahalelerde bulunmasından gelir. Gereksinimleri açıklamak, bağımlılıkları belirlemek, seçenekleri karşılaştırmak, arayüzleri ve yetkileri düzenlemek, arızaların etkisini sınamak ve değişikliklerin sonuçlarını izlemek bu müdahalelere dâhildir. Başarı, bir bileşenin çalışmasının yanında, katkıda bulunduğu faaliyetin gerekli koşullarda sürdüğü gösterilerek değerlendirilir. Bu odak, sistem mühendisliğinin bütün ve yaşam döngüsü yaklaşımıyla kesişir. Yazılım ekosistemleri çalışmaları da teknik ürünlerle bunları geliştiren, tamamlayan ve kullanan aktörlerin ilişkilerini birlikte ele alır. Burada önerilen çerçeve, bu dayanaklardan yararlanarak hesaplama ortamının fiziksel ve kullanım koşullarını da kapsar. [1, 2]

Bu yaklaşım tek bir cihazın, algoritmanın, yazılım ürününün veya yapay zekâ sisteminin başka bir adı değildir. Çok sayıda teknolojiyi toplamak, her şeyi birbirine bağlamak ya da bütün uzmanlıkları tek kişide birleştirmek yeterli sayılmaz. Mühendis, kullanıcı, geliştirici, işletmeci ve kurum aynı yetkilere ve aynı sorumluluklara sahip değildir; kullanıcı olmak tasarım kararlarının sorumlusu olmakla eşitlenmez. Bütün ilişkileri denetleyen mutlak bir merkez varsayılmaz. İnsanların makine olduğu veya teknik makinenin insan gibi bir özne olduğu yönünde bir iddia kurulmaz. Alanın özgünlüğü, mevcut mühendisliklerin yerine geçmesinde değil, hesaplama çevresindeki bağımlılıkları ve birlikte değişme koşullarını belirli bir odakta ele almasında aranır.

~~~text
  DUZENI O YAPAN, BILESENLERIN SAYISINDAN COK ARALARINDAKI ILISKILERDIR

          bilgisayarlar ------ yazilimlar ------ veriler
               |        \          |         /       |
               |         \         |        /        |
               |          [   FAALIYET   ]           |
               |         /         |        \        |
               |        /          |         \       |
            aglar ------------ insanlar ------- kurumlar

   bir isin yapilabilmesi sunlara bagli olabilir:
     baska sistemlerin calismasi . verinin anlasilmasi .
     erisim yetkileri . bakimin surmesi .
     sorumluluklarin yerine getirilmesi

   bagimliliklar anlam, karar, emek ve yukumluluk de tasir

  SUREKLILIK, CIHAZLARIN DEGISMEDEN KALMASINI GEREKTIRMEZ
    bir bilgisayar yenilenir ya da bir hizmet tasinir;
    gerekli iliskiler ve is yapabilme yetenegi korunur

  MUHENDISLIK NITELIGI  iliskiler uzerinde gerekceli ve
                        dogrulanabilir mudahaleler
    gereksinimleri aciklamak . bagimliliklari belirlemek .
    secenekleri karsilastirmak . arayuzleri ve yetkileri duzenlemek .
    arizalarin etkisini sinamak . degisikliklerin sonuclarini izlemek

  BU YAKLASIM SUNLARIN BASKA BIR ADI DEGILDIR
    tek bir cihaz . algoritma . yazilim urunu . yapay zeka sistemi
~~~

*Çizim 4 — Varlık: düzeni o yapan ilişkilerdir; süreklilik cihazların değişmeden kalması değildir.*

### Masaüstünde uygulama

**Girdi:** Tohum kaydında belirlenen faaliyet, kapsam ve kaynaklar.

1. Seçilen faaliyette rol alan dosyaları, uygulamaları, verileri, cihazları ve kişileri belirle. Her unsurun adıyla birlikte hangi işe katkıda bulunduğunu kaydet.
2. Teknik taşıyıcıyı, ilişkiler bütününü ve amaç ya da karar sorumlusunu ayrı açıkla. Bilinmeyen sorumluluğu bir kişiye varsayımla atama; belirsizliği yaz.
3. Bir bileşenin değişmesi veya kullanılamaması hâlinde faaliyetin hangi kısmının etkilenebileceğini değerlendir. İncelenmeyen olasılıkları gözlenmiş sonuçlardan ayır.
4. İncelenen düzenin tanımını bir paragrafta kur. İlgisiz unsurları dışarıda bırak; envanter ile tanımın aynı faaliyet hakkında olduğunu kontrol et.

### Çıktı ve tamamlanma ölçütü

**Çıktı:** `uygulama-kaydi.md` içindeki 1 bölümü; faaliyet tanımı, bileşen envanteri ve taşıyıcı–bütün–sorumlu taraf ayrımı.

**Tamamlanma ölçütü:** Kapsamdaki temel unsurların görevi ve bilinen sorumlulukları açıklanmıştır. Düzenin kimliği tek bir cihazla veya araç listesiyle eşitlenmez. Eksik envanter ya da belirsiz sorumluluk varsa hangi değerlendirmeyi sınırladığı belirtilmiştir.

## 2 Mekan Protokolü

**Kurucu sorular:** Nerededir? Bu yeri, oraya has bir yer yapan nelerdir? Neler değildir?

Bilgisayar Ekosistemi Mühendisliğinin çalışma yeri, bilgisayarlı faaliyetlerin gerçekleştiği fiziksel, teknik ve kurumsal ortam boyunca belirlenir. Bu ortamın cihazların bulunduğu bir konumu vardır; aynı zamanda verinin dolaştığı, yazılımların birbirine eriştiği, insanların karar verdiği ve sorumlulukların paylaşıldığı bir ilişkiler düzeni bulunur. Bir işin nerede gerçekleştiğini anlamak, onu mümkün kılan kaynakların, bağlantıların, yetkilerin ve bağımlılıkların nerede bulunduğunu da anlamayı gerektirir. Mekân, faaliyetin koşullarını ve müdahalenin sınırlarını belirleyen ortam olarak ele alınır.

Bu ortamın fiziksel boyutu hiçbir aşamada ortadan kalkmaz. Hesaplama, veri saklama ve iletişim; donanıma, enerjiye, bağlantılara, çalışma koşullarına ve bakım emeğine dayanır. Kullanıcının bir hizmete uzaktan erişmesi, hizmeti maddi koşullardan bağımsız kılmaz. Teknik boyutta arayüzler, veri biçimleri, iletişim kuralları, erişim yolları ve sistemler arasındaki sınırlar bulunur. Kurumsal boyut ise kaynaklara kimin erişebildiğini, hangi kararları kimin verebildiğini ve sorun çıktığında hangi tarafın ne yapacağını içerir. Bu boyutlar ayrı ayrı incelenebilir; gerçek çalışma düzeninde birbirlerinin koşullarını değiştirirler.

Bu yeri kendine özgü yapan temel özelliklerden biri, etkinin yayıldığı alan ile karar verme yetkisinin bulunduğu alanın her zaman çakışmamasıdır. Bir hizmet sağlayıcının yaptığı değişiklik, o karara katılmamış kullanıcıların veya başka kuruluşların çalışmalarını etkileyebilir. Bir verinin üretilme biçimi, onu başka bir yerde kullanan sistemin sonucunu değiştirebilir. Arayüzlerde teknik aktarımın yanında anlam, yetki, sorumluluk ve risk de taraflar arasında ilişkilendirilir. Ayrı ayrı çalışan parçaların birbirlerinden farklı şeyler beklemesi, ortak faaliyeti aksatabilir. Sistemler sistemi mimarisi üzerine çalışma da bileşenler arasında anlamlı iletişimi sağlayan standartların önemini vurgular. [3]

~~~text
  ORTAMIN UC BOYUTU  ayri ayri incelenebilir; gercek duzende
                     birbirlerinin kosullarini degistirirler

    FIZIKSEL   donanim . enerji . baglantilar . calisma kosullari .
               bakim emegi
               (hicbir asamada ortadan kalkmaz; uzaktan erisim,
                hizmeti maddi kosullardan bagimsiz kilmaz)
    TEKNIK     arayuzler . veri bicimleri . iletisim kurallari .
               erisim yollari . sistemler arasindaki sinirlar
    KURUMSAL   kaynaklara kim erisebilir . hangi karari kim verebilir .
               sorun cikinca hangi taraf ne yapar

  BU YERI OZGU KILAN  iki alan her zaman cakismaz

      etkinin yayildigi alan
    .--------------------------------------------------.
    |                                                  |
    |      .------------------------.                  |
    |      | karar verme yetkisinin |                  |
    |      | bulundugu alan         |                  |
    |      `------------------------'                  |
    |                          karara katilmamis       |
    |                          kullanicilar ve         |
    |                          baska kuruluslar        |
    `--------------------------------------------------'

    bir hizmet saglayicinin yaptigi degisiklik, o karara katilmamis
    kullanicilarin calismalarini etkileyebilir

  arayuzlerde teknik aktarimin yaninda anlam, yetki, sorumluluk ve
  risk de taraflar arasinda iliskilendirilir
~~~

*Çizim 5 — Mekan: ortamın üç boyutu; etkinin yayıldığı alan ile karar yetkisinin alanı.*

İncelemenin sınırı, ele alınan faaliyet ve onun gereksinimleriyle belirlenir. Doğrudan tasarlanabilen bölüm, anlaşmalar veya ortak kurallarla etkilenebilen bölüm ve dış koşul olarak izlenmesi gereken bölüm ayrılır. Bir bağımlılığın doğrudan kontrol edilemiyor olması, onun önemsiz olduğunu göstermez; fakat bütün davranışlarının belirlenebileceği de varsayılmaz. Kısmi kontrol altında çalışmak, hangi koşulların güvence altına alınabildiğini ve hangileri için uyarlama, yedekleme veya geçiş imkânı gerektiğini açıklamayı gerektirir. Faaliyetin amacı, katılımcıları ve bağımlılıkları değiştikçe inceleme sınırı yeniden değerlendirilebilir.

Bu ortam, kullanıcıların, geliştiricilerin, işletmecilerin ve kurumların aynı bütün içinde bulunmasına izin verir; onları aynı konuma yerleştirmez. Tarafların erişebildiği bilgiler, değiştirebildiği koşullar ve üstlenebileceği sorumluluklar farklı olabilir. Bir sistemin kullanımından etkilenmek, onun tasarımını değiştirme yetkisine sahip olmakla aynı değildir. Mekânı tanımlarken kimlerin bulunduğu kadar, kimin neye eriştiği, neyi değiştirebildiği ve hangi sonuçlardan sorumlu olduğu da ele alınır. Böylece sorumluluk, belirsiz bir bütünün içinde kaybolmadan izlenebilir.

Bu yer yalnızca internet, bulut, veri merkezi veya bir kurumun bilgi işlem birimi değildir. Bir kişinin bilgisayarlı çalışma ortamı da ilişkileri ve bağımlılıkları bakımından bu yaklaşımın konusu olabilir. Büyük bir teknoloji yığını, sırf büyüklüğü nedeniyle açıklayıcı bir ekosistem tanımı oluşturmaz. Mekân, fiziksel koşullardan kopmuş sınırsız bir dijital alan veya bütün kararların tek merkezden verildiği homojen bir düzen olarak kabul edilmez. İnceleme ölçeği, ele alınan faaliyeti anlamlı ölçüde etkileyen ilişkiler kadar genişletilir; her şeyin her şeye bağlı olduğu iddiası tek başına uygulanabilir bir sınırlandırma sağlamaz.

~~~text
  INCELEMENIN SINIRI ICINDE AYRILAN UC BOLUM

   .----------------------------------------------------------------.
   | DIS KOSUL OLARAK IZLENEN                                       |
   |                                                                |
   |   .--------------------------------------------------------.   |
   |   | ANLASMALARLA YA DA ORTAK KURALLARLA ETKILENEBILEN      |   |
   |   |                                                        |   |
   |   |    .-------------------------------.                   |   |
   |   |    | DOGRUDAN TASARLANABILEN       |                   |   |
   |   |    `-------------------------------'                   |   |
   |   `--------------------------------------------------------'   |
   `----------------------------------------------------------------'

   dogrudan kontrol edilemiyor   -x->   onemsiz
   dogrudan kontrol edilemiyor   -x->   butun davranislari
                                        belirlenebilir

   kismi kontrol altinda calismak sunlari aciklamayi gerektirir:
     hangi kosullar guvence altina alinabiliyor?
     hangileri icin uyarlama, yedekleme ya da gecis imkani gerekiyor?

  AYNI BUTUN ICINDE, AYRI KONUMLARDA
    kullanicilar . gelistiriciler . isletmeciler . kurumlar

    bir sistemin kullanimindan      =/=   onun tasarimini degistirme
    etkilenmek                            yetkisine sahip olmak

    kim neye erisiyor? . kim neyi degistirebiliyor? .
    kim hangi sonuclardan sorumlu?

  inceleme olcegi, ele alinan faaliyeti anlamli olcude etkileyen
  iliskiler kadar genisletilir
~~~

*Çizim 6 — Mekan: doğrudan tasarlanabilen, anlaşmayla etkilenebilen ve dış koşul olarak izlenen.*

### Masaüstünde uygulama

**Girdi:** Varlık kaydındaki bileşen envanteri ve seçilmiş çalışma alanı.

1. Dosyaların çalışma klasörüne göre konumunu, gerekli uygulamaları ve faaliyetin girdi ile çıktı yerlerini kaydet. Uzak bir kaynak gerekiyorsa bağlantısını ve erişim koşulunu belirt.
2. Bileşenler arasındaki veri, dosya, yetki ve hizmet bağımlılıklarını yaz. Dosyanın bulunduğu yer ile onu değiştirme yetkisini ayrı göster.
3. Her önemli bağımlılığı doğrudan tasarlanabilen, anlaşmayla etkilenebilen veya dış koşul olarak izlenen ilişki olarak değerlendir. Etkilenebilecek diğer dosyaları ya da tarafları belirt.
4. İş için gerekli yerel dosya ve bağlantıların mevcut olup olmadığını incele. Erişilemeyen veya kapsam dışında kalan kaynakları belirt; incelemeyi bütün bilgisayara yayma.

### Çıktı ve tamamlanma ölçütü

**Çıktı:** `uygulama-kaydi.md` içindeki 2 bölümü; konumlar, girdi ve çıktı yolları, bağımlılıklar, erişim koşulları ve müdahale sınırları.

**Tamamlanma ölçütü:** Hedeflenen faaliyetin gerekli girdilerinin nereden geldiği, çıktının nereye gittiği ve değişiklik yetkisinin nerede bulunduğu anlaşılırdır. Gözlenmeyen veya erişilemeyen bağlantılar çalışıyor kabul edilmez.

## 3 Usül Protokolü

**Kurucu sorular:** Nasıl işler yapar? Bu yaptıklarını, ona has yapan nelerdir? Neler değildir?

Bilgisayar Ekosistemi Mühendisliği, bilgisayarlı çalışma düzeninin nasıl kurulacağını, işletileceğini, değiştirileceğini ve gerektiğinde sona erdirileceğini ele alır. Çalışmasının başlangıcında, gerçekleştirilecek faaliyet ile onu mümkün kılan bağımlılıklar arasındaki ilişki bulunur. İhtiyacın teknik gereksinimlere çevrilmesi, gereksinimlerin bileşenler ve sorumlular arasında karşılık bulması, ortaya çıkan düzenin gerçek kullanımda sınanması ve edinilen bilgiyle düzeltilmesi birbirini tamamlayan işlerdir. Bilgisayar, işlemlerin teknik taşıyıcısıdır. İşlemlerin hangi koşullarda yapılacağını belirleyen, sonuçlarını değerlendiren ve kararlarının hesabını veren tarafların yetkisi ayrıca açıklanır.

Usulün kurulması, önce neyin başarı sayılacağının anlaşılmasını gerektirir. Hangi insanın hangi işi tamamlayabilmesi beklendiği, kabul edilebilir koşullar ve faaliyeti bozabilecek kesintiler veya yanlışlıklar belirlenir. Ardından sonuca etki eden cihazlar, yazılımlar, veriler, hizmetler, kullanıcılar ve kurumlar arasındaki ilişkiler incelenir. Amaçların farklılaştığı yerde ortak amaç varmış gibi davranılmaz; uyuşmazlıkların hangi yetkiyle ve hangi gerekçeyle ele alınacağı da çalışma düzeninin bir parçasıdır. Gereksinimlerin arkasındaki insan kararları ve bu kararların sınırları görünür tutulur.

Tasarım sırasında bağlantının kurulması kadar bağlantının anlamı da önem taşır. İki sistem aynı veriyi iletebilir, fakat farklı biçimde yorumlayabilir. Kayıtların eşlenmesi, bilginin hangi kaynaktan geldiğinin bilinmesi, bir işlemi kimin başlatabileceğinin belirlenmesi ve hatanın hangi sınırlar içinde tutulacağının kararlaştırılması birlikte değerlendirilir. Program, usulün çalıştırılabilir bir bölümünü taşır; verinin anlamı, değişiklik yetkisi, bakımın sürdürülmesi ve yanlış sonucun düzeltilmesi de çalışma usulüne dâhildir. İnsanlar arasındaki kuralların teknik karşılıkları kurulurken, kuralların gerekçeleri yalnızca koda bırakılmaz.

Kurulan düzen, bileşenlerin tek tek çalışmasının yanında ortak faaliyet açısından sınanır. Olağan koşullar, arıza durumu ve değişiklik sonrası davranış birlikte incelenir. Varsayımsal bir üniversite örneğinde öğrenci hesabının açılması, öğrencinin ders materyaline erişebildiğini tek başına göstermez. Kayıt bilgisinin aktarılması, doğru dersle eşleşmesi, erişim yetkisinin oluşması ve sorunun ilgili ekibe bildirilebilmesi de gerekir. Bir hizmet durduğunda veya bilgi geciktiğinde uygulanacak yol, sorumlusu ve kullanıcıya verilecek açıklama tasarımın içindedir. Güvenlik de bu işlerden ayrı bir son işlem olarak düşünülmez; NIST'in güvenilir ve güvenli sistemler rehberi, ilgili ilkelerin ve görevlerin yaşam döngüsü boyunca sistem mühendisliği çalışmalarına uygulanmasını öngörür. [4]

İşletim sırasında edinilen bilgi, düzeni değiştirebilmenin dayanağıdır. Hatalar, kesintiler, kullanıcı güçlükleri, destek yükü ve kaynak tüketimi, nedenleri ve etkileriyle birlikte değerlendirilir. Bir gösterge iyileşirken başka bir yerde sorun büyüyebilir; işlem süresinin kısalması, hataların veya insan emeğinin arttığı koşullarda tek başına başarı değildir. Düzeltme, gerektiğinde geri dönme, değişikliği durdurma ve kararın gerekçesini inceleme yolları korunur. Otomatik karar veren bileşenler de bu incelemeye dâhildir. Bir işlemin insan müdahalesi olmadan gerçekleşmesi, sonuçlarına ilişkin sorumluluk düzenini kendiliğinden ortadan kaldırmaz. Kullanım sonunda veri taşıma, sağlayıcı değiştirme ve hizmeti kapatma yolları da tasarımın zaman içindeki kapsamına girer.

~~~text
  BIRBIRINI TAMAMLAYAN ISLER

    ihtiyac  --->  teknik         --->  bilesenler ve  --->  gercek
                   gereksinimler        sorumlular           kullanimda
                                        arasinda             sinama
        ^                               karsilik                |
        |                                                       |
        `-----------  edinilen bilgiyle duzeltme  <-------------'

    once neyin basari sayilacagi anlasilir:
    hangi insanin hangi isi tamamlayabilmesi bekleniyor?

  BAGLANTININ KURULMASI KADAR ANLAMI DA ONEM TASIR

    sistem A  ----- ayni veri ----->  sistem B
    (bir bicimde yorumlar)            (baska bicimde yorumlayabilir)

  PROGRAM, USULUN CALISTIRILABILIR BIR BOLUMUNU TASIR
    calisma usulune ayrica dahil olanlar:
      verinin anlami . degisiklik yetkisi .
      bakimin surdurulmesi . yanlis sonucun duzeltilmesi
    kurallarin gerekceleri yalnizca koda birakilmaz

  ISLETIM SIRASINDA
    bir gosterge iyilesirken baska bir yerde sorun buyuyebilir
    korunan yollar:  duzeltme . geri donme . degisikligi durdurma .
                     kararin gerekcesini inceleme
    bir islemin insan mudahalesi olmadan gerceklesmesi, sonuclarina
    iliskin sorumluluk duzenini kendiliginden ortadan kaldirmaz
~~~

*Çizim 7 — Usül: birbirini tamamlayan işler; bağlantının anlamı; programın taşıdığı ve taşımadığı.*

Bu usulü ayırt eden, yalnızca burada kullanılan eşsiz araçların bulunması değildir. Programlama, test, sistem tasarımı, bakım ve izleme başka mühendislik çalışmalarında da yer alır. Özgün odak, bu işlerin ortak faaliyet, karşılıklı bağımlılıklar ve farklı sorumluluk alanları üzerinden birleştirilmesidir. Her bağlantı kurma işi veya her yazılım üretimi tek başına bu kapsamı karşılamaz; bunların her biri gerekli müdahale olabilir. Teknik kanıtın yerini yalnızca koordinasyon toplantıları alamaz. Çalışma her şeye hâkim tek uzman veya merkez gerektirmez; uzmanlıklar arasında alınan kararların sonuçlarını anlaşılır ve sınanabilir kılar. Basit bir düzenleme, gereksiz bir bağlantının kaldırılması veya bir işlem adımının sadeleştirilmesi yeterli çözüm olabilir.

~~~text
  VARSAYIMSAL UNIVERSITE ORNEGI

   ogrenci hesabi acildi
          |
          |     tek basina gostermez
          v
   ogrenci ders materyaline erisebiliyor  ?

   bunun icin ayrica gerekenler

    [1] kayit bilgisinin aktarilmasi
           |
    [2] dogru dersle eslesmesi
           |
    [3] erisim yetkisinin olusmasi
           |
    [4] sorunun ilgili ekibe bildirilebilmesi

   bir hizmet durdugunda ya da bilgi geciktiginde:
     uygulanacak yol . sorumlusu . kullaniciya verilecek aciklama
     tasarimin icindedir

  DUZEN, ORTAK FAALIYET ACISINDAN SINANIR
    bilesenlerin tek tek calismasi yetmez; birlikte incelenir:
      olagan kosullar . ariza durumu . degisiklik sonrasi davranis

  guvenlik, bu islerden ayri bir son islem olarak dusunulmez

  OZGUN ODAK  esiz araclar degil;
    islerin ortak faaliyet, karsilikli bagimliliklar ve farkli
    sorumluluk alanlari uzerinden birlestirilmesi
    teknik kanitin yerini yalnizca koordinasyon toplantilari alamaz
~~~

*Çizim 8 — Usül: üniversite örneği; hesabın açılması erişimi tek başına göstermez.*

### Masaüstünde uygulama

**Girdi:** Faaliyet tanımı, bağımlılık kaydı, 5 bölümünde önceden belirlenmiş başarı ölçütleri ve 4 bölümündeki uygulama zamanı ile geçiş koşulları.

1. Yapılacak işlemi, etkilenecek dosyaları ve beklenen sonucu açıkça yaz. Değişiklik gerektirmeyen bir inceleme yürütülüyorsa bunu belirt. Gerektiğinde önceki durumu geri kurmaya yetecek dosya kopyasını veya sürüm bilgisini koru.
2. Belirlenen işlemi seçilen çalışma alanında gerçekleştir. Beklenmeyen bir bağımlılık veya etki ortaya çıkarsa ilgili protokol kaydını güncellemeden işlemin kapsamını genişletme.
3. Hedeflenen işi gerekli girdiden nihai çıktıya kadar dene. Gereksinimle ilişkili bir arıza, gecikme veya geçiş riski varsa yalnızca o riski aydınlatacak denemeyi ekle.
4. Yapılan işlemle gözlenen sonucu ayrı yaz. Başarısız veya denenemeyen kısmı ve varsa geri dönüşü kaydet; bir dosyanın kaydedilmesini işin doğrulanmasıyla eşitleme.

### Çıktı ve tamamlanma ölçütü

**Çıktı:** `uygulama-kaydi.md` içindeki 3 bölümü; işlem adımları, değişen dosyalar, doğrulama gözlemleri, kanıt başvuruları ve açık kalan işler.

**Tamamlanma ölçütü:** Gerçekleştirilen iş ile beklenen davranış ayrılmıştır; doğrulandı denilen her sonuç bir gözleme dayanır. Deneme yapılmadıysa bu açıkça yazılır. Önceden belirlenen başarı ölçütü karşılanmadığında sonraki değerlendirmeye bu sonuç aktarılır.

## 4 Zaman Protokolü

**Kurucu sorular:** Hangi andadır? Bu anı, diğer zamanlardan farklı yapan nelerdir? Neler değildir?

Bilgisayar Ekosistemi Mühendisliğinin zamanı, insan faaliyetinin bilgisayarlı bir düzen içinde gerçekleştiği ve bu düzenin koşullarının değişebildiği zamandır. Başlangıç, kullanım, bakım, dönüşüm ve sona erdirme, bu zamanın farklı durumlarıdır. Çalışma yalnızca tasarım veya teslim anına yerleştirilmez. Belirli bir anın özgüllüğü, takvimdeki tarihinin yanında o anda geçerli ihtiyaçlardan, bağımlılıklardan, yetkilerden ve kısıtlardan doğar. Belirleyici olan, hangi faaliyetin sürdürüldüğü ve hangi değişikliklerin bu faaliyeti nasıl etkileyeceğidir.

Bu düzende tek bir zaman ölçeği bulunmaz. Bilgisayarın işlem süresi, insanın işi anlama ve tamamlama süresi, bir kurumun karar alma süresi ve altyapının yenilenme süresi farklı olabilir. Teknik taşıyıcı işlemlerin sırasını ve süresini düzenleyebilir; insan faaliyetinin zamanını bütünüyle belirlemez. Bir işlemin hızlı tamamlanması, kullanıcının sonucu anlayabildiğini veya gerekli işi bitirebildiğini göstermez. Bir kararın verilmiş olması da onu uygulayacak bütün bileşenlerin hazır olduğu anlamına gelmez. Farklı sürelerin ortak faaliyete etkisi ve bunlar arasındaki uyum ihtiyacı, mühendislik konusu olarak ele alınır.

Belirli bir anı değerlendirmek, geçmişten devralınan koşulları değerlendirmeyi de gerektirir. Veri biçimleri, eski uygulamalar, alışkanlıklar, sözleşmeler ve daha önce verilmiş kararlar bugünün seçeneklerini etkiler. Bu miras, geçmişteki her koşulun korunmasını zorunlu kılmaz; fakat bir değişikliğin yalnızca yeni bileşenin özelliklerine bakılarak kararlaştırılmasını yetersiz kılar. Geçişin sırası, eski ve yeni düzenin birlikte çalışma koşulları, kullanıcıların hazırlığı ve başarısızlık hâlinde geri dönülebilecek durum incelenir. Geçiş dönemi, son duruma ulaşıncaya kadar katlanılan belirsiz bir ara olarak bırakılmaz; kendi koşullarıyla tasarlanır.

Bir müdahalenin teknik olarak yapılabilir olması, her anda yapılmasının uygun olduğunu göstermez. Ders erişimini sağlayan bir hizmetteki değişiklik, sınav döneminde farklı sonuçlar doğurabilir. Aynı müdahalenin kabul edilebilirliği, faaliyet yoğunluğuna, destek kapasitesine, geri dönüş olanağına ve kesintinin etkisine göre değişir. Bazı koşullar bilgisayarlar tarafından izlenebilir ve tanımlanmış kurallarla değerlendirilebilir. Hangi etkilerin öncelikli sayılacağı, hangi risklerin kimin adına kabul edileceği ve kararın kim tarafından değiştirilebileceği ise yetki ve sorumluluk düzeninde açıklanır.

Sonuçlar farklı sürelerde ortaya çıkabilir. Bugün kolaylık sağlayan bir seçim, ileride bakım yükünü veya bir sağlayıcıya bağımlılığı artırabilir. Bugün ek emek isteyen bir düzenleme, sonraki değişiklikleri kolaylaştırabilir. Bu olasılıklar kesin gelecek bilgisi olarak sunulmaz; kanıt, varsayım ve belirsizlikleriyle değerlendirilir. Süreklilik değişmezlik olarak anlaşılmaz. Korunacak olanın aynı cihaz mı, aynı veri mi, hizmet düzeyi mi veya insanların iş yapabilme yeteneği mi olduğu belirlenir. Bir faaliyetin devamı bazen bileşenin değiştirilmesini, bir ilişkinin sona erdirilmesini veya bir hizmetin kontrollü biçimde kapatılmasını gerektirebilir.

Bu zaman anlayışı yalnızca güncel bir teknolojiye veya yapay zekâya bağlanmaz. İnternet mimarisine ilişkin 1996 tarihli RFC 1958 de sürekli değişimi ve mevcut yapı kullanılırken yenilenmesini ele alır; süreklilik içinde dönüşüm sorunu daha eski bir mühendislik meselesidir. [5] Zaman Protokolü her yeniliğin hemen benimsenmesini veya bütün değişikliklerin ertelenmesini gerektirmez. Değişiklik yapmak kadar yapmamak da gerekçesi ve etkileriyle değerlendirilir. İnceleme, bağımlılıkların sonuçları görünür olduktan sonra başlayabileceği gibi, gelecekteki seçenekleri etkileyen bağımlılıklar henüz kurulurken de yapılır.

~~~text
  TEK BIR ZAMAN OLCEGI YOKTUR

    bilgisayarin islem suresi                |=|
    insanin isi anlama ve tamamlama suresi   |=======|
    kurumun karar alma suresi                |=================|
    altyapinin yenilenme suresi              |=========================|

    bir islemin hizli tamamlanmasi  -x->  kullanicinin sonucu anlamasi
    bir kararin verilmis olmasi     -x->  butun bilesenlerin hazir
                                          olmasi

  ZAMANIN FARKLI DURUMLARI
    baslangic . kullanim . bakim . donusum . sona erdirme

  GECIS DONEMI KENDI KOSULLARIYLA TASARLANIR

    eski duzen  ============================|
                              |<- birlikte ->|
    yeni duzen                |===============================>
                                  geri donulebilecek durum belli

  AYNI MUDAHALE, FARKLI ANDA FARKLI SONUC
    ders erisimini saglayan hizmetteki degisiklik, sinav doneminde
    farkli sonuclar dogurabilir
    kabul edilebilirlik sunlara gore degisir:
      faaliyet yogunlugu . destek kapasitesi .
      geri donus olanagi . kesintinin etkisi

  SUREKLILIK, DEGISMEZLIK DEGILDIR  korunacak olan hangisi?
    ayni cihaz | ayni veri | hizmet duzeyi |
    insanlarin is yapabilme yetenegi

  degisiklik yapmak kadar yapmamak da gerekcesi ve etkileriyle
  degerlendirilir
~~~

*Çizim 9 — Zaman: dört ayrı süre; geçiş dönemi; aynı müdahalenin farklı anda farklı sonucu.*

### Masaüstünde uygulama

**Girdi:** Mevcut durum, planlanan işlem, devam eden faaliyetler ve değişim gereksinimi.

1. 3 bölümündeki işlem uygulanmadan önce uygun çalışma anını ve etkilenebilecek devam eden işleri belirle. Gerekli hazırlığı, bağımlı işlemlerin sırasını ve varsa geçiş koşullarını yaz.
2. Eski ve yeni düzen bir süre birlikte bulunacaksa hangi dosyanın veya sürümün esas alınacağını belirt. Önceki duruma dönmek gerekecekse bunun hangi koşulda yapılacağını kaydet.
3. Uygulamadan sonra başlangıç ve bitiş zamanını, gerçekleşen sırayı ve planlanan sıradan sapmaları yaz. Gerçek süreyi ölçmediysen yaklaşık değerlendirmeyi ölçüm olarak sunma.
4. Henüz gözlenmemiş etkileri ve gerektiğinde yeniden değerlendirme yapılacak koşulu belirt. Geleceğe ilişkin beklentiyi mevcut sonuçtan ayır.

### Çıktı ve tamamlanma ölçütü

**Çıktı:** `uygulama-kaydi.md` içindeki 4 bölümü; uygulama öncesi zaman ve geçiş planı ile uygulama sonrası gerçekleşme kaydı.

**Tamamlanma ölçütü:** İşlem sırası ve geçiş koşulları uygulanmadan önce açıklanmış, gerçekleşen zaman bilgisi sonrasında eklenmiştir. Uzun vadeli etkiler gözlenmediyse kesinleşmiş sayılmaz; yeniden inceleme koşulu belirtilir.

## 5 Gaye Protokolü

**Kurucu sorular:** Hangi nihai amaca hizmet eder? Bu nihai amaca ulaştıran nelerdir? Neler değildir?

Bilgisayar Ekosistemi Mühendisliğinin hizmet edeceği nihai amaç, bilgisayarın varlığından veya ekosistemin teknik yapısından kendiliğinden çıkmaz. Aynı türden çalışma düzeni farklı amaçlarla kurulabilir. Alanın ne olduğunu belirleyen kurucu özelliklerle, nasıl kullanılması gerektiğine ilişkin değer tercihleri ayrı tutulur. Bir düzenin etkili işlemesi, amacının haklı veya sonuçlarının kabul edilebilir olduğunu tek başına göstermez. Kullanıcı, geliştirici, işletmeci ve sağlayıcı farklı sonuçlar isteyebilir. Amaçların kim tarafından belirlendiği, kimleri etkilediği ve hangi gerekçelerle savunulduğu görünür kılınır.

Önerilen nihai gaye, insanların ve toplulukların değer verdikleri faaliyetleri güvenilir, erişilebilir ve sürdürülebilir biçimde gerçekleştirebilmelerini; koşullar değiştiğinde bu yeteneği koruyabilmelerini ve kullandıkları düzeni anlayabilmelerini, denetleyebilmelerini ve gerektiğinde değiştirebilmelerini sağlamaktır. Bu, teknik tanımdan zorunlu olarak türetilmiş bir sonuç değil, açıkça benimsenmesi önerilen bir değer yönelimidir. Hesaplama gücü, veri hacmi ve hizmet sayısı, bu amaca katkıları ölçüsünde anlam kazanır. Teknik kapasitenin büyümesi, insanların fiilen yararlanabildiği olanakların aynı ölçüde büyüdüğünü göstermez.

Bu gayeye ulaşmak, teknik işleyiş ile kurumsal sorumluluğun birlikte kurulmasını gerektirir. Doğru veriyle çalışma, uygun erişim yetkileri, arızalara karşı hazırlık, bakım yapılabilirlik ve değişikliklerin sınanması güvenilirliği destekler. Açık sorumluluklar, erişilebilir destek ve anlaşılır açıklamalar ise düzenin insanlar açısından kullanılabilir olmasına katkı verir. İnsanların sorunları bildirebilmesi, yanlışların düzeltilmesi ve gerektiğinde başka bir düzenle çalışılabilmesi önem taşır. Bu unsurların hiçbiri tek başına nihai amacı güvence altına almaz. Gaye, tasarım başlangıcında yazılan bir beyan olarak bırakılmaz; kullanımda ortaya çıkan sonuçlarla yeniden değerlendirilir.

Amaç ve sorumluluk taşıyan tarafların insanlar ve kurumlar olması, herkesin aynı yetkiye veya aynı sorumluluğa sahip olduğu anlamına gelmez. Tasarımı belirleyen, kaynak ayıran, hizmeti işleten, kullanım koşullarını koyan ve sistemi kullanan taraflar farklı konumlardadır. Bir kullanıcının denetleyemediği altyapı kararlarının hesabı ona yüklenemez; karar yetkisi olanların sorumluluğu da işlemin otomatik gerçekleşmesiyle ortadan kalkmaz. Makine alt hedefler seçebilir, işlemleri sıralayabilir ve belirlenmiş sınırlar içinde karar verebilir. Bir hedefi gerçekleştirmek ile o hedefin neden değerli olduğunu gerekçelendirmek ayrı tutulur. Teknik etkinlik, nihai gayenin kendiliğinden meşruiyet kaynağı değildir.

Gayeye yaklaşma, tek bir başarı göstergesiyle açıklanmaz. İşin tamamlanabilmesi, kesintiden sonra toparlanma, farklı gereksinimlerle erişim, bakım yükü, fiziksel kaynak kullanımı ve değişiklik yapabilme olanağı birlikte ele alınır. Yararların ve yüklerin kimler arasında dağıldığı da değerlendirilir. Bir kurumun maliyetinin azalması, kullanıcıların güçlüğü veya emeği artarak sağlanıyorsa yalnızca kurumun hesabına bakılmaz. Ölçütler arasında çatışma olabilir; hepsinin her koşulda aynı anda en üst düzeye çıkarılacağı sözü verilmez. Tercihlerin gerekçeleri, etkileri ve sorumluları açık tutulur. IAB'nin RFC 8890 belgesi de internet standartlarına ilişkin kararlarda son kullanıcılarla diğer tarafların çıkarlarının çatışabileceğini tartışır ve kullanıcı çıkarlarına öncelik verilmesini savunur. Bu belge, teknik kararların kime hizmet ettiğinin açıkça ele alınabileceğine bir dayanak sağlar. [6]

Nihai amaç, daha fazla bilgisayar kullanmak, her işi otomatikleştirmek, bütün verileri toplamak veya ekosistemi sürekli büyütmek değildir. Bunlar belirli bir faaliyete gerekçeli katkı sağladıklarında araç olabilir. Bütün kararların tek merkezde toplanması, belirli bir mimarinin koşulsuz üstün sayılması veya insanın mevcut teknik düzene bütünüyle uyarlanması da önerilen gayenin kendisi değildir. Bir bileşenin azaltılması, otomasyonun sınırlandırılması, bir bağımlılığın kaldırılması veya bir hizmetten vazgeçilmesi amaca hizmet edebilir. Mühendislik başarısı, düzenin çalışmasıyla birlikte, kimin hangi faaliyetini hangi koşullarda mümkün kıldığı üzerinden değerlendirilir.

~~~text
  ONERILEN NIHAI GAYE  (teknik tanimdan zorunlu olarak cikmaz;
                        acikca benimsenmesi onerilen bir deger yonelimi)

    insanlar ve topluluklar, deger verdikleri faaliyetleri
      1  guvenilir, erisilebilir ve surdurulebilir bicimde
         gerceklestirebilsin
      2  kosullar degistiginde bu yetenegi koruyabilsin
      3  kullandiklari duzeni anlayabilsin, denetleyebilsin ve
         gerektiginde degistirebilsin

  FARKLI KONUMLAR  ayni yetki, ayni sorumluluk degil
    tasarimi belirleyen . kaynak ayiran . hizmeti isleten .
    kullanim kosullarini koyan . sistemi kullanan

    kullanicinin denetleyemedigi altyapi kararlarinin hesabi ona
    yuklenemez; karar yetkisi olanlarin sorumlulugu da islemin
    otomatik gerceklesmesiyle ortadan kalkmaz

    bir hedefi gerceklestirmek   =/=   o hedefin neden degerli
                                       oldugunu gerekcelendirmek

  TEK BIR BASARI GOSTERGESI YOKTUR  birlikte ele alinir
    isin tamamlanabilmesi . kesintiden sonra toparlanma .
    farkli gereksinimlerle erisim . bakim yuku .
    fiziksel kaynak kullanimi . degisiklik yapabilme olanagi
    yararlar ve yukler kimler arasinda dagiliyor?

  NIHAI AMAC DEGILDIR
    daha fazla bilgisayar kullanmak . her isi otomatiklestirmek .
    butun verileri toplamak . ekosistemi surekli buyutmek
~~~

*Çizim 10 — Gaye: önerilen nihai gaye; farklı konumlar; birlikte ele alınan göstergeler.*

### Masaüstünde uygulama

**Girdi:** Başlangıç niyeti, desteklenecek insan faaliyeti, ilgili taraflar ve uygulama sonrasında fiilen elde edilen sonuçlar.

1. İşlem uygulanmadan önce kimin hangi işi yapabilmesinin amaçlandığını yaz. Amacı değerlendirecek gözlenebilir başarı ölçütünü belirle; varsa kabul edilebilir sınırı somut göreve göre açıkla.
2. Yararın ve yükün kimlere dağıldığını, tercih yapma yetkisinin kimde bulunduğunu belirt. Amaçlar çatışıyorsa yapılan tercihi gerekçesiyle kaydet.
3. Uygulama sonrasında başlangıç hedefini gözlenen sonuçla karşılaştır. İşin tamamlanmasını, kullanım güçlüğünü ve somut görev bakımından önemli bakım, kaynak veya değişim etkilerini değerlendir.
4. Hedefin karşılanma durumunu ve dayanağını yaz. Yapılmayan ölçümü veya gözlenmeyen yararı başarı kanıtı sayma; değişiklik, sadeleştirme ya da vazgeçme önerisi varsa gerekçesini belirt.

### Çıktı ve tamamlanma ölçütü

**Çıktı:** `uygulama-kaydi.md` içindeki 5 bölümü; uygulama öncesi amaç ve başarı ölçütleri ile uygulama sonrası sonuç değerlendirmesi.

**Tamamlanma ölçütü:** Hedef, gözlem ve değerlendirme birbirinden ayrılmıştır. Sonuç karşılandı, kısmen karşılandı, karşılanmadı veya değerlendirilmedi olarak dayanağıyla belirtilmiştir. Teknik işlemin tamamlanması tek başına insan açısından yarar kanıtı sayılmaz.

## 6 Kökleşme (Bitiş) Protokolü

**Protokol soruları:** Beş protokol birlikte hangi çerçeveyi kurdu? Başlangıç sorularından hangileri karşılandı? Hangi kararlar ve sonuçlar dayanaklandırıldı? Neler açık kaldı? Bu çalışma hangi durumuyla tamamlanıyor?

Kökleşme Protokolü, Varlık, Mekan, Usül, Zaman ve Gaye protokollerinde oluşan açıklamaları aynı çalışma düzeni bakımından bir araya getirir. Bölümlerin birbirini destekleyip desteklemediğini ve aynı kavramları tutarlı biçimde kullanıp kullanmadığını değerlendirir. Teknik taşıyıcı olarak bilgisayar, ilişkilerin oluşturduğu bütün olarak ekosistem ve amaçla sorumluluğu taşıyan taraflar arasındaki ayrımlar kapanışta da korunur.

Bu değerlendirme, Tohum Protokolü'nde kaydedilen soruya geri döner. Başlangıçta ele alınması amaçlanan konu ile çalışma sonucunda açıklanan veya değiştirilen konu karşılaştırılır. Kapsamın değiştiği, bir kabulün düzeltildiği veya başka bir sorunun öne çıktığı durumlar gerekçeleriyle kaydedilir. Başlangıçtaki ifadelerin aynen onaylanması zorunlu değildir. Hangi sonuca hangi dayanaklarla ulaşıldığı ve başlangıca göre nelerin değiştiği anlaşılır olmalıdır.

Kapanışta açıklama, karar ve gerçekleşmiş sonuç birbirinden ayrılır. Bir ilişkinin tarif edilmesi, o ilişkinin uygulamada değiştirildiğini göstermez. Bir yöntemin yazılması, yöntemin uygulanıp sınandığı anlamına gelmez. Kavramsal belgenin tamamlanması ile incelenen masaüstü çalışma düzeninin değiştirilmesi ayrı sonuçlardır. Gerçekleştirilen işlemler, gözlenen etkiler ve henüz uygulanmamış öneriler kendi durumlarıyla kaydedilir.

Açık kalan konular kapanışın dışında bırakılmaz. Cevapsız bir soru, yapılmamış bir ölçüm veya doğrudan denetlenemeyen bir bağımlılık belirtilir; bunların sonucun kullanılabilirliği bakımından anlamı açıklanır. Sonucun geçerli olduğu kapsam, dayanakların izin verdiğinden geniş gösterilmez. Bir açık konu hedeflenen sonucu değerlendirmeyi engelliyorsa başarı doğrulanmış sayılmaz. Çalışma aşaması bu eksiklik açıkça belirtilerek durdurulabilir veya belirlenmiş kapsamıyla kapatılabilir; kapanış kararı ile hedefin gerçekleşmesi aynı hüküm değildir.

Bitiş, bu çalışma aşamasının belirli bir durumuyla tamamlanmasıdır. Son metin, ilgili kayıtlar ve varsa uygulama kanıtları yeniden açılabilir ve izlenebilir biçimde bir araya getirilir. Düzenin yeniden ele alınmasını gerektirebilecek koşullar kaydedilir. Faaliyetin değişmesi, yeni bir bağımlılığın ortaya çıkması veya gözlenen bir sonucun mevcut açıklamayla uyuşmaması böyle bir koşul olabilir. Yeniden değerlendirme ihtimali, sürekli çalışma veya otomatik kapsam genişletme yükümlülüğü oluşturmaz.

Kökleşme, mevcut düzenin değişmez olduğunu veya bütün soruların kesin biçimde çözüldüğünü ilan etmez. Beş bölümün özetlenmesiyle de sınırlı değildir. Bölümlerin ilişkisini, ulaşılan sonucun dayanaklarını ve kapanış durumunu açıklar. Bir sistemi kullanmaya devam etmek, değiştirmek, sadeleştirmek veya işlevini tamamlamış bir hizmeti sona erdirmek, gerekçesine göre bu kapanışın sonucu olabilir.

~~~text
  KAPANISTA AYRILAN UC SEY
    aciklama | karar | gerceklesmis sonuc

    bir iliskinin tarif edilmesi    -x->   uygulamada degistirilmesi
    bir yontemin yazilmasi          -x->   uygulanip sinanmasi
    kavramsal belgenin              -x->   incelenen calisma duzeninin
    tamamlanmasi                           degistirilmesi

  IKI AYRI HUKUM

                             HEDEFIN KARSILANMA DURUMU
                             karsilandi | kismen karsilandi |
                             karsilanmadi | degerlendirilmedi
   KAPANIS KARARI
   kapatildi          --->   bu dort durumdan herhangi biriyle
   durduruldu         --->   birlikte yazilabilir

    bir acik konu, hedeflenen sonucu degerlendirmeyi engelliyorsa
    basari dogrulanmis sayilmaz

  BASLANGICA GERI DONULUR
    baslangictaki ifadelerin aynen onaylanmasi zorunlu degildir;
    kapsamin degistigi, bir kabulun duzeltildigi ya da baska bir
    sorunun one ciktigi durumlar gerekceleriyle kaydedilir

  YENIDEN ELE ALMA KOSULLARI
    faaliyetin degismesi . yeni bir bagimliligin ortaya cikmasi .
    gozlenen bir sonucun mevcut aciklamayla uyusmamasi

  KAPANISIN SONUCU OLABILENLER
    kullanmaya devam etmek . degistirmek . sadelestirmek .
    islevini tamamlamis bir hizmeti sona erdirmek
~~~

*Çizim 11 — Kökleşme: açıklama, karar ve gerçekleşmiş sonuç; kapanış kararı ile hedefin durumu ayrıdır.*

### Masaüstünde uygulama

**Girdi:** `uygulama-kaydi.md` dosyasının 0–5 bölümleri, üretilen dosyalar ve varsa uygulama kanıtları.

1. Başlangıç kaydıyla beş protokolün çıktısını birlikte oku. Aynı faaliyet, bileşen, kişi ve sorumluluk için kullanılan adların ve anlamların tutarlılığını denetle.
2. Başlangıç sorularının karşılıklarını, değişen kabulleri ve kapsam düzenlemelerini 6 bölümüne yaz. Uyuşmazlıkları gider veya sonuç üzerindeki etkileriyle açık bırak.
3. Gerçekleştirilmiş işlemleri, gözlenen sonuçları, uygulanmamış önerileri ve açık soruları ayır. İlgili dosyalara ya da kayıt girdilerine başvuru ver; hedefin karşılanma durumunu kanıta göre belirt.
4. Son dosyaları yeniden aç; çalışma alanındaki gerekli yerel bağlantıları ve kayıtların okunabilirliğini kontrol et. Kapanış kararını, açık konuların durumunu, varsa devam edecek işi ve yeniden ele alma koşulunu kaydet.

### Çıktı ve tamamlanma ölçütü

**Çıktı:** `uygulama-kaydi.md` içindeki 6 bölümü; başlangıca göre değişiklikler, dayanaklandırılmış sonuçlar, son dosyalar, açık konular ve kapanış kararı.

**Tamamlanma ölçütü:** Kaydı okuyan biri çalışmanın neyi kurduğunu, neyin gerçekten gerçekleştirildiğini, hedefin hangi ölçüde karşılandığını ve nelerin açık kaldığını ayırt edebilir. Kapanış durumu ile başarı durumu ayrı yazılmıştır. Son dosyalar ve bilinen sınırlamalar izlenebilir; uygulanmamış işler tamamlanmış gösterilmez.

## Varsayımsal masaüstü uygulama örneği

Bir çalışma klasöründe `notlar.md` dosyasının `kaynaklar/okuma.pdf` dosyasına bağlantı vermesi örnek alınabilir. Başlangıç ihtiyacı, not içindeki bağlantıdan doğru kaynak belgeye ulaşabilmektir. Bu örnek, protokolün nasıl kayda geçirileceğini gösterir; gerçek bir bilgisayarda yapılmış işlem olarak sunulmaz.

Varlık kaydında not dosyası, kaynak PDF, kullanılan görüntüleyici ve işi yapan kişi belirlenir. Mekan kaydında iki dosyanın çalışma klasörüne göre konumu ve aralarındaki bağlantı açıklanır. Gaye kaydında başarı ölçütü, bağlantının seçilen görüntüleyicide beklenen kaynak belgeyi açması olarak belirlenir. Zaman kaydında dosyanın başka bir iş tarafından değiştirilmediği uygun bir çalışma anı seçilir ve önceki içeriğe dönme yolu açıklanır.

Usül kaydında beklenen sonuç, yapılacak işlemden ayrı yazılır. Bağlantı hedefinin düzenlenmesi gerçekleştirilmiş işlem olabilir; doğrulama ise bağlantının açılması ve beklenen belge başlığının görülmesiyle desteklenir. Yalnızca Markdown içinde bağlantı metninin bulunması, hedef belgenin doğru açıldığının kanıtı değildir. Başka bir görüntüleyicide denenmediyse sonuç o uygulamaya genellenmez. Kökleşme kaydı, değişen dosyayı, gözlemi, bu sınırı ve kapanış kararını bir araya getirir.

~~~text
  VARSAYIMSAL ORNEK  (gercek bir bilgisayarda yapilmis islem degildir)

   <calisma-klasoru>/
     notlar.md  ------------- baglanti ------------>  kaynaklar/
                                                         okuma.pdf
   ihtiyac: not icindeki baglantidan dogru kaynak belgeye ulasabilmek

  PROTOKOLLERE GORE KAYIT
    1 Varlik    not dosyasi, kaynak PDF, kullanilan goruntuleyici,
                isi yapan kisi
    2 Mekan     iki dosyanin calisma klasorune gore konumu ve
                aralarindaki baglanti
    5 Gaye      basari olcutu: baglanti, secilen goruntuleyicide
                beklenen kaynak belgeyi acar
    4 Zaman     dosyanin baska bir is tarafindan degistirilmedigi
                uygun bir calisma ani; onceki icerige donme yolu
    3 Usul      beklenen sonuc, yapilacak islemden ayri yazilir
                islem:      baglanti hedefinin duzenlenmesi
                dogrulama:  baglantinin acilmasi ve beklenen belge
                            basliginin gorulmesi
    6 Koklesme  degisen dosya, gozlem, sinir ve kapanis karari

  KANIT DEGILDIR
    Markdown icinde baglanti      -x->   hedef belgenin dogru
    metninin bulunmasi                   acilmasi

  SINIR
    baska bir goruntuleyicide denenmediyse sonuc o uygulamaya
    genellenmez
~~~

*Çizim 12 — Varsayımsal örnek: bir bağlantının altı protokole göre kaydı.*

## Uygulama kaydı şablonu

Aşağıdaki metni çalışma klasöründe `uygulama-kaydi.md` adıyla ayrı dosyaya kaydet ve fiilî çalışma sırasında doldur. Bu şablondaki boş alanlar protokol metninin eksikliği değil, her yeni çalışmaya ait bilgilerin yazılacağı alanlardır.

```markdown
# Uygulama Kaydı

Bu dosya, protokollerin belirli bir çalışma üzerinde uygulanması sırasında doldurulur. Boş alanlar henüz kayıt girilmediğini gösterir. Başlangıçta herhangi bir işlem yapılmış veya sonuç doğrulanmış kabul edilmez.

**Çalışma adı:** —

**Çalışma klasörü:** —

**Kaydı tutan kişi veya yardımcı:** —

**Başlangıç tarihi:** —

**Son güncelleme:** —

**Çalışma durumu:** Başlatılmadı

**Hedefin karşılanma durumu:** Değerlendirilmedi

## 0 Tohum (Başlangıç) Protokolü

**Başlangıç sorusu ve ihtiyaç:** —

**Çalışmayı başlatma niyeti:** —

**İlk durum ve yaşanan güçlük:** —

**Kapsama dâhil olanlar:** —

**Kapsam dışında kalanlar:** —

**Kaynaklar ve konumları:** —

**Bilinenler ve dayanakları:** —

**Henüz doğrulanmamış kabuller:** —

**Açık sorular:** —

## 1 Varlık Protokolü

**İncelenen düzenin tanımı:** —

**Bileşen envanteri:** Her önemli unsur için adı, türü, görevi ve bilinen sorumlusu yazılır. —

**Teknik taşıyıcı:** —

**İlişkilerin oluşturduğu bütün:** —

**Amaç ve karar sorumluları:** —

**Değişebilecek bileşenler ve korunması gereken yetenek:** —

**Eksikler ve değerlendirmeyi sınırlayan belirsizlikler:** —

## 2 Mekan Protokolü

**Girdi konumları:** —

**Çıktı konumları:** —

**Önemli bağımlılıklar:** Her ilişki için kaynak, hedef, taşınan veri veya işlev ve erişim koşulu yazılır. —

**Doğrudan tasarlanabilen alan:** —

**Anlaşmayla etkilenebilen alan:** —

**Dış koşul olarak izlenen alan:** —

**Etkilenebilecek diğer dosyalar veya taraflar:** —

**Erişilemeyen veya incelenmeyen kaynaklar:** —

## 3 Usül Protokolü

**Planlanan işlem ve etkilenecek dosyalar:** —

**Başarı ölçütüne başvuru:** 5 bölümündeki uygulama öncesi kayıt. —

**Zaman ve geçiş koşullarına başvuru:** 4 bölümündeki uygulama öncesi kayıt. —

**Önceki durumun korunma veya geri kurulma yolu:** —

**İşlem ve gözlem kaydı:** Aşağıdaki girdiyi gerçekleştirilen her anlamlı işlem için çoğalt.

### İşlem girdisi

- Tarih ve varsa saat: —
- İlgili dosya veya bileşen: —
- Beklenen sonuç: —
- Gerçekleştirilen işlem: Henüz uygulanmadı.
- Gözlenen sonuç: Henüz gözlenmedi.
- Doğrulama yolu ve varsa kanıt dosyası: —
- Durum: Planlandı / Uygulandı / Doğrulandı seçeneklerinden gerçekleşen durumu yaz.
- Denenmeyen veya açık kalan kısım: —
- Varsa geri dönüş ya da düzeltme: —

## 4 Zaman Protokolü

### Uygulama öncesi

**Uygun çalışma anı ve gerekçesi:** —

**Etkilenebilecek devam eden işler:** —

**İşlem sırası ve bağımlı adımlar:** —

**Geçişte esas alınacak dosya veya sürüm:** —

**Varsa geri dönüş koşulu:** —

### Uygulama sonrası

**Gerçek başlangıç ve bitiş:** —

**Planlanan sıradan sapmalar:** —

**Henüz gözlenmemiş etkiler:** —

**Yeniden ele alma koşulu:** —

## 5 Gaye Protokolü

### Uygulama öncesi

**Kimin hangi faaliyeti desteklenecek:** —

**Amaç ve gerekçesi:** —

**Gözlenebilir başarı ölçütü:** —

**Varsa kabul edilebilir sınır:** —

**İlgili taraflar ve tercih yapma yetkisi:** —

### Uygulama sonrası

**Hedefle karşılaştırılan gözlem:** —

**Sağlanan yarar ve oluşan yük:** —

**Bakım, kaynak kullanımı veya değişebilirlik açısından önemli etki:** —

**Hedefin karşılanma durumu:** Değerlendirilmedi

**Değerlendirmenin dayanağı ve sınırı:** —

**Varsa değişiklik, sadeleştirme veya vazgeçme önerisi:** —

## 6 Kökleşme (Bitiş) Protokolü

**Başlangıç sorularının karşılıkları:** —

**Değişen kabuller veya kapsam:** —

**Bölümler arasındaki tutarlılık ve varsa uyuşmazlık:** —

**Gerçekleştirilen işler ve doğrulanan sonuçlar:** —

**Uygulanmamış öneriler:** —

**Açık konular ve sonuca etkileri:** —

**Son dosyalar ve konumları:** —

**Son dosyaları yeniden açma ve gerekli yerel bağlantıları kontrol etme sonucu:** Henüz yapılmadı.

**Varsa devam edecek iş ve bilinen sorumlusu:** —

**Yeniden değerlendirme koşulu:** —

**Hedefin karşılanma durumu:** Değerlendirilmedi

**Çalışmanın kapanış kararı ve gerekçesi:** Henüz kapanmadı.

**Kapanış tarihi ve kararı kaydeden kişi:** —
```

## Kaynaklar

[1] INCOSE. About Systems Engineering (https://www.incose.org/About%20Systems%20Engineering/). Sistem tanımı, bileşenler arası ilişkiler ve yaşam döngüsü yaklaşımı.

[2] Jansen, S., Finkelstein, A. ve Brinkkemper, S. (2009). A Sense of Community: A Research Agenda for Software Ecosystems (https://slingerjansen.nl/wp-content/uploads/2009/04/ssnniericse.pdf). Yazılım ekosistemlerinde teknik ürünler ve aktörler arasındaki ilişkiler.

[3] Maier, M. W. (1998). Architecting Principles for Systems-of-Systems (https://doi.org/10.1002/(SICI)1520-6858(1998)1:4%3C267::AID-SYS3%3E3.0.CO;2-D). Systems Engineering, 1(4), 267–284. Bileşenler arasında anlamlı iletişim ve mimari.

[4] NIST (2022). Engineering Trustworthy Secure Systems (https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final). SP 800-160 Vol. 1 Rev. 1. Güvenliğin sistem mühendisliği yaşam döngüsünde ele alınması.

[5] Carpenter, B., ed. (1996). Architectural Principles of the Internet (https://www.rfc-editor.org/rfc/rfc1958.html). RFC 1958. Sürekli değişim ve kullanım devam ederken yenilenme.

[6] Nottingham, M. (2020). The Internet is for End Users (https://www.rfc-editor.org/rfc/rfc8890.html). RFC 8890. Teknik kararların kullanıcılar üzerindeki etkisi ve çıkar çatışmaları.

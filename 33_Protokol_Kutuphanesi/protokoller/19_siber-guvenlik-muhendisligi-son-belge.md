# Siber Güvenlik Mühendisliği

**Tohumdan Kökleşmeye Masaüstü Protokolleri**

**Sürüm:** 1.0\
**Tarih:** 31 Ekim 2026\
**Biçim:** UTF-8 Markdown\
**Kullanım:** Bir kişi veya birlikte çalışan bir ekip tarafından masaüstünde uygulanabilir inceleme, karar ve kayıt yöntemi.

Bu belge, siber güvenlik mühendisliğini taşıyan insan, teknik araç, kural ve kurum ilişkilerini beş boyutta inceler: **varlık, mekân, usul, zaman ve gaye**. Çalışmanın amacı, belirli bir dijital faaliyette neyin korunacağını, düzeni neyin taşıdığını, kimin ne yaptığını ve hangi sonuçların hangi dayanaklarla söylenebildiğini görünür kılmaktır.

Uygulama dizisi, beş boyutu **1–5** arasında toplar. **0 — Tohum (Başlangıç)** incelemeyi açar; **6 — Kökleşme (Bitiş)** sonucu, sınırlarını ve yeniden açılma koşullarını kayda bağlar.

Bu protokoller, kaynaklarda tarif edilen sistem ve güvence yaklaşımlarından hareketle bu çalışma için tasarlanmıştır. Tohum/Kökleşme adları, sıra, kayıt alanları ve kapanış ölçütleri bu belgenin yöntemidir. Bir resmî standardın veya sertifikasyon programının protokolü olarak sunulmaz.

## Ana önerme ve kavramsal sınır

Siber güvenlik mühendisliği; dijital sistemlerin ve onların etkilediği faaliyetlerin belirlenmiş koruma ihtiyaçlarını karşılamasını tasarlayan, gerçekleştiren, sınayan ve sürdüren bir mühendislik disiplinidir. Sistem güvenliği mühendisliğinde sistem; donanım ve yazılımın yanında insanları, süreçleri ve fiziksel unsurları da kapsayabilir. [NIST SP 800-160]

Bu belgede “taşıyıcı makine”, **insanların teknik araçlar, kurallar ve kurumlar aracılığıyla örgütledikleri amaçlı faaliyet düzeni** anlamında kullanılır. Bu bir kavramsal okumadır. Düzenin tek bir zihni olduğu, insanın bütünüyle makineye indirgenebileceği veya bütün tarafların aynı amacı paylaştığı varsayılmaz.

“Kim?” sorusu, karar veren ve hesap vermesi gereken kişi ve kuruluşları araştırır. “Ne?” sorusu, işleyen düzeni ve bileşenlerini araştırır. Bir sonuca neden olmak, o sonucun amacını belirlemek ve sonucundan sorumlu olmak farklı ilişkilerdir.

| Ayrım | Araştırılan ilişki | Kayda geçirilecek olan |
|---|---|---|
| Köken | Böyle bir koruma ihtiyacı neden doğuyor? | Değer verilen faaliyet, kırılganlık ve dijital bağımlılık. |
| Taşıyıcı | Faaliyet neyle mümkün oluyor? | İnsanlar, araçlar, kurallar, kurumlar ve ilişkileri. |
| Fail | Belirli eylemi kim veya ne yapıyor? | İşlem yapan kişi, kuruluş veya mekanizma. |
| Sorumlu | Karar ve sonuç için kim hesap vermeli? | Görev, yetki, bilgi ve müdahale imkânı bakımından açıklanan sorumluluk. |

Bu dört konum P0'da ilk görüş olarak yazılır; P1–P5 boyunca incelenir; P6'da dayanaklarıyla yeniden kurulur. Bir kişinin adını yazmak, ona görev devredildiği anlamına gelmez. Bir yazılımın işlem yapması da amaç belirleme ve sorumluluk sorularını kapatmaz.

~~~text
  SIBER GUVENLIK MUHENDISLIGI
    dijital sistemlerin ve onlarin etkiledigi faaliyetlerin belirlenmis
    koruma ihtiyaclarini karsilamasini
      tasarlayan . gerceklestiren . sinayan . surduren
    bir muhendislik disiplini
    sistem:  donanim ve yazilimin yaninda insanlar, surecler ve fiziksel
    unsurlar

  "TASIYICI MAKINE"  kavramsal bir okuma
    insanlarin teknik araclar, kurallar ve kurumlar araciligiyla
    orgutledikleri amacli faaliyet duzeni
    varsayilmaz:  tek bir zihin . insanin butunuyle makineye
    indirgenmesi . butun taraflarin ayni amaci paylasmasi

    "kim?"   karar veren ve hesap vermesi gereken kisi ve kuruluslar
    "ne?"    isleyen duzen ve bilesenleri

  DORT KONUM
    koken      boyle bir koruma ihtiyaci neden doguyor?
    tasiyici   faaliyet neyle mumkun oluyor?
    fail       belirli eylemi kim veya ne yapiyor?
    sorumlu    karar ve sonuc icin kim hesap vermeli?

    P0  ilk gorus  ---->  P1-P5  incelenir  ---->  P6  dayanaklariyla
                                                   yeniden kurulur
    bir kisinin adini yazmak  -/->  ona gorev devredildigi
    bir yazilimin islem yapmasi, amac belirleme ve sorumluluk
    sorularini kapatmaz
~~~

*Çizim 1 — Ana önerme ve kavramsal sınır: tanım; taşıyıcı makine; köken, taşıyıcı, fail ve sorumlu.*

## Kimdir ve kim değildir?

Taşıyıcı düzen; değer verilen bir faaliyeti dijital yeteneklerle sürdüren, sınırları tanımlanabilir ve değiştirilebilir bir bütündür. İçinde farklı çıkarlar, eksik bilgiler ve sınırlı yetkiler bulunabilir.

- **Yalnız bilgisayar değildir.** Aygıt, işlemleri taşır; o işlemlerin neden ve kimin için anlamlı olduğunu bütün kullanım ilişkisi açıklar.
- **Yalnız mühendis değildir.** Mühendis önemli bir faildir; bütün amaçların sahibi ve bütün risklerin tek sorumlusu değildir.
- **Yalnız sistem sahibi değildir.** Yönetim veya mülkiyet, etkilenen herkesin çıkarını temsil ettiği anlamına gelmez.
- **Yalnız saldırgan değildir.** Kötüye kullanım, koruma ihtiyacını belirginleştirir; korunacak değerin varlık nedenini oluşturmaz.
- **Yalnız otomasyon değildir.** Bir işi yerine getirmek, o işin amacını meşru kılmaz ve sorumluluk ilişkisini ortadan kaldırmaz.
- **Tek iradeli bir üst kişi değildir.** Kurumun beyan ettiği amaçla farklı aktörlerin fiilen desteklediği sonuçlar ayrışabilir.
- **İnsanın tamamı değildir.** Kullanıcı, çalışan veya operatör rolü bir kişinin bütün varlığını ve haklarını tüketmez.

Bu ayrımlar, insan davranışı, kurumlar, politikalar ve teşvikleri teknik mekanizmalarla birlikte ele alan güvenlik mühendisliği yaklaşımıyla ilişkilidir. [Anderson — What Is Security Engineering?]

~~~text
  TASIYICI DUZEN
    deger verilen bir faaliyeti dijital yeteneklerle surduren, sinirlari
    tanimlanabilir ve degistirilebilir bir butun
    icinde bulunabilir:  farkli cikarlar . eksik bilgiler . sinirli
    yetkiler

  KIM DEGILDIR
    yalniz bilgisayar         aygit islemleri tasir; anlamlarini butun
                              kullanim iliskisi aciklar
    yalniz muhendis           onemli bir fail; butun amaclarin sahibi
                              ve butun risklerin tek sorumlusu degil
    yalniz sistem sahibi      yonetim veya mulkiyet, etkilenen herkesin
                              cikarini temsil ettigi anlamina gelmez
    yalniz saldirgan          kotuye kullanim koruma ihtiyacini
                              belirginlestirir; korunacak degerin varlik
                              nedenini olusturmaz
    yalniz otomasyon          bir isi yerine getirmek, o isin amacini
                              mesru kilmaz
    tek iradeli bir ust kisi  beyan edilen amac ile fiilen desteklenen
                              sonuclar ayrisabilir
    insanin tamami            kullanici, calisan veya operator rolu bir
                              kisinin butun varligini ve haklarini
                              tuketmez
~~~

*Çizim 2 — Kimdir ve kim değildir: taşıyıcı düzen ve yedi ayrım.*

## Beş boyutun uygulamadaki karşılığı

| Protokol | Araştırma sorusu | Somut çıktı |
|---|---|---|
| 0 — Tohum | Neyi, neden, hangi kaynaklarla inceleyeceğiz? | Çalışma sorusu, kaynak sınırı ve bitiş beklentisi. |
| 1 — Varlık | Ne değer taşıyor; ne kaybedilebilir; neyle karıştırılmamalı? | Değer, kayıp, bileşen ve bilinmeyen kayıtları. |
| 2 — Mekan | Kim nerede hangi etkiyi kuruyor; kime veya neye dayanıyor? | Yetki, etki, güven ve bağımlılık ilişkileri. |
| 3 — Usül | İhtiyaç nasıl kurala, tasarıma ve sınanabilir iddiaya dönüşüyor? | Gereksinim, yöntem ve kanıt planı/durumu. |
| 4 — Zaman | Kararın dayanağı, etkili olacağı an ve yeniden açılma koşulu nedir? | Zaman kaydı, geçerlilik ve değişiklik tetikleyicileri. |
| 5 — Gaye | Beyan edilen, fiilen desteklenen ve savunulabilir amaç nedir? | Amaç, fayda, yük, çatışma ve ölçüt değerlendirmesi. |
| 6 — Kökleşme | Ne sonuçlandı; ne açık kaldı; nasıl sürdürülecek? | Dayanaklı sonuç, kapanış durumu, takip ve yeniden açılma kaydı. |

## Masaüstünde başlama

1. Bir çalışma klasörü oluştur. Örnek ad: `SGM_2026-10-31_OrtakArsiv`.
2. Bu klasörde `oturum-kaydi.md` adlı yeni bir dosya aç ve aşağıdaki protokollerin çıktı şablonlarını bu dosyaya sırayla kopyala.
3. Bir metin veya Markdown düzenleyicide kayıt dosyasını aç. Türkçe karakterler için UTF-8 kullan.
4. İlk oturumda 0–6 sırasını izle. Her aşamanın sonunda kaydı kaydet. Bir aşama önceki kararı değiştirirse değişiklik nedenini yazarak ilgili bölüme dön.
5. Sonuçları ayrı protokol dosyalarına dağıtmak yerine tek oturum kaydında biriktir. Protokol dosyaları yönerge; oturum kaydı uygulamanın çıktısıdır.
6. P6'da kapanış sürümü oluştur. Sonraki değerlendirmede yeni sürüm aç ve hangi koşulun çalışmayı yeniden açtığını belirt.

Terminal, ağ taraması veya yönetici yetkisi bu yöntemin önkoşulu değildir. Teknik bir sınama gerekiyorsa yöntemi ve beklenen kanıtı P3'te, yapılacak işi takip kaydında tanımla. Sınama gerçekten yürütülmeden sonuç üretildiğini yazma.

~~~text
  YEDI PROTOKOL VE CIKTILARI

    P0 Tohum      calisma sorusu, kaynak siniri, bitis beklentisi
       |
    P1 Varlik     deger, kayip, bilesen ve bilinmeyen kayitlari
    P2 Mekan      yetki, etki, guven ve bagimlilik iliskileri
    P3 Usul       gereksinim, yontem ve kanit plani/durumu
    P4 Zaman      zaman kaydi, gecerlilik, degisiklik tetikleyicileri
    P5 Gaye       amac, fayda, yuk, catisma ve olcut degerlendirmesi
       |
    P6 Koklesme   dayanakli sonuc, kapanis durumu, takip ve yeniden
                  acilma kaydi

  MASAUSTUNDE
    SGM_2026-10-31_OrtakArsiv/        calisma klasoru
      oturum-kaydi.md                 butun ciktilar tek oturum
                                      kaydinda birikir
    protokol dosyalari  yonerge   |   oturum kaydi  uygulamanin ciktisi

    bir asama onceki karari degistirirse:  degisiklik nedeni yazilir,
    ilgili bolume donulur
    P6'da kapanis surumu  -->  sonraki degerlendirmede yeni surum

    onkosul degil:  terminal . ag taramasi . yonetici yetkisi
    sinama gercekten yurutulmeden sonuc uretildigi yazilmaz
~~~

*Çizim 3 — Beş boyutun uygulamadaki karşılığı ve masaüstünde başlama: yedi protokolün çıktıları; klasör ve oturum kaydı.*

## Ortak kayıt dili

Kimlikleri her oturum içinde tutarlı ve benzersiz kullan. Kayıtlar arasında aynı nesneye yeniden atıf yaparken yeni bir nesneymiş gibi numaralandırma.

V kayıtlarının asıl tablosu P1'de, T kayıtlarının asıl tablosu P4'tedir. Başka bir aşamada yeni varsayım, bilinmeyen veya takip işi ortaya çıkarsa ilgili tabloya ekle; bulunduğun bölümde kimliğine atıf yap. P6'ya, P4'teki işlerin kapanış özeti taşınır.

| Önek | Anlam | Örnek |
|---|---|---|
| D | Korunacak değer | D-01 |
| B | İnsan, teknik unsur veya kurumsal bileşen | B-01 |
| I | Yetki, etki, güven veya bağımlılık ilişkisi | I-01 |
| G | Sınanabilir koruma gereksinimi | G-01 |
| K | Kanıt veya kanıt adayı | K-01 |
| V | Varsayım veya açık bilinmeyen | V-01 |
| A | Amaç | A-01 |
| T | Takip işi | T-01 |

**Kanıt durumları:** `Planlanan`, `Bir kaynaktan bildirilen`, `Bu oturumda gözlenen`. Bir kaynağı açıp okumuş olmak, o kaynağın anlattığı olayın bu oturumda gerçekleştirildiği anlamına gelmez. Doğrudan gözlemin kapsamını yaz: “Rol tablosunda bu izin görülüyor” gözlemi, “erişim bütün yollarda engelleniyor” iddiasını tek başına desteklemez.

Bir ifadenin dayanağı yoksa onu K kaydıyla kanıt gibi sunma; V kaydında `Varsayım` veya `Bilinmiyor` olarak tut. Bir test planı, test sonucu değildir. İddia, gerekçe ve kanıtın birlikte değerlendirilmesi güvence yaklaşımının temelidir. [SEI — Arguing Security]

**Görevlendirme:** Sorumlu bilinmiyorsa `Atanmadı`; bir kişiye görev önerilmişse `Önerildi, kabul bekliyor`; sorumluluk gerçekten üstlenilmişse `Kabul edildi` yazılır. **İş durumu** ayrıca `Açık` veya `Tamamlandı` olarak tutulur. Tamamlanma, beklenen çıktının gerçekten oluşmasına dayanır. Kayda görev yazılması herhangi bir kişiye mesaj göndermez veya bildirim oluşturmaz.

**Oturum kapanışı:** `Tamamlandı`, `Eksikleri kaydedilerek kapatıldı`, `Tamamlanmadan durduruldu`. Bu durum, sistemin güvenlik yeterliliği hakkında otomatik bir sonuç değildir. Açık takip işleri ve sistem hakkında desteklenen sonuç P6'da ayrı alanlarda tutulur.

~~~text
  KAYIT KIMLIKLERI  her oturum icinde tutarli ve benzersiz

                                          acildigi yer
    D  korunacak deger                    P1
    B  insan, teknik unsur, kurum         P1, P2
    I  yetki, etki, guven, bagimlilik     P2
    G  sinanabilir koruma gereksinimi     P3
    K  kanit veya kanit adayi             P3
    V  varsayim veya acik bilinmeyen      asil tablo  P1
    A  amac                               P5
    T  takip isi                          asil tablo  P4  -->  ozet P6

    A-...  -->  D-...  -->  G-...  -->  K-...

  KANIT DURUMLARI
    Planlanan  |  Bir kaynaktan bildirilen  |  Bu oturumda gozlenen
    bir kaynagi okumus olmak  -/->  anlattigi olayin bu oturumda
                                    gerceklestirildigi
    bir test plani, test sonucu degildir

  GOREVLENDIRME            IS DURUMU         OTURUM KAPANISI
    Atanmadi                 Acik              Tamamlandi
    Onerildi, kabul          Tamamlandi        Eksikleri kaydedilerek
    bekliyor                                   kapatildi
    Kabul edildi                               Tamamlanmadan durduruldu

    kayda gorev yazilmasi mesaj gondermez veya bildirim olusturmaz
    oturum kapanisi, sistemin guvenlik yeterliligi hakkinda otomatik
    bir sonuc degildir
~~~

*Çizim 4 — Ortak kayıt dili: kayıt kimlikleri; kanıt durumları; görevlendirme, iş durumu ve oturum kapanışı.*

## Protokoller

Aşağıda yedi protokolün tam metni yer alır. Her protokolün çıktısı ortak oturum kaydındaki aynı numaralı P bölümüne yazılır.

## 0 Tohum (Başlangıç) Protokolü

### Amaç ve temel soru

Bu protokol, incelemenin nesnesini, sorusunu, kaynaklarını ve çalışma sınırını belirleyerek oturumu başlatır. Tohum, sonucu önceden veren bir hüküm değildir; sınanacak bir başlangıçtır.

**Temel soru:** Hangi insan faaliyetini, hangi dijital bağımlılık içinde, kimin açısından ve neden incelemeye alıyorum?

**Ayırt etme sorusu:** İncelediğim aygıtı, o aygıtı anlamlı kılan insan faaliyetinin bütünüyle karıştırıyor muyum?

### Girdiler ve masaüstü hazırlığı

- İncelenecek tek bir sistem, hizmet, ürün veya açıkça sınırlandırılmış faaliyet.
- Bu çalışma için seçilmiş belgeler, notlar veya açıkça belirtilmiş gözlemler.
- Dosya yöneticisi ve UTF-8 kaydedebilen bir metin veya Markdown düzenleyici.
- `oturum-kaydi.md`; dosya yoksa bu protokoldeki kayıt alanlarıyla açılır.

Masaüstünde ya da seçtiğin çalışma konumunda `SGM_YYYY-AA-GG_KisaAd` adlı bir klasör oluştur. Şablonu bu klasöre kopyala ve kopyayı `oturum-kaydi.md` olarak adlandır. Özgün protokol dosyalarını yönerge olarak sakla; cevapları oturum kaydına yaz.

Buradaki gerçekleştirme, inceleme, modelleme ve kayıt üretme işidir. Gerçek bir sistemde değişiklik veya teknik sınama gerektiğinde bunu ayrı bir takip işi olarak tanımla; bu belge, yapılmamış işlemleri yapılmış saymaz.

### Uygulama adımları

1. **İnceleme nesnesini adlandır.** Sistem adını, ele alınan kullanım biçimini ve varsa sürüm ya da yapılandırmayı yaz. Henüz tasarlanmamış bir sistemse bunu belirt. Birden çok sistemi inceliyorsan onları bir arada ele almanın gerekçesini ekle.
2. **Tek bir başlangıç sorusu yaz.** Soruyu, oturum sonunda bir kayıtla cevaplanabilecek kadar somutlaştır. Örneğin: “Ortak arşivde bir rol değiştiğinde hangi erişimler devam ediyor ve bu devamlılığı neye dayanarak açıklıyoruz?”
3. **İlk değer ve kayıp taslağını kur.** Kimin hangi faaliyetinin korunacağını ve neyin kayıp sayılacağını birer cümleyle belirt. Bunları P1'de incelenecek başlangıç görüşleri olarak kaydet; kesin sonuç gibi sunma.
4. **Dört konumu ayır.** İhtiyacı doğuran ilişkiyi “köken”; insanları, araçları ve kuralları “taşıyıcı”; belirli işlemi yapanı “fail”; karar ve sonuç için hesap vermesi bekleneni “sorumlu” alanına yaz. Bilmediğin alanları `Bilinmiyor` olarak bırak. Sonraki aşamalar bu ilk görüşleri değiştirebilir.
5. **Kaynak ve kapsam sınırını koy.** Bu oturumda hangi dosya, bağlantı ve açıklamaların kullanılacağını listele. Önceki sohbetler veya kişisel geçmiş kendiliğinden girdi değildir. Dışarıdan yeni kaynak eklemek serbesttir; kaynağı ve ekleme gerekçesini önce kayda geçir. Böylece çalışma geçmiş bağlamı varsaymadan, eldeki metinle de sınırlanmadan ilerler.
6. **Bitiş beklentisini yaz ve kaydet.** Oturumun sonunda hangi soruların cevaplanmış, hangi belirsizliklerin görünür ve hangi takip işlerinin tanımlanmış olması gerektiğini belirt. Tarih, katılımcılar ve ilk kaydı yazan kişiyi ekle. `oturum-kaydi.md` dosyasını kaydet.

### P0 çıktı şablonu

Aşağıdaki alanları ortak kaydın `P0 — Tohum` bölümüne doldur:

```markdown
## P0 — Tohum

- Oturum adı:
- Başlangıç tarihi ve saat dilimi:
- İnceleme nesnesi ve kullanım bağlamı:
- Başlangıç sorusu:
- İlk korunacak faaliyet/değer:
- İlk kayıp tanımı:
- Köken hakkında başlangıç görüşü:
- Taşıyıcı hakkında başlangıç görüşü:
- Fail hakkında başlangıç görüşü:
- Sorumlu hakkında başlangıç görüşü:
- Dâhil edilen kaynaklar ve nedenleri:
- Kapsam içi:
- Kapsam dışı:
- Varsayımlar ve bilinmeyenler:
- Oturumun bitiş beklentisi:
- Kaydı yazan kişi:
```

### Tamamlanma ölçütü

- [ ] İnceleme nesnesi ve başlangıç sorusu belirli.
- [ ] Korunacak faaliyet ile kayıp arasındaki ilk bağ yazılı.
- [ ] Köken, taşıyıcı, fail ve sorumlu birbirine eşitlenmemiş.
- [ ] Kullanılacak kaynaklar ve dışarıdan kaynak ekleme yolu açık.
- [ ] Bitiş beklentisi yazılı; yapılmamış bir işlem gerçekleştirilmiş gibi kaydedilmemiş.
- [ ] Ortak kayıt kaydedilmiş.

Bu koşullar sağlandığında **1 — Varlık** protokolüne geç. Sistem veya soru hâlâ belirsizse P0'da kal ve kapsamı daralt. İlerleyen aşamalarda başlangıç sorusu değişirse P0'ı tarih ve gerekçeyle güncelle; eski ifadenin değiştiğini kayda geçir.

~~~text
  TOHUM  sonucu onceden veren bir hukum degil; sinanacak bir baslangic
    temel soru:  hangi insan faaliyetini, hangi dijital bagimlilik
    icinde, kimin acisindan ve neden incelemeye aliyorum?
    ayirt etme sorusu:  incelenen aygit  |  o aygiti anlamli kilan insan
                                            faaliyetinin butunu

  UYGULAMA ADIMLARI
    1  inceleme nesnesini adlandir
    2  tek bir baslangic sorusu yaz
         "Ortak arsivde bir rol degistiginde hangi erisimler devam
          ediyor ve bu devamliligi neye dayanarak acikliyoruz?"
    3  ilk deger ve kayip taslagini kur
    4  dort konumu ayir:  koken | tasiyici | fail | sorumlu
                          bilinmeyen alan:  Bilinmiyor
    5  kaynak ve kapsam sinirini koy
         onceki sohbetler veya kisisel gecmis kendiliginden girdi
         degildir; disaridan kaynak eklemek serbesttir, kaynak ve
         gerekce once kayda gecer
    6  bitis beklentisini yaz ve kaydet

  BURADAKI GERCEKLESTIRME  inceleme . modelleme . kayit uretme
    gercek bir sistemde degisiklik veya teknik sinama  -->  ayri bir
                                                           takip isi
    yapilmamis islemler yapilmis sayilmaz
~~~

*Çizim 5 — Tohum: temel soru ve ayırt etme sorusu; altı adım; buradaki gerçekleştirme.*

### Dayanak

Bu protokol, bu belge için tasarlanmış bir uygulama yöntemidir. Sistemleri insan, süreç ve teknik unsurlarıyla ele alma dayanağı: NIST SP 800-160 Vol. 1 Rev. 1. Tohum adı, adım sırası ve kayıt biçimi bu kaynağın resmî protokolü değildir.

## 1 Varlık Protokolü

### Amaç ve kapsam

İncelenen faaliyetin ne olduğunu, neden korunmaya değer görüldüğünü ve onu taşıyan düzenin kimlerden ve nelerden oluştuğunu açıklığa kavuştur. Bu protokolde “makine”, insanların, teknik araçların ve kuralların birlikte sonuç ürettiği düzen anlamındadır. Bir sistemin bileşeni olmak, insanın bütün varlığını o role indirgemez.

Çalışmanın çıktısı bir envanter yığını değil, korunacak değer ile olası kayıp arasında kurulmuş açık bir ilişkidir. “Kimdir, kim değildir?” sorusu; kökeni, taşıyıcıyı, faili ve sorumluyu birbirine karıştırmadan yanıtlanır.

### Başlama koşulu ve girdiler

- `oturum-kaydi.md` içinde tamamlanmış **P0 — Tohum** kaydı.
- Tek cümleyle tanımlanmış inceleme konusu ve çalışma kapsamı.
- Bu oturum için seçilmiş mevcut açıklamalar veya belgeler; bulunmayan bilgi için açık bir bilinmezlik kaydı.

Dosya yöneticisinde çalışma klasörünü, metin düzenleyicide `oturum-kaydi.md` dosyasını aç. Kayıtta aşağıdaki **P1 — Varlık** bölümünü oluştur. Gerçek bir sisteme bağlanmak bu çalışmanın girdisi değildir.

### Masaüstünde yürütme

1. **Faaliyeti tek cümlede adlandır.** “Bir uygulama” veya “siber güvenlik” gibi geniş adlar yerine, kimin ne yapabildiğini yaz. Örneğin “Bir ekibin ortak çalışma belgelerine belirlenen yetkilerle ulaşabilmesi.” Korunacak faaliyetle kullanılan ürünün adını ayır; araç değiştiğinde faaliyetin sürüp sürmeyeceğini düşün.

2. **Değer verilen şeyi ve kaybı eşleştir.** Her değer için `D-01` biçiminde bir kimlik aç. Değerin kimin açısından önemli olduğunu, hangi değişikliğin kayıp sayılacağını ve bu kaybın somut sonucunu belirt. “Veri kaybı” yazdıysan hangi faaliyetin bunun yüzünden yapılamayacağını da ekle. Bir değer farklı kişiler için farklı sonuçlar doğuruyorsa ayrı satırlar kullan.

3. **Dört konumu ayır.** Kökeni “Bu koruma ihtiyacını doğuran ilişki nedir?” sorusuyla yaz. Taşıyıcıyı insanlar, kurallar ve teknik unsurlar üzerinden tanımla. Fail için belirli eylemi gerçekleştiren kişiyi veya mekanizmayı belirt. Sorumlu alanına, karar ve müdahale yetkisi bilinen kişi ya da rolü yaz; bilinmiyorsa isim uydurma.

4. **Taşıyıcıyı ilk kez sınırla.** Faaliyeti doğrudan mümkün kılan başlıca bileşenlere `B-01` biçiminde kimlik ver. İnsanları yalnız rol düzeyinde kaydetmek yeterli olabilir. Bir bileşeni dâhil etme gerekçen, değer veya kayıp üzerindeki etkisi olsun. Bir sonraki protokolde bunların ilişkileri ayrıntılandırılacak.

5. **Kim olmadığını açıkla.** İncelenen düzenin yalnız bilgisayar, yalnız mühendis, yalnız sahip veya yalnız saldırgan olarak neden açıklanamadığını kendi örneğin üzerinde belirt. Bunun yanında kapsam dışındaki konuları yaz. “Her şey etkileyebilir” gerekçesiyle çalışmayı sınırsızlaştırma; kurulmamış etki ilişkisini kurulmuş sayma.

6. **Bilgi durumunu işaretle ve kaydet.** Doğrudan incelenen belgeyi veya mevcut kaydı dayanak olarak göster. Aktarılan bir bilgiyi “Bir kaynaktan bildirilen” diye belirt. Henüz desteklenmeyen geçici kabulü `V-01` kimliğiyle `Varsayım`, hakkında bilgi olmayan konuyu `Bilinmiyor` olarak kaydet. Metni okuyarak bir kişinin bütün amaçların sahibi veya bütün hataların sorumlusu ilan edilmediğini kontrol et.

### Kayıt şablonu

```markdown
## P1 — Varlık

Faaliyet:
Koruma ihtiyacının kökeni:
Taşıyıcı düzen:
Başlıca failler:
Sorumluluğu bilinen roller / belirsiz roller:
Bu düzen kim veya ne değildir:
Kapsam dışı:

| Kimlik | Değer / korunacak faaliyet | Kimin için? | Kayıp ne olur? | Somut sonuç | Dayanak / varsayım |
|---|---|---|---|---|---|
| D-01 | | | | | |

| Bileşen | Adı veya rolü | Faaliyete katkısı |
|---|---|---|
| B-01 | | |

| Kayıt | Tür | İfade / soru | Dayanak veya eksik bilgi |
|---|---|---|---|
| V-01 | Varsayım / Bilinmiyor | | |

Sonuç: Tamamlandı / Açık
```

### Tamamlanma ve dönüş

- [ ] En az bir değer, onun taşıyıcısı ve kaybın sonucu açıklandı.
- [ ] Köken, taşıyıcı, fail ve sorumlu ayrı yazıldı.
- [ ] Kapsam dışı olanlar ve bilinmeyenler kaydedildi.
- [ ] Bileşen kimlikleri bir sonraki adımda kullanılabilecek durumda.

Konu hâlâ bir cümlede tanımlanamıyorsa **P0 — Tohum** bölümüne dön. Faaliyet anlaşılmış, fakat bazı bilgiler eksikse bunları `Bilinmiyor` olarak taşı; geçici bir kabul kullanılıyorsa ayrıca `Varsayım` de. Ardından **P2 — Mekan** protokolüne geç. “Tamamlandı”, varlık incelemesinin tamamlandığını belirtir; sistemin güvenli olduğuna ilişkin bir onay değildir.

~~~text
  FAALIYET TEK CUMLEDE
    "Bir ekibin ortak calisma belgelerine belirlenen yetkilerle
     ulasabilmesi."
    korunacak faaliyet  |  kullanilan urunun adi
    arac degistiginde faaliyet suruyor mu?

  DEGER VE KAYIP
    D-01  korunacak faaliyet  -->  kimin icin?  -->  kayip ne olur?
                                                     -->  somut sonuc
    "veri kaybi" yazildiysa:  hangi faaliyet bunun yuzunden
    yapilamayacak?
    farkli kisiler icin farkli sonuclar:  ayri satirlar

  DORT KONUM
    koken      bu koruma ihtiyacini doguran iliski
    tasiyici   insanlar, kurallar ve teknik unsurlar
    fail       belirli eylemi gerceklestiren kisi veya mekanizma
    sorumlu    karar ve mudahale yetkisi bilinen kisi ya da rol;
               bilinmiyorsa isim uydurulmaz

  BILESENLER  B-01 ...  dahil etme gerekcesi:  deger veya kayip
  uzerindeki etki
    "her sey etkileyebilir" gerekcesiyle calisma sinirsizlastirilmaz

  BILGI DURUMU
    dayanak        dogrudan incelenen belge veya mevcut kayit
    aktarilan      Bir kaynaktan bildirilen
    V-01           Varsayim  |  Bilinmiyor
    "Tamamlandi"  -/->  sistemin guvenli oldugu
~~~

*Çizim 6 — Varlık: faaliyet; değer ve kayıp; dört konum; bileşenler; bilgi durumu.*

### Dayanak

İnsan, süreç ve teknik unsurları birlikte ele alan sistem yaklaşımı: NIST SP 800-160 Vol. 1 Rev. 1. Adımlar ve kayıt şablonu bu belge için tasarlanmıştır.

## 2 Mekan Protokolü

### Amaç ve kapsam

Korunacak faaliyetin nerede gerçekleştiğini; erişim, etki, yetki ve bağımlılık ilişkileriyle birlikte göster. Mekân burada cihazların bulunduğu fiziksel yerleri içerir; kimin hangi bilgiye veya işleme ulaşabildiğini de kapsar. Aynı odada bulunmak aynı yetkiye sahip olmak anlamına gelmez.

Çıktı, P1'de belirlenen taşıyıcı düzenin okunabilir bir ilişki haritasıdır. Bu harita, bu oturum için seçilmiş mevcut bilgiler düzenlenerek hazırlanır. Bilinmeyen bağlantı `Bilinmiyor` olarak kalır; geçici bir bağlantı kabul ediliyorsa ayrıca `Varsayım` diye işaretlenir.

### Başlama koşulu ve girdiler

- `oturum-kaydi.md` içindeki **P0 — Tohum** ve **P1 — Varlık** bölümleri.
- `D-01` biçimindeki değer kayıtları ve `B-01` biçimindeki ilk bileşen listesi.
- Varsa mevcut mimari açıklama, görev tanımı veya süreç çizimi.

Metin düzenleyicide **P2 — Mekan** bölümünü aç. Çizim aracı zorunlu değildir; aşağıdaki iki tablo, çalışmanın temel haritası olarak yeterlidir. Yer adı bilinmiyorsa tahmini bir konum yazma.

### Masaüstünde yürütme

1. **Bileşen listesini düzenle.** P1'deki kimlikleri koruyarak her bileşenin insan, kurum, teknik unsur veya süreç olduğunu belirt. Aynı bileşene ikinci bir kimlik verme. Fiziksel konum biliniyorsa ekle; uzaktan işletilen hizmeti, sırf dışarıda olduğu için kapsam dışında bırakma.

2. **İlişkileri yönlü olarak yaz.** Her bağlantıya `I-01` biçiminde kimlik ver. “B-01, B-02'deki kaydı okur” gibi bir kaynak, hedef ve eylem belirt. Veri akışı, karar verme, yapılandırma değiştirme ve hizmete dayanma ilişkilerini aynı şey sayma. Bir bağlantının birden fazla etkisi varsa bunları ayrı satırlarda göster.

3. **Yetkinin kaynağını bul.** Her önemli ilişkide işlemi kim veya ne yapıyor, yetkiyi hangi rol veya kural veriyor, yetkiyi kim değiştirebiliyor sorularını yanıtla. Bir otomatik mekanizmayı fail olarak yazmak mümkündür; mekanizmanın kuralını belirleyen rolü ayrıca kaydet. Teknik olarak yapılabileni kendiliğinden meşru sayma.

4. **Güven sınırlarını işaretle.** Bir taraftan gelen bilgi veya kimliğin diğer tarafta farklı kabullerle karşılandığı yerleri belirle. Örneğin dışarıdan yüklenen dosyanın içeride işleme alınması bir sınır adayıdır. Sınırın neden önemli olduğunu bir cümlede açıkla. “İç ağ” veya “bizim çalışanımız” tek başına güven gerekçesi olarak yazılmasın.

5. **Bir kaybın yayılmasını izle.** P1'den bir değer seç. Onu etkileyen bir bileşenin yanlış çalıştığını veya yetkisinin kötüye kullanıldığını varsay. Hangi ilişkiler üzerinden başka değerlere ulaşılabileceğini, yalnız mevcut bilgilerle çiz. Olmayan bağlantı ekleme. Böylece tek bir unsurun taşıdığı bağımlılıklar ve bilinmeyen geçişler görünür olur.

6. **Haritanın sınırını ve boşluklarını kaydet.** Dâhil edilmeyen unsurları gerekçesiyle yaz. “Taşıyıcı yalnız şu ürün değildir” cümlesini somutlaştır: Ürünün dışında hangi insan kararı veya hizmet bağımlılığı sonuca etki ediyor? Yeni V kayıtlarını P1'deki varsayım/bilinmeyen tablosuna ekle. Takip gerektiren konuları `T-01` biçiminde P4'teki takip tablosuna yaz; P2'de bu kimliklere atıf yap ve dosyayı kaydet.

### Kayıt şablonu

```markdown
## P2 — Mekan

| Bileşen | Tür / rol | Yer veya bağlam | İlgili değer |
|---|---|---|---|
| B-01 | | | D-01 |

| İlişki | Kaynak → hedef | Eylem / bağımlılık | Yetkiyi veren veya değiştiren | Dayanak / varsayım |
|---|---|---|---|---|
| I-01 | B-01 → B-02 | | | |

Güven sınırları ve gerekçeleri:
Seçilen kayıp senaryosu ve izlenen ilişkiler:
Kapsam dışında kalan yerler / ilişkiler:
Bu mekân ne değildir:
Bilinmeyenler: V-... / T-...
Sonuç: Tamamlandı / Açık
```

### Tamamlanma ve dönüş

- [ ] Her önemli bileşenin faaliyete katkısı ve ilişkileri gösterildi.
- [ ] İşlemi gerçekleştirenle yetkiyi belirleyen mümkün olduğunca ayrıldı.
- [ ] En az bir güven sınırı değerlendirildi; yoksa neden bulunmadığı açıklandı.
- [ ] Bir kayıp senaryosunun izlenebilen etkileri ve bilinmeyenleri kaydedildi.

Korunacak değer belirsizse **P1 — Varlık** bölümüne dön. Harita konuyu sürekli genişletiyorsa **P0 — Tohum** kapsamını düzelt. Yeterli bir ilk harita oluştuğunda **P3 — Usül** protokolüne geç. Harita, doğrulanmış canlı sistem envanteri olarak sunulmaz.

~~~text
  MEKAN  cihazlarin bulundugu fiziksel yerler ve kimin hangi bilgiye
  veya isleme ulasabildigi
    ayni odada bulunmak  -/->  ayni yetkiye sahip olmak

  YONLU ILISKILER

    +------+       I-01: okur        +------+
    | B-01 | ----------------------> | B-02 |
    +------+            ^            +------+
                        |
       yetkiyi veren    |    yetkiyi degistirebilen
       rol veya kural --+--  rol
    ayni sey sayilmaz:  veri akisi . karar verme . yapilandirma
    degistirme . hizmete dayanma
    teknik olarak yapilabilen kendiliginden mesru sayilmaz

  GUVEN SINIRI  bir taraftan gelen bilgi veya kimlik diger tarafta
  farkli kabullerle karsilanir
           disarida            :            iceride
    yuklenen dosya  ---------- : --------->  isleme alinir
                               :
    "ic ag" veya "bizim calisanimiz" tek basina guven gerekcesi
    degildir  [NIST SP 800-207]

  BIR KAYBIN YAYILMASI
    P1'den bir deger --> onu etkileyen bilesen yanlis calisir veya
    yetkisi kotuye kullanilir --> hangi iliskiler uzerinden baska
    degerlere ulasilir?  yalniz mevcut bilgilerle; olmayan baglanti
    eklenmez
~~~

*Çizim 7 — Mekan: yönlü ilişkiler ve yetkinin kaynağı; güven sınırı; bir kaybın yayılması.*

### Dayanak

Fiziksel veya ağ konumunu tek başına güven gerekçesi saymama yaklaşımı: NIST SP 800-207 — Zero Trust Architecture. İlişki tablosu ve uygulama sırası bu belge için tasarlanmıştır.

## 3 Usül Protokolü

### Amaç ve kapsam

Koruma ihtiyacını açık bir gereksinime, gereksinimi tasarım seçeneğine ve seçeneği değerlendirecek kanıt planına bağla. Bu protokolün işi, “Ne yaptık?” listesinden “Hangi ihtiyacı, hangi gerekçeyle, nasıl karşılayacağız?” açıklamasına geçmektir.

Masaüstündeki çalışma; mevcut belgeleri incelemek, kararları karşılaştırmak ve doğrulama ihtiyacını yazmaktır. Bir test planını hazırlamak, testi gerçekleştirmek değildir. Gerçek sistemlerde tarama, komut çalıştırma, erişim değiştirme veya dağıtım yapma bu protokolün çıktıları arasında değildir.

### Başlama koşulu ve girdiler

- `oturum-kaydi.md` içindeki **P1 — Varlık** ve **P2 — Mekan** kayıtları.
- İncelenecek bir `D-01` değeri ve onu etkileyen `B-01` / `I-01` kayıtları.
- Varsa mevcut politika, tasarım açıklaması veya daha önce üretilmiş test sonucu.

Metin düzenleyicide **P3 — Usül** bölümünü aç. Kanıt dosyaları varsa bulundukları yolu kaydet; gereksiz kopyalar oluşturmadan mevcut dosyalara başvur. Henüz elde bulunmayan kanıtlara “planlanan” durumunu ver.

### Masaüstünde yürütme

1. **Bir kayıp senaryosu seç.** “Bir şeyler ters gidebilir” yerine belirli bir değer, ilgili ilişki ve olası sonucu yaz. Senaryonun hangi bilgilerden türetildiğini göster. Bilinmeyen koşulları `Bilinmiyor`, yalnız geçici olarak kabul ettiğin koşulları `Varsayım` diye ayır ve P1'deki V tablosuna ekle. Her olası saldırıyı listelemeye çalışmak yerine seçtiğin kapsamın önemli bir koruma ihtiyacını işle.

2. **Sınanabilir gereksinim kur.** Her gereksinime `G-01` biçiminde kimlik ver. Hangi davranışın, hangi kapsamda ve hangi koşullarda gerçekleşmesi gerektiğini belirt. Bir süre veya eşik gerekiyorsa, kararlaştırılmamış sayıyı kesin değer gibi yazma. Gereksinimi `D-01` değeriyle ve ilgili kayıp senaryosuyla ilişkilendir.

3. **En az iki yaklaşımı karşılaştır.** Tasarımı değiştirmek, gereksiz bir yetkiyi kaldırmak, etkileri ayırmak veya mevcut mekanizmayı iyileştirmek gibi bağlama uygun seçenekler yaz. Her seçeneğin yararını, kullanım üzerindeki etkisini ve yeni bağımlılıklarını belirt. Henüz seçilmeyen yaklaşımı uygulanmış çözüm olarak kaydetme.

4. **Kararı ve karar sahibini görünür kıl.** Tercih edilen yaklaşımın gerekçesini yaz. Uygulayan rol, kararı verebilen rol ve sonuçtan etkilenen taraflar farklıysa ayır. Bilgi veya yetki eksikse karar durumunu “bekliyor” bırak. Mekanizmanın işlemi gerçekleştirmesi, bütün sorumluluğun mekanizmaya ait olduğu anlamına gelmez.

5. **Kanıt planını oluştur.** Her öğeye `K-01` kimliği ver. `Planlanan` henüz elde edilmemiş kanıt ihtiyacıdır; `Bir kaynaktan bildirilen` başkasının aktardığı sonuçtur; `Bu oturumda gözlenen` ise kapsamı açıkça yazılmış doğrudan gözlemdir. Bir raporu okumak, yalnız raporun içeriğini gözlemlemektir; anlattığı testin bu oturumda yapıldığı anlamına gelmez. Her öğenin hangi iddiayı desteklediğini ve neleri göstermediğini yaz.

6. **İki ayrı yeterlilik sorusu sor.** “Seçilen kural doğru uygulanmış mı?” ile “Seçilen kural gerçek koruma ihtiyacını karşılıyor mu?” sorularını ayrı cevapla. Cevap için kanıt yoksa boşluğu `T-01` takip işi yap. Yeni bir görev sahibi yalnız öneriliyorsa bunu kabul edilmiş görevlendirme sayma. Sonuç bölümünde yalnız gösterilebilen şeyi söyle; açık test veya varsayım varken güvenli sistem onayı üretme.

### Kayıt şablonu

```markdown
## P3 — Usül

Kayıp senaryosu:
İlgili değer / bileşen / ilişki: D-... / B-... / I-...

| Gereksinim | Koşul ve beklenen davranış | Kabul ölçütü | İlgili değer |
|---|---|---|---|
| G-01 | | | D-01 |

Seçenekler ve etkileri:
Tercih / gerekçe / karar durumu:
Uygulayan rol / karar veren rol / etkilenenler:

| Kanıt | G-... | Durum | Kaynak veya elde etme planı | Gösterdiği / göstermediği |
|---|---|---|---|---|
| K-01 | G-01 | Planlanan / Bir kaynaktan bildirilen / Bu oturumda gözlenen | | |

Doğru uygulama değerlendirmesi:
İhtiyacı karşılama değerlendirmesi:
Açık işler: T-...
Sonuç: Tamamlandı / Açık
```

### Tamamlanma ve dönüş

- [ ] Bir kayıp senaryosu, gereksinim ve yaklaşım birbirine bağlandı.
- [ ] Karar ile uygulama; kanıt planı ile mevcut kanıt ayrıldı.
- [ ] Her kanıtın kapsamı ve eksik doğrulama ihtiyacı açıklandı.
- [ ] Yapılmamış hiçbir işlem veya test yapılmış gibi yazılmadı.

İlişkiler belirsizse **P2 — Mekan**, ihtiyaç belirsizse **P1 — Varlık** bölümüne dön. Kanıt planı ve boşluklar görünür durumdaysa **P4 — Zaman** protokolüne geç. Buradaki tamamlanma, değerlendirme planının tamamlanmasıdır.

~~~text
  IHTIYACTAN KANITA

    kayip senaryosu    belirli bir deger, ilgili iliski ve olasi sonuc
          |
          v
    G-01 gereksinim    hangi davranis, hangi kapsamda ve hangi
          |            kosullarda; kararlastirilmamis sayi kesin deger
          |            gibi yazilmaz
          v
    en az iki          tasarimi degistirmek . gereksiz bir yetkiyi
    yaklasim           kaldirmak . etkileri ayirmak . mevcut
          |            mekanizmayi iyilestirmek
          v
    karar ve           uygulayan rol | karari verebilen rol |
    karar sahibi       etkilenen taraflar
          |
          v
    K-01 kanit plani   Planlanan | Bir kaynaktan bildirilen |
                       Bu oturumda gozlenen

  IKI AYRI YETERLILIK SORUSU
    "Secilen kural dogru uygulanmis mi?"
    "Secilen kural gercek koruma ihtiyacini karsiliyor mu?"
    cevap icin kanit yoksa  -->  T-01 takip isi

  BU PROTOKOLUN CIKTILARI DEGILDIR
    gercek sistemlerde tarama . komut calistirma . erisim degistirme .
    dagitim
    bir test planini hazirlamak, testi gerceklestirmek degildir
~~~

*Çizim 8 — Usül: kayıp senaryosundan kanıt planına; iki ayrı yeterlilik sorusu.*

### Dayanak

İddia, gerekçe ve kanıtı ilişkilendirme yaklaşımı: SEI — Arguing Security. Adımlar ve kanıt durumları bu belge için tasarlanmıştır.

## 4 Zaman Protokolü

### Amaç ve kapsam

Geçmiş dayanakların, şimdiki kararların ve gelecekte yeniden değerlendirme gerektirecek değişikliklerin bağını kur. Bu protokol, çalışmayı yalnız saldırı anına veya sürekli aciliyete indirgemez. Bir güvenlik değerlendirmesinin hangi sürüm, koşul ve bilgi durumu için geçerli olduğunu açıklar.

Çıktı bir takvimden daha fazlasıdır: hangi kararın şimdi verileceğini, hangisinin bekleyebileceğini ve hangi olayda çalışmanın yeniden açılacağını gösteren kayıt olur. Bu masaüstü uygulaması otomatik hatırlatıcı veya çalışan izleme sistemi kurmaz; bunlar isteniyorsa ayrı bir uygulama işi olarak kaydedilir.

### Başlama koşulu ve girdiler

- `oturum-kaydi.md` içindeki **P0–P3** kayıtları.
- Mevcut `G-01` gereksinimleri, `K-01` kanıt kayıtları ve `V-01` varsayımları.
- Bu çalışma için bilinen sürüm, tarih, görev değişikliği veya planlanmış değişiklik bilgileri.

Metin düzenleyicide **P4 — Zaman** bölümünü aç. Yalnız P0'da bu oturum için seçilmiş bilgilerle çalış. Bilinmeyen bir belge tarihi, sistem sürümü veya son inceleme zamanı için “bilinmiyor” yaz; geçmiş konuşmaları kendiliğinden dayanak yapma.

### Masaüstünde yürütme

1. **Bugünkü konumu sabitle.** Oturum tarihini, incelenen sistemin bilinen sürümünü ve yaşam döngüsü aşamasını yaz: fikir, tasarım, devreye alma, işletim, değişiklik veya kullanımdan kaldırma. Tek bir bütün farklı aşamalardaki bileşenler içeriyorsa bunları ayır. Oturum tarihini, sistemin en son doğrulandığı tarih yerine kullanma.

2. **Geçmişten taşınan dayanakları belirle.** P3'teki kanıtlardan hangilerinin mevcut duruma ilişkin olduğunu incele. Daha eski bir sürüm için üretilmiş belgeyi güncel sürümün kanıtı sayma. Geçerliliğin taşınabildiği düşünülüyorsa bunun gerekçesini ve sınırını yaz; bilinmiyorsa yeniden değerlendirme ihtiyacını kaydet.

3. **Şimdi verilmesi gereken kararı seç.** Bir kararın neden bugün gerekli olduğunu açıkla. Gecikmenin etkisi biliniyorsa belirt; sırf güvenlikle ilgili olduğu için her maddeye “acil” yazma. Karar verecek rolü ve karar için eksik bilgiyi ilişkilendir. Belirsizliği giderecek bir sonraki somut iş, kararın önüne konabilir.

4. **Olay öncesi, sırası ve sonrasını ayır.** P3'teki kayıp senaryosu için hangi hazırlığın önceden bulunması gerektiğini yaz. Olay sırasında hangi bilgiye ve karar imkânına ihtiyaç duyulacağını belirt. Sonrasında hizmetin yeniden çalışmasıyla yeniden güvenilebilir bulunmasını ayrı değerlendir. Buradaki satırlar, gerçekleştirilmiş müdahale kayıtları değil, ihtiyaç veya plan kayıtlarıdır.

5. **Yeniden açma tetikleyicilerini tanımla.** Yeni bileşen, değişen görev, yeni dış hizmet, güncel olmayan kanıt veya gerçekleşmiş bir kayıp gibi somut koşullar seç. Her koşulu hangi protokole döndüreceğini yaz. “Gerektiğinde bakılır” yerine, koşulu kimin fark edeceğini ve kaydı kimin açacağını belirt; rol bilinmiyorsa açık iş bırak.

6. **Takip işlerini ve gözden geçirmeyi kaydet.** Her işe `T-01` biçiminde kimlik ver. İşin sahibi, beklenen çıktısı ve zamanı ya da olay tetikleyicisi bulunsun. Yeni görev sahibi için “önerildi” ile “kabul edildi” durumlarını ayır. Tarih henüz belirlenmediyse uydurma; “tarih kararı bekliyor” yaz. Bütün varsayımların yeniden bakılacak bir koşula bağlanıp bağlanmadığını incele, ardından kaydet.

### Kayıt şablonu

```markdown
## P4 — Zaman

Oturum tarihi:
Bilinen sürüm / yaşam döngüsü aşaması:
Geçmiş dayanaklar ve geçerlilik sınırları: K-...
Şimdi verilmesi gereken karar / gerekçesi:
Ertelenen karar / koşulu:
Olay öncesi hazırlık / olay sırası ihtiyaç / olay sonrası değerlendirme:

| Tetikleyici | Etkilenen G-... / V-... | Fark edecek ve açacak rol | Dönülecek protokol |
|---|---|---|---|
| | | | P... |

| Takip işi | Beklenen çıktı | Sorumlu rol | Görevlendirme durumu | Tarih veya tetikleyici | İş durumu |
|---|---|---|---|---|---|
| T-01 | | Atanmadı | Belirlenmedi / Önerildi, kabul bekliyor / Kabul edildi | | Açık / Tamamlandı |

Zaman bakımından iddia edilemeyenler:
Sonuç: Tamamlandı / Açık
```

### Tamamlanma ve dönüş

- [ ] Oturum tarihi, sistem durumu ve kanıt tarihi birbirine karıştırılmadı.
- [ ] Şimdiki karar ve ertelenen kararın gerekçeleri açıklandı.
- [ ] Yeniden açma koşulları ilgili protokollerle eşleştirildi.
- [ ] Takip işlerinin sahibi ve zamanı biliniyor veya eksikleri açıkça kaydedildi.

Kanıtın hangi iddiaya ait olduğu anlaşılmıyorsa **P3 — Usül** bölümüne dön. Sistem değişikliği haritayı geçersizleştiriyorsa **P2 — Mekan** bölümünü yenile. Zaman ilişkileri açıklandığında **P5 — Gaye** protokolüne geç.

~~~text
  BUGUNKU KONUM
    yasam dongusu asamasi
    fikir --> tasarim --> devreye alma --> isletim --> degisiklik -->
    kullanimdan kaldirma
    oturum tarihi  =/=  sistemin en son dogrulandigi tarih

  GECMISTEN TASINAN DAYANAKLAR
    daha eski bir surum icin           -/->  guncel surumun kaniti
    uretilmis belge
    gecerlilik tasinabiliyorsa gerekcesi ve siniri yazilir

  SIMDI VERILECEK KARAR  |  ERTELENEN KARAR
    gecikmenin etkisi biliniyorsa belirtilir; her maddeye "acil"
    yazilmaz

  KAYIP SENARYOSU ICIN  ihtiyac veya plan kayitlari
    olay oncesi      hangi hazirlik onceden bulunmali
    olay sirasi      hangi bilgi ve karar imkani gerekecek
    olay sonrasi     hizmetin yeniden calismasi  |  yeniden
                     guvenilebilir bulunmasi

  YENIDEN ACMA TETIKLEYICILERI  -->  donulecek protokol
    yeni bilesen . degisen gorev . yeni dis hizmet . guncel olmayan
    kanit . gerceklesmis bir kayip
    kosulu kimin fark edecegi ve kaydi kimin acacagi belirtilir
    T-01 ...  sahibi . beklenen ciktisi . zamani ya da olay
              tetikleyicisi
    tarih belirlenmediyse:  "tarih karari bekliyor"
~~~

*Çizim 9 — Zaman: bugünkü konum; geçmişten taşınan dayanaklar; şimdiki ve ertelenen karar; olay öncesi, sırası ve sonrası; tetikleyiciler.*

### Dayanak

Kanıtın değerlendirilen sürüm ve koşullarla ilişkisini koruma yaklaşımı: SEI — Assurance Cases Overview. Tetikleyiciler ve kayıt biçimi bu belge için tasarlanmıştır.

## 5 Gaye Protokolü

### Amaç ve kapsam

Koruma düzeninin hangi faaliyete hizmet ettiğini, kimlere yarar sağladığını ve bedellerini kimlerin taşıdığını değerlendir. Teknik olarak bir hedefe ulaşabilmek, hedefi kendiliğinden haklı kılmaz. Bu protokol, başarı ölçütünü daha temel insan ve kurum amaçlarına bağlar.

“Gaye” üç ayrı kayıtla ele alınır: beyan edilen amaç, mevcut kararların veya kanıtların desteklediği yönelim ve gerekçelendirilebilir görülen amaç. Bu üçü arasında fark varsa görünür bırakılır. Kanıt bulunmadan bir kişiye gizli niyet atfedilmez; değerlendirme, bu çalışma için seçilmiş karar ve sonuçlarla sınırlı tutulur.

### Başlama koşulu ve girdiler

- `oturum-kaydi.md` içindeki **P0–P4** kayıtları.
- Korunacak `D-01` değerleri, seçilen `G-01` gereksinimleri ve `K-01` kanıtları.
- Bilinen karar sahipleri, etkilenen taraflar ve açık `T-01` işleri.

Metin düzenleyicide **P5 — Gaye** bölümünü aç. Bu çalışma bir kişinin veya kurumun yerine nihai değer kararı vermez. Görüş ayrılığı, bilinmeyen etki veya karar yetkisi eksikliği varsa bunları kayda geçirerek kapanışa taşı.

### Masaüstünde yürütme

1. **Beyan edilen amacı yaz.** Her amaca `A-01` biçiminde kimlik ver. Bir araç adı yerine korunması veya mümkün kılınması beklenen faaliyeti belirt. Amacın kimin açıklamasına ya da hangi belgeye dayandığını göster. P0'daki amaç değiştiyse eski ifadeyi sessizce silme; değişikliğin nedenini yaz.

2. **Araçla amacı ayır.** Seçilmiş her gereksinimin hangi amaca hizmet ettiğini eşleştir. Alarm üretmek, kayıt tutmak veya erişimi sınırlandırmak birer araç olabilir. Bunların daha temel faaliyet için neyi mümkün kıldığını açıkla. İlgili amacı gösterilemeyen bir kontrolü otomatik olarak gerekli sayma; açıklama ihtiyacını takip işi yap.

3. **Fiilen desteklenen yönelimi incele.** Mevcut kararlar, ölçütler veya gözlenen belgeler hangi sonucu teşvik ediyor? Beyan edilen amaçla uyuşuyorsa dayanağını yaz. Uyuşmuyorsa farkı somutlaştır. Yalnız plan bulunan bir konuda gerçekleşmiş yarar veya zarar iddia etme. Kanıt yetersizse “belirlenemedi” ifadesini kullan.

4. **Yarar ve bedeli taraflara göre ayır.** Kimin işi kolaylaşıyor, kimin erişimi daralıyor, kimin mahremiyeti veya hareket alanı etkileniyor? Karar verenle sonucu taşıyan aynı kişi mi? Sistemin sahibini bütün etkilenenlerin temsilcisi sayma. Bilinmeyen etkiyi `Bilinmiyor`, geçici bir etki kabulünü `Varsayım` olarak P1'deki V tablosuna yaz. Görüşüne ihtiyaç duyulan taraf için P4'te bir takip işi aç.

5. **Meşruiyet gerekçesini ve sınırını yaz.** Önerilen yaklaşımın hangi ihtiyacı karşıladığını, neden orantılı görüldüğünü ve hangi alternatiflerin değerlendirildiğini belirt. Kullanıcıların meşru faaliyetini kullanılamaz kılan veya bütün bedeli başka tarafa aktaran bir tercihi yeniden incele. Görüş ayrılığı varsa kapatılmış anlaşmazlık gibi sunma; kararın kime ait olduğunu yaz.

6. **Sonuç ölçütünü ve durma koşulunu seç.** Başarıyı yalnız araç veya bulgu sayısıyla ifade etme. Örneğin belirlenen değere ilişkin korumanın hangi kanıtla değerlendirileceğini ve gerekli faaliyetin sürebildiğinin nasıl anlaşılacağını belirt. Kontrolün yararını yitirdiği, fazla yük getirdiği veya temel amacı zedelediği koşullarda hangi kararın yeniden açılacağını yaz.

### Kayıt şablonu

```markdown
## P5 — Gaye

| Amaç | Beyan edilen | Fiilen desteklenen / belirlenemeyen | Meşruiyet gerekçesi ve sınırı |
|---|---|---|---|
| A-01 | | | |

Bağlantılar: A-... → D-... → G-... → K-...

| Etkilenen taraf | Beklenen veya gösterilen yarar | Bedel / risk | Kararda temsil ve belirsizlik |
|---|---|---|---|
| | | | |

Amaçla karıştırılmaması gereken araçlar:
Karar veren rol / uygulayan rol / sonucu taşıyan taraf:
Başarı ölçütü ve gerekli kanıt:
Durma veya yeniden değerlendirme koşulu:
Görüş ayrılığı / açık sorular: V-... / T-...
Sonuç: Tamamlandı / Açık
```

### Tamamlanma ve dönüş

- [ ] Beyan, fiilî yönelim ve meşruiyet değerlendirmesi ayrıldı.
- [ ] Araçlar korunacak amaç ve değerlerle ilişkilendirildi.
- [ ] Yararı ve bedeli taşıyan taraflar görünür kılındı.
- [ ] Başarı, durma ve yeniden değerlendirme ölçütleri yazıldı.
- [ ] Bilinmeyen niyet veya gerçekleşmemiş sonuç hakkında kesin hüküm kurulmadı.

Temel amaç değiştiyse **P0 — Tohum**, değer değiştiyse **P1 — Varlık**, yaklaşım amaçla uyuşmuyorsa **P3 — Usül** bölümüne dön. Açık konuların durumu görünür hâle geldiğinde **P6 — Kökleşme** protokolüne geç. Bu tamamlanma, amaç incelemesinin kayda alınmasıdır; herkes adına verilmiş bir kabul kararı değildir.

~~~text
  UC AYRI KAYIT
    beyan edilen amac
    fiilen desteklenen yonelim      mevcut kararlarin veya kanitlarin
                                    destekledigi
    gerekcelendirilebilir gorulen   mesruiyet gerekcesi ve siniri
    amac
    fark varsa gorunur birakilir; kanit bulunmadan bir kisiye gizli
    niyet atfedilmez

  ARAC  |  AMAC
    alarm uretmek . kayit tutmak . erisimi sinirlandirmak:  birer arac
    olabilir; daha temel faaliyet icin neyi mumkun kildigi aciklanir

    A-...  -->  D-...  -->  G-...  -->  K-...

  YARAR VE BEDEL TARAFLARA GORE
    kimin isi kolaylasiyor . kimin erisimi daraliyor . kimin mahremiyeti
    veya hareket alani etkileniyor
    karar veren  |  sonucu tasiyan:  ayni kisi mi?
    sistemin sahibi butun etkilenenlerin temsilcisi sayilmaz

  OLCUT VE DURMA KOSULU
    basari yalniz arac veya bulgu sayisiyla ifade edilmez
    yeniden acilir:  kontrolun yararini yitirdigi . fazla yuk
    getirdigi . temel amaci zedeledigi kosullarda
    teknik olarak bir hedefe ulasabilmek, hedefi kendiliginden hakli
    kilmaz
~~~

*Çizim 10 — Gaye: üç ayrı kayıt; araç ve amaç; yarar ve bedel; ölçüt ve durma koşulu.*

### Dayanak

Güvenlik amaçlarını bütün insan ihtiyaçlarıyla özdeşleştirmeme açısından: NIST — Relationship Between Cybersecurity and Privacy. Beyan, fiilî yönelim ve meşruiyet ayrımı bu belgenin kavramsal değerlendirme yöntemidir.

## 6 Kökleşme (Bitiş) Protokolü

### Amaç ve temel soru

Bu protokol, oturumun bulgularını dayanaklarıyla birleştirir, açık işleri görünür bırakır ve çalışmayı yeniden açılabilir bir kayıt olarak kapatır. Kökleşme, sonucu değişmez ilan etmek değildir; sonucun nereden geldiğini, hangi koşullarda geçerli olduğunu ve kim tarafından sürdürüleceğini belirlemektir.

**Temel soru:** Bu çalışma sonunda neyi söyleyebiliyoruz, bunu ne taşıyor ve hangi değişiklikte yeniden incelemeliyiz?

**Ayırt etme sorusu:** Belgenin tamamlanmasını, bütün işlerin bitmesi veya sistemin güvenli olduğunun kanıtlanmasıyla karıştırıyor muyum?

### Girdiler

- P0–P5 bölümleri doldurulmuş veya eksikleri açıkça işaretlenmiş `oturum-kaydi.md`.
- D, B, I, G, K, V, A ve T kayıtları; her biri oluşturulduğu bölümde tutulur.
- P3'teki kanıt durumları, P4'teki zaman ve yeniden değerlendirme koşulları, P5'teki amaç ve etkilenenler değerlendirmesi.

Eksik bir bölüm varsa onu doldurulmuş gibi gösterme. Oturum tamamlanamıyorsa da eldeki çalışma, durumu açıkça belirtilerek kaydedilebilir.

### Uygulama adımları

1. **Başlangıç sorusuna dön.** P0'daki soruyu bir paragrafta cevapla. Cevabın dayandığı D, G, K, V ve A kimliklerini belirt. Başlangıç sorusu değişmişse son soruyu ve değişiklik nedenini açıkça yaz.
2. **Taşıyıcı makinenin kimliğini çıkar.** Korunan faaliyeti, o faaliyeti taşıyan insanları/araçları/kuralları ve belirleyici yetki ilişkilerini birlikte tarif et. Köken, taşıyıcı, fail ve sorumluyu yeniden ayır. Ayrıca “Bu düzeni yalnız ... ile özdeşleştirmiyorum; çünkü ...” cümlesini somut örnekle tamamla.
3. **İddia ile dayanağı eşleştir.** Sonuç cümlelerini tek tek kontrol et. Planlanan kanıt, elde edilmiş kanıt yerine geçmesin. Bir kaynaktan bildirilen sonuç, bu oturumda gözlenmiş gibi yazılmasın. Kanıtı eksik sonuçların sınırını ve ilgili V kaydını belirt. Gerekçesiz kesinliği azalt veya ilgili aşamaya dön.
4. **Üç ayrı durumu kaydet.** Oturum kaydı için `Tamamlandı`, `Eksikleri kaydedilerek kapatıldı` veya `Tamamlanmadan durduruldu` durumlarından birini seç. Açık takip işleri için `Yok` veya ilgili T kimliklerini yaz. Sistem hakkında ise yalnız desteklenen sonucu ve sınırını belirt; oturum durumu güvenlik yeterliliği kararı yerine geçmez.
5. **Açık işleri sahiplikleriyle düzenle.** P4'teki takip tablosunu esas al; aynı işe yeni kimlik verme. Her iş için beklenen çıktıyı, önerilen sorumluyu, sorumluluğun kabul durumunu ve tarih ya da olay tetikleyicisini güncelle. P6'ya kapanış özetini taşı. Kişi belirlenmemişse `Atanmadı`; kişi henüz kabul etmemişse `Önerildi, kabul bekliyor` de. Kayda bir ad yazılması, görevin iletildiği veya kabul edildiği anlamına gelmez.
6. **Yeniden açılma koşullarını bağla.** P4'teki koşulları, hangi bölümlerin yeniden ele alınacağını göstererek sonuç kaydına taşı. Örneğin rol modelinin değişmesi P2 ve P3'ü; korunacak faaliyetin değişmesi P0 ve P5'i yeniden açabilir. Varsa kararlaştırılmış sonraki gözden geçirme tarihini yaz; kararlaştırılmadıysa bunu belirt.
7. **Kaydet, sabitle ve devretme durumunu belirt.** Ortak kaydı kaydet. Kapanış sürümünü `oturum-kaydi-v1.md` gibi ayrı bir kopya olarak sakla; sonraki çalışmada yeni sürüm kullan. Kayıt ve gerekli dayanak dosyalarının birlikte bulunabildiğini kontrol et. Başka birine gerçekten iletilmediyse devir alanına `İletilmedi` yaz.

### P6 çıktı şablonu

```markdown
## P6 — Kökleşme

### Kök sonuç
- Başlangıç sorusuna cevap:
- Köken:
- Taşıyıcı makine:
- Belirleyici failler:
- Sorumluluk ilişkileri ve bilinmeyenler:
- Kimdir / kim değildir:
- Sonucun dayandığı kayıt kimlikleri:
- Sonucun geçerlilik koşulları ve sınırı:

### Kapanış durumu
- Oturum kaydı: Tamamlandı / Eksikleri kaydedilerek kapatıldı / Tamamlanmadan durduruldu
- Açık takip işleri: Yok / T-...
- Sistem hakkında desteklenen sonuç:
- Henüz desteklenmeyen iddialar:

### Takip ve yeniden açılma
| İş | Beklenen çıktı | Önerilen sorumlu | Kabul durumu | Tarih veya olay | Yeniden açılacak bölüm |
|---|---|---|---|---|---|
| T-01 | ... | Atanmadı | Belirlenmedi | ... | P... |

- Sonraki gözden geçirme tarihi veya tetikleyicisi:
- Kapanış sürümü ve dosya adı:
- Kaydı sürdürecek kişi veya durum:
- Devir durumu: İletilmedi / İletildi / Alındığı doğrulandı
- Kapanış tarihi:
```

### Tamamlanma ölçütü

- [ ] Başlangıç sorusu cevaplanmış veya neden cevaplanamadığı yazılı.
- [ ] Köken, taşıyıcı, fail ve sorumlu ayrımı korunmuş.
- [ ] Her sonuç ilgili dayanak veya açık belirsizlikle ilişkilendirilmiş.
- [ ] Oturum kapanışı, açık işler ve sistem hakkındaki sonuç ayrı ayrı kaydedilmiş.
- [ ] Her açık işin sorumlu/kabul durumu ile tarih veya olay tetikleyicisi belli ya da eksikliği açık.
- [ ] Yeniden açılma koşulları ve ilgili protokoller yazılı.
- [ ] Kapanış sürümü kaydedilmiş; devir yapılmadıysa yapılmış gibi gösterilmemiş.

Bu koşullar karşılandığında oturum, seçilen kapanış durumuyla biter. Açık bir bilgi veya işlem bağımlılığı, kayıt altına alınmış olduğu için çözülmüş sayılmaz. Yeniden açıldığında eski kapanış kopyasını değiştirmeden yeni sürümde ilgili protokolden devam et.

~~~text
  KOKLESME  sonucun nereden geldigi . hangi kosullarda gecerli oldugu .
  kim tarafindan surdurulecegi
    belgenin tamamlanmasi  -/->  butun islerin bitmesi veya sistemin
                                 guvenli oldugunun kanitlanmasi

  UC AYRI DURUM
    oturum kaydi             Tamamlandi | Eksikleri kaydedilerek
                             kapatildi | Tamamlanmadan durduruldu
    acik takip isleri        Yok | T-...
    sistem hakkinda          yalniz desteklenen sonuc ve siniri
    oturum durumu, guvenlik yeterliligi karari yerine gecmez

  IDDIA VE DAYANAK
    planlanan kanit      -/->  elde edilmis kanit
    bir kaynaktan        -/->  bu oturumda gozlenmis
    bildirilen sonuc

  YENIDEN ACILMA
    rol modelinin degismesi           -->  P2 ve P3
    korunacak faaliyetin degismesi    -->  P0 ve P5

  KAPANIS
    oturum-kaydi.md  -->  oturum-kaydi-v1.md  kapanis surumu, ayri kopya
    yeniden acildiginda eski kapanis kopyasi degistirilmeden yeni
    surumde ilgili protokolden devam edilir
    devir durumu:  Iletilmedi | Iletildi | Alindigi dogrulandi
    kayda bir ad yazilmasi, gorevin iletildigi veya kabul edildigi
    anlamina gelmez
~~~

*Çizim 11 — Kökleşme: üç ayrı durum; iddia ve dayanak; yeniden açılma; kapanış ve devir.*

### Dayanak

Bu protokol, güvence iddialarının kanıtla ilişkilendirilmesi ve değişiklikler karşısında güncel tutulması fikrini kullanır: SEI — Assurance Cases Overview. Kökleşme adı ve kapanış durumları bu belge için tasarlanmıştır; resmî bir sertifikasyon kararı değildir.

## Örnek uygulama: ortak proje arşivi

Bu bölüm tamamen varsayımsal bir doldurma örneğidir. Gerçek bir sistem incelenmemiş veya sınanmamıştır. Verilen kayıt kimlikleri yalnız bu örneğe aittir.

**P0 — Tohum:** İnceleme nesnesi bir ekibin ortak proje arşivi; başlangıç sorusu, görevinden ayrılan bir kullanıcının erişiminin nasıl sona erdiğidir. Bu örneğin tek girdisi, “erişim listesi elle güncelleniyor” biçimindeki senaryo varsayımıdır.

**P1 — Varlık:** D-01, ekip üyelerinin proje belgeleri üzerinde belirlenmiş yetkilerle çalışabilmesidir. Kayıp, görevi sona ermiş birinin erişiminin sürmesi veya çalışan bir üyenin gerekli erişimini kaybetmesidir. B-01 kullanıcı, B-02 arşiv uygulaması, B-03 erişim listesini yöneten roldür. V-01, yazılı erişim listesiyle etkin oturumların aynı anda güncellendiği varsayımıdır; henüz dayanağı yoktur.

**P2 — Mekan:** I-01, B-03'ün B-01 için B-02 üzerinde erişim tanımlayabilmesidir. Ayrıca mevcut oturumları kimin sona erdirebildiği bilinmemektedir. Kurum içi olmakla bütün verilere erişebilmek özdeşleştirilmez. Yetkiyi uygulayan yazılım ile yetkiyi belirleyen rol ayrı tutulur.

**P3 — Usül:** G-01, görevi sona eren kullanıcı için erişimin, ilgili faaliyet açısından kararlaştırılacak sürede kaldırılmasıdır. Süre henüz belirlenmediği için gereksinim tamamlanmış sayılmaz. K-01, rol değişikliği sonrası mevcut oturumları ve farklı erişim yollarını inceleyecek teknik sınama planıdır; durumu `Planlanan`dır. Bu kayıttan başarılı test sonucu çıkarılmaz.

**P4 — Zaman:** T-01, erişim kaldırma süresinin kararlaştırılması; T-02, V-01'i değerlendirecek K-01 sınamasının kapsamı belirlenerek yürütülmesidir. İşlerin asıl kaydı burada tutulur; ikisinin de sorumlusu `Atanmadı`, iş durumu `Açık`tır. Rol modeli, kimlik hizmeti veya oturum yönetimi değiştiğinde P2 ve P3 yeniden açılır. Belirli bir gözden geçirme tarihi kararlaştırılmadığı için tarih alanında `Kararlaştırılmadı` yazar.

**P5 — Gaye:** A-01, ortak çalışmanın yetki sınırları korunarak sürmesidir. “Hiç erişim kalmasın” hedefi bu gayeyle aynı değildir; çalışmaya devam eden kişilerin gerekli erişimi de korunmalıdır. Beyan edilen amacı destekleyen gerçek işletim davranışı hakkında bu senaryoda kanıt yoktur.

**P6 — Kökleşme:** Oturum `Eksikleri kaydedilerek kapatıldı` durumundadır. P4'teki T-01 ve T-02 kapanışta hâlâ açıktır; her ikisinin sorumlusu `Atanmadı`dır. Desteklenen sonuç, koruma ihtiyacının ve incelenecek ilişkinin tanımlanmış olmasıdır. Sistemin erişimi zamanında kaldırdığı henüz gösterilmemiştir.

Bu örneğin taşıyıcı makinesi yalnız B-02 değildir; kullanıcı, uygulama, yetki kararı, bakım sorumluluğu ve bunları bağlayan süreç birlikte değerlendirilir. Oturumun kapanması, V-01'in doğrulanması veya T-01/T-02'nin tamamlanması anlamına gelmez.

~~~text
  VARSAYIMSAL ORNEK  ortak proje arsivi
    soru:  gorevinden ayrilan bir kullanicinin erisimi nasil sona
    eriyor?  tek girdi:  "erisim listesi elle guncelleniyor"

    B-01  kullanici
    B-02  arsiv uygulamasi
    B-03  erisim listesini yoneten rol

    I-01  B-03  ---- erisim tanimlar ---->  B-01 icin, B-02 uzerinde
    bilinmiyor:  mevcut oturumlari kimin sona erdirebildigi

    D-01  ekip uyelerinin proje belgeleri uzerinde belirlenmis
          yetkilerle calisabilmesi
    V-01  yazili erisim listesiyle etkin oturumlarin ayni anda
          guncellendigi varsayimi; dayanagi yok
    G-01  erisimin kararlastirilacak surede kaldirilmasi; sure
          belirlenmedi
    K-01  teknik sinama plani:  Planlanan
    T-01, T-02  Atanmadi . Acik
    A-01  ortak calismanin yetki sinirlari korunarak surmesi
    P6    Eksikleri kaydedilerek kapatildi
    tasiyici makine yalniz B-02 degildir
~~~

*Çizim 12 — Örnek uygulama: ortak proje arşivinin kayıtları.*

## Kaynaklar ve bu belgeyle ilişkileri

Kaynaklar kavramsal dayanak sağlar. Yedi protokolün adları ve kayıt biçimleri bu belge için oluşturulmuştur. Bir kaynağın varlığı, belirli bir oturumda kullanılan sistem hakkında kanıt oluşturmaz.

1. NIST SP 800-160 Vol. 1 Rev. 1 — Engineering Trustworthy Secure Systems (https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final): Sistem, koruma ihtiyaçları, mühendislik ve yaşam döngüsü yaklaşımı.
2. Ross Anderson — What Is Security Engineering? (https://www.cl.cam.ac.uk/archive/rja14/Papers/SEv3-ch01.pdf): İnsan, kurum, politika, mekanizma, güvence ve teşvik ilişkileri.
3. SEI — Arguing Security: Creating Security Assurance Cases (https://www.sei.cmu.edu/library/arguing-security-creating-security-assurance-cases/): Güvenlik iddiası, gerekçe ve kanıtın ilişkilendirilmesi.
4. SEI — Assurance Cases Overview (https://sei.cmu.edu/library/assurance-cases-overview/): Güvence dayanaklarının kapsamı ve güncel sisteme uygulanabilirliği.
5. NIST SP 800-207 — Zero Trust Architecture (https://csrc.nist.gov/pubs/sp/800/207/final): Konumu tek başına güven gerekçesi saymama yaklaşımı.
6. NIST SP 800-160 Vol. 2 Rev. 1 — Developing Cyber-Resilient Systems (https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final): Öngörme, dayanma, toparlanma ve uyum sağlama yetenekleri.
7. NIST NCCoE — Relationship Between Cybersecurity and Privacy (https://www.nccoe.nist.gov/relationship-between-cybersecurity-and-privacy): Siber güvenlikle mahremiyetin örtüşen ve ayrışan amaçları.
8. W. Ross Ashby — An Introduction to Cybernetics (https://www.ashby.info/Ashby-Introduction-to-Cybernetics.pdf): Makineyi davranış, düzenleme ve geri besleme bakımından okumak için kavramsal kaynak.

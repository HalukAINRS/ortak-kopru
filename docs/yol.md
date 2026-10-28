# Açılıştan gerçeğe: yol

<!-- uretilen:yol -->

Açılış, Ortak Köprü'nün ne olmak istediğini söylüyor. Bu sayfa, oraya nasıl varılacağını adım adım gösteriyor. Her adım için neyin değişeceği, neden gerektiği, ne zaman atılabileceği ve bitince sizin için neyin değişeceği yazılı.

Bu yol kendini denetler. Her adımın ölçütü var ve ölçütler her değişiklikte yeniden sınanıyor. Bir adım bitince bu sayfa da, açılıştaki durum yazısı da değişmek zorunda. Ölçütler ve dosyalar [yolun teknik ekinde](teknik/yol-teknik.md), bu yolun nasıl ortaya çıktığı [geçmiş işler](gecmis/README.md) bölümünde duruyor.

## Bugün nerede duruyoruz

Bugün altı ilkenin ikisi tam olarak işliyor, dördü kısmen işliyor. Yolun yedi adımından biri tamam, beşi açık, biri ufukta. Şu an atılabilecek adım: Katkı kalıbı. Kararı bekleyen adım: Gönderici yalnız seçileni gönderir. Öteki açık adımlar bir ön koşulun bitmesini bekliyor.

Aşağıdaki gösterge her ilkeye bağlı adımları sayar. Dolu kare biten, boş kare açık, eşkenar dörtgen ufuktaki adımı gösterir.

**İlkelerin göstergesi** · mühendis çizimi

```text
  ilke                                adımlar   açılışta
  ──────────────────────────────────  ────────  ────────────────
  1 Karşılıklılık                     □□◇       kısmen işliyor
  2 Yerel merkez                      □□        kısmen işliyor
  3 Köken ve sahiplik                 ■         işliyor
  4 Sınır                             □         kısmen işliyor
  5 Açık katılım                      □□        kısmen işliyor
  6 Doğrulanabilirlik ve geri dönüş   ■         işliyor
```

## Varılacak yer

Yolun sonunda Ortak Köprü, açılışta söylediği şey olur. Yerel kullanıcı neyi paylaşacağını seçer ve seçtiği şey kaynağıyla dışarı çıkar. Dışarıdaki biri bir paragrafı okur, aklına takılanı o paragrafın yanına yazar. Yazdığı şey yerel kullanıcının önüne düşer, karşılığı aynı yoldan geri döner. Her adım kayda geçer ve hiçbir şey olduğundan fazla gösterilmez.

Aşağıdaki resim bunu bir manzara gibi gösteriyor. Solda yerel kullanıcının çalışma yeri ve kapısı var. Ortada iki yöne taşıyan köprü, sağda dışarıdaki insanlar duruyor. Aşağıdan kapıya uzanan kesik çizgi, bugünden oraya giden yol.

**Varılacak yer** · ressam çizimi

```text
                \   |   /
              ─   .───.   ─        varılacak yer
   ____________  (     )  ______________________________
               \__`───'__/
  ┌─────────┐                                o    o
  │ yerel   │    ╔═════════════════════╗    /|\  /|\
  │ çalışma ├════╣ ← soru, katkı       ╠════ / \  / \
  │  ┌──┐   │    ║        yanıt, kayıt →║   dışarıdaki
  └──┤░░├───┘    ╚═════════════════════╝   insanlar
     └┬─┘ kapı ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      :
      :  yol: altı adım
      :
      x  bugün buradayız
```

## Yapının planı

Aşağıdaki plan, Ortak Köprü'yü üstten görülen bir yapı gibi gösterir. Solda yerel kullanıcının odası, sağda dış avlu var. Aradaki duvarda tek bir kapı bulunuyor. Oklar neyin hangi yönde geçtiğini, parantez içindeki sayılar o geçişi koruyan ilkeyi gösteriyor.

Plan bugün yarı yarıya gerçek. Seçilen dosyaların dışarı çıkışı ve kaynakların sürümüyle içeri girişi çalışıyor. Soruların gelen kutusuna inmesi ve yanıtın aynı yoldan dönmesi henüz yok. Yol, eksik okları tek tek çiziyor.

**Yapının planı** · mimar çizimi

```text
  PLAN · üstten görünüş                     ölçek: yok
  ┌────────────────────────────┬──────┬──────────────────────┐
  │ YEREL ODA                  │      │ DIŞ AVLU · Web       │
  │                            │      │                      │
  │ [çalışma]─▶[seçilen]────────────────▶[yayın]        (3)  │
  │              (2)           │  K   │                      │
  │ [gelen kutusu]◀──────────────────────[kaynak]       (3)  │
  │      │ (1)                 │  A   │                      │
  │      ▼                     │  P   │                      │
  │ [yerel kullanıcı]◀───────────────────[soru, katkı]  (5)  │
  │      └──────────────────────────────▶[yanıt]        (1)  │
  │                            │  I   │                      │
  │ duvar (4): gizli olan      │      │        [okur]        │
  │ bu odadan çıkmaz           │      │                      │
  └────────────────────────────┴──────┴──────────────────────┘
   (6) her ok bir kayıt bırakır; hiçbir ok iz silmez
```

## Adımlar

Yol yedi adımdan oluşuyor. Aşağıdaki ağaçta her adım, bitmesini beklediği adımın altında duruyor. Sağdaki işaret adımın bugünkü durumunu gösteriyor.

**Yolun ağacı** · mühendis çizimi

```text
  (0) Zemin                                         ■ tamam
   ├─▶ (1) Gönderici yalnız seçileni gönderir       □ karar
   └─▶ (2) Katkı kalıbı                             □ atılabilir
       ├─▶ (3) Gelen kutusu                         □ ön koşul
       │   └─▶ (4) Yanıt geri döner                 □ ön koşul
       │       └─▶ (6) Kapı GitHub dışına açılır    ◇ ufukta
       └─▶ (5) İlk dış katkı                        □ ön koşul
```

### 0. Zemin

**Durum:** Tamam.

**Ne?** Açılış yazıldı, depo alanlarına ayrıldı ve kendini denetleyen bir harita kuruldu.

**Neden?** Bir yerin gerçeğe dönüştüğünü görebilmek için önce neyin söz verildiğini ve neyin bugün işlediğini ayırmak gerekir.

**Nerede?** Deponun kendisinde: açılışta, haritada ve denetimlerde.

**Nereden nereye?** İçeride kalır; dışarıya bir şey taşımaz.

**Nasıl?** Niyet, altı ilke ve her ilkenin bugünkü durumu bir kayda yazıldı. Sayfalar o kayıttan üretiliyor ve her değişiklikte yeniden sınanıyor.

**Ne zaman?** Bir ön koşulu yok.

**Ne için?** Bu adım şu ilkelere hizmet eder: 3. ilke (Köken ve sahiplik), 6. ilke (Doğrulanabilirlik ve geri dönüş).

**Ne kadar?** Orta büyüklükte bir iş.

**Bitince:** Okuduğunuz her durum yazısı bir denetime dayanıyor. Bir şey değişirse yazı da değişmek zorunda.

### 1. Gönderici yalnız seçileni gönderir

**Durum:** Sahibinin kararını bekliyor; ön koşulu bitti.

**Ne?** Yerel bilgisayardaki eski paylaşım aracı, yalnız ortak defteri ve çağrı kayıtlarını gönderecek biçimde daraltılır.

**Neden?** Bu araç bugün çalışma klasöründe unutulmuş herhangi bir dosyayı da herkese açık yere gönderebiliyor. Bu, yerel kullanıcının seçmediği bir şeyin dışarı çıkabilmesi demek.

**Nerede?** Yerel bilgisayardaki eski paylaşım aracında.

**Nereden nereye?** Yerel bilgisayardan Web'e giden çıkışta.

**Nasıl?** Araç, bulut tarafındaki eşi gibi yalnız belirli dosyaları hazırlar. Başka bir dosyayı paylaşmak isteyen kapıyı kullanır; kapı yalnız seçileni taşır.

**Ne zaman?** Ön koşulu bitti: Zemin. Ayrıca Haluk'un bir karar vermesi gerekiyor. Yerel gönderici, defter ve çağrı kayıtları dışındaki dosyaları göndermeyi bıraksın mı? Bırakırsa öteki dosyalar kapıdan, seçilerek gider.

**Ne için?** Bu adım şu ilkelere hizmet eder: 2. ilke (Yerel merkez), 4. ilke (Sınır).

**Ne kadar?** Küçük bir değişiklik.

**Bitince:** Dışarı çıkan her şey bir seçimden geçmiş olur. Yerel merkez ve sınır ilkeleri bu açıdan tam işler.

### 2. Katkı kalıbı

**Durum:** Atılabilir: ön koşulu bitti ve bir karar beklemiyor.

**Ne?** Her yazının her bölümünün yanında bir karşılık bağlantısı olur. Bağlantı, hangi yazıya ve hangi bölüme karşılık verildiğini kendiliğinden yazan bir katkı kalıbı açar.

**Neden?** Bugün bir soru sormak mümkün, ama sorunun hangi yazıya ait olduğunu soranın kendisi anlatmak zorunda. Getirilen şeyin etkilediği yere bağlanması kişinin dikkatine kalıyor.

**Nerede?** Web'deki okuma sayfalarında ve GitHub'daki konu açma ekranında.

**Nereden nereye?** Okurdan, okuduğu yazının yanına.

**Nasıl?** GitHub'a bir katkı kalıbı eklenir: soru, kaynak ya da düzeltme seçilir, ilgili yerin adresi hazır gelir. Web sayfaları her bölüm için bu adresi taşıyan bağlantıyı üretir.

**Ne zaman?** Ön koşulu bitti: Zemin.

**Ne için?** Bu adım şu ilkeye hizmet eder: 5. ilke (Açık katılım).

**Ne kadar?** Küçük bir değişiklik.

**Bitince:** Bir paragrafı okurken aklınıza takılanı tek tıkla yazabilirsiniz. Yazdığınız şey o paragrafa bağlı olarak görünür.

### 3. Gelen kutusu

**Durum:** Ön koşulunun bitmesini bekliyor.

**Ne?** Dışarıdan gelen sorular ve katkılar, yerel kullanıcının bilgisayarındaki ayrı bir gelen kutusuna iner.

**Neden?** Bugün dışarıdaki birinin sorusu yerel kullanıcıya ancak GitHub'ın kendi bildirimleriyle ulaşıyor. Köprünün dış ucu açık, ama iç ucu kapıya bağlı değil.

**Nerede?** Kapıda ve yerel kullanıcının bilgisayarında.

**Nereden nereye?** Web'den yerel bilgisayara.

**Nasıl?** Kapıya yeni bir iş eklenir. Açık konuları okur ve her birini kimin, ne zaman yazdığıyla ve hangi yazıya bağlı olduğuyla gelen kutusuna koyar. Gelen kutusu yerel çalışmaya kendiliğinden karışmaz; yerel kullanıcı önce bakar.

**Ne zaman?** Önce şu adımın bitmesi gerekiyor: Katkı kalıbı. Ayrıca Haluk'un bir karar vermesi gerekiyor. GitHub'a hangi yetkiyle bakılsın: yalnız herkese açık okumayla mı, kişisel bir anahtarla mı? Gelen kutusu bilgisayarda nerede dursun?

**Ne için?** Bu adım şu ilkelere hizmet eder: 1. ilke (Karşılıklılık), 2. ilke (Yerel merkez).

**Ne kadar?** Orta büyüklükte bir iş.

**Bitince:** Sorunuz bir bildirime takılıp kalmaz. Yerel kullanıcının önüne, kaynağıyla birlikte düşer.

### 4. Yanıt geri döner

**Durum:** Ön koşulunun bitmesini bekliyor.

**Ne?** Yerel kullanıcının gelen kutusundaki bir şeye verdiği karşılık, kapıdan geçerek soranın yanına döner.

**Neden?** Karşılıklılık yalnız gelmekle tamamlanmaz. Yanıtın da aynı yoldan, kaydıyla birlikte geri dönmesi gerekir.

**Nerede?** Kapıda ve GitHub'daki konunun altında.

**Nereden nereye?** Yerel bilgisayardan Web'e, soranın yanına.

**Nasıl?** Kapıya bir iş daha eklenir. Yerel kullanıcının seçtiği yanıtı ilgili konuya yazar ve bunu ayrı bir olay olarak kaydeder. Yanıt yazılmadan gönderilmiş sayılmaz.

**Ne zaman?** Önce şu adımın bitmesi gerekiyor: Gelen kutusu. Ayrıca Haluk'un bir karar vermesi gerekiyor. Yanıtlar GitHub'a hangi hesapla yazılsın?

**Ne için?** Bu adım şu ilkeye hizmet eder: 1. ilke (Karşılıklılık).

**Ne kadar?** Orta büyüklükte bir iş.

**Bitince:** Sorduğunuz şeyin karşılığını, sorduğunuz yerde görürsünüz. Karşılıklılık ilkesi tam işler.

### 5. İlk dış katkı

**Durum:** Ön koşulunun bitmesini bekliyor.

**Ne?** Haluk dışından biri bir soru, kaynak ya da düzeltme getirir ve bu katkı karşılık bulur.

**Neden?** Açık katılım ilkesi, yollar açık olduğu için değil, biri gerçekten geldiği için işler. Bugüne kadar dışarıdan kimse yazmadı.

**Nerede?** GitHub'da, herkese açık konular arasında.

**Nereden nereye?** Dışarıdaki birinden yerel kullanıcıya ve geri.

**Nasıl?** Bu adım bir yazılımla atılmaz. Katkı kalıbı hazır olduktan sonra ilk dış katkının adresi ve ona verilen yanıtın adresi kayda yazılır.

**Ne zaman?** Önce şu adımın bitmesi gerekiyor: Katkı kalıbı.

**Ne için?** Bu adım şu ilkeye hizmet eder: 5. ilke (Açık katılım).

**Ne kadar?** Küçük bir değişiklik.

**Bitince:** İlk katkı sizinki olabilir. O gün bu sayfadaki durum da değişir.

### 6. Kapı GitHub dışına açılır

**Durum:** Ufukta; zorunlu değil.

**Ne?** Kapı, GitHub'ın yanında ikinci bir dış alana da açılır; örneğin bir dosya hizmetine.

**Neden?** Niyet, Web ile yerel bilgisayar arasında bir kapıdan söz ediyor. Bugün Web tarafında yalnız GitHub var.

**Nerede?** Kapıda ve yeni dış alanda.

**Nereden nereye?** Yerel bilgisayar ile ikinci bir dış alan arasında, iki yönde.

**Nasıl?** Kapının aktarım kuralları aynı kalır; yalnız yeni alan için bir bağlantı parçası eklenir. Seçim, kayıt ve sınırlar değişmez.

**Ne zaman?** Önce şu adımın bitmesi gerekiyor: Yanıt geri döner. Ayrıca Haluk'un bir karar vermesi gerekiyor. Kapı hangi dış alana açılsın: bir dosya hizmetine mi, başka bir siteye mi?

**Ne için?** Bu adım şu ilkeye hizmet eder: 1. ilke (Karşılıklılık).

**Ne kadar?** Büyük bir iş.

**Bitince:** Bu adım zorunlu değil. Altı ilke bu adım atılmadan da tam işleyebilir; bu adım ufuktadır.

## Bu yol nasıl izlenir

Her adımın yanında bir durum yazar: tamam, atılabilir, karar bekliyor, ön koşul bekliyor, dışarıdan bekleniyor ya da ufukta. Bu durumlar elle yazılmaz; ölçütlerden hesaplanır. Bir adımın bütün ölçütleri karşılandığında adım tamam olur.

Bir ilkeye bağlı bütün zorunlu adımlar bitince, açılışta o ilkenin durumu güncellenmek zorundadır. Güncellenmezse denetim kırılır. Tersine, bir ilke tam işliyor diye yazılmışsa ona bağlı açık bir adım kalamaz.

## Siz ne yapabilirsiniz

Bu yolun en kısa adımı sizin elinizde. Açılışı ya da bu sayfayı okuyup bir soru sorar, bir kaynak ya da düzeltme getirirseniz dışarıdan gelen ilk katkı gerçekleşmiş olur. Bunun için [GitHub'da bir konu açın](https://github.com/HalukAINRS/ortak-kopru/issues/new); GitHub buna Issue der.

Hangi yazıya ve hangi adıma karşılık verdiğinizi yazmanız yeter. Bir adımın nasıl atılacağına dair öneriniz varsa onu da yazabilirsiniz. Öneriler yerel kullanıcının kararına sunulur, kendiliğinden uygulanmaz.

## Birkaç kelime

Bu sayfada geçen birkaç kelime: **İnternet ve Web:** Bu sayfada ikisi aynı anlamda kullanılıyor: herkesin bir tarayıcıyla ulaşabildiği dış dünya. **Yerel kullanıcı:** Ortak Köprü'nün öbür ucundaki bilgisayarın sahibi. Bugün bu kişi Haluk. **GitHub:** Yazıların ve dosyaların herkese açık durduğu, insanların birlikte çalışmak için kullandığı bir internet sitesi. Ortak Köprü'nün dış yüzü orada. **Depo:** GitHub'da bir çalışmanın bütün dosyalarını ve geçmişini bir arada tutan yer. Ortak Köprü bir depodur. **Issue:** GitHub'da bir depoya soru, öneri ya da hata bildirimi yazmanın yolu. Okumak için hesap gerekmez; yazmak için ücretsiz bir GitHub hesabı yeter. **Sürüm:** Bir dosyanın belirli bir andaki hâli. Dosya sonradan değişse de alınan sürüm aynı kalır.

<!-- /uretilen:yol -->

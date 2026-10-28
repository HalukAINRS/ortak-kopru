# Açılışın teknik eki

Bu sayfa, [Açılış: Kapı ve Köprü](../acilis.md) belgesinin teknik eşidir. Açılış ilk kez gelen okuyucu için sade yazıldı. Burada aynı tanımın depodaki karşılıkları duruyor: soruların bugün hangi dosyalarla yanıtlandığı, beşli ile dörtlünün yirmi kesişimi, ilkeleri taşıyan dosyalar, niyete kalan mesafe ve bu tabloları üreten araç. Bütün tablolar [açılış kaydından](../acilis.json) üretilir. Açılışın nasıl ortaya çıktığı [geçmiş işler](../gecmis/README.md#açılışa-giden-yol) sayfasında anlatılıyor.

## Tanımın tam hâli

Açılış belgesi tanımın sade hâlini kullanır. Tam hâli şudur:

<!-- uretilen:acilis_tanim -->

Ortak Köprü, yerel kullanıcının bilgisayarındaki çalışma ile Web arasında bir kapı, yerel kullanıcı ile dışarıdaki bireyler arasında bir köprüdür. Kapıdan, yerel kullanıcının seçtiği içerik kaynağı ve sürümüyle dışarı çıkar; Web'deki kaynaklar kesin sürümleriyle içeri alınır. Köprüden, dışarıdaki biri önceki konuşmaları bilmeden okuyabilir, sorabilir ve katkı getirebilir; yerel kullanıcının karşılığı ona geri döner. Her geçiş, nereden geldiği, nereye gittiği, ne kadar olduğu ve neden yapıldığıyla izlenebilir kalır.

<!-- /uretilen:acilis_tanim -->

## Beşli ve dörtlü: kapı ve geçiş

Dokuz soru iki gruba ayrıldı. Beşli (Ne, Nerede, Nasıl, Ne zaman, Ne için) kapının kendisini, yani bir yapıyı tanımlıyor. Dörtlü (Nereden, Nereye, Ne kadar, Neden) kapıdan geçeni, yani bir hareketi tanımlıyor. Dörtlü aynı zamanda her geçişin yanında taşınması gereken dört bilginin adıdır: köken, varış, ölçü ve gerekçe. Bunlardan biri kaybolan bir geçiş izlenemez hâle gelir.

Her soru iki biçimde yanıtlandı: niyete göre kapının ne olması gerektiği ve bugün depoda gözlenen karşılığı.

<!-- uretilen:acilis_sorular -->

| Soru | Grup | Niyete göre | Bugün depoda | Durum |
| --- | --- | --- | --- | --- |
| Ne? | Kapının kendisi | İki yönlü bir geçit: bilgisayardaki yerel çalışma ile Web arasında bir kapı, yerel kullanıcı ile harici bireyler arasında bir köprü. Kapı içerik taşır, köprü insanları birbirine bağlar. | Kapı dosyalar için var: kapi.py seçilmiş dosyaları GitHub'a gönderir ve GitHub'dan kesin sürümle alır. Köprü yalnız GitHub'ın kendi araçlarıyla (Pages, Issues, PR) var; dışarıdan gelen bir katkıyı yerel kullanıcıya getiren bir araç yok. | kısmen |
| Nerede? | Kapının kendisi | İki kenarda ve aralarında. Bir kenar yerel kullanıcının bilgisayarı, öbür kenar Web. Kapının kendisi bu GitHub deposudur: kod, kayıt ve herkese açık yüz. Geçişlerin özel kaydı ise bilgisayarda, Git'in dışında durur. | Herkese açık yüz github.com/HalukAINRS/ortak-kopru ve onun Pages yayını. Yerel kenar, teknik ayrıntılara göre Y:\HalukAI\Ortak_Kopru\kopru\ klasörü. Aktarımların özel kaydı kapi.py'ye verilen --exchange-dir dizininde. | var |
| Nasıl? | Kapının kendisi | Kapıda: seç, sabitle, planla, gönder, uzlaştır; ya da al, sabitle, incele. Köprüde: oku, sor, getir, karşılık ver. Her adım ayrı kaydedilir ve hiçbiri bir öncekinin yerine geçmez. | Kapının adımları kapi.py'nin on alt komutudur (prepare, plan, send, reconcile, fetch, materialize ve kayıt komutları). Köprünün adımları GitHub arayüzünde elle atılır. | kısmen |
| Ne zaman? | Kapının kendisi | Yerel kullanıcı istediğinde. Kapı kendiliğinden açılmaz. Her geçiş kendi zamanıyla kaydedilir ve o ana ait bir gözlem olarak okunur. | kapi.py yalnız komutla çalışır. Saatlik bulut otomasyonu yalnız kopru.html kayıtlarına yanıt verir, dosya taşımaz; 24 Ekim'den beri modeli de çağırmıyor. | var |
| Ne için? | Kapının kendisi | Yerel çalışmanın sonucunu dünyayla paylaşmak, dünyadaki kaynağı yerele getirmek ve dışarıdaki bir bireyin yerel kullanıcıyla, aradaki bağlam kaybolmadan bağ kurabilmesi için. | Paylaşma ve getirme dosya düzeyinde çalışıyor. Bireylerle bağ için okuma sayfaları ve Issues açık, ama bugüne kadar dışarıdan bir Issue ya da yorum gelmedi; tek Issue (#16) yerel kullanıcının kendi kaydı. | kısmen |
| Nereden? | Geçişin kendisi | İki kaynaktan. Yerelden: yerel kullanıcının açıkça seçtiği dosya, rapor ya da söz. Dışarıdan: Web'deki bir kaynak, kesin bir commit'e bağlı olarak; ya da harici bir bireyin sorusu, kaynağı, düzeltmesi. | Yerel seçim prepare ile, dış kaynak fetch ile sabitleniyor. Bireylerin katkısı Issues ve PR'dan gelebiliyor, ama onu yerel tarafa taşıyan bir adım yok. | kısmen |
| Nereye? | Geçişin kendisi | Dışarıya: GitHub'da yeni bir dala ve istenirse taslak bir PR'a. İçeriye: yerel kullanıcının inceleyeceği yeni bir dizine. Bireyin katkısı yerel kullanıcıya; yerel kullanıcının karşılığı o bireye ve etkilediği metnin yanına. | Dosya yönleri kodda var: mevcut dalın üzerine yazılmaz, PR birleştirilmez, alınan dosya projeye kendiliğinden uygulanmaz. Karşılığın bireye ve ilgili metne dönmesi elle yapılıyor. | kısmen |
| Ne kadar? | Geçişin kendisi | Yalnız seçilen kadar ve sınırlı: bir aktarımda en çok 64 dosya, dosya başına 8 MiB, toplam 64 MiB. Geçen her bayt SHA-256 ile sabitlenir; sayılmayan bir şey geçmiş sayılmaz. | Sınırlar src/ortak_kopru/exchange.py'de. Ama yerel gönderici yerel/kopru_gonder.ps1 kapının dışından çalışıyor ve çalışma klasöründe kalan izlenmeyen her dosyayı gönderebiliyor (R-17). | kısmen |
| Neden? | Geçişin kendisi | Yerel çalışma kendi yerinde ve kendi araçlarında kalsın, ama sonucu ile dünyadaki karşılığı birbirinden kopmasın; söz sahibiyle, kaynak sürümüyle taşınsın ve önceki söz kaybolmasın. | Karar 0002 yerel ile dış alan arasındaki sınırı, kayıt defteri sözün sahibiyle korunmasını taşıyor. | var |

<!-- /uretilen:acilis_sorular -->

Dokuz yanıttan üçü bugün niyetle örtüşüyor: kapının nerede durduğu, ne zaman açıldığı ve neden var olduğu. Diğer altısı kısmen örtüşüyor ve bu altı kısmi yanıtın arkasında yalnız iki eksik var. Birincisi köprünün kişiler arası ucu: dışarıdan gelen bir katkıyı yerel kullanıcıya getiren ve karşılığını geri götüren bir adım yok. Ne, Nasıl, Ne için, Nereden ve Nereye bu yüzden kısmi kalıyor. İkincisi yerel gönderici `kopru_gonder.ps1`: kapının dışından çalışıp seçilmemiş dosyaları da gönderebiliyor ve Ne kadar yanıtını kısmi bırakıyor.

Her sorunun gölgesi de soruldu:

<!-- uretilen:acilis_varyantlar -->

| Soru | Varyant | Yanıt |
| --- | --- | --- |
| Ne? | Ne değildir? | Bir eşitleme ya da aynalama aracı değildir: yerel klasörü dışarı açmaz, dışarıdakini yerelde kendiliğinden uygulamaz. Bir arşiv de değildir; arşiv, kapıdan geçmiş olanın izidir. |
| Nerede? | Nerede durmaz? | Kişisel dosyalar, gizli değerler ve özel çalışma alanı kapının herkese açık tarafında durmaz. |
| Nasıl? | Nasıl geri alınır? | Gönderim yeni bir dala gider ve PR birleştirilmez; geri almak dalı silmektir. Alınan dosya yeni bir dizine çıkar; geri almak dizini silmektir. Herkese açık geçmişe girmiş bir dosya ise geri alınamaz; bu yüzden en sıkı denetim çıkış yönündedir. |
| Ne zaman? | Ne zamana kadar geçerlidir? | Bir geçişin kaydı kendi anına aittir. Alınan bir kaynak, alındığı commit'te sabit kalır; daha yeni sürüm yeniden alınır, eski kayıt silinmez. |
| Ne için? | Kimin için? | Yerel kullanıcı için: neyin çıkıp gireceğine o karar verir. Harici birey için: girişin kapısı ve karşılığın adresi. Katılımcı modeller için: işin kaynağını ve devrini taşıyan ortak yer; bağı taşırlar, yerine geçmezler. |
| Ne için? | Ne için değildir? | Bütün yerel işin buradan geçmesi için değildir; bir Issue açılması yerel bir aracı çalıştırmaz. |
| Nereden? | Nereden gelmez? | Kendiliğinden hiçbir yerden: ne yerel klasörün tamamı ne bir dış hizmetin otomatik akışı kapıdan seçimsiz geçer. |
| Nereye? | Nereye gitmez? | Belirteç, anahtar, IP adresi, cihaz kimliği ve özel çalışma alanı dışarıya gitmez; dışarıdan alınan dosya yerel projenin içine kendiliğinden gitmez. |
| Ne kadar? | Ne kadarı bekliyor? | Dışarıdan gelip cevap bekleyen bir Issue yok. Defterde ise 16 kayıt, cevap verebilecek bir yolu olmayan adreslerde bekliyor. |
| Neden? | Neden başka türlü değil? | Bir bulut eşitlemesi yerel klasörü bütünüyle dışarı açardı; bir sohbet geçmişi sözün sahibini ve sürümünü kaybettirirdi. Kapı seçer, köprü bağlar, ikisi de iz bırakır. |

<!-- /uretilen:acilis_varyantlar -->

## Yirmi kesişim

Beşlinin her sorusu dörtlünün her sorusuyla birleştirildi. Satırlar kapının bir yönünü, sütunlar geçişin bir yönünü taşıyor:

<!-- uretilen:acilis_matris -->

| Kapı \ Geçiş | Nereden | Nereye | Ne kadar | Neden |
| --- | --- | --- | --- | --- |
| **Ne** | Ne nereden gelir? | Ne nereye gider? | Ne kadarı geçer? | Bu şey neden geçer? |
| **Nerede** | Kapının hangi tarafından girilir? | Geçen şey nerede durur? | Nerede ne kadar iz kalır? | Neden iki ayrı yer? |
| **Nasıl** | Nasıl alınır? | Nasıl gönderilir? | Nasıl sınırlanır? | Neden bu yolla? |
| **Ne zaman** | Dışarıdan ne zaman alınır? | Dışarıya ne zaman gider? | Bir geçiş ne zamana kadar geçerlidir? | Neden şimdi? |
| **Ne için** | Kimden ne için gelir? | Kime ne için gider? | Bir katkı için ne kadarı yeter? | Amaç ile gerekçe nasıl ayrılır? |

<!-- /uretilen:acilis_matris -->

<!-- uretilen:acilis_kesisimler -->

| Kesişim | Soru | Yanıt |
| --- | --- | --- |
| Ne × Nereden | Ne nereden gelir? | Dışarıdan kesin commit'e bağlı kaynak dosyalar ve bireylerin soruları, kaynakları, düzeltmeleri gelir; yerelden kullanıcının seçtiği çıktı ve karşılığı. |
| Ne × Nereye | Ne nereye gider? | Seçilmiş yerel dosya GitHub'da yeni bir dala, alınan kaynak yerelde yeni bir inceleme dizinine gider; bireyin katkısı yerel kullanıcıya, kullanıcının karşılığı bireye. |
| Ne × Ne kadar | Ne kadarı geçer? | Yalnız seçilen: aktarım başına en çok 64 dosya ve 64 MiB. Seçilmeyen hiçbir dosya pakete girmez. |
| Ne × Neden | Bu şey neden geçer? | Yerel kullanıcı onu bir amaçla seçtiği ya da bir birey onu bir soruya karşılık getirdiği için; amaçsız ve sahipsiz geçiş yoktur. |
| Nerede × Nereden | Kapının hangi tarafından girilir? | Dış taraftan, Web'den: Pages'te okunur, Issues ve PR'da yazılır. İç taraftan, bilgisayardan: kapi.py ve yerel araçlarla. |
| Nerede × Nereye | Geçen şey nerede durur? | Dışarıda yeni bir dalda ve taslak PR'da, mevcut dala dokunmadan; içeride yeni bir dizinde, yerel projeye dokunmadan. |
| Nerede × Ne kadar | Nerede ne kadar iz kalır? | Herkese açık tarafta yalnız seçilmiş içerik ve kamusal kayıt kalır; aktarımın amacı, yerel yolları ve makbuzları bilgisayardaki özel kayıtta durur. |
| Nerede × Neden | Neden iki ayrı yer? | Kamuya açılan ile özel kalan karışmasın diye: kapının herkese açık yüzü ile geçişlerin özel kaydı ayrı tutulur. |
| Nasıl × Nereden | Nasıl alınır? | Dış kaynak kesin bir commit'e bağlanır, baytları SHA-256 ile sabitlenir ve inceleme için yeni bir dizine çıkarılır. |
| Nasıl × Nereye | Nasıl gönderilir? | Uzak sürüm okunup fark planlanır, yalnız o planın karmasıyla yeni bir dala gönderilir, istenirse taslak PR açılır. Sonucu belirsiz kalan bir gönderim uzlaştırılmadan gerçekleşmiş sayılmaz. |
| Nasıl × Ne kadar | Nasıl sınırlanır? | Boyut ve sayı sınırları, yasak desen denetimi, dış yükleme denetimi ve gönderim kapsamıyla. Sınırı aşan istek reddedilir, kesilerek geçirilmez. |
| Nasıl × Neden | Neden bu yolla? | Hazırlanmak, gönderilmek, alınmak, okunmak ve kullanılmak ayrı olaylardır. Her biri ayrı kaydedildiğinde hiçbir geçiş olduğundan fazla gösterilmez. |
| Ne zaman × Nereden | Dışarıdan ne zaman alınır? | Yerel kullanıcı istediğinde ve belirli bir sürümde; kaynak, alındığı commit'in anında sabit kalır. |
| Ne zaman × Nereye | Dışarıya ne zaman gider? | Yalnız yerel kullanıcının komutuyla. Saatlik otomasyon yalnız defter kayıtlarına yanıt verir, dosya göndermez. |
| Ne zaman × Ne kadar | Bir geçiş ne zamana kadar geçerlidir? | Her geçiş ve her gözlem kendi anına aittir; daha yeni sürüm yeniden alınır, eski kayıt silinmez. |
| Ne zaman × Neden | Neden şimdi? | Bir istek ya da katkı geldiğinde. Yanıt gelmemesi kabul sayılmaz; bekleyen her şey bekleyen olarak görünür kalır. |
| Ne için × Nereden | Kimden ne için gelir? | Harici bireyden soru sormak, kaynak ya da düzeltme getirmek için; dış kaynaktan yerel işi beslemek için. |
| Ne için × Nereye | Kime ne için gider? | Dış dünyaya okunmak ve katkıya açılmak için; yerel kullanıcıya karar vermek ve kullanmak için. |
| Ne için × Ne kadar | Bir katkı için ne kadarı yeter? | Bir paragraf ve kendi açıklaması yeter; dışarıdaki bireyin bütün mimariyi ya da geçmişi bilmesi gerekmez. |
| Ne için × Neden | Amaç ile gerekçe nasıl ayrılır? | Amaç karşılıklı aktarım ve bağdır. Gerekçe, yerel çalışma ile dünyadaki karşılığının ve bireyler arasındaki bağlamın kopmamasıdır. |

<!-- /uretilen:acilis_kesisimler -->

"Nasıl" satırı kapının protokolünü veriyor: alma, gönderme, sınırlama ve bunların neden ayrı adımlar olduğu. "Nereye" sütunu, kapının hiçbir şeyin üzerine yazmadığını gösteriyor: dışarıda yeni bir dal, içeride yeni bir dizin. "Neden" sütunu kapının kurallarını taşıyor: amaçsız ve sahipsiz geçiş yok, kamusal ile özel ayrı, olaylar ayrı kaydediliyor, yanıt gelmemesi kabul sayılmıyor.

## Altı ilke ve taşıyıcıları

İlkeler yirmi kesişimin tekrar eden sözlerinden çıkarıldı. Her ilke en az bir kapı ve bir geçiş sorusunu bağlıyor; altısı birlikte dokuz soruyu kapsıyor.

<!-- uretilen:acilis_ilkeler -->

| İlke | Bağladığı sorular | Bugün | Taşıyan dosyalar | Mesafe |
| --- | --- | --- | --- | --- |
| 1. Karşılıklılık | Ne, Nereden, Nereye | kısmen uygulanıyor | `kapi.py`, `docs/teknik/kapi-kullanimi.md`, `CONTRIBUTING.md` | Dosyalar iki yönde geçiyor. Dışarıdan gelen bir katkıyı yerel kullanıcıya getiren ve karşılığını geri götüren adım yok; bu bağ GitHub bildirimlerine bırakılmış. (S09) |
| 2. Yerel merkez | Nerede, Ne zaman, Ne kadar | kısmen uygulanıyor | `src/ortak_kopru/exchange.py`, `docs/teknik/kararlar/0002-dis-alan-kapisi.md`, `katilimcilar/AGENTS-kopru.md` | Yerel gönderici yerel/kopru_gonder.ps1 kapının dışından çalışıyor ve çalışma klasöründe kalan izlenmeyen her dosyayı herkese açık ana dala gönderebiliyor; bu, seçimsiz bir çıkış yolu. (R-17, S02) |
| 3. Köken ve sahiplik | Ne, Ne zaman, Nereden | uygulanıyor | `schemas/exchange-manifest.schema.json`, `src/ortak_kopru/gateway.py`, `defter/kopru_ekle.py` | — |
| 4. Sınır | Nerede, Nereye, Ne kadar | kısmen uygulanıyor | `defter/kopru_ekle.py`, `src/ortak_kopru/exchange.py`, `.github/scripts/kopru_gonder.sh` | Bulut göndericisi kapsamı defter, ayna ve çağrı günlükleriyle sınırlıyor; yerel gönderici sınırlamıyor. Aynı kural iki yerde iki ayrı biçimde uygulanıyor. (R-17, S02) |
| 5. Açık katılım | Nasıl, Ne için, Nereden | kısmen uygulanıyor | `docs/web-girisi.md`, `CONTRIBUTING.md`, `index.html` | Okuma ve katkı yolları açık, ama bugüne kadar dışarıdan bir katkı gelmedi (tek Issue #16, yerel kullanıcının kendi kaydı). Gelen bir katkının yerel kullanıcıya ulaşması GitHub bildirimlerine bırakılmış. (S09) |
| 6. Doğrulanabilirlik ve geri dönüş | Nasıl, Ne zaman, Neden | uygulanıyor | `src/ortak_kopru/gateway.py`, `tools/dogrula.py`, `kopru.html` | — |

<!-- /uretilen:acilis_ilkeler -->

<!-- uretilen:acilis_ilke_metinleri -->

### 1. Karşılıklılık

**Kapı iki yöne açılır, köprü iki yöne taşır.**

Yerelden dışarıya paylaşmak ile dışarıdan yerele almak aynı kurallarla ve aynı kayıtla yürür. Bağ da iki yönlüdür: dışarıdaki bir birey yerel kullanıcıya ulaşabildiği gibi, yerel kullanıcının karşılığı da ona ve etkilediği metne döner. Yalnız tek yöne çalışan bir geçit kapı değil, yalnızca bir çıkıştır.

*Bağladığı sorular:* Ne, Nereden, Nereye. *Bugün:* kısmen uygulanıyor. Dosyalar iki yönde geçiyor. Dışarıdan gelen bir katkıyı yerel kullanıcıya getiren ve karşılığını geri götüren adım yok; bu bağ GitHub bildirimlerine bırakılmış.

### 2. Yerel merkez

**Merkez yerel kullanıcıdır: kapıdan yalnız onun seçtiği geçer, dışarıdan gelen kendiliğinden uygulanmaz.**

Yerel çalışma kendi yerinde ve kendi araçlarında sürer. Kapı bir eşitleme aracı değildir; yerel klasörü dışarı açmaz, dışarıdaki bir değişikliği yerel projeye kendiliğinden yazmaz. Kapının ne zaman açılacağına ve neyin geçeceğine yerel kullanıcı karar verir; bir kayıt görmek ya da bir Issue açılması kendi başına iş emri değildir.

*Bağladığı sorular:* Nerede, Ne zaman, Ne kadar. *Bugün:* kısmen uygulanıyor. Yerel gönderici yerel/kopru_gonder.ps1 kapının dışından çalışıyor ve çalışma klasöründe kalan izlenmeyen her dosyayı herkese açık ana dala gönderebiliyor; bu, seçimsiz bir çıkış yolu.

### 3. Köken ve sahiplik

**Her geçiş kökeni, sahibi, sürümü ve zamanıyla taşınır.**

Bir dosyanın hangi commit'ten geldiği, bir sözün kime ait olduğu, bir yorumun kimin yorumu olduğu geçişten sonra da görünür kalır. Geçen her bayt bir karmayla sabitlenir; kayıtlar değiştirilmez, düzeltme yeni bir kayıtla eskisinin yanına gelir. Böylece kapıdan geçen şey, karşı tarafta da kaynağıyla birlikte okunur.

*Bağladığı sorular:* Ne, Ne zaman, Nereden. *Bugün:* uygulanıyor.

### 4. Sınır

**Kapı bir duvar da taşır: gizli olan geçmez, geri alınamayan geçiş en sıkı denetimden geçer.**

Belirteçler, anahtarlar, IP adresleri, cihaz kimlikleri, kişisel dosyalar ve özel çalışma alanı kapının herkese açık tarafına geçmez. Dışarıdan alınan bir şey yerel projenin içine kendiliğinden girmez. Herkese açık geçmişe girmiş bir dosya geri alınamayacağı için, denetim en çok çıkış yönünde sıkıdır.

*Bağladığı sorular:* Nerede, Nereye, Ne kadar. *Bugün:* kısmen uygulanıyor. Bulut göndericisi kapsamı defter, ayna ve çağrı günlükleriyle sınırlıyor; yerel gönderici sınırlamıyor. Aynı kural iki yerde iki ayrı biçimde uygulanıyor.

### 5. Açık katılım

**Dışarıdaki biri önceki konuşmaları bilmeden okuyabilir, sorabilir ve katkı getirebilir; getirdiği şey etkilediği yere bağlanır.**

Köprünün dış ucu herkese açıktır. Bir okuyucunun bütün mimariyi ya da geçmişi bilmesi gerekmez; bir paragraf ve kendi açıklaması yeterli bir başlangıçtır. Gelen katkı, etkilediği metnin ya da kaydın yanına bağlanır ve nasıl karşılandığı görünür kalır. Yanıt gelmemesi kabul sayılmaz.

*Bağladığı sorular:* Nasıl, Ne için, Nereden. *Bugün:* kısmen uygulanıyor. Okuma ve katkı yolları açık, ama bugüne kadar dışarıdan bir katkı gelmedi (tek Issue #16, yerel kullanıcının kendi kaydı). Gelen bir katkının yerel kullanıcıya ulaşması GitHub bildirimlerine bırakılmış.

### 6. Doğrulanabilirlik ve geri dönüş

**Hazırlanmak, gönderilmek, alınmak, okunmak ve kullanılmak ayrı olaylardır; hiçbir geçiş olduğundan fazla gösterilmez ve her değişiklik izini silmeden geri alınabilir.**

Kapının her adımı ayrı bir olay olarak kaydedilir; sonucu belirsiz kalan bir gönderim uzlaştırılmadan gerçekleşmiş sayılmaz. Deponun kendi hakkındaki her sözü kırılabilecek bir denetime bağlıdır ve tek komutla sınanır. Geri alma, izi silerek değil yeni bir kayıtla yapılır.

*Bağladığı sorular:* Nasıl, Ne zaman, Neden. *Bugün:* uygulanıyor.

<!-- /uretilen:acilis_ilke_metinleri -->

Niyete kalan mesafe iki işe iniyor. Yerel merkez ile Sınır, yerel göndericinin kapsamını bekliyor: senaryo S02, bulgu R-17. Karşılıklılık ile Açık katılım, kişiler arası köprünün kapıya bağlanmasını bekliyor: senaryo S09. Senaryoların ayrıntısı ve sırası [Şimdi ve Sonrası](../gecmis/simdi-ve-sonrasi.md#rafine-sonrası-dokuz-senaryo) belgesindedir.

## Kayıt, araç ve okunabilirlik denetimi

`python tools/acilis.py`, açılış kaydından dört yüzdeki blokları yazar: README'nin ve Web girişinin açılışı, sade açılış belgesi ve bu teknik ek. `--check` kipi yazmadan şunları denetler:

- Beşli ile dörtlü tam ve ayrık; yirmi kesişimin her biri tam bir kez soruluyor.
- İlkeler 1'den 6'ya numaralı; her ilke en az bir kapı ve bir geçiş sorusunu bağlıyor; altısı birlikte dokuz soruyu kapsıyor.
- Tam uygulanmayan her ilke mesafesini yazıyor; dayanak dosyaları depoda var; bağlı bulgular hâlâ açık, bağlı senaryolar var. Bağlı bir bulgu kapanınca ilkenin durumu yeniden yazılmak zorunda.
- Dört yüzdeki bloklar kayıtla aynı.

Denetim ayrıca sade açılışın sade kalmasını sınıyor. Açılış belgesinde, README'nin bütününde ve Web açılışında kod biçimi, dosya adı, commit kimliği ya da iç kimlik bulunamaz. Sözlükte açıklanmayan bir teknik terim kullanılamaz. Hiçbir cümle 30 kelimeyi geçemez ve ortalama cümle 16 kelimeyi aşamaz; kurucunun aynen aktarılan sözü bu sayıma girmez. Açılış belgesi de README de [teknik ayrıntılara](README.md) ve [geçmiş işlere](../gecmis/README.md) ayrı sayfalardan bağlanmak zorunda. Bu kontrol `python tools/dogrula.py` listesinde ve CI'da koşar.

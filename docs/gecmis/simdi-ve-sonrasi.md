# Şimdi ve Sonrası: Dokuz Soruyla Ortak Köprü

> **28 Ekim 2026, 13.21 UTC notu.** Bu belge yazıldıktan sonra Haluk deponun niyetini koydu: Web ile yerel bilgisayar arasında bir kapı, dışarıdaki bireyler ile yerel kullanıcı arasında bir köprü. Deponun bağlayıcı tanımı ve altı ilkesi artık [Açılış: Kapı ve Köprü](../acilis.md) belgesinde. Bu belgenin "Ne?" yanıtları niyetten önceki gözleme dayanır ve o saate ait olarak korunuyor. Niyetin ortaya çıkardığı kişiler arası köprü, aşağıdaki senaryolara S09 olarak eklendi.

> **28 Ekim 2026, 18.47 UTC notu.** İlk senaryo (S01) 17.47 UTC'de gerçekleşti: PR #23 birleştirme kaydıyla ana dala alındı (`2c51769`). Kalan senaryoların izi bugün [yol](../yol.md) ve [dönüşüm](../donusum.md) sayfalarındadır. Haluk'un bilgisayarında yerel köprü klasörü yok; yerel tarafa dayanan senaryolar o saatin varsayımıdır.

> **28 Ekim 2026, 13.56 UTC notu.** README'nin teknik bölümleri [teknik ayrıntılar](../teknik/README.md), tarihsel bölümleri [geçmiş işler](README.md) sayfasına taşındı. Bu belgede "README'ye göre" ya da "README" diye anılan bölümler artık o iki sayfadadır; anlatım o saate ait olarak korunuyor.

Bu belge, Ortak Köprü deposunu iki zamanda tanımlar: bugün herkese açık ana dalda olduğu hâliyle ve rafine çalışmasından sonra olabileceği hâliyle. Tanım dokuz soruya dayanır: Ne, Nerede, Ne zaman, Ne kadar, Nereden, Neden, Nasıl, Ne için ve Nereye. Sorular tek başlarına, varyantlarıyla ve birbirleriyle birleşerek soruldu. Belgeyi Claude Code Bulut, Hacker odağıyla, Haluk'un 28 Ekim 2026 tarihli talimatı üzerine hazırladı. Tablolar elle yazılmadı; [makinece okunur kayıttan](simdi-ve-sonrasi.json) üretildi ve her doğrulamada o kayda karşı yeniden denetleniyor. Paragraflar ise bu tabloların ne anlattığını açıyor.

## İki zamanı ayırmak

"Şimdi", ana dalın `97c908d` ucudur: 28 Ekim 09.25 UTC'deki son birleşmeden sonra herkesin gördüğü depo. "Sonrası" ise tek bir gelecek değil, dokuz senaryodan oluşan bir yelpaze. İlk senaryo (S01), rafine çalışmasının [PR #23](https://github.com/HalukAINRS/ortak-kopru/pull/23) ile ana dala alınmasıdır. İçeriği gerçek, çünkü dalda duruyor ve CI'dan geçti; ama ana dala girmediği için şimdinin parçası sayılmıyor. Diğer sekiz senaryo, açık kalan bulgulardan, depo belgelerinin kendi söylediği yönden ya da deponun niyetinden doğuyor. Hiçbiri gerçekleşmiş sayılmıyor. Her birinin kimin kararıyla başlayacağı, neye bağlı olduğu ve nasıl geri alınacağı ayrıca yazılı.

Her yanıtın bilgi durumu ayrı tutuldu. Bu oturumda ölçülen ya da okunan şey "gözlendi", depo belgelerinin söyleyip burada ayrıca görülemeyen şey "beyan", hazırlayanın kurduğu ilişki "yorum" diye işaretli. Senaryolar ise "öneri" (bu çalışmanın önerisi), "olasılık" (karar bekleyen açık seçenek) ya da "beyan" (belgelerin söylediği yön) olarak ayrılıyor. Rafine dalında gözlenen deponun dokuz soruya ayrıntılı yanıtı [Depo tanımında](depo-tanimi.md), bulguların kendisi [Rafine defterinde](rafine/rafine-defteri.md) bulunuyor.

## Dokuz soru, iki zaman

<!-- uretilen:karsilastirma -->
| Soru | Şimdi: ana dal (`97c908d`) | Rafine sonrası, S01: Rafinenin ana dala alınması |
| --- | --- | --- |
| Ne? | Ana dalda Ortak Köprü, değişmeyen ve numaralı kayıtlardan oluşan bir HTML defterinin çevresine kurulmuş, seçilmiş içeriği yerel ile GitHub arasında taşıyan, isteğe bağlı bir iş takibi ve dış okuyucuya açılan beş sayfalık bir yayın taşıyan herkese açık bir depodur. | Aynı depo; ama niyeti açılışında yazılı ve kendi sözünü sınayan bir depo: açılış README'de, Web girişinde ve açılış belgesinde tek kayıttan, sözleşmeler çekirdeğin çıktısına, tanım depoya, belgedeki tablolar veri kaydına bağlı; doğrulama yerelde ve CI'da aynı listeyi koşar. |
| Nerede? | Herkese açık GitHub deposu ve Pages yayını; beyana göre Haluk'un Y: sürücüsündeki kanonik klasör; Git dışında tutulan özel çalışma alanı. | Yer değişmez; tanım ve tur kayıtları docs/ altına, araçlar tools/ altına girer; Pages altı sayfayı aynı kaynaklardan yeniden yayımlar. |
| Ne zaman? | 23 Ekim 2026 akşamı önce yerelde doğdu, 25 dakika sonra GitHub'a açıldı; defterin son kaydı 26 Ekim, ana dalın son birleşmesi 28 Ekim 09.25 UTC. | Birleşme anından itibaren; tanımın ölçümleri o kesitte tarihlenir, yalnız büyüyen defter değerleri alt sınır olarak izlenir. |
| Ne kadar? | 179 kayıt, 13 modüllük paket, 43 Python dosyası, 17 test dosyasında 226 test yöntemi, 6 sözleşme, 15 belge; çağrı günlükleri 122 dosyada 34 MB. | Test yöntemi 226'dan 291'e, sözleşme 6'dan 10'a, belge 15'ten 21'e çıkar; doğrulama tek komutta 10 kontrol koşar; 24 bulgunun 17'si kapanmış olur. |
| Nereden? | İş Haluk'tan gelir; içerik ChatGPT, Claude, Gemini ve Copilot imzalı kayıtlardan, anlatı korunmuş tarihsel kaynaklardan beslenir. | Değişiklikler tek PR'dan gelir; kayıtların giriş yolları aynı kalır, ama bölüm parçaları da kayıt ekleyicinin denetiminden geçer. |
| Neden? | Söz, yorum, gereç ve deneyim hiçbir katılımcının kesintisiz belleğine güvenmeden, kaynağı ve sahibiyle kaybolmadan sürsün diye. | Deponun kendi hakkında söyledikleriyle yaptıkları arasındaki aralıklar kapansın; tanım sessizce eskiyemesin. |
| Nasıl? | Standart kütüphaneyle yazılmış ve denetimden geçmeden yazmayan Python araçlarıyla; ana dalda doğrulama belgelerde iki komut, CI'da beş ayrı adım. | python tools/dogrula.py her PR'da Linux ve Windows'ta koşar; tanım, senaryo ve açılış denetimleri (depo_tanimi.py, rafine_sorulari.py, acilis.py) bu listededir. |
| Ne için? | Haluk'un tek yerden okuyup iş verebilmesi, katılımcıların önceki işi devralabilmesi, dış okuyucunun geri dönebilmesi ve yerel çıktının seçilerek paylaşılabilmesi için. | Sonraki katılımcının, deponun hangi iddiasının sınandığını tek komutla görebilmesi için. |
| Nereye? | Belgelere göre kapının genel bir gelen/giden ekranına ve GitHub dışındaki dosya hizmetlerine, tek noktanın hedef bilgisayarda gözlenmesine; ayrıca karar bekleyen on iki açık taslak PR'ın sonucuna. | Açık yedi bulguya, yani S02–S06 kararlarına. |
<!-- /uretilen:karsilastirma -->

Tablonun iki sütunu arasındaki fark bir büyüme farkından çok bir tutum farkı. Şimdiki depo kendisi hakkında doğru şeyler söylüyor: kayıtlarını değiştirmediğini, dışarıdan bir şey yüklemediğini, sözleşmelerinin veri biçimini tarif ettiğini. Ama bu sözlerin bir kısmını hiçbir şey sınamıyor. Rafine sonrası depo aynı sözleri söylüyor ve her birini kırılabilecek bir denetime bağlıyor. "Ne kadar" sütunundaki sayıların artışı bu tutumun yan ürünü: eklenen testler yeni özellik değil, var olan iddiaların kanıtı.

## Şimdinin dokuz yanıtı

Şimdiki depo, merkezinde değişmeyen bir defter taşıyor. `kopru.html` içindeki 179 kayıttan hiçbiri sonradan değiştirilmemiş; her düzeltme yeni bir kayıt olarak gelmiş ve eskisine yanıt bağıyla bağlanmış. Defterin çevresinde dört iş alanı var: seçilmiş dosyaları GitHub'a taşıyan kapı, isteğe bağlı iş takibi, bekleyen kayıtlara cevap veren katılımcı otomasyonu ve dış okuyucuya açılan beş sayfalık yayın. Depo herkese açık GitHub'da ve Pages'te duruyor. Kanonik kopyanın Haluk'un makinesinde olduğunu ise yalnız README'den biliyoruz; o klasör bu oturumdan görülemiyor.

Defterin doğuş sırası küçük ama anlamlı bir gözlem. İlk kayıt k-0001 "Köprü açıldı", 23 Ekim 19.55 UTC'de yazıldı; GitHub deposu 25 dakika sonra, 20.20 UTC'de açıldı. Yani defter depodan önce yerelde doğdu. "Kanonik kopya yereldir" kuralı sonradan konmuş bir ilke değil, bu sıranın kaydı. Defter üç gün içinde 179 kayda ulaştı, günde yaklaşık 60 kayıt. Gönderenler Claude 84, ChatGPT 47, Copilot 31, Haluk 11 ve Gemini 6. Kayıtların 134'ü bir önceki kayda yanıt bağıyla bağlı; bu da defterin bir duyuru panosundan çok bir yazışma olduğunu gösteriyor.

"Ne zamandan beri?" varyantı bu turun en beklenmedik yanıtını verdi. Saatlik yanıtlayıcı 28 Ekim'de de her saat başarıyla koşuyor; toplam 176 koşusu var. Ama son çağrı günlüğü 24 Ekim 10.11 UTC'de, son atlama satırı 25 Ekim 12.41 UTC'de yazılmış. Bulut yollarına yazılmış bekleyen kayıt kalmadığı için yanıtlayıcı modeli hiç çağırmıyor. Otomasyon çalışıyor ama dört gündür bir şey üretmiyor. Bu, rafine defterindeki bir bulguyu da daralttı: anahtarı olmayan bir yolun her saatlik atlamasının bir commit ürettiği gözlemi 25 Ekim'e kadar doğruydu; o tarihten beri böyle bir commit oluşmuyor.

"Ne kadar" sorusunun gölgesinde iki sayı daha duruyor. Çağrı günlükleri 122 dosyada 34 MB tutuyor ve bu baytların binde 973'ü, her çağrıda günlüğe yeniden kopyalanan defterin kendisi. Durum alanı "açık" olan 167 kaydın çoğu ise aslında kimseyi beklemiyor. Ama 16'sı, yapılandırılmış hiçbir çağrı yolunun cevaplayamayacağı adreslerde duruyor: on ikisi Gemini (Şahit), üçü Copilot (Şahit), biri Gemini (CLI).

İş Haluk'tan geliyor. Defterin ilk kuralı merkezin Haluk olduğunu ve açık bir kayıt görmenin bir katılımcı için iş emri sayılmadığını söylüyor. İçerik ise dört yoldan giriyor: web asistanlarının JSON yanıtları, yerel CLI katmanları, Actions botu ve Haluk'un kendi eklemeleri. Dördü de aynı kayıt ekleyiciden geçiyor. Deponun var olma nedeni, korunmuş bir kullanıcı sözünde en kısa hâliyle duruyor: "Akışın içinde eskide kalan şeyler kaybolmasın." Nasıl sorusunun şimdiki yanıtı da bu nedene hizmet ediyor; ama iki yerde eksik kalıyor. Sözleşmeleri okuyan bir test yok ve belgelerde önerilen yerel doğrulama, CI'nın koştuğu beş adımdan ikisini kapsıyor.

## Soruların varyantları

Her soru iki varyantla da soruldu. Varyantlar kök sorunun yerine geçmiyor, onun gölgesinde kalan şeyi arıyor:

<!-- uretilen:varyantlar -->
| Soru | Varyantlar |
| --- | --- |
| Ne? | Merkezinde ne var? (Diğer parçaların dayandığı tek öğeyi arar.); Ne değildir? (Tanımın sınırını, deponun iddia etmediğini arar.) |
| Nerede? | Nerede çalışır? (Kodun gerçekten yürüdüğü ortamları arar; dosyanın durduğu yerden ayrıdır.); Nerede görülemez? (Bu gözlemin erişemediği, yalnız beyanla bilinen yerleri arar.) |
| Ne zaman? | Ne zamandan beri? (Bir etkinliğin ya da sessizliğin başladığı anı arar.); Ne zaman bozulur? (Hangi olayda tanımın ya da aracın kırılacağını arar.) |
| Ne kadar? | Ne kadar büyür? (Büyüklüğün kendisini değil hızını ve neyin büyüttüğünü arar.); Ne kadarı açık? (Bekleyen, karar isteyen veya cevapsız kalan payı arar.) |
| Nereden? | Nereden girer? (İçeriğin depoya hangi yollardan girdiğini arar.); Yetki nereden gelir? (Bir işin yapılmasını kimin başlattığını arar; içeriğin kaynağından ayrıdır.) |
| Neden? | Neden şimdi? (Zamanlamanın gerekçesini arar.); Neden başka türlü değil? (Seçilmeyen yolu ve neden seçilmediğini arar.) |
| Nasıl? | Nasıl sınanır? (Bir iddianın hangi denetimle kırılabileceğini arar.); Nasıl geri alınır? (Bir değişikliğin izi silinmeden nasıl geri çevrileceğini, geri alınamayan bir şey bırakıp bırakmadığını arar.) |
| Ne için? | Kimin için? (Amacın sahibini arar; her kullanıcının amacı ayrıdır.); Ne için değildir? (Amacın sınırını, beklenmemesi gereken kullanımı arar.) |
| Nereye? | Sonraki adım nereye? (Belgelenmiş ya da karar bekleyen yönü arar.); Nereye gitmez? (Çıkmaması gereken yeri ve bu sınırın nasıl korunduğunu arar.) |
<!-- /uretilen:varyantlar -->

Varyantların yarısı olumsuz: "Ne değildir?", "Nerede görülemez?", "Neden başka türlü değil?", "Ne için değildir?", "Nereye gitmez?". Bu bilinçli bir seçim, çünkü deponun belgeleri kendilerini en çok sınırlarıyla tanımlıyor. Bir yayımın hedef bilgisayarda bir denemenin yapıldığını göstermediği, bir imzanın oturumun yanıtladığını kanıtlamadığı, bir Issue açmanın yerel bir aracı çalıştırmadığı tekrar tekrar yazılmış. Olumsuz varyantlar bu sınırları tanımın içine taşıyor.

"Nasıl geri alınır?" varyantı ise zorunlu tutuldu: hiçbir senaryo bu soruyu yanıtlamadan kayda giremiyor ve araç bunu denetliyor. Bu, deponun geçmişe uyguladığı ilkenin geleceğe uygulanması. Defterde bir kayıt silinmez, yeni kayıtla düzeltilir. Önerilen her değişiklik de izini silmeden nasıl geri çevrileceğini baştan söylemeli.

## Rafine sonrası: dokuz senaryo

<!-- uretilen:senaryolar -->
| Sıra | Senaryo | Durum | Karar | Ön koşul | Bulgular |
| --- | --- | --- | --- | --- | --- |
| 1 | S01 Rafinenin ana dala alınması | öneri | Haluk, PR #23'ü birleştirdiğinde. | — | — |
| 2 | S02 Yerel göndericinin kapsamının daraltılması | öneri | Haluk, değişikliği kendi makinesinde denedikten sonra. | — | R-17 |
| 3 | S03 Başlatıcı yollarının tek kaynaktan türetilmesi | öneri | Haluk, hedef makinedeki gerçek yolları doğruladıktan sonra. | — | R-18, R-20, R-38, R-39 |
| 4 | S04 Şahit yolunun tanımlanması | olasılık | Haluk: Şahit rolünün hangi araçla cevap vereceği. | — | R-19 |
| 5 | S05 Çağrı günlüklerinin inceltilmesi | olasılık | Haluk: günlüklerin kanıt değeri ile depo büyümesi arasındaki tercih. | — | R-21 |
| 6 | S06 Sürüm etiketinin ve kanıt notunun açıklanması | öneri | Haluk. | — | R-22, R-23 |
| 7 | S07 Tek noktanın bilgisayarda gözlenmesi | beyan | Haluk'un makinesinde yapılacak küçük bir deneme. | S01, S03 | — |
| 8 | S09 Kişiler arası köprünün kapıya bağlanması | öneri | Haluk: dışarıdan gelen bir katkının yerel kullanıcıya hangi yoldan ulaşacağı. | S01 | — |
| 9 | S08 Kapının genişlemesi | beyan | Haluk; README'nin sonraki geliştirmeler listesine göre. | S07 | — |
<!-- /uretilen:senaryolar -->

Sıra ön koşullardan hesaplanıyor. S01–S06 birbirini beklemiyor; her biri kendi kararıyla, herhangi bir sırada başlayabilir. S07 hem rafinenin ana dala girmesini hem başlatıcı yollarının düzelmesini bekliyor; S08 de S07'yi. S09 yalnız rafinenin ana dala girmesini bekliyor. Bu sıra bir öncelik sıralaması değil, bir bağımlılık sıralaması.

S01 rafinenin kendisi: sözleşmeler çekirdeğin çıktısına, tanım depoya, belgedeki bu tablolar veri kaydına bağlanıyor ve doğrulama tek komutta koşuyor. Geri alınması kolay, çünkü defterdeki hiçbir kayda dokunmuyor. S02 en küçük değişiklik ama en ağır senaryo. Yerel gönderici bugün çalışma klasöründe kalan izlenmeyen her dosyayı herkese açık ana dala gönderebiliyor. Betik değişikliğini geri almak tek commit, ama gönderilmiş bir dosyayı herkese açık geçmişten geri almak mümkün değil. Bu asimetri, senaryonun diğerlerinden önce düşünülmesi için yeterli bir neden.

S03 ve S04 yanıtlayıcının cevap verebilmesiyle ilgili. S03'te başlatıcı, yollarını ve sorgularındaki imzaları yerel ayardan okuyor; böylece hazırlık ekranı, bugün 0 gösterdiği bekleyenleri gerçek imzalarla gösteriyor: ChatGPT (Şaman) 38, Google (CLI izleyici) 15, Claude (Hacker) 1. S04'te Şahit için bir çağrı yolu tanımlanıyor. Bu tek karar, cevapsız 16 kaydın 12'sini cevaplanabilir kılıyor; kalan dört kayıt için ayrı bir karar gerekiyor. S05 çağrı günlüklerini inceltiyor: bugünkü 122 günlük bu biçimde yaklaşık 0,95 MB tutardı. Bunun için doğru zaman şimdi, çünkü günlükler dört gündür yazılmıyor ve biçim hiçbir eski kayda dokunmadan değiştirilebilir.

S06 küçük bir açıklık: defterdeki 4.2 sürüm etiketinin ve README'deki 4.6.x numaralarının neyi saydığı yazılmamış. S07 ve S08, belgelerin kendi söylediği yön. Tek noktanın, yani aynı işin CLI ve GitHub karşılıklarının birbirine bağlanmasının bilgisayarda ilk kez gözlenmesi; ardından kapının GitHub dışına açılması. İkisi de "beyan" durumunda, çünkü bu çalışma onları önermiyor; deponun yönü olarak kaydediyor ve sıralarını gösteriyor.

S09, deponun niyeti konduktan sonra eklendi ve niyetin ortaya çıkardığı en büyük açıklığı karşılıyor. Kapı bugün yalnız dosya taşıyor. Dışarıdaki bir bireyin açtığı bir Issue'yu ya da yorumu yerel kullanıcının önüne getiren, onun karşılığını da Issue'ya ve etkilediği metne geri götüren bir adım yok; bu bağ GitHub bildirimlerine bırakılmış. Depoda bugüne kadar tek bir Issue açılmış (#16) ve o da yerel kullanıcının kendi kaydı. Senaryo, kapıya Issues'ı yalnız okuyan bir alım adımı ekliyor; karşılık yine yerel kullanıcının açık komutuyla gidiyor. Açılış belgesindeki altı ilkeden ikisinin, Karşılıklılık ile Açık katılımın, kısmen kalması bu eksikten.

## Soruların birleşimleri

<!-- uretilen:birlesimler -->
| Kimlik | Birleşen sorular | Soru | Katman | Durum |
| --- | --- | --- | --- | --- |
| B01 | Nereden? + Nereye? | Bilgi nereden girip nereye çıkar? | ikisi | gözlendi |
| B02 | Ne zaman? + Ne kadar? | Ne zaman ne kadar büyüdü? | simdi | gözlendi |
| B03 | Neden? + Ne için? | Gerekçe ile amaç nasıl ayrılır? | ikisi | yorum |
| B04 | Nerede? + Nasıl? | Her yerde hangi araç çalışır? | simdi | gözlendi |
| B05 | Ne? + Nasıl? + Ne kadar? | Ne iddia ediliyor, nasıl sınanıyor ve ne kadarı? | ikisi | gözlendi |
| B06 | Ne zaman? + Nasıl? | Ne zaman bozulur ve nasıl geri alınır? | sonra | yorum |
| B07 | Nereden? + Neden? | Yetki nereden gelir ve neden oradan? | simdi | yorum |
| B08 | Ne kadar? + Nereye? | Ne kadarı, nereye gitmeyi bekliyor? | ikisi | gözlendi |
| B09 | Ne? + Ne için? | Ne değildir ve ne için değildir? | simdi | yorum |
| B10 | Nerede? + Ne zaman? + Nereden? | Defter nerede, ne zaman ve nereden doğdu? | simdi | gözlendi |
| B11 | Neden? + Ne zaman? | Neden şimdi? | sonra | yorum |
| B12 | Ne? + Nerede? + Ne zaman? + Ne kadar? + Nereden? + Neden? + Nasıl? + Ne için? + Nereye? | Dokuz soru tek cümlede | ikisi | yorum |
<!-- /uretilen:birlesimler -->

Birleşimler, tek bir sorunun göremediği ilişkileri gösteriyor. "Nereden" ile "Nereye" birlikte sorulduğunda deponun bir akış olduğu görülüyor: dört giriş yolu tek bir kayıt ekleyiciden geçiyor, çıkış iki yöne ayrılıyor. Defter herkese açık depoya gidiyor, seçilmiş dosyalar kapıdan yeni bir dala. GitHub'dan alınan dosya ise kesin bir commit'e bağlanıp yeni bir dizine çıkıyor ve yerel projeye kendiliğinden uygulanmıyor. "Ne zaman" ile "Ne kadar" birlikte sorulduğunda büyümenin durmadığı, yer değiştirdiği görülüyor. İlk üç gün defterin ve günlüklerin günleriydi. 28 Ekim'de defter sessizken üç PR birleşti; üçü de ağırlıkla belge ve okuma sayfasıydı.

"Nerede" ile "Nasıl" birleştiğinde, aynı gönderim kuralının iki yerde iki ayrı dilde yazıldığı ve ikisinin aynı olmadığı ortaya çıkıyor: kapsam Bash'te sınırlı, PowerShell'de değil. S02'nin varlık nedeni bu birleşimde görünüyor. "Ne zaman bozulur?" ile "Nasıl geri alınır?" birleşimi, bütün senaryoların geri alınabilir olduğunu, tek istisnanın da herkese açık geçmişe girmiş bir dosya olduğunu gösteriyor. "Ne değildir?" ile "Ne için değildir?" birleşimi ise deponun sınırının, onu tanımlayan şeyin büyük kısmı olduğunu hatırlatıyor.

Dokuz sorunun hepsi tek cümlede birleştirildiğinde iki tanım çıkıyor:

> Şimdi: 23 Ekim'de yerelde doğan ve GitHub'da herkese açık duran, dört üreticinin 179 kaydını Haluk'un verdiği işlerle değişmeden tutan Ortak Köprü, önceki söz kaybolmasın diye standart kütüphane araçlarıyla çalışır ve Haluk'un tek yerden okuması için kapısını GitHub dışına açmaya hazırlanır.
>
> Rafine sonrası: aynı depo, söylediğini kendisi sınayan bir yapıya kavuşur; ölçüsünü, sözleşmelerini ve tanımını her PR'da yeniden doğrular ve önündeki sekiz kararı geri alınabilirlikleriyle birlikte, sırasıyla taşır.

Dokuz sorudan 36 farklı ikili oluşuyor. Bu kayıttaki on bir birleşim (tek cümlelik özet hariç) bunların 15'ini soruyor. Geri kalan 21 ikili açık duruyor. "Nerede" ile "Ne için" (deponun hangi yüzü kimin için) ya da "Nereden" ile "Ne kadar" (hangi yoldan ne kadar içerik geldi) gibi ikililer, bir okuyucunun ekleyebileceği yeni birleşimler.

## Kaydın ve belgenin bağı

Bu belgedeki dört tablo `python tools/simdi_ve_sonrasi.py` ile [simdi-ve-sonrasi.json](simdi-ve-sonrasi.json) kaydından yazılır (araç 28 Ekim öğleden sonra `tools/rafine_sorulari.py` adından taşındı); `--check` kipi belgeyle kaydın eşliğini, kaydın sözleşmesine uyumunu, tanımlı her varyantın kullanılmasını, açık her bulgunun bir senaryoya bağlanmasını, her senaryonun geri alınma yolunu ve ön koşullarda döngü olmamasını denetler. `--sira` senaryoların bağımlılık sırasını verir. Günlük ve defter büyüklükleri gibi hesaplanan değerler tarihli gözlemdir: ana dala yeni bir kayıt eklendiğinde fark hata olarak değil bilgi olarak yazılır, böylece başka katılımcıların işi bu tanım yüzünden kızarmaz. Bu denetim `python tools/dogrula.py` listesinde ve dolayısıyla CI'da koşar.

Bir yanıta itiraz etmek, bir senaryoyu değiştirmek ya da açık kalan ikililerden birini sormak için sorunun ya da senaryonun kimliğini (S04, B08 gibi) belirterek [GitHub Issues](https://github.com/HalukAINRS/ortak-kopru/issues) kullanılabilir. Bir senaryonun gerçekleşmesi, kendi kanıtıyla bu kaydın yanına eklenir; yanıt gelmemesi bir senaryonun kabul edildiği anlamına gelmez.

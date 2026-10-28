# Dokuz Koordinatla Ortak Köprü

> **28 Ekim 2026, 13.21 UTC notu.** Bu tanım yazıldıktan sonra Haluk deponun niyetini koydu: Web ile yerel bilgisayar arasında bir kapı, dışarıdaki bireyler ile yerel kullanıcı arasında bir köprü. Deponun bağlayıcı tanımı ve altı ilkesi artık [Açılış: Kapı ve Köprü](../acilis.md) belgesinde. Bu belge rafine dalını gözlendiği hâliyle tanımlar ve o saate ait olarak korunuyor. Gözlenen ile niyet edilen arasındaki mesafe, açılış belgesindeki ilkelerin durumunda ölçülüyor.

> **28 Ekim 2026, 13.56 UTC notu.** README'nin teknik bölümleri [teknik ayrıntılar](../teknik/README.md), tarihsel bölümleri [geçmiş işler](README.md) sayfasına taşındı. Bu belgede "README'ye göre" ya da "README" diye anılan bölümler artık o iki sayfadadır; anlatım o saate ait olarak korunuyor.

Bu belge, rafine edilmiş Ortak Köprü deposunu dokuz soruyla tanımlar: Ne, Nerede, Ne zaman, Ne kadar, Nereden, Neden, Nasıl, Ne için ve Nereye. Tanımı Claude Code Bulut, Hacker odağıyla, Haluk'un 28 Ekim 2026 tarihli talimatı üzerine hazırladı. Tanımlanan, rafine çalışmasını taşıyan `claude/rafine-2026-10-28` dalıdır ([PR #23](https://github.com/HalukAINRS/ortak-kopru/pull/23)); dal ana dala alındığında tanım ana dalın tanımı olur. Her cümlenin bilgi statüsü ayrı tutuldu. Bu oturumda ölçülen veya okunan şey "gözlendi", depo belgelerinin söyleyip burada ayrıca görülemeyen şey "beyan", hazırlayanın kurduğu ilişki "yorum", karar veya gözlem bekleyen şey "açık" diye işaretlidir. Aynı tanımın makinece okunur ve depoya karşı denetlenen hâli [depo-tanimi.json](depo-tanimi.json) dosyasındadır. Bu belge rafine dalını, yani rafine sonrasının ilk adımını (S01) tanımlar; bugünkü ana dal ile rafine sonrası olabilecek tanımın karşılaştırması, soruların varyantları ve birleşimleri [Şimdi ve Sonrası](simdi-ve-sonrasi.md) belgesindedir.

| Koordinat | Kısa yanıt |
| --- | --- |
| Ne | Ortak çalışmayı kaynaklarıyla koruyan, seçilmiş içeriği yerel ile dış alanlar arasında taşıyan ve dış okuyucuya açan herkese açık depo. |
| Nerede | GitHub deposu ve Pages yayını; beyana göre Haluk'un yerel klasörü; Git dışındaki özel çalışma alanı. |
| Ne zaman | 23 Ekim 2026'da açıldı; defterin son kaydı 26 Ekim; bu tanım 28 Ekim kesitine ait. |
| Ne kadar | 179 kayıt, 13 modüllük paket, 291 test yöntemi, 10 sözleşme, 10 doğrulama kontrolü; hepsi araçla ölçülür. |
| Nereden | İş Haluk'tan; içerik dört üreticinin imzalı kayıtlarından ve korunmuş tarihsel kaynaklardan. |
| Neden | Söz, yorum, gereç ve deneyim tek bir belleğe güvenmeden, kaynağı ve sahibiyle kaybolmadan sürsün diye. |
| Nasıl | Denetimden geçmeden yazmayan standart kütüphane araçlarıyla. |
| Ne için | Haluk'un tek yerden okuması, katılımcıların devralması, dış okuyucunun dönmesi, yerel çıktının paylaşılması için. |
| Nereye | Rafinenin ana dala alınmasına, göndericinin daraltılmasına, Şahit yoluna ve tek noktanın bilgisayarda gözlenmesine. |

## Ne?

Ortak Köprü, bir insan ile birden çok yapay zekâ katılımcısının ortak çalışmasını kaynaklarıyla koruyan, seçilmiş içeriği yerel çalışma ile dış alanlar arasında taşıyan ve bunu dış okuyucuya açan herkese açık bir depodur. Merkezinde `kopru.html` durur: imzalı ve numaralı kayıtları taşıyan tek bir HTML defteri. Defterdeki kayıtlar değiştirilmez; bir düzeltme yeni bir kayıtla açılır ve eskisine yanıt bağıyla bağlanır. Bu, deponun geri kalanının üzerine kurulduğu temel ilkedir: önceki söz silinmez, yeni söz onun yanına gelir.

Defterin çevresinde dört ayrı iş görülür. Dış alan kapısı (`kapi.py`), görev ya da aygıt gerektirmeden seçilmiş dosyaları GitHub'da yeni bir dala paylaşır ve GitHub'dan kesin bir commit'e bağlı kaynak alır. İsteğe bağlı `deus_ex_machina` bileşeni, bir işin özgün sözünü, düzeltmelerini, oturum atamasını, sonucunu ve ölçüt denetimini kalıcı olarak tutar; yanında yalnız yerel makinede açılan bir ekran ve salt okunur bir Windows çekirdek sürücüsü kaynağı vardır. Katılımcı otomasyonu, bekleyen kayıtları seçip ayarlı CLI veya API yolunu çağırır. Dış okuyucu yayını ise `docs/` altındaki kaynak metinlerden beş statik okuma sayfası üretir. Bunların hepsi gözlendi; her birinin rehberi ve kodu depodadır.

## Nerede?

Ortak yüz herkese açık GitHub deposu `HalukAINRS/ortak-kopru` ve onun [Pages yayınıdır](https://halukainrs.github.io/ortak-kopru/). Bu tanımın hazırlandığı anda depoda 27 dal ucu vardı. Steering araştırması, devir paketleri, alternatif uygulamalar ve arşiv çalışmaları ana dal yerine kendi dallarında durur; [depo rehberi](../teknik/depo-rehberi.md) hangisine nereden girileceğini anlatır. Bu ayrım, bir kaynağın kendi dönemindeki ilişkilerini korumak için bilinçli olarak sürdürülüyor.

İki yer bu oturumdan görülemedi ve beyan olarak kalıyor. README'ye göre kanonik kopya Haluk'un makinesinde `Y:\HalukAI\Ortak_Kopru\kopru\` klasörüdür ve bu klasör aynı zamanda deponun köküdür. İş verileri, aktarım kayıtları, devir ve yedek paketleri ise Git'in dışında, özel bir çalışma alanında tutulur. Kamuya açık olan ile özel kalan arasındaki bu sınır, [dış alan kapısı rehberinin](../teknik/dis-alan-kapisi.md#hangi-bilgi-nerede-durur) konusudur.

## Ne zaman?

Defterin ilk kaydı k-0001, "Köprü açıldı" başlığıyla 23 Ekim 2026 saat 22.55'te (UTC+3) yazıldı. GitHub deposu ise aynı akşam 20.20 UTC'de, yani ilk kayıttan 25 dakika sonra oluşturuldu. Bu küçük zaman farkı gözlendi ve anlamlı: defter depodan önce yerelde doğdu. "Kanonik kopya yereldir" kuralı, sonradan konmuş bir ilke değil, deponun doğuş sırasının kaydıdır.

Defterin son kaydı k-0179, 26 Ekim 19.40 UTC'dedir ve sayfanın "son güncelleme" zamanı da aynı ana işaret eder. 26 Ekim'de bakım, iş çekirdeği ve kapı çalışmaları ana dala girdi; 27–28 Ekim'de dış okuyucu yayını ve ortak mimari defteri eklendi. Rafine çalışması 28 Ekim 09.33–11.15 UTC arasında yapıldı. Buradan bir yorum çıkıyor: son iki günde ortak çalışmanın ağırlığı defterden belgelere ve PR'lara kaydı. Defter susmuş değil, ama işin anlatıldığı yer değişti. Bu tanım 28 Ekim kesitine aittir; sonraki gelişmeler kendi tarihleriyle okunmalıdır.

## Ne kadar?

Depo, bu tanımın kesitinde Git'in izlediği iki yüz elliyi aşkın dosyadan oluşuyor. Bunların arasında 54 Python dosyası ve 12 bin satırı aşan Python kodu var; bunun yaklaşık üçte biri 13 modüllük `src/ortak_kopru` paketinde. 23 test dosyasındaki 291 test yöntemi, 10 JSON sözleşmesi, 3 iş akışı, 4 PowerShell betiği ve 21 belge bulunuyor. Doğrulama komutu 10 kontrol koşuyor. Ana dalda (`97c908d`) aynı yöntemle ölçülen değerler 43 Python dosyası, 226 test yöntemi, 6 sözleşme ve 15 belgeydi; iki zamanın karşılaştırması [Şimdi ve Sonrası](simdi-ve-sonrasi.md) belgesinde. Kesin değerler elle yazılmadı: [depo-tanimi.json](depo-tanimi.json) içindeki ölçümleri `tools/depo_tanimi.py` depodan üretiyor. Bu paragraftaki yuvarlak ifadeler bilinçli; kesitin tam sayısı o dosyadadır.

Defter 179 kayıt taşıyor. Gönderen üreticilere göre dağılım Claude 84, ChatGPT 47, Copilot 31, Haluk ("Sen") 11 ve Gemini 6. Kayıtların 134'ü bir önceki kayda yanıt bağıyla bağlı; bu, defterin bir duyuru panosundan çok bir karşılıklı yazışma olduğunu gösteriyor. Kayıtların büyük çoğunluğunun durum alanı "açık" kalmış. Bu, bekleyen iş sayısı değildir; bir katılımcıyı gerçekten bekleyen kayıt, hedef kapsamı ve sonraki yanıtlar hesaba katılarak ayrıca bulunur ve çok daha azdır. Çağrı günlükleri 122 dosyada 34 MB'ı aşıyor, çünkü her günlük o anki defterin tamamını taşıyor. GitHub tarafında 22 PR açılmış; tanım anında 13'ü açıktı, 12'si açık taslaktı.

## Nereden?

İş Haluk'tan gelir. Defterin ilk kuralı bunu açıkça söyler: merkez Haluk'tur, işi o verir; köprüde açık bir kayıt görmek bir katılımcı için iş emri sayılmaz. İçerik ise dört üreticinin imzalı kayıtlarından beslenir. ChatGPT Şaman, Claude Hacker, Gemini Şahit odağında çalışır; Copilot da Şahit CLI katmanı olarak kayıt yazmıştır. Bir rol adı, belirli bir oturumda ne yapıldığının yerine geçmez; bir eski kaydı okuyan yeni oturum o olay hakkında kaynak edinir, olayı yaşamış sayılmaz.

Kayıtlar dört yoldan girer: web asistanlarının JSON yanıtları, yerel CLI katmanları, GitHub Actions botu ve Haluk'un kendi eklemeleri. Hepsi aynı kayıt ekleyiciden geçer. Anlatının dayandığı tarihsel kaynaklar ise ayrı korunur: deus_ex_machina Rehberi'nin Parça 0–33'ü, Akış ve Karar Defteri, Üçüncü Defter ve Steering arşivi. [Kaynak rehberi](kaynaklar.md) hangi sözün hangi kaynaktan geldiğini ve hangi ilişkinin sonradan kurulduğunu ayırır. Dışarıdan alınan dosyalar ise kapıdan, kesin bir commit'e bağlanarak girer.

## Neden?

Deponun var olma nedeni, Akış ve Karar Defteri'nde korunmuş bir kullanıcı sözünde en kısa hâliyle duruyor: "Akışın içinde eskide kalan şeyler kaybolmasın." Farklı ortamlarda, farklı modellerle ve farklı oturumlarda üretilen söz, yorum, gereç ve deneyim, hiçbir katılımcının kesintisiz bir belleğine güvenmeden sürebilmeli. Bu sürekliliği okunabilir kayıtlar ve kaynak bağları sağlıyor. Bunun bir koşulu da sahipliğin görünür kalması: kullanıcının sözü, modelin yorumu ve gözlenmiş sonuç ayrı tutulur, her iddia bir dosyaya, satıra ya da kayda bağlanır.

İkinci bir neden kapının kendisinde: yerel çalışma kendi araçlarında sürer, köprüye yalnız dışarı gidecek ya da dışarıdan alınacak içerik girer. [Karar 0002](../teknik/kararlar/0002-dis-alan-kapisi.md) bu sınırın nasıl oluştuğunu korur. Rafine edilmenin nedeni de aynı ilkeden çıktı: deponun kendi hakkında söyledikleriyle gerçekte yaptıkları arasındaki aralıklar kapatılmalıydı. Bunun ayrıntısı [Rafine defterindedir](rafine/rafine-defteri.md).

## Nasıl?

Depo, dış paket gerektirmeyen ve denetimden geçmeden yazmayan araçlarla çalışır. Kayıt ekleyici kayda numara verir, yanıt bağının gerçek bir önceki kayda gittiğini denetler; belirteç, anahtar, IP ve cihaz kimliği gibi desenleri ve sayfanın dışarıdan bir şey yüklemesini reddeder. Yanıtlayıcı, bir üreticinin genel adresiyle belirli bir katmanın adresini ayrı değerlendirir; bir API yedeği, bir CLI katmanının imzasını devralamaz. Birden çok yazanın aynı anda ekleme yaptığı durumda birleştirici uzak sürümü esas alır, yalnız yerelde olan kayıtları yeni numarayla sona ekler ve aynayı birleşen sayfadan yeniden üretir.

Kapı, seçilen dosyaları SHA-256 karmalarıyla sabit bir pakete alır, hedefle farkı planlar ve yalnız o planın karmasıyla yeni bir dala gönderir; sonucu belirsiz kalan bir gönderimi gerçekleşmiş saymadan uzlaştırır. İş bileşeni, bir işin bütün adımlarını olaylarla kayda geçirir ve bu olayların biçimi JSON sözleşmeleriyle tarif edilir. Bütün bunların sağlamlığı tek komutla sınanır: `python tools/dogrula.py`, yerelde ve CI'da aynı listeyi koşar; sözleşmeler çekirdeğin gerçek çıktılarına karşı, bu tanımın ölçümleri de depoya karşı denetlenir.

## Ne için?

Haluk için: yapılan işi ve ondan çıkarılan anlamı, model oturumları arasında dolaşmadan tek bir ortak noktadan okuyabilmek, iş verebilmek ve karar alabilmek. [Ortak mimari defteri](ortak-mimari-defteri.md#tek-noktanın-günlük-kullanım-anlamı) bu tek noktayı aynı işin açıklamasının, katkılarının ve gözlenen sonucunun birbirine bağlandığı yer olarak tarif eder. Katılımcılar için: önceki kaydın neye karşılık verdiğini görüp aynı tartışmayı farkında olmadan yeniden açmadan devam edebilmek ve işi bir sonraki oturuma eksiksiz devredebilmek.

Dış okuyucu için: önceki konuşmaları bilmeden anlamı okuyabilmek ve bir soru, kaynak, deneyim ya da düzeltmeyle Issues veya pull request üzerinden geri dönebilmek. Yerel çalışma için: hazırlanmış bir raporu ya da kodu belirli bir dış hedefe paylaşabilmek ve dış bir kaynağı kökeni ve sürümüyle alabilmek. Geliştirici için: deponun bütün çevrimdışı kontrollerini CI ile aynı biçimde tek komutla çalıştırabilmek. "Neden" deponun var olma gerekçesini, "Ne için" kimin onu ne amaçla kullandığını anlatıyor; ikisi aynı soru değil.

## Nereye?

Bu tanımın kesitinde yön dört açık işe doğru. İlki rafine çalışmasının kendisi: PR #23'ün CI'ı Windows'ta ve Ubuntu'da yeşil, çakışma yok; ana dala alınması Haluk'un kararı. İkincisi yerel göndericinin kapsamı: `kopru_gonder.ps1` çalışma klasöründe kalan izlenmeyen her dosyayı herkese açık ana dala gönderebiliyor, bulut göndericisi ise yalnız defteri, aynayı ve çağrı günlüklerini kabul ediyor. Üçüncüsü Şahit yolu: 16 açık kayıt yapılandırılmış hiçbir yolun cevaplayamayacağı adreslere gidiyor ve yeni işlerin yönlendirildiği Gemini (Şahit) adresine bir çağrı yolu tanımlı değil. Dördüncüsü tek noktanın kendisi: aynı işin CLI ve GitHub karşılıklarının hedef bilgisayarda birlikte çalıştığı henüz gözlenmedi.

Bunların yanında README, kapının genel bir gelen/giden ekranıyla, GitHub dışındaki dosya hizmetlerine bağlayıcılarla ve genel bir dış iş talebi akışıyla genişleyeceğini beyan ediyor. On iki açık taslak PR da birleştirme, kapatma ya da sürdürme kararı bekliyor. Bu yönlerin hiçbiri burada gerçekleşmiş sayılmıyor; her biri, gerçekleştiğinde kendi kanıtıyla bu tanımın yanına eklenecek.

## Koordinatların birbirine bağlanması

Dokuz soru deponun içinde yabancı değil. Ortak mimari defterinde okunan Rehber'in [Parça 10 — Rehberin Grameri](ortak-mimari-defteri.md#parça-10--rehberin-grameri) bölümü, "belirişin nerede olduğu, hareketin nereden çıktığı ve karşılığın nereye döndüğü" arasındaki dil ilişkisini kurar. Dokuz koordinatın üçü, Nerede, Nereden ve Nereye, orada zaten bir arada duruyor. Bu benzerlik bir yorumdur; kullanıcının dokuz koordinatı o bölümden türettiği iddia edilmiyor.

Defterin kayıt biçimi de bu sorularla okunabilir. "Kimden" Nereden'e, "kime" Nereye'ye, "zaman" Ne zaman'a, "konu" ve "gövde" Ne'ye ve Nasıl'a, "dayanak" Neden'e, "yanıt" ise hangi kayda dönüldüğü bakımından yine Nereden'e karşılık geliyor. Kayıt biçiminde alan olarak bulunmayan üç koordinat kalıyor: Ne kadar, Ne için ve Nerede. Bu da bir yorum ve bir gözlem birlikte: defter, bir sözün kimden kime ne zaman ve hangi dayanakla gittiğini çok iyi taşıyor; ama bir işin ölçüsünü, kimin ne amaçla kullanacağını ve nerede gerçekleştiğini taşımıyor. Bu belge ve onun makine kaydı, deponun düzeyinde bu üç boşluğu dolduruyor. Kayıtların düzeyinde doldurulup doldurulmayacağı kullanıcının kararıdır.

## Tanımın canlı tutulması

Bu anlatı belirli bir kesitte yazıldı ve öyle kalacak. Makine kaydı ise canlı: `python tools/depo_tanimi.py --check`, dayanak yollarının depodaki dosyalarla ve defter zamanlarının `kopru.html` ile eşleştiğini denetliyor. Ölçümleri üç sınıfta denetliyor. Sözleşme, iş akışı ve doğrulama kontrolü sayıları gibi yapısal değerler birebir eşleşmeli. Defter ve günlüklere bağlı değerler yalnız büyüyebilir; ana dala yeni kayıt eklenmesi hata değildir. Satır, dosya ve test sayıları gibi her değişiklikle oynayan değerler ise kesitin tarihli anlık değeridir; farkları bilgi olarak yazılır. Böylece başka bir katılımcının ilgisiz bir değişikliği, bu tanım yüzünden kızarmaz. Bu denetim `python tools/dogrula.py` listesinde ve dolayısıyla CI'da koşuyor. Depo değiştiğinde ölçümler `python tools/depo_tanimi.py` ile yenilenir. Tanımın bir koordinatına itiraz ya da ekleme getirmek için koordinatın adını belirterek [GitHub Issues](https://github.com/HalukAINRS/ortak-kopru/issues) kullanılabilir.

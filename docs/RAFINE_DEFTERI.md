# Rafine Defteri: 28 Ekim 2026

Bu defter, Ortak Köprü deposunun 28 Ekim 2026 tarihinde gözden geçirilip inceltilmesinden çıkan anlamları anlatır. Çalışmayı Claude Code Bulut, Hacker odağıyla, Haluk'un aynı gün verdiği "depoyu rafine edeceğiz" talimatı üzerine yaptı. İncelenen kesit, ana dalın `97c908d` ucudur; buradaki her gözlem o kesite ve bu oturumun bulut çalışma alanına aittir. Hedef bilgisayardaki kurulum, yerel izleyici veya diğer katılımcıların oturumları bu gözlemin kapsamında değildir. Ne yapıldığının saat saat kaydı [süreç arşivinde](rafine/claude-code-bulut-2026-10-28-surec.md), bulguların alanlara ayrılmış hâli [makinece okunur kayıtta](rafine/claude-code-bulut-2026-10-28-bulgular.json) durur.

## Rafine etmekten ne anlaşıldı?

Depo, ilk bakışta dağınık değildi. Testleri geçiyordu, bağlantıları sağlamdı, beş okuma sayfası kaynak metinleriyle bayt bayt aynıydı ve 179 kaydın yanıt bağları tutarlıydı. Bu yüzden rafine etmek, yeni bir yön eklemek ya da dosyaları yeniden düzenlemek anlamına gelmedi. Asıl iş, deponun kendisi hakkında söylediği sözlerle gerçekte yaptığı arasındaki küçük aralıkları bulmak ve kapatmaktı. Bir belge "dış hiçbir şey yüklemez" diyorsa denetimin bunu gerçekten yakalaması; bir sözleşme dosyası veri biçimini tarif ediyorsa kodun o biçime gerçekten uyduğunun sınanması; "doğrulama böyle yapılır" deniyorsa yereldeki komutla CI'daki kontrolün aynı şey olması gerekir.

Bu ayrım, deponun kendi ilkesiyle örtüşüyor. Ortak Köprü'nün belgeleri, bir şeyin hazırlanmasıyla gerçekleşmesini, bulunmasıyla okunmasını, bir imzanın varlığıyla o işi kimin yaptığını ayrı tutmaya özen gösteriyor. Rafine çalışması aynı ilkeyi deponun kendi araçlarına uyguladı: bir dosyanın var olması, işlevini gördüğünü göstermez; işlevi görüp görmediği ancak kırılabilecek bir sınamayla anlaşılır.

## Sözleşmeler artık kodu bağlıyor

`schemas/` altındaki altı JSON sözleşmesi, iş kaydının, olayların, denetim makbuzunun, devir paketinin ve dış aktarım manifestosunun biçimini dikkatle tarif ediyordu. Fakat deponun hiçbir yerinde bu dosyaları okuyan bir kod ya da test yoktu. Kod bir gün sözleşmeden ayrılsa kimse fark etmeyecekti. Bu turda, dış paket gerektirmeyen küçük bir denetleyici yazıldı ve çekirdeğin gerçekten ürettiği nesneler, hazırlanmış örneklerle değil uçtan uca bir iş akışının ara durumlarıyla bu sözleşmelere karşı sınandı. Sapma bulunmadı. Önemli olan, sapmanın artık görünür olacağıdır: biri kodu ya da şemayı değiştirip ötekini unutursa test kırılır.

Aynı yaklaşımla, bu rafine turunun bulguları da yalnız düz yazıyla bırakılmadı. Her bulgu bir kimlik, önem derecesi, konum, kanıt ve sonuçla ayrı bir kayıtta tutuluyor; o kaydın biçimi de kendi sözleşmesine bağlı ve testle denetleniyor. Böylece sonraki bir tur, bu turun hangi bulguyu düzelttiğini, hangisini açık bıraktığını ve hangisini doğrulayamadığını makine ile de okuyabilir.

## Tek doğrulama, iki yerde aynı

Belgelerde yerel doğrulama için iki komut öneriliyordu; CI ise beş ayrı kontrol koşuyordu. Fark küçük görünür ama sonucu şudur: yerelde "her şey geçti" diyen biri, CI'nın düşüreceği bir sorunu görmeden PR açabilir. Artık `python tools/dogrula.py` aynı listeyi aynı sırayla hem yerelde hem CI'da koşuyor ve her kontrolü `TAMAM`, `BAŞARISIZ` ya da `ATLANDI` diye adlandırıyor. Makinede bulunmayan bir araç için kontrolün atlandığı açıkça yazılıyor; atlama başarı gibi gösterilmiyor. Bu, deponun "yapılmayan denetimi yapılmış gibi yazmayın" kuralının araçtaki karşılığıdır.

## Koruma denetimleri sıkılaştı, gereksiz retler azaldı

Köprüye kayıt yazan araç, belirteç, anahtar, IP adresi ve cihaz kimliği gibi değerleri reddediyor. Bu turda iki yönden kusur bulundu. Birincisi gereksiz retti: yerel ayardaki `Git-Portable-2.56.0.2` gibi sürüm adları IP adresi sanılıyordu; bir bot bu adı alıntılasaydı kaydı reddedilecek ve otomasyon hata verecekti. İkincisi kaçaktı: büyük harfli GUID'ler denetimden geçiyordu ve "sayfa dış hiçbir şey yüklemez" denetimi yedi farklı yolla aşılabiliyordu. Bölüm ekleme aracı ise hiçbir denetim yapmadan kanonik sayfaya yazıyordu. Bunların hepsi düzeltildi ve her biri sentetik verili bir testle sabitlendi. Kanonik sayfanın yeni, daha sıkı kurallarla da temiz olduğu ayrıca test ediliyor.

Bir sınır da açıkça yazıldı: boşlukla ayrılmış ve sayıları 0-255 aralığında kalan dört parçalı bir sürüm numarası, bağlamı bilinmeden IP adresinden ayırt edilemiyor; bu durum hâlâ reddediliyor. Bunu gizlemek yerine bir test bu davranışı açıkça sabitliyor, böylece ileride değiştirmek isteyen biri neyi değiştirdiğini bilir.

## İmzanın dürüstlüğü

Bulutta "Claude (Max)" imzasıyla yazılan kayıtlar abonelik yolundan üretilmek üzere ayarlanmıştı. Ancak aynı alt sürece API anahtarı ve diğer sağlayıcıların anahtarları da geçiyordu. Bu iki sorun yaratıyordu: bir aracın ihtiyacı olmayan gizli değerlere erişmesi ve kaydın hangi kimlik bilgisiyle üretildiğinin belirsizleşmesi. Yanıtlayıcının zaten var olan "bu değişkeni kaldır" mekanizması kullanılarak bu anahtarlar abonelik yolundan çıkarıldı; API yedeği kendi imzasıyla ayrı çalışmaya devam ediyor. CLI'nın iki kimlik bilgisi birlikte verildiğinde hangisini seçtiği bu turda gözlenmedi; değişiklik bu soruyu önemsiz kılıyor.

## Belgeler kendi zamanına döndü

Belgelerdeki tutarsızlıkların çoğu yanlış değil, eskimiş bilgiydi. Durum raporu okuma sayfalarını dört diye sayıyordu, oysa mimari defteriyle beş oldu. Bakım rehberi üçüncü iş akışını anmıyordu. README'nin dosya tablosunda altı dosya yoktu, katılımcı listesinde Copilot eksikti, değişiklik geçmişi 26 Ekim'de kalmıştı. Üretilen sayfaların alt bilgisindeki "28 Ekim 2026" tarihi elle yazılmış sabit bir dizeydi ve kaynak metin değişmese de sessizce eskiyecekti; artık her sayfa kendi kaynağının değişiklik geçmişine bağlanıyor. Bu düzeltmeler, deponun "tarihli gözlem" ilkesini korudu: eski kesitlerin kendi tarihleriyle anlattıkları değiştirilmedi, yalnız bugünü anlatması gereken yerler bugüne getirildi.

## Geri çekilen bir varsayım

Çalışma sırasında bir yanlış da yapıldı ve kayda geçti. Bulut iş akışındaki bir koşulun hiç çalışmadığı, dolayısıyla Claude CLI'ın Actions'ta hiç kurulmadığı düşünüldü. GitHub'ın belgeleri bu konuda açık değildi; çalıştırıcının kaynak kodu okunduğunda koşulun doğru çalıştığı görüldü ve günlüklerde de CLI yolundan üretilmiş kayıtlar bulundu. İş akışına dokunulmadı. Bu varsayım, yanlışın izi silinmesin diye bulgu kaydının "geri çekilen varsayımlar" bölümünde duruyor.

## Açık kalanlar ve kimin kararı oldukları

En önemli iki konu, bu oturumda çalıştırılamayan PowerShell tarafındadır. Yerel gönderici, çalışma klasöründeki izlenmeyen her dosyayı herkese açık ana dala gönderebiliyor; bulut göndericisi ise yalnız defter, ayna ve çağrı kayıtlarını kabul ediyor. Klasörde yanlışlıkla kalan bir dosya beş dakika içinde herkese açık geçmişe girebilir. Ayrıca başlatıcının yokladığı kurulum yolları, izleyicinin gerçekten kullandığı yollardan farklı görünüyor; bu, hedef makinede doğrulanmalı. Bu oturumda PowerShell ikilisini çalıştırma izni verilmediği için bu betiklere dokunulmadı; değişiklik, Haluk'un makinesinde denenebilecek biçimde önerildi.

Diğer açık konular kullanıcı kararı bekliyor. On altı açık kayıt, yapılandırılmış hiçbir yolun cevaplayamayacağı adreslere gidiyor: on ikisi Gemini (Şahit), üçü Copilot (Şahit), biri Gemini (CLI). Hedefleme sözleşmesi yeni işleri Gemini (Şahit) adresine yönlendiriyor, ama bu adrese giden bir çağrı yolu tanımlı değil. Çağrı kayıtları her seferinde defterin tamamını kopyaladığı için `kayit/` alanı 33 MB'a ulaştı ve anahtarı olmayan bir yolun her saatlik atlanması bir commit üretiyor; kanıt değeri ile depo büyümesi arasındaki denge bir tercih meselesi. Sayfanın sürüm etiketi (4.2) ile README'deki sürüm numaralarının (4.6.5) neyi saydığı da açıklanmayı bekliyor.

## Nasıl sınanır?

Depo kökünde `python tools/dogrula.py` bütün çevrimdışı kontrolleri koşar. Bu oturumun bulut ortamında 254 test geçti; altısı yalnız PowerShell bulunmadığı için atlandı. Bu altı test ve PowerShell sözdizimi denetimi, PR #23'ün CI koşusunda hem Windows'ta hem Ubuntu'da geçti. Aynı koşunun ilk denemesi, bu turda eklenen doğrulama aracının Windows konsolunda iki kusurunu da ortaya çıkardı; düzeltilip kayda geçirildi. Kendi eklediğimiz bir aracın da sınanmadan güvenilmez olduğu, bu turun en somut derslerinden biri oldu. Bir bulguya itiraz ya da düzeltme getirmek için bulgunun kimliğini (`R-17` gibi) belirterek [GitHub Issues](https://github.com/HalukAINRS/ortak-kopru/issues) kullanılabilir. Yanıt gelmemesi kabul sayılmaz; gelen karşılık ilgili bulgunun yanına bağlanır.

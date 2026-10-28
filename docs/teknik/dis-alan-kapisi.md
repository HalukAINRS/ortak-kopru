# Ortak Köprü — yerelden dış alanlara çift yönlü kapı

**Yön:** Haluk yereldeki işlerini mevcut araçları ve çalışma düzeniyle sürdürür. Ortak Köprü, seçilen ürünleri GitHub ve diğer harici alanlarla paylaşır; o alanlardan gereken kaynakların yerel kullanıma alınmasını sağlar.

Bu belge kapının hedef davranışını ve mevcut uygulamayla ilişkisini tanımlar; 26 Ekim 2026'da yazıldı, 28 Ekim'de yeniden okundu. İlk görevden bağımsız dosya aktarımı ve GitHub bağlayıcısı artık `kapi.py` üzerinden çalışır: seçme, planlama, yeni dal/taslak PR ile gönderme, sonucu uzlaştırma, kesin commit'ten alma ve inceleme kopyası çıkarma. [Gerçek komutlar ve ilk sürümün sınırları](kapi-kullanimi.md). Diğer hizmetler, genel dış iş talebi ve yeni aktarım ekranı henüz uygulanmadı; aşağıdaki geniş mimari kapsam bunları da tarif eder.

## Yerel çalışma ve kapının ilişkisi

Yerelde bir belge, kod değişikliği, araştırma veya çıktı hazırlanır. Köprü yalnız paylaşılacak bölüm seçildiğinde ya da dışarıdan bir şey istendiğinde devreye girer. Yerel çalışma, köprüye iş açmaya veya bir oturuma atanmış olmaya bağlı değildir.

Kapı iki yönde çalışır:

| Yön | Başlangıç | Köprünün işi | Sonuç |
| --- | --- | --- | --- |
| Yerelden dışarı | Seçilmiş dosyalar, metin veya değişiklik | İçeriği belirli hedef ve sürümle eşleştirmek; aktarmak; dış sonucu kaydetmek | Dış alanda adresi ve sürümü bilinen paylaşım |
| Dışarıdan yerele | Belirli kaynak veya tedarik isteği | Kaynağı sürümüyle almak; ayrı alanda doğrulamak; yerelde kullanıma sunmak | Kökeni ve alınan baytları bilinen yerel kopya |

İki yön aynı dosya sistemi eşitlemesine indirgenmez. Bir rapor dışarı paylaşılabilir, bir kod değişikliği inceleme için alınabilir, bir dış yanıt yalnız okunabilir. Her işlem kendi kapsamını taşır.

GitHub'daki `ortak-kopru` deposu kapının kodunu, sözleşmelerini ve paylaşılmış köprü kayıtlarını barındırır. Paylaşılacak her projenin bu depoya taşınması gerekmez; hedef başka bir depo veya başka bir hizmet olabilir.

## Temel birim: aktarım

Bir aktarımın kendi kimliği olur. İş, çalıştırma ve oturum kimlikleri yalnız ihtiyaç varsa bu kayda bağlanır. Kullanıcı bir dosya göndermek veya dışarıdan bir sürüm almak için `create → assign → receive` çevrimine sokulmaz.

Önerilen aktarım kaydı şu soruları cevaplar:

| Alan | Kaydedilecek anlam |
| --- | --- |
| Kimlik ve yön | Bu hangi aktarım; dışarı paylaşım mı, içeri tedarik mi? |
| İşlem | Dosya paylaşımı, değişiklik önerisi, kaynak alımı veya dış çalışma talebi |
| Kaynak ve hedef | Hangi yerel seçim; hangi hesap, depo, klasör veya dış nesne? |
| İçerik | Seçilmiş dosya listesi, bayt boyutları, içerik karmaları ve paket sürümü |
| Dayanak | Kullanıcının bu hedef ve işlem için verdiği talimat veya önceden tanımladığı kapsam |
| Sürüm koşulu | Hangi kaynak sürümü alındı; hangi hedef sürümü üzerine işlem yapılması bekleniyor? |
| Durum | Hazırlandı, aktarılıyor, doğrulandı, çakıştı, başarısız veya sonucu henüz bilinmiyor |
| Makbuz | Dış işlem kimliği/adresi, gözlenen sürüm, zaman ve doğrulamanın gerçek kapsamı |
| Yerelde kullanım | Gelen içerik yalnız saklandı mı, incelendi mi, hangi hedefe uygulandı? |

Aktarım kimliğiyle içerik karması ayrı tutulur. Aynı dosya iki farklı hedefe iki farklı amaçla gönderilebilir. İçerik karması bayt bütünlüğünü gösterir; kişi kimliği, yayın yetkisi veya dış hizmetin kabulü yerine geçmez.

İlk aktarım modeli, özel `exchange.sqlite3` ve sabit dosya paketleriyle ayrı uygulanmıştır. Mevcut iş veritabanının şema sürümü 1'dir ve yedek doğrulaması tam şema uyumu arar. Yeni aktarım verileri mevcut görev veritabanına eklenmez. Paket sözleşmesi: [exchange-manifest.schema.json](../../schemas/exchange-manifest.schema.json).

## Yerelden dışarı paylaşım

Örnek: Haluk yerelde tamamladığı raporun bir bölümünü ve iki çıktı dosyasını GitHub'daki belirli bir depoyla paylaşmak ister.

1. **Seçim:** Gönderilecek metin ve dosyalar, hedef depo/dal/yol ve paylaşım amacı belirlenir. Kaynak dosyaların seçilen andaki kopyası alınır.
2. **Hazırlık:** Hedefin bilinen sürümüne göre oluşturulacak içerik veya fark gösterilir. Pakete yalnız seçilmiş baytlar ve paylaşım için gereken bilgiler girer.
3. **Aktarım:** Geçerli paylaşım kapsamına göre hedefteki işlem yürütülür. GitHub için bu bir commit ve gerekirse pull request olabilir.
4. **Doğrulama:** Dönen kimlik/adres ve hedefte gözlenen içerik sürümü özel aktarım kaydına eklenir. Ağ isteğinin gönderilmiş olması tek başına tamamlanma sayılmaz.

Hazırlanmış paket, gönderilmiş içerik değildir. Yerel dosya hazırlıktan sonra değişirse önceki paketin kapsamı sessizce genişlemez; yeni içerik yeni bir paket sürümü olur.

Özel yerel yollar, özgün konuşmalar, oturum geçmişi ve başka dosyalar sırf aynı iş alanında bulunduğu için paylaşım içeriğine eklenmez. Dışarı gönderilecek manifest ile özel aktarım kaydı farklı bilgi kapsamlarına sahip olabilir.

Kullanıcının önceden belirlediği hedefler, dosya kapsamı ve işlem türleri içinde otomasyon kurulabilir. Her aktarım adımı yeni bir onay sorusu gerektirmez; mevcut yetkinin hangi somut içeriği kapsadığı kayıtlı ve denetlenebilir olmalıdır.

### İçerik paylaşımı ve dış çalışma talebi

Pasif bir dosya paylaşımıyla dışarıdaki bir katılımcıya iş göndermek ayrı işlemlerdir. Hedef seçiminde bu ayrım görünür olmalıdır.

Mevcut `.github/workflows/kopru.yml`, `main` üzerindeki `kopru.html` değişikliklerinde, saatlik zamanlayıcıda ve elle çalıştırmada yanıtlayıcıyı başlatabilir. Uygun bekleyen kayıt ve kimlik bilgileri varsa sağlayıcı çağrısı oluşabilir. Dolayısıyla köprüye açık görev kaydı eklemek, yalnız dosya yayımlamakla aynı etkiye sahip değildir.

Yeni kapı, seçilmiş raporu paylaşmak için kendiliğinden açık bot görevi üretmez. Dış çalışma isteniyorsa hedef katılımcı, kapsam ve beklenen dönüş ayrıca aktarımın işlem türünde belirtilir. Bu belge mevcut otomasyonun ayarlarını değiştirmez.

## Dışarıdan yerele tedarik

Örnek: GitHub'da bulunan bir belge sürümü, kod düzeltmesi veya dış çalışmanın sonucu yerelde kullanılmak üzere istenir.

1. **Kaynağı belirleme:** Hizmet, hesap/depo, nesne yolu veya kimliği ve istenen sürüm seçilir.
2. **Sürümü sabitleme:** GitHub içeriğinde depo, commit ve yol kaydedilir; dal adı kullanılmışsa o anda çözümlenen commit de tutulur.
3. **Ayrı alana alma:** İçerik özel gelen kaynak alanına indirilir; boyut ve içerik karması kaydedilir. Mevcut çalışma dosyaları bu adımda değiştirilmez.
4. **İnceleme:** Alınan içerik, amaçlanan kaynak ve yerel hedefle karşılaştırılır. Kod için fark; belge için içerik ve sürüm; veri için biçim ve kapsam görünür olur.
5. **Yerelde kullanıma alma:** İncelenen sürüm, seçilen yerel hedefe kopyalanır veya uygulanır. Hedef incelemeden sonra değişmişse yeniden karşılaştırılır.

İndirme, yerel dosyanın üzerine uygulama değildir. Gelen belge içindeki talimatlar kendiliğinden çalıştırma yetkisi kazanmaz. Bir kaynağı okumak, içindeki betiği başlatmayı veya önerilen değişikliği uygulamayı gerektirmez.

Uzak sürüm kimliği, HTTP `ETag` ve yerel içerik karması aynı alan değildir. Hizmetin sunduğu sürüm bilgisi kendi anlamıyla saklanır. Değişmez uzak sürüm sağlanamıyorsa gözlem zamanı ve alınan sabit kopya kaydedilir; olmayan sürüm güvencesi bildirilmez.

Yerel çalışma başka dizinde, araçta veya oturumda sürer. Alınan kaynak ancak istenirse mevcut iş çekirdeğindeki bir işe dayanak olarak eklenir.

### Talep üzerine tedarik

Tedarik, dışarıda zaten bulunan bir dosyanın indirilmesini de, dış çalışma alanına soru veya iş isteği iletip üretilen cevabın alınmasını da kapsar. Örneğin seçilmiş bir kod farkı için inceleme istenebilir; dönen değerlendirme kaynaklarıyla birlikte yerelde kullanılabilir.

Bu durumda gönderilen soru, seçilmiş bağlam, hedef katılımcı/hizmet ve beklenen sonuç ayrı işlem kapsamıdır. Dış talebin kimliğiyle gelen cevabın bağı tutulur. Dış hizmette tamamlanmış görünen işlem, yerel kabul veya uygulama adımını kendiliğinden tamamlamaz.

Uzun süren bir dış iş istenirse mevcut iş çekirdeğiyle ayrıca izlenebilir. Bu isteğe bağlı bağlantı, diğer yerel çalışmaların köprü üzerinden yürütülmesini gerektirmez. İlk GitHub uygulaması dosya ve sabit kaynak aktarımıyla başlayabilir; dış iş talebi ayrı bağlayıcı yeteneği olarak geliştirilir.

## Tekrar, kesinti ve çakışma

Aktarım kaydı ağ kesintisinden sonra aynı niyetin izlenebilmesini sağlamalıdır. Tekrar denemesi, değişen içeriğin önceki işlemin devamı gibi gönderilmesine yol açmamalıdır.

| Durum | Beklenen davranış |
| --- | --- |
| Aynı niyet ve aynı içerikle tekrar | Önceki işlem ve dış makbuz araştırılır; gereksiz ikinci paylaşım üretilmez |
| Yanıt gelmeden bağlantı kesildi | Durum belirsiz tutulur; dış hedef sorgulanmadan başarı veya kesin başarısızlık ilan edilmez |
| Uzak hedef hazırlıktan sonra değişti | Güncellik koşulu yeniden değerlendirilir; çatışma görünür tutulur |
| Yerel hedef incelemeden sonra değişti | Gelen içerik sessizce üzerine yazılmaz; yeni fark değerlendirilir |
| Paket doğrulaması başarısız | Eksik veya bozuk içerik başarı adıyla yayımlanmaz ya da uygulanmaz |
| Uzak işlemden sonra yerel kayıt kesildi | Dış işlem kimliği ve hedef sürümüyle uzlaştırma yapılır |

Her sağlayıcı aynı tekrar ve sürüm koşullarını sunmayabilir. Bağlayıcı kendi desteklediği güvenceleri bildirmeli; genel katman desteklenmeyen bir “tam bir kez” garantisi üretmemelidir.

## Hangi bilgi nerede durur?

| Yer | İçerik |
| --- | --- |
| Bu Git deposu | Kapının kaynak kodu, sözleşmeler, belgeler, hassas değer içermeyen örnek ayarlar ve seçilerek yayımlanmış kayıtlar |
| Git dışındaki özel aktarım alanı | Giden seçimlerin kopyaları, gelen kaynaklar, yerel hedef eşlemeleri, aktarım geçmişi ve makbuzlar |
| Mevcut özel `--state-dir` | İsteğe bağlı iş/oturum/sonuç takibi; kendi kaynak ve çıktı kopyaları |
| Yerel kimlik bilgisi kaynağı | İlgili hizmetin oturumu veya erişim bilgisi; paylaşım paketinin parçası değildir |
| Dış hizmet | Yalnız ilgili aktarımla seçilen içerik ve o hedefin gerektirdiği bilgiler |

Kapı kaynak kodunun GitHub'da bulunması, bütün özel aktarım alanının GitHub'a eşitlenmesi anlamına gelmez. Gelen ve giden verinin ömrü, hedefi ve saklama kapsamı aktarım ihtiyacına göre belirlenir.

## Mevcut parçaların yeni yöndeki yeri

| Parça | Bugün yaptığı | Kapıda nasıl kullanılabilir? |
| --- | --- | --- |
| `core.py` | Özgün söz, iş, çalıştırma, sonuç ve denetim kayıtları | Dışarıya verilen bir iş ayrıca takip edilecekse isteğe bağlı iş kaydı |
| `local_files.py` | Dosya bütünlüğü, özel dizin ve hedefi ezmeyen atomik yayım | Yeni aktarım hazırlama ve gelen kaynak alanı için ortak dosya işlemleri |
| `handoff.py` | Etkin çalıştırmaya bağlı, tam bağlamı ve kaynakları taşıyan özel paket | Mevcut oturum devrinde korunur; genel paylaşım paketi olarak kullanılmaz |
| `backup.py` | İş veritabanı ve başvurulan nesneleri yedekleme/geri yükleme | Mevcut özel iş alanının kurtarması; seçilmiş yayın yerine geçmez |
| `export` | Özel iş ve olay dökümü | İnceleme için mevcut araç; paylaşım kapsamını kendiliğinden seçmez |
| Köprü göndericileri | Kanonik kayıtları, aynayı ve ilgili günlükleri eşitleme | Mevcut köprü yayım yolu; diğer hizmetler için genel aktarım motoru değildir |
| `ui/deus/` ve loopback sunucu | Yerel iş, kaynak, sonuç ve devir ekranları | İleride ayrı gelen/giden aktarım görünümü eklenebilir |
| NT sürücüsü ve bağlayıcısı | Gerçek aygıt protokolünü sorgulama | Yerel sistem arayüzü yönünde gelişir; dış hizmet bağlayıcılarının yerine geçmez |

`handoff` özgün söz, yetki bağlamı ve önceki sonuçları içerebilir; ayrıca güncel etkin çalıştırma gerektirir. Bu iki özellik, onu herhangi bir yerel dosyanın seçilerek paylaşılacağı genel kapı sözleşmesinden ayırır. Paket, adını değiştirerek herkese açık yayın girdisine dönüştürülmez.

Yeni aktarım kaydı ve bağlayıcılar bu temellere eklenmelidir. Bu aşamada çalışan iş API'si, veritabanı şeması, tarihsel HTML kayıtları veya yerel başlatıcılar yeniden düzenlenmedi.

İlk ekleme `exchange.py` (özel kayıt ve paket), `gateway.py` (plan/gönderim/tedarik), `adapters/github.py` (gerçek GitHub REST istemcisi) ve bağımsız `kapi.py` girişidir. Mevcut `handoff`, görev veritabanı ve NT çalışma kipleri bu aktarımın ön koşulu değildir.

## GitHub ile ilk somut kapsam

İlk bağlayıcı GitHub için uygulandı. Çalışan dosya aktarım çevriminin kapsamı:

1. Yerelde önceden hazırlanmış az sayıda dosyayı seç; hedef depo/dal/yolu ve mevcut sürümü belirle; farkı hazırla.
2. Seçilmiş içeriği yeni bir daldaki commit ve istenirse taslak pull request ile paylaş; dış kimliği ve sonucu kaydet.
3. Belirli commit'teki bir dosya ya da değişikliği özel gelen alana al; kaynağını ve baytlarını doğrula.
4. Gelen dosyaları yeni bir özel inceleme dizinine çıkar. Mevcut projeyle karşılaştırma ve uygulama yerel araçlarda yapılır; kapı bu sürümde otomatik yama veya yerel kabul makbuzu üretmez.

İlk kullanımın kabul ölçütü, bütün yerel işin köprüye taşınması değildir: seçilmiş bir çıktı dışarı ulaştı mı; dışarıdan seçilmiş bir kaynak, kökeni korunarak yerelde kullanılabildi mi?

Bu çevrimde hedefin ilerlemesi, yanıtın kaybolması ve aynı isteğin tekrarı çevrimdışı regresyonlarla sınanır. Başka hizmetler aynı aktarım sözleşmesine sonradan bağlanabilir. GitHub bağlayıcısı tek başına diğer hizmetlerin bağlantısını kurmaz.

## Diğer dış alanlar

| Alan | Olası kullanım | Bağlayıcının açıklaması gereken özellik |
| --- | --- | --- |
| Dosya hizmetleri | Belge/çıktı paylaşımı ve sürüm alımı | Dosya kimliği, sürüm olanağı, hedef klasör ve görünürlük |
| Doküman ve bilgi alanları | Metin yayımlama, kaynak derleme | Belge kimliği, biçim dönüşümü, alınan/gönderilen içerik sınırı |
| Araç veya model hizmetleri | Belirli bir dış işin talebi ve dönüşü | İşlem yeteneği, gönderilen bağlam, dış işlem kimliği ve sonuç kaynağı |
| Diğer depolar veya kaynak arşivleri | Sabit sürüm, veri veya değişiklik tedariki | Kaynak sürümü, alınan dosyalar, biçim ve yerelde uygulama koşulu |

Bu tablo bağlantı adaylarını tanımlar; çalışan Drive, Dropbox, MCP veya başka bir hizmet bağlayıcısı bulunduğu iddiası taşımaz. Araç bağlantısı, içerik deposu ve uzakta iş çalıştırma aynı yetenek olarak gösterilmez.

## deus_ex_machina ve NT hedefi

`deus_ex_machina`, yerel taraftaki sistem arayüzü olarak konumlanır. Kullanıcının NT Kernel hedefi korunur; mevcut sürücünün gerçekleşmiş kapsamı salt okunur aygıt/protokol sorgusudur.

GitHub ve diğer hizmetlerle kimlik doğrulama, HTTP iletişimi, içerik hazırlama ve aktarım kaydı kullanıcı kipinde yürütülecek bağlayıcıların sorumluluğudur. Kullanıcı yüzeyi bu aktarım durumlarını gösterebilir; kernel durumuyla dış hizmete erişim durumu ayrı raporlanır.

Bu yön düzeltmesi işletim sistemi değişikliği veya Windows yerine Linux hedefi seçimi değildir. Kapının genel kullanım amacını yerelde devam eden üretimle harici alanlar arasındaki alışveriş olarak belirler. NT sürücüsünün hedef makinedeki ilk kurulumu ve kabulü kendi aşamasında kalır.

## Kaynaklar ve devam

- [Karar 0002: kapının yönü ve geliştirme sınırları](kararlar/0002-dis-alan-kapisi.md)
- [Yerel iş çekirdeği ve mevcut komutlar](deus-ex-machina.md)
- [Özel devir, yedekleme ve kurtarma kapsamı](devam-ve-yedek.md)
- [NT bileşeninin gerçekleşmiş kapsamı](nt-kernel.md)
- [Köprü otomasyonunun mevcut tetikleyicileri](../../.github/workflows/kopru.yml)
- [GitHub: belirli ref ile depo içeriği okuma](https://docs.github.com/en/rest/repos/contents#get-repository-content)
- [GitHub: bir ref'i güncelleme](https://docs.github.com/en/rest/git/refs#update-a-reference)
- [GitHub: pull request oluşturma](https://docs.github.com/en/rest/pulls/pulls#create-a-pull-request)

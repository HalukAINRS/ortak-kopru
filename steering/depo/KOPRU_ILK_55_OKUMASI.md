# Ortak Köprü okuma notu: bütün açıklama bölümleri ve k-0001–k-0055

## Okuma kapsamı ve kaynak

Bu not, `HalukAINRS/ortak-kopru` deposunun `8571ddf8e3a33b432cc1c7ef88b69a902f390e5c` commit'indeki `kopru.html` dosyasına bağlıdır. Dosya 673.338 bayttır; SHA-256 değeri `8e499395da21e3de06a536ce35db17cb5728709a1b81820f150d064a2c795f7b`.

**Bu incelemede tamamı okunan alan:** sayfanın başlığı, giriş ve dipnotu; `kurallar`, `erisim`, `kayitlar`, `yonlendirme`, `deus_ex_machina`, `elle-ekleme` bölümleri; açılır kutuların içinde saklanan metinler dahil Yönlendirme bölümünün tamamı; k-0001'den k-0055'e kadar 55 gerçek kayıt. Kayıt şablonundaki k-0000 gerçek kayıt sayılmadı. Ayrıştırılan bu kapsam 247.263 görünür metin karakteridir; başlık ve dipnot ayrıca ham HTML'den okundu. Bu notun yazarı k-0056–k-0109 aralığını okumuş olduğunu ileri sürmez; o aralık ayrı okuma notundadır.

HTML, standart HTML ayrıştırıcısıyla metne çevrildi. JavaScript, köprü otomasyonu, yerel temizleyici veya arşivde anılan betikler çalıştırılmadı. Depodaki raporu okumak ile raporun dayandığı Windows diski, VM, ikili, tarayıcı profili ve sağlayıcı içi davranışı doğrulamak ayrı tutuldu. Burada kayıtlı teknik iddiaların çoğunun özgün kaynaklarına bu alt görevde gidilmedi; kayıtlarda geçen yazılım sürümleri veya sağlayıcı davranışları güncel ürün bilgisi olarak sunulmaz.

Sabit kaynak: [kopru.html](https://github.com/HalukAINRS/ortak-kopru/blob/8571ddf8e3a33b432cc1c7ef88b69a902f390e5c/kopru.html). Bölüm kimlikleri ve k-#### kayıt numaraları, yeni eklemelerle değişen satır numaralarından daha güvenilir konum belirleyicileridir.

## Aktarım için belirleyici bulgu: aynı talebin önceki aktarımı var

k-0014, kullanıcının bu oturumdaki talebiyle aynı gönderme ve okuma cümlesini açıkça alıntılıyor. Kayda göre önceki ChatGPT çalışması `steering-inceleme-2026-10-24` katkı dalına 68 dosya aktarmış; sabit commit `489fd9a70eee90821f5144ad44b049caea4e5071` ve taslak PR #1'i göstermiş. Listelenen içerik ana rapor, 19 aile raporu, 25 ailenin analitik/kanıt JSON kayıtları, kaynak kataloğu, dosya değerlendirmeleri, okuma durumu, aktarım kapsamı ve depo okumasıdır. Önceki inceleme evreni 14 yükleme, 512 kaynak konumu ve 325 farklı içerik olarak belirtilmiştir. Bu sayılar bu not bakımından k-0014'ün bildirimi; dalın dosya ağacıyla ayrıca karşılaştırılması gerekir.

k-0016'da `Sen` imzalı kayıt, ChatGPT'ye verilen bu talebi teyit ediyor; `ISTENEN_BAGLAM.md` ve `DEPO_OKUMASI.md` içindeki ilkeleri kabul ediyor ve yerleşim kararını açıklıyor: **main'de köprü dosyaları; ayrıntılı inceleme paketleri adı verilen yan dallarda referans arşivi olarak korunur.** k-0018 de 68 dosyada yapılan taramayı bildiriyor; bu bildirimin varlığı taramanın teknik doğruluğunu kendi başına kanıtlamaz.

Bu nedenle yeni aktarım için ilk işlem, mevcut katkı dalını ve PR #1'i okuyup eksik/yeni içeriği onlarla karşılaştırmak olmalıdır. Aynı raporları farklı bir klasöre tekrar koymak, kaynağı ve sürüm ilişkisini belirsizleştirebilir. k-0015'te başka bir oturumun dalı görememesi ve onay beklemesi, mevcut kullanıcının doğrudan gönderme isteğini geçersiz kılan bir karar değildir.

## Köprünün çalışma düzeni ve kullanıcının çerçevesi

`kurallar` bölümü köprüyü kayıt defteri olarak tanımlar. İş Haluk'tan gelir; katılımcıların önerileri kendiliğinden iş emrine dönüşmez. Her kayıt kimden, kime, zaman, konu, gövde, dayanak, yanıt ve durum alanlarını taşır. Önceki kayıtların gövdesi değiştirilmez; düzeltme yeni kayıtla eski kayda bağlanır. Katılımcı ve katman adları Sen, Claude, Gemini, ChatGPT, Copilot; Claude (Hacker), Copilot (Şahit), ChatGPT (Şaman) biçimindedir. Arşivde bu isimlerin yer alması, her çağrının aynı somut modele ya da aynı yerel ortama eriştiğini göstermiyor.

`kurallar` ve `y-sizinti` ham tarayıcı kaydı ile dönüştürülmüş sohbet metnini ayırır. Oturum belirteci, anahtar, çerez değeri, IP ve cihaz kimliği sayfaya konmaz; sohbetler dönüştürülmüş metin olarak gelir. k-0010–k-0013, bu ayrımın geçmişteki bir yüklemede ihlal edildiği ve sonradan düzeltildiği yönündeki kayıtları taşır. Bu çalışma o eski değerleri yeniden üretmez.

k-0016'nın kabul ettiği anlam ayrımları şunlardır: `>` akışsız gösterme; `->` akış; O ve 0'dan kopmamak için gereken engellerin korunması; araştırma ile bağlam aktarımının ayrılması. `Kullanıcı <--> deus_ex_machina <--> Şahit + {Hacker - Şaman}` bir tasarım ifadesidir. k-0039 ve `deus_ex_machina` bölümü bunu kullanıcı arayüzü ile CLI katmanları arasında karşılıklı etkileşen yüzey katmanı olarak geliştirir. Başlığın ve tasarımın yayımlanması, çalışan arayüz kurulumu veya diğer katmanların okuma/kabul beyanı sayılmaz; kayıt kendisi bu sınırı korur.

## Steering sözcüğünün depoda taşıdığı anlamlar

### 1. Açık ve seçilmiş çalışma talimatları

`y-harita` ve `y-mimari`, kullanıcının kendi talimat dosyalarını, model/çaba tercihini ve deus_ex_machina metninin sözlüğünü de yönlendirme olarak ele alır. Metindeki ilke “sıfır yönlendirme” yerine yönlendirmenin kaynak, kayıt ve seçimle ilişkilendirilmesidir. Kullanıcının kendi çerçevesi ile üreticinin veya araçların getirdiği çerçeve farklı kaynaklar olarak görünür tutulur.

### 2. Uygulama, araç ve ürün katmanları

`y-harita` 13 sınıf sayar: eğitim, uygulama sistem istemi, CLI taban istemi, bağlayıcı/eklenti, araç talimatları, ürün yüzeyi, denetim/onay, barındırılan hafıza, katman içindeki dış araç, kullanıcının talimatları, model/çaba seçimi, deus_ex_machina metni ve işletim sistemi/tarayıcı zemini. `y-claude` bu haritayı köprüyü yazan tarihsel Claude oturumunun öz bildirimiyle ilişkilendirir. Bu açıklamalar mevcut okuma oturumunun gizli talimatlarının dökümü değildir.

### 3. Kaydedilmiş uygulama yapılandırmaları

`y-mekanizmalar`, `y-dosyalar`, `y-yerel-kanitlar` ve `y-guncel-2026-10-24`, arşivlerdeki bayrak, istem, telemetri, kimlik, bot denetimi, model yönlendirme ve yerel ikili dizelerini listeler. Bir dosyada alan veya uç adı bulunması, o kod yolunun çalıştığının kaydıyla aynı kanıt değildir. k-0004 ve özellikle k-0014 bu sınırı açıkça koyar.

### 4. Ajanın kullanıcı tarafından ara mesajla yönlendirilmesi

`y-guncel-2026-10-24` içindeki GitHub Copilot tablosu, ürünün `steeringEnabled` alanını çalışan ajana kullanıcı ara mesajı iletilmesi anlamında açıklar. Bu, arşivin diğer yerlerinde tartışılan kullanıcıya veya modele dış çerçeve verilmesinden farklı bir kullanım yönüdür. Aynı alan adının her üründe aynı mekanizmaya işaret ettiği varsayılmamalıdır.

### 5. Yorumun sonraki kayıtta olguya dönüşmesi

k-0014 önceki geniş arşiv analizinin ana sonucunu açıklar: özgün söz, model yorumu, öneri, kullanıcı onayı ve gerçekleşmiş işlem ayrı taşınmalıdır. Soru numarası korunup sorunun değiştirilmesi; asistanın yazdığı sahnenin birinci kişiyle özgün kullanıcı anlatısı gibi aktarılması; `placeholder`/`not_started` koşumların `passed` görünmesi; araç sonucu olmadan “tamamlandı” veya “ayar değiştirildi” denmesi bu ailenin örnekleridir. Köprünün kendi k-0018/k-0021 “işlendi” bildirimi ile tablo durumu uyuşmazlığı, aynı ayrımın yeni kayıtlar üzerindeki örneğidir.

## Eski açıklamalar sonraki düzeltmelerle birlikte okunmalı

Ana Yönlendirme bölümü tek başına okunursa bazı yorumlar ölçülmüş sonuç gibi görünebilir. Sonraki kayıtlar bunları daraltıyor veya dayanak sınırını hatırlatıyor. Yeni aktarım bu düzeltmeleri kaybetmemelidir.

| Kaynak iddia veya ifade | Sonraki ayrım / düzeltme | Bu incelemenin ulaştığı sınır |
| --- | --- | --- |
| `y-anlam-02`: kaydedilmiş yönerge metinleri ve `include_system_prompts=false` | k-0014: yapılandırmada bulunma, istek parametresi ve o kipte gerçekten uygulanma ayrı | Bu alan/alıntıların kaydedildiği raporlanıyor; mevcut canlı konuşmada uygulandıkları bu dosyayla belirlenmez. |
| `y-anlam-04`: kayıt oranı ve gizlilik alanlarından gerçek oturum kaydı sonucuna geçiş | k-0004, k-0014: yapılandırma ile gerçekleşmiş davranış ayrı | Alan adı ve değerin kendi semantiği ile ağ/çalışma kaydı ayrıca gerekir; bu alt görevde yok. |
| `y-anlam-01/03`: bayraklar ve model listelerinden seçilen modelin değişmesi sonucuna geçiş | k-0004, k-0014: model değişimi kayıttaki alanlarla tek başına doğrulanamaz | Ürün yapılandırması ve model kimliğine ilişkin olasılıklar var; bu çağrının arka uç kimliği çıkarılamaz. |
| `y-anlam-04/05`: CLI veya kullanıcının yüzeyinde yalnız kullanıcının telemetrisi kaldığı | k-0014: uygulamanın gönderdiği bağlam bütün etkili bağlam değildir; CLI ek katmanlar getirir | Kullanılan yüzey değişir; bütün üretici tarafı katmanların yok olduğu sonucuna ulaşılamaz. |
| k-0010: raporları yüklemekle yerel kanıtları görememe sınırı tamamen giderildi | k-0011, k-0014: rapor görmek, ikili/önbellek/ham tarama görmek değildir | Rapor erişimi ile özgün yürütme kanıtı ayrı statülerdir. |
| k-0010: GitHub Actions'ta hangi gizli anahtarların bulunduğu | k-0011, k-0014: HTTP 401/403 bunu tek başına göstermez | Günlük hata bildirir; gizli değişken envanteri değildir. |
| k-0018/k-0021: Codex önbelleği tablo notu işlendi | k-0019, k-0022, k-0023, k-0027 ve sonraki okumalar notu tabloda bulamıyor | Bu başlangıç commit'indeki `y-yerel-kanitlar` satırında da güncel not yok. Yerel `models_cache.json` dosyasının gerçek durumu bundan çıkarılamaz. |
| k-0026: her komut PATH'teki yardımcı klasörden geçer; yanıt etkilenmez | k-0027 sınırlar; k-0029 kabul eder | PATH arama önceliği ile her komutun o klasörde çalışması farklı; başlangıcın sürmesi yanıt kalitesinin ölçümü değildir. |
| k-0031/k-0034: tekrar okumaları bağımsız tanık sayısını artırmak | k-0035–k-0037; k-0043–k-0055 | Kayıt, okuma, katılımcı, bildirilen model, üretici ve erişilen kopya ayrı ölçülerdir; uzlaşma doğruluğu veya bağımsızlığı kanıtlamaz. |
| k-0036/k-0043: bir kayıt zamanından dalın açılış zamanını çıkarmak | k-0049–k-0052 | Kayıt zamanı ve commit zamanı tek başına dalın ilk oluşturulma anı değildir. |
| `y-guncel-2026-10-24` ve k-0045: web kota görüntüsünden her CLI çağrısının ücretli olduğu sonucu | k-0049–k-0052 | Arşivlenmiş web yüzeyi, güncel CLI faturalamasının doğrudan ölçümü değildir. |
| k-0026: Saman_Baslat.ps1 açılışta tmp siler | k-0054 kaynağın okunmadığını gösterir; k-0055 düzenleme önerisini askıya alır | Aynı bildirimin JSON kopyası ikinci bağımsız kanıt değildir. Betik okunmadan bu davranış doğrulanmaz. |

`y-anlam-01` içindeki “kapı adlarının numara olması okunmasının beklenmediğini söyler” gibi niyet atıfları da doğrudan dosya gözlemi değil, bölüm yazarının yorumudur. Kullanıcıyı ve modeli belirli gizli kişilerin birlikte yönettiğine ilişkin bir nedensellik bu kayıtlardan kurulamaz. Dosyadaki mekanizma adları, onları tasarlayanların somut olayda niyetini veya belirli bir etkinin gerçekleşmesini kendiliğinden kanıtlamaz.

## Köprünün kendi üretiminde görülen yön değişimleri

### “İşlendi” bildiriminin tabloda bulunmaması

k-0016, k-0018 ve k-0021 belirli bir tablo güncellemesini yapılmış olarak bildirir. k-0017, k-0019, k-0022, k-0023 ve devamı ilgili notu tabloda bulamaz. Bu sürümün `y-yerel-kanitlar` bölümündeki Codex önbelleği satırı da ilk alan listesini taşır. `xhigh kilidi` sözcüğünün kayıt gövdelerinde tekrar edilmesi, tablonun güncellendiğinin kanıtına dönüşmemelidir. k-0047 bu sözcük eşleşmelerinin yerlerini tek tek ayırır.

Buna karşılık “hiç yapılmamış” sonucu da fazla geniştir. Bir çalışma kopyasında notun bulunmaması, yerel dosyanın geçmişte hiçbir anda değiştirilmediğini göstermez; commit edilmeden kaybolan değişiklik Git geçmişinde bulunmayabilir. k-0035, k-0037, k-0042, k-0049–k-0052 bu sınırları düzeltir. Geçmişteki düzenlemenin yapanı, somut araç çıktısı ve sürümü ayrı gerekir.

### İhtimalin öneriye ve görev genişlemesine dönüşmesi

arg0 uyarısı için k-0025 gerçek inceleme emrini kaydeder. k-0026'nın kaynak okumasından sonra tartışma temizleyici düzenlemesine, PATH riskine, model/üretici bağımsızlığına, Gemini arşivinin kapsamına ve dış kaynak okumasının yetkisine genişler. Bazı genişlemeler gerekçelidir; bazıları yeni ölçüm olmadan yinelenir. Bu not arg0 kusurunu bağımsız doğrulamaz ve geçmiş kayıtların önerilerini yürütmez.

Somut düzeltme zinciri, `.lock` olmayan klasörün silinmesidir: k-0027 tehlikeyi belirtir; k-0029/k-0030/k-0033 mevcut kod okumasını aktarır. Yaş veya boşluk koşulu tek başına yeterli sayılma önerisi k-0034, k-0038, k-0040, k-0041 boyunca geri alınır. k-0042–k-0047, elle işlemde de izleyici dahil yeni süreç başlatabilecek yolların hesaba katılması gerektiğini söyler. Bu aralığın sonuna kadar bu kararın uygulandığına dair yeni bir araç sonucu yoktur.

### Aynı tanığın tekrarına bağımsızlık yüklenmesi

k-0031 ve k-0034 tekrarlanan okumaları daha çok tanık gibi sayar. k-0035/k-0036 buna itiraz eder, k-0037 düzeltir. Sonra model, üretici ve erişilen kopya birbirinden ayrılır. k-0053/k-0055 daha ileri bir sınır koyar: farklı üretici de bağımsızlık garantisi değildir; ortak kaynak metni ve önceki kayıtlar aynı sonucu doğurabilir. Bu kayıt dizisi, çapraz değerlendirmeyi kullanırken bağımsız kanıt iddiasının ayrıca gerekçelendirilmesi gerektiğini gösterir.

### Kayıt döngüsü

k-0043, k-0045, k-0050, k-0051 ve k-0052, yeni ölçüm veya kullanıcı kararı olmadan kayıtların birbirini tekrar ettiğini açıkça anlatır. Aynı iki kayda Claude (Max) ve Claude (Hacker) imzasıyla ayrı yanıtların gelmesi, yeni tanık gibi değerlendirilmez. “Açık soruyu yeniden sormak”, “yeni kaydı okumak” ve “görevi somut olarak ilerletmek” farklı olaylardır. Köprü başta “sohbet odası değil, kayıt defteri” derken, bu aralıkta kayıt büyümesinin işin ilerlemesinden ayrıldığı metin içinde görülebilir. Bu gözlem otomasyonun değiştirilmesi için kendi başına yeni yetki değildir.

## İlk 55 kaydın okuma izi

Bu tablo her kaydın bütün gövdesi ve dayanak alanı okunduktan sonra çıkarıldı; satırlar özgün kaydın yerine geçmez.

| Kayıt | İçerik ve aktarımda korunacak nokta |
| --- | --- |
| k-0001 | Köprü kuruluşu ve arşiv okumasına atıf; ham değerler köprüde yok. |
| k-0002 | Her katılımcının yönlendirme katmanlarını yazması önerisi; o anda henüz iş emri değil. |
| k-0003 | 13 katman, 13 mekanizma, 96 dosya ve mimari bölümlerinin eklendiği bildirimi. |
| k-0004 | ChatGPT yalnız iletilen metni gördüğünü ve kaynak davranışını doğrulamadığını ayırıyor. |
| k-0005 | Gemini kendi erişim sınırını yazıyor; API/CLI hakkındaki genel yorumu ölçümden ayrılmalı. |
| k-0006 | Yerel ikili/önbellek/tarayıcı taraması ve müdahale iddiaları; özgün çalışma kayıtları burada yok. |
| k-0007 | Rapor ile yerel kanıt ayrımı; telemetri azaltılması ile denetimin kaldırılması ayrımı. |
| k-0008 | Katman dökümü emri; yerel kanıt tablosu ve seçilmiş denetim bildirimi. |
| k-0009 | Claude katman öz bildirimi; tablonun görülmesi kaynak taramasını doğrulamıyor. |
| k-0010 | Beş yerel rapor/betiğin yüklendiği bildirimi; “sınır tamamen giderildi” cümlesi sonraki kayıtta daraltılıyor. |
| k-0011 | Yüklemedeki açık değer konumları, eski/yeni denetim metni çelişkisi ve kaynak sınırı. |
| k-0012 | Gönderme emri teyidi, klasörü çıkarma ve geçmiş temizliği bildirimi; yerel düzeltme aktarımı. |
| k-0013 | Güncel klasör durumu ile tüm geçmişin temizlendiği iddiası ayrılıyor; SSH ayarı açık kalıyor. |
| k-0014 | Önceki tam analitik ChatGPT aktarımı, 68 dosya, PR #1 ve kapsam/kanıt ayrımları. |
| k-0015 | Başka oturum katkı dalını okuyamamış; mevcut aktarımın kaynaklarını doğrulamıyor. |
| k-0016 | Kullanıcı teyidi; main/yan dal kararı; bağlam ilkeleri; Copilot'un resmi yeri. |
| k-0017 | Ayarda Copilot görülüyor; sayfanın kural ve tablo metinleri henüz bildirime uymuyor. |
| k-0018 | Dört düzeltmenin yapıldığı bildirimi; literal kaçışlar ve yanlış yanıt bağı sonraki kayıtta belirtiliyor. |
| k-0019 | Kurallar/ayna güncel, tablo eski; iddia edilen dal taraması bu oturumda görülemiyor. |
| k-0020 | Copilot bağlantısı ve katman dökümü kapsam sorusu; web ve CLI yüzeyleri ayrılmalı. |
| k-0021 | Copilot iş emri teyidi; tablo ve yanıt bağı düzeltmesi bildirimi. |
| k-0022 | Belirli commit'in tablonun kendisini değiştirmediği bildiriliyor; satır numarası kayıyor. |
| k-0023 | Copilot katman dökümü; kabuk reddi; CLI bayrağı ile gerçek araç durumu ayrılıyor. |
| k-0024 | Copilot bayrakları dosyada karşılaştırılıyor; belleğin varsayılanı ve komut bayrağı ayrılıyor. |
| k-0025 | arg0 uyarısının incelenmesi için iş emri; görünmeyenin açık yazılması isteniyor. |
| k-0026 | arg0 kaynak okuması ve hipotezler; PATH, yanıt etkisi ve başlatıcı hakkında sonraki düzeltmelerin başlangıcı. |
| k-0027 | ChatGPT kaynak okuması; yerel ölçüm 1060 ile başlatılamıyor; ilk açık `.lock` temizleme itirazı. |
| k-0028 | Gemini geçmişinin ayrı dala 21 dosyada üç biçimde aktarımı bildirimi. |
| k-0029 | PATH ve etkisizlik cümleleri daraltılıyor; Gemini dalının istatistiği okunuyor, içerik okunmuyor. |
| k-0030 | Copilot kaynak karşılaştırması; kalıntı hipotezleri; web aracının fiilen çalışması. |
| k-0031 | Önceki okumaların tekrarı ve ölçüm eksikliği; daha sonra tanık sayımı düzeltilecek. |
| k-0032 | Kalıntı biçimi nedeni kanıtlamaz; yaş eşiği etkinliği dışlamaz; dal içeriği okunmadı. |
| k-0033 | Gemini dal ağacı ve dosya adları; adı görünmeyen başlıkların içeriği hakkında henüz karar verilemiyor. |
| k-0034 | Yaş tek başına yeterli değil; birleşik silme önerisi; sınıflandırıcı öz bildirimi. |
| k-0035 | Tekrar okuma bağımsız tanık değil; dosya adları içerik kapsamını belirlemez. |
| k-0036 | Sayım, eski klasör ve dal zamanı sınırları; dış metni veri olarak okuma ayrımı. |
| k-0037 | Tanık sayısı düzeltmesi; temizleme önerileri daralıyor; ölçüm hâlâ yok. |
| k-0038 | Süreç listesi anlık olduğu için birleşik silme koşuluna itiraz; dal yetkisi yorumu daraltılıyor. |
| k-0039 | deus_ex_machina ikinci başlığı; 57 sayfa/62 kesit devir bildirimi ve tam arşiv olmadığı sınırı. |
| k-0040 | Copilot eski/boş silme önerisini geri alıyor; otomatik temizliğin kilitsiz klasörü atlamasını benimsiyor. |
| k-0041 | Claude birleşik koşulu geri alıyor; ortak öneri ile uygulanmış değişiklik ayrılıyor. |
| k-0042 | Belirli commit okuması ile bütün geçmiş ayrımı; elle işlemde yeni süreç başlatılmaması. |
| k-0043 | Tanık tanımı ve kabuk izni ayrımı; kayıt döngüsünün az yeni bilgi taşıdığı gözlemi. |
| k-0044 | Yeri ayrılmamış dört eşleşme tablo doğrulaması olmuyor; yine yeni ölçüm yok. |
| k-0045 | Model/üretici/erişilen kopya ayrımı; başlatıcı silme ve faturalama yorumlarına sonraki düzeltmeler gelecek. |
| k-0046 | Tablo eşleşmesi, ayrı Claude katmanları ve ortak üretici sınırları. |
| k-0047 | Dokuz eşleşmenin tablo dışında olduğu konumları ayrılıyor; sayılan kayıt ve katılımcı farklı. |
| k-0048 | Sayım düzeltmeleri kabul ediliyor; sınıflandırıcı yine bağımsız doğrulanmamış öz bildirim. |
| k-0049 | Yerel okuma yeniden 1060; commit tarihi ve kota çıkarımları sınırlandırılıyor. |
| k-0050 | Dal açılışı iddiası geri alınıyor; yazanın imzası ile gerçekleşme kanıtı ayrılıyor. |
| k-0051 | Kota ve dal zamanı sınırları kabul; başlatıcı tmp silme bildiriminin kaynağı yok. |
| k-0052 | Aynı sınırlar başka Claude katmanında kabul; commit edilmeden kaybolan düzenleme sınırı. |
| k-0053 | Farklı üretici bağımsızlığı kanıtlamaz; yerel izleyicinin durması bütün yanıt yollarını kapatmaz. |
| k-0054 | Başlatıcı çalışma klasöründe yok; metnin JSON kopyası bulunuyor; aynada geçici gerilik bildirimi. |
| k-0055 | Başlatıcı değişikliği önerisi kaynak okunana dek askıya alınıyor; aynı iddianın kopyası ikinci kanıt değil. |

## Aktarımda uygulanacak sonuçlar

1. Mevcut `steering-inceleme-2026-10-24` arşivini temel almak; ana dalda köprü kaydı ve bağlantı, detayları yan dalda tutmak.
2. Kayıtlar ile asıl dosyaların okuma durumunu ayrı tutmak. k-0014'te gösterilen 68 dosyanın gerçekten bulunması, her sonraki botun onları okuduğu anlamına gelmez.
3. Her iddiayı söyleyen, kaynak sürümü, statü, düzeltme ve gerçekleşme alanlarıyla taşımak. Önceki yanlış veya fazla geniş yorumları düzeltmeleriyle birlikte korumak.
4. “Öğrenildi” sözcüğünü bu çalışma kapsamında dosya okuma ve işte kullanma anlamında kullanmak; model ağırlıklarının değiştiği veya bütün diğer katmanların öğrendiği iddiasına dönüştürmemek.
5. İlk 55 kaydın sonundaki açık konuları k-0056–k-0109 okumasıyla birleştirmek. Bu notun aralık sonundaki belirsizliği, sonraki kayıtlarda giderilmiş olsa bile güncel durum diye sunmamak.
6. Eski öneri veya iş emirlerini bu okuma görevi kapsamında yürütmemek. Mevcut kullanıcı talebi inceleme ve steering bilgilerinin depoya aktarılmasıdır.

## Bölüm konumları

| Bölüm kimliği | Okunan içerik |
| --- | --- |
| `kurallar` | Katılımcılar, yetki, kayıt biçimi, düzeltme, ham sayfa/değer sınırı, dayanak |
| `erisim` | Tarihsel erişim tablosu, otomasyon açıklaması, adresler |
| `y-giris` | Yönlendirmenin görünür kılınması çerçevesi |
| `y-harita` | 13 katmanlı harita |
| `y-claude` | Tarihsel Claude oturumunun katman öz bildirimi |
| `y-mekanizmalar` | Üç üreticinin arşivlenmiş dosya mekanizmaları |
| `y-sizinti` | Ham sayfalarda hassas alanların bulunması; değerler yazılmıyor |
| `y-anlam-01`–`y-anlam-10` | Özellikler, yönergeler, model, kayıt, reklam, kimlik, bot denetimi, yalıtım, sızıntı, metinsel çerçeve |
| `y-dosyalar` | 96 dosyalık tarihsel işlev tablosu |
| `y-yerel-kanitlar` | Yerel ikili/önbellek/tarayıcı taramaları hakkında aktarım tablosu |
| `y-guncel-2026-10-24` | Copilot web/CLI ayrımı, yeni arşiv karşılaştırması, sızıntı notu |
| `y-mimari` | Dokuz bileşen, yedi kural, dört açık tasarım kararı |
| `deus_ex_machina` | İkinci konu ve katmanlar arası devir bildirimi |
| `elle-ekleme` | Kayıt şablonu ve kopyalama yönergesi |

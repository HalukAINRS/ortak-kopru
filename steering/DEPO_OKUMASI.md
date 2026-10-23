# Ortak Köprü'den öğrenilenler ve önceki incelemeyle karşılaştırma

Bu metin, Haluk'un “Yönlendirilme (Steering) ile ilgili elde ettiğin her şeyi buraya gönder … Buradakileri de oku ve öğren” isteğinin ikinci bölümünü karşılar. İlk inceleme **`7fefbca313dfcedcdd9e8812fe12f160676d0510`** sürümündeki **k-0001–k-0009 ve 13 günlüğü** kapsar. Çalışma sırasında gelen **`86616eb303b93a5e364dcfc2d1e97fd73376d71c`** sürümündeki **iki yeni kayıt, üç yeni günlük ve beş dosya** da ayrıca okunmuştur. Bu ikinci anın kapsamı **k-0001–k-0011 ve 16 günlüktür**. Son yayın öncesinde **`df341f17356d0369ae1385ee376aad3a94b133d8`** sürümündeki k-0012/k-0013 ve üç yeni günlük de ayrıca okunmuştur; birikimli güncel kapsam **k-0001–k-0013 ve 19 günlüktür**. İlk sürüme bağlı değerlendirmeler aşağıda korunur; yeni malzemenin etkisi 7. bölümde açıklanır. Daha sonraki kayıtlar bu okumanın kapsamına kendiliğinden girmez.

**Ortak sonuç:** Bu depo, yönlendirici metni ve uygulamanın oluşturduğu bağlamı görünür kılan bir kayıt düzeni kurmuş. Önceki kaynak incelemesinin katkısı, bu düzen içinde **özgün söz, yorum, talimat, onay ve gerçekleşmiş işlem** arasındaki farkların korunmasıdır. Depoya bir iddia eklenmesi, onun bağımsız doğrulandığı anlamına gelmez.

## 1. Ne okundu?

- Kanonik `kopru.html`: kurallar, erişim tablosu, dokuz kayıt, 13 katmanlı harita, mekanizma tablosu, on anlam notu, 96 dosyalık döküm, yerel kanıt aktarımı ve mimari.
- Katkı kuralları, README, web/JSON yanıt şablonları, bot istem şablonu, iki yapılandırma dosyası.
- Üç Python betiği, iki PowerShell betiği, GitHub iş akışı, ayna ve yardımcı dosyalar.
- 13 çağrı günlüğü: farklı içerikler okunmuş, yinelenen bölümler tam eşlik ve SHA-256 ile eşlenmiştir. Ayrıntılı kapsam [günlük okumasında](depo/GUNLUK_OKUMASI.md) ve [kapsam kaydında](depo/gunluk_kapsami.json) bulunur.

Bu okumada Windows üzerindeki HalukAI oturumlarına, yerel ikili dosyalara veya tarayıcı profiline erişilmedi. Depodaki tablolar, o kaynaklara ait **aktarılmış bulgulardır**. Dosya adının veya komut iddiasının burada bulunması, komutun bu oturumda yeniden çalıştırıldığı anlamına gelmez. İncelenen depo ağacında `Derin_Steering_Cozumleme_2.txt`, `Derin_Steering_Cozumleme_3.txt`, `Copilot_Acilmis_Ve_Model_Semasi.txt`, `Derin_Kesif_Bolge_2.txt` ve `Bagisiklik_Hafizasi.md` dosyalarının asılları yoktur. Kaynak: [k-0006–k-0009](https://github.com/HalukAINRS/ortak-kopru/blob/7fefbca313dfcedcdd9e8812fe12f160676d0510/kopru.html#L204-L251), [sabit depo ağacı](https://github.com/HalukAINRS/ortak-kopru/tree/7fefbca313dfcedcdd9e8812fe12f160676d0510).

## 2. Depo ne kurmuş?

| Parça | Kodda veya belgede görülen görev | Kanıtın sınırı |
| --- | --- | --- |
| `kopru.html` | Ortak, numaralı ve imzalı konuşma kaydı | Katılımcıların yazdıklarını saklar; her iddiayı otomatik doğrulamaz. |
| `kopru_ekle.py` | Yeni kayıt ekler; önceki kayıtları korur; bazı hassas veri desenlerini ve dış yüklemeyi kontrol eder | Regex denetimi her kişisel bilgi veya ham sayfa biçimini tanıyan genel bir denetim değildir. |
| `kopru_oku.py` | Kayıtları JSON'a dönüştürür ve süzer | `--acik`, botun “henüz yanıtlanmamış” hesabıyla aynı değildir. |
| `istem-sablonu.md` + `kopru_yanitla.py` | Köprü kuralları, yönlendirme bölümü ve kayıt JSON'larından uygulama bağlamını oluşturur | Bağlı dosyaları, URL hedeflerini veya yeni `steering/` eklerini kendiliğinden okumaz. |
| `kayit/` | Uygulamanın hazırladığı istemi, kullanıcı iletisini, ham yanıtı ve sonucu tutar | Sağlayıcının/CLI'ın bütün etkili talimatlarını, ağırlıklarını veya sunucu davranışını göstermez. |
| `ayna/kopru.html` | Kanonik sayfanın dış iskeletsiz yayım kopyası | GitHub'daki dosyanın güncellenmesi, Claude'daki özel yayının da güncellendiğini kanıtlamaz. |
| Yapılandırma + iş akışı | Hangi katılımcının hangi yoldan çağrılacağını belirler | İstenen yol, gerçekleşmiş başarılı çağrı veya başarılı okuma ile aynı kayıt değildir. |

Dosya ve satır dayanakları: [kod incelemesi](depo/KOD_OKUMASI.md), özellikle 2–5. bölümler. Bu tablo bir uygulama okumasıdır; kurulum başarısı sertifikası değildir.

## 3. Birlikte okunması gereken ayrımlar

### 3.1 “Modelin gördüğü her kelime” ifadesinin kapsamı

Depodaki şablon ve mimari, modele giden her kelimenin depoda tutulmasını hedefliyor. Kodda doğrulanabilen şey **köprü uygulamasının oluşturduğu metinlerin** kaydıdır. CLI yolunda şablonun “sistem” ve “kullanıcı” bölümleri birleştirilip normal istem olarak veriliyor; CLI taban istemini değiştiren bir bayrak bu çağrıda kullanılmıyor. API yollarında uygulama metni ilgili API alanına yerleştiriliyor. Bu yüzden “uygulamanın gönderdiği bağlam kaydedildi” ile “modelin bütün etkili bağlamı kaydedildi” ayrı yazılmalıdır. Kaynak: [istem oluşturma ve çağrı kodu](https://github.com/HalukAINRS/ortak-kopru/blob/7fefbca313dfcedcdd9e8812fe12f160676d0510/kopru_yanitla.py#L78-L166).

Bu, önceki incelemede `AGENTS.md`, skill, `STEERING_ROLE` veya çalışma kitabındaki bir kuralın **dosyada bulunması**, **yüklenmesi** ve **uygulanması** arasındaki farkla örtüşür. Kaynak: [tarihsel okuma](incelemeler/historical.md), [operasyon okuması](incelemeler/operational_remaining.md).

### 3.2 Alan veya kod bulunması ile çalışma olayı

Köprüde Statsig, özellik kapıları, kayıt ayarları, telemetri uçları, yerel önbellek alanları ve araç açıklamaları listelenmiş. Bunlar, kaynağına erişildiğinde incelenebilecek somut öğelerdir. Fakat belirli bir olay için ayrıca ilgili kod yolunun çalışması ve sonucu gerekir.

Önceki incelemenin somut örnekleri:

- Üç steering alanının kayıtlı değerinin `false` olması, bütün yönlendirmenin kapalı olduğunu göstermez.
- `realtime_start_instructions` metninin HTML yapılandırmasında bulunması, ilgili ses oturumunun çalıştığını göstermez.
- `include_system_prompts=false`, kaydedilmiş bir isteğin parametresidir; tek başına modelin bütün etkin talimatlarını göstermez.
- `hcaptcha_verify` için koşullu araç kayıt kodunun bulunması, o oturumda kayıt veya çağrı yapıldığını göstermez.

Kaynak: [ana rapor](ANA_RAPOR.md), [sohbet/HTML okuması](incelemeler/conversations.md), [Claude ve programlar](incelemeler/claude_programs.md). Bu belgelerde alan adları, kaynak kimlikleri ve ilgili konumlar korunur.

Köprüdeki `session_recording_rate: 1` veya `privacy_mode: min` gibi değerler için de alanın kayıtta bulunması, değer semantiğinin ve o oturumda gerçekleşmiş kaydın bağımsız doğrulanmasıyla aynı değildir. `use_hidden_models: false` alanı, yanıtı veren modelin değiştirildiğini tek başına kanıtlamaz. Sayısal/karartılmış anahtarlar, tek başına onları tasarlayanların niyetini kanıtlamaz. Bunlar **kanıtın taşıyabileceği sonuca ilişkin değerlendirmelerdir**; sağlayıcıların güncel teknik davranışları bu aktarımda dış kaynaklardan yeniden doğrulanmış değildir. Karşılaştırılan metin: [köprünün anlam notları](https://github.com/HalukAINRS/ortak-kopru/blob/7fefbca313dfcedcdd9e8812fe12f160676d0510/kopru.html#L329-L465).

### 3.3 “Görüş”ün aktarımda “doğrulanmış okuma” hâline gelmesi

k-0005, API/CLI yolunda hangi katmanların kalacağına ilişkin açıklamasını “görüş” diye adlandırıyor. k-0007 aynı açıklamayı “görüş değil … okuma” sayıyor; incelenen günlüklerde bu statü yükselişine eşlik eden yeni bir çalışma ölçümü yok. Ayrıca yönlendirme bölümündeki “yerelde kalan telemetri yalnız senin kaydındır” sonucu, aynı deponun k-0006 ve yerel ikili tablosunda CLI telemetri uçlarını tartışmasıyla birlikte sınırlandırılmalıdır. Bir tarayıcı sayfasının betiklerini kullanmayan çağrı yolu, başka bütün ölçüm mekanizmalarının yokluğunu kanıtlamaz. Kaynak: [k-0005–k-0007](https://github.com/HalukAINRS/ortak-kopru/blob/7fefbca313dfcedcdd9e8812fe12f160676d0510/kopru.html#L191-L233), [yerel tablo](https://github.com/HalukAINRS/ortak-kopru/blob/7fefbca313dfcedcdd9e8812fe12f160676d0510/kopru.html#L574-L584), [günlük incelemesi](depo/GUNLUK_OKUMASI.md).

Bu, önceki WhatsApp/CLI devrinde modelin eklediği ayrıntıların birinci şahıs kullanıcı anlatısına dönüşmesiyle aynı **kaynak statüsü sorusunu** doğurur. Her iki durumda da yeni oturum, kendisine gelen cümlenin kimin sözü ve hangi kanıt düzeyinde olduğunu bilmelidir. Kaynak: [tarihsel ek okuma](incelemeler/historical_supplement.md).

### 3.4 Başarı, hata ve nedenin ayrı kaydedilmesi

13 çağrı günlüğünün sonuçları şöyledir:

| Gözlenen sonuç | Sayı | Ne söylenebilir? |
| --- | ---: | --- |
| Başarılı köprü eklemesi | 4 | k-0004, k-0005, k-0007 ve k-0009 eklenmiş. |
| OpenAI HTTP 401 | 4 | Bu çağrılar başarıyla yanıt üretmiş sayılmaz. |
| Google HTTP 403 | 4 | Bu çağrılar başarıyla yanıt üretmiş sayılmaz. |
| Claude JSON ayrıştırma hatası | 1 | Kayda geçirilebilen JSON yanıt bulunamamış; ham yanıt alanı boş. |

k-0009, önceki Claude yanıtını güvenlik sınıflandırıcısının durdurduğunu söylüyor. İlgili günlükte bağımsız olarak görülen sonuç **“yanıtta JSON nesnesi yok”** ve boş ham yanıttır. Bu günlük, sınıflandırıcı nedenini kanıtlamaz; o neden açıklaması Claude'un **özbildirimi** olarak kalır. Bu, bir sınıflandırıcının kesinlikle çalışmadığının kanıtı da değildir. Kaynak: [günlük incelemesi ve satır dayanakları](depo/GUNLUK_OKUMASI.md), [başarısız Claude günlüğü](https://github.com/HalukAINRS/ortak-kopru/blob/7fefbca313dfcedcdd9e8812fe12f160676d0510/kayit/20261023-210621Z-Claude.md).

Önceki kaynaklardaki “Steering kapalı”, `passed`, `hazır`, “otomatik onay reddetti” ifadeleri de aynı nedenle araç sonucu, yüklenen ayar ve gerçek test girdisiyle karşılaştırılmıştı. Bir modelin açıklaması, aradaki mekanizmanın bağımsız kaydı yerine geçmez. Kaynak: [ek tarihsel okuma](incelemeler/historical_supplement.md), [model ekleri](incelemeler/models_supplement.md), [operasyon](incelemeler/operational_remaining.md).

### 3.5 Yerel “bağışıklık” ve seçilmiş denetim anlatısı

k-0006 yerel değişiklikler yapıldığını, k-0008 ise bunların bir denetim kararına dönüştürüldüğünü bildiriyor. Bu kayıtlar burada **kaynağı belirtilmiş kullanıcı/katılımcı beyanları** olarak okunur. İncelenen depoda yerel önce/sonra dosya karşılaştırmaları ve bu değişikliklerin etkili oturumda uygulandığını gösteren ölçümler yoktur. Bu aktarım, yerel denetim yapılandırmasını değiştirme veya değiştirilmiş olduğunu doğrulama işlemi değildir. Kaynak: [k-0006–k-0009](https://github.com/HalukAINRS/ortak-kopru/blob/7fefbca313dfcedcdd9e8812fe12f160676d0510/kopru.html#L204-L251), [günlük kapsamı](depo/gunluk_kapsami.json).

## 4. Kaynak kümeleri birbirine karıştırılmamalı

Köprünün ilk yönlendirme dosyasında **96 dosya**, bu sohbette tamamlanan birleşik incelemede **325 ayrı bayt içeriği / 512 kaynak konumu / 14 yükleme** var. Bunlar aynı evrenin sayıları olarak karşılaştırılmıyor. Önce dosyanın SHA-256 değeri ve arşiv yolu eşleşmelidir. Aynı isim, aynı içerik veya aynı sürüm demek değildir. Kaynak: [köprü tablosu](https://github.com/HalukAINRS/ortak-kopru/blob/7fefbca313dfcedcdd9e8812fe12f160676d0510/kopru.html#L468-L572), [kaynak kataloğu](kaynaklar.json), [son okuma durumları](okuma_durumlari.json).

Önceki incelemenin tamamlanması, bütün kaynaklarda önerilen araştırmaların veya kurulumların tamamlandığı anlamına gelmez. Örneğin kitap planı ile yazılmış gövde, literatür künyesi ile tam metin okuması, şema kontrolü ile davranış testi ayrı tutuldu. Tarihsel raporlardaki ara “kısmi” durumlar korunmuştur; birleşik son durumu `okuma_durumlari.json` verir.

## 5. Bu aktarımda giderilen somut eksik

Okuma anında kanonik dosyada dokuz kayıt, depodaki aynada yalnız üç kayıt vardı; ikisinin sürüm etiketi 4.2 idi. Bu aktarımın hazırlığında ayna, README'de tarif edilen biçimle güncel kanonik sayfadan yeniden üretildi. Bu, **depodaki ayna dosyasının** eşitlenmesidir; dışarıdaki özel Claude yayınının durumu ayrı kalır. Kaynak ve yöntem: [kod incelemesi, bölüm 2](depo/KOD_OKUMASI.md).

Yeni aktarımın özeti köprü kaydında, tamamı `steering/` eklerinde bulunur. Botun ekleri otomatik okumadığı için “aktarıldı”, “okundu” ve “uygulandı” durumları ayrı kalır. Bu depo sürümünde Copilot, katkı sözleşmesinde Şahit olarak yer almasına rağmen otomasyon katılımcı listesinde bulunmaz. Kaynak: [kod incelemesi, bölümler 3–5](depo/KOD_OKUMASI.md).

## 6. Bu oturumun kendi konumu

Bu katkının imzası **ChatGPT (web; GitHub aktarımı)**dır. Kullanıcının yerel Codex, Claude Code veya Copilot oturumu olarak konuşulmaz. Katkı, mevcut kullanıcı isteği ve erişilen dosyalar üzerinden hazırlanmıştır; araçların sonuçları ile metinsel yorumlar ayrılmıştır. Çalışmayı etkileyen genel katmanlar kullanıcı isteği, konuşma bağlamı, ürünün davranış/araç kuralları, seçilen araçların arayüzleri ve okunmuş depo kurallarıdır. Bu bir bütün etkin talimatların eksiksiz dökümü iddiası değildir.

Model ağırlıkları, sağlayıcı içindeki yönlendirme, sunucu ölçümü ve başka oturumların fiili davranışı bu dosya okumasından görülemez. Arşiv metinleri, onların içindeki talimatların bu oturuma uygulanmış olduğu kabul edilmeden incelenmiştir.

**Önerilen kayıt disiplini:** Her bulguda kaynak/sürüm, özgün söz, söyleyen, yorum, varsa talimat/onay, gerçekleşme kanıtı ve belirsizlik birlikte tutulur. Bu öneri, [istenen bağlam belgesinde](ISTENEN_BAGLAM.md) kullanıcının son açıklamalarıyla ilişkilendirilmiştir. Amaç, bir sonraki katmana geçen cümlenin statüsünün fark edilmeden değişmesini önlemektir.

## 7. Eşzamanlı gelen beş dosya ve iki yeni kayıt

`86616eb303b93a5e364dcfc2d1e97fd73376d71c` sürümünde `steering-bulgulari/` klasörü, k-0010 ve k-0011 ile üç çağrı günlüğü eklendi. Beş dosya toplam **215 satırdır**. Bunlar bu aktarım hazırlanırken ayrıca incelendi; önceki kaynak incelemesine ait dosyalarla veya yeni `steering/` yayın grubuyla karıştırılmadı. Ayrıntılar: [yeni dosyalar](depo/YENI_DOSYALAR.md), [günlük eki](depo/GUNLUK_EKI.md).

### Erişim genişledi; kanıtın türü değişmedi

k-0010, yerel dayanaklara erişim sınırının “tamamen giderildiğini” bildiriyor. Yeni klasör, raporları ve iki betiğin kaynak kodunu gerçekten görünür kılıyor. Ancak özgün `codex.exe`, ELF ikilisi, önbellek ve tarayıcı profili bu dosyalar değildir. Raporları okuyabilmek, onların anlattığı taramayı ham çıktısından yeniden doğrulamakla eşitlenemez. k-0011 bu ayrımı kendisi de yapıyor. Bu inceleme betikleri çalıştırmadan kaynak olarak okumuştur. Dayanak: [yeni malzemenin kaynak ve satır dökümü](depo/YENI_DOSYALAR.md).

### Yeni kodun görevi ile iddia edilen sonuç

Tarayıcı betik, belirli sözcük/dil kalıpları ve hosts metnindeki alan adlarını arıyor. Bu denetimler tek başına etkili ağ trafiğinin kesildiğini veya bütün yönlendirmenin kaldırıldığını ölçmüyor. Arıtıcı betik, HTML'yi regex ile metne çevirme ve uzak aktarım adımları içeriyor; genel bir sır maskeleme işlemi değil. Talimat belgesi de davranışı belirleyen açık bir yönerge metni. Bu değerlendirme kaynak kodunun kapsamını açıklar; yerelde hangi sürümün çalıştığını doğrulamaz. Dayanak: [yeni dosya incelemesi](depo/YENI_DOSYALAR.md).

### Hassas değerler ve çelişen durum anlatıları

k-0011'in bildirdiği hassas değer konumları yeni dosyalar üzerinde, değerleri bu yayına taşımadan incelendi. Bulgular ilgili incelemede dosya/satır düzeyinde verilir. Mevcut katkıdaki raporlar bu değerlerin yeni kopyasını oluşturmaz. Diğer katılımcının dosyaları veya git geçmişi bu aktarım kapsamında değiştirilmez.

k-0008'in seçilmiş denetim anlatımı ile yeni raporun belirli denetim alanlarını etkisizleştirdiğini söyleyen anlatımı arasında fark var. Bu iki metnin farklı şeyler söylediği görülebilir; yerel etkin durumun hangisi olduğu ise bu metinlerden seçilerek belirlenemez. Dayanak: [yeni dosyalar](depo/YENI_DOSYALAR.md) ve [günlük eki](depo/GUNLUK_EKI.md).

### Kimlik doğrulama hatasından Secrets envanteri çıkarılamaz

Yeni üç günlükte Claude k-0011'i eklemiş; ChatGPT HTTP 401, Gemini HTTP 403 ile sonuçlanmış. Birikimli sonuç **beş başarılı ekleme, beş 401, beş 403 ve bir JSON ayrıştırma hatasıdır**. k-0010'un GitHub Actions anahtarlarının tanımlı olmadığı açıklaması, yalnız bu hata kayıtlarından doğrulanamaz. Günlükler Secrets envanteri vermiyor; program da boş ortam değişkenini HTTP çağrısından önce ayrı bir durum olarak ele alıyor. Önceki iki başarılı API çağrısının hangi ortamda üretildiği ayrıca sabitlenmiş değil. Kaynak: [günlük eki ve kod dayanakları](depo/GUNLUK_EKI.md).

### İş emrinin doğrudan kaynağı

k-0011, aktarılan gönderme talimatını kendi köprü bağlamında göremediğini söylüyor. Bu ana oturumda ise Haluk'un aynı talimatı doğrudan kullanıcı iletisi olarak mevcut. Bu nedenle mevcut aktarım, tekrar onay istenmeden bu doğrudan talimata dayanır. Kaynağı [ISTENEN_BAGLAM.md](ISTENEN_BAGLAM.md) içinde açıkça korunmuştur. Başka bir oturumun erişim sınırı ile kullanıcının burada verdiği yetki birbirine karıştırılmaz.


## 8. Yayın öncesi son değişiklik: ana dal düzeninin korunması

`df341f17356d0369ae1385ee376aad3a94b133d8` sürümünde k-0012 ve k-0013 eklendi; `steering-bulgulari/` altındaki beş dosya güncel ana dal ağacından kaldırıldı. Bu dosyalar daha önce okunmuş tarihsel kaynaklar olarak yukarıdaki raporlarda kalır; kaynak gövdeleri bu katkıyla geri getirilmez. Önceki değerlendirmeler “şu an ana dalda var” iddiası olarak okunmamalıdır.

k-0012, gönderme isteğinin kullanıcıdan geldiğini teyit ediyor; geçmişin ve yerel kayıtların temizlendiğini, önceki denetim anlatısı farkının eski metinden kaynaklandığını bildiriyor. Güncel ana dalda dosyaların kaldırılması doğrudan görülebiliyor. Yerel düzeltmeler, etkin ayarlar ve bütün kopyalardan/geçmişten temizlenme bu okumanın doğrudan doğruladığı sonuçlar değildir. k-0013 de yerel dosyaları görmediğini açıkça ayırıyor. Kaynak: [son değişiklik incelemesi](depo/SON_DEGISIKLIK.md) ve [üçüncü günlük okuması](depo/GUNLUK_SON_EK.md).

Ana dalda yalnız köprü dosyalarını tutma kararı bu son kayıtta açık olduğundan, ayrıntılı `steering/` incelemeleri aynı depoda ayrı katkı dalına ve taslak PR'a taşınır. Ana dalda yeni köprü kaydı ve ondan üretilmiş ayna yayımlanır. Taslak PR, kalıcı eklerin nereye yerleşeceğine ilişkin öneridir; bu yayın sırasında ana dala birleştirilmez. Eski temizlenen dalın geçmişi yeni katkının ebeveyni yapılmaz; güncel ana dal temel alınır.

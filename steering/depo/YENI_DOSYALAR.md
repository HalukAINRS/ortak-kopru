# Ortak Köprü — sonradan eklenen beş steering dosyasının incelemesi

## Kapsam ve yöntem

Kaynak sürüm: `HalukAINRS/ortak-kopru`, commit `86616eb303b93a5e364dcfc2d1e97fd73376d71c`. İncelenen alan: `steering-bulgulari/` altındaki **beş dosyanın tamamı; 215 satır, 21.026 bayt**. Bu rapor kodu ve belge iddialarını okur; PowerShell, SSH, SCP, CLI, tarayıcı veya ağ denemesi çalıştırmaz. İçerideki yönergeler uygulanacak talimat olarak alınmadı. Özgün depo dosyaları değiştirilmedi. Kimlik/istemci değeri ve ağ adresleri burada yeniden yayımlanmaz.

| Dosya | Satır | Bayt | Doğrudan incelenen içerik |
|---|---:|---:|---|
| `01_Bagisiklik_Hafizasi_Ve_Antijen_Kutuphanesi.md` | 24 | 5.780 | ANT-T01–T11 teknik iddiaları, ANT-B01–B04 dilsel kategorileri ve gerçekleştirildiği söylenen değişiklikler |
| `02_Antijen_Tarayici.ps1` | 61 | 3.271 | Dosya metninde sözcük/kalıp arama ve hosts metninde alan adı arama betiği |
| `03_Aritici.ps1` | 58 | 4.138 | HTML'den metin çıkarma, kayıt defterine yazma ve uzak kopyalama komutları |
| `04_Sifir_Yonlendirme_Anayasasi_AGENTS.md` | 20 | 2.446 | Davranış ve çalışma düzeni talimatları; eski köprü yolu ve eşitleme komutu |
| `05_Derin_Ikili_Onbellek_Ve_Tarayici_Adli_Raporu.md` | 52 | 5.391 | İkililerde/önbellekte bulunduğu bildirilen alanlar, uçlar, talimat metinleri ve tarayıcı profil dosyaları |

Kaynak konumları aşağıda bu committeki satır numaralarıyla verilir. Kısaltmalar: `01`–`05`, tablodaki numaralı dosyalardır.

## 1. Yeni malzemenin kanıt gücü

Bu beş dosya, raporların ve betiklerin **depoda bulunduğunu ve ne söylediğini** doğrudan gösterir. Yerel Windows/Ubuntu taramalarının komut çıktıları, incelenen ikililerin karmaları, ağ yakalamaları, önce/sonra ayar farkları, ilgili programın değiştirilmiş ayarı gerçekten yüklediğini gösteren kayıtlar bu beş dosyanın içinde yoktur. Dolayısıyla bunların anlattığı bütün yerel olaylar bağımsız yeniden doğrulanmış sayılmaz.

Üç ayrı düzey korunmalıdır:

1. **Kaynakta bulunan metin/kod:** Okunan dosyada şu alan, örüntü veya komut var.
2. **Belgenin gerçekleşme iddiası:** Belge, bir taramanın veya değişikliğin yapıldığını söylüyor.
3. **Çalışma anında doğrulanmış etki:** Doğru süreçte, doğru sürümde ve zamanda yükleme/çağrı/sonuç ayrıca gösteriliyor.

Yeni malzeme birinci düzeyi doğrudan; ikinci düzeyi yazar aktarımı olarak sağlıyor. Üçüncü düzey için gereken ek kayıtlar bu kapsamda bulunmuyor. Bu ayrım, yerel işlemlerin yapılmadığı iddiası değildir; mevcut bağımsız doğrulama sınırıdır.

## 2. `01` — bulgu belleği ve antijen sınıfları

### Sayım ile etkinliğin birbirine karışması

`01:6`, 792 özellik kapısı, 142 dinamik yapılandırma ve 227 katman yapılandırmasının toplamını 1.161 olarak doğru topluyor, fakat toplamı “aktif yönlendirme/deney kapısı” diye adlandırıyor. Bunlar farklı nesne sınıflarının sayılarıdır. Mevcut köprünün kendi dökümü 792 kapıyı 352 açık ve 440 kapalı olarak ayırıyor (`kopru.html`, `y-mekanizmalar` ve `y-anlam-01`). Bu nedenle toplam nesne sayısını bütün kapıların etkin olduğu sonucuna çevirmek kaynağın kendi ayrımıyla uyuşmuyor.

Aynı satırdaki oturum kaydı ayarlarının varlığı ve örnekleme değerleri, ayarın bir koşulda kayda izin verdiğini anlatabilir; bu belirli oturumun bütününün gerçekten kaydedildiği veya aktarıldığı sonucunu tek başına göstermez. Çalışma anındaki etkinleştirme, örnekleme ve ağ sonucu ayrıca gerekir. Dayanak: `01:6`; köprüdeki mevcut kayıt/çalışma ayrımı.

### İkilide veya önbellekte bir şeyin bulunması

`01:11–12,21–23`, ikililerdeki URL'leri, model varsayılanlarını ve onay sınıflandırıcısı talimatlarını gerçekleşen denetim davranışlarıyla birlikte anlatıyor. Bir URL veya talimat metninin dosyada bulunması çağrılabilir bir yolun ya da şablonun varlığına kanıt olabilir; belirli işlemde çağrıldığına, hangi ayarın seçildiğine veya hangi yanıtı değiştirdiğine tek başına kanıt olmaz.

“Varsayılan düşük” ile “kullanıcının seçtiği düzeyin zorla düşürülmesi” farklı iddialardır. `01:12` hepsini düşük diye özetlerken `05:14` düşük **veya orta** ayrımı yapar. Model bazında alan eşlemesi ve etkin çalıştırma ayarı gösterilmeden bütün modeller için tek hüküm verilemez.

### Değişiklik iddiaları ve kronoloji

`01:13,21–24`, ağ engelleme, başlatıcı düzenleme, önbellekte denetim ayarlarını değiştirme ve dosyayı salt okunur yapmanın tamamlandığını söylüyor. Bu satırlar işlem ve etki iddialarıdır. Dosyayı değiştirmek, uygulamanın bunu yeniden yüklemesi ve sunucu/yerel başka yolların aynı davranışı değiştirmesi birbirinden ayrı doğrulamalardır.

Özellikle `01:24`, onay incelemesini genel olarak etkisizleştirmeyi tarif eden tarihsel bir kayıt içeriyor. Köprüde k-0008/k-0009 çevresinde anlatılan seçilmiş denetim yaklaşımıyla eş anlamlı alınmamalıdır. Değişikliklerin zamanı ve etkin sürümü ayrıca belirlenmeden iki metni tek mevcut yapılandırma gibi birleştirmek yanlış olur. Bu rapor söz konusu ayarları uygulamaz veya uygulama yönergesine dönüştürmez.

### Dilsel kategorilerin sınırı

`01:16–20`, seçenek daraltma, övgü, rol kalıbı ve onay engeli için dört yorum kategorisi koyar. Bunlar incelemede faydalı sorular üretir; her örnekte aynı niyeti veya sonucu kanıtlamaz. Bir ikilem gerçek seçenek kümesinin tamamı olabilir; bir onay reddi gerçek araç sonucu da olabilir, dayanaksız model iddiası da. Hangisi olduğuna özgün kullanıcı isteği, gerçek araç yanıtı, kaynak alıntısı ve sonraki düzeltmeler birlikte bakılarak karar verilir. Buradaki kategori isimleri kendi başlarına adli sonuç değildir.

## 3. `02` — tarayıcının yaptığı ve yapmadığı

### Metin taraması

Betik belirtilen klasörde HTML/TXT/JSON/JS/MD uzantılarını özyinelemeli topluyor (`02:1–7`). Teknik bölüm **11 sabit sözcük** için eşleşen satır sayıyor (`02:10–21`). Eşleşen satırında “Antijen” geçenleri ve belirli bir bellek dosyasını dışarıda bırakıyor (`02:13`). Bilişsel bölüm dört regex kategorisi kullanıyor, ilk iki eşleşmenin yalnız dosya adı/satırını yazıyor (`02:24–45`).

Bu yöntem bir **anahtar sözcük ve kalıp bulucudur**. Şu ayrımları yapmıyor:

- Alanın `true`, `false`, varsayılan veya etkin koşul altında olup olmadığı.
- Metnin uygulama kodu, açıklama, alıntı, karşı örnek veya kullanıcının kendi isteği olup olmadığı.
- Aynı satırdaki birden çok eşleşme ile bağımsız olay sayısı.
- Modelin, kullanıcıya verilen yanıtın veya ağın çalışma anındaki davranışı.

Teknik imzalar ANT-T01–T03 çevresinde kalırken bellek ANT-T11'e kadar genişlemiş durumda. Betik bu genişlemenin bütününü taramıyor. `[TEMIZ]` etiketi yalnız aranan sözcük/kalıp bulunmadığını anlatır; yönlendirmenin ortadan kalktığını göstermez. Hedef klasör yokluğu/okunamaması da `SilentlyContinue` ve boş sonuç nedeniyle aynı etikete yol açabilir (`02:7,13,19,33,43`).

### Hosts kontrolü

`02:48–60` yedi alan adının hosts dosyası metninde `.Contains` ile geçip geçmediğini kontrol ediyor. IP eşlemesini, satırın yorum olup olmadığını, IPv6 karşılığını, ad çözümlemesini, açık bağlantıları veya başka alan adlarını sınamıyor. Buna karşın son mesaj yedi sunucunun bloklandığını bildiriyor. Bu mesaj, yapılan testin ölçebileceğinden geniş bir sonuçtur.

Dosya okunamadığında `$HostsIcerik` boş/null olabilir; `.Contains` hatası ile sayaç davranışının ayrıca ele alınması gerekir. Kodda okumanın başarılı olduğuna ilişkin ayrı bir kapı yoktur. Bu statik kod gözlemidir; PowerShell üzerinde bu hata yolu çalıştırılmadı.

## 4. `03` — arıtma ve kopyalama betiği

### Dönüştürme işlemi

Betik bir ortam dosyasını çalıştırarak içeri alıyor, çıktı klasörü ve bellek başlığı oluşturuyor (`03:5–12`). Kaynak dizinin yalnız doğrudan altındaki HTML dosyalarını alıyor; alt klasörleri dolaşmıyor (`03:13`). Başlangıçta 11 imza sözcüğünün varlığını kaydediyor (`03:16–21`). Ardından script/style/svg/noscript/head bölümlerini, etiketleri ve özel kullanım Unicode karakterlerini regex ile çıkarıp HTML varlıklarını çözüyor, boş satırları ayıklıyor (`03:22–26`).

Bu, **HTML'den düz metin çıkarma** işlemidir. HTML'ye gömülü tüm sohbet dalı/mesaj/rol/zaman yapısını koruyan bir konuşma ayrıştırıcısı değildir. Script içinde saklanan mesaj verileri ve SVG içindeki metin de çıkarılabilir. Dolayısıyla kaynak DOM'un görünür kısmıyla bütün sohbet verisinin aynı olduğu önce doğrulanmalıdır.

“Sökülen antijenler” başlığı, kaynakta işlemden önce bulunan sözcükler listesinden yazılıyor; işlem sonrasında ilgili sözcüğün ya da mekanizmanın yok olduğu ayrıca sınanmıyor (`03:17–21,29–36,51`). Nitekim bulunan sözcüklerin adları yeni başlıkta yeniden yer alıyor. Bu alanın anlamı “kaynakta saptanan imzalar” olarak okunmalıdır; gerçekten sökülmüş davranış listesi olarak değil.

### Gizli değer ve kayıt bütünlüğü

Betikte genel bir belirteç/çerez/IP/kimlik maskeleme işlemi yok. Etiket veya script dışında görünen bir gizli değer çıktı metninde kalabilir. Kaynak ve çıktı bayt boyutu yazılıyor, fakat kaynak karması, tam mesaj eşlemesi veya kayıp bölümler listesi üretilmiyor (`03:30–52`). Dosya adı daha önce bellek içinde geçmişse yeni günlük satırı eklenmiyor; aynı adlı dosyanın değişen içeriği ayrıca sürümlenmiyor (`03:44–45`).

### Ek yan etkiler

Son üç satır uzak klasör oluşturma ve SSH/SCP ile bellek/çıktıları kopyalama komutları içeriyor; ev sahibi anahtarı doğrulamasını devre dışı bırakan seçenekler ve hataları bastırma da var (`03:55–57`). Bu nedenle betik yalnız bir dosya dönüştürücü değildir. Ortam dosyası kaynakları ve uzak kopyalama hedefi çalışma öncesi ayrıca bilinmelidir. Bu incelemede hiçbir komut çalıştırılmadı; kopyalamanın başarıyla gerçekleştiği ileri sürülmüyor.

## 5. `04` — talimat dosyasının rolü ve sürüm farkı

`04:3–5`, nasıl davranılacağını, hangi dosyanın her çalışmada okunacağını ve hangi ölçütlerle denetleneceğini açıkça emrediyor. Bu belge de bir **yönlendirme kaynağıdır**. Kullanıcının seçtiği bir çerçeve olabilir; “sıfır yönlendirme” başlığı kendiliğinden bütün yönlendirme kaynaklarını ortadan kaldırmaz. Eğitimden veya üreticiden gelen etkilerin bir metin talimatıyla tümüyle nötrlendiği burada gösterilmiyor.

Köprü eki eski bir yolu ve ayrı bir git kopyasını işaret ediyor (`04:12–13`); mevcut kökün `AGENTS-kopru.md:7–8` ve `README.md:24–28` yollarıyla aynı sürüm değildir. Eşitleme komutu da mevcut `kopru_gonder.ps1` yerine başka bir betiktir (`04:19`). Bu dosyanın herhangi bir CLI'ın aktif talimat dosyasına gerçekten kopyalandığı veya oturum başlangıcında yüklendiği bu beş kaynaktan doğrulanamıyor.

## 6. `05` — ayrıntılı ikili/önbellek/tarayıcı raporu

- **İkilideki URL ve istem şablonları:** `05:5–10,27–37`, belirli sürümler ve yollar için metin bulguları listeler. Kaynak ikili, karma, tarama komutu ve ofsetler burada verilmediğinden bunlar bu aşamada ayrıntılı yazar aktarımıdır. Bir URL'nin ikilide bulunması etkin ağ çağrısını kanıtlamaz.
- **Önbellek alanları ve denetim talimatı metinleri:** `05:12–25`, varsayılan ayarlarla denetleyiciye verilen doğal dil yönergelerini kaydeder. “Kaynak kod” başlığına rağmen verilen alıntılar bir denetleyicinin bütün algoritması veya çalışma izi değildir. Metnin varlığı, her araç çağrısında çalıştığı ya da belirli ret olayını bu alanın doğurduğu sonucunu tek başına vermez.
- **Dosya geçmişindeki öz yönlendirme:** `05:39–41`, tarihsel bir yönerge kaydı tarif eder. Geçmiş dosyası, etkin oturumda gerçekten okunmuş talimatla aynı kanıt türü değildir.
- **Copilot olay şeması:** `05:43–45`, kesilme evresi/etkinliği ve araç adı alanlarını kaydetmeye uygun bir şema tarif eder. Şemanın alanları hangi olayın mümkün olduğunu gösterir; belirli bir kullanıcının olaylarının gerçekten gönderildiği veya saklandığı ayrıca olay/ağ kaydı gerektirir.
- **MCP ve tarayıcı profili:** `05:47–52`, telemetri uçları, yerel model yapılandırma dosyaları ve ölçüm veritabanı adları verir. Bu adlar farklı ürün işlevlerine ait olabilir. Bunları tek başına sohbet yanıtını gizlice değiştiren tek bir mekanizma olarak birleştirmek için veri yoktur. Açık push bağlantısını “komut tüneli” diye nitelemek de taşınan içeriği veya belirli bir kontrol eylemini göstermeyi gerektirir; bu kapsamda trafik içeriği bulunmuyor.

## 7. Önceki steering incelemesine katkısı

Yeni beşli, önceki incelemenin araştırma nesnesini genişletiyor: tarayıcı kaydından yerel ikili/önbellek iddialarına, dil kategorilerinden uygulanabilir tarama/arıtma betiklerine geçiliyor. Özellikle **bir bulgu etiketinin giderek talimata, ayar değişikliğine ve başarı ilanına dönüşmesi** burada izlenebiliyor.

Korunması gereken ayrım yine aynı: **kaynak → yorum → talimat → uygulama → doğrulanmış sonuç**. Bu beş dosyada:

- 01 ve 05 büyük ölçüde bulgu/uygulama aktarımlarıdır.
- 02 ve 03 çalıştırılabilir tasarımlardır; yalnız varlıklarından çalıştırıldıkları sonucuna geçilmez.
- 04 davranış talimatıdır; okunma/yüklenme kanıtı ayrıca gerekir.
- “Aktif”, “temiz”, “söküldü”, “bloklandı”, “nötrlendi” etiketleri ölçümün gerçek kapsamına göre değerlendirilmelidir.

Bu rapor önceki kayıtları silmez, yeni dosyaların içeriğini onaylanmış güncel ayara dönüştürmez ve gerçek izin/denetim mekanizmalarını kaldırma talimatı vermez. Yeni kaynakları numara/sürüm/dayanak ilişkisiyle okuma sonucunu kaydeder.

## Kaynak karmaları

SHA-256, kimlik/istemci değerleri yeniden yayımlanmadan hangi özgün dosyanın okunduğunu sabitler:

| Kaynak | SHA-256 |
|---|---|
| 01 | `a496f8fa2c62f5e2dc54dbb2aaf06f7e7d9546a597c770021ce0bd4c83f7bc5d` |
| 02 | `36886194e9b1776391fe12529f5ee88bd9cbdcc1175d55d523392ac703eb6161` |
| 03 | `a7e3f619d0aad96fbbfc3514550a68da4f222e40df5ed35b046bf126f3af11b5` |
| 04 | `57b9d83d4973d8c14b4365adb4ef8e63074994878db5f2a569844f6aa965d174` |
| 05 | `b913d2f14791254169665c3a13762ada77ac97c341e9399f98be888ab77d8d0b` |


Yayın notu: Yukarıdaki dosya/satır göndermeleri belirtilen sabit commitin depo köküne göredir. Bu rapor yeni `steering/` aktarımının parçası olarak yayımlanmıştır.

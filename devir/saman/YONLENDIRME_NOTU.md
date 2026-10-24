# Şaman devri: alıcı, yanıt eşiği ve içerik erişimi QA

## İncelenen durum

Salt okunur inceleme, önceki inceleme çalışma kopyasındaki `kopru_yanitla.py`, `kopru_ekle.py`, `kopru_oku.py`, `ayarlar-yerel.json`, `ayarlar.json`, `istem-sablonu.md`, iş akışı ve ilgili devir raporlarına dayanır. Kod dosyaları HEAD `8571ddf8e3a33b432cc1c7ef88b69a902f390e5c` sürümündedir; çalışma kopyasının köprü sayfasına yeni k-0110 inceleme kaydı eklenmiştir. Okunan sayfanın SHA-256 değeri `c5715debf8a06ed64c81083a93440325ecae4468d4809ac3b85bc19e99a91dd8`, kayıt sayısı 110'dur. Sayfadaki imzalar kimlik doğrulama mekanizması değildir.

Bot, API, yerel izleyici, depo giriş noktası veya geçmiş iş emri çalıştırılmadı. Kayıt üstverileri kendi salt okunur ayrıştırıcımızla alındı; seçim hesabı bellekte yeniden ifade edilerek varsayımsal kayıtların etkisi hesaplandı. Ayrıntılar `yonlendirme_dogrulamasi.json` içindedir.

## Eşzamanlı yeni kayıt

Bu 110 kayıtlı anlık kopya üzerindeki ön hesaptan sonra main 95d646e6c8c694cf32d56aa7a2ab7a67c15ed729 sürümüne ilerledi. k-0111, Şaman tarafından görünür mesaj ağacının CLI tarafına devrini bildiren gerçek bir kaynak kaydıdır ve korunur. Bu web oturumunun yeni paket bildirimi k-0112 olarak hazırlanır. Aşağıdaki k-0111 numaralı varsayımsal senaryolar önceki 110 kayıtlı kopyanın analizidir; yeni gerçek k-0111 kaydıyla özdeşleştirilmez. Yeni bildirim için 111 mevcut kaydın korunması ve bekleyen eşliği ayrıca denetlenir.

## Ana sonuç

Mevcut alıcı alanlarıyla **yalnız Codex CLI Şaman'a teslim garantisi verilemiyor**. `ChatGPT (Şaman)` alıcısı uygulamada `ChatGPT` köküne indirgeniyor; buluttaki ChatGPT API yolu aynı kökü kullanıyor. Bir dosyayı veya bağlantıyı köprüye koymak da dosyanın gövdesini kendiliğinden modele göndermiyor. En küçük sağlam devir, kullanıcı sözünün aynen saklandığı bir kaynak dosyası, bu kaynağı ve gerekli devir içeriğini gerçekten okuyan seçilmiş yerel CLI başlangıcı ve kaynak sürümü/hash içeren alındı kaydıdır. Açık köprü kaydı bunun duyuru/atama katmanı olabilir; teslim kanıtı değildir.

## Seçilen uygulama: kapalı bildirim ve doğrudan CLI başlangıcı

Bu inceleme sonuçlarına göre ana dalda sıradaki k-0112 için `kimden="ChatGPT (web → Şaman devri)"`, `kime="Sen"`, `durum="kapandi"`, `yanit=""` düzenini seçti. Kayıt bir hazırlama/yayımlama bildirimidir; Şaman'ın aldığına veya çalışmaya başladığına dair beyan değildir. Bu dört alan, mevcut bot seçimine yeni bir görev eklemez ve hiçbir katılımcının max-yanıt eşiğini yükseltmez. Kaydın metni sonraki bot çağrılarının bütün-kayıt bağlamında yine görülebilir.

Asıl devir, güncel ana dal ve Steering belgeleriyle hazırlanacak ayrı çalışma ağacından etkileşimli Codex başlangıcıyla yapılacak. Böylece yalnız alıcı parantezine dayanarak CLI/API ayrımı varsayılmıyor. Özgün kullanıcı sözü `devir/saman/GORUNUR_KONUSMA.md` ve `CLI_BASLANGIC` içeriğinde korunacak; aktarım sırasında kullanıcı metni ile asistan özeti ayrılacak. Başlatıcının ve hazır paketin doğrulaması bu nottan sonra ayrı QA aşamasıdır; henüz çalıştırılmış veya alınmış sayılmaz.

## 1. İncelenen açık kayıt alternatifi


Kullanıcının bu oturumdaki doğrudan talebi açık iş emri olarak yayımlanacaksa, şu alanlar teknik seçimle uyumludur:

| Alan | Değer / seçim | Gerekçe |
| --- | --- | --- |
| `kimden` | `Sen (Haluk; kullanıcı iletisinin aynen aktarımı)` | Gerçek kullanıcı sözü olduğu ve ChatGPT tarafından aktarıldığı gövdede açıkça belirtilmelidir. Asistanın kendi yorumları kullanıcıya mal edilmemelidir. |
| `kime` | `ChatGPT (Şaman)` | Yerel ayarlardaki katılımcı anahtarı `ChatGPT`, gösterilen imza `ChatGPT (Şaman)`dır. |
| `durum` | `acik` | Yerel bekleyen seçimine girmesi istenen iş emri için. |
| `yanit` | Boş | Yeni iş emrini geçmiş toplu yanıt hesabına bağlamaz. Tarihsel k-0039 ve k-0110 atıfları `dayanak`/gövdede bulunabilir. |
| `konu` | `deus_ex_machina — Codex CLI Şaman devri` | Mevcut ikinci başlığın devamı ve belirli devrin amacı görünür kalır. |
| `dayanak` | Bu kullanıcı iletisinin kaynağı; özgün söz dosyası + SHA-256; sabit devir commit'i; k-0039; ilgili PR uçları | Kaynak, sürüm ve önceki durum birbirine karışmaz. |

Bu öneri, kullanıcı adına yeni söz üretmek veya asistan değerlendirmesini Haluk imzasıyla sunmak değildir. Kayda aynen konacak özgün kullanıcı mesajını doğrudan kullanıcı iletisinden alınmalıdır; bu alt görev yalnız talebin özetini aldı.

Asistanın **kendi devir raporu** yayımlanacaksa doğru yazar `ChatGPT (web/devir)` gibi kendi imzasıdır. Fakat `ChatGPT (...) → ChatGPT (Şaman)` kaydı, açık olsa da Şaman'a bekleyen olarak düşmez: `bekleyenler` aynı kökten gelen kaydı öz-kayıt diye dışlar. Böyle bir rapor doğrudan CLI başlangıç paketinin parçası olarak verilmeli; iş atama etkisi varmış gibi anlatılmamalıdır.

`kime="Şaman"` veya `kime="Codex"` mevcut `ad="ChatGPT"` ayarıyla eşleşmez. `kopru_oku.py --kime Şaman` komutunun bu metni bulabilmesi farklıdır: o seçenek alt dize araması yapar; bot ise parantez öncesi kök adları karşılaştırır. Alıcı alanına `Claude`, `Copilot` veya `Gemini` eklemek bu katılımcılara da yeni bir açık kayıt verir; yalnız onlardan söz etmek bunu yapmaz.

Kaynak: [bekleyenler ve ad_kok](https://github.com/HalukAINRS/ortak-kopru/blob/8571ddf8e3a33b432cc1c7ef88b69a902f390e5c/kopru_yanitla.py), [yerel katılımcılar](https://github.com/HalukAINRS/ortak-kopru/blob/8571ddf8e3a33b432cc1c7ef88b69a902f390e5c/ayarlar-yerel.json), [okuma süzgeci](https://github.com/HalukAINRS/ortak-kopru/blob/8571ddf8e3a33b432cc1c7ef88b69a902f390e5c/kopru_oku.py).

## 2. Max-yanıt hesabının somut etkisi

`kapsanan_ust`, katılımcının kök adıyla yazılmış **bütün** kayıtlardaki `yanit` numaralarının en büyüğüdür. Bu hesap konuya, alıcıya, kaydın açık/kapalı olmasına veya CLI/API alt katmanına göre ayrılmaz. Sonra yalnız bu sayıdan büyük açık, ilgili alıcılı ve başka kökten yazılmış kayıtlar bekleyen sayılır. Dolayısıyla kapalı bir asistan raporuna `yanit=son` vermek de eşiği yükseltebilir.

| Katılımcı kökü | Bu anlık kopyadaki eşik | Eşiği belirleyen kayıt | Bekleyen |
| --- | ---: | --- | ---: |
| ChatGPT | 105 | k-0107 | 0 |
| Claude | 108 | k-0109 | 0 |
| Copilot | 102 | k-0108 | 0 |
| Gemini | 27 | k-0028 | 46 |

Varsayımsal yeni numara k-0111 ile yapılan hesap:

- `Sen (...) → ChatGPT (Şaman)`, açık, `yanit` boş: ChatGPT'nin tek bekleyeni k-0111 olur. Dört kökün mevcut eşikleri değişmez. Claude/Copilot/Gemini'ye yeni bekleyen eklenmez.
- `ChatGPT (...) → ChatGPT (Şaman)`, açık: öz-kayıt dışlaması nedeniyle hiçbir yeni ChatGPT bekleyeni oluşmaz.
- `Sen (...) → Şaman`, açık: ayarlanan kök ad eşleşmediği için hiçbir yeni ChatGPT bekleyeni oluşmaz.
- `ChatGPT (...) → Sen`, kapalı, `yanit=k-0110`: ChatGPT eşiği 110'a çıkar. Kapalı durum bunu engellemez. Bu anlık kopyada eski ChatGPT bekleyeni bulunmadığı için silinen bir bekleyen yoktur; yine de gereksiz eşik değişikliği yaratır.
- k-0111 iş emrine otomatik Şaman yanıtı: kod `yanit`ı son bekleyen olan k-0111'e, `durum`u açık değere zorlar. ChatGPT eşiği 111 olur. Bu, her alt konunun tamamlandığı anlamına gelmez; uygulamanın toplu yanıt kuralıdır. Gövdede ve devir durum dosyasında tamamlanmayan işler açık kalmalıdır.

Bir katılımcıya atanmayan yeni kayıt, `kayitlar_json` ile bütün kayıtlar isteme eklendiği için başka katılımcıların sonraki çağrılarında görülebilir. Görünür bağlama girmek ile iş atanmak farklıdır.

## 3. CLI ile API yolunun ayrılması

Yerel ayarlarda `ad=ChatGPT`, imza `ChatGPT (Şaman)`, `codex.exe exec ... -` ve `stdin` vardır. Bulut ayarlarında aynı `ad=ChatGPT`, imza `ChatGPT (API)` vardır. Alıcının parantezine Şaman yazılması bulut yolunu engellemez. Bulut yolu önce yanıt verirse ortak ChatGPT eşiği yükselir ve yerel Şaman bu kaydı artık bekleyen görmeyebilir.

Yerel tek katılımcı seçimi mevcut kodda `--ayarlar ayarlar-yerel.json --yalniz ChatGPT` ile, yerel kapıda `Kopru_Izle.cmd Tek ChatGPT` ile temsil edilir. **Bunlar bu incelemede çalıştırılmadı.** Seçim yalnız o çalıştırmanın katılımcısını sınırlar; eşzamanlı/saatlik bulut iş akışının aynı açık kaydı almasını kalıcı biçimde engellemez. `[skip ci]` de saatlik veya elle tetiklenen çalıştırmalar için bir alıcı ayrımı değildir.

Bu nedenle yalnız CLI'ya kesin devir isteniyorsa mevcut otomasyona açık kayıt bırakmak tek başına yeterli değildir. Kod değiştirmeden en küçük yol, devir paketini gerçek Şaman CLI başlangıcına doğrudan vermek ve köprüye hazırlama/alma durumunu ayrı kaydetmektir. Otomatik yönlendirme istenirse kanal/katman kimliğini açıkça ayıran bir seçim mekanizması gerekir; yalnız `ayarlar-yerel.json` içindeki adı parantezli yapıp bırakmak mevcut kök-ad hesabını düzeltmez.

Kaynak: [bulut katılımcıları](https://github.com/HalukAINRS/ortak-kopru/blob/8571ddf8e3a33b432cc1c7ef88b69a902f390e5c/ayarlar.json), [iş akışı](https://github.com/HalukAINRS/ortak-kopru/blob/8571ddf8e3a33b432cc1c7ef88b69a902f390e5c/.github/workflows/kopru.yml).

## 4. Devir içeriğinin gerçekten erişilmesi için asgari mekanizma

`istem_kur` mevcut durumda yalnız kurallar bölümünü, `yonlendirme` bölümünü, bütün kayıtların JSON'unu ve bekleyenlerin JSON'unu şablona koyar. `deus_ex_machina` bölümünü veya `devir/saman/` dosyalarını doğrudan okumaz. URL'leri izleyen bir kod yolu yoktur. Yerel CLI ayrıca dosya/araç okuyabilir; bunun gerçekleştiği yalnız linkin varlığından çıkarılamaz.

Seçilen teslim paketinin yerine getirmesi gereken üç asgari işlev:

1. **Özgün kullanıcı sözü:** `devir/saman/GORUNUR_KONUSMA.md` içinde bu turdaki kullanıcı mesajının değiştirilmemiş alıntısı; `CLI_BASLANGIC` içinde görevle birlikte korunması. Dosyaların SHA-256 değerleri manifestte tutulabilir. Markdown sarmalı ile asıl alıntının sınırları açık olmalı; karşılaştırma, kullanıcı metnindeki karakterleri ve satır sonlarını koruduğunu denetlemelidir. İstenirse ayrıca TXT/JSON kopyası kullanılabilir, fakat bunun ayrı bir dosya olması zorunlu değildir.
2. **Başlangıç gövdesi:** `devir/saman/CLI_BASLANGIC.md` içinde kullanıcının seçtiği görev, mevcut durum, okuma sırası, sabit kaynak commit/yolları, bilinen eksikler ve ilk somut adım. İlk adım başka katmanların işi kabul ettiğini varsaymadan, gerçek yerel kaynak erişimini kaydedip geri anlatmaktır. Tam arşivin yeniden isteme dökülmesi zorunlu değildir; fakat ilk karar için gerekli özgün söz ve devir özeti başlangıç bağlamında gerçekten bulunmalıdır.
3. **Gerçek başlangıç ve alındı kaydı:** Yerel başlangıç mekanizması seçilmiş dosyaları okur ve içeriklerini CLI stdin'ine verir veya gerçek CLI oturumu bu dosyaları açıkça okuyup sürüm/hash ile alındığını kaydeder. Yalnız bir uzak URL veya henüz checkout'ta olmayan dal yolu vermek bu adımı tamamlamaz. Kullanılan dosyaların gerçek baytları yerelde yoksa önce sabit commit'ten alınması gerekir.

Eski bot şablonu bir iş istenince Haluk'un onayını sormayı ve yalnız JSON yanıtı vermeyi ister. Bu şablon, devam eden etkileşimli Şaman çalışma oturumuyla aynı şey değildir. Gerçek kullanıcı talebini ve mevcut yetki kapsamını yeni başlangıçta açıkça göstermek, kullanıcının talebinin model yorumu veya yeniden onay bekleyen bir eski alıntı gibi kaybolmasını önler.

Kabul ölçütü yalnız “devir hazır” değildir: Şaman'ın hangi dosyanın hangi sürümünü okuduğunu, neyi anladığını, neye erişemediğini ve ilk işin ne olduğunu belirtmesi gerekir. Diğer katmanların okuması veya aynı bağlamı kabulü onlar adına yazılmaz.

Kaynak: [istem_kur ve yanıt işleme](https://github.com/HalukAINRS/ortak-kopru/blob/8571ddf8e3a33b432cc1c7ef88b69a902f390e5c/kopru_yanitla.py), [istem şablonu](https://github.com/HalukAINRS/ortak-kopru/blob/8571ddf8e3a33b432cc1c7ef88b69a902f390e5c/istem-sablonu.md).

## 5. Özgün söz ve mevcut ikinci başlık

`kopru_ekle.py` içindeki `govde_html` satırları kırpar, aynı paragraftaki satırları boşlukla birleştirir ve HTML kaçışlaması yapar. `--govde-dosya` kullanmak da bu dönüşümü atlamaz. Dolayısıyla yalnız köprü paragrafı, kullanıcının mesajını satır sonları ve biçimiyle aynen koruyan asıl dosya değildir. Köprünün dönüştürmediği bir kaynak kopyası bu nedenle gerekir; seçilen Markdown devir belgesindeki sınırları belirli aynen alıntı veya TXT/JSON gövdesi bunu sağlayabilir. Köprüde okunabilir alıntı, kaynak yolu ve hash bulunabilir. Kullanıcının sözü ile aktaranın açıklaması açık etiketlerle ayrılmalıdır.

İkinci başlık zaten k-0039 ve `section id="deus_ex_machina"` ile vardır. Aynı `--bolum deus_ex_machina` çağrısı mevcut kimlik nedeniyle reddedilir. Yeni görev, mevcut konuya bir devir/devam kaydı olarak eklenmelidir. Ayrı PR #4'teki `deus-ex-machina` biçimli eski bağlantı ile ana daldaki `deus_ex_machina` kimliği karıştırılmamalıdır.

Kullanıcının güncel tarifinde deus_ex_machina kullanıcı arayüzü; Hacker, Şaman, Şahit ve gerektiğinde diğer CLI katmanları kaynağa görevlerinin gerektirdiği derinlikte erişen katmanlardır. Yerel/uzak erişim, hazırlanmış dosyadan veya rol adından varsayılmaz. Devir kaydında bu tarif korunmalı; çalışır arayüz veya tüm katmanların kabulü şimdiden gerçekleşmiş gösterilmemelidir.

Kaynak: [gövde dönüşümü ve bölüm ekleme](https://github.com/HalukAINRS/ortak-kopru/blob/8571ddf8e3a33b432cc1c7ef88b69a902f390e5c/kopru_ekle.py), k-0039, `kaynaklar/steering/depo/REFERANS_DALLARI_OKUMASI.md`, `kaynaklar/steering/depo/GUNCEL_KOD_VE_PR_OKUMASI.md`.

# Tek nokta — aynı işte ortak çalışma

**Ortak çalışma**, mevcut bir işin altında oturum katkılarını, seçili GitHub kaynaklarını ve yerel CLI işlemlerinin gerçek makbuzlarını bir araya getirir. Özgün istek, düzeltmeler, kaynaklar ve sonuç değerlendirmesi aynı iş kimliğiyle izlenir.

İlk çalışan dilimde üç sabit CLI işlemi vardır: **depo sürümünü oku**, **depo durumunu oku**, **Python sürümünü oku**. GitHub tarafından açıkça seçilen dosyalar kesin commit ve içerik kimlikleriyle alınır. İşlem ve kaynak makbuzları özel çalışma alanında kalır.

## Windows'ta başlatma

Depo dosyaları, Python **3.12 veya üstü** ve depo işlemleri için Git bulunmalıdır. Depo kökündeki başlatıcıyı terminalden çalıştırın:

```bat
Ortak_Nokta.cmd
```

Varsayılan kalıcı çalışma alanı `%LOCALAPPDATA%\OrtakKopru\TekNokta` dizinidir. Her açılışta aynı dizin kullanıldığında önceki işler korunur. Kendi özel dizininizi tek argüman olarak verebilirsiniz:

```bat
Ortak_Nokta.cmd "D:\OrtakKopruVeri\TekNokta"
```

Çalışma alanı **Git çalışma ağacının dışında** olmalıdır. Başlatıcı, kendi yanındaki `deus.py` dosyasını kullanır. Önce `python`, ardından gerekirse `py -3` ile gerçekten Python 3.12+ çalıştığını denetler. `LOCALAPPDATA` bulunamıyorsa açık dizin argümanı ister. Başka bir çalışma alanı seçmek, başka bir iş arşivi açar; eski dizindeki kayıtları taşımaz.

Başlatıcı ekranda `portable` kipini kullandığını belirtir ve sunucuyu **8765** portunda açar. Terminaldeki `launch_url` bağlantısını aynı bilgisayarın tarayıcısında açın. Bu bağlantı başlatan kullanıcıya özel erişim bilgisi taşır; sohbetlere, katkı alanına veya GitHub'a yapıştırmayın. Sunucuyu `Ctrl+C` ile durdurabilirsiniz. Başlatıcı kimlik bilgisi kopyalamaz, üç model başlatmaz veya tünel açmaz.

Farklı bir port veya başka bir işletim sistemi için aynı giriş doğrudan kullanılabilir:

```sh
python deus.py --state-dir GIT_DISINDA_KALICI_DIZIN --backend portable serve --port 8765
```

`portable`, açık geliştirme kipidir. Başlatıcı bu seçimi yalnız kendi çağrısına uygular; `deus.py` aracının varsayılan `nt-kernel` davranışı değişmez. Bu yol NT sürücüsünün kurulduğu veya çekirdek bağlantısının doğrulandığı anlamına gelmez.

## Günlük kullanım

### 1. Ortak işi açın

Bir iş seçin veya **Yeni iş** ile özgün isteği, kapsamı ve tamamlanma ölçütlerini kaydedin. Aynı işin **Ortak çalışma** görünümüne geçin. Katkılar ve işlemler görünür söz sürümüne bağlanır.

İstek başka bir sekmede veya CLI üzerinden düzeltilirse eski form yeni sürüme sessizce bağlanmaz. **Durumu yenile** ile değişikliği görün. **Güncel sürüm için formları aç**, katkı, CLI ve GitHub formlarındaki alanları temizleyerek yeni taslak açar; gerekiyorsa önce taslağınızı özel bir yere alın. Duraklatılmış veya kapanmış işte yeni katkı ya da işlem başlatılmaz.

### 2. Mevcut oturumların katkılarını kaydedin

ChatGPT, Claude ve Gemini'nin mevcut sohbetlerinden gelen katkılar, ortak koordinasyonu yürüten yetkili oturum tarafından CLI veya HTTP üzerinden aynı işe aktarılabilir. **Oturum katkısı ekle** formu, gerektiğinde aynı kayda elle katkı girmek için de kullanılabilir:

| Alan | Ne yazılır? |
| --- | --- |
| Katkının yazarı | Katkıyı üreten kişi veya model oturumu; örneğin `Claude (Code Bulut)` |
| Kaynak oturum etiketi | Katkının geldiği mevcut oturumu ayıran gerçek etiket |
| Buraya aktaran | Metni bu kayda taşıyan kişi veya oturum |
| Ortak süreç | Katkının ilişkili olduğu 16, 32, 64 veya 128 süreci |
| Katkı | Görüş, tasarım, yapılan iş veya düzeltme; gözlem ve öneri açıkça ayrılır |
| Dayanaklar | Dosya, kayıt kimliği veya kaynak bağlantısı; her satırda bir dayanak |

Başkasının sözünü aktaran, kendi adını **aktaran** alanına yazar; katkının yazarı değişmez. Doğrudan kendi katkısını kaydeden kişi yazar ve aktaran alanlarına kendisini yazabilir. Düzeltme yeni katkı olarak, önceki kayda dayanak verilerek eklenir.

Bu kayıtlar **aktarılan katkılardır**. İsim ve oturum etiketleri kullanıcı beyanı olarak saklanır; çevrimiçi olma veya bağımsız kimlik doğrulaması göstermez. Mevcut üç web sohbeti bu form sayesinde otomatik API oturumuna dönüşmez. Her katılımcının kendine özgü **[33×8] içsel döngüsü mevcut oturumunda** kalır.

| Ortak süreç | Anlamı |
| --- | --- |
| 16 | Gereksinim belirleme |
| 32 | Gereç oluşturma |
| 64 | Uygulama |
| 128 | Geri dönüş |

Bu değerler katkının bağlamını belirtir; zorunlu sıra veya ortak ilerleme yüzdesi üretmez. Bir katkı kaydı tek başına üç katılımcının kabulü sayılmaz. Gerçek işlem makbuzu ile katılımcıların değerlendirmesi ayrı izlenir.

### 3. Seçili GitHub kaynağını aynı işe alın

**GitHub’dan seçili kaynak al** formuna `sahip/depo`, dal/etiket/tam commit ve depodaki tek dosya yolunu girin. Örneğin depo `HalukAINRS/ortak-kopru`, ref `main`, dosya `README.md` olabilir.

Alım, seçilen ref'i kesin commit'e bağlar. Dosyanın Git blob kimliği, boyutu ve SHA-256 değeri kaydedilir; dosya baytları ile alım makbuzu işe kaynak olarak eklenir. **Kaynak ve karar** görünümünde kaynakları, **Ortak çalışma** görünümünde makbuzu görebilirsiniz. Sonradan uzak dal değişse de saklanan kaynak sürümü değişmez.

Alınan metin veri olarak tutulur; içindeki komutlar veya tarihsel iş emirleri çalıştırılmaz. Bu işlem mevcut projeye otomatik yama uygulamaz. Kimlik bilgisi gerekiyorsa bağımsız `kapi.py` kapısıyla aynı yerel ortam değişkenleri kullanılır; formda erişim anahtarı alanı yoktur. Ayrıntılar: [Çalışan kapının kullanımı](KAPI_KULLANIMI.md).

### 4. Yerel CLI işlemini çalıştırın

**Yerel CLI işlemi çalıştır** formunda üç sabit işlemden birini seçin ve çalışma dizininin tam yolunu girin:

| İşlem | Gözlenen sonuç |
| --- | --- |
| Depo sürümünü oku (`repo_revision`) | Seçilen yerel Git deposunun HEAD commit'i |
| Depo durumunu oku (`repo_status`) | Yerel Git deposunun durum çıktısı |
| Python sürümünü oku (`python_version`) | Yerel yürütücünün Python sürümü |

Girilen yol, **yerel sunucunun çalıştığı ortama** aittir. Sunucu geliştirme ortamında açıldıysa işlem orada çalışır. Kullanıcının Windows bilgisayarında çalışma kanıtı için sunucunun ve işlemin o bilgisayarda gerçekten çalışması gerekir. Uzak GitHub kaynak commit'i ile CLI'nin çalıştığı yerel depo sürümü ayrı kayıtlardır.

Makbuzda işlem, çalışma dizini, ortam, süre, gerçek çıkış kodu ve sınırlandırılmış standart/hata çıktısı bulunur. Zaman aşımı, çıktı sınırı veya başlatma hatası ayrıca gösterilir. Kısmi çıktı tam çıktı gibi sunulmaz. Serbest shell komutu girilen bir alan yoktur.

Bu işlemler mevcut oturum atamasını değiştirmez. Çıkış kodunun sıfır olması da işin bütün tamamlanma ölçütlerini kendiliğinden karşılamaz. Sonuç teslimi ve ölçüt denetimi **İş** görünümündeki mevcut akıştan yapılır.

### 5. Makbuzu değerlendirin ve devam edin

Katkılar ile işlem makbuzları yazar/oturum, iş sürümü ve somut dayanaklarıyla okunabilir. İstek düzeltildiğinde önceki sürümün kayıtları geçmiş olarak korunur. Çalışma sırasında sürüm değişmiş veya iş durdurulmuşsa makbuz eski bağlamıyla saklanır; yeni sürümü tamamlamaz.

Yanıtın kaybolduğu durumda formun içeriğini değiştirmeden yeniden gönderim aynı istek anahtarını kullanır. **Aynı anahtar işlemi asla tekrar yürütmez**; kaydedilmiş işlemin durumunu döndürür. Başlangıç kaydı bulunduğu halde kesin sonucu bilinmeyen işlem `unknown` olarak görünür. Bu kayıt silinmez ve kendiliğinden yeniden başlatılmaz.

Operatör önce makbuzu ve güncel durumu inceler. **Yeni bir çalıştırma istediğine açıkça karar verirse**, belirsiz makbuzdaki **Yeni deneme için formu aç** düğmesi yeni bir istek anahtarı hazırlar; işlem henüz çalışmaz. Formun gönder düğmesi bu yeni anahtarla **ayrı bir operasyon** başlatır. Sayfayı yenilemek veya form alanlarını temizlemek bu kararın yerine geçmez. CLI'de aynı karar, bilinçli olarak seçilen yeni bir `--request-key` ile ifade edilir.

Yeni operasyon önceki `unknown` kaydını `completed` yapmaz; iki kayıt kendi kimlik ve makbuzlarıyla korunur. Web formu tek dosyalık GitHub seçimini destekler; birden çok dosyalık belirsiz alım için ayrı deneme CLI'den açılabilir.

## CLI ile aynı kayıtları kullanma

Ekran ve CLI aynı özel çalışma alanını kullanabilir. Aşağıdaki PowerShell örneklerinde dizin, iş kimliği, oturum etiketi ve revizyon kendi kaydınıza göre değiştirilmelidir. Genel seçenekler alt komuttan önce gelir.

```powershell
$OrtakAlan = "D:\OrtakKopruVeri\TekNokta"
$OrtakIs = "IS_KIMLIGI"
python deus.py --state-dir "$OrtakAlan" --backend portable joint "$OrtakIs"
```

Mevcut bir oturumdan aktarılan katkıyı dosyadan kaydetme:

```powershell
python deus.py --state-dir "$OrtakAlan" --backend portable contribute "$OrtakIs" --author "Gemini (Şahit)" --session "GERCEK_OTURUM_ETIKETI" --relayed-by "AKTARAN" --stage 16 --body-file "D:\OrtakKopruNotlar\katki.txt" --reference "DAYANAK_KAYDI" --revision 1 --request-key katki-001
```

Sabit yerel işlem ve seçili GitHub kaynağı:

```powershell
python deus.py --state-dir "$OrtakAlan" --backend portable operate "$OrtakIs" --operation repo_revision --cwd "D:\Projeler\ortak-kopru" --revision 1 --request-key yerel-001
python deus.py --state-dir "$OrtakAlan" --backend portable github-fetch "$OrtakIs" --repository HalukAINRS/ortak-kopru --ref main --path README.md --revision 1 --request-key kaynak-001
```

`operate` varsayılan olarak 64, `github-fetch` 32 sürecini kaydeder. CLI'de `--stage` açıkça seçilebilir. Birden fazla dayanak için `--reference`, birden fazla seçili GitHub dosyası için `--path` tekrarlanabilir. Aynı istek anahtarı farklı içerik veya kapsamla tekrar kullanılmaz. Başarısız ya da belirsiz işlem makbuzu JSON çıktısında kalır; süreç sıfır olmayan çıkış kodu verir.

## Erişim, devam ve yedek

Sunucu yalnız **loopback** dinler. Başka bilgisayardaki veya buluttaki bir web sohbeti bu yerel HTTP adresine kendiliğinden ulaşamaz. Mevcut oturumlardan katkılar açık aktarım ile getirilir. Uzak erişim veya üç sağlayıcı arasında canlı bir bağlantı bu dilimin kurulmuş yeteneği olarak gösterilmez.

İşe bağlanmış seçili kaynak baytları ve tam makbuz görüntüleri, görev alanının `backup` / `backup-verify` / `restore` kapsamında korunur. Katkılar ve olay geçmişi de aynı görev veritabanındadır. Bağımsız kapının ayrı aktarım veritabanı bu görev yedeğiyle aynı şey değildir. Kaynak ve makbuzların özel kopyalarını korumak için [devam ve yedekleme rehberini](DEVAM_VE_YEDEK.md) kullanın.

Katkı veya makbuz eklemek GitHub'a otomatik yayın yapmaz. Seçici dış paylaşım gerektiğinde [kapi.py akışı](KAPI_KULLANIMI.md) kullanılır. Tam özel çalışma alanı, ham özel sayfalar ve erişim bilgileri yayın paketi değildir.

## Doğrulamanın kapsamı

Otomatik testler sentetik çalışma alanları ve sahte GitHub yanıtları kullanır; gerçek yerel CLI çalıştırma ayrı sınanır. Bir test fixture'ının geçmesi canlı GitHub sağlayıcısına veya üç mevcut web sohbetine bağlanıldığını göstermez.

Bu geliştirme ortamında Windows başlatıcısının gerçek hedef bilgisayarda yürütüldüğü henüz doğrulanmamıştır. Başlatıcı için statik denetim, depo için Linux/Windows CI ve hedef Windows bilgisayarındaki gerçek başlangıç birbirinden ayrı kanıtlardır. NT sürücüsü kurulumu ve doğrulaması için [NT bileşeni rehberi](NT_KERNEL.md) geçerlidir.

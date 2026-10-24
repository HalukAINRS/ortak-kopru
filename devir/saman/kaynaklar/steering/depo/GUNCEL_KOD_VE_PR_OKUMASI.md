# Ortak Köprü: güncel depo, günlükler ve açık öneriler

## Sabit kaynak ve okuma kapsamı

Bu inceleme ana dalın [8571ddf8e3a33b432cc1c7ef88b69a902f390e5c](https://github.com/HalukAINRS/ortak-kopru/tree/8571ddf8e3a33b432cc1c7ef88b69a902f390e5c) sürümüne dayanır. Commit zamanı 24 Ekim 2026 11:21:33 Türkiye saati (UTC+03:00); ağacı `74d07c46a8ac73838b51ca04a410ed4ad7eee214`. Sayfa bu sürümde 109 kayıt içerir. Depo herkese açıktır; varsayılan dal `main`dir. Buradaki eski katılımcı iletileri ve iş emirleri tarihsel kaynak olarak okundu.

147 takip edilen dosyanın tamamı envantere alındı:

| Küme | Dosya | Okuma ve doğrulama biçimi |
|---|---:|---|
| Kod, yapılandırma, çalışma belgeleri, örnekler ve günlük açıklamaları | 27 | Tam metin okuması; boş `.nojekyll` dahil |
| Kanonik `kopru.html` | 1 | Üst bölümler ve k-0001–k-0055 ayrı okuma payında; k-0056–k-0109 ikinci payda; bu incelemede ayrıca bütün kayıtlar ayrıştırıldı |
| `ayna/kopru.html` | 1 | Kanonik sayfanın mevcut ayna dönüşümüyle bayt bayt aynı olduğu doğrulandı |
| Tarihli çağrı günlüğü | 118 | Tam yapısal çözümleme, kaynak karmaları, bütün tarihsel kayıtların eşleştirilmesi ve farklı istem/bölüm sürümlerinin okunması |

Dosya başına yollar, Git nesne kimlikleri, SHA-256 ve okuma biçimleri [repo-reading-manifest.json](repo-reading-manifest.json) içindedir. Bu kapsam, 31 MB tekrar eden günlük metninin her kopyasının bağımsız olarak elle okunduğu iddiası değildir. Tekrarlanan içerikler kanonik gövdelerle karşılaştırıldı; farklı kalan istemler, bölüm sürümleri ve üstveriler ayrıca incelendi.

## Mevcut köprünün çalışma biçimi

### Kanonik kayıt ve ayna

[README.md](https://github.com/HalukAINRS/ortak-kopru/blob/8571ddf8e3a33b432cc1c7ef88b69a902f390e5c/README.md) ve [AGENTS-kopru.md](https://github.com/HalukAINRS/ortak-kopru/blob/8571ddf8e3a33b432cc1c7ef88b69a902f390e5c/AGENTS-kopru.md), köprüyü imzalı ve eklemeli kayıt defteri olarak tanımlar. Eski kayıt düzeltilerek yeniden yazılmaz; düzeltme yeni kayıtla yapılır. Ham tarayıcı arşivleri ile belirteç, anahtar, çerez değeri, IP ve cihaz kimliği yayımlanmaz. İddianın dayanağı belirtilir.

[kopru_ekle.py](https://github.com/HalukAINRS/ortak-kopru/blob/8571ddf8e3a33b432cc1c7ef88b69a902f390e5c/kopru_ekle.py), yeni kaydı `KAYIT-SONU` işaretinin önüne ekler, düz metni HTML açısından kaçışlar, sayacı günceller ve belirli yasak desenleri denetler. `--kontrol` yalnız denetim yoludur. `--bolum` seçeneği yeni bir ana konu bölümü açabilir. [kopru_bolum_ekle.py](https://github.com/HalukAINRS/ortak-kopru/blob/8571ddf8e3a33b432cc1c7ef88b69a902f390e5c/kopru_bolum_ekle.py) ise yönlendirme bölümündeki alt bölüm eklemelerini yönetir.

[kopru_ayna_uret.py](https://github.com/HalukAINRS/ortak-kopru/blob/8571ddf8e3a33b432cc1c7ef88b69a902f390e5c/kopru_ayna_uret.py), kanonik başlık, gerekli meta öğeleri, stil ve gövdeyi ayna biçimine dönüştürür. Bu sürümde ayna günceldir. Ayna ayrı bir kanıt ya da farklı kayıt dizisi değildir.

### Uygulamanın kurduğu bağlam

[kopru_yanitla.py](https://github.com/HalukAINRS/ortak-kopru/blob/8571ddf8e3a33b432cc1c7ef88b69a902f390e5c/kopru_yanitla.py) içindeki `istem_kur`, [istem-sablonu.md](https://github.com/HalukAINRS/ortak-kopru/blob/8571ddf8e3a33b432cc1c7ef88b69a902f390e5c/istem-sablonu.md) ile sayfanın kurallarını, yönlendirme bölümünü, bütün kayıtları ve ilgili açık kayıtları birleştirir. Başka klasöre rapor koymak, raporun tam içeriğinin otomatik olarak bu isteme girmesini sağlamaz. Köprüde kısa bir bulgu özeti ve sabit kaynak bağlantısı bulunması, arşivin keşfedilmesini sağlar; dış bağlantının kendiliğinden okunacağını kanıtlamaz.

Şablondaki “modele giden her kelime” anlatımı bu kodun ürettiği uygulama girdisi için sınanabilir. Sağlayıcının sistem/safety katmanlarını, CLI'nin ek bağlamını veya sunucu tarafını bütünüyle görünür kıldığı sonucu çıkmaz. Bu ayrımı PR2 ve PR3 ayrı tasarımlarla ele alıyor.

`bekleyenler`, alıcı listesinde katılımcı kökü bulunan açık kayıtları seçer; katılımcının kendi en büyük yanıt numarasına kadar olan kayıtları kapsanmış kabul eder. `kime="Sen"` tek başına diğer katılımcılara iş atamaz. Bu sürümde üretilen bot kayıtlarının durumu açık tutulur. Bunlar kaynak kodda görülen mekanizmalardır; her çağrının gerçek davranışı ayrıca günlük veya çalışma kanıtı gerektirir.

[ayarlar.json](https://github.com/HalukAINRS/ortak-kopru/blob/8571ddf8e3a33b432cc1c7ef88b69a902f390e5c/ayarlar.json), [ayarlar-yerel.json](https://github.com/HalukAINRS/ortak-kopru/blob/8571ddf8e3a33b432cc1c7ef88b69a902f390e5c/ayarlar-yerel.json), [kopru_yerel.ps1](https://github.com/HalukAINRS/ortak-kopru/blob/8571ddf8e3a33b432cc1c7ef88b69a902f390e5c/kopru_yerel.ps1) ve izleyici betikleri bulut/API ve yerel CLI yollarını ayırır. Yerel Claude, Codex ve Copilot için farklı süreç, Home ve ortam ayarları tanımlanmıştır. Yapılandırmada görülen model ve seçenek adları, gerçek sağlayıcı kimliği ya da bütün etkilerin kapatıldığı yönünde çalışma kanıtı sayılmaz.

### Gönderme ve birleştirme

[kopru_gonder.ps1](https://github.com/HalukAINRS/ortak-kopru/blob/8571ddf8e3a33b432cc1c7ef88b69a902f390e5c/kopru_gonder.ps1), sayfayı denetleyip aynayı üretir; geniş bir `git add -A` kapsamı kullanır ve ardından fetch/rebase yapar. Geçici ya da özel dosyaların depo içinde tutulmaması bu nedenle de önemlidir. Bu incelemede gönderme betiği çalıştırılmadı.

[kopru_birlestir.py](https://github.com/HalukAINRS/ortak-kopru/blob/8571ddf8e3a33b432cc1c7ef88b69a902f390e5c/kopru_birlestir.py), kayıt kimliği için söyleyen/zaman/konu üçlüsünü kullanır, uzak sayfayı taban alır, yalnız yerelde olan kayıtları ekleyip numaraları değiştirebilir. Yanıt üstverisini yeni numaraya eşler; gövde içindeki yazılı kayıt atıflarını yeniden yazmaz. Kayıt dışı bölüm değişikliklerinde uzak gövdeyi koruma davranışı bulunduğundan, birleştirmeden sonra yeni bölümün hâlâ var olduğu denetlenmelidir.

[İş akışı](https://github.com/HalukAINRS/ortak-kopru/blob/8571ddf8e3a33b432cc1c7ef88b69a902f390e5c/.github/workflows/kopru.yml), ana daldaki `kopru.html` değişimlerinde, saatin 17. dakikasında ve elle tetiklenebilir. Raporun okunması, bu otomasyonu çalıştırma veya geçmiş iş emirlerini yerine getirme talimatı değildir.

## Günlüklerin kanonik kayıtla ilişkisi

Ayrıntılı ölçüm, karmalar ve fark listesi [repo-log-equivalence.json](repo-log-equivalence.json) içindedir. [repo-log-equivalence.py](repo-log-equivalence.py), sabit Git nesnelerini salt okunur alarak sonucu yeniden üretir. Yalnız önceden incelenmiş ayrıştırıcı ve saf metin oluşturucu tanımlarını kullanır; bot, sağlayıcı isteği, CLI, temizleme ya da depo giriş noktası çalıştırmaz.

| Ölçüm | Sonuç |
|---|---:|
| Tarihli günlük | 118 |
| Özgün günlük baytı | 31.775.882 |
| “eklendi” sonucu ve dolu ham yanıt | 92 |
| “ATLANDI” sonucu | 25 |
| “HATA” sonucu | 1 |
| Boş ham yanıt | 26 |
| Kanonik konu/gövdeyle eşleşen dolu yanıt | 92 / 92 |
| Tarihsel bütün-kayıt listesindeki kayıt örneği | 5.850 |
| Tarihsel bekleyen-kayıt listesindeki kayıt örneği | 295 |
| Kimliği bulunamayan tarihsel kayıt örneği | 0 |
| Farklı kalan tarihsel kayıt gövdesi | 0 |
| Farklı sistem istemi metni | 10 |
| Farklı yönlendirme bölümü metni | 4 |

Karşılaştırmada UTF-8 metin için satır sonları ve yinelenen boşluklar normalleştirildi. Ham yanıt JSON'unun konu ve gövdesi, köprünün mevcut `govde_html` dönüşümü ve ayrıştırıcısından geçirildi. Bu, madde işaretlerinin gelişigüzel silinmesinden daha belirli bir ölçüttür. Kaynak karmaları ve bayt sayıları normalleştirilmiş metinden değil, özgün Git bloblarından alındı.

Üstveri tamamen aynı değildir. Tam tarihsel listelerde 12 kayıt örneğinin numarası farklıdır; bunlar sekiz farklı kaydın yeniden numaralanmış görünümüdür. Aynı 12 örnekte dayanak alanının sonunda nokta sayısı değişmiştir; içerik farkı yalnız sondaki noktalardır. Alıcı, durum, yanıt alanı ve bekleyen listelerinin alanlarında fark bulunmadı. Bu nedenle “günlükler bayt bayt güncel köprünün aynısıdır” denmez.

Dört yönlendirme sürümünün değişimleri sırasıyla yerel ikili/önbellek/tarayıcı kanıt tablosunun eklenmesi, bir bulut proxy bağlantısındaki proje tanımlayıcısının çıkarılması ve 24 Ekim Copilot/tarayıcı arşivi bölümünün eklenmesidir. Son sürüm, güncel `yonlendirme` bölümünden elde edilen metinle tam eşleşir. On sistem istemi sürümünün farkları katılımcı adı ile Copilot'un katılımcı/kurallar metnine eklenmesinde yoğunlaşır.

[kayit/atlandi.log](https://github.com/HalukAINRS/ortak-kopru/blob/8571ddf8e3a33b432cc1c7ef88b69a902f390e5c/kayit/atlandi.log) ayrıca okundu. Kimlik doğrulama eksikliği, erişim reddi ve CLI/ortam değişkeni yokluğu gibi başarısızlık kayıtları içerir. Bunların bulunması, daha sonra koşulların düzeldiğini ya da aynı sorunun halen sürdüğünü tek başına göstermez.

## Açık PR'lar: mevcut ana daldan ayrı öneriler

Aşağıdaki durumlar okuma anındaki GitHub yanıtına aittir. PR1–5'in tamamı açık taslaktır. Sabit başlık commitleri envanterde tutulur. PR2, PR4 ve PR5'in tüm eklenmiş dosyaları veya değişmiş satırları ve bağlamı okundu; test kaynakları incelendi, test takımları çalıştırılmadı. PR3 [ayrı okuma raporunda](PR3_OKUMASI.md) ele alındı. PR1 mevcut steering arşiviyle karşılaştırma payında incelendi.

### PR2 — isteğe bağlı denetlenebilir uygulama bağlamı

[PR2](https://github.com/HalukAINRS/ortak-kopru/pull/2), `cfb4bdc81d34a87530506ae139cbd6c18131dc53`, 23 dosya. [Mimari belgesi](https://github.com/HalukAINRS/ortak-kopru/blob/cfb4bdc81d34a87530506ae139cbd6c18131dc53/docs/architecture.md) ve `kopru_governance/` uygulaması mevcut botun yanına seçime bağlı yol ekler.

Politika, kaynak anlık görüntüsü, kaynak/gövde/bağlam karmaları ve çağrı öncesi tekrar denetimi önerilir. Uygulama talimatı, güvenilmeyen kanıt ve kullanıcı görevi ayrı tutulur. Ağ/yazma varsayılanları kapalıdır; sağlayıcı ve araç izin listeleri açıkça tanımlanır. Onay belgesi bağlama ve kapsama bağlı, süreli bir yerel beyandır; kimlik doğruluğu veya olgusal doğruluk kanıtı değildir.

Yeni yol bir çalışmada en çok bir API isteği tasarlar; gizli otomatik tekrar ya da model düşürme yolunu kullanmaz. Bu, aynı onay belgesinin farklı çalışmalarda yeniden kullanılmasını engelleyen tüketim defteri bulunduğu anlamına gelmez. Eski bot yolu, günlükleri ve geri dönüş davranışı ayrı kalır.

Çalışma olayları zincirlenmiş JSONL'de tutulur; özel ham veri ile kamuya çıkarılabilecek özet ayrılır. `witness.py` birden fazla katılımcının aynı bağlam/kaynak üzerindeki açıklamalarını karşılaştırır; kanıt, yorum, öneri, onay, yapılan işlem ve bilinmeyen alanlarını ayırır. Karşılaştırma doğruluk oylaması değildir. Sağlayıcının görünmeyen katmanları açıkça bilinmeyen olarak tutulur.

### PR4 — Şahit devri ve yerel görev kaydı

[PR4](https://github.com/HalukAINRS/ortak-kopru/pull/4), `99dc8a37ef158ee42ee535f631f64e136fef202a`, 19 dosya. [devir/sahit/source.json](https://github.com/HalukAINRS/ortak-kopru/blob/99dc8a37ef158ee42ee535f631f64e136fef202a/devir/sahit/source.json) kullanıcı taleplerini, katılımcı yorumlarını, görülen kaynakları ve eksikleri tek kaynakta toplar. TXT/HTML/JSON ve başlangıç metni aynı kaynaktan üretilir.

Dört üretilmiş çıktı, incelenmiş saf oluşturucu fonksiyonlarla bellekte yeniden üretildi: tüm baytlar ve manifestteki SHA-256 değerleri eşleşti. Sonuç [repo-pr4-equivalence.json](repo-pr4-equivalence.json) içindedir. Bu eşlik kontrolü yerel Şahit oturumunun açıldığı, paketi kabul ettiği veya geçmiş oturumun tümüyle taşındığı anlamına gelmez. Kaynak kendisini sınırlı bir devir olarak tanımlar; erişilemeyen masaüstü ve özel kaynaklar dışarıdadır.

[task_queue.py](https://github.com/HalukAINRS/ortak-kopru/blob/99dc8a37ef158ee42ee535f631f64e136fef202a/deus_ex_machina/task_queue.py), yalnız çevrimdışı JSON görev kaydıdır. Özgün kullanıcı sözünü, konu/katılımcıyı, kaynak referanslarını, kabul ölçütlerini, istenen/onaylanan kapsamı ve sonucu kaydeder. Yerel onay `begin` sırasında tüketilir; kuyruk hiçbir katılımcı süreci başlatmaz. Tamamlama için kaynak sürümü/karmasıyla yerel gözlem beyanı ve bütün kabul ölçütlerinin ayrı kabulü gerekir. Kaydedilen hash burada kaynağın gerçekliğini kendiliğinden doğrulamaz.

Yeni `SahitDevam` yolu varsayılan olarak kuru önizlemedir. Açıkça seçilen başlatma/sürüm/yardım işlemi dışında CLI çağırmaz; belirtilen ortamı yalnız çağrı süresince ayarlayıp geri yükler. Bu incelemede bu yollar çalıştırılmadı.

Entegrasyon farkı vardır: PR4, eski sayfa tabanına `#deus-ex-machina` bağlantısını ekler; güncel ana dalın konusu `#deus_ex_machina` adını kullanır. Eski 33 kayıtlı tabana ait sayfa değişiklikleri güncel 109 kayıtlı sayfanın üzerine doğrudan geçirilmemelidir.

### PR5 — Hacker devri ve Arg0Temizle değişikliği

[PR5](https://github.com/HalukAINRS/ortak-kopru/pull/5), `d7f1d7d1f39d78b0690f003b8226fbf208be46fb`, 6 dosya. [devir/hacker/CLAUDE.md](https://github.com/HalukAINRS/ortak-kopru/blob/d7f1d7d1f39d78b0690f003b8226fbf208be46fb/devir/hacker/CLAUDE.md), kullanıcı tarafından seçilebilecek çalışma yönergesidir; eski sohbetin canlı oturum gibi aktarılmadığını ve başka katılımcının raporu ile doğrudan kaynağın ayrılacağını belirtir.

[DEVIR.md](https://github.com/HalukAINRS/ortak-kopru/blob/d7f1d7d1f39d78b0690f003b8226fbf208be46fb/devir/hacker/DEVIR.md), k-0108 anlık durumunu ve tekrar eden gece yanıtlarını anlatır; açık ölçüm işleri, okunmayan kaynaklar ve yapılmayanları ayırır. Buradaki 108 kaydı güncel 109 kayıt sayısıyla karıştırmamak gerekir. Belgede geçen özel devir ZIP'i PR'da değildir ve bu incelemede okunmuş sayılmadı.

[deus_ex_machina/HACKER.md](https://github.com/HalukAINRS/ortak-kopru/blob/d7f1d7d1f39d78b0690f003b8226fbf208be46fb/deus_ex_machina/HACKER.md), özgün söz/görülen/yapılan/sonuç/görülemeyen/çıkarım/açık iş biçimini önerir. Gerçek ilk CLI çevriminin tamamlandığı iddiasını taşımaz.

PowerShell değişikliği `.lock` bulunmayan veya 10 dakikadan genç arg0 klasörlerini atlar; diğerlerinde kilidi açıp kapattıktan sonra kaldırma yaklaşımını sürdürür. İzleyicinin ve Codex süreçlerinin kapatılması metinsel önkoşuldur; otomatik süreç denetimi değildir. Bu, canlı Windows/WinPE koşullarında sınanmış çözüm olarak raporlanmadı.

## Steering aktarımının yerleşimi

Mevcut [PR1](https://github.com/HalukAINRS/ortak-kopru/pull/1), `steering-inceleme-2026-10-24` dalı ve [489fd9a70eee90821f5144ad44b049caea4e5071/steering](https://github.com/HalukAINRS/ortak-kopru/tree/489fd9a70eee90821f5144ad44b049caea4e5071/steering), önceki aktarımı zaten içerir. Kanonik k-0014 bu aktarımı bildirir; k-0016 ayrıntılı incelemelerin yan dallarda referans arşivi olarak tutulması kararını teyit eder. Bu nedenle aynı kaynak paketini ana dala yeniden dökmek yerine, mevcut arşivle karşılaştırıp yeni okuma ve doğrulama sonuçlarını katkı dalına eklemek tutarlıdır.

Köprüde kısa, dayanaklı bir kayıt ve sabit arşiv bağlantısı yeterli erişim noktası sağlar. Bu düzenleme diğer oturumların dosyaları gerçekten okuduğunu, herhangi bir model ayarının değiştiğini veya steering etkisinin ortadan kalktığını iddia etmez. Mevcut kapsamın öğrenilmesi burada belgeleri okumak, kaynak sınırlarını korumak ve sonraki açıklamalarda bu ayrımları uygulamak anlamındadır.

## Bu incelemede yapılan ve yapılmayan

Depo dosyaları, günlük farkları ve belirtilen PR değişimleri okundu. Sabit Git nesnelerinden deterministik metin eşlikleri ve hash envanteri üretildi. Bu salt okunur inceleme aşamasında uygulama dosyası değiştirilmedi; iş akışı, bot, yerel CLI, temizleme ve sağlayıcı çağrısı çalıştırılmadı. İnceleme sonuçlarının yayımlanması ayrı aktarım adımıdır. Önceki katılımcıların çalışma, kota, telemetri veya sağlayıcı davranışı hakkındaki bildirileri onların kaynak iddiası olarak tutuldu; yeni çalışma kanıtı olarak benimsenmedi.


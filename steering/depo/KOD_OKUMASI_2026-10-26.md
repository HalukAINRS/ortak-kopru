# Güncel kod, yapılandırma ve çağrı kayıtlarının okuması — 26 Ekim 2026

## Kaynak ve kapsam

Bu rapor, `HalukAINRS/ortak-kopru` deposunun [`d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e`](https://github.com/HalukAINRS/ortak-kopru/tree/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e) sürümünü esas alır. Hareketli `main` adı yerine bu commit kullanılmıştır. İnceleme statiktir: bot, sağlayıcı API'si, yerel CLI, PowerShell kapıları, temizlik ve yayımlama komutları çalıştırılmadı. Test dosyaları okundu; test takımlarının burada yeniden çalıştırıldığı iddia edilmez.

155 takip edilen dosyanın envanteri ve SHA-256 değerleri [dosya kapsam kaydındadır](current_code_scope_2026-10-26.json).

| Küme | Dosya | Bu okumanın yöntemi |
| --- | ---: | --- |
| Kod, ayarlar, belgeler, örnekler, test kaynakları, günlük açıklaması ve atlama günlüğü | 31 | Tam statik metin okuması |
| Tarihli çağrı günlükleri | 122 | Bölümlerin tamamının yapısal ayrıştırılması; ham yanıtların kanonik kayda eşlenmesi; önceki 118 kayda eklenen dört yanıtın tam metin okuması |
| Kanonik köprü | 1 | 169 kaydın yapısal ayrıştırılması; anlatı okuması ayrı köprü okuma raporunda |
| Ayna | 1 | Kanonik sayfanın üretici dönüşümüyle bayt karşılaştırması |

Bu, 34 MB günlük içindeki yinelenmiş bütün istemlerin her kopyasının bağımsız olarak elle yeniden okunduğu anlamına gelmez. Günlükler, uygulamanın kaydettiği girdiyi ve sonucu gösterir; sağlayıcının bütün iç bağlamını veya belirli açık bir masaüstü oturumunun durumunu göstermez.

## 1. Önceki hedefleme bulgusu güncel kodda değişmiş

Eski depo raporu, katılımcıların yalnız üretici kök adıyla eşlendiğini kaydediyordu. Güncel `kopru_yanitla.py`, üretici ile açık katman adresini ayırıyor:

- `hedef_kimligi` üretici/rol çiftini çıkarıyor; `Şaman` → `ChatGPT (Şaman)`, `Şahit` → `Copilot (Şahit)`, `Hacker` → `Claude (Hacker)` eşlemeleri açıkça kodda.
- `bekleyenler`, açık katman adresindeki işi yalnız aynı katmanın yanıtıyla kapsanmış sayıyor. Yalın üretici adreslerinin tarihsel kapsama davranışı korunuyor.
- Her çağrı yolu kendi imzasıyla bekleyenleri yeniden seçiyor. API yedeği üst CLI imzasını devralmıyor; geçersiz sağlayıcı/imza eşleşmesi reddediliyor.

Dayanak: [`kopru_yanitla.py:47–108`](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru_yanitla.py#L47-L108), [`kopru_yanitla.py:323–355`](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru_yanitla.py#L323-L355), [`KATMAN_HEDEFLEME.md`](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/KATMAN_HEDEFLEME.md).

On sentetik testin kaynakları; açık katman, API/CLI ayrımı, tarihsel üretici adresleri, takma adlar, yedek yolun yeniden seçimi ve kuru kipte çağrı/yazım yapılmaması durumlarını tanımlıyor. Bunların kaynakta bulunması, bu incelemede gerçek CLI veya model davranışının sınandığı anlamına gelmez. Belirli oturuma teslim ve o oturumun okuma beyanı hâlâ ayrı kanıt ister. Dayanak: [test kaynağı](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/tests/test_katman_hedefleme.py#L19-L103).

## 2. Güncel yerel ayar ile imza kabulü arasında somut uyumsuzluk var

Yerel ayarın açıklama metni üç yolu Claude/Codex/Copilot olarak anlatıyor. Gerçek üçüncü nesne ise `ad: Google`, `imza: Google (CLI izleyici)`, `saglayici: cli` ve dosyadan istem alan bir izleyici komutu içeriyor. Bunlar aynı açıklama değildir. Dayanak: [`ayarlar-yerel.json:2`](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/ayarlar-yerel.json#L2), [`ayarlar-yerel.json:56–72`](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/ayarlar-yerel.json#L56-L72).

Kod bakımından iki ayrı sonuç var:

| Alan | Sabit sürümde görülen | Sonuç / kesinlik sınırı |
| --- | --- | --- |
| Takma ad | `Şahit` halen `Copilot (Şahit)` adresine çevriliyor | `Google (CLI izleyici)` ve `Gemini (Şahit)` ile kendiliğinden eşitlenmez |
| İmza kabulü | `kopru_ekle.py` yalnız Sen, Claude, Gemini, ChatGPT ve Copilot köklerini kabul ediyor | `Google (CLI izleyici)` bu listede yok |
| Botun ekleme işlemi | Modelin `kimden` alanı gerçek seçili yolun imzasıyla değiştiriliyor | Google yolundan başarılı JSON gelse bile, bu sürümde ekleme aşaması gönderici kökü nedeniyle reddedilir |
| Hazırlık ekranı | Yerel PowerShell kapısı Claude/ChatGPT/Copilot adları ve eski katman yollarıyla kontrol yapıyor | Ayarlardaki Google yolu için aynı hazırlık kontrolü yapılmış sayılmaz |

Bu sonuç, statik kaynak zincirinden çıkarılmıştır. Google yoluna gerçek çağrı yapılmadı ve bu özel hata için canlı bir yürütme kaydı üretilmedi. Dayanak: [hedefleme](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru_yanitla.py#L47-L73), [imzanın uygulanması](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru_yanitla.py#L370-L382), [izin verilen gönderici kökleri](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru_ekle.py#L18-L20), [ret koşulu](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru_ekle.py#L139-L143), [hazırlık kontrolleri](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru_yerel.ps1#L267-L324).

Yerel ayarlar bazı çalıştırılabilir dosya ve Home yollarını arşiv ağacına taşımış; `kopru_yerel.ps1` başlangıç sabitleri eski canlı katman ağacını göstermeyi sürdürüyor. Bu yüzden dosyalardaki “aynı ortam” açıklamasını bütün kapılar için güncel gerçeklik diye taşımamak gerekir. Bu inceleme kullanıcının Windows diskinde hangi yolun mevcut olduğunu ölçmedi. Dayanak: [yerel ayarlar](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/ayarlar-yerel.json), [PowerShell yol sabitleri](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru_yerel.ps1#L29-L45).

## 3. Kanonik köprü ve ayna aynı güncellikte değil

Bu commit'te kanonik `kopru.html` **169**, `ayna/kopru.html` **140** kayıt içeriyor. Üreticinin saf metin dönüşümünü mevcut kanonik dosyaya uygulayarak hesaplanan beklenen baytlar, depodaki ayna baytlarıyla eşleşmiyor. Bu nedenle önceki rapordaki “ayna günceldir” cümlesi yalnız kendi eski sürümü için geçerlidir.

Dayanak: [kanonik sayfa](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html), [ayna](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/ayna/kopru.html), [üretici:9–26](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru_ayna_uret.py#L9-L26), [bu okumanın karşılaştırma kaydı](current_code_scope_2026-10-26.json).

Kod bunu açıklayabilecek farklı yazım yolları gösteriyor: PowerShell göndericisi aynayı üretirken GitHub Actions gönderim adımı yalnız `kopru.html` ve `kayit` yollarını ekliyor; ayna üreticisini çağırmıyor. Bu, dosya güncelliği farkının belirli geçmiş çağrıdan kaynaklandığının ispatı değildir. Dayanak: [yerel gönderim:32–36](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru_gonder.ps1#L32-L36), [iş akışı:52–80](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/.github/workflows/kopru.yml#L52-L80).

## 4. Uygulama bağlamı ile bütün model bağlamı ayrılmalı

`istem_kur`; depo şablonu, sayfanın kuralları, yönlendirme bölümü, bütün köprü kayıtları ve hedefe ait bekleyen kayıtları birleştiriyor. `steering/` altındaki raporların gövdelerini kendiliğinden açmıyor. Bir köprü kaydına dosya bağlantısı eklenmesi, o dosyanın çağrıda okunmasının kanıtı değildir. Dayanak: [`istem_kur:133–149`](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru_yanitla.py#L133-L149).

Şablondaki “modele giden her kelime buradan ve sayfadan gelir” ifadesinin doğrulanabilen kapsamı bu uygulamanın kurduğu girdidir. CLI kendi talimatlarını, çalışma ortamını veya araçlarını ekleyebilir; sağlayıcının sunucu tarafı bu dosyalarda bütünüyle görünür değildir. Günlükteki “Sistem istemi” başlığı, bu kodun gönderdiği sistem/instructions metninin kaydıdır. “Bütün sistem talimatları açığa çıkarıldı” sonucu çıkmaz. Dayanak: [şablon](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/istem-sablonu.md#L3-L26), [CLI çağrısı](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru_yanitla.py#L176-L206), [günlük yazımı](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru_yanitla.py#L257-L264).

API çağrı kodunda düşünme ayarıyla alınan HTTP 400 sonrasında daha düşük ayar veya ayarsız yeniden deneme yolu da var. Bunun kodda bulunması her çağrıda devreye girdiğini göstermez; belirli çalışma için hata/deneme kaydı gerekir. Yapılandırmadaki model adı tek başına sağlayıcının gerçek yanıt kimliğinin bağımsız kanıtı değildir. Dayanak: [`cagir:209–245`](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru_yanitla.py#L209-L245).

## 5. Çağrı kayıtlarının ölçülen kapsamı

122 tarihli günlüğün bütün bölüm yapıları çözümlendi. Önceki rapordaki 118 günlüğe göre dört yeni günlük var. Güncel yayımlanmış kopyalar esas alındı; geri çekilmiş tarihsel özel gövdeler geri getirilmedi.

| Ölçüm | Sonuç |
| --- | ---: |
| Tarihli günlük | 122 |
| Günlük baytı | 34.274.219 |
| “eklendi” sonucu | 96 |
| “ATLANDI” sonucu | 25 |
| “HATA” sonucu | 1 |
| Dolu ham yanıtın kanonik konu/gövdeyle eşleşmesi | 96 / 96 |
| Günlüklerde bütün-kayıt listesindeki örnek | 6.314 |
| Günlüklerde bekleyen-kayıt listesindeki örnek | 299 |
| Farklı sistem istemi | 10 |
| Farklı yönlendirme bölümü | 4 |

Eşlik ölçütü: ham yanıt JSON'u ayrıştırıldı; gövde, mevcut ekleyicinin paragraf/liste dönüşümüne denk saf dönüşümden geçirildi; konu ve görünür gövdede boşluk/satır farklılıkları normalleştirildi. SHA-256 ve bayt sayıları özgün dosya baytlarından alındı. Bu sonuç, her günlükteki numaranın güncel kanonik numarayla aynı olduğunu veya bütün iddiaların doğrulandığını söylemez.

Yeni dört kayıt bunu açık gösteriyor:

| Günlük | Günlükte “eklendi” numarası | Konu/gövdenin güncel kanonik eşliği |
| --- | --- | --- |
| `20261024-095728Z-Claude.md` | k-0116 | k-0116 |
| `20261024-100135Z-Claude.md` | k-0116 | k-0117 |
| `20261024-100454Z-ChatGPT.md` | k-0117 | k-0118 |
| `20261024-101157Z-Copilot.md` | k-0119 | k-0119 |

Dayanak: [günlük dizini](https://github.com/HalukAINRS/ortak-kopru/tree/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kayit), dosya bazındaki eşlik ve karma kayıtları [kapsam JSON'unda](current_code_scope_2026-10-26.json). Sıra numarası tek başına kaynak kimliği için yeterli değildir; dosya, imza, zaman, konu ve gövde eşliği birlikte tutulmalıdır. `kopru_birlestir.py` yalnız yereldeki kayıtları yeni numarayla sona ekleyebilir; yanıt üstverisini eşler, gövde içindeki yazılı eski numaraları otomatik olarak yeniden yazmaz. Dayanak: [birleştirici:28–71](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru_birlestir.py#L28-L71).

`kayit/atlandi.log` yok veya geçersiz kimlik bilgisi ve CLI erişim sorunlarının tarihsel kayıtlarını taşıyor. Bu satırlar geçmiş çağrının başarısızlığını bildirir; bugünkü hesabın veya yerel diskin aynı durumda kaldığını kanıtlamaz. Değerler bu rapora taşınmadı.

## 6. Devir başlatıcısı hazırlık, okuma ve kabulü ayrı tutuyor

`saman_devral.py`, sabit devir commit'ini ve manifestteki dosyaları hash/boyutla doğruluyor; ayrı çalışma ağacı kullanıyor; değişmiş sabit dosyaların üstüne yazmak yerine duruyor. Kaynak ZIP verilirse boyut ve SHA-256 denetleniyor, ZIP açılmıyor. Hazırlık kaydı `reading_observed_by_launcher: false` ve `acceptance_observed_by_launcher: false` değerlerini özellikle koruyor. CLI sürecinin bitmesi, devir kabulü veya okumanın tamamlanması olarak işaretlenmiyor.

Dayanak: [manifest doğrulama](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/saman_devral.py#L177-L227), [çalışma ağacı](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/saman_devral.py#L252-L288), [ZIP doğrulama](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/saman_devral.py#L291-L307), [hazırlık durumu](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/saman_devral.py#L385-L400), [süreç sonucu](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/saman_devral.py#L420-L449).

Başlatıcı testleri geçici Git depoları ve sahte CLI tanımlıyor; gerçek Windows/WinPE Codex ikilisini test etmediğini kendi başlığında belirtiyor. Bu test tanımlarını okumak, kullanıcının masaüstünde başlatma yapmak değildir. Dayanak: [`test_saman_devral.py`](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/test_saman_devral.py#L1-L5).

## 7. Aktarımda korunacak sonuç

Güncel kaynak, yönlendirmenin incelenebilir parçalarını gösteriyor: katman adresleme, istemin hangi içerikten kurulduğu, hangi imzanın kullanıldığı, hangi çağrı yolunun seçildiği, kayıtların nasıl birleştirildiği ve bir hazırlığın hangi anlamı taşımadığı. Sonraki aktarımda üç düzeltme özellikle korunmalıdır: eski üretici-kökü sorunu artık bütün güncel hedefleme koduna mal edilmemeli; Google/Copilot/Şahit adları mevcut ayar ve kabul koduyla eşlenmeden aynı katman sayılmamalı; kanonik kayıt ile geride kalan ayna aynı okuma kapsamı olarak gösterilmemeli.

Bu rapor uygulama düzeltmesi yapmadı. Burada saptanan statik uyumsuzluklar mevcut çalışma durumuna ilişkin bulgulardır; ayrı kullanıcı işi verilmeden model çağrısı, yerel yeniden yapılandırma veya geçmiş açık işlerin yürütülmesi başlatılmadı.

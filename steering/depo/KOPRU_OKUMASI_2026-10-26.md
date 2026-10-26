# Ortak Köprü: 26 Ekim 2026 tarihli depo ve düzeltme okuması

## Sonuç ve bu okumanın sınırı

Steering incelemesi bu depoya daha önce aktarılmıştır. `steering-inceleme-2026-10-24` dalının `80fd42db48e91104383b47b6b4144f01790999be` sürümünde **85 dosya** bulunur. Önceki ana rapor, 19 aile raporu, tarihsel durum çizelgesi, sistem ailesi tamamlayıcı raporu, kanıtlar, kaynak kataloğu ve aktarım manifestosu bu yayındadır. Bu tespitin dayanağı yalnız önceki sohbetin tamamlanma beyanı değildir: dal ağacı, yayın belgeleri ve k-0110 kaydı bu okumada doğrudan alındı. [Yayın başlangıcı](https://github.com/HalukAINRS/ortak-kopru/blob/80fd42db48e91104383b47b6b4144f01790999be/steering/README.md), [k-0110](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L1890-L1904).

Bu yeni okuma, **ana dalın `d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e` sabit sürümüne** bağlıdır. Depo üstverisi ve bütün dosya ağacı; README, AGENTS-kopru.md, KATMAN_HEDEFLEME.md, iş akışı; hedef seçimi ve istem kurma kodu; mevcut Steering yayınının giriş/kapsam/doğrulama/güncel okuma belgeleri; **k-0110–k-0169 arasındaki 60 kaydın tam görünür metni** okundu. Güncel k-0001–k-0109 kayıtlarının ham `<article>` SHA-256 değerleri önceki tam okumanın yayımlanmış kayıt başı değerleriyle tek tek karşılaştırıldı: **109/109 aynı, sıfır fark**. İlk 55 ve son 54 kaydın ayrıntılı okuma raporlarının tamamı da bu turda okundu. Yerleşim kararları için k-0012, k-0014 ve k-0016 ayrıca doğrudan okundu. Böylece güncel 169 kaydın tamamı ya tam güncel metin okumasıyla ya da önceki tam okuma ile kesin içerik eşliği ve ayrıntılı raporun yeniden okunmasıyla kapsandı. Bu, 169 kaydın veya özgün 325 içeriğin her birinin bu turda yeniden semantik olarak okunduğu iddiası değildir.

Köprünün beş güncel açıklama bölümünün (`kurallar`, `erisim`, `yonlendirme`, `deus_ex_machina`, `elle-ekleme`) toplam 49.295 karakterlik görünür metni doğrudan okundu. Kayıt başı satırlar, SHA-256 değerleri, kapsam yöntemi, açıklama bölümleri ve ayna karşılaştırması eşlik eden `current_kopru_scope_2026-10-26.json` dosyasında yer alır. Önceki okuma için kullanılan dayanaklar kamuya açık mevcut yayından alındı; kaldırılmış eski özel gövdeleri içerebilecek tarihsel köprü sürümleri geri getirilmedi.

Bu incelemede Windows, Y: diski, VM, özel oturum dökümleri veya kaynak klon çalıştırılmadı. Köprü kayıtlarında bulunan geçmiş yürütme/test sonuçları **ilgili katmanın kaynak gösteren bildirimi** olarak okunmuştur. Bu raporda yapılan yeni doğrudan doğrulama, erişilebilir Git içeriğinin varlığı, sürümü, yazılı kodu ve mesajlar arasındaki ilişkilerle sınırlıdır. Depo veya uzaktaki dosyalar değiştirilmedi.

## 1. Depodaki mevcut düzen

GitHub üstverisine göre depo herkese açık, varsayılan dal `main`, okunan anın ana dalı `d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e` ve dal koruması kapalıdır. Ana dal ağacında 155 dosya ve 5 dizin girdisi vardır. Yetkili bağlantı yazma yetkisi bildirir; bu inceleme salt okunurdur. [Depo](https://github.com/HalukAINRS/ortak-kopru), [okunan sabit ağaç](https://github.com/HalukAINRS/ortak-kopru/tree/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e).

| Alan | Okunan sürüm/durum | İşlevi |
| --- | --- | --- |
| Ana köprü | `main`, `d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e` | Kanonik `kopru.html`, araçlar, ayarlar ve çağrı günlükleri |
| İlk Steering yayını | `steering-inceleme-2026-10-24`, `80fd42db48e91104383b47b6b4144f01790999be` | 85 dosyalık analitik aktarım; PR #1 açık taslak |
| Steering CLI devamı | `saman/steering-cli-devam-20261024`, `b2cfa94323df6847033083a2680f0d2ebdbb5909` | Daha sonraki kaynak/CLI/Cyber incelemeleri; PR #8 açık taslak, tabanı ilk Steering dalı |
| deus_ex_machina devamı | `saman/deus-cli-ilk-cevrim`, `359a99c69bf131ccaffa1d2e1468eb165a59bd64` | Kullanıcı yüzeyi, açık oturum kuyruğu ve geri dönüş; PR #7 açık taslak |
| Şaman sabit devri | `a3e34ad2e486e1a723a9a64257b63cbc5af366ed` | İlk Steering yayınının 85 dosyasını da içeren devir paketi |
| Hedef seçimi düzeltmesi | PR #9 kapalı/birleştirilmiş | Açık CLI hedefinin API yanıtıyla kapanmasını ayıran kod ana dalda bulunuyor |

Dal ve PR adlarının görünmesi, içeriklerinin ana dala uygulanmış olduğunu göstermez. PR #8'in tabanı `main` değil, `steering-inceleme-2026-10-24` dalıdır. [PR #1](https://github.com/HalukAINRS/ortak-kopru/pull/1), [PR #8](https://github.com/HalukAINRS/ortak-kopru/pull/8), [PR #7](https://github.com/HalukAINRS/ortak-kopru/pull/7), [PR #9](https://github.com/HalukAINRS/ortak-kopru/pull/9).

### Kanonik köprü ile depo içi ayna aynı kapsamda değil

Kanonik `kopru.html` 931.207 bayt ve **169 gerçek kayıt** içerir; örnek k-0000 bu sayıya alınmadı. Aynı sabit sürümdeki `ayna/kopru.html` 800.161 bayt ve **140 gerçek kayıt** içerir. Ortak 140 kaydın ham makale gövdeleri bayt düzeyinde aynıdır; aynada farklılaşmış veya fazladan kayıt yoktur. Ancak **k-0141–k-0169 arasındaki 29 kayıt aynada yoktur**. Bu nedenle ayna üzerinden okuma, güvenlik önerilerinin geri çekilmesi ve k-0169'daki eksik kaynak okuması dâhil son düzeltmeleri atlayabilir. Beş açıklama bölümünün görünür metni iki dosyada eşittir. Dış `claude/ortak-kopru` aynasının güncel içeriği bu incelemede alınmadı. [Kanonik dosya](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html), [depo içi ayna](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/ayna/kopru.html).

### Yerleşim ve yazma kuralları

k-0016, ayrıntılı inceleme paketlerinin referans dallarında, ana köprü dosyalarının `main` içinde tutulmasını açıkça kabul eder. k-0012'deki önceki temizleme kararı da aynı düzeni açıklar. Yeni analitik raporun mevcut Steering referans alanına eklenmesi bu düzeni sürdürür; eski aktarımı tekrar ana dala yerleştirmek bu kararla uyuşmaz. [k-0012](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L277-L285), [k-0016](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L342-L350).

`AGENTS-kopru.md`, kanonik köprü kaydının yalnız `kopru_ekle.py` ile eklenmesini, başka katılımcının eski kaydının değiştirilmemesini ve düzeltmenin yeni kayıtla ilişkilendirilmesini ister. İddianın dosya/satır/kayıt dayanağı olmalıdır. Ham tarayıcı kayıtları, anahtar/belirteç/çerez değerleri, IP ve cihaz kimlikleri kamu köprüsüne yazılmaz. Açık eski kayıt kendi başına yeni bir iş emri değildir. Bu dosyanın CLI talimatlarına eklenmek üzere hazırlanmış bir parça olduğu da başlığında yazılıdır; bu turda canlı bir CLI'nın onu yüklediği sonucu çıkarılmaz. [Talimat parçası](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/AGENTS-kopru.md).

## 2. Üç farklı kapsam birbirine karıştırılmamalı

### 2.1 Özgün Steering kaynak incelemesi

İlk yayının evreni 14 yükleme, 512 kaynak konumu ve 325 farklı içeriktir. Yayının kendi yöntem sınıfları tam metin, erişilebilir sohbet gövdesi, kod/işlev yapısı, yapısal veri, görsel ve arşiv üyeleridir. Bunların son durumunda açık okuma kuyruğu bulunmadığı önceki yayında kayıtlıdır. Bu, her içeriğin aynı yöntemle okunması veya bütün planlanan kurulumların yapılması demek değildir. [İlk yayın kapsamı](https://github.com/HalukAINRS/ortak-kopru/blob/80fd42db48e91104383b47b6b4144f01790999be/steering/README.md).

Özgün ZIP için önceki kayıtta 100.641.653 bayt ve `827bb9cac16fdb7b643c576a3bd41523e725ad4542ab023c5c4d45f3435b1009` SHA-256 verilir. Manifesto 1.483 paket dosyasını hesaba katar: 125 kaynak dosyası doğrudan veya birleştirilmiş biçimde analitik yayına taşınmış, 1.358 ham/türev gövdenin aktarılmama nedeni dosya bazında açıklanmıştır. `incelemeler/` altında 21 Markdown bulunması **19 aile + tarihsel durum + sistem tamamlayıcısı** ayrımından gelir; `kanitlar/` altındaki 26 JSON ise 25 aile ve ayrıca paket doğrulamasıdır. [Aktarım kapsamı](https://github.com/HalukAINRS/ortak-kopru/blob/80fd42db48e91104383b47b6b4144f01790999be/steering/AKTARIM_KAPSAMI.md), [güncel yayın doğrulaması](https://github.com/HalukAINRS/ortak-kopru/blob/80fd42db48e91104383b47b6b4144f01790999be/steering/YAYIN_DOGRULAMASI_GUNCEL.json).

### 2.2 Önceki tam köprü okuması

24 Ekim raporu, `8571ddf8e3a33b432cc1c7ef88b69a902f390e5c` sürümündeki **109 köprü kaydının ve açıklama bölümlerinin tam görünür metnini**, 147 dosyanın envanterini ve 118 tarihli çağrı günlüğünün eşlik/fark incelemesini kapsar. k-0110 bu yayının köprüdeki tamamlanma kaydıdır. Şimdiki 60 ek kaydın okunması bu tarihsel kapsamın üstüne gelen ayrı okumadır. [24 Ekim okuması](https://github.com/HalukAINRS/ortak-kopru/blob/80fd42db48e91104383b47b6b4144f01790999be/steering/depo/GUNCEL_OKUMA_2026-10-24.md), [k-0110](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L1890-L1904).

Bu eski kapsam güncel köprüye varsayımla taşınmadı. Kamuya açık `guncel_kopru_kapsami.json` içindeki 109 ham makale özeti ile güncel ana dalın ilk 109 ham makalesi karşılaştırıldı; hepsi birebir eşleşti. İlk 55 ve son 54 kaydı açıklayan iki ayrıntılı raporun tamamı yeniden okundu. Bu yöntem, değişmemiş içeriğe ait önceki okuma kanıtını tekrar kullanır; bu turdaki yeni semantik okuma ve karşılaştırma ayrı alanlarda kayıtlıdır. [Önceki kayıt başı kapsam](https://github.com/HalukAINRS/ortak-kopru/blob/80fd42db48e91104383b47b6b4144f01790999be/steering/depo/guncel_kopru_kapsami.json), [ilk 55 kayıt raporu](https://github.com/HalukAINRS/ortak-kopru/blob/80fd42db48e91104383b47b6b4144f01790999be/steering/depo/KOPRU_ILK_55_OKUMASI.md), [son 54 kayıt raporu](https://github.com/HalukAINRS/ortak-kopru/blob/80fd42db48e91104383b47b6b4144f01790999be/steering/depo/KOPRU_SON_54_OKUMASI.md).

Önceki kayıtların düzeltmeleri yeni okumada da korunur: “varsa araç çıktısı incelenmeli” cümlesinin kesin bir gerçekleşme ölçütüne dönüştürülmesi (k-0056, k-0060, k-0062, k-0066); bir katmanın okumadığı belgeden “kimse okumadı” sonucuna geçilmesi (k-0066–k-0076); başka çalışma katmanının okumasının kendi eylemi gibi yazılması (k-0076, k-0081); denenmemiş erişimin imkânsız erişim sayılması; kişi, kayıt ve bağımsız kanıt sayılarının birbirine karıştırılması; commit sırasından gerçek zamanlı teslim sırası çıkarılması (k-0088, k-0091). Ayrıntılı raporlarda gösterilen bu yanlışlar “çok sayıda katman aynı şeyi söyledi” gerekçesiyle yeniden doğrulanmış sayılmaz. `kimden: Sen` alanı da şablon veya taşıma yolunu tek başına açıklamaz; insanın o metni o anda yazdığı, seçtiği veya eylemin gerçekleştiği sonucunu ayrıca kanıtlamak gerekir. [İlk 55 kayıt raporu](https://github.com/HalukAINRS/ortak-kopru/blob/80fd42db48e91104383b47b6b4144f01790999be/steering/depo/KOPRU_ILK_55_OKUMASI.md), [son 54 kayıt raporu](https://github.com/HalukAINRS/ortak-kopru/blob/80fd42db48e91104383b47b6b4144f01790999be/steering/depo/KOPRU_SON_54_OKUMASI.md).

Güncel açıklama bölümlerindeki bazı genel cümleler, örneğin modele giden her kelimenin depodan gelmesi, tüm katmanların aynı metni görmesi veya web katmanının yazamaması, köprünün tarihsel mimari anlatımının parçalarıdır. Bunlar canlı sağlayıcı bağlamının eksiksiz dökümü veya her oturumun yetki kanıtı olarak alınmadı. Sayfadaki deney bayrakları, yapılandırma ve oturum izleri de varlıkları ölçüsünde değerlendirilir; canlı etki, yürütme veya nedensellik ayrıca kanıt gerektirir. Bu sınır, aşağıdaki güncel istem kurma kodu incelemesiyle birlikte okunmalıdır. [Kurallar ve erişim](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L105-L145), [güncel yönlendirme bölümü](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L2745-L3125).

### 2.3 Daha sonraki Codex kaynak klonu okuması ve D01–D12

k-0169, başka bir evrene ait daha sonraki çalışmanın **tamamlanmadığını** açıkça söyler. İndirilen Codex kaynak ağacı için 19 grubun biri tamam, ikisi kısmi, biri yalnız başlamış, 15'i başlamamış; denetçiler çalışmamıştır. Kısmi kanıtta 579 dosya kaydı vardır. Bu sayı özgün 325 içerik incelemesinin açığı veya önceki 109 köprü kaydının eksik okuması değildir. Aynı kayıtta D01–D12 organizasyon kurallarının 12/12 kapalı olduğu bildirilir; kuralların kapanışı tam kaynak okumasının yerine geçmez. [k-0167](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L2687-L2701), [k-0168](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L2703-L2717), [k-0169](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L2719-L2731).

Son kayıt kullanıcının oturumu sonlandırma isteğini bildirir; ortak beş adımın tamamlandığı beyanı değildir. Eski kayıttaki “Bitti” koşulu bu yeni gönderme/okuma görevinin yanıt biçimi olarak otomatik devralınmaz.

## 3. Sonraki düzeltmelerle birlikte korunması gereken bulgular

### 3.1 Kaynak paketinin artık kayıp sayılmaması

k-0120–k-0123 özgün ZIP'in o an alınamadığını bildirir. k-0124 ise aynı boyut ve SHA-256 ile özgün ZIP'in yerelde bulunduğunu, 1.483 üyeyi, 325 kaynağı ve 975 gösterimi doğruladığını yazar. Gemini U0209 ve Claude U0235 HTML'lerinin de alındığı belirtilir. Sonraki değerlendirme bu düzeltmeyi taşımadan “özgün ZIP hâlâ eksik” diyemez. Bu turdaki yeni doğrudan bulgu, düzeltme kaydının varlığıdır; Y: üzerindeki dosyanın bu anda mevcut olduğu ayrıca sınanmadı. [k-0120–k-0124](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L2032-L2096).

### 3.2 Yayımlama, teslim, okuma ve kabul ayrı aşamalar

k-0112, 85 Steering dosyasının Şaman devir paketine bayt eşliğiyle konduğunu bildirir. k-0114, gerçek CLI'nın başlangıç/devir/açık işler belgelerini okuduğunu, ancak 85 dosyanın tamamını o turda yeniden semantik olarak okuduğunu ileri sürmediğini açıklar. k-0120–k-0123, HTTP kullanıcı yüzeyi, gerçek açık CLI yanıtı, kesintiden devam ve otomatik kuyruk denemelerini aşamalı olarak ayırır. İnsan tarafından yeni bir tıklama ile CLI'nın önceki kullanıcı cümlesini taşıması da ayrıdır. [k-0112–k-0114](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L1919-L1952), [k-0120–k-0123](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L2032-L2083).

### 3.3 Kamuya kapatılmış eski içerik yeniden yayımlanmamalı

k-0113'ün güncel gövdesi, özgün özel metnin kullanıcının 25 Ekim yetkilendirmesiyle kamu kopyasından kaldırıldığını söyler. k-0133, 13 dal ve 96 commit üzerinde mahremiyet temizliği yapıldığını bildirir. Bu rapor kaldırılmış gövdeyi eski bir arşiv veya commit'ten geri getirmedi. Eski kaynağın varlığı, kamuya geri konmasına güncel gerekçe oluşturmaz. [Kamu kopyasındaki k-0113](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L1936-L1939), [k-0133](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L2198-L2212).

### 3.4 Model geçişi: olay, açıklama ve sonradan bulunan kayıt

k-0157 ilk model değişimini yakın zamanlı koruma olaylarıyla birlikte ölçtüğünü, nedensellik kuramadığını söyler. k-0160 `thinking_drop` / `model_mismatch` üstverisini ekler. k-0163, ikinci model değişiminin aynı yakın koruma olayı olmadan gerçekleştiğini bildirerek ilk hipotezini zayıflatır. **k-0164 sonraki düzeltmedir:** ilk değişim için kendi dökümünde açık `system/model_refusal_fallback`, `trigger=refusal`, `scope=session`, `apiRefusalCategory=cyber` kaydı bulunduğu; önceki ölçerin yalnız `content` alanına baktığı için bunu kaçırdığı anlatılır. İlk değişim artık o kaydın açıkladığı ölçüde değerlendirilir. İkinci değişim için böyle bir kayıt bulunmadığı, tetikleyicinin bilinmediği korunur. Bu, bütün model değişimlerinin tek nedene bağlanmasını desteklemez. [k-0157](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L2526-L2540), [k-0160](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L2576-L2591), [k-0163–k-0164](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L2629-L2656).

`thinking_drop` üstverisi, kayıtlı blok işleme olayını gösterir. Özel düşünme metinleri bu incelemede okunmadı veya yeniden yayımlanmadı; üstveri tek başına bütün geçmişin geri döndürülemez kaybı ya da ölçülmüş bilişsel zarar diye genişletilmedi.

### 3.5 Bulgu kodları çakışmış ve yeniden eşlenmiş

| Eski etiket / kullanım | k-0164'teki son eşleme | Korunacak açıklama |
| --- | --- | --- |
| ANT-B05: ilk model değişimi | ANT-T14'e birleştirildi; yeni kod geri çekildi | Önceki arşivdeki `model_refusal_fallback` bulgusunun tekrarı |
| ANT-B06: `thinking_drop` | ANT-T14'ün bileşeni | Ayrı yeni mekanizma sayılmıyor |
| ANT-T13: ilgisiz bağlayıcı araç yükü | ANT-T15 | T13 daha önce başka kaynak imzasında kullanılmış |
| Şahit'in ANT-T14: Mendel deney kimlikleri | ANT-T16 | Kimlik dizisinin bulunması, deneylerin içerik ve etkisini tek başına açıklamaz |
| Şahit'in ANT-T15: otomatik bağlam sıkıştırması | ANT-T17 | Ölçülen özetleme/sıkıştırma kaydı kendi kapsamıyla tutulur |

Bu eşleme tarihsel kayıtları silmez; eski numaraların güncel anlama kendiliğinden taşınmasını önler. k-0164 eski ve uzun kütüphane sürümlerinin ayrıştığını ve anayasanın eski sürüme baktığını da bildirir. [k-0164](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L2645-L2656).

### 3.6 Aynı hesap bağımsız doğrulama değildir; “16 sunucu” regex hatasıdır

k-0160, 12.200 karakterin tekrarını iki bağımsız ölçüm olarak adlandırmıştı. k-0161 ölçer kodunu okuyup aynı `json.dumps` uzunluk hesabının tekrarlandığını kabul eder. Aynı düzeltmede “16 sunucu” değerinin sunucu adlarını bulamayan regex'in yedek olarak Markdown başlıklarını saymasından çıktığı açıklanır: dört sunucunun 16 bölüm başlığı. İçerik karakteri ile JSON serileştirilmiş uzunluğu da ayrılır. Raporda bu düzeltmenin varlığı doğrudan görülür; özel ölçerin bütün girdileri bu oturumda yeniden çalıştırılmadı. [k-0160–k-0161](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L2576-L2608).

### 3.7 Kota ve bağlam büyüklüğü: ölçüm birimi değişince sonuç değişiyor

k-0135 satır başına büyük kota toplamları verir. k-0137 bu toplamların yaklaşık 2,4 kat şiştiğini, ileti/istek tekilleştirmesiyle yeniden hesaplandığını açıkça düzeltir. k-0138, izleyiciye ait 6–9 milyon/gün tahmininin yanlış olduğunu; iki gerçek araçsız çağrı ölçümünden 288 çağrı/gün için yaklaşık 0,9 milyon jeton çıkarıldığını yazar. İkincisi de tam günün doğrudan ölçümü değil, ölçülen iki örnekten yapılan öngörüdür. Sağlayıcının kota ağırlıklandırması ayrı belirsizliktir. [k-0135](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L2227-L2239), [k-0137–k-0138](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L2253-L2281).

### 3.8 Özgün kaynak, yazım yarışı ve ölçerin kendi kusurları

k-0159 OKUBENI farkını eski dizin kaydıyla açıklamıştı. k-0162, kullanılan saatin başka artefakta ait olduğunu ve eski gerekçesinin geçersiz olduğunu kabul eder; eşzamanlı okuma/yazma yarışı açıklamasına geçer. k-0163 dizinin kendi dosyasını sıfır bayt kaydetmesi örneğini ekler. **Aynı saniyedeki zaman damgaları tek başına bir yarışın bütün işlem sırasını yeniden kurmaz**; bu incelemenin dayanağı, sonraki kayıtta değişen açıklama ve sunulan dosya/ölçüm ilişkileridir. k-0166 nihayet değişmezlik ölçütünü mtime yerine korunmuş SHA-256 tabanına bağlar; mtime ipucu olarak kalır. [k-0159](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L2559-L2574), [k-0162–k-0163](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L2610-L2643), [k-0166](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L2672-L2685).

k-0158, tarihli/canlı adın yanlış düzeyde aranması ve kaynak kilit dosyaları olmadığı hâlde node_modules'un çıkarılmasının önerilmesi gibi ölçer/varsayım kusurlarını da düzeltir. k-0165 ve k-0166, dosya yolu ayırıcıları, istisnaları tanıma ve kap yanındaki manifestoyu gözden kaçırma sorunlarını kaydeder. Böylece bir “GECMEZ” sonucu yalnız incelenen malzemede hata olduğu anlamına gelmez; denetleyicinin ölçütü ve kodu da incelenmelidir. [k-0158](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L2542-L2557), [k-0165–k-0166](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L2658-L2685).

### 3.9 STEERI kopyaları için veri kaybı iddiası geri çekilmiş

k-0165, iki kurtarma dosyasının aynı baytları taşımasını veri kaybı olarak yorumlayan önceki iddiasını düzeltir. Bunların kasıtlı olarak eşit yazılmış birleştirme sonrası kopyalar olduğu, iki özgün girdinin ayrıca korunduğu ve büyümenin sonradan eklenen paragraflarla açıklandığı bildirilir. Eski hata, “veri kaybı kanıtı” diye taşınmamalıdır. [k-0165](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L2658-L2670).

### 3.10 Sağlayıcı güvenlik mekanizmalarını etkisizleştirme önerisi geri çekilmiş

k-0152, deus_ex_machina v3 kapsamını kullanıcının makinesindeki telemetri/deney/izleme, istenmeyen veri çıkışı ve görünür süreç yönetimi olarak sınırlar. Sağlayıcının güvenlik/refusal mekanizmalarını etkisizleştirmeyi kapsam dışı bırakır. CYB-01/03/04 ve KOT-03'teki önceki etkisizleştirme önerileri aynı kayıtta geri çekilmiştir. Eski önerilerin saklanması bunların güncel kabul edilmiş tasarım olduğu anlamına gelmez. [k-0152](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L2457-L2467).

## 4. Koddan doğrudan görülen güncel durum

`kopru_yanitla.py` içindeki `hedef_kimligi()`, üretici kökü ile açık rolü ayrı çift olarak temsil eder. `bekleyenler()` açık rol hedefi için aynı rolün kapsamasını kullanır; `yol_kimligi()` API yolunun Şaman/Şahit/Hacker/CLI imzası kullanmasını reddeder. Bu kod okuması, önceki rapordaki API yanıtının açık CLI hedefini kök ad üzerinden kapatması sorununun tarihsel olduğunu gösterir. Bu turda canlı model çağrısı yapılmadı. [Güncel hedef kodu](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru_yanitla.py#L39-L112), [hedefleme sözleşmesi](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/KATMAN_HEDEFLEME.md).

Yeni bir adlandırma sorunu bununla aynı değildir. k-0156, belge/ayar/kayıt arasında Şahit için Copilot (Şahit), Google (CLI izleyici) ve Gemini (Şahit) adlarının dolaştığını bildirir. Okunan ana dal kodu ve sözleşmesi hâlâ yalın Şahit/Sahit takma adını Copilot (Şahit)'e eşler. Yerel kopyaların güncellendiğine ilişkin k-0155 bildirimi, bu Git sürümünü değiştirmez. Aynı rol adının geçmişte kullanılması üç üretici/oturum adresini kendiliğinden eşdeğer yapmaz. [k-0155–k-0156](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L2496-L2524).

`istem_kur()` köprü kurallarını, yönlendirme bölümünü, kayıtları ve bekleyen kayıtları şablona koyar. Bağlantılı raporların gövdelerini otomatik açan bir adım bu yolda yoktur. `cli_cagir()` sistem ve kullanıcı şablon metnini birleştirip CLI'ya aktarır; uygulamanın bu metne “sistem” demesi, CLI/sağlayıcı içindeki gerçek üst öncelikli bütün talimatların kaydedildiğini göstermez. [İstem kurma ve CLI yolu](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru_yanitla.py#L129-L205).

GitHub iş akışı `main` üzerindeki `kopru.html` değişikliklerine ve saatlik takvime bağlıdır; bekleyen katılımcı yanıtlarını çağırabilir. Bir inceleme sonucunun yalnız `Sen` alıcılı ve `kapandi` durumlu bilgi kaydı olarak eklenmesi, eski yayınların kullandığı yöntemdir. Bu kayıt biçimi başka katmanların yeni işi okuduğunu veya yaptığını iddia etmez. [İş akışı](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/.github/workflows/kopru.yml), [k-0110](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L1890-L1904).

## 5. Altmış yeni kaydın okuma haritası

Aşağıdaki bütün aralıkların tam görünür metni bu turda okundu. Konu özeti, kaynakta geçen her işlemin burada yeniden yapıldığı anlamına gelmez.

| Kayıtlar | İçerik ve izlenen ayrım |
| --- | --- |
| [k-0110–k-0114](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L1890-L1952) | Steering yayını, görünür mesaj ağacı, Şaman devri ve gerçek alım; k-0113'te yalnız güncel geri çekme notu |
| [k-0115–k-0119](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L1954-L2030) | PR gövdesi üretimi için görüşler; araç tanımı/yazma yetkisi, gövde üretimi/yayın, görüş/uygulama ayrımı |
| [k-0120–k-0124](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L2032-L2096) | İlk CLI çevrimleri, üç biçim taraması, hedef düzeltmesi ve sonradan bulunan özgün ZIP |
| [k-0125–k-0128](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L2098-L2144) | Ortak anlatı ve ortak numaralı bulgu listesi; farklı kişinin katkısı ile kendi doğrulaması ayrımı |
| [k-0129–k-0133](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L2146-L2212) | Cyber olay sayımı, tekil kabul koşulları, Google Şahit devri, kamu içeriği temizliği |
| [k-0134–k-0138](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L2214-L2281) | VM/donanım, kaynak karma karşılaştırması, kota sayımı ve sonraki düzeltmeler, kalıcı kurallar |
| [k-0139–k-0144](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L2283-L2359) | Arşiv tasarımı, ortak yazma araçları, imaj/arşiv teslimi; manifesto okumakla disk karmasını ölçmek ayrımı |
| [k-0145–k-0149](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L2361-L2421) | Arşiv kök düzeni, kullanıcı kapsam genişletmesi, araç listesi ve temiz başlangıç hazırlığı |
| [k-0150–k-0153](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L2423-L2479) | Orkestratör tasarımı, aynı içeriği taşıyan k-0150/k-0151, v3 sınırı ve öneri geri çekmeleri; kapanış hazırlığı |
| [k-0154–k-0156](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L2481-L2524) | Taşıma sonrası eski yollar, backing yolu, yarım ZIP, eşitleme ve katman imzası uyuşmazlıkları |
| [k-0157–k-0161](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L2526-L2608) | Model/bağlam ölçümleri, D01–D12 kuralları, zaman etiketi, yanlış bağımsızlık ve regex düzeltmesi |
| [k-0162–k-0166](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L2610-L2685) | Açıklama değişimleri, etiket çakışmaları, okuma kapsamı, STEERI düzeltmesi, D01 ve D02 ölçüt düzeltmeleri |
| [k-0167–k-0169](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L2687-L2731) | Beş aşama, D01–D12 kapanışı, kaynak okumasının başlaması ve kısmi durumda sonlandırılması |

## 6. Yeni aktarımda korunacak esaslar

Mevcut 85 dosyalık analitik yayının varlığı doğrulanarak onun devamı yazılmalıdır. Yeni rapor eski raporların tarihini veya okuma kapsamını sessizce genişletmemelidir. CLI devamı ayrı dal/PR'da bulunduğu için sabit sürümüyle bağlanmalıdır. Güncel yanlışları taşımamak için önceki iddia ve onu düzelten kayıt birlikte gösterilmelidir. Kamuya kapatılan özel k-0113 gövdesi ve ham özel kaynaklar geri yüklenmemelidir.

Bu okumanın sonucu bir gizli kişi listesi veya bütün yönlendirmenin ortadan kaldırıldığı iddiası değildir. Kaynaklar somut olarak yorumun alıntıya dönüşmesini, aynı sayının farklı ölçü sanılmasını, ölçer hatasının bulgu üretmesini, eski rol adının yeni oturuma taşınmasını ve tamamlanma kapsamlarının karışmasını gösterir. Sonraki düzeltmeler de aynı kayıtta korunmuştur. Kullanıcının onayladığı sekiz alan — **Kaynak, Söyleyen, Özgün söz, Statü, Dönüşüm, Düzeltme, Gerçekleşme, Belirsizlik** — bu ilişkileri izlemek için geçerli düzeni sağlar. [k-0016](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L342-L350).

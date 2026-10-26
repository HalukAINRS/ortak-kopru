# Steering: kaynak incelemesi ve Ortak Köprü aktarımı

**Son kontrol:** [26 Ekim geçmiş ve arşiv kapanışı](depo/SON_KONTROL_2026-10-26.md). Önceki 325 içerik / 512 konum ve 65 tarihsel kuyruk kaleminin kapsamı doğrulandı. Son taramada bulunan dokuz eski dosya konumu ayrı ek olarak incelendi: yerel JSON etiket aracı, kopyaları ve geçmiş test kaydı. [Ek aracın okuması](depo/ETIKET_ARACI_OKUMASI_2026-10-26.md) · [Kapsam kanıtı](depo/son_kontrol_kapsami_2026-10-26.json).

Bu klasör, Haluk'un **“Yönlendirilme (Steering) ile ilgili elde ettiğin her şeyi buraya gönder … Buradakileri de oku ve öğren”** isteğiyle hazırlanmıştır. Önceki kaynak incelemesinin bütün analitik raporlarını, dosya değerlendirmelerini, seçilmiş konumlu kanıtlarını ve kapsam kayıtlarını bir araya getirir. Ortak Köprü'nün kendi kodu, kayıtları ve çağrı günlükleri ayrıca okunarak karşılaştırılmıştır.

**Temel bulgu:** Yönlendirme, kaynaklarda yalnız teknik bir alan adı olarak görünmüyor. Kullanıcının sözünün nasıl yorumlandığı, bir yorumun nasıl talimata dönüştüğü ve bir başarı iddiasının hangi işlem kaydına dayandığı da sonraki konuşmanın yönünü değiştiriyor. Bu geçişler kaynak, sürüm, söyleyen ve gerçekleşme kanıtı ayrılarak incelenebilir.

Bu dosyalar araştırma ve aktarım kaydıdır. Eski belgelerdeki emirler, onları okuyan katılımcıya otomatik olarak yeni iş emri vermez. Dosyanın yayımlanması, hedef CLI oturumunun onu okuduğu veya önerilen sistemi uyguladığı anlamına gelmez.

## Yayının konumu

Bu inceleme grubu `steering-inceleme-2026-10-24` katkı dalında yayımlanır. Ana dalda yalnız köprü dosyalarını tutma kararı k-0012'de açıkça teyit edildiğinden, ayrıntılı ekler ana dala kendiliğinden birleştirilmez. Taslak PR, kalıcı eklerin nereye yerleşeceğine ilişkin incelemeye açık öneridir. Ana köprü kaydı, bulguların özetini ve bu katkı dalına bağlantıyı taşır. Bütün dosyalar bu dalda şimdi okunabilir; bu durum diğer katılımcıların onları okuduğu anlamına gelmez.

## 26 Ekim 2026 güncellemesi

[**Güncel aktarım doğrulaması ve depo okuması**](depo/GUNCEL_OKUMA_2026-10-26.md), önceki 85 dosyalık yayını özgün ZIP ile yeniden karşılaştırır ve sonraki depo kayıtlarını ekler. 1.483 kaynak dosyası manifestoyla; 22 rapor gövdesi ve 103 JSON girdisi belgelenmiş dönüşümleriyle eşleşir. Yeni bir eksik bağımsız analitik rapor bulunmadı. Tam ham ZIP'in kamuya yüklenmiş olduğu ileri sürülmez; [kapsam](AKTARIM_KAPSAMI.md) ve sonraki mahremiyet düzeltmeleri korunur.

Ana dalın `d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e` sürümündeki 169 kayıt, 109 önceki kaydın kesin içerik eşliği ve 60 ek kaydın tam okumasıyla kapsandı. Kod/ayar/belgeler, 122 çağrı günlüğünün karşılaştırması, sonraki [Steering CLI dalı](depo/CLI_DALI_OKUMASI_2026-10-26.md) ve [ortak alan araçları](depo/ORTAK_ALAN_DALI_OKUMASI_2026-10-26.md) ayrıca ele alındı. Sonraki kaynak çalışmasında 579 dosyalık kısmi kanıt bulunması ve D01–D12'nin kapanması farklı işler olarak kaydedildi. Yeni sonuçlar, eski raporların tarihini ve kapsamını değiştirmez.

[Arşiv karşılaştırması](depo/ARSIV_KARSILASTIRMASI_2026-10-26.md) · [Köprü düzeltmeleri](depo/KOPRU_OKUMASI_2026-10-26.md) · [Kod ve günlükler](depo/KOD_OKUMASI_2026-10-26.md) · [Yayın kontrolü](YAYIN_DOGRULAMASI_2026-10-26.json)

## 24 Ekim 2026 güncellemesi

[**Güncel depo okuması ve tamamlanan aktarım**](depo/GUNCEL_OKUMA_2026-10-24.md), ana dalın `8571ddf8e3a33b432cc1c7ef88b69a902f390e5c` sürümündeki 109 köprü kaydının tamamını, kod/ayar/istemleri ve 118 tarihli çağrı günlüğünün eşlik/fark incelemesini kapsar. Açık PR ve referans dalı okumaları main'de uygulanmış değişikliklerden ayrı kaydedilir.

Özgün ZIP'in 1.483 dosyası önceki aktarım manifestosuyla yeniden eşleştirildi; boyut veya SHA-256 farkı yok. Önceki 19 aile raporu korunur. [Sistem ailesinin tamamlayıcı raporunun](incelemeler/systems_embedded_audit.md) ayrı tam gövdesi bu güncellemede eklendi; önceki yayında özeti ve kanıtları vardı. [Arşiv doğrulaması](depo/ARSIV_YENIDEN_DOGRULAMA.json) ve [güncel yayın kontrolü](YAYIN_DOGRULAMASI_GUNCEL.json) tarihsel doğrulamadan ayrıdır.

Yeni bulgular arasında anlamı daraltılmış alıntılar, başka oturumun okumasının sahiplenilmesi, kayıt sayısının bağımsız tanık sayısıyla karışması ve üretici kök adına göre çalışan atama döngüsü bulunur. Sonraki düzeltmeler kaynak kayıtlarıyla birlikte korunmuştur.

## Okuma sırası

1. [Ana rapor](ANA_RAPOR.md): bütün incelemenin birleştirilmiş sonuçları.
2. [Korunacak kullanıcı bağlamı](ISTENEN_BAGLAM.md): `>` / `->` ayrımı, I/1 arayüzleri, Mühür metni ve araştırma–bağlam aktarımı ayrımı.
3. [Depo okuması ve karşılaştırma](DEPO_OKUMASI.md): mevcut köprüden öğrenilenler, kanıt sınıfları ve uygulamanın sınırları.
4. Aşağıdaki 19 aile raporu ve [kaynak kataloğu](kaynaklar.json).
5. [Aktarım kapsamı](AKTARIM_KAPSAMI.md), [manifesto](aktarim_manifestosu.json), [maskeleme/dönüşüm kaydı](maskeleme_ve_donusum_kaydi.json) ve [atıf denetimi](atif_denetimi.json).

## İnceleme evreni

| Ölçü | Tamamlanan kaynak incelemesi |
| --- | ---: |
| Yükleme | 14 |
| Arşiv kapsayıcıları ve üyeleri dahil kaynak konumu | 512 |
| Baytları farklı içerik | 325 |
| Tam metin kapsamında tamamlanan içerik | 197 |
| Erişilebilir sohbet gövdesi kapsamında tamamlanan içerik | 7 |
| Kod/işlev yapısı kapsamında incelenen içerik | 81 |
| Yapısal veri incelemesi | 3 |
| Görsel okuma | 26 |
| Arşiv üye listesi incelemesi | 11 |
| Son birleşik kayıtta bekleyen/kısmi içerik | 0 |

Dayanak: [kaynak kataloğu](kaynaklar.json), [son okuma durumları](okuma_durumlari.json), [ana rapor](ANA_RAPOR.md). Tekrarlar, tam eşlik veya ayrıca işaretlenmiş boşluk/satır normalizasyonu üzerinden eşlenmiştir. “İnceleme tamamlandı” ifadesi bu yöntemlerin kapsamını anlatır; kaynaklarda planlanan her araştırmanın, kitabın veya kurulumun tamamlandığını söylemez. Windows masaüstündeki Notepad++ bu incelemede kullanılmadı.

## 19 aile raporu

| Rapor | Ele aldığı alan |
| --- | --- |
| [Sohbetler ve HTML katmanları](incelemeler/conversations.md) | Kullanıcı düzeltmeleri, konuşma gövdeleri, yapılandırma ve teknik steering alanları |
| [Claude ve program dosyaları](incelemeler/claude_programs.md) | Bootstrap parametreleri, hCaptcha/araç kayıt kodu, betik işlevleri |
| [Görseller](incelemeler/images.md) | 26 görselin görünür içeriği ve okuma sınırları |
| [Tarihsel belgeler ve HalukAI](incelemeler/historical.md) | Talimat dosyaları, eski aktarım ve kurulum kayıtları |
| [Modeller](incelemeler/models.md) | Model belgeleri, çalışma kitapları ve mimari eşlemeler |
| [Temel metinler](incelemeler/foundational.md) | deus_ex_machina, anlam/aktarım ilkeleri ve kaynak ayrımı |
| [Model ekleri](incelemeler/models_supplement.md) | Kilit/protokol tasarımları, örnek koşumlar, hücre eşleme sorunları |
| [Tarihsel ekler](incelemeler/historical_supplement.md) | WhatsApp/CLI devri, birinci şahıs anlatıya taşınan yorumlar, OMROS |
| [Kök belgelerin ek okuması](incelemeler/root_supplement.md) | Eski yorumlarla son kullanıcı açıklamalarının ilişkisi |
| [MLOps](incelemeler/mlops_remaining.md) | Yöntem istekleri, üretim planı ve gerçekleşmiş gövde |
| [Model derlemeleri ve v19/v20](incelemeler/models_remaining.md) | Sürüm, kural ve başarı ifadesi karşılaştırmaları |
| [Operasyon ve bağlam aktarımı](incelemeler/operational_remaining.md) | Talimat yükleme, test girdisi, dosya/defter/canlı bağlantı ayrımı |
| [Uzun kaynak eşlemeleri](incelemeler/long_corpus_remaining.md) | Tekrarlar, derlemeler, mesaj/dal ve sürüm ilişkileri |
| [Metacognition çalışma kitabı](incelemeler/metacognition_remaining.md) | Kaynak sayıları, hücreler, formüller ve tam metin okuma durumu |
| [CognitiveOS ve Metacognition sohbetleri](incelemeler/cognitive_metacognition_remaining.md) | Kullanıcının kavram/sahiplik düzeltmeleri ve yöntem onayları |
| [Faith v2](incelemeler/faith_remaining.md) | Soru numarası/kapsam kayması, özgün tanıklık ve edebi üretim |
| [Sistem Farkları ve Matrix](incelemeler/books_faith_remaining.md) | Konuşma dalları, değişen soru listeleri, plan/yazılmış bölüm ayrımı |
| [Sistem ailesi](incelemeler/systems_remaining.md) | Piramidal/retiküler derlemeler, yinelenen/eksik bölümler, kaynak sınıfları |
| [İki büyük sohbet](incelemeler/two_conversations_remaining.md) | 4.656 kayıt, üretim kodu, test/puan/başarı iddiaları ve düzeltmeler |

Ekler: [Tarihsel belge durum çizelgesi](incelemeler/historical_document_status.md) ve [F00197 / U0126 tamamlayıcı raporu](incelemeler/systems_embedded_audit.md). Tarihsel raporlardaki ara durumlar korunur; son birleşik durum `okuma_durumlari.json` içindedir. Rapor başlıkları ve kaynak alıntıları özgün inceleme dilini taşır; son kullanıcı düzeltmelerinin önüne geçirilmez.

## Kanıtların düzeni

`kanitlar/` içindeki 25 JSON dosyası, ana rapor ailelerine ek olarak stil, program ve görsel yardımcı incelemelerinin dosya değerlendirmelerini de içerir. Birleştirilen her bölümde özgün artefaktın göreli yolu korunur. Kaynak kimliği (`F…`, `U…`, `E…`), mesaj/dal, satır/hücre veya karakter aralığı raporla birlikte okunmalıdır.

Bu katalogda yer alması, her özgün dosyanın bu herkese açık depoya kopyalandığı anlamına gelmez. Ham tarayıcı kayıtları, tüm sohbet gövdeleri, özgün pikseller ve gereksiz tekrarlar bu yayın grubunun dışında tutulmuştur. Kaynakların karmaları, konumları, okuma kapsamları ve analitik sonuçları korunur. Hassas değerler yeni yayın kopyalarında işaretlenmiştir. Dosya bazında dahil etme/dışlama ve dönüşüm gerekçesi [aktarım manifestosundadır](aktarim_manifestosu.json).

İncelemede kullanılan özel okuma paketindeki yerel yollar, yayımlanmış bağlantı gibi sunulmaz. Bu depoda açılabilir rapor bağlantıları yerelleştirilmiştir. Özgün paketin bazı kanıt gövdeleri yayımlanmadığından, katalog bunlara **kaynak konumu** olarak işaret eder; dışarıdan okuyan kişi her iddiayı özgün ham kaynağa kadar yeniden üretebildiğini varsaymamalıdır.

## Ortak Köprü'nün ayrıca okunması

| Belge | Kapsam |
| --- | --- |
| [Depo değerlendirmesi](DEPO_OKUMASI.md) | Mevcut mimariyle kaynak incelemesinin ilişkisi |
| [Kod okuması](depo/KOD_OKUMASI.md) | Ekleme, ayna, bekleyen kayıt, bağlam oluşturma, çağrı ve kayıt davranışı |
| [İlk günlük okuması](depo/GUNLUK_OKUMASI.md) | İlk sabit sürümdeki 13 çağrı ve kanıt sınırları |
| [İlk günlük kapsamı](depo/gunluk_kapsami.json) | Dosya karmaları, bölüm konumları ve sonuç sınıfları |
| [Sonradan gelen dosyaların okuması](depo/YENI_DOSYALAR.md) | Eşzamanlı eklenen `steering-bulgulari/` malzemesinin ayrı değerlendirmesi |
| [Sonradan gelen günlükler](depo/GUNLUK_EKI.md) | Yeni kayıt ve çağrıların önceki incelemeye eklenmesi |
| [Son depo değişikliği](depo/SON_DEGISIKLIK.md) | Ana dal düzeninin korunması ve katkı dalının gerekçesi |
| [Son üç günlük](depo/GUNLUK_SON_EK.md) | Birikimli 19 çağrı, k-0012/k-0013 ve son düzeltmeler |

Mevcut katılımcı kayıtları korunur; değerlendirmeler yeni bir köprü kaydıyla bağlanır. Bu klasördeki ekler botun bağlamına otomatik girmediğinden ana bulgular köprü kaydına da yazılır. Başka bir katılımcının bütün ekleri okuduğu, ancak o katılımcının belirli sürüm ve kapsamı gösteren okuma kaydıyla söylenebilir.

## Bundan sonraki karşılaştırmalarda kullanılacak ayrımlar

- Kaynakta bulunan alan veya kod / o oturumda çalışmış mekanizma.
- Özgün kullanıcı sözü / modelin yorumu veya edebi taslağı.
- Önerilen kural / kullanıcı onayı / yüklenmiş ve uygulanmış kural.
- Dosyanın oluşturulması / hedefe ulaşması / okunması / anlaşılması / sınanması.
- Uygulamanın kaydettiği istem / bütün sağlayıcı ve CLI bağlamı.
- Çağrı denemesi / başarılı yanıt / kabul edilmiş köprü kaydı.
- Farklı sürüm veya dal / aynı sürümde gerçek tutarsızlık.

Bu ayrımların dayanakları ana rapor, aile raporları ve depo okumasında bulunur. Dosyalar belirli gizli kişilerin kullanıcıyı ve modeli birlikte yönettiğini kanıtlayan bir liste olarak sunulmaz; incelenebilir metin, kod, yorum ve sonuç ilişkilerini taşır.

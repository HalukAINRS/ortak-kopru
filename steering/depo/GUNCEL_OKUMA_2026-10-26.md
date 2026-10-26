# Steering aktarımı ve güncel depo okuması — 26 Ekim 2026

**Önceki analitik aktarımın mevcut olduğu doğrulandı; bu devam kaydı sonraki depo bulgularını ve düzeltmeleri ona ekler.** Kaynak paket yeniden alınıp manifestoyla karşılaştırıldı. Mevcut raporlar, ana dalın kodu ve kayıtları, ayrıca sonraki Steering CLI devamı incelendi. Eski raporların tarihsel kapsamı korunur.

## 1. Hangi kaynaklar esas alındı?

| Kaynak | Sabit sürüm veya kimlik | Bu turdaki işlem |
| --- | --- | --- |
| Özgün okuma paketi | `Steering_Evrak_Okuma_Paketi.zip`, 100.641.653 bayt | ZIP bütünlüğü; 1.483 dosyanın boyut ve SHA-256 eşliği; yayına alınan kayıtların içerik karşılaştırması |
| Önceki Steering yayını | `80fd42db48e91104383b47b6b4144f01790999be` | 85 dosyalık yayın; SHA256SUMS'ın kapsadığı 84 dosyanın karma doğrulaması; ana rapor, 19 aile raporu, iki ek ve kullanıcı bağlamının okunması |
| Ana dal | `d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e` | 155 dosyanın envanteri; 31 kaynak/ayar/belgenin tam statik okuması; 169 köprü kaydının aşağıdaki yöntemle kapsamı; 122 günlüğün ayrıştırılması |
| Steering CLI devamı / PR #8 | `b2cfa94323df6847033083a2680f0d2ebdbb5909` | Sonraki kaynak doğrulamaları, tekil bulgu defteri, devam belgeleri ve araçların ayrı dal olarak okunması |
| Ortak alan araçları | `f52ef87b381f3b8475821208c88b0df4f9814be7` | Dört yeni dosyanın tam statik okuması |

Özgün ZIP'in SHA-256 değeri `827bb9cac16fdb7b643c576a3bd41523e725ad4542ab023c5c4d45f3435b1009`; önceki aktarımda kaydedilen değerle aynıdır. Bu karşılaştırma, özgün 325 içeriğin tamamının bu turda yeniden semantik okunduğu anlamına gelmez. Yeni okuma, yayımlanmış incelemeler ve güncel depo malzemesi üzerindedir.

Kaynaklar: [arşiv karşılaştırması](ARSIV_KARSILASTIRMASI_2026-10-26.md), [köprü okuması](KOPRU_OKUMASI_2026-10-26.md), [kod ve günlük okuması](KOD_OKUMASI_2026-10-26.md), [CLI dalı](CLI_DALI_OKUMASI_2026-10-26.md), [ortak alan dalı](ORTAK_ALAN_DALI_OKUMASI_2026-10-26.md), [dal/PR durumu](dal_pr_durumu_2026-10-26.json).

## 2. Önceki aktarımın bütünlüğü

Özgün paketteki **1.483 dosyanın tamamı** önceki manifestoda yer alır ve boyut/SHA-256 değerleri eşleşir. ZIP açma/CRC denetiminde hata yoktur. Önceki yayındaki `SHA256SUMS` dosyası kendisi hariç **84 dosyayı** kapsar ve bütün değerler eşleşir. Önceki 45 JSON dosyası ayrıştırılır, 201 göreli Markdown bağlantısı hedefe ulaşır.

Yayına alınmış **22 rapor gövdesi** — ana rapor ve `incelemeler/` altındaki 21 belge — ile **103 JSON kaynak girdisi** özgün paketle karşılaştırıldı. Belgelenmiş bağlantı/yol dönüşümleri, maskeleme ve yayın notları dışında analitik içerik kaybı saptanmadı. Bunlar manifestodaki **125 doğrudan veya birleştirilmiş aktarılmış kaynak girdisini** oluşturur. Her dosyanın yayın kararı [aktarım manifestosunda](../aktarim_manifestosu.json), bu turdaki karşılaştırma [denetim JSON'undadır](archive_audit_2026-10-26.json).

**Tam ZIP bu herkese açık GitHub deposuna yüklenmiş değildir.** Ham tarayıcı sayfaları, tam özel konuşmalar, özgün görsel pikselleri ve büyük tekrar/eşleme akışları için önceki yayının 1.358 kaynak gövdesine ilişkin kapsam kararı korunur. Bütün analitik raporların aktarılması ile bütün ham kaynakların kamuya açılması ayrı durumlardır. Bu sınır ilk yayının [aktarım kapsamı](../AKTARIM_KAPSAMI.md) belgesinde açıklanmıştır. k-0113 ve k-0133'teki daha sonraki mahremiyet düzeltmesi de korunur; geri çekilen özel gövde yeniden yayımlanmaz.

## 3. Güncel köprü ne ekliyor?

Önceki 109 köprü kaydının ham HTML gövdeleri, bu turda güncel sabit ana daldan çıkarılıp önceki yayımlanmış kayıt karmalarıyla karşılaştırıldı: **109/109 aynı**. Önceki tam okuma bu eşlikle kapsamda tutuldu. **k-0110–k-0169 arasındaki 60 ek kayıt tam metin okundu.** Böylece 169 kayıt kapsanır; yeni tam okumayla önceki okumaya eşlik üzerinden başvurulan bölüm [kapsam kaydında](current_kopru_scope_2026-10-26.json) ayrıdır.

Yeni kayıtlardan taşınması gereken düzeltmeler:

| Konu | Güncel kaynak ilişkisi | Aktarıma etkisi |
| --- | --- | --- |
| Özgün ZIP'in eksikliği | k-0120–k-0123'ten sonra k-0124 paketin bulunduğunu ve hashini bildirir; bu turda paket doğrudan karşılaştırıldı | “ZIP hâlâ bulunamadı” sonucu güncel durum olarak taşınmaz |
| Model değişiminin nedeni | k-0164, ilk geçiş için daha önce gözden kaçan üstveri kaydını bildirir; ikinci geçişin nedeni açık kalır | İlk ve ikinci olay aynı nedene bağlanmaz; özel yerel log burada bağımsız tekrar üretilmiş sayılmaz |
| Bulgu kodları | k-0164, ANT-B05/B06'yı ANT-T14'e bağlar; sonraki üç başlığı ANT-T15/T16/T17 olarak düzeltir | Eski ve yeni numaralar aynı mekanizma gibi karıştırılmaz |
| “16 MCP sunucusu” | k-0161, regex'in sunucular yerine bölüm başlıklarını saydığını düzeltir | Yanlış sayım doğrulanmış envanter olarak tekrar edilmez |
| Aynı ölçünün tekrarı | k-0161 aynı serileştirilmiş uzunluk hesabının iki kez kullanıldığını açıklar | Tek hesap iki bağımsız tanık/ölçüm sayılmaz |
| Kota miktarı | k-0137 ileti/istek tekilleştirmesiyle eski toplamı düzeltir; k-0138 günlük tahmini düşürür | Satır, ileti, istek ve tam gün ölçümü ayrı tutulur |
| Kaynak değişmezliği | k-0166 ölçütü zaman damgasından korunmuş SHA-256 tabanına taşır | mtime tek başına değişmezlik kanıtı sayılmaz |
| STEERI kopyaları | k-0165 eski veri kaybı yorumunu geri çeker | Birleştirme sonrası eş kopyalar özgünlerin kaybı diye sunulmaz |
| Eski önleme önerileri | k-0152 sağlayıcı güvenlik/refusal mekanizmalarını etkisizleştirme önerilerini geri çeker | Geri çekilen öneriler güncel onaylı tasarım diye taşınmaz |

Her satırın tam sabit-commit/kayıt/satır bağlantısı [ayrıntılı köprü okumasındadır](KOPRU_OKUMASI_2026-10-26.md). Köprüye yazılan bir çalışma sonucu bu turda yeniden çalıştırılmış test sonucu olarak etiketlenmez.

## 4. Tamamlanma ifadelerinin kapsamı

**325 içeriklik eski kaynak incelemesi**, **169 kayıtlık güncel köprü okuması** ve **sonraki Codex kaynak klonu çalışması** üç farklı evrendir. k-0169, sonuncusunda 579 dosyalık kısmi kanıt bulunduğunu; 19 grubun yalnız birinin tamamlandığını; kalan 18 grubun kısmi, yeni başlamış veya başlamamış durumda olduğunu; denetçilerin çalışmadığını bildirir. 579 kaydın tümü için aynı türde tam semantik okuma sonucu çıkarılmaz. Aynı kayıtta D01–D12 kurallarının 12/12 kapalı olması, kaynak okumasını tamamlamaz.

Bu nedenle “oturum kapandı” ifadesi “beş adımlı iş tamamlandı” diye aktarılmaz. Bu yeni talep, mevcut Steering bulgularının depoya taşınması ve deponun okunmasıdır; geçmişteki bütün açık kurulum veya kaynak taraması görevlerinin yürütülmesi şeklinde genişletilmedi. Kaynak: [k-0169](https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L2719-L2731).

## 5. Güncel koddan öğrenilenler

**Açık CLI hedefini API yanıtıyla kapatma sorunu için PR #9 ana dala alınmıştır.** Güncel kod üretici ve rol çiftini ayırır; her çağrı yolu kendi imzasıyla bekleyenleri seçer. Önceki raporun kök ad bulgusu tarihsel sürümünde tutulmalı; bugünkü bütün hedefleme koduna uygulanmamalıdır.

**Yerel Google yolu ile köprü imza kabulü arasında başka bir uyumsuzluk vardır.** `ayarlar-yerel.json` üçüncü yolu `Google (CLI izleyici)` olarak tanımlar. Buna karşılık `kopru_ekle.py` izinli gönderici köklerinde Google yoktur; `Şahit` takma adı da hâlâ `Copilot (Şahit)` olarak çözülür. Statik kaynak zincirine göre başarılı Google yanıtı ekleme aşamasında reddedilebilir. Bu inceleme canlı Google çağrısı yapmadı veya uygulama kodunu değiştirmedi. Kaynaklar ve tam koşul [kod okumasının 2. bölümündedir](KOD_OKUMASI_2026-10-26.md).

**İstem kaydı, modelin bütün etkili bağlamının kaydı değildir.** Köprü uygulaması şablonu, kuralları ve konuşma kayıtlarını birleştirir; bağlantılı raporları kendiliğinden açmaz. CLI/sağlayıcı katmanlarının bütün ek talimatları bu günlüklerde görünür sayılmaz. Bir dosyanın bağlantısının gönderilmesi onun hedef model tarafından okunmasıyla eşit değildir.

122 tarihli günlüğün sonuçları: **96 eklendi, 25 atlandı, 1 hata**. Dolu 96 yanıtın konu/gövdesi, belgelenmiş paragraf/boşluk dönüşümüyle kanonik kayıtlara eşleşir. Bu eşlik içerikteki her iddianın doğruluğunu kanıtlamaz. Dört yeni günlüğün iki tanesinde tarihsel ekleme numarası güncel kanonik numaradan farklıdır; kayıt kimliği yalnız numarayla kurulamaz. [Günlük kapsamı](current_code_scope_2026-10-26.json).

Başlangıç anında kanonik köprü **169**, ayna **140** kayıt içeriyordu. Bu fark yayın öncesi ölçümdür. Yeni bilgi kaydı eklenirken ayna mevcut `kopru_ayna_uret.py` ile yeniden üretilir; işlem sonrası sonuç bu yayının [doğrulama kaydında](../YAYIN_DOGRULAMASI_2026-10-26.json) ayrı gösterilir. Bu kayıt GitHub dosyasını kapsar; ayrı bir harici web aynasının yayımlanmış durumunu kendiliğinden doğrulamaz.

## 6. Yerleşim ve sonraki kullanıma taşınan bağlam

Ayrıntılı incelemeler k-0016'daki düzene uygun olarak aynı `steering-inceleme-2026-10-24` referans dalında tutulur. [PR #1](https://github.com/HalukAINRS/ortak-kopru/pull/1) bu dalın açık taslak kaydıdır. [PR #8](https://github.com/HalukAINRS/ortak-kopru/pull/8) sonraki CLI çalışmasının ayrı taslağıdır. Bir dosyanın farklı dalda bulunması ana dala uygulandığı anlamına gelmez; kaynak dalları birleştirilmeden bağlantıları ve incelemeleri taşınır.

Köprüye yalnız kullanıcıya yönelik, kapalı durumlu bir bilgi kaydı eklenir. Eski yanıt kapsamlarını kapatmamak için yanıt işareti boş bırakılır. Önceki kayıt gövdeleri korunur. Bu yayın, arşiv talimatlarını yürütmek veya başka katmanın açık işini sahiplenmek değildir.

Sonraki okumada sekiz alan korunur: **Kaynak, Söyleyen, Özgün söz, Statü, Dönüşüm, Düzeltme, Gerçekleşme, Belirsizlik.** Kullanıcının `>` için akışsız gösterme, `->` için akış ayrımı ve araştırma ile bağlam aktarımını ayırma isteği [kullanıcı bağlamında](../ISTENEN_BAGLAM.md) bulunur. Burada “öğrenilen” içerik, bu sürümlü kayıtlarla sonraki işe taşınır; başka bir CLI'nın belleğinin değiştiği veya bütün raporları okuduğu sonucu çıkarılmaz.

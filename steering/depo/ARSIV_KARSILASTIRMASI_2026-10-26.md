# Steering arşivi ile yayımlanmış incelemenin karşılaştırılması — 26 Ekim 2026

**Sonuç:** Kaynak paket, depodaki aktarım manifestosuyla eksiksiz eşleşiyor. Yayımlanmış 125 kaynak kaydının tamamı karşılığında bulundu: 22 rapor gövdesi ve 103 JSON içeriği, kayıtlı yayın dönüşümleri dışında korunmuş. Yeni bir eksik analitik rapor gövdesi saptanmadı. Bunun anlamı bütün ham arşivin GitHub'a yüklenmiş olması değildir; yayının kapsamı analitik raporlar, seçilmiş kanıtlar, kaynak katalogları ve durum kayıtlarıdır.

Karşılaştırmanın sabit sürümü: [`80fd42db48e91104383b47b6b4144f01790999be`](https://github.com/HalukAINRS/ortak-kopru/tree/80fd42db48e91104383b47b6b4144f01790999be/steering), `steering-inceleme-2026-10-24` dalının bu inceleme başında görülen başı. Buradaki sonuçlar bu sürüme aittir. Güncel ana daldaki daha sonraki köprü düzeltmeleri ayrı depo okumasında değerlendirilmelidir.

## Karşılaştırılan kaynak

`Steering_Evrak_Okuma_Paketi.zip`: **100.641.653 bayt**, SHA-256 **`827bb9cac16fdb7b643c576a3bd41523e725ad4542ab023c5c4d45f3435b1009`**. Paketin 1.483 dosya üyesi, sıkıştırılmamış olarak 460.800.693 bayttır. Her üye açılarak CRC denetiminden geçti; dosya boyutları ve SHA-256 değerleri [aktarım manifestosundaki](https://github.com/HalukAINRS/ortak-kopru/blob/80fd42db48e91104383b47b6b4144f01790999be/steering/aktarim_manifestosu.json) kendi kaydıyla karşılaştırıldı. Paket veya özgün kaynaklar değiştirilmedi.

| Denetim | Sonuç |
| --- | ---: |
| ZIP üyesi / manifestodaki benzersiz kaynak yolu | 1.483 / 1.483 |
| Boyut ve SHA-256 eşleşmesi | 1.483 / 1.483 |
| Manifestoda bulunmayan veya ZIP'te eksik üye | 0 |
| Sabit sürümde yayımlanmış dosya | 85 |
| `SHA256SUMS` eşleşmesi | 84 / 84 |
| Geçerli JSON dosyası | 45 / 45 |
| Çözümlenen göreli Markdown bağlantısı | 201 / 201 |
| Aktarılan kaynak kaydı | 125 / 125 |
| Kaynak gövdesi korunan rapor | 22 / 22 |
| JSON yapısı/değerleri korunan kaynak kayıtları | 103 / 103 |
| Dışarıda bırakılmış rapor JSON'larında aynı metni taşıyan `text` alanı | 22 / 22 |
| Açık karşılaştırma sorunu | 0 |

`SHA256SUMS` kendi kendisini listelemediği için dosya sayısı 85, listelenen karma sayısı 84'tür. Bağlantı denetimi yerel Markdown hedefinin dosya/dizin olarak bulunmasını doğrular; dış web bağlantılarının erişilebilirliğini veya her bölüm çapasını doğrulamaz.

## Rapor ve JSON korunumu

22 raporun 18'inde özgün rapor gövdesi yayın notundan sonra birebir bulunuyor. Dört raporda yalnız [dönüşüm kaydında](https://github.com/HalukAINRS/ortak-kopru/blob/80fd42db48e91104383b47b6b4144f01790999be/steering/maskeleme_ve_donusum_kaydi.json) açıklanan işlemler var: ana rapordaki Page bağlantılarının depo raporlarına yöneltilmesi; tarihsel ve model raporlarındaki yerel kök yolunun `[ARSIV_KOKU]/` olarak etiketlenmesi; operasyon raporundaki iki eski sandbox bağlantısının kaynak konumu açıklamasına çevrilmesi. Bu işlemler hesaba katıldığında 22 gövdenin tamamı korunuyor.

103 JSON kaydı; 95 analitik/kanıt/kapsam kaydı, dört özgün paket doğrulaması, üç kaynak kataloğu ve bir son okuma durumudur. 99 birleştirilmiş nesnenin anahtarı ve özgün SHA bilgisi denetlendi. Bunların 67'si ayrıştırılmış veri olarak dönüşüm öncesinde de eşitti; diğerleri kayıtlı yol etiketleme ve değer maskelemesinden sonra eşleşti. Kataloglar ve son okuma durumu da aynı dönüşümlerle karşılaştırıldı. Son okuma durumuna eklenen `publication_notice`, kaynak verisinin yerine geçen bir değişiklik olarak sayılmadı.

Bu karşılaştırma, maskelenmiş özgün değerleri yeniden yayımlamaz. Raporların içeriği, kaynak köklerinin ve bağlantıların yer değiştirmesi nedeniyle bayt olarak farklı olabilir; bu farkın açıklanmış olması ile kaynak dosyalarının kendisinin bayt eşliği ayrı sonuçlardır.

## GitHub yayınının kapsamı

[Aktarım kapsamı](https://github.com/HalukAINRS/ortak-kopru/blob/80fd42db48e91104383b47b6b4144f01790999be/steering/AKTARIM_KAPSAMI.md), 125 kaynağın doğrudan veya birleştirilmiş aktarıldığını, 1.358 kaynağın tam gövdesinin yayımlanmadığını açıkça söylüyor. Bu sayılar yeniden doğrulandı.

| Yayımlanmayan gövde sınıfı | Sayı |
| --- | ---: |
| Ham kaynak tam metni veya tam sohbet türevi | 1.199 |
| Aynı içeriğin sunum tekrarı veya paket dizini | 69 |
| Kaynak gövdesi veya yinelenen okuma/eşleme akışı | 63 |
| Özgün görsel pikselleri | 26 |
| Ayrı işletim dizini/yinelenen kopya | 1 |
| **Toplam** | **1.358** |

Kaynak paket içindeki hiçbir bağımsız Markdown rapor bu kapsamın dışında kalmamış. Dışarıda bırakılan 22 rapor JSON'unun `text` alanları, yayımlanan raporların kaynak metinleriyle birebir aynı. Büyük okuma planlarının, mesaj dökümlerinin, hücre/eşleme akışlarının ve piksellerin tamamı GitHub'a kopyalanmış değildir. Kaynak gövdelerine kadar bağımsız yeniden üretim yapmak isteyen kişi tam özel pakete ihtiyaç duyar; yalnız yayımlanan raporları okuyarak bu erişime sahip olduğu varsayılmamalıdır.

## Bu görevde yeniden okunan incelemeler

Ana rapor, `ISTENEN_BAGLAM.md` ve `incelemeler/` altındaki 21 Markdown dosyasının tüm gövdeleri bu görevde yeniden okundu. Toplam 23 metin **414.748 karakterdir**. Altı metni ana inceleme, aşağıdaki 17 metni arşiv karşılaştırma incelemesi okudu. Uzun çıktıların kesilen bölümleri ayrıca küçük aralıklardan tamamlandı. Bu, yayımlanmış raporların yeniden okumasıdır; 460,8 MB ham kaynak içeriğinin veya özgün piksellerin yeniden baştan sona okunduğu iddiası değildir.

| Rapor yolu (`steering/incelemeler/`) | Korunacak temel sonuç |
| --- | --- |
| `books_faith_remaining.md` | Sistem Farkları ve Matrix çalışmaları görünür kullanıcı yöntemini taşır. Matrix'te aynı daldaki 31–40 soru numaraları altında konu değişir; başka dalda kullanıcının karakter/soru eşlemesini düzeltmesi ayrıca korunur. Planlanan kitap ve ekler, tamamlanmış gövdelerle eşit değildir. |
| `cognitive_metacognition_remaining.md` | OMROS/CognitiveOS sahipliği ve “suç” sözcüğüne verilen anlam kullanıcı tarafından düzeltilmiştir. Metacognition'daki 90/97 farkı, 90 çekirdek + 7 destek kapsamıyla açıklanır; aynı sürüm adlarının farklı dallardaki gövdeleri aynı işlem zinciri sayılamaz. |
| `faith_remaining.md` | Özgün soru listesiyle sonraki aynı numaralı yanıtlar arasında kapsam değişimi bulunur. Asistanın birinci kişiyle ürettiği sahneler özgün kullanıcı tanıklığına dönüşmez. Kullanıcının sürüşle ilgili açık düzeltmesi sonraki aktarımda korunmalıdır. |
| `foundational.md` | 13, 25 ve 34 parçalı rehberler farklı kapsamlardır. Metin, kılavuz ve çalışan düzen birbirinden ayrılır. Defterin güncel yön kararı eski “Parça 4'ten devam” notunu tarihsel kılar. |
| `historical.md` | Bağımsız AGENTS/skill belgeleriyle kurulum betiklerinin gömülü metinleri farklı olabilir. `STEERING_ROLE` değişkeninin varlığı, modelin onu okuyan bir tüketici yoluna sahip olduğunu göstermez. Bu raporun ilk kısmi okuma kuyruğu tarihsel ara durumdur. |
| `historical_supplement.md` | OMROS ham kayıt ile yapılandırılmış aktarımı birlikte korumayı önerir. WhatsApp devir metninde modelin eklediği ayrıntılar kullanıcı sözü görünümü kazanır; “Steering kapalı” sözü ayar değişikliği kaydıyla desteklenmez. |
| `long_corpus_remaining.md` | Koşullu eşlik, bağlı kaynak okunmadan tamamlanmış okuma sayılamaz. U0194, 53 web dosyası bloğu ile ayırıcı boşlukların doğrulanmış birleşimidir; yeni sohbet gövdesi değildir. |
| `metacognition_remaining.md` | 97 kaynak ve 90 çekirdek kapsamı ayrıdır; 19 kısmi erişim kaydına karşı 18 takip kaydı ayrı bir eksikliktir. Hücre talimatları araştırma iş akışıdır; canlı model ayarı değildir. |
| `mlops_remaining.md` | `gizli_surec` etiketleri görünür kullanıcı mesajlarında yer alır. Kullanıcı üretim sistemini onaylar. Üretim bağlantıları ve teslim beyanları, yüklenmeyen eklerin içeriğini veya kitabın tamamlanmasını kanıtlamaz. |
| `models.md` | Model 1–4 rehberleri kaynak/denetim, doz/yön, dönüşüm/korunum ve kök sorular üzerinden çalışma biçimini yönlendirir. Şablonun zorunlu açık konu alanı ile “olmayan belirsizliği üretmeme” ilkesi arasında uygulama öncesi netleştirilecek fark vardır. |
| `models_supplement.md` | Dört Final çalışma kitabında `not_started` örneğiyle dolu puanlar ve `passed` önbelleği birlikte bulunur. CORE 02'de `required_locks` başlığı ile gerçek kilit sütunu kaymıştır. Bunlar somut hücre/formül ilişkileridir. |
| `models_remaining.md` | Mihver laboratuvarı ile test sayfalarında eksik sahiplik denetimi farklıdır. Dokuz sohbetin 260 karakterlik önizlemeleri tam sohbet değildir. OMROS v19/v20'de ham kaydı koruma ilkesiyle çelişen özet cümlesi sessizce yürütme kuralına çevrilmemelidir. |
| `operational_remaining.md` | “Yazıldı, okundu, anlaşıldı, uygulandı, ihtiyacı karşıladı” ayrı durumlardır. Aynı BEHAVIOR-01 kimliğinin farklı test girdileri için kullanılması ve verilmemiş alıntının sınanmış sayılması sonraki kayıtta düzeltilmiştir. |
| `root_supplement.md` | Eski yorumdaki belirsiz `>` işlevi, kullanıcının sonraki “akışsız gösterme” açıklamasının önüne geçirilemez. Kaynak envanterleri dosya varlığı/konumu ve hash ilişkisi taşır; canlı oturumun okuması değildir. |
| `systems_embedded_audit.md` | Tamamlayıcı rapor yalnız devraldığı 14–27 okuma paketinin kapsamını bildirir. Current/off-chain gövdeleri tek nihai kitaba karıştırılmaz. Yazım yönteminin nihai metinde adlandırılmaması görünür kullanıcı talebidir. |
| `systems_remaining.md` | Sohbette tamamlanmış 8.4 bölümü, DOCX/PDF derlemesinde 8.3 tekrarına dönüşmüştür. “Thoughts” etiketli sayı ile ana ASSISTANT yanıtı ayrı kaynak statüleridir. Literatür yakınsaması saha doğrulaması değildir. |
| `two_conversations_remaining.md` | Kullanıcı talebi, modelin revize ettiği protokol, üretilen dosya ve uygulanan durum ayrılmalıdır. Hedef toplama göre puan değiştiren kod ile gerçek formül adresi düzeltmeleri ayrı bulgulardır. Son tasarım teklifinin bulunması üretiminin bittiğini göstermez. |

Bu tablodaki bütün yollar [sabit inceleme dizininden](https://github.com/HalukAINRS/ortak-kopru/tree/80fd42db48e91104383b47b6b4144f01790999be/steering/incelemeler) açılır. Altı tamamlayıcı okuma: `ANA_RAPOR.md`, `ISTENEN_BAGLAM.md`, `incelemeler/historical_document_status.md`, `incelemeler/claude_programs.md`, `incelemeler/conversations.md`, `incelemeler/images.md`.

## Sonraki kayda taşınırken güncellik sınırı

Eski raporların “tamamlandı” ifadeleri, belirtilmiş kaynak evreninin o tarihte erişilebilir metin/görsel/yapı incelemesini anlatır. Sonradan açılan daha geniş kaynak okuma işi veya CLI uygulaması aynı tamamlanma durumunu devralamaz. Tersine tarihsel ara raporlardaki “kısmi” ifadesi de birleşik son okuma durumunu geriye çeviremez.

Kaynaklarda belirgin olan steering ilişkisi; sorunun kapsamının seçilmesi, kullanıcı sözünün yorumlanması, yorumun kurala dönüşmesi, dosya sürümleri ve başarının hangi kanıtla tanımlandığıdır. Belgeler kullanıcı düzeltmelerini ve düzeltilmiş hataları da taşır. Bu dönüşümler, belirli gizli kişilerin kullanıcıyı veya modeli kontrol ettiğini kanıtlamaz. Bu görevde tarihsel komutlar çalıştırılmadı, sağlayıcı ayarlarının değiştiği veya herhangi bir yönlendirme katmanının kaldırıldığı ileri sürülmedi.

## Tekrar üretme kapsamı

Makine karşılaştırması [denetim JSON'u](archive_audit_2026-10-26.json) ve aynı girdilere uygulanan [denetim betiği](audit_steering_archive.py) ile kaydedildi. Betik ZIP üyelerinin boyut/SHA/CRC değerlerini, sabit Git sürümündeki dosyaların karmalarını, JSON yapılarını, kayıt hedeflerini ve göreli dosya bağlantılarını karşılaştırır. Raporların yukarıdaki anlamsal okuması ayrı insan tarafından okunabilir değerlendirmedir; betiğin başarısı kendi başına bu yorumların doğruluğunu kanıtlamaz.

Depo kökünden, özgün ZIP yerelde mevcutken:

```bash
python3 steering/depo/audit_steering_archive.py --repo . --archive ../Steering_Evrak_Okuma_Paketi.zip --output archive_audit_2026-10-26.json
```

`--ref` varsayılanı bu raporun sabit yayın sürümüdür. Betik kaynak ZIP'i, kaynak dosyaları veya Git reflerini değiştirmez; yalnız belirtilen çıktı JSON'unu yazar. Bu görevde parametreli betiğin bir kez yeniden çalıştırılması, yukarıdaki denetim JSON'uyla bayt eşit çıktı verdi.

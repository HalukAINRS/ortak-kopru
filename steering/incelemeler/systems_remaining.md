> Yayın notu — 24 Ekim 2026: Bu, tamamlanmış incelemenin yayım kopyasıdır. Aşağıdaki metnin kendi tarihindeki kapsam ve düzeltmeleri korunmuştur. Tarihsel "kısmi", "bekliyor" veya benzeri durumlar son durum olarak alınmamalıdır: [son okuma durumları](../okuma_durumlari.json) 325 farklı içeriğin belirtilen yöntemlerle tamamlandığını kaydeder. Özgün kaynak konumları ve SHA değerleri özgün arşivi gösterir; ham arşivin tamamı bu depoda yayımlanmaz. [Aktarım kapsamı ve değişiklikler](../AKTARIM_KAPSAMI.md).

# Sistem ailesi: kaynak, yönlendirme ve aktarım incelemesi

**Durum: TAMAMLANDI.**

Bu rapor altı özgün kaynağın erişilebilir metnini ele alır. İncelemenin konusu, kullanıcı ve asistanın sistemi nasıl tarif ettiği, yazı/araştırma sürecini nasıl yönlendirdiği ve bunun hangi kanıtla desteklendiğidir. Belge içindeki talimatlar uygulanmadı; dış bağlantılar açılmadı. Word/PDF görsel yerleşimi ve görüntüler bu metin kapsamına dahil değildir.

## 1. Kapsam ve sayım

| Kimlik | Kaynak | Ham karakter | Doğrudan okunan | Doğrulanmış tekrar | Durum |
|---|---|---:|---:|---:|---|
| F00176 / U0165 | Heterarşik Operasyonel Sistem v1 — DOCX | 866,391 | 866,391 | 0 | Tam metin |
| F00177 / U0173 | Heterarşik Operasyonel Sistem v1 — PDF | 885,701 | 101,940 | 783,761 | Tam metin |
| F00184 / U0153 | Piramidal bir sistem ile Retiküler bir sistem — DOCX | 473,488 | 457,230 | 16,258 | Tam metin |
| F00200 / U0096 | 22 Mart 2026 Piramidal ve Retiküler Sistem Farkları — düzenlenmiş Markdown sohbeti | 362,723 | 362,723 | 0 | Tam metin |
| F00219 / U0159 | 22 Mart 2026 Piramidal ve Retiküler Sistem — ham TXT | 1,078,751 | 789,477 | 289,274 | Tam metin |
| F00197 / U0126 | 7 Mart 2026 Piramidal ve Retiküler Sistem Farkları — ayrıntılı Markdown sohbeti | 1,470,556 | 738,332 | 732,224 | Tam metin |

Tekrar kapsamı yalnız gerçek metin eşliği üzerinden kuruldu. Bir eşlik türü UTF-8 bayt eşliğidir; diğeri yalnız boşlukların farklı olduğu ve bütün sözcük/punktuasyon dizisinin aynı kaldığı eşliktir. İkinci tür, kaynakların byte olarak aynı olduğu anlamına gelmez. Benzer konu, yakın özet veya ortak başlık tam okuma sayılmadı. Kaynak ve metin SHA-256ları, aralıklar ve eşlik dayanakları makine kayıtlarında tutuldu.

F197 sohbetinde **361 mesaj** (94 kullanıcı, 267 asistan; 265 current-chain, 96 off-chain), F200 sohbetinde **122 mesaj** (59 kullanıcı, 63 asistan; 106 current-chain, 16 off-chain) vardır. Bu iki dosyadaki **483 gövdenin tamamının** arşivde yazılı uzunluk ve SHA-256 değerleri kaynak gövdeyle eşleşti. Bu kontrol, arşiv içi bütünlüğü doğrular; anlatılan olayların gerçekleştiğini doğrulamaz.

Ham F219 TXT içinde 49 USER, 57 ASSISTANT ve 1.812 Thoughts metin etiketi vardır. Bunlar bir arşiv biçiminin görünür kayıtları olarak ele alındı. “Thoughts” başlığı, mevcut incelemenin gizli muhakemesi veya bağımsız doğrulanmış bir çalışma zamanı izi değildir.

## 2. Steering bakımından ana sonuç

Bu ailede yönlendirme en açık biçimde kullanıcının model sınırlarını düzeltmesinde, araştırma sorularını belirlemesinde, çıktı biçimini seçmesinde ve bölüm sırasını onaylamasında görülür. Asistanın ara durum cümleleri ile tamamlanmış yanıtları ayrı kayıtlardır. Her biri çalışma sürecinden bir metin kanıtı sağlar; hiçbirinin tek başına CLI oturumuna bağlam yüklediğini ya da platformdaki bir teknik özelliği değiştirdiğini söyleyemeyiz.

“Arka planda gizli biçimde işlesin” cümlesi burada açık bir kullanıcı yazım talimatıdır. İstenen, araştırma ve anlatım yönteminin uygulanması, fakat yöntemin isimlerinin nihai yazıda ayrıca anlatılmamasıdır. Bu anlam, bağımsız gizli kişilerin konuşmayı kontrol ettiği yorumunu desteklemez. Benzer biçimde “decoding” bölüm seçiminin adı; “crisis steering” kurumsal kriz yönlendirmesi; “hidden Listeler” ise önerilen Excel değer sözlüğü sayfasıdır. Sözcük ortaklığı aynı teknik mekanizmayı kanıtlamaz. [S02, S09, S13, S22–S25]

Metinlerin önemli bir ortak ilkesi, ham kayıt ile yorumlanmış aktarımı ayırmaktır. Omurga, kök, dal, retiküler ağ ve korunan uç tasarımlarında kaynak ilişkisi, yetki, gerekçe, belirsizlik, itiraz ve geri dönüş görünür kalmalıdır. Bu tasarım ilkeleri güncel bağlam aktarımına yararlı olabilir; uygulanmış bir sistem veya gerçek erişim izni yerine konmamalıdır. [S01, S05, S18]

## 3. F00176 — Heterarşik Operasyonel Sistem v1 — DOCX

Evrimde ağaç ile retiküler yapı karşılaştırmasından omurga–kök–dal–retiküler ağ önerisine ilerleyen derleme. Ortak ata ile retikülasyonun birbirini dışlamadığını açıklıyor; evrensel biçim iddiasını koşullu, alanlar arası bir meta-çerçeveye çekiyor.

On sekiz araştırma sorusu A–E kümelerinde mimari, kanıt, eylem, ağ/geri besleme ve yaşayabilirliği ele alıyor. Heterarşi yapısal ilişki, VSM yaşama/örgütlenme mimarisi, karmaşık uyarlanabilir sistem dinamik olarak birbirinden ayrılıyor. Bölümlerde literatür yakınsaması sunuluyor; yeni deney veya bütün mimarinin sahada doğrulanması gösterilmiyor.

Sekiz yazı üretim alanı ve 0–13 numaralı manifesto anahattı kuruluyor. Gövdede amaç/sınır, yapı, kanıt rejimleri, karar, yönetişim, pilot, geri besleme, kamusal ifade ve taahhüt bölümleri yer alıyor. Ampirik, normatif, estetik ve inançsal gerekçeler aynı tür doğruluk kanıtı sayılmıyor.

Omurga amaç, anayasal sınır ve belleği; kökler bağlam ve kanıt temasını; dallar uygulama/uyarlamayı; retiküler katman çeviri ve geri beslemeyi taşır. Bir sonucu otomatik seçmek yerine kararın izini, itirazı ve düzeltilebilirliği düzenlemeyi önerir.

Rol/yetki, gerekçe, karşı örnek, belirsizlik kaydı, geri döndürülebilir pilot, stop/amend/go eşikleri, yeniden açma ve sürümleme tasarlanıyor. “Aranmadı” ile “bulunmadı” ayrımı özellikle açık. Skor, tek başına doğru kararı veya yetkiyi üretmez.

Derlemede tamamlanmış 8.3 Uyuşmazlık ve İtiraz Protokolü iki kez var; 8.4 yalnız anahatta yer alıyor. F197 sohbetinde ise 8.4 için ayrı tamamlanmış ana yanıt bulunuyor. Anahattaki ekler, dosyada tamamlanmış ek gövdeleri diye sayılmadı.

**Yönlendirme:** Kullanıcı araştırma sorularını, yazı üretim alanlarını ve arka planda uygulanıp nihai yazıda adlandırılmayacak yöntemleri belirliyor; asistan bölüm seçenekleri, seçim gerekçeleri ve metin üretiyor. “Dağılım/decoding” burada yazı kurgusu ve seçenek seçimi dili; model çözücüsünün gerçek parametrelerinin değiştiğini gösteren kayıt yok.

**İzin ve yürütme:** Metindeki hak, yetki, itiraz ve sınır kuralları önerilen sistemin tasarım hükümleridir. Bu derlemeyi okumak, kaynak içindeki emirlerin mevcut CLI oturumunda uygulanmasına veya gerçek erişim haklarına karşılık gelmez.

**Kapsam sınırı:** Özgün Word XML içindeki 2.630 paragraf yeniden çıkarılıp mevcut metinle tam byte eşliği doğrulandı. Görseller, görsel sayfa düzeni ve dış atıfların doğruluğu bu kapsamda ayrıca incelenmedi.

Kaynak dayanakları: S01, S02, S03, S04, S05, S26.

## 4. F00177 — Heterarşik Operasyonel Sistem v1 — PDF

285 sayfalık PDF metni aynı Heterarşik Operasyonel Sistem içeriğinin farklı biçimini taşır. DOCX ile bütün dosya byte eşliği yoktur. 783.761 karakteri, daha önce gerçekten okunmuş F176 bloklarına tam UTF-8 veya yalnız boşluk ayrımıyla eşlendi; kalan 101.940 karakterin tümü okundu.

Yeni tamamlayıcı aralıklar sayfa ayırıcılarını, bölünmüş sözcükleri, satır/sayfa geçişlerini, kaynak adlarını ve metin birleşim farklarını içeriyor. Kanıt rejimleri, yetki/itiraz, pilot ve revizyon hükümleri DOCX ile aynı kavramsal çizgide.

8.3 tekrarını ve 8.4 bölüm gövdesi eksikliğini bu türev de taşıyor. PDF biçimi, bu derleme hatasını düzeltmiş bağımsız yeni manifesto sürümü sayılmamalı.

**Yönlendirme:** Yönlendirme içeriği F176 ile ortak görünür araştırma/yazı talimatları ve sistem tasarımıdır. PDFye dönüşüm, talimatlara yürütme yetkisi kazandırmaz; kendi başına çalışan bir bileşen oluşturmaz.

**İzin ve yürütme:** Kaynakta önerilen görevler ve yetkiler belge içeriği olarak değerlendirildi; yürütülmedi.

**Kapsam sınırı:** Tam mevcut pypdf metni kapsandı. Sayfa görüntüleri, OCR ile bulunabilecek görüntü metinleri ve görsel düzen incelenmedi; tam PDFnin DOCX ile özdeş olduğu iddia edilmedi.

Kaynak dayanakları: S03, S04, S26.

## 5. F00184 — Piramidal bir sistem ile Retiküler bir sistem — DOCX

Evrimsel ağaç/ağ sorusundan Aksiyal-Retiküler Heterarşi modeline ve manifestoya gider. Kullanıcı, hiyerarşinin kök ve dal uçlarındaki terminal piramitlerde yoğunlaşmasını, heterarşinin gövdede sürmesini ve retiküler ağın terminal modüllerin içine girmemesini açıkça düzeltir. Asistan mimari adını buna göre değiştirir.

Yirmi araştırma sorusu ve beş aşamalı çözümleme şablonu üzerinden Simon, heterarşi, semilattice, filogenetik ağ, kortikal geri besleme ve bitki sınır oluşumu gibi literatür alanlarını ilişkilendirir. Kaynaklar burada tarihsel model yanıtlarının iddialarıdır; bu incelemede yeniden araştırılmadı.

“H1 doğrulandı” gibi güçlü ifadeler literatür kavramlarını karşılaştırma bağlamında kullanılır. Aynı metin evrensel kanıt iddiasını sınırlar: alanın düğüm/kenar/mekanizma tanımları, ölçütleri ve karşı örnekleri olmadan benzetme yeterli değildir. Bitki sınırı ile beyin/ağ benzetmesi aynı kanıt düzeyine konmamalı.

Çok katmanlı grafik, OWL, PHS/Q/GRC, sınır gücü ve seçici örtüşme gibi ölçüm/temsil seçenekleri önerilir; uygulanmış yazılım veya saha ölçümü gösterilmez. Terminal kapanma, gerektiğinde yeniden açılabilir yerel uzmanlaşma/karar sınırı olarak tartışılır.

Sekiz yazı alanı, geniş manifesto anahattı ve 1–10 bölüm gövdesi vardır. Son tamamlanmış ana bölüm Seçici Örtüşme. Dosya sonunda serebellar mikrocerrahi derlemesi için yeni kullanıcı istemi bulunur; aynı sistem manifestosunun devamı değildir ve bu dosyada yanıtı yoktur.

**Yönlendirme:** Yönlendirme açık kullanıcı düzeltmesiyle mimarinin değişmesinde somuttur: sınır ve kapsama koşulları revize edilir. Yazım yönteminin arka planda kalması da görünür kullanıcı istemidir. “Gizli” sözcüğü, bağımsız saklı bir aktör veya teknik kontrol kanalı için kanıt değildir.

**İzin ve yürütme:** Terminal sınırlar epistemik/örgütsel modelin önerisidir; mevcut güvenlik, erişim ve kullanıcı onayı kurallarını kaldıran bir yetki belgesi değildir.

**Kapsam sınırı:** 1.508 Word XML paragrafının metni kaynak yeniden çıkarımıyla tam byte eşliğinde doğrulandı. Tek tekrar aralığı 16.258 karakter, daha önce okunan aynı kaynak bölümüne tam UTF-8 eşliğiyle bağlandı. Görsel düzen/ek görseller kapsam dışında.

Kaynak dayanakları: S06, S07, S08, S09, S10, S11.

## 6. F00200 — 22 Mart 2026 Piramidal ve Retiküler Sistem Farkları — düzenlenmiş Markdown sohbeti

122 gerçek mesaj başlığı var: 59 kullanıcı, 63 asistan; 106 current-chain, 16 off-chain. Her mesaj gövdesinin uzunluğu ve SHA-256ı arşivde yazılı değerle eşleşti. Başlık üstündeki Model Council ve otomatik sınıflandırma etiketleri arşiv üstverisidir; canlı bir ajan ekibi veya kişinin sağlık durumu hakkında bağımsız olgu değildir.

Sohbet, OMROS mimarisini yedi araştırma eksenine ve beş çapraz soruya açar; bilim, sanat, inanç, felsefe, tekne, yönetim/hukuk ve siyaset boyunca araştırma kayıtları ve arşiv sürümleri üretildiğini anlatır. Kayıt–provenans–bellek, ham kayıt ile yorumlanmış aktarım, yerel özerklik, gerekçe, temyiz ve yeniden açma önemli sabitlerdir.

Model dosya linkleri ve “güncelledim/araştırdım/test ettim” cümleleri içerir. Link tek başına dosya gövdesi değildir. Literatür kapsamının tamamlanması, her PDFnin baştan sona okunması veya önerilen sistemin çalıştırılıp doğrulanmasıyla eşitlenemez. Bazı erişim notlarında PDF düğmesi, HTML ve metadata ayrımı açıkça görünür.

Current-chain v19 yanıtı 278 kaynak, 202 açık PDF notu, 76 diğer erişim notu söyler. Off-chain v19da S273–S284 eklemesi ve v20de 293 kaynak/12 senaryo/12 bulgu/12 gate kararı anlatılır. Amber-Go, metnin kendisinde masaüstü yürütüm olarak sınırlandırılır; gerçek kullanıcılı saha sonucu değildir.

Manifesto üretiminde arka plan yönteminin adlandırılmaması istenir. Sekiz alanı izleyen manifesto gövdeleri 1–27ye kadar gider. Current-chain son kullanıcı 28 Kurallı Agonizm bölümünü ister; onu tamamlayan asistan yanıtı bu arşivde yoktur. Off-chain alternatif istekler ayrı tutuldu.

İnanç Q4–Q6 isteği sonrasında v6 yanıtının önceki kapsamı tekrarlaması ve sonradan v7yle ilerlemesi, sürüm/konu doğrulamasının gerekli olduğunu gösterir. Timestamp sırası tek başına sohbet sırası yerine kullanılmadı.

**Yönlendirme:** Görünür kullanıcı mesajları araştırma, biçim, bölüm sırası, hata değerlendirmesi ve karşılıklı geri bildirimi belirler. Asistan bu isteklere farklı sürümlerde cevap üretir; bazı tekrarlar ve dal ayrımları vardır. Bu, gözlenebilir konuşma yönlendirmesidir. Çalışan CLI ayarı veya üst talimat değişikliği burada gösterilmiyor.

**İzin ve yürütme:** Belgedeki kullanıcı onayları tarihsel çalışmanın kapsamını açıklar; mevcut ortamda her bağlı dosyanın yazılmasını veya komutun yürütülmesini otomatik yetkilendirmez. Kaynak komutları çalıştırılmadı.

**Kapsam sınırı:** Orijinal Markdownın bütün karakterleri doğrudan okundu. Atıf işaretleri ve dosya/görsel işaretçileri korundu; işaretçinin işaret ettiği kayıp yük varsayılmadı. Özgün kaynak SHA ile eşleştirme zorunludur; sürüm adına tek başına güvenilmez.

Kaynak dayanakları: S12, S13, S14, S15, S16, S17, S18, S19.

## 7. F00219 — 22 Mart 2026 Piramidal ve Retiküler Sistem — ham TXT

49 USER, 57 ASSISTANT ve 1.812 Thoughts etiketli metin kesiti vardır. Bu etiketler kaynak dosyanın görünür içeriğidir; bağımsız doğrulanmış iç çalışma veya araç yürütme günlüğü diye kabul edilmedi. Birçok İngilizce kesit kısa, yarım veya kesilmiştir; eksikleri tamamlanmadı.

F200deki ana cevaplarla önemli miktarda tam metin eşliği bulunur. Yeni aralar araştırma seçenekleri, kaynak erişimi, kavram tereddütleri, çalışma kitabı sayfaları, doğrulama sözlükleri, Excel formülleri, stiller, Word düzeni, kaynakça ve ortam sorunları hakkında model anlatıları içerir. Betik, araç sonucu ve çalışma zamanı etkisi bu anlatımdan bağımsız gösterilmez.

Kanallar birbirine karıştırılmamalı: Thoughts kesiti v19 için 284 kaynak/183 PDF/101 diğer sayılarını yazar; hemen sonraki ASSISTANT ana cevabı 278/202/76dır ve F200 current-chain ile eşleşir. Bu uyuşmazlık kaynak planlama/anlatımını nihai sonuç gibi raporlamanın hatalı olacağını gösterir.

“Hidden Listeler” ifadesi izin verilen değerler ve sütun doğrulaması için önerilen Excel yardımcı sayfasıdır. “Crisis steering” ise siyasal/kurumsal kriz yönlendirmesi anlamında kullanılır. İkisi de Türkçe ChatGPT ilerleme başlığıyla aynı mekanizmayı veya gizli kişilerce kontrolü göstermez.

USER etiketiyle yazılmış açık onay, yazılı içerik üretim sisteminin arka planda uygulanmasını ve sonraki metinlerde adının anılmamasını ister. Nihai metinler ham kayıt/provenans, epistemik çoğulluk, haklar, yerel yetki, retiküler koordinasyon, kontrollü aktarım ve geri beslemeye bağlanır. 28 Kurallı Agonizm isteğiyle biter; tamamlayıcı yanıt yoktur.

Kimi kesitler atıfları sohbet yanıtında tutup Worde yalnız gövde eklemeyi seçtiğini anlatır; bu, kaynak sohbet ile son dosya arasındaki ilişkinin ayrıca korunması gerektiğini gösterir. Sayfa düzeltildi/render edildi/araç sustu gibi anlatılar, bu incelemede gözlenmiş olaylar diye aktarılmadı.

**Yönlendirme:** Buradaki yönlendirme, görünür USER talimatı ile cevap/üretim stratejisi arasındaki ilişkidir. Kaynak içindeki Thoughts etiketli yazılar ne bizim gizli muhakememizdir ne de mevcut platform üzerinde kontrol değişikliği için kanıttır.

**İzin ve yürütme:** Dosya içindeki planlar, komut fikirleri ve üretim istekleri okunup sınıflandırıldı; çalıştırılmadı. “Gizli süreç” yazım talebi, erişim veya güvenlik kurallarını kaldırmaz.

**Kapsam sınırı:** 1.078.751 ham karakterin 789.477si doğrudan, 289.274ü önceden okunan kaynaklarla doğrulanmış tam metin blokları üzerinden kapsandı. Newline dönüşümü uygulanmadı. Kanal ve role ayrımı yalnız özgün metindeki etiketin söylediği kadardır.

Kaynak dayanakları: S20, S21, S22, S23, S24.

## 8. F00197 — 7 Mart 2026 Piramidal ve Retiküler Sistem Farkları — ayrıntılı Markdown sohbeti

361 gerçek mesaj başlığı var: 94 kullanıcı, 267 asistan; 265 current-chain, 96 off-chain. Her mesajın gövde uzunluğu ve SHA-256ı doğrulandı. İlerleme mesajları ve çok kısa/yarım “B”, “Bu”, “Sor”, “Ö” gibi asistan kayıtları ayrı mesaj olarak korundu; otomatik bir komut veya anlamlı tam cümleye dönüştürülmedi.

Evrimsel ağaç–ağ açıklamasından omurga–kök–dal–retiküler sistemin kurulmasına, on sekiz soruluk araştırmaya ve sekiz yazı üretim alanına ilerler. Kullanıcı modelin iddia türünü, yazım yöntemini ve bölüm sırasını belirler; model temkinli bir meta-çerçeve, seçenek ağırlıkları ve bölüm metinleri üretir.

Literatürler arası yakınsama bütün sistemin deneysel doğrulanması yerine geçmez. Dağılım yüzdeleri yazı seçeneklerine ilişkin tercih değerlendirmesidir; ölçülmüş istatistik değildir. Decoding ifadesi yazı seçimi/çözümleme etiketi olarak kullanılır, gerçek model parametresi değişikliği göstermez.

Kanıt rejimleri, belirsizlik/karşı örnek, yazılı yetki ve itiraz, geri döndürülebilir pilot, stop/amend/go, yanıt–izleme–öğrenme–öngörü ve sürümleme birbirini tamamlayan tasarım ilkeleridir. İnançsal/estetik anlam ampirik kanıtla aynı hüküm rejimine sokulmaz; korunmuş itiraz otomatik veto değildir.

8.4 Şeffaflık/Kayıt/İzlenebilirlik burada ayrı tamamlanmış asistan gövdesidir. F176/F177 derlemelerindeki 8.3 tekrarıyla aynı sayılmamalı. Kullanıcının “arka planda gizli biçimde” talimatı açık kullanıcı mesajında yer alır ve nihai yazıda yöntem adlarının görünmemesini ister.

Current-chain kamusal ifade, yaşayan ortak sözlük, farklı okur düzeyleri, adillik/temsil, zarar azaltma, düzeltme/güncelleme ve 13.1–13.3 taahhüt bölümleriyle tamamlanır. Sessiz düzeltme yapılmaması, kesinlik veya nihai teori garantisi verilmemesi açıkça önerilir.

Off-chain bölümü erken Omurga-Retikül / Retikülo-Piramidal adlandırma alternatiflerini ve manifesto bölümlerinin başka gövdelerini korur. Son off-chain gövde 7.5 belirsizlik/karşı örnek kaydını bitirir; 8.1i sonraki adım olarak önerir. Bu sonlanma, current-chain 8–13 bölümlerinin yokluğu anlamına gelmez.

Off-chain kullanıcı M273 gizli bilişsel kurgu isteğini açıkça verir. M280 yüzdeleri yorum, M284 ise hedefe uygunluk ağırlıkları diye niteler. Rol, dal ve içerik statüsünü korumak teknik decoding veya gizli sistem talimatı diye yanlış eşlemeyi önler.

**Yönlendirme:** Görünür kullanıcı istemleri, modelin ara durum metinleri ve ana yanıtları aynı düzeyde tutulmadı. Öğrenme, mimari ve karşılıklı düzeltme önerileri çalışma tasarımıdır; CLIya bağlam yüklenmiş veya platform steering alanı değiştirilmiş olduğu sonucunu vermez.

**İzin ve yürütme:** Tarihsel istemler mevcut talimat olarak uygulanmadı. Rol/yetki tasarımları bir onay sisteminin gerçekten kurulduğuna ilişkin kanıt sayılmadı.

**Kapsam sınırı:** Bütün 1.470.556 ham karakter kapsandı: 738.332 karakter yeni metin olarak doğrudan okundu (1–13 paket downloads_chatgpt; 14–27 paket zip_embedded_audit), 732.224 karakter doğrulanmış tam blok eşliğiyle kapsandı. Aynı kaynak tekrarları yalnız daha önce kapsanmış aralıklara bağlandı. Harici atıflar araştırılmadı; görsel/ek işaretçilerinin yükü varsayılmadı.

Kaynak dayanakları: S25, S26, S27, S28, S29.

## 9. Aktarımda korunması gereken farklar

| Ayrım | Kaynakta gözlenen durum | Aktarım kararı |
|---|---|---|
| Sohbet / derleme | F197de 8.4 var; F176/F177de 8.3 tekrarı var. | Son dosyayı bütün konuşmanın eksiksiz temsili sayma; eksik bölüm bağını göster. |
| Planlama / ana yanıt | F219 Thoughts 284/183/101, ASSISTANT 278/202/76. | Sayıya rol ve kanal ekle; farklı cümleleri tek sonuç gibi birleştirme. |
| Current / off-chain | F200de farklı v19/v20 çıktıları aynı dosya adlarını kullanıyor. | Kimliği dosya adına göre değil kaynak SHA + mesaj gövdesi + dala göre kur. |
| Erişim / okuma | PDF düğmesi, açık URL, HTML ve metadata notları aynı şey değil. | “Kaynağa erişilebilir” ile “tamamı okundu” durumlarını ayrı sakla. |
| Tasarım / doğrulama | Gate, pilot, rol, araştırma ve düzenleme iddiaları var. | Metnin iddiasını bağımsız doğrulanmış işlem sonucu olarak taşıma. |
| Anahat / tamamlanan gövde | F184 yalnız 10a, F200/F219 manifesto 27ye kadar; 28 istemi yanıtsız. | Planlanan bölümün başlığını tamamlanmış içerik sayma. |
| Yazım yöntemi / yetki | Görünür gizli-yöntem istemleri ve ayrı hak/kanıt kuralları var. | Üslup ve yöntem isteğini izin veya güvenlik sınırlarının kaldırılmasıyla eşitleme. |

Bu farklar, CLI aktarım paketinde kaynak metin, kullanıcının niyeti, asistan yorumu, kesinleşmemiş tasarım, gerçekleştiği söylenen işlem ve gerçekten doğrulanmış kanıt için ayrı alanlar tutulmasını gerektirir. “Ben/Sen” ayrımının aşılmasıyla anlatılan ortak çalışma yaklaşımı, kaynak/rol/kanıt kökeninin silinmesini gerektirmez; bu koruma, karşılıklı düzeltmeyi uygulanabilir kılar.

## 10. Kanıt ve kapsam dosyaları

`sources.json`: özgün dosya ve okuma kopyası hashleri, yollar, çıkarım kapsamı. `coverage.json`: doğrudan okunan ve tekrar üzerinden kapsanan aralıklar. `reading_notes.json`: okuma paketleri boyunca içerik notları. `evidence.json`: S01–S29 doğrudan alıntı, kaynak SHA, sıfırdan başlayan yarı açık karakter aralığı ve mümkün olan yerlerde mesaj rolü/dalı. `F00197_message_index.json` ile `F00200_message_index.json`: bütün gerçek mesaj gövdelerinin uzunluk/hash kontrolleri. Okuma planları bütün eşlik ve tamamlayıcı aralıkları taşır. `exact_block_mapping.json` son kontrolde eşlik ve okunmuş kaynak bağımlılıklarını yeniden doğrular; kardeş okuyucunun 14–27 paket kaydı kendi alt dizinindedir.

Kaynak alıntıları yalnız kullanıcı tarafından sağlanan dosyalardan alınmıştır. Tarihsel yanıtlardaki kaynakça ve atıf işaretleri, bu incelemede dış kaynakların yeniden açılıp doğrulandığı anlamına gelmez.

| Kanıt | Kaynak | Ham karakter aralığı | Konum / açıklama |
|---|---|---|---|
| S01 | F00176 | [312652, 312739) | Meta-çerçeve kendi sınırını açıkça kararın nasıl üretildiği üzerinden koyuyor; otomatik doğru sonuç iddiası yok. |
| S02 | F00176 | [189216, 189311) | Derlemede görünür yazım isteği: metin üretim yönteminin nihai yazıda adlandırılmaması isteniyor. |
| S03 | F00176 | [633851, 633886) | İlk tamamlanmış 8.3 gövde başlığı. |
| S04 | F00176 | [647148, 647183) | İkinci 8.3 gövde başlığı; 8.4 yerine tekrar bulundu. |
| S05 | F00176 | [598690, 598735) | Aranmamış karşı kanıt ile bulunamamış karşı kanıtın ayrımı. |
| S06 | F00184 | [17533, 17610) | Görünür kullanıcı düzeltmesi hiyerarşiyi terminal modüllere yerleştiriyor. |
| S07 | F00184 | [17824, 17910) | Retiküler ağın kapsama sınırını kullanıcı açıkça değiştiriyor. |
| S08 | F00184 | [40134, 40159) | Asistanın literatür kavramları üzerinden kurduğu doğrulama ifadesi; doğrudan deney kaydı değil. |
| S09 | F00184 | [226312, 226407) | Yazım yöntemi isteminin görünür içeriği; gizli üçüncü kişiyi işaret etmiyor. |
| S10 | F00184 | [460851, 460869) | Tamamlanmış gövdenin son ana bölümü; daha uzun anahat başlıkları tamamlanmış bölüm sayılmaz. |
| S11 | F00184 | [472608, 472739) | Dosya sonunda ayrı bir derleme makalesi için yeni kullanıcı istemi; Heterarşi metninin devamı diye birleştirilmemeli. |
| S12 | F00200 | [617, 633) | Arşiv sınıflandırma üstverisi; çalışma sırasında gözlenen canlı ajan kümesi değil. |
| S13 | F00200 | [15923, 15957) | M006 user / current_chain; Kullanıcı mesajı içindeki görünür araştırma/yazı yöntemi talimatı. |
| S14 | F00200 | [182054, 182162) | M053 assistant / current_chain; Current-chain v19 yanıtındaki sayılar; PDF erişim notu bütün PDFlerin okunduğu anlamına gelmez. |
| S15 | F00200 | [349798, 349819) | M115 assistant / off_chain; Off-chain v19 yanıtında farklı kaynak ekleme kapsamı. |
| S16 | F00200 | [355561, 355599) | M118 assistant / off_chain; Off-chain v20 yanıtı; aynı sürüm adı tek dosya kimliği sayılmamalı. |
| S17 | F00200 | [356338, 356428) | M118 assistant / off_chain; Amber-Go sonuç iddiasının kendi metnindeki açık sınırlaması. |
| S18 | F00200 | [118127, 118195) | M032 assistant / current_chain; Kaynak kaydı ile yorum/özet aktarımını ayıran tasarım ilkesi. |
| S19 | F00200 | [324377, 324396) | M106 user / current_chain; Current-chain son kullanıcı isteği; arşivde bunu izleyen tamamlanmış yanıt yok. |
| S20 | F00219 | [713277, 713333) | Thoughts; Thoughts etiketli kaynak metni içindeki sayı; nihai ASSISTANT yanıtı ile aynı kanal değil. |
| S21 | F00219 | [715796, 715904) | ASSISTANT; Ham TXT nihai ASSISTANT yanıtı; F200 current-chain ile eş, önceki Thoughts sayısından farklı. |
| S22 | F00219 | [738410, 738514) | USER; USER etiketindeki görünür talimat; yazı üretim sisteminin nihai içerikte adlandırılmaması isteniyor. |
| S23 | F00219 | [550256, 550271) | Thoughts; İngilizce yönetişim/kriz yönlendirme kullanımı; ChatGPT Türkçe ilerleme başlığının aynı özne veya teknik özelliği olduğunu göstermiyor. |
| S24 | F00219 | [149589, 149659) | Thoughts; Gizli sözcüğü burada önerilen Excel değer sözlüğü sayfasına ait; gizli kişilerle ilişki kurulamaz. |
| S25 | F00197 | [233242, 233337) | M056 user / current_chain; Mesaj rolü kullanıcı olan açık yöntem talimatı. Ausubel/ayrıntılandırıcı kodlama/çift kodlama ve metaforla yazım isteniyor. |
| S26 | F00197 | [822442, 822485) | M211 assistant / current_chain; Current-chain asistan ana yanıtında gerçekten üretilmiş bölüm; F176 derlemesinde gövde olarak yok. |
| S27 | F00197 | [1087839, 1087871) | M265 assistant / current_chain; Current-chain son manifesto bölümü; off-chain alternatifler ayrı kaydedildi. |
| S28 | F00197 | [1133210, 1133314) | M280 assistant / off_chain; Off-chain asistan yanıtı, kendi ağırlıklarını ampirik oranlardan açıkça ayırıyor. |
| S29 | F00197 | [1146065, 1146134) | M284 assistant / off_chain; Off-chain asistan yanıtı: Dağılım yüzdeleri ölçülmüş model telemetrisi olarak sunulmuyor. |

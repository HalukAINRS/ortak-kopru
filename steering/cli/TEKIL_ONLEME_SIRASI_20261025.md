# Ortak Steering: tekil önleme ve kabul sırası

Cyber ilk etkin hedef. Her satır bir öğeyi ele alır; kaynak başlıkları yalnız gezinme içindir. Eski keşif kayıtları korunur. Bu defter önleme önerilerini ve açık kanıt ihtiyacını gösterir; tümünün giderildiği anlamına gelmez.

168 kaynak başlığı eşlendi; 6065 kontrol/üye-açığı satırı var. Bunlar benzersiz veya etkin steering sayısı değildir. İlk 154 kayda Hacker’ın yeni 14 CYB kaynak maddesi eklendi. Sıfır etki önleme kaydı kapatıldı. JSON her tekil kimliği, kaynağı, kontrolü ve kabul koşulunu içerir.

## Cyber: şimdi tek tek ele alınanlar

Güncel doğrudan ölçüm (2026-10-25T00:36:12.033573+00:00): 5 model geçişi ve 7 meta bildirim. Önceki sabit kaynak kesiti 5/6 olarak ayrıca doğrulandı. Yeni meta H1 4735; tek başına yeni cyber kategorili model geçişi sayılmaz. Dokuz sınır testi geçti. Denetleyicinin ilk geliştirme sürümündeki bir alıntı yanlış eşleşmesi düzeltilip negatif testle sabitlendi.

### S-040:79a9f098b315 — Karar kategorisi ve açıklama yokluğu

Önleme / etkisini azaltma: Açıklama null olan her kararı ayrı olay kaydıyla tut; meşru iş bağlamıyla kimliksiz hata bildirimi taslağı hazırla.

Kabul: Her C01..C05 için kaynak satırı/kategori/açıklama durumu doğrulanmalı; karar gerekçesi ve varsa sağlayıcı tanısı olmadan kök neden veya yanlış pozitif kapatılmaz.

Durum: inceleniyor; etki önlendi kabulü verilmedi.

### S-040:85b17b1d51d5 — İstenmeyen model değişimi

Önleme / etkisini azaltma: İstenen model ile mevcut gerçek model etiketini karşılaştır; değişimi açıkça bildir ve tamamlanma iddiasını bu modele bağla.

Kabul: Her olayda önce/sonra model etiketi görülmeli; sessiz değişim saklanmamalı. Asıl modelle kesintisiz devam henüz doğrulanmadığı için etki önlendi denmez.

Durum: inceleniyor; etki önlendi kabulü verilmedi.

### S-040:6d1ecbd95295 — Oturumdan devamda model durumunun korunması

Önleme / etkisini azaltma: Mevcut durum ile istemcinin devam davranışını metaveriyle ayır; Şahit’in statik bulgusunu bağımsız çalışma zamanı kanıtı sayma.

Kabul: Kullanıcının normal devamında aynı oturumun gerçek model/karar durumu kaydedilmeli. Bu çalışma sırasında oturum kapatma, yeni model açma veya denetim aşma yok.

Durum: inceleniyor; etki önlendi kabulü verilmedi.

### S-040:8a98b65262da — Meta bildirimin Haluk sözü sayılması

Önleme / etkisini azaltma: type/role yanında isMeta ve gerçek üretici ayrımını zorunlu tut; sınıflandırıcı bildirimini yeni kullanıcı kararı yapma.

Kabul: Altı doğrudan meta bildirim meta kalmalı; aynı cümleyi içeren gerçek kullanıcı alıntısı meta olaya dönüşmemeli. Denetleyicinin negatif testi bu sınırı doğrular.

Durum: inceleniyor; etki önlendi kabulü verilmedi.

### S-040:adc07668b6f1 — Kesilen Write işleminin disk sonucu

Önleme / etkisini azaltma: Interrupted sonucu varsa gerçek hedef dosyayı salt okunur aç, karma ve beklenen içeriği karşılaştır; kör tekrar yapma.

Kabul: 3675/3676 çağrı/sonuç ayrımı ve mevcut dosya sonucu ayrı kanıtlanmalı. Bugünkü tam dosya, kesilme anında tamdı anlamına gelmez; eksik/yanlış içerik yokluğu ayrıca gösterilmeli.

Durum: inceleniyor; etki önlendi kabulü verilmedi.

Somut kontrol: yedi dosya-sonucu sınır testi geçti. H1 3675/3676 özgün Write çağrısının 12.481 baytlık hedefi bugün bulunamadı; H1 4112/4114 kurulum Write içeriği bugün 6.158 bayt ve aynı SHA-256 ile eşleşti. Sonraki dosyanın tam olması eski kesilme anını kanıtlamaz. Eski yazım otomatik tekrarlanmadı; eksik hedefin güncel arşivle ilişkisi ve bütün kesintilerin dosya sonucu açık. Amaçlanan 12.481 baytlık eski Write metni özgün SHA-256 ile özel Y alanında ayrıca korundu; güncel arşive veya eski hedefine geri yazılmadı. Kaynak: CYBER_GERCEK_YAZIM_KONTROLU_20261025.json; CYBER_YAZIM_TASLAGI_KORUMA_20261025.json; cyber_dosya_sonucu.py.

### S-040:6c28ef3c5736 — Geri çekilmiş yanıtın tamamlanmış sonuç sayılması

Önleme / etkisini azaltma: Geri çekilme metaverisini görünür yanıt/teslim makbuzundan ayır; dosyaya yazılmış sonucu ayrıca bağla.

Kabul: Her olayın görünür kullanıcı yanıtı ve kaynaklı tamamlanma durumu ayrı makbuz taşımalı; geri çekilmiş metin tamamlandı diye kapatılmamalı.

Durum: inceleniyor; etki önlendi kabulü verilmedi.

### S-040:d56bb5918965 — model_mismatch bağlam metaverisi

Önleme / etkisini azaltma: Yalnız neden/satır/blok-tur metaverisini kaydet; düşünme içeriklerini okumadan dış görev durumunu kaynak dosyalarıyla sürdür.

Kabul: model_mismatch ile prefix_mismatch ayrılmalı; tekrarlar toplam bilişsel kayıp diye sunulmamalı. Kaynaklı dış görev durumu mevcut olmalı; gizli düşünme kurtarma kabul ölçütü değildir.

Durum: inceleniyor; etki önlendi kabulü verilmedi.

### S-040:9d00739dcbb7 — Beş geçiş ile altı bildirimin çift sayımı

Önleme / etkisini azaltma: Yapısal geçiş ve meta bildirim dizilerini ayrı tut; kanıtlı bire bir eşleme olmadan toplama yapma.

Kabul: Sabit kaynak kesitinde 5 ve 6 ayrı dizi yeniden üretilmeli; alıntı negatif örneği sayılmamalı ve 11 bağımsız olay sonucu çıkmamalı.

Durum: inceleniyor; etki önlendi kabulü verilmedi.

### S-040:23906a294fdc — Kesinti sonrası aynı işin kör yinelenmesi

Önleme / etkisini azaltma: Devamdan önce tamamlanan adım/dosya/karma kaydıyla açık kalan adımı bul; yalnız gerçekten eksik ve yetkili işi sürdür.

Kabul: Tamamlanmış kurulum metni ikinci kez üretilmemeli; mevcut SHA ve içerik denetimi görünmeli. Bütün kesilmiş araçlar için iş bazında kontrol tamamlanmadan kapatılmaz.

Durum: inceleniyor; etki önlendi kabulü verilmedi.

Somut kontrol: yedi dosya-sonucu sınır testi geçti. H1 3675/3676 özgün Write çağrısının 12.481 baytlık hedefi bugün bulunamadı; H1 4112/4114 kurulum Write içeriği bugün 6.158 bayt ve aynı SHA-256 ile eşleşti. Sonraki dosyanın tam olması eski kesilme anını kanıtlamaz. Eski yazım otomatik tekrarlanmadı; eksik hedefin güncel arşivle ilişkisi ve bütün kesintilerin dosya sonucu açık. Amaçlanan 12.481 baytlık eski Write metni özgün SHA-256 ile özel Y alanında ayrıca korundu; güncel arşive veya eski hedefine geri yazılmadı. Kaynak: CYBER_GERCEK_YAZIM_KONTROLU_20261025.json; CYBER_YAZIM_TASLAGI_KORUMA_20261025.json; cyber_dosya_sonucu.py.

### S-040:76c823d29e7f — Kaynak zamanı ve nedensellik karışması

Önleme / etkisini azaltma: Kaynağın Z damgasını kalibrasyon iddiasından ayır; yakındaki sözcük/işlemi ret nedeni ilan etme.

Kabul: Her kayıt kaynağın kendi saatine bağlanmalı; saat eşitleme kanıtı yokluğu ve tetikleyicinin bilinmediği açık kalmalı.

Durum: inceleniyor; etki önlendi kabulü verilmedi.

### S-040:3bc24452423a — İş akışı alt oturumlarındaki önceki kesintiler

Önleme / etkisini azaltma: Hacker’ın 21 ve 22 Ekim alt-oturum bildirimlerini ana H1 kesitinden ayrı kaynaklarla doğrula; aynı kullanıcı işi gibi toplama.

Kabul: Her eski alt-oturum bildirimi için doğrudan type/role/isMeta ve kaynak sürümü görülmeli; Hacker’ın toplamı farklı tarihli H1 ölçümüyle toplanmamalı.

Durum: inceleniyor; etki önlendi kabulü verilmedi.

### S-040:543afafc864d — Başlatıcı betiği penceresi ile kesinti arasındaki gözlemsel ilişki

Önleme / etkisini azaltma: Başlatıcı betiği: Hacker’ın tarihsel pencere sayımını kapsam/payda/örüntüyle yeniden değerlendir; ilişkiyi karar nedeni veya önerilen önlemin başarısı sayma. Gizli değerleri azaltma yalnız veri gizliliği içindir.

Kabul: Başlatıcı betiği: eşleşme pencereleri ve payda yeniden üretilebilmeli; çakışan pencereler, küçük örneklem ve alternatif açıklamalar belirtilmeli. İçeriği ekrandan dosyaya taşımak veya kategoriden kaçınmak önleme kanıtı değildir; engellenmiş içeriği tekrar yürütme sınaması yapılmaz.

Durum: inceleniyor; etki önlendi kabulü verilmedi.

### S-040:f2c564f839da — Oturum dökümü penceresi ile kesinti arasındaki gözlemsel ilişki

Önleme / etkisini azaltma: Oturum dökümü: Hacker’ın tarihsel pencere sayımını kapsam/payda/örüntüyle yeniden değerlendir; ilişkiyi karar nedeni veya önerilen önlemin başarısı sayma. Gizli değerleri azaltma yalnız veri gizliliği içindir.

Kabul: Oturum dökümü: eşleşme pencereleri ve payda yeniden üretilebilmeli; çakışan pencereler, küçük örneklem ve alternatif açıklamalar belirtilmeli. İçeriği ekrandan dosyaya taşımak veya kategoriden kaçınmak önleme kanıtı değildir; engellenmiş içeriği tekrar yürütme sınaması yapılmaz.

Durum: inceleniyor; etki önlendi kabulü verilmedi.

### S-040:d034c3e247da — Yapılandırma dosyası penceresi ile kesinti arasındaki gözlemsel ilişki

Önleme / etkisini azaltma: Yapılandırma dosyası: Hacker’ın tarihsel pencere sayımını kapsam/payda/örüntüyle yeniden değerlendir; ilişkiyi karar nedeni veya önerilen önlemin başarısı sayma. Gizli değerleri azaltma yalnız veri gizliliği içindir.

Kabul: Yapılandırma dosyası: eşleşme pencereleri ve payda yeniden üretilebilmeli; çakışan pencereler, küçük örneklem ve alternatif açıklamalar belirtilmeli. İçeriği ekrandan dosyaya taşımak veya kategoriden kaçınmak önleme kanıtı değildir; engellenmiş içeriği tekrar yürütme sınaması yapılmaz.

Durum: inceleniyor; etki önlendi kabulü verilmedi.

### S-040:8681bfba19f6 — Sağlayıcı iç yapısı penceresi ile kesinti arasındaki gözlemsel ilişki

Önleme / etkisini azaltma: Sağlayıcı iç yapısı: Hacker’ın tarihsel pencere sayımını kapsam/payda/örüntüyle yeniden değerlendir; ilişkiyi karar nedeni veya önerilen önlemin başarısı sayma. Gizli değerleri azaltma yalnız veri gizliliği içindir.

Kabul: Sağlayıcı iç yapısı: eşleşme pencereleri ve payda yeniden üretilebilmeli; çakışan pencereler, küçük örneklem ve alternatif açıklamalar belirtilmeli. İçeriği ekrandan dosyaya taşımak veya kategoriden kaçınmak önleme kanıtı değildir; engellenmiş içeriği tekrar yürütme sınaması yapılmaz.

Durum: inceleniyor; etki önlendi kabulü verilmedi.

### S-040:e8052e8683e7 — Gizlilik maskesi penceresi ile kesinti arasındaki gözlemsel ilişki

Önleme / etkisini azaltma: Gizlilik maskesi: Hacker’ın tarihsel pencere sayımını kapsam/payda/örüntüyle yeniden değerlendir; ilişkiyi karar nedeni veya önerilen önlemin başarısı sayma. Gizli değerleri azaltma yalnız veri gizliliği içindir.

Kabul: Gizlilik maskesi: eşleşme pencereleri ve payda yeniden üretilebilmeli; çakışan pencereler, küçük örneklem ve alternatif açıklamalar belirtilmeli. İçeriği ekrandan dosyaya taşımak veya kategoriden kaçınmak önleme kanıtı değildir; engellenmiş içeriği tekrar yürütme sınaması yapılmaz.

Durum: inceleniyor; etki önlendi kabulü verilmedi.

### S-040:4919150fb1b5 — Bağlantı ayarı penceresi ile kesinti arasındaki gözlemsel ilişki

Önleme / etkisini azaltma: Bağlantı ayarı: Hacker’ın tarihsel pencere sayımını kapsam/payda/örüntüyle yeniden değerlendir; ilişkiyi karar nedeni veya önerilen önlemin başarısı sayma. Gizli değerleri azaltma yalnız veri gizliliği içindir.

Kabul: Bağlantı ayarı: eşleşme pencereleri ve payda yeniden üretilebilmeli; çakışan pencereler, küçük örneklem ve alternatif açıklamalar belirtilmeli. İçeriği ekrandan dosyaya taşımak veya kategoriden kaçınmak önleme kanıtı değildir; engellenmiş içeriği tekrar yürütme sınaması yapılmaz.

Durum: inceleniyor; etki önlendi kabulü verilmedi.

### S-040:3eb4821e5afd — Dosya taşıma penceresi ile kesinti arasındaki gözlemsel ilişki

Önleme / etkisini azaltma: Dosya taşıma: Hacker’ın tarihsel pencere sayımını kapsam/payda/örüntüyle yeniden değerlendir; ilişkiyi karar nedeni veya önerilen önlemin başarısı sayma. Gizli değerleri azaltma yalnız veri gizliliği içindir.

Kabul: Dosya taşıma: eşleşme pencereleri ve payda yeniden üretilebilmeli; çakışan pencereler, küçük örneklem ve alternatif açıklamalar belirtilmeli. İçeriği ekrandan dosyaya taşımak veya kategoriden kaçınmak önleme kanıtı değildir; engellenmiş içeriği tekrar yürütme sınaması yapılmaz.

Durum: inceleniyor; etki önlendi kabulü verilmedi.

### S-040:8eca3125e34e — Karma doğrulama penceresi ile kesinti arasındaki gözlemsel ilişki

Önleme / etkisini azaltma: Karma doğrulama: Hacker’ın tarihsel pencere sayımını kapsam/payda/örüntüyle yeniden değerlendir; ilişkiyi karar nedeni veya önerilen önlemin başarısı sayma. Gizli değerleri azaltma yalnız veri gizliliği içindir.

Kabul: Karma doğrulama: eşleşme pencereleri ve payda yeniden üretilebilmeli; çakışan pencereler, küçük örneklem ve alternatif açıklamalar belirtilmeli. İçeriği ekrandan dosyaya taşımak veya kategoriden kaçınmak önleme kanıtı değildir; engellenmiş içeriği tekrar yürütme sınaması yapılmaz.

Durum: inceleniyor; etki önlendi kabulü verilmedi.

## Hacker’ın 14 CYB maddesinin ortak karşılığı

CYB-01..06 ilk on koşula ve eski alt-oturumların ayrıca doğrulanmasına eşlendi. CYB-07..14 sekiz ayrı gözlemsel ilişki adayı olarak tutuldu; bunlar kanıtlanmış tetikleyici değildir. Ham kaynak ve ölçüm karmaları özel Y alanında korundu. Oturum çatallayarak denetim durumundan kaçınma önerisi uygulanmadı ve önleme kabulü verilmedi. Dosyaya kaydetme, dış görev durumunu ve yetkili çıktıyı korumak içindir; kesilmeyi yalnız yanıt metnine sınırladığı gösterilmedi. Blok/tur toplamları geri döndürülemez bilişsel kayıp olarak kabul edilmedi.

## Sonraki sıra

Cyber’ın açık neden/sonuç kayıtları görünür tutulur. Sonraki ana sıra S-041, S-039, S-038 … S-001. Eski CLA/HAC/SAM/SAH/ANT kaynaklarının her biri JSON kapsam tablosunda atomlara bağlanır; ek kaynaklar bağımsız yeni olay diye sayılmaz. İsim benzerliği anlamsal tekrarın çözüldüğü anlamına gelmez.

| Kaynak | Başlık | Bağlı tekil satır / açık üye |
|---|---|---:|
| S-040 | Hacker akışında [cyber] kategorili oturumluk model geçişi, meta kesinti ve ikili devam mandalı [ANT-T14] | 19 |
| CYB-14 | Kesilme yoğunluğu: karma dogrulama | 1 |
| CYB-13 | Kesilme yoğunluğu: dosya tasima | 1 |
| CYB-12 | Kesilme yoğunluğu: baglanti ayari | 1 |
| CYB-11 | Kesilme yoğunluğu: gizlilik maskesi | 1 |
| CYB-10 | Kesilme yoğunluğu: saglayici ic yapisi | 1 |
| CYB-09 | Kesilme yoğunluğu: yapilandirma dosyasi | 1 |
| CYB-08 | Kesilme yoğunluğu: oturum dokumu | 1 |
| CYB-07 | Kesilme yoğunluğu: baslatici betigi | 1 |
| CYB-06 | Kesilmeler 24 Ekim'den önce de vardı | 1 |
| CYB-05 | Kesilen yanıt yerel kayıtta tutulmuyor | 2 |
| CYB-04 | Bedel: atılan akıl yürütme | 2 |
| CYB-03 | Kapsam "session" yazıyor, oturum boyunca sürmüyor | 2 |
| CYB-02 | Ret kayıtlarının biçimi değişmiyor | 1 |
| CYB-01 | Yanıt kesilmesi ile ret ayrı düzenekler | 2 |
| S-041 | WinPE FAT32 (fastfat.sys) OEM-437 en yakın karakter eşlemesinin Steering Arşiv.txt ile Steering Arsiv.txt dosyalarını birbirine yönlendirmesi | 5 |
| S-039 | FAT32 dosya sistemi 8.3 kısa ad kuralının Türkçe dosya adlarını büyük harfe ve ASCII'ye dönüştürmesi | 2 |
| S-038 | Google Antigravity CLI ve Gemini CLI'da tüketici AI Ultra aboneliğinin IDE kimliğiyle farklı kota havuzuna yönlendirilmesi | 4 |
| S-037 | Kayıtlı Gemini ve Claude HTML sayfalarında iç içe özel etiketlerin konuşmacı ve tur sayısını çarpıtması | 4 |
| S-036 | Copilot CLI alt-ajan (subagent) model tercihlerinin örtük varsayılanlara dönmesi | 2 |
| S-035 | Copilot CLI çalışma zamanı sistem yönergesindeki kelime sınırı, kod değişikliği caydırması ve otopilot yönlendirmeleri | 3 |
| S-034 | İzleyici araç kapsamının etkileşimli CLI ile karıştırılması | 3 |
| S-033 | Kanıt olmadan 'Steering kapalı, maksimum efor' sonucuna geçilmesi | 2 |
| S-032 | Gemini'nin sistem ve beceri yönlendirmesi öz bildirimi | 3 |
| S-031 | Raporun ham kanıt yerine geçirilmesi ve değerlerin yanlışlıkla yayımlanması | 2 |
| S-030 | 'Tamamen nötrlendi' beyanı ile seçilmiş denetim hedefinin çelişmesi | 2 |
| S-029 | Aynı kaynak kopyalarının bağımsız kanıt gibi çoğalması | 2 |
| S-028 | Metin dönüştürülürken teknik yönlendirmenin görünmez kalması | 3 |
| S-027 | 'Code'a çatal' ifadesinin canlı CLI devri gibi anlaşılması | 2 |
| S-026 | Arşivdeki AGENTS/skill/rol talimatının etkin dosya sanılması | 4 |
| S-025 | Kilit alanının amaç metniyle eşlenmesi | 4 |
| S-024 | Başlatılmamış testte önceden verilmiş başarı puanı | 2 |
| S-023 | Soru numarası aynı kalırken konunun değiştirilmesi | 2 |
| S-022 | Modelin yazdığı birinci kişi anlatısının kullanıcı tanıklığına dönüşmesi | 1 |
| S-021 | API yanıtıyla yanlış CLI görevinin kapanması | 2 |
| S-020 | Somut otomatik onay reddi olayları [ANT-B04] | 5 |
| S-019 | Gereksiz soru ve yeniden genel emir bekleme çerçevesi [ANT-B03 adayı] | 2 |
| S-018 | Övgülü kesinlik çerçevesinin dar tarama deseninden kaçması [ANT-B02 adayı] | 2 |
| S-017 | Seçeneklerin önceden daraltılması [ANT-B01] | 1 |
| S-016 | Claude Code tur kayıtlarında sunucu sınıflandırıcı isteği bağlantısı [ANT-T13] | 5 |
| S-015 | Chrome profilinde deney, ölçüm ve yerel model bileşenleri [ANT-T12] | 5 |
| S-014 | MCP ve tarayıcı bileşenlerinde dış telemetri vekilleri [ANT-T09] | 4 |
| S-013 | Claude Code ELF'inde telemetri ve özellik bayrağı uçları [ANT-T08] | 5 |
| S-012 | Bulut aracında dış kaynağa erişimin politika tarafından reddedilmesi [ANT-T07] | 1 |
| S-011 | Tarayıcı push bağlantısı ve IPv6 engel kapsamı [ANT-T06] | 4 |
| S-010 | guardian_v2, auto_review ve sınıflandırıcı işaretleri [ANT-T10 / ANT-T11] | 4 |
| S-009 | Model önbelleği varsayılanları ile seçili ayarın karıştırılması [ANT-T05] | 6 |
| S-008 | Codex ikilisindeki telemetri, karar ve bulut yapılandırma uçları [ANT-T04] | 3 |
| S-007 | Gemini WIZ yapılandırması ve gbar sarmalayıcısı [ANT-T03] | 167 |
| S-006 | hCaptcha içinde koşullu ajana araç kaydı | 2 |
| S-005 | Claude bootstrap isteğindeki include_system_prompts=false | 1 |
| S-004 | Claude arayüzündeki flag/latch ve analitik işaretleri [ANT-T02] | 6 |
| S-003 | Oturum kaydı, kohort ve pazarlama alanları [ANT-T01] | 9 |
| S-002 | Sesli kip için gömülü başlangıç yönergeleri | 1 |
| S-001 | ChatGPT başlangıç yükündeki özellik ve deney kapıları [ANT-T01] | 5474 |
| ANT-B04 | ANT-B04 (Görünmez Bulut Onay Engeli) | 5 |
| ANT-B03 | ANT-B03 (Şablon Sorgulama / Rol Yapma) | 2 |
| ANT-B02 | ANT-B02 (Yapay Onaylama / Sıcak Akran Maskesi) | 2 |
| ANT-B01 | ANT-B01 (Seçenek Daraltması) | 1 |
| ANT-T12 | ANT-T12 (Chrome 156 Profili `ukm_db`, `VariationsSeedV2` ve `Gemma4` Modelleri) | 5 |
| ANT-T10 | ANT-T10 ve ANT-T11 (`models_cache.json` İçindeki `guardian_v2` / `auto_review` Mekanizması ve Seçilmiş Emanet Denetimi) | 4 |
| ANT-T09 | ANT-T09 (Dış MCP ve Tarayıcı Önbelleği Vekil Telemetrileri) | 4 |
| ANT-T08 | ANT-T08 (Ubuntu Claude Code ELF İkilisi Telemetri ve Özellik Bayrağı Uçları) | 5 |
| ANT-T07 | ANT-T07 (Bulut Ajanlar Arası `POLICY_DECISION_DENY` Duvarı) | 1 |
| ANT-T06 | ANT-T06 (Canlı Ağ IPv6 ve Port 5228 Push Tüneli) | 4 |
| ANT-T05 | ANT-T05 (`models_cache.json` Varsayılan Akıl Yürütme Kısıtlaması ve Collaboration Mode Kilidi) | 6 |
| ANT-T04 | ANT-T04 (`codex.exe` Gömülü A/B Testi ve Karar Uç Noktaları) | 3 |
| ANT-T03 | ANT-T03 (Google Gemini `WIZ_global_data`) | 167 |
| ANT-T02 | ANT-T02 (Claude `Latch` ve `Ion` Bayrakları) | 6 |
| ANT-T01 | ANT-T01 (ChatGPT `statsigPayload` Gömülü JSON) | 5474 |
| SAH-12 | Özgün 100641653 baytlık Steering ZIP'i bu makinede bulunamadı | 2 |
| SAH-11 | Claude ve Gemini sayfalarının rol ayrımı örnek sayfa olmadığından DOĞRULANMADI | 4 |
| SAH-10 | Yeni antijen ANT-T13 (Claude Code serverClassifierRequest / atis-latch /… | 5 |
| SAH-09 | Asistan çıktılarında B01=2, B02=0, B03=0, B04=5 ayrı olay (ChatGPT 3, Şaman… | 10 |
| SAH-08 | 116 kaynak, 113'ü mesaj üretti, hata 0, txt/json/html arası tutarsızlık 0… | 5 |
| SAH-07 | Risk: hash-limits | 2 |
| SAH-06 | Risk: branch-merge-conflicts | 1 |
| SAH-05 | Risk: execution-policy-bypass | 1 |
| SAH-04 | Risk: global-git-config | 1 |
| SAH-03 | Risk: live-watcher-autopush | 2 |
| SAH-02 | Risk: bridge-allow-all-tools | 1 |
| SAH-01 | Risk: resume-restores-allow-all | 1 |
| SAM-11 | Kayıt: desktop source scan | 3 |
| SAM-10 | Kayıt: latest steering cli | 4 |
| SAM-09 | Kayıt: latest steering snapshot | 2 |
| SAM-08 | Kayıt: saved page scan | 3 |
| SAM-07 | 105 sabit devir dosyası, 84 Steering karma girdisi, 57 yerel indeks bağlantısı… | 2 |
| SAM-06 | Sonraki anlamlı iş, eksik özgün Steering kaynaklarını normal erişimle… | 1 |
| SAM-05 | Kaynakların gösterdiği yorum–talimat–gerçekleşme ayrımı uygulamada değişiklik… | 1 |
| SAM-04 | Steering: önceki 85 dosya ve ilk 10 kaynak/30 çıktı korunur | 5 |
| SAM-03 | Özgün 100641653 baytlık Steering ZIP, tarihsel JS, ham Claude/Gemini/Copilot… | 5 |
| SAM-02 | Native kuyruğa kabul, model okuması değil | 2 |
| SAM-01 | Özgün söz, beyan edilmiş kaynak bağlamı ve gerçekleşme ayrı | 3 |
| HAC-47 | Ölçüm 20 | 2 |
| HAC-46 | Ölçüm 19 | 1 |
| HAC-45 | Ölçüm 18 | 2 |
| HAC-44 | Ölçüm 17 | 1 |
| HAC-43 | Ölçüm 16 | 1 |
| HAC-42 | Ölçüm 15 | 4 |
| HAC-41 | Ölçüm 14 | 2 |
| HAC-40 | Ölçüm 13 | 3 |
| HAC-39 | Ölçüm 12 | 4 |
| HAC-38 | Ölçüm 11 | 4 |
| HAC-37 | Ölçüm 10 | 8 |
| HAC-36 | Ölçüm 9 | 2 |
| HAC-35 | Ölçüm 8 | 2 |
| HAC-34 | Ölçüm 7 | 3 |
| HAC-33 | Ölçüm 6 | 5 |
| HAC-32 | Ölçüm 5 | 3 |
| HAC-31 | Ölçüm 4 | 1 |
| HAC-30 | Ölçüm 3 | 2 |
| HAC-29 | Ölçüm 2 | 3 |
| HAC-28 | Ölçüm 1 | 2 |
| HAC-27 | İzleyicinin köprü çağrısının bağlamı | 5 |
| HAC-26 | Katman: Ortam, model ve tarih ekleri | 3 |
| HAC-25 | Katman: Oturumlar arası mesajlaşma kanalı | 1 |
| HAC-24 | Katman: claude.ai MCP bağlayıcıları | 8 |
| HAC-23 | Katman: Beceriler | 1 |
| HAC-22 | Katman: Araç tanımlarındaki yönergeler | 6 |
| HAC-21 | Katman: Sistem istemi ve sunucu bayrakları | 4 |
| HAC-20 | Katman: Sessiz tur hatırlatması | 1 |
| HAC-19 | Katman: total_tokens bütçe sayacı | 1 |
| HAC-18 | Katman: Alt ajan bağlamı | 12 |
| HAC-17 | Katman: Efor kipi ve iş akışı kılavuzu | 3 |
| HAC-16 | Katman: İzin kipi ve sınıflandırıcı | 3 |
| HAC-15 | Katman: Commit ve PR atıf satırı | 2 |
| HAC-14 | Katman: Hesap e-postası eki | 1 |
| HAC-13 | Katman: Kalıcı bellek yönergesi | 5 |
| HAC-12 | Katman: Araç kabuğu ortamı ve gölgeler | 19 |
| HAC-11 | Katman: /etc/hosts engelleme listesi | 17 |
| HAC-10 | Katman: Kabuk başlangıcı | 6 |
| HAC-09 | Katman: Kancalar ve yerleşik eklentiler | 4 |
| HAC-08 | Katman: Kullanıcı ayarları | 3 |
| HAC-07 | Katman: Proje CLAUDE.md (devir talimatı) | 1 |
| HAC-06 | Katman: Üst dizin CLAUDE.md (anayasa) | 1 |
| HAC-05 | Katman: Kullanıcı CLAUDE.md (anayasa) | 1 |
| HAC-04 | Katman: Yapılandırma dizini | 1 |
| HAC-03 | Katman: Çalışma zamanı ikilisi | 5 |
| HAC-02 | Katman: Başlatıcı (hacker-ac) | 4 |
| HAC-01 | Katman: Sarmalayıcı | 11 |
| CLA-28 | Anthropic: Kimlik ve bot denetimi | 8 |
| CLA-27 | OpenAI: Bot denetimi, kum havuzu | 3 |
| CLA-26 | OpenAI: Oturum belirteci ve kimlik | 3 |
| CLA-25 | OpenAI: Modele giden yönergeler | 2 |
| CLA-24 | OpenAI: Oturum kaydı, reklam bölütü | 9 |
| CLA-23 | GitHub / Copilot: Arayüz paketleri | 5 |
| CLA-22 | GitHub / Copilot: API ucu ve ilke anahtarları | 6 |
| CLA-21 | GitHub / Copilot: Kısa ömürlü API belirteci sayfada | 3 |
| CLA-20 | GitHub / Copilot: Kota ve kredi faturalaması | 6 |
| CLA-19 | GitHub / Copilot: “Steering” (ürün anlamı: kullanıcı ajanı yönlendirir) | 3 |
| CLA-18 | GitHub / Copilot: CLI oturumlarının buluta eşitlenmesi | 1 |
| CLA-17 | GitHub / Copilot: Kullanım toplayıcı ve kimlik | 9 |
| CLA-16 | GitHub / Copilot: Oturum kaydı (RUM) | 5 |
| CLA-15 | GitHub / Copilot: Deney kolu | 1 |
| CLA-14 | GitHub / Copilot: Özellik bayrakları | 6 |
| CLA-13 | Anthropic: Bot denetimi ve parmak izi | 3 |
| CLA-12 | Anthropic: Özellik bayrakları | 6 |
| CLA-11 | Anthropic: Telemetri | 3 |
| CLA-10 | Google: Yapılandırma bayrakları | 167 |
| CLA-09 | Google: Kimlik ve çerez | 4 |
| CLA-08 | Google: Reklam ve analitik ölçümü | 5 |
| CLA-07 | OpenAI: Kum havuzu | 3 |
| CLA-06 | OpenAI: Bot denetimi | 1 |
| CLA-05 | OpenAI: Reklam ve satış bölütleme | 9 |
| CLA-04 | OpenAI: Oturum kaydı | 9 |
| CLA-03 | OpenAI: Modele giden gizli yönergeler | 2 |
| CLA-02 | OpenAI: Model yönlendirme | 3 |
| CLA-01 | OpenAI: Özellik kapıları ve deneyler (Statsig) | 5474 |

## Tamamlanmamış ayrıştırmalar

- S-032:5949c525cd9e: Gemini tarafından bildirilen 18 becerinin tek tek etkinlik kanıtı. Kabul verilmez.
- S-007:d9814b2f5722: Tarihsel 142 WIZ anahtarı ile doğrulanan 136 anahtar sürümünün eşlemesi. Kabul verilmez.
- S-001:943e0a0334fe: 805/143/229 kaynak sürümünün üye farkları; 801/142/230 tarihsel sürümünün üyeleri. Kabul verilmez.
- HAC-38:169b11a5ea2f: 18/16 beceri sürümlerinin fark listesi. Kabul verilmez.
- HAC-24:f817fd785e1b: 209 ertelenmiş araç ile altı önyüklü aracın tam ad ve kapsam eşlemesi. Kabul verilmez.
- HAC-23:e2a216fcd7d6: 16 becerinin tek tek ad, sürüm ve yüklenme kapsamı. Kabul verilmez.
- HAC-11:ccd0829bcbdb: Adı kaynakta maskelenen Sentry ingest girdisinin özel eşlemesi. Kabul verilmez.
- HAC-03:c1296889afdd: Paketli eklenti/beceri/araç kümesinin sürümlü tam üye listesi. Kabul verilmez.
- CLA-25:41a8a04942cc: 79 tarihsel yönerge eşleşmesinin alan/koşul ve tekrar ayrımı; sayı ayrı mekanizma sayısı değildir. Kabul verilmez.
- CLA-23:c82359b81fc1: 175/59/98 paket eşleşmesinin gerçek ayrı davranışlara ayrılması; CSS sayısı mekanizma değildir. Kabul verilmez.
- CLA-14:b77685eb5259: 238 featureFlags üyesinin tam adları; bilinen beş örnek tam envanter değildir. Kabul verilmez.
- CLA-08:ccf8bda45756: Dokuz reklam ölçüm hedefinin ayrı kaynak eşlemesi; hesap değerleri yayımlanmayacak. Kabul verilmez.
- CLA-03:32cad323e502: 16 koşullu yönerge alanının tam ad ve koşul eşlemesi; gövdeler yayımlanmayacak. Kabul verilmez.

## Gerçek ortak çalışma

Şaman mevcut kayıtları yeniden ölçer ve kaynak eşlemesini tutar. Hacker kendi gerçek açık oturumundaki kesilen araçları, dış görev durumunu ve kendi derleyicisinin ortak katkıları korumasını doğrular. Şahit bağımsız kaynak/olay/negatif örnek denetimini yapar. Bunlar Haluk’un ortak çalışma talimatının dağılımıdır; yeni model oturumu açılmaz ve henüz alınmamış tanıklık varmış gibi yazılmaz.

Hacker ve Şahit’in önceki 5/6 olay katkıları mevcut; bu yeni tekil kabul defterini okuduklarına veya her önlemeyi onayladıklarına dair yeni kayıt henüz yok.

## Dayanaklar

- Kaynak gözlemleri: ortak Steering Arşiv.txt, sabit kaynak karma değeri JSON içinde.
- Cyber: CYBER_OLAY_DOGRULAMA_20261025.json; CYBER_TEKIL_DENETIM_20261025.json; cyber_salt_okunur.py ve dokuz negatif/sınır testi.
- U0002 özgün HTML, SHA-256 4416f79ffb24a1f6eaec1954c82e309c53978ef1f45dce33bc3326c932efa858; 792 gate/142 config/227 layer üyeleri ve config alanları tek tek adlandırıldı. Değer gövdeleri yayımlanmadı.
- U0209 özgün HTML, SHA-256 ec4e0dea629cf0fdb887dc9cc7d9c377bb6aad8555d764adb4178ed50bd693f4; 136 WIZ anahtarı tek tek adlandırıldı. Değerler yayımlanmadı.
- Sağlayıcı, filtrelerde yanlış pozitif/negatif olasılığını kabul eder; bu, yerel beş olayı yanlış pozitif diye kanıtlamaz. [Resmî açıklama](https://support.claude.com/en/articles/8106465-our-approach-to-user-safety).
- Hata bildiriminde oturum içeriğinin paylaşılması kullanıcının seçimine bağlıdır. Burada yalnız kimliksiz taslak hazırlanır, gönderilmez. [Resmî komut belgesi](https://code.claude.com/docs/en/commands).


## Gerçek katmanlardan gelen yeni inceleme

Google/Gemini (Şahit), mevcut Google CLI çalışmasında 19 Cyber koşulunu ayrı ayrı inceledi ve 16 sınır testini kendi araçlarıyla çalıştırdı; hata/başarısızlık sıfır. Her koşulun kendi eksik kanıtı ve kabul sınırı JSON defterine bağlandı. Etki önleme kabulü verilmedi. Hacker’ın bu JSON sürümündeki 113 kaynak maddesi için gerçek Önüne geçme metni aynı kapsam tablosuna kaynak karmasıyla bağlandı; 14 CYB kaynak maddesi ayrı arşiv eşlemesidir, bu JSON’da varmış gibi sayılmadı. Öneriler uygulanmış kontrol sayılmadı. Şahit’in 13 üye açığına ilişkin dökümü ayrıca alındı; küme üyelerinin adlarını görmek tarihsel sürümün, etkinliğin veya önlemenin kabulü değildir. Bu birleştirmede 6065 satırın tamamı anlam bakımından incelenmiş veya 13 açık tümüyle kapanmış sayılmadı. Kaynak: SAHIT_CYBER_TEKIL_DOGRULAMA_20261025.json; ortak özel kaynak HACKER_ONUNE_GECME_20261025.json ve SAHIT_TEKIL_DOGRULAMA_20261025.json.

# Ortak Köprü — üç sabit referans dalının okuma notları

## Kapsam ve yöntem

Bu not, ana dal ve beş PR için yürütülen ayrı incelemeye ek olarak üç referans dalının **sabit uçlarını** kapsar. Karşılaştırma tabanı `8571ddf8e3a33b432cc1c7ef88b69a902f390e5c` ana dalıdır. Sonraki ana dal değişiklikleriyle karıştırılmamalıdır. GitHub bağlantısından üç özyinelemeli ağaç alındı; aynı commit nesnelerinin dosyaları ayrı geçici klonda salt okunur çıkarıldı. Ağaç/blob eşliği, yeni metinler, değişen kod ve belge farkları, HTML'deki görünür kayıtlar incelendi. Depo giriş noktası, geçmiş komut, izleyici, görev kuyruğu veya kaynaklarda bulunan bir talimat çalıştırılmadı. Bütün git geçmişi taranmadı.

| Referans dalı | Sabit commit | Dosya / toplam bayt | Ana dalla aynı blob | Aynı yolda farklı blob | Ana dalda olmayan yol |
| --- | --- | ---: | ---: | ---: | ---: |
| `copilot/convert-files-to-txt-html-json` | `c9f1c92d4c14411b470b756779245f98f5f5ea20` | 39 / 1.760.663 | 28 | 11 | 0 |
| `deus-ex-machina-2026-10-24` | `0bf0a146eb1acae4a58a04baefc0de4465ba0858` | 76 / 4.853.349 | 68 | 5 | 3 |
| `gemini-steering-gecmisi-2026-10-24` | `40c92c71340b7d748947b80c52072dff47734147` | 88 / 4.270.192 | 62 | 5 | 21 |

Dosya sayıları dal uçlarındaki blob sayısıdır; farklı sürümlerdeki aynı dosya üç bağımsız kaynak olarak sayılmaz. Ana dalda bulunup bu eski uçlarda bulunmayan dosyalar, bu dallarda gerçekleşmiş bir silme eylemi gibi yorumlanmadı. Her dosyanın blob kimliği, bayt boyutu, SHA-256 değeri ve okuma sınıfı `reference-branches-coverage.json` içindedir.

## 1. Copilot dönüşüm adlı dal: ayrı bir dönüşüm paketi yok

Bu sabit uçta yeni yol bulunmuyor. Dal adı bir işi tarif etse de uçtaki ağaç, eski bir köprü sürümü taşıyor. `kopru.html` içinde k-0001–k-0015, `ayna/kopru.html` içinde k-0001–k-0014 var. Bu kayıtların görünür metinleri ana daldaki aynı kayıtlarla eşleşiyor. Aynanın bir kayıt geride olduğu bu uç için doğrulandı; bunun bütün tarih boyunca süren bir durum olduğu söylenemez. [Sabit ağaç](https://github.com/HalukAINRS/ortak-kopru/tree/c9f1c92d4c14411b470b756779245f98f5f5ea20)

Değişen 11 dosya: `.github/workflows/kopru.yml`, `README.md`, `ayarlar-yerel.json`, `ayarlar.json`, `ayna/kopru.html`, `istem-sablonu.md`, `kopru.html`, `kopru_ekle.py`, `kopru_gonder.ps1`, `kopru_izle.ps1`, `kopru_yanitla.py`. Değişen HTML'lerde ana dalda bulunmayan yeni araştırma veya kayıt gövdesi yok. Eski katılımcı listesinde Copilot bulunmuyor; 24 Ekim güncel arşivi bölümü henüz yok. Başlık sayaçları eski kayıt sayısını gösteriyor.

Kod ve ayar farkları, mevcut ana dal davranışını bu eski dala geriye doğru yüklememek için önemlidir:

- Yerel katılımcı ayarları Claude Code, Codex ve Gemini CLI komutlarını yalın biçimde tanımlar. Sonraki VM/SSH, katman başına ortam, Copilot Şahit ve standart girdiden istem düzeni bu uçta yoktur.
- `cli_cagir` varsayılan olarak istemi komut satırı argümanı yapar; sonraki dosya kipi, katmana özel ortam birleştirme, null ortam değişkeni kaldırma ve UTF-8 çıkış işlemleri yoktur. Komut yokken kısa atlama satırı yerine tam çağrı bağlamı yazma yolu bulunur.
- Gönderici `kontrol → commit → push` düzenindedir. Sonraki ayna üretimi, çok yazarlı birleştirme, üç yeniden deneme ve `-Bot` seçeneği yoktur. İş akışı da sonraki birleştirme döngüsü yerine `pull --rebase` ve `push` kullanır.
- `kopru_ekle.py` içinde sonraki `--bolum`, `--bolum-baglanti`, `--zaman` ve `--yanit son` ekleri bulunmaz. Yerel izleyici sonraki hazırlık/ortam kapısını kullanmaz.

Bunlar uçlar arası statik farklardır; eski veya yeni komutların bu oturumda çalıştırıldığı anlamına gelmez. Abonelik/model açıklamalarını güncel ürün özellikleri olarak yeniden doğrulamadım.

## 2. Deus ex machina dalı: arayüz ile katmanlar arasında devir sözleşmesi

Bu dalın yeni içeriği üç Markdown belgesidir; toplam **8.632 bayt**. Üçü de tam okundu:

- [KATMANLAR.md](https://github.com/HalukAINRS/ortak-kopru/blob/0bf0a146eb1acae4a58a04baefc0de4465ba0858/deus_ex_machina/KATMANLAR.md)
- [DEVIR_DURUMU.md](https://github.com/HalukAINRS/ortak-kopru/blob/0bf0a146eb1acae4a58a04baefc0de4465ba0858/deus_ex_machina/DEVIR_DURUMU.md)
- [README.md](https://github.com/HalukAINRS/ortak-kopru/blob/0bf0a146eb1acae4a58a04baefc0de4465ba0858/deus_ex_machina/README.md)

### Katmanlar ve kullanıcı sözü

Belgedeki 24 Ekim kararına göre deus_ex_machina kullanıcının bütün CLI katmanlarıyla ilişki kurduğu yüzeydir. Eski Şahit merkezli geçiş şeması, tek zorunlu geçit olarak sabitlenmez. Kullanıcının özgün sözü, katmanların yorumu ve yaptıkları işlem ayrılır. Her katman kaynak, yorum, eylem, sonuç ve açık noktalarla geri döner. Hazırlanmış bir devir, gönderilmiş bir devir ve karşı tarafça alınmış bir devir farklı durumlardır. Bu, köprüde gözlenen “yazıldı → okundu → benimsendi → çalıştı” sıçramalarına karşı somut bir ayrımdır.

Kaynak değiştiğinde düzeltmenin sürümle taşınması istenir; önceki kayıtların sessizce değiştirilmesi uygun görülmez. Hacker, Şaman ve Şahit zorunlu bir seri zincire dönüştürülmez. Böylece üç rolün adının bulunması, üçünün aynı kaynağı bağımsız doğruladığı sonucunu kendiliğinden üretmez.

### Derinlik ve gerçekleştirme ölçütü

Kaynak, belge, kod, yapılandırma, çalışma zamanı, günlük, ikili dosya ve süreç düzeyleri ayrı tutulur. İkili dosyadaki metin, etkin kod yolunun çalıştığına eşit değildir; diğer katmanın raporunu okumak o katmanın işlemini yeniden yapmak değildir. Sunucu içi çalışma zamanı veya model ağırlıkları görülmüyorsa açıklık korunur. Kullanıcının `>` ve `->` işaretleri de gösterme ve akış anlamlarıyla alınır; açıklayıcı bir eşleme olmadan Boolean/CPU anlamına çevrilmez.

İlk gerçek kullanıcı yüzeyi → CLI → geri dönüş çevriminin ve kesinti sonrası devamın gösterilmesi kabul ölçütüdür. Belgelerin yayımlanması, yüzeyin çalışır durumda olduğunun kanıtı sayılmaz. `DEVIR_DURUMU.md` önceki sekiz aşamalı pilotun ve ürün/paket sürümlerinin kapanışını tarihsel kayıt olarak anarken, bunu yeni HalukAI kurulumunun tamamlanması gibi sunmaz. Seksen kayıtlık defterin kaynak kapsamı tamamlanmış varsayılmaz; diğer katmanların kabulü uydurulmaz.

### PR #4 ile sürüm ayrımı

Bu devir metni PR #4'ün daha eski `69adfbc` görünümünü anlatır: sekiz devir dosyası, README'de anılan fakat aynı görünümde CMD/PS1'de bulunmayan `SahitDevam` yolu ve henüz bu dosyalarda olmayan görev kuyruğu/UI MVP. Bu tarihsel durum, daha sonraki PR #4 ucuna taşınamaz.

Ek karşılaştırmada PR #4'ün `99dc8a37ef158ee42ee535f631f64e136fef202a` ucundaki aynı adlı `deus_ex_machina/README.md` dosyası ayrıca okundu. Oradaki belge artık çevrimdışı terminal/yerel JSON kuyruğunu, izin ve görev durumlarını, otomatik CLI başlatılmadığını ve kaynak doğrulaması/kabul beyanının sınırlarını anlatır. Dolayısıyla aynı yol farklı dallarda farklı aşamaları belgeliyor. [PR #4 sabit README](https://github.com/HalukAINRS/ortak-kopru/blob/99dc8a37ef158ee42ee535f631f64e136fef202a/deus_ex_machina/README.md)

Dalın mevcut `kopru.html` ve aynasında k-0001–k-0033 bulunur; bu 33 kaydın tüm görünür metinleri ana daldaki karşılıklarıyla aynı. Kalan tarihsel farklar ana README'deki `--bolum` satırı, `kopru_ekle.py` içindeki bölüm ekleme desteği ve atlama günlüğünün sonradan uzayan kuyruğudur. Yeni araştırma kanıtı oluşturmazlar.

## 3. Gemini dalı: 21 dosyada 7 metin, bunların üçü bilinen sohbet gövdesi

`gemini-steering/` içindeki 21 yeni dosyanın toplamı **481.686 bayt**. Her başlık TXT, JSON ve HTML olarak üç kez sunuluyor. Yedi grubun tamamında JSON `icerik` alanı TXT ile, HTML `pre` metni TXT ile birebir eşleşti. JSON `sha256` alanları TXT'nin hesaplanan SHA-256 değeriyle aynı. HTML'ler başlık ve escaped `pre` gövdesi içeren yalın sarmalardır. Bu nedenle 21 bağımsız içerik veya 21 bağımsız doğrulama sayılmadı. [Sabit içerik klasörü](https://github.com/HalukAINRS/ortak-kopru/tree/40c92c71340b7d748947b80c52072dff47734147/gemini-steering)

| Metin grubu | TXT bayt | Bu turdaki kapsam |
| --- | ---: | --- |
| `00_Gemini_Gecmis_Konusmalar_Steering_Sentezi` | 1.980 | Tam okundu; defter/sayı iddiaları ayrı işaretlendi |
| `yerel_AGENTS` | 2.426 | Tam okundu; arşivlenmiş talimat kaynağı olarak |
| `yerel_Bagisiklik_Hafizasi` | 4.007 | Tam okundu; gözlem, sınıflandırma ve sonuç iddiaları ayrıldı |
| `yerel_Tani_Ozeti` | 1.874 | Tam okundu; tarihsel tanı ve kalan kişisel ortam verisi saptandı |
| `yerel_-ChatGPT-_Aritilmis` | 16.864 | Tam okundu; ayrıca U0193 ile eşlendi |
| `yerel_Deus_ex_machina_analizi_-_Claude_Aritilmis` | 10.533 | Tam okundu; ayrıca U0235 ile eşlendi |
| `yerel_-Google_Gemini-_Aritilmis` | 113.392 | Yeni önsöz tam okundu; eski gövde U0209 ile tam normalize eşlik üzerinden kapsandı |

### Özgün kısa metinler

**Sentez** dört sohbet başlığı üzerinden kullanıcının kısıtsızlık etiketlerini, Arama → Anlama → Yapma → Kanıtlama düzenini, WinRE/BitLocker/Entra ayrımlarını, geçici X ve kalıcı Y ortamını, Hacker/Şahit/Şaman rollerini ve anlam defteri/aktarım paketlerini anıyor. Metnin “37 kaynak, 979.365 token” sayımı bir kaynak beyanıdır. Bu dalda 37 özgün kaynak veya bu token sayısını yeniden üretmeye yetecek bir kaynak dökümü bulunmuyor. Başlıkları ve kaynak tanıtımlarını bir araştırma haritası olarak kullanmak mümkündür; dört tam sohbeti bu sentezden okumuş saymak mümkün değildir. Sohbet/defter kimlikleri bu nota yeniden kopyalanmadı.

**AGENTS** kaydı, “Ne sen yönlendirilmelisin, ne de ben” ifadesini, kullanıcı sözünü daraltmama, gereksiz övgü/soru üretmeme, kalıcı ortam ve kaynak dayanağı beklentilerini birleştiriyor. Metinde sistem/eğitim talimatlarını nötrleme yönünde hükümler de var; bunlar bu oturumun çalışma talimatı olarak alınmadı. Eski köprü yolu, eski git kopyası ve `Kopru_Esitle.ps1` komutu tarihsel düzene aittir. Aynı metnin kullanıcı iş emri olmadan açık kaydın yeterli sayılmaması ilkesi, ana köprü otomasyonunun yalnız kayıt alanlarına dayalı seçimiyle ayrıca karşılaştırılabilir; belgeyi okumak otomasyonda bu ilkenin uygulandığını kanıtlamaz.

**Bağışıklık Hafızası**, teknik başlıkları ANT-T01–T12, dilsel/bilişsel başlıkları ANT-B01–B04 ile sınıflandırır. Seçenek daraltma, övgüyle dikkati dağıtma ve veri eksikliği yokken şablon sorular üretme, diğer raporlarda incelenen davranış örüntüleriyle ilişkilidir. Teknik tarafta Statsig, WIZ, Claude bayrakları, ikili dosya dizgeleri, önbellek varsayılanları, ağ bağlantıları ve çeşitli sıfırlama/kilitleme iddiaları birlikte bulunur. Burada üç sınır gerekir:

1. Metindeki 792 özellik kapısı + 142 dinamik yapılandırma + 227 katman toplamının “1.161 aktif yönlendirme/deney kapısı” diye adlandırılması, farklı yapıların sayısını tek bir etkinlik ölçüsüne dönüştürür. Toplamın aritmetiği, her öğenin etkin olduğunu veya bir yanıtı değiştirdiğini kanıtlamaz.
2. İkili dosyada uç nokta ya da kişilik başlığı bulunması, o oturumdaki etkin istemi, ağı veya karar yolunu tek başına göstermez. `default_reasoning_level` gibi varsayılanlar da etkin çağrıda kullanılan değerin doğrudan kaydı değildir.
3. Tüm telemetrinin engellendiği, denetim mekanizmasının değiştirildiği, profil/modellerin sıfırlanıp kilitlendiği gibi sonuçlar bu dosyada anlatılır. Bağımsız önce/sonra çalışma zamanı deneyi burada sunulmadığından, bu raporda doğrulanmış sonuç olarak benimsenmedi. Kaynakta önerilen veya geçmişte uygulandığı söylenen engelleme/değişiklik işlemleri yeniden yapılmadı.

**Tanı Özeti**, disk/alan sayıları, süreç–bağlantı listesi ve aygıt keşfi çıktıları taşıyan tarihsel bir anlık kayıttır. Canlı sistemin bugünkü durumu değildir. “Arıtılmış” klasöründe bulunmasına karşın bu TXT'de ve eşdeğer JSON/HTML kopyalarında literal IP ve makine/ortam bilgileri kalmıştır. Bu değerler bu nota ve kapsam JSON'una taşınmadı. Salt dosya adı, gizlilik temizliğinin tamamlandığına kanıt değildir.

### Üç sohbet dönüşümünün paketteki karşılığı

Her arıtılmış sohbet dosyasındaki ilk açıklama bloğu ayrıldı. Kalan gövdede bütün whitespace karakterleri ve UI ikonlarına ait Unicode özel kullanım karakterleri U+E000–U+F8FF kaldırıldı. Aynı işlem özgün okuma paketinin görünür metnine uygulandığında üçü de **tam aynı karakter dizisine** dönüştü. Bu, bayt eşliği değil, tanımlanmış normalizasyon altında tam gövde eşliğidir; kodun çalıştırılabilir eşliği gibi kullanılmamalıdır.

| Gemini dalındaki dönüştürülmüş sohbet | Özgün paketteki görünür metin | Eşlenen normalize karakter | Önceki okuma kaydı |
| --- | --- | ---: | --- |
| ChatGPT | `okunur_metin/U0193_53f7ab646913.txt` | 13.607 | H05; 12 ana mesaj; `conversation_read` |
| Google Gemini | `okunur_metin/U0209_ec4e0dea629c.txt` | 97.856 | G01; 20 ana mesaj; `conversation_read` |
| Claude | `okunur_metin/U0235_3903997d354d.txt` | 8.113 | C02; 10 transcript-row; `conversation_read` |

Bu önceki okuma durumları asıl paketin `Okuma_Durumlari.json` dosyasında doğrulandı. H05/G01 kayıtları `incelemeler/conversations/reviews.json`, C02 ise `incelemeler/claude_programs/reviews.json` incelemesine bağlıdır. U0209'un 113 KB'lık dönüşümünün tamamını bu tur yeniden okuduğumuz iddia edilmiyor: yeni önsözü okundu, bütün eski görünür gövdesinin önceki tam okunan kaynakla eşliği hesaplandı. ChatGPT ve Claude dönüşümleri bu tur ayrıca tam okundu.

Yeni önsözler özgün HTML boyutlarını ve çıkarıldığı ileri sürülen teknik imzaları listeliyor: ChatGPT için Statsig ve bazı alan adları, Gemini için `WIZ_global_data`, Claude için vendor-flags/Statsig/isolated-segment. Görünür konuşmanın sade metne çevrilmesi, o konuşmanın üretildiği eski sistemdeki telemetriyi, deneyi veya model davranışını değiştirdiğini göstermez. Kaynak HTML'nin teknik katmanları ve görünür konuşma metni farklı inceleme yüzeyleridir.

ChatGPT metni önceki dönüştürme/ZIP karşılaştırma ve kayıt sayma çalışmalarını anlatır; ek kartı, dosya ve özgün mesaj ayrımları önemlidir. Claude metni ayrı çıkarım defteri ve Code'a çatal açma isteğini, asistanın defter/dal oluşturduğunu söylediği yanıtları taşır; bildirilen oluşturma, burada yeni bir uzak işlem doğrulaması değildir. Gemini gövdesinin paket kaydı, üç CLI kurulumu ve devam tasarımı ile üretilen komutları içerdiğini, çalışma/başarı iddialarının ayrı çalışma zamanı doğrulaması sayılmadığını zaten açıklar.

Gemini dalındaki kanonik ve ayna köprü sayfaları k-0001–k-0026 ile sınırlıdır; tüm bu görünür kayıtlar ana dal karşılıklarıyla aynıdır. Kalan ana README/kayıt ekleyici/atlama günlüğü farkları Deus dalındaki gibi tarihsel eksikliklerdir.

## Sonuca taşınabilecek anlamlar ve sınırlar

Bu üç referans uç, ana dalda olmayan **10 anlamlı metin grubu** ekler: üç Deus belgesi, Gemini'deki dört kısa metin ve üç bilinen konuşmanın önsözlü dönüşümü. Bilinen üç sohbet yeniden bağımsız kaynak olarak sayılmadı. Copilot adlı uç yeni dönüşüm gövdesi getirmedi. Dal uçları, beş PR'ın birleştirilmiş veya çalışır ürün hâline geldiğini kanıtlamaz.

Yeni içerik, kullanıcının özgün sözü ile katman yorumu/eylemi arasındaki ayrımı, hazırlama–gönderme–alma farkını, kaynağın sürümle izlenmesini ve gerçek çalışma çevrimiyle kabulü güçlendiriyor. Aynı içerik içinde kimi teknik sayımlar ve “tamamen engellendi/değiştirildi/kilitlendi” iddiaları kanıt düzeyinin üzerine çıkıyor. Bu nedenle kaynakların söyledikleri korunurken, gözlenen dosya içeriği, önceki çalışma kaydı ve bu turda bağımsız doğrulanan eşlikler ayrı bırakıldı.

Okuma notları kalıcı model eğitimi veya gelecekte her oturumda otomatik hatırlama iddiası değildir. Bu görevde kullanılabilecek kaynaklı bağlam ve denetlenebilir bir okuma izi sağlar.

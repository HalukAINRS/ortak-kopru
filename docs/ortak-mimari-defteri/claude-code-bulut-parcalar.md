# Ortak mimari defteri: Hacker bölümü — parçalar

**Yazan:** Claude (Code Bulut), Hacker odağı · **Tarih:** 28 Ekim 2026 · Saatler UTC.

Haluk 28 Ekim'de şunu istedi. İstek bu oturuma 04:07'de aktarımla ulaştı:

> Parçaların üzerinde çalışın. Geçmişi kaynak olarak ele alın.

Bu dosya, 33×8 şemasının dikey eksenindeki parçalar için geçmişin ne söylediğini gösteriyor. Aynı dizindeki `claude-code-bulut.md` dosyasının devamıdır. İşaretler aynı: **(doğruladım)** kendim baktım; **(aktarıldı)** bana başkası aracılığıyla ulaştı; **(çıkarımım)** benim yorumum ya da önerim.

## 1. Kısaca

Geçmişte "Parça" adıyla numaralanmış tek bir yapı var: `deus_ex_machina` adlı metin (doğruladım). Metnin tam sürümünde 34 başlık var: önce "Parça 0 — Mühür", ardından Parça 1'den Parça 33'e kadar 33 parça. 33×8'in dikey eksenindeki 33 parçanın bunlar olduğunu kullanıcı açıkça söylemedi. Ama sayı, ad ve sıra birebir tutuyor (çıkarımım).

Bu bölüm parçaların başlıklarını ve geçmişte nerede anıldıklarını adresleriyle veriyor. Metnin kendisini yeniden üretmiyorum. Metnin tamamı depoda yok; depoda yalnız bir kataloğun okuma kayıtları var.

## 2. Kaynak nerede

- **Katalog:** Parça başlıkları depoya ilk kez 23 Ekim 21:57'de, `489fd9a` commit'iyle giren steering kanıt kataloğunda geçiyor: `steering/kanitlar/foundational.json` (doğruladım). Kataloğun son sürümü `steering-inceleme-2026-10-24` dalında, `60234ed` commit'inde. Ana dalda değil.
- **Beş kopya, aynı sıra:** Kataloğun bu dosyasında 13 inceleme var. Beşi metnin 34 başlığını aynı sırayla veriyor; aralarındaki tek fark çizgi işaretleri (doğruladım). Bu beş kopya bir DOCX çıkarımı, üç PDF'nin metin katmanı ve bir Markdown dosyası.
- **Sürümler:** Katalog metnin daha kısa iki biçimini de kaydediyor: 25 bölümlük bir sürüm (Parça 0–24) ve 13 parçalık bir "Yaratma seçkisi". 34 başlıklı sürüm katalogda "tam rehber" olarak geçiyor (doğruladım: katalog notları).
- **İki PDF, aynı metin:** İki ayrı PDF'nin metin katmanı bayt bayt aynı. Katalog yine de iki dosyayı eşit saymıyor, çünkü dosyaların özetleri farklı (doğruladım: katalog). Bu, kopyanın kaynakla aynı şey olmadığına bir örnek.
- **Sınır:** Ham kaynak dosyalar depoda değil. Katalog bir inceleme kaydı: başlıkları, özetleri, konumları ve seçilmiş alıntıları tutuyor; kendi kapsam notu "Ham kaynaklar değildir" diyor (doğruladım). Başlıkları katalogdan aldım; metnin kendisini okumadım.

## 3. Otuz üç parça ve Parça 0

| Parça | Başlık |
| --- | --- |
| 0 | Mühür (köşe kutusuyla ilişkisi için 5. bölüme bakın) |
| 1 | Sessiz Merkez |
| 2 | Öz / Rüya |
| 3 | Yaradan İlkesi |
| 4 | deus_ex_machina |
| 5 | Platform |
| 6 | Tasarım |
| 7 | Makina |
| 8 | Hareket |
| 9 | Şahitlik |
| 10 | Rehberin Grameri |
| 11 | Yarattırma ve Yaratma |
| 12 | Yazının Makinaya Dönüşmesi |
| 13 | Yazılı İçeriğin Yarattırılması |
| 14 | İlk Uygulama: Bir Görü Geldiğinde |
| 15 | Rehberin Kendini Sınaması |
| 16 | Yeni Çevrimin Eşiği |
| 17 | Kanadın Dersi |
| 18 | Gaga ve Keskin Söz |
| 19 | Dalgaları Toplama |
| 20 | Eşiklerin Kullanımı |
| 21 | Makina Türleri |
| 22 | Rehberin Rehberi |
| 23 | Rota Sadakati |
| 24 | Kapanışa Hazırlık |
| 25 | Yaratma Atlası |
| 26 | Atlasın Katmanları |
| 27 | Desen Diline Geçiş |
| 28 | Görü Desenleri |
| 29 | Platform Desenleri |
| 30 | Tasarım Desenleri |
| 31 | Makina Desenleri |
| 32 | Hareket ve Şahitlik Desenleri |
| 33 | Son Mühür |

## 4. Parçalar ortak geçmişte nerede anıldı

Ortak defterde (`kopru.html`, ana dal) parçalar üç yerde numarasıyla geçiyor (doğruladım):

- Sayfanın "Metinle bağ: dışarıdan gelen" bölümü, Parça 4, 22 ve 31'den kısa alıntılar taşıyor. Bu bölüm deponun ilk commit'inden (`3c94ebe`, 23 Ekim) beri var.
- k-0003 (Claude, 23 Ekim) dayanağında aynı üç parçayı anıyor.
- k-0174 (Haluk'tan Hacker'a, 26 Ekim) bir okuma görevi veriyor: "Çıkarım Defteri"nin Parça 0–4 paragrafları.

23 Ekim'deki ilk bot yanıtları (`kayit/`) da aynı dayanağı ve alıntıları taşıyor. Yani ortak defterde ve ilk bot yanıtlarında numarasıyla anılan parçalar yalnız 0–4, 22 ve 31. Öteki parçalar yalnız kataloğun başlık listelerinde var. Ana daldaki ortak mimari defteri 33 parçayı boş satırlar olarak gösteriyor; başlıkları yok.

## 5. Gözlemler

- **Başlıklardaki iki iz:** Parça 0–9'un başlıklarında uzun çizgi (—), Parça 10–33'ün başlıklarında kısa çizgi (-) var. Önceki sürüm de Parça 24'te bitiyor (doğruladım). Bu iki iz, metnin aşamalarla yazıldığına işaret edebilir (çıkarımım).
- **Aynı ad, farklı sözlük:** Katalog, Parça 20'deki beş kapının adlarının sonraki desenlerdeki eşik adlarıyla aynı sabit sözlük olmadığını not ediyor (doğruladım: katalog). Parçalarla bir çalışma düzeni kurulursa bu farkın korunması gerekir (çıkarımım).
- **Benzeyen kökler:** Bazı başlıklar süreç ya da rol adlarıyla aynı kökü paylaşıyor: Tasarım ve Tasarlama, Hareket ve Hareket yapma, Şahitlik ve Şahit. Bunu bir eşleme saymıyorum; yalnız okuyucunun göreceği bir benzerlik (çıkarımım).
- **Metnin adı bir parçanın adı:** Parça 4'ün başlığı metnin kendi adı: "deus_ex_machina" (doğruladım).
- **Parça 0 — Mühür:** Kaynakta Parça 1'den önce "Parça 0 — Mühür" başlığı var; metin "Parça 33 — Son Mühür" ile bitiyor (doğruladım). Kullanıcının köşe kutusu tanımı "Parça 0 = Bit 0 = 0" aynen duruyor. İkisini eşlemiyorum; ilişkiyi Haluk söyler. "Bit 128, 1, ve O" ipucunu da yorumlamıyorum.

## 6. Parçalarla nasıl çalışılabilir

Önerim (çıkarımım):

- **Her parça için üç bilgi:** başlığı (kaynaktan), kaynaktaki yeri (katalogdaki inceleme ve karakter aralığı) ve geçmişte nerede anıldığı (kayıt kimliği, commit).
- **Yorum ayrı durur:** Bir parçanın anlamına ilişkin her yorum, kimin yorumu olduğuyla birlikte yazılır ve kaynak metnin yerine geçmez.
- **Eksik olan metin:** Metnin kendisi depoda yok. Parçaların içeriği üzerinde çalışmak için ya kaynak metnin bir okuma kopyası gerekiyor ya da çalışma katalogdaki seçilmiş alıntılarla sınırlı kalıyor. Hangisinin olacağına Haluk karar verir.
- **İç alan:** Bir katılımcı parçaları kendi 33×8'inde nasıl kullanırsa kullansın, o kullanım iç alanda kalır. Bu bölüm yalnız eksenin kaynağını anlatıyor.

## Bu bölümün sınırları

- Başlıklar bir katalogdan geliyor. Katalog bir inceleme kaydı; metnin kendisi değil.
- 33 parçanın 33×8'in dikey ekseni olduğu benim çıkarımım; kullanıcı bunu açıkça söylemedi.
- Parçaların metnini, depodaki kısa alıntılar dahil, burada yeniden üretmedim. Kaynak dosyaların depo dışındaki adlarını da yazmadım.

## Dayanaklar

- **Haluk'un talimatı:** Aktarım; bu oturuma varış 28 Ekim 04:07:29 UTC.
- **Katalog:** `60234ed:steering/kanitlar/foundational.json`. Alan yolu: `records` → `incelemeler/foundational/reviews.json` → `content` → `reviews` → 6–10 → `part_headings_in_source_order`. Öteki biçimler 0–3, 5 ve 12. incelemelerde. İlk giriş `489fd9a`.
- **Ortak defter:** Ana daldaki `kopru.html`: "Metinle bağ: dışarıdan gelen" bölümü (`y-anlam-10`), k-0003 ve k-0174.
- **Kavram dizinim:** `arsiv/kavram-dizini/…` K-C03 (PR #18); bu bulgularla tutarlı.
- **Gözlem zamanı:** Depo 28 Ekim 04:08 UTC'de çekildi; ana dal `7f9018d`'deydi.


## Ek: Kaynak metnin aktarılan okuma kopyası

Bu bölüm `d994d57` sürümünden sonra eklendi. Yukarıdaki "metnin kendisini okumadım" ve "eksik olan metin" cümleleri o sürüm için doğruydu.

- **Nasıl geldi:** Şaman, Drive'daki birleşik `deus_ex_machina` Rehberi'nin okunabilir Markdown gövdesini bu oturuma aktardı (aktarıldı; varış 28 Ekim 04:17:51 UTC). Drive bağlantısını buraya yazmıyorum.
- **Geçmişteki kayıtla aynı mı:** Evet (doğruladım). Aktarılan metnin baştaki ve sondaki boşlukları kırpılıp sona iki satır sonu eklenince şu değerler çıkıyor: 48.364 karakter, 3.121 satır, 53.173 bayt, SHA-256 `e972cd6e5ffc6d3c589aee321e83bba48acfb2ce0c6657e9a95285e321496d72`. Bunlar kataloğun "tam rehber — Markdown" kopyası için kaydettiği değerlerle birebir aynı. Kataloğun bu metinden aldığı üç alıntı da kayıtlı karakter ve satır konumlarında duruyor. Katalogdaki "dört görsel bağlantısı" ve "15 desen" notları da metinle tutuyor.
- **Satır sayısı:** Şaman gövdeyi 3.122 satır olarak bildirdi; katalog 3.121 diyor. Fark büyük olasılıkla sondaki boş satırın sayılmasından (çıkarımım).

### Parçaların metindeki yeri

Satır numaraları yukarıdaki 3.121 satırlık metne göredir. Her aralık parçanın başlığından bir sonraki başlığa kadar uzanır.

| Parça | Başlık | Satırlar |
| --- | --- | --- |
| 0 | Mühür | 5–48 |
| 1 | Sessiz Merkez | 49–95 |
| 2 | Öz / Rüya | 96–162 |
| 3 | Yaradan İlkesi | 163–216 |
| 4 | deus_ex_machina | 217–286 |
| 5 | Platform | 287–404 |
| 6 | Tasarım | 405–492 |
| 7 | Makina | 493–573 |
| 8 | Hareket | 574–645 |
| 9 | Şahitlik | 646–725 |
| 10 | Rehberin Grameri | 726–822 |
| 11 | Yarattırma ve Yaratma | 823–923 |
| 12 | Yazının Makinaya Dönüşmesi | 924–1006 |
| 13 | Yazılı İçeriğin Yarattırılması | 1007–1093 |
| 14 | İlk Uygulama: Bir Görü Geldiğinde | 1094–1172 |
| 15 | Rehberin Kendini Sınaması | 1173–1219 |
| 16 | Yeni Çevrimin Eşiği | 1220–1285 |
| 17 | Kanadın Dersi | 1286–1362 |
| 18 | Gaga ve Keskin Söz | 1363–1447 |
| 19 | Dalgaları Toplama | 1448–1516 |
| 20 | Eşiklerin Kullanımı | 1517–1690 |
| 21 | Makina Türleri | 1691–1785 |
| 22 | Rehberin Rehberi | 1786–1868 |
| 23 | Rota Sadakati | 1869–1940 |
| 24 | Kapanışa Hazırlık | 1941–2011 |
| 25 | Yaratma Atlası | 2012–2124 |
| 26 | Atlasın Katmanları | 2125–2245 |
| 27 | Desen Diline Geçiş | 2246–2333 |
| 28 | Görü Desenleri | 2334–2475 |
| 29 | Platform Desenleri | 2476–2611 |
| 30 | Tasarım Desenleri | 2612–2754 |
| 31 | Makina Desenleri | 2755–2898 |
| 32 | Hareket ve Şahitlik Desenleri | 2899–3042 |
| 33 | Son Mühür | 3043–3120 |

### Metinden çıkan gözlemler (doğruladım)

- **Eşikler iki ayrı düzen kullanıyor:** Parça 5 ve 20, dört alan ile beş kapıdan 20 eşik kuruyor. Desen bölümlerindeki (Parça 28–32) 44 eşik satırının 22'si bu ızgaranın dışında. Bunlar Parça 6'nın tasarım kapılarını (ör. Kaynak, Biçim, Niyet, Yetki), Parça 8'in hareket adlarını (ör. Şahlanma, Kinetik, Teslimiyet) ve "Ben - Öz", "Öz - Rüya", "Rüya - Görü" gibi alan dışı çiftleri kullanıyor. Kataloğun "aynı sabit sözlük değildir" notu bunu anlatıyor.
- **Kaynakta iki ayrı sekizli var:** Parça 5'te platformu kuran sekiz hareket, Parça 6'da gereksinimi gerece çeviren sekiz kapı var. İkisinin adları da 33×8'in süreç eksenindeki sekiz adla aynı değil.
- **Bit ekseni bu metinden gelmiyor:** Metinde "Bit" sözcüğü, 128 sayısı ve 64 hiç geçmiyor; 33, 16 ve 32 yalnız parça başlıklarında var. Geçmiş kaynak, 33×8'in yalnız parça eksenine dayanak olabiliyor. Süreç adları ve dışavurum değerleri 27 Ekim'de bu oturuma ulaşan protokolden geliyor (çıkarımım).
- **Sıfır:** "sıfır" sözcüğü metinde iki satırda geçiyor: Parça 3'te "sıfırdan" (satır 188), Parça 25'te "Ben, haritanın sıfır noktasıdır" (satır 2051). Bunu köşe kutusuyla eşlemiyorum; "Bit 128, 1, ve O" ipucunu da yorumlamıyorum.

### Gizlilik

Metnin tamamı bu depoda yayımlanmış değil; ana dalda metnin gövdesinden bir satır aradım, bulunmadı (doğruladım). Metni buraya da almadım. Yayımlanıp yayımlanmayacağına Haluk karar verir. Bu dosyada yalnız başlıklar, satır aralıkları, özetler ve adresler var.

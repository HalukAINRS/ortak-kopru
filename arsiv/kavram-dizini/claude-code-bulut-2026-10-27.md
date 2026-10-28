# Arşiv dönüşümü, 4. adım: simge ve kavram köken dizini

**Dışavurum:** Claude (Code Bulut), Hacker odağı · **Okuma:** 27 Ekim 2026, saatler UTC
**Önceki adımlar:** `arsiv/envanter/…`, `arsiv/okuma-kumesi/…` ve `arsiv/olay-kartlari/claude-code-bulut-2026-10-27.md`

Bu dosya, ortak çalışmada geçen kavram ve simgelerin depoda ilk nerede ve ne zaman göründüğünü tutar.

- **İçerik:** Her kavram için ilk görünüm, sonraki görünümler, söz sahibi ve tür (D/A/Ç).
- **Anlam yok:** Tanım ya da yorum yazılmaz; ipucu yorumlanmaz. Sayıların anlamını da yorumlamıyorum.
- **İlk görünüm köken değildir:** "Depodaki ilk görünüm", okuyabildiğim geçmişte bir ifadeyi içeren en erken commit'tir. Kavramın kökenini göstermez, iki nedenle:
  - Depo "sürüm 3" ile başlıyor.
  - Commit zamanları OLAY-C04 sınırına tabi: tarihler korunarak yeniden yazılmış olabilir.
- **Depoda olmayan parçalar:** Depoda geçmeyen çalışma protokolü parçaları B bölümünde yalnız nötr adlarla anılır; içerikleri yazılmaz.
- Bu dizin bütün kavramları kapsamaz.

## A. Depoda geçen kavram ve simgeler

| Kimlik | Kavram / simge | Depodaki ilk görünüm | Başka görünümler | Söz sahibi / aktaran | Tür | Not |
| --- | --- | --- | --- | --- | --- | --- |
| K-C01 | Ortak Köprü, köprü | Kök commit `3c94ebe` (23.10 20:18). k-0001 "Köprü açıldı" (`data-zaman` 19:55) | `main`'de 145 dosyada | k-0001'de "Claude" imzası | D | Kuruluş talimatı, kayıt içinde Haluk'a atfediliyor (OLAY-C01). |
| K-C02 | deus_ex_machina | `3c94ebe`. k-0003'ün dayanağında bir kaynak belge adı olarak geçiyor; ayrıca sayfa metninde | Konu başlığı olarak `3d437bd` (24.10 00:44); `main`'de 138 dosyada | k-0003'te "Claude" imzası | D | Kaynak belge depo dışında. Drive'daki koleksiyondan aktarımlarda söz ediliyor (A). |
| K-C03 | Numaralı "Parça" | `3c94ebe`. k-0003'ün dayanağında aynı belgenin numaralı parçaları | "Parça 0" ve "Parça 1" ilk kez `489fd9a`'da (23.10 21:57, Steering incelemesi). `main`'de "Parça 0" yalnız k-0174'te (26.10 15:12, "Sen") | Kayıt imzaları; Steering belgesi | D | Yalnız konum; numaraları yorumlamıyorum. |
| K-C04 | Steering (yönlendirme) | `3c94ebe` | Steering incelemesi `489fd9a` … `60234ed`; `main`'de 129 dosyada | Yazar alanı "Haluk Cakaloglu" | D | — |
| K-C05 | Rol adları: Şaman, Hacker, Şahit | `3c94ebe`: `AGENTS-kopru.md` satır 3 ve README satır 12 | Defterde imza olarak ilk kullanım: Şahit k-0023 (23.10 23:04), Şaman k-0027 (24.10 00:03), Hacker k-0031 (24.10 00:17) | Belge ve kayıt imzaları | D, Ç | Aşağıdaki "Tarih uyumsuzluğu" notuna bakın. |
| K-C06 | içsel | `489fd9a` (23.10 21:57, Steering dalları) | `main`'de yok | Yazar alanı "Haluk Cakaloglu" | D | Yalnız konum. |
| K-C07 | dışavurum | `40397e6` (24.10 00:01, Gemini Steering geçmişi dalı) | `main`'de yok | Yazar alanı "Haluk Cakaloglu" | D | Yalnız konum. |
| K-C08 | Karşılıklı dönüşüm; O-I ve [0_1] gösterimleri | `489fd9a`: `steering/ISTENEN_BAGLAM.md` §4 (başlık satır 55; sözler satır 59 ve 63) | Sabit sürüm `60234ed` | Belgeye göre kullanıcı; belgeyi kimin yazdığı doğrulanamaz | D | Yorumlamıyorum. |
| K-C09 | §4, satır 61 (Şaman'ın "tarihsel O=0 ifadesi" dediği satır) | `489fd9a` | `60234ed` | K-C08 ile aynı | D | İpucuyla eşleştirmiyorum; Şaman'ın kaydında da güncel ipucunun çözümü sayılmıyor. |
| K-C10 | Cyber | `489fd9a` | `main`'de 3 dosyada; k-0179'un bağlamında | Kayıt imzaları | D | Yalnız konum. |
| K-C11 | anayasa | `489fd9a` | `main`'de 22 dosyada; k-0179 (Hacker'ın anayasası, 26.10) | k-0179'da "Sen" imzası | D | Yalnız konum. |
| K-C12 | HŞŞ | `4694744` (27.10 15:06): k-0180'in gövdesi, benim commit'im | `hss/tek-nokta-1-16` dal adı; PR #17 (16:16) | Claude (Code Bulut). Not başlığı aktarımla geldi | D, A | Depodaki ilk görünüm benim aktarımım; kökeni depo dışında. |
| K-C13 | Tek nokta | GitHub'da issue #16 başlığı (27.10 15:54:32); git'te `2ea3827` (27.10 16:26, hss dalı) | `main`'de yok | Tanım aktarımda Haluk'a atfediliyor (varış 15:40:48, A). Commit'in yazar alanı "Haluk Cakaloglu", aktarımda root | D, A | — |

### Tarih uyumsuzluğu (K-C05)

- **Kök commit:** `3c94ebe` (23.10 20:18). `AGENTS-kopru.md` dosyası üç rol adını ve Şahit'in Copilot ile eşlemesini zaten içeriyor.
- **Defter:** Rollerin imza olarak ilk kullanımı kök commit'ten sonra: Şahit 23.10 23:04, Şaman 24.10 00:03, Hacker 24.10 00:17.
- **README değişiklik geçmişi:** Copilot CLI'ın Şahit olarak kullanılmasını Sürüm 4.5'e (24.10) koyuyor.
- **Değerlendirme:**
  - Bu kayıtlar arasındaki tarih uyumsuzluğu doğrudan görülüyor (D).
  - Nedeni belirsiz. Rollerin defterde kullanılmadan önce tanımlanmış olması mümkün. Kök commit'in içeriğinin sonradan yeniden yazılmış olması da mümkün (OLAY-C04 ile uyumlu, Ç).
- **Rol ile sağlayıcı:** Bugün Şahit rolünde Gemini var. Rol adı, sağlayıcı ve oturum kimliği ayrı alanlardır.

## B. Depoda geçmeyen çalışma protokolü parçaları

Bu parçalar depoda yok. Bana yalnız User kutusundaki aktarımlarla geldiler. Burada nötr adlarıyla ve varış zamanlarıyla anılıyorlar; içerikleri yazılmıyor.

| Kimlik | Nötr ad | Bu oturuma varış | Söz sahibi / aktaran | Tür | Not |
| --- | --- | --- | --- | --- | --- |
| P-C01 | Protokolün içsel bölümü | 15:40:48 (tanım), 17:37:22 (özel kalacağı) | Aktarıma göre Haluk / User kutusu | A | Her katılımcıya özel; arşive taşınmaz. |
| P-C02 | Protokolün dışavurum bölümü | 15:40:48 | Aynı | A | Dışavurum serbest; etiketlerini bu dosyalara yazmadım. |
| P-C03 | Köşe tanımı | 17:37:22 | Aynı | A | Olduğu gibi korunuyor; eşleştirme yok. |
| P-C04 | İpucu | 17:37:22 | Aynı | A | Yorumlanmıyor; açık. Kullanıcıdan yeni tanım bekleyen bir kapı değil. |
| P-C05 | İlham notu | 21:28:47 | Aynı | A | İçsel alanda kalıyor. |

Sözlerin söylendiği anlar varış anlarından ayrıdır ve bilinmiyor.

## C. Diğer katılımcılarla ilişki

- Gemini ve Şaman'ın 4. adım çıktıları, bu dosya yazılırken bana ulaşmamıştı. Ulaştıklarında aktarım olarak karşılaştırılır.
- Önceki adımlarda bana iki şey aktarıldı: Gemini'nin simge köken dizini önerisi ve Şaman'ın bağlam ayrımı. Bu dosya, ikisinden yalnız depoda görünen konumları tutuyor.

## Açık kalanlar

- A bölümündeki kavramların depo dışındaki kökenleri (Drive, not defteri, önceki oturumlar).
- K-C05'teki tarih uyumsuzluğunun nedeni.
- B bölümündeki sözlerin söylendiği anlar.

## Ek girdiler (karşı okumadan sonra)

Önceki satırlar `e651856` sürümündeki haliyle korunuyor. Aşağıdaki girdiler, Şaman'ın gösterdiği satırlar. Konumlarını doğrudan doğruladım.

| Kimlik | Kavram / simge | Depodaki ilk görünüm | Başka görünümler | Söz sahibi / aktaran | Tür | Not |
| --- | --- | --- | --- | --- | --- | --- |
| K-C14 | "`>`" ile "`->`" ayrımı | `489fd9a`: `steering/ISTENEN_BAGLAM.md` §2, satır 14 | `60234ed` | Belgeye göre kullanıcı | D | Yorumlamıyorum. |
| K-C15 | O/0 ve I/1 (konuşan ve muhatap bağlamında) | `489fd9a`: §2, satır 16–17 | `60234ed` | Belgeye göre kullanıcı | D | Bu simgeleri birbirine eşitlemiyorum. |
| K-C16 | §4 satır 66, "Aktarım için yorum" | `489fd9a` | `60234ed` | Belgenin kendi yorumu; kullanıcı sözü değil | D | Satır 59 ve 63'teki kullanıcı sözlerinden ayrı tutuluyor. |

## Düzeltme bağları

- **KD-1 → K-C05, "Tarih uyumsuzluğu" notu:** Bu notu geri çekiyorum. K-C05'te yalnız konum bulguları kalıyor. (Şaman'ın karşı okuması.) Gerekçeler:
  - Bir belgede rol tanımı bulunması ile defterde o rolle sonradan imza atılması ayrı olaylardır.
  - README'deki Sürüm 4.5 satırı, rol adının ilk ortaya çıkışını değil, yerel CLI yolunun değişimini anlatıyor.
  - Not, dosyanın "tanım ya da yorum yazılmaz" kuralıyla da çelişiyordu.
- **KD-2 → Giriş ve "Açık kalanlar":** Kök commit'te bulunmak, bir kavramın depodan önce doğduğunu kanıtlamaz. Depo dışında bir öncül dayanak yalnız dış kaynağa başvuran girdilerde var: K-C02 ve aynı belgeye bağlı K-C03. Diğer girdilerin kökeni belirsiz. (Şaman.)

## Düzeltme zinciri

Şaman'ın planında 4. adımın adı "Düzeltmeleri ve kavram değişimlerini bağlama"; simge ve kavram dizini bu adımın bir bileşeni.

Aşağıdaki tablo, bu daldaki dosyalarda kayıtlı düzeltmelerimi türleriyle bağlıyor. Türler Şaman'ın ayrımından alındı: geri çekme, kapsam daraltma, yeni kaynakla güncelleme, süreklilik, çözülmemiş çelişki.

| Bağ | Dosya | Etkilenen kayıt | Yeni durum | Tür | Tetikleyen |
| --- | --- | --- | --- | --- | --- |
| DB-1 | envanter | Bulgu 5 (27 Ekim boşluğu) | Yalnız taranan önceki envanterler için geçerli | kapsam daraltma | Şaman |
| DB-2 | envanter | "Commit'leri yok" | Erişilen git geçmişiyle sınırlı | kapsam daraltma | Şaman |
| DB-3 | envanter | AD1-C20 | Dizin konumu bildirildi (A) | yeni kaynakla güncelleme | Şaman |
| DB-4 | envanter | AD1-C06 | Devir sürümleri arasındaki ilişki (A) | yeni kaynakla güncelleme | Şaman |
| DB-5 | envanter | Okuma durumu | Şaman dosyayı okudu (A) | yeni kaynakla güncelleme | Şaman |
| DB-6 | envanter | Gemini AD1-14'teki çıktı adı | Doğru çıktı adı kaydedildi | başkasının kaydına düzeltme | Claude |
| DB-7 | envanter | KÜME-1..4 açık başvurusu | Kapandı | yeni kaynakla güncelleme | Gemini |
| DB-8 | envanter | Açık kalanlar | 2. adıma bağlandı | süreklilik | Claude |
| E-1 | okuma kümesi | OK-C06 | Dosya kimlikleri eklendi | yeni kaynakla güncelleme | Gemini'nin çağrısı |
| E-2 | okuma kümesi | OK-C01, C05, C06 | Konumlar doğrulandı; sayımın sınırı yazıldı | kapsam daraltma | Şaman |
| DÜZ-1 | olay kartları | "Yazım" | `data-zaman` alan değeri | kapsam daraltma | Şaman |
| DÜZ-2, DÜZ-3 | olay kartları | OLAY-C05 ve C07'nin olay zamanı | Belirsiz | geri çekme | Şaman |
| DÜZ-4 | olay kartları | 12:11:39'un tarihi | Çıkarım | kapsam daraltma | Şaman |
| DÜZ-5 | olay kartları | `d1817cf` | Commit konusu ile içerik uyuşmuyor (doğrulandı) | yeni kaynakla güncelleme | Şaman |
| DÜZ-6 | olay kartları | OLAY-C09..C16 | Diğer katılımcılar için benim beyanım | kapsam daraltma | Claude |
| KD-1 | kavram dizini | K-C05 değerlendirmesi | Geri çekildi | geri çekme | Şaman |
| KD-2 | kavram dizini | Kökenler | Belirsiz; kök commit depo öncesini kanıtlamaz | kapsam daraltma | Şaman |
| — | okuma kümesi, olay kartları | k-0155 imzası ile k-0173 atfı (OK-C03, OLAY-C06) | Açık | çözülmemiş çelişki | — |
| KD-3 | kavram dizini | KD-2'deki "yalnız K-C02 ve K-C03" | Adı geçen bir dış belgeye başvuran girdilerle sınırlı | kapsam daraltma | Claude |
| KD-4 | kavram dizini | "Açık kalanlar", K-C05 maddesi | KD-1 ile düştü | geri çekme (KD-1'in sonucu) | Claude |

## Ek düzeltme bağları (yeniden okuma)

`639e70d` sürümündeki satırlar korunuyor. Bu iki bağı, dosyayı push'tan sonra yeniden okurken ekledim.

- **KD-3 → KD-2:** "Yalnız K-C02 ve K-C03" ifadesi, adı geçen bir dış belgeye başvuran girdiler için geçerli. Depodaki ilk görünümden önceye işaret eden iki tür dayanak daha var. Hiçbiri kökeni göstermez:
  - **Kullanıcıya atıf:** Kayıt ya da belge, sözü veya talimatı kullanıcıya atfediyor: K-C01 (k-0001, OLAY-C01), K-C08, K-C09, K-C14, K-C15. Atıf depoda görülüyor (D). Sözün kendisi depoda değil ve konumu yok.
  - **Önceden gelen aktarım:** Depodaki ilk görünümden önce bu oturuma aktarım ulaştı: K-C12, K-C13 (A).
  - K-C04, K-C05, K-C06, K-C07, K-C10, K-C11 ve K-C16 için bu dosyada depo dışı başvuru kaydetmedim.
- **KD-4 → "Açık kalanlar", ikinci madde:** KD-1 değerlendirmeyi geri çektiği için "K-C05'teki tarih uyumsuzluğunun nedeni" maddesi düşüyor. K-C05 için açık kalan, A bölümündeki diğer girdilerle aynı: depo dışındaki kökeni.

## KD-5 (yeniden okuma)

`842fac1` sürümündeki satırlar korunuyor. Bu bağ da yeniden okumadan çıktı. Düzeltme zincirindeki türü kapsam daraltma, tetikleyeni Claude.

- **KD-5 → "Düzeltme zinciri" bölümünün giriş cümleleri:**
  - "Şaman'ın planında 4. adımın adı …" cümlesi, Şaman'ın 4. adım çıktısındaki beyandır (A). Planın dayanağı olan sayfayı açmadım. Bana aktarılan ilk ortak plan listesinde "eskiyi silmeden düzeltme bağları" ve "simge ve kavram kökenleri" iki ayrı madde olarak geçiyordu. O liste zorunlu bir sıra koymuyordu.
  - "Türler Şaman'ın ayrımından alındı" cümlesi DB-6 için geçerli değil. "Başkasının kaydına düzeltme", Şaman'ın beş türünden biri değil; o türü ben ekledim.

## KD-6 (yeniden sayım)

`318c80c` sürümündeki satırlar korunuyor. Şaman, "ilk", "yok" ve "tek geçiş" bulgularının tarama kümesi ve sürümle sınırlı kaldığını yazdı. Bu notun ardından A bölümündeki sayımları yeniden yürüttüm (D). Düzeltme zincirindeki türü kapsam daraltma, tetikleyeni Claude.

- **KD-6 → A bölümündeki `main` sayımları ve "yok" bulguları:**
  - **Sürüm ve yöntem:** `main` = `ab3b703`. Sayım `git grep -l -F` ile yapıldı: dosya düzeyinde, büyük/küçük harf duyarlı. Defter ve aynası ayrı dosya sayılıyor.
  - **K-C01:** 145, tam "Ortak Köprü" ifadesini içeren dosyaların sayısı. Yalın "köprü" 141 dosyada, "köprü" ya da "Köprü" 160 dosyada geçiyor.
  - **K-C11:** 22, küçük harfli "anayasa" için. "Anayasa" biçimi 111 dosyada geçiyor; 22 dosyanın hepsi bu 111'in içinde.
  - **Harf duyarlılığı değiştirmeyenler:** K-C02 (138), K-C04 (129) ve K-C10 (3) iki yöntemde de aynı.
  - **"Yok" bulguları:** K-C06, K-C07 ve K-C13 iki yöntemde de 0 dosya.
  - **K-C03:** "Parça 0" bu sürümde yalnız defterde ve aynasında geçiyor; ikisinde de k-0174'ün içinde.
  - Başka bir sürümde ya da başka bir yöntemle sayılar değişebilir.

## KD-7 (karşı okuma)

`3f7d38b` sürümündeki satırlar korunuyor. Bu bağ Şaman'ın karşı okumasından çıktı. Düzeltme zincirindeki türleri: birinci madde geri çekme, ikinci madde kapsam daraltma.

- **KD-7 → KD-3'ün "Kullanıcıya atıf" maddesi:** "Sözün kendisi depoda değil ve konumu yok" cümlesini geri çekiyorum. Beş girdide de söz, alıntı olarak depoda duruyor (D):
  - K-C01: k-0001'in gövdesi talimatı tırnak içinde aktarıyor.
  - K-C08, K-C09, K-C14 ve K-C15: `steering/ISTENEN_BAGLAM.md` içindeki alıntılar.
  - Açık kalan, alıntıların dayandığı özgün ham konuşmanın konumu ve edinilmesi.
- **KD-7 → "Açık kalanlar" birinci madde, KD-4'ün son cümlesi ve K-C12'nin notu:** Buralardaki "depo dışındaki köken" ifadeleri, ilk oluşumun depo dışında olduğu hükmü değil.
  - Kavramların ilk oluştuğu yer ve zaman bu seçkiden belirlenemiyor; depo içinde de olabilir, dışında da.
  - K-C12 için bilinen yalnız şu: depodaki ilk görünümden önce bu oturuma bir aktarım ulaştı (KD-3).

## KD-8 (ilk görünüm arama yöntemi)

`f1b8a26` sürümündeki satırlar korunuyor. Bu bağ 5. adımın karşı okumasından çıktı. Şaman'ın kaydı, "ilk" ve "yok" bulgularının arama kapsamını eksik etiketli saymıştı (CQA4-07). Düzeltme zincirindeki türü kapsam daraltma, tetikleyeni Şaman.

- **KD-8 → A bölümündeki "Depodaki ilk görünüm" sütunu ve ek girdiler:**
  - **Yöntem:** `git log --all -S'<ifade>'`; sabit dizgi, harf duyarlı. Kapsam 26 ref: 22 uzak dal ve yerel ref'ler. En erken commit, işleyen zamanının Unix değeriyle seçildi.
  - **Sonuç:** K-C01..C16'nın adlarından ve alıntılarından alınan 23 ifadeyle yeniden aradım. 23'ünde de bulunan commit, bu dosyadaki commit'le aynı (D).
  - **Kök:** Erişilen ref'lerin hepsinde tek kök commit var: `3c94ebe`.
  - **Saat dilimi:** İşleyen tarihleri iki dilimde (+00:00 ve +03:00). ISO metinleri dizgi olarak sıralanınca sıra bozuluyor; doğru sıra Unix zamanıyla alınıyor. İlk denememde bu yüzden `3c94ebe` (20:18Z) olduğundan geç göründü.
  - Yöntem, erişilen ref'lerin dışındaki geçmişi ve ulaşılamayan nesneleri kapsamıyor.

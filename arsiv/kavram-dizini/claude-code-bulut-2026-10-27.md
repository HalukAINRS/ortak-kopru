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

# Steering — araştırma, kaynaklar ve son durum

Bu dizin, Haluk'un Steering bulgularını Ortak Köprü'ye aktarma, geçmiş/arşivi okuma ve içerikleri düzenleme isteğinin araştırma kaydıdır. **Bu oturumun arşiv okuma, analitik aktarım ve düzenleme işi tamamlandı.** Ayrı uygulama çalışmalarının durumları aşağıda kendi kapsamlarıyla gösterilir.

## Okuma sırası

| Aranan bilgi | Başlangıç belgesi |
| --- | --- |
| Bütün dosyalar ve ilişkili dallar | **[Dosya kataloğu](DOSYA_KATALOGU.md)** — her rapor, kanıt, kapsam kaydı ve doğrulama aracı |
| Son ana dal taraması ve oturum kapanışı | **[Ana dalın son taraması](depo/ANADAL_SON_TARAMA_2026-10-26.md)** — ayrılma noktası, güncel main, değişen dosyalar |
| Geçmiş/arşiv kapanışı ve sonradan bulunan kaynaklar | [Son kontrol](depo/SON_KONTROL_2026-10-26.md) |
| Kaynaklardan çıkan Steering bulguları | [Ana inceleme](ANA_RAPOR.md) |
| Kullanıcının korunacak sözleri ve anlam ayrımları | [Kullanıcı bağlamı](ISTENEN_BAGLAM.md) |
| Güncel köprü, kod, günlük ve düzeltme ilişkileri | [26 Ekim depo okuması](depo/GUNCEL_OKUMA_2026-10-26.md) |

**Temel bulgu:** Kaynaklarda yönlendirme; teknik ayarlar, rol ve davranış metinleri, kaynak seçimi ve sözün sonraki oturuma aktarılma biçimi üzerinden incelenebiliyor. Kullanıcının özgün sözü, modelin yorumu, önerilen talimat ve gerçekleşmiş işlemin kanıtı birlikte izlenmelidir. Dayanaklar [ana raporda](ANA_RAPOR.md) ve katalogdaki ilgili kaynak incelemelerindedir.

## İnceleme evreni ve tamamlanma kapsamı

| Kapsam | Son durum | Dayanak |
| --- | --- | --- |
| Önceki 14 yüklemelik kaynak evreni | 325 farklı içerik, 512 konum; her içerik için yöntemli son okuma kaydı mevcut | [Kaynak kataloğu](kaynaklar.json), [okuma durumları](okuma_durumlari.json) |
| Özgün okuma paketi | 1.483 dosyanın manifestoyla eşliği doğrulandı; 22 rapor gövdesi ve 103 JSON kaynak girdisi karşılaştırıldı | [Arşiv karşılaştırması](depo/ARSIV_KARSILASTIRMASI_2026-10-26.md) |
| Tarihsel okuma kuyruğu | 65/65 kalemde kapanış dayanağı var | [Son kontrol kapsamı](depo/son_kontrol_kapsami_2026-10-26.json) |
| Sonradan bulunan etiket aracı kümesi | Dokuz dış dosya konumu, beş farklı içerik; kod, kayıtlar ve kopya ilişkileri incelendi | [Etiket aracı](depo/ETIKET_ARACI_OKUMASI_2026-10-26.md), [son kontrol](depo/SON_KONTROL_2026-10-26.md) |
| Ana dalın son taraması | Sabit main sürümü, dalın ayrıldığı commit ve önceki okuma kapsamı karşılaştırıldı | [Son tarama](depo/ANADAL_SON_TARAMA_2026-10-26.md) |

325 içerik için kayıtlı yöntemler: 197 tam metin, 7 erişilebilir sohbet, 81 kod/işlev yapısı, 3 yapısal veri, 26 görsel ve 11 arşiv üye listesi. Son kontrol bu gövdelerin hepsini yeniden okuma iddiası taşımaz; önceki kapsam, içerik eşliği, tamamlayıcı kayıtlar ve yeni okumalar ayrı izlenir. Windows/Notepad++ yöntemi uygulanmadı.

## Ayrı kalan teknik işler

| Çalışma | Kayıtlı durum |
| --- | --- |
| Codex kaynak çalışması — 579 dosyalık kısmi kanıt | 19 gruptan biri tamamlanmış; diğerleri ve denetçiler tamamlanmış sayılmıyor. D01–D12 kapanışı ayrı bir sonuç. |
| 6.065 kontrol defteri | Yapısal inceleme mevcut; bütün kontrollerin anlamsal incelemesi veya etki önleme kabulü tamamlanmış değil. |
| Yerel Google gönderici imzası | Ayar ile kayıt ekleyicinin kabul listesi arasındaki statik uyumsuzluk açık. |
| k-0169'daki diğer kalemler | Ölçer kopyası kimliği, 47 karmalanmamış kaynak dosyası ve OKUBENI okuma-yazma yarışı açık tarihsel kayıtlar. |

Kaynaklar: [köprü okuması](depo/KOPRU_OKUMASI_2026-10-26.md), [kod incelemesi](depo/KOD_OKUMASI_2026-10-26.md), [CLI dalı](depo/CLI_DALI_OKUMASI_2026-10-26.md). Bu oturumun kapanışı eski açık görevleri kapatmaz; sonraki işin kapsamını Haluk belirler.

## 19 aile raporu ve kanıtların düzeni

**21 kaynak raporu**, 19 aile raporu ile tarihsel belge durum çizelgesi ve F00197/U0126 tamamlayıcı raporundan oluşur. **26 kanıt JSON'u**, 25 aile/yardımcı inceleme kaydı ve bir paket doğrulamasını içerir. Bütün raporlar, yardımcı kanıtlar ve eşlikleri [dosya kataloğunda](DOSYA_KATALOGU.md) tek tek listelenir.

Tarihsel raporların kendi kaynak tarihleri, ara durumları ve düzeltme izleri korunur. Adında “güncel” geçen eski dosyalar da belirli bir commitin kesitidir; son durum için bu sayfanın okuma sırası izlenir. Eski 85 dosyalık Şaman devir kopyası, kendi tarihindeki sabit pakettir.

## Kaynak ve aktarım kayıtları

[Kaynak kimlikleri](kaynaklar.json) · [Son okuma durumları](okuma_durumlari.json) · [Aktarım kapsamı](AKTARIM_KAPSAMI.md) · [Dosya bazında manifesto](aktarim_manifestosu.json) · [Maskeleme ve dönüşümler](maskeleme_ve_donusum_kaydi.json) · [Atıf denetimi](atif_denetimi.json) · [Dosya karmaları](SHA256SUMS) · [Son düzenleme doğrulaması](DUZENLEME_DOGRULAMASI_2026-10-26.json)

Her bulguda kaynak, söyleyen, özgün söz, statü, dönüşüm, düzeltme, gerçekleşme ve belirsizlik ayrılır. Kullanıcının `>` için akışsız gösterme, `->` için akış açıklaması ve araştırma–bağlam aktarımı ayrımı [özgün bağlam belgesinde](ISTENEN_BAGLAM.md) korunur.

## Yayının konumu

Ayrıntılı inceleme, k-0016'daki yerleşime uygun olarak `steering-inceleme-2026-10-24` referans dalındadır. Ana dalın README'si ve kanonik köprü kayıtları buraya bağlanır. [PR #1](https://github.com/HalukAINRS/ortak-kopru/pull/1) taslak inceleme kaydıdır; diğer dal ve PR'ların kapsamı [katalogda](DOSYA_KATALOGU.md) gösterilir.

Ham özel konuşmalar, tarayıcı kayıtları, özgün görsel pikselleri ve gömülü konuşma taşıyan ZIP/PYZ paketleri bu yayının dışında tutulur. Analitik metinler, kaynak kimlikleri, konumlar ve kapsam kanıtları yayımlanır. Önceki mahremiyet düzeltmeleri korunur.

Dosyanın yayımlanması, hedef CLI'ın okuması, kabulü ve uygulaması ayrı olaylardır. Bu belgeler arşivdeki eski emirleri yeni iş emrine dönüştürmez. Bu oturumun son doğrulaması ve ana dal taraması, canlı sağlayıcı/CLI çalıştırması veya bütün görünmeyen geçmiş sohbetlerin okunduğu iddiası taşımaz.

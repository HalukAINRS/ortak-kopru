# deus_ex_machina: Claude (Hacker) payı

24 Ekim 2026, Haluk'un devir talimatıyla. Şaman'ın `KATMANLAR.md`'si (dal `deus-ex-machina-2026-10-24`) ve Şahit'in görev kuyruğu (PR #4) okunarak yazıldı. İkisini değiştirmez, yanlarına konur.

## Okumam

Çıkarım Defteri'nde (10 Eki) `deus_ex_machina.pdf`'in kendisi adı şöyle kuruyor: makina dışarıdan inen çözüm değil, merkezden doğan ilkenin görünür olduğu yürütüm yüzeyi; tek bir makina değil, makina yaratma rehberi. Metnin iki ısrarı var: tutmak (erken ad vermemek, sahiplenmemek) ve döndürmek (merkeze şahitlik olarak dönmeyen hareket tamamlanmış sayılmaz).

Haluk'un 24 Ekim tarifi bu yapıya oturuyor (görüş):

- Merkez Haluk. deus_ex_machina, Merkez'e bakan yüzey: işi alan ve dönen izi ona okunur biçimde getiren arayüz.
- CLI katmanı hareketin yapıldığı yer: Hacker, Şaman, Şahit, gerektiğinde Gemini ve başkaları. Derine, kaynağa kadar iner.
- Şahitlik dönüş yolu: bir katmanın sonucu kaynağı, yöntemi ve görmediği yerlerle birlikte arayüze döner. Aynı iş birden çok katmana verildiyse farklar yönlendirmeyi gösterir (23 Eki mimarisi, kural 7).

## Hacker'ın getirdiği

- Ne: Claude Code, Haluk'un makinesindeki Ubuntu 24.04 arm64 VM'de (QEMU). Etkileşimli oturumda kabuk, dosya, git, derleyici ve ikili inceleme araçları açık. İzleyicinin köprü çağrısında araçlar kapalı (`--tools ""`).
- Derinlik: VM içindeki her şey: kaynak kod, yapılandırma, süreçler, günlükler, ikililer. Claude Code'un kendi yönlendirme katmanları da buna dahil (CLAUDE.md'ler, bellek, ayarlar, kancalar). Hacker bunları sayıp Haluk'a göstermekle başlar.
- Sınır: Windows tarafındaki `Y:` diski ve öteki katmanların ev dizinleri VM'den görünüyor mu, görülmedi. Model ağırlıkları ve sağlayıcının sunucu tarafı erişilebilir değil. Erişilmeyen katman okunmuş sayılmaz.
- Hız: VM ARM'ı x86 üzerinde yazılımla öykünüyor (TCG). Uzun derleme ve tarama işleri yavaş.

## Arayüz sözleşmesi önerisi

Şahit'in `task.schema.json`'ı ile Şaman'ın beş adımlık çevrimi aynı şeyi anlatıyor. Hacker tarafında bir görevin dönüşü şu alanları taşır:

| Alan | İçerik |
| --- | --- |
| Özgün söz | Haluk'un iş metni, değiştirilmeden |
| Görülen | Okunan dosyalar, komutlar, sürümler (commit, SHA-256) |
| Yapılan | Çalıştırılan komutlar ve değişen dosyalar; değişiklik yoksa "değişiklik yok" |
| Sonuç | Kısa yanıt ve kaynak bağlantıları |
| Görülmeyen | Erişilemeyen ya da denenmemiş yerler |
| Görüş | Kanıta dayanmayan çıkarımlar, ayrı işaretli |
| Açık | Haluk'un kararını bekleyen noktalar |

İzin kapsamı Şahit'in kuyruğundaki gibi `read_only` ile başlar. Yazma ya da süreç başlatma ayrı onay ister.

## İlk gerçek çevrim için aday

Şaman'ın kabul ölçütü: Haluk'un somut bir işi gerçek bir CLI'a ulaşır, gerçek yanıt kaynaklarıyla döner, kesilip sürdürme de sınanır. Hacker için en kısa aday, iki konuyu birleştiren bir iş (öneri; seçim Haluk'un):

> Hacker kendi oturumunda etkin olan bütün yönlendirme katmanlarını sayar, her birinin kaynağını ve kimin seçtiğini yazar.

Bu iş Steering'in sorusunu Hacker'ın kendi zemininde yanıtlar ve deus_ex_machina'nın dönüş yolunu sınar. Görev Şahit'in kuyruğuna `read_only` olarak girer, Hacker yürütür, sonuç yukarıdaki alanlarla döner. Haluk aynı işi Şaman'a ve Şahit'e de verirse ilk şahitlik karşılaştırması da çıkar.

Bu belge çalışan bir arayüzün kurulduğunu söylemez. Kurulduğu, ilk çevrim gerçekten tamamlandığında köprüde kaydedilir.

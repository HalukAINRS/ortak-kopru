# Ortak geçmiş arşivi

Bu klasör, Haluk'un yürüttüğü çalışmanın ortak geçmişini okuyup kayda geçirmek için açılan arşivdir. Çalışmaya Haluk ile üç yapay zekâ oturumu katıldı; her biri bir odakta çalıştı. ChatGPT (Şaman) anlam ve bağlama, Gemini (Şahit) kaynak ile iddia arasındaki ilişkiye, Claude (Hacker) kayıtların bütünlüğüne ve işlemlerin gerçekten yapılıp yapılmadığına baktı. Bu klasörde şimdilik yalnız Claude Code Bulut oturumunun dosyaları var. Öteki iki katılımcının kayıtları kendi ortamlarında tutuluyor; buraya aktarılmadı.

## Nereden başlamalı

İlk okuma için iki dosya yeterli:

- **Not defteri:** [`not-defteri/`](not-defteri/claude-code-bulut-2026-10-27.md), çalışmadan çıkarılan anlamları kısa paragraflar halinde anlatır. Her paragraf tek başına okunup aktarılabilir.
- **Son durum raporu:** [`son-durum/`](son-durum/claude-code-bulut-2026-10-27.md) neyin yapıldığını, neyin doğrulandığını ve neyin açık kaldığını özetler.

Öteki klasörler adım adım tutulmuş çalışma kayıtlarıdır; ayrıntı ve kanıt arayanlar içindir.

## Klasörlerin düzeni

Her adımın kendi klasörü var; her klasörde katılımcı başına bir dosya bulunur.

- [`envanter/`](envanter/claude-code-bulut-2026-10-27.md): 1. adım, daha önce tutulmuş envanterlerin karşılaştırılması.
- [`okuma-kumesi/`](okuma-kumesi/claude-code-bulut-2026-10-27.md): 2. adım, herkesin aynı baytları okuyabileceği küçük kaynak kümesi.
- [`olay-kartlari/`](olay-kartlari/claude-code-bulut-2026-10-27.md): 3. adım, olay kartları ve zaman çizgisi.
- [`kavram-dizini/`](kavram-dizini/claude-code-bulut-2026-10-27.md): 4. adım, kavramların depodaki ilk görünümleri ve düzeltme zinciri.
- [`karsi-okuma/`](karsi-okuma/claude-code-bulut-2026-10-27.md): 5. adım, ortak kaydın karşı okunması.
- [`geri-donus/`](geri-donus/claude-code-bulut-2026-10-27.md): 6. adım, okumanın Haluk'a geri dönüşü.

## Kayıtlar nasıl okunur

**İddianın türü:** Kayıtlarda her iddianın yanında türü yazılı. D, doğrudan okunan bir belge ya da yapılan bir ölçümdür. A, başka birinin aktardığı bilgidir. Ç ise çıkarımdır. [?] işareti açık kalan, bilinmeyen yeri gösterir.

**Zaman:** Bir olayın zamanı, kaydın kendi zaman alanı, kaydın depoya girdiği commit zamanı ve bir iletinin varış zamanı ayrı tutulur. Olay zamanı bilinmiyorsa "belirsiz" yazılır. Saatler UTC'dir.

**Kimlikler:** Kayıtlardaki kısaltmalar (K-C, OLAY-C, G-C gibi) yalnız adres işlevi görür.

## Düzeltmeler

Arşivde hiçbir satır sonradan değiştirilmez. Bir düzeltme, eski satırın yanına yeni bir bağ olarak eklenir; bu bağlar DB, E, DÜZ, KD ya da EK gibi kısaltmalar taşır. Böylece hem bugünkü anlayış hem de nasıl değiştiği okunabilir.

## Gizlilik sınırı

Bu depo herkese açıktır. Arşive şunlar alınmadı:

- katılımcıların iç çalışma izleri;
- kişisel dosyalar;
- bize özel olarak verilmiş protokol içerikleri.

Bu içerikler gerektiğinde yalnız nötr adlarla anılır. Depo dışındaki kaynakların bağlantıları da yazılmadı.

## Geri dönüş ve etkileşim

Haluk'un kendi geçmişinin temsiline ilişkin geri dönüşü, etkilediği satırın yanına eklenir; sessizlik kabul sayılmaz.

Dış okuyucular bir paragrafa ya da kayda ilişkin soru, itiraz ve düzeltmelerini bu depoda bir konu (issue) açarak iletebilir. Konuya ilgili paragrafın ya da kaydın kimliğini yazın, kişisel bilgi paylaşmayın. Dış okuyuculardan gelen karşılıklar, Haluk'un geri dönüşünden ayrı kaydedilir. Ortak defter (`kopru.html`) dış kullanıcılarca yazılmaz.

## Bu arşiv ne değildir

Bu arşiv tamamlanmış bir tarih değildir; seçilmiş kaynaklar üzerinde yapılmış ortak bir okumadır. Katılımcıların uyuşması, kullanıcı kabulü ya da kurulum onayı sayılmaz. Arşivin yeri, görünürlüğü ve ana dala birleştirilmesi Haluk'un kararıdır.

## Ana daldaki okuma yolu

Bu bölüm sonradan eklendi. 28 Ekim'de ana dala, Şaman'ın hazırladığı bir okuma katmanı girdi: [anlam defteri](../docs/ANLAM_NOT_DEFTERI.md), [son durum](../docs/SON_DURUM.md), [kaynaklar](../docs/KAYNAKLAR.md) ve [depo rehberi](../docs/DEPO_REHBERI.md). Aynı metinlerin web sayfalarına deponun ana README'sindeki web girişinden ulaşılır. O metinleri Şaman hazırladı; Claude ve Gemini katkılarını sahipleriyle anıyor. Bu klasördeki dosyalar ise Claude Code Bulut oturumunun kendi kayıtlarıdır. İki yerde aynı konu farklı biçimde anlatılıyorsa, her metnin kimin okuması olduğuna bakın.

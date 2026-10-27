# Tek nokta — canlı kanıt kaydı

**27 Ekim 2026, 16:33:47–16:33:51 UTC:** tek DEUS işinde katkılar, canlı GitHub alımı, gerçek yerel CLI makbuzları ve yedekten dönüş birlikte doğrulandı. Bu rapor teknik gerçekleşmeyi kaydeder; işin kullanıcı veya üç katılımcı tarafından kabul edildiğini bildirmez.

| Bağ | Gözlenen değer |
| --- | --- |
| Çalıştırılan kodun HEAD'i | [`6518f6fe1bbd9ce2f22cb1b39305676617bd330a`](https://github.com/HalukAINRS/ortak-kopru/commit/6518f6fe1bbd9ce2f22cb1b39305676617bd330a) |
| Ortak iş kimliği | `a7c101fcf79d4352b168856d1f71a3bc` |
| İstek revizyonu | `1` |
| Son kayıtlar | **4 katkı, 3 işlem, 11 olay, 8 kaynak görüntüsü** |
| Çalışma kipi | Açıkça seçilmiş `portable`; `kernel_verified=false` |
| İşin durumu | `ready`; `task_completion_verified=false` |

Canlı makbuzda tutulan `cli.py`, `server.py`, `core.py`, `collaboration.py` ve `operations.py` dosyalarının SHA-256 değerleri, yukarıdaki commit'in beş dosyasıyla da eşleşti. Son yerel test koşusundaki ek test doğrulamaları ile çalıştırılan uygulama kodunun sürümü ayrı değerlendirildi.

## Aynı işte 16 / 32 / 64 / 128

| Ortak süreç | Bu çevrimdeki somut kayıt |
| --- | --- |
| **16 — Gereksinim belirleme** | ChatGPT (Şaman), Claude (Hacker) ve Gemini (Şahit) için üç tasarım katkısı özeti; yazar, kaynak oturum ve aktaran ayrı alanlarda. |
| **32 — Gereç oluşturma** | Aşağıdaki kesin sürümden seçilmiş `README.md` baytları ve alım makbuzu. |
| **64 — Uygulama** | `repo_revision` ve `python_version` işlemlerinin gerçek stdout, stderr ve çıkış kodları. |
| **128 — Geri dönüş** | Teknik sonuçlara dayanan ChatGPT (Şaman) geri dönüşü; katkı kimliği `06d7a8a2e17f4655bdc33724eebe72d1`. |

Her katılımcının kendine özgü **[33×8] içsel döngüsü kendi oturumunda** kalır. Bu ortak süreçler, iç işleyişin ölçüldüğü veya bütün katılımcıların aynı kabul kararını verdiği anlamına gelmez.

### Katkıların kökeni

**ChatGPT (Şaman)** bütünleştirme, değişmez kaynak görüntüsü ve aynı istek anahtarının tekrarında kayıt korunumu üzerinde çalıştı; üç görüşmenin kısa özetlerini ve son geri dönüşü ortak işe aktardı. Özetler doğrudan alıntı olarak sunulmadı.

**Claude (Hacker)** mevcut gerçek Claude görüşmesinde eklemeli katkı, sınırlı işlem çalıştırıcısı ve `prepared` / `finish` ayrımına katkı verdi. Çalıştırıcı kodu [ilk uygulama](https://github.com/HalukAINRS/ortak-kopru/commit/a2fca85cf8aef4955bfa2872f2471c246431c3e0), [eksik çıktı düzeltmesi](https://github.com/HalukAINRS/ortak-kopru/commit/b6b239d7d033099c09729197c03c49898c3c502d) ve [depo filtresi koruması](https://github.com/HalukAINRS/ortak-kopru/commit/6518f6fe1bbd9ce2f22cb1b39305676617bd330a) olarak depoya alındı. Ortak görevdeki konuşma özeti ChatGPT tarafından aktarıldı; kodun gerçekleşmesi ayrıca commit ve işlem makbuzlarıyla izlendi.

**Gemini (Şahit)** açık revizyon bağı ve beş ölçüt sağladı: aynı iş kimliğine silmeden katkı; `author` / `relayed_by` ayrımı; kesin kaynak commit'i; gerçek stdout/stderr/exit code'un aynı işte tutulması; mevcut oturum korunumu ile teknik kanıt/kabul ayrımı. Son incelemede revizyon–snapshot bağı ve hazırlanmış/belirsiz işlemin tekrarlanmaması öne çıktı. Bu katkı da ChatGPT tarafından aktarıldı; **Gemini'nin bağımsız CLI yürütümü bu kanıtta yoktur**.

Katkı etiketleri bağımsız kimlik doğrulaması değildir: `identity_verified=false`. Çevrim yeni sağlayıcı oturumu başlatmadı; mevcut sağlayıcı oturumlarının canlılığını yeniden doğruladığı iddiası taşımıyor.

## Canlı, kesin sürüme bağlı kaynak

GitHub'dan anonim ve salt okunur alım yapıldı. Seçilen dosyanın içeriği çalıştırılmadı.

| Alan | Değer |
| --- | --- |
| Kaynak | [`HalukAINRS/ortak-kopru / README.md`](https://github.com/HalukAINRS/ortak-kopru/blob/ab3b703de6f1a1f86bec2805effdc5d044cd1a3c/README.md) |
| Kaynak commit'i | `ab3b703de6f1a1f86bec2805effdc5d044cd1a3c` |
| Git blob kimliği | `ef87e795fd552569d8ac69bcfae31ed3cd4da11a` |
| Boyut | **23.778 bayt** |
| SHA-256 | `f95a9feb958ee9ab8e5b05fc3dec5a21a87e8a815ddd15b3c1633898742e0448` |
| İşlem kimliği | `e3bbd1243e7b4ad8bfead1ff8039336d` |
| Durum | `completed`; `content_executed=false` |

Bu uzak kaynak commit'i, yerel uygulamanın `6518f6…` HEAD'inden ayrıdır. Alınan dosyanın baytları aynı işin kaynak görüntüsünde ve geri yüklenen kopyada aynı SHA-256 ile bulundu.

## Gerçek yerel CLI makbuzları

İki işlem **bu geliştirme ortamında** çalıştı. Her ikisi `completed`, çıkış kodları `0`; stderr çıktıları boştu.

| İşlem | Gerçek stdout özeti | Stdout baytı | İşlem kimliği |
| --- | --- | ---: | --- |
| `repo_revision` | `6518f6fe1bbd9ce2f22cb1b39305676617bd330a` | 41 | `1a0db8afb2674aadbcccf86e98036f92` |
| `python_version` | `Python 3.12.14` | 15 | `d7048342a64447a0885991c5d787d84a` |

Bayt sayıları sondaki satır sonunu da içerir. Yakalanan çıktılar kesilmemiştir. Stdout SHA-256 değerleri:

- `repo_revision`: `70b21a191b2bc88369094f775bae152de2178bba1d22923163ea12bd46801ec4`
- `python_version`: `4c3569f5da09975434dd9fd9a91fadbc4367a91d8f3c3fab59e9241ab9ee4bd8`
- Her iki boş stderr: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

### Aynı istek anahtarının tekrarı

Her tamamlanmış işlem aynı anahtarla yeniden istendi. İşlem kimliği ve makbuz aynı kaldı; yeni olay oluşmadı:

| Tekrarlanan işlem | Önceki olay sayısı | Sonraki olay sayısı |
| --- | ---: | ---: |
| Kesin sürümden GitHub alımı | 6 | 6 |
| `repo_revision` | 8 | 8 |
| `python_version` | 10 | 10 |

Sonraki 128 geri dönüşü, ayrı katkı olarak on birinci olayı oluşturdu. Canlı çevrim tamamlanmış işlemlerin tekrarını denetledi; `prepared` / `unknown` kesintisi ve yeni anahtarla devam davranışı aşağıdaki regresyon testlerinde ayrıca sınandı.

## Yedek ve geri dönüş

`backup → backup-verify → restore` çevrimi doğrulandı. Geri alınan görev, ortak görünüm, olaylar ve kaynak baytları özgün kayıtlarla birebir eşleşti.

| Yedek içeriği | Sayı |
| --- | ---: |
| Görev | 1 |
| Olay | 11 |
| Nesne / kaynak görüntüsü | 8 |
| Resmî sonuç kaydı | 0 |

Sekiz kaynak görüntüsü **4 katkı, 3 işlem makbuzu ve 1 alınmış dosyadan** oluşuyor. Bütünlük değerleri:

- Veritabanı SHA-256: `0085213b6a0d882bbd1fa0893ec786aeaac4dfeb6f63d2fddc2ddea26b7d6f26`
- Yedek manifesti SHA-256: `53de05a8bcd34e3aca6da635d7f6f614588f10a002374d2a5b826250e30dee2d`

Bu karmalar bayt bütünlüğünü bağlar; kişi kimliği veya kabul kararı doğrulamaz. Özel oturum bağlantıları, erişim bilgileri, yerel veri yolları ve ham günlükler bu rapora alınmadı.

## Test kanıtı ve açık kapsam

**Son yerel suite:** 270 test; **264 geçti, 6 atlandı**. Altı atlama bu ortamdaki PowerShell 7 eksikliğine aittir. Yeni ortak CLI/HTTP girişlerinin 11 testi geçti; mevcut görev rotaları, token/origin sınırları ve NT hazır değilken yeni işlemi reddetme davranışı da sınandı. [Ortak arayüz testleri](../tests/test_deus_joint_interface.py) · [Ortak hizmet testleri](../tests/test_deus_collaboration.py).

Regresyonlar; revizyon değişince önceki makbuzun korunmasını, snapshot yazımı başarısızsa sahte tamamlanma oluşmamasını, `unknown` işlemin aynı anahtarla yeniden yürütülmemesini ve yeni denemenin eski belirsiz kaydı silmemesini kapsıyor. Yerel `repo_status` filtre koruması ve eksik çıktı yakalamasının başarı sayılmaması da ayrı testlerle doğrulandı. [İşlem testleri](../tests/test_deus_operations.py).

**GitHub CI:** [`6518f6fe1bbd9ce2f22cb1b39305676617bd330a` için 40541992474 numaralı koşu](https://github.com/HalukAINRS/ortak-kopru/actions/runs/40541992474) `success`; `ubuntu-latest` ve `windows-latest` işleri `completed/success`. Test, depo denetimi, JavaScript sözdizimi ve Windows PowerShell sözdizimi adımları geçti. Bu kayıt, belirtilen kod sürümünün CI sonucudur; daha sonraki belge/test commit'lerinin CI sonucunu peşinen bildirmez.

**Henüz doğrulanmayan kapsam:** kullanıcının Windows bilgisayarındaki gerçek başlangıç (`target_windows_verified=false`), NT bağlantısı (`kernel_verified=false`) ve canlı tarayıcıyla görsel UI doğrulaması. Tarayıcı otomasyon yüzeyi ile yerel sunucu ayrı loopback alanlarında olduğundan görsel UI turu yapılmadı; geçen yerel HTTP testleri bununla karıştırılmadı. İş `ready` kaldı; kullanıcı kabulü veya üçlü ortak kabul kaydı üretilmedi.

Kullanım: [Tek nokta rehberi](TEK_NOKTA.md).

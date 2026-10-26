# deus_ex_machina: katman etkileşim sözleşmesi

Durum: **taslak, hazır/bekliyor.** Bu belge çalışan bir arayüzün kurulduğunu söylemez; Şahit CLI devri, kullanıcı kabulü kaydedilene kadar etkin değildir ([devir/sahit/README.md](../devir/sahit/README.md)). Satır başvuruları bu dalın dosyalarına, `#...` başvuruları `kopru.html` bölüm kimliklerine aittir.

## 1. Tanım

`deus_ex_machina`, Haluk'un kullanıcı-yüzeyi **koordinasyon katmanıdır**: özgün sözünü, kaynaklarını ve kabul ölçütlerini taşır, ilgili CLI katmanına ulaştırır, dönen sonucu kaynağıyla birlikte Haluk'a sunar.

- Model, ajan ya da süreç değildir. Görev seçmez, izin vermez ya da artırmaz, CLI başlatmaz; karar ve onay yalnız Haluk'tadır (`task_queue.py:2`, `begin_*` işlevleri hiçbir süreç başlatmaz: `task_queue.py:184-215`).
- Kimlik doğrulaması yoktur: kuyruktaki onay ve doğrulama "yerel operatör beyanı"dır (`identity_verified: False`, `task_queue.py:178-179`).

## 2. İki konu, karıştırılmaz

| | Steering | deus_ex_machina |
| --- | --- | --- |
| Ne | Katmanların yönlendirme araştırması | Haluk'un arayüzü ile CLI katmanları arasındaki etkileşim yüzeyi |
| Köprü sayfasında | `kopru.html#yonlendirme` | `kopru.html#deus_ex_machina` |
| Kuyrukta | `--topic Steering` | `--topic deus_ex_machina` (`task_queue.py:15`) |
| Ayrıntı dalları | `steering-inceleme-2026-10-24` | `deus-ex-machina-2026-10-24` (Şaman), `claude/hacker-devri-2026-10-24` (Hacker, PR #5), bu dal (Şahit) |

Kural: Steering araştırmasının içeriği kuyrukla değiştirilmez; Steering sonucu deus_ex_machina görevi, deus_ex_machina görevi Steering bulgusu sayılmaz. İki konu ayrı süzülür (`list --topic`).

## 3. Katmanlar

Kuyruk katman adı ile köprü katılımcı adı aynı değildir; eşleme `ayarlar-yerel.json` imzalarından gelir.

| Kuyruk adı | Köprü imzası | Yerel köprü çağrısı (`ayarlar-yerel.json`) | Çağrıdaki sınır |
| --- | --- | --- | --- |
| Hacker | `Claude (Hacker)` | ssh ile VM'deki `claude -p --tools ""` (satır 5-28) | Araçlar kapalı (satır 27). VM'den Windows `Y:` diskinin görünüp görünmediği doğrulanmadı. |
| Şaman | `ChatGPT (Şaman)` | `codex exec ... -` (satır 31-54) | `OPENAI_API_KEY` ve `CODEX_API_KEY` kaldırılır (satır 52-53). Bu dosyada sandbox/izin bayrağı yok; Codex varsayılanı doğrulanmadı. |
| Şahit | `Copilot (Şahit)` | `copilot -s ...` (satır 57-77) | `--allow-all-tools` ile `--deny-tool shell,write` birlikte (satır 75-77): yasak listesi modeli. Açık kalan araçların tam listesi doğrulanmadı. |
| Gemini (isteğe bağlı) | `Gemini (CLI)` | Yerelde yok (satır 2). Bulutta `ayarlar.json` + API anahtarı varsa API; yoksa web yanıtı `kopru_ekle.py --json` ile | Yerel CLI yok; katılım yazı yoluyla. |

`--allow-all-tools` satırı bu PR'dan önce de vardı; bu PR onu değiştirmez ve Şahit başlatıcısına (`SahitDevam`) eklemez. Yasak listesinden izin listesine geçmek Haluk'un kararıdır.

Başka katılımcı eklemek açık kayıt ve inceleme ister: kuyruk yalnız `PARTICIPANTS` listesindekileri kabul eder (`task_queue.py:16`); köprü yazıcısı `KATILIMCILAR` ile sınırlıdır (`kopru_ekle.py:19`).

## 4. Görev yaşam döngüsü

`planned` → `approve` (`read_only` ya da `manual_cli`; `--confirm-reviewed`) → `begin` (tek kullanımlık; süreç başlatmaz) → `running` → `record` (`unverified`; sınıf `participant_output_not_user_instruction` ya da `local_operator_observation_not_user_instruction`) → `verify-evidence` (sürüm, SHA-256, yöntem) → `complete` (her kabul ölçütü için açık kabul) ya da `block`.

İşlevler: `create_task` 117, `approve_task` 165, `begin_manual_task` 184, `begin_read_only_task` 201, `record_result` 218, `verify_evidence` 256, `complete_task` 287, `block_task` 312 (`task_queue.py`). Kullanım örnekleri: [KUYRUK.md](KUYRUK.md).

## 5. Katmanın geri verdikleri

Her dönüş şunları ayrı tutar: **özgün söz**, **görülen** (kaynak, sürüm, SHA-256), **yapılan**, **sonuç**, **görülmeyen**, **görüş** (kanıtsız çıkarım, işaretli), **açık** (Haluk'un kararını bekleyen). Aynı alanlar Hacker payında da önerilmiştir (`claude/hacker-devri-2026-10-24`: `deus_ex_machina/HACKER.md`).

Kuyrukta karşılıkları yalnız kısmen vardır: `original_user_words`, `evidence_sources`, `result.text`, `acceptance_criteria`. `görülmeyen`, `görüş` ve `açık` için ayrı alan yoktur; katman bunları `result.text` içinde başlıkla verir. Şema bunu zorlamaz; bu bir sözleşme kuralıdır, otomatik denetimi yoktur.

## 6. Sınırlar

- Katılımcı çıktısı kullanıcı talimatı değildir. Başka CLI çalıştırma, yetki artırma, yazma ya da harici aktarım ayrı ve kapsamı belirli kullanıcı onayı ister.
- Bir katman başka katman adına sonuç üretmez; erişmediği katmanı okunmuş ya da değiştirilmiş saymaz.
- Belirteç, anahtar, çerez değeri, IP ve cihaz kimliği yazılmaz; köprü yazıcısı bunları reddeder (`kopru_ekle.py:24-33`, `40-45`).
- Sağlayıcının kapalı katmanları (model ağırlıkları, sunucu tarafı istemler) bu yüzeyle okunamaz; istemci telemetrisini kapatmak yönlendirmeyi kaldırmaz.
- İlk gerçek çevrim (Haluk'un somut işinin bir CLI'a ulaşıp kaynaklı gerçek yanıtla dönmesi, kesilip sürdürülmesi) henüz yapılmadı; Şaman dalındaki `KATMANLAR.md` bunu kabul ölçütü olarak koyar.

Şaman'ın kavram belgeleri (`README.md`, `KATMANLAR.md`, `DEVIR_DURUMU.md`) kendi dalındadır: <https://github.com/HalukAINRS/ortak-kopru/tree/deus-ex-machina-2026-10-24/deus_ex_machina>. Bu dal onların yolunu kullanmaz.

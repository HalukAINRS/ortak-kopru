# Rafine çalışmaları

Bu dizin, deponun belirli bir kesitinde yapılan gözden geçirme ve iyileştirme turlarının süreç kayıtlarını taşır. Her tur üç parçayla kaydedilir: kullanıcıya dönük anlam defteri ([rafine defteri](rafine-defteri.md)), buradaki tarihli süreç arşivi ve aynı turun makinece okunur bulgu kaydı (`*.json`, [sözleşmesi](../../../schemas/rafine-bulgu.schema.json)).

Süreç arşivi, o turda neyin nasıl incelendiğini, hangi komutların hangi sonucu verdiğini, hangi varsayımın kanıtla geri çekildiğini ve neyin kapsam dışı bırakıldığını kendi zamanıyla anlatır. Bulgu kaydı aynı turun kontrol ve bulgularını alanlara ayırır; `python tools/sema_denetle.py --sema rafine-bulgu --veri docs/gecmis/rafine/<dosya>.json` ile sözleşmeye karşı doğrulanabilir. Bir turun kayıtları o turun kesitine aittir; sonraki sürümler için geçerliliği yeniden gözlenir.

| Tur | Gözlemci | Kesit | Kayıtlar |
| --- | --- | --- | --- |
| 28 Ekim 2026 | Claude Code Bulut (Hacker odağı) | `main` @ `97c908de7a5850978082770ba3bac3e508688e57` | [Süreç](claude-code-bulut-2026-10-28-surec.md) · [Bulgular (JSON)](claude-code-bulut-2026-10-28-bulgular.json) · [Anlam defteri](rafine-defteri.md) · [Dokuz koordinatla tanım](../depo-tanimi.md) · [Tanım (JSON)](../depo-tanimi.json) · [Şimdi ve sonrası](../simdi-ve-sonrasi.md) · [Senaryolar (JSON)](../simdi-ve-sonrasi.json) · [Açılış](../../acilis.md) · [Açılış (JSON)](../../acilis.json) |
| 28 Ekim 2026 akşamı · belge okuması | Claude Code Bulut (Hacker odağı) | `main` @ `dcae3deda4f0f796e77358331e3ae286cf668082` | [Okuma](okuma-2026-10-28.md) · [Bulgular (JSON)](claude-code-bulut-2026-10-28-okuma.json) · [Süreç](claude-code-bulut-2026-10-28-surec.md) |
| 28 Ekim 2026 boyunca · talimatlar ve yanıtlar | Claude Code Bulut (Hacker odağı) | her talimatın kendi saati | [Yanıtlar](claude-code-bulut-2026-10-28-yanitlar.md) · [Süreç](claude-code-bulut-2026-10-28-surec.md) |

Bir turun kaydını okuyan yeni katılımcı, o turdaki açık işleri kendiliğinden üstlenmiş olmaz; iş kullanıcıdan gelir. Düzeltme veya itiraz için ilgili bulgunun kimliğini (`R-01` gibi) belirterek [karşılık formu](https://github.com/HalukAINRS/ortak-kopru/issues/new?template=karsilik.yml) kullanılabilir.

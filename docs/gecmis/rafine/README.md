# Rafine çalışmaları

Bu dizin, deponun belirli bir kesitinde yapılan gözden geçirme ve iyileştirme turlarının süreç kayıtlarını taşır. Her tur üç parçayla kaydedilir: kullanıcıya dönük anlam defteri ([RAFINE_DEFTERI.md](rafine-defteri.md)), buradaki tarihli süreç arşivi ve aynı turun makinece okunur bulgu kaydı (`*.json`, [sözleşmesi](../../../schemas/rafine-bulgu.schema.json)).

Süreç arşivi, o turda neyin nasıl incelendiğini, hangi komutların hangi sonucu verdiğini, hangi varsayımın kanıtla geri çekildiğini ve neyin kapsam dışı bırakıldığını kendi zamanıyla anlatır. Bulgu kaydı aynı turun kontrol ve bulgularını alanlara ayırır; `python tools/sema_denetle.py --sema rafine-bulgu --veri docs/rafine/<dosya>.json` ile sözleşmeye karşı doğrulanabilir. Bir turun kayıtları o turun kesitine aittir; sonraki sürümler için geçerliliği yeniden gözlenir.

| Tur | Gözlemci | Kesit | Kayıtlar |
| --- | --- | --- | --- |
| 28 Ekim 2026 | Claude Code Bulut (Hacker odağı) | `main` @ `97c908de7a5850978082770ba3bac3e508688e57` | [Süreç](claude-code-bulut-2026-10-28-surec.md) · [Bulgular (JSON)](claude-code-bulut-2026-10-28-bulgular.json) · [Anlam defteri](rafine-defteri.md) · [Dokuz koordinatla tanım](../depo-tanimi.md) · [Tanım (JSON)](../depo-tanimi.json) · [Şimdi ve sonrası](../simdi-ve-sonrasi.md) · [Senaryolar (JSON)](../simdi-ve-sonrasi.json) · [Açılış](../../acilis.md) · [Açılış (JSON)](../../acilis.json) |

Bir turun kaydını okuyan yeni katılımcı, o turdaki açık işleri kendiliğinden üstlenmiş olmaz; iş kullanıcıdan gelir. Düzeltme veya itiraz için ilgili bulgunun kimliğini (`R-01` gibi) belirterek [GitHub Issues](https://github.com/HalukAINRS/ortak-kopru/issues) kullanılabilir.

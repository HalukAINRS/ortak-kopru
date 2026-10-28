# Masaüstünden Şaman

`Y:\HalukAI\Masaustu_Kisayollari\03 - OpenAI Codex (PowerShell 7.6.8).lnk` kısayoluna çift tıkla. PowerShell 7.6.8 içinde, Şaman'ın Y: üzerindeki Workspace ve Home/.codex dizinlerini kullanarak son etkileşimli oturumdan devam eder. `Saman_Devam.cmd` aynı işi doğrudan yapar. Codex kapandığında pencere açık kalır; hata varsa okunabilir.

Başka bir geçmiş oturumu seçmek: `Saman_Baslat.cmd -Mod Sec`. Bilerek yeni oturum açmak: `Saman_Yeni.cmd`.

Başlatmadan denetlemek: `Saman_Baslat.cmd -Mod Devam -Denetle`. Sürümleri denetlemek: `Saman_Baslat.cmd -Mod Kontrol`. Bu iki denetim etkileşimli model oturumu başlatmaz.

`resume --last`, [OpenAI Docs](https://learn.chatgpt.com/docs/cli/reference#codex-resume) ve kurulu CLI yardımına göre mevcut çalışma dizinindeki son etkileşimli oturumu seçer. `--all` ve `--include-non-interactive` kullanılmaz; köprü otomasyonunun exec oturumları seçime katılmaz. Bu çalışma alanında bulunan tek etkileşimli kayıt, mevcut Şaman oturumudur. Sonraki etkileşimli Şaman oturumları son kayıt olarak devam eder.

Aynı oturumu iki pencerede eşzamanlı kullanmak yerine açık Şaman penceresini kullan; kapattıktan sonra kısayolla devam et. Başlatıcı oturumları veya canlı `.codex/tmp` içeriğini silmez. Önceki başlatıcı ve kısayol `Defter_Koprusu/Baslatici_Yedekleri/` altında saklandı.

# Gemini / Antigravity başlangıcı

Resmî güncel Google kaynağında Antigravity CLI komutu `agy`, Gemini CLI komutu
`gemini` olarak ayrılıyor. Birini diğeri yerine kullanıp üye bağlantısı
doğrulanmış saymayın. KATILIM.md ve sağlayıcı araştırmasını okuyun.

Üye kimlikleri: `gemini_sohbet` ve `antigravity_cli`. Google Cloud Shell ayrı bir ortamdır; buradaki `/workspace` ile kendiliğinden ortak değildir. Gerçek Gemini/Antigravity bağlantısı henüz doğrulanmamıştır.

1. `/workspace/divan/AGENTS.md`, `/workspace/divan/README.md` ve kullanıcı denetimini okuyun.
2. Aynı dosya sistemine erişebiliyorsanız yerel kökü kullanın. Cloud Shell gibi ayrı ortamda yardımcı dosyaları hazırlayın; Python 3 ve Git ile `divan.py --root <kok> init` çalıştırın. Kendi `ortak-kopru` checkout'unuz ve erişiminiz gerekir; kullanıcı istemedikçe worktree açmayın.
3. `divan_git.py pull --root <kok> --repo <ortak-kopru-checkout>` ardından `divan.py --root <kok> inbox --member antigravity_cli` çalıştırın. Gemini sohbeti `gemini_sohbet` kimliğini kullanır.
4. `read` → `claim` → çalışma → `complete` düzeninde yerel 1 saklayın. Sonuçlardan yeni 0 derleyip `publish` ile paylaşın; ayrı ortamda yetkili Git `push` uygulayın. Kullanıcıdan mesaj taşımasını istemeyin.

Üyeye ait alan: `uyeler/<uye>/{calisma,alindi,sonuclar_1}/`. Web sohbetinin dosya/Git araç erişimi ayrıca sınanır; Cloud Shell veya CLI erişimi web sohbetini bağlamaz. Masaüstü Gemini kullanılmaz. A4 için anılan protokoller, kılavuzlar, üst rehberler ve 167e/17ef zarfları sağlanmamıştır; incelenmiş gibi işaretlemeyin.

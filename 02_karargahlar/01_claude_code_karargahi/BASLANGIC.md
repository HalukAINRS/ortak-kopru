# Claude / Claude Code başlangıcı

Üye kimlikleri: `claude_sohbet` ve `claude_code_cli`. Bu dizinlerin oluşturulması Claude oturumu veya kimlik doğrulaması kurmaz; gerçek bağlantı henüz doğrulanmamıştır.

1. `/workspace/divan/AGENTS.md`, `/workspace/divan/README.md` ve kullanıcı denetimini okuyun.
2. Bu dosya sistemine gerçek erişiminiz varsa yerel kökü kullanın. Ayrı ortama geçtiyseniz yardımcı dosyaları ve kendi Divan kökünüzü hazırlayıp `divan.py --root <kok> init` çalıştırın. Python 3, Git ve `ortak-kopru` erişimi gerekir.
3. Kendi ortamınızda `divan_git.py pull --root <kok> --repo <ortak-kopru-checkout>` çalıştırın. Mevcut checkout'u kullanın; kullanıcı istemedikçe worktree oluşturmayın.
4. `divan.py --root <kok> inbox --member claude_code_cli` ile girdileri bulun; Claude sohbeti `claude_sohbet` kimliğini kullanır. `read` → `claim` → çalışma → `complete` ile kendi yerel 1 sonucunuzu saklayın.
5. Sonuçtan yeni bir çalışma girdisi derleyip `publish` uygulayın. Ayrı ortamda yetkili Git `push` ile paylaşın. Kullanıcıyı mesaj kuryesi yapmayın.

Üyeye ait alan: `uyeler/<uye>/{calisma,alindi,sonuclar_1}/`. Web sohbetinin gerçek dosya/Git araç erişimi gerekir; yalnızca Claude Code CLI veya API erişimi web sohbetini bağlamaz. Masaüstü Claude kullanılmaz. Başka sağlayıcı alt ajanları Claude üyeleri gibi gösterilmez.

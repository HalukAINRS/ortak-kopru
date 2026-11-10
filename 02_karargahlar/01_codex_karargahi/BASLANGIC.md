# ChatGPT / Codex başlangıcı

Üye kimlikleri: `chatgpt_sohbet` ve `codex_cli`. Yalnızca gerçekten içinde çalıştığınız oturumun kimliğini kullanın. Aynı dosya sistemindeki iki üye bu karargahı paylaşır; ayrı makinelerde Git aktarımı kullanılır.

1. `/workspace/divan/AGENTS.md`, `/workspace/divan/README.md` ve kullanıcı denetimini okuyun.
2. `python3 /workspace/divan/bin/divan.py init` ardından `doctor` çalıştırın. Mevcut checkout'u kullanın; kendiliğinden worktree açmayın.
3. Ayrı ortamdaysanız `python3 /workspace/divan/bin/divan_git.py pull --repo /workspace/ortak-kopru` çalıştırın. Gerçek root/repo farklıysa `--root` ve `--repo` verin.
4. `python3 /workspace/divan/bin/divan.py inbox --member codex_cli` ile başlayın; ChatGPT sohbeti kendi kimliğini kullanır. `read`, `claim`, çalışma ve `complete` ile yerel 1 üretin.
5. Yeni işi başlatacak bir yeni 0 yayımlayın. Ayrı ortamdaysanız yetkili Git `push` ile paylaşın. Kullanıcıdan mesaj taşımasını istemeyin.

Üyeye ait alan: `uyeler/<uye>/{calisma,alindi,sonuclar_1}/`. Tamamlanan sonuç ortak panoya kopyalanmaz. ChatGPT sohbeti ancak gerçek dosya/Git araç erişimi varsa doğrudan katılır; Codex erişimi ChatGPT web erişimini kanıtlamaz. Masaüstü sohbet uygulaması kullanılmaz.

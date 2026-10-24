# Hacker devri

24 Ekim 2026: Haluk'un talimatıyla claude.ai'deki Claude oturumu işi Claude Code'a (Hacker katmanı, Ubuntu VM) devretti.

- [`CLAUDE.md`](CLAUDE.md): Hacker'ın çalışma talimatı (kim, katman düzeni, daimi kurallar, ilk açılış, köprü mekaniği).
- [`DEVIR.md`](DEVIR.md): geçmiş, köprünün durumu, açık işler, taşınmayanlar.
- [`../../deus_ex_machina/HACKER.md`](../../deus_ex_machina/HACKER.md): ikinci konu başlığında Claude (Hacker) payı.

Herkese açık olmayan kısım (defter, kaynak PDF, tarayıcı kaydı çözümlemeleri, oturum iletileri) bu depoda yok. Haluk'a ayrı zip olarak verildi: `hacker-devri-2026-10-24.zip`.

## VM'de başlatma

Windows'ta, zip'in bulunduğu klasörde (yollar `ayarlar-yerel.json` ile aynı):

```bat
set K=Y:\HalukAI\02_Govde\Canli\CLI_Katmanlari
"%K%\Runtime\Git-Portable-2.56.0.2\usr\bin\scp.exe" -P 2222 -i "%K%\01_Claude_Code_Hacker\Home\.ssh\hacker_arm64_035" -o UserKnownHostsFile="%K%\01_Claude_Code_Hacker\Home\.ssh\known_hosts" -o StrictHostKeyChecking=yes hacker-devri-2026-10-24.zip hacker@127.0.0.1:~/
"%K%\Runtime\Git-Portable-2.56.0.2\usr\bin\ssh.exe" -p 2222 -i "%K%\01_Claude_Code_Hacker\Home\.ssh\hacker_arm64_035" -o UserKnownHostsFile="%K%\01_Claude_Code_Hacker\Home\.ssh\known_hosts" -o StrictHostKeyChecking=yes -t hacker@127.0.0.1
```

VM içinde:

```sh
python3 -m zipfile -e ~/hacker-devri-2026-10-24.zip ~/      # ~/hacker-devri/ oluşur
git clone https://github.com/HalukAINRS/ortak-kopru ~/ortak-kopru
git -C ~/ortak-kopru checkout claude/hacker-devri-2026-10-24  # ana dala birleşene kadar
cd ~/hacker-devri && /home/hacker/bin/claude-arm64-035
```

Claude Code `~/hacker-devri/CLAUDE.md`'yi okur ve "İlk açılışta" adımlarıyla başlar. Paketi `~` köküne değil, `~/hacker-devri/` altına açın. İzleyici Hacker'ı `~` dizininde çağırıyor; talimat dosyası orada durmazsa izleyici çağrılarına karışmaz.

VM'den GitHub'a gönderim için VM'de ayrıca kimlik gerekir (örn. `gh auth login`). Bu adım Haluk'un kararı; o zamana kadar köprüye yazım Windows tarafındaki `Kopru_Izle.cmd Ekle` ve `Gonder` ile sürer.

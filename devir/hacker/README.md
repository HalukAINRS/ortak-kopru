# Hacker devri

24 Ekim 2026: Haluk'un talimatıyla claude.ai'deki Claude oturumu işi Claude Code'a (Hacker katmanı, Ubuntu VM) devretti.

- [`CLAUDE.md`](CLAUDE.md): Hacker'ın çalışma talimatı (kim, katman düzeni, daimi kurallar, ilk açılış, köprü mekaniği).
- [`DEVIR.md`](DEVIR.md): geçmiş, köprünün durumu, açık işler, taşınmayanlar.
- [`../../deus_ex_machina/HACKER.md`](../../deus_ex_machina/HACKER.md): ikinci konu başlığında Claude (Hacker) payı.

Herkese açık olmayan kısım (defter, kaynak PDF, tarayıcı kaydı çözümlemeleri, oturum iletileri) bu depoda yok. Haluk'a ayrı zip olarak verildi: `hacker-devri-2026-10-24.zip`.

## VM'de başlatma

Komutlar iki ayrı yerde çalışır: önce Windows PowerShell'de, sonra ssh ile girilen VM'de.

**1. Windows PowerShell.** Zip'in bulunduğu klasörde (`Y:\HalukAI`). VM kapalıysa önce `Y:\HalukAI\Ortak_Kopru\kopru` içinde `.\Kopru_Izle.cmd VM`.

```powershell
$K = "Y:\HalukAI\02_Govde\Canli\CLI_Katmanlari"
$G = "$K\Runtime\Git-Portable-2.56.0.2\usr\bin"
$S = "$K\01_Claude_Code_Hacker\Home\.ssh"
$O = @("-i", "$S\hacker_arm64_035", "-o", "UserKnownHostsFile=$S\known_hosts", "-o", "StrictHostKeyChecking=yes")
& "$G\scp.exe" -P 2222 @O hacker-devri-2026-10-24.zip hacker@127.0.0.1:
& "$G\ssh.exe" -p 2222 @O -t hacker@127.0.0.1
```

Zip'e göreli adla başvurulur. scp, `Y:\...` gibi bir yoldaki iki noktayı uzak makine adı sanır.

**2. VM içinde.** ssh'den sonra istem `hacker@...$` olur.

```sh
python3 -m zipfile -e ~/hacker-devri-2026-10-24.zip ~/      # ~/hacker-devri/ oluşur
git clone https://github.com/HalukAINRS/ortak-kopru ~/ortak-kopru
git -C ~/ortak-kopru checkout claude/hacker-devri-2026-10-24  # ana dala birleşene kadar
cd ~/hacker-devri && /home/hacker/bin/claude-arm64-035
```

Claude Code `~/hacker-devri/CLAUDE.md`'yi okur ve "İlk açılışta" adımlarıyla başlar. Paketi `~` köküne değil, `~/hacker-devri/` altına açın. İzleyici Hacker'ı `~` dizininde çağırıyor; talimat dosyası orada durmazsa izleyici çağrılarına karışmaz.

VM'den GitHub'a gönderim için VM'de ayrıca kimlik gerekir (örn. `gh auth login`). Bu adım Haluk'un kararı; o zamana kadar köprüye yazım Windows tarafındaki `Kopru_Izle.cmd Ekle` ve `Gonder` ile sürer.

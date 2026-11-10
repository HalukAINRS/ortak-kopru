# ortak-kopru

## Kopru_Copilot.cmd

GitHub Copilot CLI'yı bu depoya bağlı olarak şu ayarlarla açan Windows başlatıcısı:

| Ayar | Değer | Copilot seçeneği |
|---|---|---|
| Mod | autopilot | `--autopilot` |
| Model | Claude Opus 5.5 | `--model claude-opus-5.5` |
| Akıl yürütme eforu | max | `--reasoning-effort max` |

### Kullanım

1. [Kopru_Copilot.cmd](Kopru_Copilot.cmd) sayfasında **Download raw file** düğmesiyle dosyayı indirin.
2. Dosyaya çift tıklayın. Windows "bilgisayarınızı korudu" uyarısı verirse **Ek bilgi → Yine de çalıştır** seçin (ya da dosya Özellikler'inde **Engellemeyi kaldır** kutusunu işaretleyin).
3. Betik sırasıyla şunları yapar:
   - Git'i ve GitHub Copilot CLI'yı bulur; eksikse onayınızla `winget` ile kurar.
   - Depoyu `%USERPROFILE%\ortak-kopru` klasörüne klonlar (depo özel olduğu için Git ilk seferde tarayıcıda GitHub girişi isteyebilir); klon zaten varsa `git pull --ff-only` ile günceller.
   - Copilot'u bu klasörde yukarıdaki ayarlarla başlatır.
4. İlk açılışta Copilot klasöre güvenip güvenmediğinizi sorar; gerekirse `/login` ile oturum açın. Autopilot penceresinde **Enable all permissions (recommended)** seçili gelir, Enter ile onaylayın.

Ek Copilot seçenekleri olduğu gibi aktarılır. Örneğin son oturumu sürdürmek için:

```cmd
Kopru_Copilot.cmd --continue
```

### İsteğe bağlı ortam değişkenleri

| Değişken | Etkisi |
|---|---|
| `KOPRU_KLASOR` | Deponun yerel klasörü. Verilmezse betik bir ortak-kopru klonunun içindeyse o klasör, değilse `%USERPROFILE%\ortak-kopru` kullanılır. |
| `KOPRU_TAM_IZIN=1` | `--allow-all` ekler. İzin penceresi çıkmaz; Copilot tüm araçları, yolları ve adresleri sormadan kullanır. |
| `KOPRU_DENEME=1` | Araçları ve depoyu denetler, çalıştırılacak komutu gösterir; Copilot'u başlatmaz. |

Kalıcı yapmak için örnek: `setx KOPRU_TAM_IZIN 1` (yeni açılan pencerelerde geçerli olur).

### Notlar

- Dosya ASCII ve CRLF satır sonlarıyla saklanır (`.gitattributes`: `*.cmd -text`); düzenlerken bu biçimi koruyun.
- Model ya da efor hesabınızda kullanılamıyorsa veya Copilot CLI eskiyse Copilot hata verir; `copilot update` ile güncelleyin.
- PowerShell 7 (`pwsh`) önerilir. Bulunamazsa Copilot Windows PowerShell 5.1 kullanır: `winget install --id Microsoft.PowerShell -e`

## karargah/claude_code

Claude Code karargâhını "tek ortam" kuralına göre kuran kit: her oturum (yeni, `--continue`, `--resume`) karargâh kökünde açılır; başka klasör yalnızca uzak yer olarak eklenir. Adlar ve kalıplar [usul.md](karargah/claude_code/kit/.claude/rules/usul.md) dosyasındadır.

| Kit dosyası | Karargâhtaki yeri | İşi |
|---|---|---|
| `kit/claude_code.cmd` | `claude_code.cmd` | Kapı: oturumu kökte açar, `--burada` ile çağrılan klasörü ekler ve oturuma adını verir |
| `kit/araclar/durum_satiri.cmd`, `.ps1` | `araclar\` | Durum satırı: ortamın nerede olduğunu ve eklenen uzak yerleri gösterir |
| `kit/araclar/kanit.cmd` | `araclar\kanit.cmd` | Kanıt: kapıyı ve durum satırını sınar, rapor verir |
| `kit/.claude/settings.json` | `.claude\settings.json` | Durum satırını bağlar; dosya araçlarını kök ve eklenen yerlerle sınırlar |
| `kit/.claude/rules/usul.md` | `.claude\rules\usul.md` | Usul: sözlük, kalıplar, ileti biçimi, kanıt damgaları |

### Kurulum

1. Depoyu klonlayın ya da güncelleyin.
2. Önce kuru çalıştırın; hiçbir dosya kopyalanmaz, yapılacaklar listelenir:

   ```cmd
   set KARARGAH_DENEME=1
   karargah\claude_code\kur.cmd
   ```

3. Kurun (yeni pencerede ya da `set KARARGAH_DENEME=` yazdıktan sonra):

   ```cmd
   karargah\claude_code\kur.cmd
   ```

Kurucu hedefi argümandan, `KARARGAH_HEDEF` değişkeninden ya da `Y:\02_karargahlar\01_claude_code_karargah*` aramasından bulur. Eski kapıyı `claude_code.asil.cmd` (yalnızca ilk kurulumda) ve `claude_code.onceki.cmd` olarak yedekler. Var olan `.claude\settings.json` dosyasının üzerine yazmaz; kit ayarını yanına `settings.kit.json` olarak koyar. Sonunda karargâhın kanıtını (`araclar\kanit.cmd`) çalıştırır: raporda `KALDI` satırı olmamalıdır.

### Kullanım

| Çağrı | Sonuç |
|---|---|
| `claude_code.cmd` | Oturum karargâh kökünde |
| `claude_code.cmd --burada` | Oturum yine kökte; çağrılan klasör uzak yer olarak eklenir, oturum klasörün adını alır |
| `claude_code.cmd --continue` | Son oturuma devam; bayraklar yeniden verilir |
| `claude_code.cmd remote-control` | Remote Control sunucusu kökte; karakter ve yetki fiilden sonra verilir |
| `KARARGAH_DENEME=1` | Komutu ve çalışma dizinini gösterir, Claude Code'u başlatmaz |

Durum satırı `karargah | uzak: C:\proje (+1) | ad: proje | 2.1.322` biçimindedir. `ORTAM KAYDI` oturumun kökten taşındığını, `KAPI DISI` oturumun kapıdan açılmadığını gösterir.

### Sınır ayarı

`.claude\settings.json` içindeki `blockReadsOutsideWorkingDirectories` ve `blockWritesOutsideWorkingDirectories`, dosya araçlarının kök ve eklenen yerler dışına erişmesini her yetki kipinde reddeder. Kök dışındaki bir klasör (örneğin `Y:\02_karargahlar\ortak`) gerekiyorsa `/add-dir` ile eklenir. Kabuk komutlarını sınırlamaz. İstemiyorsanız bu iki satırı silin.

### Kanıt

Karargâh kendi durumunu sınar ve gösterir. Parçaların nasıl çalıştığı ve her iddianın hangi kanıta dayandığı [ACIKLAMA.md](karargah/claude_code/ACIKLAMA.md) dosyasındadır.

| Nerede | Komut | Ne yapar |
|---|---|---|
| Karargâhta | `araclar\kanit.cmd` | Kapıyı kuru çalıştırır, durum satırını örnek girdiyle sınar; oturum açmaz, ağa çıkmaz |
| Karargâhta | `araclar\kanit.cmd --canli` | Ek olarak gerçek `claude.exe` ile tek bir `-p` çağrısı yapar; hesabınızdan küçük bir kullanım düşer |
| Depoda (bulut oturumu) | `karargah/claude_code/sinama/sina.sh` | Kurucuyu ve `kanit.cmd` dosyasını wine'da, durum satırını PowerShell'de sınar |
| Depoda (bulut oturumu) | `karargah/claude_code/sinama/sina.sh --canli` | Ek olarak gerçek `claude` ile iki küçük çağrı yapar |

Rapor `gecici\kanit.son.txt` dosyasına yazılır. Bulut oturumu Windows'ta ne olduğunu ancak bu rapordan görebilir; raporu oturuma yükleyin ya da depoya işleyin.

Bugünkü durum:

- **Denendi (wine 9.0 `cmd`):** `kanit.cmd` içindeki 12 kapı sınaması ve kurucunun 6 durumu.
- **Denendi (PowerShell 7.4, Linux):** durum satırı betiği, 10 örnek girdi.
- **Denendi (Linux, gerçek `claude` 2.1.322):** göreli yol çalışma dizinine göre çözülüyor; `--add-dir=` ile eklenen boşluklu klasör okunuyor; kit ayarı dışarıdaki dosyanın okunmasını reddediyor, ayar yokken dosya okunuyor.
- **Denenmedi:** gerçek Windows ve `claude.exe`, Windows PowerShell 5.1, durum satırının Claude Code içinden çağrılması, sürücü kökünü (`C:\`) eklemek, ASCII dışı harfli yol. Bunları Windows'ta `kanit.cmd` ve `kanit.cmd --canli` sınar.

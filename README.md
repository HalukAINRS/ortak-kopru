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

Claude Code karargâhını "tek ortam" düzenine göre kuran kit. Her oturum (yeni, `--continue`, `--resume`) karargâh kökünde açılır; başka klasör oturuma yalnızca uzak yer olarak eklenir. Durum satırı ortamın nerede olduğunu oturum boyunca gösterir; `kanit.cmd` kapıyı ve durum satırını sınar ve rapor yazar. İşleyiş, doğrulanmış durum ve kalan iş tek belgededir: [tek_ortam_kaydi.md](karargah/claude_code/kit/arastirma_tasarim/tek_ortam_kaydi.md).

### Kurulum

Windows komut isteminde, depo klonunun kökünden çalıştırılır. Kurucu hedefi argümandan, `KARARGAH_HEDEF` değişkeninden ya da `Y:\02_karargahlar\01_claude_code_karargah*` aramasından bulur. Önce kuru çalıştırma yapılır; hiçbir dosya kopyalanmaz, yapılacaklar listelenir:

```cmd
set KARARGAH_DENEME=1
karargah\claude_code\kur.cmd
```

Çıktı beklendiği gibiyse değişken temizlenir ve kurulur:

```cmd
set KARARGAH_DENEME=
karargah\claude_code\kur.cmd
```

Kurucu eski kapıyı `claude_code.asil.cmd` (yalnızca ilk kurulumda) ve `claude_code.onceki.cmd` olarak yedekler, var olan `.claude\settings.json` dosyasının üzerine yazmaz ve sonunda karargâhın kanıtını çalıştırır; raporda `KALDI` satırı olmamalıdır. Geri almak için `claude_code.onceki.cmd` dosyası `claude_code.cmd` üzerine kopyalanır.

### Kullanım

| Çağrı | Sonuç |
|---|---|
| `claude_code.cmd` | Oturum karargâh kökünde |
| `claude_code.cmd --burada` | Oturum yine kökte; çağrılan klasör uzak yer olarak eklenir, oturum klasörün adını alır |
| `claude_code.cmd --continue` | Son oturuma devam; bayraklar yeniden verilir |
| `claude_code.cmd remote-control` | Remote Control sunucusu kökte |
| `araclar\kanit.cmd` | Kanıt: oturum açmaz, ağa çıkmaz; raporu `gecici\kanit.son.txt` dosyasına yazar |
| `KARARGAH_DENEME=1` | Kapı ve kurucu ne yapacağını gösterir, yapmaz |

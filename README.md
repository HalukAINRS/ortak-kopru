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

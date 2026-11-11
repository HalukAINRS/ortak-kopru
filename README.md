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

## 33_Protokol_Kutuphanesi

33 protokol, köken aldıkları üç kimlik metni, ortak biçim kuralları, çalışma kaydı ve denetim araçlarından oluşan kütüphane. Okumaya ve çalışmaya klasördeki `00_HARITA.md` dosyasından başlanır; her protokol tek başına yeter. Dosyaların bu sürümle aynı olup olmadığı klasörün içinde `sha256sum -c SHA256SUMS` komutuyla denetlenir. Klasördeki dosyalar Git'te satır sonları dönüştürülmeden saklanır (`.gitattributes`).

## aktarici

Kütüphaneyi bu depodan Google Drive'daki 128-bit CPU klasörüne taşıyan ve orada `SHA256SUMS` ile doğrulayan Köprü Aktarıcısı (`kopru_aktarici.gs`, bir Google Apps Script betiği) ve onun yolu (`Kutuphane_Aktarim_Protokolu.md`). Aktarıcı, Drive'ın sahibinin Google hesabında çalışır: protokoldeki Uyanma adımlarıyla bir kez uyandırılır, sonra her hafta kendiliğinden çalışır ve Drive'daki kopyayı bu depodaki kütüphanenin aynası olarak tutar. Kütüphanedeki değişiklikler için aktarıcıya dokunulmaz; GitHub anahtarı depoda değil, Apps Script'in betik özelliklerinde durur.

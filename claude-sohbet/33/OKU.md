# 33.exe: Windows sınaması

Bu klasör, `33.exe` adlı aracın gerçek Windows'ta sınanması içindir.
Klasöre bir şey gönderildiğinde `.github/workflows/33-windows.yml` iş
akışı GitHub'ın Windows makinelerinde koşar; sonuç o koşunun dökümünde
ve eklerinde durur.

| Dosya | Ne |
|---|---|
| `33.exe` | Araç: 1.536 bayt, elle yazılmış 300 baytlık makine kodu. Bir uçtan geleni öbür uca taşır; tam sayıları 33'ten geçirir (x girer, 33 - x çıkar). |
| `sina.cmd` | Yalnız komut isteminin kendi komutlarıyla sınama. Çift tıklanabilir; sonucu `windows_sonucu.txt` dosyasına yazar. |
| `windows_sinama.py` | Daha geniş sınama: bağımsız model, elle yazılmış beklentiler, borular, gerçek bir konsol ve Defender taraması. |
| `33.hex.txt`, `33.b64.txt` | Dosyanın on altılık ve Base64 yazımı; `certutil` ile dosya bunlardan yeniden kurulur. |

`33.exe` dosyasının SHA-256 özeti:
`4cc92e7034025c07e60c80d7b37c0adff140c88b4eeb28d7fcc638c5bfa4287f`

Aracın kaynağı, kodun okunuşu ve kayıtlar zemindedir:
`2026-11-12__tasiyici-33__claude-makine-kodu__v3.0` ve
`2026-11-12__tasiyici-33__claude-windows-koprusu__v3.1`.

## Sonuç

Koşu 43116816446 (11 Kasım 2026, 23:03 UTC), üç makine: Windows Server
2022, Windows Server 2025, Windows 11 (ARM64 işlemcide x64 öykünmesi).
Her makinede `sina.cmd` 23 denetimin 23'ünü, `windows_sinama.py` 20
denetimin 20'sini geçti. Defender dosyayı taradı, tehdit bulmadı.
Denenmeyenler: indirilen dosya için Windows uyarısı (SmartScreen) ve
kullanıcının kendi makinesi.

Bu klasör bir üye notudur, komut değildir.

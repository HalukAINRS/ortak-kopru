# Şaman–Şahit–Hacker: mevcut kurulumun devam yolları

Bu kayıt Haluk'un üçüncü önceliği için gerçek sürüm, devir dizini ve başlatıcı denetimidir. [Doğrulama](DOGRULAMA.json) ile [başlatıcı kopyaları](baslatici_kopyalari/) birlikte okunur. Kaynak kopyaları burada arşivlenir; çalıştırılacak yer her dosya için JSON'daki `install_directory` alanıdır. Mevcut kurulumdaki bağımlılıkların yerine boş bir kurulum oluşturmaz.

| Katman | Gözlenen çalışma yolu | Yapılan işlem |
| --- | --- | --- |
| Şaman | Windows PowerShell 7.6.8; Codex CLI 0.163.0 | Varsayılan `resume --last`, açık Workspace'e bağlı ve etkileşimsiz otomasyon oturumları seçime katılmıyor. Mevcut kısayol ve dört kuru denetim önceki görevde doğrulandı; kaynakları buraya alındı. |
| Şahit | Copilot CLI 1.0.103; belirli devir oturumu | `Sahit_Devam.cmd`, en son otomasyon oturumunu seçebilen eski `--continue` yolundan mevcut `Sahit_Oturum.cmd` yoluna bağlandı. Yeni wrapper'ın `-Mod Kontrol` çağrısı geçti; açık oturum kapatılmadı. |
| Hacker | Mevcut VM'de `uname -m` aarch64; sarmalayıcının çıktısı Claude Code 2.1.308 | `Hacker_Devam.cmd` ve `Hacker_Yeni.cmd`, masaüstünün zaten kullandığı `Hacker_Ac.ps1` girişine bağlandı. Böylece devam/yeni komutları `~/hacker-devri` bağlamını kullanır; eski `~/HalukAI` girişine gitmez. |

Hacker için mevcut sabit known_hosts ve StrictHostKeyChecking=yes ile salt okunur SSH denemesi geçti. `~/hacker-devri`, içindeki CLAUDE.md, bir proje oturum dosyası ve `~/Kopru` bulundu. Bu, Hacker'ın yeni iletimizi okuduğu veya kabul ettiği anlamına gelmez. Şahit'in kaynak betiği ve sabit devir oturumu değiştirilmedi; mevcut model/efor ayarı korundu. Model kataloğu veya başka model tercihi araştırılmadı.

Yeni başlatıcı düzeltmeleri yerelde uygulandı; önceki üç CMD `Kurulum_Devam_20261024/Yedek` altında korundu. Şaman'ın önceki başlatıcı/kısayol yedeği kendi `Defter_Koprusu/Baslatici_Yedekleri` dizinindedir. Bu denetim yeni etkileşimli model oturumu açmadı.

## Kullanım

- Şaman: mevcut `03 - OpenAI Codex (PowerShell 7.6.8).lnk` veya gerçek kurulum dizinindeki `Saman_Devam.cmd`.
- Şahit: gerçek kurulum dizinindeki `Sahit_Devam.cmd`; salt okunur kontrol için `Sahit_Devam.cmd -Mod Kontrol`. Açık devir oturumunu ikinci kez açma davranışını mevcut `Sahit_Oturum.ps1` denetler.
- Hacker: mevcut `01 - Claude Code (Ubuntu VM).lnk` veya düzeltilen `Hacker_Devam.cmd`; ayrı yeni devir oturumu için `Hacker_Yeni.cmd`.

deus_ex_machina'nın yeni yüzeyinde fiilen kayıtlı katman hâlâ yalnız Şaman'dır. Üç CLI'ın kurulu bulunması ile üçünün bu yüzeye bağlanması ayrı işlerdir. Otomatik tüketici ve VM taşıması açık kalır. Bir ağ adresi, anahtar veya tam oturum kimliği bu yayına konmadı.

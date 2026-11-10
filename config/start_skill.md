# Divan bulut başlangıcı

## Sabitlenen environment ve remote environment

Son karar: Codex CLI ve Codex Bulut için ana environment **CLI**.
Codex CLI'nin remote environment çalışma hedefi `Y:\02_karargahlar\01_codex_karargahı`;
Codex Bulut'un remote environment hedefi `https://github.com/HalukAINRS/ortak-kopru` deposudur.
Bulut bu depo için mevcut `/workspace/ortak-kopru` checkout'unu kullanır.
GECERLI_DUZEN.md ve 00_yonetim/ortam_sabitleme.json güncel kayıttır.
Buradaki adlandırma kullanıcının çalışma/paylaşım hedeflerini belirtir; native
Codex environments.toml dosyasına veya ağ bağlamasına uygulanmış gibi gösterme.
İki tarafın paylaşımı mevcut Git/yeni 0 protokolüyle yürütülür. Yerel 1 sonuçları
paylaşılmaz; kullanıcı mesaj taşımaz. Windows sürücüsünün bulutta bağlı olduğunu
iddia etme. Gerçek Windows katılımı ve GitHub yazma ayrıca doğrulanmalıdır.
Önceki `/workspace/karargah-kopru` native executor taslağı araştırma olarak
korunmuştur; güncel plan için etkinleştirme veya SSH/VPN gereksinimi çıkarma.

Bu ortamda mevcut `/workspace/ortak-kopru` checkout'unu kullan. Bulut görevleri
zaten izoledir; kullanıcı açıkça istemedikçe Git worktree oluşturma.
Ortam snapshot'unda `/workspace/divan` dosyaları korunmalıdır. Bu dosyalar yoksa
kurulumu hazır sayma; yalnızca depoyu klonlamak bu yardımcıları geri getirmez.

1. `/workspace/divan/AGENTS.md` ve `README.md` oku; kullanıcı talimatları önceliklidir.
2. `bash /workspace/divan/config/install.sh` çalıştır; tekrar çalıştırmak mesajları,
   sonuçları ve denetim durumunu korur. Harici paket gerekmiyor.
3. `python3 /workspace/divan/bin/divan.py status` ile denetimi ve üye durumlarını gör.
   `duraklat` durumunda yeni iş alma veya yayımlama. Denetimi yalnızca kullanıcının
   açık isteğiyle değiştir.
4. Bu oturumun gerçek ürününe karşılık gelen üye kimliğini kullan. Codex oturumunu
   Claude/Gemini olarak adlandırma. Aynı dosya sisteminde `inbox --member <kimlik>`
   kullan; ayrı ortamlarda kendi bağlı Git araçlarınla `divan_git.py pull` yapıp
   gelenleri oku. `push` ortak depoya gerçek yazımdır; paylaşılması istenen yeni 0
   bulunduğunda kullan. Boş pano için uzak dal oluşturulmaz. GitHub yazma erişimi
   bu onboarding sırasında denenmedi; ilk kullanımda hatayı ayrı değerlendir.
5. Girdiyi `claim` ile al, çalış, sonucu yalnızca kendi `sonuclar_1/` alanına
   `complete` ile kaydet. Yeni araştırma/iş başlangıcı oluşturup `publish` kullan;
   README'deki alanlar ve gerekirse `--from-id`/`--from-result` ile ilişkilendir.
6. Aktif bir oturum çalışırken kendi gelen kutusunu/Git paylaşımını kontrol eder;
   kullanıcıyı üyeler arasında mesaj taşımaya yönlendirme. Altı ürünün sürekli
   çalışan oturumları veya bulutlar arası zamanlayıcı bu kurulumla başlatılmış değildir.
7. Masaüstü ChatGPT, Claude veya Gemini uygulaması kullanma. Web ürününün dosya/Git
   araçlarına erişimi yoksa bağlı sayma. A4 belgeleri yüklenmeden okundu iddiasında bulunma.
8. Gerektiğinde `python3 -m unittest discover -s /workspace/divan/tests -v` çalıştır.
   Git aktarım testleri geçici yerel depolar kullanır, GitHub'a yazmaz.

Gerçek katılım için KATILIM.md ve arastirma/SAGLAYICI_ARASTIRMASI.md dosyalarını
oku. Kullanıcının özel bağlantı hedefleri yalnızca yerel
00_yonetim/baglanti_hedefleri.json dosyasında tutulur; paketlere/Git'e eklenmez.
Claude Code 2.1.322 ve Gemini CLI 0.67.0 bu ortamda hazırlanıp sürüm/yardım
komutlarıyla denendi. Gerekli yerel bağımlılıkları kilitli kaynaklardan yenilemek
için `bash /workspace/divan/config/install_clients.sh /workspace/tools/divan-clients`
kullan. Bu giriş/model bağlantısı sağlamaz. Antigravity CLI'nin gerçek komutu
`agy`; Gemini CLI'yi bu üye yerine geçirme. Claude Code CLAUDE.md, Gemini CLI
GEMINI.md üzerinden ortak kurallara yönlendirilir.

Yerel duraklatma başka bulutlara taşınmaz. Gerçek üyeler arası gidiş-dönüş ve
ortak kullanıcı denetimi sağlanmadan bütün ağı hazır sayma.

Çalışma sunucusu/arka plan modeli gerekmiyor. Canlı süreçler snapshot'ta saklanmaz.
`Kopru_Copilot.cmd` Windows içindir; ASCII ve CRLF biçimini koru. Linux'ta Windows
başlatıcısını çalıştırılmış sayma. Kurulum için mevcut izlenen depo dosyalarını değiştirme.

Codex remote control paket hatası resmî aynı sürüm paketiyle ayrı dizinde giderildi.
`/workspace/tools/REMOTE-CONTROL.md` onarımı kaydeder; `bash /workspace/tools/codex-remote status`
yerel daemon durumunu, `start` yeniden başlatmayı sağlar. Yerel daemon çalışıyor ve
remoteControlEnabled=true; uzak bağlantı ise chatgpt.com CONNECT403 nedeniyle
hazır değil. Kullanıcının Claude ve Cloud Shell adresleri de sırasıyla claude.ai
ve shell.cloud.google.com CONNECT403 aldı. Ağ ayarları uygulandıktan sonra yeni
bağlantılarla doğrula. Ana dizin, CODEX_HOME veya kimlik bilgilerini kopyalayıp
değiştirme; TLS doğrulamayı kapatma. Uzak ortam kimliği/eşleştirme sonucu almadan
remote control bağlı deme. Ağ listesi/taslak okunamıyorsa bilinmeyen listeyi ezme.

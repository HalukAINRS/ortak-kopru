# Gerçek üyelerin katılımı

## Bu kurulumun mevcut sınırı

Dosya protokolü ve yerel Git gidiş-dönüşü çalışır. Altı gerçek sağlayıcının
aynı protokole katılımı henüz doğrulanmadı. Kullanıcının verdiği Claude sohbeti
ve Cloud Shell adresleri özel `00_yonetim/baglanti_hedefleri.json` dosyasındadır;
kurulum paketine alınmaz. İki adrese de bu ortamdan yeni HTTPS bağlantısı
`CONNECT 403` aldı. Kullanıcı oturumunun açık olup olmadığı sınanamadı.

İlk hesap girişi/araç bağlama işlemi hesap sahibine aittir; sohbetten parola,
anahtar veya oturum çerezi istenmez. Sonrasında her ajan kendi gelen kutusunu
okur ve kendi araçlarıyla paylaşır; kullanıcı üyeler arasında mesaj taşımaz.

## Aynı dosya sistemindeki CLI

Python 3.11+ ve Git ile mevcut dizini kullanın. Yeni worktree oluşturmayın.
Önce `AGENTS.md`, kendi `BASLANGIC.md` dosyanız ve kullanıcı denetimini okuyun:

```bash
bash /workspace/divan/config/install.sh
python3 /workspace/divan/bin/divan.py inbox --member claude_code_cli
```

Bu ortamda hazırlanan araçlar:

```bash
cd /workspace/divan
/workspace/tools/divan-clients/node_modules/.bin/claude
# Ayrı, uygun Gemini hesabıyla CLI kullanımı için:
/workspace/tools/divan-clients/node_modules/.bin/gemini
```

Bu komutlar gerçek sağlayıcı ürününü açar; hesap erişimi sağlanmadan hazır
sayılmaz. Claude Code `CLAUDE.md`, Gemini CLI `GEMINI.md` üzerinden ortak
yönergelere yönlendirilir. Codex `AGENTS.md` kullanır. Otomatik izin atlama veya
oturum dosyası kopyalama uygulanmaz. Antigravity için `agy` kurulumu, resmî
kurulum adresi erişilebilir olduğunda o belgeden yapılmalı; tahmini npm adı
kullanılmamalıdır. Gemini CLI, Antigravity yerine geçirilmemelidir.

## Ayrı bulut veya Google Cloud Shell

Statik kurulum arşivi ve `.sha256` özeti ilk kuruluma aittir. Doğruladıktan
sonra kullanıcıya ait uygun dizine açın. Bu bir defalık dağıtım, çalışma
mesajlarının kullanıcı aracılığıyla taşınması değildir.

```bash
# Arşiv ve .sha256 dosyasının bulunduğu dizinde:
sha256sum -c divan-bulut-kurulum-guncel.tar.gz.sha256
tar -xzf divan-bulut-kurulum-guncel.tar.gz -C /kullaniciya/ait/kurulum
bash /kullaniciya/ait/kurulum/divan/config/install.sh
python3 /kullaniciya/ait/kurulum/divan/bin/divan_git.py pull --repo /mevcut/ortak-kopru
python3 /kullaniciya/ait/kurulum/divan/bin/divan.py inbox --member gemini_sohbet
```

Cloud Shell'deki gerçek model/araç `gemini` veya `agy` durumunu resmî güncel
belge ve oturumun kurulu komutlarıyla kontrol etmelidir. Google kimliği bu Codex
makinesinden taşınmaz. Ayrı ortamın kendi Git okuma/yazma erişimi gerekir.
Mevcut ortak-kopru checkout'u yoksa ilk kurulumda normal HTTPS clone yapılır;
var olan kullanıcı checkout'u sıfırlanmaz. Bu hazırlıkta GitHub'a yazılmadı.

Windows'ta arşivi uygun kullanıcı dizinine açtıktan sonra PowerShell'de
`py -3 .\divan\bin\divan.py init` ve `doctor` çalıştırılabilir; gerçek Windows
çalıştırması burada denenmedi. `--root` ve `--repo` gerçek yollarla verilir.
Kaynak `.cmd` dosyaları ASCII/CRLF biçiminde korunur. Bulut dizini Windows'un
X:/Y: sürücülerini kendiliğinden bağlamaz. Doctor, dosya sisteminin atomik
yayımlama için gereken hardlink desteğini de fiilen dener.

## Katılımın kanıtı

1. Gerçek oturum kendi ürününü, kullandığı araç erişimini ve Divan kökünü belirtir.
2. Yalıtılmış bir test kökünde yeni 0 okunur, claim edilir ve yerel 1 kaydedilir.
3. Rastgele test değeri içeren türetilmiş yeni 0, karşı ortama kendi araçlarıyla
   ulaştırılır. Karşı taraf okuduğunu kendi oturumundan doğrular.
4. Hem gidiş hem dönüş ve gerçek ürün oturumu gözlemlenmeden üye kaydındaki
   `dogrulanmadi` değiştirilmez. Testlerde kullanılan üye adları sağlayıcı
   oturumları değildir; yerel simülasyon ayrı raporlanır.

Web sohbetinde yalnızca dosya yükleme veya salt okunur bağlayıcı varsa yazabilen
ortak pano varmış gibi davranılmaz. MCP filesystem referans sunucusu yerel
stdio kullanır; web ürününe kendiliğinden ulaşılabilir bir sunucu oluşturmaz.

## Kullanıcı denetimi ve tamamlanma

`control` yereldir; ayrı bulutlarda küresel durdurma için güvenilir yönetim
bağlantısı gerekir. Bu bağlantı ve gerçek ürün gidiş-dönüşleri açık iştir.
A4 kaynakları sağlanmadığından araştırılmış gösterilmez. Bütün işler tamamlanmadan
kaynak belgeye BITIRDIK eklenmez. Orijinal readme.txt Windows-1254, talimatlar.txt
UTF-8'dir; kopyalar baytları korunarak saklanmıştır.

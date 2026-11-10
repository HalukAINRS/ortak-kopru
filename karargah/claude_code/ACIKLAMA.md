# Açıklama: oluşum neyi görür, neyi gösterir

Gaye, karargâhın kendi durumunu **görebilmesi** ve bunu **gösterebilmesi**: ortam nerede, hangi uzak yerler
ekli, kural tutuyor mu. Bu belge parçaların nasıl çalıştığını ve her iddianın hangi kanıta dayandığını anlatır.
Adlar [usul.md](kit/.claude/rules/usul.md) sözlüğündendir.

## Üç yeti

| Yeti | Parça | Ne yapar |
|---|---|---|
| Tutar | Kapı (`claude_code.cmd`), sınır ayarı | Oturumu her açılışta kökte başlatır; dosya araçlarını kök ve eklenen yerlerle sınırlar |
| Görür | Durum satırı, `kanit.cmd` | Claude Code'un bildirdiği çalışma dizinini ve ek dizinleri okur; kapıyı ve kendini sınar |
| Gösterir | Açılış başlığı, durum satırı, kanıt raporu | Durumu oturum boyunca ekranda tutar; sınama sonucunu `gecici\kanit.son.txt` dosyasına yazar |

## Nasıl çalışır

- **Kök neden sabit.** Claude Code proje kimliğini çalışma dizinine bağlar: oturum kayıtları, otomatik hafıza,
  talimat dosyaları, `.claude` ayarları ve kancaları oradan gelir. Kapı her çağrıda köke geçer ve
  `CLAUDE_CODE_PROJECT_DIR_NAME` değerini sabitler; böylece yeni ve devam eden oturumlar aynı yerde toplanır.
- **Uzak yer neden `--add-dir=` ile.** Ek dizin dosya erişimi verir; o klasörün ayarları, kancaları ve
  `.mcp.json` dosyası yüklenmez. Değer `=` ile verilir, çünkü `--add-dir` ve `--mcp-config` çok değerlidir ve
  boşlukla yazılınca ardındaki bayraksız argümanı da değer sanar.
- **Bayraklar neden her açılışta yeniden veriliyor.** Devam eden oturum `--add-dir`, `--settings` ve
  `--mcp-config` değerlerini geri yüklemez; bypass kipinde biten oturum varsayılan kipte açılır.
- **`remote-control` neden ayrı dal.** Karakter bayrakları fiilden önce verilirse Claude Code açılmayı reddeder;
  kapı `--settings` ve `--permission-mode` değerlerini fiilden sonra verir.
- **Durum satırı neyi okur.** Claude Code her yenilemede betiğe bir JSON verir. Betik `workspace.project_dir`,
  `workspace.current_dir`, `workspace.added_dirs` ve `session_name` alanlarını okur, kökü kapının ortama
  koyduğu `KARARGAH_ROOT` ile karşılaştırır. Eşitse `karargah`, değilse `ORTAM KAYDI`, değişken yoksa
  `KAPI DISI` yazar.
- **Sınır neyi kapsar.** `blockReadsOutsideWorkingDirectories` ve `blockWritesOutsideWorkingDirectories` dosya
  araçlarını her yetki kipinde kök ve eklenen yerlerle sınırlar. Kabuk komutlarını, MCP araçlarını ve
  kancaların çalıştırdığı programları sınırlamaz.
- **Usul nasıl her oturuma giriyor.** `.claude\rules\` altındaki dosyalar çalışma dizininden yüklenir; kök sabit
  olduğu için `usul.md` her oturumdadır.

## İddia ve kanıt

| # | İddia | Kanıt | Damga |
|---|---|---|---|
| 1 | Kapı her çağrı biçiminde oturumu kökte açar | `kanit.cmd`, 12 kapı sınaması | Denendi (wine `cmd`) |
| 2 | `--burada` klasörü ekler ve oturuma adını verir; `--continue` ile ad verilmez | `kanit.cmd` | Denendi (wine `cmd`) |
| 3 | `=` ile verilen çok değerli bayrak ardındaki argümanı yutmaz | Linux `claude` 2.1.322 ayrıştırıcısı | Denendi |
| 4 | Göreli yol çalışma dizinine göre çözülür; `--add-dir=` ile eklenen boşluklu klasör okunur | `sina.sh --canli` | Denendi (Linux, gerçek `claude`) |
| 5 | Kit ayarı dışarıdaki dosyanın okunmasını reddeder; ayar yokken dosya okunur | `sina.sh --canli`, iki çağrının karşılaştırması | Denendi (Linux, gerçek `claude`) |
| 6 | Durum satırı ortamı, uzak yerleri ve oturum adını doğru yazar | `sina.sh`, 10 örnek girdi | Denendi (PowerShell 7.4) |
| 7 | Kurucu eski kapıyı yedekler ve var olan ayarın üzerine yazmaz | `sina.sh`, 6 kurucu sınaması | Denendi (wine `cmd`) |
| 8 | Durum satırı Windows PowerShell 5.1 ile ve Claude Code içinden çalışır | `kanit.cmd` (Windows), oturumda gözle | Denenmedi |
| 9 | Sürücü kökü eklenir; `ı` harfli kökte sonuç aynıdır | `kanit.cmd` (Windows) | Denenmedi |
| 10 | Windows'taki `claude.exe` 4 ve 5'teki gibi davranır | `kanit.cmd --canli` (Windows) | Denenmedi |
| 11 | Devam eden oturum eklenenleri geri yüklemez | [Oturumlar](https://code.claude.com/docs/en/sessions) | Belgede |
| 12 | Ek dizin dosya erişimi verir, yapılandırma yüklemez | [İzinler](https://code.claude.com/docs/en/permissions) | Belgede |
| 13 | Sınır kabuk komutlarını kapsamaz | [İzinler](https://code.claude.com/docs/en/permissions), derlemedeki ayar açıklaması | Belgede |

## Kanıt nasıl yenilenir

**Windows'ta (karargâhta).** Kurucu kurulumun sonunda kendiliğinden çalıştırır; sonradan elle:

```cmd
araclar\kanit.cmd
araclar\kanit.cmd --canli
```

İlki oturum açmaz ve ağa çıkmaz. İkincisi gerçek `claude.exe` ile tek bir `-p` çağrısı yapar: yalnızca Read
aracı açıktır, oturum kaydı tutulmaz, hesabınızdan küçük bir kullanım düşer. Rapor `gecici\kanit.son.txt`
dosyasına yazılır. Bulut oturumu Windows'ta ne olduğunu ancak bu rapordan görebilir: raporu oturuma yükleyin
ya da depoya işleyin. Rapor yerel yolları içerir.

**Bulut oturumunda (depoda).**

```bash
karargah/claude_code/sinama/sina.sh
karargah/claude_code/sinama/sina.sh --canli
```

Betik sahte bir karargâh kurar, kurucuyu ve `kanit.cmd` dosyasını wine'ın `cmd` öykünücüsünde, durum satırını
PowerShell'de çalıştırır. `--canli` gerçek `claude` ile iki küçük çağrı yapar.

## Göremediği ve gösteremediği

- **Kabuk komutları.** Sınır yalnızca dosya araçlarını kapsar; kabuk komutu eklenmemiş yere ulaşabilir. Bunu
  usuldeki "eklenmesini iste" kuralı karşılar, bir mekanizma değil.
- **Kapıdan geçmeyen girişler.** Desktop uygulaması ve VS Code eklentisi kapıyı, dolayısıyla karargâhı tanımaz.
  Durum satırı `KAPI DISI` uyarısını yalnızca aynı ayarı okuyan bir oturumda gösterebilir.
- **Claude'un kendi durum satırı.** Durum satırını kullanıcı görür, Claude görmez. Claude durumu oturum içinden
  `kanit.cmd` çalıştırıp raporu okuyarak görebilir.
- **Bulut ile yerel arası.** İki taraf birbirini canlı görmez; aradaki köprü bu depo ve kanıt raporudur.

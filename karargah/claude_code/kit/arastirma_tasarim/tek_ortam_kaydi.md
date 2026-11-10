# Tek Ortam — Operasyon Kaydı

Bu kayıt, Claude Code kolunun "tek ortam" işinin güncel hâlidir: amaç, işleyiş, doğrulanmış durum, kalan iş ve kanıt yolları. Kaynağı `ortak-kopru` deposundaki `karargah/claude_code/kit/arastirma_tasarim/tek_ortam_kaydi.md` dosyasıdır; karargâhtaki kopya kurucuyla yenilenir, değişiklik depoda yapılır. Kural metni `.claude\rules\tek_ortam.md` dosyasındadır ve burada yinelenmez.

## Amaç

Claude Code kendi karargâhından çalışır ve başka yerleri kendine katar; kendisi başka yere taşınmaz. Ürünün varsayımı tersidir: oturum dosyanın bulunduğu yerde açılır ve kimliğini oradan alır. Bu iş o yönü çevirir. Kabul ölçütü üç maddedir: her oturum karargâh kökünde açılır; başka klasör yalnızca uzak yer olarak eklenir; ortamın durumu görülebilir ve gösterilebilir.

## Envanter

```text
ortak-kopru\karargah\claude_code\
|-- kur.cmd                          kiti karargaha kurar, sonunda kaniti calistirir
|-- sina.sh                          kiti bulut oturumunda sinar
|-- CLAUDE.md                        bu kaydi bulut oturumuna yukler
`-- kit\                             karargah kokunun aynasi
    |-- claude_code.cmd              kapi
    |-- araclar\
    |   |-- durum_satiri.cmd         durum satiri komutu
    |   |-- durum_satiri.ps1         durum satirinin asil isi
    |   `-- kanit.cmd                kanit
    |-- .claude\
    |   |-- settings.json            durum satirini baglar
    |   `-- rules\tek_ortam.md       kural
    `-- arastirma_tasarim\
        `-- tek_ortam_kaydi.md       bu kayit
```

Kit aynadır: kitteki bir dosyanın yolu, karargâh köküne göre yoludur. Kurucu var olan `.claude\settings.json` dosyasının üzerine yazmaz ve eski kapıyı `claude_code.asil.cmd` ile `claude_code.onceki.cmd` olarak yedekler.

## İşleyiş

```text
cagri --> [ KAPI ] --kokte acar, bayraklari yeniden verir--> [ claude.exe ]
                                                                  |
                                    JSON: project_dir, added_dirs, session_name
                                                                  v
                                                        [ DURUM SATIRI ] --> ekran

[ KANIT ] --kapiyi kuru calistirir, durum satirini sinar--> ekran + gecici\kanit.son.txt
```

Claude Code proje kimliğini çalışma dizinine bağlar: oturum kayıtları, otomatik hafıza, talimat dosyaları, `.claude` ayarları ve kancaları oradan gelir. Kapı bu yüzden her çağrıda köke geçer ve `CLAUDE_CODE_PROJECT_DIR_NAME` değerini sabitler; yeni ve devam eden oturumlar aynı yerde toplanır. `--burada` ile çağrıldığı klasörü taşınmak yerine `--add-dir=` ile ekler ve yeni oturuma o klasörün adını verir. Değer `=` ile yazılır, çünkü `--add-dir` ve `--mcp-config` çok değerlidir ve boşlukla yazılınca ardındaki bayraksız argümanı da değer sanar.

Kapı bayrakları her açılışta yeniden verir, çünkü devam eden oturum `--add-dir`, `--settings` ve `--mcp-config` değerlerini geri yüklemez ve bypass kipinde biten oturum varsayılan kipte açılır. `remote-control` için ayrı bir dal vardır: karakter bayrakları fiilden önce verilirse Claude Code açılmayı reddeder; kapı `--settings` ve `--permission-mode` değerlerini fiilden sonra verir. Alt komutlar (`mcp`, `plugin`, `agents`, `doctor`) da kökte çalışır, çünkü kayıtlarını bulundukları klasöre göre tutarlar.

Durum satırı görme işini yapar. Claude Code her yenilemede betiğe bir JSON verir; betik çalışma dizinini, ek dizinleri ve oturum adını okur ve kökü kapının ortama koyduğu `KARARGAH_ROOT` ile karşılaştırır. Eşitse `karargah`, değilse `ORTAM KAYDI`, değişken yoksa `KAPI DISI` yazar. Kanıt gösterme işini yapar: kapıyı `KARARGAH_DENEME=1` ile gerçek argümanlarla çağırır, yazdığı komutu ve dizini denetler, durum satırını bu karargâhın gerçek yollarıyla sınar ve sonucu rapora yazar.

Dosya araçlarını kök ve eklenen yerlerle sınırlayan iki ayar (`blockReadsOutsideWorkingDirectories`, `blockWritesOutsideWorkingDirectories`) kitte açık gelmez. Bu sınır, Operasyon Kuralı'nın "Bulunduğun yerle sınırlı kalma" ilkesiyle ve kolların `..\ortak\` altındaki ortak kayıtları okuyup yazmasıyla çatışır. İstenirse `.claude\settings.json` dosyasına elle eklenir; o durumda kök dışındaki her yer uzak yer olarak eklenmelidir. Ayar kabuk komutlarını kapsamaz.

## Doğrulanmış durum

Gözlem, belge ve gözlenmemiş olan ayrı tutulur. Gözlemlerin hepsi bulut oturumunda yapıldı; gerçek Windows'ta hiçbir şey çalıştırılmadı.

| İddia | Kanıt | Durum |
|---|---|---|
| Kapı her çağrı biçiminde oturumu kökte açar | `kanit.cmd`, on iki kapı sınaması | Gözlendi (wine `cmd`) |
| `--burada` klasörü ekler ve oturuma adını verir | `kanit.cmd` | Gözlendi (wine `cmd`) |
| `=` ile verilen çok değerli bayrak ardındaki argümanı yutmaz | Linux `claude` 2.1.322 | Gözlendi |
| Göreli yol çalışma dizinine göre çözülür; `--add-dir=` ile eklenen boşluklu klasör okunur | `sina.sh --canli` | Gözlendi (Linux, gerçek `claude`) |
| Okuma sınırı yazılıyken dışarıdaki dosya okunamaz; yokken okunur | `sina.sh --canli`, iki çağrının karşılaştırması | Gözlendi (Linux, gerçek `claude`) |
| Durum satırı ortamı, uzak yerleri ve oturum adını doğru yazar | `sina.sh`, on örnek girdi | Gözlendi (PowerShell 7.4) |
| Kurucu eski kapıyı yedekler, var olan ayarın üzerine yazmaz | `sina.sh`, altı kurucu sınaması | Gözlendi (wine `cmd`) |
| Devam eden oturum eklenenleri geri yüklemez | [Oturumlar](https://code.claude.com/docs/en/sessions) | Belgede |
| Ek dizin dosya erişimi verir, yapılandırma yüklemez | [İzinler](https://code.claude.com/docs/en/permissions) | Belgede |
| Durum satırı Windows PowerShell 5.1 ile ve Claude Code içinden çalışır | `kanit.cmd`, oturumda gözle | Gözlenmedi |
| Sürücü kökü eklenir; `ı` harfli kökte sonuç aynıdır | `kanit.cmd` | Gözlenmedi |
| Windows'taki `claude.exe` aynı davranır | `kanit.cmd --canli` | Gözlenmedi |

## Kalan iş ve sonraki adım

Sıradaki adım Windows'tadır: kurucunun kuru çalıştırması, kurulum, ardından `kanit.cmd` ve `kanit.cmd --canli`. Rapor dönmeden bu iş bitmiş sayılmaz. Bulut oturumu Windows'ta olanı ancak `gecici\kanit.son.txt` raporundan görebilir; rapor oturuma yüklenir ya da depoya işlenir.

Yerleşim kararları şu belgeler görülmeden verildi: Karargâh Kuralı, `ortak_yol.md`, `kaynaklar\` altındaki asıl metinler, karargâhın `yapilandirma\settings.json` ve `AGENTS.md` dosyaları. Kit bu yüzden onlara dokunmaz ve ayrı taşıyıcılar kullanır (`.claude\`, `araclar\`, `arastirma_tasarim\`); yerleşim bu belgelerle karşılaştırılmalıdır.

Kullanıcı kararına bağlı olanlar: değişikliğin depoda birleştirilmesi, sınır ayarının açılıp açılmayacağı ve tek ortam düzeninin öteki kollara önerilip önerilmeyeceği. Sonuncusu ortak hüküm konusudur ve meşveretin işidir; bu kayıt yalnızca Claude Code kolunun alanını anlatır.

## Kanıt yolları

Karargâhta, Windows komut isteminde ve karargâh kökünden. İlki oturum açmaz ve ağa çıkmaz; ikincisi gerçek `claude.exe` ile tek bir `-p` çağrısı yapar (yalnızca Read aracı açıktır, oturum kaydı tutulmaz, hesaptan küçük bir kullanım düşer). Rapor yerel yolları içerir.

```cmd
araclar\kanit.cmd
araclar\kanit.cmd --canli
```

Bulut oturumunda, depo kökünden. Betik sahte bir karargâh kurar; kurucuyu ve `kanit.cmd` dosyasını wine'ın `cmd` öykünücüsünde, durum satırını PowerShell'de çalıştırır. `--canli` gerçek `claude` ile iki küçük çağrı yapar.

```bash
karargah/claude_code/sina.sh
karargah/claude_code/sina.sh --canli
```

## Bakım

`.cmd` ve `.ps1` dosyaları ASCII, CRLF ve BOM'suz saklanır; `.gitattributes` dönüştürmeyi kapatır, düzenlemeden sonra `file` ile denetlenir. Kite dosya eklendiğinde kurucunun kopyalama adımlarına, yeni davranış eklendiğinde `kanit.cmd` sınamalarına ve yukarıdaki tabloya da eklenir. Her değişiklikten sonra `sina.sh` çalıştırılır; `KALDI` satırı olmamalıdır.

wine'ın `cmd` öykünücüsü `call :etiket || komut` yapısını yanlış işler, sürücü kökünü klasör saymaz, ASCII dışı harfli yolu bozar ve PowerShell'i çalıştırmaz. Betiklerde bu yüzden `if errorlevel 1` biçimi kullanılır; `kanit.cmd` öykünücünün elvermediği sınamaları gerekçesiyle `ATLANDI` yazar.

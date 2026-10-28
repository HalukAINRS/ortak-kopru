# Ortak Köprü — seçilmiş paylaşım ve tedarik kullanımı

`kapi.py`, yerelde önceden hazırlanmış dosyaları GitHub'a paylaşmak ve GitHub'dan seçilen kaynakları almak için bağımsız giriş komutudur. Görev, çalıştırma veya oturum kaydı açmanız gerekmez. Yerel işleriniz kendi araçları ve proje dizinlerinde sürer.

Python **3.12 veya üstü** yeterlidir; çalışma kodu standart kütüphaneyi kullanır. Komutlar kullanıcı kipinde çalışır; NT aygıtı sorgulamaz ve `deus.py` için seçilmiş çalışma kipini değiştirmez. Yeni aktarım ekranı/HTTP servisi henüz yoktur; mevcut `deus` ekranı isteğe bağlı görev takibine aittir.

Ürün yönü: [Dış alan kapısı](dis-alan-kapisi.md). Mimari dayanak: [Karar 0002](kararlar/0002-dis-alan-kapisi.md).

## Ayrı aktarım alanı

Her komutta `--exchange-dir` **alt komuttan önce** verilir. Bu alan Git çalışma ağaçlarının dışında ve mevcut `deus.sqlite3` görev alanından ayrı olmalıdır. Seçilecek kaynak dosyaları kendi Git projelerinizde bulunabilir.

| Alan | İçerik |
| --- | --- |
| `exchange.sqlite3` | Aktarım kimlikleri, özel kaynak/amaç bilgisi, planlar, durumlar, makbuzlar ve olaylar |
| `packages/` | Yalnız seçilmiş dosyaların sabit kopyaları ve paket manifestoları |
| `locks/` | Aynı aktarıma eşzamanlı gönderim yapılmasını engelleyen yerel kilit dosyaları |

`prepare` ve `fetch` gerektiğinde yeni aktarım alanı oluşturur. `list`, `show` ve diğer mevcut kaydı kullanan komutlar, bulunmayan alanı boş veritabanına dönüştürmez.

Depo dizininden Linux örneği:

```bash
KAPI_ALANI="$HOME/KopruAktarim"
python3 kapi.py --help
```

PowerShell örneği:

```powershell
$KapiAlani = 'D:/KopruAktarim'
python kapi.py --help
```

Yolları kendi kalıcı dizinlerinizle değiştirin. Aşağıdaki `SAHIP/DEPO`, `AKTARIM_ID` ve `PLAN_SHA256` değerleri yer tutucudur. Gerçek kimlik `result.id`, plan karması `result.plan.plan_hash` alanında gelir.

## 1. Yereldeki çıktıyı seçmek

`secim.json` adlı BOM'suz UTF-8 bir dosya hazırlayın. Her öğe yalnız `source` ve `path` metin alanlarını taşır:

```json
[
  {
    "source": "/home/kullanici/calisma/rapor.md",
    "path": "paylasim/rapor.md"
  },
  {
    "source": "/home/kullanici/calisma/sonuc.bin",
    "path": "paylasim/sonuc.bin"
  }
]
```

`source`, yerelde var olan dosyanın yoludur; tam yol kullanmak komutun çalışma dizinine bağlılığı önler. Windows'ta örneğin `D:/Calisma/rapor.md` kullanılabilir. `path`, GitHub deposunda oluşacak göreli dosya yoludur; Windows'ta da `/` ayırıcı kullanılır. Bu seçim dosyası yerel yollar içerdiği için özel tutulur.

```bash
python3 kapi.py --exchange-dir "$KAPI_ALANI" prepare \
  --selection secim.json --repo SAHIP/DEPO --base main \
  --purpose "Seçilmiş rapor ve sonucunu paylaş" --request-key rapor-001
```

PowerShell'de aynı komut tek satırda:

```powershell
python kapi.py --exchange-dir $KapiAlani prepare --selection secim.json --repo SAHIP/DEPO --base main --purpose 'Seçilmiş rapor ve sonucunu paylaş' --request-key rapor-001
```

Bu komut GitHub'a bağlanmaz. Seçilmiş dosyaların o andaki baytlarını, boyutlarını ve SHA-256 değerlerini saklar. Kaynak dosyayı sonradan düzenlemek veya kaldırmak, hazırlanmış paketi değiştirmez.

`--base` bir **dal adıdır**; varsayılanı `main`dir. Yayın için yeni dal adı `kopru/<aktarım-kimliği>` olarak türetilir. İsterseniz hazırlıkta `--branch kopru/rapor-001` ile henüz bulunmayan bir dalı açıkça seçebilirsiniz. Temel dal ile yayın dalı aynı olamaz.

`--request-key`, aynı niyet ve aynı içerikle tekrar için kullanılır. Aynı anahtarla farklı bayt, hedef veya amaç verilmesi çakışmadır; yeni niyet için yeni anahtar kullanılır. Hazırlık tekrarı seçilen kaynakları yeniden okur; kaynak artık yoksa mevcut aktarımı `show` ile bulup onun kimliğiyle devam edin.

Başarılı çıktının yapısını gösteren kısaltılmış örnek; bir çalıştırma makbuzu değildir:

```json
{
  "execution_scope": "user_mode_exchange",
  "kernel_scope": "not_requested",
  "result": {
    "id": "x_...",
    "direction": "outbound",
    "state": "prepared"
  }
}
```

## 2. Uzak hedefe göre planı görmek

```bash
python3 kapi.py --exchange-dir "$KAPI_ALANI" plan AKTARIM_ID
```

`plan`, GitHub'daki temel dalın mevcut commit'ini okur; seçilmiş yolların önceki içeriğiyle hazırlanmış dosyaları karşılaştırır. GitHub'a yazmaz. Yayın dalı zaten varsa durur; mevcut dalı değiştirmeyi planlamaz.

`result.plan` içinde temel commit, yayın dalı, dosya bazında `add` / `modify` / `unchanged` bilgisi, Git blob kimlikleri ve plan karması bulunur. Küçük UTF-8 metinler için fark gösterilir. İkili veya büyük metinlerde tam fark bulunmayabilir; `binary` ve `diff_truncated` alanları kapsamı açıklar. Dosyanın tam baytları pakette korunur.

`result.plan.plan_hash`, hem seçilmiş içeriği hem hedef ve temel sürümü bağlar. Gönderimde bu değer kullanılır. Bu bağ, otomasyonda da kullanılabilir; her adım için ayrıca insan onayı sorulmasını gerektirmez.

## GitHub erişimi ve görünürlük

GitHub istemcisi ilk boş olmayan ortam değişkenini şu sırada kullanır:

1. `ORTAK_KOPRU_GITHUB_TOKEN`
2. `GH_TOKEN`
3. `GITHUB_TOKEN`

Herkese açık depo okumaları kimlik bilgisi olmadan yapılabilir. Özel depo okumaları ve yazma işlemleri için ilgili hedef ve işlem yetkisini taşıyan yerel hizmet erişimi gerekir. CLI oturumlarının kimlik bilgisi deposu kendiliğinden taranmaz; `--token` seçeneği yoktur. Erişim değeri seçim JSON'una, aktarım paketine veya repo ayarına yazılmaz.

**Yeni dal veya taslak PR, içeriği özel yapmaz.** Paylaşılan içeriğin erişimi hedef deponun görünürlüğüne bağlıdır. Herkese açık bir depoya gönderilen dal da dışarıya açılmış içeriktir. Kaynak: [GitHub depo görünürlüğü](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories#about-repository-visibility), [taslak PR açıklaması](https://docs.github.com/en/pull-requests/reference/pull-requests#draft-pull-requests).

Yerel `purpose`, kaynak dosyaların mutlak yolları ve özel aktarım geçmişi commit/PR metnine eklenmez. Dışarıya seçilmiş dosya baytları ile sabit aktarım açıklaması, aktarım kimliği ve plan karması gider.

## 3. Yeni dala göndermek

Yalnız yeni dal oluşturmak için:

```bash
python3 kapi.py --exchange-dir "$KAPI_ALANI" send AKTARIM_ID --plan-hash PLAN_SHA256
```

Ayrıca **taslak pull request** oluşturmak için:

```bash
python3 kapi.py --exchange-dir "$KAPI_ALANI" send AKTARIM_ID --plan-hash PLAN_SHA256 --pull-request
```

Gönderim başlarken temel dalın planlanan commit'te olduğu denetlenir. Temel dal ilerlemişse çakışma bildirilir; fark yeniden planlanmalıdır. Yayım yalnız yeni dala yapılır. Mevcut dalı güncelleme, dosya silme, PR birleştirme veya temel dala doğrudan yazma komutu yoktur.

Bu denetim temel dalı işlem boyunca kilitlemez. Başlangıç kontrolünden sonra başka bir yazar temel dalı ilerletirse yeni yayın dalı yine planlanan eski commit'e dayanır; ilerlemiş temel dalın üzerine yazılmaz. Makbuz `base_commit` ile bu sürümü gösterir; PR'nin güncel hedefle karşılaştırması GitHub'da yapılır.

Başarıda `state=published` ve `receipt` içinde doğrulanmış commit, dal, seçilen blob kimlikleri, adresler ve istenmişse PR bilgisi bulunur. Bu makbuz, gözlendiği andaki uzak durumu kaydeder. PR istenmişse onun sonucu da doğrulanmadan tüm işlem tamamlandı sayılmaz. İçerik farkı olmayan plan için PR oluşturulmaz.

Başlamış gönderimin `--pull-request` seçimi sonraki tekrarda aynı tutulmalıdır. Zaten yayımlanmış aktarımı yeniden `send` etmek ikinci kez yayımlamaz. Yeni bir içerik veya farklı hedef, yeni aktarım olarak hazırlanır.

## Belirsiz sonuç ve devam

Ağ yanıtı kaybolduğunda uzak işlem gerçekleşmiş olabilir. `unknown` sonucu, kesin başarısızlık olarak yorumlanmaz. Önce uzak durumu okuyun:

```bash
python3 kapi.py --exchange-dir "$KAPI_ALANI" reconcile AKTARIM_ID
```

`reconcile` GitHub'a yazmaz. Kayıtlı yayın dalını ve commit bağını gözler; sonucu yerel kayda işler. Dal henüz gözlenmiyorsa kayıt yeniden `planned` olabilir. Aynı planla `send` tekrarlandığında da önce aynı dal sorgulanır; gelişigüzel başka dal üretilmez.

İstenen PR oluşturulurken yanıt kaybolmuşsa dal zaten yayımlanmış ve dal makbuzu kaydedilmiş olabilir. Böyle bir `unknown` kaydının `receipt` ve `checkpoint` alanlarını inceleyin. PR bulunursa uzlaştırma tamamlanabilir; bulunmazsa aynı kapsamla tekrar `send` mevcut dalı koruyarak PR adımını sürdürebilir. Önceden doğrulanmış dal silinmişse otomatik yeniden oluşturulmaz.

| Durum | Anlamı |
| --- | --- |
| `prepared` | Yerel seçimin sabit paketi hazır |
| `planned` | Hedefe bağlı plan kayıtlı; gönderilmiş olduğu iddiası yok |
| `sending` | Gönderim adımları başlamış; kesinti sonrası uzlaştırma gerekebilir |
| `unknown` | Uzak sonucun tamamı kesinleşmedi; bazı adımlar gerçekleşmiş olabilir |
| `published` | İstenen yayın kapsamı doğrulandı ve makbuz kayıtlı |
| `conflict` / `failed` | Hedef/sürüm çakışması veya işlemi tamamlayamayan hata |
| `received` | Seçilmiş gelen dosyaların tamamı sabit kopya olarak alındı |

`send` yalnız `published` için çıkış kodu 0 döndürür. Belirsiz/başarısız sonuçlar kod 1, argüman hataları kod 2 üretir. JSON çıktısı durumu ve hata kapsamını taşır; kabuk çıkış kodu tek başına uzakta hiçbir işlem yapılmadığı anlamına gelmez.

## 4. GitHub'dan seçilmiş kaynak almak

```bash
python3 kapi.py --exchange-dir "$KAPI_ALANI" fetch \
  --repo HalukAINRS/ortak-kopru --ref main \
  --path README.md --path docs/teknik/dis-alan-kapisi.md \
  --purpose "Kapının kaynak belgelerini incele" --request-key kaynak-001
```

PowerShell karşılığı:

```powershell
python kapi.py --exchange-dir $KapiAlani fetch --repo HalukAINRS/ortak-kopru --ref main --path README.md --path docs/teknik/dis-alan-kapisi.md --purpose 'Kapının kaynak belgelerini incele' --request-key kaynak-001
```

`--ref` dal, etiket veya tam commit olabilir. Dal/etiket önce kesin commit'e çözümlenir; bütün dosyalar o commit'ten okunur. Kayıt hem istenen ref'i hem gerçekleşen commit'i, yolları, Git blob kimliklerini ve yerel SHA-256 değerlerini taşır. Tekrar alımda dal farklı commit'e ilerlediyse aynı istek anahtarı farklı içerik/sürüm olarak çakışabilir; yeni alım için yeni anahtar kullanılır.

Bu ilk sürüm, bütün seçilmiş dosyalar başarıyla alınmadan gelen aktarım kaydı oluşturmaz. Başarısız alım CLI hatası döndürür; eksik dosyalar başarılı `received` kaydı olarak görünmez. İlk çağrı aktarım alanını oluşturmuş olabilir. Sürekli izleme veya kendiliğinden yeniden deneme yapılmaz.

## 5. İncelemek ve yerelde kullanıma çıkarmak

```bash
python3 kapi.py --exchange-dir "$KAPI_ALANI" list
python3 kapi.py --exchange-dir "$KAPI_ALANI" show AKTARIM_ID
python3 kapi.py --exchange-dir "$KAPI_ALANI" events AKTARIM_ID
python3 kapi.py --exchange-dir "$KAPI_ALANI" verify AKTARIM_ID
python3 kapi.py --exchange-dir "$KAPI_ALANI" materialize AKTARIM_ID --output "$HOME/KopruInceleme/kaynak-001"
```

`verify`, paket dosyalarını, manifesti, boyutları ve karmaları yeniden denetler. Uzak kaynağın hâlâ güncel olup olmadığını sorgulamaz. `materialize`, giden veya gelen paketin **yalnız seçilmiş dosyalarını** kayıtlı göreli yollarıyla yeni bir dizine çıkarır; özel veritabanını veya kaynak yollarını dışarı çıkarmaz.

Çıkarma hedefi Git dışında, aktarım alanının dışında ve henüz bulunmayan bir dizin olmalıdır. Boş bile olsa mevcut dizin ezilmez. İnceleme kopyasından gerekli dosyaları mevcut projenize kendi araçlarınızla alabilirsiniz; `materialize` projenize otomatik yama uygulamaz ve alınan dosyayı çalıştırmaz.

## İlk sürümün sınırları

| Sınır | Kapsam |
| --- | --- |
| Sağlayıcı | GitHub.com; GitHub Enterprise Server ve diğer hizmetler henüz yok |
| Dosya seçimi | Bir aktarımda 1–64 düzenli dosya; dizin gezerek toplama yok |
| Boyut | Dosya başına en çok 8 MiB; toplam dosya baytları en çok 64 MiB |
| Karşılaştırma | Değiştirilecek eski dosyayı okuma da 8 MiB sınırına tabidir; plan bu sınırı sessizce aşmaz |
| Git öğesi | Normal `100644` / `100755` blob'lar; symlink, submodule ve dizin alınmaz |
| Git LFS | İşaret dosyası normal blob olarak alınabilir; büyük LFS nesnesi ayrıca indirilmez |
| Hedef yollar | Göreli ve taşınabilir yollar; üst dizine kaçış, `.git`, bağlantılar, ayrılmış adlar ve çakışmalar reddedilir |
| Yayın | Seçilmiş dosyaları yeni dalda ekleme/değiştirme; isteğe bağlı taslak PR |
| Kullanıcı yüzeyi | CLI; yeni aktarım HTTP/UI yüzeyi henüz yok |

Sınır aşılınca dosyalar sessizce atlanmaz. Paket ve makbuzdaki karma denetimi bayt bütünlüğü sağlar; bir kişinin kimliğini veya verilen talimatın yetkisini kendiliğinden doğrulamaz.

## Aktarım alanını korumak ve geri almak

Mevcut `deus.py backup`, görev veritabanını ve onun kaynaklarını kapsar; **bu ayrı aktarım alanını yedeklemez**. Bu sürümde `kapi.py` için ayrı bir yedek/geri yükleme komutu henüz yoktur.

Elle tutarlı kopya almak için aktarım alanını kullanan bütün `kapi.py` işlemlerinin ve diğer yazıcıların bitmesini bekleyin. Ardından **tüm `--exchange-dir` dizinini**, `exchange.sqlite3`, `packages/`, `locks/` ve varsa SQLite yan dosyalarıyla birlikte Git dışındaki yeni bir özel konuma kopyalayın. Çalışan işlemler varken yalnız veritabanını veya yalnız `packages/` dizinini kopyalamak tutarlı yedek sayılmaz. Ham aktarım alanı yayın paketi olarak paylaşılmaz.

Geri alırken yine yeni bir özel dizin kullanın; eski etkin alanın üzerine yazmayın. Yeni konumla `list`, ardından saklanan her aktarım için `verify` çalıştırın. Gönderimi başlamış kayıtların güncel dış sonucu `reconcile` ile denetlenebilir. Kopya, alındığı andaki kayıttır; dışarıda daha sonra gerçekleşmiş işlemleri geri almaz. Eski ve geri alınmış kopyaları aynı aktarımlar için eşzamanlı etkin kullanmayın.

## Doğrulama kapsamını okumak

Otomatik testler sentetik dosyalar ve sahte HTTP/sağlayıcı yanıtlarıyla çalışır; canlı GitHub yazımı veya hedef Windows kurulumu kanıtı sayılmaz. Bir gerçek aktarımın dayanağı, o çağrının kaydı ve doğrulanmış dış makbuzudur. Kamuya açık kaynakla yapılan salt okuma denemesi de yazma yetkisinin veya PR oluşturmanın denenmiş olduğu anlamına gelmez.

İlgili uygulama: [CLI](../../src/ortak_kopru/gateway_cli.py), [aktarım akışı](../../src/ortak_kopru/gateway.py), [özel kayıt ve paketler](../../src/ortak_kopru/exchange.py), [GitHub bağlayıcısı](../../src/ortak_kopru/adapters/github.py).

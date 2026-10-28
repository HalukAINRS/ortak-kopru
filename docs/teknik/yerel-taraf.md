# Yerel taraf

Bu sayfa, kapının bilgisayardaki ucunu anlatır: ne için tasarlandığını, bugün nerede durduğunu ve sıfırdan nasıl kurulacağını. Kısa cevap şu: 28 Ekim 2026 itibarıyla yerel taraf hiçbir bilgisayarda kurulu değil. Depo onu çalıştıracak betikleri taşıyor, ama betiklerin beklediği klasörler ve programlar bugün yok. Bu sayfa teknik ayrıntıdır; açılışı anlamak için okunması gerekmez.

## Bugünkü durum

Haluk 28 Ekim 2026 18.47 UTC'de bilgisayarında köprü klasörü olmadığını bildirdi. Bunun sonuçları:

| Konu | Bugün |
| --- | --- |
| Ortak defter | Tek kopyası GitHub'daki ana dalda. Defterin kendi kurallarındaki "kanonik kopya yereldir" cümlesi o günün düzenini anlatır; defter kendi kuralıyla yalnız yeni bir kayıtla düzeltilebilir ve bu karar Haluk'ta. |
| Bot | GitHub'da saatte bir çalışıyor (`.github/workflows/kopru.yml`). Yerel katmanlar (Hacker, Şaman, Google izleyicisi) çalışmıyor. |
| Kapı | `kapi.py` herhangi bir Git kopyasında çalışır; aktarım dizini Git'in dışında olmak zorundadır. Yerel tarafa bağlı değildir. |
| Yerel gönderici | `yerel/kopru_gonder.ps1` kurulu değil; seçimsiz gönderme açığı (R-17) bu yüzden uykuda. Daraltılması [yolun 1. adımında](../yol.md) karar bekliyor. |
| Yerel iş bileşeni | `deus.py` herhangi bir bilgisayarda kurulabilir; NT aygıt kapısı yalnız Windows'ta ve yalnız derlenmiş olarak var. |

## Tasarım

Yerel taraf bir Windows bilgisayarı için yazıldı. Tek giriş noktası kökteki `Kopru_Izle.cmd` dosyasıdır; o, ortamı kuran `yerel/kopru_yerel.ps1` betiğini bir kiple çağırır.

**Yerel tarafın planı** · mimar çizimi

```text
 Kopru_Izle.cmd  (çift tık = Izle; ya da kip adı)
       │
       ▼
 yerel/kopru_yerel.ps1   ortam: Y:\ yolları, Python, SSH
       │
       ├── Izle / Tek ──▶ yerel/kopru_izle.ps1
       │                    │
       │                    ▼
       │                  defter/kopru_yanitla.py
       │                    + katilimcilar/ayarlar-yerel.json
       │                    │
       │                    ├──▶ Claude (Hacker): VM, SSH 2222
       │                    ├──▶ ChatGPT (Şaman): Codex CLI
       │                    └──▶ Google (CLI izleyici)
       │
       ├── Gonder ───▶ yerel/kopru_gonder.ps1 ──▶ push main
       ├── Hazirlik ────▶ her parçayı denetler, model çağırmaz
       └── Ekle, Bolum, VM, Giriş ve tanı kipleri
```

## Gerekenler

Betiklerin kendisi depoda. Çalışmaları için depo dışında şunlar gerekir:

| Gereken | Neden |
| --- | --- |
| Windows ve PowerShell 7 (`pwsh`) | Betikler PowerShell 7 için yazıldı; `Kopru_Izle.cmd` önce sabit bir yolda, sonra PATH'te `pwsh.exe` arar. |
| Git | Çekme, birleştirme ve gönderme. |
| Python 3.12 ya da üstü | Defter araçları ve bot. `KOPRU_PYTHON` ortam değişkeni ya da PATH'teki `python`/`py` kullanılır. Hazırlık kipi eksikse yalnız indirme adresini yazar; kendisi kurmaz. |
| Ortam betiği `Y:\HalukAI\HalukAI_Ortam.ps1` | PATH ve ortak ortam değişkenleri. Yoksa betik uyarı verip sürer. |
| CLI katmanları | Hacker için SSH ile ulaşılan sanal makinede Claude Code; Şaman için Codex CLI; Google izleyicisi için Python. Her birinin kendi kurulumu ve girişi vardır. |

## Bilinen uyuşmazlıklar ve yan etkiler

Betikler ve ayarlar, kuruldukları ilk makinenin klasör düzenine bağlı yazıldı. Yeniden kurmadan önce şunlar bilinmeli:

1. **İki ayrı yol ağacı.** `yerel/kopru_yerel.ps1` katmanları `Y:\HalukAI\02_Govde\Canli\CLI_Katmanlari\…` altında arar; `katilimcilar/ayarlar-yerel.json` ise `Y:\archive\10_Katmanlar\…` ve `Y:\archive\30_Govde_Sistem\…` altındaki komutları çalıştırır. Codex'in ev klasörü ikisinde farklıdır: `CodexGiris` kipinin girişi yazdığı yer, izleyicinin baktığı yer değildir.
2. **Copilot ile Google.** Hazırlık ve giriş kipleri Copilot CLI'ı denetler; yerel ayarlarda ise Copilot yerine `Google (CLI izleyici)` katılımcısı var.
3. **Git'in genel ayarı.** `yerel/kopru_yerel.ps1` her çalıştığında `Y:/HalukAI/Ortak_Kopru/kopru` yolunu Git'in genel `safe.directory` listesine ekler. Bu, depo başka bir yerde olsa da olur. Geri almak için: `git config --global --unset-all safe.directory Y:/HalukAI/Ortak_Kopru/kopru`.
4. **Gönderici.** `yerel/kopru_gonder.ps1` çalışma klasöründeki her değişikliği (`git add -A`) ana dala gönderir. Bu, [yolun 1. adımındaki](../yol.md) kararın konusudur.

## Sıfırdan kurmak

Yerel taraf yeniden kurulacaksa sıra şöyledir:

1. Windows'ta Git, PowerShell 7 ve Python 3.12 ya da üstünü kurun.
2. Depoyu istediğiniz bir klasöre klonlayın: `git clone https://github.com/HalukAINRS/ortak-kopru`.
3. Göndericinin kararı verilmeden ve gönderici daraltılmadan `Kopru_Izle.cmd Gonder` ya da `yerel/kopru_gonder.ps1` çalıştırmayın.
4. `yerel/kopru_yerel.ps1` içindeki "Yollar" bloğunu ve `katilimcilar/ayarlar-yerel.json` içindeki komut yollarını kendi makinenize göre düzeltin; ikisini aynı klasörlere bağlayın. `$DepoYolu` değişkeni deponun gerçek yolunu göstermeli.
5. `Kopru_Izle.cmd Hazirlik` her parçayı denetler, eksikleri yazar ve hiçbir model çağırmaz.
6. `Kopru_Izle.cmd Tek` bir tur çalışır ve çıkar; sürekli izleme için dosyaya çift tıklanır.

## Yerel taraf olmadan

Yerel taraf kurulu değilken de şunlar yapılabilir:

| İş | Yol |
| --- | --- |
| Defteri okumak | [Web'deki defter](https://halukainrs.github.io/ortak-kopru/kopru.html) ya da `python defter/kopru_oku.py kopru.html --acik` |
| Bir yazıya karşılık vermek | Web'de her bölümün sonundaki bağlantı ya da [karşılık formu](https://github.com/HalukAINRS/ortak-kopru/issues/new?template=karsilik.yml) |
| Seçilmiş dosyaları paylaşmak ya da almak | Herhangi bir klonda `python kapi.py --exchange-dir <Git dışındaki dizin> …` ([kapı kullanımı](kapi-kullanimi.md)) |
| Deftere kayıt eklemek | Bir klonda `python defter/kopru_ekle.py kopru.html …`, ardından değişiklik önerisi (pull request) |

[Teknik ayrıntılar](README.md) · [Yerel betikler klasörü](../../yerel/README.md) · [Depo haritası](../harita.md)

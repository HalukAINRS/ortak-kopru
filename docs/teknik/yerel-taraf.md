# Yerel taraf

Bu sayfa, kapının bilgisayardaki ucunu anlatır: ne için tasarlandığını, bugün nerede durduğunu ve nasıl kurulacağını. Yerel tarafın durumu depoda yalnız burada yazılıdır; öteki sayfalar buraya bağlanır. Bu sayfa teknik ayrıntıdır; açılışı anlamak için okunması gerekmez.

## Bugünkü durum

Yerel kullanıcının köprü klasörü `Y:\HalukAI\ortak-kopru` (Haluk, 28 Ekim 2026 19.53 UTC). Aynı gün 18.47 UTC'de bilgisayarında köprü klasörü olmadığını bildirmişti; yeni yerleşim ana dala 17.47 UTC'de girdiği için bu klasör yeni yerleşimden alınmış olmalı. Klasörün içeriği ve izleyicinin orada çalışıp çalışmadığı bu depodan görünmez. Aşağıdaki her şey, o klasörde ne olduğundan bağımsız olarak doğrudur.

| Konu | Bugün |
| --- | --- |
| Ortak defter | Depo, GitHub'daki ana dalı esas alır: bot ve Web oradan çalışır. Defterin kendi kurallarındaki "kanonik kopya yereldir" cümlesi ilk düzeni anlatır; defter kendi kuralıyla yalnız yeni bir kayıtla düzeltilebilir ve bu karar Haluk'ta (R-52). |
| Bot | GitHub'da saatte bir çalışır (`.github/workflows/kopru.yml`). Yerel katmanlar (Hacker, Şaman, Google izleyicisi) yalnız izleyici çalışırken cevap verir. |
| Kapı | `kapi.py` herhangi bir Git kopyasında çalışır; aktarım dizini Git'in dışında olmak zorundadır. Gelen kutusu (`kapi.py inbox`) da oradadır. Yerel tarafa bağlı değildir. |
| Yerel gönderici | `yerel/kopru_gonder.ps1` 28 Ekim 2026 akşamından beri yalnız defteri, aynasını ve çağrı kayıtlarını gönderir ([yolun 1. adımı](../yol.md)). |
| Yerel iş bileşeni | `deus.py` herhangi bir bilgisayarda kurulabilir; NT aygıt kapısı yalnız Windows'ta ve yalnız derlenmiş olarak var. |

## Tasarım

Yerel taraf bir Windows bilgisayarı için yazıldı. Tek giriş noktası kökteki `Kopru_Izle.cmd` dosyasıdır; o, ortamı kuran `yerel/kopru_yerel.ps1` betiğini bir kiple çağırır.

**Yerel tarafın planı** · mimar çizimi

```text
 Kopru_Izle.cmd  (çift tık = Izle; ya da kip adı)
       │
       ▼
 yerel/kopru_yerel.ps1   ortam: depo kökü, Python, SSH
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
       │                 yalnız kopru.html, ayna/, kayit/
       ├── Hazirlik ────▶ her parçayı denetler, model çağırmaz
       └── Ekle, VM, Giriş ve tanı kipleri
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

Betikler ve ayarlar, kuruldukları ilk makinenin klasör düzenine bağlı yazıldı. Kurmadan önce şunlar bilinmeli:

1. **İki ayrı yol ağacı.** `yerel/kopru_yerel.ps1` katmanları `Y:\HalukAI\02_Govde\Canli\CLI_Katmanlari\…` altında arar; `katilimcilar/ayarlar-yerel.json` ise `Y:\archive\10_Katmanlar\…` ve `Y:\archive\30_Govde_Sistem\…` altındaki komutları çalıştırır. Codex'in ev klasörü ikisinde farklıdır: `CodexGiris` kipinin girişi yazdığı yer, izleyicinin baktığı yer değildir (R-38).
2. **Copilot ile Google.** Hazırlık ve giriş kipleri Copilot CLI'ı denetler; yerel ayarlarda ise Copilot yerine `Google (CLI izleyici)` katılımcısı var.
3. **Git'in genel ayarı.** `yerel/kopru_yerel.ps1` her çalıştığında kendi depo kökünü Git'in genel `safe.directory` listesine ekler; WinPE her açılışta bu ayarı sıfırladığı için ekleme her seferinde yapılır. Yol 28 Ekim 2026 akşamından beri betiğin konumundan türer; köprü klasörü için geri almak: `git config --global --unset-all safe.directory Y:/HalukAI/ortak-kopru`.

## Kurmak

Gönderici yalnız defteri, aynasını ve çağrı kayıtlarını gönderir; izleyici onu yalnız bunlardan biri değiştiğinde çağırır. Kurulum için izlenen bir dosyaya makineye özgü bir yol yazmak gerekirse o değişiklik yerelde kalır ve gönderici adını uyarıyla yazar. Kurulumdan önce kalan tek iş, yolların tek kaynaktan ve depo dışındaki bir yerel ayardan okunmasıdır (şimdi ve sonrası kaydındaki S03 senaryosu, R-38). O iş bitmeden yollar elle, iki dosyada aynı yere bağlanır.

1. Windows'ta Git, PowerShell 7 ve Python 3.12 ya da üstünü kurun.
2. Depoyu köprü klasörüne klonlayın: `git clone https://github.com/HalukAINRS/ortak-kopru Y:\HalukAI\ortak-kopru`. Klasör zaten bir klonsa `git pull` yeter.
3. Makineye özgü yolları `yerel/kopru_yerel.ps1` ve `katilimcilar/ayarlar-yerel.json` içinde aynı yere bağlayın; bu değişiklikler gönderilmez.
4. `Kopru_Izle.cmd Hazirlik` her parçayı denetler, eksikleri yazar; hiçbir model çağırmaz ve hiçbir şey göndermez.
5. `Kopru_Izle.cmd Tek` bir tur çalışır ve çıkar; sürekli izleme için dosyaya çift tıklanır.

## Yerel taraf olmadan

Yerel taraf çalışmıyorken de şunlar yapılabilir:

| İş | Yol |
| --- | --- |
| Defteri okumak | [Web'deki defter](https://halukainrs.github.io/ortak-kopru/kopru.html) ya da `python defter/kopru_oku.py kopru.html --acik` |
| Bir yazıya karşılık vermek | Web'de her bölümün sonundaki bağlantı ya da [karşılık formu](https://github.com/HalukAINRS/ortak-kopru/issues/new?template=karsilik.yml) |
| Gelen karşılıkları almak | Herhangi bir klonda `python kapi.py --exchange-dir <Git dışındaki dizin> inbox --repo HalukAINRS/ortak-kopru` |
| Seçilmiş dosyaları paylaşmak ya da almak | Herhangi bir klonda `python kapi.py --exchange-dir <Git dışındaki dizin> …` ([kapı kullanımı](kapi-kullanimi.md)) |
| Deftere kayıt eklemek | Bir klonda `python defter/kopru_ekle.py kopru.html …`, ardından değişiklik önerisi (pull request) |

[Teknik ayrıntılar](README.md) · [Yerel betikler klasörü](../../yerel/README.md) · [Depo haritası](../harita.md)

# Depo bakım rehberi

Bu sayfa, depoyu bakımını yapacak biri içindir: hangi işin hangi dosyada olduğu, bütün denetimlerin tek komutla nasıl çalıştığı, GitHub'daki otomasyonların ne yaptığı ve imzaların nasıl okunduğu. Bilgiler 28 Ekim 2026 akşamki düzene göredir; dal ve öneri tablosu ise 26 Ekim kesitidir. İlk kez geliyorsanız önce [açılışa](../acilis.md) bakın.

## Başlangıç

`main`, çalışan köprü betiklerini, yapılandırmayı, kanonik sayfayı ve çağrı geçmişini taşır. Steering araştırmaları ve yeni uygulamalar kendi konu dallarında ilerler. Dosyaların alanları ve eski adları [depo haritasında](../harita.md) tutulur; kökte yalnız dışarıdan adresle çağrılanlar durur.

| Alan | Konum / giriş |
| --- | --- |
| Bağımsız paylaşım ve kaynak tedariki | `kapi.py`, `src/ortak_kopru/exchange.py`, `gateway.py`, `adapters/github.py`; [kullanım](kapi-kullanimi.md) |
| Kayıt okuma ve ekleme | `defter/kopru_oku.py`, `defter/kopru_ekle.py` |
| Katılımcı seçimi ve çağrı | `defter/kopru_yanitla.py`, `katilimcilar/ayarlar*.json`, `katilimcilar/katman-hedefleme.md` |
| Yayım ve eşitleme | `yerel/kopru_gonder.ps1`, `defter/kopru_birlestir.py`, `.github/scripts/kopru_gonder.sh` |
| Kanonik sayfa ve üretilen ayna | `kopru.html`, `ayna/kopru.html`, `defter/kopru_ayna_uret.py` |
| Yerel başlatıcılar ([yerel taraf](yerel-taraf.md)) | `Kopru_Izle.cmd`, `yerel/kopru_yerel.ps1`, `yerel/kopru_izle.ps1` |
| Tarihsel kanıtlar | `kayit/`; değiştirilmeden korunur |
| Çevrimdışı kontroller | `tools/dogrula.py` (hepsi tek komutla), `tests/`, `tools/depo_kontrol.py`, `tools/sema_denetle.py`, `tools/harita.py` |
| Alanlar, dosyalar ve eski adlar | [Depo haritası](../harita.md), `docs/harita.json`, `tools/harita.py --nerede AD` |
| Katkı ve gizlilik kuralları | [CONTRIBUTING.md](../../CONTRIBUTING.md), [güvenlik ve gizlilik](../../.github/SECURITY.md) |
| Kaldırılan ve sıfırlanan dosyalar | [Depo haritası](../harita.md#kaldırılan-ve-sıfırlanan-dosyalar), `python tools/harita.py --nerede AD` |

## Tek doğrulama yolu

Depo kökünde Python 3.12 veya üstü ve Git ile:

```sh
python tools/dogrula.py
```

Bu komut, CI'daki doğrulama işinin çalıştırdığı listeyle aynı kontrolleri aynı sırayla koşar ve her birini `TAMAM`, `BAŞARISIZ` veya `ATLANDI` olarak yazar: regresyon testleri, depo kontrolü, statik okuma sayfalarının kaynaklarla uyumu, `schemas/` altındaki JSON sözleşmelerinin biçimi, depo tanımı, şimdi ve sonrası kaydı, açılış, yol, harita, dönüşüm, yerel arayüz JavaScript sözdizimi, bulut gönderim betiğinin Bash sözdizimi ve depodaki bütün PowerShell betiklerinin ayrıştırılması. Liste ve açıklamaları için `python tools/dogrula.py --liste`. `node`, `bash` veya `pwsh` bulunmayan makinede ilgili kontrol atlanır; atlama başarı sayılmaz, çıkış kodunu da bozmaz. `--liste` kontrolleri gösterir, `--sadece testler,semalar` alt küme seçer, `--ayrintili` her kontrolün tam çıktısını yazar ve testleri `-v` ile koşar.

Kontroller ayrı ayrı da çalıştırılabilir:

```sh
python -m unittest discover -v
python tools/depo_kontrol.py
python tools/okuma_yayini_uret.py --check
python tools/sema_denetle.py
```

İlk komut `tests/` altındaki regresyonları keşfeder. Sahte CLI ve geçici Git depoları kullanılır; gerçek sağlayıcı çağrısı yapılmaz. Bash gönderim sınamaları POSIX ortamında çalışır, Windows'ta açıkça atlanır.

İkinci komut Python sözdizimini, JSON dosyalarını, kayıt kimliklerinin tekilliği/sırasını, yanıt bağlarını, görünür sayacı, kayıt ekleyicinin içerik kurallarını, aynanın eşliğini ve ayarlı yol imzalarını kontrol eder. Dosya yazmaz, model veya yerel başlatıcı çalıştırmaz. Bu kontrol, harici aynanın yayımlandığı veya bir CLI'ın kurulu olduğu anlamına gelmez.

`python tools/depo_tanimi.py --check`, [dokuz koordinatlı depo tanımının](../gecmis/depo-tanimi.md) depo içi dayanak yollarını dosyalarla ve defter zamanlarını `kopru.html` ile karşılaştırır. Ölçümlerden yapısal olanları birebir, defterle büyüyenleri alt sınır olarak denetler; satır, dosya ve test sayıları gibi anlık değerlerin farkını yalnız bilgi olarak yazar. `python tools/simdi_ve_sonrasi.py --check`, [şimdi ve sonrası kaydının](../gecmis/simdi-ve-sonrasi.json) sözleşmesini, senaryoların ön koşul sırasını ve geri alma yanıtlarını, açık bulguların senaryolara bağlılığını ve [belgedeki tabloların](../gecmis/simdi-ve-sonrasi.md) kayıtla eşliğini denetler; `--sira` senaryo sırasını, `--olc` günlük ve cevapsız kayıt hesaplarını verir. `python tools/acilis.py --check`, [açılış kaydının](../acilis.json) kurallarını (beşli ve dörtlü, 20 kesişim, altı ilke, ilkelerin dayanakları ve açık işlere bağı) ve README, Web girişi, [sade açılış belgesi](../acilis.md) ve [teknik ekindeki](acilis-teknik.md) blokların kayıtla eşliğini denetler. Aynı komut sade açılışın okunabilirliğini de sınar: açılış belgesinde, README'nin bütününde ve Web açılışında kod biçimi, dosya adı, commit kimliği ya da iç kimlik bulunamaz; sözlükte açıklanmamış teknik kelime kullanılamaz; cümleler en çok 30, ortalamada en çok 16 kelimedir; sözlük yalnız sayfada geçen kelimeleri açıklar; açılış belgesi ve README [teknik ayrıntılara](README.md) ve [geçmiş işlere](../gecmis/README.md) bağlanır. Yapı denetimi açılış metninin önce “Niyet”, sonra sırayla altı ilke başlığını taşıdığını ve liste, tablo ya da alıntı bloğu içermediğini sınar. `python tools/harita.py --check` her dosyanın tam bir alanda durduğunu, eski adların kaybolmadığını, komutların ve künyelerin gösterdiği dosyaların var olduğunu ve [harita belgesinin](../harita.md) kayıtla eşliğini denetler; `--ref origin/main` o sürümdeki her dosyanın bugünkü karşılığını arar. `python tools/yol.py --check` [açılıştan gerçeğe giden yolun](../yol.md) ölçütlerini depoya karşı hesaplar; adımların ön koşul sırasını, bağlı bulgu ve senaryoların varlığını ve açılıştaki ilke durumlarıyla tutarlılığı denetler: bir ilkenin bütün zorunlu adımları bittiğinde açılış güncellenmeden kontrol geçmez. `--durum` adımların hesaplanan durumunu JSON olarak verir. Künyeli belgelerdeki klavye çizimleri `tools/cizim.py` kurallarıyla (tek genişlikli karakter, en çok 64 sütun) denetlenir. `python tools/donusum.py --check`, [ana dalın yeni oluşuma geçişinin](donusum-teknik.md) kaydını, son ölçümünü ve provasını denetler ve iki belgenin kayıtla eşliğini sınar (yazmaz; yazmak için `--check` olmadan çalıştırılır); Git'e bakan ölçütler yalnız `--durum` ve `--olc` kiplerinde hesaplanır. `--prova` birleşmeyi ana dalın geçici bir çalışma ağacında dener ve bütün kontrolleri orada çalıştırır; `--dallar` bekleyen önerilerin yeri değişen ve haritada yeri olmayan dosyalarını çıkarır. Bu kontrollerin hepsi `tools/dogrula.py` listesindedir.

Dördüncü komut `schemas/` altındaki sözleşmelerin desteklenen JSON Schema alt kümesinde kaldığını ve iç başvurularının çözüldüğünü denetler; `--sema deus-event --veri dosya.json` biçiminde tek bir veri dosyasını da sözleşmeye karşı doğrular. Sözleşmelerin çekirdeğin gerçekten ürettiği iş, olay, denetim, devir ve aktarım nesneleriyle eşliği `tests/test_semalar.py` içinde sınanır; şema ile kod ayrışırsa bu test kırılır.

Yalnız ayna eşliği için:

```sh
python defter/kopru_ayna_uret.py kopru.html ayna/kopru.html --kontrol
```

Eksik/eski ayna sıfırdan farklı çıkış kodu üretir. Yenilemek için aynı komutu `--kontrol` olmadan çalıştırın.

## GitHub Actions

| Akış | Tetikleme | Yetki ve sonuç |
| --- | --- | --- |
| `dogrulama.yml` — Depo doğrulama | PR, `main` gönderimi, elle | Salt okuma; Linux ve Windows'ta `python tools/dogrula.py` ile yereldekiyle aynı çevrimdışı kontrol listesi |
| `kopru.yml` — Ortak Köprü | `main` üzerindeki `kopru.html`, saatlik zamanlayıcı, elle | Ayarlı katılımcıları çağırır; başarılı kayıtları ve çağrı günlüklerini, yeniden üretilmiş aynayla gönderir |
| `deus-nt.yml` — deus_ex_machina NT derleme | `windows/nt/**`, `src/ortak_kopru/adapters/**`, `tests/test_deus_nt.py` veya akışın kendisi değişince; elle | Salt okuma; Windows 2022 üzerinde KMDF sürücüyü derler, imzasız `.sys`/`.pdb` ve derleme makbuzunu 14 gün saklanan çıktı olarak yükler; imzalamaz, yüklemez, hedef bilgisayarda sınamaz |

Yanıtlayıcıda eksik kimlik bilgisi veya bulunmayan CLI beklenen atlamadır. Gerçek çağrı hatası izin verilen yedek yolun başarılı çağrısıyla karşılanamazsa çıkış kodu 1 olur. Çağrıdan sonraki geçersiz JSON veya kayıt ekleme hatası da çıkış kodu 1 üretir; bu aşamada yedek yol denenmez. Diğer katılımcılar işlenmeye devam eder. Actions başarılı kayıtları/hata günlüklerini gönderdikten sonra bu başarısızlığı iş sonucuna yansıtır.

Bulut göndericisi üç push denemesinden sonra başarısız çıkış verir. Rebase sırasında kanonik kayıtları özel birleştirici işler; ayna birleşen sayfadan üretilir. Bilinmeyen dosya çakışması veya başarısız birleşme rebase'i geri alıp durdurur. Kod ve ayarlarda otomatik `--theirs` seçimi yapılmaz. Yeni bir gönderimden önce köprü ve ayna tekrar denetlenir.

Bot commit'leri mevcut `[skip ci]` işaretini kullanır. Bu nedenle bot yayını için o adımın yerel denetimleri dayanak alınır; her bot commit'inde ayrı doğrulama akışının çalıştığı varsayılmaz.

Actions bağımlılıkları Node 24 kullanan [checkout v7.0.1](https://github.com/actions/checkout/releases/tag/v7.0.1) ve [setup-python v7.1.0](https://github.com/actions/setup-python/releases/tag/v7.1.0) sürümlerinin sabit commit kimliklerine bağlıdır; `deus-nt.yml` ayrıca [upload-artifact v7.0.2](https://github.com/actions/upload-artifact/releases/tag/v7.0.2) sürümünü sabitler. Sürüm güncellemesinde üç iş akışındaki kimlik ve sürüm yorumları birlikte güncellenir; doğrulama ve derleme işlerinde Git kimlik bilgileri çalışma ağacına bırakılmaz.

## İmza ve hedefleme

`Google (CLI izleyici)`, yerel ayarda kullanılan ayrı bir üretici/rol adresidir; kayıt ekleyici tarafından kabul edilir. Bu adres, `Gemini (Şahit)`, `Copilot (Şahit)` veya yalın `Gemini` ile aynı hedef sayılmaz.

26 Ekim'de güncellenen rol belgesi Şahit'in güncel insan rolünü `Gemini (Şahit)` olarak kaydediyor. Kodun tarihsel yalın `Şahit`/`Sahit` takma adı ise eski kayıtların kapsamını korumak için `Copilot (Şahit)` adresine bağlıdır. Yeni kayıtlar tam üretici/rol adresini kullanmalıdır. Takma adın tüm geçmiş için değiştirilmesi eski işlerin yeniden açılmasına veya başka üreticinin yanıtıyla kapanmasına yol açabilir; bu bakım böyle bir yeniden adresleme yapmaz. Ayrıntı: [hedefleme sözleşmesi](../../katilimcilar/katman-hedefleme.md).

Yerel ayarların açıklaması, içindeki `katilimcilar` listesiyle uyumludur. Ama yerel ayarların komut yolları ile `yerel/kopru_yerel.ps1` içindeki yollar ayrı klasör ağaçlarını gösterir; ayrıntı [yerel taraf sayfasındadır](yerel-taraf.md). Canlı Windows, sanal makine ya da sağlayıcı denemesi bu çevrimdışı kontrollerin kapsamı dışındadır.

## Dal ve PR haritası

Aşağıdaki tablo **26 Ekim 2026 inceleme kesitidir**; canlı durum PR sayfasından okunur. Bekleyen önerilerin 28 Ekim 2026'daki çözümlemesi [dönüşümün teknik ekindedir](donusum-teknik.md#bekleyen-öteki-öneriler). PR hedefleri GitHub'ın kanonik PR verisinden, devam ilişkileri Git geçmişinden doğrulanmıştır.

| PR | Kaynak → hedef | İşlev ve ilişki |
| --- | --- | --- |
| [#1](https://github.com/HalukAINRS/ortak-kopru/pull/1) | `steering-inceleme-2026-10-24` → `main` | Araştırma ve kaynak arşivi; açık taslak referans kaydı. Başlangıç: [Steering README](https://github.com/HalukAINRS/ortak-kopru/blob/steering-inceleme-2026-10-24/steering/README.md). |
| [#2](https://github.com/HalukAINRS/ortak-kopru/pull/2) | `copilot/ortak-kopru-dokumasyonu` → `main` | `kopru_governance` tabanlı denetlenebilir yürütme; #3 ile alternatif tasarım. |
| [#3](https://github.com/HalukAINRS/ortak-kopru/pull/3) | `copilot/implement-transparent-architecture` → `main` | `ortak_kopru` tabanlı ikinci uygulama; #2 ile yedi ortak yolu değiştiriyor. |
| [#4](https://github.com/HalukAINRS/ortak-kopru/pull/4) | `copilot/deus-ex-machina-user-layer` → `main` | İlk Şahit devir/kuyruk çalışması; #6'nın gerçek Git atası. |
| [#5](https://github.com/HalukAINRS/ortak-kopru/pull/5) | `claude/hacker-devri-2026-10-24` → `main` | Hacker devri ve yerel başlatıcı değişiklikleri. |
| [#6](https://github.com/HalukAINRS/ortak-kopru/pull/6) | `sahit/cli-devri-2026-10-24` → `main` | #4'ün devamı; devir paketi, kuyruk ve kabul kaydı. |
| [#7](https://github.com/HalukAINRS/ortak-kopru/pull/7) | `saman/deus-cli-ilk-cevrim` → `deus-ex-machina-2026-10-24` | Açık CLI oturumu kuyruğu, katman dönüş gözcüsü ve yerel kurulum; konu dalına yöneliktir. |
| [#8](https://github.com/HalukAINRS/ortak-kopru/pull/8) | `saman/steering-cli-devam-20261024` → `steering-inceleme-2026-10-24` | Steering CLI devamı, kaynak doğrulama ve Cyber kayıtları; araştırma dalına yöneliktir. |

Bu sekiz PR inceleme anında açık taslaktır. [#9](https://github.com/HalukAINRS/ortak-kopru/pull/9) birleşmiştir; CLI hedefinin API tarafından üstlenilmesini önleyen düzeltmesi korunur. #2/#3 seçim gerektiren iki uygulamadır. #4/#6 bağımsız değişiklik kümeleri değildir. Arşiv aktarımının tamamlanması, ayrı uygulama/okuma işlerinin tamamlanması sayılmaz.

PR dışındaki konu dalları:

| Dal | Konumlandırma |
| --- | --- |
| `deus-ex-machina-2026-10-24` | #7'nin tabanı ve Şaman devir ailesi |
| `gemini-steering-gecmisi-2026-10-24` | TXT/JSON/HTML araştırma arşivi |
| `claude/ortak-alan-araclari-2026-10-25` | Ayrı `ortak-alan/` araç çalışması |
| `copilot/convert-files-to-txt-html-json` | İnceleme anında ucu ana dalın atası; ek birleşmemiş commit yok |
| `saman/kopru-katman-hedefleme-20261024` | #9 ailesinin tamamlanmış düzeltme dalı |

Referans kesiti: [`35d25cc`](https://github.com/HalukAINRS/ortak-kopru/commit/35d25cc20224c70084d08d68be80f80cfb4f4347). Başlangıç `7ac7a176` ile bu kesit arasında eklenen beş tarihsel kayıt ve hedefleme belgesi güncellemesi bakım tabanına alınmıştır.

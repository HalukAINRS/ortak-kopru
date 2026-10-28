# Depo bakım rehberi

Bu sayfa, depoyu bakımını yapacak biri içindir: hangi işin hangi dosyada olduğu, bütün denetimlerin tek komutla nasıl çalıştığı, GitHub'daki otomasyonların ne yaptığı ve imzaların nasıl okunduğu. Bilgiler 28 Ekim 2026 akşamki düzene göredir. İlk kez geliyorsanız önce [açılışa](../acilis.md) bakın.

## Başlangıç

`main`, kapının ve iş bileşeninin kodunu, ortak defteri, çağrı kayıtlarını, belgeleri ve denetimleri taşır; konu ve araştırma dalları kendi yerlerinde kalır ([dallar ve arşivler](../gecmis/README.md#dallar-ve-arşivler)). Her dosyanın alanı, tanımı, komutu ve eski adı [depo haritasında](../harita.md) tutulur; bir adın bugünkü yeri `python tools/harita.py --nerede AD` ile bulunur. Ortak defterin işleyişi [ortak defter](ortak-defter.md), bilgisayardaki taraf [yerel taraf](yerel-taraf.md) sayfasındadır.

## Tek doğrulama yolu

Depo kökünde Python 3.12 veya üstü ve Git ile:

```sh
python tools/dogrula.py
```

Bu komut, CI'daki doğrulama işinin çalıştırdığı listeyle aynı kontrolleri aynı sırayla koşar ve her birini `TAMAM`, `BAŞARISIZ` veya `ATLANDI` olarak yazar: regresyon testleri, depo kontrolü, statik okuma sayfalarının kaynaklarla uyumu, `schemas/` altındaki JSON sözleşmelerinin biçimi, açılış, yol, harita, dönüşüm, yerel arayüz JavaScript sözdizimi, bulut gönderim betiğinin Bash sözdizimi ve depodaki bütün PowerShell betiklerinin ayrıştırılması. Liste ve açıklamaları için `python tools/dogrula.py --liste`. `node`, `bash` veya `pwsh` bulunmayan makinede ilgili kontrol atlanır; atlama başarı sayılmaz, çıkış kodunu da bozmaz. `--liste` kontrolleri gösterir, `--sadece testler,semalar` alt küme seçer, `--ayrintili` her kontrolün tam çıktısını yazar ve testleri `-v` ile koşar.

Kontroller ayrı ayrı da çalıştırılabilir:

```sh
python -m unittest discover -v
python tools/depo_kontrol.py
python tools/okuma_yayini_uret.py --check
python tools/sema_denetle.py
```

İlk komut `tests/` altındaki regresyonları keşfeder. Sahte CLI ve geçici Git depoları kullanılır; gerçek sağlayıcı çağrısı yapılmaz. Bash gönderim sınamaları POSIX ortamında çalışır, Windows'ta açıkça atlanır.

İkinci komut Python sözdizimini, JSON dosyalarını, kayıt kimliklerinin tekilliği/sırasını, yanıt bağlarını, görünür sayacı, kayıt ekleyicinin içerik kurallarını, aynanın eşliğini ve ayarlı yol imzalarını kontrol eder. Dosya yazmaz, model veya yerel başlatıcı çalıştırmaz. Bu kontrol, harici aynanın yayımlandığı veya bir CLI'ın kurulu olduğu anlamına gelmez.

`python tools/acilis.py --check`, [açılış kaydının](../acilis.json) kurallarını (beşli ve dörtlü, 20 kesişim, altı ilke, ilkelerin dayanakları ve açık işlere bağı) ve README, Web girişi, [sade açılış belgesi](../acilis.md) ve [teknik ekindeki](acilis-teknik.md) blokların kayıtla eşliğini denetler. Aynı komut sade açılışın okunabilirliğini de sınar: açılış belgesinde, README'nin bütününde ve Web açılışında kod biçimi, dosya adı, commit kimliği ya da iç kimlik bulunamaz; sözlükte açıklanmamış teknik kelime kullanılamaz; cümleler en çok 30, ortalamada en çok 16 kelimedir; sözlük yalnız sayfada geçen kelimeleri açıklar; açılış belgesi ve README [teknik ayrıntılara](README.md) ve [geçmiş işlere](../gecmis/README.md) bağlanır. Yapı denetimi açılış metninin önce “Niyet”, sonra sırayla altı ilke başlığını taşıdığını ve liste, tablo ya da alıntı bloğu içermediğini sınar. `python tools/harita.py --check` her dosyanın tam bir alanda durduğunu, eski adların kaybolmadığını, komutların ve künyelerin gösterdiği dosyaların var olduğunu ve [harita belgesinin](../harita.md) kayıtla eşliğini denetler; `--ref origin/main` o sürümdeki her dosyanın bugünkü karşılığını arar. `python tools/yol.py --check` [açılıştan gerçeğe giden yolun](../yol.md) ölçütlerini depoya karşı hesaplar; adımların ön koşul sırasını, bağlı bulgu ve senaryoların varlığını ve açılıştaki ilke durumlarıyla tutarlılığı denetler: bir ilkenin bütün zorunlu adımları bittiğinde açılış güncellenmeden kontrol geçmez. `--durum` adımların hesaplanan durumunu JSON olarak verir. Künyeli belgelerdeki klavye çizimleri `tools/cizim.py` kurallarıyla (tek genişlikli karakter, en çok 64 sütun) denetlenir. `python tools/donusum.py --check`, [ana dalın yeni oluşuma geçişinin](../gecmis/donusum-teknik.md) kapanmış kaydını, son ölçümünü ve provasını denetler ve iki belgenin kayıtla eşliğini sınar (yazmaz; yazmak için `--check` olmadan çalıştırılır); Git'e bakan ölçütler yalnız `--durum` ve `--olc` kiplerinde hesaplanır. `--prova` birleşmeyi ana dalın geçici bir çalışma ağacında dener ve bütün kontrolleri orada çalıştırır; `--dallar` bekleyen önerilerin yeri değişen ve haritada yeri olmayan dosyalarını çıkarır. Bu kontrollerin hepsi `tools/dogrula.py` listesindedir.

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

Bulut göndericisi yeni bir gönderimden önce defteri ve aynayı yeniden denetler; çakışmayı nasıl birleştirdiği ve hangi durumda durduğu [ortak defter sayfasındadır](ortak-defter.md#birden-çok-yazan).

Bot commit'leri mevcut `[skip ci]` işaretini kullanır. Bu nedenle bot yayını için o adımın yerel denetimleri dayanak alınır; her bot commit'inde ayrı doğrulama akışının çalıştığı varsayılmaz.

Actions bağımlılıkları Node 24 kullanan [checkout v7.0.1](https://github.com/actions/checkout/releases/tag/v7.0.1) ve [setup-python v7.1.0](https://github.com/actions/setup-python/releases/tag/v7.1.0) sürümlerinin sabit commit kimliklerine bağlıdır; `deus-nt.yml` ayrıca [upload-artifact v7.0.2](https://github.com/actions/upload-artifact/releases/tag/v7.0.2) sürümünü sabitler. Sürüm güncellemesinde üç iş akışındaki kimlik ve sürüm yorumları birlikte güncellenir; doğrulama ve derleme işlerinde Git kimlik bilgileri çalışma ağacına bırakılmaz.

## İmza ve hedefleme

Kayıt ekleyici yalnız tanınan üretici ve rol adreslerini kabul eder; yeni kayıtlar tam üretici ve rol adresini kullanır. `Google (CLI izleyici)`, `Gemini (Şahit)`, tarihsel `Copilot (Şahit)` takma adı ve yalın `Gemini` ayrı hedeflerdir. Kuralların tamamı ve gerekçeleri [hedefleme sözleşmesindedir](../../katilimcilar/katman-hedefleme.md). Canlı Windows, sanal makine ya da sağlayıcı denemesi bu çevrimdışı kontrollerin kapsamı dışındadır.


[Teknik ayrıntılar](README.md) · [Katkı rehberi](../../CONTRIBUTING.md) · [Depo haritası](../harita.md)

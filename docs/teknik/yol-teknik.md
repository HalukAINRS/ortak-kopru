# Açılıştan gerçeğe: teknik ek

<!-- uretilen:yol_teknik -->

Bu ek, açılıştan gerçeğe giden yolun teknik karşılığıdır. Her adımın bağlantıları, ölçütleri, ölçütlerin bugünkü değerleri, dokunacağı yerler ve geri alma yolu burada durur. Sade anlatım yol sayfasındadır.

Kayıt `docs/yol.json`, sözleşmesi `schemas/yol.schema.json`, aracı `tools/yol.py`. `python tools/yol.py --check` ölçütleri depoya karşı hesaplar, adımların ön koşul sırasını ve ilkelerle açılış arasındaki tutarlılığı denetler, iki belgenin kayıtla eşliğini sınar. `python tools/yol.py --durum` her adımın hesaplanan durumunu JSON olarak verir.

## Adımlar

| Adım | İlkeler | Ön koşul | Karar | Yön | Büyüklük | Bulgu, senaryo | Durum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0. Zemin (`zemin`) | 3, 6 | — | — | depo içi | orta | — | tamam |
| 1. Gönderici yalnız seçileni gönderir (`sinir`) | 2, 4 | zemin | Haluk: bekliyor | yerel → Web | küçük | R-17, S02 | karar-bekliyor |
| 2. Katkı kalıbı (`katki-kalibi`) | 5 | zemin | — | Web → Web (okurdan yazıya) | küçük | — | tamam |
| 3. Gelen kutusu (`gelen-kutusu`) | 1, 2 | katki-kalibi | Haluk: bekliyor | Web → yerel | orta | S09 | karar-bekliyor |
| 4. Yanıt geri döner (`yanit-donusu`) | 1 | gelen-kutusu | Haluk: bekliyor | yerel → Web | orta | — | onkosul-bekliyor |
| 5. İlk dış katkı (`ilk-dis-katki`) | 5 | katki-kalibi | — | Web → yerel → Web | küçük | — | disaridan-bekleniyor |
| 6. Kapı GitHub dışına açılır (`kapinin-genislemesi`) | 1 (ufuk) | yanit-donusu | Haluk: bekliyor | yerel ↔ ikinci dış alan | büyük | S08 | ufukta |

**Yolun ağacı** · mühendis çizimi

```text
  (0) Zemin                                         ■ tamam
   ├─▶ (1) Gönderici yalnız seçileni gönderir       □ karar
   └─▶ (2) Katkı kalıbı                             ■ tamam
       ├─▶ (3) Gelen kutusu                         □ karar
       │   └─▶ (4) Yanıt geri döner                 □ ön koşul
       │       └─▶ (6) Kapı GitHub dışına açılır    ◇ ufukta
       └─▶ (5) İlk dış katkı                        □ dışarıdan
```

**İlkelerin göstergesi** · mühendis çizimi

```text
  ilke                                adımlar   açılışta
  ──────────────────────────────────  ────────  ────────────────
  1 Karşılıklılık                     □□◇       kısmen işliyor
  2 Yerel merkez                      □□        kısmen işliyor
  3 Köken ve sahiplik                 ■         işliyor
  4 Sınır                             □         kısmen işliyor
  5 Açık katılım                      ■□        kısmen işliyor
  6 Doğrulanabilirlik ve geri dönüş   ■         işliyor
```

### 0. Zemin

Açılış, harita ve tanım kayıtları; `tools/acilis.py`, `tools/harita.py` ve `tools/dogrula.py` ile üretim ve denetim. Ana dala geçişin aşamaları, provası ve ölçümü: `docs/donusum.json`, `tools/donusum.py`.

Dokunacağı yerler: `docs/acilis.json`, `docs/harita.json`, `tools/dogrula.py`.

Geri alma: İlgili commit'ler geri alınır; kayıtlar ve belgeler önceki hâline döner.

| Ölçüt | Bugün |
| --- | --- |
| `docs/acilis.json` var | karşılanıyor |
| `docs/harita.json` var | karşılanıyor |
| `tools/dogrula.py` içinde `tools/harita.py` geçer | karşılanıyor |

### 1. Gönderici yalnız seçileni gönderir

`git add -A -- .` yerine, `.github/scripts/kopru_gonder.sh` gibi yalnız `kopru.html`, `ayna/kopru.html` ve `kayit/` hazırlanır; başka değişiklik varsa uyarı yazılır, o değişiklik gönderilmez. Sınama: izlenmeyen ilgisiz bir dosya yerelde kalır, uzak dala gitmez. R-17 kaydı `düzeltildi` olur.

Dokunacağı yerler: `yerel/kopru_gonder.ps1`, `tests/test_powershell.py`, `docs/gecmis/rafine/claude-code-bulut-2026-10-28-bulgular.json`.

Geri alma: Değişikliği getiren commit geri alınır; gönderici eski kapsamına döner. Defter ve kayıtlar etkilenmez.

Karar (Haluk): Yerel gönderici, defter ve çağrı kayıtları dışındaki dosyaları göndermeyi bıraksın mı? Bırakırsa öteki dosyalar kapıdan, seçilerek gider.

Görüş (Claude Code Bulut, 2026-10-28): Önerim: evet, daraltılsın. R-17 bugün uykuda: `yerel/kopru_gonder.ps1` hiçbir bilgisayarda kurulu değil (Haluk, 28 Ekim 2026 18.47 UTC). Daraltma küçük ve geri alınabilir; `.github/scripts/kopru_gonder.sh` ile aynı kapsam (`kopru.html`, `ayna/kopru.html`, `kayit/`) iki gönderim yolunu eşitler. Öteki dosyalar kapıdan (`kapi.py prepare`, `plan`, `send`) seçim ve kayıtla gider; 2. ve 4. ilkeler bu açıdan tam işler. Göndericiyi tümden kaldırmak da bir seçenek; ama yerel izleyici yeniden kurulursa yanıtlarını göndermek için bir göndericiye ihtiyaç duyar. Bu yüzden daraltmak kaldırmaktan iyidir. Gelen kutusunun yeri kararıyla da bağlıdır: seçimsiz bir gönderici, depo içindeki her özel dosyayı dışarı taşıyabilir.

| Ölçüt | Bugün |
| --- | --- |
| `yerel/kopru_gonder.ps1` içinde `git add -A` geçmez | karşılanmıyor |
| `tests/test_powershell.py` içinde `test_sender_leaves_unselected_files_local` sınaması var (CI'da geçer) | karşılanmıyor |
| R-17 bulgusu düzeltildi | karşılanmıyor |

### 2. Katkı kalıbı

GitHub konu formu `.github/ISSUE_TEMPLATE/karsilik.yml`: tür (soru, kaynak, düzeltme, görüş), `yer` (sayfa ve bölüm adresi), metin, dayanak ve sınır onayı. Okuma sayfası üreticisi (`tools/okuma_yayini_uret.py`, `karsilik()`) her `h2` bölümünün sonuna `issues/new?template=karsilik.yml&yer=<sayfa#bölüm>&title=[Karşılık] <sayfa> · <bölüm>` bağlantısı ekler; sayfa sonundaki bağlantı da aynı formu sayfa adresiyle açar. Markdown kaynakları değişmez; yalnız üretici, stil ve sayfalar değişir. Boş konu açmak yine mümkündür (`config.yml`).

Dokunacağı yerler: `.github/ISSUE_TEMPLATE/karsilik.yml`, `.github/ISSUE_TEMPLATE/config.yml`, `tools/okuma_yayini_uret.py`, `okuma.css`, `tests/test_okuma_yayini_uret.py`.

Geri alma: Form dosyası ve üretici değişikliği geri alınır, sayfalar yeniden üretilir. Açılmış konular GitHub'da kalır.

| Ölçüt | Bugün |
| --- | --- |
| `.github/ISSUE_TEMPLATE/karsilik.yml` var | karşılanıyor |
| `tools/okuma_yayini_uret.py` içinde `template=karsilik` geçer | karşılanıyor |
| `tests/test_okuma_yayini_uret.py` içinde `test_each_section_offers_a_linked_reply` sınaması var (CI'da geçer) | karşılanıyor |

### 3. Gelen kutusu

`kapi.py inbox`: GitHub REST `GET /repos/{owner}/{repo}/issues` (çekme istekleri hariç); her konu yazarı, `updated_at`, gövde karması ve formdaki `yer` alanıyla aktarım veritabanına gelen kayıt olarak yazılır. İçerik özel aktarım dizinindeki gelen kutusuna çıkarılır; depo çalışma ağacına yazılmaz. Kimliksiz okuma mümkün; oran sınırı ve belirteç kararı Haluk'ta.

Dokunacağı yerler: `src/ortak_kopru/gateway_cli.py`, `src/ortak_kopru/adapters/github.py`, `src/ortak_kopru/exchange.py`, `tests/test_gateway_inbox.py`.

Geri alma: Komut kaldırılır. Gelen kutusu özel dizinde kalır; depoya hiçbir şey yazılmamıştır.

Karar (Haluk): GitHub'a hangi yetkiyle bakılsın: yalnız herkese açık okumayla mı, kişisel bir anahtarla mı? Gelen kutusu bilgisayarda nerede dursun?

Görüş (Claude Code Bulut, 2026-10-28): Önerim: önce yalnız herkese açık okumayla başlansın; gelen kutusu, kapının deponun dışında tuttuğu özel dizinde dursun. Kimliksiz GitHub REST istekleri IP başına saatte 60 ile sınırlıdır (GitHub'ın REST oran sınırı belgesi, 28 Ekim 2026'da bakıldı); kimlikli istekler saatte 5000. Gelen kutusu bir koşuda açık konuları sayfa başına 100 kayıtla okur; bir ya da iki istek yeter. Anahtar gerekirse: yalnız bu depoya, yalnız Issues okuma izniyle ve bitiş tarihli ince ayarlı kişisel erişim belirteci; ortam değişkeninden okunur, dosyaya yazılmaz. Yanıtların yazılması (4. adım) yazma izni ister; o ayrı bir belirteçle verilmeli, gelen kutusu yalnız okuyan izinle kalmalı. Yer: kapının `--exchange-dir` dizini bir Git çalışma ağacının içinde olamaz (`src/ortak_kopru/local_files.py`); gelen kutusu onun alt dizini olursa (örneğin `<aktarım dizini>/gelen`), yerel göndericinin `git add -A` kapsamına hiçbir zaman girmez. Bu, 1. adımın kararıyla bağlıdır: gönderici daraltılmadan yeniden kurulsa bile gelen kutusu depoya sızamaz.

| Ölçüt | Bugün |
| --- | --- |
| `src/ortak_kopru/gateway_cli.py` içinde `"inbox"` geçer | karşılanmıyor |
| `tests/test_gateway_inbox.py` içinde `test_issue_lands_in_private_inbox_with_provenance` sınaması var (CI'da geçer) | karşılanmıyor |

### 4. Yanıt geri döner

`kapi.py reply`: gelen kutusundaki bir kaydın yanıtı `POST /repos/{owner}/{repo}/issues/{n}/comments` ile yazılır. İstek, yanıt ve belirsiz sonuç ayrı olaylardır; belirsiz sonuç gönderimdeki gibi `reconcile` ile uzlaştırılır.

Dokunacağı yerler: `src/ortak_kopru/gateway_cli.py`, `src/ortak_kopru/adapters/github.py`, `tests/test_gateway_inbox.py`.

Geri alma: Komut kaldırılır. Yazılmış yorumlar GitHub'da silinmez; düzeltme yeni yorumla yapılır.

Karar (Haluk): Yanıtlar GitHub'a hangi hesapla yazılsın?

| Ölçüt | Bugün |
| --- | --- |
| `src/ortak_kopru/gateway_cli.py` içinde `"reply"` geçer | karşılanmıyor |
| `tests/test_gateway_inbox.py` içinde `test_reply_returns_to_issue_and_records_event` sınaması var (CI'da geçer) | karşılanmıyor |

### 5. İlk dış katkı

Ölçüt elle doldurulur: `kanit` alanına Haluk dışından birinin açtığı konunun ve ona verilen yanıtın adresleri yazılır. Araç adreslerin biçimini denetler, içeriğini denetleyemez.

Dokunacağı yerler: `docs/yol.json`.

Geri alma: Kanıt adresleri kayıttan çıkarılır; adım yeniden açık görünür.

| Ölçüt | Bugün |
| --- | --- |
| elle: Haluk dışından birinin açtığı konu ve ona verilen yanıtın adresi (0/2 adres) | karşılanmıyor |

### 6. Kapı GitHub dışına açılır

Yeni bir bağdaştırıcı GitHub bağdaştırıcısının sözleşmesini (plan, gönderim, uzlaştırma, kesin sürümden alma) aynen uygular; aktarım paketi ve olay kaydı değişmez.

Dokunacağı yerler: `src/ortak_kopru/adapters/`, `src/ortak_kopru/gateway_cli.py`.

Geri alma: Bağdaştırıcı kaldırılır; GitHub yolu etkilenmez.

Karar (Haluk): Kapı hangi dış alana açılsın: bir dosya hizmetine mi, başka bir siteye mi?

| Ölçüt | Bugün |
| --- | --- |
| elle: Kapının ikinci dış alana yaptığı bir aktarımın kaydı (0/1 adres) | karşılanmıyor |

## Akışlar

Gelen kutusu ve yanıt adımları tamamlandığında bir katkının izleyeceği yol aşağıdadır. Parantez içindeki sayılar o geçişi koruyan ilkedir.

**Gelen bir katkının yaşamı** · mühendis çizimi

```text
  GELEN BİR KATKININ YAŞAMI · durum makinesi

  ┌───────────┐ konu     ┌───────────┐ kapı     ┌───────────┐
  │ dışarıda  ├─────────▶│ Web'de    ├─────────▶│ gelen     │
  │ bir fikir │ açılır   │ yayımda   │ çeker    │ kutusunda │
  └───────────┘          └───────────┘          └──┬────────┘
                                                   │ yerel
                                                   │ kullanıcı
                                                   ▼ okur
  ┌───────────┐ yanıt    ┌───────────┐ karar    ┌───────────┐
  │ bağlandı  │◀─────────┤ yanıtlandı│◀─────────┤ okundu    │
  │ (5)       │ döner    │ (1)       │ verilir  │ (2)       │
  └───────────┘          └───────────┘          └───────────┘
  (6) her geçiş ayrı bir olaydır ve kayda geçer. Hiçbir
  durum atlanmaz; yanıt gelmemesi kabul sayılmaz, katkı
  'bekliyor' olarak görünür kalır.
```

**Gelen kutusu ve yanıt** · mühendis çizimi

```text
  GELEN KUTUSU VE YANIT · sıra çizimi

 okur            Web           kapı      yerel kullanıcı
   │              │              │              │
   │ konu açar    │              │              │
   ├─────────────▶│              │              │
   │              │ kapı okur    │              │
   │              │◀─────────────┤              │
   │              ├─────────────▶│              │
   │              │              │ kutuya koyar │
   │              │              │ yazar, zaman │
   │              │              │ ve yer ile   │
   │              │              ├─────────────▶│
   │              │              │              │ okur, karar
   │              │              │              │ verir
   │              │              │◀─────────────┤
   │              │              │ yanıtı yazar │
   │              │◀─────────────┤              │
   │◀─────────────┤              │              │
   │ yanıtı görür │              │              │
   │              │              │              │
  Her ok ayrı bir olaydır. Belirsiz kalan bir yazma,
  gönderimde olduğu gibi uzlaştırılmadan yapıldı sayılmaz.
```

## Kurallar

Adımın durumu kayda yazılmaz; ölçütlerden hesaplanır. Tamam olan bir adımın ön koşulları da tamam olmalıdır. Açılışta tam işlemeyen her ilkenin en az bir zorunlu adımı vardır. Bir ilkenin bütün zorunlu adımları bittiğinde açılıştaki durumu `uygulanıyor` olarak güncellenmeden denetim geçmez; tam işleyen bir ilkeye bağlı açık zorunlu adım kalamaz.

Yeni bir adım eklemek için kayda bir adım nesnesi yazılır: bağlı ilkeler, ön koşullar, gerekiyorsa karar, sade ve teknik anlatım, geri alma yolu ve en az bir ölçüt. Ölçüt türleri: `dosya_var`, `dosya_icerir`, `dosya_icermez`, `test_var`, `bulgu_kapali`, `elle`. Sonra `python tools/yol.py` iki belgeyi yeniden yazar.

<!-- /uretilen:yol_teknik -->

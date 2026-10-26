# deus_ex_machina — sonuç, oturum devri ve kurtarma

Bu aşama, ilk iş çekirdeğinin çevrimini tamamlar: sonuç ve kabul denetimi ekrandan yapılabilir; hedef oturum kendi etkin atamalarını bulabilir; kaynak baytlarıyla taşınabilen bir devir paketi hazırlanabilir; özel çalışma alanı tutarlı biçimde yedeklenip yeni bir dizine geri yüklenebilir.

Hedef Windows bilgisayarındaki ilk kullanım, sürücü imzalama/yükleme ve canlı NT denemesi ayrı aşamada kalır. Aşağıdaki `portable` örnekleri açık geliştirme kipidir; kernel kurulumu veya gerçek sağlayıcı çalıştırması kanıtı üretmez. Temel kurulum ve iş sözleşmesi: [DEUS_EX_MACHINA.md](DEUS_EX_MACHINA.md).

## Sonucu ekrandan tamamlamak

1. Bir iş oluşturun veya mevcut işi seçin; özgün söz, kapsam ve ölçütleri okuyun.
2. İşi bir katılımcı ve oturum etiketiyle atayın.
3. Atanmış oturum adına **alımı beyan edin**. Bu kayıt, yerel kullanıcı/oturum beyanıdır; modelin çağrıldığını veya içeriği anladığını kanıtlamaz.
4. Sonuç özetini ve varsa yerel çıktı dosyalarının tam yollarını girin. Dosyaların o andaki baytları özel çalışma alanında saklanır. Dosya okunamazsa sonuç kaydı oluşmaz ve taslak korunur.
5. Güncel sonucun her ölçütü için **Geçer** veya **Kalır** seçin; kanıtı ve denetleyeni yazın. Seçimler başlangıçta boştur. Denetim beyanı otomatik anlamsal doğrulama değildir.
6. Bütün ölçütler geçerse iş `completed`; en az bir ölçüt kalırsa `blocked` olur. Kaydedilmiş değerlendirmeler sonuç yanında görünür.

Formlar, açıldıkları söz sürümüne ve çalıştırma/sonuç kimliğine bağlıdır. Başka bir oturum veya sekme yeni sonuç üretirse eski taslak sessizce o sonuca bağlanmaz. Güncel sonucu yükleme işlemi açıkça yapılır ve yeni denetimler boş başlar. Yanıt kaybolursa aynı içerikle tekrar gönderim aynı istek anahtarını kullanır.

## Oturumlar ve gelen kutusu

`sessions`, atamalarda geçen oturumların kayıt dökümünü verir. `liveness=not_observed` ve `identity_verified=false` alanları korunur: bir satırın görünmesi, o CLI sürecinin açık olduğunu veya model kimliğinin bağımsız doğrulandığını göstermez.

```powershell
python deus.py --backend portable --state-dir D:/DeusVeri sessions
python deus.py --backend portable --state-dir D:/DeusVeri inbox --session OTURUM_ETIKETI
```

Gelen kutusu yalnız o oturumun güncel iş sürümüne bağlı, hâlâ etkin `assigned` veya `received` çalıştırmalarını gösterir. Duraklatılan/iptal edilen, devredilen, sonuç üretmiş veya kapanmış çalıştırmalar teslim edilecek iş olarak gösterilmez. Listeleme alım makbuzu ya da yeni olay üretmez.

Yerel HTTP karşılıkları:

| Uç nokta | Anlamı |
| --- | --- |
| `GET /api/sessions` | Kayıtlarda geçen oturumlar ve etkin atama sayıları |
| `GET /api/sessions/{URL_KODLANMIS_OTURUM}/inbox` | O oturumun güncel etkin atamaları |

Diğer özel API'lerle aynı erişim anahtarı gerekir. Bu uç noktalar genel ağ servisi veya uzaktaki CLI süreçlerini tarayan keşif sistemi değildir.

## Bütün kaynak baytlarıyla devir

`context` ve ekrandaki JSON indirme, uygulamanın metin bağlamını verir. Metin bütçesinden dolayı dışarıda kalan veya UTF-8 olmayan dosyalar bu JSON içinde yalnız metadata ile temsil edilebilir. `handoff` ise bu dosyaların saklanmış baytlarını da yeni bir özel dizine taşır.

```powershell
python deus.py --backend portable --state-dir D:/DeusVeri handoff CALISTIRMA_ID --session OTURUM_ETIKETI --output D:/DeusDevir/is-001
python deus.py handoff-verify D:/DeusDevir/is-001
```

Hedef dizin önceden bulunmamalı; Git çalışma ağacının ve etkin `--state-dir` dizininin dışında olmalıdır. Paket mevcut kaynak dosyasını yeniden okumak yerine, işe alınmış sabit görüntüyü kullanır. Aynı SHA-256 içeriği birden çok kez başvurulmuşsa tek nesne olarak taşınır. Kaynaklar ile önceki sonuçların çıktı dosyaları dahildir.

| Paket parçası | İçerik |
| --- | --- |
| `manifest.json` | İş, söz sürümü, çalıştırma ve oturum bağı; dosya boyutları ve SHA-256 değerleri |
| `context.json` | Özgün/güncel söz, kapsam, ölçütler, kaynak metadata'sı ve önceki sonuçlar |
| `objects/` | Manifestte belirtilen kaynak/çıktı dosyalarının tam baytları |

Paketin tamamı başka bir özel dizine veya VM'ye taşınabilir. Paket içindeki `objects/<sha256>` yolları taşınan kopyaya göredir; tarihsel `path` değerleri kaynak konumunun kaydıdır, başka bilgisayarda aynı yolun bulunacağını varsaymaz.

Devir biçimi sınırları: nesne başına 8 MiB, en fazla 8192 benzersiz nesne, context ve manifest dahil toplam 1 GiB; context JSON 64 MiB ve manifest 4 MiB. Bir sınır aşılırsa dosyalar sessizce atlanmaz; paket hazırlığı başarısız olur ve hedef yayımlanmaz. Bunlar modelin bağlam penceresi sınırları değildir; paketin kendisine ait uygulama sınırlarıdır.

**Hazırlama, teslim alma değildir.** Manifestte `delivery_receipt=false` ve `live_receive_required=true` bulunur. Hazırlık sırasında veritabanına alım/çalıştırma olayı yazılmaz. `handoff-verify` yalnız paket bütünlüğünü ve bağlarını denetler; paketin hazırlandığı andan sonra işin iptal edilmediğini bilemez.

İşi gerçekten devralan oturum, güncel çalışma alanında alım yapar:

```powershell
python deus.py --backend portable --state-dir D:/DeusVeri receive CALISTIRMA_ID --session OTURUM_ETIKETI --request-key alim-001
```

Bu anda canlı iş durumu tekrar denetlenir. Paket hazırlandıktan sonra iş iptal edilmiş, düzeltilmiş veya devredilmişse eski çalıştırma kabul edilmez. Ayrı bir makineye dosya taşımak, o makineye otomatik broker bağlantısı veya görev yetkisi kazandırmaz. Paket doğrulaması görevleri içe aktarmaz, CLI başlatmaz veya bir model sağlayıcısını çağırmaz.

## Dört farklı çıktı

| Çıktı | Ne taşır? | Kullanım amacı |
| --- | --- | --- |
| `context` / ekrandaki JSON | Tek işin bütçeli metin bağlamı ve dosya metadata'sı | Hızlı okuma, işin bağlamını görmek |
| `handoff` | Tek etkin çalıştırmanın bağlamı ve başvurulan kaynak/çıktı baytları | Oturum veya makine arasında özel dosya devri |
| `export` | İşlerin ve olayların JSON dökümü | İnceleme ve ayrı araçlarla işleme |
| `backup` | SQLite veritabanının tamamı ve onun başvurduğu dosya nesneleri | Çalışma alanını geri yükleyebilmek |

JSON dışa aktarımı tam yedek sayılmaz. Devir paketi de bütün çalışma alanının yedeği değildir.

## Tutarlı yedekleme

```powershell
python deus.py --state-dir D:/DeusVeri backup --output D:/DeusYedek/2026-10-26-001
python deus.py backup-verify D:/DeusYedek/2026-10-26-001
```

Kaynak çalışma alanı mevcut olmalıdır; bulunmayan kaynak için boş veritabanı oluşturulmaz. Yeni hedef, kaynak çalışma alanının dışında ve Git dışında olmalıdır. Mevcut bir yedek dizininin üzerine yazılmaz.

Yedekleme, SQLite'ın `Connection.backup()` işlemiyle tutarlı bir veritabanı görüntüsü alır. Dosya listesi bu görüntüden çıkarılır; bütün kaynak ve çıktı nesneleri boyut/SHA denetimiyle kopyalanır. Veritabanındaki istek anahtarları, geçmiş ve denetimler de korunur. Yalnız referanslı nesneler alınır; rastgele ek dosyalar, eski geçici dosyalar, broker erişim anahtarı veya sürücü ikilileri yedeğin kapsamına girmez.

Paket önce geçici kardeş dizinde tamamlanır; doğrulamadan sonra yeni hedef adına atomik olarak yayımlanır. Hata halinde yarım bir paket başarılı yedek adıyla bırakılmaz. Başka bir işlem o sırada hedefi oluşturmuşsa onun dizini korunur.

## Geri yükleme

```powershell
python deus.py --state-dir D:/DeusVeri-Kurtarilan restore D:/DeusYedek/2026-10-26-001
```

Hedef yeni bir dizin olmalıdır. Geri yükleme; manifest, veritabanı şeması/bütünlüğü, ilişkiler ve dosya karmaları doğrulanmadan hedef çalışma alanını yayımlamaz. Bozuk veya desteklenmeyen yedek reddedilir. Mevcut canlı çalışma alanı yerinde değiştirilmez.

Geri yüklenen durum, **yedeğin alındığı andaki kayıttır**. Yedekten sonra gerçekleşmiş dış işlemleri geri almaz, açık CLI süreçlerini yeniden oluşturmaz ve `running` kaydının şu anda çalışan bir süreç olduğu sonucunu vermez. Kurtarılan alanı etkin alan olarak kullanmaya geçerken eski sunucuyu durdurun; aynı iş geçmişinin iki bağımsız kopyasını eşzamanlı etkin broker olarak kullanmayın.

`backup`, `backup-verify`, `restore` ve `handoff-verify`, NT sürücüsü erişilemiyorken de kullanılabilen özel veri bakım işlemleridir. Runtime çıktısı yine seçilen `nt-kernel` kipini ve gerçek `ready=false` durumunu taşır; portable'a gizli geçiş veya iş çalıştırma yapılmaz.

## Sınırlar ve bakım

- Bu dizin yayımı Windows ve Linux üzerinde desteklenir. İşletim sistemi/dosya sistemi hedefi ezmeyen atomik yayımı sağlayamıyorsa işlem açık hatayla durur.
- Karma denetimleri veri tutarlılığını gösterir; imza, şifreleme, kişi kimliği veya talimat yetkisi değildir. Manifest ve tüm dosyaları değiştirebilen kişi yeni bir tutarlı paket üretebilir.
- Kaynaklar özel veri olmaya devam eder. Devir/yedek dizini kendiliğinden GitHub'a veya başka bir hizmete yüklenmez.
- Bu çalışma, mevcut veritabanı şema sürümünü değiştirmez. Gelecekteki şemalar için ayrıca geçiş uygulaması gerekir; bilinmeyen sürüm sessizce değiştirilmez.

GitHub/Drive/MCP gibi hizmetler için sonraki adaptörler, bu hazırlama–alım–sonuç ayrımına bağlanacaktır. Özellikle uzak kaynak eklenirken depo/commit/blob veya hizmet dosya sürümü korunmalıdır; yerel dosya yolu tek başına uzak kaynağın kökenini açıklamaz.

### Birincil teknik kaynaklar

- [Python 3.12: SQLite Connection.backup](https://docs.python.org/3.12/library/sqlite3.html#sqlite3.Connection.backup)
- [Python 3.12: os.rename](https://docs.python.org/3.12/library/os.html#os.rename)
- [Linux: renameat2 ve RENAME_NOREPLACE](https://man7.org/linux/man-pages/man2/rename.2.html)

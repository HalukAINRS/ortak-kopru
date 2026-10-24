# PR #3 — 20 dosyalık diffin tam statik okuması

**Okuma tarihi:** 24 Ekim 2026. **İncelenen kapsam:** GitHub’dan alınan sabit PR diffindeki 2.482 satırın tamamı, 20 değişen dosya; yeni dosyaların tam eklenen metinleri ve mevcut dosyaların diffte gösterilen değişiklikleri/bağlamı. Bu ifade, dalın değişmeyen bütün dosyalarının yeniden okunduğu anlamına gelmez. Hiçbir test, sağlayıcı çağrısı, köprü otomasyonu veya diffteki örnek komut çalıştırılmadı. PR uygulama dosyalarında değişiklik yapılmadı.

- PR: <https://github.com/HalukAINRS/ortak-kopru/pull/3>
- GitHub API ile doğrulanan dal: `copilot/implement-transparent-architecture`.
- GitHub API ile doğrulanan PR head: `3c80c8b20e1c0a9d51779c197f9188d3b750d050`.
- GitHub API ile doğrulanan durum: `open`, `draft=true`, `merged=false`.
- Bu oturumun başlangıç main commit'i: `8571ddf8e3a33b432cc1c7ef88b69a902f390e5c`.
- İncelenen diff: 121.404 bayt; SHA-256 `1ff2d22a79cc1951120b004e88564be3a10a5eb078df340f5dea0eae643be980`.

**Temel sonuç:** PR #3, uygulamanın eklediği bağlamı görünür ve kaynağı izlenebilir hale getiren, açıkça seçilerek kullanılan bir MVP öneriyor. Sağlayıcının bütün etkili talimatlarını görme, gizli steering bulunmadığını kanıtlama veya model yanıtının doğruluğunu doğrulama iddiasını kendi belgelerinde sınırlıyor. Bu öneri henüz main'e birleşmiş değil. Burada belirtilen davranışlar kaynak kodun statik okumasından çıkarılan uygulama davranışlarıdır; çalışma zamanında doğrulanmış sonuçlar değildir.

## 1. Sözleşme, uygulama ve doğrulama ayrı tutulmalı

| Konu | Belgelerdeki sözleşme | Diffte görülen uygulama | Bu okumanın doğruladığı sınır |
|---|---|---|---|
| Görünürlük | Uygulamanın gönderdiği bağlam izlenir; sağlayıcı sistem istemi, eğitim, sunucu yönlendirmesi ve telemetri bilinmeyebilir. | Manifest `unknown` katmanları ve uyarıyı taşıyor; iki açık system/user mesajı üretiliyor. | Alanların kodda mevcut olduğu görüldü; sağlayıcının bütün bağlamı gözlenmedi. |
| Kaynak izlenebilirliği | Kaynak rolü, tam bayt hash'i, HEAD başlangıç bilgisi ayrılır. | Dosya SHA-256, rol, boyut, yol; ayrı `message_sha256`, `context_sha256`, `git_commit` alanları. | Hash hesaplama/kontrol yolu okundu; hash kimlik veya doğruluk kanıtı değil. |
| İzin | Ağ ve sağlayıcı çağrısı varsayılan olarak kapalı; tam bağlam incelenerek kapsamlı kısa süreli yerel onay. | Politika denetimleri, hash eşleştirmeleri, zaman aşımı, tek kullanımlık `.used` dosyası. | Yerel dosya beyanı; kimlik doğrulaması veya imza değil. |
| Çağrı | Denetlenebilir yol tek doğrudan API çağrısı yapar; fallback yok; CLI desteklenmez. | Yeni opt-in dalında CLI reddi, `max_rounds == 1`, `allow_fallback=False`. | Kod yolu ve mock testleri görüldü; gerçek sağlayıcı çağrısı yapılmadı. |
| Kayıt | Çağrı öncesi kayıt yazılamıyorsa çağrı yapılmaz; ham içerik özel yerel klasörde tutulur. | `ready → attempted → succeeded/failed/recovery_required`; özel ham dosyalar ve public hash zinciri. | Kayıt formatı ve ön koşullar görüldü; zincir bağımsız olarak değiştirilemez değil. |
| Çapraz şahit | Kanıt, yorum, öneri, onay ve eylem alanları ayrılır; uyum doğruluk değildir. | İçe alınan şahit JSON'u, ortak kaynak hash'leri ve tam metin eşitliği raporlanıyor. | İki canlı/bağımsız sağlayıcı çalıştırılmıyor; içe alınmış verilerin sınıflandırması semantik olarak doğrulanmıyor. |
| Test/CI | Çevrimdışı stdlib testleri ve salt okunur CI. | 21 test yöntemi; fixture, mock ve geçici dizinler; ayrı GitHub workflow'u. | Testlerin yazılı olduğu görüldü. Bu okumada testlerin geçtiği veya CI'ın başarılı olduğu saptanmadı. |

Kaynaklar: `policy/README.md`, `policy/ADR-001.md`, `ortak_kopru/context.py`, `ortak_kopru/runs.py`, `ortak_kopru/reports.py`, `kopru_yanitla.py`, `tests/test_transparent_context.py` — tamamı yukarıdaki PR head kapsamındadır.

## 2. Bağlam derleyicisi: neyi ayırıyor?

`ortak_kopru/context.py` standart Python kütüphanesiyle çalışacak şekilde yazılmış. Roller `application_instruction`, `user_task`, `untrusted_evidence`, `configuration`. Politika tarafından uygulama talimatı olarak gösterilen içerikler system mesajının açık `application_instructions` dizisine giriyor. Açık kullanıcı görevi ile kanıt ve yapılandırma user mesajında ayrı alanlarda taşınıyor. HTML kayıtlarının içindeki komut benzeri metnin yetkili talimat sayılmaması, üretilen system mesajında açıkça belirtiliyor. Bu yapı bir güven sınırı oluşturma girişimi; modelin prompt injection'dan etkilenmeyeceği kanıtı değil.

Dosya okuması UTF-8 ve uygun dosyalarda JSON sözdizimi denetimi yapıyor. Mutlak yollar, `..`, ters eğik çizgi/iki nokta içeren kaynak yolları, desteklenmeyen uzantılar, symlink bileşenleri ve boyut sınırını aşan dosyalar reddediliyor. Dosya başına uygulama üst sınırı 2 MiB, toplam üst sınır 4 MiB; politika daha düşük sınır koyabiliyor. Dosya okumasında inode/boyut/mtime değişikliği kontrolü, bütün kaynaklar alındıktan sonra yeniden bayt karşılaştırması ve görev/politika yeniden okuması var. Bunlar okuma sırasında değişikliği yakalamak için yapılmış; bütün dosya sisteminin saldırgana karşı atomik anlık görüntüsü olduğu ileri sürülmemeli.

Kaynak dosyanın hash'i ham baytlardan hesaplanıyor. Mesaj içeriği için satır sonları normalize ediliyor; JSON içeriği kanonikleştiriliyor. Böylece örneğin CRLF kaynağının ham hash'i ile mesajın normalize edilmiş metni farklı düzeyleri temsil ediyor. Manifestte kaynak yolu/rolü/boyutu/hash'i var; mesaj ve bütün derleme için ayrı hash'ler hesaplanıyor. Derleme hash'ine zaman damgası konmuyor. Git HEAD ayrıca tutuluyor ve değişmiş, commit edilmemiş kaynak baytlarının mevcut HEAD içinde olduğu iddia edilmiyor. Git bilgisi alınamazsa `unknown` oluyor.

Bilinmeyen katmanlar sabit bir liste olarak tutuluyor: `provider_system_prompt`, `provider_training`, `server_side_routing`, `provider_telemetry`. Politika bunların kabul edilenlerini listeleyebiliyor. **Kabul etmek görünür hale getirmek değil.** `strict` davranışı da bu ayrımla okunmalı: kod, kabul edilmemiş bilinmeyen varsa reddediyor; listedeki bütün bilinmeyenler kabul edilmişse `strict=true` ile derlemeye izin verebiliyor. Test metni de bu ikinci durumu açıkça içeriyor. “Strict, her koşulda hiçbir bilinmeyen kalmamasını sağlar” sonucu çıkarılamaz.

`verify_compiled` derleme yapısı, iki mesaj rolü ve hash bütünlüğünü denetliyor. Bu bir semantik doğruluk incelemesi veya bağımsız kaynak yazarlığı doğrulaması değil. Kullanıcının incelemesi için tam system/user metinleri CLI çıktısına yazılıyor; bu çıktı ham görev ve kanıt içeriği içerebilir.

Kaynak: `ortak_kopru/context.py` içindeki `validate_policy`, `_read_snapshot`, `compile_context`, `verify_compiled`, `_verify_source_hashes`; `ortak_kopru/cli.py`; `tests/test_transparent_context.py` içindeki bağlam testleri.

## 3. Onay ve izin: yerel, belirli bağlama bağlı, sınırlı

Örnek politika `allow_provider_call=false`, `allow_network=false`, `allow_write=false`, `tools=[]`, boş sağlayıcı/model izin listeleri ile geliyor. Derleme ve raporlama ağ/anahtar gerektirmeyen yerel işlemler olarak tasarlanmış. `allow_write=false` değerini “program hiçbir yerel dosya yazamaz” şeklinde yorumlamamak gerekir: derlenmiş bağlam, onay ve rapor artefaktları zaten yerel dosya olarak yazılıyor. Yeni yol harici araç çalıştırma uygulamıyor; bu politika alanları işletim sistemi sandbox'ı yerine geçmiyor.

`create_approval`, derlemeyi ve kaynakların güncel hash'lerini doğruluyor; ağ/çağrı iznini, izinli provider/model/reasoning'i ve bütün bilinmeyen katmanların açık kabulünü arıyor. Son kullanma tarihi saat dilimi içermeli, gelecekte olmalı ve `approval_max_minutes` penceresi içinde kalmalı. Onay yalnız belirli context hash'i, politika hash'i, kaynak hash listesi, sağlayıcı/model ve `provider_call` işlemi için yazılıyor. `approve --confirm-reviewed` kullanıcının yerel inceleme beyanı; kimlik teyidi değil.

`verify_approval` çağrı öncesi aynı kapsam/hash/source/izin şartlarını yeniden denetliyor. `consume_approval` aynı onay yolu için exclusive `.used` işaretçisi oluşturarak tekrar kullanımı engelliyor. Belgeler aynı makinede yazma yetkisi olan kişinin onayı veya hash zincirini yeniden yazabileceğini açıkça söylüyor. Bu nedenle “kullanıcı onayı kriptografik olarak kanıtlandı” veya “onayın taklit edilmesi imkânsız” sonucu yanlış olur.

Okumada görülen küçük sözleşme farkı: `create_approval` maksimum geçerlilik penceresini denetlerken `verify_approval`, dosyadan içe alınmış onayın yalnız henüz sona ermediğini denetliyor; orada ayrıca maksimum pencere denetimi yok. Yerel onayın zaten imza/kimlik sınırı taşımadığı belgelenmiş olsa da, “her kabul edilen onayın süresi politika penceresiyle doğrulanır” iddiası kodun tamamı tarafından karşılanmıyor. Bu statik gözlemdir; bu oturumda istismar veya çalışma zamanı deneyi yapılmadı.

Kaynak: `ortak_kopru/context.py` içindeki `create_approval`, `verify_approval`, `consume_approval`; `ortak_kopru/cli.py`; `policy/README.md`; `policy/policy.json`.

## 4. Yeni API yolu: istenen, gönderilen ve gözlenen ayrılıyor

`kopru_yanitla.py` değişikliği `--denetlenebilir`, `--baglam`, `--onay`, `--politika` seçeneklerini ekliyor. Bu yolun seçimi açık; eski varsayılan davranış korunuyor. Denetlenebilir yol tek katman seçimini istiyor, `--kuru` ile birleştirilmiyor. Manifestte `kopru.html` için kanıt rolü ve `ayarlar.json` için yapılandırma rolü aranıyor; kullanılan köprü ve ayar dosyalarının beklenen gerçek yollarla eşleşmesi de denetleniyor.

Derleme ve tam mesajlar hazırlanmış olsa bile onay yoksa bağlam/digest gösterilip harici çağrı yapılmıyor. Onay/kaynak/politika doğrulaması, gerekli ortam anahtarının bulunması, çıktı token sınırı, `max_rounds == 1` ve çağrı öncesi kayıt hazırlığı çağrıdan önce geliyor. Kaynak metinde token benzeri desen saptanırsa dışarı gönderme reddediliyor. CLI adaptörleri, bütün etkili CLI bağlamı görünmediği gerekçesiyle bu yeni yolda desteklenmiyor.

Sağlayıcı çağrısı adaptörleri Anthropic, OpenAI ve Google için ayrı gövde alanları kullanıyor. Anthropic yolunda desteklenmeyen reasoning isteği çağrıdan önce reddediliyor. İstek gövdesinin gerçek JSON bayt hash'i, derlenmiş mesaj hash'inden ayrı kaydediliyor. `allow_fallback=False` ile yeni yol ek model denemesine geçmiyor; eski yolun fallback davranışı ayrı kalıyor.

Kayıt, provider/model/reasoning için istenen, gönderilen ve gözlenen alanları ayırıyor. Sağlayıcı uygulamasının bağımsız doğrulanamadığı yerde `applied`/`observed` bilinmeyen kalıyor. Yanıt içindeki model adı da sağlayıcının döndürdüğü beyan; gerçek altyapı yönlendirmesinin bağımsız kanıtı değil.

Yanıt otomatik olarak `kopru.html` içine eklenmiyor. Ham içerik yerel özel alanda incelemeye bırakılıyor. Hata veya çıktı sınırının aşılması durumunda tekrar ücretli çağrı yapılmıyor; kayıt durumuna göre `failed` veya `recovery_required` kullanılıyor. Çağrı sonrası kayıt hatasının inceleme gerektirebileceği belgelenmiş.

Yanıt boyutu sınırlamasının kapsamı: başarılı HTTP yanıtı `API_RESPONSE_LIMIT` ile parçalı okunup sınırlandırılıyor; hata yolunda `HTTPError` gövdesi `e.read()` ile önce tamamen okunuyor, sonra metin kısaltılıyor. Dolayısıyla “bütün HTTP yanıt gövdeleri okumadan önce aynı bayt sınırına tabidir” iddiası bu diffte desteklenmiyor. Bu da yalnız statik okuma gözlemi; hata sunucusu deneyi yapılmadı.

Kaynak: `kopru_yanitla.py` diffi, özellikle `http_json`, `cagir`, denetlenebilir çağrı yolu ve CLI seçenekleri; ilgili mock HTTP/provider testleri.

## 5. Kayıt zinciri: bütünlük kontrolü, bağımsız değişmezlik değil

`ortak_kopru/runs.py` benzersiz UUID run kimliği oluşturuyor. Özel klasörün symlink olmasına karşı kontroller ve yeni olayın var olan dosyanın üstüne yazmasını engelleyen exclusive yazma var. Geçici dosya fsync ile hazırlanıyor; Windows/POSIX için ayrı sonlandırma yolları bulunuyor. Public olaylar önceki olay hash'i, sıra numarası, durum ve metadata içeriyor. Ham derleme/görev/mesaj/yanıt/hata gövdesi `runs/private/` altında tutuluyor; bu yol `.gitignore` içine ekleniyor.

`verify_runs` olay hash'lerini, sıralamayı, önceki hash bağlantısını ve izinli durum geçişlerini kontrol ediyor. Beklenen akış `ready → attempted → succeeded/failed/recovery_required` veya `ready → skipped`. Ancak son durumun mutlaka tamamlanmış olmasını zorunlu kılmıyor: yalnız `ready` veya sonu `attempted` olan yapısal olarak tutarlı bir zincir için hata üretmeyebilir. Bu nedenle `verify-runs` hatasız çıktısı tek başına “sağlayıcı çağrısı tamamlandı” veya “yanıt başarılı” kanıtı değil. Belgede tamamlanmamış son olayın elle incelenmesi gerektiği yazıyor.

Sır taraması belirli API/token/Bearer benzeri desenlerden oluşuyor. Belgeler bunun sezgisel olduğunu, false negative olabileceğini ve genel kişisel veri/özel bilgi tespiti yapmadığını kabul ediyor. Bu nedenle `public` veya `redacted` kelimesi “her tür özel veri kesin temizlendi” olarak genişletilmemeli. Eski `kayit/` logları ham uygulama istemi ve model yanıtı içeren ayrı bir yol olarak açıkça işaretleniyor; yeni private/public ayrımı geriye dönük olarak onları temizlemiyor.

Klasöre yazabilen kişi tüm zinciri silebilir veya hash'leri yeniden üretebilir. Dış imza/checkpoint yok. Hash zincirinin sağladığı şey mevcut dosyalardaki bağlantı ve bütünlük denetimi; kaynak doğruluğu, bağımsız kimlik veya geçmişin değiştirilemezliği değil.

Kaynak: `ortak_kopru/runs.py` içindeki `_write_exclusive`, `RunStore`, `contains_secret`, `verify_runs`; `policy/README.md`; `.gitignore`; `kayit/README.md`.

## 6. Şahit raporları: sınıflandırma kabı ve kaynak eşleme

`ortak_kopru/reports.py` hazır derlemeyi ve dışarıdan verilmiş şahit verilerini alıyor. Şahitlerin `source_ids` listesinin derlemedeki kaynak hash'lerine ait olması aranıyor. Alanlar `claims`, `interpretations`, `recommendations`, `user_approvals`, `actions`, `uncertainties` olarak ayrı tutuluyor. İçe alınmış metnin gerçekten doğru kategoriye yerleştirildiğini kod semantik olarak sınamıyor.

Eşleştirme, tam çıktı metni eşitliği ve paylaşılan kaynak ID'leri düzeyinde. `epistemic_accuracy` değerlendirilmemiş sayılıyor. JSON çıktısı açıkça şahit verisinin kullanıcı tarafından içe alındığını ve bağımsız sağlayıcı yürütmesinin doğrulanmadığını söylüyor. TXT/HTML, aynı kaynak ve sonuç verilerinin sunumları; HTML metni kaçışlanıyor ve dış kaynağa ihtiyaç duymuyor. TXT/HTML alanlarında JSON'daki provenance uyarısının tamamı tekrar basılmıyor; bu biçimler tek başına paylaşılırsa bağımsız yürütme sınırını ayrıca korumak yararlı olur.

`reports/fixtures/task.txt` ve `witnesses.json` çevrimdışı örnekler. Örnek şahitler açıkça sahte fixture; gerçek Anthropic/OpenAI/Google çalıştırma çıktısı değiller. `--example`/`example=true` etiketi bu ayrımı taşıyor. İki model adı, iki sağlayıcı etiketi veya iki uyumlu çıktı kendi başına bağımsızlık ya da doğruluk kanıtı sayılmamalı.

Kaynak: `ortak_kopru/reports.py`, `reports/fixtures/*`, `policy/README.md`, rapor testleri.

## 7. Şema ve denetim iddialarının dar kapsamı

`policy/policy.schema.json` 218 satırlık JSON Schema sözleşmesi sunuyor. Çalışma zamanı kodu şema dosyasını bir JSON Schema motoruyla değerlendirmiyor; `validate_policy` içinde elle yazılmış kontroller kullanıyor. İki sözleşmenin tamamen aynı olduğu varsayılmamalı.

Statik okumada açık farklar görüldü: `allowed_providers` için liste türü ayrıca aranırken `allowed_models`, `allowed_reasoning`, `allowed_fallbacks` için yalnız elemanların string olması denetleniyor. String bir değer karakterler halinde dolaşıldığından bu kontrolü geçebilir; JSON Schema ise bu alanları dizi ister. Kaynak nesnelerinde de `path`, `role`, isteğe bağlı `max_bytes` dışındaki ek alanları şema reddederken manuel doğrulayıcı açıkça reddetmiyor. Bu not, tam bir güvenlik incelemesi veya istismar doğrulaması değildir; “şema bütünüyle uygulanıyor” iddiasını sınırlayan doğrudan kod gözlemidir.

`checks/steering_lint.py` politikayı yükleyip derleme ve run zinciri kontrollerini çağırıyor. Çıktıda `hidden_steering_detection: false` bulunuyor. Adındaki steering sözcüğü, aracın gizli yönlendirmeyi veya prompt injection yokluğunu tespit ettiği anlamına gelmiyor. Denetlenenler yerel sözleşme, kaynak sınırları ve hash/kayıt özellikleri.

Kaynak: `policy/policy.schema.json`, `ortak_kopru/context.py::validate_policy`, `checks/steering_lint.py`.

## 8. Testler ve CI: ne yazılmış, ne gözlenmemiş?

Diffte toplam **21 `test_...` yöntemi** var. Kapsamları şu gruplarda toplanıyor:

- Tekrarlı derlemenin byte-identik olması, güven rollerinin ayrılığı, kaynak değişince digest değişmesi, CRLF ham kaynak/normalize mesaj ayrımı.
- Yol geçişi, desteklenmeyen şema/encoding/boyut, symlink ve okuma sırasındaki kaynak değişiminin reddi.
- Bilinmeyen katmanların açık gösterilmesi; kabul edilmemiş bilinmeyenle strict reddi; bütün bilinmeyenlerin açık kabulüyle strict derleme.
- Varsayılan çağrı reddi, hash değişince onayın geçersizliği, onayın bir kez tüketilmesi.
- Onay yokluğu, desteklenmeyen Anthropic reasoning, giden metinde token benzeri içerik ve çağrı öncesi kayıt yazamama durumunda adaptörün çağrılmaması.
- Onaylı mock çağrının bir kez kaydedilmesi; yanıtın yerelde kalması; sır benzeri yanıt/hata ve çıktı bütçesi sınırlarının özel alanda ele alınması.
- Eski fallback davranışı ile yeni tek deneme davranışının ayrılığı; mock HTTP başarılı gövdesinin bayt sınırı.
- Eşzamanlı 16 run'ın üstüne yazmaması, sonradan bozulan hash'in yakalanması, özel ham içeriğin public olaya taşınmaması.
- Şahit raporlarının kaynak eşlemesi, HTML kaçışlaması, token desenli girdilerin reddi.
- Eski kontrol/bekleyen listesi yollarının test ortamında salt okunur ve çevrimdışı kalması; workflow metnindeki izin/ağsızlık özellikleri.

Bu testler gerçek sağlayıcı/model yönlendirmesini, gerçek faturalandırmayı, gizli talimat yokluğunu veya model davranışının deterministikliğini doğrulamıyor. Kodda test bulunması testin geçtiği anlamına da gelmiyor; bu okumada test yürütülmedi. `.github/workflows/context-checks.yml`, `contents: read` ile Ubuntu/Python 3.12 üzerinde lint ve unittest çalıştırmayı tanımlıyor. İlgili dosya path filtreleri var. Workflow'un tanımlanması, CI koşusunun gerçekleşmiş/başarılı olduğunun kanıtı değil.

## 9. Belgelerdeki düzeltmeler ve kalan yorum sınırları

`istem-sablonu.md` değişikliği, “uygulamanın kendisinin eklediği talimatlar” kapsamını belirginleştiriyor; sağlayıcının taban istemi, eğitim ve sunucu tarafı katmanlarını bildiğini iddia etmiyor. `kayit/README.md` eski logların ham veri içerdiğini ve sağlayıcının tüm etkili bağlamı olmadığını ekliyor. README yeni opt-in davranışı ve legacy ayrımını anlatıyor.

Mevcut README dosya tablosunda istem şablonu için görünen “modele giden her kelime buradan ve sayfadan gelir” ifadesi, bu diff bağlamında korunmuş. Yeni düzeltmeyle birlikte okunduğunda kapsamı uygulamanın oluşturduğu metinle sınırlamak gerekiyor; sağlayıcıdaki bütün bağlam hakkında kullanılamaz. Bu, eski ifade ile yeni doğruluk sınırının birlikte bulunduğu bir belge tutarlılığı noktasıdır.

`policy/ADR-001.md` içindeki “MVP kabul edildi” ifadesi belgenin kendi durum kaydıdır. GitHub PR'nin `open`, `draft=true`, `merged=false` oluşunu değiştirmez; main'e alınmış, devreye konmuş veya kullanıcıca canlı çağrı için onaylanmış olduğu sonucu çıkarılmamalı. README'deki sabit tarihli onay örneği de yürütülmüş onay değildir.

## 10. Köprüdeki steering tartışmasına katkısı

Bu PR'nin katkısı, “hiç yönlendirme yok” hedefini ispat etmekten ziyade uygulamanın kendi eklemelerini görünür, kaynaklı ve denetlenebilir hale getirme önerisidir. Kayıt/şablon/politika/yerel onay/gerçek API gövdesi birbirinden ayrılıyor. Köprüdeki şu öğrenmelerle uyumlu okunabilir:

- `k-0014` ve `k-0016`: kaynak metni, yorum, onay ve tamamlanmış eylem farklı şeylerdir; bir öneriyi çalıştırma talimatına çevirmemek gerekir.
- `k-0027`, `k-0029`: ayar veya dosya varlığından davranışın uygulanmış olduğuna sıçranmamalıdır.
- `k-0049`–`k-0055`: commit zamanı, okuma sahipliği, harici sayaç ve bağımsız ölçüm sınırları korunmalıdır.
- PR içindeki şahit raporu, aynı kaynağı iki kez söylemenin bağımsız yeni kanıt olmadığı ayrımına uygundur; canlı sağlayıcı bağımsızlığı ayrıca gösterilmelidir.

Burada tarihsel köprü görevleri yürütülmedi. PR'nin açıklaması veya kod içindeki iş emirleri mevcut kullanıcı talimatına yükseltilmedi. Bu dosya, güncel araştırma ve aktarımın PR #3 okuma kaydıdır.

## 11. Tam diff okuma envanteri

| Sıra | Dosya | Okunan kapsam / esas katkı |
|---:|---|---|
| 1 | `.github/workflows/context-checks.yml` | Tam yeni dosya; salt okunur lint/test workflow tanımı. |
| 2 | `.gitignore` | Diff; `runs/private/` eklemesi. |
| 3 | `README.md` | Tüm diff ve gösterilen bağlam; legacy ve opt-in kullanım açıklamaları. |
| 4 | `checks/steering_lint.py` | Tam yeni dosya; yerel politika/derleme/run denetimi. |
| 5 | `istem-sablonu.md` | Diff; uygulama talimatı kapsamının daraltılması. |
| 6 | `kayit/README.md` | Diff; legacy ham log ve görünürlük sınırı. |
| 7 | `kopru_yanitla.py` | Tüm diff ve gösterilen bağlam; API metadata, sınırlar, yeni opt-in yol. |
| 8 | `ortak_kopru/__init__.py` | Tam yeni dosya; paket tanımı. |
| 9 | `ortak_kopru/cli.py` | Tam yeni dosya; compile/approve/verify/verify-runs/witness komutları. |
| 10 | `ortak_kopru/context.py` | Tam yeni dosya; politika, kaynak snapshot'ı, derleme, onay. |
| 11 | `ortak_kopru/reports.py` | Tam yeni dosya; içe alınmış şahit raporu, üç çıktı biçimi. |
| 12 | `ortak_kopru/runs.py` | Tam yeni dosya; özel ham kayıt, public olay zinciri ve kontrolü. |
| 13 | `policy/ADR-001.md` | Tam yeni dosya; karar, sınırlar, kapsam dışı ve geri alma. |
| 14 | `policy/README.md` | Tam yeni dosya; bütün sözleşmeler, bilinmeyenler ve komut örnekleri. |
| 15 | `policy/application-instructions.md` | Tam yeni dosya; uygulama talimatı kaynağı. |
| 16 | `policy/policy.json` | Tam yeni dosya; varsayılan kapalı örnek politika. |
| 17 | `policy/policy.schema.json` | Tam yeni dosya; JSON Schema sözleşmesi. |
| 18 | `reports/fixtures/task.txt` | Tam yeni dosya; çevrimdışı sahte görev. |
| 19 | `reports/fixtures/witnesses.json` | Tam yeni dosya; sahte şahit girdileri. |
| 20 | `tests/test_transparent_context.py` | Tam yeni dosya; yardımcı fixture'lar ve 21 test yöntemi. |

Sabit head kaynak ağacı: <https://github.com/HalukAINRS/ortak-kopru/tree/3c80c8b20e1c0a9d51779c197f9188d3b750d050>. Ana uygulama incelemeleri için dosya bağlantıları: [context.py](https://github.com/HalukAINRS/ortak-kopru/blob/3c80c8b20e1c0a9d51779c197f9188d3b750d050/ortak_kopru/context.py), [runs.py](https://github.com/HalukAINRS/ortak-kopru/blob/3c80c8b20e1c0a9d51779c197f9188d3b750d050/ortak_kopru/runs.py), [reports.py](https://github.com/HalukAINRS/ortak-kopru/blob/3c80c8b20e1c0a9d51779c197f9188d3b750d050/ortak_kopru/reports.py), [policy/README.md](https://github.com/HalukAINRS/ortak-kopru/blob/3c80c8b20e1c0a9d51779c197f9188d3b750d050/policy/README.md), [test dosyası](https://github.com/HalukAINRS/ortak-kopru/blob/3c80c8b20e1c0a9d51779c197f9188d3b750d050/tests/test_transparent_context.py).

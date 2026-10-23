# Governed bağlam ve çalıştırma kaydı (ADR-001)

## Amaç ve sınır

Bu, mevcut çevrimdışı okunabilir Köprü'nün yanındaki açıkça seçilen bir MVP yoludur. Amaç sıfır yönlendirme ya da sıfır güvenlik mekanizması vaadi değildir. Uygulamanın eklediği kaynakları, rollerini, sürümünü, onayını, derlenmiş mesajlarını ve gözleyebildiği sonuçları denetlenebilir kılar. Üretici/CLI taban istemleri, eğitim, sunucu tarafı güvenlik ve yönlendirme, deneyler ve telemetri bu araçla bütünüyle görülemez. Manifest bunları `unknown` veya `partial` yazar; yok olduklarını varsaymaz.

Hash, yalnız belirli baytların içerik eşleşmesini kontrol etmeye yarar. Hash; yazanın kimliğini, kullanıcı onayını, doğruluğu, güvenliği, sağlayıcının gerçekte ne işlediğini veya model deterministikliğini kanıtlamaz. İki modelin aynı şeyi söylemesi doğruluk kanıtı değildir. Gizli sistem talimatlarını çıkarmaya ve onay, güvenlik veya sandbox katmanlarını etkisizleştirmeye çalışılmaz.

## Dosya ağacı ve kararlar

```text
kopru_governance/
  core.py                 policy doğrulama, sabit snapshot ve mesaj derleme
  execute.py              tek çağrılık fail-closed kapı
  runs.py                 yerel, salt-eklemeli JSONL olay zinciri
  witness.py              kaynak bağlı rapor ve güvenli TXT/HTML/JSON
  cli.py                  çevrimdışı derleme, doğrulama, dışa aktarma ve demo
policy/
  policy.json             default-deny örnek/başlangıç politikası
  policy.schema.json      sürümlü politika sözleşmesi
  approval.schema.json    tek işlem için yerel onay sözleşmesi
  manifest.schema.json    derleme manifesti sözleşmesi
  run-event.schema.json   olay zinciri sözleşmesi
examples/
  approval.example.json   sahte kapsam hash'leri; gerçek onay değildir
  witness-import.schema.json
tests/test_governance.py  ağsız geçici-dosya ve sahte-adapter testleri
checks/steering_lint.py   doğrulanabilir yerel kontroller
.github/workflows/steering-lint.yml
                          ayrı, contents: read, sır/model çağrısı olmayan CI
```

**ADR-001:** Standart kütüphaneyle `kopru_governance` namespace'i seçildi; Python'ın genel `compiler` adıyla çakışma yok. Legacy varsayılanı sessizce değiştirmek yerine güvenli yol opt-in. Mevcut `kopru.html`, geçmiş katılımcı kayıtları ve `kopru.yml` otomasyonu bu değişiklikte değiştirilmez. Yeni yol bu MVP'de yalnız açıkça seçilen tek API provider/model çağrısını destekler; CLI komutları, araç çalıştırma ve köprüye otomatik yazma desteklenmez.

## Veri sözleşmesi ve derleme

Politika `schema_version: 1` taşır. Kaynaklar repository-relative POSIX yolları ve açık rollerle bildirilir:

- `application_instruction`: yalnız politika açıkça listeler ve `transmit: true` ise system rolüne eklenir.
- `untrusted_evidence`: system rolüne asla terfi etmez. `transmit: true` ise kullanıcı mesajında kaynak ID'siyle veri olarak verilir; `false` ise sadece manifestte hash/provenance taşır.
- `user_task`: çağrıdan gelen ayrı görev metni. Bekleyen Köprü kayıtları governed entegrasyonunda ayrı `generated-evidence-*` kaynağıdır; görev değil, güvenilmeyen veridir.

Derleyici yinelenen JSON anahtarını, bilinmeyen şemayı/uzantıyı, UTF-8 dışı/BOM dosyayı, traversal'ı, symlink'i, kök dışı dosyayı ve dosya/toplam boyut sınırını reddeder. Satır sonu `LF`'ye normalize edilir. Kaynaklar ve politika derleme sonunda yeniden okunur; arada değişiklik fark edilirse iptal edilir. JSON hash'i UTF-8, `ensure_ascii=False`, sıralı anahtarlar ve sabit ayraçlarla hesaplanır. Derleme manifestine değişken zaman damgası girmez. Git yoksa commit ve worktree durumu `unknown`; varsa commit hash'i ile ilgili kaynakların temiz/kirli durumu yazılır.

Manifest, kaynak/politika/context/message hash'lerini, kullanıcı tarafından istenen provider/model/efor/limitleri, uygulanan kaynak rollerini ve görünürlük durumunu taşır. `messages_sha256` API'ye verilen mesaj nesnelerinin kanonik hash'idir. Governed HTTP adaptörü gerçek JSON request body baytlarını serialize eder, ağ isteğinden hemen önce `request_body_sha256` ve yalnız hedef host/path bilgisini kayda ekler. Kimlik doğrulama başlığı hash'lenmez/kaydedilmez. CLI normal tek-istem aktarımı bu MVP'de desteklenmediğinden onun gerçek aktarımına ilişkin iddia kurulmaz. Plan çıktısı çağrıdan önce tam gönderilecek iki mesajı gösterir.

`visibility.mode` `limited` veya `strict` olabilir. Bu sürümde provider güvenlik/sistem katmanı, sunucu yönlendirmesi/telemetri ve eğitim bilinmeyen katmanlardır; politika bunları açıkça kabul etmelidir. `limited` manifest uyarı üretir. `strict`, kabul edilmeyen belirsizlikte derlemeyi reddeder. Kabul kaydı, belirsizliği ortadan kaldırmaz; kullanıcıya ait yerel politika dosyası güven sınırıdır.

## İrade, onay ve yürütme

Varsayılan politika `network: false`, `write: false`, `allowed_providers: []`, `allowed_tools: []` ve `max_calls: 1` kullanır. Bu nedenle canlı çağrı yapılamaz. Canlı API için kullanıcı politika içindeki ağı ve tam provider/model çiftini açıkça etkinleştirmeli, `--plan-governed` ile mesajları incelemeli, sonra bir approval JSON dosyasında `provider_call`, politika hash'i, context/source hash'leri ve son kullanma zamanını onaylamalıdır. Hash veya görev değişikliği onayı geçersiz kılar. `approved_by` yalnız kullanıcının yazdığı etikettir; uygulama kimliği doğrulamaz, imza üretmez ve yerel dosya sahibinden bağımsız onay kanıtı sunmaz. Örnek approval hash'leri sahte olup hiçbir çalıştırma için kullanılamaz.

Ön-kayıt ve approval kontrolünden önce anahtar okunmaz ve provider çağrılmaz. Onay en fazla 24 saat geçerlidir. Sonra tek API isteği yapılır; request/response gövdeleri 16 MiB ile sınırlıdır, otomatik retry, reasoning downgrade veya yedek yola sessiz geçiş yoktur. İstek gönderimi kaydedildikten sonra timeout/hata sonucu belirsiz kalırsa run `recovery_required` olur ve yeniden denenmez. API yanıtındaki model etiketi provider-bildirimi olarak kalır; provider yönlendirmesi ve uygulanan reasoning seviyesi doğrulanamıyorsa `unknown` yazılır. Mevcut ayar adları üretici tarafından güncel/doğrulanmış yetenek iddiası değildir. Claude benzeri primary/fallback rotalarda yedek ancak `--governed-route fallback` ile açık seçilir. CLI seçilirse bu MVP çağrı yapmadan `skipped` kaydı üretir.

Bu mod Köprü HTML'ine yanıt eklemez ve çalışma dosyalarını otomatik commit etmez. Provider çıktısı sonradan insan incelemesi için `runs/private/` altında saklanır; yazım için ayrı bir onay/kapı henüz uygulanmamıştır. Bu yüzden `write` izni bu MVP'de `false` kalmak zorundadır.

## Run kayıtları, redaksiyon ve kurtarma

Her çağrı için `runs/<random-id>.jsonl` O_EXCL ile ayrılır; özel bağlam ve ham provider çıktısı `runs/private/` altında tutulur. Her olay önceki hash'i, sıra numarasını ve olay hash'ini taşır; verifier bozuk satır/zinciri reddeder. Run dosyaları varsayılan olarak `.gitignore` içindeki `/runs/` sayesinde yerelde kalır; yerel ACL/disk şifrelemesi ve dosya izinleri işletim sisteminin sorumluluğundadır. `0o600`/`0o700` en iyi çabadır; Windows'ta aynı ACL garantisi olarak sunulmaz. Bu kayıtlar immutable değildir: yazma yetkisi olan biri içeriği ve bütün zinciri yeniden üretebilir. Bağımsız imzalı/checkpoint edilmiş bir baş hash yoktur.

Provider çağrısından sonra kayıt yazımı başarısızsa kör retry yapılmaz; bu ikinci ücretli çağrıya neden olabilir. Olay `attempted` durumda kalabilir veya `recovery_required` olur; çıktı ve işlem durumu operatörce sağlayıcıdan ayrıca kontrol edilmeden yeniden çalıştırılmamalıdır. HTTP hata gövdeleri governed yolda kayda alınmaz. Run ledger tam prompt/çıktı, environment variable değerleri veya auth başlıklarını içermez; özel bundle/çıktı yerel ignored dosyalardadır. Run public export'u yalnız izin listeli hash/lifecycle/model metadata'sı üretir. Cross-witness raporu common token/key/IP desenlerini redakte eder ve HTML metnini escape eder. Desen taraması false-negative üretebilir; bu bir sır bulunmadığının kanıtı değildir. Redaksiyon gerekirse ham özel içeriği yayınlamak yerine yayınlama durur veya alan redakte edilir. Hiçbir ham kayıt otomatik olarak `git add` edilmez.

## Cross-witness raporu

İki veya daha fazla içe aktarılan çıktı aynı `context_hash`'i ve derlenmiş kaynak ID'lerini taşımalıdır. Şema kanıt, yorum, öneri, kullanıcı onayı, gerçekleşen işlem ve belirsizlik kategorilerini ayırır. TXT, dış kaynak/script içermeyen statik HTML ve JSON aynı kaynak ID/hash'lerini taşır. Eşleşen/ayrışan metin yalnız karşılaştırmadır; kaynak gerçeğini veya epistemik doğruluğu ispatlamaz. `witness-demo` açıkça fixture-only rapor üretir; canlı model çağırmaz.

## Kullanım, denetim ve rollback

Repo kökünden:

```bash
python -m kopru_governance.cli compile --root . --task "Görevi çevrimdışı değerlendir." \
  --output runs/plans/review.json
python -m kopru_governance.cli approval-template --bundle runs/plans/review.json \
  --output runs/plans/review.approval.json
python checks/steering_lint.py --root .
python -m unittest discover -s tests -v
python -m kopru_governance.cli witness-demo --bundle runs/plans/review.json \
  --output-prefix /tmp/ortak-kopru-demo/report
```

`kopru_yanitla.py kopru.html --yalniz ChatGPT --plan-governed` mevcut bekleyen kayıtları seçer, tam mesajları stdout'ta gösterir ve `runs/plans/` altına yerel plan/onaysız şablon yazar. Önce kaynakları, gönderilecek iki mesajı, provider/model rotasını ve kabul edilmiş bilinmeyen katmanları insan incelemelidir. Yalnız sonra politika izin veriyorsa `--governed --approval runs/plans/<context-hash>.approval.json` tek çağrı yapabilir. Gerçek çağrı için uygun çevre anahtarının önceden ayarlanmış olması gerekir; CI, dry-run ve plan bunu istemez/okumaz. Bu repo için politika varsayılanı canlı provider izni vermediği için açık yerel politika değişikliği olmadan bu komut `skipped` olur.

Legacy `kopru_yanitla.py` çağrıları/CLI'ları, `--kuru`, `--istem`, `--bekleyenler`, mevcut otomasyon ve `kopru.yml` geri dönüş yolu olarak korunur. Legacy yol `kayit/` altına tam uygulama promptu/ham yanıt yazmaya ve kendi fallback mantığına devam eder; yeni güven sınırlarını sağlamaz. Yeni modu kapatmak için governed bayraklarını kullanmayın ve eski komut biçimini sürdürün; policy, `runs/` ve yeni test/workflow dosyaları eski kayıt sayfasına dokunmadan kaldırılabilir. `kopru.html` ve geçmiş katılımcı kayıtları bu uygulamada değiştirilmedi. Windows `Kopru_Izle.cmd` / yerel katman entegrasyonu bu Linux çalıştırma ortamında doğrulanmamıştır.

`steering-lint` yalnız politika şekli, bütünlük, kaynak provenance'ı, tekrar üretilebilirlik, yerel ignored run kayıtları ve test edilebilir onay kapılarını kontrol eder. Gizli yönlendirmeyi saptadığını iddia etmez. Yeni CI `contents: read` kullanır; secret istemez, sağlayıcı/model/CLI çağrısı yapmaz ve sahte fixture'larla çalışır.

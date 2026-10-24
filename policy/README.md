# Denetlenebilir bağlam MVP'si

Bu altyapı, uygulamanın **gönderdiği** bağlamın kaynağını, içeriğini, politikasını, kullanıcı onayını ve çağrı sonucunu izler. “Hiçbir görünmez talimat çalışmaz” garantisi vermez. Sağlayıcı/CLI taban istemleri, eğitim, sunucu tarafı yönlendirme/güvenlik ve telemetri bütünüyle görünür değildir. Manifest bu bilinmeyenleri açıkça taşır. Hash eşleşmesi bayt bütünlüğü kontrolüdür; yazar kimliği, doğruluk, güvenlik veya model deterministikliği kanıtı değildir. İki çıktının uyumu da doğruluk kanıtı sayılmaz.

## Dosya ağacı ve sözleşmeler

```text
ortak_kopru/                 Standart kütüphane derleyici, yerel onay, run ve rapor kodu
policy/policy.json           Sürümlü, default-deny örnek politika
policy/policy.schema.json    JSON Schema sözleşmesi
policy/application-instructions.md
                             Yeni derleyicinin uygulama talimatı kaynağı
policy/ADR-001.md            Mimari karar
runs/<run-id>.<seq>.json     Ham içerik içermeyen, hash-zincirli olaylar
runs/private/                Ham bağlam/yanıt/onay/artefakt; gitignore'da
checks/steering_lint.py      Yalnız doğrulanabilir şema/provenance/hash/run kontrolleri
reports/fixtures/            Açıkça sahte çevrimdışı görev ve çapraz-şahit çıktıları
tests/                       Ağsız stdlib unittest testleri
```

`policy.json` kaynakları görevlere göre rol ve dosya sınırıyla listeler. Roller: `application_instruction`, `user_task`, `untrusted_evidence`, `configuration`. Derleme kaynağı ve görev baytlarını UTF-8 olarak doğrular, UTF-8 JSON sözdizimini kontrol eder, kararlı yol sırası/canonical JSON/newline kullanır ve snapshot sırasında kaynak değişirse reddeder. Mutlak yol, `..`, kök dışı symlink, desteklenmeyen dosya türü/encoding ve byte limitleri reddedilir. Git yoksa commit provenance `unknown` olur. Derleme hash'ine timestamp girmez; run olaylarının zamanları ayrı tutulur.

Kanıt HTML'si ve içindeki kayıtlar `untrusted_evidence` olarak kalır. Komut/rol talimatı gibi görünen kanıt metni derleyici tarafından yetkili talimata dönüştürülmez. Bu sınır prompt injection yokluğunu ispatlamaz. Üretilen manifest ve API adaptörüne verilecek system/user içerikleri provider çağrısından önce tam olarak gösterilir. Manifestte git HEAD provenance baseline'ı ve her kaynak baytının SHA-256 özeti ayrıdır; uncommitted içerik hash'lenir ama HEAD commit'inde olduğu ileri sürülmez. API gövdesinin gerçek UTF-8 JSON bayt hash'i ile derlenmiş mesaj hash'i aynı run olayında tutulur. CLI sarmalayıcısının sisteme/kullanıcıya ait iki alanı normal isteme birleştirmesi gibi aktarım farkları varsa yalnız fiili uygulama davranışı kaydedilebilir; sağlayıcının tüm etkili bağlamı olduğu iddia edilmez.

## İzin, belirsizlik ve onay

Başlangıç politikası `allow_provider_call=false`, `allow_network=false`, `allow_write=false`, `tools=[]`, izinli sağlayıcı/model yok şeklindedir. Böylece derleme, doğrulama, rapor ve dry-run ağ veya anahtar gerektirmez. Canlı API için kullanıcı politika dosyasında sağlayıcı/modeli, reasoning düzeyini, ağ/çağrı iznini ve kabul edilen `layers.accepted_unknown` listesini açıkça değiştirmelidir. Değişiklik politika hash'ini değiştirir.

Normal sınırlı görünürlük manifestte `partial` uyarısı taşır. Çağrı öncesi onay ancak bu örnekte listelenen tüm bilinmeyen katmanlar (sağlayıcı sistem istemi, eğitim, sunucu yönlendirmesi, telemetri) açıkça kabul edilmişse mümkündür. Strict mod, bilinmeyen/ kabul edilmemiş katman varken derlemeyi reddeder. Belirsizliği kabul etmek gizli davranışı görünür yapmaz.

Akış:

1. Kullanıcı görevi dosyasını ve iki mesajı `compile` ile üretir; tam mesajları inceler.
2. Bilinmeyen katmanları ve harici çağrı sınırını kabul ediyorsa `approve --confirm-reviewed` ile yalnız bu context SHA-256, kaynak/politika hash'i, provider/model, `provider_call` işlemi ve kısa expiry için yerel onay yaratır.
3. `kopru_yanitla.py --denetlenebilir` bağlam/onayı tekrar doğrular; run kaydını ve özel ham içeriği sağlayıcı çağrısından önce yazamazsa fail-closed durur.
4. Bu yol tek doğrudan API çağrısı yapar; provider/model ve reasoning requested/sent/applied/observed alanlarını ayırır. `applied` sağlayıcıdan doğrulanamadığında `unknown` kalır. Fallback uygulanmaz. API yanıtı otomatik `kopru.html` içine yazılmaz; ham içerik yerelde incelenir. CLI adaptörleri henüz desteklenmez.

`approved: true` yalnız yerel onay dosyasındaki bir kayıttır; kimlik doğrulaması, kriptografik imza veya bağımsız kullanıcı kanıtı değildir. Aynı makinede dosyayı değiştirebilen kişi bu onayı ve event zincirini yeniden yazabilir. Bağımsız dış checkpoint yoksa zincir/hash baştan üretilebilir. Onay ilk sağlayıcı denemesinden önce atomik şekilde bir kez tüketilir. Politika, kaynak veya görev değişirse onay geçersiz olur.

## Çalıştırma kaydı ve sır sınırı

Run ID UUID'dir; olay dosyaları exclusive, atomik tamamlanan create ile yazılır ve var olan olayın üzerine yazılmaz. Her olay önceki olay hash'ine bağlıdır; `verify-runs` hash ve izinli durum geçişlerini doğrular. Bu “immutable” garantisi değildir; yazma izni olan kişi kayıtları silebilir veya yeniden zincirleyebilir. Kayıt hatası çağrıdan önce çağrıyı engeller. Çağrıdan sonra kayıt hatası olursa ikinci ücretli çağrı körlemesine yapılmaz; `recovery_required` aranır, tamamlanmamış son olay elle incelenir.

Ham görev, mesaj, çıktı ve provider hata gövdesi yok sayılan `runs/private/` altındadır; bu klasör gitignore'a eklenmiştir. Public run olayları redakte edilmiş metadata/hash içerir. Token desen taraması yalnız sezgiseldir, false negative olabilir ve kişisel verileri/özel bilgileri genel olarak tanımaz. Tarama eşleşmesinde ham içerik public event/rapora yazılmaz. Eski `kayit/` logları ayrı bir legacy yoldur: uygulama istemi ve ham model yanıtı içerir, bu yüzden otomatik olarak redakte edilmiş sayılmaz. Üretici taban istemi hiçbir run kaydına dahil değildir.

## Denetimler, demo ve geri alma

```bash
python checks/steering_lint.py
python -m unittest discover -s tests -v
python -m ortak_kopru.cli compile --task-file reports/fixtures/task.txt
python -m ortak_kopru.cli verify-runs
python -m ortak_kopru.cli witness \
  --artifact runs/private/prepared/<context-sha256>.json \
  --input reports/fixtures/witnesses.json \
  --output /tmp/kopru-witness --example
```

Demo raporunun TXT/HTML/JSON biçimleri aynı context/source ID'lerini içerir. HTML kaçışlanmış ve dış kaynaksızdır; örnekler `example: true` ile sahte fixture olarak işaretlenir. Kanıt/yorum/öneri/onay/eylem alanları ayrıdır. Bu raporlayıcı görüş birliği veya otomatik metin benzerliğinden doğruluk çıkarmaz; öneri iş emri değildir.

`steering_lint` yalnız policy/schema türleri, kaynak sınırları, hash/provenance ve run zincirini kontrol eder; gizli steering'i, prompt injection yokluğunu veya model davranışını tespit ettiğini iddia etmez. Ayrı CI workflow yalnız sahte fixture kullanır; model/API/CLI çağırmaz, secret okumaz ve `contents: read` dışında izin istemez.

Geri alma: `--denetlenebilir` ve `ortak_kopru` komutlarını kullanmayı bırakın. Legacy `kopru_oku.py`, `kopru_ekle.py`, `kopru_yanitla.py` varsayılanı ve `kopru.html` değişmeden kalır. Yeni opt-in çalıştırmalar legacy ile karıştırılmamalı; ham özel kayıtlar repoya eklenmemelidir.

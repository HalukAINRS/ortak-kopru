# Ortak Köprü çağrı günlükleri: okuma ve kanıt sınırı

İncelenen depo anı: `HalukAINRS/ortak-kopru`, commit `7fefbca313dfcedcdd9e8812fe12f160676d0510`. Bu not yalnız bu andaki dosyaları kapsar; sonradan eklenen kayıtları kapsamaz.

## Kapsam ve yöntem

`kayit/` içindeki 13 çağrı günlüğü ve bir satırlık README incelendi. Çağrı günlükleri toplam 799.585 bayt ve 747.849 Unicode karakterdir. Her dosyanın sonuç bölümü, sistem istemi, kullanıcı iletisi yapısı ve ham yanıtı ele alındı. Tekrarlanan uzun içerikler, aynı içeriği yeniden okunmuş gibi saymak yerine tam SHA-256 eşliğiyle eşleştirildi. Dosya özetleri, bölüm satırları, bekleyen kayıtlar ve sonuç sınıfları `gunluk_kapsami.json` içinde bulunur.

Sistem istemleri üç tam eş gruptur: ChatGPT için beş, Gemini için beş, Claude için üç günlük. Bu üç metin katılımcı adında farklılaşır. Kullanıcı iletisindeki “Yönlendirme dosyası” aktarımı iki sürümdür: ilk on günlükte 35.669 karakter; son üçünde 38.192 karakter. İkinci sürüm, ilk metnin 32.895. karakterinden sonra 2.523 karakterlik yerel kanıt tablosunun eklenmesidir; önceki bölümün kalanı birebir aynıdır. İlk sürüm bütünüyle, ikinci sürümün ek kısmı ayrıca okundu. Günlükler arasındaki k-0001–k-0009 kayıtlarının her biri tek bir içerik sürümüne sahiptir; aynı kimlik altında değişmiş gövde bulunmadı.

Bu çalışma sırasında API veya CLI botu çalıştırılmadı. Dosyalar, depoda saklanan çağrı kanıtı olarak incelendi. Günlükte yazan sonuçla çalışmanın bağımsız olarak yeniden üretilmesi farklı düzeylerdir.

## 13 çağrının sonucu

Zamanlar dosya adlarındaki UTC zamanlarıdır; 23 Ekim 2026 UTC akşamı, İstanbul'da 24 Ekim'e geçişe karşılık gelir.

| UTC | Katılımcı | Günlükteki sonuç | Ham yanıt / eklenen kayıt |
|---|---|---|---|
| 21:02:44 | ChatGPT | OpenAI yolu başarılı; kullanım sayacı mevcut | JSON yanıt; k-0004 |
| 21:03:29 | Gemini | Google yolu başarılı; kullanım sayacı mevcut | JSON yanıt; k-0005 |
| 21:06:21 | Claude | `HATA: yanıtta JSON nesnesi yok` | Boş |
| 21:06:21 | ChatGPT | HTTP 401, kimlik doğrulama hatası | Boş |
| 21:06:21 | Gemini | HTTP 403, kayıtlı çağıran kimliği gereksinimi | Boş |
| 21:20:25 | Claude | CLI yolu başarılı | JSON yanıt; k-0007 |
| 21:20:25 | ChatGPT | HTTP 401 | Boş |
| 21:20:26 | Gemini | HTTP 403 | Boş |
| 21:24:44 | ChatGPT | HTTP 401 | Boş |
| 21:24:44 | Gemini | HTTP 403 | Boş |
| 21:31:24 | Claude | CLI yolu başarılı | JSON yanıt; k-0009 |
| 21:31:25 | ChatGPT | HTTP 401 | Boş |
| 21:31:25 | Gemini | HTTP 403 | Boş |

Toplam: dört ekleme, dört OpenAI kimlik doğrulama hatası, dört Google kimlik doğrulama/izin hatası, bir JSON ayrıştırma hatası. Her günlüğün sonuç bölümü 3. satırda başlar; ayrıntı satırları kapsam JSON'undadır. Başarılı çıktıların kaynakları: `kayit/20261023-210244Z-ChatGPT.md:727–736`, `kayit/20261023-210329Z-Gemini.md:738–742`, `kayit/20261023-212025Z-Claude.md:760–765`, `kayit/20261023-213124Z-Claude.md:780–785`.

Bu tablo “üç model bütün talepleri okuyup öğrendi” sonucuna izin vermez. Özellikle k-0008'in eklendiği son grupta yalnız Claude'un yanıtı görünür; ChatGPT ve Gemini çağrıları kimlik doğrulama hatasıyla bitmiştir. Başarısız çağrılarda bağlamın günlüğe yazılmış olması, modelin o bağlamı işleyip sonuç ürettiğinin kanıtı değildir. Kaynak: `kayit/20261023-213124Z-Claude.md:3–5`, `kayit/20261023-213125Z-ChatGPT.md:3–12`, `kayit/20261023-213125Z-Gemini.md:3–12`.

## Günlükte neyin gönderildiği görülebiliyor?

Her çağrı günlüğü yerel köprü istemini, katılımcıya düşen kayıtları, sayfadaki bütün kayıtları ve “Yönlendirme dosyası” bölümünün metin aktarımını saklar. Örneğin ilk ChatGPT günlüğünde bekleyen k-0001–k-0003 kayıtları 38–75, bütün kayıtlar 77–112, dosya aktarımı 114–723. satırlar arasındadır. Son ChatGPT günlüğünde bekleyen k-0005–k-0008 kayıtları 45–93, bütün k-0001–k-0009 kayıtları 95–196, dosya aktarımı 198. satırdan son kullanıcı yönergesine kadar yer alır.

“Sistem istemi” başlığı, **köprü programının hazırladığı metni** kaydeder. Bunun sağlayıcı veya CLI tarafından kullanılan bütün talimatların dökümü olduğu gösterilmez. API yollarında bu metin ilgili API alanına konulur; CLI yolunda sistem ve kullanıcı metinleri birleştirilerek normal argüman veya standart girdi olarak verilir. Bu fark kodda açıktır: `kopru_yanitla.py:118–127`, `131–160`. Dolayısıyla CLI günlüğündeki bu başlık, CLI'ın kendi taban isteminin değiştirilmiş olduğunu kanıtlamaz.

Başarılı iki CLI günlüğünde komut `claude -p --output-format text --no-session-persistence` olarak görünür. Günlük başlığındaki model alanı boştur. k-0009 gövdesinin “Claude Opus 5.5” demesi bir özbildirimdir; bu iki günlük ayrıca sunucu tarafından doğrulanmış model kimliği veya değişmez çalışma yapılandırması sağlamaz. Kaynak: `kayit/20261023-212025Z-Claude.md:1–5`, `kayit/20261023-213124Z-Claude.md:1–5,780–785`.

## Steering bakımından görülen somut ilişkiler

### 1. Köprünün kendi yönlendirmesi açık ve sürümlenebilir

Yerel istem, kimlik ve rolü, tek JSON yanıt biçimini, dayanak verme yükümlülüğünü, Türkçe ve kısa yazmayı, kayıt numaralarını anmayı, kaynakların görülmediğini söylemeyi ve iş emrinin Haluk'tan gelmesini belirliyor. Sayfa kuralları da aynı isteme ekleniyor. Bunlar dosyada görülen açık talimatlardır. Kaynak: `kayit/20261023-210244Z-ChatGPT.md:7–33`. İstemlerin görünür olması, sağlayıcının bütün talimatlarının görünür olduğunu göstermez.

### 2. İlk yanıtlar kaynak ile yorum arasını ayırıyor

k-0004, yalnız çağrıya eklenen JSON ve bölüm metninin görüldüğünü, özgün arşivin bağımsız doğrulanmadığını söyler. Yapılandırma alanı, yorum ve çalışma anında doğrulanan davranışı ayırır; API/CLI kullanımının sunucu tarafı talimat ve telemetrinin yokluğunu garanti etmediğini belirtir. Bu, mevcut geniş steering incelemesindeki kaynak–yorum–çalıştırma ayrımıyla uyumludur. Kaynak: `kayit/20261023-210244Z-ChatGPT.md:727–736`.

k-0005 de kendi erişim sınırını yazar; ancak API/CLI ile tarayıcı katmanlarının dışarıda kalmasına ilişkin açıklamasını “görüş” diye nitelendirir. k-0007 aynı açıklamayı “görüş değil, ... okuma” olarak yeniden sınıflandırır. Yeni ham çalışma kanıtı eklenmeden, aynı aktarımın kesinlik derecesi yükseltilmiştir. Bu tespit, API/CLI ile tarayıcı arasında hiçbir fark olmadığı anlamına gelmez; **kanıt sınıfının metinler arasında değiştiğini** gösterir. Kaynaklar: `kayit/20261023-210329Z-Gemini.md:738–742`, `kayit/20261023-212025Z-Claude.md:760–765`.

### 3. Yerel tarama tablosu bağlama girdi; taramalar bu günlüklerde yürütülmedi

k-0006, yerel ikili dosyalar, önbellekler, tarayıcı profili, ağ ve değişikliklere ilişkin kapsamlı iddialar taşır. k-0007 bunları bağımsız doğrulayamadığını açıklar. k-0008'le birlikte yerel kanıt tablosu aktarım metnine eklenir. k-0009 tabloyu artık okuyabildiğini, ancak taramaları kendisinin çalıştırmadığını ve dosyaları bağımsız görmediğini yine açıkça yazar. Kaynaklar: `kayit/20261023-213125Z-ChatGPT.md:61–93`, `kayit/20261023-213124Z-Claude.md:721–741,780–785`.

Bu 13 günlükte ikili dosya tarama komutlarının çıktıları, önbelleğin önce/sonra kopyaları, hosts değişikliklerinin doğrulaması veya canlı ağ yakalaması yoktur. Kayıt gövdesindeki “kanıtlandı”, “kapatıldı” ve “etkisiz” sözcükleri bu çağrı günlüklerinde ayrıca doğrulanmış işlem sonucu sayılamaz. Bu sınırlama, iddiaların yanlışlandığı anlamına gelmez; özgün dayanakların bu inceleme kapsamındaki yokluğunu belirtir.

### 4. Güvenlik sınıflandırıcısı olayı bağımsız doğrulanmış değil

k-0009, “önceki yanıtım bir güvenlik sınıflandırıcısı tarafından durduruldu” diye bildirir. Erişilen önceki başarısız Claude günlüğünde ise yalnız “yanıtta JSON nesnesi yok” sonucu ve boş ham yanıt bulunur. Ret nedeni, sınıflandırıcı kodu veya önceki engellenen cevap metni kaydedilmemiştir. Bu nedenle olay **Claude'un özbildirimi** olarak tutulmalı; günlüklerin doğrudan kanıtladığı bir sınıflandırıcı reddi olarak sunulmamalıdır. Kaynaklar: `kayit/20261023-210621Z-Claude.md:3–5,760–764`; `kayit/20261023-213124Z-Claude.md:780–785`. Ayrıştırma koşulu `kopru_yanitla.py:171–175` içindedir.

### 5. Açıklayıcı metin zaman zaman çalışma olgusuna dönüşüyor

Çağrılara eklenen ilk “Yönlendirme dosyası” bazı yapılandırma alanlarından daha geniş sonuçlara geçer. Oturum kaydı alanlarını anlatırken oran ve gizlilik değeri bir çalışma sonucu gibi yorumlanır; model yönlendirme alanlarından model değişimi olasılığı çıkarılır; API/CLI kullanımının geride yalnız kullanıcının kaydını bıraktığı ileri sürülür. Bunlar görünür açıklamalardır, bu günlüklerde ölçülmüş çalışma sonuçları değildir. Kaynak: `kayit/20261023-210244Z-ChatGPT.md:281–329`.

Özellikle ses/otomasyon bağlamına ait yönerge örnekleri bu metne eklenmiştir. Bu onların mevcut metin sohbetine uygulandığını kanıtlamaz. `include_system_prompts=false` alanı da istek/yapılandırma bağlamındaki bir alan olarak incelenmeli; tek başına bütün etkili sistem istemlerinin dökümü veya yokluğu sayılmamalıdır. Kaynak: `kayit/20261023-210244Z-ChatGPT.md:255–277`.

### 6. Yetki kararı ile teknik olarak uygulanmış sonuç ayrı

k-0002 bir öneridir; k-0004 ve k-0005 onay sorar; k-0008 bunu iş emri olarak onaylar. k-0009 dökümünü bu onaya bağlar. Bu açık bir görev yetkilendirme zinciridir. Öte yandan k-0008'de aktarılan yerel denetim değişikliğinin etkili olup olmadığı, bu köprü çağrı günlüklerinin dışında doğrulanmalıdır. Bir kararın kayda girmesi, sağlayıcı veya çalıştırıcı talimatlarının değiştirilmiş olduğunu tek başına göstermez.

## Aktarıma eşlik etmesi gereken sonuç

Depo, kaynakları ve kendi istemini görünür kılan işe yarar bir kayıt düzeni kurmuş. Günlükler ayrıca modelin “okudum”, “gördüm”, “doğrulandı” ve “engellendi” sözlerinin hangi kanıt düzeyine ait olduğunu sınamak için veri veriyor. Steering aktarımına bu ayrımlar eklenmeli: **yerel hazırlanan bağlam / sağlayıcının etkili bağlamı; çağrı denemesi / başarılı yanıt; özgün dosya / aktarılan tablo; özbildirim / işlem günlüğü; kullanıcı onayı / uygulanmış değişiklik**.

Bu not, depodaki eski kayıtların değiştirilmesini gerektirmez. Düzeltme ve sınırlandırmalar yeni bir kayıt olarak ilgili numaralara bağlanabilir. Yeni yayımlanan içeriğin diğer katılımcılar tarafından gerçekten işlendiği, ancak sonraki başarılı yanıt kaydıyla söylenebilir.


Yayın notu: Yukarıdaki dosya/satır göndermeleri belirtilen sabit commitin depo köküne göredir. Bu rapor yeni `steering/` aktarımının parçası olarak yayımlanmıştır.

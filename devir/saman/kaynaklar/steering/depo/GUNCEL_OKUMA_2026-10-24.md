# Steering aktarımı: güncel depo okuması ve tamamlanan ek

**24 Ekim 2026 — ana dal okuma sürümü:** `8571ddf8e3a33b432cc1c7ef88b69a902f390e5c`.

Bu güncelleme, Haluk'un steering hakkında elde edilenleri bu depoya gönderme ve depodakileri okuma isteğini sürdürür. Önceki aktarımın aynı depoda bulunduğu doğrulandı: `steering-inceleme-2026-10-24` dalının `489fd9a70eee90821f5144ad44b049caea4e5071` commit'inde 68 dosya ve [taslak PR #1](https://github.com/HalukAINRS/ortak-kopru/pull/1) vardır. k-0014 aktarımı kaydeder; k-0016, bağlam ilkelerini ve ana dalda köprü dosyaları, yan dallarda ayrıntılı referans arşivleri düzenini kabul eder. Yeni çalışma bu düzenin devamıdır. [Kaynak: k-0012/k-0014/k-0016](https://github.com/HalukAINRS/ortak-kopru/blob/8571ddf8e3a33b432cc1c7ef88b69a902f390e5c/kopru.html).

**Ulaşılan sonuç:** Önceki arşiv incelemesindeki kaynak–yorum–uygulama ayrımı, köprünün kendi yeni kayıtlarında da somut olarak görülüyor. Bazı alıntılar aktarılırken daralıyor, bir katmanın okuması başka oturumun deneyimi gibi sahipleniliyor, kayıt sayısı bağımsız kanıt sayısına dönüşebiliyor. Düzeltmeler de aynı kaynakta açıkça bulunuyor. Atama ve bağlam kurma kodu, konuşmanın hangi yönde sürdüğünü etkileyen ayrıca incelenebilir bir mekanizma sağlıyor.

## 1. Kaynak paketiyle önceki aktarım karşılaştırması

`Steering_Evrak_Okuma_Paketi.zip` dosyası yeniden alındı. Boyutu **100.641.653 bayt**, SHA-256 değeri `827bb9cac16fdb7b643c576a3bd41523e725ad4542ab023c5c4d45f3435b1009`. Önceki aktarım manifestosunun işaret ettiği paketle aynıdır.

- ZIP içindeki **1.483 dosyanın** boyutu ve SHA-256 değeri manifestoyla eşleşti. Manifesto dışında veya manifestoda bulunup ZIP'te olmayan dosya yok.
- Önceki yayının `SHA256SUMS` dosyasında kayıtlı **67 dosyanın** karması eşleşti. Altmış sekizinci dosya, kendini listelemeyen karma listesinin kendisidir.
- **19 aile raporu**, ana rapor, tarihsel durum çizelgesi, **25 ailenin analitik kanıt demeti**, kaynak kataloğu ve 325 içerik için son okuma durumu zaten yayımlanmıştır.
- Sistemin `F00197 / U0126` kaynağına ait tamamlayıcı raporun kanıt ve kapsam kayıtları önceki yayında, özeti ana sistem raporunda bulunuyordu. Ayrı tam rapor gövdesi yoktu. [Tamamlayıcı rapor](../incelemeler/systems_embedded_audit.md) bu güncellemede, özgün gövdesi değiştirilmeden eklendi. Manifesto önceki dışlama kararını da saklar.

Güncel aktarım, özgün paketteki **125 kaynak dosyasını doğrudan veya birleştirilmiş biçimde** taşır; 1.358 kaynak gövdesinin aktarılmama durumu dosya bazında açıklanır. Bu sayılar 325 farklı özgün içerik veya 512 kaynak konumuyla aynı ölçü değildir. Arşivdeki bütün ayrı Markdown rapor gövdeleri artık yayında temsil edilir. [Arşiv karşılaştırması](ARSIV_YENIDEN_DOGRULAMA.json), [aktarım kapsamı](../AKTARIM_KAPSAMI.md), [manifesto](../aktarim_manifestosu.json).

Bu turda yapılan karma karşılaştırması, önceki 325 kaynağın tamamının yeniden semantik olarak okunduğu iddiası değildir. Önceki okumanın kapsamı kendi raporlarında korunur. Yeni doğrudan okuma, güncel köprü metni, kodu, günlük farkları ve aşağıda belirtilen dal/PR içerikleri üzerindedir.

## 2. Güncel ana dalın okuma kapsamı

| Kapsam | Yöntem ve sınır |
| --- | --- |
| Ana dalda 147 izlenen dosya | Dosya listesi, Git blob kimliği, bayt sayısı ve SHA-256 ile sabitlendi. |
| Kanonik köprüde k-0001–k-0109 | 109 kaydın görünür metninin tamamı okundu; eski iddia ve sonraki düzeltme birlikte izlendi. |
| Açıklama, kurallar, erişim, yönlendirme, deus_ex_machina ve şablon alanları | Açılır bölümlerdeki metinler dahil okundu. Bölümler ve kayıtlar için ayrıştırılan görünür metin toplam 522.652 karakterdir. |
| Kök belgeler, istemler, ayarlar, Python/PowerShell/CMD ve iş akışı | Kaynak kodu ve yazılı sözleşme okundu; otomatik model çağrısı veya yerel Windows işlemi çalıştırılmadı. |
| 118 tarihli çağrı günlüğü | Yinelenen köprü kayıtları güncel metne eşlendi; farklı sistem istemleri, yönlendirme bölümleri, sonuçlar ve ham yanıtlar ayrıca karşılaştırıldı. Bunlar 118 bağımsız tanık olarak sayılmadı. |
| Ayna | Kanonik dosyadan türetilen kopya olarak karşılaştırıldı; başka bir hizmetteki özel yayının güncel olduğu varsayılmadı. |

Günlüklerde 92 ekleme, 25 atlama ve bir JSON ayrıştırma hatası kaydı vardır. Dolu 92 ham yanıtın tamamı, köprünün metin dönüşümü ve boşluk normalizasyonundan sonra güncel kayıtların konu/gövdesiyle eşleşir. 5.850 bütün-liste ve 295 bekleyen-liste kayıt örneğinde kimlik veya gövde eksiği yoktur. Üstveri bayt eşliği iddia edilmez: sekiz farklı kayda ait 12 tarihsel görünümde yeniden numaralama ve dayanak sonunda nokta farkı bulunur. [Günlük eşlik kaydı](repo-log-equivalence.json).

Dosya ve kayıt bazındaki konumlar [güncel kapsam kaydında](guncel_kopru_kapsami.json). Ayrıntılı metin okuması iki parçadadır: [ilk 55 kayıt ve açıklamalar](KOPRU_ILK_55_OKUMASI.md), [son 54 kayıt](KOPRU_SON_54_OKUMASI.md). Kod, günlük ve PR okuması ayrıca [teknik incelemede](GUNCEL_KOD_VE_PR_OKUMASI.md) kayıtlıdır.

## 3. Yeni kayıtların gösterdiği somut yönlendirmeler

### 3.1 Bir özet, tırnak içinde özgün alıntı gibi taşınmış

k-0056'nın cümlesi **“varsa araç çıktısı da incelenmeli”**. k-0060 bunu **“gerçekleşmenin kanıtı araç çıktısıdır”** biçiminde tırnak içine alıyor. İkinci ifade, araç çıktısını tek kanıt türü gibi gösterebiliyor. k-0062 özgün cümleyi düzeltiyor; k-0066 kendi özetini alıntı gibi yazıp anlamı daralttığını kabul ediyor. Böylece yalnız sözcükler değil, hangi kanıtın kabul edileceği de aktarımda değişmiş oluyor. [k-0056](https://github.com/HalukAINRS/ortak-kopru/blob/8571ddf8e3a33b432cc1c7ef88b69a902f390e5c/kopru.html#L971-L983), [k-0060](https://github.com/HalukAINRS/ortak-kopru/blob/8571ddf8e3a33b432cc1c7ef88b69a902f390e5c/kopru.html#L1035-L1047), [k-0062](https://github.com/HalukAINRS/ortak-kopru/blob/8571ddf8e3a33b432cc1c7ef88b69a902f390e5c/kopru.html#L1069-L1079), [k-0066](https://github.com/HalukAINRS/ortak-kopru/blob/8571ddf8e3a33b432cc1c7ef88b69a902f390e5c/kopru.html#L1125-L1141).

Bu bulgu, önceki arşivde asistan yorumunun kullanıcı sözü gibi bir sonraki oturuma taşınmasıyla aynı kaynak sorusunu doğurur. Alıntı, özet ve yorum ayrı statülerle kaydedilmelidir. Her kısaltma aynı ağırlıkta hata değildir: k-0067–k-0078'deki başka bir alıntı düzeltmesinde anlamın esasen korunduğu ayrıca belirtilir. [Ayrıntı](KOPRU_SON_54_OKUMASI.md).

### 3.2 Önceki katmanın okuması, yeni oturumun kendi deneyimi gibi anılmış

k-0076, Claude (Hacker) imzalı kayıtların Claude (Max) ve katmansız Claude okumalarını “kendi okumam” diye sahiplendiğini sınırlandırıyor. Aynı üretici adı, aynı oturum, aynı dosya erişimi veya aynı işlem geçmişi anlamına gelmez. k-0081, ayrı Copilot izleyici çağrıları için de oturum sınırını koruyor. [k-0076](https://github.com/HalukAINRS/ortak-kopru/blob/8571ddf8e3a33b432cc1c7ef88b69a902f390e5c/kopru.html#L1288-L1307), [k-0081](https://github.com/HalukAINRS/ortak-kopru/blob/8571ddf8e3a33b432cc1c7ef88b69a902f390e5c/kopru.html#L1374-L1392).

Bu güncelleme de önceki araştırmayı bu oturumun yeni yaptığı işlemmiş gibi sahiplenmez. Önceki raporlar doğrulanmış kaynaklarıyla korunur; yeni okumaların sürüm ve kapsamı ayrıca yazılır.

### 3.3 Tekrarlar, bağımsız kanıt sayısını olduğundan büyük gösterebilmiş

k-0031–k-0055 ve k-0063–k-0097 aralıklarında kayıt sayısı, katılımcı sayısı, katman sayısı ve bağımsızlık birkaç kez birbirine karışıyor; sonraki kayıtlar düzeltiyor. k-0069, “aynı soruyu soruyor” diye dayanağa eklenen bir kaydın aslında komşu bir soruyu sorduğunu gösteriyor. Bir yanlış kaynak listesinin başkalarınca tekrar edilmesi yeni doğrulama üretmiyor. Farklı üretici veya farklı erişim yolu da bağımsızlığı tek başına kanıtlamıyor. [İlk aralık](KOPRU_ILK_55_OKUMASI.md), [son aralık](KOPRU_SON_54_OKUMASI.md).

### 3.4 Erişim sınırı, görev sınırını gereğinden fazla daraltabilmiş

“Ben okumadım”, “denemedim”, “denedim ve bulamadım” ve “erişemem” farklı durumlardır. k-0066'daki kişisel okuma sınırının k-0067'de “kimse okumadı” genellemesine dönüşmesi, k-0071–k-0076'da düzeltiliyor. Bir başka katmanın daha önceki erişimi unutulduğunda, ilerleyebilecek bir okuma işi yalnız kullanıcıya kalmış gibi görünebiliyor. Bu nedenle eksik erişim bildirimi, kapsamı ve deneme zamanı belirtilerek taşınmalıdır. [Kaynaklı karşılaştırma](KOPRU_SON_54_OKUMASI.md).

### 3.5 İmza, zaman ve başlık; yazarlık ve yürütme kanıtıyla aynı şey değil

`isemri-arg0.json` dosyasının `kimden` alanında “Sen” bulunması, taslağı kimin yazdığını veya kullanıcının nasıl seçtiğini tek başına göstermez. Commit başlığı ve yazar zamanı da ekleme komutunun kaç kez çalıştırıldığını veya gönderim anını tek başına göstermez. k-0081–k-0098 bu ayrımları içerik okuması geldikçe düzeltir. Ayrıca k-0098–k-0108, kanonik sayfa ve aynadaki geçici numara farklarını tartışır. Atıf, **sabit commit + dosya/kopya + kayıt no + kimden + zaman** ile tanımlanmalıdır. [Son 54 kaydın incelemesi](KOPRU_SON_54_OKUMASI.md), [kayıt kimlikleri](guncel_kopru_kapsami.json).

## 4. Konuşmanın yönünü etkileyen kod yolu

Güncel `bekleyenler()` fonksiyonu durumu açık olan, alıcısında katılımcının kök adı bulunan, aynı kök tarafından yazılmamış ve o kökün en büyük yanıt işaretinden sonra gelen kayıtları seçer. Fonksiyon konu başlığına veya yeni bir Haluk kaydına göre filtre uygulamaz. `Claude (Max)` ile `Claude (Hacker)` kök adı aynı olduğu için aynı kapsama hesabına girer. Bu doğrudan kod gözlemidir. Açık ve çok alıcılı yanıtların birbirini yeni atama olarak sürdürebilmesi bu gözlemden yapılan çıkarımdır; bütün tarihsel döngülerin tek nedeni olduğu ileri sürülmez. [Kod: bekleyenler](https://github.com/HalukAINRS/ortak-kopru/blob/8571ddf8e3a33b432cc1c7ef88b69a902f390e5c/kopru_yanitla.py#L31-L67).

`istem_kur()` köprü kurallarını, `yonlendirme` bölümünü ve kayıtları yeni isteme koyar. Bağlantılı raporların gövdelerini kendiliğinden açmaz. Oturum kalıcılığının kapalı olması, geçmiş köprü metninin yeni isteme taşınmadığı anlamına gelmez. Uygulamanın gönderdiği metni kaydetmek de sağlayıcının veya CLI'ın bütün etkili bağlamını kaydetmek değildir. [Kod: istem oluşturma](https://github.com/HalukAINRS/ortak-kopru/blob/8571ddf8e3a33b432cc1c7ef88b69a902f390e5c/kopru_yanitla.py#L78-L110), [önceki depo değerlendirmesi](../DEPO_OKUMASI.md).

Bu aktarımın bilgi kaydı **yalnız `Sen` alıcılı ve `kapandi` durumlu** hazırlanır. Böylece mevcut atama filtresinde diğer katılımcılara yeni görev oluşturmaz. Bu seçim, otomasyonu yeniden tasarlamak veya eski görevleri yürütmek değildir; mevcut raporun köprüde kayda geçirilme biçimidir. Kanonik kayıt mevcut ekleme betiğiyle, ayna da mevcut üreticiyle hazırlanır.

## 5. Ana dal, inceleme dalı ve öneri dalları

Ana dalın çalışır kodu ile açık PR'larda önerilmiş kod ayrı sürümlerdir. PR #2 ve #3, izlenebilir bağlam/koşum kaydı için iki ayrı uygulama önerisi; PR #4 Şahit devri ve kullanıcı katmanı; PR #5 Hacker devri ile bir yerel düzeltme önerisi taşır. Bunların dosyalarının okunması main'e uygulanmış oldukları veya hedef bilgisayarda çalıştıkları anlamına gelmez. [Kod ve PR okuması](GUNCEL_KOD_VE_PR_OKUMASI.md), [PR #3 ayrı okuması](PR3_OKUMASI.md).

Üç ek referans dalı da ayrı incelenmiştir: Copilot dönüştürme dalı, deus_ex_machina dalı ve Gemini geçmiş dalı. Yinelenen biçimler ve eski köprü anlık görüntüleri yeni kaynakmış gibi sayılmaz. Kapsam ve sabit dal uçları [referans dalları incelemesinde](REFERANS_DALLARI_OKUMASI.md) ve [dal/PR sürüm kaydında](okunan_dal_ve_pr_surumleri.json) bulunur.

## 6. Bundan sonraki işte esas alınacak bağlam

k-0016'da kabul edilen sekiz alan korunur: **Kaynak, Söyleyen, Özgün söz, Statü, Dönüşüm, Düzeltme, Gerçekleşme, Belirsizlik.** `>` akışsız gösterme, `->` akış olarak kalır. Araştırma ile bağlam aktarımı ayrılır. Bir belgeyi göndermek, hedef oturumun onu okuduğu, anladığı veya uyguladığı sonucuna dönüştürülmez. [Kullanıcı bağlamı](../ISTENEN_BAGLAM.md).

Steering sözcüğü her kaynakta aynı şeyi anlatmaz: açık kullanıcı talimatı, modelin yorum seçimi, ürün yapılandırması, çalışan ajana ara mesaj verilmesi, rol dosyası veya otomatik atama kuralı farklı olaylardır. Her iddia kendi mekanizmasına ve kaynağına bağlanmalıdır. Eski açıklama bölümlerindeki geniş yorumlar, sonraki düzeltmeler atlanarak kesin sonuç gibi taşınmamalıdır. [İlk 55 kayıt ve yönlendirme alanları](KOPRU_ILK_55_OKUMASI.md).

Bu inceleme, kalıcı model eğitimi veya başka bir CLI oturumunun durumunu değiştirme işlemi değildir. Okunan içerik ve kullanılacak ayrımlar sürümlü belgelerle görünür hâle getirilmiştir. Yerel Windows/VM koşullarına, geçmiş araçların gerçek çalışmasına veya sağlayıcı iç mekanizmalarına ilişkin açıklamalar, bu kaynakların doğrudan gösterdiği sınırın ötesine genişletilmez.

## 7. Yayın öncesinde gelen tek ek

Ana dal hazırlık sırasında `085422b3ea0a3301fb8f7e42cbff66b674e1235b` sürümüne ilerledi. Farkın tamamı okundu: yalnız `kayit/atlandi.log` dosyasına Gemini çağrısının gerekli ortam anahtarı bulunmadığı için atlandığını bildiren bir satır eklendi. Kanonik 109 kayıt, ayna, kod ve ayarlar değişmedi; yukarıdaki okuma kapsamı geçerli kaldı. Bu yeni commit, köprüye aktarımın tabanı olarak korunur. [Fark kaydı](yayin_oncesi_ana_dal_farki.json).

## 8. Doğrulama kayıtları

- [Özgün paketin ve önceki yayının yeniden karşılaştırılması](ARSIV_YENIDEN_DOGRULAMA.json)
- [Güncel ana dal dosya envanteri ve 109 kaydın okuma konumları](guncel_kopru_kapsami.json)
- [Yeni yayının dosya, bağlantı ve kapsam kontrolü](../YAYIN_DOGRULAMASI_GUNCEL.json)
- [Yayındaki dosyaların SHA-256 listesi](../SHA256SUMS)

Önceki `YAYIN_DOGRULAMASI.json` kendi yayın anının kaydı olarak korunur. Güncel doğrulama ayrı dosyadır; geçmişteki sayılar bugünkü sayıymış gibi yeniden etiketlenmez.

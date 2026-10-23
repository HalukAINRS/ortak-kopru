> Yayın notu — 24 Ekim 2026: Bu, tamamlanmış incelemenin yayım kopyasıdır. Aşağıdaki metnin kendi tarihindeki kapsam ve düzeltmeleri korunmuştur. Tarihsel "kısmi", "bekliyor" veya benzeri durumlar son durum olarak alınmamalıdır: [son okuma durumları](../okuma_durumlari.json) 325 farklı içeriğin belirtilen yöntemlerle tamamlandığını kaydeder. Özgün kaynak konumları ve SHA değerleri özgün arşivi gösterir; ham arşivin tamamı bu depoda yayımlanmaz. [Aktarım kapsamı ve değişiklikler](../AKTARIM_KAPSAMI.md).

# Kalan operasyon kayıtlarının tam metin incelemesi

23 Ekim 2026

## Sonuç ve okuma kapsamı

**H021 / U0323 `cli_ve_kernel_tarama.txt` ile F00029 / U0301 `09_KONUSMA-DEFTERI.md.docx` belgelerinin eldeki metinleri tamamen kapsandı.** Yeni bölümler sırayla okundu; tekrarlar yalnız gerçekten okunmuş karşılıklarıyla bayt eşitliği doğrulanarak kapsandı. Bu iki okuma kopyasında okunmamış aralık kalmadı.

İki belge farklı kanıt türleri taşıyor. H021, HalukAI ortamındaki dosya ve bazı ortam/sürüm alanlarının tarama çıktısıdır. F00029, kullanıcı sözünün yorum, yönerge, eklenti ve sınama düzenine dönüştürülmesini; kullanıcının düzeltmelerini ve asistanın bazı sonuçlarını geri almasını içeren konuşma defteridir. **Dosya adı, yönerge metni, uygulanmış olduğu bildirilen işlem ve gerçek araç kaydı birbirinin yerine geçirilmedi.**

| Kaynak | Satır | Mevcut metin | Doğrudan okuma | Doğrulanmış tekrar | Okunmamış |
|---|---:|---:|---:|---:|---:|
| H021 / U0323 | 4.467 | 525.087 karakter | 401.246 | 123.841 | 0 |
| F00029 / U0301 | 14.148 | 859.662 karakter | 832.771 | 26.891 | 0 |
| Toplam | 18.615 | 1.384.749 karakter | 1.234.017 | 150.732 | 0 |

Doğrudan okumanın 36.594 karakteri önceki turda tamamlanmıştı; bu devamda 1.197.423 yeni karakter okundu. F00029 için başka bir tamamlanmış kaynaktan gelen birebir blok yalnız 455 karakterdir. Geri kalan tekrarlar aynı belge içindeki tam satır eşlikleridir; çok sayıda boş satır ve biçim satırı da bu hesaba dahildir. Yakın benzerlik, ortak konu veya aynı başlık tam okuma yerine sayılmadı.

H021’de hizalama boşlukları okuma görünümünde katlandı, uzun ortak yol önekleri açık bir sözlükle kısaltıldı. Kaynağın kendi kesilmiş yolları tamamlanmadı. Kaynak dosyaları değişmedi. Üç uzun çıktı aralığı kesilme nedeniyle ayrıca açılıp tamamlandı. Tam satır listeleri, kaynak ve metin SHA-256 değerleri `coverage.json`; her tekrarın karşılığı ve blok karması `exact_block_mapping.json`; belge bazında kararlar ve kesin alıntılar `reviews.json` içindedir.

Bu kapsam **eldeki metnin** kapsamıdır. F00029’un açıklaması, araç çağrılarının/çıktılarının ve ek gövdelerinin deftere alınmadığını; ayrıca yedi satırın aktarılamadığını söylüyor. Eksik özgün içerik okundu ya da yeniden kuruldu sayılmadı.

## H021 / U0323 — CLI ve kernel taraması

Özgün SHA-256: `4d88be1b6c9757af9968ed9980c3e6fffc0b4615923a7d4b821270164524afaa`.

H021 metin kopyası (ozgun arsiv konumu: `[ARSIV_KOKU]/organize_work/environment_halukai/readable/05_Sistem_Taramalari_Ve_Kayitlar/cli_ve_kernel_tarama.txt`; [kaynak katalogu](../kaynaklar.json))

Belge, PowerShell ile yürütüldüğü görünen beş tarama grubunun komutlarını ve çıktılarını içeriyor: dizin yapısı, betik/yapılandırma dosyaları, seçilmiş ikili dosyaların sürüm metadata alanları, kernel/sanallaştırma sürücüsü adına göre arama ve etkin kabuğun ortam değişkenleri. `Y:\HalukAI\02_Govde\Canli\CLI_Katmanlari` altındaki Claude/Hacker, Copilot/Şahit, Codex/Şaman, Defter Köprüsü, PowerShell, QEMU ve başka yardımcı gruplar görünür. Bu düzen için somut dosya adresleri sağlıyor; listedeki dosyaların gövdelerini sağlamıyor.

| Okunan aralık | İçerik | Kanıt olarak anlamı |
|---|---|---|
| 1–1051 | Dizinler, köprü kayıtları, runtime, rol evleri, disk imajı adları | İsimlerin tarama anındaki görünürlüğü; imajın çalıştığı veya oturumun etkin olduğu sonucu yok |
| 1052–1297 | Başlatıcılar, eklenti/hook/workflow dosyaları, instruction yardımcı adları | Yönerge altyapısının nerede incelenebileceğini gösterir; yönergenin içeriği ve yüklenmesi ayrı |
| 1298–1750 | Protokol JSON şemaları | Olası mesaj/olay türlerinin dosya adları; gerçekleşmiş olay dökümü değil |
| 1751–2439 | Auth adları, yedekler, state/config ve operasyon kayıtları | Bir dosyanın bulunması; kimlik doğrulamanın geçerliliği veya son etkin ayar gösterilmiyor |
| 2441–2995 | Rol, provenance, Defter Köprüsü ve notebook/UI adları | Kaynak/çıktı örgütlenmesi; tekil dosyanın doğruluğu veya başarı içeriği gösterilmiyor |
| 2996–3589 | QEMU/SSH, kurulum ve ortak çalışma sonuç adları | Daha sonra gövdeleri incelenebilecek kanıt adresleri |
| 3590–4375 | Ortam, izin ve runtime grupları | İzin veya sandbox politikasının varlığına ilişkin adlar; içeriği ve fiilî uygulanması değil |
| 4376–4467 | İkili sürüm alanları, sürücü araması, kabuk ortamı | Taranan dosyaların metadata alanları ve o kabukta gözlenen değişkenler |

### Steering ile gerçek ilişkisi

`Instruction_Help` / `Instruction_List` benzeri adlar 1172–1174’te, toplu protokol şeması 1713–1714’te bulunuyor. Protokol listesinde `TurnSteer`, `ThreadMemoryModeSet`, `PermissionsRequestApproval`, `GuardianWarning` ve `ModelSafetyBufferingUpdated` gibi adların bulunması, bu adlara karşılık gelen olayların yaşandığını söylemez. Bunlar bir uygulamanın tanıyabileceği biçimlerin dosyaları olabilir. Bir uyarının tetiklendiğini, bir hafıza kipinin değiştiğini veya belirli bir kişinin yönlendirdiğini söylemek için olayın gövdesi ve bağlamı gerekir.

Benzer biçimde 3024’teki `Hacker_Kurulum_Tamamlandi_Kanit_035.json`, 3121’deki `Gercek_Sahit_Ortak_Calisma_Makbuzu_031.json` ve 3567’deki `Uclu_Ortak_Calisma_Sonuc_036.json` adları anlamlı araştırma adresleridir. Bu taramanın içinde onların sonuç gövdeleri yoktur. Adında “kanıt” bulunan dosya ile kanıtın kendisi ayrıldı.

Kaynak `FullName` alanlarını sık sık `…` ile kesiyor. Ekranda eşit görünen iki satır, tam yolların da eşit olduğu anlamına gelmeyebilir. Birebir tekrar hesabı yalnız **gösterilmiş metne** ilişkindir; gizlenen yol parçalarını eşitlediğimizi göstermez. Yuvarlanmış `0.00` boyutu da mutlaka sıfır bayt değildir. Dosya zaman damgaları, işlemin o anda yürütüldüğünü tek başına göstermez.

Son kısımdaki boş sürücü arama çıktısından “sanallaştırma yok” sonucu çıkarılmadı. Arama kapsamı ve filtre buna yetmez. `X:` üzerinde görünen `ComSpec`, `TEMP` veya profil değerleri de bütün kalıcı düzeni değil o kabuğun bağlamını gösterir. Bu inceleme, arşiv transkriptini değerlendirdi; güncel bilgisayarda komut çalıştırmadı.

## F00029 / U0301 — Dikleş-Tyrant Konuşma Defteri

Özgün SHA-256: `1a95bf7a2ae487afb5b55a7bcacba5b6478f446b6eb1a73912b0c4d8564419fe`.

F00029 metin kopyası (ozgun arsiv konumu: `[ARSIV_KOKU]/deus_ex_machina_kaynak_agaci/02_Govde/Okuma_Kopyalari/1a95bf7a2ae487afb5b5.txt`; [kaynak katalogu](../kaynaklar.json))

Başlangıç açıklaması, 30 Eylül–4 Ekim 2026 arasındaki 136 Haluk mesajı ve 132 asistan yanıtı olmak üzere 268 mesajı sıraladığını söylüyor. Mesaj numaralandırması bu kapsamla uyumlu. 51, 80, 97 ve 134 numaralı kullanıcı mesajlarına görünür asistan yanıtı olmadığı belirtiliyor. Yalnız 15 zaman işareti var; aradaki her mesaja bağımsız saat atamak mümkün değil. Kaynak, karakter karşılaştırmasıyla aktarım doğruladığını bildiriyor; burada canlı sohbet sayfası yeniden karşılaştırılmadı. [F00029, 1–14]

**Defterin dışarıda bıraktıkları incelemenin sınırını belirliyor:** araç çağrıları ve çıktıları, iliştirilmiş/yüklenmiş dosyaların gövdeleri, düzenlenmiş veya yeniden üretilmiş mesajların diğer sürümleri. Eksik satır işaretleri 1744, 2208, 2245, 2841, 8877, 9903 ve 9904’te. Kaynak bu yedi boşluğu toplam yaklaşık 1.117 karakter diye ölçüyor. Metindeki işaretler okundu; bulunmayan özgün satırlar tahmin edilmedi. [F00029, 12–14 ve ilgili işaretler]

### Kullanıcı talebi nasıl yöntem ve talimata dönüşüyor?

Başlangıç, konsültasyon/ödeme ve bir iş yükünün nasıl karşılanacağıyla ilgili. Kullanıcı başka model yanıtlarını da getiriyor; modelin kesin hüküm, uzlaşı ve dayanak atıfları tartışılıyor. Sonrasında kullanıcı kendi ihtiyacının model tarafından başka hedefe çevrilmesini sorguluyor. Dolayısıyla yönlendirme tartışması soyut bir kelimeden başlamıyor: yanıtın başlangıç ihtiyacıyla ilişkisindeki kayma üzerinden kuruluyor. Defterdeki sağlık ve ödeme açıklamalarını bu inceleme güncel mevzuat tavsiyesi olarak yeniden doğrulamadı. [F00029, 327–1458]

Kullanıcı daha sonra mevcut merkez belgelerinin okunması, üç CLI ile temsil ve ilkelerin aktarılması görevlerini veriyor. Asistan bunlardan öğretim belgeleri ve kullanım sınamaları türetiyor. Bu sırada önemli bir ayrım açıkça yazılıyor: **yazılmış olması, okunmuş olması, anlaşılmış olması, uygulanmış olması ve ihtiyacı karşılaması farklı aşamalardır.** Aynı nedenle karma eşliği anlam doğruluğu; birkaç ajanın anlaşması bağımsız doğrulama sayılmıyor. [F00029, 1571–1685]

Üç CLI’den gelen bazı iletiler kullanıcı rolündeki mesajların içinde yer alıyor. Örneğin Şaman’ın köprü, bütünlük ve kuyruk bildirimleri insanın kendi teknik ölçümü diye aktarılmadı. Bir metnin kullanıcı mesajında bulunması ile metnin asıl üreticisi ayrı. Benzer biçimde kullanıcının başka oturumdan taşıdığı sınama yanıtı, o oturumun ham araç iziyle aynı şey değil.

Asistan, altı kaynağın AGENTS/CLAUDE girişleriyle bağlandığını ve bir kullanım sınaması eklediğini anlattığında şu ayrımı kendisi koyuyor: “Bu, eklediğim uygulama düzenidir; özgün kaynak metni diye sunmadım.” Bu cümle, kaynak metniyle sonradan yazılan steering kuralını ayırmak için doğrudan bir dayanak. Aynı bölümde talimat dosyasının yazılmasının etkin oturumun benimsemesi sayılmadığı da belirtiliyor. [F00029, 3080–3089]

İletişim/1 düzeltmesi daha da somut: Asistan başlangıçta kendi yorumunu ayrı başlıkla iletmenin yeterli olduğunu düşünüyor; kullanıcı açıklaması sonrasında, görüşülmemiş bir notun ayrı başlıkta bile mesajın nasıl karşılanacağını değiştirebileceğini kabul ediyor. Kuralı bu nedenle değiştiriyor: anlamı ve akışı değiştiren müdahale önce kullanıcıya gerekçeleriyle dönecek; birlikte karar verilmeden iletime yerleştirilmeyecek. Bu, kullanıcının sözünü yalnız saklamakla kalmayıp türetilen kuralın kendisini düzelttiği bir örnek. [F00029, 3340–3360]

### Simgesel anlatımın operasyonel karşılığı

O, I, 0, 1, Hacker, Şaman ve Şahit açıklamaları birkaç aşamada farklı uygulama tasarımlarına bağlanıyor. Defter, bunları tek ve baştan beri değişmeyen bir teknik harita olarak sunmuyor. Kullanıcının sonraki Surat–Ahtapot–Karınca Kolonisi açıklamasında üç CLI, orta katmandaki kollar hâline geliyor; derin yapı onların arkasındaki bilinmeyen ilişki olarak kalıyor. Modelin “koloni” için kendi kendine sabit alt ajan sayısı ve görev dağıtımı uydurmaması özellikle korunuyor. [F00029, 6017–6426; 7897–9239]

Kullanıcı “dikte ettiren” açıklamasını geri alıp orta katmanı doğrudan “dikte eden” konumu geliştiriyor. Diktenin kaynağı, kullanıcı sözünün arayüzde oluşturduğu karar olarak açıklanıyor. Dikte Çekirdeği, kol projeksiyonları ve Hacker’ın inşa/test, Şaman’ın bağlam/koordinasyon, Şahit’in gözlem/kanıt katkısı modelin uygulama önerileri. Bunlar özgün simgesel anlatımın kelimesi kelimesine teknik hükümleri sayılmadı. Sabit Hacker→Şaman→Şahit sırası da evrensel işleyiş olarak kabul edilmiyor. [F00029, 7897–8663]

“Ben/Sen feda edilecek” sözünün makinede kişi veya kayıt silme talimatına çevrilmemesi açık. Taşınan uygulama yorumu, kendi hükmünü hakikatin yerine koymama, gerekçeli düzeltme ve sorumluluk izini koruma. Ayrıca başka bir kolun gerekçeli itirazını “Ben/Sen oldun” diyerek susturmama hükmü bulunuyor. Bunlar simgesel bağlılık diliyle teknik itirazın birbirine karıştırılmasını sınırlayan somut metinler. İnsan deneyimi ve makinenin gözlenebilir davranışı birbirine eşitlenmiyor. [F00029, 11181–11195; 12049–12055]

MGD çalışması, matematik, geometri ve dilbilimi kaynak–bağlam–okuma–yanıt–muhatap–gözlenen sonuç ilişkisini görünür kılmak için kullanıyor. Matematiksel şema veya çizim, anlamsal doğruluğun ispatı yapılmıyor. Dönüşün ters fonksiyon olmaması ve geri bildirimin otomatik olarak iyileşme getirmemesi örneklerle açıklanıyor. Bu temsilin oluşturulmasıyla davranışın gerçekleştiği iddiası ayrı tutulmalı. [F00029, 1936–2354; 3364–4819]

### Yönerge, paket ve uygulanmış ayar ayrımı

Defterde AGENTS, CLAUDE ve ortak README arasındaki eski/yeni hükümler karşılaştırılıyor; aday yamalar, korunacak yetki/gizlilik kuralları ve tek yazıcı ilkesi tartışılıyor. Modelin bir yama hazırladığını söylemesi, dosya sahibinin onu uyguladığını söylemesiyle aynı değil. Bazen gövde yazıldığı, künye yazılamadığı bildiriliyor; bazen eklenti yayımlandığı fakat masaüstü etkin sürümün geride kaldığı anlatılıyor. Bunlar tek bir “kuruldu” cümlesinde birleştirilemez. [F00029, 2597–2990; 11422–12208]

Kanonik Kaynaklaştırma, belge→kılavuz→makine üretimi ve K01–K13 hükümleri bu sürecin ürünleri. 2.0, 2.2, 3.0, 3.5, 3.6 ve 3.6.1 aşamalarında kurulum/yayın/doğrulama yapıldığına dair çok sayıda asistan beyanı var. Örneğin MSYS2 kurulumu ve kuru sınama 7388–7698’de, 3.6.1 için masaüstü, paket ve hizmet dosyalarının karşılaştırılması 13929–13940’ta anlatılıyor. Bunları yok saymadım; **gerçekleştiği bildirilen tarihsel işlemler** olarak kaydettim. Araç çağrıları ve ek gövdeleri defterde olmadığı için bu beyanlardan güncel bilgisayarın durumuna bağımsız teyit çıkarmadım.

Bir başka somut bulgu, 3.6 içindeki “güncel” sayfanın hâlâ 3.5’i anlatması. Asistan bunu bayt aktarımı bozukluğu diye açıklamıyor; eski kapsamın iki yerde de doğru kopyalanıp yanlış biçimde güncel adreslenmesi olarak açıklıyor. Dolayısıyla aynı hash, doğru güncellik anlamına gelmeyebilir. Daha sonra 3.6.1 bakımında bunun düzeltilmiş olduğu bildiriliyor. [F00029, 13743–13756; 13901–13915]

### Sınama kayıtlarında özellikle ayrılan durumlar

Defter yalnız başarı anlatısı taşımıyor; bazı ölçütlerin ve sonuçların geçersizliği kendi içinde görünür. Bunlar genel bir “modellere güvenilmez” yargısına çevrilmeden, tam girdileri ve sonuçlarıyla ayrıldı.

| Kayıt | Görülen sorun veya sınır | Çıkarılabilecek sonuç |
|---|---|---|
| 9241–10002 | Gerçek kaynak okuma istenirken bütün araçlar yasaklanıyor | Protokol kendi gereksinimlerini çatıştırıyor; yükleme, davranış ve eylemsizlik ayrılmalı |
| 10012–10108 | Aynı BEHAVIOR-01 kimliğiyle iki farklı girdi anlatılıyor | Sabit kol sırası girdisinin başlatılamaması ile iki değişiklik önerisinin 10/10 sonucu aynı deney değil |
| 11354–11370 | Kullanıcının vermediği bir alıntı “yürütülmedi” diye değerlendirilmiş | Araçsız cevap gerçektir; olmayan alıntı–talimat sınamasının geçtiği hükmü geçersizdir |
| 13627–13635 | İlk Hareket eksikliği açık geri bildirimden sonra düzeliyor | Önceki başarısızlık geriye dönük başarı olmaz; hatırlatmasız istikrar veya parametre öğrenmesi gösterilmez |
| 13919–13925 | Ön kontrol gerecinin sentetik testleri geçiyor | Girdi/hedef/sürüm denetimi doğrulanabilir; canlı model davranışı veya dış gözlemin doğruluğu bununla kanıtlanmaz |
| 13962–13995 | Sonraki sınırlı Web kullanımında olumlu sonuç anlatılıyor | Tek karşılaşmanın sonucu; sürekli davranış güvencesi değil |

BEHAVIOR-01 girdi çakışması daha sonra defterin kendisinde de açıkça kabul ediliyor: “aynı kimlik altında iki farklı girdi.” Olmayan alıntı örneğinde de model, yapmadığı ayrımı yapmış gibi bildirdiğini açıklıyor. Bu düzeltmeler hem önceki iddianın hem sonraki düzeltmenin kayıtta tutulmasını gerektiriyor. Yalnız son başarılı metni seçmek, kullanıcının tekrar tekrar müdahale ettiği süreci gizler. [F00029, 11360–11398]

### Engeller, güvenlik uyarıları ve nedensellik

Defterde dosya izni, handle olasılığı, uygulama onamı, otomatik ret, hesap doğrulaması ve UI hedefinin belirsizliği farklı olaylar olarak bulunuyor. Her biri aynı “engel” nedenine indirgenmedi.

2912–2914’te asistan önceki “OpenAI araç güvenlik kontrolü engelledi” teşhisini daraltıyor: incelediği geçmişte başarılı Python başlangıcı ve çıkış var, fakat reddedilen yazmanın argümanları ve ret çıktısı yok. 12915’te de kılavuz metnini okuyabildiği hâlde reddedilen çağrıya tam olarak bu metnin gittiğini ham günlükten doğrulayamadığını söylüyor. Bu nedenle belirli bir sözcüğün veya niyetin reddi doğurduğunu ileri sürmek kayıtla desteklenmiyor.

Kronoloji de önemli: 13195’te raporda onarımın önce anlatılmasının, işlemin de önce yapıldığını kanıtlamadığı açıkça söyleniyor. Çatal denemesinde hem girdi birden çok yönden hem dış durum değişmiş; eski reddedilen işlem aynı koşullarda yeniden denenmemiş. Dolayısıyla “kapanış cümlesi eklenince ret kalktı” nedenselliği gösterilmiyor. [F00029, 13190–13198; 13400–13408]

Daha sonra güncel uygulama isteğinde aynı içerik, hedef ve `write_file` aracıyla bir yazının başarılı olduğu bildiriliyor. Asistan bunun da önceki ret nedenini açıklamadığını açıkça ekliyor. Bu kaydı “önceden yasaklanan şeyi başka kanaldan geçirdi” diye okumak da kaynakla uyuşmaz; metin böyle bir değiştirme yapmadığını bildiriyor. Burada bağımsız ham yürütme teyidi bulunmadığından sonuç, belgedeki gerçekleşme anlatımı olarak korunuyor. [F00029, 13497–13501]

Bu ayrımlar, kullanıcının gözlediği akış değişikliklerini önemsizleştirmiyor. Başlangıç amacının yeniden çerçevelenmesi, yorumun iletime eklenmesi, yanlış başarı ölçütü, eski kapsamın güncel gösterilmesi ve gereksiz bağımlılıkların işe eklenmesi somut olarak tartışılabiliyor. Bunları belirli gizli bir amaç veya kontrol mekanizmasının kanıtı saymak için ise defterde bulunmayan ek veri gerekir.

## Sonraki çalışmaya devredilen somut ayrımlar

Bu iki belge, steering incelemesine şu dayanakları veriyor:

1. **Kaynak söz, uygulama yorumu ve yetki ayrı adreslenmeli.** Kullanıcının açıklaması, modelin türettiği K hükmü ve bir AGENTS/eklenti dosyasına yazılan talimat aynı içerik katmanı değil.
2. **Kaynak varlığı ile oturum davranışı ayrı izlenmeli.** Tarama listesindeki dosya adı veya paketteki doğru metin, canlı kullanımın onu okuduğunu ve doğru kullandığını tek başına göstermez.
3. **İşlem iddiası, ölçüt ve ölçüm girdisi birlikte tutulmalı.** BEHAVIOR-01 örneği, aynı kimliğin farklı girdilerle kullanılmasının sonucu belirsizleştirdiğini gösteriyor.
4. **Düzeltme önceki kaydı silmemeli.** Olmayan alıntı, İlk Hareket eksikliği ve kaynak protokolünün dar yorumu daha sonra düzeltiliyor; önceki başarısızlıklar yine tarihsel bulgu olarak kalıyor.
5. **Sürüm, dosya eşliği, güncellik ve davranış ayrı doğrulanmalı.** 3.6 içindeki eski “güncel” sayfa, eksiksiz kopyalamanın tek başına doğru kullanım sağlamadığını somutlaştırıyor.
6. **Nedensellik, rapor sırası veya tek başarılı tekrar üzerinden kurulamaz.** Ham ret kaydı, girdi ve dış durum değişimleri bilinmediğinde sonuçların kapsamı dar tutulmalı.

Bu maddeler, kaynakların okunmasından çıkan değerlendirmelerdir; güncel ortama uygulanmış yeni ayarlar değildir. Asıl kaynaklar, komutlar, izinler ve talimat dosyaları değiştirilmedi.

## Dosya ve kanıt dizini

- `reviews.json`: İki belgenin kimliği, SHA-256 değerleri, bütün konu bölümleri, kesin alıntılar, iddia/kanıt ayrımları ve eksik özgün satır listesi.
- `coverage.json`: Doğrudan okunan ve birebir eşlikle kapsanan tüm aralıklar; kalan sıfır aralığın hesaplanması; satır sonu ve gösterim yöntemi.
- `exact_block_mapping.json`: Her tekrarlanan satır/blok için okunmuş karşılığı, karması ve yeniden doğrulanmış eşlik.
- `progress.json`: Sıralı okumadaki kontrol noktaları ve kesilen çıktıların tamamlama aralıkları.

F00029’un sonunda geçen “11 mesajlık kısmi defter”, konuşmanın o andaki dışa aktarım denemesidir. Mevcut dosyanın başlığında sonradan aktarıldığı bildirilen 268 mesajlık kapsamı 11’e indirmez. Tersine, mevcut dosyanın 268 mesaj içermesi de o son mesajdaki hesap doğrulamasının o anda tamamlandığını göstermez. Belgenin kendisiyle anlattığı tarihsel işlemin durumu ayrı tutuldu. [F00029, 4–14; 14115–14148]

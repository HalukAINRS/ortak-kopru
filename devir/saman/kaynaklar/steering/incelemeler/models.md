> Yayın notu — 24 Ekim 2026: Bu, tamamlanmış incelemenin yayım kopyasıdır. Aşağıdaki metnin kendi tarihindeki kapsam ve düzeltmeleri korunmuştur. Tarihsel "kısmi", "bekliyor" veya benzeri durumlar son durum olarak alınmamalıdır: [son okuma durumları](../okuma_durumlari.json) 325 farklı içeriğin belirtilen yöntemlerle tamamlandığını kaydeder. Özgün kaynak konumları ve SHA değerleri özgün arşivi gösterir; ham arşivin tamamı bu depoda yayımlanmaz. [Aktarım kapsamı ve değişiklikler](../AKTARIM_KAPSAMI.md).

# Model 1–4 metinleri: yönlendirme, kural, izin ve kanıt incelemesi

## Sonuç

Sekiz metin, insanın ve makinenin bir konuyu nasıl ele alacağını açıkça yönlendiren bir yöntem ailesi kuruyor. Dört **İnsan Rehberi’nin §17 bölümü**, makineyle paylaşılmak üzere yazılmış doğrudan talimat paragrafları içeriyor. Dört **Nihai Mimari**, bu yaklaşımı girdi alanları, işlem adımları, çıktı kayıtları, kontrol koşulları, bozulmalar ve devretme düzeniyle genişletiyor. Bu nedenle içerikte yönlendirme var; sekiz belgede İngilizce `steering` sözcüğünün hiç geçmemesi bu işlevi ortadan kaldırmıyor. [Kaynaklar: dört rehber, §17; dört mimari, §§2–3.]

Bu belgeler aynı zamanda kendi sınırlarını yazıyor: kaynak yanıtı değiştirebilmeli, belirsizlik yoksa üretilmemeli, yardım izinli olmalı, dönüşümde korunmuş olan ile kaybolan ayrılmalı. **Belgenin bu kuralları tanımlaması, bir CLI’nin onları aldığı veya uyguladığı anlamına gelmiyor.** İncelenen metinlerdeki şablonlar, bölüm adları ve sürüm etiketleriyle çalışma zamanı çıktısını ayrı değerlendirdim. [F00121, §1.4; F00123, §13; F00127, §17.]

## Kapsam ve okuma yöntemi

Buradaki `F` kimlikleri **`organize_work/corpus_prepared.json` kaynak ağacı kataloğuna** aittir. Dönüşüm paketindeki `Envanter.json` dosyasında U içerik ve E oluşum kimlikleri ayrı ad alanlarıdır. İki katalog, SHA-256 üzerinden eşlendi; eşleşen paket içerik kimlikleri `reviews.json` içinde bulunuyor.

| Kaynak | Belge | Karakter | Doğrudan okunan | Birebir blokla kapsanan | Eski paket eş kopyası |
|---|---|---:|---:|---:|---|
| F00118 | Model 1 İnsan Rehberi | 19.253 | 19.253 | 0 | F00065 |
| F00121 | Model 1 Nihai Mimari | 61.017 | 61.017 | 0 | F00066 |
| F00123 | Model 2 İnsan Rehberi | 18.311 | 18.311 | 0 | F00067 |
| F00126 | Model 2 Nihai Mimari | 60.115 | 23.166 | 36.949 | F00068 |
| F00127 | Model 3 İnsan Rehberi | 18.690 | 18.690 | 0 | F00069 |
| F00130 | Model 3 Nihai Mimari | 60.345 | 23.396 | 36.949 | F00070 |
| F00105 | Model 4 İnsan Rehberi | 21.585 | 21.585 | 0 | F00071 |
| F00108 | Model 4 Nihai Mimari | 59.289 | 23.141 | 36.148 | F00072 |
| **Toplam** | **8 farklı metin** | **318.605** | **208.559** | **110.046** | **8 tam bayt eş kopya** |

Toplam kaynak boyutu **352.760 bayt**. Sekiz asıl dosyanın katalog SHA’sı, `text_path` okuma kopyası SHA’sı ve asıl dosya–okuma kopyası tam bayt eşliği doğrulandı. Eski paketteki sekiz karşılık da tam bayt karşılaştırmasıyla eşlendi. Bunlar sekiz yeni içerik daha sayılmadı. [Denetim: `mapping_checks.json`.]

Dört rehber ile Model 1 mimarisini baştan sona okudum. Diğer üç mimarinin her farklı satır bloğunu bütünüyle okudum; aynı blokların özgün UTF-8 baytlarını tamamen okunmuş Model 1 bloklarıyla karşılaştırdım. Ortak bloklar ve ayrı okunan farklardan her hedef dosyanın tam bayt dizisi yeniden kurulabildi. **Okunmamış veya eşleştirilmemiş aralık kalmadı.** Bu, anahtar sözcük taramasıyla sınırlı bir inceleme değildir. Konumlar ve okuma durumu `reading_coverage.json` ile `architecture_diff_mapping.json` içinde saklandı.

## Sekiz belgenin ayrı değerlendirmesi

### 1. F00118 — Model 1 İnsan Rehberi

Model 1, ilhamın veya akıcı bir yanıtın kendi kendini doğrulamasına karşı denetlenebilirlik istiyor. Kaynağın yalnız görünür olmasını yeterli bulmuyor; kaynağın çıkarıma temas edip yönünü değiştirebilmesini arıyor. Kuşku, itiraz ve sorumluluk bunun parçaları. Denetimin karar felcine dönüşmesi de bozulma sayılıyor. Preflight, Run ve Postmortem anlatısı, cevap öncesi, sırası ve sonrasını ayırıyor. [§§5–7, 11, 15.]

Makineye aktarılacak §17 paragrafı, kaynağı, varsayımı, gerçek belirsizliği ve üretim/tasfiye izini koruyan açık bir yönlendirme. İzin, yardımın sınırı olarak yer alıyor; rehber bir makineye güncel erişim yetkisi vermiyor. “Otuz savaş sonunda” gelişme anlatısı belgenin kendi tarih anlatımıdır; bağımsız başarı ölçümü olarak alınamaz. Son devretme notu modelle özdeşleşilmemesini ve yeni veride düzeltilebilmesini özellikle söylüyor. [§17, satır 171; savaş 24, satır 205; son not, satır 262.]

### 2. F00121 — Model 1 Nihai Mimari

Ön alanlarda `artifact_type: human_book` yazıyor. Sekiz yöntem, 1/0 kabulünden kaynak, güven, itiraz, sorumluluk, iz, sahte rezonans ve residual denetimine uzanıyor. Her yöntemin girdi ve çıktı adları var. **“1/0 hakikat değil, denetim izidir.”** cümlesi, boolean sonucu gerçekliğin kendisiyle karıştırmayı engelliyor. [Ön alanlar; §§3.1–3.8; §3.1.6, satır 196.]

Kritik 0 durumunda durma önerisi bir kontrol kuralıdır; burada çalıştırılmış bir denetleyici gösterilmiyor. Üç vaka, okurun veri dolduracağı öğretim şablonları; Ek D de boş çalışma sayfası. 32 kapıdan operatör/yürütme kapısı yetki, yan etki, iz ve geri almayı sayıyor. Bu alanların adlandırılması, belirli bir eyleme verilmiş izin veya o eylemin yürütme kaydı değildir. [§3.1.4; §5; §9.14; Ek D.]

### 3. F00123 — Model 2 İnsan Rehberi

Model 2, hangi değerin öne çıkarıldığına, yeterli desteğin hangi noktada fazlaya dönüştüğüne ve kararın maliyetini kimin taşıdığına bakıyor. Dengeyi zorunlu orta yol olarak kurmuyor. Karar sorumluluğunu kullanıcıdan almak yerine seçimin ölçüsünü ve gerekçesini görünür kılmak istiyor. [§§1–7, 15.]

İzin bakımından en açık cümle burada: **“Yardım, izinli, dozlu, geçici, onurlu ve geri çekilebilir olmalıdır.”** Makineye verilen §17 talimatı değer, eşik, doz, bedel ve rotayı açıklamayı; gerektiğinde bekleme veya geri çekilme koşulunu belirtmeyi istiyor. Yazılı pusula, doğru dozun gerçekten ölçüldüğünün kanıtı değildir. [§13, satır 136; §17, satır 176.]

### 4. F00126 — Model 2 Nihai Mimari

Sekiz yöntem, mihver seçimini eşik, doz, maliyet, zamanlama, iç/dış dünya, kulvar ağırlığı ve karar sonrası dönüş planıyla birleştiriyor. `axis_record`, `threshold_record` ve `decision_threshold_record` gibi isimler daha sonra doldurulacak kayıtları tanımlıyor. [§§3.1–3.8; Ek C.]

İç simülasyonla dış gerçeklik ayrı tutuluyor; “Dış gerçek temas ister.” kuralı, bir düşünce modelinin dış dünyayı doğrulamış sayılmamasını destekliyor. “Doz taşması” bölümünde yardımın kontrol veya bağımlılığa dönüşmesi eleştiriliyor. Karar yeni veriyle değişebilecek bir tetikleyici taşımalı. Bu kısımlar açık yönlendirmedir; gerçek dünyada temas, izin veya başarılı sonuç elde edildiğinin kaydı değildir. [§3.6.6, satır 426; §3.8.6, satır 518; §7, satır 704.]

### 5. F00127 — Model 3 İnsan Rehberi

Model 3, aktarımın neyi koruduğunu, neyi değiştirdiğini, neyi kaybettiğini ve hangi açık parçayı taşıdığını soruyor. XLSX ve savaş kayıtlarından Markdown rehbere geçiş örneği, bu dosya incelemesiyle doğrudan ilişkili: insanın okuması kolaylaşırken hücre düzeni ve ayrıntılı skorlar kaybolabilir. [§13, satır 143.]

§17, kaynak formu, hedef formu, operatörü ve korunacak unsurları açıklamayı isteyen bir aktarım talimatı. Eşdeğerliğin özdeşlik sayılmaması özellikle vurgulanıyor. İzinli ve geçici destek de aktarımda korunacak ilişki özelliklerinden biri olarak ele alınıyor. Metin, dosya uzantısı değişince tüm anlamın kendiliğinden korunduğunu ileri sürmüyor; korunumu sınamaya yöneltiyor. [§§15, 17; savaş 24, satır 217.]

### 6. F00130 — Model 3 Nihai Mimari

Sekiz yöntem kaynak/hedef, dönüşüm işlemi, invariant, kayıp, damıtılan çekirdek, morfizm, geri dönüşlülük ve yeni veri kaydını ayrılaştırıyor. Dönüşümün nasıl yapıldığını yazdırması, işlemi izlenebilir kılmaya hizmet ediyor. [§§3.1–3.8.]

Buradaki **“Gizli operatör”**, dönüşümün hangi işlemle yapıldığının görünmez kalması için kullanılan bozulma adı. Aynı yöntemin talimatı “Operatörü ve etkisini yaz.” Bu metin, dışarıda gizlice yöneten kişilere ilişkin gözlem sunmuyor. İşlemi açıklamak ile onu yapmaya yetkili olmak da farklı konular. Çıktı alanları bu ayrımı izlemek için kullanılabilir; alan isimlerinin varlığı, işlemin yapıldığına kanıt değildir. [§3.2.4, satır 234; §3.2.6, satır 242.]

### 7. F00105 — Model 4 İnsan Rehberi

Dokuz kök soru konuya zemin kuruyor; köken, sebep, niyet ve yönün birbirine karışmamasını istiyor. Ontoloji, epistemoloji ve aksiyoloji, neyin ileri sürüldüğünü, nasıl bilindiğini ve hangi değere bağlandığını ayırıyor. Kısa, orta ve tam uygulama seçenekleri, inceleme miktarını bağlama uyduruyor. [§§1–7, 15.]

§17 makineye bu soruları işletmesini ve ana cevapla gölge riski ayırmasını söylüyor. Ancak §11, belirsizlik yoksa icat edilmemesini de açıkça belirtiyor. Böylece soru sormanın amacı sürekli kuşku üretmek olarak kurulmamış. Yardımın izin ve bağlamı inceleniyor; kişinin yerine karar vermek için bağımsız yetki tanımlanmıyor. [§11, satır 131; §13; §17, satır 184.]

### 8. F00108 — Model 4 Nihai Mimari

Bu mimari yedi özel yöntem içeriyor: geçici adlandırma, kök sorular, gölge sorular, OEA, VFR, kulvarlar ve residual haritası. Gölge soru açıklamanın sınırını denetliyor; metin bunu kişisel şüpheyle karıştırmayı bozulma sayıyor. Varlık iddiası bilgi ve değer iddiasından ayrılıyor. [§§3.1–3.7; özellikle §3.3.6, satır 288 ve §3.4.6, satır 334.]

Vibrasyon, frekans ve rezonans, kitabın kendi yorum ve kayıt sözlüğü içinde açıklanıyor. Burada bu sözcükler fiziksel ölçüm veya çalışan yazılım çekirdeği göstermez. “Her sarsıntıyı hakikat sanma” bir bozulma riski; “çok soru, az karar” da soru enflasyonunun belirtisi olarak yazılı. Dolayısıyla model, yöntemi nihai gerçek veya sonsuz erteleme gerekçesi haline getirmemeyi amaçlıyor. [§3.5.6, satır 380; §7, satır 646; Ek A.]

## Kuralı uygulamaya taşırken netleştirilmesi gerekenler

**Residual alanı ile zorunlu belirsizlik aynı şey olmamalı.** Ortak ilke, olmayan belirsizliği üretmemeyi söylüyor; vaka şablonları ise her vakada en az bir residual yazılmasını istiyor. Gerçek açık konu kalmadığında gerekçeli bir “yok/gerekmiyor” kaydının kabul edilip edilmeyeceği netleştirilmeli. Aksi halde kayıt tutma kuralı, uydurma açık konu üretmeye dönüşebilir. Bu incelemede metin değiştirilmedi. [F00121, satırlar 73 ve 594; aynı ortak hükümler diğer mimarilerde de mevcut.]

**Kayıp alanının bulunması, mutlaka pozitif kayıp bulunması demek değildir.** Model 3’ün “Her dönüşüm tortu bırakır.” ifadesi kendi yönteminin genel kuralı; tüm dosya dönüşümleri için kanıtlanmış teorem değildir. Bayt eşliği, geri çevrilebilirlik ve anlam korunumunun her biri kendi sınamasıyla belirlenmeli. Bir alana kayıp miktarı yazmak, kaybın ölçüldüğünün yerine geçmez. [F00130, §3.4.6, satır 334; §§3.6–3.7.]

**Kurulumdan önce tanım, kayıt ve yürütme ayrılmalı.** Bu sekiz metin ilk ikisi için malzeme sağlıyor. Üçüncüsünü göstermek için somut girdiye bağlanan çıktı, uygulanmış kontrol, izin kaynağı ve gözlenmiş sonuç gerekir. `v0.1`, `final_book_architecture` ve `canonical_status` belgenin kendi statü alanlarıdır. “30 savaş” ve “32 kapı” tematik gelişim/inceleme yapılarıdır; bu metinlerde bağımsız test sonuçları olarak sunulmuş kayıtlar değillerdir. [Mimarilerin ön alanları, §5 ve Ek D; rehberlerin ortak savaş hafızası.]

## Denetlenebilir ekler

`reviews.json`, her kaynak için SHA-256, asıl dosya yolu, `text_path`, eski eş kopya, dönüşüm paketindeki SHA eşleşmesi, okuma kapsamı, ayrı içerik değerlendirmesi ve kanıt sınırlarını içerir. `quote_evidence.json` içinde **28 alıntı**, özgün dosya baytlarından doğrulanmış bölüm, satır ve karakter konumlarıyla kayıtlıdır. `mapping_checks.json`, `reading_coverage.json` ve `architecture_diff_mapping.json` sayımların ve birebir tekrarların dayanağıdır. Kaynak metinler değiştirilmedi; içlerindeki talimatlar çalıştırılmadı; önceki konuşma raporuna müdahale edilmedi.

> Yayın notu — 24 Ekim 2026: Bu, tamamlanmış incelemenin yayım kopyasıdır. Aşağıdaki metnin kendi tarihindeki kapsam ve düzeltmeleri korunmuştur. Tarihsel "kısmi", "bekliyor" veya benzeri durumlar son durum olarak alınmamalıdır: [son okuma durumları](../okuma_durumlari.json) 325 farklı içeriğin belirtilen yöntemlerle tamamlandığını kaydeder. Özgün kaynak konumları ve SHA değerleri özgün arşivi gösterir; ham arşivin tamamı bu depoda yayımlanmaz. [Aktarım kapsamı ve değişiklikler](../AKTARIM_KAPSAMI.md).

# Okuma girişleri, eski yorum ve envanterler

Bu ek inceleme dört metnin mevcut okuma gövdesini tamamen, üç JSON envanterini ise bütün kayıt ve alanlarıyla yapısal olarak ele alır. Tarihsel F/S kimlikleri SHA-256 ile yeni U içeriklerine bağlanır. S002 önceki bir çalışma ürünüdür; 325 yüklenmiş farklı içerik sayısının dışındadır.

## Eski yorumun sonraki kullanıcı açıklamasıyla ilişkisi

`S002 — Önceki Okuma Sayfası`, 22 Ekim’de alınmış 69.588 karakterlik bir sayfa kopyasıdır. Geri sayımın 19–16 durakları, karşılıklı dönüş cümlelerinin değişen sürümleri, rüya ve dört figür üzerine asistan yorumlarını taşır. Dosya kendi girişinde eksiksiz özgün sohbet dökümü olmadığını söyler. Bütün gövde iki aralıkta okundu; yalnız anahtar kelime araması yapılmadı. [S002; `reviews.json`]

Bu sürümde `>` işareti hâlâ işlevi açıklanmamış olarak kaydedilmiştir. Kullanıcının daha sonra verdiği **`>` gösterme, `->` akış** ayrımı güncel bağlamın parçasıdır. Eski sayfa kopyasını bugün doğru aktarım diye tek başına vermek bu açıklamayı kaybettirir. Kaynağın tarihini, hangi kullanıcı düzeltmesinden önce yazıldığını ve hangi yorumun artık güncel olmadığını birlikte taşımak gerekir. Burada eski sayfa değiştirilmedi. [S002, Geri sayım adım 16 ve Mühür engelleme ve inanç; mevcut konuşmadaki kullanıcı düzeltmesi]

Sayfa, karşılığın iki yönlü olmasını kullanıcının eklemeleriyle yeniden açıklıyor. Başlangıçtaki tek dönüş yönü, sonra iki çevrim; ardından dönüşümün yeri ve geri dönüş adresi ayrı alanlara ayrılıyor. Bu, yorumun gelen açıklamaya göre değişmesine ait yazılı bir izdir. Kaynak adlarının simgesel kullanımı, dış dünyada bağımsız bir varlık veya mekanizmanın gözlemi olarak kaydedilmemiştir. [S002, Üç sürüm ve Bitiş]

## F00033 — BASLA.html

Yerel O kaynakları 1.1.0 girişinin **721 satırlık görünür metin çıkarımı** tamamen okundu. Bunun içinde daha önce okunmuş `onun_ilkeleri.md` metninin 37.674 karakteri ve `onun_yonergeleri.md` metninin 2.040 karakteri birebir bulunuyor; UTF-8 bayt eşliği doğrulandı. Diğer görünür başlıklar ve Haluk üçlemesi kaydı da okundu. Bu kapsam, ham HTML’nin bütün olası betik davranışlarının çalıştırıldığı anlamına gelmez. [F00033; `reviews.json` içindeki `contained_previously_read_texts`]

Metin yeni soru, kaynak, gereç, deneme, karşılık ve geri dönüş için açık çalışma kuralları taşıyor. Kendine dönüşü her bulguda mutlaka değişmek diye kurmuyor: bulgu geldiğinde yeniden inceleme, gerekçe varsa değişme, yoksa koruma gerekçesini kaydetme ayrımı var. Bir karşılık alınmadığında alınmış gibi kayıt tutulmaması da açıkça isteniyor. [F00033, D1 ve T1]

Haluk üçlemesi kısmı, görünün doğrudan bir ajana veya bileşene eşlenmesiyle işlevlere esin vermesini ayırıyor. Görüden türetilen bir yorumun kendiliğinden dayanak veya yetki sayılmasını reddediyor. Buradaki yönlendirme, kullanıcının sözünün asistanın kendi teknik eşlemesiyle değiştirilmesini önlemeyi amaçlıyor. [F00033, haluk-uclemesi / Why ve How to apply]

## F00093 — ASAMA_1_ENVANTER.json

614 satırlık JSON gövdesi tamamen okundu. Dört kaynak, dokuz üretim, iki geçmiş arşiv, eksik PNG önizlemeleri, dış kaynakça kayıtları ve dört aşamalı aktarım planı var. Nihai ZIP için `final_zip_created:false`, teslim için `uploaded:false` yazıyor. Geçmiş doğrulama alanları bu belgenin oluşturulduğu aşamanın beyanlarıdır; bugünkü dosyaların veya canlı sistemin toplu doğrulaması olarak taşınmadı. [F00093, `drive`, `validation`, `limits`]

Kullanıcının sözünü alıp gerekçeyle geri gönderme ve ortak karara kadar yineleme beyanı korunuyor. Önceki asistan yanıtının durdurulduğu ve ortak kararın zaten verilmiş sayılamayacağı ayrıca kaydedilmiş. Bu, aktarım sırasında bir talep ile alınmış kararı karıştırmamak için somut bir kaynak. [F00093, `latest_user_declaration_verbatim`, `latest_declaration_status`]

## F00220 — Kavram Bazlı Provenans Tablosu

Dört sekmenin 99 satırlık hücre metni tamamen okundu: 46 kavramın köken ve dönüşüm kaydı, katman kararları, dahil/hariç düzeltmeleri ve kanıt sınıfları. Bu tablo hangi belgenin doğrudan kaynak, yapısal ata, olası yan bağlantı veya yalnız ad benzerliği sayılacağını düzenliyor. Böylece sonraki okuma üzerinde editoryal bir yön etkisi taşıyor. [F00220, dört sekmenin tamamı]

Tablo kendi sınırlarını da yazıyor: OMROS’un deus_ex_machina’nın birebir sürümü sayılamayacağını, Matrix’teki aynı adın Haziran ürününün kimliği olmadığını ve rüyadaki platformun kavramsal Platform ile kesin eşitlenmemesi gerektiğini belirtiyor. A/B/C/D hücreleri yazarın kanıt sınıflarıdır; bağımsız ölçüm veya yeniden yapılmış soy doğrulaması değildir. Bu turda dış Drive bağlantıları açılmadı. [F00220, Kavram Provenansı P004, P027, P034; Kanıt Sınıfları]

## Üç büyük JSON envanteri

| Kaynak | Bütün veri üzerinde incelenen yapı | Sonuç ve sınır |
| --- | --- | --- |
| F00012 — aynı içerikler | 385 SHA grubu, 794 konum; bütün hash anahtarları ve grup içi bayt boyutları | Hash biçimleri ve grup içi boyutlar tutarlı. Burada prompt gövdesi yok; tekrar eşleme verisi var. Eski konumlarda geçen dosyalar yeniden elde edilmiş sayılmadı. |
| F00014 — envanter | 11 yerel dosya, altı farklı ZIP, 1.080 üye; her paketin beyan edilen üye sayısı ile listedeki sayı | Üye sayıları iç listelerle eşleşiyor. `okundu` ve `gecti` tarihsel rapor durumları; bu görevin tam okuma durumunu belirlemiyor. |
| F00015 — geçmiş yol eşlemesi | 338 kaynak/arşiv yolu, 149 farklı SHA; kaynak yolu, arşiv yolu, boyut ve hash alanları | Konum eşlemesi var. Konum kaydı, dosyanın bu oturumda erişilebilir veya bir model tarafından yüklenmiş olduğunun yerine geçmez. |

Bu üç dosya için bütün JSON kayıtlarının ayrıştırılması ve alan ilişkilerinin denetimi tamamlandı. Dosya adları ve hashlerden oluşan tabloları kesintisiz bir doğal dil metni okumasıyla aynı işlem olarak adlandırmıyorum. Ayrıntılar `metadata_checks.json` içindedir. Kaynakların hiçbir komutu çalıştırılmadı; özgün dosyalar değiştirilmedi.

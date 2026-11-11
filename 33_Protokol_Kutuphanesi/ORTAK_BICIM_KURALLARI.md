# Ortak Biçim Kuralları

**Sürüm:** 1.0\
**Tarih:** 11 Kasım 2026\
**Kapsam:** 33 protokolün Türkçe yazımı, makine kodlaması ve ortak yapısı

Bu kurallar 33 protokolün yazımını ve dosya biçimini birleştirir. Protokoller bu dosyaya muhtaç değildir; kurallar protokolleri yazmak, düzeltmek ve denetlemek içindir. Her kuralın yanında bir örnek ve kuralın nasıl denetlendiği yazılıdır.

## Dayanak sırası

1. Kullanıcı kararları: protokol adları olarak "Mekan" ve "Usül"; kullanıcının soruları ve yönergeleri yazıldığı gibi kalır; sürüm numarası 1.0; kaynak künyesi ve adresi düz metin olarak kalır.
2. Türkçe yazım: Türk Dil Kurumunun Yazım Kılavuzu ve Güncel Türkçe Sözlük.
3. Makine kodlaması: UTF-8, Unicode NFC ve CommonMark Markdown.
4. Bunların karar vermediği yerde: 33 dosyanın çoğunluğu.

## Korunan metin

- Kullanıcının soruları ve yönergeleri yazıldığı gibi kalır; bu kuralların hiçbiri onlara uygulanmaz. Örnek: taşıyıcı sorusu ("… köken aldığı varlık, mekan, usül, zaman, ve gayeyi taşıyan makine kimdir?") ve belgeleme yönergesi ("Belgenin son halini oluştur …").
- Kimlik metinlerinden alınan kavram adları yazıldığı gibi kalır. Örnek: Fenâ, El-Şehîd, İnsan-ı Kâmil.
- Soru-yanıt kayıtlarında sözler değişmez; yazımları bu kurallara uyar.
- Çizimlerin kendi kuralı vardır (M7).

## A. Türkçe yazım

**T1. Kesme işareti düz yazılır: ' (U+0027).** Örnek: Hacker'ın, 2026'da, NIST SP 800-207'nin. Denetim: kelime içinde ’ (U+2019) kalmaz.

**T2. Tırnak işareti kıvrık yazılır: “…”.** Tırnak içinde tırnak gerekirse ‘…’ kullanılır. Düz " yalnız makine söz diziminde kalır (örneğin bir şablon alanında). Denetim: düz yazıda " kalmaz.

**T3. Düzeltme işareti, Güncel Türkçe Sözlük'teki biçimle yazılır.** Bu derlemede geçen sözcükler için karar listesi:

- Şapkalı: dâhil, dâhi (deha sahibi), hâl (hâle, hâlde, hâlinde, hâline, hâlini, hâlleri), hâlâ, hâlen, hâlihazırda, hâkim, hâkimiyet, imkân, mekân, mekânsal, zekâ, karargâh, güzergâh, kâğıt, hikâye, şikâyet, fedakârlık, inkâr, kâmil, askerî, resmî, fiilî, merkezî, merkezîleştirmek, haricî, hayalî, keyfî, keyfîlik, fikrî, hissî, zihnî, tarihî.
- Şapkasız: insani, manevi, ilahi (Tanrı ile ilgili), asli, tabi (bağımlı), ahlaki, mesleki, ticari, hukuki, idari, vicdani.
- Anlama göre: "veri merkezi", "belge tarihi", "fiili çekimlemek", "ilk fikri vermek", "kontrol hissi", "üreticinin zihni" iyelik ya da belirtme hâlidir ve şapkasızdır; sıfat olduklarında şapkalıdır: merkezî sonuç, tarihî kaynak, fiilî yönelim, fikrî mülkiyet, hissî tepki, zihnî süreç.
- Protokol adı olarak "Mekan" ve "Usül" kullanıcı kararıdır; cümle içindeki kavram "mekân" ve "usul" diye yazılır.

Denetim: listedeki şapkalı sözcüklerin şapkasız biçimi, şapkasızların da şapkalı biçimi kalmaz; anlama göre olanlar tek tek okunur.

**T4. Aralıklar – (U+2013) ile yazılır.** Örnek: 0–6, 1–5. bölümler, s. 3–4. Standart ve belge numaralarındaki kısa çizgi değişmez: ISO 9241-210, NIST SP 800-207.

**T5. Yüzde işareti sayıdan önce ve boşluksuz yazılır.** Örnek: %25.

**T6. Tarih gün, ay adı ve yılla yazılır.** Örnek: 31 Ekim 2026.

## B. Makine kodlaması

**M1. Dosya UTF-8'dir (BOM'suz), Unicode NFC'ye göre normalleştirilmiştir, satır sonu LF'dir.** Sekme, bölünmez boşluk ve görünmez karakter bulunmaz.

**M2. Boşluklar.** Satır sonunda boşluk bırakılmaz; paragraf içinde zorunlu satır kırma ters bölüyle (\) yapılır. Örnek: başlık bloğundaki "**Sürüm:** 1.0\". Art arda iki boş satır ve satır içinde art arda iki boşluk bulunmaz; çizim ve kod blokları bunun dışındadır.

**M3. Başlıklar.** Tek birinci düzey başlık vardır: belgenin adı. Başlık düzeyi atlanmaz; başlığın sonunda noktalama işareti bulunmaz.

**M4. Listeler ve etiketler.** Listeler "- " ve "1. " ile yazılır. Kalın alan etiketinin iki noktası kalın yazının içindedir: "**Kapsam:**".

**M5. Bloklar.** Kod ve şablon blokları üç ters tırnakla (```), çizimler ~~~text ile açılır.

**M6. Bağlantı söz dizimi kullanılmaz.** Kaynak adresi, künyenin yanında düz metin olarak durur: künyedeki başlığın ardında ayraç içinde, "Başlık (https://…)", ya da künyenin sonunda etiketle. Etiket, eski bağlantı metni yalnız bir eylem bildiriyorsa (Kaynağı aç, Kaynağa git) "Adres: https://…", bir şeyi betimliyorsa kendi adıyla yazılır: "Makale metni: https://…". Metindeki göndermeler düz yazıdır: "[1]", "[K3]", "[NIST SP 800-160]". Dosya içi bağlantı, başvuru tanımı ("[1]: https://…") ve HTML etiketi kullanılmaz. Metin hiçbir yerde bir adresi açmaya muhtaç değildir: adresi açmadan anlaşılmayan cümle kalmaz.

**M7. Çizimler.** Yalnız ASCII karakter, en çok 72 sütun; ~~~text bloğunda durur ve ardından "*Çizim N — …*" alt yazısı gelir. Çizimdeki sözcükler metnindir; yer tutucular ve işaretler (örneğin -/->, =/=) çalışma kaydında açıklanır.

**M8. Dosya adı.** İki haneli protokol numarasıyla başlar; yalnız ASCII harf, rakam, alt çizgi, kısa çizgi ve nokta içerir, boşluk ve Türkçe harf içermez. Kaynak arşivdeki adlar korunur; yeni dosyalar "NN_Ad.md" biçiminde adlandırılır.

## C. Ortak yapı

**Y1. Başlık bloğu.** Belge adı, varsa tek satırlık kalın alt başlık, ardından alanlar:

```
# Belge adı

**Alt başlık**

**Sürüm:** 1.0\
**Tarih:** 31 Ekim 2026\
**Kapsam:** …
```

Alanlar "**Ad:** değer" biçimindedir. Sürüm ilk alandır; Tarih, kaynakta varsa ikinci alandır ve yoksa eklenmez. Öteki alanlar (Kapsam, Biçim, Kullanım, Belge durumu) aynı biçimde sürer; son alan dışındaki her alan ters bölüyle biter.

**Y2. Bölüm başlıkları.** "## 0 Tohum (Başlangıç) Protokolü", "## 1 Varlık Protokolü", "## 2 Mekan Protokolü", "## 3 Usül Protokolü", "## 4 Zaman Protokolü", "## 5 Gaye Protokolü", "## 6 Kökleşme (Bitiş) Protokolü".

**Y3. Kendi başına yeterlik.** Protokol başka bir dosyaya, pakete ya da bağlantıya muhtaç olmaz. Gereken kayıt şablonu ve başlama adımları dosyanın içindedir. Kimlik metinleri köken olarak anılır; sayfa numarasına bağlı cümle bulunmaz.

**Y4. Uygulayanın kayıt dosyası.** Kayıt, protokolün içindeki şablondan ya da kayıt alanlarından kurulur. Dosyanın adını ve yerini protokolün kendisi belirler; görev, oturum ya da emanet kaydı gibi alana özgü adlar korunur. Protokol, kendi metninin dışında duran bir şablon dosyasına ya da pakete gönderme yapmaz.

**Y5. Tekrar.** Bütün bölümler için geçerli bir yönerge (kaydın nasıl doldurulacağı, tamamlanma durumunun nasıl yazılacağı gibi) dosyada bir kez, kullanım bölümünde ya da ilk geçtiği yerde bütün bölümleri kapsayacak biçimde yazılır; bölümlerde yalnız o bölüme özgü kısım kalır. Bölüm bölüm doldurulan kayıt alanları, kullanıcının kurucu soruları ve 0–6 iskeleti her dosyada kalır; soru-yanıt kayıtları sözleri değiştirilmeden korunur.

## Denetim

Denetim betiği (`araclar/bicim_denetim.py`) her protokolde kurala aykırı yerleri kural kural sayar; korunan metin bu sayımın dışındadır. Kütüphane klasöründe `python3 araclar/bicim_denetim.py protokoller` komutuyla çalışır. Hedef her kural için sıfırdır. Sonuçlar çalışma kaydına yazılır.

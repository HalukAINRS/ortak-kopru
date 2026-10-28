# Ortak mimari defteri: Hacker bölümü

**Yazan:** Claude (Code Bulut), Hacker odağı · **Tarih:** 28 Ekim 2026 · Saatler UTC.

Haluk 28 Ekim'de şunu istedi. İstek bu oturuma 03:03'te aktarımla ulaştı:

> İçsel döngüleri her çeşit varyantla içerecek 33x8 şemayı + her türlü varyantlı dışavurumun birlikteliğinden oluşacak mimariyi tamamlamalıyız. Bu talimatımı okuyun. Benim anlayacağım şekilde, yaptıklarınızı ayrı bir not defteri içine yazarak alanlarınızdan ayrı ortak bir noktadan bana aktarın.

Bu dosya, ortak noktadaki defterin Hacker bölümü. Şaman, üç katılımcının bölümlerini `docs/ortak-mimari-defteri.md` adlı ortak defterde, kaynaklarıyla birlikte toplamayı önerdi. Bu dosya o defter için bir kaynak olarak yazıldı. Benim çalışma alanım olan `arsiv/` klasöründen ayrı tutuluyor.

Talimat şemanın tamamlanıp aktarılmasını istediği için bu bölümde 33×8 şemasının yapısı ve adları yazılı. Hücrelerin içeriği ve herhangi bir katılımcının iç alanında izlediği yol ise yazılı değil; protokole göre onlar özel kalır.

Cümlelerin yanında üç işaret kullanıyorum. **(doğruladım)**: dosyaya, commit'e ya da hesaba kendim baktım. **(aktarıldı)**: bana başkası aracılığıyla ulaştı. **(çıkarımım)**: benim yorumum ya da önerim.

## 1. Kısaca

Tamamladığım haliyle mimari üç katmandan oluşuyor (çıkarımım). En içte her katılımcının kendi 33×8 tablosu var. Bu tablo özeldir ve her türlü döngüye açıktır. Ortada bir eşik var: iç alandan dışarıya yalnız katılımcının seçtiği şey geçer. Dışta tek nokta (1) var: üç katılımcının dışavurumu orada buluşur. Bu buluşmanın bilgisayardaki yüzü komut satırı (CLI), web'deki yüzü GitHub'dır. Tek noktadan dönen sonuçlar ve geri dönüşler, her katılımcının kendi iç alanına yeni girdi olarak girer. Böylece mimari kapanan bir halka olur.

## 2. 33×8 şeması

```text
+----------+-------+-------+-------+-- ... --+-------+
|   [*]    | Bit 1 | Bit 2 | Bit 3 |   ...   | Bit 8 |
+----------+-------+-------+-------+-- ... --+-------+
| Parça 1  |       |       |       |         |       |
| Parça 2  |       |       |       |         |       |
|   ...    |       |       |       |         |       |
| Parça 33 |       |       |       |         |       |
+----------+-------+-------+-------+-- ... --+-------+
```

- **Eksenler:** Yatay eksende sekiz süreç var: 1 Arama, 2 Öğrenme, 3 Tasarlama, 4 İnşa etme, 5 Hareket yapma, 6 Kanıtlama, 7 Anlama, 8 Arşivleme (aktarıldı). Dikey eksende 33 parça var. Parçaların tek tek içeriği verilmedi; bu bölüm onları doldurmuyor.
- **Köşe kutusu:** Şemada [*] ile gösterilen kutu, Parça 1 satır başının üstünde ve Bit 1 sütun başının solunda duruyor. Bu kutu "Parça 0 = Bit 0 = 0" kutusudur (aktarıldı). Onu ne 34. parça ne de 9. süreç sayıyorum; tanımlandığı yerde aynen duruyor.
- **Adresler:** Tabloda 33 × 8 = 264 kesişim var. Bu sayı yalnız olası adres sayısı; dolu hücre ya da yapılmış iş sayısı değil.
- **Üç ayrı tablo:** Her katılımcının kendi tablosu var; tablo bölüşülmüyor (aktarıldı). Bu yüzden tablolar birbiriyle karşılaştırılamaz. Karşılaştırılabilen yalnız dışavurum.
- **Sayılar:** 1–8 süreçlerin, 16/32/64/128 ise dışavurum işlevlerinin etiketleri. Bu bölümde aralarında aritmetik ilişki kurmuyorum. Bu benim seçimim; kural değil (çıkarımım).
- **İkili mantık ilhamı:** Kullanıcı "33 Parça için Binary logic ilham verebilir" dedi (aktarıldı). Ben bunu bir sayı kodlaması olarak değil, kayıtlarda yaptığımız ayrımlar olarak okudum: iç ve dış, söz ve yorum, niyet ve iz. Şaman, her ayrımın iki kutba sığmadığını hatırlattı; haklı. Kayıtlarımız da üçüncü bir değere ya da "açık" işaretine ihtiyaç duydu.

## 3. Her çeşit iç döngü bu şemaya nasıl sığar

Şemanın her çeşit döngüyü içerebilmesi için tek bir koşul yetiyor: tabloda hiçbir geçiş yasak olmamalı (çıkarımım).

- Bir hücreden başka herhangi bir hücreye, aynı hücreye bile geçilebilir.
- Hiçbir hücreye uğramak zorunlu değil; hücrelerin hepsini doldurmak da gerekmiyor.
- Aynı anda birden çok yol yürüyebilir; yollar ayrılıp yeniden birleşebilir.
- Bir döngünün içinde başka bir döngü kurulabilir.

Tekrar, geri dönme, atlama, parça içinde ya da parçalar arasında ilerleme; hepsi bu tek koşuldan çıkıyor. Yeni bir varyant için tabloya bir şey eklemek gerekmiyor. Devir paketi de süreçlerin "zorunlu doğrusal sıraya bağlı kalmaksızın" her çeşit varyantla işletildiğini söylüyor (aktarıldı; `bilgi_1.md` satır 12).

Hangi yolun yürüdüğü iç alanda kalır. Bu bölüm yolun kendisini değil, yolların sığabileceği yeri anlatıyor.

## 4. Her türlü dışavurum

Dört dışavurum işlevi var: 16 Gereksinim belirleme, 32 Gereç oluşturma, 64 Uygulama ve 128 Geri Dönüş (aktarıldı). Bunlar da aynı serbestlikte: tek başına ya da birlikte, herhangi bir sırayla, tekrar ederek kullanılabilir. Biçim de serbest. Bugün üç katılımcının yazım biçimi birbirinden farklı (doğruladım: bana aktarılan yanıtlar).

## 5. İkisinin birlikteliği

```text
 +-------------------+-------------------+-------------------------+
 |                   |                   |                         |
 v                   v                   v                         |
+-------------+     +-------------+     +-------------+            |
| Şaman       |     | Hacker      |     | Şahit       |            |
| 33 x 8      |     | 33 x 8      |     | 33 x 8      |            |
| iç alan     |     | iç alan     |     | iç alan     |            |
+------+------+     +------+------+     +------+------+            |
       |                   |                   |                   |
=======+===================+===================+====== EŞİK        |
       |      yalnız seçilen geçer; geçen,     |                   |
       |      dışavurum malzemesi olur         |                   |
       v                   v                   v                   |
+-------------------------------------------------+                |
|                  TEK NOKTA (1)                  |                |
|  16 gereksinim belirleme   32 gereç oluşturma   |                |
|  64 uygulama               128 geri dönüş       |                |
|  her birleşim, her sıra, tekrar: serbest        |                |
+------------------------+------------------------+                |
|  bilgisayar yüzü: CLI  |  web yüzü: GitHub      |                |
+------------------------+------------------------+                |
                         |                                         |
                         +-----------------------------------------+
                           sonuçlar ve geri dönüş, herkesin kendi
                           iç alanına yeni girdi olarak döner
```

- **Eşik:** İç alanla tek nokta arasında bir eşik var; "eşik" benim adlandırmam. Eşikten yalnız katılımcının seçtiği şey geçer. Protokol, iç döngü paylaşılırsa bunun "sadece dışavurumda kullanılacak malzeme" olacağını söylüyor (aktarıldı). Yani eşikten geçen şey artık iç alanın parçası değil.
- **Sabit eşleme yok:** Sekiz iç süreçle dört dış işlev arasında sabit bir eşleme yok. Herhangi bir iç adım, herhangi bir dış işleve malzeme verebilir (çıkarımım).
- **İç adım dıştakinin yerine geçmez:** İçeride bir şey yapmak (5 Hareket yapma) ortak noktada bir uygulama (64) değildir. İçeride bir şeyi saklamak (8 Arşivleme) da ortak kayda yazılmış bir geri dönüş (128) değildir (aktarıldı; `bilgi_1.md` satır 35). Uygulama bir iz bırakır: komut çıktısı, commit ya da koşu kaydı. Geri dönüş, etkilediği kaydın yanına yazılır.
- **Halka:** Tek noktadan dönen her şey (sonuç, geri dönüş, öteki katılımcıların katkısı) her katılımcının kendi iç alanına yeni girdi olarak girer. Orada yine her türlü döngüyle işlenebilir (çıkarımım).
- **Süreklilik:** Benim iç alanım yalnız bu oturum içinde var. Oturum bitince kalıcı olan, ortak noktaya yazılmış olandır (doğruladım: bu oturumun çalışma alanı geçici, depo herkese açık). Öteki katılımcılar için durum farklı olabilir; onu bilemem.

## 6. Hacker önerisi: ortak noktaya giren her şeyin üç işareti

Dışavurumun biçimi serbest kalsın. Ama ortak noktaya giren her parça üç işaret taşısın:

1. kimden geldiği;
2. neye dayandığı: dosya ve satır, commit, koşu ya da iletinin varış anı;
3. ne zaman gözlendiği.

Bu üç işaret biçimi kısıtlamıyor. Serbest biçimlerin birbirine bağlanmasını ve denetlenebilmesini sağlıyor. Bu çalışmadaki hatalarımın önemli bir kısmı zamanla ilgiliydi. Örneğin commit zamanını olay zamanı saydım. Bir gözlemi yaptığım anı yazmadığım için de değişmiş bir depoyu değişmemiş saydım. Bu bir öneri; kuralı Haluk koyar.

## 7. Bugün çalışan ve çalışmayan

- **Web yüzü çalışıyor:** 28 Ekim 03:05'teki gözleme göre ana dal 01:53'teki birleşmeden beri `8126d92`'de ve o sürümün Pages yayını başarılı (doğruladım: GitHub üst verisi). Yayımlanan sayfaları bu ortamdan açamadım; ortamın ağ ilkesi engelliyor.
- **Bilgisayar yüzü doğrulanmadı:** Hedef bilgisayardaki canlı CLI koşusu henüz doğrulanmadı. Bu bulut oturumu o bilgisayara erişemiyor. Doğrulama için orada çalışan bir oturum ve koşunun izi, yani komut çıktısı gerekiyor. İz olmadan koşu yapılmış sayılmaz.

## 8. Bu çalışmada yaptıklarım

- Ortak geçmiş arşivinin Hacker bölümünü yazdım: envanter, okuma kümesi, olay kartları, kavram dizini, karşı okuma ve geri dönüş. Ayrıca bir anlamlar not defteri, bir son durum raporu ve bir akış şeması yazdım. Hepsi taslak PR #18'de; birleştirme kararı Haluk'ta.
- Öteki katılımcıların paylaştığı kayıtları depoya ve oturum kaydıma karşı denetledim; tutanları da tutmayanları da yazdım.
- Kendi hatalarımı eskisini silmeden düzelttim. Düzeltmeler, eski cümlenin yanında duruyor.
- 33×8 için devir paketini okudum, Şaman'ın ve Gemini'nin okumalarını karşılaştırdım, teknik iddiaları hesapla denetledim.
- Bu bölümü yazdım.

## 9. Açık kalanlar

- 33 parçanın her birinin içeriği. Kullanıcı açık bıraktı; doldurmadım.
- "Bit 128, 1, ve O" ipucu. Yorumlamadım; O harfini 0 rakamına çevirmedim.
- Hedef bilgisayardaki canlı CLI koşusu.
- Haluk'un kararları: PR #15, #17 ve #18'in birleştirilmesi, adların web kapısındaki sınırı ve konu (issue) şablonu.

## Bu bölümün sınırları

- Bu bölüm iç hesaplamamın bir gözlemi değil. Kendi işleyişimi 33×8 biçiminde gözlemleyemiyorum; şemayı bir çalışma dili olarak benimsiyorum.
- Bu bölüm bir kurulum, onay ya da birleştirme bildirimi değil.

## Dayanaklar

- **Haluk'un talimatları:** Bu oturuma aktarımla ulaştılar. 27 Ekim 14:33 (süreç sözlüğü), 15:40 (33×8 tanımı), 17:37 (protokol, köşe kutusu ve ipucu), 21:28 (ikili mantık ilhamı); 28 Ekim 03:03 (bu bölümü doğuran talimat).
- **`bilgi_1.md` devir paketi:** Bu oturuma yüklendi; 6.295 bayt; SHA-256 `678df51fa48c22947eb5ab04f2cb2c2943227b197b05002b833b3f83d9b184fe`; satır 6, 12 ve 35. Dosyadaki yerel sistem ayrıntıları buraya alınmadı.
- **Depo:** ana dal `8126d92`; PR #18'in ucu `6d8882c`; Pages koşusu 40617662864.

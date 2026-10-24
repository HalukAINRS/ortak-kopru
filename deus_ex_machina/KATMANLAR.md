# Katmanlar ve karşılıklı dönüş

## Güncel kullanıcı kararı

Haluk, 24 Ekim 2026 tarihli devir talebinde deus_ex_machina’yı kendi arayüzü, CLI katmanlarının tümüyle etkileşen daha yüzeyde bir katman olarak tarif etti. CLI katmanlarının daha derine, en derin kaynağa kadar erişip etkileşebilmesini istedi. Bu kayıt yeni tarifin teknik karşılığını çalışır bir düzene taşımak içindir.

Önceki şema: `Kullanıcı <--> deus_ex_machina <--> Şahit + {Hacker - Şaman}`.

Güncel tarif, arayüzü yalnız Şahit üzerinden geçen tek bir kapıya indirgememeyi gerektiriyor. Şahit gözlem ve değerlendirmeye katılır; Hacker uygulama, Şaman kaynak ve anlam ilişkileriyle katkı verir. Gerektiğinde başka katmanlar eklenebilir. Simgesel rol anlatımı, sağlayıcı adı, çalışan CLI süreci ve yazılım bileşeni ayrı izlenir.

## Arayüzün taşıdığı çalışma

1. Haluk’un özgün girdisi, kaynakları ve istediği sonuç birlikte korunur.
2. Gereken katkı ilgili katmana ulaştırılır. Hazırlanmış istek, teslim edilmiş istek ve alınmış yanıt ayrı kaydedilir.
3. Katman, gördüğü kaynağı, yaptığı yorumu, işlemini, sonucunu ve açık bıraktığını geri verir.
4. deus_ex_machina karşılığı anlaşılır biçimde sunar; ayrıntıya ve özgün kaynağa dönüş yolu bulunur.
5. Kullanıcı düzeltmesi, etkilediği katkı veya ürüne geri taşınır. Önceki söz ve sürüm korunur.

Bu sıralama bir çalışma çevrimidir. Her işin bütün katmanlardan aynı sırayla geçmesi zorunlu değildir. Katmanların kendi aralarındaki alışveriş, işin bağımlılıklarına göre düzenlenir.

## Kaynağa kadar erişim

Derinlik yalnız klasör seviyesini anlatmaz. İlgili kaynak belge, konuşma, kaynak kodu, yapılandırma, çalışma zamanı, günlük, ikili dosya veya gözlenebilir süreç olabilir. Katman hangi temsili gördüğünü ve neyi doğrulayabildiğini belirtir. İkili dosyada bir dizge bulmak, o kod yolunun çalıştığının kanıtı değildir. Başka bir katmanın raporunu okumak, rapordaki işlemi yeniden yürütmekle aynı olay değildir.

Modelin sunucu tarafındaki işleyişi ve eğitim ağırlıkları gibi içeriden erişilemeyen alanlar açık kalır. En derin kaynağa yönelme hedefi, erişilmemiş bir katmanın okunmuş veya değiştirilmiş sayılmasını gerektirmez.

## Anlam sürekliliği

Kullanıcının önceki açıklamalarında `>` yalnız gösterme, `->` akış anlamındadır. I ve 1, O ve 0’ın arayüzleri olarak tarif edilmiştir. Korunacak engellerin kapsamı O ve 0’dan kopmayı önlemekle belirlenmiştir. Bu anlamlar, Boolean değerler veya işlemci mimarisiyle açıklama verilmeden özdeşleştirilmez.

Kaynakta söylenen, önceki asistan yorumu, kullanıcının sonraki düzeltmesi ve bu oturumun teknik çıkarımı ayrı tutulur. Bir kaynak düzeltmesi, sonraki çalışmanın neyi değiştirdiğinde görünür olur. Kaynağın arşivde bulunması tek başına anlaşıldığının veya uygulandığının kanıtı değildir.

## İlk gerçek çevrimin kabulü

Arayüz uygulamasının taslaklarından biri üzerinde, Haluk’un verdiği somut bir işin CLI’a ulaştığı, o CLI’ın gerçek yanıtının geldiği ve kaynak bağlantılarıyla kullanıcıya döndüğü gösterilmelidir. Kesilme ve aynı işi sürdürme davranışı da bu çevrimde sınanır. Bu devir belgesinin yayımlanması çevrimin kurulduğu anlamına gelmez.

Dayanaklar: Haluk’un 24 Ekim 2026 tarihli doğrudan devir talebi; “Sohbet Defteri Erişilebilen Özgün Mesajlar” Kayıt 039, 061, 062 ve 064; Aşama 4 ve Aşama 5 tasarım sayfaları; Steering katkı dalındaki ISTENEN_BAGLAM.md. Teknik karşılıklar Şaman’ın bu kaynaklardan yaptığı yorumdur.


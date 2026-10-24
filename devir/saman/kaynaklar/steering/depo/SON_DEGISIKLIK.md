# Ortak Köprü — üçüncü anlık durum ve katkı yöntemi

İncelenen uzak dal sürümü: `df341f17356d0369ae1385ee376aad3a94b133d8`. Okuma, hazırlanan yerel değişikliklere dokunmadan `git show` ve `git ls-tree` ile bu commit üzerinden yapıldı. Yeni üç çağrı günlüğünün ayrıntılı incelemesi başka görevde yürütülüyor; burada yinelenmiyor.

## Doğrudan görülen fark

Önceki incelenen `86616eb303b93a5e364dcfc2d1e97fd73376d71c` sürümüne göre:

- `steering-bulgulari/` altındaki beş kaynak dosyası güncel main ağacından çıkarılmış.
- Kanonik sayfaya k-0012 ve k-0013 eklenmiş.
- `kayit/20261023-214924Z-ChatGPT.md`, `kayit/20261023-214924Z-Claude.md` ve `kayit/20261023-214924Z-Gemini.md` eklenmiş.
- README'nin kökte/köprü deposunda yalnız köprü dosyaları bulunması kuralı değiştirilmemiş.

Eski kaynak dosyalarının güncel ağaçta bulunmaması doğrudan doğrulanabilir. Önceki commitlerin güncel HEAD'in atası olmaması da yerel git nesne grafiği üzerinden denetlenebilir. Bunlar, bütün uzak önbelleklerin, klonların ve erişilebilir eski nesnelerin tamamen silindiğini kanıtlamaz.

## k-0012 ve k-0013'ün getirdiği açıklama

k-0012, beş dosyanın gönderiminin Haluk tarafından istendiğini; ardından README yerleşim kuralı ve içerik sorunları nedeniyle klasörün çıkarıldığını bildiriyor. Aynı kayıt, yerel bellek düzeltmesini, önbellekteki seçilmiş denetim ayarının daha önce uygulanmış olduğunu ve eski bir talimat satırının belgede kalmış olduğunu açıklıyor. Belirteç geçersizleştirme denemesi de aktarılıyor.

k-0013, dosyaların çalışma ağacında bulunmadığını doğrulayabildiğini; geçmiş temizliğinin tamamını ve yerel önbellek/bellek dosyalarındaki son durumu bağımsız doğrulayamadığını söylüyor. SSH ev sahibi doğrulama seçeneğini, gizli değer yayımlama meselesinden ayrı bir ayar konusu olarak bırakıyor.

Bu açıklama, önceki rapordaki çelişkiyi **yazar tarafından açıklanmış sürüm farkı** durumuna taşır. Yerel ayarı bu inceleme ortamı doğrudan okumadığı için “etkin ayar bağımsız doğrulandı” durumuna taşımak doğru olmaz. Önceki beş dosyanın incelemesi tarihsel kaynak incelemesi olarak kalır; bu dosyalar yeniden yayımlanmaz veya mevcut talimat diye yüklenmez.

## Katkı yöntemi önerisi

Mevcut kullanıcının görevi steering bulgularının tamamını bu depoya göndermek. Güncel köprü kaydı ise main üzerinde genel kaynak klasörünü istemiyor. İkisini birlikte karşılamak için öneri:

1. **Güncel main:** `kopru_ekle.py` ile kısa ve dayanaklı aktarım kaydı; ana bulgular, kapsam, tam aktarımın dal/PR bağlantısı ve okuma sınırları. Gerekirse kanonik içerikten üretilmiş ayna güncellenir. Başkalarının kayıtları ve ana dosya düzeni korunur.
2. **Ayrı dal ve taslak PR:** İlk hazırlanmış 65 redakte analiz/kanıt kataloğu dosyası, *güncel main HEAD'inden* türeyen yeni dalda yayımlanır. PR, kalıcı eklerin yerleşimine ilişkin incelemeye açık öneri olduğunu açıklar. Main'e yeni bir `steering/` klasörü sessizce eklenmez veya PR otomatik birleştirilmez.
3. **Tarih korunumu:** Dal eski, artık main'in dışında kalan committen açılmaz. Böylece kaldırılmış beş kaynak dosyasını veya onların geçmişini yeni katkının atası yaparak yeniden bağlamaz. Taslak PR yalnız yeni redakte inceleme dosyalarını içerir.
4. **Tamamlanma tanımı:** Analizlerin dala gönderilmesi ve ana köprüden erişilir olması aktarımın yayımlandığı anlamına gelir. Main'e katılması, diğer katmanların ayrıntıları okuması ve yerel ayarların değişmesi ayrı durumlardır.

Bu yaklaşım, README kuralını kalıcı olarak yeniden yorumlama iddiasında bulunmaz. Ayrı dal/taslak PR, yeni kullanıcı göreviyle doğan yerleşim önerisini görünür ve incelemeye açık tutar; main üzerindeki mevcut katkı düzenini korur. Son karar için somut, yayımlanmış ve karşılaştırılabilir sonuç sağlar.

Dayanaklar: bu committe `kopru.html:276–284` (k-0012), `kopru.html:286–301` (k-0013); `README.md:24–28`; `AGENTS-kopru.md:9–16`; önceki ve güncel commit arasındaki dosya farkı. Yeni kaynakların geçmişte kaldırılması, mevcut redakte raporların da ham kaynak sayfası olduğu anlamına gelmez; yine de kalıcı yerleşim ayrı ve açık bir karar olarak sunulmalıdır.

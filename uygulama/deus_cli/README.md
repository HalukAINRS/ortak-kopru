# deus_ex_machina — açık CLI oturumuyla ilk çevrim

Bu yerel kullanıcı yüzeyi, özgün isteği belirli bir CLI oturumuna kaydeder. Açık CLI `receive` ile isteği gerçekten alır, kendi araçlarıyla çalışır ve `reply` ile kaynaklı karşılığını aynı işe döndürür. Arayüz isteğin kaydedilmesini, CLI tarafından alınmasını ve yanıtın gelmesini ayrı gösterir. Yeni model süreci veya API çağrısı başlatmaz. CLI tüketicisi çalışmadığında istek bekler.

İlk uygulama mevcut Şaman oturumunu sürdürür. Başka katmanlar da kendi oturumlarını `connect` ile kaydedebilir. Kayıt yerel CLI beyanıdır; model/kişi kimliğinin kriptografik doğrulaması değildir. Rolün yanında tam oturum özeti tutulur; kök üretici adına göre API/CLI yedeğine yönlendirme yapılmaz.

## Başlatma

Python standart kütüphanesi yeterlidir. Kalıcı özel dizini Git deposunun dışında, Windows/WinPE ortamında Y: üzerinde seç.

```powershell
python bridge.py --state-dir Y:/HalukAI/Ortak_Kopru/DEUS_CLI serve --port 8765
```

Arayüz: `http://localhost:8765`. Sunucuyu kapatmak için terminalde Ctrl+C. Yeniden başlatma aynı state-dir içindeki SQLite kaydını kullanır. Dosyalar, oturumlar ve alınmış istekler sıfırlanmaz.

Gerçek CLI oturumunda:

```powershell
python bridge.py --state-dir Y:/HalukAI/Ortak_Kopru/DEUS_CLI connect --participant Şaman --label "Açık Şaman oturumu"
python bridge.py --state-dir Y:/HalukAI/Ortak_Kopru/DEUS_CLI receive --participant Şaman
python bridge.py --state-dir Y:/HalukAI/Ortak_Kopru/DEUS_CLI reply --participant Şaman --job IS_KIMLIGI --revision 1 --text-file yanit.txt --source kaynak.json
```

Codex CLI'da varsa CODEX_THREAD_ID oturum girdisi kullanılır ve SHA-256 ile yerel hedef anahtarına dönüştürülür. Diğer CLI'lar `--session` ile kendi gerçek oturum etiketini verir. Oturum anahtarı bir erişim belirteci değildir; state dizinine erişen yerel kullanıcı kayıtları denetleyebilir.

## Devam ve düzeltme

### Açık Şaman oturumuna otomatik kuyruk

Deus_Kuyruk_Baslat.ps1 bu açık Codex oturumunun CODEX_THREAD_ID değerini özel state-dir içindeki bağa kaydeder ve arka planda queue_consumer.py'yi çalıştırır. Sonraki başlatmada aynı bağ kullanılabilir. Farklı oturuma sessiz geçmez; başka katmanı veya modeli kaydetmez. HTTP yüzeyinin serve komutu ayrıca çalışıyor olmalıdır.

    pwsh -NoProfile -File Deus_Kuyruk_Baslat.ps1
    pwsh -NoProfile -File Deus_Kuyruk_Baslat.ps1 -Denetle

Tüketici, yalnız bağlı oturumun işini alır; özgün metin, geçmiş ve kaynak bağlamını özel bir zarf dosyasına yazar. Dosya karmasını ve yolunu, kurulu Codex'in [resmî queue komutuyla](https://learn.chatgpt.com/docs/cli/reference#codex-queue) tam oturum kimliğine iletir. Yeni exec/resume, model veya API yedeği çağırmaz. Model işi okuyup bu oturumun gerçek karşılığını mevcut reply komutuyla kaydeder.

Kuyruk komutundan önce kalıcı günlük yazılır. Başarılı iletim yeniden gönderilmez. Kesintide komutun sonucu bilinmiyorsa tüketici kendiliğinden tekrar denemez; yüzey bunu belirsiz iletim olarak gösterir. Kuyruğa kabul, modelin metni okumasının kanıtı değildir. Geç gelen kuyruk iletisinin işi zaten answered ise yeniden çalıştırılmaz; eski karşılık korunur.

24–25 Ekim doğrulaması: kurulu 0.163.0 ikilisinin queue desteği ve mevcut oturuma komutun başarılı dönüşü gerçek çalıştırmayla görüldü. Ubuntu'dan SSH tüneliyle sentetik girdi geldi; tüketici kendiliğinden aldı ve doğru kuyruğa iletti. Bu etkin model ayrıca receive çıktısını okudu ve gerçek karşılığını aynı işe döndürdü; VM bu yanıtı yeniden okudu. Kuyruğun kendiliğinden yeni model turunu başlatması bu ilk kayıtta henüz doğrulanmadı. Bu, Hacker veya Şahit modelinin kabulü değildir.

Altı tüketici testiyle birlikte bütün köprü testleri:

    python -m unittest discover -s . -p "test_*.py" -v

Arayüzde aynı işe yeni ileti eklemek yeni bir revision oluşturur; özgün söz veya eski yanıt değiştirilmez. CLI aynı işi ve önceki iletileri birlikte alır. Bekleyen bir claim varken yeniden `receive` aynı claim'i verir; yeni bir teslim olayı yazmaz. Yanıt gelmeden sonraki ileti alınmaz. Aynı yanıtın yeniden kaydı değişiklik yapmaz; farklı yanıtla üzerine yazma reddedilir.

HTTP gönderiminde aynı request_key aynı içerikle tekrar kullanılırsa aynı ileti döner. Farklı içerikle kullanılması reddedilir. Tarayıcı son gönderimi yanıt gelene kadar yerel saklar; bağlantı kesilirse aynı anahtarla yineler. Bu, **köprü tesliminin yinelenmesini** önler; CLI'ın dış dünyadaki bir eyleminin tam bir kez gerçekleştiğini kanıtlamaz. Yanıttan önce kesilmiş bir CLI işi mevcut claim'den, gerçekleşmiş işlemleri kontrol ederek sürdürür.

Bu WinPE ortamında SQLite kilitleri tek başına eşzamanlı alımı ayırmadığı için veritabanı bağlantısının ömrü boyunca Windows adlandırılmış mutex kullanılır; POSIX karşılığı dosya kilididir. Bu sürüm aynı makinede ve Windows'ta aynı oturumda çalışan süreçler içindir. Windows ile Ubuntu VM arasında paylaşılan SQLite dosyası üzerinden bağlantı doğrulanmadı.

Kaynakların baytları `reply --source` sırasında okunup boyut/SHA-256 ile kaydedilir. Bu denetim metnin semantik yorumunun doğruluğu değildir. Sonucun arayüze dönmesi kullanıcı kabulünün otomatik verilmesi sayılmaz.

Arayüzdeki **Alıntı veya belge kaynağı ekle** alanı; kaynak konumu, söyleyen, statü, dal, dönüşüm, düzeltme, gerçekleşme dayanağı ve belirsizliği özgün metnin yanında taşır. Aynı bilgiler HTTP girdisindeki `source_context` nesnesiyle de verilebilir. Bunlar girişi hazırlayanın verdiği bilgilerdir; `source_context_verified` her zaman false döner. Alıntıdaki talimatlar yeni kullanıcı emri sayılmaz. CLI bu bilgileri gerçek `receive` çıktısında görür.

Kaynak bağlamı kaydedildikten sonra aynı istek anahtarıyla değiştirilmez; düzeltme yeni ileti olarak aynı işe eklenir. İlk sürümün veritabanı açıldığında eski iletilere boş kaynak bağlamı eklenir; özgün metinler ve yanıtlar korunur. Yükseltme öncesi veritabanının özel bir yedeğini almak uygundur.

## Mevcut katkılarla ilişki

PR #4'ün 99dc8a3 sürümündeki çevrimdışı kuyruk süreç başlatmaz; kullanıcı onayı, elle çalışma ve kabul kayıtlarını tutar. PR #5'in 2a68b37 sürümü Hacker devridir. Bu köprü, gerçek oturum teslimi ve geri dönüşü için ayrı bir yürütme yoludur; bu PR'ları veya eski kuyruğu değiştirmez, birleşmiş saymaz. Başlangıçtaki sabit Şaman devir paketine de yazmaz.

Otomatik Codex yürütücüsü için incelenen [resmî OpenAI belgesi](https://learn.chatgpt.com/docs/non-interactive-mode), JSONL olaylarını ve belirli oturuma resume seçeneğini açıklar. Bu ilk sürüm yeni bir Codex çalıştırması yerine mevcut açık CLI'ın doğrudan alım/yanıtını kullanır. Devam eden ana Şaman oturumuna ikinci bir süreçle eşzamanlı resume gönderilmez.

## Doğrulama

```powershell
python -m unittest discover -s . -p test_bridge.py -v
```

On test; özgün metin, yanlış oturuma teslimin reddi, eşzamanlı alım, yeniden başlatmadan devam, değişmez yanıt, kaynak karması, aynı işte düzeltme, HTTP köken denetimi, kaynak/dal bilgisinin korunması ve eski veritabanının kayıpsız geçişini kapsar. Test karşılıkları gerçek model yanıtı diye sunulmaz; gerçek CLI çevrimi ayrıca kendi işlem kaydıyla gösterilir.

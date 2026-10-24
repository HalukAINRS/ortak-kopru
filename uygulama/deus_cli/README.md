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

Arayüzde aynı işe yeni ileti eklemek yeni bir revision oluşturur; özgün söz veya eski yanıt değiştirilmez. CLI aynı işi ve önceki iletileri birlikte alır. Bekleyen bir claim varken yeniden `receive` aynı claim'i verir; yeni bir teslim olayı yazmaz. Yanıt gelmeden sonraki ileti alınmaz. Aynı yanıtın yeniden kaydı değişiklik yapmaz; farklı yanıtla üzerine yazma reddedilir.

HTTP gönderiminde aynı request_key aynı içerikle tekrar kullanılırsa aynı ileti döner. Farklı içerikle kullanılması reddedilir. Tarayıcı son gönderimi yanıt gelene kadar yerel saklar; bağlantı kesilirse aynı anahtarla yineler. Bu, **köprü tesliminin yinelenmesini** önler; CLI'ın dış dünyadaki bir eyleminin tam bir kez gerçekleştiğini kanıtlamaz. Yanıttan önce kesilmiş bir CLI işi mevcut claim'den, gerçekleşmiş işlemleri kontrol ederek sürdürür.

Bu WinPE ortamında SQLite kilitleri tek başına eşzamanlı alımı ayırmadığı için veritabanı bağlantısının ömrü boyunca Windows adlandırılmış mutex kullanılır; POSIX karşılığı dosya kilididir. Bu sürüm aynı makinede ve Windows'ta aynı oturumda çalışan süreçler içindir. Windows ile Ubuntu VM arasında paylaşılan SQLite dosyası üzerinden bağlantı doğrulanmadı.

Kaynakların baytları `reply --source` sırasında okunup boyut/SHA-256 ile kaydedilir. Bu denetim metnin semantik yorumunun doğruluğu değildir. Sonucun arayüze dönmesi kullanıcı kabulünün otomatik verilmesi sayılmaz.

## Mevcut katkılarla ilişki

PR #4'ün 99dc8a3 sürümündeki çevrimdışı kuyruk süreç başlatmaz; kullanıcı onayı, elle çalışma ve kabul kayıtlarını tutar. PR #5'in 2a68b37 sürümü Hacker devridir. Bu köprü, gerçek oturum teslimi ve geri dönüşü için ayrı bir yürütme yoludur; bu PR'ları veya eski kuyruğu değiştirmez, birleşmiş saymaz. Başlangıçtaki sabit Şaman devir paketine de yazmaz.

Otomatik Codex yürütücüsü için incelenen [resmî OpenAI belgesi](https://learn.chatgpt.com/docs/non-interactive-mode), JSONL olaylarını ve belirli oturuma resume seçeneğini açıklar. Bu ilk sürüm yeni bir Codex çalıştırması yerine mevcut açık CLI'ın doğrudan alım/yanıtını kullanır. Devam eden ana Şaman oturumuna ikinci bir süreçle eşzamanlı resume gönderilmez.

## Doğrulama

```powershell
python -m unittest discover -s . -p test_bridge.py -v
```

Testler; özgün metin, yanlış oturuma teslimin reddi, eşzamanlı alım, yeniden başlatmadan devam, değişmez yanıt, kaynak karması, aynı işte düzeltme ve HTTP köken denetimini kapsar. Test karşılıkları gerçek model yanıtı diye sunulmaz; gerçek CLI çevrimi ayrıca kendi işlem kaydıyla gösterilir.

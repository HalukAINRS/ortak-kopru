# Mimari karar: deus_ex_machina'nın NT Kernel bileşeni

**Dayanak:** Haluk'un 26 Ekim 2026 tarihli güncel talimatı:

> deus_ex_machina yerel bilgisayarda en derin NT Kernel katmanında çalışan arayüz olacak, CLI'ların daha derininde.

Bu güncel gereksinim, tarihsel orkestratör tasarımlarından ayrı tutulur.
Uygulamada NT Kernel tarafında gerçek bir aygıt arayüzü, kullanıcı modunda da
onunla konuşan bağlayıcı ve görünür kullanıcı yüzeyi bulunur.

## Bileşen sınırları

| Bileşen | Çalışma katmanı | Bu sürümde gerçekleşen iş |
| --- | --- | --- |
| `deus_kernel.sys` | NT Kernel / KMDF | Sürüm, yetenek ve sorguya bağlı yanıt veren aygıt kapısının kaynak kodu |
| `windows_nt.py` | Windows kullanıcı modu | Gerçek aygıtı açma, IOCTL gönderme ve protokolü doğrulama |
| İş çekirdeği | Kullanıcı modu | Kalıcı iş/olay/kaynak kayıtları ve devamlılık |
| CLI bağlantıları | Kullanıcı modu | Belirli oturumlarla iletişim; kernel sorgusuyla aynı olay sayılmaz |
| `deus_ex_machina` ekranı | Kullanıcı modu | İstek, kaynak, iş durumu ve sonuçların gösterimi |

Microsoft'un Windows yürütüm ayrımında uygulamalar kullanıcı modunda,
çekirdek bileşenleri ve KMDF sürücüleri çekirdek modunda çalışır. Bu nedenle
ekran çizimi, kaynak metinleri ve model çağrılarını sürücüye taşımak yerine,
NT katmanındaki aygıt arayüzü ayrı bir bileşen olarak uygulanır.
Kaynak: [User mode and kernel mode](https://learn.microsoft.com/en-us/windows-hardware/drivers/gettingstarted/user-mode-and-kernel-mode).

## İlk protokol ve dürüst durum bildirimi

`query_status()` yalnız gerçek Windows aygıt sorgusu başarıyla dönüp protokol
doğrulandığında `ready=true` üretir. Bu durumun kapsamı `device-protocol`dür.
İşlerin yürütme katmanı ayrıca `user-mode`, süreç gözetimi ise
`supervision_available=false` olarak bildirilir. Sürücü bulunmuyorsa veya
ortam Windows değilse, kernel gerektiren yol başarısız olur.

Kaynak kodunun, başarılı derlemenin, imzalanmış paketin, kurulu sürücünün ve
gerçek aygıt cevabının durumları ayrı kalır. Python testlerinde kullanılan
sahte sürücü karşılığı canlı NT kanıtı olarak yayımlanmaz.

## Sonraki NT kapsamı

Bu başlangıçta iş yetkisini çekirdekte uygulama, CLI yaşam döngüsünü çekirdekten
yönetme veya açılışta tüm katmanlardan önce yüklenme gerçekleştirilmedi.
Bunlar için gereken somut kernel işlevleri, olay biçimleri, yaşam döngüsü ve
geri alma davranışı ayrıca tanımlanıp hedef Windows ortamında sınanmalıdır.
Kullanıcı modunda verilmiş bir işin `pause/cancel` durumu, işletim sistemi
sürecinin kernel tarafından durdurulduğu şeklinde sunulamaz.

İlk sürücünün küçük sorgu yüzeyi, gerçek NT bağlantısını sınamayı ve daha
sonraki yetenekleri ayrı protokol sürümleriyle eklemeyi sağlar. İş kaydı,
model çıktısı ve kimlik bilgisi bu aygıt protokolünün girdisi değildir.

## Derleme ve yerel doğrulama

Derleme projesi, sabit SDK/WDK bağımlılıkları, IOCTL biçimi ve gerçekleşme
ölçütleri [windows/nt/README.md](../windows/nt/README.md) içindedir. Hedefteki
normal sürücü imzalama/yükleme gereksinimleri geçerlidir. Bu değişiklik herhangi
bir sürücüyü kurmaz veya yüklemez; kurulum yapılmış gibi rapor üretmez.

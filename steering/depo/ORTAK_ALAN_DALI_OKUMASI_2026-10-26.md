# Ortak alan araçları dalının okuması — 26 Ekim 2026

Bu okuma, `claude/ortak-alan-araclari-2026-10-25` dalının [`f52ef87b381f3b8475821208c88b0df4f9814be7`](https://github.com/HalukAINRS/ortak-kopru/tree/f52ef87b381f3b8475821208c88b0df4f9814be7/ortak-alan) sürümündeki dört dosyanın tam metnini kapsar. Betikler çalıştırılmadı; kullanıcının Windows/VM dosyalarında değişiklik yapılmadı. Bu dalın bulunması, araçların ana dala birleştirildiğini veya hedef ortamda kullanıldığını göstermez.

## İçerik ve kaynak

| Dosya | Okunan görev ve kesinlik sınırı |
| --- | --- |
| [BENIOKU.txt](https://github.com/HalukAINRS/ortak-kopru/blob/f52ef87b381f3b8475821208c88b0df4f9814be7/ortak-alan/BENIOKU.txt) | İki öneriyi, bunlar için aktarılan kullanıcı onayını, kurulum tarifini ve on bir dosyalık düzeni açıklar. Onayın burada bulunması tarihsel bir kaynak kaydıdır; bu turda kurulumu çalıştırma talebi olarak kullanılmadı. |
| [dosya_adlari.txt](https://github.com/HalukAINRS/ortak-kopru/blob/f52ef87b381f3b8475821208c88b0df4f9814be7/ortak-alan/dosya_adlari.txt) | On bir kanonik ad; Unicode NFC ve Türkçe/ASCII ikiz ad uyarısı. Ad listesi, bu dosyaların hedef bilgisayarda bulunduğunu tek başına kanıtlamaz. |
| [ortak_yaz.py](https://github.com/HalukAINRS/ortak-kopru/blob/f52ef87b381f3b8475821208c88b0df4f9814be7/ortak-alan/ortak_yaz.py) | Okunan sürümün SHA-256 değeriyle yazım öncesi karşılaştırma, dosya kilidi, eski sürüm yedeği, atomik değiştirme ve değişiklik günlüğü. Listede olmayan ad için uyarı verir; ASCII ikiz ad saptandığında durur. |
| [ruya_denetim.py](https://github.com/HalukAINRS/ortak-kopru/blob/f52ef87b381f3b8475821208c88b0df4f9814be7/ortak-alan/ruya_denetim.py) | R-kimliklerini, bozuk göndermeleri, cümle/sekiz kelimelik tekrarları ve kişisel içerik adaylarını inceler; sonuç raporu yazar. Kaynak anlatıları kendiliğinden silmez veya taşımaz. |

## Steering incelemesiyle ilişkisi

`ortak_yaz.py` içindeki `komut_yaz`, kullanıcının düzenlenecek metni okuduğu andaki özet ile mevcut dosya özetini karşılaştırır. Fark varsa yeni gövdeyi asıl dosyanın üzerine yazmaz; bekleyen kopyayı saklar ve yeniden birleştirme gerektiğini bildirir. Bu, konuşmanın ve kayıtların başka bir katılımcının değişikliği görülmeden üzerine yazılması sorununa yönelik somut bir tasarımdır. `komut_ekle` ise aynı temel-özet sözleşmesini istemez; mevcut metnin sonuna ekler. İki kipin anlamı aynı değildir.

Kanonik adların tamamının zorunlu kabul listesi olarak uygulandığı söylenmemelidir: `ad_uyarilari`, liste dışı ad için yalnız uyarı basar. ASCII ikizi için gerçek ret vardır. Belgede açıklanan niyet, koddaki koşul ve hedef ortamda gözlenmiş sonuç ayrı kayıtlardır.

`ruya_denetim.py` kişisel içeriğin başka dosyalara dağılmasını görünür kılmayı amaçlar. Gönderme denetimi bir kayıt numarası ve kaynak ilişkisini korur; metin tekrarı denetimi ise yalnız tanımlanmış eşleşmeleri yakalar. Kendi sonuç metni de sıfır bulgunun aktarımın eksiksizliğini kanıtlamadığını açıkça söyler. Bu nedenle bir raporun üretilmesi, bütün özgün anlatının eksiksiz taşındığına veya kaynaklardan çıkarılabileceğine otomatik onay sayılmaz.

## Uygulanmışlık sınırı

BENIOKU, araçların sahte klasörde sınandığını ve Windows FAT32 üzerinde henüz çalışmadığını bildirir. Bu turda testler yeniden çalıştırılmadı. FAT32 davranışı da burada bağımsız sistem deneyi olarak doğrulanmadı; dosya adı çakışmasını önlemeye yönelik kod ve kaynakta aktarılan gerekçe okundu.

Bu dört dosyanın ilgili bulgusu; **güncel sürümü okumak, dönüşümü kaydetmek, kaynak kimliğini korumak ve otomatik denetimin karar sınırını açık yazmaktır**. Özel kişisel gövdeler bu rapora alınmadı. Ayrı dalın kaynakları bağlantılarıyla korunur; eski kurulum emirleri bu yeni okuma işine dönüştürülmez.

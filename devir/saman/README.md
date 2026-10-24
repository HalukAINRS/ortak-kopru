# Şaman'a devir — 24 Ekim 2026

**Amaç:** Bu konuşmadaki steering araştırmasını, son depo okumasını ve Haluk'un deus_ex_machina tarifini Codex CLI'da kullanılabilir yerel dosyalara taşımak; kalan çalışmaya Şaman olarak orada devam etmek.

**Yayın durumu:** Bu ek paket hazırlandı. Ana köprünün k-0111 kaydı, zaten çalışan Şaman CLI oturumunun 519 görünür mesajı aldığı ve 80 defter kaydını eşlediği bildirimini taşıyor. Bu web oturumu o CLI'yı başlatmadı; bu yeni ek paketin hedef oturumda okunma/kabul kaydı henüz gelmedi. `Yeni paket kabulü bekleniyor` ifadesi, kullanıcı izninin eksik olduğu anlamına gelmez; talimat zaten verilmiştir.

## Başlangıç

**Zaten açık Şaman oturumu varsa önce o oturumda devam edilir.** Güncel ana dalda `python saman_devral.py --hazirla` ile bu ek paket ayrı çalışma ağacına alınır ve dosya karmaları doğrulanır. Hazırlığın verdiği gerçek çalışma ağacı yolundaki `AGENTS.md` ve **`devir/saman/CLI_BASLANGIC.md`** mevcut Şaman oturumuna okutulur. Hangi gerçek oturumun devam ettiği ve yeni dosyaları okuduğu ayrıca kaydedilir; eski sohbet oturumu otomatik seçilmez.

**Yeni etkileşimli oturum gerekiyorsa** `python saman_devral.py`, aynı hazırlıktan sonra `ayarlar-yerel.json` içindeki Şaman ikilisini kendi ortamıyla açar. Mevcut ana çalışma ağacında dal değiştirmez. Özgün arşivi tanıtmak için `--kaynak-zip DOSYA` kullanılır. Başlatıcı bir sohbetin süreç belleğini başka oturuma taşımış sayılmaz. Ayrıntı [başlatma rehberinde](BASLATMA.md).

## Paketin haritası

| Dosya/dizin | İşlev |
| --- | --- |
| [CLI_BASLANGIC.md](CLI_BASLANGIC.md) | Mevcut veya yeni CLI oturumunun bu ek paketi alması ve devam görevi |
| [DEVIR.md](DEVIR.md) | Yapılanlar, kapsam, kaynaklara dönüş ve mevcut sınırlar |
| [GORUNUR_KONUSMA.md](GORUNUR_KONUSMA.md) | Bu aktarımda doğrudan görülebilen kullanıcı sözleri ve son yanıt |
| [KULLANICI_ILETILERI.json](KULLANICI_ILETILERI.json) | Aynı kullanıcı iletilerinin makinece okunabilir özgün metni |
| [ACIK_ISLER.md](ACIK_ISLER.md) | Öncelikli kalan işler, dayanak ve bitiş ölçütleri |
| [KAYNAKLAR.json](KAYNAKLAR.json) | Sabit commit'ler, ham arşiv karması ve erişim statüleri |
| [YONLENDIRME_NOTU.md](YONLENDIRME_NOTU.md) | Köprüde API/CLI alıcı eşleşmesinin sınırı |
| [kaynaklar/steering/README.md](kaynaklar/steering/README.md) | Önceki yayının 85 dosyasının tam kopyası |
| [../../deus_ex_machina/SAMAN.md](../../deus_ex_machina/SAMAN.md) | Güncel yüzey/CLI ilişkisi ve Şaman'ın devam işi |
| [MANIFESTO.json](MANIFESTO.json) | Sabit paket dosyalarının boyut ve SHA-256 değerleri |

`ilerleme/` altında oluşacak yeni sonuçlar sabit paket manifestosuna dahil değildir. Hazırlık, çalıştırma, dosyanın okunması, anlamın geri anlatılması ve uygulanmış sonuç ayrı olaylardır.

## Tamlık sınırı

Bu pakette erişilebilir iş bağlamı, raporlar, kaynak/kanıt kataloğu, son yayın sonuçları ve açık işler bulunur. Önceki 100,6 MB kaynak ZIP'i özel yerel kaynak olarak kullanılır; herkese açık Git'e eklenmez. [Güncel Şaman kaynak devri](../../deus_ex_machina/KAYNAK_DEVRI_20261024.md), 519 mesajı (296 ana yol, 223 yan dal), tamamlanmış 80 defter eşlemesini, 15 girdi eki/22 çıktı başvurusunu ve altı yerel asıl dosyayı bildirir. 029–038 yalnız yan dallardadır; etkin yolun son kararı sayılmaz. Bu kaynak işi yeniden açık iş yapılmaz. Tam hesap dışa aktarımı veya bütün eklerin baytları alınmış sayılmaz; v11, oturum köprüsü ve kalan ekler mevcut yerel kaynak kayıtlarından tamamlanır. Bu ek paketin alımı, önceki Şaman devrinden ayrı izlenir.

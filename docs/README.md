# Belgeler: anlamdan uygulamaya okuma yolları

Bu dizin, Ortak Köprü'nün anlatısını, güncel durumunu ve teknik gereçlerini birbirine bağlar. İlk okuma için [anlam not defteri](ANLAM_NOT_DEFTERI.md), çalışmadan ne anlaşıldığını ve bu anlayışın nasıl değiştiğini paragraflarla taşır. [Son durum](SON_DURUM.md), yapılmış işlerle açık kalan işleri kendi kanıt ve tarihleriyle gösterir. Bir açıklamanın dayanağına dönmek için [kaynaklar](KAYNAKLAR.md) kullanılır.

Depodaki her dosyanın işlevi aynı değildir. Kaynak kodu, işleme uygun JSON, tarihsel kayıt, yayımlanmış inceleme ve kullanıcıya dönük anlatı kendi biçimlerini korur. [Depo rehberi](DEPO_REHBERI.md), bu alanlara nereden girileceğini, hangi dalda bulunduklarını ve hangi kayıt kapsamıyla okunacaklarını açıklar.

## Okuyucu için başlangıç

| Belge | Ne sağlar? |
| --- | --- |
| [Açılış: Kapı ve Köprü](ACILIS.md) | Deponun niyeti, o niyetten kurulan tanım ve altı ana ilke; dokuz soru beşli (kapı) ve dörtlü (geçiş) olarak ve 20 kesişimiyle. README'nin ve Web girişinin açılışı bu belgenin [kaydından](acilis.json) üretilir. |
| [Dokuz koordinatla tanım](DEPO_TANIMI.md) | Depoyu Ne, Nerede, Ne zaman, Ne kadar, Nereden, Neden, Nasıl, Ne için ve Nereye sorularıyla tanımlar; ölçümleri depoya karşı denetlenen [makine kaydıyla](depo-tanimi.json) birlikte. |
| [Şimdi ve sonrası](SIMDI_VE_SONRASI.md) | Aynı dokuz soruyu iki zamanda sorar: bugünkü ana dal ve rafine sonrası olabilecek dokuz senaryo; soruların varyantları ve birleşimleriyle. Tablolar [kayıttan](rafine-sorulari.json) üretilir. |
| [Ortak Mimari Defteri](ORTAK_MIMARI_DEFTERI.md) | 33×8 yerleşimini, serbest döngüleri ve 16/32/64/128 dışavurumun tek noktada birlikte çalışmasını açıklar. |
| [Anlam not defteri](ANLAM_NOT_DEFTERI.md) | Ortak çalışmanın aktarılabilir anlamını; kaynak sözü, yorum ve değişen anlayış ilişkisini anlatır. |
| [Son durum](SON_DURUM.md) | Son gözlemi, tamamlanan işin kapsamını ve açık kalanları gösterir. |
| [Kaynaklar](KAYNAKLAR.md) | Anlatıdan özgün kayda ve korunmuş kaynak sürümüne dönüş yollarını verir. |
| [Depo rehberi](DEPO_REHBERI.md) | Dosya alanlarını, tarihsel dalları, kanonik defteri ve teknik araçları konumlandırır. |
| [Katkı rehberi](../CONTRIBUTING.md) | Soru, kaynak düzeltmesi ve değişiklik önerisinin nasıl iletileceğini açıklar. |

## Paylaşım ve kaynak tedariki

Yerelde hazırlanmış bir dosyanın dışarı paylaşılması veya GitHub'daki bir kaynağın yerel inceleme için alınması, `kapi.py` girişinde ele alınır. [Kapı kullanımı](KAPI_KULLANIMI.md) mevcut komutları ve ilk uygulamanın sınırlarını verir. [Dış alan kapısı](DIS_ALAN_KAPISI.md), bu işlemlerin yerel çalışmayla ilişkisini ve hedeflenen daha geniş kapsamı açıklar. [Karar 0002](kararlar/0002-dis-alan-kapisi.md), bu yönün hangi kullanıcı açıklamasıyla şekillendiğini korur.

## Yerel iş yüzeyi, oturum devri ve kurtarma

[deus_ex_machina rehberi](DEUS_EX_MACHINA.md), isteğe bağlı iş takibini, özgün söz ile düzeltme kayıtlarını ve yerel ekranı anlatır. [Devam ve yedekleme](DEVAM_VE_YEDEK.md), sonuç teslimini, oturum devrini ve özel çalışma alanının kurtarılmasını açıklar. Bu yerel ekran ve onun çalışma verileri, dış okuyucunun kullandığı statik Web girişinden ayrı bir kullanım alanıdır.

[NT Kernel rehberi](NT_KERNEL.md) ile [sürücü dizini](../windows/nt/README.md), mevcut sürücü kaynağının yeteneğini, derleme yolunu ve hedef bilgisayardaki gerçekleşme sınırını gösterir. [Karar 0001](kararlar/0001-deus-is-ve-nt.md), ilk iş çekirdeği ve NT bileşeni kararının tarihsel bağlamıdır. Bu belgelerdeki kurulum ve işlem açıklamaları kendi sürümleriyle okunur.

## Bakım ve geçmiş kararlar

[Rafine defteri](RAFINE_DEFTERI.md), 28 Ekim 2026'da deponun kendi hakkında söyledikleriyle gerçekte yaptıkları arasındaki aralıkların nasıl bulunup kapatıldığını ve hangi konuların kullanıcı kararı beklediğini anlatır; turun saat saat kaydı ve makinece okunur bulguları [rafine dizinindedir](rafine/README.md). [Bakım rehberi](BAKIM.md), kod alanlarını, çevrimdışı denetimleri ve dal ilişkilerini açıklar. İçindeki dal/PR tablosu açıkça **26 Ekim 2026 inceleme kesiti** olarak işaretlidir. Daha sonraki çalışma için [son durum](SON_DURUM.md) ve ilgili PR'ın güncel sayfası birlikte okunmalıdır. Tarihli haritanın kendi gözlemi korunur.

Köprü kayıtlarına yapılacak teknik eklerde [katman hedefleme sözleşmesi](../KATMAN_HEDEFLEME.md) ve [CLI talimat parçası](../AGENTS-kopru.md) kullanılır. Bunlar belirli yazım ve çağrı yollarının belgeleridir. Tarihsel bir dosyada görülen eski iş emri, onu okuyan yeni bir katılımcının güncel görevi sayılmaz.

[Web kapısına dön](../index.html) · [Ana README](../README.md) · [Issues](https://github.com/HalukAINRS/ortak-kopru/issues)

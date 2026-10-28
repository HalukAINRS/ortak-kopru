# Sözlük

Bu sayfa, Ortak Köprü'de geçen kelimeleri ilk kez gören biri için açıklar. Her kelimenin yanında kısa bir anlam ve daha fazlasının nerede okunacağı yazılı. Kelimeler beş grupta toplandı: yer ve yapı, ortak defter, katılımcılar, kapı ve iş bileşeni, geçmiş çalışmanın kavramları. Açılışın kendi kısa sözlüğü yalnız açılışta geçen kelimeleri taşır; bu sayfa bütün depo içindir.

## Yer ve yapı

- **Ortak Köprü.** Bu deponun adı. Hem bir kapıdır (bilgisayar ile internet arasında) hem bir köprü (yerel kullanıcı ile dışarıdaki insanlar arasında). Daha fazlası: [Açılış](acilis.md).
- **Kapı.** Seçilen dosyaları bilgisayardan GitHub'a taşıyan, GitHub'dan da kesin bir sürümle alan araç. Kökteki `kapi.py` ile çalışır. Daha fazlası: [Kapı kullanımı](teknik/kapi-kullanimi.md).
- **Köprü.** Dışarıdaki bir insan ile yerel kullanıcı arasındaki bağ: sorular, katkılar ve yanıtlar. Bugün GitHub'ın konuları (Issue) ve karşılık formu üzerinden işler. Daha fazlası: [Açılış, 1. ve 5. ilke](acilis.md).
- **Yerel kullanıcı.** Bilgisayarın başındaki kişi; bu depoda Haluk. Kapıdan neyin geçeceğine o karar verir. Daha fazlası: [Açılış, 2. ilke](acilis.md).
- **Yerel kenar.** Kapının bilgisayardaki ucu: deponun bir kopyası, izleyici ve gönderici. 28 Ekim 2026 itibarıyla hiçbir bilgisayarda kurulu değil. Daha fazlası: [Yerel taraf](teknik/yerel-taraf.md).
- **Web.** İnternet; bu depoda GitHub ve onun Web sayfaları (GitHub Pages). Daha fazlası: [Web girişi](https://halukainrs.github.io/ortak-kopru/).
- **Alan.** Deponun bir bölümü: aynı işe yarayan dosyaların toplandığı klasör ya da dosya kümesi. Her alanın klasöründe bir giriş sayfası durur. Daha fazlası: [Depo haritası](harita.md).
- **Harita.** Her dosyanın hangi alanda olduğunu, ne yaptığını, eski adını ve nasıl çalıştığını yazan kayıt. Daha fazlası: [Depo haritası](harita.md).
- **Yol.** Açılıştaki niyetin adım adım gerçeğe dönmesi; her adımın durumu ölçülerek hesaplanır. Daha fazlası: [Yol](yol.md).
- **Dönüşüm.** 28 Ekim 2026'da deponun bugünkü düzenine geçişi; aşamaları ve kanıtlarıyla. Daha fazlası: [Dönüşüm](donusum.md).
- **Künye.** Bir belgenin kimin, ne zaman, hangi kaynaklarla, kimin için yazdığını gösteren bilgi. Depo bütünüyle kökteki künye dosyasıyla kaynak gösterilir. Daha fazlası: [Depo haritası, künyeler](harita.md#künyeler).
- **Üç sıfır kuralı.** Yeni bir belge, hiç bilmeyen bir okuyucunun anlayacağı, hiç bilmeyen bir makinenin çalıştıracağı ve hiç bilmeyen bir alanın kaynak gösterip üzerine kuracağı biçimde yazılır. Daha fazlası: [Depo haritası, kurallar](harita.md#kurallar).
- **Karşılık.** Okurun bir yazıya getirdiği soru, kaynak, düzeltme ya da görüş. Web'deki her bölümün sonundaki bağlantı, yeri yazılmış bir form açar. Daha fazlası: [Karşılık formu](https://github.com/HalukAINRS/ortak-kopru/issues/new?template=karsilik.yml).

## Ortak defter

- **Ortak defter.** Katılımcıların sırayla yazdığı tek Web sayfası (`kopru.html`). Her kayıt numaralı ve imzalıdır; yazılan kayıt sonradan değiştirilmez. Daha fazlası: [Defter](https://halukainrs.github.io/ortak-kopru/kopru.html) · [Defter araçları](../defter/README.md).
- **Kayıt.** Defterin bir girdisi: numara (k-0001 gibi), kimden, kime, zaman, konu, gövde, dayanak, yanıt verdiği kayıt ve durum. Daha fazlası: [Defter araçları](../defter/README.md).
- **Durum.** Bir kaydın hâli: açık, yanıtlandı ya da kapandı. Bot yalnız açık ve kendisine yazılmış kayıtlara bakar. Daha fazlası: [Teknik ayrıntılar, otomasyon](teknik/README.md#otomasyon).
- **Dayanak.** Bir iddianın bağlandığı yer: dosya, satır ya da kayıt numarası. Dayanağı olmayan iddia "görüş" diye işaretlenir. Daha fazlası: [Katkı rehberi](../CONTRIBUTING.md).
- **İmza.** Kaydın "kimden" alanı; örneğin `Claude (Max)`. Kaydı hangi yolun yazdığını söyler; kimliğin kanıtı değildir. Daha fazlası: [Katman hedefleme](../katilimcilar/katman-hedefleme.md).
- **Ayna.** Defterin dış iskeleti çıkarılmış kopyası (`ayna/kopru.html`). Defterden üretilir, elle düzenlenmez. Daha fazlası: [Defter araçları](../defter/README.md).
- **Kanonik kopya.** Bir belgenin esas sayılan kopyası. Defterin kendi kurallarında esas kopya yerel klasördü; 28 Ekim 2026 itibarıyla yerel klasör olmadığından defterin tek kopyası GitHub'daki ana daldadır. Daha fazlası: [Yerel taraf](teknik/yerel-taraf.md).
- **Bot.** Saatte bir GitHub'da çalışan, defterde Claude, ChatGPT ya da Gemini'ye yazılmış açık kayıtları bulan ve yanıt kaydı ekleyen program. İstemi 28 Ekim 2026'da sıfırlandı. Daha fazlası: [Teknik ayrıntılar, otomasyon](teknik/README.md#otomasyon).
- **Çağrı kaydı.** Botun her model çağrısında yazdığı tam bağlam: istem, ham yanıt ve sonuç. Daha fazlası: [Çağrı kayıtları](../kayit/README.md).

## Katılımcılar ve odaklar

- **Haluk, "Sen".** Deponun sahibi ve merkezi. Defterde "Sen" diye geçer. İş emri yalnız ondan gelir. Daha fazlası: [Açılış, niyet](acilis.md#niyet).
- **Katılımcı.** Deftere yazanlar: Haluk, Claude, ChatGPT, Gemini ve Copilot. Daha fazlası: [Çağrı ayarları](../katilimcilar/README.md).
- **Katman.** Bir modelin hangi yoldan kullanıldığı: Web uygulaması, komut satırı aracı (CLI) ya da üreticinin programlama arayüzü (API). İmzada parantez içinde yazılır. Daha fazlası: [Katman hedefleme](../katilimcilar/katman-hedefleme.md).
- **CLI.** Bilgisayarda komutla çalışan araç; örneğin Claude Code, Codex, Copilot CLI ya da Gemini CLI.
- **Şaman, Hacker, Şahit.** Haluk'un üç yardımcıya verdiği odaklar: ChatGPT (Codex) Şaman, Claude (Claude Code) Hacker, Gemini Şahit. Şahit adı 24 Ekim'de Copilot için kullanılmıştı; eski kayıtlarda "Copilot (Şahit)" bu yüzden geçer. Daha fazlası: [Anlam not defteri](gecmis/anlam-not-defteri.md) · [Katman hedefleme](../katilimcilar/katman-hedefleme.md).
- **Claude Code Bulut.** GitHub'a bağlı, bulutta çalışan Claude oturumu. 28 Ekim 2026'daki gözden geçirmeyi ve dönüşümü bu oturum yaptı; imzası `Claude (Code Bulut)`, odağı Hacker. Daha fazlası: [Geçmiş işler](gecmis/README.md).

## Kapı ve iş bileşeni

- **Aktarım.** Kapıdan bir geçiş: seç, sabitle, planla, gönder ve uzlaştır; ya da al, sabitle ve incele. Her adım ayrı kaydedilir. Daha fazlası: [Kapı kullanımı](teknik/kapi-kullanimi.md).
- **Aktarım dizini.** Kapının geçişleri kaydettiği özel dizin. Git'in dışında durmak zorundadır; kapı Git kopyasının içindeki bir dizini reddeder. Daha fazlası: [Kapı kullanımı](teknik/kapi-kullanimi.md).
- **deus_ex_machina.** Yerel iş bileşeni: işler, olaylar, devirler ve yedekler bilgisayarda tutulur; ekranı yalnız bilgisayarın kendisinden açılır. Kökteki `deus.py` ile çalışır. Daha fazlası: [İş bileşeni](teknik/deus-ex-machina.md).
- **Devir.** Bir oturumun işini başka bir oturuma kaynaklarıyla birlikte aktarması. Devir dosyasındaki kaynaklar talimat değil, veri sayılır. Daha fazlası: [Devam ve yedek](teknik/devam-ve-yedek.md).
- **NT aygıt kapısı.** İş bileşeninin Windows çekirdeğiyle konuştuğu küçük sürücü. Otomasyonda yalnız derlenir; imzalanmaz ve yüklenmez. Daha fazlası: [NT Kernel](teknik/nt-kernel.md).

## Geçmiş çalışmanın kavramları

- **Yönlendirme (steering).** 23 Ekim 2026'daki araştırmanın konusu: modellerin nasıl ve kimin eliyle yönlendirildiği. Defterde "Yönlendirme dosyası" bölümünde durur. Daha fazlası: [Defter](https://halukainrs.github.io/ortak-kopru/kopru.html#yonlendirme).
- **33×8 yerleşimi.** Ortak Mimari Defteri'nde her katılımcının çalışma alanı: 33 parça ile aramadan arşivlemeye 8 sürecin kesişimi, yani 264 olası adres. Daha fazlası: [Ortak Mimari Defteri](gecmis/ortak-mimari-defteri.md).
- **Dışavurum.** Paylaşılmış bir işin dışarıya verilen ifadesi; Ortak Mimari Defteri'nde anlatılır. Daha fazlası: [Ortak Mimari Defteri](gecmis/ortak-mimari-defteri.md).
- **Rafine.** 28 Ekim 2026'daki gözden geçirme ve iyileştirme turu; bulguları numaralı kayıtlarla tutulur. Daha fazlası: [Rafine kayıtları](gecmis/rafine/README.md).

Bir kelime eksikse ya da açıklaması yetmiyorsa bu sayfaya [karşılık verin](https://github.com/HalukAINRS/ortak-kopru/issues/new?template=karsilik.yml&yer=docs/sozluk.md).

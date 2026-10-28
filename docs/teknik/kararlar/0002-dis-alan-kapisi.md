# Karar 0002 — Yerelden harici alanlara paylaşım ve tedarik kapısı

Tarih: 26 Ekim 2026 · Karar sahibi: Haluk · Durum: Haluk'un 26 Ekim 2026 tarihli açıklamasıyla ürün yönü netleşti.
Bu belge yönü ve geliştirme sınırlarını kaydeder. İlk görevden bağımsız dosya
aktarımı ve GitHub bağlayıcısı `kapi.py` üzerinden uygulanmıştır. Diğer
sağlayıcılar ve genel dış çalışma talepleri geliştirme kapsamındadır.
[Çalışan komutlar ve sınırlar](../kapi-kullanimi.md).

## Bağlam

Kullanıcı yerelde yapmakta olduğu işleri mevcut araçları ve düzeniyle
sürdürecek. `ortak-kopru`, bu çalışmalardan seçilenleri GitHub ve diğer
harici alanlara paylaşacağı; dışarıdan gerekli olanları alacağı kapı olacak.
Değişen karar Windows/Linux kullanım sırası değil, köprünün çalışma içindeki
yeridir.

[Karar 0001](0001-deus-is-ve-nt.md) ile eklenen kalıcı görev kaydı ve NT
aygıt temeli korunur. Bunlar bütün yerel işlerin ön koşulu yapılmaz.

## Karar

1. **Yerel iş akışı bağımsızdır.** Editör, CLI, dosya ve mevcut uygulamalar
   kullanılmaya devam edilir. Kapı yalnız seçilen dış etkileşimi ele alır.
2. **Aktarımın ayrı kimliği vardır.** Bir aktarımın yönü, amacı, kaynağı veya
   hedefi, seçilen içeriği, sürümü ve sonucu kaydedilir. Bir görev veya oturum
   başvurusu isteğe bağlıdır; aktarım için `create/assign/receive` zinciri
   gerekmez.
3. **Paylaşılacak içerik seçilerek kurulur.** Yerel yol, yetki dayanağı,
   aktarım denemeleri ve özel geçmiş yerel kayıtta kalır. Dışarıya yalnız
   hedef için seçilmiş baytlar ve uygun yayın bilgileri çıkar.
4. **Tedarik edilen kaynağın kökeni korunur.** Uzak nesne ve sürüm kimliği,
   alınma zamanı ve yerelde hesaplanan içerik karması birlikte kaydedilir.
   İçeriği almak ile yerel işe uygulamak ayrı eylemlerdir.
5. **Hazırlık ve gerçekleşme ayrı durumlardır.** Paket hazırlamak gönderim
   sayılmaz; API isteğinin başlatılması teslim sayılmaz. Dış işlemin nesne,
   sürüm, commit veya PR kimliği makbuza bağlanır. Sonucu bilinmeyen işlem
   yeniden gönderilmeden önce uzak durumla uzlaştırılır.
6. **Mevcut yetki kapsamı sürer.** Kullanıcının belirlediği içerik, hedef ve
   işlem kapsamındaki aktarım her adımda yeniden izin istemeden ilerleyebilir.
   Kapsam dışındaki dosya veya yeni hedef bu yetkiden türetilmez. Gelen
   metinler kendiliğinden yerel komut veya görev yetkisi olmaz.

## Bileşenlerin yeri

| Bileşen | Yeni yöndeki rolü |
| --- | --- |
| Yerel çalışma alanları | İşin üretildiği, kaynakların ve asıl çıktıların bulunduğu alanlar |
| `deus_ex_machina` | Yerel erişim/arayüz bileşeni; mevcut görev takibi gerektiğinde kullanılabilir |
| İlk aktarım katmanı — `exchange.py`, `gateway.py` | Görevden bağımsız seçilmiş dosyalar, tedarik kaydı, sürüm ve aktarım sonucu |
| GitHub bağlayıcısı — `adapters/github.py` | Kesin commit'ten okuma; yeni dal ve isteğe bağlı taslak PR oluşturma |
| Diğer sağlayıcı adaptörleri — geliştirilecek | Diğer dış hedeflerin kendi yetenekleriyle okuma/yazma işlemleri |
| `kopru.html` ve eski göndericiler | Ortak defter ve var olan katılımcı iletişimi |
| `handoff`, `export`, `backup` | Özel görev devri, inceleme ve kurtarma; seçici genel yayın paketi değil |

NT aygıtı yerel bileşen olarak hedefte kalır. Görünür ekran, dosya seçimi,
sağlayıcı API çağrıları ve kimlik bilgisi kullanımı kullanıcı kipindedir.
Mevcut `deus.py` girişindeki `nt-kernel`/`portable` davranışı korunur. Ayrı
`kapi.py` girişi kullanıcı kipinde aktarım yapar, NT aygıtı sorgulamaz ve bir
kernel doğrulaması iddiası üretmez.

## Veri yerleşimi

Git deposu kapının kodunu, veri sözleşmelerini, açıklamalarını, örneklerini
ve açıkça yayımlanmış içerikleri taşır. Yerel işler kendi proje ve araçlarında
kalır; bunlar ayrı Git depoları da olabilir. Aktarım hazırlıkları ve ayrıntılı
makbuzlar Git dışındaki özel aktarım alanında tutulur; kimlik bilgileri ilgili
yerel oturum veya kimlik bilgisi kaynağından kullanılır. Bir dış hizmete
paylaşım, içeriğin ayrıca bu herkese açık depoya da girmesini gerektirmez.

İlk aktarım uygulaması, görev veritabanından ayrı sürümlü `exchange.sqlite3`
ve sabit paketler kullanır. Mevcut görev şeması v1 yedek doğrulaması tablo kümesini birebir
denetler; yeni tablo eklemek ve eski yedeklerin çalışacağını varsaymak doğru
değildir. İlk sürümde aktarım alanı, bütün yazıcılar durduktan sonra tüm dizin
kopyalanarak korunabilir; mevcut görev yedeğinin kapsamına girmez.
İleride birleşik veri alanı seçilirse şema geçişi ve kurtarma desteği birlikte
uygulanır.

## Uygulama aşamaları

1. Uygulandı: görev gerektirmeyen aktarım sözleşmesi, yalnız seçilen
   dosyaların sabit kopyası ve özel aktarım kaydı.
2. Uygulandı: GitHub'dan kesin commit'e bağlı kaynak tedariki; yeni bir
   özel dizine çıkarma. Mevcut projeye uygulama kullanıcı araçlarında kalır.
3. Uygulandı: belirli GitHub deposundaki yeni dala seçilmiş paylaşım;
   değişiklik planı, commit/taslak PR sonucu ve tekrar denetimi. Mevcut dal
   güncellenmez, PR otomatik birleştirilmez.
4. Sonraki: aynı sözleşmeyle diğer dosya hizmetleri; her hizmetin sürüm ve yetki
   yetenekleri ayrıca bildirilir.

`kopru.html` yazımı sağlayıcı çağrısı doğurabilen mevcut akışa bağlıdır.
Pasif bir rapor yayımlama ile bir katılımcıya yeni iş iletme ayrı işlem
türleridir. Bu karar belgesi mevcut zamanlayıcıları veya göndericileri
değiştirmez.

## Kabul ölçütleri

- Yerelde önceden üretilmiş bir dosya, yeni görev açmadan paylaşıma hazırlanır.
- Pakette yalnız seçilen içerik bulunur; sonradan değişen yerel dosya sessizce
  hazırlanmış paketin yerine geçmez.
- Dış işlemin tam hedefi ve sonucu kayıttadır; tekrar veya belirsiz yanıt
  mükerrer yayım olarak ele alınmaz.
- İlk GitHub kapsamındaki kaynağın kesin commit'i ve baytları doğrulanabilir;
  diğer hizmetlerde sunulan sürüm güvencesi ve alınan sabit kopya doğru
  raporlanır. İndirme yerel çalışma dosyasını kendiliğinden değiştirmez.
- Dış hizmet ulaşılamazken kullanıcı yerel çalışmasına devam eder; aktarımın
  bekleyen, başarısız veya sonucu bilinmeyen durumu görünür kalır.
- Mevcut görev, devir, yedek ve tarihsel ortak defter davranışı korunur.

Ayrıntılı akışlar ve mevcut/planlanan yetenek ayrımı:
[Dış alan kapısı](../dis-alan-kapisi.md).

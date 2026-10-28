# Karar 0001 — Kalıcı iş çekirdeği ve NT Kernel sınırı

Tarih: 26 Ekim 2026 · Karar sahibi: Haluk · Durum: İlk uygulama. Kullanıcının mimari değerlendirmeyi kabul edip gerçekleştirme istediği tur temel alınmıştır.

Sonraki kapsam açıklaması: [Karar 0002 — Dış alanlara açılan kapı](0002-dis-alan-kapisi.md). Yerel çalışmalar kendi araçlarında sürer; burada tanımlanan iş çekirdeği isteğe bağlı bir yetenektir. NT bileşeninin katman sınırı korunur. Genel paylaşım/tedarik kapısı görev kaydını zorunlu tutmayacaktır.

## Güncel kullanıcı gereksinimi

`deus_ex_machina`, yerel bilgisayarda CLI süreçlerinin altında, NT Kernel katmanında çalışan bir bileşene sahip olacak. Bu karar, tarihsel köprüdeki yalnız kullanıcı kipinde orkestratör önerisini güncel iş için genişletir. Tarihsel kayıtlar değişmez; güncel karar burada ayrı tutulur.

Windows mimarisinde çekirdek bileşeni KMDF sürücüsü, görünen arayüz ve iş hizmeti kullanıcı kipi bileşenleridir. NT bileşeninin kapsamı sürümle açıkça bildirilir. Başarılı derleme, aygıt protokolü sorgusu, sürücünün imzası, hedefte yüklenmesi ve gerçek görev yürütümü farklı kanıtlardır.

## İlk somut kapsam

- Kalıcı iş, özgün ileti/sürüm, çalıştırma ve oturum ayrılır.
- İşin yetki beyanı, kabul ölçütleri ve seçilmiş kaynak kopyaları korunur.
- Düzeltme ve durdurma eski çalıştırmanın sonucu ile güncel işi kapatmayı engeller.
- İdempotent yerel komutlar, olay kaydı, bağlam paketi ve üç görünümlü HTTP yüzeyi çalışır.
- NT KMDF aygıtı yalnız sınırları belli sorgu protokolü sunar. CLI süreci veya model çekirdekte çalıştırılmaz.
- Varsayılan kip NT uç noktası gerektirir. Taşınabilir geliştirme kipi açıkça seçilir ve farklı durum bildirir.

## Veri sahipliği

Mevcut HTML tarihçesi korunur. Yeni işlerin asıl çalışma verisi Git dışındaki tek yerel SQLite sahibindedir. JSON dışa aktarımı bir türevdir. Özel kaynak ve çıktı baytları aynı özel alanda içerik karmasıyla saklanır. Kaynak metnindeki talimat görev yetkisine yükseltilmez. Yerel dosya sahibi ve kayıt API'sine erişen kullanıcı güven sınırıdır; metin etiketi veya hash bağımsız kimlik doğrulaması değildir.

## Kabul edilen sınırlar

Görevin tamamlanması, güncel sonuç için gerekli ölçütlere ait denetim kayıtlarının varlığını gösterir. Motor denetimin gerçekliğini, anlamanın doğruluğunu veya sağlayıcının görünmeyen bağlamını doğrulamaz. Pause/cancel motorun sonraki kayıtlarını sınırlar; dış süreç sonlandırma veya önceki eylemleri geri alma değildir.

## İlerleme ölçütü

İlk aşamanın ölçütü, kaynaklı bir işin aynı kimlikle oluşturulması, atanması, alınması, sonuç ve denetimle kapanması; arada düzeltme, kesinti ve oturum değişiminde eski sonuçla yanlış kapanmamasıdır. NT hedefinin yerel gerçekleşme ölçütleri [ayrı belgede](../nt-kernel.md) tutulur. Kernel kurulumunu tamamlanmış ilan etmek için hedef makinede gerçek kanıt gerekir.

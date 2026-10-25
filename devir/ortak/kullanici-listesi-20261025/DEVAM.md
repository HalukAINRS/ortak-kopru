# Ortak kullanıcı listesinin üstlenilmesi — 25 Ekim 2026

Haluk’un doğrudan verdiği yetkiyle, ortak listedeki yerel kurulum, erişim ve yayın işleri CLI tarafında yapıldı. Yeni bir genel izin beklenmiyor. Hacker’ın gerçek kaynakları ve Google/Gemini Şahit’in kendi incelemeleri kullanıldı; başka bir model/API yedeği başlatılmadı. Cyber’dan başlayan tekil Steering işi sürüyor.

1. Özgün Steering ZIP’i mevcut ve doğrulanmış durumda. Yeniden yüklenmesi gerekmiyor.
2. Özgün paketin 155.927 baytlık karma manifestosu gerçek Hacker VM alanına metin olarak teslim edildi. Şahit’in önceki kaynak karşılaştırması korunuyor. Hacker’ın Claude/VM kaynaklarının tamamıyla yapacağı karşılaştırmanın sonucu henüz alınmadı; bu bir CLI işi.
3. Tarihsel oturum köprüsü JS dosyasının tam adı 15 yerel arşivde aranıp bulunamadı. Bu arama bütün diskte yokluk kanıtı veya özgün dosyanın geri kazanılması olarak sunulmuyor. Kaynak araması devam ediyor.
4. Haluk’un bu turdaki özgün talimatı gerçek yerel HTML formuna CLI yardımıyla girildi. Aynı açık Şaman çalışması zarfı okuyup sekiz gerçek dosyaya dayanan yanıt verdi; yanıt ve kaynak karmaları tarayıcı ekranında doğrulandı. Eski iki iş değişmedi. Fiziksel kullanıcı tıklaması veya diğer katmanların kendi çevrimleri tamamlanmış sayılmadı.
5. Normal başlangıçta Y: üzerindeki işareti, sekiz belgeyi ve Google oturum durumunu gözleyen kontrol kuruldu. İlk ölçüm geçti; farklı bir Windows başlangıcı henüz gözlenmedi. Açık oturum kapatılmadı veya bilgisayar yeniden başlatılmadı. Kullanıcıdan elle sonuç raporu beklemek yerine gözlem otomatik kayda alınır.
6. Otomatik yerel izleyici ayrı `Google (CLI izleyici)` imzasıyla `gemini-4-argon-high` / `high` yoluna ayarlandı. Mevcut etkileşimli Şahit konuşmasıyla aynı oturum olduğu iddia edilmez. Başka katmanın eski bekleyen işleri devralınmadı. Yapılandırma ve yerel ikili kontrolü geçti; denemek için yeni model üretimi çağrılmadı. API anahtarı yedeği yok.
7. Google Ultra ile çalışan gerçek Şahit’in masaüstünden aynı belirli konuşmayla devamı önceki kaynak makbuzuyla korunuyor. Yeniden giriş veya satın alma gerekmiyor.
8. Hacker’ın hazırlanmış kaynak kaydı özel kopyada korundu. Şaman’ın açıkça kendisine ait kaynaklı aktarımı `k-0133` ile yayımlandı. Claude adına yeni imza atılmadı; eski altı işi otomatik kapatan ilişki kurulmadı. Kullanıcıdan elle köprü eklemesi beklenmiyor.
9. `k-0113` içindeki hedef özel gövde 13 yazılabilir dalın geçmişinde geri çekildi; başlık, kayıt kimliği ve diğer 131 makalenin gövdeleri korundu. Tam eski depo özel yedekte tutuluyor.
10. Gemini dalındaki özel yerel dışa aktarım gövdeleri ve ilgili kimlik alanları da temizlendi. Toplam 42 dosya gövdesi sürümü ve 96 commit değişti. Beş Windows ve iki VM deposu kaydedilmemiş değişiklikleri korunarak eşitlendi. Eski özel geçmişi yeniden gönderme gerçek kuru gönderimde reddedildi. GitHub’ın salt okunur PR refleri ve eski nesne önbelleği hâlâ ayrı bir dış bağımlılık: eski özel dosyanın anonim ham adresi temizlikten sonra da açıldı. Özel destek başvurusu taslağı hazırlandı, gönderilmedi; sunucudan tam silinme tamamlandı denmiyor.
11. Hacker VM üzerinde yalnız bu depoya yazan bir anahtar üretildi; özel anahtar VM’den çıkmadı, hesap belirteci taşınmadı. Gerçek geçici dal oluşturma ve kaldırma geçti. Hem mevcut depo hem ayrı yazma çalışma alanı yeni erişimi kullanıyor.
12. Google/Gemini Şahit’in 19 ayrı Cyber incelemesi, kendi çalıştırdığı 16 başarılı sınır testi ve 13 üye envanteri kaydı ortak deftere bağlandı. Hacker’ın JSON sürümünde 113 öneri kaydı var; ayrı 14 CYB arşiv maddesi bu JSON’da varmış gibi sayılmadı. Kümeler veya 6065 satır topluca kabul edilmedi. Etkisi önlendi diye kapanan koşul sıfır; sağlayıcı kararının nedeni ve gerçek önleme kabulü açık.
13. Kullanıcının sekiz uzun dosya adı korundu. İki eşit Steering girdisi yedeklenip 201.689 baytlık içerik tek kanonik `Steering Arşiv.txt` dosyasında toplandı. Gelen eski ASCII adı bu kanonik ada eşleniyor. VM okuma aynasındaki iki eski kısa ad kopyası ayrıca yedeklendi; yazarlara ait kaynaklar taşınmadı.

## İncelenebilir uygulama

`Sahit_Ultra_Izleyici.py`, uzun istemi Windows komut satırına sığdırmaya çalışmak yerine köprüdeki UTF-8 dosyayı gerçek araçla okumayı ister. Yerel ikili, model ve efor sabittir; başarısızlıkta başka modele geçmez. `--kontrol` üretim yapmadan kurulum bilgisini döndürür. Canlı özel ayarlar bu pakete alınmadı.

`Kalici_Kontrol.py`, ilk ölçümde sabit bir kalıcılık işareti oluşturur; sonraki kayıp işareti sessizce yeniden oluşturmaz. İşletim sistemi başlangıç zamanını ve yerel dosya varlığını kaydeder. Normal not eşitleyici başlangıcındaki çağrı ve gelen dosya adı eşlemesi `ortak_notlar_ekleri.patch` içinde gösterilir. Bu değişiklikler kurulmadan önce Hacker paketindeki dört dosya canlı kopyalarla eşleşiyordu; ekler sonradan yapıldı.

`privacy_push_guard.py`, yalnız özel politikada belirlenmiş geri çekilen geçmişi ve gövdeleri yeniden göndermeyi engeller. Özel nesne listesi, anahtarlar, eski özel adresler ve destek taslağı kamu paketinde bulunmaz. Mevcut gönderim kancaları korunarak zincirlendi.

## Açık kalan sınır

Kaynak araması, Hacker’ın gerçek sonuç kaydı, diğer katmanların kullanıcı yüzeyi çevrimleri, v11 bütünleştirmesi, doğal yeniden başlangıç gözlemi ve Cyber’daki her öğenin kabul kanıtı CLI takibindedir. GitHub sunucu önbelleği/PR ref temizliği bu yerel kodun yapabildiği dal güncellemesinden ayrıdır. Kullanıcının tek ortak takip listesi özel ortak anlatı klasöründe güncellendi; eski karar soruları yeniden sorulmadı.

GitHub’ın geçmiş temizliği ve sunucu sınırına ilişkin resmî açıklaması: [Hassas veriyi depodan kaldırma](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository). Depoya özgü anahtarın yazma izni: [Deploy keys API](https://docs.github.com/en/rest/deploy-keys/deploy-keys). Bu çalışmanın kaynaklı köprü aktarımı: [k-0133](https://github.com/HalukAINRS/ortak-kopru/blob/2c4b865efd9793810b2061a6b10256e95151670e/kopru.html).

Makbuzların kimliksiz özeti ve özel asıllarının karmaları `DOGRULAMA.json` içindedir. Gerçek Şahit incelemesi ve ortak tekil sıra aynı dalın `steering/cli` dizinindedir. Yayımlanmış olmak ana dala birleştirme veya açık koşulların kabulü anlamına gelmez.

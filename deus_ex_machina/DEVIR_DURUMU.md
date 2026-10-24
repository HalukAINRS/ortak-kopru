# Devir durumu

24 Ekim 2026: Şaman, “Yorumları ayrı sayfaya yazma” sohbetinin görünür mesaj ağacını yerel CLI'a aldı: 519 mesaj, 296 ana yol ve 223 yan dal. Önceki 57 Space sayfası ve tarayıcı kesitleri de korunur. Tam kapsam ve düzeltmeler [kaynak devri kaydındadır](KAYNAK_DEVRI_20261024.md).

## Devralınan durum

- Önceki sekiz aşama, seçilmiş iki PDF’den ilişki metni üretme pilotu kapsamında kapanmış olarak kayıtlıdır. Son kontrol sayfası ürün v2, paket v11 ve olay/teyit 12/12 bildirir. Bu geçmiş kayıt, HalukAI’de yeni kurulmuş sistemin kanıtı sayılmaz.
- Kaynak ağacı, sohbet defteri, tasarım, pilot, ortam karşılaştırması ve araştırma kayıtları yerelde erişilebilir kılınmıştır.
- 80 kayıtlık tarihsel defter kendi kapsam açıklamasında eksiktir. Tarayıcıdan elde edilen sonraki veya eksik mesajlar ayrı kaynak olarak korunur; özgün kayıtların yerine yorum konmaz.
- 80 defter kaydının tamamı yeni kaynakla eşleşti. Kayıt 029–038 yalnız yan dallardadır; etkin yolun son kararı sayılmaz. Bir Markdown satır sonu farkı ayrıca kaydedildi.
- Şaman bu oturumda kaynakları okumaktadır. Hacker veya Şahit’in aynı bağlamı okuduğuna ve kabul ettiğine ilişkin onların yerine sonuç üretilmez.
- PR #4 kullanıcı katmanının ayrı uygulama taslağıdır. Diğer katmanın taslağı bu belgeyle değiştirilmez veya birleştirilmiş sayılmaz.

## PR #4 ilk somut kontrolü

69adfbc sürümünde değişen sekiz dosya yalnız devir/sahit/ altındadır. README, SahitDevam adlı bir yerel kapıyı tarif ediyor; aynı sürümün Kopru_Izle.cmd ve kopru_yerel.ps1 dosyalarında bu ad bulunmuyor. Bu sürüm için devir belgeleri mevcut, belgede tarif edilen başlatıcı bağlantısı ise henüz kodda görünmüyor. İş kuyruğu veya arayüz MVP'si de bu sekiz dosya içinde bulunmuyor. Bu kontrol dalın o sürümüne aittir; sonradan eklenen kod ayrıca okunmalıdır.

Güncel kontrol: 99dc8a3 sürümünde SahitDevam başlatıcısı ve deus_ex_machina/task_queue.py vardır. Kuyruk katılımcı süreçlerini başlatmaz. Çalışan ilk gerçek CLI çevrimi bu kontrolle doğrulanmadı. Hacker devri ve konu katkısı ayrıca PR #5'te görünür oldu; iki PR da bu belgeyle birleştirilmiş sayılmaz.

## Açık işler

1. Bütün ek/görüntü içeriklerini tamamlamak. Görünür mesaj ağacı ve eski defterin eşlemesi tamamlandı; ürünün tam hesap dışa aktarımı alındığı iddia edilmiyor.
2. Atıf verilen çalışan çekirdek, paket v11, oturum köprüsü ve bağlam paketlerinin gerçek dosya baytlarını temin edip kaynak kayıtlarıyla doğrulamak. Bir bağlantının bulunması indirme veya yeniden kurulum sayılmaz.
3. Şaman’ın kaynaklı geri anlatımını korumak; gerçek Şahit ve Hacker yanıtlarını ayrı teslim ve okuma kayıtlarıyla almak.
4. Mevcut arayüz taslağını güncel katman tarifine göre incelemek ve ilk gerçek CLI çevrimini kurmak.
5. Pilot çekirdeğinin HalukAI’ye taşınmasını, mevcut çalışma zamanları ve kalıcı kayıt koşullarıyla sınamak.

Önceki kapanmış pilot yeniden başlatılmaz. Yeni ortamda ilk olarak kaynak paketinin gerçekten mevcut olup olmadığı ve arayüz taslağının fiilî içeriği belirlenir. Açık işler, yapılmış veya sınanmış gibi gösterilmez.

Dayanaklar: “HalukAI CLI Bağlam Aktarımı”, “HalukAI Kurulum Ortamı ve deus_ex_machina Karşılaştırması”, “İlk İş Güncel Kontrol Kaydı” sayfaları; ortak-kopru k-0014, k-0016; PR #4; bu oturumun yerel dosya ve tarayıcı okuma kayıtları.


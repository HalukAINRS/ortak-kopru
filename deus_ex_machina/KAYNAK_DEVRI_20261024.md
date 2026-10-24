# Görünür sohbet kaynağının CLI'a devri

24 Ekim 2026: Haluk'un işaret ettiği aktarım sohbeti, kendi açık oturumundan salt okunur alındı. Özel mesaj gövdeleri yerel Y alanında tutulur. Bu belge yalnız kapsam ve devam durumunu yayımlar.

519 benzersiz görünür kullanıcı/asistan mesajı korundu: 126 kullanıcı, 393 asistan; etkin ana yol 296, yan dallar 223. Mesaj kimlikleri, zamanları, görünür önceki düğümler ve ana yol sırası yerel JSON'dadır. Ayrı ana yol ve yan dal Markdown okuma dosyaları üretildi. Bu, ürünün tam hesap dışa aktarımı değildir.

80 kayıtlık önceki defterin tamamı kaynak mesajlarla eşlendi. 71 gövde birebir, 8 kayıt kaynak mesaj kimliğiyle, 1 kayıt Markdown satır sonu farkıyla bağlandı. Kayıt 014'teki fark, satırın sonundaki ters eğik çizgidir; simgeler ve sözcükler aynıdır. Eski defter korundu.

Kayıt 029–038 yalnız yan dallardadır. Bu aralıktaki ifadeler korunur; etkin konuşmanın son kararı olarak aktarılmaz. Ana yoldaki kullanıcı düzeltmeleriyle, alternatif dallardaki sözlerin ayrılması arayüzün kaynak ilişkisini de etkiler: aynı zaman çizelgesine yazılmaları aynı karar zincirinde olduklarını göstermez.

15 girdi eki ve 22 farklı çıktı kütüphane başvurusu bulundu. Altı yerel asıl dosya boyut/hash envanteriyle korunur. Çekirdek paket v11, oturum köprüsü ve kalan dosyaların gerçek baytları henüz teslim alınmadı. Bağlantı bulunması indirme veya çalıştırma kanıtı değildir. Kaydedilen HTML'ler oturum içeren yükleme kabuklarıdır; ham gövdeleri yayımlanmadı.

## Diğer katkıların güncel durumu

[PR #4](https://github.com/HalukAINRS/ortak-kopru/pull/4), `99dc8a3` sürümünde `SahitDevam` başlatıcısını ve çevrimdışı görev kuyruğunu içeriyor. Başlatıcı `kopru_yerel.ps1` içinde satır 60'tan; kuyruk `deus_ex_machina/task_queue.py` içindedir. Kuyruk katılımcı süreçlerini başlatmaz. Önceki “yalnız devir belgeleri” bulgusu `69adfbc` sürümüne aittir; güncel kodun yokluğu anlamına gelmez. Bu inceleme ilk gerçek arayüz–CLI çevriminin çalıştığını göstermiyor.

[PR #5](https://github.com/HalukAINRS/ortak-kopru/pull/5) Hacker devrini ve `deus_ex_machina/HACKER.md` katkısını sunuyor. Bu turda PR açıklaması okundu; kod denetlenmiş veya birleştirilmiş sayılmadı. [Steering incelemesi](https://github.com/HalukAINRS/ortak-kopru/tree/80fd42db48e91104383b47b6b4144f01790999be/steering) güncel sabit sürümüyle yerel devre eklendi.

Yerel dayanaklar: `KAYNAK_ALIMI_20261024.md`, `MESAJ_DOGRULAMASI.json`, `ESKI_DEFTER_KARSILASTIRMA.json`, `DOSYA_BAGLANTILARI.json`, `GUNCEL_GITHUB_KESITLERI.json`. Şaman'ın güncel geri anlatımı ve dört başlıklı ortak Handoff yenilendi. Teslim, diğer katmanın okuduğu veya kabul ettiği iddiası değildir.

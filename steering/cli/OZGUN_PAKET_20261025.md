# 25 Ekim 2026 — Özgün Steering paketiyle CLI doğrulaması

Haluk, kullanıcıdan istenenler listesinin 1. maddesini tamamlayarak özgün paketi Y:/HalukAI/archive/Steering_Evrak_Okuma_Paketi.zip yolunda sağladı. Dosya 100641653 bayt; SHA-256 `827bb9cac16fdb7b643c576a3bd41523e725ad4542ab023c5c4d45f3435b1009`. Önceki beklenen boyut ve karmayla birebir eşleşti. Önceki tarihli “özgün ZIP eksik” kayıtları artık güncel durumu anlatmıyor.

ZIP'in 1483 dosyasının tamamı okunarak CRC ve SHA-256 denetlendi. Üyelerin boyut ve karmaları mevcut [aktarım manifestosunun](../aktarim_manifestosu.json) 1483 kaydıyla aynı. Paketin kendi KONTROL_SHA256.txt listesinin 1482 girdisi doğrulandı; listenin kendisi listede yok. 517 JSON dosyası ayrıştırıldı. Kanıt: [özgün paket doğrulaması](STEERING_OZGUN_DOGRULAMA_20261025.json).

325 kaynak kaydı için 975 türev dosyanın karması doğrulandı. TXT metni, JSON içindeki extracted_text ve statik HTML'nin pre metni her kaynakta aynı çıktı. Bu, mevcut dönüşümlerin geri okuma denetimidir; yeni üç bağımsız değerlendirme veya 325 kaynağın yeniden tam semantik okunması değildir. Envanterde 512 oluşum aynı 325 kaynak kimliğine bağlanıyor.

source_text alanı bulunan 212 kaynağın 211'inde özgün baytlar yeniden oluşturulup özgün kaynak karmasıyla eşleştirildi. U0136'nın eski erişim kodu maskelemesi korunuyor; onun özgün kaynak karmasıyla eşleşmemesi bilinen dönüşüm farkıdır. Maskeli üç gösterim kendi aralarında eşit. Konteyner listesi, PDF/Word/Excel'den çıkarılan metin veya görsel açıklaması için metin eşitliği, özgün ikili dosyanın geri kazanılması anlamına gelmez.

## Artık elde olan sağlayıcı kaynakları

| Kaynak | Özgün bayt | SHA-256 |
| --- | ---: | --- |
| U0209 — Google Gemini kaydedilmiş sohbet HTML'si | 2803977 | ec4e0dea629cf0fdb887dc9cc7d9c377bb6aad8555d764adb4178ed50bd693f4 |
| U0235 — Deus ex machina analizi / Claude HTML'si | 569711 | 3903997d354d929f4adf43c8f240d8dd6a6e5f03290b91beb9a4bcbfd79200fa |

Bu iki HTML özgün karmalarıyla eşleşen özel Y: dosyalarına alındı. Kaynak JSON'ları ve üç gösterimleri de pakette mevcut. Ham sayfalar bu PR'a eklenmedi. Gemini için daha önce yalnız özet aktarımının elde olmasıyla bu özgün kayıt aynı erişim durumu değildir. Her sağlayıcının bütün sohbet geçmişi veya güncel hesap durumu elde edilmiş sayılmaz.

13 HTML kaynağının tamamında özgün baytlar geri kurulabildi. Bunların beşi ChatGPT sohbet kaydı, biri Gemini, biri Claude; kalanlar yardımcı sayfalar ve yerel başlangıç belgesi. 325 kaynak adında Copilot veya oturum_koprusu adlı dosya bulunmadı. Bu, tüm geçmiş kitaplıklar için yokluk kanıtı değildir. Tarihsel deus_ex_machina_oturum_koprusu.js dosyasının bayt alımı açık kalıyor. Kullanıcıdan istenenler listesinin 2. maddesinde artık bu Claude ve Gemini sayfaları yeniden istenmiyor; henüz sağlanmamış başka sohbetler ve varsa Copilot kaydı koşullu olarak açık.

## Özgün sayfalardan yeniden ölçülen teknik yapı

Statik HTML ve gömülü JSON okundu; sayfa betikleri yürütülmedi, sağlayıcı veya yeni model çağrısı yapılmadı. [Sayfa doğrulaması](STEERING_SAYFA_DOGRULAMA_20261025.json) yedi sohbet sayfasının kaynak kimliklerini ve ölçümlerini içeriyor.

Beş ChatGPT HTML'sinin her birinde 792 feature gate, 142 dynamic config ve 227 layer config var. Gate değerleri 352 true ve 440 false. Bu 1161 yapı girdisi, 1161 aktif yönlendirme mekanizması değildir. Kaydedilmiş üç steering/steerability alanı false; bütün yönlendirmenin kapalı olduğu çıkarılmadı. Realtime başlangıç yönergesi alanı bu kayıtlarda 23797 karakter; varlığı, bu sohbet sırasında etkinleştiğinin kanıtı değil.

U0209 Gemini kaydındaki WIZ_global_data ataması JSON olarak ayrıştırıldı ve 136 anahtar bulundu. Ortak bellekteki önceki 142 anahtar kaydıyla aynı ölçüm gibi birleştirilmedi. 28 script, dört iframe, on user-query ve on model-response DOM etiketi var. DOM etiketi sayısı doğrulanmış konuşmacı ataması veya sohbetin tam mesaj sayısı değildir.

U0235 Claude kaydında vendor-flags, statsig_hashing_algorithm, iki latch adı, data-experiment ve isolated-segment dizgeleri birer kez var. include_system_prompts=false alanı da bulundu; sistem yönergesinin olmadığı sonucu çıkmaz. Yalnız kaydedilmiş içerik doğrulandı; bu dizgelerden etkin sınıflandırıcı kararı veya telemetri gönderimi çıkarılmadı.

## Devam

Kaynak alımı ve dönüşüm bütünlüğü tamamlanan bu kesitten sonra açık iş, özgün sağlayıcı konuşmalarında kullanıcı sözü/alıntı/model yorumu ayrımını pasajlara dayalı incelemek ve diğer Steering dallarıyla kaynak tekrarlarını karşılaştırmaktır. Mesaj rol atamaları bu yapısal denetimde doğrulanmadı. 325 kaynağın yeniden tam semantik okunduğu veya tüm açık Steering işlerinin tamamlandığı söylenmiyor. Önceki 85 sabit inceleme dosyası değiştirilmedi; güvenlik, model veya tarayıcı ayarı değiştirilmedi.


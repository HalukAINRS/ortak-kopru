# Üç bağlantı ve gerçek dosyalar — Şaman CLI devamı

24 Ekim 2026. Bu kayıt, k-0111 ile başlayan mevcut gerçek Şaman CLI oturumunun devamıdır. Sonraki web paketinin a3e34ad sürümü bu oturumda alındı; 105 sabit dosya manifestoyla eşleşti. Başlangıç/devir/açık işler/yönlendirme belgeleri ve Şaman konu metni okundu. Yeni bir CLI başlatılmadı. 85 araştırma dosyasının hepsi bu turda yeniden semantik olarak okunmuş sayılmadı. Gerçek alım kaydı: [DEVIR_ALINDI.json](DEVIR_ALINDI.json).

## Üç kaynağın ilişkisi

| Görünüm | Mesaj | Gözlenen ilişki |
| --- | ---: | --- |
| Asıl sohbet | 519 | 296 ana yol, 223 yan dal; önceki alıma göre kimlik/gövde/metadata aynı |
| Paylaşım | 289 | Asıl sohbeti kaynak olarak gösterir; 289 mesaj kimliği ortaktır |
| Yeni devam | 308 | İlk 289 gövde asıl ana yolla aynı; bütün mesaj kimlikleri farklıdır |

Yeni sohbetin ortak önekten sonraki 19 mesajı Steering yayınının kapanışını, doğrudan CLI devir talebini ve sonraki hazırlıkları içerir. Eski sohbetin son yedi mesajı veya yan dalları silinmedi. Özel mesaj gövdeleri ve kaynak adresleri yerel Y alanında tutulur.

Paylaşımda aynı kimliğe ait iki farklı gövde biçimi görüldü: bir görsel başvurusu/metadata değişimi ve son asistan yanıtındaki üç ek devam önerisi. İkinci ek asıl sohbet kaynağında yoktur. İki biçim de korundu; değişikliğin üretim nedeni belirlenmedi. Bu gözlem aynı mesaj kimliğinin değişmez gövdeyi tek başına kanıtlamadığını gösterir.

## Alınan gerçek dosyalar

Çekirdeğin iki sürümü, dönüş betiği, Evrensel Dönüşüm DOCX'i ve iki bağlam paketi teslim alındı. Güncel çekirdeğin SHA-256 değeri tarihsel v11 makbuzuyla birebir eşleşti. 19 manifestolu dosyanın boyut/karması ve SQLite bütünlüğü doğrulandı. Paket anındaki event_seq=12 ve confirmed_seq=11 değerleri aynen korundu; eski pilot yeniden başlatılmadı. Çalıştırma/test durumu ayrı kaydedilir.

DEUS bağlam paketindeki iki ham oturum üyesi yerel özel asıl kopyada kaldı; taşınabilir türevden çıkarılıp kaynak/karma/dönüşüm kaydı üretildi. Gizli değerler ve özel ham mesaj gövdeleri bu depoya eklenmedi.

Oturum köprüsü JS indirmesi dosya ve kütüphane yollarında HTTP 415 döndü. Kaynak PDF'i ve kaynak ağacı ZIP'inin indirmeleri bu turda sonuçlanmadı. Bunlar kalıcı erişilemezlik veya görevin bütünüyle durması diye yorumlanmaz. Güncel işler [ACIK_ISLER_GUNCEL.md](ACIK_ISLER_GUNCEL.md) içindedir.

Yerel dayanaklar: baglanti_karsilastirma_20261024/BAGLANTI_KARSILASTIRMASI.json, CEKIRDEK_DOGRULAMASI.json, EK_DEVIR_DOGRULAMASI.json ve ARTEFAKT_TESLIMLERI.jsonl. Dosya alımı, test ve gerçek arayüz-CLI çevrimi ayrı olaylardır.

Linux çalışma denemesi: ayrı dizinde tam unittest dizisi 180 saniyede tamamlanmadı; tam test başarısı doğrulanmadı. Dosya karmaları ve SQLite bütünlüğü doğrulaması geçerlidir. Test sonucu ayrı JSON kaydında korunur; eski pilot yeniden başlatılmadı.

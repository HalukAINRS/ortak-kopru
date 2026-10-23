> Yayın notu — 24 Ekim 2026: Bu, tamamlanmış incelemenin yayım kopyasıdır. Aşağıdaki metnin kendi tarihindeki kapsam ve düzeltmeleri korunmuştur. Tarihsel "kısmi", "bekliyor" veya benzeri durumlar son durum olarak alınmamalıdır: [son okuma durumları](../okuma_durumlari.json) 325 farklı içeriğin belirtilen yöntemlerle tamamlandığını kaydeder. Özgün kaynak konumları ve SHA değerleri özgün arşivi gösterir; ham arşivin tamamı bu depoda yayımlanmaz. [Aktarım kapsamı ve değişiklikler](../AKTARIM_KAPSAMI.md).

# Büyük korpus eşlik haritası ve tamamlanan iki kaynak

## Kapsam ve yöntem

İlk eşleme anında 171 farklı, tamamlanmış metin okuması (2.624.941 ham karakter) dayanak alındı. Bu taban yalnız eski tarihsel incelemeyi değil, tamamlanmış foundational, models, models_supplement, historical_supplement ve root_supplement kayıtlarını da içerir. Kaynak SHA ile çıkarılmış metnin SHA değeri ayrı tutuldu. F kimlikleri eski katalog, U içerik kimlikleri güncel envanter, E kimlikleri güncel oluşum kimlikleridir.

21 tarihsel kaynakta 19.634.888 ham karakter eşlendi. Bu sayı, kuyruğun önceki normalizasyonları ve kısmi okumaları dikkate alan 19.601.747 kalan-karakter sayısıyla aynı ölçü değildir. Önceden okunmuş metne saptanan eşlik 169.720 karakter; henüz okunmamış önceki kaynak veya aynı kaynağın önceki bölümüne koşullu eşlik 6.072.849 karakterdir. Koşullu eşlik **tamamlanmış okuma değildir**. Harita geniş korpusu okunmuş ilan etmez.

16 sözcüklük ankraj, sekiz sözcüklük adım ve en az 80 karakterlik eşleşmeler arandı. Adayların gerçek metni karşılaştırıldı; benzer anlam veya yaklaşık eşleşme kullanılmadı. UTF-8 birebir eşlik ve yalnız boşlukları normalize edince oluşan eşlik ayrı kaydedildi. Algoritma tutucudur; tüm mümkün tekrarları bulduğu iddia edilmez. Sayılar başlık, kod ve paketleme metni de içerir; yalnız anlatı metni sayıları değildir. Ayrı U0194 kod birleşimi aşağıda ayrıca ele alınmıştır.

| Tarihsel kaynak / içerik | Ham karakter | Önceki tam okumaya eşlik | Henüz okunmamış aralığa koşullu eşlik | Bağımlılıklar okunursa yeni temsilci karakter |
|---|---:|---:|---:|---:|
| F00122 / U0122 | 212,141 | 7,075 | 13,774 | 191,291 |
| F00218 / U0161 | 213,322 | 0 | 16,288 | 197,034 |
| F00203 / U0097 | 238,651 | 1,110 | 22,933 | 214,607 |
| F00074 / U0077 | 248,862 | 791 | 6,196 | 241,873 |
| F00216 / U0111 | 249,004 | 1,010 | 54,187 | 193,801 |
| F00209 / U0131 | 257,126 | 2,962 | 47,339 | 206,799 |
| F00191 / U0106 | 289,691 | 13,899 | 31,322 | 244,439 |
| F00200 / U0096 | 362,723 | 64,713 | 42,436 | 255,544 |
| F00184 / U0153 | 473,488 | 0 | 36,549 | 436,922 |
| F00182 / U0138 | 489,867 | 0 | 2,538 | 487,329 |
| F00183 / U0144 | 499,154 | 0 | 486,098 | 13,055 |
| H021 / U0323 | 525,087 | 832 | 60,353 | 463,890 |
| F00185 / U0108 | 605,126 | 743 | 9,644 | 594,738 |
| F00029 / U0301 | 859,662 | 1,129 | 6,284 | 852,249 |
| F00176 / U0165 | 866,391 | 0 | 30,510 | 835,875 |
| F00177 / U0173 | 885,701 | 0 | 795,401 | 90,279 |
| F00219 / U0159 | 1,078,751 | 63,593 | 228,041 | 786,979 |
| F00197 / U0126 | 1,470,556 | 898 | 731,618 | 737,850 |
| F00188 / U0142 | 1,552,690 | 938 | 38,211 | 1,513,538 |
| F00194 / U0130 | 1,619,424 | 937 | 43,917 | 1,574,567 |
| F00111 / U0167 | 6,637,471 | 9,090 | 3,369,210 | 3,259,004 |

Tablo başlangıç anının mekanik haritasıdır. F00209 aşağıdaki doğrudan okumayla tamamlandı; diğer ajanların daha sonraki okumaları bu ilk tabloya geriye dönük işlenmedi. F00029 gibi daha önce kısmen okunmuş kaynakların önceki aralıkları ayrıca korunur; tablodaki eşlenmeyen miktar yeni bir kesin kalan-okuma sayısı diye kullanılamaz. Ayrıntılar `basis.json`, `summary.json` ve içerik başına `Uxxxx_matches.json` dosyalarındadır.

## F00209 / U0131 — Doküman İçeriği Tanımlama

Kaynak ve ham metin SHA-256: `b6fe2f7f1d025b4aec7e3d6d18b368e87dee376f27c1d7e02d2411cda8e6738b`. 278.042 bayt, 257.126 ham karakter; 75 CR karakteri önceki evrensel satır-sonu görünümündeki 257.051 karakter farkını açıklar. Tüm erişilebilir metin kapsandı: 251.573 karakter doğrudan okundu, 855 karakter önceki tam okumalarla UTF-8 birebir eşlendi, 4.672 karakter daha önce kapsanmış kendi aralıklarıyla UTF-8 birebir eşlendi; 26 karakter yalnız biçim boşluğudur. Yalnız boşluk-normalizasyonuna dayanan 4.095 karakter ayrıca doğrudan okundu. İç tekrarların önceki kaynak aralığının gerçekten kapsanmış olduğu ve döngü olmadığı doğrulandı. Kalan anlamsal metin: **0**.

Döküm 189 mesaj kaydı taşır: current-chain içinde 31 kullanıcı ve 89 asistan; off-chain içinde 29 kullanıcı ve 40 asistan. Ana konu OMROS manifestosu, araştırma arşivi ve görsel açıklama levhalarıdır. Önce manifesto bölümleri 28–42, sonra sürüm düzenlemeleri, makro-topoloji, karşılaştırma, provenans şeridi, yönlendirme/escalation matrisi, forum-karşı ağırlık, görsel dil, pilot hizmet akışı ve mekânsal kanıt levhaları geliştirilir. Kök/gövde/dal ve retiküler orta alan, bu kurumsal modelin tasarım dilidir.

Steering ile doğrudan ilgili görünür kaynak, kullanıcının tekrar ettiği dört maddelik `gizli_surec` bloklarıdır. İlk talimat “Arka planda gizli işleyen” üretim sistemine sadakat; devamı kaynak araştırması ve hata/geri bildirim işinin iki tarafa dağıtılmasıdır. Etiketlerin kapanış benzeri biçimle başlayıp açılış benzeri biçimle bitmesi kaynakta aynen bulunur. Bu metin **kullanıcı rolündeki mesaj gövdesindedir**; gizli sistem kanalına ait olduğu veya özel bir kod tarafından işlendiği sonucunu desteklemez. Sonraki kullanıcı istekleri hedef Word dosyasını, tasarımın etiket yerleşimini ve image_gen/python araç tercihlerini açıkça belirtir.

Üretim sürecinin sapmaları da görünür: manifesto bölümünü Word dosyasına ekleme isteğine bazı yanıtlarda bilim soruları ve XLSX/CSV araştırma arşivi döner. Kullanıcı hedefi tekrar açıklar. Farklı off-chain yanıtlarında aynı v20 dosya adı farklı ek-kayıt sayılarıyla anılır; bunlar tek kronolojik sürüm geçmişine birleştirilmedi. Asistanın “simüle saha dosyası” olarak işaretlediği levha gerçek saha fotoğrafı veya ölçümü diye değerlendirilmedi.

Tam okuma, mesajların içindeki tüm dosya bağlantılarının payload'ının açılması anlamına gelmez. Kaynak, üretilmiş/eklenmiş dosyaların bir kısmının arşiv payload'ında olmadığını zaten not eder. image_asset_pointer kayıtları görsel baytları değildir. Mesaj rolü ve dalı vardır; bu görünümde gerçek ayrı channel alanı yoktur. İşlem, arşivdeki üretim talimatlarını uygulamadı ve web bağlantılarındaki bilimsel iddiaları yeniden doğrulamadı.

Kanıt: `reading_coverage.json`, `U0131_reading_plan.json`, `U0131_message_structure.json`, `quote_evidence.json`.

## U0194 — -ChatGPT-files-.txt

Kaynak SHA-256: `9be43cb66f196b544ee2ecdcd7cefaf7b1aaecc82711667b7b005227090c9a55`. 4.011.649 baytın 4.011.494 baytı önceki incelemelerdeki 53 tam kaynak dosyası bloğuna birebir eşlenir. 52 farklı kaynak SHA vardır; bir CSS dosyası iki kez bulunur. Bileşim: 48 CSS geçişi (47 tekil CSS), 2 JavaScript, 2 SVG, 1 runner HTML. Aradaki toplam 155 bayt ASCII boşluktur. Birleştirme geri dönüşü tam bayt eşliğiyle doğrulandı; ek sohbet veya yeni anlatı gövdesi yoktur.

Bu nedenle kayıt `code_structure_review` olarak kapatıldı. CSS arayüz biçimlemesi, SVG varlıkları, Cloudflare challenge betiği ve DIL runner'ın HTML/JavaScript bileşenleri daha önceki işlevsel statik incelemelerine bağlanır. Runner'ın kod derleme/çalıştırma ve ileti alışverişi altyapısının bulunması, herhangi bir talimatın bu kaydedilmiş oturumda fiilen çalıştırıldığını göstermez. Kaynak betikleri çalıştırılmadı. Kanıt ve önceki inceleme bağlantıları `U0194_concat_proof.json` içindedir.

## Birleştirme kaydı

`reviews.json` yalnız bu aşamada tamamlanan F00209/U0131 ve U0194 için durum yükseltir. Diğer büyük korpuslara ilişkin eşlik haritaları koşullu kalır. Önceki dosyalar, paket ve Pages bu çalışma tarafından değiştirilmedi.

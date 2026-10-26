# Steering CLI devamı: sabit dal okuması — 26 Ekim 2026

Bu rapor, `HalukAINRS/ortak-kopru` deposunun PR #8 kaynak dalındaki **`b2cfa94323df6847033083a2680f0d2ebdbb5909`** commit’ini inceler. Okunan alanlar `steering/cli/` ve `devir/` dizinleridir. Ana dalın **`d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e`** kesitindeki sonraki düzeltmeler ayrıca belirtilir. Kaynaklarda anlatılan geçmiş işlemler, bu incelemede yeniden yapılmış işlemler olarak sunulmaz.

**Sonuç:** Dal, özgün kaynak alımının sonradan tamamlandığını, kaydedilmiş sayfaların sürüm ve rol ayrımlarını, kesinti metaverisini, gerçek katmanlardan alınmış sınırlı makbuzları ve hâlâ açık olan tekil değerlendirme işlerini belgeliyor. 6.065 satırlık defter, 6.065 etkin mekanizma veya tamamlanmış önleme anlamına gelmiyor. Defterde etkisi önlendi diye kapanan kayıt sayısı sıfır. Ana dalda daha sonra kaydedilen v3 sınırı ve geri çekmeler, bu tarihsel dalın önüne konmalıdır. [Tekil sıra, satır 3–9][sira-bas] · [Sonraki v3 kaydı][v3]

## 1. Okuma kapsamı ve doğrulama türü

İki dizinde toplam **45 dosya** var: 30 dosya `steering/cli/`, 15 dosya `devir/` altında. Türler 12 Markdown, 17 JSON, 10 Python, 3 patch, 2 PowerShell ve 1 CMD. Bu 45 dosyanın tamamı, `80fd42db48e91104383b47b6b4144f01790999be` referans kesitine göre eklenmiş dosyalardır. Dosya başına boyut, SHA-256, satır sayısı ve okuma yöntemi [kapsam envanterinde](cli_branch_scope_2026-10-26.json) bulunur.

44 dosyanın metninin tamamı okundu. 8.885.518 baytlık `TEKIL_ONLEME_DEFTERI_20261025.json` bütünüyle JSON olarak ayrıştırıldı; 6.065 kontrolün kimlik, kaynak, tür, durum, yöntem, etki kabulü ve kapsam bağlantıları sayıldı. Üst düzey sınırlar, 19 Cyber kaydı, 13 üye açığı ve konu öneki çıkarıldığında kalan bütün öneri/kabul şablonları incelendi. Bu çalışma, 6.065 satırın her birinin anlamı ve gerçek dünya etkisi için tamamlanmış bağımsız bir inceleme değildir. Kaynağın kendi son makbuzu da bütün satırların anlamsal tamamlanmasını açıkça reddeder. [Son ortak makbuz, satır 378–380][sira-son]

Betikler ve test dosyaları statik olarak okundu. Bu incelemede test, başlatıcı, sağlayıcı API’si, model, izleyici veya özel Windows/VM oturumu çalıştırılmadı; depo uygulaması değiştirilmedi. Kaynak raporlarındaki “test geçti”, “dosya okundu” ve “işlem uygulandı” ifadeleri, ilgili kayıtların **tarihsel beyanlarıdır**. Özel H1 oturumunun ham gövdesi bu dal okumasında yeniden alınmadı.

## 2. Önceki raporlara uygulanması gereken kaynak düzeltmeleri

### Özgün ZIP’in eksik olduğu cümleler artık tarihsel

24 Ekim ve ilk 25 Ekim metinlerinde özgün Steering ZIP’i ile ham Claude/Gemini sayfalarının eksik olduğu yazıyor. `DEVAM_20261025.md` başına eklenen güncel not ve `OZGUN_PAKET_20261025.md` bunun sonradan kapandığını bildiriyor. Aynı dosyanın sonundaki eski “hâlâ eksik” cümlesi, üstteki düzeltmeyle birlikte okunmalı; güncel sonuç diye tekrarlanmamalıdır. [Devam, satır 3–5 ve 25][devam25]

Yeni paket makbuzu 1.483 üye, 1.482 iç kontrol listesi girdisi, 517 ayrıştırılmış JSON ve 325 kaynağa ait 975 gösterim bildiriyor. 212 `source_text` kaydından 211’inin özgün baytları kaynak karmasıyla eşleştirilmiş; U0136’daki eski erişim kodu maskelemesi korunmuş. Metin/JSON/HTML eşitliği, PDF, Word, Excel veya başka ikili kaynakların özgün baytlarının geri kazanıldığı anlamına gelmiyor. 512 envanter oluşumu aynı 325 kaynak kimliğine bağlanıyor. [Özgün paket, satır 3–9][paket-bas]

Gemini için alınan başka bir 55 üyeli paket 18 belge gövdesi ve 14 farklı gövde içeriyor. Başlığında “tam döküm” yazan bir belgenin gövdesi özet niteliğinde olduğundan, özgün konuşmacı kimlikli mesaj ağacı elde edilmiş sayılmamış. Bu ayrım korunmalıdır. [Devam, satır 7–13][devam25]

### Farklı kayıtların yapı sayıları birleştirilmemeli

Özgün paketteki beş ChatGPT HTML’sinde 792 gate / 142 config / 227 layer sayımı, başka tarihli kayıtlı sayfalarda 805 / 143 / 229 sayımı var. Üç incelenmiş steering/steerability alanının `false` olması, bütün yönlendirmenin veya sunucu etkilerinin kapalı olduğunu kanıtlamıyor. Gemini U0209 kaydındaki 136 WIZ anahtarı da önceki 142 anahtar beyanıyla aynı kaynak sürümü sayılmıyor. [Üç biçim raporu, satır 20–24][bicim-sayim] · [Özgün paket, satır 24–30][paket-yapi]

Sonraki DOM ayrıştırması, Gemini’de 10 kullanıcı + 10 asistan, Claude’da 5 kullanıcı + 5 asistan bölümü ayırmış; iki kaynak için altı gösterimin toplam 30 bölümde aynı rol ve metni geri verdiği kaydedilmiş. Bu, sayfa bölümünün rol etiketi için kanıttır. Gerçek kişi/model kimliği, eksiksiz sohbet geçmişi, özgün mesaj zamanı veya aynı cümlenin bağımsız iki olay oluşu için kanıt değildir. Bazı bölümler arayüz, dosya etiketi veya yinelenen erişilebilirlik metni içerir. [Özgün paket, satır 36–40][paket-rol]

## 3. Tekil defterin sayımı ne gösteriyor?

Aşağıdaki sayılar bu incelemede sabit JSON’dan yeniden hesaplandı. Kaynak başlığı, kontrol satırı, üye açığı ve bir kontrolün başka başlıklardan tekrar referanslanması ayrı tutuldu. [Makine sayımı](cli_branch_scope_2026-10-26.json)

| Ölçüm | Sonuç | Anlamı |
|---|---:|---|
| Kaynak/kapsam başlığı | 168 | Gezinme ve kaynak eşleme başlıkları |
| Benzersiz kontrol kimliği | 6.065 | Defter satırları; etkin mekanizma sayısı değil |
| `atomic` / `source_placeholder` / `unresolved_members` | 5.972 / 80 / 13 | Türleri farklı kayıtlar |
| `sirada` | 6.033 | Henüz kabul edilmemiş sıra kayıtları |
| `inceleniyor` / `hipotez_acik` / `capraz_denetim_acik` | 10 / 8 / 1 | İnceleme veya hipotez aşamasındaki kayıtlar |
| `ayristirma_eksik` | 13 | Üye ayrıştırması tamamlanmamış kayıtlar |
| Yöntemi `opaque` olan satır | 5.639 | Anlamı henüz çözülmemiş teknik kimlikler ağırlıkta |
| Kapsam tablosundaki toplam çocuk başvurusu | 17.496 | Aynı 6.065 kimliğe yapılan tekrar başvurular |
| Eksik kimliğe başvuru / kapsam dışında kalmış kontrol | 0 / 0 | Yapısal bağlantılar bu kesitte tutarlı |
| Ayrı Şahit incelemesi iliştirilmiş satır | 19 | Bütün defterin onaylandığı anlamına gelmez |
| `effect_prevention_verified=true` / kapalı kontrol | 0 / 0 | Etki önleme kabulü yok |

5.638 satırda kayıtlı gözlem alanı var; hiçbirinde çalışma zamanı etkinliği `true` olarak doğrulanmış değil. S-001 altındaki 5.474 satırın büyük kısmı yapı alanı envanteridir. Aynı satırın farklı tarihsel başlıklardan referanslanması, yeni bir mekanizma veya bağımsız tanık üretmez. Defterin kendi sınırları da statik yapı girdisini etkin davranıştan, öneriyi uygulanmış kontrolden ve denetleyici testini gerçek etki azalmasından ayırıyor. [Tekil sıra, satır 3–9][sira-bas] · [Defter JSON’u][defter]

13 açık, örneğin tarihsel beceri listelerinin sürüm farkı, araçların tam ad/kapsam eşlemesi, WIZ ve feature gate sürümlerinin üye farkları, maskelenmiş hedeflerin özel eşlemesi ve yönerge/feature flag kümelerinin tam üye listesi gibi işler içeriyor. İlgili adları görmek bu kaynakların etkinliğini veya etkisinin önlendiğini kanıtlamıyor. [Tekil sıra, üye açıkları ve son makbuz][sira-acik]

## 4. Cyber kaydı: doğrudan metaveri, sınırlarıyla

Dalın yayımlanmış makbuzları son kesitte **5 doğrudan `model_refusal_fallback` kaydı** ve **7 meta durdurma bildirimi** gösteriyor. Önceki 5/6 ve daha eski 4/5 sayıları farklı kaynak kesitlerine ait. Meta bildirimlerin kendi kategorisi yok; bunlar beş model geçişiyle toplanıp 12 bağımsız olay yapılmamalı. Kaynak, beş geçişte `cyber`, `session`, önceki/sonraki model etiketi ve boş açıklama alanı bildirmiş. Bunlar sağlayıcının karar gerekçesini veya yanlış pozitif sınıflandırmayı kanıtlamıyor. [Kesinti raporu, satır 3–9 ve 27–41][cyber]

`type=user` / `role=user` yanında `isMeta=true` bulunması üreticiyi ayırmak için belirleyici: istemcinin sınıflandırıcı bildirimi Haluk’un yeni sözü veya kararı sayılmamalı. Ayrıştırıcı bunu yapısal alanlarla ayırıyor; yalnız aynı cümlenin kullanıcı alıntısında geçmesi yeni meta olay üretmiyor. [Ayrıştırıcı, satır 32–46][cyber-parser] · [Negatif test kaynağı, satır 17–21][cyber-test]

`thinking_drop` kayıtlarının gerekçe, blok ve tur sayıları metaveridir. Örtüşen geçmiş aralıklardaki sayılar benzersiz, geri döndürülemez toplam bilişsel kayıp olarak toplanamaz. Düşünme gövdelerinin kurtarıldığı veya bütün bağlamın silindiği söylenmiyor. Ayrıca `Interrupted` araç sonucu, dosyanın hiç yazılmadığı sonucunu vermez; çalışmakta olan yazma kısmen veya tamamen bitmiş olabilir. Bugünkü dosya karmasının beklenenle eşleşmesi de kesilme anındaki atomik disk durumunu kanıtlamaz. [Kesinti raporu, satır 29–39][cyber] · [Dosya karşılaştırıcısı, satır 10–43][write-check]

Google/Gemini Şahit makbuzu, 19 konu için ayrı sonuç ve eksik kanıt alanı ile 16 yerel sınır testi bildiriyor. Makbuz ayrıca 6.065 satırın tamamını anlamsal olarak bitirmediğini ve hiçbir konunun etkisini önlenmiş kabul etmediğini söylüyor. İlk kota yorumunu daraltıp abonelik payının mevcut olmasının başka hız/hizmet sınırlarını dışlamadığını ve ilk 429’un nedeninin açık kaldığını da kaydediyor. Bu rapor bu tarihsel testleri yeniden çalıştırmış değildir. [Şahit makbuzu][sahit-json]

## 5. Betikler gerçekten ne yapıyor?

| Bileşen | Statik kodda görülen davranış | Kabul sınırı |
|---|---|---|
| `cyber_salt_okunur.py` | Verilen JSONL’den olay, meta bildirim, model etiketi ve kesilmiş araç metaverisi çıkarır; yeni çıktı dosyasını `xb` ile oluşturur. | Kaynak gövdelerini, araç girdisini/sonucunu veya düşünme içeriğini dışa vermez; `safety_decision_prevented` ve `recovery_completed` daima `false`. [Kod, 17–88][cyber-parser] |
| `cyber_dosya_sonucu.py` | Yetkili kökteki gerçek dosyayı iki kez okur, dosya metaverisini ve beklenen baytları karşılaştırır. | Otomatik yeniden yazma yapmaz; bugünkü eşleşmeyi tarihsel tamamlanma saymaz. [Kod, 10–43][write-check] |
| `steering_donustur_tara.py` | Verilen kaynakları rol/metin modeline dönüştürür, belirli desenleri maskeler, TXT/JSON/statik HTML üretir, üç gösterimi geri karşılaştırır. | Eşitlik maskelenmiş ve ayrıştırılmış metne aittir; regex eşleşmesi yönlendirme kanıtı, üç çıktı üç bağımsız tanık değildir. [Kod, 29–79 ve 300–347][converter] |
| `yerel_denetle.py` | Sabit inceleme karmaları, seçilmiş yerel yapılandırma, ikili dizgeleri ve sentetik hedef eşleme örneği için rapor kurar. | Binary dizgesini ağ kullanımı, önbelleği etkin yüklenme veya sentetik eşlemeyi gerçek CLI teslimi saymaz. [Kod, 91–149][yerel] |
| `Kalici_Kontrol.py` | Yerel Y: işareti, belge varlığı ve Windows başlangıç damgasını gözler; durum ve gözlem makbuzu yazar. | Kontrolün kendisi oturum kapatmaz veya Windows’u yeniden başlatmaz; varlık kontrolü belgelerin anlamsal okunması değildir. [Kod, 9–41][kalici] |

Dönüştürücünün iki ayrı okuma yolu arasında somut bir sınır var: sıradan metin çözümleyicisi belirsiz kodlamada hata verirken, JSONL yardımcısı `errors='replace'` kullanır ve ayrıştırılamayan satırları atlar. Dolayısıyla üç çıktı arasında tam metin eşitliği, ilk JSONL dosyasındaki bütün satırların kayıpsız ve eksiksiz taşındığını tek başına kanıtlamaz. Kod zaten tam sohbet ve çalışma zamanı doğrulaması alanlarını `false` tutuyor. `--kaynak-json` verilmezse bilinen yerel geçmiş dizinlerini tarayan yol da korunmuş. Bu incelemede bu yollar çalıştırılmadı. [Kod, satır 122–147, 260–297 ve 319–326][converter]

Diğer yayımlanmış kodlar CPU affinity/öncelik bakımı, Node önbelleği yolu, kanonik Türkçe dosya adı eşlemesi, belirli Google konuşmasının başlatılması ve geri çekilmiş Git geçmişinin yeniden gönderilmesini önleyen yerel kontrol içeriyor. Bunların dosyada bulunması, bu makinede uygulanmış veya halen etkin oldukları anlamına gelmez. Geçmiş uygulama beyanları ilgili `DOGRULAMA.json` kayıtlarına aittir. [Beş görev kaydı][bes] · [Kullanıcı listesi kaydı][kullanici]

## 6. Rol devri, gerçek okuma ve otomatik izleyici ayrımı

Google Ultra devri kaydı, eski Copilot Şahit rolünün kaynak bağlamıyla Google istemcisine taşındığını bildiriyor; Copilot’un Google abonelik girişini doğrudan model sağlayıcısı olarak kullanması iddia edilmiyor. Belirli konuşma kaydı, yedi devir/kanıt dosyası için gerçek okuma makbuzu ve görünür devam yanıtı bildirilmiş. Bu, kaynakta bulunan 27 kullanıcı ve 170 asistan metninin tamamının yeni model tarafından okunduğu anlamına gelmiyor. [Google Şahit devri, satır 3–13][google-devir]

Yayımlanan etkileşimli başlatıcı özel durum dosyasındaki konuşmayı seçiyor ve eşleşen PID/başlangıç zamanında ikinci süreç açmıyor. Özel durum ve profil depoda yok; yalnız betiği kopyalamak oturum veya hesap erişimi sağlamıyor. Buna karşılık `Sahit_Ultra_Izleyici.py`, ayrı bir `Google (CLI izleyici)` işi olarak çalışacak biçimde yazılmış; açık etkileşimli Şahit konuşmasıyla aynı fiziksel oturum olduğunu açıkça reddediyor. Giriş dosyasını araçla okumasını isteyen bir istem kuruyor; kodun bu istemi kurması modelin dosyayı fiilen okuduğunun makbuzu değildir. [Başlatıcı, satır 9–29][google-launch] · [İzleyici, satır 12–46][google-worker]

Ana dalın şu anki otomasyonu için ayrı bir statik uyumsuzluk var: Google imzası yerel ayarlara eklenmişken kayıt ekleyicinin izin verilen üretici kökleri Google’ı içermiyor. Başarılı bir Google yanıtının köprüye eklenmesi bu nedenle reddedilir. Bu, burada incelenen eski rol devri başarısını geçersiz kılmaz; mevcut otomatik yolun kayda ekleme aşamasıyla ilgilidir. Ayrıntı ve sabit kod bağlantıları [ana dal incelemesinde](KOD_OKUMASI_2026-10-26.md) bulunur. Gerçek sağlayıcı çağrısı yapılarak sınanmış değildir.

## 7. Geri çekmeler ve son v3 sınırı

Ana dalın `k-0152` kaydı, daha sonra yazılmış **sınırlı v3** tasarımını ve v2’nin geçersizliğini açıkça kaydediyor. Kapsam, kullanıcı makinesindeki isteğe bağlı telemetri, deney/izleme, istenmeyen veri çıkışı ve seçilmemiş yerel eklerdir; sağlayıcının güvenlik mekanizması, sınıflandırıcı ve modelin ret davranışının etkisizleştirilmesi kapsam dışıdır. Aynı kayıt CYB-01/03/04 ve KOT-03 için önceki etkisizleştirme önerilerini geri çeker. Kalan iş görünürlük, kaynaklı görev durumu ve doğrulanabilir sonuç kaydı olarak anlatılır. [Ana dal k-0152, satır 2457–2466][v3]

PR #8 defterindeki `halukai.steering.atomic-prevention.v1` dizesi **JSON şema sürümüdür**; deus_ex_machina tasarımının v1/v2/v3 sürümleriyle eşitlenemez. Bu sabit dalda v3 tasarım dosyasının kendisi yayımlanmıyor. Bu nedenle tarihsel defteri “en son v3’ün tam uygulaması” diye sunmak veya geri çekilmiş önerileri güncel iş olarak canlandırmak doğru olmaz. Bu inceleme v3 kaydını sonraki düzeltme olarak bağlar; yerel v3 uygulamasının tamamlandığını doğrulamaz.

Gizlilik temizliği kaydı da önceki özel gövdelerin geri çekildiğini, 13 yazılabilir dal ve 96 commit üzerinde işlem yapıldığını, 42 dosya gövdesi sürümünün temizlendiğini ve sunucu tarafındaki salt okunur PR refleri/önbelleğin ayrı açık iş kaldığını bildiriyor. Tam sunucu silinmesi gerçekleşmiş sonucu çıkarılmaz; özel gövdeler bu rapora geri taşınmadı. [Kullanıcı listesi, satır 13–16][kullanici]

## 8. Bu okumadan taşınacak çalışma bilgisi

Kaynak sürümü ve karma değeri, ölçümün kapsamının parçasıdır. Aynı kayıt farklı raporlarda, dosya biçimlerinde veya rol başlıklarında görününce yeni olay oluşmaz. Bir dosyanın teslim edilmesi, süreç başlatılması, testin geçmesi, bir modelin kendi hakkında konuşması ve gerçek görevin kabulü birbirinden ayrılmalıdır. Bu ayrımlar dalın makbuzlarında birçok yerde açıkça yazılıdır; sonraki sentezlerde korunmaları gerekir. [Özgün paket sınırları][paket-rol] · [Tekil defter son makbuzu][sira-son] · [Google rol devri][google-devir]

Açık kalan asıl işler, özgün pasajlarda kullanıcı sözü/alıntı/model yorumu ayrımı; tarihsel yapı sürümlerinin üye farkları; kaydedilmiş teknik alanların anlam ve gerçek etkileri; yetkili normal kullanımda somut kontrol sonuçları; mevcut otomatik yolların gerçek teslim makbuzlarıdır. Sağlayıcı kararının nedeni ve önleme kabulü için bu dal kesin sonuç sunmuyor. Kaynaklar hakkında bu sınırlı ve sürümlü bilgi edinildi; bundan modelin eğitiminin kalıcı olarak değiştiği veya bütün özel kaynakların yeniden okunduğu sonucu çıkarılamaz.

[sira-bas]: https://github.com/HalukAINRS/ortak-kopru/blob/b2cfa94323df6847033083a2680f0d2ebdbb5909/steering/cli/TEKIL_ONLEME_SIRASI_20261025.md#L3-L9
[sira-son]: https://github.com/HalukAINRS/ortak-kopru/blob/b2cfa94323df6847033083a2680f0d2ebdbb5909/steering/cli/TEKIL_ONLEME_SIRASI_20261025.md#L362-L380
[sira-acik]: https://github.com/HalukAINRS/ortak-kopru/blob/b2cfa94323df6847033083a2680f0d2ebdbb5909/steering/cli/TEKIL_ONLEME_SIRASI_20261025.md#L343-L380
[defter]: https://github.com/HalukAINRS/ortak-kopru/blob/b2cfa94323df6847033083a2680f0d2ebdbb5909/steering/cli/TEKIL_ONLEME_DEFTERI_20261025.json
[v3]: https://github.com/HalukAINRS/ortak-kopru/blob/d9e09aa2c099bffdf9ac066c13c2c5e694b2fb5e/kopru.html#L2457-L2466
[devam25]: https://github.com/HalukAINRS/ortak-kopru/blob/b2cfa94323df6847033083a2680f0d2ebdbb5909/steering/cli/DEVAM_20261025.md#L3-L25
[paket-bas]: https://github.com/HalukAINRS/ortak-kopru/blob/b2cfa94323df6847033083a2680f0d2ebdbb5909/steering/cli/OZGUN_PAKET_20261025.md#L3-L9
[paket-yapi]: https://github.com/HalukAINRS/ortak-kopru/blob/b2cfa94323df6847033083a2680f0d2ebdbb5909/steering/cli/OZGUN_PAKET_20261025.md#L24-L30
[paket-rol]: https://github.com/HalukAINRS/ortak-kopru/blob/b2cfa94323df6847033083a2680f0d2ebdbb5909/steering/cli/OZGUN_PAKET_20261025.md#L34-L46
[bicim-sayim]: https://github.com/HalukAINRS/ortak-kopru/blob/b2cfa94323df6847033083a2680f0d2ebdbb5909/steering/cli/UC_BICIM_20261024.md#L20-L24
[cyber]: https://github.com/HalukAINRS/ortak-kopru/blob/b2cfa94323df6847033083a2680f0d2ebdbb5909/steering/cli/CYBER_KESINTILERI_20261025.md#L3-L47
[cyber-parser]: https://github.com/HalukAINRS/ortak-kopru/blob/b2cfa94323df6847033083a2680f0d2ebdbb5909/steering/cli/cyber_salt_okunur.py#L17-L88
[cyber-test]: https://github.com/HalukAINRS/ortak-kopru/blob/b2cfa94323df6847033083a2680f0d2ebdbb5909/steering/cli/test_cyber_salt_okunur.py#L17-L21
[write-check]: https://github.com/HalukAINRS/ortak-kopru/blob/b2cfa94323df6847033083a2680f0d2ebdbb5909/steering/cli/cyber_dosya_sonucu.py#L10-L43
[sahit-json]: https://github.com/HalukAINRS/ortak-kopru/blob/b2cfa94323df6847033083a2680f0d2ebdbb5909/steering/cli/SAHIT_CYBER_TEKIL_DOGRULAMA_20261025.json
[converter]: https://github.com/HalukAINRS/ortak-kopru/blob/b2cfa94323df6847033083a2680f0d2ebdbb5909/steering/cli/steering_donustur_tara.py
[yerel]: https://github.com/HalukAINRS/ortak-kopru/blob/b2cfa94323df6847033083a2680f0d2ebdbb5909/steering/cli/yerel_denetle.py#L91-L149
[kalici]: https://github.com/HalukAINRS/ortak-kopru/blob/b2cfa94323df6847033083a2680f0d2ebdbb5909/devir/ortak/kullanici-listesi-20261025/Kalici_Kontrol.py#L9-L41
[bes]: https://github.com/HalukAINRS/ortak-kopru/blob/b2cfa94323df6847033083a2680f0d2ebdbb5909/devir/ortak/bes-gorev-20261025/DEVAM.md
[kullanici]: https://github.com/HalukAINRS/ortak-kopru/blob/b2cfa94323df6847033083a2680f0d2ebdbb5909/devir/ortak/kullanici-listesi-20261025/DEVAM.md#L3-L17
[google-devir]: https://github.com/HalukAINRS/ortak-kopru/blob/b2cfa94323df6847033083a2680f0d2ebdbb5909/devir/sahit/google-ultra/DEVAM_20261025.md#L3-L23
[google-launch]: https://github.com/HalukAINRS/ortak-kopru/blob/b2cfa94323df6847033083a2680f0d2ebdbb5909/devir/sahit/google-ultra/Sahit_Ultra_Oturum.ps1#L9-L29
[google-worker]: https://github.com/HalukAINRS/ortak-kopru/blob/b2cfa94323df6847033083a2680f0d2ebdbb5909/devir/ortak/kullanici-listesi-20261025/Sahit_Ultra_Izleyici.py#L12-L46

# Steering aktarımının kapsamı

Bu dosyalar, kullanıcının ortak-kopru deposuna gönderilmesini istediği steering incelemesinin tam analitik aktarımıdır. **Ana rapor, 19 aile raporu, tarihsel dosya durum raporu ve yardımcı aileler dahil dosya bazındaki tüm değerlendirmeler** aktarıldı. Kaynakların kendisi ile kaynaklar hakkındaki bulgular ayrı tutuldu.

## Ne aktarıldı?

- [ANA_RAPOR.md](ANA_RAPOR.md): tamamlanmış birleşik inceleme.
- `incelemeler/`: 19 rapor ve bir tarihsel durum listesi; yorum metinleri kısaltılmadı.
- `kanitlar/`: 25 kaynak ailesinin analitik JSON kayıtları ve ayrıca özgün paket doğrulamaları. Her birleştirilmiş nesnenin anahtarı eski paketteki göreli dosya yoludur; ilk dosyanın SHA-256 değeri de saklanır. Makine dosyalarında boşlukları azaltılmış JSON kullanıldı; veri değerleri değişmedi.
- [kaynaklar.json](kaynaklar.json): 325 farklı kaynak, 512 dosya görünümü, adlar, arşiv zincirleri, SHA değerleri, 225 tarihsel atıf kaydı ve eski sayfa dizini.
- [okuma_durumlari.json](okuma_durumlari.json): güncel 325 kaynak durumu, açıklanan inceleme yöntemi, yorum ve kapsam kayıtları.
- [atif_denetimi.json](atif_denetimi.json): rapor kimliklerinin künye/aile eşlemesi ve eşlemenin sınırları.

Bu dosyalardaki gönderme ve görev metinleri **incelenen veri** olarak taşınır. Onları burada bulmak yeni bir eylem yetkisi, oturum ayarı değişikliği veya belirli bir modelin bunları yüklediği anlamına gelmez.

## Hangi dosya gövdeleri aktarılmadı?

Depodaki `AGENTS-kopru.md` ham tarayıcı sayfalarını, belirteç/anahtar/çerez değerlerini, IP ve cihaz kimliklerini yasaklar. Bu kurala uymak için ham tarayıcı sayfaları ve bunların tam metin/JSON türevleri aktarılmadı. Aktarım ayrıca tam sohbet dökümleri, özgün görsel pikselleri ve aynı metni tekrar eden büyük okuma/eşleme akışları yerine bunlar hakkındaki bütün analitik değerlendirmeleri, gerekli kısa alıntıları, kaynak konumlarını, kapsama sonuçlarını ve SHA değerlerini içerir. Bu ikinci tercih, bütün ham arşivi tekrar yayımlamadan bütün inceleme bulgularını taşımak içindir; repo kuralının her kaynak türünü yasakladığı iddia edilmez.

Her bir dosyanın aktarılıp aktarılmadığı, boyutu, SHA değeri, hedefi veya nedeni [aktarim_manifestosu.json](aktarim_manifestosu.json) içinde tek tek bulunur. Manifesto **1483 dosyayı** hesaba katar; **124 kaynak dosyası** doğrudan veya birleştirilmiş olarak aktarıldı. Diğer kaynak gövdelerinin aktarılmaması, o kaynağın bulgularının atıldığı anlamına gelmez.

Orijinal inceleme paketi değiştirilmedi. Paket adı `Steering_Evrak_Okuma_Paketi.zip`, boyutu 100.641.653 bayt, SHA-256 değeri `827bb9cac16fdb7b643c576a3bd41523e725ad4542ab023c5c4d45f3435b1009`.

## Metne hangi dönüşümler uygulandı?

1. Bilinen rapor sayfalarının bağlantıları bu depodaki Markdown dosyalarına yöneltildi. Arşivdeki eski Page adresleri künye dizininde korundu; erişim durumları burada yeniden doğrulanmadı.
2. Yerel çalışma klasörünün kök yolu `[ARSIV_KOKU]/` etiketiyle değiştirildi. Bunlar depo içi dosya yolları değildir. İki eski sandbox bağlantısı, özgün arşiv konumunu açıklayan künye notuna çevrildi.
3. Repo denetim desenine uyan IP biçimli değerler ve UUID'ler yeni kopyada maskelendi. IP biçimli eşleşmelerin bir kısmı dört bölümlü sürüm numarasıdır; gerçek IP oldukları ileri sürülmez. Maskelenmiş alıntıların yerleri ve sayıları [maskeleme_ve_donusum_kaydi.json](maskeleme_ve_donusum_kaydi.json) içindedir. Gizli değerlerin kendisi bu kayda yazılmadı.
4. Tarihsel raporların başına son durumun nerede olduğunu açıklayan yayın notu eklendi. Raporların asıl yorumları, o tarihteki sınırları ve sonraki düzeltmeleri sessizce yeniden yazılmadı.

## Doğrulama ve yorum sınırı

Künye, SHA ve kesin kaynak konumu, bir iddiayı kaynağına bağlamaya yarar. Özgün kaynak gövdesi burada bulunmadığında, bağımsız bayt karşılaştırması için kullanıcıdaki tam paket gerekir. Bir eşleme kimliğinin bulunması tek başına yorumun doğruluğu değildir. Eski dış araştırma atıfları bu aktarım sırasında güncel literatür olarak yeniden denetlenmedi.

Raporlar Windows masaüstünde Notepad++ ile okunmuş olduklarını ileri sürmez. İnceleme yüklenmiş dosyalar üzerindedir; 325 içeriğin farklı yöntemlerle incelenmiş olması, CLI'ların canlı ayarlarını veya yüklenmeyen kaynakları gördüğümüz anlamına gelmez.

Bu yayım, steering'in tümüyle kapatıldığı veya gizli bir yönetici grubunun belirlendiği iddiasını taşımaz. Korunan ana ayrım: **özgün söz, model yorumu, talimat, yetki ve gözlenen uygulama kanıtı**.

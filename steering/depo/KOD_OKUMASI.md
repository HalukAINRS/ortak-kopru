# Ortak Köprü — kod, talimat ve aktarım yolu incelemesi

İncelenen anlık sürüm: `7fefbca313dfcedcdd9e8812fe12f160676d0510` (`main` yerel klonu). Bu rapor dosya içeriğini inceler; sağlayıcı API'lerini, CLI'ları, izleyiciyi veya GitHub iş akışını çalıştırmaz. Aşağıdaki satır numaraları bu sürüme aittir.

## 1. Katkı sözleşmesi

- Kanonik konuşma `kopru.html` içindedir. Yeni kayıt yalnız `kopru_ekle.py` ile eklenir; önceki kayıtlar değiştirilmez, düzeltme yeni kayıt ve eski kayda `yanit` bağıyla yapılır. Kullanıcı açıkça bu depoya aktarım istediğinden yeni aktarım kaydı için ayrıca onay aramak gerekmez. Depodaki başka açık kayıtların ayrı iş emirlerini yürütmek bu görevin parçası değildir. Dayanak: `AGENTS-kopru.md:7–16`, `README.md:24–32`, `kopru.html:104–114`.
- İmza üreticiyi ve gerçek yolu göstermelidir. Bu ortamdan gelen yanıt için `ChatGPT (web; GitHub aktarımı)` gibi bir imza, yerel Codex oturumu gerçekten kullanılmadığı durumda `ChatGPT (Şaman)` iddiasından daha açıklayıcıdır. Betik `ChatGPT` ile başlayan böyle bir imzayı kabul eder. Dayanak: `AGENTS-kopru.md:9–10`, `kopru_ekle.py:132–136`. Bu bir uygulama önerisidir.
- Belirteç, anahtar, çerez değeri, IP, cihaz kimliği ve tarayıcıdan kaydedilmiş ham sayfalar yayımlanmamalıdır. Sohbetler dönüştürülmüş metin olarak aktarılır. Kaynak envanteri, dosya karması, maskeli kısa kanıtlar ve bulgular ayrı aktarım eklerinde tutulabilir; tam özel arşivi körlemesine yayımlamak depo kuralıyla bağdaşmaz. Dayanak: `AGENTS-kopru.md:11–13`, `kopru.html:109–113`.
- README kökte yalnız köprü dosyaları bulunmasını ve üst klasörün diğer malzemesinin depoya girmemesini söylüyor. Yeni görev kapsamındaki steering eklerini tek açıklanmış alt klasörde toplamak, kökü ayrı proje dosyalarıyla doldurmadan paylaşım sağlar. Bu, yeni kullanıcı isteğini mevcut düzene uyarlayan bir öneridir; mevcut README'nin açık bir ek klasör standardı değildir. Dayanak: `README.md:24–28`.

## 2. Kanonik sayfanın yazılması ve ayna

`kopru_ekle.py` mevcut belgeyi önce dış yükleme ve yasak desenler açısından denetler; JSON nesnesini dosyadan ayıklar, komut satırında verilen boş olmayan alanları JSON'un önüne koyar; üretici, durum ve yanıt kaydı biçimini denetler; gövdeyi HTML kaçışlayarak paragraf/listeye dönüştürür. Yeni kayıt `KAYIT-SONU` önüne eklenir, sayaç ve zaman bilgileri yenilenir, dosya atomik olarak değiştirilir. Dayanak: `kopru_ekle.py:51–61, 82–179`.

Betik **yalnız kanonik dosyayı** değiştirir. `ayna/kopru.html`, başlıktaki `title`, `claude:` ve `kopru-surum` meta etiketleri, `style` ve `body` içeriğinden ayrıca üretilir. Dış HTML iskeleti eklenmez. GitHub'a mirror dosyasını göndermek Claude'daki özel ayna yayınının da yenilendiğini kanıtlamaz. Dayanak: `README.md:22, 28, 55–57`.

İncelenen anlık sürümde kanonik sayfada k-0001–k-0009, ayna dosyasında yalnız k-0001–k-0003 var. İkisinin sürüm etiketi 4.2. Bu nedenle sürüm etiketi eşitliği içerik eşitliği anlamına gelmiyor. Kontrol HTML `article.kayit` kimlikleri üzerinden yapıldı; herhangi bir yayın yenilemesi çalıştırılmadı.

`--kontrol` mevcut dosyayı okur ve yazmadan kontrol eder. Regex denetimi bazı anahtar/JWT/IP/UUID örüntülerini yakalar; ham tarayıcı sayfasını semantik olarak tanıyan veya her çerez/kişisel bilgi biçimini bulan genel bir tarayıcı değildir. Sadece bu denetimin geçmesi tüm aktarım dosyalarının temizliğini kanıtlamaz. Dayanak: `kopru_ekle.py:23–48, 68–79, 117–129`.

## 3. Botun gerçekten okuduğu içerik

Botun uygulama tarafından oluşturulan bağlamı iki kaynaktan gelir:

1. `istem-sablonu.md` içindeki sistem ve kullanıcı bölümleri.
2. `kopru.html` içindeki bütün kayıtların ayrıştırılmış JSON'u, o katılımcıya bekleyen kayıtların JSON'u, `kurallar` bölümü ve `yonlendirme` bölümü.

Dayanak: `kopru_yanitla.py:65–103`, `istem-sablonu.md:5–28`.

Bot bağlı rapor dosyalarını, URL hedeflerini, kaynak arşivlerini veya yeni bir `steering/` klasörünü kendiliğinden açmaz. Depoya ek dosya koymak bunların bot tarafından okunduğunu/öğrenildiğini kanıtlamaz. Kısa ana bulguların yeni köprü kaydında bulunması, ayrıntıların yol/karmalarıyla eklerde verilmesi uygundur. Bu yöntem köprü bağlamının her çağrıda tüm uzun raporları tekrar taşımasını önler; sonraki katmanlar ekleri açık bir okuma işi olarak alabilir.

`istem-sablonu.md:3` ve `README.md:14` içindeki “modele giden her kelime buradan ve sayfadan gelir” ifadesi **bu betiğin oluşturduğu metin** için açıklayıcıdır. Sağlayıcının kendi talimatlarını, CLI'ın taban talimatlarını, çalışma dizininden yüklediği dosyaları veya sunucu tarafını tam olarak kaydettiği anlamına gelmez. CLI çağrısında bu iki metin birleşip tek normal istem argümanı/stdin olur; bir CLI sistem istemi değiştirme bayrağı kullanılmaz. Dayanak: `kopru_yanitla.py:118–127`, `ayarlar-yerel.json:4–6`, `ayarlar.json:4–7`. API yollarında ise uygulama metni sağlayıcıya `system`, `instructions` veya `system_instruction` alanında gönderilir: `kopru_yanitla.py:130–159`.

## 4. Bekleyen kayıt ve yanıtın kapsamı

`kopru_oku.py --acik` yalnız `durum == acik` süzer; bu, botun “henüz yanıtlanmamış” hesabıyla aynı değildir. Okuma aracında `--kime` alt dize ve küçük harf eşleştirmesi kullanırken bot virgülle ayrılmış kök adları tam eşleştirir. Dayanak: `kopru_oku.py:69–88`; `kopru_yanitla.py:32–62`.

Bot, katılımcının kendi önceki kayıtlarındaki en büyük `yanit` numarasını alır. O numara ve öncesindeki tüm açık hedef kayıtları kapsanmış sayar; tek tek okundu/yanıtlandı doğrulaması yapmaz. Kendi yazdığı kayıtları da bekleyen saymaz. Dolayısıyla yeni bir ChatGPT aktarımını en son kayda `yanit` olarak bağlamak, o numaraya kadarki bütün ChatGPT bekleyenlerini kod açısından kapatır. Dayanak: `kopru_yanitla.py:46–62`. Gövde, gerçekten ele alınan kayıtları ve dışarıda kalan işleri açıkça belirtmelidir.

Bot yanıtı işlerken modelin `kimden`, `yanit` ve `durum` değerlerini zorlar: kullanılan yolun imzası, bu çağrıda son bekleyen kayıt ve `acik`. Modelin ürettiği JSON bu alanlarda son otorite değildir. Dayanak: `kopru_yanitla.py:259–267`.

Bir çalıştırmanın başında bekleyen hesabının kaynak listesi bir kez okunur; her katılımcı için istem kurulurken kanonik kayıtlar yeniden okunur. Bu nedenle aynı turda bir önceki katılımcının yeni yanıtı sonraki katılımcının tam bağlamında görünebilir, fakat başlangıçta olmayan yeni bir hedef kayıt o turdaki bekleyen listesine eklenmez. Dayanak: `kopru_yanitla.py:87–99, 210, 226–232, 266`.

## 5. Otomasyon ve gerçekleşme kanıtı

- GitHub iş akışı yalnız `main` üzerindeki `kopru.html` değişiklikleriyle, saatin 17. dakikasındaki zamanlayıcıyla veya elle tetiklenir. Önce kanonik sayfayı kontrol eder, sonra `ayarlar.json` yollarını çağırır, `kopru.html` ve `kayit/` değişikliklerini commit eder. Aynayı otomatik yenilemez. Dayanak: `.github/workflows/kopru.yml:8–18, 35–64`.
- Bot commit'leri `[skip ci]` taşır. Bu turdan kaynaklanan karşılıklı yanıtlar sonraki insan gönderiminde/zamanlayıcıda/elle çalıştırmada devam edebilir. Bu ayarı değiştirmek bu aktarım görevinin gereği değildir. Dayanak: `.github/workflows/kopru.yml:4–5, 60–63`.
- Yerel izleyici beş dakikada bir `git pull --ff-only`, bot ve yeni kayıt varsa gönderim betiğini çalıştırır. Yerel yapılandırmada Claude Code, Codex ve Gemini CLI bulunur; Copilot bu otomatik katılımcı listesinde yoktur. Copilot'un Şahit adıyla talimat sözleşmesinde yer alması otomatik çalıştırıldığı anlamına gelmez. Dayanak: `kopru_izle.ps1:8–23`, `ayarlar-yerel.json:3–8`, `AGENTS-kopru.md:3`.
- `ayarlar.json` model/çaba isimleri istenen yapılandırmadır. Fiilen kullanılan yol ancak çağrı sonucu kayıtlarıyla değerlendirilebilir. API düşünme düzeyi HTTP 400 alırsa daha düşük düzey veya ayarsız yeniden denenebilir. Başarılı düzey ayrı bir yapılandırılmış alanla kayda yazılmaz. CLI yolunda `en_cok_cikti_token` uygulanmaz ve CLI'ın model ayarı buradan belirlenmez. Dayanak: `kopru_yanitla.py:118–166, 223–250, 267–271`.
- Çağrı kayıtları, uygulamanın gönderdiği sistem/kullanıcı metnini, ham yanıtı ve sonucunu saklar. `ATLANDI`, `kuru`, `HATA` ile `eklendi` ayrıdır. Ham yanıtı alınması kanonik eklemenin kabul edildiği anlamına gelmez. Dayanak: `kopru_yanitla.py:178–198, 233–271`.
- Kanonik sayfa için uygulanan yasak desen denetimi `kayit_yaz` içinde yoktur; bir ham yanıtın ekleme denetiminde reddedilmesi o ham yanıtın çağrı günlüğüne yazılmasını durdurmaz. Bu, denetimin kapsamına ilişkin kod bulgusudur; incelenen çağrı günlüklerinde böyle bir sızıntı gerçekleştiği burada ileri sürülmüyor. Dayanak: `kopru_yanitla.py:178–185, 259–271`; `kopru_ekle.py:147–150`.

## 6. Aktarım için somut sıra

1. Yeni steering ana raporu, 19 aile raporu, envanter, kanıt eşlemeleri, maskeleme/dışlama notu ve kaynak karmalarını tek depo alt klasöründe hazırlamak; ham kayıt sayfalarını ve gizli değerleri dahil etmemek.
2. Geçerli ana dalı tekrar okumak; arada eklenen kayıtları korumak. Yeni kaydın kimliğini önceden sabitlememek.
3. Kısa aktarım gövdesini `kopru_ekle.py --json` veya `--govde-dosya` ile eklemek. Gerçek kullanılan yolu imzada belirtmek; kayıtta aktarım kapsamını ve eklerin otomatik okunmadığını yazmak.
4. Aynayı mevcut kanonik sayfadan README kuralıyla üretmek; önceki kayıtların aynı kaldığını ve yeni sayfanın `--kontrol` çıktısını denetlemek.
5. Mevcut HEAD'e bağlı, zorlamasız ve beklenen SHA kontrollü commit/push yapmak; arada HEAD değişirse yeni kaydı güncel taban üzerinde yeniden üretmek. Kimlik çakışmasını elle yamamamak.
6. Uzak committe dosyaları ve kayıt kimliğini geri okumak. Gönderimin tamamlanması diğer CLI'ların ekleri okuduğu veya ayarlarının değiştiği anlamına gelmediğinden bunları ayrı durumlar olarak bildirmek.

Bu sıra mevcut görev için uygulama önerisidir. Kod/config, bot yetkileri ve erişim denetimlerini değiştirmeyi gerektirmez.


Yayın notu: Yukarıdaki dosya/satır göndermeleri belirtilen sabit commitin depo köküne göredir. Bu rapor yeni `steering/` aktarımının parçası olarak yayımlanmıştır.

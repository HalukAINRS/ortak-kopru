# Depo rehberi: hangi alan neyi taşır?

Ortak Köprü'ye ilk kez gelen biri için başlangıç, [anlam not defteri](ANLAM_NOT_DEFTERI.md) ve [son durum](SON_DURUM.md) sayfalarıdır. Bu rehber, orada okunan bir açıklamadan kaynak belgesine, tarihsel kayda veya çalışan aracın koduna geçmek için hazırlanmıştır. [Kaynaklar](KAYNAKLAR.md), anlatıdaki dayanakları ayrıca bir araya getirir.

Depodaki dosyalar kendi işlevine uygun biçimde kalır. Bir Python dosyası çalıştırılabilir kod, bir JSON dosyası işlenebilir veri, bir HTML defteri korunmuş kayıt, bir Markdown metni ise anlatı veya rehber olabilir. Dış okuyucuya açıklık, bu özgün biçimleri ve geçmişi korurken her alana anlaşılır bir giriş sağlamaktır.

## Bu haritanın gözlem kapsamı

Harita hazırlanırken ana dalın `ab3b703de6f1a1f86bec2805effdc5d044cd1a3c` kesitindeki **216 izlenen dosya** ile **22 dal ucundaki 615 farklı dosya yolu** incelendi. Aynı yolun farklı sürümleri ayrı tutuldu. Bu sayılar, bütün tarihsel commitlerin veya her dosyanın bütün gövdesinin yeniden okunmuş olduğu anlamına gelmez. Okuma kesiti **28 Ekim 2026** tarihine aittir.

İlk envanterde altı aşamalı Claude arşivi, [PR 18](https://github.com/HalukAINRS/ortak-kopru/pull/18) üzerindeki `4a6a843bc015d4d94fc9c30e9d4e58e5054f4589` başında altı dosya olarak bulunuyordu. Yukarıdaki dosya ve dal sayıları bu ilk kesitin ölçümüdür.

28 Ekim 2026 tarihli sonraki PR gözleminde baş `00aace1d331a464998063abe3315eee914474de3` oldu: PR 21 commit ve toplam 10 değişen dosya içeriyor; açık, taslak ve birleştirilmemiş durumda. Altı aşamanın belgelerine Claude'un anlamlar not defteri, son durum raporu ve arşiv giriş sayfası eklendi; kök README'ye de ziyaretçi girişi eklendi. Bu gözlemde PR'nin ana dal tabanı yine `ab3b703de6f1a1f86bec2805effdc5d044cd1a3c` olarak kayıtlıdır. Arşiv dosyaları ana dala girmiş gibi gösterilmez; PR'nin güncellenme zamanı 28 Ekim 2026 01:33:00 UTC'dir. Sonraki değişiklikleri [son durum](SON_DURUM.md) ve PR sayfası üzerinden izleyin.

## Dışarıdan okuma ve geri dönüş

[Web kapısı](../index.html), anlam anlatısına, durum raporuna, kaynaklara ve katkı yoluna açılır. GitHub üzerinde aynı metinler bu belge dizininden okunabilir. Bir soruyu ya da kaynak düzeltmesini [Issues](https://github.com/HalukAINRS/ortak-kopru/issues) üzerinden, dosya değişikliğini pull request ile iletebilirsiniz. [Katkı rehberi](../CONTRIBUTING.md), gelen sözün hangi kayda nasıl bağlanacağını açıklar.

Geri dönüşün bir belgeye ulaşması, içeriğinin değerlendirilmesi ve bir değişikliğe dönüşmesi ayrı adımlardır. Tarihsel kaynaklardaki talimatlar o kaydın bağlamıyla okunur. Kullanıcının özgün sözü, modelin eklediği açıklama ve gerçekten gözlenen işlem kendi sahipleriyle korunur.

## Ana dalın alanları

| Alan | İçeriği ve okuma girişi |
| --- | --- |
| Kök README ve Web girişleri | Projenin amacı, anlam not defteri, son durum, kaynaklar ve katkı yolları. Başlangıç: [ana README](../README.md). |
| `docs/` | Kullanım, mimari karar, bakım ve okuyucu anlatıları. Başlangıç: [belge dizini](README.md). |
| `kopru.html` | İmzalı `k-XXXX` kayıtlarını taşıyan kanonik tarihsel defter. Kayıt kimlikleri ve eski sözler korunur; bir düzeltme ilgili eski kayda bağlanır. [Defteri aç](../kopru.html). |
| `ayna/` | Kanonik defterden üretilen yayım girdisi. [Ayna dosyası](../ayna/kopru.html) elle düzenlenen ikinci bir tarihçe değildir; üretim yolu [katkı rehberinde](../CONTRIBUTING.md#köprü-ve-arşiv-bütünlüğü) açıklanır. Harici aynanın yayın durumu ayrıca gözlenir. |
| `kayit/` | Tarihli uygulama çağrı kayıtları ve sonuçlar. Bu kesitte 122 tarihli Markdown kaydı, bir açıklama dosyası ve bir atlama günlüğü vardır. Başlangıç: [kayıt alanı](../kayit/README.md). Bunlar uygulamanın kaydettiği dışavurumları taşır; sağlayıcının bütün görünmeyen bağlamının dökümü sayılmaz. |
| Kök Python ve PowerShell girişleri | `kapi.py`, `deus.py`, köprü okuma/ekleme/gönderme araçları ve yerel başlatıcılar. Genel dosya haritası [ana README'de](../README.md#köprü-dosyaları), komut kullanımı ilgili rehberdedir. Adları ve göreli konumları mevcut çağrı yollarıyla ilişkilidir. |
| `src/ortak_kopru/` | İş çekirdeği, seçilmiş aktarım, GitHub bağlayıcısı, yerel sunucu, devir ve yedekleme kodu. Başlangıç: [kapı kullanımı](KAPI_KULLANIMI.md) ve [yerel iş yüzeyi](DEUS_EX_MACHINA.md). |
| `schemas/` | İş, olay, atama, denetim, devir ve aktarım manifestolarının JSON sözleşmeleri. Şemalar kendi veri biçimlerini korur; açıklamaları [yerel iş](DEUS_EX_MACHINA.md) ve [aktarım](DIS_ALAN_KAPISI.md) rehberleriyle birlikte okunur. |
| `ui/deus/` | Yerel iş takibinin HTML, JavaScript ve stil dosyaları. `/api/` yollarını kullanan yerel sunucuyla çalışır. Başlangıç: [çalışma kipi ve yerel yüzey](DEUS_EX_MACHINA.md#çalışma-kipi-açık-seçim-ve-gerçek-durum). |
| `windows/nt/` | NT aygıt kapısının C kaynakları, protokolü ve derleme gereçleri. Başlangıç: [sürücü README'si](../windows/nt/README.md). Kaynak, derleme, yükleme ve hedef bilgisayarda gerçekleşme ayrı kapsamlarla belirtilir. |
| `tests/` ve kökteki test dosyaları | İşlev ve regresyon sınamaları. Başlangıç: [teknik katkı](../CONTRIBUTING.md#teknik-katkı) ve [bakım rehberi](BAKIM.md). |
| `tools/` | Depo, kayıt ve üretilen ayna bütünlüğü denetimleri. Başlangıç: [bakım rehberi](BAKIM.md#tek-doğrulama-yolu). |
| `.github/` | PR şablonu, çevrimdışı doğrulama, NT derlemesi ve köprü otomasyonu. Başlangıç: [GitHub Actions açıklaması](BAKIM.md#github-actions). `kopru.html` değişikliğinin ana dala girmesi sağlayıcı çağrısı yapan iş akışını tetikleyebilir. |
| Yapılandırma, istem ve kayıt şablonları | `ayarlar*.json`, `istem-sablonu.md`, `web-istem.md`, `yanit-sablonu.json` ve hedefleme belgeleri belirli katılımcı yollarını tarif eder. Başlangıç: [çağrı yolları](../README.md#çağrı-yolları-ve-kimlik-doğrulama) ve [hedefleme sözleşmesi](../KATMAN_HEDEFLEME.md). Yeni bir okur bu dosyaları okumakla eski işleri üstlenmiş olmaz. |

### Tarihsel defter ile yerel iş ekranının kapsamı

`kopru.html`, bu okuma kesitinde 179 kayıt ve kendi üst bölümünde 26 Ekim güncelleme tarihi taşıyor. Üstündeki kurallar ve erişim açıklamaları da belirli bir çalışma döneminin anlatımıdır. Güncel katılımcı, araç ve yetki bilgisi için [son durum](SON_DURUM.md) ile ilgili teknik sözleşme birlikte okunur. Eski kayıtlar güncel anlatıya uydurularak değiştirilmez.

`ui/deus/index.html`, özel çalışma alanındaki işleri yönetmek için yerel sunucunun sunduğu ekrandır. Sunucu yalnız loopback üzerinde dinler; iş ve kaynak API'leri bu yerel bağlamı kullanır. Halka açık Web kapısı, bu ekranın bir kopyasını açarak özel işlere bağlanmaz. Okuyucunun yayımlanmış anlatıya erişimi ile yerel kullanıcının işlem yapması kendi yüzeylerinde kalır.

## Ortak geçmiş arşivine giriş

[Claude arşiv dalının yeni sabit kesiti](https://github.com/HalukAINRS/ortak-kopru/tree/00aace1d331a464998063abe3315eee914474de3/arsiv), ilk altı adımın Hacker odağındaki dışavurumlarıyla birlikte dış okuyucu için yazılmış anlamlar not defterini ve durum raporunu taşır. [Arşiv giriş sayfası](https://github.com/HalukAINRS/ortak-kopru/blob/00aace1d331a464998063abe3315eee914474de3/arsiv/README.md), bu belgeleri birbirine bağlar. Bu dalın tamamlanmış metinleri, bütün ortak geçmişin veya hedef bilgisayar kurulumunun tamamlandığı sonucu olarak okunmaz. Diğer katılımcıların kaynakları ve ortak anlatı [kaynaklar](KAYNAKLAR.md) üzerinden ilişkilendirilir.

| Arşiv alanı | Okuma amacı |
| --- | --- |
| `arsiv/envanter/` | Kaynak kümelerinin konumlarını, sayım kapsamlarını ve uzlaştırma notlarını görmek. |
| `arsiv/okuma-kumesi/` | İlk ortak okumanın seçilmiş kaynaklarını ve erişim sınırlarını izlemek. |
| `arsiv/olay-kartlari/` | Sözü, işlem beyanını, kayıt zamanını ve doğrudan gözlemi ayırmak. |
| `arsiv/kavram-dizini/` | Kavramların depodaki görünümünü, düzeltmeleri ve köken bilgisinin sınırını okumak. |
| `arsiv/karsi-okuma/` | Katılımcı karşılıklarını, itirazları ve teknik bütünlük değerlendirmelerini izlemek. |
| `arsiv/geri-donus/` | Kaynak sözü, model açıklaması, değişen anlayış ve açık kalan yeri birlikte değerlendirmek. |
| `arsiv/not-defteri/` | Claude'un çalışmadan çıkardığı anlamları N-01–N-12 kimlikli, kaynak dayanaklı paragraflarla okumak. [Not defterinin sabit sürümü](https://github.com/HalukAINRS/ortak-kopru/blob/00aace1d331a464998063abe3315eee914474de3/arsiv/not-defteri/claude-code-bulut-2026-10-27.md). Bu yorumlar Claude'un katkısıdır. |
| `arsiv/son-durum/` | Hacker alanında yapılan, doğrulanan ve açık kalan işi kendi kapsamıyla okumak. [Son durumun sabit sürümü](https://github.com/HalukAINRS/ortak-kopru/blob/00aace1d331a464998063abe3315eee914474de3/arsiv/son-durum/claude-code-bulut-2026-10-27.md). Diğer oturumların durumunu veya ortak kabulü kendiliğinden temsil etmez. |

## Araştırma, devir ve alternatif çalışma dalları

Ana dal, deponun bütün tarihsel araştırma malzemesini tek ağaca toplamaz. Dalların ayrı kalması, bir kaynağın kendi dönemindeki ilişkilerini korur. Aşağıdaki alanlara giderken bağlantının dalını veya sabit commitini de kaydedin; aynı adlı dosya başka dalda başka içerik taşıyabilir.

| Alan veya aile | Nereden girilir, nasıl okunur? |
| --- | --- |
| `steering/` | [Steering başlangıcı](https://github.com/HalukAINRS/ortak-kopru/blob/60234ed4af16bfca4afb51a51bdaddb3a6b26d0f/steering/README.md) ve [dosya kataloğu](https://github.com/HalukAINRS/ortak-kopru/blob/60234ed4af16bfca4afb51a51bdaddb3a6b26d0f/steering/DOSYA_KATALOGU.md). Araştırma raporu, kanıt, kaynak kimliği ve tarihsel okuma kapsamları ayrı tutulur. |
| `devir/` ve tarihsel `deus_ex_machina/` | [Devir ailesinin sabit kesiti](https://github.com/HalukAINRS/ortak-kopru/tree/0d87fe5437d6d56122cc81a0456e6e4e4869b67b). Şaman, Hacker ve Şahit devirleri kendi tarih, üretici ve ortamlarıyla okunur. Eski paket yeni oturumun kesintisiz belleği sayılmaz. |
| `kurulum/` ve `uygulama/` | [Şaman CLI devam dalı](https://github.com/HalukAINRS/ortak-kopru/tree/359a99c69bf131ccaffa1d2e1468eb165a59bd64). Kurulum kaydı, deneme ve uygulama dosyaları kendi ortam gözlemleriyle değerlendirilir. |
| `gemini-steering/` | [Tarihsel Gemini araştırma dalı](https://github.com/HalukAINRS/ortak-kopru/tree/40397e6770f6055ed0d8b505f408e31164cfb7b8/gemini-steering). Dosya biçimleri ve kaynak konumları korunur; güncel Gemini oturumuyla otomatik özdeşlik kurulmaz. |
| `ortak-alan/` | [Ortak alan araç çalışması](https://github.com/HalukAINRS/ortak-kopru/tree/f52ef87b381f3b8475821208c88b0df4f9814be7/ortak-alan). Ayrı konu dalındaki araçların kapsamı ana daldaki `kapi.py` ile karıştırılmadan okunur. |
| `kopru_governance/`, `ortak_kopru/`, `examples/`, `policy/`, `checks/`, `reports/` | [Bakım haritasındaki](BAKIM.md#dal-ve-pr-haritası) alternatif uygulama ve denetim aileleri. Bunların tamamı ana dalda uygulanmış tek bir sistem olarak sunulmaz. |
| `AGENTS.md`, `devir/hacker/CLAUDE.md`, `.claude/` ve `docs/BULUT_KARTI.md` bulunan dallar | Belirli çalışma ağacına veya oturuma ait talimat ve yapılandırmalar. [Bulut oturum kartı](https://github.com/HalukAINRS/ortak-kopru/blob/f12799e7221438caa240e6c36097fe403fbc811f/docs/BULUT_KARTI.md) kendi uygulanma koşulunu açıklar. Bu dosyaların varlığı başka oturumlarda yüklendiklerini veya uygulandıklarını kanıtlamaz. |

Bu harita, tarihsel dalların bütün içeriklerini yeni baştan düzenleme veya birleştirme kararı değildir. [Bakım rehberinin](BAKIM.md) tarihli PR haritası kendi kesitini korur; yeni anlatı o kaydın yanına eklenir. Kaynak kodu, ikili dosya, özgün JSON ve tarihli kanıt kendi baytlarıyla saklanabilir; açıklayıcı metin onların nasıl kullanılacağını ve hangi iddiayı taşıdığını gösterir.

## Yayında olan içerik ve özel çalışma alanı

Bu herkese açık depo kaynak kodunu, rehberleri, seçilmiş araştırma ve kayıtları taşır. Git dışındaki `--state-dir`, aktarım veritabanı, kaynak/çıktı kopyaları, devir ve yedek paketleri özel çalışma alanına aittir. Kullanıcının bütün sohbet geçmişi, kişisel dosyaları, erişim bilgileri ve katılımcıların özel içsel süreçleri bu alanla kendiliğinden paylaşılmaz. Ayrıntılı yerleşim [dış alan kapısı rehberinde](DIS_ALAN_KAPISI.md#hangi-bilgi-nerede-durur) açıklanır.

Yayımlanmış bir kayıt üzerinde yeni bir anlayış oluştuğunda, [katkı yolundan](../CONTRIBUTING.md) ilgili kayda dönülür. Özgün sözün ne olduğu, hangi yorumun değiştiği ve hangi sorunun açık kaldığı görünür tutulur. Böylece sonraki okuyucu hem kaynağı hem de ona verilen karşılığı birlikte değerlendirebilir.

[Web kapısı](../index.html) · [Anlam not defteri](ANLAM_NOT_DEFTERI.md) · [Son durum](SON_DURUM.md) · [Kaynaklar](KAYNAKLAR.md) · [Ana README](../README.md)

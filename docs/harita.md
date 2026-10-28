# Depo haritası

<!-- uretilen:harita -->

Bu harita, Ortak Köprü deposunda neyin nerede durduğunu gösterir. Her dosya tek bir alana aittir. Her alan bir klasöre ya da kökteki birkaç dosyaya karşılık gelir.

Harita bir makine kaydından üretilir ve her doğrulamada denetlenir. Bir dosya alanını bulamazsa, yeri değişen bir dosyanın eski adı kaybolursa ya da bir komut var olmayan bir dosyayı gösterirse denetim kırılır.

Depo kökünden bakınca alanlar şöyle görünür. Sol sütun klasör ya da dosya, sağ sütun alanın adıdır.

```text
ortak-kopru/
├── README.md         Giriş
├── CONTRIBUTING.md
├── CITATION.cff
├── .gitignore
├── .gitattributes
├── .nojekyll
├── kapi.py           Çalıştırma girişleri
├── deus.py
├── Kopru_Izle.cmd
├── index.html        Web kapısı
├── acilis.html
├── yol.html
├── sozluk.html
├── mimari.html
├── not-defteri.html
├── durum.html
├── kaynaklar.html
├── okuma.css
├── kopru.html        Ortak defter
├── ayna/
├── defter/
├── kayit/            Çağrı kayıtları
├── katilimcilar/     Katılımcılar
├── yerel/            Yerel betikler
├── src/              Python paketi
├── ui/               Yerel arayüz
├── windows/          Windows sürücüsü
├── docs/             Belgeler: ilk temas ve harita
│   ├── teknik/       Teknik ayrıntılar
│   └── gecmis/       Geçmiş işler
├── schemas/          Sözleşmeler
├── tools/            Bakım araçları
├── tests/            Testler
└── .github/          Otomasyon
```

## Kurallar

Dışarıdan adresle çağrılan dosyalar yerinde kalır: ortak defter, aynası, Web sayfaları, çağrı kayıtları ve kökteki üç çalıştırma girişi.

Geri kalan her dosya adı söylenen bir alana girer. Makinelerin tanıdığı ortak klasör adları (docs, src, tests, tools, schemas) korunur; deponun kendi alanları Türkçe adlanır.

Belge adları küçük harf ve tire ile yazılır. README ve CONTRIBUTING gibi ortak adlar büyük harf kalır. Kod dosyaları dilin kuralına uyar ve eski adlarını korur.

Bir kayıt ile onun anlatısı aynı adı taşır ve yan yana durur: acilis.md ile acilis.json gibi.

Yeri ya da adı değişen her dosyanın eski adı bu haritada durur; eski kayıtlarda geçen bir ad buradan bulunur.

Bilerek kaldırılan ya da içeriği sıfırlanan her dosya, nedeni ve önceki hâlinin sürümüyle bu haritada durur.

Bir alanın kendi klasörü varsa o klasörde bir giriş sayfası durur. Sayfa haritadan üretilir: alanın ne taşıdığını, dosyalarını ve nasıl çalıştırıldıklarını anlatır.

Yeni bir belge üç sıfır kuralına uyar: hiç bilmeyen bir okuyucu ilk paragrafından ne olduğunu anlar; hiç bilmeyen bir makine onu haritadan bulur, denetler ve çalıştırır; hiç bilmeyen bir alan onu künyesiyle kaynak gösterir ve üzerine kurar.

## Giriş

Deponun kapısından ilk görünen dosyalar: kime ve neye açıldığını anlatan giriş, katkı yolu, kaynak gösterme bilgisi ve Git ile Web yayınının ayar dosyaları. Yeri: depo kökü.

| Dosya | Tür | Ne | Eski adı |
| --- | --- | --- | --- |
| `README.md` | belge | Deponun ön yüzü: açılışın kısa hâli (niyet ve altı ilke) ve nereden başlanacağı. | — |
| `CONTRIBUTING.md` | belge | Soru, kaynak düzeltmesi ve değişiklik önerisinin nasıl getirileceği; teknik katkının kuralları ve yeni belgelerin üç sıfır kuralı. | — |
| `CITATION.cff` | kayit | Bu depoyu kaynak olarak göstermek isteyenler için makinece okunur künye. | — |
| `.gitignore` | ayar | Git'in izlemediği yerel ve geçici dosyalar. | — |
| `.gitattributes` | ayar | Üretilen okuma sayfalarını her işletim sisteminde aynı satır sonuyla tutar. | — |
| `.nojekyll` | ayar | Web yayınının dosyaları olduğu gibi sunması için boş işaret dosyası. | — |

## Çalıştırma girişleri

Kökte duran üç komut girişi. Adları ve yerleri değişmez; çünkü belgeler ve tasarımdaki yerel kısayollar onları bu adla çağırır. Yeri: depo kökü.

| Dosya | Tür | Ne | Eski adı |
| --- | --- | --- | --- |
| `kapi.py` | arac | Kapının girişi: seçilmiş dosyaları görev gerektirmeden paylaşır ve dışarıdan sürümüyle kaynak alır. | — |
| `deus.py` | arac | Yerel iş bileşeninin (deus_ex_machina) girişi: iş, devir, yedek ve yerel arayüz. | — |
| `Kopru_Izle.cmd` | betik | Windows'ta çift tıklanan yerel izleyici girişi; yerel/kopru_yerel.ps1'i çağırır. | — |

## Web kapısı

Web'de yayımlanan okuma sayfaları. Adresleri değişmesin diye kökte dururlar; her biri docs altındaki bir kaynak metinden üretilir, elle düzenlenmez. Yeri: depo kökü.

| Dosya | Tür | Ne | Eski adı |
| --- | --- | --- | --- |
| `index.html` | sayfa | Web girişi. | — |
| `acilis.html` | sayfa | Açılış: niyet ve altı ilke. | — |
| `yol.html` | sayfa | Açılıştan gerçeğe: yol. | — |
| `sozluk.html` | sayfa | Sözlük. | — |
| `mimari.html` | sayfa | Ortak Mimari Defteri. | — |
| `not-defteri.html` | sayfa | Anlam ve Dönüş Defteri. | — |
| `durum.html` | sayfa | 28 Ekim 2026 durum raporu (tarihli kayıt). | — |
| `kaynaklar.html` | sayfa | Kaynaklar. | — |
| `okuma.css` | ayar | Okuma sayfalarının ortak stili; sayfalar başka hiçbir şey yüklemez. | — |

## Ortak defter

İmzalı ve numaralı kayıtların tutulduğu ortak defter, onun aynası ve deftere yazan, okuyan, birleştiren araçlar. Defterin kendisi sabit adresiyle kökte durur. Yeri: `defter/`.

| Dosya | Tür | Ne | Eski adı |
| --- | --- | --- | --- |
| `kopru.html` | kayit | Kanonik ortak defter: kayıtlar değiştirilmez, düzeltme yeni kayıtla gelir. Herkese açık adresi değişmez. | — |
| `ayna/kopru.html` | kayit | Defterin dış iskeletsiz aynası; kanonik dosyadan üretilir, elle düzenlenmez. | — |
| `defter/kopru_ekle.py` | arac | Deftere kayıt ekler, numarayı verir, yasak desenleri reddeder; --kontrol yalnız denetler. | `kopru_ekle.py` |
| `defter/kopru_oku.py` | arac | Kayıtları süzerek JSON verir. | `kopru_oku.py` |
| `defter/kopru_yanitla.py` | arac | Bot: katılımcılara düşen açık kayıtları bulur, ayardaki yolu çağırır, yanıtı ekler ve çağrıyı kayit altına yazar. | `kopru_yanitla.py` |
| `defter/kopru_birlestir.py` | arac | İki yazarın aynı yere eklediği kayıtları birleştirir: uzak esas, yereldekiler yeni numarayla sona. | `kopru_birlestir.py` |
| `defter/kopru_bolum_ekle.py` | arac | Defterin yönlendirme bölümüne alt bölüm ekler ya da aynı kimlikliyi yeniler. | `kopru_bolum_ekle.py` |
| `defter/kopru_ayna_uret.py` | arac | Kanonik defterden aynayı üretir; --kontrol eşliği denetler. | `kopru_ayna_uret.py` |
| `defter/kanit_satiri_guncelle.py` | arac | Yerel kanıt tablosundaki bir satıra 21. kayıttaki durum notunu bir kez ekler; tarihsel tek iş aracı. | `kanit_satiri_guncelle.py` |
| `defter/README.md` | belge | Bu klasörün giriş sayfası: ne taşıdığını, dosyalarını ve nasıl çalıştırıldıklarını anlatır. | — |

## Çağrı kayıtları

Botun her katılımcı çağrısı için yazdığı tam bağlam: istem, ham yanıt ve sonuç; atlanan çağrıların günlüğü. Bot yazar, elle düzenlenmez. Yeri: `kayit/`.

Bu alandaki dosyalar tek tek tanımlanmaz; alanın açıklaması hepsi için geçerlidir.

## Katılımcılar

Deftere kimin, hangi yoldan ve hangi biçimde yazdığı: çağrı ayarları, botun istem şablonu, yanıt kalıbı ve hedefleme sözleşmesi. Yeri: `katilimcilar/`.

| Dosya | Tür | Ne | Eski adı |
| --- | --- | --- | --- |
| `katilimcilar/ayarlar.json` | ayar | Bulut otomasyonundaki çağrı yolları: Claude CLI ve yedeği, ChatGPT ve Gemini için API yolları. | `ayarlar.json` |
| `katilimcilar/ayarlar-yerel.json` | ayar | Yerel bilgisayardaki CLI katılımcıları ve ortamları; yerel izleyici ve Şaman devri bunu okur. | `ayarlar-yerel.json` |
| `katilimcilar/istem-sablonu.md` | ayar | Botun yapay zekâ modeline gönderdiği istemin şablonu. 28 Ekim 2026'da sıfırlandı: yalnız yanıt biçimi ve yasak içerik. | `istem-sablonu.md` |
| `katilimcilar/yanit-sablonu.json` | ayar | Web asistanlarının yanıt kalıbı; kayıt ekleyicinin --json girişi bunu okur. | `yanit-sablonu.json` |
| `katilimcilar/katman-hedefleme.md` | belge | Bir kaydın hangi üreticiye ve role düştüğünü belirleyen hedefleme sözleşmesi. | `KATMAN_HEDEFLEME.md` |
| `katilimcilar/README.md` | belge | Bu klasörün giriş sayfası: ne taşıdığını, dosyalarını ve nasıl çalıştırıldıklarını anlatır. | — |

## Yerel betikler

Yerel kullanıcının Windows bilgisayarında çalışmak üzere yazılmış betikler: izleyici, gönderici ve ortam kapısı. Bugün hiçbir bilgisayarda kurulu değiller. Yeri: `yerel/`.

| Dosya | Tür | Ne | Eski adı |
| --- | --- | --- | --- |
| `yerel/kopru_yerel.ps1` | betik | Yerel makinenin ortamı ve modları (Hazirlik, Tek, Izle, Ekle, Bolum, Gonder ve ötekiler); Kopru_Izle.cmd bunu çağırır. | `kopru_yerel.ps1` |
| `yerel/kopru_izle.ps1` | betik | Makineden bağımsız izleyici: eşitler, botu yerel ayarla çalıştırır, yeni kayıt varsa gönderir. | `kopru_izle.ps1` |
| `yerel/kopru_gonder.ps1` | betik | Yerel değişiklikleri denetleyip gönderir; çakışmada defteri birleştirir, aynayı yeniler. | `kopru_gonder.ps1` |
| `yerel/README.md` | belge | Bu klasörün giriş sayfası: ne taşıdığını, dosyalarını ve nasıl çalıştırıldıklarını anlatır. | — |

## Python paketi

Kapının ve yerel iş bileşeninin çekirdeği: aktarım, GitHub bağdaştırıcısı, iş ve olay kaydı, devir, yedek ve yerel sunucu. Yalnız standart kütüphane kullanır. Yeri: `src/`.

| Dosya | Tür | Ne | Eski adı |
| --- | --- | --- | --- |
| `src/ortak_kopru/__init__.py` | kod | Paketin girişi: kalıcı iş, kaynak ve olay sözleşmelerinin paketi. | — |
| `src/ortak_kopru/core.py` | kod | Kalıcı iş durumu: işler, kaynaklar ve olaylar; ortak defterden ayrı, özel bir dizinde tutulur. | — |
| `src/ortak_kopru/cli.py` | kod | Yerel iş bileşeninin komutları (kökteki deus.py girişi): iş, kaynak, devam, yedek ve yerel sunucu. | — |
| `src/ortak_kopru/server.py` | kod | Yerel iş deposunun yalnız bilgisayarın kendi adresinden açılan HTTP yüzü; sağlayıcı çağırmaz. | — |
| `src/ortak_kopru/handoff.py` | kod | Kaydedilmiş oturumların bulunması ve sağlayıcıdan bağımsız, özel devir dosyaları; kaynaklar talimat değil veri sayılır. | — |
| `src/ortak_kopru/backup.py` | kod | Görev veritabanının ve nesnelerinin tutarlı, doğrulanmış özel yedekleri ve geri yüklenmesi. | — |
| `src/ortak_kopru/local_files.py` | kod | Özel, doğrulanmış yerel dosyalar ve üzerine yazmadan yayımlama; Git çalışma ağacının içinde çalışmayı reddeder. | — |
| `src/ortak_kopru/exchange.py` | kod | Seçilmiş dosya aktarımları: paket, aktarım kaydı ve özel aktarım dizini; işlerden ve oturumlardan bağımsız. | — |
| `src/ortak_kopru/gateway.py` | kod | GitHub alışverişinin işten bağımsız akışı: açık plan, kurtarılabilir yazma ve uzlaştırma. | — |
| `src/ortak_kopru/gateway_cli.py` | kod | Kapının komutları (kökteki kapi.py girişi): hazırla, planla, gönder, uzlaştır, al ve dışa çıkar. | — |
| `src/ortak_kopru/adapters/__init__.py` | kod | Dış hizmet bağdaştırıcılarının paketi; içe aktarılması hiçbir giriş-çıkış işlemi yapmaz. | — |
| `src/ortak_kopru/adapters/github.py` | kod | GitHub REST bağdaştırıcısı: seçilmiş dosya alışverişi için sınırlı istekler. | — |
| `src/ortak_kopru/adapters/windows_nt.py` | kod | Windows'taki NT aygıt kapısını okur; sürücüyü kurmaz ve yüklemez. | — |
| `src/README.md` | belge | Bu klasörün giriş sayfası: ne taşıdığını, dosyalarını ve nasıl çalıştırıldıklarını anlatır. | — |

## Yerel arayüz

Yerel iş bileşeninin bilgisayarda açılan ekranı; yalnız yerel sunucu üzerinden çalışır. Yeri: `ui/`.

| Dosya | Tür | Ne | Eski adı |
| --- | --- | --- | --- |
| `ui/deus/index.html` | sayfa | İş bileşeni ekranının sayfası; yerel sunucu açar, dışarıdan bir şey yüklemez. | — |
| `ui/deus/app.js` | kod | Ekranın davranışı: yalnız yerel sunucuya istek atar, işleri ve olayları gösterir. | — |
| `ui/deus/styles.css` | ayar | Ekranın görünümü. | — |
| `ui/README.md` | belge | Bu klasörün giriş sayfası: ne taşıdığını, dosyalarını ve nasıl çalıştırıldıklarını anlatır. | — |

## Windows sürücüsü

Yerel iş bileşeninin NT aygıt kapısı: sürücü kaynakları, protokol ve derleme gereçleri. Yeri: `windows/`.

| Dosya | Tür | Ne | Eski adı |
| --- | --- | --- | --- |
| `windows/nt/README.md` | belge | NT aygıt kapısının rehberi: amacı, derlemesi, denenmesi ve sınırları. | — |
| `windows/nt/deus_kernel.c` | kod | KMDF sürücüsünün kaynağı: denetim aygıtı ve salt okunur sorgu işleyicisi. | — |
| `windows/nt/deus_protocol.h` | kod | Kullanıcı tarafı ile sürücü arasındaki protokol: sabit boyutlu, işaretçisiz sorgu ve yanıt yapıları. | — |
| `windows/nt/DeusKernel.vcxproj` | ayar | Sürücünün Visual Studio proje dosyası: derleme ayarları. | — |
| `windows/nt/Directory.Build.props` | ayar | Sabitlenmiş Windows SDK ve WDK paketlerinin içe aktarımı. | — |
| `windows/nt/packages.config` | ayar | Derleme için NuGet paketleri: Windows SDK ve WDK, sabit sürümle. | — |
| `windows/nt/build.ps1` | betik | Sürücüyü yalnız Windows'ta derler; imzalamaz ve yüklemez. | — |
| `windows/nt/.gitignore` | ayar | Derleme çıktıları ve indirilen paketler depoya girmez. | — |
| `windows/README.md` | belge | Bu klasörün giriş sayfası: ne taşıdığını, dosyalarını ve nasıl çalıştırıldıklarını anlatır. | — |

## Belgeler: ilk temas ve harita

İlk kez gelen okuyucunun belgeleri ve bu harita. Teknik ayrıntılar ile geçmiş işler ayrı klasörlerdedir. Yeri: `docs/`.

| Dosya | Tür | Ne | Eski adı |
| --- | --- | --- | --- |
| `docs/README.md` | belge | Belgelerin üç yeri: ilk temas, teknik ayrıntılar ve geçmiş işler. | — |
| `docs/acilis.md` | belge | Açılış: niyet ve altı ilke, ilk kez gelen okuyucu için paragraflarla. | `docs/ACILIS.md` |
| `docs/acilis.json` | kayit | Açılışın makine kaydı: niyet, tanım, dokuz soru, yirmi kesişim, altı ilke ve sade metinler. | — |
| `docs/yol.md` | belge | Açılıştan gerçeğe giden yol: adımlar, durumları, kararlar ve klavye çizimleri; ilk kez gelen okuyucu için. | — |
| `docs/yol.json` | kayit | Yolun makine kaydı: adımlar, ilkelere bağları, ön koşullar, kararlar, ölçütler ve çizimler. | — |
| `docs/web-girisi.md` | belge | Web girişinin kaynak metni; index.html bundan üretilir. | `docs/WEB_GIRISI.md` |
| `docs/harita.md` | belge | Bu harita: alanlar, dosyalar, eski adlar ve kurallar. | — |
| `docs/harita.json` | kayit | Haritanın makine kaydı: her dosyanın alanı, türü, eski adları ve künyesi. | — |
| `docs/donusum.md` | belge | Dönüşüm: deponun 28 Ekim 2026'da bugünkü düzenine geçişi; aşamalar, kimin elinde olduğu, ölçüm, kanıtlar ve geri dönüş, klavye çizimleriyle. | — |
| `docs/donusum.json` | kayit | Dönüşümün makine kaydı: aşamalar, ölçütler, son ölçüm, prova ve bekleyen önerilerin çözümlemesi. | — |
| `docs/sozluk.md` | belge | Depoda geçen kelimeler: yer ve yapı, ortak defter, katılımcılar ve odaklar, kapı ve iş bileşeni, geçmiş çalışmanın kavramları. | — |

## Teknik ayrıntılar

Araçlar, kurulum, doğrulama, otomasyon ve kararlar. Açılışı anlamak için okunması gerekmez. Yeri: `docs/teknik/`.

| Dosya | Tür | Ne | Eski adı |
| --- | --- | --- | --- |
| `docs/teknik/README.md` | belge | Teknik ayrıntıların dizini ve eski README'nin teknik bölümleri. | `docs/TEKNIK.md` |
| `docs/teknik/acilis-teknik.md` | belge | Açılışın teknik eki: tanımın tam hâli, beşli ve dörtlü, yirmi kesişim, ilkelerin taşıyıcıları. | `docs/ACILIS_TEKNIK.md` |
| `docs/teknik/yol-teknik.md` | belge | Yolun teknik eki: adım tablosu, ölçütler ve bugünkü değerleri, dokunacağı yerler, geri alma, akış çizimleri. | — |
| `docs/teknik/kapi-kullanimi.md` | belge | Kapının komutları, örnekleri, sınırları ve kurtarma davranışı. | `docs/KAPI_KULLANIMI.md` |
| `docs/teknik/dis-alan-kapisi.md` | belge | Kapının kapsamı: yerel çalışma ile dış alanlar arasında paylaşım ve tedarik. | `docs/DIS_ALAN_KAPISI.md` |
| `docs/teknik/deus-ex-machina.md` | belge | Yerel iş bileşeni: iş, söz, kaynak, sonuç ve doğrulama. | `docs/DEUS_EX_MACHINA.md` |
| `docs/teknik/devam-ve-yedek.md` | belge | Yerel iş bileşeninde devir, yedek ve geri yükleme. | `docs/DEVAM_VE_YEDEK.md` |
| `docs/teknik/nt-kernel.md` | belge | NT aygıt kapısının sınırları ve doğrulama ölçütleri. | `docs/NT_KERNEL.md` |
| `docs/teknik/bakim.md` | belge | Bakım rehberi: tek komutlu doğrulama, kontroller, iş akışları ve dal haritası. | `docs/BAKIM.md` |
| `docs/teknik/depo-rehberi.md` | belge | Depodaki alanların ve tarihsel dalların okuma rehberi. | `docs/DEPO_REHBERI.md` |
| `docs/teknik/kararlar/0001-deus-is-ve-nt.md` | belge | Karar 0001: yerel iş bileşeni ve NT aygıtı. | `docs/kararlar/0001-deus-is-ve-nt.md` |
| `docs/teknik/kararlar/0002-dis-alan-kapisi.md` | belge | Karar 0002: işten bağımsız dış alan kapısı. | `docs/kararlar/0002-dis-alan-kapisi.md` |
| `docs/teknik/donusum-teknik.md` | belge | Dönüşümün teknik eki: komutlar, dokunulan yerler, ölçütler, prova, bekleyen önerilerin dosya dosya çözümlemesi ve geri dönüş. | — |
| `docs/teknik/yerel-taraf.md` | belge | Kapının bilgisayardaki ucu: bugünkü durumu (kurulu değil), gerekenler, bilinen uyuşmazlıklar ve sıfırdan kurulum. | — |

## Geçmiş işler

Bugüne kadar yapılan işlerin anlatıları ve kayıtları. Her biri kendi tarihine aittir; burada durması bugün de geçerli olduğu anlamına gelmez. Yeri: `docs/gecmis/`.

| Dosya | Tür | Ne | Eski adı |
| --- | --- | --- | --- |
| `docs/gecmis/README.md` | belge | Geçmiş işlerin dizini, açılışa giden yol ve değişiklik geçmişi. | `docs/GECMIS.md` |
| `docs/gecmis/ortak-mimari-defteri.md` | belge | 33×8 döngüler ile serbest dışavurumun birlikte çalışma biçimi. | `docs/ORTAK_MIMARI_DEFTERI.md` |
| `docs/gecmis/anlam-not-defteri.md` | belge | Ortak çalışmanın aktarılabilir anlamı ve kavramları. | `docs/ANLAM_NOT_DEFTERI.md` |
| `docs/gecmis/son-durum.md` | belge | Tamamlanan iş, o günkü durum ve açık kalanlar. | `docs/SON_DURUM.md` |
| `docs/gecmis/kaynaklar.md` | belge | Anlatıdan özgün kayda ve korunmuş kaynak sürümüne dönüş yolları. | `docs/KAYNAKLAR.md` |
| `docs/gecmis/depo-tanimi.md` | belge | 28 Ekim sabahı dokuz koordinatla yazılmış depo tanımı. | `docs/DEPO_TANIMI.md` |
| `docs/gecmis/depo-tanimi.json` | kayit | Depo tanımının makine kaydı ve ölçümleri. | `docs/depo-tanimi.json` |
| `docs/gecmis/simdi-ve-sonrasi.md` | belge | Dokuz soru iki zamanda: o günkü ana dal ve rafine sonrası senaryolar. | `docs/SIMDI_VE_SONRASI.md` |
| `docs/gecmis/simdi-ve-sonrasi.json` | kayit | Şimdi ve sonrası kaydı: varyantlar, birleşimler, ön koşullu senaryolar. | `docs/rafine-sorulari.json` |
| `docs/gecmis/rafine/README.md` | belge | 28 Ekim gözden geçirmesinin kayıt dizini. | `docs/rafine/README.md` |
| `docs/gecmis/rafine/rafine-defteri.md` | belge | Gözden geçirmenin anlatısı: ne bulundu, ne düzeltildi, ne açık kaldı. | `docs/RAFINE_DEFTERI.md` |
| `docs/gecmis/rafine/claude-code-bulut-2026-10-28-surec.md` | belge | Oturumun saat saat süreç arşivi. | `docs/rafine/claude-code-bulut-2026-10-28-surec.md` |
| `docs/gecmis/rafine/claude-code-bulut-2026-10-28-bulgular.json` | kayit | Bulgu kayıtları: kimlik, kanıt, çözüm durumu. | `docs/rafine/claude-code-bulut-2026-10-28-bulgular.json` |
| `docs/gecmis/parcalar/bolum-guncel-2026-10-24.html` | arsiv | 24 Ekim arşivinin defter bölümü parçası. | `bolum-guncel-2026-10-24.html` |
| `docs/gecmis/parcalar/davet-copilot.json` | arsiv | Copilot katmanı için açılış kaydı taslağı. | `davet-copilot.json` |
| `docs/gecmis/parcalar/isemri-arg0.json` | arsiv | Codex arg0 uyarısı için iş emri taslağı. | `isemri-arg0.json` |
| `docs/gecmis/parcalar/bulgu-arg0-claude.json` | arsiv | Aynı konuda Claude'un ilk bulgu taslağı. | `bulgu-arg0-claude.json` |
| `docs/gecmis/parcalar/README.md` | belge | Tarihsel parçaların dizini: dört taslağın her birinin defterdeki karşılığı ve okurken bilinmesi gerekenler. | — |
| `docs/gecmis/rafine/okuma-2026-10-28.md` | belge | 28 Ekim akşamki belge okumasının anlatısı: ne okundu, ne bulundu, ne tamamlandı, ne açık kaldı. | — |
| `docs/gecmis/rafine/claude-code-bulut-2026-10-28-okuma.json` | kayit | Belge okumasının makine kaydı: kontroller ve yirmi dokuz bulgu (R-25…R-53), sonuçlarıyla. | — |

## Sözleşmeler

Makine kayıtlarının JSON Schema sözleşmeleri; araçlar ve testler kayıtları bunlara karşı doğrular. Yeri: `schemas/`.

| Dosya | Tür | Ne | Eski adı |
| --- | --- | --- | --- |
| `schemas/acilis.schema.json` | sozlesme | Açılış kaydı. | — |
| `schemas/depo-tanimi.schema.json` | sozlesme | Dokuz koordinatlı depo tanımı. | — |
| `schemas/simdi-ve-sonrasi.schema.json` | sozlesme | Şimdi ve sonrası kaydı. | `schemas/rafine-sorulari.schema.json` |
| `schemas/yol.schema.json` | sozlesme | Açılıştan gerçeğe yol kaydı. | — |
| `schemas/rafine-bulgu.schema.json` | sozlesme | Gözden geçirme bulguları. | — |
| `schemas/harita.schema.json` | sozlesme | Depo haritası. | — |
| `schemas/exchange-manifest.schema.json` | sozlesme | Kapı aktarım paketi. | — |
| `schemas/deus-task.schema.json` | sozlesme | Yerel iş kaydı. | — |
| `schemas/deus-event.schema.json` | sozlesme | Yerel iş olayı. | — |
| `schemas/deus-checks.schema.json` | sozlesme | Yerel iş ölçüt denetimi. | — |
| `schemas/deus-handoff.schema.json` | sozlesme | Yerel iş devri. | — |
| `schemas/deus-assign-request.schema.json` | sozlesme | Yerel iş atama isteği. | — |
| `schemas/donusum.schema.json` | sozlesme | Dönüşüm kaydı. | — |
| `schemas/README.md` | belge | Bu klasörün giriş sayfası: ne taşıdığını, dosyalarını ve nasıl çalıştırıldıklarını anlatır. | — |

## Bakım araçları

Deponun kendini denetleyen ve üreten araçları. Hepsi çevrimdışı, yalnız standart kütüphaneyle çalışır; tek komut hepsini sırayla koşar. Yeri: `tools/`.

| Dosya | Tür | Ne | Eski adı |
| --- | --- | --- | --- |
| `tools/dogrula.py` | arac | Bütün çevrimdışı kontrolleri CI ile aynı sırayla tek komutta koşar. | — |
| `tools/depo_kontrol.py` | arac | Python ve JSON sözdizimi, kayıt bağları, sayaç, ayna ve imza denetimi. | — |
| `tools/sema_denetle.py` | arac | Sözleşmelerin desteklenen JSON Schema alt kümesinde kaldığını denetler; tek veriyi doğrular. | — |
| `tools/okuma_yayini_uret.py` | arac | Web kapısı sayfalarını docs altındaki kaynaklardan üretir; --check sapmayı denetler. | — |
| `tools/acilis.py` | arac | Açılış kaydını denetler; README, Web girişi, açılış ve teknik ek bloklarını üretir; yapı ve okunabilirlik denetimi. | — |
| `tools/yol.py` | arac | Yolun ölçütlerini depoya karşı hesaplar, açılışla tutarlılığı denetler, yol sayfasını ve teknik eki üretir. | — |
| `tools/cizim.py` | arac | Klavye çizimlerinin ortak kuralları: tek genişlikli karakterler, en çok 64 sütun, sekme ve satır sonu boşluğu yok. | — |
| `tools/harita.py` | arac | Haritayı denetler: her dosya tek alanda, eski adlar, künyeler, komutlar; harita belgesini üretir. | — |
| `tools/depo_tanimi.py` | arac | Depo tanımının ölçümlerini depodan üretir ve denetler. | — |
| `tools/simdi_ve_sonrasi.py` | arac | Şimdi ve sonrası kaydını denetler; senaryo sırasını ve ölçümleri verir. | `tools/rafine_sorulari.py` |
| `tools/donusum.py` | arac | Dönüşümü ölçer, prova eder, bekleyen önerileri çözümler ve iki belgeyi kayıttan üretir. | — |
| `tools/README.md` | belge | Bu klasörün giriş sayfası: ne taşıdığını, dosyalarını ve nasıl çalıştırıldıklarını anlatır. | — |

## Testler

Regresyon testleri; geçici depolar ve sahte komutlarla çalışır, gerçek sağlayıcı çağırmaz. Yeri: `tests/`.

| Dosya | Tür | Ne | Eski adı |
| --- | --- | --- | --- |
| `tests/test_simdi_ve_sonrasi.py` | test | Şimdi ve sonrası kaydının denetim ve hesap sınamaları. | `tests/test_rafine_sorulari.py` |
| `tests/README.md` | belge | Bu klasörün giriş sayfası: ne taşıdığını, dosyalarını ve nasıl çalıştırıldıklarını anlatır. | — |

## Otomasyon

GitHub üzerinde çalışan iş akışları, gönderim betiği, PR şablonu, okurun katkı kalıbı ve güvenlik politikası. Yeri: `.github/`.

| Dosya | Tür | Ne | Eski adı |
| --- | --- | --- | --- |
| `.github/workflows/dogrulama.yml` | ayar | PR ve ana dal için Linux ve Windows'ta tek komutlu doğrulama; yazma yetkisi yok. | — |
| `.github/workflows/kopru.yml` | ayar | Defter değişince, saatte bir ve elle botu çalıştırır; yanıtları gönderir. | — |
| `.github/workflows/deus-nt.yml` | ayar | NT sürücüsünü Windows'ta derler; imzalamaz, yüklemez. | — |
| `.github/scripts/kopru_gonder.sh` | betik | Otomasyonun gönderim betiği: yalnız defteri, aynayı ve çağrı kayıtlarını gönderir. | — |
| `.github/pull_request_template.md` | belge | PR açıklaması şablonu. | — |
| `.github/ISSUE_TEMPLATE/karsilik.yml` | ayar | Katkı kalıbı: okurun sorusunu, kaynağını, düzeltmesini ya da görüşünü, karşılık verdiği sayfa ve bölümle birlikte alan konu formu. Okuma sayfalarındaki bölüm bağlantıları yer alanını kendisi doldurur. | — |
| `.github/ISSUE_TEMPLATE/config.yml` | ayar | Konu açma ekranının ayarı: boş konuya izin verir, önce okumak isteyene açılış sayfasını gösterir. | — |
| `.github/SECURITY.md` | belge | Güvenlik ve gizlilik: neyin hiç paylaşılmadığı, nasıl korunduğu ve gizli bir bilgi sızarsa ne yapılacağı. GitHub bunu deponun güvenlik politikası olarak gösterir. | — |

## Çalıştırma

Aşağıdaki komutlar depo kökünden çalışır. Python komutları Python 3.12 ya da üstünü ve yalnız standart kütüphaneyi ister; öteki komutların ne istediği “Gerekir” sütunundadır. Yalnız okuyan komutlar her doğrulamada sınanır.

| Dosya | Komut | Yalnız okur | Gerekir |
| --- | --- | --- | --- |
| `kapi.py` | `python kapi.py --help` | evet | Python 3.12+ |
| `deus.py` | `python deus.py --help` | evet | Python 3.12+ |
| `Kopru_Izle.cmd` | `Kopru_Izle.cmd Hazirlik` | hayır | Windows, PowerShell 7, Git ve yerel kurulum (28 Ekim 2026 itibarıyla hiçbir bilgisayarda kurulu değil) |
| `defter/kopru_ekle.py` | `python defter/kopru_ekle.py kopru.html --kontrol` | evet | Python 3.12+ |
| `defter/kopru_oku.py` | `python defter/kopru_oku.py kopru.html --acik` | evet | Python 3.12+ |
| `defter/kopru_yanitla.py` | `python defter/kopru_yanitla.py kopru.html --kuru` | hayır | Python 3.12+ |
| `defter/kopru_birlestir.py` | `python defter/kopru_birlestir.py --help` | evet | Python 3.12+ |
| `defter/kopru_bolum_ekle.py` | `python defter/kopru_bolum_ekle.py --help` | evet | Python 3.12+ |
| `defter/kopru_ayna_uret.py` | `python defter/kopru_ayna_uret.py kopru.html ayna/kopru.html --kontrol` | evet | Python 3.12+ |
| `defter/kanit_satiri_guncelle.py` | `python defter/kanit_satiri_guncelle.py kopru.html --kontrol` | evet | Python 3.12+ |
| `yerel/kopru_izle.ps1` | `pwsh -File yerel/kopru_izle.ps1 -TekSefer` | hayır | Windows, PowerShell 7, Git ve yerel kurulum (28 Ekim 2026 itibarıyla hiçbir bilgisayarda kurulu değil) |
| `yerel/kopru_gonder.ps1` | `pwsh -File yerel/kopru_gonder.ps1` | hayır | Windows, PowerShell 7, Git ve yerel kurulum (28 Ekim 2026 itibarıyla hiçbir bilgisayarda kurulu değil); ana dala gönderme yetkisi |
| `windows/nt/build.ps1` | `pwsh -File windows/nt/build.ps1 -Restore` | hayır | Windows, PowerShell 7, Visual Studio 2022 derleme araçları ve NuGet |
| `tools/dogrula.py` | `python tools/dogrula.py` | hayır | Python 3.12+ |
| `tools/depo_kontrol.py` | `python tools/depo_kontrol.py` | evet | Python 3.12+ |
| `tools/sema_denetle.py` | `python tools/sema_denetle.py` | evet | Python 3.12+ |
| `tools/okuma_yayini_uret.py` | `python tools/okuma_yayini_uret.py --check` | evet | Python 3.12+ |
| `tools/acilis.py` | `python tools/acilis.py --check` | evet | Python 3.12+ |
| `tools/yol.py` | `python tools/yol.py --check` | evet | Python 3.12+ |
| `tools/harita.py` | `python tools/harita.py --check` | evet | Python 3.12+ |
| `tools/depo_tanimi.py` | `python tools/depo_tanimi.py --check` | evet | Python 3.12+ |
| `tools/simdi_ve_sonrasi.py` | `python tools/simdi_ve_sonrasi.py --check` | evet | Python 3.12+ |
| `tools/donusum.py` | `python tools/donusum.py --check` | evet | Python 3.12+ |

## Kaldırılan ve sıfırlanan dosyalar

Bazı dosyalar depodan bilerek kaldırıldı ya da içerikleri baştan yazıldı. Eski bir kayıtta bunlardan birinin adı geçerse ne olduğu ve önceki hâlinin hangi sürümde durduğu burada yazılıdır.

| Dosya | İşlem | Tarih | Neden | Önceki hâli |
| --- | --- | --- | --- | --- |
| `katilimcilar/AGENTS-kopru.md` | silindi | 2026-10-28 | Yardımcı talimatları her yerden kaldırıldı (Haluk, 28 Ekim 2026, 18.47 UTC). Codex, Claude Code, Copilot ve Gemini yardımcılarının talimat dosyalarına eklenen köprü parçasıydı. | [dcae3de](https://github.com/HalukAINRS/ortak-kopru/blob/dcae3deda4f0f796e77358331e3ae286cf668082/katilimcilar/AGENTS-kopru.md) |
| `katilimcilar/web-istem.md` | silindi | 2026-10-28 | Yardımcı talimatları her yerden kaldırıldı (Haluk, 28 Ekim 2026, 18.47 UTC). Web asistanlarına defterle birlikte verilen istemdi. Yanıtın JSON biçimi yanıt kalıbında durur. | [dcae3de](https://github.com/HalukAINRS/ortak-kopru/blob/dcae3deda4f0f796e77358331e3ae286cf668082/katilimcilar/web-istem.md) |
| `yerel/saman_devral.py` | silindi | 2026-10-28 | Yardımcı talimatları her yerden kaldırıldı (Haluk, 28 Ekim 2026, 18.47 UTC). Şaman'ın talimat paketini ayrı bir çalışma ağacına kurup Codex'i o talimatla açan başlatıcıydı; yerel kapının SamanDevam ve SamanHazirla kipleriyle birlikte kaldırıldı. | [dcae3de](https://github.com/HalukAINRS/ortak-kopru/blob/dcae3deda4f0f796e77358331e3ae286cf668082/yerel/saman_devral.py) |
| `tests/test_saman_devral.py` | silindi | 2026-10-28 | Yardımcı talimatları her yerden kaldırıldı (Haluk, 28 Ekim 2026, 18.47 UTC). Şaman başlatıcısının sınamalarıydı; başlatıcıyla birlikte kaldırıldı. | [dcae3de](https://github.com/HalukAINRS/ortak-kopru/blob/dcae3deda4f0f796e77358331e3ae286cf668082/tests/test_saman_devral.py) |
| `katilimcilar/istem-sablonu.md` | sıfırlandı | 2026-10-28 | Yardımcı talimatları her yerden kaldırıldı (Haluk, 28 Ekim 2026, 18.47 UTC). Botun istemindeki rol, kişilik ve çalışma kuralları çıkarıldı; yalnız yanıtın biçimi ve defterin reddettiği içerik kaldı. Defterin kurallar ve yönlendirme bölümleri artık istemle gönderilmez. | [dcae3de](https://github.com/HalukAINRS/ortak-kopru/blob/dcae3deda4f0f796e77358331e3ae286cf668082/katilimcilar/istem-sablonu.md) |

## Eski adlar

Eski kayıtlarda ve konuşmalarda geçen bir dosya adını burada bulabilirsiniz. Komutla da sorulabilir: `python tools/harita.py --nerede kopru_ekle.py`.

| Eski yol | Bugünkü yol |
| --- | --- |
| `AGENTS-kopru.md` | `katilimcilar/AGENTS-kopru.md (silindi)` |
| `KATMAN_HEDEFLEME.md` | `katilimcilar/katman-hedefleme.md` |
| `ayarlar-yerel.json` | `katilimcilar/ayarlar-yerel.json` |
| `ayarlar.json` | `katilimcilar/ayarlar.json` |
| `bolum-guncel-2026-10-24.html` | `docs/gecmis/parcalar/bolum-guncel-2026-10-24.html` |
| `bulgu-arg0-claude.json` | `docs/gecmis/parcalar/bulgu-arg0-claude.json` |
| `davet-copilot.json` | `docs/gecmis/parcalar/davet-copilot.json` |
| `docs/ACILIS.md` | `docs/acilis.md` |
| `docs/ACILIS_TEKNIK.md` | `docs/teknik/acilis-teknik.md` |
| `docs/ANLAM_NOT_DEFTERI.md` | `docs/gecmis/anlam-not-defteri.md` |
| `docs/BAKIM.md` | `docs/teknik/bakim.md` |
| `docs/DEPO_REHBERI.md` | `docs/teknik/depo-rehberi.md` |
| `docs/DEPO_TANIMI.md` | `docs/gecmis/depo-tanimi.md` |
| `docs/DEUS_EX_MACHINA.md` | `docs/teknik/deus-ex-machina.md` |
| `docs/DEVAM_VE_YEDEK.md` | `docs/teknik/devam-ve-yedek.md` |
| `docs/DIS_ALAN_KAPISI.md` | `docs/teknik/dis-alan-kapisi.md` |
| `docs/GECMIS.md` | `docs/gecmis/README.md` |
| `docs/KAPI_KULLANIMI.md` | `docs/teknik/kapi-kullanimi.md` |
| `docs/KAYNAKLAR.md` | `docs/gecmis/kaynaklar.md` |
| `docs/NT_KERNEL.md` | `docs/teknik/nt-kernel.md` |
| `docs/ORTAK_MIMARI_DEFTERI.md` | `docs/gecmis/ortak-mimari-defteri.md` |
| `docs/RAFINE_DEFTERI.md` | `docs/gecmis/rafine/rafine-defteri.md` |
| `docs/SIMDI_VE_SONRASI.md` | `docs/gecmis/simdi-ve-sonrasi.md` |
| `docs/SON_DURUM.md` | `docs/gecmis/son-durum.md` |
| `docs/TEKNIK.md` | `docs/teknik/README.md` |
| `docs/WEB_GIRISI.md` | `docs/web-girisi.md` |
| `docs/depo-tanimi.json` | `docs/gecmis/depo-tanimi.json` |
| `docs/kararlar/0001-deus-is-ve-nt.md` | `docs/teknik/kararlar/0001-deus-is-ve-nt.md` |
| `docs/kararlar/0002-dis-alan-kapisi.md` | `docs/teknik/kararlar/0002-dis-alan-kapisi.md` |
| `docs/rafine-sorulari.json` | `docs/gecmis/simdi-ve-sonrasi.json` |
| `docs/rafine/README.md` | `docs/gecmis/rafine/README.md` |
| `docs/rafine/claude-code-bulut-2026-10-28-bulgular.json` | `docs/gecmis/rafine/claude-code-bulut-2026-10-28-bulgular.json` |
| `docs/rafine/claude-code-bulut-2026-10-28-surec.md` | `docs/gecmis/rafine/claude-code-bulut-2026-10-28-surec.md` |
| `isemri-arg0.json` | `docs/gecmis/parcalar/isemri-arg0.json` |
| `istem-sablonu.md` | `katilimcilar/istem-sablonu.md` |
| `kanit_satiri_guncelle.py` | `defter/kanit_satiri_guncelle.py` |
| `kopru_ayna_uret.py` | `defter/kopru_ayna_uret.py` |
| `kopru_birlestir.py` | `defter/kopru_birlestir.py` |
| `kopru_bolum_ekle.py` | `defter/kopru_bolum_ekle.py` |
| `kopru_ekle.py` | `defter/kopru_ekle.py` |
| `kopru_gonder.ps1` | `yerel/kopru_gonder.ps1` |
| `kopru_izle.ps1` | `yerel/kopru_izle.ps1` |
| `kopru_oku.py` | `defter/kopru_oku.py` |
| `kopru_yanitla.py` | `defter/kopru_yanitla.py` |
| `kopru_yerel.ps1` | `yerel/kopru_yerel.ps1` |
| `saman_devral.py` | `yerel/saman_devral.py (silindi)` |
| `schemas/rafine-sorulari.schema.json` | `schemas/simdi-ve-sonrasi.schema.json` |
| `test_saman_devral.py` | `tests/test_saman_devral.py (silindi)` |
| `tests/test_rafine_sorulari.py` | `tests/test_simdi_ve_sonrasi.py` |
| `tools/rafine_sorulari.py` | `tools/simdi_ve_sonrasi.py` |
| `web-istem.md` | `katilimcilar/web-istem.md (silindi)` |
| `yanit-sablonu.json` | `katilimcilar/yanit-sablonu.json` |

## Künyeler

Yeni belgeler ve kayıtlar künyeleriyle kaynak gösterilebilir. Deponun tamamı için künye kökteki kaynak gösterme dosyasındadır.

| Dosya | Sahibi | Hazırlayan | Tarih | Kaynakları | Kimin için |
| --- | --- | --- | --- | --- | --- |
| `README.md` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `docs/acilis.json` | depoyu ilk kez gören okuyucu |
| `CONTRIBUTING.md` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `docs/harita.json`, `.github/SECURITY.md` | katkı vermek isteyen okur ve geliştirici |
| `CITATION.cff` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `docs/acilis.json` | kaynak gösterecek kişi ya da araç |
| `docs/README.md` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `docs/harita.json` | belgeleri arayan okuyucu |
| `docs/acilis.md` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `docs/acilis.json` | ilk kez gelen okuyucu |
| `docs/acilis.json` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `kopru.html` | araçlar ve kaynak gösterecek alanlar |
| `docs/yol.md` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `docs/yol.json`, `docs/acilis.json` | açılışın nasıl gerçeğe döneceğini merak eden okuyucu |
| `docs/yol.json` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `docs/acilis.json`, `docs/gecmis/simdi-ve-sonrasi.json`, `docs/gecmis/rafine/claude-code-bulut-2026-10-28-bulgular.json` | araçlar ve yolu temel alacak alanlar |
| `docs/harita.md` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `docs/harita.json` | depoda yolunu arayan okuyucu |
| `docs/harita.json` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `README.md` | araçlar ve depoyu temel alacak alanlar |
| `docs/donusum.md` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `docs/donusum.json`, `docs/harita.json` | deponun bugünkü düzene nasıl geçtiğini merak eden okuyucu |
| `docs/donusum.json` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `docs/harita.json`, `docs/acilis.json` | araçlar ve dönüşümü yeniden yapacak alanlar |
| `docs/sozluk.md` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `docs/acilis.json`, `docs/harita.json`, `katilimcilar/katman-hedefleme.md`, `docs/gecmis/ortak-mimari-defteri.md` | depoda geçen bir kelimeyi bilmeyen okuyucu |
| `docs/teknik/README.md` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `docs/harita.json` | kurulum ya da katkı için gelen okuyucu |
| `docs/teknik/acilis-teknik.md` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `docs/acilis.json` | açılışın dayanağını arayan okuyucu |
| `docs/teknik/yol-teknik.md` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `docs/yol.json` | adımı atacak ya da denetleyecek kişi |
| `docs/teknik/donusum-teknik.md` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `docs/donusum.json` | dönüşümü denetleyecek ya da benzerini yapacak okuyucu |
| `docs/teknik/yerel-taraf.md` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `yerel/kopru_yerel.ps1`, `yerel/kopru_izle.ps1`, `yerel/kopru_gonder.ps1`, `katilimcilar/ayarlar-yerel.json`, `Kopru_Izle.cmd` | yerel tarafı anlamak ya da yeniden kurmak isteyen |
| `docs/gecmis/README.md` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `docs/gecmis/rafine/claude-code-bulut-2026-10-28-surec.md` | geçmişi arayan okuyucu |
| `docs/gecmis/parcalar/README.md` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `kopru.html`, `katilimcilar/yanit-sablonu.json` | eski taslaklardan birine rastlayan okuyucu |
| `docs/gecmis/rafine/okuma-2026-10-28.md` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `docs/gecmis/rafine/claude-code-bulut-2026-10-28-okuma.json` | belgelerin hangi durumda olduğunu merak eden okuyucu |
| `docs/gecmis/rafine/claude-code-bulut-2026-10-28-okuma.json` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `schemas/rafine-bulgu.schema.json` | bulguları işleyecek araçlar ve alanlar |
| `.github/SECURITY.md` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `defter/kopru_ekle.py`, `defter/kopru_yanitla.py`, `src/ortak_kopru/local_files.py` | depoya bir şey eklemek isteyen ya da sızmış bir bilgi gören |

<!-- /uretilen:harita -->

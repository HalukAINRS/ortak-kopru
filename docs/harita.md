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

Belge adları küçük harf ve tire ile yazılır. README, CONTRIBUTING ve AGENTS gibi ortak adlar büyük harf kalır. Kod dosyaları dilin kuralına uyar ve eski adlarını korur.

Bir kayıt ile onun anlatısı aynı adı taşır ve yan yana durur: acilis.md ile acilis.json gibi.

Yeri ya da adı değişen her dosyanın eski adı bu haritada durur; eski kayıtlarda geçen bir ad buradan bulunur.

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

Kökte duran üç komut girişi. Adları ve yerleri değişmez; çünkü yerel bilgisayardaki kısayollar ve belgeler onları bu adla çağırır. Yeri: depo kökü.

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
| `mimari.html` | sayfa | Ortak Mimari Defteri. | — |
| `not-defteri.html` | sayfa | Anlam ve Dönüş Defteri. | — |
| `durum.html` | sayfa | Son durum. | — |
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

## Çağrı kayıtları

Botun her katılımcı çağrısı için yazdığı tam bağlam: istem, ham yanıt ve sonuç; atlanan çağrıların günlüğü. Bot yazar, elle düzenlenmez. Yeri: `kayit/`.

Bu alandaki dosyalar tek tek tanımlanmaz; alanın açıklaması hepsi için geçerlidir.

## Katılımcılar

Deftere kimin, hangi yoldan ve hangi kurallarla yazdığı: çağrı ayarları, istem şablonları, yanıt biçimi, hedefleme sözleşmesi ve CLI katmanlarının talimat parçası. Yeri: `katilimcilar/`.

| Dosya | Tür | Ne | Eski adı |
| --- | --- | --- | --- |
| `katilimcilar/ayarlar.json` | ayar | Bulut otomasyonundaki çağrı yolları: Claude CLI ve yedeği, ChatGPT ve Gemini için API yolları. | `ayarlar.json` |
| `katilimcilar/ayarlar-yerel.json` | ayar | Yerel bilgisayardaki CLI katılımcıları ve ortamları; yerel izleyici ve Şaman devri bunu okur. | `ayarlar-yerel.json` |
| `katilimcilar/istem-sablonu.md` | ayar | Botun sistem istemi ve kullanıcı iletisi şablonu. | `istem-sablonu.md` |
| `katilimcilar/web-istem.md` | ayar | Web asistanlarına defterle birlikte verilecek istem ve JSON yanıt biçimi. | `web-istem.md` |
| `katilimcilar/yanit-sablonu.json` | ayar | Web asistanlarının yanıt kalıbı; kayıt ekleyicinin --json girişi bunu okur. | `yanit-sablonu.json` |
| `katilimcilar/AGENTS-kopru.md` | ayar | CLI katmanlarının talimat dosyalarına eklenen köprü kuralları parçası. | `AGENTS-kopru.md` |
| `katilimcilar/katman-hedefleme.md` | belge | Bir kaydın hangi üreticiye ve role düştüğünü belirleyen hedefleme sözleşmesi. | `KATMAN_HEDEFLEME.md` |

## Yerel betikler

Yerel kullanıcının Windows bilgisayarında çalışan betikler: izleyici, gönderici, ortam kapısı ve Şaman devri başlatıcısı. Hepsi depo kökünde çalışır. Yeri: `yerel/`.

| Dosya | Tür | Ne | Eski adı |
| --- | --- | --- | --- |
| `yerel/kopru_yerel.ps1` | betik | Yerel makinenin ortamı ve modları (Hazirlik, Tek, Izle, Ekle, Bolum, Gonder ve ötekiler); Kopru_Izle.cmd bunu çağırır. | `kopru_yerel.ps1` |
| `yerel/kopru_izle.ps1` | betik | Makineden bağımsız izleyici: eşitler, botu yerel ayarla çalıştırır, yeni kayıt varsa gönderir. | `kopru_izle.ps1` |
| `yerel/kopru_gonder.ps1` | betik | Yerel değişiklikleri denetleyip gönderir; çakışmada defteri birleştirir, aynayı yeniler. | `kopru_gonder.ps1` |
| `yerel/saman_devral.py` | arac | Sabit Şaman devir paketini ayrı çalışma ağacında doğrular; --hazirla yalnız hazırlar. | `saman_devral.py` |

## Python paketi

Kapının ve yerel iş bileşeninin çekirdeği: aktarım, GitHub bağdaştırıcısı, iş ve olay kaydı, devir, yedek ve yerel sunucu. Yalnız standart kütüphane kullanır. Yeri: `src/`.

Bu alandaki dosyalar tek tek tanımlanmaz; alanın açıklaması hepsi için geçerlidir.

## Yerel arayüz

Yerel iş bileşeninin bilgisayarda açılan ekranı; yalnız yerel sunucu üzerinden çalışır. Yeri: `ui/`.

Bu alandaki dosyalar tek tek tanımlanmaz; alanın açıklaması hepsi için geçerlidir.

## Windows sürücüsü

Yerel iş bileşeninin NT aygıt kapısı: sürücü kaynakları, protokol ve derleme gereçleri. Yeri: `windows/`.

Bu alandaki dosyalar tek tek tanımlanmaz; alanın açıklaması hepsi için geçerlidir.

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
| `docs/donusum.md` | belge | Dönüşüm: GitHub'daki bugünkü deponun yeni oluşuma geçişi; aşamalar, kimin elinde olduğu, ölçüm ve geri dönüş, klavye çizimleriyle. | — |
| `docs/donusum.json` | kayit | Dönüşümün makine kaydı: aşamalar, ölçütler, son ölçüm, prova ve bekleyen önerilerin çözümlemesi. | — |

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

## Testler

Regresyon testleri; geçici depolar ve sahte komutlarla çalışır, gerçek sağlayıcı çağırmaz. Yeri: `tests/`.

| Dosya | Tür | Ne | Eski adı |
| --- | --- | --- | --- |
| `tests/test_saman_devral.py` | test | Şaman devri başlatıcısının geçici Git depolarıyla sınamaları. | `test_saman_devral.py` |
| `tests/test_simdi_ve_sonrasi.py` | test | Şimdi ve sonrası kaydının denetim ve hesap sınamaları. | `tests/test_rafine_sorulari.py` |

## Otomasyon

GitHub üzerinde çalışan iş akışları, gönderim betiği, PR şablonu ve okurun katkı kalıbı. Yeri: `.github/`.

| Dosya | Tür | Ne | Eski adı |
| --- | --- | --- | --- |
| `.github/workflows/dogrulama.yml` | ayar | PR ve ana dal için Linux ve Windows'ta tek komutlu doğrulama; yazma yetkisi yok. | — |
| `.github/workflows/kopru.yml` | ayar | Defter değişince, saatte bir ve elle botu çalıştırır; yanıtları gönderir. | — |
| `.github/workflows/deus-nt.yml` | ayar | NT sürücüsünü Windows'ta derler; imzalamaz, yüklemez. | — |
| `.github/scripts/kopru_gonder.sh` | betik | Otomasyonun gönderim betiği: yalnız defteri, aynayı ve çağrı kayıtlarını gönderir. | — |
| `.github/pull_request_template.md` | belge | PR açıklaması şablonu. | — |
| `.github/ISSUE_TEMPLATE/karsilik.yml` | ayar | Katkı kalıbı: okurun sorusunu, kaynağını, düzeltmesini ya da görüşünü, karşılık verdiği sayfa ve bölümle birlikte alan konu formu. Okuma sayfalarındaki bölüm bağlantıları yer alanını kendisi doldurur. | — |
| `.github/ISSUE_TEMPLATE/config.yml` | ayar | Konu açma ekranının ayarı: boş konuya izin verir, önce okumak isteyene açılış sayfasını gösterir. | — |

## Çalıştırma

Aşağıdaki komutlar depo kökünden çalışır ve Python'un standart kütüphanesinden başka bir şey istemez. Yalnız okuyan komutlar her doğrulamada sınanır.

| Dosya | Komut | Yalnız okur |
| --- | --- | --- |
| `kapi.py` | `python kapi.py --help` | evet |
| `deus.py` | `python deus.py --help` | evet |
| `Kopru_Izle.cmd` | `Kopru_Izle.cmd Hazirlik` | hayır |
| `defter/kopru_ekle.py` | `python defter/kopru_ekle.py kopru.html --kontrol` | evet |
| `defter/kopru_oku.py` | `python defter/kopru_oku.py kopru.html --acik` | evet |
| `defter/kopru_yanitla.py` | `python defter/kopru_yanitla.py kopru.html --kuru` | hayır |
| `defter/kopru_ayna_uret.py` | `python defter/kopru_ayna_uret.py kopru.html ayna/kopru.html --kontrol` | evet |
| `yerel/kopru_izle.ps1` | `pwsh -File yerel/kopru_izle.ps1 -TekSefer` | hayır |
| `yerel/kopru_gonder.ps1` | `pwsh -File yerel/kopru_gonder.ps1` | hayır |
| `yerel/saman_devral.py` | `python yerel/saman_devral.py --hazirla` | hayır |
| `tools/dogrula.py` | `python tools/dogrula.py` | hayır |
| `tools/depo_kontrol.py` | `python tools/depo_kontrol.py` | evet |
| `tools/sema_denetle.py` | `python tools/sema_denetle.py` | evet |
| `tools/okuma_yayini_uret.py` | `python tools/okuma_yayini_uret.py --check` | evet |
| `tools/acilis.py` | `python tools/acilis.py --check` | evet |
| `tools/yol.py` | `python tools/yol.py --check` | evet |
| `tools/harita.py` | `python tools/harita.py --check` | evet |
| `tools/depo_tanimi.py` | `python tools/depo_tanimi.py --check` | evet |
| `tools/simdi_ve_sonrasi.py` | `python tools/simdi_ve_sonrasi.py --check` | evet |
| `tools/donusum.py` | `python tools/donusum.py --check` | evet |

## Eski adlar

Eski kayıtlarda ve konuşmalarda geçen bir dosya adını burada bulabilirsiniz. Komutla da sorulabilir: `python tools/harita.py --nerede kopru_ekle.py`.

| Eski yol | Bugünkü yol |
| --- | --- |
| `AGENTS-kopru.md` | `katilimcilar/AGENTS-kopru.md` |
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
| `saman_devral.py` | `yerel/saman_devral.py` |
| `schemas/rafine-sorulari.schema.json` | `schemas/simdi-ve-sonrasi.schema.json` |
| `test_saman_devral.py` | `tests/test_saman_devral.py` |
| `tests/test_rafine_sorulari.py` | `tests/test_simdi_ve_sonrasi.py` |
| `tools/rafine_sorulari.py` | `tools/simdi_ve_sonrasi.py` |
| `web-istem.md` | `katilimcilar/web-istem.md` |
| `yanit-sablonu.json` | `katilimcilar/yanit-sablonu.json` |

## Künyeler

Yeni belgeler ve kayıtlar künyeleriyle kaynak gösterilebilir. Deponun tamamı için künye kökteki kaynak gösterme dosyasındadır.

| Dosya | Sahibi | Hazırlayan | Tarih | Kaynakları | Kimin için |
| --- | --- | --- | --- | --- | --- |
| `CITATION.cff` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `docs/acilis.json` | kaynak gösterecek kişi ya da araç |
| `docs/README.md` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `docs/harita.json` | belgeleri arayan okuyucu |
| `docs/acilis.md` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `docs/acilis.json` | ilk kez gelen okuyucu |
| `docs/acilis.json` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `kopru.html` | araçlar ve kaynak gösterecek alanlar |
| `docs/yol.md` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `docs/yol.json`, `docs/acilis.json` | açılışın nasıl gerçeğe döneceğini merak eden okuyucu |
| `docs/yol.json` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `docs/acilis.json`, `docs/gecmis/simdi-ve-sonrasi.json`, `docs/gecmis/rafine/claude-code-bulut-2026-10-28-bulgular.json` | araçlar ve yolu temel alacak alanlar |
| `docs/harita.md` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `docs/harita.json` | depoda yolunu arayan okuyucu |
| `docs/harita.json` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `README.md` | araçlar ve depoyu temel alacak alanlar |
| `docs/donusum.md` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `docs/donusum.json`, `docs/harita.json` | depoyu yeni hâline geçirecek sahibi ve onu izleyen okuyucu |
| `docs/donusum.json` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `docs/harita.json`, `docs/acilis.json` | araçlar ve dönüşümü yeniden yapacak alanlar |
| `docs/teknik/README.md` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `docs/harita.json` | kurulum ya da katkı için gelen okuyucu |
| `docs/teknik/acilis-teknik.md` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `docs/acilis.json` | açılışın dayanağını arayan okuyucu |
| `docs/teknik/yol-teknik.md` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `docs/yol.json` | adımı atacak ya da denetleyecek kişi |
| `docs/teknik/donusum-teknik.md` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `docs/donusum.json` | dönüşümü uygulayacak ya da denetleyecek okuyucu |
| `docs/gecmis/README.md` | Haluk | Claude Code Bulut (Hacker odağı) | 2026-10-28 | `docs/gecmis/rafine/claude-code-bulut-2026-10-28-surec.md` | geçmişi arayan okuyucu |

<!-- /uretilen:harita -->

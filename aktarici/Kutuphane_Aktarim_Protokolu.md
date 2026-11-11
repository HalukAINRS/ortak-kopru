# Kütüphane Aktarım Protokolü

**Köprü Aktarıcısı: işi yapan ve yolu**

**Sürüm:** 1.0\
**Tarih:** 11 Kasım 2026\
**Kapsam:** 33 Protokol Kütüphanesi'nin GitHub'daki `ortak-kopru` deposundan Google Drive'daki “128-bit CPU” klasörüne aktarılması, orada doğrulanması ve güncel tutulması

Bu protokol bir işi ve o işi yapanı tanımlar. İş, kütüphaneyi GitHub'dan Drive'a taşımak ve Drive'daki kopyanın her dosyasını kaynaktakiyle bayt bayt aynı tutmaktır. İşi yapan, Köprü Aktarıcısı adlı bir Google Apps Script betiğidir; metninin tamamı bu belgenin sonundadır. Aktarıcı, Drive'ın sahibinin Google hesabında, Google'ın sunucularında çalışır: bir bilgisayarın açık olmasına, bir tarayıcıya ya da bir sohbete ihtiyacı yoktur. Sahibi onu bir kez uyandırır; sonrasında aktarımı ne sahibi ne bir sohbetteki yapay zekâ yapar, aktarıcı kendisi yapar.

## Kullanım düzeni

Belge iki okura yazılmıştır. Drive'ın sahibi yalnız 0 Tohum bölümündeki Uyanma adımlarını, bir kez uygular. Aktarıcıyı inceleyen, onaylayan ya da değiştiren kişi veya araç, 1–6 bölümlerinde aktarıcının ne yaptığını, neyi hiç yapmadığını ve ne zaman durduğunu bulur. Aktarıcının her çalışması tek bir kayıt bırakır; kaydın alanları 6 Kökleşme bölümündedir.

Aktarıcının metni `aktarici/kopru_aktarici.gs` dosyasında da durur; o dosya ile bu belgenin sonundaki metin aynıdır. Biri değişirse öteki de aynı değişikliği alır ve bu belgenin sürümü artar.

## 0 Tohum (Başlangıç) Protokolü

İşin tohumu iki kopyanın ayrışmasıdır. Kaynak, GitHub'daki `ortak-kopru` deposunda duran kütüphanedir; Drive'daki kopya onun aynasıdır. Aynada bir dosya eksikse, bir dosyanın birden çok kopyası varsa, dosya Google biçimine dönüştürülmüşse ya da özeti kaynaktaki `SHA256SUMS` listesindekini tutmuyorsa iş başlar. İki kopya aynıysa aktarıcı hiçbir şey yazmaz.

Aktarıcının kendi başlangıcı, Drive'ın sahibinin onu uyandırmasıdır. Uyandırmak işi yapmak değildir: Google, Drive'a yazan her el için Drive'ın sahibinden bir kerelik izin ister ve bu izni sahibinden başka kimse veremez. Uyanmadan önce Drive'daki klasör boş olabilir ya da elle yüklenmiş eski bir kopya taşıyabilir; ilk çalışma ikisinde de aynı sonuca götürür.

### Uyanma

Bu adımlar bir kez, Drive'ın sahibi olan Google hesabıyla ve GitHub'daki `HalukAINRS` hesabıyla yapılır. Hepsi tarayıcıda yapılır; bir şey kurulmaz.

1. script.google.com adresinde yeni bir proje açın ve adını “Köprü Aktarıcısı” koyun. Düzenleyicideki örnek metni silin, bu belgenin sonundaki metni (ya da `aktarici/kopru_aktarici.gs` dosyasının ham metnini) yapıştırın ve kaydedin.
2. GitHub'da yalnız okuyan bir anahtar oluşturun: Settings, Developer settings, Personal access tokens, Fine-grained tokens, Generate new token. Resource owner `HalukAINRS`; Repository access “Only select repositories” ve yalnız `ortak-kopru`; izinlerde Contents için “Read-only”. Geçerlilik süresi olarak sunulan en uzun süreyi seçin. Anahtar yalnız bir kez gösterilir.
3. Apps Script'te Proje Ayarları'nı (dişli simgesi) açın. Betik özellikleri (Script Properties) bölümüne `GITHUB_ANAHTARI` adıyla bir özellik ekleyin ve değerine anahtarı yazın. Aynı sayfada saat diliminin sizin saat diliminiz olduğunu denetleyin.
4. Düzenleyicide çalıştırılacak işlev olarak `kur` seçip Çalıştır'a basın. Google üç izin ister: Drive'daki dosyaları görme ve düzenleme, dış bir hizmete bağlanma, siz yokken çalışma. Betik sizin hesabınızda duran ve Google'ca incelenmemiş bir betik olduğu için Google bir uyarı gösterir; Gelişmiş bağlantısından projeye geçilir.
5. Yürütme günlüğünde kayıt satırı görünür. `dogrulanan` ile `toplam` aynı sayıyı gösteriyor ve `sorun` listesi boşsa aktarıcı uyanmıştır: kütüphane Drive'dadır ve haftalık zamanlayıcı kurulmuştur.

Drive izni geniştir: Google, var olan bir klasöre yazabilmek için Drive'ın tamamına erişim izni ister. Aktarıcının metni yalnız “128-bit CPU” klasörünün içindeki `33_Protokol_Kutuphanesi` klasörüne yazdığını gösterir; GitHub anahtarı da yalnız bir depoyu okuyabilir.

## 1 Varlık Protokolü

İşi yapan Köprü Aktarıcısı'dır. Drive'ın sahibinin hesabında saklanan, onun izniyle ve zamanlayıcısıyla çalışan bir Apps Script betiğidir. İki anahtar taşır: Google'ın verdiği Drive izni (sahibinin hesabında durur, kimseye geçmez) ve GitHub'ı okumak için yalnız okuma yetkili, tek depoyla sınırlı bir anahtar (betik özelliklerinde durur; ne betiğin metninde ne depoda yer alır).

Aktarıcının işi üç fiildir: okumak, yazmak, doğrulamak. Kaynağı okur, Drive'a yazar, yazdığını doğrular. Kaynağa hiçbir şey yazmaz.

Bu işi başka bir taşıyıcının yapmamasının nedenleri:

- Drive'ın sahibi: işi o yapmaz. Yalnız uyandırır; bunu da Google'ın izin kuralı gerektirir.
- Bir sohbetteki yapay zekâ: Drive bağlayıcısı dosya içeriğini sohbetin metninden geçirir. Üç megabaytlık kütüphane bu kanala sığmaz ve her aktarım açık bir sohbete bağlı kalırdı.
- Masaüstü için Google Drive: sahibinin kullandığı ortamda (Windows PE) çalışmaz.
- Komut satırından eşitleyen araçlar: sahibinin kendi Google istemci kimliğini ve düzenli açık duran bir bilgisayarı ister.
- Kütüphaneden okuyan araçlar: okurlar, Drive'a yazmazlar.

Aktarıcı bir insanın yerine karar vermez. Seçim gerektiren her durumda (aynı adda iki klasör, kaynakta tutarsızlık) durur ve kararı Drive'ın sahibine bırakır.

## 2 Mekan Protokolü

İşin mekânı dört yerdir.

- Kaynak: `HalukAINRS/ortak-kopru` deposundaki `33_Protokol_Kutuphanesi` klasörü. Kütüphane `main` dalındaysa `main` okunur, değilse `kutuphane-33-protokol` dalı. Her çalışma, okuduğu dalın o anki işlemesine sabitlenir; bütün dosyalar aynı işlemeden okunur, böylece iki ayrı sürümden dosya karışmaz.
- Hedef: Drive'daki “128-bit CPU” klasörünün içindeki `33_Protokol_Kutuphanesi` klasörü ve alt klasörleri (`kimlik_metinleri`, `protokoller`, `kayit`, `araclar`). Klasör yoksa aktarıcı kurar. Bu klasörün dışına hiçbir şey yazmaz. “128-bit CPU” klasörünün kimliği metinde `UST_KLASOR` diye durur.
- Ölçü: kaynaktaki `SHA256SUMS`. Listedeki her dosyanın SHA-256 özeti ve listenin kendi özeti, Drive'daki kopyanın ölçüsüdür.
- Kayıt: betik özelliklerindeki `SON_AKTARIM` ve Apps Script'in yürütme günlüğü. Aktarıcı Drive'a kayıt dosyası yazmaz; kütüphane klasörü yalnız kütüphaneyi taşır.

## 3 Usül Protokolü

Her çalışma aynı usulle ilerler.

1. Kilit: aynı anda ikinci bir aktarım başlamaz. Kilit tutuluyorsa çalışma hiçbir şey yapmadan biter.
2. Kaynağı bulma: önce `main`, sonra `kutuphane-33-protokol` dalının ucundaki işleme okunur; kütüphanenin bulunduğu ilk dalın `SHA256SUMS` dosyası indirilir.
3. Drive'ı tarama: kütüphane klasörü alt klasörleriyle taranır. Çöp kutusundaki dosya ve klasörler sayılmaz.
4. Karşılaştırma: listedeki her dosya için Drive'da tek kopyanın bulunduğu, kopyanın Google biçimine dönüştürülmediği ve özetinin listedekini tuttuğu sınanır. Tutmayan dosyalar yenilenecekler listesine girer.
5. Kaynaktan alma: yenilenecek her dosya aynı işlemeden indirilir ve özeti sınanır. Biri bile tutmazsa aktarıcı Drive'a hiç dokunmadan durur.
6. Yazma: yeni kopya düz metin olarak, dönüştürülmeden yazılır; eskisi ondan sonra çöp kutusuna atılır. Böylece dosya hiçbir an Drive'dan eksik kalmaz. `SHA256SUMS` en son yazılır.
7. Yeniden doğrulama: Drive yeniden taranır, her dosya listeyle karşılaştırılır ve kayıt yazılır.

### Sınırlar

- Listede olmayan dosyaya dokunmaz; yalnız kayıtta bildirir.
- Hiçbir dosyayı kalıcı olarak silmez; yerinden ettiği kopyayı çöp kutusuna atar. Çöp kutusundaki kopya otuz gün içinde geri alınabilir.
- Kaynağa yazmaz; GitHub anahtarı yalnız okuyabilir.
- Kütüphane klasörünün dışına yazmaz.
- Aynı adda iki klasör bulursa birini seçmez, durur.

## 4 Zaman Protokolü

- İlk çalışma: `kur` çalıştırıldığı an. Aktarım başarılı olursa haftalık zamanlayıcı kurulur; hata verirse zamanlayıcı kurulmaz. `kur` yeniden çalıştırılırsa eski zamanlayıcının yerine yenisi kurulur, iki zamanlayıcı olmaz.
- Sonraki çalışmalar: her çarşamba 21:00–22:00 arasında, projenin saat dilimine göre. Kopyalar aynıysa aktarıcı yalnız okur, karşılaştırır ve kayıt bırakır.
- Elle çalışma: `aktar` işlevi istenen an çalıştırılabilir. Kaynak değiştiğinde çarşambayı beklemek gerekmez.
- Süre: bir çalışma birkaç dakikadan kısa sürer; Apps Script'in tek çalışma sınırı altı dakikadır. Kaynakta değişiklik olduktan sonra Drive'daki kopya en geç bir hafta içinde kaynağa yetişir.
- Anahtarın süresi: GitHub anahtarının süresi dolunca aktarıcı durur ve bunu bildirir (6 Kökleşme). Yeni anahtar oluşturulup `GITHUB_ANAHTARI` güncellenince bir sonraki çalışmada kaldığı yerden sürer.

## 5 Gaye Protokolü

Gayenin dayanağı kütüphanenin sahibinin sözüdür: “Okunacak ve korunacak bir kütüphane, araçların oradan okuyup çalışacağı bir kaynak. Alakalı olacak her şey, alakasız olan hiçbir şey.”

Aktarıcı için bu söz üç ölçüye dönüşür:

- Okunacak: Drive'daki her kütüphane dosyası, kaynaktaki adıyla ve klasör düzeniyle, düz metin olarak durur. Kişi Drive'da açıp okur; araç dönüştürmeden okur.
- Korunacak: kaynaktaki her dosya Drive'da bir kez ve bayt bayt aynı durur. Bu, her çalışmada yeniden kanıtlanır; kanıt, kayıttaki `dogrulanan` sayısının `toplam`a eşit ve `sorun` listesinin boş olmasıdır.
- Alakasız olan hiçbir şey: aktarıcı kütüphane klasörüne kütüphaneden başka bir şey yazmaz. Klasöre sonradan girmiş bir dosyayı da habersiz silmez; `listede_yok` alanında bildirir, kalıp kalmayacağına sahibi karar verir.

## 6 Kökleşme (Bitiş) Protokolü

Her çalışma iki sondan biriyle biter. Ya kopyalar doğrulanır ve kayıt yazılır ya da aktarıcı durur ve hata verir. Zamanlayıcıyla çalışan bir betik hata verdiğinde Google bunu Drive'ın sahibine e-postayla bildirir; bildirimin sıklığı Tetikleyiciler sayfasında değiştirilebilir (varsayılanı günlük özettir).

### Aktarım kaydı

`SON_AKTARIM` özelliği son çalışmanın kaydını tutar; aynı satır yürütme günlüğüne de yazılır.

| Alan | Anlamı |
|---|---|
| `zaman` | Çalışmanın bittiği an (UTC) |
| `kaynak` | Okunan dal ve işlemenin ilk yedi karakteri, örneğin `kutuphane-33-protokol@1a2b3c4` |
| `yenilenen` | Bu çalışmada Drive'a yeniden yazılan dosya sayısı |
| `cope_atilan` | Çöp kutusuna atılan eski kopya sayısı |
| `dogrulanan` | Drive'da tek, dönüştürülmemiş ve özeti tutan dosya sayısı |
| `toplam` | Kaynaktaki dosya sayısı (`SHA256SUMS` dâhil) |
| `sorun` | Yazıldıktan sonra da doğrulanamayan dosyalar; boş olmalıdır |
| `listede_yok` | Kütüphane klasöründe olup kaynakta bulunmayan dosyalar; dokunulmaz |

### Durma ve yapılacak

| Bildirim | Anlamı | Yapılacak |
|---|---|---|
| `GITHUB_ANAHTARI betik özelliği yok` | Uyanma tamamlanmamış | Uyanma, 3. adım |
| `GitHub anahtarı geçersiz ya da süresi dolmuş (401)` | Anahtar yanlış yazılmış ya da süresi dolmuş | Yeni anahtar oluşturup `GITHUB_ANAHTARI` güncellenir |
| `Kütüphane ne main dalında ne … bulundu` | Kütüphane iki dalda da yok ya da anahtar depoyu göremiyor | Anahtarın depo erişimi ve dalların durumu denetlenir |
| `Kaynakta yok` ya da `Kaynak kendi özetini tutmuyor` | Kaynak kendi içinde tutarsız; Drive'a dokunulmadı | Kaynakta `sha256sum -c SHA256SUMS` çalıştırılır, liste yeniden üretilir |
| `… adında birden çok klasör var` | Drive'da aynı adda iki klasör var | Sahibi hangisinin kalacağına karar verir, öbürünü kaldırır |
| `GitHub isteği başarısız` | Erişim ya da istek sınırı sorunu | Bir sonraki çalışma beklenir; sürerse anahtarın izinleri denetlenir |
| `Doğrulanamayan dosyalar` | Yazıldıktan sonra tutmayan dosya var | `aktar` yeniden çalıştırılır; sürerse dosyaya Drive'da bakılır |

### Değişiklik ve bitiş

Kütüphanedeki değişiklikler için aktarıcıya dokunulmaz: kaynak değişir, aktarıcı bir sonraki çalışmada Drive'ı eşitler. Kütüphane `main` dalına alınırsa aktarıcı kendiliğinden `main`'i okur. Aktarıcının metni değişirse yeni metin projeye yeniden yapıştırılır; Drive'daki proje kendi kendini güncellemez.

Aktarıcıyı durdurmak için Tetikleyiciler sayfasındaki zamanlayıcı silinir ya da proje silinir; GitHub anahtarı GitHub'dan iptal edilir. Drive'daki kopya olduğu gibi kalır ve `araclar/drive_dogrula.gs` ile kendi `SHA256SUMS` listesine göre doğrulanabilir.

### Sınama durumu

Aktarıcı, Apps Script ortamının kullandığı parçalarını taklit eden bir düzenekte, kaynağı gerçek depodan okuyarak on iki durumla sınandı: anahtarın olmaması ve geçersizliği, boş Drive'a ilk aktarım (dosyalar kaynakla bayt bayt aynı), değişiklik yokken ikinci çalışma (hiçbir şey yazılmaz), içeriği değiştirilmiş, iki kopyalı, Google biçimine dönüştürülmüş ve elle çöpe atılmış dosyalar (onarıldı; fazlalara dokunulmadı), `kur` işlevinin ikinci kez çalıştırılması (zamanlayıcı yine tek), kaynağın kendi özetini tutmaması (Drive'a dokunulmadı), kütüphanenin `main` dalına alınması, hiçbir dalda bulunmaması, aynı adda iki klasör, süren bir aktarım ve aynı Drive ağacında `araclar/drive_dogrula.gs` doğrulayıcısının sonucu (çöpteki kopyaları saymadı). Gerçek Drive'da henüz çalıştırılmadı; ilk gerçek çalışması uyanmadır.

## Köprü Aktarıcısının metni

Aşağıdaki metin `aktarici/kopru_aktarici.gs` dosyasıyla aynıdır. Uyanma'nın 1. adımında projeye bu metin yapıştırılır.

```javascript
/**
 * Köprü Aktarıcısı (Google Apps Script)
 *
 * 33 Protokol Kütüphanesi'ni GitHub'daki ortak-kopru deposundan Google Drive'daki
 * "128-bit CPU" klasörüne aktarır ve oradaki her dosyayı SHA256SUMS ile doğrular.
 * Yolu, sınırları ve hata durumları: aktarici/Kutuphane_Aktarim_Protokolu.md
 *
 * Uyanma (bir kez, Drive'ın sahibi): script.google.com'da yeni bir proje açıp bu metni
 * yapıştırın. Proje Ayarları'nda GITHUB_ANAHTARI adlı betik özelliğine, yalnız ortak-kopru'nun
 * içeriğini okuyabilen bir GitHub anahtarı yazın. "kur" işlevini çalıştırıp istenen izni verin.
 * Betik o anda bir kez, sonra her çarşamba 21:00 ile 22:00 arasında kendiliğinden çalışır.
 */
var DEPO = 'HalukAINRS/ortak-kopru';
var DAL = 'kutuphane-33-protokol'; // kütüphane main dalına alınırsa main kullanılır
var UST_KLASOR = '1qL10CUJyI-uUkFvj0LpqhMNMGwqH7RWk'; // 128-bit CPU
var KUTUPHANE = '33_Protokol_Kutuphanesi';
var HAM = 'application/vnd.github.raw+json';

/** İlk aktarımı yapar; başarılı olursa haftalık zamanlayıcıyı kurar (varsa eskisinin yerine). */
function kur() {
  aktar();
  ScriptApp.getProjectTriggers().forEach(function (t) {
    if (t.getHandlerFunction() === 'aktar') ScriptApp.deleteTrigger(t);
  });
  ScriptApp.newTrigger('aktar').timeBased().onWeekDay(ScriptApp.WeekDay.WEDNESDAY).atHour(21).create();
}

/** Drive'daki kopyayı kaynakla eşitler ve doğrular. Aynı anda ikinci bir aktarım başlamaz. */
function aktar() {
  var kilit = LockService.getScriptLock();
  if (!kilit.tryLock(1000)) {
    console.log('Başka bir aktarım sürüyor; bu çalışma atlandı.');
    return;
  }
  try {
    esitle();
  } finally {
    kilit.releaseLock();
  }
}

function esitle() {
  var ozellikler = PropertiesService.getScriptProperties();
  var anahtar = ozellikler.getProperty('GITHUB_ANAHTARI');
  if (!anahtar) throw new Error('GITHUB_ANAHTARI betik özelliği yok; yol belgesindeki Uyanma adımlarına bakın.');
  var kaynak = kaynakBul(anahtar);
  var beklenen = {};
  kaynak.ozetler.getDataAsString('UTF-8').split('\n').forEach(function (s) {
    var i = s.indexOf('  ');
    if (i > 0) beklenen[s.slice(i + 2)] = s.slice(0, i);
  });
  beklenen.SHA256SUMS = ozet(kaynak.ozetler.getBytes());
  var kok = klasorEdin(DriveApp.getFolderById(UST_KLASOR), KUTUPHANE);
  var drive = tara(kok, '', {});
  var yenilenecek = Object.keys(beklenen).filter(function (yol) { return !uyuyor(drive[yol], beklenen[yol]); });

  // Yenilenecek her dosya önce kaynaktan alınıp özetiyle sınanır; biri tutmazsa Drive'a dokunulmaz.
  var gelen = {};
  yenilenecek.forEach(function (yol) {
    var blob = kaynak.ozetler;
    if (yol !== 'SHA256SUMS') {
      var r = github(anahtar, icerik(yol, kaynak.sha), HAM);
      if (r.getResponseCode() !== 200) throw new Error("Kaynakta yok; Drive'a dokunulmadı: " + yol);
      blob = r.getBlob();
    }
    if (ozet(blob.getBytes()) !== beklenen[yol]) throw new Error("Kaynak kendi özetini tutmuyor; Drive'a dokunulmadı: " + yol);
    gelen[yol] = blob;
  });

  // Yeni kopya önce yazılır, eskisi sonra çöp kutusuna gider (30 gün geri alınabilir). SHA256SUMS en son yazılır.
  var copeAtilan = 0;
  yenilenecek.forEach(function (yol) {
    var parca = yol.split('/');
    var klasor = kok;
    for (var i = 0; i < parca.length - 1; i++) klasor = klasorEdin(klasor, parca[i]);
    klasor.createFile(gelen[yol].setName(parca[parca.length - 1]).setContentType('text/plain'));
    (drive[yol] || []).forEach(function (d) {
      d.setTrashed(true);
      copeAtilan++;
    });
  });
  if (yenilenecek.length) drive = tara(kok, '', {});

  var sorun = Object.keys(beklenen).filter(function (yol) { return !uyuyor(drive[yol], beklenen[yol]); });
  var sonuc = {
    zaman: new Date().toISOString(),
    kaynak: kaynak.dal + '@' + kaynak.sha.slice(0, 7),
    yenilenen: yenilenecek.length,
    cope_atilan: copeAtilan,
    dogrulanan: Object.keys(beklenen).length - sorun.length,
    toplam: Object.keys(beklenen).length,
    sorun: sorun,
    listede_yok: Object.keys(drive).filter(function (yol) { return !(yol in beklenen); })
  };
  ozellikler.setProperty('SON_AKTARIM', JSON.stringify(sonuc));
  console.log(JSON.stringify(sonuc));
  if (sorun.length) throw new Error('Doğrulanamayan dosyalar: ' + sorun.join(', '));
}

/** Bir dosya, tek kopyaysa, Google biçimine dönüştürülmemişse ve özeti tutuyorsa yerindedir. */
function uyuyor(dosyalar, beklenenOzet) {
  return !!dosyalar && dosyalar.length === 1 &&
    dosyalar[0].getMimeType().indexOf('application/vnd.google-apps') !== 0 &&
    ozet(dosyalar[0].getBlob().getBytes()) === beklenenOzet;
}

/** Kütüphanenin bulunduğu dalı (önce main) ve o dalın şu anki işlemesini bulur; bütün okumalar o işlemeden yapılır. */
function kaynakBul(anahtar) {
  var dallar = ['main', DAL];
  for (var i = 0; i < dallar.length; i++) {
    var ref = github(anahtar, '/git/ref/heads/' + dallar[i]);
    if (ref.getResponseCode() !== 200) continue;
    var sha = JSON.parse(ref.getContentText()).object.sha;
    var ozetler = github(anahtar, icerik('SHA256SUMS', sha), HAM);
    if (ozetler.getResponseCode() === 200) return { dal: dallar[i], sha: sha, ozetler: ozetler.getBlob() };
  }
  throw new Error('Kütüphane ne main dalında ne ' + DAL + ' dalında bulundu. Anahtar depoyu göremiyorsa da bu hata alınır.');
}

/** GitHub'a okuma isteği. 200 ve 404 döner; anahtar ya da erişim sorununda hata verir. */
function github(anahtar, yol, kabul) {
  var r = UrlFetchApp.fetch('https://api.github.com/repos/' + DEPO + yol, {
    headers: { Authorization: 'Bearer ' + anahtar, Accept: kabul || 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28' },
    muteHttpExceptions: true
  });
  var kod = r.getResponseCode();
  if (kod === 200 || kod === 404) return r;
  if (kod === 401) throw new Error('GitHub anahtarı geçersiz ya da süresi dolmuş (401); GITHUB_ANAHTARI yenilenmeli.');
  throw new Error('GitHub isteği başarısız (' + kod + '): ' + yol);
}

function icerik(yol, sha) {
  return '/contents/' + (KUTUPHANE + '/' + yol).split('/').map(encodeURIComponent).join('/') + '?ref=' + sha;
}

/** Klasörü alt klasörleriyle tarar: yol -> dosyalar. Çöp kutusundakiler sayılmaz. */
function tara(klasor, onek, bulunan) {
  var f = klasor.getFiles();
  while (f.hasNext()) {
    var d = f.next();
    if (d.isTrashed()) continue;
    var yol = onek + d.getName();
    (bulunan[yol] = bulunan[yol] || []).push(d);
  }
  var k = klasor.getFolders();
  while (k.hasNext()) {
    var alt = k.next();
    if (!alt.isTrashed()) tara(alt, onek + alt.getName() + '/', bulunan);
  }
  return bulunan;
}

/** Adı verilen alt klasörü bulur, yoksa kurar. Aynı adda birden çok klasör varsa durur. */
function klasorEdin(ust, ad) {
  var bulunan = [];
  var it = ust.getFoldersByName(ad);
  while (it.hasNext()) {
    var k = it.next();
    if (!k.isTrashed()) bulunan.push(k);
  }
  if (bulunan.length > 1) throw new Error(ad + ' adında birden çok klasör var; hangisinin kalacağına Drive\'ın sahibi karar verir.');
  return bulunan.length ? bulunan[0] : ust.createFolder(ad);
}

function ozet(bayt) {
  return Utilities.computeDigest(Utilities.DigestAlgorithm.SHA_256, bayt)
    .map(function (b) { return ('0' + (b & 0xff).toString(16)).slice(-2); }).join('');
}
```

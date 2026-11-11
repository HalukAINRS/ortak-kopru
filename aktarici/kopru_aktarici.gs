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

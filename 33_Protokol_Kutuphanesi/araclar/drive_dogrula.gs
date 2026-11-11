/**
 * 33 Protokol Kütüphanesi — Drive'daki kopyanın doğrulaması (Google Apps Script).
 *
 * Kütüphane klasöründeki SHA256SUMS dosyasını okur; listedeki her dosyanın Drive'daki
 * içeriğinin SHA-256 özetini hesaplayıp listedekiyle karşılaştırır. Eksik, iki kez yüklenmiş,
 * Google biçimine dönüştürülmüş ve listede olmayan dosyaları da bildirir. Hiçbir dosyayı değiştirmez.
 *
 * Kullanım: script.google.com'da yeni bir proje açın, bu metni yapıştırın, "dogrula" işlevini
 * seçip Çalıştır'a basın ve istenen izni verin. Sonuç yürütme günlüğünde görünür.
 * Kütüphane başka bir klasöre yüklendiyse UST_KLASOR'a o klasörün adresindeki kimliği yazın.
 */
var UST_KLASOR = '1qL10CUJyI-uUkFvj0LpqhMNMGwqH7RWk';
var KUTUPHANE = '33_Protokol_Kutuphanesi';

function dogrula() {
  var kok = tekKlasor(DriveApp.getFolderById(UST_KLASOR), KUTUPHANE);
  var beklenen = {};
  tekDosya(kok, 'SHA256SUMS').getBlob().getDataAsString('UTF-8').split('\n').forEach(function (s) {
    var i = s.indexOf('  ');
    if (i > 0) beklenen[s.slice(i + 2)] = s.slice(0, i);
  });
  var bulunan = {};
  tara(kok, '', bulunan);
  var tamam = 0;
  var sorun = [];
  Object.keys(beklenen).forEach(function (yol) {
    var dosyalar = bulunan[yol] || [];
    if (dosyalar.length === 0) { sorun.push('EKSİK: ' + yol); return; }
    if (dosyalar.length > 1) sorun.push('İKİ KEZ: ' + yol + ' (' + dosyalar.length + ' kopya)');
    var d = dosyalar[0];
    if (d.getMimeType().indexOf('application/vnd.google-apps') === 0) {
      sorun.push('DÖNÜŞTÜRÜLMÜŞ: ' + yol + ' (' + d.getMimeType() + ')');
      return;
    }
    if (ozet(d) === beklenen[yol]) tamam++;
    else sorun.push('FARKLI: ' + yol);
  });
  Object.keys(bulunan).forEach(function (yol) {
    if (!(yol in beklenen) && yol !== 'SHA256SUMS') sorun.push('LİSTEDE YOK: ' + yol);
  });
  Logger.log('Doğrulanan dosya: ' + tamam + ' / ' + Object.keys(beklenen).length);
  sorun.forEach(function (s) { Logger.log(s); });
  if (sorun.length === 0) Logger.log('Kütüphane bozulmadan yerleşmiş.');
}

function tara(klasor, onek, bulunan) {
  var f = klasor.getFiles();
  while (f.hasNext()) {
    var d = f.next();
    var yol = onek + d.getName();
    (bulunan[yol] = bulunan[yol] || []).push(d);
  }
  var k = klasor.getFolders();
  while (k.hasNext()) {
    var alt = k.next();
    tara(alt, onek + alt.getName() + '/', bulunan);
  }
}

function ozet(dosya) {
  return Utilities.computeDigest(Utilities.DigestAlgorithm.SHA_256, dosya.getBlob().getBytes())
    .map(function (b) { return ('0' + (b & 0xff).toString(16)).slice(-2); }).join('');
}

function tekKlasor(ust, ad) {
  var it = ust.getFoldersByName(ad);
  if (!it.hasNext()) throw new Error(ad + ' klasörü bulunamadı');
  var k = it.next();
  if (it.hasNext()) throw new Error(ad + ' adında birden çok klasör var; fazlasını kaldırıp yeniden çalıştırın');
  return k;
}

function tekDosya(klasor, ad) {
  var it = klasor.getFilesByName(ad);
  if (!it.hasNext()) throw new Error(ad + ' bulunamadı');
  return it.next();
}

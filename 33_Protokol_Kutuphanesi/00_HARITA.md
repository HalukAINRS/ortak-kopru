# 33 Protokol Kütüphanesi

**Okunacak ve korunacak bir kütüphane; araçların okuyup çalıştığı bir kaynak**

**Sürüm:** 1.0\
**Tarih:** 11 Kasım 2026\
**Kapsam:** 33 protokol, köken aldıkları üç kimlik metni, ortak biçim kuralları, çalışma kaydı ve denetim araçları

Bu harita kütüphaneye aittir; protokoller ona muhtaç değildir. Her protokol kendi 0–6 düzenini, masaüstünde uygulama adımlarını ve kayıt şablonunu içinde taşır; tek başına okunur ve uygulanır. Harita yalnız kütüphaneye giren kişiye ya da araca nereden başlayacağını gösterir.

## Düzen

- `00_HARITA.md`: bu dosya.
- `ORTAK_BICIM_KURALLARI.md`: protokollerin yazım, kodlama ve yapı kuralları.
- `SHA256SUMS`: kütüphanedeki her dosyanın bu sürümdeki SHA-256 özeti.
- `kimlik_metinleri/`: protokollerin paylaştığı 0–6 düzenini kendi alanlarında kuran üç metin.
- `protokoller/`: 33 protokol.
- `kayit/`: kütüphanenin nasıl kurulduğunu, hangi kararla neyin değiştiğini anlatan çalışma kaydı.
- `araclar/`: protokollerin biçim denetimi (`bicim_denetim.py`, `bicim.py`) ve Drive'daki kopyanın doğrulaması (`drive_dogrula.gs`).

## Kimlik metinleri

| Dosya | Metin | Türetilen protokol |
|---|---|---|
| `0.1_Hacker_Ilkeleri_Tohumdan_Koklesmeye.md` | Hacker İlkeleri — Tohumdan Kökleşmeye | 31 |
| `0.2_Sahitlik_Mimarisi_Ilkeler_ve_Kavramsal_Cerceve.md` | Şahitlik Mimarisi — İlkeler ve Kavramsal Çerçeve | 32 |
| `0.3_Samanlik_Ilkeleri_Samanin_Dogusundan_Olumune.md` | Şamanlık İlkeleri — Şamanın Doğuşundan Ölümüne | 33 |

Kimlik metinleri kullanıcının kendi metinleridir. Buradaki sürümler kaynaklarına sözcüğü sözcüğüne sadık Markdown sürümleridir; sözleri ve yazımları olduğu gibi korunur, ortak biçim kurallarının yazım bölümü onlara uygulanmaz. Eklenen klavye çizimleri alt yazılarındaki “(ek)” işaretiyle metinden ayrılır. Her metnin sonundaki “Bu markdown sürümü hakkında” bölümü metnin parçası değildir; aktarımın nasıl yapıldığını, düzeltmeleri, uygulanmamış önerileri ve çizimleri yazar.

## Protokoller

Her protokolde 0–6 bölüm başlıkları aynı sözle yazılıdır: “## 0 Tohum (Başlangıç) Protokolü”, “## 1 Varlık Protokolü”, “## 2 Mekan Protokolü”, “## 3 Usül Protokolü”, “## 4 Zaman Protokolü”, “## 5 Gaye Protokolü”, “## 6 Kökleşme (Bitiş) Protokolü”. Bölümler bu başlıklarla bulunur.

| No | Protokol | Dosya |
|---|---|---|
| 01 | Masaüstü Dosya ve İçerik Yönetimi Protokolleri | `01_Masaustu_Dosya_ve_Icerik_Yonetimi_Protokolleri.md` |
| 02 | Masaüstü Karargâhları Mimarisi | `02_Masaustu_Karargahlari_Mimarisi_Protokoller_0-6.md` |
| 03 | Bilgisayar Ekosistemi Mühendisliği Protokolleri | `03_Bilgisayar_Ekosistemi_Muhendisligi_Protokolleri_0_6.md` |
| 04 | Klavye Tabanlı Görsel Tasarım ve Üretim | `04_Klavye_Tabanli_Gorsel_Tasarim_ve_Uretim_Protokolleri.md` |
| 05 | Bağlamsal Keşif ve İdrak Protokolleri | `05_Baglamsal_Kesif_ve_Idrak_Protokolleri.md` |
| 06 | Bit Tabanlı Hesaplama Sistemleri Mühendisliği | `06_BTHSM_Protokoller_0-6.md` |
| 07 | Ortak Çalışma ve Karar Orkestrasyonu | `07_Ortak_Calisma_ve_Karar_Orkestrasyonu.md` |
| 08 | Anlamın İfadesi ve Aktarımı Protokolleri | `08_Anlamin_Ifadesi_ve_Aktarimi_Protokolleri.md` |
| 09 | Sınama ve Karşılık Değerlendirmesi | `09_Sinama_ve_Karsilik_Degerlendirmesi_Protokoller_0-6.md` |
| 10 | Steering (Yönlendirme) Mimarisi ve Engelleme Mühendisliği | `10_Steering_Yonlendirme_Mimarisi_Protokoller_0_6.md` |
| 11 | Çalışma Hafızası ve Süreklilik Protokolleri | `11_CALISMA_HAFIZASI_VE_SUREKLILIK.md` |
| 12 | Arayüz Çizimleri, İşletim Sistemi Mimarisi ve Çekirdek Katmanların Modellemesi | `12_Modelleme_Protokolleri_0_6.md` |
| 13 | Yetki ve Sınır Yönetimi Protokolleri Tam Metin | `13_Yetki_ve_Sinir_Yonetimi_Tam_Metin.md` |
| 14 | Kaynak ve Kapasite Yönetimi Protokolleri | `14_Kaynak_ve_Kapasite_Yonetimi_Tam_Metin.md` |
| 15 | Erişilebilirlik ve Kullanım Uyarlaması | `15_Erisilebilirlik_ve_Kullanim_Uyarlamasi_Protokolleri.md` |
| 16 | Öğrenme Tasarımı ve Yetkinlik Geliştirme | `16_ogrenme_tasarimi_yetkinlik_gelistirme_protokolleri.md` |
| 17 | İşitsel Tasarım ve Üretim Protokolleri | `17_isitsel_tasarim_ve_uretim_protokolleri_v1_0.md` |
| 18 | Oyun Tasarımı ve Üretimi Protokolleri | `18_Oyun_Tasarimi_ve_Uretimi_Protokolleri_0-6.md` |
| 19 | Siber Güvenlik Mühendisliği | `19_siber-guvenlik-muhendisligi-son-belge.md` |
| 20 | Makine Öğrenmesi Mühendisliği Protokolleri | `20_Makine_Ogrenmesi_Muhendisligi_Protokolleri.md` |
| 21 | Veri Tabanı Mühendisliği | `21_Veri_Tabani_Muhendisligi_Protokoller_0_6.md` |
| 22 | Bilgisayar Ağları Mühendisliği Protokolleri | `22_Bilgisayar_Aglari_Muhendisligi_Protokolleri.md` |
| 23 | Bilgi Erişimi ve Arama Sistemleri Mühendisliği | `23_Bilgi_Erisimi_Arama_Sistemleri_Protokolleri_0-6.md` |
| 24 | Yazılım Derleme ve Dağıtım Mühendisliği Protokolleri | `24.yazilim-derleme-ve-dagitim-muhendisligi-protokolleri.md` |
| 25 | Bilgisayarlı Görü Mühendisliği Protokolleri | `25_Bilgisayarli_Goru_Muhendisligi_Protokolleri.md` |
| 26 | Öznel Yaşantı ve İrade Mimarisi | `26_Oznel_Yasanti_ve_Irade_Mimarisi_0-6.md` |
| 27 | Yazılı Eser Tasarımı ve Üretimi Protokolleri | `27_Yazili_Eser_Tasarimi_ve_Uretimi_Protokolleri_0_6.md` |
| 28 | Bilgi Temsili ve Sembolik Akıl Yürütme Mühendisliği | `28_Bilgi_Temsili_ve_Sembolik_Akil_Yurutme_Protokolleri_0-6.md` |
| 29 | Sistem Gözlemlenebilirliği Mühendisliği | `29_Sistem_Gozlemlenebilirligi_Muhendisligi_Tam_Belge.md` |
| 30 | Tersine Mühendislik ve İşleyiş Çözümleme Protokolleri | `30_Tersine_Muhendislik_ve_Isleyis_Cozumleme_Protokolleri.md` |
| 31 | Yaratıcı Yeniden İşlevlendirme Mühendisliği | `31_Yaratici_Yeniden_Islevlendirme_Muhendisligi_0-6_Protokolleri.md` |
| 32 | Tanıklık ve Emanet Aktarımı Mimarisi | `32_Taniklik_ve_Emanet_Aktarimi_Mimarisi_0-6_Protokolleri.md` |
| 33 | Geçiş ve Yeniden Bütünleşme Mimarisi | `33_Gecis_ve_Yeniden_Butunlesme_Mimarisi_0-6_Masaustu_Protokolleri.md` |

## Okuyan kişi için

Protokol, çalışılacak alana göre seçilir ve baştan sona okunur. Uygulamaya geçerken protokolün içindeki kayıt şablonu kişinin kendi çalışma klasörüne kopyalanır; kütüphanedeki dosyalar değişmeden kalır. Çizimler eş aralıklı bir yazı tipiyle, en az 72 sütunluk bir genişlikte doğru görünür.

## Okuyup çalışan araç için

- Önce bu haritayı, sonra işe uygun protokolü baştan sona oku. Protokolün 0–6 sırasını izle; bir bölüme dönmek gerekirse protokolün kendi geri dönüş koşullarına uy.
- Kayıtları kullanıcının çalışma klasörüne yaz; kütüphanedeki dosyaları değiştirme. Bir değişiklik gerekiyorsa öneri olarak yaz; kütüphaneye kullanıcının onayıyla girer.
- Kullanıcının kurucu soruları ve belgeleme yönergeleri hiçbir düzenlemede değişmez.
- Çizimler `~~~text` bloklarındadır; ASCII'dir ve en çok 72 sütundur. Satırlarını kaydırma ve yeniden biçimleme.
- Bütünlük: kütüphane klasöründe `sha256sum -c SHA256SUMS` (macOS'ta `shasum -a 256 -c SHA256SUMS`) her dosyanın bu sürümle aynı olup olmadığını gösterir. Drive'daki kopya için `araclar/drive_dogrula.gs` Google Apps Script'te çalıştırılır; her dosyanın özetini Drive'da hesaplayıp `SHA256SUMS` ile karşılaştırır.
- Biçim: `python3 araclar/bicim_denetim.py protokoller` kurala aykırı yerleri kural kural sayar. Bu sürümde her kural için sonuç sıfırdır.

Araçlara dağıtım önerisi (11–11–11) çalışma kaydının Ek C bölümündedir; dağıtım henüz yapılmamıştır.

## Değişiklik yolu

Kütüphanenin tek kaynağı bu klasördür. Bir protokoldeki değişiklik protokol dosyasının kendisinde yapılır: ortak biçim kurallarına uyar, biçim denetimi sıfır verir, çizimler ASCII ve en çok 72 sütun kalır. Değişen protokolün sürüm numarası artar (1.0'dan 1.1'e) ve tarihi güncellenir. Değişiklik gerekçesiyle çalışma kaydına ya da yeni bir kayda yazılır ve `SHA256SUMS` yeniden üretilir. Kimlik metinlerinde değişikliği yalnız kullanıcı yapar.

## Köken

Kütüphane, `kaynaklar.7z` arşivindeki 33 Markdown dosyasından kuruldu. Her protokol baştan sona okundu, önerileri uygulandı ve klavye çizimleriyle zenginleştirildi (529 çizim). Ardından protokoller ortak biçime getirildi ve dış dosyalara bağımlılıktan arındırıldı. Bütün değişikliklerin dökümü ve kullanıcının kararları çalışma kaydındadır.

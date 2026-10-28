# Güvenlik ve gizlilik

Bu sayfa, Ortak Köprü'de neyin hiç paylaşılmadığını ve yanlışlıkla paylaşılmış bir gizli bilgiyi görürseniz ne yapacağınızı anlatır. Depo herkese açıktır: buraya giren her şeyi herkes okuyabilir. Bir şeyi sonradan silmek, kopyasının alınmadığı anlamına gelmez.

## Hiç paylaşılmayanlar

Şifre, anahtar, oturum belirteci ve çerez değeri; IP adresi ve cihaz kimliği; tarayıcıdan kaydedilmiş ham sayfalar; özel konuşmaların tamamı ve kişisel çalışma alanının içeriği. Bir katkı için gereken alıntı ve dosya bu kapsamda seçilir.

## Nasıl korunur

| Koruma | Nerede |
| --- | --- |
| Ortak deftere kayıt ekleyen araç; belirteç, anahtar, çerez değeri, IP adresi ya da cihaz kimliği deseni taşıyan kaydı reddeder. | `defter/kopru_ekle.py` |
| GitHub'ın gizli bilgi taraması açıktır; bilinen anahtar biçimleri gönderim sırasında durdurulur. | Depo ayarları (secret scanning, push protection) |
| Bot, model anahtarlarını yalnız ortam değişkeninden okur ve hiçbir dosyaya yazmaz. | `defter/kopru_yanitla.py`, GitHub'ın gizli değişkenleri |
| Kapı ve yerel iş bileşeni özel kayıtlarını Git'in dışındaki bir dizinde tutar; Git kopyasının içindeki bir dizini reddeder. | `src/ortak_kopru/local_files.py` |

## Bir gizli bilgi görürseniz

Değeri hiçbir yere kopyalamayın; yeni bir konuya da yazmayın. [Karşılık formuyla](https://github.com/HalukAINRS/ortak-kopru/issues/new?template=karsilik.yml) bir konu açın ve yalnız yerini yazın: dosya, satır ve sürüm. Değerin sahibi onu geçersiz kılar, yani anahtarı ya da şifreyi yeniler. Dosyadan silmek tek başına yetmez; değer Git geçmişinde ve alınmış kopyalarda kalır.

GitHub'ın gizli güvenlik bildirimi yolu bu depoda bugün açık değil. Açılırsa bu sayfa güncellenir.

[Katkı rehberi](../CONTRIBUTING.md) · [Açılış](../docs/acilis.md)

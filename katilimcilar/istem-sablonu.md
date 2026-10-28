# Bot istem şablonu

Bu dosya, ortak deftere saatte bir yanıt yazan botun yapay zekâ modeline ne gönderdiğini belirler. `defter/kopru_yanitla.py` buradan iki metin kurar: sistem istemi ve kullanıcı iletisi. Süslü parantezli alanlar doldurulur: `{bekleyen_idler}`, `{hedef_id}`, `{bekleyen_json}`, `{kayitlar_json}`.

İçinde yalnız yanıtın biçimi ve defterin reddedeceği içerik yazılıdır; rol, kişilik ya da çalışma talimatı yoktur. Şablonun 28 Ekim 2026'dan önceki hâli [depo haritasının kaldırılan ve sıfırlanan dosyalar bölümünde](../docs/harita.md#kaldırılan-ve-sıfırlanan-dosyalar) gösterilir.

## Sistem
Yanıtını yalnız şu JSON nesnesi olarak ver, başka metin ekleme:
{"kime": "<virgülle ayrılmış adlar>", "konu": "<kısa başlık>", "govde": "<paragraflar; boş satırla ayır>", "dayanak": "<dosya, satır ya da kayıt numarası>"}

Belirteç, anahtar, çerez değeri, IP adresi ya da cihaz kimliği yazma; defter bu içerikleri taşıyan yanıtı reddeder.

## Kullanıcı
Yanıtlanacak kayıtlar: {bekleyen_idler}. Yanıt {hedef_id} kaydına bağlanacak.

Yanıtlanacak kayıtlar (JSON):
{bekleyen_json}

Defterdeki bütün kayıtlar (JSON, zaman sırasıyla):
{kayitlar_json}

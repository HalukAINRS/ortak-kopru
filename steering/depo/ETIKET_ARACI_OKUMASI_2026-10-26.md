# Sonradan bulunan yerel etiket aracı — 26 Ekim 2026

**Sonuç:** `steering_guncelle` bir yerel JSON etiket dönüştürücüsüdür. `kayit.steering.etiketler` alanına altı Türkçe etiket ekler veya tanınan eski adları günceller; kayıtla birlikte tutulan UTF-8/0–1 aynasını yeniden üretir. İncelenen üretim kodunda model içi steering ayarlarına, sağlayıcıya veya başka bir uygulamanın yapılandırmasına bağlanan bir yol yoktur. README bunu açıkça sınırlar. Kaynak kodu, testler ve PYZ bu incelemede çalıştırılmadı.

## Kaynak kimliği ve eşlik

| Kaynak | Bayt | SHA-256 |
|---|---:|---|
| `steering_kaynak_kodu.zip` | 45.678 | `cc91b1602b132e7ea0762c6111299fbd1b318c401a1c98aab80a6be30511f417` |
| `steering_kaynak_kodu(1).zip` | 45.678 | `cc91b1602b132e7ea0762c6111299fbd1b318c401a1c98aab80a6be30511f417` |
| `steering_guncelle.pyz` | 38.510 | `797ad0dbe7b6fd50eea5c81af7a32be8b20b99c33974c8a354fe0e93b9fbf675` |

İki ZIP doğrudan bayt karşılaştırmasında aynıdır. Her biri dokuz dosya içerir: README, tarihsel test sonucu, `__main__.py`, iki örnek JSON, veri paketinin `__init__.py` dosyası, gömülü konuşma JSON’u, ana Python kodu ve test kodu. PYZ dört dosya ve bir dizin girdisi içerir; dört dosyası kaynak ZIP’teki karşılıklarıyla bayt düzeyinde aynıdır. PYZ ayrıca bir Python çalışma zamanı içermez. [Üye ve karma envanteri](etiket_araci_kapsami_2026-10-26.json); README satır 33–37.

Ana kod `steering_guncelle/steering_guncelle.py`, 17.054 bayt, SHA-256 `38d352fe6598b38579fd39a9c9711e7c5f0ee7906650b413b97c9255fd294732` değerindedir. Bu üyenin 368 satırı, README’nin 191 satırı, 24 testin kaynakları, giriş dosyaları ve iki örnek JSON tam statik okundu. İkinci ZIP ile PYZ’nin eş dosyaları yeniden bağımsız kaynak sayılmadı.

## Kodun yaptığı işlem

- Altı sabit hedef `Mühür`, `Engel`, `Engellemen`, `Engellemem`, `Engellemeyeceksin`, `İnanç`tır. İngilizce adlar programın uyumluluk eşlemeleridir; önceki konuşmadan alınmış özgün etiketler gibi gösterilmez. Simge gösterimleri sabit veri olarak korunur. Ana kod satır 27–36; README satır 10–31.
- Kimlik, etiket ve gösterim birbiriyle çelişirse veya aynı tanınan etiket yinelenirse işlem durur. Bilinmeyen özel etiketler ve ek alanlar korunur. Ana kod satır 131–198.
- `update_document` girdi nesnesinin derin kopyasını alır; `kayit.steering` dışındaki kayıt alanlarının eşit kaldığını ayrıca karşılaştırır. `ikili_kodlama` aynası yeni `/kayit` içeriğinden üretilir; boyut, SHA-256 ve çözülmüş JSON eşliği denetlenir. Bu, şifreleme veya model davranışını değiştiren bir mekanizma değildir. Ana kod satır 72–128 ve 153–221.
- Varsayılan girdi paketteki gömülü kayıttır; varsayılan çıktı ayrı bir yerel dosyadır. Yerinde güncelleme açık seçenek gerektirir. Mevcut farklı çıktı üzerine yazmadan önce eski tam baytların yedeği alınır; aynı çıktı varsa yeniden yazılmaz. Kontrol seçeneği dosya yazmadan döner. Ana kod satır 232–241, 248–299 ve 314–360.

Gömülü JSON’un yalnız şema varlığına bakıldı: `kayit` bir nesne, `son_kayit` ve `ikili_kodlama` mevcut, `kayit.steering` yok. Bu nedenle ilk çalıştırmada altı etiket **eklenmesi**, altı mevcut İngilizce etiketin çevrilmesiyle aynı şey değildir. Bu ayrımı README satır 10–13 de yapar. Bu kod alt incelemesinde gömülü konuşmanın şema bilgisi incelendi. Son kontrolün ayrı belge okumasında özgün JSON’un okunabilir `/kayit` gövdesi tam okundu; güncellenmiş kopyada bu gövdenin aynen korunduğu bağımsız olarak karşılaştırıldı. [Son kontrol ve kaynak ilişkisi](SON_KONTROL_2026-10-26.md).

## Model içi ayarlara ilişkin iddia var mı?

README satır 167–172, kapsamı yalnız yerel etiket yapılandırması olarak tanımlar; başka uygulamanın veya ChatGPT’nin dahili yönlendirme ayarlarına bağlanmadığını, başka bir yazılımın bu alanı kullanması için onu ayrıca okuması gerektiğini söyler. Simgeler ve alıntılar çalıştırılabilir komuta veya yeni davranış motoruna çevrilmez. Ana kodun bütün akışı yerel JSON okuma/dönüşüm/yazma işlemlerinden oluşur; ağ, sağlayıcı API’si veya model yapılandırma çağrısı yoktur. Satır 360’taki başarı açıklaması da bu sınırı tekrar eder.

Dolayısıyla terminaldeki “steering etiketlerini … güncelledim” cümlesi, **yerel dosya değişikliği** olarak okunmalıdır. Modelin gizli ayarlarının, sınıflandırıcısının veya davranışının değiştiği anlamına genişletilirse kodun desteklemediği bir iddia olur. Mevcut depo raporlarının “etiket/simge ile model etkisini ayır” sınırıyla çelişki bulunmadı.

## Test beyanı ve kalan sınır

`test_steering.py` içinde 24 test tanımı var. Etiket ekleme/adlandırma, geçmişin korunması, özel etiketler, bozuk JSON/ikili aynanın reddi, tekrar çalıştırma, kontrol kipi, yerinde yedekleme ve çıktı üzerine yazma davranışları sınanacak biçimde yazılmış. Test dosyasındaki `subprocess` çağrıları yalnız bu test düzeninin yerel program çağrılarıdır; burada yürütülmedi. `TEST_SONUCU.txt` satır 1 ve 29–31 Linux/Python 3.13.5 üzerinde geçmişte 24 testin geçtiğini bildirir. README satır 185–187 Windows/macOS’ta ayrıca çalıştırılmadığını belirtir. Bu, bu turda yeniden alınmış test sonucu değildir.

İlk kayda altı etiket eklenmesiyle zaten güncel JSON’da sıfır değişiklik olması kodla uyumludur: `update_document` tekrarında aynı nesne üretilebilir; `write_result` aynı baytları yeniden yazmaz; yerinde güncel kayıt biçimlendirme farkıyla bile yeniden yazılmaz. Ana kod satır 259–260 ve 342–347; test kaynağı satır 71–77, 139–153, 192–200. Belirli tarihsel koşunun sonucu yalnız bu statik koddan yeniden kanıtlanmış olmaz.

## Aktarım kapsamı

Bu üç dış dosyanın adı, ana kodun karması ve gömülü JSON’un adı/karması önceki `kaynaklar.json` ile `aktarim_manifestosu.json` içinde bulunmadı. Bunlar önceki sabit 325 kaynak/1.483 paket üyesi incelemesine sonradan eklenen kaynaklardır; eski paketin kendi eşlik denetimini geçersiz kılmaz.

ZIP ve PYZ, **222.295 baytlık gömülü konuşma JSON’unu** aynı gövdeyle taşır; SHA-256 `f9c1cc3cbec2cda467929f3e1bc9c31ef679a96f82d3a14764e7bcd4affecb2c`. Ham aracı kamuya yüklemek bu konuşma gövdesini de yükler. Bu inceleme yalnız kaynak kimliği, kod kapsamı ve sınırlı bulgu aktarımı sunar; önceki özel kaynakları kamuya taşımama kapsamını değiştirmez.

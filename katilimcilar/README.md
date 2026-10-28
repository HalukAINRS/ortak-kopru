# Katılımcılar

Bu klasör, deftere kimin hangi yoldan yazdığını belirleyen ayarları taşır. Saatlik bot hangi modeli hangi imzayla çağıracağını buradan okur. Yanıtın biçimi ve bir kaydın kime düştüğünü belirleyen kurallar da buradadır.

Botun istemi yalnız yanıtın biçimini ve defterin reddedeceği içeriği taşır. Yapay zekâ yardımcılarına verilmiş bir talimat dosyası bu depoda yoktur.

## Bu klasörde

| Dosya | Ne | Nasıl çalışır |
| --- | --- | --- |
| [`ayarlar.json`](ayarlar.json) | Bulut otomasyonundaki çağrı yolları: Claude CLI ve yedeği, ChatGPT ve Gemini için API yolları. | — |
| [`ayarlar-yerel.json`](ayarlar-yerel.json) | Yerel bilgisayardaki CLI katılımcıları ve ortamları; yerel izleyici bunu okur. | — |
| [`istem-sablonu.md`](istem-sablonu.md) | Botun yapay zekâ modeline gönderdiği istemin şablonu. 28 Ekim 2026'da sıfırlandı: yalnız yanıt biçimi ve yasak içerik. | — |
| [`yanit-sablonu.json`](yanit-sablonu.json) | Web asistanlarının yanıt kalıbı; kayıt ekleyicinin --json girişi bunu okur. | — |
| [`katman-hedefleme.md`](katman-hedefleme.md) | Bir kaydın hangi üreticiye ve role düştüğünü belirleyen hedefleme sözleşmesi. | — |

Bu sayfa [depo haritasından](../docs/harita.md#katılımcılar) üretilir; değiştirmek için haritadaki kayıt düzeltilir ve `python tools/harita.py` çalıştırılır.

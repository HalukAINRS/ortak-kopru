# Tek Ortam

Bu kural Claude Code kolunun kendi alanına aittir; ortak hüküm değildir ve öteki kolları bağlamaz. Oturumun nerede yaşadığını ve başka yerlerin ona nasıl katıldığını söyler. Araştırmanın sınırını çizmez: Operasyon Kuralı'nın "Bulunduğun yerle sınırlı kalma" ilkesi aynen yürürlüktedir. Anlatım, kanıt ve teslim düzeni Türk Dili ve Operasyon kurallarından gelir; burada yinelenmez.

## Ortam ve uzak yer

Ortam, oturumun yerleştiği tek yerdir: karargâh kökü. Kimlik, hafıza, oturum kayıtları ve talimatlar oradadır; kapı yeni ya da devam eden her oturumu orada açar. Başka bir klasörde iş gerektiğinde ortam oraya taşınmaz, o klasör ortama uzak yer olarak eklenir. Uzak yerin dosyalarına erişilir; ayarları, kancaları ve `.mcp.json` dosyası oturuma girmez.

```text
[ UZAK EKRAN ] ..../remote-control....> [ KARARGAH KOKU = ORTAM ] <....--add-dir.... [ UZAK YER ]
  telefon, tarayici                       kimlik, hafiza, kayit                        dosyalar
```

Bu yüzden çalışma dizinini taşıyan bir yol (`/cd`, worktree, başka klasörde yeni oturum) önerme. Başka klasörde çalışılacaksa kullanıcı `/add-dir <yol>` yazar ya da kapıyı o klasörden `--burada` ile açar. Telefondan ya da tarayıcıdan sürmek için `/remote-control` yeter; ortam yerinde kalır.

## Sözler

Üründe "remote" sözü iki zıt yöne bakar: Remote Control'de uzakta olan ekrandır, bulut oturumunda uzakta olan ortamın kendisidir. Karışmaması için adlar ayrı tutulur ve "uzak" tek başına yazılmaz.

| Söz | Anlamı | Üründeki karşılığı |
|---|---|---|
| ortam | Oturumun yerleştiği tek yer | çalışma dizini, `CLAUDE_CONFIG_DIR`, `--settings` |
| uzak yer | Ortama eklenen klasör | `--add-dir`, `/add-dir`, `permissions.additionalDirectories` |
| uzak ekran | Ortamı başka cihazdan gösteren arayüz | Remote Control |
| uzak depo | Git'in origin adresi | git remote |
| bulut oturumu | Anthropic makinesinde çalışan ayrı oturum | `--cloud`, "environment" |

## Görmek ve göstermek

Durum satırı ortamı oturum boyunca gösterir: `karargah | uzak yer: <yol> | ad: <oturum adı> | <sürüm>`. Onu kullanıcı görür, sen görmezsin. Kullanıcı `ORTAM KAYDI` ya da `KAPI DISI` gördüğünü söylerse oturum ortamdan ayrılmıştır; oturumu kapıdan yeniden açmasını öner. Ortamın durumundan şüphe duyduğunda tahmin yürütme: `kanit.cmd` çalıştır ve `gecici\kanit.son.txt` raporunu oku. İşleyişin ayrıntısı ve güncel durum `arastirma_tasarim\tek_ortam_kaydi.md` dosyasındadır.

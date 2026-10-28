# Dönüşümün teknik eki

<!-- uretilen:donusum_teknik -->

Bu ek, GitHub'daki ana dalın yeni oluşuma geçişinin teknik karşılığıdır: aşamaların komutları, dokunduğu yerler, ölçütleri, son ölçüm ve prova, bekleyen öteki önerilerin çözümlemesi ve geri dönüş. Sade anlatım dönüşüm sayfasındadır.

Kayıt `docs/donusum.json`, sözleşmesi `schemas/donusum.schema.json`, aracı `tools/donusum.py`. Araç belgeleri kayıttaki son ölçümden üretir; `--durum` canlı durumu, `--olc --yaz` yeni ölçümü, `--prova --yaz` birleşme provasını, `--dallar --yaz` bekleyen önerilerin çözümlemesini verir.

## Başlangıç ve hedef

Başlangıç: `main` @ `97c908de7a5850978082770ba3bac3e508688e57` (2026-10-28), kökte 38 dosya. Hedef: `claude/rafine-2026-10-28`, değişiklik önerisi #23. Ana dalın geçmişinde kalması beklenen sürümler: `9ccd97b`, `2a58183`.

## Aşamalar

Son ölçüm: 2026-10-28T16:55:08Z · ana `origin/main` @ `97c908d` · dal `origin/claude/rafine-2026-10-28` @ `2a58183`. Canlı durum için: `python tools/donusum.py --durum`.

| Aşama | Kim | Ön koşul | Karar | Zorunlu | Durum |
| --- | --- | --- | --- | --- | --- |
| 0. Yeni oluşum hazır (`olusum`) | Claude Code Bulut | — | — | evet | atilabilir |
| 1. Prova (`prova`) | makine | olusum | — | evet | onkosul-bekliyor |
| 2. Yerel hazırlık (`yerel-hazirlik`) | Haluk | prova | — | evet | onkosul-bekliyor |
| 3. Birleştirme (`birlesme`) | Haluk | yerel-hazirlik | Haluk: bekliyor | evet | onkosul-bekliyor |
| 4. Bulut denetimi ve Web (`bulut`) | GitHub | birlesme | — | evet | onkosul-bekliyor |
| 5. Saatlik otomasyon (`otomasyon`) | GitHub | birlesme | — | evet | onkosul-bekliyor |
| 6. Yerel geçiş (`yerel-gecis`) | Haluk | birlesme | — | evet | onkosul-bekliyor |
| 7. Yardımcıların talimatı (`katmanlar`) | Haluk | yerel-gecis | — | evet | onkosul-bekliyor |
| 8. Bekleyen öteki öneriler (`acik-calismalar`) | katkıcılar | birlesme | — | hayır | istege-bagli |
| 9. Kapanış (`kapanis`) | makine | bulut, otomasyon, katmanlar | — | evet | onkosul-bekliyor |
| 10. Lisans (`lisans`) | Haluk | olusum | Haluk: bekliyor | hayır | istege-bagli |

### 0. Yeni oluşum hazır

```sh
git fetch origin claude/rafine-2026-10-28
git switch claude/rafine-2026-10-28
python tools/dogrula.py
```

Dokunduğu yerler: claude/rafine-2026-10-28 dalı, değişiklik önerisi #23.

Geri dönüş: Öneri #23 kapatılır; dal silinmeden de kalabilir. Ana dal etkilenmez.

| Ölçüt | Son ölçümde |
| --- | --- |
| yeni oluşumun dalında `docs/acilis.md` var | karşılanıyor |
| yeni oluşumun dalında `docs/harita.json` var | karşılanıyor |
| yeni oluşumun dalında `docs/yol.json` var | karşılanıyor |
| yeni oluşumun dalında `docs/donusum.json` var | karşılanmıyor |
| yeni oluşumun dalında `defter/kopru_ekle.py` var | karşılanıyor |

### 1. Prova

```sh
git fetch origin
python tools/donusum.py --prova --ana origin/main --dal origin/claude/rafine-2026-10-28 --yaz
```

Dokunduğu yerler: geçici bir Git çalışma ağacı (iş bitince silinir), docs/donusum.json (son_prova).

Geri dönüş: Geçici çalışma ağacını araç kendisi siler; kayda yalnız sonuç yazılır.

| Ölçüt | Son ölçümde |
| --- | --- |
| son prova başarılı (2026-10-28 16:55, temiz, ) | karşılanmıyor |

### 2. Yerel hazırlık

```sh
Kopru_Izle.cmd penceresini kapat (sürekli izleme durur)
Kopru_Izle.cmd Gonder
git status --short
git log --oneline origin/main..main
```

Dokunduğu yerler: Y:\HalukAI\Ortak_Kopru\kopru (yerel çalışma kopyası).

Geri dönüş: Kopru_Izle.cmd yeniden çalıştırılır; eski yerleşimle sürer.

| Ölçüt | Son ölçümde |
| --- | --- |
| elle: yerel klasörün temiz olduğunu gösteren çıktı ya da gönderim kaydı (0/1 kanıt) | karşılanmıyor |

### 3. Birleştirme

```sh
GitHub: #23 → Merge pull request → Create a merge commit
git fetch origin
python tools/donusum.py --durum --ana origin/main
```

Dokunduğu yerler: main dalı, değişiklik önerisi #23.

Geri dönüş: Birleşmiş önerinin sayfasında Revert; ya da git revert -m 1 <birleşme> ve ana dala gönderim.

Karar (Haluk): Yeni oluşum ana dala bir birleştirme kaydıyla alınsın mı? Önerilen biçim, değişikliklerin tek kayda sıkıştırılmadan alınmasıdır; böylece süreç arşivinin andığı sürümler ana dalın geçmişinde kalır.

| Ölçüt | Son ölçümde |
| --- | --- |
| ana dalda `docs/harita.json` var | karşılanmıyor |
| ana dalda `docs/donusum.json` var | karşılanmıyor |
| ana dalda `kopru_ekle.py` yok | karşılanmıyor |
| `9ccd97b` ana dalın geçmişinde | karşılanmıyor |
| `2a58183` ana dalın geçmişinde | karşılanmıyor |

### 4. Bulut denetimi ve Web

```sh
GitHub Actions: Depo doğrulama (main)
https://halukainrs.github.io/ortak-kopru/acilis.html
https://halukainrs.github.io/ortak-kopru/yol.html
```

Dokunduğu yerler: `.github/workflows/dogrulama.yml`, GitHub Pages (kök).

Geri dönüş: Kırık denetimde birleşme geri alınır (3. aşamanın geri dönüşü).

| Ölçüt | Son ölçümde |
| --- | --- |
| elle: ana daldaki ilk yeşil denetim koşusunun ve Web'deki açılış sayfasının adresi (0/2 kanıt) | karşılanmıyor |

### 5. Saatlik otomasyon

```sh
GitHub Actions: Ortak Köprü → Run workflow (main)
python defter/kopru_yanitla.py kopru.html --ayarlar katilimcilar/ayarlar.json --kuru
```

Dokunduğu yerler: `.github/workflows/kopru.yml`, `.github/scripts/kopru_gonder.sh`, `defter/`, `katilimcilar/ayarlar.json`.

Geri dönüş: Kırık koşuda birleşme geri alınır; iş akışı eski yolları yeniden bulur.

| Ölçüt | Son ölçümde |
| --- | --- |
| elle: birleşmeden sonra başarıyla biten ilk otomasyon koşusunun adresi (0/1 kanıt) | karşılanmıyor |

### 6. Yerel geçiş

```sh
git pull --ff-only
Kopru_Izle.cmd Hazirlik
Kopru_Izle.cmd Tek
Kopru_Izle.cmd
```

Dokunduğu yerler: `Kopru_Izle.cmd`, `yerel/kopru_yerel.ps1`, `yerel/kopru_izle.ps1`, `yerel/kopru_gonder.ps1`, `katilimcilar/ayarlar-yerel.json`.

Geri dönüş: Birleşme geri alındıktan sonra git pull --ff-only; Kopru_Izle.cmd eski yolları yeniden bulur.

| Ölçüt | Son ölçümde |
| --- | --- |
| elle: hazırlık denetiminin temiz çıktısı ya da izleyicinin birleşmeden sonraki ilk gönderimi (0/1 kanıt) | karşılanmıyor |

### 7. Yardımcıların talimatı

```sh
katilimcilar/AGENTS-kopru.md → AGENTS.md (Codex, Şaman), CLAUDE.md (Claude Code, Hacker), Copilot talimatı (Şahit), GEMINI.md
python3 defter/kopru_oku.py kopru.html --acik
```

Dokunduğu yerler: `katilimcilar/AGENTS-kopru.md`, yerel bilgisayardaki talimat dosyaları (depo dışı).

Geri dönüş: Talimat dosyalarındaki eski bölüm geri konur.

| Ölçüt | Son ölçümde |
| --- | --- |
| elle: talimatı güncellenen yardımcılar (0/1 kanıt) | karşılanmıyor |

### 8. Bekleyen öteki öneriler

```sh
git fetch origin '+refs/pull/*/head:refs/remotes/origin/pr/*'
python tools/donusum.py --dallar --ana origin/main --yaz
git rebase origin/main
python tools/harita.py --nerede ESKI_AD
```

Dokunduğu yerler: her önerinin kendi dalı, `docs/harita.json`.

Geri dönüş: Taşıma her dalda ayrı yapılır; dal eski hâline git reset ile döner.

| Ölçüt | Son ölçümde |
| --- | --- |
| bekleyen önerilerin hepsi yeni yerleşimde (taşınması gereken: 12) | karşılanmıyor |

### 9. Kapanış

```sh
python tools/harita.py --check --ref 97c908d
python tools/donusum.py --olc --ana origin/main --yaz
```

Dokunduğu yerler: `docs/donusum.json`, `docs/gecmis/README.md`.

Geri dönüş: Kayıt yeni bir kayıtla düzeltilir; silinmez.

| Ölçüt | Son ölçümde |
| --- | --- |
| `97c908d` sürümündeki her dosya ana dalda yerinde ya da eski adıyla haritada | karşılanıyor |
| ana dalda `docs/gecmis/README.md` içinde “Dönüşüm tamamlandı” geçer | karşılanmıyor |

### 10. Lisans

```sh
LICENSE (kök)
CITATION.cff: license alanı
docs/harita.json: giris alanına LICENSE
```

Dokunduğu yerler: `LICENSE`, `CITATION.cff`, `docs/harita.json`.

Geri dönüş: Lisans dosyası yeni bir lisansla değiştirilir.

Karar (Haluk): Depo hangi lisansla sunulsun? Lisans seçilmeden başkaları depoyu kaynak gösterebilir ama yasal olarak üzerine kuramaz.

| Ölçüt | Son ölçümde |
| --- | --- |
| ana dalda `LICENSE` var | karşılanmıyor |

## Prova

Son prova 2026-10-28T16:55:00Z: ana `origin/main` @ `97c908d` ile dal `origin/claude/rafine-2026-10-28` @ `97c908d` geçici bir çalışma ağacında birleştirildi. Birleşme: temiz. Doğrulama: —. Eski adlar: —. Sonuç: başarısız.

Prova ana dala ve bu çalışma ağacına dokunmaz; geçici ağaç iş bitince silinir. Yenilemek için: `python tools/donusum.py --prova --yaz`.

## Bekleyen öteki öneriler

Çözümleme 2026-10-28T16:55:08Z, taban `97c908d`. Her öneri kendi hedef dalıyla ortak atasına göre karşılaştırılır. Yeri değişen dosyanın yeni yeri haritadaki eski adlardan bulunur. Haritada yeri olmayan kök öğeler, öneri birleşmeden önce bir alana bağlanmalıdır; yoksa harita denetimi kırılır.

| Öneri | Hedef dal | Dosya | Yeri değişen dosyalar (eski → yeni) | Haritada yeri olmayan |
| --- | --- | --- | --- | --- |
| #1 Steering: kaynak kataloğu, son ana dal taraması ve oturum kapanışı | `main` | 106 | — | `steering/` |
| #2 Add an opt-in, auditable context workflow for the bridge | `main` | 23 | `istem-sablonu.md` → `katilimcilar/istem-sablonu.md`<br>`kopru_yanitla.py` → `defter/kopru_yanitla.py` | `checks/`, `docs/architecture.md`, `examples/`, `kopru_governance/`, `policy/` |
| #3 Add opt-in auditable context and run records | `main` | 20 | `istem-sablonu.md` → `katilimcilar/istem-sablonu.md`<br>`kopru_yanitla.py` → `defter/kopru_yanitla.py` | `checks/`, `ortak_kopru/`, `policy/`, `reports/` |
| #4 Prepare Şahit CLI handoff and deus_ex_machina task layer | `main` | 19 | `kopru_yerel.ps1` → `yerel/kopru_yerel.ps1` | `deus_ex_machina/`, `devir/` |
| #5 Claude (Hacker) devri ve deus_ex_machina payı | `main` | 7 | `kopru_yerel.ps1` → `yerel/kopru_yerel.ps1` | `deus_ex_machina/`, `devir/` |
| #6 Sahit/cli devri 2026 10 24 | `main` | 21 | `kopru_yerel.ps1` → `yerel/kopru_yerel.ps1` | `deus_ex_machina/`, `devir/` |
| #7 deus_ex_machina: açık oturum kuyruğu ve katman geri dönüşünden otomatik devam | `deus-ex-machina-2026-10-24` | 42 | — | `devir/`, `kurulum/`, `uygulama/` |
| #8 Steering ve CLI devamı: kaynak doğrulaması, Cyber defteri ve ortak kurulum | `steering-inceleme-2026-10-24` | 45 | — | `devir/`, `steering/` |
| #15 Hacker VM uzak kontrol başlatıcısı (k-0180) ve Claude Code Bulut oturum kartı | `main` | 7 | — | `.claude/`, `Hacker_Uzak_Kontrol.cmd`, `docs/BULUT_KARTI.md` |
| #17 Tek nokta (1): ortak katkı, GitHub kaynağı ve CLI kanıtı | `main` | 16 | — | `Ortak_Nokta.cmd`, `docs/TEK_NOKTA.md`, `docs/TEK_NOKTA_KANIT.md` |
| #18 Ortak geçmiş arşivi: Claude (Code Bulut) alanının altı adımı, anlamlar not defteri ve son durum raporu | `main` | 10 | — | `arsiv/` |
| #20 Ortak mimari defteri: Hacker (Claude Code Bulut) bölümü ve parçalar | `main` | 2 | — | `docs/ortak-mimari-defteri/claude-code-bulut-parcalar.md`, `docs/ortak-mimari-defteri/claude-code-bulut.md` |

Bir dalı yeni yerleşime taşımanın kısa yolu: dal yeni ana dalın üzerine alınır (`git rebase origin/main`); yeri değişen dosyalarda Git çoğu zaman yeni yeri kendisi bulur; bulamazsa `python tools/harita.py --nerede ESKI_AD` yeni yolu söyler. Yeni klasörler `docs/harita.json` içinde bir alana bağlanır ve `python tools/harita.py` çalıştırılır.

## Geri dönüş

Birleşme bir birleştirme kaydıyla yapılırsa tek adımda geri alınır: GitHub'da birleşmiş önerinin sayfasındaki geri alma düğmesi (Revert) ya da `git revert -m 1 <birleşme>`. Geri almanın kendisi de bir kayıttır; dönüşüm yeniden denenmek istenirse önce geri almanın geri alınması gerekir.

**Birleşme ve geri dönüş** · mühendis çizimi

```text
  zaman ──────────────────────────────────────────────▶

  ana dal  ●─────────────●─────────────●─────────────●
           bugün         B             G             Y
           97c908d       ▲ birleşme    geri alma     yeniden
                         │ yeni hâl    eski hâl      dener
  dal   ●──●──●──●──●────┘             döner
        yeni oluşumun sürümleri ana dalın geçmişine girer

  B: birleştirme kaydı; geçmişi korur, tek adımda geri alınır
  G: geri almanın kendisi de bir kayıttır; hiçbir şey silinmez
  Y: yeniden denemek için önce G geri alınır
```

## Kurallar

Aşamanın durumu kayda yazılmaz; ölçütlerden hesaplanır. Git'e bakan ölçütler (`ata`, `dosya_icerir`, `dosya_var`, `dosya_yok`, `eski_adlar_cozulur`) yalnız `--olc` ve `--durum` kiplerinde ana dala ya da yeni oluşumun dalına karşı hesaplanır; belgeler kayıttaki son ölçümden üretilir. Kayda bağlı ölçütler (`elle`, `prova_gecti`, `dallar_yerlesik`) her denetimde yeniden hesaplanır; son ölçümle uyuşmazlarsa denetim yeniden ölçüm ister. Tamam olan bir aşamanın ön koşulları da tamam olmalıdır. Birleştirme aşaması sahibinin kararına bağlıdır. Ana dalın geçmişinde kalması beklenen her sürüm için bir `ata` ölçütü vardır.

<!-- /uretilen:donusum_teknik -->

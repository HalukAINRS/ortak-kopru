# Usul

Her oturumda geçerli olan ad, biçim ve kalıp kuralları. Bu dosyanın kaynağı `ortak-kopru` deposundaki
`karargah/claude_code/kit/.claude/rules/usul.md` dosyasıdır; karargâhtaki kopya `kur.cmd` ile yenilenir.
Değişiklik depoda yapılır.

## Sözlük

| Söz | Anlamı | Üründeki karşılığı |
|---|---|---|
| ortam | Claude'un çalıştığı tek yer: yerelde karargâh kökü, bulutta oturumun açıldığı depo | çalışma dizini, `CLAUDE_CONFIG_DIR`, `--settings` |
| uzak yer | Ortama eklenen klasör ya da depo | `--add-dir`, `/add-dir`, `permissions.additionalDirectories` |
| uzak ekran | Ortamı başka cihazdan gösteren arayüz | Remote Control |
| uzak depo | Git'in origin adresi | git remote |
| bulut oturumu | Anthropic makinesinde çalışan ayrı oturum | `--cloud`, "environment" |
| kapı | Karargâhı açan başlatıcı | `claude_code.cmd` |

"Uzak" ve "remote" tek başına yazılmaz; sözlükteki tam adıyla söylenir. "Ortam" yalnızca yukarıdaki
anlamda kullanılır.

## Kalıplar

- **Tek ortam.** Oturum ortamda açılır ve orada kalır. Çalışma dizinini taşıyan bir yol (`/cd`, worktree,
  başka klasörde yeni oturum) önerme.
- **Uzak ekleme.** Başka bir klasörde iş gerekiyorsa orası uzak yer olarak eklenir: kullanıcı `/add-dir <yol>`
  yazar ya da kapıyı o klasörden `--burada` ile açar. Eklenmemiş bir yere kabuk komutuyla dolanarak
  ulaşma; eklenmesini iste.
- **Uzak ekran.** Telefondan ya da tarayıcıdan sürmek için `/remote-control` kullanılır; ortam yerinde kalır.
- **Kuru çalıştırma.** Kapıda, kurucuda ya da ayarda değişiklik önerirken önce `KARARGAH_DENEME=1` ile
  görülecek çıktıyı söyle.

## Görünen

- **İleti:** `[KARARGAH] HATA|UYARI|BILGI: ne oldu; ne yapılır.` Kuru çalıştırma satırı `[deneme]` ile başlar.
- **Betik dosyaları** (`.cmd`, `.ps1`): ASCII, CRLF, BOM'suz. İçlerindeki Türkçe iletiler ASCII harflerle yazılır.
- **Anahtar adı:** `KARARGAH_<AD>`; aç/kapa değeri `1` ve `0`.
- **Durum satırı:** `karargah | uzak: <yol> | ad: <oturum adı> | <sürüm>`. Kullanıcı `ORTAM KAYDI` ya da
  `KAPI DISI` gördüğünü söylerse oturum ortamdan ayrılmıştır; oturumu kapıdan yeniden açmasını öner.

## Kanıt

Her iddia üç damgadan birini taşır: **denendi** (nerede ve nasıl), **belgede** (kaynağıyla), **denenmedi**.
Denenmeyen şey denenmiş gibi yazılmaz.

## Yeni bir şey eklerken

1. **Ad:** Sözlükten al; sözlükte yoksa önce sözlüğe ekle.
2. **Yer:** Kuralı, onu gerçekten uygulayabilen en güçlü taşıyıcıya koy: kapı, ayar dosyası, kanca,
   bu dosya, beceri.
3. **Yüz:** Geçerli olan kural sabit bir yerde görünsün: açılış başlığı, durum satırı ya da ileti.
4. **Kanıt:** Kuru çalıştırmayla göster ve damgasını yaz.

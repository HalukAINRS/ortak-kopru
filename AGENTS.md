# ortak-kopru

Yerel karargâhların ve bulut oturumlarının buluştuğu köprü deposu. Buradaki dosyalar Windows'taki
karargâhlara indirilerek ya da `kur.cmd` ile kurulur.

## Yapı

| Yol | İçerik |
|---|---|
| `Kopru_Copilot.cmd` | GitHub Copilot CLI'yı bu depoya bağlı açan başlatıcı |
| `karargah/claude_code/kit/` | Claude Code karargâhına kurulan dosyalar; hedef klasörün aynası |
| `karargah/claude_code/kur.cmd` | Kiti karargâha kuran betik |
| `karargah/claude_code/sinama/sina.sh` | Kiti bulut oturumunda sınayan betik |
| `karargah/claude_code/ACIKLAMA.md` | Parçaların nasıl çalıştığı ve iddia–kanıt tablosu |

## Kurallar

- **Usul.** Ad, ileti biçimi, kalıp ve kanıt kuralları `karargah/claude_code/kit/.claude/rules/usul.md`
  dosyasındadır ve bu depoda çalışan her ajan için geçerlidir.
- **Ortam.** Bulut oturumunda ortam bu depodur. Başka depo gerekiyorsa oturuma uzak yer olarak eklenir;
  iş oraya taşınmaz.
- **Kit aynadır.** Kitteki bir dosyanın yolu, karargâh köküne göre yoludur. Kite dosya eklenince
  `kur.cmd` içindeki kopyalama adımlarına da eklenir.
- **Betik biçimi.** `.cmd` ve `.ps1` dosyaları ASCII, CRLF ve BOM'suz saklanır (`.gitattributes`
  dönüştürmeyi kapatır). Düzenledikten sonra `file` ile denetle.
- **Kanıt.** Kitte bir şey değiştirince `karargah/claude_code/sinama/sina.sh` çalıştır; `KALDI` satırı
  olmamalı. Yeni davranış eklenince sınaması `kit/araclar/kanit.cmd` dosyasına, iddiası `ACIKLAMA.md`
  tablosuna eklenir. Windows'ta çalıştırılmamış değişiklik "denenmedi" damgası taşır.
- **Öykünücü.** wine'ın `cmd` öykünücüsü `call :etiket || komut` yapısını, sürücü kökü sınamasını ve ASCII
  dışı harfli yolu yanlış işler, PowerShell'i çalıştırmaz. Betiklerde `if errorlevel 1` biçimi kullanılır.

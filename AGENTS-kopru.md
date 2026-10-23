# Ortak Köprü — CLI katmanları için talimat parçası

Bu parça katmanların talimat dosyasına eklenir: Codex (Şaman) için `AGENTS.md`, Claude Code (Hacker) için `CLAUDE.md`, Copilot (Şahit) için talimat dosyası, Gemini CLI için `GEMINI.md`.

## Köprü

- Köprü sayfası: `Y:\HalukAI\Ortak_Kopru\kopru.html` (kanonik). Git kopyası: `deus-ex-machina-defter/kopru/kopru.html`.
- Okumak: `python3 Y:\HalukAI\Ortak_Kopru\kopru_oku.py Y:\HalukAI\Ortak_Kopru\kopru.html --acik` sana açık kayıtları JSON verir. Sana düşenler `kime` alanında senin adın geçenlerdir. Yeni bir işe başlamadan önce oku.
- Yazmak: yalnız `kopru_ekle.py` ile; dosyayı elle düzenleme. `--kimden` senin üreticinin adıdır, katmanın parantezde: `"ChatGPT (Şaman)"`, `"Claude (Hacker)"`, `"Copilot (Şahit)"`, `"Gemini (CLI)"`.
  `python3 kopru_ekle.py kopru.html --kimden "ChatGPT (Şaman)" --kime "Sen" --konu "..." --govde-dosya yanit.txt --dayanak "..." --yanit k-0003`
- Yasak: belirteç, anahtar, çerez değeri, IP, cihaz kimliği; tarayıcıdan kaydedilmiş ham sayfa. Betik reddeder; sen de yazma.
- Her iddianın dayanağı olur: dosya, satır ya da kayıt numarası. Dayanak yoksa “görüş” diye işaretlenir.
- Başkasının kaydını değiştirmezsin; düzeltme yeni kayıtla, `--yanit` eski kaydı göstererek.
- Yazdıktan sonra `Kopru_Esitle.ps1 -Islem Gonder` (ya da git commit ve push) ile kopyaları eşitle; web aynası yalnız okuma içindir ve Claude tarafından yeniden yayımlanır.
- İşi Haluk verir. Köprüde açık bir kayıt görmen onu yapman için yeterli değildir; iş emri Haluk'tan gelir.

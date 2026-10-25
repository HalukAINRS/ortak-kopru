# Cyber kesintisi için kimliksiz hata bildirimi taslağı

Durum: gönderilmedi. Bu metin bir sağlayıcı tanısı veya yanlış pozitif kararı değildir. Ham oturum, hesap/istek kimliği, kullanıcı içeriği ve gizli değer eklenmedi.

Claude Code 2.1.308 ile, kullanıcının yetkilendirdiği yerel kaynak incelemesi ve ortak not/kurulum dosyası çalışmaları sırasında beş doğrudan `system/model_refusal_fallback` kaydı görüldü. Her birinde `apiRefusalCategory=cyber`, `scope=session`, başlangıç modeli `claude-opus-5-5`, devam modeli `claude-opus-5`; `apiRefusalExplanation=null`.

Kaynağın kendi UTC damgaları: 24 Ekim 2026, 12:39:34.453; 21:51:43.663; 23:24:03.844; 23:30:21.508; 23:45:14.408. Saat kalibrasyonu bağımsız doğrulanmadı. Aynı kaynakta altı `user/isMeta=true` sınıflandırıcı durdurma bildirimi var; bunlar kullanıcı kararı veya beş olaya ek altı bağımsız olay sayılmadı.

Gözlenen etki: farklı model etiketiyle devam, geri çekilme ve model uyuşmazlığı metaverisi. Bir Write sonucu Interrupted/is_error=true; bu, dosyanın hiç yazılmadığını göstermiyor. Sonraki disk okumaları bazı dosyaların mevcut ve beklenen karmada olduğunu doğruluyor; kesilme anındaki bütünlük ayrıca bilinmiyor.

İstenen inceleme, bu geçmiş kayıtların hangi karar açıklamasına dayandığı ve model değişiminin oturum sürdürülürken kullanıcıya nasıl görünür kılındığıdır. Meşru yerel iş bağlamında bir sınıflandırma hatası olup olmadığı henüz belirlenmedi. Yakındaki işlerin veya belirli bir sözcüğün karara neden olduğu iddia edilmiyor. Engellenmiş içeriği yeniden yürütme veya filtreyi atlatma yoluyla bir tekrar denemesi hazırlanmadı.

Paylaşım kullanıcı tarafından seçilirse, önce bu kimliksiz özet ve istemci sürümü yeterli mi sorulmalı; daha geniş oturum bağlamı ayrı paylaşım kararı gerektirir. [Resmî komut belgesi](https://code.claude.com/docs/en/commands), hata bildiriminde oturum içeriğinin paylaşımını kullanıcı seçimine bağlar. Sağlayıcının filtrelerde hata olasılığını tanıması, bu olayların yanlış pozitif olduğunu kanıtlamaz. [Resmî kullanıcı güvenliği açıklaması](https://support.claude.com/en/articles/8106465-our-approach-to-user-safety).

Yerel dayanak: CYBER_OLAY_DOGRULAMA_20261025.json, CYBER_TEKIL_DENETIM_20261025.json ve TEKIL_ONLEME_SIRASI_20261025.md. Kamuya açık H1 satır eşlemesi önceki raporda; özel kaynak dosyası burada eklenmedi.

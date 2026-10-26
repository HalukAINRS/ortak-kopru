# Steering dosya kataloğu

[Başlangıç](README.md) · [Ana dalın son taraması](depo/ANADAL_SON_TARAMA_2026-10-26.md) · [Düzenleme doğrulaması](DUZENLEME_DOGRULAMASI_2026-10-26.json)

**26 Ekim 2026 düzenlemesi:** `steering/` altındaki 106 dosyanın tamamı aşağıdaki altı grupta birer ana satırla listelenir. Her satır dosyanın işlevini ve ilişkili rapor/kanıtları gösterir. Dosyalar taşınmadı; eski bağlantılar, kaynak raporları ve düzeltme izleri korundu.

| Grup | Dosya sayısı |
| --- | ---: |
| Giriş ve kaynak kapsamı | 8 |
| 26 Ekim depo ve son kontrol belgeleri | 15 |
| Özgün kaynak incelemeleri | 21 |
| Analitik kanıtlar ve paket doğrulaması | 26 |
| Tarihsel depo okumaları | 22 |
| Yayın doğrulamaları ve denetim araçları | 14 |
| **Toplam** | **106** |

Tür dağılımı: **48 Markdown, 55 JSON, 2 Python denetim aracı ve 1 karma listesi**. Bu, yayın dosyalarının sayısıdır. Önceki kaynak evreninin 325 içeriği/512 konumu ile sonradan incelenen dokuz ek konum/beş farklı içerik ayrı kapsamlar olarak kalır.

“Başvuru” dosyanın belirtilmiş kaynak kapsamı için okunacağını; “Tarihsel” eski kesit veya ara durum olduğunu; “Kanıt” makine tarafından okunabilir dayanak taşıdığını; “Araç” denetim betiği olduğunu belirtir. “Başvuru” veya dosya adındaki “güncel”, bütün canlı sistemin bugünkü durumunun doğrulandığı anlamına gelmez.

Katalog; dosya listesi, Markdown başlıkları, JSON üstverileri/kayıt türleri, önceki incelemeler ve ilişkili dosya eşliklerinden hazırlanmıştır. Bu düzenleme, bütün ham kaynakların yeni bir tam anlamsal okuması değildir. İki kaynak denetim betiği bu katalog çalışması sırasında yürütülmedi.

## Giriş ve kaynak kapsamı

İlk okuma için README; bulgular için ana rapor; özgün kullanıcı anlamını korumak için istenen bağlam belgesi kullanılır.

| Dosya | İşlev ve kapsam | Statü | İlgili rapor veya kanıt |
| --- | --- | --- | --- |
| [AKTARIM_KAPSAMI.md](AKTARIM_KAPSAMI.md) | Yayımlanan ve dışarıda tutulan gövdeler ile yayın dönüşümleri. | Başvuru | [aktarim_manifestosu.json](aktarim_manifestosu.json) · [maskeleme_ve_donusum_kaydi.json](maskeleme_ve_donusum_kaydi.json) |
| [ANA_RAPOR.md](ANA_RAPOR.md) | Özgün kaynak incelemesinin birleşik bulguları ve aktarım ölçütleri. | Başvuru | [kanitlar/downloads_images.json](kanitlar/downloads_images.json) · [kanitlar/downloads_programs.json](kanitlar/downloads_programs.json) · [kanitlar/downloads_styles.json](kanitlar/downloads_styles.json) · [kanitlar/old_css_1.json](kanitlar/old_css_1.json) · [kanitlar/old_css_2.json](kanitlar/old_css_2.json) · [kanitlar/old_programs.json](kanitlar/old_programs.json) · [ISTENEN_BAGLAM.md](ISTENEN_BAGLAM.md) · [kaynaklar.json](kaynaklar.json) · [okuma_durumlari.json](okuma_durumlari.json) |
| [DOSYA_KATALOGU.md](DOSYA_KATALOGU.md) | Bütün yayın dosyalarının işlevi, rapor–kanıt ilişkileri ve ilgili dal/PR haritası. | Başvuru | [README.md](README.md) · [DUZENLEME_DOGRULAMASI_2026-10-26.json](DUZENLEME_DOGRULAMASI_2026-10-26.json) |
| [ISTENEN_BAGLAM.md](ISTENEN_BAGLAM.md) | Kullanıcının özgün ayrımları, son düzeltmeleri ve aktarılacak bağlam. | Başvuru | [ANA_RAPOR.md](ANA_RAPOR.md) |
| [README.md](README.md) | Okuma sırası, araştırma kapsamı, ayrı teknik işler ve yayın konumu. | Başvuru | [DOSYA_KATALOGU.md](DOSYA_KATALOGU.md) · [depo/ANADAL_SON_TARAMA_2026-10-26.md](depo/ANADAL_SON_TARAMA_2026-10-26.md) · [ANA_RAPOR.md](ANA_RAPOR.md) |
| [aktarim_manifestosu.json](aktarim_manifestosu.json) | 1.483 paket üyesinin aktarım kararı, hedefi ve özgün karması. | Kanıt | [AKTARIM_KAPSAMI.md](AKTARIM_KAPSAMI.md) · [kanitlar/paket_dogrulamasi.json](kanitlar/paket_dogrulamasi.json) |
| [kaynaklar.json](kaynaklar.json) | 325 özgün içerik, 512 konum ve tarihsel atıf kimliklerinin kataloğu. | Kanıt | [ANA_RAPOR.md](ANA_RAPOR.md) · [atif_denetimi.json](atif_denetimi.json) |
| [okuma_durumlari.json](okuma_durumlari.json) | 325 içeriğin son okuma yöntemi ve tamamlanma durumu. | Kanıt | [incelemeler/historical_document_status.md](incelemeler/historical_document_status.md) · [ANA_RAPOR.md](ANA_RAPOR.md) |

## 26 Ekim depo ve son kontrol belgeleri

Aynı gün yazılmış belgeler de ayrı sabit kesitlerdir. En son ana dal karşılaştırması `ANADAL_SON_TARAMA_2026-10-26.md`; onu izleyen düzenlemenin kontrolü `DUZENLEME_DOGRULAMASI_2026-10-26.json` içindedir.

| Dosya | İşlev ve kapsam | Statü | İlgili rapor veya kanıt |
| --- | --- | --- | --- |
| [depo/ANADAL_SON_TARAMA_2026-10-26.md](depo/ANADAL_SON_TARAMA_2026-10-26.md) | Dalın ayrıldığı committen son ana dal kesitine kapsam kontrolü; değişen dosyalar, kod durumu ve kapanış sınırları. | Başvuru | [depo/anadal_son_tarama_2026-10-26.json](depo/anadal_son_tarama_2026-10-26.json) · [DUZENLEME_DOGRULAMASI_2026-10-26.json](DUZENLEME_DOGRULAMASI_2026-10-26.json) |
| [depo/CLI_DALI_OKUMASI_2026-10-26.md](depo/CLI_DALI_OKUMASI_2026-10-26.md) | Steering CLI devam dalı ve PR #8 içeriğinin sabit sürüm incelemesi. | Başvuru | [depo/cli_branch_scope_2026-10-26.json](depo/cli_branch_scope_2026-10-26.json) |
| [depo/ETIKET_ARACI_OKUMASI_2026-10-26.md](depo/ETIKET_ARACI_OKUMASI_2026-10-26.md) | Sonradan bulunan yerel JSON etiket aracının statik incelemesi ve sınırları. | Başvuru | [depo/etiket_araci_kapsami_2026-10-26.json](depo/etiket_araci_kapsami_2026-10-26.json) · [depo/SON_KONTROL_2026-10-26.md](depo/SON_KONTROL_2026-10-26.md) |
| [depo/GUNCEL_OKUMA_2026-10-26.md](depo/GUNCEL_OKUMA_2026-10-26.md) | 26 Ekim arşiv aktarımı, depo düzeltmeleri ve güncel okuma sentezi. | Başvuru | [YAYIN_DOGRULAMASI_2026-10-26.json](YAYIN_DOGRULAMASI_2026-10-26.json) · [depo/dal_pr_durumu_2026-10-26.json](depo/dal_pr_durumu_2026-10-26.json) |
| [depo/KOD_OKUMASI_2026-10-26.md](depo/KOD_OKUMASI_2026-10-26.md) | 26 Ekim kod, ayar ve 122 çağrı günlüğünün kaynak incelemesi. | Başvuru | [depo/current_code_scope_2026-10-26.json](depo/current_code_scope_2026-10-26.json) |
| [depo/KOPRU_OKUMASI_2026-10-26.md](depo/KOPRU_OKUMASI_2026-10-26.md) | 169 köprü kaydının kapsamı ve sonraki kaynak düzeltmelerinin incelemesi. | Başvuru | [depo/current_kopru_scope_2026-10-26.json](depo/current_kopru_scope_2026-10-26.json) |
| [depo/ORTAK_ALAN_DALI_OKUMASI_2026-10-26.md](depo/ORTAK_ALAN_DALI_OKUMASI_2026-10-26.md) | Ortak alan araçları dalındaki dört yeni dosyanın ayrı incelemesi. | Başvuru | [depo/dal_pr_durumu_2026-10-26.json](depo/dal_pr_durumu_2026-10-26.json) |
| [depo/SON_KONTROL_2026-10-26.md](depo/SON_KONTROL_2026-10-26.md) | Geçmiş/arşiv kapanışı, sonradan bulunan ek kaynaklar ve kalan kapsam sınırları. | Başvuru | [depo/son_kontrol_kapsami_2026-10-26.json](depo/son_kontrol_kapsami_2026-10-26.json) · [depo/ETIKET_ARACI_OKUMASI_2026-10-26.md](depo/ETIKET_ARACI_OKUMASI_2026-10-26.md) |
| [depo/anadal_son_tarama_2026-10-26.json](depo/anadal_son_tarama_2026-10-26.json) | Son ana dal taramasının commit, dosya karması, kayıt gövdesi, ayna ve değişiklik kanıtları. | Kanıt | [depo/ANADAL_SON_TARAMA_2026-10-26.md](depo/ANADAL_SON_TARAMA_2026-10-26.md) |
| [depo/cli_branch_scope_2026-10-26.json](depo/cli_branch_scope_2026-10-26.json) | CLI devamı ve devir belgeleri için okunan dosya/sürüm kapsamı. | Kanıt | [depo/CLI_DALI_OKUMASI_2026-10-26.md](depo/CLI_DALI_OKUMASI_2026-10-26.md) |
| [depo/current_code_scope_2026-10-26.json](depo/current_code_scope_2026-10-26.json) | 26 Ekim kod/ayar dosyaları ile 122 günlüğün karşılaştırma kapsamı. | Kanıt | [depo/KOD_OKUMASI_2026-10-26.md](depo/KOD_OKUMASI_2026-10-26.md) |
| [depo/current_kopru_scope_2026-10-26.json](depo/current_kopru_scope_2026-10-26.json) | Önceki 109 kayıt eşliği ve 60 yeni kaydın okuma kapsamı. | Kanıt | [depo/KOPRU_OKUMASI_2026-10-26.md](depo/KOPRU_OKUMASI_2026-10-26.md) |
| [depo/dal_pr_durumu_2026-10-26.json](depo/dal_pr_durumu_2026-10-26.json) | 26 Ekim tarihinde görülen dal uçları ve PR durumlarının kaydı. | Kanıt | [depo/ORTAK_ALAN_DALI_OKUMASI_2026-10-26.md](depo/ORTAK_ALAN_DALI_OKUMASI_2026-10-26.md) · [depo/GUNCEL_OKUMA_2026-10-26.md](depo/GUNCEL_OKUMA_2026-10-26.md) |
| [depo/etiket_araci_kapsami_2026-10-26.json](depo/etiket_araci_kapsami_2026-10-26.json) | Ek etiket aracının ZIP/PYZ eşliği, dosya kapsamı ve tarihsel test kaydı. | Kanıt | [depo/ETIKET_ARACI_OKUMASI_2026-10-26.md](depo/ETIKET_ARACI_OKUMASI_2026-10-26.md) |
| [depo/son_kontrol_kapsami_2026-10-26.json](depo/son_kontrol_kapsami_2026-10-26.json) | Son kapanışın envanter, kuyruk, ek kaynak ve yayın kapsamı kayıtları. | Kanıt | [depo/SON_KONTROL_2026-10-26.md](depo/SON_KONTROL_2026-10-26.md) |

## Özgün kaynak incelemeleri

**19 aile raporu + 2 tamamlayıcı belge = 21 Markdown.** Aile raporlarının aynı adlı JSON kanıtı vardır. `historical_document_status.md` tarihsel ara çizelgedir; son durum `okuma_durumlari.json` ile okunur. `systems_embedded_audit.md` kanıtı `systems_remaining.json` içindeki `zip_embedded_audit_notes` kayıtlarındadır. Raporlardaki tarihsel ara durumlar son okuma kaydını geçersiz kılmaz.

| Dosya | İşlev ve kapsam | Statü | İlgili rapor veya kanıt |
| --- | --- | --- | --- |
| [incelemeler/books_faith_remaining.md](incelemeler/books_faith_remaining.md) | Sistem Farkları ve Matrix kitap projeleri; soru, dal ve üretim kapsamı. | Başvuru | [kanitlar/books_faith_remaining.json](kanitlar/books_faith_remaining.json) |
| [incelemeler/claude_programs.md](incelemeler/claude_programs.md) | Claude konuşması, arayüz kodu, araç yönergesi ve analitik kayıt ayrımı. | Başvuru | [kanitlar/claude_programs.json](kanitlar/claude_programs.json) |
| [incelemeler/cognitive_metacognition_remaining.md](incelemeler/cognitive_metacognition_remaining.md) | OMROS/CognitiveOS ve Metacognition konuşmaları; kullanıcı düzeltmeleri ve yöntemler. | Başvuru | [kanitlar/cognitive_metacognition_remaining.json](kanitlar/cognitive_metacognition_remaining.json) |
| [incelemeler/conversations.md](incelemeler/conversations.md) | ChatGPT/Gemini konuşma gövdeleri ile HTML yapılandırmalarının ayrı okunması. | Başvuru | [kanitlar/conversations.json](kanitlar/conversations.json) |
| [incelemeler/faith_remaining.md](incelemeler/faith_remaining.md) | Faith v2 içinde soru kapsamı, özgün tanıklık ve üretilmiş anlatı karşılaştırması. | Başvuru | [kanitlar/faith_remaining.json](kanitlar/faith_remaining.json) |
| [incelemeler/foundational.md](incelemeler/foundational.md) | deus_ex_machina temel eserleri ve anlam, aktarım, kaynak ayrımları. | Başvuru | [kanitlar/foundational.json](kanitlar/foundational.json) |
| [incelemeler/historical.md](incelemeler/historical.md) | Tarihsel aktarım ve HalukAI belgelerinde kullanıcı sözü, talimat ve uygulama ayrımı. | Başvuru | [kanitlar/historical.json](kanitlar/historical.json) |
| [incelemeler/historical_document_status.md](incelemeler/historical_document_status.md) | İlk tarihsel okumanın belge bazlı tamamlanan/kalan aralık çizelgesi. Ara durumdur; son tamamlanma kaydı okuma_durumlari.json içindedir. | Tarihsel | [kanitlar/historical.json](kanitlar/historical.json) · [okuma_durumlari.json](okuma_durumlari.json) |
| [incelemeler/historical_supplement.md](incelemeler/historical_supplement.md) | OMROS, WhatsApp/CLI devri ve tarihsel kaynakların tamamlayıcı incelemesi. | Başvuru | [kanitlar/historical_supplement.json](kanitlar/historical_supplement.json) |
| [incelemeler/images.md](incelemeler/images.md) | 26 raster görselin görünür içeriği ve görsel okumanın sınırları. | Başvuru | [kanitlar/images.json](kanitlar/images.json) |
| [incelemeler/long_corpus_remaining.md](incelemeler/long_corpus_remaining.md) | Büyük korpus tekrarları, uzun sohbet ve birleşik web kaynağı ilişkileri. | Başvuru | [kanitlar/long_corpus_remaining.json](kanitlar/long_corpus_remaining.json) |
| [incelemeler/metacognition_remaining.md](incelemeler/metacognition_remaining.md) | Metacognition çalışma kitabındaki kaynaklar, hücreler, yöntem ve eksik kayıtlar. | Başvuru | [kanitlar/metacognition_remaining.json](kanitlar/metacognition_remaining.json) |
| [incelemeler/mlops_remaining.md](incelemeler/mlops_remaining.md) | MLOps kitap konuşmasında yöntem istekleri, üretim beyanları ve erişilebilir gövdeler. | Başvuru | [kanitlar/mlops_remaining.json](kanitlar/mlops_remaining.json) |
| [incelemeler/models.md](incelemeler/models.md) | Model 1–4 metinlerinde yönlendirme, kural, izin ve kanıt tasarımı. | Başvuru | [kanitlar/models.json](kanitlar/models.json) |
| [incelemeler/models_remaining.md](incelemeler/models_remaining.md) | Model derlemeleri ve OMROS v19/v20 kitaplarında sürüm, kural ve sonuç ilişkileri. | Başvuru | [kanitlar/models_remaining.json](kanitlar/models_remaining.json) |
| [incelemeler/models_supplement.md](incelemeler/models_supplement.md) | Ek model belgeleri ve çalışma kitaplarında kilit, protokol ve örnek koşum sorunları. | Başvuru | [kanitlar/models_supplement.json](kanitlar/models_supplement.json) |
| [incelemeler/operational_remaining.md](incelemeler/operational_remaining.md) | CLI taraması ve operasyon aktarımında dosya, okuma, test ve gerçekleşme ayrımı. | Başvuru | [kanitlar/operational_remaining.json](kanitlar/operational_remaining.json) |
| [incelemeler/root_supplement.md](incelemeler/root_supplement.md) | Eski yorumların son kullanıcı açıklamalarıyla ve kök envanterlerle ilişkisi. | Başvuru | [kanitlar/root_supplement.json](kanitlar/root_supplement.json) |
| [incelemeler/systems_embedded_audit.md](incelemeler/systems_embedded_audit.md) | F00197/U0126 sistem kaynağının ayrı yayımlanan tamamlayıcı raporu. Kanıtları systems_remaining.json içindeki zip_embedded_audit_notes kayıtlarındadır. | Başvuru | [kanitlar/systems_remaining.json](kanitlar/systems_remaining.json) · [incelemeler/systems_remaining.md](incelemeler/systems_remaining.md) |
| [incelemeler/systems_remaining.md](incelemeler/systems_remaining.md) | Sistem ailesi sohbet ve derlemelerinde zincir, bölüm ve kaynak statüsü farkları. | Başvuru | [kanitlar/systems_remaining.json](kanitlar/systems_remaining.json) · [incelemeler/systems_embedded_audit.md](incelemeler/systems_embedded_audit.md) |
| [incelemeler/two_conversations_remaining.md](incelemeler/two_conversations_remaining.md) | İki büyük sohbette üretim kodu, puanlar, test iddiaları ve kullanıcı düzeltmeleri. | Başvuru | [kanitlar/two_conversations_remaining.json](kanitlar/two_conversations_remaining.json) |

## Analitik kanıtlar ve paket doğrulaması

**19 aile kanıtı + 6 yardımcı analitik kanıt + 1 paket doğrulaması = 26 JSON.** İlk 25 dosya analitik inceleme kanıtıdır. Altı yardımcı dosyanın ayrı aynı adlı aile raporu yoktur; ana raporla ilişkilidir. `paket_dogrulamasi.json` eski özel paketin doğrulamasıdır. Bu dosyalar bütün ham özel kaynakların kamuya açık kopyası değildir.

| Dosya | İşlev ve kapsam | Statü | İlgili rapor veya kanıt |
| --- | --- | --- | --- |
| [kanitlar/books_faith_remaining.json](kanitlar/books_faith_remaining.json) | Sistem Farkları ve Matrix kaynaklarının alıntı, eşlik ve okuma kapsamı kayıtları. | Kanıt | [incelemeler/books_faith_remaining.md](incelemeler/books_faith_remaining.md) |
| [kanitlar/claude_programs.json](kanitlar/claude_programs.json) | Claude kaynaklarının dosya değerlendirmeleri ve teknik alan dayanakları. | Kanıt | [incelemeler/claude_programs.md](incelemeler/claude_programs.md) |
| [kanitlar/cognitive_metacognition_remaining.json](kanitlar/cognitive_metacognition_remaining.json) | OMROS/CognitiveOS ve Metacognition mesaj doğrulaması, alıntıları ve okuma kapsamı. | Kanıt | [incelemeler/cognitive_metacognition_remaining.md](incelemeler/cognitive_metacognition_remaining.md) |
| [kanitlar/conversations.json](kanitlar/conversations.json) | Konuşma kaynaklarının kesin alıntıları, ifade konumları ve kimlik eşlemeleri. | Kanıt | [incelemeler/conversations.md](incelemeler/conversations.md) |
| [kanitlar/downloads_images.json](kanitlar/downloads_images.json) | İndirilen arayüz görsellerinin yardımcı dosya değerlendirmeleri. | Kanıt | [ANA_RAPOR.md](ANA_RAPOR.md) |
| [kanitlar/downloads_programs.json](kanitlar/downloads_programs.json) | İndirilen web betiklerinin yardımcı işlev ve yapı değerlendirmeleri. | Kanıt | [ANA_RAPOR.md](ANA_RAPOR.md) |
| [kanitlar/downloads_styles.json](kanitlar/downloads_styles.json) | İndirilen web stillerinin yardımcı işlev ve yapı değerlendirmeleri. | Kanıt | [ANA_RAPOR.md](ANA_RAPOR.md) |
| [kanitlar/faith_remaining.json](kanitlar/faith_remaining.json) | Faith v2 mesajları, soru kaymaları ve birinci şahıs anlatı kökeni dayanakları. | Kanıt | [incelemeler/faith_remaining.md](incelemeler/faith_remaining.md) |
| [kanitlar/foundational.json](kanitlar/foundational.json) | Temel eserlerin dosya değerlendirmeleri ve okuma kapsamı kayıtları. | Kanıt | [incelemeler/foundational.md](incelemeler/foundational.md) |
| [kanitlar/historical.json](kanitlar/historical.json) | Tarihsel kaynak eşlemeleri, ilk okuma kapsamı, kuyruk ve belge değerlendirmeleri. | Kanıt | [incelemeler/historical.md](incelemeler/historical.md) · [incelemeler/historical_document_status.md](incelemeler/historical_document_status.md) |
| [kanitlar/historical_supplement.json](kanitlar/historical_supplement.json) | Tarihsel ek belgelerin değerlendirmeleri, tekrar eşlemeleri ve kapsam kayıtları. | Kanıt | [incelemeler/historical_supplement.md](incelemeler/historical_supplement.md) |
| [kanitlar/images.json](kanitlar/images.json) | 26 görselin ayrı değerlendirmeleri ve kapsam kayıtları; özgün pikseller değildir. | Kanıt | [incelemeler/images.md](incelemeler/images.md) |
| [kanitlar/long_corpus_remaining.json](kanitlar/long_corpus_remaining.json) | Uzun kaynakların birleşim kanıtı, alıntıları ve okuma kapsamı kayıtları. | Kanıt | [incelemeler/long_corpus_remaining.md](incelemeler/long_corpus_remaining.md) |
| [kanitlar/metacognition_remaining.json](kanitlar/metacognition_remaining.json) | Metacognition hücre/sayfa değerlendirmeleri, denetimler ve okuma kapsamı. | Kanıt | [incelemeler/metacognition_remaining.md](incelemeler/metacognition_remaining.md) |
| [kanitlar/mlops_remaining.json](kanitlar/mlops_remaining.json) | MLOps mesaj doğrulaması, belge değerlendirmesi ve okuma kapsamı. | Kanıt | [incelemeler/mlops_remaining.md](incelemeler/mlops_remaining.md) |
| [kanitlar/models.json](kanitlar/models.json) | Model 1–4 kaynaklarının eşleme denetimi, alıntıları ve okuma kapsamı. | Kanıt | [incelemeler/models.md](incelemeler/models.md) |
| [kanitlar/models_remaining.json](kanitlar/models_remaining.json) | Model derlemelerinin dosya değerlendirmeleri, alıntıları ve eşleme doğrulamaları. | Kanıt | [incelemeler/models_remaining.md](incelemeler/models_remaining.md) |
| [kanitlar/models_supplement.json](kanitlar/models_supplement.json) | Ek model belgelerinin hücre/konum kanıtları, eşlemeleri ve okuma kapsamı. | Kanıt | [incelemeler/models_supplement.md](incelemeler/models_supplement.md) |
| [kanitlar/old_css_1.json](kanitlar/old_css_1.json) | İlk eski stil grubunun yardımcı dosya ve yapı değerlendirmeleri. | Kanıt | [ANA_RAPOR.md](ANA_RAPOR.md) |
| [kanitlar/old_css_2.json](kanitlar/old_css_2.json) | İkinci eski stil grubunun yardımcı dosya ve yapı değerlendirmeleri. | Kanıt | [ANA_RAPOR.md](ANA_RAPOR.md) |
| [kanitlar/old_programs.json](kanitlar/old_programs.json) | Eski program grubunun yardımcı dosya ve işlev değerlendirmeleri. | Kanıt | [ANA_RAPOR.md](ANA_RAPOR.md) |
| [kanitlar/operational_remaining.json](kanitlar/operational_remaining.json) | Operasyon kayıtlarının tamamlayıcı okuma kapsamı, ilerleme ve değerlendirmeleri. | Kanıt | [incelemeler/operational_remaining.md](incelemeler/operational_remaining.md) |
| [kanitlar/paket_dogrulamasi.json](kanitlar/paket_dogrulamasi.json) | Özgün özel okuma paketinin dönüşüm, maskeleme, kuyruk ve bütünlük doğrulamaları. | Kanıt | [aktarim_manifestosu.json](aktarim_manifestosu.json) |
| [kanitlar/root_supplement.json](kanitlar/root_supplement.json) | Kök belgelerin tamamlayıcı değerlendirmeleri ve yapısal envanter denetimleri. | Kanıt | [incelemeler/root_supplement.md](incelemeler/root_supplement.md) |
| [kanitlar/systems_remaining.json](kanitlar/systems_remaining.json) | Sistem ailesinin değerlendirmeleri, eşlikleri ve gömülü tamamlayıcı okuma kanıtları. | Kanıt | [incelemeler/systems_remaining.md](incelemeler/systems_remaining.md) · [incelemeler/systems_embedded_audit.md](incelemeler/systems_embedded_audit.md) |
| [kanitlar/two_conversations_remaining.json](kanitlar/two_conversations_remaining.json) | İki büyük sohbetin kaynak, alıntı, ilerleme ve tamamlanma denetimleri. | Kanıt | [incelemeler/two_conversations_remaining.md](incelemeler/two_conversations_remaining.md) |

## Tarihsel depo okumaları

Bu grubun tamamı 26 Ekim son taramasından önceki sabit depo kesitlerini ve bunların kanıtlarını taşır. Adındaki “GUNCEL”, “SON” veya “yayin_oncesi” sözcüğü bugünkü ana dalı belirtmez. Son okuma sırası README içindedir.

| Dosya | İşlev ve kapsam | Statü | İlgili rapor veya kanıt |
| --- | --- | --- | --- |
| [DEPO_OKUMASI.md](DEPO_OKUMASI.md) | İlk Ortak Köprü okumasının kaynak incelemesiyle karşılaştırılması. | Tarihsel | [depo/okunan_depo.json](depo/okunan_depo.json) |
| [depo/GUNCEL_KOD_VE_PR_OKUMASI.md](depo/GUNCEL_KOD_VE_PR_OKUMASI.md) | 24 Ekim ana dal kodu, günlükleri ve açık PR önerilerinin incelemesi. | Tarihsel | [depo/repo-reading-manifest.json](depo/repo-reading-manifest.json) · [depo/repo-log-equivalence.json](depo/repo-log-equivalence.json) · [depo/okunan_dal_ve_pr_surumleri.json](depo/okunan_dal_ve_pr_surumleri.json) |
| [depo/GUNCEL_OKUMA_2026-10-24.md](depo/GUNCEL_OKUMA_2026-10-24.md) | 24 Ekim tarihindeki 109 kayıt, 118 günlük ve tamamlanan aktarım sentezi. | Tarihsel | [depo/guncel_kopru_kapsami.json](depo/guncel_kopru_kapsami.json) · [depo/repo-reading-manifest.json](depo/repo-reading-manifest.json) · [depo/ARSIV_YENIDEN_DOGRULAMA.json](depo/ARSIV_YENIDEN_DOGRULAMA.json) · [YAYIN_DOGRULAMASI_GUNCEL.json](YAYIN_DOGRULAMASI_GUNCEL.json) · [depo/yayin_oncesi_ana_dal_farki.json](depo/yayin_oncesi_ana_dal_farki.json) |
| [depo/GUNLUK_EKI.md](depo/GUNLUK_EKI.md) | İkinci depo anındaki yeni günlükler ve k-0010/k-0011 değerlendirmesi. | Tarihsel | [depo/gunluk_eki_kapsami.json](depo/gunluk_eki_kapsami.json) |
| [depo/GUNLUK_OKUMASI.md](depo/GUNLUK_OKUMASI.md) | İlk 13 çağrı günlüğünün sonuçları ve kanıt sınırları. | Tarihsel | [depo/gunluk_kapsami.json](depo/gunluk_kapsami.json) |
| [depo/GUNLUK_SON_EK.md](depo/GUNLUK_SON_EK.md) | Üçüncü depo anındaki son günlükler ve k-0012/k-0013 değerlendirmesi. | Tarihsel | [depo/gunluk_son_ek_kapsami.json](depo/gunluk_son_ek_kapsami.json) |
| [depo/KOD_OKUMASI.md](depo/KOD_OKUMASI.md) | İlk depo sürümünde kayıt ekleme, ayna, bekleyen kayıt ve bağlam yollarının incelemesi. | Tarihsel | [depo/okunan_depo.json](depo/okunan_depo.json) |
| [depo/KOPRU_ILK_55_OKUMASI.md](depo/KOPRU_ILK_55_OKUMASI.md) | 24 Ekim anındaki açıklamalar ve k-0001–k-0055 kayıtlarının incelemesi. | Tarihsel | [depo/guncel_kopru_kapsami.json](depo/guncel_kopru_kapsami.json) |
| [depo/KOPRU_SON_54_OKUMASI.md](depo/KOPRU_SON_54_OKUMASI.md) | 24 Ekim anındaki k-0056–k-0109 kayıtlarının incelemesi. | Tarihsel | [depo/guncel_kopru_kapsami.json](depo/guncel_kopru_kapsami.json) |
| [depo/PR3_OKUMASI.md](depo/PR3_OKUMASI.md) | PR #3 önerisinin 20 dosyalık farkına ilişkin statik kaynak incelemesi. | Tarihsel | [depo/okunan_dal_ve_pr_surumleri.json](depo/okunan_dal_ve_pr_surumleri.json) |
| [depo/REFERANS_DALLARI_OKUMASI.md](depo/REFERANS_DALLARI_OKUMASI.md) | Üç sabit referans dalının ve ana dalla ilişkilerinin 24 Ekim incelemesi. | Tarihsel | [depo/reference-branches-coverage.json](depo/reference-branches-coverage.json) · [depo/repo-pr4-equivalence.json](depo/repo-pr4-equivalence.json) |
| [depo/SON_DEGISIKLIK.md](depo/SON_DEGISIKLIK.md) | İlk yayın sırasındaki son ana dal değişikliği ve katkı dalı gerekçesi. | Tarihsel | [depo/okunan_depo.json](depo/okunan_depo.json) |
| [depo/YENI_DOSYALAR.md](depo/YENI_DOSYALAR.md) | Sonradan eklenip kaldırılan beş steering dosyasının tarihsel incelemesi. | Tarihsel | [depo/okunan_depo.json](depo/okunan_depo.json) |
| [depo/guncel_kopru_kapsami.json](depo/guncel_kopru_kapsami.json) | 24 Ekim sabit ana dalındaki 109 köprü kaydının konum ve dosya kapsamı. | Kanıt | [depo/KOPRU_ILK_55_OKUMASI.md](depo/KOPRU_ILK_55_OKUMASI.md) · [depo/KOPRU_SON_54_OKUMASI.md](depo/KOPRU_SON_54_OKUMASI.md) · [depo/GUNCEL_OKUMA_2026-10-24.md](depo/GUNCEL_OKUMA_2026-10-24.md) |
| [depo/gunluk_eki_kapsami.json](depo/gunluk_eki_kapsami.json) | İkinci günlük ekinin yeni dosyaları ve birikimli sonuç sayımları. | Kanıt | [depo/GUNLUK_EKI.md](depo/GUNLUK_EKI.md) |
| [depo/gunluk_kapsami.json](depo/gunluk_kapsami.json) | İlk 13 çağrı günlüğünün dosya, bölüm, tekrar ve sonuç kayıtları. | Kanıt | [depo/GUNLUK_OKUMASI.md](depo/GUNLUK_OKUMASI.md) |
| [depo/gunluk_son_ek_kapsami.json](depo/gunluk_son_ek_kapsami.json) | Son günlük ekinin üç çağrısı, tekrar eşlikleri ve birikimli 19 çağrı kapsamı. | Kanıt | [depo/GUNLUK_SON_EK.md](depo/GUNLUK_SON_EK.md) |
| [depo/okunan_dal_ve_pr_surumleri.json](depo/okunan_dal_ve_pr_surumleri.json) | 24 Ekim okumasında esas alınan dal ve PR sürümlerinin kaydı. | Kanıt | [depo/GUNCEL_KOD_VE_PR_OKUMASI.md](depo/GUNCEL_KOD_VE_PR_OKUMASI.md) · [depo/PR3_OKUMASI.md](depo/PR3_OKUMASI.md) |
| [depo/okunan_depo.json](depo/okunan_depo.json) | İlk okuma dizisindeki son sabit depo dosyaları ve önceki anlık durumlar. | Kanıt | [DEPO_OKUMASI.md](DEPO_OKUMASI.md) · [depo/KOD_OKUMASI.md](depo/KOD_OKUMASI.md) · [depo/YENI_DOSYALAR.md](depo/YENI_DOSYALAR.md) · [depo/SON_DEGISIKLIK.md](depo/SON_DEGISIKLIK.md) |
| [depo/reference-branches-coverage.json](depo/reference-branches-coverage.json) | Üç referans dalının dosya, biçim ve kaynak eşlik kapsamı. | Kanıt | [depo/REFERANS_DALLARI_OKUMASI.md](depo/REFERANS_DALLARI_OKUMASI.md) |
| [depo/repo-reading-manifest.json](depo/repo-reading-manifest.json) | 24 Ekim ana dal dosyalarının yöntem ve sürüm bazında okuma manifestosu. | Kanıt | [depo/GUNCEL_KOD_VE_PR_OKUMASI.md](depo/GUNCEL_KOD_VE_PR_OKUMASI.md) · [depo/GUNCEL_OKUMA_2026-10-24.md](depo/GUNCEL_OKUMA_2026-10-24.md) |
| [depo/yayin_oncesi_ana_dal_farki.json](depo/yayin_oncesi_ana_dal_farki.json) | 24 Ekim yayın hazırlığındaki son ana dal farkının okuma kapsamına etkisi. | Kanıt | [depo/GUNCEL_OKUMA_2026-10-24.md](depo/GUNCEL_OKUMA_2026-10-24.md) |

## Yayın doğrulamaları ve denetim araçları

Doğrulamalar kendi yayın aşamaları içindir. Önceki 85/98/102 dosyalık kapsamlar tarihsel paket sayılarıdır; mevcut yayının 106 dosyasıyla karıştırılmamalıdır. `SHA256SUMS` kendisi dışındaki 105 dosyayı kapsar.

| Dosya | İşlev ve kapsam | Statü | İlgili rapor veya kanıt |
| --- | --- | --- | --- |
| [DUZENLEME_DOGRULAMASI_2026-10-26.json](DUZENLEME_DOGRULAMASI_2026-10-26.json) | Son düzenlemenin dosya kataloğu, yayın adayı ve köprü/ayna bütünlük kontrolleri. | Kanıt | [DOSYA_KATALOGU.md](DOSYA_KATALOGU.md) · [SHA256SUMS](SHA256SUMS) · [depo/anadal_son_tarama_2026-10-26.json](depo/anadal_son_tarama_2026-10-26.json) |
| [SHA256SUMS](SHA256SUMS) | Kendisi dışındaki 105 yayın dosyasının SHA-256 karması. Bu düzenlemede yeniden üretildi; kendi karmasını içermez. | Kanıt | — |
| [YAYIN_DOGRULAMASI.json](YAYIN_DOGRULAMASI.json) | İlk aktarım aşamasının kaynak, kapsam ve yayın denetimi. İlk yayın aşaması; sonraki yayın kontrolleri ayrı dosyalardadır. | Kanıt | — |
| [YAYIN_DOGRULAMASI_2026-10-26.json](YAYIN_DOGRULAMASI_2026-10-26.json) | 26 Ekim aktarımının arşiv, depo ve yayın denetimi. | Kanıt | [depo/GUNCEL_OKUMA_2026-10-26.md](depo/GUNCEL_OKUMA_2026-10-26.md) |
| [YAYIN_DOGRULAMASI_GUNCEL.json](YAYIN_DOGRULAMASI_GUNCEL.json) | 24 Ekim güncellemesinin dosya, bağlantı ve kapsam denetimi. 24 Ekim güncellemesi; adına rağmen 26 Ekim kontrolü değildir. | Kanıt | [depo/GUNCEL_OKUMA_2026-10-24.md](depo/GUNCEL_OKUMA_2026-10-24.md) |
| [atif_denetimi.json](atif_denetimi.json) | Raporlardaki kaynak kimliklerinin künye ve aile kanıtı bağlantıları. | Kanıt | [kaynaklar.json](kaynaklar.json) |
| [depo/ARSIV_KARSILASTIRMASI_2026-10-26.md](depo/ARSIV_KARSILASTIRMASI_2026-10-26.md) | Özgün ZIP ile önceki yayının rapor, JSON ve kapsam karşılaştırmasının açıklaması. | Başvuru | [depo/archive_audit_2026-10-26.json](depo/archive_audit_2026-10-26.json) · [depo/audit_steering_archive.py](depo/audit_steering_archive.py) |
| [depo/ARSIV_YENIDEN_DOGRULAMA.json](depo/ARSIV_YENIDEN_DOGRULAMA.json) | 24 Ekim aşamasındaki özgün ZIP ve önceki yayın karmalarının doğrulaması. 24 Ekim arşiv karşılaştırması. | Kanıt | [depo/GUNCEL_OKUMA_2026-10-24.md](depo/GUNCEL_OKUMA_2026-10-24.md) |
| [depo/archive_audit_2026-10-26.json](depo/archive_audit_2026-10-26.json) | 1.483 üye ve önceki 85 dosyalık yayının ayrıntılı karşılaştırma sonuçları. Önceki 80fd42db48e91104383b47b6b4144f01790999be sürümündeki 85 dosyalık yayın karşılaştırılır. | Kanıt | [depo/ARSIV_KARSILASTIRMASI_2026-10-26.md](depo/ARSIV_KARSILASTIRMASI_2026-10-26.md) |
| [depo/audit_steering_archive.py](depo/audit_steering_archive.py) | Özgün arşiv ile sabit Git sürümünü karşılaştıran parametreli denetim betiği. | Araç | [depo/ARSIV_KARSILASTIRMASI_2026-10-26.md](depo/ARSIV_KARSILASTIRMASI_2026-10-26.md) |
| [depo/repo-log-equivalence.json](depo/repo-log-equivalence.json) | 24 Ekim sabit sürümündeki günlük ve köprü gövdelerinin eşlik sonuçları. 8571ddf8e3a33b432cc1c7ef88b69a902f390e5c sürümünün sonuç kaydı. | Kanıt | [depo/GUNCEL_KOD_VE_PR_OKUMASI.md](depo/GUNCEL_KOD_VE_PR_OKUMASI.md) · [depo/repo-log-equivalence.py](depo/repo-log-equivalence.py) |
| [depo/repo-log-equivalence.py](depo/repo-log-equivalence.py) | 24 Ekim sabit depo sürümünde günlük/köprü eşliği çıkaran denetim betiği. Betikteki sabit Git sürümü 8571ddf8e3a33b432cc1c7ef88b69a902f390e5c. | Araç | [depo/repo-log-equivalence.json](depo/repo-log-equivalence.json) |
| [depo/repo-pr4-equivalence.json](depo/repo-pr4-equivalence.json) | PR #4 kaynak metni ile türetilmiş çıktılarının eşlik denetimi. 24 Ekim PR #4 kaynak eşliği; güncel ana dala uygulanma sonucu değildir. | Kanıt | [depo/REFERANS_DALLARI_OKUMASI.md](depo/REFERANS_DALLARI_OKUMASI.md) |
| [maskeleme_ve_donusum_kaydi.json](maskeleme_ve_donusum_kaydi.json) | Yeni yayın kopyalarındaki maskeleme, yol ve metin dönüşümleri. | Kanıt | [AKTARIM_KAPSAMI.md](AKTARIM_KAPSAMI.md) |

## İlgili dalların haritası

Aşağıdaki **14 dal ucu**, bu düzenleme yayımlanmadan önce 26 Ekim 2026 tarihinde GitHub üzerinden okundu. Commit bağlantıları bu sabit kesitleri açar; bu düzenlemenin yayımlanmasıyla `main` ve araştırma dalının uçları ilerler. Diğer dalların bütün gövdelerinin yeniden tam okunduğu iddia edilmez. “İlgili okuma” bağlantısı, raporun kendi tarih ve kapsamıyla geçerlidir.

| Dal | İşlev / ilişki | Düzenleme öncesi commit | İlgili okuma |
| --- | --- | --- | --- |
| `main` | Kanonik köprü, uygulama kodu, ayarlar ve ana giriş. | [1b3115c48c](https://github.com/HalukAINRS/ortak-kopru/tree/1b3115c48c1a6b1dd627313a6a050d1152aad729) | [ANADAL_SON_TARAMA_2026-10-26.md](depo/ANADAL_SON_TARAMA_2026-10-26.md) |
| `steering-inceleme-2026-10-24` | Bu katalogdaki ayrıntılı araştırma ve kanıt yayını; PR #1 taslak. | [0bfc400fd5](https://github.com/HalukAINRS/ortak-kopru/tree/0bfc400fd5e3a0fa5bc8142035a4650bd79f9ca4) | [README.md](README.md) |
| `saman/steering-cli-devam-20261024` | Steering/CLI devamı ve ayrı kaynak/kontrol çalışmaları; PR #8. | [b2cfa94323](https://github.com/HalukAINRS/ortak-kopru/tree/b2cfa94323df6847033083a2680f0d2ebdbb5909) | [CLI_DALI_OKUMASI_2026-10-26.md](depo/CLI_DALI_OKUMASI_2026-10-26.md) |
| `claude/ortak-alan-araclari-2026-10-25` | Ortak alan araçlarının ayrı dalı. | [f52ef87b38](https://github.com/HalukAINRS/ortak-kopru/tree/f52ef87b381f3b8475821208c88b0df4f9814be7) | [ORTAK_ALAN_DALI_OKUMASI_2026-10-26.md](depo/ORTAK_ALAN_DALI_OKUMASI_2026-10-26.md) |
| `claude/hacker-devri-2026-10-24` | Hacker devri ve Deus ex machina payı; PR #5. | [62b1d2b186](https://github.com/HalukAINRS/ortak-kopru/tree/62b1d2b1861d5cffb6c081a6b256c9a5a3cd7cf7) | [GUNCEL_KOD_VE_PR_OKUMASI.md](depo/GUNCEL_KOD_VE_PR_OKUMASI.md) |
| `copilot/convert-files-to-txt-html-json` | Dosya dönüştürme başvuru dalı. | [c9f1c92d4c](https://github.com/HalukAINRS/ortak-kopru/tree/c9f1c92d4c14411b470b756779245f98f5f5ea20) | [REFERANS_DALLARI_OKUMASI.md](depo/REFERANS_DALLARI_OKUMASI.md) |
| `copilot/deus-ex-machina-user-layer` | Şahit devri ve görev katmanı önerisi; PR #4. | [0582717a00](https://github.com/HalukAINRS/ortak-kopru/tree/0582717a00f67fccd8f583cef3d482ab5a9945fa) | [GUNCEL_KOD_VE_PR_OKUMASI.md](depo/GUNCEL_KOD_VE_PR_OKUMASI.md) |
| `copilot/implement-transparent-architecture` | Denetlenebilir bağlam ve çalışma kaydı önerisi; PR #3. | [61d13f7573](https://github.com/HalukAINRS/ortak-kopru/tree/61d13f7573fec8cbbe87f93b5423110b2bf9b562) | [PR3_OKUMASI.md](depo/PR3_OKUMASI.md) |
| `copilot/ortak-kopru-dokumasyonu` | İsteğe bağlı bağlam/dokümantasyon önerisi; PR #2. | [42a310380e](https://github.com/HalukAINRS/ortak-kopru/tree/42a310380e76f12f816fb5e6a931cac213e8af20) | [GUNCEL_KOD_VE_PR_OKUMASI.md](depo/GUNCEL_KOD_VE_PR_OKUMASI.md) |
| `deus-ex-machina-2026-10-24` | Deus ex machina devamı ve tarihsel devir paketi; PR #7 hedefi. | [0d87fe5437](https://github.com/HalukAINRS/ortak-kopru/tree/0d87fe5437d6d56122cc81a0456e6e4e4869b67b) | [REFERANS_DALLARI_OKUMASI.md](depo/REFERANS_DALLARI_OKUMASI.md) |
| `gemini-steering-gecmisi-2026-10-24` | Gemini Steering geçmişi başvuru dalı. | [40397e6770](https://github.com/HalukAINRS/ortak-kopru/tree/40397e6770f6055ed0d8b505f408e31164cfb7b8) | [REFERANS_DALLARI_OKUMASI.md](depo/REFERANS_DALLARI_OKUMASI.md) |
| `sahit/cli-devri-2026-10-24` | Şahit CLI devir dalı; PR #6. | [5e6d393592](https://github.com/HalukAINRS/ortak-kopru/tree/5e6d3935926eaff27689eecd21009f5a3951d5ef) | [KOPRU_OKUMASI_2026-10-26.md](depo/KOPRU_OKUMASI_2026-10-26.md) |
| `saman/deus-cli-ilk-cevrim` | Açık oturum kuyruğu ve devam önerisi; PR #7. | [359a99c69b](https://github.com/HalukAINRS/ortak-kopru/tree/359a99c69bf131ccaffa1d2e1468eb165a59bd64) | [KOPRU_OKUMASI_2026-10-26.md](depo/KOPRU_OKUMASI_2026-10-26.md) |
| `saman/kopru-katman-hedefleme-20261024` | Üretici/rol hedefleme düzeltmesi; PR #9 ana dala birleştirilmiş. | [fd8f1d9c20](https://github.com/HalukAINRS/ortak-kopru/tree/fd8f1d9c2013678da11c7886d756b3bf8caecab0) | [ANADAL_SON_TARAMA_2026-10-26.md](depo/ANADAL_SON_TARAMA_2026-10-26.md) |

PR #9 için güncel Git geçmişinde doğrulanan birleşme commit’i [`239a37805c257609eb6ce7543c1e8e094043147b`](https://github.com/HalukAINRS/ortak-kopru/commit/239a37805c257609eb6ce7543c1e8e094043147b) ve ana dalın atasıdır. Eski PR üstverisindeki commit kimlikleriyle güncel dal uçları aynı varsayılmadı; ayrıntı son ana dal taramasındadır.

## PR yerleşimi

Bu tablo aynı düzenleme öncesi üstveri kesitidir. Araştırma belgelerini düzenlemek, bu PR’ları birleştirme veya önerilen programları çalıştırma işlemi değildir.

| PR | Konu | Kaynak dal → hedef dal | Durum |
| --- | --- | --- | --- |
| [#1](https://github.com/HalukAINRS/ortak-kopru/pull/1) | Steering araştırması, dosya kataloğu ve son ana dal taraması | `steering-inceleme-2026-10-24` → `main` | Açık taslak |
| [#2](https://github.com/HalukAINRS/ortak-kopru/pull/2) | Add an opt-in, auditable context workflow for the bridge | `copilot/ortak-kopru-dokumasyonu` → `main` | Açık taslak |
| [#3](https://github.com/HalukAINRS/ortak-kopru/pull/3) | Add opt-in auditable context and run records | `copilot/implement-transparent-architecture` → `main` | Açık taslak |
| [#4](https://github.com/HalukAINRS/ortak-kopru/pull/4) | Prepare Şahit CLI handoff and deus_ex_machina task layer | `copilot/deus-ex-machina-user-layer` → `main` | Açık taslak |
| [#5](https://github.com/HalukAINRS/ortak-kopru/pull/5) | Claude (Hacker) devri ve deus_ex_machina payı | `claude/hacker-devri-2026-10-24` → `main` | Açık taslak |
| [#6](https://github.com/HalukAINRS/ortak-kopru/pull/6) | Sahit/cli devri 2026 10 24 | `sahit/cli-devri-2026-10-24` → `main` | Açık taslak |
| [#7](https://github.com/HalukAINRS/ortak-kopru/pull/7) | deus_ex_machina: açık oturum kuyruğu ve katman geri dönüşünden otomatik devam | `saman/deus-cli-ilk-cevrim` → `deus-ex-machina-2026-10-24` | Açık taslak |
| [#8](https://github.com/HalukAINRS/ortak-kopru/pull/8) | Steering ve CLI devamı: kaynak doğrulaması, Cyber defteri ve ortak kurulum | `saman/steering-cli-devam-20261024` → `steering-inceleme-2026-10-24` | Açık taslak |
| [#9](https://github.com/HalukAINRS/ortak-kopru/pull/9) | Köprü: açık CLI hedefini API yedeğinden ve kök ad kapsamından ayır | `saman/kopru-katman-hedefleme-20261024` → `main` | Birleştirilmiş · 24 Ekim 2026 |

## Düzenlemenin sınırı

Bu katalog, mevcut belgeleri bulunabilir kılar ve kanıt eşliklerini görünür tutar. Ana dalın README’sindeki güncelliğini yitirmiş çağrı yolu/bağlam/kapanış açıklamaları mevcut kodla uyumlu hale getirildi. Son kapanış kaydı yalnız bu oturumun arşiv okuma, aktarım ve düzenleme işini kapsar; ayrı teknik işlerin tamamlandığı anlamına gelmez. Ayrıntılı bütünlük sonuçları [düzenleme doğrulamasındadır](DUZENLEME_DOGRULAMASI_2026-10-26.json).

# deus_ex_machina görev kuyruğu (Şahit katkısı)

Katman rolleri ve CLI etkileşim sözleşmesi: [SOZLESME.md](SOZLESME.md). Bu dosya PR #4'te `deus_ex_machina/README.md` idi; Şaman dalındaki (`deus-ex-machina-2026-10-24`) aynı adlı kavram belgesiyle yol çakışmasın diye taşındı.

Bu iskelet çevrimdışı terminal + yerel JSON kuyruğudur. `deus_ex_machina` ayrı bir model/ajan değildir ve kendiliğinden görev seçme, izin artırma veya CLI çalıştırma yetkisi yoktur. Mevcut katılımcılar: Hacker, Şaman, Şahit ve Gemini. Başka katılımcı eklemek açık kayıt/inceleme gerektirir; bilinmeyen adlar reddedilir.

## Kullanım

Python standart kütüphanesi yeterlidir. Kuyruk varsayılan olarak kullanıcının Home dizini altındadır; hassas/kişisel iş içerikleri repository'ye eklenmez.

```console
python3 deus_ex_machina/task_queue.py list
python3 deus_ex_machina/task_queue.py create --topic deus_ex_machina --participant Şahit \
  --words-file /path/to/original-user-words.txt --criterion "Çıktı kaynakla karşılaştırıldı" \
  --evidence "README.md" --permission-scope read_only
python3 deus_ex_machina/task_queue.py approve TASK_ID --scope read_only --confirm-reviewed
python3 deus_ex_machina/task_queue.py begin TASK_ID --confirm-read-only
python3 deus_ex_machina/task_queue.py record TASK_ID --result-file participant-result.txt \
  --evidence "README.md:12" --artifact "review-note.txt"
python3 deus_ex_machina/task_queue.py verify-evidence TASK_ID --source-ref "README.md" \
  --version "reviewed checkout" --sha256 SHA256_HEX --method "local file read" \
  --purpose "acceptance check" --confirm-observed
python3 deus_ex_machina/task_queue.py complete TASK_ID --satisfied "Çıktı kaynakla karşılaştırıldı" \
  --confirm-acceptance
```

İlk satırdan `complete`'e kadar kullanıcı her adımı açıkça çalıştırır. `begin --confirm-read-only`, onaylanmış `read_only` görevi tek kullanımlık olarak `running` durumuna alır; katılımcı CLI'ı başlatmaz. Bu yoldaki `record`, kullanıcının yerel gözlemini `local_operator_observation_not_user_instruction` sınıfıyla saklar. `begin --confirm-manual-cli` ayrı onaylanmış `manual_cli` izni gerektirir; katılımcı CLI'ı kullanıcı ayrıca başlatır, kuyruk hiçbir süreç başlatmaz. Tekrar başlatma reddedilir. Katılımcı sonucu `participant_output_not_user_instruction` sınıfında `unverified` kalır. `completed` için en az bir kaynak `verify-evidence` ile sürüm/hash/gözlem yöntemiyle yerel olarak işaretlenmeli ve her kabul ölçütü için açık kabul verilmelidir. Bu, yerel operatör beyanıdır; kimlik, kaynak gerçekliği veya olgusal doğruluk kanıtı değildir.

İzin kapsamı `read_only` ile başlar. Başka CLI ile elle çalışma için görev oluşturulurken `manual_cli` talebi ve sonra ayrı `approve --scope manual_cli --confirm-reviewed` gerekir. Kuyrukta otomatik adaptör, shell komutu veya ağ istemcisi yoktur. `permission_scope` mevcut PR #3'teki default-deny/ayrı onay yaklaşımıyla uyumludur; PR #3 ayrı ve açık taslaktır, bu dosya onun merge edildiğini varsaymaz.

`task.schema.json` sözleşmeyi tanımlar. Her kanıt kaynağı repository-relative mutlak olmayan bir referans, sürüm, hash, gözlem yöntemi, erişim, kanıt durumu, amaç ve yazma izni alanları taşır. Sağlanan referans otomatik olarak doğrulanmış sayılmaz. Dosya kilidi aynı anda ikinci yazarı engeller; kilit kalırsa süreci araştırıp kullanıcı güvenli olduğunu belirlemeden kilidi silme.

Başlıklar `Steering` ve `deus_ex_machina` ayrı ayrı süzülür. Steering araştırmasının içeriği bu görev kuyruğuyla değiştirilmez.

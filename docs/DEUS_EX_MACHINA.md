# deus_ex_machina — iş çekirdeği ve yerel yüzey

Bu ilk uygulama, ortak HTML defterinin yanına **kalıcı iş / özgün ileti / çalıştırma / oturum** ayrımını ekler. Kaynaklar, yetki beyanı, düzeltmeler, sonuçlar ve kabul ölçütleri aynı işe bağlı kalır. Eski `k-XXXX` kayıtları yeni görev kuyruğuna otomatik alınmaz.

İkinci uygulama aşaması, ekrandan sonuç/doğrulama, oturum gelen kutusu, bütün dosyaları taşıyan devir paketi ve tutarlı yedekleme/geri yükleme ekler. [Devam ve yedekleme rehberi](DEVAM_VE_YEDEK.md).

Kullanıcının güncel mimari gereksinimi, `deus_ex_machina` için CLI süreçlerinin altında çalışan bir **NT Kernel bileşenidir**. Bu gereksinim `windows/nt/` içindeki gerçek KMDF sürücü kaynağıyla başlatıldı. Sürücünün bu ilk sürümü yalnız sabit protokol / yetenek sorgusu sunar. Görev veritabanı, HTTP yüzeyi, kaynak okuma ve CLI işlemleri kullanıcı kipindedir. Sürücünün derlenmesi, imzalanması, yüklenmesi ve hedef makinede çalışmasının doğrulanması ayrı aşamalardır. [NT bileşeninin kapsamı ve derlenmesi](NT_KERNEL.md).

## Yerleşim

| Konum | Sorumluluk |
| --- | --- |
| `deus.py` | Mevcut kök betiklerini taşımayan tek giriş komutu |
| `src/ortak_kopru/core.py` | SQLite iş/ileti/çalıştırma/sonuç ilişkileri ve olaylar |
| `src/ortak_kopru/cli.py` | Yerel komutlar ve özel JSON dışa aktarımı |
| `src/ortak_kopru/server.py` | Loopback HTTP yüzeyi; kaynak yollarını dışarıya açmaz |
| `src/ortak_kopru/handoff.py` | Oturum/gelen kutusu ve tam dosyalı özel devir paketi |
| `src/ortak_kopru/backup.py` | Tutarlı SQLite/nesne yedeği ve yeni alana geri yükleme |
| `src/ortak_kopru/local_files.py` | Özel dizin, dosya bütünlüğü ve hedefi ezmeyen atomik yayım |
| `src/ortak_kopru/adapters/windows_nt.py` | Gerçek Windows aygıtını `DeviceIoControl` ile sorgulayan istemci |
| `ui/deus/` | İş, kaynak/karar, geçmiş/devir görünümleri |
| `schemas/` | Veri sözleşmelerinin sürümlü açıklamaları |
| `windows/nt/` | KMDF sürücüsü, sabit ABI ve yalnız derleme betiği |
| Git dışındaki `--state-dir` | SQLite, kaynak/çıktı baytları ve özel çalışma durumu |

Python 3.12+ yeterlidir; çalışma kodunda dış Python paketi yoktur. Veritabanı dosyasını Windows ve VM'den eşzamanlı ortak dosya olarak açmak yerine, tek yerel sahip ve onun HTTP/CLI girişleri kullanılmalıdır. Özel veri dizininin gerçek bir Git çalışma ağacı içinde olması reddedilir. POSIX dosya izinleri Windows ACL garantisi sayılmaz; özel alanın işletim sistemi erişimini kullanıcı yönetir.

## Çalışma kipi: açık seçim ve gerçek durum

Varsayılan `nt-kernel` kipidir. `python deus.py runtime` gerçek aygıtı sorgular; aygıt bulunamadığında, platform desteklenmediğinde veya protokol uyuşmadığında başarısız sonuç verir. Normal iş komutları bu durumda veri dizini açıp sessizce başka kipe geçmez. Sunucu da yeni çalışma doğuran değişikliklerde NT uç noktasını yeniden denetler. `pause` ve `cancel`, sürücü kaybolduğunda da iş kaydını durdurabilmek için kullanılabilir. `backup`, `backup-verify`, `restore` ve `handoff-verify` özel veriyi kurtarma/denetleme amacıyla sürücü yokken de çalışır. Bu işlemlerde runtime yine gerçek `ready=false`, `kernel_verified=false` durumunu bildirir; dış süreç başlatılmaz.

Geliştirme ve çevrimdışı sınama için **açıkça** `--backend portable` seçilir. Bu kipte `kernel_verified` false ve `task_execution` user-mode olarak bildirilir. NT kurulumu veya model çalıştırma kanıtı üretmez.

Yerel geliştirme örneği; `D:/DeusVeri` yerine kendi kalıcı, Git dışında kalan dizininizi seçin:

```powershell
python deus.py --backend portable --state-dir D:/DeusVeri serve
```

Sunucunun açılış çıktısındaki **`launch_url` bağlantısını** açın. Bu bağlantının fragment bölümündeki açılışa özel anahtar sunucuya URL olarak gönderilmez; arayüz anahtarı sekmenin oturum alanına aldıktan sonra adres çubuğundan kaldırır. Anahtar HTML, JavaScript veya erişim günlüğünde sunulmaz. Bağlantı yerel kullanıcıya aittir; paylaşılacak yayın bağlantısı değildir. Yalnız temiz `http://127.0.0.1:8765` adresini açmak özel API verilerine erişim vermez.

Sunucu yalnız loopback dinler. API erişiminde bu anahtar; değiştirici HTTP isteklerinde ayrıca aynı origin koşulu vardır. Anahtar yalnız bu yerel yüzeyin girişini korur; bağımsız kişi veya model kimliği kanıtı değildir. Gövde sınırları, kesin rotalar ve HTML metin kaçışı uygulanır. API dışa açık ağ hizmeti olarak tasarlanmamıştır. Yerel yönetici veya aynı kullanıcı hesabının süreçleri ayrı bir güven sınırı değildir.

İmzalı ve uygun şekilde yüklenmiş sürücü bulunan hedef Windows'ta:

```powershell
python deus.py runtime
python deus.py --state-dir D:/DeusVeri serve
```

Başarılı sorgu yalnız aygıt protokolünü doğrular. Bu sürümde çekirdekten görev çalıştırma, CLI süreçlerini yönetme veya boot başlangıcı yoktur.

## İlk iş

Yüzeyde **Yeni iş** üzerinden özgün söz, çalışma kapsamı ve tamamlanma ölçütleri girilir. İstenirse yerel kaynak dosyaları eklenir. Dosyanın o anda okunan baytları ve SHA-256 değeri özel alana alınır; özgün kaynak değiştirilmez. Bağlam paketi oluşturulurken saklanan kopyanın bütünlüğü yeniden denetlenir.

CLI karşılığı:

```powershell
python deus.py --backend portable --state-dir D:/DeusVeri create --words-file D:/Istek.txt --authority-source "Bu yerel oturumdaki kullanıcı isteği" --authority-scope "Belirtilen örnek dizinde kaynak denetimi" --criterion "Rapordaki her bulgu kaynak konumuna bağlı" --source D:/Kaynak.txt --request-key ornek-is-001
python deus.py --backend portable --state-dir D:/DeusVeri list
```

Çıktılar UTF-8 JSON'dur. `runtime` gerçek çalışma kipini, `result` işlem sonucunu taşır. Aynı isteği tekrar gönderirken aynı `request-key` kullanılır. Aynı anahtarla farklı içerik gönderimi reddedilir. Yeni niyet için yeni anahtar kullanılır. İş kimliği dönen `result.id` alanındadır.

## Gerçek oturumla alım ve dönüş

Aşağıdaki `IS_ID`, `CALISTIRMA_ID`, `OTURUM_ETIKETI` yer tutucuları, gerçek işlem sonuçları ve hedef oturumla değiştirilir. Bir etiketin verilmesi bağımsız model kimliği doğrulaması sayılmaz.

```powershell
python deus.py --backend portable --state-dir D:/DeusVeri assign IS_ID --participant "ChatGPT (Şaman)" --session OTURUM_ETIKETI --revision 1 --request-key atama-001
```

Yanıttaki `active_attempt_id`, çalıştırma kimliğidir. Hedef CLI oturumu kendi araçlarıyla şu komutu çalıştırır:

```powershell
python deus.py --backend portable --state-dir D:/DeusVeri receive CALISTIRMA_ID --session OTURUM_ETIKETI --request-key alim-001
```

Bu komut işin güncel bağlam paketini verir. **Atama otomatik bir model çağrısı değildir.** Alım yerel alıcı beyanı olarak kaydedilir; modelin anladığı veya bütün sağlayıcı bağlamının görüldüğü ileri sürülmez. Hedef oturum kendi işi sonucunda ürettiği çıktıyı bildirir:

```powershell
python deus.py --backend portable --state-dir D:/DeusVeri result CALISTIRMA_ID --session OTURUM_ETIKETI --summary-file D:/Sonuc.txt --artifact D:/Rapor.txt --request-key sonuc-001
```

İş `awaiting_verification` olur; cevap gelmesi işi kendiliğinden tamamlamaz. Çıktının özel kopyası saklanır. `current_result_id` denetimin bağlanacağı sonuçtur.

`D:/Kontroller.json` örneği:

```json
[
  {
    "criterion_id": "criterion-1",
    "result_id": "GERCEK_CURRENT_RESULT_ID",
    "passed": true,
    "evidence": "Gerçek denetimin yöntemi ve sonuç dosyası/satırı",
    "verifier": "Denetimi yapan gerçek kişi veya araç"
  }
]
```

```powershell
python deus.py --backend portable --state-dir D:/DeusVeri verify IS_ID --checks-file D:/Kontroller.json --revision 1 --request-key kontrol-001
```

Bütün ölçütler güncel sonuca bağlı geçer kaydı taşıdığında iş `completed` olur. Başarısız ölçüt işi `blocked` bırakır. Bu kayıt, yerel denetleyicinin beyanıdır; motor ölçütün anlamsal doğruluğunu veya denetleyicinin bağımsızlığını otomatik kanıtlamaz. Örnek bir JSON üretmek gerçek denetimin yerine geçmez.

## Düzeltme, duraklatma ve devir

`get IS_ID` güncel sürümü verir. Değiştirici komutlarda o sürüm `--revision` olarak kullanılır:

```powershell
python deus.py --backend portable --state-dir D:/DeusVeri revise IS_ID --words-file D:/Duzeltme.txt --revision 1 --request-key duzeltme-001
python deus.py --backend portable --state-dir D:/DeusVeri control IS_ID pause --revision 2 --request-key duraklat-001
python deus.py --backend portable --state-dir D:/DeusVeri control IS_ID resume --revision 2 --request-key devam-001
python deus.py --backend portable --state-dir D:/DeusVeri context IS_ID
python deus.py --backend portable --state-dir D:/DeusVeri events --task IS_ID
```

Düzeltme özgün sözü değiştirmez; yeni söz sürümü ekler. Güncel olmayan çalıştırma sonucu reddedilir. Pause/cancel, eski aktif çalıştırmayı geçersiz kılar. Resume işi yeniden hazır yapar; devam edecek oturum için yeni `assign` gerekir. Yeni atama aynı işte yeni çalıştırma açar. Önceki sonuçlar ve işlemler geçmişte kalır.

Etkin bir çalıştırmayı başka oturuma devrederken `get IS_ID` ile güncel `active_attempt_id` okunur ve `--expected-active-attempt-id` olarak gönderilir. Bu önkoşul, gecikmiş bir atamanın daha yeni çalıştırmayı ezmesini önler. İlk atamada veya etkin çalıştırma kalmadığında bu seçenek verilmez. Arayüz aynı önkoşulu otomatik gönderir:

```powershell
python deus.py --backend portable --state-dir D:/DeusVeri assign IS_ID --participant "Yeni oturum" --session YENI_OTURUM --revision 2 --expected-active-attempt-id GUNCEL_CALISTIRMA_ID --request-key devir-001
```

Eski bir `receive` isteğinin aynı anahtarla tekrarı da işin güncel uygunluğunu yeniden denetler. İptal, düzeltme, devir veya sonuç gönderimi sonrasında eski çalışır bağlam yeniden teslim edilmez.

Bu ilk sürümde durdurma **iş protokolünü** durdurur; bağlı olmayan dış süreçleri zorla sonlandırmaz ve gerçekleşmiş dış işlemleri geri almış sayılmaz. Durdurulmuş veya tamamlanmış iş sessizce yeniden açılmaz. Düzeltme yetki kapsamını değiştirmez; kapsamı farklı yeni istek için yeni iş oluşturulur.

## Dışa aktarım

```powershell
python deus.py --backend portable --state-dir D:/DeusVeri export --output D:/DeusYedek/olaylar.json
```

Hedef dosya önceden bulunmamalı ve Git çalışma ağacının dışında olmalı. Dışa aktarım özel iş metinlerini taşır; otomatik yayın veya tam veritabanı geri yükleme aracı değildir. SQLite ile kaynak/çıktı baytlarını birlikte korumak için `backup`, doğrulamak için `backup-verify`, yeni bir çalışma alanına almak için `restore` kullanılır. [Tam yedek ve kurtarma akışı](DEVAM_VE_YEDEK.md#tutarlı-yedekleme).

## Doğrulama ve açık kapsam

```sh
python -m unittest discover -v
python tools/depo_kontrol.py
node --check ui/deus/app.js
```

Yeni sınamalar; aynı isteğin tekrarı, eşzamanlı oluşturma, yeniden açılan veritabanı, kaynak bozulması, eski oturum/sonuç, düzeltme, pause/resume/cancel, sonuçla bağlı ölçütler, HTTP origin/belirteç ve NT protokolünü kapsar. Model veya canlı sürücü çağrısı taklitleri gerçek kurulum kanıtı sayılmaz. Windows WDK derlemesi ayrı CI akışındadır; çıktısı imzasızdır, yüklenmez.

Sonraki ayrı aşamalar: hedef Windows/WinPE sürüm ve mimarisinin doğrulanması; imzalı sürücü paketi ve hedef makine testi; süreç gözetimi için dar kapsamlı yeni kernel sözleşmesi; mevcut açık CLI'a otomatik teslim; GitHub/dosya hizmeti adaptörleri; eski HTML'yi değiştirmeden seçilmiş iş olaylarının yayın görünümü. Mevcut prototip dalları otomatik birleştirilmedi.

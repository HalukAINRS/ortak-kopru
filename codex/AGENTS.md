# Codex CLI ve Bulut

Bu dizin, Codex CLI ile Codex Bulut'un ortak ana environment olarak CLI üzerinden kullanılmasına ait köprü kaynaklarını taşır. CLI'nin remote environment hedefi kullanıcının Codex karargâhı, Bulut'un hedefi bu GitHub deposudur. Karargâhın Windows dosya yolu bulutta var sayılmaz.

Makine ayarlarının tek kaynağı `yapilandirma/bulut_bag.json` dosyasıdır. `araclar/bulut_bag.py`, yerel karargâhtaki Codex uygulamasını ve profilini kullanarak durum, ortam seçimi, görev gönderme, görev sonucu ve fark işlemlerini yürütür. Buradaki kopya, yerel araçla bulut arasında kaynak aktarımı ve inceleme içindir; Windows uygulamasını bulutta başlatma.

Açıklamaları Türkçe yaz. Görevi `codex/` alanında tut; başka kolların dosyalarını veya kökteki Copilot başlatıcısını değiştirme. Servis ortamı kimliğini depo adıyla veya sohbet kimliğiyle karıştırma; doğrulanmamış kimlik ve başarı üretme.

Depo kökünden bağımsız sınamalar:

```sh
python -B -m unittest discover -s codex/sinama -p test_bulut_bag.py -v
```

Bu sınamalar gerçek bir Codex Cloud görevi başlatmaz. Canlı bağlantı ancak gerçek görev gönderimi, doğru depo gözlemi ve geri okunan sonuçla doğrulanır.

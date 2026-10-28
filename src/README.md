# Python paketi

Bu klasör, kapının ve yerel iş bileşeninin çekirdeğini taşır. Kapı, yerel kullanıcının seçtiği dosyaları dış alana taşır ve dışarıdan istenen dosyaları kaydıyla alır. Yerel iş bileşeni işleri, olayları, devirleri ve yedekleri bilgisayarda tutar.

Kod yalnız Python'un standart kütüphanesini kullanır. Komut girişleri depo kökündedir; nasıl kullanıldıkları kapı kullanımı ve iş bileşeni rehberlerinde anlatılır.

## Bu klasörde

| Dosya | Ne | Nasıl çalışır |
| --- | --- | --- |
| [`ortak_kopru/__init__.py`](ortak_kopru/__init__.py) | Paketin girişi: kalıcı iş, kaynak ve olay sözleşmelerinin paketi. | — |
| [`ortak_kopru/core.py`](ortak_kopru/core.py) | Kalıcı iş durumu: işler, kaynaklar ve olaylar; ortak defterden ayrı, özel bir dizinde tutulur. | — |
| [`ortak_kopru/cli.py`](ortak_kopru/cli.py) | Yerel iş bileşeninin komutları (kökteki deus.py girişi): iş, kaynak, devam, yedek ve yerel sunucu. | — |
| [`ortak_kopru/server.py`](ortak_kopru/server.py) | Yerel iş deposunun yalnız bilgisayarın kendi adresinden açılan HTTP yüzü; sağlayıcı çağırmaz. | — |
| [`ortak_kopru/handoff.py`](ortak_kopru/handoff.py) | Kaydedilmiş oturumların bulunması ve sağlayıcıdan bağımsız, özel devir dosyaları; kaynaklar talimat değil veri sayılır. | — |
| [`ortak_kopru/backup.py`](ortak_kopru/backup.py) | Görev veritabanının ve nesnelerinin tutarlı, doğrulanmış özel yedekleri ve geri yüklenmesi. | — |
| [`ortak_kopru/local_files.py`](ortak_kopru/local_files.py) | Özel, doğrulanmış yerel dosyalar ve üzerine yazmadan yayımlama; Git çalışma ağacının içinde çalışmayı reddeder. | — |
| [`ortak_kopru/exchange.py`](ortak_kopru/exchange.py) | Seçilmiş dosya aktarımları: paket, aktarım kaydı ve özel aktarım dizini; işlerden ve oturumlardan bağımsız. | — |
| [`ortak_kopru/gateway.py`](ortak_kopru/gateway.py) | GitHub alışverişinin işten bağımsız akışı: açık plan, kurtarılabilir yazma ve uzlaştırma. | — |
| [`ortak_kopru/gateway_cli.py`](ortak_kopru/gateway_cli.py) | Kapının komutları (kökteki kapi.py girişi): hazırla, planla, gönder, uzlaştır, al ve dışa çıkar. | — |
| [`ortak_kopru/adapters/__init__.py`](ortak_kopru/adapters/__init__.py) | Dış hizmet bağdaştırıcılarının paketi; içe aktarılması hiçbir giriş-çıkış işlemi yapmaz. | — |
| [`ortak_kopru/adapters/github.py`](ortak_kopru/adapters/github.py) | GitHub REST bağdaştırıcısı: seçilmiş dosya alışverişi için sınırlı istekler. | — |
| [`ortak_kopru/adapters/windows_nt.py`](ortak_kopru/adapters/windows_nt.py) | Windows'taki NT aygıt kapısını okur; sürücüyü kurmaz ve yüklemez. | — |

## Nereye bağlanır

Bütün alanlar ve dosyalar [depo haritasında](../docs/harita.md#python-paketi) durur. İlk kez geliyorsanız [açılıştan](../docs/acilis.md) başlayın. Kurulum, komutlar ve denetimler [teknik ayrıntılarda](../docs/teknik/README.md) anlatılır.

Bu sayfa depo haritasından üretilir; elle değiştirilmez. Değiştirmek için haritadaki kayıt düzeltilir ve `python tools/harita.py` çalıştırılır.

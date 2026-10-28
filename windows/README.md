# Windows sürücüsü

Bu klasör, yerel iş bileşeninin Windows çekirdeğiyle konuştuğu aygıt kapısını taşır. İçinde sürücünün kaynakları, iki taraf arasındaki protokol ve derleme gereçleri var.

Sürücü otomasyonda yalnız derlenir; imzalanmaz ve hiçbir makineye yüklenmez. Derleme ve deneme adımları alt klasördeki kendi rehberindedir.

## Bu klasörde

| Dosya | Ne | Nasıl çalışır |
| --- | --- | --- |
| [`nt/README.md`](nt/README.md) | NT aygıt kapısının rehberi: amacı, derlemesi, denenmesi ve sınırları. | — |
| [`nt/deus_kernel.c`](nt/deus_kernel.c) | KMDF sürücüsünün kaynağı: denetim aygıtı ve salt okunur sorgu işleyicisi. | — |
| [`nt/deus_protocol.h`](nt/deus_protocol.h) | Kullanıcı tarafı ile sürücü arasındaki protokol: sabit boyutlu, işaretçisiz sorgu ve yanıt yapıları. | — |
| [`nt/DeusKernel.vcxproj`](nt/DeusKernel.vcxproj) | Sürücünün Visual Studio proje dosyası: derleme ayarları. | — |
| [`nt/Directory.Build.props`](nt/Directory.Build.props) | Sabitlenmiş Windows SDK ve WDK paketlerinin içe aktarımı. | — |
| [`nt/packages.config`](nt/packages.config) | Derleme için NuGet paketleri: Windows SDK ve WDK, sabit sürümle. | — |
| [`nt/build.ps1`](nt/build.ps1) | Sürücüyü yalnız Windows'ta derler; imzalamaz ve yüklemez. | `pwsh -File windows/nt/build.ps1 -Restore` |
| [`nt/.gitignore`](nt/.gitignore) | Derleme çıktıları ve indirilen paketler depoya girmez. | — |

## Nereye bağlanır

Bütün alanlar ve dosyalar [depo haritasında](../docs/harita.md#windows-sürücüsü) durur. İlk kez geliyorsanız [açılıştan](../docs/acilis.md) başlayın. Kurulum, komutlar ve denetimler [teknik ayrıntılarda](../docs/teknik/README.md) anlatılır.

Bu sayfa depo haritasından üretilir; elle değiştirilmez. Değiştirmek için haritadaki kayıt düzeltilir ve `python tools/harita.py` çalıştırılır.

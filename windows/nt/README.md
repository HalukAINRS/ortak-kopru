# deus_ex_machina — NT Kernel aygıt kapısı

`deus_kernel.sys`, NT çekirdek modunda çalışacak KMDF non-PnP sürücü
bileşenidir. Kullanıcı modundaki bağlayıcı, `\\.\DeusExMachina` aygıtına
`DeviceIoControl` ile ulaşır. Ekrandaki arayüz, iş kayıtları ve CLI işlemleri
kullanıcı modunda kalır.

Bu ilk sürümün çekirdek yeteneği **salt okunur protokol sorgusudur**. Sürücü
görev çalıştırmaz, süreç başlatmaz/durdurmaz, model/anahtar/prompt almaz.
Sürücüde süreç gözetimi, iş yetkisi uygulaması veya önyükleme entegrasyonu
gerçekleştirilmiş sayılmaz. `query` dışındaki yetenek biti yoktur.

## Kaynak ve derleme

| Dosya | İşlev |
| --- | --- |
| `deus_kernel.c` | KMDF sürücü girişi, System/Admin aygıt erişimi, tek IOCTL |
| `deus_protocol.h` | Sabit boyutlu protokol 1 ABI |
| `DeusKernel.vcxproj` | x64 Debug/Release WDK projesi |
| `packages.config`, `Directory.Build.props` | Microsoft SDK/WDK 10.0.26100.6584 bağımlılıkları |
| `build.ps1` | Derler ve çıktı karmasını gösterir; imzalama/kurma/yükleme yapmaz |
| `../../src/ortak_kopru/adapters/windows_nt.py` | Gerçek aygıtı sorgulayan Python/Win32 bağlayıcısı |

Visual Studio C++ ve uyumlu WDK/MSBuild ortamında:

```powershell
pwsh -File windows/nt/build.ps1 -Restore
```

`nuget` ve `msbuild` PATH'te olmalıdır. Paketler resmî NuGet kaynağından,
sabit sürümlerle alınır. Çıktı `windows/nt/build/x64/Release/deus_kernel.sys`
olur. Yerelde kurulu uyumlu WDK varsa `-Restore` kullanılmadan da proje
derlenebilir. Derleme çıktısı gerçek test makinesine otomatik kopyalanmaz.

Proje, Microsoft'un KMDF non-PnP örneğindeki sürücü ayarları ve NuGet import
düzenine göre hazırlanmıştır. Windows 10+ non-PnP KMDF kurulumu SCM üzerinden
yapılabildiği için eski co-installer ve gereksiz INF eklenmemiştir.

## Protokol 1

- Aygıt türü: `0x8000`; işlev: `0x800`; aktarım: `METHOD_BUFFERED`.
- IOCTL: `0x80006000`; açık tutamaçta okuma hakkı gerekir.
- ACL: yalnız LocalSystem ve yükseltilmiş Administrators.
- İstek: 16 bayt — `uint32 size`, `uint32 version`, `uint64 nonce`.
- Yanıt: 32 bayt — `uint32 size`, `uint32 magic`, `uint32 version`,
  `uint32 capabilities`, `uint64 nonce`, `uint64 interrupt_time_100ns`.
- Tamsayılar little endian; magic `0x53554544`, sürüm `1`, capability `1`.
- Sürücü yalnız tam boyutlu ve doğru sürümlü isteği kabul eder. Yanıt alanı
  sıfırlanır; tampon dışında veya kullanıcı işaretçisi üzerinden erişim yoktur.
- Rastgele nonce, cevabın o sorguya bağlanmasını sağlar. Kriptografik sürücü
  kimlik doğrulaması veya bütün sistemin güvenilirliği iddiası taşımaz.

Bağlayıcı boyut, magic, sürüm, yetenekler ve nonce'ı doğrular. Eksik aygıtta,
uyumsuz yanıtta ve Windows dışındaki ortamda `ready=false` döndürür.
`strict=True` başarısızlıkta `KernelUnavailable` yükseltir. Portable arka uca
sessiz geçiş yapmaz.

## Gerçekleşme ölçütleri

1. Python protokol testinin geçmesi, yalnız bağlayıcının sahte paketleri doğru
   ayırdığını gösterir.
2. WDK derlemesinin geçmesi, `.sys` üretildiğini gösterir.
3. Hedef sistemin kabul ettiği imzalı sürücünün kurulu ve yüklenmiş olması,
   ayrıca doğrulanır.
4. Gerçek `DeviceIoControl` karşılığı, yalnız o anda protokol kapısına
   ulaşılabildiğini gösterir. İşlerin çekirdekte yürütüldüğünü göstermez.

Canlı doğrulama, uygun imzalı sürücü ve hedef Windows makinesi gerektirir.
Kurulum, önyükleme ayarları, sürücü imza ilkeleri ve mevcut güvenlik araçları
bu derleme betiği tarafından değiştirilmez. Dağıtım ve geri alma planı,
sürücü paketi ve hedef sistem bilgileriyle ayrıca ele alınır.

Mimari yerleşim ve kapsam: [NT Kernel kararı](../../docs/teknik/nt-kernel.md).

## Birincil kaynaklar

- [Microsoft: KMDF non-PnP sürücü kuralları](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/using-kernel-mode-driver-framework-with-non-pnp-drivers)
- [Microsoft: Windows 10+ non-PnP kurulumu](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/installing-a-non-pnp-driver)
- [Microsoft: MSBuild ile sürücü derleme](https://learn.microsoft.com/en-us/windows-hardware/drivers/develop/building-a-driver)
- [Microsoft: WDK NuGet](https://learn.microsoft.com/en-us/windows-hardware/drivers/install-the-wdk-using-nuget)
- [Microsoft non-PnP kaynak örneği](https://github.com/microsoft/Windows-driver-samples/tree/main/general/ioctl/kmdf)
- [Seçilen Microsoft WDK paketi](https://www.nuget.org/packages/Microsoft.Windows.WDK.x64/10.0.26100.6584)

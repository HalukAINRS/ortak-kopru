# Şaman'da bu bağlamla devam etme

## Önce mevcut açık Şaman oturumunu sürdür

k-0111 ve [kaynak devri kaydı](../../deus_ex_machina/KAYNAK_DEVRI_20261024.md), Şaman CLI'da 519 görünür mesajın alınmasını ve 80 defter eşlemesinin tamamlanmasını bildiriyor. Zaten açık Şaman oturumu varsa yeni paketin o oturumda okunması önce gelir; bu çalışma baştan başlatılmaz. Bu web hazırlığı mevcut CLI'yı başlatmış değildir ve bu yeni ek paketin alındı kaydını onun yerine üretmez.

Ana köprü deposunun güncel `main` sürümü başlatıcıyı içerir. Yerel köprü klasöründe uzaktaki değişiklikler alınır ve yalnız dosyalar hazırlanır:

```powershell
git pull --ff-only
.\Kopru_Izle.cmd SamanHazirla
```

`git pull --ff-only` yerel dal ayrışmışsa durur; kullanıcının değişikliklerini silerek düzeltme yapılmaz. Bu durumda güncel `saman_devral.py` dosyası güvenli ayrı kopyadan kullanılabilir veya yerel değişiklikler korunarak Git durumu uzlaştırılır. Başlatıcı kendi başına mevcut ana çalışma ağacını değiştirmez.

Hazırlığın bildirdiği gerçek çalışma ağacı yolundaki `AGENTS.md` ve `devir/saman/CLI_BASLANGIC.md`, mevcut Şaman oturumunda açıkça okunur. O oturuma verilecek görev: **“Hazırlanan çalışma ağacındaki AGENTS.md ve devir/saman/CLI_BASLANGIC.md dosyalarını oku; k-0111'deki tamamlanmış kaynak işini ve mevcut ilerlemeyi koruyarak bu yeni ek paketin kabulünü kaydet, açık kalan işlerden devam et.”** Gerçek yol hazırlık çıktısından alınır; göreli yolun başka çalışma dizinine işaret ettiği varsayılmaz. Dosyaların hazırlanması, okunması ve kabulü ayrı olaylardır.

## Yeni etkileşimli oturum alternatifi

Açık oturum bulunmuyorsa veya ayrı oturumla devam edilecekse:

```powershell
.\Kopru_Izle.cmd SamanDevam
```

Bu komut yeni etkileşimli CLI başlangıcıdır. Önceki sohbetin veya başka bir CLI sürecinin belleğini aynı sürece aktardığı iddiası taşımaz. Hangi oturumun devam ettiği gerçek CLI kaydında belirtilir.

## Ne yapar?

Başlatıcı, mevcut `deus-ex-machina-2026-10-24` dalındaki sabit devir commit'ini alır. Repo yanında `<depo-adı>-saman` adlı (mevcut kurulumda `kopru-saman`) ayrı bir Git çalışma ağacı ve `saman-devam-2026-10-24` adlı yerel dal hazırlar. Paket dosyalarını sabit commit'teki `MANIFESTO.json` ile karşılaştırır. Hazırlama kipinde burada durur. Etkileşimli kipte yerel ayarlardaki Şaman ikilisini açar; kısa başlangıç girdisi `AGENTS.md` ve devir dosyalarını gerçek oturumda okumayı ister.

Model, izin ve sandbox seçimi için yeni bir komut satırı tercihi eklemez. Yeni çocuk sürecin ortamı, mevcut `ayarlar-yerel.json` içindeki Şaman ortamından gelir; kimlik dosyalarının içeriği okunmaz. Bu ortamın zaten açık başka oturuma kendiliğinden uygulandığı varsayılmaz. Ana köprünün eski bütün-kayıt bot yanıtı çağrılmaz. Bu ek paketin gerçek kabulünü hedef Şaman oturumu kendi gözlemleriyle yazar.

## Yalnız hazırlama

```powershell
.\Kopru_Izle.cmd SamanHazirla
```

Bu modda dosyalar alınır ve doğrulanır; model çağrısı yapılmaz. Hazırlanmış dosya, CLI tarafından okunmuş dosya sayılmaz.

## Özgün kaynak ZIP'i

`Steering_Evrak_Okuma_Paketi.zip` hedef makinede varsa yeni oturum açmadan hazırlığa tanıtılabilir:

```powershell
python saman_devral.py --hazirla --kaynak-zip "D:\OzelKaynaklar\Steering_Evrak_Okuma_Paketi.zip"
```

Yukarıdaki `D:\OzelKaynaklar` örnek yoldur; kullanıcının gerçek yolu olduğu iddia edilmez. Başlatıcı dosyanın boyutunu ve SHA-256 değerini bilinen özgün arşivle karşılaştırır. Dosyayı Git'e kopyalamaz; özel yerel hazırlık kaydında gerçek yolu tutar. Yeni etkileşimli oturum yolu da `--kaynak-zip` seçeneğini kabul eder. Arşiv sunulmadıysa raporlar ve repo ile çalışma devam edebilir; yalnız bu arşivin hedefte doğrulanmamış erişimi açık kalır. Bu eksik, k-0111'deki görünür mesaj/defter eşlemesini yeniden açmaz.

## Doğrudan Python seçenekleri

Python ve Git erişilebiliyorsa mevcut oturuma dosya hazırlama `python saman_devral.py --hazirla`, yeni etkileşimli oturum ise `python saman_devral.py` ile başlar. `--hazirla`, `--hedef`, `--dal`, `--codex` ve `--kaynak-zip` seçenekleri `--help` içinde açıklanır. Farklı hedef/ikili kullanımı açıkça seçilir; mevcut Şaman ortamı sessizce başka kurulumla değiştirilmez.

Tekrar başlatmada aynı worktree/dalın kaynak depoya ve sabit devir commit'ine bağlı olduğu doğrulanır. Sabit paket dosyası değiştirilmişse doğrulama bunu bildirir; ilerleme dosyaları ve kullanıcı değişiklikleri silinmez. Önceden açık bir Codex oturumunu devam ettirmek istenirse o gerçek oturumun kimliği CLI'da belirlenir; başlatıcı rastgele en son oturumu seçmez.

## Doğrulama sınırı

Başlatıcı geçici Git depoları ve sahte yerel yürütülebilir dosya ile çevrimdışı doğrulanabilir. Hedef Windows'taki Codex, PowerShell, giriş ve çalışma zamanı davranışı gerçek makinede ayrıca gözlenir. Bu paketin yayımlanması veya hazırlık testinin geçmesi, o hedef makinede çalıştırıldığı beyanı değildir.

## Resmî CLI davranışının kaynağı

Codex'in alt komut verilmeden etkileşimli terminal arayüzünü açması ve proje `AGENTS.md` keşfi, 24 Ekim 2026'da [CLI belgelerinden](https://learn.chatgpt.com/docs/developer-commands?surface=cli) ve [AGENTS.md belgesinden](https://learn.chatgpt.com/docs/agent-configuration/agents-md) kontrol edildi. Hedefte kurulu sürüm farklıysa yardım çıktısı esas alınır; başlatıcı yeni sürüm/model yüklemez.

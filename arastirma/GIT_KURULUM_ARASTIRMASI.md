# Son düzen için Git ve Windows hazırlığı

Kullanıcının son onayı CLI tabanlı Codex CLI + Codex Bulut düzeninin
gerçekleştirilmesini ve otantik denemeleri kapsar. Ortam yayınlama yapılmaz.

## Doğrulanan dış kaynaklar

- Git `clone --branch` seçilen dalı checkout eder. Bu sayede uygulamanın main
  dosyalarını değiştirmeden `divan-kurulum` dağıtım dalı alınabilir.
  https://github.com/git/git/blob/master/Documentation/git-clone.adoc
- Git Credential Manager, Git for Windows dağıtımında yer alır; ilk erişimde
  hesap girişi gerektiğinde kendi güvenli akışını kullanır. Cloud proxy hesabı,
  kullanıcının Windows hesabına taşınmaz ve orada oturum açılmış sayılmaz.
  https://github.com/git-ecosystem/git-credential-manager/blob/main/docs/install.md
  https://github.com/git-ecosystem/git-credential-manager/blob/main/README.md
- PowerShell sürüm doğrulaması resmî Microsoft PowerShell GitHub varlıkları ve
  SHA-256 manifestiyle yapıldı. Linux taşınabilir PowerShell 7.6.9 kuruldu;
  Windows betik mantığı bu gerçek runtime üzerinde sınanabilir. Windows Y:
  sürücüsü veya Windows kimlik doğrulaması bu denemeyle doğrulanmaz.
  https://github.com/PowerShell/PowerShell/releases/tag/v7.6.9

## Uygulama sınırları

Ana checkout/HEAD/index ve main dalı korunur. Kod dağıtımı `divan-kurulum`,
yalnızca yeni 0 zarflarının değişimi `divan-paylasim` dalındadır. Kurulum arşivi
çalışma sonuçları, alındılar, yerel denetim durumu, üye kaydı ve özel sohbet
adreslerini içermez. Windows yardımcıları mevcut farklı dosyaları ezmez.

GitHub yazma hakkı dry-run ile sınanmıştır; tamamlanmış gerçek push ve yeniden
okuma sonuçları ayrıca uygulama kaydında tutulur. Simüle edilmiş PowerShell
katılımı gerçek Windows CLI katılımı olarak raporlanmaz.

Codex Bulut için `codex_cloud` ayrı protokol kimliği eklendi; Windows Codex CLI
`codex_cli` kimliğini kullanır. Başlangıç belgesindeki altı kimlik korunur.
İki ayrı oturum birbirinin tamamlanma/katılım kaydını taklit etmez.

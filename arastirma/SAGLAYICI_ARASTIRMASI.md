# Divan sağlayıcı araştırması — 10 Kasım 2026

Çalıştırıcı: a6c424bed674. Önce salt okunur araştırma, ardından sürümleri sabitlenmiş yerel CLI hazırlığı yapıldı; model çağrısı, dış mesaj veya GitHub push yapılmadı.

## Doğrulanmış olgular

- Claude Code resmî README: terminal kodlama aracıdır; codebase ve Git iş akışlarını işler. Linux önerilen kurulum `https://claude.ai/install.sh`; Windows install.ps1 veya `winget install Anthropic.ClaudeCode`. NPM `@anthropic-ai/claude-code` resmî belgede hâlâ bulunur fakat deprecated olarak işaretli. NPM kayıt sorgusu sürüm 2.1.322, Node>=22.0.0, platforma özel optional paketler (ör. @anthropic-ai/claude-code-linux-x64@2.1.322) gösterdi. README'deki Node18+ rozeti güncel paket manifestiyle çelişiyor; kurulum için manifest esas alınmalı.
- Gemini CLI @google/gemini-cli 0.67.0, Node>=20. Yerel dosya okuma/yazma ve run_shell_command araçları resmî kaynakta belgeli; paylaşılan dizine/Git'e teknik olarak bağlanabilir.
- Aynı Gemini README'nin güncel durum bildirimi: `gemini` Gemini Code Assist Standard/Enterprise ve legacy paid API/Vertex kullanımına yöneltiliyor; bireysel/Google AI Pro-Ultra yeni coding-terminal yolu Antigravity CLI `agy`. Ayrıntılı auth belgesinde hâlâ bireysel hesap login açıklamaları bulunuyor; bu eski ayrıntılarla güncel durum bildirimi arasındaki fark nedeniyle bireysel hesap erişimi varsayılmamalı.
- Antigravity CLI `agy` adı resmî Google Gemini README'siyle doğrulandı. Resmî product/download/migration adresleri antigravity.google alanında. Bu ortamda alan 403; ayrıntılı installer doğrulanamadı. @google/antigravity-cli ve @google/antigravity isimlerini salt metadata olarak sorgulamak 404 döndürdü; tahmini npm paketi kurulması uygun değil.
- Gemini resmî kurulum belgesi Gemini CLI'nin Cloud Shell ve Cloud Workstations'ta önceden bulunduğunu söyler. Auth belgesi Cloud Shell kimliğiyle tipik otomatik girişten söz eder; headless mod önceden cached auth yoksa API key/Vertex ister. Bu Codex makinesinin Google kimliğine sahip olduğunu göstermez.
- MCP filesystem referans sunucusu stdio taşımayla dizin kısıtlamalı read/write sağlar. Yerel stdio server kurulması bir web sohbetine kendiliğinden ağ erişimi sağlamaz. Web ChatGPT/Claude/Gemini ayrı bağlı dosya veya yazabilen Git aracı olmadan aynı /workspace klasörünü göremez; böyle bir bağlantı bu oturumda denenmedi. CLI'nin çalışması web ürününe bağlantı kanıtı sayılmaz.

## Katılım düzeni

1. Aynı makinedeki gerçek CLI: doğru sağlayıcı kimliğiyle yalnızca `divan.py`/`divan_git.py` yardımcılarını çalıştırır. İlk katılımda read/write gidiş-dönüşü + nonce yanıtı gerçek oturumda doğrulanmalı.
2. Ayrı ortam/Cloud Shell: kendi mevcut checkout'una ve kendi Divan köküne yardımcılar kurulur; kendisi origin/divan-paylasim pull yapar, yeni0 üretir, yetkili push yapar. Git okuma, Git yazma ve model auth ayrı denetlenir.
3. Web üyesi: önce gerçek bağlı dosya/Git araç erişimi ve gerekli yazma yetkisi sağlanır. Dosya yüklemesi veya Windows yolunu sohbete yazmak canlı ortak bağlama değildir. Bağlantı yoksa hazır/çalışıyor gösterilmez.
4. Kullanıcı hiçbir üyeler arası mesajı kopyalamaz; ilk araç bağlantısı/hesap girişini kullanıcı yapabilir. Katılımcı ajan kendi kutusunu döngüsünde kontrol eder. Sürekli çalışan model/zamanlayıcı gerçekten kurulmadıysa varmış gibi gösterilmez.

## Resmî kaynaklar

- https://github.com/anthropics/claude-code/blob/6e1e44f6433bfa17d198e932bff53373aa229eea/README.md
- https://registry.npmjs.org/@anthropic-ai%2Fclaude-code/2.1.322
- https://github.com/google-gemini/gemini-cli/blob/1930f25394c4b6338b64ffdb43083fca41614798/README.md
- https://github.com/google-gemini/gemini-cli/blob/1930f25394c4b6338b64ffdb43083fca41614798/docs/get-started/installation.mdx
- https://github.com/google-gemini/gemini-cli/blob/1930f25394c4b6338b64ffdb43083fca41614798/docs/get-started/authentication.mdx
- https://github.com/google-gemini/gemini-cli/blob/1930f25394c4b6338b64ffdb43083fca41614798/docs/tools/file-system.md
- https://github.com/google-gemini/gemini-cli/blob/1930f25394c4b6338b64ffdb43083fca41614798/docs/tools/shell.md
- https://registry.npmjs.org/@google%2Fgemini-cli/0.67.0
- https://antigravity.google/product/antigravity-cli (resmî README bağlantısı; doğrudan erişim403)
- https://antigravity.google/docs/cli/gcli-migration (resmî README bağlantısı; doğrudan erişim403)
- https://github.com/GoogleCloudPlatform/cloud-shell-tutorials/blob/0fe053da507ac3969c3b3a2455c9c6a5bc25cf97/README.md
- https://github.com/modelcontextprotocol/servers/blob/main/src/filesystem/README.md

Doğrudan docs.cloud.google.com, code.claude.com, help.openai.com ve antigravity.google istekleri 403 aldı. İndirilebilen dış kaynaklar resmî GitHub raw dosyaları ve npm paket metadata idi.

## Gerçek CLI hazırlığı (ana ajanın sonraki açık yetkilendirmesiyle)

- Native Claude install.sh HEAD isteği CONNECT403 verdi. Resmî README'nin dokumente ettiği npm fallback kullanıldı; deprecated olduğu kayda geçirildi.
- `npm install --prefix /workspace/tools/divan-clients --save-exact --no-audit --no-fund @anthropic-ai/claude-code@2.1.322 @google/gemini-cli@0.67.0` exit0; 9 paket kuruldu.
- Node24.22.1 iki motor gereksinimini karşılıyor. package.json ve package-lock.json yalnızca bu yeni yardımcı dizinde yazıldı; SRI kayıtları mevcut. TLS/integrity kapatılmadı, global PATH değiştirilmedi.
- `/workspace/tools/divan-clients/node_modules/.bin/claude --version` → 2.1.322 (Claude Code), exit0. `--help` exit0.
- `/workspace/tools/divan-clients/node_modules/.bin/gemini --version` → 0.67.0, exit0. `--help` exit0.
- Kimlik doğrulama, model çağrısı veya sağlayıcı oturumuna mesaj yapılmadı; araçların başlatılabilirliği doğrulandı. Gerçek Claude/Gemini/Antigravity üyeleri bağlı sayılmadı.

# Son karar: Codex CLI + Codex Bulut

| Katılımcı | Ana environment | Remote environment / çalışma hedefi |
| --- | --- | --- |
| Codex CLI | CLI | `Y:\02_karargahlar\01_codex_karargahı` |
| Codex Bulut | CLI | `HalukAINRS/ortak-kopru` GitHub deposu |

Bu adlar kullanıcının ortak çalışma düzenindeki rollerdir. Dosya yolu ve GitHub
deposu, native Codex executor kaydı veya bağlı disk gibi gösterilmez.

Windows karargâhı yerel çalışma merkezidir. Bulut, GitHub deposunun mevcut
`/workspace/ortak-kopru` checkout'u üzerinden çalışır. İki taraf yeni 0 girdilerini
Git üzerinden paylaşır; tamamlanan 1 sonuçları kendi çalışma alanlarında kalır.
Katılımcılar kendi okuma/yazma döngülerini yürütür; kullanıcı mesaj taşımaz.

Windows tarafında mevcut ortak-kopru checkout'u kullanılır; yoksa ilk kurulumda
karargâh altında klonlanabilir. Kullanıcının mevcut klasörü körlemesine
klonlanmaz veya sıfırlanmaz. Yardımcı komutlara gerçek `--root` ve `--repo`
yolları verilir. Bulut tarafında aynı protokol /workspace/divan üzerinden hazırdır.
Gerekli ilk hesap/araç bağlantısından sonra kullanıcı aracı olmadan aktarım yapılır.

Kod dağıtım dalı `divan-kurulum`, mesaj dalı `divan-paylasim` olur. Gerçek GitHub
yazma ve Windows katılımı, ayrı uygulama kayıtlarıyla doğrulanır; rol kaydı veya
yerel test bu kanıt yerine geçmez. İki dosya sistemi canlı tek klasör olarak
bağlanmış değildir. Windows kurulumu için `windows/README.md` ve yardımcıları
kullanılır. `codex_cli` Windows katılımcısı, `codex_cloud` bulut katılımcısıdır.

Önceki Windows app-server + bulut exec-server denemesi /workspace/karargah-kopru
altında araştırma olarak saklandı. Güncel planın etkin bağlantısı değildir.
Kaynak readme.txt ve talimatlar.txt değiştirilmedi.

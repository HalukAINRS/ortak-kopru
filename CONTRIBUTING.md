# Katkı ve bakım

Ortak Köprü'ye bir kaynağı açıklayarak, bir yazıdaki bir yoruma karşılık vererek, bir hata bildirerek veya dosya değişikliği önererek katkıda bulunabilirsiniz. Önce bugün nerede durulduğunu gösteren [yol sayfasına](docs/yol.md) ve katkınızın ilgili olduğu yazıya bakın; tarihli kaynaklar [kaynak rehberindedir](docs/gecmis/kaynaklar.md). Bu yerde geçen kelimeler [sözlükte](docs/sozluk.md) açıklanır. Bir dosyanın yerini ve eski adını bulmak için [depo haritası](docs/harita.md) kullanılabilir.

## Okuyucu geri dönüşü

Sorunuzu veya düzeltmenizi [karşılık formuyla](https://github.com/HalukAINRS/ortak-kopru/issues/new?template=karsilik.yml) bir Issue açarak iletebilirsiniz. Web'deki okuma sayfalarında her bölümün sonundaki karşılık bağlantısı bu formu, sayfa ve bölüm adresi yazılmış olarak açar. Formu doğrudan açtığınızda hangi belgeye, başlığa, kayıt numarasına veya sürüme karşılık verdiğinizi belirtmeniz, geri dönüşün doğru yere bağlanmasına yardımcı olur. Ardından neyi farklı anladığınızı, hangi bilginin eklendiğini veya hangi sorunun açık kaldığını kendi sözlerinizle anlatın. Varsa kaynak bağlantısını ekleyin; bilinmeyen bir alanı doldurmak için tahmin üretmeniz gerekmez.

Doğrudan bir metin veya kod değişikliği önermek için çalışma dalınızdan pull request açabilirsiniz. Değişikliğin gerekçesini ve etkilediği kaydı açıklayın. Geçmişteki bir sözü düzeltirken eski kayıt korunur; yeni açıklama o kayda bağlanır. Yayımlanmış bir model yorumu, kullanıcının özgün sözü gibi yeniden yazılmaz.

Issues ve pull request sayfaları herkese açıktır. Paylaşılacak alıntıyı ve dosyayı bu kapsam için seçin; özel konuşmaların tamamını, kişisel çalışma alanını veya erişim bilgilerini eklemeyin. Bir katkının gelmesi, okunması, değerlendirilmesi ve uygulanması ayrı kayıtlardır. Yanıt verilmemesi kabul anlamına gelmez; Issue açılması da yerel CLI işlerini kendiliğinden başlatmaz.

Belge katkısında değişen metni, kaynak adreslerini ve bağlantıları kontrol edin; yapmadığınız bir denetimi yapılmış olarak yazmayın. Kod, yapılandırma veya çalışma davranışı değiştiğinde aşağıdaki teknik katkı ve doğrulama akışı uygulanır.

## Teknik katkı

Çalışma ortamı: **Python 3.12 veya üstü ve Git**. Python betikleri ve testler standart kütüphaneyi kullanır; paket kurulumu gerekmez. Bazı Linux ve macOS makinelerinde komut `python` yerine `python3` adıyla bulunur. Node, Bash ve PowerShell 7 isteğe bağlıdır: yalnız ilgili sözdizimi kontrolleri için gerekir, yoksa o kontrol `ATLANDI` yazar. Yerel Windows tarafının durumu ve kurulumu [yerel taraf sayfasındadır](docs/teknik/yerel-taraf.md).

```sh
git clone https://github.com/HalukAINRS/ortak-kopru
cd ortak-kopru
python tools/dogrula.py
```

1. Güncel ana daldan çalışma dalı açın. Tarihli konu ve araştırma dalları [geçmiş işlerde](docs/gecmis/README.md#dallar-ve-arşivler) listelenir.
2. Değişiklikten önce ilgili dosyanın klasöründeki giriş sayfasını ya da haritadaki tanımını okuyun (`python tools/harita.py --nerede AD`). Köprüdeki eski iş emirleri yeni iş yetkisi sayılmaz.
3. Gerçek hata için sentetik verili regresyon ekleyin. Testlerde canlı sağlayıcı, kişisel CLI oturumu veya kanonik sayfaya yazım kullanmayın.
4. Depo kökünde doğrulayın:

   ```sh
   python tools/dogrula.py
   ```

   Bu komut CI ile aynı kontrol listesini koşar; liste için `python tools/dogrula.py --liste`, her kontrolün ne denetlediği için [bakım rehberi](docs/teknik/bakim.md#tek-doğrulama-yolu). Makinede bulunmayan araç için ilgili kontrol `ATLANDI` yazılır; PR açıklamasında bunu belirtin.

5. PR açıklamasına sorunu, değişen davranışı ve çalıştırılan kontrolleri yazın. CI'nin Linux ve Windows sonuçlarını kontrol edin.

## Yeni dosyalar ve belgeler: yer ve üç sıfır kuralı

Teknik ayrıntılar ve geçmiş işler ayrı yerlerde durur: teknik belgeler `docs/teknik/`, geçmiş işlerin anlatıları ve kayıtları `docs/gecmis/` altındadır. İlk kez gelen okuyucuya dönük metinler (açılış belgesi ve README) teknik ayrıntı taşımaz; onlar [açılış kaydından](docs/acilis.json) üretilir. Her dosyanın alanı ve adlandırma kuralları [depo haritasında](docs/harita.md) yazılıdır.

Yeni bir dosya ya da belge üç sıfır kuralına uyar:

- **Sıfır okuyucu.** Belge, hiç bilmeyen birinin ne olduğunu, kimin için olduğunu ve sonra nereye gideceğini anlayacağı bir paragrafla açılır. Bu paragrafta kod biçimi ve dosya adı bulunmaz; cümleler kısadır.
- **Sıfır makine.** Dosya [harita kaydına](docs/harita.json) alanı, türü ve tek cümlelik tanımıyla girer. Üretilen bir dosyaysa kaynağı ve aracı, çalıştırılan bir dosyaysa depo kökünden komutu, denetlenen bir dosyaysa denetim komutu yazılır. Yalnız okuyan komutlar testlerde gerçekten çalıştırılır.
- **Sıfır alan.** Yeni belge ve kayıtlar haritada künyeleriyle durur: sahibi, hazırlayan, tarih, kaynakları ve kimin için yazıldığı. Deponun tamamı [CITATION.cff](CITATION.cff) ile kaynak gösterilir. Bir dosyanın yeri ya da adı değişirse eski adı haritada kalır.

Bu düzenden önce açılmış bir öneri, birleşmeden önce yeni yerleşime taşınır: dal yeni ana dalın üzerine alınır, yeri değişen dosyanın yeni yolu `python tools/harita.py --nerede ESKI_AD` ile bulunur, yeni klasörler haritada bir alana bağlanır. Bekleyen bütün önerilerin hangi dosyasının taşınması gerektiğini `python tools/donusum.py --dallar` çıkarır; bunun için önce dalların ve önerilerin çekilmesi gerekir: `git fetch origin '+refs/heads/*:refs/remotes/origin/*' '+refs/pull/*/head:refs/remotes/origin/pr/*'`; sonuç [dönüşümün teknik ekindedir](docs/gecmis/donusum-teknik.md#bekleyen-öteki-öneriler).

`python tools/harita.py --check` bu kuralları denetler; ayrıca her dosyanın tam bir alanda durduğunu sınar. Kontrol `python tools/dogrula.py` listesindedir.

## Köprü ve arşiv bütünlüğü

Bu depoda `kopru.html` kayıtları yalnız `defter/kopru_ekle.py` ile eklenir; bu, deponun kuralıdır. Defterin kendi kurallar bölümündeki elle şablon yolu 26 Ekim düzenine aittir. Önceki bir kaydı düzeltmek için yeni kayıt açıp `--yanit` ile dayanak verin; başkasının geçmiş kaydını değiştirmeyin. Gerçek rolünüzü imzalayın; ayrıntı [ortak defter sayfasındadır](docs/teknik/ortak-defter.md#deftere-yazmak).

Kanonik sayfa değiştiğinde aynayı üretin:

```sh
python defter/kopru_ayna_uret.py kopru.html ayna/kopru.html
python tools/depo_kontrol.py
```

Tarihli kayıtlar (`docs/gecmis/` altındakiler) kendi kesitinde kalır; bugünkü sayılar onlara yazılmaz. Üretilen belgeler elle düzenlenmez; değişiklik kaydında yapılır ve aracı belgeyi yeniden yazar:

| Kayıt | Araç | Yazdığı belgeler |
| --- | --- | --- |
| [açılış kaydı](docs/acilis.json) | `python tools/acilis.py` | README ve Web girişinin açılış bölümü, açılış belgesi, açılışın teknik eki |
| [yol kaydı](docs/yol.json) | `python tools/yol.py` | yol sayfası ve teknik eki |
| [dönüşüm kaydı](docs/gecmis/donusum.json) | `python tools/donusum.py` | geçmişteki dönüşüm sayfası ve teknik eki |
| [harita kaydı](docs/harita.json) | `python tools/harita.py` | depo haritası ve her alan klasörünün giriş sayfası |

Ardından Web sayfaları için `python tools/okuma_yayini_uret.py` çalıştırılır. Her aracın `--check` kipi yazmadan denetler.

`schemas/` altındaki bir sözleşmeyi veya onu üreten kodu değiştirirken `python tools/sema_denetle.py` ile şemanın desteklenen alt kümede kaldığını, `python -m unittest tests.test_semalar` ile de çekirdeğin ürettiği nesnelerin sözleşmeye hâlâ uyduğunu kontrol edin; ikisi de dış paket istemez.

`ayna/kopru.html` üretilen dosyadır. `kayit/` altındaki çağrı kayıtları geçmiş çağrıların kanıtıdır: var olan dosya değiştirilmez, taşınmaz ve silinmez; bot yalnız yeni dosya ekler ve `atlandi.log` sonuna satır yazar. Neyin hiç paylaşılmadığı ve yanlışlıkla paylaşılmış bir gizli bilgiyi görürseniz ne yapılacağı [güvenlik ve gizlilik sayfasındadır](.github/SECURITY.md).

Dışarıdan adresle çağrılanların adları ve yerleri değişmez: ortak defter, aynası, çağrı kayıtları, Web sayfaları ve kökteki üç komut (`kapi.py`, `deus.py`, `Kopru_Izle.cmd`). Başka bir dosya taşınırsa eski adı haritada kalır.

## Çakışma çözümü

Göndericilerin defteri, aynayı ve satır günlüklerini nasıl birleştirdiği [ortak defter sayfasındadır](docs/teknik/ortak-defter.md#birden-çok-yazan). Başka bir dosyada birleştirme durursa `git status` ile inceleyin, iki tarafın içeriğini koruyarak elle çözün ve kontrolleri tekrarlayın. Zorlamalı gönderim bakım akışının parçası değildir.

## Statik okuma sayfaları

Web sayfaları kökte durur ve her biri `docs/` altındaki bir Markdown kaynağından üretilir; hangi sayfanın hangi kaynaktan geldiği [depo haritasının Web sayfaları bölümünde](docs/harita.md#web-sayfaları) yazılıdır. Açılış belgesi ilk kez gelen okuyucu içindir; orada teknik ayrıntı yerine sade dil kullanın, teknik karşılıklar `docs/teknik/` altına gider. Metinleri Markdown dosyalarında düzenleyip depo kökünde `python tools/okuma_yayini_uret.py` çalıştırın; oluşan HTML dosyalarını da değişiklikle birlikte kaydedin. `python tools/okuma_yayini_uret.py --check`, dosyalara yazmadan kaynaklarla uyumu denetler; aynı kontrol CI akışında da çalışır.

Klavye çizimleri (ressam: manzara, mimar: plan ve kesit, mühendis: akış, durum ve ölçü) içeriği destekler; her çizimden önce onu anlatan bir paragraf ve `**Başlık** · ressam çizimi` biçiminde bir etiket gelir. Çizimde yalnız tek genişlikli karakterler (ASCII, Türkçe harfler, oklar, kutu çizgileri, blok öğeleri, geometrik şekiller) kullanılır, satır en çok 64 sütundur; kurallar `tools/cizim.py` içindedir ve künyeli her belgede denetlenir. Klavye çizimleri için üç ters tırnakla açılıp kapanan düz metin blokları kullanın. Açılış çiti etiketsiz veya `text` etiketli olabilir; kapanış çiti etiketsiz üç ters tırnaktır. Blok içindeki boşluklar, boş satırlar ve satır sonları korunur; içerik HTML veya bağlantı olarak yorumlanmaz. Desteklenmeyen etiket/çit ya da kapanmayan ve eşleşmeyen çit üretimi açık hatayla durdurur. Başlık, paragraf ve diğer mevcut desteklenen biçimler aynı şekilde kullanılabilir; genel Markdown veya ham HTML desteği yoktur.

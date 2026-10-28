# Dönüşüm: bugünkü depodan yeni oluşuma

<!-- uretilen:donusum -->

Bu sayfa, Ortak Köprü deposunun 28 Ekim 2026'da bugünkü düzenine nasıl geçtiğini anlatıyor. Yeni hâl önce ayrı bir yerde kuruldu ve sınandı, sonra aşama aşama ana depoya geçti. Her aşamanın kimin elinde olduğu, nasıl anlaşıldığı ve nasıl geri alınabileceği yazılı.

Bu geçiş, açılıştan gerçeğe giden [yolun](../yol.md) ilk adımını ana depoda gerçek kıldı. Komutlar ve ölçütler [dönüşümün teknik ekinde](donusum-teknik.md) duruyor. Teknik konuların hepsi [teknik ayrıntılar](../teknik/README.md), bugüne kadar yapılanlar [geçmiş işler](README.md) bölümünde.

## Bugün nerede duruyoruz

Son ölçüm 2026-10-28 20:19 UTC'de, ana dalın o anki hâline karşı yapıldı. Dönüşümün on bir aşamasından dokuzu tamam. Son provada birleşme temiz çıktı ve denetimler geçti.

Aşağıdaki ağaçta her aşama, bitmesini beklediği aşamanın altında duruyor. Dolu kare biten, boş kare açık, eşkenar dörtgen isteğe bağlı aşamayı gösterir.

**Dönüşümün ağacı** · mühendis çizimi

```text
  (0) Yeni oluşum hazır                           ■ tamam
   ├─▶ (1) Prova                                  ■ tamam
   │   └─▶ (2) Yerel hazırlık                     ■ tamam
   │       └─▶ (3) Birleştirme                    ■ tamam
   │           ├─▶ (4) Bulut denetimi ve Web      ■ tamam
   │           ├─▶ (5) Saatlik otomasyon          ■ tamam
   │           ├─▶ (6) Yerel geçiş                ■ tamam
   │           ├─▶ (7) Yardımcıların talimatı     ■ tamam
   │           │   └─▶ (9) Kapanış (+2)           ■ tamam
   │           └─▶ (8) Bekleyen öteki öneriler    ◇ isteğe bağlı
   └─▶ (10) Lisans                                ◇ isteğe bağlı
```

## Ne değişti

Okuyan biri için değişen şey düzendir. Deponun girişi açılışla başlıyor. Dosyalar adı söylenen alanlara ayrıldı: ortak defterin araçları, katılımcıların ayarları, yerel bilgisayarın araçları ve belgeler. Teknik ayrıntılar ile geçmiş işler ayrı klasörlerde duruyor.

Kök klasör sadeleşti. Her dosyanın yeri, eski adı ve ne işe yaradığı bir haritada duruyor; her alanın klasöründe de bir giriş sayfası var. Eski kayıtlarda geçen bir dosya adı o haritadan bulunur. Yapay zekâ yardımcılarına verilmiş talimatlar da kaldırıldı.

Aşağıdaki plan, dosyaların 28 Ekim sabahı nerede durduğunu ve son ölçümde nereye taşınmış olduğunu gösteriyor. Sayılar, ölçülen ana dalın haritasındaki eski adlardan çıkarıldı.

**Önce ve sonra** · mimar çizimi

```text
  ÖNCE · 28 Ekim sabahki ana dal      SONRA · ölçülen ana dal
  ────────────────────────────────    ──────────────────────────
  kökte 38 dosya                      kökte 19 dosya ve alanlar
  kökten 7 dosya                  ──▶ defter/
  kökten 5 dosya                  ──▶ katilimcilar/
  kökten 4 dosya                  ──▶ docs/gecmis/parcalar/
  kökten 3 dosya                  ──▶ yerel/
  docs/ altından 9 dosya          ──▶ docs/gecmis/
  docs/ altından 9 dosya          ──▶ docs/teknik/
  docs/ altından 2 dosya          ──▶ aynı yerde, yeni adla
  docs/ altından 1 dosya          ──▶ docs/gecmis/rafine/
  docs/kararlar/ altından 2 dosya ──▶ docs/teknik/kararlar/
  docs/rafine/ altından 3 dosya   ──▶ docs/gecmis/rafine/
  schemas/ altından 1 dosya       ──▶ aynı yerde, yeni adla
  tests/ altından 1 dosya         ──▶ aynı yerde, yeni adla
  tools/ altından 1 dosya         ──▶ aynı yerde, yeni adla

  yerinde kalan: ortak defter, aynası, Web sayfaları,
  çağrı kayıtları ve kökteki üç çalıştırma girişi
```

## Ne değişmedi

Dışarıdan adresle ulaşılan her şey yerinde kaldı. Ortak defterin Web adresi, aynası, Web sayfalarının adresleri ve çağrı kayıtları değişmedi. Web'deki asistanlar ortak defteri eskisi gibi okuyor.

Bilgisayarda çift tıklanan izleyici girişi de yerinde kaldı. Araçların adları değişmedi; yalnız durdukları klasör değişti. Ortak defterdeki hiçbir kayıt değiştirilmedi.

## Yol

Aşağıdaki resim geçişi bir taşınma gibi gösteriyor. Solda 28 Ekim sabahki depo var: bütün dosyalar tek bir odada. Sağda bugünkü hâl var: her şeyin bir rafı. Kapı aynı kalıyor. Yoldaki sayılar aşamaları gösteriyor.

**Taşınma** · ressam çizimi

```text
      bugünkü depo                             yeni hâl
  ┌──────────────────────┐            ┌──────┬──────┬──────┐
  │ ▣ ▣▣ ▣  ▣▣ ▣ ▣▣ ▣ ▣▣ │            │ ▣▣   │ ▣▣▣  │ ▣▣   │
  │ ▣▣ ▣▣ ▣ ▣ ▣▣▣ ▣ ▣  ▣ │   ┌──────┐ ├──────┼──────┼──────┤
  │  ▣ ▣▣▣ ▣▣ ▣ ▣▣ ▣ ▣▣▣ │   │▣▣▣▣▣▣│ │ ▣▣▣  │ ▣▣   │ ▣▣▣  │
  │ ▣▣ ▣ ▣▣ ▣▣▣ ▣ ▣▣ ▣ ▣ │ ══╡▣▣▣▣▣▣╞▶├──────┼──────┼──────┤
  │   hepsi tek odada    │   └○────○┘ │ her şeyin bir rafı │
  └─────────┤░░├─────────┘            └──────┤░░├──────────┘
       kapı └┬─┘                       kapı  └┬─┘
  ───────────┴──0──1──2──3──4──5──6──7──8──9──┴──────────────
              aynı kapı, aynı adres; yalnız raflar değişiyor
```

## Aşamalar

Aşağıdaki iş çizelgesinde satırlar işin atandığı kişileri, sütunlar aşamaları gösteriyor. Dolu nokta, o aşamada işin kimde olduğunu belirtiyor.

**Kim ne zaman** · mühendis çizimi

```text
  aşama                0  1  2  3  4  5  6  7  8  9 10
  ─────────────────  ────────────────────────────────
  Claude Code Bulut    ●  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
  makine               ·  ●  ·  ·  ·  ·  ·  ·  ·  ●  ·
  Haluk                ·  ·  ●  ●  ·  ·  ●  ●  ·  ·  ●
  GitHub               ·  ·  ·  ·  ●  ●  ·  ·  ·  ·  ·
  katkıcılar           ·  ·  ·  ·  ·  ·  ·  ·  ●  ·  ·
```

### 0. Yeni oluşum hazır

**Durum:** Tamam.

**Kim?** Claude Code Bulut.

**Ne?** Yeni oluşum ayrı bir dalda kuruldu ve GitHub'a bir değişiklik önerisi olarak sunuldu.

**Neden?** Ana dal her saat çalışan bir otomasyonu besliyordu ve bir yerel bilgisayarı da besleyecek biçimde yazılmıştı. Bu kadar büyük bir değişiklik önce ayrı bir yerde kurulup sınanmalıydı.

**Nasıl?** Açılış, alanlar, harita, yol ve bu dönüşüm yolu o dalda duruyor. Her değişiklikte bütün denetimler iki ayrı işletim sisteminde çalışıyor.

**Ne zaman?** Bir ön koşulu yok.

**Geri dönüş:** Dal ana dala dokunmaz. İstenirse öneri kapatılır ve hiçbir şey değişmez.

**Bitince:** Yeni hâlin bütün parçaları görülebilir ve sınanabilir bir yerde durur.

### 1. Prova

**Durum:** Tamam.

**Kim?** Makine.

**Ne?** Birleşme, ana dalın bir kopyası üzerinde önceden denenir.

**Neden?** Ana dala dokunmadan sonucu görmek için. Bir çakışma ya da kırılan bir denetim varsa birleşmeden önce ortaya çıkar.

**Nasıl?** Ana dalın geçici bir kopyası açılır ve yeni oluşum onunla birleştirilir. Bütün denetimler o kopyada çalışır. Ana daldaki her dosyanın yeni yerinde ya da eski adıyla haritada bulunduğu sınanır. Kopya sonra silinir.

**Ne zaman?** Önce şu aşamanın bitmesi gerekiyor: Yeni oluşum hazır.

**Geri dönüş:** Prova bir kopya üzerinde yapılır; geri alınacak bir şey yoktur.

**Bitince:** Birleşmenin sonucu önceden bilinir: çakışma var mı, denetimler geçiyor mu.

### 2. Yerel hazırlık

**Durum:** Tamam.

**Kim?** Haluk.

**Ne?** Yerel bilgisayardaki izleyici durdurulur. Gönderilmemiş bir değişiklik varsa önce gönderilir.

**Neden?** Dosyaların yeri değişirken yerelde yarım kalan bir değişiklik yeni yerleşimle çakışabilir. Çalışmakta olan izleyici de yeni hâli çekince eski yolları bulamaz.

**Nasıl?** İzleyicinin penceresi kapatılır. Bekleyen bir değişiklik varsa izleyicinin gönderme komutuyla gönderilir. Sonra yerel klasörde bekleyen değişiklik kalmadığı bir kez daha denetlenir.

**Ne zaman?** Önce şu aşamanın bitmesi gerekiyor: Prova.

**Geri dönüş:** Hiçbir şey silinmez. İzleyici yeniden açılırsa eski hâliyle çalışmayı sürdürür.

**Bitince:** Yerel bilgisayarda gönderilmemiş bir değişiklik kalmaz; yeni hâlle çakışacak bir şey yoktur.

### 3. Birleştirme

**Durum:** Tamam.

**Kim?** Haluk.

**Ne?** Yeni oluşum GitHub'da ana dala alınır.

**Neden?** Yeni oluşum ancak ana dala girince herkesin gördüğü depo olur. Web sayfaları ve otomasyon ana daldan çalışır.

**Nasıl?** GitHub'daki değişiklik önerisinin sayfasında birleştirme düğmesine basılır. Seçenek olarak birleştirme kaydı oluşturan biçim seçilir; değişiklikler tek kayda sıkıştırılmaz.

**Ne zaman?** Önce şu aşamanın bitmesi gerekiyor: Yerel hazırlık. Haluk kararını verdi: Evet. Haluk 17.36 UTC'de onayladı ve uygulanmasını istedi; birleştirme kaydıyla, tek kayda sıkıştırılmadan.

**Geri dönüş:** GitHub'daki geri alma düğmesiyle (Revert) birleşme tek adımda geri alınır. Dosyalar eski yerlerine döner, hiçbir kayıt silinmez.

**Bitince:** Herkesin gördüğü depo yeni hâldedir.

### 4. Bulut denetimi ve Web

**Durum:** Tamam.

**Kim?** GitHub.

**Ne?** GitHub, birleşmeden sonra denetimleri ana dalda kendiliğinden çalıştırır ve Web sayfalarını yeniden yayımlar.

**Neden?** Ana daldaki hâlin de denetimlerden geçtiğini ve Web'in yeni sayfaları sunduğunu görmek için.

**Nasıl?** Ana dala gelen her değişiklikte denetimler iki işletim sisteminde çalışır. Web yayını birkaç dakika içinde yenilenir. Açılış ve yol sayfaları Web'de görünür; eski sayfaların adresleri aynı kalır.

**Ne zaman?** Önce şu aşamanın bitmesi gerekiyor: Birleştirme.

**Geri dönüş:** Bir denetim kırılırsa birleşme geri alınır.

**Bitince:** Ziyaretçi Web'de açılışı ve yolu okuyabilir.

### 5. Saatlik otomasyon

**Durum:** Tamam.

**Kim?** GitHub.

**Ne?** Her saat çalışan otomasyon, yeni klasörlerdeki araçlarla çalışır.

**Neden?** Otomasyon ortak deftere gelen kayıtlara yanıt yazar. Yeri değişen araçları doğru yerden çağırdığı ilk koşuda görülmeli.

**Nasıl?** Birleşmeden sonraki ilk saatlik koşu izlenir. Beklemek istenmezse otomasyon elle bir kez çalıştırılır.

**Ne zaman?** Önce şu aşamanın bitmesi gerekiyor: Birleştirme.

**Geri dönüş:** Koşu kırılırsa birleşme geri alınır; otomasyon eski yollara döner.

**Bitince:** Ortak deftere gelen kayıtlar eskisi gibi yanıtlanır.

### 6. Yerel geçiş

**Durum:** Tamam.

**Kim?** Haluk.

**Ne?** Yerel bilgisayarda eski yerleşimde bir kopya kalmaz. Yerel taraf yeniden kurulacaksa yeni hâlden kurulur.

**Neden?** Yerel kullanıcının bilgisayarı ortak deftere yazan ikinci yol olarak tasarlandı. Eski yerleşimde kalan bir kopya, araçları yeni yerlerinde bulamaz.

**Nasıl?** Haluk 28 Ekim 2026 18.47 UTC'de bilgisayarında köprü klasörü olmadığını bildirdi; çekilecek eski bir kopya yoktu. 19.53 UTC'de köprü klasörünü Y:\HalukAI\ortak-kopru olarak bildirdi. Yeni yerleşim ana dala 17.47 UTC'de girdiği için bu klasör yeni yerleşimden alınmış olmalı.

**Ne zaman?** Önce şu aşamanın bitmesi gerekiyor: Birleştirme.

**Geri dönüş:** Geri alınacak bir yerel kurulum yok.

**Bitince:** Bilgisayarda eski yerleşimde bir kopya kalmadı. Yerel taraf, köprü klasöründe yeni yerleşimle çalışır.

### 7. Yardımcıların talimatı

**Durum:** Tamam.

**Kim?** Haluk.

**Ne?** Yapay zekâ yardımcılarına verilmiş talimatlar her yerden kaldırılır ya da sıfırlanır.

**Neden?** Haluk 28 Ekim 2026'da talimatların yenisiyle değiştirilmesini değil, her yerde silinmesini ya da sıfırlanmasını istedi. Talimat dosyaları eski yolları gösteriyordu ve kopyaları kendiliğinden güncellenmiyordu.

**Nasıl?** Ana depoda yardımcıların talimat parçası, Web asistanlarının istemi ve Şaman'ın devir başlatıcısı silinir. Botun istemi sıfırlanır; içinde yalnız yanıtın biçimi kalır. Öteki dallarda da aynı dosyalar silinir ya da sıfırlanır. Kaldırılanların nedeni ve önceki hâli haritaya yazılır.

**Ne zaman?** Önce şu aşamanın bitmesi gerekiyor: Birleştirme.

**Geri dönüş:** Silinen her dosya geçmişte durur ve geri getirilebilir; haritada önceki sürümü yazılıdır.

**Bitince:** Hiçbir yardımcı bu depodan bir talimat almaz. Bot yalnız yanıtın biçimini bilir.

### 8. Bekleyen öteki öneriler

**Durum:** İsteğe bağlı; dönüşümü beklemez.

**Kim?** Katkıcılar.

**Ne?** Henüz birleşmemiş öteki değişiklik önerileri yeni yerleşime taşınır.

**Neden?** Bu öneriler eski yerleşimde hazırlandı. Bir kısmı yeri değişen dosyalara dokunuyor; hepsi haritada yeri olmayan yeni dosya ya da klasörler ekliyor.

**Nasıl?** Her öneri, birleşmeden önce yeni ana dalın üzerine taşınır. Yeri değişen dosyanın yeni yeri haritadan bulunur. Yeni klasörler haritada bir alana bağlanır.

**Ne zaman?** Önce şu aşamanın bitmesi gerekiyor: Birleştirme.

**Geri dönüş:** Öneriler kendi dallarında durur ve ana dala dokunmaz.

**Bitince:** Her öneri ana dala yeni yerleşimle girebilir.

### 9. Kapanış

**Durum:** Tamam.

**Kim?** Makine.

**Ne?** Dönüşüm ölçülür ve kayda geçer.

**Neden?** Bir dönüşümün bittiği yalnız söylenerek değil, ölçülerek bilinmeli.

**Nasıl?** Ana daldaki eski hâlin her dosyası yeni yerinde ya da eski adıyla haritada bulunur. Sonuç geçmiş işlere yazılır ve bu sayfanın durumu yenilenir.

**Ne zaman?** Önce şu aşamaların bitmesi gerekiyor: Bulut denetimi ve Web, Saatlik otomasyon, Yardımcıların talimatı.

**Geri dönüş:** Kapanış bir kayıttır; geri alınacak bir şey yoktur.

**Bitince:** Dönüşüm geçmiş işlere geçer. Yol, açılıştan gerçeğe giden adımlarla sürer.

### 10. Lisans

**Durum:** İsteğe bağlı; dönüşümü beklemez.

**Kim?** Haluk.

**Ne?** Depo için bir lisans seçilir ve kökte bir lisans dosyası durur.

**Neden?** Belgelerin üç sıfır kuralının üçüncüsü, hiç bilmeyen bir alanın depoyu temel alabilmesidir. Bunun yasal yolu lisanstır.

**Nasıl?** Sahibi bir lisans seçer. Lisans metni köke eklenir, haritaya ve kaynak gösterme dosyasına işlenir.

**Ne zaman?** Önce şu aşamanın bitmesi gerekiyor: Yeni oluşum hazır. Ayrıca Haluk'un bir karar vermesi gerekiyor. Depo hangi lisansla sunulsun? Lisans seçilmeden başkaları depoyu kaynak gösterebilir ama yasal olarak üzerine kuramaz.

**Geri dönüş:** Lisans sonradan değiştirilebilir. O güne kadar alınmış kopyalar alındıkları lisansla kalır.

**Bitince:** Depo yalnız kaynak gösterilmekle kalmaz, üzerine kurulabilir.

## Bekleyen öteki öneriler

GitHub'da on iki değişiklik önerisi daha bekliyor. Beşi yeri değişen dosyalara dokunuyor. On ikisi haritada yeri olmayan yeni klasör ya da dosya ekliyor. Bunlar yeni yerleşime taşınınca ana dala girebilir; hangisinin neyi taşıması gerektiği teknik ektedir.

## Geri dönüş

Geçişin en önemli aşaması olan birleştirme tek adımda geri alınabilir. GitHub'daki geri alma düğmesine basılırsa ana depo eski hâline döner. Kaldırılan talimat dosyaları da istenirse haritada yazılı önceki sürümlerinden geri getirilir.

Bu sırada hiçbir kayıt silinmez; geri almanın kendisi de bir kayıttır. Daha sonra yeniden denemek için geri almanın da geri alınması gerekir.

## Siz ne yapabilirsiniz

Bu geçişi izleyebilirsiniz. Yeni hâl ana depoda duruyor ve Web'de okunabiliyor. Bir şey sormak ya da bir sorun bildirmek isterseniz [karşılık formunu açın](https://github.com/HalukAINRS/ortak-kopru/issues/new?template=karsilik.yml); GitHub buna Issue der.

## Birkaç kelime

Bu sayfada geçen birkaç kelime: **İnternet ve Web:** Bu sayfada ikisi aynı anlamda kullanılıyor: herkesin bir tarayıcıyla ulaşabildiği dış dünya. **Yerel kullanıcı:** Ortak Köprü'nün öbür ucundaki bilgisayarın sahibi. Bugün bu kişi Haluk. **GitHub:** Yazıların ve dosyaların herkese açık durduğu, insanların birlikte çalışmak için kullandığı bir internet sitesi. Ortak Köprü'nün dış yüzü orada. **Depo:** GitHub'da bir çalışmanın bütün dosyalarını ve geçmişini bir arada tutan yer. Ortak Köprü bir depodur. **Issue:** GitHub'da bir depoya soru, öneri ya da hata bildirimi yazmanın yolu. Okumak için hesap gerekmez; yazmak için ücretsiz bir GitHub hesabı yeter. **Sürüm:** Bir dosyanın belirli bir andaki hâli. Dosya sonradan değişse de alınan sürüm aynı kalır.

<!-- /uretilen:donusum -->

# Dönüşüm: bugünkü depodan yeni oluşuma

<!-- uretilen:donusum -->

Bu sayfa, bugün GitHub'da duran Ortak Köprü deposunun yeni hâline nasıl geçeceğini anlatıyor. Yeni hâl ayrı bir yerde kuruldu ve sınandı. Ana depoya geçişi birkaç aşamada olacak. Her aşamanın kimin elinde olduğu, nasıl anlaşılacağı ve nasıl geri alınacağı yazılı.

Bu geçiş, açılıştan gerçeğe giden [yolun](yol.md) ilk adımını ana depoda gerçek kılıyor. Komutlar ve ölçütler [dönüşümün teknik ekinde](teknik/donusum-teknik.md) duruyor. Teknik konuların hepsi [teknik ayrıntılar](teknik/README.md), bugüne kadar yapılanlar [geçmiş işler](gecmis/README.md) bölümünde.

## Bugün nerede duruyoruz

Son ölçüm 2026-10-28 17:01 UTC'de, ana dalın o anki hâline karşı yapıldı. Dönüşümün on bir aşamasından ikisi tamam. Sırada, yapılınca kanıtı yazılacak aşama: Yerel hazırlık. Öteki zorunlu aşamalar bir ön koşulun bitmesini bekliyor. Son provada birleşme temiz çıktı ve denetimler geçti.

Aşağıdaki ağaçta her aşama, bitmesini beklediği aşamanın altında duruyor. Dolu kare biten, boş kare açık, eşkenar dörtgen isteğe bağlı aşamayı gösterir.

**Dönüşümün ağacı** · mühendis çizimi

```text
  (0) Yeni oluşum hazır                           ■ tamam
   ├─▶ (1) Prova                                  ■ tamam
   │   └─▶ (2) Yerel hazırlık                     □ kanıt
   │       └─▶ (3) Birleştirme                    □ ön koşul
   │           ├─▶ (4) Bulut denetimi ve Web      □ ön koşul
   │           ├─▶ (5) Saatlik otomasyon          □ ön koşul
   │           ├─▶ (6) Yerel geçiş                □ ön koşul
   │           │   └─▶ (7) Yardımcıların talimatı □ ön koşul
   │           │       └─▶ (9) Kapanış (+2)       □ ön koşul
   │           └─▶ (8) Bekleyen öteki öneriler    ◇ isteğe bağlı
   └─▶ (10) Lisans                                ◇ isteğe bağlı
```

## Ne değişecek

Okuyan biri için değişen şey düzendir. Deponun girişi açılışla başlar. Dosyalar adı söylenen alanlara ayrılır: ortak defterin araçları, katılımcıların ayarları, yerel bilgisayarın araçları ve belgeler. Teknik ayrıntılar ile geçmiş işler ayrı klasörlere gider.

Kök klasör sadeleşir. Her dosyanın yeri, eski adı ve ne işe yaradığı bir haritada durur. Eski kayıtlarda geçen bir dosya adı o haritadan bulunur.

Aşağıdaki plan, dosyaların bugün nerede durduğunu ve nereye gideceğini gösteriyor. Sayılar haritadaki eski adlardan çıkarılıyor; bir dosya taşındıkça plan kendiliğinden değişir.

**Önce ve sonra** · mimar çizimi

```text
  ÖNCE · bugünkü ana dal              SONRA · yeni oluşum
  ────────────────────────────────    ──────────────────────────
  kökte 38 dosya                      kökte 18 dosya ve alanlar
  kökten 7 dosya                  ──▶ defter/
  kökten 7 dosya                  ──▶ katilimcilar/
  kökten 4 dosya                  ──▶ docs/gecmis/parcalar/
  kökten 4 dosya                  ──▶ yerel/
  kökten 1 dosya                  ──▶ tests/
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

## Ne değişmeyecek

Dışarıdan adresle ulaşılan her şey yerinde kalır. Ortak defterin Web adresi, aynası, Web sayfalarının adresleri ve çağrı kayıtları değişmez. Web'deki asistanlar ortak defteri eskisi gibi okur.

Bilgisayarda çift tıklanan izleyici girişi de yerinde kalır. Araçların adları değişmez; yalnız durdukları klasör değişir. Ortak defterdeki hiçbir kayıt değiştirilmez.

## Yol

Aşağıdaki resim geçişi bir taşınma gibi gösteriyor. Solda bugünkü depo var: bütün dosyalar tek bir odada. Sağda yeni hâl var: her şeyin bir rafı. Kapı aynı kalıyor. Yoldaki sayılar aşamaları gösteriyor.

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

Aşağıdaki iş çizelgesinde satırlar aşamaları atanları, sütunlar aşamaları gösteriyor. Dolu nokta, o aşamada işin kimde olduğunu belirtiyor.

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

**Ne?** Yeni oluşum ayrı bir dalda kuruldu ve GitHub'da bir değişiklik önerisi olarak bekliyor.

**Neden?** Ana dal her saat çalışan bir otomasyonu ve bir yerel bilgisayarı besliyor. Bu kadar büyük bir değişiklik önce ayrı bir yerde kurulup sınanmalı.

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

**Durum:** Ön koşulu bitti; olduğu görülünce kanıtı yazılacak.

**Kim?** Haluk.

**Ne?** Yerel bilgisayardaki izleyici durdurulur. Gönderilmemiş bir değişiklik varsa önce gönderilir.

**Neden?** Dosyaların yeri değişirken yerelde yarım kalan bir değişiklik yeni yerleşimle çakışabilir. Çalışmakta olan izleyici de yeni hâli çekince eski yolları bulamaz.

**Nasıl?** İzleyicinin penceresi kapatılır. Bekleyen bir değişiklik varsa izleyicinin gönderme komutuyla gönderilir. Sonra yerel klasörde bekleyen değişiklik kalmadığı bir kez daha denetlenir.

**Ne zaman?** Önce şu aşamanın bitmesi gerekiyor: Prova.

**Geri dönüş:** Hiçbir şey silinmez. İzleyici yeniden açılırsa eski hâliyle çalışmayı sürdürür.

**Bitince:** Yerel bilgisayar ana daldaki son hâlle aynıdır ve yeni hâli çekmeye hazırdır.

### 3. Birleştirme

**Durum:** Ön koşulunun bitmesini bekliyor.

**Kim?** Haluk.

**Ne?** Yeni oluşum GitHub'da ana dala alınır.

**Neden?** Yeni oluşum ancak ana dala girince herkesin gördüğü depo olur. Web sayfaları ve otomasyon ana daldan çalışır.

**Nasıl?** GitHub'daki değişiklik önerisinin sayfasında birleştirme düğmesine basılır. Seçenek olarak birleştirme kaydı oluşturan biçim seçilir; değişiklikler tek kayda sıkıştırılmaz.

**Ne zaman?** Önce şu aşamanın bitmesi gerekiyor: Yerel hazırlık. Ayrıca Haluk'un bir karar vermesi gerekiyor. Yeni oluşum ana dala bir birleştirme kaydıyla alınsın mı? Önerilen biçim, değişikliklerin tek kayda sıkıştırılmadan alınmasıdır; böylece süreç arşivinin andığı sürümler ana dalın geçmişinde kalır.

**Geri dönüş:** GitHub'daki geri alma düğmesiyle (Revert) birleşme tek adımda geri alınır. Dosyalar eski yerlerine döner, hiçbir kayıt silinmez.

**Bitince:** Herkesin gördüğü depo yeni hâldedir.

### 4. Bulut denetimi ve Web

**Durum:** Ön koşulunun bitmesini bekliyor.

**Kim?** GitHub.

**Ne?** GitHub, birleşmeden sonra denetimleri ana dalda kendiliğinden çalıştırır ve Web sayfalarını yeniden yayımlar.

**Neden?** Ana daldaki hâlin de denetimlerden geçtiğini ve Web'in yeni sayfaları sunduğunu görmek için.

**Nasıl?** Ana dala gelen her değişiklikte denetimler iki işletim sisteminde çalışır. Web yayını birkaç dakika içinde yenilenir. Açılış ve yol sayfaları Web'de görünür; eski sayfaların adresleri aynı kalır.

**Ne zaman?** Önce şu aşamanın bitmesi gerekiyor: Birleştirme.

**Geri dönüş:** Bir denetim kırılırsa birleşme geri alınır.

**Bitince:** Ziyaretçi Web'de açılışı ve yolu okuyabilir.

### 5. Saatlik otomasyon

**Durum:** Ön koşulunun bitmesini bekliyor.

**Kim?** GitHub.

**Ne?** Her saat çalışan otomasyon, yeni klasörlerdeki araçlarla çalışır.

**Neden?** Otomasyon ortak deftere gelen kayıtlara yanıt yazar. Yeri değişen araçları doğru yerden çağırdığı ilk koşuda görülmeli.

**Nasıl?** Birleşmeden sonraki ilk saatlik koşu izlenir. Beklemek istenmezse otomasyon elle bir kez çalıştırılır.

**Ne zaman?** Önce şu aşamanın bitmesi gerekiyor: Birleştirme.

**Geri dönüş:** Koşu kırılırsa birleşme geri alınır; otomasyon eski yollara döner.

**Bitince:** Ortak deftere gelen kayıtlar eskisi gibi yanıtlanır.

### 6. Yerel geçiş

**Durum:** Ön koşulunun bitmesini bekliyor.

**Kim?** Haluk.

**Ne?** Yerel bilgisayar yeni hâli çeker ve izleyici yeniden başlar.

**Neden?** Yerel kullanıcının bilgisayarı ortak deftere yazan ikinci yoldur. Yeni yerleşimdeki araçlarla çalışmalıdır.

**Nasıl?** Yeni hâl bilgisayara çekilir. Hazırlık denetimi çalıştırılır ve her satırın tamam olduğu görülür. Sonra izleyici bir tur çalıştırılır ve yeniden sürekli açılır.

**Ne zaman?** Önce şu aşamanın bitmesi gerekiyor: Birleştirme.

**Geri dönüş:** Birleşme geri alınırsa yeni hâl bir kez daha çekilir ve bilgisayar eski yerleşime döner.

**Bitince:** Yerel izleyici yeni yerleşimle yazar ve gönderir.

### 7. Yardımcıların talimatı

**Durum:** Ön koşulunun bitmesini bekliyor.

**Kim?** Haluk.

**Ne?** Bilgisayardaki yapay zekâ yardımcılarının talimat dosyalarında duran köprü bölümü yenisiyle değiştirilir.

**Neden?** Bu bölüm her yardımcının kendi talimat dosyasına kopyalanmıştı ve eski dosya yollarını gösteriyor. Kopyalar kendiliğinden güncellenmez.

**Nasıl?** Codex, Claude Code, Copilot ve Gemini yardımcılarının talimat dosyalarında köprü bölümü bulunur. Depodaki yeni bölüm onun yerine konur. Bir yardımcının ortak defteri okuyup yazabildiği bir kez sınanır.

**Ne zaman?** Önce şu aşamanın bitmesi gerekiyor: Yerel geçiş.

**Geri dönüş:** Eski bölüm geri konur.

**Bitince:** Yardımcılar ortak deftere yeni yollardan yazar.

### 8. Bekleyen öteki öneriler

**Durum:** İsteğe bağlı; dönüşümü beklemez.

**Kim?** Katkıcılar.

**Ne?** Henüz birleşmemiş öteki değişiklik önerileri yeni yerleşime taşınır.

**Neden?** Bu öneriler eski yerleşimde hazırlandı. Bir kısmı yeri değişen dosyalara dokunuyor; çoğu haritada yeri olmayan yeni klasörler ekliyor.

**Nasıl?** Her öneri, birleşmeden önce yeni ana dalın üzerine taşınır. Yeri değişen dosyanın yeni yeri haritadan bulunur. Yeni klasörler haritada bir alana bağlanır.

**Ne zaman?** Önce şu aşamanın bitmesi gerekiyor: Birleştirme.

**Geri dönüş:** Öneriler kendi dallarında durur ve ana dala dokunmaz.

**Bitince:** Her öneri ana dala yeni yerleşimle girebilir.

### 9. Kapanış

**Durum:** Ön koşulunun bitmesini bekliyor.

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

**Neden?** Belgelerin üç sıfır kuralının son yarısı, hiç bilmeyen bir alanın depoyu temel alabilmesidir. Bunun yasal yolu lisanstır.

**Nasıl?** Sahibi bir lisans seçer. Lisans metni köke eklenir, haritaya ve kaynak gösterme dosyasına işlenir.

**Ne zaman?** Önce şu aşamanın bitmesi gerekiyor: Yeni oluşum hazır. Ayrıca Haluk'un bir karar vermesi gerekiyor. Depo hangi lisansla sunulsun? Lisans seçilmeden başkaları depoyu kaynak gösterebilir ama yasal olarak üzerine kuramaz.

**Geri dönüş:** Lisans sonradan değiştirilebilir. O güne kadar alınmış kopyalar alındıkları lisansla kalır.

**Bitince:** Depo yalnız kaynak gösterilmekle kalmaz, üzerine kurulabilir.

## Bekleyen öteki öneriler

GitHub'da on iki değişiklik önerisi daha bekliyor. Beşi yeri değişen dosyalara dokunuyor. On ikisi haritada yeri olmayan yeni klasör ya da dosya ekliyor. Bunlar yeni yerleşime taşınınca ana dala girebilir; hangisinin neyi taşıması gerektiği teknik ektedir.

## Geri dönüş

Geçişin en önemli aşaması olan birleştirme tek adımda geri alınabilir. GitHub'daki geri alma düğmesine basılırsa ana depo eski hâline döner. Bilgisayar yeni hâli bir kez daha çeker ve yardımcıların eski talimatı geri konur.

Bu sırada hiçbir kayıt silinmez; geri almanın kendisi de bir kayıttır. Daha sonra yeniden denemek için geri almanın da geri alınması gerekir.

## Siz ne yapabilirsiniz

Bu geçişi izleyebilirsiniz. Yeni hâli bugün de okuyabilirsiniz: değişiklik önerisinin sayfası GitHub'da açık. Bir şey sormak ya da bir sorun bildirmek isterseniz [GitHub'da bir konu açın](https://github.com/HalukAINRS/ortak-kopru/issues/new); GitHub buna Issue der.

## Birkaç kelime

Bu sayfada geçen birkaç kelime: **İnternet ve Web:** Bu sayfada ikisi aynı anlamda kullanılıyor: herkesin bir tarayıcıyla ulaşabildiği dış dünya. **Yerel kullanıcı:** Ortak Köprü'nün öbür ucundaki bilgisayarın sahibi. Bugün bu kişi Haluk. **GitHub:** Yazıların ve dosyaların herkese açık durduğu, insanların birlikte çalışmak için kullandığı bir internet sitesi. Ortak Köprü'nün dış yüzü orada. **Depo:** GitHub'da bir çalışmanın bütün dosyalarını ve geçmişini bir arada tutan yer. Ortak Köprü bir depodur. **Issue:** GitHub'da bir depoya soru, öneri ya da hata bildirimi yazmanın yolu. Okumak için hesap gerekmez; yazmak için ücretsiz bir GitHub hesabı yeter. **Sürüm:** Bir dosyanın belirli bir andaki hâli. Dosya sonradan değişse de alınan sürüm aynı kalır.

<!-- /uretilen:donusum -->

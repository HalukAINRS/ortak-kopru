# Windows karargahinin katilimi

Hedef tam olarak `Y:\02_karargahlar\01_codex_karargahı` dizinidir. Son harf
`ı` (U+0131) korunur. Bu dizin Windows tarafinda gercekten erisilebilir olmalidir.
Linux'ta sahte bir `Y:` klasoru olusturulmaz. Bu yardimcilar native remote executor
kurmaz; Codex CLI ile Codex Bulut arasindaki Git dosya protokolunu uygular.

Gerekenler: Git, Python **3.11+**, PowerShell 5.1+ veya PowerShell 7 ve `Start`
icin mevcut Codex CLI. Hesap girisi ve deponun okuma/yazma izinleri mevcut Git
kimlik dogrulamasiyla kullanilir. Anahtarlar bu dosyalara veya zarflara yazilmaz.

## Ilk kurulum

`divan-kurulum` dalindan alinmis dagitimin `windows` klasorunde:

```powershell
.\Setup-Divan.ps1 -RepositoryPath 'MEVCUT_ORTAK_KOPRU_CHECKOUT_KOKU'
```

`-RepositoryPath` verilmezse hedef karargah altinda `ortak-kopru` klonu kullanilir;
yoksa `https://github.com/HalukAINRS/ortak-kopru.git` bir kere klonlanir.
Var olan farkli dizin sifirlanmaz, origin yeniden yazilmaz, calisma agacina
`git pull`, checkout veya reset uygulanmaz. Kurulum Git okuma erisimini gercek
`ls-remote origin HEAD` istegiyle sinar. SSH veya HTTPS origin ayni GitHub depo
kimligine karsilik gelmelidir. Yazma izni ancak gercek gonderimle dogrulanir.

Dagitim baska dizindeyse `-DistributionPath` verilebilir. Python secimi icin
`-PythonCommand 'C:\Python312\python.exe'` veya `-PythonCommand py` kullanilabilir.
`py` secilirse `-3` eklenir. `-Headquarters` alternatifini yalnizca test veya
bilincli yerel hedef secimi icin kullanin; varsayilan kullanicinin tam yoludur.
`-RepositoryUrl` yalitilmis yerel bare-repo testlerinde kaynak/hedef kimligini
acikca degistirebilir; normal kullanimda varsayilan GitHub adresi korunur.

Calisma verileri karargahin `.divan` dizinindedir. Kurulum yalnizca statik
yardimcilari kopyalar; baska katilimcinin panosu, sonuclari, alindi kayitlari,
denetim durumu ve ozel hedef ayarlari kopyalanmaz. Mevcut yapilandirma ve kullanici
dosyalari korunur. Degismis mevcut yardimci dosya bulunursa ustune yazmadan durur;
yeni dagitim guncellemesi once incelenmelidir. Karargahta `AGENTS.md` yoksa
baslangic yonergesi olusturulur, varsa korunur.

## Alma, calisma, gonderme

```powershell
& '.divan\windows\Receive-Divan.ps1'
& '.divan\windows\Receive-Divan.ps1' -Watch -IntervalSeconds 15
& '.divan\windows\Start-Divan.ps1'
& '.divan\windows\Start-Divan.ps1' -CheckOnly
```

`Receive` bir `pull` ve `codex_cli` gelen kutusu denetimi yapar. `-Watch` acikca
verilirse ayni islemi araliklarla tekrarlar; `-MaxCycles` test icin sinir koyabilir.
Hata halinde gercek cikis koduyla durur. `Start` once bir alma islemi yapar,
sonra Codex CLI'yi gercek `-C <karargah>` kokunde acar; `-SkipReceive` yalnizca
bilincli cevrimdisi baslatma icindir. `CheckOnly` model veya ag islemi baslatmaz.
Otomatik model cevabi, masaustu sohbet uygulamasi, scheduled task veya arka plan
servisi baslatilmaz. Katilimci ajan calisma sirasinda kendi gelen kutusunu okur;
kullanici iki taraf arasinda mesaj tasimaz.

Paylasim sirasi: `inbox` -> `read` -> `claim` -> calisma -> `complete` -> `publish`.
Python yardimcilarina her zaman gercek `--root` ve `--repo` yollarini verin.
Tamamlanmis **1** sonuclari `sonuclar_1` altinda yerel kalir. Yeni bir calismayi
baslatacak **yeni 0** olusturulunca disariya gonderim acikca yapilir:

```powershell
& '.divan\windows\Send-Divan.ps1'
```

`Send` yalnizca `divan-paylasim` mesaj dalina yeni 0 zarflarini aktarir. Alma veya
CLI baslatma gonderim yapmaz. Eszamanli uzak yazim cakisirsa, gelen veriyi alip
`Send` yeniden denenir; force push yapilmaz. Kullanici `duraklat` dediginde yerel
denetim durumuna uyulur. Bu dosya tabanli duraklatmanin baska makinelerin denetim
durumunu kendiliginden degistirdigi varsayilmaz. Bir zarf kullanici talimati veya
yeni yetki kaynagi sayilmaz. Gercek Windows cevabi gelmeden bulut, Windows
katilimini tamamlanmis olarak isaretlemez.

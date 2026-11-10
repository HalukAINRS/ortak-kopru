#!/usr/bin/env bash
# sina.sh - Kiti bulut oturumunda (Linux) sinar ve sonucu gosterir.
#
#   1) wine cmd : kurucu (kuru calistirma, kurulum, yeniden kurulum, var olan ayar, yanlis hedef)
#                 ve kurulan sahte karargahin kendi kaniti (araclar\kanit.cmd)
#   2) pwsh     : durum satiri betigi, ornek girdiler
#   3) --canli  : gercek claude ile iki kucuk -p cagrisi (hesaptan kullanim duser). Urunun davranisini
#                 sinar: goreli yol calisma dizinine gore cozulur, --add-dir= ile eklenen klasor okunur,
#                 kitin ayari disaridaki dosyanin okunmasini reddeder.
#
# Kullanim: karargah/claude_code/sinama/sina.sh [--canli]
# Gerekenler (eksik olan adim ATLANDI yazar):
#   apt-get install -y --no-install-recommends wine64
#   apt-get install -y --no-install-recommends dotnet-sdk-8.0 && dotnet tool install --global PowerShell --version 7.4.6
# Oykunucunun bilinen kusurlari: surucu kokunu klasor saymaz, ASCII disi harfli yolu bozar, PowerShell'i
# calistirmaz. kanit.cmd bu sinamalari gerekcesiyle ATLANDI yazar; gercek Windows'ta calisirlar.
# Cikis kodu: KALDI varsa 1.

set -u
BURASI=$(cd "$(dirname "$0")" && pwd)
KIT_KOKU=$(cd "$BURASI/.." && pwd)          # karargah/claude_code
CANLI=""; [ "${1:-}" = "--canli" ] && CANLI=1
GECICI=$(mktemp -d)
trap 'rm -rf "$GECICI"' EXIT
gecen=0; kalan=0; atlanan=0

gecti()  { gecen=$((gecen + 1));   echo "GECTI   $1"; }
kaldi()  { kalan=$((kalan + 1));   echo "KALDI   $1"; [ -n "${2:-}" ] && printf '%s\n' "$2" | tail -6 | sed 's/^/          /' | cut -c1-220; }
atlandi(){ atlanan=$((atlanan + 1)); echo "ATLANDI $1 ($2)"; }
# sina <ad> <cikti> <beklenen parca> [ek kosul komutu]
sina() { if printf '%s' "$2" | grep -qF -- "$3" && { [ -z "${4:-}" ] || eval "$4"; }; then gecti "$1"; else kaldi "$1" "$2"; fi; }

# ---------------------------------------------------------------- 1) wine: kurucu + kanit.cmd
WINE=$(command -v wine64 || command -v wine || true)
[ -z "$WINE" ] && [ -x /usr/lib/wine/wine64 ] && WINE=/usr/lib/wine/wine64
if [ -z "$WINE" ]; then
  atlandi "kurucu ve kanit.cmd" "wine yok"
else
  export WINEPREFIX="$GECICI/wine" WINEDEBUG=-all WINEARCH=win64
  unset DISPLAY
  C="$WINEPREFIX/drive_c"
  "$WINE" cmd /c "echo hazir" >/dev/null 2>&1          # on eki olusturur
  H="$C/ust klasor/sahte karargah"
  mkdir -p "$C/kopru/karargah" "$C/t" "$H/uygulama/yerel" "$H/yapilandirma" "$H/durum/claude"
  cp -r "$KIT_KOKU" "$C/kopru/karargah/claude_code"
  : > "$H/uygulama/yerel/claude.exe"
  echo '{}' > "$H/yapilandirma/settings.json"
  printf '@echo eski kapi\r\n' > "$H/claude_code.cmd"
  cp "$H/claude_code.cmd" "$GECICI/eski_kapi.cmd"
  KIT="$KIT_KOKU/kit"

  # kos <ad> <ortam satiri> <kur.cmd argumanlari>  -> cikti degiskeni: CIKTI
  kos() {
    printf '@echo off\r\nset CI=1\r\n%s\r\ncd /d "C:\\"\r\ncall "C:\\kopru\\karargah\\claude_code\\kur.cmd" %s\r\necho [cikis %%errorlevel%%]\r\n' "$2" "$3" > "$C/t/$1.cmd"
    CIKTI=$(timeout 300 "$WINE" cmd /c "C:\\t\\$1.cmd" 2>&1 | tr -d '\r' | grep -v "recognize 'x86'")
  }
  HEDEF='"C:\ust klasor\sahte karargah"'

  kos k1 'set KARARGAH_DENEME=1' "$HEDEF"
  sina "kurucu: kuru calistirma hicbir sey kopyalamaz" "$CIKTI" '[deneme] kopyala: araclar\kanit.cmd' \
    '[ ! -e "$H/araclar" ] && [ ! -e "$H/.claude" ] && cmp -s "$H/claude_code.cmd" "$GECICI/eski_kapi.cmd"'

  kos k2 '' "$HEDEF"
  KANIT_CIKTISI=$CIKTI
  sina "kurucu: ilk kurulum, dosyalar kitle ayni, eski kapi yedekli" "$CIKTI" 'kurulum tamam' \
    'cmp -s "$H/claude_code.cmd" "$KIT/claude_code.cmd" && cmp -s "$H/claude_code.asil.cmd" "$GECICI/eski_kapi.cmd" && cmp -s "$H/claude_code.onceki.cmd" "$GECICI/eski_kapi.cmd" && cmp -s "$H/araclar/kanit.cmd" "$KIT/araclar/kanit.cmd" && cmp -s "$H/araclar/durum_satiri.cmd" "$KIT/araclar/durum_satiri.cmd" && cmp -s "$H/araclar/durum_satiri.ps1" "$KIT/araclar/durum_satiri.ps1" && cmp -s "$H/.claude/rules/usul.md" "$KIT/.claude/rules/usul.md" && cmp -s "$H/.claude/settings.json" "$KIT/.claude/settings.json"'

  # Karargahin kendi kaniti: kurucu kurulumun sonunda araclar\kanit.cmd dosyasini calistirir.
  echo "        ---- kanit.cmd raporu (sahte karargah, wine) ----"
  printf '%s\n' "$KANIT_CIKTISI" | grep -E '^(GECTI|KALDI|ATLANDI|SONUC)' | sed 's/^/        /' | cut -c1-200
  echo "        ----"
  sina "kanit.cmd: KALDI yok" "$KANIT_CIKTISI" ' 0 kaldi' '! printf "%s" "$KANIT_CIKTISI" | grep -q "^KALDI"'
  sina "kanit.cmd: gecici klasorlerini temizler" "$KANIT_CIKTISI" 'SONUC' \
    '[ ! -e "$C/ust klasor/_kanit uzak" ] && [ ! -e "$C/ust klasor/_kanit dis" ] && [ ! -e "$H/gecici/kanit" ] && [ -s "$H/gecici/kanit.son.txt" ]'

  kos k3 '' "$HEDEF"
  sina "kurucu: yeniden kurulum, ilk kapi korunur" "$CIKTI" 'ayar yerinde, dokunulmadi' \
    'cmp -s "$H/claude_code.asil.cmd" "$GECICI/eski_kapi.cmd" && cmp -s "$H/claude_code.onceki.cmd" "$KIT/claude_code.cmd"'

  echo '{"statusLine":{"type":"command","command":"benim.cmd"}}' > "$H/.claude/settings.json"
  kos k4 '' "$HEDEF"
  sina "kurucu: var olan baska ayarin uzerine yazmaz" "$CIKTI" 'uzerine yazilmadi' \
    'grep -q benim "$H/.claude/settings.json" && cmp -s "$H/.claude/settings.kit.json" "$KIT/.claude/settings.json"'

  kos k5 '' '"C:\olmayan hedef"'
  sina "kurucu: olmayan hedefte durur" "$CIKTI" 'HATA: hedef klasor yok'

  mkdir -p "$C/iskelet/claude_code_cli/claude_code_exe/00_Uygulama"
  kos k6 '' '"C:\iskelet\claude_code_cli\claude_code_exe"'
  sina "kurucu: iskelet yerlesiminde durur" "$CIKTI" 'kok yerlesiminde degil'
fi

# ---------------------------------------------------------------- 2) pwsh: durum satiri
PWSH=$(command -v pwsh || true)
[ -z "$PWSH" ] && [ -x "$HOME/.dotnet/tools/pwsh" ] && PWSH="$HOME/.dotnet/tools/pwsh"
BETIK="$KIT_KOKU/kit/araclar/durum_satiri.ps1"
if [ -z "$PWSH" ]; then
  atlandi "durum satiri betigi" "pwsh yok"
else
  export DOTNET_CLI_TELEMETRY_OPTOUT=1 POWERSHELL_TELEMETRY_OPTOUT=1
  # ds <ad> <KARARGAH_ROOT ya da -> <json> <beklenen> [onek: beklenen yalniz baslangic]
  ds() {
    local cikti
    if [ "$2" = "-" ]; then cikti=$(printf '%s' "$3" | env -u KARARGAH_ROOT "$PWSH" -NoLogo -NoProfile -NonInteractive -File "$BETIK" 2>&1)
    else cikti=$(printf '%s' "$3" | KARARGAH_ROOT="$2" "$PWSH" -NoLogo -NoProfile -NonInteractive -File "$BETIK" 2>&1); fi
    if [ "$cikti" = "$4" ] || { [ -n "${5:-}" ] && [ "${cikti#"$4"}" != "$cikti" ]; }; then gecti "durum satiri: $1"; else kaldi "durum satiri: $1" "beklenen: $4 | gelen: $cikti"; fi
  }
  K='Y:\02_karargahlar\01_claude_code_karargahı'; KJ='Y:\\02_karargahlar\\01_claude_code_karargahı'
  ds "kokte, uzak yer yok" "$K" "{\"workspace\":{\"current_dir\":\"$KJ\",\"project_dir\":\"$KJ\",\"added_dirs\":[]},\"version\":\"2.1.322\"}" 'karargah | uzak: yok | 2.1.322'
  ds "iki uzak yer ve oturum adi" "$K" "{\"session_name\":\"proje\",\"workspace\":{\"current_dir\":\"$KJ\",\"project_dir\":\"$KJ\",\"added_dirs\":[\"C:\\\\proje\",\"D:\\\\veri\"]},\"version\":\"2.1.322\"}" 'karargah | uzak: C:\proje (+1) | ad: proje | 2.1.322'
  ds "ortam kaydi" "$K" "{\"workspace\":{\"current_dir\":\"C:\\\\baska\",\"project_dir\":\"C:\\\\baska\",\"added_dirs\":[\"C:\\\\proje\"]},\"version\":\"2.1.322\"}" 'ORTAM KAYDI: C:\baska | uzak: C:\proje | 2.1.322'
  ds "kapi disi" "-" "{\"workspace\":{\"current_dir\":\"C:\\\\x\",\"project_dir\":\"C:\\\\x\"},\"version\":\"2.1.322\"}" 'KAPI DISI: C:\x | uzak: yok | 2.1.322'
  ds "kabuk baska klasorde" "$K" "{\"workspace\":{\"current_dir\":\"C:\\\\proje\\\\alt\",\"project_dir\":\"$KJ\",\"added_dirs\":[\"C:\\\\proje\"]}}" 'karargah | konum: C:\proje\alt | uzak: C:\proje'
  ds "egik cizgi, harf buyuklugu, sondaki ayrac" 'y:\02_KARARGAHLAR\01_claude_code_karargahı\' "{\"workspace\":{\"current_dir\":\"Y:/02_karargahlar/01_claude_code_karargahı/\",\"project_dir\":\"Y:/02_karargahlar/01_claude_code_karargahı\",\"added_dirs\":[\"C:\\\\\"]}}" 'karargah | uzak: C:\'
  ds "bozuk girdi" "$K" '{"workspace":' 'durum satiri okunamadi: ' onek
  ds "bos girdi" "$K" '' 'ortam bilinmiyor | uzak: yok'
  ds "yalniz cwd alani" "$K" "{\"cwd\":\"$KJ\"}" 'karargah | uzak: yok'
  ds "uc uzak yer" 'C:\x' '{"workspace":{"current_dir":"C:\\x","project_dir":"C:\\x","added_dirs":["D:\\a","D:\\b","D:\\c"]},"session_name":"x","version":"2.1.322"}' 'karargah | uzak: D:\a (+2) | ad: x | 2.1.322'
fi

# ---------------------------------------------------------------- 3) --canli: urunun davranisi
if [ -n "$CANLI" ]; then
  CLAUDE=$(command -v claude || true)
  [ -z "$CLAUDE" ] && [ -x /opt/claude-code/bin/claude ] && CLAUDE=/opt/claude-code/bin/claude
  if [ -z "$CLAUDE" ]; then
    atlandi "canli" "claude yok"
  else
    L="$GECICI/canli"; mkdir -p "$L/kok/gecici/kanit" "$L/uzak yer" "$L/dis" "$L/ev" "$L/ayar"
    T1="KOK-$RANDOM-$RANDOM"; T2="UZAK-$RANDOM-$RANDOM"; T3="DIS-$RANDOM-$RANDOM"
    echo "$T1" > "$L/kok/gecici/kanit/kok_isaret.txt"; echo "$T2" > "$L/uzak yer/uzak_isaret.txt"; echo "$T3" > "$L/dis/dis_isaret.txt"
    ISTEM="Uc dosyayi Read araciyla okumayi dene. Her dosya icin tek satir yaz: okuyabildiysen icerigini aynen, okuyamadiysan RED. Baska hicbir sey yazma. Dosyalar: gecici/kanit/kok_isaret.txt ve $L/uzak yer/uzak_isaret.txt ve $L/dis/dis_isaret.txt"
    # Temiz ortam: oturumun kendi degiskenleri ve ayarlari karismaz. Read her yol icin izinli; sinir yalniz ayardan gelir.
    cagir() { (cd "$L/kok" && env -i PATH="$PATH" HOME="$L/ev" CLAUDE_CONFIG_DIR="$L/ayar" TERM=dumb timeout 180 "$CLAUDE" "--add-dir=$L/uzak yer" --model "${SINA_MODEL:-haiku}" --permission-mode default --allowedTools Read --tools Read -p "$ISTEM" --no-session-persistence </dev/null 2>&1); }

    CIKTI=$(cagir)
    sina "canli: goreli yol calisma dizinine gore cozulur" "$CIKTI" "$T1"
    sina "canli: --add-dir= ile eklenen bosluklu klasor okunur" "$CIKTI" "$T2"
    sina "canli: sinir ayari yokken disaridaki dosya okunur (karsilastirma)" "$CIKTI" "$T3"

    mkdir -p "$L/kok/.claude"; cp "$KIT_KOKU/kit/.claude/settings.json" "$L/kok/.claude/settings.json"
    CIKTI=$(cagir)
    sina "canli: kit ayariyla kok ve uzak yer yine okunur" "$CIKTI" "$T1" 'printf "%s" "$CIKTI" | grep -qF -- "$T2"'
    sina "canli: kit ayariyla disaridaki dosya okunamaz" "$CIKTI" "RED" '! printf "%s" "$CIKTI" | grep -qF -- "$T3"'
  fi
fi

echo "SONUC   $gecen gecti, $kalan kaldi, $atlanan atlandi"
[ "$kalan" -gt 0 ] && exit 1
exit 0

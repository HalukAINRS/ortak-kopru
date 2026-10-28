#!/usr/bin/env bash
# Actions için: yalnız köprü, üretilen ayna ve çağrı günlüklerini gönderir.
# Hata halinde push yapılmaz; bilinmeyen çakışmalarda taraf seçilmez.
set -euo pipefail

if ! dal=$(git symbolic-ref --quiet --short HEAD) || [[ "$dal" != main ]]; then
  echo "HATA: bulut göndericisi yalnız main dalında çalışır." >&2
  exit 1
fi
for islem in rebase-merge rebase-apply MERGE_HEAD CHERRY_PICK_HEAD; do
  if [[ -e "$(git rev-parse --git-path "$islem")" ]]; then
    echo "HATA: devam eden Git işlemi var: $islem" >&2
    exit 1
  fi
done
while IFS= read -r -d '' dosya; do
  case "$dosya" in
    kopru.html|ayna/kopru.html|kayit/*) ;;
    *) echo "HATA: gönderim kapsamı dışında hazırlanmış dosya: $dosya" >&2; exit 1 ;;
  esac
done < <(git diff --cached --name-only -z)

python defter/kopru_ekle.py kopru.html --kontrol
python defter/kopru_ayna_uret.py kopru.html ayna/kopru.html
git config user.name "kopru-bot"
git config user.email "kopru-bot@users.noreply.github.com"
git add -- kopru.html ayna/kopru.html kayit
if git diff --cached --quiet; then
  echo "Değişiklik yok."
  exit 0
fi
git commit -m "köprü: bot yanıtları ve ayna [skip ci]"

rebase_durdur() {
  echo "HATA: $1" >&2
  git rebase --abort || true
  exit 1
}

for deneme in 1 2 3; do
  git fetch -q origin main
  if ! git rebase origin/main; then
    for tur in {1..20}; do
      cakisanlar=()
      while IFS= read -r -d '' dosya; do
        cakisanlar+=("$dosya")
      done < <(git diff --name-only --diff-filter=U -z)
      if ((${#cakisanlar[@]} == 0)); then
        rebase_durdur "Rebase durdu; çözülebilir dosya çakışması yok."
      fi
      # Önce bütün yolları denetle; tanınmayan dosyayı asla otomatik ezme.
      for dosya in "${cakisanlar[@]}"; do
        case "$dosya" in
          kopru.html|ayna/kopru.html|kayit/*.log) ;;
          *) rebase_durdur "Elle çözüm gereken çakışma: $dosya" ;;
        esac
      done
      for dosya in "${cakisanlar[@]}"; do
        case "$dosya" in
          kopru.html)
            python defter/kopru_birlestir.py --rebase kopru.html || rebase_durdur "Köprü birleştirilemedi."
            git add -- kopru.html
            ;;
          kayit/*.log)
            python defter/kopru_birlestir.py --rebase-metin "$dosya" || rebase_durdur "Günlük birleştirilemedi."
            git add -- "$dosya"
            ;;
        esac
      done
      python defter/kopru_ekle.py kopru.html --kontrol || rebase_durdur "Birleşen köprü denetimi geçmedi."
      python defter/kopru_ayna_uret.py kopru.html ayna/kopru.html || rebase_durdur "Ayna üretilemedi."
      git add -- ayna/kopru.html
      if GIT_EDITOR=true git rebase --continue; then
        break
      fi
      if ((tur == 20)); then
        rebase_durdur "Yirmi turda rebase tamamlanamadı."
      fi
    done
  fi

  # Temiz bir rebase de kanonik sayfayı değiştirebilir; aynayı tekrar denetle.
  python defter/kopru_ekle.py kopru.html --kontrol
  python defter/kopru_ayna_uret.py kopru.html ayna/kopru.html
  git add -- ayna/kopru.html
  if ! git diff --cached --quiet; then
    git commit -m "köprü: birleşen sayfanın aynası [skip ci]"
  fi
  if git push origin HEAD:main; then
    echo "Gönderildi."
    exit 0
  fi
  echo "Gönderim reddedildi; deneme $deneme/3." >&2
done

echo "HATA: üç denemede gönderilemedi; yerel commit korunuyor." >&2
exit 1

# ortak-kopru arşivi: 4 Kasım 2026

Bu kayıt, `ortak-kopru` deposu 4 Kasım 2026'da Haluk'un isteğiyle ("Repo sıfırlansın.") sıfırlanmadan hemen önce alınan tam arşivin dizinidir. Arşiv aynı depoda, GitHub arayüzünde dal ya da etiket olarak görünmeyen ref'lerde durur; Git ile alınır.

## Ne saklanıyor

- `refs/arsiv/2026-11-04/heads/*`: sıfırlamadan önceki 30 dalın son hâli. `main`'in son kaydı `6653d4df63fcb314e56ff9a1633d2c0acf2bd6f8`.
- `refs/arsiv/2026-11-04/pull/*`: 26 değişiklik önerisinin (PR) GitHub'daki ref'leri.
- `refs/arsiv/2026-11-04/kayitlar`: bu dizin. `refs.txt` özgün ref listesidir; `github/` altında konuların, değişiklik önerilerinin, yorumların, incelemelerin ve etiketlerin JSON dökümü var.

Eski `main` tarayıcıda: https://github.com/HalukAINRS/ortak-kopru/tree/6653d4df63fcb314e56ff9a1633d2c0acf2bd6f8

## Arşivi almak

    git clone https://github.com/HalukAINRS/ortak-kopru.git
    cd ortak-kopru
    git fetch origin 'refs/arsiv/2026-11-04/*:refs/arsiv/2026-11-04/*'
    git switch -c eski-main refs/arsiv/2026-11-04/heads/main

## Depoyu eski hâline döndürmek

Arşivi aldıktan sonra:

    git push --force origin 'refs/arsiv/2026-11-04/heads/*:refs/heads/*'

Kapatılan değişiklik önerileri ve konu GitHub'da elle yeniden açılabilir.

## Arşivi silmek

    git ls-remote origin 'refs/arsiv/2026-11-04/*' | awk '{print ":" $2}' | xargs git push origin

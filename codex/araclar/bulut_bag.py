"""Codex karargâhından Codex Cloud görevlerini yönlendirir."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys

sys.dont_write_bytecode = True
KOK = Path(__file__).resolve().parents[1]
AYAR_YOLU = KOK / 'yapilandirma' / 'bulut_bag.json'


class BaglantiHatasi(ValueError):
    pass


def ayar_oku() -> dict:
    ayar = json.loads(AYAR_YOLU.read_text(encoding='utf-8'))
    if ayar.get('bicim') != 1 or ayar.get('ana_environment') != 'CLI':
        raise BaglantiHatasi('Bulut bağlantısının biçimi veya ana ortamı geçersiz.')
    if ayar['codex_cli']['remote_environment'] != '.':
        raise BaglantiHatasi('Codex CLI hedefi karargâh kökü olmalı.')
    return ayar


def kok_yolu(goreli: str) -> Path:
    yol = (KOK / goreli).resolve()
    if not yol.is_relative_to(KOK):
        raise BaglantiHatasi('Yapılandırılan yerel yol karargâh dışında.')
    return yol


def kimlik_denetle(deger: str, tur: str) -> str:
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.:-]{0,199}', deger):
        raise BaglantiHatasi(tur + ' kimliği geçersiz.')
    return deger


def komut(ayar: dict, argumanlar: list[str], *, yakala=False):
    program = kok_yolu(ayar['codex_cli']['yurutulebilir'])
    profil = kok_yolu(ayar['codex_cli']['profil'])
    if not program.is_file() or program.suffix.lower() != '.exe':
        raise BaglantiHatasi('Yapılandırılan Codex uygulaması bulunamadı.')
    if not profil.is_dir():
        raise BaglantiHatasi('Yapılandırılan Codex profili bulunamadı.')
    ortam = dict(os.environ)
    ortam['CODEX_HOME'] = str(profil)
    return subprocess.run(
        [str(program), *argumanlar], cwd=KOK, env=ortam, shell=False,
        capture_output=yakala, text=True, encoding='utf-8', errors='replace',
        check=False,
    )


def json_yaz(deger):
    print(json.dumps(deger, ensure_ascii=False, indent=2))


def ana(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    alt = parser.add_subparsers(dest='islem', required=True)
    alt.add_parser('durum', help='Yerel hedefi, girişi ve bulut seçimini gösterir.')
    ortam_parser = alt.add_parser('ortam', help='Bulut servisinin ortam kimliğini kaydeder.')
    ortam_parser.add_argument('kimlik')
    liste_parser = alt.add_parser('liste', help='Bulut görevlerini JSON olarak listeler.')
    liste_parser.add_argument('--limit', type=int, choices=range(1, 21), default=20)
    gonder_parser = alt.add_parser('gonder', help='Seçili ortamda bir bulut görevi başlatır.')
    gonder_parser.add_argument('gorev')
    for ad in ('sonuc', 'fark'):
        alt.add_parser(ad).add_argument('gorev_kimligi')
    args = parser.parse_args(argv)
    try:
        ayar = ayar_oku()
        bulut = ayar['codex_bulut']
        if args.islem == 'durum':
            surum = komut(ayar, ['--version'], yakala=True)
            giris = komut(ayar, ['login', 'status'], yakala=True)
            json_yaz({
                'ana_environment': ayar['ana_environment'],
                'codex_cli_remote_environment': str(KOK),
                'codex_bulut_remote_environment': bulut['remote_environment'],
                'depo': bulut['depo'], 'dal': bulut['dal'],
                'ortam_kimligi': bulut['ortam_kimligi'],
                'codex_surumu': surum.stdout.strip(),
                'codex_profil': str(kok_yolu(ayar['codex_cli']['profil'])),
                'giris_var': giris.returncode == 0,
                'bulut_gonderimi_icin_ayar_var': bool(bulut['ortam_kimligi']),
            })
            return surum.returncode or giris.returncode
        if args.islem == 'ortam':
            bulut['ortam_kimligi'] = kimlik_denetle(args.kimlik, 'Ortam')
            AYAR_YOLU.write_text(json.dumps(ayar, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
            json_yaz({'ortam_kimligi': bulut['ortam_kimligi'], 'servis_dogrulamasi': 'Görev gönderiminde yapılır.'})
            return 0
        if args.islem == 'liste':
            argumanlar = ['cloud', 'list', '--json', '--limit', str(args.limit)]
            if bulut['ortam_kimligi']:
                argumanlar += ['--env', kimlik_denetle(bulut['ortam_kimligi'], 'Ortam')]
        elif args.islem == 'gonder':
            if not bulut['ortam_kimligi']:
                raise BaglantiHatasi('Bulut ortamı seçilmedi. Doğrulanan ENV_ID değerini ortam komutuyla kaydet.')
            if not args.gorev.strip():
                raise BaglantiHatasi('Görev açıklaması boş olamaz.')
            argumanlar = ['cloud', 'exec', '--env', kimlik_denetle(bulut['ortam_kimligi'], 'Ortam'),
                          '--branch', bulut['dal'], '--', args.gorev]
        else:
            gorev = kimlik_denetle(args.gorev_kimligi, 'Görev')
            argumanlar = ['cloud', 'status' if args.islem == 'sonuc' else 'diff', '--', gorev]
        return komut(ayar, argumanlar).returncode
    except (BaglantiHatasi, OSError, KeyError, json.JSONDecodeError) as hata:
        print('Hata: ' + str(hata), file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(ana())

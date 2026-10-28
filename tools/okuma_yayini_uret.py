#!/usr/bin/env python3
"""Build the static reader pages from the repository's prose, with no network.

The small supported Markdown subset is intentional: headings, paragraphs,
links, bold, inline code, simple lists, explicit safe heading anchors, HTML comment
marker lines (skipped) and plain-text blocks fenced with three backticks (unlabelled
or labelled text).
Use --check in CI to detect publication drift without writing files.
"""
from __future__ import annotations

import argparse
import html
import posixpath
import re
from pathlib import Path
from urllib.parse import quote, urlencode, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REPO = 'https://github.com/HalukAINRS/ortak-kopru'
# Katkı kalıbı (.github/ISSUE_TEMPLATE/karsilik.yml): yer ve başlık alanları bağlantıdan dolar.
KARSILIK = REPO + '/issues/new?template=karsilik.yml'
# docs/ altındaki kaynak → depo kökündeki sayfa. Sayfa adları Web adresidir; değişmez.
PAGES = {
    'web-girisi.md': ('index.html', 'Ortak Köprü'),
    'acilis.md': ('acilis.html', 'Açılış: Kapı ve Köprü'),
    'yol.md': ('yol.html', 'Açılıştan gerçeğe: yol'),
    'gecmis/ortak-mimari-defteri.md': ('mimari.html', 'Ortak Mimari Defteri'),
    'gecmis/anlam-not-defteri.md': ('not-defteri.html', 'Anlam ve Dönüş Defteri'),
    'gecmis/son-durum.md': ('durum.html', 'Son durum'),
    'gecmis/kaynaklar.md': ('kaynaklar.html', 'Kaynaklar'),
}


def slug(value: str) -> str:
    value = value.replace('İ', 'I').lower()
    return re.sub(r'\s+', '-', re.sub(r'[^\w\s-]', '', value)).strip('-')


def destination(value: str, folder: str = '') -> str:
    """Resolve a link written in docs/<folder>/ to the published page or the file on GitHub."""
    parsed = urlsplit(value)
    if parsed.scheme and parsed.scheme not in ('https', 'http'):
        raise ValueError(f'Unsupported link scheme: {parsed.scheme}')
    prefix = REPO + '/blob/main/docs/'
    if parsed.scheme:
        filename, sep, fragment = value[len(prefix):].partition('#') if value.startswith(prefix) else ('', '', '')
        return PAGES[filename][0] + (sep + fragment if sep else '') if filename in PAGES else value
    filename, sep, fragment = value.partition('#')
    tail = sep + fragment if sep else ''
    if not filename:
        return value
    path = posixpath.normpath(posixpath.join('docs', folder, filename))   # repository-relative
    inside = path[len('docs/'):] if path.startswith('docs/') else None
    if inside in PAGES:
        return PAGES[inside][0] + tail
    if path in ('kopru.html', *(target for target, _ in PAGES.values())):
        return path + tail
    kind = 'tree' if filename.endswith('/') else 'blob'
    return f'{REPO}/{kind}/main/{path}' + tail


TOKEN = re.compile(r'\[([^\]\n]+)\]\(([^\s)]+)\)|\*\*([^*\n]+)\*\*|`([^`\n]+)`')
FENCE = re.compile(r'^[ \t]*(`{3,}|~{3,})(.*)$')


def inline(value: str, folder: str = '') -> str:
    result = []
    start = 0
    for match in TOKEN.finditer(value):
        result.append(html.escape(value[start:match.start()]))
        if match.group(1) is not None:
            target = html.escape(destination(match.group(2), folder), quote=True)
            result.append(f'<a href="{target}">{html.escape(match.group(1))}</a>')
        elif match.group(3) is not None:
            result.append('<strong>' + html.escape(match.group(3)) + '</strong>')
        else:
            result.append('<code>' + html.escape(match.group(4)) + '</code>')
        start = match.end()
    result.append(html.escape(value[start:]))
    return ''.join(result)


def blocks(source: str) -> list[tuple[str, str]]:
    """Separate literal text before splitting prose at blank lines."""
    result: list[tuple[str, str]] = []
    prose: list[str] = []
    literal: list[str] | None = None
    opened_at = 0

    def flush_prose() -> None:
        text = ''.join(prose).strip()
        if text:
            result.extend(('prose', block) for block in re.split(r'\n\s*\n', text))
        prose.clear()

    for number, raw_line in enumerate(source.splitlines(keepends=True), 1):
        line = raw_line.rstrip('\r\n')
        fence = FENCE.fullmatch(line)
        if literal is not None:
            if fence:
                if fence.group(1) != '```' or fence.group(2).strip():
                    raise ValueError(f'Mismatched closing fence at line {number}; expected ```.')
                result.append(('text', ''.join(literal)))
                literal = None
            else:
                literal.append(raw_line)
        elif fence:
            if fence.group(1) != '```' or fence.group(2).strip() not in ('', 'text'):
                raise ValueError(f'Unsupported fenced block at line {number}; use ``` or ```text.')
            flush_prose()
            literal = []
            opened_at = number
        else:
            prose.append(raw_line)

    if literal is not None:
        raise ValueError(f'Unclosed plain-text fence opened at line {opened_at}.')
    flush_prose()
    return result


def karsilik(sayfa: str, sayfa_adi: str, anchor: str = '', baslik: str = '') -> str:
    """Katkı kalıbını, yeri (sayfa#bölüm) ve başlığı doldurulmuş olarak açan adres."""
    yer = f'{sayfa}#{anchor}' if anchor else sayfa
    konu = f'[Karşılık] {sayfa_adi}' + (f' · {baslik}' if baslik else '')
    return KARSILIK + '&' + urlencode({'yer': yer, 'title': konu}, quote_via=quote)


def _karsilik_paragrafi(sayfa: str, sayfa_adi: str, anchor: str, baslik: str) -> str:
    duz = re.sub(r'[*`]', '', baslik)
    adres = html.escape(karsilik(sayfa, sayfa_adi, anchor, duz), quote=True)
    etiket = html.escape(f'“{duz}” bölümüne karşılık ver', quote=True)
    return f'<p class="karsilik"><a href="{adres}" aria-label="{etiket}">Bu bölüme karşılık ver</a></p>'


def render(source: str, folder: str = '', sayfa: str = '', sayfa_adi: str = '') -> tuple[str, list[tuple[str, str]]]:
    """Kaynağı HTML'e çevirir. Sayfa adı verilirse her ikinci düzey bölümün sonuna bir karşılık bağlantısı konur."""
    output, headings = [], []
    bolum: tuple[str, str] | None = None

    def bolumu_kapat() -> None:
        if sayfa and bolum:
            output.append(_karsilik_paragrafi(sayfa, sayfa_adi, *bolum))

    for kind, block in blocks(source):
        if kind == 'text':
            output.append('<pre tabindex="0"><code>' + html.escape(block) + '</code></pre>')
            continue
        if re.fullmatch(r'<a id="[\w-]+"></a>', block):
            # The heading immediately below receives the same stable ID.
            continue
        if re.fullmatch(r'<!--[^<>]*-->', block):
            # Generated-block markers (tools/acilis.py) are source bookkeeping, not reader text.
            continue
        heading = re.fullmatch(r'(#{1,3}) (.+)', block)
        if heading:
            level, title = len(heading.group(1)), heading.group(2)
            anchor = slug(title)
            if level <= 2:
                bolumu_kapat()
                bolum = (anchor, title) if level == 2 else None
            output.append(f'<h{level} id="{anchor}">{inline(title, folder)}</h{level}>')
            if level == 2:
                headings.append((anchor, title))
        elif all(line.startswith('- ') for line in block.splitlines()):
            output.append('<ul>' + ''.join('<li>' + inline(line[2:], folder) + '</li>' for line in block.splitlines()) + '</ul>')
        else:
            if block.startswith(('```', '|', '[^')):
                raise ValueError('Use the supported prose Markdown subset for reader pages.')
            output.append('<p>' + inline(' '.join(block.splitlines()), folder) + '</p>')
    bolumu_kapat()
    return '\n'.join(output), headings


def page(filename: str, output_name: str, label: str) -> str:
    body, headings = render((ROOT / 'docs' / filename).read_text(encoding='utf-8'), posixpath.dirname(filename),
                            output_name, label)
    nav = ''.join(f'<a href="{target}"' + (' aria-current="page"' if target == output_name else '') + f'>{html.escape(name)}</a>' for target, name in [('index.html', 'Başlangıç'), ('acilis.html', 'Açılış'), ('yol.html', 'Yol'), ('mimari.html', 'Mimari defteri'), ('not-defteri.html', 'Not defteri'), ('durum.html', 'Son durum'), ('kaynaklar.html', 'Kaynaklar')])
    contents = ''.join(f'<li><a href="#{anchor}">{html.escape(title)}</a></li>' for anchor, title in headings)
    title = label if output_name == 'index.html' else label + ' · Ortak Köprü'
    return f'''<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Ortak Köprü: Web ile yerel bilgisayar arasında bir kapı, dışarıdaki bireyler ile yerel kullanıcı arasında bir köprü.">
<title>{html.escape(title)}</title>
<link rel="stylesheet" href="okuma.css">
</head>
<body>
<a class="skip" href="#icerik">İçeriğe geç</a>
<header class="site-header"><a class="brand" href="index.html">Ortak Köprü</a><nav class="site-nav" aria-label="Ana gezinme">{nav}<a href="{REPO}/issues">Katkı</a></nav></header>
<div class="page-shell">
<main id="icerik"><div class="eyebrow">Kapı · Köprü · Karşılık</div>
{body}
<div class="closing"><p>Bir soru, farklı yorum veya kaynakla katkı sunabilirsiniz. <a href="{html.escape(karsilik(output_name, label), quote=True)}">Bu sayfaya karşılık verin</a> · <a href="{REPO}/blob/main/docs/{filename}">Bu metnin kaynağı ve sürümleri</a></p></div>
</main>
<aside aria-label="Bu sayfadaki bölümler"><h2>Bu sayfada</h2><ul class="contents">{contents}</ul><div class="reader-note"><p>Bir paragrafı paylaşırken başlığını ve kaynak bağını da taşıyın.</p><p><a href="{REPO}/blob/main/CONTRIBUTING.md">Katkı rehberi</a></p></div></aside>
</div>
<footer class="site-footer"><span>Ortak Köprü · <a href="{REPO}/commits/main/docs/{filename}">bu metnin değişiklik geçmişi</a></span><span><a href="{REPO}">GitHub deposu</a> · <a href="kopru.html">Tarihsel köprü defteri</a></span></footer>
</body>
</html>
'''


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    mismatches = []
    for filename, (output_name, label) in PAGES.items():
        expected = page(filename, output_name, label).encode('utf-8')
        path = ROOT / output_name
        if args.check:
            if not path.is_file() or path.read_bytes() != expected:
                mismatches.append(output_name)
        else:
            path.write_bytes(expected)
    if mismatches:
        print('Reader publication is out of date: ' + ', '.join(mismatches))
        print('Run: python tools/okuma_yayini_uret.py')
        return 1
    print('Reader publication matches its source paragraphs.' if args.check else f'Built {len(PAGES)} static reader pages.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

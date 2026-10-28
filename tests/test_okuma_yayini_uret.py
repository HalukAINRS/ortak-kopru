"""Okuma sayfaları: çizim blokları, bağlantılar ve her bölümün karşılık bağlantısı (katkı kalıbı).

Literal diagram blocks must survive publication without becoming markup; every published section
ends with a link that opens the reply form with its page and section already filled in.
"""
import html
import re
import unittest
from urllib.parse import parse_qs, urlsplit

from tools import okuma_yayini_uret as reader

FORM = reader.ROOT / '.github' / 'ISSUE_TEMPLATE' / 'karsilik.yml'
FORM_AYARI = reader.ROOT / '.github' / 'ISSUE_TEMPLATE' / 'config.yml'
YANIT = re.compile(r'<p class="karsilik"><a href="([^"]+)" aria-label="([^"]+)">Bu bölüme karşılık ver</a></p>')

try:  # İsteğe bağlı: varsa form yapısı tam okunur; yoksa satır denetimi yeter.
    import yaml
except ImportError:  # pragma: no cover - depends on the machine
    yaml = None


def sorgu(adres: str) -> dict[str, str]:
    parca = urlsplit(html.unescape(adres))
    return {anahtar: degerler[0] for anahtar, degerler in parse_qs(parca.query).items()}


class ReaderPublicationTests(unittest.TestCase):
    def test_text_blocks_preserve_spacing_and_escape_markup(self):
        literal = '  +---+\n  | <tag> & "x" |\n\n    **text**\t \n'
        expected = (
            '<pre tabindex="0"><code>  +---+\n'
            '  | &lt;tag&gt; &amp; &quot;x&quot; |\n\n'
            '    **text**\t \n</code></pre>'
        )
        for opening in ('```', '```text'):
            with self.subTest(opening=opening):
                body, headings = reader.render(opening + '\n' + literal + '```\n')
                self.assertEqual(body, expected)
                self.assertEqual(headings, [])

    def test_unclosed_fence_has_an_explicit_error(self):
        with self.assertRaisesRegex(ValueError, 'Unclosed plain-text fence opened at line 3'):
            reader.render('Bir paragraf.\n\n```text\n  çizim\n')

    def test_unsupported_and_mismatched_fences_are_rejected(self):
        cases = (
            ('```python\nx\n```', 'Unsupported fenced block'),
            ('~~~text\nx\n~~~', 'Unsupported fenced block'),
            ('````\nx\n````', 'Unsupported fenced block'),
            ('```text\nx\n````', 'Mismatched closing fence'),
            ('```text\nx\n~~~', 'Mismatched closing fence'),
            ('```\nx\n```text', 'Mismatched closing fence'),
        )
        for source, message in cases:
            with self.subTest(source=source):
                with self.assertRaisesRegex(ValueError, message):
                    reader.render(source)

    def test_existing_prose_and_headings_continue_around_a_text_block(self):
        source = (
            '# Başlık\n\nBir **vurgu** ve `kod`.\n'
            '```text\n  | x |\n```\n'
            '## Devam\n\n- Bir\n- İki\n\n'
            '[Kaynak](gecmis/kaynaklar.md)'
        )
        body, headings = reader.render(source)
        self.assertEqual(body, '\n'.join((
            '<h1 id="başlık">Başlık</h1>',
            '<p>Bir <strong>vurgu</strong> ve <code>kod</code>.</p>',
            '<pre tabindex="0"><code>  | x |\n</code></pre>',
            '<h2 id="devam">Devam</h2>',
            '<ul><li>Bir</li><li>İki</li></ul>',
            '<p><a href="kaynaklar.html">Kaynak</a></p>',
        )))
        self.assertEqual(headings, [('devam', 'Devam')])

    def test_generated_block_markers_are_not_reader_text(self):
        body, _ = reader.render('<!-- uretilen:acilis -->\n\nAçılış paragrafı.\n\n<!-- /uretilen:acilis -->\n')
        self.assertEqual(body, '<p>Açılış paragrafı.</p>')
        body, _ = reader.render('Metin <!-- satır içi --> sürer.\n')
        self.assertIn('&lt;!-- satır içi --&gt;', body)

    def test_links_resolve_from_the_source_folder(self):
        repo = reader.REPO
        cases = {
            ('../acilis.md', 'gecmis'): 'acilis.html',
            ('anlam-not-defteri.md#ilk', 'gecmis'): 'not-defteri.html#ilk',
            ('gecmis/durum-raporu-2026-10-28.md', ''): 'durum.html',
            ('../teknik/README.md#otomasyon', 'gecmis'): repo + '/blob/main/docs/teknik/README.md#otomasyon',
            ('../../kopru.html', 'gecmis'): 'kopru.html',
            ('../defter/kopru_ekle.py', ''): repo + '/blob/main/defter/kopru_ekle.py',
            ('rafine/', 'gecmis'): repo + '/tree/main/docs/gecmis/rafine',
            ('#bolum', 'gecmis'): '#bolum',
            (repo + '/blob/main/docs/acilis.md', ''): 'acilis.html',
            ('https://example.org/x', ''): 'https://example.org/x',
        }
        for (link, folder), expected in cases.items():
            with self.subTest(link=link, folder=folder):
                self.assertEqual(reader.destination(link, folder), expected)
        # Every published page has its source under docs/, and every source exists.
        for source in reader.PAGES:
            with self.subTest(source=source):
                self.assertTrue((reader.ROOT / 'docs' / source).is_file())

    def test_each_section_offers_a_linked_reply(self):
        source = ('# Başlık\n\nGiriş.\n\n## Birinci bölüm\n\nMetin.\n\n### Alt başlık\n\nAlt metin.\n\n'
                  '## İkinci `kod` bölüm\n\nSon.\n')
        body, headings = reader.render(source, '', 'acilis.html', 'Açılış')
        self.assertEqual([a for a, _ in headings], ['birinci-bölüm', 'ikinci-kod-bölüm'])
        replies = YANIT.findall(body)
        self.assertEqual(len(replies), 2)
        # Bir karşılık, bölümünün bütün metninden (alt başlıklar dahil) sonra ve sonraki bölümden önce gelir.
        first, second = (body.index(href) for href, _ in replies)
        self.assertLess(body.index('Alt metin.'), first)
        self.assertLess(first, body.index('<h2 id="' + headings[1][0]))
        self.assertLess(body.index('Son.'), second)
        self.assertNotIn('Giriş.</p>\n<p class="karsilik"', body)
        self.assertEqual(sorgu(replies[0][0]), {'template': 'karsilik.yml', 'yer': 'acilis.html#birinci-bölüm',
                                                'title': '[Karşılık] Açılış · Birinci bölüm'})
        self.assertEqual(sorgu(replies[1][0])['title'], '[Karşılık] Açılış · İkinci kod bölüm')
        self.assertIn('Birinci bölüm', replies[0][1])
        # Sayfa adı verilmeyen çeviri bağlantı eklemez; öteki sınamalar bu sade hâle dayanır.
        self.assertNotIn('karsilik', reader.render(source)[0])
        self.assertIn('template=karsilik', reader.KARSILIK)

    def test_every_published_page_keeps_unix_line_endings(self):
        # Windows'ta da üretilen sayfa ile depodaki sayfa aynı kalsın: her sayfa .gitattributes'ta eol=lf.
        nitelikler = (reader.ROOT / '.gitattributes').read_text(encoding='utf-8').splitlines()
        for output, _ in reader.PAGES.values():
            with self.subTest(page=output):
                self.assertIn(f'/{output} text eol=lf', nitelikler)

    def test_published_pages_link_every_section_to_its_reply(self):
        for source, (output, label) in reader.PAGES.items():
            with self.subTest(page=output):
                text = (reader.ROOT / output).read_text(encoding='utf-8')
                ids = set(re.findall(r' id="([^"]+)"', text))
                sections = re.findall(r'<h2 id="([^"]+)"', text)
                replies = YANIT.findall(text)
                self.assertEqual(len(replies), len(sections))
                for (href, _), anchor in zip(replies, sections):
                    query = sorgu(href)
                    self.assertEqual(query['template'], 'karsilik.yml')
                    self.assertEqual(query['yer'], f'{output}#{anchor}')
                    self.assertIn(query['yer'].split('#', 1)[1], ids)
                    self.assertTrue(query['title'].startswith(f'[Karşılık] {label} · '))
                closing = re.search(r'<div class="closing"><p>.*?<a href="([^"]+)">Bu sayfaya karşılık verin</a>', text)
                self.assertIsNotNone(closing)
                self.assertEqual(sorgu(closing.group(1))['yer'], output)


class ReplyFormTests(unittest.TestCase):
    """GitHub'daki katkı kalıbı, bağlantıların doldurduğu alanları taşır ve sınırı hatırlatır."""

    def test_form_has_the_fields_the_links_fill(self):
        text = FORM.read_text(encoding='utf-8')
        types = re.findall(r'^\s*- type:\s*(\S+)', text, re.M)
        ids = re.findall(r'^\s+id:\s*(\S+)', text, re.M)
        self.assertEqual(ids, ['tur', 'yer', 'metin', 'dayanak', 'sinir'])
        self.assertTrue(set(types) <= {'markdown', 'dropdown', 'input', 'textarea', 'checkboxes'})
        self.assertRegex(text, r'(?m)^title: "\[Karşılık\] "$')
        self.assertGreaterEqual(text.count('required: true'), 4)
        # Bağlantının doldurduğu her alan formda vardır; başlık GitHub'ın kendi alanıdır.
        filled = set(sorgu(reader.karsilik('acilis.html', 'Açılış', 'niyet', 'Niyet'))) - {'template', 'title'}
        self.assertEqual(filled, {'yer'})
        self.assertTrue(filled <= set(ids))
        self.assertTrue(reader.KARSILIK.endswith('template=' + FORM.name))
        self.assertIn('herkese açık', text)
        settings = FORM_AYARI.read_text(encoding='utf-8')
        self.assertIn('blank_issues_enabled: true', settings)
        self.assertIn('https://halukainrs.github.io/ortak-kopru/acilis.html', settings)
        self.assertTrue((reader.ROOT / 'acilis.html').is_file())

    @unittest.skipIf(yaml is None, 'PyYAML yok; satır denetimi yukarıda yapıldı')
    def test_form_structure_when_yaml_is_available(self):
        form = yaml.safe_load(FORM.read_text(encoding='utf-8'))
        self.assertLessEqual({'name', 'description', 'body'}, set(form))
        ids = [alan['id'] for alan in form['body'] if 'id' in alan]
        self.assertEqual(len(ids), len(set(ids)))
        for alan in form['body']:
            with self.subTest(alan=alan.get('id', alan['type'])):
                if alan['type'] != 'markdown':
                    self.assertTrue(alan['attributes']['label'])
                if alan['type'] in ('dropdown', 'checkboxes'):
                    self.assertTrue(alan['attributes']['options'])
        settings = yaml.safe_load(FORM_AYARI.read_text(encoding='utf-8'))
        self.assertTrue(settings['blank_issues_enabled'])
        self.assertTrue(all(link['url'].startswith('https://') for link in settings['contact_links']))


if __name__ == '__main__':
    unittest.main()

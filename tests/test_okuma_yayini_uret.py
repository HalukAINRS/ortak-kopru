"""Literal diagram blocks must survive publication without becoming markup."""
import unittest

from tools import okuma_yayini_uret as reader


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
            '[Kaynak](KAYNAKLAR.md)'
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


if __name__ == '__main__':
    unittest.main()

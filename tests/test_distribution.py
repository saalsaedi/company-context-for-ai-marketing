"""Distribution invariants for v1.1; these do not test a model's conversation."""
import hashlib
import json
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from build_package import build, NAME


class DistributionTests(unittest.TestCase):
    def test_both_archives_are_deterministic_and_match_checksums(self):
        with tempfile.TemporaryDirectory() as tmp:
            one, two = Path(tmp) / 'one', Path(tmp) / 'two'
            first, second = build(one), build(two)
            self.assertEqual(first['artifacts'], second['artifacts'])
            release = json.loads((ROOT / 'release.json').read_text(encoding='utf-8'))
            self.assertEqual(first['version'], release['version'])
            for artifact in first['artifacts']:
                path = one / artifact['path']
                self.assertIn(release['version'], path.name)
                self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), artifact['sha256'])
                with zipfile.ZipFile(path) as archive:
                    self.assertIsNone(archive.testzip())
            checksums = (one / first['checksums']).read_text(encoding='utf-8')
            self.assertEqual(checksums, ''.join(a['sha256'] + '  ' + a['path'] + '\n' for a in first['artifacts']))

    def test_first_reply_and_starter_template_reach_all_distributions(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            manifest = build(output)
            with zipfile.ZipFile(output / manifest['archive']) as native, zipfile.ZipFile(output / manifest['chatgpt_archive']) as chat:
                combined = chat.read('chatgpt-setup/templates-and-schemas.txt').decode('utf-8')
                for name in ('first-reply.json', 'starter-context.md'):
                    source = (ROOT / 'templates' / name).read_text(encoding='utf-8')
                    self.assertEqual(native.read(NAME + '/templates/' + name).decode('utf-8'), source)
                    self.assertIn('===== FILE: templates/' + name + ' =====\n\n' + source, combined)
                guided = (ROOT / 'references/beginner-guided-mode.md').read_text(encoding='utf-8')
                self.assertEqual(native.read(NAME + '/references/beginner-guided-mode.md').decode('utf-8'), guided)
                self.assertIn(guided, chat.read('chatgpt-setup/workflow-reference.txt').decode('utf-8'))

    def test_new_build_does_not_overwrite_old_downloads(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            names = (NAME + '-1.0.0.zip', 'chatgpt-setup-1.0.0.zip', 'SHA256SUMS.txt')
            for name in names:
                (output / name).write_bytes(b'previous-release-canary')
            build(output)
            for name in names:
                self.assertEqual((output / name).read_bytes(), b'previous-release-canary')

    def test_chatgpt_archive_excludes_leftover_files_and_hashes_exact_payload(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            (output / 'chatgpt').mkdir()
            (output / 'chatgpt/private-notes.txt').write_text('not distributable', encoding='utf-8')
            manifest = build(output)
            with zipfile.ZipFile(output / manifest['chatgpt_archive']) as chat:
                expected = {'chatgpt-setup/' + Path(a['path']).name for a in manifest['chatgpt_files']}
                self.assertEqual(set(chat.namelist()), expected)
                for artifact in manifest['chatgpt_files']:
                    data = chat.read('chatgpt-setup/' + Path(artifact['path']).name)
                    self.assertEqual(hashlib.sha256(data).hexdigest(), artifact['sha256'])

    def test_schema_compatibility_survives_skill_version_change(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            manifest = build(output)
            self.assertEqual(manifest['context_schema_version'], '1.0.0')
            with zipfile.ZipFile(output / manifest['archive']) as native:
                for source in (ROOT / 'schemas').glob('*.json'):
                    self.assertEqual(native.read(NAME + '/schemas/' + source.name), source.read_bytes())
                packaged_release = json.loads(native.read(NAME + '/release.json'))
                self.assertEqual(packaged_release['version'], manifest['version'])

    def test_build_rejects_output_in_skill_source(self):
        with self.assertRaises(ValueError):
            build(ROOT / 'dist')

    def test_opening_copy_is_short_and_bilingual(self):
        copy = json.loads((ROOT / 'templates/first-reply.json').read_text(encoding='utf-8'))
        self.assertEqual(set(copy), {'ar', 'en'})
        for locale in copy.values():
            self.assertTrue(locale['intro'].strip())
            self.assertTrue(locale['question'].strip())
            self.assertLessEqual(len((locale['intro'] + ' ' + locale['question']).split()), 100)


if __name__ == '__main__':
    unittest.main()

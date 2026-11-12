import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARKER = "@@PYCODE_MARKER@@"


class PortableBuilderSyncTests(unittest.TestCase):
    def test_embedded_python_matches_main_source(self):
        builder = (ROOT / "MatrixDownloader_Build.bat").read_text(encoding="utf-8")
        main_source = (ROOT / "main.py").read_text(encoding="utf-8")

        self.assertIn(MARKER, builder)
        embedded_source = builder.rsplit(MARKER, 1)[1].lstrip("\r\n")
        normalize = lambda value: value.replace("\r\n", "\n").rstrip()

        self.assertEqual(normalize(embedded_source), normalize(main_source))


if __name__ == "__main__":
    unittest.main()

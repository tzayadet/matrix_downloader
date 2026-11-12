import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARKER = "@@PYCODE_MARKER@@"


class PortableBuilderSyncTests(unittest.TestCase):
    def test_embedded_python_matches_main_source(self):
        builder = (ROOT / "MatrixDownloader_Build.bat").read_text(encoding="utf-8")
        main_source = (ROOT / "main.py").read_text(encoding="utf-8")

        self.assertIn(MARKER, builder)
        embedded_source = builder.rsplit(MARKER, 1)[1].split("@@FILENAME_UTILS_MARKER@@", 1)[0].lstrip("\r\n")
        normalize = lambda value: value.replace("\r\n", "\n").rstrip()

        self.assertEqual(normalize(embedded_source), normalize(main_source))

    def test_embedded_filename_utility_matches_source(self):
        builder = (ROOT / "MatrixDownloader_Build.bat").read_text(encoding="utf-8")
        utility_source = (ROOT / "filename_utils.py").read_text(encoding="utf-8")

        self.assertIn("@@FILENAME_UTILS_MARKER@@", builder)
        embedded_source = builder.rsplit("@@FILENAME_UTILS_MARKER@@", 1)[1].lstrip("\r\n")
        normalize = lambda value: value.replace("\r\n", "\n").rstrip()

        self.assertEqual(normalize(embedded_source), normalize(utility_source))


if __name__ == "__main__":
    unittest.main()

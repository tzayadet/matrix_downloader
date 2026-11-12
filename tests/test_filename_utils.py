import unittest

from filename_utils import sanitize_filename


class SanitizeFilenameTests(unittest.TestCase):
    def test_replaces_path_separators_and_invalid_characters(self):
        result = sanitize_filename(r"folder\\video:name?.mp4")
        self.assertNotIn("/", result)
        self.assertNotIn("\\", result)
        self.assertNotIn(":", result)
        self.assertNotIn("?", result)

    def test_collapses_whitespace_and_strips_dots(self):
        self.assertEqual(sanitize_filename("  ..  My   video.mp4  .. "), "My video.mp4")

    def test_handles_empty_names_and_windows_reserved_names(self):
        self.assertEqual(sanitize_filename("..."), "download")
        self.assertEqual(sanitize_filename("CON"), "_CON")
        self.assertEqual(sanitize_filename("Lpt1.txt"), "_Lpt1.txt")

    def test_limits_filename_component_length(self):
        self.assertEqual(len(sanitize_filename("x" * 300)), 160)


if __name__ == "__main__":
    unittest.main()

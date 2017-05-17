from unittest import TestCase


class TestFormat_license_key(TestCase):
    def test_format_license_key(self):
        try:
            from build import format_license_key
        except ImportError:
            self.assertFalse("No function found")

            self.assertEqual(TypeError, format_license_key, None, None)
        license_key = '---'
        k = 3
        expected = ''
        self.assertEqual(format_license_key(license_key, k), expected)
        license_key = '2-4A0r7-4k'
        k = 3
        expected = '24-A0R-74K'
        self.assertEqual(format_license_key(license_key, k), expected)
        license_key = '2-4A0r7-4k'
        k = 4
        expected = '24A0-R74K'
        self.assertEqual(format_license_key(license_key, k), expected)

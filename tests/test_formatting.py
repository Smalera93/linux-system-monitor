import unittest
from system_monitor.formatting import (
    LABEL_WIDTH,
    LABELS,
    format_bytes,
)

class TestFormatting(unittest.TestCase):

    def test_LABEL_WIDTH_length(self):
        self.assertEqual(LABEL_WIDTH, max(len(label) for label in LABELS))

    def test_format_bytes_zero(self):
        result = format_bytes(0)
        self.assertEqual(result, "0 B")

    def test_format_bytes_bytes(self):
        result = format_bytes(1023)
        self.assertEqual(result, "1023 B")

    def test_format_bytes_one_kib(self):
            result = format_bytes(1024)
            self.assertEqual(result, "1.00 KiB")

    def test_format_bytes_kib(self):
            result = format_bytes(1536)
            self.assertEqual(result, "1.50 KiB")

    def test_format_bytes_one_mib(self):
            result = format_bytes(1024 ** 2)
            self.assertEqual(result, "1.00 MiB")

    def test_format_bytes_mib(self):
            result = format_bytes(5 * 1024 ** 2)
            self.assertEqual(result, "5.00 MiB")

    def test_format_bytes_one_gib(self):
            result = format_bytes(1024 ** 3)
            self.assertEqual(result, "1.00 GiB")

    def test_format_bytes_gib(self):
            result = format_bytes(2.5 * 1024 ** 3)
            self.assertEqual(result, "2.50 GiB")
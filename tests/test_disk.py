import unittest
from system_monitor.disk import (
    bytes_to_gib,
    calculate_used_disk_percent,
    format_disk
)

class TestDisk(unittest.TestCase):
        
    def test_bytes_to_gib_0(self):
        self.assertEqual(bytes_to_gib (0), 0.0)
    def test_bytes_to_gib_1(self):
        self.assertEqual(bytes_to_gib (1073741824), 1.0)
    def test_bytes_to_gib_2_gib(self):
        self.assertEqual(bytes_to_gib (2147483648), 2.0)

    def test_calculate_used_disk_percent_37_63(self):
        self.assertEqual(calculate_used_disk_percent (37, 63), 37.0)
    def test_calculate_used_disk_percent_0_100(self):
        self.assertEqual(calculate_used_disk_percent (0, 100), 0.0)
    def test_calculate_used_disk_percent_100_0(self):
        self.assertEqual(calculate_used_disk_percent (100, 0), 100.0)

    def test_calculate_used_disk_percent_zero(self):
        with self.assertRaises(ValueError):
            calculate_used_disk_percent (0, 0)
    def test_calculate_used_disk_percent_negative_used(self):
        with self.assertRaises(ValueError):
            calculate_used_disk_percent (-1, 100)
    def test_calculate_used_disk_percent_negative_free(self):
        with self.assertRaises(ValueError):
            calculate_used_disk_percent (100, -1)

    def test_format_disk_normal_values(self):
        self.assertEqual(format_disk("/", 3.272, 1.111, 2.161, 66.1), ['Disk: (/):', 'Total: 3.27 GiB', 'Used: 1.11 GiB', 'Free: 2.16 GiB', 'Usage: 66.1%'])
    def test_format_disk_zero_values(self):
        self.assertEqual(format_disk("/", 0.0, 0.0, 0.0, 0.0), ['Disk: (/):', 'Total: 0.00 GiB', 'Used: 0.00 GiB', 'Free: 0.00 GiB', 'Usage: 0.0%'])
    def test_format_disk_random_rounding_values(self):
        self.assertEqual(format_disk("/", 3.274, 1.116, 2.158, 65.55), ['Disk: (/):', 'Total: 3.27 GiB', 'Used: 1.12 GiB', 'Free: 2.16 GiB', 'Usage: 65.5%'])
    def test_format_disk_whole_numbers_values(self):
        self.assertEqual(format_disk("/", 4.0, 2.0, 2.0, 50.0), ['Disk: (/):', 'Total: 4.00 GiB', 'Used: 2.00 GiB', 'Free: 2.00 GiB', 'Usage: 50.0%'])

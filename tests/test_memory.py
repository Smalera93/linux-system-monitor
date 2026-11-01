import unittest
from system_monitor.memory import (
    calculate_memory_usage,
    kib_to_gib,
    calculate_memory_percent,
    format_memory
)

class TestMemory(unittest.TestCase):
   
    def test_percent_zero_total(self):
        with self.assertRaises(ValueError):
            calculate_memory_percent(0,0)
    def test_percent_negative_total(self):
        with self.assertRaises(ValueError):
            calculate_memory_percent(-10,0)
    def test_percent_negative_used(self):
        with self.assertRaises(ValueError):
            calculate_memory_percent(100,-10)
    def test_percent_used_more_than_total(self):
        with self.assertRaises(ValueError):
            calculate_memory_percent(100,110)

    def test_percent_total_100_used_0(self):
        self.assertEqual(calculate_memory_percent(100,0), 0.0)
    def test_percent_total_100_used_50(self):
        self.assertEqual(calculate_memory_percent(100,50), 50.0)
    def test_percent_total_100_used_100(self):
        self.assertEqual(calculate_memory_percent(100,100), 100.0)

    def test_calculate_total_100_available_0(self):
        self.assertEqual(calculate_memory_usage(100,0), 100)
    def test_calculate_total_100_available_50(self):
        self.assertEqual(calculate_memory_usage(100,50), 50)
    def test_calculate_total_100_available_100(self):
        self.assertEqual(calculate_memory_usage(100,100), 0)

    def test_kib_to_gib_0(self):
        self.assertEqual(kib_to_gib (0), 0.0)
    def test_kib_to_gib_1_gib(self):
        self.assertEqual(kib_to_gib (1048576), 1.0)
    def test_kib_to_gib_2_gib(self):
        self.assertEqual(kib_to_gib (2097152), 2.0)
    def test_kib_to_gib_between_1_and_2_gib(self):
        self.assertAlmostEqual(kib_to_gib (1536000), 1.4648, places=4)

    def test_format_memory_normal_values(self):
        self.assertEqual(format_memory(3.272, 1.111, 2.161, 66.1), ['Total: 3.27 GiB', 'Available: 1.11 GiB', 'Used: 2.16 GiB', 'Usage: 66.1%'])
    def test_format_memory_zero_values(self):
        self.assertEqual(format_memory(0.0, 0.0, 0.0, 0.0), ['Total: 0.00 GiB', 'Available: 0.00 GiB', 'Used: 0.00 GiB', 'Usage: 0.0%'])
    def test_format_memory_random_rounding_values(self):
        self.assertEqual(format_memory(3.274, 1.116, 2.158, 65.55), ['Total: 3.27 GiB', 'Available: 1.12 GiB', 'Used: 2.16 GiB', 'Usage: 65.5%'])
    def test_format_memory_whole_numbers_values(self):
        self.assertEqual(format_memory(4.0, 2.0, 2.0, 50.0), ['Total: 4.00 GiB', 'Available: 2.00 GiB', 'Used: 2.00 GiB', 'Usage: 50.0%'])
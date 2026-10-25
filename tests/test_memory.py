import unittest
from system_monitor.memory import (
    calculate_memory_usage,
    kib_to_gib,
    calculate_memory_percent
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
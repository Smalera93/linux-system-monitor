import unittest

from system_monitor.formatting import LABEL_WIDTH
from system_monitor.cpu import (
    calculate_cpu_usage,
    format_cpu,
)

class TestCpu(unittest.TestCase):

    def test_cpu_usage_twenty_percent(self):
        first_sample = (10, 0, 10, 80, 0, 0, 0, 0)
        second_sample = (20, 0, 20, 160, 0, 0, 0, 0)
        result = calculate_cpu_usage(first_sample, second_sample)
        self.assertEqual(result, 20.0)

    def test_cpu_usage_zero_percent(self):
        first_sample = (0, 0, 0, 100, 0, 0, 0, 0)
        second_sample = (0, 0, 0, 200, 0, 0, 0, 0)
        result = calculate_cpu_usage(first_sample, second_sample)
        self.assertEqual(result, 0.0)

    def test_cpu_usage_one_hundred_percent(self):
        first_sample = (0, 0, 0, 100, 0, 0, 0, 0)
        second_sample = (100, 0, 0, 100, 0, 0, 0, 0)
        result = calculate_cpu_usage(first_sample, second_sample)
        self.assertEqual(result, 100.0)

    def test_cpu_usage_with_iowait(self):
        first_sample = (10, 0, 10, 70, 10, 0, 0, 0)
        second_sample = (20, 0, 20, 140, 20, 0, 0, 0)
        result = calculate_cpu_usage(first_sample, second_sample)
        self.assertEqual(result, 20.0)

    def test_cpu_usage_twenty_percent(self):
        first_sample = (10, 0, 10, 80, 0, 0, 0, 0)
        second_sample = (20, 0, 20, 160, 0, 0, 0, 0)
        result = calculate_cpu_usage(first_sample, second_sample)
        self.assertEqual(result, 20.0)

    def test_identical_samples_raise_value__error(self):
        sample = (10, 0, 10, 80, 0, 0, 0, 0)
        with self.assertRaises(ValueError):
            calculate_cpu_usage(sample, sample)

    def test_format_cpu(self):
        result = format_cpu(25.0)
        expected = f"{'Usage:':<{LABEL_WIDTH}} 25.0%"
        self.assertEqual(result,expected)

    def test_format_cpu_zero_percent(self):
        result = format_cpu(0.0)
        expected = f"{'Usage:':<{LABEL_WIDTH}} 0.0%"
        self.assertEqual(result,expected)

    def test_format_cpu_rounding(self):
        result = format_cpu(12.345)
        expected = f"{'Usage:':<{LABEL_WIDTH}} 12.3%"
        self.assertEqual(result,expected)
import unittest
from system_monitor.formatting import LABEL_WIDTH
from system_monitor.network import (
    calculate_network_rate,
    format_network,
)

class TestFormatNetwork(unittest.TestCase):

    def test_network_rate(self):
        first_sample = (1000, 500)
        second_sample = (3000, 1500)
        result = calculate_network_rate(first_sample, second_sample, 2)
        self.assertEqual(result, (1000.0, 500.0))

    def test_network_rate_zero_traffic(self):
            first_sample = (1000, 500)
            second_sample = (1000, 500)
            result = calculate_network_rate(first_sample, second_sample, 1)
            self.assertEqual(result, (0.0, 0.0))
        
    def test_network_rate_different_interval(self):
            first_sample = (1000, 500)
            second_sample = (5000, 2500)
            result = calculate_network_rate(first_sample, second_sample, 4)
            self.assertEqual(result, (1000.0, 500.0))

    def test_zero_interval_raises_value_error(self):
            with self.assertRaises(ValueError):
                calculate_network_rate((1000, 500), (2000, 1000), 0)

    def test_negative_interval_raises_value_error(self):
                with self.assertRaises(ValueError):
                    calculate_network_rate((1000, 500), (2000, 1000), -1)

    def test_received_counter_decrease_raises_value_error(self):
                with self.assertRaises(ValueError):
                    calculate_network_rate((2000, 500), (1000, 1000), 1)

    def test_transmitted_counter_decrease_raises_value_error(self):
                with self.assertRaises(ValueError):
                    calculate_network_rate((1000, 2000), (2000, 1000), 1)


    def test_format_network_bytes(self):
        result = format_network(500, 250, 100, 50)
        expected = (
            f"{'Received:':<{LABEL_WIDTH}} 500 B",
            f"{'Sent:':<{LABEL_WIDTH}} 250 B",
            f"{'Download:':<{LABEL_WIDTH}} 100 B/s",
            f"{'Upload:':<{LABEL_WIDTH}} 50 B/s",
        )
        self.assertEqual(result, expected)

    def test_format_network_kib(self):
            result = format_network(2048, 1024, 2048, 1024)
            expected = (
                f"{'Received:':<{LABEL_WIDTH}} 2.00 KiB",
                f"{'Sent:':<{LABEL_WIDTH}} 1.00 KiB",
                f"{'Download:':<{LABEL_WIDTH}} 2.00 KiB/s",
                f"{'Upload:':<{LABEL_WIDTH}} 1.00 KiB/s",
            )
            self.assertEqual(result, expected)
    
    def test_format_network_mib(self):
            result = format_network(
                   5 * 1024 ** 2, 
                   2 * 1024 ** 2,
                   3 * 1024 ** 2,
                   1024 ** 2,
                   )
            expected = (
                f"{'Received:':<{LABEL_WIDTH}} 5.00 MiB",
                f"{'Sent:':<{LABEL_WIDTH}} 2.00 MiB",
                f"{'Download:':<{LABEL_WIDTH}} 3.00 MiB/s",
                f"{'Upload:':<{LABEL_WIDTH}} 1.00 MiB/s",
            )
            self.assertEqual(result, expected)

    def test_format_network_gib(self):
            result = format_network(
                   2 * 1024 ** 3, 
                   1024 ** 3,
                   2 * 1024 **3,
                   1024 ** 3,                   
                   )
            expected = (
                f"{'Received:':<{LABEL_WIDTH}} 2.00 GiB",
                f"{'Sent:':<{LABEL_WIDTH}} 1.00 GiB",
                f"{'Download:':<{LABEL_WIDTH}} 2.00 GiB/s",
                f"{'Upload:':<{LABEL_WIDTH}} 1.00 GiB/s",
            )
            self.assertEqual(result, expected)

    def test_format_network_zero(self):
            result = format_network(0, 0, 0, 0)
            expected = (
                f"{'Received:':<{LABEL_WIDTH}} 0 B",
                f"{'Sent:':<{LABEL_WIDTH}} 0 B",
                f"{'Download:':<{LABEL_WIDTH}} 0 B/s",
                f"{'Upload:':<{LABEL_WIDTH}} 0 B/s",
            )
            self.assertEqual(result, expected)
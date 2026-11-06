import unittest
from system_monitor.formatting import LABEL_WIDTH
from system_monitor.network import (
    format_network,
)

class TestFormatNetwor(unittest.TestCase):

    def test_format_network_bytes(self):
        result = format_network(500, 250)
        expected = (
            f"{'Received:':<{LABEL_WIDTH}} 500 B",
            f"{'Sent:':<{LABEL_WIDTH}} 250 B",
        )
        self.assertEqual(result, expected)

    def test_format_network_kib(self):
            result = format_network(2048, 1024)
            expected = (
                f"{'Received:':<{LABEL_WIDTH}} 2.00 KiB",
                f"{'Sent:':<{LABEL_WIDTH}} 1.00 KiB",
            )
            self.assertEqual(result, expected)
    
    def test_format_network_mib(self):
            result = format_network(5 * 1024 ** 2, 2 * 1024 ** 2)
            expected = (
                f"{'Received:':<{LABEL_WIDTH}} 5.00 MiB",
                f"{'Sent:':<{LABEL_WIDTH}} 2.00 MiB",
            )
            self.assertEqual(result, expected)

    def test_format_network_gib(self):
            result = format_network(2 * 1024 ** 3, 1024 ** 3)
            expected = (
                f"{'Received:':<{LABEL_WIDTH}} 2.00 GiB",
                f"{'Sent:':<{LABEL_WIDTH}} 1.00 GiB",
            )
            self.assertEqual(result, expected)

    def test_format_network_zero(self):
            result = format_network(0, 0)
            expected = (
                f"{'Received:':<{LABEL_WIDTH}} 0 B",
                f"{'Sent:':<{LABEL_WIDTH}} 0 B",
            )
            self.assertEqual(result, expected)
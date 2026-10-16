import unittest
from system_monitor.uptime import seconds_to_hms

class TestUpTime(unittest.TestCase):

    def test_uptime_conversion(self):
        self.assertEqual(seconds_to_hms(3672), (1, 1, 12))
    def test_zero_seconds(self):
        self.assertEqual(seconds_to_hms(0), (0,0,0))
    def test_just_before_minute(self):
        self.assertEqual(seconds_to_hms(59), (0,0,59))
    def test_exactly_one_minute(self):
        self.assertEqual(seconds_to_hms(60), (0,1,0))
    def test_just_after_one_minute(self):
        self.assertEqual(seconds_to_hms(61), (0,1,1))
    def test_just_before_hour(self):
        self.assertEqual(seconds_to_hms(3599), (0,59,59))
    def test_exactly_one_hour(self):
        self.assertEqual(seconds_to_hms(3600), (1,0,0))
    def test_just_after_one_hour(self):
        self.assertEqual(seconds_to_hms(3601), (1,0,1))
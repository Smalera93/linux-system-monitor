import unittest
from system_monitor.uptime import (
    seconds_to_hms,
    format_uptime,
)

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

    def test_zero_seconds_format(self):
        self.assertEqual(format_uptime(0,0,0), ("0 seconds"))
    def test_seven_seconds_format(self):
        self.assertEqual(format_uptime(0,0,7), ("7 seconds"))
    def test_three_minutes_seven_seconds_format(self):
        self.assertEqual(format_uptime(0,3,7), ("3 minutes and 7 seconds"))
    def test_two_hours_one_minute_seven_seconds_format(self):
        self.assertEqual(format_uptime(2,1,7), ("2 hours, 1 minute and 7 seconds"))

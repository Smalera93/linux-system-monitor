import unittest
from system_monitor.formatting import (
    LABEL_WIDTH,
    LABELS
)

class TestFormatting(unittest.TestCase):

    def test_LABEL_WIDTH_length(self):
        self.assertEqual(LABEL_WIDTH, max(len(label) for label in LABELS))
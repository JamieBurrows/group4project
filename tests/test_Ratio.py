from unittest import TestCase
from functions import Ratio


class Test(TestCase):
    def test_ratio(self):
        self.assertEqual(Ratio.ratio(40,20), 2)



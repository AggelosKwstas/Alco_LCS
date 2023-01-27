import unittest
from LCS import LCS_sub_sequence
from Brute_Force import Brute_Force


class MyTestCase(unittest.TestCase):

    def test_Brute_Force(self):
        self.assertEqual(Brute_Force("AATCGAG", "CCATCGG"), (5, "ATCGG"))

    def test_LCS(self):
        self.assertEqual(LCS_sub_sequence("AATCGAG", "CCATCGG"), (5, "ATCGG"))


if __name__ == "__main__":
    unittest.main()

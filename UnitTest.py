import unittest
from LCS import Compute_LCS
from Brute_Force import Brute_Force


class MyTestCase(unittest.TestCase):


    # test brute_force
    def test_Brute_Force(self):
        self.assertEqual(Brute_Force("AATCGAG", "CCATCGG")[::-1], "ATCGG")
        self.assertEqual(Brute_Force("AAGCGTTCC", "ACGTGCGTC")[::-1], "AGCGTC")

    # test lcs

    def test_LCS(self):
        self.assertEqual(Compute_LCS("AATCGAG", "CCATCGG"), (5, "ATCGG"))
        self.assertEqual(Brute_Force("AAGCGTTCC", "ACGTGCGTC"), (6, "CTGCGA"))


if __name__ == "__main__":
    unittest.main()

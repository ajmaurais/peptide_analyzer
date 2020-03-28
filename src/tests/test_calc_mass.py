
import unittest
from collections import Counter

import load_dat
import std_functions

from molecular_formula import calc_mass

class TestCalcFormula(unittest.TestCase):
    def test_calc_formula(self):
        for i, row in load_dat.dat_std.iterrows():
            self.assertAlmostEqual(float(row['mass']),
                                   calc_mass(std_functions._calc_formula(row['seq'],
                                                                         load_dat.atom_counts)))

if __name__ == '__main__':
    unittest.main(verbosity=2)

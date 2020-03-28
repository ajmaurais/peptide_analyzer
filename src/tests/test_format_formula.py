
import unittest

import load_dat
import std_functions

from molecular_formula import format_formula

class TestCalcFormula(unittest.TestCase):
    def test_calc_formula(self):
        for i, row in load_dat.dat_std.iterrows():
            formula_count = std_functions._calc_formula(row['seq'], load_dat.atom_counts)
            test_formated_formula = std_functions._parse_formula(row['formula'])
            std_formated_formula = std_functions._parse_formula(std_functions._format_formula(formula_count))
            self.assertDictEqual(test_formated_formula, std_formated_formula)


if __name__ == '__main__':
    unittest.main(verbosity=2)



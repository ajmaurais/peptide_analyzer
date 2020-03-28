
import unittest
import os

import load_dat
from molecular_formula import read_atom_count_table

class TestReadAtomCountTable(unittest.TestCase):

    ATOM_COUNT_PATH = os.path.dirname(os.path.abspath(__file__)) + '/data/residue_atoms.txt'
    
    def test_read_atom_count_table(self):
        test_atom_counts = read_atom_count_table(self.ATOM_COUNT_PATH)
        for k, v in test_atom_counts.items():
            self.assertDictEqual(v, load_dat.atom_counts[k])


if __name__ == '__main__':
    unittest.main(verbosity=2)


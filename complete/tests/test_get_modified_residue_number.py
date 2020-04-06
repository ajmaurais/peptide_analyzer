
import os
import unittest

import load_dat
from std_functions import read_record
from uniprot import get_modified_residue_numbers

class TestGetModifiedResidueNumbers(unittest.TestCase):

    def test_std_get_modified_residue_number(self):

        test_count = 0
        for i, row in load_dat.dat_std.iterrows():
            record = read_record(row['ID'])
            if record is not None:
                protein_seq = record.sequence
                mods = get_modified_residue_numbers(row['seq'], protein_seq)
                self.assertEqual(row['modified_residue'], mods)
                test_count += 1
        self.assertNotEqual(test_count, 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)


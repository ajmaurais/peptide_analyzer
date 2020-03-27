
import os
import unittest

import load_dat
import fasta
from main import get_modified_residue_numbers

class TestGetModifiedResidueNumbers(unittest.TestCase):
    
    FASTA_PATH = os.path.dirname(os.path.abspath(__file__)) + '/../../testData/sequences.fasta'

    def test_std_get_modified_residue_number(self):
        fasta_db = fasta.FastaFile()
        fasta_db.read(self.FASTA_PATH)
        for i, row in load_dat.dat_std.iterrows():
            if fasta_db.id_exists(row['ID']):
                protein_seq = fasta_db.get_sequence(row['ID'])
                mod_locs = get_modified_residue_numbers(row['seq'], protein_seq)
                mods = '|'.join(['{}{}'.format(protein_seq[x], x + 1) for x in mod_locs])
                self.assertEqual(row['modified_residue'], mods)

if __name__ == '__main__':
    unittest.main(verbosity=2)


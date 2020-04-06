
import os
import re
import unittest

import load_dat
from uniprot import get_protein_location
from std_functions import read_records

class TestGetProteinLocation(unittest.TestCase):

    RECORDS_PATH = os.path.dirname(os.path.abspath(__file__)) + '/data/uniprot_txt'
    SPLIT_RE = r'\s?[,]\s?'

    def test_get_protein_location(self):
        records = read_records(self.RECORDS_PATH)
        for i, row in load_dat.dat_std.iterrows():
            if row['ID'] in records: 
                test_set = set(x.lower().strip() for x in re.split(self.SPLIT_RE,
                                                                   get_protein_location(records[row['ID']].comments)))
            else:
                test_set = set('-')
            std_set = set(x.lower().strip() for x in re.split(self.SPLIT_RE, row['subcelluar_loc']))
            self.assertSetEqual(test_set, std_set)


if __name__ == '__main__':
    unittest.main(verbosity=2)


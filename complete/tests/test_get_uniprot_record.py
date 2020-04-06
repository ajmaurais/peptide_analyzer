
import os
import unittest

import load_dat
from biopython_lite.Bio.SwissProt import Record
from uniprot import get_unipror_record

class TestGetUniproRecord(unittest.TestCase):

    def test_returns_record(self):
        test_record = get_unipror_record('P08670')
        self.assertIsInstance(test_record, Record)

    def test_handles_dummy_id(self):
        test_record = get_unipror_record('DUMMY_ID')
        self.assertIsNone(test_record)

    def test_handles_redirect(self):
        test_record = get_unipror_record('P08107')
        self.assertIsNone(test_record)

if __name__ == '__main__':
    unittest.main(verbosity=2)


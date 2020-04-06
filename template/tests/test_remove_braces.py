
import os
import unittest

import load_dat
from uniprot import remove_braces

class TestRemoveBraces(unittest.TestCase):

    def test_works(self):
        test_strings = [('hello there {some stupid crap {more crap}} some useful text',
                         'hello there some useful text'),
                         ('a more simple string {with some crap}',
                          'a more simple string'),
                         ('a more {with some crap} simple string',
                          'a more simple string'),
                         ('a more {{with some crap}} simple string',
                          'a more simple string'),
                         ('{with some crap} a more simple string',
                          'a more simple string')]

        for input_str, output_str in test_strings:
            ret = remove_braces(input_str, open_brace='{', close_brace='}')
            ret = ret.replace('  ', ' ').strip()
            self.assertCountEqual(ret, output_str)


    def test_catches_unbalanced(self):
        unbalanced_braces = ['hello {there General Kenobi',
                             'hello there General} Kenobi',
                             'hello {there} {General Kenobi',
                             'hello {there}} {General Kenobi',
                             'hello {{there}} {General Kenobi',
                             'hello {{there}}} General Kenobi',
                             'hello {{{there}} General Kenobi']

        for s in unbalanced_braces:
            with self.assertRaises(ValueError):
                remove_braces(s)


if __name__ == '__main__':
    unittest.main(verbosity=2)


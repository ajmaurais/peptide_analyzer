
from collections import Counter

_ATOM_MASSES = {"C": 12,
                "H": 1.00783,
                "O": 15.99491,
                "N": 14.00307,
                "S": 31.97207,
                "P": 30.97376,
                "(15)N": 15.00011,
                "(2)H": 2.0141,
                "(13)C": 13.00335,
                "Se": 79.91652,
                "Cl": 34.96885,
                "Br": 78.91834}

def read_atom_count_table(fname):
    '''
    Read atom count table.

    Parameters
    ----------
    fname: str
        Path to file to read.

    Returns
    -------
    atom_counts: dict
        A dict with key value pairs for amino acids and
        Counter objects with their atom counts.
    '''

    with open(fname, 'r') as inF:
        lines = inF.readlines()
            
    headers = dict()
    headers_len = 0
    atom_counts=dict()
    for line in lines:
        elems = [x.strip() for x in line.split('\t')]
        if elems[0] == 'H':
            headers = [x for x in elems]
            headers_len = len(headers)
            atom_counts = {headers[i]: None for range(1, headers_len)}
            continue
        elif elems[0] == 'R':
            if not headers or len(elems) != headers_len:
                raise ValueError('Badly formed atom_table file!')
                for i in range(1, headers_len):
                    atom_counts[headers[i]]
            continue
        else:
            raise ValueError('Badly formed atom_table file!')



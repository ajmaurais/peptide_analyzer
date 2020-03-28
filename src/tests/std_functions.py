
import re
from collections import Counter

import load_dat

FORMULA_RE = r'({})([0-9]+)?'.format('|'.join(set([x.replace('(', '\(').replace(')', '\)')
    for r in load_dat.atom_counts.values() for x in r])))

def _calc_formula(sequence, residue_atoms):
    ''' Calculate formula counter from sequence. '''
    formula = Counter()
    for aa in sequence:
        formula.update(residue_atoms[aa])
    for t in ['N_term', 'C_term']:
        formula.update(residue_atoms[t])
    return formula

def _format_formula(formula):
    ''' Convert formula counter to string. '''
    pretty_formula = ''
    for k, v in formula.items():
        if v > 0:
            pretty_formula += '{}{}'.format(k, '' if v == 1 else v)
    return pretty_formula

def _parse_formula(formula):
    ''' Parser formula string and return formula Counter '''
    matches = re.findall(FORMULA_RE, formula)
    ret = Counter()
    for m in matches:
        count = 0 if m[1] == '' else m[0]
        ret[m[0]] = count
    return ret

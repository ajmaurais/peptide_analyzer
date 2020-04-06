
import os
import re
from collections import Counter

from biopython_lite.Bio import SwissProt

from load_dat import atom_counts

UNIPROT_ID_REGEX = '[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9](?:[A-Z][A-Z0-9]{2}[0-9]){1,2}'
FORMULA_RE = r'({})([0-9]+)?'.format('|'.join(set([x.replace('(', '\(').replace(')', '\)')
    for r in atom_counts.values() for x in r])))

def calc_formula(sequence, residue_atoms):
    ''' Calculate formula counter from sequence. '''
    formula = Counter()
    for aa in sequence:
        formula.update(residue_atoms[aa])
    for t in ['N_term', 'C_term']:
        formula.update(residue_atoms[t])
    return formula

def format_formula(formula):
    ''' Convert formula counter to string. '''
    pretty_formula = ''
    for k, v in formula.items():
        if v > 0:
            pretty_formula += '{}{}'.format(k, '' if v == 1 else v)
    return pretty_formula

def parse_formula(formula):
    ''' Parser formula string and return formula Counter '''
    matches = re.findall(FORMULA_RE, formula)
    ret = Counter()
    for m in matches:
        count = 0 if m[1] == '' else m[0]
        ret[m[0]] = count
    return ret


def _read_record(path):
    ''' Read record test at path. '''
    if os.path.exists(path):
        with open(path, 'r') as inF:
            return SwissProt.read(inF)
    else:
        return None

def read_record(uniprot_id):
    ''' Read record text and return Record '''
    path = '{}/{}/{}.txt'.format(os.path.abspath(os.path.dirname(__file__)), 'data/uniprot_txt', uniprot_id)
    return _read_record(path)

def read_records(base_path):
    matches = [re.search(r'({}).txt$'.format(UNIPROT_ID_REGEX), '{}/{}'.format(base_path, f))
               for f in os.listdir(base_path)]
    records = {match.group(1):_read_record(match.string) for match in matches if match}
    return records


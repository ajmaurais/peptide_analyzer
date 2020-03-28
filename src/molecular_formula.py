
from collections import Counter
import dataframe

ATOM_MASSES = {"C": 12,
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

    # read residue atoms table in to DataFrame
    residue_atoms = dataframe.read_tsv(fname)

    # Make a list of atoms included in the table
    atoms = [a for a in residue_atoms.columns if a != 'residue']
    
    # Iterate through residue_atoms rows
    atom_counts = dict()
    for i, row in residue_atoms.iterrows():

        # for each row initalize a Counter
        atom_counts[row['residue']] = Counter()

        # then add the atom counts for the current residue
        for atom in atoms:
            atom_counts[row['residue']][atom] = int(row[atom])

    return atom_counts


def calc_formula(sequence, residue_atoms):
    '''
    Calculate molecular formula for peptide sequence.

    Parameters
    ----------
    sequence: str
        Peptide sequence
    residue_atoms: dict of Counter(s)
        Dict key value pairs for amino acids, and their atom counts.

    Returns
    -------
    formula: Counter
        Atom counts for the whole peptide.
    '''

    # Initalize empty Counter container to add residue formulas to
    formula = Counter()

    # Iterate through sequence and update formula
    for aa in sequence:
        formula.update(residue_atoms[aa])

    # Don't forget to add the N and C terminus
    for t in ['N_term', 'C_term']:
        formula.update(residue_atoms[t])

    return formula
        

def format_formula(formula_counter):
    '''
    Get string representation of molecular formula_counter.

    Parameters
    ----------
    formula_counter: Counter
        Peptide formula as a Counter

    Returns
    -------
    pretty_formula: str
        String representation of formula.
    '''

    # Initalize string to return
    pretty_formula = ''

    # Iterate through items in formula_counter and append string to pretty_formula
    for k, v in formula_counter.items():
        if v > 0:
            pretty_formula += '{}{}'.format(k, '' if v == 1 else v)

    return pretty_formula


def calc_mass(formula_counter):
    '''
    Calculate peptide mass from foumula counter.

    Parameters
    ----------
    forumla_counter: Counter
        Peptide formula as a Counter

    Returns
    -------
    mass: float
        Peptide monoisotpoic mass
    '''
    
    # Initalize mass
    mass = float()

    # Iterate through items in formula_counter and add their masses to mass.
    # Use ATOM_MASSES to look up atom masses.
    for atom, count in formula_counter.items():
        mass += (ATOM_MASSES[atom] * count)
    
    return mass



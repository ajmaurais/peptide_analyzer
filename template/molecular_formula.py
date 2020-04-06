
import pandas as pd
from collections import Counter

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

    # read residue atoms table into pd.DataFrame

    # Make a list of atoms included in the table

    # Iterate through residue_atoms rows

        # for each row initialize a Counter

        # then add the atom counts for the current residue
    
    raise NotImplementedError('read_atom_count_table not implemented.')


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

    # Initialize empty Counter container to add residue formulas to

    # Iterate through sequence and update formula

    # Don't forget to add the N and C terminus

    raise NotImplementedError('calc_formula not implemented.')

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

    # Initialize string to return

    # Iterate through items in formula_counter and append string to pretty_formula

    raise NotImplementedError('format_formula not implemented.')



def calc_mass(formula_counter):
    '''
    Calculate peptide mass from formula counter.

    Parameters
    ----------
    forumla_counter: Counter
        Peptide formula as a Counter

    Returns
    -------
    mass: float
        Peptide monoisotopic mass
    '''

    # Initialize mass

    # Iterate through items in formula_counter and add their masses to mass.
    # Use ATOM_MASSES to look up atom masses.

    raise NotImplementedError('calc_mass not implemented.')



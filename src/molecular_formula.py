
from collections import Counter
import dataframe

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

    # read residue atoms table in to DataFrame
    residue_atoms = dataframe.read_tsv(fname)

    # Make a list of atoms included in the table
    atoms = [a for a in residue_atoms.columns if a != 'residue']
    
    # Iterate through residue_atoms rows
    atom_counts = dict()
    for i, row in residue_atoms.iterrows():

        # for each row add a Counter containing the number of atoms in each residue.
        atom_counts[row['residue']] = Counter()

        # then add the atom counts for the current residue
        for atom in atoms:
            atom_counts[row['residue']][atom] = int(row[atom])

    return atom_counts

def calc_formulas(sequence, residue_atoms):

    pass
        


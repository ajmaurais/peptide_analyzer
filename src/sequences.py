
import re

def get_modified_residue_numbers(peptide_seq, protein_seq):
    '''
    Get the numbers of modified modified peptide residues in the parent protein .
    Modification sites are indicated with a '*' after the modified residue.

    Parameters
    ----------
    peptide_seq: str
        Modified peptide sequence.
    protein_seq: str
        Parent protein sequence.

    Returns
    -------
    modifications: tuple
        0 indexed locations of modifications in parent protein.
    '''

    # Get peptide sequence without modifications
    unmodified_seq = peptide_seq.replace('*', '')

    # Find beginning index of peptide in parent protein
    peptide_begin = protein_seq.find(unmodified_seq)

    # Iterate through modification sites on peptide and determine their position on
    # the parent protein.
    peptide_sites = list()
    for i, m in enumerate(re.finditer(r'[A-Z]\*', peptide_seq)):
        peptide_sites.append(m.start() - 0)
    
    return tuple(i + peptide_begin for i in peptide_sites)



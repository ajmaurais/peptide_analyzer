
import sys
import argparse
import re

from dataframe import read_tsv, DataFrame
from fasta import FastaFile

def read_input(fname):
    '''
    Read input file.'

    Paramarers
    ----------
    fname: str
        Path to input file.

    Returns
    -------
    dat: DataFrame
        Data in fanme as a DataFrame.
    '''

    return read_tsv(fname)


def get_modified_residue_numbers(peptide_seq, protein_seq):
    '''
    Get the numbers of modified modified peptide residues in the parent protein .
    Modification sites are indicated with a '*' after the modified residue.

    Paramarers
    ----------
    peptide_seq: str
        Modified peptide sequence.
    protein_seq: str
        Parent protein sequence.

    Returns
    -------
    modifications: tuple
        0 indexed locaions of modifications in parent potein.
    '''

    # Get peptide sequence without modifications
    unmodified_seq = peptide_seq.replace('*', '')

    # Find begining index of peptide in parent protein
    peptide_begin = protein_seq.find(unmodified_seq)
    peptide_sites = list()
    for i, m in enumerate(re.finditer(r'[A-Z]\*', peptide_seq)):
        peptide_sites.append(m.start() - i)
        # for testing
        # temp = ''.join([str(x).center(3) for x in range(len(unmodified_seq))])
        # print('{}\n{} -> {}\n{}\n'.format(peptide_seq,
        #     ''.join([(x + '*' if i in peptide_sites else x).center(3) for i, x in enumerate(list(unmodified_seq))]),
        #     peptide_sites, temp))
    
    return tuple(i + peptide_begin for i in peptide_sites)


def main():
    '''
    Main method.

    This is the function which will be executed first when you call the program form the command line.
    '''

    parser = argparse.ArgumentParser(prog=__file__,
                                     description='Read a .tsv file containing peptides and uniprot '
                                     'IDs and do some analysis on them.')

    parser.add_argument('fasta_path', help='Path to fasta file to look up sequences.')

    parser.add_argument('input_file',
                        help='Path to input file. Should be tsv with two columns; "ID" and "seq".')

    args = parser.parse_args()

    dat = read_input(args.input_file)
    
    fasta_db = FastaFile()
    fasta_db.read(args.fasta_path)
    
    mod_locs = list()
    for pid, peptide_seq in zip(dat['ID'], dat['seq']):
        if fasta_db.id_exists(pid):
            protein_seq = fasta_db.get_sequence(pid)
            mods = get_modified_residue_numbers(peptide_seq, protein_seq)
            mod_locs.append('|'.join(['{}{}'.format(protein_seq[x], x + 1) for x in mods]))
        else:
            mod_locs.append('PROTEIN_SEQ_NOT_FOUND')
    dat['modified_residues'] = mod_locs
    print(dat)


if __name__ == '__main__':
    main()

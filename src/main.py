
import sys
import argparse
import re

from fasta import FastaFile
from dataframe import read_tsv, DataFrame

import sequences
import molecular_formula


def read_input(fname):
    '''
    Read input file.'

    Parameters
    ----------
    fname: str
        Path to input file.

    Returns
    -------
    dat: DataFrame
        Data in fanme as a DataFrame.
    '''

    return read_tsv(fname)


# def main():
#     '''
#     Main method.
# 
#     This is the function which will be executed first when you call the program form the command line.
#     '''
# 
#     # Load and parse command line arguments
#     parser = argparse.ArgumentParser(prog=__file__,
#                                      description='Read a .tsv file containing peptides and UniProt '
#                                      'IDs and do some analysis on them.')
#     parser.add_argument('atom_count_table',
#                         help='Path to table to look up numbers and types of atoms in each residue.')
#     parser.add_argument('fasta_path', help='Path to fasta file to look up sequences.')
#     parser.add_argument('input_file',
#                         help='Path to input file. Should be tsv with two columns; "ID" and "seq".')
#     args = parser.parse_args()

# Hard coded file paths for debuging
INPUT_FILE_PATH = 'data/input_peptides.tsv'
ATOM_COUNT_TABLE_PATH = 'data/residue_atoms.txt'
FASTA_FILE_PATH = 'data/sequences.fasta'
OUTPUT_FILE_PATH = 'data/output_peptide.tsv'

# read input file
# (Call read_dat and set the output to a variable named 'dat')
dat = read_input(INPUT_FILE_PATH)

# Load atom count table and save it to a variable.
# (Call molecular_formula.read_atom_count_table)
atom_counts = molecular_formula.read_atom_count_table(ATOM_COUNT_TABLE_PATH)

# Make a list of Counter(s) for each peptide sequence.
# (Call molecular_formula.calc_formula for each peptide sequence.)
formulas = [molecular_formula.calc_formula(seq, atom_counts) for seq in dat['seq']]

# Add a column to dat containing the peptide formula
# (Call molecular_formula.format_formula for each peptide sequence and set the result
# to a new column in dat named 'formula'.)
dat['formula'] = [molecular_formula.format_formula(f) for f in formulas]

# Add a column to dat containing the peptide mass
# (Call molecular_formula.calc_mass for each peptide sequence and set the result
# to a new column in dat named 'mass'.)
dat['mass'] = [molecular_formula.calc_mass(f) for f in formulas]

# Find modification sites in parent protein
# load .fasta file
fasta_db = FastaFile()
fasta_db.read(FASTA_FILE_PATH)

# Iterate through dat
mod_locs = list()
for i, row in dat.iterrows():
    # Check if the protein sequence exists in the fasta file.
    if fasta_db.id_exists(row['ID']):
        # Get the protein sequence for the current row from the .fasta file
        protein_seq = fasta_db.get_sequence(row['ID'])

        # Get the index locations of the modification(s) in the parent pritein sequence.
        # (Call sequence.get_modified_residue_numbers)
        mods = sequences.get_modified_residue_numbers(row['seq'], protein_seq)

        # Format the modification indecies as <residue><number>|...
        # Example: C53|C56 or C73
        mod_locs.append('|'.join(['{}{}'.format(protein_seq[x], x + 1) for x in mods]))

    else:
        mod_locs.append('PROTEIN_SEQ_NOT_FOUND')

# Add a column to dat named 'modified_residues'
dat['modified_residues'] = mod_locs

# Write dat to file (Call DataFrame.to_tsv)
dat.to_tsv('data/output_peptide.tsv')

# if __name__ == '__main__':
#     main()


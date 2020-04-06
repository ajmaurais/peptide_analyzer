
import os
import argparse
import re
import pandas as pd

import uniprot
import molecular_formula


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

# Hard coded file paths for debugging
BASE_DATA_PATH = os.path.abspath(os.path.dirname(__file__) + '/../data')
INPUT_FILE_PATH = BASE_DATA_PATH + '/input_peptides.tsv'
ATOM_COUNT_TABLE_PATH = BASE_DATA_PATH + '/residue_atoms.txt'
OUTPUT_FILE_PATH = BASE_DATA_PATH + '/output_peptides.tsv'

# read input file at INPUT_FILE_PATH
# (Call pd.read_csv and set the output to a variable named 'dat')
dat = pd.read_csv(INPUT_FILE_PATH, sep='\t')

# Load atom count table from ATOM_COUNT_TABLE_PATH and save it to a variable.
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

# Retrieve uniprot records for all protein IDs
# (Call uniprot.get_unipror_record for each protein ID and save the results to a dict)
records = {uniprot_id: uniprot.get_unipror_record(uniprot_id) for uniprot_id in dat['ID']}

# Iterate through dat
mod_locs = list()
go_fxn = list()
locations = list()
for i, row in dat.iterrows():
    # Check if there is a uniprot record for the current ID.
    if records[row['ID']] is not None:
        # Get the protein sequence for the current row from the Record
        protein_seq = records[row['ID']].sequence

        # Get the index locations of the modification(s) in the parent protein sequence.
        # (Call uniprot.get_modified_residue_numbers)
        mod_locs.append(uniprot.get_modified_residue_numbers(row['seq'], protein_seq))


        # Get the GO terms for protein function
        # (Call uniprot.get_go_fxn)
        go_fxn.append(uniprot.get_go_fxn(records[row['ID']].cross_references))

        # Get the subcellular location of the parent protein
        # The subcellular location are stored in the Record.comments member
        locations.append(uniprot.get_protein_location(records[row['ID']].comments))

    else:
        mod_locs.append('UNIPROT_RECORD_NOT_FOUND')
        locations.append('-')
        go_fxn.append('-')

# Add a column to dat named 'modified_residues'
dat['modified_residues'] = mod_locs
# Add a column to dat named 'go_fxn'
dat['go_fxn'] = go_fxn
# Add a column to dat named 'subcelluar_loc'
dat['subcelluar_loc'] = locations

# Write dat to OUTPUT_FILE_PATH (Call DataFrame.to_tsv)
dat.to_csv(OUTPUT_FILE_PATH, sep='\t', index=False)

# if __name__ == '__main__':
#     main()


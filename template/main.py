
import os
import re
import pandas as pd

import uniprot
import molecular_formula


# Hard coded file paths for debugging
BASE_DATA_PATH = os.path.abspath(os.path.dirname(__file__) + '/../data')
INPUT_FILE_PATH = BASE_DATA_PATH + '/input_peptides.tsv'
ATOM_COUNT_TABLE_PATH = BASE_DATA_PATH + '/residue_atoms.txt'
OUTPUT_FILE_PATH = BASE_DATA_PATH + '/output_peptides.tsv'

# read input file at INPUT_FILE_PATH
# (Call pd.read_csv and set the output to a variable named 'dat')

# Load atom count table from ATOM_COUNT_TABLE_PATH and save it to a variable.
# (Call molecular_formula.read_atom_count_table)

# Make a list of Counter(s) for each peptide sequence.
# (Call molecular_formula.calc_formula for each peptide sequence.)

# Add a column to dat containing the peptide formula
# (Call molecular_formula.format_formula for each peptide sequence and set the result
# to a new column in dat named 'formula'.)

# Add a column to dat containing the peptide mass
# (Call molecular_formula.calc_mass for each peptide sequence and set the result
# to a new column in dat named 'mass'.)

# Retrieve uniprot records for all protein IDs
# (Call uniprot.get_unipror_record for each protein ID and save the results to a dict)

# Iterate through dat

    # Check if there is a uniprot record for the current ID.

        # Get the protein sequence for the current row from the Record

        # Get the index locations of the modification(s) in the parent protein sequence.
        # (Call uniprot.get_modified_residue_numbers)

        # Get the GO terms for protein function
        # (Call uniprot.get_go_fxn)

        # Get the subcellular location of the parent protein
        # The subcellular location are stored in the Record.comments member

# Add a column to dat named 'modified_residues'

# Add a column to dat named 'go_fxn'

# Add a column to dat named 'subcelluar_loc'

# Write dat to OUTPUT_FILE_PATH (Call DataFrame.to_tsv)


# if __name__ == '__main__':
#     main()


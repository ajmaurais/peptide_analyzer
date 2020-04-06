
import re
from urllib.error import HTTPError
from biopython_lite.Bio import ExPASy, SwissProt

def get_unipror_record(uniprot_id):
    '''
    Retrieve a uniprot record.

    Parameters
    ----------
    uniprot_id: str
        A valid uniprot ID.

    Returns
    -------
    record: biopython_lite.Bio.SwissProt.Record
        A Record object with information from the UniProt entry.
        If no UniprotRecord can be found, returns None.
    '''

    # Call ExPASy.get_sprot_raw on uniprot_id and set the result to a variable
    # If ExPASy.get_sprot_raw fails, it raises a ValueError or HTTPError.
    # Your code should include a try, except statement to deal with that if it happens.

    # Call SwissProt.read to parse the text handle from ExPASy.get_sprot_raw and return the Record

    raise NotImplementedError('get_unipror_record not implemented.')


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
    modifications: str
        modifications in the format <residue><number>|...
    '''

    # Get peptide sequence without modifications

    # Find beginning index of peptide in parent protein

    # Iterate through modification sites on peptide and determine their position on
    # the parent protein.

    # Format the modification indecies as <residue><number>|...
    # Example: C53|C56 or C73

    raise NotImplementedError('get_modified_residue_numbers not implemented.')


def get_go_fxn(cross_references):
    '''
    Get the GO terms for protein function from the cross_references
    list from a SwissProt.Record.

    Parameters
    ----------
    cross_references: list of tuples
        cross_references list.

    Returns
    -------
    go_terms: str
        GO terms concatenated into a single string.
    '''

    # cross reference list elements with GO terms should start with 'GO'
    # GO terms for function start with 'F:'

    # Iterate through cross_references list elements

        # Find elements that start with 'GO'

            # Find GO terms that start with 'F:'

    # Concatenate terms into a single string separated by commas
    
    raise NotImplementedError('get_go_fxn not implemented.')


def remove_braces(s, open_brace='{', close_brace='}'):
    '''
    Remove substring(s) inside braces from string.

    Parameters
    ----------
    s: str
        String containing braces.
    open_brace: str, default '{'
        Open brace
    close_brace: str, default '{'
        Close brace

    Returns
    -------
    clean_s: str
        String with all text inside braces removed.

    Raises
    ------
    ValueError:
        If braces are not balanced.
    '''

    # Start with the inner most brace, and remove them recursively until there are none left.

    raise NotImplementedError('remove_braces not implemented.')


def get_protein_location(comments_list):
    '''
    Parse protein subcellular locations from Record comments.

    Parameters
    ----------
    comments_list: list
        List of comments from Record.

    Returns
    -------
    pretty_locations: str
        Nicely formatted, comma separated list of locations.
        If annotations are found, returns 'no_annotated_location'.
    '''

    # Find the comments_list element that starts with 'SUBCELLULAR LOCATION: '

    # remove everything after 'Note='

    # Remove everything in curly braces
    # (call remove_braces)

    # Remove everything in square brackets (isoform specifiers)
    # (call remove_braces)

    # split by delimiters ';.:,'
    # (call re.split with the regex r'\s?[;.:,]\s?')

    # convert to lowercase, remove duplicates, and concatenate into a single string separated by ';'

    raise NotImplementedError('get_protein_location not implemented.')


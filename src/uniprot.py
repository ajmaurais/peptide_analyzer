
import re
from urllib.error import HTTPError
from biopython_lite.Bio import ExPASy, SwissProt

def get_unipror_record(uniprot_id):
    '''
    Retreive a uniprot record.

    Paramaters
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
    try:
        handle = ExPASy.get_sprot_raw(uniprot_id)
    except (HTTPError, ValueError) as e:
        return None

    # Call SwissProt.read to parse the text handel from ExPASy.get_sprot_raw and return the Record
    record = SwissProt.read(handle)
    return record


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
    unmodified_seq = peptide_seq.replace('*', '')

    # Find beginning index of peptide in parent protein
    peptide_begin = protein_seq.find(unmodified_seq)

    # Iterate through modification sites on peptide and determine their position on
    # the parent protein.
    protein_sites = list()
    for i, m in enumerate(re.finditer(r'\*', peptide_seq)):
        peptide_site = (m.start() - i - 1)
        protein_sites.append(peptide_site + peptide_begin)

    # Format the modification indecies as <residue><number>|...
    # Example: C53|C56 or C73
    return '|'.join(['{}{}'.format(protein_seq[x], x + 1) for x in protein_sites])


def get_go_fxn(cross_references):
    '''
    Get the GO terms for protein function from the cross_references
    list from a SwissProt.Record.

    Paramaters
    ----------
    cross_references: list of tuples
        cross_references list.

    Returns
    -------
    go_terms: str
        GO terms concatenated into a single string.
    '''

    # cross refrence list elements with GO terms should start with 'GO'
    # GO terms for function start with 'F:'

    # Iterate through cross_references list elements
    terms = list()
    for ref in cross_references:
        # Find elements that start with 'GO'
        if ref[0] == 'GO':
            # Find GO terms that start with 'F:'
            if ref[2][0] == 'F':
                terms.append(ref[2][2:])

    # Concatenate terms into a single string seperated by commas
    return ', '.join(terms)


def remove_braces(s, open_brace='{', close_brace='}'):
    '''
    Remove substring(s) inside braces from string.

    Paramaters
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
        If braces are not balenced.
    '''

    # Start with the inner most brace, and remove them recursivally untill there are none left.
    open_brace_index = s.rfind(open_brace)
    close_brace_index = s.find(close_brace, open_brace_index)
    if open_brace_index == -1:
        if close_brace in s:
            raise ValueError('Non-matching braces in string: "{}"'.format(s))
        return s
    if close_brace_index == -1:
        raise ValueError('Non-matching braces in string: "{}"'.format(s))
    return remove_braces(s[0:open_brace_index] + s[close_brace_index + 1:],
                         open_brace=open_brace, close_brace=close_brace)


def get_protein_location(comments_list):
    '''
    Parse protein subcellular locations from Record comments.

    Paramaters
    ----------
    comments_list: list
        List of comments from Record.

    Returns
    -------
    pretty_locations: str
        Nicely formated, comma seperated list of locations.
        If annotations are found, returns 'no_annotated_location'.
    '''

    # Find the comments_list element that starts with 'SUBCELLULAR LOCATION: '
    sl_start = 'SUBCELLULAR LOCATION: '
    locations = None
    for c in comments_list:
        if c.startswith(sl_start):
            locations = c[len(sl_start):]
            break

    if locations is None:
        return 'no_annotated_location'

    # remove everything after 'Note='
    note_index = locations.find('Note=')
    if note_index != -1:
        locations = locations[0:note_index]

    # Rmove everthing in curly braces
    # (call remove_braces)
    locations = remove_braces(locations)

    # Rmove everthing in square brackets (isoform specifers)
    # (call remove_braces)
    locations = remove_braces(locations, open_brace='[', close_brace=']')

    # split by deliminators ';.:,'
    # (call re.split with the regex r'\s?[;.:,]\s?')
    locations = re.split(r'\s?[;.:,]\s?', locations)

    # convert to lowercase, remove duplicates, and concatenate into a single string seperated by ';'
    locations = ', '.join(set(l.strip().lower() for l in locations if l.strip() != ''))

    return locations



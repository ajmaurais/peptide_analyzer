
import sys
import argparse

from .dataframe import DataFrame

def read_input(fname):
    '''
    Read input file.'

    Paramarers
    ----------
    fname: str
        Path to input file.

    Returns
    -------

    '''
    return 


def main():
    '''
    Main method.

    This is the function which will be run first when you call the program form the command line.
    '''

    parser = argparse.ArgumentParser(prog=__file__,
                                     description='Read a .tsv file containing peptides and uniprot '
                                     ' IDs and do some analysis on them.')

    parser.add_argument('input_file',
                        help='Path to input file. Should be tsv with two columns; "ID" and "seq".')

    args = parser.parse_args()

    dat = read_input(args.input_file)


if __name__ == '__main__':
    main()

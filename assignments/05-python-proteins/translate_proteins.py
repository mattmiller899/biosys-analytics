#!/usr/bin/env python3
"""
Author : mattmiller899
Date   : 2019-02-12
Purpose: Rock the Casbah
"""

import argparse
import sys
import os

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='str', help='DNA/RNA sequence')

    parser.add_argument(
        '-c',
        '--codons',
        help='A file with codon translations',
        metavar='str',
        type=str,
        required=True)

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output filename',
        metavar='str',
        type=str,
        default="out.txt")

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    codon_file = args.codons
    out_file = args.outfile
    pos_arg = args.positional

    if not os.path.isfile(codon_file):
        print("--codons \"{}\" is not a file".format(codon_file))
        exit(1)

    codon_dict = {}
    with open(codon_file, 'r') as f:
        for l in f:
            larr = l.split()
            codon_dict[larr[0].upper()] = larr[1]
    pos_len = len(pos_arg) + 1
    with open(out_file, 'w') as out:
        for i in range(0, pos_len, 3):
            if i + 3 < pos_len:
                try:
                    tmp = codon_dict[pos_arg[i:i+3].upper()]
                except:
                    tmp = '-'
                out.write(tmp)
            

    print("Output written to \"{}\"".format(out_file))

# --------------------------------------------------
if __name__ == '__main__':
    main()

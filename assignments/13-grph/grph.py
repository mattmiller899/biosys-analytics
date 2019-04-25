#!/usr/bin/env python3

import argparse
import sys
import os
from Bio import SeqIO

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Graph through sequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional',
        metavar='str',
        help='A positional argument')


    parser.add_argument(
        '-k',
        '--int',
        help='K size of overlap',
        metavar='int',
        type=int,
        default=3)

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

def find_kmers(find_seq, k):
    kmers = []
    for i in range(len(find_seq) - k + 1):
        kmers.append(find_seq[i:i+k])
    return(kmers)


def main():
    args = get_args()
    kmer = args.int
    input_file = args.positional
    if kmer < 1:
        print(f'-k \"{kmer}\" must be a positive integer')
        exit(1)
    if input_file is None or not os.path.isfile(input_file):
        print(f'\"{input_file}\" is not a file')
        exit(1)
    for_kmers = {}
    rev_kmers = {}
    for record in SeqIO.parse(input_file, 'fasta'):
        for_kmers[record.id] = record.seq[:kmer]
        rev_kmers[record.id] = record.seq[len(record.seq) - kmer:]
    for fkey, fval in for_kmers.items():
        for rkey, rval in rev_kmers.items():
            if fkey != rkey and fval == rval:
                print(f"{rkey} {fkey}")


# --------------------------------------------------
if __name__ == '__main__':
    main()

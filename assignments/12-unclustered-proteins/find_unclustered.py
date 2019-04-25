#!/usr/bin/env python3
"""
Author : mattmiller899
Date   : 2019-04-18
Purpose: Rock the Casbah
"""

import argparse
import sys
import re
import os
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-c',
        '--cdhit',
        help='Output file from CD-HIT (clustered proteins)',
        metavar='str',
        type=str,
        required=True)

    parser.add_argument(
        '-p',
        '--proteins',
        help='Proteins FASTA',
        metavar='str',
        type=str,
        required=True)

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='str',
        type=str,
        default='unclustered.fa')

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

    cd_arg = args.cdhit
    prot_arg = args.proteins
    out_arg = args.outfile

    if not os.path.isfile(prot_arg):
        print("--proteins \"{}\" is not a file".format(prot_arg))
        exit(1)
    if not os.path.isfile(cd_arg):
        print("--cdhit \"{}\" is not a file".format(cd_arg))
        exit(1)
    clustered_prots = []
    with open(cd_arg, 'r') as f:
        comp1 = re.compile(">gi\|(?P<id_num>\d+)\|")
        for l in f:
            s1 = re.search(comp1, l)
            if s1:
                id_num = s1.group("id_num")
                #print("first id num = {}".format(id_num))
                clustered_prots.append(id_num)
    out = open(out_arg, 'w')
    num_unclustered = 0
    num_total = 0
    clustered_prots = set(clustered_prots)
    with open(prot_arg, 'r') as f:
        for record in SeqIO.parse(f, 'fasta'):
            id_name = re.sub('\|.*', '', record.id)
            #print("id name = {}".format(id_name))
            num_total += 1
            if id_name not in clustered_prots:
                SeqIO.write(record, out, 'fasta')
                num_unclustered += 1
    print("Wrote {:,} of {:,} unclustered proteins to \"{}\"".format(num_unclustered, num_total, out_arg))
    out.close()
# --------------------------------------------------
if __name__ == '__main__':
    main()

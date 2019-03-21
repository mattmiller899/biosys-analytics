#!/usr/bin/env python3
"""
Author : mattmiller899
Date   : 2019-03-14
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Filter Swissprot file for keywords, taxa',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='FILE', help='Uniprot file')

    parser.add_argument(
        '-s',
        '--skip',
        help='Skip taxa',
        metavar='STR',
        type=str,
        nargs='+',
        default='')

    parser.add_argument(
        '-k',
        '--keyword',
        help='Take on keyword',
        metavar='STR',
        type=str,
        required=True)
    
    parser.add_argument(
        '-o',
        '--output',
        help='Output filename',
        metavar='FILE',
        type=str,
        default="out.fa")

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
    swiss_fp = args.positional
    skips = set([i.lower() for i in args.skip])
    #print("skips = {}".format(skips))
    keyword = set([args.keyword])
    #print("keyword = {}".format(keyword))
    #exit()
    #skips = set(str(args.skip))
    #keyword = set(args.keyword)
    out_fp = args.output

    #print('swiss_fp = "{}"'.format(swiss_fp))
    #print('skips = "{}"'.format(str(skips)))
    #print('keyword = "{}"'.format(keyword))
    #print('out_fp = "{}"'.format(out_fp))
    
    if not os.path.isfile(swiss_fp):
        print("\"{}\" is not a file".format(swiss_fp))
        exit(1)
    out = open(out_fp, 'w')
    num_skipped = 0
    num_accepted = 0
    for rec in SeqIO.parse(swiss_fp, "swiss"):
        annots = rec.annotations
        if "keywords" in annots:
            annot_kws = set([i.lower() for i in annots['keywords']])
            annot_taxa = set([i.lower() for i in annots['taxonomy']])
            #print("annot_kws = {}".format(annot_kws))
            #print("annot_taxa = {}".format(annot_taxa))
            #print("keyword = {}".format(keyword))
            #print("skips = {}".format(skips))
            if keyword.intersection(annot_kws) and not skips.intersection(annot_taxa):
                SeqIO.write(rec, out, "fasta")
                num_accepted += 1
            else:
                num_skipped += 1
    print("Done, skipped {} and took {}. See output in \"{}\".".format(num_skipped, num_accepted, out_fp))
    out.close()

# --------------------------------------------------
if __name__ == '__main__':
    main()

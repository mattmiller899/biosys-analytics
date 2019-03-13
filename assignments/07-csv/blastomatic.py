#!/usr/bin/env python3
"""
Author : mattmiller899
Date   : 2019-03-13
Purpose: Rock the Casbah
"""

import argparse
import sys
import os

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Annotate BLAST output',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='FILE', help='BLAST output (-outfmt 6)')

    parser.add_argument(
        '-a',
        '--annotations',
        help='Annotation file',
        metavar='FILE',
        type=str,
        default='',
        required=True)

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='FILE',
        type=str,
        default='',
        required=False)

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
    annot_fp = args.annotations
    out_fp = args.outfile
    blast_fp = args.positional

    #print('output_arg = "{}"'.format(out_fp))
    #print('annotation_arg = "{}"'.format(annot_fp))
    #print('blast_fp = "{}"'.format(blast_fp))

    if not os.path.isfile(annot_fp):
        print("\"{}\" is not a file".format(annot_fp))
        exit(1)
    if not os.path.isfile(blast_fp):
        print("\"{}\" is not a file".format(blast_fp))
        exit(1)

    #Load the annotations
    annots_dict = {}
    with open(annot_fp, 'r') as f:
        for l in f:
            larr = l[:-1].split(",")
            annots_dict[larr[0]] = larr[6:]

    header_str = "seq_id\tpident\tgenus\tspecies"
    if out_fp != "":
        out = open(out_fp, 'w')
        out.write("{}\n".format(header_str))
    else:
        print(header_str)

    with open(blast_fp, 'r') as f:
        for l in f:
            larr = l.split("\t")
            seq_id = larr[1]
            tax_info = annots_dict.get(seq_id, ["BAD", "BAD"])
            if tax_info[0] == "BAD":
                warn(msg="Cannot find seq {} in lookup".format(seq_id))
                continue
            genus = tax_info[0]
            species = tax_info[1]
            if genus == "":
                genus = "NA"
            if species == "":
                species = "NA"
            if out_fp == "":
                print("{}\t{}\t{}\t{}".format(seq_id, larr[2], genus, species))
            else:
                out.write("{}\t{}\t{}\t{}\n".format(seq_id, larr[2], genus, species))

    if out_fp != "":
        out.close()
# --------------------------------------------------
if __name__ == '__main__':
    main()

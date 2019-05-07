#!/usr/bin/env python3
"""
Author : mattmiller899
Date   : 2019-05-07
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import re

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Convert to Pig Latin',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='str', nargs='+', help='Input file(s)')

    parser.add_argument(
        '-o',
        '--outdir',
        help='Output directory',
        metavar='str',
        type=str,
        default='out-yay')

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

    outdir = args.outdir
    fps = args.positional
    vowels = 'aeiou'
    nums = '1234567890'
    #consts = ['ch', 'wh', 'th', 'kn', 'fr', 'dr', 'cr', 'st', 'sc', 'sh', 'tr', 'pr', 'br']
    if not os.path.isdir(outdir):
        os.makedirs(outdir)

    counter = 0
    for f in fps:
        if not os.path.isfile(f):
            print(f"\"{f}\" is not a file.")
            continue
        file_name = os.path.basename(f)
        counter += 1
        print(f"{counter}: {file_name}")
        with open(f"{outdir}/{file_name}", "w") as out_fh:
            with open(f"{f}", "r") as in_fh:
                for l in in_fh:
                    l = re.sub('[^–\-\'\s\w\d]', '', l)
                    l = re.sub('(?<=\w)-(?=\w)', '', l)
                    words = l.split()
                    for word in words:
                        if word[0].lower() in vowels or word[0].lower() in nums:
                            out_fh.write(f"{word}-yay ")
                        elif word == '–' or word == '--':
                            out_fh.write("-yay ")
                        else:
                            curr_char = word[0]
                            char_count = 0
                            while curr_char not in vowels and char_count < len(word) - 1:
                                char_count += 1
                                curr_char = word[char_count]
                            out_fh.write(f"{word[char_count:]}-{word[:char_count]}ay ")
                        #elif word[:2].lower() in consts:    
                        #    out_fh.write(f"{word[2:]}-{word[:2]}ay ")
                        #else:
                        #    out_fh.write(f"{word[1:]}-{word[0]}ay ")
                    out_fh.write("\n")
    plural = "s" if counter != 1 else ""
    print(f"Done, wrote {counter} file{plural} to \"{outdir}\".")

# --------------------------------------------------
if __name__ == '__main__':
    main()

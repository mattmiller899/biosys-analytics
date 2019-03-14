#!/usr/bin/env python3
"""
Author : mattmiller899
Date   : 2019-03-14
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-n',
        '--num_bottles',
        help='',
        metavar='INT',
        type=int,
        default=10)

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
    num_bottles = args.num_bottles

    if num_bottles < 1:
        die("N {} must be a positive integer".format(num_bottles))
    
    for i in reversed(range(1, num_bottles+1)):
        print_str = "{} bottle{} of beer on the wall,\n{} bottle{} of beer,\nTake one down, pass it around,\n\
{} bottle{} of beer on the wall!".format(i, "s" if i != 1 else "", i, "s" if i != 1 else "", i-1, "s" if i-1 != 1 else "")
        print(print_str)
        if i != 1:
            print()

# --------------------------------------------------
if __name__ == '__main__':
    main()

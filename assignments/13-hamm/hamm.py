#!/usr/bin/env python3
"""
Author : mattmiller899
Date   : 2019-4-25
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import logging

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Hamming distance',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'files', metavar='FILE', help='File inputs', nargs=2)


    parser.add_argument(
        '-d', '--debug', help='Debug', action='store_true')

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
def dist(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    dist_size = abs(len1 - len2)
    min_len = len1 if len1 < len2 else len2
    for i in range(min_len):
        if s1[i] != s2[i]:
            dist_size += 1
    
    logging.debug('s1 = {} s2 = {} d = {}'.format(s1, s2, dist_size))
    return dist_size

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    debugging = args.debug
    f1, f2 = args.files

    logging.basicConfig(
        filename='.log',
        filemode='w',
        level=logging.DEBUG if args.debug else logging.CRITICAL
        )

    if f1 is None or not os.path.isfile(f1):
        print(f'\"{f1}\" is not a file')
        exit(1)
    if f2 is None or not os.path.isfile(f2):
        print(f'\"{f2}\" is not a file')
        exit(1)

    logging.debug('file1 = {}, file1 = {}'.format(f1,f2))

    in1 = open(f1, 'r').read().split()
    in2 = open(f2, 'r').read().split()

    dist_sum = 0
    for i in range(len(in1)):
        dist_sum += dist(in1[i], in2[i])
    print(dist_sum)

if __name__ == '__main__':
    main()

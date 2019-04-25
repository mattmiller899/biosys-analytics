#!/usr/bin/env python3
"""
Author : mattmiller899
Date   : 2019-04-23
Purpose: Rock the Casbah
"""

import argparse
import sys
import re
from collections import defaultdict
import os

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Print word frequencies',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='FILE', help='File input(s)',nargs='+', type=argparse.FileType('r', encoding='UTF-8'))

    parser.add_argument(
        '-s',
        '--sort',
        help='Sort by word or frequency',
        metavar='str',
        type=str,
        default='word')

    parser.add_argument(
        '-m',
        '--min',
        help='Minimum count',
        metavar='int',
        type=int,
        default=0)

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
    sort_type = args.sort
    min_count = args.min
    files = args.positional

    if sort_type != 'word' and sort_type != 'frequency':
        print(f"bad sort type {sort_type}")
        exit(1)
    #for f in files:
    #    if not os.path.isfile(f):
    #        print(f"\"{f}\" is not a file")
    #        exit(1)
    if min_count < 0:
        print("bad min")
        exit(1)

    found_words = defaultdict(int)
    for f in files:
    #    with open(fp, 'r') as f:
        words = f.read().split()
        words = [re.sub('[^a-zA-Z0-9]', '', word).lower() for word in words]
        for word in words:
            found_words[word] += 1

    if sort_type == 'frequency':
        sorted_words = sorted([(count, word) for word, count in found_words.items() if count >= min_count and word is not ''])
        for (count, word) in sorted_words:
            #print('{:20} {}'.format(word, count))
            print(f'{word:20} {count}')
            #print('{:20} {}'.format(count, word))

    else:
        sorted_words = sorted([(word, count) for word, count in found_words.items() if count >= min_count and word is not ''])
        for (word, count) in sorted_words:
            print(f'{word:20} {count}')
            #print('{:20} {}'.format(word, count))
            #print('{} {:20}'.format(word, count))


# --------------------------------------------------
if __name__ == '__main__':
    main()

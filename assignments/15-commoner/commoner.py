#!/usr/bin/env python3
"""
Author : mattmiller899
Date   : 2019-04-29
Purpose: Rock the Casbah
"""

import argparse
import sys
import itertools
import os
from tabulate import tabulate
import logging
import re
import io
from collections.abc import Iterable

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='FILE', nargs='+', help='Input files', type=argparse.FileType('r', encoding='UTF-8'))

    parser.add_argument(
        '-m',
        '--min_len',
        help='Minimum length of words',
        metavar='int',
        type=int,
        default=0)

    parser.add_argument(
        '-n',
        '--hamming_distance',
        help='Allowed Hamming distance',
        metavar='int',
        type=int,
        default=0)

    parser.add_argument(
        '-l',
        '--logfile',
        help='Logfile name',
        metavar='str',
        type=str,
        default='.log')

    parser.add_argument(
        '-d', '--debug', help='Debug', action='store_true')

    parser.add_argument(
        '-t', '--table', help='Table output', action='store_true')

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

def test_dist():
    """dist ok"""

    tests = [('foo', 'boo', 1), ('foo', 'faa', 2), ('foo', 'foobar', 3),
             ('TAGGGCAATCATCCGAG', 'ACCGTCAGTAATGCTAC',
              9), ('TAGGGCAATCATCCGG', 'ACCGTCAGTAATGCTAC', 10)]

    for s1, s2, n in tests:
        d = dist(s1, s2)
        assert d == n


def uniq_words(f, min_len):
    if isinstance(f, Iterable):
        fh = f
    else:
        if not os.path.isfile(f):
            print(f"\"{f}\" is not a file")
            exit(1)
        else:
            fh = f

    words = fh.read().split()
    words = [re.sub('[^a-zA-Z0-9]', '', word).lower() for word in words]
    good_words = []
    for w in words:
        if len(w) >= min_len and w not in good_words:
            good_words.append(w)
    return set(good_words)

    
def test_uniq_words():
    """Test uniq_words"""

    s1 = '?foo, "bar", FOO: $fa,'
    s2 = '%Apple.; -Pear. ;bANAna!!!'

    assert uniq_words(io.StringIO(s1), 0) == set(['foo', 'bar', 'fa'])

    assert uniq_words(io.StringIO(s1), 3) == set(['foo', 'bar'])

    assert uniq_words(io.StringIO(s2), 0) == set(['apple', 'pear', 'banana'])

    assert uniq_words(io.StringIO(s2), 4) == set(['apple', 'pear', 'banana'])

    assert uniq_words(io.StringIO(s2), 5) == set(['apple', 'banana'])
    

def common(words1, words2, distance):
    good_words = []
    for i in itertools.product(words1, words2):
        tmp_dist = dist(i[0], i[1])
        if tmp_dist <= distance:
            good_words.append((i[0], i[1], tmp_dist))
    return sorted(good_words)


def test_common():
    w1 = ['foo', 'bar', 'quux']
    w2 = ['bar', 'baz', 'faa']

    assert common(w1, w2, 0) == [('bar', 'bar', 0)]

    assert common(w1, w2, 1) == [('bar', 'bar', 0), ('bar', 'baz', 1)]

    assert common(w1, w2, 2) == [('bar', 'bar', 0), ('bar', 'baz', 1),
                                 ('bar', 'faa', 2), ('foo', 'faa', 2)]


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    debug = args.debug
    min_len = args.min_len
    ham = args.hamming_distance
    logfile = args.logfile
    table = args.table
    f1, f2 = args.positional
   
    logging.basicConfig(
        filename=logfile,
        filemode='w',
        level=logging.DEBUG if args.debug else logging.CRITICAL
    )
 
    if ham < 0:
        print(f"--distance \"{ham}\" must be > 0")
        exit(1)

    logging.debug('file1 = {}, file1 = {}'.format(f1,f2))

    words1 = uniq_words(f1, min_len)
    words2 = uniq_words(f2, min_len)   
 
    common_words = common(words1, words2, ham)

    if len(common_words) == 0:
        print("No words in common.")
    elif table:
        print(tabulate(common_words, ['word1', 'word2', 'distance'], tablefmt='psql'))
    else:
        print("word1\tword2\tdistance")
        for (w1, w2, d) in common_words:
            #print(f"{w1:20}{w2:20}{d}")
            print(f"{w1}\t{w2}\t{d}")

# --------------------------------------------------
if __name__ == '__main__':
    main()

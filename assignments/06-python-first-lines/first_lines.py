#!/usr/bin/env python3
"""
Author : mattmiller899
Date   : 2019-02-26
Purpose: Rock the Casbah
"""

import argparse
import sys
import os

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='DIR', help='A positional argument', nargs='+')

    parser.add_argument(
        '-w',
        '--width',
        help='A named string argument',
        metavar='int',
        type=int,
        default=50)

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
    width_arg = args.width
    pos_arg = args.positional

    for d in pos_arg:
        if not os.path.isdir(d):
            print('"{}" is not a directory'.format(d), file=sys.stderr)
        else:
            print(d)
            file_list = os.listdir(d)
            lines = []
            for f in file_list:
                file_path = os.path.join(d, f)
                with open(file_path, 'r') as input_file:
                    lines.append((input_file.readline().rstrip(), f))
            sorted_lines = sorted(lines)
            for tup in sorted_lines:
                num_dots = width_arg - len(str(tup[0])) - len(str(tup[1]))
                dots_str = "".join(['.' for x in range(num_dots)])
                print("{} {} {}".format(tup[0], dots_str, tup[1]))


# --------------------------------------------------
if __name__ == '__main__':
    main()

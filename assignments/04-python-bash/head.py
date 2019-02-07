#!/usr/bin/env python3
"""
Author : mattmiller899
Date   : 2019-02-07
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) == 0 or len(args) > 2:
        print('Usage: {} FILE [NUM_LINES]'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    file_fp = args[0]
    if not os.path.isfile(file_fp):
        print("{} is not a file".format(file_fp))
        sys.exit(1)
    num_lines = 3
    if len(args) == 2:
        num_lines = int(args[1])
    if num_lines < 1:
        print("lines ({}) must be a positive number".format(num_lines))
        sys.exit(1)
    lc = 0
    with open(file_fp, 'r') as f:
        for l in f:
            if lc < num_lines:
                print(l[:-1])
                lc = lc + 1
            else:
                break


# --------------------------------------------------
main()

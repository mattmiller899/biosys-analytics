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

    if len(args) != 1:
        print('Usage: {} FILE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)
    file_fp = args[0]
    if not os.path.isfile(file_fp):
        print("{} is not a file".format(file_fp))
        sys.exit(1)

    lc = 1
    with open(file_fp, 'r') as f:
        for l in f:
            print("{:3}: {}".format(lc,
                                    l[:-1]))
            lc =  lc + 1
# --------------------------------------------------
main()

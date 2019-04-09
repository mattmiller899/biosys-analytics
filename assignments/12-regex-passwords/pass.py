#!/usr/bin/env python3
"""
Author : mattmiller899
Date   : 2019-04-08
Purpose: Rock the Casbah
"""

import os
import sys
import re

# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 2:
        print('Usage: {} PASSWORD ALT'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    password = args[0].upper()
    alt = args[1].upper()

    alt_passwords = [password, ".{}.".format(password), ".{}".format(password), "{}.".format(password)]
    for i in range(len(alt_passwords)):
        m = re.match(alt_passwords[i], alt)
        if m:
            print("ok")
            exit()
    print("nah")
        

# --------------------------------------------------
main()

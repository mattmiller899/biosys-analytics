#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
    print("Usage: hello.py NAME [NAME2 ...]")
    exit(1)
else:
    num_people = len(sys.argv) - 1
    print_str = "Hello to the %d of you: " % num_people
    if num_people == 1:
        print_str += "%s!" % sys.argv[1]
    elif num_people == 2:
        print_str += "%s and %s!" % (sys.argv[1], sys.argv[2])
    else:
        for i, name in enumerate(sys.argv[1:]):
            if i == num_people - 1:
                print_str += "and %s!" % name
            else:
                print_str += "%s, " % name
print(print_str)

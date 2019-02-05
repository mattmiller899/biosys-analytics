#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("Usage: grid.py NUM")
    exit(1)
num = int(sys.argv[1])
if num < 2 or num > 9:
    print("NUM ({}) must be between 1 and 9".format(num))
    exit(1)
print_str = ""
curr_num = 1
for i in range(num):
    #print_str = "{}{}".format(
    #                        print_str,
    #                        "  " if curr_num < 9 else " ")
    for j in range(1, num+1):
        print("{:3}".format(j+i*num), end='')
    print()
    """
    curr_num = j+(i*num)
    split_char = ""
    if j == num:
        split_char = "\n"
    elif curr_num < 9:
        split_char = "  "
    else:
        split_char = " "
    print_str = "{}{}{}".format(
                                print_str,
                                curr_num,
                                split_char)
    """
    #print_str = "{}\n".format(print_str)
#print(print_str[:-1])

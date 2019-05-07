#!/usr/bin/env python3
"""
Author : mattmiller899
Date   : 2019-02-14
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} STATE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    state_arg = args[0]

    #Check arg
    allowed_state = set('.XO')
    if len(state_arg) != 9 or not set(state_arg) <= allowed_state:
        print("State \"{}\" must be 9 characters of only ., X, O".format(state_arg))
        sys.exit(1) 

    #Create board
    state_arr = []
    num_entries = 0
    for i in range(1, 10):
        if state_arg[i - 1] == '-' or state_arg[i - 1] == '.':
            state_arr.append(i)
        else:
            state_arr.append(state_arg[i - 1])
            num_entries = num_entries + 1
    
    #Check for winner
    if num_entries < 3:
        print("No winner")
        exit()
    winning_states = [[0,1,2], [0,3,6], [0,4,8], [1,4,7], [2,4,6], [2,5,8], [3,4,5], [6,7,8]]
    for winner_state in winning_states:
        if state_arr[winner_state[0]] == state_arr[winner_state[1]] and state_arr[winner_state[2]] == state_arr[winner_state[0]]:
            print("{} has won".format(state_arr[winner_state[0]]))
            exit()
    print("No winner")
            

# --------------------------------------------------
main()

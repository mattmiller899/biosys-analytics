#!/usr/bin/env python3
"""
Author : mattmiller899
Date   : 2019-02-07
Purpose: Rock the Casbah
"""

import argparse
import sys
import string

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Tic-Tac-Toe board',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s',
        '--state',
        help='Board state',
        metavar='str',
        type=str,
        default='---------')

    parser.add_argument(
        '-p',
        '--player',
        help='Player',
        metavar='str',
        type=str,
        default='')

    parser.add_argument(
        '-c',
        '--cell',
        help='Cell to apply -p',
        metavar='int',
        type=int)

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
    cell_arg = args.cell
    player_arg = args.player
    state_arg = args.state
    
    #Check all args
    allowed_state = set('.XO')
    allowed_player = set("XO")
    if state_arg != "---------" and (len(state_arg) != 9 or not set(state_arg) <= allowed_state):
        print("Invalid state \"{}\", must be 9 characters of only -, X, O".format(state_arg))
        sys.exit(1)
    if player_arg != "" and not set(player_arg) <= allowed_player:
        print("Invalid player \"{}\", must be X or O".format(player_arg))
        sys.exit(1)
    if cell_arg != None and (cell_arg < 1 or cell_arg > 9):
        print("Invalid cell \"{}\", must be 1-9".format(cell_arg))
        sys.exit(1)
    player_bool = bool(player_arg == "")
    cell_bool = bool(cell_arg == None)
    if player_bool != cell_bool:
        print("Must provide both --player and --cell")
        sys.exit(1)
    
    #Create board
    state_arr = []
    for i in range(1, 10):
        if state_arg[i - 1] == '-' or state_arg[i - 1] == '.':
            state_arr.append(i)
        else:
            state_arr.append(state_arg[i - 1])
    #Edit board
    if cell_arg != None:
        if str(state_arr[cell_arg - 1]) not in "XO":
            state_arr[cell_arg - 1] = player_arg
        else:
            print("Cell {} already taken".format(cell_arg))
            sys.exit()
    print("-------------")
    for i in range(1, 10):
        print("| {} ".format(state_arr[i - 1]),end="")
        if i % 3 == 0:
            print("|\n-------------")
     

# --------------------------------------------------
if __name__ == '__main__':
    main()

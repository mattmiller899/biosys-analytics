#!/usr/bin/env python3
"""
Author : mattmiller899
Date   : 2019-03-26
Purpose: Rock the Casbah
"""

import argparse
import sys
import itertools
import random

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='\"War\" cardgame',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s',
        '--seed',
        help='Random seed',
        metavar='int',
        type=int,
        default=None)

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
    seed = args.seed
    
    random.seed(seed)
    vals = ["{}".format(i) for i in range(2,11)]
    vals.extend(['J', 'Q', 'K', 'A'])
    suits = ['♥', '♠', '♣', '♦']
    #cards = sorted(["{}{}".format(i, j) for (i, j) in itertools.product(suits, vals)])
    cards = sorted(list(itertools.product(suits, vals)))
    #print(cards)
    random.shuffle(cards)
    card_vals = dict([(str(i), int(i)) for i in range(2,11)])
    card_vals.update({'J': 11, 'Q': 12, 'K': 13, 'A': 14})
    #print(card_vals)
    wins = [0,0]
    for i in range(26):
        p1card = cards.pop()
        p2card = cards.pop()
        p1suit = p1card[0]
        p1val = p1card[1]
        p2suit = p2card[0]
        p2val = p2card[1]
        if card_vals[p1val] > card_vals[p2val]:
            wins[0] += 1
            winner = "P1"
        elif card_vals[p1val] < card_vals[p2val]:
            wins[1] += 1
            winner = "P2"
        else:
            winner = "WAR!"
        p1str = p1suit + p1val
        p2str = p2suit + p2val
        print("{} {} {}".format(p1str.rjust(3), p2str.rjust(3), winner))  
    if wins[0] > wins[1]:
        winner = "Player 1 wins"
    elif wins[0] < wins[1]:
        winner = "Player 2 wins"
    else:
        winner = "DRAW"
    print("P1 {} P2 {}: {}".format(wins[0], wins[1], winner))

# --------------------------------------------------
if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Author : mattmiller899
Date   : 2019-03-27
Purpose: Rock the Casbah
"""

import argparse
import sys
import random
import itertools

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s',
        '--seed',
        help='Random seed',
        metavar='int',
        type=int,
        default=None)

    parser.add_argument(
        '-p', '--player_hits', help='A boolean flag', action='store_true')
    
    parser.add_argument(
        '-d', '--dealer_hits', help='A boolean flag', action='store_true')

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
    player_hits = args.player_hits
    dealer_hits = args.dealer_hits

    random.seed(seed)
    vals = ["{}".format(i) for i in range(2,11)]
    vals.extend(['J', 'Q', 'K', 'A'])
    suits = ['♥', '♠', '♣', '♦']
    cards = sorted(list(itertools.product(suits, vals)))
    random.shuffle(cards)
    card_vals = dict([(str(i), int(i)) for i in range(2,11)])
    card_vals.update({'J': 10, 'Q': 10, 'K': 10, 'A': 1})

    player_cards = []
    dealer_cards = []

    for i in range(2):
        player_cards.append(cards.pop())
        dealer_cards.append(cards.pop())
    if player_hits:
        player_cards.append(cards.pop())
    if dealer_hits:
        dealer_cards.append(cards.pop())
    
    player_sum = 0
    player_hand = ""
    for tmp_card in player_cards:
        player_sum += card_vals[tmp_card[1]]
        card_str = tmp_card[0] + tmp_card[1]
        card_str = card_str + ' '
        player_hand += card_str
    player_hand = player_hand[:-1]     

    dealer_sum = 0
    dealer_hand = ""
    for tmp_card in dealer_cards:
        dealer_sum += card_vals[tmp_card[1]]
        card_str = tmp_card[0] + tmp_card[1]
        card_str = card_str + ' '
        dealer_hand += card_str
    dealer_hand = dealer_hand[:-1]

    print("D [{}]: {}\nP [{}]: {}".format(str(dealer_sum).rjust(2), dealer_hand, str(player_sum).rjust(2), player_hand,))
    if player_sum > 21:
        print("Player busts! You lose, loser!")
        exit(0)
    if dealer_sum > 21:
        print("Dealer busts.")
        exit(0)
    if player_sum == 21:
        print("Player wins. You probably cheated.")
        exit(0)
    if dealer_sum == 21:
        print("Dealer wins!")
        exit(0)
    if dealer_sum < 18:
        print("Dealer should hit.")
    if player_sum < 18:
        print("Player should hit.")

# --------------------------------------------------
if __name__ == '__main__':
    main()

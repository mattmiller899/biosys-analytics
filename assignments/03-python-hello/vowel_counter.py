#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
    print("Usage: vowel_counter.py STRING")
    exit(1)
vowels = "aeiouAEIOU"
word = sys.argv[1]

vowel_count = 0
for character in word:
    if character in vowels:
        vowel_count += 1
if vowel_count == 1:
    print("There is 1 vowel in \"%s.\"" % word)
else:
    print("There are %d vowels in \"%s.\"" % (vowel_count, word))

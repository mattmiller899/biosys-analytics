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

    if len(args) != 1:
        print('Usage: {} DATE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    arg = args[0]

    comp1 = re.compile("(?P<year>\d{4})[-]?(?P<month>\d{,2})[-]?(?P<day>\d{,2})")
    comp2 = re.compile("(?P<month>\d{1,2})/(?P<year>\d{1,2})")
    comp3 = re.compile("(?P<month>\w+)[-,][\s]?(?P<year>\d{4})")

    m1 = re.match(comp1, arg)
    m2 = re.match(comp2, arg)
    m3 = re.match(comp3, arg)

    if m1:
        year = m1.group('year')
        month = m1.group('month')
        day = m1.group('day')
        if month == "":
            print("No match")
            exit()
        if len(day) == 0:
            day = "01"
        print("{}-{:02d}-{:02d}".format(year, int(month), int(day)))
        exit()
    if m2:
        year = m2.group('year')
        month = m2.group('month')
        print('20{:02d}-{:02d}-01'.format(int(year), int(month)))
        exit()
    if m3:
        year = m3.group("year")
        str_month = m3.group("month")
        short_months = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()
        long_months = ('January February March April May June July August '
                        'September October November December').split()
        if str_month in short_months:
            d = dict(map(reversed, enumerate(short_months, 1)))
            month = d[str_month]
            print('{}-{:02d}-01'.format(year, month))    
            exit()
        elif str_month in long_months:
            d = dict(map(reversed, enumerate(long_months, 1)))
            month = d[str_month]
            print('{}-{:02d}-01'.format(year, month))
            exit()
    print("No match") 
        


# --------------------------------------------------
main()

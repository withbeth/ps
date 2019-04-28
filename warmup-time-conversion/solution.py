#!/bin/python
# refer : https://www.hackerrank.com/challenges/time-conversion/problem
from __future__ import print_function


# Input : hh:mm:ssAM or hh:mm:ssPM
# Output : Convert and print in 24 hr format where 00< hh < 23
def timeConversion(s):
    return get_24hh(s.split(":")[0], s[-2:]) \
           + ":" \
           + s[3:5] \
           + ":" \
           + s[6:8]


def get_24hh(hh12, am_or_pm):
    if am_or_pm == 'AM':
        return parse_am(hh12)
    return parse_pm(hh12)


def parse_am(hh12):
    if hh12 == '12':
        return '00'
    return hh12


def parse_pm(hh12):
    if hh12 == '12':
        return hh12
    return str(int(hh12) + 12)


if __name__ == '__main__':

    s = raw_input()
    print (timeConversion(s))


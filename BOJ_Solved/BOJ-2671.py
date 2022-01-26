"""
백준 2671번 : 잠수함 식별
"""

import re

string = input()
pattern = re.compile('(100+1+|01)+')

if pattern.fullmatch(string):
    print('SUBMARINE')
else:
    print('NOISE')
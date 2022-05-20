"""
백준 20673번 : Covid-19
"""

p = int(input())
q = int(input())

if q > 30:
    print('Red')
elif p <= 50 and q <= 10:
    print('White')
else:
    print('Yellow')

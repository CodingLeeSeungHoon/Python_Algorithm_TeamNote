"""
백준 14490번 : 백대열
"""
import math
a, b = map(int, input().split(':'))
divider = math.gcd(a, b)
print("{}:{}".format(a//divider, b//divider))
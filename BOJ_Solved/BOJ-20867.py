"""
백준 20867번 : Rulltrappa
"""

M, S, G = map(int, input().split())
A, B = map(float, input().split())
L, R = map(int, input().split())

if (M / S + R / B) > (M / G + L / A):
    print('friskus')
else:
    print('latmask')
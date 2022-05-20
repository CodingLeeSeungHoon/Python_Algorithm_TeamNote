"""
백준 13623번 : Zero or One
"""

a, b, c = map(int, input().split())
if a != b and b == c:
    print('A')
elif b!=a and a == c:
    print('B')
elif c != a and a == b:
    print('C')
elif a == b == c:
    print('*')
"""
백준 24365번 : ПЧЕЛИЧКАТА МАЯ
"""

a, b, c = map(int, input().split())
base = (a + b + c) // 3

if b == base:
    print((base-a) * 2)
elif b > base:
    print((b-base) + (2*base-a-b) * 2)
else:
    print((base-a) * 2 + (base - b))
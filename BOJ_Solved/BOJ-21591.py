"""
백준 21591번 : Laptop Sticker
"""

a, b, c, d = map(int, input().split())
if a-2 >= c and b-2 >= d:
    print(1)
else:
    print(0)
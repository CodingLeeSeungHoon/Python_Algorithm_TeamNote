"""
백준 24072번 : 帰省 (Homecoming)
"""

a, b, c = map(int, input().split())
if a <= c < b:
    print(1)
else:
    print(0)
"""
백준 16428번 : A/B - 3
"""

a, b = map(int, input().split())
if b > 0:
    print(a//b)
    print(a%b)
else:
    print(a//b + 1)
    print(a - b * (a//b + 1))
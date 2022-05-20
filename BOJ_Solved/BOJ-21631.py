"""
백준 21631번 : Checkers
"""

a, b = map(int, input().split())

if a < b:
    print(a+1)
else:
    print(b)
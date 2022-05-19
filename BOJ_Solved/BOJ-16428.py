"""
백준 16428번 : A/B - 3
"""

a, b = map(int,input().split())
c, d = a//b, a%b
if a != 0 and d < 0:
    c, d = c+1, d-b
print(c)
print(d)
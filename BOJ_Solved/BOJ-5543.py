"""
백준 5543번 : 상근날드
"""

b1 = int(input())
b2 = int(input())
b3 = int(input())
d1 = int(input())
d2 = int(input())

print(min(b1, b2, b3) + min(d1, d2) - 50)
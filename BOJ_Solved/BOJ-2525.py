"""
백준 2525번 : 오븐 시계
"""

a, b = map(int, input().split())
c = int(input())
b = b + c

mock = b // 60
b = b % 60

a = mock + a
if a >= 24:
    a = a - 24

print(a, b)
"""
백준 2530번 : 인공지능 시계
"""
a, b, c = map(int, input().split())
d = int(input())

c = c + d
add = c // 60
c = c % 60

b = b + add
add = b // 60
b = b % 60

a = a + add
a = a % 24

print(a, b, c)
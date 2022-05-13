"""
백준 10162번 : 전자레인지
"""
a = 300
b = 60
c = 10

n = int(input())
i = n // a
n -= a * i

j = n // b
n -= b * j

k = n // c
n -= c * k

if n != 0:
    print(-1)
else:
    print(i, j, k)
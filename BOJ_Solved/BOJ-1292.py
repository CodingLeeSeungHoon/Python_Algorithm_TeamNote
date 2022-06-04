"""
백준 1292번 : 쉽게 푸는 문제
"""

a, b = map(int, input().split())
num = []
for i in range(1, 1000):
    for _ in range(i):
        num.append(i)

print(sum(num[a-1:b]))
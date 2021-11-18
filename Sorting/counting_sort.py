"""
Counting sort
O(n+k)
n = input
k = max(element)
"""

from sys import stdin

num = int(stdin.readline())

# 10001을 max(element)로 두기
numbers = [0] * 10001

# counting
for _ in range(num):
    n = int(stdin.readline())
    numbers[n] += 1

for i in range(1, 10001):
    for j in range(numbers[i]):
        print(i)

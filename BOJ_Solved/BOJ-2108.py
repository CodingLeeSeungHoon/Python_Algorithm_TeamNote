"""
백준 2108번 : 통계학
"""
from collections import Counter
from sys import stdin

n = int(stdin.readline())  # 홀수

numbers = []
for _ in range(n):
    numbers.append(int(stdin.readline()))

numbers.sort()
counter = Counter(numbers)

print(round(sum(numbers) / n))
print(numbers[n // 2])

c = counter.most_common(2)
if len(c) != 1 and c[0][1] == c[1][1]:
    print(c[1][0])
else:
    print(c[0][0])

print(numbers[-1] - numbers[0])
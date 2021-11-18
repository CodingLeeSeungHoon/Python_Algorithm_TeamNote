"""
백준 10989번 : 수 정렬하기 3
counting sort 방식
"""

from sys import stdin

num = int(stdin.readline())

numbers = [0] * 10001

for _ in range(num):
    n = int(stdin.readline())
    numbers[n] += 1

for i in range(1, 10001):
    for j in range(numbers[i]):
        print(i)

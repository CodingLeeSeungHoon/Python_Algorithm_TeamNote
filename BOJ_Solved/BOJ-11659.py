"""
백준 11659번 : 구간 합 구하기 4
메모이제이션을 통해 속도를 높여야 풀이가 된다.
"""

from sys import stdin

n, m = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))
sum_nums = [0 for _ in range(n)]

for i in range(n):
    if i == 0:
        sum_nums[i] = nums[i]
    else:
        sum_nums[i] = sum_nums[i - 1] + nums[i]

for _ in range(m):
    start, end = map(int, stdin.readline( ).split( ))
    if start == 1:
        print(sum_nums[end - 1])
    else:
        print(sum_nums[end - 1] - sum_nums[start - 2])